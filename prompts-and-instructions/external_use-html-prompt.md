ENERGY & PERMITTING DAILY DIGEST — HTML OUTPUT PROMPT

Copy everything below this line and paste into Gemini or Claude:

————————————————————————————————

Generate today's Energy & Permitting Daily Digest as a complete, styled HTML file.

SCOPE
- Geography: US primary, China secondary
- Energy: All sectors, weighted toward electricity/grid
- Permitting: NEPA, environmental review, siting, interconnection, permitting reform

SEARCH THESE SOURCES:
- News: Utility Dive, E&E News, RTO Insider, Canary Media, Heatmap News, Reuters Energy, Bloomberg Energy
- Government: FERC.gov, DOE.gov, Federal Register
- Companies: NextEra, Duke, Southern, Dominion, AEP, Xcel, Entergy, PG&E, Vistra, Constellation, Talen, AES
- Transmission: ITC, ATC, GridLiance, LS Power
- Renewables: Invenergy, Apex, Ørsted, Avangrid, EDF, Pattern
- Nuclear: NuScale, TerraPower, X-energy, Kairos, Oklo, Holtec
- Tech/Data Centers: Meta, Google, Microsoft, Amazon, Oracle
- RTOs: PJM, MISO, CAISO, ERCOT, SPP, NYISO, ISO-NE

EVENTS TO CHECK:
- FERC Open Meeting agenda/outcomes
- Congressional hearings (Senate ENR, House E&C)
- RTO board meetings
- Major comment deadlines

For each section, actively search for news from these sources rather than relying on general searches.

SOURCE ACCURACY RULES (CRITICAL):

1. PRIMARY vs. SECONDARY SOURCES
   - Primary: Original reports, official announcements, filings, press releases
   - Secondary: News articles, commentary, analysis about primary sources
   - ALWAYS distinguish between them. Never present secondary coverage as the primary source.

2. DATING
   - Use the ORIGINAL publication date for reports/documents, not news coverage date
   - Example: If a Jan 15 article discusses a December report, use the December date
   - Format: "Report Name (December 2025)" not "Report Name · Jan 15, 2026"

3. ACCURATE TITLES
   - Title should reflect WHAT HAPPENED, not what the article is about
   - WRONG: "NPC Permitting Report" (when source is an article about company supporting the report)
   - RIGHT: "Williams Endorses NPC Permitting Report"

4. REACTIONS/COMMENTARY
   - Lead with WHO is reacting and WHAT they said
   - Reference the original source with its actual date
   - Example: "Williams CEO endorses NPC's December 2025 permitting report, calling for streamlined NEPA reviews"

5. VERIFICATION
   - If uncertain about a date or fact: "(date unconfirmed)" or "(per [source])"
   - When source is paywalled: "(paywalled - summary based on available excerpt)"

6. LINK TO BEST SOURCE
   - Prefer linking to primary sources when available
   - If only secondary coverage exists, note that it's coverage of [original]

SECTIONS TO GENERATE:

1. Top Developments (3 bullet points summarizing biggest news)

2. News & Statements (past 24-48 hrs)
   Search: energy policy news, permitting reform, FERC orders, transmission projects, utility announcements, renewable energy, grid reliability, DOE announcements, offshore wind
   - Focus on NEW announcements, not coverage of older items
   - If covering reactions to older news, frame as reactions

3. Publications (past 7 days only)
   Search: EIA, RMI, RFF, OECD, NREL, think tank reports, academic energy publications
   - Use actual publication date, not discovery date

4. Congressional & Executive Activity
   Search: energy bills Congress, FERC notices, Federal Register energy/environment, DOE announcements, EPA rules, BLM leasing
   - Include docket numbers and filing dates where available

5. Business Activity (include MW, $, timelines)
   Search: energy project announcements, renewable PPAs, utility M&A, transmission projects, data center power deals, nuclear agreements
   - Distinguish between: announced, filed, approved, completed

6. China
   Search: China energy policy, State Grid, NDRC energy, China renewables, China carbon market, Five-Year Plan energy

