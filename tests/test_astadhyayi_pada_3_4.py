# -*- coding: utf-8 -*-
"""
3.4.1 to 3.4.24 — the opening of अध्याय ३ पाद ४.

What this block asserts that no earlier one could:

  * a licence rather than a rule — an affix out of its proper TIME
    being correct anyway, and only one way round;
  * a rule given on a NAMED SCHOOL's authority, twice, and the naming
    itself making the rule optional;
  * a प्रतिषेध reaching backward PAST its neighbour;
  * a seventh suspension of 3.1.94, bounded by a pair of affixes
    rather than by a section;
  * a philosophical ground offered for a grammatical condition;
  * a commentary saying brevity is no consideration in ordinary
    speech.
"""

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from tests import unwrapped
from src.astadhyayi.dhatu_sambandha import (
    TUMARTHA, anuprayoga, dhatu_sambandha, nipatana, tumartha_affix,
)
from src.astadhyayi.ktva_namul import (
    KTVA, attributed_schools, ktva_namul,
)
from src.astadhyayi.lakara import LAKARA, lakara_for
from src.astadhyayi.tense_transfer import transferred_extent
from src.astadhyayi.upapada_krt import Added, NotAdded


class EachRuleAnswersForItsOwnExample(unittest.TestCase):

    LAKARA_CASES = (
        ("3.4.2", "loṭ", dict(time="sarva", doubled=True,
                              sense="kriyāsamabhihāra")),
        ("3.4.3", "loṭ", dict(time="sarva", doubled=True,
                              sense="samuccaya")),
        ("3.4.6", "luṅ", dict(time="sarva", chandasi=True)),
        ("3.4.7", "leṭ", dict(time="sarva", chandasi=True,
                              lin_nimitta=True)),
        ("3.4.8", "leṭ", dict(time="sarva", chandasi=True,
                              sense="upasaṃvāda")),
    )

    TUMARTHA_CASES = (
        ("3.4.9", dict()),
        ("3.4.12", dict(beside="śak")),
        ("3.4.13", dict(beside="īśvara")),
        ("3.4.14", dict(krtya_artha=True)),
        ("3.4.16", dict(root="sthā", bhava_laksana=True)),
        ("3.4.17", dict(root="sṛp", bhava_laksana=True)),
    )

    KTVA_CASES = (
        ("3.4.18", "ktvā", dict(beside="alam")),
        ("3.4.19", "ktvā", dict(root="mā", vyatihara=True)),
        ("3.4.20", "ktvā", dict(paravara=True)),
        ("3.4.21", "ktvā", dict(samana_kartrka=True, purvakala=True)),
        ("3.4.22", "ṇamul", dict(samana_kartrka=True, purvakala=True,
                                 abhiksnya=True)),
        ("3.4.24", "ktvā", dict(beside="agre", samana_kartrka=True,
                                purvakala=True)),
    )

    def test_the_lakara_rules_answer(self):
        for sutra, gives, where in self.LAKARA_CASES:
            with self.subTest(sutra=sutra, **where):
                answer = lakara_for(**where)
                self.assertIsInstance(answer, Added)
                self.assertEqual(answer.by, sutra)
                self.assertEqual(answer.gives, gives)

    def test_the_vedic_infinitive_rules_answer(self):
        for sutra, where in self.TUMARTHA_CASES:
            with self.subTest(sutra=sutra, **where):
                answer = tumartha_affix(**where)
                self.assertIsInstance(answer, Added)
                self.assertEqual(answer.by, sutra)

    def test_the_ktva_rules_answer(self):
        for sutra, gives, where in self.KTVA_CASES:
            with self.subTest(sutra=sutra, **where):
                answer = ktva_namul(**where)
                self.assertIsInstance(answer, Added)
                self.assertEqual(answer.by, sutra)
                self.assertEqual(answer.gives, gives)

    def test_the_fixed_words_answer(self):
        for word, sutra in (("prayai", "3.4.10"),
                            ("rohiṣyai", "3.4.10"),
                            ("avyathiṣyai", "3.4.10"),
                            ("avacakṣe", "3.4.15"),
                            ("dṛśe", "3.4.11"),
                            ("vikhye", "3.4.11")):
            with self.subTest(word=word):
                self.assertEqual(nipatana(word).by, sutra)

    def test_and_each_fixed_word_carries_its_own_affix(self):
        """
        3.4.10 fixes कै for one word and इष्यै for two others, so the
        affix cannot belong to the entry point — the correction 3.2's
        निपातन table needed within five rules of being written.
        """
        affixes = {nipatana(w).gives for w in
                   ("prayai", "rohiṣyai", "avacakṣe", "dṛśe")}
        self.assertGreater(len(affixes), 1)
        self.assertEqual(nipatana("prayai").gives, "kai")
        self.assertEqual(nipatana("rohiṣyai").gives, "iṣyai")


