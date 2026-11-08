---
summary: "How ads are named so results add up by tag: YYMMDD_concept_angle_persona_awareness_format_voice_shape_hook_version. Allowed values, rules, a field map for a brand that keeps its own names, and how to adopt it on a live account."
---

# Ad naming convention

**Source:** a practitioner's post on running an angle system (Nov 2026): name every ad by angle, persona, awareness and format, and rank them weekly. The field list is ours, built on the shared tag schema.
**Users:** every skill that names, reads or ranks an ad. `creative-leaderboard` parses names with it (`.claude/skills/creative-leaderboard/scripts/ad_name.py`); skills that name ad files (`static-ads`, `video-edits`, `motion-ads`) and briefs follow it; `set-up-brain` asks about it in the intake.
**Status:** *Stated* (one source, no data). This file is the one home for how ads are named. Other files point here.

The point is simple. If the name carries the creative tags, a plain Ads Manager export can be added up by angle, persona, awareness, format, voice and shape without anyone tagging ads by hand. The name is what the team typed, so tags read from it are Verified (`system/evidence-and-labels.md`): they say what the team meant the ad to be, not what a viewer sees in it. What the ad actually does is the job of `ad-breakdown`.

## The format

```
YYMMDD_C07_A03_P2_PA_ugc-talk_creator_enemy_H2_v1
```

Ten fields, in this order:

| # | Field | Example | Allowed values |
|---|---|---|---|
| 1 | `launch_date` | `261107` | The day the ad first goes live, `YYMMDD` |
| 2 | `concept_id` | `C07` | The concept's ID from the brain's `idea-bank/concepts.md`, with its suffix when there is one (`C07-2`) |
| 3 | `angle_id` | `A03` | The angle's ID from `angle-bank/angles.csv` |
| 4 | `persona_id` | `P2` | `P1`, `P2`... in the order of `personas/personas-profile.md` |
| 5 | `awareness` | `PA` | `UN` unaware, `PA` problem aware, `SA` solution aware, `PR` product aware, `MA` most aware |
| 6 | `format` | `ugc-talk` | `ugc-talk`, `podcast`, `street`, `skit`, `vsl`, `ai-anim`, `ai-avatar`, `song`, `demo`, `mashup`, `founder-talk`, `static-benefit`, `static-compare`, `static-review`, `static-meme`, `static-native`, `static-offer`, `carousel`, `motion`, `other` |
| 7 | `voice` | `creator` | `creator`, `expert`, `customer`, `founder`, `vo`, `song`, `skit`, `ai`, `other`, `none` (a static without a speaker) |
| 8 | `shape` | `enemy` | `symptom`, `enemy`, `story`, `objection`, `authority`, `offer`, `other` |
| 9 | `hook` | `H2` | The hook variant inside the concept: `H1`, `H2`... |
| 10 | `version` | `v1` | The cut or edit: `v1`, `v2`... |

The values are the shared tag schema that `ad-breakdown`, `angle-bank` and `creative-leaderboard` all use. What each value means (an angle, a persona, an awareness level, each format and shape) is defined in `brain-system/creative-strategy-context/creative-vocabulary.md`. The five shapes are described in `brain-system/creative-strategy-context/winning-script-patterns.md`.

Anything after the tenth field is a free tail the parser keeps but does not rank on: a length or a ratio, say `..._H2_v1_15s_9x16`.

## Rules

- **`_` separates fields.** Never put `_` inside a value. Inside a value, use a hyphen (`ugc-talk`, `C07-2`)
- **`x` means unknown or not decided.** Every field is always there, so the positions never shift. A static with no persona yet: `261107_C07_A03_x_PA_static-benefit_none_symptom_H1_v1`
- **No spaces, no æ, ø or å.** ASCII only, as in `idea-bank/concepts.md`. They break shells and some ad tools
- **Upper case for IDs and awareness, lower case for the rest.** The parser accepts either, but one way reads faster in Ads Manager
- **The launch date is the day the ad goes live.** If the plan slips, fix the name before launch. The leaderboard counts hit rate from this date
- **A duplicate keeps its name.** Ads Manager adds a Copy (or Kopi) suffix. The parser ignores it, but a new edit should get a new `version`
- **An ID must exist before the name does.** Add the concept to `idea-bank/concepts.md` and the angle to `angle-bank/angles.csv` first. A name with an ID that isn't in either file is a typo until someone adds it

