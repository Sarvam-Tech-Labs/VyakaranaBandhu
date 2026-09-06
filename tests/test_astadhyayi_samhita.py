# -*- coding: utf-8 -*-
"""
Tests for 6.1.72–83 — संहितायाम्, and a heading inside a heading.

Three things here are new to the project.

**Two अधिकारs are open at once, and they are bounded differently.**
संहिता runs 6.1.72–157 and is bounded by the words of 6.1.158, which
is OUTSIDE its run; अचि opens at 6.1.77 inside it and is bounded by
the words of 6.1.108, which is a MEMBER. Both are declared by the
vṛtti and neither by a word in the sūtra.

**A rule fixes what a LATER rule will make optional.** 6.1.74's vṛtti
says so outright — पदान्ताद् वा इति विकल्पे प्राप्ते नित्यं तुगागमो
भवति. An अपवाद pointing forward.

**And one rule supplies nothing at all.** 6.1.80 only narrows 6.1.79,
so it must never be the answer to *what happens here* — it has to be
reported on the answer instead.
"""

from __future__ import annotations

import unittest

import src.astadhyayi.rules  # noqa: F401 — populates the registry
from src.astadhyayi.samhita import (
    ACI_MARKER, ACI_RUN, ANG_SENSES, NAVAYAVA, SAMHITA_MARKER,
    SAMHITA_RUN, SAMHITA_TABLE, joins, provisions_for, samhita_run)
from src.astadhyayi.sutra import REGISTRY


def _order(sutra_id):
    return tuple(int(p) for p in sutra_id.split("."))


class TwoHeadingsAreOpenAtOnce(unittest.TestCase):
    def test_the_outer_one_covers_the_rest_of_the_pada(self):
        self.assertEqual(SAMHITA_RUN, ("6.1.72", "6.1.157"))
        self.assertIn("अनुदात्तं पदमेकवर्जम्",
                      provisions_for("6.1.72")[0].why)

    def test_and_its_marker_stands_outside_the_run(self):
        """
        The rule whose words bound संहिता is 6.1.158, and it is not
        governed by the heading it bounds. 6.1.45's आकार was bounded
        the other way, by its own last rule, and the two shapes have
        to stay distinguishable.
        """
        self.assertEqual(SAMHITA_MARKER, "6.1.158")
        self.assertGreater(_order(SAMHITA_MARKER), _order(SAMHITA_RUN[1]))

    def test_the_inner_one_opens_five_sutras_later(self):
        self.assertEqual(ACI_RUN, ("6.1.77", "6.1.108"))
        self.assertGreater(_order(ACI_RUN[0]), _order(SAMHITA_RUN[0]))
        self.assertLess(_order(ACI_RUN[1]), _order(SAMHITA_RUN[1]))

    def test_and_its_marker_is_a_member_of_its_own_run(self):
        self.assertEqual(ACI_MARKER, ACI_RUN[1])

    def test_the_vrtti_declares_the_inner_one_by_the_words_of_a_rule(self):
        self.assertIn("संप्रसारणाच्च इति यावत्",
                      provisions_for("6.1.77")[0].why)

    def test_the_report_carries_both_and_says_how_they_differ(self):
        answer = samhita_run()
        self.assertEqual(answer.sutra, "6.1.72")
        for named in ("6.1.157", "6.1.77", "6.1.108", "6.1.158"):
            self.assertIn(named, answer.why, named)


class TheOuterHeadingSuppliesNothing(unittest.TestCase):
    """
    6.1.72 states a condition every rule to 6.1.157 is read under and
    orders no operation. If it were reachable it would answer every
    question the table is ever asked, since it has no condition of
    its own to fail.
    """

    def test_it_orders_nothing(self):
        self.assertEqual(provisions_for("6.1.72")[0].does, "")

    def test_it_is_never_the_answer(self):
        for kwargs in ({}, {"before": "cha"}, {"before": "ac"},
                       {"before": "hal"}):
            self.assertNotEqual(joins(**kwargs).sutra, "6.1.72", kwargs)

    def test_the_condition_it_states_is_recorded_with_its_counter(self):
        row = provisions_for("6.1.72")[0]
        self.assertIn("दधि अत्र", row.keeps_out)
        self.assertIn("संहितायामिति", row.why)


