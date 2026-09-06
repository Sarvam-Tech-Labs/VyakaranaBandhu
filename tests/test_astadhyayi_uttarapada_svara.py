# -*- coding: utf-8 -*-
"""
६.२.१११–१९९ — the second member, and the three placements it takes.

What is worth testing here is not that ninety rows exist. It is that
the pāda's last stretch keeps the shape the vṛttis describe: one
scope-word running to the end of the pāda with three placement-words
taking turns inside it; headings that name nothing staying out of
reach; refusals reporting the rule they refuse and never themselves;
and a rule that names both members beating one that names only one.
"""

from __future__ import annotations

import re
import unittest

from src.astadhyayi.purvapada_udatta import (
    Accented, BAHUVRIHI_RUN, PLACED_TABLE)
from src.astadhyayi.sources import REGISTRY
from src.astadhyayi.uttarapada_svara import (
    ACARYADI, ADI_RUN, ANTA_RUN, CARVADI, DEVATA_EXCEPTIONS,
    KRATVADI, NIRUDAKADI, PRAKRTI_RUN, THE_SIX, UTTARAPADA_RUN,
    UTTARAPADA_TABLE, provisions_for, second_member,
    uttarapada_runs)
import src.astadhyayi.rules  # noqa: F401  — populates the registry


def _n(sutra_id):
    return tuple(int(part) for part in sutra_id.split("."))


def _within(sutra_id, span):
    return _n(span[0]) <= _n(sutra_id) <= _n(span[1])


class TheRunsPartitionTheScopeWord(unittest.TestCase):
    """
    उत्तरपदम् lasts to the end of the pāda; आदिः, प्रकृत्या and अन्तः
    take turns inside it.

    **उत्तरपदस्येत्येतदा पादपरिसमाप्तेः। आदिरिति प्रकृत्या भगालम्
    इति यावत्**, and then **प्रकृत्येत्येतदधिकृतम् अन्तः इति यावद्
    वेदितव्यम्**. Three stretches end to end with no gap and no
    overlap — which is what makes the placement of any one rule
    decidable from its number alone.
    """

    def test_the_scope_word_reaches_the_last_sutra_of_the_pada(self):
        self.assertEqual(UTTARAPADA_RUN[1], "6.2.199")

    def test_the_three_placements_are_end_to_end(self):
        self.assertEqual(ADI_RUN[0], UTTARAPADA_RUN[0])
        self.assertEqual(_n(PRAKRTI_RUN[0]), _n(ADI_RUN[1])[:2] +
                         (_n(ADI_RUN[1])[2] + 1,))
        self.assertEqual(_n(ANTA_RUN[0]), _n(PRAKRTI_RUN[1])[:2] +
                         (_n(PRAKRTI_RUN[1])[2] + 1,))
        self.assertEqual(ANTA_RUN[1], UTTARAPADA_RUN[1])

    def test_the_adi_run_stops_where_prakrtya_bhagalam_stands(self):
        """**आदिरिति प्रकृत्या भगालम् इति यावत्** — 6.2.137 is the
        bound, so आदिः holds through 6.2.136 and no further."""
        self.assertEqual(ADI_RUN[1], "6.2.136")
        self.assertEqual(PRAKRTI_RUN[0], "6.2.137")

    def test_every_row_falls_inside_the_scope_word(self):
        for row in UTTARAPADA_TABLE:
            self.assertTrue(_within(row.sutra, UTTARAPADA_RUN),
                            row.sutra)

    def test_the_summary_names_all_four(self):
        why = uttarapada_runs().why
        for bound in (UTTARAPADA_RUN[1], ADI_RUN[1], PRAKRTI_RUN[1],
                      ANTA_RUN[0]):
            self.assertIn(bound, why)


