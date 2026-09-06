# -*- coding: utf-8 -*-
"""
८.४.१–३९ — रषाभ्यां नो णः, and the thirty-eight rules about it.

The last pāda opens on one rule and spends thirty-eight more on
where else it holds and where it does not. The tests take that
shape: the rule, the five things it reaches across, the
compounds and the preverbs, and then the six refusals — of which
the last is 8.4.1's own समानपदे said again from the other side.
"""

from __future__ import annotations

import unittest

from src.astadhyayi.natva import (
    BHA_BHU_SEVEN,
    NATVA_RUN,
    NATVA_TABLE,
    PRANIRADI_TEN,
    PURAGA_SIX,
    SAMANAPADE,
    VYAVAYA_FIVE,
    provisions_for,
    the_cerebral_n,
)
from src.astadhyayi.sources import REGISTRY
import src.astadhyayi.rules  # noqa: F401  (populates REGISTRY)


class TheRuleAndItsReach(unittest.TestCase):
    """8.4.1–2."""

    def test_an_n_after_an_r_or_a_sa_becomes_na_in_one_word(self):
        # आस्तीर्णम्, कुष्णाति.
        got = the_cerebral_n(gana="ra-ṣa-para-na",
                             after="samāna-pada")
        self.assertEqual(got.sutra, "8.4.1")
        self.assertEqual(got.does, "ṇa")
        self.assertIn(SAMANAPADE, provisions_for("8.4.1")[0].why)

    def test_and_the_sa_in_it_is_named_for_the_sutras_after(self):
        # षग्रहणम् उत्तरार्थम् — 8.4.41's ष्टुत्व would have
        # given the cerebral here anyway, and that rule is
        # codified.
        self.assertIn("उत्तरार्थम्", provisions_for("8.4.1")[0].why)
        self.assertTrue(REGISTRY.has("8.4.41"))

    def test_and_it_reaches_across_five_things(self):
        # करणम्, अर्केण — the ण् two sounds from its र्.
        self.assertEqual(len(VYAVAYA_FIVE), 5)
        got = the_cerebral_n(gana="ra-ṣa-para-na",
                             after="vyavāya")
        self.assertEqual(got.sutra, "8.4.2")
        self.assertIn("8.4.1", got.blocked_by)
        self.assertIn("करणम्", provisions_for("8.4.2")[0].why)


class AcrossACompoundSeam(unittest.TestCase):
    """8.4.3–13."""

    def test_a_name_lets_it_cross_the_seam(self):
        # शूर्पणखा — and 8.4.1's समानपदे would have stopped it.
        got = the_cerebral_n(after="pūrvapada", sense="saṃjñā")
        self.assertEqual(got.sutra, "8.4.3")
        self.assertNotEqual(
            the_cerebral_n(after="pūrvapada").sutra, "8.4.3")
        keeps = provisions_for("8.4.3")[0].keeps_out
        self.assertIn("चर्मनासिकः", keeps)
        self.assertIn("ऋगयनम्", keeps)

    def test_three_sutras_in_a_row_are_about_one_word(self):
        # वन after six named first members in a name, after ten
        # more either way, and after a herb or tree by choice.
        self.assertEqual(len(PURAGA_SIX), 6)
        self.assertEqual(len(PRANIRADI_TEN), 10)
        for word in PURAGA_SIX:
            self.assertEqual(
                the_cerebral_n("vana", after="puragādi",
                               sense="saṃjñā").sutra, "8.4.4")
        self.assertEqual(
            the_cerebral_n("vana", after="pranirādi").sutra,
            "8.4.5")
        got = the_cerebral_n("vana", after="oṣadhi-vanaspati")
        self.assertEqual(got.sutra, "8.4.6")
        self.assertTrue(got.optional)

    def test_and_only_the_second_of_the_three_needs_no_name(self):
        # असंज्ञायाम् अपि — the only place in the run where the
        # name is not wanted.
        self.assertIn("असंज्ञायाम्", provisions_for("8.4.5")[0].why)

    def test_two_words_take_it_from_what_stands_in_front(self):
        # पूर्वाह्णः of an अ-final; इक्षुवाहणम् of a load.
        self.assertEqual(
            the_cerebral_n("ahna",
                           after="a-anta-pūrvapada").sutra,
            "8.4.7")
        self.assertEqual(
            the_cerebral_n("vāhana", after="āhita").sutra,
            "8.4.8")

    def test_and_one_word_has_three_senses_and_two_sutras(self):
        # क्षीरपाणा उशीनराः of a country, compulsorily; and the
        # act and the vessel by choice.
        country = the_cerebral_n("pāna", after="pūrvapada",
                                 sense="deśa")
        self.assertEqual(country.sutra, "8.4.9")
        self.assertFalse(country.optional)
        for sense in ("bhāva", "karaṇa"):
            got = the_cerebral_n("pāna", after="pūrvapada",
                                 sense=sense)
            self.assertEqual(got.sutra, "8.4.10", sense)
            self.assertTrue(got.optional, sense)

    def test_and_one_option_over_three_places_is_fixed_two_ways(self):
        # माषवापिणौ by choice; वृत्रहणौ and वस्त्रयुगिणौ always.
        shape = "prātipadika-anta-num-vibhakti"
        choice = the_cerebral_n(gana=shape, after="pūrvapada")
        self.assertEqual(choice.sutra, "8.4.11")
        self.assertTrue(choice.optional)
        for after, code in (("ekāc-uttarapada", "8.4.12"),
                            ("kumat-uttarapada", "8.4.13")):
            got = the_cerebral_n(gana=shape, after=after)
            self.assertEqual(got.sutra, code, after)
            self.assertFalse(got.optional, after)
            self.assertIn("8.4.11", got.blocked_by, after)


