# -*- coding: utf-8 -*-
"""
Tests for 6.1.84–114 — एकः पूर्वपरयोः.

Two things here are worth holding down hard.

**A heading whose every word is argued for.** The vṛtti on 6.1.84
says what पूर्वपर buys and what एक buys, and names the failure each
prevents. A table that recorded the run and not the argument would
lose the only reason this heading is two words long.

**And a chain of exceptions that has to be read in ORDER.** 6.1.88
displaces 6.1.87; 6.1.94 displaces 6.1.88; 6.1.89 displaces 6.1.94
but NOT 6.1.95, which is a rule of the same kind standing one later.
The maxim that settles it is पुरस्तादपवादा अनन्तरान् विधीन् बाधन्ते
नोत्तरान्, and it is what makes उपेतः right and *उपैतः wrong.
"""

from __future__ import annotations

import unittest

import src.astadhyayi.rules  # noqa: F401 — populates the registry
from src.astadhyayi.ekadesa import (
    EKADESA_MARKER, EKADESA_RUN, EKADESA_TABLE, PURASTAT,
    WHY_BOTH_WORDS, ekadesa_run, one_for_both, provisions_for)
from src.astadhyayi.sutra import REGISTRY

#: Inside the run and held by other modules, each reached ahead long
#: before this pāda was read in order.
HELD_ELSEWHERE = {
    "6.1.85": "src.astadhyayi.asiddha",
    "6.1.86": "src.astadhyayi.asiddha",
    "6.1.97": "src.astadhyayi.anga",
    "6.1.101": "src.astadhyayi.anga",
}


def _order(sutra_id):
    return tuple(int(p) for p in sutra_id.split("."))


class TheHeadingsEveryWordIsArguedFor(unittest.TestCase):
    def test_it_runs_where_the_vrtti_bounds_it(self):
        self.assertEqual(EKADESA_RUN, ("6.1.84", "6.1.111"))
        self.assertEqual(EKADESA_MARKER, "6.1.112")
        self.assertIn("ख्यत्यात् परस्य",
                      provisions_for("6.1.84")[0].why)

    def test_and_the_marker_stands_outside_the_run(self):
        self.assertGreater(_order(EKADESA_MARKER),
                           _order(EKADESA_RUN[1]))

    def test_both_of_its_words_are_recorded_with_what_they_buy(self):
        self.assertEqual(len(WHY_BOTH_WORDS), 2)
        why = provisions_for("6.1.84")[0].why
        for phrase in WHY_BOTH_WORDS:
            self.assertIn(phrase, why)

    def test_the_failure_each_word_prevents_is_named(self):
        """
        Without पूर्वपर, 1.1.67 and 1.1.66 would send the
        substitution to opposite sides of the junction. Without एक,
        two स्थानिन् would take two substitutes. Both rules the
        argument leans on are codified.
        """
        why = provisions_for("6.1.84")[0].why
        for cited in ("1.1.67", "1.1.66"):
            self.assertIn(cited, why, cited)
            self.assertTrue(REGISTRY.has(cited), cited)

    def test_the_heading_supplies_nothing(self):
        self.assertEqual(provisions_for("6.1.84")[0].does, "")
        for kwargs in ({}, {"after": "a-ā"}, {"before": "ac"}):
            self.assertNotEqual(one_for_both(**kwargs).sutra, "6.1.84",
                                kwargs)

    def test_the_report_carries_both_arguments(self):
        answer = ekadesa_run()
        self.assertEqual(answer.sutra, "6.1.84")
        for phrase in WHY_BOTH_WORDS:
            self.assertIn(phrase, answer.why)


