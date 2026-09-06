# -*- coding: utf-8 -*-
"""
Tests for where a substitute lands — 1.1.52 to 1.1.55.

These four are one decision with three exceptions, and the interesting part is
the order they are tried in: 1.1.53 exists only to beat 1.1.55, so a test suite
that never puts a ṅit and anekāl substitute through together would pass while
the sūtra did nothing. आनङ् is that case and the Kāśikā names it.

Every example below is the commentary's own, and each is checked against the
corpus for the case marking it depends on.
"""

from __future__ import annotations

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi.adesa import (
    Adesa,
    PANCAMI,
    SASTHI,
    Site,
    apply_adesa,
    pancami_padas,
    replace_adi,
    site_for,
    sthanin_padas,
    substitution_site,
)
from src.astadhyayi.sources import all_sutra_ids, facts


class Anekal(unittest.TestCase):
    """अनेकाल् counts sounds, not characters."""

    def test_a_digraph_counts_once(self):
        self.assertTrue(Adesa("bhū").anekal)      # bh + ū
        self.assertFalse(Adesa("bh").anekal)      # one sound, two letters
        self.assertFalse(Adesa("ā").anekal)
        self.assertTrue(Adesa("ān").anekal)
        self.assertFalse(Adesa("au").anekal)      # one vowel, two letters

    def test_an_empty_substitute_is_not_anekal(self):
        self.assertFalse(Adesa("").anekal)

    def test_the_it_letters_are_kept_off_the_form(self):
        """
        They are carried separately because reading them off the string needs
        1.3.2–1.3.9, which are not codified. शि is śit and one sound; if the ś
        lived in the form it would count as two.
        """
        si = Adesa("i", frozenset("ś"))
        self.assertTrue(si.sit)
        self.assertFalse(si.anekal)
        self.assertFalse(si.ngit)


class DecisionOrder(unittest.TestCase):
    """Which sūtra governs, and why that order."""

    def test_the_default_is_the_last_sound(self):
        self.assertEqual(substitution_site(Adesa("i")).by, "1.1.52")
        self.assertIs(substitution_site(Adesa("i")).site, Site.ANTYA)

    def test_anekal_takes_the_whole(self):
        """2.4.52 अस्तेर्भूः — भू is two sounds, so all of अस् goes."""
        decision = substitution_site(Adesa("bhū"))
        self.assertEqual(decision.by, "1.1.55")
        self.assertIs(decision.site, Site.SARVA)

    def test_sit_takes_the_whole_even_when_short(self):
        """7.1.20 जश्शसोः शिः — कुण्डानि तिष्ठन्ति."""
        decision = substitution_site(Adesa("i", frozenset("ś")))
        self.assertEqual(decision.by, "1.1.55")
        self.assertIs(decision.site, Site.SARVA)

    def test_ngit_beats_anekal_which_is_the_whole_point_of_1_1_53(self):
        """
        ङिच्च य आदेशः, सोऽनेकालपि अलोऽन्त्यस्य स्थाने भवति.

        आनङ् at 6.3.25 is both ṅit and anekāl. Test 1.1.55 first and 1.1.53
        can never fire; this is the case that fixes the order.
        """
        anang = Adesa("ān", frozenset("ṅ"))
        self.assertTrue(anang.anekal, "the premise: it is anekāl")
        self.assertTrue(anang.ngit)
        decision = substitution_site(anang)
        self.assertEqual(decision.by, "1.1.53")
        self.assertIs(decision.site, Site.ANTYA)
        # and without the ṅ it would have gone the other way
        self.assertEqual(substitution_site(Adesa("ān")).by, "1.1.55")

    def test_pancami_wins_over_everything(self):
        decision = substitution_site(Adesa("ī"), pancami=True)
        self.assertEqual(decision.by, "1.1.54")
        self.assertIs(decision.site, Site.ADI)
        # even for a substitute that would otherwise take the whole
        self.assertEqual(
            substitution_site(Adesa("bhū"), pancami=True).by, "1.1.54"
        )

    def test_each_decision_names_the_sutra_and_gives_a_reason(self):
        for adesa in [Adesa("i"), Adesa("bhū"), Adesa("ān", frozenset("ṅ")),
                      Adesa("i", frozenset("ś"))]:
            decision = substitution_site(adesa)
            self.assertTrue(decision.by.startswith("1.1."), decision)
            self.assertTrue(decision.why, decision)


