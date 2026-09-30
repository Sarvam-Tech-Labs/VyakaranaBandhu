# -*- coding: utf-8 -*-
"""
The harness that judges the engine against other people's answers — and proof
that it can tell a right answer from a wrong one. A harness that passes
everything would make every dataset look like a success.
"""

from __future__ import annotations

import json
import os
import tempfile
import unittest

from src.astadhyayi.sandhi import harness as H


def case(words, outputs, **kw):
    return {"id": kw.pop("id", "t"), "input": words, "outputs": outputs, **kw}


class Comparison(unittest.TestCase):

    def test_joined_ignores_spaces_hyphens_and_the_avagraha_spelling(self):
        self.assertEqual(H.joined("rāmo ’tra"), H.joined("rāmo'tra"))
        self.assertEqual(H.joined("deva-indra"), "devaindra")

    def test_ignoring_the_avagraha_is_opt_in_and_drops_it_from_both_sides(self):
        """A dataset that writes `vā'mutra` for an elided a: the engine derives
        `vāmutra` from `vā amutra` (6.1.101). Off by default, that is a miss —
        so the option cannot hide a real difference unasked."""
        row = case(["vā", "amutra"], ["vā'mutra"])
        self.assertFalse(H.run_case(row).ok)
        self.assertTrue(H.run_case(row, ignore_avagraha=True).ok)
        self.assertEqual(H.joined("rāmo 'tra", ignore_avagraha=True), "rāmotra")
        self.assertEqual(H.joined("rāmo 'tra"), "rāmo'tra")

    def test_ignoring_the_avagraha_does_not_excuse_a_wrong_form(self):
        row = case(["vā", "amutra"], ["vā'mitra"])
        self.assertFalse(H.run_case(row, ignore_avagraha=True).ok)

    def test_norm_nasal_normalizes_anunasika_spelling(self):
        # Vidyut writes m̐ (bhavām̐ścinoti) for candrabindu on the vowel (bhavā̐ścinoti)
        self.assertEqual(H.joined("bhavām̐ścinoti", norm_nasal=True), "bhavā̐ścinoti")
        self.assertEqual(H.joined("pum̐sputraḥ", norm_nasal=True), "pu̐sputraḥ")
        row = case(["pum", "putraḥ"], ["pum̐sputraḥ"])
        self.assertFalse(H.run_case(row).ok)
        self.assertTrue(H.run_case(row, norm_nasal=True).ok)

    def test_a_right_answer_matches(self):
        r = H.run_case(case(["dadhi", "atra"], ["dadhyatra"]))
        self.assertTrue(r.ok, r)
        self.assertEqual(r.steps[0], "6.1.77")

    def test_a_wrong_answer_is_a_miss_and_says_what_the_engine_gave(self):
        r = H.run_case(case(["dadhi", "atra"], ["dadhiatra"]))
        self.assertFalse(r.ok)
        self.assertEqual(r.verdict, "missing")
        self.assertIn("dadhyatra", r.got)

    def test_a_case_may_list_only_one_of_several_options(self):
        """The engine returns both haraiha and harayiha; a source listing one
        is not contradicted by the engine also giving the other."""
        self.assertTrue(H.run_case(case(["haras", "iha"], ["harayiha"])).ok)
        self.assertTrue(H.run_case(case(["haras", "iha"], ["haraiha"])).ok)

    def test_an_exhaustive_case_must_have_exactly_the_sources_forms(self):
        r = H.run_case(case(["haras", "iha"], ["harayiha"], exhaustive=True))
        self.assertFalse(r.ok)
        self.assertEqual(r.verdict, "extra")

    def test_a_counter_example_fails_if_the_engine_over_applies(self):
        """Nothing may happen where a vowel does not follow: dadhi siñcati.
        Written as a counter-example the engine's set must equal the case's."""
        good = H.run_case(case(["dadhi", "siñcati"], ["dadhisiñcati"],
                               counter_example=True))
        self.assertTrue(good.ok, good)
        bad = H.run_case(case(["dadhi", "atra"], ["dadhiatra"],
                              counter_example=True))
        self.assertFalse(bad.ok)


class UnderSpecifiedVisarga(unittest.TestCase):

    def test_a_visarga_from_s_matches_under_the_s_reading(self):
        r = H.run_case(case(["rāmaḥ", "atra"], ["rāmo'tra"]))
        self.assertTrue(r.ok, r)
        self.assertIn("0=s", r.reading)

    def test_a_visarga_from_r_matches_under_the_r_reading_and_says_so(self):
        r = H.run_case(case(["punaḥ", "atra"], ["punaratra"]))
        self.assertTrue(r.ok, r)
        self.assertIn("0=r", r.reading)

    def test_a_caller_who_says_the_final_is_not_second_guessed(self):
        r = H.run_case(case(["punaḥ", "atra"], ["punaratra"],
                            flags={"0": ["final:r"]}))
        self.assertTrue(r.ok, r)
        self.assertEqual(r.reading, "")


