# Breakdown: <ad name>

<!-- Copy this file to audits/breakdowns/YYYY-MM-DD-<ad-slug>.md. Fill every field; unknown is "x" or
"Data-limited: <what would resolve it>". Labels: Verified, Stated, Inferred, Data-limited. -->

## Header

| Field | Value |
|---|---|
| Ad name | |
| Ad id | <account ad id, or Ad Library id> |
| Link | <the ad or Library link, or "No link given"> |
| Brand | <ours, or the competitor's> |
| Video or static | <and why, in one line> |
| Process | video / static / loser / light pass |
| Date of breakdown | YYYY-MM-DD |
| Launch date, days live | |
| Transcript source | <transcription route and model, or the data route that returned it> |

### Numbers

<!-- Our ad only. For a competitor ad write: "Not our ad: no performance data." -->

| Metric | Value | Account benchmark (same period) | Label |
|---|---|---|---|
| Spend | | | |
| Results (<the KPI event>) | | | |
| CPA | | | |
| ROAS | | | |
| Hook rate | | | |
| Hold rate | | | |
| CTR | | | |
| Frequency | | | |
| Run time (days) | | | |

Source: <Meta Ads MCP (ads_read) / export source-pulls/ad-account-YYYY-MM-DD.csv / pasted>, date range <from-to>,
pulled <date>, attribution <setting>, currency <code>. Winner bar: <quoted from running-notes/success-definition.md, or
"no bar set">. Verdict against the bar: <winner / loser / not enough data>.

### Your read (asked before the breakdown)

<!-- Word for word, with the time. Or: "No hypothesis given." -->

1. Angle:
2. Who it's for:
3. Why it won (or lost):
4. What you'd change:

## The breakdown

<!-- The parts from processes/video-breakdown.md or processes/static-breakdown.md, in order, each with a label. -->

## Why it worked, in five lines

<!-- "Why it lost" for a loser. Each line cites a part or a timestamp. -->

1.
2.
3.
4.
5.

## Tag block

<!-- The shared schema. Field meanings: brain-system/creative-strategy-context/creative-vocabulary.md, the ladder in
awareness-script-ladder.md, shapes and hook families in winning-script-patterns.md. Unknown is "x".
Allowed values are listed after each field. -->

```
concept_id:     x        # C07 from idea-bank/concepts.md, or x                          | label:
angle_id:       x        # A01... from angle-bank/angles.csv, or x                       | label:
persona_id:     x        # P1... in the order of personas/personas-profile.md, or x      | label:
awareness:      x        # UN / PA / SA / PR / MA                                        | label:
sophistication: x        # S1-S5 (market level, breakdown only)                          | label:
format:         x        # ugc-talk, podcast, street, skit, vsl, ai-anim, ai-avatar, song, demo, mashup,
                         # founder-talk, static-benefit, static-compare, static-review, static-meme,
                         # static-native, static-offer, carousel, motion, other          | label:
voice:          x        # creator, expert, customer, founder, vo, song, skit, ai, other, none | label:
shape:          x        # symptom, enemy, story, objection, authority, offer, other     | label:
ladder_start:   x        # 1-11, the ladder step the ad opens on                         | label:
hook_family:    x        # callout, story, show, claim, question, secret                 | label:
enemy:          none     # short text naming the specific thing blamed, or none          | label:
mechanism:      x        # yes / no                                                      | label:
product_at:     x        # % of runtime when the product or brand is first named (video); x for static | label:
proof:          none     # personal, number, authority, demo, timeline, taste, none (join with +) | label:
close:          none     # link, offer, guarantee, none (join with +)                    | label:
funnel:         x        # TOF / MOF / BOF from delivery (audience segments); x if unseen, never from awareness | label: Seen
```

Suggested ad name (`brain-system/system/ad-naming-convention.md`), for the team to apply in Ads Manager if they want:
`<YYMMDD_C07_A03_P2_PA_ugc-talk_creator_enemy_H2_v1>`

## Pattern check

<!-- Against brain-system/creative-strategy-context/winning-script-patterns.md and awareness-script-ladder.md. Point to
the docs; don't restate their numbers. -->

| Pattern | This ad | Evidence (timestamp or element) |
|---|---|---|
| Names a specific enemy (not a vague one) | yes / vague / no | |
| Opens on the viewer's problem, in the viewer's words | yes / no | |
| Gives one mechanism, said simply, with a "because" | yes / no | |
| Shape (of the five, or other) | | |
| Ladder start, and does it fit the awareness tag | step <n>, fits / starts too high / too low | |
| Product timing against the pattern | | |
| Proof, or does the enemy and the why carry belief | | |
| Close | | |

One line: where this ad follows the patterns and where it breaks them, and whether the break looks like the reason it
worked, or a risk it got away with.

## Your read vs the breakdown

- **Where you agreed:**
- **What the breakdown found that you didn't mention:**
- **Where the breakdown disagrees, and why:**
- **One thing to take into the next brief:**

## Next steps

<!-- Routed to skills, offered, not run: iterations, recreate, scriptwriting / static-ads, angle-bank,
ad-policy-check. -->
