# -*- coding: utf-8 -*-
"""
७.१.८४–१०३ — the strong cases, and the ॠ that closes the pāda.

The tests are built round the four rules that decline पथिन्
between them, the रूपातिदेश at 7.1.95, and the ॠ rules that end
the pāda on something else entirely.
"""

from __future__ import annotations

import unittest

from src.astadhyayi.sarvanamasthana import (
    CATUR_ANADUH,
    KROSTU,
    PATHI_THREE,
    RTA_FROM,
    STRONG_RUN,
    STRONG_TABLE,
    USANAS_THREE,
    USANAS_VOCATIVE,
    provisions_for,
    strong_stem,
)
from src.astadhyayi.sources import REGISTRY
import src.astadhyayi.rules  # noqa: F401  (populates REGISTRY)


class FourRulesForOneWord(unittest.TestCase):
    """7.1.85–88, which decline पथिन् between them."""

    def test_the_three_stems_take_a_before_su(self):
        # पन्थाः, मन्थाः, ऋभुक्षाः.
        self.assertEqual(len(PATHI_THREE), 3)
        for stem in PATHI_THREE:
            got = strong_stem(stem, before="su")
            self.assertEqual(got.sutra, "7.1.85", stem)
            self.assertEqual(got.does, "āt", stem)

    def test_their_i_becomes_a_in_every_strong_case(self):
        # पन्थानौ, पन्थानः, ऋभुक्षाणम्.
        got = strong_stem("pathin", part="i",
                          before="sarvanāmasthāna")
        self.assertEqual(got.sutra, "7.1.86")
        self.assertEqual(got.does, "at")

    def test_and_two_of_them_turn_their_th_into_nth(self):
        # पन्थाः, मन्थाः — and ऋभुक्षिन् has no थ् to turn.
        got = strong_stem("pathin", part="th",
                          before="sarvanāmasthāna")
        self.assertEqual(got.sutra, "7.1.87")
        self.assertNotIn("ṛbhukṣin", provisions_for("7.1.87")[0].of)

    def test_but_a_bha_stem_loses_its_ti_instead(self):
        # पथः, पथा, ऋभुक्षे.
        got = strong_stem("pathin", part="ṭi", result="bha")
        self.assertEqual(got.sutra, "7.1.88")
        self.assertEqual(got.does, "ṭi-lopa")
        self.assertIn("7.1.86", got.blocked_by)

    def test_the_anuvrtti_is_dropped_for_contradiction(self):
        # सर्वनामस्थानमनुवर्तमानमपि विरोधादिह न सम्बध्यते — a stem
        # cannot be भ and strong at once, so the word running
        # down from 7.1.86 simply does not connect here.
        row = provisions_for("7.1.88")[0]
        self.assertEqual(row.before, ())
        self.assertIn("विरोधाद्", row.why)


class TheStemsWithARuleEach(unittest.TestCase):
    """7.1.84, 7.1.89–94."""

    def test_div_becomes_dyau(self):
        # द्यौः — and the दिव् meant is the noun, not the root.
        got = strong_stem("div", before="su")
        self.assertEqual(got.sutra, "7.1.84")
        self.assertEqual(got.does, "aut")

    def test_pums_becomes_pumams(self):
        # पुमान्, पुमांसौ, पुमांसः.
        got = strong_stem("puṃs", before="sarvanāmasthāna")
        self.assertEqual(got.sutra, "7.1.89")
        self.assertEqual(got.does, "asuṅ")

    def test_go_makes_its_ending_nit(self):
        # गौः, गावौ, गावः — a property conferred, not a shape.
        got = strong_stem("go", before="sarvanāmasthāna")
        self.assertEqual(got.sutra, "7.1.90")
        self.assertEqual(got.does, "ṇit")

    def test_sakhi_gets_two_rules_and_both_spare_the_vocative(self):
        # सखायौ by 7.1.92, सखा by 7.1.93, and हे सखे by neither.
        self.assertEqual(
            strong_stem("sakhi", before="sarvanāmasthāna").sutra,
            "7.1.92")
        self.assertEqual(
            strong_stem("sakhi", before="su").sutra, "7.1.93")
        self.assertEqual(
            strong_stem("sakhi", before="sambuddhi").sutra, "")

    def test_an_r_final_stem_takes_anan_before_su(self):
        # कर्ता, माता, पिता, भ्राता.
        got = strong_stem(gana="ṛ-anta", before="su")
        self.assertEqual(got.sutra, "7.1.94")
        self.assertEqual(got.does, "anaṅ")

    def test_three_more_stems_are_named_beside_them(self):
        # उशना, पुरुदंसा, अनेहा.
        self.assertEqual(len(USANAS_THREE), 3)
        for stem in USANAS_THREE:
            self.assertEqual(strong_stem(stem, before="su").sutra,
                             "7.1.94", stem)

    def test_usanas_has_three_vocatives_and_the_vrtti_picks_none(self):
        # संबोधने तूशनसस्त्रिरूपं सान्तं तथा नान्तमथाप्यदन्तम् —
        # हे उशनः, हे उशनन्, हे उशन, all three standing, and a
        # fourth teacher wanting guṇa besides.
        self.assertEqual(len(USANAS_VOCATIVE), 3)
        self.assertIn("त्रिरूपं", provisions_for("7.1.94")[0].why)


