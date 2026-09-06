# -*- coding: utf-8 -*-
"""
Tests for 6.2.1–63 — the first member keeping its own accent.

Three things carry the section.

**प्रकृत्या preserves rather than places.** One rule answers three
different accentuations, because which syllable of the first member
carries the accent was settled by some rule of 6.1 and this section
only declines to silence it. A resolver that reported a PLACE here
would be inventing one.

**The section is arranged by the second member.** Sixty-three sūtras
and almost every one names the word that must FOLLOW, with a sense
added. So the score has to weight the second member above the first,
and a rule's own counter-examples are what show the sense biting.

**And one rule puts two accents at once.** 6.2.51, with the same
word युगपत् 6.1.200 used, and against the same paribhāṣā.
"""

from __future__ import annotations

import unittest

import src.astadhyayi.rules  # noqa: F401 — populates the registry
from src.astadhyayi.purvapada_svara import (
    PRAKRTYA_RUN, PURVAPADA_RUN, PURVAPADA_TABLE, TATPURUSA_KINDS,
    WHAT_IT_EXCEPTS, first_member, prakrtya_run, provisions_for)
from src.astadhyayi.sutra import REGISTRY

def _order(sutra_id):
    return tuple(int(p) for p in sutra_id.split("."))


TATPURUSA = "tatpuruṣa"


def _order(sutra_id):
    return tuple(int(p) for p in sutra_id.split("."))


class TheWholePadaIsAnExceptionToOneRule(unittest.TestCase):
    def test_the_rule_it_excepts_is_codified(self):
        self.assertTrue(REGISTRY.has("6.1.223"))

    def test_and_the_opening_note_says_so_in_the_vrttis_words(self):
        self.assertIn(WHAT_IT_EXCEPTS, provisions_for("6.2.1")[0].why)

    def test_it_names_both_rules_that_would_otherwise_silence_it(self):
        why = provisions_for("6.2.1")[0].why
        for cited in ("6.1.223", "6.1.158"):
            self.assertIn(cited, why, cited)
            self.assertTrue(REGISTRY.has(cited), cited)

    def test_nothing_answers_by_default_and_the_message_says_why(self):
        answer = first_member(uttarapada="hasta")
        self.assertEqual(answer.sutra, "")
        self.assertEqual(answer.keeps, "")
        self.assertIn("6.1.223", answer.why)


class TwoWordsOfOneSutraHaveTwoDifferentReaches(unittest.TestCase):
    """
    प्रकृत्या stops at 6.2.63, where 6.2.64's आदिरुदात्तः takes over
    the placement; पूर्वपदम् runs on to 6.2.110, where 6.2.111's
    उत्तरपदादिः takes the rest of the pāda.
    """

    def test_the_two_runs_open_together_and_close_apart(self):
        self.assertEqual(PRAKRTYA_RUN[0], PURVAPADA_RUN[0])
        self.assertNotEqual(PRAKRTYA_RUN[1], PURVAPADA_RUN[1])

    def test_the_inner_run_is_what_this_table_holds(self):
        held = sorted(r.sutra for r in PURVAPADA_TABLE)
        first, last = (int(s.split(".")[2]) for s in PRAKRTYA_RUN)
        self.assertEqual(held,
                         sorted("6.2.%d" % n
                                for n in range(first, last + 1)))

    def test_the_report_carries_both_and_what_they_except(self):
        answer = prakrtya_run()
        self.assertEqual(answer.sutra, "6.2.1")
        self.assertIn(PRAKRTYA_RUN[1], answer.why)
        self.assertIn(PURVAPADA_RUN[1], answer.why)
        self.assertIn(WHAT_IT_EXCEPTS, answer.why)


class PrakrtyaPreservesAndDoesNotPlace(unittest.TestCase):
    def test_almost_every_row_preserves(self):
        placing = [(r.sutra, r.keeps) for r in PURVAPADA_TABLE
                   if r.keeps != "prakṛti"]
        self.assertEqual(placing,
                         [("6.2.27", "ādi"), ("6.2.28", "ādi"),
                          ("6.2.51", "ādi-anta")])

    def test_the_answer_says_preserved_and_names_no_syllable(self):
        answer = first_member(samasa="bahuvrīhi")
        self.assertEqual(answer.keeps, "prakṛti")
        self.assertEqual(answer.sutra, "6.2.1")

    def test_the_note_says_the_one_rule_answers_three_placements(self):
        """
        कार्ष्ण is first-accented, अध्यापक middle-accented and
        ब्रह्मचारिन् end-accented, and 6.2.1 covers all three
        because it changes nothing.
        """
        why = provisions_for("6.2.1")[0].why
        for form in ("कार्ष्णोत्तरासङ्गाः", "अध्यापकपुत्रः",
                     "ब्रह्मचारिपरिस्कन्दः"):
            self.assertIn(form, why, form)

    def test_and_the_second_rule_says_it_again_of_three_forms(self):
        why = provisions_for("6.2.2")[0].why
        self.assertIn("6.1.213", why)
        self.assertIn("6.1.197", why)


