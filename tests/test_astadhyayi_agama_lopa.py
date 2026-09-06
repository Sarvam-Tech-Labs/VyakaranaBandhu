# -*- coding: utf-8 -*-
"""
Tests for 6.1.58–71 — four kinds of operation in one stretch.

The stretch is worth testing for three things it does that no other
part of the project has done.

**A निपातन and an आदेश one rule apart, and the vṛtti argues which is
which.** 6.1.60 gives शीर्षन् in the Veda and refuses to call it a
substitute — शिरस् is used there too, so neither stands in for the
other. 6.1.61 gives the same शीर्षन् before a य-taddhita and DOES
call it a substitute, arguing the base in from the affix. The table
has to hold that difference or both rules read alike.

**A यथासंख्यम् pairing.** 6.1.63 lists thirteen stems and thirteen
substitutes and pairs them off in order. Held as a mapping, a stem
cannot lose its partner; held as two tuples, it silently can.

**And an ordering argued from where a word STANDS in the rule.**
6.1.66 puts लोप first so that its removal happens before 6.1.67's.
"""

from __future__ import annotations

import unittest

import src.astadhyayi.rules  # noqa: F401 — populates the registry
from src.astadhyayi.agama_lopa import (
    CHANGE_TABLE, PADADI, PADADI_VARTIKA, WHY_THE_HAL_IS_STATED,
    operates, provisions_for, stands_for)
from src.astadhyayi.sutra import REGISTRY

#: The two inside the run that belong to another module.
HELD_ELSEWHERE = ("6.1.64", "6.1.65")


class TheStretchIsWhereItSaysItIs(unittest.TestCase):
    def test_it_covers_everything_but_the_two_held_elsewhere(self):
        held = sorted(row.sutra for row in CHANGE_TABLE)
        expected = sorted("6.1.%d" % n
                          for n in list(range(58, 64)) + list(range(66, 72)))
        self.assertEqual(held, expected)

    def test_the_two_gaps_are_codified_in_the_module_that_owns_them(self):
        for code in HELD_ELSEWHERE:
            self.assertTrue(REGISTRY.has(code), code)
            self.assertEqual(REGISTRY.get(code).apply.__module__,
                             "src.astadhyayi.anga", code)
            self.assertEqual(provisions_for(code), (), code)

    def test_every_rule_of_the_stretch_is_registered_here(self):
        for row in CHANGE_TABLE:
            self.assertEqual(REGISTRY.get(row.sutra).apply.__name__,
                             "operates", row.sutra)

    def test_the_pada_is_contiguous_through_it(self):
        for n in range(58, 72):
            self.assertTrue(REGISTRY.has("6.1.%d" % n), n)


class FourKindsOfOperationInOneStretch(unittest.TestCase):
    def test_all_four_are_present(self):
        kinds = {row.does for row in CHANGE_TABLE}
        self.assertEqual(kinds, {"āgama", "ādeśa", "lopa", "nipātana"})

    def test_each_row_says_which_kind_it_is(self):
        for row in CHANGE_TABLE:
            self.assertTrue(row.does, row.sutra)

    def test_an_augment_reports_what_it_adds_and_removes_nothing(self):
        answer = operates("sṛj", before="jhal-akit")
        self.assertEqual(answer.does, "āgama")
        self.assertEqual(answer.gives, "am")
        self.assertEqual(answer.drops, "")

    def test_a_removal_reports_what_it_takes_and_adds_nothing(self):
        answer = operates(before="val")
        self.assertEqual(answer.does, "lopa")
        self.assertEqual(answer.drops, "v-or-y")
        self.assertEqual(answer.gives, "")

    def test_asking_for_one_kind_does_not_return_another(self):
        self.assertEqual(operates(before="val", wants="āgama").sutra, "")
        self.assertEqual(operates(before="val", wants="lopa").sutra,
                         "6.1.66")

    def test_and_asking_for_a_kind_no_rule_here_does_returns_nothing(self):
        self.assertEqual(operates(before="val", wants="saṃjñā").sutra, "")


