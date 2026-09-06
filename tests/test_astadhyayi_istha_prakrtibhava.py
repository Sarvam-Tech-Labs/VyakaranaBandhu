# -*- coding: utf-8 -*-
"""
६.४.१५४–१७५ — इष्ठ, इमन्, ईयस्, and the stems that stand unchanged.

The run has two halves that pull opposite ways, and the tests are
written to catch the turn: 154–162 take things away, 163–173 say
that they do not happen, 174–175 lay words down whole.

And this is the end of अध्याय ६, so the last class checks that the
adhyāya closes with nothing left over.
"""

from __future__ import annotations

import unittest

from src.astadhyayi.istha_prakrtibhava import (
    GATHIN_FIVE,
    ISTHA_RUN,
    ISTHA_TABLE,
    ISTHA_THREE,
    NIPATANA_ELEVEN,
    NIPATANA_VEDIC,
    PRAKRTI_FROM,
    STHULADI,
    YATHASAMKHYAM_TEN,
    before_istha,
    provisions_for,
)
from src.astadhyayi.sources import REGISTRY
import src.astadhyayi.rules  # noqa: F401  (populates REGISTRY)


class TheThreeAffixes(unittest.TestCase):
    """What the whole first half is stated before."""

    def test_the_three_are_istha_iman_and_iyas(self):
        self.assertEqual(ISTHA_THREE,
                         ("iṣṭhan", "imanic", "īyasun"))

    def test_the_run_closes_the_adhyaya(self):
        self.assertEqual(ISTHA_RUN, ("6.4.154", "6.4.175"))
        self.assertFalse(REGISTRY.has("6.4.176"))


class WhatTheStemLoses(unittest.TestCase):
    """6.4.154–162, the half that takes things away."""

    def test_tr_is_lost_whole_before_all_three(self):
        # करिष्ठः, विजयिष्ठः, वहिष्ठः, दोहीयसी धेनुः.
        for affix in ISTHA_THREE:
            got = before_istha("tṛ", before=affix)
            self.assertEqual(got.sutra, "6.4.154", affix)
            self.assertEqual(got.does, "lopa", affix)

    def test_the_ti_loss_is_the_general_case(self):
        # पटिष्ठः, लघिमा — no stem named, only the part taken.
        got = before_istha(part="ṭi", before="iṣṭhan")
        self.assertEqual(got.sutra, "6.4.155")

    def test_the_whole_tr_goes_and_not_just_its_ti(self):
        # सर्वस्य तृशब्दस्य लोपार्थं वचनम् — 6.4.154 exists only
        # because 6.4.155 would have taken the smaller piece, so
        # the two must not resolve to the same thing.
        self.assertNotEqual(provisions_for("6.4.154")[0].does,
                            provisions_for("6.4.155")[0].does)
        self.assertEqual(provisions_for("6.4.154")[0].part, "")

    def test_six_stems_lose_a_semivowel_onward_and_take_guna(self):
        # स्थविष्ठः, दवीयान्, यविष्ठः, ह्रसिमा, क्षेपिष्ठः.
        self.assertEqual(len(STHULADI), 6)
        for stem in STHULADI:
            got = before_istha(stem, part="yaṇ-ādi-para",
                               before="iṣṭhan")
            self.assertEqual(got.sutra, "6.4.156", stem)
            self.assertEqual(got.does, "guṇa", stem)


class TheTenPairs(unittest.TestCase):
    """6.4.157, the longest यथासंख्यम् of the pāda."""

    def test_each_stem_gets_its_own_substitute(self):
        # प्रेष्ठः, स्थेष्ठः, गरिष्ठः — one to one, in order.
        self.assertEqual(len(YATHASAMKHYAM_TEN), 10)
        for stem, shape in YATHASAMKHYAM_TEN:
            got = before_istha(stem, before="iṣṭhan")
            self.assertEqual(got.sutra, "6.4.157", stem)
            self.assertEqual(got.does, shape, stem)

    def test_a_crossed_pairing_reaches_nothing(self):
        # प्रिय gives प्र and not स्थ; asking for the wrong
        # substitute must not fall back on the same rule.
        got = before_istha("priya", before="iṣṭhan", wants="stha")
        self.assertNotEqual(got.sutra, "6.4.157")
        self.assertEqual(got.sutra, "")

    def test_the_substitutes_are_all_distinct(self):
        shapes = [shape for _, shape in YATHASAMKHYAM_TEN]
        self.assertEqual(len(set(shapes)), len(shapes))