class TheFirstPlacingRuleStandsBeforeItsHeading(unittest.TestCase):
    """
    6.2.27 आदिः प्रत्येनसि places an accent thirty-seven sūtras
    before 6.2.64 makes placing the ordinary case — and the word
    उदात्त is not in the rule at all.
    """

    def test_it_places_rather_than_preserves(self):
        answer = first_member("kumāra", uttarapada="pratyenas",
                              samasa="karmadhāraya")
        self.assertEqual(answer.sutra, "6.2.27")
        self.assertEqual(answer.keeps, "ādi")

    def test_the_note_says_the_missing_word_has_to_be_supplied(self):
        why = provisions_for("6.2.27")[0].why
        self.assertIn("सामर्थ्याद् वेदितव्यम्", why)

    def test_the_rule_before_it_preserves_for_the_same_word(self):
        answer = first_member("kumāra", samasa="karmadhāraya")
        self.assertEqual(answer.sutra, "6.2.26")
        self.assertEqual(answer.keeps, "prakṛti")

    def test_and_the_disagreement_at_that_rule_reappears_at_the_next(self):
        """
        6.2.26's vṛtti records two readings of how far it reaches,
        and 6.2.28's records that the two give different forms.
        """
        self.assertIn("केचित्", provisions_for("6.2.26")[0].why)
        self.assertIn("एके कुर्वन्ति", provisions_for("6.2.28")[0].why)


class TwoAccentsAtOnceForTheSecondTime(unittest.TestCase):
    def test_it_is_the_only_such_row_here(self):
        both = [r.sutra for r in PURVAPADA_TABLE
                if r.keeps == "ādi-anta"]
        self.assertEqual(both, ["6.2.51"])

    def test_it_names_the_paribhasa_it_breaks(self):
        row = provisions_for("6.2.51")[0]
        self.assertIn("6.1.158", row.blocks)
        self.assertNotIn(row.sutra, row.blocks)

    def test_and_the_earlier_rule_of_the_same_shape_is_codified(self):
        self.assertTrue(REGISTRY.has("6.1.200"))
        from src.astadhyayi.pada_svara import provisions_for as svara

        self.assertEqual(svara("6.1.200")[0].where, "ādi-anta")
        self.assertIn("6.1.200", provisions_for("6.2.51")[0].why)

    def test_both_of_them_say_the_same_word(self):
        self.assertIn("युगपत्", provisions_for("6.2.51")[0].why)


