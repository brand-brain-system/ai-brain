"""scripts/voice-lint.py: the mechanical scan for AI-writing tells.

English tells come from Parker's list; the Danish ones are ours (see
creative-strategy-context/ai-writing-tells.md, "Danish copy"). These tests
pin what each Danish pattern catches and that plain Danish stays clean.
"""
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from test_runtime_hooks import FACTORY

SCRIPT = Path(FACTORY) / "scripts" / "voice-lint.py"


def lint(text):
    with tempfile.TemporaryDirectory() as tmp:
        draft = Path(tmp) / "draft.txt"
        draft.write_text(text, encoding="utf-8")
        r = subprocess.run(
            [sys.executable, str(SCRIPT), str(draft)],
            capture_output=True,
            text=True,
            encoding="utf-8",
            env={**os.environ, "PYTHONIOENCODING": "utf-8"},
        )
    return r.returncode, r.stdout


class VoiceLintTest(unittest.TestCase):
    def assertFlag(self, text, family):
        code, out = lint(text)
        self.assertEqual(code, 1, out)
        self.assertIn(f"[{family}]", out)

    def test_english_still_flagged(self):
        self.assertFlag("It's not just a jacket, it's a lifestyle.", "negative parallelism")

    def test_plain_danish_is_clean(self):
        code, out = lint(
            "Jeg læser kommentarerne under annoncerne, før jeg skriver noget.\n"
            "Kan jeg ikke pege på, hvor det kommer fra, så ryger det ud.\n"
        )
        self.assertEqual(code, 0, out)

    def test_ikke_bare_men(self):
        self.assertFlag("Det er ikke bare en jakke, det er en livsstil.", "negativ parallelisme (da)")

    def test_ikke_kun_men_ogsa(self):
        self.assertFlag("Den er ikke kun blød, men også holdbar.", "negativ parallelisme (da)")

    def test_ikke_tacked_on_after_a_sentence(self):
        self.assertFlag("Træk historien ud. Ikke ordene.", "afvist-og-vendt (da)")

    def test_ikke_then_men_over_two_lines(self):
        self.assertFlag('Ikke "kunderne føler nok"\nMen en kommentar.', "afvist-og-vendt (da)")

    def test_signposted_transition(self):
        self.assertFlag("Men her er sagen.", "signaleret overgang (da)")

    def test_self_question(self):
        self.assertFlag("Og resultatet? Et helt nyt look.", "selvstillet spørgsmål (da)")

    def test_throat_clearing(self):
        self.assertFlag("I dagens hurtige verden har alle travlt.", "indledning uden indhold (da)")

    def test_calques_and_brochure(self):
        self.assertFlag("Lad os dykke ned i, hvordan du frigør dit fulde potentiale.", "brochuresprog (da)")

    def test_participle_tail(self):
        self.assertFlag("Stoffet er blødt, hvilket understreger vores omhu.", "participiehale (da)")

    def test_vague_source(self):
        self.assertFlag("Studier viser, at det virker.", "vag kilde (da)")

    def test_ad_speak_cta(self):
        self.assertFlag("Vent ikke, bestil din i dag.", "kommando-CTA (da)")

    def test_vocabulary_with_danish_letters(self):
        self.assertFlag("En sømløs og afgørende løsning.", "AI vocabulary (da)")

    def test_serial_comma_before_og(self):
        self.assertFlag("Vi har blå, grønne, og røde jakker.", "engelsk komma før 'og' (da)")

    def test_balanced_triplet(self):
        self.assertFlag("Den er blød, behagelig og holdbar.", "balanced triplet (da)")

    # The tells that moved into the words around the dash (v14)

    def test_quietly(self):
        self.assertFlag("Claude quietly shipped the best feature of the year.", "AI vocabulary")

    def test_plain_contrast(self):
        self.assertFlag("It's not a chatbot, it's a coworker.", "plain contrast")

    def test_fake_deadline(self):
        self.assertFlag("Set this up before Monday.", "fake deadline")

    def test_crowd_address(self):
        self.assertFlag("Most people use Claude wrong.", "crowd address")

    def test_like_a_pro(self):
        self.assertFlag("Claude can now research like a $150/hour analyst.", "like-a-pro upgrade")

    def test_fake_deep_line(self):
        self.assertFlag("Setup is the part everyone skips.", "fake-deep line")
        self.assertFlag("That's the whole game.", "fake-deep line")

    def test_fragment_triplet(self):
        self.assertFlag("Write. Edit. Ship.", "fragment triplet")

    def test_sirens_and_arrows(self):
        self.assertFlag("\U0001F6A8 BREAKING: a new model is out \U0001F447", "sirens and arrows")

    def test_plain_english_is_clean(self):
        code, out = lint(
            "I wore them on a six-hour flight and forgot they were on.\n"
            "It's not cheap, but it lasted three winters.\n"
            "Breaking in new boots hurts.\n"
            "Most people I know wear them daily.\n"
        )
        self.assertEqual(code, 0, out)

    # v19: the families after FeedHive's ai-slop-detector (MIT)
    def test_chatbot_residue(self):
        self.assertFlag("Certainly! Here is a punchier version of the headline.", "chatbot residue")

    def test_placeholder_and_gap_markers(self):
        self.assertFlag("[Your Brand] socks stay dry.", "placeholder or citation debris")
        self.assertFlag("[NUMBER MISSING] golfers switched.", "placeholder or citation debris")
        self.assertFlag("Rated best in class [3].", "placeholder or citation debris")

    def test_interpretive_aside(self):
        self.assertFlag("That last point matters more than it sounds.", "interpretive aside")

    def test_rhetorical_self_correction(self):
        self.assertFlag("It dries fast. Or rather, instantly.", "rhetorical self-correction")

    def test_fake_unscripted_scaffolding(self):
        self.assertFlag("So yeah, that's when I switched.", "fake-unscripted scaffolding")

    def test_hedge_stacking(self):
        self.assertFlag("It may potentially reduce blisters.", "hedge stacking")

    def test_imagine_a_world(self):
        self.assertFlag("Imagine a world where your socks never slip.", "imagine-a-world opener")

    def test_engagement_bait(self):
        self.assertFlag("Thrilled to announce our new sock. Agree?", "engagement bait")

    def test_lives_and_sits(self):
        self.assertFlag("The app is where your round data lives.", "lives-and-sits metaphor")

    def test_danish_v19_families(self):
        self.assertFlag("Selvfølgelig! Her er en kortere version.", "chatbot-rest (da)")
        self.assertFlag("[Indsæt tal] kunder har skiftet.", "pladsholder (da)")
        self.assertFlag("Læs det igen.", "fortolkende indskud (da)")
        self.assertFlag("Den tørrer hurtigt. Eller rettere, med det samme.", "selvkorrektion (da)")
        self.assertFlag("Og ærligt talt, så skiftede jeg.", "falsk spontanitet (da)")
        self.assertFlag("Den kan potentielt hjælpe mod vabler.", "hækkestabling (da)")
        self.assertFlag("Forestil dig en hverdag hvor strømperne bliver oppe.", "forestil dig en verden (da)")
        self.assertFlag("Stolt over at kunne annoncere vores nye strømpe.", "engagement-lokkemad (da)")

    def test_v19_plain_copy_stays_clean(self):
        code, out = lint(
            "Rather than wash them hot, use 40 degrees.\n"
            "The heel is reinforced and the seam sits flat.\n"
            "Så kom jeg hjem og tog dem af.\n"
            "Jeg kan godt lide, at de er tynde.\n"
        )
        self.assertEqual(code, 0, out)


if __name__ == "__main__":
    unittest.main()