class ANipatanaAndAnAdesaOneRuleApart(unittest.TestCase):
    """
    The pair the stretch is worth reading for. Same word, same shape,
    two different kinds of thing — and each vṛtti gives its own kind
    of evidence.
    """

    def test_the_vedic_one_is_a_nipatana(self):
        answer = operates("śiras", chandasi=True)
        self.assertEqual(answer.sutra, "6.1.60")
        self.assertEqual(answer.does, "nipātana")
        self.assertTrue(answer.nipatana)

    def test_and_the_taddhita_one_is_an_adesa(self):
        answer = operates("śiras", before="ya-taddhita")
        self.assertEqual(answer.sutra, "6.1.61")
        self.assertEqual(answer.does, "ādeśa")
        self.assertFalse(answer.nipatana)

    def test_they_give_the_same_shape(self):
        self.assertEqual(provisions_for("6.1.60")[0].adesa, "śīrṣan")
        self.assertEqual(provisions_for("6.1.61")[0].adesa, "śīrṣan")

    def test_the_first_note_argues_it_is_not_a_substitute(self):
        why = provisions_for("6.1.60")[0].why
        self.assertIn("न पुनरयमादेशः", why)
        self.assertIn("प्रयुज्यत एव", why)

    def test_the_second_note_argues_the_base_into_the_rule(self):
        why = provisions_for("6.1.61")[0].why
        self.assertIn("आक्षिपति", why)

    def test_the_third_gives_a_different_shape_for_a_reason(self):
        """
        6.1.62 gives शीर्ष without the न्, because with the न् there
        6.4.167 would hold it in place and spoil the form.
        """
        self.assertEqual(operates("śiras", before="ac-taddhita").adesa,
                         "śīrṣa")
        self.assertIn("6.4.167", provisions_for("6.1.62")[0].why)


class TheThirteenArePairedOffInOrder(unittest.TestCase):
    """
    यथासंख्यम्. Thirteen names and thirteen substitutes, and the
    pairing is what the rule states — so it is held as a mapping,
    where a name cannot lose its partner.
    """

    def test_there_are_thirteen_of_them(self):
        self.assertEqual(len(PADADI), 13)

    def test_no_stem_is_left_without_a_substitute(self):
        for stem, substitute in PADADI.items():
            self.assertTrue(substitute, stem)

    def test_the_answer_depends_on_which_stem_asked(self):
        for stem, substitute in PADADI.items():
            answer = operates(stem, before="śas-prabhṛti")
            self.assertEqual(answer.sutra, "6.1.63", stem)
            self.assertEqual(answer.adesa, substitute, stem)

    def test_the_row_holds_no_substitute_of_its_own(self):
        """
        A single column could not carry thirteen answers, and
        splitting the rule into thirteen rows would make one sūtra
        look like thirteen. The flag is what keeps both honest.
        """
        row = provisions_for("6.1.63")[0]
        self.assertTrue(row.by_mapping)
        self.assertEqual(row.adesa, "")

    def test_the_vartika_adds_three_more_and_they_are_kept_apart(self):
        self.assertEqual(len(PADADI_VARTIKA), 3)
        self.assertEqual(set(PADADI) & set(PADADI_VARTIKA), set())
        self.assertEqual(stands_for("sānu"), "snu")

    def test_a_stem_on_neither_list_gets_nothing(self):
        self.assertEqual(stands_for("hasta"), "")
        self.assertEqual(operates("hasta", before="śas-prabhṛti").sutra,
                         "")

    def test_the_note_records_that_the_scope_is_disputed(self):
        """
        Some carry छन्दसि down and confine the rule to the corpus;
        others want it everywhere and quote a verse for it; a third
        party carries अन्यतरस्याम् down instead. The vṛtti reports
        all three and settles none, and the note has to say so.
        """
        why = provisions_for("6.1.63")[0].why
        self.assertIn("केचिदत्र", why)
        self.assertIn("अपरे पुनर्", why)


class AWordsPlaceInARuleFixesAnOrder(unittest.TestCase):
    def test_the_two_removals_are_distinct_rules(self):
        self.assertEqual(operates(before="val").sutra, "6.1.66")
        self.assertEqual(operates(before="apṛkta").sutra, "6.1.67")

    def test_they_take_different_things(self):
        self.assertNotEqual(provisions_for("6.1.66")[0].drops,
                            provisions_for("6.1.67")[0].drops)

    def test_the_note_gives_the_argument_and_the_forms_that_decide_it(self):
        why = provisions_for("6.1.66")[0].why
        self.assertIn("पूर्वं लोपग्रहणं किम्", why)
        self.assertIn("कण्डूः", why)

    def test_the_wider_removal_dropped_the_word_dhatoh(self):
        """
        6.1.66 reaches a non-root as well — गौधेरः and पचेरन् — and
        the vṛtti says exactly why: the धातु of 6.1.64 was itself a
        fresh mention, so what 6.1.8 supplied has lapsed.
        """
        self.assertIn("धातोरधातोश्च", provisions_for("6.1.66")[0].why)


