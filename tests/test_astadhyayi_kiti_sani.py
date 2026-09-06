# -*- coding: utf-8 -*-
"""
७.४.४१–५७ — दा becomes दद्, तास् and अस् lose their स्, and सन्.

Three groups again, and two of the seventeen are worth the whole
run: 7.4.46, whose substitute's last sound is argued for in a
verse against three rejected candidates, and 7.4.50, which leaves
a word that is all affix and nothing else.
"""

from __future__ import annotations

import unittest

from src.astadhyayi.kiti_sani import (
    AP_JNAP_RDH,
    KITI_RUN,
    KITI_TABLE,
    MI_MA_EIGHT,
    SANI_FROM,
    SUDHITADI,
    THANTAM,
    before_kit,
    provisions_for,
)
from src.astadhyayi.sources import REGISTRY
import src.astadhyayi.rules  # noqa: F401  (populates REGISTRY)


class TheKitBlock(unittest.TestCase):
    """7.4.41–47."""

    def test_two_roots_take_an_i_optionally(self):
        # निशितम् beside निशातम्; अवच्छितम् beside अवच्छातम्.
        for root in ("śā", "chā"):
            got = before_kit(root, before="ta-ādi-kit")
            self.assertEqual(got.sutra, "7.4.41", root)
            self.assertTrue(got.optional, root)

    def test_and_a_varttika_makes_it_compulsory_of_a_vow(self):
        # श्यतेरित्त्वं व्रते नित्यम् — संशितव्रतः. And a verse
        # settles that the two options do not combine.
        why = provisions_for("7.4.41")[0].why
        self.assertIn("व्रते नित्यम्", why)
        self.assertIn("मिथस्ते न विभाष्यन्ते", why)

    def test_dha_becomes_hi_and_ha_too_before_ktva(self):
        # हितः, हित्वा; हित्वा राज्यं वनं गतः.
        self.assertEqual(
            before_kit("dhā", before="ta-ādi-kit").sutra, "7.4.42")
        self.assertEqual(
            before_kit("hā", before="ktvā").sutra, "7.4.43")

    def test_the_ha_meant_is_named_by_its_own_form(self):
        # जहातेर्निदेशाज् जिहीतेर्न भवति — हात्वा is the other.
        self.assertIn("जिहीतेर् न भवति",
                      provisions_for("7.4.43")[0].why)

    def test_and_the_veda_makes_that_optional(self):
        # हित्वा शरीरं यातव्यम्; हात्वा.
        got = before_kit("hā", before="ktvā", chandasi=True)
        self.assertEqual(got.sutra, "7.4.44")
        self.assertTrue(got.optional)
        self.assertIn("7.4.43", got.blocked_by)

    def test_five_vedic_forms_are_laid_down(self):
        # सुधितम्, वसुधितम्, नेमधिता, धिष्व, धिषीय.
        self.assertEqual(len(SUDHITADI), 5)
        for word in SUDHITADI:
            got = before_kit(word, chandasi=True)
            self.assertEqual(got.sutra, "7.4.45", word)
            self.assertTrue(got.nipatana, word)


class TheVerseAboutOneSound(unittest.TestCase):
    """7.4.46, and the three candidates it rejects."""

    def test_da_becomes_dad_before_a_ta_initial_kit(self):
        # दत्तः, दत्तवान्, दत्तिः.
        got = before_kit("dā", gana="ghu", before="ta-ādi-kit")
        self.assertEqual(got.sutra, "7.4.46")
        self.assertEqual(got.does, "dad")

    def test_the_verse_weighs_four_candidates_and_keeps_one(self):
        # तान्ते दोषो दीर्घत्वं स्यात्; दान्ते निष्ठानत्वम्;
        # धान्ते धत्वप्राप्तिः; थान्तेऽदोषः — chosen for
        # producing no wrong form at all.
        for fault in ("दीर्घत्वं", "निष्ठानत्वम्",
                      "धत्वप्राप्तिस्"):
            self.assertIn(fault, THANTAM, fault)
        self.assertIn("तस्मात् थान्तम्", THANTAM)

    def test_but_after_a_vowel_final_preverb_it_is_plain_t(self):
        # प्रत्तम्, अवत्तम्, नीत्तम्, परीत्तम्.
        got = before_kit("dā", gana="ghu",
                         upasarga="ac-anta-upasarga",
                         before="ta-ādi-kit")
        self.assertEqual(got.sutra, "7.4.47")
        self.assertEqual(got.does, "ta")
        self.assertIn("7.4.46", got.blocked_by)

    def test_and_the_case_of_the_sutra_is_read_twice_over(self):
        # अचः इत्येतद् द्विरावर्तयितव्यम् — once for the preverb
        # and once for what is replaced.
        self.assertIn("द्विरावर्तयितव्यम्",
                      provisions_for("7.4.47")[0].why)


