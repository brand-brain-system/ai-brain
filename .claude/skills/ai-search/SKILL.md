---
name: ai-search
description: Check and improve how AI assistants and search describe and recommend a brand in Denmark (ai-search, AI visibility, AEO, GEO, AI SEO, ChatGPT recommends, Perplexity, Google AI Overviews, AI Mode, "dukker vi op i ChatGPT", SEO check, product schema, robots.txt AI bots, share of AI voice). Builds a versioned portfolio of the questions Danish buyers actually ask, runs each several times per assistant in the browser, logs whether the brand is mentioned, recommended and described correctly, maps which sources the answers cite, checks the site's own basics (crawler access, readable product pages, structured data), and ends in a ranked fix list routed to the right skill or person. Use when someone asks whether the brand shows up in ChatGPT or Google's AI answers, why a competitor gets recommended, what AI says about the brand, or for an SEO or AI-search check. Read-only on the site; posts nothing.
---

# AI search (Danish market)

Always run inside the brand's brain folder. People now ask an assistant "hvad er den bedste
[kategori] til [situation]?" and buy from the shortlist it gives. Those answers are built from the
brand's own pages and from what others write about it (reviews, price comparison, media, forums).
This skill measures that shortlist from the outside, finds out why the brand is on it or not, and
turns it into fixes.

Method built on Corey Haines' open-source `ai-seo` skill (MIT, credited in
`brain-system/third-party/marketingskills/MANIFEST.md`), cut to physical-product brands in Denmark.
Their study figures (citation shares, lifts) are vendor research about US English answers and are not
carried over as facts.

## Where the knowledge lives

| File | Answers |
|---|---|
| `SKILL.md` (this file) | The steps and what must never happen |
| `prompt-portfolio.md` | How to build the question list, the intent families, cohorts and versioning |
| `site-checks.md` | The checks on the brand's own site: crawler access, readable pages, structured data, feeds |
| `scripts/tally.py` | Turns the run log into rates per prompt, assistant and topic, and the most-cited domains |
| `feedback.md` | What we've observed. A log, not a rulebook |
| brain: `search-visibility/` | The portfolio, the run log, readouts and the fix list (README there) |
| brain: `personas/voice-of-customer/`, research map | The words buyers use, which the questions are written in |
| brain: `competitors/_competitive-set.md` | Who to watch for in the answers |
| brain: `brand-lens.md`, `sub-context-docs/website-and-product-audit.md` | The brand's true facts, to check the answers against |

## Prerequisites
- **The browser** (the built-in one or Chrome). The assistants are run as a visitor would, logged
  out where the assistant allows it, so the answers aren't shaped by someone's history. If an
  assistant requires a login, the human logs in; never enter credentials
- **Personas and voice of customer.** Without them the questions are guesses; say so and label the
  portfolio Inferred
- **The brand's true facts:** prices, sizes, where it's sold, delivery, returns, guarantee, what
  the product does and doesn't do. From the brain, not from the web

## The steps

**1. Build or load the portfolio** (`search-visibility/prompt-portfolio.md`), per
`prompt-portfolio.md`. First run: 15-25 core prompts in Danish across the intent families, plus two
controls. Later runs: load the version on file and change nothing in the core during a comparison.

**2. STOP: approve the portfolio.** The human checks that these are questions their customers ask.

**3. Run.** Each core prompt **3 times** per assistant, in a fresh chat each time: ChatGPT, Google
(AI Overview on the results page and AI Mode where available in Denmark), Perplexity, and Gemini or
Copilot if the human wants them. Country Denmark, Danish language. Log one row per run in
`search-visibility/runs.csv` (columns in `prompt-portfolio.md`): mentioned, recommended (on the
shortlist the answer gives), position, competitors named, the cited URLs, and any statement about the
brand that is wrong. Save a screenshot of every answer that mentions the brand or a competitor in
`search-visibility/<date>/`. Rule 7: a plain browser session, one assistant at a time; no automation
that hammers a site.

**4. Tally** with `python3 brain-system/.claude/skills/ai-search/scripts/tally.py search-visibility/runs.csv`.
It prints mention and recommendation rates as "2/3" with the number of runs, per prompt, per
assistant and per topic, the competitors' rates beside the brand's, and the domains cited most. One
run is an anecdote; never report a single answer as "ChatGPT recommends us".

**5. Read the sources.** For the topics the brand loses, open the pages the answers cited when a
competitor won. Note page, domain, kind (own site, competitor, price comparison, retailer, media,
review site, forum, test or authority such as Forbrugerrådet Tænk) and what that page says that the
brand's pages don't. After 15-25 prompts the same domains repeat: that is the target list.

**6. Check the facts.** Every wrong or outdated statement about the brand (price, sizes, ingredients,
where to buy, returns) goes in the readout with the source that probably caused it. A wrong price or
a wrong claim about health or safety is a red flag at the top.

**7. Site checks** on the brand's own site, per `site-checks.md`: crawler access for search and AI
bots, product facts readable as text, structured data, the product feed. Read-only.

**8. Readout and fix list** (`search-visibility/readout-<date>.md`, `search-visibility/fix-list.md`).
Rates by topic and assistant beside the competitors, the source map, the wrong facts, the site
findings, and the fixes ranked by how many lost topics they touch. Route each fix:
- **A page on the brand's site** that should state a fact plainly (product page, FAQ, size guide,
  about): `iterate-landing-page` for a landing page; otherwise a brief for whoever runs the site
- **Reviews** (thin or old on the review sites the answers cite): `lifecycle-flows`, the review
  request flow
- **Third-party sources** (price comparison, retailers, media, test sites, forums): a task for a
  person. List the exact pages and what is missing
- **The product feed and site basics**: a task for whoever runs the shop
- **Comparison-type questions** where rivals win: an idea for the idea bank, not a page written "for AI"

**9. STOP: approve the fix list.** Nothing is changed on the site or anywhere else by this skill.

**10. Re-run** monthly or after a fix is live, with the same portfolio version, and compare per topic.
Log in `running-notes/refresh-schedule.md`. Put a fix's effect as an open loop when the change is
material (`brain-system/system/open-loops-system.md`).

## Labels
- Rates from the runs: **Verified** as observed answers, with n, assistant, date and country
- Why the brand is or isn't recommended: **Inferred** from the cited sources; say which
- Anything an assistant says about how it ranks: **Stated**, and usually not checkable
- Vendor studies about AI citations: **Stated**, and about other markets. Never a forecast

## Guardrails (never)
- Never write content "for AI" or mass-produce near-duplicate pages; fixes are pages that help people
- Never post, review, comment or edit anywhere (Reddit, review sites, Wikipedia, forums) as or for the
  brand. Never suggest fake or paid reviews, or reviews written by staff
- Never put personal data or a real customer's details into a prompt
- Never log in with anyone's credentials; never change the site, the feed or robots.txt
- Never report one run as a ranking, and never compare portfolios of different versions
