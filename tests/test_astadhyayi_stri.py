# -*- coding: utf-8 -*-
"""
४.१.१–३८ — the nominal base, the case-endings, and the feminine.

अध्याय ३ gave every affix that comes after a ROOT and closed by
enumerating the eighteen verbal endings. **अध्याय ४ opens by doing the
same work for nouns**, and the parallel is exact enough to test:
one heading naming what everything attaches to, one enumeration of the
endings, and silent letters in that enumeration cutting names out of
it.

Then 4.1.3 opens the feminine affixes, which are the first run in this
project where a rule as often refuses as gives.
"""

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi.sutra import REGISTRY
from tests import unwrapped


class TheNominalCounterpartOfTheVerbalOne(unittest.TestCase):
    """
    4.1.2 against 3.4.78. Both enumerate the endings of their half of
    the grammar, and both make names out of letters that are never
    spoken — which is a claim about the two rules that can be checked
    rather than admired.
    """

    def test_both_rules_enumerate_and_both_are_codified(self):
        from src.astadhyayi.lakara import TIN
        from src.astadhyayi.sup import SUP

        self.assertTrue(REGISTRY.has("3.4.78"))
        self.assertTrue(REGISTRY.has("4.1.2"))
        self.assertTrue(TIN)
        self.assertTrue(SUP)

    def test_the_verbal_list_is_three_by_three_by_two(self):
        from src.astadhyayi.lakara import TIN

        self.assertEqual(len(TIN), 3 * 3 * 2)

    def test_and_the_nominal_list_is_three_by_seven(self):
        """
        Not a census — the SHAPE. 4.1.2 is three numbers in each of
        seven cases and 3.4.78 is three persons by three numbers in
        each of two voices, and each list's length is the product of
        what the grammar says it is made of.
        """
        from src.astadhyayi.sup import SUP

        self.assertEqual(len(SUP), 3 * 7)

    def test_each_rule_makes_a_name_from_a_silent_letter(self):
        from src.astadhyayi.lakara import lakara_substitutes
        from src.astadhyayi.sup import sup_endings

        verbal = unwrapped(lakara_substitutes().why)
        nominal = unwrapped(sup_endings().why)
        self.assertIn("प्रत्याहारग्रहणार्थः", verbal)
        self.assertIn("प्रत्याहारग्रहणार्थः", nominal)

    def test_but_the_nominal_one_makes_two(self):
        """
        3.4.78 spent the last letter of its last member on तिङ्.
        4.1.2 spends two letters on two names: सुट्, the first five,
        and सुप्, the whole. And the slice is not arbitrary — the
        rules about a strong stem turn on exactly those five.
        """
        from src.astadhyayi.sup import SUP, SUT, sup_endings

        whole = sup_endings()
        five = sup_endings(name="suṭ")
        self.assertEqual(whole.gives, SUP)
        self.assertEqual(five.gives, SUT)
        self.assertEqual(five.gives, SUP[:5])
        self.assertEqual(whole.name, "sup")
        self.assertEqual(five.name, "suṭ")

    def test_a_name_the_rule_does_not_make_is_refused(self):
        from src.astadhyayi.sup import sup_endings

        answer = sup_endings(name="tiṅ")
        self.assertEqual(answer.gives, ())
        self.assertIn("सुट्", answer.why)

    def test_the_senses_come_from_elsewhere_and_the_note_says_where(self):
        """
        संख्याकर्मादयश्च स्वादीनामर्थाः शास्त्रान्तरेण विहिताः, तेन
        सहास्यैकवाक्यता — the reverse of the कृत् affixes, each of
        which was given IN a sense.
        """
        notes = unwrapped(REGISTRY.get("4.1.2").notes)
        self.assertIn("शास्त्रान्तरेण विहिताः", notes)
        self.assertIn("3.4.67", notes)


