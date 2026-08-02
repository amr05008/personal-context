---
date: 2026-08-01
summary: Refreshed all six public context files from the latest published writing, then found and scrubbed internal employer material that had been public in communication.md for months
tags: [context-curation, public-private-boundary, writing-style, opinions]
---

## Summary

Started as a routine refresh — pull the latest aaronroy.com posts into the MCP as writing-style examples. Only one post postdated the last update (`what-i-look-for-in-product-managers-now`, 2026-07-22), which turned out to be a *new mode* (career/advisory) rather than another project narrative. Scope grew from there: opinions, communication, projects, identity, and expertise were all stale relative to the published record, plus a year of LinkedIn posts and a newly launched YouTube channel.

The important part was unplanned. A pre-commit sensitivity sweep — the third Aaron asked for — found `communication.md` had been teaching writing style by quoting internal product updates and strategy docs **verbatim**: a launch metric, a roadmap milestone, three strategy pillar names, and candid internal language about past organizational missteps. Public repo, real name, months of exposure. All paraphrased; the style lesson survives, the payload is gone.

## Changes

- `context/writing-style.md` — new "Advisory posts about work and career" mode (genre framing, the employer disclaimer, section-level starter projects, the reassurance close) + Example 6
- `context/opinions.md` — new "On the Product Management Craft" section; personal agents as the foundation; cloud-run over local scheduling; multi-model practice (Claude primary, OpenRouter for rotation, ChatGPT retained)
- `context/communication.md` — five internal quotes paraphrased; `source_refs` renamed from internal project shorthand to opaque placeholders; short public note on speaking about work
- `context/projects.md`, `context/identity.md` — YouTube channel (@aaron_wa, launched July 2026)
- `context/expertise.md` — prototyping moved off InVision to Claude Design → Claude Code → Vercel; adds skills-building, MCP-over-UI practice, and a teaching/technical-writing section
- `context/private.md` (GITIGNORED) — employer-boundary rules moved here; side-venture clarification (Wami is the only official/revenue side business; the content engine's commercial thesis stays private)
- `README.md` — pre-commit review moved into the numbered update workflow; `sources/blogs` corrected to gitignored; `pytest` documented as a `dev` extra

Commits: `9ebd796` (context refresh + scrub), `56d9547` (README workflow), plus this wrap-up's log commit. Cross-repo: `claude-channels@ec9f69c` taught `/ship` to scan file contents on public repos.

## Decisions

- **Bright line split public/private.** The "my opinions are my own" disclaimer and "teach the transferable lesson" stay public — both are already visible in his published posts. Everything else (never show Manychat work except externally-usable products, hiring rationale, screen-recording hygiene, never quote internal docs) moved to `private.md`. Key enabler: `get_all_context()` globs `context/*.md`, so `private.md` is served locally — moving rules there costs **zero** functionality.
- **Paraphrase over deletion** for the internal quotes. "Celebrates wins with data, not superlatives" teaches the pattern without the real numbers; the specifics were pure downside.
- **Kept the Kimi K3 routing analysis out of `opinions.md`.** Sharp reasoning, but short shelf life — opinions.md is served on every drafting call.
- **Did not add `vibe-coding-a-tour-de-france-app` as a source_ref.** Predates the last update (likely a deliberate skip) and project-narrative mode already has eight refs behind it.

## Notes

- **The rules already existed and weren't followed.** `README.md:226` said to review context files for "internal company information" before committing. `README.md:223` said to use opaque `source_refs` names instead of descriptive ones — exactly what the old internal-shorthand filenames violated. Two documented rules, both in this repo, neither reachable at the moment of decision. That's why the fix was *placement* (into the numbered workflow) rather than new guidance.
- **Three of my errors this session shared one root cause** — treating inference as verified fact: deleted a true ChatGPT claim after reading an adjacent reply as agreement (caught by `/grill` via `expertise.md`); told Aaron a vault note was wrong after misreading "gitignored" as "deleted"; scoped the leak audit to the diff and reported clean twice. Captured in memory as `verify-before-asserting-not-after`.
- Test suite now runnable and green (10 passed) after `uv sync --extra dev` — it had been silently unrunnable, which is why earlier verification fell back to exercising the MCP directly.
- `context/private.md` and `context/travel.md` changes are **local-only** (gitignored) — they will not sync to another machine.