class TheExceptionChainIsReadInOrder(unittest.TestCase):
    """
    Five rules stand over one junction and each takes it from the one
    before. What decides which of two exceptions wins is not the
    numbering but a maxim about how far an earlier exception reaches.
    """

    def test_the_general_rule_gives_guna(self):
        answer = one_for_both(after="a-ā", before="ac")
        self.assertEqual(answer.sutra, "6.1.87")
        self.assertEqual(answer.does, "guṇa")

    def test_a_diphthong_takes_it_to_vrddhi(self):
        answer = one_for_both(after="a-ā", before="ec")
        self.assertEqual(answer.sutra, "6.1.88")
        self.assertEqual(answer.blocked_by, ("6.1.87",))

    def test_and_a_root_beginning_with_e_takes_it_to_the_later_form(self):
        answer = one_for_both(after="upasarga-a", before="eṅ-dhātu")
        self.assertEqual(answer.sutra, "6.1.94")
        self.assertEqual(answer.does, "pararūpa")
        self.assertEqual(answer.blocked_by, ("6.1.88",))

    def test_and_three_named_things_take_it_back_to_vrddhi(self):
        answer = one_for_both(after="a-ā", before="eti-edhati-ūṭh")
        self.assertEqual(answer.sutra, "6.1.89")
        self.assertEqual(answer.does, "vṛddhi")
        self.assertEqual(answer.blocked_by, ("6.1.94",))

    def test_but_not_past_the_rule_that_stands_one_later(self):
        """
        6.1.95 is a पररूप rule of exactly the same shape as 6.1.94,
        and 6.1.89 does NOT displace it. The reason is the maxim, and
        the form it decides is उपेतः.
        """
        self.assertNotIn("6.1.95", provisions_for("6.1.89")[0].blocks)
        why = provisions_for("6.1.89")[0].why
        self.assertIn("6.1.95", why)
        self.assertIn("उपेतः", why)

    def test_the_maxim_is_recorded_and_cited_where_it_is_used(self):
        self.assertIn("बाधन्ते नोत्तरान्", PURASTAT)
        for code in ("6.1.89", "6.1.102"):
            self.assertIn("पुरस्तादपवादा", provisions_for(code)[0].why,
                          code)

    def test_no_refusal_or_displacement_names_itself(self):
        for row in EKADESA_TABLE:
            self.assertNotIn(row.sutra, row.blocks, row.sutra)


class ARuleCanDisplaceOneStatedLaterInTheBook(unittest.TestCase):
    """
    Five rows of this section displace a rule stated after them, and
    two of those reach out of the pāda altogether: 6.1.93 against a
    vṛddhi 7.1.90 gives, and 6.1.113 against a य् 8.3.17 gives.
    Both were debts when this class was written, and both have since
    landed — so what it now asserts is that NOTHING a row of this
    table names is outside the registry.
    """

    def test_displacing_a_later_rule_is_ordinary_here(self):
        """
        Not the exception it was in adhyāya 5. Five rows of this one
        name a rule that comes AFTER them, and the numbering settles
        nothing: what settles it is what each vṛtti argues.
        """
        forward = [r.sutra for r in EKADESA_TABLE
                   if any(_order(b) > _order(r.sutra) for b in r.blocks)]
        self.assertGreaterEqual(len(forward), 4)
        self.assertIn("6.1.89", forward)
        self.assertIn("6.1.90", forward)

    def test_every_later_rule_named_is_codified_or_a_written_debt(self):
        outside = set()
        for row in EKADESA_TABLE:
            for named in row.blocks:
                if _order(named) <= _order(row.sutra):
                    continue
                if REGISTRY.has(named):
                    continue
                outside.add(named)
        # 7.1.90's णित् landed with पाद ७.१ and 8.3.17's य् with
        # पाद ८.३. The set has shrunk to nothing, which is where
        # a debt written as the shortfall ends up.
        self.assertEqual(outside, set())

    def test_one_of_them_reaches_forward_by_a_word_of_its_own(self):
        """
        6.1.90's च is what makes it displace two पररूप rules stated
        after it, and both of those are codified here.
        """
        for code in ("6.1.95", "6.1.96"):
            self.assertTrue(REGISTRY.has(code), code)
            self.assertEqual(provisions_for(code)[0].does, "pararūpa")
        # चकारः + अधिक… joins into चकारो‍धिक…, so the
        # fragment has to start after the junction.
        self.assertIn("धिकविधानार्थः",
                      provisions_for("6.1.90")[0].why)

    def test_and_both_of_those_are_live_now(self):
        # Written when neither was codified, then rewritten when
        # 7.1.90 गोतो णित् landed with पाद ७.१. 8.3.17
        # भोभगोअघोअपूर्वस्य योऽशि has landed with पाद ८.३, so
        # both displacements this section makes across a pāda
        # boundary can be asked of the engine end to end.
        self.assertTrue(REGISTRY.has("7.1.90"))
        self.assertTrue(REGISTRY.has("8.3.17"))

    def test_and_each_note_says_why_the_displacement_reaches(self):
        self.assertIn("नाप्राप्तायां", provisions_for("6.1.93")[0].why)
        self.assertIn("पूर्वत्रासिद्धम्",
                      provisions_for("6.1.113")[0].why)


