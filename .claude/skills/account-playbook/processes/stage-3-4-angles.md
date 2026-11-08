# Stages 3 and 4: market mining, personas, the angle bank and the gap matrix (days 3-12)

The net-new angle that opens the next level of spend comes from what customers say, not from
rivals' ads. Stage 3 collects it word for word; Stage 4 turns it into angles and shows which ones
the account has never said. The method is in
`brain-system/creative-strategy-context/angle-discovery.md`.

## Stage 3: market mining and personas (days 3-10)

### Entry criteria

- The brain is built. Nothing else: this stage needs no account data, so it can start on day 1 or
  before access arrives

### Calls

1. `angle-bank`, process `mine-market`: reviews, Reddit and forums, TikTok and ad comments,
   support tickets, post-purchase surveys, through the routes in `tool-map.md`. Quotes are saved
   word for word with their source. It routes on to the two skills below; run them through it,
   not a second time
2. `research-map`: the quotes grouped and ranked by how many different people said them. Its own
   stop: a person approves the groups before the page is built
3. `persona-gap` Mode A, only if personas aren't evidenced yet: `personas/personas-profile.md` is
   missing, still the scaffold's empty cards, or has cards without quotes and labels. Otherwise
   mark it skipped with that reason
4. `persona-gap` Mode B, twice:
   - **Own ads against the personas:** the account's ads (Stage 2 tags where they exist), tagged by
     persona and awareness. Shows which personas the account never speaks to
   - **The competitor ad read:** the main rivals from `competitors/_competitive-set.md` in the
     Meta Ad Library. What they run is Verified; their ranks are proxies. When the question is how
     a rival grew, not just what it runs, offer `competitor-teardown`

### Outputs

New dated files in `source-pulls/`, `research-map/evidence.jsonl` and `research-map/map.html`,
`personas/personas-profile.md` (if Mode A ran), and the Mode B files in
`audits/<YYYY-MM>/persona-gap-<YYYY-MM-DD>/`.

### Stops

- The strategist approves the research-map groups
- Mode A's cards go through its independent audit before they are used

### Exit check

- [ ] A quote bank exists with an open-original link for every quote
- [ ] Personas are evidenced: every card has quotes and labels, and passed the audit
- [ ] Own and rival ads are tagged against the personas

## Stage 4: angle bank and gap matrix (days 7-12)

### Entry criteria

- Stage 3 is done
- Stage 2 is done, or skipped with a reason (then the account side is Inferred, from Mode B)

### Calls

1. `angle-bank`, process `build-bank`: every angle in `angle-bank/angles.csv` with a persona, an
   awareness level and the customer quote behind it
2. `angle-bank`, process `map-account`: the account's ads from `angle-bank/ad-tags.csv` laid onto
   the angles
3. `angle-bank`, process `gap-matrix`: angles against awareness levels, live cells against empty
   ones, and the top 5 gaps

### Outputs

`angle-bank/angles.csv`, an updated `angle-bank/ad-tags.csv`, and
`angle-bank/gap-matrix-<YYYY-MM-DD>.md` and `.html`. Copy the top 5 gaps to the status page, each
with its angle ID.

### Stops

The strategist reads the matrix and agrees the top 5 gaps, or changes them. Their call wins; note
the change and the reason on the status page.

### Exit check

- [ ] Every angle has a persona, an awareness level and a quote with a source
- [ ] The gap matrix is saved, with its date and labels
- [ ] The top 5 gaps are on the status page, agreed by the strategist
