# -*- coding: utf-8 -*-
"""
Tests for the curated playground inputs.

A worked input that no longer works is worse than none at all: it invites a
reader to click it and shows them the wrong thing, and nothing else in the
project would notice. So these tests actually *run* every case through the
same code path the UI uses, and check three things:

  * it does not raise;
  * a "worked" case produces something rather than nothing;
  * and it fires the sūtra it is offered under.

That third one is the reason 182 of the cases are derived from the provision
tables rather than typed: a derived input is built out of the rule's own
conditions and cannot drift from it. Writing this test is also what found the
three playground bugs recorded below — none of them was visible from the
Python side, because they all lived in the coercion between a web form and a
function signature.
"""

from __future__ import annotations

import re
import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi.cases import CURATED, Case, cases_for, coverage
from src.astadhyayi.playground import run, spec_for
from src.astadhyayi.sutra import REGISTRY

#: Sūtras whose case legitimately reports a different sūtra, with the reason.
#: Each of these contributes no provision of its own — it is a heading, an
#: atideśa, or a rule whose whole effect is folded into a neighbour — so there
#: is nothing for a verdict to cite it by. Keeping the list explicit is what
#: stops it becoming a place to hide a real failure.

def _refusing_sutras():
    """
    Every sūtra codified as a प्रतिषेध — a row that REFUSES an affix
    rather than giving one. Read from the tables themselves so the set
    cannot drift from what the code actually does.

    Such a rule answers by whichever rule supplies the form instead,
    and carries its own id on `blocked_by`. That is the standing
    decision 2.3.72 settled: a rule which excepts a word by name does
    not thereby govern it.

    Two sets come back, because there are two shapes. A rule that
    refuses a NAMED affix has a supplier to answer by. A rule that
    names none — 4.1.10 न षट्स्वस्रादिभ्यः, यो यतः प्राप्नोति स
    सर्वः प्रतिषिध्यते — refuses the whole section at once and has
    no supplier to name, so it answers by itself. That is the standing
    carve-out *unless refusing is all the rule did*, and it is read
    off the rows rather than listed by hand.
    """
    from src.astadhyayi import (kala_taddhita, lakara, stri,
                                tacchila, upapada_krt)

    named, blanket = set(), set()
    for table in (upapada_krt.UPAPADA, lakara.LAKARA,
                  tacchila.TACCHILA, stri.STRI_TABLE,
                  kala_taddhita.KALA_TABLE):
        for row in table:
            if not getattr(row, "refuses", False):
                continue
            if getattr(row, "gives", ""):
                named.add(row.sutra)
            else:
                blanket.add(row.sutra)
    # A sūtra with rows of both kinds still has a supplier to name.
    return named, blanket - named


CITES_ANOTHER = {
    "2.3.35": "दूरान्तिकार्थेभ्यो द्वितीया च works with 2.3.34 and 2.3.36 "
              "to give ONE word four cases — दूरान्तिकार्थेभ्यश् चतस्रो "
              "विभक्तयो भवन्ति — and the three cannot be told apart by "
              "their conditions. Only the first of them can be named as "
              "the rule that fired; the other three endings are on its "
              "`also`",
    "1.3.62": "पूर्ववत् सनः is an atideśa; where the root has its ātmanepada "
              "directly the resolver names that cause, which is what "
              "पूर्ववत् means — येन निमित्तेन पूर्वस्मात्, तेनैव",
    "1.4.60": "गतिश्च contributes no provision: its च is folded into 1.4.59's "
              "pair of names, and its yogavibhāga shapes 1.4.61 onwards",
    "1.4.80": "ते प्राग्धातोः is about placement, not classification",
    "1.4.81": "छन्दसि परेऽपि is about placement too — where the preverb may "
              "stand, not what it is called",
    "1.4.82": "व्यवहिताश्च likewise, and neither contributes a name for a "
              "verdict to cite them by",
    "1.4.103": "सुपः is answered together with 1.4.99–1.4.104, which do "
               "nothing separately",
}



def _order(sutra_id):
    """
    A sūtra id as a sortable triple, or None if it is not one.

    An empty `by` is a real answer — it is how a rule says no rule of its
    run reached the input — and it used to reach this function and raise
    ValueError on int(""), so a case that should have failed with a
    readable message crashed the whole test instead.
    """
    parts = str(sutra_id).split(".")
    if len(parts) != 3 or not all(p.isdigit() for p in parts):
        return None
    return tuple(int(p) for p in parts)


