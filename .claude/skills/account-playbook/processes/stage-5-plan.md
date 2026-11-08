# Stage 5: strategy and test plan (days 10-14)

Turn the top gaps into a round the account can afford to test, and get a yes before anything is
made or spent.

## Entry criteria

- Stage 4 is done: the top 5 gaps are agreed
- The account read is under 30 days old. If not, re-run Stage 1 first

## Inputs

The gap matrix and top 5 gaps, the account audit (spend band, monthly ad target, structure note),
"what the account scaled on", `personas/personas-profile.md`, `strategy/strategic-roadmap.md` if it
exists, and the measurement caveat if there is one.

## Calls

1. **The roadmap.** If `strategy/strategic-roadmap.md` is missing, past its `refresh_by`, or older
   than the gap matrix, re-run the Phase 2 prompts in `brain-system/prompts/strategic-roadmap/` in
   the order of `brain-system/prompts/onboarding-runner.md`, "Phase 2". Otherwise read it as it is.
   The roadmap's own gate applies: the strategist approves, adjusts or rejects it
2. **Pick the gaps to test.** `angle-bank`, process `next-tests`, turns the top gaps into test
   proposals written as idea-bank entries, and stops for the strategist to pick. Then run
   `evaluate-ideas` so the picks are ranked against the roadmap beside the rest of the pile. Why
   new angles go on proven formats first is in
   `brain-system/creative-strategy-context/angle-discovery.md`
3. **Size and map the round** with the sprint-plan prompt,
   `brain-system/prompts/ideas-and-briefs/sprint-plan.md`. It sizes from spend and cadence, sets
   the split and the variations, and offers the T-E-E-P test setup
   (`brain-system/creative-strategy-context/teep-creative-test-setup.md`) as an option next to the
   brand's current setup, not as a rule. The monthly ad target from Stage 1 is a cross-check on
   its size, not an override
4. **Show the prices.** Before the stop, list every cost the round will create, as numbers: the
   test budget and its split, creator fees, and paid generation per
   `brain-system/creative-strategy-context/production.md`. A cost nobody knows yet is written as
   unknown, never guessed

## Outputs

`strategy/strategic-roadmap.md` (new or confirmed), `idea-bank/` entries and its evaluation file,
and `sprints/<YYYY-MM-DD>-<slug>/sprint-plan.md`. On the status page: which gaps were picked, the
sprint size, the test setup, and the approval with its date.

## Stops

**STOP: the strategist approves the plan and the budget split.** Ask through the form. Show the
plan, the gaps it tests, the setup, the split and every price first. Nothing is made, booked or
paid for before the yes. Claude never sets a budget in the ad account; the team does.

## Exit check

- [ ] The roadmap is approved, or the strategist chose to run without one (written down)
- [ ] The sprint plan names the gaps it tests, the size, the variations, the test setup and the
      budget split
- [ ] Every price was shown, and the approval is on the status page with its date
