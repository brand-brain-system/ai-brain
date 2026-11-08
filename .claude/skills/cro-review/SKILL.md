---
name: cro-review
description: Review an existing landing page for message match, clarity, hierarchy, proof, objection handling, offer comprehension, friction and mobile conversion. Use when the user asks for a CRO review, landing-page critique, teardown or prioritized recommendations. Review only unless implementation is explicitly requested.
---

# CRO Review

Review the page as a specific argument for a specific visitor—not against a generic checklist. Separate things that are broken or contradicted from craft judgment and from ideas that require a test.

## Local setup (read first)

Ported 2026-10-06 from Alex Cooper's Adcrate build (Parker course; credit kept). Paths, tools and Danish-language checks follow the "Local setup" table in `../new-landing-page/SKILL.md`: brand truth in `Brand/`, customer words in `source-pulls/`, `python -X utf8` instead of `python3`, the scripts find Chrome or Edge on Windows. Runs go to `<brand brain>/sprints/<sprint>/landing-pages/<YYYY-MM-DD>-<brand>-<slug>/`.

## Evidence to load

1. Open the exact live URL or HTML and inspect desktop and phone views. Preserve the URL in the review.
2. When available, load the page brief, selected template, approved copy and source ad. If an ad is named, verify promise, offer, audience and visual continuity.
3. Load the brand brain or supplied brand context: approved claims, offer, customer language, objections, positioning and assets.
4. Read [references/review-rubric.md](references/review-rubric.md).

If conversion data, heatmaps or experiments are unavailable, say so once. Do not turn general CRO patterns into claims about what caused performance.

## Review order

1. **Truth and function:** false or unsupported proof, broken actions, wrong offer, unreadable mobile layout, missing disclosure.
2. **Message match:** whether the first screen continues the promise and level of awareness that brought the visitor there.
3. **Comprehension:** whether a new visitor can identify the product, buyer, value, mechanism, offer and next step without inference.
4. **Persuasion:** proof, objections, differentiation, risk reversal and the order in which the argument earns the ask.
5. **Presentation:** hierarchy, scannability, visual credibility and whether the design helps the argument.

## Output

Lead with a one-sentence verdict and the three changes most likely to matter. Then provide a compact table:

| Priority | Section | Observation | Why it matters | Recommended change | Basis |
|---|---|---|---|---|---|

Use these basis labels:

- `Verified fault`: broken, inconsistent, unsupported or contradicted by the supplied evidence.
- `Craft judgment`: a reasoned recommendation based on the page, audience and argument.
- `Test hypothesis`: plausible but requires a controlled test or performance data.

End with:

- **Keep:** the elements that should survive a revision.
- **Test next:** at most three controlled tests, each changing one meaningful variable.
- **Missing evidence:** only information that would materially change the review.

Quote page copy only as much as needed to identify the section. Draft replacement copy only for the highest-priority issues unless the user asks for a rewrite.

## Boundaries

- Do not grade visual polish as conversion performance.
- Do not recommend fake urgency, inflated counts, generic badges or invented testimonials.
- Do not silently edit, publish or deploy the page. If implementation is requested, use the appropriate landing-page build skill and preserve the approved review as the change brief.

