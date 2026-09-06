# -*- coding: utf-8 -*-
"""
3.2.1 to 3.2.20 — the affix a root takes when a word stands beside it.

Expectations are the Kāśikā's worked forms and, wherever it asks
*kim*, its own counter-example. Three things here are worth more than
the per-rule coverage:

  * the अपवाद chain actually cuts, and cuts in the right direction —
    3.2.2 beats 3.2.3 though 3.2.3 is the narrower-looking rule;
  * यथासंख्यम् is enforced, so स्तम्ब cannot go with जप्;
  * the one condition the module does not own is ASKED — the preverb
    of 1.4.59 — and asking is tested by making the answer depend on
    that rule rather than on a list kept here. 1.1.71 is NOT among
    them, though the neighbouring runs ask it: आत् names a plain sound
    and forms no pratyāhāra, which is what made the false declaration
    easy to write.
"""

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi.upapada_krt import (
    BHIKSADI, HVADI, PURASADI, STAMBA_KARNA, TUNDA_SOKA, UPAPADA,
    Added, NotAdded, _how_specific, provisions_for, upapada_affix,
)


class EachRuleAnswersForItsOwnExample(unittest.TestCase):
    """The vṛtti's worked form for every one of the twenty."""

    CASES = (
        ("3.2.1", "aṇ", dict(root="kṛ", beside="kumbha", role="karman")),
        ("3.2.2", "aṇ", dict(root="hveñ", beside="svarga",
                             role="karman")),
        ("3.2.3", "ka", dict(root="dā", beside="go", role="karman")),
        ("3.2.4", "ka", dict(root="sthā", beside="sama", role="sup")),
        ("3.2.5", "ka", dict(root="parimṛj", beside="tunda",
                             role="karman")),
        ("3.2.6", "ka", dict(root="dā", beside="sarva", role="karman",
                             upasarga="pra")),
        ("3.2.7", "ka", dict(root="khyā", beside="go", role="karman",
                             upasarga="sam")),
        ("3.2.8", "ṭak", dict(root="gai", beside="śakra",
                              role="karman")),
        ("3.2.9", "ac", dict(root="hṛ", beside="aṃśa", role="karman")),
        ("3.2.10", "ac", dict(root="hṛ", beside="asthi", role="karman",
                              sense="vayas")),
        ("3.2.11", "ac", dict(root="hṛ", beside="puṣpa", role="karman",
                              upasarga="āṅ", sense="tācchīlya")),
        ("3.2.12", "ac", dict(root="arh", beside="pūjā",
                              role="karman")),
        ("3.2.13", "ac", dict(root="ram", beside="stamba", role="sup")),
        ("3.2.14", "ac", dict(root="kṛ", beside="śam", role="sup",
                              sense="saṃjñā")),
        ("3.2.15", "ac", dict(root="śī", beside="kha",
                              role="adhikaraṇa")),
        ("3.2.16", "ṭa", dict(root="car", beside="kuru",
                              role="adhikaraṇa")),
        ("3.2.17", "ṭa", dict(root="car", beside="bhikṣā", role="sup")),
        ("3.2.18", "ṭa", dict(root="sṛ", beside="puras", role="sup")),
        ("3.2.19", "ṭa", dict(root="sṛ", beside="pūrva",
                              role="kartṛ")),
        ("3.2.20", "ṭa", dict(root="kṛ", beside="śoka", role="karman",
                              sense="hetu-tācchīlya-ānulomya")),
    )

    def test_every_rule_of_the_run_answers_for_itself(self):
        for sutra, affix, where in self.CASES:
            with self.subTest(sutra=sutra, **where):
                answer = upapada_affix(**where)
                self.assertIsInstance(answer, Added)
                self.assertEqual(answer.by, sutra)
                self.assertEqual(answer.gives, affix)

    def test_every_named_member_of_a_list_is_reached(self):
        """A row that names a group must answer for all of it."""
        for group, sutra, extra in (
            (HVADI, "3.2.2", dict(beside="x", role="karman")),
            (BHIKSADI, "3.2.17", dict(root="car", role="sup")),
            (PURASADI, "3.2.18", dict(root="sṛ", role="sup")),
        ):
            for member in group:
                with self.subTest(sutra=sutra, member=member):
                    where = dict(extra)
                    if "root" in where:
                        where["beside"] = member
                    else:
                        where["root"] = member
                    self.assertEqual(upapada_affix(**where).by, sutra)