class TheFourKindsOfSubstituteAreDistinct(unittest.TestCase):
    def test_all_of_them_are_present(self):
        kinds = {r.does for r in EKADESA_TABLE if r.does}
        self.assertEqual(
            kinds,
            {"guṇa", "vṛddhi", "pararūpa", "pūrvarūpa", "pūrvasavarṇa",
             "ā", "n", "ut"})

    def test_the_earlier_form_and_the_later_form_are_told_apart(self):
        self.assertEqual(one_for_both(after="ak", before="am").does,
                         "pūrvarūpa")
        self.assertEqual(one_for_both(after="a-ā", before="om-āṅ").does,
                         "pararūpa")

    def test_asking_for_one_kind_does_not_get_another(self):
        self.assertEqual(
            one_for_both(after="a-ā", before="ac", wants="vṛddhi").sutra,
            "")
        self.assertEqual(
            one_for_both(after="a-ā", before="ac", wants="guṇa").sutra,
            "6.1.87")

    def test_a_refusal_is_never_the_answer_to_a_request(self):
        asked = one_for_both(after="a-ā", before="ic",
                             wants="pūrvasavarṇa")
        self.assertEqual(asked.sutra, "")
        unasked = one_for_both(after="a-ā", before="ic")
        self.assertEqual(unasked.sutra, "6.1.104")
        self.assertEqual(unasked.does, "")


class TheLongVowelIsRefusedAndThenGivenBack(unittest.TestCase):
    """
    6.1.102 gives the homogeneous long vowel; 6.1.104 and 6.1.105
    refuse it in two cases; 6.1.106 gives it back in the corpus for
    one of them. Three rules deep, and the last needs the corpus.
    """

    def test_the_giving_rule_answers_where_nothing_refuses(self):
        answer = one_for_both(after="ak", before="prathamā-dvitīyā")
        self.assertEqual(answer.sutra, "6.1.102")
        self.assertEqual(answer.does, "pūrvasavarṇa")

    def test_the_two_refusals_name_it(self):
        for code in ("6.1.104", "6.1.105"):
            row = provisions_for(code)[0]
            self.assertTrue(row.refuses, code)
            self.assertEqual(row.blocks, ("6.1.102",), code)

    def test_the_second_refusal_is_undone_in_the_corpus(self):
        plain = one_for_both(after="dīrgha", before="jas-ic")
        self.assertEqual(plain.sutra, "6.1.105")
        self.assertEqual(plain.does, "")

        vedic = one_for_both(after="dīrgha", before="jas-ic",
                             chandasi=True)
        self.assertEqual(vedic.sutra, "6.1.106")
        self.assertTrue(vedic.optional)
        self.assertEqual(vedic.blocked_by, ("6.1.105",))

    def test_and_the_n_of_sas_depends_on_which_long_vowel_it_is(self):
        """
        तस्मात् — the न् follows only the long vowel 6.1.102 gave.
        गाः पश्य has a long vowel from 6.1.93 and keeps its स्.
        """
        answer = one_for_both(after="pūrvasavarṇa-dīrgha",
                              before="śas", result="puṃs")
        self.assertEqual(answer.sutra, "6.1.103")
        self.assertEqual(answer.gives, "n")
        self.assertEqual(
            one_for_both(after="o", before="śas", result="puṃs").sutra,
            "")


