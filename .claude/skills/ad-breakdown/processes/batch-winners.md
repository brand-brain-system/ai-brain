# Process: batch of winners

Break down the account's own winners together, to see what the account actually scales on. Often it is fewer angles
than the team thinks: one practitioner reports accounts that scaled on only one to three core angles, with whole
personas and awareness levels never tried (Stated, a practitioner's post, Nov 2026). This process checks that on our
own numbers, and writes the tags the angle bank and the leaderboard read.

Our own account only. A competitor's ads have no spend data, so there is no "winner" to batch; use `persona-gap` Mode
B for those.

## 1. Set the bar and the set

- **The winner bar** comes from `running-notes/success-definition.md` and `running-notes/brand-rules.md` (the KPI, the
  target CPA or ROAS, a minimum spend if the brand has one). Quote it in the batch file's header. **Never invent a
  bar.** If there isn't one, ask the person for it. If they don't give one, run on the top spenders, call them "top
  spenders, not winners" everywhere, and write `is_winner` as `x`
- **The default set:** the top 10 ads by spend in the last 90 days that meet the bar. The person can change the window
  or the count. Fewer than 10 meet it: take those, and say how many
- **Pull** at ad level through the account route in `../SKILL.md`, step 3: spend, results, CPA, ROAS, hook rate, hold
  rate, CTR, frequency, launch date, days live, and the ad name. Write the source, the date range, the pull date and
  the attribution setting once in the header. If the numbers look odd (Meta far from the store), run
  `ad-account-analysis` `measurement-check` before going on
- **Twins:** ads with the same creative and a different headline or copy count as one. Break down the one with most
  spend and write how many twins it has and their total spend
- **Show the list and the cost before going on.** The ads, their spend, video or static, the total video minutes and the
  transcription price from `get_pricing`. Wait for a yes

## 2. The strategist's read

Ask once for the account, before anything is shown: "Which one to three angles do you think we scale on, and on whom?
Anything you expect to be missing?" Then the four questions in `../SKILL.md`, step 2, for the top 3 by spend only.
Record skips as "No hypothesis given".

## 3. Gather, one small agent per ad

Get each creative and transcribe each video as in `../SKILL.md`, steps 3 and 4, into
`audits/breakdowns/_media/YYYY-MM-DD-batch/<ad-slug>/`. Then spawn one `gather` agent per ad, in parallel, so the raw
transcripts stay out of the main context. Hand each one the transcript (`transcript.md`), the frames or the image, and
the ad's row from the pull, and ask for these fields back, quoted exactly with timestamps:

- length, aspect ratio, video or static
- the first spoken line, the first on-screen text, what the first frame shows
- who speaks (creator, expert, customer, founder, voiceover, song, skit, AI, none)
- the first second the product or brand is named or shown
- every line that blames something (the old fix, a cheap copy, a habit)
- every line with "because", or that explains why something works or fails
- every proof element (a personal result, a number, an expert, a demo, a timeline, a taste reaction)
- the last 10 seconds: the CTA words, any offer, any guarantee
- for a static: all text verbatim, and the order the elements sit top to bottom

The agent extracts; it doesn't tag or judge. The main session does the tagging from the briefings.

## 4. Light pass on every ad

For each ad, from its briefing (open the transcript or image only where a briefing is unclear):

- the transcript or inventory (it goes into the batch file, folded under the ad's heading)
- the tag block and the pattern check from `../breakdown-template.md`
- **Why it won, in five lines**, each tied to a tag or a timestamp

That is the light pass named at the end of `video-breakdown.md` and `static-breakdown.md`.

## 5. Full pass on the top 3

The top 3 by spend get the full video or static breakdown, each in its own file
(`audits/breakdowns/YYYY-MM-DD-<ad-slug>.md`), with "Your read vs the breakdown" against the per-ad hypothesis. The
batch file links to them.

## 6. What the account scales on

The cross-ad summary, in the batch file. Count both ways: number of ads, and share of the set's spend. Spend share is
the truth; counts only show variety.

| Field | What to show |
|---|---|
| Angle | Each angle, its ads, its spend share. **The core-angles check:** the share of winner spend on the top 1, 2 and 3 angles. Name them |
| Persona | Each persona, its spend share, and the personas in `personas/personas-profile.md` with no winner at all |
| Awareness | Spend share per level, and the levels with no winner |
| Shape | The five shapes and `other`, with ads and spend share |
| Voice | Who speaks. One voice on most of the spend means Meta may see one ad in many outfits (`brain-system/creative-strategy-context/andromeda-v2.md`) |
| Format | Ads and spend share per format |
| Hook family | Ads per family |
| Patterns | How many name a specific enemy, open on the problem, give one mechanism. Compare with `winning-script-patterns.md`, without restating its numbers |

Then three short paragraphs, each labelled:

- **What the account scales on:** the angles, personas, awareness levels, shapes, voices and formats that carry the
  spend (Verified for the spend, Inferred for the tags)
- **What is missing:** personas, awareness levels and shapes with no winner. These are questions, not verdicts: an
  empty cell may never have been tried, or tried and lost. Check `angle-bank/angles.csv` and the loser breakdowns
  before calling it a gap. The full angle by awareness gap map is the `angle-bank` skill's job; hand it over
- **Proven angles in new formats, new angles on proven formats:** two or three concrete pairs from the table (a winning
  angle that has only run as UGC, the format that carries most spend), for the next brief

Close with "Your read vs the breakdown" for the account-level hypothesis.

## 7. Writing ad-tags.csv

The rules for every process that writes a tag row. Only our own ads get a row.

- File: `angle-bank/ad-tags.csv`. If it is missing, create it with exactly this header line:
  `ad_id,ad_name,launch_date,spend,results,cpa,roas,is_winner,concept_id,angle_id,persona_id,awareness,format,voice,shape,hook_family,enemy,mechanism,proof,close,product_at,tag_source,label`
- One row per ad, `tag_source` = `breakdown`. If a `breakdown` row for the same `ad_id` exists, replace it and say so.
  Leave rows from other sources (`name`, `read`) alone
- Values as in the tag block. Unknown is `x`. `launch_date` as `YYYY-MM-DD`. Numbers as pulled, decimal point, no
  currency sign (the currency is in the batch file's header). `is_winner` is `yes` or `no` against the brand's bar, `x`
  with no bar. `label` is `Inferred` (the tags are a reading of the ad; the numbers' source is in the breakdown file)
- Write with Python's `csv` module, UTF-8, so a comma inside `enemy` or `ad_name` is quoted
- `sophistication`, `ladder_start` and `funnel` stay in the breakdown file; the CSV has no column for them
- A new angle with no `angle_id`: write `x` and list it under next steps for `angle-bank` to log. Never make up an id

## Where it goes

- `audits/breakdowns/YYYY-MM-DD-batch-winners.md`: header (bar, window, source, attribution, currency, hypotheses),
  the set with spend, one light-pass section per ad, the summary, "Your read vs the breakdown", next steps
- The three full files, and the rows in `angle-bank/ad-tags.csv`
- Next steps as in `../SKILL.md`, step 10. Usually: `angle-bank` to log the angles and run the gap map, then
  `iterations` on the top winner and `scriptwriting` or `static-ads` for a proven angle in a new format
