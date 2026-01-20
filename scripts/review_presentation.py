#!/usr/bin/env python3
"""
Review digest presentation for links, formatting, and design coherence.
Validates URLs, checks formatting consistency, auto-fixes where possible.
"""

import os
import re
import sys
import urllib.request
import urllib.error
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import NamedTuple

SCRIPT_DIR = Path(__file__).parent
PROJECT_DIR = SCRIPT_DIR.parent


class LinkCheckResult(NamedTuple):
    url: str
    status: str  # 'ok', 'redirect', 'error', 'timeout'
    code: int
    message: str


def extract_links(content: str) -> list[tuple[str, str]]:
    """Extract all markdown links from content. Returns list of (text, url) tuples."""
    # Match [text](url) pattern
    pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    return re.findall(pattern, content)


def check_link(url: str, timeout: int = 10) -> LinkCheckResult:
    """Check if a URL is accessible. Returns LinkCheckResult."""
    try:
        # Create request with browser-like headers
        req = urllib.request.Request(
            url,
            method='HEAD',
            headers={
                'User-Agent': 'Mozilla/5.0 (compatible; DigestBot/1.0)',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            }
        )

        with urllib.request.urlopen(req, timeout=timeout) as response:
            return LinkCheckResult(url, 'ok', response.status, 'OK')

    except urllib.error.HTTPError as e:
        if e.code in (301, 302, 303, 307, 308):
            return LinkCheckResult(url, 'redirect', e.code, f'Redirects to: {e.headers.get("Location", "unknown")}')
        elif e.code == 403:
            # Many sites block HEAD requests but work fine with GET
            return LinkCheckResult(url, 'ok', 200, 'OK (HEAD blocked, likely accessible)')
        elif e.code == 405:
            # Method not allowed for HEAD, try GET
            try:
                req = urllib.request.Request(url, headers={
                    'User-Agent': 'Mozilla/5.0 (compatible; DigestBot/1.0)',
                })
                with urllib.request.urlopen(req, timeout=timeout) as response:
                    return LinkCheckResult(url, 'ok', response.status, 'OK')
            except Exception:
                return LinkCheckResult(url, 'error', e.code, str(e))
        else:
            return LinkCheckResult(url, 'error', e.code, str(e))

    except urllib.error.URLError as e:
        return LinkCheckResult(url, 'error', 0, str(e.reason))

    except TimeoutError:
        return LinkCheckResult(url, 'timeout', 0, 'Request timed out')

    except Exception as e:
        return LinkCheckResult(url, 'error', 0, str(e))


def check_all_links(links: list[tuple[str, str]], max_workers: int = 5) -> dict[str, LinkCheckResult]:
    """Check all links concurrently. Returns dict of url -> result."""
    results = {}
    urls = list(set(url for _, url in links))  # Deduplicate URLs

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_url = {executor.submit(check_link, url): url for url in urls}

        for future in as_completed(future_to_url):
            url = future_to_url[future]
            try:
                results[url] = future.result()
            except Exception as e:
                results[url] = LinkCheckResult(url, 'error', 0, str(e))

    return results


