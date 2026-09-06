# -*- coding: utf-8 -*-
"""
Tests for 1.1.20 to 1.1.27 — saṃjñās that name a class of word or affix.

Two of these are worth more than the rest as tests, because their membership
comes from outside the Aṣṭādhyāyī and is therefore checkable against a text
this project did not write. 1.1.20's six ghu roots fall out of the dhātupāṭha
and match the Kāśikā's own count of four plus two; 1.1.27's thirty-five
sarvanāmans are the Gaṇapāṭha's list, keyed to that very sūtra.

The derivation for ghu also exercises 1.3.2–1.3.9 from the far side: the shape
test runs on the it-stripped stem, so डुदाञ् only reaches दा if 1.3.5 takes
डु as a pair and 1.3.3 takes the ñ.
"""

from __future__ import annotations

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi import samjna as S
from src.astadhyayi.corpus import gana_for, load_dhatupatha
from src.astadhyayi.itsamjna import DHATU, analyze


class Ghu(unittest.TestCase):
    """1.1.20 दाधा घ्वदाप्."""

    def test_the_six_the_kasika_names(self):
        self.assertEqual(
            frozenset(S.ghu_roots()),
            frozenset({"ḍudāñ", "dāṇ", "do", "deṅ", "ḍudhāñ", "dheṭ"}),
        )

    def test_the_kasikas_count_four_of_da_form_and_two_of_dha(self):
        """दारूपाश्चत्वारो धातवो धारूपौ च द्वौ."""
        da = [r for r in S.ghu_roots()
              if analyze(r, DHATU).stem.replace("̐", "") in ("dā", "do", "de")]
        dha = [r for r in S.ghu_roots()
               if analyze(r, DHATU).stem.replace("̐", "") in ("dhā", "dhe")]
        self.assertEqual(len(da), 4, da)
        self.assertEqual(len(dha), 2, dha)

    def test_the_exclusion_is_doing_work(self):
        """
        अदाप्, with दैप् added by the Kāśikā. Both are in the dhātupāṭha with
        the right shape, so without the exclusion the list would be eight.
        """
        for excluded in ("dāp", "daip"):
            self.assertNotIn(excluded, S.ghu_roots())
            self.assertIn(
                analyze(excluded, DHATU).stem.replace("̐", ""),
                S.GHU_SHAPES,
                f"{excluded} has the shape and is kept out by name",
            )
        self.assertEqual(len(S.ghu_roots()) + len(S.NOT_GHU), 8)

    def test_the_members_are_really_in_the_dhatupatha(self):
        forms = {
            e.upadesa.replace("̐", "") for e in load_dhatupatha().values()
        }
        for root in S.ghu_roots():
            self.assertIn(root, forms, root)

    def test_it_depends_on_the_it_rules_being_right(self):
        """डुदाञ् reaches दा only if 1.3.5 takes डु and 1.3.3 takes the ñ."""
        parsed = analyze("ḍudāñ", DHATU)
        self.assertEqual(parsed.stem, "dā")
        self.assertEqual([m.by for m in parsed.its], ["1.3.5", "1.3.3"])

    def test_membership(self):
        self.assertTrue(S.is_ghu("ḍudāñ"))
        self.assertFalse(S.is_ghu("dāp"))
        self.assertFalse(S.is_ghu("bhū"))


class AdyantavatEkasmin(unittest.TestCase):
    """1.1.21 आद्यन्तवदेकस्मिन्."""

    def test_a_lone_item_is_both_ends(self):
        self.assertEqual(
            S.positions(1, 0), frozenset({S.Position.ADI, S.Position.ANTA})
        )

    def test_a_longer_sequence_behaves_ordinarily(self):
        self.assertEqual(S.positions(3, 0), frozenset({S.Position.ADI}))
        self.assertEqual(S.positions(3, 1), frozenset({S.Position.MADHYA}))
        self.assertEqual(S.positions(3, 2), frozenset({S.Position.ANTA}))

    def test_a_pair_has_no_middle(self):
        self.assertEqual(S.positions(2, 0), frozenset({S.Position.ADI}))
        self.assertEqual(S.positions(2, 1), frozenset({S.Position.ANTA}))

    def test_the_atidesa_is_what_makes_the_lone_case_different(self):
        """
        Without the sūtra a single item would be first only, or last only, and
        one of the two operations would slip past it — which is the fault the
        Kāśikā says the rule is begun to repair.
        """
        self.assertEqual(len(S.positions(1, 0)), 2)
        self.assertEqual(len(S.positions(2, 0)), 1)


