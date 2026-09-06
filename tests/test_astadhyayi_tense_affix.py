# -*- coding: utf-8 -*-
"""
3.1.33 to 3.1.67 — the affix a lakāra brings with it.

Expectations are the Kāśikā's worked forms and its *kim*
counter-examples. Two things here can only be held by a test: a claim
about a rule in another adhyāya, and a ranking that silently did
nothing while every answer still looked plausible.
"""

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi.tense_affix import (
    ASYADI, BHIYADI, CLI, DAYADI, DIPADI, JRYADI, KRBHVASTI, KRMRADI,
    LIPYADI, NIPATANA, SARTYADI, SRIYADI, UNAYADI, USADI, _weight,
    anuprayoga, cli_becomes, cli_slot, nipatana, sarvadhatuke_yak,
    tense_affix,
)


class TheAffixEachLakaraBrings(unittest.TestCase):

    def test_each_rule_answers_for_its_own_example(self):
        cases = (
            ("3.1.33", "sya", dict(lakara="lṛṭ")),
            ("3.1.33", "sya", dict(lakara="lṛṅ")),
            ("3.1.33", "tāsi", dict(lakara="luṭ")),
            ("3.1.34", "sip", dict(lakara="leṭ")),
            ("3.1.35", "ām", dict(lakara="liṭ", root="kās")),
            ("3.1.35", "ām", dict(lakara="liṭ", affix_final=True)),
            ("3.1.36", "ām", dict(lakara="liṭ", ijadi_guru=True)),
            ("3.1.37", "ām", dict(lakara="liṭ", root="ās")),
            ("3.1.38", "ām", dict(lakara="liṭ", root="vid")),
            ("3.1.39", "ām", dict(lakara="liṭ", root="bhī")),
        )
        for sutra, affix, where in cases:
            with self.subTest(sutra=sutra, **where):
                answer = tense_affix(**where)
                self.assertEqual(answer.by, sutra)
                self.assertEqual(answer.gives, affix)

    def test_lr_without_marks_covers_two_lakaras(self):
        """
        लृरूपम् उत्सृष्टानुबन्धं सामान्यम् एकम् एव — one syllable for
        both, which is why the conditional needs no rule of its own.
        """
        for lakara in ("lṛṭ", "lṛṅ"):
            with self.subTest(lakara=lakara):
                self.assertEqual(tense_affix(lakara=lakara).by, "3.1.33")

    def test_every_named_root_of_a_list_rule_is_reached(self):
        for group, sutra in ((DAYADI, "3.1.37"), (USADI, "3.1.38"),
                             (BHIYADI, "3.1.39")):
            for root in group:
                with self.subTest(sutra=sutra, root=root):
                    self.assertEqual(
                        tense_affix(lakara="liṭ", root=root).by, sutra)

    def test_rcch_is_excepted_though_it_meets_both_conditions(self):
        """अनृच्छ इति किम्? आनर्च्छ — named out, not condition-filtered."""
        self.assertEqual(
            tense_affix(lakara="liṭ", ijadi_guru=True).by, "3.1.36")
        refused = tense_affix(lakara="liṭ", ijadi_guru=True, root="ṛcch")
        self.assertEqual(refused.by, "")
        self.assertEqual(refused.gives, "")

    def test_a_mantra_refuses_the_am(self):
        """अमन्त्र इति किम्? कृष्णो नोनाव."""
        self.assertEqual(
            tense_affix(lakara="liṭ", root="kās", mantra=True).gives, "")

    def test_only_the_three_optional_rules_are_marked_so(self):
        self.assertTrue(tense_affix(lakara="liṭ", root="vid").optional)
        self.assertTrue(tense_affix(lakara="liṭ", root="bhī").optional)
        self.assertFalse(tense_affix(lakara="liṭ", root="ās").optional)

    def test_bahulam_is_not_optional(self):
        """
        3.1.34 says बहुलम्, which reports usage rather than offering a
        choice — a distinction this project has carried since 2.4.39.
        """
        answer = tense_affix(lakara="leṭ")
        self.assertTrue(answer.bahulam)
        self.assertFalse(answer.optional)

    def test_the_aorist_is_not_answered_here(self):
        """लुङ् takes च्लि by 3.1.43 and goes through `cli_becomes`."""
        self.assertEqual(tense_affix(lakara="luṅ").by, "")


