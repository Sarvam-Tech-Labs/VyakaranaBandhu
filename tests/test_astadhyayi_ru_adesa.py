# -*- coding: utf-8 -*-
"""
८.२.६२–८१ — क्विन्, the रुँ, अहन्, and what अदस् becomes.

Nineteen rows and one sūtra missing from them: 8.2.66 ससजुषो
रुँः was codified inside `anga` long before this pāda was read.
The tests hold that gap open on purpose — the run is complete
only because both halves are.
"""

from __future__ import annotations

import unittest

from src.astadhyayi.ru_adesa import (
    AVAYAH_THREE,
    BHA_KUR_CHUR,
    CODIFIED_APART,
    RU_RUN,
    RU_TABLE,
    UBHAYATHA_THREE,
    VASU_FOUR,
    provisions_for,
    the_word_end,
)
from src.astadhyayi.sources import REGISTRY
import src.astadhyayi.rules  # noqa: F401  (populates REGISTRY)


class WhatAWordEndsIn(unittest.TestCase):
    """8.2.62–65."""

    def test_a_kvin_word_ends_in_a_guttural(self):
        # घृतस्पृक्, ऋत्विक्.
        got = the_word_end(gana="kvin-pratyaya")
        self.assertEqual(got.sutra, "8.2.62")
        self.assertEqual(got.does, "ku")

    def test_and_the_name_is_of_the_whole_word_not_the_affix(self):
        # क्विन् प्रत्ययो यस्माद् धातोः स क्विन्प्रत्ययः — which
        # is why the guttural lands on the LAST sound.
        self.assertIn("यस्माद् धातोः",
                      provisions_for("8.2.62")[0].why)

    def test_nas_does_it_only_optionally(self):
        # जीवनक् beside जीवनट्.
        got = the_word_end("naś")
        self.assertEqual(got.sutra, "8.2.63")
        self.assertTrue(got.optional)

    def test_and_the_other_side_of_that_option_is_not_nothing(self):
        # षत्वे प्राप्ते कुत्वविकल्पः — where the guttural does
        # not come a ष् does, so the alternatives are ट् and क्.
        self.assertIn("षत्वे प्राप्ते",
                      provisions_for("8.2.63")[0].why)

    def test_a_m_final_root_gives_a_word_ending_in_n(self):
        # प्रशान्, प्रतान्, प्रदान्.
        got = the_word_end(gana="ma-anta-dhātu")
        self.assertEqual(got.sutra, "8.2.64")
        self.assertEqual(got.does, "na")

    def test_and_that_n_survives_a_rule_four_sutras_back(self):
        # नत्वस्य असिद्धत्वान् नलोपो न भवति — 8.2.7 cannot see
        # it, and that rule is codified.
        self.assertIn("असिद्धत्वान्",
                      provisions_for("8.2.64")[0].why)
        self.assertTrue(REGISTRY.has("8.2.7"))

    def test_and_before_a_m_or_a_v_it_comes_too(self):
        # अगन्म तमसस् पारम्; अगन्व; जगन्वान्.
        for after in ("ma", "va"):
            got = the_word_end(gana="ma-anta-dhātu", before=after)
            self.assertEqual(got.sutra, "8.2.65", after)


