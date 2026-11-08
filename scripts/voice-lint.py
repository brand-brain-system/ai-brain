#!/usr/bin/env python3
# Origin: Parker (Simple Labs), used with permission; see third-party/parker/MANIFEST.md
"""voice-lint: deterministic scan for mechanical AI-writing tells in creative copy.

The mechanical layer of the two-layer check defined in
creative-strategy-context/ai-writing-tells.md (shipped to brand
brains as creative-strategy-context/ai-writing-tells.md). Sign inventory
generalized from Wikipedia: Signs of AI writing, retrieved 2026-07-03.
The v19 families (chatbot residue to lives-and-sits, and their Danish
twins) follow FeedHive's ai-slop-detector (MIT), rewritten as regexes here.

Scope: creative deliverables only — scripts, headlines, hooks, overlay and
static copy, ad-prompt spoken lines, iteration copy. Never run it against
context docs, prompts, or system docs. English and Danish copy are both
scanned; the Danish patterns are marked "(da)" in the report.

This layer is deterministic on purpose: it cannot be talked out of a flag.
A judgment pass (the creative-voice-review agent) decides which flags are
real — customer verbatims are exempt, the brand's corpus outranks the list,
one hit is noise and clustering is signal.

Usage:
    python3 voice-lint.py DRAFT_FILE
    cat draft.txt | python3 voice-lint.py -

Exit code 0 = clean at the mechanical layer, 1 = flags found.
"""
import re
import sys

# ---- AI vocabulary tiers (density matters, not one hit) ----
# Families: importance-inflators, texture words, transformation verbs,
# brochure adjectives. Update here first when the tier list drifts;
# ai-writing-tells.md points at this list as the maintained copy.

FLAGGED_WORDS = {
    # importance-inflators
    "pivotal", "crucial", "testament", "vital", "paramount", "indelible",
    # texture words
    "vibrant", "meticulous", "meticulously", "intricate", "intricacies",
    "seamless", "seamlessly", "robust", "holistic", "tapestry", "interplay",
    "nuanced", "multifaceted",
    # transformation verbs
    "elevate", "elevates", "elevating", "unlock", "unlocks", "unlocking",
    "empower", "empowers", "empowering", "transformative", "revolutionize",
    "revolutionary", "streamline", "supercharge", "harness", "unleash",
    # brochure adjectives and verbs
    "renowned", "unparalleled", "groundbreaking", "boasts", "boasting",
    "nestled", "enduring", "effortlessly", "curated", "bespoke",
    "delve", "delves", "foster", "fosters", "fostering", "garner",
    "garnered", "bolster", "bolstered", "underscore", "underscores",
    "underscoring", "showcase", "showcases", "showcasing", "synergy",
    "landscape", "realm", "game-changer", "game-changing",
    # the drama adverb ("Claude quietly shipped...")
    "quietly",
}

# ---- Pattern families (name, regex, note) ----

