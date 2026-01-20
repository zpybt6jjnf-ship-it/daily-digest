#!/usr/bin/env python3
"""
Review digest content for accuracy and comprehensiveness.
Auto-fixes issues where possible, flags others.
"""

import os
import re
import sys
from pathlib import Path
from datetime import datetime

try:
    import anthropic
except ImportError:
    print("Error: anthropic package not installed. Run: pip install anthropic")
    sys.exit(1)

SCRIPT_DIR = Path(__file__).parent
PROJECT_DIR = SCRIPT_DIR.parent
SOURCES_PATH = PROJECT_DIR / 'prompts-and-instructions' / 'sources.md'


def load_sources_config() -> str:
    """Load the sources configuration for reference."""
    if SOURCES_PATH.exists():
        return SOURCES_PATH.read_text()
    return ""


def get_review_prompt(digest_content: str, sources_config: str) -> str:
    """Generate the content review prompt."""
    return f"""You are a fact-checker and editor reviewing an auto-generated Energy & Permitting Daily Digest.

Your task is to:
1. Check for accuracy issues and FIX them
2. Check for comprehensiveness gaps and NOTE them
3. Return the corrected digest

---

ACCURACY CHECKS (fix these):

1. DATE ACCURACY
   - Verify dates match actual events, not article publication dates
   - If a news article from Jan 15 discusses a December report, the report date should be December
   - Fix any dates that appear to be article dates rather than event dates

2. TITLE ACCURACY
   - Titles should describe WHAT HAPPENED, not what an article is about
   - WRONG: "NPC Permitting Report" (when it's actually an article about reactions to the report)
   - RIGHT: "Williams CEO Endorses NPC Permitting Recommendations"
   - Fix misleading titles

3. SOURCE ATTRIBUTION
   - Primary sources (reports, announcements) should be distinguished from secondary coverage
   - If an item is about reactions/commentary, it should be labeled as such
   - Add "Re: [Original] ([Date])" for reaction pieces

4. FACTUAL CLAIMS
   - Check that numbers (MW, $, dates) appear plausible
   - Flag any claims that seem unlikely or unverifiable
   - Add "(unverified)" to suspicious claims

5. DUPLICATE CONTENT
   - Remove or consolidate duplicate stories
   - If same event covered multiple times, keep the best version

---

COMPREHENSIVENESS CHECKS (note in Limitations section):

Review against this source configuration:
{sources_config[:3000]}

Check if these were likely covered:
- Major utility announcements (NextEra, Duke, Southern, Dominion, etc.)
- FERC orders and notices
- RTO/ISO filings (PJM, MISO, CAISO, ERCOT)
- Congressional activity
- Nuclear developments (NuScale, TerraPower, Constellation, etc.)
- Data center/tech company energy deals

Note any obvious gaps in the Limitations section.

---

DIGEST TO REVIEW:

{digest_content}

---

OUTPUT INSTRUCTIONS:

1. Return the COMPLETE corrected digest (not just the changes)
2. At the very end, after the digest, add a section:

---
## Review Notes (Internal - Remove Before Sending)

**Issues Fixed:**
- [List each fix made]

**Warnings:**
- [List any issues that couldn't be auto-fixed]

**Coverage Gaps Noted:**
- [List any sources/topics that appear missing]
---

Return the full corrected digest with review notes appended."""


def review_content(digest_path: Path) -> tuple[str, dict]:
    """Review digest content and return corrected version with review notes."""
    api_key = os.environ.get('ANTHROPIC_API_KEY')
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY environment variable not set")

    client = anthropic.Anthropic(api_key=api_key)

    digest_content = digest_path.read_text()
    sources_config = load_sources_config()

    prompt = get_review_prompt(digest_content, sources_config)

    print("Reviewing content for accuracy and comprehensiveness...")

    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=16000,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    # Extract text content
    result = ""
    for block in response.content:
        if hasattr(block, 'text'):
            result += block.text

    # Parse out review notes
    review_notes = {}
    if "## Review Notes" in result:
        parts = result.split("## Review Notes")
        corrected_digest = parts[0].strip()
        notes_section = parts[1] if len(parts) > 1 else ""

        # Extract individual note sections
        if "**Issues Fixed:**" in notes_section:
            match = re.search(r'\*\*Issues Fixed:\*\*\n(.*?)(?=\*\*|$)', notes_section, re.DOTALL)
            if match:
                review_notes['fixes'] = [l.strip('- \n') for l in match.group(1).strip().split('\n') if l.strip('- \n')]

        if "**Warnings:**" in notes_section:
            match = re.search(r'\*\*Warnings:\*\*\n(.*?)(?=\*\*|$)', notes_section, re.DOTALL)
            if match:
                review_notes['warnings'] = [l.strip('- \n') for l in match.group(1).strip().split('\n') if l.strip('- \n')]

        if "**Coverage Gaps Noted:**" in notes_section:
            match = re.search(r'\*\*Coverage Gaps Noted:\*\*\n(.*?)(?=\*\*|---|$)', notes_section, re.DOTALL)
            if match:
                review_notes['gaps'] = [l.strip('- \n') for l in match.group(1).strip().split('\n') if l.strip('- \n')]
    else:
        corrected_digest = result

    # Clean up any remaining review notes markers
    corrected_digest = re.sub(r'\n---\n## Review Notes.*$', '', corrected_digest, flags=re.DOTALL)

    return corrected_digest, review_notes


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description='Review digest content for accuracy')
    parser.add_argument('--digest', '-d', type=Path, required=True, help='Path to digest file')
    parser.add_argument('--output', '-o', type=Path, help='Output path (default: overwrite input)')
    parser.add_argument('--dry-run', action='store_true', help='Print changes without saving')
    args = parser.parse_args()

    if not args.digest.exists():
        print(f"Error: Digest file not found: {args.digest}")
        sys.exit(1)

    try:
        corrected_digest, review_notes = review_content(args.digest)

        # Print review summary
        print("\n" + "="*50)
        print("CONTENT REVIEW COMPLETE")
        print("="*50)

        if review_notes.get('fixes'):
            print(f"\n✓ Issues Fixed ({len(review_notes['fixes'])}):")
            for fix in review_notes['fixes'][:10]:
                print(f"  - {fix}")
            if len(review_notes['fixes']) > 10:
                print(f"  ... and {len(review_notes['fixes']) - 10} more")

        if review_notes.get('warnings'):
            print(f"\n⚠ Warnings ({len(review_notes['warnings'])}):")
            for warning in review_notes['warnings']:
                print(f"  - {warning}")

        if review_notes.get('gaps'):
            print(f"\n○ Coverage Gaps Noted ({len(review_notes['gaps'])}):")
            for gap in review_notes['gaps'][:5]:
                print(f"  - {gap}")

        if args.dry_run:
            print("\n[DRY RUN - No changes saved]")
        else:
            output_path = args.output or args.digest
            output_path.write_text(corrected_digest)
            print(f"\n✓ Saved to: {output_path}")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
