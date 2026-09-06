# -*- coding: utf-8 -*-
"""
३.४.८०–११७ — the endings, and the pāda closes.

3.4.77 named the ten and 3.4.78 gave the eighteen; these rules work on
those eighteen and nothing else. Which makes the whole block testable
against the two enumerations behind it, the way 3.4.77 made the लकार
table testable — and this file spends most of its length doing that.

The last four sūtras close अध्याय ३, and the last of those closes it
by pointing back at 3.1.85.
"""

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi.sutra import REGISTRY
from tests import unwrapped


class ThePadaAndTheAdhyayaAreComplete(unittest.TestCase):
    """
    3.4 is read from its first sūtra to its last, which finishes
    अध्याय ३. Both facts are asserted as PROPERTIES read off the
    corpus, because a count of 117 or of 3,983 goes stale and a
    contiguity does not.
    """

    def _codified_in(self, adhyaya, pada):
        return {s.id.number for s in REGISTRY.all()
                if s.id.adhyaya == adhyaya and s.id.pada == pada}

    def _in_corpus(self, adhyaya, pada):
        from src.astadhyayi.corpus import collate

        return {int(key.rsplit(".", 1)[1]) for key in collate()
                if key.startswith("%d.%d." % (adhyaya, pada))}

    def test_the_fourth_pada_is_read_end_to_end(self):
        self.assertEqual(self._codified_in(3, 4), self._in_corpus(3, 4))

    def test_and_so_is_every_pada_of_the_third_adhyaya(self):
        """
        The whole of अध्याय ३ — every rule that gives an affix after a
        root, from 3.1.1 to the end. Asserted against the corpus so it
        cannot drift from what the text actually contains.
        """
        for pada in (1, 2, 3, 4):
            with self.subTest(pada="3.%d" % pada):
                self.assertEqual(self._codified_in(3, pada),
                                 self._in_corpus(3, pada))

    def test_the_two_rules_codified_out_of_order_are_now_in_it(self):
        """
        3.4.79 and 3.4.113 were written long before the reading reached
        this pāda, because derivations elsewhere stopped without them.
        They are not a separate category any more — the run has passed
        through them, and the reached-ahead list in the asiddha tests
        no longer names them.
        """
        from tests.test_astadhyayi_asiddha import Registration

        for sutra in ("3.4.79", "3.4.113"):
            with self.subTest(sutra=sutra):
                self.assertTrue(REGISTRY.has(sutra))
                self.assertNotIn(sutra, Registration.IDS)


