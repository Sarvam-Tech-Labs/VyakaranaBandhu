# -*- coding: utf-8 -*-
"""
3.2.48 to 3.2.60 — ड, णिनि, टक्, ख्युन्, खिष्णुच् and क्विन्.

Four things this block asserts that no earlier one could:

  * a sūtra of TWO KINDS at once — 3.2.59 fixes five words outright
    and names three roots that take the affix by rule, so it is
    registered against the table and feeds the fixed-word lookup;
  * a rule that names a companion in order to REFUSE it (3.2.58),
    where every rule before named companions to require them;
  * one condition asked as two questions, because the vṛtti asks after
    each separately — the च्वि meaning without the च्वि affix;
  * a rule wanting NO companion at all (3.2.59's युज् केवलात्).
"""

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi.upapada_krt import (
    ADHYADI, ANCADI, ANTADI, TYADADI, UPAPADA,
    Added, NotAdded, nipatana, provisions_for, upapada_affix,
)


class EachRuleAnswersForItsOwnExample(unittest.TestCase):

    CASES = (
        ("3.2.48", "ḍa", dict(root="gam", beside="dūra",
                              role="karman")),
        ("3.2.49", "ḍa", dict(root="han", beside="śatru",
                              role="karman", sense="āśis")),
        ("3.2.50", "ḍa", dict(root="han", beside="tamas",
                              role="karman", upasarga="apa")),
        ("3.2.51", "ṇini", dict(root="han", beside="kumāra",
                                role="karman")),
        ("3.2.52", "ṭak", dict(root="han", beside="jāyā",
                               role="karman", sense="lakṣaṇa")),
        ("3.2.53", "ṭak", dict(root="han", beside="śleṣman",
                               role="karman", agent="amanuṣya")),
        ("3.2.54", "ṭak", dict(root="han", beside="hastin",
                               role="karman", sense="śakti")),
        ("3.2.56", "khyun", dict(root="kṛ", beside="āḍhya",
                                 role="karman", sense="karaṇa",
                                 cvi_sense=True)),
        ("3.2.57", "khiṣṇuc", dict(root="bhū", beside="āḍhya",
                                   role="sup", cvi_sense=True)),
        ("3.2.58", "kvin", dict(root="spṛś", beside="ghṛta",
                                role="sup")),
        ("3.2.59", "kvin", dict(root="añc", beside="pra", role="sup")),
        ("3.2.60", "kañ", dict(root="dṛś", beside="tad", role="sup")),
    )

    def test_every_giving_rule_answers_for_itself(self):
        for sutra, affix, where in self.CASES:
            with self.subTest(sutra=sutra, **where):
                answer = upapada_affix(**where)
                self.assertIsInstance(answer, Added)
                self.assertEqual(answer.by, sutra)
                self.assertEqual(answer.gives, affix)

    def test_the_pada_runs_unbroken_from_its_first_sutra(self):
        """
        The single place this is asserted, and it names NO endpoint.

        Four copies of this test have now gone stale — twice as
        "1 to 28", twice as "1 to 47" — each time the pāda grew. The
        standing rule was already *assert the property, not the
        census*, and a range still reads like a property while
        behaving like a hardcoded count. Contiguity from the first
        sūtra is the actual property, and it survives the pāda
        growing.
        """
        from src.astadhyayi.sutra import REGISTRY

        numbers = sorted(
            int(str(s.id).rsplit(".", 1)[1]) for s in REGISTRY.all()
            if str(s.id).startswith("3.2."))
        self.assertTrue(numbers, "3.2 has nothing codified at all")
        self.assertEqual(numbers, list(range(1, len(numbers) + 1)),
                         "3.2 has a gap")

    def test_all_of_3_2_48s_companions_are_reached(self):
        for word in ANTADI:
            with self.subTest(word=word):
                self.assertEqual(
                    upapada_affix(root="gam", beside=word,
                                  role="karman").by, "3.2.48")

    def test_both_cvi_rules_reach_all_seven_of_their_companions(self):
        for word in ADHYADI:
            with self.subTest(word=word):
                self.assertEqual(
                    upapada_affix(root="kṛ", beside=word,
                                  role="karman", sense="karaṇa",
                                  cvi_sense=True).by, "3.2.56")
                self.assertEqual(
                    upapada_affix(root="bhū", beside=word, role="sup",
                                  cvi_sense=True).by, "3.2.57")

    def test_3_2_60_reaches_every_pronoun_and_the_varttikas_two(self):
        for word in TYADADI:
            with self.subTest(word=word):
                self.assertEqual(
                    upapada_affix(root="dṛś", beside=word,
                                  role="sup").by, "3.2.60")
        # समानान्ययोश्चेति वक्तव्यम् — सदृशः, अन्यादृशः
        for word in ("samāna", "anya"):
            self.assertIn(word, TYADADI)


