# Update the visual workflow map

## When

Only when the release changed how the work flows: a new skill, a new step between skills, a new brain file that a skill writes and another reads, or a changed order. A new method doc
that no skill's order depends on does not need it.

## Input

`system/workflow-map.html` (the visual page of the factory's workflow, published since v20 at https://claude.ai/artifact/SNrfEJAaYtfT5DynghVsDj, private to the owner), the release's new pieces, and the map (`python scripts/factory-map.py --section skills`).

## Steps

1. **Read the page as it is.** If it was published as a claude.ai artifact, read the published version too (Artifact tool, `action: "read"`), in case it was changed there.
2. **Change only what moved.** Add the new skill or step where it sits in the flow, with its inputs and outputs (the brain files it reads and writes). Keep the page's layout, colours and
   names as they are.
3. **Check every name against the repo.** Each skill on the page exists in `.claude/skills/` (or the routine bundle), each brain path exists in `templates/brand-scaffold/` or is made at run
   time by a skill that says so.
4. **Look at it** at desktop and phone width in a browser before publishing.
5. **Republish** it to the same artifact URL (Artifact tool, publish with the `url`), so the owner's link keeps working. Commit the HTML file in the factory with the release.

## Output

The updated `system/workflow-map.html` in the release commit, the artifact link republished, and the link in the report to the owner.

## Rules

- The page shows the method, never a brand's data.
- Prices, accounts and live numbers never appear on it.
