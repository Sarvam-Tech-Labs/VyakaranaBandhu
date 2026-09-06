# -*- coding: utf-8 -*-
"""
Tests for the grahaṇa chain — 1.1.68 to 1.1.71.

These four decide what a sound named in a rule picks up, so a fault here is
invisible until it produces a wrong form somewhere far away. The tests are built
around the commentaries' own worked cases, chiefly the Kāśikā on 1.1.70, which
supplies both the rule and the derivation that goes wrong without it.
"""

from __future__ import annotations

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi import grahana as G
from src.astadhyayi import varna as V
from src.astadhyayi.sivasutra import resolve, resolve_all
from src.astadhyayi.sources import facts
from src.chandas.core import LONG_VOWELS, SHORT_VOWELS


class Kala(unittest.TestCase):
    """Duration, taken from the prosody engine rather than restated."""

    def test_it_matches_the_prosody_engines_own_vowel_tables(self):
        for vowel in SHORT_VOWELS:
            self.assertEqual(G.kala(vowel), 1, vowel)
        for vowel in LONG_VOWELS:
            self.assertEqual(G.kala(vowel), 2, vowel)

    def test_the_sandhyaksaras_are_long(self):
        """सन्ध्यक्षराणां ह्रस्वा न सन्ति — they have no short forms."""
        for vowel in ("e", "ai", "o", "au"):
            self.assertEqual(G.kala(vowel), 2, vowel)

    def test_a_consonant_has_no_duration_of_its_own(self):
        for sound in ("k", "y", "ś", V.ANUSVARA):
            self.assertIsNone(G.kala(sound), sound)

    def test_pluta_counts_three(self):
        self.assertEqual(G.kala("a" + G.PLUTA_MARK), 3)


class Varieties(unittest.TestCase):
    """1.1.69's स्वरानुनासिक्यकालभिन्नस्य ग्रहणं भवति."""

    def test_r_alone_among_the_semivowels_has_no_nasal_counterpart(self):
        """अन्तःस्था द्विप्रभेदाः, रेफवर्जिता यवलाः सानुनासिका निरनुनासिकाश्च."""
        self.assertEqual(G.varieties("r"), ("r",))
        for sound in ("y", "v", "l"):
            self.assertEqual(len(G.varieties(sound)), 2, sound)

    def test_the_usmans_have_none_either(self):
        for sound in sorted(V.USMAN):
            self.assertEqual(G.varieties(sound), (sound,), sound)

    def test_vowels_all_have_one(self):
        for sound in sorted(V.SVARA):
            self.assertEqual(len(G.varieties(sound)), 2, sound)

    def test_a_stop_has_none(self):
        """ṅ is already the nasal of its varga; it has no further nasal form."""
        for sound in sorted(V.SPARSA):
            self.assertEqual(G.varieties(sound), (sound,), sound)


class WhichAn(unittest.TestCase):
    """1.1.69 परेण णकारेण प्रत्याहारग्रहणम्."""

    def test_it_is_the_longer_reading_not_the_three_of_sivasutra_one(self):
        readings = sorted(len(r.sounds) for r in resolve_all("aṆ"))
        self.assertEqual(readings, [3, 14], "the ambiguity is real")
        for sound in ("h", "y", "v", "r", "l"):
            self.assertIn(sound, G.AN, f"{sound} must be in the wider aṆ")

    def test_the_semivowels_are_in_it_because_they_have_varieties_to_sweep(self):
        """
        The wider reading earns its place: y, v and l have anunāsika
        counterparts, and 1.1.69 exists to reach them.
        """
        for sound in ("y", "v", "l"):
            self.assertIn(sound, G.AN)
            self.assertGreater(len(G.grahana(sound)), 1, sound)

    def test_it_is_closed_under_savarnatva(self):
        """
        The śivasūtras list only the hrasva vowels. If aṆ stopped there, a rule
        writing ā would denote ā alone — and then the t of आत् in 1.1.1 would
        have nothing to exclude.
        """
        for long_vowel in ("ā", "ī", "ū", "ṝ"):
            self.assertIn(long_vowel, G.AN, long_vowel)


