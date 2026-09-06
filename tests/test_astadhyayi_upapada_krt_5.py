# -*- coding: utf-8 -*-
"""
3.2.61 to 3.2.75 — the क्विप् run, and the affixes that close the pāda.

What this block asserts that no earlier one could:

  * a condition that is PROSODIC and not grammatical — 3.2.66's
    अनन्तः पादम्, the first anywhere in the project;
  * a rule whose whole work is to RESTRICT another (3.2.73's नियम),
    so that its condition is not a qualification but the rule itself;
  * a rule deliberately open at every joint, held back only by usage —
    3.2.75's दृश्यन्ते;
  * a tie broken by NARROWNESS, since 3.2.70 names one root and
    3.2.61 names twelve with that one among them.
"""

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi.upapada_krt import (
    ATO_AFFIXES, JANADI, SADADI, UPAPADA,
    Added, NotAdded, _how_specific, _ranking, provisions_for,
    upapada_affix,
)


class EachRuleAnswersForItsOwnExample(unittest.TestCase):

    CASES = (
        ("3.2.61", "kvip", dict(root="dviṣ", beside="mitra",
                                role="sup")),
        ("3.2.62", "ṇvi", dict(root="bhaj", beside="ardha",
                               role="sup")),
        ("3.2.63", "ṇvi", dict(root="sah", beside="turā", role="sup",
                               chandasi=True)),
        ("3.2.64", "ṇvi", dict(root="vah", beside="praṣṭha",
                               role="sup", chandasi=True)),
        ("3.2.65", "ñyuṭ", dict(root="vah", beside="kavya",
                                chandasi=True)),
        ("3.2.66", "ñyuṭ", dict(root="vah", beside="havya",
                                chandasi=True)),
        ("3.2.67", "viṭ", dict(root="jan", beside="go", role="sup",
                               chandasi=True)),
        ("3.2.68", "viṭ", dict(root="ad", beside="āma", role="sup")),
        ("3.2.69", "viṭ", dict(root="ad", beside="kravya",
                               role="sup")),
        ("3.2.70", "kap", dict(root="duh", beside="kāma", role="sup")),
        ("3.2.71", "ṇvin", dict(root="vah", beside="śveta",
                                role="karman", mantra=True)),
        ("3.2.72", "ṇvin", dict(root="yaj", upasarga="ava",
                                mantra=True)),
        ("3.2.73", "vic", dict(root="yaj", upasarga="upa",
                               chandasi=True)),
        ("3.2.74", "manin", dict(root="dā", beside="su", role="sup",
                                 chandasi=True)),
        ("3.2.75", "manin", dict(root="śṛ", beside="su",
                                 attested=True)),
    )

    def test_every_rule_of_the_run_answers_for_itself(self):
        for sutra, affix, where in self.CASES:
            with self.subTest(sutra=sutra, **where):
                answer = upapada_affix(**where)
                self.assertIsInstance(answer, Added)
                self.assertEqual(answer.by, sutra)
                self.assertEqual(answer.gives, affix)

    def test_all_twelve_of_3_2_61s_roots_are_reached(self):
        for root in SADADI:
            with self.subTest(root=root):
                # दुह् is the exception: 3.2.70 names it alone and wins.
                expected = "3.2.70" if root == "duh" else "3.2.61"
                self.assertEqual(
                    upapada_affix(root=root, beside="mitra",
                                  role="sup").by, expected)

    def test_all_five_of_3_2_67s_roots_are_reached(self):
        for root in JANADI:
            with self.subTest(root=root):
                self.assertEqual(
                    upapada_affix(root=root, beside="go", role="sup",
                                  chandasi=True).by, "3.2.67")

    def test_the_two_closing_rules_give_four_affixes_each(self):
        """चकाराद् विज् भवति — the fourth comes out of the च."""
        self.assertEqual(len(ATO_AFFIXES), 4)
        for where in (dict(root="dā", beside="su", role="sup",
                           chandasi=True),
                      dict(root="śṛ", beside="su", attested=True)):
            with self.subTest(**where):
                answer = upapada_affix(**where)
                self.assertEqual(answer.gives, "manin")
                for affix in ("क्वनिप्", "वनिप्", "विच्"):
                    self.assertIn(affix, answer.also)


