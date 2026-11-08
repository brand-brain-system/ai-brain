---
name: iterate-landing-page
description: Create a new iterated version of an existing landing page from the user's direction. Use the supplied page as the structural and visual baseline, preserve everything the direction does not change, research and approve any materially new copy or claims, build a separate version, verify it against the baseline on desktop and mobile, and deliver the page with QA and a concise change receipt. Use when the user asks to revise, improve, adapt, test, reskin, or make another version of an existing landing page. Do not open the landing-page template picker or choose a swipe-file template; use new-landing-page for a net-new page.
---

# Iterate Landing Page

Owner: Alex Cooper. Built 2026-10-01 as the existing-page counterpart to `new-landing-page`.

## Local setup (read first)

Ported 2026-10-06 from Alex Cooper's Adcrate build (Parker course; credit kept). Paths, tools and Danish-language checks follow the "Local setup" table in `../new-landing-page/SKILL.md`: brand truth in `Brand/`, customer words in `source-pulls/`, `python -X utf8` instead of `python3`, the scripts find Chrome or Edge on Windows. Runs go to `<brand brain>/sprints/<sprint>/landing-pages/<YYYY-MM-DD>-<brand>-<slug>/`.

## Goal

Take one existing landing page and the user's direction, then produce one new version of that page. The existing page is the baseline. Preserve its underlying visual system, section logic, responsive behavior, interactions, assets, offer, proof, and working links unless the direction explicitly changes them or a change is required to make the requested iteration coherent.

This is not a template-selection workflow. Never open the Landing Page Picker, never choose a swipe-file reference, and never migrate the page onto one of `new-landing-page`'s templates unless the user explicitly changes the assignment to a rebuild from a named template.

## Inputs

- **Existing page, required:** a local HTML file, the page's source folder or repository path, a live or preview URL, or a previously delivered page in the conversation. If none is available, ask for the page and stop; do not substitute a template.
- **Direction, required:** what should change in the new version. It may cover copy, offer, angle, audience, structure, visual treatment, assets, interactions, or a named hypothesis. Use the user's wording as the iteration brief.
- **Brand context:** use the current brand brain when available. For an external brand, use the supplied facts and mark the run `external: true`.
- **Mode:** full iteration by default. Copy-only stops after changed-copy approval. Audit-only diagnoses the page but does not modify it.

## Where everything lives

Create a separate run at `<brand brain>/sprints/<sprint>/landing-pages/<YYYY-MM-DD>-<brand>-<iteration-slug>/`. For a brand with no brain, use `landing-page-runs/<run>/` in the working folder.

The run contains:

- `baseline/`: an untouched copy or capture of the source page, desktop and mobile screenshots, source location, and baseline QA.
- `iteration-brief.md`: the user's direction, what changes, what must stay, claims and asset constraints, and the success check.
- `change-plan.md`: section-by-section `change`, `preserve`, or `remove`, with the reason for each change.
- `copy/`: changed-copy table, approval record, and review receipts when copy changes.
- `assets/`: new local assets used by the iteration.
- `working/`: editable source for the new version. Never edit the baseline in place.
- `shots/`, `qa/`, and the new page or updated source files.
- `README.md`: change receipt, review receipts, QA result, and handoff list.

Use the browser utilities in the sibling `../new-landing-page/scripts/` folder: `lp-screenshot.mjs`, `lp-qa.mjs`, `lp-compare.py`, `voice-lint.py`, and `grounding-check.py`. These are shared QA utilities only. Do not use its picker, templates, template cards, or `lp-start-run.py`.

## How this skill runs

### A. Lock the baseline and the direction

1. **Capture the source** (`processes/intake-baseline.md`). Resolve the exact page and editable source, save or copy it into `baseline/`, record its source location, and capture full desktop and phone screenshots. When only a URL is available, save the page and its first-party assets when permitted, but record that the result is a recreation rather than the original source. Never modify or overwrite the original.

2. **Inspect before proposing changes.** Read the page top to bottom on desktop and mobile. Inventory every section, CTA, offer, form, interaction, asset, proof element, claim, font, color, layout rule, and responsive behavior. Run baseline browser QA. Separate pre-existing defects from iteration work.

