# -*- coding: utf-8 -*-
"""
८.४.४०–६८ — ष्टुत्व, the doubling, जश्त्व, and the last sūtra.

Twenty-eight rows and one sūtra missing from them: 8.4.55 खरि च
was codified apart. The last class is about 8.4.68 अ अ इति,
which closes the work by undoing something the work itself put
there in its first line.
"""

from __future__ import annotations

import unittest

from src.astadhyayi.stutva import (
    CODIFIED_APART,
    DOUBLING_REFUSED,
    NOT_YATHASAMKHYAM,
    STUTVA_RUN,
    STUTVA_TABLE,
    THE_LAST,
    at_the_junction,
    provisions_for,
)
from src.astadhyayi.sources import REGISTRY
import src.astadhyayi.rules  # noqa: F401  (populates REGISTRY)


class TheTwoAssimilations(unittest.TestCase):
    """8.4.40–44, and the four refusals that qualify them."""

    def test_a_s_or_a_dental_takes_the_class_it_meets(self):
        # तच्छिवः, रामश्च; वृक्षष्षण्डे.
        self.assertEqual(
            at_the_junction(gana="stu", before="ścu").does, "ścu")
        self.assertEqual(
            at_the_junction(gana="stu", before="ṣṭu").does, "ṣṭu")

    def test_and_the_pairs_are_not_matched_one_to_one(self):
        # स्तोःश्चुना इति यथासंख्यम् अत्र न इष्यते — said of the
        # first rule and again of the second.
        self.assertIn("यथासंख्यम्", NOT_YATHASAMKHYAM)
        self.assertIn(NOT_YATHASAMKHYAM,
                      provisions_for("8.4.40")[0].why)
        self.assertIn("संख्यातानुदेशाभावः",
                      provisions_for("8.4.41")[0].why)

    def test_and_three_refusals_qualify_them(self):
        wanted = {("stu", "pada-anta-ṭu", None): "8.4.42",
                  ("tu", None, "ṣa"): "8.4.43",
                  ("tu", "śa", None): "8.4.44"}
        for (gana, after, before), code in wanted.items():
            query = {"gana": gana}
            if after:
                query["after"] = after
            if before:
                query["before"] = before
            got = at_the_junction(**query)
            self.assertEqual(got.sutra, code, code)
            self.assertTrue(got.refuses, code)

    def test_and_the_kasika_thinks_one_exception_too_narrow(self):
        # अत्यल्पम् इदम् उच्यते — of the नाम् 8.4.42 excepts.
        self.assertIn("अत्यल्पम्", provisions_for("8.4.42")[0].why)


class TheDoublingAndThreeTeachers(unittest.TestCase):
    """8.4.46–52, where the grammar and the manuscripts part."""

    def test_two_rules_double_a_yar(self):
        # अर्क्कः, ब्रह्म्मा; दद्ध्यत्र.
        self.assertEqual(
            at_the_junction(gana="yar", after="ac-ra-ha").sutra,
            "8.4.46")
        self.assertEqual(
            at_the_junction(gana="yar", after="ac",
                            before="an-ac").sutra, "8.4.47")

    def test_and_three_teachers_refuse_it_in_three_measures(self):
        self.assertEqual(len(DOUBLING_REFUSED), 3)
        wanted = {"śākaṭāyana": ("8.4.50", "tri-prabhṛti", ""),
                  "śākalya": ("8.4.51", "", ""),
                  "ācārya": ("8.4.52", "", "dīrgha")}
        for teacher, (code, gana, after) in wanted.items():
            got = at_the_junction(gana=gana, after=after,
                                  view=teacher)
            self.assertEqual(got.sutra, code, teacher)
            self.assertTrue(got.refuses, teacher)
            self.assertEqual(got.view, teacher, teacher)

    def test_and_none_of_the_three_answers_without_being_asked(self):
        got = at_the_junction(gana="yar", after="ac-ra-ha")
        self.assertEqual(got.sutra, "8.4.46")
        self.assertFalse(got.refuses)

    def test_and_the_note_says_which_teacher_the_manuscripts_follow(self):
        # 8.4.51's four words are 8.4.46's own examples given
        # back without their doubling.
        self.assertIn("manuscripts in fact follow",
                      provisions_for("8.4.51")[0].why)

    def test_and_one_word_is_taken_out_of_the_doubling_by_a_sense(self):
        # पुत्रादिनी of abuse; पुत्त्रादिनी of plain fact.
        got = at_the_junction("putra", before="ādinī",
                              sense="ākrośa")
        self.assertEqual(got.sutra, "8.4.48")
        self.assertTrue(got.refuses)
        self.assertIn("8.4.47", got.blocked_by)


