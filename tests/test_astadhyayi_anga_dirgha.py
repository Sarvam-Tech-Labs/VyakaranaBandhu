# -*- coding: utf-8 -*-
"""
६.४.१–२१ — the aṅga heading, and the first things done to a stem.

The heading is the point. 6.4.1 governs six hundred and thirteen
sūtras, to the end of adhyāya 7, and everything this module and
the whole of adhyāya 7 will say is read through it. So the first
thing to hold the table to is that the bound is the vṛtti's and
not a guess.

After that, three arguments:

**A refusal that supplies nothing and settles something.** 6.4.4
न तिसृचतसृ is a ज्ञापक for the order of two rules in adhyāya 7.

**A नियम that takes back what an earlier rule had given.** 6.4.12
restricts 6.4.8 to one ending, and 6.4.13 then has to let another
back in.

**And one substitute that needs its तुक् and one that must not
have it.** 6.4.19 and 6.4.21 replace the same छ् and reason in
opposite directions about the same rule, 6.1.73.
"""

from __future__ import annotations

import re
import unittest

import src.astadhyayi.rules  # noqa: F401 — populates the registry
from src.astadhyayi.anga_dirgha import (
    ANGA_DIRGHA_TABLE, ANGA_RUN, APTRN_LIST, DIRGHA_RUN,
    IN_HAN_FOUR, JVARADI, LEANS_ON_6_3_137, anga_runs,
    provisions_for, to_the_stem)
from src.astadhyayi.sutra import REGISTRY


def _n(sutra_id):
    return tuple(int(part) for part in sutra_id.split("."))


class TheLongestHeadingInTheGrammar(unittest.TestCase):
    """
    **अधिकारोऽयम् आ सप्तमाध्यायपरिसमाप्तेः** — 6.4.1 to 7.4.97,
    read off the vṛtti and not inferred from where the rules leave
    off. Nothing else in the Aṣṭādhyāyī governs a quarter of it.
    """

    def test_it_runs_to_the_end_of_adhyaya_seven(self):
        self.assertEqual(ANGA_RUN, ("6.4.1", "7.4.97"))

    def test_which_is_more_than_six_hundred_sutras(self):
        from src.astadhyayi.corpus import collate

        inside = [key for key in collate()
                  if _n(ANGA_RUN[0]) <= _n(key) <= _n(ANGA_RUN[1])]
        self.assertGreater(len(inside), 600)

    def test_and_this_module_covers_only_its_opening(self):
        self.assertEqual(DIRGHA_RUN[0], ANGA_RUN[0])
        self.assertLess(_n(DIRGHA_RUN[1]), _n(ANGA_RUN[1]))
        self.assertEqual(DIRGHA_RUN[1], "6.4.21")

    def test_it_closes_where_a_different_heading_opens(self):
        """6.4.22 असिद्धवत्, which was codified before any of
        this and is a heading of another kind entirely."""
        self.assertEqual(_n("6.4.22")[2], _n(DIRGHA_RUN[1])[2] + 1)
        self.assertTrue(REGISTRY.has("6.4.22"))

    def test_the_summary_names_both_bounds(self):
        why = anga_runs().why
        for piece in (ANGA_RUN[1], DIRGHA_RUN[1], "6.4.22"):
            self.assertIn(piece, why)


class TheHeadingProvesItsOwnScopeThreeTimes(unittest.TestCase):
    """
    6.4.1's vṛtti does not merely state the scope. It takes three
    rules that will use it — one from this pāda, one from further
    on, one from 7.1 — and shows a pair for each: the operation
    applying, and the same operation not applying because what it
    would act on is no अङ्ग.
    """

    def test_the_note_quotes_three_rules(self):
        row, = provisions_for("6.4.1")
        for cited in ("हलः", "नामि", "अतो भिस ऐस्"):
            self.assertIn(cited, row.why, cited)

    def test_and_a_counter_example_for_each(self):
        row, = provisions_for("6.4.1")
        for cited in ("निरुतम्", "क्रिमिणां पश्य", "वृक्षैः"):
            self.assertIn(cited, row.why, cited)

    def test_two_of_the_three_are_inside_this_module(self):
        for code in ("6.4.2", "6.4.3"):
            self.assertTrue(REGISTRY.has(code), code)

    def test_and_the_third_is_now_a_live_dependency(self):
        """Written as a debt: 7.1.9 अतो भिस ऐस् was quoted by the
        heading and not codified. पाद ७.१ has been read through,
        so the heading's third proof can now be asked of the
        engine — which is what the debt was written for."""
        self.assertTrue(REGISTRY.has("7.1.9"))


