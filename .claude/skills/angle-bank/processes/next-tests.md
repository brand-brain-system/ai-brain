# Process: plan the next tests

Turn the top gaps into tests on the lowest-risk path, write them into the idea bank, and stop for the
strategist. Method: `brain-system/creative-strategy-context/angle-discovery.md`, step 6.

## 1. Pick the rung for each gap

Change one big thing at a time, so the result says what worked.

1. **A new angle on a proven format.** Take the account's best format, voice and shape from the share
   tables in the gap matrix (the winner spend by `format`, `voice`, `shape` in `angle-bank/ad-tags.csv`)
   and change only the angle
2. **A proven angle in a new format.** An angle with `won` status carried to a format it hasn't run in:
   a UGC winner as a static, a static's headline as a podcast clip or a song ad

Never a new angle on a new format in the first test: if it fails, nobody knows which half failed.

## 2. Write each test as an idea-bank entry

Follow the idea bank's format: one file per idea in `idea-bank/entries/YYYY-MM-DD-<slug>.md` with the
fields in `brain-system/.claude/skills/harvest-ideas/SKILL.md` ("Entry schema"), then a row in
`idea-bank/index.md`. For these entries:

- `source_type`: `angle-bank`
- `hunt_lane`: the cell, for example `gap matrix 2026-11-07, A03 at UN, P2`
- `source_path`: the gap matrix file and the angle row
- `idea`: the angle, the rung and the proven format it goes on, in one paragraph
- `justification`: the evidence from the gap proposal (people, persona weight, roadmap fit), with labels
- `stage_of_awareness` and `persona_or_audience_fit`: from the cell
- `status`: `raw idea`

The entry is an idea, not a brief: no scripts, variations or storylines inside it (the harvest-ideas
hard rules hold here too).

## 3. Stop: the strategist picks

Show the five proposals with their entries. Nothing is briefed, scripted or made until the strategist
picks. They may pick none; that is a result too, and the reason goes in the entry's `notes`.

## 4. When a test is picked

- **Register the concept.** It becomes a concept in `idea-bank/concepts.md` with the next free id, by
  that file's rules (it is usually the sprint plan that puts it there). The entry's index row gets
  "adapted into concept" and the id
- **Update the bank.** The angle's status goes to `briefed` in `angle-bank/angles.csv`
- **Route the making.** Scripts: `scriptwriting`, opening at the ladder step for the cell's awareness
  level (`brain-system/creative-strategy-context/awareness-script-ladder.md`). Statics: `static-ads`.
  Openers: `hooks`. Before launch: `ad-policy-check`
- **Name the ads** by `brain-system/system/ad-naming-convention.md`, so the next map-account reads the
  tags from the names. Renaming or launching in Ads Manager is the team's job
- **Size the test** by `brain-system/creative-strategy-context/creative-volume.md` and the register's
  rules; the test setup by `teep-creative-test-setup.md` or `meta-full-funnel-cbo-playbook.md` (both in
  `brain-system/creative-strategy-context/`)

The next monthly map-account reads how the test did and moves the angle to `live`, `won` or `lost`.