class ALicenceRatherThanARule(unittest.TestCase):
    """
    3.4.1 does not give an affix. It says an affix stated for the
    WRONG TIME is correct anyway, where two acts stand as qualifier
    and qualified — and only one way round.
    """

    def test_it_needs_the_relation(self):
        self.assertIsInstance(dhatu_sambandha(related=True), Added)
        self.assertIsInstance(dhatu_sambandha(), NotAdded)

    def test_the_asymmetry_is_recorded(self):
        answer = dhatu_sambandha(related=True)
        self.assertIn("विशेष्यकालमनुरुध्यते", answer.why)
        self.assertIn("विपर्ययो न भवति", answer.why)

    def test_and_the_repetition_that_widens_it_is_a_separate_claim(self):
        plain = dhatu_sambandha(related=True)
        wider = dhatu_sambandha(related=True, taddhita=True)
        self.assertNotIn("तद्धित", plain.why)
        self.assertIn("तद्धित", wider.why)

    def test_it_is_broader_than_the_transfers_of_3_3(self):
        """
        3.3.131 lent one NAMED tense's affixes to a NAMED time; this
        lends nothing, and says the ordinary affix is simply not
        wrong. The notes at both ends say so.
        """
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("3.3.131", REGISTRY.get("3.4.1").notes)

    def test_and_what_3_3_131_transfers_is_now_wholly_codified(self):
        """
        वर्तमाने लट् इत्यारभ्य यावद् उणादयो बहुलम् इति — 3.2.123 to
        3.3.1, both ends named as rules. Both are codified, so the
        extent is checkable and not merely recorded.
        """
        from src.astadhyayi.sutra import REGISTRY

        have = {str(s.id) for s in REGISTRY.all()}
        first, last = transferred_extent()
        self.assertIn(first, have)
        self.assertIn(last, have)


class ARuleGivenOnANamedSchoolsAuthority(unittest.TestCase):
    """
    3.4.18 प्राचामाचार्याणां मतेन and 3.4.19 उदीचामाचार्याणां मतेन —
    the teachers of the east and of the north. Nothing in 3.2 or 3.3
    attributed a rule this way, and in both the vṛtti reads the
    attribution ITSELF as making the rule optional.
    """

    def test_both_are_recorded_and_read_from_the_table(self):
        self.assertEqual(
            attributed_schools(),
            (("3.4.18", "prācām"), ("3.4.19", "udīcām")))

    def test_and_naming_a_school_is_what_makes_the_rule_optional(self):
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("प्राचांग्रहणं विकल्पार्थम्",
                      unwrapped(REGISTRY.get("3.4.18").notes))
        self.assertIn("उदीचांग्रहणात्",
                      unwrapped(REGISTRY.get("3.4.19").notes))

    def test_both_rows_are_marked_optional(self):
        rows = {r.sutra: r for r in KTVA}
        self.assertTrue(rows["3.4.18"].optional)
        self.assertTrue(rows["3.4.19"].optional)

    def test_and_a_principle_is_cited_as_a_courtesy(self):
        """
        3.4.18's वासरूपविधिश्चेत् पूजार्थम् — if 3.1.94 is invoked
        here it is for HONOURING THE TEACHERS and not for the
        grammar. Nothing else in these four pādas does that.
        """
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("पूजार्थम्", REGISTRY.get("3.4.18").notes)


