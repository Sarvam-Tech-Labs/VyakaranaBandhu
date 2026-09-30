# -*- coding: utf-8 -*-
"""
The sandhi engine's core — what it consults, not what it knows.

The rules of each family are tested in `test_sandhi_<family>.py`. This file
tests the machinery underneath them, and it does so with the derivations the
tradition itself uses to *argue* about ordering, because those are the cases a
plain string-rewriting engine gets wrong and a faithful one cannot:

  * **वाक्पतिः** — 8.2.30, 8.2.39 and 8.4.55 turn च् to क् to ग् to क्. Let 8.2.39
    look again at the क् that 8.4.55 made and it turns it back for ever.
  * **हर इह** — 8.3.19 drops a य् and leaves two vowels side by side, and 6.1.87
    does NOT join them, because the loss is asiddha to it (8.2.1).
  * **मनोरथः** — रु before र् is open to 6.1.114 and 8.3.14; the second is later
    and the Laghusiddhāntakaumudī settles it by *पूर्वत्रासिद्धम्*.
  * **पुना रमते** — 6.3.111 names the loss 8.3.14 makes, so 8.2.1 may not hide it.
  * **प्रश्नः** — 8.4.44 changes nothing and is still a step: it refuses 8.4.40.

A test that cannot fail is worse than no test (NORTH_STAR §3), so where a
result could come out right by luck the test also asserts the *steps*.
"""

from __future__ import annotations

import unittest
from dataclasses import replace

from src.astadhyayi import corpus
from src.astadhyayi.anga import yan_sandhi
from src.astadhyayi.sandhi import SandhiInputError, rulebook, sandhi, trace
from src.astadhyayi.sandhi.engine import Outcome
from src.astadhyayi.sandhi.parse import parse, to_iast, tokenize
from src.astadhyayi.sandhi.segs import (
    ANGA, AVASANA, PADA, RU, SAMASA, UPASARGA, Seg, State, View, Word)
from src.astadhyayi.varna import SVARA


def steps_of(text, **kw):
    """The sūtras of the first derivation, in order."""
    return [s.sutra for s in sandhi(text, **kw).outcomes[0].steps
            if not s.declined]


def surfaces(text, **kw):
    return set(sandhi(text, **kw).surfaces)