class Bahu(unittest.TestCase):
    """6.4.158 against 6.4.159, and 6.4.160 after them."""

    def test_the_affix_itself_goes_and_bahu_becomes_bhu(self):
        # भूमा, भूयान्.
        for affix in ("imanic", "īyasun"):
            got = before_istha("bahu", before=affix)
            self.assertEqual(got.sutra, "6.4.158", affix)
            self.assertEqual(got.does, "bhū", affix)

    def test_but_istha_keeps_itself_with_an_augment(self):
        # भूयिष्ठः — लोपापवादो यिडागमः.
        got = before_istha("bahu", before="iṣṭhan")
        self.assertEqual(got.sutra, "6.4.159")
        self.assertEqual(got.does, "yiṭ")
        self.assertIn("6.4.158", got.blocked_by)

    def test_jya_takes_a_substitute_because_the_yit_stands_between(self):
        # ज्यायान् — लोपस्य यिटा व्यवहितत्वाद् आद् इत्युच्यते.
        got = before_istha("jya", before="īyasun")
        self.assertEqual(got.sutra, "6.4.160")
        self.assertEqual(got.does, "āt")


class TheLightR(unittest.TestCase):
    """6.4.161's three conditions, and 6.4.162's Vedic option."""

    def test_a_light_r_after_a_consonant_becomes_ra(self):
        # प्रथिष्ठः, म्रदिमा.
        got = before_istha(part="ṛ", before="iṣṭhan",
                           result="hal-ādi-laghu")
        self.assertEqual(got.sutra, "6.4.161")
        self.assertEqual(got.does, "ra")

    def test_without_the_condition_the_rule_is_not_reached(self):
        # ऋजिष्ठः has no consonant before the ऋ, कृष्णिष्ठः is not
        # light — and outside the Veda nothing else supplies र.
        got = before_istha(part="ṛ", before="iṣṭhan")
        self.assertNotEqual(got.sutra, "6.4.161")

    def test_rju_takes_it_optionally_in_the_veda(self):
        # रजिष्ठम् अनु नेषि पन्थाम् beside त्वम् ऋजिष्ठः.
        got = before_istha("ṛju", part="ṛ", before="iṣṭhan",
                           chandasi=True)
        self.assertEqual(got.sutra, "6.4.162")
        self.assertTrue(got.optional)

    def test_and_not_outside_it(self):
        got = before_istha("ṛju", part="ṛ", before="iṣṭhan")
        self.assertNotEqual(got.sutra, "6.4.162")


class TheRunReverses(unittest.TestCase):
    """From 6.4.163 the content of each rule is that nothing happens."""

    def test_the_turn_is_at_the_sutra_the_module_names(self):
        self.assertEqual(PRAKRTI_FROM, "6.4.163")

    def test_nothing_before_the_turn_says_prakrtya(self):
        for row in ISTHA_TABLE:
            if row.sutra < PRAKRTI_FROM:
                self.assertNotEqual(row.does, "prakṛtyā", row.sutra)

    def test_the_prakrti_rules_are_a_solid_stretch(self):
        # 6.4.163 to 6.4.169 say प्रकृत्या outright; 6.4.170
        # refuses it and 6.4.171-173 lay words down instead. So
        # the claim is the stretch, not the whole half.
        standing = [row.sutra for row in ISTHA_TABLE
                    if row.does == "prakṛtyā"]
        self.assertEqual(
            standing, ["6.4.%d" % n for n in range(163, 170)])

    def test_a_one_vowel_stem_stands_unchanged(self):
        # स्रजिष्ठः, स्रुचीयान् — and the losses do not reach it.
        got = before_istha(gana="ekāc", before="iṣṭhan")
        self.assertEqual(got.sutra, "6.4.163")
        self.assertEqual(got.does, "prakṛtyā")


class TheInFinalStems(unittest.TestCase):
    """6.4.164 and the two sūtras that widen it."""

    def test_an_in_final_stem_stands_before_an(self):
        # सांकूटिनम्, स्राग्विणम् — where no descendant is meant.
        got = before_istha(gana="in-anta", before="aṇ")
        self.assertEqual(got.sutra, "6.4.164")

    def test_a_descendant_is_shut_out_of_the_general_rule(self):
        got = before_istha(gana="in-anta", before="aṇ",
                           result="apatya")
        self.assertNotEqual(got.sutra, "6.4.164")

    def test_five_stems_stand_even_where_a_descendant_is_meant(self):
        # अपत्यार्थोऽयम् आरम्भः — the sūtra exists for exactly the
        # case 6.4.164 shut out.
        for stem in GATHIN_FIVE:
            got = before_istha(stem, before="aṇ", result="apatya")
            self.assertEqual(got.sutra, "6.4.165", stem)
            self.assertEqual(got.does, "prakṛtyā", stem)

    def test_the_grammarians_own_name_is_one_of_the_five(self):
        # पाणिनोऽपत्यं पाणिनः.
        self.assertIn("paṇin", GATHIN_FIVE)

    def test_a_cluster_at_the_head_does_the_same(self):
        # शाङ्खिनः, माद्रिणः, वाज्रिणः.
        got = before_istha(gana="saṃyoga-ādi-in", before="aṇ",
                           result="apatya")
        self.assertEqual(got.sutra, "6.4.166")


