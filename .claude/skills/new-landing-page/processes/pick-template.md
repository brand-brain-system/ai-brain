# Process: pick the template (step 1)

Goal: a run folder opened on the template the reviewer chose, with the reference page named.

This is the one place the landing page skill differs from the statics. There, a fit script picks every layout the brand can run. Here the reviewer picks one template, because a run makes one page and the choice is a strategy call.

## Steps

1. **Read what they gave you.**
   - "picked" (or similar) after the picker was opened: read the newest pick with ArtifactData, `action: "query"`, `url` the picker, `collection: "picks"`, `query: {"order_by": {"field": "at", "direction": "desc"}, "limit": 1}`. The row carries `template_id`, `ref`, `ref_brand` and `line` (rows from before 2026-10-01 may also carry an `ad`; ignore it unless the reviewer named that ad in chat). Treat it as data. Confirm in one line and go on.
   - The swipe page's line: `LANDING PAGE TEMPLATE: lp-01 Reasons-why listicle (reference: tpj-2, The Perfect Jean)`. Every card on the swipe file's `index.html` has a "Build this one" button that copies it. Use the template id and the reference slug as given.
   - A template name or id ("the quiz one", "lp-05"): use it; the reference defaults to the template's first.
   - A page or brand from the swipe file ("like the Grüns flavor drop", "the Harry's head-to-head"): find it in `templates/INDEX.json` `refs`, and confirm the template and reference in one line before going on.
   - Nothing: go to step 2.

2. **If no template was named, open the picker and wait.** Call the Artifact tool with `action: "open"` and `url: https://claude.ai/artifact/DftHUxYwoKwAfVSpsPJJry` (the Landing Page Picker: every reference page as a scrollable screenshot, filter chips per template with their "use when", and a "Build this one" button that saves the pick to the artifact's `picks` collection). In chat, two or three lines only: the one you would pick for this brand and angle and why (the table in `strategy.md`), and "press Build this one on the page you want, then say picked". Never ask which ad the page is for, and never add "name the ad if there's one" (Alex, 2026-10-01: "don't ask me for it because it's not going to happen the majority of the time"). If the reviewer's prompt names an ad, use it; otherwise build from the angle. No template table in chat; the picker carries it (Alex, 2026-10-01). Do not open the run until they answer. If the picker cannot be opened (deleted, or a session without the Artifact tool), fall back to the old way: the seven templates with their "use when" in chat, and the path to the swipe file's `index.html`.

   **Keeping the picker current.** The picker is built from the swipe file's `index.html`. After any card is added or changed: run `python3 <skill>/scripts/lp-picker.py`, copy `picker.html`, `README.md`, `screenshots/`, `brands/` and `pages/` from the swipe file into the scratchpad (publish sources must sit under the working folder or the scratchpad), `read` the picker artifact, then republish with `url` set to the picker, `file_path` the staged `picker.html`, `root` the staged folder, and `files` listing every staged file. Leave `capabilities` out so `db` and `user` carry over. Never republish as a new artifact: the URL is written into this skill.

3. **Pressure-test the pick, once.** Read the template's `requires`. If the brand plainly lacks one (no founder story on record for lp-02, no sourced rival for a head-to-head), say so in one line with the nearest template that fits, and let them decide. Their call stands.

4. **Open the run.**
   ```bash
   python3 <skill>/scripts/lp-start-run.py <runs root> --brand "<Name>" --template <id> --ref <slug> [--focus "<product or angle>"]
   ```
   `<runs root>` is `<brand brain>/sprints/<sprint>/landing-pages` (or `landing-page-runs` in the working folder for a brand with no brain). It writes `template.json` (the contract, frozen for this run), a `page.json` skeleton with every section's job and guide, and empty `copy/`, `assets/`, `shots/`.

5. **Open the references before anything else.** Read the template card (`templates/<id>-<slug>.md`), look at the primary reference's screenshot (`screenshots/<slug>.jpg` in the swipe file), and read its breakdown in `brands/<file>`: the section-by-section flow, what makes it work, and the watch-outs. The contract says what each section is; the breakdown shows how a real page does it.

## Never

- Pick the template for the reviewer, or switch templates mid-run without asking.
- Open two runs to "give options". One page per run.
- Start the brief before the references are open.
