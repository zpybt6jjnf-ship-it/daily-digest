# Bottlenecks Labs Design System

**Version:** 1.0
**Last Updated:** January 2026

Use this guide to replicate the Bottlenecks Labs visual identity across any project or medium.

---

## Brand Philosophy

**Clean Retro** — Professional, data-forward design with warm, trustworthy aesthetics. The design balances modern functionality with subtle retro touches: bold borders, offset shadows, gradient accents, and monospace typography for labels.

**Key Principles:**
- Clarity over decoration
- Data should breathe (generous whitespace)
- Warm, approachable professionalism
- Subtle personality through accent colors and typography

---

## Logo

### Logo Mark
A 44×44px dark square containing a stylized mountain range rendered as a gradient line chart.

```svg
<svg width="44" height="44" viewBox="0 0 44 44" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="brandGradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#2a9d8f" />
      <stop offset="50%" style="stop-color:#e9c46a" />
      <stop offset="100%" style="stop-color:#e76f51" />
    </linearGradient>
  </defs>
  <rect x="0" y="0" width="44" height="44" fill="#1a1a2e" />
  <path d="M 0,30.8 L 3.52,28.6 L 7.92,33 L 12.32,22 L 16.72,26.4 L 22,13.2 L 27.28,24.2 L 31.68,19.8 L 36.08,26.4 L 40.48,24.2 L 44,28.6" stroke="url(#brandGradient)" stroke-width="1.32" fill="none" stroke-linejoin="round" />
</svg>
```

### Logo Usage
- Always pair the logo mark with "BOTTLENECKS LABS" in Space Mono
- Minimum clear space: 8px around all sides
- Never stretch, rotate, or recolor the logo

---

## Color Palette

### Primary Colors

| Name | Hex | RGB | Usage |
|:-----|:----|:----|:------|
| **Ink** | `#1a1a2e` | 26, 26, 46 | Primary text, borders, dark backgrounds |
| **Cream** | `#faf8f5` | 250, 248, 245 | Page background, card backgrounds |
| **Paper** | `#ffffff` | 255, 255, 255 | Content containers, elevated surfaces |

### Accent Colors

| Name | Hex | RGB | Usage |
|:-----|:----|:----|:------|
| **Teal** | `#2a9d8f` | 42, 157, 143 | Links, primary actions, positive indicators |
| **Coral** | `#e76f51` | 231, 111, 81 | Highlights, emphasis, arrows/icons |
| **Gold** | `#e9c46a` | 233, 196, 106 | Warnings, special callouts, decorative accents |
| **Navy** | `#264653` | 38, 70, 83 | Alternative dark color, depth |

### Neutral Colors

| Name | Hex | RGB | Usage |
|:-----|:----|:----|:------|
| **Ink Light** | `#4a4a5a` | 74, 74, 90 | Body text, secondary content |
| **Ink Muted** | `#8a8a9a` | 138, 138, 154 | Captions, metadata, disabled states |
| **Border** | `#e8e6e1` | 232, 230, 225 | Subtle borders, dividers |
| **Border Dark** | `#d4d2cd` | 212, 210, 205 | Emphasized borders, dashed lines |

### Gradient

The brand gradient flows from teal through gold to coral:
```css
background: linear-gradient(90deg, #2a9d8f, #e9c46a, #e76f51);
```

Used for: accent bars, logo mark, decorative elements.

---

## Typography

### Font Families

| Font | Usage | Fallbacks |
|:-----|:------|:----------|
| **DM Sans** | Body text, headings | -apple-system, BlinkMacSystemFont, sans-serif |
| **Space Mono** | Labels, metadata, brand name, code | 'Courier New', monospace |

### Font Import
```css
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Mono:wght@400;700&display=swap');
```

### Type Scale

| Name | Size | Weight | Line Height | Usage |
|:-----|:-----|:-------|:------------|:------|
| **Display** | 32px (2rem) | 700 | 1.2 | Hero headlines |
| **H1** | 24px (1.5rem) | 700 | 1.3 | Page titles |
| **H2** | 18px (1.125rem) | 700 | 1.3 | Section headers |
| **H3** | 16px (1rem) | 600 | 1.4 | Subsection headers |
| **Body** | 14px (0.875rem) | 400 | 1.55 | Primary content |
| **Body Small** | 13px | 400 | 1.5 | Secondary content |
| **Caption** | 12px (0.75rem) | 400 | 1.4 | Metadata, captions |
| **Label** | 11px | 600-700 | 1.2 | Uppercase labels |
| **Micro** | 10px | 400 | 1.3 | Fine print |

