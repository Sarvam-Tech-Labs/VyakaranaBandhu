# -*- coding: utf-8 -*-
"""
७.१.९–३३ — what the case ending becomes.

Twenty-five sūtras, and between them most of how a noun declines.
The tests are written on the Kāśikā's own forms, and the classes
follow the shape of the run: the अ-final stem, then the pronoun,
then the neuter, then युष्मद् and अस्मद् on their own.
"""

from __future__ import annotations

import unittest

from src.astadhyayi.sup_adesa import (
    ATAH_RUN,
    DATARADI_FIVE,
    NASI_NI,
    PURVADI_NINE,
    SUP_RUN,
    SUP_TABLE,
    TA_NASI_NAS,
    THE_TWO,
    YUSMAD_RUN,
    case_ending,
    provisions_for,
)
from src.astadhyayi.sources import REGISTRY
import src.astadhyayi.rules  # noqa: F401  (populates REGISTRY)


class TheAFinalStem(unittest.TestCase):
    """7.1.9–13, under the अतः heading."""

    def test_bhis_becomes_ais(self):
        # वृक्षैः, प्लक्षैः.
        got = case_ending("bhis", after="a-anta")
        self.assertEqual(got.sutra, "7.1.9")
        self.assertEqual(got.does, "ais")

    def test_the_heading_stops_at_the_sutra_the_vrtti_names(self):
        # अत इत्यधिकारो जसः शी इति यावत् — 7.1.17 and no further.
        self.assertEqual(ATAH_RUN, ("7.1.9", "7.1.17"))
        self.assertLess(ATAH_RUN[1], SUP_RUN[1])

    def test_three_endings_take_three_substitutes(self):
        # वृक्षेण, वृक्षात्, वृक्षस्य — one to one.
        self.assertEqual(len(TA_NASI_NAS), 3)
        for named, shape in TA_NASI_NAS:
            got = case_ending(named, after="a-anta")
            self.assertEqual(got.sutra, "7.1.12", named)
            self.assertEqual(got.does, shape, named)

    def test_a_crossed_pairing_reaches_nothing(self):
        # टा gives इन and not स्य.
        self.assertEqual(
            case_ending("ṭā", after="a-anta", wants="sya").sutra, "")

    def test_the_dative_becomes_ya(self):
        # वृक्षाय.
        got = case_ending("ṅe", after="a-anta")
        self.assertEqual(got.sutra, "7.1.13")
        self.assertEqual(got.does, "ya")

    def test_none_of_them_reaches_a_stem_that_is_not_a_final(self):
        # अग्निभिः, सख्या, सख्ये — the heading's own condition.
        for ending in ("bhis", "ṭā", "ṅe"):
            self.assertEqual(case_ending(ending).sutra, "", ending)


class TheVedaCutsBothWays(unittest.TestCase):
    """7.1.10's बहुलम्, and 7.1.11's refusal."""

    def test_the_veda_reaches_what_the_general_rule_could_not(self):
        # नद्यैः has no अ-final stem and takes ऐस् anyway.
        got = case_ending("bhis", chandasi=True)
        self.assertEqual(got.sutra, "7.1.10")
        self.assertTrue(provisions_for("7.1.10")[0].bahulam)

    def test_idam_and_adas_refuse_the_ais(self):
        # एभिः, अमीभिः.
        for stem in ("idam", "adas"):
            got = case_ending("bhis", stem=stem, after="a-anta")
            self.assertEqual(got.sutra, "7.1.11", stem)
            self.assertEqual(got.does, "", stem)
            self.assertIn("7.1.9", got.blocked_by)

    def test_the_refusal_lapses_where_a_ka_stands_inside(self):
        # इमकैः, अमुकैः — and the vṛtti reads the अकोः as proof
        # that a word with something inserted is still that word.
        got = case_ending("bhis", stem="idam", after="a-anta",
                          case="ka")
        self.assertNotEqual(got.sutra, "7.1.11")


