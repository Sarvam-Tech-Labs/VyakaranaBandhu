# -*- coding: utf-8 -*-
"""
Tests for the web layer — the catalogue, one sūtra's record, the dependency
graph, and running a rule from a form.

The point of the playground is that it reads each rule's signature rather than
carrying a hand-written form per sūtra. So the test that matters is the sweep:
every codified rule must produce a spec a form can fill, and the day one does
not, the sweep says which and why. Two of these also guard bugs that only
appeared over HTTP — a frozenset default that JSON could not serialise, and an
empty registry when a POST arrived before any GET.
"""

from __future__ import annotations

import json
import re
import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi import api, playground
from src.astadhyayi.glosses import GLOSSES
from src.astadhyayi.sources import facts
from src.astadhyayi.sutra import REGISTRY


class Catalogue(unittest.TestCase):

    def setUp(self):
        self.data = api.catalogue()

    def test_it_lists_everything_codified(self):
        self.assertEqual(self.data["codified"], len(REGISTRY.all()))
        self.assertEqual(len(self.data["sutras"]), self.data["codified"])
        self.assertGreater(self.data["total"], 3900)

    def test_rows_are_in_reading_order(self):
        ids = [row["id"] for row in self.data["sutras"]]
        keyed = [tuple(int(part) for part in i.split(".")) for i in ids]
        self.assertEqual(keyed, sorted(keyed))

    def test_it_knows_which_padas_are_complete(self):
        """
        Checked against the registry rather than against a list of pādas,
        which is what this was before: it named 1.1 as complete and 1.2 as
        not, and went red the day 1.2 was finished — for the best possible
        reason. What the catalogue must get right is the arithmetic.
        """
        from collections import Counter

        from src.astadhyayi.sources import all_sutra_ids

        in_corpus = Counter(sid.rsplit(".", 1)[0] for sid in all_sutra_ids())
        codified = Counter(
            f"{s.id.adhyaya}.{s.id.pada}" for s in REGISTRY.all()
        )
        expected = {
            pada for pada, total in in_corpus.items()
            if codified.get(pada, 0) == total
        }
        self.assertEqual(set(self.data["pada_complete"]), expected)
        self.assertIn("1.1", self.data["pada_complete"])

    def test_open_and_scope_flags_match_the_notes(self):
        from src.astadhyayi.report import findings

        for row in self.data["sutras"]:
            markers = {m for m, _ in findings(REGISTRY.get(row["id"]).notes)}
            self.assertEqual(row["open"], "OPEN" in markers, row["id"])
            self.assertEqual(row["scope"], "SCOPE" in markers, row["id"])

    def test_the_whole_thing_serialises(self):
        json.dumps(self.data, ensure_ascii=False)


class Detail(unittest.TestCase):

    def test_it_carries_what_the_record_holds(self):
        found = api.detail("1.1.5")
        self.assertEqual(found["devanagari"], "क्ङिति च")
        self.assertEqual(
            [p["word"] for p in found["padaccheda"]], ["क्ङिति", "च"]
        )
        self.assertEqual(
            sorted({a["from"] for a in found["anuvrtti"]}), ["1.1.3", "1.1.4"]
        )
        self.assertTrue(found["codification"])
        self.assertTrue(found["findings"])

    def test_the_case_of_each_pada_is_carried(self):
        """
        The UI outlines the three cases the paribhāṣās read, so the vibhakti
        has to travel with the word.
        """
        found = api.detail("6.1.77") if REGISTRY.has("6.1.77") else None
        found = found or api.detail("1.1.3")
        cases = {p["word"]: p["vibhakti"] for p in found["padaccheda"]}
        self.assertIn(6, cases.values())

    def test_every_codified_sutra_serialises(self):
        """
        Caught a real bug: a playground field default can be a frozenset —
        Adesa.its — and json.dumps refuses it. In-process tests passed; the
        HTTP endpoint returned an error until the defaults went through the
        serialiser.
        """
        for sutra in REGISTRY.all():
            payload = api.detail(str(sutra.id))
            try:
                json.dumps(payload, ensure_ascii=False)
            except TypeError as err:
                self.fail(f"{sutra.id} will not serialise: {err}")

    def test_sources_come_through_with_their_status(self):
        statuses = {
            s["source"]: s["status"] for s in api.detail("1.1.9")["sources"]
        }
        self.assertEqual(statuses["mūla"], "verified")
        self.assertEqual(statuses["katre"], "unreadable")
        self.assertEqual(statuses["benson"], "absent")


