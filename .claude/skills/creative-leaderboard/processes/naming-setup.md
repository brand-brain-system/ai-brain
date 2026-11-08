# Process: naming setup

The first run on an account. Decide how this brand's ad names carry the creative tags, and leave the team a list of suggested names. Claude never renames anything in the ad account.

## Inputs

- `brain-system/system/ad-naming-convention.md` (the convention, the field map format, the adoption rules)
- The intake answer on ad naming, if `set-up-brain` asked it (`running-notes/brand-rules.md`)
- `idea-bank/concepts.md`, `angle-bank/angles.csv`, `personas/personas-profile.md`: the IDs a name can point to
- An ad-level pull of the last 90 days (the route in `weekly-leaderboard.md` step 1), saved under `source-pulls/`

## 1. See how the account names ads now

Take the ad names from the pull, sorted by spend. Read the top 30 and a random 20 of the rest. Write down, in a few lines:

- Is there a pattern at all? Which separator, how many parts, which part is a date, a concept, a product, a creator, a format?
- How many names follow it, by count and by share of spend
- Whether the account already uses our convention (run `--audit` on the pull and see what parses)

## 2. Decide with the strategist

Show what you found and offer two options in one popup form:

1. **Adopt the factory convention for new ads** (the default when there is no pattern, or a loose one)
2. **Keep the brand's convention and map it** (the default when most spend sits on names that follow a clear pattern)

Either way, old ads keep their names (step 4).

## 3a. If they adopt the convention

Write one line in `running-notes/brand-rules.md`: "Ad names follow `brain-system/system/ad-naming-convention.md` from <date> (decided by <who>)." Tell the people who launch ads, in the hand-over, what the format is and where the IDs come from.

## 3b. If they keep their own

Write `running-notes/ad-naming.md` in the field map format from the convention doc: separator, date format, one row per position, value maps from their words to ours. Then test it:

```bash
python3 brain-system/.claude/skills/creative-leaderboard/scripts/ad_name.py "<a real name>" --naming-map running-notes/ad-naming.md
python3 brain-system/.claude/skills/creative-leaderboard/scripts/leaderboard.py source-pulls/<pull>.csv --naming-map running-notes/ad-naming.md --audit
```

Fix the map until the names that follow their pattern parse. A field their names don't carry stays `x`; say which tags will have to come from `ad-breakdown`.

## 4. Old ads: tags in a file, names in a suggestion list

- Old ads keep their names. Their tags go into `angle-bank/ad-tags.csv`: from `ad-breakdown` for the winners (tag_source `breakdown`), or from a read of the ad (tag_source `read`, label Inferred). The angle-bank process that tags the last 90 days does this; don't do it twice
- For the live ads the team may want to rename, write `audits/leaderboard/suggested-names-YYYY-MM-DD.csv` with these columns: `ad_id,current_name,suggested_name,spend_90d,basis`. Build each suggested name with `ad_name.py --build field=value ...`, from tags that are already in `ad-tags.csv`. Use `x` for any field nobody has tagged, and say in `basis` where each tag came from. Never guess an angle or persona from the old name alone

## 5. STOP: the rename is a human hand-off

Show the strategist the decision, the map (if any), the audit result and the suggested-names file. Then stop.

- Renaming live ads is the team's call, made and done by a person in Ads Manager. Say so in plain words
- Claude never renames, duplicates, pauses or edits ads, and the access is read-only anyway
- If the team renames, ask them to tell you when, so the next pull's names can be checked with `name-audit`

## Done when

- The decision is written (`brand-rules.md` line, or `running-notes/ad-naming.md` tested on real names)
- The suggested-names CSV exists, or the strategist said it isn't wanted
- The strategist knows the next weekly leaderboard will read the names this way
