# -*- coding: utf-8 -*-
"""
जि (ji) → जयति (jayati), and जयति (jayati) → जि (ji).

Two questions that look like one question asked twice, and are not. The
first is what the Aṣṭādhyāyī answers: eight rules, in order, each naming
itself. The second the Aṣṭādhyāyī does not answer at all — there is no
rule that takes an affix off a word — so it is answered by making every
verb the grammar makes and seeing which making produced this one.

The tests are in that order. Between them stands the class-marker: ten
classes, ten विकरण (vikaraṇa), and one hand-checked form apiece — every
one of them the vṛtti's own example, so that the engine is measured
against the grammar and not against itself.

The rest is about the honesty of a search: that the filter which makes it
cheap loses nothing (checked over every form in reach, not on a sample),
that what the engine cannot build is withheld rather than answered
wrongly, and that where the grammar itself gives two answers, two answers
come back.
"""

from __future__ import annotations

import contextlib
import io
import re
import unittest

from src.astadhyayi.corpus import load_dhatupatha
from src.astadhyayi.prakriya import derive
from src.astadhyayi.prakriya_rules import all_rules, verb
from src.astadhyayi.sources import REGISTRY
from src.astadhyayi.vibhakti import NUMBERS, PERSONS
from src.astadhyayi.vikarana import CLASS_MARKERS, marker_of_class
from src.astadhyayi.vyutpatti import (
    FROM_A_VOWEL,
    IN_REACH,
    NOT_A_ROOT,
    SLOTS,
    VOWEL_BUCKET,
    candidates,
    forms_of,
    iast,
    in_reach,
    main,
    opening,
    owed_for,
    paradigm,
    root_opening,
    roots_of,
    searchable,
    unreachable,
)
from src.normalizer import iast_to_devanagari
import src.astadhyayi.rules  # noqa: F401  (populates REGISTRY)


#: 01.0642 जि जये — "to win". The entry this whole file is about.
JI = "01.0642"
#: 01.1096 जि अभिभवे — spelt the same, read again, a different sense.
JI_AGAIN = "01.1096"


def _entry(code: str):
    return load_dhatupatha()[code]


def _third_singular(code: str) -> str:
    return forms_of(_entry(code).upadesa, code.split(".")[0])[(0, 0)]


class TheForwardDerivation(unittest.TestCase):
    """जि (ji) + तिप् (tip) → जयति (jayati), in the engine's own steps."""

    def setUp(self) -> None:
        self.done = derive(verb("ji", person=0, number=0), all_rules())

    def test_it_ends_where_the_dhatupatha_says_it_should(self):
        self.assertEqual(self.done.surface, "jayati")
        self.assertEqual(self.done.stopped, "no rule applies")

    def test_and_it_starts_from_the_root_and_an_ending_it_did_not_choose(self):
        # जि (ji) is not अनुदात्तेत् (anudāttet), so 1.3.12 does not make it
        # middle and 1.3.78 शेषात् कर्तरि परस्मैपदम् leaves it active. The
        # ending is तिप् (tip) because of that, not because it was typed in.
        start = verb("ji", person=0, number=0)
        self.assertEqual(start.surface, "jitip")
        self.assertNotIn("ātmanepada", start.terms[-1].samjnas)
        self.assertIn("sārvadhātuka", start.terms[-1].samjnas)

    def test_and_the_four_rules_that_do_the_work_are_these(self):
        # 1.3.3 हलन्त्यम् strips तिप्'s प्; 3.1.68 कर्तरि शप् puts शप्
        # between; 7.3.84 gives the इ (i) its गुण (guṇa); 6.1.78 turns the
        # ए (e) so made into अय् (ay) before the following अ (a).
        used = [step.sutra for step in self.done.steps]
        for sutra in ("1.3.3", "1.3.9", "3.1.68", "1.3.8",
                      "7.3.84", "6.1.78"):
            self.assertIn(sutra, used, sutra)
        self.assertEqual(used[-2:], ["7.3.84", "6.1.78"])

    def test_and_each_of_those_is_a_registered_sutra(self):
        for step in self.done.steps:
            self.assertTrue(REGISTRY.has(step.sutra), step.sutra)

    def test_and_the_intermediate_forms_are_the_ones_a_grammarian_writes(self):
        # जितिप् → जिति → जिशप्ति → जिअति → जेअति → जयति.
        seen = [self.done.start.surface] + [s.after for s in self.done.steps]
        for form in ("jitip", "jiti", "jiśapti", "jiati", "jeati", "jayati"):
            self.assertIn(form, seen, form)

    def test_and_sap_leaves_only_its_a_behind(self):
        # शप् (śap) is श् + अ + प्. The श् is an इत् by 1.3.8 and the प्
        # by 1.3.3, so what is actually inserted into the word is one अ —
        # and the श् is not wasted: it is what makes 3.4.113 call the
        # affix सार्वधातुक, which is the condition 7.3.84 then reads.
        after_sap = next(s for s in self.done.steps if s.sutra == "3.1.68")
        self.assertEqual(after_sap.after, "jiśapti")
        self.assertTrue(REGISTRY.has("3.4.113"))
        self.assertIn("jiati", [s.after for s in self.done.steps])

    def test_and_the_whole_paradigm_is_the_one_in_the_books(self):
        self.assertEqual(forms_of("ji"), {
            (0, 0): "jayati", (0, 1): "jayataḥ", (0, 2): "jayanti",
            (1, 0): "jayasi", (1, 1): "jayathaḥ", (1, 2): "jayatha",
            (2, 0): "jayāmi", (2, 1): "jayāvaḥ", (2, 2): "jayāmaḥ",
        })


