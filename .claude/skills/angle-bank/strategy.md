# Angle bank: which process when

## Before picking

Load the brand's winner definition (`running-notes/success-definition.md`, `running-notes/brand-rules.md`),
the personas (`personas/personas-profile.md`) and the roadmap (`strategy/strategic-roadmap.md`). Check
which routes this brain has in `tool-map.md`. A missing piece is named in
`running-notes/missing-context.md`, not guessed.

## When to run what

| Situation | Run | Why |
|---|---|---|
| First run on an account, or the bank is empty | All five, in order: mine-market, build-bank, map-account, gap-matrix, next-tests | The matrix needs both sides: the customer's reasons and the account's history |
| Monthly | map-account, then gap-matrix | New ads launched and old ones won or died. The bank stays; the cells move |
| New research landed (a review export, a Reddit pull, a survey, a research-map rebuild) | build-bank, then gap-matrix | New quotes can add an angle or raise an angle's `evidence_people`, which changes the ranking |
| The strategist asks for the next tests, and the matrix is less than a month old | next-tests | No need to read the account again |
| A single question: "what did the account scale on?" | map-account only | The share of winner spend answers it |
| Competitor ads, no spend data | Not this skill: `persona-gap` Mode B | The matrix needs spend and a winner definition |

## Tiebreakers

1. **No winner definition?** map-account still tags the ads, but the share of winner spend and every
   won or lost cell wait for the answer. Say so in the output
2. **No account access?** Build the bank and stop. A matrix from the public Ad Library has no winners;
   use `persona-gap` Mode B for the ad side and label it a proxy
3. **The measurement hasn't been checked this month, or Meta and the store disagree?** Run
   `ad-account-analysis` measurement-check before map-account. Winners from a broken pixel are not winners
4. **Fewer than about ten ads above the floor?** Run it, but read the matrix as a list, not a pattern.
   Say the count on the page
