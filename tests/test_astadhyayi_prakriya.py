# -*- coding: utf-8 -*-
"""
The derivation engine — src/astadhyayi/prakriya.py.

Every rule codified before this answered a question put to it. None applied
itself to a form and handed the result on. This is the frame that does, and
what makes it faithful is not the loop but what it consults before each step.

Two things are tested apart, because they fail apart:

  * the **chain** — that डुकृञ् actually becomes कृ, by the right sūtras, in
    an order that matters;
  * the **machinery** — that 1.4.2 is consulted where two rules contend for
    one place and *not* where they act in different places. The real rule
    set never produces a genuine conflict, so those tests build one. They
    are labelled as constructed, and they test the engine, not the grammar.
"""

from __future__ import annotations

import unittest

from src.astadhyayi.prakriya import (
    MAX_STEPS, Operational, State, Term, can_see, derive,
)
from src.astadhyayi.prakriya_rules import MARKING, all_rules, upadesa
from src.astadhyayi.vipratisedha import Strength


class TheItDeletionChain(unittest.TestCase):
    """1.3.2–1.3.9, the only complete operational chain yet codified."""

    def derive(self, form, role="dhātu"):
        return derive(upadesa(form, role), all_rules())

    def test_dukrn_becomes_kr(self):
        self.assertEqual(self.derive("ḍukṛñ").surface, "kṛ")

    def test_and_says_which_sutra_did_what(self):
        """
        A result is not a derivation. What makes it one is that each step
        names the rule that authorised it — and those names are not written
        here. They come from `itsamjna`, which records the sūtra on every
        mark it makes.
        """
        cited = [step.sutra for step in self.derive("ḍukṛñ").steps]
        self.assertIn("1.3.5", cited)          # the initial डु
        self.assertIn("1.3.3", cited)          # the final ञ्
        self.assertEqual(cited[-1], "1.3.9")   # and then लोप

    def test_the_order_matters_and_lopa_is_last(self):
        """
        1.3.9 removing the final before 1.3.5 had looked at the opening
        would leave डु unexamined. The rule states its own condition — लोप
        applies to *what has been named* — so it waits.
        """
        for form, role in (("ḍukṛñ", "dhātu"), ("ṇic", "pratyaya"),
                           ("ḍudāñ", "dhātu")):
            with self.subTest(form=form):
                steps = self.derive(form, role).steps
                lopa = [i for i, s in enumerate(steps) if s.sutra == "1.3.9"]
                self.assertEqual(lopa, [len(steps) - 1])

    def test_more_worked_forms(self):
        for form, role, expected in (
            ("ḍudāñ", "dhātu", "dā"),
            ("ṇic", "pratyaya", "i"),
            ("sup", "vibhakti", "su"),
        ):
            with self.subTest(form=form):
                self.assertEqual(self.derive(form, role).surface, expected)

    def test_a_form_with_no_it_letters_stops_at_once(self):
        found = self.derive("bhū")
        self.assertEqual(found.surface, "bhū")
        self.assertEqual(found.steps, ())
        self.assertEqual(found.stopped, "no rule applies")

    def test_1_3_4s_prohibition_is_honoured_without_being_a_step(self):
        """
        न विभक्तौ तुस्माः takes a name away rather than conferring one, and
        `analyze` applies it when deciding what is marked at all. So it
        never appears in the trace — but the same letters derive differently
        depending on whether they are a case ending, which is the proof that
        it is doing something.
        """
        as_ending = self.derive("bhyas", "vibhakti")
        as_affix = self.derive("bhyas", "pratyaya")

        # The स् survives the it-rules as a case ending and does not as a
        # plain affix, which is the whole of what 1.3.4 does. This test used
        # to assert the vibhakti came through *untouched* — true until
        # 8.2.66 and 8.3.15 were codified, and now false for a good reason:
        # a word-final स् is a visarga. The surviving स् is still visible,
        # as the ः it became.
        self.assertTrue(as_ending.surface.endswith("ḥ"))
        self.assertEqual(as_affix.surface, "bhya")
        self.assertNotIn(
            "1.3.9", [s.sutra for s in as_ending.steps
                      if s.before.endswith("s")][:1] or ["1.3.9"])

    def test_the_trace_reads_as_a_derivation(self):
        text = self.derive("ḍukṛñ").trace()
        self.assertIn("ḍukṛñ", text)
        self.assertIn("kṛ", text)
        self.assertIn("1.3.9", text)


