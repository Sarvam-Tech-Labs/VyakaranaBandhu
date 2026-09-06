# -*- coding: utf-8 -*-
"""
८.२.४–२२ — the merged vowel's accent, the न् dropped, मतुप्'s व.

Four blocks in nineteen sūtras, and the tests take them in turn.
The one that matters most is 8.2.21, where a rule that reads as
a free option is not one: a throat is always गल and poison is
always गर, and the choice is made by the word.
"""

from __future__ import annotations

import unittest

from src.astadhyayi.nalopa_matup import (
    ASANDIVAT_SIX,
    ASIDDHA,
    NALOPA_RUN,
    NALOPA_TABLE,
    VYAVASTHITA,
    in_the_word,
    provisions_for,
)
from src.astadhyayi.sources import REGISTRY
import src.astadhyayi.rules  # noqa: F401  (populates REGISTRY)


class TheMergedVowelsAccent(unittest.TestCase):
    """8.2.4–6."""

    def test_an_anudatta_after_an_accented_semivowel_is_svarita(self):
        # कुमार्यौ, कुमार्यः.
        got = in_the_word(gana="udātta-svarita-yaṇ-para")
        self.assertEqual(got.sutra, "8.2.4")
        self.assertEqual(got.does, "svarita")

    def test_and_the_note_walks_the_derivation_backwards(self):
        # 6.1.161 accents the ई, the ई becomes य्, and the य्
        # carries the accent forward. That rule is codified.
        why = provisions_for("8.2.4")[0].why
        self.assertIn("6.1.161", why)
        self.assertTrue(REGISTRY.has("6.1.161"))

    def test_a_vowel_merged_with_an_udatta_is_udatta(self):
        # अग्नी, वायू, वृक्षैः.
        got = in_the_word(gana="ekādeśa-udātta")
        self.assertEqual(got.sutra, "8.2.5")
        self.assertEqual(got.does, "udātta")

    def test_and_the_counter_example_turns_on_the_tripadi_itself(self):
        # पररूपे कर्तव्ये स्वरितस्य असिद्धत्वात् — 8.4.66's
        # स्वरित cannot be seen from where 6.1.97 stands.
        why = provisions_for("8.2.5")[0].why
        self.assertIn("असिद्धत्वात्", why)
        self.assertIn("8.4.66", why)
        self.assertIn("पचन्ति", provisions_for("8.2.5")[0].keeps_out)

    def test_but_at_a_words_beginning_it_may_be_either(self):
        # सूत्थितः heard two ways.
        got = in_the_word(gana="ekādeśa-udātta",
                          before="pada-ādi-anudātta")
        self.assertEqual(got.sutra, "8.2.6")
        self.assertTrue(got.optional)
        self.assertIn("8.2.5", got.blocked_by)


class TheNDropped(unittest.TestCase):
    """8.2.7–8, and the refusal read as proof."""

    def test_a_pratipadika_word_loses_its_final_n(self):
        # राजा, राजभ्याम्, राजभिः, राजतरः.
        got = in_the_word(gana="prātipadika-n-anta")
        self.assertEqual(got.sutra, "8.2.7")
        self.assertEqual(got.does, "lopa")

    def test_and_both_of_its_words_are_tested(self):
        # प्रातिपदिकग्रहणं किम्? अहन्नहिम्; अन्तग्रहणं किम्?
        # राजानौ.
        keeps = provisions_for("8.2.7")[0].keeps_out
        self.assertIn("अहन्नहिम्", keeps)
        self.assertIn("राजानौ", keeps)

    def test_but_not_before_ni_or_in_the_vocative(self):
        # आर्द्रे चर्मन्; हे राजन्.
        for affix in ("ṅi", "sambuddhi"):
            got = in_the_word(gana="prātipadika-n-anta",
                              before=affix)
            self.assertEqual(got.sutra, "8.2.8", affix)
            self.assertTrue(got.refuses, affix)
            self.assertIn("8.2.7", got.blocked_by, affix)

    def test_and_the_refusal_proves_a_name_survives_its_ending(self):
        # With the ending gone the word would be no प्रातिपदिक
        # at all and there would be nothing to refuse — so
        # 1.1.62 keeps the name alive, and that rule is codified.
        why = provisions_for("8.2.8")[0].why
        self.assertIn("प्रत्ययलक्षणेन", why)
        self.assertTrue(REGISTRY.has("1.1.62"))