class TheLongestHeadingInTheProject(unittest.TestCase):
    """
    4.1.1 governs to the end of अध्याय ५. Every heading met so far
    covered part of a pāda or filled gaps in one.
    """

    def test_it_names_the_sutra_it_runs_to(self):
        from src.astadhyayi.sup import nominal_base

        answer = nominal_base()
        self.assertEqual(answer.by, "4.1.1")
        self.assertEqual(answer.through, "5.4.160")

    def test_and_that_sutra_is_the_last_of_adhyaya_5(self):
        """
        आ पञ्चमाध्यायपरिसमाप्तेः is checked against the text on disk,
        not against a number I typed: the sūtra the heading runs to
        must really be the last one the corpus has for 5.4.
        """
        from src.astadhyayi.corpus import collate
        from src.astadhyayi.sup import nominal_base

        last = max(int(key.rsplit(".", 1)[1]) for key in collate()
                   if key.startswith("5.4."))
        self.assertEqual(nominal_base().through, "5.4.%d" % last)

    def test_it_covers_three_things_two_of_which_are_class_words(self):
        from src.astadhyayi.sup import AP, NGI, nominal_base

        covered = set(nominal_base().covers)
        self.assertIn("prātipadika", covered)
        self.assertEqual(covered - {"prātipadika"}, set(NGI) | set(AP))
        self.assertEqual(len(NGI), 3)
        self.assertEqual(len(AP), 3)

    def test_and_the_run_below_it_takes_its_affixes_from_it(self):
        """
        The reuse. STRI is 4.1.1's two class-words plus the two
        affixes that stand outside both — read off the heading rather
        than typed again, so the section's inventory comes from the
        rule that governs it.
        """
        from src.astadhyayi.stri import STRI
        from src.astadhyayi.sup import AP, NGI

        self.assertEqual(set(NGI) | set(AP), set(STRI) - {"ūṅ", "ṣpha"})

    def test_every_affix_the_table_gives_comes_from_a_named_set(self):
        """
        The payoff, and the same shape as the check 3.4.77 bought for
        the ten लकाराः: a whole run of rules naming affixes as bare
        strings, tested against the lists they are supposed to come
        from.

        There are TWO lists, because the feminine is marked under two
        headings. 4.1.3's section gives eight; 4.1.77 to 4.1.81 give
        two more from under 4.1.76 तद्धिताः, and 4.1.77's vṛtti says
        so outright — स च तद्धितसंज्ञो भवति. Merging them would have
        hidden exactly that.
        """
        from src.astadhyayi.stri import STRI, STRI_TABLE, STRI_TADDHITA

        given = {row.gives for row in STRI_TABLE if row.gives}
        self.assertTrue(given)
        self.assertEqual(given - set(STRI) - set(STRI_TADDHITA), set())
        self.assertEqual(set(STRI) & set(STRI_TADDHITA), set())

    def test_and_the_two_headings_are_both_codified(self):
        for heading in ("4.1.3", "4.1.76"):
            with self.subTest(heading=heading):
                self.assertTrue(REGISTRY.has(heading))

    def test_the_reuse_is_declared_and_is_a_call(self):
        """
        4.1.3 declares 4.1.1 and EARNS it: `stri_heading` asks that
        rule what it governs and subtracts what this section gives.

        4.1.4 declared the same edge and did not earn it — the module
        builds STRI from 4.1.1's class-words at import, but no call
        from `stri_affix` asks 4.1.1 anything. A dependency of the
        file is not a dependency of the rule, and the reuse guard is
        what told them apart.
        """
        self.assertIn("4.1.1", REGISTRY.get("4.1.3").reuses)
        self.assertNotIn("4.1.1", REGISTRY.get("4.1.4").reuses)

    def test_and_the_heading_works_its_own_answer_out(self):
        """
        The proof that it is a call: what 4.1.3 says it takes is
        exactly what 4.1.1 governs less what this section produces.
        Restated in prose the two could drift; computed they cannot.
        """
        from src.astadhyayi.stri import STRI, stri_heading
        from src.astadhyayi.sup import nominal_base

        governed = set(nominal_base().covers)
        self.assertEqual(stri_heading().gives,
                         ", ".join(sorted(governed - set(STRI))))
        self.assertEqual(stri_heading().gives, "prātipadika")

    def test_and_it_subtracts_the_section_not_the_codified_part(self):
        """
        The first version of this subtracted what the TABLE gives, and
        while 4.1.73 to 4.1.75 were still ahead it answered that this
        section may take चाप् and ङीन् as input — the exact opposite of
        true, because those are two of the things it produces. A
        section is defined by what it is for, not by how much of it
        has been read.
        """
        from src.astadhyayi.stri import stri_heading

        for affix in ("cāp", "ṅīn", "ṭāp", "ṅīp"):
            with self.subTest(affix=affix):
                self.assertNotIn(affix, stri_heading().gives)


class AHeadingThatTakesPartOfTheHeadingAboveIt(unittest.TestCase):
    """
    4.1.3 स्त्रियाम् stands under 4.1.1, and can use only one of the
    three things that rule names — because this is the section where
    the other two are made.
    """

    def test_the_reason_is_on_record_in_the_vrttis_words(self):
        notes = unwrapped(REGISTRY.get("4.1.3").notes)
        self.assertIn("ङ्यापोरनेनैव विधानात्", notes)
        self.assertIn("प्रातिपदिकमात्रम्", notes)

    def test_and_the_run_really_does_produce_them(self):
        """
        Not a claim about the commentary — a claim about the code. If
        this section makes the ङी and आप् affixes, they have to be in
        what its table gives; if they were only conditions, the
        argument would be empty.

        PAID. चाप् and ङीन् were owed while 4.1.73 and 4.1.74 were
        still ahead, and the debt was written as the exact shortfall
        so that it would fail the moment they arrived — which it did.
        All six are given now, and so are ऊङ् and ष्फ, which stand
        outside both class-words.
        """
        from src.astadhyayi.stri import STRI, STRI_TABLE
        from src.astadhyayi.sup import AP, NGI

        given = {row.gives for row in STRI_TABLE if row.gives}
        self.assertEqual((set(NGI) | set(AP)) - given, set())
        self.assertEqual(set(STRI) - given, set())

    def test_what_the_heading_means_is_left_open_twice(self):
        from src.astadhyayi.stri import stri_heading

        why = unwrapped(stri_heading().why)
        self.assertIn("केयं स्त्री नाम", why)
        self.assertIn("चेत्युभयथापि युज्यते", why)


