# -*- coding: utf-8 -*-
"""
८.१.५१–७४ — the rest of the निघात, and the vocative that is not there.

Four movements, and the tests follow them: the constructions
that spare a verb (51–56), the words that spare it by standing
after it (57–66), the five sūtras that start taking accents away
again (67–71), and the three about a vocative counting as absent
(72–74).
"""

from __future__ import annotations

import unittest

from src.astadhyayi.nighata import THE_NIGHATA, Toneless
from src.astadhyayi.nighata_sesa import (
    CANADI_SIX,
    KASTHADI,
    PADAT_ENDS_AT,
    SESA_RUN,
    SESA_TABLE,
    in_the_sentence,
    provisions_for,
)
from src.astadhyayi.sources import REGISTRY
import src.astadhyayi.rules  # noqa: F401  (populates REGISTRY)


class TheConstructionsThatSpare(unittest.TestCase):
    """8.1.51–56."""

    def test_a_future_or_an_imperative_with_a_verb_of_motion(self):
        # आगच्छ देवदत्त, ग्रामं द्रक्ष्यसि; ग्रामं पश्य.
        wanted = {"lṛṭ": "8.1.51", "loṭ": "8.1.52"}
        for gana, code in wanted.items():
            got = in_the_sentence(gana=gana,
                                  joined="gatyartha-loṭ",
                                  position="samāna-kāraka")
            self.assertEqual(got.sutra, code, gana)
            self.assertTrue(got.refuses, gana)
            self.assertIn(THE_NIGHATA, got.blocked_by, gana)

    def test_and_only_two_of_the_six_karakas_count(self):
        # कर्तृकर्मणी एव अत्र कारकग्रहणेन गृह्येते, न करणादि
        # कारकान्तरम्.
        self.assertIn("न करणादि",
                      provisions_for("8.1.51")[0].why)

    def test_but_with_a_preverb_the_sparing_is_only_optional(self):
        # आगच्छ देवदत्त ग्रामं प्रविश, प्रविश.
        got = in_the_sentence(gana="loṭ", joined="gatyartha-loṭ",
                              position="sopasarga-anuttama")
        self.assertEqual(got.sutra, "8.1.53")
        self.assertTrue(got.optional)
        self.assertIn("8.1.52", got.blocked_by)

    def test_and_hanta_gets_the_same_treatment_for_the_same_reason(self):
        # हन्त प्रविश, प्रविश — while 8.1.30's हन्त is
        # compulsory, which the note says outright.
        got = in_the_sentence(gana="loṭ", joined="hanta",
                              position="sopasarga-anuttama")
        self.assertEqual(got.sutra, "8.1.54")
        self.assertTrue(got.optional)
        self.assertIn("नित्यम्", provisions_for("8.1.54")[0].why)
        self.assertTrue(REGISTRY.has("8.1.30"))

    def test_a_vocative_one_word_after_am_keeps_its_accent(self):
        # आम् पचसि देवदत्त३ — and it is 8.1.19 that is refused.
        got = in_the_sentence(gana="āmantrita", joined="ām",
                              position="ekāntara", sense="anantika")
        self.assertEqual(got.sutra, "8.1.55")
        self.assertIn("8.1.19", got.blocked_by)

    def test_and_in_the_veda_a_following_particle_spares_the_verb(self):
        # गवां गोत्रम् उदसृजो यद् अङ्गिरः.
        got = in_the_sentence(gana="tiṅ", before="yat-hi-tu-para",
                              chandasi=True)
        self.assertEqual(got.sutra, "8.1.56")
        self.assertNotEqual(
            in_the_sentence(gana="tiṅ",
                            before="yat-hi-tu-para").sutra,
            "8.1.56")

    def test_and_the_vocative_of_the_sutra_before_is_not_carried_down(self):
        # आमन्त्रितम् इत्येतद् अस्वरितत्वान् न अनुवर्तते.
        self.assertIn("अस्वरितत्वान्",
                      provisions_for("8.1.56")[0].why)