class WhatThreePointOneFortyReachesBackTo(unittest.TestCase):
    """
    3.1.40 makes a claim about a rule in another adhyāya, and running
    3.1.40 cannot check it. तत्सामर्थ्यादस्तेर्भूभावो न भवति — 2.4.52
    अस्तेर्भूः is kept off, not by a prohibition but because THIS rule
    would be pointless if it applied.
    """

    def test_all_three_auxiliaries_serve(self):
        """कृञिति प्रत्याहारेण कृभ्वस्तयो गृह्यन्ते."""
        answer = anuprayoga()
        self.assertEqual(answer.by, "3.1.40")
        for auxiliary in KRBHVASTI:
            self.assertIn(auxiliary, ("kṛ", "bhū", "as"))
        self.assertEqual(len(KRBHVASTI), 3)

    def test_2_4_52_is_codified_and_would_otherwise_have_applied(self):
        """
        The claim only means something if the rule it displaces is real
        and reachable. अस् does become भू before an ārdhadhātuka — that
        is 2.4.52 working — and पाचयामास is why it must not here.
        """
        from src.astadhyayi.adesa_dhatu import substitute

        elsewhere = substitute("as", given=("ārdhadhātuka",))
        self.assertEqual(elsewhere.by, "2.4.52")
        self.assertEqual(elsewhere.gives, "bhū")

    def test_it_needs_an_am_to_follow(self):
        self.assertEqual(anuprayoga(after_am=False).by, "")


class TheNipatanaRules(unittest.TestCase):
    """A निपātana is what the rules do not reach, so it is recorded."""

    def test_both_answer_for_themselves(self):
        for sutra in ("3.1.41", "3.1.42"):
            with self.subTest(sutra=sutra):
                answer = nipatana(sutra)
                self.assertEqual(answer.by, sutra)
                self.assertTrue(answer.gives)

    def test_they_speak_about_no_other_rule(self):
        self.assertEqual(nipatana("3.1.35").by, "")

    def test_3_1_41_is_a_specimen_and_not_one_form(self):
        """
        इतिकरणः प्रदर्शनार्थः, न केवलं प्रथमपुरुषबहुवचनम् — the whole
        paradigm follows, so the note has to say so and not merely give
        the form the sūtra quotes.
        """
        _forms, why = NIPATANA["3.1.41"]
        self.assertIn("प्रदर्शनार्थः", why)


class CliIsAPlaceholder(unittest.TestCase):

    def test_3_1_43_opens_a_slot_and_describes_nothing(self):
        """
        इकार उच्चारणार्थः, चकारः स्वरार्थः — nothing of it survives into
        a form, and the vṛtti gives no example: अस्य सिजादीन् आदेशान्
        वक्ष्यति, तत्रैवोदाहरिष्यामः.
        """
        answer = cli_slot()
        self.assertEqual(answer.by, "3.1.43")
        self.assertEqual(answer.gives, "cli")

    def test_something_always_replaces_it(self):
        """
        3.1.44 is unconditional, so every input gets an answer. A च्लि
        left standing would be a form no rule could finish.
        """
        for where in (dict(root="kṛ"), dict(root="pac"),
                      dict(root="śliṣ"), dict()):
            with self.subTest(**where):
                self.assertTrue(cli_becomes(**where).by)


#: Roots more than one rule of this run names. श्वि is in 3.1.49's
#: pair and in 3.1.58's eight, and the vṛtti on 3.1.49 says so —
#: अङोऽप्यत्र विकल्प इष्यते. A list member reached by a neighbouring
#: rule is the text, not a fault in the table.
ALSO_NAMED = {"śvi": ("3.1.49", "3.1.58")}