class TheVoicingAndTheUnvoicing(unittest.TestCase):
    """8.4.53–56, and the one sūtra codified apart."""

    def test_a_jhal_goes_voiced_before_a_jhas(self):
        # लब्धा, दोग्धा, बोद्धा — and 8.2.40 had already made
        # the second half aspirate.
        got = at_the_junction(gana="jhal", before="jhaś")
        self.assertEqual(got.sutra, "8.4.53")
        self.assertEqual(got.does, "jaś")
        self.assertIn("8.2.40", provisions_for("8.4.53")[0].why)
        self.assertTrue(REGISTRY.has("8.2.40"))

    def test_and_the_reduplication_goes_unvoiced(self):
        # चिखनिषति, बुभूषति, जिघत्सति.
        got = at_the_junction(gana="abhyāsa-jhal")
        self.assertEqual(got.sutra, "8.4.54")
        self.assertEqual(got.does, "car")

    def test_and_the_rule_between_them_is_codified_apart(self):
        # 8.4.55 खरि च, reached ahead long before the pāda was
        # read.
        self.assertEqual(CODIFIED_APART, ("8.4.55",))
        self.assertNotIn("8.4.55",
                         [row.sutra for row in STUTVA_TABLE])
        self.assertTrue(REGISTRY.has("8.4.55"))

    def test_and_at_a_pause_a_word_may_be_quoted_two_ways(self):
        # वाक् beside वाग्; दधिँ beside दधि.
        car = at_the_junction(gana="jhal", after="avasāna")
        self.assertEqual(car.sutra, "8.4.56")
        self.assertTrue(car.optional)
        nasal = at_the_junction(gana="aṇ-a-pragṛhya",
                                after="avasāna")
        self.assertEqual(nasal.sutra, "8.4.57")
        self.assertTrue(nasal.optional)


class TheAnusvaraAndTheBackwardRules(unittest.TestCase):
    """8.4.58–65."""

    def test_an_anusvara_takes_the_class_of_what_follows(self):
        # शङ्किता, उञ्छिता, कुण्डिता, नन्दिता, कम्पिता.
        got = at_the_junction(gana="anusvāra", before="yay")
        self.assertEqual(got.sutra, "8.4.58")
        self.assertEqual(got.does, "parasavarṇa")

    def test_but_a_word_final_one_only_optionally(self):
        got = at_the_junction(gana="anusvāra-pada-anta",
                              before="yay")
        self.assertEqual(got.sutra, "8.4.59")
        self.assertTrue(got.optional)
        self.assertIn("8.4.58", got.blocked_by)

    def test_and_two_rules_run_the_other_way_round(self):
        # उत्त्थाता and वाग्घसति — the sound takes the class of
        # what stands BEFORE, which is done nowhere else.
        backward = [row.sutra for row in STUTVA_TABLE
                    if row.does == "pūrvasavarṇa"]
        self.assertEqual(backward, ["8.4.61", "8.4.62"])
        self.assertIn("reverses the direction",
                      provisions_for("8.4.61")[0].why)

    def test_and_two_more_undo_what_the_doubling_just_made(self):
        # शय्या beside शय्य्या; प्रत्तम् with one त् or two.
        for gana, before, code in (
                ("yam", "yam", "8.4.64"),
                ("jhar", "jhar-savarṇa", "8.4.65")):
            got = at_the_junction(gana=gana, after="hal",
                                  before=before)
            self.assertEqual(got.sutra, code, gana)
            self.assertEqual(got.does, "lopa", gana)
            self.assertTrue(got.optional, gana)