class WhenTwoRulesWantTheSamePlace(unittest.TestCase):
    """
    1.4.2 विप्रतिषेधे परं कार्यम्, and the definition that gates it.

    The rules below are constructed. The codified operational set produces
    no genuine conflict — the it-marking rules act on different letters — so
    testing the engine's most important behaviour needs a conflict built on
    purpose. These test the engine, not the grammar.
    """

    def rule(self, sutra, text, site="same", standing=Strength.EQUAL):
        def matches(state, _text=text):
            return state.surface != _text

        def perform(_state, _text=text):
            return State((Term(text=_text),))

        return Operational(sutra=sutra, what="to " + text, standing=standing,
                           matches=matches, perform=perform,
                           site=lambda _state, _s=site: _s)

    def test_the_later_rule_is_done(self):
        found = derive(State((Term(text="x"),)),
                       [self.rule("7.3.101", "a"), self.rule("7.3.103", "b")],
                       max_steps=1)
        self.assertEqual(found.steps[0].sutra, "7.3.103")
        self.assertEqual(found.surface, "b")

    def test_and_the_loser_is_named(self):
        """A derivation that does not say what it displaced cannot be checked."""
        found = derive(State((Term(text="x"),)),
                       [self.rule("7.3.101", "a"), self.rule("7.3.103", "b")],
                       max_steps=1)
        self.assertEqual(found.steps[0].against, ("7.3.101",))
        self.assertTrue(found.steps[0].why)

    def test_an_apavada_beats_the_later_rule(self):
        """
        The first of 1.4.2's three exclusions. An exception defeats the rule
        it excepts however the numbers fall, and `vipratisedha` knows it —
        the engine has only to ask, rather than compare numbers itself.
        """
        found = derive(
            State((Term(text="x"),)),
            [self.rule("7.3.101", "a", standing=Strength.APAVADA),
             self.rule("7.3.103", "b")],
            max_steps=1)
        self.assertEqual(found.steps[0].sutra, "7.3.101")
        self.assertEqual(found.surface, "a")


class WhenTwoRulesWantDifferentPlaces(unittest.TestCase):
    """
    The defect the first draft had, and the reason `site` exists.

    विप्रतिषेध is two rules reaching *one* place at once — एकस्मिन् युगपत्.
    The engine called 1.4.2 on every turn where more than one rule matched,
    which made 1.3.5 marking the opening of डुकृञ् and 1.3.3 marking its
    final look like rivals, and put 1.4.2's name on an ordering it never
    decided. Both rules simply apply; neither displaces anything.
    """

    def test_no_step_of_a_real_derivation_claims_to_displace_anything(self):
        for form, role in (("ḍukṛñ", "dhātu"), ("ṇic", "pratyaya"),
                           ("ḍudāñ", "dhātu"), ("sup", "vibhakti")):
            for step in derive(upadesa(form, role), all_rules()).steps:
                with self.subTest(form=form, sutra=step.sutra):
                    self.assertEqual(step.against, ())
                    self.assertEqual(step.why, "")

    def test_but_both_rules_still_run(self):
        """Not conflicting is not the same as not applying."""
        cited = {s.sutra for s in derive(upadesa("ḍukṛñ"), all_rules()).steps}
        self.assertEqual(cited, {"1.3.3", "1.3.5", "1.3.9"})