class ARunThatRefusesAsOftenAsItGives(unittest.TestCase):
    """
    4.1.10, 4.1.11, 4.1.12, 4.1.22, 4.1.23 and 4.1.24 all say NO.
    They are not one shape, and the difference is worth holding.
    """

    def test_one_rule_refuses_the_whole_section_and_the_rest_name_an_affix(self):
        """
        4.1.10's यो यतः प्राप्नोति स सर्वः प्रतिषिध्यते is the only
        blanket refusal in the run, and it is the only row that names
        no affix. Every other refusal names what it refuses, because
        there is a supplier to hand the answer back to.
        """
        from src.astadhyayi.stri import STRI_TABLE

        blanket = {row.sutra for row in STRI_TABLE
                   if row.refuses and not row.gives}
        named = {row.sutra for row in STRI_TABLE
                 if row.refuses and row.gives}
        self.assertEqual(blanket, {"4.1.10"})
        self.assertTrue(named)
        self.assertNotIn("4.1.10", named)

    def test_the_blanket_refusal_answers_by_itself(self):
        from src.astadhyayi.stri import NotAdded, stri_affix

        answer = stri_affix(samjna="ṣaṭ")
        self.assertIsInstance(answer, NotAdded)
        self.assertEqual(answer.by, "4.1.10")
        self.assertFalse(answer.gives)

    def test_a_named_refusal_answers_by_the_rule_that_supplies(self):
        """
        The standing decision: a rule which excepts a stem by name
        does not thereby govern it. 4.1.11 refuses what 4.1.5 gives,
        so the answer comes back BY 4.1.5 with 4.1.11 on blocked_by.

        The question has to name the affix, because BOTH things are
        true of a मन्-final stem: ङीप् is refused, and 4.1.13's डाप्
        optionally comes. Asked without `wants`, the most specific
        rule that GIVES answers, and that is the right answer to the
        question that was asked.
        """
        from src.astadhyayi.stri import stri_affix

        answer = stri_affix(stem_final="man", wants="ṅīp")
        self.assertEqual(answer.by, "4.1.5")
        self.assertEqual(answer.blocked_by, "4.1.11")
        self.assertFalse(answer.gives)

    def test_and_asked_without_one_the_other_rule_answers(self):
        from src.astadhyayi.stri import stri_affix

        answer = stri_affix(stem_final="man")
        self.assertEqual(answer.by, "4.1.13")
        self.assertEqual(answer.gives, "ḍāp")
        self.assertTrue(answer.optional)

    def test_and_the_rule_it_refuses_still_answers_its_own_ground(self):
        from src.astadhyayi.stri import stri_affix

        self.assertEqual(stri_affix(stem_final="n").gives, "ṅīp")
        self.assertEqual(stri_affix(stem_final="n").by, "4.1.5")


class AStemInManIsAStemInN(unittest.TestCase):
    """
    4.1.11 exists because मन् is a case of न् — otherwise there would
    be nothing for it to refuse. The relation is DECLARED, not read
    off the spelling, because `stem_final` holds two kinds of value.
    """

    def test_every_declared_containment_names_a_final_some_rule_states(self):
        """
        A containment to a final no rule mentions would be dead
        weight, and one FROM a final no rule mentions would be a
        guess. Both halves must be in the table.
        """
        from src.astadhyayi.stri import STRI_TABLE, WITHIN

        stated = {row.stem_final for row in STRI_TABLE if row.stem_final}
        for narrow, wider in WITHIN.items():
            with self.subTest(final=narrow):
                self.assertIn(narrow, stated)
                for one in wider:
                    self.assertIn(one, stated)

    def test_the_narrower_rule_wins_where_both_reach(self):
        from src.astadhyayi.stri import stri_affix

        self.assertEqual(stri_affix(stem_final="van").by, "4.1.7")
        self.assertEqual(stri_affix(stem_final="n").by, "4.1.5")

    def test_and_a_final_member_is_not_read_as_a_sound(self):
        """
        The reason the relation is declared. पाद ends in द्, not in
        अ, and a suffix-match on the spelling would have made 4.1.4
        reach it. That is this codebase's recurring one-name-two-
        questions fault, met INSIDE a single field.
        """
        from src.astadhyayi.stri import WITHIN, stri_affix

        self.assertNotIn("pāda", WITHIN)
        self.assertEqual(stri_affix(stem_final="pāda").by, "4.1.8")


class WordsThatDoWorkFarFromWhereTheyStand(unittest.TestCase):
    """
    Three in this short run, and each is stated by the vṛtti rather
    than inferred — which is what makes them checkable.
    """

    def test_an_option_stated_for_a_rule_six_sutras_back(self):
        """
        4.1.13's अन्यतरस्याम् is there so that 4.1.7's र becomes
        optional in a bahuvrīhi: बहुधीवा beside बहुधीवरी. The mirror
        of 3.4.111's एवकार उत्तरार्थः, running the other way.
        """
        notes = unwrapped(REGISTRY.get("4.1.13").notes)
        self.assertIn("अन्यतरस्यांग्रहणं किमर्थम्", notes)
        self.assertIn("4.1.7", notes)

    def test_a_word_pulled_backward_out_of_its_own_rule(self):
        """
        4.1.18's सर्वत्र is read DOWN into 4.1.17 —
        उत्तरसूत्रादिहापकृष्यते — so the eastern teachers' ष्फ may
        beat a rule fifty-seven sūtras later. Anuvṛtti normally runs
        forward.
        """
        notes = unwrapped(REGISTRY.get("4.1.18").notes)
        self.assertIn("उत्तरसूत्रादिहापकृष्यते", notes)
        self.assertIn("4.1.17", notes)
        self.assertIn("4.1.75", notes)

    def test_and_half_a_condition_carrying_down(self):
        """
        4.1.26 states a numeral OR an indeclinable; 4.1.27 takes only
        the numeral. संख्याग्रहणमनुवर्तते, नाव्ययग्रहणम् — anuvṛtti
        is usually all-or-nothing from a given rule, and here one word
        of two runs on.
        """
        from src.astadhyayi.stri import provisions_for

        notes = unwrapped(REGISTRY.get("4.1.27").notes)
        self.assertIn("नाव्ययग्रहणम्", notes)
        wider, = {row.of_samjna for row in provisions_for("4.1.26")}
        narrower = {row.of_samjna for row in provisions_for("4.1.27")}
        self.assertEqual(wider, "saṃkhyā-avyaya-ādi")
        self.assertEqual(narrower, {"saṃkhyā-ādi"})

    def test_a_rule_whose_whole_content_is_not_the_affix_it_names(self):
        """
        4.1.7 names ङीप्, which 4.1.5 had already given to any
        न्-final stem. तत्सन्नियोगेन रेफविधानार्थं वचनम् — the affix
        is named only because it and the र must come together. The
        same shape as 3.4.84, where the endings and आह् were one act.
        """
        from src.astadhyayi.stri import stri_affix

        answer = stri_affix(stem_final="van")
        self.assertEqual(answer.gives, "ṅīp")
        self.assertEqual(answer.along_with, "r")
        self.assertEqual(stri_affix(stem_final="n").along_with, "")
        self.assertIn("3.4.84", REGISTRY.get("4.1.7").notes)