class AWordRepeatedEarlierProvesItIsAbsentLater(unittest.TestCase):
    """
    The inverse of the idle-word argument. 6.1.68 says अपृक्तम्,
    which 6.1.67 had already supplied; 6.1.69 reads that redundancy
    as proof that the word stops at 6.1.68.
    """

    def test_the_note_states_the_argument(self):
        self.assertIn("अपृक्तमिति नाधिक्रियते",
                      provisions_for("6.1.69")[0].why)

    def test_and_names_the_form_that_needs_it(self):
        self.assertIn("हे कुण्ड", provisions_for("6.1.69")[0].why)

    def test_the_two_rules_have_different_conditions_on_what_precedes(self):
        sixty_eight = provisions_for("6.1.68")[0]
        sixty_nine = provisions_for("6.1.69")[0]
        self.assertEqual(sixty_eight.after, ("hal", "ṅī", "āp"))
        self.assertEqual(sixty_nine.after, ("eṅ", "hrasva"))

    def test_each_answers_only_where_its_own_condition_holds(self):
        self.assertEqual(operates(before="su-ti-si", after="hal").sutra,
                         "6.1.68")
        self.assertEqual(operates(before="su-ti-si", after="eṅ").sutra, "")
        self.assertEqual(operates(before="sambuddhi", after="eṅ").sutra,
                         "6.1.69")
        self.assertEqual(operates(before="sambuddhi", after="hal").sutra,
                         "")


class TheVerseArgumentIsRecordedWithItsForms(unittest.TestCase):
    """
    6.1.68's vṛtti sets out in a śloka why the rule is stated at all,
    when 8.2.23's संयोगान्तलोप looks as though it would do the work.
    Four forms decide it, and each names the rule that would fail.
    """

    def test_there_are_four_of_them(self):
        self.assertEqual(len(WHY_THE_HAL_IS_STATED), 4)

    def test_each_names_the_rule_that_would_fail(self):
        for line in WHY_THE_HAL_IS_STATED:
            self.assertRegex(line, r"\d\.\d\.\d+")

    def test_and_the_note_carries_the_verse(self):
        why = provisions_for("6.1.68")[0].why
        self.assertIn("नलोपादिर्न सिध्यति", why)
        self.assertIn("विधीयते", why)

    def test_the_rule_the_verse_argues_against_has_since_landed(self):
        """
        Written as the shortfall, and it did bring someone back.
        8.2.23 संयोगान्तस्य लोपः is what the verse argues
        against, and it is codified now — with its own vṛtti's
        three orderings, which are the same kind of argument.
        """
        self.assertTrue(REGISTRY.has("8.2.23"))


class TheAugmentDisplacesTheGuna(unittest.TestCase):
    def test_the_rule_records_what_it_displaces(self):
        row = provisions_for("6.1.58")[0]
        self.assertEqual(row.blocks, ("7.3.86",))
        self.assertNotIn(row.sutra, row.blocks)

    def test_and_the_rule_displaced_is_not_codified_yet(self):
        """
        The debt written as the exact shortfall. 7.3.86 पुगन्तलघूपधस्य
        च is what the अम् displaces, and it is absent while 7.3.84
        सार्वधातुकार्धधातुकयोः — which was reached ahead for
        नयति — is present. Adding the one this row names should
        bring someone back to it.
        """
        self.assertTrue(REGISTRY.has("7.3.84"))
        # Written as a debt: 7.3.86 पुगन्तलघूपधस्य च was not
        # codified. It has landed with पाद ७.३, so the guṇa the
        # augment displaces can be asked of the engine directly.
        self.assertTrue(REGISTRY.has("7.3.86"))

    def test_the_note_says_it_is_an_apavada_and_not_a_second_step(self):
        self.assertIn("लघूपधगुणापवादोऽयममागमः",
                      provisions_for("6.1.58")[0].why)

    def test_the_answer_reports_the_displaced_rule_by_its_own_number(self):
        self.assertEqual(operates("sṛj", before="jhal-akit").blocked_by,
                         ("7.3.86",))


class TheOptionalAugmentIsToldApartByAnAccent(unittest.TestCase):
    """
    6.1.58 and 6.1.59 share their affix condition exactly. The first
    names two roots; the second names no root at all and turns on
    what the धातुपाठ marked the root with.
    """

    def test_they_share_the_affix_condition(self):
        self.assertEqual(provisions_for("6.1.58")[0].before,
                         provisions_for("6.1.59")[0].before)

    def test_but_only_one_of_them_names_roots(self):
        self.assertTrue(provisions_for("6.1.58")[0].of)
        self.assertEqual(provisions_for("6.1.59")[0].of, ())

    def test_the_accent_and_the_penult_are_what_reach_the_second(self):
        answer = operates(before="jhal-akit", upadha="ṛ",
                          accent="anudātta")
        self.assertEqual(answer.sutra, "6.1.59")
        self.assertTrue(answer.optional)

    def test_the_wrong_accent_reaches_nothing(self):
        self.assertEqual(
            operates(before="jhal-akit", upadha="ṛ",
                     accent="udātta").sutra, "")

    def test_and_the_wrong_penult_reaches_nothing(self):
        self.assertEqual(
            operates(before="jhal-akit", upadha="i",
                     accent="anudātta").sutra, "")

    def test_the_named_roots_still_answer_without_either(self):
        self.assertEqual(operates("dṛś", before="jhal-akit").sutra,
                         "6.1.58")