PATTERNS = [
    ("negative parallelism", re.compile(
        r"(\b(it|this|that|these|those|they)('?s|'?re| is| are| was| were)?"
        r"\s*n[o']t\s+(just|only|merely|simply)\b"
        r"|\bnot\s+only\b.{3,80}\bbut(\s+also)?\b"
        r"|\bmore\s+than\s+just\s+a?\b"
        r"|\bno\s+\w+[,.]\s*no\s+\w+[,.]\s*just\b"
        r"|\bisn'?t\s+(just|only|merely)\b|\baren'?t\s+(just|only|merely)\b"
        r"|\bwasn'?t\s+(just|only|merely)\b)", re.I),
     "the 'not just X, it's Y' frame — signature AI construction"),
    ("inflated significance", re.compile(
        r"\b(stands?\s+as|serves?\s+as|is\s+a\s+testament|"
        r"plays?\s+a\s+(vital|crucial|key|pivotal|significant)\s+(role|part)|"
        r"marks?\s+a\s+(shift|turning\s+point|new)|key\s+turning\s+point|"
        r"(ever-)?evolving\s+landscape|indelible\s+mark|deeply\s+rooted|"
        r"represents?\s+a\s+breakthrough|setting\s+the\s+stage|"
        r"a\s+whole\s+new\s+(way|level))\b", re.I),
     "importance-inflation instead of a plain claim"),
    ("participle tail", re.compile(
        r",\s+(highlighting|underscoring|emphasizing|ensuring|reflecting|"
        r"symbolizing|showcasing|demonstrating|solidifying|cementing|"
        r"reinforcing|elevating|fostering|contributing|signaling|"
        r"cultivating|embodying)\b", re.I),
     "sentence trailing into an unattributed '-ing' synthesis"),
    ("vague attribution", re.compile(
        r"\b(experts?\s+(say|agree|argue|recommend)|studies\s+show|"
        r"research\s+(shows|suggests)|industry\s+(reports?|insiders)|"
        r"observers\s+(have\s+)?not(e|ed)|many\s+(believe|agree)|"
        r"customers\s+rave|scientists\s+(say|agree)|doctors\s+agree)\b",
        re.I),
     "weasel attribution with no named source — also a compliance risk"),
    ("puffery register", re.compile(
        r"\b(commitment\s+to\s+(excellence|quality)|rich\s+heritage|"
        r"in\s+the\s+heart\s+of|natural\s+beauty|diverse\s+array|"
        r"wide\s+(range|variety)\s+of|premium\s+(experience|feel|quality)|"
        r"luxuriously|expertly[- ]crafted|thoughtfully\s+designed|"
        r"crafted\s+with\s+(care|precision)|attention\s+to\s+detail)\b",
        re.I),
     "brochure register no human says out loud"),
    ("signposted transition", re.compile(
        r"\b(but\s+here'?s\s+the\s+(thing|kicker|catch|best\s+part)|"
        r"here'?s\s+why(\s+it\s+works)?[:.]|that'?s\s+where\s+\w+"
        r"(\s+\w+)?\s+comes?\s+in|enter\s+[A-Z]\w+|look\s+no\s+further|"
        r"the\s+best\s+part\??|say\s+goodbye\s+to|say\s+hello\s+to|"
        r"the\s+secret\s+to|the\s+result\??|gone\s+are\s+the\s+days)\b",
        re.I),
     "formulaic bridge — real speech cuts, it doesn't signpost"),
    ("pristine CTA", re.compile(
        r"\b(don'?t\s+wait|order\s+yours?\s+today|shop\s+now\s+and|"
        r"experience\s+the\s+difference|what\s+are\s+you\s+waiting\s+for|"
        r"treat\s+yourself|you\s+(deserve|owe\s+it\s+to\s+yourself)|"
        r"join\s+(the\s+)?thousands|elevate\s+your)\b", re.I),
     "command-close ad-speak CTA — close like a friend instead"),
    ("copula avoidance", re.compile(
        r"\b(features?\s+an?\s+|offers?\s+an?\s+(range|variety|selection|"
        r"array)|provides?\s+an?\s+(range|variety|seamless|unmatched)|"
        r"delivers?\s+(unmatched|unparalleled|exceptional))", re.I),
     "'features/offers/delivers a' where 'is/has' belongs"),
    ("manufactured-intimacy opener", re.compile(
        r"\b(can\s+i\s+be\s+(real|honest|straight|100)"
        r"(\s+with\s+you)?(\s+for\s+a\s+(sec|second|minute))?"
        r"|let\s+me\s+be\s+(real|honest|straight)"
        r"|can\s+we\s+be\s+(real|honest)"
        r"|let\s+me\s+keep\s+it\s+(real|100|a\s+hundred)"
        r"|keeping\s+it\s+(real|100)"
        r"|i'?m(a|\s+gonna)?\s+be\s+(real|honest)\s+with\s+you"
        r"|real\s+talk)\b", re.I),
     "manufactured-intimacy opener — performed vulnerability that asks "
     "permission to be real instead of just being it; open on the actual "
     "confession, not the request to make one"),
    ("rhetorical self-question", re.compile(
        r"(\b(sound\s+familiar|crazy,?\s+right|guess\s+what|"
        r"you\s+know\s+what('?s)?\s+(crazy|wild|funny)|"
        r"want\s+to\s+know\s+the\s+(best|craziest)|"
        r"and\s+the\s+craziest\s+part)\s*\?"
        r"|\b(honestly|seriously|the\s+truth|real\s+talk)\s*\?)", re.I),
     "a question the speaker isn't actually asking — humans don't "
     "interview themselves; allowed only as a deliberate question hook "
     "in the opener"),
    ("throat-clearing", re.compile(
        r"\b(in\s+today'?s\s+(fast-paced|busy|modern|digital)|"
        r"when\s+it\s+comes\s+to|in\s+a\s+world\s+(where|of)|"
        r"we\s+all\s+know\s+(that|the\s+feeling)|let'?s\s+face\s+it|"
        r"picture\s+this[:.])", re.I),
     "opener spent on nothing — the first line is the expensive one"),
    ("audience enumeration", re.compile(
        r"\bwhether\s+you'?re\s+(a\s+)?\w+([\s\w]*)\s+or\s+(a\s+)?\w+",
        re.I),
     "'whether you're X or Y' — names everyone, lands with no one"),
    ("plain contrast", re.compile(
        r"\b(it|this|that)('s|\s+is)\s+not\s+(a\s+|an\s+|the\s+|your\s+)?"
        r"[\w-]+(\s+[\w-]+)?\s*[,;.—–-]+\s*(it|this|that)('s|\s+is)\b",
        re.I),
     "'it's not X, it's Y' — say what it does instead"),
    ("fake deadline", re.compile(
        r"\b(set\s+(this|it)\s+up|do\s+(this|it)|try\s+(this|it))\s+"
        r"(before|by|this|over\s+the)\s+(monday|tuesday|wednesday|thursday|"
        r"friday|saturday|sunday|weekend|tonight|tomorrow)\b", re.I),
     "invented urgency — say how long it takes; a real offer deadline is "
     "fine and must be true"),
    ("crowd address", re.compile(
        r"\bmost\s+people\s+(use|get|do|don'?t|are|think|make|miss|skip|"
        r"never|have\s+no)\b", re.I),
     "talking to a crowd — talk to the one reader, say what you do"),
    ("like-a-pro upgrade", re.compile(
        r"\blike\s+a\s+(pro|boss)\b|\blike\s+an?\s+\$\d", re.I),
     "'like a pro / like a $150 analyst' — show the result, let them judge"),
    ("fake-deep line", re.compile(
        r"\b(that'?s|this\s+is)\s+the\s+(whole|real|entire)\s+"
        r"(game|point|trick|secret)\b"
        r"|\bthe\s+part\s+(everyone|nobody|most\s+people)\s+skips\b",
        re.I),
     "a line that sounds deep and repeats the one before — cut it"),
    # ---- Added v19 (7 Nov 2026), after FeedHive's ai-slop-detector (MIT):
    # the families our list lacked. Credits: third-party/open-source-skills.
    ("chatbot residue", re.compile(
        r"(^\W*(certainly|absolutely|great\s+question|of\s+course)\s*!"
        r"|\bhere\s+is\s+an?\s+(polished|revised|rewritten|shorter|"
        r"longer|punchier|improved)\s+version\b|\bi\s+hope\s+this\s+helps\b"
        r"|\bwould\s+you\s+like\s+me\s+to\b|\blet\s+me\s+know\s+if\s+"
        r"you'?d\s+like\b|\bas\s+an\s+ai\b)", re.I),
     "assistant chatter left in the deliverable — delete it"),
    ("placeholder or citation debris", re.compile(
        r"\[(your|brand|company|insert|name|product|number|stat|link|city)"
        r"\b[^\]]*\]|\bXX\s?%|contentReference|oaicite|turn\d+search\d+"
        r"|\[\d{1,2}\](?!\()", re.I),
     "a gap marker or citation leftover — fill it from a source or cut the "
     "line; never ship it"),
    ("interpretive aside", re.compile(
        r"\b(that\s+(last\s+)?(point|part|bit|line)\s+matters"
        r"|matters\s+more\s+than\s+it\s+sounds|read\s+that\s+again"
        r"|let\s+that\s+sink\s+in|i'?ll\s+say\s+it\s+(again|louder))\b",
        re.I),
     "telling the reader how to read it — show why, or cut the aside"),
    ("rhetorical self-correction", re.compile(
        r"\bor\s+rather\b|\bactually,?\s+let\s+me\s+rephrase\b", re.I),
     "'fast. Or rather, instant.' — say the second thing"),
    ("fake-unscripted scaffolding", re.compile(
        r"^\W*(and\s+honestly|and\s+look|so\s+yeah|and\s+yeah)\b", re.I),
     "filler that performs being unscripted — say what happened"),
    ("hedge stacking", re.compile(
        r"\b(may|might|could)\s+(potentially|possibly)\b"
        r"|\bcan\s+sometimes\s+help\b|\bmight\s+help\s+to\b", re.I),
     "two hedges on one claim — give the evidence or cut the claim"),
    ("imagine-a-world opener", re.compile(
        r"\b(imagine\s+a\s+(world|life|day)\s+where|what\s+if\s+i\s+told"
        r"\s+you)\b", re.I),
     "describe what the product does today instead"),
    ("engagement bait", re.compile(
        r"(\bagree\s*\?\s*\W*$|\b(thrilled|excited|humbled|proud)\s+to\s+"
        r"(announce|share)\b|\bthat'?s\s+it\.\s+that'?s\s+the\s+"
        r"(post|tweet|ad)\b|\brepost\s+(if|this)\b"
        r"|\bno\s+fluff,?\s+just\b|\bultimate\s+guide\b"
        r"|\beverything\s+you\s+need\s+to\s+know\b)", re.I),
     "social-post formula — ask a real question or make the claim"),
    ("lives-and-sits metaphor", re.compile(
        r"\bwhere\s+(your|the|all)\s+[\w-]+(\s+[\w-]+)?\s+(lives|sits)\b",
        re.I),
     "data and products don't live anywhere — say where it is stored or shown"),
]

