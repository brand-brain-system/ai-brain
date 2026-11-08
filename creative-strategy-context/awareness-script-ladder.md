---
summary: "The 11-step awareness ladder: which step a script opens on per awareness level (UN 1, PA 3, SA 5, PR 7, MA 9), what each step must do, which script shape fits each entry, how statics compress it, with a worked example."
---

# The awareness script ladder

**Source:** a practitioner's post on how winning scripts follow awareness, handed in by the team on 7 Nov 2026. The entry step for most aware viewers, the shape fit, the static rule and the example are ours.
**Users:** the whole team, all brands. Read by `scriptwriting`, `static-ads`, `headlines`, `ad-breakdown` (the `ladder_start` tag) and anyone writing a brief.
**Status:** *Stated* (one source, no data shown). Not yet tested on our accounts. The parts we added are *Inferred* from the source and our own docs.

The idea: winning scripts walk roughly the same eleven steps, from a stranger's first second to the call to action. The more aware the viewer, the further down the ladder the script starts. Steps before the entry are skipped or folded into one line. Steps after it all have to happen, even if some get one line.

The words (awareness codes, UMP, UMS, enemy) are defined in `creative-vocabulary.md`.

## The eleven steps

| # | Step | What it must do |
|---|---|---|
| 1 | Unaware hook | Stop someone who doesn't know they have the problem. Open on their life, a surprising fact, a story or a pattern they recognise. No product, often no problem name yet |
| 2 | Education | Teach the one thing that makes them see the problem: link the symptom to its cause. The root cause (UMP) often first shows up here |
| 3 | Problem intro | Name the problem in the viewer's own words, so they think "that's me" |
| 4 | Problem agitation | Show what it costs: time, money, how it feels, who notices. Set the intensity for this viewer (`creative-vocabulary.md`, valence and intensity) |
| 5 | Failed solutions | The kinds of fix they tried, and why each one fails. The enemy usually lives here, and the reason it fails is the opposite of the mechanism |
| 6 | Solution intro | The new kind of fix and how it works (UMS): why it works where the others didn't |
| 7 | Failed products | Other products of this kind and what they get wrong: the copy, the cheap version, the wrong spec. The enemy at product level |
| 8 | Product intro | Name the product as the one that does the fix right |
| 9 | Benefits, USPs and proof | What it does for them, what only it has, and proof they can believe. For most aware viewers the offer leads here |
| 10 | Picture the vision state | A concrete scene of life with the problem gone. A scene, not an adjective |
| 11 | Call to action | What to do now and why now: link, offer, guarantee |

Step 5 and step 7 are easy to mix up. Step 5 is about kinds of fix (diets, creams, training classes). Step 7 is about products of the kind you sell (the other harnesses, the other serums). A solution aware viewer needs both; a product aware viewer already has the kind of fix, so the script starts at 7.

## Where to enter

| Awareness | Enter at | Why | Runs to |
|---|---|---|---|
| `UN` Unaware | 1 | They need to see the problem before any fix makes sense | 11, usually long |
| `PA` Problem aware | 3 | They know the problem; naming it in their words earns the next line | 11 |
| `SA` Solution aware | 5 | They know the kind of fix; show why the fixes they know fail | 11 |
| `PR` Product aware | 7 | They know your product; show why the others in your category fall short | 11 |
| `MA` Most aware | 9 | They know and want it; give them the offer, the proof and the reason to act now | 11, often 9 then 11 |

**Our decision on most aware: enter at 9, not 8.** Step 8 introduces the product, and a most aware viewer doesn't need an introduction. Name the product in the first line anyway, inside step 9, because they must know which ad they are looking at. Step 10 is optional here. Enter at 8 instead when the viewer knows the brand but not this product: a new product or a new size shown to existing customers. Offers in Danish ads follow the price rules in `offer-design.md` and the brand's compliance file.

The `ladder_start` tag records the step the script actually opens on, 1-11, which is not always the textbook entry. A problem aware script that opens on a story at step 1 is tagged `PA` and `ladder_start` 1.

## The ladder and the five shapes

The ladder says where to enter and what must be covered. The shape (`winning-script-patterns.md`) says in what order the beats come. Shapes don't climb the ladder in a straight line: a symptom call out pulls step 2 forward as a twist, and a story often tells step 5 before step 3 is complete.

| Shape (`shape` tag) | Usual entry | How it walks the ladder | Best fit |
|---|---|---|---|
| Symptom call out (`symptom`) | 3 | Symptom (3), surprising reframe (2), stop doing what you do now (5), why that fails (5), what works and why (6), the product (8) | `PA`; `UN` when the symptom is visible but not yet seen as a problem |
| Story with a cost (`story`) | 3-4 | Low point with a number (3, 4), fixes tried (5), who told them the real cause (2, 6), the product (8), week by week (9, 10) | `PA`; `UN` when the story opens on a life moment (1) |
| Authority secret (`authority`) | 1 or 5 | Credible role and the one thing (1), not the obvious fixes (5), the real cause (2), the old way that fails (5), the product (8) | `UN`, or `SA` when the obvious fixes are well known |
| Enemy first (`enemy`) | 7 | Don't buy the category where they buy it (7), what's wrong with those (7), if you have the symptom you need this (3 then 9), the product (8, 9) | `PR`, late `SA` |
| Objection opener (`objection`) | 7-9 | The doubt (9), what others do wrong (7), what we do (9), one number (9), the guarantee (11) | `PR` |
| Offer (`offer`) | 9 | The product and the deal (9), proof (9), why now (11) | `MA` |

