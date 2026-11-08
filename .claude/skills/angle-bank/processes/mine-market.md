# Process: mine the market

Mine the customers, not the Ad Library. A rival's ad shows what the rival thinks; a customer's own
sentence shows why people buy. This step gathers those sentences word for word. It is mostly routing:
the steps already have homes.

## Copy the words, not the topic

"I check the clock at 3 a.m. every night" is an angle waiting to happen. "Sleep problems" is a topic.
Save the sentence as it was written, with its source, date and id. A paraphrase is marked as one
(`brain-system/system/evidence-and-labels.md`).

## Where to look, and the route for each

The route for every source is in `brain-system/system/data-access.md`; which ones this brain has is in
`tool-map.md`.

| Source | What it gives that others don't |
|---|---|
| Reviews, all star ratings | Product experience; the low ratings carry the sharpest language |
| Reddit and forums | The problem before anyone bought: what they tried, what they blame |
| TikTok and Instagram comments in the category | Raw, short, often the insider phrases |
| Comments on the brand's own ads | Objections and questions, in reply to a message we know |
| Support tickets | What went wrong, and what people expected instead |
| Post-purchase surveys | The trigger and the reason they bought now |

Public pages are read in the browser without logging in. Exports (reviews, comments, tickets,
surveys) are saved as dated files in `source-pulls/`. A source the brand can't give is a named gap in
`running-notes/missing-context.md`.

## The steps

1. **Pull and save.** Follow `persona-gap` Mode A step A1 (`brain-system/.claude/skills/persona-gap/SKILL.md`):
   verbatim, with source, date and id, and the unweighted pull kept apart from any keyword search
2. **Read for usable language.** Use `brain-system/creative-strategy-context/customer-review-mining-method.md`:
   the trigger events, metaphors, insider phrases and "used to... now" lines are where angles hide
3. **Save each quote once.** When there is a lot of material, build the research map
   (`brain-system/.claude/skills/research-map/SKILL.md`, steps 1-7). Every quote gets an id
   (`q012`) in `research-map/evidence.jsonl`, a link to the original and a hashed author. The groups it
   counts by different people are the raw material for `build-bank.md`
4. **Look for the enemy on purpose.** For each group, note what customers use now or used before, and
   what they blame. That is the enemy an angle can name (`creative-vocabulary.md`)

## Output

Quotes with ids and sources in `source-pulls/` and `research-map/evidence.jsonl`, and the research map's
groups with their people counts. No new file format: build-bank reads what research-map and persona-gap
already write.