class ThreeRulesWorkingOnOneRefusal(unittest.TestCase):
    """
    4.1.22 states a refusal, 4.1.23 narrows it, 4.1.24 loosens it —
    and none of them repeats the others.
    """

    def test_all_three_hold_to_the_same_condition(self):
        from src.astadhyayi.stri import provisions_for

        for sutra in ("4.1.22", "4.1.23", "4.1.24"):
            with self.subTest(sutra=sutra):
                row, = provisions_for(sutra)
                self.assertTrue(row.refuses)
                self.assertEqual(row.compound, "dvigu")
                self.assertEqual(row.of_samjna, "taddhita-luk")

    def test_and_only_the_last_of_them_is_optional(self):
        from src.astadhyayi.stri import provisions_for

        optional = [sutra for sutra in ("4.1.22", "4.1.23", "4.1.24")
                    if provisions_for(sutra)[0].optional]
        self.assertEqual(optional, ["4.1.24"])

    def test_the_narrowing_rule_leaves_the_wider_case_alone(self):
        """
        4.1.23 restricts the refusal to a FIELD, so a rope of the same
        measurement keeps its ङीप् — द्विकाण्डी रज्जुः. The row's own
        `keeps_out` says so, and the resolver has to agree.
        """
        from src.astadhyayi.stri import provisions_for, stri_affix

        row, = provisions_for("4.1.23")
        self.assertIn("रज्जुः", row.keeps_out)
        field = stri_affix(compound="dvigu", stem_final="kāṇḍa",
                           samjna="taddhita-luk", sense="kṣetra")
        rope = stri_affix(compound="dvigu", stem_final="kāṇḍa",
                          samjna="taddhita-luk")
        self.assertEqual(field.blocked_by, "4.1.23")
        self.assertEqual(rope.blocked_by, "4.1.22")


class WhatTheRulesKeepOut(unittest.TestCase):
    """
    Where a row records the form its rule's own words exclude, the
    form has to be traceable in the rule's notes — otherwise the
    record is decoration.
    """

    def test_each_kept_out_form_is_in_its_rules_notes(self):
        from src.astadhyayi.stri import STRI_TABLE

        checked = 0
        for row in STRI_TABLE:
            if not row.keeps_out:
                continue
            notes = unwrapped(REGISTRY.get(row.sutra).notes)
            head = row.keeps_out.split(",")[0].split(" (")[0].strip()
            checked += 1
            with self.subTest(sutra=row.sutra, form=head):
                self.assertIn(head, notes)
        self.assertGreater(checked, 5)


class TwoWordsIrregularInOppositeHalves(unittest.TestCase):
    """
    4.1.32 fixes अन्तर्वत् and पतिवत् in one rule, and each has its
    irregularity where the other has its regularity.
    """

    def test_the_rule_gives_an_augment_and_the_affix_follows(self):
        from src.astadhyayi.stri import stri_affix

        answer = stri_affix("antarvat")
        self.assertEqual(answer.by, "4.1.32")
        self.assertEqual(answer.gives, "ṅīp")
        self.assertEqual(answer.along_with, "nuk")

    def test_and_both_directions_are_on_record(self):
        notes = unwrapped(REGISTRY.get("4.1.32").notes)
        self.assertIn("मतुब् निपात्यते, वत्वं सिद्धम्", notes)
        self.assertIn("वत्वं निपात्यते, मतुप् सिद्धः", notes)

    def test_the_fixing_holds_them_to_the_special_sense(self):
        notes = unwrapped(REGISTRY.get("4.1.32").notes)
        self.assertIn("निपातनसामर्थ्यात्", notes)
        self.assertIn("पतिमती पृथिवी", notes)