#: code → (the sūtra that gives its class the marker, the vṛtti's form).
#: Every one of these words is quoted in the commentary on the sūtra
#: beside it, so the engine is measured against the grammar's own worked
#: examples and not against what it happens to produce.
GIVEN = {
    "01.0001": ("3.1.68", "bhavati"),    # भू — शप्
    "02.0001": ("2.4.72", "atti"),       # अद् — शप् elided
    "03.0001": ("2.4.75", "juhoti"),     # हु — श्लु, and doubling
    "04.0001": ("3.1.69", "dīvyati"),    # दिव् — श्यन्
    "05.0001": ("3.1.73", "sunoti"),     # षु — श्नु
    "06.0001": ("3.1.77", "tudati"),     # तुद् — श
    "07.0001": ("3.1.78", "ruṇaddhi"),   # रुध् — श्नम्, inside the root
    "08.0001": ("3.1.79", "tanoti"),     # तन् — उ
    "09.0001": ("3.1.81", "krīṇāti"),    # क्री — श्ना
    "10.0001": ("3.1.25", "corayati"),   # चुर् — णिच्
}


class TenClassesAndTenMarkers(unittest.TestCase):
    """One form per class, and every one the vṛtti's own example."""

    def test_every_class_makes_the_form_its_vrtti_gives(self):
        for code, (_sutra, want) in GIVEN.items():
            self.assertEqual(_third_singular(code), want, code)

    def test_and_the_marker_each_used_is_the_one_the_corpus_names(self):
        for code, (sutra, _want) in GIVEN.items():
            marker = marker_of_class(code.split(".")[0])
            self.assertIsNotNone(marker, code)
            self.assertEqual(marker[1], sutra, code)
            self.assertTrue(REGISTRY.has(sutra), sutra)

    def test_and_the_sutra_that_gave_it_is_named_in_the_derivation(self):
        # Not a coincidence of spelling: the trace has to cite the rule.
        for code, (sutra, _want) in GIVEN.items():
            if sutra == "3.1.68":
                continue          # the उत्सर्ग, tested in its own class
            done = derive(verb(_entry(code).upadesa,
                               gana=code.split(".")[0]), all_rules())
            self.assertIn(sutra, [step.sutra for step in done.steps], code)

    def test_and_a_second_root_of_each_class_agrees(self):
        wanted = {
            ("01.0642", "01"): "jayati",     # जि
            ("02.0044", "02"): "yāti",       # या
            ("03.0011", "03"): "dadhāti",    # डुधाञ्
            ("04.0002", "04"): "sīvyati",    # षिवुँ
            ("06.0002", "06"): "nudati",     # णुदँ
            ("07.0002", "07"): "bhinatti",   # भिदिँर्
            ("08.0010", "08"): "karoti",     # डुकृञ्
            ("09.0002", "09"): "prīṇāti",    # प्रीञ्
        }
        for (code, gana), want in wanted.items():
            self.assertEqual(
                forms_of(_entry(code).upadesa, gana)[(0, 0)], want, code)

    def test_and_the_seventh_class_puts_its_marker_inside_the_root(self):
        # 1.1.47 मिदचोऽन्त्यात्परः — रुध् takes श्नम् as रु-न-ध्, which
        # is what मकारो देशविध्यर्थः is for, and the ण् of रुणद्धि then
        # comes by 8.4.2 from the र् two sounds back.
        done = derive(verb(_entry("07.0001").upadesa, gana="07"), all_rules())
        seen = [step.after for step in done.steps]
        self.assertIn("runadhti", seen)
        self.assertIn("8.4.2", [step.sutra for step in done.steps])
        self.assertTrue(REGISTRY.has("1.1.47"))

    def test_and_the_third_class_doubles_before_it_can_be_read(self):
        # 2.4.75's श्लु is named where लुक् would have done — लुकि
        # प्रकृते श्लुविधानं द्विर्वचनार्थम्, for the sake of the
        # doubling. हु becomes जुहोति through 6.1.10, 7.4.62 and 8.4.54.
        done = derive(verb("hu", gana="03"), all_rules())
        used = [step.sutra for step in done.steps]
        for sutra in ("2.4.75", "6.1.10", "7.4.62", "8.4.54"):
            self.assertIn(sutra, used, sutra)
        self.assertIn("huhuti", [step.after for step in done.steps])

    def test_and_the_tenth_class_is_a_new_root_and_then_takes_sap(self):
        # 3.1.25's णिच् is not a विकरण: 3.1.32 सनाद्यन्ता धातवः makes
        # चोरि a root, and शप् comes after THAT. चोरयति has both.
        done = derive(verb(_entry("10.0001").upadesa, gana="10"), all_rules())
        used = [step.sutra for step in done.steps]
        self.assertLess(used.index("3.1.25"), used.index("3.1.68"))
        self.assertIn("7.3.86", used)     # चुर् → चोर् before the णिच्
        self.assertTrue(REGISTRY.has("3.1.32"))


