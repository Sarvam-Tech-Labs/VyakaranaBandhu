# -*- coding: utf-8 -*-
"""
Operations named from a closed vocabulary — src/astadhyayi/operations.py.

Several sūtras do not perform an operation but name one and say something of
it: 1.1.58 lists ten that 1.1.57 shall not reach, 2.1.2 confines itself to
accent, 8.2.2 names four in which a lost न् still counts. Each matched a bare
string, and nothing checked it — so `dirgha` for `dīrgha` did not fail. It
took the other branch and named a different sūtra as its authority.

That is the shape of defect this codification keeps meeting: not a crash, but
a confident wrong answer. These tests are about the refusal, not the lookup.
"""

from __future__ import annotations

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi.operations import (
    OPERATIONS, UnknownOperation, among, check_group, is_operation, names,
    resolve,
)
from src.astadhyayi.playground import run, spec_for
from src.astadhyayi.sources import all_sutra_ids, facts
from src.astadhyayi.sthanivat import EXCLUDED, sthanivat
from src.astadhyayi.svara import NOT_PARANGAVAT, parangavat


class AMisspellingIsRefused(unittest.TestCase):
    THREE = dict(al_vidhi=True, sthanin_is_vowel=True,
                 caused_by_following=True, purva_vidhi=True)

    def test_the_case_that_prompted_this(self):
        """
        Both spellings used to be answered. One of the answers was wrong,
        and nothing in the output said which.
        """
        right = sthanivat(operation="dīrgha", **self.THREE)
        self.assertFalse(right.applies)
        self.assertEqual(right.by, "1.1.58")

        with self.assertRaises(UnknownOperation):
            sthanivat(operation="dirgha", **self.THREE)

    def test_an_empty_operation_still_means_unstated(self):
        """
        Refusing a typo must not turn 'nothing stated' into an error — a
        reader who has not said which operation is asking a real question,
        and 1.1.57 answers it.
        """
        self.assertIsNone(resolve(""))
        self.assertIsNone(resolve(None))
        self.assertTrue(sthanivat(operation="", **self.THREE).applies)

    def test_the_message_says_what_the_names_are(self):
        with self.assertRaises(UnknownOperation) as caught:
            resolve("dirgha")
        message = str(caught.exception)
        self.assertIn("dirgha", message)
        self.assertIn("dīrgha", message)

    def test_2_1_2_refuses_one_too(self):
        with self.assertRaises(UnknownOperation):
            parangavat(operation="satva")          # no retroflex
        blocked = parangavat(operation="ṣatva")
        self.assertFalse(blocked.holds)


class TheVocabularyIsConsistentWithTheRulesThatUseIt(unittest.TestCase):

    def test_1_1_58s_ten_are_all_real_operations(self):
        """
        Checked at import as well. A rule holding a list of operations that
        do not exist would exclude nothing, silently.
        """
        self.assertEqual(len(EXCLUDED), 10)
        for name in EXCLUDED:
            with self.subTest(operation=name):
                self.assertTrue(is_operation(name))
        check_group(EXCLUDED, "1.1.58")

    def test_2_1_2s_two_are_too(self):
        for name, _ in NOT_PARANGAVAT:
            with self.subTest(operation=name):
                self.assertTrue(is_operation(name))

    def test_a_bad_group_is_caught_when_it_is_declared(self):
        with self.assertRaises(UnknownOperation):
            check_group(("dīrgha", "not-an-operation"), "a test")

    def test_every_cited_sutra_exists(self):
        """
        Each operation may name the sūtra that prescribes it. Those numbers
        were read from the corpus rather than recalled, and this is what
        keeps them that way.
        """
        known = set(all_sutra_ids())
        for operation in OPERATIONS.values():
            if not operation.prescribed_by:
                continue
            with self.subTest(operation=operation.name):
                self.assertIn(operation.prescribed_by, known)
                # and it is a real sūtra, not merely a well-formed number
                self.assertTrue(facts(operation.prescribed_by).devanagari)

    def test_every_operation_carries_both_scripts_and_a_gist(self):
        for operation in OPERATIONS.values():
            with self.subTest(operation=operation.name):
                self.assertTrue(operation.devanagari.strip())
                self.assertRegex(operation.devanagari, r"[\u0900-\u097F]")
                self.assertGreater(len(operation.gist), 12)

    def test_among_answers_without_dereferencing_nothing(self):
        self.assertTrue(among("dīrgha", EXCLUDED))
        self.assertFalse(among("guṇa", EXCLUDED))
        self.assertFalse(among(None, EXCLUDED))
        self.assertFalse(among("", EXCLUDED))
        self.assertFalse(among("dīrgha", ("", None)))


class TheFormCannotProduceABadName(unittest.TestCase):
    """
    The refusal is the safety net; the list is what makes it unnecessary.
    A free text box invites the very typo the vocabulary exists to catch.
    """

    def test_operation_is_offered_as_a_list(self):
        field = next(f for f in spec_for("1.1.56").fields
                     if f.name == "operation")
        self.assertEqual(field.kind, "select")
        self.assertIn("dīrgha", field.options)
        self.assertNotIn("dirgha", field.options)

    def test_the_blank_option_is_there_because_unstated_is_an_answer(self):
        field = next(f for f in spec_for("1.1.56").fields
                     if f.name == "operation")
        self.assertIn("", field.options)

    def test_every_rule_taking_an_operation_offers_the_same_list(self):
        from src.astadhyayi.sutra import REGISTRY

        seen = 0
        for sutra in REGISTRY.all():
            for field in spec_for(str(sutra.id)).fields:
                if field.name != "operation":
                    continue
                seen += 1
                with self.subTest(sutra=str(sutra.id)):
                    self.assertEqual(field.kind, "select")
                    self.assertEqual(
                        set(field.options), {""} | set(names()))
        self.assertGreaterEqual(seen, 10)

    def test_a_bad_name_through_the_playground_is_reported_not_answered(self):
        outcome = run("1.1.56", {"al_vidhi": True, "operation": "dirgha",
                                 "sthanin_is_vowel": True,
                                 "caused_by_following": True,
                                 "purva_vidhi": True})
        self.assertFalse(outcome["ok"])
        self.assertIn("dirgha", outcome["error"])


if __name__ == "__main__":
    unittest.main()
