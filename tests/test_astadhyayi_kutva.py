# -*- coding: utf-8 -*-
"""
७.३.५२–६९ — च् and ज् become gutturals, and the ten refusals.

One rule and ten that take it back — in a stretch of eleven, one
of which supplies instead — six of them turning on a sense. The tests ask each pair the question the vṛtti asks:
पाक्यम् or अवश्यपाच्यम्, वाक्यम् or वाच्यम्, प्रयोग्यः or
प्रयोज्यः — one sound apart, and the sense is what decides.
"""

from __future__ import annotations

import unittest

from src.astadhyayi.kutva import (
    KUTVA_RUN,
    KUTVA_TABLE,
    NIPATANA,
    REFUSALS_FROM,
    YAJADI,
    guttural,
    provisions_for,
)
from src.astadhyayi.sources import REGISTRY
import src.astadhyayi.rules  # noqa: F401  (populates REGISTRY)


class TheRuleItself(unittest.TestCase):
    """7.3.52 and the four that extend it."""

    def test_a_c_or_j_becomes_a_guttural(self):
        # पाकः, त्यागः, रागः; पाक्यम्, वाक्यम्.
        for affix in ("ghit", "ṇyat"):
            got = guttural(gana="c-j-anta", before=affix)
            self.assertEqual(got.sutra, "7.3.52", affix)
            self.assertEqual(got.does, "kutva", affix)

    def test_which_guttural_is_settled_elsewhere(self):
        # 1.1.50 स्थानेऽन्तरतमः — the nearest one, and the sūtra
        # names the class only.
        self.assertIn("1.1.50", provisions_for("7.3.52")[0].why)
        self.assertTrue(REGISTRY.has("1.1.50"))

    def test_a_list_of_nouns_is_already_so_made(self):
        # न्यङ्कुः, मद्गुः, भृगुः, दूरेपाकः.
        self.assertEqual(guttural(gana="nyaṅku-ādi").sutra,
                         "7.3.53")

    def test_han_and_three_more_change_after_a_reduplication(self):
        # जिघांसति, प्रजिघीषति, जिगीषति, चिकीषति.
        wanted = {
            ("han", None): "7.3.55",
            ("hi", None): "7.3.56",
            ("ji", "san"): "7.3.57",
            ("ci", "san"): "7.3.58",
        }
        for (root, affix), code in wanted.items():
            got = guttural(root, before=affix or "", abhyasa=True)
            self.assertEqual(got.sutra, code, root)

    def test_and_only_one_of_those_four_is_optional(self):
        # चिचीषति beside चिकीषति; the other three are settled.
        optional = [row.sutra for row in KUTVA_TABLE
                    if row.optional]
        self.assertEqual(optional, ["7.3.58"])

    def test_the_reduplication_must_be_the_roots_own(self):
        # जिहननीयिषति — the reduplication belongs to a derived
        # stem, and the change does not come.
        self.assertIn("अभ्यासनिमित्ते",
                      provisions_for("7.3.55")[0].why)

    def test_one_exception_is_shown_unnecessary_and_kept(self):
        # अचङीति शक्यमकर्तुम् — in the चङ् the stem is the causal
        # and the rule could not have reached. It is kept
        # ज्ञापकार्थम्, and what it proves gets प्रजिघाययिषति.
        why = provisions_for("7.3.56")[0].why
        self.assertIn("शक्यम् अकर्तुम्", why)
        self.assertIn("ज्ञापकार्थम्", why)


class TheRefusals(unittest.TestCase):
    """7.3.59–69, ten refusals and one rule that is not."""

    def test_the_refusals_are_ten_in_a_stretch_of_eleven(self):
        # 7.3.59 to 7.3.69 looks like one block and is not:
        # 7.3.64 sits in the middle of it and SUPPLIES the
        # guttural. The first draft of this test asserted eleven
        # refusals and the table said ten.
        self.assertEqual(REFUSALS_FROM, "7.3.59")
        refusing = [row.sutra for row in KUTVA_TABLE
                    if row.refuses]
        self.assertEqual(len(refusing), 10)
        self.assertEqual(refusing[0], REFUSALS_FROM)
        self.assertNotIn("7.3.64", refusing)

    def test_a_root_beginning_with_a_guttural_keeps_its_own(self):
        # कूजो वर्तते, खर्जः, गर्जः.
        got = guttural(gana="ku-ādi", before="ghit")
        self.assertEqual(got.sutra, "7.3.59")
        self.assertEqual(got.does, "")
        self.assertIn("7.3.52", got.blocked_by)

    def test_and_two_roots_by_name(self):
        # समाजः, परिव्राजः.
        for root in ("aj", "vraj"):
            self.assertEqual(
                guttural(root, before="ghit").sutra, "7.3.60",
                root)

    def test_aj_has_no_example_before_nyat_and_the_vrtti_says_why(self):
        # अजेर्व्यघञपोः इति वीभावस्य विधानाद् ण्यति नास्त्युदाहरणम्
        # — 2.4.56 replaces the root with वी there, and that rule
        # is codified.
        self.assertIn("नास्त्युदाहरणम्",
                      provisions_for("7.3.60")[0].why)
        self.assertTrue(REGISTRY.has("2.4.56"))