class Tapara(unittest.TestCase):
    """1.1.70 तपरस्तत्कालस्य."""

    def test_the_kasikas_own_case_at_71_9(self):
        """
        7.1.9 अतो भिस ऐस् — bhis becomes ais after अत्. The Kāśikā asks
        तत्कालस्येति किम्? and answers खट्वाभिः। मालाभिः॥ : the t is what stops
        the rule reaching ā, so वृक्ष takes ais and खट्वा does not.
        """
        self.assertEqual(facts("7.1.9").devanagari, "अतो भिस ऐस्")
        denoted = G.grahana("at")
        self.assertIn("a", denoted)
        self.assertNotIn("ā", denoted)
        # and the unrestricted form would have swept ā in
        self.assertIn("ā", G.grahana("a"))

    def test_it_supersedes_1_1_69_rather_than_refining_it(self):
        """
        अणिति नानुवर्तते; पूर्वग्रहणकशास्त्रं न प्रवर्तत एव. 1.1.69 must not
        appear in the provenance of a tapara term.
        """
        self.assertEqual(G.grahana("at").by, ("1.1.68", "1.1.70"))
        self.assertNotIn("1.1.69", G.grahana("at").by)
        self.assertIn("1.1.69", G.grahana("a").by)

    def test_other_qualities_stay_free(self):
        """तुल्यकालस्य गुणान्तरयुक्तस्य सवर्णस्य — duration is fixed, the rest
        is not, so the nasalised short a is still reached."""
        denoted = G.grahana("at")
        self.assertIn(V.nasalize("a"), denoted)
        self.assertNotIn(V.nasalize("ā"), denoted)

    def test_the_long_tapara_reaches_only_the_long(self):
        """आत् in 1.1.1 — vṛddhi is ā and not short a."""
        denoted = G.grahana("āt")
        self.assertIn("ā", denoted)
        self.assertNotIn("a", denoted)

    def test_both_readings_of_tapara_are_recognised(self):
        """तः परो यस्मात् सोऽयं तपरः, तादपि परस्तपरः."""
        self.assertEqual(G.tapara_of("at"), "a")
        self.assertEqual(G.tapara_of("ta"), "a")
        self.assertIsNone(G.tapara_of("a"))
        self.assertIsNone(G.tapara_of("ka"))


class Udit(unittest.TestCase):
    """1.1.69's उदित् half."""

    def test_the_kasikas_example_cutu_at_1_3_7(self):
        """चुटू — the Kāśikā cites it here. Each udit stands for its varga."""
        self.assertEqual(facts("1.3.7").devanagari, "चुटू")
        self.assertEqual(
            frozenset(G.grahana("cu").sounds), frozenset(V.VARGA["cu"])
        )
        self.assertEqual(
            frozenset(G.grahana("ṭu").sounds), frozenset(V.VARGA["ṭu"])
        )

    def test_every_varga_is_reachable_by_its_udit(self):
        for name, group in V.VARGA.items():
            self.assertEqual(
                frozenset(G.grahana(name).sounds), frozenset(group), name
            )

    def test_a_varga_is_delivered_by_savarnatva_not_by_a_list(self):
        """
        The udit rule works because a varga IS a savarṇa class. If it were a
        table lookup this would pass trivially; it goes through 1.1.9 instead.
        """
        for name, group in V.VARGA.items():
            self.assertEqual(
                frozenset(V.savarnas_of(group[0])), frozenset(group), name
            )
            self.assertIn("1.1.69", G.grahana(name).by)

    def test_a_bare_consonant_is_not_udit_and_denotes_itself_alone(self):
        """Which is the whole reason the udit convention exists."""
        self.assertEqual(G.grahana("k").sounds, ("k",))
        self.assertEqual(G.grahana("k").by, ("1.1.68",))
        self.assertIsNone(G.udit_of("k"))


class Pratyahara(unittest.TestCase):
    """1.1.71 feeding the chain."""

    def test_ik_unpacks_then_widens(self):
        denoted = G.grahana("iK")
        self.assertEqual(denoted.by, ("1.1.68", "1.1.71", "1.1.69"))
        for sound in ("i", "ī", "u", "ū", "ṛ", "ṝ", "ḷ", "ḹ"):
            self.assertIn(sound, denoted, sound)
        self.assertNotIn("a", denoted)
        self.assertNotIn("e", denoted)

    def test_hal_denotes_every_consonant_and_no_vowel(self):
        denoted = G.grahana("haL")
        for sound in resolve("haL").sounds:
            self.assertIn(sound, denoted, sound)
        for vowel in ("a", "ā", "i", "e"):
            self.assertNotIn(vowel, denoted, vowel)

    def test_an_affix_does_not_widen(self):
        """अप्रत्ययः."""
        self.assertEqual(G.grahana("a", pratyaya=True).sounds, ("a",))
        self.assertNotIn("1.1.69", G.grahana("a", pratyaya=True).by)
        self.assertIn("ā", G.grahana("a"))


