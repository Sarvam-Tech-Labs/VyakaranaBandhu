# -*- coding: utf-8 -*-
"""
८.२.४२–६१ — the निष्ठा's त्, and the six things it becomes.

Twenty sūtras on one affix. Half the run turns on a SENSE and
not a form, and the tests give that half a class of its own:
शीनम् against शीतम्, समक्नौ against उदक्तम्, आद्यूनः against
द्यूतम्, निर्वाणः against निर्वातः — four pairs that differ in
nothing but what is meant.
"""

from __future__ import annotations

import unittest

from src.astadhyayi.nistha_natva import (
    DHYADI_FIVE,
    NASATTADI_SIX,
    NISTHA_RUN,
    NISTHA_TABLE,
    NUDADI_SIX,
    PHULLADI_FOUR,
    THE_AFFIX,
    provisions_for,
    the_nistha,
)
from src.astadhyayi.sources import REGISTRY
import src.astadhyayi.rules  # noqa: F401  (populates REGISTRY)


class WhereTheNComes(unittest.TestCase):
    """8.2.42–46, five shapes that give the त् a न्."""

    def test_after_an_r_or_a_d_and_the_d_goes_too(self):
        # आस्तीर्णम्, विशीर्णम्; भिन्नः, छिन्नः.
        got = the_nistha(gana="ra-da-para")
        self.assertEqual(got.sutra, "8.2.42")
        self.assertEqual(got.does, "na")
        self.assertIn("पूर्वस्य च दः",
                      provisions_for("8.2.42")[0].why)

    def test_four_more_shapes_give_it_too(self):
        wanted = {"saṃyoga-ādi-āt-anta-yaṇvat": "8.2.43",
                  "lvādi": "8.2.44",
                  "odit": "8.2.45"}
        for gana, code in wanted.items():
            got = the_nistha(gana=gana)
            self.assertEqual(got.sutra, code, gana)
            self.assertEqual(got.does, "na", gana)
        self.assertEqual(
            the_nistha("kṣi", gana="dīrgha").sutra, "8.2.46")

    def test_and_one_of_them_is_bounded_by_the_root_list_itself(self):
        # लूञ् छेदने इत्येतत्प्रभृति व्री वरणे इति यावत् — the
        # ग्रन्थ and not the grammar says where the class stops.
        why = provisions_for("8.2.44")[0].why
        self.assertIn("व्री वरणे", why)
        self.assertIn("वृत्करणेन", why)

    def test_and_another_is_stated_for_three_earlier_rules_output(self):
        # 6.4.59–61 give क्षि its length, and this rule does
        # nothing where they have not run. All three codified.
        why = provisions_for("8.2.46")[0].why
        self.assertIn("6.4.59", why)
        for code in ("6.4.59", "6.4.60", "6.4.61"):
            self.assertTrue(REGISTRY.has(code), code)
        self.assertNotEqual(the_nistha("kṣi").sutra, "8.2.46")


class WhereTheSenseDecides(unittest.TestCase):
    """8.2.47–50, four pairs told apart by meaning alone."""

    def test_each_of_the_four_has_a_form_beside_it(self):
        wanted = {("śyai", "a-sparśa"): "8.2.47",
                  ("añc", "an-apādāna"): "8.2.48",
                  ("div", "a-vijigīṣā"): "8.2.49",
                  ("nirvāṇa", "a-vāta"): "8.2.50"}
        for (root, sense), code in wanted.items():
            got = the_nistha(root, sense=sense)
            self.assertEqual(got.sutra, code, root)
            # and without the sense the rule is not reached
            self.assertNotEqual(the_nistha(root).sutra, code, root)

    def test_and_each_records_the_form_it_keeps_out(self):
        # शीतो वायुः; उदक्तम् उदकं कूपात्; द्यूतम् वर्तते;
        # निर्वातो वातः.
        wanted = {"8.2.47": "शीतो वायुः",
                  "8.2.48": "उदक्तम्",
                  "8.2.49": "द्यूतं",
                  "8.2.50": "निर्वातो वातः"}
        for code, form in wanted.items():
            self.assertIn(form, provisions_for(code)[0].keeps_out,
                          code)

    def test_and_one_of_them_says_exactly_why_the_senses_part(self):
        # विजिगीषया हि तत्र अक्षपातनादि क्रियते — the dice are
        # thrown in order to win.
        self.assertIn("अक्षपातनादि",
                      provisions_for("8.2.49")[0].why)


class ThreeOtherSounds(unittest.TestCase):
    """8.2.51–55, क्, व्, म् and ल्."""

    def test_three_single_roots_take_three_different_sounds(self):
        wanted = {"śuṣ": ("8.2.51", "ka"),
                  "pac": ("8.2.52", "va"),
                  "kṣai": ("8.2.53", "ma")}
        for root, (code, does) in wanted.items():
            got = the_nistha(root)
            self.assertEqual(got.sutra, code, root)
            self.assertEqual(got.does, does, root)

    def test_and_one_finished_word_has_two_rules_in_it(self):
        # पक्व — the क् is 8.2.30's and the व् is 8.2.52's, and
        # neither is visible in the written stem.
        self.assertIn("8.2.30", provisions_for("8.2.52")[0].why)
        self.assertTrue(REGISTRY.has("8.2.30"))

    def test_the_fourth_is_optional_and_its_other_side_is_not_plain(self):
        # प्रस्तीमः beside प्रस्तीतः — and where the म् does
        # not come the न् cannot either, 8.2.43 being invisible.
        got = the_nistha("styai", upasarga="pra")
        self.assertEqual(got.sutra, "8.2.54")
        self.assertTrue(got.optional)
        self.assertIn("पूर्वत्रासिद्धत्वात्",
                      provisions_for("8.2.54")[0].why)

    def test_and_four_words_are_laid_down_without_a_preverb(self):
        # फुल्ल, क्षीब, कृश, उल्लाघ.
        self.assertEqual(len(PHULLADI_FOUR), 4)
        for word in PHULLADI_FOUR:
            got = the_nistha(word, upasarga="anupasarga")
            self.assertEqual(got.sutra, "8.2.55", word)
            self.assertTrue(got.nipatana, word)
            self.assertNotEqual(the_nistha(word).sutra, "8.2.55",
                                word)