class OneOptionMakingThreeForms(unittest.TestCase):
    """
    4.1.38 मनोरौ वा. The वा covers this rule's own औ AND the ऐ
    carried down from 4.1.37, so a rule naming one substitute yields
    three readings.
    """

    def test_the_rule_answers_and_is_optional(self):
        from src.astadhyayi.stri import stri_affix

        answer = stri_affix("manu", sense="puṃyoga")
        self.assertEqual(answer.by, "4.1.38")
        self.assertTrue(answer.optional)
        self.assertEqual(answer.along_with, "au")

    def test_the_rule_it_borrows_from_supplies_the_other(self):
        from src.astadhyayi.stri import stri_affix

        borrowed = stri_affix("vṛṣākapi", sense="puṃyoga")
        self.assertEqual(borrowed.by, "4.1.37")
        self.assertIn("ai", borrowed.along_with)
        self.assertFalse(borrowed.optional)

    def test_and_the_note_says_why_there_are_three(self):
        notes = unwrapped(REGISTRY.get("4.1.38").notes)
        self.assertIn("द्वावपि विकल्प्येते", notes)
        self.assertIn("त्रैरूप्यं", notes)

    def test_one_word_of_the_accent_rule_is_for_one_member_only(self):
        """
        4.1.37 names four words and states the accent for one of them.
        अग्न्यादिषु पुनरन्तोदात्तेषु स्थानिवद्भावादेव सिद्धम् — the
        other three get it by 1.1.56 from the stems they replace.
        """
        from src.astadhyayi.stri import provisions_for

        row, = provisions_for("4.1.37")
        self.assertEqual(len(row.of), 4)
        self.assertIn("स्थानिवद्भावादेव सिद्धम्",
                      unwrapped(REGISTRY.get("4.1.37").notes))


class TheFourthAttribution(unittest.TestCase):
    """
    4.1.17 प्राचाम् is the fourth teacher-citation the project has
    met, and the second to the eastern school.
    """

    def test_the_rule_names_them_and_the_other_view_stands(self):
        from src.astadhyayi.stri import provisions_for

        row, = provisions_for("4.1.17")
        self.assertEqual(row.authority, "prācām")
        self.assertTrue(row.optional)
        self.assertIn("अन्येषाम्", unwrapped(REGISTRY.get("4.1.17").notes))

    def test_and_the_next_rule_closes_the_option_for_one_list(self):
        from src.astadhyayi.stri import provisions_for, stri_affix

        row, = provisions_for("4.1.18")
        self.assertFalse(row.optional)
        self.assertEqual(stri_affix(gana="lohitādi").gives, "ṣpha")

    def test_every_attribution_so_far_is_still_findable(self):
        """
        Five now, in two kinds: two schools cited in 3.4, one man
        cited twice in 3.4, and the eastern school twice again here.
        The set is read off the tables rather than listed, so it grows
        with the work — and it did, the moment 4.1.43 was codified.
        """
        from src.astadhyayi.ktva_namul import attributed_schools
        from src.astadhyayi.stri import STRI_TABLE
        from src.astadhyayi.tin_adesha import TIN_ADESA

        cited = {row.sutra for row in TIN_ADESA if row.authority}
        cited |= {row.sutra for row in STRI_TABLE if row.authority}
        cited |= {sutra for sutra, _ in attributed_schools()}
        self.assertEqual(
            cited,
            {"3.4.18", "3.4.19", "3.4.111", "3.4.112",
             "4.1.17", "4.1.43"})


class TheGanaThatIsNotOneList(unittest.TestCase):
    """
    4.1.4's अजादि. अजादिग्रहणं तु क्वचिद् जातिलक्षणे ङीषि प्राप्ते,
    क्वचित् तु पुंयोगलक्षणे ... — its members are there to block five
    different rules, a different one each.
    """

    def test_the_rule_records_all_five_grounds(self):
        notes = unwrapped(REGISTRY.get("4.1.4").notes)
        for ground in ("जातिलक्षणे", "पुंयोगलक्षणे",
                       "पुष्पफलोत्तरपदलक्षणे", "वयोलक्षणे",
                       "टिल्लक्षणे"):
            with self.subTest(ground=ground):
                self.assertIn(ground, notes)

    def test_and_it_is_where_the_vrtti_sends_what_it_cannot_place(self):
        """
        4.1.21's कथं त्रिफला? अजादिषु दृश्यते, and 4.1.64's
        पुष्पफलमूलोत्तरपदात् तु यतो नेष्यते तदजादिषु पठ्यते. The list
        is a residue, and two rules of this pāda say so.
        """
        self.assertIn("अजादिषु दृश्यते",
                      unwrapped(REGISTRY.get("4.1.21").notes))

    def test_the_gana_is_read_from_the_text_on_disk(self):
        """
        The lists are data, not code. If अजादि is not in the गणपाठ
        the rule is citing something the project does not have.
        """
        from src.astadhyayi.corpus import load_ganapatha

        self.assertIn("4.1.4", load_ganapatha())


if __name__ == "__main__":
    unittest.main()

