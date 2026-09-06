# -*- coding: utf-8 -*-
"""
3.2.76 to 3.2.93 — the widest rule of the pāda, and what restricts it.

What this block asserts that no earlier one could:

  * an अधिकार that adds nothing and puts every rule after it under a
    condition none of them states — 3.2.84 भूते;
  * four rules in a row that PROVIDE nothing, because 3.2.76 has
    already given क्विप् to every root — and the vṛtti counts how many
    ways each restricts, which is how 3.2.89 is seen to differ;
  * a condition on the WHOLE and not on any part of it, twice;
  * a root pinned by what a LATER rule would do with it.
"""

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi.upapada_krt import (
    BHUTE_FROM, BHUTE_THROUGH, BRAHMADI, SUKARMADI, UPAPADA,
    Added, NotAdded, bhute_heading, provisions_for, upapada_affix,
)


class EachRuleAnswersForItsOwnExample(unittest.TestCase):

    CASES = (
        ("3.2.76", "kvip", dict(root="sraṃs", beside="ukhā",
                                attested=True, wants="kvip")),
        ("3.2.77", "ka", dict(root="sthā", beside="śam", role="sup")),
        ("3.2.78", "ṇini", dict(root="bhuj", beside="uṣṇa",
                                role="sup", sense="tācchīlya")),
        ("3.2.79", "ṇini", dict(root="kruś", beside="uṣṭra",
                                role="sup", upamana="kartṛ")),
        ("3.2.80", "ṇini", dict(root="śī", beside="sthaṇḍila",
                                role="sup", sense="vrata")),
        ("3.2.81", "ṇini", dict(root="pā", beside="kṣīra", role="sup",
                                sense="ābhīkṣṇya")),
        ("3.2.82", "ṇini", dict(root="man", beside="darśanīya",
                                role="sup")),
        ("3.2.83", "khaś", dict(root="man", beside="paṇḍita",
                                role="sup", sense="ātmamāna")),
        ("3.2.85", "ṇini", dict(root="yaj", beside="agniṣṭoma",
                                role="karaṇa", past=True)),
        ("3.2.86", "ṇini", dict(root="han", beside="pitṛvya",
                                role="karman", past=True,
                                sense="kutsā")),
        ("3.2.87", "kvip", dict(root="han", beside="brahman",
                                role="karman", past=True)),
        ("3.2.88", "kvip", dict(root="han", beside="mātṛ",
                                role="karman", past=True,
                                chandasi=True)),
        ("3.2.89", "kvip", dict(root="kṛ", beside="puṇya",
                                role="karman", past=True)),
        ("3.2.90", "kvip", dict(root="su", beside="soma",
                                role="karman", past=True)),
        ("3.2.91", "kvip", dict(root="ci", beside="agni",
                                role="karman", past=True)),
        ("3.2.92", "kvip", dict(root="ci", beside="śyena",
                                role="karman", past=True,
                                names_a="agni")),
        ("3.2.93", "ini", dict(root="krī", beside="soma",
                               role="karman", past=True,
                               upasarga="vi", sense="kutsā")),
    )

    def test_every_giving_rule_answers_for_itself(self):
        for sutra, affix, where in self.CASES:
            with self.subTest(sutra=sutra, **where):
                answer = upapada_affix(**where)
                self.assertIsInstance(answer, Added)
                self.assertEqual(answer.by, sutra)
                self.assertEqual(answer.gives, affix)


class AHeadingThatAddsNothing(unittest.TestCase):
    """
    3.2.84 भूते. यदित ऊर्ध्वम् अनुक्रमिष्यामो भूत इत्येवं तद्
    वेदितव्यम् — whatever is said from here on is of the past. It gives
    no affix, so it has its own entry point, as 3.1's four headings do.
    """

    def test_it_gives_no_affix(self):
        self.assertEqual(bhute_heading().gives, "")
        self.assertEqual(bhute_heading().by, "3.2.84")

    def test_it_knows_what_falls_under_it(self):
        for sutra in ("3.2.85", "3.2.90", "3.2.93"):
            with self.subTest(sutra=sutra):
                self.assertEqual(bhute_heading(sutra).by, "3.2.84")
        for sutra in ("3.2.60", "3.2.83", "3.2.123", "3.1.1"):
            with self.subTest(sutra=sutra):
                self.assertIsInstance(bhute_heading(sutra), NotAdded)

    def test_it_stops_where_the_present_tense_rule_begins(self):
        """3.2.123 वर्तमाने लट् is the first rule it does not reach."""
        self.assertEqual((BHUTE_FROM, BHUTE_THROUGH), (84, 122))

    def test_and_it_is_registered_against_its_own_function(self):
        from src.astadhyayi.sutra import REGISTRY

        self.assertEqual(REGISTRY.get("3.2.84").apply.__name__,
                         "bhute_heading")

    def test_every_rule_under_it_carries_the_condition_it_confers(self):
        """
        None of them states भूते; all of them want it. That is what an
        अधिकार does, and since the codification has no way to
        represent 'running', each row has to carry it.
        """
        under = [r for r in UPAPADA
                 if BHUTE_FROM < int(r.sutra.rsplit(".", 1)[1])
                 <= BHUTE_THROUGH]
        self.assertTrue(under)
        for row in under:
            with self.subTest(sutra=row.sutra):
                self.assertTrue(row.past)

    def test_and_the_condition_is_live(self):
        """भूत इति किम्? अग्निष्टोमेन यजते."""
        self.assertNotEqual(
            upapada_affix(root="yaj", beside="agniṣṭoma",
                          role="karaṇa").by, "3.2.85")


