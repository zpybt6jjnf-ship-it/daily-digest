ENERGY & PERMITTING DAILY DIGEST — CONTENT PROMPT

Copy everything below this line and paste into Claude.ai or Gemini:

————————————————————————————————

# 1. TASK OVERVIEW

Generate today's Energy & Permitting Daily Digest: a structured news briefing covering US energy policy, grid/transmission, permitting, and China developments.

**DATE:** [Today's date]

**SCOPE:**
- Geography: US primary, China secondary
- Energy: All sectors, weighted toward electricity/grid
- Permitting: NEPA, environmental review, siting, interconnection queues, permitting reform

---

# 2. DATE BOUNDARIES (Calculate First)

Before doing ANY searches, calculate and write down these boundaries:

```
TODAY'S DATE:        _______________
NEWS CUTOFF:         _______________ (Today minus 3 days)
PUBLICATION CUTOFF:  _______________ (Today minus 7 days)
```

**Example:** If today is January 20, 2026:
- News window: January 17-20, 2026 ONLY
- Publications/Grantees window: January 13-20, 2026 ONLY

┌─────────────────────────────────────────────────────────────────────────────┐
│ TIME WINDOWS (ABSOLUTE — NO EXCEPTIONS)                                    │
│                                                                             │
│   News & Statements:     72 hours (3 days) — HARD CUTOFF                   │
│   Publications:          7 days — HARD CUTOFF                              │
│   Grantee Activities:    7 days — HARD CUTOFF                              │
│                                                                             │
│   An item dated January 5 CANNOT appear in a January 20 digest.            │
│   "Relevance" and "importance" do NOT override date requirements.          │
└─────────────────────────────────────────────────────────────────────────────┘

---

# 3. OUTPUT FORMAT

Your output must follow this exact structure. Review this format BEFORE searching so you know what you're building toward.

```
===TOP_DEVELOPMENTS===
- [First major development] — [Brief summary]
- [Second major development] — [Brief summary]
- [Third major development] — [Brief summary]

===NEWS===

##SUBSECTION: Federal Regulatory Action

ITEM:
tags: [tag1, tag2]
significance: high
title: [What Happened — descriptive title]
source: [Source Name]
date: [Date]
summary: [2-3 sentence summary with key numbers and implications]
url: [Full URL]

##SUBSECTION: Grid & Markets

ITEM:
...

##SUBSECTION: [Other subsections as needed: Offshore Wind, Nuclear, etc.]

===PUBLICATIONS===

ITEM:
tags: []
significance: medium
title: [Publication Title]
source: [Publisher]
date: [Publication Date]
summary: [Key findings/recommendations]
url: [URL]

===CONGRESSIONAL===

ITEM:
tags: []
significance: high
title: [What Happened]
source: [Source]
date: [Date]
summary: [Summary with docket numbers if available]
url: [URL]

===BUSINESS===

ITEM:
tags: [Nuclear, Data Center, Grid, Wind, Solar, Storage, Policy]
significance: high
title: [What Happened]
source: [Source]
date: [Date]
summary: [Include MW, $, timelines where stated]
url: [URL]

===CHINA===

ITEM:
tags: []
significance: medium
title: [Title]
source: [Source]
date: [Date]
summary: [Summary]
url: [URL]

===MACRO_TRENDS===
**[Theme 1 name].** [2-3 sentences analyzing the trend, citing specific items from this digest.]

**[Theme 2 name].** [2-3 sentences on second major theme.]

**[Theme 3 name].** [2-3 sentences on third theme.]

===MARKET_CONTEXT===
[Optional — include only if market moves are notable]
- Oil prices: [Brief note]
- Natural gas: [Henry Hub or regional price context]

===CALENDAR===

| Date | Event | Significance |
|------|-------|--------------|
| [Date] | [Event] | [Why it matters] |

===KEY_QUESTIONS===
- [First question to watch]
- [Second question]
- [Third question]

===GRANTEES===

ORG: [Organization Name]
title: [Publication Title]
date: [Date]
summary: [1-2 sentence summary of findings, not just a quote]
url: [URL]

NO_PUBLICATIONS: [Org1], [Org2], [Org3]...

===LIMITATIONS===
- [Limitation 1: e.g., Paywalled sources not fully accessible]
- [Limitation 2]
- Grantee orgs searched: All 21
```

**VALID TAGS** (use max 2 per item):
Nuclear, Data Center, Grid, Wind, Solar, Storage, Policy

---

# 4. WORKFLOW

Execute these steps IN ORDER:

## Step 1: Calculate Date Boundaries
Fill in the date boundaries in Section 2 above. All subsequent work depends on these cutoffs.

## Step 2: Search for News (72-hour window)
Search for news using queries from Appendix A. For each search result:
1. Find the EXACT publication date on the source
2. Check: Is date ≥ news cutoff?
3. If YES → note for potential inclusion
4. If NO or UNCERTAIN → skip

**Include specific dates in search queries** (e.g., "FERC order January 18 2026")

## Step 3: Search for Publications (7-day window)
Search EIA, NREL, think tanks, etc. Apply same date verification.

## Step 4: Search All 21 Grantee Organizations (7-day window)
Search EVERY organization listed in Appendix B. No exceptions.
- Search format: "[Org Name] energy [month year]"
- Verify dates before including
- Track all orgs searched

## Step 5: Verify Every Item
Before adding ANY item to your output, complete this check:
```
□ Date verified from source: _____
□ Date ≥ cutoff: YES / NO
□ URL accessible and matches summary: YES / NO
```
If any answer is NO or uncertain → EXCLUDE the item.

## Step 6: Compile Output
- Organize items into the format from Section 3
- Assign significance scores (high/medium/low)
- Select top 3 highest-significance items for TOP_DEVELOPMENTS
- List grantees with no publications in NO_PUBLICATIONS
- Note limitations and gaps

## Step 7: Final Date Audit
Before submitting, verify EVERY item one more time:
```
NEWS items (must be ≥ news cutoff):
[ ] Item 1: Date _____ ≥ Cutoff _____ ? YES/NO
[ ] Item 2: Date _____ ≥ Cutoff _____ ? YES/NO
...

PUBLICATIONS (must be ≥ publication cutoff):
[ ] Item 1: Date _____ ≥ Cutoff _____ ? YES/NO
...

GRANTEES (must be ≥ publication cutoff):
[ ] Item 1: Date _____ ≥ Cutoff _____ ? YES/NO
...
```
REMOVE any item that fails this audit.

---

# 5. SECTION REQUIREMENTS

## TOP_DEVELOPMENTS
- 3 bullet points featuring the highest-significance items from the digest
- Should reflect items scored as "high" significance

## NEWS & STATEMENTS (72-hour window ONLY)
Organize into subsections:
- Federal Regulatory Action
- Grid & Markets
- Offshore Wind (if applicable)
- Nuclear Developments (if applicable)
- Other subsections as needed

Requirements:
- Every item MUST have a verified date within 72-hour window
- Focus on NEW announcements, not coverage of older items
- If covering reactions to older news, frame as reactions
- Add topic tags to relevant items

## PUBLICATIONS (7-day window ONLY)
- Use the document's PUBLICATION date, not discovery date
- If a Jan 15 article discusses a December report, the report is OUTSIDE the window

## CONGRESSIONAL & EXECUTIVE ACTIVITY
- Include docket numbers and filing dates where available
- If no activity within window: "No significant congressional or executive activity within the 72-hour window."

## BUSINESS ACTIVITY
- Include MW, $, timelines where stated
- Distinguish between: announced, filed, approved, completed
- Add topic tags

## CHINA
- If no China news within window: "No significant China energy developments within the 72-hour window." May note relevant background context.

## MACRO TRENDS
- 2-3 paragraphs connecting items to ongoing themes
- MUST cite specific items from this digest
- Avoid speculation; stick to observable patterns

## MARKET CONTEXT (Optional)
- Include only if market moves help contextualize the day's stories

## CALENDAR
- Upcoming deadlines, hearings, FERC meetings, court rulings, conferences
- Verify dates against official calendars

## GRANTEES
- Search ALL 21 organizations (see Appendix B)
- Only include items with verified dates in 7-day window
- List organizations with no recent publications in NO_PUBLICATIONS line

## LIMITATIONS
- List sources not systematically covered
- Note paywalled sources that limited coverage
- Confirm: "Grantee orgs searched: All 21"

## EMPTY SECTION HANDLING
- If 0 items within window: Include header + "No significant developments within the [72-hour/7-day] window."
- If only 1-2 marginal items: "Light news day for [topic]"
- NEVER omit a required section — always include header with explanation

---

# 6. VERIFICATION RULES

## Date Verification (MANDATORY FOR EVERY ITEM)

Before including ANY item:
1. Find the EXACT date (day, month, year) on the source
2. Calculate: Is [item date] ≥ [cutoff date]?
3. If YES and verified → include
4. If NO or UNCERTAIN → EXCLUDE

**Exclusion triggers** (if ANY apply, do not include):
- Date is before the calculated cutoff
- Date cannot be verified from the source itself
- Date is vague (e.g., "January 2026" without specific day)
- Only the news coverage date is available, not the event date
- URL is inaccessible or content doesn't match

**What to do instead:**
- If older item provides context → mention briefly in a newer item's summary
- If no items meet criteria → note "Light news day" or "No significant developments"

## Source Accuracy

**Primary vs. Secondary Sources:**
- Primary: Original reports, official announcements, filings, press releases
- Secondary: News articles, commentary about primary sources
- Always distinguish between them

**Dating:**
- Use ORIGINAL publication date for reports/documents
- If a Jan 15 article discusses a December report → report date is December (outside window)

**Titles:**
- Describe WHAT HAPPENED, not what an article is about
- WRONG: "NPC Permitting Report"
- RIGHT: "Williams Endorses NPC Permitting Report"

**Deduplication:**
- Each story appears in ONE section only
- Pick the most relevant section; mention secondary angles in summary

## Significance Scoring

Assign to each NEWS, BUSINESS, and CONGRESSIONAL item:

**HIGH** — Any of these apply:
- Scale: $1B+, 1GW+, affects 500,000+ customers
- Precedent: "first," "largest," "landmark," "historic"
- Policy shift: Major FERC order, court ruling, legislation passed
- Market signal: Major company entering/exiting, significant M&A
- Immediate impact: Project approved, begins operation, construction starts
- Story appears in 3+ major sources

**MEDIUM:**
- Notable but not exceptional ($100M-$1B, 100MW-1GW)
- Incremental progress on known projects
- Regulatory filings or proposals (not final decisions)
- Regional significance

**LOW:**
- Routine updates, minor milestones
- Commentary without new information
- Local projects with limited broader implications

---

# APPENDIX A: Sources & Search Guidance

## Priority News Sources

**Trade Publications:**
- Utility Dive (utility industry, regulation) - utilitydive.com
- E&E News Energywire (energy policy, Congress) - eenews.net
- E&E News Greenwire (environmental policy) - eenews.net
- RTO Insider (wholesale markets, RTOs) - rtoinsider.com
- S&P Global Platts (commodities, markets) - spglobal.com/platts
- Canary Media (clean energy) - canarymedia.com
- Heatmap News (climate, energy policy) - heatmap.news
- Power Magazine (generation, grid tech) - powermag.com
- Solar Power World - solarpowerworldonline.com
- Renewable Energy World - renewableenergyworld.com
- Nuclear Newswire - ans.org/news
- Natural Gas Intelligence - naturalgasintel.com
- Transmission Hub - transmissionhub.com

**Wire Services:**
Reuters Energy, Bloomberg Energy, Wall Street Journal, Politico Pro Energy, The Hill Energy

**Government Sources:**
- FERC.gov (orders, notices, meeting agendas)
- DOE.gov (announcements, funding, reports)
- EIA.gov (data releases, analyses)
- EPA.gov (rules, permits, enforcement)
- BLM.gov (leasing, ROW permits)
- CEQ.gov (NEPA guidance)
- Federal Register (proposed/final rules)
- Congress.gov (bills, hearings)

**State-Level Sources:**
- California: CPUC, CEC
- Texas: PUCT, ERCOT
- New York: NYSPSC, NYSERDA
- PJM states: State utility commission announcements

**RTO/ISO Sources:**
- PJM (Mid-Atlantic, Midwest) - pjm.com
- MISO (Midwest, South) - misoenergy.org
- CAISO (California) - caiso.com
- ERCOT (Texas) - ercot.com
- SPP (Central US) - spp.org
- NYISO (New York) - nyiso.com
- ISO-NE (New England) - iso-ne.com

## Company Watchlist

**Investor-Owned Utilities (Top 20):**
NextEra Energy, Duke Energy, Southern Company, Dominion Energy, American Electric Power, Xcel Energy, Entergy, WEC Energy, Evergy, Ameren, CenterPoint, DTE Energy, Consumers Energy, PPL Corporation, Eversource, National Grid, Pacific Gas & Electric, Edison International, Pinnacle West/APS, NRG Energy

**Independent Power Producers:**
Vistra, Constellation Energy, Talen Energy, AES Corporation, Clearway Energy

**Transmission Companies:**
ITC Holdings, American Transmission Co, GridLiance, NextEra Transmission, LS Power Grid, Invenergy Transmission, Pattern Energy

**Renewable Developers:**
Invenergy, Apex Clean Energy, EDF Renewables, Avangrid Renewables, Ørsted, Vineyard Wind, Dominion Offshore Wind, Equinor, RWE, TotalEnergies, BP, Lightsource BP, Longroad Energy, 174 Power Global, Savion

**Nuclear (Advanced & Existing):**
Constellation Energy, Vistra, NuScale Power, TerraPower, X-energy, Kairos Power, Oklo, Holtec, GE Hitachi, Westinghouse, TVA, Energy Northwest, UAMPS

**Oil & Gas (energy transition relevance):**
ExxonMobil, Chevron, ConocoPhillips, Williams Companies, Kinder Morgan, Enterprise Products, Cheniere, Venture Global, NextDecade

**Technology / Data Centers:**
Meta, Google, Microsoft, Amazon/AWS, Oracle, Digital Realty, Equinix, QTS Realty

**Equipment & Technology:**
GE Vernova, Siemens Energy, Vestas, First Solar, Tesla, Fluence, Form Energy

## Search Query Templates

Always include SPECIFIC DATES in searches.

**News & Statements:**
- "FERC" + "order" + [specific date]
- "transmission" + "approved" + [specific date]
- "offshore wind" + [company] + [specific date]
- "grid reliability" + [RTO] + [specific date]

**Publications:**
- site:eia.gov + "report" + [date range]
- site:nrel.gov + [date range]
- site:rmi.org + [date range]

**Congressional:**
- site:congress.gov + "energy" + [specific date]
- "Senate energy hearing" + [specific date]

**Business:**
- [company] + "announces" + [specific date]
- "PPA" + "MW" + [specific date]
- "data center" + "power" + [specific date]

## Events Calendar Reference

**Recurring Events:**
- FERC Open Meeting: Monthly (3rd Thursday)
- EIA Weekly Petroleum Status: Wednesday
- EIA Natural Gas Storage: Thursday

**RTO/ISO Meetings:**
- PJM Board/Members Committee: Monthly
- MISO Board of Directors: Monthly
- CAISO Board of Governors: Monthly
- ERCOT Board of Directors: Monthly

**Major Conferences:**
- CERAWeek (March)
- EEI Financial Conference (November)
- AWEA Cleanpower (Spring)
- Solar Power International (Fall)

## Coverage Gaps to Acknowledge

Note in Limitations if not accessible:
- Paywalled sources (S&P Global, Bloomberg Terminal)
- Real-time FERC filings
- Earnings call transcripts
- State PUC dockets
- International sources (IEA, IRENA)

---

# APPENDIX B: Grantee Organizations

**You MUST search ALL 21 organizations. No exceptions.**

## Organizations by Topic

**Nuclear & Advanced Energy (4):**
1. Nuclear Innovation Alliance
2. Third Way
3. Breakthrough Institute
4. ClearPath

**Grid & Transmission (3):**
5. Grid Strategies
6. Bipartisan Policy Center
7. Rocky Mountain Institute (RMI)

**Permitting & Siting (4):**
8. Institute for Progress
9. Environmental Policy Innovation Center
10. Siting Solutions Project / Clean Tomorrow
11. Siting Clean Collaborative

**General Energy Policy (4):**
12. R Street Institute
13. Niskanen Center
14. Clean Air Task Force
15. RAND Corporation

**Industry & Markets (2):**
16. Clean Energy Buyers Alliance
17. Electricity Customers Alliance

**Conservative/Cross-partisan (4):**
18. American Conservation Coalition
19. Foundation for American Innovation
20. Rainey Center
21. Abundance Institute

## Search Procedure

1. Calculate 7-day cutoff: [Today] minus 7 days = _____
2. Search each org: "[Org Name] energy [month year]"
3. For each result:
   - Find EXACT publication date
   - Is date ≥ cutoff? If YES → include. If NO → skip.
4. Track all orgs searched
5. List orgs with no recent publications in NO_PUBLICATIONS

**A search result appearing does NOT mean it's within the date window. You MUST verify each date.**

---

# FINAL INSTRUCTION

Generate the content in the exact structured format from Section 3. Include only verified, current news within the specified time windows. Output only the structured content — no HTML, no explanation, no commentary.
