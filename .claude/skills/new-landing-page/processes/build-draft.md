# Process: build the page and check it (steps 5 and 6)

Goal: a working phone-first page built from the approved copy, checked against the template and the reference, and verified in a real browser before the reviewer sees it.

## Build (step 5)

1. **Read new feedback first.** Any note with status `new` on a registered board that touches this template or the skill is applied before the build (`apply-feedback.md`).

2. **Set the brand's look** in `brief.json` `tokens`: `palette` (the page background, ink, the button colour as `accent`, a soft panel colour), `fonts` (the brand's own font files first: check the brain's assets, then the brand's site CSS for its `.woff2` files, and embed them in the page; a Google Fonts stand-in only when neither exists), `logo` (text, or `src` pointing at a file in `assets/`). Take them from the brand's identity doc or its site; note in `brief.md` where each came from.

3. **Place the photos.** Every image in `page.json` is `{"src": "assets/<file>"}` or a `{"placeholder": ...}`. Files come from the brand's asset folder, or from its own site once the reviewer has said yes to saving them (name the files, source and size when asking). Resize anything over about 1600px wide. The product is always a real photo, placed as it is. Go through the brand's whole asset pull, not the two hero files: cut packshots out of their plain backgrounds so they can float across section edges, use people drinking or using the product (faces beat faceless product shots), use ingredient or texture shots as design elements, and never show the same photo more than twice (Alex, 2026-09-30: the reference "still feels a level above in design").
   - **Optional, only on a yes:** a missing lifestyle or scene photo can be generated with an image model. Preflight the cost, say "N images, about X credits", wait for the yes, attach the real product photo as the reference, and never generate the product alone, a person presented as a real customer, a before and after, or an expert. Generated images are listed as such in the handoff.

4. **Capture the whole reference.** The swipe file's screenshot stops at 3,400 pixels; the design needs all of it.
   ```bash
   node <skill>/scripts/lp-screenshot.mjs <reference url> <scratchpad>/ref-desktop.png --desktop --height 11000
   node <skill>/scripts/lp-screenshot.mjs <reference url> <scratchpad>/ref-phone.png --height 14000
   ```
   Read both top to bottom in strips. The desktop layout is usually not the phone layout made wider: two columns in the hero, flanking images in the bands, a gallery beside the buy box.

5. **Write `design-spec.md`** (worked example: For Wellness, `adcrate-for-wellness/workflows/landing-pages/2026-09-30-for-wellness-welcome-kit-offer-lander/design-spec.md`):
   - The reference's visual grammar: type (display face, case, weight, scale), colour roles (ground, band colour, button colour, sticker and badge colours), edges (waves, scallops, stripes), and every component style.
   - A table: each reference block, and the approved section that fills it. Blocks the brand cannot fill honestly (proof it lacks, urgency it may not run) are listed as dropped with the reason, never filled with new copy.
   - The palette and type mapped to the brand, keeping the reference's look as closely as possible (Alex, 2026-10-01: "always uses the templates as the base, and we should make the design look as much like the template as possible. It should be delivered in HTML, not in an artefact."): every component, edge and flourish stays (Grüns's scallops, stripes, hard-shadow cards and pills included), redrawn in the brand's accent hues. Neutrals, grounds, borders and shadows stay the reference's. Type keeps the reference's treatment (weights, case, sizes, tracking); the face is the brand's own font files if they exist, otherwise the closest Google Fonts match to the reference's face. This replaces the 2026-09-30 note that said to swap the reference's motifs for the brand's own.
   - The reference's density. A big account's page carries more sections than a template's minimum: proof, how the subscription works, a stats block, a flavour or variant feature, a creator video wall. Fill each one the brand can fill honestly; the new words go through the copy gates and the chat table before the build.
   Approved lines may be recomposed into the reference's components (a line split into a sticker, a plan note split into bullets, "Choose Cinnamon, Vanilla or Mocha" as three flavour boxes). A block that needs words nobody approved goes back through the copy table.