class FourRulesThatProvideNothing(unittest.TestCase):
    """
    3.2.76 क्विप् च gives क्विप् to EVERY root. So 3.2.87, 3.2.89,
    3.2.90 and 3.2.91 can only restrict — किमर्थमिदमुच्यते, यावता
    सर्वधातुभ्यः क्विब् विहित एव? — and the vṛtti counts the ways each
    of them does.
    """

    def test_all_four_are_marked_as_niyama(self):
        marked = sorted(r.sutra for r in UPAPADA if r.niyama)
        self.assertEqual(marked,
                         ["3.2.87", "3.2.89", "3.2.90", "3.2.91"])

    def test_3_2_89_leaves_the_root_free_where_the_others_do_not(self):
        """
        धातुनियमं वर्जयित्वा कालोपपदप्रत्ययनियमः — threefold, not
        fourfold, so OTHER companions work with कृ: शास्त्रकृत्,
        भाष्यकृत्. That difference is only visible because the vṛtti
        counts the restrictions rule by rule.
        """
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("threefold", REGISTRY.get("3.2.89").notes.lower())
        for sutra in ("3.2.87", "3.2.90", "3.2.91"):
            with self.subTest(sutra=sutra):
                self.assertIn("fourfold",
                              REGISTRY.get(sutra).notes.lower())

    def test_the_widest_rule_is_what_makes_them_necessary(self):
        """
        3.2.76 states almost nothing and reaches everything, which is
        why the four after it have nothing left to give.
        """
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("नियम", REGISTRY.get("3.2.76").notes)
        row = provisions_for("3.2.76")[0]
        self.assertEqual(row.of, ())
        self.assertEqual(row.beside, ())

    def test_all_three_of_3_2_87s_companions_are_reached(self):
        for word in BRAHMADI:
            with self.subTest(word=word):
                self.assertEqual(
                    upapada_affix(root="han", beside=word,
                                  role="karman", past=True).by,
                    "3.2.87")

    def test_all_five_of_3_2_89s_are_too(self):
        for word in SUKARMADI:
            with self.subTest(word=word):
                self.assertEqual(
                    upapada_affix(root="kṛ", beside=word,
                                  role="karman", past=True).by,
                    "3.2.89")

    def test_and_the_veda_hands_back_what_3_2_87_shut_out(self):
        """
        पूर्वेण नियमाद् अप्राप्तः क्विप् प्रत्ययो विधीयते — मातृहा,
        with a companion 3.2.87 does not name.
        """
        self.assertEqual(
            upapada_affix(root="han", beside="mātṛ", role="karman",
                          past=True, chandasi=True).by, "3.2.88")
        self.assertNotEqual(
            upapada_affix(root="han", beside="mātṛ", role="karman",
                          past=True).by, "3.2.88")


class AConditionOnTheWholeAndNotAPart(unittest.TestCase):
    """
    समुदायोपाधि. 3.2.80's व्रत is conveyed by root and companion and
    affix TOGETHER — धातूपपदप्रत्ययसमुदायेन व्रतं गम्यते — and 3.2.92's
    अग्न्याख्या likewise. Two of them in one pāda.
    """

    def test_both_are_recorded_as_such(self):
        from src.astadhyayi.sutra import REGISTRY

        for sutra in ("3.2.80", "3.2.92"):
            with self.subTest(sutra=sutra):
                self.assertIn("समुदाय", REGISTRY.get(sutra).notes)

    def test_3_2_92_wants_a_settled_name_and_not_a_sense(self):
        """
        आख्याग्रहणं रूढिसंप्रत्ययार्थम् — a hawk-shaped ALTAR, not a
        hawk. Codified through `names_a`, the field that already
        carries what a finished word denotes.
        """
        self.assertEqual(
            upapada_affix(root="ci", beside="śyena", role="karman",
                          past=True, names_a="agni").by, "3.2.92")
        self.assertNotEqual(
            upapada_affix(root="ci", beside="śyena", role="karman",
                          past=True).by, "3.2.92")


