---
name: extract-page-template
description: Turn a real landing-page URL, HTML file or screenshots into a reusable section contract with component types, section jobs, writing constraints, adaptation rules and watch-outs. Use when the user wants to reverse-engineer, templatize or add a landing page to a swipe library. Extract structure, not copyrighted copy or unverified performance claims.
---

# Extract Page Template

Convert a specific page into a reusable structural contract. Preserve the mechanism that makes the page coherent; remove the source brand’s words, identity and unsupported assumptions.

## Local setup (read first)

Ported 2026-10-06 from Alex Cooper's Adcrate build (Parker course; credit kept). Paths, tools and Danish-language checks follow the "Local setup" table in `../new-landing-page/SKILL.md`: brand truth in `Brand/`, customer words in `source-pulls/`, `python -X utf8` instead of `python3`, the scripts find Chrome or Edge on Windows. Runs go to `<brand brain>/sprints/<sprint>/landing-pages/<YYYY-MM-DD>-<brand>-<slug>/`.

## Shared library

Read these sibling resources before extracting:

- `../new-landing-page/processes/build-template-cards.md`
- `../new-landing-page/templates/INDEX.json`
- the existing template cards in `../new-landing-page/templates/`
- [references/template-output.md](references/template-output.md)

## Capture the page

1. Record the exact URL or file and access date.
2. Inspect desktop and phone. For a live page, use the shared screenshot script and visually check the captures:

   `node ../new-landing-page/scripts/lp-screenshot.mjs <url> <output> --height 3400`

3. Account for sticky bars, modals, quizzes, accordions, menus and state changes. A single screenshot may hide the actual sequence.
4. If access is blocked or content is incomplete, mark the extraction partial. Never fill unseen sections from category memory.

## Extract in two passes

### Pass 1: page anatomy

Describe the source page itself:

- page type and likely awareness stage;
- first-screen promise, proof and action;
- section order, one section per block;
- each section’s job in the argument;
- proof stack, offer mechanics, urgency and interaction;
- desktop/mobile behavior;
- what appears distinctive, weak or dependent on the source brand.

Paraphrase. Do not copy headlines, testimonial text, names or proprietary prose into the contract.

### Pass 2: reusable contract

For every section define:

- stable section ID;
- supported component type;
- required or optional;
- one-sentence job;
- writing guide with useful word, item and proof limits;
- inputs required to run it honestly;
- legal adaptation when that input is unavailable.

Then compare the structure with every existing template:

- If it matches one, record it as another reference and state any meaningful variant.
- If it does not, label the output `candidate template`.
- Do not promote a candidate into the shared library from one attractive page alone. Require evidence that the structure is intentional: another independent example, meaningful spend/performance evidence, or explicit human approval of the exception.

## Delivery

Unless the user explicitly asks to edit the library, deliver:

1. Source-page breakdown.
2. Match decision: existing template or candidate.
3. Template contract in the schema from `references/template-output.md`.
4. Inputs, adaptations and watch-outs.
5. Missing evidence needed before promotion.

When library editing is requested and supported, update `templates/INDEX.json`, run `lp-validate-templates.py --write-cards`, and inspect the generated card. Edit the JSON, never a generated template card. Keep spend, CPA and ROAS in private source notes, not in the reusable contract.
