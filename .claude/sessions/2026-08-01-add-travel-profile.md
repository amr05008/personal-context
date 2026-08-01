---
date: 2026-08-01
summary: Added a private travel profile (interview → file → live retro-test against a real booking), public example, and the vault-symlink storage architecture
tags: [travel-profile, privacy, mcp]
---

## Summary

Built the travel profile from the vault template (`~/repos/vault/templates/travel-profile-template.md`) via a section-by-section interview, then validated it by re-running an already-booked JFK⇄LAX trip (Aug 6–7) as if planning cold. The profile's shortlist contained the exact booked return flight and airline/routing; three divergences were folded back into the profile, proving out the `## Learned` loop on day one.

## Changes

- `context/travel.md` — the filled profile (GITIGNORED; now a **symlink** to `~/repos/vault/areas/travel/travel-profile.md`, canonical copy in the private vault repo for backup/sync)
- `docs/travel.example.md` — public placeholder example; deliberately outside `context/` because `get_all_context()` globs `context/*.md`
- `.gitignore` — added `context/travel.md` and `.playwright-mcp/` (browser-test snapshots were landing in the working tree)
- `README.md` — documented the gitignored-served-context pattern (symlinks, example placement, no account numbers)
- vault commit `754b347` — canonical profile copy

Commits here: `b0525e1` (example + gitignore), `613b7c9` (playwright gitignore), plus this wrap-up's doc/log commit.

## Decisions

- **No `get_travel_profile()` tool yet.** Schema still settling; the file is already served via `get_all_context()`. Add the tool (matching `get_writing_style()`) after 2–3 real trips settle the shape.
- **Canonical file lives in the private vault, symlinked into `context/`.** Solves backup (vault is a private GitHub repo) without weakening the public-repo boundary — the gitignore covers the symlink.
- **M3-only.** The profile never goes on a work machine; the handoff artifact is the output-contract shortlist (self-contained, nothing sensitive), pasted to wherever booking happens.
- **Account numbers stay in 1Password** — the SkyMiles number appeared in a shared screenshot and was deliberately never written anywhere.

## Notes

- Retro-test learnings already folded in: time-of-day preference was wrong in the interview (real rule: early-afternoon departures — morning at home + JFK rush-hour avoidance); work lodging rule refined (boutique-inside-Bonvoy is the sweet spot, e.g. Hotel June West LA).
- Open question for next booking: cabin rule may be "extra legroom, cheapest tier that has it" (booked Main Extra out / Comfort Extra back) rather than "Comfort+ at 3hr+".
- Known search-flow gaps: Google Flights defaults to including basic economy (must switch to "Economy (exclude Basic)" — it moved JetBlue's real price $765→$875); miles prices need a delta.com award-search step.
- Machine-local memory `travel-profile-workflow` (this project's auto-memory) carries the where-it-lives + how-to-run recipe.
