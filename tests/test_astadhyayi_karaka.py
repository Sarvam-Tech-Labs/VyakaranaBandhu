# -*- coding: utf-8 -*-
"""
Tests for 1.4.23 to 1.4.55 — the kārakas.

The individual definitions are easy to test and easy to get right. What is
worth testing here is the thing that makes the section a system rather than a
list: **the order of the six names is the mechanism.** They stand under 1.4.1,
where one name only applies and the later stands, and Pāṇini has arranged them
so the later is always the one wanted.

Three consequences follow, and each is tested below:

  * कर्तृ is last and displaces everything. A participant that is both the
    most effective means and the independent one comes out कर्तृ.
  * 1.4.38 and 1.4.46–1.4.48 do nothing *but* move a case later — from
    सम्प्रदान or अधिकरण to कर्मन्. Under any reading that ignores 1.4.1 they
    would merely add a second name and change no outcome.
  * 1.4.55 breaks the rule on purpose, with a च and a stated reason.

A codification that resolved by "the first rule that matches" would pass every
single-condition test in this file and fail all three of those.
"""

from __future__ import annotations

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi.karaka import (
    FACTS,
    PROVISIONS,
    VERB_SENSES,
    Karaka,
    Participant,
    karaka_of,
    near_misses,
    provisions_for,
)
from src.astadhyayi.sources import facts
from src.astadhyayi.sutra import REGISTRY

A, S, KR = Karaka.APADANA, Karaka.SAMPRADANA, Karaka.KARANA
ADH, KM, KT, H = (Karaka.ADHIKARANA, Karaka.KARMAN, Karaka.KARTR,
                  Karaka.HETU)


#: (sūtra, the form the Kāśikā works, what is asserted, the name it takes)
WORKED = [
    # अपादान
    ("1.4.24", "grāmād āgacchati", dict(given=["dhruva-apāya"]), A),
    ("1.4.25", "corād bibheti",
     dict(verb_sense=["bhī-trā"], given=["bhaya-hetu"]), A),
    ("1.4.26", "adhyayanāt parājayate",
     dict(verb="ji", upasargas=["parā"], given=["asoḍha"]), A),
    ("1.4.27", "yavebhyo gāṃ vārayati",
     dict(verb_sense=["vāraṇa"], given=["vāraṇa-īpsita"]), A),
    ("1.4.28", "upādhyāyād antardhatte",
     dict(given=["antardhi-adarśana"]), A),
    ("1.4.29", "upādhyāyād adhīte", dict(given=["ākhyātā-upayoga"]), A),
    ("1.4.30", "brahmaṇaḥ prajāḥ prajāyante",
     dict(given=["jani-prakṛti"]), A),
    ("1.4.31", "himavato gaṅgā prabhavati",
     dict(verb="bhū", given=["prabhava"]), A),
    # सम्प्रदान
    ("1.4.32", "brāhmaṇāya gāṃ dadāti",
     dict(given=["karmaṇā-abhipreta"]), S),
    ("1.4.33", "devadattāya rocate",
     dict(verb_sense=["ruc"], given=["prīyamāṇa"]), S),
    ("1.4.34", "devadattāya ślāghate",
     dict(verb_sense=["ślāgh-hnu-sthā-śap"], given=["jñīpsyamāna"]), S),
    ("1.4.35", "devadattāya śataṃ dhārayati",
     dict(verb_sense=["dhṛ"], given=["uttamarṇa"]), S),
    ("1.4.36", "puṣpebhyaḥ spṛhayati",
     dict(verb_sense=["spṛh"], given=["spṛhā-īpsita"]), S),
    ("1.4.37", "devadattāya krudhyati",
     dict(verb_sense=["krudh-druh-īrṣyā-asūyā"], given=["kopa-viṣaya"]), S),
    ("1.4.39", "devadattāya rādhyati",
     dict(verb_sense=["rādh-īkṣ"], given=["vipraśna"]), S),
    ("1.4.40", "devadattāya pratiśṛṇoti",
     dict(verb="śru", upasargas=["prati"], given=["pūrvasya-kartā"]), S),
    ("1.4.41", "devadattāya anugṛṇāti",
     dict(verb="gṝ", upasargas=["anu"], given=["pūrvasya-kartā"]), S),
    # करण, अधिकरण
    ("1.4.42", "dātreṇa lunāti", dict(given=["sādhakatama"]), KR),
    ("1.4.45", "kaṭe āste", dict(given=["ādhāra"]), ADH),
    # कर्मन्
    ("1.4.49", "kaṭaṃ karoti", dict(given=["īpsitatama"]), KM),
    ("1.4.50", "viṣaṃ bhuṅkte", dict(given=["anīpsita-tathāyukta"]), KM),
    ("1.4.51", "māṇavakaṃ panthānaṃ pṛcchati", dict(given=["akathita"]), KM),
    ("1.4.52", "māṇavakaṃ grāmaṃ gamayati",
     dict(causative=True,
          verb_sense=["gati-buddhi-pratyavasāna-śabdakarman-akarmaka"],
          given=["aṇau-kartā"]), KM),
    # कर्तृ
    ("1.4.54", "devadattaḥ pacati", dict(given=["svatantra"]), KT),
    ("1.4.54", "sthālī pacati", dict(given=["svatantra"]), KT),
]