class Graph(unittest.TestCase):

    def test_it_shows_the_three_kinds_of_dependency_apart(self):
        found = api.graph("1.1.5")
        kinds = {edge["kind"] for edge in found["edges"]}
        self.assertIn("anuvṛtti", kinds)
        self.assertIn("related", kinds)

    def test_an_anuvrtti_edge_carries_the_word_carried(self):
        """
        Which is the whole reason to draw them differently: the reader wants
        to know WHICH word comes down, not merely that something does.
        """
        edges = [
            e for e in api.graph("1.1.5")["edges"] if e["kind"] == "anuvṛtti"
        ]
        self.assertTrue(edges)
        self.assertTrue(all(e["label"] for e in edges))
        self.assertIn("इकः", {e["label"] for e in edges})

    def test_anuvrtti_edges_point_forward_in_the_text(self):
        """A word is carried DOWN, so its source always precedes."""
        def key(sutra_id):
            return tuple(int(p) for p in sutra_id.split("."))

        for sutra in REGISTRY.all():
            for edge in api.graph(str(sutra.id))["edges"]:
                if edge["kind"] == "anuvṛtti":
                    self.assertLess(
                        key(edge["from"]), key(edge["to"]),
                        f"{edge['from']} -> {edge['to']}",
                    )

    def test_there_is_exactly_one_root(self):
        found = api.graph("1.1.5")
        roots = [n for n in found["nodes"] if n.get("root")]
        self.assertEqual(len(roots), 1)
        self.assertEqual(roots[0]["id"], "1.1.5")

    def test_one_call_reaches_the_whole_adhikara_chain(self):
        """
        What the depth control was for, and could not deliver.

        It offered 1, 2 and 3, and the test that guarded it asked only
        `assertGreaterEqual(deeper, shallower)` — which passes when depth
        does nothing whatever, and depth did nothing for 220 of the 379
        codified sūtras. The corpus's adhikāra field already lists every
        heading over a sūtra rather than the nearest one, so the first step
        of the walk arrives at the top of the chain and there is no second
        step to take.

        The property that actually matters is this one: whatever the corpus
        says stands over a sūtra is in the graph, in one call and with no
        parameter to get wrong.
        """
        for sutra in REGISTRY.all():
            sutra_id = str(sutra.id)
            found = api.graph(sutra_id)
            present = {node["id"] for node in found["nodes"]}
            for item in facts(sutra_id).adhikara:
                if item.sutra == sutra_id:
                    continue
                with self.subTest(sutra=sutra_id, heading=item.sutra):
                    self.assertIn(item.sutra, present)

    def test_an_edge_says_whether_it_touches_the_sutra_asked_about(self):
        """
        The distinction the depth control was exposing by accident. For a
        rule standing under four headings the links *between the headings*
        outnumber the ones to the rule itself — 2.1.21 has 21 against 6 —
        so the page hides them behind a toggle that says so, rather than
        behind a number that meant something different for every sūtra.
        """
        found = api.graph("2.1.21")
        cross = [e for e in found["edges"] if e["cross"]]
        direct = [e for e in found["edges"] if not e["cross"]]
        self.assertTrue(cross)
        self.assertTrue(direct)
        self.assertEqual(len(cross), found["cross_links"])
        for edge in direct:
            self.assertIn("2.1.21", (edge["from"], edge["to"]))
        for edge in cross:
            self.assertNotIn("2.1.21", (edge["from"], edge["to"]))

    def test_the_walk_terminates_on_every_codified_sutra(self):
        """
        With no depth to bound it, the guard against a cycle in the data is
        that a node already seen is never queued again. If that ever breaks
        the walk runs to its round cap and returns a graph far too large,
        so the size is worth asserting rather than assuming.
        """
        for sutra in REGISTRY.all():
            found = api.graph(str(sutra.id))
            with self.subTest(sutra=str(sutra.id)):
                self.assertLess(len(found["nodes"]), 40)

    def test_nodes_say_whether_they_are_codified(self):
        """
        The UI only makes a node clickable when there is something to show, so
        the flag has to be right.
        """
        found = api.graph("1.1.5")
        for node in found["nodes"]:
            self.assertEqual(node["codified"], REGISTRY.has(node["id"]),
                             node["id"])

    def test_every_edge_ends_on_a_node_that_is_present(self):
        for sutra in REGISTRY.all():
            found = api.graph(str(sutra.id))
            ids = {node["id"] for node in found["nodes"]}
            for edge in found["edges"]:
                self.assertIn(edge["from"], ids, edge)
                self.assertIn(edge["to"], ids, edge)

    def test_the_adhikara_edge_holds_for_a_codified_sutra(self):
        """
        This test used to be called ...though_nothing_codified_uses_it_yet,
        and it asserted that no codified sūtra fell under an adhikāra: the
        first heading is 1.4.1, which was past everything then written. It had
        to reach for an uncodified sūtra to exercise the path at all. That is
        no longer the state, so what it checks is now the ordinary case.
        """
        from src.astadhyayi.sources import all_sutra_ids, facts

        under = [s for s in all_sutra_ids() if facts(s).adhikara]
        self.assertGreater(len(under), 3000)

        codified_under = [s for s in under if REGISTRY.has(s)]
        self.assertGreater(len(codified_under), 20)

        found = api.graph("1.4.10")
        edges = [e for e in found["edges"] if e["kind"] == "adhikāra"]
        self.assertEqual(len(edges), 1)
        self.assertEqual(edges[0]["from"], "1.4.1")
        self.assertEqual(edges[0]["to"], "1.4.10")
        self.assertTrue(
            all(n["codified"] for n in found["nodes"]),
            "both ends are codified now, and the graph should say so",
        )

    def test_and_there_is_no_longer_a_sutra_that_is_not_codified(self):
        """
        This test used to pick an uncodified sūtra at run time and check
        that the graph answered for it, the node coming back marked
        uncodified. Three versions of it went stale by naming a sūtra or a
        heading the work then reached; the fourth named neither and went
        stale all the same, because there is now no uncodified sūtra left
        to pick. All 3,983 are in the registry.

        What the test was for survives as two claims. The corpus and the
        registry agree — every sūtra the index knows is codified — and the
        graph still walks a heading chain and marks what it finds, which
        is now checked on a codified sūtra instead.
        """
        from src.astadhyayi.sources import all_sutra_ids, facts

        uncodified = [s for s in all_sutra_ids() if not REGISTRY.has(s)]
        self.assertEqual(uncodified, [])

        # The same path as before, on a sūtra that HAS a heading other
        # than itself — a heading is listed as its own adhikāra, and the
        # graph rightly draws no edge from a sūtra to itself.
        target = next(
            s for s in all_sutra_ids()
            if {i.sutra for i in facts(s).adhikara} - {s}
        )
        found = api.graph(target)
        edges = [e for e in found["edges"] if e["kind"] == "adhikāra"]
        expected = {item.sutra for item in facts(target).adhikara} - {target}
        self.assertGreaterEqual(len(edges), 1)
        self.assertTrue(expected <= {e["from"] for e in edges})
        direct = [e for e in edges if not e["cross"]]
        self.assertTrue(direct)
        self.assertTrue(all(e["to"] == target for e in direct))
        self.assertTrue(all(n["codified"] for n in found["nodes"]))

    def test_dependents_is_the_graph_read_backward(self):
        """1.1.49's whole point is what it governs, so this is the question
        a reader actually asks of it."""
        governed = {row["id"] for row in api.dependents("1.1.49")}
        self.assertIn("1.1.51", governed)
        self.assertIn("1.1.52", governed)
        for other in governed:
            sources = {
                edge["from"] for edge in api.graph(other)["edges"]
                if edge["kind"] == "anuvṛtti"
            }
            self.assertIn("1.1.49", sources, other)