## What goes where

- **The ad name** carries the creative tags, in the format above. This is the only name this convention sets
- **The ad set and campaign names are the brand's.** Keep whatever the team uses. The concept register suggests `C07_<persona>_<angle>` for an ad set (`idea-bank/concepts.md`); that is fine and doesn't conflict, since the leaderboard reads only the ad name
- **File names** for statics and videos start with the same ad name, so the file and the ad can be matched

## A brand that already has its own convention

Don't make a team change a naming habit that works. Keep their convention and write a field map once in the brain's `running-notes/ad-naming.md`. The parser reads it (`--naming-map running-notes/ad-naming.md`).

The map is a small Markdown file: the separator, the date format, and one table row per position in their names.

```markdown
# Ad naming field map

How this brand names ads, mapped to our fields. Written <date> by <who>, from <n> live ad names.

separator: `-`
date_format: DDMMYY
min_fields: 5

| Position | Their field | Our field | Value map |
|---|---|---|---|
| 1 | Product code | x | |
| 2 | Launch date | launch_date | |
| 3 | Concept | concept_id | |
| 4 | Angle word | angle_id | pain=A01; gift=A02 |
| 5 | Type | format | UGC=ugc-talk; STAT=static-benefit |
| 6 | Creator | voice | |
```

- **Our field** is one of `launch_date`, `concept_id`, `angle_id`, `persona_id`, `awareness`, `format`, `voice`, `shape`, `hook`, `version`, or `x` for a position we skip
- **Value map** turns their words into our values, `theirs=ours`, split by `;`. A value that isn't mapped must already be one of our allowed values, or the name is listed as not parsing
- **Date format** uses `YYYY`, `YY`, `MM` and `DD` (`DDMMYY`, `YYYYMMDD`, `YYYY.MM.DD`)
- **min_fields** is how many parts a name needs before it counts as theirs. Default: the highest position in the table
- Fields their convention doesn't carry come out as `x`. Those tags can still come from `ad-breakdown`

Test the map on the account's real names with `python3 brain-system/.claude/skills/creative-leaderboard/scripts/ad_name.py "<name>" --naming-map running-notes/ad-naming.md` before the first leaderboard.

## Adopting it on an account that already runs ads

1. **New ads only.** From the adoption date, every new ad gets a name in this format (or in the brand's mapped format). Write the date in `running-notes/ad-naming.md` or `running-notes/brand-rules.md`
2. **Old ads get their tags in a file, not a new name.** Their tags go into `angle-bank/ad-tags.csv`, from `ad-breakdown` (tag_source `breakdown`) or from a read of the ad (tag_source `read`, labelled Inferred). The leaderboard then lists them as names that don't parse, which is expected for old ads
3. **Renaming live ads is the team's call.** `creative-leaderboard` can write a CSV of suggested names (`processes/naming-setup.md` in that skill). Whether to rename, and when, is decided by a person, who does it by hand in Ads Manager. Claude never renames anything in the ad account; the account access is read-only

## Examples

**Video.** A creator talks to camera, opens on the thing the viewer uses now, problem aware, second hook, first cut:

```
261107_C07_A03_P2_PA_ugc-talk_creator_enemy_H2_v1
```

The same script said by a vet, as a new cut:

```
261107_C07_A03_P2_PA_ugc-talk_expert_enemy_H2_v2
```

A song ad on a new concept, for unaware viewers, persona not chosen, with a length tail:

```
261114_C11_A06_x_UN_song_song_story_H1_v1_30s
```

**Static.** A benefit headline with no speaker, solution aware, symptom call out:

```
261107_C08_A01_P1_SA_static-benefit_none_symptom_H1_v1
```

An offer static for the most aware, on the second run of a concept:

```
261121_C07-2_A04_P1_MA_static-offer_none_offer_H3_v1
```