class WhereTheMarkerDecidesTheWholeParadigm(unittest.TestCase):
    """The classes whose singular and plural part company, and why."""

    def test_the_ninth_class_has_three_shapes_of_one_marker(self):
        # श्ना stands as आ before the पित् ति, becomes ई by 6.4.113 before
        # a consonant-initial ङित्, and is dropped by 6.4.112 before a
        # vowel-initial one. क्रीणाति, क्रीणीतः, क्रीणन्ति.
        made = forms_of(_entry("09.0001").upadesa, "09")
        self.assertEqual(made[(0, 0)], "krīṇāti")
        self.assertEqual(made[(0, 1)], "krīṇītaḥ")
        self.assertEqual(made[(0, 2)], "krīṇanti")
        for sutra in ("6.4.112", "6.4.113"):
            self.assertTrue(REGISTRY.has(sutra), sutra)

    def test_and_the_seventh_class_loses_its_markers_a(self):
        # 6.4.111 श्नसोरल्लोपः — रुणद्धि keeps the अ before the पित् ति
        # and रुन्धन्ति does not.
        made = forms_of(_entry("07.0001").upadesa, "07")
        self.assertEqual(made[(0, 0)], "ruṇaddhi")
        self.assertEqual(made[(0, 2)], "rundhanti")
        self.assertTrue(REGISTRY.has("6.4.111"))

    def test_and_the_third_class_takes_at_where_others_take_anta(self):
        # 7.1.4 अदभ्यस्तात् — झि becomes अत् after an अभ्यस्त, and it is
        # 7.1.3 झोऽन्तः's exception: जुह्वति, ददति, not *जुह्वन्ति.
        self.assertEqual(forms_of("hu", "03")[(0, 2)], "juhvati")
        self.assertEqual(
            forms_of(_entry("03.0010").upadesa, "03")[(0, 2)], "dadati")
        # and where nothing is अभ्यस्त, 7.1.3 stands
        self.assertEqual(forms_of("bhū", "01")[(0, 2)], "bhavanti")
        for sutra in ("7.1.3", "7.1.4"):
            self.assertTrue(REGISTRY.has(sutra), sutra)

    def test_and_guna_is_kept_off_by_the_markers_own_silent_letter(self):
        # श (śa) and श्यन् (śyan) are अपित्, 1.2.4 सार्वधातुकमपित् makes
        # them ङिद्वत्, and 1.1.5 क्ङिति च then blocks the guṇa that
        # would have given *तोदति for तुदति. उ (3.1.79) has no श् and is
        # आर्धधातुक, so nothing blocks it and करोति has its अर्.
        self.assertEqual(_third_singular("06.0001"), "tudati")
        self.assertEqual(forms_of(_entry("08.0010").upadesa, "08")[(0, 0)],
                         "karoti")
        for sutra in ("1.2.4", "1.1.5", "3.4.113", "3.4.114"):
            self.assertTrue(REGISTRY.has(sutra), sutra)

    def test_and_the_light_penult_is_a_rule_of_its_own(self):
        # 7.3.84 reaches only an aṅga that ENDS in an इक्. बुध् does not,
        # and its guṇa is 7.3.86's; जीव् has a long ई and takes none —
        # जीवति, not *जेवति, which is what a scan for "the last इक्
        # anywhere" produced.
        self.assertEqual(_third_singular("01.1016"), "bodhati")
        self.assertEqual(_third_singular("01.0643"), "jīvati")
        self.assertEqual(_third_singular("01.1145"), "karṣati")
        self.assertTrue(REGISTRY.has("7.3.86"))


