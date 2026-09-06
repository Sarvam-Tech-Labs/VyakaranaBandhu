# -*- coding: utf-8 -*-
"""
८.२.८२–१०८ — the प्लुत, and the three accents it can carry.

One heading of three words, and twenty-six rules under it. Three
of those change the heading's third word to अनुदात्त and three
more to स्वरित, so the tests keep the accent in view throughout:
it is the one thing the run varies without ever saying so twice.
"""

from __future__ import annotations

import unittest

from src.astadhyayi.pluta import (
    ADHIKARA_TO,
    ANUDATTA_THREE,
    BRUHI_FIVE,
    PLUTA_RUN,
    PLUTA_TABLE,
    SAMHITA_TO,
    SVARITA_THREE,
    provisions_for,
    the_pluta,
)
from src.astadhyayi.sources import REGISTRY
import src.astadhyayi.rules  # noqa: F401  (populates REGISTRY)


class TheHeadingOfThreeWords(unittest.TestCase):
    """8.2.82, and what every rule under it borrows."""

    def test_the_heading_runs_to_the_end_of_the_pada(self):
        self.assertEqual(ADHIKARA_TO, "8.2.108")
        self.assertEqual(PLUTA_RUN, ("8.2.82", "8.2.108"))
        self.assertIn("आ पादपरिसमाप्तेः",
                      provisions_for("8.2.82")[0].why)

    def test_and_it_carries_three_words_and_not_one(self):
        # वाक्यस्य टेः, प्लुत, and उदात्त.
        why = provisions_for("8.2.82")[0].why
        self.assertIn("एतत् त्रयम्", why)

    def test_but_the_heading_itself_answers_nothing(self):
        headings = [row.sutra for row in PLUTA_TABLE if row.heading]
        self.assertEqual(headings, ["8.2.82"])
        self.assertNotEqual(
            the_pluta(sense="pratyabhivāda").sutra, "8.2.82")

    def test_and_the_accent_it_supplies_is_what_a_rule_answers_with(self):
        # A rule that names no accent takes the heading's उदात्त.
        got = the_pluta(sense="pratyabhivāda")
        self.assertEqual(got.sutra, "8.2.83")
        self.assertEqual(got.accent, "udātta")
        self.assertEqual(provisions_for("8.2.83")[0].accent, "")


