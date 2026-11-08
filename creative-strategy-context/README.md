# Creative strategy context

Shared craft knowledge every brain reads in place (at `brain-system/creative-strategy-context/`).

| Path | What |
|---|---|
| `production.md` | Ours. How generated ads are made: prompt anatomy, model settings, rendering, fixing errors, paying for generation (quote, repair budget, cost log), generated clips, an AI person who stays the same |
| `safe-zones.md` | Ours. Where each platform's buttons and text cover a 9:16 frame (one safe box x 100-880, y 290-1340, plus per-placement numbers), measured on real phones by one creator, Oct 2026. `video-edits` and `motion-ads` point here |
| `black-friday-and-q4-data.md` | Ours. What cross-brand Meta data (Parker's Q4 2025 study, credited) says about Black Friday and Q4, the calendar moved to this year with the Danish rules, and where it corrects the Q4 docs |
| `measurement-and-attribution.md` | Ours, built on Corey Haines' MIT `attribution` skill (`third-party/marketingskills/MANIFEST.md`). How to read a DTC brand's numbers when Meta, Google, GA4, the email tool and the store disagree; the post-purchase survey; holdout tests |
| `offer-design.md` | Ours, built on Corey Haines' MIT `offers` skill. The offer itself: the value equation, bundles, thresholds, gifts, guarantees beyond the law, true urgency, with the Danish lines |
| `meta-full-funnel-cbo-playbook.md` | Ours, in Danish by request. A step-by-step Meta playbook for one full-funnel CBO setup with 7DC attribution in three parts (TOF Old Winners, BOF Retargeting, TOF new creative): exclusions and spend limits. From a public post by Ben Radack, credited; *Stated*, not yet tested on our accounts |
| `teep-creative-test-setup.md` | Ours. Sarah Levinger's creative test setup from a public post, credited: 1 campaign with 4 T-E-E-P adsets, 3-10 ads per test in a fixed format mix, Trigger ads built on one micro-when, concepts from customer data, winners scaled horizontally (Opopop example). *Stated*, not yet tested on our accounts |
| `self-help-books-2026.md` | Ours. Sarah Levinger's read of the top self-help books of 2026 from a public post, credited: what people want now (peace, agency over attention, boundaries, less overthinking) and books 1-8 with their core idea. Books 9 and 10 are missing from the source |
| `yapper-ads.md` | Ours. How to make yapper ads that find new angles, from a whiteboard the team handed in (author unknown): mine customer words, find the villain moment, hook with the pain on screen, tell it like a friend, product as the discovery, prove it and close the loop; bullets not a script. New villain + same product = new angle. *Stated*, not yet tested on our accounts |
| `swipe-library/` | Ours and Alex Cooper's. Static-ad templates by category (`templates.csv` + `prompts.md` + images), `cards/` (fit data in `INDEX.json`), `offer-q4/` (offer templates), `ai-visual/` (prompts for AI-native images) |
| everything else (`*.md`) | The assistant's method docs, used with permission (`third-party/parker/MANIFEST.md`): hooks, headlines, scripts, iterations, static-ad design and recreation, AI writing tells, buying phases, price and luxury, older audiences, review mining, Q4 and gifting, seasonality, metrics glossary and more |

Images are stored through Git LFS. Add a template by adding its image, a row in the category's `templates.csv` and, if it has one, a card; never publish the library.
