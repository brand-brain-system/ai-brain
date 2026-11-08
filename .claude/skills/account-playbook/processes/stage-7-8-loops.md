# Stages 7 and 8: the weekly loop, the monthly loop and the day-90 review

The loops never close. They keep the next batch starting from what actually won, not from what
someone liked. Each week and month gets one row on the status page.

## Stage 7: the weekly loop (from week 3, every week)

### Entry criteria

- The first round from Stage 6 has been live for at least a week
- An account route works (Stage 0). Without one, see "When access is partial" in
  `stage-0-access.md`

### Calls, in this order

1. **`creative-leaderboard`**, process `weekly-leaderboard`: the week's board, ranked by the brand's own winner definition,
   for the team (internal)
2. **`weekly-creative-report`**: the shareable page for the client. It goes out only after a yes
3. **`iterations` Phase A** on the winners: which ads to iterate on. The picks go to Phase B, and
   their new ads go through Stage 6 steps 6-9 (checks, naming, hand-off)
4. **`ad-breakdown`** on the week's best new ad, and `loser-breakdown` on the week's biggest
   miss. Their tags go into `angle-bank/ad-tags.csv`
5. **Angle statuses:** update `angle-bank/angles.csv` from the board through `angle-bank` (`live`,
   `won`, `lost`)
6. **`harvest-ideas`, then `evaluate-ideas`**: the week's idea hunt and the ranked pile the next
   sprint plan draws from

When the board shows the round is spent, start the next round at Stage 5, step 2 (pick the gaps,
size the round). The roadmap is re-run only when Stage 8 says so.

### Outputs

`audits/leaderboard/<YYYY-Www>.md` and `.html`, `audits/<YYYY-MM>/weekly-creative-report-<YYYY-WW>.html`,
iteration briefs, breakdown files, updated `angle-bank/angles.csv` and `ad-tags.csv`, new
`idea-bank/` entries and an evaluation, and the week's row on the status page.

### Stops

- The client report is sent only after a yes
- Renames found on the board (ads off the convention) are a hand-off: the team renames in Ads
  Manager
- New ads from iterations stop before launch, as in Stage 6

### Exit check (per week)

- [ ] The week's row on the status page is filled: board, report sent or not, iterations picked,
      breakdowns, angle status changes
- [ ] The next batch is chosen from the board

## Stage 8: the monthly loop

### Calls

1. **`angle-bank`**, processes `map-account` and `gap-matrix` again, on the month's ads. Compare
   the new top 5 gaps with last month's
2. **`persona-gap`**: Mode B on the month's new ads. Mode A again when
   `personas/personas-profile.md` is past its `refresh_by` or the research map has grown a group
   the cards don't cover
3. **`ad-account-analysis`**, process `measurement-check`: once a month, as that process says
4. **`refresh-context`**: the docs past their `refresh_by`. If it re-runs the roadmap, the
   strategist approves it before the next sprint plan uses it
5. **`growth-plan`**, when the Meta loop is steady: two rounds through Stage 7, or when the
   strategist asks what to do beyond Meta

### Outputs

A new `angle-bank/gap-matrix-<YYYY-MM-DD>.md` and `.html`, refreshed persona files, a new
measurement check, refreshed docs, `strategy/growth-plan.md` when it runs, and the month's row on
the status page.

### Stops

- The strategist approves any change to the roadmap or the top 5 gaps

## The day-90 review

On day 90 after access, check the bet this playbook is built on: did the gaps we picked become
winners?

1. For each of the top 5 gaps from Stage 4: was it launched, and did any ad on it meet the
   brand's winner definition? Fill the "Top 5 gaps" table on the status page
2. Write the time from access to the first launch on a new angle
3. Log both numbers, without brand details, in `.claude/skills/angle-bank/feedback.md` and in this
   skill's `feedback.md` (the open test there)
4. Tell the strategist what the result means for the next 90 days, in three lines. Then save the
   brain
