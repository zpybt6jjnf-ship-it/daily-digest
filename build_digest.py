#!/usr/bin/env python3
"""
Build Digest - Converts structured content into branded HTML

Usage:
    python build_digest.py content.txt              # Read from file
    python build_digest.py content.txt -o out.html  # Specify output
    cat content.txt | python build_digest.py        # Read from stdin
"""

import sys
import re
import argparse
from datetime import datetime
from pathlib import Path

# =============================================================================
# BRAND COLORS
# =============================================================================
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

TAG_COLORS = {
    'Nuclear': '#9b59b6',
    'Data Center': '#1abc9c',
    'Grid': '#e67e22',
    'Wind': '#3498db',
    'Solar': '#d4a017',  # Darker gold for better contrast with white text
    'Storage': '#27ae60',
    'Policy': '#e74c3c',
}

# =============================================================================
# CONTENT PARSER
# =============================================================================
def parse_content(text):
    """Parse the structured content format into a dictionary."""
    sections = {}

    # Split by section markers
    section_pattern = r'===(\w+)==='
    parts = re.split(section_pattern, text)

    # parts[0] is before first section, then alternating: section_name, content
    for i in range(1, len(parts), 2):
        section_name = parts[i].strip()
        section_content = parts[i + 1].strip() if i + 1 < len(parts) else ''
        sections[section_name] = section_content

    return sections


def parse_top_developments(content):
    """Parse top developments bullet points."""
    items = []
    for line in content.strip().split('\n'):
        line = line.strip()
        if line.startswith('- '):
            # Parse "- **Title** — Summary" or "- Title — Summary"
            line = line[2:]  # Remove "- "
            if ' — ' in line:
                parts = line.split(' — ', 1)
                title = parts[0].strip().strip('*')
                summary = parts[1].strip() if len(parts) > 1 else ''
                items.append({'title': title, 'summary': summary})
            else:
                items.append({'title': line, 'summary': ''})
    return items


def parse_news_section(content):
    """Parse news section with subsections and items."""
    subsections = []
    current_subsection = None
    current_item = None

    for line in content.split('\n'):
        line = line.rstrip()

        if line.startswith('##SUBSECTION:'):
            if current_subsection and current_item:
                current_subsection['items'].append(current_item)
            if current_subsection:
                subsections.append(current_subsection)
            current_subsection = {
                'name': line.replace('##SUBSECTION:', '').strip(),
                'items': []
            }
            current_item = None

        elif line.strip() == 'ITEM:':
            if current_item and current_subsection:
                current_subsection['items'].append(current_item)
            current_item = {'tags': [], 'significance': '', 'title': '', 'source': '', 'date': '', 'summary': '', 'url': ''}

        elif current_item is not None:
            if line.startswith('tags:'):
                tags_str = line.replace('tags:', '').strip()
                # Parse [tag1, tag2] format
                tags_str = tags_str.strip('[]')
                if tags_str:
                    current_item['tags'] = [t.strip() for t in tags_str.split(',') if t.strip()]
            elif line.startswith('significance:'):
                current_item['significance'] = line.replace('significance:', '').strip().lower()
            elif line.startswith('title:'):
                current_item['title'] = line.replace('title:', '').strip()
            elif line.startswith('source:'):
                current_item['source'] = line.replace('source:', '').strip()
            elif line.startswith('date:'):
                current_item['date'] = line.replace('date:', '').strip()
            elif line.startswith('summary:'):
                current_item['summary'] = line.replace('summary:', '').strip()
            elif line.startswith('url:'):
                current_item['url'] = line.replace('url:', '').strip()

    # Don't forget the last item and subsection
    if current_item and current_subsection:
        current_subsection['items'].append(current_item)
    if current_subsection:
        subsections.append(current_subsection)

    return subsections


