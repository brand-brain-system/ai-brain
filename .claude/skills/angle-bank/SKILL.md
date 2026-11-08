---
name: angle-bank
description: Find the net-new angles that open up the next level of spend (angle-bank, angle bank, new angles, find new winning angles, gap matrix, which angles are we missing, vinkler, angle x awareness, what did the account scale on). Mines what customers say word for word, turns it into a bank of one-line angles tagged by persona and awareness level, tags the last 90 days of the ad account by angle, persona and awareness, shows which angles carry the winner spend, and builds a gap matrix (angles and personas x awareness) that ranks the empty cells by evidence. Ends in five test proposals and idea-bank entries for the strategist to pick. Use when an account has stopped scaling, when someone asks what the account scaled on, which angles or personas are missing, or for new angles. Read-only on the ad account.
triggers:
  - angle bank
  - new angles
  - find new winning angles
  - gap matrix
  - which angles are we missing
  - what did the account scale on
  - angle x awareness
  - vinkler
---

# Angle bank: the angles the buyers have never heard

Most accounts scale on one to three angles. Swiping a rival's winner gives you more ads; it rarely
gives you a new reason to buy. This skill finds those reasons in what customers say, checks which
ones the account has already tried, and points at the empty cells: messages the buyers have never
heard, ranked by how many people back them.

The method and its reasoning are in `brain-system/creative-strategy-context/angle-discovery.md`.
What an angle, persona, awareness level, enemy, UMP and UMS are is defined once in
`brain-system/creative-strategy-context/creative-vocabulary.md`. Read both before the first run.
This file is the order of work; it doesn't repeat them.

## The flow

| Step | Process | Writes (in the brain) |
|---|---|---|
| 1. Mine the market | `processes/mine-market.md` | quotes in `source-pulls/` and `research-map/evidence.jsonl` |
| 2. Build the bank | `processes/build-bank.md` | `angle-bank/angles.csv` |
| 3. Map the account | `processes/map-account.md` | `angle-bank/ad-tags.csv`, the share of winner spend |
| 4. Read the gaps | `processes/gap-matrix.md` | `angle-bank/gap-matrix-YYYY-MM-DD.md` and `.html`, the top 5 gaps |
| 5. Plan the tests | `processes/next-tests.md` | `idea-bank/entries/`, then `idea-bank/concepts.md` when picked |

`strategy.md` says which steps to run when. A first run on a new account runs all five in order. Steps 1 and 3 don't need each other: dispatch the step 1 sources at once, one `gather` agent each, and map the account in the main session while they read (`brain-system/system/agent-teams.md`).

## Where the data is stored

Everything this skill writes stays in the brand's brain and is committed to the brain's private
GitHub repo. Nothing goes to the factory. The two files:

- `angle-bank/angles.csv`: `angle_id,angle,persona_ids,awareness,enemy,ump,ums,quote,quote_source,evidence_people,status,first_seen,last_tested,notes`
- `angle-bank/ad-tags.csv`: `ad_id,ad_name,launch_date,spend,results,cpa,roas,is_winner,concept_id,angle_id,persona_id,awareness,format,voice,shape,hook_family,enemy,mechanism,proof,close,product_at,tag_source,label`

Several values in one field are joined by `+` (`PA+SA`, `P1+P2`). Unknown is `x`. The tag values
are the shared schema that `ad-breakdown` writes and `creative-leaderboard` parses; their list is in
`creative-vocabulary.md`. Quotes are personal data: short, with a source id, and hashed authors as in
`research-map`.

The script:

```
python3 brain-system/.claude/skills/angle-bank/scripts/gap_matrix.py --min-spend <floor>
```

It reads both files from `angle-bank/` and writes the dated `.md` and `.html` next to them. `--help`
lists the flags.

## Account access is read-only

The ad account is read through the route in `brain-system/system/data-access.md`: Meta's Ads MCP
with read permission only (never the permission to manage ads), then an ad-level export, then a
person pasting it. This skill never pauses, renames, launches, edits or pays for anything in the
account. Renaming ads to the naming convention is the team's job in Ads Manager.

## Stops for a person

1. **No winner definition, no winners.** The brand's own definition comes from
   `running-notes/success-definition.md` and `running-notes/brand-rules.md`. If it is missing, ask,
   log the question in `running-notes/missing-context.md`, and don't mark any ad a winner until there
   is an answer
2. **Account access.** A person connects the MCP or hands over the export. A token lives in the
   brain's local config, never in a repo
3. **The bank before the matrix.** Show the angle list and every merge to the strategist before the
   counts are used (`build-bank.md`)
4. **The pick.** The five test proposals and their idea-bank entries go to the strategist. Nothing is
   briefed, scripted or made until they pick (`next-tests.md`)

Nothing is sent, posted, published or paid for by this skill.

## Labels and limits

Every number and quote carries its label per `brain-system/system/evidence-and-labels.md`. Every table
says its limit: the matrix is only as good as the tags, `evidence_people` counts different people in
the pulls (it is not a market share), and an empty cell means never tried in this window. Tags read
from an ad name are as good as the naming; tags from a quick read are Inferred.

## Files

| File | What it holds |
|---|---|
| `SKILL.md` | The flow (this file) |
| `strategy.md` | Which process to run when |
| `processes/` | One file per step, `INDEX.md` lists them |
| `scripts/gap_matrix.py` | Builds the gap matrix. Python 3 standard library, no install |
| `feedback.md` | What we've observed. A log, not a rulebook |
