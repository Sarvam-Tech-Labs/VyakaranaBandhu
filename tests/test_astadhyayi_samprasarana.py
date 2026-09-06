# -*- coding: utf-8 -*-
"""
Tests for 6.1.13–44, the संप्रसारण section.

What is worth testing here is not that thirty-two rows exist. It is
the four things the section actually turns on: that a refusal names
the rule it takes the form away from rather than itself; that a rule
naming a root outright beats one that reaches the same root through a
gaṇa; that an option can both SUPPLY and LOOSEN in one breath; and
that the one rule turning on a state rather than on a base is not
reachable without that state.
"""

from __future__ import annotations

import unittest

import src.astadhyayi.rules  # noqa: F401 — populates the registry
from src.astadhyayi.samprasarana import (
    BALIYAS, CHANDASI_NIPATANA, GRAHYADI, SAMPRASARANA_RUN,
    SAMPRASARANA_TABLE, VACYADI, _how_specific, provisions_for,
    samprasarana_run, vocalises)
from src.astadhyayi.sutra import REGISTRY


def _order(sutra_id):
    return tuple(int(p) for p in sutra_id.split("."))


class TheSectionIsWhatTheVrttiSaysItIs(unittest.TestCase):
    def test_the_heading_runs_where_the_vrtti_bounds_it(self):
        """
        6.1.13's vṛtti names the far end by the words of the rule it
        stops at, not by a number: विभाषा परेः. That is 6.1.44, and
        the constant has to agree with the note that cites it.
        """
        self.assertEqual(SAMPRASARANA_RUN, ("6.1.13", "6.1.44"))
        opening = provisions_for("6.1.13")[0]
        self.assertIn("विभाषा परेः इति यावत्", opening.why)

    def test_every_row_falls_inside_that_run(self):
        first, last = (_order(s) for s in SAMPRASARANA_RUN)
        for row in SAMPRASARANA_TABLE:
            self.assertLessEqual(first, _order(row.sutra), row.sutra)
            self.assertLessEqual(_order(row.sutra), last, row.sutra)

    def test_the_run_is_contiguous(self):
        """
        A gap would be a sūtra silently skipped, which is the one
        failure the collation cannot catch on its own.
        """
        first, last = (int(s.split(".")[2]) for s in SAMPRASARANA_RUN)
        for n in range(first, last + 1):
            code = "6.1.%d" % n
            self.assertTrue(provisions_for(code), code)
            self.assertTrue(REGISTRY.has(code), code)

    def test_the_report_names_the_bound_it_was_read_from(self):
        answer = samprasarana_run()
        self.assertEqual(answer.sutra, "6.1.13")
        self.assertIn("6.1.44", answer.why)


class ARefusalNamesWhatItTakesTheFormFrom(unittest.TestCase):
    """
    The standing decision from 2.3.72 onwards: a प्रतिषेध does not
    govern what it excepts. Every refusing row here has to name, on
    `blocks`, the rule that supplies — with THAT rule's number.
    """

    def setUp(self):
        self.refusing = [r for r in SAMPRASARANA_TABLE if r.refuses]

    def test_there_are_refusals_to_check(self):
        self.assertGreaterEqual(len(self.refusing), 6)

    def test_none_of_them_names_itself(self):
        for row in self.refusing:
            self.assertNotIn(row.sutra, row.blocks, row.sutra)

    def test_each_names_a_rule_that_comes_before_it(self):
        """
        A refusal narrows something already stated. Naming a LATER
        rule would mean the table had recorded the dependency the
        wrong way round, which nothing else here would catch.
        """
        for row in self.refusing:
            if row.after_samprasarana:
                # 6.1.37 refuses a SECOND vocalisation wherever one
                # has happened. There is no single supplier to name.
                continue
            self.assertTrue(row.blocks, row.sutra)
            for blocked in row.blocks:
                self.assertLess(_order(blocked), _order(row.sutra),
                                "%s names %s, which comes after it"
                                % (row.sutra, blocked))

    def test_and_every_rule_named_is_one_this_project_has_codified(self):
        for row in self.refusing:
            for blocked in row.blocks:
                self.assertTrue(REGISTRY.has(blocked),
                                "%s names %s, which is not codified"
                                % (row.sutra, blocked))

    def test_all_but_one_of_them_takes_from_a_rule_that_supplies(self):
        """
        The exception is 6.1.44, whose विभाषा narrows a REFUSAL
        rather than a giving rule — and it is the only such row, so
        the shape is worth pinning rather than waving through.
        """
        by_id = {r.sutra: r for r in SAMPRASARANA_TABLE}
        narrows_a_refusal = []
        for row in self.refusing:
            for blocked in row.blocks:
                if by_id[blocked].refuses:
                    narrows_a_refusal.append((row.sutra, blocked))
        self.assertEqual(narrows_a_refusal, [("6.1.44", "6.1.43")])

    def test_a_refusal_is_never_the_answer_to_a_request_for_the_thing(self):
        """
        Asking *which rule gives me संप्रसारण here* must not be
        answered by the rule that takes it away.
        """
        asked = vocalises("vaś", before="yaṅ", wants="samprasāraṇa")
        self.assertEqual(asked.sutra, "")
        unasked = vocalises("vaś", before="yaṅ")
        self.assertEqual(unasked.sutra, "6.1.20")
        self.assertEqual(unasked.does, "")