### Label Style
Uppercase labels use Space Mono with letter-spacing:
```css
font-family: 'Space Mono', monospace;
font-size: 11px;
font-weight: 700;
text-transform: uppercase;
letter-spacing: 0.08em;
color: #2a9d8f; /* or #e9c46a for gold variant */
```

---

## Spacing

Use a consistent 4px base unit:

| Token | Value | Usage |
|:------|:------|:------|
| `space-1` | 4px | Tight gaps, inline spacing |
| `space-2` | 8px | Small gaps, icon margins |
| `space-3` | 12px | Default component padding |
| `space-4` | 16px | Card padding, section gaps |
| `space-5` | 24px | Section padding |
| `space-6` | 32px | Large section margins |
| `space-8` | 48px | Page-level spacing |

---

## Border & Shadow

### Borders
- **Standard border:** 2px solid `#1a1a2e`
- **Subtle border:** 1px solid `#e8e6e1`
- **Dashed divider:** 1px dashed `#d4d2cd`
- **Accent border-left:** 3px solid (teal, coral, or gold)

### Border Radius
| Token | Value | Usage |
|:------|:------|:------|
| `radius-sm` | 4px | Buttons, tags, small elements |
| `radius-md` | 8px | Cards, inputs, containers |
| `radius-lg` | 12px | Large containers, modals |

### Box Shadow (Retro Offset)
The signature retro shadow is a solid offset, not a blur:
```css
box-shadow: 4px 4px 0 #1a1a2e;
```

On hover, increase offset:
```css
box-shadow: 6px 6px 0 #1a1a2e;
transform: translate(-2px, -2px);
```

---

## Components

### Cards

**Standard Card:**
```css
.card {
  background: #ffffff;
  border: 2px solid #1a1a2e;
  border-radius: 12px;
  padding: 24px;
  box-shadow: 4px 4px 0 #1a1a2e;
}
```

**Subtle Card (for nested content):**
```css
.card-subtle {
  background: #faf8f5;
  border-radius: 8px;
  padding: 14px 16px;
}
```

**Highlighted Card (with accent border):**
```css
.card-highlight {
  background: #faf8f5;
  border-left: 3px solid #2a9d8f;
  border-radius: 4px;
  padding: 16px 20px;
}
```

### Buttons

**Primary Button:**
```css
.btn-primary {
  background: #1a1a2e;
  color: #faf8f5;
  border: 2px solid #1a1a2e;
  border-radius: 4px;
  padding: 10px 20px;
  font-weight: 600;
  font-size: 14px;
}

.btn-primary:hover {
  background: #2a9d8f;
  border-color: #2a9d8f;
}
```

**Secondary Button:**
```css
.btn-secondary {
  background: #ffffff;
  color: #1a1a2e;
  border: 1px solid #d4d2cd;
  border-radius: 4px;
  padding: 10px 20px;
}

.btn-secondary:hover {
  border-color: #2a9d8f;
  color: #2a9d8f;
}
```

### Tables

```css
.table {
  width: 100%;
  border-collapse: collapse;
  font-size: 13px;
}

.table th {
  background: #faf8f5;
  padding: 10px 12px;
  text-align: left;
  font-weight: 600;
  color: #1a1a2e;
  border-bottom: 2px solid #d4d2cd;
}

.table td {
  padding: 10px 12px;
  border-bottom: 1px solid #e8e6e1;
  color: #4a4a5a;
}
```

### Links

```css
a {
  color: #2a9d8f;
  text-decoration: none;
  font-weight: 500;
}

a:hover {
  text-decoration: underline;
}
```

Arrow links use the coral arrow:
```html
<a href="#">Read more <span style="color: #e76f51;">→</span></a>
```

### Section Headers

Section headers use a coral highlight effect:
```css
.section-title {
  font-size: 18px;
  font-weight: 700;
  color: #1a1a2e;
}

.section-title span {
  background: linear-gradient(180deg, transparent 55%, rgba(231, 111, 81, 0.3) 55%);
  padding: 0 4px;
}
```

---

## Layout Patterns

### Header
- White background with 2px bottom border
- Logo mark + brand name on left
- Navigation or date on right
- Followed by gradient accent bar (4px height)

