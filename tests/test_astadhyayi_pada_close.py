# -*- coding: utf-8 -*-
"""
3.2.178 to 3.2.188 — the close of अध्याय ३ पाद २.

With these eleven the pāda is complete: 188 sūtras, contiguous.

What this block asserts that no earlier one could:

  * one word doing two different jobs a hundred sūtras apart —
    दृश्यते at 3.2.75 and at 3.2.178;
  * two rules dividing a single WORD between them by whether it is
    being used as a name;
  * a rule excepting another from the same pāda, and naming it;
  * a condition about what a thing is PART OF.
"""

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi.tacchila import tacchila_affix
from src.astadhyayi.upapada_krt import (
    Added, NotAdded, kta_in_present, nistha,
)


class EachRuleAnswersForItsOwnExample(unittest.TestCase):

    CASES = (
        ("3.2.178", "kvip", dict(root="yuj", attested=True,
                                 wants="kvip")),
        ("3.2.179", "kvip", dict(root="bhū", samjna=True)),
        ("3.2.180", "ḍu", dict(root="bhū", upasarga="pra")),
        ("3.2.181", "ṣṭran", dict(root="dhe", karaka="karman")),
        ("3.2.182", "ṣṭran", dict(root="nī", karaka="karaṇa")),
        ("3.2.183", "ṣṭran", dict(root="pū", karaka="karaṇa",
                                  part_of="hala")),
        ("3.2.184", "itra", dict(root="ṛ", karaka="karaṇa")),
        ("3.2.185", "itra", dict(root="pū", karaka="karaṇa",
                                 samjna=True)),
        ("3.2.186", "itra", dict(root="pū", karaka="karaṇa",
                                 rsi_devata="ṛṣi")),
    )

    def test_every_affix_rule_answers_for_itself(self):
        for sutra, gives, where in self.CASES:
            with self.subTest(sutra=sutra, **where):
                answer = tacchila_affix(**where)
                self.assertIsInstance(answer, Added)
                self.assertEqual(answer.by, sutra)
                self.assertEqual(answer.gives, gives)


class ThePadaIsComplete(unittest.TestCase):
    """
    188 sūtras, contiguous, each answered by exactly one entry point.
    No endpoint is named in the contiguity check — a range is a census,
    as four earlier failures taught.
    """

    def test_it_runs_unbroken_from_its_first_sutra(self):
        from src.astadhyayi.sutra import REGISTRY

        numbers = sorted(
            int(str(s.id).rsplit(".", 1)[1]) for s in REGISTRY.all()
            if str(s.id).startswith("3.2."))
        self.assertTrue(numbers)
        self.assertEqual(numbers, list(range(1, len(numbers) + 1)))

    def test_and_the_pada_has_no_sutra_after_its_last(self):
        """
        The corpus is what says where the pāda ends, not a number
        chosen here: 3.2.189 has no text.
        """
        import io
        import json

        d = json.load(io.open("reference/commentary/kashika.json",
                              encoding="utf-8"))
        self.assertTrue(d.get("32188"))
        self.assertFalse(d.get("32189"))

    def test_every_rule_is_answered_by_exactly_one_entry_point(self):
        from src.astadhyayi.sutra import REGISTRY

        registered = {str(x.id) for x in REGISTRY.all()
                      if str(x.id).startswith("3.2.")}
        by_apply = {}
        for x in REGISTRY.all():
            if str(x.id).startswith("3.2."):
                by_apply.setdefault(x.apply.__name__, set()).add(
                    str(x.id))
        seen = set()
        for ids in by_apply.values():
            self.assertEqual(seen & ids, set())
            seen |= ids
        self.assertEqual(seen, registered)


class OneWordDoingTwoJobs(unittest.TestCase):
    """
    दृश्यते at 3.2.75 was read प्रयोगानुसरणार्थम् — so the rule
    follows usage. At 3.2.178 it is विध्यन्तरोपसंग्रहार्थम् — to
    gather in operations other than the affix. Same word, hundred
    sūtras apart, and only the commentary tells them apart.
    """

    def test_both_readings_are_recorded_where_they_belong(self):
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("प्रयोगानुसरणार्थम्",
                      REGISTRY.get("3.2.75").notes)
        self.assertIn("विध्यन्तरोपसंग्रहार्थम्",
                      REGISTRY.get("3.2.178").notes)

    def test_and_3_2_178_names_the_other_reading_to_contrast_it(self):
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("3.2.75", REGISTRY.get("3.2.178").notes)

    def test_all_four_open_rules_of_the_pada_want_attestation(self):
        """3.2.75, 3.2.76, 3.2.101 and now 3.2.178."""
        from src.astadhyayi.tacchila import TACCHILA
        from src.astadhyayi.upapada_krt import UPAPADA

        rows = {r.sutra: r for r in tuple(UPAPADA) + tuple(TACCHILA)}
        for sutra in ("3.2.75", "3.2.76", "3.2.101", "3.2.178"):
            with self.subTest(sutra=sutra):
                self.assertTrue(rows[sutra].attested)


