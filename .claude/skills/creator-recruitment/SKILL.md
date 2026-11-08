---
name: creator-recruitment
description: Find, vet and contact creators for a brand in the Danish market (creator-recruitment, find creators, UGC creators, influencer outreach, creator sourcing, creator pool). Builds a shortlist with a written fit reason per creator instead of a mass-scraped list, drafts Danish collaboration offers that follow the Danish spam, hidden-advertising and GDPR rules, tracks the pipeline in the brain, and can run an optional check-in loop for replies. Use when someone asks to find creators, recruit UGC creators, build a creator list, reach out to influencers or follow up on creator replies. Tool-agnostic: reads the brain's tool-map.md.
---

# Creator recruitment (Danish market)

Always run inside the brand's brain folder. The US playbook scrapes 20,000 creators and emails them
all. That doesn't fit here: the Danish pool is small, everyone knows everyone, and a clumsy mass
message burns the brand with the creators it'll want next year. So this skill builds a **shortlist
of 30-80 who fit, each with a reason**, and grows it into a community that gets the next brief first.

The human approves the shortlist, every outreach text, and every deal. The skill never agrees to
a rate or signs anything.

## Where the knowledge lives

| File | Answers |
|---|---|
| `SKILL.md` (this file) | The steps and what must never happen |
| `dansk-lovgivning.md` | The Danish legal rules for outreach, data and marking, with sources |
| `feedback.md` | What we've observed. A log, not a rulebook |
| brain: `personas/personas-profile.md` | Who the creators need to speak to |
| brain: `creators/tracker.csv` | The pool and pipeline (the only place creator details are stored) |
| brain: `creators/README.md` | Tracker columns and the retention rule |
| brain: `tool-map.md` | "Creator comms", "Creator tracker", "Task board" roles |

## Prerequisites (check first, ask if missing)
- **The need**, from the human: how many creators, for which personas, which platforms, what kind
  of content (UGC for paid ads, organic posts on the creator's own profile, or both), the budget
  range per video in DKK, and the timeline. No budget range: ask. It decides who's realistic
- **Personas** in the brain. Without them, fit reasons turn generic
- **Usage rights decided**: organic only, paid ads on the brand's account, or paid via the
  creator's account (whitelisting / Spark Ads). It changes the rate and the contract, so it goes in
  the first message

## The steps

**1. Search profile.** Per persona: niche terms and Danish hashtags, follower range (micro,
roughly 5-100k, is usually the sweet spot for UGC in Denmark), language (Danish-speaking, and
audience in Denmark), content signals (talks to camera, good light and sound, shows products
naturally, **tells personal stories** rather than listing features), and **someone the persona looks
up to**: not necessarily the same age or life stage, but a person the persona would like to be or
trust. Personal-story creator ads are reported to outperform classic problem/solution UGC (Dara
Denney, Sep 2026, a sponsored video: Stated, not tested here). Show it to the human before searching.

**2. Search**, best sources first:
- **The brand's own orbit**: people who already tag the brand, review it, or comment
  enthusiastically. Warmest possible lead
- **Danish ads in the niche** in the Meta Ad Library: creators already appearing in ads are proven
  ad-ready. Note which brand they worked for (exclusivity may apply)
- **Platform search** on TikTok and Instagram with the search profile, in the browser. Public
  profiles only
- **The employer's existing tools**: many Danish brands already use a creator platform or agency
  (e.g. Make Influence) or have a creator list. Check before building from scratch
- **An open call**: a short "bliv creator hos os" form (in whatever form tool the employer uses)
  shared on the brand's channels. Consent from the start, and it builds the community
- **Apify (optional)**: only to pull public metrics (followers, average views, posting rate) for
  creators already on the longlist, not to harvest thousands. Check the actor's price per
  result first, state the expected cost and get a yes

**3. Vet and shortlist.** For each candidate: watch 3-5 recent posts. Write `persona_fit` (one line,
which persona and why) and `evidence` (1-2 post links). Check average views against followers
(bought followers show as tiny view counts), comment quality, audience language, and brand-safety
red flags. Judge fit on content, niche and audience. Don't guess gender, age, ethnicity or other
personal traits: if a persona needs a specific kind of person, describe what the content shows and
let the human decide. Add rows to `creators/tracker.csv` with status `shortlist`.

**4. STOP: approve the shortlist.** Show it as a table. Approved rows → `approved`.

**5. Draft the outreach** in Danish, one message per creator, personal (mention a post of theirs
and why it fits). Follow `dansk-lovgivning.md`, "Outreach". The message:
- says who we are and which brand, clearly
- is an offer of a collaboration: what kind of content, the usage rights, the timeline, and asks
  for their rate (or states the range, if the human prefers)
- does **not** sell: no discount codes, no product pitch beyond what they need to judge the
  collaboration, no "check out our shop"
- has one short line on where we found them and a link to the privacy policy (GDPR art. 14)
- is sent to a business contact they published, or as a platform DM
Show all drafts together.

**6. STOP: approve the texts.** Then send through the "Creator comms" role, or hand them over.
Send in small batches, not dozens at once: platforms flag mass DMs, and the pool is small.
Update `status` → `contacted`, `last_contact`.

**7. Replies and negotiation.** Log each reply in the tracker. Summarise quotes against the budget
range for the human. The human decides who to book and at what rate. When booked: write the
collaboration brief (brief templates in the brain's `briefs/_templates/`) with the marking and
usage-rights lines filled in, and save the agreed terms in `creators/briefs-sent/`.

**8. After delivery.** Score `quality` 1-5 with one line. Good creators get tagged in `notes` for
the next brief. Run the retention rule in `creators/README.md` monthly.

## Optional: check-in loop
On yes, schedule a recurring check (every few hours on weekdays) with the `schedule` or `loop`
skill: read new replies through "Creator comms", update `tracker.csv`, and report only what needs
the human (a quote to approve, a question, a creator ready to book). The loop never replies,
negotiates or books by itself. It ends when the recruitment round is done. Write the loop's
definition in the brain's `schedules/` first (template in its README), so it survives a switch of
tool.

## Guardrails (never)
- Never agree to a rate, accept terms, send a contract or pay anything
- Never send without approval of the text in this session
- Never use a private contact (personal phone, private email found elsewhere). Only published
  business contacts or platform DMs
- Never mass-scrape and mass-message. If the need is more than ~100 creators, stop and talk to the
  human about an open call or a platform instead
- Never store sensitive data about creators (health, religion, political views, sexuality,
  ethnicity), not even inferred from their content
- Creators under 18: stop and flag. A contract needs the guardians, and ads aimed at children have
  stricter rules (see `dansk-lovgivning.md`)
