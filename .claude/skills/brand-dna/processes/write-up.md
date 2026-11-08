# Process: write-up (phase 4)

**Accomplishes:** the research moved into the brain's homes, and a one-page Brand DNA export.
**Select when:** `research.md` or `refresh.md` has a finished working file; or the export alone is asked for.
**Inputs:** `audits/<YYYY-MM>/brand-dna-research-<YYYY-MM-DD>.md`; the brain's `sub-context-docs/brand-profile-narrative.md`, `brand-lens.md` and `sub-context-docs/visual-vocabulary.md`.
**Output:** updated `sub-context-docs/brand-profile-narrative.md`, `brand-lens.md`, `sub-context-docs/visual-vocabulary.md`, `competitors/`, `running-notes/missing-context.md`; the export `brand-context/brand-one-pager.md`.

## Steps
1. **Write each fact to its home** (the table in `SKILL.md`), with its label and "(source, date)". Keep what's already there unless the new source is better; when two sources disagree, keep both and flag it
2. **Write the image generation prompt modifier last**, into `sub-context-docs/visual-vocabulary.md`: one paragraph of 50-75 words, prepended to every polished-format image prompt. It names the exact hex colors with their roles, the font descriptions (weight, case, style), the photography direction (light, grading, composition, surfaces) and the mood. Built from the ad style first and the website second. Count the words. It's for polished formats: native and UGC prompts leave it out
3. **Export** `brand-context/brand-one-pager.md` in this exact format, filled from the homes (a view, not a second copy to edit: say so in its first line, with the date):

```
BRAND DNA DOCUMENT
==================
Generated <date> from this brain's brand files. Edit those files, then re-export. <Concept label if not a client>

BRAND OVERVIEW
Name / Tagline / Design Agency / Voice Adjectives [5] / Positioning / Competitive Differentiation

VISUAL SYSTEM
Primary Font / Secondary Font / Primary Color [hex] / Secondary Color [hex] / Accent Color [hex] / Background Colors / CTA Color and Style

PHOTOGRAPHY DIRECTION
Lighting / Color Grading / Composition / Subject Matter / Props and Surfaces / Mood

PRODUCT DETAILS
Physical Description / Label-Logo Placement / Distinctive Features / Packaging System

AD CREATIVE STYLE
Typical formats / Text overlay style / Photo vs illustration / UGC usage / Offer presentation

PROOF INVENTORY (the only source for proof in ads)
Review count / Rating / Customers / Press / Certifications — each with source and date, or "none verified"
Risk reversal: Guarantee / Free shipping (threshold) / Return window / Trial — each with source and date, "statutory" where it's only the legal minimum, or "none verified"

IMAGE GENERATION PROMPT MODIFIER
<the 50-75 word paragraph>
```

Each line keeps its label in brackets where it isn't Verified, e.g. "Secondary Font: heavy geometric sans [Inferred: no CSS name exposed]".

4. **Gaps:** every "not found" that a creative skill will miss goes in `running-notes/missing-context.md`, saying which skill needs it (e.g. "rating: needed by review templates pb-11, pb-17")

## Quality checks
- The modifier is 50-75 words and names at least the primary hex, one font description, the light and the mood
- No field in the export is filled that's empty in its home
- The export's proof inventory matches `brand-lens.md` exactly

## Stop when
The homes and the export agree, and gaps are logged. Then the "what I need from you" list (`SKILL.md`). What usually follows: `static-ads` (dry run or prompt pack), `new-landing-page`, or `persona-gap` mode A if there are no personas yet.