class TheInnerHeadingAlsoStatesARule(unittest.TestCase):
    """
    6.1.77 is both, as 6.1.45 was. A resolver that shut every heading
    out would lose इको यणचि itself — which is the most-cited rule of
    the whole pāda.
    """

    def test_it_is_marked_a_heading(self):
        self.assertTrue(provisions_for("6.1.77")[0].heading)

    def test_and_it_still_answers(self):
        answer = joins(before="ac")
        self.assertEqual(answer.sutra, "6.1.77")
        self.assertEqual(answer.does, "yaṇ")

    def test_the_two_headings_differ_in_whether_they_order_anything(self):
        headings = [(r.sutra, bool(r.does)) for r in SAMHITA_TABLE
                    if r.heading]
        self.assertEqual(headings, [("6.1.72", False), ("6.1.77", True)])


class ARuleFixesWhatALaterRuleWillLoosen(unittest.TestCase):
    """
    6.1.74 is stated before 6.1.76 and takes its two words out of an
    option that has not been stated yet. The project met this shape
    once before, at 5.1.21.
    """

    def test_the_later_rule_is_the_optional_one(self):
        self.assertTrue(provisions_for("6.1.76")[0].optional)
        self.assertFalse(provisions_for("6.1.74")[0].optional)

    def test_and_the_earlier_rule_names_it(self):
        row = provisions_for("6.1.74")[0]
        self.assertEqual(row.blocks, ("6.1.76",))
        self.assertGreater(_order(row.blocks[0]), _order(row.sutra))

    def test_a_named_word_gets_the_fixed_augment(self):
        answer = joins("āṅ", before="cha", after="padānta-dīrgha")
        self.assertEqual(answer.sutra, "6.1.74")
        self.assertFalse(answer.optional)
        self.assertEqual(answer.blocked_by, ("6.1.76",))

    def test_and_an_unnamed_word_falls_back_to_the_option(self):
        answer = joins("kuṭī", before="cha", after="padānta-dīrgha")
        self.assertEqual(answer.sutra, "6.1.76")
        self.assertTrue(answer.optional)

    def test_the_four_senses_the_marker_picks_out_are_recorded(self):
        self.assertEqual(len(ANG_SENSES), 4)
        self.assertIn("ङिद्विशिष्टग्रहणं किम्",
                      provisions_for("6.1.74")[0].why)


class WhatPrecedesTellsTheThreeTukRulesApart(unittest.TestCase):
    """
    6.1.73, 6.1.75 and 6.1.76 share their `before` exactly — छ — and
    nothing else distinguishes them. Drop the `after` column and all
    three collapse into whichever happens to be first.
    """

    def test_all_three_want_the_same_following_sound(self):
        for code in ("6.1.73", "6.1.75", "6.1.76"):
            self.assertEqual(provisions_for(code)[0].before, "cha", code)

    def test_but_each_wants_a_different_preceding_one(self):
        preceding = [provisions_for(c)[0].after
                     for c in ("6.1.73", "6.1.75", "6.1.76")]
        self.assertEqual(preceding, ["hrasva", "dīrgha",
                                     "padānta-dīrgha"])

    def test_and_each_answers_only_for_its_own(self):
        for after, code in (("hrasva", "6.1.73"), ("dīrgha", "6.1.75"),
                            ("padānta-dīrgha", "6.1.76")):
            self.assertEqual(joins(before="cha", after=after).sutra,
                             code, after)

    def test_a_fourth_shape_reaches_none_of_them(self):
        self.assertEqual(joins(before="cha", after="hal").sutra, "")

    def test_the_augment_belongs_to_the_sound_and_not_the_word(self):
        """
        ह्रस्व एवात्रागमी, न तु तदन्तः — and the consequence is
        चिच्छिदतुः, where 7.4.60 does not strike the त् out because a
        part of a part is not a part of the whole.
        """
        why = provisions_for("6.1.73")[0].why
        # एव + अत्र + आगमी joins into एवात्रागमी, so the
        # आ of आगमी is gone and the fragment has to carry the
        # whole junction.
        self.assertIn("ह्रस्व एवात्रागमी", why)
        self.assertIn("चिच्छिदतुः", why)
        self.assertIn(NAVAYAVA, why)