class ThePrateshedhaDoesNotGovernWhatItExcepts(unittest.TestCase):
    def test_vas_keeps_its_vowel_before_yan_and_loses_it_elsewhere(self):
        """
        6.1.20 न वशः is stated with यङि carrying down. Take the यङ्
        away and 6.1.16 is untouched — उष्टः and उशन्ति are its
        forms, and the refusal has nothing to say about them.
        """
        under_yan = vocalises("vaś", before="yaṅ")
        self.assertEqual(under_yan.sutra, "6.1.20")
        self.assertEqual(under_yan.blocked_by, ("6.1.16",))

        elsewhere = vocalises("vaś", before="ṅit")
        self.assertEqual(elsewhere.sutra, "6.1.16")
        self.assertEqual(elsewhere.does, "samprasāraṇa")

    def test_ven_is_refused_in_the_perfect_and_before_lyap_only(self):
        for affix in ("liṭ", "lyap"):
            self.assertTrue(vocalises("veñ", before=affix).blocked_by,
                            affix)
        self.assertEqual(vocalises("veñ", before="kit").sutra, "6.1.15")

    def test_one_refusal_has_to_reach_two_giving_rules(self):
        """
        6.1.40's vṛtti: before a कित् perfect ending 6.1.15 would take
        the root, and before the rest 6.1.17 would take the copy. So
        the single refusal names both.
        """
        self.assertEqual(vocalises("veñ", before="liṭ").blocked_by,
                         ("6.1.15", "6.1.17"))

    def test_pari_turns_the_refusal_back_into_a_choice(self):
        plain = vocalises("vyeñ", before="lyap")
        self.assertEqual(plain.sutra, "6.1.43")
        self.assertFalse(plain.optional)

        after_pari = vocalises("vyeñ", before="lyap", pre="pari")
        self.assertEqual(after_pari.sutra, "6.1.44")
        self.assertTrue(after_pari.optional)
        self.assertEqual(after_pari.blocked_by, ("6.1.43",))


class ANamedRootBeatsAGana(unittest.TestCase):
    """
    6.1.15 names वच् and स्वप् outright and reaches nine more through
    यजादि. श्वि is one of the nine, and 6.1.30 names it. So 6.1.30
    must be the narrower rule for श्वि and the wider for वच् — the
    same row, two different scores, depending on the root asked.
    """

    def setUp(self):
        self.fifteen = provisions_for("6.1.15")[0]

    def test_svi_is_in_the_gana_and_named_by_the_later_rule(self):
        self.assertIn("śvi", VACYADI)
        self.assertNotIn("śvi", self.fifteen.of)
        self.assertIn("śvi", provisions_for("6.1.30")[0].of)

    def test_the_score_changes_with_the_root_that_asked(self):
        by_name = _how_specific(self.fifteen, "vac")
        by_gana = _how_specific(self.fifteen, "śvi")
        self.assertGreater(by_name, by_gana)

    def test_and_the_narrower_rule_is_the_one_that_answers(self):
        self.assertEqual(vocalises("śvi", before="liṭ").sutra, "6.1.30")
        self.assertEqual(vocalises("vac", before="kit").sutra, "6.1.15")

    def test_svi_still_reaches_the_gana_rule_where_no_rule_names_it(self):
        """
        Before a कित् affix that is not a perfect ending, nothing
        names श्वि, and it falls back to being one of the यजादि.
        """
        self.assertEqual(vocalises("śvi", before="kit").sutra, "6.1.15")