class ATieBrokenByNarrowness(unittest.TestCase):
    """
    3.2.70 दुहः कब् names ONE root; 3.2.61 names twelve with दुह् among
    them. Both reach कामदुघा, and by stated conditions they tie exactly
    — so the twelve won on table order and the cow got गोधुक्'s affix.
    """

    def test_the_two_rules_state_the_same_amount(self):
        wide = provisions_for("3.2.61")[0]
        narrow = provisions_for("3.2.70")[0]
        self.assertEqual(_how_specific(wide), _how_specific(narrow))
        self.assertIn("duh", wide.of)
        self.assertEqual(narrow.of, ("duh",))

    def test_and_the_narrower_one_wins(self):
        self.assertGreater(_ranking(provisions_for("3.2.70")[0]),
                           _ranking(provisions_for("3.2.61")[0]))
        answer = upapada_affix(root="duh", beside="kāma", role="sup")
        self.assertEqual((answer.by, answer.gives), ("3.2.70", "kap"))

    def test_how_specific_still_answers_its_own_question(self):
        """
        Narrowness went into the RANKING and not into `_how_specific`,
        which answers how much a rule says — a fact about one rule,
        where the ranking is a fact about a pair. 3.2.1 still says the
        least of anything in the table.
        """
        self.assertEqual(_how_specific(provisions_for("3.2.1")[0]), 1)


class AConditionAboutVerseAndNotGrammar(unittest.TestCase):
    """
    3.2.66's अनन्तः पादम् — the root must not stand at the end of a
    metrical quarter. The first condition in this project that is
    about prosody at all.
    """

    def test_within_the_line_it_answers_and_at_the_end_it_does_not(self):
        self.assertEqual(
            upapada_affix(root="vah", beside="havya",
                          chandasi=True).by, "3.2.66")
        self.assertNotEqual(
            upapada_affix(root="vah", beside="havya", chandasi=True,
                          pada_final=True).by, "3.2.66")

    def test_it_is_the_only_rule_of_the_pada_with_such_a_condition(self):
        prosodic = [r.sutra for r in UPAPADA if r.refuses_pada_final]
        self.assertEqual(prosodic, ["3.2.66"])


class ARuleWhoseWorkIsToRestrictAnother(unittest.TestCase):
    """
    3.2.73. The vṛtti asks why it exists at all — यजेरपि विच् सिद्ध एव,
    3.2.75 gives यज् its विच् already — and answers
    यजेर्नियमार्थमेतत्: it is a नियम. उपयजेश्छन्दस्येव, न भाषायाम्.
    """

    def test_it_holds_in_the_veda_and_not_outside(self):
        self.assertEqual(
            upapada_affix(root="yaj", upasarga="upa",
                          chandasi=True).by, "3.2.73")
        self.assertNotEqual(
            upapada_affix(root="yaj", upasarga="upa").by, "3.2.73")

    def test_the_rule_it_narrows_would_otherwise_reach_the_root(self):
        """
        3.2.75 does give यज् these affixes where usage shows them, so
        the नियम has something to narrow. That is what makes 3.2.73 a
        restriction rather than a provision.
        """
        self.assertEqual(
            upapada_affix(root="yaj", beside="su", attested=True).by,
            "3.2.75")

    def test_and_the_notes_record_the_argument(self):
        from src.astadhyayi.sutra import REGISTRY

        notes = REGISTRY.get("3.2.73").notes
        self.assertIn("नियम", notes)
        self.assertIn("3.2.75", notes)