class AfterAPreverb(unittest.TestCase):
    """8.4.14–33, twenty sūtras on one condition."""

    def test_the_rule_every_pranama_in_the_language_comes_from(self):
        # प्रणमति, परिणमति — and नम् is written णम् in the root
        # list, which is what that spelling is for.
        got = the_cerebral_n(gana="ṇopadeśa", after="upasarga")
        self.assertEqual(got.sutra, "8.4.14")
        self.assertIn("णोपदेशः", provisions_for("8.4.14")[0].why)

    def test_and_one_word_is_taken_out_of_a_refusal_seventeen_sutras_early(self):
        # हे प्राण् — 8.4.37 will refuse every word-final न्.
        got = the_cerebral_n("ani", after="upasarga",
                             gana="pada-anta")
        self.assertEqual(got.sutra, "8.4.20")
        self.assertIn("8.4.37", got.blocked_by)
        self.assertIn("अपवादोऽयम्", provisions_for("8.4.20")[0].why)

    def test_and_a_reduplicated_root_takes_it_twice(self):
        # प्राणिणिषति — a cerebral already made would not be
        # copied, so the second ण् is given outright.
        got = the_cerebral_n("ani", after="upasarga",
                             gana="sābhyāsa")
        self.assertEqual(got.sutra, "8.4.21")
        self.assertIn("अद्विर्वचने",
                      provisions_for("8.4.21")[0].why)

    def test_and_one_root_wants_a_short_a_before_its_n(self):
        # प्रहण्यते; प्रघ्नन्ति has lost the अ and प्राघानि has
        # a long one.
        got = the_cerebral_n("hanti", gana="at-pūrva",
                             after="upasarga")
        self.assertEqual(got.sutra, "8.4.22")
        keeps = provisions_for("8.4.22")[0].keeps_out
        self.assertIn("प्रघ्नन्ति", keeps)
        self.assertIn("प्राघानि", keeps)

    def test_and_antar_is_not_a_preverb_so_two_words_need_their_own_rules(self):
        # अन्तर्हण्यते and अन्तरयणम्, both only of a non-place.
        for word, code in (("hanti", "8.4.24"), ("ayana", "8.4.25")):
            query = {"after": "antar", "sense": "a-deśa"}
            if word == "hanti":
                query["gana"] = "at-pūrva"
            got = the_cerebral_n(word, **query)
            self.assertEqual(got.sutra, code, word)
        self.assertIn("अन्तर् is not a preverb",
                      provisions_for("8.4.24")[0].why)

    def test_and_one_vedic_rule_turns_on_how_a_word_is_recited(self):
        # छन्दस्यृदवग्रहात् — नृऽमनाः, पितृऽयानम्.
        got = the_cerebral_n(after="ṛ-anta-avagraha",
                             chandasi=True)
        self.assertEqual(got.sutra, "8.4.26")
        # ऋकारः + अवगृह्यते elides the अ, so the quoted
        # fragment has to begin after the अवग्रह.
        self.assertIn("वगृह्यते", provisions_for("8.4.26")[0].why)

    def test_the_krt_affixes_n_and_the_three_rules_that_qualify_it(self):
        # प्रयाणम्, प्रमाणम् always; प्रयापणम् and प्रकोपणम् by
        # choice; प्रेङ्खणम् always again.
        always = the_cerebral_n(gana="kṛt-ac-para-na",
                                after="upasarga")
        self.assertEqual(always.sutra, "8.4.29")
        for gana, code in (("ṇi-kṛt", "8.4.30"),
                           ("hal-ādi-ik-upadha-kṛt", "8.4.31")):
            got = the_cerebral_n(gana=gana, after="upasarga")
            self.assertEqual(got.sutra, code, gana)
            self.assertTrue(got.optional, gana)
        fixed = the_cerebral_n(gana="ic-ādi-sanum-kṛt",
                               after="upasarga")
        self.assertEqual(fixed.sutra, "8.4.32")
        self.assertFalse(fixed.optional)


