# Concept register

Every ad belongs to one concept. A concept is **persona × angle × offer**: change any of the three and it's a new concept, because it reaches different people. Format (UGC, static, VSL, carousel) is not part of the concept: the same concept made as a video and as a static is one concept in two formats. The team's wider word "concept" (angle + format + structure) and how it maps to this register: `brain-system/creative-strategy-context/creative-vocabulary.md`.

**Not the idea index.** `idea-bank/index.md` lists raw ideas, ungraded. An idea becomes a concept here when `sprint-plan` puts it on a concept map (or a person briefs it directly). The idea's index row then gets the status "adapted into concept" and the concept ID.

**Why a register.** Meta credits a sale to the last ad clicked, so one ad's ROAS says little. A concept with several ads in its own ad set gives a number you can learn from ("this argument, to these people, works"). The weekly report reads results per concept, and briefs, statics and videos all carry the concept ID so they can be added up.

## The register

| ID | Persona | Angle (the argument, one sentence) | Offer | Awareness | Sprint | Formats made | Ads live | Status | Evidence / result |
|---|---|---|---|---|---|---|---|---|---|

- **ID:** `C01`, `C02` … in order, never reused. A second shoot or a new ad set of the same concept: `C07-2`
- **Persona:** by name, from `personas/personas-profile.md`
- **Angle:** the argument, not the topic ("shortens recovery after the long run", not "recovery"). It should trace to the offer brief (`strategy/offer-brief.md`): its big idea, a mechanism or a belief in its chain
- **Offer:** the product plus how value is framed (single, bundle, subscription, gift)
- **Status:** idea / briefed / live / winning / fatigued / retired. When it changes, write why and the date under Evidence, with the number it rests on
- **Evidence:** spend and the north-star metric at concept level, from the weekly report. A concept with no ads yet carries only its reason: the idea, source pull or roadmap gap it came from

## Naming

The same ID everywhere, so results can be sorted by concept in Ads Manager:

- **Ad set:** `C07_<persona>_<angle>`
- **Ad (the name in Ads Manager):** the full creative name, date first, then `C07_A03_P2_PA_...`, per `brain-system/system/ad-naming-convention.md`. The weekly leaderboard reads it. The file names below stay short
- **Statics:** `C07_` in front of the static-ads file name
- **Videos:** `C07_` in front of the video-edits name (`C07_B014_H3_15s`)
- **Briefs:** a `Concept: C07` line in the brief header

ASCII only (no æ, ø, å): they cause trouble in shells and some ad tools.

## Rules that come with it (Stated: one performance agency's creative lead, a 2026 Meta course; not tested here yet)

- **One concept per ad set.** Mixing concepts muddles who Meta looks for and makes the result unreadable
- **Test a concept with enough ads.** At a hit rate around 5 %, a new concept needs 10-20 ads before a winner is likely. One or two ads test those ads, not the concept
- **Don't add ads to a winning ad set.** Put them in a new one (`C07-2`)
- **When a concept fails, change in this order:** angle, then offer, then persona, format last
- **Diversity means different concepts,** not variations of one. Ads that say the same thing to the same people get grouped by Meta and shown to the same audience

When this brand's own results contradict a rule, note it in `running-notes/feedback.md` and follow the data.
