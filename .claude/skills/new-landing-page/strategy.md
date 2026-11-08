# Strategy: which way to run new-landing-page

Read the ask, the angle (and the ad, if one is named) and the brand before touching the library.

## 1. Which brand, and how much the brain already knows

- **A brand with a built brain** (a folder with `brain_config.json`, `brand-lens.md`, `sub-context-docs/`): auto-fill the brief from the docs listed in `brief-schema.md`. Ask only for what the docs do not hold, which is nearly always the offer (number, code, dates) and the button link. Never ask for an ad; propose the angle from the evidence if the ask has none.
- **A brand with no brain**: the brief is the pasted context plus one round of questions. Mark it `external: true` so the run README says the facts came from the conversation, and write the run to `landing-page-runs/<run>/` in the working folder.

## 2. Copy only, or a full run

- **Full run** (default): all nine steps.
- **Copy only** (the ask says "just the copy", "outline it", "what would it say"): steps 0 to 4. Deliver the approved copy table and `page.json`; say the page can be built from it any time.
- **Revision** (the ask says "revise", "apply my notes", "I left feedback"): go straight to step 8 on the newest run for that brand.
- **Library build** (adding or changing templates): `processes/build-template-cards.md`, no brand work.

## 3. The template is the reviewer's pick

The reviewer chooses. Your job at step 1 is to make the choice easy and informed:

- If they pasted the swipe page's line (`LANDING PAGE TEMPLATE: lp-01 Reasons-why listicle (reference: tpj-2, The Perfect Jean)`), use it as given.
- If they named a page or a brand from the swipe file ("do the Grüns flavor drop one"), map it to its template and reference and confirm in one line.
- If they named nothing, open the Landing Page Picker artifact (`processes/pick-template.md` step 2), recommend one in chat with the reason, and wait for "picked".

**How to recommend** (from the swipe file's picker, `README.md`): match the template to the job the page is doing (or the named ad, if any).

| If the page (or the ad)... | Recommend |
|---|---|
| Comes from many creators with different angles | lp-01 Reasons-why listicle |
| Tells a founder or origin story to a problem-aware, older buyer | lp-02 Founder-story long page |
| Picks a fight with a known incumbent | lp-03 Advertorial |
| Speaks to a buyer who already wants the category | lp-04 Product page built for ads |
| Sells a trial, a free gift or a limited drop | lp-05 Offer lander |

Say it plainly if their pick fights the evidence (a founder page for a brand with no founder story on record; a head-to-head with no sourced rival facts), show why, and let them decide. Then build what they chose.

## 4. Can the brand fill the template

After intake, read the template's `requires` against the brief before writing a word:

1. **Required inputs present?** Each item in `requires` must exist in the brief (an offer, a founder story, a rival with sourced facts, bundle items with prices). If one is missing, ask once; if it does not exist, tell the reviewer the template cannot be run honestly and name the nearest template that can.
2. **Urgency.** The template's urgency device (a countdown, "almost gone") is used only when `urgency_allowed` is true and the date or stock limit is real. Otherwise the offer bar states the offer without a clock.
3. **Proof.** Review sections need verbatim sourced reviews; press bars need real press; stat strips need allowlisted numbers; expert bylines need a real named expert. A missing proof type drops its optional section, or takes the adaptation on the template card. Never a lookalike.
4. **Photos.** List which sections need a photo and which the brand has. The rest become labelled boxes and go on the handoff list.

Record what dropped and why in `brief.md` under "Template fit", and say it in one line above the copy table.

## 5. When to stop and ask

Once at step 1 if no template was picked. Once at intake for missing facts. Once at the copy table. Once at the draft board. Never for taste: write the copy from the evidence, deliver, and offer to pivot.