class ThreeConditionsDefinedInVerse(unittest.TestCase):
    """
    गुणवचन at 4.1.44, स्वाङ्ग at 4.1.54 and जाति at 4.1.63. Each is a
    condition the sūtra states in one word and the vṛtti defines in a
    verse — because none of the three is visible in the form of the
    word, and a rule that turns on one of them cannot be applied
    without knowing what it means.

    Three in thirty-eight sūtras, and none anywhere else in the run.
    """

    IN_VERSE = {
        "4.1.44": "सोऽसत्त्वप्रकृतिर्गुणः",
        "4.1.54": "अद्रवं मूर्तिमत् स्वाङ्गं",
        "4.1.63": "आकृतिग्रहणा जातिर्",
    }

    def test_each_one_carries_its_definition(self):
        for sutra, verse in self.IN_VERSE.items():
            with self.subTest(sutra=sutra):
                self.assertIn(verse,
                              unwrapped(REGISTRY.get(sutra).notes))

    def test_and_each_is_a_condition_the_table_actually_uses(self):
        """
        A definition attached to a condition nothing turns on would be
        ornament. Each of the three has to be a `sense` or a `samjna`
        some row states.
        """
        from src.astadhyayi.stri import STRI_TABLE

        conditions = {row.sense for row in STRI_TABLE if row.sense}
        conditions |= {row.of_samjna for row in STRI_TABLE
                       if row.of_samjna}
        for named in ("guṇavacana", "svāṅga", "jāti"):
            with self.subTest(condition=named):
                self.assertIn(named, conditions)

    def test_the_quality_word_rule_answers_and_is_optional(self):
        from src.astadhyayi.stri import stri_affix

        answer = stri_affix(stem_final="u", sense="guṇavacana")
        self.assertEqual(answer.by, "4.1.44")
        self.assertEqual(answer.gives, "ṅīṣ")
        self.assertTrue(answer.optional)


class ElevenWordsAndElevenSenses(unittest.TestCase):
    """
    4.1.42, and no other rule of the run does anything like it. The
    pairing is held as pairs so it cannot come apart, which is the
    same reason 3.4.82's nine endings are held against 3.4.78's nine.
    """

    def test_the_two_lists_are_the_same_length(self):
        from src.astadhyayi.stri import provisions_for

        row, = provisions_for("4.1.42")
        words = [word for word, _ in row.pairs]
        senses = [sense for _, sense in row.pairs]
        self.assertEqual(len(words), len(senses))
        self.assertEqual(len(set(words)), len(words))
        self.assertEqual(len(row.pairs), 11)

    def test_a_word_answers_only_in_its_own_sense(self):
        from src.astadhyayi.stri import NotAdded, stri_affix

        self.assertEqual(
            stri_affix("kuṇḍa", sense="amatra").by, "4.1.42")
        self.assertIsInstance(
            stri_affix("kuṇḍa", sense="āvapana"), NotAdded)

    def test_and_a_word_outside_the_eleven_is_not_reached(self):
        from src.astadhyayi.stri import NotAdded, stri_affix

        self.assertIsInstance(
            stri_affix("devadatta", sense="amatra"), NotAdded)

    def test_the_sense_decides_which_rule_gives_the_affix(self):
        """
        नागी in the sense of bulk is this rule's; नागी as a
        class-name is 4.1.63's. नागशब्दो गुणवचनः स्थौल्ये ङीषम्
        उत्पादयति ... जातिवचनात् तु जातिलक्षणो ङीषेव भवति — one word,
        one affix, two rules, told apart by nothing but the sense.
        """
        from src.astadhyayi.stri import stri_affix

        bulk = stri_affix("nāga", sense="sthaulya")
        kind = stri_affix("nāga", sense="jāti",
                          samjna="astrīviṣaya")
        self.assertEqual(bulk.by, "4.1.42")
        self.assertEqual(kind.by, "4.1.63")
        self.assertEqual(bulk.gives, kind.gives)


class ThreePairsDifferingOnlyInAccent(unittest.TestCase):
    """
    4.1.25 against 4.1.26, 4.1.39 against 4.1.40, and 4.1.60 against
    the ङीष् rules it excepts. ङीप् and ङीष् both give ई; each pair
    spends a whole sūtra on which syllable carries the pitch.
    """

    PAIRS = (("4.1.25", "4.1.26"), ("4.1.39", "4.1.40"))

    def test_each_pair_gives_two_different_affixes(self):
        from src.astadhyayi.stri import provisions_for

        for one, other in self.PAIRS:
            with self.subTest(pair=(one, other)):
                first = {row.gives for row in provisions_for(one)}
                second = {row.gives for row in provisions_for(other)}
                self.assertEqual(first | second, {"ṅīp", "ṅīṣ"})

    def test_and_at_least_one_of_each_pair_says_so(self):
        marks = [sutra for pair in self.PAIRS for sutra in pair
                 if "स्वरे विशेषः" in unwrapped(REGISTRY.get(sutra).notes)
                 or "स्वरे विशेषः" in "".join(
                     row.why for row in
                     __import__("src.astadhyayi.stri", fromlist=["x"])
                     .provisions_for(sutra))]
        self.assertTrue(marks)

    def test_the_two_affixes_really_are_both_i(self):
        """
        The point of the pairs. If ङीप् and ङीष् gave different
        shapes the rules would be doing ordinary work; they give the
        same shape, and the whole difference is the accent their
        marks leave behind.
        """
        from src.astadhyayi.sup import NGI

        for affix in NGI:
            with self.subTest(affix=affix):
                self.assertTrue(affix.startswith("ṅī"))


