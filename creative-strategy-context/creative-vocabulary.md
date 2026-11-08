---
summary: "The team's shared words in one home: angle, format, structure, concept, persona, UMP and UMS, awareness and sophistication codes, funnel, native ad, pre-sell page, and the breakdown frameworks, mapped to tags and brain files."
---

# Creative vocabulary

**Source:** a practitioner's post on shared team vocabulary, a set of ad breakdown prompts and a study of 100 winning scripts, all handed in by the team on 7 Nov 2026. Authors not credited by the owner's choice.
**Users:** the whole team, all brands. Read by `ad-breakdown`, `angle-bank`, `creative-leaderboard`, `scriptwriting`, `persona-gap` and anyone writing a brief.
**Status:** working definitions. The words come from the sources (*Stated*); where the factory already used a word, this doc follows the factory and says so. Not a ruling on craft: it says what we mean when we say a word.

This is the one home for the words. Other docs point here. Where another doc already explains a word in depth, this doc gives one line and the pointer.

## The core words

### Angle
The reason to buy that you lead with. It targets one problem, one desire or one belief. Two angles for the same hair serum: "no side effects" and "hair back before the wedding". If it takes a paragraph to explain, it is not an angle yet. How to find them: `angle-discovery.md`. Where they are stored: `angle-bank/angles.csv`, one row per angle, `angle_id` `A01`...

### Format
What the ad looks like: AI animation, podcast clip, B-roll VSL, creator to camera, a static with a benefit headline. Our format values are fixed in the tag schema (`format` below). The format catalogue lives in `ad-formats/`.

### Structure
The order of the parts in the script or the copy: hook, problem, failed solution, mechanism, proof, offer, call to action. Two tools name a structure: the **shape** (one of the five patterns in `winning-script-patterns.md`) and the **ladder step** it opens on (`awareness-script-ladder.md`).

### Concept
The full ad idea: **concept = angle + format + structure.** Change any one of the three and it is a new concept, not a variation of the old one.

How this meets the brain's concept register (`idea-bank/concepts.md`): the register files a concept by persona, angle and offer, because that is what results are read by, and lists the formats made under one ID. So `concept_id` follows the register, and a change of format or structure is recorded in the ad's `format` and `shape` tags, not with a new ID. Read together, concept_id + format + shape is the full concept in the sense above; count it that way when you count creative diversity (`andromeda-v2.md`).

### Avatar
The audience as a whole: the people who have the problem ("men losing their hair"). In a brain the avatar is the brand's buyer as set in `brand-lens.md` and the top of `personas/personas-profile.md`.

### Persona
One specific version of the avatar: same problem, different situation and motivation. Inside "men losing their hair": the man who marries next year and wants hair in the photos, and the man who stopped a medicine because of the side effects. Each needs a different angle. Personas are built from evidence by `persona-gap` Mode A and stored in `personas/personas-profile.md`; `persona_id` is `P1`, `P2`... in that file's order.

### Mechanism: UMP and UMS
The reason the product works, in two halves:
- **UMP, the unique mechanism of the problem:** the root cause, the real reason the problem exists and the old fixes failed. It moves the blame off the viewer.
- **UMS, the unique mechanism of the solution:** how the product fixes that exact cause.

A good UMS is the opposite of the UMP: the old fix failed for a reason, the new one works for the opposite reason. This is the meaning `scriptwriting.md` already uses (VSL structure and "The Million-Dollar Mechanism"); the VSL build is in `.claude/skills/scriptwriting/processes/build-vsl-mechanism.md`. A USP is different: a feature only you have, which may or may not explain why it works.

### Enemy
The specific thing blamed for the viewer's problem, usually what they use now instead of you: the cheap copy, the cream they rely on, the old pillow. Specific beats vague: name the thing, not "bad ingredients". An enemy without a mechanism gets agreement and no sale. Patterns and numbers: `winning-script-patterns.md`. The yapper villain (`yapper-ads.md`) is close kin: the villain is who or what made them feel the pain; often it is the same thing.

### Awareness level
How much someone knows about the problem and the solutions (Eugene Schwartz). Our codes:

| Code | Level | What they know |
|---|---|---|
| `UN` | Unaware | Don't know they have the problem, or don't link a symptom to it |
| `PA` | Problem aware | Feel the problem; don't know what kind of fix exists or which works |
| `SA` | Solution aware | Know the kind of fix; don't know your product, or why it beats the rest |
| `PR` | Product aware | Know your product; not yet convinced |
| `MA` | Most aware | Know it and want it; waiting for the deal or the moment |

What to write at each level: `scriptwriting.md`, "Writing for different stages of awareness". Which step to open on: `awareness-script-ladder.md`.

### Sophistication level
How many similar claims the market has already heard (Schwartz). It is read for the category, not for one person. What an ad must do at each level:

| Code | Market | What the ad must do |
|---|---|---|
| `S1` | First with the claim | Say the claim plainly. Nobody has heard it |
| `S2` | Others make the same claim | Make the claim bigger or more specific: faster, more, a number |
| `S3` | The claims have stopped working | Bring a mechanism: say how it works |
| `S4` | Rivals copy the mechanism | Make the mechanism better, easier or better proved |
| `S5` | Nobody believes claims any more | Lead with the viewer's own experience and a fresh root cause (UMP), not a promise |

`scriptwriting.md` uses Stage 3-5 for the same scale (VSL section). The "high" and "low" sophistication in `problem-solution-headline-writer.md` and `iterations.md` map roughly to S4-S5 and S1-S2 (*Inferred*).

### Funnel stage
Who the ad was **delivered to**: `TOF` (cold, never met the brand), `MOF` (engaged: visited, watched, followed), `BOF` (warm: added to cart, checked out, existing customers). It is a fact about delivery, not about the ad. Awareness is what the ad assumes the viewer knows (`persona-research-and-creative-strategy-process.md`, step 5). Two separate axes: a product-aware ad is not a BOF ad.

**Never derive the funnel stage from the awareness level.** In a broad campaign Meta reads the ad itself to decide who sees it, so a product-aware mechanism ad can be the account's biggest cold ad (`angle-discovery.md`, "Product-aware angles run cold"). Read it, don't guess it:
- **Our account:** the audience-segment breakdown (new, engaged, existing customers) where the campaign has it, else the ad set's targeting and exclusions. Label *Seen*
- **Someone else's ads (Ad Library, a competitor):** delivery can't be seen. The tag is `x`

The tag table's home is `.claude/skills/persona-gap/SKILL.md` (Mode B).

### Native ad
Two meanings. Say which one you mean.
1. **On Meta:** an ad built to pass as a post: long primary text, often in advertorial style, with a raw or organic-looking image. Our format tag: `static-native`.
2. **Native ad networks:** Taboola, Outbrain, MediaGo and similar, which place ads as recommended articles on publisher sites.

### Landing page and pre-sell page
- **Landing page:** any first page after the ad click: product page, collection, offer page, pre-sell page, quiz.
- **Pre-sell page:** a page between the ad and the product or offer page that teaches and persuades first: a listicle, an advertorial, a quiz. Built by `new-landing-page`.
- **"Pre-lander":** we don't use the word. What people mean by it is a pre-sell page.

## Words used in ad breakdowns

Short working definitions of the frameworks `ad-breakdown` names. Each one is a lens, not a score.

### LF8 (Life Force 8)
Eight built-in desires (Drew Whitman): survival and longer life; food and drink; freedom from fear, pain and danger; sexual companionship; comfortable living; being superior and keeping up with others; care and protection of loved ones; social approval. A breakdown names the primary one and at most one secondary. Full list with notes: `killer-performance-ads.md`, "Emotions and Triggers".

### NESB
Four things a strong idea feels like: **New** (not heard before), **Easy** (simple to do and to understand), **Safe** (low risk, credible), **Big** (a result worth the trouble). A breakdown asks which of the four the ad carries and which one is missing.

### Positioning archetypes
Who the speaker is to the viewer:
- **Friend / Convert:** a peer who had the problem and doubted the fix until it worked for them. Trust comes from sameness.
- **Authority:** an expert. Trust comes from knowledge.
- **Hybrid:** both at once, such as an expert who had the problem herself.

Our `voice` tag records who talks; the archetype says how they win trust. A `creator` or `customer` is usually Friend, an `expert` Authority, a `founder` either.

