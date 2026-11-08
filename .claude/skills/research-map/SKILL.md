---
name: research-map
description: Organise customer research into a ranked, clickable map (research-map, research map, voice of customer map, organise research, rank pain points, belief map, quote bank, evidence page). Every quote is saved once with its source link; quotes are grouped into layers (situation, symptom, belief, desire, product experience, trigger); each group is ranked by how many different people said it, and clicking a group shows the exact quotes with an "open original" link. One self-contained HTML page the team can open. Use when someone has pulled reviews, Reddit or forum posts, comments or survey answers and wants to see what customers say most, back personas with data, or check the quote behind a claim. Feeds persona-gap Mode A.
---

# Research map: ranked by data, every line traceable to a quote

The page answers one question: **how many different people said this, and what exactly did they say?** A
persona, a hook or a headline that rests on a group can be checked by anyone in two clicks.

Run inside the brain. Input is `source-pulls/` (verbatim posts with source, date, id); output is
`research-map/` in the brain.

## Files

| File | What it holds |
|---|---|
| `SKILL.md` | The steps (this file) |
| `strategy.md` | Layers, grouping rules, what counts |
| `scripts/build-map.py` | Counts and writes `map.html`. Stdlib Python, no install |
| `feedback.md` | What we've observed. A log, not a rulebook |

## Steps

**1. Pull and keep the unweighted pull apart.** Same rule as persona-gap A1: a pull that searched for a
keyword shows the language, never the share. Each quote row carries `pull`: `unweighted` or `searched`.

**2. Save one row per quote** in `research-map/evidence.jsonl` (format in `strategy.md`). Quotes are
short (under 15 words where you can), copied word for word, with the link to the original post. `author`
is a hash of the poster, never a handle or a name.

**3. Propose the groups and show them to the human before any number is shown.** Read the compact
one-line-per-post file, then write `groups.json`: layers, and a title for each group in the customer's own
framing ("It's salt or diet", not "Dietary attribution"). Grouping is a judgement, so the human approves
or merges groups first. A group is a statement someone could say yes or no to.

**4. Tag each quote to a group.** One group per quote per layer. A post that holds a belief and a desire
gets one row in each layer, same author.

**5. Link desires.** Desires are the spine: for each situation, symptom, belief and product experience,
list which desires it connects to (`desires` in `groups.json`). Only link when quotes show the connection.

**6. Build.**

```
python3 brain-system/.claude/skills/research-map/scripts/build-map.py research-map
```

It prints the top groups and every warning (unknown group, missing source, a group backed by fewer than two
people). Fix warnings or leave the group as a lead for `hypotheses/`.

**7. Audit.** The persona-gap A5 agent, who didn't write the groups, gets `evidence.jsonl` and the source
files: does each quote exist word for word in the source, and does it belong in its group? Wrong ones are
moved or deleted, not explained away.

**8. Read it with the human.** Say what the top group in each layer is, what is missing (layers with few
groups mean the data didn't ask), and the limit. Then personas (persona-gap A3-A4) are built from the map:
a persona is a situation + belief + desire that real people share, and the card cites the groups.

## Limits stated on the page

Posts are not customers. Counts are different people in one pull, not a share of the market. Reddit
over-represents people with a problem; Trustpilot over-represents online buyers. Say which way it pulls.

## Privacy

The brain is private, but quotes are still personal data (GDPR). Store the hash, not the handle; do not
publish `map.html` or the evidence file outside the team, and anonymise before it goes in a pitch.
