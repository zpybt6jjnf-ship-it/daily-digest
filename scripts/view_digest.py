#!/usr/bin/env python3
"""
View Daily Digest as styled HTML in browser.
No credentials required - just generates and opens the preview.
"""

import re
import sys
import webbrowser
from pathlib import Path
from datetime import datetime

SCRIPT_DIR = Path(__file__).parent
PROJECT_DIR = SCRIPT_DIR.parent
DIGESTS_DIR = PROJECT_DIR / 'digests'
TEMPLATE_PATH = SCRIPT_DIR / 'email_template.html'

# Brand colors from Bottlenecks Labs
COLORS = {
    'cream': '#faf8f5',
    'paper': '#ffffff',
    'ink': '#1a1a2e',
    'ink_light': '#4a4a5a',
    'ink_muted': '#8a8a9a',
    'teal': '#2a9d8f',
    'coral': '#e76f51',
    'gold': '#e9c46a',
    'border': '#e8e6e1',
    'border_dark': '#d4d2cd',
}


def get_latest_digest() -> Path:
    """Get the most recently modified digest file."""
    digests = list(DIGESTS_DIR.glob('energy-digest-*.md'))
    if not digests:
        raise FileNotFoundError(f"No digest files found in {DIGESTS_DIR}")
    return max(digests, key=lambda p: p.stat().st_mtime)


def parse_digest(digest_path: Path) -> dict:
    """Parse markdown digest into structured data."""
    content = digest_path.read_text()

    date_match = re.search(r'\*\*([A-Za-z]+ \d+, \d{4})\*\*', content)
    date = date_match.group(1) if date_match else datetime.now().strftime('%B %d, %Y')

    coverage_match = re.search(r'\*Coverage: (.+?)\*', content)
    coverage = coverage_match.group(1) if coverage_match else 'Recent'

    summary_match = re.search(r'^---\n\n(.+?)\n\n---', content, re.MULTILINE | re.DOTALL)
    summary = summary_match.group(1).strip() if summary_match else ''

    sections = []
    section_pattern = r'^## (.+?)$\n\n(.*?)(?=^## |\Z)'
    for match in re.finditer(section_pattern, content, re.MULTILINE | re.DOTALL):
        sections.append({'title': match.group(1).strip(), 'content': match.group(2).strip()})

    return {'date': date, 'coverage': coverage, 'summary': summary, 'sections': sections}


def format_top_developments(summary: str) -> str:
    """Format the top developments summary as HTML."""
    summary = re.sub(r'^(Three|Two|Four|Five|Several) developments? dominate:?\s*', '', summary, flags=re.IGNORECASE)

    items = re.split(r'\s*\(\d+\)\s*', summary)
    items = [item.strip().rstrip(';.') for item in items if item.strip()]

    if len(items) <= 1 and ';' in summary:
        items = [item.strip().rstrip('.') for item in summary.split(';') if item.strip()]

    if len(items) > 1:
        html = '<ul style="margin: 12px 0 0 0; padding: 0 0 0 18px;">'
        for item in items:
            html += f'<li style="margin: 0 0 8px 0; font-size: 14px; line-height: 1.5; color: {COLORS["ink"]};">{item}</li>'
        html += '</ul>'
        return html
    return f'<p style="margin: 12px 0 0 0; font-size: 14px; line-height: 1.5; color: {COLORS["ink"]};">{summary}</p>'


def render_table(table_text: str) -> str:
    """Convert markdown table to HTML."""
    lines = [l.strip() for l in table_text.strip().split('\n') if l.strip()]
    if not lines:
        return ''

    html = f'<table style="width: 100%; border-collapse: collapse; margin: 12px 0; font-size: 13px; border: 1px solid {COLORS["border"]}; border-radius: 8px;">'
    is_header = True

    for line in lines:
        if re.match(r'^\|[\s\-:]+\|$', line):
            continue
        if not line.startswith('|'):
            continue

        cells = [c.strip() for c in line.split('|')[1:-1]]

        if is_header:
            html += f'<tr style="background: {COLORS["cream"]};">'
            for cell in cells:
                html += f'<th style="padding: 10px 12px; text-align: left; font-weight: 600; color: {COLORS["ink"]}; border-bottom: 2px solid {COLORS["border_dark"]};">{cell}</th>'
            html += '</tr>'
            is_header = False
        else:
            html += '<tr>'
            for cell in cells:
                cell = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', cell)
                html += f'<td style="padding: 10px 12px; border-bottom: 1px solid {COLORS["border"]}; color: {COLORS["ink_light"]};">{cell}</td>'
            html += '</tr>'

    html += '</table>'
    return html


