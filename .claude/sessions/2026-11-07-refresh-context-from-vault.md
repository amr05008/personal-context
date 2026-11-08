---
date: 2026-11-07
summary: Light refresh from the vault and live channels: bike accounts, three new posts, model-cost opinions, a stale GlutenOrNot privacy claim, and a vaguer finance entry
tags: [context-curation, youtube, writing-style, opinions, public-private-boundary]
---

## Summary

Brought the public context up to date with what's now out there: the new `@aaron_wa_bikes` accounts (YouTube, Instagram, TikTok), `@aaron_wa` as an AI-only channel, and the three posts published since 2026-08-01 (`what-it-costs-to-get-llms-to-produce-usable-work`, `fable-flagged-my-airbnb-camera-scan-as-a-cybersecurity-risk`, `getting-jevvy-with-it`). Then, at Aaron's request, cut the finance project down to a one-line description.

## Changes

- `context/identity.md` — bike links grouped under their own heading; YouTube bullet updated for the channel split
- `context/projects.md` — `@aaron_wa` rewritten with the video list; new entries for bike channels, ride-overlay, and model experiments (cost-per-turn, jev-sandbox); GlutenOrNot updated (barcode/label/menu scanning, overview video, Jev test, cropped-label bug); finance entry made deliberately vague
- `context/opinions.md` — new "On Model Choice and Cost" section; Pi harness; the safeguards-vs-defensive-security take
- `context/expertise.md` — model evaluation, classifier models, ride-overlay; defensive network checks; finance tool chain removed
- `context/writing-style.md` — new "Experiment and tool-test writeups" mode, a note on short takes, and Example 7

Commits: `a3653d2` (refresh), `ace2c2e` (finance entry), plus this log.

## Decisions

- **GlutenOrNot privacy claim follows the newest post.** The Feb post said "no analytics"; the June redesign says "we still don't track what you scan", and the August post analyzes its PostHog data. `opinions.md` and `projects.md` now use the June wording, which also stops contradicting `expertise.md`.
- **Only public sources crossed over.** Channel facts came from the live channels and published posts, not the vault's strategy notes: no view or subscriber counts, no posting rules.
- **One public repo left out on purpose** at Aaron's request until it's ready to promote (recorded in local memory).
- **Finance history left as is.** Earlier commits still show the old pipeline description (no amounts); Aaron chose not to rewrite `main`.

## Notes

- **Use the live channel lists, not the vault, for "what's published."** The vault's YouTube status line was dated 2026-08-19 and missed later videos. `social-watcher youtube-channel-videos --handle aaron_wa` (and `--handle aaron_wa_bikes`) gave the real list for 3 quota units each.
- New posts since a given date: list `~/repos/aaronroy.com/src/content/blog/*.md` by `pubDate` and compare against the `blogs/` entries in each file's `source_refs`.
