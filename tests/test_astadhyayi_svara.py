# -*- coding: utf-8 -*-
"""
Tests for duration and accent — 1.2.27 to 1.2.32.

Two of these are checked against something outside themselves. 1.2.27's
durations must agree with what `grahana.kala` has been computing for 1.1.70
since before this pāda was touched — the two read the same tables, and a
disagreement would mean the metre engine and the grammar had drifted apart. And
1.2.29 to 1.2.31 are checked against the dhātupāṭha, which is the text that
actually carries the marks: 1,486 roots udātta, 667 anudātta, 106 svarita.

1.2.32 is the one worth reading twice. अर्धह्रस्वम् is half a MĀTRĀ and not
half the vowel, so the high part is a constant and the low part is what varies.
Reading it the other way makes every long svarita wrong, and one test exists
to separate the two readings.
"""

from __future__ import annotations

import unittest
from collections import Counter

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi import svara as V
from src.astadhyayi.corpus import load_dhatupatha
from src.astadhyayi.grahana import kala
from src.astadhyayi.sivasutra import resolve
from src.astadhyayi.svara import Accent


class Duration(unittest.TestCase):
    """1.2.27 ऊकालोऽज्झ्रस्वदीर्घप्लुतः."""

    def test_the_three_the_sutra_fuses(self):
        """
        उ ऊ ऊ३ इत्येवंकालोऽज् यथाक्रमं ह्रस्वदीर्घप्लुतः — a praśliṣṭa-nirdeśa
        of three enunciations, matched in order against three names.
        """
        self.assertEqual(
            [(name, matras) for name, _, matras in V.DURATIONS],
            [("hrasva", 1), ("dīrgha", 2), ("pluta", 3)],
        )
        for name, vowel, matras in V.DURATIONS:
            self.assertEqual(V.duration(vowel), matras, vowel)
            self.assertEqual(V.duration_name(vowel), name, vowel)

    def test_the_kasikas_examples(self):
        """दधि, मधु short; कुमारी, गौरी long; देवदत्त३ protracted."""
        self.assertTrue(V.is_hrasva("i"))
        self.assertTrue(V.is_hrasva("u"))
        self.assertTrue(V.is_dirgha("ī"))
        self.assertTrue(V.is_pluta("a3"))

    def test_the_diphthongs_are_long(self):
        for vowel in resolve("eC").sounds:
            self.assertEqual(V.duration(vowel), 2, vowel)

    def test_1_1_70_asks_this_sutra_rather_than_measuring_again(self):
        """
        `grahana.kala` answers 1.1.70's तत्कालस्य, and duration is not
        1.1.70's notion to define — 1.2.27 is where a vowel gets measured.

        This stood for a while as two identical functions and a test that
        they agreed. Agreement is the weaker claim: it can only fail once
        one copy has already been edited and something built on the
        difference. So the assertion is now that there is one answer, not
        two that match.
        """
        import inspect

        body = inspect.getsource(kala)
        self.assertIn("duration", body,
                      "1.1.70 should ask 1.2.27 for the mātrā count")
        self.assertNotIn("SHORT_VOWELS", body,
                         "1.1.70 is counting for itself again")
        vowels = list(resolve("aC").sounds) + [
            "ā", "ī", "ū", "ṝ", "ḹ", "a3", "ā3",
        ]
        for vowel in vowels:
            self.assertEqual(V.duration(vowel), kala(vowel), vowel)

    def test_a_consonant_has_no_duration(self):
        for sound in ("k", "y", "ś", "ḥ"):
            self.assertIsNone(V.duration(sound), sound)
            self.assertIsNone(V.duration_name(sound), sound)

    def test_the_three_names_are_exclusive(self):
        for vowel in ("a", "ā", "a3"):
            flags = [V.is_hrasva(vowel), V.is_dirgha(vowel), V.is_pluta(vowel)]
            self.assertEqual(sum(flags), 1, vowel)


