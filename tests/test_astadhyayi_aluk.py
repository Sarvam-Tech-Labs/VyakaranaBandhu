# -*- coding: utf-8 -*-
"""
६.३.१–२४ — the case ending that does not drop.

Everything here is stated against 2.4.71 सुपो धातुप्रातिपदिकयोः,
which drops every ending inside a compound. 6.3.2's vṛtti says it
outright — **समासे कृते प्रातिपदिकत्वात् सुपो लुकि प्राप्ते
प्रतिषेधः क्रियते** — so what has to be true of this module is that
its default is the DROP, and that every rule is a departure from it
with a named condition. A resolver that answered *kept* by
accident would be inventing a Sanskrit word.
"""

from __future__ import annotations

import re
import unittest

import src.astadhyayi.rules  # noqa: F401 — populates the registry
from src.astadhyayi.aluk import (
    ALUK_RUN, ALUK_TABLE, NGI_VARTIKA, NIYAMA_THREE, OJASADI,
    OJASADI_VARTIKA, SASTHI_VARTIKA, STOKADI, STOKADI_SENSES,
    UTTARAPADE_RUN, aluk_runs, provisions_for, stays)
from src.astadhyayi.sutra import REGISTRY


def _n(sutra_id):
    return tuple(int(part) for part in sutra_id.split("."))


class TheDefaultIsThatTheEndingGoes(unittest.TestCase):
    """
    The whole run is a प्रतिषेध of 2.4.71, so silence has to mean
    *dropped* and not *unknown*.
    """

    def test_a_query_no_rule_reaches_says_the_ending_is_dropped(self):
        got = stays("aśva", uttarapada="pati")
        self.assertEqual(got.keeps, "")
        self.assertEqual(got.sutra, "")
        self.assertIn("2.4.71", got.why)

    def test_and_so_does_an_empty_one(self):
        self.assertEqual(stays().sutra, "")

    def test_every_rule_that_supplies_names_which_case(self):
        for row in ALUK_TABLE:
            if row.heading:
                continue
            self.assertIn(
                row.keeps,
                ("pañcamī", "tṛtīyā", "caturthī", "saptamī",
                 "ṣaṣṭhī"),
                row.sutra)


class TheTwoRunsStopInDifferentPlaces(unittest.TestCase):
    """
    **अलुगधिकारः प्रागानङः। उत्तरपदाधिकारः प्रागङ्गाधिकारात्** —
    one line of 6.3.1's vṛtti giving both bounds, and they are
    twenty-four sūtras apart from each other and a hundred and
    fifteen apart at the far end.
    """

    def test_aluk_stops_where_anan_replaces_it(self):
        self.assertEqual(ALUK_RUN, ("6.3.1", "6.3.24"))
        self.assertEqual(_n("6.3.25")[2], _n(ALUK_RUN[1])[2] + 1)

    def test_uttarapade_runs_the_whole_pada(self):
        self.assertEqual(UTTARAPADE_RUN, ("6.3.1", "6.3.139"))

    def test_they_start_together_and_the_second_outlives_the_first(
            self):
        self.assertEqual(ALUK_RUN[0], UTTARAPADE_RUN[0])
        self.assertLess(_n(ALUK_RUN[1]), _n(UTTARAPADE_RUN[1]))

    def test_every_row_falls_inside_the_shorter_run(self):
        for row in ALUK_TABLE:
            self.assertLessEqual(_n(row.sutra), _n(ALUK_RUN[1]),
                                 row.sutra)

    def test_the_summary_names_both_bounds_and_what_ends_each(self):
        why = aluk_runs().why
        for piece in (ALUK_RUN[1], UTTARAPADE_RUN[1], "6.3.25",
                      "6.4.1"):
            self.assertIn(piece, why)


class TheTableIsTheWholeRun(unittest.TestCase):
    def test_one_row_for_each_sutra_from_1_to_24(self):
        got = [row.sutra for row in ALUK_TABLE]
        self.assertEqual(got, ["6.3.%d" % n for n in range(1, 25)])

    def test_every_row_carries_its_reason(self):
        for row in ALUK_TABLE:
            self.assertGreater(len(row.why), 60, row.sutra)

    def test_the_run_is_grouped_by_the_case_it_keeps(self):
        """
        Pāṇini takes the cases in order and does not come back to
        one he has left: the ablative once, then the instrumental,
        then the dative, then the locative, then the genitive. A
        row out of that order would mean the reading is wrong.
        """
        order = ("pañcamī", "tṛtīyā", "caturthī", "saptamī",
                 "ṣaṣṭhī")
        seen = []
        for row in ALUK_TABLE:
            if row.heading or not row.keeps:
                continue
            if not seen or seen[-1] != row.keeps:
                seen.append(row.keeps)
        self.assertEqual(tuple(seen), order)


