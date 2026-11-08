# Decide one home per item

## Input

`coverage.md` from `map-against-factory.md`. Skip the covered claims unless the source adds a sharper example.

## Steps

1. **Group the partly covered and new claims** into items. An item is one thing to build: several claims that belong together become one method doc or one skill.
2. **Pick the one home for each item.** A rule lives in one file; other files point to it (factory `CLAUDE.md` rule 2, `system/system-of-records.md`).

   | The item is... | Home |
   |---|---|
   | A name for something the team should say the same way | `creative-strategy-context/creative-vocabulary.md` (one entry) |
   | A way to think or decide that many skills use | A method doc in `creative-strategy-context/`: frontmatter `summary` of at most 240 bytes, a Source / Users / Status block like `yapper-ads.md` |
   | A job with its own inputs, steps and output, run on request | A new skill in `.claude/skills/<name>/` (SKILL.md, strategy.md, processes/, feedback.md) |
   | A new way to do a job an existing skill already does | A new process in that skill's `processes/`, routed from its `strategy.md` |
   | Something the factory already says elsewhere | A pointer: one line in the right file, pointing to the home |
   | A file every brain must keep (a log, a bank, a status page) | A template in `templates/brand-scaffold/` |
   | A count, a parse, a check a person would do the same way every time | A script (Python 3 standard library, `argparse`, UTF-8, works on Windows) with a test in `tests/` |
   | A claim we haven't seen hold | An open test in a skill's `feedback.md` |

3. **Sort rules from methods to try.** Rule 6: a new rule goes in `feedback.md` first and moves into the rules only after it held on a second brand. So:
   - **Method to try**: a way of working, offered as an option ("the sprint plan can offer this setup"). It may ship in a method doc or skill, labelled Stated, with its open test logged
   - **Rule**: a must or must not that changes what a skill does every time. It ships as an open test in `feedback.md` only, with what to log and what would count as holding
   - A legal or platform rule that is written down by the authority (Danish law, Meta policy) is not a rule-6 rule; it goes to its existing home (`ad-policy-check`, the Danish sections)
4. **Check the catalog cap.** Every new method doc adds a row to the craft catalog that brains inject on every turn. The map's header shows the headroom. If new rows would go over, shorten
   summaries, or fold a small doc into an existing one. The check is `tests/test_runtime_hooks.py`.
5. **Ask the owner the few real questions** through the question form (AskUserQuestion), not as chat text. At most four, each with options and the recommended one first. Good questions are
   ones only the owner can answer:
   - **Access**: is there a route to the data the method needs (an ad account connection, an export, a tool)? Read-only only
   - **Scope**: all of it in one release, or the core first?
   - **Visuals**: does a result need a page (HTML, an artifact), or is markdown enough?
   - **Naming or conventions** the team already uses that the build must keep
   Don't ask what the factory already answers (`CLAUDE.md`, `system/`).
6. **Write the plan** as one table: `item | home (path) | new or edit | rule or method to try | claims (ids)`. Add what was left out and why.

## Output

`plan.md` in the scratchpad, shown to the owner in chat with the answers folded in.

**STOP.** The owner approves, changes or cuts the plan. Nothing is built before that.