class ARuleOpenAtEveryJointAndHeldBackByUsage(unittest.TestCase):
    """
    3.2.75 अन्येभ्योऽपि दृश्यन्ते. अपिशब्दः सर्वोपाधिव्यभिचारार्थः, and
    निरुपपदादपि भवति — no condition need hold and no companion need
    stand. Read as a provision it would hand four affixes to every
    root there is. दृशिग्रहणं प्रयोगानुसरणार्थम् is what stops that.
    """

    def test_it_answers_where_usage_is_asserted(self):
        answer = upapada_affix(root="śṛ", beside="su", attested=True)
        self.assertEqual(answer.by, "3.2.75")

    def test_it_works_with_no_companion_at_all(self):
        """निरुपपदादपि भवति — धीवा, पीवा."""
        self.assertEqual(
            upapada_affix(root="dhī", attested=True).by, "3.2.75")

    def test_but_it_does_not_swallow_the_pada(self):
        """
        Without the attestation condition this rule would outrank
        nothing and reach everything, so कुम्भकारः would gain three
        affixes it does not have. The condition IS the codification of
        दृश्यन्ते.
        """
        self.assertEqual(
            upapada_affix(root="kṛ", beside="kumbha",
                          role="karman").by, "3.2.1")
        self.assertNotEqual(
            upapada_affix(root="kṛ", beside="kumbha",
                          role="karman").gives, "manin")

    def test_it_is_the_complement_of_3_2_74_and_not_silence(self):
        """
        अनाकारान्तेभ्यः — after roots that do NOT end in आ. So an
        ā-final root outside the Veda reaches neither: 3.2.74 wants
        the Veda, 3.2.75 wants a non-ā-final root.
        """
        self.assertTrue(provisions_for("3.2.75")[0].not_a_final)
        self.assertNotEqual(
            upapada_affix(root="dā", beside="su", attested=True).by,
            "3.2.75")


class TheThingsRecordedRatherThanRun(unittest.TestCase):
    """
    Several arguments in this run bear on rules elsewhere or on the
    text's own composition. None is a call, and the notes are where
    they belong.
    """

    def test_3_2_61s_jnapaka_is_recorded(self):
        """
        उपसर्गग्रहणं ज्ञापनार्थम् — mentioning the preverb here tells
        us that elsewhere, where सुप् is mentioned and the preverb is
        not, no preverb is meant. A rule saying something by the fact
        of its own wording.
        """
        from src.astadhyayi.sutra import REGISTRY

        notes = REGISTRY.get("3.2.61").notes
        self.assertIn("ज्ञापक", notes)
        self.assertIn("3.1.106", notes)

    def test_3_2_71_is_part_fixing_and_part_rule(self):
        """
        धातूपपदसमुदाया निपात्यन्ते अलाक्षणिककार्यसिद्ध्यर्थम्,
        प्रत्ययस्तु विधीयत एव — the compounds are fixed for their
        irregular pieces, the affix is genuinely prescribed. So it is
        in the table, and what is fixed is in the notes.
        """
        from src.astadhyayi.sutra import REGISTRY

        rows = provisions_for("3.2.71")
        self.assertEqual(len(rows), 3)
        self.assertTrue(all(r.gives == "ṇvin" for r in rows))
        self.assertIn("प्रत्ययस्तु विधीयत एव",
                      REGISTRY.get("3.2.71").notes)

    def test_this_block_declares_no_reuse(self):
        from src.astadhyayi.sutra import REGISTRY

        for n in range(61, 76):
            with self.subTest(sutra="3.2.%d" % n):
                self.assertEqual(REGISTRY.get("3.2.%d" % n).reuses, ())


class TheAnuvrttiThatEnd(unittest.TestCase):
    """
    Three times in this pāda a condition stops running and only the
    commentary says so. The codification cannot represent anuvṛtti at
    all — every row states its own conditions — so a condition that
    ends is simply one not written, and the notes are the only record
    that a choice was made.
    """

    def test_all_three_are_recorded(self):
        from src.astadhyayi.sutra import REGISTRY

        for sutra, phrase in (("3.2.48", "नानुवर्तते"),
                              ("3.2.61", "न\n  व्याप्रियते"),
                              ("3.2.68", "निवृत्तम्")):
            with self.subTest(sutra=sutra):
                self.assertIn(phrase.replace("\n  ", " "),
                              REGISTRY.get(sutra).notes.replace(
                                  "\n  ", " "))

    def test_and_3_2_68_really_does_reach_outside_the_veda(self):
        """छन्दसीति निवृत्तम् — so the rule answers with no Veda said."""
        self.assertEqual(
            upapada_affix(root="ad", beside="āma", role="sup").by,
            "3.2.68")


if __name__ == "__main__":
    unittest.main()
