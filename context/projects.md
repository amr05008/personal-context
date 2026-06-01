---
last_updated: 2026-06-01
source_refs:
  - blogs/glutenornot-free-ingredient-scanner-celiac-disease.md
  - blogs/Making-migrations-fun-with-Claude-Code.md
  - blogs/vibe-coding-a-tour-de-france-app-using-replit-and-google-sheets.md
  - blogs/experiments-with-strava-mcp.md
  - blogs/giving-agents-personal-context.md
  - blogs/how-to-build-a-personal-morning-briefing.md
---

# Projects

## Active Projects

### ManyChat (Work)
Product role at ManyChat, a chatbot/messaging automation platform. Remote position.

### GlutenOrNot
Free ingredient scanner for celiac disease. Web (PWA) + iOS app. Takes a photo of an ingredient label, uses Google Cloud Vision OCR + Claude for analysis, returns safe/caution/unsafe verdict. No accounts, no subscriptions, no tracking. Built in under a week with Aaron Batchelder.
- Site: glutenornot.com
- Repo: github.com/amr05008/glutenornot.com
- iOS App Store: available

### aaronroy.com
Personal blog built with Astro 5, Tailwind CSS, deployed on Vercel. Migrated from WordPress in ~6 hours using Claude Code. 34 posts spanning product, AI, 3D printing, cycling, startups.
- Repo: github.com/amr05008/aaronroy.com

### Personal Context System
Curated markdown files (identity, writing-style, opinions, expertise, projects, communication) served via FastMCP MCP server so any Claude Code session can pull voice, opinions, and style automatically. Inspired by Karpathy's LLM Wiki and nlwhittemore's Personal Context Portfolio. Bootstrapped by ingesting blog posts, then refined through Claude Code interviews. Uses a gitignored `sources/private/` directory for sensitive materials like work emails. Open-source.
- Repo: github.com/amr05008/personal-context
- Blog: aaronroy.com/giving-agents-personal-context/

### Scheduled Agents
Daily briefing agent that pulls weather + RSS feeds and posts to Discord. Built as an alternative to the OpenClaw agent "King Ziti" — which ran on a Raspberry Pi 5 and handled tasks like researching swimming classes, sending email reports, and managing shared task lists via Discord. King Ziti required "hundreds of hours of tinkering" to maintain. Scheduled Agents aims to replicate those benefits with less overhead by combining with the personal-context system.
- Repo: github.com/amr05008/scheduled-agents

### Daily Briefing
A Claude Code routine that delivers a personalized morning briefing — local weather with a cyclist's slant (wind conditions) layered with favorite RSS feeds. Runs as a Claude Code routine on Anthropic's cloud (created via the `/schedule` command), so it executes regardless of whether his computer is on — unlike Claude Cowork's Scheduled Tasks, which require the machine to stay active. Aaron taught a hands-on ManyChat workshop on building these (six TAs, exercises following a prompt → sources → schedule → delivery pattern; later exercises layer in connectors like Slack).
- Repo: github.com/amr05008/daily-briefing
- Blog: aaronroy.com/how-to-build-a-personal-morning-briefing/

### Monthly Finances
Automated monthly finance pipeline: **SimpleFin Bridge → SQLite → Claude → Notion**. Runs unattended on macOS `launchd` schedules — a daily pull + LLM categorization (Claude Sonnet 4.6, with a forever merchant cache), a monthly report on the 1st that synthesizes spending insights (Claude Opus 4.8) into a Notion page, and a weekly healthcheck that catches stale/frozen bank feeds. Discord pings on failures. Replaced the legacy `tally.py` + CSV-drop workflow and has been the only pipeline since the May 2026 auto-run. Tracks category budgets, an emergency-fund target, and 529 contributions (sensitive config kept gitignored).

## Notable Past Projects

### Fantasy Tour de France App
Vibe-coded alternative UI for a fantasy cycling competition. Originally built on Replit with Google Sheets, later migrated to Streamlit.
- Live: fantasytour.streamlit.app

### Wami (Co-founder)
Handwriting robot company. Purchased robots from Bond/Newell Brands after the company was shut down. Runs a seasonal business sending luxury brand loyalty notes (Kering, Richemont, LVMH). Production studio in Bushwick, Brooklyn.
- Site: wami.io

### Bond (Employee → Wami transition)
Robotic handwritten notes at scale. Built PLG features that added $1M+ in self-service revenue. Shut down by parent company Newell Brands in 2018.

### 3DPrinterOS
Earlier career — platform for managing fleets of 3D printers at scale. Taught 3D printing courses.