def parse_items(content):
    """Parse a section with ITEM: blocks."""
    items = []
    current_item = None

    for line in content.split('\n'):
        line = line.rstrip()

        if line.strip() == 'ITEM:':
            if current_item:
                items.append(current_item)
            current_item = {'tags': [], 'significance': '', 'title': '', 'source': '', 'date': '', 'summary': '', 'url': ''}

        elif current_item is not None:
            if line.startswith('tags:'):
                tags_str = line.replace('tags:', '').strip().strip('[]')
                if tags_str:
                    current_item['tags'] = [t.strip() for t in tags_str.split(',') if t.strip()]
            elif line.startswith('significance:'):
                current_item['significance'] = line.replace('significance:', '').strip().lower()
            elif line.startswith('title:'):
                current_item['title'] = line.replace('title:', '').strip()
            elif line.startswith('source:'):
                current_item['source'] = line.replace('source:', '').strip()
            elif line.startswith('date:'):
                current_item['date'] = line.replace('date:', '').strip()
            elif line.startswith('summary:'):
                current_item['summary'] = line.replace('summary:', '').strip()
            elif line.startswith('url:'):
                current_item['url'] = line.replace('url:', '').strip()

    if current_item:
        items.append(current_item)

    return items


def parse_calendar(content):
    """Parse markdown table into list of dicts."""
    rows = []
    lines = [l.strip() for l in content.strip().split('\n') if l.strip()]

    for line in lines:
        if line.startswith('|') and '---' not in line:
            cells = [c.strip() for c in line.split('|')[1:-1]]
            if len(cells) >= 3 and cells[0].lower() != 'date':
                rows.append({
                    'date': cells[0],
                    'event': cells[1],
                    'significance': cells[2] if len(cells) > 2 else ''
                })
    return rows


def parse_key_questions(content):
    """Parse bullet list of questions."""
    questions = []
    for line in content.strip().split('\n'):
        line = line.strip()
        if line.startswith('- '):
            questions.append(line[2:].strip())
    return questions


def parse_grantees(content):
    """Parse grantee section."""
    orgs = []
    no_pubs = []
    current_org = None

    for line in content.split('\n'):
        line = line.rstrip()

        if line.startswith('ORG:'):
            if current_org:
                orgs.append(current_org)
            current_org = {'name': line.replace('ORG:', '').strip(), 'title': '', 'date': '', 'summary': '', 'url': ''}

        elif line.startswith('NO_PUBLICATIONS:'):
            no_pubs_str = line.replace('NO_PUBLICATIONS:', '').strip()
            no_pubs = [o.strip() for o in no_pubs_str.split(',') if o.strip()]

        elif current_org is not None:
            if line.startswith('title:'):
                current_org['title'] = line.replace('title:', '').strip()
            elif line.startswith('date:'):
                current_org['date'] = line.replace('date:', '').strip()
            elif line.startswith('summary:'):
                current_org['summary'] = line.replace('summary:', '').strip()
            elif line.startswith('url:'):
                current_org['url'] = line.replace('url:', '').strip()

    if current_org:
        orgs.append(current_org)

    return orgs, no_pubs


def parse_limitations(content):
    """Parse bullet list of limitations."""
    items = []
    for line in content.strip().split('\n'):
        line = line.strip()
        if line.startswith('- '):
            items.append(line[2:].strip())
    return items


# =============================================================================
# HTML GENERATORS
# =============================================================================
def html_escape(text):
    """Basic HTML escaping."""
    if not text:
        return ''
    return (text
            .replace('&', '&amp;')
            .replace('<', '&lt;')
            .replace('>', '&gt;')
            .replace('"', '&quot;'))


def render_tags(tags):
    """Render topic tags HTML. Limit to 2 tags max for cleaner look."""
    if not tags:
        return ''

    # Limit to 2 most relevant tags to avoid clutter
    display_tags = tags[:2]

    tag_html = []
    for tag in display_tags:
        color = TAG_COLORS.get(tag, COLORS['teal'])
        tag_html.append(
            f'<span style="display: inline-block; background: {color}; color: #ffffff; '
            f'font-size: 10px; padding: 2px 8px; border-radius: 3px; margin-right: 4px; '
            f'font-weight: 600;">{html_escape(tag)}</span>'
        )

    return f'<p style="margin: 0 0 8px 0;">{"".join(tag_html)}</p>'


