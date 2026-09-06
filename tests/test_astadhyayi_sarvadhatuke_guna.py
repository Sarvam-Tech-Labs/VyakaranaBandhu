# -*- coding: utf-8 -*-
"""
७.३.८५–१०० — guṇa and vṛddhi before a सार्वधातुक, and the ईट्.

Sixteen sūtras following on a rule codified long before them.
The tests ask what each adds to 7.3.84, and end on the three
that give one list of roots two augments in two teachers' names.
"""

from __future__ import annotations

import unittest

from src.astadhyayi.sarvadhatuke_guna import (
    AUGMENTS_FROM,
    GARGYA_GALAVA,
    GUNA_RUN,
    GUNA_TABLE,
    PUJARTHAM,
    RUDADI_FIVE,
    TU_RU_FIVE,
    before_sarvadhatuka,
    provisions_for,
)
from src.astadhyayi.sources import REGISTRY
import src.astadhyayi.rules  # noqa: F401  (populates REGISTRY)


class WhatItAddsToTheGunaBeforeIt(unittest.TestCase):
    """7.3.84 is codified apart, and this run widens it."""

    def test_the_rule_it_follows_on_is_live(self):
        self.assertTrue(REGISTRY.has("7.3.84"))
        self.assertEqual(GUNA_RUN[0], "7.3.85")

    def test_a_light_penult_takes_guna_too(self):
        # भेदनम्, छेदनम्, भेत्ता, छेत्ता.
        got = before_sarvadhatuka(gana="pug-anta-laghu-upadha",
                                  before="ārdhadhātuka")
        self.assertEqual(got.sutra, "7.3.86")
        self.assertEqual(got.does, "guṇa")

    def test_and_a_verse_asks_how_bhetta_is_possible(self):
        # संयोगे गुरुसंज्ञायां गुणो भेत्तुर्न सिध्यति — with the
        # affix's cluster after it the penult is heavy. The
        # answer is read out of two rules' कित् marking.
        why = provisions_for("7.3.86")[0].why
        self.assertIn("गुरुसंज्ञायां", why)
        for code in ("3.2.140", "1.2.10"):
            self.assertIn(code, why, code)
            self.assertTrue(REGISTRY.has(code), code)

    def test_jagr_takes_it_so_that_the_vrddhi_shall_not(self):
        # जागरयति — and once the guṇa is in, 7.2.116 has no अ in
        # the penult to work on.
        got = before_sarvadhatuka("jāgṛ")
        self.assertEqual(got.sutra, "7.3.85")
        self.assertIn("7.2.116", got.blocked_by)


class WhatRefusesIt(unittest.TestCase):
    """7.3.87 and 7.3.88."""

    def test_a_reduplicated_stem_refuses_it_before_a_vowel(self):
        # नेनिजानि, वेविजानि, अनेनिजम्.
        got = before_sarvadhatuka(gana="abhyasta-laghu-upadha",
                                  before="ac-ādi-pit-sārvadhātuka")
        self.assertEqual(got.sutra, "7.3.87")
        self.assertEqual(got.does, "")
        self.assertIn("7.3.86", got.blocked_by)

    def test_and_two_roots_refuse_it_before_a_tin(self):
        # अभूत्, सुवै.
        for root in ("bhū", "sū"):
            got = before_sarvadhatuka(root, before="tiṅ")
            self.assertEqual(got.sutra, "7.3.88", root)
            self.assertIn("7.3.84", got.blocked_by, root)

    def test_why_bobhaviti_keeps_its_guna_is_proved_from_elsewhere(self):
        # ज्ञापकात्, यदयं बोभूतु इति गुणाभावार्थं निपातनं करोति —
        # 7.4.65 lays down बोभूतु expressly without guṇa, and
        # would not need to if this refusal reached there.
        self.assertIn("7.4.65", provisions_for("7.3.88")[0].why)