class ARefusalIsNotNarrowerByCountingWords(unittest.TestCase):
    """
    4.1.56 न क्रोडादिबह्वचः exists for nothing but to stop 4.1.54.
    It states ONE condition against that rule's two, so a resolver
    that ranked everything by specificity let the rule being excepted
    beat the exception.

    Specificity picks between rules that GIVE. Whether a प्रतिषेध
    applies is a different question, and the resolver now asks it
    separately.
    """

    def test_the_exception_stops_the_wider_rule(self):
        from src.astadhyayi.stri import stri_affix

        blocked = stri_affix(gana="kroḍādi", samjna="svāṅga")
        self.assertEqual(blocked.by, "4.1.54")
        self.assertEqual(blocked.blocked_by, "4.1.56")
        self.assertFalse(blocked.gives)

    def test_though_it_states_fewer_conditions(self):
        from src.astadhyayi.stri import _how_specific, provisions_for

        wider = provisions_for("4.1.54")[0]
        exception = provisions_for("4.1.56")[0]
        self.assertLess(_how_specific(exception), _how_specific(wider))

    def test_and_the_wider_rule_still_answers_where_nothing_excepts(self):
        from src.astadhyayi.stri import stri_affix

        self.assertEqual(stri_affix(samjna="svāṅga").gives, "ṅīṣ")

    def test_three_rules_refusing_one_affix_and_the_narrowest_speaks(self):
        """
        4.1.22, 4.1.23 and 4.1.24 all refuse the same ङीप्. Which of
        them reports is settled among the refusals alone, so the
        narrowest that matches is the one that speaks — and none of it
        depends on how they rank against the rule they except.
        """
        from src.astadhyayi.stri import stri_affix

        plain = stri_affix(compound="dvigu", samjna="taddhita-luk")
        field = stri_affix(compound="dvigu", samjna="taddhita-luk",
                           stem_final="kāṇḍa", sense="kṣetra")
        depth = stri_affix(compound="dvigu", samjna="taddhita-luk",
                           stem_final="puruṣa", sense="pramāṇa")
        self.assertEqual(
            [plain.blocked_by, field.blocked_by, depth.blocked_by],
            ["4.1.22", "4.1.23", "4.1.24"])
        for answer in (plain, field, depth):
            self.assertEqual(answer.by, "4.1.21")


class AWordTravellingBackwardAndWhatItArrivesToDo(unittest.TestCase):
    """
    4.1.18's सर्वत्र is pulled DOWN into 4.1.17 —
    उत्तरसूत्रादिहापकृष्यते, बाधकबाधनार्थम् — so that the eastern
    teachers' ष्फ may beat 4.1.75's चाप्. Both ends of the transaction
    are in the commentary, and both are now codified.
    """

    def test_the_lender_says_which_way_the_word_travels(self):
        notes = unwrapped(REGISTRY.get("4.1.18").notes)
        self.assertIn("उत्तरसूत्रादिहापकृष्यते", notes)
        self.assertIn("बाधकबाधनार्थम्", notes)

    def test_and_the_far_end_says_what_it_arrives_to_do(self):
        notes = unwrapped(REGISTRY.get("4.1.75").notes)
        self.assertIn("सर्वत्रग्रहणात्", notes)
        self.assertIn("4.1.18", notes)
        self.assertIn("4.1.17", notes)

    def test_both_rules_of_the_transaction_are_codified(self):
        for sutra in ("4.1.17", "4.1.18", "4.1.75"):
            with self.subTest(sutra=sutra):
                self.assertTrue(REGISTRY.has(sutra))

    def test_and_the_rule_it_beats_gives_the_affix_it_beats(self):
        from src.astadhyayi.stri import stri_affix

        self.assertEqual(stri_affix("āvaṭya").gives, "cāp")
        self.assertEqual(stri_affix(marked="yañ", wants="ṣpha").gives,
                         "ṣpha")


class TheOneRuleRunningTheOtherWay(unittest.TestCase):
    """
    Four rules of this run license a Vedic form. 4.1.62 licenses an
    ORDINARY one and leaves the Veda alone, and it is the only one of
    its kind here.
    """

    def test_the_vedic_rules_are_marked_and_this_one_is_not(self):
        from src.astadhyayi.stri import STRI_TABLE

        vedic = {row.sutra for row in STRI_TABLE if row.chandasi}
        self.assertEqual(
            vedic, {"4.1.29", "4.1.46", "4.1.47", "4.1.59", "4.1.71"})
        self.assertNotIn("4.1.62", vedic)

    def test_and_it_holds_itself_to_ordinary_speech(self):
        from src.astadhyayi.stri import NotAdded, stri_affix

        self.assertEqual(stri_affix("sakhi", sense="bhāṣā").by,
                         "4.1.62")
        self.assertIsInstance(stri_affix("sakhi"), NotAdded)

    def test_the_note_gives_the_vedic_form_it_leaves_standing(self):
        self.assertIn("सखा सप्तपदी भव",
                      unwrapped(REGISTRY.get("4.1.62").notes))


class ARedundancyThatTeaches(unittest.TestCase):
    """
    4.1.41 puts two words in a list that its own षित् clause would
    already have reached. षित्त्वादेव सिद्धे ज्ञापनार्थं वचनम् — and
    what it teaches is अनित्यः षिल्लक्षणो ङीषिति, that the षित्
    ground is NOT invariable.

    The same shape as 3.4.103's ङिद्वचनं ज्ञापनार्थम्: a rule that
    says too much, and the excess is the information.
    """

    def test_the_rule_states_both_grounds_separately(self):
        from src.astadhyayi.stri import provisions_for

        rows = provisions_for("4.1.41")
        self.assertEqual({row.marked for row in rows} - {""}, {"ṣit"})
        self.assertEqual({row.gana for row in rows} - {""}, {"gaurādi"})

    def test_and_the_note_records_what_the_excess_teaches(self):
        notes = unwrapped(REGISTRY.get("4.1.41").notes)
        self.assertIn("ज्ञापनार्थं वचनम्", notes)
        self.assertIn("अनित्यः षिल्लक्षणो ङीषिति", notes)

    def test_the_project_has_met_this_shape_before(self):
        """
        Not a claim about words: both notes have to point at the
        same kind of argument, and 3.4.103 is where it was first met.
        """
        self.assertIn("3.4.103", unwrapped(REGISTRY.get("4.1.41").notes))
        self.assertIn("ज्ञापनार्थम्",
                      unwrapped(REGISTRY.get("3.4.103").notes))