def render_news_item(item):
    """Render a single news item card."""
    tags_html = render_tags(item.get('tags', []))

    return f'''
          <tr>
            <td style="padding: 0 28px 14px 28px;">
              <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background: #faf8f5; border-radius: 8px; border-left: 3px solid #e76f51;">
                <tr>
                  <td style="padding: 14px 16px;">{tags_html}<p style="font-size: 14px; font-weight: 600; color: #1a1a2e; margin: 0 0 4px 0;">{html_escape(item.get('title', ''))}</p>
                    <p style="font-family: 'Courier New', monospace; font-size: 11px; color: #8a8a9a; margin: 0 0 8px 0;"><span style="color: #2a9d8f; font-weight: 500;">{html_escape(item.get('source', ''))}</span> · {html_escape(item.get('date', ''))}</p>
                    <p style="font-size: 13px; line-height: 1.6; color: #4a4a5a; margin: 0;">{html_escape(item.get('summary', ''))}</p>
                    <p style="margin: 10px 0 0 0;"><a href="{html_escape(item.get('url', '#'))}" style="color: #2a9d8f; text-decoration: none; font-size: 12px; font-weight: 500;">Source →</a></p>
                  </td>
                </tr>
              </table>
            </td>
          </tr>'''


def render_subsection_header(name):
    """Render a gold-underlined subsection header with breathing room."""
    return f'''
          <tr>
            <td style="padding: 16px 28px 12px 28px;">
              <p style="margin: 0; font-size: 13px; font-weight: 600; color: #1a1a2e; text-transform: uppercase; letter-spacing: 0.5px; padding-bottom: 6px; border-bottom: 2px solid #e9c46a; display: inline-block;">{html_escape(name)}</p>
            </td>
          </tr>'''


def render_section_header(title):
    """Render a coral-highlighted section header."""
    return f'''
          <tr>
            <td style="padding: 20px 28px 16px 28px;">
              <h2 style="margin: 0; font-size: 16px; font-weight: 700; color: #1a1a2e;">
                <span style="background: linear-gradient(180deg, transparent 55%, rgba(231, 111, 81, 0.3) 55%); padding: 0 4px;">{html_escape(title)}</span>
              </h2>
            </td>
          </tr>'''


def render_section_divider():
    """Render dashed divider between sections."""
    return '''
          <tr>
            <td style="padding: 8px 28px 20px 28px;">
              <table role="presentation" width="100%" cellpadding="0" cellspacing="0">
                <tr><td style="border-bottom: 1px dashed #d4d2cd;"></td></tr>
              </table>
            </td>
          </tr>'''


def render_calendar_table(rows):
    """Render the What to Watch table."""
    rows_html = ''
    for row in rows:
        rows_html += f'''
                <tr>
                  <td style="padding: 10px 12px; border-bottom: 1px solid #e8e6e1; color: #4a4a5a; vertical-align: top;">{html_escape(row.get('date', ''))}</td>
                  <td style="padding: 10px 12px; border-bottom: 1px solid #e8e6e1; color: #4a4a5a; vertical-align: top;">{html_escape(row.get('event', ''))}</td>
                  <td style="padding: 10px 12px; border-bottom: 1px solid #e8e6e1; color: #4a4a5a; vertical-align: top;">{html_escape(row.get('significance', ''))}</td>
                </tr>'''

    return f'''
          <tr>
            <td style="padding: 0 28px 16px 28px;">
              <table style="width: 100%; border-collapse: collapse; font-size: 12px;">
                <tr>
                  <th style="background-color: #1a1a2e; color: #ffffff; padding: 10px 12px; text-align: left; font-weight: 600; font-size: 11px; text-transform: uppercase;">Date</th>
                  <th style="background-color: #1a1a2e; color: #ffffff; padding: 10px 12px; text-align: left; font-weight: 600; font-size: 11px; text-transform: uppercase;">Event</th>
                  <th style="background-color: #1a1a2e; color: #ffffff; padding: 10px 12px; text-align: left; font-weight: 600; font-size: 11px; text-transform: uppercase;">Significance</th>
                </tr>
                {rows_html}
              </table>
            </td>
          </tr>'''


