# Weekly brain report: the data file

One JSON file per report. Every top-level key except `meta` is optional; a missing section is left out of the page. Text accepts `**bold**` and `*italic*`. `label` is one of `Verified`, `Stated`,
`Inferred`, `Data-limited`. `example.json` is a complete file.

| Key | Holds |
|---|---|
| `meta` | `brand`, `kicker` (the pill on top), `week_label`, `date_range`, `accent` (a hex colour), `concept_label` (footer, e.g. "Concept, not commissioned by <brand>"), `prepared_by`, `example` (true shows the red example banner: leave it out in a real report) |
| `headline`, `intro` | The title after the brand name, and one or two sentences under it |
| `key_points` | Three cards: `title`, `body`, `label`. The short version: read this and nothing else |
| `account` | `summary`; `working` and `dying`: lists of `{title, detail, label}`; `note` (the yellow structural callout). No export: `{"data_limited": true, "needs": "an ad-account export in source-pulls/"}` |
| `competitors` | `summary` and `cards` (`title`, `body`, `label`), or `data_limited` + `needs` |
| `voice` | `summary` and `items`: `{theme, quote, source, note, label}`; the quote is exact, with source and date; or `data_limited` + `needs` |
| `openings` | `summary`; `organic` and `affinity`: `{title, intro, items: [{text, label}], callout}` (use `callout` for the "do not chase" list) |
| `next` | `summary` and `concepts`: `{name, persona, angle, why, label, verdict}` |
| `judging` | Optional: `title`, `summary`, `judges: [{name, text}]`, `died` |
| `limits` | A list of plain sentences: what the report couldn't see |
| `sources` | `{name, what, date}` for every source used |

Rules for the writer: numbers carry their window; quotes are never shortened; one `label` per claim; a section you can't fill honestly is marked `data_limited`, not padded.