class TheVrddhiInstead(unittest.TestCase):
    """7.3.89–91, three rules for one environment."""

    def test_an_u_final_stem_takes_vrddhi_after_a_luk(self):
        # यौति, नौति, स्तौति.
        got = before_sarvadhatuka(
            gana="u-anta", before="hal-ādi-pit-sārvadhātuka",
            result="luk")
        self.assertEqual(got.sutra, "7.3.89")
        self.assertEqual(got.does, "vṛddhi")

    def test_urnu_takes_it_optionally(self):
        # प्रोर्णौति beside प्रोर्णोति.
        got = before_sarvadhatuka(
            "ūrṇu", before="hal-ādi-pit-sārvadhātuka")
        self.assertEqual(got.sutra, "7.3.90")
        self.assertTrue(got.optional)

    def test_but_guna_where_the_ending_is_a_single_sound(self):
        # प्रौर्णोत्, प्रौर्णोः.
        got = before_sarvadhatuka(
            "ūrṇu", before="apṛkta-hal-pit-sārvadhātuka")
        self.assertEqual(got.sutra, "7.3.91")
        self.assertEqual(got.does, "guṇa")
        self.assertIn("7.3.90", got.blocked_by)

    def test_and_the_word_aprkta_is_read_as_teaching_a_maxim(self):
        # हलि was already running, so naming the single-sound
        # ending adds nothing unless a paribhāṣā is being taught.
        self.assertIn("परिभाषा",
                      provisions_for("7.3.91")[0].why)


class TheAugments(unittest.TestCase):
    """7.3.92–100, where the run stops strengthening."""

    def test_the_turn_is_at_the_sutra_the_module_names(self):
        self.assertEqual(AUGMENTS_FROM, "7.3.92")

    def test_everything_from_there_supplies_an_augment(self):
        def number(code):
            return int(code.rsplit(".", 1)[1])

        for row in GUNA_TABLE:
            if number(row.sutra) >= number(AUGMENTS_FROM):
                self.assertTrue(row.augment, row.sutra)

    def test_and_nothing_before_it_does(self):
        def number(code):
            return int(code.rsplit(".", 1)[1])

        for row in GUNA_TABLE:
            if number(row.sutra) < number(AUGMENTS_FROM):
                self.assertFalse(row.augment, row.sutra)

    def test_trnah_takes_an_im_and_bru_an_it(self):
        # तृणेढि; ब्रवीति.
        self.assertEqual(
            before_sarvadhatuka(
                "tṛṇah",
                before="hal-ādi-pit-sārvadhātuka").does, "im")
        self.assertEqual(
            before_sarvadhatuka(
                "brū", before="hal-ādi-pit-sārvadhātuka").does,
            "īṭ")

    def test_five_roots_take_the_it_optionally(self):
        # उत्तौति beside उत्तवीति; अभ्यमति beside अभ्यमीति.
        self.assertEqual(len(TU_RU_FIVE), 5)
        for root in TU_RU_FIVE:
            got = before_sarvadhatuka(
                root, before="hal-ādi-sārvadhātuka")
            self.assertEqual(got.sutra, "7.3.95", root)
            self.assertTrue(got.optional, root)

    def test_as_and_the_sic_take_it_before_a_single_sound(self):
        # आसीत्, अकार्षीत्, असावीत्.
        for root in ("as", "sic"):
            self.assertEqual(
                before_sarvadhatuka(
                    root, before="apṛkta-sārvadhātuka").sutra,
                "7.3.96", root)

    def test_and_the_veda_takes_it_bahulam(self):
        # आप एवेदं सलिलं सर्वम् आः; गोभिरक्षाः.
        got = before_sarvadhatuka("as",
                                  before="apṛkta-sārvadhātuka",
                                  chandasi=True)
        self.assertEqual(got.sutra, "7.3.97")
        self.assertTrue(provisions_for("7.3.97")[0].bahulam)


