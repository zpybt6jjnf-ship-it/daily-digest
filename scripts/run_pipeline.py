#!/usr/bin/env python3
"""
Unified Daily Digest Pipeline

Orchestrates the complete digest workflow:
1. Generate digest using Claude API with web search
2. Review content for accuracy and comprehensiveness
3. Review presentation (links, formatting)
4. Send via email

All review steps are advisory (non-blocking) with auto-fix enabled.
"""

import os
import sys
import json
from datetime import datetime
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
PROJECT_DIR = SCRIPT_DIR.parent
DIGESTS_DIR = PROJECT_DIR / 'digests'
LOGS_DIR = PROJECT_DIR / 'logs'

# Ensure directories exist
DIGESTS_DIR.mkdir(exist_ok=True)
LOGS_DIR.mkdir(exist_ok=True)


def log_step(step: str, status: str, details: dict = None):
    """Log a pipeline step for debugging."""
    timestamp = datetime.now().isoformat()
    log_entry = {
        'timestamp': timestamp,
        'step': step,
        'status': status,
        'details': details or {}
    }
    print(f"[{timestamp}] {step}: {status}")
    if details:
        for key, value in details.items():
            if isinstance(value, list) and len(value) > 3:
                print(f"  {key}: {value[:3]} ... ({len(value)} total)")
            else:
                print(f"  {key}: {value}")
    return log_entry