class WhereASenseDecides(unittest.TestCase):
    """Six pairs of forms, one sound apart."""

    def test_each_pair_differs_only_in_the_sense(self):
        # पाक्यम् / अवश्यपाच्यम्; वाक्यम् / वाच्यम्;
        # प्रयोग्यः / प्रयोज्यः; भोग्यः / भोज्यम्.
        wanted = {
            ("", "ṇya", "āvaśyaka"): "7.3.65",
            ("vac", "ṇyat", ""): "7.3.67",
            ("prayojya", "", "śakya"): "7.3.68",
            ("bhojya", "", "bhakṣya"): "7.3.69",
        }
        for (root, affix, sense), code in wanted.items():
            got = guttural(root, before=affix, sense=sense)
            self.assertEqual(got.sutra, code, (root, sense))
            self.assertEqual(got.does, "", code)

    def test_and_without_the_sense_the_guttural_comes(self):
        # पाक्यम्, वाक्यम् — 7.3.52 stands.
        self.assertEqual(
            guttural(gana="c-j-anta", before="ṇyat").sutra,
            "7.3.52")

    def test_two_words_are_laid_down_as_a_hand_and_an_ailment(self):
        # भुजः पाणिः; न्युब्ज उपतापो रोगः. In other senses they
        # are भोगः and समुद्गः.
        for root in ("bhuja", "nyubja"):
            got = guttural(root, before="ghañ",
                           sense="pāṇi-upatāpa")
            self.assertEqual(got.sutra, "7.3.61", root)
            self.assertTrue(got.nipatana, root)

    def test_and_two_more_as_parts_of_a_rite(self):
        # पञ्च प्रयाजाः; प्रयागः otherwise.
        for root in ("prayāja", "anuyāja"):
            self.assertEqual(
                guttural(root, sense="yajña-aṅga").sutra,
                "7.3.62", root)

    def test_the_two_are_named_as_a_specimen_only(self):
        # प्रदर्शनार्थम्, अन्यत्राप्येवंप्रकारे कुत्वं न भवति —
        # so उपयाजाः, पत्नीसंयाजाः and ऋतुयाजैः come out too.
        self.assertIn("प्रदर्शनार्थम्",
                      provisions_for("7.3.62")[0].why)

    def test_vanc_keeps_its_c_of_going(self):
        # वञ्च्यं वञ्चन्ति वणिजः; वङ्कं काष्ठम् otherwise.
        self.assertEqual(guttural("vañc", sense="gati").sutra,
                         "7.3.63")
        self.assertNotEqual(guttural("vañc").sutra, "7.3.63")

    def test_every_laid_down_word_has_its_sense_recorded(self):
        self.assertEqual(len(NIPATANA), 7)
        for word, sense in NIPATANA:
            self.assertTrue(sense, word)

    def test_five_roots_refuse_it_before_nya(self):
        # याज्यम्, याच्यम्, रोच्यम्, प्रवाच्यम्, अर्च्यम्.
        self.assertEqual(len(YAJADI), 5)
        for root in YAJADI:
            self.assertEqual(guttural(root, before="ṇya").sutra,
                             "7.3.66", root)


class TheOneRuleThatAlsoStrengthens(unittest.TestCase):
    """7.3.64, where a निपातन does two things at once."""

    def test_okas_is_laid_down_with_the_guttural_and_the_guna(self):
        # न्योकः शकुन्तः; न्योको गृहम्.
        got = guttural("uc", before="ka")
        self.assertEqual(got.sutra, "7.3.64")
        self.assertEqual(got.does, "kutva-guṇa")
        self.assertTrue(got.nipatana)

    def test_and_it_is_built_on_ka_for_the_accent(self):
        # स्वरार्थम्, अन्तोदात्तोऽयमिष्यते, घञि सत्याद्युदात्तः
        # स्यात् — a घञ् would have put the accent at the front.
        self.assertIn("स्वरार्थम्",
                      provisions_for("7.3.64")[0].why)


class NothingHappensByDefault(unittest.TestCase):
    """A root with no palatal takes nothing from this run."""

    def test_an_unnamed_root_reaches_nothing(self):
        got = guttural("bhū", before="ghit")
        self.assertEqual(got.sutra, "")
        self.assertEqual(got.does, "")


class Registration(unittest.TestCase):
    """Every row reaches the registry with real notes."""

    def test_the_run_is_contiguous(self):
        self.assertEqual(KUTVA_RUN, ("7.3.52", "7.3.69"))
        codes = [row.sutra for row in KUTVA_TABLE]
        self.assertEqual(
            codes, ["7.3.%d" % n for n in range(52, 70)])

    def test_every_sutra_is_registered_with_real_notes(self):
        for row in KUTVA_TABLE:
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

    def test_the_affixes_this_run_turns_on_are_live(self):
        # 3.3.18's घञ् gives पाकः, 3.1.124's ण्यत् पाक्यम्, and
        # 2.4.56's वी is why अज् has no example before ण्यत्.
        for code in ("3.3.18", "3.1.124", "2.4.56"):
            self.assertTrue(REGISTRY.has(code), code)

    def test_but_the_last_pada_of_the_adhyaya_is_not_read(self):
        # 7.4.62's कुहोश्चुः is what turns the reduplication's
        # own guttural back into a palatal — जिघांसति has both
        # rules in it. It is not codified; when it lands this
        # fails and the note must state the live dependency.
        # 7.4.62 has landed with पाद ७.४. जिघांसति has both
        # rules in it — this module's guttural and that one's
        # palatal for the copy — and both can be asked now.
        self.assertTrue(REGISTRY.has("7.4.62"))


if __name__ == "__main__":
    unittest.main()