class AnOptionCanSupplyAndLoosenAtOnce(unittest.TestCase):
    """
    6.1.30's उभयत्रविभाषा. Before यङ् nothing reached श्वि at all, so
    the option SUPPLIES; before लिट् 6.1.15 already reached it as a
    यजादि root, so the option LOOSENS. One rule, two jobs, and the
    vṛtti says so in as many words.
    """

    def test_the_vrtti_states_both_halves(self):
        self.assertIn("यङि संप्रसारणमप्राप्तं",
                      provisions_for("6.1.30")[0].why)

    def test_nothing_else_reaches_svi_before_yan(self):
        others = [r.sutra for r in SAMPRASARANA_TABLE
                  if r.sutra != "6.1.30"
                  and "śvi" in (r.of + (VACYADI if r.gana else ()))
                  and "yaṅ" in (r.before, r.also_before)]
        self.assertEqual(others, [])

    def test_but_something_does_reach_it_before_a_kit_affix(self):
        self.assertEqual(vocalises("śvi", before="kit").sutra, "6.1.15")

    def test_both_ways_the_answer_is_the_option(self):
        for affix in ("liṭ", "yaṅ"):
            answer = vocalises("śvi", before=affix)
            self.assertEqual(answer.sutra, "6.1.30", affix)
            self.assertTrue(answer.optional, affix)


class AnIdleWordDropsAnInheritedOption(unittest.TestCase):
    """
    6.1.31 and 6.1.32 share their affix condition exactly. The first
    is a choice, the second is not — and the only thing that makes the
    difference is 6.1.32 repeating a word it already had by
    अनुवृत्ति.
    """

    AFFIX = "ṇau-saṃ-caṅoḥ"

    def test_the_two_rules_share_the_condition(self):
        self.assertEqual(provisions_for("6.1.31")[0].before, self.AFFIX)
        self.assertEqual(provisions_for("6.1.32")[0].before, self.AFFIX)

    def test_but_only_one_of_them_is_a_choice(self):
        self.assertTrue(vocalises("śvi", before=self.AFFIX).optional)
        self.assertFalse(vocalises("hve", before=self.AFFIX).optional)

    def test_and_the_note_says_what_dropped_the_option(self):
        self.assertIn("विभाषेत्यस्य निवृत्त्यर्थम्",
                      provisions_for("6.1.32")[0].why)


class OneRuleTurnsOnAStateAndNotOnABase(unittest.TestCase):
    """
    6.1.37 names no root and no affix. Without the `already` gate it
    would match every question the table is ever asked, and being a
    refusal it would win every one of them.
    """

    def setUp(self):
        self.row = provisions_for("6.1.37")[0]

    def test_it_is_the_only_row_of_its_shape(self):
        gated = [r.sutra for r in SAMPRASARANA_TABLE
                 if r.after_samprasarana]
        self.assertEqual(gated, ["6.1.37"])
        self.assertEqual(self.row.of, ())
        self.assertEqual(self.row.before, "")

    def test_it_is_unreachable_without_the_state(self):
        self.assertEqual(vocalises("vyadh", before="kit").sutra,
                         "6.1.16")

    def test_and_it_wins_once_the_state_holds(self):
        answer = vocalises("vyadh", before="kit", already=True)
        self.assertEqual(answer.sutra, "6.1.37")
        self.assertEqual(answer.does, "")

    def test_the_note_carries_the_argument_for_the_order(self):
        self.assertIn("प्रथमं परस्य यणः क्रियते", self.row.why)


