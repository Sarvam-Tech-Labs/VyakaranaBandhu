# -*- coding: utf-8 -*-
"""
Tests for 6.1.45–57 — the आकार heading.

Three things here are not like anything the project has met before.

The heading is bounded by its OWN LAST RULE. Every प्राक् heading of
adhyāyas 4 and 5 was bounded by a word lifted out of the rule that
comes AFTER its last — प्राक् क्रीतात्, प्राग् वतेः — and the marker
was therefore outside the run. 6.1.45's vṛtti says नित्यं स्मयतेः
इति यावत्, and 6.1.57 is a member.

The heading is also a RULE, so unlike every table since adhyāya 4 the
fallback here supplies something.

And उपदेशे is what keeps the general rule off सिध्, खिद्, भी and
स्मि, which is why the rules after 6.1.48 have to name them one by
one. A resolver that let 6.1.45 reach them would answer सेधयति with
आ and be wrong in exactly the place the vṛtti argues hardest.
"""

from __future__ import annotations

import unittest

import src.astadhyayi.rules  # noqa: F401 — populates the registry
from src.astadhyayi.atva import (
    ATVA_MARKER, ATVA_RUN, ATVA_TABLE, EC, SHIDADI, VIBHASA_RUN,
    atva_run, becomes_a, provisions_for)
from src.astadhyayi.sutra import REGISTRY


def _order(sutra_id):
    return tuple(int(p) for p in sutra_id.split("."))


class TheHeadingEndsOnItsOwnLastRule(unittest.TestCase):
    def test_the_marker_is_inside_the_run(self):
        """
        The whole difference from every heading before this one. A
        प्राक् heading's marker is the rule after its last and is
        NOT governed by it; this marker is the last rule itself.
        """
        self.assertEqual(ATVA_MARKER, ATVA_RUN[1])
        self.assertTrue(provisions_for(ATVA_MARKER))

    def test_the_vrtti_names_that_rule_by_its_own_words(self):
        opening = provisions_for("6.1.45")[0]
        self.assertIn("नित्यं स्मयतेः इति यावत्", opening.why)
        self.assertIn("नित्यं स्मयतेः", provisions_for("6.1.57")[0].why)

    def test_the_run_is_contiguous_and_codified(self):
        first, last = (int(s.split(".")[2]) for s in ATVA_RUN)
        for n in range(first, last + 1):
            code = "6.1.%d" % n
            self.assertTrue(provisions_for(code), code)
            self.assertTrue(REGISTRY.has(code), code)

    def test_every_row_falls_inside_the_run(self):
        first, last = (_order(s) for s in ATVA_RUN)
        for row in ATVA_TABLE:
            self.assertLessEqual(first, _order(row.sutra), row.sutra)
            self.assertLessEqual(_order(row.sutra), last, row.sutra)

    def test_the_report_says_which_way_the_bound_runs(self):
        answer = atva_run()
        self.assertEqual(answer.sutra, "6.1.45")
        self.assertIn("6.1.57", answer.why)


class TheHeadingIsAlsoARule(unittest.TestCase):
    def test_it_supplies_where_no_narrower_rule_does(self):
        answer = becomes_a("glai", final="ai")
        self.assertEqual(answer.sutra, "6.1.45")
        self.assertEqual(answer.does, "ā")

    def test_it_is_the_only_row_marked_a_heading(self):
        headings = [r.sutra for r in ATVA_TABLE if r.heading]
        self.assertEqual(headings, ["6.1.45"])

    def test_and_it_carries_a_condition_of_its_own(self):
        row = provisions_for("6.1.45")[0]
        self.assertEqual(row.not_before, "śit")
        self.assertTrue(row.final_ec)

    def test_a_sit_affix_takes_the_substitution_away(self):
        self.assertEqual(becomes_a("glai", final="ai", before="śit").sutra,
                         "")