class TheHeadingConfersNothing(unittest.TestCase):
    def test_it_never_answers(self):
        row, = provisions_for("6.3.1")
        self.assertTrue(row.heading)
        self.assertEqual(row.keeps, "")
        self.assertNotEqual(stays(gana="stokādi").sutra, "6.3.1")

    def test_and_the_rule_it_reads_out_as_its_example_does(self):
        got = stays(gana="stokādi")
        self.assertEqual(got.sutra, "6.3.2")
        self.assertEqual(got.keeps, "pañcamī")


class TheFourOf6_3_2AreSensesAndNotWords(unittest.TestCase):
    """
    **स्तोकान्तिकदूरार्थकृच्छ्राणि स्तोकादीनि** — which is why the
    vṛtti's own examples include अल्प, अभ्याश and विप्रकृष्ट, none
    of which the sūtra names.
    """

    def test_the_four_are_the_four(self):
        self.assertEqual(len(STOKADI), 4)
        self.assertEqual(set(STOKADI), set(STOKADI_SENSES))

    def test_each_sense_covers_its_own_head_word(self):
        for head, covered in STOKADI_SENSES.items():
            self.assertIn(head, covered, head)

    def test_and_three_of_them_cover_a_word_the_sutra_never_says(
            self):
        extra = {word for words in STOKADI_SENSES.values()
                 for word in words} - set(STOKADI)
        self.assertEqual(extra, {"alpa", "abhyāśa", "viprakṛṣṭa"})


class ARefusalReportsTheRuleItRefuses(unittest.TestCase):
    """
    6.3.19 and 6.3.20 are both प्रतिषेधs of the locative अलुक्, and
    both of their example-words are कृदन्तs that 6.3.14 would
    otherwise have reached.
    """

    def test_those_are_the_only_two(self):
        refusing = {row.sutra for row in ALUK_TABLE if row.refuses}
        self.assertEqual(refusing, {"6.3.19", "6.3.20"})

    def test_each_names_an_earlier_rule_that_supplies(self):
        for code in ("6.3.19", "6.3.20"):
            row, = provisions_for(code)
            self.assertEqual(row.blocks, ("6.3.14",))
            self.assertLess(_n(row.blocks[0]), _n(code))

    def test_the_answer_keeps_nothing_and_names_the_supplier(self):
        got = stays(uttarapada="siddha")
        self.assertEqual(got.sutra, "6.3.19")
        self.assertEqual(got.keeps, "")
        self.assertEqual(got.blocked_by, ("6.3.14",))

    def test_and_the_supplier_still_answers_elsewhere(self):
        got = stays(samasa="tatpuruṣa", uttarapada_gana="kṛt")
        self.assertEqual(got.sutra, "6.3.14")
        self.assertEqual(got.keeps, "saptamī")

    def test_a_refusal_supplies_nothing_to_ask_for(self):
        self.assertEqual(
            stays(uttarapada="siddha", wants="saptamī").sutra, "")


class TwoRulesNameTheSameStemAndAreToldApartByWhatFollows(
        unittest.TestCase):
    """
    6.3.4 and 6.3.5 both name मनस्. One wants the compound to be a
    name, the other wants आज्ञायिन् after it — and naming the
    second member is the sharper of the two claims, so the score
    has to put 6.3.5 first when both could be read.
    """

    def test_the_name_condition_reaches_6_3_4(self):
        self.assertEqual(stays("manas", result="saṃjñā").sutra,
                         "6.3.4")

    def test_the_following_word_reaches_6_3_5(self):
        self.assertEqual(stays("manas", uttarapada="ājñāyin").sutra,
                         "6.3.5")

    def test_and_naming_both_still_reaches_the_narrower_one(self):
        self.assertEqual(
            stays("manas", uttarapada="ājñāyin",
                  result="saṃjñā").sutra, "6.3.5")

    def test_manas_alone_reaches_neither(self):
        """Neither rule is unconditional, so मनस् with nothing said
        about it falls back to 2.4.71 and the ending goes."""
        self.assertEqual(stays("manas").sutra, "")