class ReadFromTheText(unittest.TestCase):
    """1.1.54's trigger is the sūtra's own case marking."""

    def test_the_kasikas_two_pancami_examples(self):
        """
        क्व च परस्य कार्यं शिष्यते? यत्र पञ्चमीनिर्देशः.
        """
        self.assertEqual(pancami_padas("7.2.83"), ("आसः",))
        self.assertEqual(pancami_padas("6.3.97"), ("द्वि-अन्तर्-उपसर्गेभ्यः",))

    def test_the_1_1_52_and_1_1_55_examples_stand_in_the_sixth_instead(self):
        for sutra_id in ("1.2.50", "2.4.52", "7.1.20", "6.3.25"):
            self.assertEqual(pancami_padas(sutra_id), (), sutra_id)
            self.assertTrue(sthanin_padas(sutra_id), sutra_id)

    def test_site_for_routes_each_example_to_its_own_sutra(self):
        expected = {
            "1.2.50": ("1.1.52", Adesa("i")),
            "2.4.52": ("1.1.55", Adesa("bhū")),
            "7.1.20": ("1.1.55", Adesa("i", frozenset("ś"))),
            "6.3.25": ("1.1.53", Adesa("ān", frozenset("ṅ"))),
            "7.2.83": ("1.1.54", Adesa("ī")),
        }
        for sutra_id, (by, adesa) in expected.items():
            self.assertEqual(site_for(sutra_id, adesa).by, by, sutra_id)

    def test_the_fifth_and_sixth_cases_never_both_drive_one_rule_here(self):
        """
        1.1.49 reads the sixth, 1.1.54 the fifth. 6.3.97 has both, which is why
        site_for takes the pañcamī as decisive rather than as merely present —
        the fifth names the environment, the sixth the sthānin.
        """
        both = [
            s for s in ("7.2.83", "6.3.97")
            if pancami_padas(s) and sthanin_padas(s)
        ]
        self.assertEqual(both, ["6.3.97"])
        self.assertEqual(site_for("6.3.97", Adesa("ī")).by, "1.1.54")

    def test_one_word_can_stand_in_both_cases_in_the_same_sutra(self):
        """
        3.4.84 ब्रुवः पञ्चानामादित आहो ब्रुवः states ब्रुवः twice over, once in
        the fifth and once in the sixth: āha replaces the first five endings OF
        bruvaḥ, AFTER bruvaḥ. So the two readings select padas and not
        word-forms, and a disjointness check on strings would be wrong — as an
        earlier version of this test wrongly assumed.
        """
        self.assertIn("ब्रुवः", pancami_padas("3.4.84"))
        self.assertIn("ब्रुवः", sthanin_padas("3.4.84"))
        cases = sorted(
            p.vibhakti for p in facts("3.4.84").padas if p.word == "ब्रुवः"
        )
        self.assertEqual(cases, [PANCAMI, SASTHI])

    def test_a_shared_word_always_means_the_sutra_states_it_twice(self):
        """
        The invariant that does hold, and a real check on the corpus: one pada
        cannot carry two cases. So wherever the fifth and sixth readings return
        the same word, that word must occur more than once in the padaccheda.
        """
        shared_anywhere = 0
        for sutra_id in all_sutra_ids():
            shared = set(pancami_padas(sutra_id)) & set(sthanin_padas(sutra_id))
            for word in shared:
                shared_anywhere += 1
                occurrences = [
                    pada for pada in facts(sutra_id).padas if pada.word == word
                ]
                self.assertGreater(
                    len(occurrences), 1, f"{sutra_id}: {word} in two cases"
                )
        self.assertGreater(shared_anywhere, 0, "the check would be vacuous")

    def test_the_case_numbers_are_the_traditional_ones(self):
        self.assertEqual((PANCAMI, SASTHI), (5, 6))
        for sutra_id in ("7.2.83",):
            cases = {p.word: p.vibhakti for p in facts(sutra_id).padas}
            self.assertEqual(cases["आसः"], PANCAMI)


