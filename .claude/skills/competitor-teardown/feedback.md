# Feedback log

What we've observed in teardowns: which public signals told us the most, which stages were worth the
time, where the script broke. A log, not a rulebook: new lessons land here with a date, and once
confirmed on a second brand they move into `SKILL.md` (factory rule 6), leaving one line here saying
where they went. Rival-specific findings go in the brain's `competitors/<rival>/`, never here.

## Tested

- **31 Oct 2026, `teardown.py` on a large public US Shopify store** (scratch only, nothing saved):
  `catalog` read two pages (356 products) with added-by-month, sale share and the best-selling order;
  `stack` over 3 months found the store platform, Google Tag Manager and a live Clarity script but not
  the Meta pixel or the email tool, which that store loads through the tag manager or an app embed.
  So a missing pixel in `stack` means little; check the Ad Library for real ads. `hero` found the
  title and headline change; `ads` builds Denmark-set links. Not yet run on a Danish store or a full
  24-month window

## Open tests

- **31 Oct 2026, is going inside worth 30-60 days?** On the first teardown, note which plays came only
  from stage 3 (their emails and cart reminders). If none, shorten it to the welcome series

## Log
