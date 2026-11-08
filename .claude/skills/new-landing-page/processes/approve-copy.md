# Process: approve the copy (step 4, between the copy and the build)

Same gate as the statics: nothing is built until the person running the skill has seen the copy, as a plain table in the chat reply, and answered. The gates check truth and voice; this step is the human's call on taste, the offer and the message.

## What it produces

**A plain table in the chat reply, nothing else.** One row per section, in page order:

| # | Section | What this section does on the reference page | Proposed copy | Customer words behind it |

Build it with `python3 <skill>/scripts/lp-copy.py table <run>`, which writes `<run>/copy/approval-table.md` and prints it. Each "Proposed copy" cell holds every line in that section joined with " / ". The middle column is the section's job from the template: it describes what the reference does there and never quotes the reference's words. The last column lists the customer phrases each section was built from, with their source, so the reviewer can see the page is in the buyers' words.

Above the table, three short lines and no more:
1. The template, the reference page, the angle, and the ad it is matched to if one was named.
2. Anything that dropped or was adapted, and why ("no sourced rival prices, so the comparison table is out").
3. How to reply: `approved`, or edits like `S03 headline: "old line" -> "new line"`, or `cut S07`.

Then stop.

## Steps

1. **Post the table.** One message. Do not build, screenshot or publish anything.
2. **Wait.** If the reply says the copy misses the angle (or the named ad), that is a promise failure: go back to `write-page-copy.md` step 2, not to a polish pass, and post the table again.
3. **Apply the reply exactly.** Each edit replaces that field in `page.json`. `cut S07` removes the section (a required section cannot be cut without breaking the template: say so and offer the card's adaptation). Then `lp-copy.py collect` and `lp-copy.py check` again, and the mechanical voice lint on changed lines. An edit that fails the check goes back to the reviewer with the reason; it is never silently changed.
4. **Record it.** `<run>/copy/approval.md`: the reply verbatim, the date, who approved, what changed. Then continue to `build-draft.md`. A copy-only run ends here.

## Rules

- The reviewer's edits are the brand speaking. Apply them as written, check them for claims, flag a failure; do not rewrite them for voice without asking.
- After approval, the words on the page are the approved words. Any later copy change comes from a board note or goes back through this table.