class Substitutable(unittest.TestCase):
    """1.2.28 अचश्च."""

    def test_only_a_vowel_can_be_shortened_or_lengthened(self):
        for vowel in resolve("aC").sounds:
            self.assertTrue(V.substitutable(vowel), vowel)
        for consonant in resolve("haL").sounds:
            self.assertFalse(V.substitutable(consonant), consonant)

    def test_aca_iti_kim_suvag_brahmanakulam(self):
        """A form ending in a consonant has nothing to shorten."""
        self.assertFalse(V.substitutable("k"))
        self.assertFalse(V.substitutable("t"))

    def test_it_pairs_with_1_1_48_on_the_same_three_forms(self):
        """
        रै → अतिरि, नौ → अतिनु, गो → उपगु. This sūtra says the substituend must
        be a vowel; 1.1.48 says which vowel the substitute must be; 1.1.50
        supplies the choice neither of them states.
        """
        from src.astadhyayi.adesa import hrasva_of_ec

        for vowel, short in [("ai", "i"), ("au", "u"), ("o", "u")]:
            self.assertTrue(V.substitutable(vowel), vowel)
            self.assertEqual(hrasva_of_ec(vowel), short, vowel)


class AccentNames(unittest.TestCase):
    """1.2.29, 1.2.30, 1.2.31."""

    def test_three_accents_and_no_more(self):
        self.assertEqual(len(list(Accent)), 3)

    def test_unmarked_is_udatta(self):
        """Which is why the texts write only two marks."""
        self.assertIs(V.accent_of(""), Accent.UDATTA)
        self.assertIs(V.accent_of("bhū"), Accent.UDATTA)

    def test_the_two_marks_the_texts_use(self):
        self.assertIs(V.accent_of(V.SLP1_ANUDATTA), Accent.ANUDATTA)
        self.assertIs(V.accent_of(V.SLP1_SVARITA), Accent.SVARITA)

    def test_1_2_31_combines_the_qualities(self):
        """
        उदात्तानुदात्तसमाहारो योऽच् — and the Kāśikā insists it is the
        QUALITIES and not two vowels: गुणावेव वर्णधर्मौ गृह्येते, नाचौ.
        """
        self.assertIs(
            V.combines(Accent.UDATTA, Accent.ANUDATTA), Accent.SVARITA
        )
        self.assertIs(
            V.combines(Accent.ANUDATTA, Accent.UDATTA), Accent.SVARITA
        )

    def test_nothing_else_combines_into_a_svarita(self):
        for pair in [(Accent.UDATTA, Accent.UDATTA),
                     (Accent.ANUDATTA, Accent.ANUDATTA),
                     (Accent.SVARITA, Accent.UDATTA)]:
            self.assertIsNone(V.combines(*pair), pair)


class AgainstTheDhatupatha(unittest.TestCase):
    """The accents, read off the text that actually marks them."""

    def setUp(self):
        self.dhatus = load_dhatupatha()

    def test_all_three_accents_occur(self):
        counts = Counter(
            V.accent_of(entry.accent) for entry in self.dhatus.values()
        )
        self.assertEqual(len(counts), 3)
        for accent in Accent:
            self.assertGreater(counts[accent], 50, accent)

    def test_the_anudatta_roots_are_what_1_3_12_reads(self):
        """
        अनुदात्तङित आत्मनेपदम् makes an anudātta root take ātmanepada endings,
        so the mark is grammatical information and there is a lot of it.
        """
        anudatta = [
            e for e in self.dhatus.values()
            if V.accent_of(e.accent) is Accent.ANUDATTA
        ]
        self.assertGreater(len(anudatta), 600)
        self.assertTrue(all(e.anudatta for e in anudatta))

    def test_the_accent_is_kept_off_the_form(self):
        """
        The marks are not sounds. Left in the upadeśa, the it-rules would try
        to scan them and 1.3.3 would look at the wrong final.
        """
        for entry in list(self.dhatus.values())[:300]:
            self.assertNotIn(V.SLP1_ANUDATTA, entry.upadesa, entry.code)
            self.assertNotIn(V.SLP1_SVARITA, entry.upadesa, entry.code)

    def test_edha_carries_both_a_nasal_mark_and_an_accent_mark(self):
        """
        01.0002 एधँ has both, and they are different things: the tilde is
        1.3.2's it-marker, the backslash is 1.2.30's accent.
        """
        from src.astadhyayi.itsamjna import DHATU, analyze

        edha = self.dhatus["01.0002"]
        self.assertIs(V.accent_of(edha.accent), Accent.ANUDATTA)
        self.assertEqual(analyze(edha.upadesa, DHATU).stem, "edh")


