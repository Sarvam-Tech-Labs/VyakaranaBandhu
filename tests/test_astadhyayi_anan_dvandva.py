# -*- coding: utf-8 -*-
"""
६.३.२५–३३ — आनङ् and the द्वन्द्व substitutions.

The run is nine rules and two classes. Its interest is not the
substitutes but the arguing around them: a word repeated to narrow
itself, a substitute written with a marker to stop another rule, a
substitute whose whole point is to arrive after two others have
acted, and a form that is half laid down and half derived.
"""

from __future__ import annotations

import re
import unittest

import src.astadhyayi.rules  # noqa: F401 — populates the registry
from src.astadhyayi.aluk import ALUK_RUN
from src.astadhyayi.anan_dvandva import (
    ANAN_RUN, ANAN_TABLE, NOT_PAIRED, PUTRA_CARRIES, RTA_VIDYA,
    RTA_YONI, VAYU_VARTIKA, provisions_for, substitute)
from src.astadhyayi.sutra import REGISTRY


def _n(sutra_id):
    return tuple(int(part) for part in sutra_id.split("."))


class ThisRunIsWhatEndsTheOneBeforeIt(unittest.TestCase):
    """
    6.3.1's अलुक् was bounded by **प्रागानङः** — before आनङ् —
    so this run's first sūtra is the other run's stated bound, and
    the two numbers have to agree.
    """

    def test_it_opens_one_sutra_after_aluk_closes(self):
        self.assertEqual(_n(ANAN_RUN[0])[2], _n(ALUK_RUN[1])[2] + 1)

    def test_the_debt_the_aluk_module_wrote_is_paid(self):
        self.assertTrue(REGISTRY.has(ANAN_RUN[0]))

    def test_every_row_falls_inside_the_run(self):
        for row in ANAN_TABLE:
            self.assertLessEqual(_n(ANAN_RUN[0]), _n(row.sutra))
            self.assertLessEqual(_n(row.sutra), _n(ANAN_RUN[1]))


class TheTableIsTheWholeRun(unittest.TestCase):
    def test_one_row_for_each_sutra_from_25_to_33(self):
        got = [row.sutra for row in ANAN_TABLE]
        self.assertEqual(got, ["6.3.%d" % n for n in range(25, 34)])

    def test_every_row_names_a_substitute(self):
        for row in ANAN_TABLE:
            self.assertTrue(row.becomes, row.sutra)

    def test_every_row_carries_its_reason(self):
        for row in ANAN_TABLE:
            self.assertGreater(len(row.why), 60, row.sutra)

    def test_nothing_answers_where_no_rule_is_reached(self):
        got = substitute("aśvattha")
        self.assertEqual((got.becomes, got.sutra), ("", ""))
        self.assertIn("stands as it is", got.why)


class TheClassCarriesStraightDownFromTheAlukRun(unittest.TestCase):
    """
    6.3.23 and 6.3.24 had just been keeping a genitive for ऋ-final
    words of learning and birth. 6.3.25 takes the same class and
    does something else to it — which is why the two modules name
    the class with the same string.
    """

    def test_the_class_is_the_one_the_earlier_rule_named(self):
        from src.astadhyayi.aluk import provisions_for as aluk_for

        earlier, = aluk_for("6.3.23")
        here, = provisions_for("6.3.25")
        self.assertEqual(here.gana, earlier.gana)

    def test_and_it_covers_both_kinds(self):
        self.assertIn("hotṛ", RTA_VIDYA)
        self.assertIn("mātṛ", RTA_YONI)
        for word in RTA_VIDYA + RTA_YONI:
            self.assertTrue(word.endswith("ṛ"), word)

    def test_a_word_from_the_aluk_run_is_still_running_here(self):
        """
        **पुत्र इत्यनुवर्तते, ऋत इति च** — पुत्र was last said at
        6.3.22, two sūtras before the heading changed, and 6.3.25
        still has it. पितापुत्रौ is the proof.
        """
        self.assertEqual(PUTRA_CARRIES, ("putra",))
        row, = provisions_for("6.3.25")
        self.assertIn("पितापुत्रौ", row.why)
        self.assertIn("पुत्र इत्यनुवर्तते", row.why)

    def test_the_rule_reaches_the_class_and_not_a_stem_alone(self):
        self.assertEqual(
            substitute(gana="ṛd-anta-vidyā-yoni",
                       dvandva="ṛd-anta").sutra, "6.3.25")
        self.assertEqual(substitute("hotṛ").sutra, "")