class TheTableIsTheWholeStretch(unittest.TestCase):
    def test_one_row_for_each_sutra_from_111_to_199(self):
        got = [row.sutra for row in UTTARAPADA_TABLE]
        want = ["6.2.%d" % n for n in range(111, 200)]
        self.assertEqual(got, want)

    def test_and_they_are_in_reading_order(self):
        ids = [_n(row.sutra) for row in UTTARAPADA_TABLE]
        self.assertEqual(ids, sorted(ids))

    def test_every_row_carries_its_reason(self):
        for row in UTTARAPADA_TABLE:
            self.assertGreater(len(row.why), 60, row.sutra)


class WherePutsTheAccentAgreesWithWhichRunItIsIn(unittest.TestCase):
    """
    A rule's placement is decidable from its number, and the code
    must agree with that.

    Four rules place the accent somewhere none of the three headings
    names — 6.2.125 on the FIRST member, 6.2.173 before the कप्,
    6.2.174 one syllable further back, 6.2.199 on the following word
    — and two more give it to both members at once. Each of those is
    named here rather than exempted silently, because each is a claim
    the vṛtti makes and not a gap in the table.
    """

    ODD = {
        "6.2.125": "pūrvapada-ādi",
        "6.2.140": "ubhe-prakṛti",
        "6.2.141": "ubhe-prakṛti",
        "6.2.173": "pūrva-anta",
        "6.2.174": "antyāt-pūrva",
        "6.2.175": "nañvat",
        "6.2.199": "para-ādi",
    }

    def test_the_plain_rules_place_where_their_run_says(self):
        expected = {"ādi": ADI_RUN, "prakṛti": PRAKRTI_RUN,
                    "anta": ANTA_RUN}
        checked = 0
        for row in UTTARAPADA_TABLE:
            if row.refuses or row.sutra in self.ODD:
                continue
            self.assertIn(row.where, expected, row.sutra)
            self.assertTrue(_within(row.sutra, expected[row.where]),
                            "%s places %s outside its run"
                            % (row.sutra, row.where))
            checked += 1
        self.assertGreater(checked, 70)

    def test_and_the_odd_ones_are_exactly_those_listed(self):
        odd = {row.sutra: row.where for row in UTTARAPADA_TABLE
               if not row.refuses
               and row.where not in ("ādi", "prakṛti", "anta")}
        self.assertEqual(odd, self.ODD)

    def test_a_refusal_places_nothing(self):
        for row in UTTARAPADA_TABLE:
            if row.refuses:
                self.assertEqual(row.where, "", row.sutra)


class AHeadingThatNamesNothingIsNotReachable(unittest.TestCase):
    """
    6.2.111 and 6.2.143 state a placement and no condition, so a row
    for them would match every query put to the section.

    6.2.137 is a heading too — **प्रकृत्येत्येतदधिकृतम्** — but it
    also names भगाल, so it stays reachable and answers for its own
    word. That is the same line 6.1.45 and 6.2.1 sit on.
    """

    def test_the_two_pure_headings_never_answer(self):
        for code in ("6.2.111", "6.2.143"):
            row, = provisions_for(code)
            self.assertTrue(row.heading)
            self.assertNotEqual(
                second_member().sutra, code)
            self.assertNotEqual(
                second_member("mukha", purvapada="abhi").sutra, code)

    def test_a_heading_that_names_a_word_still_answers(self):
        row, = provisions_for("6.2.137")
        self.assertTrue(row.heading)
        got = second_member("bhagāla", samasa="tatpuruṣa")
        self.assertEqual(got.sutra, "6.2.137")
        self.assertEqual(got.where, "prakṛti")

    def test_an_unreached_query_names_no_rule_at_all(self):
        got = second_member("aśvattha")
        self.assertEqual(got.sutra, "")
        self.assertIn("6.1.223", got.why)