class TheEighteenAreTheOnlyThingTheseRulesTouch(unittest.TestCase):
    """
    The payoff 3.4.78 makes possible, and the counterpart of the one
    3.4.77 made possible for the ten.
    """

    def test_the_two_voices_partition_the_eighteen(self):
        from src.astadhyayi.lakara import TIN
        from src.astadhyayi.tin_adesha import ATMANEPADA, PARASMAIPADA

        self.assertEqual(PARASMAIPADA + ATMANEPADA, TIN)
        self.assertEqual(len(PARASMAIPADA), len(ATMANEPADA))
        self.assertEqual(set(PARASMAIPADA) & set(ATMANEPADA), set())

    def test_every_ending_a_rule_names_is_one_of_them(self):
        """
        A row's `of` is either a whole ending from 3.4.78 or a single
        sound inside one. Nothing else may appear, or a rule would be
        replacing something the grammar never gave.
        """
        from src.astadhyayi.lakara import TIN
        from src.astadhyayi.tin_adesha import TIN_ADESA

        #: The sounds these rules work on WITHIN an ending, and the
        #: two augments a later rule marks.
        WITHIN = {"i", "u", "e", "ā", "s", "hi", "yāsuṭ"}
        named = {item for row in TIN_ADESA for item in row.of}
        self.assertTrue(named)
        self.assertEqual(named - set(TIN) - WITHIN, set())

    def test_the_perfects_nine_line_up_with_the_eighteens_nine(self):
        """
        3.4.82 is a यथासंख्य rule, so the two lists must be the same
        length or the correspondence has nowhere to land.
        """
        from src.astadhyayi.tin_adesha import (
            LIT_PARASMAIPADA, PARASMAIPADA, provisions_for)

        row, = provisions_for("3.4.82")
        self.assertEqual(len(row.of), len(row.gives))
        self.assertEqual(row.of, PARASMAIPADA)
        self.assertEqual(row.gives, LIT_PARASMAIPADA)

    def test_and_one_of_the_nine_is_given_twice(self):
        """
        णल् stands at the third person singular and again at the
        first, so पपाच is both *he cooked* and *I cooked* — nine slots
        and eight shapes. The property is the collapse, not the count.
        """
        from src.astadhyayi.tin_adesha import LIT_PARASMAIPADA, tin_adesha

        self.assertGreater(len(LIT_PARASMAIPADA),
                           len(set(LIT_PARASMAIPADA)))
        third = tin_adesha("tip", lakara="liṭ",
                           ending_pada="parasmaipada")
        first = tin_adesha("mip", lakara="liṭ",
                           ending_pada="parasmaipada")
        self.assertEqual(third.gives, first.gives)
        self.assertEqual(third.by, "3.4.82")

    def test_every_yathasamkhya_row_pairs_off_evenly(self):
        """
        Wherever a row names several endings and several results, the
        two lists are read position for position by 1.3.10. A row where
        they differ in length would give a silently wrong answer rather
        than an error, which is why this is checked over the table
        rather than case by case.
        """
        from src.astadhyayi.tin_adesha import TIN_ADESA

        for row in TIN_ADESA:
            if len(row.of) > 1 and row.gives and row.kind == "ādeśa":
                with self.subTest(sutra=row.sutra):
                    self.assertEqual(len(row.of), len(row.gives))


class TheOptionThatWillNotDie(unittest.TestCase):
    """
    3.4.83's वा is carried by anuvṛtti through five later rules and
    then killed by one syllable at 3.4.99. It is the clearest case in
    the project so far of a word doing work far from where it stands.
    """

    def test_the_same_elision_is_optional_in_one_lakara_and_not_the_next(self):
        """
        The sharpest form of it. 3.4.98 and 3.4.99 drop the SAME sound
        — the स् of the first person — and the only difference is
        which लकार precedes. In the लेट् it is optional because
        3.4.83's वा has been carried down fifteen sūtras; after a
        ङित् it is not, because 3.4.99 says नित्यम्.
        """
        from src.astadhyayi.tin_adesha import tin_adesha

        vedic = tin_adesha("s", lakara="leṭ", person="uttama")
        ordinary = tin_adesha("s", lakara="laṅ", person="uttama")
        self.assertEqual(vedic.by, "3.4.98")
        self.assertEqual(ordinary.by, "3.4.99")
        self.assertEqual(vedic.gives, ordinary.gives)
        self.assertTrue(vedic.optional)
        self.assertFalse(ordinary.optional)

    def test_and_the_word_that_kills_it_says_so(self):
        self.assertIn("नित्यग्रहणं विकल्पनिवृत्त्यर्थम्",
                      unwrapped(REGISTRY.get("3.4.99").notes))
        self.assertIn("3.4.83", REGISTRY.get("3.4.99").notes)

    def test_the_rules_it_reaches_all_point_back_at_it(self):
        """
        An option carried by inference is invisible in the rules it
        reaches, so each of them has to record where it came from or
        the trail is lost.
        """
        for sutra in ("3.4.85", "3.4.86", "3.4.97", "3.4.98"):
            with self.subTest(sutra=sutra):
                self.assertIn("3.4.83", REGISTRY.get(sutra).notes)