class NamedAffixes(unittest.TestCase):
    """1.1.22 घ and 1.1.26 निष्ठा."""

    def test_gha(self):
        self.assertEqual(S.GHA, ("tarap", "tamap"))
        self.assertTrue(S.is_gha("tarap"))
        self.assertTrue(S.is_gha("tamap"))
        self.assertFalse(S.is_gha("tara"))

    def test_nistha(self):
        self.assertEqual(S.NISTHA, ("kta", "ktavatu"))
        self.assertTrue(S.is_nistha("kta"))
        self.assertTrue(S.is_nistha("ktavatu"))
        self.assertFalse(S.is_nistha("kti"))

    def test_the_two_sets_do_not_overlap(self):
        self.assertEqual(frozenset(S.GHA) & frozenset(S.NISTHA), frozenset())

    def test_nistha_joins_up_with_1_3_8_and_1_1_5(self):
        """
        ककारः कित्कार्यार्थः — the k of क्त is there so the affix is kit, and
        that is how चि + क्त gives चितः. Three sūtras in one derivation.
        """
        from src.astadhyayi.adesa import Adesa, guna_or_none
        from src.astadhyayi.itsamjna import PRATYAYA

        kta = Adesa.from_upadesa("kta", PRATYAYA)
        self.assertTrue(S.is_nistha("kta"))
        self.assertIn("k", kta.its)          # 1.3.8
        self.assertIsNone(guna_or_none("i", affix=kta))   # 1.1.5


class Samkhya(unittest.TestCase):
    """1.1.23 to 1.1.25."""

    def test_the_four_the_sutra_adds(self):
        self.assertEqual(S.SAMKHYA_BY_1_1_23, ("bahu", "gaṇa", "vatu", "ḍati"))
        for word in S.SAMKHYA_BY_1_1_23:
            self.assertTrue(S.is_samkhya(word), word)

    def test_bhuri_is_kept_out(self):
        """भूर्यादीनां निवृत्त्यर्थं संख्यासंज्ञा विधीयते."""
        self.assertFalse(S.is_samkhya("bhūri"))

    def test_sat_by_the_final_s(self):
        self.assertTrue(S.is_sat("ṣaṣ"))

    def test_sat_by_the_final_n(self):
        for word in ("pañcan", "saptan", "navan", "daśan"):
            self.assertTrue(S.is_sat(word), word)

    def test_the_final_is_of_the_upadesa_not_the_inflected_form(self):
        """
        अन्तग्रहणमौपदेशिकार्थम्. पञ्चन् is ṣaṭ; पञ्च, the form as it appears,
        ends in a and would not be.
        """
        self.assertTrue(S.is_sat("pañcan"))
        self.assertFalse(S.is_sat("pañca"))

    def test_satani_sahasrani_are_excluded(self):
        """तेनेह न भवति — शतानि। सहस्राणि। Numerals, but not ending in ṣ or n."""
        for word in ("śata", "sahasra"):
            self.assertTrue(S.is_samkhya(word), word)
            self.assertFalse(S.is_sat(word), word)

    def test_dati_by_1_1_25(self):
        self.assertTrue(S.is_sat("ḍati"))

    def test_samkhya_is_a_precondition_of_sat(self):
        """संख्या comes down by anuvṛtti, so a non-numeral in n is not ṣaṭ."""
        self.assertFalse(S.is_samkhya("rājan"))
        self.assertFalse(S.is_sat("rājan"))

    def test_not_every_samkhya_is_a_sat(self):
        others = [w for w in S.NUMERALS if not S.is_sat(w)]
        self.assertIn("eka", others)
        self.assertIn("dvi", others)
        self.assertGreater(len(others), 5)


