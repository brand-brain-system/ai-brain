# Season heads-up

```
Name:        season-heads-up
Kind:        routine
Owner:       the strategist on this brand
Schedule:    weekly, Monday 07:30
Skill:       prompt below
Reads:       sub-context-docs/marketing-calendar-and-campaigns.md; sprints/<sprint>/briefs/
Writes:      running-notes/current-work.md (a line when a season's prep starts)
Report:      only when a date is 6 weeks or less away and no brief exists yet; otherwise silent
Ends when:   n/a (routine)
Needs:       a filled-in marketing calendar
Triggers:    not armed (template)
Started:     -
```

## Prompt

Check `marketing-calendar.md` for dates in the next 6 weeks: the brand's own launches and sales, plus
the Danish retail calendar (Black Week and Cyber Monday, jul, mellemdagssalg, Valentine's Day,
fastelavn, Mother's and Father's Day, Singles' Day, payday weekends if the brand leans on them).

For each one that has no brief in `sprints/<sprint>/briefs/` yet, report:

- The date, and how many weeks are left
- What the offer brief needs before `offer-ads` can run: real prices, before-prices and their
  period, dates, codes, free-shipping terms, stock limits
- Whether creators or shoots need booking now to make the date

## Why it earns its keep

Seasonal work is usually late because nobody asked for the prices in time. This asks six weeks out,
with the exact list of inputs the offer ads need.
