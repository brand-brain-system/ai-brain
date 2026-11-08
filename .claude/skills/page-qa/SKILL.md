---
name: page-qa
description: Functionally check one or more landing-page HTML files or review URLs at desktop and phone widths for broken assets, placeholder or mismatched links, form wiring, overflow, console errors, failed requests and safe interactions. Use for landing-page QA, pre-handoff checks or batch page checks. It does not submit forms, follow CTAs or judge conversion strategy.
---

# Page QA

Run deterministic browser checks before a landing page is handed off. This skill verifies function; it does not replace visual comparison, CRO judgment, legal review or a real form submission test.

## Local setup

Ported 2026-10-06 from Alex Cooper's Adcrate build (Parker course; credit kept). On Windows the checker finds Chrome or Edge itself (patched 2026-10-06); `CHROME=<path>` overrides. Reports for a brand go in its run folder under `<brand brain>/sprints/<sprint>/landing-pages/`.

## Checker

Use the canonical checker in the sibling landing-page system:

`../new-landing-page/scripts/lp-qa.mjs`

For one page:

`node ../new-landing-page/scripts/lp-qa.mjs <file-or-url> --out <qa.json> [--cta-url <expected-url>]`

For several pages, run one independent report per target. Do not merge failures into a single untraceable log.

## Before running

- Identify whether the target is meant to be a self-contained HTML deliverable or a hosted page. The checker flags external assets in a self-contained file; on a hosted page, interpret that result in context.
- Ask for the canonical CTA URL only when CTA consistency is part of the check. Do not guess it.
- Use a temporary output location for an informal audit. For a landing-page run, write to its `qa/` folder as `qa-v<N>.json` or `final.json`.

## What it checks

- Desktop at 1440px and phone at 390px.
- Horizontal overflow.
- Broken images and missing internal anchors.
- Empty, `#` or JavaScript links.
- CTA URLs against `--cta-url` when supplied.
- Non-embedded assets in a self-contained deliverable.
- Forms with no submit control or no detectable wiring.
- FAQ/details toggles and safe local controls.
- Console errors, uncaught exceptions and failed network requests.
- Visible placeholders and missing image alt text in the report.

The checker never follows a CTA or submits a form. A live form submission always requires explicit authority and appropriate test data.

## Interpret and report

1. A nonzero exit or `result: fail` blocks handoff.
2. Fix failures in the source, data or builder, then rerun. Do not simply edit the JSON report.
3. Review warnings manually. Record why any remaining warning is safe; warnings are not silently ignored.
4. Open desktop and phone screenshots for visual defects the checker cannot infer: hierarchy, clipping that does not create overflow, awkward wrapping, overlays and reference fidelity.

Return:

- overall pass/fail;
- report path for every target;
- failures grouped by page and viewport;
- warnings requiring human judgment;
- what was fixed and the result of the clean rerun;
- what still needs a manual or authorized live test.

## Boundaries

- Do not call a page conversion-ready because it passed functional QA.
- Do not publish, attach a domain, add tracking or submit live data as part of QA.
- Do not suppress a failure merely because the page appears correct in one screenshot.