class TheOptionAndTheOnlyRefusal(unittest.TestCase):
    """8.2.56–57."""

    def test_six_roots_have_two_forms_each(self):
        # नुन्नः/नुत्तः, विन्नः/वित्तः, त्राणः/त्रातः.
        self.assertEqual(len(NUDADI_SIX), 6)
        for root in NUDADI_SIX:
            got = the_nistha(root)
            self.assertEqual(got.sutra, "8.2.56", root)
            self.assertTrue(got.optional, root)

    def test_five_roots_refuse_it_outright(self):
        # ध्यातः, ख्यातः, पूर्तः, मूर्तः, मत्तः.
        self.assertEqual(len(DHYADI_FIVE), 5)
        for root in DHYADI_FIVE:
            got = the_nistha(root)
            self.assertEqual(got.sutra, "8.2.57", root)
            self.assertTrue(got.refuses, root)

    def test_and_that_refusal_is_the_only_one_in_the_whole_run(self):
        refusing = [row.sutra for row in NISTHA_TABLE if row.refuses]
        self.assertEqual(refusing, ["8.2.57"])

    def test_and_it_is_aimed_at_three_rules_at_once(self):
        # 8.2.42 for पॄ and मूर्छ्, 8.2.43 for ध्या and ख्या,
        # 8.2.56 for मद्.
        row = provisions_for("8.2.57")[0]
        self.assertEqual(set(row.blocks),
                         {"8.2.42", "8.2.43", "8.2.56"})


class FourWordsLaidDown(unittest.TestCase):
    """8.2.58–61, a त् where the grammar owed a न्."""

    def test_three_words_keep_their_t_in_a_named_sense(self):
        wanted = {("vitta", "bhoga"): "8.2.58",
                  ("bhitta", "śakala"): "8.2.59",
                  ("ṛṇa", "ādhamarṇya"): "8.2.60"}
        for (word, sense), code in wanted.items():
            got = the_nistha(word, sense=sense)
            self.assertEqual(got.sutra, code, word)
            self.assertTrue(got.nipatana, word)

    def test_and_one_of_them_buys_a_compound_besides(self):
        # सप्तम्यन्तेन उत्तरपदेन समासः — a locative first
        # member, which no ordinary rule allows.
        self.assertIn("सप्तम्यन्तेन",
                      provisions_for("8.2.60")[0].why)

    def test_and_the_vrtti_keeps_the_root_out_of_one_of_them(self):
        # भिदिक्रिया शब्दव्युत्पत्तेर् एव निमित्तम् — the root
        # is only the word's etymology, and where the SPLITTING
        # is meant भिन्नम् stands.
        self.assertIn("शब्दव्युत्पत्तेर्",
                      provisions_for("8.2.59")[0].why)

    def test_six_vedic_forms_are_laid_down_as_absences(self):
        # नत्वाभावो निपात्यते — the whole sūtra lists places
        # where the run's own rule is set aside.
        self.assertEqual(len(NASATTADI_SIX), 6)
        for word in NASATTADI_SIX:
            got = the_nistha(word, chandasi=True)
            self.assertEqual(got.sutra, "8.2.61", word)
            self.assertTrue(got.nipatana, word)
        self.assertIn("नत्वाभावो",
                      provisions_for("8.2.61")[0].why)
        self.assertIn("नसन्नम्",
                      provisions_for("8.2.61")[0].keeps_out)


class NothingHappensByDefault(unittest.TestCase):
    """A root none of these rules names keeps the affix's त्."""

    def test_an_unnamed_root_reaches_nothing(self):
        got = the_nistha("kṛ")
        self.assertEqual(got.sutra, "")
        self.assertEqual(got.does, "")
        self.assertIn("keeps the t", got.why)


class Registration(unittest.TestCase):
    """Every row reaches the registry with real notes."""

    def test_the_run_is_contiguous(self):
        self.assertEqual(NISTHA_RUN, ("8.2.42", "8.2.61"))
        codes = [row.sutra for row in NISTHA_TABLE]
        self.assertEqual(
            codes, ["8.2.%d" % n for n in range(42, 62)])

    def test_the_affix_the_whole_run_is_about_is_codified(self):
        self.assertEqual(THE_AFFIX, "3.2.102")
        self.assertTrue(REGISTRY.has(THE_AFFIX))

    def test_every_sutra_is_registered_with_real_notes(self):
        for row in NISTHA_TABLE:
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

    def test_the_affix_and_the_lengths_this_run_wants_are_live(self):
        # 3.2.102's निष्ठा and 6.4.59–61's lengthening of क्षि.
        for code in ("3.2.102", "6.4.59", "6.4.61"):
            self.assertTrue(REGISTRY.has(code), code)

    def test_and_what_the_new_sounds_then_meet_has_landed(self):
        # 8.4.2 अट्कुप्वाङ्नुम्व्यवायेऽपि is what turns the न्
        # this run makes into a ण् in आस्तीर्णम् and क्षीणः, and
        # it is codified — so a form this module only names can
        # be followed to the sound actually heard.
        self.assertTrue(REGISTRY.has("8.4.2"))
        self.assertTrue(REGISTRY.has("8.4.1"))


if __name__ == "__main__":
    unittest.main()