class ANiyamaGrantsNothing(unittest.TestCase):
    """
    6.3.10's own vṛtti says the form was already available —
    **कारविशेषस्य संज्ञा एताः, तत्र पूर्वेणैव सिद्धे नियमार्थम्
    इदम्** — so the rule's content is three restrictions, each with
    a counter-example of its own.
    """

    def test_it_is_the_only_niyama_in_the_run(self):
        niyamas = {row.sutra for row in ALUK_TABLE if row.niyama}
        self.assertEqual(niyamas, {"6.3.10"})

    def test_the_rule_it_narrows_reaches_the_same_words(self):
        """स्तूपेशाणः is a name, so 6.3.9 had it already."""
        row, = provisions_for("6.3.10")
        earlier, = provisions_for("6.3.9")
        self.assertEqual(row.gana, earlier.gana)
        self.assertEqual(stays(gana="hal-adanta",
                               result="saṃjñā").sutra, "6.3.9")

    def test_and_it_states_three_restrictions(self):
        self.assertEqual(len(NIYAMA_THREE), 3)
        for word in NIYAMA_THREE:
            self.assertIn(word.split("-")[0],
                          "".join(NIYAMA_THREE))

    def test_each_restriction_has_a_counter_example(self):
        row, = provisions_for("6.3.10")
        self.assertGreaterEqual(row.keeps_out.count(";"), 2)


class AnOptionCanFaceBothWays(unittest.TestCase):
    """
    6.3.13's विभाषा is **उभयत्रविभाषा**: in a बहुव्रीहि from a
    body-part 6.3.12 would have kept the ending always, so the
    option takes it away; in a तत्पुरुष 6.3.19 would have refused
    it always, so the option grants it.
    """

    def test_the_optional_rules_are_these(self):
        got = tuple(row.sutra for row in ALUK_TABLE if row.optional)
        self.assertEqual(
            got, ("6.3.13", "6.3.14", "6.3.16", "6.3.17", "6.3.18",
                  "6.3.22", "6.3.24"))

    def test_and_the_answer_carries_the_option_through(self):
        self.assertTrue(stays(uttarapada="bandha").optional)
        self.assertFalse(stays("ojas").optional)

    def test_the_rule_that_would_have_been_compulsory_is_there(self):
        self.assertEqual(stays(gana="svāṅga").sutra, "6.3.12")
        self.assertFalse(stays(gana="svāṅga").optional)

    def test_and_so_is_the_one_that_would_have_refused(self):
        self.assertEqual(stays(uttarapada="siddha").sutra, "6.3.19")


class BahulamIsNotAnOption(unittest.TestCase):
    """
    6.3.14 alone says बहुलम्, and the vṛtti gives कर्णेजपः on one
    side and कुरुचरः on the other — two different words, not two
    forms of one. An option would have claimed both spellings of
    each, which is not what is attested.
    """

    def test_only_one_rule_says_it(self):
        got = {row.sutra for row in ALUK_TABLE if row.bahulam}
        self.assertEqual(got, {"6.3.14"})

    def test_it_is_reported_apart_from_the_ordinary_option(self):
        got = stays(samasa="tatpuruṣa", uttarapada_gana="kṛt")
        self.assertTrue(got.bahulam)
        self.assertFalse(stays(uttarapada="bandha").bahulam)


class WhatOnlyAVarttikaSupplies(unittest.TestCase):
    """
    Three places in this run where the sūtras alone would leave
    real Sanskrit unaccounted for, and the record has to say so
    rather than quietly widen a sūtra.
    """

    def test_6_3_3_names_four_and_the_varttika_adds_a_fifth(self):
        row, = provisions_for("6.3.3")
        self.assertEqual(len(OJASADI), 4)
        self.assertEqual(OJASADI_VARTIKA, ("añjas",))
        self.assertEqual(row.of, OJASADI + OJASADI_VARTIKA)
        self.assertIn("अञ्जस", row.why)

    def test_the_genitive_varttikas_carry_named_men(self):
        """Śunaḥśepa and Divodāsa are names, and no sūtra of the
        Aṣṭādhyāyī reaches either."""
        self.assertIn("śunaḥ-śepa", SASTHI_VARTIKA)
        self.assertIn("divo-dāsa", SASTHI_VARTIKA)
        row, = provisions_for("6.3.21")
        # देवानांप्रिय is quoted as the vārttika states it, before
        # the nominative ending: **देवानांप्रिय इत्यत्र च**.
        for word in ("शुनःशेपः", "दिवोदासाय", "देवानांप्रिय"):
            self.assertIn(word, row.why)

    def test_and_6_3_9_gets_two_stems_with_no_name_condition(self):
        self.assertEqual(NGI_VARTIKA, ("hṛd", "div"))
        row, = provisions_for("6.3.9")
        self.assertEqual(row.result, ("saṃjñā",))
        self.assertIn("हृद्द्युभ्यां", row.why)