class Ordering8_2_1(unittest.TestCase):
    """What a rule is entitled to see."""

    def test_the_vakpati_chain_does_not_cycle(self):
        r = sandhi("vāc pati")
        self.assertEqual(r.surfaces, ("vākpati",))
        self.assertEqual(steps_of("vāc pati"), ["8.2.30", "8.2.39", "8.4.55"])
        self.assertEqual(r.outcomes[0].stopped, "no rule applies")

    def test_a_loss_that_is_asiddha_does_not_let_the_vowels_join(self):
        """हर इह: the loss of the य् is invisible to 6.1.87."""
        both = sandhi("haras iha")
        self.assertEqual(set(both.surfaces), {"haraiha", "harayiha"})
        lost = next(o for o in both.outcomes
                    if "8.3.19" in [s.sutra for s in o.steps
                                    if not s.declined])
        self.assertEqual(lost.text(), "hara iha")
        self.assertNotIn("6.1.87", [s.sutra for s in lost.steps])

    def test_that_same_pair_joins_where_no_loss_intervenes(self):
        """The control: with no रु there is no loss, so 6.1.87 acts."""
        self.assertEqual(surfaces("hara iha"), {"hareha"})
        self.assertIn("6.1.87", steps_of("hara iha"))

    def test_a_sapada_rule_beats_a_later_tripadi_rule_for_one_sound(self):
        """मनोरथः — 6.1.114 against 8.3.14, decided by 8.2.1."""
        self.assertEqual(surfaces("manas ratha"), {"manoratha"})
        self.assertEqual(steps_of("manas ratha"),
                         ["8.2.66", "6.1.114", "6.1.87"])

    def test_a_rule_that_names_a_tripadi_product_may_see_it(self):
        """8.2.66's रु is read by 6.1.113 — वचनप्रामाण्यात्."""
        self.assertEqual(surfaces("rāmas atra"), {"rāmo'tra"})
        self.assertEqual(steps_of("rāmas atra"),
                         ["8.2.66", "6.1.113", "6.1.87", "6.1.109"])

    def test_without_consumes_the_same_rule_goes_blind(self):
        """Take `consumes` away and 6.1.113 can no longer act: the rule is
        exactly as blind as 8.2.1 says, and the declaration is what lets it
        see."""
        rules = tuple(
            replace(r, consumes=frozenset()) if r.sutra == "6.1.113" else r
            for r in rulebook.all_rules())
        start = parse("rāmas atra")
        from src.astadhyayi.sandhi.engine import derive
        outcome = derive(start, rules)[0]
        self.assertNotIn("6.1.113", [s.sutra for s in outcome.steps])
        self.assertNotEqual(outcome.surface, "rāmo'tra")

    def test_a_loss_can_be_named_by_a_sapada_rule(self):
        """पुना रमते — 6.3.111 reads the र् that 8.3.14 lost."""
        self.assertEqual(surfaces("punar ramate"), {"punāramate"})
        self.assertEqual(steps_of("punar ramate"), ["8.3.14", "6.3.111"])
        self.assertEqual(surfaces("haris ramyaḥ"), {"harīramyaḥ"})

    def test_the_full_visarga_chain_in_order(self):
        self.assertEqual(steps_of("rāmas ca"),
                         ["8.2.66", "8.3.15", "8.3.34", "8.4.40"])
        self.assertEqual(surfaces("rāmas ca"), {"rāmaśca"})

    def test_a_rule_earlier_in_the_tripadi_never_sees_a_later_rule_s_work(self):
        """After 8.4.55 has hardened the ग्, 8.2.39 must still see a ग्."""
        state = parse("vāc pati")
        from src.astadhyayi.sandhi.engine import apply, collect
        rules = rulebook.all_rules()
        seen = []
        for _ in range(6):
            found = collect(state, rules)
            if not found:
                break
            rule, app = min(found, key=lambda ra: ra[0].order)
            state = apply(state, rule, app)
            seen.append(rule.sutra)
        self.assertEqual(seen, ["8.2.30", "8.2.39", "8.4.55"])
        final = next(s for s in state.segs if s.made_by == "8.4.55")
        self.assertEqual(final.s, "k")
        early = View(state, "8.2.39")
        self.assertEqual(
            [x.s for x in early.live if x.w == 0][-1], "g",
            "8.2.39 must see the ग् 8.2.39 itself made, not the क् of 8.4.55")
        earliest = View(state, "8.2.30")
        self.assertEqual([x.s for x in earliest.live if x.w == 0][-1], "k")


class ChainedSubstitutes(unittest.TestCase):
    """A substitute that has joined two words and then a third belongs to all
    three, or the first word's earlier sounds look like the end of the word."""

    def test_a_chain_of_joins_does_not_strand_the_first_word(self):
        """सa + a + i: 6.1.101 then 6.1.87 — the स् must not become a
        pada-final स् for 8.2.66, which would leave a रु in the result."""
        out = sandhi("sa a i").outcomes[0]
        self.assertEqual(out.surface, "se")
        self.assertNotIn("8.2.66", [s.sutra for s in out.steps])
        self.assertEqual([s.sutra for s in out.steps], ["6.1.101", "6.1.87"])

    def test_the_words_of_a_chained_substitute_are_a_range(self):
        from src.astadhyayi.sandhi.segs import _words
        state = parse("sa a i")
        from src.astadhyayi.sandhi.engine import apply, collect
        rules = rulebook.all_rules()
        for _ in range(2):
            rule, app = min(collect(state, rules), key=lambda ra: ra[0].order)
            state = apply(state, rule, app)
        merged = next(s for s in state.segs if s.made_by == "6.1.87")
        self.assertEqual(_words(merged), frozenset({0, 1, 2}))

    def test_a_ru_nothing_resolves_is_printed_as_the_r_it_is(self):
        """अग्निर् अत्र: no rule turns this रु into anything, and the उ is an इत्."""
        out = sandhi("agnis atra").outcomes[0]
        self.assertEqual(out.surface, "agniratra")
        self.assertNotIn("ru", out.text())
        self.assertEqual(out.text(), "agnir atra")

    def test_but_while_the_derivation_runs_the_ru_is_shown(self):
        out = sandhi("agnis atra").outcomes[0]
        self.assertIn("agniru atra", out.steps[0].after)


