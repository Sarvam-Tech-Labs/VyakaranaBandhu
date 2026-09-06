# -*- coding: utf-8 -*-
"""
७.४.२५–४० — the vowel lengthened before य्, and the क्यच् block.

One rule and four that give particular stems something else, and
then six Vedic sūtras — every one of which is only intelligible
against the form the ordinary grammar owed.
"""

from __future__ import annotations

import unittest

from src.astadhyayi.dirgha_yaki import (
    ASANAYADI,
    CHANDASI_FOUR,
    DIRGHA_RUN,
    DIRGHA_TABLE,
    DYATI_FOUR,
    KYAC_FROM,
    before_ya,
    provisions_for,
)
from src.astadhyayi.sources import REGISTRY
import src.astadhyayi.rules  # noqa: F401  (populates REGISTRY)


class TheLengthening(unittest.TestCase):
    """7.4.25–26, and what each of them keeps out."""

    def test_a_vowel_final_stem_lengthens_before_a_knit_ya(self):
        # भृशायते, चीयते, स्तूयते, चीयात्.
        got = before_ya(gana="ac-anta",
                        before="a-kṛt-a-sārvadhātuka-ya-kṅit")
        self.assertEqual(got.sutra, "7.4.25")
        self.assertEqual(got.does, "dīrgha")

    def test_the_vrtti_tests_all_three_of_its_conditions(self):
        # प्रकृत्य — a कृत्'s य्; चिनुयात् — a सार्वधातुक;
        # उरुया — the affix is not क्ङित्.
        keeps = provisions_for("7.4.25")[0].keeps_out
        for form in ("प्रकृत्य", "चिनुयात्", "उरुया"):
            self.assertIn(form, keeps, form)

    def test_and_the_same_before_cvi(self):
        # शुचीकरोति, पटूभवति.
        self.assertEqual(
            before_ya(gana="ac-anta", before="cvi").sutra,
            "7.4.26")


class WhatAnRFinalStemTakesInstead(unittest.TestCase):
    """7.4.27–30, three substitutes for one vowel."""

    def test_rin_before_a_plain_ya_and_cvi(self):
        # मात्रीयति, पित्रीयति, मात्रीभूतः.
        got = before_ya(gana="ṛ-anta",
                        before="a-kṛt-a-sārvadhātuka-ya")
        self.assertEqual(got.sutra, "7.4.27")
        self.assertEqual(got.does, "rīṅ")
        self.assertIn("7.4.25", got.blocked_by)

    def test_rin_short_before_sa_yak_and_the_optative(self):
        # आद्रियते, क्रियते, क्रियात्.
        for affix in ("śa", "yak", "liṅ"):
            got = before_ya(gana="ṛ-anta", before=affix)
            self.assertEqual(got.sutra, "7.4.28", affix)
            self.assertEqual(got.does, "riṅ", affix)

    def test_and_the_short_substitute_is_stated_against_the_length(self):
        # रिङ्वचनं दीर्घनिवृत्त्यर्थम्.
        self.assertIn("दीर्घनिवृत्त्यर्थम्",
                      provisions_for("7.4.28")[0].why)

    def test_but_a_cluster_initial_root_takes_guna(self):
        # स्मर्यते, स्मर्यात्; अर्यते, अर्यात्.
        got = before_ya(gana="ṛ-anta-saṃyoga-ādi", before="yak")
        self.assertEqual(got.sutra, "7.4.29")
        self.assertEqual(got.does, "guṇa")
        self.assertIn("7.4.28", got.blocked_by)

    def test_and_so_before_yan(self):
        # अरार्यते, सास्वर्यते, सास्मर्यते.
        self.assertEqual(
            before_ya(gana="ṛ-anta-saṃyoga-ādi",
                      before="yaṅ").sutra, "7.4.30")


class TheAFinalStem(unittest.TestCase):
    """7.4.32–33, where an अ becomes ई."""

    def test_it_becomes_i_before_cvi(self):
        # शुक्लीभवति, खट्वीकरोति.
        got = before_ya(gana="a-varṇa-anta", before="cvi")
        self.assertEqual(got.sutra, "7.4.32")
        self.assertEqual(got.does, "ī")
        self.assertIn("7.4.26", got.blocked_by)

    def test_and_before_kyac(self):
        # पुत्रीयति, घटीयति, मालीयति.
        got = before_ya(gana="a-varṇa-anta", before="kyac")
        self.assertEqual(got.sutra, "7.4.33")
        self.assertIn("7.4.25", got.blocked_by)

    def test_the_turn_is_at_the_sutra_the_module_names(self):
        self.assertEqual(KYAC_FROM, "7.4.33")

    def test_and_it_is_a_separate_sutra_for_the_six_that_follow(self):
        # पृथग्योगकरणमुत्तरार्थम्.
        self.assertIn("उत्तरार्थम्",
                      provisions_for("7.4.33")[0].why)


