---
name: new-landing-page
description: Create one new landing page from a brand brief by recreating a proven page structure from the landing-page swipe file. The reviewer picks the template, approves the section-by-section copy in chat, reviews the self-contained HTML draft, and receives a browser-verified final page with a QA report and handoff list. Use for a net-new lander, listicle, advertorial, offer page, or a request to recreate one of the library's reference pages for a brand. Do not use when the user supplies an existing landing page and asks to change, improve, adapt, or make a new version of it; use iterate-landing-page instead.
---

# New Landing Page

Owner: Alex Cooper. Built 2026-09-30 for Parker course session 6, on the offer-statics and static-ad-engine production line (template library, brief, copy table approved in chat, review gates, a board with Feedback, a learning loop). The one change from the statics: **a run makes one landing page, and the reviewer picks the template.** No fit table that picks for them, no batch, no variations.

## Local setup (read first)

Ported 2026-10-06 from Alex Cooper's Adcrate build, shared through the Parker course for participants to use and adapt (see `NOTICE.md`); his name and dated decisions stay in the text as credit and history. The rest of this skill is his wording, so where it says the left column, do the right one. The sibling skills (`iterate-landing-page`, `cro-review`, `page-qa`, `extract-page-template`) use this table too.

| Alex's text says | Here |
|---|---|
| Brand truth: `brand-lens.md`, `sub-context-docs/`, `personas/`, `running-notes/brand-rules.md` | `brand-lens.md` (voice, claims gate, **proof inventory**), `sub-context-docs/brand-profile-narrative.md` (product, prices, offer, mechanism), `sub-context-docs/visual-vocabulary.md` (palette, fonts, photo style), `personas/`, `assets/`, `running-notes/feedback.md` |
| Run output `<brand brain>/sprints/<sprint>/landing-pages/<run>/` | `<brand brain>/sprints/<sprint>/landing-pages/<YYYY-MM-DD>-<brand>-<template>/` |
| The Parker MCP (reviews, ad comments, survey, account search) | The brain's `source-pulls/` (dated pulls) and `personas/voice-of-customer/voice-of-customer.md`. Thin bank (under 30 phrases): pull fresh from the sources in `source-pulls/README.md` and save the pull there first. A named ad comes from the Meta Ad Library. The Parker MCP only if it's connected |
| The Landing Page Picker artifact (Alex's URL) | That artifact is Alex's, not ours. Send the local `swipe-file/index.html` with SendUserFile (display render); the reviewer presses "Build this one" and pastes the copied line into chat. Our own picker can be published later with `processes/pick-template.md` step 2; write its new URL here |
| Method docs in `parker-system/creative-strategy-context/`, agents in `.claude/agents/` | The factory's `brain-system/creative-strategy-context/` (the five method docs Alex bundled are carried there, from Parker) and the factory's `.claude/agents/` |
| `python3 <script>` | `python -X utf8 <script>` (on Windows `python3` is a Store stub; `-X utf8` keeps æ, ø and å intact) |
| Chrome at the macOS path | The scripts find Chrome or Edge on Windows themselves (patched 2026-10-06); `CHROME=<path>` overrides |
| Higgsfield image generation | The fal.ai MCP: `get_pricing` first, then a yes |
| `/anonymise` | No such skill here. Before a client's page is shown outside the team, take out the brand name, prices and quotes by hand. A page for a brand that isn't a client says "Concept, not commissioned by <brand>" in its footer |
| "Parker Desktop syncs the brain; do not run git" | Doesn't apply: a brain is a git repo; pull before work, push after (`CLAUDE.md`) |

**Danish pages.** The copy also gets the long-text checks from `static-ads/copy-guide.md`: chiefing, LIX (`python -X utf8 ".claude/skills/static-ads/lix.py" "<text>"`) on every section of 30 words or more, and the AI check by judgment, since `voice-lint.py` only knows English. An offer lander (lp-05) follows the Danish price rules in `offer-ads/offer-copy.md`: no før-pris or "spar" without the documented 30-day lowest price. Health wording follows the EU section of `brand-lens.md`.

**Light machine.** Screenshots and QA are cheap. Build once, compare, fix the source, rebuild: no loop of full-page captures.

## Goal

Take a brand (what it sells, the offer, what it may claim, its real reviews and photos, and the angle or the ad behind the page) and the template the reviewer picked, and produce one landing page: every section written for the brand at the template's contract, the claims check and both review gates passed, the copy approved by a human, then built as a working phone-first HTML page, reviewed from the file or a request-only preview, revised, browser-verified, and handed off with a QA report.

**The library is the point.** Each template is a section contract taken from pages that big accounts put real spend behind: which sections, in what order, each section's job and word budget. The skill does not invent page structures; it fills the one the reviewer picked.

**The second law: the page keeps one promise.** Every run names the angle the page sells (the problem it solves, for whom) and the hero states it plainly. Naming a specific ad is optional (Alex, 2026-10-01: "We don't have to necessarily do this. I don't like forcing this into the skill."). When the reviewer names one, the page matches it: the headline repeats the ad's promise, the offer is the ad's offer, the featured review is from someone like the person in the ad. When they don't, build from the angle and the buyer, and never ask for an ad.

## Inputs

- **Brand**: from the command or the conversation; ask if missing.
- **The template**: the reviewer picks it (step 1). Never pick for them.
- **The angle**: what the page sells and to whom. Taken from the ask, else proposed from the brand's evidence (the brain, the account's proven lines, the customer voice) and stated in one line at intake; never a blocking question.
- **The ad (optional)**: a Parker ad link or ad name, only if the reviewer puts one in their prompt. Never asked for: not in chat, not in the picker, not as "name it if there's one". Most runs have none.
- **The offer**: mechanic, number, code, dates. Almost never on file; asked once at intake. Prints as `[OFFER]` until stated.
- **Mode**: copy only (stops after the approved copy) or full run. Default is a full run.