class Units(unittest.TestCase):
    """The run of pieces a rule about a pada's inside may look across."""

    def _view(self, spec):
        return View(parse(spec), "8.4.1")

    def test_pieces_joined_within_one_pada_are_one_unit(self):
        v = self._view("rāma~ena")
        first = v.live[0]
        self.assertEqual("".join(s.s for s in v.unit_of(first)), "rāmaena")
        self.assertTrue(v.joined_pada(first))

    def test_two_padas_are_two_units(self):
        v = self._view("rāma ena")
        self.assertEqual("".join(s.s for s in v.unit_of(v.live[0])), "rāma")
        self.assertFalse(v.joined_pada(v.live[0]))

    def test_a_chosen_kind_of_boundary_can_be_crossed(self):
        v = self._view("pra|nayati")
        from src.astadhyayi.sandhi.segs import UPASARGA
        self.assertEqual(
            "".join(s.s for s in v.unit_of(v.live[0], across=(UPASARGA,))),
            "pranayati")
        self.assertEqual("".join(s.s for s in v.unit_of(v.live[0])), "pra")

    def test_a_finished_word_is_its_own_unit_and_its_interior_is_not_offered(self):
        v = self._view("gacchati")
        self.assertFalse(v.joined_pada(v.live[0]))
        self.assertEqual(v.pairs(), [])


class SightAndVisibility(unittest.TestCase):
    """`View`, in isolation from any rule."""

    def _state(self):
        base = parse("ka ta", pause=False)
        return base

    def test_an_original_sound_is_visible_to_everyone(self):
        state = self._state()
        for rule in ("1.1.1", "6.1.77", "8.4.68"):
            self.assertEqual(
                "".join(s.s for s in View(state, rule).live), "kata")

    def test_a_tripadi_product_is_hidden_from_an_earlier_rule_only(self):
        state = self._state()
        old = state.segs[-1]                       # the final a
        made = Seg(uid=99, s="ā", w=old.w, made_by="8.3.15", prior=(old,))
        state = replace(state, segs=state.segs[:-1] + (made,))
        self.assertEqual(View(state, "8.4.40").live[-1].s, "ā")
        self.assertEqual(View(state, "8.3.15").live[-1].s, "ā")
        early = View(state, "8.2.39").live[-1]
        self.assertEqual(early.s, "a")
        self.assertTrue(early.through)

    def test_a_sapada_product_is_visible_to_a_rule_that_stands_before_it(self):
        """8.2.1 hides only the tripādī. 6.1.101 is later than 6.1.77 and
        is not hidden from it, nor it from 6.1.101."""
        state = self._state()
        old = state.segs[-1]
        made = Seg(uid=99, s="ā", w=old.w, made_by="6.1.101", prior=(old,))
        state = replace(state, segs=state.segs[:-1] + (made,))
        self.assertEqual(View(state, "6.1.77").live[-1].s, "ā")

    def test_a_rule_cannot_edit_what_it_sees_only_through_its_past(self):
        state = self._state()
        old = state.segs[-1]
        made = Seg(uid=99, s="ā", w=old.w, made_by="8.3.15", prior=(old,))
        state = replace(state, segs=state.segs[:-1] + (made,))
        sight = View(state, "8.2.39").live[-1]
        from src.astadhyayi.sandhi.rule import replace as edit_replace
        self.assertTrue(edit_replace(sight, "x").hidden)

    def test_an_insertion_is_invisible_to_earlier_rules(self):
        state = self._state()
        inserted = Seg(uid=99, s="t", w=0, made_by="8.3.31", prior=())
        state = replace(state, segs=(state.segs[0], inserted) + state.segs[1:])
        self.assertEqual("".join(s.s for s in View(state, "8.4.40").live),
                         "ktaa"[:0] + "kata"[:1] + "t" + "ata")
        self.assertEqual("".join(s.s for s in View(state, "8.2.30").live),
                         "kata")

    def test_a_loss_is_kept_as_an_empty_sound(self):
        state = self._state()
        gone = Seg(uid=99, s="", w=1, made_by="8.3.19", prior=(state.segs[-1],))
        state = replace(state, segs=state.segs[:-1] + (gone,))
        self.assertEqual("".join(s.s for s in View(state, "8.4.40").live),
                         "kat")
        self.assertEqual("".join(s.s for s in View(state, "6.1.87").live),
                         "kata")


