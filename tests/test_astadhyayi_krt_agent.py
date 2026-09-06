# -*- coding: utf-8 -*-
"""
3.1.133 to 3.1.150 — the agent affixes, and the close of the pāda.

Expectations are the Kāśikā's worked forms and its *kim*
counter-examples. What is most worth holding here is that three
conditions are ASKED of rules already codified rather than restated —
इगुपध, the presence of a preverb, and 3.1.140's stretch of the
dhātupāṭha — because a restatement drifts silently and a call does not.
"""

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi.krt_agent import (
    AGENT, JNADI, JVALADI_FROM, JVALADI_THROUGH, LIMPADI, PADI, PRUSRLU,
    VYADHADI, _has_upasarga, _how_specific, _in_jvaladi, _is_igupadha,
    agent_affix, provisions_for,
)


class ThreeConditionsAreAskedNotRestated(unittest.TestCase):
    """
    The reason this matters is not tidiness. A restated condition is a
    second copy of a rule, and the two drift: correct one and the other
    stays wrong, with nothing to say which is which.
    """

    def test_igupadha_is_1_1_65_and_the_pratyahara_together(self):
        """
        1.1.65 अलोऽन्त्यात्पूर्व उपधा says WHICH sound is penultimate,
        and इक् says whether it falls in that span. The Kāśikā's four
        examples come out right, and पच् falls outside.
        """
        for root in ("kṣip", "likh", "budh", "kṛś"):
            with self.subTest(root=root):
                self.assertTrue(_is_igupadha(root))
        self.assertFalse(_is_igupadha("pac"))

    def test_and_that_is_why_three_roots_had_to_be_named(self):
        """
        ज्ञा's penult is ञ् — no इक् at all — so 3.1.135 names it
        separately. Asking 1.1.65 is what makes that visible; a
        hand-kept list would have hidden the reason.
        """
        for root in JNADI:
            with self.subTest(root=root):
                self.assertFalse(
                    _is_igupadha(root),
                    "a named root that WAS igupadha would make the "
                    "naming pointless")
                self.assertEqual(agent_affix(root=root).by, "3.1.135")

    def test_the_preverb_is_1_4_59s_question(self):
        """उपसर्गाः क्रियायोगे — asked, not matched against a list."""
        self.assertTrue(_has_upasarga("pra"))
        self.assertTrue(_has_upasarga("ud"))
        self.assertFalse(_has_upasarga("deva"))
        self.assertFalse(_has_upasarga(""))

    def test_3_1_140s_gana_is_a_stretch_of_the_dhatupatha(self):
        """
        ज्वल इत्येवमादिभ्यः कस इत्येवमन्तेभ्यः — the vṛtti gives the
        group by naming both ends, so it is a span and the corpus
        already records it. चल is the vṛtti's own example and falls
        between them.
        """
        self.assertLess(JVALADI_FROM, JVALADI_THROUGH)
        for root in ("jval", "cal", "kas"):
            with self.subTest(root=root):
                self.assertTrue(_in_jvaladi(root))
        self.assertFalse(_in_jvaladi("pac"))