class AnAcaryaCanBeWhatTellsTwoRulesApart(unittest.TestCase):
    """
    6.1.91 and 6.1.92 name the same preverb and the same ऋ-initial
    root. Only आपिशलि's name, and the kind of root, separate them.
    """

    def test_only_one_row_here_names_a_teacher(self):
        named = [(r.sutra, r.teacher) for r in EKADESA_TABLE
                 if r.teacher]
        self.assertEqual(named, [("6.1.92", "Āpiśali")])

    def test_it_is_out_of_reach_until_the_teacher_is_named(self):
        self.assertEqual(
            one_for_both(after="upasarga-a",
                         before="ṛ-sup-dhātu").sutra, "")

    def test_and_reachable_once_he_is(self):
        answer = one_for_both(after="upasarga-a",
                              before="ṛ-sup-dhātu", teacher="Āpiśali")
        self.assertEqual(answer.sutra, "6.1.92")
        self.assertTrue(answer.optional)
        self.assertEqual(answer.teacher, "Āpiśali")

    def test_the_unattributed_rule_is_not_a_choice(self):
        answer = one_for_both(after="upasarga-a", before="ṛ-dhātu")
        self.assertEqual(answer.sutra, "6.1.91")
        self.assertFalse(answer.optional)

    def test_the_note_says_the_name_adds_nothing_but_respect(self):
        self.assertIn("पूजार्थम्", provisions_for("6.1.92")[0].why)


class TheSectionIsWhereItSaysItIs(unittest.TestCase):
    def test_the_rows_cover_everything_but_the_four_held_elsewhere(self):
        held = sorted(r.sutra for r in EKADESA_TABLE)
        expected = sorted("6.1.%d" % n for n in range(84, 115)
                          if "6.1.%d" % n not in HELD_ELSEWHERE)
        self.assertEqual(held, expected)

    def test_each_gap_belongs_to_the_module_that_owns_it(self):
        for code, module in HELD_ELSEWHERE.items():
            self.assertTrue(REGISTRY.has(code), code)
            self.assertEqual(REGISTRY.get(code).apply.__module__,
                             module, code)
            self.assertEqual(provisions_for(code), (), code)

    def test_the_pada_is_contiguous_through_the_section(self):
        for n in range(1, 115):
            self.assertTrue(REGISTRY.has("6.1.%d" % n), n)

    def test_every_rule_here_is_registered_against_this_resolver(self):
        for row in EKADESA_TABLE:
            self.assertEqual(REGISTRY.get(row.sutra).apply.__name__,
                             "one_for_both", row.sutra)


class NothingAnswersByDefault(unittest.TestCase):
    def test_an_unreached_question_gets_nothing(self):
        answer = one_for_both(after="hal", before="hal")
        self.assertEqual(answer.sutra, "")
        self.assertEqual(answer.does, "")

    def test_and_the_message_says_what_the_heading_is_for(self):
        self.assertIn("6.1.84",
                      one_for_both(after="hal", before="hal").why)


class EveryRowCarriesItsEvidence(unittest.TestCase):
    def test_each_note_has_something_in_it(self):
        for row in EKADESA_TABLE:
            self.assertGreater(len(row.why), 120, row.sutra)

    def test_the_registered_notes_are_read_off_these_rows(self):
        for row in EKADESA_TABLE:
            registered = REGISTRY.get(row.sutra).notes
            opening = " ".join(
                row.why.split("\\n\\n")[0].split()).replace("**", "")
            flattened = " ".join(registered.split()).replace("**", "")
            self.assertIn(opening[:60], flattened, row.sutra)


class WhatIsNotCodifiedYet(unittest.TestCase):
    def test_the_module_names_the_kind_and_not_the_sound(self):
        """
        `one_for_both` says *guṇa*, not *ए*. Which actual vowel
        results is 1.1.50's स्थानेऽन्तरतमः and the guṇa tables, which
        1.1.2 and `adesa` hold — so this module must not be found
        answering with a sound.
        """
        self.assertTrue(REGISTRY.has("1.1.50"))
        answer = one_for_both(after="a-ā", before="ac")
        self.assertEqual(answer.does, "guṇa")
        self.assertEqual(answer.gives, "")

    def test_the_prakrtibhava_run_answers_from_another_module(self):
        self.assertEqual(provisions_for("6.1.115"), ())
        self.assertEqual(REGISTRY.get("6.1.115").apply.__module__,
                         "src.astadhyayi.prakrtibhava")


if __name__ == "__main__":
    unittest.main()
