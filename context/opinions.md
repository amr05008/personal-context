---
last_updated: 2026-08-01
source_refs:
  - blogs/building-products-age-of-ai.md
  - blogs/glutenornot-free-ingredient-scanner-celiac-disease.md
  - blogs/Making-migrations-fun-with-Claude-Code.md
  - blogs/unlocking-revenue-with-product-led-growth.md
  - blogs/useful-and-silly-ways-i-use-chatgpt.md
  - blogs/giving-agents-personal-context.md
  - blogs/what-i-look-for-in-product-managers-now.md
  - blogs/go-get-yourself-a-personal-agent.md
  - blogs/how-to-build-a-personal-morning-briefing.md
---

# Opinions & Perspectives

## On AI & LLMs

- AI tools have fundamentally changed what non-technical people can build. PMs can now undertake almost any technical project — websites, apps, scripts, migrations.
- Claude Code is a standout tool. Used it to migrate an entire WordPress site in 6 hours across two evenings. "This technology is absolutely wild."
- The prompt is the product. In GlutenOrNot, the real value is in the prompt engineering — encoding celiac disease knowledge, tone, and conservative safety defaults.
- LLMs are best used as collaborators, not replacements. Different tools for different jobs.
- Claude is his primary model and the one he builds on. He also runs a range of other models through OpenRouter — one key, swap the model slug — for evaluating what's new and for not being locked to a single provider. ChatGPT stays in the mix for quick lookups and personal tasks.
- Worth staying model-curious. He tries new frontier models as they land rather than assuming today's default is still the best one.
- MCPs (Model Context Protocols) are exciting for connecting LLMs to real data sources. Early adopter — experimented with Strava MCP, built his own.
- Personal context should be curated markdown, not complex infrastructure. Simple files served via MCP beat heavyweight agent systems that require "hundreds of hours of tinkering."
- LLMs should know who they're talking to. Equipping agents with your voice, opinions, and expertise makes every session more useful without repeating yourself.
- The best approach to building personal context is bootstrapping from existing writing (blog posts), then refining through interviews — not starting from scratch.
- Context systems should be LLM-agnostic. Plans to make personal-context portable across models so switching providers doesn't mean rebuilding.
- Personal agents are the highest-leverage thing he's built — "the most useful, the most interesting and now the foundation I layer new projects on top of."
- Scheduled automation belongs in the cloud, not on your laptop. Cloud-run routines fire "even if your computer falls into the ocean"; locally scheduled tasks need the machine awake.
- The repeatable shape of a useful personal automation is prompt → sources → schedule → delivery.

## On the Product Management Craft

- The PM job changed materially in the past 6-12 months. What to build, who for, and why is unchanged — how you reach those decisions and how you communicate them is where the shift happened.
- The move is *toward* learning, shipping, and talking to customers, and *away from* copying and pasting information between tools.
- PMs should be able to design, build, host, and deploy interactive prototypes. Learning from a prototype that a workflow is wrong is far cheaper than learning it from shipped code.
- GitHub fluency is table stakes for product people, not a nice-to-have. "If you say you are a builder and have no commits in the past 12 months on GitHub, that's a yellow flag." Sources of truth reconcile back into GitHub; other tools sit on top of that.
- Most work shouldn't happen in product web UIs anymore. Get what you need through MCPs, APIs, and connectors.
- Building skills to remove friction from repetitive workflows is now core PM work, not overhead. Roughly an hour upfront against a task you repeat produces a compounding bank of insight.
- None of this is gatekeeping. "It's totally okay if you don't know how to do some of these items today." The point is naming what people may not know exists so they can go learn it — everyone is still figuring this out.

## On Product Strategy

- Product-led growth over sales-led, especially for SMB. At Bond, shifting to self-service added $1M+ in revenue and freed the sales team to go upmarket.
- Ship fast, iterate later. Concept to App Store in under a week. "Having seemingly gained back 3 hours, I turned to a project I've kicked down my to do list 100 times."
- The best products remove friction. GlutenOrNot: no accounts, no subscriptions, no analytics tracking users. Just photo → verdict.
- Data and customer feedback win buy-in. He prepares presentations with current data and customer interviews to persuade stakeholders — not just opinions.
- Side projects are the best way to learn. Every new technology he writes about, he learned by building something with it.

## On Building & Making

- Health tools should be free for basic functionality. Charging subscriptions for a simple ingredient lookup "felt wrong."
- Keep it simple. The GlutenOrNot mobile app is 680 lines of code. "We resisted adding features: no scan history, no favorites, no social sharing. Just the core loop."
- Conservative by design for anything involving safety. When uncertain, default to caution, never false confidence.
- Pair building (async) works. Clear ownership + shared principles + no meetings = shipped product in a week.
- Teaching is how he explores a topic in depth, not how he demonstrates authority. "Teaching is one of my favorite ways to explore the depths of a topic I enjoy or am actively digging into."
- Give without asking. Close by handing over something genuinely useful — the repo, the deck, the walkthrough — and let it stand on its own. Never close by soliciting engagement.

## On Startups

- Startups should focus on staying alive. The Wami story is a lesson in resourcefulness — buying robots out of a closing factory, restructuring to survive COVID.
- Know your negotiating position. "We naively didn't recognize how unequal our negotiating power was with the billion-dollar Josten's company."
- Revenue is the best survival strategy. Wami restructured as a "usually profitable, mostly seasonal business" rather than chasing growth.

## On Cycling

- Data analysis is part of the fun. Obsessive about ride metrics, race performance, power numbers.
- Showing up and trying matters more than being fast. "I'm not particularly good nor fast but I had so much fun."
- Cycling communities are welcoming. Practice sessions, local bike shops, and racing leagues are entry points worth seeking out.