class ARefusalReportsWhatItRefuses(unittest.TestCase):
    """
    A प्रतिषेध does not govern what it excepts.

    Each of these names an earlier rule of this same run and hands
    the word back to it — 6.2.133 to 6.2.132, 6.2.168 to 6.2.167,
    6.2.176 to 6.2.175, 6.2.181 to 6.2.180 — and 6.2.142 to 6.2.141,
    which is the pair that carried two accents.
    """

    PAIRS = {
        "6.2.133": "6.2.132",
        "6.2.142": "6.2.141",
        "6.2.168": "6.2.167",
        "6.2.176": "6.2.175",
        "6.2.181": "6.2.180",
    }

    def test_those_are_all_of_them(self):
        refusing = {row.sutra for row in UTTARAPADA_TABLE
                    if row.refuses}
        self.assertEqual(refusing, set(self.PAIRS))

    def test_each_names_the_rule_it_takes_the_word_from(self):
        for refuser, supplier in self.PAIRS.items():
            row, = provisions_for(refuser)
            self.assertIn(supplier, row.blocks, refuser)
            self.assertLess(_n(supplier), _n(refuser), refuser)

    def test_and_the_answer_carries_the_supplier_on_blocked_by(self):
        got = second_member("putra",
                            purvapada_gana="ācārya-ādi-ākhyā",
                            samasa="tatpuruṣa")
        self.assertEqual(got.sutra, "6.2.133")
        self.assertEqual(got.where, "")
        self.assertEqual(got.blocked_by, ("6.2.132",))

    def test_the_supplier_still_answers_where_it_is_not_refused(self):
        got = second_member("putra", purvapada_gana="puṃs",
                            samasa="tatpuruṣa")
        self.assertEqual(got.sutra, "6.2.132")
        self.assertEqual(got.where, "ādi")


class SpecificityIsScoredOnHowTheRowMatched(unittest.TestCase):
    """
    The lesson 6.1.15 taught, in a new place.

    6.2.151 fills three second-member columns — two affixes, four
    words, a gaṇa — and 6.2.117 fills one. Scoring the columns a row
    HAS would let 6.2.151 win a query it matched through its affix
    alone, and सुकर्मा would come back end-accented. Scoring how the
    query matched puts 6.2.117 first, where the Kāśikā puts it.
    """

    def test_a_rule_reached_by_its_affix_alone_scores_only_that(self):
        self.assertEqual(
            second_member(purvapada="su", affix="man",
                          samasa="bahuvrīhi").sutra, "6.2.117")

    def test_and_the_wider_rule_still_answers_on_its_own_ground(self):
        self.assertEqual(second_member(affix="man").sutra, "6.2.151")

    def test_naming_both_members_beats_naming_one(self):
        """6.2.167 names मुख; 6.2.185 names मुख and अभि."""
        self.assertEqual(
            second_member("mukha", purvapada="abhi").sutra, "6.2.185")
        self.assertEqual(
            second_member("mukha", result="svāṅga",
                          samasa="bahuvrīhi").sutra, "6.2.167")

    def test_the_later_option_beats_the_earlier_rule_in_the_veda(self):
        plain = second_member("stana", purvapada_gana="saṅkhyā",
                              samasa="bahuvrīhi")
        vedic = second_member("stana", purvapada_gana="saṅkhyā",
                              samasa="bahuvrīhi", chandasi=True)
        self.assertEqual(plain.sutra, "6.2.163")
        self.assertFalse(plain.optional)
        self.assertEqual(vedic.sutra, "6.2.164")
        self.assertTrue(vedic.optional)


class TheColumnsOfOneMemberAreAlternatives(unittest.TestCase):
    """
    A rule names the second member by a word, a class or an affix,
    and any one of them does; it names the first member by a word or
    a class, and any one of those does. But what it says about the
    two members has to hold together.

    6.2.145 सूपमानात् क्तः reaches a क्त-word after सु AND after a
    comparison — either source will do. 6.2.112 wants कर्ण in second
    place and a colour-word in first, and one without the other is
    not the rule.
    """

    def test_either_source_reaches_the_same_rule(self):
        after_su = second_member(affix="kta", purvapada="su")
        after_upamana = second_member(affix="kta",
                                      purvapada_gana="upamāna")
        self.assertEqual(after_su.sutra, "6.2.145")
        self.assertEqual(after_upamana.sutra, "6.2.145")

    def test_but_both_halves_of_a_two_sided_rule_are_required(self):
        self.assertEqual(
            second_member("karṇa", purvapada_gana="varṇa",
                          samasa="bahuvrīhi").sutra, "6.2.112")
        # कर्ण with no colour-word in front is not 6.2.112's case,
        # and 6.2.113 wants a name or a likeness, so nothing is
        # reached and 6.1.223 stands.
        self.assertEqual(
            second_member("karṇa", samasa="bahuvrīhi").sutra, "")

    def test_any_of_six_kinds_reaches_6_2_151(self):
        for query in ({"affix": "man"}, {"affix": "ktin"},
                      {"uttarapada": "śayana"},
                      {"uttarapada": "sthāna"},
                      {"uttarapada": "krīta"},
                      {"gana": "yājakādi"}):
            self.assertEqual(second_member(**query).sutra, "6.2.151",
                             query)