def _heading_range(sutra_id):
    """The stretch a heading governs, or None if it is not one.

    Two sources, because the corpus knows only some of them: data.json types
    2.1.11 विभाषा an adhikāra but calls 2.1.3 and 2.1.5 saṃjñās, though the
    Kāśikā opens both with इत्यधिकारो वेदितव्यः. Where the codification has
    read the range out of the commentary it is recorded, and that record is
    the better authority.
    """
    from src.astadhyayi.reading import adhikara
    from src.astadhyayi.samasa import SAMJNAS

    for heading in SAMJNAS:
        if heading.sutra == sutra_id:
            return (heading.sutra, heading.through)
    found = adhikara(sutra_id)
    if found is not None and found.sutra_id == sutra_id:
        return (sutra_id, found.ends_at)
    return None


def _within(sutra_id, span):
    """Whether this id falls inside a heading's range. An id that is not
    one — an empty `by`, meaning no rule fired — is inside nothing."""
    here = _order(sutra_id)
    if here is None:
        return False
    return _order(span[0]) <= here <= _order(span[1])


class EveryRuleHasSomethingToTry(unittest.TestCase):
    def test_all_of_them(self):
        have, missing = coverage()
        self.assertEqual(list(missing), [])
        self.assertEqual(len(have), len(REGISTRY.all()))

    def test_and_the_count_is_worth_having(self):
        total = sum(len(cases_for(str(s.id))) for s in REGISTRY.all())
        self.assertGreater(total, len(REGISTRY.all()))

    def test_most_are_derived_rather_than_typed(self):
        """
        Which is the point: a derived input is built from the rule's own
        conditions and cannot drift from it. If this ever inverts, the
        self-maintaining half has been quietly abandoned.
        """
        derived = sum(
            len(cases_for(str(s.id))) - len(CURATED.get(str(s.id), ()))
            for s in REGISTRY.all()
        )
        typed = sum(len(v) for v in CURATED.values())
        self.assertGreater(derived, 150)
        self.assertGreater(derived + typed, 450)


class EveryCaseActuallyRuns(unittest.TestCase):
    """The whole reason these tests exist."""

    def setUp(self):
        self.all_cases = [
            (str(sutra.id), case)
            for sutra in REGISTRY.all()
            for case in cases_for(str(sutra.id))
        ]

    def test_none_of_them_raises(self):
        for sutra_id, case in self.all_cases:
            with self.subTest(sutra=sutra_id, case=case.label):
                outcome = run(sutra_id, dict(case.values))
                self.assertTrue(outcome.get("ok"),
                                f"{sutra_id} {case.label}: "
                                f"{outcome.get('error')}")

    def test_a_worked_case_produces_something(self):
        for sutra_id, case in self.all_cases:
            if case.kind != "worked":
                continue
            with self.subTest(sutra=sutra_id, case=case.label):
                result = run(sutra_id, dict(case.values)).get("result")
                self.assertNotIn(result, (None, False, [], (), {}, ""),
                                 f"{sutra_id} {case.label} produced nothing")

    def test_and_fires_the_sutra_it_is_offered_under(self):
        """
        The strong one. A case filed under 1.3.17 that comes back citing
        1.3.78 is not a worked example of 1.3.17 — it is a worked example of
        the residue clause, and showing it to a reader would teach the wrong
        thing.
        """
        refusing, blanket = _refusing_sutras()
        for sutra_id, case in self.all_cases:
            if case.kind != "worked" or sutra_id in CITES_ANOTHER:
                continue
            result = run(sutra_id, dict(case.values)).get("result")
            by = result.get("by") if isinstance(result, dict) else None
            if by is None:
                continue
            # A प्रतिषेध does not govern what it excepts, so its own
            # worked input comes back naming the rule that SUPPLIES.
            # Rather than exempting each one by hand, require the
            # stronger thing: that the refusing rule is named in the
            # answer it produced.
            if sutra_id in blanket:
                # Refusing is ALL the rule did, so there is no
                # supplier to answer by and it answers by itself.
                # What has to hold is that it really refused.
                with self.subTest(sutra=sutra_id, case=case.label):
                    self.assertEqual(by, sutra_id)
                    self.assertFalse(
                        result.get("gives"),
                        f"{sutra_id} refuses every affix of its "
                        f"section, so its case must come back with "
                        f"none named")
                continue
            if sutra_id in refusing:
                with self.subTest(sutra=sutra_id, case=case.label):
                    self.assertEqual(
                        result.get("blocked_by"), sutra_id,
                        f"{sutra_id} refuses, so its case should come "
                        f"back by the rule that supplies with "
                        f"{sutra_id} on blocked_by — got {by}")
                continue
            with self.subTest(sutra=sutra_id, case=case.label):
                if sutra_id in str(by):
                    continue
                # A heading confers no compound and joins no pair; its
                # worked form necessarily fires under a rule it governs.
                # Asking a heading to fire itself is asking it to stop
                # being a heading, so the requirement for one is that the
                # rule that did fire falls inside its range.
                span = _heading_range(sutra_id)
                self.assertIsNotNone(
                    span, f"{sutra_id} {case.label} came back by {by}")
                self.assertTrue(
                    _within(str(by), span),
                    f"{sutra_id} governs {span[0]}–{span[1]} but its case "
                    f"{case.label} fired {by}, outside that range",
                )

    def test_the_exceptions_are_few_and_each_gives_a_reason(self):
        """
        The cap is the point of the dict. It went over once, from
        four entries of a single shape — प्रतिषेध rules answering
        by their supplier — and the answer was not to raise it but
        to teach the test that shape, which it now checks harder
        than the exemption did.
        """
        self.assertLess(len(CITES_ANOTHER), 10)
        for sutra_id, reason in CITES_ANOTHER.items():
            self.assertTrue(REGISTRY.has(sutra_id), sutra_id)
            self.assertGreater(len(reason), 40, sutra_id)

    def test_a_counter_case_is_a_counter_case(self):
        """
        A case marked as one must actually fail to reach its sūtra — otherwise
        it is a worked example wearing the wrong label, and the ✕ beside it in
        the UI would be a lie.
        """
        checked = 0
        for sutra_id, case in self.all_cases:
            if case.kind != "counter":
                continue
            result = run(sutra_id, dict(case.values)).get("result")
            by = result.get("by") if isinstance(result, dict) else None
            if by is None:
                continue
            checked += 1
            with self.subTest(sutra=sutra_id, case=case.label):
                self.assertNotIn(sutra_id, str(by),
                                 f"{sutra_id} {case.label} is labelled a "
                                 f"counter-example but the rule fired")
        self.assertGreaterEqual(checked, 20)