class TheSubstitutesAreNotVocalisations(unittest.TestCase):
    """
    Five rules put a finished form in instead of ordering the
    semivowel to give up its consonant. A question asking for a
    संप्रसारण must not be answered by one of them.
    """

    def setUp(self):
        self.adesa_rows = [r for r in SAMPRASARANA_TABLE if r.adesa]

    def test_the_substitutes_are_five(self):
        self.assertEqual(sorted({r.adesa for r in self.adesa_rows}),
                         ["kī", "pī", "sphī", "v", "śṛ"])

    def test_none_of_them_also_refuses(self):
        for row in self.adesa_rows:
            self.assertFalse(row.refuses, row.sutra)

    def test_the_answer_reports_the_substitute_as_what_it_does(self):
        answer = vocalises("cāy", before="yaṅ")
        self.assertEqual(answer.does, "kī")
        self.assertEqual(answer.adesa, "kī")

    def test_and_asking_for_a_vocalisation_does_not_reach_it(self):
        self.assertEqual(
            vocalises("cāy", before="yaṅ", wants="samprasāraṇa").sutra,
            "")

    def test_but_asking_for_the_substitute_by_name_does(self):
        self.assertEqual(
            vocalises("cāy", before="yaṅ", wants="kī").sutra, "6.1.21")


class ThePreverbSeparatesThreeRulesOnOneRoot(unittest.TestCase):
    """
    श्या is reached three ways: 6.1.24 by a SENSE, 6.1.25 by प्रति,
    6.1.26 by अभि or अव. Each preverb has to pick out its own rule,
    and the sense-rule has to answer where no preverb is given.
    """

    NISTHA = "niṣṭhā"

    def test_the_sense_rule_answers_with_no_preverb(self):
        for sense in ("dravamūrti", "sparśa"):
            answer = vocalises("śyā", before=self.NISTHA, result=sense)
            self.assertEqual(answer.sutra, "6.1.24", sense)

    def test_a_third_sense_reaches_nothing(self):
        self.assertEqual(
            vocalises("śyā", before=self.NISTHA, result="saṃkoca").sutra,
            "")

    def test_prati_reaches_its_own_rule_without_any_sense(self):
        answer = vocalises("śyā", before=self.NISTHA, pre="prati")
        self.assertEqual(answer.sutra, "6.1.25")
        self.assertFalse(answer.optional)

    def test_both_of_the_two_preverbs_of_one_rule_reach_it(self):
        for pre in ("abhi", "ava"):
            answer = vocalises("śyā", before=self.NISTHA, pre=pre)
            self.assertEqual(answer.sutra, "6.1.26", pre)
            self.assertTrue(answer.optional, pre)

    def test_a_preverb_no_rule_names_falls_back_to_the_sense_rule(self):
        answer = vocalises("śyā", before=self.NISTHA, pre="sam",
                           result="dravamūrti")
        self.assertEqual(answer.sutra, "6.1.24")


class ASettledOptionIsMarkedAsOne(unittest.TestCase):
    """
    व्यवस्थितविभाषा is not a free choice: 6.1.27 is settled by WHAT
    is spoken of and 6.1.28 by whether a preverb stands there. Both
    are still options, so the flag has to imply the flag.
    """

    def test_every_settled_option_is_an_option(self):
        for row in SAMPRASARANA_TABLE:
            if row.vyavasthita:
                self.assertTrue(row.optional, row.sutra)

    def test_and_they_are_the_three_the_vrtti_calls_so(self):
        settled = [r.sutra for r in SAMPRASARANA_TABLE if r.vyavasthita]
        self.assertEqual(settled, ["6.1.26", "6.1.27", "6.1.28"])
        for code in settled:
            self.assertIn("विभाष", provisions_for(code)[0].why)


