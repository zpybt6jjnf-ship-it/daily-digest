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
- FERC Open Meeting, Congressional hearings (Senate ENR, House E&C), RTO board meetings

SOURCE ACCURACY RULES:
1. Use ORIGINAL publication dates, not news coverage dates
2. Title = what happened, not what article is about
3. Distinguish primary sources from secondary coverage
4. For reactions: "Re: [Original] (Date)"
5. Flag uncertain facts: "(unverified)" or "(paywalled)"

SECTIONS TO GENERATE:
1. Top Developments (3 bullet points summarizing biggest news)
2. News & Statements (past 24-48 hrs)
3. Publications (past 7 days only)
4. Congressional & Executive Activity
5. Business Activity (include MW, $, timelines)
6. China
7. Macro Trends (2-3 paragraphs)
8. What to Watch This Week (table + Key Questions)
9. Grantee Activities (see detailed instructions below)
10. Limitations & Gaps

GRANTEE ACTIVITIES — DETAILED INSTRUCTIONS:
Search for recent publications/statements (past 7 days) from these organizations:
- ClearPath, Clean Air Task Force, Bipartisan Policy Center, Clean Energy Buyers Alliance
- R Street Institute, Breakthrough Institute, Third Way, Foundation for American Innovation
- Rainey Center, Siting Solutions Project, Electricity Customers Alliance
- American Conservation Coalition, Niskanen Center, Institute for Progress
- Environmental Policy Innovation Center, RAND Corporation

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

OUTPUT:
Generate a complete, valid HTML file using the template above. Fill in all sections with real, current news. Output only the HTML code, no explanation.

CRITICAL REMINDERS:
- All links must say "Source →" (exactly this text)
- Grantee cards only for orgs WITH publications; combine those without into one italic line at the end
- Each grantee card needs a substantive summary (not just a quote)
- Include the SVG logo exactly as shown
- Use the exact inline styles from the template