class Refusals(unittest.TestCase):
    """A rule that changes nothing is still a step."""

    def test_a_prohibition_is_cited_and_stops_the_rule_it_refuses(self):
        r = sandhi("praś~na")
        out = r.outcomes[0]
        self.assertEqual(out.surface, "praśna")
        self.assertIn("8.4.44", [s.sutra for s in out.steps])
        self.assertNotIn("8.4.40", [s.sutra for s in out.steps])
        step = next(s for s in out.steps if s.sutra == "8.4.44")
        self.assertEqual(step.detail.kind, "pratiṣedha")
        self.assertEqual(step.before, step.after)
        self.assertIn("8.4.40", [a.sutra for a in step.against])

    def test_the_rule_it_refuses_still_works_elsewhere(self):
        self.assertEqual(surfaces("yaj~na"), {"yajña"})

    def test_a_refusal_is_not_repeated(self):
        out = sandhi("praś~na").outcomes[0]
        self.assertEqual(
            [s.sutra for s in out.steps].count("8.4.44"), 1)


class Options(unittest.TestCase):
    """A विभाषा is not a coin toss: both courses are returned."""

    def test_an_optional_rule_gives_two_derivations(self):
        r = sandhi("haras iha")
        self.assertEqual(len(r.outcomes), 2)
        self.assertEqual(r.outcomes[0].choices[-1], ("8.3.19", True))
        self.assertEqual(r.outcomes[1].choices[-1], ("8.3.19", False))

    def test_the_declined_course_says_it_declined(self):
        refused = sandhi("haras iha").outcomes[1]
        declined = [s for s in refused.steps if s.declined]
        self.assertEqual([s.sutra for s in declined], ["8.3.19"])
        self.assertEqual(declined[0].before, declined[0].after)

    def test_the_taken_option_comes_first(self):
        self.assertEqual(sandhi("haras iha").surfaces[0], "haraiha")

    def test_options_are_capped_and_the_cap_is_honoured(self):
        from src.astadhyayi.sandhi.engine import derive
        start = parse("haras iha")
        self.assertEqual(len(derive(start, rulebook.all_rules(),
                                    max_outcomes=1)), 1)


class Substitutes(unittest.TestCase):
    """Chosen by the grammar's own rules, not written in a table."""

    def test_the_sandhi_of_alike_vowels_beats_yan_by_1_4_2(self):
        """इ + इ: 6.1.77 and 6.1.101 both reach it; the later is done."""
        out = sandhi("agni indra").outcomes[0]
        self.assertEqual(out.surface, "agnīndra")
        step = out.steps[0]
        self.assertEqual(step.sutra, "6.1.101")
        self.assertIn("6.1.77", [a.sutra for a in step.against])
        self.assertTrue(any("1.4.2" in a.why for a in step.against))

    def test_vrddhi_is_the_exception_to_guna(self):
        out = sandhi("kṛṣṇa aikya").outcomes[0]
        self.assertEqual(out.surface, "kṛṣṇaikya")
        self.assertEqual(out.steps[0].sutra, "6.1.88")
        self.assertIn("6.1.87", [a.sutra for a in out.steps[0].against])

    def test_purvarupa_is_written_as_the_tradition_writes_it(self):
        out = sandhi("hare ava").outcomes[0]
        self.assertEqual(out.surface, "hare'va")
        self.assertEqual(out.text(), "hare 'va")

    def test_r_takes_its_r_from_1_1_51(self):
        self.assertEqual(surfaces("mahā ṛṣi"), {"maharṣi"})

    def test_a_substitute_of_two_sounds_is_not_a_pada_final_r(self):
        """महर्षि: 6.1.85 does not make the र् of अर् pada-final for a rule that
        rests on the sound itself, or 8.3.15 would make it महःषि."""
        self.assertNotIn("8.3.15", steps_of("mahā ṛṣi"))

    def test_the_yan_of_each_ik_agrees_with_the_projects_own_codification(self):
        """`anga.yan_sandhi` is 6.1.77 codified as a question; the engine's
        6.1.77 is the same sūtra as a step. Where the first answers, the
        second must give the same sound."""
        checked = 0
        for ik in ("i", "ī", "u", "ū", "ṛ", "ṝ", "ḷ"):
            for vowel in ("a", "ā", "e", "ai", "o", "au", "u", "i", "ṛ"):
                expected = yan_sandhi(ik, vowel).result
                if expected is None:
                    continue
                out = sandhi(f"ka{ik} {vowel}kha".replace("ka" + ik, ik)
                             if False else f"{ik} {vowel}").outcomes[0]
                first = out.steps[0]
                self.assertEqual(first.sutra, "6.1.77", (ik, vowel))
                self.assertEqual(first.detail.adesa, expected, (ik, vowel))
                checked += 1
        self.assertGreater(checked, 30)

    def test_the_substitute_is_not_a_literal_in_the_source(self):
        """No family module may write the pairing i→y as a table."""
        import pathlib
        for path in pathlib.Path("src/astadhyayi/sandhi").rglob("*.py"):
            text = path.read_text(encoding="utf-8")
            for pair in ('"i": "y"', "'i': 'y'", '"u": "v"', "'u': 'v'",
                         '"i": "e"', "'i': 'e'"):
                self.assertNotIn(pair, text, f"{path} tabulates the answer")


