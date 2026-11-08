# Process: build the angle bank

Turn what customers said into angles, each tagged before anyone writes a script.

## What counts as an angle

One angle is **one line, one reason to buy**: a problem it solves, a desire it meets, or a belief it
proves or breaks. The full definition is in `brain-system/creative-strategy-context/creative-vocabulary.md`.

- **The one-line test.** If it takes a paragraph to explain, it isn't an angle yet. Park it in `notes`
  on a row with status `idea`, or as a lead in `hypotheses/`, until it can be said in one line
- **One reason, not two.** A line with "and" in it is usually two angles. Split it
- **An argument, not a topic.** "Sleeps through the night without waking at 3 a.m." is an angle;
  "sleep" is a topic
- **Not a format.** "A podcast clip" is how it looks. The angle is what it says

## Fill one row per angle in `angle-bank/angles.csv`

| Column | How to fill it |
|---|---|
| `angle_id` | `A01`, `A02`... in order. Never reused, even after a merge or a retirement |
| `angle` | The one line, in the customer's framing |
| `persona_ids` | `P1`... in the order of `personas/personas-profile.md`. Several with `+`. `x` if no persona fits yet |
| `awareness` | `UN`, `PA`, `SA`, `PR`, `MA`: the levels this angle can speak to. Several with `+` |
| `enemy` | The specific thing it blames (what they use now, the old fix, the wrong belief), or `none`. Specific beats vague |
| `ump` / `ums` | The root cause of the problem and how the product fixes that exact cause, when the angle has one. Both must trace to the offer brief (`strategy/offer-brief.md`) or the product facts in `brand-lens.md`. Blank if not, never invented |
| `quote` | The best verbatim line behind it, under 15 words |
| `quote_source` | The quote's id in `research-map/evidence.jsonl` (`q012`), or the file and id in `source-pulls/` |
| `evidence_people` | How many **different people** said this, from the research map's count. Not quotes: one person who says it three times is one |
| `status` | See the lifecycle below |
| `first_seen` / `last_tested` | Dates, `YYYY-MM-DD` |
| `notes` | Merges, splits, why it was retired, the label of anything not Verified |

An angle the team suggests without a customer quote is allowed, with `evidence_people` 0 and
"team idea, no customer quote yet" in `notes`. It ranks last in the gap matrix until a quote turns up.

## Start from what the account already says

Before mining for new angles, write down the ones the live and past ads already use, so map-account
can tag them. They come from the ad copy and the concept register (`idea-bank/concepts.md`). Then add
the new ones from the research map's groups: one group usually gives one angle, a belief group often
gives the enemy, a desire group the promise.

## Dedupe and merge

Two rows are one angle when they give **the same reason to buy to the same person**, even in
different words. Then:

1. Keep the lower id. Write "merged A09 into A04, YYYY-MM-DD" in the kept row's `notes`, and delete the other row
2. Recount `evidence_people` from the research map (different people across both groups). Never add the
   two numbers: the same person may be behind both
3. Keep the stronger quote
4. Change `angle_id` in `angle-bank/ad-tags.csv` from the old id to the kept one, so no ad points at a
   deleted row (the script reports any that do)

Same reason, different persona: keep one row and list both personas. Same words, different reason
(price as "cheap" vs price as "worth it"): two angles.

## The status lifecycle

`idea` -> `briefed` -> `live` -> `won` or `lost` -> `retired`

| Status | Set when | Set by |
|---|---|---|
| `idea` | The angle is in the bank, no ad yet | build-bank |
| `briefed` | The strategist picked a test for it and a brief exists | next-tests |
| `live` | An ad with this angle is running in the 90-day window and no winner yet | map-account |
| `won` | At least one ad with this angle meets the brand's winner definition in the window | map-account |
| `lost` | It was tested with enough ads (`idea-bank/concepts.md` has the rule of thumb) and none won | map-account, confirmed by a person |
| `retired` | A person stops it: compliance, the product changed, it fatigued for good. Reason and date in `notes` | a person |

Every change gets a date in `last_tested` or `notes`. A lost angle can come back at another awareness
level or for another persona; that is a new test, not a new row.

## Stop: show the bank

Show the strategist the list (id, line, personas, awareness, people) and every merge before the gap
matrix uses it. Grouping is a judgement, same as the research map's groups.

## Audit

The quote in each row must exist word for word in its source. The `persona-gap` A5 audit agent, who
didn't write the bank, checks a sample (all rows on a first build). A quote that can't be found is
replaced or the row's `evidence_people` drops to what can be traced.
