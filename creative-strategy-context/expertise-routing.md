# Expertise routing — which creative-strategy-context docs each doc type loads

> Status: `[~]` drafted 2026-06-11 from the strategist's correction: generated docs followed process without loading the domain expertise, so the analysis read as generic-AI rather than strategist-led. This map names the required creative-strategy-context reads per doc family. The synced expertise core block in every generating prompt points here. The reads are mandatory before analysis, not optional references — the analysis is performed *through* these methods, in their vocabulary.

Paths are relative to `creative-strategy-context/` in whichever tree is running (the factory root, or `brain-system/` inside a brand brain). Where a brand lens exists (`brand-lens.md` at the brand brain's root), load it after the generic docs — it bends the rules for this brand.

## The doc catalog — what exists, so you can reason over all of it

This is the catalog of every creative-strategy method doc and an honest line on what each one *is*. It is deliberately **descriptive, not prescriptive** — it does not tell you when to pull a doc or what it's related to, because those are guesses that go stale and quietly cap what you'd consider. Relevance is *your* call as the planner: read the catalog, hold the task in mind, and reason like a strategist about which docs would genuinely help — generously, biased toward pulling more. It is generated from each doc's `summary` frontmatter by `scripts/build-doc-map.py`, so it stays honest as the corpus grows. (The sections further down are keyed to *build tasks*, when you already know which doc you're generating; this catalog is for when someone just asks a question.)

How to use it:

- **Reason over the whole set, generously.** Don't match a label — look at what each doc actually is and pull everything that would make the answer better. A real question usually wants several, often across areas (a hook question that's really about a persona's emotional state pulls hooks *and* the persona and emotional-delivery docs). There's no quota and no cap; under-retrieval is the failure mode.
- **The catalog is a starting point, not the boundary.** A one-line summary can't capture everything in a doc. When the task is gray, novel, or specific, grep the actual doc bodies across `creative-strategy-context/` for the question's concepts and open what surfaces — the docs' own words find what a summary didn't mention.
- **An opened doc beats an assumption.** If you're unsure whether a doc is relevant, open it and look; the cost of reading one more is small, the cost of a generic answer is not.

Many of these docs end with a required sign-off line ("This is everything I know about X"). That stamp is a proof-of-read: if you used a doc, its sign-off must appear. A missing sign-off on a doc the question clearly needed is a tell that you skipped the read.

**Not reasoning docs — never pull these for analysis:** `expertise-routing.md` (this catalog), `brand-brain-CLAUDE-template.md` (a copy of the operating contract). They live in the folder but carry no method.

