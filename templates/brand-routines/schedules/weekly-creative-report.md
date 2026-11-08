# Weekly creative report

```
Name:        weekly-creative-report
Kind:        routine
Owner:       the strategist on this brand; shared with the account lead
Schedule:    weekly, Monday 08:00
Skill:       prompt below
Reads:       the "Ad account" role in tool-map.md, read-only (the data routes, an Ads Manager export
             dropped in a folder, or Ads Manager in the browser); idea-bank/concepts.md;
             strategy/offer-brief.md; hypotheses/; brain-system/creative-strategy-context/creative-volume.md (the volume target)
Writes:      audits/weekly/<YYYY-MM-DD>.md (create audits/ when the first report is written);
             proposed status changes for idea-bank/concepts.md (a human applies them)
Report:      the summary as a team-chat draft; posting needs approval
Ends when:   n/a (routine)
Needs:       read access to the ad account. Without it, this routine can't run: don't arm it
Triggers:    not armed (template)
Started:     -
```

## Prompt

Compare the last 7 days with the 7 before. Read ads by their concept ID (`idea-bank/concepts.md`, and the
`C07_` prefix in ad-set and ad names). Ads without an ID are listed once at the end as a naming gap.

**How to read the numbers.** Meta credits a sale to the last ad clicked, but shows people a sequence
of ads. So one ad's ROAS is the least reliable number in the account: an ad that opens the sequence
can look weak and be doing the most work. Trust runs upward: ad < ad set (concept) < campaign.
Use the metrics in this order:

1. **Share of spend.** Where Meta chooses to put the money over time is the best single signal of
   what works, better than the ad's own ROAS
2. **ROAS or CPA** on 7-day click, and on incremental attribution where the account has it
   (Columns → Compare attribution settings). Existing customers excluded where the setup allows.
   Say which attribution every number uses
3. **CPC and CTR:** early warning, not a verdict. An ad far above the account's usual CPC rarely
   comes good
4. **Hook rate (3 s) and hold rate (15 s)** for video: to find what to fix, not to judge the ad

Then write:

1. **Concepts:** per concept, spend, the KPI (the brand's main KPI is written in `CLAUDE.md`),
   number of live ads, and the change on last week. Winners and losers are named at this level, with
   spend next to every number so a winner on 200 kr. isn't read as a winner on 20,000
2. **Inside the concepts:** don't recommend turning off an ad because its own ROAS is low while its
   ad set hits the target: it may be the opener. Flag such ads as "low attributed, keep". In an ad
   set missing its target, name the weakest ads freely
3. **Fatigue:** on cold (prospecting) ads, frequency above 2 is a flag; also frequency climbing
   while CTR or hook rate falls. Name the concept, not only the ad, and whether it's the ad wearing
   out or the persona's audience being too small for the spend
4. **Concentration (portfolio risk):** share of spend on the top 3 ads and the top 3 concepts, and
   the change. When a few ads carry most of the spend, the account falls with them; say how many
   ads hold at least 5 % of spend
5. **Volume:** new ads launched this week against the monthly target in `brain-system/creative-strategy-context/creative-volume.md`,
   and the mix: winners remade / iterations / new concepts. Hit rate over the last 4 weeks (share of
   new ads that reached meaningful spend: define the threshold in `CLAUDE.md`)
6. **Hypotheses:** for each open hypothesis the week touched, one line. Evidence goes to
   `validations/` only after a human agrees. Then one line on `strategy/strategic-roadmap.md`: does the
   week support it, weaken it, or say nothing? When the "what would change it" condition is met,
   propose a rewrite; the human decides. When a verdict touches a persona, propose the change to its
   card in `personas/personas-profile.md`: the field it confirms or breaks, and its "Testing now" line
7. **Next week:** up to three concrete creative moves, each tied to a number above:
   - a winning concept: more ads in a **new** ad set (`C07-2`), not added to the running one
   - a fatigued winner: new hooks on the same body first, then the same message in a new format
   - a failing concept: change the angle first, then the offer, then the persona; format last
   - low hook rate: new hooks; good hook, low hold: fix the bridge
   Plus proposed status changes for `idea-bank/concepts.md`
8. **Before calling an ad a loser, and feeding the result back:** apply the four-part loser test and the
   feed-back table in `brain-system/creative-strategy-context/ad-account-analysis.md` ("Before Calling an Ad a
   Loser"). Say which of the four held for every ad named a loser, and list each proposed doc update with
   its date and the test behind it; a human applies them.

Read-only. Never change budgets, pause ads or publish anything. Every number comes from the pull;
nothing is estimated. Label anything read through business context (season, a sale, a stock-out) as
Inferred.

The reading rules above (spend first, concept level, keep low-attributed openers, frequency 2, the
order of changes) come from the "creative for 2026" Meta course video shared 30 Sep 2026: Stated,
one practitioner's method. When this brand's own data contradicts one, note it in
`running-notes/feedback.md` and follow the data.

## Why it earns its keep

The Monday "what worked, what didn't" answer, written the same way every week, so trends are
visible across reports, not just within one. Reading it by concept makes each week a lesson about
arguments and people, not a verdict on single ads.