class TheAoristSubstitutes(unittest.TestCase):

    def test_each_rule_answers_for_its_own_example(self):
        cases = (
            ("3.1.44", "sic", dict(root="kṛ")),
            ("3.1.45", "ksa", dict(root="duh", shal_igupadha_anit=True)),
            ("3.1.46", "ksa", dict(root="śliṣ", sense="āliṅgana")),
            ("3.1.48", "caṅ", dict(root="kṛ", nyanta=True)),
            ("3.1.48", "caṅ", dict(root="śri")),
            ("3.1.49", "caṅ", dict(root="dheṭ")),
            ("3.1.50", "caṅ", dict(root="gup", chandas=True)),
            ("3.1.52", "aṅ", dict(root="vac")),
            ("3.1.53", "aṅ", dict(root="lip")),
            ("3.1.54", "aṅ", dict(root="lip", atmanepada=True)),
            ("3.1.55", "aṅ", dict(root="gam")),
            ("3.1.56", "aṅ", dict(root="sṛ")),
            ("3.1.57", "aṅ", dict(root="bhid")),
            ("3.1.58", "aṅ", dict(root="jṝ")),
            ("3.1.59", "aṅ", dict(root="ruh", chandas=True)),
            ("3.1.60", "ciṇ", dict(root="pad", before="ta",
                                   atmanepada=True)),
            ("3.1.61", "ciṇ", dict(root="budh", before="ta",
                                   atmanepada=True)),
            ("3.1.66", "ciṇ", dict(voice="bhāvakarmaṇoḥ", before="ta",
                                   atmanepada=True)),
        )
        for sutra, affix, where in cases:
            with self.subTest(sutra=sutra, **where):
                answer = cli_becomes(**where)
                self.assertEqual(answer.by, sutra)
                self.assertEqual(answer.gives, affix)

    def test_every_named_root_of_a_list_rule_is_reached(self):
        for group, sutra, extra in (
            (SRIYADI, "3.1.48", {}),
            (ASYADI, "3.1.52", {}),
            (LIPYADI, "3.1.53", {}),
            (SARTYADI, "3.1.56", {}),
            (JRYADI, "3.1.58", {}),
            (KRMRADI, "3.1.59", dict(chandas=True)),
            (UNAYADI, "3.1.51", dict(nyanta=True, chandas=True)),
            (DIPADI, "3.1.61", dict(before="ta", atmanepada=True)),
        ):
            for root in group:
                with self.subTest(sutra=sutra, root=root):
                    answer = cli_becomes(root=root, **extra).by
                    self.assertIn(
                        answer, (sutra, *ALSO_NAMED.get(root, ())),
                        f"{root} is in {sutra}'s list and reached "
                        f"{answer or 'nothing'}")

    def test_svi_is_named_by_two_rules_and_that_is_the_text(self):
        """
        श्वि stands in 3.1.49's pair and in 3.1.58's eight, and the
        vṛtti on the first acknowledges the second: अङोऽप्यत्र विकल्प
        इष्यते — अश्वत्, अश्वयीत् beside अशिश्वियत्. Three forms from
        two rules, and neither is wrong.
        """
        self.assertIn("śvi", JRYADI)
        self.assertEqual(cli_becomes(root="śvi").by, "3.1.49")

    def test_3_1_45_needs_all_three_of_its_conditions(self):
        """
        शल इति किम्? अभैत्सीत्. इगुपधादिति किम्? अधाक्षीत्. अनिट इति
        किम्? अकोषीत्. Stated as one word and meaning three things.
        """
        self.assertEqual(
            cli_becomes(root="duh", shal_igupadha_anit=True).gives, "ksa")
        self.assertNotEqual(cli_becomes(root="duh").by, "3.1.45")

    def test_3_1_46_restricts_rather_than_grants(self):
        """
        अत्र नियमार्थमेतत् — श्लिष् already met 3.1.45's conditions, so
        without this rule it would take क्स in every sense. With it, क्स
        only where embracing is meant: समाश्लिषज्जतु काष्ठम् is out.
        """
        self.assertEqual(
            cli_becomes(root="śliṣ", sense="āliṅgana").by, "3.1.46")
        self.assertNotEqual(
            cli_becomes(root="śliṣ", sense="lepana").by, "3.1.46")


