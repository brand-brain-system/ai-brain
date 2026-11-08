# Corey Haines' marketingskills in this factory

Source: `github.com/coreyhaines31/marketingskills`, commit `88c79f6` (30 Oct 2026), read 31 Oct 2026. Licence: MIT, copy in [`LICENSE.md`](LICENSE.md).
Found through a Dutch PDF guide to the repo ("50 kant-en-klare marketing skills voor Claude", by a consultancy), which is only an index and credits the repo; nothing was taken from the guide.

**No file was copied.** The repo's skills were read, and the pieces that fit a Danish DTC brand were rewritten in our own words, with our paths, labels and stop rules, and with Danish law added
from primary sources. Their study figures and benchmarks (mostly US vendor research) were not carried over as facts. MIT asks that the copyright and permission notice travel with copies or
substantial portions; the licence copy stays here and each file below credits the repo in its first lines.

| Here | Built on (their skill, version) | What we took | What we changed |
|---|---|---|---|
| `.claude/skills/lifecycle-flows/` | `emails` 2.1.4, `sms` 1.1.0 (and the capture parts of `popups`) | The flow set (welcome, cart, post-purchase, replenishment, win-back, sunset), "one email, one job", SMS segment counting, discount late in cart reminders | Danish legal file from Forbrugerombudsmanden's guidance; a legal basis per message; drafts only; removed templates that would break Danish rules (false urgency, review rewards, cart reminders without consent) |
| `.claude/skills/ai-search/` | `ai-seo` 2.12.0 (references: prompt portfolio, multilingual and commerce, platform factors) | The audit loop, intent families, cohorts and versioning, repeated runs with rates, bot types by purpose, "fix the page before writing a new one" | Danish prompts and sources, browser runs logged per row, our `tally.py`, fixes routed to our skills; vendor citation shares dropped |
| `.claude/skills/competitor-teardown/` | `reverse-engineer-marketing` 1.0.0 (stages, evidence standard, DTC pack, go-inside rules) | Moves timeline, clusters not single moves, going inside with approval, gap table, plays and plays to skip, watch mode | Our own Python `teardown.py` (their Node script not used), Danish rules, our labels, paid data sources off by default |
| `.claude/skills/growth-plan/` | `marketing-plan` 1.2.2 | Stage-tagged moves, scored current state, 90-day and 12-month horizon, every move with a mechanism and a leading indicator | DTC stages (reach, convert, repeat, recommend, measure), our rubric, routing to our skills; funding tiers and SaaS benchmarks dropped |
| `creative-strategy-context/measurement-and-attribution.md` | `attribution` 1.1.6 (and its DTC and paradigms references) | One source of truth for counts, why each tool is biased, the survey as awareness not credit, how to read a lift test | Cut to DTC on Meta and Shopify, Danish survey question, our labels and readout table |
| `creative-strategy-context/offer-design.md` | `offers` 1.0.3 (value equation, scarcity, bonus stacking) | The value equation (theirs, after Alex Hormozi), one lever at a time, real urgency only | Physical-product levers; Danish law on statutory rights, "gratis" and false urgency, read in the law's annex |

## Re-read 7 Nov 2026

Commit `96798cf` (6 Nov 2026): the same 53 skills. `customer-research`, `ad-creative` and `competitor-profiling` were re-read for v19 and nothing new was taken; see `third-party/open-source-skills/MANIFEST.md`.

## Read and not used

Evaluated on 31 Oct 2026 against the factory; reasons in `REWRITE-QUEUE.md`, section 12.