class ThePronoun(unittest.TestCase):
    """7.1.14–17, and the nine that make them optional."""

    def test_the_dative_becomes_smai(self):
        # सर्वस्मै, यस्मै, कस्मै — and भवते keeps its य.
        got = case_ending("ṅe", after="sarvanāma")
        self.assertEqual(got.sutra, "7.1.14")
        self.assertEqual(got.does, "smai")
        self.assertIn("7.1.13", got.blocked_by)

    def test_two_more_take_smat_and_smin(self):
        # सर्वस्मात्, सर्वस्मिन्.
        self.assertEqual(len(NASI_NI), 2)
        for named, shape in NASI_NI:
            got = case_ending(named, after="sarvanāma")
            self.assertEqual(got.sutra, "7.1.15", named)
            self.assertEqual(got.does, shape, named)

    def test_nine_pronouns_make_those_two_optional(self):
        # पूर्वस्मात् beside पूर्वात्, स्वस्मिन् beside स्वे.
        self.assertEqual(len(PURVADI_NINE), 9)
        for stem in PURVADI_NINE:
            for named in ("ṅasi", "ṅi"):
                got = case_ending(named, stem=stem,
                                  after="sarvanāma")
                self.assertEqual(got.sutra, "7.1.16", (stem, named))
                self.assertTrue(got.optional, (stem, named))

    def test_a_pronoun_outside_the_nine_has_no_option(self):
        # त्यस्मात्, त्यस्मिन्.
        got = case_ending("ṅasi", stem="tyad", after="sarvanāma")
        self.assertEqual(got.sutra, "7.1.15")
        self.assertFalse(got.optional)

    def test_the_nominative_plural_becomes_si(self):
        # सर्वे, ये, के, ते.
        got = case_ending("jas", after="sarvanāma")
        self.assertEqual(got.sutra, "7.1.17")
        self.assertEqual(got.does, "śī")


class TheNeuter(unittest.TestCase):
    """7.1.19–26, four rules deep at its deepest."""

    def test_the_dual_becomes_si(self):
        # कुण्डे, दधिनी, मधुनी.
        self.assertEqual(
            case_ending("auṅ", after="napuṃsaka").sutra, "7.1.19")

    def test_and_after_an_ap_final_stem_too(self):
        # खट्वे, बहुराजे.
        self.assertEqual(
            case_ending("auṅ", after="āp-anta").sutra, "7.1.18")

    def test_the_plural_becomes_si_short(self):
        # कुण्डानि, दधीनि, मधूनि.
        got = case_ending("jas", after="napuṃsaka")
        self.assertEqual(got.sutra, "7.1.20")
        self.assertEqual(got.does, "śi")

    def test_the_nominative_and_accusative_singular_are_dropped(self):
        # दधि, मधु, त्रपु, जतु.
        for ending in ("su", "am"):
            got = case_ending(ending, after="napuṃsaka")
            self.assertEqual(got.sutra, "7.1.23", ending)
            self.assertEqual(got.does, "luk", ending)

    def test_but_an_a_final_neuter_turns_them_into_am(self):
        # कुण्डम्, वनम्, पीठम्.
        got = case_ending("su", after="a-anta-napuṃsaka")
        self.assertEqual(got.sutra, "7.1.24")
        self.assertEqual(got.does, "am")
        self.assertIn("7.1.23", got.blocked_by)

    def test_and_five_pronouns_turn_them_into_add(self):
        # कतरत्, कतमत्, इतरत्, अन्यतरत्, अन्यत्.
        self.assertEqual(len(DATARADI_FIVE), 5)
        for stem in DATARADI_FIVE:
            got = case_ending("su", stem=stem)
            self.assertEqual(got.sutra, "7.1.25", stem)
            self.assertEqual(got.does, "aḍḍ", stem)

    def test_and_itara_in_the_veda_refuses_even_that(self):
        # मृतम् इतरम् आण्डम् — four rules deep, and the refusal
        # has to beat the three below it.
        got = case_ending("su", stem="itara", chandasi=True)
        self.assertEqual(got.sutra, "7.1.26")
        self.assertEqual(got.does, "")
        self.assertIn("7.1.25", got.blocked_by)

    def test_outside_the_veda_the_add_stands(self):
        # इतरत् काष्ठम्.
        self.assertEqual(
            case_ending("su", stem="itara").sutra, "7.1.25")


class TheNumerals(unittest.TestCase):
    """7.1.21 against 7.1.22, an exception and its rule."""

    def test_a_sat_numeral_drops_the_ending(self):
        # षट्, पञ्च, सप्त, नव, दश.
        got = case_ending("jas", after="ṣaṭ")
        self.assertEqual(got.sutra, "7.1.22")
        self.assertEqual(got.does, "luk")

    def test_asta_takes_aus_instead(self):
        # अष्टौ — and only the अष्टन् that already has its आ.
        got = case_ending("jas", stem="aṣṭan", case="kṛta-ātva")
        self.assertEqual(got.sutra, "7.1.21")
        self.assertIn("7.1.22", got.blocked_by)

    def test_the_asta_without_its_a_is_not_this_word(self):
        # अष्ट तिष्ठन्ति.
        self.assertNotEqual(
            case_ending("jas", stem="aṣṭan").sutra, "7.1.21")


