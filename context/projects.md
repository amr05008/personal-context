---
last_updated: 2026-11-07
source_refs:
  - blogs/glutenornot-free-ingredient-scanner-celiac-disease.md
  - blogs/glutenornot-redesign.md
  - blogs/what-it-costs-to-get-llms-to-produce-usable-work.md
  - blogs/getting-jevvy-with-it.md
  - blogs/Making-migrations-fun-with-Claude-Code.md
  - blogs/vibe-coding-a-tour-de-france-app-using-replit-and-google-sheets.md
  - blogs/experiments-with-strava-mcp.md
  - blogs/giving-agents-personal-context.md
  - blogs/how-to-build-a-personal-morning-briefing.md
---

# Projects

## Active Projects

### Manychat (Work)
Product Director at Manychat, a chatbot/messaging automation (chat marketing) platform. Currently building Manychat for Brands. Remote position.

### GlutenOrNot
Free ingredient scanner for celiac disease. Web (PWA) + iOS app. Scans a barcode, an ingredient label, or a restaurant menu (including labels and menus in other languages): barcode scans look up the ingredient list in product databases, photo scans use Google Cloud Vision OCR, then Claude checks the text for gluten and returns a safe/caution/unsafe verdict. No accounts, no subscriptions, and it doesn't track what you scan. Built in under a week with Aaron Batchelder; redesigned June 2026.
- Site: glutenornot.com
- Repo: github.com/amr05008/glutenornot.com
- iOS App Store: available
- Overview video: youtube.com/watch?v=g6qqkZzcHJE
- Speed is the open problem — responses can take 5+ seconds, which hurts on bad connections. In September 2026 he tested TypeSafe's Jev as a fast first-pass classifier (17x faster and ~240x cheaper than the current model on ~1,000 labels, with neither missing a label that visibly contained gluten); the plan under consideration is Jev first, routing hard cases to a frontier model. The test also surfaced a bug: cropped labels missing the flour line were being called safe.

### aaronroy.com
Personal blog built with Astro 5, Tailwind CSS, deployed on Vercel. Migrated from WordPress in ~6 hours using Claude Code. 40+ posts spanning product, AI, 3D printing, cycling, startups. The hub for his writing, videos, and experiments; readers can opt into occasional email roundups (Buttondown).
- Repo: github.com/amr05008/aaronroy.com

### Personal Context System
Curated markdown files (identity, writing-style, opinions, expertise, projects, communication) served via FastMCP MCP server so any Claude Code session can pull voice, opinions, and style automatically. Inspired by Karpathy's LLM Wiki and nlwhittemore's Personal Context Portfolio. Bootstrapped by ingesting blog posts, then refined through Claude Code interviews. Uses a gitignored `sources/private/` directory for sensitive materials like work emails. Open-source.
- Repo: github.com/amr05008/personal-context
- Blog: aaronroy.com/giving-agents-personal-context/

### Scheduled Agents
Daily briefing agent that pulls weather + RSS feeds and posts to Discord. Built as an alternative to the OpenClaw agent "King Ziti" — which ran on a Raspberry Pi 5 and handled tasks like researching swimming classes, sending email reports, and managing shared task lists via Discord. King Ziti required "hundreds of hours of tinkering" to maintain. Scheduled Agents aims to replicate those benefits with less overhead by combining with the personal-context system.
- Repo: github.com/amr05008/scheduled-agents

### Daily Briefing
A Claude Code routine that delivers a personalized morning briefing — local weather with a cyclist's slant (wind conditions) layered with favorite RSS feeds. Runs as a Claude Code routine on Anthropic's cloud (created via the `/schedule` command), so it executes regardless of whether his computer is on — unlike Claude Cowork's Scheduled Tasks, which require the machine to stay active. Aaron taught a hands-on Manychat workshop on building these (six TAs, exercises following a prompt → sources → schedule → delivery pattern; later exercises layer in connectors like Slack).
- Repo: github.com/amr05008/daily-briefing
- Blog: aaronroy.com/how-to-build-a-personal-morning-briefing/

### YouTube Channel (@aaron_wa)
Launched July 2026 at youtube.com/@aaron_wa. The AI-builder channel: hands-on how-to builds and tool tests — Claude Code, agents, MCPs, and new models, tried on real projects rather than reviewed from a changelog. Videos so far: a note-taking project in GitHub, an interactive prototype with Claude Design + Claude Code, Kimi K3 in Zed via OpenRouter, the Claude Code status line (costs and usage limits), setting up the Pi coding agent, a GlutenOrNot app overview, and adding Strava data to bike videos with HyperFrames. Older Zwift and cyclocross uploads stay on this channel, but new bike footage goes to @aaron_wa_bikes. The format: open by showing the finished thing working, and close on a give (a repo or writeup) rather than a subscribe ask or a comment prompt.

### Bike Channels (@aaron_wa_bikes)
Started October 2026, same handle on YouTube (youtube.com/@aaron_wa_bikes), Instagram (instagram.com/aaron_wa_bikes), and TikTok. Cycling kept separate from the AI work: low-effort, frequent POV clips — cyclocross practice and races, park laps, rides while traveling — as full videos plus Shorts/Reels, many with a ride-data overlay. Instagram is the everyday channel; TikTok mirrors it. Longer race reviews and wrap-ups go on aaronroy.com under the bikes and cyclocross categories. AI×cycling builds (like ride-overlay) stay on @aaron_wa because they're AI builds.

### Ride Overlay
A Claude Code skill that puts ride data (power, heart rate, speed) from a FIT file onto action-camera footage using HyperFrames (HeyGen's open-source HTML-to-MP4 renderer). Built to get more control over overlays than Insta360 Studio offers; the look can be changed by prompting (e.g. km/h → mph). It's how the overlays on his bike Shorts and Reels get made.
- Repo: github.com/amr05008/ride-overlay
- Video: youtube.com/watch?v=36zoCF5suIE

### Model Experiments
Public test benches for figuring out which model is worth using for a job:
- **cost-per-turn** — 309 runs across four tasks (PostHog analysis, slide decks, release notes, action-item extraction) and multiple models, harnesses, and effort levels, measuring cost per *usable* result rather than per token. Repo: github.com/amr05008/cost-per-turn · Blog: aaronroy.com/what-it-costs-to-get-llms-to-produce-usable-work/
- **jev-sandbox** — tests of TypeSafe's Jev, a "System One" decision model that returns probabilities instead of text, against GlutenOrNot labels and email triage. Repo: github.com/amr05008/jev-sandbox · Blog: aaronroy.com/getting-jevvy-with-it/

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