class ASutraOfTwoKindsAtOnce(unittest.TestCase):
    """
    3.2.59 is the first the project has met that must be codified in
    both places. ऋत्विगादयः पञ्चशब्दाः क्विन्प्रत्ययान्ता निपात्यन्ते —
    five WORDS fixed; अपरे त्रयो धातवो निर्दिश्यन्ते — three ROOTS
    named, which take the affix by rule.
    """

    def test_the_five_words_are_given_whole(self):
        for word in ("ṛtvij", "dadhṛṣ", "sraj", "diś", "uṣṇih"):
            with self.subTest(word=word):
                answer = nipatana(word)
                self.assertEqual(answer.by, "3.2.59")
                self.assertEqual(answer.gives, "kvin")

    def test_and_the_three_roots_take_it_by_rule(self):
        self.assertEqual(
            upapada_affix(root="añc", beside="pra", role="sup").by,
            "3.2.59")
        for root in ("yuj", "kruñc"):
            with self.subTest(root=root):
                self.assertEqual(upapada_affix(root=root).by, "3.2.59")
        self.assertEqual(len(ANCADI), 3)

    def test_rtvij_records_that_the_vrtti_declines_to_derive_it(self):
        """
        रूढिरेषा यथाकथंचिदनुगन्तव्या — three derivations offered and
        none chosen, because the word is settled. A commentary
        declining to derive what usage has already fixed, which is
        exactly the ground a निपातन stands on.
        """
        self.assertIn("रूढिरेषा", nipatana("ṛtvij").why)


class ARuleThatWantsNoCompanionAtAll(unittest.TestCase):
    """
    युजेः क्रुञ्चेश्च केवलादेव — from the BARE root. Every rule of the
    pāda before this one required a companion or was indifferent; this
    is the first that requires its absence.
    """

    def test_the_bare_root_takes_it(self):
        self.assertEqual(upapada_affix(root="yuj").by, "3.2.59")

    def test_and_a_companion_puts_it_out_of_reach(self):
        answer = upapada_affix(root="yuj", beside="aśva",
                               role="karman")
        self.assertNotEqual(answer.by, "3.2.59")

    def test_and_what_it_takes_instead_is_the_next_rule(self):
        """
        सोपपदात् तु सत्सूद्विष० इत्यादिना क्विब् भवति, अश्वयुक्.

        This stood as a DEBT: with a companion युज् should take
        3.2.61's क्विप्, and 3.2.61 was not codified, so the
        fall-through landed on 3.2.1 and the contrast could not be
        shown. The test asserted the debt so that paying it would be
        noticed — it went red the moment 3.2.61 was registered, which
        is what a debt asserted as a test is for.

        Now the whole of the vṛtti's contrast runs: bare, क्विन् by
        3.2.59; with a companion, क्विप् by 3.2.61.
        """
        bare = upapada_affix(root="yuj")
        with_companion = upapada_affix(root="yuj", beside="aśva",
                                       role="karman")
        self.assertEqual((bare.by, bare.gives), ("3.2.59", "kvin"))
        self.assertEqual((with_companion.by, with_companion.gives),
                         ("3.2.61", "kvip"))


class ARuleThatNamesACompanionToRefuseIt(unittest.TestCase):
    """
    स्पृशोऽनुदके क्विन्. Every other rule of the pāda names companions
    to require them; this one names उदक to shut it out, which is why
    the table needed a field of its own for it.
    """

    def test_any_other_word_is_reached_and_that_one_is_not(self):
        for word in ("ghṛta", "mantra", "jala"):
            with self.subTest(word=word):
                self.assertEqual(
                    upapada_affix(root="spṛś", beside=word,
                                  role="sup").by, "3.2.58")
        answer = upapada_affix(root="spṛś", beside="udaka", role="sup")
        self.assertNotEqual(answer.by, "3.2.58")

    def test_the_refusal_is_held_in_its_own_field(self):
        row = provisions_for("3.2.58")[0]
        self.assertEqual(row.not_beside, ("udaka",))
        self.assertEqual(row.beside, ())


