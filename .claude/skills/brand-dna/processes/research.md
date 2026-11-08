# Process: research (a brand with no DNA yet)

**Accomplishes:** every Brand DNA field found, sourced and labelled, ready for `write-up.md`.
**Select when:** the brain has no prompt modifier or proof inventory. **Not when:** the DNA exists (`refresh.md`).
**Inputs:** brand name, the brand's URL, the lead product (ask once if the brand sells several), any files from the brand.
**Output:** a working file `audits/<YYYY-MM>/brand-dna-research-<YYYY-MM-DD>.md`: every field with its value, source (URL and date) and label. It's the raw research; `write-up.md` moves each fact to its home.

Work as a senior brand strategist reverse-engineering the brand. The output feeds image prompts, so exact specifications beat impressions: a hex code beats "warm red", a measured layout beats "clean".

## Phase 1: external research (web search)
Run each search, open the results that are primary (the brand's own pages, the agency's case study, the brand's press kit) and note what each says:
1. **Design credits:** "who designed [Brand] branding", "[Brand] design agency case study", "[Brand] rebrand"
2. **Public brand assets:** "[Brand] brand guidelines pdf", "[Brand] press kit", "[Brand] media kit", "[Brand] style guide"
3. **Typography:** "[Brand] font", "[Brand] typeface", "what font does [Brand] use"
4. **Colors:** "[Brand] brand colors", "[Brand] hex codes", "[Brand] color palette"
5. **Packaging:** "[Brand] packaging design", "[Brand] unboxing", "[Brand] product photography"
6. **Advertising:** the brand in the Meta Ad Library (country: where it sells; DK for a Danish brand, all countries otherwise): which formats it runs now, the text overlay style, photo vs illustration, UGC, how offers are shown. What exists, never what performs
7. **Press and positioning:** "[Brand] brand story", "[Brand] founding story", "[Brand] mission"

A Danish brand rarely has a public style guide or agency case study: search in Danish too ("[Brand] designbureau", "[Brand] rebranding", "[Brand] historie"), and expect phase 2 to carry most of the visual system.

## Phase 2: on-site analysis (the brand's URL)
Use the built-in browser (or the Chrome extension). Public pages only.
1. **Voice and tone:** read the hero copy, the About page and two or three product descriptions. Five distinct adjectives, each backed by a short quote from the site
2. **Photography style:** lighting, color grading, composition, subject matter, props and surfaces, mood
3. **Typography on site:** read the real fonts, not by eye: `getComputedStyle(document.querySelector('h1')).fontFamily` and the same for body text and buttons, plus `@font-face` and Google Fonts links in the page CSS. Per role: name, weight, case (`text-transform`), letter-spacing, distinctive treatments
4. **Color application:** read the CSS: `getComputedStyle(el).color` / `backgroundColor` for the header, hero, body, buttons and announcement bar. Primary vs accent, background colors, the CTA color and shape (radius, fill or outline)
5. **Layout density:** airy or dense, grid-based or organic, how much white space around the product
6. **Packaging details:** from the product pages and photos: materials, colors, shape, label and logo placement, textures, translucency, matte vs gloss. Write it so an image model can't get the pack wrong: this text is reused in every prompt
7. **Proof the site shows:** review count and rating (with the platform), press logos, certifications, customer counts. Each with the page URL and today's date
8. **Risk reversal:** the promises that take the risk out of buying, from the footer, FAQ, shipping and returns pages: a guarantee (its exact terms), free shipping and its threshold, the return window, a trial period. Each with the page URL and today's date. A right the law already gives every Danish customer (14 days' right of withdrawal, 2 years' reklamationsret) is noted but marked "statutory": an ad may not present it as a perk

## Phase 3: competitive context
Find 2-3 direct competitors (same category, same market and price level; search "[category] [country]" and look at who else advertises in the Ad Library). For each: one line on how they look (palette, photo style, type) and how they position, and one line on what visually separates our brand from them. Save one file per rival from `competitors/<name>/competitor-snapshot.md` when the rival matters beyond this run.

## Quality checks before write-up
- Every field has a value or "not found"; every value has a source and a label
- Hex codes and font names come from CSS or the brand's own files (Verified), or are marked Inferred
- Proof numbers have a URL and a date, or they're not in
- Packaging description is specific enough that two people would draw the same pack

## Stop when
All fields are filled or marked "not found", and the working file is saved. Next: `write-up.md`.