class Playground(unittest.TestCase):

    def test_every_codified_rule_can_be_put_behind_a_form(self):
        """
        The sweep. If a rule grows a parameter the form builder cannot handle,
        this says which one rather than leaving a dead panel in the UI.
        """
        unbuildable = []
        for sutra in REGISTRY.all():
            spec = playground.spec_for(str(sutra.id))
            if not spec.runnable:
                unbuildable.append(f"{sutra.id}: {spec.note}")
        self.assertEqual(unbuildable, [])

    def test_a_scalar_rule(self):
        result = playground.run("1.1.1", {"sound": "ai"})
        self.assertTrue(result["ok"])
        self.assertIs(result["result"], True)
        self.assertIn("'ai'", result["called"])

    def test_a_rule_returning_a_structure(self):
        result = playground.run("1.1.7", {"text": "indraḥ"})
        self.assertTrue(result["ok"])
        self.assertEqual(result["result"][0]["sounds"], ["n", "d", "r"])

    def test_a_rule_taking_a_dataclass(self):
        """
        1.1.5 takes an Adesa, whose `its` is a frozenset. The form hands back a
        list, and it has to be rebuilt as a set or the rule fails on its first
        `&`.
        """
        blocked = playground.run(
            "1.1.5", {"target": "i", "affix.form": "ta", "affix.its": "k"}
        )
        self.assertTrue(blocked["ok"])
        self.assertEqual(blocked["result"]["by"], "1.1.5")

        allowed = playground.run(
            "1.1.5", {"target": "i", "affix.form": "a", "affix.its": ""}
        )
        self.assertTrue(allowed["ok"])
        self.assertIsNone(allowed["result"])

    def test_a_rule_taking_a_list(self):
        result = playground.run(
            "1.1.50", {"sthanin": "i", "candidates": "a, e, o"}
        )
        self.assertTrue(result["ok"])
        self.assertEqual(result["result"], ["e"])

    def test_a_rule_taking_an_enum(self):
        result = playground.run("1.1.10", {"scheme": "kāśikā-4"})
        self.assertTrue(result["ok"])
        self.assertTrue(result["result"], "the fourfold reading rescues pairs")

    def test_an_engine_refusal_is_reported_and_not_raised(self):
        """
        The scanner rejecting a letter that is not a Sanskrit sound is the
        engine doing its job, and the message is worth showing.
        """
        result = playground.run("1.1.7", {"text": "zzz"})
        self.assertFalse(result["ok"])
        self.assertIn("unknown character", result["error"])

    def test_every_run_result_serialises(self):
        for sutra in REGISTRY.all():
            spec = playground.spec_for(str(sutra.id))
            values = {field.name: field.default for field in spec.fields}
            result = playground.run(str(sutra.id), values)
            json.dumps(result, ensure_ascii=False)

    def test_a_blank_or_defaultless_field_does_not_crash_the_rule(self):
        """
        A number field whose parameter has no default round-trips as the string
        "None", and int("None") throws. Found by running every rule with its
        own defaults — 1.1.21 positions(length, index) has none.
        """
        result = playground.run("1.1.21", {"length": None, "index": ""})
        self.assertTrue(result["ok"], result.get("error"))

    def test_the_playground_populates_the_registry_by_itself(self):
        """
        A POST to /api/astadhyayi/run reached a server whose registry was
        empty: only report.py imported the rules, and no GET had run yet. The
        module must not depend on someone else having imported them.
        """
        import sys

        self.assertIn("src.astadhyayi.rules", sys.modules)
        with open("src/astadhyayi/playground.py", encoding="utf-8") as handle:
            source = handle.read()
        self.assertIn("import src.astadhyayi.rules", source)


