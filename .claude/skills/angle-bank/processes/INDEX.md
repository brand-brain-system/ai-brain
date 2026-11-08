# Angle bank: process index

- **mine-market**: gather what customers say, word for word, from reviews, Reddit, comments, support tickets and surveys. Mostly routing to `research-map` and `persona-gap` Mode A. Output: quotes with ids and sources
- **build-bank**: turn the quotes into one-line angles, each tagged by persona, awareness, enemy, UMP/UMS, best quote and how many people back it. Dedupe, merge, keep the status. Output: `angle-bank/angles.csv`
- **map-account**: read the last 90 days of the ad account at ad level, apply the brand's winner definition, tag every ad above the spend floor. Output: `angle-bank/ad-tags.csv` and the share of winner spend by angle, persona and awareness
- **gap-matrix**: run `scripts/gap_matrix.py`, then read it: which cells are won, live, lost and never tried, and which empty cells matter most. Output: the dated matrix and the top 5 gaps as test proposals
- **next-tests**: turn the top gaps into tests (new angle on a proven format first, then proven angles in new formats), written as idea-bank entries. Stops for the strategist to pick

Run order and cadence: `../strategy.md`.