class TheFourProhibitions(unittest.TestCase):
    """
    A प्रतिषेध always answers over the rule it refuses — read after it,
    it could never fire. Each names itself, refusing being what it is
    for.
    """

    def test_each_refuses_and_reports_itself(self):
        cases = (
            ("3.1.47", dict(root="dṛś", shal_igupadha_anit=True)),
            ("3.1.51", dict(root="ūna", nyanta=True, chandas=True)),
            ("3.1.64", dict(root="rudh", voice="karmakartari")),
            ("3.1.65", dict(root="tap", sense="anutāpa")),
        )
        for sutra, where in cases:
            with self.subTest(sutra=sutra):
                answer = cli_becomes(**where)
                self.assertEqual(answer.by, sutra)
                self.assertEqual(answer.gives, "")

    def test_3_1_47_hands_drs_to_3_1_57_rather_than_to_silence(self):
        """
        अस्मिन् प्रतिषिद्धे इरितो वा इत्यङ्सिचौ भवतः — the prohibition's
        effect is that a DIFFERENT rule becomes reachable, and both
        अदर्शत् and अद्राक्षीत् stand. Without asserting 3.1.45's
        conditions, दृश् goes to 3.1.57 on its own mark.
        """
        self.assertEqual(
            cli_becomes(root="dṛś", shal_igupadha_anit=True).by, "3.1.47")
        from src.astadhyayi.pada import root_its

        self.assertIn("r", root_its("dṛś"),
                      "दृशिर् carries the mark 3.1.57 turns on")

    def test_3_1_51_is_confined_to_the_veda(self):
        """Outside it the चङ् comes as usual — औनिनत्."""
        self.assertEqual(
            cli_becomes(root="ūna", nyanta=True, chandas=True).by,
            "3.1.51")
        self.assertEqual(
            cli_becomes(root="ūna", nyanta=True).by, "3.1.48")

    def test_3_1_65_widens_the_refusal_by_naming_a_sense(self):
        """
        तस्य ग्रहणम् अकर्मकर्त्रर्थम्, तत्र हि भावकर्मणोरपि प्रतिषेधो
        भवति. Naming अनुताप looks like a restriction and works as an
        extension: the refusal reaches भाव and कर्मन् too, where 3.1.64
        stops at कर्मकर्तृ.
        """
        for voice in ("karmakartari", "bhāvakarmaṇoḥ"):
            with self.subTest(voice=voice):
                self.assertEqual(
                    cli_becomes(root="tap", sense="anutāpa",
                                voice=voice).by, "3.1.65")
        # 3.1.64 does NOT reach beyond कर्मकर्तृ.
        self.assertNotEqual(
            cli_becomes(root="rudh", voice="bhāvakarmaṇoḥ",
                        before="ta", atmanepada=True).by, "3.1.64")


class TwoConditionsReadFromTheCorpus(unittest.TestCase):
    """
    इरित् and ऌदित् are marks the dhātupāṭha writes on the root, and
    1.3.2 उपदेशेऽजनुनासिक इत् is what makes them its — so they are
    asked, never asserted by the caller.
    """

    def test_irit_roots_are_found_not_declared(self):
        for root in ("bhid", "chid"):
            with self.subTest(root=root):
                self.assertEqual(cli_becomes(root=root).by, "3.1.57")

    def test_ldit_roots_likewise(self):
        for root in ("gam", "śak"):
            with self.subTest(root=root):
                self.assertEqual(cli_becomes(root=root).by, "3.1.55")

    def test_a_root_with_neither_mark_falls_to_the_default(self):
        self.assertEqual(cli_becomes(root="kṛ").by, "3.1.44")

    def test_3_1_57_holds_in_the_active_only(self):
        """परस्मैपदेष्वित्येव — अभित्त, अच्छित्त keep the सिच्."""
        self.assertEqual(
            cli_becomes(root="bhid", atmanepada=True).by, "3.1.44")