class APratisedhaReachingBackwardPastItsNeighbour(unittest.TestCase):
    """
    3.4.23 refuses both क्त्वा and णमुल्. णमुल् is given in the rule
    immediately before; क्त्वा comes from 3.4.21 — णमुलनन्तरः, क्त्वा
    तु पूर्वसूत्रविहितोऽपि प्रतिषिध्यते.
    """

    def test_the_refusal_names_itself(self):
        answer = ktva_namul(beside="yad", anakanksa=True)
        self.assertIsInstance(answer, NotAdded)
        self.assertEqual(answer.by, "3.4.23")

    def test_and_it_refuses_the_ground_of_two_different_rules(self):
        from src.astadhyayi.sutra import REGISTRY

        notes = unwrapped(REGISTRY.get("3.4.23").notes)
        self.assertIn("णमुलनन्तरः", notes)
        self.assertIn("पूर्वसूत्रविहितोऽपि", notes)

    def test_without_the_second_condition_the_affix_still_comes(self):
        """अनाकाङ्क्ष इति किम्? — where more IS looked for."""
        answer = ktva_namul(beside="yad", samana_kartrka=True,
                            purvakala=True)
        self.assertIsInstance(answer, Added)


class ASeventhSuspensionBoundedByAPairOfAffixes(unittest.TestCase):
    """
    The six before it bounded 3.1.94 by SECTION. 3.4.24 bounds it by a
    PAIR OF AFFIXES: क्त्वाणमुलौ यत्र सह विधीयेते तत्र
    वासरूपविधिर्नास्ति — wherever in the grammar the two occur
    together.
    """

    def test_the_ground_is_recorded(self):
        from src.astadhyayi.sutra import REGISTRY

        notes = unwrapped(REGISTRY.get("3.4.24").notes)
        self.assertIn("क्त्वाणमुलौ यत्र सह विधीयेते", notes)
        # Sandhi has bitten this file's assertions four times now:
        # नास्ति + इति + एतत् runs together as नास्तीत्येतत्, so
        # neither नास्ति nor नास्तीति appears. Match up to the last
        # boundary that survives the joining, and no further.
        # `unwrapped` handles line breaks; sandhi has to be READ.
        self.assertIn("वासरूपविधिर्नास्ती", notes)

    def test_all_seven_suspensions_are_on_record(self):
        """
        One test holding the lot, so an eighth has somewhere to go
        rather than restarting the count. Each was found separately
        and none follows from another.
        """
        from src.astadhyayi.sutra import REGISTRY

        for sutra in ("3.2.146", "3.2.177", "3.3.10", "3.3.44",
                      "3.3.107", "3.3.163", "3.4.24"):
            with self.subTest(sutra=sutra):
                self.assertIn("वासरूप", REGISTRY.get(sutra).notes)

    def test_and_the_principle_they_suspend_is_codified(self):
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("3.1.94", {str(s.id) for s in REGISTRY.all()})


class APhilosophicalGroundForAGrammaticalCondition(unittest.TestCase):
    """
    3.4.21's समानकर्तृकता holds because
    शक्तिशक्तिमतोर्भेदस्याविवक्षितत्वात् — the difference between a
    POWER and WHAT HAS IT is not meant to be marked. The first ground
    of that kind in this reading.
    """

    def test_it_is_recorded(self):
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("शक्तिशक्तिमतोर्भेदस्य",
                      unwrapped(REGISTRY.get("3.4.21").notes))

    def test_and_the_rules_dual_is_read_as_not_binding(self):
        """
        द्विवचनमतन्त्रम् — so more than two acts are reached. The same
        reading 3.3.18 gave its own masculine singular: a grammatical
        form inside a rule not meaning what that form means anywhere
        else.
        """
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("द्विवचनमतन्त्रम्",
                      unwrapped(REGISTRY.get("3.4.21").notes))
        self.assertIn("न तन्त्रम्",
                      unwrapped(REGISTRY.get("3.3.18").notes))


class BrevityIsNoConsiderationInOrdinarySpeech(unittest.TestCase):
    """
    3.4.5's लाघवं च लौकिके शब्दव्यवहारे नाद्रियते. The tradition
    prizes brevity in the sūtras above almost everything, and here it
    says the value does not apply to the language they describe.
    """

    def test_the_remark_is_recorded(self):
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("लाघवं च लौकिके",
                      unwrapped(REGISTRY.get("3.4.5").notes))

    def test_and_the_two_anuprayoga_rules_differ_as_stated(self):
        self.assertEqual(anuprayoga().by, "3.4.4")
        self.assertEqual(anuprayoga(gathered=True).by, "3.4.5")
        self.assertNotEqual(anuprayoga().gives,
                            anuprayoga(gathered=True).gives)


