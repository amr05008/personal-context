---
last_updated: 2026-11-07
source_refs:
  - blogs/what-it-costs-to-get-llms-to-produce-usable-work.md
  - blogs/fable-flagged-my-airbnb-camera-scan-as-a-cybersecurity-risk.md
  - blogs/getting-jevvy-with-it.md
  - blogs/glutenornot-free-ingredient-scanner-celiac-disease.md
  - blogs/Making-migrations-fun-with-Claude-Code.md
  - blogs/the-twisting-tale-of-our-handwriting-robots.md
  - blogs/building-products-age-of-ai.md
  - blogs/reflecting-on-cx-2025.md
  - blogs/experiments-with-strava-mcp.md
  - blogs/unlocking-revenue-with-product-led-growth.md
  - blogs/giving-agents-personal-context.md
  - blogs/how-to-build-a-personal-morning-briefing.md
  - blogs/go-get-yourself-a-personal-agent.md
  - blogs/glutenornot-redesign.md
  - blogs/what-i-look-for-in-product-managers-now.md
---

# Writing Style

## Voice Characteristics

Aaron writes in a **conversational, first-person voice** that reads like he's talking to a friend who happens to be interested in tech. Key traits:

- **Direct and unpretentious.** He says "I" frequently. No corporate "we" when it's his personal work. No hedging or false modesty, but also no bragging — just stating what happened.
- **Enthusiastic without being breathless.** Genuine excitement comes through ("This technology is absolutely wild") but it's grounded in specifics, not hype.
- **Practical over theoretical.** He shows how things work with real examples, costs, code snippets, and screenshots. He doesn't philosophize about trends — he builds things and writes about what he learned.
- **Self-aware and honest.** Calls out his own mistakes openly ("In retrospect, this was a mistake"), admits when he's "not particularly good nor fast" at something, asks "very silly questions" without caring.

## Sentence Patterns

- **Opens with personal context.** Posts almost always start with "I recently..." or a personal situation that led to the project. The reader gets the "why" before the "what." (Exception: advisory/recommendation posts lead with the thesis instead — "I think you should build a personal agent." — then back it with personal stakes in the next sentence.)
- **Short declarative sentences mixed with longer flowing ones.** "The app works. It's in the App Store. Here's what might come next:" followed by longer explanation.
- **Uses parenthetical asides** to add color or clarification: "(yes, Josten's, the yearbook company)", "(vibe coding = instructing AI agents to write code)".
- **Rhetorical momentum through progression.** He narrates projects chronologically — the problem, what he tried, what happened, what's next. Like a story, not a tutorial.
- **Numbered lists and bullet points** for concrete takeaways, but prose for narrative.

## Vocabulary & Word Choice

- Uses everyday language, not jargon. "Whammy of a prompt" over "comprehensive instruction set."
- Technical terms are explained inline on first use, often in parentheses.
- Uses informal connectors: "Alas," "Thus," "Well," "So" — more literary than corporate.
- Occasional colloquialisms: "gnarly mechanical," "kicked down my to do list 100 times," "off to the races."
- Names specific tools, brands, and people. Not "an AI tool" but "Claude Code." Not "a pizza place" but "Roberta's Pizza."

## Tone Markers

- **Optimistic pragmatism.** Things are exciting and achievable, not overwhelming or risky.
- **Builder's pride without arrogance.** He's proud of what he's built and shares details, but always credits collaborators and tools.
- **Accessible to non-technical readers.** A parent, friend, or non-engineer should be able to follow the narrative even if they skim the code.
- **Mild humor through understatement.** Buying robots out of a closing factory is described matter-of-factly. Side notes about Nashville fried chicken.

## Structural Patterns

- **Blog post structure**: personal hook → problem/context → what he built → how it works (with details) → what's next → links/resources
- **Headers are descriptive, not clever.** "What GlutenOrNot Does," "The main event," "Why It's Free" — clear about what follows. Titles get more room to play ("Getting jevvy with it"), but the headers inside stay plain ("What is Jev?", "First impressions").
- **Ends with forward-looking section.** Almost every post has a "What's Next" or "Helpful Resources" section.
- **Heavy use of inline links** to tools, people, repos, and prior posts. The writing is densely linked.
- **Images and screenshots** are used to show, not just tell. Captions are descriptive.

## Context-Specific Variations

### Blog posts (primary voice)
The patterns above describe this mode. Narrative-driven, detailed, personal.

### Work contexts (inferred from blog tone)
Likely more structured but still direct. Uses data and customer feedback to make cases. Comfortable with slide decks and PRDs. "I had to win over hearts and minds" suggests persuasive but not aggressive.

### Advisory posts about work and career
When the subject is his profession rather than a side project, a few extra moves show up:

- **Names the genre and the audience early.** "Consider this post an open letter to product managers looking for their next role..." The reader knows what they're reading and whether it's for them within the first few paragraphs.
- **Establishes standing, then disclaims it.** "I'm writing this as someone who hires and mentors product managers, so this comes from my experience and perspective. This is my opinion and not the official position of my employer (Manychat) so do with this information what you will." Credibility first, then explicit separation from the employer — include this disclaimer whenever a post draws on his work at Manychat.
- **States the through-line before the sections start.** Usually a one-sentence more-X-less-Y contrast: "more time spent on learning, shipping and interacting with customers, and less time spent on copying and pasting information between tools."
- **Every section ends with a way in.** Each recommendation is followed by a concrete starter project and a link — the teaching-first, give-without-strings instinct applied section by section, not just at the end.
- **Blunt judgments stay soft.** "If you say you are a builder and have no commits in the past 12 months on GitHub, that's a yellow flag." A yellow flag, not a dealbreaker.
- **Closes with an open door, not a CTA.** "feel free to email me" — offering his own time is consistent with the no-engagement-bait rule below, not an exception to it.