class TheLossesOfS(unittest.TestCase):
    """7.4.48–53."""

    def test_ap_becomes_at_before_a_bh(self):
        # अद्भिः, अद्भ्यः; अप्सु otherwise.
        self.assertEqual(
            before_kit("ap", before="bha-ādi").sutra, "7.4.48")

    def test_an_s_final_stem_becomes_t_final(self):
        # वत्स्यति, विवत्सति, जिघत्सति.
        got = before_kit(gana="s-anta",
                         before="sa-ādi-ārdhadhātuka")
        self.assertEqual(got.sutra, "7.4.49")
        self.assertEqual(got.does, "ta")

    def test_tas_and_as_lose_their_s_three_ways(self):
        # कर्तासि, कर्तारौ, कर्ताहे.
        wanted = {"sa-ādi": ("7.4.50", "lopa"),
                  "ra-ādi": ("7.4.51", "lopa"),
                  "e": ("7.4.52", "ha")}
        for affix, (code, does) in wanted.items():
            for root in ("tās", "as"):
                got = before_kit(root, before=affix)
                self.assertEqual(got.sutra, code, (root, affix))
                self.assertEqual(got.does, does, (root, affix))

    def test_and_one_of_those_leaves_a_word_that_is_all_affix(self):
        # व्यतिसे — से इति प्रत्ययमात्रम् एतत् पदम्, which is why
        # 8.3.111's ष् does not come.
        why = provisions_for("7.4.50")[0].why
        self.assertIn("प्रत्ययमात्रम्", why)
        self.assertIn("8.3.111", why)

    def test_two_roots_lose_their_vowel_before_ya_and_i(self):
        # आदीध्य गतः, आदीधिता; आवेव्यते, आवेविता.
        for root in ("dīdhī", "vevī"):
            for affix in ("ya-ādi", "i-varṇa-ādi"):
                self.assertEqual(
                    before_kit(root, before=affix).sutra,
                    "7.4.53", (root, affix))


class BeforeSan(unittest.TestCase):
    """7.4.54–57, where the run ends."""

    def test_the_turn_is_at_the_sutra_the_module_names(self):
        self.assertEqual(SANI_FROM, "7.4.54")

    def test_eight_stems_take_an_is(self):
        # मित्सति, दित्सति, धित्सति, आरिप्सते, शिक्षति.
        self.assertEqual(len(MI_MA_EIGHT), 8)
        for root in MI_MA_EIGHT:
            got = before_kit(root, before="sa-ādi-san")
            self.assertEqual(got.sutra, "7.4.54", root)
            self.assertEqual(got.does, "is", root)

    def test_three_take_an_i_instead(self):
        # आपीप्सति, ज्ञीप्सति, ईर्त्सति.
        self.assertEqual(len(AP_JNAP_RDH), 3)
        for root in AP_JNAP_RDH:
            got = before_kit(root, before="sa-ādi-san")
            self.assertEqual(got.sutra, "7.4.55", root)
            self.assertEqual(got.does, "īt", root)
            self.assertIn("7.4.54", got.blocked_by, root)

    def test_and_dambh_takes_both_lengths(self):
        # धिप्सति, धीप्सति — the च carrying the ई down.
        got = before_kit("dambh", before="sa-ādi-san")
        self.assertEqual(got.sutra, "7.4.56")
        self.assertTrue(got.optional)

    def test_muc_takes_guna_only_without_an_object(self):
        # मोक्षते वत्सः स्वयमेव; मुमुक्षति वत्सं देवदत्तः.
        got = before_kit("muc", before="sa-ādi-san",
                         result="akarmaka")
        self.assertEqual(got.sutra, "7.4.57")
        self.assertEqual(got.does, "guṇa")
        self.assertTrue(got.optional)
        self.assertNotEqual(
            before_kit("muc", before="sa-ādi-san").sutra, "7.4.57")

    def test_and_what_is_really_optional_is_a_refusal(self):
        # हलन्ताच् च इति कित्त्वप्रतिषेधो विकल्प्यते — the guṇa
        # follows from that, and 1.2.10 is codified.
        self.assertIn("कित्त्वप्रतिषेधो",
                      provisions_for("7.4.57")[0].why)
        self.assertTrue(REGISTRY.has("1.2.10"))


class NothingHappensByDefault(unittest.TestCase):
    """A root none of the seventeen names is untouched."""

    def test_an_unnamed_root_reaches_nothing(self):
        got = before_kit("pac", before="ta-ādi-kit")
        self.assertEqual(got.sutra, "")
        self.assertEqual(got.does, "")


class Registration(unittest.TestCase):
    """Every row reaches the registry with real notes."""

    def test_the_run_is_contiguous(self):
        self.assertEqual(KITI_RUN, ("7.4.41", "7.4.57"))
        codes = [row.sutra for row in KITI_TABLE]
        self.assertEqual(
            codes, ["7.4.%d" % n for n in range(41, 58)])

    def test_every_sutra_is_registered_with_real_notes(self):
        for row in KITI_TABLE:
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
        # 3.1.7's सन्, 3.4.21's क्त्वा and 3.2.102's निष्ठा are
        # the three this run names, and 1.2.10 is the refusal
        # 7.4.57 makes optional. All codified.
        for code in ("3.1.7", "3.4.21", "3.2.102", "1.2.10"):
            self.assertTrue(REGISTRY.has(code), code)

    def test_and_the_last_heading_of_the_adhyaya_has_landed(self):
        # 7.4.58 अत्र लोपोऽभ्यासस्य opens अभ्यासस्य by dropping
        # the copy in exactly the environment 7.4.54-57 named —
        # this run's own — so the two files meet at that sūtra,
        # and 7.4.97 closes the adhyāya.
        self.assertTrue(REGISTRY.has("7.4.58"))
        self.assertTrue(REGISTRY.has("7.4.97"))


if __name__ == "__main__":
    unittest.main()
