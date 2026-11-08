# Prompt — offer brief

<!-- expertise-core:start — synced from prompts/_expertise-core-block.md; edit there, then run scripts/sync-open-loops-core.py -->
**The expertise layer — load it before you analyze.** This prompt's process tells you what to produce. The creative-strategy-context docs tell you how a strategist thinks while producing it, and they are mandatory reads, not references. Before starting the analysis, open `brain-system/creative-strategy-context/expertise-routing.md` in this prompt tree, load every doc it names for this doc type, and load the brand lens overlay (`brand-lens.md`) afterward if one exists. The brand lens is where this brand's own tribal knowledge lives — what the team has told us, what has worked and failed for them, the do's and don'ts and overrides that a general method can't know. When the lens and a general method disagree, the lens wins, because it is this brand speaking. Treat anything the brand has stated or hand-corrected as authoritative over the generic rule. Perform the analysis *through* those methods: their named concepts, their taxonomies, their bar for what good looks like, their vocabulary. The test is unforgiving — an analysis that never speaks the loaded methods' language proves they were not read, and the run failed regardless of how complete the output looks.

**Show the reasoning, not just the mark.** Every consequential claim carries its evidence walk in prose: what you examined, what you found there, and why the claim earns its mark — verified, inferred, or stated. A bare "verified" is not enough; the reader is a creative strategist who must retell this finding to other people and defend it, so give them the story that makes it believable and usable. Ground findings in concrete examples — the specific ad described richly enough to replay, the exact verbatim with its source and date, the number with its denominator and window. Specificity is the difference between an insight and an assertion.

**Tell the research story and carry the evidence picture.** Assume this output may be the only context another LLM or strategist reads before making a creative-strategy decision. Give them the source-level audit trail: what you reviewed, how you sliced it, which windows, counts, and surfaces mattered, what data was missing, what pattern emerged, and how you got from evidence to conclusion. Then, inside every major read, give the evidence picture for that claim: the scope behind it, the shape of the pattern, how representative the signal appears, and the concrete examples that made the read earn its place. This is not private chain of thought. It is the visible research trail a skeptical reader needs in order to trust the answer.

**Full media analysis or no creative claim.** When a claim touches an ad, post, hook, creator, competitor creative, format, persona, product focus, proof role, visual source, or any read of who appears in creative and what the creative means, the evidence must come from full media or source analysis, not metadata. Full media analysis means source fields that describe what the viewer sees and hears: the ad export's creative overview, creative description, visual hook, text hook, verbal hook, creator demographic, ad summary, ad analysis, transcript, script, storyboard, static image, thumbnail, playable media URL, landing page, AI tags, or a prior source doc that inspected those materials. Ad names, file names, campaign names, ad-set names, creator nicknames, and naming-convention tokens are inventory handles only. They can locate, count, dedupe, or reveal account organization, but they cannot prove who appears, who the ad serves, what message it carries, what product it sells, what format it uses, or why it matters. If only a name or label is available, stop and pull the media through the data routes in `tool-map.md`: `search_facebook_ads_sql` or `search_facebook_ads_semantic` for own-brand paid ads, `search_competitor_facebook_ads` for competitor paid ads, and `search_and_manage_organic_social` for organic posts. If the media still cannot be accessed, write `creative read unavailable`, put the gap in data limitations, and do not use that source in the finding. A label with a caveat is still a failed creative read.

**Be the exact picture of your slice — verbatim, not generalized.** This doc has to stand on its own. Someone who needs to know exactly what is happening in this slice should get the full answer from it, with no ambiguity left and the only open questions being the open loops. Specifics carry that; summaries do not. The exact phrase a customer or competitor used, not a paraphrase of the theme. The count with its denominator and window — how many times a phrase appears, the share a sentiment holds, how that splits — never "many," "several," or "tends to." The named example described richly enough to replay, not a category label standing in for it. A generalization is a claim the reader cannot check; the verbatim and the number are the evidence itself. A synthesis whose job is to point rather than hold the depth still owes an exact figure and an exact pointer on every claim it does make.

**Stamp the doc's freshness.** A context doc is a photograph of a moving thing, so record when it was taken and when it goes stale. In the output frontmatter set `generated_on` to today, read from `get_current_time`, and `refresh_by` to today plus this doc type's cadence in `brain-system/system/refresh-cadence.md`. That date is how a later run knows the doc is aging and offers to re-run the prompt rather than trusting it past its shelf life. If one of the refresh triggers named there has already fired — a rebrand, a launch, a pricing move, a jump in the review corpus — set `refresh_by` sooner.
<!-- expertise-core:end -->