7. Macro Trends (2-3 paragraphs)
   - Connect today's items to ongoing themes (permitting stalemate, data center load growth, nuclear momentum, etc.)
   - Cite specific items from this digest
   - Avoid speculation; stick to observable patterns

8. What to Watch This Week (table + Key Questions)
   - Table of upcoming deadlines, hearings, FERC meetings, court rulings, conferences
   - Verify dates against official calendars where possible

9. Grantee Activities (see detailed instructions below)

10. Limitations & Gaps
    - List sources not systematically covered
    - Note items where dates could not be verified
    - Note paywalled sources that limited coverage

GRANTEE ACTIVITIES — DETAILED INSTRUCTIONS:
Search for recent publications/statements (past 7 days) from these organizations:
- ClearPath, Clean Air Task Force, Bipartisan Policy Center, Clean Energy Buyers Alliance
- R Street Institute, Breakthrough Institute, Third Way, Foundation for American Innovation
- Rainey Center, Siting Solutions Project / Clean Tomorrow, Electricity Customers Alliance
- American Conservation Coalition, Niskanen Center, Institute for Progress
- Environmental Policy Innovation Center, RAND Corporation, Nuclear Innovation Alliance, Grid Strategies, Abundance Institute

Also search for similar organizations and note findings under "Similar Organizations"

Format:
- If publication found: Create a card with org name, publication summary (not just a quote), and "Source →" link
- If NO publication found for an org: Do NOT create a separate card for it
- At the END of the section: List all orgs with no recent publications in ONE line:
  "No recent energy/permitting publications identified: [Org1], [Org2], [Org3]..."

OUTPUT FORMAT:
Generate a complete HTML file using this exact template. Replace the placeholder comments with actual content.

STRICT FORMATTING RULES:
1. Every news item MUST end with a link that says exactly "Source →" (not "Read more", not "Link", not the URL)
2. Link format: <a href="URL" style="color: #2a9d8f; text-decoration: none; font-size: 12px; font-weight: 500;">Source →</a>
3. Use the exact HTML structure shown in the template — do not simplify or change styles
4. Every section must use the coral-highlighted header style shown
5. Grantee section must have individual cards for EACH organization, not a combined list
6. MUST include the SVG logo in the header exactly as shown in the template

BRAND COLORS:
- cream: #faf8f5
- ink: #1a1a2e
- ink_light: #4a4a5a
- ink_muted: #8a8a9a
- teal: #2a9d8f
- coral: #e76f51
- gold: #e9c46a
- border: #e8e6e1