class OneEndingForEveryTimeAtOnce(unittest.TestCase):
    """
    3.4.2 and after hold सर्वेषु कालेषु — in every time at once —
    because they stand under 3.4.1. Every rule of 3.2 and 3.3 chose an
    ending FOR a time.
    """

    def test_the_new_rows_carry_a_time_no_earlier_row_did(self):
        times = {r.time for r in LAKARA}
        self.assertIn("sarva", times)
        for row in LAKARA:
            if row.time == "sarva":
                with self.subTest(sutra=row.sutra):
                    self.assertTrue(row.sutra.startswith("3.4."))

    def test_and_a_query_for_one_time_does_not_reach_them(self):
        every = {r.sutra for r in LAKARA if r.time == "sarva"}
        self.assertTrue(every)
        for kwargs in (dict(), dict(time="bhaviṣyat"),
                       dict(time="vartamāna")):
            with self.subTest(**kwargs):
                self.assertNotIn(lakara_for(**kwargs).by, every)


class TheVedicInfinitivesRunOnAccentsThatCannotBeChecked(unittest.TestCase):
    """
    3.4.9 gives fifteen affixes and marks two PAIRS as differing in
    accent alone — स्वरे विशेषः. The sūtrapāṭha on disk is unaccented.
    """

    def test_the_rule_really_does_give_fifteen(self):
        row = next(r for r in TUMARTHA if r.sutra == "3.4.9")
        self.assertEqual(len(row.gives), 15)

    def test_the_pairs_that_differ_by_accent_are_both_there(self):
        row = next(r for r in TUMARTHA if r.sutra == "3.4.9")
        for pair in (("ase", "asen"), ("adhyai", "adhyain")):
            with self.subTest(pair=pair):
                self.assertIn(pair[0], row.gives)
                self.assertIn(pair[1], row.gives)

    def test_and_the_corpus_cannot_tell_them_apart(self):
        from src.astadhyayi.corpus import load_vidyut_sutrapatha

        text = load_vidyut_sutrapatha()["3.4.9"].text
        for mark in ("॑", "॒"):
            with self.subTest(mark=repr(mark)):
                self.assertNotIn(mark, text)


class ThePadaIsOpenAndTwoRulesOfItWereWrittenLongAgo(unittest.TestCase):
    """
    3.4.79 and 3.4.113 were codified before the reading reached this
    pāda, because derivations elsewhere stopped without them. They are
    left where they are.
    """

    def test_both_are_still_registered_and_still_work(self):
        from src.astadhyayi.anga import sarvadhatuka
        from src.astadhyayi.sutra import REGISTRY

        have = {str(s.id) for s in REGISTRY.all()}
        self.assertIn("3.4.79", have)
        self.assertIn("3.4.113", have)
        self.assertTrue(sarvadhatuka(tin=True).by)

    def test_the_reading_now_runs_unbroken_from_the_first_sutra(self):
        """
        No endpoint named: what holds is that the numbers run from one
        without a gap, up to wherever the reading has got to.
        """
        from src.astadhyayi.sutra import REGISTRY

        numbers = sorted(
            int(str(s.id).rsplit(".", 1)[1]) for s in REGISTRY.all()
            if str(s.id).startswith("3.4."))
        read = [n for n in numbers if n < 79]
        self.assertTrue(read)
        self.assertEqual(read, list(range(1, len(read) + 1)))

    def test_and_the_module_says_why_the_two_are_out_of_order(self):
        import src.astadhyayi.rules.adhyaya_3_pada_4 as module

        self.assertIn("before the reading reached it",
                      module.__doc__ or "")



