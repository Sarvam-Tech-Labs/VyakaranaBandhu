# -*- coding: utf-8 -*-
"""
७.२.३५–७८ — the इट् itself: given, lengthened, refused again.

7.2.35 is the rule the whole of 7.2.8–34 was stated before, so
the first class asserts that relation. Then the four sūtras that
place one long vowel, the block that names a root at a time, the
थल् restriction that names a teacher, and the three at the end
that reach a different affix class altogether.
"""

from __future__ import annotations

import unittest

from src.astadhyayi.it_agama import (
    BHARADVAJA,
    GAMA_FOUR,
    IT_RUN,
    IT_TABLE,
    KIRADI_FIVE,
    KRTADI_FIVE,
    NIGAMA_FOUR,
    RADHADI,
    RUDADI_FIVE,
    SANI_ELEVEN,
    SARVADHATUKA_FROM,
    THE_RULE,
    TISAHADI,
    VRDADI_FOUR,
    provisions_for,
    the_it,
)
from src.astadhyayi.sources import REGISTRY
import src.astadhyayi.rules  # noqa: F401  (populates REGISTRY)


class TheRuleTheRefusalsWereStatedBefore(unittest.TestCase):
    """7.2.35, and its relation to the pāda's earlier run."""

    def test_a_val_initial_ardhadhatuka_takes_the_it(self):
        # लविता, लवितुम्, लवितव्यम्.
        got = the_it(before="val-ādi-ārdhadhātuka")
        self.assertEqual(got.sutra, "7.2.35")
        self.assertEqual(got.does, "iṭ")

    def test_it_stands_after_every_rule_that_refuses_it(self):
        from src.astadhyayi.anit import ANIT_RUN, THE_RULE_ITSELF

        self.assertEqual(THE_RULE, "7.2.35")
        self.assertEqual(THE_RULE_ITSELF, THE_RULE)
        self.assertEqual(IT_RUN[0], THE_RULE)
        self.assertGreater(int(THE_RULE.rsplit(".", 1)[1]),
                           int(ANIT_RUN[1].rsplit(".", 1)[1]))

    def test_it_names_the_affix_class_rather_than_leaving_a_restriction(self):
        # रुदादिभ्यः सार्वधातुके इत्येतस्मिन् नियमार्थे
        # विज्ञायमाने प्रतिपत्तिगौरवं भवति — 7.2.76 could have
        # done the same work by restricting, and would have cost
        # the reader more.
        self.assertIn("प्रतिपत्तिगौरवं",
                      provisions_for("7.2.35")[0].why)

    def test_and_the_default_answer_defers_to_the_earlier_run(self):
        # Where no rule of THIS run is reached, whether the इट्
        # comes is 7.2.8–34's business and the module says so
        # rather than guessing.
        got = the_it("pac")
        self.assertEqual(got.sutra, "")
        self.assertIn("7.2.8-34", got.why)


class FourRulesToPlaceOneLongVowel(unittest.TestCase):
    """7.2.37–43 are about the ई of ग्रहीता, not about the इ."""

    def test_grah_lengthens_it_outside_the_perfect(self):
        # ग्रहीता, ग्रहीतुम्, ग्रहीतव्यम्.
        got = the_it("grah")
        self.assertEqual(got.sutra, "7.2.37")
        self.assertEqual(got.does, "dīrgha")

    def test_and_not_in_the_perfect(self):
        # जगृहिव, जगृहिम.
        self.assertNotEqual(the_it("grah", before="liṭ").sutra,
                            "7.2.37")

    def test_vr_and_the_long_r_final_roots_lengthen_it_optionally(self):
        # वरिता, वरीता; तरिता, तरीता.
        got = the_it("vṛ")
        self.assertEqual(got.sutra, "7.2.38")
        self.assertTrue(got.optional)

    def test_but_not_in_the_optative(self):
        # विवरिषीष्ट — the short इ only.
        got = the_it("vṛ", before="liṅ")
        self.assertEqual(got.sutra, "7.2.39")
        self.assertEqual(got.does, "")
        self.assertIn("7.2.38", got.blocked_by)

    def test_nor_before_a_parasmaipada_sic(self):
        # प्रावारिष्टाम्, अतारिष्टाम्.
        got = the_it("vṛ", before="sic", pada="parasmaipada")
        self.assertEqual(got.sutra, "7.2.40")

    def test_two_of_the_rules_here_are_about_the_augment_itself(self):
        # 7.2.39 refuses the LENGTH in the optative; 7.2.42 makes
        # the AUGMENT optional in the आत्मनेपद optative. Both
        # reach वृ + लिङ् + आत्मनेपद and neither blocks the other
        # — वरिषीष्ट has a short इ, वृषीष्ट has none — so the
        # query has to say which is wanted.
        length = the_it("vṛ", before="liṅ", pada="ātmanepada")
        augment = the_it("vṛ", before="liṅ", pada="ātmanepada",
                         wants="iṭ")
        self.assertEqual(length.sutra, "7.2.39")
        self.assertEqual(augment.sutra, "7.2.42")
        self.assertTrue(augment.optional)