class UpadeseIsWhatKeepsTheGeneralRuleOffFourRoots(unittest.TestCase):
    """
    सिध्, खिद्, भी and स्मि have no diphthong in the धातुपाठ — the ए
    they work on is guṇa arrived at later. That is precisely why
    6.1.49 to 6.1.57 name them by hand, and a resolver that let the
    heading reach them would make five of the section's rules idle.
    """

    NAMED_LATE = ("sidh", "khid", "bhī", "smi", "gur", "vī", "lī")

    def test_none_of_them_is_reached_by_the_heading(self):
        for root in self.NAMED_LATE:
            self.assertEqual(becomes_a(root).sutra, "", root)

    def test_each_is_named_by_a_rule_of_its_own(self):
        named = set()
        for row in ATVA_TABLE:
            named.update(row.of)
        for root in self.NAMED_LATE:
            self.assertIn(root, named, root)

    def test_the_four_diphthongs_are_what_the_heading_wants(self):
        # The order is the varṇa module's, not ours — the SET is
        # what matters, and it is asked there rather than
        # written out a second time here.
        self.assertEqual(set(EC), {"e", "ai", "o", "au"})
        for final in EC:
            self.assertEqual(becomes_a("glai", final=final).sutra,
                             "6.1.45", final)

    def test_a_root_taught_with_a_simple_vowel_reaches_nothing(self):
        self.assertEqual(becomes_a("ci", final="i").sutra, "")

    def test_but_the_rule_that_names_it_still_reaches_it(self):
        self.assertEqual(becomes_a("ci", before="ṇi").sutra, "6.1.54")

    def test_the_note_gives_the_counter_example_for_upadese(self):
        self.assertIn("चेता", provisions_for("6.1.45")[0].why)


class ASitAffixIsReadAsSidadi(unittest.TestCase):
    """
    एश् has its श् at the end. On the plain reading of शित् it would
    stop the substitution and जग्ले would be unreachable — so the
    vṛtti reads the marker as an INITIAL श् instead.
    """

    def test_the_maxim_is_recorded_where_it_is_used(self):
        # तदादौ + अल्ग्रहणे joins into तदादावल्ग्रहणे, so the
        # fragment has to start after the junction.
        self.assertIn("विधिस्तदादावल्ग्रहणे", SHIDADI)
        self.assertIn(SHIDADI, provisions_for("6.1.45")[0].why)

    def test_the_note_states_the_two_readings_and_picks_one(self):
        why = provisions_for("6.1.45")[0].why
        self.assertIn("श एव इत् शित्", why)
        self.assertIn("जग्ले", why)

    def test_the_perfect_is_not_the_affix_the_rule_refuses(self):
        """
        Read एश् as a शित् and this comes back empty. It does not,
        because the column holds the marker and not the affix.
        """
        self.assertEqual(becomes_a("glai", final="ai", before="liṭ").sutra,
                         "6.1.45")


class TheOptionRunsAndThenAWordEndsIt(unittest.TestCase):
    """
    6.1.51's विभाषा carries down six rules. 6.1.57 says नित्यम् and
    the option stops — the same device 6.1.32 used by repeating
    संप्रसारणम्.
    """

    def test_the_optional_rules_are_exactly_the_run(self):
        optional = [r.sutra for r in ATVA_TABLE if r.optional]
        first, last = (int(s.split(".")[2]) for s in VIBHASA_RUN)
        self.assertEqual(optional,
                         ["6.1.%d" % n for n in range(first, last + 1)])

    def test_the_rule_that_ends_it_is_not_itself_a_choice(self):
        self.assertFalse(becomes_a("smi", before="ṇi",
                                   result="hetubhaya").optional)

    def test_and_the_rule_before_it_still_is(self):
        self.assertTrue(becomes_a("bhī", before="ṇi",
                                  result="hetubhaya").optional)

    def test_the_two_differ_in_nothing_but_the_root(self):
        fifty_six = provisions_for("6.1.56")[0]
        fifty_seven = provisions_for("6.1.57")[0]
        self.assertEqual(fifty_six.before, fifty_seven.before)
        self.assertEqual(fifty_six.result, fifty_seven.result)
        self.assertNotEqual(fifty_six.of, fifty_seven.of)

    def test_the_note_names_the_word_that_dropped_the_option(self):
        self.assertIn("नित्यग्रहणाद् विभाषेति निवृत्तम्",
                      provisions_for("6.1.57")[0].why)

    def test_nothing_before_the_run_is_optional(self):
        for row in ATVA_TABLE:
            if _order(row.sutra) < _order(VIBHASA_RUN[0]):
                self.assertFalse(row.optional, row.sutra)


