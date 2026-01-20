# Daily Digest

Energy & Permitting Daily Digest project, compiled by Bottlenecks Labs.

## Quick Start

**From your computer:**
```bash
./digest.sh copy   # Copies prompt to clipboard, opens Gemini
./digest.sh new    # Creates today's HTML file for pasting
./digest.sh view   # Opens latest digest in browser
```

**From anywhere (phone, tablet, etc.):**
1. Open the prompt from a Google Doc (copy `prompts-and-instructions/external_use-html-prompt.md`)
2. Paste into Gemini (gemini.google.com)
3. Copy the HTML output
4. Save as `.html` file, open in any browser

## Project Structure

```
prompts-and-instructions/
  ├── external_use-html-prompt.md  # Full prompt for Gemini (outputs styled HTML)
  ├── digest-prompt.md             # Prompt for local Claude Code use (outputs markdown)
  └── sources.md                   # Reference list of news sources and companies

digests/                           # Output directory for generated digests

scripts/
  ├── view_digest.py               # Convert markdown → styled HTML (local use)
  ├── review_presentation.py       # Check links in digest
  └── email_template.html          # HTML template reference
```

## Design System

See `STYLE_GUIDE.md` for the complete Bottlenecks Labs visual identity:
- Brand colors (ink, cream, teal, coral, gold)
- Typography (DM Sans, Space Mono)
- Component patterns (cards, tables, callouts)

## Digest Sections

1. Top Developments (3 key bullet points)
2. News & Statements (past 24-48 hrs)
3. Publications (past 7 days)
4. Congressional & Executive Activity
5. Business Activity
6. China
7. Macro Trends
8. What to Watch This Week
9. Grantee Activities
10. Limitations & Gaps

## Source Accuracy Rules

- Use ORIGINAL publication dates, not news coverage dates
- Title = what happened, not what article is about
- Distinguish primary sources from secondary coverage
- For reactions: label as "Re: [Original] (Date)"
- Flag uncertain facts: "(unverified)" or "(paywalled)"