class TheRankingThatDidNothing(unittest.TestCase):
    """
    `_weight` scores how much a row says, and once returned False for
    every row: `len(row.of) > 0 + 3 * ...` reads the whole sum as one
    comparison, because `>` binds looser than `+`. The ranking silently
    did nothing, last-match-wins stayed in force, and every answer
    still looked plausible — which is why the scores are asserted here
    and not only their effect.
    """

    def test_the_scores_are_numbers_and_they_differ(self):
        scores = {row.sutra: _weight(row) for row in CLI}
        self.assertTrue(all(isinstance(s[1], int) and not isinstance(s[1], bool)
                            for s in scores.values()),
                        "a bool here means the sum collapsed into a "
                        "comparison again")
        self.assertGreater(len({s[1] for s in scores.values()}), 1,
                           "if every row scores the same the ranking is "
                           "doing nothing")

    def test_the_default_says_least(self):
        default = next(r for r in CLI if r.sutra == "3.1.44")
        self.assertEqual(_weight(default)[1], 0,
                         "3.1.44 states no condition at all")

    def test_a_prohibition_outranks_everything(self):
        for row in CLI:
            with self.subTest(sutra=row.sutra):
                self.assertEqual(_weight(row)[0], 1 if row.refuses else 0)

    def test_duh_is_the_case_that_needed_it(self):
        """
        दुह् is दुहिँर्, so 3.1.57 genuinely reaches it and taking the
        last match gave अङ् where the vṛtti gives अधुक्षत्. Both rules
        are right about दुह्; three stated conditions say more than one
        mark.
        """
        from src.astadhyayi.pada import root_its

        self.assertTrue({"i", "r"} <= root_its("duh"),
                        "the collision is real, not contrived")
        self.assertEqual(
            cli_becomes(root="duh", shal_igupadha_anit=True).by, "3.1.45")


class TheTableIsWellFormed(unittest.TestCase):

    def test_every_row_names_a_sutra_of_this_run(self):
        for row in CLI:
            with self.subTest(sutra=row.sutra):
                self.assertRegex(row.sutra, r"^3\.1\.(4[4-9]|5\d|6[0-6])$")
                self.assertTrue(row.why)
                self.assertEqual(bool(row.gives), not row.refuses)

    def test_the_rows_are_in_the_texts_own_order(self):
        def order(sid):
            return tuple(int(p) for p in sid.split("."))

        seen = [order(r.sutra) for r in CLI]
        self.assertEqual(seen, sorted(seen))

    def test_the_three_sutras_naming_two_bases_are_two_rows(self):
        """
        3.1.48 names any ण्यन्त stem OR three roots. Written as one row
        the named list shut the causatives out and अचीकरत् reached
        nothing — the third sūtra in this adhyāya to need splitting for
        that reason, after 3.1.25 and 3.1.55.
        """
        rows = [r for r in CLI if r.sutra == "3.1.48"]
        self.assertEqual(len(rows), 2)
        self.assertEqual({bool(r.nyanta) for r in rows}, {True, False})


class TheVikaranaBegins(unittest.TestCase):

    def test_3_1_67_gives_yak_for_the_act_and_the_object(self):
        answer = sarvadhatuke_yak()
        self.assertEqual(answer.by, "3.1.67")
        self.assertEqual(answer.gives, "yak")

    def test_it_reaches_karmakartr_too_and_says_why(self):
        """विप्रतिषेधाद्धि यकः शपो बलीयस्त्वम्."""
        answer = sarvadhatuke_yak(voice="karmakartari")
        self.assertEqual(answer.by, "3.1.67")
        self.assertIn("बलीयस्त्वम्", answer.why)

    def test_the_agent_goes_to_3_1_68_instead(self):
        """
        कर्तरि शप् was reached ahead for the present paradigm of पच्,
        and the run has now caught up with it — so 3.1.67 must NOT
        answer for the agent.
        """
        from src.astadhyayi.sutra import REGISTRY

        self.assertTrue(REGISTRY.has("3.1.68"))
        self.assertEqual(sarvadhatuke_yak(voice="kartari").by, "")


if __name__ == "__main__":
    unittest.main()
