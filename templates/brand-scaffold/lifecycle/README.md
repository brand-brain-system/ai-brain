# Lifecycle

This README explains the folder. It is not one of the folder's docs, so leave it out of any list or index of them.

The brand's email and SMS program: how consents are collected, which flows run on which legal basis, the drafts, and what they earned.

## What lives here

- `consent-audit.md`: every place an email or phone number is collected, the exact consent text, a dated screenshot, and whether it holds under the Danish rules
- `flow-map.md`: every live flow with trigger, timing and legal basis, and the ranked list of missing flows
- `flows/<flow>/`: one folder per flow: the flow sheet, every email and SMS, and `setup.md` (what was built in the platform, as a draft)
- `results.md`: per flow and message, after 30 and 90 days, with the platform's numbers read as claims

The `lifecycle-flows` skill writes these (`brain-system/.claude/skills/lifecycle-flows/`). The Danish rules it checks against are in its `dansk-lovgivning.md`. Customer lists and personal data stay in the email platform, never here.

A new brain starts with this folder empty.