## Where everything lives

Paths are relative to this skill's folder, wherever it is installed.

| What | Path |
|---|---|
| This skill: workflow, rules, brief schema | `SKILL.md`, `strategy.md`, `brief-schema.md`, `processes/` |
| The template library | `templates/INDEX.json` (the 5 section contracts the scripts read: lp-01 reasons-why listicle, lp-02 founder-story long page, lp-03 advertorial, lp-04 product page built for ads, lp-05 offer lander. Renumbered 2026-10-01 after Alex removed the quiz finder and angle-swap templates; runs before then use the old ids (old 02, 03, 04, 06, 08 = new 01 to 05)) and `templates/lp-NN-<slug>.md` (the same, readable) |
| The swipe file | `swipe-file/` inside this skill (moved in from beside it on 2026-10-01; it is the skill's template library, not a skill of its own). `index.html` is the source of the cards; `picker.html` (built from it by `scripts/lp-picker.py`) is published as the **Landing Page Picker** artifact, https://claude.ai/artifact/DftHUxYwoKwAfVSpsPJJry, where the reviewer picks; `screenshots/` are the phone-width references; `brands/` are the per-page breakdowns; `README.md` has the master outlines |
| Scripts | `scripts/` (they find the skill folder themselves; run them from anywhere) |
| Page and board templates | `assets/board-template.html`; the page's own components live in `scripts/lp-build-page.py` |
| Helper-agent briefs | `references/agent-briefs/` |
| Feedback | `references/feedback-boards.md` (every board), `references/feedback-log.md` (what each note changed) |
| Method docs | The factory's `brain-system/creative-strategy-context/` (mounted in the brain at `brain-system/`) |
| Review agents | The factory's `.claude/agents/` |
| Brand truth | The brand's brain: `brand-lens.md`, `sub-context-docs/`, `personas/`, `running-notes/brand-rules.md`. The doc-to-field map is in `brief-schema.md` |
| Run output | `<brand brain>/sprints/<sprint>/landing-pages/<YYYY-MM-DD>-<brand>-<template>/`. A brand with no brain: `landing-page-runs/<run>/` in the working folder, brief marked `external: true` |

## What you are working from

Methods, loaded before any run: `brain-system/creative-strategy-context/emotional-delivery-and-timing.md` (the buying phase the page has to meet: Trigger, Exploration, Evaluation, Purchase; at Evaluation, name the hesitation rather than adding pressure), `brain-system/creative-strategy-context/advertising-to-older-audiences.md` (clarity over cleverness, authority, longer stories; most big accounts in the swipe file spend on buyers 45 and up), `brain-system/creative-strategy-context/advertising-luxury-and-higher-price-points.md` (the price objection, for anything above category average), `brain-system/creative-strategy-context/customer-review-mining-method.md` (how to pull the buyer's words), `brain-system/creative-strategy-context/ai-writing-tells.md` (the lint the voice gate runs). The swipe file's `README.md` carries the master outlines and the seven rules that held across brands.

Tools: the 21st.dev MCP only when the reviewer asks for it (off by default since Alex preferred the page without it, 2026-09-30; `processes/build-draft.md`), the Parker MCP if one is connected (`search_facebook_ads_sql` for the named ad when there is one, and the account's proven hooks and angles, `search_customer_reviews_semantic` and `search_facebook_ad_comments_semantic` for buyer language), the two review agents, SendUserFile for the page (the Artifact tool only for the template picker at step 1, or when the reviewer asks for a published link or a board by name), ArtifactData to read the pick, and the scripts:

- `lp-start-run.py` (opens the run from the picked template)
- `lp-copy.py collect | check | table` (all the copy in one file; the claims and structure check; the approval table)
- `lp-build-page.py` (the page, from `page.json`)
- `lp-screenshot.mjs` (desktop and phone screenshots, for QA)
- `lp-qa.mjs` (desktop and phone browser QA: links, embedded assets, responsive overflow, safe interactions, forms and console errors)
- `lp-compare.py` (reference and draft side by side, in strips, for the look check)
- `lp-board.py` (the draft board and the final board)
- `lp-validate-templates.py` (the library)
- `lp-picker.py` (rebuilds the picker artifact's page from the swipe file after a card changes)
- `brain-system/scripts/voice-lint.py`, `brain-system/scripts/grounding-check.py` (the gates' mechanical layer)

## Background that loads up front

- **Every new landing page starts from a template, and looks as much like its reference page as possible** (Alex, 2026-10-01: "always uses the templates as the base, and we should make the design look as much like the template as possible. It should be delivered in HTML, not in an artefact."). There is no from-scratch path for a new page: a net-new landing-page request runs this skill, on one of the five templates and one of its reference pages. A request to modify an existing page routes to `iterate-landing-page` instead. Sections, their order, each section's job and word budget are fixed, and the page is a near-copy of the reference's design: the same layout and grid on desktop and phone, the same type treatment (weights, case, sizes, tracking), the same spacing and rhythm, the same component shapes (cards, borders, shadows, radii, pills, badges, edges and flourishes), the same colour roles and contrast, the same interactions. Someone who has seen the reference should recognise it in two seconds. Only four things change: every word (from `page.json`), the product photos (the brand's), the logo (the brand's), and the accent colours (the reference's brand hues mapped one to one onto the brand's). The reference's neutrals, grounds, borders and shadows stay as they are. (Earlier: Alex, 2026-09-30: "this doesn't look anything like the initial one that I chose".) If the brand cannot fill a required section honestly, say so at the copy table and offer the template's own adaptation (on its card); never redesign the page to force a fit. Optional sections drop cleanly.
- **Numbers are the whole risk.** Every price, percent, count, rating and guarantee window on the page comes from the brief's allowlist. The check stops the run on a miss. The offer is `[OFFER]` until the brand states it; a missing proof number is `[STAT NEEDED: verify before publishing]`, never a plausible guess.
- **Proof is real or absent.** Review quotes are verbatim and sourced. No invented author, expert, press logo, customer count or rival fact. A section whose proof the brand lacks drops or takes the adaptation on the card.
- **Urgency is a brand rule, not a default.** Countdown bars and "almost gone" lines appear only when `urgency_allowed` is true and the deadline or stock limit is real.
- **Photos are placed, never invented.** Real brand photos saved in the run's `assets/` folder. Where none exists, the page shows a labelled "PHOTO NEEDED" box and the handoff lists it. Never describe or restyle the product, and never borrow a reference page's images.

## How this skill runs

Nine steps in three parts, the same shape as offer statics. Parts A and B each end with the reviewer deciding.

0. **Apply open feedback first** (`processes/apply-feedback.md`). Read every board in `references/feedback-boards.md` for notes with status `new`, fold each into the right file (a template, a process, the rules, or the brand's own brain), log it, and mark it on its board. Also whenever the reviewer says "apply feedback".

### A. Plan the page

1. **The reviewer picks the template, in the picker artifact** (`processes/pick-template.md`). Unless the ask already names a template or a reference page, open the Landing Page Picker artifact (https://claude.ai/artifact/DftHUxYwoKwAfVSpsPJJry) with the Artifact tool's `open` action, say in two or three lines which one you would pick for this brand and angle and why, and wait. They press "Build this one" on a card and say "picked" in chat; read the newest row of the artifact's `picks` collection with ArtifactData and confirm the template, reference and angle in one line (Alex, 2026-10-01: "I want to pick from an artefact where I get to see all the landing pages"). Neither the picker nor the chat ever asks which ad the page is for; an ad only enters the run when the reviewer names one in their prompt (Alex, 2026-10-01). Then `lp-start-run.py <runs root> --brand <Name> --template <id> [--ref <slug>]` opens the run with `template.json` and a `page.json` skeleton.

2. **Research the brand** (`processes/intake-brief.md`). Fill `brief.md` and `brief.json` from the brand's brain, quoting the doc for every field: product, prices, the offer, the allowlist, what may not be said, verbatim reviews, photos, palette and type, the page's button link. Settle the angle (from the ask, or proposed from the evidence); if the reviewer named an ad, pull it (its hook, angle, the promise to match). Pull the buyer's own words through the Parker MCP, at volume and from every source the brand has: reviews (semantic and counted), ad comments across the account (and the named ad's own, if any), the post-purchase survey, Reddit and TikTok. They go into a customer-voice bank of 30 or more verbatim phrases in `brief.json`. Ask for every missing field in one message, then stop until answered. Never guess a price, a claim or an asset.

3. **Write and check the copy** (`processes/write-page-copy.md`). Fill `page.json` section by section: open the template card and the primary reference's screenshot and breakdown, write each section to its job and word budget, built from the customer-voice bank (each key line traced to the phrase it came from in `page.json`), in the brand's register, from the brief's facts only. The hero states the page's promise (the named ad's, when there is one). Then `lp-copy.py collect` and `lp-copy.py check` until it passes, then spawn `context-grounding-review` and `creative-voice-review` yourself, in parallel, on the whole page's copy (`references/agent-briefs/review-gates.md`); fix and re-run until grounded and ships, three rounds at most (`brain-system/system/agent-teams.md`); a landing page is always Ship tier. Nothing else spawns these; if you do not, they do not run.

4. **The reviewer approves the copy, in chat** (`processes/approve-copy.md`). `lp-copy.py table` builds it: **one row per section** (section, what that section does on the reference page, the proposed copy with every line joined by " / "). Paste it as a plain table in the reply, one line above it saying how to reply, and stop. Apply edits and cuts exactly as written, re-run the check on changed lines, record `copy/approval.md`. Nothing is built before this.

### B. Make the page

5. **Build the page as a recreation of the reference** (`processes/build-draft.md`). Capture the whole reference page on desktop and on a phone (`lp-screenshot.mjs <url> --desktop --height 11000` and `lp-screenshot.mjs <url> --height 14000`), write `design-spec.md` (the reference's visual grammar block by block, its desktop and phone layouts, and which approved section fills each block), then write the run's `build-design.py` from `assets/example-design-build.py`: one responsive page, the reference's desktop layout on a computer and its phone layout on a phone, matched to the reference as closely as possible (only words, photos, logo and accent hues change), every word read from `page.json`, the photos embedded. Never type copy into the HTML. `lp-build-page.py` is only a quick structural preview, never the deliverable. Generating a missing lifestyle photo is optional and only after a cost yes; the product is always a real photo. Default to one full-page build. If two comparison passes show the same shared visual drift, lock the hero and next one or two blocks against the reference first, then extend that visual system down the page section by section. This is an internal recovery mode, not a third human approval gate.

6. **Check the build, desktop first.** `lp-screenshot.mjs <run>/<page>.html <run>/shots/draft-vN-desktop.png --desktop --keep-popups` and the same without `--desktop` for the phone, then run `lp-compare.py <reference.png> <draft.png> <run>/shots/compare-vN` (side-by-side strips, reference left, draft right) and read every strip. Run `node <skill>/scripts/lp-qa.mjs <run>/<page>.html --out <run>/qa/qa-vN.json --cta-url <cta_url>` and fix every failure: broken or non-embedded assets, empty or mismatched CTA links, horizontal overflow, console errors, uncaught exceptions, missing form wiring and safe interactions that do not respond. The script never submits a form; verify its route and validation locally, and never submit to a live endpoint without explicit authority. Then check: does it look like the reference, block by block, on desktop and on the phone; every approved line present and unchanged, sections in template order, no leftover placeholder that should be filled, nothing clipped at phone width, interactive sections (quiz, card game, FAQ) working. A fault in the build is fixed in `page.json`, `brief.json` or the builder, then rebuilt; never patched in the HTML.

7. **Send the page as an HTML file** (`processes/review-and-revise.md`). Send the self-contained `<brand>-<page>.html` from the run folder with SendUserFile, so it opens like a real landing page in any browser, together with a full-length desktop screenshot (`shots/<page>-desktop.jpg`). The reviewer judges the web version first (Alex, 2026-09-30: "I ideally want to see the web version, not the mobile version. You can give me both, but I'm more so caring about the web version right now."). Not an artifact and not a board (Alex, 2026-09-30: "I want this delivered to me as an HTML doc, like an actual landing page, not an artefact", after "You don't need to send me to an artefact here to give feedback"). The reviewer replies in chat: notes by section ("S03: ..."), "approved" or "finish it". When the reviewer asks for a shareable review URL, publish this exact QA-passed draft to a temporary preview URL and record it; do not silently make a public page, attach a production domain or treat preview publishing as approval to launch. The section-feedback board remains request-only.

### C. Finish

8. **Revise.** Take the reviewer's chat notes, route each with `processes/apply-feedback.md` (a note about this page changes `page.json`; a note about the template or the skill changes the skill), bump `page.json` `version`, re-run `lp-copy.py check`, run the voice gate on changed lines, rebuild, re-check, and send the rebuilt HTML file. Reply with one line per change. Copy changes beyond what the notes asked for go back through the chat table. Repeat until the reviewer approves.

9. **Final page** (`processes/finalize.md`). Once approved: the final self-contained HTML file (sent again), a final phone screenshot, the passing final browser-QA report, and `README.md` in the run folder with the three receipt blocks and the **handoff list**: every open placeholder, every photo still needed, the button link, any temporary review URL, and the build notes for whoever puts it live. Parker Desktop syncs the brain; do not run git.

## Output structure

Run folder `<YYYY-MM-DD>-<brand>-<template>/`:

- `template.json` (the picked contract, frozen for the run), `brief.md`, `brief.json`
- `page.json` (the page: every section's copy, the source of truth)
- `copy/all-copy.md`, `copy/approval-table.md`, `copy/approval.md`
- `assets/` (the photos), `design-spec.md`, `build-design.py`, `<brand>-<page>.html` (the deliverable, self-contained), `shots/`, `qa/` (one JSON browser-QA report per draft)
- `README.md` with counts, decisions, the handoff list and the three receipt blocks

### Brand Context Applied

What I used (which docs and brief fields shaped the copy), what I avoided (banned claims, devices and words, and what replaced them), why this template and this angle fit the brand's moment.

### Grounding Review

The `context-grounding-review` verdict, one or two plain sentences on what it checked (every number traced to the allowlist, every quote to its source, the hero's promise matched to the angle, and to the named ad when there is one), and what was rewritten if it bounced.

### Voice Review

The `creative-voice-review` verdict, lint density before and after across `copy/all-copy.md`, what was flagged and fixed, any flag kept with its reason.

## Growing or changing the library

New templates come from new swipe pages: `processes/build-template-cards.md`. Edit `templates/INDEX.json`, then `lp-validate-templates.py --write-cards`. To cut a template, delete its entry and its card.

## Hard rules

- **Every new page uses this skill and a template.** A request to create a new landing page, lander, listicle page, advertorial or offer page builds on a template from `templates/` with a reference page from the swipe file. A request to revise or adapt an existing landing page uses `iterate-landing-page`, with that page as the baseline and no template picker. Never design a new page from scratch, never use a generic layout, and never use the artifact-design treatment (Alex, 2026-10-01: "always uses the templates as the base, and we should make the design look as much like the template as possible. It should be delivered in HTML, not in an artefact.").
- **One page per run.** No batches, no variations. A second page is a second run (a second template, or the same template for a second angle).
- **The reviewer picks the template, from the picker artifact.** Open it every run that has no named template; recommend in chat; never choose silently.
- **Copy approval gate.** Nothing is built until the reviewer has seen the one-row-per-section table in chat and replied. Not a file, not a page: the table in the reply.
- **Every later stage is delivered as the page itself, as an HTML file.** The draft and the final go out as a self-contained HTML file sent in chat with SendUserFile, plus a desktop screenshot. Never an artifact, a board or a folder (Alex, 2026-09-30 and 2026-10-01). Do not call the Artifact tool for a landing page unless the reviewer asks for a published link or a board in so many words. The one standing exception is opening the template picker at step 1. A folder path is a footnote, never the deliverable.
- **It has to look like the page they picked, as closely as possible.** A page that only follows the reference's section order has failed the build step. Copy the reference's layout, type treatment, spacing, components and flourishes; change only words, photos, logo and accent hues. If you would not mistake a strip of the draft for the same strip of the reference with the words blurred, it fails QA.
- **Rendering is not completion.** Every draft passes `lp-qa.mjs` at desktop and phone widths before it is sent: no broken or external assets in the self-contained file, placeholder links, CTA mismatch, sideways overflow, console errors or dead safe interactions. A form's wiring is checked without submitting it; a live submission requires explicit authority.
- **One promise, matched when there's an ad.** The run names its angle and the hero states it. An ad is optional and never asked for (Alex, 2026-10-01). When the reviewer names one, the hero repeats its promise and the offer is its offer; a mismatch then is a build failure, not a style note.
- **Never redesign the template.** Sections, order and jobs come from the contract. Adapt with the card's named swap, drop an optional section, or tell the reviewer the template is the wrong pick.
- **The customer writes the page.** Headlines, bullets, reason titles and FAQ questions are built from verbatim customer phrases pulled through Parker (reviews, ad comments, survey, Reddit, TikTok), traced line by line. Marketing voice only where no customer phrase does the job, and the trace says why (Alex, 2026-10-01).
- **Only allowlisted numbers, only verbatim sourced quotes, no invented proof.** The check is a wall. Health and efficacy lines stay inside the brand's approved wording.
- **Nothing from the reference page is reused.** Structure is borrowed. Its words, images, logos, names and numbers are not. The reference column in the approval table describes what a section does; it never quotes it.
- **Photos are real and local.** Saved in `assets/`, placed as they are. A missing photo is a labelled box, not a generated product.
- **Every button goes to one link.** `cta_url`, with the offer already applied where the brand can do that.
- **Both gates run every time, on the whole page's copy, spawned by you.** No page ships with a missing receipt block.
- **Fix the source, rebuild the page.** Copy lives only in `page.json`; the HTML is always generated by the run's build script. Never hand-edit the output file.
- **Feedback is the learning loop.** The reviewer's notes arrive in chat (or as comments on the published page, or on a board if they asked for one); each is applied or declined with a reason, and anything that is a lesson for every run goes into the skill, logged in `references/feedback-log.md`. Everyone's feedback counts the same.
- **Preview is not production.** A temporary shareable review URL is created only when the reviewer asks. It contains the exact QA-passed draft, is recorded in the run README, and grants no authority to attach a real domain, add tracking, submit data or launch the page.
- **Nothing is spent before a yes.** Image generation, if used at all, is preflighted and approved first.
- **What leaves the building.** The template library and the swipe file's screenshots are public pages and safe to show. The swipe file's spend tables, and every brand's brief, copy and page, are client material: `/anonymise` before anything is shown outside the team.