class OneRuleSuppliesNothingAndOnlyNarrows(unittest.TestCase):
    """
    6.1.80 धातोस्तन्निमित्तस्यैव adds no substitution. It says when
    6.1.79's holds for a root, and nothing else — so it must not be
    the answer to *what happens here*.
    """

    def test_it_is_the_only_row_of_its_shape(self):
        narrowing = [r.sutra for r in SAMHITA_TABLE if r.restricts]
        self.assertEqual(narrowing, ["6.1.80"])
        self.assertEqual(provisions_for("6.1.80")[0].does, "")

    def test_it_is_never_the_answer(self):
        self.assertNotEqual(joins(before="ya-pratyaya").sutra, "6.1.80")

    def test_the_rule_it_narrows_answers_instead(self):
        answer = joins(before="ya-pratyaya")
        self.assertEqual(answer.sutra, "6.1.79")
        self.assertEqual(answer.does, "vānta")

    def test_and_the_narrowing_is_reported_on_that_answer(self):
        self.assertEqual(joins(before="ya-pratyaya").narrowed_by,
                         ("6.1.80",))

    def test_it_names_the_rule_it_narrows_and_not_itself(self):
        row = provisions_for("6.1.80")[0]
        self.assertEqual(row.restricts, ("6.1.79",))
        self.assertNotIn(row.sutra, row.restricts)

    def test_the_note_carries_the_two_readings_of_its_own_evakara(self):
        """
        एवकारकरणं किम्? धात्ववधारणं यथा स्यात्, तन्निमित्तावधारणं मा
        भूत् — one word, two readings, and the wrong one loses
        बाभ्रव्यः.
        """
        why = provisions_for("6.1.80")[0].why
        self.assertIn("एवकारकरणं किम्", why)
        self.assertIn("बाभ्रव्यः", why)
        self.assertIn("गव्यं", why)


class TheNipatanasAreToldApartByASense(unittest.TestCase):
    """
    6.1.81 and 6.1.82 both put अय् in before यत्, and both are laid
    down whole. Only the sense separates them, and each vṛtti gives
    the form that fails it.
    """

    def test_all_three_are_marked_as_laid_down(self):
        laid_down = [r.sutra for r in SAMHITA_TABLE if r.nipatana]
        self.assertEqual(laid_down, ["6.1.81", "6.1.82", "6.1.83"])

    def test_each_answers_only_in_its_own_sense(self):
        self.assertEqual(
            joins("kṣi", before="yat", result="śakya").sutra, "6.1.81")
        self.assertEqual(
            joins("krī", before="yat", result="tadartha").sutra, "6.1.82")

    def test_the_wrong_sense_reaches_nothing(self):
        self.assertEqual(
            joins("kṣi", before="yat", result="tadartha").sutra, "")
        self.assertEqual(joins("kṣi", before="yat").sutra, "")

    def test_each_records_the_form_its_sense_keeps_out(self):
        self.assertIn("क्षेयं पापम्", provisions_for("6.1.81")[0].keeps_out)
        self.assertIn("क्रेयं", provisions_for("6.1.82")[0].keeps_out)

    def test_the_two_senses_are_set_against_each_other_in_one_sentence(self):
        """
        क्रेयं नो धान्यम्, न चास्ति क्रय्यम् — the vṛtti puts both
        forms in one clause, which is the clearest kind of evidence
        a sense-condition can have.
        """
        why = provisions_for("6.1.82")[0].why
        self.assertIn("न चास्ति क्रय्यम्", why)


class TheVedicNipatanaIsOutOfReachWithoutTheCorpus(unittest.TestCase):
    def test_it_answers_nothing_in_ordinary_speech(self):
        self.assertEqual(joins("bhī", before="yat").sutra, "")

    def test_but_does_once_the_corpus_is_named(self):
        answer = joins("bhī", before="yat", chandasi=True)
        self.assertEqual(answer.sutra, "6.1.83")
        self.assertTrue(answer.chandasi)
        self.assertTrue(answer.nipatana)

    def test_it_is_the_only_vedic_row(self):
        vedic = [r.sutra for r in SAMHITA_TABLE if r.chandasi]
        self.assertEqual(vedic, ["6.1.83"])

    def test_the_note_records_that_one_form_is_feminine_only(self):
        self.assertIn("स्त्रियामेव निपातनम्",
                      provisions_for("6.1.83")[0].why)