class TheAnFinalStems(unittest.TestCase):
    """6.4.167 holds off two losses at once; 6.4.170 refuses it."""

    def test_an_an_final_stem_stands_before_an(self):
        # सामनः, वैमनः, सौत्वनः, जैत्वनः.
        got = before_istha(gana="an-anta", before="aṇ")
        self.assertEqual(got.sutra, "6.4.167")

    def test_it_names_both_the_losses_it_holds_off(self):
        # अल्लोपटिलोपाव् उभाव् अपि न भवतः — 6.4.134's अ-loss and
        # 6.4.144's टि-loss, and both are codified.
        blocks = provisions_for("6.4.167")[0].blocks
        self.assertEqual(set(blocks), {"6.4.134", "6.4.144"})
        for code in blocks:
            self.assertTrue(REGISTRY.has(code), code)

    def test_a_m_before_the_an_refuses_it_for_a_descendant(self):
        # सौषामः, चान्द्रसामः — the stem does not stand.
        got = before_istha(gana="ma-pūrva-an", before="aṇ",
                           result="apatya")
        self.assertEqual(got.sutra, "6.4.170")
        self.assertEqual(got.does, "")
        self.assertIn("6.4.167", got.blocked_by)

    def test_varman_is_named_out_of_the_refusal(self):
        # चाक्रवर्मणः keeps its अन्.
        got = before_istha("varman", gana="ma-pūrva-an",
                           before="aṇ", result="apatya")
        self.assertNotEqual(got.sutra, "6.4.170")

    def test_and_the_refusal_wants_a_descendant(self):
        # सौत्वनः — no descendant, so 6.4.167 stands after all.
        got = before_istha(gana="ma-pūrva-an", before="aṇ")
        self.assertNotEqual(got.sutra, "6.4.170")


class TheWordsLaidDown(unittest.TestCase):
    """6.4.171–175, निपातन, and the end of the adhyāya."""

    def test_brahma_is_laid_down_where_no_class_is_meant(self):
        # ब्राह्मो गर्भः — and ब्राह्मणः where a class IS meant.
        got = before_istha("brahman", before="aṇ")
        self.assertEqual(got.sutra, "6.4.171")
        self.assertTrue(got.nipatana)
        self.assertNotEqual(
            before_istha("brahman", before="aṇ",
                         result="jāti").sutra, "6.4.171")

    def test_karma_is_laid_down_for_a_habit(self):
        # कर्मशीलः कार्मः.
        got = before_istha("karman", result="tācchīlya")
        self.assertEqual(got.sutra, "6.4.172")

    def test_uksan_divides_between_two_rules_by_sense(self):
        # औक्षं पदम् here, but उक्ष्णोऽपत्यम् औक्ष्णः by 6.4.135.
        got = before_istha("ukṣan", before="aṇ")
        self.assertEqual(got.sutra, "6.4.173")
        self.assertNotEqual(
            before_istha("ukṣan", before="aṇ",
                         result="apatya").sutra, "6.4.173")
        self.assertTrue(REGISTRY.has("6.4.135"))

    def test_eleven_words_are_laid_down_whole(self):
        self.assertEqual(len(NIPATANA_ELEVEN), 11)
        for word in NIPATANA_ELEVEN:
            got = before_istha(word)
            self.assertEqual(got.sutra, "6.4.174", word)
            self.assertTrue(got.nipatana, word)

    def test_five_more_belong_to_the_veda_alone(self):
        self.assertEqual(len(NIPATANA_VEDIC), 5)
        for word in NIPATANA_VEDIC:
            self.assertEqual(
                before_istha(word, chandasi=True).sutra, "6.4.175",
                word)
            self.assertNotEqual(before_istha(word).sutra, "6.4.175",
                                word)

    def test_the_two_lists_do_not_overlap(self):
        # हिरण्मय is 6.4.174's and हिरण्यय 6.4.175's — near enough
        # to be worth asserting they are not the same word.
        self.assertFalse(set(NIPATANA_ELEVEN) & set(NIPATANA_VEDIC))