class EachRuleAnswersForItsOwnExample(unittest.TestCase):

    def test_the_worked_forms_reach_their_rules(self):
        cases = (
            ("3.1.133", "ṇvul", dict(root="bhaj")),
            ("3.1.135", "ka", dict(root="kṣip")),
            ("3.1.136", "ka", dict(root="sthā", upasarga="pra")),
            ("3.1.137", "śa", dict(root="dṛś", upasarga="ud")),
            ("3.1.138", "śa", dict(root="limp")),
            ("3.1.139", "śa", dict(root="dā")),
            ("3.1.140", "ṇa", dict(root="jval")),
            ("3.1.141", "ṇa", dict(root="vyadh")),
            ("3.1.142", "ṇa", dict(root="du")),
            ("3.1.143", "ṇa", dict(root="grah")),
            ("3.1.144", "ka", dict(root="grah", sense="geha")),
            ("3.1.145", "ṣvun", dict(root="nṛt", craftsman=True)),
            ("3.1.146", "thakan", dict(root="gai", craftsman=True)),
            ("3.1.147", "ṇyuṭ", dict(root="gā", craftsman=True)),
            ("3.1.148", "ṇyuṭ", dict(root="hā", sense="vrīhi")),
            ("3.1.149", "vun", dict(root="pru", sense="samabhihāra")),
            ("3.1.150", "vun", dict(root="jīv", sense="āśis")),
        )
        for sutra, affix, where in cases:
            with self.subTest(sutra=sutra, **where):
                answer = agent_affix(**where)
                self.assertEqual(answer.by, sutra)
                self.assertEqual(answer.gives, affix)

    def test_every_named_root_of_a_list_rule_is_reached(self):
        for group, sutra, extra in ((PADI, "3.1.137", dict(upasarga="ud")),
                                    (LIMPADI, "3.1.138", {}),
                                    (VYADHADI, "3.1.141", {}),
                                    (PRUSRLU, "3.1.149",
                                     dict(sense="samabhihāra"))):
            for root in group:
                with self.subTest(sutra=sutra, root=root):
                    self.assertEqual(
                        agent_affix(root=root, **extra).by, sutra)

    def test_3_1_133_reaches_a_root_no_other_rule_does(self):
        """सर्वधातुभ्यः — and every rule after it is an अपवाद."""
        self.assertEqual(agent_affix(root="bhaj").by, "3.1.133")
        self.assertEqual(_how_specific(provisions_for("3.1.133")[0]), 0)


class TheApavadaChainIsStated(unittest.TestCase):
    """
    3.1.136 and 3.1.139 are णस्यापवादः, 3.1.140 and 3.1.143 are
    अचोऽपवादः, and 3.1.141's श्यै is written बाधकबाधनार्थम् to defeat
    3.1.136 in turn. A first draft as an if-chain in reverse order lost
    four of these, because ज्ञा, स्था, पा and दा all end in आ and
    3.1.141's clause swallowed them.
    """

    def test_the_four_the_if_chain_lost(self):
        for sutra, where in (("3.1.135", dict(root="jñā")),
                             ("3.1.136", dict(root="sthā",
                                              upasarga="pra")),
                             ("3.1.137", dict(root="pā", upasarga="ud")),
                             ("3.1.139", dict(root="dā"))):
            with self.subTest(sutra=sutra):
                self.assertTrue(
                    _ends_in_a_for_test(where["root"]),
                    "these are exactly the roots 3.1.141 also reaches")
                self.assertEqual(agent_affix(**where).by, sutra)

    def test_and_3_1_141_still_answers_where_nothing_cuts_into_it(self):
        """
        धा was a bad witness for this — it is one of 3.1.139's own two
        roots. पा is the right one: 3.1.137 names it but wants a
        preverb, so with none attached nothing cuts in and the general
        आ-final clause answers.
        """
        self.assertEqual(agent_affix(root="pā").by, "3.1.141")
        self.assertEqual(agent_affix(root="glā").by, "3.1.141")

    def test_syai_is_named_to_defeat_3_1_136(self):
        """
        आकारान्तत्वादेव श्यायतेः प्रत्यये सिद्धे पुनर्वचनं
        बाधकबाधनार्थम् — श्यै is आ-final and 3.1.141 reaches it anyway,
        so the naming exists to beat the क that 3.1.136 would give with
        a preverb. Without the weight, अवश्यायः would be lost.
        """
        syai = next(r for r in AGENT
                    if r.sutra == "3.1.141" and "śyai" in r.of)
        ka = next(r for r in AGENT if r.sutra == "3.1.136")
        self.assertGreater(_how_specific(syai), _how_specific(ka))
        self.assertEqual(
            agent_affix(root="śyai", upasarga="ava").by, "3.1.141")


