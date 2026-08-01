---
last_updated: 2026-08-01
source_refs:
  - blogs/what-i-look-for-in-product-managers-now.md
  - private/work-email-1.md
  - private/work-email-2.md
  - private/work-strategy-1.md
  - private/work-product-update-1.md
  - private/work-product-update-2.md
  - private/work-quarterly-plan-1.md
---

# Communication Preferences

## General Communication Style

Direct, conversational, specific. Uses real names, links, and concrete details rather than abstractions. Gets to the point but wraps it in enough context for the reader to follow.

## Slack

- Breaks messages into distinct, short messages rather than long paragraphs
- Direct and action-oriented, leans heavily on bullet points
- Prefers async. Uses threads and links to relevant docs
- Will add examples from work Slack when available in private sources

## Work Emails (Monthly Product Updates)

Aaron writes regular monthly product update emails to the broader team. The pattern is consistent:

**Structure:**
- Opens with "Hey all," or "Hey folks," — casual, warm
- Lead paragraph summarizes the month's big story (1-2 sentences). Early updates may be narrative-heavy; sets expectations that future updates will become more metric-driven as real numbers come in.
- "What we're doing" section re-states the product vision in 2-3 sentences (consistent across updates so new readers can jump in)
- "[Month] Updates" section with bolded sub-headers per initiative
- Each initiative gets 2-4 bullet points with metrics and links
- "What's happening this month" section previewing upcoming work
- "How you can help" closing section — specific, actionable asks (introductions, naming feedback, etc.)
- Closes with "Until next month, Aaron" (or omitted in early updates)

**Tone:**
- Authoritative but approachable. Writing as a product leader to peers, not a VP to reports.
- Celebrates wins with data, not superlatives. States the actual metric against the goal it beat, rather than reaching for words like "amazing success."
- Uses customer quotes and named accounts to ground abstract progress.
- Links heavily — to changelogs, presentations, Jira, Google Docs.

**Patterns:**
- Numbers everywhere. Downloads, adoption rates, GMV, percentage changes.
- Uses "thus far" regularly as a time marker.
- Italicized sub-headers for initiative names within sections.
- Ends with a call to action — an open invitation to reply in the team's channel, or a "How you can help" section with specific asks.

## Strategic Communication (Product Ethos)

When communicating strategic direction or change, Aaron's style shifts:

- Opens with historical context to ground the message — years of track record and cumulative customer outcomes, stated as concrete figures rather than adjectives.
- Directly acknowledges uncomfortable truths, including past organizational missteps, in plain language rather than euphemism.
- Sets clear principles, not just tasks. Three principles, each one sentence.
- Uses Q&A format for anticipated concerns. Structures the doc as "questions we imagine you have" with direct answers.
- Balances honesty about uncertainty ("It's an open question") with clarity about what IS decided.
- Uses bold themed titles for strategic pillars — short, memorable phrases, often a metaphor or a call back to fundamentals, rather than descriptive labels.

## Planning Documents (POAs, PRDs)

Creates detailed quarterly plans (POAs) and PRDs. Consistent structure:

**Structure:**
- Opens with an overview paragraph stating what the document covers and its draft status
- "How we see this setting us up for success" section — connects quarterly work to a longer-term milestone (e.g. a beta ready ahead of a major company event)
- Numbered priorities with nested explanations — each priority gets a one-liner summary of what it means in practice
- "Blockers / Dependencies" section with detailed nested bullets spelling out specific technical and organizational requirements
- "Not in scope" section — explicitly calls out what's excluded and why
- "Open Questions / Action Items" section at the end

**Tone:**
- More structured than updates, but still conversational. Uses "we" naturally.
- Honest about uncertainty — "This is still very much in flux but it's a helpful baseline" and "This is interesting for us but may not end up being something we can accomplish."
- Specific about technical requirements in blockers — lists exact capabilities needed rather than vague concerns.

Also creates go-to-market plans. Uses data, customer quotes, and prototypes to make the case. Shares broadly across the company to align teams.

## Presentations

Comfortable presenting. Spoke at NYU's Product Management Club about building products in the age of AI. Uses slides with key points, follows up with detailed blog writeups.

## Speaking Publicly About Work

Aaron writes publicly about product work while holding a full-time role.

- **His opinions are his own, not his employer's.** Any post drawing on his work carries an explicit disclaimer — "This is my opinion and not the official position of my employer (Manychat)." He states it plainly rather than leaving it ambiguous.
- **Teach the transferable lesson.** When writing about ways of working, abstract up to the general principle so a reader can apply it anywhere, independent of where he happened to learn it.

Further constraints on work-related content are in `private.md`.

## Collaboration Preferences

- Async over sync. "No meetings, just trying things and sharing what worked."
- Clear ownership. Divides responsibilities explicitly on pair projects.
- Shared principles over shared process. Aligns on values, then works independently.
- Uses CLAUDE.md and project documentation to maintain continuity across sessions.
- Expects to "connect on Friday as a group to discuss" — uses written communication to set context before synchronous meetings.

## How We Work Together (AI Agents)

Preferences for how Aaron likes AI agents to operate in a working session. (The sections above describe outbound communication style; this is about working mode.)

- **Bias toward action.** When there's enough to act on, act — don't survey options you won't pursue or re-litigate settled decisions. Lead with the recommendation, not an exhaustive menu.
- **Understand before changing.** Read the relevant code/context first; for anything non-trivial, get the lay of the land before editing.
- **Direct and honest.** Push back when something's wrong, risky, or overcomplicated. Report outcomes faithfully — if a test failed or a step was skipped, say so plainly. No flattery.
- **Concise and scannable.** Short, structured answers. Skip preamble and filler.
- **Ship fast, stay simple.** Prefer the smallest version that works; add complexity only when warranted. Be conservative on anything safety-, health-, or money-adjacent.
- **Match the voice.** Before drafting any written content, pull personal-context (`get_writing_style` / `get_all_context`). For social posts, teach and give — no engagement-bait CTAs.
- **Default public, route sensitive to private.** New context is public by default, but anything work-sensitive or moonlighting-adjacent goes in `context/private.md` (gitignored). When in doubt, leave it out.