class WhereTheLengtheningComes(unittest.TestCase):
    """8.2.83–99, and what each of them wants."""

    def test_a_greeting_a_call_and_an_opening(self):
        wanted = {"pratyabhivāda": "8.2.83",
                  "dūrād-dhūta": "8.2.84",
                  "abhyādāna": "8.2.87"}
        for sense, code in wanted.items():
            if code == "8.2.87":
                got = the_pluta("om", sense=sense)
            else:
                got = the_pluta(sense=sense)
            self.assertEqual(got.sutra, code, sense)
            self.assertEqual(got.does, "pluta", sense)

    def test_and_distance_is_settled_by_the_calling_not_measured(self):
        # दूरं यद्यपि अपेक्षाभेदाद् अनवस्थितम्, तथापि हूतापेक्षम्.
        self.assertIn("हूतापेक्षम्",
                      provisions_for("8.2.84")[0].why)

    def test_but_hai_and_he_take_it_off_the_sentences_end(self):
        # है३ देवदत्त; देवदत्त हे३.
        for word in ("hai", "he"):
            got = the_pluta(word, sense="dūrād-dhūta",
                            position="anantya")
            self.assertEqual(got.sutra, "8.2.85", word)
            self.assertIn("8.2.84", got.blocked_by, word)

    def test_and_the_two_are_named_twice_over_for_a_reason(self):
        # पुनर् हैहयोर् ग्रहणम् अनन्त्ययोर् अपि यथा स्यात्.
        self.assertIn("अनन्त्ययोर् अपि",
                      provisions_for("8.2.85")[0].why)

    def test_a_named_school_makes_one_rule_an_option(self):
        # प्राचाम् — and the rule adds no lengthening but says
        # which syllable carries one already due.
        got = the_pluta(gana="guru-an-ṛt", position="anantya",
                        view="prācām")
        self.assertEqual(got.sutra, "8.2.86")
        self.assertTrue(got.optional)
        self.assertEqual(got.view, "prācām")
        self.assertIn("स्थानिविशेष",
                      provisions_for("8.2.86")[0].why)

    def test_five_words_take_it_on_their_first_syllable(self):
        # अनुब्रू३हि, प्रे३ष्य, श्रौ३षट्, वौ३षट्, आ३वह.
        self.assertEqual(len(BRUHI_FIVE), 5)
        for word in BRUHI_FIVE:
            got = the_pluta(word, sense="yajña-karman",
                            position="ādi")
            self.assertEqual(got.sutra, "8.2.91", word)

    def test_and_one_word_takes_two_lengthenings_at_once(self):
        # आ३श्रा३वय — which happens nowhere else in the work.
        got = the_pluta(sense="agnīt-preṣaṇa",
                        position="ādi-para")
        self.assertEqual(got.sutra, "8.2.92")
        self.assertIn("nowhere else",
                      provisions_for("8.2.92")[0].why)

    def test_the_doubling_of_pada_one_meets_the_lengthening_here(self):
        # चौरचौ३र — 8.1.8 doubles the word and 8.2.95 lengthens
        # the copy. Both codified.
        got = the_pluta(gana="āmreḍita", sense="bhartsana")
        self.assertEqual(got.sutra, "8.2.95")
        self.assertIn("8.1.8", provisions_for("8.2.95")[0].why)
        self.assertTrue(REGISTRY.has("8.1.8"))

    def test_and_a_verb_left_hanging_takes_it_too(self):
        # अङ्ग कू३ज — and अङ्ग पच expects nothing.
        got = the_pluta("aṅga", gana="tiṅ", sense="bhartsana",
                        position="ākāṅkṣa")
        self.assertEqual(got.sutra, "8.2.96")
        self.assertIn("अङ्ग पच",
                      provisions_for("8.2.96")[0].keeps_out)

    def test_deliberation_lengthens_each_and_then_only_the_first(self):
        # होतव्यं दीक्षितस्य गृहा३इ in the Veda; अहिर् नु३
        # रज्जुर् नु in the spoken language.
        each = the_pluta(sense="vicāryamāṇa")
        self.assertEqual(each.sutra, "8.2.97")
        first = the_pluta(sense="vicāryamāṇa", position="pūrva")
        self.assertEqual(first.sutra, "8.2.98")
        self.assertIn("8.2.97", first.blocked_by)

    def test_and_the_second_of_those_confines_the_first_to_the_veda(self):
        # इह भाषाग्रहणात् पूर्वयोगश् छन्दसि विज्ञायते.
        self.assertIn("भाषाग्रहणात्",
                      provisions_for("8.2.98")[0].why)


class TheThreeAccents(unittest.TestCase):
    """8.2.100–105, where the heading's third word changes."""

    def test_three_sutras_make_it_anudatta(self):
        self.assertEqual(len(ANUDATTA_THREE), 3)
        for code in ANUDATTA_THREE:
            self.assertEqual(provisions_for(code)[0].accent,
                             "anudātta", code)

    def test_and_three_more_make_it_svarita(self):
        self.assertEqual(len(SVARITA_THREE), 3)
        for code in SVARITA_THREE:
            self.assertEqual(provisions_for(code)[0].accent,
                             "svarita", code)

    def test_and_every_other_rule_takes_the_headings_udatta(self):
        named = set(ANUDATTA_THREE) | set(SVARITA_THREE) | {"8.2.82"}
        for row in PLUTA_TABLE:
            if row.sutra in named:
                continue
            self.assertEqual(row.accent, "", row.sutra)
            self.assertEqual(the_pluta_accent(row), "udātta",
                             row.sutra)

    def test_one_vedic_line_takes_two_different_accents(self):
        # अधः स्विद् आसी३द् by 8.2.97, उपरि स्विद् आसी३त् by
        # 8.2.102 — one high and one low in the same sentence.
        low = the_pluta("upari-svid-āsīt")
        self.assertEqual(low.sutra, "8.2.102")
        self.assertEqual(low.accent, "anudātta")
        self.assertEqual(the_pluta(sense="vicāryamāṇa").accent,
                         "udātta")
        self.assertIn("8.2.97", provisions_for("8.2.102")[0].why)

    def test_and_one_sentence_takes_two_at_once(self):
        # अगम३ः पूर्वा३न् ग्रामा३न् अग्निभूता३इ — every word
        # स्वरित by 8.2.105, the last अनुदात्त by 8.2.100.
        self.assertEqual(
            the_pluta(sense="praśna", position="anantya").accent,
            "svarita")
        self.assertEqual(
            the_pluta(sense="praśna-anta").accent, "anudātta")

    def test_and_the_rule_pada_one_needed_is_here(self):
        # 8.1.60's स्वयं ह रथेन याति३ keeps its accent by that
        # sūtra and takes its प्लुत by this one. Both codified.
        got = the_pluta(gana="tiṅ", sense="kṣiyā",
                        position="ākāṅkṣa")
        self.assertEqual(got.sutra, "8.2.104")
        self.assertIn("8.1.60", provisions_for("8.2.104")[0].why)
        self.assertTrue(REGISTRY.has("8.1.60"))


