# -*- coding: utf-8 -*-
"""
3.3.1 to 3.3.15 — the opening of अध्याय ३ पाद ३.

What this block asserts that no earlier one could:

  * a rule licensing a SEPARATE TEXT, which is on disk and is quoted
    rather than restated;
  * a condition on what PART OF SPEECH a companion is;
  * one grammatical device — the बहुव्रीहि spelling of अनद्यतन —
    doing the same work for two different tenses a pāda apart;
  * a rule that borrows its affixes from one sūtra and its conditions
    from another, and states nothing itself;
  * the वासरूप suspension established a third time, in a second pāda.
"""

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi.bhava_krt import (
    KRIYARTHA, kriyartha_affix, vasarupa_suspended,
)
from src.astadhyayi.lakara import LAKARA, lakara_for, lrt_substitute
from src.astadhyayi.unadi import (
    GAMYADI, UNADI_EXAMPLES, gamyadi, unadi, unadi_count,
)
from src.astadhyayi.upapada_krt import Added, NotAdded


class ARuleThatLicensesAnotherText(unittest.TestCase):
    """
    3.3.1 उणादयो बहुलम् does not give an affix. It admits the affixes
    of the उणादिपाठ, 748 sūtras that are on disk and had never been
    read by any code here.
    """

    def test_the_licensed_text_is_actually_loaded(self):
        self.assertGreater(unadi_count(), 700)

    def test_the_kasikas_own_citation_resolves_in_it(self):
        """
        The vṛtti cites प०उ० १.१ कृवापाजिमिस्वदिसाध्यशूभ्य उण् for
        कारुः. That is the first row of the file, and this asserts the
        two are the same text — which is what makes the locator worth
        holding instead of the affix.
        """
        answer = unadi("kāru")
        self.assertEqual(answer.by, "3.3.1")
        self.assertEqual(answer.locator, "1.1")
        self.assertIn("uṇ", answer.text)
        self.assertIn("kṛvāpāji", answer.text)

    def test_every_worked_example_resolves_to_a_real_sutra(self):
        from src.astadhyayi.corpus import unadi_sutra

        for word, locator in UNADI_EXAMPLES.items():
            with self.subTest(word=word):
                self.assertIsNotNone(unadi_sutra(locator))
                self.assertEqual(unadi(word).text,
                                 unadi_sutra(locator).text)

    def test_bahulam_refuses_to_refuse(self):
        """
        A word absent from the list settles nothing —
        केचिदविहिता एव प्रयोगत उन्नीयन्ते. So an unknown word still
        gets 3.3.1, with an empty locator, and NOT a refusal.
        """
        answer = unadi("kimcidanyat")
        self.assertEqual(answer.by, "3.3.1")
        self.assertEqual(answer.locator, "")
        self.assertIn("बहुलम्", answer.why)

    def test_but_the_name_sense_is_a_real_condition(self):
        answer = unadi("kāru", samjna=False)
        self.assertIsInstance(answer, NotAdded)
        self.assertEqual(answer.by, "3.3.1")

    def test_neither_of_its_conditions_is_in_the_sutra(self):
        """
        वर्तमान इत्येव, संज्ञायामिति च — both run down from the pāda
        before, from two different rules of it.
        """
        from src.astadhyayi.sutra import REGISTRY

        notes = REGISTRY.get("3.3.1").notes
        self.assertIn("3.2.123", notes)
        self.assertIn("3.2.185", notes)