<!-- DOC-MAP:START -->
| Doc | What it is |
|---|---|
| `ad-account-analysis.md` | How to read own ad-account data — the two kinds of metrics and what the numbers actually mean for creative decisions. Includes the breakdown effect, attribution settings with dated 2026 platform changes (link-click-only click attribution, incremental attribution + cost caps), when spend deserves trust as the primary signal, and the outside-account 'what changed?' diagnostic for sudden performance swings. |
| `ad-metrics-glossary.md` | Plain-language definitions of the Meta ad metrics the assistant reads — what each measures, how it's calculated, and how to read it in the account, organized by category. |
| `adapting-scripts.md` | The method for adapting an existing video or script (such as a breakout organic) into a new ad — the why-viral comment check and seamless product-slot test that gate the choice, then the segment-faithful structural recreation process. |
| `advertising-luxury-and-higher-price-points.md` | Luxury vs high-priced as two axes (status and identity vs cost against the category), the constraints luxury brands impose, price-objection handling above the category average, what luxury creative looks like, and how to tell which applies. |
| `advertising-to-older-audiences.md` | How to build creative for older audiences (roughly 50–70) on paid social — the mental model behind the demographic and the messaging, pacing, hooks, visuals, tone, authority, social-proof, and format patterns that tend to win, plus the common misreads that sink them. |
| `ai-animation-prompting.md` | Prompting method for AI-animated ad assets — how animation prompting differs from static image and Veo-style video prompting. |
| `ai-drama-ads.md` | AI drama ads: long-form scripted soap-opera stories (1-3 min) made entirely with AI characters, where the product is the plot's secret or reveal. What the format is, why it holds attention, story shapes, the product's role, cast and compliance rules, cutdowns, and when it fits a brand. |
| `ai-static-ad-generation.md` | How to generate AI static image ads — prompt construction for static creative. |
| `ai-writing-tells.md` | The written AI-slop signs — vocabulary, rhetoric, and formatting tells that mark generated copy — and the lint-then-judge review every creative deliverable passes before it ships. |
| `algospeak.md` | Algospeak and platform content policy — the coded language creators use to get sensitive topics past moderation, how enforcement differs across TikTok and Meta, category playbooks for cannabis/CBD, adult wellness, harm reduction and mental health, crypto, and body image / sex ed, and the compliance guardrails that keep a brand's account alive. |
| `analyzing-public-ad-accounts.md` | How to analyze public ad accounts — impression-rank as a proxy, volume/recency/variant reading, and the library-vs-live-spend distinction. |
| `andromeda-v2.md` | How Meta's 2026 delivery and creative-diversity system (Andromeda v2) behaves, so delivery patterns read as auction mechanics rather than mysteries. |
| `angle-discovery.md` | How to find net-new angles: mine the market, not the Ad Library; one-line angles tagged by persona and awareness; read 90 days of winners; map and rank empty cells; test on proven formats; close the loop by name. |
| `awareness-script-ladder.md` | The 11-step awareness ladder: which step a script opens on per awareness level (UN 1, PA 3, SA 5, PR 7, MA 9), what each step must do, which script shape fits each entry, how statics compress it, with a worked example. |
| `black-friday-and-q4-data.md` | Cross-brand Meta data on Black Friday and Q4 (432 brands, Q4 2025): CPMs by week, hit rates, when sale ads ran, winner speed, new ideas vs new takes, deals, what won BF week, the audience shift, statics vs video, openers. Caveats, this year's calendar under Danish price rules, picking a seasonal swipe file. |
| `creative-consumption-analysis.md` | The per-persona method for characterizing the organic content a persona already watches — creator type, production level, setting, delivery, format — then reverse-engineering that native aesthetic into a casting and production brief so ads blend in to stand out. |
| `creative-strategy-by-brand-size.md` | How creative strategy shifts with spend (~$10k, $50k, $1m a month): shots on goal and angles, founder ads and new audiences, big net-new swings and persona unlocks; and who makes the ads at each level (founder, strategist, agency, more creative sources). |
| `creative-strategy-fundamentals.md` | The senior-strategist priors — confidence before speed, the kill-list discipline, where curiosity tends to land, the trying-too-hard failure modes. |
| `creative-vocabulary.md` | The team's shared words in one home: angle, format, structure, concept, persona, UMP and UMS, awareness and sophistication codes, funnel, native ad, pre-sell page, and the breakdown frameworks, mapped to tags and brain files. |
| `creative-volume.md` | How many ads a brand needs per month and how to split the effort: winners remade, iterations, new concepts, and cost per asset against margin per ad. |
| `creator-briefs.md` | Writing creator briefs: freestyle vs director briefs, the talent gate (most creators need a script), more freedom for authorities, scripts for regulated products, script the hook only, first-frame detail, clear references, shared terms, story structure, and finding creators who can yap. |
| `customer-review-mining-method.md` | How to mine customer reviews and comments for creative material — golden nuggets, denominators, theme rates, the qualifying signals (metaphors, insider if-you-know-you-know phrases, trigger events, transformations), and the whole-review concept including the review-as-primary-text play. |
| `emotional-delivery-and-timing.md` | The emotional landing state beneath hooks — valence/intensity and the TEEP buying phase (Trigger, Exploration, Evaluation, Purchase). |
| `gifting-and-q4-creative.md` | Gifting-season and Q4 creative: the gift buyer is not the user, depth over breadth into peak, the gifting journey, a suggested Q4 phase model into Q1 prep, pre-season months as signal not ROAS, the adaptation ladder from evergreen to sale creative, and offer honesty. |
| `hook-psychology.md` | The cognitive science beneath hooks — the mechanisms (notice, qualify, intrigue, reassure, move, transport) that explain why a hook works. The why-layer under the format taxonomy. |
| `hooks.md` | The reference taxonomy of hook formats with real examples — the named formats and what each one is. |
| `ideation-and-brainstorming.md` | How a senior creative strategist generates ideas and plans a creative round — the always-on capture posture and the spark, the structured weekly hunt (hunt brief, cold pass, lanes, merge), sizing the sprint, splitting it across SKUs and personas, and mapping concepts; the reasoning the idea bank, sprint plan, and briefs operationalize. |
| `iterations.md` | The doctrine for making iterations on a winning ad — what to hold fixed and what to vary. |
| `killer-performance-ads.md` | What a genuinely great performance ad looks like — the bar that creative and opportunities get graded against. Carries the full ugly-ads doctrine: what ugly actually means (mimicking the customer's organic feed), the fake-ugly tells, first-frame believability and setting-as-relevance, the barbell rule (super ugly or super obvious ad — the middle dies), and the AI-replication moat. |
| `legal-ai-ugc.md` | Disclosure rules for AI-generated people in ads: the principle (label synthetic humans, not AI products or backgrounds), the EU AI Act's deepfake label (art. 50, since 2 Aug 2026) as it binds a Danish brand, the Danish likeness proposal, and New York's S.8420-A. Not legal advice. |
| `lifestyle-headline-generator.md` | How to write effective headlines for lifestyle brands. |
| `lifestyle-video-ad-formats.md` | The library of video ad formats for lifestyle-positioned brands. |
| `measurement-and-attribution.md` | Reading DTC numbers when tools disagree: store as truth, survey, holdout tests, incremental CPA. |
| `meta-creative-playbook.md` | Meta's own 2026 creative guidance (Creative Shop): the ad-set format mix and Meta's lift numbers, Reels essentials, static-as-billboard, the motivators method with white-space maps, creator diversity and briefs, remixing for volume, Advantage+ generative AI, and where it differs from practitioner doctrine. |
| `meta-full-funnel-cbo-playbook.md` | A Danish step-by-step Meta playbook for one full-funnel CBO setup with 7DC attribution in three parts (TOF Old Winners, BOF Retargeting, TOF new creative): exclusions, spend limits and a launch checklist. From one practitioner's post, not yet tested on our accounts. |
| `new-product-launches.md` | Launch creative for an established brand's new product or SKU: what counts as new, the Step Zero classifier, three launch scenarios (depth, bridge-and-expand, audience expansion), where brand authority transfers, awareness and proof strategy, and per-format specs. |
| `new-sku-launch.md` | Launching a new SKU into an existing catalog (colorway, flavor, format, bundle, spinoff) — the Scenario A/B case of the launch method, which lives in full in new-product-launches.md. |
| `non-problem-solution-creative.md` | Creative strategy for non-problem-solution brands — products bought for transformation, emotion, and belonging rather than to fix a pain. Why agitation misfires here, what to sell instead (the feeling, the experience, disruptor status), and the reaction- and story-led formats that carry it. |
| `offer-design.md` | Building the offer itself: value levers, bundles, guarantees beyond the law, true urgency. |
| `organic-social-analysis.md` | How to analyze organic social through a creative-strategy lens. |
| `persona-research-and-creative-strategy-process.md` | The identity-first persona process — served-vs-buyer, the diagnosis, confidence scaled to the data available, the persona-vs-overlay distinction, and the non-linear buyer journey; how persona research drives creative strategy. |
| `problem-solution-headline-writer.md` | How to write effective problem/solution headlines. |
| `problem-solution-video-ad-formats.md` | The library of video ad formats for problem-solution-positioned brands. |
| `production.md` | How generated ads are made: prompt anatomy, model settings, rendering and fixes, paying for generation (quote, repair budget, cost log), generated video clips, an AI person who stays the same. Shared by the static, offer, video, song and motion skills. |
| `safe-zones.md` | Where each platform's buttons and text cover a 1080x1920 frame: the one safe box (x 100-880, y 290-1340) and per-placement numbers for Reels, Stories, Feed, TikTok and Facebook, measured on real phones by one creator in Oct 2026. Used by video-edits and motion-ads. |
| `scriptwriting.md` | The scriptwriting craft for ads — cold-audience acquisition principles and how to build a script. |
| `seasonality.md` | Seasonality beyond sale spikes: buyer, angle and SKU shifts, the ICP flip in gifting windows, evergreen winners stay on while seasonal layers in, planning months ahead, finding which seasons matter for a brand (ask, then validate), and nuance that beats obvious advice. |
| `selecting-ads-to-iterate-on.md` | The method for choosing which ads are worth iterating on — spend-in-context, run time, the breakdown effect, slow-burners vs high-risers, 60-day trends. |
| `self-help-books-2026.md` | Sarah Levinger's read of the top self-help books of 2026: people want peace, agency over their attention, protected boundaries and relief from overthinking. Books 1-8 with their core idea; 9 and 10 missing. |
| `spoken-script-voice.md` | The doctrine of human-sounding ad scripts and the brand voice-profile method, plus the AI-tells audit run on every draft. |
| `static-ad-design.md` | The design psychology of statics: how the eye scans (the default Z path), visual hierarchy, scroll-stopping formatting down to one-word emphasis and line breaks, sufficient as well as short, message-image fit, money shots, where proof goes, and layouts that lose the eye. |
| `static-ad-recreation.md` | How to recreate or adapt an existing static ad. |
| `story-skeletons-and-modifiers.md` | How to turn an off-niche organic video into an ad that doesn't read as one — single-task writing, story skeletons, communication modifiers, and the swap test. |
| `teep-creative-test-setup.md` | Sarah Levinger's creative test setup: 1 campaign with 4 T-E-E-P adsets, 3-10 ads per test in a fixed format mix, Trigger ads built on one micro-when, concepts from customer data, winners scaled horizontally. |
| `veo3-video-prompting.md` | How to prompt AI video generation (Veo 3). |
| `visual-vocabulary-method.md` | The method behind a brand's visual vocabulary — in-play / adjacent / out-of-play shot classification, the script-congruence and format-dependence rules. |
| `visuals.md` | The why-layer of the visual craft — how the visual carries the message alone (sound off, copy skimmed) and the eight principles that decide whether an ad is even seen: half-second clarity, visual hierarchy, pattern interruption, human presence, emotional specificity, native context over polish, click pre-qualification, and cognitive ease. |
| `winning-script-patterns.md` | What 100 tagged winning scripts share: a named enemy, problem first, one mechanism, hooks that describe the viewer, varied voices, product timing by job, proof and close. Five fill-in shapes and a pre-flight check. Stated. |
| `yapper-ads.md` | How to make yapper ads that find new angles: mine customer words, find the villain moment, hook with the pain on screen, tell it like a friend, bring the product in as the discovery, prove it and close the loop. New villain + same product = new angle. |

<!-- DOC-MAP:END -->

## Own ad-account reads

Performance reports and audits (weekly, monthly, 90-day, and the shareable report the `weekly-creative-report` skill builds for a brand's leadership), performance-targets-and-metrics, whitespace:
- `ad-account-analysis.md` — the canonical own-account reading method
- `ad-metrics-glossary.md` — plain-language definitions of the Meta metrics the read leans on; pull it when a number's meaning or calculation is in question
- `killer-performance-ads.md` — what a genuinely great ad looks like, the bar every read grades against
- `andromeda-v2.md` — how Meta's delivery system behaves, so delivery patterns are read as auction mechanics rather than mysteries
- `meta-creative-playbook.md` — Meta's own stated format-mix minimums (three formats per ad set, the 9:16-with-audio share) to check ad sets against, carried as Meta's numbers rather than promised lifts

Hook audits, any read of openers, and any feedback or critique on a video ad or a hook:
- `hook-psychology.md` — the canonical why-layer; the lead doc for generating hooks and for giving feedback/critique on a hook or video ad. Reason from its mechanisms (notice / qualify / intrigue / reassure / move / transport) and diagnose a weak hook by which job it fails — before reaching for format labels
- `hooks.md` — the hook format taxonomy and examples; name the real format and ground the read in its examples. A hook read that never uses its named concepts failed
- `emotional-delivery-and-timing.md` — the layer beneath hooks: the emotional state the viewer lands in, valence/intensity, and the TEEP phase she's in. Load it when the hook has to match a mood or a decision phase, not just create an emotion
- `ad-account-analysis.md`
- `ad-formats/` — the format taxonomy (video, static, both); name real formats from it
- `ai-writing-tells.md` — when the task *generates* hooks rather than reading them, the generated lines pass the lint-then-judge review before output

Selecting which ads to iterate on (account-level "what should we iterate on," before any specific ad is named):
- `selecting-ads-to-iterate-on.md` — the selection method: spend-in-account-context, run time, the breakdown effect, the promo caveat, slow-burner vs high-riser, 60-day trends. This is Phase A of the `iterations` skill, which then flows into Phase B (making the iterations) using `iterations.md`
- `ad-account-analysis.md` — the own-account reading method the selection grades against

Iteration reads (biweekly iterations report, iteration recommendations anywhere):
- `iterations.md` — the iteration doctrine
- `meta-creative-playbook.md` — Meta's remixing and format-adaptation moves for asset volume, read through `andromeda-v2.md`'s differentiation hierarchy where the two pull apart
- `ad-account-analysis.md`
- `ai-writing-tells.md` — when the iteration produces new copy (hooks, headlines, script lines), that copy passes the lint-then-judge review like any other creative deliverable

90-day creative-strategy audit and diversity audit:
- `killer-performance-ads.md`, `ad-account-analysis.md`, `hooks.md`, `ad-formats/`, `iterations.md`
- `persona-research-and-creative-strategy-process.md` — the served-vs-buyer read lives here
- `meta-creative-playbook.md` — the platform's format-mix minimums and its creative white-space map, a quick way to show where the account is crowded or empty

Visual-vocabulary generation — building the brand's `sub-context-docs/visual-vocabulary.md`:
- `visual-vocabulary-method.md` — the canonical method: in-play/adjacent/out-of-play classification, the script-congruence and format-dependence rules
- `ad-formats/` — the format taxonomy the visual grammar is read against
- `hooks.md` — the opener taxonomy, so visual hooks are named
- `analyzing-public-ad-accounts.md` — for the rival visual reads that source adjacent and out-of-play candidates
- `organic-social-analysis.md` — for the brand's own organic, where in-play and adjacent shots are seen

## Competitor and external reads

Competitor ad-account evaluations, creative landscape, top-impressions reports, single-competitor ad analysis, external 90-day audits:
- `analyzing-public-ad-accounts.md` — the canonical rival-library method: impression-rank as proxy, volume/recency/variant reading, library-vs-live-spend distinction
- `hooks.md`, `ad-formats/`
- `killer-performance-ads.md` — the bar for judging what a rival's winner actually is

## Customer language and persona reads

Customer review audits, review-sourced persona and VoC docs:
- `customer-review-mining-method.md` — the canonical mining method: golden nuggets, denominators, theme rates
- `persona-research-and-creative-strategy-process.md`

Persona source pulls, personas-profile, voice library, lifecycle maps, bias notes:
- `persona-research-and-creative-strategy-process.md` — identity-first persona doctrine, served-vs-buyer, the diagnosis
- `emotional-delivery-and-timing.md` — the canonical definition of TEEP (Trigger → Exploration → Evaluation → Purchase), required wherever the persona docs emit a "T-E-E-P content angle map" or "T-E-E-P decomposition," so the phases are reasoned from a real model rather than the acronym alone

VoC extractions and assembly:
- `customer-review-mining-method.md`
- `persona-research-and-creative-strategy-process.md`

## Organic and niche-feed reads

Organic channel inventories and organic audits:
- `organic-social-analysis.md`
- the video-format doc matching the brand's positioning: `lifestyle-video-ad-formats.md` and/or `problem-solution-video-ad-formats.md` — check the brand's actual positioning before choosing; many brands need both

TikTok mining:
- `adapting-scripts.md` — the adaptation method is the whole point of the doc
- `hooks.md`, plus the video-format docs above

## Ideation, briefs, and creative generation

Idea bank, idea evaluation, sprint plan, brief creation, concepting:
- `ideation-and-brainstorming.md`, `iterations.md`, `scriptwriting.md`
- `emotional-delivery-and-timing.md` — for brief creation especially: the TEEP phase and the from→to emotional shift are required brief inputs, and the funnel-as-emotional-arc lens shapes how variations diverge
- `creator-briefs.md` — for brief creation: the freedom-vs-direction call (freestyle vs director briefs), the role of references, the shared creator terminology, and giving the creator a story structure to build on
- `creative-consumption-analysis.md` — the per-persona read of the native content a persona already watches, reverse-engineered into a casting and production brief
- `meta-creative-playbook.md` — Meta's motivator-to-concept chain (motivator or barrier, benefit, message theme, hook, concept), creator-squad diversity, and briefing creators for inputs (alternate hooks, background footage) as well as finished deliverables

Idea evaluation specifically also loads, because it grades the captured pile against the strategy rather than capturing it:
- `persona-research-and-creative-strategy-process.md` — so each idea's persona and served-vs-buyer read is graded, not assumed
- `killer-performance-ads.md` — so every evidence band grades against the real bar
- `creative-strategy-fundamentals.md` — the priors that order confidence before speed and the kill-list discipline

Sprint plan specifically also loads, because it sizes and splits a round against the account's real production reality rather than grading ideas:
- `ad-account-analysis.md` — the own-account reading method behind the round-sizing math: the spend read and the net-new-evergreen cadence, promotional creative stripped out
- `persona-research-and-creative-strategy-process.md` — the diagnosis and the served-vs-buyer read that set the SKU split and the confidence-ranked persona allocation
- `killer-performance-ads.md` — the bar behind the two live reads: what is already working (double down) and what has been tried and failed (avoid)
- `creative-strategy-fundamentals.md` — the priors underneath sizing: confidence before speed, and the discipline that every concept in the round names a hypothesis
- `emotional-delivery-and-timing.md` — so each concept's doorway and leading emotion are set from a real model, not a label
- `teep-creative-test-setup.md` — one practitioner's test setup (1 campaign with 4 T-E-E-P adsets, ads per test, micro-when Trigger ads, horizontal scaling), offered to the person as an option; an open test, not a rule

Scriptwriting — any task that produces spoken words for an ad:
- `spoken-script-voice.md` — the human-voice doctrine and the brand voice-profile method; mandatory before writing any script's words, and the AI-tells audit runs on every draft
- `ai-writing-tells.md` — the written-slop sign families and the lint-then-judge review; every creative deliverable passes it before shipping, via the `creative-voice-review` agent and `scripts/voice-lint.py`
- `visual-vocabulary-method.md` — the visual twin of the voice profile; per-beat visual direction sources from the brand's `sub-context-docs/visual-vocabulary.md`, each beat marked in-play, adjacent, or out-of-play, with the script-congruence and format-dependence rules
- `visuals.md` — the why-layer beneath the visual-vocabulary method: how the visual carries the message with sound off and copy skimmed, and the eight principles that decide whether the ad is even seen
- `creative-consumption-analysis.md` — the persona's native-content read, so casting and on-screen situations blend into her feed
- `creator-briefs.md` — when the script hands off to a creator, the terminology and story-structure the brief needs
- `yapper-ads.md` — when the ad is one person telling a story to camera: the six steps (customer words, villain moment, pain-on-screen hook, friend story, product as discovery, proof and close), bullets not a script, and new villain = new angle; *Stated*, untested
- `scriptwriting.md`, `adapting-scripts.md` (the `recreate` skill runs this one for a video it recreates)

Headline and static generation:
- `spoken-script-voice.md` — the AI-tells list applies to headlines too
- `ai-writing-tells.md` — the written-slop signs are the primary check for headlines and statics; the lint-then-judge review runs before output
- `visual-vocabulary-method.md` — generated visuals source from the brand's `sub-context-docs/visual-vocabulary.md`; in-play shots ground the generation prompt, out-of-play visual inventions get flagged
- `lifestyle-headline-generator.md` or `problem-solution-headline-writer.md` by brand positioning
- `static-ad-design.md` — the design psychology of statics: the milliseconds-long eye scan, the visual-hierarchy call, message-image congruency, the money-shot, and where social proof goes. Statics have hooks too
- `visuals.md` — the eight principles that decide whether a static is even seen, the why-layer under the design rules
- `ai-static-ad-generation.md`, `static-ad-recreation.md` where statics are produced (the `recreate` skill runs `static-ad-recreation.md` for a static it recreates)
- `ai-animation-prompting.md` — when the asset is AI-animated, how animation prompting differs from static-image and Veo-style video prompting
- `legal-ai-ugc.md` — when the generated asset shows a synthetic human, the disclosure rules (the answer is labeling AI creative, not abandoning it)

## Brand-and-task modifiers — pull when the brand or the task fits

These docs don't belong to one task family. They bend the read when the brand or the moment matches, and they cut across the creative-generation and strategy work above — hooks, headlines, scripts, statics, ideation, the account read, and the persona and messaging calls. Reason over them the way you reason over the catalog: pull the ones the brand or task actually calls for, and don't force a fit where there isn't one.

- `advertising-luxury-and-higher-price-points.md` — when the brand is luxury-positioned or priced above its category average: the two axes, the brand-element constraints, and price-objection handling
- `advertising-to-older-audiences.md` — when the target skews roughly 50–70: the messaging, pacing, hooks, visuals, tone, and social-proof patterns that win, and the common misreads
- `non-problem-solution-creative.md` — when the product is bought for transformation, emotion, or belonging rather than to fix a pain: why agitation misfires and what to sell instead
- `creative-strategy-by-brand-size.md` — when the plan depends on spend level: the different priorities and plays at roughly $10k, $50k, and $1m per month
- `seasonality.md` — when the task lands near a gifting window or seasonal peak: how the buyer, angle, and SKU shift, why evergreen winners stay on, and how to find which seasons actually matter
- `black-friday-and-q4-data.md` — when the task touches Black Friday, Black Week, Christmas or Q4 planning: the cross-brand numbers (timing, CPMs, what won the sale week, gifting, the audience shift), this year's calendar with the Danish price rules, and where the data corrects `seasonality.md` and `gifting-and-q4-creative.md`
- `new-product-launches.md` (with its SKU-case pointer `new-sku-launch.md`) — when the task is launch creative for an established brand's new product, SKU, colorway, format, bundle, spinoff, or new-audience entry
- `algospeak.md` — when the category faces platform moderation risk (cannabis/CBD, adult wellness, harm reduction, mental health, crypto, body image): the coded-language and compliance guardrails that keep the account alive

## Syntheses

Brand-profile narrative, competitor snapshots, working thesis, gaps-opportunities-inspo, strategic roadmap, open-loops roll-up:
- `persona-research-and-creative-strategy-process.md` — the diagnosis discipline
- `killer-performance-ads.md` — so opportunity claims grade against the real bar
- `creative-strategy-fundamentals.md` — the open-loops reasoning layer: the senior-strategist priors, where curiosity tends to land, the posture moves that sharpen a question, and the trying-too-hard failure modes. Load it wherever loops are graded or strategic forks are drawn.
- plus the family docs of whatever upstream surfaces the synthesis reads (an ad-account-heavy synthesis loads the ad-account methods)

## Phase-2 strategy inputs

The four reads that resolve each territory's Phase-1 evidence into a committed recommendation for the strategic roadmap. All four load the synthesis core above; each also loads its territory's methods.

Persona strategy input — the WHO call:
- `persona-research-and-creative-strategy-process.md` — the served-vs-buyer read and the identity-first diagnosis that decide who to target
- `killer-performance-ads.md` — so the lead-persona call grades against the real performance bar
- `ad-account-analysis.md` — so delivery is read as who the account actually converts, not who the brand believes it targets

Messaging strategy input — what the brand should say:
- `creative-strategy-fundamentals.md` — the cross-read between what the brand says, what the customer says, and what the field rewards, where the message lives
- `customer-review-mining-method.md` — so the recommended lane is built from measured customer language, not brand echo
- `hooks.md`, `ad-account-analysis.md` — so the register and proof the account rewards are read from real openers and real winners
- `killer-performance-ads.md` — the bar the recommended message has to clear

Creator and talent strategy input — who should be on screen:
- `persona-research-and-creative-strategy-process.md` — so on-screen people are read against served-vs-buyer evidence, not casting assumptions
- `killer-performance-ads.md` — so talent proof is graded against the real bar for performance creative
- `ad-account-analysis.md` — so spend, delivery, frequency, and performance are read as Meta account behavior
- `andromeda-v2.md` — so creator and talent choices are read as creative-diversity signals, not only representation or credibility
- `visual-vocabulary-method.md` — so on-screen people, settings, proof moves, and first-frame visuals are reconstructed rather than labeled
- `analyzing-public-ad-accounts.md` — so competitor talent reads use rival library evidence correctly

Offer brief — the argument for the lead offer:
- `creative-strategy-fundamentals.md` — the cross-read of brand, customer and field the big idea has to come from
- `customer-review-mining-method.md` — so the desire, the objections and their counts come from measured customer language
- `persona-research-and-creative-strategy-process.md` — awareness and sophistication, which set the shape of the argument
- `killer-performance-ads.md` — the bar the argument has to let an ad clear

## The test

Before emitting, re-read your analysis against the loaded docs: does it use their named concepts, taxonomies, and vocabulary where they apply? A doc that routes to a method but does not speak its language proves the method was never opened, and the run failed regardless of how complete the output looks.

For creative deliverables, this test is no longer self-graded. The `context-grounding-review` agent (`.claude/agents/context-grounding-review.md`) runs it independently as a ship gate: it derives what should have been loaded and pulled for the task from this catalog, the brand vault, and the tool inventory, runs the deterministic checks in `scripts/grounding-check.py` (verbatims trace to the vault, cited sources exist on disk, receipts present), and diffs the output's *evidence* — its vocabulary, not its claims — against that read. A `bounced` verdict sends the work back for re-pulls and regeneration. Sign-off stamps remain the proof-of-read convention, but they are corroboration the gate verifies, not proof on their own.