class TheApavadaChainCutsBothWays(unittest.TestCase):
    """
    3.2.1 is the widest and everything after it is an अपवाद — but the
    order in which they cut is not the order they are written in, and
    a first-match or last-match resolver gets it wrong either way.
    """

    def test_3_2_1_answers_where_nothing_cuts_in(self):
        """कर्मण्यण् — and it says the least of any row in the table."""
        self.assertEqual(
            upapada_affix(root="kṛ", beside="nagara", role="karman").by,
            "3.2.1")
        self.assertEqual(_how_specific(provisions_for("3.2.1")[0]), 1)

    def test_3_2_2_beats_3_2_3_though_it_states_less_about_shape(self):
        """
        कप्रत्ययस्यापवादः. मा IS आ-final, so 3.2.3 reaches it and would
        give क; naming a ROOT has to outweigh naming a shape or
        धान्यमायः comes out as *धान्यमः. A live conflict, tested here
        on the one of the three that has the shape today.
        """
        from src.astadhyayi.krt_conditions import ends_in_a

        named = provisions_for("3.2.2")[0]
        shape = provisions_for("3.2.3")[0]
        self.assertTrue(ends_in_a("māṅ".rstrip("ṅ")))
        self.assertGreater(_how_specific(named), _how_specific(shape))
        self.assertEqual(
            upapada_affix(root="māṅ", beside="dhānya",
                          role="karman").gives, "aṇ")
        self.assertEqual(
            upapada_affix(root="hveñ", beside="svarga",
                          role="karman").gives, "aṇ")

    def test_two_of_3_2_2s_roots_reach_3_2_3_only_through_6_1_45(self):
        """
        The debt, collected.

        ह्वेञ् and वेञ् are ए-final in upadeśa, not आ-final, so
        3.2.3's आतोऽनुपसर्गे कः does not reach them on their own
        shape — and the vṛtti's कप्रत्ययस्यापवादः holds only once
        6.1.45 आदेच उपदेशेऽशिति has turned the एच् into आ. That rule
        is codified now and `ends_in_a` asks it, so the contest
        3.2.2 was written to settle is one this code can finally
        stage.

        What makes the answer usable rather than accidental is the
        ORDER 6.1.45's vṛtti argues for: अशिति is a
        प्रसज्यप्रतिषेध, so the आ is अनैमित्तिक and is already there
        before any kṛt affix arrives to ask.
        """
        from src.astadhyayi.atva import becomes_a
        from src.astadhyayi.krt_conditions import ends_in_a
        from src.astadhyayi.sutra import REGISTRY

        self.assertTrue(REGISTRY.has("6.1.45"))
        for root in ("hveñ", "veñ"):
            with self.subTest(root=root):
                bare = root.rstrip("ñ")
                self.assertTrue(ends_in_a(bare))
                self.assertEqual(becomes_a(bare, final="e").sutra,
                                 "6.1.45")
        # And a root with no एच् is untouched by the new path.
        self.assertFalse(ends_in_a("pac"))
        self.assertIn("6.1.45", REGISTRY.get("3.2.2").notes)

    def test_3_2_6_and_3_2_7_exist_only_to_readmit_a_preverb(self):
        """
        सोपसर्गार्थ आरम्भः. दा is ā-final: bare it has 3.2.3's क
        already, and what 3.2.6 adds is क WITH प्र, which 3.2.3's
        अनुपसर्गे had shut out. So both must answer, by different rules.
        """
        bare = upapada_affix(root="dā", beside="go", role="karman")
        with_pra = upapada_affix(root="dā", beside="sarva",
                                 role="karman", upasarga="pra")
        self.assertEqual((bare.by, bare.gives), ("3.2.3", "ka"))
        self.assertEqual((with_pra.by, with_pra.gives), ("3.2.6", "ka"))

    def test_a_preverb_3_2_6_does_not_name_falls_back_to_3_2_1(self):
        """प्र इति किम्? गोसंदायः — with सम् the general अण् returns."""
        answer = upapada_affix(root="dā", beside="go", role="karman",
                               upasarga="sam")
        self.assertEqual((answer.by, answer.gives), ("3.2.1", "aṇ"))

    def test_3_2_20_hands_the_ground_back_to_3_2_1(self):
        """एतेष्विति किम्? कुम्भकारः — outside the three senses, अण्."""
        self.assertEqual(
            upapada_affix(root="kṛ", beside="kumbha", role="karman",
                          sense="hetu-tācchīlya-ānulomya").gives, "ṭa")
        self.assertEqual(
            upapada_affix(root="kṛ", beside="kumbha",
                          role="karman").gives, "aṇ")