class TheVedicRulesAreOutOfReachWithoutTheCorpus(unittest.TestCase):
    def test_they_answer_nothing_by_default(self):
        for root in ("cāy", "tyaj"):
            self.assertEqual(vocalises(root).sutra, "", root)

    def test_and_hve_falls_back_to_the_rule_that_is_not_vedic(self):
        """
        ह्वे is the one root reached by both a Vedic rule and an
        ordinary one. Outside the corpus 6.1.34 is out of reach and
        6.1.33 answers; name the corpus and the narrower rule takes
        over. That is what the corpus is worth in the score.
        """
        self.assertEqual(vocalises("hve").sutra, "6.1.33")
        self.assertEqual(vocalises("hve", chandasi=True).sutra, "6.1.34")

    def test_but_do_once_the_corpus_is_named(self):
        self.assertEqual(vocalises("hve", chandasi=True).sutra, "6.1.34")
        self.assertEqual(vocalises("cāy", chandasi=True).sutra, "6.1.35")

    def test_bahulam_is_recorded_separately_from_an_option(self):
        """
        बहुलम् is not विभाषा. An option gives two forms for one
        condition; बहुलम् says the corpus is the only evidence for
        whether the rule fired at all.
        """
        answer = vocalises("hve", chandasi=True)
        self.assertTrue(answer.bahulam)
        self.assertFalse(answer.optional)

    def test_the_laid_down_forms_are_nine(self):
        self.assertEqual(len(CHANDASI_NIPATANA), 9)
        answer = vocalises("tyaj", chandasi=True)
        self.assertEqual(answer.sutra, "6.1.36")
        self.assertTrue(answer.nipatana)


class TheVocalisationLandsSomewhere(unittest.TestCase):
    def test_almost_every_rule_works_on_the_root(self):
        elsewhere = [(r.sutra, r.on) for r in SAMPRASARANA_TABLE
                     if r.on != "dhātu"]
        self.assertEqual(elsewhere,
                         [("6.1.17", "abhyāsa"), ("6.1.33", "abhyasta")])

    def test_the_copy_rule_says_so_in_its_answer(self):
        self.assertEqual(vocalises("vac", before="liṭ").on, "abhyāsa")

    def test_and_the_one_that_covers_both_halves_says_that(self):
        self.assertEqual(vocalises("hve").on, "abhyasta")

    def test_a_refusal_reports_no_landing_place_at_all(self):
        self.assertEqual(vocalises("veñ", before="liṭ").on, "")


class TheCompoundRulesAreTheOnlyTwo(unittest.TestCase):
    """
    6.1.13 and 6.1.14 are the only rules in the section conditioned on
    a compound at all, and they differ by nothing but which compound.
    """

    def test_only_two_rows_name_a_following_word(self):
        with_uttarapada = [r.sutra for r in SAMPRASARANA_TABLE
                           if r.uttarapada]
        self.assertEqual(with_uttarapada, ["6.1.13", "6.1.14"])

    def test_the_compound_is_what_tells_them_apart(self):
        self.assertEqual(provisions_for("6.1.13")[0].samasa, "tatpuruṣa")
        self.assertEqual(provisions_for("6.1.14")[0].samasa, "bahuvrīhi")

    def test_the_wrong_compound_reaches_neither(self):
        self.assertEqual(
            vocalises("ṣyaṅ", uttarapada="bandhu",
                      samasa="tatpuruṣa").sutra, "")
        self.assertEqual(
            vocalises("ṣyaṅ", uttarapada="putra",
                      samasa="bahuvrīhi").sutra, "")

    def test_a_following_word_neither_rule_names_reaches_nothing(self):
        self.assertEqual(
            vocalises("ṣyaṅ", uttarapada="kula",
                      samasa="tatpuruṣa").sutra, "")


class TheTwoListsAreDistinct(unittest.TestCase):
    def test_they_overlap_in_nothing(self):
        self.assertEqual(set(VACYADI) & set(GRAHYADI), set())

    def test_the_second_list_takes_a_second_marker(self):
        row = provisions_for("6.1.16")[0]
        self.assertEqual(row.before, "ṅit")
        self.assertEqual(row.also_before, "kit")

    def test_and_the_first_list_takes_only_one(self):
        row = provisions_for("6.1.15")[0]
        self.assertEqual(row.before, "kit")
        self.assertEqual(row.also_before, "")

    def test_a_grahyadi_root_before_a_kit_affix_reaches_its_own_rule(self):
        self.assertEqual(vocalises("grah", before="kit").sutra, "6.1.16")