class TheRootIsFoundByMakingNotByUnmaking(unittest.TestCase):
    """जयति (jayati) → जि (ji), which no rule of the grammar does."""

    def test_the_word_is_traced_to_the_root_the_dhatupatha_gives(self):
        found = roots_of("jayati")
        self.assertEqual([v.code for v in found], [JI, JI_AGAIN])
        for one in found:
            self.assertEqual(one.upadesa, "ji")
            self.assertEqual(one.dhatu, "ji")
            self.assertEqual(one.gana, 1)

    def test_and_either_script_asks_the_same_question(self):
        self.assertEqual([v.code for v in roots_of("जयति")],
                         [v.code for v in roots_of("jayati")])
        self.assertEqual(iast("जयति"), "jayati")

    def test_and_the_answer_carries_the_derivation_that_produced_it(self):
        # Not a lookup table: the answer is the making, and it can be
        # read back and checked against the word that was asked about.
        one = roots_of("jayati")[0]
        self.assertEqual(one.prakriya.surface, "jayati")
        self.assertIn("3.1.68", [s.sutra for s in one.prakriya.steps])
        trace = one.trace()
        self.assertIn("कर्तरि शप्", trace)
        self.assertIn("jeati → jayati", trace)
        self.assertTrue(trace.rstrip().endswith("[no rule applies]"))

    def test_and_it_says_which_of_the_nine_endings_it_is(self):
        one = roots_of("jayati")[0]
        self.assertEqual((one.person, one.number), (0, 0))
        self.assertEqual(one.person_name, PERSONS[0])
        self.assertEqual(one.number_name, NUMBERS[0])
        self.assertEqual(one.pada, "parasmaipada")

    def test_and_the_other_eight_are_traced_to_the_same_root(self):
        for (person, number), form in forms_of("ji").items():
            found = roots_of(form)
            self.assertIn(JI, [v.code for v in found], form)
            hit = next(v for v in found if v.code == JI)
            self.assertEqual((hit.person, hit.number), (person, number),
                             form)

    def test_and_a_word_of_every_class_is_traced_home(self):
        for code, (_sutra, form) in GIVEN.items():
            self.assertIn(code, [v.code for v in roots_of(form)], form)

    def test_and_the_class_marker_it_used_is_named(self):
        one = roots_of("jayati")[0]
        self.assertEqual(one.marker, ("śap", "3.1.68"))
        self.assertEqual(marker_of_class("01"), ("śap", "3.1.68"))


class WhatTheGrammarWillNotDecide(unittest.TestCase):
    """Two answers, because the dhātupāṭha reads जि (ji) twice."""

    def test_the_ambiguity_is_reported_and_not_collapsed(self):
        found = roots_of("jayati")
        self.assertEqual(len(found), 2)
        self.assertEqual({v.upadesa for v in found}, {"ji"})
        # identical in every grammatical respect — the senses differ and
        # nothing else does, so no rule can choose between them.
        self.assertNotEqual(found[0].artha, found[1].artha)
        self.assertEqual(found[0].pada, found[1].pada)
        self.assertEqual(found[0].prakriya.surface,
                         found[1].prakriya.surface)

    def test_and_the_two_senses_are_the_dhatupathas_own_words(self):
        senses = {v.code: v.artha for v in roots_of("jayati")}
        self.assertIn("jaye", senses[JI])
        self.assertIn("aBiBave", senses[JI_AGAIN])

    def test_but_a_third_entry_spelt_the_same_is_not_among_them(self):
        # 10.0324 जि भाषायाम् is also spelt जि, and now that the tenth
        # class is in reach it IS derived — but not to this word. णिच्
        # gives it another shape, and only the dhātupāṭha's code ever
        # separated the two.
        self.assertNotIn("10.0324", [v.code for v in roots_of("jayati")])
        self.assertTrue(in_reach("10"))
        self.assertNotEqual(forms_of("ji", "10")[(0, 0)], "jayati")
        self.assertEqual(forms_of("ji", "01")[(0, 0)], "jayati")