class TheRuAndAhan(unittest.TestCase):
    """8.2.67–71, and the one rule that is not in this table."""

    def test_the_run_leaves_a_hole_where_8_2_66_is(self):
        # ससजुषो रुँः lives in `anga` and is not restated here.
        self.assertEqual(CODIFIED_APART, ("8.2.66",))
        codes = [row.sutra for row in RU_TABLE]
        self.assertNotIn("8.2.66", codes)
        self.assertTrue(REGISTRY.has("8.2.66"))

    def test_and_the_run_is_complete_only_because_both_halves_are(self):
        for n in range(62, 82):
            self.assertTrue(REGISTRY.has("8.2.%d" % n), n)

    def test_three_words_are_laid_down_whole(self):
        # अवयाः, श्वेतवाः, पुरोडाः.
        self.assertEqual(len(AVAYAH_THREE), 3)
        for word in AVAYAH_THREE:
            got = the_word_end(word)
            self.assertEqual(got.sutra, "8.2.67", word)
            self.assertTrue(got.nipatana, word)

    def test_ahan_takes_a_ru_and_then_a_plain_r(self):
        # अहोभ्याम्; अहर् ददाति.
        self.assertEqual(the_word_end("ahan").does, "ru")
        got = the_word_end("ahan", before="a-sup")
        self.assertEqual(got.sutra, "8.2.69")
        self.assertEqual(got.does, "ra")
        self.assertIn("8.2.68", got.blocked_by)

    def test_and_the_sutras_own_spelling_is_read_as_proof(self):
        # नलोपम् अकृत्वा निर्देशो ज्ञापकः — अहन् is written with
        # its न् so that 8.2.7 shall not take it off.
        why = provisions_for("8.2.68")[0].why
        self.assertIn("ज्ञापकः", why)
        self.assertIn("नलोपाभावो", why)

    def test_the_veda_takes_three_words_both_ways(self):
        # अम्न एव beside अम्नर् एव.
        self.assertEqual(len(UBHAYATHA_THREE), 3)
        for word in UBHAYATHA_THREE:
            got = the_word_end(word, chandasi=True)
            self.assertEqual(got.sutra, "8.2.70", word)
            self.assertTrue(got.optional, word)

    def test_and_bhuvas_only_as_the_great_utterance(self):
        # भुवर् इत्य् अन्तरिक्षम् — and not भुवो विश्वेषु.
        got = the_word_end("bhuvas", gana="mahāvyāhṛti",
                           chandasi=True)
        self.assertEqual(got.sutra, "8.2.71")
        self.assertNotEqual(
            the_word_end("bhuvas", chandasi=True).sutra, "8.2.71")


class TheDAndTheLengthening(unittest.TestCase):
    """8.2.72–79."""

    def test_four_words_end_in_d(self):
        self.assertEqual(len(VASU_FOUR), 4)
        for word in VASU_FOUR:
            got = the_word_end(word)
            self.assertEqual(got.sutra, "8.2.72", word)
            self.assertEqual(got.does, "da", word)

    def test_and_the_vrtti_says_which_of_the_four_is_qualified(self):
        # वसुर् एव विशेष्यते — since वसु may or may not end in
        # स्, स्रंस् and ध्वंस् always do, and अनडुह् never does.
        why = provisions_for("8.2.72")[0].why
        self.assertIn("व्यभिचारा", why)
        # असम्भवात् + च joins into असम्भवाच् च.
        self.assertIn("असम्भवाच् च", why)

    def test_two_endings_take_a_d_or_a_ru_before_two_affixes(self):
        # अचकाद् भवान्; अचकास् त्वम् beside अचकात् त्वम्.
        self.assertEqual(
            the_word_end(gana="sa-anta-a-asti", before="tip").does,
            "da")
        for gana, code in (("sa-anta-dhātu", "8.2.74"),
                           ("da-anta-dhātu", "8.2.75")):
            got = the_word_end(gana=gana, before="sip")
            self.assertEqual(got.sutra, code, gana)
            self.assertTrue(got.optional, gana)

    def test_and_one_sutra_says_two_words_for_the_next_one(self):
        # धातुग्रहणं च उत्तरार्थं रुग्रहणं च.
        self.assertIn("उत्तरार्थं",
                      provisions_for("8.2.74")[0].why)

    def test_three_sutras_lengthen_an_ik_and_each_reaches_further(self):
        # गीः; दीव्यति; मूर्छिता.
        wanted = {("ra-va-anta-dhātu", ""): "8.2.76",
                  ("ra-va-anta-dhātu", "hal"): "8.2.77",
                  ("ra-va-upadha-hal-para", "hal"): "8.2.78"}
        for (gana, before), code in wanted.items():
            got = the_word_end(gana=gana, before=before)
            self.assertEqual(got.sutra, code, gana)
            self.assertEqual(got.does, "dīrgha", gana)

    def test_and_the_v_of_the_first_is_said_for_the_two_after_it(self):
        # वकारग्रहणम् उत्तरार्थम् — here only the र् does work.
        self.assertIn("उत्तरार्थम्",
                      provisions_for("8.2.76")[0].why)

    def test_and_three_words_refuse_all_three_lengthenings(self):
        # धुर्यः, कुर्यात्, छुर्यात्.
        self.assertEqual(len(BHA_KUR_CHUR), 3)
        for word in BHA_KUR_CHUR:
            got = the_word_end(word)
            self.assertEqual(got.sutra, "8.2.79", word)
            self.assertTrue(got.refuses, word)
            self.assertEqual(set(got.blocked_by),
                             {"8.2.76", "8.2.77", "8.2.78"}, word)