class NothingAnswersByDefault(unittest.TestCase):
    def test_an_unnamed_root_keeps_its_semivowel(self):
        answer = vocalises("gam", before="kit")
        self.assertEqual(answer.sutra, "")
        self.assertEqual(answer.does, "")

    def test_and_the_message_says_why_rather_than_being_blank(self):
        self.assertIn("6.1.13", vocalises("gam", before="kit").why)

    def test_the_opening_rule_is_not_a_heading(self):
        """
        Every heading the project has met supplies by default. This
        section has none: 6.1.13 is an ordinary rule that happens to
        carry the word the rest are read with.
        """
        self.assertFalse(
            any(getattr(r, "heading", False) for r in SAMPRASARANA_TABLE))


class TheMaximIsCitedWhereItIsUsed(unittest.TestCase):
    def test_the_constant_is_the_words_of_the_maxim(self):
        self.assertIn("बलीयो भवति", BALIYAS)

    def test_and_the_two_rules_that_lean_on_it_quote_it(self):
        for code in ("6.1.31", "6.1.32"):
            why = provisions_for(code)[0].why
            self.assertIn("बलीय", why, code)


class EveryRowCarriesItsEvidence(unittest.TestCase):
    def test_each_note_has_something_in_it(self):
        for row in SAMPRASARANA_TABLE:
            self.assertGreater(len(row.why), 120, row.sutra)

    def test_each_note_opens_on_the_words_of_its_own_sutra(self):
        """
        Not decoration. A note that opens on something else is a note
        that has drifted from the rule it is filed under.
        """
        for row in SAMPRASARANA_TABLE:
            self.assertIn("—", row.why.split("\\n\\n")[0], row.sutra)

    def test_the_registered_notes_are_read_off_these_rows(self):
        """
        The registration is generated from `why`. Writing the vṛtti a
        second time by hand is the duplication this project has a
        standing rule against, and this is what would catch it.
        """
        for row in SAMPRASARANA_TABLE:
            registered = REGISTRY.get(row.sutra).notes
            opening = " ".join(
                row.why.split("\\n\\n")[0].split()).replace("**", "")
            flattened = " ".join(registered.split()).replace("**", "")
            self.assertIn(opening[:60], flattened, row.sutra)


class WhatIsNotCodifiedYet(unittest.TestCase):
    """
    The debt written as the exact shortfall. 6.1.45 आदेच उपदेशेऽशिति
    opens the next section of the pāda and is not codified; asserting
    it is ABSENT is what will fail the day it is added without this
    file being revisited.
    """

    def test_the_section_after_this_one_is_not_this_table(self):
        """
        6.1.45 is codified now, in `atva` — the debt this test was
        first written as has been paid. What has to keep holding is
        the boundary: the संप्रसारण heading stops at 6.1.44, and
        this table must not reach past it.
        """
        self.assertTrue(REGISTRY.has("6.1.45"))
        self.assertEqual(provisions_for("6.1.45"), ())
        self.assertEqual(REGISTRY.get("6.1.45").apply.__module__,
                         "src.astadhyayi.atva")

    def test_and_the_sandhi_stretch_belongs_to_another_module(self):
        """
        6.1.72 संहितायाम् is codified now, in `samhita` — the second
        debt this class was written as, paid. What still has to hold
        is that the संप्रसारण table stops where its heading does.
        """
        self.assertTrue(REGISTRY.has("6.1.72"))
        self.assertEqual(provisions_for("6.1.72"), ())
        self.assertEqual(REGISTRY.get("6.1.72").apply.__module__,
                         "src.astadhyayi.samhita")

    def test_the_module_does_not_claim_to_rewrite_the_root(self):
        """
        `vocalises` reports which rule acts. Turning वच् into उक्तः
        needs 8.2.30 and 6.4.2, neither of which is codified, and the
        module says so rather than half-doing it.
        """
        answer = vocalises("vac", before="kit")
        self.assertEqual(answer.does, "samprasāraṇa")
        self.assertNotIn("ukta", str(answer))


if __name__ == "__main__":
    unittest.main()