class ARuleWhoseFormSaysOneThingAndMeansAnother(unittest.TestCase):
    """
    3.4.25 gives an affix meaning 'having made him a thief' — and
    चोरकरणम् आक्रोशसंपादनार्थमेव, न त्वसौ चोरः क्रियते: the making is
    only for the abusing, and nobody is made a thief.
    """

    def test_the_rule_answers_and_the_disclaimer_is_recorded(self):
        answer = ktva_namul(root="kṛ", karman=True, sense="ākrośa")
        self.assertEqual((answer.by, answer.gives),
                         ("3.4.25", "khamuñ"))
        self.assertIn("न त्वसौ चोरः क्रियते", unwrapped(answer.why))

    def test_and_the_sense_is_needed(self):
        self.assertNotEqual(
            ktva_namul(root="kṛ", karman=True).by, "3.4.25")


class OneGroundUsedInOppositeDirections(unittest.TestCase):
    """
    3.4.21 holds समानकर्तृकता BECAUSE
    शक्तिशक्तिमतोर्भेदस्याविवक्षितत्वात्. 3.4.26 says न चास्मिन्
    प्रकरणे शक्तिशक्तिमतोर्भेदो विवक्ष्यते, समानकर्तृकत्वं हि
    विरुध्यते — the distinction is NOT drawn here because drawing it
    would contradict the condition.

    The same ground, five sūtras apart, pointed both ways.
    """

    def test_both_rules_cite_it(self):
        from src.astadhyayi.sutra import REGISTRY

        for sutra in ("3.4.21", "3.4.26"):
            with self.subTest(sutra=sutra):
                self.assertIn("शक्तिशक्तिमतोर्भेदस्",
                              unwrapped(REGISTRY.get(sutra).notes))

    def test_and_3_4_26_says_it_is_the_other_way_round(self):
        from src.astadhyayi.sutra import REGISTRY

        notes = unwrapped(REGISTRY.get("3.4.26").notes)
        # न and विवक्ष्यते are separated by four words in the vṛtti;
        # match the phrase that actually runs together.
        self.assertIn("न चास्मिन् प्रकरणे", notes)
        self.assertIn("विवक्ष्यते", notes)
        self.assertIn("3.4.21", notes)


class AConditionThatARootAddsNothing(unittest.TestCase):
    """
    3.4.27's सिद्धाप्रयोग — निरर्थकत्वाद् न प्रयोगमर्हति. The verb
    'make' contributes no meaning: अन्यथा भुङ्क्त इति यावानर्थः,
    तावानेवान्यथाकारं भुङ्क्त इति गम्यते.

    3.3.154 made a condition of a WORD being meant and not said; this
    makes one of a ROOT adding nothing to what is said. Two conditions
    about absence, and neither is about a form.
    """

    def test_it_is_needed(self):
        self.assertEqual(
            ktva_namul(root="kṛ", beside="anyathā",
                       siddha_aprayoga=True).by, "3.4.27")
        self.assertNotEqual(
            ktva_namul(root="kṛ", beside="anyathā").by, "3.4.27")

    def test_the_counter_example_is_a_real_making(self):
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("अन्यथा कृत्वा शिरो भुङ्क्ते",
                      unwrapped(REGISTRY.get("3.4.27").notes))

    def test_and_the_pair_with_3_3_154_is_recorded(self):
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("3.3.154", unwrapped(REGISTRY.get("3.4.27").notes))
        self.assertIn("सिद्धाप्रयोग",
                      unwrapped(REGISTRY.get("3.3.154").notes))