class TheSixRefusals(unittest.TestCase):
    """8.4.34–39, where the run takes it all back."""

    def test_they_are_the_last_six_rows_and_no_others(self):
        refusing = [row.sutra for row in NATVA_TABLE if row.refuses]
        self.assertEqual(
            refusing, ["8.4.%d" % n for n in range(34, 40)])

    def test_seven_roots_refuse_it_by_name(self):
        # प्रभानम्, प्रभवनम्, प्रपवनम्.
        self.assertEqual(len(BHA_BHU_SEVEN), 7)
        for root in BHA_BHU_SEVEN:
            got = the_cerebral_n(root, after="upasarga")
            self.assertEqual(got.sutra, "8.4.34", root)
            self.assertTrue(got.refuses, root)

    def test_and_a_word_final_sa_and_a_word_final_n_refuse_it_too(self):
        # निष्पानम्; वृक्षान्, गिरीन्.
        self.assertEqual(
            the_cerebral_n(gana="ṣa-pada-anta-para").sutra,
            "8.4.35")
        got = the_cerebral_n(gana="pada-anta-na")
        self.assertEqual(got.sutra, "8.4.37")
        self.assertEqual(set(got.blocked_by), {"8.4.1", "8.4.2"})

    def test_and_one_of_them_is_the_first_sutra_said_backwards(self):
        # पदव्यवायेऽपि — 8.4.1 wanted one word and this refuses
        # where there are two: प्र गां नयामः.
        got = the_cerebral_n(gana="pada-vyavāya")
        self.assertEqual(got.sutra, "8.4.38")
        self.assertIn("समानपदे", provisions_for("8.4.38")[0].why)
        self.assertIn("from the other side",
                      provisions_for("8.4.38")[0].why)

    def test_and_the_last_reaches_the_altered_shapes_as_well(self):
        # क्षुभ्नीतः, क्षुभ्नन्ति — by स्थानिवद्भाव.
        got = the_cerebral_n(gana="kṣubhnādi")
        self.assertEqual(got.sutra, "8.4.39")
        self.assertIn("स्थानिवद्भावाद्",
                      provisions_for("8.4.39")[0].why)


class NothingHappensByDefault(unittest.TestCase):
    """A न् none of these rules reaches stands as it is."""

    def test_an_unnamed_root_reaches_nothing(self):
        got = the_cerebral_n("pac")
        self.assertEqual(got.sutra, "")
        self.assertEqual(got.does, "")


class Registration(unittest.TestCase):
    """Every row reaches the registry with real notes."""

    def test_the_run_opens_the_last_pada(self):
        self.assertEqual(NATVA_RUN, ("8.4.1", "8.4.39"))
        codes = [row.sutra for row in NATVA_TABLE]
        self.assertEqual(
            codes, ["8.4.%d" % n for n in range(1, 40)])

    def test_every_sutra_is_registered_with_real_notes(self):
        for row in NATVA_TABLE:
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
        # 8.4.41's ष्टुत्व, which 8.4.1's ष् is named for;
        # 5.4.88's अह्न, which 8.4.7 acts on; and 8.4.37, which
        # 8.4.20 excepts a word from before it is stated.
        for code in ("8.4.41", "5.4.88", "8.4.37"):
            self.assertTrue(REGISTRY.has(code), code)


if __name__ == "__main__":
    unittest.main()
