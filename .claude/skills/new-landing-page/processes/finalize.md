# Process: the final page (step 9)

Goal: the approved page handed off so someone can put it live without asking what is left.

Runs only after the reviewer has approved a draft in chat (or on a board, if one was used).

## Steps

1. **Freeze and verify the page.** `lp-copy.py collect` and `check` one last time on the approved `page.json`. Build the clean page (`lp-build-page.py <run>`), screenshot it (`shots/final.png`, then a JPEG copy for decks and Slack), and run `lp-qa.mjs` one last time to `qa/final.json` with the approved `cta_url`. Do not finalize on a failed report.

2. **Send the final HTML file** (SendUserFile, `display: attach`). It is self-contained, so it is the file to hand over; `design-spec.md` and `page.json` go with it for whoever rebuilds it in the store's page builder.

3. **Write the run `README.md`:**
   - What was built: brand, template, reference page, the angle, the ad it is matched to if one was named (with the Parker and media links), drafts taken, date approved.
   - **The handoff list**, the part the next person needs:
     - every open placeholder (`[OFFER]`, `[STAT NEEDED]`, codes, dates) and who can fill it;
     - every photo still needed, with what it should show; any generated image, marked as generated;
     - the button link, and whether the offer is applied by the link or needs a code;
     - the final browser-QA result and report path; any warning that remains and why it is safe;
     - any temporary review URL, its provider and whether it should be removed after handoff;
     - claims that need the brand's sign-off before going live (health and efficacy lines, rival comparisons and their dates);
     - build notes: the page is a single self-contained HTML file; to rebuild it in Shopify, Replo or another page builder, use `page.json` as the section-by-section spec (section order, copy, which component each section is) and the screenshot as the visual target; interactive sections (quiz, card game) need the builder's own equivalent;
     - what to watch once live: if an ad was named, message match with it and the offer staying in step with its offer; pulling the page when a sale ends.
   - The three receipt blocks: **Brand Context Applied**, **Grounding Review**, **Voice Review** (from `copy/notes.md`, updated for any revision).
   - The final file's path.

4. **Figma copy, when asked** (Alex, 2026-09-30: "what if you use the figma mcp to build this instead?", then yes to mirroring). The HTML stays the live page; Figma is the editable design and handoff copy. With the Figma MCP: load its `figma-use`, `figma-generate-design` and `figma-create-new-file` skill resources; `whoami` for the team; `create_new_file`; build local components first (pill button, check item, gift tile with an INSTANCE_SWAP icon, review, FAQ row), then a `Desktop · 1440` and a `Mobile · 390` frame as editable auto-layout sections with copy from `page.json`, image frames named `img/...`; fill them with `upload_assets` (curl POST of the run's `assets/`); clear default white fills on layout containers; read back types, fonts and image frames; one screenshot per frame. Never place a full-page screenshot in the file. Worked example: For Wellness, https://www.figma.com/design/YfbQqfJOqtYmkqAJWiSb3B.

5. **Close the loop.** Run `apply-feedback.md` once more for any template or skill notes left during the run, so the next run starts from them.

6. **Deliver.** The file first, then a short chat summary with the handoff list and a Sources list. Leave syncing to Parker Desktop; do not run git in a brand's brain.

## Never

- Call the page finished while the check fails.
- Hide an open placeholder. If `[OFFER]` is still on the page, the summary says so in its first lines.
- Push the page to a live store, a page builder or a production domain. A temporary review URL is allowed only when the reviewer asks for it; putting the page live is still the brand's step.
