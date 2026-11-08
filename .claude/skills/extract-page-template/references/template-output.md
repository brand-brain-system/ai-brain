# Template extraction output

## Source breakdown

- Source URL or file
- Access date
- Capture coverage: desktop, phone, interactive states
- Page type
- Likely traffic and awareness stage; label inferred assumptions
- Above the fold
- Section-by-section flow
- Proof stack
- Offer and urgency mechanics
- Mobile adaptations
- What appears to work structurally
- Watch-outs and source-brand dependencies

## Match decision

Choose one:

- `Existing template: <id>` — same underlying contract; add as a reference only when requested.
- `Candidate template: <working name>` — materially different structure; not yet promoted.

Name the closest existing template and the exact structural differences.

## Contract JSON

Use this shape so an approved candidate can move into the shared `templates/INDEX.json` without translation:

```json
{
  "id": "candidate",
  "name": "Plain-language name",
  "slug": "lowercase-hyphenated",
  "status": "candidate",
  "use_when": "The traffic, buyer and job this structure serves",
  "teep": "Exploration to Evaluation",
  "requires": ["inputs that must exist"],
  "nice_to_have": ["proof or assets that improve it"],
  "urgency_device": "none unless real",
  "story": "Why the sequence works without source-brand claims",
  "refs": [
    {"brand": "Source brand", "url": "https://...", "captured": "YYYY-MM-DD", "screenshot": "path"}
  ],
  "sections": [
    {
      "id": "s01",
      "type": "supported component",
      "required": true,
      "job": "One sentence",
      "guide": "What to write, item and word limits, and proof requirements"
    }
  ],
  "adaptation": ["What to do when an optional input is absent"],
  "watch_outs": ["Failure modes exposed by the source page"]
}
```

Component names should match the shared builder. If none fits, describe the required component and its behavior; do not silently substitute a visually similar block with a different job.

