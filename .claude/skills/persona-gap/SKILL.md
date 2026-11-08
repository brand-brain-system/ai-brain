---
name: persona-gap
description: Build evidence-based personas and audit a brand's ads against them (persona-gap, personas, avatars, customer avatar, category entry points, triggers, ad account audit, ad library analysis, awareness audit, funnel gaps). Mode A builds trigger-based personas from real customer language, ranked by how much evidence backs each one, with every field labelled and audited by an agent that didn't write it. Mode B tags every ad a brand runs (Meta Ad Library, or the ad account) by persona, awareness, funnel stage, format and message, and shows where the gaps are, in a spreadsheet and a written diagnosis. Use when someone wants to build or rebuild personas, analyse an ad account or a competitor's ads, research a potential employer or client, or find which customers the ads miss.
---

# Persona-gap: personas from evidence, ads against personas

Two modes. Run A before B when the brand has no evidenced personas yet; B without A falls back on
the brand's own categories (occasions, product lines), which shows what the brand sells, not who
buys.

- **Mode A: build personas.** From `source-pulls/` (or a fresh pull) to `personas/personas-profile.md`
- **Mode B: ad audit.** Every ad the brand runs, tagged, counted against the personas, as a
  spreadsheet plus `analyse.md` and the one-sentence diagnosis

First runs (Sep-Oct 2026): four public-data test brands, ending with a 511-ad audit of the golf test brand.
The counting, tagging and PDF-showcase code from those runs is not in the factory yet (`REWRITE-QUEUE.md`);
write it fresh from the steps below and save it in the run's `audits/` folder, so the next run reuses it.

**Every table says its limit, every time.** Without account access, *share of ads* stands in for
*share of spend*, and reviews are not customers.

## Mode A: build personas

A persona is defined by **when** someone enters the category (the trigger), not who they are. The
card template is `templates/brand-scaffold/personas/personas-profile.md` in the factory.

**A1. Gather evidence, not opinions.** Reviews (all star ratings: the negatives carry the best
language), Reddit and forum posts asking for help, search queries, ad comments, post-purchase
surveys, support tickets. `source-pulls/README.md` in the scaffold says which sources show the
trigger; reviews are weak on it. Save verbatim with source, date and id. Keep unweighted pulls and
keyword-searched pulls in separate files: only the unweighted one gives shares.

**A2. Find the entry moments.** Read everything (a compact one-line-per-post file, never the raw
JSON). Then answer, in this order, and quote for each:
- What was happening right before they looked for a solution?
- What did they try or use before, and why did it stop being good enough?
- What did they want instead, in their words?

Write each recurring moment as one line, with the quotes under it.

When there is a lot of material, build the `research-map` first (`.claude/skills/research-map/`): every quote saved once with its link, grouped, counted by different people. A3 then reads its counts, and each card cites the groups it rests on.

**A3. Rank by evidence strength.** Per moment: how many separate posts back it, from how many
different sources, and whether it appears in the unweighted pull. Table: moment | posts | sources |
unweighted share | example id. A moment backed by one post is a lead for `hypotheses/`, not a
persona (the pitch test brand: the occasion buyer, 1 of 200, dropped). Show the ranking to the human before
writing cards.

