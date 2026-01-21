# Daily Digest

Energy & Permitting Daily Digest project, compiled by Bottlenecks Labs.

## Quick Start

```bash
./digest.sh copy              # Copy content prompt to clipboard, open Claude.ai
# Paste prompt in Claude.ai, get structured content back
# Save output: pbpaste > content.txt
./digest.sh build content.txt # Generate branded HTML from content
./digest.sh view              # Open latest digest in browser
```

## Workflow

This project uses a **hybrid approach**:
1. **Research** (LLM): Claude.ai generates structured text content using the content prompt
2. **Formatting** (Python): `build_digest.py` converts the structured content to branded HTML

This separation ensures consistent HTML output regardless of which LLM generates the content.

## Project Structure

```
prompts-and-instructions/
  └── content-prompt.md       # Full research prompt for Claude.ai (outputs structured text)

digests/
  ├── energy-digest-*.html    # Generated digest HTML files
  └── html-design-template.html  # Visual reference of HTML template

build_digest.py               # Python script that converts structured content → HTML
digest.sh                     # Helper script for workflow commands
STYLE_GUIDE.md                # Bottlenecks Labs visual identity
```

## Design System

See `STYLE_GUIDE.md` for the complete Bottlenecks Labs visual identity:
- Brand colors (ink, cream, teal, coral, gold)
- Typography (DM Sans, Space Mono)
- Component patterns (cards, tables, callouts)

### Topic Tags

News items use colored topic tags (max 2 per item):

| Tag | Color | Hex |
|:----|:------|:----|
| Nuclear | Purple | `#9b59b6` |
| Data Center | Teal | `#1abc9c` |
| Grid | Orange | `#e67e22` |
| Wind | Blue | `#3498db` |
| Solar | Dark Gold | `#d4a017` |
| Storage | Green | `#27ae60` |
| Policy | Red | `#e74c3c` |

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

## Structured Content Format

The content prompt outputs structured text with section markers:

```
===TOP_DEVELOPMENTS===
- [Development] — [Summary]

===NEWS===
##SUBSECTION: Federal Regulatory Action
ITEM:
tags: [Nuclear, Policy]
title: [What Happened]
source: [Source Name]
date: [Date]
summary: [Summary]
url: [URL]

===PUBLICATIONS===
...
```

The `build_digest.py` script parses this format and generates HTML.

## Source Accuracy Rules

- Use ORIGINAL publication dates, not news coverage dates
- Title = what happened, not what article is about
- Distinguish primary sources from secondary coverage
- For reactions: label as "Re: [Original] (Date)"
- Flag uncertain facts: "(unverified)" or "(paywalled)"