class TheWordsThatSpareByFollowing(unittest.TestCase):
    """8.1.57–66, ten sūtras that turn on what comes after."""

    def test_six_kinds_of_word_spare_a_verb_they_follow(self):
        # चन, चित्, इव, गोत्रादि, a taddhita, an आम्रेडित.
        self.assertEqual(len(CANADI_SIX), 6)
        got = in_the_sentence(
            gana="tiṅ", after="a-gati",
            before="cana-cid-iva-gotrādi-taddhita-āmreḍita")
        self.assertEqual(got.sutra, "8.1.57")
        self.assertTrue(got.refuses)

    def test_and_the_gotradi_here_are_read_back_into_8_1_27(self):
        # इह अपि गोत्रादयः कुत्सनाभीक्ष्ण्ययोर् एव गृह्यन्ते.
        why = provisions_for("8.1.57")[0].why
        self.assertIn("कुत्सनाभीक्ष्ण्ययोर्", why)
        self.assertTrue(REGISTRY.has("8.1.27"))

    def test_the_cadi_here_is_narrowed_by_pointing_at_an_earlier_sutra(self):
        # चादयो न चवाहाहैवयुक्ते इत्यत्र ये निर्दिष्टाः — 8.1.24's
        # five and not the whole class of 1.4.57.
        why = provisions_for("8.1.58")[0].why
        self.assertIn("1.4.57", why)
        self.assertTrue(REGISTRY.has("1.4.57"))
        self.assertTrue(REGISTRY.has("8.1.24"))

    def test_six_sutras_spare_only_the_first_of_two_verbs(self):
        # च and वा, ह of a breach of custom, अह of assignment,
        # the elided च or अह, and any elided चादि.
        wanted = {("ca", ""): "8.1.59",
                  ("ha", "kṣiyā"): "8.1.60",
                  ("aha", "viniyoga"): "8.1.61",
                  ("ca-lopa", "avadhāraṇa"): "8.1.62",
                  ("cādi-lopa", ""): "8.1.63"}
        for (particle, sense), code in wanted.items():
            got = in_the_sentence(gana="prathamā-tiṅ",
                                  joined=particle, sense=sense)
            self.assertEqual(got.sutra, code, particle)

    def test_and_saying_prathama_is_what_keeps_the_second_out(self):
        # प्रथमाग्रहणं द्वितीयादेस् तिङन्तस्य मा भूद् इति.
        self.assertIn("द्वितीयादेस्",
                      provisions_for("8.1.59")[0].why)

    def test_two_of_them_are_vedic_and_optional(self):
        # वै and वाव; एक and अन्य.
        for particle, code in (("vai", "8.1.64"),
                               ("eka", "8.1.65")):
            got = in_the_sentence(gana="prathamā-tiṅ",
                                  joined=particle, chandasi=True)
            self.assertEqual(got.sutra, code, particle)
            self.assertTrue(got.optional, particle)

    def test_and_only_one_rule_of_the_whole_pada_says_always(self):
        # यद्वृत्तान्नित्यम् — यो भुङ्क्ते, यं भोजयति.
        got = in_the_sentence(gana="tiṅ", after="yadvṛtta")
        self.assertEqual(got.sutra, "8.1.66")
        self.assertTrue(got.refuses)
        self.assertFalse(got.optional)
        self.assertFalse(
            [row for row in SESA_TABLE
             if row.sutra == "8.1.66" and (row.sense or row.chandasi)])

    def test_and_yadvrtta_is_read_more_widely_than_kimvrtta_was(self):
        # इह वृत्तग्रहणेन तद्विभक्त्यन्तं प्रतीयात् डतरडतमौ च
        # प्रत्ययौ इत्येतद् न आश्रीयते — 8.1.48 was confined and
        # this is not.
        self.assertIn("न आश्रीयते", provisions_for("8.1.66")[0].why)
        self.assertTrue(REGISTRY.has("8.1.48"))


