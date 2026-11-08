# Creative leaderboard

```
Name:        creative-leaderboard
Kind:        routine
Owner:       the strategist on this brand
Schedule:    weekly, Monday 07:30 (after competitor-ad-watch, before the week's planning)
Skill:       /creative-leaderboard (weekly-leaderboard process)
Reads:       the "Ad account" role in tool-map.md (Meta Ads MCP read-only, or the newest
             source-pulls/ad-account-*.csv); running-notes/success-definition.md;
             running-notes/ad-naming.md if the brand keeps its own naming
Writes:      audits/leaderboard/<YYYY-Www>.md and .html; angle-bank/ad-tags.csv (name-parsed rows)
Report:      max 5 lines in chat: what won by angle and format, hit rate, ads whose names don't parse
Ends when:   n/a (routine)
Needs:       read access to the ad account and a written winner definition; skips and says so without them
Triggers:    not armed (template)
Started:     -
```

## Prompt

Run `/creative-leaderboard` for the last full week (Monday to Sunday) and the last 28 days. Read the
winner definition from the brain; never invent one. List ads whose names don't parse. End with the
three things the next batch should start from, each routed to `iterations` or `angle-bank`. Then,
if the brand's weekly report is due, offer `/weekly-creative-report`. Never send it without a yes.

## Why it earns its keep

The next batch starts from what actually won, by angle, persona and format, not from what someone
liked. It reads the account and writes only in the brain.
