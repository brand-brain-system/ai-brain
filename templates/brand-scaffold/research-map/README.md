# Research map

This README explains the folder. It is not one of the folder's docs, so leave it out of any list or index of them.

The customer research organised and ranked: every quote once, with its source link, grouped by layer (situation, symptom, belief, desire, product experience), each group counted by how many different people said it.

## What lives here

- `evidence.jsonl`: one quote per line, with source, link, date, a hashed author and which pull it came from
- `groups.json`: the layers, the groups and which desires they link to
- `map.html`: the page the team opens, built from the two files by `brain-system/.claude/skills/research-map/scripts/build-map.py`

The `research-map` skill writes these. The personas in `../personas/` cite the groups. Quotes are personal data: hashed authors only, and `map.html` stays inside the team.

A new brain starts with this folder empty.