class TheAtidesaAndItsBound(unittest.TestCase):
    """
    3.4.85 makes the imperative count as the imperfect. What it does
    NOT carry is fenced twice, twenty-six sūtras apart, by two
    unrelated arguments.
    """

    def test_the_imperative_borrows_the_imperfect(self):
        from src.astadhyayi.tin_adesha import behaves_as

        answer = behaves_as("loṭ")
        self.assertEqual(answer.gives, "laṅ")
        self.assertEqual(answer.by, "3.4.85")
        self.assertEqual(answer.kind, "atideśa")

    def test_but_no_other_lakara_does(self):
        from src.astadhyayi.tin_adesha import NotSubstituted, behaves_as

        self.assertIsInstance(behaves_as("laṭ"), NotSubstituted)

    def test_and_the_borrowed_jus_does_not_come(self):
        """
        The functional half. यान्तु and वान्तु are imperatives after a
        long आ, exactly the ground 3.4.111 states — and they keep
        their own ending, because a लोट् behaving as a लङ् is not a
        लङ्. Nothing in the table has to say so: 3.4.111 names the
        लङ् and 3.4.109 holds to ङित्, and the imperative is neither.
        """
        from src.astadhyayi.tin_adesha import NotSubstituted, tin_adesha

        borrowed = tin_adesha("jhi", lakara="loṭ", preceded_by="ā")
        real = tin_adesha("jhi", lakara="laṅ", preceded_by="ā")
        self.assertIsInstance(borrowed, NotSubstituted)
        self.assertEqual(real.gives, "jus")
        self.assertEqual(real.by, "3.4.111")

    def test_and_both_rules_record_the_fence(self):
        self.assertIn("अडाटौ कस्माद् न भवतः",
                      unwrapped(REGISTRY.get("3.4.85").notes))
        self.assertIn("लङ्वद्भावेन यस्तस्य मा भूत्",
                      unwrapped(REGISTRY.get("3.4.111").notes))


class AWordSpentInAnotherRule(unittest.TestCase):
    """
    3.4.111's एवकार उत्तरार्थः — the एव in शाकटायनस्यैव does nothing
    where it stands and is collected four sūtras later, where it makes
    a name REPLACE another instead of joining it.

    Both ends of the transaction are stated in the commentary, which is
    what makes it checkable rather than a guess.
    """

    def test_the_lender_says_the_word_is_for_later(self):
        notes = unwrapped(REGISTRY.get("3.4.111").notes)
        self.assertIn("एवकार उत्तरार्थः", notes)
        self.assertIn("3.4.115", notes)

    def test_the_borrower_says_where_it_came_from(self):
        notes = unwrapped(REGISTRY.get("3.4.115").notes)
        self.assertIn("त्वेवकारोऽनुवर्तते", notes)
        self.assertIn("3.4.111", notes)

    def test_and_one_sutra_further_it_is_still_working(self):
        self.assertIn("चैवकारानुवृत्तेर्न भवति",
                      unwrapped(REGISTRY.get("3.4.116").notes))


class TheRemainderAsksTheRuleItIsTheRemainderOf(unittest.TestCase):
    """
    3.4.114 आर्धधातुकं शेषः. The plainest reuse edge in the project:
    the rule is defined by subtraction and there is exactly one thing
    it subtracts from.
    """

    def test_an_affix_3_4_113_names_is_refused_here(self):
        from src.astadhyayi.anga import ardhadhatuka, sarvadhatuka

        for kind in (dict(tin=True), dict(sit=True)):
            with self.subTest(**kind):
                self.assertTrue(sarvadhatuka(**kind).holds)
                self.assertFalse(ardhadhatuka(**kind).holds)

    def test_and_the_refusal_carries_3_4_113_s_own_words(self):
        """
        Not merely the same verdict — the same REASON. If the code
        re-tested तिङ् and शित् for itself the two could drift apart;
        because the answer is passed through, they cannot.
        """
        from src.astadhyayi.anga import ardhadhatuka, sarvadhatuka

        named = sarvadhatuka(tin=True)
        remainder = ardhadhatuka(tin=True)
        self.assertIn(named.why, remainder.why)

    def test_anything_else_after_a_root_takes_the_name(self):
        from src.astadhyayi.anga import ardhadhatuka

        answer = ardhadhatuka()
        self.assertTrue(answer.holds)
        self.assertEqual(answer.by, "3.4.114")

    def test_but_not_an_affix_that_is_not_after_a_root(self):
        from src.astadhyayi.anga import ardhadhatuka

        answer = ardhadhatuka(after_a_root=False)
        self.assertFalse(answer.holds)
        self.assertIn("धातोरित्येव", answer.why)

    def test_the_reuse_is_declared_and_not_only_performed(self):
        for sutra in ("3.4.114", "3.4.115", "3.4.116", "3.4.117"):
            with self.subTest(sutra=sutra):
                self.assertIn("3.4.113", REGISTRY.get(sutra).reuses)