### Experiment and tool-test writeups
When the post reports on testing models or a new tool (cost-per-turn, Jev), the narrative gives way to evidence:

- **States the scale of the test up front.** "What follows are my observations after 309 model runs across four experiments and $45.71 in cold hard cash." Run counts, dollars, and dataset sizes come early, so the reader knows how much weight the findings can carry.
- **Defines the bar before the results.** He says what "usable" means and that he's the judge of it, then sticks to it, even when the agent thought its run succeeded.
- **Results go in tables; reactions go in prose.** Each experiment shows the exact prompt verbatim in code formatting and a results table (runs, spend, usable, $ per usable); most add a passing and a failing example as captioned screenshots; then comes what he made of it.
- **A recurring verdict line.** Each section ends on the same bolded question ("**Would I recommend giving this task to models?**") with a direct answer: "Yes," "ABSOLUTELY," or a qualified "use it for the bones, write it by hand."
- **Says what he expected, then whether he was right.** "I guessed before I ran the experiment on the local model it would score something like 9 out of 20 runs producing a usable result." Then the real number, and "Yeah, that's not good."
- **Owns the flaws in his own method and his own product.** He names where the experiment was weak (too few runs, memory carrying over between sessions) and reports a bug the test turned up in GlutenOrNot instead of leaving it out.
- **Ends on the takeaway and the repo.** A plain-language rule of thumb, then the public repo with the full prompts and results so anyone can rerun it.

Short takes follow the same honesty in fewer words: the situation, the exact prompt, what happened, a sanity check against another model, then a firm but fair opinion that ends on what he hopes changes, not a complaint (the Fable network-scan post).

### Social posts (LinkedIn and similar)
**Teach and give, don't ask for engagement.** Aaron does not want CTAs that invite the audience to comment, react, or "let him know what you think." His close is to hand over something genuinely useful — a repo people can try themselves, a stripped-down version of the deck he presented, or other resources — and let the value speak for itself. This give-without-strings approach reflects his teaching-first ethos and reliably earns engagement on its own without explicitly soliciting it. When drafting a social post, default the ending to "here's something useful, go try it" rather than a question or discussion prompt.

## Annotated Examples

### Example 1: Opening with personal stakes
> "I recently was diagnosed with celiac disease. With this diagnosis comes a whole lot of questions about what ingredients are safe, not safe, or questionable to consume if you want to avoid getting sick."

**Why this works:** Immediately personal, immediately relatable. The reader understands the stakes (health) before hearing about the product. No preamble about "the state of food tech."

### Example 2: Honest self-assessment
> "Both Aaron and I are product people by trade. We've both played roles in building all sorts of products over the years, but neither of us would call ourselves 'engineers'. Thankfully Claude Code was there to help both of us turn our ideas into reality."

**Why this works:** Positions himself clearly — product person, not engineer. Doesn't pretend to be something he's not. The "thankfully" shows genuine appreciation for the tools without being an ad.

### Example 3: Narrative momentum through specifics
> "After the ink dried on our contract with Newell to purchase the assets, we flew down to Nashville, rented a 26-foot Penske truck, and got to work."

**Why this works:** You can see the story. "26-foot Penske truck" is a specific detail that makes it real. The sentence moves forward — signed, flew, rented, worked. No filler.

### Example 4: Leading with the recommendation (advisory posts)
> "I think you should build a personal agent. Out of all the fun and wild stuff I've explored this past year personal agents are the most useful, the most interesting and now the foundation I layer new projects on top of."

**Why this works:** When the post is advice rather than a project story, he flips the usual order — the thesis comes first ("I think you should build a personal agent"), then the personal stakes back it up. Direct second-person, no hedging, but credibility lands immediately because the next sentence is grounded in his own experience ("this past year," "I layer new projects on top of").

### Example 5: Self-deprecating specificity
> "While the prior version worked, it looked like a health app from 2014. Teal everywhere, a generic leaf logo, and the scan verdict crammed into a little pill."

**Why this works:** The criticism is aimed at his own earlier work, which makes it disarming rather than harsh. And it's vivid because it's specific — "a health app from 2014," "teal everywhere," "crammed into a little pill" — not a vague "it looked dated." Concrete details do the work of the judgment.

### Example 6: Lowering the barrier before the close (advisory posts)
> "**It's totally okay if you don't know how to do some of these items today.** You absolutely can learn them and be up to speed in no-time if you start exploring and experimenting. [...] We are all still figuring out how to adjust to this rapidly changing world."

**Why this works:** After a post full of things the reader might not know how to do, the bolded reassurance arrives before they can feel behind. "We are all still figuring out" puts him in the same boat rather than above it — he's giving standards without making them a judgment. Then he hands over an ordered first step so "you can learn this" comes with somewhere to actually start.

### Example 7: The lesson inside the data (experiment writeups)
> "What was even more wild for Kimi K3 is that on 6 out of 20 runs it surfaced 5 action items, but the issue was that they were not the right action items. **Had I not reviewed these outputs myself and just relied on the quantity of action items surfaced, I would've missed these failing results.**"

**Why this works:** The finding is specific (6 of 20 runs, 5 items, the wrong ones), and the bolded sentence turns it into a lesson anyone using models can apply. He doesn't say "always review AI output" in the abstract; he shows the exact moment where not reviewing would have burned him. The conversational "What was even more wild" keeps a results section from reading like a lab report.