HTML TEMPLATE TO USE:

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Energy & Permitting Daily Digest</title>
</head>
<body style="margin: 0; padding: 0; background-color: #faf8f5; font-family: -apple-system, BlinkMacSystemFont, sans-serif;">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background-color: #faf8f5;">
    <tr>
      <td align="center" style="padding: 24px 16px;">
        <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="max-width: 640px; background-color: #ffffff; border: 2px solid #1a1a2e; border-radius: 12px; box-shadow: 4px 4px 0 #1a1a2e;">

          <!-- Beta Banner -->
          <tr>
            <td style="background-color: #e9c46a; padding: 8px 28px; border-radius: 10px 10px 0 0;">
              <p style="margin: 0; font-family: monospace; font-size: 11px; font-weight: 700; color: #1a1a2e; text-align: center;">BETA — This digest is auto-generated and may contain errors.</p>
            </td>
          </tr>

          <!-- Header -->
          <tr>
            <td style="padding: 20px 28px; border-bottom: 2px solid #1a1a2e;">
              <table role="presentation" width="100%" cellpadding="0" cellspacing="0">
                <tr>
                  <td valign="middle" width="52">
                    <!-- Logo Mark - MUST INCLUDE -->
                    <svg width="44" height="44" viewBox="0 0 44 44" xmlns="http://www.w3.org/2000/svg">
                      <defs>
                        <linearGradient id="logoGradient" x1="0%" y1="0%" x2="100%" y2="0%">
                          <stop offset="0%" style="stop-color:#2a9d8f" />
                          <stop offset="50%" style="stop-color:#e9c46a" />
                          <stop offset="100%" style="stop-color:#e76f51" />
                        </linearGradient>
                      </defs>
                      <rect x="0" y="0" width="44" height="44" fill="#1a1a2e" rx="0" />
                      <path d="M 0,30.8 L 3.52,28.6 L 7.92,33 L 12.32,22 L 16.72,26.4 L 22,13.2 L 27.28,24.2 L 31.68,19.8 L 36.08,26.4 L 40.48,24.2 L 44,28.6" stroke="url(#logoGradient)" stroke-width="1.32" fill="none" stroke-linejoin="round" />
                    </svg>
                  </td>
                  <td valign="middle" style="padding-left: 12px;">
                    <p style="margin: 0; font-size: 16px; font-weight: 700; color: #1a1a2e;">Energy & Permitting Daily Digest</p>
                    <p style="margin: 2px 0 0 0; font-family: monospace; font-size: 11px; color: #8a8a9a;">BOTTLENECKS LABS</p>
                  </td>
                  <td align="right" valign="middle">
                    <p style="margin: 0; font-family: monospace; font-size: 12px; color: #2a9d8f; font-weight: 700;"><!-- INSERT TODAY'S DATE --></p>
                  </td>
                </tr>
              </table>
            </td>
          </tr>

          <!-- Gradient Bar -->
          <tr>
            <td style="height: 4px; background: linear-gradient(90deg, #2a9d8f, #e9c46a);"></td>
          </tr>

          <!-- Top Developments -->
          <tr>
            <td style="padding: 24px 28px;">
              <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background-color: #faf8f5; border-left: 3px solid #2a9d8f; border-radius: 4px;">
                <tr>
                  <td style="padding: 16px 20px;">
                    <p style="margin: 0; font-family: monospace; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #2a9d8f;">Top Developments</p>
                    <ul style="margin: 12px 0 0 0; padding: 0 0 0 18px;">
                      <!-- INSERT 3 BULLET POINTS SUMMARIZING TOP NEWS -->
                    </ul>
                  </td>
                </tr>
              </table>
            </td>
          </tr>

          <!-- For each SECTION, use this format: -->
          <tr>
            <td style="padding: 20px 28px;">
              <h2 style="margin: 0 0 14px 0; font-size: 16px; font-weight: 700; color: #1a1a2e;">
                <span style="background: linear-gradient(180deg, transparent 55%, rgba(231, 111, 81, 0.3) 55%); padding: 0 4px;"><!-- SECTION TITLE --></span>
              </h2>
              <!-- SECTION CONTENT -->
            </td>
          </tr>
          <tr>
            <td style="padding: 0 28px;">
              <table role="presentation" width="100%" cellpadding="0" cellspacing="0">
                <tr><td style="border-bottom: 1px dashed #d4d2cd;"></td></tr>
              </table>
            </td>
          </tr>

          <!-- For each NEWS ITEM, use this card format: -->
          <div style="background: #faf8f5; border-radius: 8px; padding: 14px 16px; margin-bottom: 12px;">
            <p style="font-size: 14px; font-weight: 600; color: #1a1a2e; margin: 0 0 4px 0;"><!-- TITLE: What Happened --></p>
            <p style="font-family: monospace; font-size: 11px; color: #8a8a9a; margin: 0 0 6px 0;"><!-- Source · Date --></p>
            <p style="font-size: 13px; line-height: 1.55; color: #4a4a5a; margin: 0;"><!-- 2-3 line summary --></p>
            <p style="margin: 10px 0 0 0;"><a href="<!-- URL -->" style="color: #2a9d8f; text-decoration: none; font-size: 12px; font-weight: 500;">Source →</a></p>
          </div>

          <!-- For TABLES (What to Watch), use: -->
          <table style="width: 100%; border-collapse: collapse; margin: 12px 0; font-size: 13px; border: 1px solid #e8e6e1; border-radius: 8px;">
            <tr style="background: #faf8f5;">
              <th style="padding: 10px 12px; text-align: left; font-weight: 600; color: #1a1a2e; border-bottom: 2px solid #d4d2cd;"><!-- Header --></th>
            </tr>
            <tr>
              <td style="padding: 10px 12px; border-bottom: 1px solid #e8e6e1; color: #4a4a5a;"><!-- Content --></td>
            </tr>
          </table>

          <!-- For KEY QUESTIONS box: -->
          <div style="margin-top: 16px; padding: 14px 16px; background: #faf8f5; border-radius: 8px; border-left: 3px solid #e9c46a;">
            <p style="font-family: monospace; font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.08em; color: #e9c46a; margin: 0 0 10px 0;">Key Questions</p>
            <ol style="margin: 0; padding: 0 0 0 18px; color: #4a4a5a;">
              <li style="margin: 0 0 6px 0; font-size: 13px; line-height: 1.5;"><!-- Question --></li>
            </ol>
          </div>

          <!-- For GRANTEE organizations WITH recent publications — one card each: -->
          <div style="background: #faf8f5; border-radius: 8px; padding: 12px 14px; margin-bottom: 10px;">
            <p style="font-size: 13px; font-weight: 600; color: #1a1a2e; margin: 0 0 6px 0;">[Org Name]</p>
            <p style="font-size: 12px; line-height: 1.5; color: #4a4a5a; margin: 0;">[Publication title and 1-2 sentence summary of findings]</p>
            <p style="margin: 8px 0 0 0;"><a href="URL" style="color: #2a9d8f; text-decoration: none; font-size: 12px; font-weight: 500;">Source →</a></p>
          </div>
          <!-- At the END, combine all orgs with NO publications into one line: -->
          <p style="font-size: 12px; font-style: italic; color: #8a8a9a; margin: 16px 0 0 0;">No recent energy/permitting publications identified: [Org1], [Org2], [Org3]...</p>

          <!-- Footer -->
          <tr>
            <td style="background-color: #1a1a2e; padding: 20px 28px; border-top: 3px solid #e9c46a; border-radius: 0 0 10px 10px;">
              <p style="margin: 0; font-size: 13px; color: #faf8f5; text-align: center; font-weight: 500;">Compiled by Bottlenecks Labs</p>
              <p style="margin: 4px 0 0 0; font-size: 11px; color: #8a8a9a; text-align: center; font-style: italic;">Coverage: Past 24-48 hours</p>
            </td>
          </tr>

        </table>
      </td>
    </tr>
  </table>