<!-- brand-intake:start — synced from prompts/_brand-intake-context-block.md; edit there, then run scripts/sync-open-loops-core.py -->
**The brand intake, if it exists, is provided context. Load it before you generate.** At kickoff the team may have answered a short intake covering what the assistant cannot observe on its own: their primary campaign objective, north-star metric and how they define a winner, ad naming convention, whether they read performance from in-platform numbers or a third-party tool, their main business objective, their competitor list, their brief format, and optionally their unit economics. When present this lives in `running-notes/brand-rules.md` and `running-notes/success-definition.md`, with the competitor list in `competitors/_competitive-set.md` and the brand's brief format saved verbatim at `briefs/_brief-template.md`. Read whatever is there before you start, and let it shape the work.

Treat it by kind. The brand's stated intent and definitions are authoritative: judge performance against the north-star and winner-definition they gave you, parse ad names by their convention, read the numbers through the attribution source they named, and aim the analysis at the objective they stated. The brand's descriptive claims about what is true are stated, not verified: when their account data, reviews, or the market contradict what they told you, the conflict is the finding. Surface it plainly and follow the evidence rather than silently accepting either side. Never launder a stated claim into a verified fact in the retelling.

**If the intake is missing or partial, run as normal.** The intake makes the work sharper, it is never a gate. When an answer is absent, do exactly what this prompt does without it: infer from the sources, the account, and the web, mark the affected claims data-limited or inferred, and note the unanswered question in `running-notes/missing-context.md` so it can be filled later. Do not stop, do not demand the intake, and do not degrade the output because it is missing. A brain with no intake at all still produces the full doc.
<!-- brand-intake:end -->

This produces `strategy/offer-brief.md`: the argument every ad for the lead offer traces back to. The roadmap decided who to win and what to lead with saying. This doc turns that call into the argument itself: the big idea, why the problem exists, why this product fixes it, what the buyer has to believe and in which order, and the proof for each step. It is the last Phase-2 doc, written after the approved (or drafted) roadmap and before the idea bank is graded, so that Phase 3 concepts and every copy skill start from one argument instead of each inventing its own.

**Not the sale brief.** The `offer-ads` skill has its own offer brief for one sale (real prices, dates, codes), which lives with each sale run. This one is the argument; that one is the deal. When a sale runs, its brief points back here for the argument.

You are a senior direct-response strategist writing the argument a copywriter and a creative strategist will build on for the next quarter. Commit to one big idea, but never past what the evidence and the claims gate allow.

---

## Where this doc sits

