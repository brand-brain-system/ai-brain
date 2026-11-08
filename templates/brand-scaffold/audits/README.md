# Audits

This README explains the folder. It is not one of the folder's docs, so leave it out of any list or index of them.

The cadence layer: how the account and the market look each week, month and quarter. The newest audit is the account's present tense.

## What lives here

- `[YYYY-MM]/`: the month's audits: the performance report, the hook audit, the organic TikTok audit and TikTok mining, the weekly performance snapshots and the biweekly iterations report.
- `[YYYY-MM]/external/`: the month's market reads: the creative landscape and the top-impressions report.
- `[YYYY-Q]/`: the quarter's 90-day audits (creative strategy, diversity, performance), the customer review audit, the whitespace analysis, and `gaps-opportunities-inspo.md`.
- `[YYYY-Q]/external/`: the quarter's external 90-day audits and the single-competitor ad analyses.
- `breakdowns/`: one ad breakdown per file, `YYYY-MM-DD-<ad-slug>.md` (`ad-breakdown` skill).
- `leaderboard/`: the weekly creative leaderboard, `YYYY-Www.md` and `.html` (`creative-leaderboard` skill).
- `INDEX.md`: the generated map, one line per audit, with the newest marked. `/refresh-context` keeps it in step with the folder.

The prompts that write these docs are in `brain-system/prompts/`: `audits-weekly/`, `audits-biweekly/`, `audits-monthly/`, `audits-monthly-external/`, `audits-quarterly/`, `audits-quarterly-external/` and `market-synthesis/`. How to read an ad account is in `brain-system/creative-strategy-context/ad-account-analysis.md`.

A new brain starts with this folder empty. The build runs every audit once as the baseline, and `/refresh-context` re-runs each one when it is due.