class TwoRulesDividingOneWord(unittest.TestCase):
    """
    विभुः and विभूः are one word used two ways, and 3.2.179 and
    3.2.180 divide it by whether it is being used as a NAME. The
    counter-example of the second IS the example of the first.
    """

    def test_the_same_root_and_preverb_give_two_affixes(self):
        as_name = tacchila_affix(root="bhū", samjna=True)
        not_a_name = tacchila_affix(root="bhū", upasarga="pra")
        self.assertEqual((as_name.by, as_name.gives),
                         ("3.2.179", "kvip"))
        self.assertEqual((not_a_name.by, not_a_name.gives),
                         ("3.2.180", "ḍu"))

    def test_and_samjna_is_tri_state_because_they_disagree(self):
        from src.astadhyayi.tacchila import provisions_for

        self.assertIs(provisions_for("3.2.179")[0].samjna, True)
        self.assertIs(provisions_for("3.2.180")[0].samjna, False)

    def test_the_counter_of_one_is_the_example_of_the_other(self):
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("विभूर्नाम", REGISTRY.get("3.2.179").notes)
        self.assertIn("विभूर्नाम", REGISTRY.get("3.2.180").notes)


class ARuleExceptingAnotherOfItsOwnPada(unittest.TestCase):
    """
    3.2.102 gave निष्ठा for the past. 3.2.187 and 3.2.188 give क्त in
    the PRESENT, and 3.2.187's vṛtti names that rule as the reason
    they are needed — eighty-five sūtras apart.
    """

    def test_the_present_rules_answer_and_the_past_one_still_does(self):
        self.assertEqual(kta_in_present(nit=True).by, "3.2.187")
        self.assertEqual(kta_in_present(sense="mati").by, "3.2.188")
        self.assertEqual(nistha("kta").by, "3.2.102")

    def test_they_answer_from_beside_the_rule_they_except(self):
        """
        Not from the affix table: the question is when क्त comes,
        which is what 3.2.102 answers differently.
        """
        from src.astadhyayi.sutra import REGISTRY

        for sutra in ("3.2.187", "3.2.188"):
            with self.subTest(sutra=sutra):
                self.assertEqual(
                    REGISTRY.get(sutra).apply.__name__,
                    "kta_in_present")

    def test_and_each_rule_names_the_other(self):
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("3.2.102", REGISTRY.get("3.2.187").notes)
        self.assertIn("3.2.187", REGISTRY.get("3.2.102").notes)

    def test_neither_condition_reaches_without_being_asserted(self):
        answer = kta_in_present()
        self.assertIsInstance(answer, NotAdded)
        self.assertEqual(answer.by, "")


class AConditionAboutWhatAThingBelongsTo(unittest.TestCase):
    """
    3.2.183's हलसूकरयोः — the instrument must be part of a plough or
    of a boar. Not what it does, not what it is called, but what it
    belongs to. No rule of the pāda had asked that before.
    """

    def test_both_wholes_are_reached_and_others_are_not(self):
        for whole in ("hala", "sūkara"):
            with self.subTest(whole=whole):
                self.assertEqual(
                    tacchila_affix(root="pū", karaka="karaṇa",
                                   part_of=whole).by, "3.2.183")
        self.assertNotEqual(
            tacchila_affix(root="pū", karaka="karaṇa",
                           part_of="ratha").by, "3.2.183")

    def test_it_is_the_only_rule_of_the_pada_with_such_a_condition(self):
        from src.astadhyayi.tacchila import TACCHILA

        having = [r.sutra for r in TACCHILA if r.part_of]
        self.assertEqual(having, ["3.2.183"])


class AKarakaPairedCrosswiseWithAKindOfBeing(unittest.TestCase):
    """
    3.2.186 ऋषौ करणे, देवतायां कर्तरि. यथासंख्यम् has bound two lists
    of words before in this pāda; here it binds a kāraka to a kind of
    being, so one form is read two ways by what it is said of.
    """

    def test_the_seer_gets_the_means(self):
        self.assertEqual(
            tacchila_affix(root="pū", karaka="karaṇa",
                           rsi_devata="ṛṣi").by, "3.2.186")

    def test_and_the_condition_is_needed(self):
        self.assertNotEqual(
            tacchila_affix(root="pū", karaka="karaṇa",
                           rsi_devata="devatā").by, "3.2.186")

    def test_the_crosswise_reading_is_recorded(self):
        from src.astadhyayi.sutra import REGISTRY

        notes = REGISTRY.get("3.2.186").notes
        self.assertIn("ऋषौ करणे", notes)
        self.assertIn("देवतायां कर्तरि", notes)


class WhatTheWholePadaLeavesOpen(unittest.TestCase):
    """
    Two debts remain, both asserted so that paying them is noticed.
    """

    def test_3_3_113_is_codified_and_the_rules_leaning_on_it_hold(self):
        """
        PAID. Two rules of this pāda sent a form to 3.3.113, and it was
        asserted uncodified so that codifying it would go red. It did.

        What holds now is stronger than the note: the rule those two
        leaned on really does license affixes beyond where they were
        prescribed, and says so in the vṛtti's own words.
        """
        from src.astadhyayi.bhava_krt import krtya_lyut_bahulam
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("3.3.113", {str(s.id) for s in REGISTRY.all()})
        for sutra in ("3.2.53", "3.2.153"):
            with self.subTest(sutra=sutra):
                self.assertIn("3.3.113", REGISTRY.get(sutra).notes)
        self.assertIn("न्यत्रापि भवन्ति", krtya_lyut_bahulam().why)

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
if __name__ == "__main__":
    unittest.main()