6. **Write the run's build script** from `<skill>/assets/example-design-build.py`: it reads `page.json` and `brief.json`, holds only layout and CSS, and writes one self-contained HTML file with the photos embedded as data. Recreate the reference's look as closely as possible: measure it from the captures (column widths, image sizes, font sizes, gaps, radii, shadow offsets) and match them; only words, photos, logo and accent hues change. Never fall back to generic blocks or to the artifact-design treatment.
   ```bash
   python3 <run>/build-design.py            # writes <run>/<brand>-<page>.html
   python3 <run>/build-design.py --labels   # the same with S01, S02 ... tags, for review help
   ```
   `lp-build-page.py` stays as a quick structural preview only; its generic look is not the deliverable (Alex, 2026-09-30).
   **Components from 21st.dev: off by default, only when the reviewer asks for them.** Alex tried it on the For Wellness run and then said "i actually prefer the version without the 21st.dev mcp" (2026-09-30), so the hand-built interaction in `assets/example-design-build.py` (selectable plans, a flavour picker that swaps the gallery photo, gallery thumbnails, review tabs) is the default. When asked ("apply elements from their library where necessary... if it actually enhances the overall landing page"): After the page matches the reference, look for real gaps, usually interaction the reference has and a static page lacks: plan cards that select, a variant picker, an FAQ that opens smoothly. Search the 21st.dev MCP (`search`, free), retrieve only the ones that fix a named gap (`get_component`), and port their structure, styling and behaviour into the single HTML file in plain CSS and JS (the deliverable has no React). Keep the reference's look and the brand's palette; never add a component for decoration, and never one that pushes urgency or proof the brand may not run. List what was used and why in the run README. Worked example: the For Wellness build ports Pricing Plan Radio Cards (id 28337), Cuisine Selector Chips (6940) and Animated Line Accordion (27711).

   **Section-by-section recovery mode:** the default remains one full-page build. If two strip-comparison passes fail for the same shared visual reason—wrong type scale, spacing rhythm, component language or first-screen composition—stop rebuilding the whole page. Build and compare the hero plus the next one or two reference blocks, lock the corrected tokens and components in `build-design.py`, then extend that system down the page in reference order. Do not rewrite approved copy, redesign the template or add another human gate. This is a recovery technique for drift, not the normal workflow.

## Check (step 6)

7. **Screenshot desktop first, then the phone.**
   ```bash
   node <skill>/scripts/lp-screenshot.mjs <run>/<brand>-<page>.html <run>/shots/draft-v<N>-desktop.png --desktop --height 9000 --keep-popups
   node <skill>/scripts/lp-screenshot.mjs <run>/<brand>-<page>.html <run>/shots/draft-v<N>-mobile.png --height 8000 --keep-popups
   ```
   Read each beside the matching reference capture. Save the desktop one as a JPEG to send with the file.

8. **Run functional browser QA.**
   ```bash
   node <skill>/scripts/lp-qa.mjs <run>/<brand>-<page>.html \
     --out <run>/qa/qa-v<N>.json --cta-url <cta_url>
   ```
   It opens the actual file at desktop and phone widths and fails on broken or non-embedded assets, empty or mismatched CTA links, missing internal targets, horizontal overflow, console errors, uncaught exceptions, forms with no submit control and safe interactions that do not respond. It records unverified form wiring and missing alt attributes as warnings. Fix the source and rebuild until it passes. The script never follows CTAs or submits forms. Confirm form routing and validation locally; do not send test data to a live endpoint without explicit authority.