class WhatAdasBecomes(unittest.TestCase):
    """8.2.80–81, where a word is rebuilt from the inside."""

    def test_the_d_becomes_m_and_what_follows_becomes_u(self):
        # अमुम्, अमू, अमुना.
        got = the_word_end("adas", gana="a-sa-anta")
        self.assertEqual(got.sutra, "8.2.80")
        self.assertEqual(got.does, "u-ma")

    def test_and_the_u_takes_the_length_of_what_it_replaces(self):
        # भाव्यमानेन अपि उकारेण सवर्णानां ग्रहणम् इष्यते — which
        # is how अमू and अमुना come from one rule.
        self.assertIn("भाव्यमानेन",
                      provisions_for("8.2.80")[0].why)

    def test_and_in_the_plural_it_is_an_i_instead(self):
        # अमी, अमीभिः, अमीषाम्.
        got = the_word_end("adas", gana="bahuvacana")
        self.assertEqual(got.sutra, "8.2.81")
        self.assertEqual(got.does, "ī-ma")
        self.assertIn("8.2.80", got.blocked_by)

    def test_and_that_plural_names_a_sense_and_not_an_ending(self):
        # बहुवचन इत्यर्थनिर्देशोऽयम् — अमी has no ending left to
        # be plural with.
        # इति + अर्थनिर्देश makes इत्यर्थ..., so the अ of
        # अर्थ is inside the त्य ligature and the fragment has
        # to begin after it.
        self.assertIn("र्थनिर्देशोऽयम्",
                      provisions_for("8.2.81")[0].why)


class NothingHappensByDefault(unittest.TestCase):
    """A word none of these rules reaches ends as it stands."""

    def test_an_unnamed_word_reaches_nothing(self):
        got = the_word_end("vṛkṣa")
        self.assertEqual(got.sutra, "")
        self.assertEqual(got.does, "")


class Registration(unittest.TestCase):
    """Every row reaches the registry with real notes."""

    def test_the_table_holds_the_run_minus_what_was_codified_apart(self):
        self.assertEqual(RU_RUN, ("8.2.62", "8.2.81"))
        codes = [row.sutra for row in RU_TABLE]
        expected = ["8.2.%d" % n for n in range(62, 82)
                    if "8.2.%d" % n not in CODIFIED_APART]
        self.assertEqual(codes, expected)

    def test_every_sutra_is_registered_with_real_notes(self):
        for row in RU_TABLE:
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
        # 8.2.7's न्-loss, which 8.2.64's own न् escapes; 8.2.66,
        # which 8.2.67's स् is laid down for; and 1.1.62, which
        # 8.2.69 has to argue against.
        for code in ("8.2.7", "8.2.66", "1.1.62"):
            self.assertTrue(REGISTRY.has(code), code)

    def test_and_what_the_ru_then_becomes_has_landed(self):
        # 8.3.15 खरवसानयोर्विसर्जनीयः makes the visarga and
        # 8.3.17 भोभगोअघोअपूर्वस्य योऽशि turns the रुँ into a
        # य् before a vowel — with three teachers disagreeing
        # about that य् in the three sūtras after. All codified,
        # so the रुँ this run gives can be followed all the way.
        for code in ("8.3.15", "8.3.17", "8.3.18", "8.3.19"):
            self.assertTrue(REGISTRY.has(code), code)


if __name__ == "__main__":
    unittest.main()
