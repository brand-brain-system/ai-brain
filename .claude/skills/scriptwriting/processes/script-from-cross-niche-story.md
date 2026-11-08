# Process — Script From Cross-Niche Story

Take a high-engagement organic video from a niche **unrelated** to the brand, extract its story skeleton, and rebuild that shape around the brand's real product facts with one communication modifier on
top. The output is a script, never a copy of the original.

Method and the modifier list: `brain-system/creative-strategy-context/story-skeletons-and-modifiers.md`. For a breakout inside the brand's own niche, use `script-from-organic-niche` instead.

## Required inputs

- The organic video (URL or file) and its engagement signal. Without a signal it is a taste pick, not evidence: say so.
- The product page or fact source, brand profile, voice profile, customer language, compliance constraints.
- Target length and placement.

## Models

Each step runs as its own subagent on the model that fits it (the `model` parameter on the Agent tool). Switching is the point: do not run the whole chain on one model.

| Step | Model | Why |
|---|---|---|
| 2 Read product, 3 baseline | `sonnet` | Fact extraction |
| 4 Skeleton extraction | `sonnet` on transcript + frames; a video-native model (e.g. Gemini, only if the brain has it connected; there is no such role in `system/tool-roles.md` yet) when pacing or cuts carry the story | Claude reads transcripts and frames, not the video itself |
| 5 Modifier and brand voice | `sonnet` | Creative rewrite |
| 7 Swap test and plagiarism check | `opus`, in a context that did not write the script | Judgement, and the writer must not grade its own page |

If a route or model is unavailable, say which and fall back to the next one down; never skip the swap test.

## Execution

### Step 1 — Qualify the video
Engagement against post date (high views on an old post is signal; low views on a fresh one is just young). Confirm it is outside the brand's niche, and that its shape could carry the brand's message
without forcing it. If it cannot, pick another video rather than bend the product.

### Step 2 — Read the product (single task)
Read the product page. Report facts only: what it is, who it's for, why it works, what may not be claimed. Nothing creative.

### Step 3 — Plain baseline (single task)
Write the boring script at the target length. This is the fact layer; it is not shown as a deliverable.

### Step 4 — Extract the skeleton
Transcribe the video and pull frames (`video-edits` has the transcription and `frame-check.py` routes). Return beats with timing, what escalates or turns, the viewer's emotion per beat, and a one-line
pattern name. No dialogue from the original is stored.

### Step 5 — Apply the skeleton, then one modifier
Rebuild the baseline in the skeleton's beats. Then add exactly one modifier. Rewrite in the brand voice profile and the customer's words (voiced, not pasted, per `scriptwriting/SKILL.md`).

### Step 6 — Hook and CTA
Load the hook context as in `SKILL.md` step 3. One CTA.

### Step 7 — Swap test and originality check
Swap in a competitor's name: if it still reads right, return to step 5 with more brand specifics. Then compare against the original's transcript: no surviving line, joke or recognisable scene.

### Step 8 — The two gates
Grounding and voice review as in `SKILL.md` step 7.

### Step 9 — Stop for a person
Show the skeleton, the modifier used, the script, and what the swap test caught. Nothing is filmed, generated or posted without a yes.

## What good looks like

- The viewer would recognise the *shape* from organic feeds, and nothing from the original video.
- One modifier, clearly doing its job.
- The brand name cannot be swapped out.
- Every fact traces to the product page.

## Common failures

- Reusing a line, joke or scene from the original (plagiarism, and a copyright risk).
- A skeleton from the brand's own niche, which is just recreating a competitor.
- Two or three modifiers stacked.
- Running every step on one model in one context, so the writer reviews itself.
- Letting the modifier invent a claim ("secret" that is not true).