class TheSectionIsWhereItSaysItIs(unittest.TestCase):
    def test_the_rows_are_the_twelve_less_the_one_held_elsewhere(self):
        held = sorted(r.sutra for r in SAMHITA_TABLE)
        expected = sorted(
            "6.1.%d" % n
            for n in list(range(72, 78)) + list(range(79, 84)))
        self.assertEqual(held, expected)

    def test_the_one_gap_belongs_to_the_module_that_owns_it(self):
        """
        6.1.78 एचोऽयवायावः is `anga.ayadi`, reached ahead long before
        this pāda was read. 6.1.79 leans on it — it names the two of
        its four substitutes that end in व् — so the boundary is
        worth pinning.
        """
        self.assertEqual(provisions_for("6.1.78"), ())
        self.assertEqual(REGISTRY.get("6.1.78").apply.__module__,
                         "src.astadhyayi.anga")
        self.assertIn("6.1.78", provisions_for("6.1.79")[0].why)

    def test_the_pada_is_contiguous_through_the_section(self):
        for n in range(1, 84):
            self.assertTrue(REGISTRY.has("6.1.%d" % n), n)

    def test_every_rule_here_is_registered_against_this_resolver(self):
        for row in SAMHITA_TABLE:
            self.assertEqual(REGISTRY.get(row.sutra).apply.__name__,
                             "joins", row.sutra)


class NothingAnswersByDefault(unittest.TestCase):
    def test_an_unreached_question_gets_nothing(self):
        answer = joins(before="hal")
        self.assertEqual(answer.sutra, "")
        self.assertEqual(answer.does, "")

    def test_and_the_message_says_the_heading_supplies_nothing(self):
        self.assertIn("6.1.72", joins(before="hal").why)


class EveryRowCarriesItsEvidence(unittest.TestCase):
    def test_each_note_has_something_in_it(self):
        for row in SAMHITA_TABLE:
            self.assertGreater(len(row.why), 120, row.sutra)

    def test_the_registered_notes_are_read_off_these_rows(self):
        for row in SAMHITA_TABLE:
            registered = REGISTRY.get(row.sutra).notes
            opening = " ".join(
                row.why.split("\\n\\n")[0].split()).replace("**", "")
            flattened = " ".join(registered.split()).replace("**", "")
            self.assertIn(opening[:60], flattened, row.sutra)


class WhatIsNotCodifiedYet(unittest.TestCase):
    def test_the_module_still_does_not_perform_the_junction(self):
        """
        `joins` says which rule acts. 8.4.40's श्चुत्व, which turns
        6.1.73's त् into च्, has since been codified — so the debt
        has moved from the rule to this module: it names the
        operation and does not carry it out, and दध्यत्र is still
        not something it returns.
        """
        self.assertTrue(REGISTRY.has("8.4.40"))
        answer = joins(before="ac")
        self.assertEqual(answer.gives, "yaṇ")
        self.assertNotIn("dadhyatra", str(answer))

    def test_the_ekadesa_heading_now_opens_inside_this_one(self):
        """
        6.1.84 एकः पूर्वपरयोः is codified now — the debt this test
        was written as, paid. And what it turned into is worth more
        than the debt was: THREE headings are open at once over
        6.1.87, and the two inner ones do not nest. अचि runs
        6.1.77–108 and एकः पूर्वपरयोः runs 6.1.84–111, so the second
        opens inside the first and CLOSES OUTSIDE it. Only the
        outermost, संहिता, contains them both.
        """
        from src.astadhyayi.ekadesa import EKADESA_RUN

        self.assertTrue(REGISTRY.has("6.1.84"))
        self.assertEqual(provisions_for("6.1.84"), ())
        self.assertEqual(REGISTRY.get("6.1.84").apply.__module__,
                         "src.astadhyayi.ekadesa")

        first, last = (_order(s) for s in SAMHITA_RUN)
        for run in (ACI_RUN, EKADESA_RUN):
            self.assertLessEqual(first, _order(run[0]), run)
            self.assertLessEqual(_order(run[1]), last, run)
        # The two inner runs overlap without either containing the
        # other: 84 falls inside 77–108, and 111 falls outside it.
        self.assertLess(_order(ACI_RUN[0]), _order(EKADESA_RUN[0]))
        self.assertLess(_order(EKADESA_RUN[0]), _order(ACI_RUN[1]))
        self.assertLess(_order(ACI_RUN[1]), _order(EKADESA_RUN[1]))


if __name__ == "__main__":
    unittest.main()
