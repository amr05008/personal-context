# Travel profile — example

Example of the travel profile this repo keeps at `context/travel.md` (gitignored — the
real one is private, this shows the shape). Filled with placeholder values. Source
template: a durable-context doc an agent reads before planning any trip, so a flight
search never starts cold.

Written as prose-with-bullets on purpose: an agent reads it as context, not as config.
Say *why* wherever a preference has a reason — the reason is what lets it handle a case
the profile didn't anticipate.

> ⚠️ Placement: this example lives in `docs/`, **not** `context/`, because
> `get_all_context()` in `server.py` globs `context/*.md` — an example there would be
> served to the model as if it were the real profile.

---

## Who's traveling — modes

The first thing to establish. Everything below has a default, and each mode overrides it.
Start with two; add more when a trip proves you need one.

- **Work** — the most common trip type. All the preferences below apply as written.
  I book myself; expense via <corporate card program>. Loyalty accrues to my own
  accounts.
- **With partner** — Overrides: direct flights only, no red-eyes, lodging standard
  goes up (see Lodging).

> If the mode isn't obvious from the request, ask before searching. It changes more than
> anything else here.

## Purpose

- **Work** — booked by me, expensed via <program>. <One line: is a corporate booking
  tool mandatory? If so, the agent's job is a shortlist to paste in, not a search.>
- **Personal** — I book it myself, optimize on my own preferences.

## Home hub

Ranked, with the reason for each — the reason is what makes the ranking usable when the
top choice doesn't work. I live in <neighborhood/city>.

1. **<AAA>** — preferred. <why: ~30-minute cab, primary airline's hub>
2. **<BBB>** — acceptable, especially domestic when <AAA>'s schedule doesn't work.
3. **<CCC>** — never (see hard rules). <why: over an hour away>

## Airlines

- **Preferred: <Airline>.** <why — hub fit, reliability>
- **Status:** <program — tier — what it actually gets me that matters to a search.
  If chasing a tier, say so: it means crediting every flight to <Airline> matters now.>
- **Other accounts held:** <programs held for when I'm forced onto them>
- **Points ecosystems:** <transferable-points cards — changes the miles-price math>
- **Loyalty numbers:** stored in <1Password / keychain> — deliberately **not in this
  file**. Not needed to plan; needed at booking, which I do myself.

**Fallback rule — the important one.** When <Airline> doesn't fly the route, is
meaningfully more expensive, or the only option violates a hard rule below: show the
<Airline> option and the best alternative side by side and let me choose.

## Flight preferences

- **Nonstop strongly preferred.** Worth ~$<X> over a connection; take a connection only
  when there's no nonstop at all.
- **If a stop is unavoidable:** max <1> stop, never a connection under <60> minutes.
- **Time of day:** <preferred departure window, and why>
- **Red-eyes:** <tolerance — and does it differ by mode?>
- **Cabin:** <Comfort+/Main equivalent>. **Never basic economy** — no seat selection,
  no changes. Upgrade when <flight length / price delta>.
- **Seat:** <aisle or window>
- **Bags:** <carry-on only by default? checked when? note bag fees if no status>

## Hard rules (the "never" list)

Negative constraints are more useful than positive ones and almost never get written
down. Anything here disqualifies an option outright.

- Never basic economy.
- Never a connection under <60> minutes.
- Never <airport>.
- <mode-specific nevers — e.g. never a red-eye with partner>

## Constraints

- **<Dietary/medical constraint.>** <What the planner should actually do about it —
  e.g. don't book meals-included packages, don't count on in-flight food.>
- <anything else medical, mobility, timing>

## Lodging — stub

Not built out yet. Enough to start:

- **Work:** <chains that are easy to book and expense; which program has the points>
- **Personal/partner:** <Airbnb vs boutique vs chain — and the comfort bar>
- <walkability / gym / kitchen requirements, by mode>

## What I want back — output contract

Without this you get a wall of flights. With it you get something decidable.

- **At most three options.** For each: routing, total door-to-door time, cash price *and*
  miles price, and one line on why it fits.
- **Name what you rejected and the disqualifier** — "the 6am nonstop was $180 cheaper
  but it's basic economy." This is how I know the rules were actually applied.
- Flag anything where a rule had to be bent, and say which one.
- Don't book. Don't hold. Don't fill in a payment form. I book.

## Learned

Append after every trip. This section is the one that compounds — after five trips it's
worth more than everything above it.

- `<YYYY-MM-DD, route>` — <what the profile got wrong, or the thing I had to explain again>
