# -*- coding: utf-8 -*-
"""
Every claim traceable to a source you can check — §1's first line, tested.

The notes quote the commentaries constantly, and for a long time nothing
verified that a quotation attributed to a source was in that source. It
turned out that 30 Sanskrit phrases were credited to the Mahābhāṣya, and the
bhāṣya this project holds is question-openers only: all 220 of its non-empty
readings are one sentence, usually किमर्थम् or किम् इदम्, never the answer.

The content was mostly right — the Kāśikā quotes Patañjali and quotes him
accurately — but a reader following the citation arrived at a forty-character
question that did not contain the claim. That is the failure this file exists
to prevent recurring.

The rule it enforces is not "every phrase must be in the corpus". Plenty of
the tradition is not on disk, and pretending otherwise would be worse. The
rule is: **a phrase is either checkable where the note says, or the note says
it is not checkable.** Nothing may quietly sit between the two.
"""

from __future__ import annotations

import re
import unicodedata
import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi.corpus import all_commentary_on
from src.astadhyayi.sources import readings_for
from src.astadhyayi.sutra import REGISTRY
from src.normalizer import devanagari_to_iast

#: A run of Devanāgarī long enough to be a quotation rather than a term.
QUOTATION = re.compile(r"[ऀ-ॿ][ऀ-ॿ\s]{8,}")

#: A note sentence claiming the bhāṣya as its source.
CITES_BHASYA = re.compile(r"Mahābhāṣya|Patañjali|bhāṣya|म\.भा\.")

#: How a note admits that a quotation cannot be checked here.
ADMITS = re.compile(r"REPORTED|not checkable|not verifiable")


def comparable(text: str) -> str:
    """
    One string both scripts reduce to.

    Three things have to be folded or the comparison is worthless, and each
    of them produced a false result before it was: the sources are written
    in both scripts, editors differ on spacing and daṇḍas, and the nasals
    are inconsistent — saṃjñā and sañjñā are the same word, and matching
    them literally reported phrases absent that the source carries verbatim.
    """
    if re.search(r"[ऀ-ॿ]", text):
        text = devanagari_to_iast(text)
    text = unicodedata.normalize("NFD", text)
    text = re.sub(r"[^a-z]", "", text.lower())
    return re.sub(r"[mn]", "N", text)


def _paragraphs(notes: str):
    return re.split(r"\n\s*\n", notes or "")


class AQuotationIsEitherCheckableOrSaysItIsNot(unittest.TestCase):

    def setUp(self):
        self.claims = []
        for sutra in REGISTRY.all():
            sid = str(sutra.id)
            for para in _paragraphs(sutra.notes):
                if not CITES_BHASYA.search(para):
                    continue
                for phrase in QUOTATION.findall(para):
                    needle = comparable(phrase)[:24]
                    if len(needle) < 12:
                        continue
                    self.claims.append((sid, phrase.strip(), needle, para))
        self.assertGreater(len(self.claims), 8)

    def _sources_carrying(self, sutra_id, needle):
        """
        Every place on disk that could carry this quotation.

        Both paths are asked, because they do not cover the same sūtras.
        `readings_for` draws on the segmented Mahābhāṣya, which has
        nothing for 2.4.1; the per-sūtra commentary files carry the
        bhāṣya on it in full. Asking only the first reported a quotation
        that is in the corpus as absent from it.
        """
        found = []
        for reading in readings_for(sutra_id):
            source = (reading.source.value
                      if hasattr(reading.source, "value")
                      else str(reading.source))
            if needle in comparable(reading.text or ""):
                found.append(source)
        try:
            commentaries = all_commentary_on(sutra_id)
        except Exception:                       # noqa: BLE001 — corpus absent
            commentaries = {}
        for name, text in commentaries.items():
            if needle in comparable(text or ""):
                found.append(name)
        return found

    def test_no_quotation_is_both_unfindable_and_unqualified(self):
        stranded = []
        for sid, phrase, needle, para in self.claims:
            if self._sources_carrying(sid, needle):
                continue
            if ADMITS.search(para):
                continue
            stranded.append(f"{sid}: {' '.join(phrase.split())[:40]}")
        self.assertEqual(
            stranded, [],
            f"{len(stranded)} quotation(s) credited to a source, absent from "
            f"the corpus, and not marked as unchecked: {stranded[:6]}",
        )

    def test_the_bhasya_on_disk_is_still_only_question_openers(self):
        """
        The premise the whole audit rests on. If a fuller bhāṣya is ever
        added this fails, and it should: most of the notes marked
        unverifiable could then be checked properly, and someone should go
        and do it rather than leave the markers standing.
        """
        lengths = []
        for sutra in REGISTRY.all():
            for reading in readings_for(str(sutra.id)):
                source = (reading.source.value
                          if hasattr(reading.source, "value")
                          else str(reading.source))
                if source == "mahabhasya" and (reading.text or "").strip():
                    lengths.append(len(reading.text.strip()))
        self.assertGreater(len(lengths), 100)
        self.assertLess(
            max(lengths), 400,
            "the Mahābhāṣya on disk is longer than question-openers now — "
            "the notes marked REPORTED can be checked, and should be",
        )

    def test_the_markers_are_not_load_bearing_everywhere(self):
        """
        A guard that everything is marked would pass if every note were
        marked, which would make the marker meaningless. Most quotations
        must still be genuinely findable.
        """
        findable = sum(
            1 for sid, _p, needle, _para in self.claims
            if self._sources_carrying(sid, needle))
        self.assertGreaterEqual(
            findable, len(self.claims) // 3,
            "too few quotations are checkable for the marker to mean much",
        )


class TheOpenQuestionOn111StaysOpen(unittest.TestCase):
    """
    Why vṛddhi is defined before guṇa. The maṅgala reading is widely
    reported and the corpus cannot confirm it — the bhāṣya entry for 1.1.1
    is forty-six characters about kutva.
    """

    def test_it_is_still_marked_open_and_says_why(self):
        notes = REGISTRY.get("1.1.1").notes
        self.assertIn("OPEN", notes)
        self.assertIn("maṅgala", notes)
        self.assertIn("CHECKED", notes)

    def test_the_bhasya_entry_for_1_1_1_really_does_not_touch_it(self):
        text = next(
            (r.text or "") for r in readings_for("1.1.1")
            if (r.source.value if hasattr(r.source, "value")
                else str(r.source)) == "mahabhasya")
        self.assertLess(len(text), 120)
        for word in ("maṅgal", "मङ्गल", "vṛddhi", "guṇa"):
            self.assertNotIn(word, text)

    def test_the_mangala_argument_the_corpus_does_carry_is_a_different_one(self):
        """
        1.3.1's व being there for auspiciousness *is* attested locally. It
        is the kind of thing that could be mistaken for confirmation of the
        1.1.1 question, so the note on 1.1.1 says explicitly that it is not.
        """
        carried = any(
            "मङ्गल" in (r.text or "") for r in readings_for("1.3.1"))
        self.assertTrue(carried)
        self.assertIn("1.3.1", REGISTRY.get("1.1.1").notes)


if __name__ == "__main__":
    unittest.main()