class TheLoopTerminates(unittest.TestCase):
    def test_a_rule_that_matches_but_changes_nothing_stops_it(self):
        """
        The failure mode a loop like this has. Better to stop and name the
        rule that did it than to spin to the cap.
        """
        idle = Operational(sutra="9.9.9", what="does nothing",
                           matches=lambda _s: True,
                           perform=lambda state: state)
        found = derive(State((Term(text="x"),)), [idle])
        self.assertEqual(found.steps, ())
        self.assertIn("9.9.9", found.stopped)
        self.assertIn("changed nothing", found.stopped)

    def test_a_derivation_that_will_not_converge_says_so(self):
        flip = Operational(
            sutra="9.9.8", what="flips",
            matches=lambda _s: True,
            perform=lambda state: State(
                (Term(text="b" if state.surface == "a" else "a"),)))
        found = derive(State((Term(text="a"),)), [flip], max_steps=6)
        self.assertEqual(len(found.steps), 6)
        self.assertIn("cap", found.stopped)

    def test_the_default_cap_is_generous_enough_for_a_real_prakriya(self):
        self.assertGreaterEqual(MAX_STEPS, 40)


class TheEngineAsksWhatIsVisible(unittest.TestCase):
    """
    8.2.1 पूर्वत्रासिद्धम्, the other thing consulted at every step. It is
    not decoration: it switches 1.4.2 off for the last quarter of the
    grammar, so an engine consulting only the first would derive the tripādī
    wrongly and with complete confidence.
    """

    def test_a_later_rules_work_is_invisible_to_a_preceding_one(self):
        """
        पूर्वत्रासिद्धम् reads *asiddha in respect of what precedes*, and the
        direction is the whole content of the rule. These two assertions
        were first written the other way round, from memory rather than
        from the sūtra, and `asiddha.py` — which had read it properly — was
        the thing that showed it.
        """
        # 8.2.31 stands later; to 6.1.87, before the tripādī, it has not
        # happened at all.
        self.assertFalse(can_see("8.2.31", "6.1.87"))
        # and the same within the tripādī itself
        self.assertFalse(can_see("8.2.31", "8.2.7"))

    def test_but_a_preceding_rules_work_is_there_to_be_seen(self):
        """
        The converse, and it has to hold or the tripādī could not proceed:
        rules apply down the text, so by the time a later one is reached the
        earlier has already done its work and is visible.
        """
        self.assertTrue(can_see("8.2.7", "8.2.31"))


class WhatTheRuleSetCovers(unittest.TestCase):
    def test_the_marking_rules_are_the_ones_that_confer_the_name(self):
        cited = {sutra for sutra, _ in MARKING}
        self.assertEqual(
            cited, {"1.3.2", "1.3.3", "1.3.5", "1.3.6", "1.3.7", "1.3.8"})

    def test_every_operational_rule_names_a_codified_sutra(self):
        import src.astadhyayi.rules  # noqa: F401
        from src.astadhyayi.sutra import REGISTRY

        for rule in all_rules():
            with self.subTest(sutra=rule.sutra):
                self.assertTrue(REGISTRY.has(rule.sutra))

    def test_an_operation_named_by_a_rule_is_in_the_vocabulary(self):
        from src.astadhyayi.operations import is_operation

        for rule in all_rules():
            if rule.operation:
                with self.subTest(sutra=rule.sutra):
                    self.assertTrue(is_operation(rule.operation))


if __name__ == "__main__":
    unittest.main()