class TwoNamesForOneAffix(unittest.TestCase):
    """
    3.4.115 and 3.4.116 give आर्धधातुक to things 3.4.113 has already
    called सार्वधातुक, and 3.4.117 lets both hold at once.
    """

    def test_the_perfect_takes_the_second_name_though_it_is_a_tin(self):
        from src.astadhyayi.anga import ardhadhatuka, sarvadhatuka

        self.assertTrue(sarvadhatuka(tin=True).holds)
        answer = ardhadhatuka(tin=True, lakara="liṭ")
        self.assertTrue(answer.holds)
        self.assertEqual(answer.by, "3.4.115")

    def test_and_so_does_a_benedictive_but_only_as_a_benediction(self):
        from src.astadhyayi.anga import ardhadhatuka

        blessing = ardhadhatuka(tin=True, lakara="liṅ", sense="āśis")
        plain = ardhadhatuka(tin=True, lakara="liṅ")
        self.assertEqual(blessing.by, "3.4.116")
        self.assertTrue(blessing.holds)
        self.assertFalse(plain.holds)

    def test_in_the_veda_both_names_hold_together(self):
        from src.astadhyayi.anga import ardhadhatuka

        answer = ardhadhatuka(tin=True, chandasi=True)
        self.assertTrue(answer.holds)
        self.assertEqual(answer.by, "3.4.117")

    def test_and_that_rule_reaches_the_whole_section_not_its_neighbour(self):
        notes = unwrapped(REGISTRY.get("3.4.117").notes)
        self.assertIn("सर्वमेव प्रकरणमपेक्ष्य", notes)
        self.assertIn("व्यत्ययो बहुलम्", notes)


class WhatTheRulesKeepOut(unittest.TestCase):
    """
    Six rules of this run spend a word on saying where they do NOT
    reach. Each is recorded with the form that would otherwise go
    wrong, and each of those words has to be in the rule's own notes
    or the record is unattached.
    """

    def test_each_word_is_in_the_rule_that_spends_it(self):
        from src.astadhyayi.tin_adesha import KEEPS_OUT

        for sutra, (word, _) in KEEPS_OUT.items():
            with self.subTest(sutra=sutra, word=word):
                self.assertTrue(REGISTRY.has(sutra))
                self.assertIn(word, unwrapped(REGISTRY.get(sutra).notes))

    def test_the_count_of_five_really_leaves_the_sixth_alone(self):
        """
        3.4.84's पञ्चानाम्. आत्थ is the fifth and comes by the rule;
        ब्रूथ is the sixth and no rule of this run touches it, so the
        paradigm has one form of a different shape in the middle of it.
        """
        from src.astadhyayi.tin_adesha import NotSubstituted, tin_adesha

        fifth = tin_adesha("thas", lakara="laṭ", root="brū",
                           ending_pada="parasmaipada")
        sixth = tin_adesha("tha", lakara="laṭ", root="brū",
                           ending_pada="parasmaipada")
        self.assertEqual(fifth.by, "3.4.84")
        self.assertIsInstance(sixth, NotSubstituted)

    def test_and_the_root_is_replaced_in_the_same_act(self):
        from src.astadhyayi.tin_adesha import tin_adesha

        answer = tin_adesha("tip", lakara="laṭ", root="brū",
                            ending_pada="parasmaipada")
        self.assertEqual(answer.along_with, "āh")

    def test_the_veda_only_rule_does_not_reach_ordinary_speech(self):
        """
        3.4.88 is stated छन्दसि. A rule given for the Veda does not
        reach elsewhere, and one given without it reaches both — which
        is why `chandasi` is a condition on the row and not a default.
        """
        from src.astadhyayi.tin_adesha import NotSubstituted, tin_adesha

        vedic = tin_adesha("hi", lakara="loṭ", chandasi=True)
        self.assertEqual(vedic.by, "3.4.88")
        self.assertIsInstance(tin_adesha("hi", lakara="loṭ"),
                              NotSubstituted)