def render_key_questions(questions):
    """Render the Key Questions box."""
    questions_html = ''
    for q in questions:
        questions_html += f'''
                      <tr>
                        <td valign="top" style="padding-right: 8px; color: #e9c46a; font-weight: 700; font-size: 13px;">?</td>
                        <td style="color: #4a4a5a; font-size: 13px; line-height: 1.5; padding-bottom: 6px;">{html_escape(q)}</td>
                      </tr>'''

    return f'''
          <tr>
            <td style="padding: 0 28px 20px 28px;">
              <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background: #faf8f5; border-radius: 8px; border-left: 3px solid #e9c46a;">
                <tr>
                  <td style="padding: 14px 16px;">
                    <p style="font-family: 'Courier New', monospace; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; color: #e9c46a; margin: 0 0 10px 0;">Key Questions</p>
                    <table role="presentation" cellpadding="0" cellspacing="0">
                      {questions_html}
                    </table>
                  </td>
                </tr>
              </table>
            </td>
          </tr>'''


def render_macro_trends(content):
    """Render macro trends box."""
    # Convert **bold** to <strong>
    content = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', content)

    # Split into paragraphs
    paragraphs = [p.strip() for p in content.split('\n\n') if p.strip()]

    paras_html = ''
    for i, p in enumerate(paragraphs):
        margin = '0' if i == len(paragraphs) - 1 else '0 0 12px 0'
        paras_html += f'<p style="font-size: 13px; line-height: 1.6; color: #4a4a5a; margin: {margin};">{p}</p>'

    return f'''
          <tr>
            <td style="padding: 0 28px 20px 28px;">
              <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background: #ffffff; border-radius: 8px; border: 1px solid #e8e6e1; border-left: 4px solid #2a9d8f;">
                <tr>
                  <td style="padding: 16px 20px;">
                    {paras_html}
                  </td>
                </tr>
              </table>
            </td>
          </tr>'''


def render_grantee_card(org):
    """Render a single grantee organization card."""
    return f'''
          <tr>
            <td style="padding: 0 28px 10px 28px;">
              <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background: #ffffff; border: 1px solid #e8e6e1; border-radius: 8px;">
                <tr>
                  <td style="padding: 14px 16px;">
                    <p style="font-size: 14px; font-weight: 600; color: #2a9d8f; margin: 0 0 6px 0;">{html_escape(org.get('name', ''))}</p>
                    <p style="font-size: 13px; line-height: 1.55; color: #4a4a5a; margin: 0;"><strong>"{html_escape(org.get('title', ''))}"</strong> ({html_escape(org.get('date', ''))}) — {html_escape(org.get('summary', ''))}</p>
                    <p style="margin: 10px 0 0 0;"><a href="{html_escape(org.get('url', '#'))}" style="color: #2a9d8f; text-decoration: none; font-size: 12px; font-weight: 500;">Source →</a></p>
                  </td>
                </tr>
              </table>
            </td>
          </tr>'''


def render_no_publications(orgs):
    """Render the list of orgs with no publications."""
    if not orgs:
        return ''
    return f'''
          <tr>
            <td style="padding: 0 28px 20px 28px;">
              <p style="font-size: 12px; font-style: italic; color: #8a8a9a; margin: 8px 0 0 0;">No recent energy/permitting publications identified: {html_escape(', '.join(orgs))}</p>
            </td>
          </tr>'''