class Glosses(unittest.TestCase):
    """
    The plain-English line under each heading. It is a reader aid rather than a
    claim, so what these check is coverage and shape, not correctness against a
    source — the source, where there is one, is shown beside it and attributed.
    """

    DEVANAGARI = re.compile(r"[ऀ-ॿ]")
    LATIN = re.compile(r"[A-Za-zāīūṛṝḷḹṅñṭḍṇśṣḥṃ]")

    def setUp(self):
        from src.astadhyayi.glosses import GLOSSES
        self.glosses = GLOSSES

    def test_every_codified_sutra_has_one(self):
        codified = {str(s.id) for s in REGISTRY.all()}
        self.assertEqual(sorted(set(self.glosses) - codified), [])
        self.assertEqual(sorted(codified - set(self.glosses)), [])

    def test_every_one_carries_a_worked_form(self):
        """
        A rule about substitution is far easier to see than to read, so the
        example is not optional.
        """
        without = [k for k, v in self.glosses.items() if not v.example.strip()]
        self.assertEqual(without, [])

    def test_the_worked_forms_are_in_devanagari(self):
        thin = [
            k for k, v in self.glosses.items()
            if not self.DEVANAGARI.search(v.example)
        ]
        self.assertEqual(thin, [])

    def test_every_worked_form_carries_both_scripts(self):
        """
        The convention is इक् (iK) — Devanāgarī with the roman beside it — so a
        reader can recognise the same word wherever else it turns up. An
        earlier version of this test looked for IAST diacritics specifically
        and so passed forms like गो go → उपगु upagu, which carry no diacritic
        but are perfectly bilingual. What matters is that both scripts appear.
        """
        one_script = []
        for sutra_id, gloss in self.glosses.items():
            if not self.LATIN.search(gloss.example):
                one_script.append(sutra_id)
        self.assertEqual(one_script, [])

    def test_they_are_short_enough_to_read(self):
        """
        A gist that runs on is not a gist.

        Measured with the roman half of each देव (iast) pair collapsed away.
        The limit is about how much prose the reader has to get through, and
        a pair is one term shown twice, not two terms — counting both halves
        would tighten the limit every time the two-script convention reached
        another word, which is the opposite of what it should do.
        """
        collapsed = re.compile(r"\s*\([^)]*\)")
        long_ones = [
            k for k, v in self.glosses.items()
            if len(collapsed.sub("", v.plain)) > 320
        ]
        self.assertEqual(long_ones, [])

    def test_none_is_left_as_a_placeholder(self):
        for sutra_id, gloss in self.glosses.items():
            self.assertGreater(len(gloss.plain.strip()), 40, sutra_id)
            self.assertNotIn("TODO", gloss.plain, sutra_id)

    def test_the_api_carries_the_gloss_and_the_cited_source(self):
        found = api.detail("1.1.5")["gloss"]
        self.assertIn("कित्", found["plain"])
        self.assertIn("चितः", found["example"])
        self.assertIn("प्रत्यय", found["sutrartha"])

    def test_the_sutrartha_is_a_source_and_not_invented(self):
        """
        Where the UI shows one it must come from the corpus, so a reader can
        tell our sentence from a cited one. 92 of the 95 have it.
        """
        from src.astadhyayi.corpus import commentary_on

        with_source = 0
        for sutra in REGISTRY.all():
            shown = api.detail(str(sutra.id))["gloss"]["sutrartha"]
            if shown:
                with_source += 1
                self.assertEqual(
                    shown, commentary_on(str(sutra.id), "sutrartha_english")
                )
        # Neither a count nor a proportion. Both were snapshots of whatever
        # had been codified that week, and both went red on the next batch
        # for no reason but that the corpus is silent on more of it. The
        # invariant is the one that matters and does not drift: the API shows
        # the source wherever the corpus has one, and nothing where it has
        # none.
        total = len(REGISTRY.all())
        available = sum(
            1 for sutra in REGISTRY.all()
            if commentary_on(str(sutra.id), "sutrartha_english")
        )
        self.assertEqual(with_source, available)
        self.assertGreater(available, 0)
        self.assertLessEqual(available, total)