class SvaritaProfile(unittest.TestCase):
    """1.2.32 तस्यादित उदात्तमर्धह्रस्वम्."""

    def test_half_a_matra_high_whatever_the_length(self):
        """
        अर्धह्रस्वम् इति च अर्धमात्रोपलक्ष्यते। ह्रस्वग्रहणमतन्त्रम्. The high
        part is a constant.
        """
        for vowel in ("a", "ā", "a3"):
            self.assertEqual(V.svarita_profile(vowel).udatta, 0.5, vowel)

    def test_the_low_part_is_what_varies(self):
        self.assertEqual(V.svarita_profile("a").anudatta, 0.5)
        self.assertEqual(V.svarita_profile("ā").anudatta, 1.5)
        self.assertEqual(V.svarita_profile("a3").anudatta, 2.5)

    def test_it_is_not_a_proportional_split(self):
        """
        Reading अर्धह्रस्व as 'half the vowel' would make a long svarita one
        mātrā high, and सर्वेषामेव ह्रस्वदीर्घप्लुतानां स्वरितानाम् एष
        स्वरविभागः says otherwise. This assertion separates the two readings.
        """
        long_profile = V.svarita_profile("ā")
        self.assertNotEqual(long_profile.udatta, 1.0)
        self.assertEqual(long_profile.udatta, 0.5)

    def test_the_parts_sum_to_the_vowels_duration(self):
        for vowel in ("a", "i", "ā", "ī", "e", "ai", "a3"):
            profile = V.svarita_profile(vowel)
            self.assertAlmostEqual(profile.total, V.duration(vowel), msg=vowel)

    def test_a_consonant_has_no_profile(self):
        self.assertIsNone(V.svarita_profile("k"))


class Registration(unittest.TestCase):
    IDS = tuple(f"1.2.{n}" for n in range(27, 33))

    def setUp(self):
        from src.astadhyayi.sutra import REGISTRY
        self.registry = REGISTRY

    def test_each_is_registered_and_executable(self):
        for sutra_id in self.IDS:
            sutra = self.registry.get(sutra_id)
            self.assertIsNotNone(sutra, sutra_id)
            self.assertTrue(callable(sutra.apply), sutra_id)

    def test_the_ac_anuvrtti_runs_through_the_accent_sutras(self):
        """अच् is read down from 1.2.27 into 1.2.29, 1.2.30 and 1.2.31."""
        for sutra_id in ("1.2.29", "1.2.30", "1.2.31"):
            carried = " ".join(self.registry.get(sutra_id).anuvrtti)
            self.assertIn("1.2.27", carried, sutra_id)

    def test_the_pada_module_was_discovered_automatically(self):
        import src.astadhyayi.rules as rules

        self.assertIn("adhyaya_1_pada_2", rules.PADAS)

    def test_the_accent_gap_on_1_1_69_is_now_a_scope_and_not_a_flat_gap(self):
        """
        It used to say accent was modelled nowhere. It is modelled now; what
        remains is that the sūtrapāṭha on disk is unaccented, so grahaṇa has
        nothing to widen over. The record has to carry that distinction, or the
        limitation reads as larger than it is.
        """
        notes = self.registry.get("1.1.69").notes
        self.assertIn("1.2.29", notes)
        self.assertIn("unaccented", notes)


if __name__ == "__main__":
    unittest.main()