class TheEnunciationIsWhatComesBack(unittest.TestCase):
    """
    The answer is the root as the grammar *writes* it, not as it looks.

    This is the whole reason the search runs forward. A word taken apart
    from the outside gives you the letters that are there; a word traced
    through its derivation gives you the letters that were there before
    the derivation removed them.
    """

    def test_a_word_with_an_n_is_traced_to_a_root_written_with_a_cerebral(self):
        # नयति (nayati) ← णीञ् (ṇīñ). 6.1.64/65 धात्वादेः turned the ण्
        # into न् before anything else happened, and 8.4.14 needs to know
        # the root was णोपदेश (ṇopadeśa) — प्रणयति, not *प्रनयति.
        found = roots_of("nayati")
        self.assertEqual([v.code for v in found], ["01.1049"])
        self.assertEqual(found[0].upadesa, "ṇīñ")
        self.assertEqual(found[0].dhatu, "ṇī")
        self.assertTrue(REGISTRY.has("8.4.14"))

    def test_and_a_word_with_no_marks_left_is_traced_to_one_with_three(self):
        # पचति (pacati) ← डुपचँष् (ḍupacaṣ): डु by 1.3.5, the nasal अ by
        # 1.3.2, the ष् by 1.3.3. None of the three is in the word.
        found = roots_of("pacati")
        self.assertEqual([v.code for v in found], ["01.1151"])
        self.assertEqual(found[0].dhatu, "pac")
        self.assertNotEqual(found[0].upadesa, found[0].dhatu)

    def test_and_two_entries_of_one_name_are_told_apart_by_their_accent(self):
        # पच् (pac) is read twice. डुपचँष् (01.1151) is svaritet and
        # active; पचिँ (01.0198) is anudāttet, so 1.3.12 अनुदात्तङित
        # आत्मनेपदम् makes it middle. The words differ, so the roots the
        # search returns differ, and the accent is what did it.
        self.assertEqual([v.code for v in roots_of("pacati")], ["01.1151"])
        self.assertEqual([v.code for v in roots_of("pacate")], ["01.0198"])
        self.assertEqual(roots_of("pacate")[0].pada, "ātmanepada")
        self.assertTrue(REGISTRY.has("1.3.12"))

    def test_and_the_gana_is_read_off_the_enunciation_not_off_the_name(self):
        # अद् (ad) is read in both the first gaṇa and the second, as
        # 01.0064 अदिँ (adi̐, बन्धने) and 02.0001 अदँ (ada̐, भक्षणे).
        # 2.4.72 अदिप्रभृतिभ्यः शपः elides शप् for the second only, so
        # the first gives अदति (adati) and the second अत्ति (atti).
        self.assertEqual([v.code for v in roots_of("adati")], ["01.0064"])
        self.assertEqual([v.code for v in roots_of("atti")], ["02.0001"])
        self.assertEqual(verb("ada̐").terms[0].enunciated, "ada̐")

    def test_and_the_class_is_carried_and_never_looked_up_by_name(self):
        # दिव् (div) is read in the first gaṇa, the fourth and the tenth,
        # and only 04.0001 दिवुँ says श्यन्. The Term carries the code.
        self.assertEqual(verb("divu̐", gana="04").terms[0].gana, "04")
        self.assertEqual(_third_singular("04.0001"), "dīvyati")

    def test_and_the_second_class_is_where_the_absence_shows(self):
        # अद् (ad) has no शप् at all, and its whole paradigm shows it.
        self.assertEqual(forms_of("ada̐", "02"), {
            (0, 0): "atti", (0, 1): "attaḥ", (0, 2): "adanti",
            (1, 0): "atsi", (1, 1): "atthaḥ", (1, 2): "attha",
            (2, 0): "admi", (2, 1): "advaḥ", (2, 2): "admaḥ",
        })
        self.assertEqual(marker_of_class("02"), ("luk", "2.4.72"))


