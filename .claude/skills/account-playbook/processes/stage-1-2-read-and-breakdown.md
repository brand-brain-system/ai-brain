# Stages 1 and 2: the account read and the winner breakdowns (days 1-5)

## Stage 1: account read (days 1-3)

### Entry criteria

- Stage 0's measurement read is "usable" or "usable with a caveat"
- The winner definition and north star are written

### Inputs

The newest `source-pulls/ad-account-<date>.csv` or the MCP route, the measurement read and its
caveat, `running-notes/brand-rules.md`.

### Calls

1. `ad-account-analysis`, process `account-audit`, on the last 90 days. Ask the run to cover three
   things this playbook needs later, each as a short section in the audit:
   - **Winners by the brand's own definition,** listed with spend and dates. This list feeds
     Stage 2
   - **Structure:** how the campaigns and ad sets are built, set beside the setup in
     `brain-system/creative-strategy-context/meta-full-funnel-cbo-playbook.md`. That doc is one
     practitioner's setup (Stated), an option to compare with, not a target. Write the
     differences, not a verdict
   - **Spend level:** the monthly spend, the band it falls in
     (`brain-system/creative-strategy-context/creative-strategy-by-brand-size.md`), and how many
     new ads a month it needs (`brain-system/creative-strategy-context/creative-volume.md`, "How
     many ads"). Say which method gave the number
2. If the audit flags a fatigue signal on a top spender, `account-audit` hands on to
   `fatigue-diagnosis` itself. Let it

### Outputs

`audits/<YYYY-MM>/account-audit-<YYYY-MM-DD>.md`. Copy the spend band and the monthly ad target to
"Account facts" on the status page, with a link to the audit.

### Stops

None, unless the measurement read was "not usable", in which case this stage does not start.

### Exit check

- [ ] The audit is saved, labelled, and carries the measurement caveat if there was one
- [ ] It names the winners by the brand's definition (or says there are none)
- [ ] It has the structure note, the spend band and the monthly ad target

## Stage 2: winner breakdowns (days 2-5)

### Entry criteria

- Stage 1 is done and lists the winners. No winners: see `../strategy.md`, entry point A

### Calls

1. `ad-breakdown`, process `batch-winners`. It asks the strategist for their own read before it
   shows its own. That is this stage's stop: a person thinks first, then the breakdown shows what
   they missed. If the strategist skips it, note "no own read" on the status page
2. When the batch is done, put its answer to "what the account scaled on" on the status page in
   three lines or fewer, with a link to the batch file

### Outputs

`audits/breakdowns/<YYYY-MM-DD>-<ad-slug>.md` per ad, rows in `angle-bank/ad-tags.csv`, and the
"What the account scaled on" box on the status page.

### Stops

The strategist's own read, before each full breakdown is shown.

### Exit check

- [ ] Every winner in the batch has a breakdown file and a row in `angle-bank/ad-tags.csv`
- [ ] "What the account scaled on" is written: the angles, personas, awareness levels and
      formats that carried the spend