class YathasankhyamBindsTheRulesThatStateIt(unittest.TestCase):
    """
    3.2.5 and 3.2.13 each name two roots and two words, and the pairing
    is crosswise. Held as two flat lists, स्तम्बेजपः would be formed —
    which is why the table keeps the pairs and not the members.
    """

    def test_each_pair_answers_for_its_own_rule(self):
        for beside, root in TUNDA_SOKA:
            with self.subTest(pair=(beside, root)):
                self.assertEqual(
                    upapada_affix(root=root, beside=beside,
                                  role="karman").by, "3.2.5")
        for beside, root in STAMBA_KARNA:
            with self.subTest(pair=(beside, root)):
                self.assertEqual(
                    upapada_affix(root=root, beside=beside,
                                  role="sup").by, "3.2.13")

    def test_a_crossed_pair_is_not_reached_by_the_rule(self):
        """रम् with कर्ण, जप् with स्तम्ब — neither is the rule's."""
        for root, beside in (("ram", "karṇa"), ("jap", "stamba")):
            with self.subTest(root=root, beside=beside):
                self.assertNotEqual(
                    upapada_affix(root=root, beside=beside,
                                  role="sup").by, "3.2.13")

    def test_and_the_crossed_pair_of_3_2_5_falls_to_the_general_rule(self):
        """
        परिमृज् with शोक is not 3.2.5's, but it is still a root with an
        object beside it, so 3.2.1 reaches it — a different form and a
        different rule, which is the whole point of the pairing.
        """
        crossed = upapada_affix(root="parimṛj", beside="śoka",
                                role="karman")
        self.assertEqual((crossed.by, crossed.gives), ("3.2.1", "aṇ"))


class TheConditionsAreAskedOfTheRulesThatOwnThem(unittest.TestCase):
    """
    Not tidiness: a restated condition is a second copy of a rule, and
    two copies drift. These tests pin the ANSWER to the other rule.
    """

    def test_the_preverb_is_1_4_59s_question(self):
        """
        उपसर्गाः क्रियायोगे. What makes this a real test rather than a
        tautology is देव: it is not a preverb, so attaching it must
        leave 3.2.3 — which refuses preverbs — still answering.
        """
        from src.astadhyayi.krt_conditions import has_upasarga

        self.assertTrue(has_upasarga("sam"))
        self.assertFalse(has_upasarga("deva"))
        self.assertEqual(
            upapada_affix(root="dā", beside="go", role="karman",
                          upasarga="deva").by, "3.2.3")
        self.assertEqual(
            upapada_affix(root="dā", beside="go", role="karman",
                          upasarga="sam").by, "3.2.1")

    def test_3_2_3s_a_final_is_the_sivasutras_through_1_1_71(self):
        """
        आतः. A consonant-final root with an object beside it must fall
        through to 3.2.1, and the reason must be the sound and not a
        list kept here.
        """
        from src.astadhyayi.krt_conditions import ends_in_a

        self.assertTrue(ends_in_a("dā"))
        self.assertFalse(ends_in_a("kṛ"))
        self.assertEqual(
            upapada_affix(root="kṛ", beside="kumbha", role="karman").by,
            "3.2.1")

    def test_1_1_71_is_still_not_declared_here(self):
        """
        1.1.71 was declared here once and the reuse guard refused it:
        आत् names a plain sound, so no pratyāhāra is ever formed and
        the rule that makes a span denote anything is never reached.
        The neighbouring runs DO declare it — हल्, अच् and इक् are
        spans — which is exactly how the wrong declaration got made.

        6.1.45 joined the list later and is a different case: it is
        not a span rule but the rule that MAKES ह्वेञ् आ-final, and
        `ends_in_a` calls it. Code calling code, which is the only
        thing the guard accepts.
        """
        from src.astadhyayi.sutra import REGISTRY

        for code in ("3.2.3", "3.2.8"):
            self.assertNotIn("1.1.71", REGISTRY.get(code).reuses, code)
            self.assertIn("1.4.59", REGISTRY.get(code).reuses, code)
        self.assertEqual(set(REGISTRY.get("3.2.3").reuses),
                         {"1.4.59", "6.1.45"})
        self.assertEqual(set(REGISTRY.get("3.2.8").reuses), {"1.4.59"})


