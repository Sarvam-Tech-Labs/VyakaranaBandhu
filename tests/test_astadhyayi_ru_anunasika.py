# -*- coding: utf-8 -*-
"""
८.३.१–३३ — the रुँ, the nasal before it, and the anusvāra.

Thirty-two rows and one sūtra missing from them: 8.3.15
खरवसानयोर्विसर्जनीयः was codified apart long before the pāda was
read. The class that matters most is the one about the three
teachers, where naming a teacher makes a rule an option twice
and an honour once — and the vṛtti says which is which.
"""

from __future__ import annotations

import unittest

from src.astadhyayi.ru_anunasika import (
    ANUNASIKA_FROM,
    CODIFIED_APART,
    PUJARTHAM,
    RU_RUN,
    RU_TABLE,
    SAMHITA,
    TEACHERS,
    in_samhita,
    provisions_for,
)
from src.astadhyayi.sources import REGISTRY
import src.astadhyayi.rules  # noqa: F401  (populates REGISTRY)


class TheHeadingsAboveThePada(unittest.TestCase):
    """8.3.2, and the one carried in from the pāda before."""

    def test_the_whole_pada_stands_under_samhita(self):
        # 8.2.108's संहितायाम् runs to the end of the adhyāya,
        # and 8.3.1's own vṛtti says so in its first words.
        self.assertEqual(SAMHITA, "8.2.108")
        self.assertTrue(REGISTRY.has(SAMHITA))
        self.assertIn("संहितायाम् इति वर्तते",
                      provisions_for("8.3.1")[0].why)

    def test_and_the_pada_opens_a_heading_of_its_own_at_once(self):
        # अत्रानुनासिकः पूर्वस्य तु वा — whatever a रुँ replaces,
        # the sound before it may go nasal.
        self.assertEqual(ANUNASIKA_FROM, "8.3.2")
        row = provisions_for("8.3.2")[0]
        self.assertTrue(row.heading)
        self.assertTrue(row.optional)
        self.assertIn("अधिकृतं वेदितव्यम्", row.why)

    def test_but_the_heading_answers_nothing(self):
        self.assertNotEqual(
            in_samhita("sam", before="suṭ").sutra, "8.3.2")

    def test_and_two_sutras_divide_that_option_between_them(self):
        # 8.3.3 makes the nasal compulsory before an अट्, and
        # 8.3.4 gives the half where it does not come an
        # anusvāra instead.
        self.assertEqual(
            in_samhita(gana="ā-anta-ru-pūrva", before="aṭ").does,
            "anunāsika")
        self.assertEqual(
            in_samhita(gana="a-anunāsika-ru-pūrva").does,
            "anusvāra")


class WhereTheRuComes(unittest.TestCase):
    """8.3.1 and 8.3.5–12."""

    def test_four_words_take_it_by_name(self):
        wanted = {("sam", "suṭ"): "8.3.5",
                  ("pum", "khay-am-para"): "8.3.6",
                  ("kān", "āmreḍita"): "8.3.12"}
        for (word, after), code in wanted.items():
            got = in_samhita(word, before=after)
            self.assertEqual(got.sutra, code, word)
            self.assertEqual(got.does, "ru", word)

    def test_and_any_n_final_word_before_a_chav(self):
        # भवांश्छादयति — the rule every भवान् before a stop
        # passes through, and प्रशान् is the one exception.
        got = in_samhita(gana="na-anta", before="chav-am-para")
        self.assertEqual(got.sutra, "8.3.7")
        self.assertIn("प्रशान्",
                      provisions_for("8.3.7")[0].keeps_out)

    def test_but_in_the_rcs_it_goes_both_ways(self):
        # तस्मिंस्त्वा दधाति, तस्मिन्त्वा दधाति.
        got = in_samhita(gana="na-anta", before="chav-am-para",
                         chandasi=True)
        self.assertEqual(got.sutra, "8.3.8")
        self.assertTrue(got.optional)
        self.assertIn("8.3.7", got.blocked_by)

    def test_and_one_vedic_rule_wants_the_same_metrical_quarter(self):
        # दीर्घादटि समानपादे — a condition nothing else in the
        # work states.
        got = in_samhita(gana="dīrgha-para-na-anta",
                         before="aṭ-samāna-pāda", chandasi=True)
        self.assertEqual(got.sutra, "8.3.9")
        self.assertIn("ऋक्पाद", provisions_for("8.3.9")[0].why)

    def test_and_the_kaskadi_reading_saves_one_word_a_second_rule(self):
        # कांस्कान् is in 8.3.48's list, so 8.3.37's
        # जिह्वामूलीय does not come and the स् is heard.
        why = provisions_for("8.3.12")[0].why
        self.assertIn("कस्कादि list", why)
        self.assertTrue(REGISTRY.has("8.3.48"))