class TwoRulesAccentBothMembersAtOnce(unittest.TestCase):
    """
    **युगपदुभे पूर्वोत्तरपदे प्रकृतिस्वरे भवतः** — and इन्द्राबृहस्पती
    then carries three उदात्तs, since 6.2.140 has already given
    बृहस्पति two.
    """

    def test_the_two_that_do_it(self):
        both = {row.sutra for row in UTTARAPADA_TABLE
                if row.where == "ubhe-prakṛti"}
        self.assertEqual(both, {"6.2.140", "6.2.141"})

    def test_a_gods_dvandva_keeps_both_accents(self):
        got = second_member(samasa="devatā-dvandva")
        self.assertEqual(got.sutra, "6.2.141")
        self.assertEqual(got.where, "ubhe-prakṛti")

    def test_unless_the_second_word_begins_low(self):
        got = second_member(samasa="devatā-dvandva",
                            result="anudāttādi")
        self.assertEqual(got.sutra, "6.2.142")
        self.assertEqual(got.where, "")
        self.assertEqual(got.blocked_by, ("6.2.141",))

    def test_and_four_words_are_taken_back_out_of_the_refusal(self):
        row, = provisions_for("6.2.142")
        self.assertEqual(row.excludes, DEVATA_EXCEPTIONS)
        self.assertEqual(len(DEVATA_EXCEPTIONS), 4)
        for word in DEVATA_EXCEPTIONS:
            got = second_member(word, samasa="devatā-dvandva",
                                result="anudāttādi")
            self.assertEqual(got.sutra, "6.2.141", word)


class TheSixOf6_2_135AreSixRulesWidened(unittest.TestCase):
    """
    **षट् च काण्डादीनि** — every one of the six is a word 6.2.126–129
    had already accented under a sense-condition, and 6.2.135 frees
    it of that at the price of a non-living genitive in front.

    So the list is not free-standing: it has to be exactly what
    those four rules named, or the vṛtti's walk through them —
    **काण्डं गर्हायाम् इत्युक्तम् अगर्हायामपि भवति** — would be
    about different words.
    """

    def test_every_one_of_the_six_was_named_earlier(self):
        earlier = set()
        for code in ("6.2.126", "6.2.127", "6.2.128", "6.2.129"):
            row, = provisions_for(code)
            earlier.update(row.of)
        self.assertEqual(len(THE_SIX), 6)
        for word in THE_SIX:
            self.assertIn(word, earlier, word)

    def test_the_sense_condition_is_gone(self):
        row, = provisions_for("6.2.135")
        self.assertEqual(row.result, ())
        self.assertEqual(row.case, "ṣaṣṭhī")

    def test_and_it_answers_where_the_earlier_rule_would_not(self):
        # दर्भकाण्डम्, with no contempt meant.
        got = second_member("kāṇḍa", purvapada_gana="aprāṇin",
                            case="ṣaṣṭhī", samasa="tatpuruṣa")
        self.assertEqual(got.sutra, "6.2.135")
        # and 6.2.126 is still what answers where contempt IS meant
        self.assertEqual(
            second_member("kāṇḍa", samasa="tatpuruṣa",
                          result="garhā").sutra, "6.2.126")