class TheAccentAndTheLastSutra(unittest.TestCase):
    """8.4.66–68, where the work closes."""

    def test_an_anudatta_after_an_udatta_becomes_svarita(self):
        # गार्ग्यः, पचति.
        got = at_the_junction(gana="anudātta", after="udātta")
        self.assertEqual(got.sutra, "8.4.66")
        self.assertEqual(got.does, "svarita")

    def test_and_that_svarita_is_invisible_to_a_rule_of_adhyaya_6(self):
        # अस्य स्वरितस्य असिद्धत्वाद् 6.1.158 न प्रवर्तते — so
        # both accents are heard, and that rule is codified.
        self.assertIn("6.1.158", provisions_for("8.4.66")[0].why)
        self.assertTrue(REGISTRY.has("6.1.158"))

    def test_and_three_teachers_are_named_to_be_excluded(self):
        # अगार्ग्यकाश्यपगालवानाम् — the only place in the work
        # where a naming excludes rather than follows.
        got = at_the_junction(gana="anudātta", after="udātta",
                              before="udātta-svarita-udaya",
                              view="a-gārgya-kāśyapa-gālava")
        self.assertEqual(got.sutra, "8.4.67")
        self.assertTrue(got.refuses)
        self.assertIn("8.4.66", got.blocked_by)
        self.assertIn("named to be excluded",
                      provisions_for("8.4.67")[0].why)

    def test_the_last_sutra_of_the_work_closes_an_open_vowel(self):
        # वृक्षः, प्लक्षः.
        self.assertEqual(THE_LAST, "8.4.68")
        got = at_the_junction("a")
        self.assertEqual(got.sutra, "8.4.68")
        self.assertEqual(got.does, "saṃvṛta")

    def test_and_what_it_undoes_the_work_itself_put_there(self):
        # इह शास्त्रे कार्यार्थम् अकारो विवृतः प्रतिज्ञातः — the
        # अ of अइउण् was declared open so that सवर्ण could work,
        # and the last rule closes it again.
        why = provisions_for("8.4.68")[0].why
        self.assertIn("कार्यार्थम्", why)
        self.assertIn("संवृतप्रतिज्ञानम्", why)

    def test_and_it_is_the_last_row_of_the_last_table(self):
        self.assertEqual(STUTVA_TABLE[-1].sutra, THE_LAST)
        self.assertEqual(STUTVA_RUN, ("8.4.40", "8.4.68"))


class NothingHappensByDefault(unittest.TestCase):
    """Two sounds none of these rules reaches stand as they are."""

    def test_an_unnamed_junction_reaches_nothing(self):
        got = at_the_junction(gana="ac", before="ac")
        self.assertEqual(got.sutra, "")
        self.assertEqual(got.does, "")


class Registration(unittest.TestCase):
    """Every row reaches the registry with real notes."""

    def test_the_table_holds_the_run_minus_what_was_codified_apart(self):
        codes = [row.sutra for row in STUTVA_TABLE]
        expected = ["8.4.%d" % n for n in range(40, 69)
                    if "8.4.%d" % n not in CODIFIED_APART]
        self.assertEqual(codes, expected)

    def test_every_sutra_is_registered_with_real_notes(self):
        for row in STUTVA_TABLE:
            self.assertTrue(REGISTRY.has(row.sutra), row.sutra)
            notes = REGISTRY.get(row.sutra).notes
            self.assertGreater(len(notes), 100, row.sutra)
            self.assertIn("SETTLED", notes, row.sutra)


class TheWholeWorkIsCodified(unittest.TestCase):
    """
    What was a debt in every module before this one.

    Every `WhatIsNotCodifiedYet` class in the suite named
    something ahead of it. This one has nothing to name: the
    Aṣṭādhyāyī is 3,983 sūtras and every one of them is in the
    registry. What is left is not coverage but depth, and that
    is what the notes and the tests are for.
    """

    def test_every_sutra_the_corpus_knows_is_codified(self):
        from src.astadhyayi.sources import all_sutra_ids

        missing = [s for s in all_sutra_ids() if not REGISTRY.has(s)]
        self.assertEqual(missing, [])

    def test_and_the_count_is_the_one_the_tradition_gives(self):
        from src.astadhyayi.sources import all_sutra_ids

        self.assertEqual(len(list(all_sutra_ids())), 3983)

    def test_and_the_first_and_the_last_are_both_there(self):
        # 1.1.1 वृद्धिरादैच् and 8.4.68 अ अ इति.
        self.assertTrue(REGISTRY.has("1.1.1"))
        self.assertTrue(REGISTRY.has(THE_LAST))


if __name__ == "__main__":
    unittest.main()