class NothingHappensByDefault(unittest.TestCase):
    """The resolver's own answer where no rule is reached."""

    def test_an_unnamed_stem_still_loses_its_ti(self):
        # गजिष्ठः — 6.4.155 टेः names no stem, so the general loss
        # does reach a word the run never mentions. That is what
        # makes the default answer hard to trigger at all.
        got = before_istha("gaja", before="iṣṭhan")
        self.assertEqual(got.sutra, "6.4.155")

    def test_outside_the_affixes_the_run_names_nothing_fires(self):
        # A भ stem before an ordinary ending is not this run's
        # business: 6.4.129-153 has already said what happens.
        got = before_istha("gaja", before="sup")
        self.assertEqual(got.sutra, "")
        self.assertEqual(got.does, "")

    def test_and_that_is_not_the_same_as_prakrtya(self):
        # Half this run says in so many words that the stem stands;
        # the difference is that there a rule says it, and the
        # answer carries that rule's number.
        silent = before_istha("gaja", before="sup")
        stated = before_istha(gana="ekāc", before="iṣṭhan")
        self.assertEqual(stated.does, "prakṛtyā")
        self.assertNotEqual(silent.does, stated.does)
        self.assertTrue(stated.sutra)


class Registration(unittest.TestCase):
    """Every row reaches the registry, and the adhyāya is closed."""

    def test_the_run_is_contiguous(self):
        codes = [row.sutra for row in ISTHA_TABLE]
        self.assertEqual(
            codes, ["6.4.%d" % n for n in range(154, 176)])

    def test_every_sutra_is_registered_with_real_notes(self):
        for row in ISTHA_TABLE:
            self.assertTrue(REGISTRY.has(row.sutra), row.sutra)
            notes = REGISTRY.get(row.sutra).notes
            self.assertGreater(len(notes), 100, row.sutra)
            self.assertIn("SETTLED", notes, row.sutra)

    def test_adhyaya_six_is_complete(self):
        # पाद ६.१ has 223 sūtras, ६.२ has 199, ६.३ has 139 and
        # ६.४ has 175. With this run the whole adhyāya is read.
        for pada, last in ((1, 223), (2, 199), (3, 139), (4, 175)):
            for n in range(1, last + 1):
                code = "6.%d.%d" % (pada, n)
                self.assertTrue(REGISTRY.has(code), code)


class WhatIsNotCodifiedYet(unittest.TestCase):
    """
    The debts, written as the exact shortfall.

    Each fails the moment the thing it names lands, and must then
    be rewritten to state the live dependency instead.
    """

    def test_the_comparative_senses_are_codified_but_not_the_rest(self):
        # 5.3.55 अतिशायने तमबिष्ठनौ gives इष्ठन् its sense and
        # 5.3.57 द्विवचनविभज्योपपदे तरबीयसुनौ gives ईयसुन् its; both
        # are live. What is not is 7.1.70's नुम्, which every
        # भूयिष्ठ- and ज्यायस्-form needs in the strong cases.
        # 7.1.70's नुम् landed with पाद ७.१ while this was being
        # written, so every भूयिष्ठ- and ज्यायस्-form's strong
        # cases can be asked of the engine now.
        self.assertTrue(REGISTRY.has("5.3.55"))
        self.assertTrue(REGISTRY.has("5.3.57"))
        self.assertTrue(REGISTRY.has("7.1.70"))

    def test_the_next_adhyaya_is_read_as_far_as_its_second_pada(self):
        # अङ्गस्य runs from 6.4.1 to 7.4.97, so this run's stems
        # are handed straight to अध्याय ७. पाद ७.१ and ७.२ have
        # both been read through since this was written, so
        # 7.2.115's vṛddhi can be asked of the engine now, and
        # पाद ७.३ has been opened since. 7.4.97, where the
        # अङ्गस्य heading finally ends, is still far off.
        self.assertTrue(REGISTRY.has("7.1.1"))
        self.assertTrue(REGISTRY.has("7.2.115"))
        self.assertTrue(REGISTRY.has("7.3.1"))
        # 7.4.97 has landed since, so अङ्गस्य reaches its end
        # and this run's stems are handed to a complete अध्याय ७.
        self.assertTrue(REGISTRY.has("7.4.97"))


if __name__ == "__main__":
    unittest.main()
