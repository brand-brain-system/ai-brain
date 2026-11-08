# Search visibility

This README explains the folder. It is not one of the folder's docs, so leave it out of any list or index of them.

How AI assistants and search describe and recommend the brand to Danish buyers, measured from the outside, and what to fix.

## What lives here

- `prompt-portfolio.md`: the versioned list of questions buyers ask, grouped by topic, with two controls
- `runs.csv`: one row per answer (assistant, run, mentioned, recommended, rivals named, cited sources, wrong facts)
- `<date>/`: screenshots of the answers from that run
- `readout-<date>.md`: rates by topic and assistant beside the rivals, the source map, wrong facts, site findings
- `fix-list.md`: the ranked fixes, each routed to a skill or a person

The `ai-search` skill writes these (`brain-system/.claude/skills/ai-search/`), and its `scripts/tally.py` turns `runs.csv` into the rates. Compare runs only within one portfolio version.

A new brain starts with this folder empty.
