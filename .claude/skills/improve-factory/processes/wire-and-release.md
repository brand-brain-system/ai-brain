# Wire it in and release it

## Input

The new files from `build-with-agents.md` and the list of proposed edits to existing files. The lead does all of this; builders don't.

## The checklist

Tick each line or write "n.a." and why. Run from the factory root.

**Wiring**

1. [ ] Apply the builders' proposed edits to existing files, merged by hand where two touch one file.
2. [ ] `system/skills-catalog.md`: one row per new or changed skill (Does / Deliberately doesn't / Status). New skills are **Written** until they have run on real or test-brand work.
3. [ ] Method docs: `python scripts/build-doc-map.py`, then `python scripts/build-doc-map.py --check` (must say current). Every new doc has a `summary` of at most 240 bytes.
4. [ ] **Craft catalog byte cap**: the map's header line (`python scripts/factory-map.py --section docs`) shows the injected size against 16,000 bytes. It must say "fits". The test that
   enforces it is `tests/test_runtime_hooks.py` (`test_full_catalog_and_profile_budget`). Over the cap, shorten summaries, never raise the cap.
5. [ ] Pointers: every existing doc or skill that should send people to the new home has its one line (one home per rule: point, don't copy). Skills route new processes from `strategy.md`
   and `processes/INDEX.md`.
6. [ ] Brain files: a file every new brain needs gets a template in `templates/brand-scaffold/`. If the brain tree changed, update `system/master-file-structure.md`.
7. [ ] Data routes: if a skill reads data in a new way, update `templates/brand-scaffold/tool-map.md` and `system/data-access.md` (and `system/tool-roles.md` for a new role).
8. [ ] Factory-only skills (this one, and any skill that must never run in a brain) are excluded from the brain sync in `bundle_map()` in `scripts/sync-executable-layer.py`, which
   `scripts/scaffold-brain.py` also reads. If the shipped list changed, update the description in `prompts/onboarding-runner.md` (Phase 0 step 5).
9. [ ] Outside material: credited in `NOTICE.md` and the right `third-party/*/MANIFEST.md` when it came from a licensed repo or from Parker. Practitioner posts need no name credit (the
   owner decided); they are labelled Stated.
10. [ ] `REWRITE-QUEUE.md`: move what shipped to "done" or note it in its section; add what was left out or proposed for later as a new numbered section.

**Checks**

11. [ ] Tests: `python -m pytest tests -q`. If pytest is not installed, `python -m unittest discover -s tests` runs the same files. All pass. A new script has its own test.
12. [ ] Voice: `python scripts/voice-lint.py <file>` on each new prose file. The lint is built for creative copy, so judge each flag: fix the real tells (em dashes, filler, chatbot residue),
    leave flags that are quoted examples or method names.
13. [ ] No brand names, no customer quotes, no account data in any changed file. Grep for the test brands' names before committing.

**Release (CLAUDE.md rule 5)**

14. [ ] `migrations/vN.md` in the four sections `migrations/README.md` asks for, like `migrations/v19.md`: **What changed** (one paragraph and a short list), **Steps for a brain**
    (numbered, exact files; move the pin, run `python3 brain-system/scripts/sync-executable-layer.py --from v(N-1)`, add any new scaffold file, "Nothing else" when that is true),
    **Check** (a command or a thing to look at), **Why** (the lesson behind the change).
15. [ ] `release-notes/vN.md`: a dated heading for the batch, then one block per new piece and per changed file, like `release-notes/v19.md`.
16. [ ] `VERSION` holds `vN`.
17. [ ] `python scripts/check-release.py vN` passes (VERSION, both notes and the tag name agree).
18. [ ] Commit with a message like `vN: <the two or three main pieces>`. Push to GitHub without asking (the owner wants pushes done).
19. [ ] **STOP. Ask the owner before creating the tag `vN`**, and before any force push or merge. On a yes: `git tag vN`, `git push origin vN`. Brains see the release at their next
    `update-brain`.
20. [ ] If the release changed the workflow, run `visual-map.md`.

## Output

A pushed commit, a tag after the owner's yes, and a short report to the owner: what shipped where, what was left as an open test, what is left for later.