class TheFieldsMatch(unittest.TestCase):
    def test_every_case_names_only_fields_the_form_has(self):
        """
        A value under a name the form does not offer is silently dropped, and
        the case then quietly tests something else.
        """
        for sutra in REGISTRY.all():
            sutra_id = str(sutra.id)
            names = {field.name for field in spec_for(sutra_id).fields}
            for case in cases_for(sutra_id):
                unknown = set(case.values) - names
                self.assertEqual(unknown, set(),
                                 f"{sutra_id} {case.label}: {unknown}")

    def test_every_case_carries_a_label(self):
        for sutra in REGISTRY.all():
            for case in cases_for(str(sutra.id)):
                self.assertTrue(case.label.strip(), str(sutra.id))
                self.assertIn(case.kind, ("worked", "counter"))


class TheBugsThisFound(unittest.TestCase):
    """
    Six faults in the form-to-function coercion, none visible from Python.

    All six had the same shape — a value that means one thing in a web form
    meaning something else to a signature — and all six made a rule report
    the wrong sūtra rather than fail, which is the kind of bug that survives.

    The last three came out of the first three: once a blank optional text
    field stopped arriving as "", the echoed call showed what the other
    blank fields were still doing.
    """

    def test_an_empty_optional_text_field_means_not_stated(self):
        """
        It used to arrive as "", which a condition reads as *stated, as the
        empty string* — and nothing matches that, so the rule silently failed
        and the answer fell through to the residue clause. 1.3.66 भुजोऽनवने
        came out parasmaipada with nothing in the form but its own root.
        """
        outcome = run("1.3.66", {"root": "bhuj"})
        self.assertEqual(outcome["result"]["by"], "1.3.66")

        field = next(f for f in spec_for("1.3.66").fields if f.name == "sense")
        self.assertTrue(field.optional)

    def test_a_select_field_arrives_as_the_enum_member(self):
        """
        It used to arrive as the enum's *value*, and code comparing with `is`
        never matched — 1.1.28's dik-samāsa condition failed that way and the
        rule reported 1.1.27.
        """
        outcome = run("1.1.28", {"word": "pūrva",
                                 "samasa": "diksamāsa-bahuvrīhi",
                                 "before_jas": True})
        self.assertEqual(outcome["result"]["by"], "1.1.28")

    def test_a_list_of_objects_has_a_written_form(self):
        """
        Four rules took a list of dataclasses or enums, which no form can
        produce, so they were unreachable from the UI entirely. Each now has a
        string-taking entry point.
        """
        for sutra_id, values in (
            ("1.2.64", {"words": ["vṛkṣa", "vṛkṣa"]}),
            ("1.2.40", {"accents": ["anudātta", "udātta"]}),
            ("1.3.9", {"form": "ḍukṛñ"}),
            ("1.4.2", {"candidates": ["7.3.101", "7.3.103"]}),
        ):
            with self.subTest(sutra=sutra_id):
                outcome = run(sutra_id, values)
                self.assertTrue(outcome["ok"], outcome.get("error"))
                self.assertNotIn(outcome["result"], (None, [], {}, ""))

    def test_and_the_written_forms_take_their_tags(self):
        """
        1.2.65 turns on nothing but whether a name is the gotra's or the
        descendant's, and a bare string cannot say. `gārgya:vṛddha` can.
        """
        outcome = run("1.2.65", {"words": ["gārgya:vṛddha", "gārgya:yuvan"]})
        self.assertEqual(outcome["result"]["by"], "1.2.65")

    def test_an_empty_optional_number_means_not_stated_too(self):
        """
        The same fault as the text field, found by reading the echoed call
        rather than the answer: a blank Optional[int] arrived as 0, so
        2.1.6 reported having been asked about vibhakti 0 when it had been
        asked about nothing. Here the answer happened to be right, which is
        why only the echo showed it.
        """
        called = run("2.1.6", {"first": "upa", "second": "kumbha",
                               "sense": "samīpa"})["called"]
        self.assertIn("None", called)
        self.assertNotIn(", 0,", called)

    def test_a_blank_list_field_is_not_a_list_holding_the_word_None(self):
        """
        `str(None).split(",")` is `["None"]`, so every blank list field
        arrived carrying a member no membership test could match — and the
        reason was invisible, since "None" looks like emptiness in a form.
        """
        called = run("2.1.6", {"first": "upa", "second": "kumbha",
                               "sense": "samīpa"})["called"]
        self.assertNotIn("'None'", called)

    def test_a_float_field_is_not_parsed_as_an_integer(self):
        """
        1.4.109 measures the interval between two sounds in mātrās and the
        Kāśikā's threshold is *half* of one — अर्धमात्राकालव्यवधानम्. The
        number branch parsed with int(), which threw on "0.5" and fell back
        to 0. Zero is also saṃhitā, so दध्यत्र came out right for a reason
        that had nothing to do with what was typed.

        The proof that the value now arrives is the other end: three mātrās
        apart must *not* be saṃhitā, and under the old coercion it was.
        """
        close = run("1.4.109", {"gap_matras": 0.5})
        self.assertEqual(close["result"]["by"], "1.4.109")
        self.assertIn("0.5", close["called"])

        apart = run("1.4.109", {"gap_matras": 3})
        self.assertNotEqual(apart["result"].get("by"), "1.4.109")

        field = next(f for f in spec_for("1.4.109").fields
                     if f.name == "gap_matras")
        self.assertFalse(field.whole)