def render_limitations(items):
    """Render limitations box."""
    items_html = ''
    for i, item in enumerate(items):
        margin = '0' if i == len(items) - 1 else '0 0 4px 0'
        items_html += f'<li style="margin: {margin};">{html_escape(item)}</li>'

    return f'''
          <tr>
            <td style="padding: 0 28px 20px 28px;">
              <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background: #f5f5f5; border-radius: 8px;">
                <tr>
                  <td style="padding: 14px 16px;">
                    <p style="font-size: 12px; font-weight: 600; color: #4a4a5a; margin: 0 0 8px 0;">Research Limitations</p>
                    <ul style="margin: 0; padding: 0 0 0 18px; font-size: 12px; color: #8a8a9a; line-height: 1.5;">
                      {items_html}
                    </ul>
                  </td>
                </tr>
              </table>
            </td>
          </tr>'''


# =============================================================================
# MAIN HTML TEMPLATE
# =============================================================================
def build_html(sections, date_str=None):
    """Build the complete HTML document from parsed sections."""

    if not date_str:
        date_str = datetime.now().strftime('%b %d, %Y')

    # Parse all sections
    top_devs = parse_top_developments(sections.get('TOP_DEVELOPMENTS', ''))
    news_subsections = parse_news_section(sections.get('NEWS', ''))
    publications = parse_items(sections.get('PUBLICATIONS', ''))
    congressional = parse_items(sections.get('CONGRESSIONAL', ''))
    business = parse_items(sections.get('BUSINESS', ''))
    china = parse_items(sections.get('CHINA', ''))
    macro_trends = sections.get('MACRO_TRENDS', '')
    calendar = parse_calendar(sections.get('CALENDAR', ''))
    key_questions = parse_key_questions(sections.get('KEY_QUESTIONS', ''))
    grantees, no_pubs = parse_grantees(sections.get('GRANTEES', ''))
    limitations = parse_limitations(sections.get('LIMITATIONS', ''))

    # Build top developments HTML
    top_devs_html = ''
    for dev in top_devs:
        top_devs_html += f'<li style="margin-bottom: 8px;"><strong>{html_escape(dev["title"])}</strong> — {html_escape(dev["summary"])}</li>'

    # Build news section HTML
    news_html = ''
    for subsection in news_subsections:
        news_html += render_subsection_header(subsection['name'])
        for item in subsection['items']:
            news_html += render_news_item(item)

    # Build publications HTML
    pubs_html = ''
    for item in publications:
        pubs_html += render_news_item(item)

    # Build congressional HTML
    cong_html = ''
    for item in congressional:
        cong_html += render_news_item(item)

    # Build business HTML
    biz_html = ''
    for item in business:
        biz_html += render_news_item(item)

    # Build china HTML
    china_html = ''
    for item in china:
        china_html += render_news_item(item)

    # Build grantees HTML
    grantees_html = ''
    for org in grantees:
        grantees_html += render_grantee_card(org)
    grantees_html += render_no_publications(no_pubs)

    # Assemble full HTML
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Energy & Permitting Daily Digest - {html_escape(date_str)}</title>
</head>
<body style="margin: 0; padding: 0; background-color: #faf8f5; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background-color: #faf8f5;">
    <tr>
      <td align="center" style="padding: 24px 16px;">
        <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="max-width: 640px; background-color: #ffffff; border: 2px solid #1a1a2e; border-radius: 12px; box-shadow: 4px 4px 0 #1a1a2e;">

          <!-- Beta Banner -->
          <tr>
            <td style="background-color: #e9c46a; padding: 10px 28px; border-radius: 10px 10px 0 0;">
              <p style="margin: 0; font-family: 'Courier New', monospace; font-size: 13px; font-weight: 700; color: #1a1a2e; text-align: center;">BETA — This digest is auto-generated and may contain errors</p>
            </td>
          </tr>

          <!-- Header -->
          <tr>
            <td style="padding: 20px 28px; border-bottom: 2px solid #1a1a2e;">
              <table role="presentation" width="100%" cellpadding="0" cellspacing="0">
                <tr>
                  <td valign="middle" width="52">
                    <img src="data:image/png;base64,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" alt="Bottlenecks Labs" width="44" height="44" style="display: block; border: 0;">
                  </td>
                  <td valign="middle" style="padding-left: 12px;">
                    <p style="margin: 0; font-size: 16px; font-weight: 700; color: #1a1a2e;">Energy & Permitting Daily Digest</p>
                    <p style="margin: 2px 0 0 0; font-family: 'Courier New', monospace; font-size: 11px; color: #8a8a9a; letter-spacing: 0.05em;">BOTTLENECKS LABS</p>
                  </td>
                  <td align="right" valign="middle">
                    <p style="margin: 0; font-family: 'Courier New', monospace; font-size: 12px; color: #2a9d8f; font-weight: 700;">{html_escape(date_str)}</p>
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
                    <p style="margin: 0; font-family: 'Courier New', monospace; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; color: #2a9d8f;">Top Developments</p>
                    <ul style="margin: 12px 0 0 0; padding: 0 0 0 18px; color: #4a4a5a; font-size: 13px; line-height: 1.6;">
                      {top_devs_html}
                    </ul>
                  </td>
                </tr>
              </table>
            </td>
          </tr>

          <!-- News & Statements -->
          {render_section_header('News & Statements')}
          {news_html}
          {render_section_divider()}

          <!-- Publications -->
          {render_section_header('Publications')}
          {pubs_html}
          {render_section_divider()}

          <!-- Congressional & Executive Activity -->
          {render_section_header('Congressional & Executive Activity')}
          {cong_html}
          {render_section_divider()}

          <!-- Business Activity -->
          {render_section_header('Business Activity')}
          {biz_html}
          {render_section_divider()}

          <!-- China -->
          {render_section_header('China')}
          {china_html}
          {render_section_divider()}

          <!-- Macro Trends -->
          {render_section_header('Macro Trends')}
          {render_macro_trends(macro_trends)}
          {render_section_divider()}

          <!-- What to Watch -->
          {render_section_header('What to Watch This Week')}
          {render_calendar_table(calendar)}
          {render_key_questions(key_questions)}
          {render_section_divider()}

          <!-- Grantee Activities -->
          {render_section_header('Grantee Activities')}
          {grantees_html}
          {render_section_divider()}

          <!-- Limitations -->
          {render_section_header('Limitations & Gaps')}
          {render_limitations(limitations)}

          <!-- Footer -->
          <tr>
            <td style="background-color: #1a1a2e; padding: 20px 28px; border-top: 3px solid #e9c46a; border-radius: 0 0 10px 10px;">
              <p style="margin: 0; font-size: 13px; color: #faf8f5; text-align: center; font-weight: 500;">Compiled by Bottlenecks Labs</p>
              <p style="margin: 6px 0 0 0; font-size: 11px; color: #8a8a9a; text-align: center;">News: 72 hrs · Publications & Grantees: 7 days · Strict cutoffs</p>
            </td>
          </tr>

        </table>
      </td>
    </tr>
  </table>
</body>
</html>'''

    return html


# =============================================================================
# MAIN
# =============================================================================
def main():
    parser = argparse.ArgumentParser(description='Build Energy Digest HTML from structured content')
    parser.add_argument('input', nargs='?', help='Input file (or stdin if not provided)')
    parser.add_argument('-o', '--output', help='Output HTML file')
    parser.add_argument('-d', '--date', help='Date string (default: today)')
    args = parser.parse_args()

    # Read input
    if args.input:
        with open(args.input, 'r') as f:
            content = f.read()
    else:
        content = sys.stdin.read()

    # Parse and build
    sections = parse_content(content)
    html = build_html(sections, args.date)

    # Output
    if args.output:
        with open(args.output, 'w') as f:
            f.write(html)
        print(f"Wrote: {args.output}")
    else:
        # Default output filename
        date_str = datetime.now().strftime('%Y-%m-%d')
        output_path = Path(__file__).parent / 'digests' / f'energy-digest-{date_str}.html'
        output_path.parent.mkdir(exist_ok=True)
        with open(output_path, 'w') as f:
            f.write(html)
        print(f"Wrote: {output_path}")


if __name__ == '__main__':
    main()
