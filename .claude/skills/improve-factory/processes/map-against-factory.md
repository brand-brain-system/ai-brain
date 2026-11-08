# Map every claim against the factory

## Input

`claims.md` from `intake-sources.md`, and the factory map from step 0 (`python scripts/factory-map.py`).

## Steps

1. **First pass from the map.** For each claim, read the map's skill and doc lines and write down the two or three files most likely to cover it. Most claims land in a doc the map already
   names (`hooks.md`, `scriptwriting.md`, `iterations.md`, `andromeda-v2.md` and so on).
2. **Grep for the words, not only the idea.** Search for the claim's key terms and their synonyms across:
   - `creative-strategy-context/` (method docs and the swipe library)
   - `.claude/skills/` (SKILL.md, strategy.md, processes, feedback.md: open tests live in feedback.md)
   - `prompts/` and `system/`
   - `templates/brand-scaffold/` when the claim implies a file a brain keeps
   Use Grep with `-i` and `output_mode: files_with_matches` first, then read only the matching lines.
3. **Go wide with sub-agents when there are many claims.** Over about 15 claims, split them into groups and send each group to an `Explore` agent (or the `gather` agent for plain reading),
   with the claim lines and the folders above. Ask each agent for: claim id, files that cover it, the exact line or heading, and covered / partly / new / conflicts. Agents read; they don't
   decide homes.
4. **Classify each claim:**
   - **covered**: the factory already says this. Name the file and heading. Nothing to build, unless the source adds a sharper example
   - **partly covered**: the factory says some of it. Name where, and what is missing
   - **new**: nothing in the factory says it
   - **conflicts**: the factory says something else. Name the file and the line, and what each side rests on
5. **Check the open tests.** A claim may already be an open test in some `feedback.md`. If so, it is "partly covered" and the new source is a second voice for the same test, not a new rule.

## Output

The coverage table in the scratchpad, `coverage.md`:

| id | claim | status | where (file, heading) | what is missing or in conflict |
|---|---|---|---|---|

Show the owner the counts (for example "23 claims: 9 covered, 7 partly, 5 new, 2 conflicts") and the table. Conflicts get a line each on what the factory says and why.

## Rules

- "Covered" needs a file and a heading. A feeling that it's somewhere is "unknown": grep again.
- A conflict is never settled by the newer source winning. It goes to `decide-homes.md`, usually as an open test.