if __name__ == "__main__":
    unittest.main()


class EveryChipStandsOnItsOwn(unittest.TestCase):
    """
    A chip label is read by someone who has not read the chip beside it.

    They arrive at one sūtra, see a row of small labels, and click one. The
    label is the whole of what they have to go on, so it has to be a claim
    and not half of one. "but ए is not" failed both ways at once: it did not
    say what ए fails to be, and its "but" pointed at a chip the reader may
    never have looked at.

    The ✕ already carries the contrast. A label that spends a word saying
    what the icon says has less room for the part that was missing.
    """

    LEANS = re.compile(
        r"^(but|and|or|nor|though|yet|so does|so do|the same)\b"
        r"|\b(likewise|as well|too|either|also)\s*$",
        re.IGNORECASE,
    )

    DANGLES = re.compile(
        r"\b(does not|do not|is not|are not|did not|cannot|will not"
        r"|does|is|are|has|have|not|no|the|a|an|of|for|in|on|with)\s*$",
        re.IGNORECASE,
    )

    def setUp(self):
        self.labels = [
            (str(sutra.id), case.label)
            for sutra in REGISTRY.all()
            for case in cases_for(str(sutra.id))
        ]
        self.assertGreater(len(self.labels), 400)

    def test_none_of_them_opens_by_pointing_at_a_neighbour(self):
        for sutra_id, label in self.labels:
            with self.subTest(sutra=sutra_id, label=label):
                self.assertIsNone(
                    self.LEANS.search(label.strip()),
                    f"{sutra_id}: {label!r} only makes sense after reading "
                    f"another chip",
                )

    def test_none_of_them_stops_on_a_dangling_verb(self):
        """
        "an unmarked affix does not" — does not *what*? The complement is
        the informative half, and it is the half that went missing.
        """
        for sutra_id, label in self.labels:
            with self.subTest(sutra=sutra_id, label=label):
                self.assertIsNone(
                    self.DANGLES.search(label.strip()),
                    f"{sutra_id}: {label!r} stops before saying what",
                )

    def test_they_are_still_short_enough_to_be_chips(self):
        """
        The fix for a fragment is a complement, not a sentence. Measured
        with the roman half of each pair collapsed, since देव (iast) is one
        term to read rather than two.
        """
        collapsed = re.compile(r"\s*\([^)]*\)")
        for sutra_id, label in self.labels:
            plain = collapsed.sub("", label)
            with self.subTest(sutra=sutra_id, label=label):
                self.assertLessEqual(len(plain), 72, f"{sutra_id}: {label!r}")