class Interior(unittest.TestCase):
    """The engine acts at junctions; the inside of a finished word is left."""

    def test_the_cch_of_gacchati_is_not_touched(self):
        for out in sandhi("rāmas gacchati").outcomes:
            self.assertIn("gacchati", out.surface)

    def test_but_a_junction_inside_a_word_is_worked(self):
        self.assertEqual(surfaces("ne~a"), {"naya"})
        self.assertEqual(steps_of("ne~a"), ["6.1.78"])

    def test_a_pada_boundary_is_not_an_anga_boundary(self):
        """Two padas: the ए is pada-final, so 6.1.109's पूर्वरूप, not 6.1.78."""
        self.assertEqual(steps_of("ne a"), ["6.1.109"])


class Citations(unittest.TestCase):
    """Every sūtra a trace names is a sūtra, and its words come from the
    corpus — a step can never quote a sūtra wrongly."""

    CASES = ("iti ādi", "rāmas atra", "manas ratha", "punar ramate",
             "vāc pati", "tad ca", "hara iha", "praś~na", "haras iha",
             "agni indra", "mahā ṛṣi", "hare ava")

    def test_every_rule_in_the_rulebook_cites_a_real_sutra(self):
        self.assertEqual(rulebook.problems(), [])

    def test_every_sutra_named_in_any_step_exists(self):
        known = corpus.load_vidyut_sutrapatha()
        for text in self.CASES:
            for outcome in sandhi(text).outcomes:
                for step in outcome.steps:
                    for sutra in step.sutras:
                        self.assertIn(sutra, known, (text, sutra))
                    for lost in step.against:
                        self.assertIn(lost.sutra, known, (text, lost.sutra))

    def test_the_quoted_words_are_the_corpus_words(self):
        known = corpus.load_vidyut_sutrapatha()
        for text in self.CASES:
            for outcome in sandhi(text).outcomes:
                for step in trace_steps(outcome):
                    self.assertEqual(step["sutra_iast"],
                                     known[step["sutra"]].text)
                    for via in step["via"]:
                        self.assertEqual(via["text_iast"],
                                         known[via["sutra"]].text)

    def test_the_trace_prints_every_form_in_both_scripts(self):
        out = sandhi("iti ādi").trace()
        self.assertIn("इत्यादि (ityādi)", out)
        self.assertIn("इको यणचि (iko yaṇaci)", out)
        self.assertIn("तस्मिन्निति निर्दिष्टे पूर्वस्य", out)   # the real text

    def test_the_result_serialises(self):
        import json
        json.dumps(sandhi("haras iha").to_dict(), ensure_ascii=False)


def trace_steps(outcome):
    return trace.outcome_dict(outcome)["steps"]