class AGroupNamedByWhereARunBegins(unittest.TestCase):
    """
    3.4.34's इतः प्रभृति कषादीन् यान् वक्ष्यति — from this rule on the
    roots named form a class called कषादि, after its first member, and
    3.4.46 will govern them all.

    A group defined by where a run BEGINS rather than by a list. Every
    gaṇa met so far was a list, and two of them are on disk.
    """

    def test_the_group_and_the_rule_that_will_govern_it(self):
        from src.astadhyayi.sutra import REGISTRY

        notes = unwrapped(REGISTRY.get("3.4.34").notes)
        self.assertIn("इतः प्रभृति", notes)
        self.assertIn("3.4.46", notes)

    def test_and_that_rule_is_codified_now(self):
        """
        PAID, twelve sūtras after it was recorded — the shortest-lived
        debt so far, where the others spanned whole pādas. The
        mechanism is the same at either length.

        What can be checked now is what 3.4.34 could only assert: that
        the rule governing the class says the SAME root must follow.
        """
        from src.astadhyayi.dhatu_sambandha import anuprayoga
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("3.4.46", {str(s.id) for s in REGISTRY.all()})
        answer = anuprayoga(kashadi=True)
        self.assertEqual(answer.by, "3.4.46")
        self.assertEqual(answer.gives, "the same root")

    def test_and_it_restricts_rather_than_prescribes(self):
        """
        ननु धातुसंबन्धे प्रत्ययविधानादनुप्रयोगः सिद्ध एव? — that
        SOMETHING is said after follows from 3.4.1 already.
        यथाविधीति नियमार्थं वचनम्: the rule is for the restriction.

        Word for word the argument 3.4.4 made about itself
        twenty-two sūtras earlier, and the two rules do the same work
        for two different runs.
        """
        from src.astadhyayi.dhatu_sambandha import anuprayoga
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("नियमार्थं वचनम्",
                      unwrapped(anuprayoga(kashadi=True).why))
        for sutra in ("3.4.4", "3.4.46"):
            with self.subTest(sutra=sutra):
                self.assertIn("सिद्ध एव",
                              unwrapped(REGISTRY.get(sutra).notes))

    def test_and_all_three_anuprayoga_rules_answer_differently(self):
        from src.astadhyayi.dhatu_sambandha import anuprayoga

        answers = {anuprayoga().by,
                   anuprayoga(gathered=True).by,
                   anuprayoga(kashadi=True).by}
        self.assertEqual(answers, {"3.4.4", "3.4.5", "3.4.46"})


class OneWordSpentEntirelyOnScope(unittest.TestCase):
    """
    3.4.32's अस्यग्रहणं किमर्थम्? उपपदस्य मा भूत् — the word अस्य is
    there so the vowel-loss falls on the ROOT and not on the word
    before it.
    """

    def test_it_is_recorded(self):
        from src.astadhyayi.sutra import REGISTRY

        notes = unwrapped(REGISTRY.get("3.4.32").notes)
        self.assertIn("अस्यग्रहणं किमर्थम्", notes)
        self.assertIn("उपपदस्य मा भूत्", notes)

    def test_and_the_rule_is_optional_as_stated(self):
        row = next(r for r in KTVA if r.sutra == "3.4.32")
        self.assertTrue(row.optional)


class ThreeListsBoundCrosswiseAgain(unittest.TestCase):
    """
    3.4.36 binds three companions to three roots. The device 3.2.5
    established, 3.3.37 stretched to three lists at once, and this
    uses in its plain two-list form over three pairs.
    """

    def test_each_bound_pair_answers(self):
        for beside, root in (("samūla", "han"), ("akṛta", "kṛ"),
                             ("jīva", "grah")):
            with self.subTest(beside=beside, root=root):
                self.assertEqual(
                    ktva_namul(beside=beside, root=root,
                               karman=True).by, "3.4.36")

    def test_and_the_lists_may_not_be_crossed(self):
        for beside, root in (("samūla", "kṛ"), ("jīva", "han"),
                             ("akṛta", "grah")):
            with self.subTest(beside=beside, root=root):
                self.assertNotEqual(
                    ktva_namul(beside=beside, root=root,
                               karman=True).by, "3.4.36")

    def test_the_earlier_rules_that_used_the_device_are_named(self):
        from src.astadhyayi.sutra import REGISTRY

        notes = unwrapped(REGISTRY.get("3.4.36").notes)
        self.assertIn("3.2.5", notes)
        self.assertIn("3.3.37", notes)


class TheNamulRunIsExercisedThroughout(unittest.TestCase):
    """
    Every row of the table has a worked case, and every rule
    registered to this entry point has a row. Read from both sides so
    neither can drift.
    """

    def test_every_row_is_reached_by_some_case(self):
        from src.astadhyayi.cases import CURATED

        covered = {sutra for sutra in CURATED
                   if sutra.startswith("3.4.")}
        rows = {r.sutra for r in KTVA}
        self.assertTrue(rows <= covered)

    def test_and_every_registered_rule_has_a_row(self):
        from src.astadhyayi.ktva_namul import ktva_namul as entry
        from src.astadhyayi.sutra import REGISTRY

        registered = {str(x.id) for x in REGISTRY.all()
                      if x.apply is entry}
        self.assertEqual(registered, {r.sutra for r in KTVA})