class WhereThePadaTurnsRound(unittest.TestCase):
    """8.1.67–71, five sūtras that take an accent away."""

    def test_what_is_praised_after_a_word_of_praise_is_toneless(self):
        # काष्ठाध्यापकः — a teacher and a half.
        got = in_the_sentence(gana="pūjita",
                              after="pūjana-kāṣṭhādi")
        self.assertEqual(got.sutra, "8.1.67")
        self.assertEqual(got.does, "anudātta")
        self.assertEqual(len(KASTHADI), 9)
        self.assertEqual(KASTHADI[0], "kāṣṭha")

    def test_and_the_verb_after_those_with_its_preverb_too(self):
        # यत् काष्ठं प्रपचति — 8.1.30's यत् had spared it, and
        # this puts the निघात back.
        got = in_the_sentence(gana="tiṅ",
                              after="pūjana-kāṣṭhādi",
                              position="sagati")
        self.assertEqual(got.sutra, "8.1.68")
        self.assertEqual(got.does, "anudātta")
        self.assertIn("8.1.30", got.blocked_by)
        self.assertIn("गतिर् अपि निहन्यते",
                      provisions_for("8.1.68")[0].why)

    def test_and_a_verb_before_a_noun_of_contempt(self):
        # पचति पूति; पचति शोभनम् keeps its accent.
        got = in_the_sentence(gana="tiṅ",
                              before="sup-kutsana-a-gotrādi",
                              position="sagati")
        self.assertEqual(got.sutra, "8.1.69")
        keeps = provisions_for("8.1.69")[0].keeps_out
        for form in ("शोभनम्", "क्लिश्नाति", "गोत्रम्"):
            self.assertIn(form, keeps, form)

    def test_and_that_is_where_8_1_17_stops(self):
        # पदाद् इति निवृत्तम् — the heading ends at 8.1.68, so
        # this rule needs nothing standing in front.
        self.assertEqual(PADAT_ENDS_AT, "8.1.68")
        self.assertIn("पदाद् इति निवृत्तम्",
                      provisions_for("8.1.69")[0].why)

    def test_a_gati_before_another_gati_or_an_accented_verb(self):
        # अभ्युद्धरति; यत् प्रपचति.
        self.assertEqual(
            in_the_sentence(gana="gati", before="gati").sutra,
            "8.1.70")
        self.assertEqual(
            in_the_sentence(gana="gati",
                            before="udāttavat-tiṅ").sutra,
            "8.1.71")

    def test_and_saying_tin_measures_how_much_carries_the_accent(self):
        # तिङ्ग्रहणम् उदात्तवतः परिमाणार्थम् — without it
        # यत् प्रकरोति, accented on the affix, would fall out.
        self.assertIn("परिमाणार्थम्",
                      provisions_for("8.1.71")[0].why)


class TheVocativeThatIsNotThere(unittest.TestCase):
    """8.1.72–74, and what a word counting as absent buys."""

    def test_a_leading_vocative_counts_as_absent(self):
        # देवदत्त यज्ञदत्त — the second has nothing in front.
        got = in_the_sentence(gana="āmantrita", position="pūrva")
        self.assertEqual(got.sutra, "8.1.72")
        self.assertEqual(got.does, "avidyamānavat")

    def test_and_three_things_then_do_not_happen(self):
        # आमन्त्रिततिङ्निघातयुष्मदस्मदादेशाभावाः — 8.1.19's
        # निघात, 8.1.28's, and the enclitics of 8.1.20-23.
        why = provisions_for("8.1.72")[0].why
        self.assertIn("8.1.19", why)
        self.assertIn("8.1.28", why)
        self.assertIn("8.1.20", why)

    def test_but_an_agreeing_vocative_after_it_puts_it_back(self):
        # अग्ने गृहपते — the first is there, so the second goes
        # toneless by 8.1.19 after all.
        got = in_the_sentence(
            gana="āmantrita-sāmānyavacana",
            before="āmantrita-samānādhikaraṇa")
        self.assertEqual(got.sutra, "8.1.73")
        self.assertTrue(got.refuses)
        self.assertIn("8.1.72", got.blocked_by)
        self.assertIn("विद्यमानवद् एव",
                      provisions_for("8.1.73")[0].why)

    def test_and_a_plural_makes_that_optional_and_closes_the_pada(self):
        # देवाः शरण्याः, either way.
        got = in_the_sentence(
            gana="āmantrita-bahuvacana",
            before="āmantrita-viśeṣavacana")
        self.assertEqual(got.sutra, "8.1.74")
        self.assertTrue(got.optional)
        self.assertIn("8.1.73", got.blocked_by)
        self.assertEqual(SESA_RUN[1], "8.1.74")