class TheGanasAreReadOffTheVrtti(unittest.TestCase):
    def test_the_kratvadi_list_is_the_six_the_vrtti_reads_out(self):
        self.assertEqual(len(KRATVADI), 6)
        self.assertEqual(KRATVADI[0], "kratu")

    def test_the_carvadi_list_matches_its_examples(self):
        row, = provisions_for("6.2.160")
        for word in CARVADI:
            self.assertIn(word, ("cāru", "sādhu", "yaudhika",
                                 "vadānya"))
        self.assertEqual(row.gana, "cārvādi")

    def test_the_five_kinds_6_2_133_refuses_for(self):
        self.assertEqual(len(ACARYADI), 5)
        self.assertEqual(ACARYADI[0], "ācārya")

    def test_the_nirudakadi_list_is_of_whole_compounds(self):
        """**निरुदकादीनि च शब्दरूपाणि** — each entry already has its
        first member in it, which is why none of them is a bare
        second member like उदक."""
        for word in NIRUDAKADI:
            self.assertTrue(
                word.startswith("nir") or word.startswith("niṣ")
                or word.startswith("dus"), word)


class WantsFiltersByPlacement(unittest.TestCase):
    def test_asking_for_a_placement_no_rule_here_gives_finds_none(self):
        self.assertEqual(second_member("mukha", purvapada="abhi",
                                       wants="ādi").sutra, "")

    def test_asking_for_the_one_it_does_give_finds_it(self):
        self.assertEqual(second_member("mukha", purvapada="abhi",
                                       wants="anta").sutra, "6.2.185")

    def test_a_refusal_supplies_nothing_to_ask_for(self):
        self.assertEqual(
            second_member("putra", purvapada_gana="ācārya-ādi-ākhyā",
                          samasa="tatpuruṣa", wants="ādi").sutra,
            "")


class TheOptionsAreTheSutrasThatSaySo(unittest.TestCase):
    """
    A rule is optional here only where its own words say विभाषा, वा,
    अन्यतरस्याम् or बहुलम्. Anything else marked optional would be
    an option the text does not give.
    """

    #: Each of these carries the option in its own words. The
    #: fragment for 6.2.169 begins after the junction, since
    #: निष्ठोपमानादन्यतरस्याम् swallows the अ of अन्यतरस्याम्.
    SAYS_IT = {
        "6.2.161": "विभाषा",
        "6.2.164": "विभाषा",
        "6.2.169": "न्यतरस्याम्",
        "6.2.171": "वा ",
        "6.2.196": "विभाषो",
        "6.2.199": "बहुलम्",
    }

    #: And these two say nothing of the kind: they take 6.2.196's
    #: विभाषा by anuvṛtti, which is why the Kāśikā glosses each with
    #: **विभाषान्त उदात्तो भवति** though neither sūtra has the word.
    CARRIED = ("6.2.197", "6.2.198")

    def test_exactly_these_are_optional(self):
        got = tuple(row.sutra for row in UTTARAPADA_TABLE
                    if row.optional)
        self.assertEqual(
            got, tuple(sorted(set(self.SAYS_IT) | set(self.CARRIED),
                              key=_n)))

    def test_the_stated_ones_carry_the_word_that_states_it(self):
        for code, word in self.SAYS_IT.items():
            row, = provisions_for(code)
            self.assertIn(word, row.why, code)

    def test_the_carried_ones_reach_back_to_one_that_does(self):
        """
        6.2.197 and 6.2.198 are optional only because 6.2.196
        विभाषोत्पुच्छे is still running. An anuvṛtti needs an unbroken
        chain, so every sūtra from 6.2.196 to each of them has to be
        optional too — the moment one is not, the option has stopped
        and these two are wrong.
        """
        for code in self.CARRIED:
            row, = provisions_for(code)
            for word in ("विभाषा", "विभाषो", "न्यतरस्याम्", "बहुलम्"):
                self.assertNotIn(word, row.why, code)
            for n in range(196, _n(code)[2] + 1):
                stage, = provisions_for("6.2.%d" % n)
                self.assertTrue(stage.optional,
                                "6.2.%d breaks the chain 6.2.196 "
                                "needs to reach %s" % (n, code))

    def test_the_answer_carries_the_option_through(self):
        self.assertTrue(
            second_member("utpuccha", samasa="tatpuruṣa").optional)
        self.assertFalse(
            second_member("puṇya", case="saptamī").optional)