class TheFirstWholeWord(unittest.TestCase):
    """
    जयति, derived from जि in nine steps.

    The five sūtras it needs were chosen by working backwards from the word
    rather than by going down the list, and that is the point of the class:
    the result is checkable against a derivation any grammarian can confirm,
    instead of against our own worked examples.
    """

    def derive_verb(self, root, ending="tip"):
        from src.astadhyayi.prakriya_rules import verb
        return derive(verb(root, ending=ending), all_rules())

    def test_ji_becomes_jayati(self):
        self.assertEqual(self.derive_verb("ji").surface, "jayati")

    def test_and_stops_there(self):
        """
        It did not, at first. 6.1.78 turns जे into जय्, जय् ends in a
        consonant, and 1.3.3 हलन्त्यम् duly called that consonant an इत् —
        so जयति came out जाति. The rule that stops it is 1.3.2's first
        word, उपदेशे, read down over the whole it-section: those rules look
        at a form as the grammar states it, never at one the derivation has
        made.
        """
        found = self.derive_verb("ji")
        self.assertEqual(found.stopped, "no rule applies")
        self.assertEqual(found.steps[-1].sutra, "6.1.78")

    def test_every_step_names_a_codified_sutra(self):
        import src.astadhyayi.rules  # noqa: F401
        from src.astadhyayi.sutra import REGISTRY

        for step in self.derive_verb("ji").steps:
            with self.subTest(sutra=step.sutra):
                self.assertTrue(REGISTRY.has(step.sutra))

    def test_the_five_rules_it_needs_all_appear(self):
        """
        A derivation that reached the right string by another route would
        pass the first test and mean nothing.
        """
        cited = [s.sutra for s in self.derive_verb("ji").steps]
        for sutra in ("1.3.3", "1.3.8", "1.3.9", "3.1.68", "7.3.84", "6.1.78"):
            with self.subTest(sutra=sutra):
                self.assertIn(sutra, cited)

    def test_the_order_is_the_one_the_grammar_takes(self):
        cited = [s.sutra for s in self.derive_verb("ji").steps]
        self.assertLess(cited.index("3.1.68"), cited.index("7.3.84"))
        self.assertLess(cited.index("7.3.84"), cited.index("6.1.78"))

    def test_a_root_with_no_ik_gets_no_guna(self):
        """
        1.1.3 इको गुणवृद्धी decides where guṇa lands, and a root with no ik
        offers it nowhere: पचति keeps its अ.

        The root is given as the dhātupāṭha enunciates it — डुपचँष्, entry
        01.1151 — and not as the bare पच्. That is not fussiness. This test
        was first written with "pac" and the engine returned पाति, having
        quite correctly called the final च् an इत् by 1.3.3: it had been
        told the form was an upadeśa, and in an upadeśa a final consonant
        is exactly what that rule marks. The wrong input, not the wrong
        rule.
        """
        found = self.derive_verb("ḍupaca̐ṣ")
        cited = [s.sutra for s in found.steps]
        self.assertEqual(found.surface, "pacati")
        self.assertIn("3.1.68", cited)
        self.assertNotIn("7.3.84", cited)

    def test_the_it_rules_all_get_exercised_on_a_real_upadesa(self):
        """डुपचँष् carries three kinds of it-letter between its two ends."""
        cited = [s.sutra for s in self.derive_verb("ḍupaca̐ṣ").steps]
        self.assertIn("1.3.2", cited)      # the anunāsika अँ
        self.assertIn("1.3.3", cited)      # the final ष्
        self.assertIn("1.3.5", cited)      # the initial डु

    def test_the_upadesa_flag_is_what_protects_the_result(self):
        """Directly, so the guard cannot be removed without a red test."""
        from src.astadhyayi.prakriya import Term

        plain = Term(text="jay", role="dhātu")
        self.assertTrue(plain.upadesa)
        self.assertFalse(plain.altered("jay").upadesa)