**A4. Write the cards.** One per moment that survives, in the template. Since 12 Oct 2026 the template has
four fields that research rarely fills unprompted, so look for them on purpose: **solutions tried before**
(how many, with quotes), the **inaction story** (what they tell themselves for not fixing it), **horror
stories** about alternatives (one about the brand's own product is an objection, never ad material), and the
**belief state** (hopeful, skeptical, cynical, resigned). Each is Data-limited when nobody says it. **Every field gets its own
label and source**, not one evidence line for the whole card: Verified (a quote or post says it,
with id), Inferred (name what it rests on, and that must itself be Verified), Data-limited (can't
be answered from the data). The field most often invented is *emotional need*; leave it
Data-limited rather than filling it with something plausible.

**Save a quote for every claim as you write it.** The engraving test brand, 29 Sep: the first audit flagged 24 of 64
fields, nearly all true things read in the full reviews but never saved as a quote. Keep quotes
short (under 15 words, with id) rather than storing full review texts, and check each one word for
word against the source in the browser (`text.includes(quote)`) before the audit.

**A5. Audit: find the unsupported.** A subagent on Sonnet that didn't write the cards gets only
`personas.md` and the source files. For every field it returns one of:
- **found:** the quote exists in the source, with file and id
- **inferred, holds:** it names what it rests on, and that is found
- **unsupported:** it can't be traced to the data

Unsupported is not a label that stays in the brain: the field is deleted or becomes Data-limited,
and the question goes to `running-notes/missing-context.md`. However good it sounds. Report the counts
(found / inferred / unsupported) with the cards.

**A6. Finish check.** Before a card is used: no invented person (demographics only where evidence
shows them and they change the ad); triggers and behaviour, not traits; every field traceable; and
"Ad this suggests next" is filled in, so the team knows what to make. A card that fails the last
one isn't done.

## Mode B: ad audit

**B1. Pull the ads (browser).** Meta Ad Library, country DK, active, search the brand name. Extract
card by card from the DOM, not the flat page text: library id, start date, body, headline, CTA, link,
format (image / video / carousel / catalogue, "flere versioner"), and **impression rank**. The
library sorts by total impressions (`sort_data[mode]=total_impressions` in the URL): keep each
card's rank. The page loads 30 cards at a time: `scrollIntoView` on the last card and repeat until
the count stops (the engraving test brand, 29 Sep: 80). Save as `ads-<date>.json`. Write the extractor fresh and keep it in the run's `audits/` folder.

With account access, pull spend, purchases, CPA, hook rate and frequency per ad instead of rank,
and the audit stops being a proxy.

**B2. Tag every ad with written rules.** Copy `tag.js` and adapt the word lists. Columns:

| Column | Values | How it's read |
|---|---|---|
| Persona | the Mode A personas, or "none/generic" | which trigger the copy speaks to |
| Occasion / product line | the brand's own categories | what the ad sells. Keep separate from persona: a lingerie ad about price speaks to the online shopper |
| Awareness | unaware / problem / solution / product / most aware | what the copy assumes the reader already knows |
| Funnel stage | TOF / MOF / BOF / x | **who the ad was delivered to, never derived from awareness** (a product-aware ad can be the biggest cold ad; `creative-vocabulary.md`, Funnel stage). Our account: the audience-segment breakdown or the ad set's targeting, labelled Seen. Ad Library and competitors: delivery is invisible, so `x`. The gap read uses the awareness column, not this one |
| Message track | the argument: e.g. memory, free engraving, speed, price, quality proof, human | the one reason the ad gives |
| Pull | pain / desire / neither | pain: the ad starts from a problem the viewer has; desire: it only makes the product look good to have (the campaign-shoot style); neither: price or offer only |
| Format | static / video / carousel / catalogue; creator or partnership | read off the card |
| Human | none / staff named / customer / creator | who is on screen or named |
| Concept | a cluster id | ads that make the same argument in the same shape are one concept (Meta groups them too) |
| Start date, rank, cohort rank | from B1 | compare rank only within the same start date |
| Hygiene | wrong numbers, field errors, outdated claims | anything the brand would want fixed |

Run, read the tags through, fix the rules, run again. The first run usually has a dozen or more
errors. Manual corrections go in the script with the reason. Versatility clichés ("for everyday and
parties") are not a persona angle.

**B2b. Tear down the ads that matter.** Tags from copy miss what the video and image show. Watch the top
10-20 by delivery (plus one or two per concept) and fill the twelve fields in `ad-teardown.md`. Near-identical
ads: tear down one, count its twins. Skipped: say in `analyse.md` that the videos weren't watched.

**B3. Count the gaps.** Share of customer voice per persona (from the unweighted pull) against
share of ad units and of concepts. Plus the **persona × awareness matrix**: empty cells are the
gaps. Reviews with no signal are left out and counted. Plus the **pain vs. desire split** (share of ad
units): one practitioner puts strong performance brands at about 60-70 % pain-led, and brands built on
campaign shoots near 10 % (Stated, "creative for 2026" course video, 30 Sep 2026). Report the split
as a question for the brand, not a verdict.

**B4. Spreadsheet.** One `.xlsx` via the xlsx skill: sheet 1 every ad with the columns above as a
filterable table, library link per row; sheet 2 the gap tables and the matrix; sheet 3 the tagging
rules and the limits. The limit sentence goes on every sheet, not only the last.

**B5. Write it.** `analyse.md` with the caveats in each table. It ends with the **diagnosis**: one or
two sentences on why these ads, now, what it rests on, and what would change it. In a brand brain
it goes in `strategy/strategic-roadmap.md`. When the account belongs to the people who'll read it (an interview, a
pitch to the agency that runs it), findings are said as questions, with credit where it's due.

**B6 (optional). Baseline.** Before reading any data, ask the same question to `claude -p` with web
search only, in an empty folder, and save the answer verbatim. It's the comparison "AI without
data vs. the brain". Save the prompt as `audits/<YYYY-MM>/persona-gap-<YYYY-MM-DD>/baseline-prompt.txt`.

**B7 (optional). PDF showcase.** `showcase/build.py` (full, names the brand) and a public build (anonymised); see the golf test brand's showcase for the shape. Screenshot each section and look for collisions.

## Rules that held

- Honesty about the limit in every table, not only in a caveat at the end
- What an ad sells (category) is not the motive it speaks to (persona)
- **Shares only from the unweighted pull.** a job-application case, 19 Sep: "32 of 42 grandparents" came from a
  pull that searched for "barnebarn"; the unweighted pull on 29 Sep had 5 of 200
- Trustpilot asks for reviews after online purchases, so the online buyer is over-represented; say
  which way that pulls. 200 is the ceiling without login; never log in
- Rank is impressions, not sales, and campaigns with different budgets can't be compared on it
- Public version: no brand name, no staff names, no negative reviews. Send the full one to the brand
  before anything goes public
- Trustpilot fetch: `fetch('/review/<domain>?languages=all&sort=recency&page=N')`, read
  `__NEXT_DATA__` per page, 20 per page. Only from inside the browser: a direct curl gets 403, and
  bot checks are never worked around. The browser pane can't write to the clipboard or post to
  localhost, so data leaves it through what you read and write yourself: keep that compact
- Show the result as persona cards (share of reviews vs share of ads, the ads' awareness per
  persona) plus the awareness bar for all ads.
- **Check the month spread of the 200 before you quote any share.** The outdoor-retail test brand, 7 Oct: 174 of 200
  were from December and January, so every share was a Christmas share. Split season from the rest
  (here 78 % vs 54 % for delivery speed, 5 % vs 46 % for returns), say so on the page with the finding,
  and call the off-season group the small sample it is (26)
- **When the reviews are generic, count topics, not personas.** "Hurtig levering" carried most
  reviews, and one tag per review hid that 29 % also mention price. Count mentions per topic, same
  definitions on the review side and the ad side, multi-label. Give the ad side a stricter word list
  where the plain word means something else ("hurtige morgenmåltider" is not delivery)
- **Reading an ad's text is not seeing the ad.** Say "text, start date and format were read" in the
  document, and never claim what the ads show (people, products)
- **The library can show fewer cards than "ca. N resultater"** (30 cards for ca. 43, because versions
  are grouped). Say both
- **The baseline can be right about the framework and wrong about the facts.** The outdoor-retail test brand: the
  plain AI guessed price-led ads and recommended guides; 14 of 30 ads already were guides. Report what
  it got wrong with the number that shows it
- **The six-page showcase that held (the outdoor-retail test brand v2):** cover with one headline number; the hub
  (data in, brain, results out, solid = done here, dashed = needs their access); the pipeline from
  research to improved ads with a person approving three steps, guardrails for stock, calendar,
  budget and brand rules, and three levels of depth; findings (chart, three findings, baseline box,
  limits); recommendations; concept ads and the next step. Every word and page has to earn its place
- **Gotchas:** `claude -p --allowedTools "A,B" "<prompt>"` swallows the prompt (the flag is variadic):
  pass the prompt on stdin. Store large browser results by returning a padded string, so the tool saves
  it to a file instead of the chat

## Cost

One session handled a full run: data fetched once, each file written once, the compact files read
instead of the JSON. The audit subagent in A5 is the only extra agent. When Mode B has a long ad list (over about 100 ads), tag it in batches at once, one `gather` agent per batch against the tag rubric; the main session writes the diagnosis (`brain-system/system/agent-teams.md`).