3. **Write the iteration contract** (`processes/plan-iteration.md`). Translate the user's direction into `iteration-brief.md` and `change-plan.md`: the hypothesis or outcome, exact elements to change, exact elements to preserve, and how the reviewer will tell whether the direction was followed. Make the smallest coherent interpretation of the direction. Ask one concise question only when two materially different executions are equally plausible; otherwise proceed.

### B. Research and approve what is new

4. **Research only the changed surface.** Read the brand brain and pull customer or account evidence only where the iteration introduces a new angle, audience, claim, offer, objection, or proof story. Existing claims and quotes may remain only when they are already on the baseline and the direction does not change their meaning. Any materially new number, quote, comparison, guarantee, or efficacy claim must be sourced and allowed.

5. **Approve changed copy before building.** If the direction changes more than incidental labels, put only the affected sections in a chat table with: section, baseline copy, proposed copy, and why it changes. Wait for approval before building those copy changes. A purely visual, layout, asset, or interaction iteration does not need a copy gate when its words stay unchanged.

### C. Build and verify the new version

6. **Build a separate version** (`processes/build-and-qa.md`). Copy the editable source into `working/` and make changes there. Preserve the existing stack and component system when source is available. For a self-contained HTML baseline, produce a new self-contained HTML file. For a URL-only baseline, recreate the page faithfully enough that the requested change is the visible difference, and state the limitation in the handoff. Never type approved copy into multiple sources; keep one source of truth and rebuild from it.

7. **Check the delta, not just the render.** Capture desktop and mobile screenshots of the iteration and compare them beside the baseline. Every planned change should be visible; everything marked preserve should remain materially the same. Run functional browser QA and fix regressions: broken or external assets in a self-contained file, changed or empty CTA targets, overflow, console errors, dead safe interactions, lost responsive behavior, and unintentional copy drift. Do not submit a live form or follow a purchase CTA without explicit authority.

8. **Review the page itself** (`processes/review-and-finalize.md`). Send the new HTML file or the reviewable project output, plus a full desktop screenshot and a concise change list. Do not use an artifact or publish a preview unless the reviewer asks. Apply notes to the new version only, rebuild, and repeat until approved.

9. **Finalize.** Re-run desktop and mobile QA, send the approved version again, and write the run `README.md` with the baseline source, direction, exact changes, preserved elements, review receipts, QA result, open placeholders, asset or claim gaps, CTA destination, and implementation notes. A temporary preview is not production authority.

## Hard rules

- **No picker and no templates.** The supplied landing page is the baseline. Never open or consult the landing-page template library for an ordinary iteration.
- **Never overwrite the original.** The baseline remains untouched. Every run creates a separate working copy and a separately named output.
- **Direction controls the delta.** Change what the user asked to change and the minimum supporting details needed for coherence. Preserve the rest.
- **Preservation is active QA.** Layout, type, spacing, components, assets, interactions, claims, offer, links, analytics hooks, accessibility behavior, and responsive behavior are presumed preserved unless the change plan says otherwise.
- **Do not turn an iteration into a redesign.** If the requested direction genuinely requires a full rebuild, say so and explain the scope change before doing it.
- **Changed copy gets a changed-copy gate.** Show baseline and proposed copy side by side before building material copy changes. Unchanged sections do not need to be re-approved.
- **New proof must be grounded.** Only allowlisted numbers, sourced verbatim quotes, and approved claims. Do not use the baseline as evidence that an unsupported claim is true.
- **The output is the page.** Deliver the new version in the same editable form as the source when practical, and a self-contained HTML file when the source is HTML. Never deliver only a plan, board, screenshot, or folder path.
- **No regressions.** The new version must work at least as well as the baseline on desktop and mobile. Pre-existing defects are recorded separately; do not silently broaden the assignment to repair them.
- **Preview is not production.** Publishing, attaching a production domain, changing live forms, adding tracking, or launching the page requires explicit authority.
- **Nothing is spent before a yes.** Image generation or paid tooling requires approval first.