class TheFilterLosesNothing(unittest.TestCase):
    """
    The search is cheap because it only tries roots that could open on
    the word's own sound. That is a claim about derivations, so it is
    checked against derivations — every root in reach in the commonest
    slot, and every slot of the two groups where the opening moves.
    """

    def test_a_word_is_looked_for_under_its_first_sound(self):
        self.assertEqual(opening("jayati"), "j")
        self.assertEqual(root_opening("ji"), "j")
        self.assertIn(_entry(JI), candidates("jayati"))

    def test_and_an_aspirate_counts_as_one_sound(self):
        self.assertEqual(opening("bhavati"), "bh")
        self.assertEqual(root_opening("bhū"), "bh")
        self.assertNotIn(_entry("01.0001"), candidates("bavati"))

    def test_and_a_root_written_with_a_cerebral_is_filed_under_the_plain(self):
        # णीञ् (ṇīñ) opens on ण् and नयति (nayati) on न्. 6.1.64/65 is
        # asked for that, not guessed at.
        self.assertEqual(root_opening("ṇīñ"), "n")
        self.assertEqual(root_opening("ṣaha̐"), "s")
        self.assertIn(_entry("01.1049"), candidates("nayati"))

    def test_and_a_root_whose_opening_is_a_mark_is_filed_under_the_rest(self):
        # डुपचँष् (ḍupacaṣ) opens on ड् only until 1.3.5 आदिर्ञिटुडवः
        # has taken डु away. It belongs under प् (p).
        self.assertEqual(root_opening("ḍupaca̐ṣ"), "p")
        self.assertEqual(root_opening("ḍukṛñ"), "k")

    def test_and_a_third_class_root_is_filed_under_its_copy(self):
        # हु (hu) is heard as जुहोति (juhoti), so it belongs under ज् —
        # 6.1.10's doubling, and then 7.4.62 and 8.4.54 on the copy.
        self.assertEqual(root_opening("hu"), "h")
        self.assertEqual(root_opening("hu", "03"), "j")
        self.assertIn(_entry("03.0001"), candidates("juhoti"))

    def test_and_every_vowel_initial_root_is_searched_together(self):
        # गुण (guṇa) by 7.3.84 and 6.1.78 both act on a root's own vowel,
        # so the opening of a vowel-initial root is the one thing a लट्
        # derivation can move: इ (i) becomes ए (e) becomes अय् (ay).
        self.assertEqual(root_opening("edha̐"), VOWEL_BUCKET)
        self.assertEqual(opening("edhate"), VOWEL_BUCKET)
        self.assertEqual(opening("atti"), VOWEL_BUCKET)

    def test_and_a_word_on_a_semivowel_looks_among_the_vowels_too(self):
        # 6.1.77 इको यणचि — इण् (iṇ) gives एति (eti) but also यन्ति
        # (yanti), and a bucket keyed on the sound alone would have lost
        # the plural of one of the commonest roots in the language.
        self.assertEqual(opening("yanti"), "y")
        self.assertIn("y", FROM_A_VOWEL)
        self.assertIn(_entry("02.0040"), candidates("yanti"))
        self.assertIn(_entry("02.0040"), candidates("eti"))

    def test_and_no_root_in_reach_is_lost_in_the_commonest_slot(self):
        # The exhaustive check, over every root the search covers.
        for entry in searchable():
            gana = entry.code.split(".")[0]
            third = next((one for one in paradigm(entry.upadesa, gana)
                          if (one.person, one.number) == (0, 0)), None)
            if third is None:
                continue
            self.assertIn(entry, candidates(third.surface),
                          f"{entry.code} {entry.upadesa} → {third.surface}")

    def test_and_none_is_lost_in_any_slot_where_the_opening_can_move(self):
        # The two groups the filter has to reason about rather than read:
        # a root that begins with a vowel, and one of the third class,
        # whose copy is what the ear meets first.
        risky = [entry for entry in searchable()
                 if entry.code.startswith("03")
                 or root_opening(entry.upadesa) == VOWEL_BUCKET]
        self.assertGreater(len(risky), 100)
        for entry in risky:
            gana = entry.code.split(".")[0]
            for made in paradigm(entry.upadesa, gana):
                self.assertIn(entry, candidates(made.surface),
                              f"{entry.code} → {made.surface}")


