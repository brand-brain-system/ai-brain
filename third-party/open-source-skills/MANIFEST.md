# Open-source skill repos read for v19

Eight public repositories were read on 7 Nov 2026 against the factory at v18, from a post that listed them as useful for ad
research and production. Each was shallow-cloned into a scratch folder, read, and deleted; nothing was installed, no script
from them was run, and **no file was copied**. What fitted a Danish DTC brand was rewritten in our words, with our paths,
labels and stop rules. Their performance figures and thresholds (mostly vendor or US data) were not carried over as facts.

Licence texts of the MIT repos we built on: [`LICENSE.md`](LICENSE.md). MIT allows commercial use, changes and sharing on
the condition that the copyright and permission notice travel with copies or substantial portions; keep that file here.

## Built on

| Here | Built on (repo, commit) | What we took | What we changed |
|---|---|---|---|
| `.claude/skills/ad-policy-check/` (new) | `gooseworks-ai/goose-skills` `df82981`, MIT (`skills/marketing/ad-policy-check`, `skills/shared/meta-ad-policy-checker`, `skills/marketing/honest-review`) | A pre-launch policy gate; rules fetched live from Meta's Transparency Center instead of a list that goes stale; stop/fix/note severities with a quoted rule and an intent-keeping rewrite; disapproval mode; "never pass what you couldn't check" | Danish rules checked through their homes in our skills; personal-attribute examples in Danish; EU AI label; no GooseWorks tools; their category table (US FDA framing) dropped |
| `ad-account-analysis/processes/measurement-check.md` (new), the recommendation rule in `ad-account-analysis/SKILL.md` | `AgriciDaniel/claude-ads` `fc3908e`, MIT (`ads/references/meta-audit.md`, `conversion-tracking.md`, `skills/ads-meta` cold-start contract); `irinabuht12-oss/marketing-skills` `b3bdcd6` (`meta-ads-audit` tracking checklist; README states MIT, no licence file in the repo) | Pass/fail/unknown/n.a. per control; tracing one real event; reconciling with the business record; account, pixel and conversion maturity read separately; a recommendation names evidence, baseline, mechanism, confidence, reversible step, window and rollback | Cut to one Danish Shopify brand on Meta; our store-as-truth rule; no fixed thresholds (their EMQ ≥ 6 and frequency rules dropped); read-only |
| `scripts/voice-lint.py` (nine English and eight Danish pattern families), `creative-strategy-context/ai-writing-tells.md` section 13, tests | `FeedHive/ai-slop-detector` `95d5507`, MIT (`skills/ai-slop-detector/SKILL.md`, 120 patterns) | The families our list lacked: chatbot residue, gap markers and citation debris, interpretive asides, self-correction, performed spontaneity, hedge stacking, "imagine a world", post formulas, things that "live" somewhere; the portability test and made-up specifics as judgment checks | Written as our own regexes, Danish twins added, tests pinning hits and clean copy |
| `prompts/personas/reddit.md`, "Pulling the threads"; one line in `harvest-ideas` | `mvanhorn/last30days-skill` `71dc2a1`, MIT (`docs/how-search-works.md`, `references/synthesis.md`, `scripts/lib/reddit_public.py`) | Comments outrank posts; a date window on every pull; clusters across sources lead, single-source is said; "no results" is not "not read" | Their engine is not used: Reddit's `.json` endpoints answer 403 and their route poses as a browser, which our no-workarounds rule forbids. Browser reading instead, anonymised authors |
| `creative-strategy-context/adapting-scripts.md`, step 2, "The shot sheet"; pointers in `recreate` and `video-edits` | `calesthio/OpenMontage` `d21f5d4`, **AGPL-3.0** (`skills/meta/video-reference-analyst.md`) | The idea of a five-aspect shot breakdown (subject, motion, scene with overlays as their own layer, framing, camera), "n/a" written out, and reading how each shot was made | Idea only, in our words. No code, text or schema taken, so the AGPL does not reach the factory. Keep it that way: never paste OpenMontage code here |

## Read and not taken

- **`coreyhaines31/marketingskills`** (`96798cf`): already the base of v11 (`third-party/marketingskills/MANIFEST.md`).
  Re-read the three skills the post named (`customer-research`, `ad-creative`, `competitor-profiling`): our
  `persona-gap`, `research-map`, `customer-review-mining-method.md`, `static-ads` and `competitor-teardown` cover them.
  Their interview and survey playbook (Mode 3) is the one piece worth a later look, when a brand can recruit customers
- **`realkimbarrett/advertising-skills`** (`45f4a4a`, MIT): short prompts on mechanism, objections, awareness and
  generic language; all covered in more depth by our method docs
- **`irinabuht12-oss/marketing-skills`**: apart from the tracking checklist above, 40-line descriptions that route to a
  third-party connector (Ryze MCP) that reads ad accounts; not connected (client data to an unknown vendor)
- **`gooseworks-ai/goose-skills`**, the rest: built on GooseWorks' hosted tools. The `claims-gate` idea of a review date
  on each approved claim is noted for `brand-lens-template.md` later
- **`AgriciDaniel/claude-ads`**, the rest: eleven other ad platforms and a JSON control plane; we run Meta first
- **`mvanhorn/last30days-skill`**, the engine: needs Python 3.12, optional paid keys and, for X, browser cookies
- **`calesthio/OpenMontage`**, the rest: a 12-pipeline video production system. Its short-form platform numbers are
  vendor statistics; our `safe-zones.md` and `video-edits` frame check already cover the specs
