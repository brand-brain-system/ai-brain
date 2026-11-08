# Process: name audit

Find the ads whose names don't parse, say why for each, and suggest the fixed name. Read-only: the list goes to the team, who fix names by hand if they want to.

## Inputs

- The newest ad-level pull under `source-pulls/` (or a new one, route in `weekly-leaderboard.md` step 1). Use the 28-day pull when there is one
- The naming: the convention, or `running-notes/ad-naming.md`
- The adoption date from `running-notes/brand-rules.md` or `running-notes/ad-naming.md`

## 1. Run the audit

```bash
python3 brain-system/.claude/skills/creative-leaderboard/scripts/leaderboard.py source-pulls/<pull>.csv --audit
```

Add `--naming-map running-notes/ad-naming.md` when the brand keeps its own names. The script prints how many names don't parse, their share of spend, and one line per ad with the reason. It writes nothing.

## 2. Sort the list

Split the ads into three groups:

1. **Launched before the adoption date.** Expected. They get their tags in `angle-bank/ad-tags.csv`, not a new name. Count them; don't list them one by one
2. **Launched after it, with a fixable slip.** A space, a missing `x`, an awareness code in lower case that the parser didn't know, `_` inside a value, an ID that isn't in `idea-bank/concepts.md` or `angle-bank/angles.csv`. Suggest the fixed name with `ad_name.py --build`
3. **Launched after it, not following the convention at all.** List them with their spend. Ask who launches these ads; the convention may not have reached that person

For ads with a valid name, also check that every concept and angle ID exists in its file. A name that parses can still point at nothing.

## 3. Write it down

Save `audits/leaderboard/name-audit-YYYY-MM-DD.md` with: the pull it read, the counts and spend share per group, the table for groups 2 and 3 (`ad name | ad ID | spend | why | suggested name`), and the IDs that don't exist yet.

## 4. Stop and hand over

Show the strategist the counts, the share of spend affected, and the file. The fix is the team's, by hand in Ads Manager, and only if they decide a rename is worth it. Claude never renames. Missing IDs go to `angle-bank` (angles) or the concept register (concepts), proposed, not added from here.

## Done when

- Every unparsed name with spend is in one of the three groups
- The file is saved and the strategist has the numbers