class TheApavadaRelation(unittest.TestCase):
    """
    Where the vṛtti itself says अपवादः, the excepted rule is named.
    Held as a relation between rules, and tested as one.
    """

    def test_every_excepted_rule_could_otherwise_have_reached(self):
        """
        An exception to a rule that could not apply anyway is not an
        exception. Each entry names a rule that is either codified in
        this run or lies ahead of it — 7.1.3 झोऽन्तः, which two rules
        here get in front of.
        """
        from src.astadhyayi.tin_adesha import EXCEPTS

        for sutra, excepted in EXCEPTS.items():
            with self.subTest(sutra=sutra):
                self.assertTrue(REGISTRY.has(sutra))
                self.assertTrue(excepted)
                for other in excepted:
                    self.assertNotEqual(other, sutra)

    def test_the_answer_carries_what_it_excepted(self):
        from src.astadhyayi.tin_adesha import tin_adesha

        answer = tin_adesha("mip", lakara="loṭ")
        self.assertEqual(answer.by, "3.4.89")
        self.assertIn("3.4.86", answer.excepts)

    def test_and_the_rule_it_excepts_still_answers_its_own_ground(self):
        """
        उत्वलोपयोरपवादः takes 3.4.86 off ONE ending, not off the
        letter. पचतु still comes by 3.4.86.
        """
        from src.astadhyayi.tin_adesha import tin_adesha

        self.assertEqual(tin_adesha("i", lakara="loṭ").by, "3.4.86")

    def test_two_augments_on_different_grounds_do_not_compete(self):
        """
        3.4.107's argument, and the reason `kind` is a field.
        सीयुट् attaches to the लिङ्; सुट् attaches to the ending, with
        लिङ् only qualifying it. भिन्नविषयत्वात् सुटा बाधनं न भवति —
        so both stand, and neither is recorded as excepting the other.
        """
        from src.astadhyayi.tin_adesha import EXCEPTS, tin_adesha

        whole = tin_adesha(lakara="liṅ", wants="āgama")
        one_ending = tin_adesha("ta", lakara="liṅ", wants="āgama")
        self.assertEqual(whole.by, "3.4.102")
        self.assertEqual(one_ending.by, "3.4.107")
        self.assertNotIn("3.4.107", EXCEPTS.get("3.4.102", ()))
        self.assertNotIn("3.4.102", EXCEPTS.get("3.4.107", ()))