class WhichWordOfARuleIsStillRunning(unittest.TestCase):
    """
    4.1.73 beats 4.1.63's ङीष् and not 4.1.48's, and the difference is
    which WORD of each is carried down here: जातिग्रहणं चेहानुवर्तते,
    तेन जातिलक्षणो ङीषनेन बाध्यते, न पुंयोगलक्षणः.
    """

    def test_the_two_rules_it_might_beat_both_give_the_same_affix(self):
        from src.astadhyayi.stri import provisions_for

        for sutra in ("4.1.48", "4.1.63"):
            with self.subTest(sutra=sutra):
                row, = provisions_for(sutra)
                self.assertEqual(row.gives, "ṅīṣ")

    def test_and_only_one_of_them_is_stated_with_the_word_that_carries(self):
        from src.astadhyayi.stri import provisions_for

        beaten, = provisions_for("4.1.63")
        standing, = provisions_for("4.1.48")
        self.assertEqual(beaten.sense, "jāti")
        self.assertNotEqual(standing.sense, "jāti")

    def test_the_note_says_which_falls_and_which_stands(self):
        notes = unwrapped(REGISTRY.get("4.1.73").notes)
        self.assertIn("जातिलक्षणो ङीषनेन बाध्यते, न पुंयोगलक्षणः",
                      notes)


class TheFourContainmentsThatWereOwed(unittest.TestCase):
    """
    क्रीत, पति, बाहु and ऊरु were kept out of the containment table
    while their rules were ahead, by a test that required both halves
    of every entry to be something a codified rule states. The rules
    are here now.
    """

    def test_all_four_are_declared(self):
        from src.astadhyayi.stri import WITHIN

        for final in ("krīta", "pati", "bāhu", "ūru"):
            with self.subTest(final=final):
                self.assertIn(final, WITHIN)

    def test_and_each_names_a_final_the_table_states(self):
        from src.astadhyayi.stri import STRI_TABLE, WITHIN

        stated = {row.stem_final for row in STRI_TABLE if row.stem_final}
        for narrow, wider in WITHIN.items():
            with self.subTest(final=narrow):
                self.assertIn(narrow, stated)
                for one in wider:
                    self.assertIn(one, stated)

    def test_the_containment_lets_the_narrower_rule_win(self):
        from src.astadhyayi.stri import stri_affix

        self.assertEqual(
            stri_affix(stem_final="ūru", sense="aupamye").by, "4.1.69")
        self.assertEqual(
            stri_affix(stem_final="u", sense="manuṣya-jāti").by,
            "4.1.66")


class TheFeminineRunIsFinished(unittest.TestCase):
    """
    4.1.3 to 4.1.75, and every affix 4.1.1's class-words promised is
    now supplied by some rule of it.
    """

    def test_the_run_is_contiguous(self):
        have = {s.id.number for s in REGISTRY.all()
                if s.id.adhyaya == 4 and s.id.pada == 1}
        self.assertEqual(have, set(range(1, max(have) + 1)))
        self.assertGreaterEqual(max(have), 75)

    def test_every_affix_has_a_rule_and_every_rule_an_affix(self):
        from src.astadhyayi.stri import STRI, STRI_TABLE, STRI_TADDHITA

        given = {row.gives for row in STRI_TABLE if row.gives}
        self.assertEqual(given, set(STRI) | set(STRI_TADDHITA))

    def test_and_an_affix_is_consumed_before_it_is_given(self):
        """
        4.1.74 यङश्चाप् reads यङ् as a class-word for ञ्यङ् and
        ष्यङ् — ञ्यङः ष्यङश्च सामान्यग्रहणमेतत् — and ष्यङ् is not
        made until 4.1.78. कारीषगन्ध्या is the example on both sides,
        and 4.1.78 spends a silent letter so that the earlier rule
        can reach it: ङकारः सामान्यग्रहणार्थः.
        """
        from src.astadhyayi.stri import provisions_for, stri_affix

        made = {row.sutra for row in provisions_for("4.1.78")}
        self.assertEqual(made, {"4.1.78"})
        self.assertEqual(
            stri_affix(marked="aṇ", sense="gotra",
                       samjna="guru-upottama").gives, "ṣyaṅ")
        self.assertIn("ञ्यङः ष्यङश्च सामान्यग्रहणमेतत्",
                      unwrapped(REGISTRY.get("4.1.74").notes))
        self.assertIn("सामान्यग्रहणार्थः",
                      unwrapped(REGISTRY.get("4.1.78").notes))

    def test_and_every_row_belongs_to_a_codified_sutra(self):
        from src.astadhyayi.stri import STRI_TABLE

        for row in STRI_TABLE:
            with self.subTest(sutra=row.sutra):
                self.assertTrue(REGISTRY.has(row.sutra))