class TwoSoundsThatSimplyGo(unittest.TestCase):
    """8.3.13–14, where the heading is quietly set aside."""

    def test_a_dha_before_a_dha_and_an_r_before_an_r(self):
        # लीढम्, मीढम्; नीरक्तम्, अग्नी रथः.
        for gana, code in (("ḍha", "8.3.13"), ("repha", "8.3.14")):
            got = in_samhita(gana=gana, before=gana)
            self.assertEqual(got.sutra, code, gana)
            self.assertEqual(got.does, "lopa", gana)

    def test_and_both_reach_inside_a_word_against_the_heading(self):
        # 8.1.16's पदस्य is still running, and neither rule can
        # obey it — the vṛtti says so of each in turn.
        self.assertIn("अपदान्तस्य",
                      provisions_for("8.3.13")[0].why)
        self.assertIn("अपदान्तस्य",
                      provisions_for("8.3.14")[0].why)
        self.assertTrue(REGISTRY.has("8.1.16"))


class ThreeTeachersAndOneSound(unittest.TestCase):
    """8.3.17–22, four rules about one य्."""

    def test_the_ru_becomes_ya_before_a_vowel(self):
        # भो अत्र; ब्राह्मणा ददति.
        got = in_samhita(gana="bho-bhago-agho-a-pūrva-ru",
                         before="aś")
        self.assertEqual(got.sutra, "8.3.17")
        self.assertEqual(got.does, "ya")

    def test_and_each_teacher_answers_only_a_reader_who_asks(self):
        self.assertEqual(len(TEACHERS), 3)
        wanted = {"śākaṭāyana": ("8.3.18", "laghu-ya"),
                  "śākalya": ("8.3.19", "lopa")}
        for teacher, (code, does) in wanted.items():
            got = in_samhita(gana="ya-va-pada-anta", before="aś",
                             view=teacher)
            self.assertEqual(got.sutra, code, teacher)
            self.assertEqual(got.does, does, teacher)
            self.assertTrue(got.optional, teacher)
            self.assertEqual(got.view, teacher, teacher)
        # and without a teacher named, the grammar's own rule
        self.assertEqual(
            in_samhita(gana="ya-va-pada-anta", before="aś").sutra,
            "")

    def test_but_the_third_naming_is_an_honour_and_not_a_dissent(self):
        # नित्यार्थोऽयम् आरम्भः। गार्ग्यग्रहणं पूजार्थम् — the
        # rule makes the loss COMPULSORY where 8.3.19 left it
        # optional, which is the opposite of what the other two
        # namings do.
        got = in_samhita(gana="o-para-ya", before="aś",
                         view="gārgya")
        self.assertEqual(got.sutra, "8.3.20")
        self.assertFalse(got.optional)
        self.assertIn("पूजार्थम्", PUJARTHAM)
        self.assertIn(PUJARTHAM, provisions_for("8.3.20")[0].why)

    def test_and_the_same_thing_was_said_of_a_teacher_in_adhyaya_7(self):
        # 7.3.99's गार्ग्यगालवयोर्ग्रहणं पूजार्थम्, which is
        # codified and which this note points back to.
        self.assertIn("7.3.99", provisions_for("8.3.20")[0].why)
        self.assertTrue(REGISTRY.has("7.3.99"))

    def test_and_before_a_consonant_every_teacher_agrees(self):
        # हलि सर्वेषाम् — भो हसति, वृक्षा हसन्ति.
        got = in_samhita(gana="bho-bhago-agho-a-pūrva-ya",
                         before="hal")
        self.assertEqual(got.sutra, "8.3.22")
        self.assertIn("शाकटायनस्य",
                      provisions_for("8.3.22")[0].why)