class SayingDvandvaTwiceNarrowsIt(unittest.TestCase):
    """
    **द्वन्द्व इति वर्तमाने पुनर्द्वन्द्वग्रहणं
    प्रसिद्धसाहचर्यार्थम्** — the word was already running from
    6.3.25, so repeating it cannot widen and can only restrict.
    What it restricts to is pairs usage has already made.
    """

    def test_an_established_pair_of_gods_is_reached(self):
        got = substitute("indra", dvandva="devatā")
        self.assertEqual(got.sutra, "6.3.26")
        self.assertEqual(got.becomes, "ānaṅ")

    def test_two_gods_who_are_not_a_pair_are_not(self):
        for word in NOT_PAIRED:
            self.assertEqual(
                substitute(word, dvandva="devatā").sutra, "", word)

    def test_and_a_varttika_keeps_one_god_out_in_either_order(self):
        self.assertEqual(VAYU_VARTIKA, ("vāyu",))
        self.assertEqual(
            substitute("vāyu", dvandva="devatā").sutra, "")
        self.assertEqual(
            substitute("agni", uttarapada="vāyu",
                       dvandva="devatā").sutra, "")

    def test_the_note_says_why_the_word_is_repeated(self):
        row, = provisions_for("6.3.26")
        self.assertIn("प्रसिद्धसाहचर्यार्थम्", row.why)


class ThreeSubstitutesCompeteForAgni(unittest.TestCase):
    """
    6.3.26 gives every god आनङ्; 6.3.27 gives अग्नि ई before two
    named gods; 6.3.28 gives अग्नि इ once a वृद्धि has been made,
    and its vṛtti says it exists to beat both — **आनङम् ईत्वं च
    बाधितुम् इकारः क्रियते**. The order has to fall out of the
    score and not be written down.
    """

    def test_the_general_rule_reaches_agni_too(self):
        self.assertEqual(
            substitute("agni", uttarapada="indra",
                       dvandva="devatā").sutra, "6.3.26")

    def test_naming_the_following_god_beats_it(self):
        self.assertEqual(
            substitute("agni", uttarapada="soma",
                       dvandva="devatā").becomes, "ī")

    def test_and_the_vrddhi_condition_beats_that(self):
        got = substitute("agni", uttarapada="varuṇa",
                         dvandva="devatā", result="vṛddhi")
        self.assertEqual(got.sutra, "6.3.28")
        self.assertEqual(got.becomes, "i")

    def test_the_last_of_the_three_says_it_displaces_the_other_two(
            self):
        row, = provisions_for("6.3.28")
        self.assertEqual(row.blocks, ("6.3.26", "6.3.27"))

    def test_indra_is_not_kept_out_by_name_but_by_arithmetic(self):
        """
        **वृद्धाविति किम्? आग्नेन्द्रः। नेन्द्रस्य परस्य
        इत्युत्तरपदवृद्धिः प्रतिषिध्यते** — इन्द्र is NOT named out
        of 6.3.28. 7.3.22 refuses the second member's वृद्धि, so
        the condition 6.3.28 asks about never arises and 6.3.26's
        आनङ् stands. Writing इन्द्र into `excludes` would have got
        आग्नेन्द्रः right for the wrong reason and then produced
        no form at all.
        """
        row, = provisions_for("6.3.28")
        self.assertNotIn("indra", row.excludes)
        got = substitute("agni", uttarapada="indra",
                         dvandva="devatā")
        self.assertEqual((got.sutra, got.becomes),
                         ("6.3.26", "ānaṅ"))

    def test_but_visnu_is_kept_out_by_name(self):
        """The one real exception, and a vārttika's rather than a
        sūtra's: **इद् वृद्धौ विष्णोः प्रतिषेधो वक्तव्यः**."""
        row, = provisions_for("6.3.28")
        self.assertEqual(row.excludes, ("viṣṇu",))
        self.assertIn("विष्णोः प्रतिषेधो", row.why)
        got = substitute("agni", uttarapada="viṣṇu",
                         dvandva="devatā", result="vṛddhi")
        self.assertEqual((got.sutra, got.becomes),
                         ("6.3.26", "ānaṅ"))

    def test_a_rule_that_names_what_it_displaces_outranks_it(self):
        """
        By conditions alone 6.3.27 would win: it names a following
        word and 6.3.28 does not. What settles it is that 6.3.28
        SAYS what it defeats — **आनङम् ईत्वं च बाधितुम्** — so the
        score has to weigh `blocks`, not only sharpness.
        """
        sharper, = provisions_for("6.3.27")
        winner, = provisions_for("6.3.28")
        self.assertTrue(sharper.uttarapada)
        self.assertFalse(winner.uttarapada)
        self.assertEqual(len(winner.blocks), 2)
        self.assertEqual(
            substitute("agni", uttarapada="varuṇa",
                       dvandva="devatā", result="vṛddhi").sutra,
            "6.3.28")