class TheShapeConferred(unittest.TestCase):
    """7.1.95–97, a रूपातिदेश and not a substitution."""

    def test_krostu_takes_a_trc_stems_shape(self):
        # क्रोष्टा, क्रोष्टारौ, क्रोष्टारम्.
        got = strong_stem(KROSTU, before="sarvanāmasthāna")
        self.assertEqual(got.sutra, "7.1.95")
        self.assertEqual(got.does, "tṛjvat")

    def test_which_trc_stem_is_a_question_the_vrtti_answers(self):
        # प्रत्यासत्तेश्च क्रुशेरेव तृजन्तस्य यद् रूपम् — the
        # nearest one, and its accent comes with the shape.
        why = provisions_for("7.1.95")[0].why
        self.assertIn("रूपातिदेशोऽयम्", why)
        self.assertIn("प्रत्यासत्ते", why)

    def test_the_feminine_is_a_separate_sutra_for_the_weak_cases(self):
        # क्रोष्ट्री, क्रोष्ट्रीभिः — असर्वनामस्थानार्थमारम्भः.
        got = strong_stem(KROSTU, result="strī")
        self.assertEqual(got.sutra, "7.1.96")

    def test_and_in_the_oblique_cases_it_is_optional(self):
        # क्रोष्ट्रा beside क्रोष्टुना.
        got = strong_stem(KROSTU, before="tṛtīyā-ādi-ac")
        self.assertEqual(got.sutra, "7.1.97")
        self.assertTrue(got.optional)

    def test_the_strong_case_rule_is_not_optional(self):
        self.assertFalse(
            strong_stem(KROSTU, before="sarvanāmasthāna").optional)


class TheAugmentAndItsException(unittest.TestCase):
    """7.1.98 against 7.1.99."""

    def test_catur_and_anaduh_take_an_udatta_am(self):
        # चत्वारः, अनड्वान्, अनड्वाहौ.
        self.assertEqual(CATUR_ANADUH, ("catur", "anaḍuh"))
        for stem in CATUR_ANADUH:
            got = strong_stem(stem, before="sarvanāmasthāna")
            self.assertEqual(got.sutra, "7.1.98", stem)
            self.assertTrue(got.augment, stem)
            self.assertTrue(got.udatta, stem)

    def test_but_the_vocative_takes_am_instead(self):
        # हे प्रियचत्वः, हे प्रियानड्वन्.
        got = strong_stem("catur", before="sambuddhi")
        self.assertEqual(got.sutra, "7.1.99")
        self.assertEqual(got.does, "am")
        self.assertIn("7.1.98", got.blocked_by)