class OneWordReadTwoWaysAndNotThree(unittest.TestCase):
    """
    दृश्यते has now been glossed at three places. 3.2.75 read it
    प्रयोगानुसरणार्थम्, 3.2.178 विध्यन्तरोपसंग्रहार्थम्, and 3.3.2
    प्रयोगानुसारार्थम् — which is 3.2.75's reading again, in almost
    the same word. So there are two readings, not three.
    """

    def test_3_3_2_takes_the_usage_following_reading(self):
        answer = unadi("carman", past=True)
        self.assertEqual(answer.by, "3.3.2")
        self.assertIn("प्रयोगानुसार", answer.why)

    def test_and_it_names_the_two_rules_it_sides_between(self):
        answer = unadi("vartman", past=True)
        self.assertIn("3.2.75", answer.why)
        self.assertIn("3.2.178", answer.why)

    def test_the_registry_records_all_three_glosses(self):
        from src.astadhyayi.sutra import REGISTRY

        for sutra, gloss in (
            ("3.2.75", "प्रयोगानुसरणार्थम्"),
            ("3.2.178", "विध्यन्तरोपसंग्रहार्थम्"),
            ("3.3.2", "प्रयोगानुसारार्थम्"),
        ):
            with self.subTest(sutra=sutra):
                self.assertIn(gloss, REGISTRY.get(sutra).notes)


class AConditionOnWhatPartOfSpeechACompanionIs(unittest.TestCase):
    """
    3.3.4 wants यावत् and पुरा as निपात. The counter-example is the
    same two words used as case-forms — and what stands there is
    3.3.13's लृट्, which the counter-example itself uses.
    """

    def test_as_particles_the_present_ending_comes(self):
        for word in ("yāvat", "purā"):
            with self.subTest(beside=word):
                answer = lakara_for(time="bhaviṣyat", beside=word,
                                    nipata=True)
                self.assertEqual((answer.by, answer.gives),
                                 ("3.3.4", "laṭ"))

    def test_otherwise_the_rule_does_not_reach_and_lrt_stands(self):
        answer = lakara_for(time="bhaviṣyat", beside="yāvat")
        self.assertEqual((answer.by, answer.gives), ("3.3.13", "lṛṭ"))

    def test_the_counter_example_uses_the_ending_it_falls_back_to(self):
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("यावद् दास्यति तावद् भोक्ष्यते",
                      REGISTRY.get("3.3.4").notes)


class TheFutureRulesShareThePastsTable(unittest.TestCase):
    """
    They ask the same question — which tense-ending — so they are rows
    in the same table, filtered on time. What must hold is that a
    future row cannot answer a past question or the other way round.
    """

    def test_the_times_partition_the_table(self):
        times = {row.time for row in LAKARA}
        self.assertIn("bhūta", times)
        self.assertIn("bhaviṣyat", times)
        for time in times:
            rows = [r for r in LAKARA if r.time == time]
            self.assertTrue(rows)

    def test_a_past_question_never_reaches_a_future_rule(self):
        future = {r.sutra for r in LAKARA if r.time == "bhaviṣyat"}
        self.assertTrue(future)
        for kwargs in (dict(), dict(anadyatana=True),
                       dict(paroksa=True), dict(beside="sma")):
            with self.subTest(**kwargs):
                self.assertNotIn(lakara_for(**kwargs).by, future)

    def test_and_a_future_question_never_reaches_a_past_rule(self):
        past = {r.sutra for r in LAKARA if r.time == "bhūta"}
        for kwargs in (dict(), dict(anadyatana=True),
                       dict(lodartha=True), dict(lipsa=True,
                                                 kimvrtta=True)):
            with self.subTest(**kwargs):
                answer = lakara_for(time="bhaviṣyat", **kwargs)
                self.assertNotIn(answer.by, past)

    def test_each_future_rule_answers_for_its_own_example(self):
        cases = (
            ("3.3.5", "laṭ", dict(beside="kadā")),
            ("3.3.6", "laṭ", dict(kimvrtta=True, lipsa=True)),
            ("3.3.7", "laṭ", dict(lipsyamana_siddhi=True)),
            ("3.3.8", "laṭ", dict(lodartha=True)),
            ("3.3.9", "liṅ", dict(lodartha=True,
                                  urdhvamauhurtika=True)),
            ("3.3.13", "lṛṭ", dict()),
            ("3.3.15", "luṭ", dict(anadyatana=True)),
        )
        for sutra, gives, where in cases:
            with self.subTest(sutra=sutra, **where):
                answer = lakara_for(time="bhaviṣyat", **where)
                self.assertEqual((answer.by, answer.gives),
                                 (sutra, gives))

    def test_lipsa_is_needed_and_not_merely_decorative(self):
        """लिप्सायामिति किम्? कः पाटलिपुत्रं गमिष्यति."""
        self.assertNotEqual(
            lakara_for(time="bhaviṣyat", kimvrtta=True).by, "3.3.6")