class Reading(unittest.TestCase):

    def test_both_schemas_are_read(self):
        self.assertEqual(H.expected_forms({"output": "a b"}), ("ab",))
        self.assertEqual(H.expected_forms({"outputs": ["a b", "ab", "c"]}),
                         ("ab", "c"))

    def test_a_bad_input_is_an_error_row_not_a_crash(self):
        r = H.run_case(case(["kaXa", "iti"], ["x"]))
        self.assertEqual(r.verdict, "error")
        self.assertIn("'X'", r.detail)

    def test_a_row_with_nothing_in_it_is_skipped(self):
        self.assertEqual(H.run_case({"id": "e", "input": [], "output": ""})
                         .verdict, "skipped")

    def test_a_row_that_does_not_say_takes_the_default_boundary(self):
        row = case(["ne", "a"], ["naya"], boundary="unknown")
        self.assertFalse(H.run_case(row).ok)                  # two padas: ne'
        self.assertTrue(H.run_case(row, default_boundary="anga").ok)
        self.assertTrue(H.evaluate([row], default_boundary="anga")
                        .matched == 1)

    def test_the_boundary_and_flags_are_passed_to_the_engine(self):
        self.assertTrue(H.run_case(case(["ne", "a"], ["naya"],
                                        boundary="anga")).ok)
        self.assertFalse(H.run_case(case(["ne", "a"], ["naya"])).ok)


class Citation(unittest.TestCase):
    """A row that names a sūtra tests the citation as well as the form."""

    def test_a_derivation_that_cites_the_named_sutra_is_credited(self):
        r = H.run_case(case(["dadhi", "atra"], ["dadhyatra"], rule="6.1.77"))
        self.assertTrue(r.ok)
        self.assertTrue(r.cited)

    def test_a_named_sutra_the_derivation_never_mentions_is_reported(self):
        r = H.run_case(case(["dadhi", "atra"], ["dadhyatra"], rule="8.4.40"))
        self.assertTrue(r.ok)
        self.assertFalse(r.cited)

    def test_a_sutra_leaned_on_counts_as_cited(self):
        """1.1.50 is not a step of the derivation but it is what a step leans on."""
        r = H.run_case(case(["dadhi", "atra"], ["dadhyatra"], rule="1.1.50"))
        self.assertTrue(r.cited)

    def test_a_row_that_names_no_sutra_is_not_scored(self):
        for rule in (None, "chutva", "6.1.77.1"):
            r = H.run_case(case(["dadhi", "atra"], ["dadhyatra"], rule=rule))
            self.assertIsNone(r.cited, rule)

    def test_the_summary_reports_the_agreement(self):
        s = H.evaluate([case(["dadhi", "atra"], ["dadhyatra"], rule="6.1.77", id="a"),
                        case(["dadhi", "atra"], ["dadhyatra"], rule="8.4.40", id="b")])
        self.assertIn("citation: of 2 matching rows", s.report())
        self.assertIn("1 cite it (50.0%)", s.report())
        self.assertEqual(list(s.uncited), ["b"])


class Summary(unittest.TestCase):

    def test_misses_are_clustered_by_junction(self):
        cases = [case(["dadhi", "atra"], ["wrong"], id=f"a{i}")
                 for i in range(3)]
        cases.append(case(["madhu", "atra"], ["madhvatra"], id="ok"))
        s = H.evaluate(cases)
        self.assertEqual(s.total, 4)
        self.assertEqual(s.matched, 1)
        worst = s.worst_junctions()
        self.assertEqual(worst[0], (("i", "a"), 0, 3))
        self.assertIn("match rate 25.0%", s.report())

    def test_the_command_line_tool_reads_both_file_kinds(self):
        import subprocess, sys
        with tempfile.TemporaryDirectory() as tmp:
            gold = os.path.join(tmp, "g.gold.json")
            rows = os.path.join(tmp, "d.jsonl")
            with open(gold, "w", encoding="utf-8") as handle:
                json.dump([case(["dadhi", "atra"], ["dadhyatra"])], handle)
            with open(rows, "w", encoding="utf-8") as handle:
                handle.write(json.dumps(
                    {"id": "x", "input": ["dadhi", "atra"],
                     "output": "dadhi atra"}) + "\n")
            done = subprocess.run(
                [sys.executable, "tools/sandhi_eval.py", gold, rows],
                capture_output=True, text=True, encoding="utf-8")
            self.assertEqual(done.returncode, 1, done.stderr)      # one file misses
            self.assertIn("1 cases: 1 match", done.stdout)
            self.assertIn("1 cases: 1 missing", done.stdout)


if __name__ == "__main__":
    unittest.main()