class TheTwoPronouns(unittest.TestCase):
    """7.1.27–33, युष्मद् and अस्मद् ending by ending."""

    def test_the_block_is_about_exactly_two_words(self):
        self.assertEqual(THE_TWO, ("yuṣmad", "asmad"))
        self.assertEqual(YUSMAD_RUN, ("7.1.27", "7.1.33"))

    def test_each_ending_has_its_own_sutra(self):
        # तव, तुभ्यम्, युष्मान्, युष्मभ्यम्, युष्माकम्.
        wanted = {
            ("ṅas", ""): ("7.1.27", "aś"),
            ("ṅe", ""): ("7.1.28", "am"),
            ("śas", ""): ("7.1.29", "na"),
            ("bhyas", ""): ("7.1.30", "bhyam"),
            ("bhyas", "pañcamī"): ("7.1.31", "at"),
            ("ṅasi", "pañcamī-ekavacana"): ("7.1.32", "at"),
            ("sām", "āgata-suṭ"): ("7.1.33", "ākam"),
        }
        for (ending, case), (code, shape) in wanted.items():
            for stem in THE_TWO:
                got = case_ending(ending, stem=stem, case=case)
                self.assertEqual(got.sutra, code, (stem, ending))
                self.assertEqual(got.does, shape, (stem, ending))

    def test_the_same_ending_goes_two_ways_by_its_case(self):
        # भ्यस् is भ्यम् as a dative and अत् as an ablative.
        dative = case_ending("bhyas", stem="yuṣmad")
        ablative = case_ending("bhyas", stem="yuṣmad",
                               case="pañcamī")
        self.assertNotEqual(dative.does, ablative.does)
        self.assertNotEqual(dative.sutra, ablative.sutra)

    def test_the_block_does_not_reach_any_other_stem(self):
        # सर्व takes स्मै and not अम्; वृक्ष takes ऐस् and not न.
        self.assertNotEqual(
            case_ending("ṅe", after="sarvanāma").sutra, "7.1.28")
        self.assertEqual(case_ending("śas").sutra, "")


class NothingHappensByDefault(unittest.TestCase):
    """भ्याम्, सुप् and ओस् go into the word untouched."""

    def test_an_ending_no_rule_names_reaches_nothing(self):
        for ending in ("bhyām", "sup", "os"):
            got = case_ending(ending, after="a-anta")
            self.assertEqual(got.sutra, "", ending)
            self.assertEqual(got.does, "", ending)


class Registration(unittest.TestCase):
    """Every row reaches the registry with real notes."""

    def test_the_run_is_contiguous(self):
        codes = [row.sutra for row in SUP_TABLE]
        self.assertEqual(
            codes, ["7.1.%d" % n for n in range(9, 34)])

    def test_every_sutra_is_registered_with_real_notes(self):
        for row in SUP_TABLE:
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

    def test_the_endings_this_run_replaces_are_live(self):
        # 4.1.2 स्वौजसमौट्० supplies every ending named here, and
        # 2.4.71 सुपो धातुप्रातिपदिकयोः is the elision 7.1.21 says
        # it does NOT displace. Both are codified.
        self.assertTrue(REGISTRY.has("4.1.2"))
        self.assertTrue(REGISTRY.has("2.4.71"))

    def test_the_rules_these_substitutes_then_meet_are_not(self):
        # वृक्षाय needs 7.3.102's lengthening, अष्टौ needs
        # 7.2.84's आ, and युष्माकम् needs 7.1.52's सुट् to be held
        # off. None of the three is read yet; when one lands this
        # assertion fails and the note must state the live edge.
        # 7.1.52's सुट् landed with पाद ७.१ and 7.2.84's आ with
        # पाद ७.२, so युष्माकम् can be asked against the rule it
        # holds off and अष्टौ against the आ it presupposes.
        # 7.3.102's lengthening is still ahead, and when it lands
        # this assertion fails.
        # All three have landed since this was written, so
        # वृक्षाय can be asked against the lengthening it needs
        # and युष्माकम् against the सुट् it holds off. 7.4.1 is
        # still ahead.
        for code in ("7.1.52", "7.2.84", "7.3.102"):
            self.assertTrue(REGISTRY.has(code), code)
        # 7.4.1 has landed with पाद ७.४, so every rule this
        # run's substitutes go on to meet is live.
        self.assertTrue(REGISTRY.has("7.4.1"))


if __name__ == "__main__":
    unittest.main()