class OneDeviceServingTwoTenses(unittest.TestCase):
    """
    अनद्यतन is written as a बहुव्रीहि at 3.2.111 for the past and at
    3.3.15 for the future, with the same wording and the same reason:
    the compound's form excludes the MIXED case.
    """

    def test_both_rules_use_the_condition(self):
        past = lakara_for(anadyatana=True)
        future = lakara_for(time="bhaviṣyat", anadyatana=True)
        self.assertEqual((past.by, past.gives), ("3.2.111", "laṅ"))
        self.assertEqual((future.by, future.gives), ("3.3.15", "luṭ"))

    def test_and_both_give_the_same_ground_for_it(self):
        rows = {r.sutra: r for r in LAKARA}
        for sutra in ("3.2.111", "3.3.15"):
            with self.subTest(sutra=sutra):
                self.assertIn("बहुव्रीहिनिर्देश", rows[sutra].why)
                self.assertIn("व्यामिश्रे", rows[sutra].why)

    def test_the_later_rule_names_the_earlier_one(self):
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("3.2.111", REGISTRY.get("3.3.15").notes)


class ARuleThatStatesNothingOfItsOwn(unittest.TestCase):
    """
    3.3.14 लृटः सद्वा takes its affixes from 3.2.127's name and its
    conditions from 3.2.124, and adds neither.
    """

    def test_it_reaches_its_affixes_through_the_name(self):
        answer = lrt_substitute(aprathama=True)
        self.assertIsInstance(answer, Added)
        self.assertEqual(answer.by, "3.3.14")
        self.assertIn(answer.gives, ("śatṛ", "śānac"))

    def test_and_only_what_bears_that_name(self):
        answer = lrt_substitute(wants="ktvā")
        self.assertIsInstance(answer, NotAdded)
        self.assertIn("3.2.127", answer.why)

    def test_the_affixes_it_offers_are_exactly_3_2_127s(self):
        """
        Not a list written here: what this rule reaches is whatever
        that rule names, so the two must agree by construction.
        """
        from src.astadhyayi.lakara import SAT, sat_samjna

        for affix in SAT:
            with self.subTest(affix=affix):
                self.assertIsInstance(sat_samjna(affix), Added)
                self.assertEqual(
                    lrt_substitute(wants=affix).gives, affix)

    def test_the_option_is_settled_by_the_lat_rules_condition(self):
        """
        व्यवस्थितविभाषा: अप्रथमासमानाधिकरणादिषु नित्यम्, अन्यत्र
        विकल्पः. Both halves must be visible in the answer, or the
        rule reads as a free option, which it is not.
        """
        self.assertIn("नित्यम्", lrt_substitute(aprathama=True).why)
        self.assertIn("नित्यम्", lrt_substitute(sambodhana=True).why)
        self.assertIn("विकल्पः", lrt_substitute().why)

    def test_and_the_dependence_is_declared(self):
        from src.astadhyayi.sutra import REGISTRY

        self.assertEqual(set(REGISTRY.get("3.3.14").reuses),
                         {"3.2.124", "3.2.127"})


