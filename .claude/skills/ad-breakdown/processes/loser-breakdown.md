# Process: loser breakdown

The same lens on an ad that failed. A feedback loop needs both sides: winners show what to repeat, losers show what to
stop, and only the pair shows which part made the difference.

Our own ads only. We can't know that a competitor ad lost.

## 1. Check it really lost

- Read the numbers against the brand's bar (`running-notes/success-definition.md`). No bar: ask, never invent one
- Did it get a fair run? Low spend or few days is "not enough data", not a loss. Say how much spend and how many days,
  and mark the verdict Data-limited if it is thin
- Is the loss the creative? A tracking problem, a broken landing page, a sold-out product or a budget cut can kill a
  good ad. If the numbers look odd, run `ad-account-analysis` `measurement-check` first. Name what you ruled out

## 2. The strategist's read

The four questions in `../SKILL.md`, step 2, with question 3 as "Why do you think it lost?"

## 3. Break it down

Run `video-breakdown.md` or `static-breakdown.md` in full, with the tag block. Two changes:

- In the closing part, "Why it worked, in five lines" becomes **Why it lost, in five lines**, each tied to a part and,
  where you can, to a number (a hook rate under the account's benchmark points to the hook; a good hook rate with a low
  hold rate points to the body; a good CTR with poor conversion points past the ad, to the page or the offer)
- Mark which parts held up. A loser often has a good hook or a good angle in the wrong shape; that part is worth
  keeping

## 4. Compare with a winner

Pick one winner from the account with the same angle or the same format (the same angle first: it isolates the
execution). Use its breakdown from `audits/breakdowns/` if one exists; if not, run a light pass on it. Then one table:

| Field | Loser | Winner | Difference that matters? |
|---|---|---|---|

Rows: every tag block field, plus the hook (three layers), product timing, the lead, the peak intensity, the CTA, and
the hook rate, hold rate, CTR and CPA. Mark the one to three differences most likely to explain the gap, Inferred, with
the reason. No winner on the same angle or format: say so, and compare with the account's top spender, noting that
the comparison is weaker.

## 5. Write it down

- The file: `audits/breakdowns/YYYY-MM-DD-<ad-slug>.md`, marked "Loser" in the header
- The row in `angle-bank/ad-tags.csv` with `is_winner` = `no` (rules in `batch-winners.md`, step 7)
- Next steps: `angle-bank` to mark the angle `lost` only if the angle, not the execution, failed; `iterations` if one
  part held and is worth a new version; otherwise note what not to brief again