class TheHeadingConfersNothingItself(unittest.TestCase):
    def test_it_never_answers(self):
        row, = provisions_for("6.4.1")
        self.assertTrue(row.heading)
        self.assertEqual(row.does, "")
        self.assertNotEqual(to_the_stem(before="nām").sutra,
                            "6.4.1")

    def test_and_the_rule_it_reads_out_does(self):
        got = to_the_stem(before="nām")
        self.assertEqual((got.sutra, got.does), ("6.4.3", "dīrgha"))

    def test_nothing_answers_where_no_rule_is_reached(self):
        got = to_the_stem("aśva", before="sup")
        self.assertEqual((got.does, got.sutra), ("", ""))
        self.assertIn("stands as it is", got.why)


class ARefusalThatSuppliesNothingAndSettlesSomething(
        unittest.TestCase):
    """
    6.4.4's content is not that तिसृ fails to lengthen. It is that
    the failure has to be STATED, and stating it proves a नुट् was
    already there: **दीर्घप्रतिषेधवचनं ज्ञापकम् — अचि र ऋतः
    इत्येतस्मात् पूर्वविप्रतिषेधेन नुडागमो भवतीति**.
    """

    def test_it_is_the_only_refusal_of_the_run(self):
        refusing = {row.sutra for row in ANGA_DIRGHA_TABLE
                    if row.refuses}
        self.assertEqual(refusing, {"6.4.4"})

    def test_it_names_the_rule_it_takes_the_word_from(self):
        row, = provisions_for("6.4.4")
        self.assertEqual(row.blocks, ("6.4.3",))
        self.assertLess(_n("6.4.3"), _n(row.sutra))

    def test_and_the_answer_supplies_nothing(self):
        got = to_the_stem("tisṛ", before="nām")
        self.assertEqual((got.sutra, got.does), ("6.4.4", ""))
        self.assertEqual(got.blocked_by, ("6.4.3",))

    def test_the_note_says_what_the_refusal_proves(self):
        row, = provisions_for("6.4.4")
        self.assertIn("ज्ञापकम्", row.why)
        for cited in ("7.1.54", "7.2.100"):
            self.assertIn(cited, row.why, cited)

    def test_both_rules_it_orders_are_live_now(self):
        """Written as the exact shortfall, when neither 7.1.54 nor
        7.2.100 was codified. 7.1.54's नुट् landed with पाद ७.१
        and 7.2.100's र with पाद ७.२, so the order 6.4.4 proves —
        the नुट् going in before the र does — can now be asked of
        the engine end to end."""
        for code in ("7.1.54", "7.2.100"):
            self.assertTrue(REGISTRY.has(code), code)


class AndTwoRulesUndoThatRefusal(unittest.TestCase):
    """
    6.4.5 gives the lengthening back to तिसृ and चतसृ in the Veda,
    and 6.4.6 adds नृ. A rule that undoes a refusal has to outrank
    it, and by conditions alone it does not — both name the same
    stems before the same affix.
    """

    def test_the_vedic_option_reaches_the_refused_stems(self):
        for stem in ("tisṛ", "catasṛ"):
            got = to_the_stem(stem, before="nām", chandasi=True)
            self.assertEqual(got.sutra, "6.4.5", stem)
            self.assertTrue(got.optional, stem)

    def test_and_outside_the_veda_the_refusal_stands(self):
        for stem in ("tisṛ", "catasṛ"):
            self.assertEqual(
                to_the_stem(stem, before="nām").sutra, "6.4.4",
                stem)

    def test_it_names_the_refusal_it_undoes(self):
        row, = provisions_for("6.4.5")
        self.assertEqual(row.blocks, ("6.4.4",))

    def test_and_the_third_of_them_records_a_disagreement(self):
        """**केचिद् अत्र छन्दसीति नानुवर्तयन्ति** — whether
        6.4.6's option is Vedic is disputed, and the record says
        so rather than choosing."""
        row, = provisions_for("6.4.6")
        self.assertFalse(row.chandasi)
        self.assertTrue(row.optional)
        self.assertIn("नानुवर्तयन्ति", row.why)


