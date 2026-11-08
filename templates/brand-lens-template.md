# Brand lens template

> Status: `[~]` template. This is the canonical scaffold for a brand's lens overlay, instantiated per brand at `brand-lens.md`, at the brand brain's root. The scaffold (`scripts/scaffold-brain.py`) seeds it when the brain is set up, every slot replaced with "Not captured yet."; the build's "Stamp the operating contract" step fills it; the refresh and self-improve routines keep adding to it. Fill the `{{slots}}`, delete this header block, and keep every line sourced and dated.
>
> **What this file is for.** The creative-strategy method docs teach how a strategist thinks in general. This lens is the one place that says how *this* brand is different — the tribal knowledge the team has handed over that no general method could know. The expertise layer loads it on top of the method docs on every creative output (the expertise-core block names it), so it is the highest-leverage way the brand's own knowledge keeps shaping the work after onboarding. **When the lens and a general method disagree, the lens wins** — it is the brand speaking. Keep it tight and true: a short lens of verified brand rules beats a long one padded with guesses.

---

# {{BRAND_NAME}} — brand lens

The standing overlay of {{BRAND_NAME}}'s own knowledge. Loaded on top of the general creative-strategy method on every creative-strategy output. Where a line here conflicts with a generic rule, this line governs. Every entry carries its source and date and is marked **stated** (the brand told us, not yet independently checked) or **verified** (observed directly in their data, creative, or a confirmed correction). Add to this file whenever the brand teaches the assistant something durable — a correction, a constraint, a preference, a what-worked — rather than letting it evaporate into a single conversation.

## Voice and language

{{How this brand sounds and the words it does and does not use — required terms, banned terms, tone rules, naming conventions for the product and the customer. Pull from brand-provided voice guidance and from the brand's own best-performing copy. Each line sourced and dated, stated or verified. Leave a labeled "nothing captured yet" line if empty so the section is visibly open, not forgotten.}}

## Claims and compliance constraints

{{Hard limits on what can be said — regulated claims, substantiation requirements, legal or category gates, comparative-claim rules. A hard rule here outranks craft. If the brand has none, say so explicitly; do not infer constraints they did not state.}}

### Food, supplements and anything eaten or drunk (EU law)

Delete this subsection for brands that sell nothing edible. For supplements it is the strictest limit on the copy, and US examples (courses, swipes, competitor ads) routinely break it.

- **No disease claims.** Copy may not say or suggest that the product prevents, treats or cures a disease, or refer to such properties (Regulation (EU) 1169/2011, art. 7(3)). Naming a disease as the enemy the product fights counts
- **Health claims only from the EU register,** for the ingredient and dose the product actually has, with its conditions of use, worded close to the authorised text (Regulation (EC) 1924/2006; the EU Register of nutrition and health claims). No claim in the register: no claim
- **Never** (1924/2006, art. 12): suggesting health suffers if you don't take it; the rate or amount of weight loss; recommendations from individual doctors or health professionals
- **The brand's authorised claims,** each with its register entry, so copy and `brief-check` check against a list instead of judging case by case:
- **Unsure:** it doesn't run. Mark it "ask the brand / check the national food authority's guidance" and add it to `running-notes/missing-context.md`

Checked against EUR-Lex on 2026-09-29. Other markets (the US and the FTC, for example) differ: this subsection covers ads shown in the EU.

## Proof inventory

The only source for proof in ads and pages. Every review count, rating, customer number, press logo, certification, award, study and guarantee that an ad, prompt pack or landing page shows comes from this table and nowhere else. No source and date: it isn't here, and the ad drops that element. `brand-dna` fills it; the offer brief's risk reversal is built from its guarantee row.

| Proof | Value | Source (URL or file) | Read on | Label |
|---|---|---|---|---|
| Review count and platform | | | | |
| Average rating | | | | |
| Customers / units sold | | | | |
| Press mentions | | | | |
| Certifications, awards | | | | |
| Studies (what was measured, by whom) | | | | |
| Guarantee and risk reversal (terms) | | | | |

## Market sophistication

{{Where the category is, stage 1-5, with one line of evidence from competitors' live ads and the date it was checked. 1: first on the market, the plain claim works. 2: others make the same claim, so make it bigger or more specific. 3: claims are worn out, show the mechanism. 4: rivals have mechanisms too, show a better or newer one. 5: nobody believes claims any more, sell identity and experience. Name the claims that are worn out. The copy guide, headlines, scriptwriting and the offer brief read this before writing.}}

## Do's and don'ts

{{The brand's standing creative preferences and prohibitions that aren't legal — formats they love or refuse, creators or talent profiles they want or won't use, visual or messaging territory they own or avoid, things that have burned them before. Sourced and dated.}}

## What has worked and what has failed

{{The brand's own track record as they've told it to us or as the account verifies — angles, hooks, offers, formats, audiences that won or lost, with the evidence and date. This is the brand-specific complement to the general method; it is why a play that's textbook-correct might still be wrong here.}}

## Positioning and audience nuances

{{Where this brand's positioning, buyer, or category reality diverges from the obvious read — a served audience that isn't the real buyer, a price/stage/business-model fact that changes the playbook, a strategic stance the team holds. Tie to the brand-profile and persona docs where they corroborate.}}

## Named preferences and standing instructions

{{Specific, durable instructions the team has given about how they want the assistant to work for them — defaults to assume, things to always flag, people whose sign-off matters, recurring asks. The catch-all for tribal knowledge that doesn't fit above.}}

---

*Sources: list the brand-provided docs, conversations, corrections, and verified observations behind the entries above, each with its date and surface, per `brain-system/system/refresh-cadence.md` and the attribution rules in `CLAUDE.md`.*