class ARefusalNamesWhatItTakesTheFormFrom(unittest.TestCase):
    def test_there_is_one_refusal_and_it_names_the_heading(self):
        refusing = [r for r in ATVA_TABLE if r.refuses]
        self.assertEqual([r.sutra for r in refusing], ["6.1.46"])
        self.assertEqual(refusing[0].blocks, ("6.1.45",))

    def test_it_reports_no_substitution(self):
        answer = becomes_a("vyeñ", before="liṭ")
        self.assertEqual(answer.does, "")
        self.assertEqual(answer.blocked_by, ("6.1.45",))

    def test_and_it_does_not_govern_what_it_excepts(self):
        """
        Away from लिट् the heading is untouched, and व्येञ् takes its
        आ like any other एजन्त root.
        """
        elsewhere = becomes_a("vyeñ", final="e", before="kta")
        self.assertEqual(elsewhere.sutra, "6.1.45")
        self.assertEqual(elsewhere.does, "ā")


class OneRootIsReachedTwiceOnDifferentTerms(unittest.TestCase):
    """
    स्फुर् is named at 6.1.47 before घञ् and at 6.1.54 before णि. One
    is fixed and the other a choice, which is only visible if both
    rows are kept and the affix is what tells them apart.
    """

    def test_two_rules_name_it(self):
        naming = [r.sutra for r in ATVA_TABLE if "sphur" in r.of]
        self.assertEqual(naming, ["6.1.47", "6.1.54"])

    def test_before_ghan_it_is_fixed(self):
        answer = becomes_a("sphur", before="ghañ")
        self.assertEqual(answer.sutra, "6.1.47")
        self.assertFalse(answer.optional)

    def test_before_ni_it_is_a_choice(self):
        answer = becomes_a("sphur", before="ṇi")
        self.assertEqual(answer.sutra, "6.1.54")
        self.assertTrue(answer.optional)

    def test_and_a_third_affix_reaches_neither(self):
        self.assertEqual(becomes_a("sphur", before="kta").sutra, "")


class ASenseCanBeWhatDecides(unittest.TestCase):
    def test_the_rule_with_a_sense_beats_the_one_without(self):
        """
        6.1.48 names three roots before णि and 6.1.49 names one root
        before णि with a sense. The one with the sense has to be the
        narrower or its condition would never bite.
        """
        with_sense = becomes_a("sidh", before="ṇi",
                               result="apāralaukika")
        self.assertEqual(with_sense.sutra, "6.1.49")

    def test_the_wrong_sense_reaches_nothing_at_all(self):
        self.assertEqual(
            becomes_a("sidh", before="ṇi", result="pāralaukika").sutra,
            "")

    def test_and_the_note_argues_that_case_rather_than_asserting_it(self):
        why = provisions_for("6.1.49")[0].why
        self.assertIn("तापसं सेधयति", why)
        self.assertIn("दास्यामीति", why)

    def test_each_sense_belongs_to_the_rule_that_names_it(self):
        for code, sense in (("6.1.49", "apāralaukika"),
                            ("6.1.55", "prajana"),
                            ("6.1.56", "hetubhaya"),
                            ("6.1.57", "hetubhaya")):
            self.assertEqual(provisions_for(code)[0].result, sense, code)


class APreverbCanBeWhatDecides(unittest.TestCase):
    def test_the_one_rule_with_a_preverb_wants_it(self):
        self.assertEqual(provisions_for("6.1.53")[0].pre, "apa")

    def test_with_it_the_rule_fires(self):
        self.assertEqual(
            becomes_a("gur", before="ṇamul", pre="apa").sutra, "6.1.53")

    def test_without_it_nothing_does(self):
        self.assertEqual(becomes_a("gur", before="ṇamul").sutra, "")


