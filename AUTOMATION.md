# Daily Digest Automation

Automated generation and distribution via GitHub Actions.

## Overview

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│  GitHub Actions │  →  │   Claude API    │  →  │   Gmail SMTP    │
│  (daily 6am ET) │     │  (web search)   │     │  (send email)   │
└─────────────────┘     └─────────────────┘     └─────────────────┘
                               ↓
                    ┌─────────────────┐
                    │  Save to repo   │
                    │  (digests/)     │
                    └─────────────────┘
```

**Cost:** Free (GitHub Actions) + Claude API usage (~$0.50-2.00/day depending on searches)

---

## Setup Instructions

### Step 1: Create GitHub Repository

1. Go to [github.com/new](https://github.com/new)
2. Create a new **private** repository named `daily-digest`
3. Clone it locally or push this folder to it:

```bash
cd "/Users/skarl/Documents/Daily Digest"
git init
git add .
git commit -m "Initial commit"
git remote add origin git@github.com:YOUR_USERNAME/daily-digest.git
git push -u origin main
```

### Step 2: Get API Keys

**Anthropic API Key:**
1. Go to [console.anthropic.com](https://console.anthropic.com)
2. Navigate to API Keys
3. Create a new key and copy it

**Gmail App Password:**
1. Go to [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords)
2. Select "Mail" and your device
3. Copy the 16-character password

### Step 3: Add GitHub Secrets

1. Go to your repo → Settings → Secrets and variables → Actions
2. Add these secrets:

| Secret Name | Value |
|:------------|:------|
| `ANTHROPIC_API_KEY` | Your Anthropic API key |
| `GMAIL_ADDRESS` | Your Gmail address |
| `GMAIL_APP_PASSWORD` | 16-character app password |
| `RECIPIENT_EMAIL` | Email to receive digest (can be same as GMAIL_ADDRESS) |

### Step 4: Enable GitHub Actions

1. Go to your repo → Actions tab
2. If prompted, enable workflows
3. The workflow runs automatically at 6am ET daily

### Step 5: Test It

1. Go to Actions → "Daily Digest" workflow
2. Click "Run workflow" → "Run workflow"
3. Watch the logs to verify it works

---

## Configuration

### Change Schedule

Edit `.github/workflows/daily-digest.yml`:

```yaml
schedule:
  - cron: '0 11 * * *'  # 6am Eastern (UTC-5)
```

Common schedules:
- `'0 11 * * *'` → 6am ET
- `'0 12 * * *'` → 7am ET
- `'0 13 * * 1-5'` → 8am ET, weekdays only

Use [crontab.guru](https://crontab.guru) to build cron expressions.

### Skip Email (Generate Only)

Remove or comment out the "Send email" step in the workflow.

### Multiple Recipients

Set `RECIPIENT_EMAIL` to a comma-separated list, or modify `send_digest.py` to loop through multiple addresses.

---

## Local Testing

Test generation locally:

```bash
export ANTHROPIC_API_KEY="your-key"
python scripts/generate_digest.py --dry-run
```

Test full flow:

```bash
export ANTHROPIC_API_KEY="your-key"
export GMAIL_ADDRESS="your@gmail.com"
export GMAIL_APP_PASSWORD="your-app-password"
python scripts/generate_digest.py --send
```

---

## Troubleshooting

### Workflow not running

- Check Actions tab for errors
- Ensure secrets are set correctly (no extra spaces)
- Verify cron schedule is correct

### Email not sending

- Verify Gmail App Password (not your regular password)
- Check that 2FA is enabled on your Google account
- Look at workflow logs for specific error

### Digest quality issues

- Claude's web search has usage limits
- Some sources may be paywalled or unavailable
- Edit the prompt in `generate_digest.py` to adjust sources

### API rate limits

- Anthropic: Check your usage at console.anthropic.com
- Gmail: 500 emails/day limit for regular accounts

---

## Files

| File | Purpose |
|:-----|:--------|
| `scripts/generate_digest.py` | Calls Claude API to generate digest |
| `scripts/send_digest.py` | Sends HTML email via Gmail |
| `scripts/email_template.html` | Email HTML template |
| `.github/workflows/daily-digest.yml` | GitHub Actions workflow |
| `digests/` | Generated digest files (auto-committed) |

---

## Estimated Costs

| Service | Cost |
|:--------|:-----|
| GitHub Actions | Free (2000 mins/month for private repos) |
| Claude API | ~$0.50-2.00/day (depends on web search usage) |
| Gmail | Free |

**Monthly estimate:** $15-60 for Claude API