def run_pipeline(
    skip_generate: bool = False,
    skip_content_review: bool = False,
    skip_presentation_review: bool = False,
    skip_send: bool = False,
    digest_path: Path = None,
    dry_run: bool = False
):
    """
    Run the complete digest pipeline.

    Args:
        skip_generate: Use existing digest instead of generating new one
        skip_content_review: Skip content accuracy review
        skip_presentation_review: Skip link/formatting review
        skip_send: Don't send email
        digest_path: Path to existing digest (required if skip_generate)
        dry_run: Run pipeline but don't save or send anything
    """
    logs = []
    today = datetime.now()
    filename = f"energy-digest-{today.strftime('%Y-%m-%d')}.md"
    filepath = DIGESTS_DIR / filename

    warnings = []
    content_notes = {}
    presentation_report = {}

    # Step 1: Generate Digest
    if skip_generate:
        if digest_path:
            filepath = digest_path
        if not filepath.exists():
            print(f"Error: Digest not found at {filepath}")
            sys.exit(1)
        logs.append(log_step('generate', 'skipped', {'file': str(filepath)}))
    else:
        logs.append(log_step('generate', 'starting'))
        try:
            from generate_digest import generate_digest, save_digest
            filename, content = generate_digest()

            if dry_run:
                logs.append(log_step('generate', 'completed (dry run)', {'filename': filename}))
            else:
                filepath = save_digest(filename, content)
                logs.append(log_step('generate', 'completed', {'file': str(filepath)}))

        except Exception as e:
            logs.append(log_step('generate', 'failed', {'error': str(e)}))
            print(f"Error generating digest: {e}")
            sys.exit(1)

    # Step 2: Content Review (accuracy & comprehensiveness)
    if skip_content_review:
        logs.append(log_step('content_review', 'skipped'))
    else:
        logs.append(log_step('content_review', 'starting'))
        try:
            from review_content import review_content

            corrected_content, content_notes = review_content(filepath)

            if content_notes.get('warnings'):
                warnings.extend([f"Content: {w}" for w in content_notes['warnings']])

            if dry_run:
                logs.append(log_step('content_review', 'completed (dry run)', {
                    'fixes': len(content_notes.get('fixes', [])),
                    'warnings': len(content_notes.get('warnings', [])),
                    'gaps': len(content_notes.get('gaps', []))
                }))
            else:
                filepath.write_text(corrected_content)
                logs.append(log_step('content_review', 'completed', {
                    'fixes': len(content_notes.get('fixes', [])),
                    'warnings': len(content_notes.get('warnings', [])),
                    'gaps': len(content_notes.get('gaps', []))
                }))

        except Exception as e:
            logs.append(log_step('content_review', 'failed', {'error': str(e)}))
            warnings.append(f"Content review failed: {e}")
            # Continue anyway (advisory)

    # Step 3: Presentation Review (links, formatting)
    if skip_presentation_review:
        logs.append(log_step('presentation_review', 'skipped'))
    else:
        logs.append(log_step('presentation_review', 'starting'))
        try:
            from review_presentation import review_presentation

            fixed_content, presentation_report = review_presentation(filepath, fix=True)

            broken_links = presentation_report.get('broken_links', [])
            if broken_links:
                warnings.append(f"Presentation: {len(broken_links)} broken links found")

            if presentation_report.get('formatting_warnings'):
                warnings.append(f"Presentation: {len(presentation_report['formatting_warnings'])} formatting issues")

            if dry_run:
                logs.append(log_step('presentation_review', 'completed (dry run)', {
                    'links_checked': presentation_report.get('summary', {}).get('links_checked', 0),
                    'broken_links': len(broken_links),
                    'fixes_applied': len(presentation_report.get('fixes_applied', []))
                }))
            else:
                filepath.write_text(fixed_content)
                logs.append(log_step('presentation_review', 'completed', {
                    'links_checked': presentation_report.get('summary', {}).get('links_checked', 0),
                    'broken_links': len(broken_links),
                    'fixes_applied': len(presentation_report.get('fixes_applied', []))
                }))

        except Exception as e:
            logs.append(log_step('presentation_review', 'failed', {'error': str(e)}))
            warnings.append(f"Presentation review failed: {e}")
            # Continue anyway (advisory)

    # Step 4: Send Email
    if skip_send:
        logs.append(log_step('send', 'skipped'))
    else:
        logs.append(log_step('send', 'starting'))
        if dry_run:
            logs.append(log_step('send', 'completed (dry run)'))
        else:
            try:
                from send_digest import send_digest_email
                send_digest_email(filepath)
                logs.append(log_step('send', 'completed'))
            except Exception as e:
                logs.append(log_step('send', 'failed', {'error': str(e)}))
                print(f"Error sending email: {e}")
                # Don't exit - digest is still saved

    # Final Summary
    print("\n" + "="*60)
    print("PIPELINE COMPLETE")
    print("="*60)

    print(f"\nDigest: {filepath}")

    if warnings:
        print(f"\nAdvisory Warnings ({len(warnings)}):")
        for w in warnings:
            print(f"  - {w}")
    else:
        print("\nNo warnings.")

    # Save pipeline log
    if not dry_run:
        log_path = LOGS_DIR / f"pipeline-{today.strftime('%Y-%m-%d-%H%M%S')}.json"
        log_data = {
            'timestamp': today.isoformat(),
            'digest_file': str(filepath),
            'warnings': warnings,
            'steps': logs,
            'content_review': content_notes,
            'presentation_review': presentation_report,
        }
        log_path.write_text(json.dumps(log_data, indent=2, default=str))
        print(f"Log saved: {log_path}")

    return filepath, warnings


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description='Run the complete Daily Digest pipeline',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run full pipeline
  python run_pipeline.py

  # Review and send existing digest
  python run_pipeline.py --skip-generate --digest path/to/digest.md

  # Generate only (no review, no send)
  python run_pipeline.py --skip-content-review --skip-presentation-review --skip-send

  # Dry run to test pipeline
  python run_pipeline.py --dry-run
        """
    )
    parser.add_argument('--skip-generate', action='store_true',
                        help='Use existing digest instead of generating')
    parser.add_argument('--skip-content-review', action='store_true',
                        help='Skip content accuracy review')
    parser.add_argument('--skip-presentation-review', action='store_true',
                        help='Skip link/formatting review')
    parser.add_argument('--skip-send', action='store_true',
                        help='Do not send email')
    parser.add_argument('--digest', '-d', type=Path,
                        help='Path to existing digest (use with --skip-generate)')
    parser.add_argument('--dry-run', action='store_true',
                        help='Run pipeline without saving or sending')

    args = parser.parse_args()

    if args.skip_generate and not args.digest:
        # Check for today's digest
        today = datetime.now()
        default_path = DIGESTS_DIR / f"energy-digest-{today.strftime('%Y-%m-%d')}.md"
        if not default_path.exists():
            parser.error("--skip-generate requires --digest or today's digest to exist")
        args.digest = default_path

    run_pipeline(
        skip_generate=args.skip_generate,
        skip_content_review=args.skip_content_review,
        skip_presentation_review=args.skip_presentation_review,
        skip_send=args.skip_send,
        digest_path=args.digest,
        dry_run=args.dry_run
    )


if __name__ == '__main__':
    main()