class Outstanding(unittest.TestCase):
    """
    The list marks a sūtra that still has something unresolved, and the eye
    beside it shows WHAT. A marker the reader has to be told the meaning of is
    not transparency, so the text travels with the row.
    """

    def setUp(self):
        self.rows = {r["id"]: r for r in api.catalogue()["sutras"]}

    def test_the_flag_and_the_text_never_disagree(self):
        for sutra_id, row in self.rows.items():
            markers = {f["marker"] for f in row["outstanding"]}
            self.assertEqual(row["open"], "OPEN" in markers, sutra_id)
            self.assertEqual(row["scope"], "SCOPE" in markers, sutra_id)
            self.assertEqual(
                bool(row["outstanding"]), row["open"] or row["scope"], sutra_id
            )

    def test_only_unresolved_findings_travel(self):
        """A SETTLED conclusion is not outstanding and must not raise a flag."""
        for sutra_id, row in self.rows.items():
            for finding in row["outstanding"]:
                self.assertIn(finding["marker"], ("OPEN", "SCOPE"), sutra_id)

    def test_the_text_is_the_note_and_not_a_summary_of_it(self):
        """
        What the eye shows has to be the finding itself. A paraphrase would be
        a second thing to keep in step with the record, and it would drift.
        """
        from src.astadhyayi.report import findings

        for sutra_id, row in self.rows.items():
            expected = [
                {"marker": m, "text": t}
                for m, t in findings(REGISTRY.get(sutra_id).notes)
                if m in ("OPEN", "SCOPE")
            ]
            self.assertEqual(row["outstanding"], expected, sutra_id)

    def test_the_open_questions_are_few_and_named(self):
        """
        An OPEN finding is a question the sources did not settle, and there
        should not be many. Asserted as a proportion rather than a fixed list,
        which would break on every batch — but the long-standing two are named,
        so silently losing one would show.
        """
        opened = sorted(k for k, v in self.rows.items() if v["open"])
        self.assertIn("1.1.1", opened)
        self.assertIn("1.1.70", opened)
        self.assertLess(len(opened) / len(self.rows), 0.1)

    def test_most_sutras_carry_no_flag(self):
        """
        If nearly everything were flagged the marker would say nothing, so
        this is a check on the marker and not on the sūtras. It caught a real
        mistake once: a standing caveat about the pada block was attached to
        all eighty of its sūtras, which is true of each of them but flagged
        two rows in five. It now sits on the two that frame the block.
        """
        clear = [k for k, v in self.rows.items() if not v["outstanding"]]
        self.assertGreater(len(clear) / len(self.rows), 0.7)


class NoNoteCarriesALiteralEscape(unittest.TestCase):
    """
    Twenty-two notes once carried a literal backslash-n where a
    paragraph break belonged, because the escaping depends on HOW the
    file was written and I used one convention in the other kind.

      * in a patch script the module's text sits inside a Python
        string, so a doubled escape there becomes a single one in the
        module, which Python reads as a newline;
      * written straight to the module, a doubled escape IS the
        module's text and Python reads it as backslash-plus-n.

    Nothing broke. The notes simply read \\n where a break belonged,
    which is exactly why nothing caught it — so this asserts the
    property across every table at once rather than at the places it
    happened to bite.
    """

    def _tables(self):
        from src.astadhyayi import (
            bhava_krt, dhatu_sambandha, ktva_namul, lakara,
            tacchila, tense_transfer, upapada_krt, vidhi_krt,
        )

        found = []
        for module in (upapada_krt, tacchila, lakara, bhava_krt,
                       tense_transfer, vidhi_krt, dhatu_sambandha,
                       ktva_namul):
            for name in dir(module):
                value = getattr(module, name)
                if not isinstance(value, tuple) or not value:
                    continue
                if all(hasattr(row, "why") and hasattr(row, "sutra")
                       for row in value):
                    found.append((module.__name__, name, value))
        return found

    def test_the_tables_are_actually_found(self):
        tables = self._tables()
        self.assertGreater(len(tables), 4)
        self.assertGreater(sum(len(rows) for _, _, rows in tables), 200)

    def test_no_row_of_any_table_has_one(self):
        for module, name, rows in self._tables():
            for row in rows:
                with self.subTest(table="%s.%s" % (module, name),
                                  sutra=row.sutra):
                    self.assertNotIn("\\n", row.why)

    def test_nor_does_any_registered_note(self):
        from src.astadhyayi.sutra import REGISTRY

        for sutra in REGISTRY.all():
            with self.subTest(sutra=str(sutra.id)):
                self.assertNotIn("\\n", sutra.notes)


if __name__ == "__main__":
    unittest.main()