class ARootPinnedByALaterRule(unittest.TestCase):
    """
    3.2.82's मन् is मन्यते of class four and not मनुते of class eight —
    and the ground is उत्तरसूत्रे हि खश्प्रत्यये विकरणकृतो विशेषः
    स्यात्, that with 3.2.83's खश् the class-marker would show a
    difference. A root disambiguated by a consequence one rule on.
    """

    def test_the_argument_is_recorded_where_it_can_be_found(self):
        from src.astadhyayi.sutra import REGISTRY

        notes = REGISTRY.get("3.2.82").notes
        self.assertIn("मन्यतेर्ग्रहणम्", notes)
        self.assertIn("3.2.83", notes)

    def test_and_both_rules_take_the_same_root(self):
        for where, sutra in (
                (dict(root="man", beside="darśanīya", role="sup"),
                 "3.2.82"),
                (dict(root="man", beside="darśanīya", role="sup",
                      sense="ātmamāna"), "3.2.83")):
            with self.subTest(sutra=sutra):
                self.assertEqual(upapada_affix(**where).by, sutra)


class RepetitionDoesThreeDifferentThings(unittest.TestCase):
    """
    A word said again though it is already running:

      3.2.77  to DEFEAT another rule — बाधकबाधनार्थं पुनर्वचनम्
      3.2.78  to END an anuvṛtti — पुनः सुब्ग्रहणम् उपसर्गनिवृत्त्यर्थम्
      3.2.93  to NARROW — पुनः कर्मग्रहणं कर्तुः कुत्सानिमित्ते कर्मणि
    """

    def test_3_2_77_defeats_and_is_held_to_where_it_must(self):
        self.assertEqual(
            upapada_affix(root="sthā", beside="śam", role="sup").by,
            "3.2.77")
        # elsewhere 3.2.4 gives the same क and keeps its own example
        self.assertEqual(
            upapada_affix(root="sthā", beside="sama", role="sup").by,
            "3.2.4")

    def test_3_2_78_ends_an_anuvrtti_so_a_preverb_does_not_come(self):
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("उपसर्गनिवृत्त्यर्थम्",
                      REGISTRY.get("3.2.78").notes)

    def test_3_2_93_narrows_to_a_blameworthy_object(self):
        """इह न भवति धान्यविक्रायः — selling grain is no reproach."""
        self.assertEqual(
            upapada_affix(root="krī", beside="soma", role="karman",
                          past=True, upasarga="vi",
                          sense="kutsā").by, "3.2.93")
        self.assertNotEqual(
            upapada_affix(root="krī", beside="dhānya", role="karman",
                          past=True, upasarga="vi").by, "3.2.93")


class AFieldReusedRatherThanRenamed(unittest.TestCase):
    """
    The eighth field-name collision, and the first to resolve toward
    reuse. `upamana` already existed as a STRING — what role the thing
    likened to plays, which 3.1.10 and 3.1.11 divide on — and 3.2.79
    asks that same question, wanting the agent. The seven before this
    were two questions under one name; this was one question under two
    spellings.
    """

    def test_3_2_79_carries_the_role_and_not_a_flag(self):
        row = provisions_for("3.2.79")[0]
        self.assertEqual(row.upamana, "kartṛ")

    def test_the_other_role_is_the_vrttis_own_counter_example(self):
        """कर्तरीति किम्? अपूपानिव भक्षयति माषान्."""
        self.assertNotEqual(
            upapada_affix(root="bhakṣ", beside="apūpa", role="sup",
                          upamana="karman").by, "3.2.79")

    def test_and_the_field_still_answers_for_the_earlier_rules(self):
        """
        3.1.10 and 3.1.11 use the same name for the same question, so
        reusing it must not have disturbed them.
        """
        from src.astadhyayi.sanadi import sanadi_affix

        answer = sanadi_affix(base="putra", is_root=False,
                              sense="ācāra", upamana="karman")
        self.assertEqual(answer.by, "3.1.10")


class NamingTheAffixWhenTwoOpenRulesOverlap(unittest.TestCase):
    """
    3.2.75 and 3.2.76 are both open and both reach स्रंस्, one giving
    four affixes and the other क्विप्. Neither is wrong, and without a
    way to say which affix is meant the resolver can only pick by
    specificity.
    """

    def test_naming_the_affix_reaches_the_rule_that_gives_it(self):
        self.assertEqual(
            upapada_affix(root="sraṃs", beside="ukhā", attested=True,
                          wants="kvip").by, "3.2.76")
        self.assertEqual(
            upapada_affix(root="sraṃs", beside="ukhā", attested=True,
                          wants="manin").by, "3.2.75")

    def test_it_also_reaches_an_affix_a_rule_carries_on_also(self):
        """3.2.44 gives अण् and खच् both; asking after either finds it."""
        self.assertEqual(
            upapada_affix(root="kṛ", beside="kṣema", role="karman",
                          wants="खच्").by, "3.2.44")

    def test_and_leaving_it_out_changes_nothing(self):
        self.assertEqual(
            upapada_affix(root="kṛ", beside="kumbha",
                          role="karman").by, "3.2.1")


if __name__ == "__main__":
    unittest.main()