class TheSecondMemberIsWhatDecides(unittest.TestCase):
    def test_most_rows_name_one(self):
        naming = [r for r in PURVAPADA_TABLE
                  if r.uttarapada or r.uttarapada_affix]
        self.assertGreater(len(naming), len(PURVAPADA_TABLE) // 2)

    def test_two_rules_naming_the_same_words_differ_by_sense(self):
        fifteen = provisions_for("6.2.15")[0]
        sixteen = provisions_for("6.2.16")[0]
        self.assertEqual(fifteen.uttarapada, sixteen.uttarapada)
        self.assertNotEqual(fifteen.result, sixteen.result)

    def test_and_each_answers_only_in_its_own_sense(self):
        self.assertEqual(
            first_member(uttarapada="sukha", result="hita",
                         samasa=TATPURUSA).sutra, "6.2.15")
        self.assertEqual(
            first_member(uttarapada="sukha", result="prīti",
                         samasa=TATPURUSA).sutra, "6.2.16")

    def test_a_sense_neither_names_reaches_neither(self):
        self.assertEqual(
            first_member(uttarapada="sukha", result="gamana",
                         samasa=TATPURUSA).sutra, "")

    def test_the_sense_is_what_separates_the_section_from_6_1_223(self):
        """
        पति with lordship is 6.2.18's; पति as a husband is not, and
        falls back to the compound accent.
        """
        self.assertEqual(
            first_member(uttarapada="pati", result="aiśvarya",
                         samasa=TATPURUSA).sutra, "6.2.18")
        self.assertEqual(
            first_member(uttarapada="pati", samasa=TATPURUSA).sutra, "")


class ARefusalNamesWhatItTakesTheAccentFrom(unittest.TestCase):
    def test_there_is_one_and_it_names_the_rule_before_it(self):
        refusing = [r for r in PURVAPADA_TABLE if r.refuses]
        self.assertEqual([r.sutra for r in refusing], ["6.2.19"])
        self.assertEqual(refusing[0].blocks, ("6.2.18",))

    def test_it_reports_no_accent_at_all(self):
        answer = first_member("bhū", uttarapada="pati",
                              result="aiśvarya", samasa=TATPURUSA)
        self.assertEqual(answer.sutra, "6.2.19")
        self.assertEqual(answer.keeps, "")
        self.assertEqual(answer.blocked_by, ("6.2.18",))

    def test_and_it_does_not_govern_what_it_excepts(self):
        elsewhere = first_member("gṛha", uttarapada="pati",
                                 result="aiśvarya", samasa=TATPURUSA)
        self.assertEqual(elsewhere.sutra, "6.2.18")
        self.assertEqual(elsewhere.keeps, "prakṛti")

    def test_one_more_word_is_given_the_accent_back_as_a_choice(self):
        answer = first_member("bhuvana", uttarapada="pati",
                              result="aiśvarya", samasa=TATPURUSA)
        self.assertEqual(answer.sutra, "6.2.20")
        self.assertTrue(answer.optional)


class SevenKindsOfFirstMemberAreDescribedNotListed(unittest.TestCase):
    def test_there_are_seven(self):
        self.assertEqual(len(TATPURUSA_KINDS), 7)

    def test_three_of_them_are_case_endings(self):
        cases = {"tṛtīyā", "saptamī", "dvitīyā"}
        self.assertTrue(cases.issubset(set(TATPURUSA_KINDS)))

    def test_each_reaches_the_rule(self):
        for kind in TATPURUSA_KINDS:
            self.assertEqual(
                first_member(kind=kind, samasa=TATPURUSA).sutra,
                "6.2.2", kind)

    def test_a_kind_it_does_not_name_reaches_nothing(self):
        self.assertEqual(
            first_member(kind="ṣaṣṭhī", samasa=TATPURUSA).sutra, "")

    def test_it_is_the_only_row_of_that_shape(self):
        with_kinds = [r.sutra for r in PURVAPADA_TABLE if r.kinds]
        self.assertEqual(with_kinds, ["6.2.2"])


class WhatARuleExceptsIsHeldSeparately(unittest.TestCase):
    def test_five_rows_except_something_from_their_own_class(self):
        excepting = [(r.sutra, r.excludes) for r in PURVAPADA_TABLE
                     if r.excludes]
        self.assertEqual(excepting,
                         [("6.2.3", ("eta",)),
                          ("6.2.32", ("kāla",)),
                          ("6.2.46", ("niṣṭhā",)),
                          ("6.2.50", ("tu",)),
                          ("6.2.52", ("iganta",))])

    def test_each_exception_is_one_word_and_not_a_class(self):
        """
        A rule of this section that excepts, excepts by NAME: एत,
        काल, निष्ठा, तु, इगन्त. None of the five is a gaṇa, so
        none of them can quietly grow.
        """
        for row in PURVAPADA_TABLE:
            if row.excludes:
                self.assertEqual(len(row.excludes), 1, row.sutra)

    def test_the_excepted_word_takes_the_rule_away(self):
        self.assertEqual(
            first_member("varṇa", uttarapada="varṇa",
                         samasa=TATPURUSA).sutra, "6.2.3")
        self.assertEqual(
            first_member("varṇa", uttarapada="eta",
                         samasa=TATPURUSA).sutra, "")

    def test_and_each_such_rule_records_the_form_it_keeps_out(self):
        for code in ("6.2.3", "6.2.46", "6.2.50"):
            self.assertGreater(len(provisions_for(code)[0].keeps_out),
                               10, code)


class TheOptionalRulesClusterAtTheEnd(unittest.TestCase):
    """
    6.2.54 to 6.2.63 are almost all optional, and the ones before
    them almost none. Worth pinning: an option in this section means
    the compound accent stands on the other side.
    """

    def test_the_options_are_where_they_are(self):
        optional = [int(r.sutra.split(".")[2])
                    for r in PURVAPADA_TABLE if r.optional]
        self.assertGreaterEqual(min(n for n in optional if n > 31), 54)
        self.assertEqual(sorted(optional)[-1], 63)

    def test_each_of_the_last_ten_is_a_choice(self):
        for n in range(54, 64):
            self.assertTrue(provisions_for("6.2.%d" % n)[0].optional, n)

    def test_and_the_answer_reports_it(self):
        self.assertTrue(first_member("īṣad").optional)


class TheSectionIsWhereItSaysItIs(unittest.TestCase):
    def test_every_rule_here_is_registered_against_this_resolver(self):
        for row in PURVAPADA_TABLE:
            self.assertEqual(REGISTRY.get(row.sutra).apply.__name__,
                             "first_member", row.sutra)

    def test_the_pada_is_contiguous_as_far_as_it_goes(self):
        for n in range(1, 64):
            self.assertTrue(REGISTRY.has("6.2.%d" % n), n)

    def test_no_row_names_itself_on_what_it_displaces(self):
        for row in PURVAPADA_TABLE:
            self.assertNotIn(row.sutra, row.blocks, row.sutra)


class EveryRowCarriesItsEvidence(unittest.TestCase):
    def test_each_note_has_something_in_it(self):
        for row in PURVAPADA_TABLE:
            self.assertGreater(len(row.why), 100, row.sutra)

    def test_the_registered_notes_are_read_off_these_rows(self):
        for row in PURVAPADA_TABLE:
            registered = REGISTRY.get(row.sutra).notes
            opening = " ".join(
                row.why.split("\\n\\n")[0].split()).replace("**", "")
            flattened = " ".join(registered.split()).replace("**", "")
            self.assertIn(opening[:60], flattened, row.sutra)


class WhatIsNotCodifiedYet(unittest.TestCase):
    def test_the_module_names_no_syllable(self):
        """
        `first_member` says the accent is PRESERVED. Which syllable
        has it was settled in 6.1, and `pada_svara` holds those
        rules — so this module must not be found naming one.
        """
        answer = first_member(samasa="bahuvrīhi")
        self.assertEqual(answer.keeps, "prakṛti")
        self.assertNotIn("ādi", answer.keeps)

    def test_the_run_that_follows_this_one_landed(self):
        """
        6.2.64 आदिरुदात्तः is codified now, and what it turns
        into is worth more than the debt was: 6.2.1's प्रकृत्या and
        6.2.64's आदिः are two PLACEMENT words under one scope word,
        and the पूर्वपद that carries into both outlives them
        both.
        """
        from src.astadhyayi.purvapada_udatta import ADI_RUN

        self.assertTrue(REGISTRY.has("6.2.64"))
        self.assertEqual(provisions_for("6.2.64"), ())
        self.assertEqual(ADI_RUN[0], "6.2.64")
        self.assertEqual(_order(ADI_RUN[0])[2],
                         _order(PRAKRTYA_RUN[1])[2] + 1)

    def test_and_the_second_member_run_takes_over_from_it(self):
        """
        6.2.111 उत्तरपदादिः takes the SECOND member and the whole
        rest of the pāda — **आ पादपरिसमाप्तेः**. The debt is
        collected, and what the two scope-words now have to show is
        that they meet: पूर्वपदम् closing at 6.2.110 and उत्तरपदम्
        opening at 6.2.111, with no sūtra belonging to neither.
        """
        from src.astadhyayi.uttarapada_svara import UTTARAPADA_RUN

        self.assertTrue(REGISTRY.has("6.2.111"))
        self.assertEqual(PURVAPADA_RUN[1], "6.2.110")
        self.assertEqual(_order(UTTARAPADA_RUN[0])[2],
                         _order(PURVAPADA_RUN[1])[2] + 1)
        self.assertEqual(UTTARAPADA_RUN[1], "6.2.199")

    def test_and_the_two_rules_these_notes_lean_on_have_landed(self):
        """
        6.2.139 गतिकारकोपपदात् कृत् is what makes ब्रह्मचारिन्
        end-accented at 6.2.1, and 6.2.144 is what 6.2.47 and
        6.2.49 are stated against. Both are codified now, so each
        citation is checked by asking the rule — and the two answer
        differently, 6.2.139 leaving the कृदन्त its own accent and
        6.2.144 moving it to the end.
        """
        from src.astadhyayi.uttarapada_svara import second_member

        self.assertIn("6.2.139", provisions_for("6.2.2")[0].why)
        self.assertIn("6.2.144", provisions_for("6.2.49")[0].blocks)
        kept = second_member(affix="kṛt", purvapada_gana="gati",
                             samasa="tatpuruṣa")
        self.assertEqual((kept.sutra, kept.where),
                         ("6.2.139", "prakṛti"))
        moved = second_member(affix="ghañ", purvapada_gana="gati")
        self.assertEqual((moved.sutra, moved.where),
                         ("6.2.144", "anta"))


if __name__ == "__main__":
    unittest.main()