class NoRuleWinsByTableOrder(unittest.TestCase):
    """
    The resolver takes the most specific matching row. Where two rows
    tie, `max` returns whichever came first in the table — which is
    not a decision, and cost 3.4.93 its own worked case once.

    So the guard is not on that one case but on all of them: for every
    curated input in the project that reaches this run, exactly one row
    may hold the top rank.
    """

    def test_every_worked_input_has_a_single_most_specific_rule(self):
        from src.astadhyayi.cases import cases_for
        from src.astadhyayi.tin_adesha import (
            TIN_ADESA, _how_specific, _reaches)

        checked = 0
        for sutra in REGISTRY.all():
            sutra_id = str(sutra.id)
            if getattr(sutra.apply, "__name__", "") != "tin_adesha":
                continue
            for case in cases_for(sutra_id):
                values = dict(case.values)
                matched = [
                    row for row in TIN_ADESA
                    if _reaches(row, values.get("of", ""),
                                values.get("lakara", ""),
                                values.get("ending_pada", ""),
                                values.get("person", ""),
                                values.get("root", ""),
                                values.get("preceded_by", ""),
                                values.get("chandasi", False),
                                values.get("sense", ""))
                    and (not values.get("wants")
                         or row.kind == values["wants"])
                ]
                top = max(_how_specific(row) for row in matched)
                winners = [row.sutra for row in matched
                           if _how_specific(row) == top]
                checked += 1
                with self.subTest(sutra=sutra_id, case=case.label):
                    self.assertEqual(winners, [sutra_id])
        self.assertGreater(checked, 20)


class TheTwoRenamedFields(unittest.TestCase):
    """
    A scar, guarded. The voice of an ending is पद and what a rule
    wants in front is naturally 'after' — and both names were already
    taken in this codebase for different questions. Overloading either
    would have produced a silently wrong answer, not an error.
    """

    def test_the_run_does_not_reuse_either_taken_name(self):
        import inspect

        from src.astadhyayi.tin_adesha import tin_adesha

        names = set(inspect.signature(tin_adesha).parameters)
        self.assertIn("ending_pada", names)
        self.assertIn("preceded_by", names)
        self.assertNotIn("pada", names)
        self.assertNotIn("after", names)

    def test_and_the_taken_names_still_mean_what_they_meant(self):
        from src.astadhyayi.fieldhelp import HELP

        self.assertIn("finished word", HELP["pada"].label
                      + " " + HELP["pada"].hint)
        self.assertIn("after", HELP["after"].label)

    def test_both_new_names_are_explained_to_a_reader(self):
        from src.astadhyayi.fieldhelp import HELP

        for name in ("ending_pada", "person", "preceded_by",
                     "after_a_root"):
            with self.subTest(field=name):
                self.assertIn(name, HELP)
                self.assertTrue(HELP[name].label.strip())
                self.assertTrue(HELP[name].hint.strip())


class TheJnapakaAt3_4_103(unittest.TestCase):
    """
    यासुट् is said to be ङित् though it is ङित् already. A rule that
    says too much, and what it teaches is read off the excess.
    """

    def test_the_augment_carries_both_stated_properties(self):
        from src.astadhyayi.tin_adesha import tin_adesha

        answer = tin_adesha(lakara="liṅ", ending_pada="parasmaipada",
                            wants="āgama")
        self.assertEqual(answer.by, "3.4.103")
        self.assertEqual(answer.gives, "yāsuṭ")
        self.assertEqual(set(answer.confers), {"udātta", "ṅit"})

    def test_and_the_note_records_what_the_redundancy_teaches(self):
        notes = unwrapped(REGISTRY.get("3.4.103").notes)
        self.assertIn("ज्ञापनार्थम्", notes)
        self.assertIn("लकाराश्रयङित्त्वमादेशानां न भवति", notes)
        self.assertIn("अचिनवम्", notes)

    def test_the_benediction_changes_the_mark_and_only_then(self):
        from src.astadhyayi.tin_adesha import tin_adesha

        blessing = tin_adesha("yāsuṭ", lakara="liṅ", sense="āśis")
        self.assertEqual(blessing.by, "3.4.104")
        self.assertIn("kit", blessing.confers)
        self.assertNotIn("ṅit", blessing.confers)