class WorkedForms(unittest.TestCase):
    def test_each_comes_out_as_the_kasika_says(self):
        for sutra, form, asserted, expected in WORKED:
            with self.subTest(sutra=sutra, form=form):
                verdict = karaka_of(**asserted)
                self.assertIs(verdict.karaka, expected,
                              f"{sutra} {form}: {verdict.by}")
                self.assertEqual(verdict.by, sutra, form)

    def test_the_table_covers_every_sutra_that_assigns_a_name(self):
        tested = {row[0] for row in WORKED}
        assigning = {p.sutra.split("v")[0] for p in PROVISIONS}
        # These five are tested in their own classes below, because what
        # matters about them is what they displace.
        elsewhere = {"1.4.38", "1.4.43", "1.4.44", "1.4.46", "1.4.47",
                     "1.4.48", "1.4.53", "1.4.55"}
        self.assertEqual(sorted(assigning - tested - elsewhere), [])


class TheOrderIsTheMechanism(unittest.TestCase):
    """
    What makes this a system: the six stand under 1.4.1, and the later wins.
    """

    def test_kartr_is_last_and_displaces_everything(self):
        """
        An agent could equally be described as the most effective means. It
        comes out कर्तृ because 1.4.54 stands after 1.4.42 and one name only
        may apply.
        """
        verdict = karaka_of(given=["sādhakatama", "svatantra"])
        self.assertIs(verdict.karaka, KT)
        self.assertEqual(verdict.by, "1.4.54")
        self.assertIn("1.4.42", verdict.instead_of)

    def test_karman_displaces_adhikarana(self):
        """
        गेहं प्रविशति is the Kāśikā's own case: without the second mention of
        कर्म at 1.4.49 it would come out अधिकरण — पुनः कर्मग्रहणम्
        आधारनिवृत्त्यर्थम्, इतरथा आधारस्यैव हि स्यात्.
        """
        verdict = karaka_of(given=["īpsitatama", "ādhāra"])
        self.assertIs(verdict.karaka, KM)
        self.assertIn("1.4.45", verdict.instead_of)

    def test_1_4_38_exists_only_to_move_a_case_later(self):
        """
        Without an upasarga क्रुध् gives सम्प्रदान; with one, कर्मन्. Both
        rules match the second case, and it is 1.4.1 that leaves the later.
        """
        plain = dict(verb="krudh", verb_sense=["krudh-druh-īrṣyā-asūyā"],
                     given=["kopa-viṣaya"])
        self.assertIs(karaka_of(**plain).karaka, S)
        self.assertEqual(karaka_of(**plain).by, "1.4.37")

        prefixed = karaka_of(upasargas=["abhi"], **plain)
        self.assertIs(prefixed.karaka, KM)
        self.assertEqual(prefixed.by, "1.4.38")

    def test_the_three_adhikarana_to_karman_sutras_do_the_same(self):
        """1.4.46, 1.4.47 and 1.4.48, each moving a locus to an object."""
        for verb, upasarga, sutra in (("śī", "adhi", "1.4.46"),
                                      ("sthā", "adhi", "1.4.46"),
                                      ("ās", "adhi", "1.4.46"),
                                      ("viś", "abhi", "1.4.47"),
                                      ("vas", "upa", "1.4.48"),
                                      ("vas", "anu", "1.4.48")):
            with self.subTest(verb=verb, sutra=sutra):
                verdict = karaka_of(verb=verb, upasargas=[upasarga],
                                    given=["ādhāra"])
                self.assertIs(verdict.karaka, KM)
                self.assertEqual(verdict.by, sutra)
                self.assertIn("1.4.45", verdict.instead_of)

    def test_and_without_the_prefix_they_stay_a_locus(self):
        """Which is what makes those three sūtras do anything at all."""
        for verb in ("śī", "sthā", "ās", "viś", "vas"):
            verdict = karaka_of(verb=verb, given=["ādhāra"])
            self.assertIs(verdict.karaka, ADH, verb)
            self.assertEqual(verdict.by, "1.4.45", verb)

    #: The sūtra that *defines* each name, as against those that extend it.
    DEFINITIONS = [("1.4.24", A), ("1.4.32", S), ("1.4.42", KR),
                   ("1.4.45", ADH), ("1.4.49", KM), ("1.4.54", KT)]

    def test_the_six_definitions_stand_in_the_order_the_mechanism_needs(self):
        """
        A structural check rather than a worked form.

        An earlier version of this test asserted the stronger claim that the
        *first* sūtra assigning each name is in that order, and it failed:
        1.4.38 assigns कर्मन् and stands before 1.4.45's अधिकरण. The
        arrangement is not a global ordering of the names but a pairwise one —
        each rule stands after the rule it is meant to displace, and 1.4.38
        never competes with 1.4.45. The claim as corrected is about the six
        definitions.
        """
        numbers = [int(s.rsplit(".", 1)[1]) for s, _ in self.DEFINITIONS]
        self.assertEqual(numbers, sorted(numbers))
        for sutra, name in self.DEFINITIONS:
            self.assertIn(
                name, [p.gives for p in provisions_for(sutra)], sutra)

    def test_and_every_rule_that_displaces_stands_after_what_it_displaces(self):
        """
        The pairwise property, which is the one the section actually relies
        on. Each of these moves a participant from an earlier name to a later
        one, and would do nothing if it stood the other way round.
        """
        moves = [
            ("1.4.38", dict(verb="krudh",
                            verb_sense=["krudh-druh-īrṣyā-asūyā"],
                            upasargas=["abhi"], given=["kopa-viṣaya"])),
            ("1.4.43", dict(verb="div", given=["sādhakatama"])),
            ("1.4.46", dict(verb="śī", upasargas=["adhi"], given=["ādhāra"])),
            ("1.4.47", dict(verb="viś", upasargas=["abhi"], given=["ādhāra"])),
            ("1.4.48", dict(verb="vas", upasargas=["upa"], given=["ādhāra"])),
        ]
        for sutra, asserted in moves:
            with self.subTest(sutra=sutra):
                verdict = karaka_of(**asserted)
                self.assertEqual(verdict.by, sutra)
                self.assertTrue(verdict.instead_of, f"{sutra} displaced nothing")
                for displaced in verdict.instead_of:
                    self.assertLess(
                        int(displaced.rsplit(".", 1)[1]),
                        int(sutra.rsplit(".", 1)[1]),
                        f"{sutra} must stand after {displaced}",
                    )