class TheInterpretiveRulesAreDoingTheWork(unittest.TestCase):
    """
    7.3.84 says गुणः and names no target; 6.1.78 gives four substitutes for
    four sounds and does not pair them. Neither gap is filled here — they
    are filled by rules codified long before, and the verdicts say so.
    """

    def test_7_3_84_defers_to_1_1_3_and_1_1_50(self):
        from src.astadhyayi.anga import guna_before_affix

        found = guna_before_affix("ji", sarvadhatuka=True)
        self.assertEqual(found.result, "je")
        self.assertIn("1.1.3", found.through)     # which vowel
        self.assertIn("1.1.50", found.through)    # which replacement

    def test_and_1_1_51_joins_in_for_r(self):
        """
        वृद्धि of ऋ is ār in two steps: 1.1.50 gives आ as the nearest, then
        1.1.51 उरण् रपरः adds the र्. A single lookup table would have got
        the same string and shown none of it.
        """
        from src.astadhyayi.anga import mrjer_vrddhi

        found = mrjer_vrddhi("mṛj")
        self.assertEqual(found.result, "mārj")
        self.assertIn("1.1.51", found.through)

    def test_6_1_78_pairs_its_lists_through_1_3_10(self):
        from src.astadhyayi.anga import AYAV, ayadi, ec

        # एच् is not listed in anga.py. It is resolved from the śivasūtras
        # through 1.1.71, which is what the sūtra's own abbreviation means.
        self.assertEqual(ec(), ("e", "o", "ai", "au"))
        self.assertEqual(len(ec()), len(AYAV))
        for source, expected in (("je", "jay"), ("lo", "lav"),
                                 ("cai", "cāy"), ("lau", "lāv")):
            with self.subTest(source=source):
                self.assertEqual(ayadi(source).result, expected)

    def test_and_1_3_10_would_refuse_unequal_lists(self):
        """
        The reason the pairing is asked for rather than written out: if
        either list were mis-copied, 1.3.10 refuses rather than pairing
        what it can, and 6.1.78 returns nothing instead of a wrong sound.
        """
        from src.astadhyayi.reading import yathasamkhya

        self.assertIsNotNone(yathasamkhya(("e", "o"), ("ay", "av")))
        self.assertIsNone(yathasamkhya(("e", "o", "ai"), ("ay", "av")))