class ANiyamaTakesBackWhatAnEarlierRuleGave(unittest.TestCase):
    """
    6.4.8 lengthens before every सर्वनामस्थान. 6.4.12 then says
    **शावेव दीर्घो भवति नान्यत्र** for four stems — and 6.4.13 has
    to let सु back in, because the नियम had shut it out.
    """

    def test_it_is_the_only_niyama_of_the_run(self):
        got = {row.sutra for row in ANGA_DIRGHA_TABLE
               if row.niyama}
        self.assertEqual(got, {"6.4.12"})

    def test_the_earlier_rule_reached_the_same_stems(self):
        row, = provisions_for("6.4.8")
        self.assertEqual(row.before, ("sarvanāmasthāna",))
        self.assertEqual(len(IN_HAN_FOUR), 4)

    def test_and_the_niyama_says_it_grants_nothing(self):
        row, = provisions_for("6.4.12")
        self.assertIn("सिद्धे सत्यारम्भो नियमार्थः", row.why)
        self.assertIn("नान्यत्र", row.why)

    def test_so_a_third_rule_has_to_let_one_ending_back_in(self):
        got = to_the_stem(gana="in-han-four", before="su")
        self.assertEqual(got.sutra, "6.4.13")
        row, = provisions_for("6.4.13")
        self.assertEqual(row.blocks, ("6.4.12",))

    def test_and_before_si_the_niyama_itself_answers(self):
        got = to_the_stem(gana="in-han-four", before="śi")
        self.assertEqual(got.sutra, "6.4.12")
        self.assertTrue(got.niyama)


class TwoRulesReasonOppositeWaysAboutOneTuk(unittest.TestCase):
    """
    6.4.19 replaces छ् WITH its तुक् — **अन्तरङ्गत्वाच् छे च इति
    तुकि कृते सतुक्कस्य शादेशः** — and 6.4.21 replaces a छ् that
    has none: **राल्लोपे सतुक्कस्य छस्याभावात् केवलो गृह्यते**.
    Both are about 6.1.73, and the difference is whether a र्
    stands before.
    """

    def test_both_act_on_the_same_pair_of_sounds(self):
        for code in ("6.4.19", "6.4.21"):
            row, = provisions_for(code)
            self.assertEqual(row.part, "cha-va", code)

    def test_one_wants_the_tuk_there(self):
        row, = provisions_for("6.4.19")
        self.assertIn("तुकि कृते", row.why)
        self.assertIn("अन्तरङ्ग", row.why)

    def test_and_the_other_wants_it_absent(self):
        row, = provisions_for("6.4.21")
        self.assertIn("सतुक्कस्य छस्याभावात्", row.why)
        self.assertEqual(row.result, ("r-pūrva",))

    def test_and_the_rule_they_both_reason_about_is_codified(self):
        self.assertTrue(REGISTRY.has("6.1.73"))

    def test_the_third_of_the_three_replaces_two_sounds_at_once(
            self):
        """6.4.20's ऊठ् stands for the व् AND the penult, and the
        penult is on a different side of the व् in two of the five
        stems."""
        self.assertEqual(len(JVARADI), 5)
        row, = provisions_for("6.4.20")
        self.assertEqual(row.part, "va-upadhā")
        self.assertIn("वकारात् परा", row.why)
        self.assertIn("पूर्वा", row.why)


class WhatALenghtheningLeansOnElsewhere(unittest.TestCase):
    """
    6.4.16's vārttika wants an इङ् substitute in गम्, and one
    Vedic form has none. Rather than widening the rule, the vṛtti
    sends the form to 6.3.137 — the catch-all of the pāda before —
    so the record has to name that rule and it has to exist.
    """

    def test_the_note_names_the_rule_it_leans_on(self):
        row, = provisions_for("6.4.16")
        self.assertEqual(LEANS_ON_6_3_137, "6.3.137")
        self.assertIn("अन्येषामपि दृश्यते", row.why)

    def test_and_that_rule_is_codified_and_is_a_catch_all(self):
        from src.astadhyayi.dirgha_samhita import (
            provisions_for as dirgha_for)

        self.assertTrue(REGISTRY.has(LEANS_ON_6_3_137))
        other, = dirgha_for(LEANS_ON_6_3_137)
        self.assertEqual(other.of, ())
        self.assertEqual(other.before, ())