9. **Visual and content QA, in this order. Fix the source and rebuild on any miss.**
   - **Looks like the reference, as closely as possible:** run `python3 <skill>/scripts/lp-compare.py <reference.png> <draft.png> <run>/shots/compare-v<N>` for desktop and again for the phone, and read every strip side by side. Same layout, type treatment, spacing, components, edges and rhythm; only words, photos, logo and accent hues differ. A strip that would not pass for the reference with the words blurred is a fail: fix the builder and rebuild.
   - **Words:** every approved line is on the page, unchanged. Nothing extra.
   - **Structure:** sections in template order; each section reads as its job; the hero and its button are visible without scrolling on a phone.
   - **One promise:** the first screen states the angle; when an ad is named, it says what the ad said, with the same offer.
   - **Numbers and placeholders:** every `[OFFER]`, `[STAT NEEDED]` and photo box that remains is intended and highlighted; none hides in small print.
   - **Buttons:** all go to the one link.
   - **Phone fit:** nothing clipped, no sideways scroll, tables scroll inside their own box, the sticky bar does not cover a button.
   - **Working parts:** the quiz advances and reveals its result; the card game flips and unlocks; FAQ items open.
   - **The brand:** the brand's logo, accent hues and real photos. None of the reference brand's words, logo, product, names or photos.

10. **A fault shared by several sections is a builder or contract fault.** Fix it in `scripts/lp-build-page.py` or `templates/INDEX.json` (and log it in `references/feedback-log.md` as a lesson), then rebuild. Do not patch section by section. Section-by-section recovery mode still fixes the shared source; it does not authorize independent one-off patches to each block.

## Lessons (add dated paragraphs here as runs teach them)

- **Always the skill, always a template, as close to the reference as possible, always HTML (2026-10-01, The Perfect Jean runs).** A session in a brand brain was asked to "run the landing page skill", did not find it (it was not installed there), and hand-built a page with the artifact-design treatment and published it as an artifact. Alex: "this is horrific design and nothing like the ones from the templates", then: "always uses the templates as the base, and we should make the design look as much like the template as possible. It should be delivered in HTML, not in an artefact." The skill is now installed for every session (`~/.claude/skills/new-landing-page`), the hard rules forbid a from-scratch page and an artifact delivery, and the look check compares the draft to the reference strip by strip with `lp-compare.py`.

- **Recreate the reference's design, not only its section order (2026-09-30, For Wellness run).** The first draft used the generic builder and followed the Grüns page's structure but none of its look; Alex: "this doesn't look anything like the initial one that I chose." Draft 1 was rebuilt from a full-length capture and a design spec. Always build from the design spec.
- **Web version first (2026-09-30).** Alex reviews on desktop: "I ideally want to see the web version, not the mobile version. You can give me both." Build responsive to the reference's desktop layout, check desktop first, and send a desktop screenshot with the file.
- **Match the reference's level, not just its layout (2026-09-30, For Wellness draft 4).** Draft 2 copied the Grüns structure but reused two photos seven times, borrowed Grüns's candy scallops, used stand-in fonts and carried 8 sections to Grüns's 15. Alex: "it still feels that one is a level above in design." Draft 4 closed it with the brand's own font files, cut-out packshots and lifestyle and ingredient photos from the brain's asset pull, the brand's own visual language, and five extra sections through the gates. Build from the whole asset pull and the reference's full density from the first draft.
- **Deliver an HTML file (2026-09-30).** Alex: "I want this delivered to me as an HTML doc, like an actual landing page, not an artefact." The build embeds the photos so the single file opens anywhere.

- **Images on a published board must be local files (2026-09-30).** A published page cannot load images from another site, so a photo left as an `https://` link shows as a broken image on the board. `lp-board.py` warns when it sees one. Save photos into `assets/`.

- **House builds have a build kit (2026-10-01).** A reference marked `house_build` in `templates/INDEX.json` (first one: `tpj-gruns-1`) is a page Parker built and Alex chose to keep. It has no live URL to capture; start from its `design_kit` folder (`assets/designs/<slug>/`: `build-design.py`, `design-spec.md`, `desktop.jpg`) and the phone screenshot in the swipe file, copy the build script into the run, and swap the accent colours, logo, photos and accent phrases.

- **Mark every button with `data-cta` (2026-10-01, For Wellness tpj-2 run).** `lp-qa.mjs` finds buttons by `a.pill`, a class containing "cta", `data-cta` or `role="button"`. A build whose buttons use another class fails with "no CTA-like links found" even when every link is right. Put `data-cta` on every link to `cta_url` in the run's build script.
