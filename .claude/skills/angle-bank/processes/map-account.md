# Process: map the account (the 90-day read)

What did the account actually scale on? Tag every ad that spent enough to show something, then count
whose spend the winners carry. Method: `brain-system/creative-strategy-context/angle-discovery.md`,
step 3.

## 1. Check the ground

- **Winner definition.** From `running-notes/success-definition.md` and `running-notes/brand-rules.md`
  (for example a CPA ceiling with a minimum spend, or a ROAS floor). Never invent one. If it is
  missing: ask, log the question in `running-notes/missing-context.md`, tag the ads anyway, and leave
  `is_winner` blank until there is an answer
- **Measurement.** If it hasn't been checked this month, run `ad-account-analysis` measurement-check
  first (`brain-system/.claude/skills/ad-account-analysis/processes/measurement-check.md`)
- **Spend floor.** The brand's own, written in the output. Without one, use one target CPA: an ad that
  spent less hasn't had the chance to prove anything (Inferred). Ads under the floor are counted, not tagged

## 2. Pull the last 90 days at ad level

Route order, read-only (`brain-system/system/data-access.md`):

1. **Meta's Ads MCP server** (`https://mcp.facebook.com/ads`) with the read permission only, never the
   permission to manage ads. A person connects it; the token stays in the brain's local config, never in a
   repo. The route is untested on a real brand: on the first run, log what the server actually exposes in
   `brain-system/.claude/skills/ad-account-analysis/feedback.md`
2. **An Ads Manager export** at ad level, saved as `source-pulls/ad-account-YYYY-MM-DD.csv` and never edited
3. **A person pastes it**

Per ad: ad id, ad name, launch date, spend, results (the brand's purchase event), CPA, ROAS, and a link
to the creative or its preview. Say the attribution setting on the page. Spend and results are Verified,
with the date of the pull.

## 3. Tag every ad above the floor

Write one row per ad in `angle-bank/ad-tags.csv` (columns in `../SKILL.md`). Take the best source
you have, in this order, and record it in `tag_source`:

| Source | When | `tag_source` | `label` |
|---|---|---|---|
| The ad name | The name follows `brain-system/system/ad-naming-convention.md`, or the brand's map in `running-notes/ad-naming.md` | `name` | Verified (the team named it) |
| A breakdown | The top spenders and every winner, when there is time: `ad-breakdown`, batch-winners process | `breakdown` | Inferred, with the breakdown file |
| A quick read | Everything else: read the copy, watch the first seconds, tag by the `persona-gap` B2 rules | `read` | Inferred |

For names, the leaderboard script parses and upserts the rows in one go:

```
python3 brain-system/.claude/skills/creative-leaderboard/scripts/leaderboard.py source-pulls/ad-account-YYYY-MM-DD.csv \
    --min-spend <floor> <the brand's winner bar> --angles angle-bank/angles.csv --write-tags angle-bank/ad-tags.csv
```

Check its "names that don't parse" list; those ads get a breakdown or a read.

Tag values come from the shared schema in `brain-system/creative-strategy-context/creative-vocabulary.md`.
An ad's angle must be an id from `angle-bank/angles.csv`. A message that isn't in the bank yet goes into
the bank first (`build-bank.md`), then gets its id; never write a made-up id. Unknown is `x`.

A tag from a read is a judgement. Read the tags through once, fix the obvious misses, and say how many
ads were tagged from each source.

## 4. Update the bank's status

For each angle, from the tags in the window: a winner -> `won`; ads running, no winner -> `live`;
tested with enough ads and none won -> propose `lost` to the strategist (one or two ads don't test an
angle). Set `last_tested`.

## 5. The core finding: what the account scaled on

Run the gap-matrix script (`gap-matrix.md`); its share tables answer this:

- **Share of winner spend by angle.** How many angles carry the winners, and what share the top 3 hold.
  The script flags 80 % or more. A practitioner's post puts most accounts at 1-3 core angles (Stated)
- **By persona and by awareness level.** Which personas and levels the winners speak to, and which none do
- **By format, voice and shape.** The account's proven format, voice and shape. `next-tests.md` puts new
  angles on these first

Write the finding in two or three sentences at the top of the gap matrix file, with the count it rests
on ("9 winners, 2 angles, 87 % of winner spend on A01 and A04"). Every share says its base and the limit:
spend share, not incrementality; tags as good as their source.