class ThisSectionReusesTheOneBeforeIt(unittest.TestCase):
    """
    6.2.64–110 and 6.2.111–199 answer the same kind of question
    about opposite halves of the compound, so they answer in the
    same shape — and बहुव्रीहि, opened at 6.2.106, reaches across
    the join into this run.
    """

    def test_the_answer_is_the_earlier_sections_own_type(self):
        got = second_member("mukha", purvapada="abhi")
        self.assertIsInstance(got, Accented)

    def test_the_bahuvrihi_heading_crosses_into_this_run(self):
        self.assertTrue(_within(BAHUVRIHI_RUN[0],
                                ("6.2.64", "6.2.110")))
        self.assertTrue(_within(BAHUVRIHI_RUN[1], UTTARAPADA_RUN))

    def test_and_the_two_tables_do_not_overlap(self):
        first = {row.sutra for row in PLACED_TABLE}
        second = {row.sutra for row in UTTARAPADA_TABLE}
        self.assertEqual(first & second, set())


class Registration(unittest.TestCase):
    def test_every_sutra_of_the_run_is_registered(self):
        for row in UTTARAPADA_TABLE:
            self.assertTrue(REGISTRY.has(row.sutra), row.sutra)

    def test_the_notes_are_read_off_these_rows(self):
        """
        The note is generated from the `why`, never written twice.
        Editing one and forgetting the other is what this catches.
        """
        collapse = re.compile(r"\s+")
        for row in UTTARAPADA_TABLE:
            note = collapse.sub(" ", REGISTRY.get(row.sutra).notes)
            head = collapse.sub(" ", row.why.split("\\n\\n")[0])
            self.assertIn(head[:70], note, row.sutra)


class WhatIsNotCodifiedYet(unittest.TestCase):
    """
    पाद ६.२ is finished with this run: 6.2.1–63 keep the first
    member's accent, 6.2.64–110 place it, and 6.2.111–199 hand the
    whole question to the second member.

    What stands next is 6.3, whose subject changes again —
    अलुगुत्तरपदे, what happens to the first member's CASE ENDING
    before a second member, rather than to its accent.
    """

    def test_the_pada_is_closed_at_both_ends(self):
        self.assertTrue(REGISTRY.has("6.2.1"))
        self.assertTrue(REGISTRY.has("6.2.199"))

    def test_and_nothing_of_the_pada_is_missing_between_them(self):
        for n in range(1, 200):
            self.assertTrue(REGISTRY.has("6.2.%d" % n), n)

    def test_and_the_next_pada_has_opened(self):
        """
        6.3.1 अलुगुत्तरपदे changes the subject: from where the
        accent of a compound falls to what the first member LOOKS
        like before a second. The debt is collected, and what it
        can now be checked against is the join — 6.2 ends at 199
        and 6.3 opens at 1, with no sūtra of either missing.
        """
        self.assertTrue(REGISTRY.has("6.3.1"))
        self.assertTrue(REGISTRY.has("6.2.199"))

    def test_and_the_new_pada_is_complete(self):
        """
        When this was written 6.3 had only begun, and the claim
        was that it was unbroken as far as it went. It now goes
        all the way: every sūtra of the pāda is codified, and the
        last of them is the bound its own first heading was read
        against.
        """
        from src.astadhyayi.aluk import UTTARAPADE_RUN

        codified = [n for n in range(1, 140)
                    if REGISTRY.has("6.3.%d" % n)]
        self.assertEqual(codified, list(range(1, 140)))
        self.assertEqual(UTTARAPADE_RUN[1], "6.3.139")


if __name__ == "__main__":
    unittest.main()