class Sarvanaman(unittest.TestCase):
    """1.1.27 सर्वादीनि सर्वनामानि."""

    def test_the_list_comes_from_the_ganapatha(self):
        gana = gana_for("1.1.27")
        self.assertIsNotNone(gana)
        self.assertEqual(gana.name, "sarvādiḥ")
        self.assertEqual(S.sarvanaman_words(), gana.items)

    def test_it_has_thirty_five_members(self):
        self.assertEqual(len(S.sarvanaman_words()), 35)

    def test_it_begins_with_sarva_as_its_name_says(self):
        self.assertEqual(S.sarvanaman_words()[0], "sarva")

    def test_the_kasikas_examples_are_members(self):
        for word in ("sarva", "viśva", "ubha", "ubhaya", "tyad", "tad",
                     "yad", "etad", "idam", "adas", "kim"):
            self.assertTrue(S.is_sarvanaman(word), word)

    def test_an_ordinary_stem_is_not(self):
        for word in ("rāma", "agni", "bhūri", "vṛkṣa"):
            self.assertFalse(S.is_sarvanaman(word), word)

    def test_the_gana_is_closed_so_membership_is_decidable(self):
        """
        39 of the 262 gaṇas are ākṛtigaṇa and cannot be tested for membership.
        This is not one of them, which is what makes is_sarvanaman total.
        """
        self.assertFalse(gana_for("1.1.27").open_ended)

    def test_an_akrtigana_is_marked_as_such(self):
        """A control: 1.1.37's svarādi IS open-ended, and says so."""
        self.assertTrue(gana_for("1.1.37").open_ended)


class Registration(unittest.TestCase):
    IDS = tuple(f"1.1.{n}" for n in range(20, 28))

    def setUp(self):
        from src.astadhyayi.sutra import REGISTRY
        self.registry = REGISTRY

    def test_each_is_registered_and_executable(self):
        for sutra_id in self.IDS:
            sutra = self.registry.get(sutra_id)
            self.assertIsNotNone(sutra, sutra_id)
            self.assertTrue(callable(sutra.apply), sutra_id)

    def test_the_first_twenty_seven_are_continuous(self):
        for number in range(1, 28):
            self.assertTrue(
                self.registry.has(f"1.1.{number}"), f"1.1.{number} missing"
            )

    def test_1_1_24_and_1_1_25_read_samkhya_from_1_1_23(self):
        for sutra_id in ("1.1.24", "1.1.25"):
            carried = " ".join(self.registry.get(sutra_id).anuvrtti)
            self.assertIn("1.1.23", carried, sutra_id)

    def test_the_semantic_condition_on_1_1_23_is_recorded_as_scope(self):
        notes = self.registry.get("1.1.23").notes
        self.assertIn("SCOPE", notes)
        self.assertIn("संख्यावाचिनोरेव", notes)

    def test_the_conditions_on_three_sarvadi_members_are_now_settled(self):
        """
        The Gaṇapāṭha annotates पूर्व, स्व and अन्तर with 1.1.34, 1.1.35 and
        1.1.36. Those were recorded here as a SCOPE until they were codified.
        Checked by MARKER and not by substring: an earlier version of this test
        looked for the word "SCOPE" anywhere in the note and went on passing
        after the note was closed, because the closing paragraph mentions it.
        """
        from src.astadhyayi.report import findings

        notes = self.registry.get("1.1.27").notes
        markers = {marker for marker, _ in findings(notes)}
        self.assertNotIn("SCOPE", markers)
        self.assertIn("SETTLED", markers)
        self.assertIn("व्यवस्थायामसंज्ञायाम्", notes)
        for sutra_id in ("1.1.34", "1.1.35", "1.1.36"):
            self.assertTrue(self.registry.has(sutra_id), sutra_id)

    def test_the_new_samjnas_are_registered(self):
        from src.astadhyayi.grahana import samjna_source

        for name, sutra_id in [("ghu", "1.1.20"), ("gha", "1.1.22"),
                               ("ṣaṭ", "1.1.24"), ("niṣṭhā", "1.1.26"),
                               ("sarvanāman", "1.1.27")]:
            self.assertEqual(samjna_source(name), sutra_id, name)


if __name__ == "__main__":
    unittest.main()