class TheAnusvaraAndTheAugments(unittest.TestCase):
    """8.3.23–33."""

    def test_a_word_final_m_becomes_an_anusvara(self):
        # कुण्डं हसति — and both conditions are tested.
        got = in_samhita(gana="ma-anta", before="hal")
        self.assertEqual(got.sutra, "8.3.23")
        keeps = provisions_for("8.3.23")[0].keeps_out
        self.assertIn("त्वमत्र", keeps)
        self.assertIn("गम्यते", keeps)

    def test_and_one_inside_a_word_before_a_jhal(self):
        # पयांसि, यशांसि — with 7.1.72's नुम्, which is codified.
        got = in_samhita(gana="na-ma-a-pada-anta", before="jhal")
        self.assertEqual(got.sutra, "8.3.24")
        self.assertIn("7.1.72", provisions_for("8.3.24")[0].why)
        self.assertTrue(REGISTRY.has("7.1.72"))

    def test_but_sam_keeps_its_m_before_one_root(self):
        # सम्राट् — and prescribing म् for म् is idle except as
        # a way of keeping the anusvāra out.
        got = in_samhita("sam", before="rāj-kvip")
        self.assertEqual(got.sutra, "8.3.25")
        self.assertIn("8.3.23", got.blocked_by)
        self.assertIn("अनुस्वारनिवृत्त्यर्थम्",
                      provisions_for("8.3.25")[0].why)

    def test_and_before_h_it_takes_the_shape_of_what_follows_it(self):
        # किम् ह्मलयति; किन् ह्नुते.
        self.assertEqual(
            in_samhita(gana="ma-anta", before="ha-ma-para").does,
            "ma")
        self.assertEqual(
            in_samhita(gana="ma-anta", before="ha-na-para").does,
            "na")

    def test_five_augments_are_given_and_each_names_its_side(self):
        # 8.3.28 at the end of the first word, 8.3.29 and
        # 8.3.30 at the head of the second, 8.3.31 at the end
        # again, 8.3.32 in front of the vowel.
        wanted = {"8.3.28": "पूर्वान्तकरणम्",
                  "8.3.29": "परादिकरणम्",
                  "8.3.31": "पूर्वान्तकरणं"}
        for code, fragment in wanted.items():
            self.assertIn(fragment, provisions_for(code)[0].why,
                          code)

    def test_and_one_of_them_makes_a_later_rule_unreachable(self):
        # धुटश् चर्त्वस्य च असिद्धत्वाद् — भवान्त्साये keeps its
        # न् where भवांश्छादयति does not.
        self.assertIn("रुत्वं न भवति",
                      provisions_for("8.3.30")[0].why)

    def test_and_the_last_one_is_the_only_compulsory_augment(self):
        # ङमुण्नित्यम् — प्रत्यङ्ङास्ते, वण्णास्ते.
        got = in_samhita(gana="hrasva-para-ṅam-anta", before="ac")
        self.assertEqual(got.sutra, "8.3.32")
        self.assertFalse(got.optional)
        for code in ("8.3.28", "8.3.29", "8.3.30", "8.3.31"):
            self.assertTrue(provisions_for(code)[0].optional, code)


class NothingHappensByDefault(unittest.TestCase):
    """Two sounds none of these rules reaches stand as they are."""

    def test_an_unnamed_junction_reaches_nothing(self):
        got = in_samhita("vṛkṣa", before="hal")
        self.assertEqual(got.sutra, "")
        self.assertEqual(got.does, "")


class Registration(unittest.TestCase):
    """Every row reaches the registry with real notes."""

    def test_the_table_holds_the_run_minus_what_was_codified_apart(self):
        self.assertEqual(RU_RUN, ("8.3.1", "8.3.33"))
        self.assertEqual(CODIFIED_APART, ("8.3.15",))
        codes = [row.sutra for row in RU_TABLE]
        expected = ["8.3.%d" % n for n in range(1, 34)
                    if "8.3.%d" % n not in CODIFIED_APART]
        self.assertEqual(codes, expected)
        self.assertTrue(REGISTRY.has("8.3.15"))

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

    def test_everything_this_run_appeals_to_is_live(self):
        # 8.2.108's संहितायाम्, 8.1.16's पदस्य, 8.3.15's
        # visarga, 7.1.72's नुम् and 7.3.99's honoured teachers.
        for code in ("8.2.108", "8.1.16", "8.3.15", "7.1.72",
                     "7.3.99"):
            self.assertTrue(REGISTRY.has(code), code)


if __name__ == "__main__":
    unittest.main()
