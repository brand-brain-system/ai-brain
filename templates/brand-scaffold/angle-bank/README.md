# Angle bank

This README explains the folder. It is not one of the folder's docs, so leave it out of any list or index of them.

The brand's angles, one line each, and every ad in the account tagged by angle, persona and awareness level, so the team can see which messages the account has scaled on and which ones the buyers have never heard.

## What lives here

- `angles.csv`: one row per angle. One angle is one reason to buy (a problem, a desire or a belief), said in one line, with the personas and awareness levels it fits, the enemy it blames, the best customer quote with its source, how many different people said it (`evidence_people`) and its status (`idea`, `briefed`, `live`, `won`, `lost`, `retired`).
- `ad-tags.csv`: one row per ad above the spend floor from the last account read, with its numbers, whether it is a winner by the brand's own definition, and its tags. `tag_source` says where a tag came from (`name`, `breakdown` or `read`) and `label` how sure it is.
- `gap-matrix-YYYY-MM-DD.md` and `.html`: angles x awareness and personas x awareness, with won, live, lost and never-tried cells, and the share of winner spend by angle. Built by `brain-system/.claude/skills/angle-bank/scripts/gap_matrix.py`.

The `angle-bank` skill writes these (`brain-system/.claude/skills/angle-bank/SKILL.md` has the columns and the steps). The quotes behind each angle live once in `research-map/evidence.jsonl` or `source-pulls/`; `quote_source` points there. Ideas the bank suggests go to `idea-bank/`, and picked ones become concepts in `idea-bank/concepts.md`.

A new brain starts with the two CSV files holding their header rows only.
