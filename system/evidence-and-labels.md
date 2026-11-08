# Evidence and labels

The rules that keep a brain honest. They apply to every durable doc, and the skills check them before they hand work over.

## The four labels

| Label | Meaning | Example |
|---|---|---|
| **Verified** | Seen directly in a source, with the source and date named | "Product page shows <rating> from <n> reviews (read <date>)" |
| **Stated** | A source says it; we haven't checked | "The founder says <claim about origin>" |
| **Inferred** | Reasoned from evidence; name what it rests on | "The offer is probably the main reason for the click, because <x>% of live ads lead with it" |
| **Data-limited** | Can't be resolved from what is available; say what would resolve it | "CPA by ad: needs ad-account access" |

There is **no fifth label for "unsupported"**. A claim that can't be traced to a source is deleted or becomes Data-limited, however good it sounds.

## Habits

- **Invent nothing.** No numbers, spend, audience sizes or performance claims without a source. A blank reads "Not captured yet"
- **Source and date everything durable.** The reader should be able to re-check it, or replace it
- **Quote exactly.** Customer language is stored verbatim with source, date and id. Paraphrase is marked as paraphrase
- **Shares come from unweighted pulls.** A keyword-searched pull can show that a thing exists, never how common it is. Say which sources over-represent whom (reviews over-represent online buyers and recent purchases)
- **Every table states its limit.** Without account access *share of ads* stands in for *share of spend*; reviews are not customers; impressions rank is reach, not results
- **The Ad Library shows what a brand runs, never how it performs.** Don't rank or call an ad a winner from it
- **The brand's own materials win.** Guidelines and press kits outrank researched facts; conflicts are flagged, not merged
- **Proof inventory is a wall.** Review counts, ratings, customer numbers, press and seals in an ad come from the proof inventory in `brand-lens.md` and nowhere else
- **Concept work is labelled as concept.** For a brand that hasn't commissioned the work, every output says so

## Independent audit

An AI that writes a synthesis tends to fill gaps. So durable syntheses (personas, the roadmap, the VoC files) are audited by a **separate agent that did not write them**. It checks each field against its
source and marks it found, inferred or unsupported; unsupported fields are deleted, never relabelled. The audit result is recorded at the bottom of the document ("<n> found, <n> inferred, <n> fixed").

## Two review gates for creative

Every draft that reaches a person passes two independent checks, in order:

1. **Grounding.** Was it built from the right documents, and does every quoted line and number trace to a file in the brain? (a script traces quotes and numbers; a reviewing agent checks what the script can't)
2. **Voice.** Does it read like a person wrote it for this brand? (a lint for known AI tells; a reviewing agent judges against the brand's voice)

Grounded first, human-sounding second. Both are in the factory: `scripts/grounding-check.py` and `scripts/voice-lint.py` with the agents in `.claude/agents/`.
