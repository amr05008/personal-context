---
last_updated: 2026-04-07
source_refs:
  - blogs/glutenornot-free-ingredient-scanner-celiac-disease.md
  - blogs/Making-migrations-fun-with-Claude-Code.md
  - blogs/vibe-coding-a-tour-de-france-app-using-replit-and-google-sheets.md
  - blogs/experiments-with-strava-mcp.md
  - blogs/giving-agents-personal-context.md
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

### Monthly Finances
Local scheduled agent: drop CSVs, run tally.py, generate a Notion page with spending insights and breakdown. Tracks emergency fund and 529 contributions.

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