class Input(unittest.TestCase):

    def test_devanagari_and_iast_give_the_same_derivation(self):
        self.assertEqual(sandhi("इति आदि").surface, sandhi("iti ādi").surface)
        self.assertEqual(steps_of("रामस् च"), steps_of("rāmas ca"))

    def test_plus_and_space_are_the_same_boundary(self):
        self.assertEqual(sandhi("iti+ādi").surface, "ityādi")

    def test_the_boundary_kind_is_read_from_the_separator(self):
        self.assertEqual(parse("deva-indra").bounds, (SAMASA, AVASANA))
        self.assertEqual(parse("pra|ejate").bounds, (UPASARGA, AVASANA))
        self.assertEqual(parse("ne~a").bounds, (ANGA, AVASANA))
        self.assertEqual(parse("iti ādi", pause=False).bounds[-1], "open")

    def test_flags_are_read_from_braces(self):
        word = parse("harī{dvivacana} etau").words[0]
        self.assertTrue(word.has("dvivacana"))
        self.assertEqual(word.text, "harī")

    def test_a_candrabindu_stays_on_its_vowel(self):
        self.assertEqual(tokenize("sa̐"), [("s", False), ("a", True)])
        state = parse("सँ")
        self.assertTrue(state.segs[-1].nasal)
        self.assertEqual([s.s for s in state.segs], ["s", "a"])

    def test_an_avagraha_in_the_input_is_refused_with_a_reason(self):
        with self.assertRaises(SandhiInputError) as ctx:
            sandhi("hare 'va")
        self.assertIn("already joined", str(ctx.exception))

    def test_an_unknown_letter_is_refused_and_named(self):
        with self.assertRaises(SandhiInputError) as ctx:
            sandhi("kaXa iti")
        self.assertIn("'X'", str(ctx.exception))

    def test_nothing_to_join_is_refused(self):
        with self.assertRaises(SandhiInputError):
            sandhi("   ")

    def test_an_unknown_boundary_is_refused(self):
        with self.assertRaises(SandhiInputError):
            sandhi("iti ādi", boundary="nonsense")

    def test_a_visarga_is_read_as_the_s_it_came_from_and_says_so(self):
        """रामः अत्र gives रामोऽत्र only because the visarga is a स् (8.2.66)
        for 6.1.113 — and the trace must say the reading was assumed."""
        r = sandhi("rāmaḥ atra")
        self.assertEqual(r.surface, "rāmo'tra")
        self.assertEqual(steps_of("rāmaḥ atra")[0], "8.2.66")
        self.assertTrue(any("final:s" in line
                            for line in trace.assumptions(r.outcomes[0])))
        self.assertIn("assumed for", r.trace())

    def test_a_word_that_comes_from_r_says_so_and_is_read_as_r(self):
        r = sandhi("punaḥ{final:r} atra")
        self.assertEqual(r.surface, "punaratra")
        self.assertNotIn("6.1.113", steps_of("punaḥ{final:r} atra"))

    def test_an_explicit_final_is_not_an_assumption(self):
        self.assertEqual(
            trace.assumptions(sandhi("punar atra").outcomes[0]), [])

    def test_to_iast_is_idempotent(self):
        self.assertEqual(to_iast(to_iast("रामः")), "rāmaḥ")


class Termination(unittest.TestCase):
    """Whatever two sounds meet, the engine answers — and answers with sounds."""

    FINALS = ("a", "ā", "i", "ī", "u", "ū", "ṛ", "e", "ai", "o", "au",
              "k", "g", "c", "j", "ṭ", "ḍ", "t", "d", "n", "p", "b", "m",
              "r", "s", "ś", "ṣ", "h", "y", "v", "l", "ṃ", "ḥ")
    INITIALS = ("a", "ā", "i", "ī", "u", "ṛ", "e", "ai", "o", "au",
                "k", "g", "c", "j", "ṭ", "t", "d", "n", "p", "b", "m",
                "y", "r", "l", "v", "ś", "ṣ", "s", "h")

    def test_every_meeting_of_two_sounds_terminates_cleanly(self):
        from src.astadhyayi.sandhi import trace as T
        known = corpus.load_vidyut_sutrapatha()
        inventory = set(SVARA) | {
            "k", "kh", "g", "gh", "ṅ", "c", "ch", "j", "jh", "ñ", "ṭ", "ṭh",
            "ḍ", "ḍh", "ṇ", "t", "th", "d", "dh", "n", "p", "ph", "b", "bh",
            "m", "y", "r", "l", "v", "ś", "ṣ", "s", "h", "ṃ", "ḥ", "ẖ", "ḫ",
            "'"}
        count = 0
        for final in self.FINALS:
            first = "ka" + final if final not in SVARA else "k" + final
            for initial in self.INITIALS:
                second = initial + "ta" if initial not in SVARA \
                    else initial + "ta"
                result = sandhi(f"{first} {second}")
                self.assertTrue(result.outcomes)
                for outcome in result.outcomes:
                    self.assertNotIn("cycling", outcome.stopped,
                                     (first, second))
                    self.assertNotIn("cap", outcome.stopped, (first, second))
                    for seg in outcome.final.segs:
                        self.assertIn(seg.s, inventory | {""},
                                      (first, second, seg.s))
                    for step in outcome.steps:
                        for sutra in step.sutras:
                            self.assertIn(sutra, known)
                    T.outcome_dict(outcome)           # renders without error
                count += 1
        self.assertGreater(count, 900)


if __name__ == "__main__":
    unittest.main()