class WhatIsWithheldIsNamedNotSilent(unittest.TestCase):
    """A form the engine cannot finish is not answered wrongly."""

    def test_every_class_of_the_dhatupatha_is_now_in_reach(self):
        # This was the debt: eight of the ten had a codified sūtra saying
        # which marker they take and no rule that put one into a form.
        # All ten are wired, so `unreachable` is empty — and it is empty
        # because the engine says so, not because a list was edited.
        engine = {rule.sutra for rule in all_rules()}
        self.assertEqual(
            IN_REACH,
            frozenset(code for code, (_m, sutra) in CLASS_MARKERS.items()
                      if sutra in engine))
        self.assertEqual(sorted(IN_REACH),
                         ["%02d" % n for n in range(1, 11)])
        self.assertEqual(unreachable(), ())
        self.assertEqual(
            {code.split(".")[0] for code in load_dhatupatha()}, IN_REACH)

    def test_and_one_slot_is_still_out_of_reach_while_a_rule_is_not_wired(self):
        # 7.2.81 आतो ङितः turns the आ (ā) of आताम् (ātām) into इय् (iy)
        # after an अ-final stem: पचेते (pacete), एधेते (edhete). The
        # engine has not got it, so those two slots are withheld — the
        # other seven of एध (edha) are answered.
        self.assertEqual(owed_for("edha̐", "ātām", "ātmanepada"),
                         ("iy", "7.2.81"))
        self.assertTrue(REGISTRY.has("7.2.81"))
        held = {(m.person, m.number) for m in paradigm("edha̐", "01")}
        self.assertEqual(set(SLOTS) - held, {(0, 1), (1, 1)})
        self.assertEqual(forms_of("edha̐", "01")[(0, 0)], "edhate")
        self.assertEqual(forms_of("edha̐", "01")[(1, 0)], "edhase")

    def test_but_that_slot_stays_in_reach_where_the_stem_is_not_a_final(self):
        # अत इति किम्? — 7.2.81 wants an अ-final stem, and the second
        # class has no शप् to supply one. आसाते (āsāte) and शयाते
        # (śayāte) are right as they stand and are not withheld.
        self.assertIsNone(owed_for("āsa̐", "ātām", "ātmanepada"))
        self.assertEqual(forms_of("āsa̐", "02")[(0, 1)], "āsāte")
        self.assertEqual(forms_of("śīṅ", "02")[(0, 1)], "śayāte")

    def test_and_a_gap_in_the_rules_is_a_silence_and_never_a_wrong_root(self):
        # गच्छति (gacchati) is not answered: 7.3.77 इषुगमियमां छः is
        # codified and not wired, so the engine makes गमति (gamati) from
        # गम् (gam) instead. What it must NOT do is hand गच्छति to some
        # other root — and it does not.
        self.assertEqual(roots_of("gacchati"), ())
        self.assertTrue(REGISTRY.has("7.3.77"))
        self.assertEqual([v.upadesa for v in roots_of("gamati")],
                         ["gam" + "ḷ" + "̐"])

    def test_and_a_derivation_that_did_not_finish_is_not_published(self):
        # The engine says when it stopped without converging, and a form
        # it could not finish is not a form the grammar makes.
        for entry in searchable():
            for made in paradigm(entry.upadesa, entry.code.split(".")[0]):
                self.assertEqual(made.prakriya.stopped, "no rule applies",
                                 f"{entry.code} {made.surface}")


class TheSearchSpaceIsTheDhatupatha(unittest.TestCase):
    """What is searched, and what is deliberately not."""

    def test_the_ganasutra_rows_are_not_roots(self):
        # Thirty rows of the file carry a hyphen where a root would be:
        # their text is a gaṇasūtra and lives in the companion file.
        # Nothing can be derived from them, and none is searched.
        placeholders = [d for d in load_dhatupatha().values()
                        if d.upadesa == NOT_A_ROOT]
        self.assertEqual(len(placeholders), 30)
        for entry in searchable():
            self.assertNotEqual(entry.upadesa, NOT_A_ROOT, entry.code)

    def test_and_the_space_is_now_every_root_the_dhatupatha_has(self):
        expected = [d for d in load_dhatupatha().values()
                    if d.upadesa != NOT_A_ROOT]
        self.assertEqual(list(searchable()), expected)
        self.assertEqual(len(expected), 2229)