# ---- Case- and shape-sensitive tells (checked outside PATTERNS) ----

SIREN = re.compile(r"[🚨👇👉⬇➡]|\bBREAKING\b")
FRAGMENT_TRIPLET = re.compile(
    r"^\W*([^\W\d_][\w'-]*)\.\s+([^\W\d_][\w'-]*)\.\s+"
    r"([^\W\d_][\w'-]*)\.?\s*$")


# ---- Danish tells ----
# Same families as above, for copy written in Danish. Factory-written, not
# Parker's: the sign inventory is the English one carried over, plus the
# Danish constructions a strategist corrected in real drafts (see
# ai-writing-tells.md, "Danish copy"). Most entries are judgment calls from
# observation, not counted corpus; one hit is noise, clustering is signal.

DA_FLAGGED_WORDS = {
    "afgørende", "essentiel", "essentielt", "essentielle", "sømløs",
    "sømløst", "sømløse", "banebrydende", "revolutionerende",
    "revolutionere", "gamechanger", "uovertruffen", "uovertrufne",
}

DA_PATTERNS = [
    ("negativ parallelisme (da)", re.compile(
        r"(\b(det|dette|den|de)\s+(er|var)\s+ikke\s+(bare|blot|kun)\b"
        r"|\b(er|var)\s+ikke\s+(bare|blot|kun)\b"
        r"|\bikke\s+(kun|bare|blot)\b.{3,80}\bmen(\s+også)?\b"
        r"|\bmere\s+end\s+(bare|blot)\b)", re.I),
     "'ikke bare X, men Y' — the English 'not just X, it's Y' carried over"),
    ("afvist-og-vendt (da)", re.compile(
        r"[.!?]\s+Ikke\s+(\S+\s+){0,3}\S+[.!?]"),
     "'… Ikke X.' tacked on as a contrast — say what you do, skip the "
     "thing you're not doing"),
    ("signaleret overgang (da)", re.compile(
        r"\b(her\s+er\s+(sagen|tingen)|men\s+her\s+er\s+(det|sagen|tingen)"
        r"|og\s+det\s+bedste\s*\?|sig\s+farvel\s+til|sig\s+goddag\s+til"
        r"|hemmeligheden\s+(bag|er)"
        r"|det\s+er\s+her\s+\w+(\s+\w+)?\s+kommer\s+ind"
        r"|led\s+ikke\s+længere|fortvivl\s+ikke)\b", re.I),
     "formulaic bridge, translated — real speech cuts, it doesn't signpost"),
    ("selvstillet spørgsmål (da)", re.compile(
        r"\b(og\s+resultatet|sandheden|ærligt\s+talt|lyder\s+det\s+bekendt"
        r"|sjovt\s+nok|ved\s+du\s+hvad|vil\s+du\s+vide\s+hvad|gæt\s+hvad"
        r"|vildt,?\s+ikke)\s*\?", re.I),
     "a question the speaker isn't actually asking — allowed only as a "
     "deliberate question hook in the opener"),
    ("indledning uden indhold (da)", re.compile(
        r"\b(i\s+dagens\s+(hurtige|travle|moderne|digitale)"
        r"|i\s+en\s+verden\s+(hvor|af)|når\s+det\s+kommer\s+til"
        r"|vi\s+kender\s+alle\s+følelsen|lad\s+os\s+(se\s+i\s+øjnene|dykke)"
        r"|forestil\s+dig[:.])", re.I),
     "opener spent on nothing — the first line is the expensive one"),
    ("brochuresprog (da)", re.compile(
        r"\b(et\s+vidnesbyrd\s+om"
        r"|spiller\s+en\s+(afgørende|vigtig|central)\s+rolle"
        r"|i\s+hjertet\s+af|rig\s+arv"
        r"|forpligtelse\s+til\s+(excellence|kvalitet)"
        r"|bred\s+vifte\s+af|mangfoldig\s+vifte|til\s+næste\s+niveau"
        r"|frigør(e|es)?\s+(dit|din|dens|det)\s+fulde\s+potentiale"
        r"|frigør\s+potentialet|håndlavet\s+med\s+omhu"
        r"|skabt\s+med\s+omhu|dykke(r)?\s+ned\s+i|dyk\s+ned\s+i"
        r"|navigere\s+i\s+(landskabet|jungle))\b", re.I),
     "brochure or calque register nobody says out loud in Danish"),
    ("participiehale (da)", re.compile(
        r",\s+hvilket\s+(understreger|fremhæver|sikrer|demonstrerer|"
        r"afspejler|styrker|viser|bekræfter)\b|,\s+og\s+sikrer\s+dermed\b",
        re.I),
     "sentence trailing into an unattributed synthesis"),
    ("vag kilde (da)", re.compile(
        r"\b(eksperter\s+(er\s+enige|siger|anbefaler)|studier\s+viser"
        r"|undersøgelser\s+viser|forskning\s+(viser|tyder)"
        r"|kunderne\s+elsker|mange\s+mener|forskere\s+er\s+enige"
        r"|læger\s+er\s+enige)\b", re.I),
     "weasel attribution with no named source — also a compliance risk"),
    ("kommando-CTA (da)", re.compile(
        r"\b(vent\s+ikke|bestil\s+din\s+i\s+dag|oplev\s+forskellen"
        r"|hvad\s+venter\s+du\s+på|forkæl\s+dig\s+selv|du\s+fortjener"
        r"|løft\s+din)\b", re.I),
     "command-close ad-speak CTA — close like a friend instead"),
    ("engelsk komma før 'og' (da)", re.compile(
        r"\b[\wæøå-]+,\s+[\wæøå-]+,\s+og\s+[\wæøå-]+\b", re.I),
     "serial comma before 'og' is English punctuation; ignore it when 'og' "
     "starts a new main clause"),
    # ---- Added v19 (7 Nov 2026): the ai-slop-detector families, in Danish
    ("chatbot-rest (da)", re.compile(
        r"(^\W*(selvfølgelig|absolut|godt\s+spørgsmål)\s*!"
        r"|\bher\s+er\s+en\s+(forbedret|revideret|kortere|længere|"
        r"skarpere|omskrevet)\s+version\b|\bhåber\s+det\s+hjælper\b"
        r"|\bvil\s+du\s+have\s+at\s+jeg\b|\bsig\s+til,?\s+hvis\s+du\s+"
        r"vil\s+have\b|\bsom\s+en\s+ai\b)", re.I),
     "assistant chatter left in the deliverable — delete it"),
    ("pladsholder (da)", re.compile(
        r"\[(dit|din|indsæt|navn|brand|firma|produkt|tal|link|by)\b[^\]]*\]",
        re.I),
     "a gap marker left in — fill it from a source or cut the line"),
    ("fortolkende indskud (da)", re.compile(
        r"\b(læs\s+det\s+(lige\s+)?igen|lad\s+det\s+(lige\s+)?synke\s+ind"
        r"|det\s+(sidste\s+)?punkt\s+betyder\s+mere)\b", re.I),
     "telling the reader how to read it — show why, or cut the aside"),
    ("selvkorrektion (da)", re.compile(r"\beller\s+rettere\b", re.I),
     "'hurtig. Eller rettere, øjeblikkelig.' — say the second thing"),
    ("falsk spontanitet (da)", re.compile(
        r"^\W*(og\s+ærligt(\s+talt)?|så\s+ja|og\s+hør\s+her)\b", re.I),
     "filler that performs being unscripted — say what happened"),
    ("hækkestabling (da)", re.compile(
        r"\b(kan|vil|kunne)\s+(potentielt|muligvis)\s+(være\s+med\s+til|"
        r"hjælpe|bidrage|forbedre)\b", re.I),
     "two hedges on one claim — give the evidence or cut the claim"),
    ("forestil dig en verden (da)", re.compile(
        r"\bforestil\s+dig\s+en\s+(verden|hverdag|dag)\s+hvor\b", re.I),
     "describe what the product does today instead"),
    ("engagement-lokkemad (da)", re.compile(
        r"(\benig\s*\?\s*\W*$|\b(stolt|glad|beæret)\s+over\s+at\s+kunne\s+"
        r"(annoncere|fortælle|dele)\b|\bdel\s+(hvis|gerne\s+hvis)\b"
        r"|\bden\s+ultimative\s+guide\b|\balt\s+hvad\s+du\s+skal\s+vide\b)",
        re.I),
     "social-post formula — ask a real question or make the claim"),
]