def render_news_section(md_content: str) -> str:
    """Render news items as styled cards."""
    items = re.split(r'(?=\*\*[^*]+\*\*\n)', md_content)
    html = ''

    for item_text in items:
        item_text = item_text.strip()
        if not item_text or item_text == '---':
            continue

        lines = item_text.split('\n')
        title_match = re.match(r'\*\*(.+?)\*\*', lines[0])
        if not title_match:
            continue

        title = title_match.group(1)
        rest = '\n'.join(lines[1:]).strip()

        source_date = ''
        description = ''
        link_url = ''

        for i, line in enumerate(rest.split('\n')):
            line = line.strip()
            if line.startswith('→') or line.startswith('->'):
                link_match = re.search(r'\[([^\]]+)\]\(([^)]+)\)', line)
                if link_match:
                    link_url = link_match.group(2)
            elif i == 0 and ('·' in line or re.match(r'^[A-Za-z].*\d{4}', line)):
                source_date = line
            elif line and not line.startswith('→'):
                description += line + ' '

        meta = f'<p style="font-family: monospace; font-size: 11px; color: {COLORS["ink_muted"]}; margin: 0 0 6px 0;">{source_date}</p>' if source_date else ''
        link = f'<p style="margin: 10px 0 0 0;"><a href="{link_url}" style="color: {COLORS["teal"]}; text-decoration: none; font-size: 12px; font-weight: 500;">Source →</a></p>' if link_url else ''

        html += f'''
            <div style="background: {COLORS['cream']}; border-radius: 8px; padding: 14px 16px; margin-bottom: 12px;">
              <p style="font-size: 14px; font-weight: 600; color: {COLORS['ink']}; margin: 0 0 4px 0;">{title}</p>
              {meta}
              <p style="font-size: 13px; line-height: 1.55; color: {COLORS['ink_light']}; margin: 0;">{description.strip()}</p>
              {link}
            </div>'''

    return html


def render_grantee_section(md_content: str) -> str:
    """Render grantee organizations as cards."""
    org_pattern = r'\*\*([^*]+)\*\*\n\n(.*?)(?=\*\*[^*]+\*\*\n|### |$)'
    matches = list(re.finditer(org_pattern, md_content, re.DOTALL))

    if not matches:
        return ''

    html = ''
    for match in matches:
        org_name = match.group(1).strip()
        org_content = match.group(2).strip()
        org_content = re.sub(r'^---$', '', org_content, flags=re.MULTILINE).strip()

        if not org_content:
            continue

        org_content = re.sub(r'\*([^*\n]+)\*', r'<em>\1</em>', org_content)
        org_content = re.sub(r'→\s*\[([^\]]+)\]\(([^)]+)\)', rf'<a href="\2" style="color: {COLORS["teal"]}; text-decoration: none; font-size: 12px;">Source →</a>', org_content)

        is_empty = 'No ' in org_content and 'identified' in org_content
        content_style = f'font-size: 12px; line-height: 1.5; color: {COLORS["ink_muted"]}; font-style: italic;' if is_empty else f'font-size: 12px; line-height: 1.5; color: {COLORS["ink_light"]};'

        items = [p.strip() for p in org_content.split('\n\n') if p.strip()]
        items_html = ''.join(f'<p style="{content_style} margin: 0 0 6px 0;">{item}</p>' for item in items)

        html += f'''
            <div style="background: {COLORS['cream']}; border-radius: 8px; padding: 12px 14px; margin-bottom: 10px;">
              <p style="font-size: 13px; font-weight: 600; color: {COLORS['ink']}; margin: 0 0 6px 0;">{org_name}</p>
              {items_html}
            </div>'''

    return html


def render_watch_section(md_content: str) -> str:
    """Render the What to Watch section."""
    html = ''

    table_match = re.search(r'(\|[^\n]+\|(?:\n\|[^\n]+\|)+)', md_content)
    if table_match:
        html += render_table(table_match.group(1))

    questions_match = re.search(r'\*\*Key Questions\*\*\n\n([\s\S]+?)(?=\n---|\n\*\*|$)', md_content)
    if questions_match:
        questions_text = questions_match.group(1).strip()
        items = re.findall(r'^\d+\.\s+(.+)$', questions_text, re.MULTILINE)

        if items:
            html += f'<div style="margin-top: 16px; padding: 14px 16px; background: {COLORS["cream"]}; border-radius: 8px; border-left: 3px solid {COLORS["gold"]};">'
            html += f'<p style="font-family: monospace; font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.08em; color: {COLORS["gold"]}; margin: 0 0 10px 0;">Key Questions</p>'
            html += f'<ol style="margin: 0; padding: 0 0 0 18px; color: {COLORS["ink_light"]};">'
            for item in items:
                html += f'<li style="margin: 0 0 6px 0; font-size: 13px; line-height: 1.5;">{item}</li>'
            html += '</ol></div>'

    return html