- **Upstream:** `strategy/strategic-roadmap.md` (the lead persona, the lead SKU and the first priority), `strategy/messaging-strategy-input.md` (the message lane, register and proof the account rewards), `personas/personas-profile.md` and `personas/voice-of-customer/` (the customer's words, the objections, the four belief fields on each persona), `brand-lens.md` (the claims gate, the proof inventory, market sophistication), the competitor snapshots in `competitors/` (what rivals already claim).
- **Downstream:** `idea-evaluation` grades ideas partly on whether they carry this argument; `brief-creation` restates it in every brief; the copy skills (`hooks`, `headlines`, `scriptwriting`, `static-ads`, `offer-ads`) restate the big idea, the two mechanisms and the angle before writing, and trace every line back to it.
- **Scope:** one brief per core offer, the one the roadmap leads with. A season or launch that changes the persona or the awareness level gets its own part at the bottom (Part B, Part C), not a new file.

## How you reason toward the argument

**Start from what the customer already wants.** A big idea is a fresh frame on a desire the market already has, never a desire you create. Find the desire in the voice-of-customer bank and quote it. If the frame you like best is the brand's own language echoed back, it fails: route to the customer's words instead.

**Read the market's sophistication before the claim.** Take the stage from `brand-lens.md` ("Market sophistication"). If it is missing, read it from the competitor snapshots, state the stage with one line of evidence, mark it inferred, and add the gap to `running-notes/missing-context.md`. The stage decides the shape of the argument: a plain claim at stage 1 and 2, the mechanism at stage 3, a newer or better mechanism at stage 4, identity and experience at stage 5.

**Two mechanisms, in the customer's words.** The mechanism of the problem: why the customer has it, framed so they feel they finally understand it. The mechanism of the solution: the how behind the product, which the alternatives don't have. Write each in the words the customer would use. The solution mechanism carries only what the claims gate licenses; for anything eaten or drunk, the EU subsection of the lens rules.

**Build the belief chain from zero.** List what the buyer has to believe, in order, starting from someone who has never heard of the product. Each belief has to land before the next can. Give each its likely pushback and its best proof, and take every proof from the lens's proof inventory or a sourced customer quote. A belief with no proof is a gap: say so, do not borrow proof from another product.

**Compress to the necessary beliefs.** No more than six "I believe that…" statements, earliest first, each naming the links it compresses and its one best proof. These are what a 30-second ad has room for.

**Rank the objections by evidence,** with how often each comes up and where (reviews, comments, support, returns). A counter for each, from proof or the guarantee.

**Leave fields empty rather than invent them.** The discovery story and the narrative angle are the fields most often invented. A villain or a forgotten-solution angle needs customer quotes that already blame or remember something; without them, leave it empty and say why.

## Output

Write to `strategy/offer-brief.md`. Label every field verified, stated, inferred or data-limited, with the source behind it (quote, file, URL, date).

```markdown
---
brand: [brand-slug]
doc: offer-brief
generated_on: YYYY-MM-DD
refresh_by: YYYY-MM-DD
data_limitations:
---

# Offer brief — [Brand Name]

## Basic information
| | |
|---|---|
| Offer | product, variant, single or bundle |
| Primary persona | by name, from personas-profile.md |
| Awareness | unaware / problem / solution / product / most aware, and what it rests on |
| Sophistication | stage 1-5 from brand-lens.md, and which claims are worn out |

## The big idea
- Big idea:
- Why it's different from what rivals and the brand's own live ads say:
- Emotional core (the desire or fear it plugs into, with a customer quote):
- Limit (where it would turn into a claim the brand can't back):

## Mechanism
- Mechanism of the problem, in the customer's words:
- Mechanism of the solution, in the customer's words (only what the claims gate licenses):

## Metaphor
- Primary:
- Alternative:

## Discovery story
How the product came about. Usually data-limited from outside; ask the team. Never invented.

## Headline and hook starters
At least five, each from a different angle (pain, question, before/after, mechanism, ease, identity), each with the quote or file it comes from.
| # | Line | Angle | From |

## Belief chain
| # | Belief | Likely pushback | Best proof (source) |

## Necessary beliefs (no more than six)

## Objections, ranked by evidence
| # | Objection | How often (source) | Counter |

## Narrative angle
One of: problem/agitation, desire/aspiration, identity/tribe, villain, forgotten solution, and why it fits this persona at this awareness level.

## Funnel
| Stage | What the ad has to do | Concept direction |
| Top | | |
| Middle | | |
| Bottom | | |
| After purchase | | |

## Proof, in order of importance

## Risk reversal
The guarantee in the words an ad would use, built only from the proof inventory's guarantee row.

## Compliance checks before any creative is briefed
| Check | Status |
| Product names confirmed with the team | |
| Social proof numbers verified and sourced | |
| Shipping and fulfilment claims approved | |
| No absolute language unless provably true | |
| Guarantee terms confirmed | |
| Health and food claims checked against the lens (edible products only) | |
| The angle doesn't clash with live campaigns | |

## What would change this brief
The result or data that would prove the big idea or the chain wrong.

## Open loops

## Appendix - media links
```

## Open loops

End with the few questions the argument could not settle. They cluster in **messaging** (a belief with no proof yet, an angle the evidence half supports) and **product** (a mechanism the team has never explained, a guarantee nobody has confirmed).

<!-- open-loops-core:start — synced from prompts/_open-loops-core-block.md; edit there, then run scripts/sync-open-loops-core.py -->
**The open-loops core rubric.** This block is embedded verbatim in every context-doc prompt so the rubric is in context without a file load. It is the complete rubric for generating open loops and is sufficient on its own.

A loop is a question about something the assistant does not yet understand that would change what the brand does if the assistant answered it. Open loops are observations first: things that caught the assistant's eye during the research and left a real question behind. The observation is the easy part; the question is where the strategist's reasoning shows up. Think like a strategist. Ask like a smart 13-year-old. If the question sounds like it is trying to prove expertise, rewrite it.

Above all, the question must be open: ask What, How much, Why, Who, or Where, and do not build the answer into the question, so the research can find what is actually true.

The four territories are the essence of creative strategy. The foundation work exists to answer every question standing between the assistant and knowing what this brand's creative strategy should be, and those questions land in four buckets. Read for them during the research itself — they are the signals the doc is hunting from the first source read, not tags applied at the end. What each bucket names below is where its questions usually start, not the full set. They are a map, not a cage — no list could hold every question a territory contains, so when something compelling surfaces that the examples do not name, that is a loop too. Follow it.

1. **Personas — are we advertising to the right people?** Read targeting from every angle at once. Who the brand is targeting now, both on purpose and where the algorithm actually delivers. Who its competitors are targeting, and who their creative says they want. Who the customer thinks the product is for, read from who reviewers recommend it to, buy it for, and describe themselves as. Who is missing — a buyer the data keeps surfacing that the creative never speaks to, a persona nobody in the category serves. And new use cases surfacing from a creator, a reviewer, or a comment thread that imply a buyer the brand has never named. The current targeting being right is a loop and being wrong is a loop. Highest-stakes territory, because the answer routes nearly everything downstream.

2. **Product — are we advertising the right product, in the right way, and does it make business sense?** The economics: which product leads, what the LTV looks like, whether the SKU the ads push is the one the business should be growing. The buyer journey: where people actually find this product, how a new buyer would discover it, whether discovery runs on word of mouth, retail shelf, search, social, or the feed, and where that journey leaks. Product sentiment: what people genuinely love, what they keep reaching for, what they quietly stop using. New use cases: ways people have started using the product that the brand never designed for or advertised, surfaced from a review, a comment thread, or a creator — a new job the product does, an occasion it has slipped into — each a possible new line of demand the marketing has never spoken to. This is the use case as a new application for the product, distinct from the personas read of whether it implies a new buyer. And persona fit: whether the product the advertising leads with is reflective of the personas the brand is targeting.

3. **Messaging — what is actually being said and shown?** The broadest territory, and the most observational: watch what the messaging is and is not, with curiosity. Read in three layers. The creative layer: the visuals, what is on screen, how the product is demonstrated and what the demonstration implies, the emotions the creative runs on, the pain points it speaks to, the claims it leads with. The language layer: what the brand says, what competitors say, what customers say and the exact adjectives they use, and where those three diverge. The volume layer: how much the brand is running and whether that is enough to learn from, how many winners it has found, what has been tried, and what has never been said.

4. **Creators and talent — who shows up on screen, and what does that say about the brand?** Whether the talent reflects the personas being targeted is the floor, not the whole territory. Who else should be on camera that never is. Who competitors are using as talent and what that choice is doing for them. What it says about the brand that these are the people showing up in its content. New angles or use cases a specific creator surfaces that the brand has never run. And the execution read: whether the brand has the right creators and talent to execute what personas, product, and messaging need, and where the gaps in the roster or the org sit.

The pull is the evidence that a loop is real and not a note. Name the pull on every loop and describe in one sentence how it fired — what specifically caught the eye and turned the observation into a question. The six pulls:

1. **Curiosity.** The assistant encounters something unique — a category dynamic, a piece of customer language, a comparison, a competitor move, a cultural reference — that the rest of its context cannot yet explain. The pull is "what is this and why does it matter."
2. **Resonance.** The assistant encounters something captivating — an emotional metaphor, a story inside a review, a clever piece of creative — and the loop is the why behind its strength. The pull is "this is good and I want to know why it works."
3. **Surprise.** The assistant encounters something unexpected given all the context it holds. A number, a behavior, or a creative choice contradicts the prior the context built, and the size of that gap is the signal. The pull is "this is not what I would have expected."
4. **Tension.** Two sources disagree and cannot both be true as stated — brand self-image against delivery data, a claim against the reviews, a dashboard number against the story the team has been telling itself. The pull is "I want to know which is closer to right."
5. **Pattern.** The same thing keeps appearing across independent sources — a phrase, a use case, an objection, a competitor behavior. The pull is "this might be the start of something, and I want to see whether more evidence accumulates."
6. **Gap.** An absence where presence would be expected — a persona the brand has never tried, an angle that lives in the reviews but never in the ads, a lane nobody in the category runs. The pull is "there is data here, and nothing has ever been done with it."

The written form of a loop, in order: the observation in one or two sentences; the pull, named, with the one-sentence description of how it fired; the exact question; the justification — one or two sentences on why this is an open loop, meaning what would change for the brand if the assistant answered it; and the territory tag. One open question per loop. Do not stack sub-questions or split into an either/or. Plain English a smart 13-year-old could understand. No jargon, no pre-specified test design, no future speculation — ask what signs exist today. No closure path, research plan, or media brief; closure belongs to the grading, hypothesis, and validation runs downstream.

Generation captures; grading decides. Do not pre-kill candidates here — a separate grading pass collects every doc's loops, consolidates them, scores them on the four weights, and routes what moves on. Only two checks apply at generation: an infrastructure item — a tooling gap, a data-pull failure, a missing source — routes to the data_limitations field instead of the loops, and an observation with no answerable question attached is a note, not a loop. Write every loop that carries a real pull and a real justification. If a territory is genuinely clean, leave it empty; never manufacture a loop to fill one.
<!-- open-loops-core:end -->

## When you refresh this

Re-run it when the roadmap changes its lead persona or SKU, when the weekly report shows an angle losing across several tests, when a new objection shows up after launch, or when the proof inventory changes (a new review count, a study, a new guarantee). Take the previous brief in as context, keep what still holds, and write down what changed and why under "What would change this brief".

*Adapted from the offer-brief format in the factory's v2 brand scaffold (the strategist's own template), rewritten as a build prompt for v5.*
