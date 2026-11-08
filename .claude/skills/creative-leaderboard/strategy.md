# Creative leaderboard: strategy

How to pick the process. Check in this order and take the first that fits.

## 1. Is naming settled for this brand?

Look for one of these:
- `running-notes/ad-naming.md` (the brand keeps its own convention, mapped to our fields), or
- a line in `running-notes/brand-rules.md` saying the brand uses the factory convention from a date, or
- recent ad names in the account that parse with `scripts/ad_name.py`

If none is there, run **`naming-setup`** first. A leaderboard on names that don't parse is a table of "x".

## 2. Is the question about the names themselves?

"Which ads are misnamed", "why is this ad missing from the board", "check our names", or more than a fifth of the week's spend sat on names that didn't parse last week: run **`name-audit`**.

## 3. Everything else

"Which angles won this week", "rank our ads", "hit rate by angle", the weekly routine, or account-playbook stage 7: run **`weekly-leaderboard`**.

## How it fits with the other skills

- **`weekly-creative-report`** is the client page. Run the leaderboard first in the same week so the report can lean on it. Don't copy the board into the report: the report picks the few things a CMO needs
- **`ad-account-analysis`** reads why an ad or the account behaves as it does (fatigue, placements, measurement). The leaderboard only ranks by tag. If the board shows something odd (one angle's CPA doubled), route it there
- **`angle-bank`** owns `angle-bank/angles.csv` and the gap matrix. The leaderboard feeds it the week's results per angle and fills `angle-bank/ad-tags.csv` from names
- **`ad-breakdown`** tags what an ad actually does. Its rows in `ad-tags.csv` (`tag_source` = `breakdown`) are never overwritten by this skill
- **`iterations`** makes the next versions of a winner. The leaderboard names which winners and which tag to keep
- **`season-report`** has its own hit rate study for a sale season. Use that one for Q4

## Two windows, two jobs

- **Last 7 days** ranks the week: what spent and what converted
- **Last 28 days** is where hit rate means something. A 7-day window holds too few new ads with enough spend. When the two disagree, say which window each claim rests on