### Footer
- Dark background (`#1a1a2e`)
- Gold top border (3px)
- Cream text, centered
- Coverage/metadata in muted color

### Content Container
- Max-width: 640-680px for reading content
- Max-width: 1100px for data/dashboard views
- Centered with auto margins
- Padding: 24-32px horizontal

### Section Dividers
Use dashed borders between major sections:
```css
border-bottom: 1px dashed #d4d2cd;
```

---

## Visual Hierarchy

### Emphasis Techniques

1. **Bold text:** For titles and key terms
2. **Teal color:** For links and primary actions
3. **Coral highlight:** For section headers (gradient background)
4. **Gold accent:** For special callouts and warnings
5. **Monospace:** For labels, metadata, technical content

### De-emphasis Techniques

1. **Muted color (`#8a8a9a`):** For secondary information
2. **Smaller font size:** For captions and metadata
3. **Italic:** For notes and "no data" states

---

## Iconography

- Prefer simple, line-based icons
- Use coral (`#e76f51`) for arrows and directional icons
- Use teal (`#2a9d8f`) for action icons
- Arrow symbol: `→` (Unicode: \2192)
- Bullet replacement: `•` or teal-colored dashes

---

## Motion & Interaction

### Transitions
```css
transition: all 0.15s ease;
```

### Hover States
- Links: underline
- Cards: lift up and increase shadow
- Buttons: color shift to teal

### Focus States
```css
:focus {
  outline: 2px solid #2a9d8f;
  outline-offset: 2px;
}
```

---

## Application Examples

### Email
- Container: white with 2px border, 4px shadow, 12px radius
- Header: logo + brand name, date on right
- Gradient bar below header
- Cards for news items (cream background, no border)
- Dashed dividers between sections
- Dark footer with gold top border

### Web Dashboard
- Cream page background
- White cards with retro shadow
- Monospace labels for data categories
- Teal for interactive elements
- Coral highlights on active/selected states

### Documents/Reports
- DM Sans for body, Space Mono for headers/labels
- Teal for links and callouts
- Gold for warnings/notes
- Tables with cream header row

### Presentations
- Dark title slides (ink background, cream text)
- Light content slides (cream background)
- Gradient accent on title text
- Retro card styling for callout boxes

---

## Code Reference (CSS Variables)

```css
:root {
  /* Colors */
  --color-cream: #faf8f5;
  --color-paper: #ffffff;
  --color-ink: #1a1a2e;
  --color-ink-light: #4a4a5a;
  --color-ink-muted: #8a8a9a;
  --color-teal: #2a9d8f;
  --color-coral: #e76f51;
  --color-gold: #e9c46a;
  --color-navy: #264653;
  --color-border: #e8e6e1;
  --color-border-dark: #d4d2cd;

  /* Typography */
  --font-sans: 'DM Sans', -apple-system, BlinkMacSystemFont, sans-serif;
  --font-mono: 'Space Mono', 'Courier New', monospace;

  /* Spacing */
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-5: 24px;
  --space-6: 32px;
  --space-8: 48px;

  /* Radius */
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
}
```

---

## Do's and Don'ts

### Do
- Use generous whitespace
- Maintain consistent spacing (4px grid)
- Use the gradient sparingly (accent bars, logo only)
- Keep text hierarchy clear (max 3-4 levels)
- Use monospace for labels and metadata
- Apply coral highlight to section headers

### Don't
- Use more than 2-3 accent colors per view
- Apply retro shadow to everything (reserve for main containers)
- Use pure black (`#000000`) — always use ink (`#1a1a2e`)
- Use pure white for backgrounds — prefer cream (`#faf8f5`)
- Overuse the gradient
- Mix too many font weights

---

## Quick Reference

**Brand Colors:** Ink `#1a1a2e` · Cream `#faf8f5` · Teal `#2a9d8f` · Coral `#e76f51` · Gold `#e9c46a`

**Fonts:** DM Sans (body) · Space Mono (labels)

**Key Patterns:**
- 2px solid borders
- 4px offset shadow
- 3px accent border-left
- 1px dashed dividers
- Coral gradient highlight on headers

**Container:** `border: 2px solid #1a1a2e; border-radius: 12px; box-shadow: 4px 4px 0 #1a1a2e;`

---

*This style guide is designed to be imported into AI assistants (Claude, ChatGPT, etc.) to enable consistent design language replication across projects.*
