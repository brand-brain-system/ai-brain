---
summary: "How to find net-new angles: mine the market, not the Ad Library; one-line angles tagged by persona and awareness; read 90 days of winners; map and rank empty cells; test on proven formats; close the loop by name."
---

# Angle discovery

**Source:** three practitioners' posts handed in by the team on 7 Nov 2026: one on finding new angles with the ad account, one on an agency's angle system, one on shared vocabulary. Authors not credited by the owner's choice.
**Users:** the whole team, all brands. The method behind the `angle-bank` skill; read by `account-playbook`, `harvest-ideas`, `evaluate-ideas` and the sprint plan.
**Status:** *Stated* (three practitioners, no data shown). Not yet tested on our accounts. The ranking of empty cells and the pointers to our skills are ours.

The words (angle, persona, awareness, enemy, UMP, UMS, concept) are defined in `creative-vocabulary.md`.

## Why net-new angles

Copying a competitor's winning ad gives you more ads. It rarely gives you new buyers, because it says what the market has already heard. Swiping is quick work anyone on the team can do. Finding an angle the account has never run is the strategist's job, and per the sources it is where the next level of spend comes from.

One source says new angles found this way grew accounts 2-3x within a few months (*Stated*, no data shown). Treat it as a reason to try, not a forecast.

This fits what the factory already says: volume only pays when it carries different strategy, new personas, angles and awareness levels (`creative-strategy-fundamentals.md`, "Strategic volume, not volume"), and 20-30% of the monthly effort goes to new concepts (`creative-volume.md`).

## What counts as an angle

An angle is the reason to buy you lead with. It targets one problem, one desire or one belief.

**The one-line test.** If it takes a paragraph to explain, it isn't an angle yet. Cut it until one sentence carries it.

| Not an angle yet | Why | An angle |
|---|---|---|
| "Recovery" | A topic | "Sore legs the morning after a long run, gone by the next run" |
| "Sustainable, gentle and great value" | Three reasons at once | "The refill costs less than the bottle you throw away" |
| "Busy mums" | A persona | "Dinner on the table before the kids melt down" |
| "UGC testimonial" | A format | Any of the above, said by a customer |

Each new enemy is a new angle even with the same product and proof (`yapper-ads.md`: new villain + same product = new angle).

## Product-aware angles run cold

Awareness is what the ad assumes the viewer knows. The funnel stage is who Meta delivered it to. They are separate axes (`creative-vocabulary.md`, Funnel stage), and mixing them costs spend: mechanism, lab-result and us-versus-them ads get filed as "BOF", moved into a retargeting campaign where Meta can't take them cold, and then made less often because "BOF ads don't scale".

In a broad campaign Meta reads the ad to pick its viewers, so a product-aware angle can be the account's biggest cold ad. A practitioner's post (Nov 2026, *Stated*) gives the pattern:
- A humidifier brand tested three product-aware claims: cleanest, first doctor-designed, first stainless steel. The one the team expected least from, stainless steel, became the top spender, on cold traffic
- The reason sat in the forums: buyers didn't know a non-plastic humidifier existed, and threads said no high-end full-metal one was on the market
- New images on the same angle raised spend about 80%; a video version ("someone finally made a humidifier out of stainless steel") raised it about 4.4x more at the same ROAS
- The same post says product-aware ads have scaled to $300k a day and unaware ads to $10k a day for some of its brands. One agency's accounts, no data shown

What to take from it:
- **Look for absence statements** when you mine forums and reviews: "there's no X that…", "why doesn't anyone make…", "I've looked everywhere for…". A product that answers one is an S1 claim for that buyer even in a crowded market (`creative-vocabulary.md`, sophistication)
- **A mechanism the category leaders don't have** is how a smaller brand stands out. The big brands already own the broad claims
- **Put the product-aware column of the gap matrix on cold traffic** like any other cell. Where it runs is decided by delivery data, not by the awareness code. Whether this holds for our brands is an open test (`.claude/skills/angle-bank/feedback.md`)

## Step 1: Mine the market, not the Ad Library

The Ad Library shows what rivals say. It never shows what works (`system/evidence-and-labels.md`), and it can only hand you angles the market has already heard. Use it to see which claims are crowded (the sophistication read), not to find angles.

Find angles where buyers talk. Ranked by what each source shows best for this job:

| Source | Speaks for | Shows best | Watch out for |
|---|---|---|---|
| Post-purchase surveys | Buyers | Why they bought, what they tried before, the trigger | Only people who bought |
| Support tickets | Buyers and near-buyers | The doubts before the sale and what went wrong after | Skews to problems |
| The brand's own 3-4 star reviews | Buyers | Honest praise with a "but": the angle and its objection in one | Over-represent online buyers and recent orders |
| Competitors' 1-2 star reviews | Their buyers | The pain the rival left behind: a ready enemy | Angry outliers |
| Reddit and forums | Buyers and non-buyers | The problem in raw words, the fixes people argue about | Loud few; keyword pulls show existence, not share |
| TikTok and Instagram comments | Viewers | Reactions, objections, insider phrases | Skews young; reacts to the post, not the product |
| The Ad Library | Rivals | What the market has already heard | No performance data, ever |

**Verbatim beats category words.** Copy what customers say, word for word. "I leave my running shoes by the door and still don't go" gives you a scene, a persona and a hook. "Low motivation" gives you nothing to film.

How to pull and sort: `customer-review-mining-method.md` for the method (golden nuggets, trigger events, metaphors, insider phrases), the `research-map` skill to rank what many people said, and `persona-gap` Mode A when the personas need building or rebuilding. This doc does not repeat them.

## Step 2: Write the angle bank