class TheLakaraDebtIsClosed(unittest.TestCase):
    """
    All three paid. 3.4.6 gave the Vedic set, 3.4.69 said what a लकार
    DENOTES, and 3.4.77 enumerates the ten and says which are टित्.

    What that buys is a check nothing could run before: the लकार table
    spans 3.2.110 to 3.4.8 and has been naming its endings as bare
    strings for two and a half pādas. Every one of them can now be
    tested against the rule that lists them.
    """

    def test_all_three_are_codified(self):
        from src.astadhyayi.sutra import REGISTRY

        have = {str(s.id) for s in REGISTRY.all()}
        for sutra in ("3.4.6", "3.4.69", "3.4.77"):
            with self.subTest(sutra=sutra):
                self.assertIn(sutra, have)

    def test_every_ending_the_table_gives_is_one_of_the_ten(self):
        """
        The payoff. Two and a half pādas of rules named endings as
        strings with nothing to check them against; 3.4.77 supplies
        the list, and the two agree.
        """
        from src.astadhyayi.lakara import LAKARA, LAKARA_LIST

        ten = {name for name, _ in LAKARA_LIST}
        given = {row.gives for row in LAKARA}
        self.assertTrue(given)
        self.assertEqual(given - ten, set())

    def test_and_the_table_really_does_span_three_padas(self):
        """
        Not a count: the property is that the same table answers for
        rules of 3.2, 3.3 and 3.4, which is why one enumeration
        validates all of them.
        """
        from src.astadhyayi.lakara import LAKARA

        padas = {row.sutra.rsplit(".", 1)[0] for row in LAKARA}
        self.assertEqual(padas, {"3.2", "3.3", "3.4"})

    def test_the_ten_are_six_tit_and_four_ngit(self):
        from src.astadhyayi.lakara import LAKARA_LIST

        self.assertEqual(len(LAKARA_LIST), 10)
        marks = [mark for _, mark in LAKARA_LIST]
        self.assertEqual(marks.count("ṭit"), 6)
        self.assertEqual(marks.count("ṅit"), 4)

    def test_and_the_mark_is_not_decoration(self):
        """
        3.4.79, codified long before the reading reached this pāda,
        replaces the टि of an ātmanepada ending after a टित् लकार.
        लट् is टित्, which is why पचते has its ए.
        """
        from src.astadhyayi.anga import tit_atmanepada
        from src.astadhyayi.lakara import LAKARA_LIST

        self.assertEqual(dict(LAKARA_LIST)["laṭ"], "ṭit")
        answer = tit_atmanepada("ta", tit_lakara=True)
        self.assertTrue(getattr(answer, "gives", answer))

    def test_the_eighteen_substitutes_are_eighteen(self):
        from src.astadhyayi.lakara import TIN, lakara_substitutes

        self.assertEqual(len(TIN), 18)
        self.assertEqual(len(set(TIN)), 18)
        self.assertEqual(lakara_substitutes().by, "3.4.78")

    def test_and_the_last_of_them_is_what_names_the_set(self):
        """
        महिङो ङकारस्तिङ् इति प्रत्याहारग्रहणार्थः — the ङ on the last
        substitute is what lets तिङ् be formed, and 3.4.113 stands on
        that name. A rule written early rests on a letter only now
        read.
        """
        from src.astadhyayi.lakara import TIN, lakara_substitutes
        from src.astadhyayi.sutra import REGISTRY

        self.assertEqual(TIN[0], "tip")
        self.assertEqual(TIN[-1], "mahiṅ")
        self.assertIn("प्रत्याहारग्रहणार्थः",
                      unwrapped(lakara_substitutes().why))
        self.assertIn("3.4.113", REGISTRY.get("3.4.78").notes)
        self.assertIn("तिङ", REGISTRY.get("3.4.113").notes)

    def test_a_name_outside_the_ten_is_refused(self):
        from src.astadhyayi.lakara import lakara_heading

        self.assertIsInstance(lakara_heading("lyaṭ"), NotAdded)
        self.assertIsInstance(lakara_heading("laṭ"), Added)