class WhatIsNotCodifiedYet(unittest.TestCase):
    """
    The debts, written as the exact shortfall.

    Each fails the moment the thing it names is wired into the engine,
    and must then be rewritten to state the live dependency instead.
    """

    def test_the_class_markers_are_no_longer_among_them(self):
        # What this class said before: eight classes were codified as
        # rules and not as operations. All ten are operations now, and
        # the engine's own rule list is what proves it.
        engine = {rule.sutra for rule in all_rules()}
        for code, (_marker, sutra) in sorted(CLASS_MARKERS.items()):
            self.assertIn(sutra, engine, code)
            self.assertTrue(REGISTRY.has(sutra), sutra)

    def test_but_three_rules_one_atmanepada_slot_wants_are_still_owed(self):
        # 7.2.81 आतो ङितः, then 6.1.66 लोपो व्योर्वलि on the य् it
        # leaves, then 6.1.87 आद्गुणः: that is पचेते (pacete) from
        # पच + अ + आते. All three are registered; none is an operation.
        engine = {rule.sutra for rule in all_rules()}
        for sutra in ("7.2.81", "6.1.66", "6.1.87"):
            self.assertTrue(REGISTRY.has(sutra), sutra)
            self.assertNotIn(sutra, engine, sutra)

    def test_and_four_more_that_particular_words_want(self):
        # Each is codified, none is wired, and each is named by the word
        # it would make:
        #   7.3.77 इषुगमियमां छः     गच्छति, where the engine has गमति
        #   7.1.6  शीङो रुट्          शेरते, where it has शयते
        #   8.3.59 आदेशप्रत्यययोः    एषि, where it has एसि
        #   7.3.36 अर्तिह्रीव्लीरी…   जापयति, where it has जाययति
        engine = {rule.sutra for rule in all_rules()}
        owed = {"7.3.77": "gacchati", "7.1.6": "śerate",
                "8.3.59": "eṣi", "7.3.36": "jāpayati"}
        for sutra, form in owed.items():
            self.assertTrue(REGISTRY.has(sutra), sutra)
            self.assertNotIn(sutra, engine, sutra)
            self.assertEqual(roots_of(form), (), form)

    def test_and_one_optional_rule_leaves_a_form_unsimplified(self):
        # 8.4.65 झरो झरि सवर्णे would drop the द् of रुन्द्धः and give
        # रुन्धः, which is the vṛtti's own form under 6.4.111. The rule
        # is optional, so what the engine has is the other reading and
        # not an error — but the simpler one is what the books print.
        self.assertTrue(REGISTRY.has("8.4.65"))
        self.assertNotIn("8.4.65", {rule.sutra for rule in all_rules()})
        self.assertEqual(forms_of(_entry("07.0001").upadesa, "07")[(0, 1)],
                         "runddhaḥ")

    def test_and_no_preverb_is_handled_yet(self):
        # प्रणयति (praṇayati) is नयति (nayati) with प्र (pra) in front
        # and 8.4.14's ण् (ṇ) — codified rules the engine does not apply
        # in sequence. The search answers for the bare verb only.
        self.assertEqual(roots_of("praṇayati"), ())
        for sutra in ("1.4.59", "8.4.14"):
            self.assertTrue(REGISTRY.has(sutra), sutra)

    def test_and_only_one_of_the_ten_lakaras_is_derived(self):
        # लट् (laṭ). 3.2.123 वर्तमाने लट् is registered, and so are the
        # other nine tenses; the engine builds forms for this one.
        self.assertTrue(REGISTRY.has("3.2.123"))
        self.assertEqual(roots_of("ajayat"), ())      # लङ् (laṅ)
        self.assertEqual(roots_of("jeṣyati"), ())     # लृट् (lṛṭ)


class BothDirectionsFromOneCommand(unittest.TestCase):
    """`python -m src.astadhyayi.vyutpatti <word>`, told apart by the word."""

    def _run(self, *words) -> str:
        buffer = io.StringIO()
        with contextlib.redirect_stdout(buffer):
            self.assertEqual(main(list(words)), 0)
        return buffer.getvalue()

    def test_a_root_is_conjugated_and_a_word_is_traced(self):
        forward = self._run("ji")
        self.assertIn("jayati", forward)
        self.assertIn("जयामः", forward)
        backward = self._run("जयति")
        self.assertIn("01.0642", backward)
        self.assertIn("कर्तरि शप्", backward)

    def test_and_a_word_is_not_mistaken_for_a_root(self):
        # जयति (jayati) is not in the dhātupāṭha, and the engine would
        # cheerfully conjugate it — जयतयति (jayatayati) — if it were not
        # asked. The corpus is what says what a root is.
        out = self._run("जयति")
        self.assertNotIn("jayatayati", out)
        self.assertIn("derivation", out)

    def test_and_a_word_no_root_makes_says_so(self):
        out = self._run("gacchati")
        self.assertIn("no root in reach", out)

    def test_and_every_line_that_shows_a_form_shows_both_scripts(self):
        # The convention the whole codification keeps: no roman alone.
        seen = 0
        for line in self._run("ji").splitlines():
            for roman in re.findall(r"\(([^)]*)\)", line):
                self.assertIn(iast_to_devanagari(roman), line, line)
                seen += 1
        # the root and the लकार on the heading line, then nine forms
        self.assertEqual(seen, 11)


if __name__ == "__main__":
    unittest.main()