class TheConditionsAreLive(unittest.TestCase):

    def test_the_rules_that_want_a_preverb_need_one(self):
        for root, sutra in (("sthā", "3.1.136"), ("dṛś", "3.1.137")):
            with self.subTest(root=root):
                self.assertEqual(
                    agent_affix(root=root, upasarga="pra").by, sutra)
                self.assertNotEqual(agent_affix(root=root).by, sutra)

    def test_the_rules_that_refuse_one_are_refused_by_it(self):
        """अनुपसर्गादिति किम्? प्रलिपः, प्रज्वलः, प्रदवः."""
        for root, sutra in (("limp", "3.1.138"), ("jval", "3.1.140"),
                            ("du", "3.1.142")):
            with self.subTest(root=root):
                self.assertEqual(agent_affix(root=root).by, sutra)
                self.assertNotEqual(
                    agent_affix(root=root, upasarga="pra").by, sutra)

    def test_the_three_sense_rules_need_their_sense(self):
        for root, sense, sutra in (("grah", "geha", "3.1.144"),
                                   ("hā", "vrīhi", "3.1.148"),
                                   ("pru", "samabhihāra", "3.1.149"),
                                   ("jīv", "āśis", "3.1.150")):
            with self.subTest(sutra=sutra):
                self.assertEqual(
                    agent_affix(root=root, sense=sense).by, sutra)
                self.assertNotEqual(agent_affix(root=root).by, sutra)

    def test_samabhihara_is_not_what_it_was_at_3_1_22(self):
        """
        There: पौनःपुन्यं भृशार्थो वा, again and again. Here:
        साधुकारित्वं लक्ष्यते, doing a thing well — सकृदपि यः सुष्ठु
        करोति तत्र भवति. One word, two senses, and the two rules must
        not share a field, so 3.1.22 keeps its own.
        """
        from src.astadhyayi.playground import spec_for

        here = {f.name for f in spec_for("3.1.149").fields}
        there = {f.name for f in spec_for("3.1.22").fields}
        self.assertIn("sense", here)
        self.assertIn("kriyasamabhihara", there)
        self.assertNotIn("kriyasamabhihara", here,
                         "the two senses must not share one field")


class TheCraftsmanRules(unittest.TestCase):

    def test_a_craftsman_is_needed_and_gai_takes_two_affixes(self):
        self.assertEqual(
            agent_affix(root="nṛt", craftsman=True).by, "3.1.145")
        self.assertNotEqual(agent_affix(root="nṛt").by, "3.1.145")
        # चकारेण ग इत्यनुकृष्यते — one root, two rules, both forms.
        self.assertEqual(
            agent_affix(root="gai", craftsman=True).gives, "thakan")
        self.assertEqual(
            agent_affix(root="gā", craftsman=True).gives, "ṇyuṭ")

    def test_3_1_146_says_the_other_affix_stands_too(self):
        self.assertIn("ण्युट्",
                      agent_affix(root="gai", craftsman=True).also)


class ThePadaIsComplete(unittest.TestCase):

    def test_3_1_runs_unbroken_from_one_to_one_hundred_and_fifty(self):
        from src.astadhyayi.sutra import REGISTRY

        numbers = sorted(
            int(str(s.id).rsplit(".", 1)[1]) for s in REGISTRY.all()
            if str(s.id).startswith("3.1."))
        self.assertEqual(numbers, list(range(1, 151)))

    def test_nothing_in_this_pada_is_still_reached_ahead(self):
        """
        3.1.22, 3.1.32, 3.1.68, 3.1.94 and 3.1.134 were all codified
        before their neighbours, for derivations that needed them. The
        reading has overtaken every one.
        """
        from tests.test_astadhyayi_asiddha import Registration

        still = [s for s in Registration.IDS if s.startswith("3.1.")]
        self.assertEqual(still, [])


def _ends_in_a_for_test(root: str) -> bool:
    from src.astadhyayi.krt_agent import _ends_in_a

    return _ends_in_a(root)


if __name__ == "__main__":
    unittest.main()