class WantsFiltersByTheCaseKept(unittest.TestCase):
    def test_asking_for_a_case_the_reached_rule_does_not_keep(self):
        self.assertEqual(stays("ojas", wants="saptamī").sutra, "")

    def test_asking_for_the_one_it_does_keep(self):
        self.assertEqual(stays("ojas", wants="tṛtīyā").sutra,
                         "6.3.3")

    def test_wants_filters_and_does_not_supply(self):
        """
        आत्मन् is named twice — by 6.3.6 for the instrumental
        before an ordinal, and by 6.3.7 for the dative in a
        grammarians' term. Neither is unconditional, so the stem
        alone reaches neither, and asking for a case does NOT
        stand in for the condition the rule wants. `wants` narrows
        what has already been reached; it never widens it.
        """
        self.assertEqual(stays("ātman").sutra, "")
        self.assertEqual(stays("ātman", wants="caturthī").sutra, "")
        self.assertEqual(
            stays("ātman", result="vaiyākaraṇākhyā").sutra, "6.3.7")
        self.assertEqual(
            stays("ātman", uttarapada_gana="pūraṇa").sutra, "6.3.6")


class Registration(unittest.TestCase):
    def test_every_sutra_of_the_run_is_registered(self):
        for row in ALUK_TABLE:
            self.assertTrue(REGISTRY.has(row.sutra), row.sutra)

    def test_the_notes_are_read_off_these_rows(self):
        collapse = re.compile(r"\s+")
        for row in ALUK_TABLE:
            note = collapse.sub(" ", REGISTRY.get(row.sutra).notes)
            head = collapse.sub(" ", row.why.split("\\n\\n")[0])
            self.assertIn(head[:70], note, row.sutra)

    def test_the_pada_module_was_created_by_being_there(self):
        from src.astadhyayi import rules
        self.assertIn("adhyaya_6_pada_3", rules.PADAS)


class WhatIsNotCodifiedYet(unittest.TestCase):
    """
    Written as the exact shortfall. 6.3.25 आनङ् ऋतो द्वन्द्वे is
    what ENDS the अलुक् heading — the bound this module states is
    read off a sūtra that is not codified — and 6.3.139 is where
    उत्तरपदे stops.
    """

    def test_the_rule_that_bounds_this_run_has_landed(self):
        """
        This module's bound is read off **अलुगधिकारः प्रागानङः** —
        a sūtra outside its own run. The debt is collected, so the
        bound can be checked against the rule instead of against
        its absence: 6.3.25 is codified, it stands one sūtra past
        the end of अलुक्, and what it does is replace the first
        member rather than keep its ending.
        """
        from src.astadhyayi.anan_dvandva import substitute

        self.assertTrue(REGISTRY.has("6.3.25"))
        self.assertEqual(_n("6.3.25")[2], _n(ALUK_RUN[1])[2] + 1)
        self.assertEqual(
            substitute(gana="ṛd-anta-vidyā-yoni",
                       dvandva="ṛd-anta").becomes, "ānaṅ")

    def test_and_the_two_runs_name_the_same_class_of_stem(self):
        """
        6.3.23 keeps a genitive for ऋ-final words of learning and
        birth; 6.3.25 replaces the same class with आनङ्. One class,
        two operations, two sūtras apart — so the two modules have
        to name it identically or one of them is about something
        else.
        """
        from src.astadhyayi.anan_dvandva import (
            provisions_for as anan_for)

        here, = provisions_for("6.3.23")
        there, = anan_for("6.3.25")
        self.assertEqual(here.gana, there.gana)

    def test_and_the_end_of_the_pada_has_landed(self):
        """
        This module's उत्तरपदे was read as running to 6.3.139 —
        **उत्तरपदाधिकारः प्रागङ्गाधिकारात्** — a bound taken from
        a sūtra outside its own run. The debt is collected: the
        pāda is complete, and its last sūtra is still under this
        heading, which is what 6.3.139's own vṛtti says.
        """
        from src.astadhyayi.dirgha_samhita import (
            provisions_for as dirgha_for)

        self.assertTrue(REGISTRY.has("6.3.139"))
        self.assertEqual(UTTARAPADE_RUN[1], "6.3.139")
        last, = dirgha_for("6.3.139")
        self.assertIn("उत्तरपद इति वर्तते", last.why)

    def test_and_the_bound_beyond_it_has_landed_too(self):
        """
        **प्रागङ्गाधिकारात्** — this module's उत्तरपदे stops
        because 6.4.1 अङ्गस्य starts. That sūtra is codified now,
        so the bound can be checked against it: the two headings
        meet, one closing at 6.3.139 and the other opening at
        6.4.1 and running to the end of adhyāya 7.
        """
        from src.astadhyayi.anga_dirgha import ANGA_RUN

        self.assertTrue(REGISTRY.has("6.4.1"))
        self.assertEqual(ANGA_RUN[0], "6.4.1")
        self.assertEqual(UTTARAPADE_RUN[1], "6.3.139")
        self.assertEqual(ANGA_RUN[1], "7.4.97")

    def test_but_the_pada_before_it_is_complete(self):
        for n in (1, 110, 111, 199):
            self.assertTrue(REGISTRY.has("6.2.%d" % n), n)


if __name__ == "__main__":
    unittest.main()
