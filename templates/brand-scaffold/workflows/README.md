# Workflows

Recurring jobs handed to the hosted the assistant product, which runs them through the the assistant connection. A workflow is not the same thing as a schedule: a schedule (`../schedules/`) runs inside this folder in a Claude Code session and keeps the brain's own docs fresh, while a workflow lives on the assistant's side.

## What lives here

- `[workflow-slug].md`: an active workflow. Each file names the task, the cadence, the sources it reads, the skills it uses, what it delivers, its status, and where the idea came from.
- `proposed/[workflow-slug].md`: workflows the dreaming run suggested, waiting on the team to say yes. A proposed workflow doesn't run until it's confirmed and moves out of `proposed/`.

The difference between the two is spelled out in `brain-system/system/schedules.md`.

A new brain starts with this folder empty.