class HetuAndKartrTogether(unittest.TestCase):
    """1.4.55, where the section breaks its own governing rule."""

    def test_the_causer_takes_both_names(self):
        verdict = karaka_of(given=["prayojaka"])
        self.assertIs(verdict.karaka, H)
        self.assertIs(verdict.also, KT)
        self.assertEqual(verdict.by, "1.4.55")

    def test_and_the_reason_is_recorded(self):
        """
        संज्ञासमावेशार्थश्चकारः, and why both are needed: हेतुत्वाद् णिचो
        निमित्तं, कर्तृत्वाच्च कर्तृप्रत्ययेनोच्यते.
        """
        verdict = karaka_of(given=["prayojaka"])
        self.assertIn("संज्ञासमावेशार्थश्चकारः", verdict.why)
        self.assertIn("णिचो", verdict.why)

    def test_it_is_the_only_provision_that_does_this(self):
        """
        Which is what makes it an exception rather than the rule. If a second
        one appeared, 1.4.1 would be doing much less than the section's
        arrangement assumes.
        """
        both = [p for p in PROVISIONS if p.alongside is not None]
        self.assertEqual([p.sutra for p in both], ["1.4.55"])

    def test_it_bears_on_the_open_question_at_1_4_20(self):
        """
        Both are cases of संज्ञासमावेश restored inside 1.4.1's scope. Here it
        is done in a sūtra with a stated purpose; at 1.4.20 by a vārttika with
        none. Recording the parallel is what makes the open question specific
        rather than vague.
        """
        notes = REGISTRY.get("1.4.55").notes
        self.assertIn("1.4.20", notes)
        self.assertIn("OPEN", REGISTRY.get("1.4.20").notes)