## Statics

A static compresses the steps from its entry point into one frame:
- **Headline = the entry step.** A problem aware static's headline names the problem (3). A product aware static's headline takes on the other products (7).
- **Body or subhead = the next one or two steps.** For a problem aware static: why the old fixes fail and what works (5, 6).
- **Image = proof or the product** (8, 9), and it should still make the point with the words covered.
- **Button or end line = step 11.**

If a static needs more than three steps to make sense, it is either aimed at too low an awareness level or it should be a video or a carousel. Eye flow and hierarchy: `static-ad-design.md`. Headline patterns per awareness level: the `headlines` skill.

## The ladder, the funnel stage and the older section

**Funnel stage.** The ladder follows awareness, not the campaign, and the funnel stage is never read off the entry step (`creative-vocabulary.md`, Funnel stage). An entry at 7 or 9 is not a BOF script: in a broad campaign Meta picks the viewers from what the ad says, and a product-aware mechanism script can scale on cold traffic (`angle-discovery.md`, "Product-aware angles run cold"). A solution aware stranger is cold to your brand and still needs a script that starts at 5, even in a TOF campaign. Pick the entry by what the viewer knows about the problem and the fixes.

**Length.** Low entries need room. A script that enters at 1 or 2 is teaching, and in the 100-script study the teaching scripts ran about 80 seconds (*Stated*, `winning-script-patterns.md`). Don't cut them to 30 seconds. Entries at 7-9 can be short.

**`scriptwriting.md`, "Writing for different stages of awareness".** That section stays. It says what kind of content each stage wants (education, agitation, comparisons, objection handling, offers) and how much of the mix should sit at the top. This doc goes one level deeper: the order of the steps and where to enter. They agree: problem aware is "agitate the pain, show failed solutions" there and steps 3-5 here; product aware is "handle objections, build trust" there and steps 7-9 here.

## Worked example: one angle, three awareness levels

A made-up product for illustration: a no-pull dog harness that clips at the chest. No real brand, and the mechanism is a teaching example, not a checked claim. Proof slots are left open because real proof comes only from the proof inventory in `brand-lens.md`.

- **Angle:** walks you dread because the dog pulls.
- **Enemy:** "no-pull" harnesses that clip on the back.
- **UMP:** dogs lean into pressure. When the lead tightens, they pull harder.
- **UMS:** a chest clip turns a pull sideways, toward the owner, so pulling stops paying off.

**Unaware, enters at 1** (authority secret, a dog trainer):
1. "Most dogs that pull on the lead were taught to pull. By the lead."
2. "Push on a dog's chest and it pushes back. It's a reflex."
3. "So the lead goes tight, your dog pulls harder, you pull back."
4. "And the walk you used to look forward to turns into a fight with your shoulder."
5. "More treats or another class won't change a reflex."
6. "What changes it is where the lead clips on. Clip it at the chest, and a pull turns the dog sideways, toward you."
8. "That's what [product] does."
9. "[One proof line from the proof inventory.]"
10. "Picture the lead hanging loose the whole way to the park."
11. "Link below."

**Problem aware, enters at 3** (symptom call out, a customer):
3. "If your arm aches after every walk, it isn't your dog's fault."
5. "You've tried the treats, the classes, maybe a firmer collar."
2. "None of it works, because dogs push into pressure. The tighter the lead, the harder they pull."
6. "The fix is where the lead clips on. At the chest, a pull just turns them toward you."
8. "The one I use is [product]."
9. "[Proof line.]"
11. "It's linked below."

**Product aware, enters at 7** (objection opener, the founder):
9. "Yes, [product] costs more than the harness at the pet shop. Here's why."
7. "Most 'no-pull' harnesses clip on the back. That's the exact spot that makes a dog pull."
9. "Ours clips at the chest, with the ring set low, so a pull turns the dog toward you."
9. "[One number from the proof inventory.]"
11. "And if your dog still pulls after [n] walks, [the guarantee from the proof inventory]."

**The problem aware version as a static:**
- Headline (3): "Arm sore after every walk?"
- Subhead (5, 6): "Treats can't beat a reflex. A chest clip can."
- Image (8, 9): the dog walking beside the owner on a loose lead, the chest clip visible.
- Button (11): Shop now.

Same angle, same enemy, same mechanism. What moves is where the script starts and how much of the ladder it has to climb.