class TheVOfMatup(unittest.TestCase):
    """8.2.9–17, four conditions and four laid-down words."""

    def test_four_different_conditions_give_the_same_substitute(self):
        # म् or अ, a झय्, a name, and in the Veda इ or र्.
        wanted = {
            ("ma-a-anta-upadha", False): "8.2.9",
            ("jhay-anta", False): "8.2.10",
            ("i-varṇa-repha-anta", True): "8.2.15",
        }
        for (gana, vedic), code in wanted.items():
            got = in_the_word(gana=gana, before="matup",
                              chandasi=vedic)
            self.assertEqual(got.sutra, code, gana)
            self.assertEqual(got.does, "va", gana)
        named = in_the_word(before="matup", sense="saṃjñā")
        self.assertEqual(named.sutra, "8.2.11")
        self.assertEqual(named.does, "va")

    def test_and_the_name_rule_does_all_the_work_on_its_own(self):
        # अहीवती, कपीवती — all ई-final, which neither 8.2.9 nor
        # 8.2.10 reaches, so nothing but the sense is left.
        why = provisions_for("8.2.11")[0].why
        self.assertIn("ई-final", why)
        self.assertNotEqual(
            in_the_word(before="matup").sutra, "8.2.11")

    def test_six_names_are_laid_down_and_what_they_give_is_the_stem(self):
        # वत्वं पूर्वेण एव सिद्धम्, आदेशार्थानि निपातनानि.
        self.assertEqual(len(ASANDIVAT_SIX), 6)
        for word in ASANDIVAT_SIX:
            got = in_the_word(word, sense="saṃjñā")
            self.assertEqual(got.sutra, "8.2.12", word)
            self.assertTrue(got.nipatana, word)
        self.assertIn("आदेशार्थानि",
                      provisions_for("8.2.12")[0].why)

    def test_and_the_kasika_records_a_second_opinion_about_them(self):
        # अपरे तु आहुः — आसन्दी is simply another stem.
        self.assertIn("अपरे तु आहुः",
                      provisions_for("8.2.12")[0].why)

    def test_two_words_keep_a_sound_only_in_a_named_sense(self):
        # उदन्वान् of the sea, राजन्वान् of good government.
        for word, sense, code in (("udanvat", "udadhi", "8.2.13"),
                                  ("rājanvat", "saurājya",
                                   "8.2.14")):
            got = in_the_word(word, sense=sense)
            self.assertEqual(got.sutra, code, word)
            self.assertTrue(got.nipatana, word)
            self.assertNotEqual(in_the_word(word).sutra, code, word)

    def test_and_the_pot_is_left_out_for_a_reason_the_vrtti_states(self):
        # उदकसत्तासम्बन्धसामान्यम् — the pot merely HAS water
        # where the sea HOLDS it.
        self.assertIn("दधात्यर्थो न विवक्ष्यते",
                      provisions_for("8.2.13")[0].why)

    def test_two_vedic_rules_give_an_augment_instead(self):
        # अक्षण्वन्तः; सुपथिन्तरः.
        for gana, before, code in (("an-anta", "matup", "8.2.16"),
                                   ("n-anta", "gha", "8.2.17")):
            got = in_the_word(gana=gana, before=before,
                              chandasi=True)
            self.assertEqual(got.sutra, code, gana)
            self.assertEqual(got.does, "nuṭ", gana)

    def test_and_that_augment_blocks_the_very_rule_the_run_is_about(self):
        # नुटोऽसिद्धत्वात् तस्य च वत्वं न भवति — with the न्
        # invisible, मतुप् is after neither a म् nor an अ. नुटः
        # plus असिद्धत्वात् elides the अ, so the quoted fragment
        # has to begin after the अवग्रह.
        self.assertIn("सिद्धत्वात् तस्य",
                      provisions_for("8.2.16")[0].why)


