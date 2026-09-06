# -*- coding: utf-8 -*-
"""
जि (ji) → जयति (jayati), and जयति (jayati) → जि (ji).

Two questions that look like one question asked twice, and are not. The
first is what the Aṣṭādhyāyī answers: eight rules, in order, each naming
itself. The second the Aṣṭādhyāyī does not answer at all — there is no
rule that takes an affix off a word — so it is answered by making every
verb the grammar makes and seeing which making produced this one.

The tests are in that order, and the second half is mostly about the
honesty of a search: that the filter which makes it cheap loses nothing
(checked over every form in reach, not on a sample), that what the engine
cannot build is named rather than silently missing, and that where the
grammar itself gives two answers, two answers come back.
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
from src.normalizer import iast_to_devanagari
from src.astadhyayi.vibhakti import NUMBERS, PERSONS
from src.astadhyayi.vikarana import CLASS_MARKERS, marker_of_class
from src.astadhyayi.vyutpatti import (
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
import src.astadhyayi.rules  # noqa: F401  (populates REGISTRY)


#: 01.0642 जि जये — "to win". The entry this whole file is about.
JI = "01.0642"
#: 01.1096 जि अभिभवे — spelt the same, read again, a different sense.
JI_AGAIN = "01.1096"


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

    def test_and_each_of_those_four_is_a_registered_sutra(self):
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
        # 10.0324 जि भाषायाम् is also spelt जि. It takes णिच् (ṇic) by
        # 3.1.25 and gives जापयति (jāpayati), not जयति — so it must not
        # appear here, and it does not, because the tenth class is out of
        # reach and the search never asked it.
        self.assertNotIn("10.0324", [v.code for v in roots_of("jayati")])
        self.assertFalse(in_reach("10"))
        self.assertEqual(marker_of_class("10"), ("ṇic", "3.1.25"))
        self.assertTrue(REGISTRY.has("3.1.25"))


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
        # Asked with the bare name both would elide and both would be
        # अत्ति — which is why the derivation carries the upadeśa.
        self.assertEqual([v.code for v in roots_of("adati")], ["01.0064"])
        self.assertEqual([v.code for v in roots_of("atti")], ["02.0001"])
        self.assertEqual(verb("ada̐").terms[0].enunciated, "ada̐")

    def test_and_the_second_class_is_the_one_where_that_shows(self):
        # अद् (ad) has no शप् at all, and its whole paradigm shows it.
        self.assertEqual(forms_of("ada̐"), {
            (0, 0): "atti", (0, 1): "attaḥ", (0, 2): "adanti",
            (1, 0): "atsi", (1, 1): "atthaḥ", (1, 2): "attha",
            (2, 0): "admi", (2, 1): "advaḥ", (2, 2): "admaḥ",
        })
        self.assertEqual(marker_of_class("02"), ("luk", "2.4.72"))


class TheFilterLosesNothing(unittest.TestCase):
    """
    The search is cheap because it only tries roots that open on the
    word's own sound. That is a claim about every derivation the engine
    can perform, so it is checked against every derivation the engine
    can perform, and not on a sample.
    """

    def test_a_word_is_looked_for_under_its_first_sound(self):
        self.assertEqual(opening("jayati"), "j")
        self.assertEqual(root_opening("ji"), "j")
        self.assertIn(load_dhatupatha()[JI], candidates("jayati"))

    def test_and_an_aspirate_counts_as_one_sound(self):
        self.assertEqual(opening("bhavati"), "bh")
        self.assertEqual(root_opening("bhū"), "bh")
        self.assertNotIn(load_dhatupatha()["01.0001"], candidates("bavati"))

    def test_and_a_root_written_with_a_cerebral_is_filed_under_the_plain(self):
        # णीञ् (ṇīñ) opens on ण् and नयति (nayati) on न्. 6.1.64/65 is
        # asked for that, not guessed at.
        self.assertEqual(root_opening("ṇīñ"), "n")
        self.assertEqual(root_opening("ṣaha̐"), "s")
        self.assertIn(load_dhatupatha()["01.1049"], candidates("nayati"))

    def test_and_a_root_whose_opening_is_a_mark_is_filed_under_what_is_left(self):
        # डुपचँष् (ḍupacaṣ) opens on ड् only until 1.3.5 आदिर्ञिटुडवः
        # has taken डु away. It belongs under प् (p).
        self.assertEqual(root_opening("ḍupaca̐ṣ"), "p")
        self.assertEqual(root_opening("ḍukṛñ"), "k")

    def test_and_every_vowel_initial_root_is_searched_together(self):
        # गुण (guṇa) by 7.3.84 and 6.1.78 both act on a root's own vowel,
        # so the opening of a vowel-initial root is the one thing a लट्
        # derivation can move: इ (i) becomes ए (e) becomes अय् (ay).
        self.assertEqual(root_opening("edha̐"), VOWEL_BUCKET)
        self.assertEqual(opening("edhate"), VOWEL_BUCKET)
        self.assertEqual(opening("atti"), VOWEL_BUCKET)

    def test_and_no_form_in_reach_falls_outside_its_own_roots_bucket(self):
        # The exhaustive check. Every root the search covers, every slot
        # of its paradigm: the word must be findable where its root was
        # filed, or the filter would be quietly dropping right answers.
        for entry in searchable():
            bucket = root_opening(entry.upadesa)
            for made in paradigm(entry.upadesa):
                self.assertEqual(opening(made.surface), bucket,
                                 f"{entry.code} {entry.upadesa} → "
                                 f"{made.surface}")

    def test_and_the_true_root_is_always_among_the_candidates_tried(self):
        for entry in searchable():
            for made in paradigm(entry.upadesa):
                self.assertIn(entry, candidates(made.surface),
                              f"{entry.code} → {made.surface}")


class WhatIsOutOfReachIsNamedNotSilent(unittest.TestCase):
    """A word the search cannot answer for, and the sūtra that is why."""

    def test_the_sixth_class_is_out_of_reach_and_says_which_rule_it_wants(self):
        # तुदति (tudati) gets no answer. Not because तुद् (tud) is
        # unknown — it is in the dhātupāṭha — but because 3.1.77
        # तुदादिभ्यः शः gives it श (śa) and not शप् (śap), and the engine
        # has no rule for श. Deriving it with शप् would make तोदति
        # (todati), which is not a word, so it is not derived at all.
        self.assertEqual(roots_of("tudati"), ())
        self.assertIn(("06", "śa", "3.1.77"), unreachable())
        self.assertTrue(REGISTRY.has("3.1.77"))

    def test_and_the_reach_is_read_off_the_engine_not_written_down_here(self):
        # Two classes today, and the list is a consequence rather than a
        # decision: a class is in reach exactly when the engine applies
        # the sūtra that gives its marker.
        engine = {rule.sutra for rule in all_rules()}
        self.assertEqual(
            IN_REACH,
            frozenset(code for code, (_m, sutra) in CLASS_MARKERS.items()
                      if sutra in engine))
        self.assertEqual(sorted(IN_REACH), ["01", "02"])
        self.assertIn("3.1.68", engine)
        self.assertNotIn("3.1.77", engine)

    def test_and_every_class_the_dhatupatha_uses_is_accounted_for(self):
        used = {code.split(".")[0] for code in load_dhatupatha()}
        self.assertEqual(used, set(CLASS_MARKERS))
        self.assertEqual(
            used, IN_REACH | {code for code, _g, _s in unreachable()})

    def test_and_one_slot_can_be_out_of_reach_while_its_paradigm_is_in(self):
        # 7.2.81 आतो ङितः turns the आ (ā) of आताम् (ātām) into इय् (iy)
        # after an अ-final stem: पचेते (pacete), एधेते (edhete). The
        # engine has not got it, so those two slots are withheld — the
        # other seven of एध (edha) are answered.
        self.assertEqual(owed_for("edha̐", "ātām", "ātmanepada"),
                         ("iy", "7.2.81"))
        self.assertTrue(REGISTRY.has("7.2.81"))
        held = {(m.person, m.number) for m in paradigm("edha̐")}
        self.assertEqual(set(SLOTS) - held, {(0, 1), (1, 1)})
        self.assertEqual(forms_of("edha̐")[(0, 0)], "edhate")
        self.assertEqual(forms_of("edha̐")[(1, 0)], "edhase")

    def test_but_that_slot_stays_in_reach_where_the_stem_is_not_a_final(self):
        # अत इति किम्? — 7.2.81 wants an अ-final stem, and the second
        # class has no शप् to supply one. आसाते (āsāte) and शयाते
        # (śayāte) are right as they stand and are not withheld.
        self.assertIsNone(owed_for("āsa̐", "ātām", "ātmanepada"))
        self.assertEqual(forms_of("āsa̐")[(0, 1)], "āsāte")
        self.assertEqual(forms_of("śīṅ")[(0, 1)], "śayāte")

    def test_and_a_gap_in_the_rules_is_a_silence_and_never_a_wrong_root(self):
        # गच्छति (gacchati) is not answered: 7.3.77 इषुगमियमां छः is
        # codified and not wired, so the engine makes गमति (gamati) from
        # गम् (gam) instead. What it must NOT do is hand गच्छति to some
        # other root — and it does not.
        self.assertEqual(roots_of("gacchati"), ())
        self.assertTrue(REGISTRY.has("7.3.77"))
        self.assertEqual([v.upadesa for v in roots_of("gamati")],
                         ["gam" + "ḷ" + "̐"])


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

    def test_and_the_space_is_every_entry_of_the_classes_in_reach(self):
        expected = [d for d in load_dhatupatha().values()
                    if d.upadesa != NOT_A_ROOT
                    and d.code.split(".")[0] in IN_REACH]
        self.assertEqual(list(searchable()), expected)
        self.assertGreater(len(expected), 1000)

    def test_and_a_derivation_that_did_not_finish_is_not_published(self):
        # The engine says when it stopped without converging, and a form
        # it could not finish is not a form the grammar makes.
        for entry in searchable():
            for made in paradigm(entry.upadesa):
                self.assertEqual(made.prakriya.stopped, "no rule applies",
                                 f"{entry.code} {made.surface}")


class WhatIsNotCodifiedYet(unittest.TestCase):
    """
    The debts, written as the exact shortfall.

    Each fails the moment the thing it names is wired into the engine,
    and must then be rewritten to state the live dependency instead.
    """

    def test_eight_classes_are_codified_as_rules_and_not_yet_as_operations(self):
        # Every one of the eight has a registered sūtra saying which
        # marker it takes. None of the eight has an operational rule in
        # the engine that puts that marker into a form. That is the
        # whole distance between a codification and a derivation.
        for code, _marker, sutra in unreachable():
            self.assertTrue(REGISTRY.has(sutra), sutra)
            self.assertNotIn(sutra, {r.sutra for r in all_rules()}, code)
        self.assertEqual(len(unreachable()), 8)

    def test_and_the_three_rules_one_atmanepada_slot_wants_are_the_same(self):
        # 7.2.81 आतो ङितः, then 6.1.66 लोपो व्योर्वलि on the य् it
        # leaves, then 6.1.87 आद्गुणः: that is पचेते (pacete) from
        # पच + अ + आते. All three are registered; none is an operation.
        engine = {rule.sutra for rule in all_rules()}
        for sutra in ("7.2.81", "6.1.66", "6.1.87"):
            self.assertTrue(REGISTRY.has(sutra), sutra)
            self.assertNotIn(sutra, engine, sutra)

    def test_and_no_preverb_is_handled_yet(self):
        # प्रणयति (praṇayati) is नयति (nayati) with प्र (pra) in front
        # and 8.4.14's ण् (ṇ) — three codified rules the engine does not
        # apply in sequence. The search answers for the bare verb only.
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

    def test_and_a_word_out_of_reach_says_which_rules_are_missing(self):
        out = self._run("tudati")
        self.assertIn("no root in reach", out)
        self.assertIn("3.1.77", out)

    def test_and_every_line_that_shows_a_form_shows_both_scripts(self):
        # The convention the whole codification keeps: no roman alone.
        # Every parenthesised IAST on a line must have its Devanāgarī
        # standing beside it on the same line.
        seen = 0
        for line in self._run("ji").splitlines():
            for roman in re.findall(r"\(([^)]*)\)", line):
                self.assertIn(iast_to_devanagari(roman), line, line)
                seen += 1
        # the root and the लकार on the heading line, then nine forms
        self.assertEqual(seen, 11)


if __name__ == "__main__":
    unittest.main()