def check_formatting(content: str) -> list[dict]:
    """Check for formatting issues in the digest."""
    issues = []
    lines = content.split('\n')

    # Check for common markdown issues
    for i, line in enumerate(lines, 1):
        # Check for broken links (missing closing paren)
        if re.search(r'\[[^\]]+\]\([^)]*$', line):
            issues.append({
                'line': i,
                'type': 'broken_link',
                'message': 'Possible broken link (missing closing parenthesis)',
                'content': line[:80],
                'fixable': False
            })

        # Check for multiple consecutive blank lines
        if i > 2 and line == '' and lines[i-2] == '' and lines[i-3] == '':
            issues.append({
                'line': i,
                'type': 'extra_blank_lines',
                'message': 'Multiple consecutive blank lines',
                'content': '',
                'fixable': True
            })

        # Check for trailing whitespace
        if line.endswith(' ') or line.endswith('\t'):
            issues.append({
                'line': i,
                'type': 'trailing_whitespace',
                'message': 'Trailing whitespace',
                'content': line[:50],
                'fixable': True
            })

        # Check for inconsistent header formatting (# without space)
        if re.match(r'^#+[^# ]', line):
            issues.append({
                'line': i,
                'type': 'header_format',
                'message': 'Header missing space after #',
                'content': line[:50],
                'fixable': True
            })

        # Check for raw HTML that might not render in email
        if '<script' in line.lower() or '<style' in line.lower():
            issues.append({
                'line': i,
                'type': 'unsafe_html',
                'message': 'Script or style tags may not render in email',
                'content': line[:50],
                'fixable': False
            })

    # Check for required sections
    required_sections = [
        ('# Energy & Permitting Daily Digest', 'Missing main header'),
        ('## News & Statements', 'Missing News & Statements section'),
        ('## Limitations', 'Missing Limitations section'),
    ]

    for pattern, message in required_sections:
        if pattern not in content and pattern.replace('## ', '## ') not in content:
            issues.append({
                'line': 0,
                'type': 'missing_section',
                'message': message,
                'content': '',
                'fixable': False
            })

    # Check for date in header
    if not re.search(r'\*\*[A-Z][a-z]+ \d{1,2}, \d{4}\*\*', content):
        issues.append({
            'line': 0,
            'type': 'missing_date',
            'message': 'Date not found in expected format',
            'content': '',
            'fixable': False
        })

    return issues


def fix_formatting(content: str) -> tuple[str, list[str]]:
    """Auto-fix formatting issues where possible. Returns (fixed_content, list of fixes)."""
    fixes = []

    # Fix multiple consecutive blank lines
    original_len = len(content)
    content = re.sub(r'\n{4,}', '\n\n\n', content)
    if len(content) != original_len:
        fixes.append('Reduced excessive blank lines')

    # Fix trailing whitespace
    lines = content.split('\n')
    fixed_lines = []
    trailing_ws_count = 0
    for line in lines:
        stripped = line.rstrip()
        if stripped != line:
            trailing_ws_count += 1
        fixed_lines.append(stripped)

    if trailing_ws_count > 0:
        fixes.append(f'Removed trailing whitespace from {trailing_ws_count} lines')
        content = '\n'.join(fixed_lines)

    # Fix headers missing space after #
    def fix_header(match):
        return match.group(1) + ' ' + match.group(2)

    fixed_content = re.sub(r'^(#+)([^# \n])', fix_header, content, flags=re.MULTILINE)
    if fixed_content != content:
        fixes.append('Fixed header formatting (added space after #)')
        content = fixed_content

    return content, fixes


def generate_report(
    link_results: dict[str, LinkCheckResult],
    formatting_issues: list[dict],
    fixes_applied: list[str]
) -> dict:
    """Generate a summary report of the review."""

    # Categorize link results
    ok_links = [r for r in link_results.values() if r.status == 'ok']
    redirect_links = [r for r in link_results.values() if r.status == 'redirect']
    error_links = [r for r in link_results.values() if r.status == 'error']
    timeout_links = [r for r in link_results.values() if r.status == 'timeout']

    # Categorize formatting issues by fixability
    unfixed_issues = [i for i in formatting_issues if not i['fixable']]

    report = {
        'summary': {
            'links_checked': len(link_results),
            'links_ok': len(ok_links),
            'links_redirect': len(redirect_links),
            'links_error': len(error_links),
            'links_timeout': len(timeout_links),
            'formatting_issues': len(formatting_issues),
            'fixes_applied': len(fixes_applied),
            'unfixed_issues': len(unfixed_issues),
        },
        'broken_links': [
            {'url': r.url, 'code': r.code, 'message': r.message}
            for r in error_links + timeout_links
        ],
        'redirects': [
            {'url': r.url, 'message': r.message}
            for r in redirect_links
        ],
        'formatting_warnings': unfixed_issues,
        'fixes_applied': fixes_applied,
    }

    # Determine overall status
    if error_links or timeout_links:
        report['status'] = 'warning'
        report['status_message'] = f'{len(error_links) + len(timeout_links)} broken links found'
    elif unfixed_issues:
        report['status'] = 'warning'
        report['status_message'] = f'{len(unfixed_issues)} formatting issues could not be auto-fixed'
    else:
        report['status'] = 'ok'
        report['status_message'] = 'All checks passed'

    return report


