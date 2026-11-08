---
name: brand-dna
description: Reverse-engineer a brand's visual and verbal identity into its brand brain (brand DNA, brand research, brand intake, visual identity, brand colors and fonts, image prompt modifier). Researches design credits, guidelines, fonts, hex colors, packaging, photography, ads, positioning and 2-3 competitors, then writes each fact into its home in the brain, with source and label, and exports a one-page Brand DNA document with a 50-75 word image generation prompt modifier. Use when a new brand brain needs its foundation, before the first static ads, prompt pack or landing page, or when someone asks for a brand DNA, brand research or "how does this brand look and sound".
---

# Brand DNA

One job: turn a brand's public identity (and whatever the brand gives us) into the brain facts every creative skill reads, so prompts, copy and pages match the brand instead of a model's default.

Always run inside the brand's brain folder (made from the factory's `templates/brand-scaffold/`). The method comes from two sources: the lead strategist's Master Brand Research Prompt (the research phases and the output format, 2026) and Alex Cooper's brand-intake reference in his static-ad engine (Parker course, used with permission: source order, the messaging half, refresh only the deltas).

## Files

| File | Answers |
|---|---|
| `SKILL.md` (this file) | What the job is, where every fact goes, what must never happen |
| `strategy.md` | Which process to run |
| `processes/research.md` | A brand with no DNA yet: the full research, phases 1-3 |
| `processes/write-up.md` | Phase 4: writing into the brain and exporting the one-pager |
| `processes/refresh.md` | A brand that already has DNA: check, then update only what changed |
| `feedback.md` | What we've learned running it. A log |

## Where each fact lives (one home each)

The export (`brand-context/brand-one-pager.md`) is a generated view. The facts live here, and edits go here:

| Brand DNA field | Home in the brain |
|---|---|
| Name, tagline, design agency, positioning, mechanism, products and prices, offer | `sub-context-docs/brand-profile-narrative.md` |
| Voice: five adjectives, example sentences, always/never | `brand-lens.md`, "Voice" |
| Proof: review count, rating, customers, press, certifications, studies | `brand-lens.md`, "Proof inventory" |
| Risk reversal: guarantee, free shipping and its threshold, return window, trial period | `brand-lens.md`, "Proof inventory", "Risk reversal" |
| Claim boundaries | `brand-lens.md`, "Claims gate" |
| Fonts, hex colors, backgrounds, CTA color and style, layout density | `sub-context-docs/visual-vocabulary.md`, "Colors and type" |
| Photography direction | `sub-context-docs/visual-vocabulary.md`, "Photography direction" |
| Product physical description, label and logo placement, packaging system | `sub-context-docs/visual-vocabulary.md`, "What the product physically looks like" |
| Ad creative style (formats, text overlay, photo vs illustration, UGC, offer presentation) | `sub-context-docs/visual-vocabulary.md`, "Ad style" |
| Image generation prompt modifier | `sub-context-docs/visual-vocabulary.md`, "Image generation prompt modifier" |
| Competitive differentiation, 2-3 rivals | `sub-context-docs/competitive-landscape.md`, one file per rival |
| Objections, awareness map | `personas/` (only from real customer language; otherwise `running-notes/missing-context.md`) |
| What couldn't be found | `running-notes/missing-context.md` |


## Ground rules

- **Label every field** with the brain's labels: Verified (seen directly: the site's CSS, the pack, the brand's own page), Stated (the source says it: a press article, the brand's About page about itself), Inferred (reasoned: name what it rests on), Data-limited. A hex code read from the site's CSS is Verified; one sampled from a photo is Inferred
- **Invent nothing.** No agency, font, hex or number without a source. Not found means "not found", and a line in `running-notes/missing-context.md`. A font described by eye is written as a description ("heavy geometric sans, likely X"), never as a name stated as fact
- **The brand's own materials win.** Guidelines, a press kit or files from the brand outrank anything researched. Researched facts that conflict with them are flagged, not merged
- **Ads show what exists, not what works.** The Meta Ad Library shows formats and styles, never performance (no spend or results). Never rank or call an ad a winner from it
- **Proof inventory is a wall.** Only numbers with a source and date go in. Every static ad, prompt pack and landing page takes its proof from this list and nowhere else
- **Concept work is labeled.** For a brand that isn't a client, the brain's `CLAUDE.md` says so and the export says it at the top
- **Public pages only.** No logging in, no forms, no buying. Fonts found on a site are licensed: note the name and where it's served from; never copy the font files out of the brain

## After the run

End with "what I need from you": brand files that would replace Inferred fields (guidelines, logo files, product photos for `assets/`), and anything Data-limited that matters for the next skill. Log what the run taught us in `feedback.md` here (general) or the brain's `running-notes/feedback.md` (brand-specific).