class TheSenseAndRoleConditionsAreLive(unittest.TestCase):

    def test_3_2_9_refuses_the_sense_it_names(self):
        """अनुद्यमन इति किम्? भारहारः — of lifting, the अण् stands."""
        self.assertEqual(
            upapada_affix(root="hṛ", beside="aṃśa", role="karman").by,
            "3.2.9")
        self.assertEqual(
            upapada_affix(root="hṛ", beside="bhāra", role="karman",
                          sense="udyamana").by, "3.2.1")

    def test_3_2_10_gives_back_the_very_sense_3_2_9_refused(self):
        """
        उद्यमनार्थोऽयम् आरम्भः. Where an age is meant, अच् comes even
        of lifting — so the pair has to be read together, and a
        resolver that took 3.2.9's प्रतिषेध as final would lose it.
        """
        self.assertEqual(
            upapada_affix(root="hṛ", beside="asthi", role="karman",
                          sense="vayas").gives, "ac")

    def test_3_2_19s_whole_content_is_the_karaka(self):
        """
        कर्तरीति किम्? पूर्वसारः. Same word, same root: only the role
        differs, and it decides the affix. The sharpest case in the
        pāda for why the role is an input.
        """
        as_agent = upapada_affix(root="sṛ", beside="pūrva",
                                 role="kartṛ")
        as_object = upapada_affix(root="sṛ", beside="pūrva",
                                  role="karman")
        self.assertEqual((as_agent.by, as_agent.gives), ("3.2.19", "ṭa"))
        self.assertEqual((as_object.by, as_object.gives),
                         ("3.2.1", "aṇ"))

    def test_sup_is_wider_than_the_named_karakas(self):
        """
        3.2.4's सुपि wants any finished word, so naming the companion
        an object or a place must not stop it — but 3.2.16's
        अधिकरणे must.
        """
        for role in ("sup", "karman", "adhikaraṇa", "kartṛ"):
            with self.subTest(role=role):
                self.assertEqual(
                    upapada_affix(root="sthā", beside="sama",
                                  role=role).by, "3.2.4")
        self.assertEqual(
            upapada_affix(root="car", beside="kuru",
                          role="adhikaraṇa").by, "3.2.16")
        self.assertNotEqual(
            upapada_affix(root="car", beside="kuru",
                          role="karman").by, "3.2.16")


class ARefusalDoesNotNameARuleThatDidNotRefuse(unittest.TestCase):
    """
    A rule that simply fails to reach a word has not acted on it, so it
    must not be reported. None of 3.2.1–20 is a प्रतिषेध, so every
    refusal here is nameless.
    """

    def test_a_root_no_rule_reaches_gets_no_sutra(self):
        answer = upapada_affix(root="ram", beside="karṇa", role="sup")
        self.assertIsInstance(answer, NotAdded)
        self.assertEqual(answer.by, "")
        self.assertEqual(answer.gives, "")

    def test_a_companion_in_no_role_at_all_is_refused(self):
        """
        3.2.1 wants the object. With no role asserted, no rule of the
        run has its condition, and the answer says so without blaming
        one.
        """
        answer = upapada_affix(root="kṛ", beside="kumbha")
        self.assertIsInstance(answer, NotAdded)
        self.assertEqual(answer.by, "")


class TheKasikaExamplesThatAreNotFormedHere(unittest.TestCase):
    """
    अनभिधानात्. 3.2.1 as written reaches ग्रामं गच्छति, and the vṛtti
    stops it by hand because usage has no such word. The table has no
    condition for that, so the code DOES form it — and this test
    records that, rather than pretending otherwise.
    """

    def test_the_rule_reaches_them_and_the_limit_is_recorded_in_prose(self):
        from src.astadhyayi.sutra import REGISTRY

        for root, beside in (("gam", "grāma"), ("dṛś", "āditya"),
                             ("śru", "himavat")):
            with self.subTest(root=root, beside=beside):
                self.assertEqual(
                    upapada_affix(root=root, beside=beside,
                                  role="karman").by, "3.2.1")
        notes = REGISTRY.get("3.2.1").notes
        self.assertIn("अनभिधानात्", notes)
        self.assertIn("SCAR", notes,
                      "a limit the code does not enforce is a scar and "
                      "must be marked as one")


if __name__ == "__main__":
    unittest.main()