class ARootAtATime(unittest.TestCase):
    """7.2.44–57, where the run turns into a list of roots."""

    def test_eight_roots_take_it_optionally(self):
        # रद्धा, रधिता; द्रोग्धा, द्रोहिता.
        self.assertEqual(len(RADHADI), 8)
        for root in RADHADI:
            got = the_it(root, before="val-ādi-ārdhadhātuka")
            self.assertEqual(got.sutra, "7.2.45", root)
            self.assertTrue(got.optional, root)

    def test_and_five_before_a_ta_initial_affix(self):
        # एष्टा, एषिता; सोढा, सहिता.
        self.assertEqual(len(TISAHADI), 5)
        for root in TISAHADI:
            self.assertEqual(
                the_it(root, before="ta-ādi-ārdhadhātuka").sutra,
                "7.2.48", root)

    def test_and_eleven_before_san(self):
        # दिदेविषति, बिभ्रज्जिषति, उच्छिश्रयिषति.
        self.assertEqual(len(SANI_ELEVEN), 10)
        for root in SANI_ELEVEN:
            self.assertEqual(the_it(root, before="san").sutra,
                             "7.2.49", root)

    def test_and_five_before_a_sa_initial_affix_that_is_not_sic(self):
        # कर्त्स्यति, कर्तिष्यति.
        self.assertEqual(len(KRTADI_FIVE), 5)
        for root in KRTADI_FIVE:
            got = the_it(root, before="sa-ādi-ārdhadhātuka")
            self.assertEqual(got.sutra, "7.2.57", root)
            self.assertTrue(got.optional, root)

    def test_a_sense_licenses_two_of_them(self):
        # अञ्चित्वा जानु जुहोति of honouring; विलुभिताः केशाः of
        # hair in disarray. Without the sense neither rule fires.
        self.assertEqual(
            the_it("añc", before="ktvā", sense="pūjā").sutra,
            "7.2.53")
        self.assertEqual(the_it("añc", before="ktvā").sutra, "")
        self.assertEqual(
            the_it("lubh", before="niṣṭhā",
                   sense="vimohana").sutra, "7.2.54")

    def test_a_preverb_licenses_two_more(self):
        # निष्कोष्टा, निष्कोषिता — and कोषिता without निर्.
        got = the_it("kuṣ", upasarga="nir",
                     before="val-ādi-ārdhadhātuka")
        self.assertEqual(got.sutra, "7.2.46")
        self.assertTrue(got.optional)
        self.assertEqual(
            the_it("kuṣ", before="val-ādi-ārdhadhātuka").sutra,
            "7.2.35")

    def test_and_the_nistha_makes_that_option_compulsory_again(self):
        # निष्कुषितः — इड्ग्रहणं नित्यार्थम्, and the sūtra
        # exists to beat 7.2.15.
        got = the_it("kuṣ", upasarga="nir", before="niṣṭhā")
        self.assertEqual(got.sutra, "7.2.47")
        self.assertFalse(got.optional)
        self.assertIn("7.2.15", got.blocked_by)


