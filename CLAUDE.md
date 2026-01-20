# Daily Digest

Energy & Permitting Daily Digest project, compiled by Bottlenecks Labs.

**Design System:** See `STYLE_GUIDE.md` for the complete Bottlenecks Labs visual identity.
**Automation:** See `AUTOMATION.md` for GitHub Actions setup.

## Quick Start

```bash
# Manual: Generate digest with Claude API
python scripts/generate_digest.py

# Manual: Preview email
python scripts/send_digest.py --preview

# Manual: Send email
python scripts/send_digest.py

# Automated: Runs daily via GitHub Actions (see AUTOMATION.md)
```

## Project Structure

- `prompts-and-instructions/` - Master prompt template for generating digests
- `digests/` - Output directory for generated digest files
- `scripts/` - Generation and email scripts
- `.github/workflows/` - GitHub Actions automation

## Automation

The digest runs automatically at 6am ET daily via GitHub Actions:
1. Calls Claude API with web search to gather news
2. Generates markdown digest
3. Sends formatted HTML email
4. Commits digest to repo

Setup: See `AUTOMATION.md`

## Email Setup (Manual)

1. Enable 2-Factor Authentication on your Google account
2. Generate an App Password: https://myaccount.google.com/apppasswords
3. Copy `.env.example` to `.env` and fill in credentials

## Digest Sections

1. News & Statements (past 24-48 hrs)
2. Publications (EIA, RMI, RFF, OECD, NREL, think tanks)
3. Congressional & Executive Activity
4. Business Activity
5. China
6. Macro Trends
7. What to Watch This Week
8. Grantee Activities
9. Limitations & Gaps

## Style Guidelines

- Clean, professional, data-forward
- No emoji
- Use tables for structured data
- Horizontal rules (`---`) between major sections