class RBecomingL(unittest.TestCase):
    """8.2.18–22, and the option that is not one."""

    def test_krp_gives_kalpta(self):
        got = in_the_word("kṛp")
        self.assertEqual(got.sutra, "8.2.18")
        self.assertEqual(got.does, "la")

    def test_and_both_letters_are_named_by_their_bare_sound(self):
        # र इति श्रुतिसामान्यम् — so 1.3.93 लुटि च क्ऌपः is
        # intelligible, the root being written with a ऌ this
        # rule has already put there.
        why = provisions_for("8.2.18")[0].why
        self.assertIn("श्रुतिसामान्यम्", why)
        self.assertIn("1.3.93", why)

    def test_a_preverbs_r_before_ay_and_gr_before_yan(self):
        # पलायते; निजेगिल्यते.
        self.assertEqual(
            in_the_word(gana="upasarga", before="ayati").sutra,
            "8.2.19")
        self.assertEqual(
            in_the_word("gṝ", before="yaṅ").sutra, "8.2.20")

    def test_and_the_commentary_splits_on_which_gr_is_meant(self):
        # केचिद् ... अपरे तु — one party takes both roots, the
        # other only 'swallow'.
        why = provisions_for("8.2.20")[0].why
        self.assertIn("केचिद्", why)
        self.assertIn("अपरे तु", why)

    def test_before_a_vowel_it_is_optional_but_not_freely(self):
        # निगिरति, निगिलति — and the choice is the word's.
        got = in_the_word("gṝ", before="ac-ādi")
        self.assertEqual(got.sutra, "8.2.21")
        self.assertTrue(got.optional)
        self.assertIn("व्यवस्थितविभाषा", VYAVASTHITA)
        self.assertIn("गल", VYAVASTHITA)
        self.assertIn("गर", VYAVASTHITA)
        self.assertIn(VYAVASTHITA, provisions_for("8.2.21")[0].why)

    def test_and_pari_takes_it_before_three_words(self):
        # परिघः/पलिघः; पर्यङ्कः/पल्यङ्कः; परियोगः/पलियोगः.
        for after in ("gha", "aṅka", "yoga"):
            got = in_the_word("pari", before=after)
            self.assertEqual(got.sutra, "8.2.22", after)
            self.assertTrue(got.optional, after)

    def test_and_that_gha_is_the_sound_and_not_the_name(self):
        # घ इति स्वरूपग्रहणम् अत्र इष्यते — which the run needs
        # said, 8.2.17 having used the NAME five sūtras back.
        self.assertIn("स्वरूपग्रहणम्",
                      provisions_for("8.2.22")[0].why)


class NothingHappensByDefault(unittest.TestCase):
    """A word none of these rules reaches goes on as it stands."""

    def test_an_unnamed_word_reaches_nothing(self):
        got = in_the_word("vṛkṣa")
        self.assertEqual(got.sutra, "")
        self.assertEqual(got.does, "")


class Registration(unittest.TestCase):
    """Every row reaches the registry with real notes."""

    def test_the_run_is_contiguous(self):
        self.assertEqual(NALOPA_RUN, ("8.2.4", "8.2.22"))
        codes = [row.sutra for row in NALOPA_TABLE]
        self.assertEqual(
            codes, ["8.2.%d" % n for n in range(4, 23)])

    def test_the_heading_the_whole_pada_stands_under_is_codified(self):
        # 8.2.1 पूर्वत्रासिद्धम्, reached ahead long ago.
        self.assertEqual(ASIDDHA, "8.2.1")
        self.assertTrue(REGISTRY.has(ASIDDHA))

    def test_every_sutra_is_registered_with_real_notes(self):
        for row in NALOPA_TABLE:
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

    def test_what_this_run_appeals_to_backwards_is_live(self):
        # 8.2.1's ordering, 6.1.161's accent, 1.1.62's name and
        # 1.3.93's written ऌ. All codified.
        for code in ("8.2.1", "6.1.161", "1.1.62", "1.3.93"):
            self.assertTrue(REGISTRY.has(code), code)

    def test_and_the_pada_after_this_one_has_been_read(self):
        # 8.3.1 मतुवसो रु सम्बुद्धौ छन्दसि opens पाद ८.३ and
        # 8.3.55 अपदान्तस्य मूर्धन्यः is where 8.1.16's पदस्य
        # heading finally stops. Both are codified, so the
        # heading this run stands under can be asked from its
        # opening to its close.
        self.assertTrue(REGISTRY.has("8.3.1"))
        self.assertTrue(REGISTRY.has("8.3.55"))


if __name__ == "__main__":
    unittest.main()