class TheVasarupaSuspensionAThirdTime(unittest.TestCase):
    """
    3.1.94 lets a general affix stand beside the special one excepting
    it. 3.2.146 argued that the तच्छीलादि section suspends that, and
    3.2.177 exists because of the suspension. 3.3.10 establishes it
    again over other ground, and 3.3.11 and 3.3.12 exist because of
    it — so two pādas now turn on the same ज्ञापक.
    """

    def test_all_three_rules_of_the_run_cite_the_suspension(self):
        self.assertEqual(vasarupa_suspended(),
                         tuple(r.sutra for r in KRIYARTHA))

    def test_3_3_10_argues_it_from_its_own_redundancy(self):
        answer = kriyartha_affix(wants="ṇvul")
        self.assertEqual(answer.by, "3.3.10")
        self.assertIn("3.1.133", answer.why)
        self.assertIn("वासरूपेण तृजादयो न भवन्ति", answer.why)

    def test_and_it_names_the_earlier_section_that_did_the_same(self):
        from src.astadhyayi.sutra import REGISTRY

        notes = REGISTRY.get("3.3.10").notes
        self.assertIn("3.2.146", notes)
        self.assertIn("3.2.177", notes)

    def test_3_3_12_restates_an_affix_from_the_pada_before(self):
        answer = kriyartha_affix(karman=True)
        self.assertEqual((answer.by, answer.gives), ("3.3.12", "aṇ"))
        self.assertIn("3.2.1", answer.why)

    def test_and_that_backward_reach_is_declared(self):
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("3.2.1", REGISTRY.get("3.3.12").reuses)

    def test_the_restatement_is_a_call_and_not_a_copied_string(self):
        """
        The declaration was written before the code backed it: the row
        held the string "aṇ" and 3.3.12 declared it reused 3.2.1
        without ever asking that rule. The guard caught it — the same
        one that caught a FALSE declaration a pāda back, here catching
        a true one the code was not living up to.

        So the row now names the rule it restates and the affix is
        fetched. What must hold is that the two agree BY ASKING, not
        by having been typed the same twice.
        """
        from src.astadhyayi.bhava_krt import KRIYARTHA, restated_affix
        from src.astadhyayi.upapada_krt import upapada_affix

        row = next(r for r in KRIYARTHA if r.sutra == "3.3.12")
        self.assertEqual(row.gives, "", "3.3.12 must hold no affix of "
                                        "its own — it restates 3.2.1's")
        self.assertEqual(row.restates, "3.2.1")

        from_source = upapada_affix(root="lū", beside="kāṇḍa",
                                    role="karman")
        self.assertEqual(from_source.by, "3.2.1")
        self.assertEqual(restated_affix("3.2.1"), from_source.gives)
        self.assertEqual(kriyartha_affix(karman=True).gives,
                         from_source.gives)

    def test_and_a_rule_it_cannot_ask_gives_nothing(self):
        from src.astadhyayi.bhava_krt import restated_affix

        self.assertEqual(restated_affix("3.2.999"), "")

    def test_the_narrower_rule_wins_as_the_vrtti_says_it_must(self):
        """सोऽपवादत्वाद् ण्वुलं बाधते — with an object beside, अण्."""
        self.assertEqual(kriyartha_affix().by, "3.3.10")
        self.assertEqual(kriyartha_affix(karman=True).by, "3.3.12")


class BothOfTheirConditionsAreNeeded(unittest.TestCase):
    """
    3.3.10 has two, and the vṛtti gives a counter-example for each
    separately — so neither can be inferred from the other.
    """

    def test_no_act_beside(self):
        answer = kriyartha_affix(kriya=False)
        self.assertIsInstance(answer, NotAdded)
        self.assertIn("भिक्षिष्य", answer.why)

    def test_an_act_beside_but_not_the_purpose(self):
        answer = kriyartha_affix(kriyartha=False)
        self.assertIsInstance(answer, NotAdded)
        self.assertIn("धावतस्ते पतिष्यति दण्डः", answer.why)

    def test_a_rule_giving_two_affixes_reports_the_one_asked_after(self):
        """
        3.3.10 gives तुमुन् AND ण्वुल्. The `wants` idiom exists so the
        answer is the affix asked about — the reason it was needed in
        the तच्छीलादि run, met again here.
        """
        self.assertEqual(kriyartha_affix(wants="tumun").gives, "tumun")
        self.assertEqual(kriyartha_affix(wants="ṇvul").gives, "ṇvul")