class BothScriptsAreShownInOneShape(unittest.TestCase):
    """
    देवनागरी (iast), everywhere a Sanskrit word is shown to a reader.

    `_both` had always done this for the generated glosses; the hand-written
    ones set the roman beside the Devanāgarī with nothing but a space, which
    reads as two words rather than one word written twice. The convention is
    now applied where the text is served, so it also covers entries written
    after this test.
    """

    #: Devanāgarī, whitespace, then something that could be transliteration.
    ADJACENT = re.compile(
        r"([\u0900-\u097F][\u0900-\u097F\u200c\u200d]*)\s+"
        r"([A-Za-zāīūṛṝḷḹṅñṭḍṇśṣḥṃ\u0301\u0300\u0310]+)"
    )

    def _offenders(self, text):
        """Adjacent pairs where the roman really is the transliteration."""
        from src.astadhyayi.playground import to_iast

        found = []
        for devanagari, roman in self.ADJACENT.findall(text or ""):
            if to_iast(devanagari).strip() == roman:
                found.append(f"{devanagari} {roman}")
        return found

    def test_no_gloss_shows_an_unbracketed_transliteration(self):
        for sutra_id, gloss in GLOSSES.items():
            for field in ("plain", "example"):
                with self.subTest(sutra=sutra_id, field=field):
                    self.assertEqual(
                        self._offenders(getattr(gloss, field)), [],
                        f"{sutra_id} {field}: {getattr(gloss, field)}")

    def test_no_curated_input_does_either(self):
        from src.astadhyayi.cases import cases_for

        for sutra in REGISTRY.all():
            for case in cases_for(str(sutra.id)):
                with self.subTest(sutra=str(sutra.id), case=case.label):
                    self.assertEqual(self._offenders(case.label), [])
                    self.assertEqual(self._offenders(case.note), [])

    def test_ordinary_prose_after_a_sanskrit_word_is_left_alone(self):
        """
        The transform has to prove the roman is the transliteration before
        it brackets. Most adjacencies in the glosses are prose — a Sanskrit
        word followed by an English one — and bracketing by position rather
        than by proof would turn the English into a gloss.
        """
        from src.astadhyayi.glosses import bracket_iast

        for text in ("अत्र stays as it is",
                     "before जस् that becomes optional",
                     "इकः in the sixth case",
                     "भू replacing अस्"):
            with self.subTest(text=text):
                self.assertEqual(bracket_iast(text), text)

    def test_it_brackets_what_it_can_prove(self):
        from src.astadhyayi.glosses import bracket_iast

        self.assertEqual(bracket_iast("उपकुम्भम् upakumbham"),
                         "उपकुम्भम् (upakumbham)")
        self.assertEqual(bracket_iast("कति kati · कतिभिः katibhiḥ, not x"),
                         "कति (kati) · कतिभिः (katibhiḥ), not x")

    def test_applying_it_twice_changes_nothing(self):
        """
        It runs at import over data that other code may re-render. If it
        were not idempotent the brackets would nest a layer per pass, and
        nothing would fail until a reader saw ((iast)).
        """
        from src.astadhyayi.glosses import bracket_iast

        for gloss in GLOSSES.values():
            for field in ("plain", "example"):
                once = getattr(gloss, field)
                with self.subTest(field=field):
                    self.assertEqual(bracket_iast(once), once)