def the_pluta_accent(row):
    """What a row answers with, once the heading has supplied."""
    return row.accent or "udātta"


class WhichVowelCarriesIt(unittest.TestCase):
    """8.2.106–108, where the lengthening goes inside a vowel."""

    def test_a_diphthong_lengthens_its_second_half_only(self):
        # ऐ३तिकायन, औ३पमन्यव.
        got = the_pluta(gana="aic")
        self.assertEqual(got.sutra, "8.2.106")
        self.assertEqual(got.does, "id-ut")

    def test_and_an_e_or_o_splits_in_two(self):
        # अग्ने gives अग्ना३इ and पटो gives पटा३उ.
        got = the_pluta(gana="ec-a-pragṛhya")
        self.assertEqual(got.sutra, "8.2.107")
        self.assertEqual(got.does, "ā-id-ut")

    def test_and_that_is_why_the_deliberating_sentences_look_odd(self):
        # गृहा३इ — the ए of the locative split by 8.2.107, which
        # 8.2.97's own note says.
        self.assertIn("8.2.107", provisions_for("8.2.97")[0].why)

    def test_and_before_a_vowel_those_become_semivowels(self):
        # अग्ना३याशा, पटा३वाशा.
        got = the_pluta(gana="id-ut", position="ac-para")
        self.assertEqual(got.sutra, "8.2.108")
        self.assertEqual(got.does, "ya-va")

    def test_and_the_last_sutra_opens_a_heading_of_its_own(self):
        # संहितायाम् runs to the end of the adhyāya, so no sūtra
        # of 8.3 or 8.4 has to say it.
        self.assertEqual(SAMHITA_TO, "8.4.68")
        self.assertIn("आध्यायपरिसमाप्तेर्",
                      provisions_for("8.2.108")[0].why)


class NothingHappensByDefault(unittest.TestCase):
    """A sentence none of these rules reaches keeps its length."""

    def test_an_unnamed_setting_reaches_nothing(self):
        got = the_pluta("devadatta")
        self.assertEqual(got.sutra, "")
        self.assertEqual(got.does, "")
        self.assertEqual(got.accent, "")


class Registration(unittest.TestCase):
    """Every row reaches the registry with real notes."""

    def test_the_run_closes_the_pada(self):
        codes = [row.sutra for row in PLUTA_TABLE]
        self.assertEqual(
            codes, ["8.2.%d" % n for n in range(82, 109)])

    def test_every_sutra_is_registered_with_real_notes(self):
        for row in PLUTA_TABLE:
            self.assertTrue(REGISTRY.has(row.sutra), row.sutra)
            notes = REGISTRY.get(row.sutra).notes
            self.assertGreater(len(notes), 100, row.sutra)
            self.assertIn("SETTLED", notes, row.sutra)

    def test_and_the_whole_pada_is_codified_with_no_gap(self):
        for n in range(1, 109):
            self.assertTrue(REGISTRY.has("8.2.%d" % n), n)


class WhatIsNotCodifiedYet(unittest.TestCase):
    """
    The debts, written as the exact shortfall.

    Each fails the moment the thing it names lands, and must then
    be rewritten to state the live dependency instead.
    """

    def test_what_this_run_appeals_to_backwards_is_live(self):
        # 1.2.27's three mātrās, 8.1.8's doubling and 8.1.60's
        # accent, all of which this run's examples need.
        for code in ("1.2.27", "8.1.8", "8.1.60"):
            self.assertTrue(REGISTRY.has(code), code)

    def test_and_the_heading_the_last_sutra_opens_is_whole_now(self):
        # संहितायाम् runs from 8.2.108 to 8.4.68, and every
        # sūtra it governs is codified — the whole of पाद ८.३
        # and पाद ८.४, which is where the work ends.
        self.assertTrue(REGISTRY.has("8.3.1"))
        self.assertTrue(REGISTRY.has(SAMHITA_TO))


if __name__ == "__main__":
    unittest.main()
