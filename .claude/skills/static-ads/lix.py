"""LIX readability score for Danish ad copy (the Danish counterpart of a reading-level check).

LIX = words per sentence + share of long words (more than 6 letters) in percent.
Sentence ends: . ! ? : and line breaks, because ad copy often breaks lines without punctuation.

Usage:
    python lix.py "Tekst der skal måles."
    python lix.py --file copy.txt
"""
import re
import sys

WORD = re.compile(r"[A-Za-zÆØÅæøåÄäÖöÜüÉé0-9]+(?:[-'][A-Za-zÆØÅæøåÄäÖöÜüÉé0-9]+)*")
# Periods that don't end a sentence: single capitals (H.C.) and common Danish abbreviations (kl. 14)
ABBREVIATION = re.compile(
    r"\b([A-ZÆØÅ]|kl|ca|fx|inkl|ekskl|evt|osv|mv|nr|bl|a|f|dvs|mht|pga|ift|eks|maks|stk|tlf|str)\.",
    re.IGNORECASE,
)
BANDS = [(25, "very easy"), (35, "easy"), (45, "medium (newspaper)"), (55, "hard"), (999, "very hard")]


def lix(text):
    unabbreviated = ABBREVIATION.sub(r"\1", text)
    sentences = [s for s in re.split(r"[.!?:\n]+", unabbreviated) if WORD.search(s)]
    words = WORD.findall(text)
    if not words:
        return None
    long_words = [w for w in words if len(re.sub(r"[-'0-9]", "", w)) > 6]
    score = len(words) / len(sentences) + 100 * len(long_words) / len(words)
    band = next(name for limit, name in BANDS if score < limit)
    return {
        "lix": round(score, 1),
        "band": band,
        "words": len(words),
        "sentences": len(sentences),
        "long_words": long_words,
    }


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    if len(sys.argv) > 2 and sys.argv[1] == "--file":
        with open(sys.argv[2], encoding="utf-8-sig") as f:
            text = f.read()
    else:
        text = " ".join(sys.argv[1:]) or sys.stdin.read()
    result = lix(text)
    if result is None:
        print("No words found.")
    else:
        print(f"LIX {result['lix']} ({result['band']}): {result['words']} words, "
              f"{result['sentences']} sentences, {len(result['long_words'])} long words")
        if result["long_words"]:
            print("Long words: " + ", ".join(result["long_words"]))