class SandhyaksaraSeparation(unittest.TestCase):
    """
    The consequence that settled e~ai. Kept here rather than with 1.1.9 because
    it is the grahaṇa chain that makes the question bite.
    """

    def test_aic_and_eng_denote_disjoint_sets(self):
        """
        1.1.1's aiC is not tapara, so 1.1.69 widens it. Were e savarṇa with ai,
        vṛddhi would take in a guṇa vowel and the two saṃjñās would overlap.
        """
        vrddhi = frozenset(G.grahana("aiC").sounds)
        guna = frozenset(G.grahana("eṄ").sounds)
        self.assertEqual(vrddhi & guna, frozenset())
        self.assertIn("ai", vrddhi)
        self.assertIn("e", guna)
        self.assertNotIn("e", vrddhi)

    def test_without_the_separation_the_two_samjnas_would_collide(self):
        """
        The separation is load-bearing, not decorative: turn it off and e is
        savarṇa with ai, which is exactly the overlap the sūtras cannot have.
        """
        self.assertTrue(V.savarna("e", "ai", enumeration=False))
        self.assertTrue(V.savarna("o", "au", enumeration=False))
        self.assertFalse(V.savarna("e", "ai"))
        self.assertFalse(V.savarna("o", "au"))

    def test_the_features_alone_would_not_have_parted_them(self):
        """Which is why the Kāśikā's enumeration had to be brought in."""
        self.assertIs(V.varna("e").sthana, V.varna("ai").sthana)
        self.assertIs(V.varna("e").abhyantara, V.varna("ai").abhyantara)


class SabdaSamjna(unittest.TestCase):
    """1.1.68's अशब्दसंज्ञा clause."""

    def test_a_technical_term_denotes_what_it_names(self):
        result = G.grahana("vṛddhi")
        self.assertEqual(result.by, ("1.1.68",))
        self.assertEqual(result.sounds, ())
        self.assertIn("1.1.1", result.note)

    def test_the_samjnas_codified_so_far_are_all_registered(self):
        for name, sutra_id in [
            ("vṛddhi", "1.1.1"), ("guṇa", "1.1.2"), ("saṃyoga", "1.1.7"),
            ("anunāsika", "1.1.8"), ("savarṇa", "1.1.9"),
        ]:
            self.assertEqual(G.samjna_source(name), sutra_id, name)

    def test_an_ordinary_sound_is_not_treated_as_a_term(self):
        self.assertIsNone(G.samjna_source("a"))
        self.assertNotEqual(G.grahana("a").sounds, ())


class Provenance(unittest.TestCase):
    """The `by` field is the point of the module, so it is tested as such."""

    TERMS = ["a", "at", "ā", "āt", "i", "k", "ku", "cu", "iK", "haL", "aC", "y"]

    def test_every_denotation_starts_from_1_1_68(self):
        for term in self.TERMS:
            self.assertEqual(G.grahana(term).by[0], "1.1.68", term)

    def test_1_1_69_and_1_1_70_never_both_apply(self):
        """They are alternatives, not a pipeline — अणिति नानुवर्तते."""
        for term in self.TERMS:
            by = G.grahana(term).by
            self.assertFalse(
                "1.1.69" in by and "1.1.70" in by, f"{term}: {by}"
            )

    def test_an_unrecognised_term_says_so_rather_than_guessing(self):
        result = G.grahana("zzz")
        self.assertEqual(result.sounds, ())
        self.assertEqual(result.by, ())

    def test_the_result_reads_as_a_membership_test(self):
        self.assertIn("k", G.grahana("ku"))
        self.assertNotIn("c", G.grahana("ku"))
        self.assertEqual(len(G.grahana("ku")), 5)


if __name__ == "__main__":
    unittest.main()