class TheListsAreTheVrttisOwn(unittest.TestCase):
    def test_eleven_stems_lengthen_before_a_sarvanamasthana(self):
        self.assertEqual(len(APTRN_LIST), 11)
        row, = provisions_for("6.4.11")
        self.assertEqual(row.of, APTRN_LIST)
        for stem in APTRN_LIST:
            self.assertEqual(
                to_the_stem(stem, before="sarvanāmasthāna").sutra,
                "6.4.11", stem)

    def test_and_the_vocative_singular_is_excepted_five_times(self):
        excepting = [row.sutra for row in ANGA_DIRGHA_TABLE
                     if "sambuddhi" in row.excludes]
        self.assertEqual(excepting, ["6.4.8", "6.4.9", "6.4.10",
                                     "6.4.11", "6.4.13", "6.4.14"])


class WantsFiltersByTheOperation(unittest.TestCase):
    def test_asking_for_the_one_it_does(self):
        self.assertEqual(
            to_the_stem(before="nām", wants="dīrgha").sutra,
            "6.4.3")

    def test_asking_for_one_it_does_not(self):
        self.assertEqual(
            to_the_stem(before="nām", wants="lopa").sutra, "")

    def test_and_it_filters_a_refusal_out_of_the_way(self):
        """
        `wants` keeps only rules that SUPPLY what is asked for, so
        6.4.4 drops out and the rule it refuses answers instead.
        That is the right answer to a narrower question, and the
        reason the unfiltered query is the one to ask: it comes
        back 6.4.4 with 6.4.3 on `blocked_by`, which is the whole
        story rather than half of it.
        """
        self.assertEqual(
            to_the_stem("tisṛ", before="nām", wants="dīrgha").sutra,
            "6.4.3")
        plain = to_the_stem("tisṛ", before="nām")
        self.assertEqual(plain.sutra, "6.4.4")
        self.assertEqual(plain.does, "")
        self.assertEqual(plain.blocked_by, ("6.4.3",))


class Registration(unittest.TestCase):
    def test_every_sutra_of_the_run_is_registered(self):
        for row in ANGA_DIRGHA_TABLE:
            self.assertTrue(REGISTRY.has(row.sutra), row.sutra)

    def test_the_notes_are_read_off_these_rows(self):
        collapse = re.compile(r"\s+")
        for row in ANGA_DIRGHA_TABLE:
            note = collapse.sub(" ", REGISTRY.get(row.sutra).notes)
            head = collapse.sub(" ", row.why.split("\\n\\n")[0])
            self.assertIn(head[:70], note, row.sutra)

    def test_it_joined_the_module_that_already_held_6_4_22(self):
        from src.astadhyayi import rules

        self.assertIn("adhyaya_6_pada_4", rules.PADAS)


class WhatIsNotCodifiedYet(unittest.TestCase):
    """
    Written as the exact shortfall. 6.4.23 श्नान्नलोपः opens the
    next stretch — the न् dropped from a stem — and everything
    from there to 6.4.175 is ahead, 6.4.77 excepted.
    """

    def test_the_run_that_follows_this_one_has_landed(self):
        """
        6.4.23 श्नान्नलोपः opens the न्-dropping stretch. The debt
        is collected, and the claim is the join: it starts two
        sūtras past this run, 6.4.22 असिद्धवत् standing between,
        and it drops a sound where this run lengthens one.
        """
        from src.astadhyayi.nalopa import n_goes

        self.assertTrue(REGISTRY.has("6.4.23"))
        self.assertEqual(_n("6.4.23")[2], _n(DIRGHA_RUN[1])[2] + 2)
        self.assertEqual(n_goes(before="śna").does, "na-lopa")
        self.assertEqual(to_the_stem(before="śna").sutra, "")

    def test_two_sutras_of_the_pada_were_codified_before_it(self):
        for code in ("6.4.22", "6.4.77"):
            self.assertTrue(REGISTRY.has(code), code)

    def test_and_the_pada_before_this_one_is_complete(self):
        for n in range(1, 140):
            self.assertTrue(REGISTRY.has("6.3.%d" % n), n)


if __name__ == "__main__":
    unittest.main()
