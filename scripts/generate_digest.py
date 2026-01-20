#!/usr/bin/env python3
"""
Generate Energy & Permitting Daily Digest using Claude API.

Requires:
- ANTHROPIC_API_KEY environment variable
"""

import os
import sys
from datetime import datetime
from pathlib import Path

try:
    import anthropic
except ImportError:
    print("Error: anthropic package not installed. Run: pip install anthropic")
    sys.exit(1)

SCRIPT_DIR = Path(__file__).parent
PROJECT_DIR = SCRIPT_DIR.parent
DIGESTS_DIR = PROJECT_DIR / 'digests'
PROMPT_PATH = PROJECT_DIR / 'prompts-and-instructions' / 'digest-prompt.md'

# Ensure digests directory exists
DIGESTS_DIR.mkdir(exist_ok=True)


def get_digest_prompt() -> str:
    """Load and customize the digest prompt with today's date."""
    today = datetime.now()
    date_str = today.strftime('%B %d, %Y')
    filename = f"energy-digest-{today.strftime('%Y-%m-%d')}.md"

    prompt = f"""Generate today's Energy & Permitting Daily Digest.

DATE: {date_str}
FILENAME: {filename}

SCOPE
- Geography: US primary, China secondary
- Energy: All sectors, weighted toward electricity/grid
- Permitting: NEPA, environmental review, siting, interconnection, permitting reform

---

COVERAGE REQUIREMENTS

PRIORITY NEWS SOURCES (search each):
- Utility Dive, E&E News, RTO Insider, Canary Media, Heatmap News
- Reuters Energy, Bloomberg Energy
- FERC.gov, DOE.gov, Federal Register

COMPANY WATCHLIST (check for announcements):
- Utilities: NextEra, Duke, Southern, Dominion, AEP, Xcel, Entergy, PG&E
- IPPs: Vistra, Constellation, Talen, AES
- Transmission: ITC, ATC, GridLiance, LS Power
- Renewables: Invenergy, Apex, Ørsted, Avangrid, EDF, Pattern
- Nuclear: NuScale, TerraPower, X-energy, Kairos, Oklo, Holtec
- Tech/Data Centers: Meta, Google, Microsoft, Amazon, Oracle

RTO/ISO SOURCES (check for filings, orders):
- PJM, MISO, CAISO, ERCOT, SPP, NYISO, ISO-NE

EVENTS TO CHECK:
- FERC Open Meeting agenda/outcomes
- Congressional hearings (Senate ENR, House E&C)
- RTO board meetings
- Major comment deadlines

For each section, actively search for news from these sources rather than relying on general searches.

---

SOURCE ACCURACY RULES (CRITICAL)

1. PRIMARY vs. SECONDARY SOURCES
   - Primary: Original reports, official announcements, filings, press releases
   - Secondary: News articles, commentary, analysis about primary sources
   - ALWAYS distinguish between them. Never present secondary coverage as the primary source.

2. DATING
   - Use the ORIGINAL publication date for reports and documents, not the date of news coverage
   - If a news article from Jan 15 discusses a report from December, the report date is December
   - Format: "Report Name (December 2025)" not "Report Name · Jan 15, 2026"

3. ACCURATE TITLES
   - Title should reflect WHAT HAPPENED, not what the article is about
   - WRONG: "NPC Permitting Report" (when source is an article about company supporting the report)
   - RIGHT: "Williams Endorses NPC Permitting Report" or "Industry Reactions to NPC Permitting Report (Dec 2025)"

4. WHEN COVERING REACTIONS/COMMENTARY
   - Lead with WHO is reacting and WHAT they said
   - Reference the original source with its actual date
   - Example: "Williams CEO endorses NPC's December 2025 permitting report, calling for streamlined NEPA reviews"

5. VERIFICATION
   - If uncertain about a date or fact, say so: "(date unconfirmed)" or "(per [source])"
   - Do not guess or infer dates
   - When a source is paywalled, note: "(paywalled - summary based on available excerpt)"

6. LINK TO BEST SOURCE
   - Prefer linking to primary sources when available
   - If only secondary coverage exists, link to it but note in summary that it's coverage of [original]

---

SECTIONS

1. News & Statements (past 24-48 hrs)
Search: energy policy news, permitting reform, FERC orders, transmission projects, utility announcements, renewable energy, grid reliability, DOE announcements, offshore wind
- Focus on NEW announcements, not coverage of older items
- If covering reactions to older news, frame as reactions

2. Publications
Search: EIA, RMI, RFF, OECD, NREL, think tank reports, academic energy publications
- Only include publications actually released in past 7 days
- Use actual publication date, not discovery date

3. Congressional & Executive Activity
Search: energy bills Congress, FERC notices, Federal Register energy/environment, DOE announcements, EPA rules, BLM leasing
- Include docket numbers and filing dates where available

4. Business Activity
Search: energy project announcements, renewable PPAs, utility M&A, transmission projects, data center power deals, nuclear agreements
- Distinguish between: announced, filed, approved, completed
- Include capacity (MW), investment ($), and timeline where stated

5. China
Search: China energy policy, State Grid, NDRC energy, China renewables, China carbon market, Five-Year Plan energy

6. Macro Trends
2-3 paragraphs connecting today's items to ongoing themes (permitting stalemate, data center load growth, nuclear momentum, etc.)
- Cite specific items from this digest
- Avoid speculation; stick to observable patterns

7. What to Watch This Week
Table of upcoming deadlines, hearings, FERC meetings, court rulings, conferences. Include "Key Questions" subsection.
- Verify dates against official calendars where possible

8. Grantee Activities
Search for recent publications/statements from these organizations:
- ClearPath
- Clean Air Task Force
- Bipartisan Policy Center
- Clean Energy Buyers Alliance
- R Street Institute
- Breakthrough Institute
- Third Way
- Foundation for American Innovation
- Rainey Center
- Siting Solutions Project / Clean Tomorrow
- Electricity Customers Alliance
- American Conservation Coalition
- Niskanen Center
- Institute for Progress
- Environmental Policy Innovation Center
- RAND Corporation

Also search for similar organizations and note as "Similar Organizations"
- Only include items from past 7 days
- Link directly to organization's publication, not news coverage of it

9. Limitations & Gaps
List sources not systematically covered, potential gaps in this edition, and data freshness caveats
- Note any items where dates could not be verified
- Note paywalled sources that limited coverage

---

FORMAT

For NEWS (new announcements):
**[What Happened]**
[Source Name] · [Actual Date of Event/Announcement]
[2-3 line summary of the news]
→ [Source](url)

For REACTIONS/COMMENTARY (about existing items):
**[Who] [Action] on [Topic]**
[Publication] · [Article Date] · Re: [Original Item] ([Original Date])
[2-3 line summary focusing on the new reaction/statement]
→ [Source](url)

For PUBLICATIONS:
**[Publication Title]**
[Publisher] · [Publication Date]
[2-3 line summary of findings/recommendations]
→ [Source](url to actual publication)

Use tables for structured data (appropriations, deals, weekly calendar).
No emoji.
Horizontal rules (---) between major sections.
Each grantee organization separated by ---.

---

HEADER FORMAT
# Energy & Permitting Daily Digest
**{date_str}** · Compiled by Bottlenecks Labs

FOOTER FORMAT
---
*Compiled: {date_str}*
*Coverage: Past 24-48 hours*

STYLE: Clean, professional, data-forward. Match Bottlenecks Labs design ethos. Accuracy over comprehensiveness.

---

QUALITY CHECKLIST (verify before finalizing)
□ Each item's date reflects the actual event/publication date, not coverage date
□ Titles describe what happened, not what an article is about
□ Primary sources linked where available
□ Reactions clearly labeled as reactions, with original source referenced
□ No items older than 7 days unless noting ongoing significance
□ Uncertain facts flagged appropriately

Output only the markdown content for the digest file. Do not include any preamble or explanation."""

    return prompt