def check_line(line):
    flags = []
    low = line.lower()
    words = re.findall(r"[a-z'-]+", low)
    hits = sorted({w for w in words if w in FLAGGED_WORDS})
    if hits:
        flags.append(("AI vocabulary", ", ".join(hits),
                      "flagged-word hit — judge density, not one hit"))
    da_words = re.findall(r"[a-zæøå'-]+", low)
    da_hits = sorted({w for w in da_words if w in DA_FLAGGED_WORDS})
    if da_hits:
        flags.append(("AI vocabulary (da)", ", ".join(da_hits),
                      "flagged-word hit — judge density, not one hit"))
    for name, rx, note in PATTERNS + DA_PATTERNS:
        m = rx.search(line)
        if m:
            flags.append((name, m.group(0).strip(), note))
    da_trip = re.search(r"\b([\wæøå-]+),\s+([\wæøå-]+)\s+og\s+([\wæøå-]+)\b",
                        line)
    if da_trip and all(len(g) <= 13 for g in da_trip.groups()) \
            and len({g.lower() for g in da_trip.groups()}) == 3:
        flags.append(("balanced triplet (da)", da_trip.group(0),
                      "smooth rule-of-three — repeat a word or break the "
                      "balance if the list is real"))
    # em-dash cadence: two or more dash breaks in one line
    if line.count("—") + line.count(" - ") + line.count(" – ") >= 2:
        flags.append(("em-dash cadence", "—…—",
                      "stacked dramatic clauses on dashes"))
    # balanced triplet: "X, Y, and Z" of short, matching-weight items
    trip = re.search(r"\b([\w-]+),\s+([\w-]+),\s+and\s+([\w-]+)\b", line)
    if trip and all(len(g) <= 13 for g in trip.groups()) \
            and len({g.lower() for g in trip.groups()}) == 3:
        flags.append(("balanced triplet", trip.group(0),
                      "smooth rule-of-three — repeat a word or break the "
                      "balance if the list is real"))
    # sirens and arrows: alarm emoji, pointing arrows, BREAKING in capitals
    siren = SIREN.search(line)
    if siren:
        flags.append(("sirens and arrows", siren.group(0),
                      "write the news as a normal sentence"))
    # three one-word sentences: "Write. Edit. Ship."
    frag = FRAGMENT_TRIPLET.search(line)
    if frag and len({g.lower() for g in frag.groups()}) == 3:
        flags.append(("fragment triplet", frag.group(0).strip(),
                      "three of everything — keep the one you believe"))
    # curly/straight quote mix within one piece of copy
    if ("“" in line or "‘" in line) and ('"' in line or "'" in line):
        flags.append(("curly-quote mix", "mixed quote styles", "pick one"))
    return flags