class OneListOfRootsAndTwoAugments(unittest.TestCase):
    """7.3.98–100, and what naming a teacher does here."""

    def test_the_five_are_the_same_five_a_pada_back(self):
        from src.astadhyayi.it_agama import RUDADI_FIVE as EARLIER

        # 7.2.76 gave them an इट् before a वल्-initial
        # सार्वधातुक; 7.3.98 gives them an ईट् before a
        # single-sound one. One list asked for, not written twice.
        self.assertIs(RUDADI_FIVE, EARLIER)
        self.assertEqual(len(RUDADI_FIVE), 5)
        self.assertTrue(REGISTRY.has("7.2.76"))

    def test_they_take_an_it_before_a_single_sound_ending(self):
        # अरोदीत्, अस्वपीत्, प्राणीत्.
        for root in RUDADI_FIVE:
            got = before_sarvadhatuka(
                root, before="apṛkta-hal-sārvadhātuka")
            self.assertEqual(got.sutra, "7.3.98", root)
            self.assertEqual(got.does, "īṭ", root)

    def test_and_an_at_in_two_teachers_view(self):
        # अरोदत्, अस्वपत्, प्राणत्.
        got = before_sarvadhatuka("rud",
                                  before="apṛkta-sārvadhātuka",
                                  wants="aṭ")
        self.assertEqual(got.sutra, "7.3.99")
        self.assertEqual(got.view, GARGYA_GALAVA)
        self.assertTrue(got.optional)

    def test_naming_them_is_to_honour_and_not_to_dissent(self):
        # गार्ग्यगालवयोर्ग्रहणं पूजार्थम् — a different thing
        # from 7.1.74 and 7.2.63, where the naming makes the rule
        # an option in the language.
        self.assertIn("पूजार्थम्", PUJARTHAM)
        self.assertIn("पूजार्थम्", provisions_for("7.3.99")[0].why)
        for code in ("7.1.74", "7.2.63"):
            self.assertTrue(REGISTRY.has(code), code)

    def test_and_ad_takes_the_same_augment_in_every_view(self):
        # आदत्, आदः — the contrast with the sūtra before is the
        # whole content of this one.
        got = before_sarvadhatuka("ad",
                                  before="apṛkta-sārvadhātuka")
        self.assertEqual(got.sutra, "7.3.100")
        self.assertEqual(got.does, "aṭ")
        self.assertIn("sarveṣām", got.view)


class NothingHappensByDefault(unittest.TestCase):
    """7.3.84 stands where this run says nothing."""

    def test_an_unnamed_root_reaches_nothing(self):
        got = before_sarvadhatuka("pac", before="tiṅ")
        self.assertEqual(got.sutra, "")
        self.assertIn("7.3.84", got.why)


class Registration(unittest.TestCase):
    """Every row reaches the registry with real notes."""

    def test_the_run_is_contiguous(self):
        self.assertEqual(GUNA_RUN, ("7.3.85", "7.3.100"))
        codes = [row.sutra for row in GUNA_TABLE]
        self.assertEqual(
            codes, ["7.3.%d" % n for n in range(85, 101)])

    def test_every_sutra_is_registered_with_real_notes(self):
        for row in GUNA_TABLE:
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

    def test_the_guna_this_run_widens_is_live(self):
        # 7.3.84 सार्वधातुकार्धधातुकयोः, 1.1.2's definition of
        # guṇa, and 7.2.116's vṛddhi that 7.3.85 holds off.
        for code in ("7.3.84", "1.1.2", "7.2.116"):
            self.assertTrue(REGISTRY.has(code), code)

    def test_but_the_rule_that_proves_one_refusal_is_not(self):
        # 7.4.65 lays down बोभूतु without guṇa, and 7.3.88's
        # whole answer rests on it. No पाद of 7.4 is read; when
        # 7.4.65 lands this fails and the note must state the
        # live dependency.
        # 7.4.65 has landed, and बोभूतु is one of its eighteen
        # निपातन forms. 7.3.88's refusal can be checked against
        # the very form that proves it now.
        self.assertTrue(REGISTRY.has("7.4.65"))


if __name__ == "__main__":
    unittest.main()