class NeitherScriptEverStandsAlone(unittest.TestCase):
    """
    The converse of the last class. A Sanskrit word must not appear in roman
    with no Devanāgarī either — देवनागरी (iast), both halves, everywhere.

    This direction is much harder to enforce than the other, and the reason
    is worth stating: going *from* Devanāgarī the script itself tells you
    what is Sanskrit. Coming back, nothing does. `root`, `name`, `sense` and
    `voice` sit in the same sentences as `gati`, `veda` and `kit`, and every
    one of them round-trips through the transliterator. So the rule is
    applied only where the evidence is real — a word carrying an IAST
    diacritic, which no English word has, or a word on a list checked by
    hand against the padaccheda of all 3,983 sūtras.
    """

    def _bare(self, text):
        """Sanskrit words in this text with no Devanāgarī attached."""
        from src.astadhyayi.glosses import _is_sanskrit

        found = []
        # skip only the pairs already in the convention. Deliberately NOT
        # the code guard the transform uses: when this test consulted that
        # too, both skipped the same 991 fields and agreed the work was
        # done. A check that shares the transform's blind spot is not a
        # check.
        for chunk in re.split(r"[\u0900-\u097F][^\s]*\s*\([^)]*\)", text or ""):
            for word, follows in re.findall(
                    r"([A-Za-zāīūṛṝḷḹṅñṭḍṇśṣḥṃ\u0310]+(?:'s)?)(\(?)", chunk):
                if follows == "(":
                    continue           # a name being called
                if _is_sanskrit(word):
                    found.append(word)
        return found

    def test_no_gloss_leaves_a_sanskrit_word_in_roman_alone(self):
        for sutra_id, gloss in GLOSSES.items():
            for field in ("plain", "example"):
                with self.subTest(sutra=sutra_id, field=field):
                    self.assertEqual(
                        self._bare(getattr(gloss, field)), [],
                        f"{sutra_id} {field}: {getattr(gloss, field)}")

    def test_nor_does_any_curated_input(self):
        from src.astadhyayi.cases import cases_for

        for sutra in REGISTRY.all():
            for case in cases_for(str(sutra.id)):
                with self.subTest(sutra=str(sutra.id), case=case.label):
                    self.assertEqual(self._bare(case.label), [])
                    self.assertEqual(self._bare(case.note), [])

    def test_proper_nouns_are_converted_too(self):
        from src.astadhyayi.glosses import add_devanagari

        self.assertEqual(add_devanagari("the Kāśikā asks"),
                         "the काशिका (Kāśikā) asks")
        self.assertEqual(add_devanagari("Pāṇini lists them"),
                         "पाणिनि (Pāṇini) lists them")

    def test_but_english_morphology_on_a_sanskrit_stem_is_not(self):
        """
        शिवसूत्रस् would be a word in no language: that -s is an English
        plural. These transliterate perfectly well, which is exactly why
        they need naming rather than detecting.
        """
        from src.astadhyayi.glosses import add_devanagari

        for text in ("the śivasūtras give it", "the sūtras of this pāda",
                     "a few vārttikas stand here"):
            with self.subTest(text=text):
                self.assertIn(text.split()[1], add_devanagari(text))

    def test_english_prose_is_never_touched(self):
        from src.astadhyayi.glosses import add_devanagari

        for text in ("the root takes the ending",
                     "without the elision it does not",
                     "one name only, and the later of them stands"):
            with self.subTest(text=text):
                self.assertEqual(add_devanagari(text), text)

    def test_a_starred_form_keeps_its_star(self):
        """
        An asterisk marks a form the rule prevents. It has to survive, or
        the reader is shown a non-existent word as though it were attested.
        """
        from src.astadhyayi.glosses import add_devanagari

        self.assertEqual(add_devanagari("not *katayaḥ"),
                         "not *कतयः (katayaḥ)")
        self.assertIn("*कतयः", GLOSSES["1.1.25"].example)

    def test_code_and_pratyaharas_are_left_in_roman(self):
        """
        aiC cannot be written in Devanāgarī at all — अच् is अ followed by
        च्, and nothing in the script says which is the marker. The capital
        is the whole signal, so these spans stay as they are.
        """
        from src.astadhyayi.glosses import add_devanagari

        # An identifier and a signature arrow are code all through.
        self.assertEqual(add_devanagari("is_vrddhi(sound) -> bool"),
                         "is_vrddhi(sound) -> bool")

        # But a line may be part code and part prose, and the distinction is
        # per token. Here aiC is a pratyāhāra and stays; ā is a cited vowel
        # and does not. This test asserted the whole line stayed roman when
        # it was written, because the guard then treated any string holding
        # a sutra number - 1.1.71 matched the dotted-name pattern - as code
        # from end to end.
        # That was the bug, and the assertion was written to match it.
        mixed = add_devanagari("derived as ā + aiC, resolved through 1.1.71")
        self.assertIn("आ (ā)", mixed)
        self.assertIn("aiC", mixed)
        self.assertNotIn("(aiC)", mixed)
        self.assertIn("1.1.71", mixed)

    def test_a_sutra_number_does_not_make_a_line_into_code(self):
        r"""
        The regression this class exists to prevent. `\w.\w` is true of
        1.1.71 and 6.1.198, so a guard written to catch dotted attribute
        access skipped 991 gloss and case fields whole and left every
        Sanskrit word in them bare — and the check consulted the same guard,
        so both agreed the work was done.
        """
        from src.astadhyayi.glosses import add_devanagari

        got = add_devanagari("6.1.198 makes the vocative initially udātta")
        self.assertEqual(got, "6.1.198 makes the vocative initially "
                              "उदात्त (udātta)")

    def test_applying_it_twice_changes_nothing(self):
        from src.astadhyayi.glosses import add_devanagari

        for gloss in GLOSSES.values():
            for field in ("plain", "example"):
                once = getattr(gloss, field)
                with self.subTest(field=field):
                    self.assertEqual(add_devanagari(once), once)


class ABeginnerIsToldWhatKindOfRuleThisIs(unittest.TestCase):
    """
    "Gives a name." is true and no use to someone starting out. It does not
    say what naming is *for*, or why a grammar would spend its opening rule
    on three vowels instead of explaining something.

    The gap is not about 1.1.1. It is about how the Aṣṭādhyāyī is built, and
    it is the same gap at every one of the 200 saṃjñā rules — so it is
    answered once per kind, not once per sūtra, and the corpus's own
    classification carries it to all 3,983.
    """

    def test_every_sutra_in_the_grammar_has_one(self):
        from src.astadhyayi.glosses import kind_of
        from src.astadhyayi.sources import all_sutra_ids

        missing = [s for s in all_sutra_ids() if kind_of(s) is None]
        self.assertEqual(missing, [], f"{len(missing)} sūtras without one")

    def test_it_explains_the_kind_rather_than_the_rule(self):
        """
        The text must be about the class of rule. If one of these ever
        mentions a particular sūtra it has stopped being reusable, and the
        199 others are getting an explanation written for their neighbour.
        """
        from src.astadhyayi.glosses import KINDS

        for name, kind in KINDS.items():
            with self.subTest(kind=name):
                self.assertIsNone(re.search(r"\d\.\d\.\d", kind.plain))
                self.assertGreater(len(kind.plain), 160,
                                   f"{name}: too short to teach anything")
                self.assertLessEqual(len(kind.label.split()), 5)

    def test_the_detail_payload_carries_it(self):
        payload = api.detail("1.1.1")
        self.assertEqual(payload["kind"]["label"], "a definition")
        self.assertIn("coins a technical term", payload["kind"]["plain"])

    def test_no_gloss_still_opens_with_a_bare_category_stub(self):
        """
        With the kind explained above it, an opener that says only what
        kind of rule this is spends the reader's first sentence saying
        nothing they were not just told.
        """
        stub = re.compile(
            r"^(Gives a [^.]{0,30}\.|A rule about the rules\.|"
            r"The companion name\.|Names the (indeclinables|roots|"
            r"noun stem|high pitch)\.)"
        )
        offenders = [k for k, g in GLOSSES.items() if stub.match(g.plain)]
        self.assertEqual(offenders, [], f"{len(offenders)} still stubbed")


