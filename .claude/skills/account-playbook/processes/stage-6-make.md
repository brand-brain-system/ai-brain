# Stage 6: make (weeks 2-4)

Build each concept in the sprint plan. Shape first, voice second, then the making skill. Every ad
ends checked, named and handed to the team. Claude never launches.

## Entry criteria

- Stage 5 is done: the plan and the budget split are approved

## Per concept, in this order

1. **The brief.** Build it from the sprint plan's concept map with the brief-creation prompt,
   `brain-system/prompts/ideas-and-briefs/brief-creation.md`, into `sprints/<sprint>/briefs/`
2. **Shape first.** Pick one of the five shapes in
   `brain-system/creative-strategy-context/winning-script-patterns.md`, and the step the script
   opens on from `brain-system/creative-strategy-context/awareness-script-ladder.md`, matched to
   the awareness level of the gap the concept tests
3. **Voice second.** Then pick who says it. Spread the voices and formats across the round so
   Meta reads them as different ads (`brain-system/creative-strategy-context/andromeda-v2.md`).
   One shape can carry several voices
4. **Make it** with the skill for the format:

   | The concept needs | Skill |
   |---|---|
   | A spoken script (creator, expert, founder, customer, voiceover) | `scriptwriting`, then `hooks` |
   | Headlines or text overlays | `headlines` |
   | Statics | `static-ads` (`offer-ads` when there is a discount or a sale) |
   | Footage cut into ads | `video-edits` |
   | A static turned into motion, or hook and end cards | `motion-ads` |
   | AI video or AI image prompts | `ai-ad-generation` |
   | A song ad | `song-ads` |
   | A near copy of a reference ad | `recreate` |

   Each skill keeps its own stops (copy approval, picks, prices before generation spend)
5. **Creators, when the concept needs a person on camera.** `creator-recruitment` for the
   shortlist and the outreach drafts; the creator brief follows
   `brain-system/creative-strategy-context/creator-briefs.md`. Outreach goes out only after a yes
6. **`brief-check`** on raw footage (missing shots) and on every finished ad (spelling, claims,
   the brief delivered)
7. **`ad-policy-check` last,** on every finished ad, after every other change. An ad that comes
   back "fix" goes back to step 4 and through both checks again
8. **Name every ad** per `brain-system/system/ad-naming-convention.md`, or the brand's map in
   `running-notes/ad-naming.md`
9. **Hand off to the team:** a list in `sprints/<sprint>/ads/` with each file, its name, the
   campaign or ad set the plan puts it in, and its check results. The team launches

## Outputs

`sprints/<sprint>/briefs/`, the finished ads and the hand-off list in `sprints/<sprint>/ads/`, and
the round's angles marked `briefed` in `angle-bank/angles.csv`. When the team confirms the launch,
mark them `live` and write the launch date on the status page.

## Stops

- Every stop inside the making skills
- Outreach to creators, only after a yes
- **STOP before anything launches.** Claude never launches, uploads or schedules an ad. The team
  does, in Ads Manager

## Exit check

- [ ] Every ad in the round passed `brief-check` and `ad-policy-check`
- [ ] Every ad carries a name in the convention
- [ ] The hand-off list is in `sprints/<sprint>/ads/` and the team has it
- [ ] The launch date is on the status page once the team confirms it