def main(argv):
    if len(argv) != 2:
        print(__doc__.strip().splitlines()[0])
        print("usage: voice-lint.py DRAFT_FILE  (or '-' for stdin)")
        return 2
    if argv[1] == "-":
        text = sys.stdin.read()
    else:
        with open(argv[1], encoding="utf-8") as f:
            text = f.read()
    total, report = 0, []
    lines = text.splitlines()
    for i, line in enumerate(lines, 1):
        if not line.strip():
            continue
        found = check_line(line)
        # Danish contrast split over two lines: 'Ikke X.' then 'Men Y.'
        nxt = next((l for l in lines[i:] if l.strip()), "")
        if line.lstrip(' "“„»').startswith("Ikke ") \
                and nxt.lstrip(' "“„»').startswith("Men "):
            found.append(("afvist-og-vendt (da)", line.strip() + " / "
                          + nxt.strip(), "'Ikke X. Men Y.' over two lines"))
        for name, evidence, note in found:
            total += 1
            report.append(f'  L{i} [{name}] "{evidence}" — {note}')
    n_lines = max(1, sum(1 for l in lines if l.strip()))
    print(f"voice-lint: {total} flag(s) across {n_lines} non-empty lines "
          f"(density {total / n_lines:.2f})")
    for r in report:
        print(r)
    if total == 0:
        print("  clean at the mechanical layer — the judgment pass "
              "still applies")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
