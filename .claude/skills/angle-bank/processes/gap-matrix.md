# Process: read the gap matrix

Every empty cell is a message the buyers have never heard. Not every empty cell is worth filling.
This step draws the matrix and picks the five that are. Method and the reasons a cell can be empty:
`brain-system/creative-strategy-context/angle-discovery.md`, steps 4 and 5.

## 1. Run the script

```
python3 brain-system/.claude/skills/angle-bank/scripts/gap_matrix.py --min-spend <floor>
```

It reads `angle-bank/angles.csv` and `angle-bank/ad-tags.csv` and writes
`angle-bank/gap-matrix-YYYY-MM-DD.md` and `.html` (open the `.html` with the team). Read its warnings
first: an angle id in the tags that isn't in the bank, ads with no angle, unknown awareness codes. Fix
the files and run again rather than reading around them.

## 2. Read the cells

Two grids, angles x awareness and personas x awareness (`UN` `PA` `SA` `PR` `MA`). On our own account the
persona grid comes from `ad-tags.csv` with spend; `persona-gap` Mode B's matrix stays the version for
public or competitor ads. Each cell is:

| State | Means |
|---|---|
| won | At least one winner in the cell |
| live | Ads, no winner yet, at least one launched in the last 14 days (too early to call) |
| lost | Ads, no winner, all older. Say how many ads: one or two is under-tested, not lost |
| never tried | No ads in the window |
| gap (highlighted) | Never tried, at a level the angle fits, with 5 or more different people behind it |

The thresholds are flags (`--young-days`, `--high-evidence`); change them for the brand and say so.
Then the share table: if the top 3 angles hold 80 % or more of winner spend, the account depends on a
few messages, and the gaps are where the next level of spend comes from.

## 3. Rank the empty cells

The script ranks empty cells by `evidence_people` only. Add the rest by hand, in this order:

1. **Evidence.** Different people behind the angle, from more than one source
2. **Persona size.** How much evidence backs the persona (`personas/personas-profile.md`, the persona-gap
   A3 ranking)
3. **Roadmap fit.** Does it serve a priority in `strategy/` (`strategy/strategic-roadmap.md`), or trip a
   road not taken?
4. **Empty for a reason?** The claim can't be made (`running-notes/brand-rules.md`, `ad-policy-check`), the
   product can't deliver it, the awareness level barely exists for this product, it was tried and lost
   with enough ads, or it would compete with a live winner for the same people. A cell that is empty for
   a reason drops out, with the reason written down

An angle that already won at another level is a strong candidate: the reason to buy is proven, only the
opening changes (`brain-system/creative-strategy-context/awareness-script-ladder.md`).

## 4. Write the top 5 as test proposals

Add a `## Top 5 gaps` section to the dated `.md` file. One block per gap:

- **Cell:** angle id and line, persona, awareness level
- **Why this one:** `evidence_people`, the persona's weight, the roadmap priority it serves
- **The quote:** the best verbatim line, with its source id
- **Enemy and mechanism:** from the bank row, or "none yet"
- **Proposed test:** which rung (new angle on the proven format, or proven angle in a new format) and the
  format, voice and shape from the share tables
- **What counts as a win:** the brand's own winner definition, and how many ads the test needs
  (`brain-system/creative-strategy-context/creative-volume.md`)
- **Risk:** what could make it fail or trip a rule
- **Label:** each line Verified, Inferred or Stated

Then hand over to `next-tests.md`.
