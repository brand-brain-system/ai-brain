# Process: build template cards (growing the library)

Turn new swipe pages into templates the skill can run. Build-time only; no brand work.

A template is not one page. It is the section contract that several real pages share. The current seven come from 14 pages across 8 accounts (`swipe-file/README.md`, "The master templates"), trimmed on 2026-10-01 from the original 35-page, 10-template library.

## Adding pages to the swipe file

1. **Find the pages worth having.** For a brand, pull its top 40 ad groups by 90-day spend through the Parker MCP, group them by landing URL, and take the pages carrying the most spend, read against the account's own CPA and ROAS. Prefer a page type the library lacks.
2. **Capture each page** at phone width: `node scripts/lp-screenshot.mjs <url> <swipe>/screenshots/<brand>-<n>.png --height 3400`, then convert to JPEG. Look at the capture; retry if a pop-up or a country picker covers it.
3. **Write the breakdown** in `<swipe>/brands/<brand>.md`, the same fields as the existing files: URL and date, page type, above the fold, the section-by-section flow (each section's job, paraphrased, never its copy), proof stack, offer mechanics, urgency devices, how the page matches the ad, why it works, and an outline. Spend tables go under a heading marked private.
4. **Add a card to the swipe page** (`<swipe>/index.html`, the `P` list) with its template key, then rebuild and republish the picker artifact (`processes/pick-template.md`, "Keeping the picker current").

## Adding or changing a template

5. **Decide: an existing template, or a new one.** If the page's sections match an existing contract, add it to that template's `refs`. A new template needs a structure the seven do not cover, seen on a page with real spend behind it.
6. **Write the contract** in `templates/INDEX.json`: `id`, `name`, `slug`, `use_when`, `teep` (the buying phase it serves), `requires`, `nice_to_have`, `urgency_device`, `story` (why the structure works, in plain words, no client numbers), `refs`, and `sections`. Each section: `id` (s01, s02 ... in page order), `type` (a component the builder has; see the list at the top of `scripts/lp-build-page.py`), `required`, `job` (what the section does for the reader, one line), `guide` (what to write: word budgets, item counts, what must be sourced). Then `adaptation` (the legal swaps when a brand lacks something) and `watch_outs` (what went wrong on real pages).
7. **A section the builder cannot draw** needs a new component in `scripts/lp-build-page.py` (a method on `Page`, its CSS, a blank shape in `scripts/lp-start-run.py`, and its name in `scripts/lp-validate-templates.py`). Build a test page with placeholder content and screenshot it before the template is used on a brand.
8. **Validate and write the cards.**
   ```bash
   python3 <skill>/scripts/lp-validate-templates.py --write-cards
   ```
   Fix `INDEX.json`, never the card or the validator.

## What never to do

- Write a contract from memory of a page. Open the capture and the breakdown.
- Copy a page's words, names or numbers into a contract. It describes structure; the skill writes the words.
- Put spend, CPA or ROAS in the library. Those stay in the swipe file's private tables; the validator rejects them.
