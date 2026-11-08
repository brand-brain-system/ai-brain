# Dreaming

The assistant thinking on its own between sessions. The `/dream` routine reads the day's conversations, and any connected comms, against everything in this brain, and comes back with suggestions. It proposes; it never applies anything by itself.

## What lives here

- `runs/[YYYY-MM-DD]/`: what each run noticed.
- `proposals/pending/[YYYY-MM-DD]-[id].md`: suggestions waiting on a decision, each with its reasoning. They cover six kinds of thing: updates to the brand's docs, skill improvements, schedules worth setting up, ideas worth chasing, new open questions, and what the assistant now understands about the person it's working with.
- `proposals/applied/` and `proposals/dismissed/`: where a proposal moves once the weekly `/self-improve` routine and the team decide on it. A dismissed one keeps its reasoning, so a rejected idea still teaches the assistant what doesn't land.

The method is in `brain-system/self-improvement/dreaming-system.md`.

A new brain starts with this folder empty.
