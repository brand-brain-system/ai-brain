# Process: weekly leaderboard

Rank the week's ads by their tags, write what won, and say what the next batch starts from.

## Inputs

- The winner bar and the tested floor, from `running-notes/success-definition.md` and `running-notes/brand-rules.md` (SKILL.md step 2). Ask if missing; never invent it
- The naming: the factory convention (`brain-system/system/ad-naming-convention.md`) or the brand's map in `running-notes/ad-naming.md`
- `angle-bank/angles.csv` if it exists, for the angle one-liners
- Last week's board, `audits/leaderboard/<last week>.md`, for continuity

## 1. Pull the two windows at ad level

Use the ad account route in the brain's `tool-map.md`, best first (`brain-system/system/data-access.md`):

1. **Meta Ads MCP, read-only.** Pull ad-level results for the last 7 days and for the last 28 days, each ending yesterday. Ask for, per ad: ad ID, ad name, spend, purchases (or the brand's north-star event), purchase value, the window's start and end dates, and the ad's created time. Save each pull as a CSV with those columns in snake_case: `source-pulls/ad-account-YYYY-MM-DD-7d.csv` and `-28d.csv`, dated the day you pulled. This route is untested on a real brand: on the first run, log in `brain-system/.claude/skills/ad-account-analysis/feedback.md` which tools the server exposed and what was missing
2. **An Ads Manager export,** if the MCP route isn't connected. Ask the team for two ad-level exports (last 7 days, last 28 days) with Ad name, Ad ID, Amount spent, Purchases, Purchases conversion value, Reporting starts and Reporting ends. Danish column names work too. Save them under the same names
3. **A person pastes it,** as the last resort. Save the paste as a CSV the same way

Never edit a saved pull. If the north star is not purchases, map its column with `--colmap '{"results": "<their column>"}'` and say so in the takeaways.

## 2. Run the script

From the brain root:

```bash
python3 brain-system/.claude/skills/creative-leaderboard/scripts/leaderboard.py \
  source-pulls/ad-account-YYYY-MM-DD-7d.csv --long source-pulls/ad-account-YYYY-MM-DD-28d.csv \
  --min-spend <floor> --winner-cpa-max <bar> --winner-min-spend <spend a winner needs> \
  --angles angle-bank/angles.csv --write-tags angle-bank/ad-tags.csv
```

- Use `--winner-roas-min` instead of (or with) `--winner-cpa-max` when the brand's bar is ROAS. Every bar given must hold
- Add `--naming-map running-notes/ad-naming.md` when the brand keeps its own names
- `--write-tags` fills `angle-bank/ad-tags.csv` from the names (tag_source `name`, label Verified) with the 28-day numbers. It never touches rows from `ad-breakdown`
- Fix every WARNING and NOTE the script prints before reading on. A missing results column means the CPA column is empty, not zero

## 3. Read it

Open `audits/leaderboard/YYYY-Www.md`. Read these, in this order:

1. **How much of the spend parsed.** Below about 80% of spend, the board shows only part of the account. Say so first, and run `name-audit` after this
2. **Hit rate on the 28-day window.** Hit rate = ads that met the brand's winner bar / ads launched in the window that reached the tested floor. Write it as `k/n (x%)`. Compare it with last week's board and with the 5% planning figure in `brain-system/creative-strategy-context/creative-volume.md`. Under 10 new tested ads, say "too few new ads to read a hit rate" and stop there (at a 5% hit rate a winner needs 10-20 tries: `idea-bank/concepts.md`)
3. **Each dimension: angle, persona, awareness, format, voice, shape, then concept.** Read the share of spend and CPA or ROAS against the bar together. A value with one tested ad is an ad, not a pattern
4. **The top ads.** Which tags do the top spenders share? Which winner sits on a tag nothing else uses?
5. **Last week's plan.** Did the batch we said we'd make get made and launched? What did it do?

Hold the reading rules from `brain-system/creative-strategy-context/ad-account-analysis.md`: spend and the north star together, never ROAS on small spend, and the breakdown effect before calling a misallocation.

## 4. Write the takeaways

Write them to a short file next to the board, `audits/leaderboard/YYYY-Www-takeaways.md`, then run the script once more with `--takeaways audits/leaderboard/YYYY-Www-takeaways.md` so they land in the `.md` and the `.html`.

Plain words, short lines, a label on every claim (`brain-system/system/evidence-and-labels.md`):

- **The verdict.** One line: what won this week and on what number
- **By angle, persona, awareness, format, voice and shape.** One line each for the tags that matter this week: what won, its spend share, its CPA or ROAS against the bar, and n. Skip a dimension with nothing to say, and say you skipped it
- **The hit rate.** `k/n (x%)` on 28 days, against last week
- **What lost or stalled.** Only with enough spend to call it
- **The next batch starts from.** Two to four moves, each tied to a row of the board:
  - a winner to iterate, keeping the tag that won and changing one thing: route to `iterations`
  - a winning angle in a format it hasn't run in, or a new angle on a format that wins: route to `angle-bank` (its test proposals) and the briefs
  - an angle to mark `won`, `lost` or `live` in `angle-bank/angles.csv`, with `last_tested`: propose it to `angle-bank`; don't edit its file from here
- **Data limits.** The windows, the source file, the parsed share of spend, and anything the pull lacked

## 5. Stop and hand over

The board is internal. Nothing is sent, posted or changed in the account. Tell the strategist what won, the hit rate with its n, the parsed share, and the suggested batch, and link both files. If `weekly-creative-report` runs this week, tell it where the board is.

## Done when

- `audits/leaderboard/YYYY-Www.md` and `.html` exist with takeaways in both
- `angle-bank/ad-tags.csv` was updated, or you said why not
- The next batch is named and routed, each move tied to a number on the board