def generate_digest() -> tuple[str, str]:
    """Generate digest using Claude API with web search."""
    api_key = os.environ.get('ANTHROPIC_API_KEY')
    if not api_key:
        raise ValueError("ANTHROPIC_API_KEY environment variable not set")

    client = anthropic.Anthropic(api_key=api_key)

    prompt = get_digest_prompt()

    print("Generating digest with Claude API (this may take a few minutes)...")

    # Use Claude with web search capability
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=16000,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        tools=[
            {
                "type": "web_search_20250305",
                "name": "web_search",
                "max_uses": 25
            }
        ]
    )

    # Extract text content from response
    content = ""
    for block in response.content:
        if hasattr(block, 'text'):
            content += block.text

    # Generate filename
    today = datetime.now()
    filename = f"energy-digest-{today.strftime('%Y-%m-%d')}.md"

    return filename, content


def save_digest(filename: str, content: str) -> Path:
    """Save digest to file."""
    filepath = DIGESTS_DIR / filename
    filepath.write_text(content)
    print(f"Digest saved to: {filepath}")
    return filepath


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description='Generate Daily Digest')
    parser.add_argument('--dry-run', action='store_true', help='Generate but do not save')
    parser.add_argument('--send', action='store_true', help='Send email after generating')
    args = parser.parse_args()

    try:
        filename, content = generate_digest()

        if args.dry_run:
            print("\n--- DRY RUN ---")
            print(content[:2000])
            print("\n... (truncated)")
        else:
            filepath = save_digest(filename, content)

            if args.send:
                # Import and run send script
                from send_digest import main as send_main
                sys.argv = ['send_digest.py']  # Reset argv for send script
                send_main()

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