class GamAndWhatTakesItBack(unittest.TestCase):
    """7.2.58–60, a rule and two refusals."""

    def test_gam_takes_it_before_a_sa_initial_affix(self):
        # गमिष्यति, जिगमिषति.
        got = the_it("gam", before="sa-ādi-ārdhadhātuka",
                     pada="parasmaipada")
        self.assertEqual(got.sutra, "7.2.58")

    def test_four_roots_refuse_it_there(self):
        # वर्त्स्यति, शर्त्स्यति, स्यन्त्स्यति.
        self.assertEqual(len(VRDADI_FOUR), 4)
        for root in VRDADI_FOUR:
            got = the_it(root, before="sa-ādi-ārdhadhātuka",
                         pada="parasmaipada")
            self.assertEqual(got.sutra, "7.2.59", root)
            self.assertEqual(got.does, "", root)
            self.assertIn("7.2.58", got.blocked_by)

    def test_and_klp_refuses_it_before_tasi_as_well(self):
        # श्वः कल्प्ता.
        got = the_it("kḷp", before="tāsi", pada="parasmaipada")
        self.assertEqual(got.sutra, "7.2.60")
        self.assertEqual(got.does, "")

    def test_the_refusal_holds_only_inside_one_word(self):
        # आत्मनेपदेन समानपदस्थस्य — कल्पितासे and कल्पिष्यते keep
        # the इट्, and so does संजिगमिषिता.
        self.assertNotEqual(
            the_it("kḷp", before="tāsi",
                   pada="ātmanepada").sutra, "7.2.60")
        self.assertIn("समानपदस्थस्य",
                      provisions_for("7.2.58")[0].why)


class TheThalRestriction(unittest.TestCase):
    """7.2.61–66, and the teacher 7.2.63 names."""

    def test_a_vowel_final_anit_root_refuses_it_in_the_thal(self):
        # ययाथ, चिचेथ, जुहोथ.
        got = the_it(gana="ac-anta-tāsi-anit", before="thal")
        self.assertEqual(got.sutra, "7.2.61")
        self.assertEqual(got.does, "")

    def test_and_so_does_one_with_an_a_in_the_upadesa(self):
        # पपक्थ, इयष्ठ, शशक्थ.
        got = the_it(gana="a-vat-upadeśa-tāsi-anit", before="thal")
        self.assertEqual(got.sutra, "7.2.62")

    def test_bharadvaja_restricts_both_of_them_to_r_final_roots(self):
        # सस्मर्थ, दध्वर्थ — and ययिथ, पेचिथ, शेकिथ everywhere
        # else, the restriction turning the two rules before into
        # options.
        got = the_it(gana="ṛ-anta", before="thal")
        self.assertEqual(got.sutra, "7.2.63")
        self.assertEqual(set(got.blocked_by), {"7.2.61", "7.2.62"})

    def test_naming_the_teacher_is_how_the_view_is_recorded(self):
        self.assertIn("bhāradvāja", BHARADVAJA)
        self.assertIn("भारद्वाजस्य", provisions_for("7.2.63")[0].why)
        self.assertIn("नियमार्थः", provisions_for("7.2.63")[0].why)

    def test_four_vedic_perfects_are_laid_down_whole(self):
        # बभूथ, आततन्थ, जगृभ्म, ववर्थ.
        self.assertEqual(len(NIGAMA_FOUR), 4)
        for word in NIGAMA_FOUR:
            got = the_it(word, chandasi=True)
            self.assertEqual(got.sutra, "7.2.64", word)
            self.assertTrue(got.nipatana, word)
            self.assertEqual(the_it(word).sutra, "", word)

    def test_and_three_roots_take_it_in_the_thal_after_all(self):
        # आदिथ, आरिथ, विव्ययिथ.
        for root in ("ad", "ṛ", "vye"):
            got = the_it(root, before="thal")
            self.assertEqual(got.sutra, "7.2.66", root)
            self.assertIn("7.2.63", got.blocked_by)


class BeforeVasu(unittest.TestCase):
    """7.2.67–69, and how one syllable is counted."""

    def test_the_it_comes_for_three_kinds_of_root(self):
        # पेचिवान्, ययिवान्, जक्षिवान्.
        got = the_it(gana="eka-ac-ā-anta-ghas", before="vasu")
        self.assertEqual(got.sutra, "7.2.67")

    def test_one_syllable_is_counted_after_the_reduplication(self):
        # धात्वभ्यासयोरेकादेशे कृते... कृतद्विर्वचना एत एकाचो
        # भवन्ति — पच् is two syllables until the perfect makes
        # it पेच्.
        self.assertIn("कृतद्विर्वचना",
                      provisions_for("7.2.67")[0].why)

    def test_four_roots_take_it_optionally_there(self):
        # जग्मिवान्, जगन्वान्.
        self.assertEqual(GAMA_FOUR, ("gam", "han", "vid", "viś"))
        for root in GAMA_FOUR:
            got = the_it(root, before="vasu")
            self.assertEqual(got.sutra, "7.2.68", root)
            self.assertTrue(got.optional, root)