class TheEngineAsksTheRulesItAlreadyHas(unittest.TestCase):
    """
    The engine used to choose the ending itself — तिप्, written in — while
    eighty codified sūtras of pada selection sat unconsulted. एध् is
    anudāttet, 1.3.12 makes it middle, and the engine said एधति.

    A dependency that exists in the grammar and in this codebase, and was
    not reflected in the code that needed it. It now asks.
    """

    def derive_verb(self, root):
        from src.astadhyayi.prakriya_rules import verb
        return derive(verb(root), all_rules())

    def test_an_anudattet_root_takes_the_middle(self):
        self.assertEqual(self.derive_verb("edha̐").surface, "edhate")

    def test_a_ngit_root_does_too(self):
        """
        शीङ् is ṅit, so 1.3.12 gives it the middle — and it is also a
        *second-gaṇa* root, 02.0026 शीङ् स्वप्ने, so 2.4.72 elides its शप्
        and the form is शेते, not शयते.

        This test asserted शयते and passed, before 2.4.72 was codified: the
        engine was giving every root a शप् whatever its gaṇa, and the test
        had frozen the wrong form. Codifying the rule corrected the word and
        failed the test, which is the right way round.
        """
        self.assertEqual(self.derive_verb("śīṅ").surface, "śete")

    def test_and_the_second_gana_loses_its_sap(self):
        """एति, अत्ति, हन्ति — no अ between root and ending."""
        for root, expected in (("iṇ", "eti"), ("ada̐", "atti"),
                               ("hana̐", "hanti")):
            with self.subTest(root=root):
                found = self.derive_verb(root)
                self.assertEqual(found.surface, expected)
                self.assertIn("2.4.72", [s.sutra for s in found.steps])

    def test_but_a_first_gana_root_keeps_it(self):
        for root, expected in (("bhū", "bhavati"), ("ḍupaca̐ṣ", "pacati")):
            with self.subTest(root=root):
                found = self.derive_verb(root)
                self.assertEqual(found.surface, expected)
                self.assertNotIn("2.4.72", [s.sutra for s in found.steps])

    def test_the_nasals_are_not_jhal(self):
        """
        8.4.55 hardens a झल् before a खर्, and the nasals are not झल्.
        Checking only that the sound sits in a varga row let न् through and
        हन् + ति came out हत्ति.
        """
        from src.astadhyayi.anga import khari_ca

        self.assertEqual(khari_ca("d", "ti").result, "t")
        self.assertIsNone(khari_ca("n", "ti").result)

    def test_and_the_residue_takes_the_active(self):
        for root, expected in (("ji", "jayati"), ("bhū", "bhavati")):
            with self.subTest(root=root):
                self.assertEqual(self.derive_verb(root).surface, expected)

    def test_the_pada_comes_from_1_3_12_and_not_from_the_engine(self):
        """
        Asserted at the source, so the wiring cannot be quietly undone: the
        ending is whatever the pada rules and the 1.4.99 tables say.
        """
        from src.astadhyayi.atmanepada import Pada, pada_of_usage
        from src.astadhyayi.prakriya_rules import verb

        self.assertIs(pada_of_usage("edha̐").pada, Pada.ATMANEPADA)
        self.assertEqual(verb("edha̐").terms[1].text, "ta")
        self.assertIn("ātmanepada", verb("edha̐").terms[1].samjnas)

        self.assertIs(pada_of_usage("ji").pada, Pada.PARASMAIPADA)
        self.assertEqual(verb("ji").terms[1].text, "tip")

    def test_the_root_initial_is_fixed_by_6_1_65(self):
        """णीञ् — the Kāśikā's own example for that sūtra."""
        found = self.derive_verb("ṇīñ")
        self.assertEqual(found.surface, "nayati")
        self.assertIn("6.1.65", [s.sutra for s in found.steps])


class AnExactUpadesaIsNotCollapsedToAName(unittest.TestCase):
    """
    डुपचँष् is one of three dhātupāṭha entries called पच्, and the only
    svaritet among them. Asked by name, the accent of another entry
    answered — 01.0198 पचिँ is anudāttet — so the engine derived पचते and
    called it 1.3.12.

    पच् is ubhayapadī for exactly the reason that got lost: *this* entry is
    svaritet, and 1.3.72 makes the middle conditional on कर्त्रभिप्राय
    rather than automatic. A caller who writes the whole upadeśa has
    already disambiguated, and the lookup was discarding it.
    """

    def test_the_exact_entry_wins_over_the_bare_name(self):
        from src.astadhyayi.pada import entries_for

        by_name = entries_for("pac")
        self.assertGreater(len(by_name), 1, "pac should be ambiguous")

        exact = entries_for("ḍupaca̐ṣ")
        self.assertEqual(len(exact), 1)
        self.assertEqual(exact[0].code, "01.1151")

    def test_and_the_pada_verdict_follows_that_entry(self):
        from src.astadhyayi.atmanepada import Pada, pada_of_usage

        verdict = pada_of_usage("ḍupaca̐ṣ")
        self.assertIs(verdict.pada, Pada.PARASMAIPADA)
        self.assertEqual(verdict.by, "1.3.78")

    def test_so_the_derivation_is_pacati(self):
        from src.astadhyayi.prakriya_rules import verb

        self.assertEqual(
            derive(verb("ḍupaca̐ṣ"), all_rules()).surface, "pacati")

    def test_a_genuinely_anudattet_root_is_still_middle(self):
        """The fix must not simply switch everything to the active."""
        from src.astadhyayi.atmanepada import Pada, pada_of_usage

        verdict = pada_of_usage("edha̐")
        self.assertIs(verdict.pada, Pada.ATMANEPADA)
        self.assertEqual(verdict.by, "1.3.12")