class NeitherScriptStandsAloneInTheForm(unittest.TestCase):
    """
    The glosses have been held to the two-script rule for a while. The form
    beside them was not, and the gap was easy to miss because each surface
    looked fine on its own: the panel prose composed two of the three
    passes, and the field labels under it composed none. So a hint could
    say आर्धधातुक with nothing beside it, on the one surface whose own
    comment promised otherwise.

    The three passes are not interchangeable. `bracket_iast` brackets the
    roman of a pair already written out; `add_devanagari` supplies the
    script for a bare roman word; `pair_bare_devanagari` supplies the roman
    for a bare Devanāgarī one. Leaving out the last is what fails a reader
    who cannot yet read the script — exactly the reader the form is for.
    """

    def test_every_label_and_hint_is_already_in_both_scripts(self):
        """
        Applying the convention to delivered text must change nothing. That
        is a stronger claim than "some roman appears somewhere": these
        hints are mostly English, so a naive both-scripts-present check
        would pass on text that never paired a single word.
        """
        from src.astadhyayi.fieldhelp import HELP, label_and_hint
        from src.astadhyayi.glosses import both_scripts

        unpaired = sorted(
            name for name in HELP
            for text in label_and_hint(name)
            if text and both_scripts(text) != text
        )
        self.assertEqual(
            unpaired, [],
            "these reach the reader with one script standing alone")

    def test_the_chain_is_written_in_one_place(self):
        """
        It was written out three times and the copies disagreed, which is
        how the drift happened. Anything showing Sanskrit to a reader calls
        `both_scripts`; nothing re-composes the passes for itself.
        """
        import inspect

        from src.astadhyayi import fieldhelp, playground

        for module in (fieldhelp, playground):
            with self.subTest(module=module.__name__):
                source = inspect.getsource(module)
                self.assertIn("both_scripts", source)
                self.assertNotIn("add_devanagari(bracket_iast", source)


class EveryFormFieldSaysWhatItWants(unittest.TestCase):
    """
    The form is built from a function signature, so left alone its labels are
    Python parameter names with the underscores taken out: `al vidhi`,
    `purva vidhi`, `dvirvacana caused by vowel`. Nobody can act on those.
    A reader who could would not need the form; a reader who needs the form
    cannot.

    So each field carries a label a person can read and a hint naming the
    term behind it. The test is not that the strings exist — it is that they
    are not the parameter name wearing a coat.
    """

    def setUp(self):
        self.fields = {
            field.name: field
            for sutra in REGISTRY.all()
            for field in playground.spec_for(str(sutra.id)).fields
        }
        self.assertGreater(len(self.fields), 150)

    def test_none_is_left_as_its_parameter_name(self):
        from src.astadhyayi.fieldhelp import missing

        self.assertEqual(missing(self.fields), ())

    def test_the_label_is_not_just_the_name_respaced(self):
        for name, field in self.fields.items():
            with self.subTest(field=name):
                self.assertNotEqual(
                    field.label.lower(),
                    name.replace("_", " ").replace(".", " · ").lower(),
                    f"{name} still shows its parameter name",
                )

    def test_a_hint_names_the_term_or_says_something_more(self):
        """
        A label alone is a way in but not a way through: a reader who knows
        the śāstra needs अल्विधि, not "does the rule work on sounds?". Most
        hints therefore carry Devanāgarī. Where one does not, it has to be
        saying something the label did not.
        """
        bare = [
            name for name, field in self.fields.items()
            if not field.hint.strip()
        ]
        self.assertLessEqual(
            len(bare), 40,
            f"{len(bare)} fields have a label but nothing behind it: "
            f"{sorted(bare)[:12]}",
        )
        with_term = [
            f for f in self.fields.values()
            if re.search(r"[\u0900-\u097F]", f.hint)
        ]
        self.assertGreater(len(with_term), 60)

    def test_the_payload_carries_both(self):
        payload = api.detail("1.1.56")
        fields = {f["name"]: f for f in payload["playground"]["fields"]}
        self.assertIn("al_vidhi", fields)
        self.assertEqual(fields["al_vidhi"]["label"],
                         "does the rule work on sounds?")
        self.assertIn("अल्विधि", fields["al_vidhi"]["hint"])