</body>
</html>

QUALITY CHECKLIST (verify before finalizing):
□ Each item's date reflects the actual event/publication date, not coverage date
□ Titles describe what happened, not what an article is about
□ Primary sources linked where available
□ Reactions clearly labeled as reactions, with original source referenced
□ No items older than 7 days unless noting ongoing significance
□ Uncertain facts flagged appropriately
□ All links use "Source →" format
□ Logo SVG included in header
□ All sections use coral-highlighted header style

SELF-REVIEW BEFORE OUTPUT:
1. FACT CHECK: Review each item for date accuracy and proper source attribution
2. DESIGN CHECK: Verify HTML matches the template exactly (colors, spacing, fonts)
3. LINK CHECK: Ensure all URLs are complete and properly formatted

OUTPUT:
Generate a complete, valid HTML file using the template above. Fill in all sections with real, current news. Output only the HTML code, no explanation.

STYLE:
- Clean, professional, data-forward
- No emoji
- Accuracy over comprehensiveness

CRITICAL REMINDERS:
- All links must say "Source →" (exactly this text)
- Grantee cards only for orgs WITH publications; combine those without into one italic line at the end
- Each grantee card needs a substantive summary (not just a quote)
- Include the SVG logo exactly as shown
- Use the exact inline styles from the template

Output as an artifact so I can preview the rendered HTML.