class NothingHappensByDefault(unittest.TestCase):
    """A word none of these rules reaches is left as it was."""

    def test_an_unnamed_word_reaches_nothing(self):
        got = in_the_sentence(gana="subanta")
        self.assertEqual(got.sutra, "")
        self.assertEqual(got.does, "")
        self.assertIn("8.1.16-50", got.why)

    def test_and_the_answer_is_the_same_one_the_earlier_half_gives(self):
        # The two runs settle one question between them, so the
        # answer type is asked of the first module rather than
        # written twice.
        self.assertIsInstance(in_the_sentence(gana="tiṅ"), Toneless)


class Registration(unittest.TestCase):
    """Every row reaches the registry with real notes."""

    def test_the_run_closes_the_pada(self):
        self.assertEqual(SESA_RUN, ("8.1.51", "8.1.74"))
        codes = [row.sutra for row in SESA_TABLE]
        self.assertEqual(
            codes, ["8.1.%d" % n for n in range(51, 75)])

    def test_every_sutra_is_registered_with_real_notes(self):
        for row in SESA_TABLE:
            self.assertTrue(REGISTRY.has(row.sutra), row.sutra)
            notes = REGISTRY.get(row.sutra).notes
            self.assertGreater(len(notes), 100, row.sutra)
            self.assertIn("SETTLED", notes, row.sutra)

    def test_and_the_whole_pada_is_codified_with_no_gap(self):
        for n in range(1, 75):
            self.assertTrue(REGISTRY.has("8.1.%d" % n), n)


class WhatIsNotCodifiedYet(unittest.TestCase):
    """
    The debts, written as the exact shortfall.

    Each fails the moment the thing it names lands, and must then
    be rewritten to state the live dependency instead.
    """

    def test_what_this_run_appeals_to_backwards_is_live(self):
        # 6.1.198's vocative accent, which 8.1.55 keeps; 1.4.57's
        # चादि, which 8.1.58 narrows; and 8.2.104's प्लुत, which
        # 8.1.60's examples carry.
        for code in ("6.1.198", "1.4.57"):
            self.assertTrue(REGISTRY.has(code), code)

    def test_and_the_pluta_one_of_its_examples_needs_has_landed(self):
        # 8.2.104 क्षियाऽऽशीःप्रैषेषु gives स्वयं ह रथेन याति३
        # its प्लुत, and 8.1.60 gives the same verb its accent.
        # Both are codified, so one form can be asked of two
        # pādas at once.
        self.assertTrue(REGISTRY.has("8.2.104"))
        self.assertTrue(REGISTRY.has("8.1.60"))

    def test_and_the_rest_of_the_adhyaya_has_been_read_too(self):
        # Written as a debt four times over, each version naming
        # what stood next. Nothing stands next any more: 8.2.4,
        # 8.2.108, 8.3.1 and 8.4.68 are all codified, and with
        # 8.4.68 so is the whole work.
        for code in ("8.2.4", "8.2.108", "8.3.1", "8.4.68"):
            self.assertTrue(REGISTRY.has(code), code)


if __name__ == "__main__":
    unittest.main()