Every angle goes into `angle-bank/angles.csv` before anyone writes a script, tagged by persona and awareness level. The row holds:
- the angle in one line, and the enemy it blames
- the UMP and UMS it rests on, if there is one
- the verbatim quote it came from, its source, and how many different people said it (`evidence_people`)
- the persona or personas (`P1+P3`) and the awareness level or levels (`PA+SA`)
- the status: `idea`, `briefed`, `live`, `won`, `lost` or `retired`

An angle with no quote behind it stays an idea with `evidence_people` 0 and is flagged. It can still be tested, but nobody should mistake it for customer language.

The same angle often works at more than one awareness level, with a different opening (`awareness-script-ladder.md`, worked example).

## Step 3: Read the last 90 days of the account

1. **Get the data.** The account read is read-only. Route order and permissions: `system/data-access.md`; the audit itself: `ad-account-analysis`.
2. **Find the winners.** Use the brand's own winner definition (`running-notes/success-definition.md`, `running-notes/brand-rules.md`). Never invent one.
3. **Tag each winner by angle and persona.** From the ad names when the naming convention is in place, from `ad-breakdown`, or from a read of the ad. `angle-bank/ad-tags.csv` records which (`tag_source`). Spend and results from the account are *Verified*; tags from a read are *Inferred*.
4. **Count.** How many winners, and how many distinct angles and personas among them. Per the sources, most accounts scaled on only 1-3 core angles (*Stated*). Write the count down; it is the baseline for everything after.
5. **Compare with the research.** Set the winners' angles, personas and awareness levels beside the angle bank. What customers say that the ads never said is the gap.

## Step 4: Map the gaps

Two grids:
- **Angles x awareness.** Angles down the side, `UN` `PA` `SA` `PR` `MA` across the top. Built by `angle-bank` as `angle-bank/gap-matrix-YYYY-MM-DD.md` and `.html`.
- **Personas x awareness.** On the own account, built by `angle-bank` from `ad-tags.csv` with spend; `persona-gap` Mode B draws it for public or competitor ads.

Each cell is one of: **won** (an ad met the brand's winner bar), **live** (running, or too new to judge), **lost** (ran and missed; say how many ads), or **never tried**.

| Angle | UN | PA | SA | PR | MA |
|---|---|---|---|---|---|
| A01 Sore legs gone by the next run | never tried | won | live | never tried | never tried |
| A02 Cheaper than the gel you throw away | never tried | never tried | never tried | lost (2 ads) | never tried |
| A03 Training for the first race | never tried | never tried | never tried | never tried | never tried |

Per the sources, most audited accounts have one or two cells live (*Stated*). Every empty cell is a message the buyers have never heard.

## Step 5: Rank the empty cells

Emptiness alone is not a reason. Some cells are empty for a good reason. Rank on evidence, then check the reason.

**Rank by:**
1. **Customer evidence.** How many different people said it (`evidence_people`), in their own words, across more than one source.
2. **Persona size.** How much evidence backs the persona in `personas/personas-profile.md`. A cell for a persona one review mentions is a long shot.
3. **Fit with the roadmap.** Does it serve a priority in `strategy/strategic-roadmap.md`, or trip a road not taken?

**Then check why it is empty:**
- **The claim can't be made.** The Danish rules, Meta's policy or the brand's compliance file forbids it (`ad-policy-check`).
- **The product can't deliver it.** Customers wish for it; the product doesn't do it.
- **The level barely exists here.** Few people are unaware of some problems; some products have no repeat buyers to be most aware.
- **It was tried.** Status `lost`. But one or two ads don't test an angle: a new concept needs 10-20 ads before a winner is likely (*Stated*, `creative-volume.md`). Under-tested is not the same as lost.
- **It eats a winner.** It would compete with a live winner for the same people.

Hand the top five cells, each with its reason and its quote, to `evaluate-ideas` and the sprint plan.

## Step 6: Test on the lowest-risk path

Change one big thing at a time, so you can tell what worked.

**Rung 1: a new angle on a proven format.** Use the format, voice and shape the account already wins with, and change the angle. If the account's winners are creator-to-camera symptom call outs, the new angle goes in as a creator-to-camera symptom call out. If it fails, the angle failed, not the format.

**Rung 2: a proven angle into new formats.** Once an angle wins, carry it across. A winning UGC angle becomes a static. A static's winning headline becomes a podcast clip or a song ad. The angle is already known to work, so the new format is the only test.

Don't put a new angle on a new format on the first test. This matches the order in `iterations.md` (angle before format) and the register's rule for a failing concept: change the angle, then the offer, then the persona, the format last (`idea-bank/concepts.md`). How many ads a test needs: `creative-volume.md`. The test setup itself: `teep-creative-test-setup.md` or `meta-full-funnel-cbo-playbook.md`.

## Step 7: Close the loop

- **Name every ad** by concept, angle, persona, awareness and format, so results can be read by angle without a manual tag pass. The one home for the format: `system/ad-naming-convention.md`. Renaming live ads is the team's job in Ads Manager.
- **Rank every week.** The `creative-leaderboard` skill reads the names and ranks angles, personas, formats and shapes by results, so the next batch starts from what won, not what someone liked.
- **Update the bank.** Set each angle's `status` and `last_tested` in `angles.csv`. Redraw the gap matrix after each test round.
- **Break down winners and losers.** `ad-breakdown` asks for your own read first, then shows what you missed. Its tag block goes straight into `ad-tags.csv`.

Swiping adds ads. The loop makes each new ad a better bet.

## What this doc does not cover

Writing the script (`scriptwriting`, `winning-script-patterns.md`, `awareness-script-ladder.md`), the account audit (`ad-account-analysis`), building personas (`persona-gap`) and the start-to-finish order for a new account (`account-playbook`).