class WhatTheOpeningLeavesOpen(unittest.TestCase):
    """Debts, asserted so that paying them is noticed."""

    def test_the_debt_3_3_11_carried_is_paid(self):
        """
        PAID. 3.3.11 named a class of affixes by pointing FORWARD to
        3.3.18, seven sūtras on, and the gap was written as a failing
        assertion. Codifying the घञ् run turned it red on schedule —
        so the assertion now runs the other way: the rule it pointed
        at answers, and 3.3.11 still names it.
        """
        from src.astadhyayi.bhava_krt import bhava_affix
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("3.3.18", {str(s.id) for s in REGISTRY.all()})
        self.assertIn("3.3.18", REGISTRY.get("3.3.11").notes)
        self.assertEqual(bhava_affix(root="pac", bhava=True).by,
                         "3.3.18")

    def test_and_what_3_3_11_gives_is_what_3_3_18_gives(self):
        """
        The class can now be checked rather than named: the affix
        3.3.11 lets stand on its ground is the one 3.3.18 supplies.
        """
        from src.astadhyayi.bhava_krt import bhava_affix

        borrowed = kriyartha_affix(bhava=True)
        source = bhava_affix(root="pac", bhava=True)
        self.assertEqual(borrowed.by, "3.3.11")
        self.assertIn(source.gives, borrowed.gives)

    def test_all_three_lakara_debts_are_paid(self):
        """
        ALL THREE PAID. 3.4.6 gives the Vedic set for any time; 3.4.69
        says what a लकार DENOTES; 3.4.77 enumerates the ten and says
        which are टित्.

        NORTH_STAR carried these from 3.2.110, where the table began
        naming its endings as bare strings. What the last of them buys
        is a check nothing could run before — every ending the table
        gives, across three pādas, against the rule that lists them.
        """
        from src.astadhyayi.lakara import LAKARA, LAKARA_LIST
        from src.astadhyayi.sutra import REGISTRY

        have = {str(s.id) for s in REGISTRY.all()}
        for sutra in ("3.4.6", "3.4.69", "3.4.77"):
            with self.subTest(sutra=sutra):
                self.assertIn(sutra, have)

        ten = {name for name, _ in LAKARA_LIST}
        given = {row.gives for row in LAKARA}
        self.assertTrue(given)
        self.assertEqual(given - ten, set())

    def test_and_a_lakara_now_has_a_meaning_and_a_form(self):
        from src.astadhyayi.denoted import lakara_denotes
        from src.astadhyayi.lakara import TIN

        self.assertEqual(lakara_denotes(), ("karman", "kartṛ"))
        self.assertEqual(lakara_denotes(akarmaka=True),
                         ("bhāva", "kartṛ"))
        self.assertEqual(len(TIN), 18)
    def test_and_the_rule_that_cited_it_can_now_be_checked(self):
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("3.4.6", REGISTRY.get("3.2.105").notes)
        self.assertEqual(
            REGISTRY.get("3.4.6").apply.__name__, "lakara_for")
    def test_it_runs_unbroken_from_its_first_sutra(self):
        from src.astadhyayi.sutra import REGISTRY

        numbers = sorted(
            int(str(s.id).rsplit(".", 1)[1]) for s in REGISTRY.all()
            if str(s.id).startswith("3.3."))
        self.assertTrue(numbers)
        self.assertEqual(numbers, list(range(1, len(numbers) + 1)))

    def test_every_rule_is_answered_by_exactly_one_entry_point(self):
        from src.astadhyayi.sutra import REGISTRY

        registered = {str(x.id) for x in REGISTRY.all()
                      if str(x.id).startswith("3.3.")}
        by_apply = {}
        for x in REGISTRY.all():
            if str(x.id).startswith("3.3."):
                by_apply.setdefault(x.apply.__name__, set()).add(
                    str(x.id))
        seen = set()
        for ids in by_apply.values():
            self.assertEqual(seen & ids, set())
            seen |= ids
        self.assertEqual(seen, registered)

    def test_the_gamyadi_words_are_licensed_whole(self):
        for word in GAMYADI:
            with self.subTest(word=word):
                self.assertEqual(gamyadi(word).by, "3.3.3")
        self.assertIsInstance(gamyadi("pacati"), NotAdded)

    def test_and_the_affix_carries_the_time_not_the_root(self):
        self.assertIn("प्रत्ययस्यैव भविष्यत्कालता",
                      gamyadi("gamī").why)


if __name__ == "__main__":
    unittest.main()