### Trigger event
The moment a need becomes conscious; in reviews, the moment the problem stopped being private, usually because someone else noticed. How to find it: `customer-review-mining-method.md`. The hook built on it: `hooks.md` #22. As a buying phase (Trigger in T-E-E-P): `emotional-delivery-and-timing.md`.

### Belief transfer
The chain of beliefs a viewer must hold before buying, and how the ad moves each one from what they believe now, one link at a time. Objection handling is belief transfer aimed at the doubts. A static does it in one frame, through implication, side-by-side contrast, proof or a reframe.

### Proof of mechanism
Evidence that the mechanism is real: a demo of the cause, a visual, a test, a study, a before and after of the cause rather than the result. The breakdown prompts call this "unique mechanism of proof" and shorten it to UMP, which clashes with our UMP (the problem's root cause), so we say "proof of mechanism" and never shorten it.

### Emotional valence and intensity
- **Valence:** the direction of the feeling, toward something good or away from something bad, and how it shifts across the ad.
- **Intensity:** how strong it is, 1-10 at the peak, and its arc over time.
- **Calibration:** intensity should fit the viewer. A restrained 4/10 can read as credible to a sceptic in a crowded market; a 9/10 can break the inertia of people who have lived with the pain for years. Over-agitate and it reads as manipulation; under-agitate and nothing moves.

The two-dial model and its four zones: `hook-psychology.md` #11. The landing state and the buying phase: `emotional-delivery-and-timing.md`.

### Benefit stacking
Laying several benefits one after another so the value adds up: usually the main benefit first, then the ones that remove the remaining reasons to wait. The breakdown names which benefits, in what order, and which were left out. A static has room for two or three.

## How the words map to tags and brain files

The tag schema is shared by `ad-breakdown` (writes it), `angle-bank` (stores it) and `creative-leaderboard` (reads it from ad names). The naming convention's home is `brain-system/system/ad-naming-convention.md`.

| Word | Tag field | Where it lives in the brain |
|---|---|---|
| Concept | `concept_id` (`C07`) | `idea-bank/concepts.md` |
| Angle | `angle_id` (`A03`) | `angle-bank/angles.csv` |
| Persona | `persona_id` (`P2`) | `personas/personas-profile.md`, in its order |
| Avatar | none | `brand-lens.md`, top of the personas profile |
| Awareness level | `awareness` (`UN` `PA` `SA` `PR` `MA`) | `angles.csv` (`awareness`), `angle-bank/ad-tags.csv` |
| Sophistication level | `sophistication` (`S1`-`S5`) | breakdowns only, `audits/breakdowns/` |
| Format | `format` | `ad-tags.csv` |
| Structure | `shape` and `ladder_start` | `ad-tags.csv`, breakdowns |
| Enemy | `enemy` | `angles.csv` (`enemy`), `ad-tags.csv` |
| UMP and UMS | `mechanism` (`yes`/`no`) | `angles.csv` (`ump`, `ums`) |
| Who talks | `voice` | `ad-tags.csv` |
| Hook family | `hook_family` | `ad-tags.csv` |
| Proof | `proof` | `ad-tags.csv`; what may be claimed: proof inventory in `brand-lens.md` |
| Close | `close` | `ad-tags.csv` |
| Funnel stage | `funnel` (*Seen* from delivery on our account, else `x`; never from awareness) | breakdowns, `persona-gap` sheets |

Unknown is always `x`. A value never contains `_` (use `-`).

## Where our docs use a word differently

Known differences, so nobody trips on them. Until a doc is changed, this list says which reading wins.

- **Concept.** Settled (v20): `idea-bank/concepts.md` decides `concept_id` (persona x angle x offer); format and shape are tags. See Concept above.
- **UMP.** Settled (v20): UMP is the root cause of the problem and UMS is how the product fixes it. `build-vsl-mechanism.md` now calls its category claim the "mechanism position".
- **New angle as an iteration.** `iterations.md` (optimisation hierarchy, level 2) calls a new angle inside the same theme an iteration. Here, and in the register, a new angle is a new concept. `iterations.md` is about which lever to pull on a winner, and that advice still stands; only the counting differs.
- **High and low sophistication.** The headline docs use two levels; breakdowns use S1-S5. Mapping above.