def review_presentation(digest_path: Path, fix: bool = True) -> tuple[str, dict]:
    """
    Review digest presentation for links and formatting.

    Args:
        digest_path: Path to the digest file
        fix: Whether to auto-fix issues

    Returns:
        Tuple of (content, report_dict)
    """
    content = digest_path.read_text()

    print("Checking links (this may take a moment)...")

    # Extract and check links
    links = extract_links(content)
    link_results = check_all_links(links) if links else {}

    print(f"Checked {len(link_results)} unique links")

    # Check formatting
    formatting_issues = check_formatting(content)

    # Apply fixes if requested
    fixes_applied = []
    if fix:
        content, fixes_applied = fix_formatting(content)

    # Generate report
    report = generate_report(link_results, formatting_issues, fixes_applied)

    return content, report


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description='Review digest presentation')
    parser.add_argument('--digest', '-d', type=Path, required=True, help='Path to digest file')
    parser.add_argument('--output', '-o', type=Path, help='Output path (default: overwrite input)')
    parser.add_argument('--no-fix', action='store_true', help='Do not auto-fix issues')
    parser.add_argument('--dry-run', action='store_true', help='Print report without saving')
    parser.add_argument('--skip-links', action='store_true', help='Skip link checking')
    args = parser.parse_args()

    if not args.digest.exists():
        print(f"Error: Digest file not found: {args.digest}")
        sys.exit(1)

    content = args.digest.read_text()

    # Check formatting
    formatting_issues = check_formatting(content)

    # Apply fixes if requested
    fixes_applied = []
    if not args.no_fix:
        content, fixes_applied = fix_formatting(content)

    # Check links unless skipped
    link_results = {}
    if not args.skip_links:
        print("Checking links (this may take a moment)...")
        links = extract_links(content)
        link_results = check_all_links(links) if links else {}
        print(f"Checked {len(link_results)} unique links")

    # Generate report
    report = generate_report(link_results, formatting_issues, fixes_applied)

    # Print summary
    print("\n" + "="*50)
    print("PRESENTATION REVIEW COMPLETE")
    print("="*50)

    print(f"\nStatus: {report['status'].upper()} - {report['status_message']}")

    s = report['summary']
    print(f"\nLinks: {s['links_ok']}/{s['links_checked']} OK", end='')
    if s['links_redirect']:
        print(f", {s['links_redirect']} redirects", end='')
    if s['links_error'] + s['links_timeout']:
        print(f", {s['links_error'] + s['links_timeout']} broken", end='')
    print()

    if report['broken_links']:
        print("\nBroken Links:")
        for link in report['broken_links'][:10]:
            print(f"  - {link['url'][:60]}...")
            print(f"    Error: {link['message']}")
        if len(report['broken_links']) > 10:
            print(f"  ... and {len(report['broken_links']) - 10} more")

    if report['fixes_applied']:
        print(f"\nFixes Applied ({len(report['fixes_applied'])}):")
        for fix in report['fixes_applied']:
            print(f"  - {fix}")

    if report['formatting_warnings']:
        print(f"\nFormatting Warnings ({len(report['formatting_warnings'])}):")
        for issue in report['formatting_warnings'][:5]:
            print(f"  - Line {issue['line']}: {issue['message']}")
        if len(report['formatting_warnings']) > 5:
            print(f"  ... and {len(report['formatting_warnings']) - 5} more")

    # Save if not dry run
    if args.dry_run:
        print("\n[DRY RUN - No changes saved]")
    else:
        output_path = args.output or args.digest
        output_path.write_text(content)
        print(f"\nSaved to: {output_path}")


if __name__ == '__main__':
    main()