class TheQuestionChangesAtTheEndOfThePada(unittest.TestCase):
    """
    3.4.67 onward ask what an affix DENOTES, where every rule of 3.2,
    3.3 and this pāda so far asked which affix comes.
    """

    def test_the_denoting_rules_answer_for_their_own_examples(self):
        from src.astadhyayi.denoted import denotes

        for sutra, where in (
            ("3.4.67", dict(affix="ṇvul")),
            ("3.4.69", dict(affix="la")),
            ("3.4.70", dict(affix="kṛtya")),
            ("3.4.71", dict(affix="kta", adikarman=True)),
            ("3.4.72", dict(affix="kta", root_sense="gati")),
            ("3.4.76", dict(affix="kta", root_sense="dhrauvya")),
        ):
            with self.subTest(sutra=sutra, **where):
                self.assertEqual(denotes(**where).by, sutra)

    def test_the_gap_filling_heading_stands_down_where_a_sense_was_stated(self):
        """
        तत्र येष्वर्थादेशो नास्ति तत्रेदमुपतिष्ठते — 3.4.67 attaches
        only where the rule giving the affix named no sense. A heading
        that fills gaps rather than covering ground, which 3.2.84,
        3.3.18 and 3.3.19 all did.
        """
        from src.astadhyayi.denoted import denotes

        self.assertEqual(denotes("ṇvul").by, "3.4.67")
        self.assertIsInstance(
            denotes("ṇvul", sense_stated=True), NotAdded)

    def test_and_three_adjacent_rules_adjust_one_another(self):
        """
        3.4.67 supplies the doer; 3.4.70's एव pulls it away for one
        class of affixes; 3.4.68 then lets seven particular words have
        it back.
        """
        from src.astadhyayi.denoted import denotes, nipatana
        from src.astadhyayi.sutra import REGISTRY

        self.assertIn("kartṛ", denotes("ṇvul").gives)
        self.assertNotIn("kartṛ", denotes("kṛtya").gives)
        self.assertEqual(nipatana("geya").gives, "kartṛ")
        self.assertIn("कर्तुरपकर्षणार्थः",
                      unwrapped(REGISTRY.get("3.4.70").notes))

    def test_two_rules_about_one_set_of_words_ask_two_questions(self):
        """
        3.4.75 and 3.3.1 both speak of the उणादि words, and I put them
        on ONE entry point for that reason. They do not ask the same
        thing: 3.3.1 asks whether the word stands and on whose
        authority, 3.4.75 asks what it denotes.

        Sharing the entry point made 3.4.75's worked case come back by
        3.3.2, and the case runner caught it. **Two rules about the
        same words are not thereby the same question** — the reverse
        of the collision that keeps splitting field names, and the
        same guard catches both.
        """
        from src.astadhyayi.sutra import REGISTRY

        self.assertNotEqual(REGISTRY.get("3.4.75").apply.__name__,
                            REGISTRY.get("3.3.1").apply.__name__)
        self.assertEqual(REGISTRY.get("3.4.75").apply.__name__,
                         REGISTRY.get("3.4.69").apply.__name__)

    def test_and_each_answers_its_own_question_about_one_word(self):
        from src.astadhyayi.denoted import denotes
        from src.astadhyayi.unadi import unadi

        stands = unadi("carman", past=True)
        means = denotes(unadi=True)
        self.assertEqual(stands.by, "3.3.2")
        self.assertEqual(means.by, "3.4.75")
        self.assertIn("karman", means.gives)

    def test_and_two_of_its_examples_are_3_3_2s_own(self):
        """
        वर्त्म and चर्म. 3.3.2 said those may be SEEN in the past;
        3.4.75 says what they DENOTE. Two halves of one question, a
        pāda and a half apart, and both codified.
        """
        from src.astadhyayi.sutra import REGISTRY

        for form in ("वर्त्म", "चर्म"):
            with self.subTest(form=form):
                self.assertIn(form, REGISTRY.get("3.3.2").notes)
                self.assertIn(form, REGISTRY.get("3.4.75").notes)


if __name__ == "__main__":
    unittest.main()
