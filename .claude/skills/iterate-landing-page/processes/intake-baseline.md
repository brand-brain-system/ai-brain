# Intake and lock the baseline

1. Resolve the exact source. Prefer editable local source over a live URL, and record both when they exist.
2. Create the run folder and `baseline/`, `working/`, `copy/`, `assets/`, `shots/`, and `qa/` directories.
3. Copy the source into `baseline/` without changing it. If the source is a repository page, record the entry file, related components, styles, assets, and build command; do not copy unrelated application code into the run.
4. Capture full-page desktop and phone screenshots with the shared `lp-screenshot.mjs` utility.
5. Inventory sections, copy, CTAs and destinations, forms, safe interactions, offer, proof, claims, images, fonts, design tokens, analytics hooks visible in source, and responsive behavior.
6. Run baseline QA where the input can be opened locally. Record failures as pre-existing. A baseline defect is not permission to expand the iteration.
7. Write `baseline/source.md` with the source location, captured date, editable-source status, page format, screenshot paths, QA path, and known limitations.

When the source is only a URL, save only material needed for the authorized iteration. Do not bypass access controls, copy customer data, or submit forms. State that the result is a recreation when the original source was unavailable.

