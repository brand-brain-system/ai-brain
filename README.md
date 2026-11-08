# Brand Brain (v22)

A system of Claude Code skills for performance creative: research, strategy, ad production, checks, measurement and learning, built for DTC brands in the Danish market.
51 skills, 61 method docs.

This is a frozen public snapshot of version v22. The working version is developed privately; newer snapshots are published here from time to time.

## How it is used

The system is a **factory**. Each brand gets its own **brain** repo that mounts this one, read-only, as `brain-system/`:

    git submodule add https://github.com/brand-brain-system/ai-brain brain-system

`scripts/scaffold-brain.py` builds a new, empty brain. `system/factory-and-brains.md` explains how factory, brain and mount fit together, and `system/skills-catalog.md` lists every skill.
The skills live in `.claude/skills/`, the shared craft knowledge in `creative-strategy-context/`.

## What is not here

The swipe library's example images and the landing-page swipe file's screenshots and saved pages are other brands' work and are left out, so the skills that pick from them
(`static-ads`, `offer-ads`, `new-landing-page`) show the templates without their pictures.

## Credits and licences

See `NOTICE.md`. In short: large parts are built on Parker by Simple Labs (PolyForm Noncommercial 1.0.0, see `third-party/parker/`), on Alex Cooper's Adcrate material, and on MIT-licensed
open-source skills (see `third-party/`). Their credits stay in the files.