class Applying(unittest.TestCase):
    """The substitution actually carried out."""

    def test_1_1_52_id_gonyah(self):
        """1.2.50 इद् गोण्याः — पञ्चगोणिः."""
        self.assertEqual(apply_adesa("goṇī", Adesa("i")), "goṇi")

    def test_1_1_55_asterbhuh(self):
        """2.4.52 अस्तेर्भूः — अस् is replaced entire."""
        self.assertEqual(apply_adesa("as", Adesa("bhū")), "bhū")

    def test_1_1_53_anang_takes_only_the_final(self):
        """6.3.25 आनङ् ऋतो द्वन्द्वे — the ṛ of होतृ goes, the stem stays."""
        self.assertEqual(
            apply_adesa("hotṛ", Adesa("ān", frozenset("ṅ"))), "hotān"
        )

    def test_1_1_54_acts_on_what_follows_not_on_the_trigger(self):
        """
        7.2.83 ईदासः — ī replaces the first sound of what comes AFTER आस्.
        In आस् + आन the ā of आन becomes ī, giving आसीन: आसीनो यजते.
        """
        self.assertEqual(replace_adi("āna", "ī"), "īna")
        self.assertEqual("ās" + replace_adi("āna", "ī"), "āsīna")

    def test_adi_and_antya_are_genuinely_opposite_ends(self):
        self.assertEqual(replace_adi("goṇī", "i"), "ioṇī")
        self.assertEqual(apply_adesa("goṇī", Adesa("i")), "goṇi")

    def test_the_first_sound_is_a_sound_not_a_character(self):
        self.assertEqual(replace_adi("bhū", "k"), "kū")
        self.assertEqual(replace_adi("aurasa", "i"), "irasa")

    def test_an_empty_form_yields_the_substitute_at_either_end(self):
        self.assertEqual(replace_adi("", "i"), "i")
        self.assertEqual(apply_adesa("", Adesa("i")), "i")


class Registration(unittest.TestCase):
    IDS = ("1.1.53", "1.1.54", "1.1.55")

    def setUp(self):
        from src.astadhyayi.sutra import REGISTRY
        self.registry = REGISTRY

    def test_each_is_registered_and_executable(self):
        for sutra_id in self.IDS:
            sutra = self.registry.get(sutra_id)
            self.assertIsNotNone(sutra, sutra_id)
            self.assertTrue(callable(sutra.apply), sutra_id)

    def test_1_1_52_no_longer_records_the_overrides_as_missing(self):
        """The SCOPE note there was discharged by codifying these three."""
        notes = self.registry.get("1.1.52").notes
        self.assertNotIn("codified yet", notes)
        for sutra_id in self.IDS:
            self.assertIn(sutra_id, notes)

    def test_the_it_dependency_is_recorded_as_scope(self):
        """
        Adesa.its is supplied by hand because 1.3.2–1.3.9 are not codified.
        That is a real limitation and has to be findable in the record.
        """
        notes = self.registry.get("1.1.55").notes
        self.assertIn("SCOPE", notes)
        self.assertIn("1.3.2", notes)

    def test_all_four_sutras_of_the_block_carry_the_anuvrtti(self):
        for sutra_id in ("1.1.52", "1.1.53", "1.1.54", "1.1.55"):
            carried = " ".join(self.registry.get(sutra_id).anuvrtti)
            self.assertIn("1.1.49", carried, sutra_id)


if __name__ == "__main__":
    unittest.main()
