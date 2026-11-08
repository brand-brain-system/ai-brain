# Research map: strategy

## Layers

Default set, from the research maps that inspired this (a health brand: what the shopper's body does, what
she thinks caused it, what she wants, what she tried). Rename or drop to fit the category; keep Desire.

| Layer | What goes in it | Test |
|---|---|---|
| Situation | What was happening, in her life or on the day | "When X happened…" |
| Symptom | What she notices or feels | Something her body or day does |
| Belief | What she thinks caused it or what she thinks is true | She says "I think", "it's", "must be" |
| Desire | What she wants, said, complained about, or asked | "I want", "I wish", "does anyone know how to" |
| Product experience | What she tried and how it went | Worked / failed / mixed / too early |
| Trigger (optional) | What made her go looking now | The moment right before the search |

A quote can sit in several layers (one row per layer, same author). Desire is the spine the page
filters on.

## What counts

- **A group's number is different authors in the unweighted pull.** Not quotes: one person who says it
  three times is one. Quotes from the searched pull show in the drawer, marked, and are never counted.
- **The percentage is of all authors in the unweighted pull** (the base), so it only means anything
  when the pull was unweighted. Say the base on the page (the script does).
- **Fewer than two people is a lead**, not a group to build on. It goes to `hypotheses/`.
- **Product experience groups** also carry an outcome per quote (worked, failed, mixed, too early) as
  `outcome` on the row; the page does not show the bar yet.

## Writing a group

Customer framing, one claim, a sentence she'd recognise. "She eats well and her BP still went up" beats
"Lifestyle-independent hypertension". Never merge two claims to raise a count. Split when a quote
contradicts its group ("it's salt" vs "it's not salt" are two groups, both counted).

## Evidence row

```json
{"id":"q012","group":"b-salt","quote":"I think it's the sodium.","source":"r/Perimenopause","url":"https://…","date":"2026-01-02","author":"a3f9","pull":"unweighted","outcome":""}
```

## `groups.json`

```json
{"meta":{"title":"…","unit":"women","lang":"en","desire_layer":"desire"},
 "layers":[{"id":"belief","label":"Belief","title":"What she thinks caused it","color":"#14434a"}],
 "groups":[{"id":"b-salt","layer":"belief","title":"It's salt or diet","note":"","desires":["d-nopills"]},
           {"id":"d-nopills","layer":"desire","title":"Wants it down without pills","short":"Without pills"}]}
```

`unit` is what the number counts ("women", "customers", "parents"). `short` is the chip label for desires.
`limit` in `meta` replaces the default limit sentence on the page.

## Not in v1

Showing outcome bars, automatic grouping, and fetching the posts. The grouping is the human-approved step
on purpose; fetching stays in persona-gap A1 (browser only, no login, no bot-check workarounds).
