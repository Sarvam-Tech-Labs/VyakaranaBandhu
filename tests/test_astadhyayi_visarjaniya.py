# -*- coding: utf-8 -*-
"""
८.३.३४–५४ — what the visarga becomes, and where it stays.

Twenty-one sūtras on one sound. The tests take the four rules
that say what it turns into first, then the seventeen that say
when it is स् or ष् anyway — and end on the two that turn on the
CASE of the word, which nothing else in the pāda does.
"""

from __future__ import annotations

import unittest

from src.astadhyayi.visarjaniya import (
    DVIS_THREE,
    KRKAMI_SEVEN,
    NIRADI,
    PASA_FOUR,
    PATI_SEVEN,
    THE_VISARGA,
    VISARGA_RUN,
    VISARGA_TABLE,
    provisions_for,
    the_visarga,
)
from src.astadhyayi.sources import REGISTRY
import src.astadhyayi.rules  # noqa: F401  (populates REGISTRY)


class WhatTheVisargaTurnsInto(unittest.TestCase):
    """8.3.34–37, four answers to one question."""

    def test_before_a_khar_it_becomes_s(self):
        # वृक्षश्छादयति, वृक्षस्तरति.
        got = the_visarga(gana="visarjanīya", before="khar")
        self.assertEqual(got.sutra, "8.3.34")
        self.assertEqual(got.does, "sa")

    def test_but_with_a_sar_after_that_khar_it_stays(self):
        # शशः क्षुरम्; वासः क्षौमम्.
        got = the_visarga(gana="visarjanīya",
                          before="khar-śar-para")
        self.assertEqual(got.sutra, "8.3.35")
        self.assertEqual(got.does, "visarjanīya")
        self.assertIn("8.3.34", got.blocked_by)

    def test_and_before_a_sar_it_may_do_either(self):
        # वृक्षः शेते, वृक्षश्शेते.
        got = the_visarga(gana="visarjanīya", before="śar")
        self.assertEqual(got.sutra, "8.3.36")
        self.assertTrue(got.optional)

    def test_and_before_a_guttural_or_labial_it_has_a_sound_of_its_own(self):
        # वृक्ष≍करोति — the जिह्वामूलीय and the उपध्मानीय, which
        # Sanskrit writes and almost never prints.
        for after in ("ku", "pu"):
            got = the_visarga(gana="visarjanīya", before=after)
            self.assertEqual(got.sutra, "8.3.37", after)
            self.assertEqual(got.does, "ka-pa", after)
            self.assertTrue(got.optional, after)


class WhenItIsSOrSaAnyway(unittest.TestCase):
    """8.3.38–48, eleven conditions on one substitute."""

    def test_not_at_a_words_head_and_after_an_in(self):
        # पयस्पाशम्; सर्पिष्पाशम्.
        plain = the_visarga(gana="visarjanīya",
                            before="ku-pu-a-pada-ādi")
        self.assertEqual(plain.sutra, "8.3.38")
        self.assertEqual(plain.does, "sa")
        after_in = the_visarga(gana="iṇ-para-visarjanīya",
                               before="ku-pu-a-pada-ādi")
        self.assertEqual(after_in.sutra, "8.3.39")
        self.assertEqual(after_in.does, "ṣa")
        self.assertIn("8.3.38", after_in.blocked_by)

    def test_and_four_affixes_make_the_whole_of_that_scope(self):
        # पाश, कल्प, क, काम्य — the only things that put a क or
        # a प after a word without beginning one.
        self.assertEqual(len(PASA_FOUR), 4)
        self.assertIn("पाश", provisions_for("8.3.38")[0].why)

    def test_two_preverbs_take_it_and_a_third_only_by_choice(self):
        # नमस्कर्ता, पुरस्कर्ता; तिरस्कर्ता beside तिरः कर्ता.
        for word in ("namas", "puras"):
            got = the_visarga(word, gana="gati", before="ku")
            self.assertEqual(got.sutra, "8.3.40", word)
            self.assertFalse(got.optional, word)
        got = the_visarga("tiras", gana="gati", before="ku")
        self.assertEqual(got.sutra, "8.3.42")
        self.assertTrue(got.optional)

    def test_and_all_three_want_the_word_to_be_a_preverb(self):
        # गत्योः इति किम्? नमः कृत्वा — and गतेः is carried down
        # into 8.3.42 two sūtras later.
        self.assertIn("नमः कृत्वा",
                      provisions_for("8.3.40")[0].keeps_out)
        self.assertIn("गतेः", provisions_for("8.3.42")[0].why)

    def test_a_shape_that_is_really_a_list_of_six_words(self):
        # निर्, दुर्, बहिर्, आविस्, चतुर्, प्रादुस्.
        self.assertEqual(len(NIRADI), 6)
        for word in NIRADI:
            got = the_visarga(word,
                              gana="i-u-upadha-a-pratyaya",
                              before="ku")
            self.assertEqual(got.sutra, "8.3.41", word)

    def test_three_words_take_it_only_of_a_number_of_times(self):
        # द्विष्करोति — and the sense is what tells this चतुर्
        # from 8.3.41's.
        self.assertEqual(DVIS_THREE, ("dvis", "tris", "catur"))
        for word in DVIS_THREE:
            got = the_visarga(word, before="ku",
                              sense="kṛtvo'rtha")
            self.assertEqual(got.sutra, "8.3.43", word)
            self.assertTrue(got.optional, word)

    def test_and_a_compound_turns_one_choice_into_a_certainty(self):
        # सर्पिः करोति optionally, सर्पिष्कुण्डिका always.
        choice = the_visarga(gana="is-us-anta", before="ku",
                             sense="sāmarthya")
        self.assertEqual(choice.sutra, "8.3.44")
        self.assertTrue(choice.optional)
        fixed = the_visarga(gana="is-us-anta", before="ku",
                            sense="samāsa")
        self.assertEqual(fixed.sutra, "8.3.45")
        self.assertFalse(fixed.optional)
        self.assertIn("8.3.44", fixed.blocked_by)

    def test_and_two_more_compound_rules_name_their_second_member(self):
        # अयस्कारः before seven words; अधस्पदम् before one.
        self.assertEqual(len(KRKAMI_SEVEN), 7)
        for word in KRKAMI_SEVEN:
            self.assertEqual(
                the_visarga(gana="a-anta-an-avyaya", before=word,
                            sense="samāsa").sutra, "8.3.46", word)
        self.assertEqual(
            the_visarga("adhas", before="pada",
                        sense="samāsa").sutra, "8.3.47")

    def test_and_one_class_is_a_list_of_finished_words(self):
        # कस्कः, भ्रातुष्पुत्रः — यथायोगम् sorts out which of
        # the two sounds each takes.
        got = the_visarga(gana="kaskādi", before="ku")
        self.assertEqual(got.sutra, "8.3.48")
        self.assertIn("यथायोगम्", provisions_for("8.3.48")[0].why)