class TheAccentsAndMarksThatAreNeverHeard(unittest.TestCase):
    """
    This run is full of letters that do no work in the word. Each one
    the vṛtti explains is recorded with its purpose, because a letter
    without a stated purpose is the thing a reader will trip on.
    """

    def test_each_explained_letter_names_the_job_it_does(self):
        for sutra, phrase in (
            ("3.4.81", "शकारः सर्वादेशार्थः"),
            ("3.4.82", "णकारो वृद्ध्यर्थः"),
            ("3.4.102", "टकारो देशविध्यर्थः"),
            ("3.4.106", "मुखसुखार्थ उच्चार्यते"),
            ("3.4.110", "तकारो मुखसुखार्थः"),
        ):
            with self.subTest(sutra=sutra):
                self.assertIn(phrase,
                              unwrapped(REGISTRY.get(sutra).notes))

    def test_and_3_4_78s_three_marks_are_all_now_collected(self):
        """
        3.4.78 gave three marks and said what each was for. All three
        have now been used by a rule of this pāda: the प् for the
        accent, the ट् so that 3.4.106 could pick इट् out, and the ङ्
        so that तिङ् could be named at all — which is what 3.4.113,
        3.4.114 and 3.4.115 stand on.
        """
        from src.astadhyayi.lakara import lakara_substitutes

        why = unwrapped(lakara_substitutes().why)
        self.assertIn("इटोऽत् इति विशेषणार्थः", why)
        self.assertIn("प्रत्याहारग्रहणार्थः", why)
        self.assertEqual(tin_of("3.4.106"), "iṭ")

    def test_the_paribhasa_tells_two_things_of_one_name_apart(self):
        """
        3.4.106's इट् is the ENDING, not the augment of the same name.
        अर्थवद्ग्रहणे नानर्थकस्य — a term names what has meaning. The
        same hazard that keeps splitting field names in this codebase,
        met in the grammar itself and settled by a paribhāṣā.
        """
        notes = unwrapped(REGISTRY.get("3.4.106").notes)
        self.assertIn("अर्थवद्ग्रहणे नानर्थकस्य", notes)
        self.assertIn("आगमस्येटो ग्रहणं न भवति", notes)


def tin_of(sutra_id):
    """The single ending a row of this run names, for a one-line check."""
    from src.astadhyayi.tin_adesha import provisions_for

    row, = provisions_for(sutra_id)
    item, = row.of
    return item


class TheNamedTeacher(unittest.TestCase):
    """
    3.4.111 and 3.4.112 cite an आचार्य by name. The pāda has already
    cited two schools; this is one man, and both alternatives stand.
    """

    def test_both_rules_name_him(self):
        from src.astadhyayi.tin_adesha import provisions_for

        for sutra in ("3.4.111", "3.4.112"):
            with self.subTest(sutra=sutra):
                row, = provisions_for(sutra)
                self.assertEqual(row.authority, "śākaṭāyana")
                self.assertTrue(row.optional)

    def test_and_the_other_view_is_recorded_beside_his(self):
        for sutra in ("3.4.111", "3.4.112"):
            with self.subTest(sutra=sutra):
                self.assertIn("अन्येषां मते",
                              unwrapped(REGISTRY.get(sutra).notes))

    def test_the_pada_attributes_to_two_schools_and_one_person(self):
        """
        प्राचाम् and उदीचाम् at 3.4.18 and 3.4.19 are bodies of
        grammarians; शाकटायन is a man. Three attributions, and the
        distinction is worth keeping because the two kinds are read
        differently: naming a school was itself read as making the
        rule optional, and naming him is not — the option here is
        stated in the disagreement, not in the citation.
        """
        from src.astadhyayi.ktva_namul import attributed_schools

        schools = dict(attributed_schools())
        self.assertEqual(set(schools), {"3.4.18", "3.4.19"})
        for sutra in schools:
            self.assertNotIn("शाकटायन", REGISTRY.get(sutra).notes)


if __name__ == "__main__":
    unittest.main()