class Karake(unittest.TestCase):
    """1.4.23 — the condition all six wait on."""

    def test_nothing_asserted_gets_no_name(self):
        verdict = karaka_of()
        self.assertIsNone(verdict.karaka)
        self.assertEqual(verdict.by, "1.4.23")

    def test_and_the_reason_is_the_sutras_own_counter_example(self):
        """वृक्षस्य पर्णं पतति — a tree, a falling, and no causal relation."""
        self.assertIn("वृक्षस्य", karaka_of().why)

    def test_the_corpus_records_it_as_the_heading_of_the_block(self):
        """
        Two texts on the same claim: the sūtra says कारके and the corpus's
        per-sūtra adhikāra data puts 1.4.24 to 1.4.55 under it.
        """
        for number in range(24, 56):
            headings = [i.sutra for i in facts(f"1.4.{number}").adhikara]
            self.assertIn("1.4.23", headings, f"1.4.{number}")

    def test_and_that_it_stops_at_1_4_55(self):
        headings = [i.sutra for i in facts("1.4.56").adhikara]
        self.assertNotIn("1.4.23", headings)


class Options(unittest.TestCase):
    """The three sūtras that offer rather than assign."""

    def test_1_4_43_makes_the_stake_an_object_too(self):
        verdict = karaka_of(verb="div", given=["sādhakatama"])
        self.assertIs(verdict.karaka, KM)
        self.assertEqual(verdict.by, "1.4.43")
        self.assertIn("1.4.42", verdict.instead_of)

    def test_1_4_44_offers_sampradana_in_hiring(self):
        verdict = karaka_of(given=["parikrayaṇa", "sādhakatama"])
        self.assertIs(verdict.karaka, S)
        self.assertTrue(verdict.optional)

    def test_1_4_53_offers_the_object_with_hr_and_kr(self):
        for verb in ("hṛ", "kṛ"):
            verdict = karaka_of(causative=True, verb=verb,
                                given=["aṇau-kartā"])
            self.assertIs(verdict.karaka, KM, verb)
            self.assertEqual(verdict.by, "1.4.53", verb)
            self.assertTrue(verdict.optional, verb)


class Hygiene(unittest.TestCase):
    def test_every_asserted_fact_is_in_the_vocabulary(self):
        unknown = {f for p in PROVISIONS for f in p.requires if f not in FACTS}
        self.assertEqual(unknown, set())

    def test_and_every_verb_sense(self):
        unknown = {s for p in PROVISIONS for s in p.senses
                   if s not in VERB_SENSES}
        self.assertEqual(unknown, set())

    def test_a_rule_that_nearly_fired_is_reported(self):
        wanting = dict(near_misses(Participant(verb_sense=("ruc",))))
        self.assertIn("1.4.33", wanting)
        self.assertEqual(wanting["1.4.33"], ("prīyamāṇa not stated",))

    def test_every_verdict_names_a_codified_sutra(self):
        for _, form, asserted, _ in WORKED:
            by = karaka_of(**asserted).by
            self.assertTrue(REGISTRY.has(by), f"{form}: {by}")


class Registration(unittest.TestCase):
    def test_1_4_23_to_1_4_55_are_codified(self):
        missing = [f"1.4.{n}" for n in range(23, 56)
                   if not REGISTRY.has(f"1.4.{n}")]
        self.assertEqual(missing, [])

    def test_each_record_carries_the_conditions_it_tests(self):
        for number in range(24, 56):
            sutra = f"1.4.{number}"
            line = REGISTRY.get(sutra).codification
            for provision in provisions_for(sutra):
                self.assertIn(provision.describe(), line, sutra)

    def test_the_records_say_where_the_ordering_is_doing_the_work(self):
        for sutra in ("1.4.38", "1.4.49", "1.4.54"):
            notes = REGISTRY.get(sutra).notes
            self.assertIn("1.4.1", notes, sutra)


if __name__ == "__main__":
    unittest.main()
