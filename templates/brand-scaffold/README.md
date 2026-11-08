# {{BRAND_NAME}}: brand brain

This is {{BRAND_NAME}}'s brand brain: the folder the assistant thinks with. It is set up but not built yet. The method, the skills and the routines are here; the brand's own knowledge (the audit, the
customers, the competitors, the strategy) hasn't been written yet.

## Where to start

- **Build it.** Open this folder in Claude Code and run `/set-up-brain`. It settles which data the brand can give (exports, public pages, connected tools), asks a few questions only the team can
  answer, and builds the rest. It takes a few hours, mostly on its own, and `BUILD-STATUS.md` shows where it is
- **Or just start talking.** The brain works while unbuilt: it reads what the team gives it and saves what it learns into `running-notes/` and `brand-lens.md`, so it starts filling in from day one
- **Want the tour?** Run `/get-started` any time

## What's here now

- `CLAUDE.md`: how the assistant works in this brain
- `brain-system/`: the shared method library (prompts, craft knowledge, system docs), mounted read-only and pinned to a release
- `.claude/`: the skills, hooks and settings; the folder README files say what each folder will hold
- `tool-map.md`: which tool fills each role for this brand, and the data routes
- `running-notes/`: current work, what the brain doesn't know yet, and the brand's rules

## Sharing

This brain is a git repo the whole team shares. Pull before you start, commit small and push when you're done (`/save-brain` has the procedure).