class TheSixVedicRules(unittest.TestCase):
    """8.3.49–54, and the two that turn on a case."""

    def test_the_widest_of_them_needs_no_condition_on_the_word(self):
        # अयस्पात्रम् — except before प्र and an आम्रेडित.
        got = the_visarga(gana="visarjanīya", before="ku",
                          chandasi=True)
        self.assertEqual(got.sutra, "8.3.49")
        self.assertTrue(got.optional)
        self.assertNotEqual(
            the_visarga(gana="visarjanīya", before="ku").sutra,
            "8.3.49")

    def test_and_one_names_five_forms_of_one_root(self):
        # कः, करत्, करति, कृधि, कृत — where a class would have
        # done.
        for after in ("kaḥ", "karat", "karati", "kṛdhi", "kṛta"):
            self.assertEqual(
                the_visarga(gana="a-aditi-visarjanīya",
                            before=after, chandasi=True).sutra,
                "8.3.50", after)

    def test_two_rules_turn_on_the_case_and_nothing_else_does(self):
        # पञ्चम्याः before परि, षष्ठ्याः before seven words.
        self.assertEqual(
            the_visarga(case="pañcamī", before="pari",
                        sense="adhi", chandasi=True).sutra,
            "8.3.51")
        self.assertEqual(len(PATI_SEVEN), 7)
        for word in PATI_SEVEN:
            self.assertEqual(
                the_visarga(case="ṣaṣṭhī", before=word,
                            chandasi=True).sutra, "8.3.53", word)
        with_case = [row.sutra for row in VISARGA_TABLE if row.case]
        self.assertEqual(with_case,
                         ["8.3.51", "8.3.52", "8.3.53", "8.3.54"])

    def test_and_one_word_is_taken_out_of_the_last_of_them(self):
        # इडायास्पतिः beside इडायाः पतिः.
        got = the_visarga("iḍā", case="ṣaṣṭhī", before="pati",
                          chandasi=True)
        self.assertEqual(got.sutra, "8.3.54")
        self.assertTrue(got.optional)
        self.assertIn("8.3.53", got.blocked_by)

    def test_and_one_of_them_records_that_the_corpus_disagrees(self):
        # बहुलम् — दिवस्पातु, and न च भवति, परिषदः पातु.
        row = provisions_for("8.3.52")[0]
        self.assertTrue(row.optional)
        self.assertIn("परिषदः पातु", row.keeps_out)


class NothingHappensByDefault(unittest.TestCase):
    """A visarga none of these rules reaches is left alone."""

    def test_an_unnamed_junction_reaches_nothing(self):
        got = the_visarga(gana="visarjanīya", before="avasāna")
        self.assertEqual(got.sutra, "")
        self.assertIn("8.3.15", got.why)


class Registration(unittest.TestCase):
    """Every row reaches the registry with real notes."""

    def test_the_run_is_contiguous(self):
        self.assertEqual(VISARGA_RUN, ("8.3.34", "8.3.54"))
        codes = [row.sutra for row in VISARGA_TABLE]
        self.assertEqual(
            codes, ["8.3.%d" % n for n in range(34, 55)])

    def test_the_rule_that_makes_the_visarga_is_codified_apart(self):
        self.assertEqual(THE_VISARGA, "8.3.15")
        self.assertTrue(REGISTRY.has(THE_VISARGA))
        self.assertNotIn(THE_VISARGA,
                         [row.sutra for row in VISARGA_TABLE])

    def test_every_sutra_is_registered_with_real_notes(self):
        for row in VISARGA_TABLE:
            self.assertTrue(REGISTRY.has(row.sutra), row.sutra)
            notes = REGISTRY.get(row.sutra).notes
            self.assertGreater(len(notes), 100, row.sutra)
            self.assertIn("SETTLED", notes, row.sutra)


class WhatIsNotCodifiedYet(unittest.TestCase):
    """
    The debts, written as the exact shortfall.

    Each fails the moment the thing it names lands, and must then
    be rewritten to state the live dependency instead.
    """

    def test_everything_this_run_appeals_to_is_live(self):
        # 8.3.15's visarga, 5.3.47's पाशप्, 5.3.67's कल्पप् and
        # 1.4.60's गति name. All codified.
        for code in ("8.3.15", "5.3.47", "5.3.67", "1.4.60"):
            self.assertTrue(REGISTRY.has(code), code)


if __name__ == "__main__":
    unittest.main()