class TheLastAffixClass(unittest.TestCase):
    """7.2.76–78 reach a सार्वधातुक, which 7.2.35 shut out."""

    def test_the_turn_is_at_the_sutra_the_module_names(self):
        self.assertEqual(SARVADHATUKA_FROM, "7.2.76")

    def test_five_roots_take_it_before_a_sarvadhatuka(self):
        # रोदिति, स्वपिति, श्वसिति, प्राणिति, जक्षिति.
        self.assertEqual(len(RUDADI_FIVE), 5)
        for root in RUDADI_FIVE:
            self.assertEqual(
                the_it(root, before="val-ādi-sārvadhātuka").sutra,
                "7.2.76", root)

    def test_and_two_more_before_particular_endings(self):
        # ईशिषे; ईडिध्वे, जनिषे.
        self.assertEqual(the_it("īś", before="se").sutra, "7.2.77")
        for root in ("īḍ", "jan"):
            for ending in ("dhve", "se"):
                self.assertEqual(
                    the_it(root, before=ending).sutra, "7.2.78",
                    (root, ending))

    def test_the_variant_reading_is_recorded_and_not_settled(self):
        # केचिद् ईडिजनोः स्ध्वे च इति सूत्रं पठन्ति — a different
        # text of the sūtra, which would catch ईशिध्वे too.
        self.assertIn("केचिद्", provisions_for("7.2.78")[0].why)


class KiradiAndTheFiveBeforeSan(unittest.TestCase):
    """7.2.74–75, where an earlier option is made compulsory."""

    def test_five_roots_take_it_before_san(self):
        # चिकरिषति, जिगरिषति, पिपृच्छिषति.
        self.assertEqual(len(KIRADI_FIVE), 5)
        for root in KIRADI_FIVE:
            got = the_it(root, before="san")
            self.assertEqual(got.sutra, "7.2.75", root)
            self.assertFalse(got.optional, root)

    def test_and_that_beats_the_option_two_of_them_would_have_had(self):
        # 7.2.41's इट् सनि वा reached कॄ and गॄ; here it is
        # compulsory, and the lengthening is not wanted either.
        self.assertIn("7.2.41",
                      provisions_for("7.2.75")[0].blocks)
        self.assertIn("नेच्छन्ति", provisions_for("7.2.75")[0].why)


class Registration(unittest.TestCase):
    """Every row reaches the registry with real notes."""

    def test_the_run_is_contiguous(self):
        self.assertEqual(IT_RUN, ("7.2.35", "7.2.78"))
        codes = [row.sutra for row in IT_TABLE]
        self.assertEqual(
            codes, ["7.2.%d" % n for n in range(35, 79)])

    def test_every_sutra_is_registered_with_real_notes(self):
        for row in IT_TABLE:
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

    def test_the_affix_names_this_run_turns_on_are_live(self):
        # 3.4.114 आर्धधातुकं शेषः and 3.4.113 तिङ्शित्
        # सार्वधातुकम् name the two affix classes 7.2.35 and
        # 7.2.76 divide between them, and 1.1.26 names the
        # निष्ठा. All three are codified.
        for code in ("3.4.113", "3.4.114", "1.1.26"):
            self.assertTrue(REGISTRY.has(code), code)

    def test_and_half_of_what_the_augment_meets_has_landed(self):
        # सोढा needs 8.2.31 हो ढः, which has landed with
        # पाद ८.२, and निष्कोष्टा needs the cerebral of पाद ८.३,
        # which has not. 8.2.19 is not that rule — it is the
        # र्-to-ल् of a preverb before अय् — and the first draft
        # of this note named it by mistake.
        # 8.3.41 इदुदुपधस्य चाप्रत्ययस्य, which gives निर् its
        # ष् in निष्कोष्टा, has landed too.
        self.assertTrue(REGISTRY.has("8.2.31"))
        self.assertTrue(REGISTRY.has("8.3.41"))


if __name__ == "__main__":
    unittest.main()