class TheVedicRuleIsOutOfReachWithoutTheCorpus(unittest.TestCase):
    def test_it_answers_nothing_in_ordinary_speech(self):
        self.assertEqual(becomes_a("khid").sutra, "")

    def test_but_does_once_the_corpus_is_named(self):
        answer = becomes_a("khid", chandasi=True)
        self.assertEqual(answer.sutra, "6.1.52")
        self.assertTrue(answer.chandasi)
        self.assertTrue(answer.optional)

    def test_it_is_the_only_vedic_row(self):
        vedic = [r.sutra for r in ATVA_TABLE if r.chandasi]
        self.assertEqual(vedic, ["6.1.52"])


class ASettledOptionIsMarkedAsOne(unittest.TestCase):
    def test_the_settled_one_is_still_an_option(self):
        row = provisions_for("6.1.51")[0]
        self.assertTrue(row.vyavasthita)
        self.assertTrue(row.optional)

    def test_it_is_the_only_row_so_marked(self):
        settled = [r.sutra for r in ATVA_TABLE if r.vyavasthita]
        self.assertEqual(settled, ["6.1.51"])

    def test_and_the_note_says_what_settles_it(self):
        self.assertIn("व्यवस्थितविभाषाविज्ञानात्",
                      provisions_for("6.1.51")[0].why)


class EveryRowCarriesItsEvidence(unittest.TestCase):
    def test_each_note_has_something_in_it(self):
        for row in ATVA_TABLE:
            self.assertGreater(len(row.why), 120, row.sutra)

    def test_the_registered_notes_are_read_off_these_rows(self):
        for row in ATVA_TABLE:
            registered = REGISTRY.get(row.sutra).notes
            opening = " ".join(
                row.why.split("\\n\\n")[0].split()).replace("**", "")
            flattened = " ".join(registered.split()).replace("**", "")
            self.assertIn(opening[:60], flattened, row.sutra)


class WhatIsNotCodifiedYet(unittest.TestCase):
    def test_the_module_does_not_build_the_finished_form(self):
        """
        `becomes_a` says which rule substitutes. Getting from ग्लै to
        ग्लाता wants 7.2.35's इट् and the तृच् rules, and from क्री to
        क्रापयति wants 7.3.36's प्. Written when none of the three
        was codified; 7.2.35 has landed with पाद ७.२, so the इट्
        half can be asked of the engine now and the other two
        cannot.
        """
        # 7.2.35's इट् and 7.3.36's प् have both landed since,
        # so ग्लाता and क्रापयति can be asked of the engine end
        # to end. 7.3.86's guṇa is not codified yet, and when it
        # lands this assertion fails.
        # All three have landed since; what is still ahead is
        # पाद ७.४, and 7.4.1 is where it begins.
        for code in ("7.2.35", "7.3.36", "7.3.86"):
            self.assertTrue(REGISTRY.has(code), code)
        # पाद ७.४ has been read through since — 7.4.1 to
        # 7.4.97 — so ग्लाता and क्रापयति can both be asked of
        # the engine end to end, and so can the causal aorist
        # 7.4.1 shortens. Every rule this module hands on to is
        # live; what is ahead is अध्याय ८.
        self.assertTrue(REGISTRY.has("7.4.1"))
        answer = becomes_a("krī", before="ṇi")
        self.assertEqual(answer.does, "ā")
        self.assertNotIn("krāpayati", str(answer))

    def test_the_two_rules_the_prasajya_argument_leans_on(self):
        """
        6.1.45's अशिति being a प्रसज्यप्रतिषेध is what lets 3.1.136
        and 3.3.128 find a root ending in आ. Both are codified, so
        this is a live dependency and not a promise.
        """
        for code in ("3.1.136", "3.3.128"):
            self.assertTrue(REGISTRY.has(code), code)
        self.assertIn("3.1.136", provisions_for("6.1.45")[0].why)


if __name__ == "__main__":
    unittest.main()