class ThePadaEndsOnSomethingElse(unittest.TestCase):
    """7.1.100–103, the ॠ of a root."""

    def test_the_turn_is_at_the_sutra_the_module_names(self):
        self.assertEqual(RTA_FROM, "7.1.100")

    def test_nothing_after_the_turn_wants_a_strong_ending(self):
        # Compared as numbers, not as strings: "7.1.86" sorts
        # after "7.1.100" lexically, and the first draft of this
        # test passed the wrong rows through because of it.
        def number(code):
            return int(code.rsplit(".", 1)[1])

        for row in STRONG_TABLE:
            if number(row.sutra) >= number(RTA_FROM):
                self.assertNotIn("sarvanāmasthāna", row.before,
                                 row.sutra)

    def test_a_final_long_r_becomes_i(self):
        # किरति, गिरति, आस्तीर्णम्.
        got = strong_stem(gana="ṝ-anta-dhātu", part="ṝ")
        self.assertEqual(got.sutra, "7.1.100")
        self.assertEqual(got.does, "it")

    def test_and_so_does_one_in_the_penult(self):
        # कीर्तयति.
        self.assertEqual(
            strong_stem(gana="ṝ-upadha-dhātu",
                        part="ṝ-upadhā").sutra, "7.1.101")

    def test_but_a_labial_before_it_gives_u_instead(self):
        # पूर्ताः, पुपूर्षति, मुमूर्षति.
        got = strong_stem(gana="oṣṭhya-pūrva-ṝ-anta", part="ṝ")
        self.assertEqual(got.sutra, "7.1.102")
        self.assertEqual(got.does, "ut")
        self.assertIn("7.1.100", got.blocked_by)

    def test_the_veda_takes_the_u_bahulam(self):
        # ततुरिम् and जगुरिः with no labial, पप्रितमम् with one
        # and no उ — both directions in one sūtra.
        got = strong_stem(gana="ṝ-anta-dhātu", chandasi=True)
        self.assertEqual(got.sutra, "7.1.103")
        self.assertTrue(provisions_for("7.1.103")[0].bahulam)

    def test_only_roots_are_reached_and_not_nouns(self):
        # पितृणाम्, मातृणाम् — the word धातोः shuts them out, and
        # लाक्षणिकस्यापि ग्रहणम् lets चिकीर्षति in.
        for row in provisions_for("7.1.100"):
            self.assertIn("dhātu", row.gana)
        self.assertIn("लाक्षणिकस्य",
                      provisions_for("7.1.100")[0].why)


class NothingHappensByDefault(unittest.TestCase):
    """Most stems go into the strong cases unchanged."""

    def test_an_unnamed_stem_reaches_nothing(self):
        got = strong_stem("vṛkṣa", before="sarvanāmasthāna")
        self.assertEqual(got.sutra, "")
        self.assertEqual(got.does, "")


class Registration(unittest.TestCase):
    """Every row reaches the registry, and the pāda is closed."""

    def test_the_run_is_contiguous(self):
        self.assertEqual(STRONG_RUN, ("7.1.84", "7.1.103"))
        codes = [row.sutra for row in STRONG_TABLE]
        self.assertEqual(
            codes, ["7.1.%d" % n for n in range(84, 104)])

    def test_every_sutra_is_registered_with_real_notes(self):
        for row in STRONG_TABLE:
            self.assertTrue(REGISTRY.has(row.sutra), row.sutra)
            notes = REGISTRY.get(row.sutra).notes
            self.assertGreater(len(notes), 100, row.sutra)
            self.assertIn("SETTLED", notes, row.sutra)

    def test_pada_seven_one_is_complete(self):
        # 103 sūtras, and 7.1.3 was codified long before the rest
        # of the pāda was read through.
        for n in range(1, 104):
            self.assertTrue(REGISTRY.has("7.1.%d" % n), n)
        self.assertFalse(REGISTRY.has("7.1.104"))


class WhatIsNotCodifiedYet(unittest.TestCase):
    """
    The debts, written as the exact shortfall.

    Each fails the moment the thing it names lands, and must then
    be rewritten to state the live dependency instead.
    """

    def test_the_names_and_the_lengthening_are_live(self):
        # 1.1.43 सुडनपुंसकस्य names the strong endings and
        # 6.4.9's वा षपूर्वस्य निगमे is what 7.1.86's second अत्
        # was written for. Both are codified. 8.2.8's न-loss,
        # which उशनस् argues about, is not — when it lands this
        # assertion fails and the note must state the live edge.
        # 8.2.8's refusal of the न-loss, which उशनस् argues
        # about, has landed with पाद ८.२ too.
        for code in ("1.1.43", "6.4.9", "8.2.8"):
            self.assertTrue(REGISTRY.has(code), code)

    def test_what_pada_seven_two_supplies_is_live_now(self):
        # 7.2.84's अष्टन आ and 7.2.115's अचो ञ्णिति are both
        # appealed to by this pāda, and both landed with पाद ७.२.
        # So 7.1.21's अष्टौ can be asked against the rule that
        # gives अष्टन् its आ, and 7.1.90's णित् against the rule
        # that says what a णित् does. पाद ७.३ has been opened
        # since; 7.4.1, where the last pāda begins, has not.
        self.assertTrue(REGISTRY.has("7.2.84"))
        self.assertTrue(REGISTRY.has("7.2.115"))
        # 7.4.1 has landed with the last pāda of the adhyāya.
        self.assertTrue(REGISTRY.has("7.4.1"))


if __name__ == "__main__":
    unittest.main()