class TheVedicBlock(unittest.TestCase):
    """7.4.34–39, six rules and what each displaces."""

    def test_three_forms_are_laid_down_against_three_senses(self):
        # अशनायति of hunger, उदन्यति of thirst, धनायति of greed.
        self.assertEqual(len(ASANAYADI), 3)
        for form, _sense in ASANAYADI:
            got = before_ya(form, before="kyac")
            self.assertEqual(got.sutra, "7.4.34", form)
            self.assertTrue(got.nipatana, form)

    def test_and_each_has_its_ordinary_form_beside_it(self):
        # अशनीयति, उदकीयति, धनीयति in any other sense.
        keeps = provisions_for("7.4.34")[0].keeps_out
        for form in ("अशनीयति", "उदकीयति", "धनीयति"):
            self.assertIn(form, keeps, form)

    def test_the_veda_refuses_both_rules_except_for_one_stem(self):
        # मित्रयुः, सुम्नयुः — and पुत्रीयन्तः keeps its ई.
        got = before_ya(gana="a-varṇa-anta", before="kyac",
                        chandasi=True)
        self.assertEqual(got.sutra, "7.4.35")
        self.assertEqual(set(got.blocked_by), {"7.4.25", "7.4.33"})
        self.assertIn("पुत्र", got.why)

    def test_and_the_vrtti_has_to_say_which_two_rules(self):
        # किं चोक्तम्? दीर्घत्वम् ईत्वं च — the sūtra says only
        # *what is said*.
        self.assertIn("किं चोक्तम्",
                      provisions_for("7.4.35")[0].why)

    def test_four_vedic_forms_each_record_what_was_due(self):
        # दुरस्युः for दुष्टीयति, वृषण्यति for वृषीयति.
        self.assertEqual(len(CHANDASI_FOUR), 4)
        for form, due in CHANDASI_FOUR:
            got = before_ya(form, chandasi=True)
            self.assertEqual(got.sutra, "7.4.36", form)
            self.assertTrue(due, form)
        # And the note names all four displaced forms outright.
        why = provisions_for("7.4.36")[0].why
        for owed in ("दुष्टीयति", "द्रविणीयति", "वृषीयति",
                     "रिष्टीयति"):
            self.assertIn(owed, why, owed)

    def test_two_more_take_a_and_one_takes_a_loss(self):
        # अश्वायति; देवायते in the Kāṭhaka's यजुस्; कव्यति in a ऋच्.
        self.assertEqual(
            before_ya("aśva", before="kyac", chandasi=True).sutra,
            "7.4.37")
        self.assertEqual(
            before_ya("deva", before="kyac", chandasi=True,
                      sense="kāṭhaka-yajus").sutra, "7.4.38")
        self.assertEqual(
            before_ya("kavi", before="kyac", chandasi=True,
                      sense="ṛc").sutra, "7.4.39")

    def test_one_of_them_is_read_as_proof_about_another(self):
        # एतदेव आत्ववचनं ज्ञापकं न च्छन्दस्यपुत्रस्य इति
        # दीर्घप्रतिषेधो भवतीति.
        self.assertIn("ज्ञापकं",
                      provisions_for("7.4.37")[0].why)

    def test_and_none_of_the_six_reaches_outside_the_veda(self):
        for row in DIRGHA_TABLE:
            if not row.chandasi:
                continue
            query = {}
            if row.of:
                query["stem"] = row.of[0]
            if row.gana:
                query["gana"] = row.gana
            if row.before:
                query["before"] = row.before[0]
            if row.sense:
                query["sense"] = row.sense
            self.assertNotEqual(before_ya(**query).sutra,
                                row.sutra, row.sutra)


class TheLastSutra(unittest.TestCase):
    """7.4.40, four roots before a त-initial कित्."""

    def test_four_roots_take_an_i(self):
        # निर्दितः, अवसितः, मितः, स्थितः.
        self.assertEqual(len(DYATI_FOUR), 4)
        for root in DYATI_FOUR:
            got = before_ya(root, before="ta-ādi-kit")
            self.assertEqual(got.sutra, "7.4.40", root)
            self.assertEqual(got.does, "it", root)


class NothingHappensByDefault(unittest.TestCase):
    """A consonant-final stem takes nothing from the run."""

    def test_an_unnamed_stem_reaches_nothing(self):
        got = before_ya(gana="hal-anta", before="yak")
        self.assertEqual(got.sutra, "")
        self.assertEqual(got.does, "")


class Registration(unittest.TestCase):
    """Every row reaches the registry with real notes."""

    def test_the_run_is_contiguous(self):
        self.assertEqual(DIRGHA_RUN, ("7.4.25", "7.4.40"))
        codes = [row.sutra for row in DIRGHA_TABLE]
        self.assertEqual(
            codes, ["7.4.%d" % n for n in range(25, 41)])

    def test_every_sutra_is_registered_with_real_notes(self):
        for row in DIRGHA_TABLE:
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

    def test_the_affixes_this_run_stands_before_are_live(self):
        # 3.1.8's क्यच्, 5.4.50's च्वि and 3.1.22's यङ् are the
        # three affixes almost every rule here names.
        for code in ("3.1.8", "5.4.50", "3.1.22"):
            self.assertTrue(REGISTRY.has(code), code)

    def test_and_the_abhyasa_heading_has_since_been_read(self):
        # 7.4.58 opens अभ्यासस्य and 7.4.97 closes the adhyāya.
        # Both are codified now, and 7.4.25 — the lengthening
        # this file is about — is what 7.4.24 undoes.
        self.assertTrue(REGISTRY.has("7.4.58"))
        self.assertTrue(REGISTRY.has("7.4.97"))
        self.assertTrue(REGISTRY.has("7.4.25"))


if __name__ == "__main__":
    unittest.main()