class TheVedicRuleIsOutOfReachWithoutTheCorpus(unittest.TestCase):
    def test_the_two_vedic_rows_are_the_two_expected(self):
        vedic = [r.sutra for r in CHANGE_TABLE if r.chandasi]
        self.assertEqual(vedic, ["6.1.60", "6.1.70"])

    def test_neither_answers_in_ordinary_speech(self):
        self.assertEqual(operates("śiras").sutra, "")
        self.assertEqual(operates(before="śi").sutra, "")

    def test_bahulam_is_recorded_only_where_the_rule_says_it(self):
        self.assertTrue(operates(before="śi", chandasi=True).bahulam)
        self.assertFalse(operates("śiras", chandasi=True).bahulam)


class NothingAnswersByDefault(unittest.TestCase):
    def test_an_unreached_question_gets_nothing(self):
        answer = operates(before="ktvā")
        self.assertEqual(answer.sutra, "")
        self.assertEqual(answer.does, "")

    def test_and_the_message_says_where_the_last_heading_stopped(self):
        self.assertIn("6.1.57", operates(before="ktvā").why)


class EveryRowCarriesItsEvidence(unittest.TestCase):
    def test_each_note_has_something_in_it(self):
        for row in CHANGE_TABLE:
            self.assertGreater(len(row.why), 120, row.sutra)

    def test_every_row_records_what_its_conditions_keep_out(self):
        """
        A rule with a condition and no counter-example is a rule
        nobody checked. Two rows here genuinely have none — 6.1.61
        and 6.1.62 turn on the shape of the following affix and the
        vṛtti gives one between them — so the bar is most of them.
        """
        with_counters = [r for r in CHANGE_TABLE if r.keeps_out]
        self.assertGreaterEqual(len(with_counters), 9)

    def test_the_registered_notes_are_read_off_these_rows(self):
        for row in CHANGE_TABLE:
            registered = REGISTRY.get(row.sutra).notes
            opening = " ".join(
                row.why.split("\\n\\n")[0].split()).replace("**", "")
            flattened = " ".join(registered.split()).replace("**", "")
            self.assertIn(opening[:60], flattened, row.sutra)


class WhatIsNotCodifiedYet(unittest.TestCase):
    def test_the_module_still_does_not_build_the_finished_form(
            self):
        """
        Half of this debt is paid: 6.4.8 is codified now, and the
        lengthening that makes राजा out of राजन् can be asked. The
        other half stands — the संयोगान्त rules that drop the न्
        are not — and this module still only says which rule acts,
        never what the word comes out as.
        """
        from src.astadhyayi.anga_dirgha import to_the_stem

        self.assertTrue(REGISTRY.has("6.4.8"))
        self.assertEqual(
            to_the_stem(before="sarvanāmasthāna",
                        result="n-anta").sutra, "6.4.8")
        # 8.2.23 has landed since, so the cluster's loss can be
        # asked of the registry. What has not changed is this
        # module: it names the operation and does not build the
        # word, and the debt has moved from the rule to that.
        self.assertTrue(REGISTRY.has("8.2.23"))
        answer = operates(before="su-ti-si", after="hal")
        self.assertEqual(answer.drops, "apṛkta-hal")
        self.assertNotIn("rājā", str(answer))

    def test_the_whole_pada_landed_around_this_stretch(self):
        """
        Both halves of the debt this test was written as are paid.
        6.1.72 संहितायाम् and 6.1.158 अनुदात्तं पदमेकवर्जम्
        are codified, and the pāda is contiguous from 6.1.1 to
        6.1.223. What is left to hold is the boundary: this table
        stops at 6.1.71 and the rules on either side of it belong to
        other modules.
        """
        self.assertTrue(REGISTRY.has("6.1.72"))
        self.assertTrue(REGISTRY.has("6.1.158"))
        for n in range(1, 224):
            self.assertTrue(REGISTRY.has("6.1.%d" % n), n)
        self.assertEqual(provisions_for("6.1.72"), ())
        self.assertEqual(provisions_for("6.1.158"), ())


if __name__ == "__main__":
    unittest.main()