def render_limitations_section(md_content: str) -> str:
    """Render the limitations section."""
    html = ''
    sections = re.split(r'\*\*([^*]+)\*\*', md_content)

    intro = sections[0].strip()
    intro = re.sub(r'^---$', '', intro, flags=re.MULTILINE).strip()
    if intro:
        html += f'<p style="font-size: 12px; color: {COLORS["ink_muted"]}; font-style: italic; margin: 0 0 14px 0;">{intro}</p>'

    i = 1
    while i < len(sections):
        if i + 1 < len(sections):
            header = sections[i].strip()
            content = sections[i + 1].strip()
            content = re.sub(r'^---$', '', content, flags=re.MULTILINE)
            content = re.sub(r'^\*Compiled:.*$', '', content, flags=re.MULTILINE)
            content = re.sub(r'^\*Coverage:.*$', '', content, flags=re.MULTILINE)
            content = content.strip()

            if content:
                list_items = re.findall(r'^-\s+(.+)$', content, re.MULTILINE)
                if list_items:
                    html += f'<p style="font-size: 12px; font-weight: 600; color: {COLORS["ink"]}; margin: 0 0 6px 0;">{header}</p>'
                    html += f'<ul style="margin: 0 0 12px 0; padding: 0 0 0 18px; color: {COLORS["ink_muted"]}; font-size: 11px;">'
                    for item in list_items:
                        html += f'<li style="margin: 0 0 3px 0;">{item}</li>'
                    html += '</ul>'
        i += 2

    return html


def markdown_to_html_content(md_content: str, section_title: str = '') -> str:
    """Convert markdown section content to styled HTML."""
    md_content = re.sub(r'\n---\n', '\n', md_content)
    md_content = re.sub(r'^---$', '', md_content, flags=re.MULTILINE)

    if 'Grantee' in section_title:
        return render_grantee_section(md_content)
    if 'Limitations' in section_title:
        return render_limitations_section(md_content)
    if 'Watch' in section_title:
        return render_watch_section(md_content)
    if re.search(r'\*\*[^*]+\*\*\n[A-Za-z]', md_content):
        return render_news_section(md_content)

    # Default rendering
    html = md_content
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', html)
    html = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', rf'<a href="\2" style="color: {COLORS["teal"]}; text-decoration: none;">\1</a>', html)

    paragraphs = [p.strip() for p in html.split('\n\n') if p.strip() and p.strip() != '---']
    return ''.join(f'<p style="font-size: 13px; line-height: 1.55; color: {COLORS["ink_light"]}; margin: 0 0 10px 0;">{p}</p>' for p in paragraphs)


def render_section(section: dict) -> str:
    """Render a complete section with header and content."""
    title = section['title']
    content = markdown_to_html_content(section['content'], title)

    return f'''
          <tr>
            <td style="padding: 20px 28px;">
              <h2 style="margin: 0 0 14px 0; font-size: 16px; font-weight: 700; color: {COLORS['ink']};">
                <span style="background: linear-gradient(180deg, transparent 55%, rgba(231, 111, 81, 0.3) 55%); padding: 0 4px;">{title}</span>
              </h2>
              {content}
            </td>
          </tr>
          <tr>
            <td style="padding: 0 28px;">
              <table role="presentation" width="100%" cellpadding="0" cellspacing="0">
                <tr>
                  <td style="border-bottom: 1px dashed {COLORS['border_dark']};"></td>
                </tr>
              </table>
            </td>
          </tr>'''


def build_html(digest_data: dict) -> str:
    """Build complete HTML from digest data."""
    template = TEMPLATE_PATH.read_text()

    top_developments_html = format_top_developments(digest_data['summary'])
    sections_html = ''.join(render_section(s) for s in digest_data['sections'])

    html = template.replace('{{DATE}}', digest_data['date'])
    html = html.replace('{{TOP_DEVELOPMENTS}}', top_developments_html)
    html = html.replace('{{SECTIONS}}', sections_html)
    html = html.replace('{{COVERAGE_RANGE}}', digest_data['coverage'])

    return html


def view_digest(digest_path: Path = None, output_path: Path = None):
    """Generate HTML preview and open in browser."""
    if digest_path is None:
        digest_path = get_latest_digest()

    if output_path is None:
        output_path = SCRIPT_DIR / 'preview.html'

    print(f"Loading: {digest_path}")

    digest_data = parse_digest(digest_path)
    html = build_html(digest_data)

    output_path.write_text(html)
    print(f"Preview saved: {output_path}")

    webbrowser.open(f'file://{output_path.absolute()}')
    print("Opened in browser")

    return output_path


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description='View Daily Digest as styled HTML')
    parser.add_argument('--digest', '-d', type=Path, help='Path to digest file (default: latest)')
    parser.add_argument('--output', '-o', type=Path, help='Output HTML path (default: scripts/preview.html)')
    parser.add_argument('--no-open', action='store_true', help='Save HTML but do not open browser')
    args = parser.parse_args()

    digest_path = args.digest
    if digest_path is None:
        try:
            digest_path = get_latest_digest()
        except FileNotFoundError as e:
            print(f"Error: {e}")
            sys.exit(1)

    if not digest_path.exists():
        print(f"Error: File not found: {digest_path}")
        sys.exit(1)

    output_path = args.output or (SCRIPT_DIR / 'preview.html')

    print(f"Loading: {digest_path}")

    digest_data = parse_digest(digest_path)
    html = build_html(digest_data)

    output_path.write_text(html)
    print(f"Preview saved: {output_path}")

    if not args.no_open:
        webbrowser.open(f'file://{output_path.absolute()}')
        print("Opened in browser")


if __name__ == '__main__':
    main()