class OneStemHasTwoSubstitutesAndBothStand(unittest.TestCase):
    """
    6.3.30's च keeps 6.3.29 alive alongside it — **चकाराद् द्यावा
    च** — so दिवस्पृथिव्यौ and द्यावापृथिव्यौ are both correct,
    which is not what a later rule usually does to an earlier one.
    """

    def test_div_alone_takes_dyava(self):
        self.assertEqual(
            substitute("div", dvandva="devatā").becomes, "dyāvā")

    def test_before_prthivi_it_takes_divas(self):
        self.assertEqual(
            substitute("div", uttarapada="pṛthivī",
                       dvandva="devatā").becomes, "divas")

    def test_and_asking_for_the_earlier_one_still_finds_it(self):
        """The `wants` filter is what shows both are available in
        the same environment: 6.3.30 does not displace 6.3.29."""
        got = substitute("div", uttarapada="pṛthivī",
                         dvandva="devatā", wants="dyāvā")
        self.assertEqual(got.sutra, "6.3.29")

    def test_the_note_says_the_ca_is_what_keeps_it(self):
        row, = provisions_for("6.3.30")
        self.assertIn("चकाराद् द्यावा च", row.why)
        self.assertEqual(row.blocks, ())


class AFormLaidDownIsMarkedAsLaidDown(unittest.TestCase):
    """
    6.3.32 and 6.3.33 are निपातन — the word is given whole rather
    than derived — and each is credited: one to the northerners,
    one to the Veda. A rule that merely substituted would be a
    different claim.
    """

    def test_those_two_are_the_only_ones(self):
        got = {row.sutra for row in ANAN_TABLE if row.nipatana}
        self.assertEqual(got, {"6.3.32", "6.3.33"})

    def test_one_is_credited_to_a_school(self):
        got = substitute("mātṛ", uttarapada="pitṛ", result="udīcām")
        self.assertEqual(got.sutra, "6.3.32")
        self.assertTrue(got.nipatana)
        self.assertEqual(
            substitute("mātṛ", uttarapada="pitṛ").sutra, "")

    def test_the_other_reverses_the_pair_and_only_in_the_veda(self):
        got = substitute("pitṛ", uttarapada="mātṛ", chandasi=True)
        self.assertEqual(got.sutra, "6.3.33")
        self.assertEqual(
            substitute("pitṛ", uttarapada="mātṛ").sutra, "")

    def test_and_only_half_of_that_one_is_laid_down(self):
        """
        **पूर्वपदस्याराङादेशो निपात्यते। उत्तरपदे तु सुपां सुलुक्०
        इति आकारादेशः** — पितरा is given, मातरा is built.
        """
        row, = provisions_for("6.3.33")
        for cited in ("7.1.39", "7.3.110"):
            self.assertIn(cited, row.why)


class TheMarkerOnTheSubstituteDoesWork(unittest.TestCase):
    """
    **नकारोच्चारणं रपरत्वनिवृत्त्यर्थम्** — आनङ् is written with a
    ङ् so that 1.1.51 उरण् रपरः does not put a र् after the
    substitute for an ऋ. A codification that recorded the
    substitute as *āna* would have lost the argument.
    """

    def test_the_substitute_is_recorded_with_its_marker(self):
        for code in ("6.3.25", "6.3.26"):
            row, = provisions_for(code)
            self.assertEqual(row.becomes, "ānaṅ")

    def test_and_the_note_says_what_the_marker_stops(self):
        row, = provisions_for("6.3.25")
        self.assertIn("रपरत्वनिवृत्त्यर्थम्", row.why)
        self.assertIn("1.1.51", row.why)


class Registration(unittest.TestCase):
    def test_every_sutra_of_the_run_is_registered(self):
        for row in ANAN_TABLE:
            self.assertTrue(REGISTRY.has(row.sutra), row.sutra)

    def test_the_notes_are_read_off_these_rows(self):
        collapse = re.compile(r"\s+")
        for row in ANAN_TABLE:
            note = collapse.sub(" ", REGISTRY.get(row.sutra).notes)
            head = collapse.sub(" ", row.why.split("\\n\\n")[0])
            self.assertIn(head[:70], note, row.sutra)


class WhatIsNotCodifiedYet(unittest.TestCase):
    """
    Written as the exact shortfall. 6.3.34 opens the पुंवद्भाव
    run — a feminine stem taking a masculine's shape before a
    second member — and it is the next thing to do.
    """

    def test_the_run_that_follows_this_one_has_landed(self):
        """
        6.3.34 opens the पुंवद्भाव run — a feminine stem taking a
        masculine's shape before a second member. The debt is
        collected, and what is worth asserting now is the join: it
        opens where this run closes, and it does something this
        run does not, so neither answers for the other.
        """
        from src.astadhyayi.pumvadbhava import behaves_as

        self.assertTrue(REGISTRY.has("6.3.34"))
        self.assertEqual(_n("6.3.34")[2], _n(ANAN_RUN[1])[2] + 1)
        self.assertEqual(
            behaves_as("bhāṣitapuṃska-anūṅ",
                       result="samānādhikaraṇa").does, "puṃvat")
        self.assertEqual(
            substitute("bhāṣitapuṃska-anūṅ").sutra, "")

    def test_but_everything_up_to_here_is_codified(self):
        for n in range(1, 34):
            self.assertTrue(REGISTRY.has("6.3.%d" % n), n)


if __name__ == "__main__":
    unittest.main()