class OneConditionAskedAsTwoQuestions(unittest.TestCase):
    """
    च्व्यर्थेष्वच्वौ — the companion must carry the sense of BECOMING
    and must not carry the affix that expresses it. The vṛtti asks
    after each separately, so the code does too.
    """

    def test_the_sense_is_required(self):
        """च्व्यर्थेष्विति किम्? आढ्यं तैलेन कुर्वन्ति."""
        self.assertNotEqual(
            upapada_affix(root="kṛ", beside="āḍhya", role="karman",
                          sense="karaṇa").by, "3.2.56")

    def test_and_the_affix_is_refused(self):
        """अच्वाविति किम्? आढ्यीकुर्वन्त्यनेन."""
        self.assertNotEqual(
            upapada_affix(root="kṛ", beside="āḍhya", role="karman",
                          sense="karaṇa", cvi_sense=True,
                          cvi_ending=True).by, "3.2.56")

    def test_both_rules_carry_both_and_they_are_separate_fields(self):
        for sutra in ("3.2.56", "3.2.57"):
            with self.subTest(sutra=sutra):
                row = provisions_for(sutra)[0]
                self.assertTrue(row.cvi_sense)
                self.assertTrue(row.refuses_cvi_ending)

    def test_the_two_rules_differ_only_in_the_karaka(self):
        """
        कर्तरीति किम्? करणे मा भूत्. Same seven companions, same two
        च्वि conditions — the instrument gets 3.2.56's ख्युन् and the
        agent gets 3.2.57's two affixes.
        """
        instrument = upapada_affix(root="kṛ", beside="āḍhya",
                                   role="karman", sense="karaṇa",
                                   cvi_sense=True)
        agent = upapada_affix(root="bhū", beside="āḍhya", role="sup",
                              cvi_sense=True)
        self.assertEqual(instrument.gives, "khyun")
        self.assertEqual(agent.gives, "khiṣṇuc")
        self.assertEqual(agent.also, "खुकञ्")


class TheHumanAgentIsShutOutAndLetBackIn(unittest.TestCase):
    """
    3.2.53 excludes the human doer outright — अमनुष्यकर्तृके. 3.2.54
    reaches him again, but BY ANOTHER ROAD: what it states is शक्तौ,
    and मनुष्यकर्तृकार्थ आरम्भः is only the vṛtti's reason for it. So
    the codified condition is the one written.
    """

    def test_3_2_53_needs_the_non_human_doer(self):
        """अमनुष्यकर्तृक इति किम्? आखुघातः शूद्रः."""
        self.assertEqual(
            upapada_affix(root="han", beside="ākhu", role="karman",
                          agent="amanuṣya").by, "3.2.53")
        self.assertNotEqual(
            upapada_affix(root="han", beside="ākhu", role="karman",
                          agent="manuṣya").by, "3.2.53")

    def test_3_2_54_states_the_ability_and_not_the_doer(self):
        """
        The reason for a rule is not a condition in it. 3.2.54 answers
        for a human agent — that is what it was written for — but it
        answers on शक्तौ, so it answers with no agent asserted at all.
        """
        row = provisions_for("3.2.54")[0]
        self.assertEqual(row.sense, "śakti")
        self.assertEqual(row.agent, "")
        self.assertEqual(
            upapada_affix(root="han", beside="hastin", role="karman",
                          sense="śakti", agent="manuṣya").by, "3.2.54")
        self.assertEqual(
            upapada_affix(root="han", beside="hastin", role="karman",
                          sense="śakti").by, "3.2.54")

    def test_and_without_the_ability_the_general_rule_answers(self):
        """शक्ताविति किम्? विषेण हस्तिनं हन्ति हस्तिघातः."""
        self.assertEqual(
            upapada_affix(root="han", beside="hastin",
                          role="karman").by, "3.2.1")


class TheDebtsThisBlockRecords(unittest.TestCase):

    def test_3_2_53s_hardest_question_is_answered_from_outside(self):
        """
        इह कस्माद् न भवति चौरघातो हस्ती? — an elephant is no man, so
        why is the form not made. The vṛtti answers by 3.3.113
        कृत्यल्युटो बहुलम्.

        PAID: that rule is codified now, so the answer can be run and
        not merely recorded. What it says is that these affixes reach
        beyond where they were given, which is the whole of why a
        commentary sends an awkward form to it.
        """
        from src.astadhyayi.bhava_krt import krtya_lyut_bahulam
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("3.3.113", {str(s.id) for s in REGISTRY.all()})
        answer = krtya_lyut_bahulam()
        self.assertEqual(answer.by, "3.3.113")
        self.assertIn("न्यत्रापि भवन्ति", answer.why)
        self.assertIn("3.3.113", REGISTRY.get("3.2.53").notes)
        notes = REGISTRY.get("3.2.53").notes
        self.assertIn("3.3.113", notes)
        self.assertIn("DEBT", notes)

    def test_this_block_declares_no_reuse(self):
        """
        Three markers here are written for rules elsewhere — 3.2.58's
        न for 8.2.62, 3.2.60's ञ for 4.1.15 — but all act on the
        finished form, downstream of choosing the affix. Cited in the
        notes, not declared, for the reason 3.2.3's false 1.1.71 taught.
        """
        from src.astadhyayi.sutra import REGISTRY

        for n in range(48, 61):
            with self.subTest(sutra="3.2.%d" % n):
                self.assertEqual(REGISTRY.get("3.2.%d" % n).reuses, ())
        self.assertIn("8.2.62", REGISTRY.get("3.2.58").notes)
        self.assertIn("4.1.15", REGISTRY.get("3.2.60").notes)


if __name__ == "__main__":
    unittest.main()