class TheGanapathaHeldTwoGanasTheCodeDidNot(unittest.TestCase):
    """
    Found by asking `load_ganapatha()` which gaṇas it keys to this
    pāda. It named two — मूलविभुजादि at 3.2.5, पार्श्वादि at 3.2.15 —
    and neither was in the code, because both sit in vārttikas at the
    END of their Kāśikā entries and the first reading had been
    truncated. The corpus knew before the codification did.
    """

    def test_the_members_come_from_the_corpus_and_not_from_here(self):
        """
        A hand-copied list would have to be corrected here whenever the
        corpus was. These are read at import, so they cannot drift.
        """
        from src.astadhyayi.corpus import load_ganapatha
        from src.astadhyayi.upapada_krt import MULAVIBHUJADI, PARSVADI

        gana = load_ganapatha()
        self.assertEqual(
            PARSVADI,
            tuple(i for e in gana["3.2.15"] for i in e.items))
        self.assertEqual(
            MULAVIBHUJADI,
            tuple(i for e in gana["3.2.5"] for i in e.items))

    def test_the_vrttis_own_examples_are_in_the_corpus_list(self):
        """
        The check that the gaṇa really belongs to this rule: the words
        the Kāśikā works under the vārttika must be members. पार्श्व,
        उदर and पृष्ठ come from पार्श्वादिषूपसंख्यानम्; उत्तान and
        अवमूर्धन् from उत्तानादिषु कर्तृषु — one gaṇa, two vārttikas.
        """
        from src.astadhyayi.upapada_krt import MULAVIBHUJADI, PARSVADI

        for word in ("pārśva", "udara", "pṛṣṭha", "uttāna"):
            with self.subTest(word=word):
                self.assertIn(word, PARSVADI)
        for word in ("mūlavibhuja", "nakhamuca", "kākaguha", "kumuda"):
            with self.subTest(word=word):
                self.assertIn(word, MULAVIBHUJADI)

    def test_3_2_15s_varttikas_reach_past_the_place(self):
        """
        What they buy is precisely that the companion need NOT be the
        अधिकरण the sūtra wants: पार्श्वाभ्यां शेते is instrumental and
        उत्तानः शेते is the agent. Both must answer where the bare
        rule would not.
        """
        for beside, role in (("pārśva", "sup"), ("uttāna", "kartṛ"),
                             ("digdhasaha", "sup")):
            with self.subTest(beside=beside, role=role):
                answer = upapada_affix(root="śī", beside=beside,
                                       role=role)
                self.assertEqual(answer.by, "3.2.15")
                self.assertEqual(answer.gives, "ac")
        # and the sūtra's own clause still answers for a real place
        self.assertEqual(
            upapada_affix(root="śī", beside="kha",
                          role="adhikaraṇa").gives, "ac")

    def test_the_vedic_varttika_changes_the_affix_not_the_companion(self):
        """
        गिरौ डश्छन्दसि — the one of the four that gives a different
        affix, and it holds in the Veda only.
        """
        vedic = upapada_affix(root="śī", beside="giri",
                              role="adhikaraṇa", chandasi=True)
        self.assertEqual((vedic.by, vedic.gives), ("3.2.15", "ḍa"))
        self.assertEqual(
            upapada_affix(root="śī", beside="giri",
                          role="adhikaraṇa").gives, "ac")

    def test_3_2_5s_varttika_supplies_whole_words_not_a_rule(self):
        """
        मूलानि विभुजतीति मूलविभुजो रथः — the gaṇa lists the FINISHED
        words, not the companions, so they are looked up whole. The
        गणपाठ marks the list आकृतिगण, so it is open and these are
        examples.
        """
        from src.astadhyayi.upapada_krt import nipatana

        for word in ("mūlavibhuja", "kumuda"):
            with self.subTest(word=word):
                answer = nipatana(word)
                self.assertEqual(answer.by, "3.2.5")
                self.assertEqual(answer.gives, "ka")

    def test_each_fixed_word_carries_its_own_affix(self):
        """
        The entry point had hardcoded इन् for every निपातन, which was
        true of 3.2.26 and false of 3.2.37 — उग्रम्पश्यः is a खश् form
        — and nothing caught it until 3.2.5's क arrived as a third.
        """
        from src.astadhyayi.upapada_krt import nipatana

        for word, affix in (("phalegrahi", "in"),
                            ("ugrampaśya", "khaś"),
                            ("mūlavibhuja", "ka")):
            with self.subTest(word=word):
                self.assertEqual(nipatana(word).gives, affix)
