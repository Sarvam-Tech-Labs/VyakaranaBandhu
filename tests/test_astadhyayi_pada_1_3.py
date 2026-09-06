# -*- coding: utf-8 -*-
"""
Tests for 1.3.1 and 1.3.10 to 1.3.13.

Three of these are checkable against something this project did not write, which
is what makes them worth more than the rest:

  1.3.1   the roots are the dhātupāṭha's, and the Kāśikā's first three
          examples are its first three entries.
  1.3.11  the Kāśikā names six adhikāras; the corpus independently marks all
          six, five of them with an explicit scope-end.
  1.3.12  all four of its worked roots are in the dhātupāṭha carrying exactly
          the mark the sūtra asks for — two by accent, two by an indicatory ṅ.

1.3.10's test is the opposite kind: it exists to prove the function REFUSES the
case it should. A silent `zip` over unequal lists would truncate and look right.
"""

from __future__ import annotations

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi import reading
from src.astadhyayi.corpus import load_dhatupatha
from src.astadhyayi.itsamjna import DHATU, analyze
from src.astadhyayi.corpus import ANUDATTA
from src.astadhyayi.pada import (
    Pada,
    atmanepada_roots,
    entries_for,
    is_anudattet,
    is_ngit,
    is_svaritet,
    marks_of,
    pada_of,
)
from src.astadhyayi.samjna import dhatu_count, is_dhatu
from src.astadhyayi.sources import all_sutra_ids, facts


class Dhatu(unittest.TestCase):
    """1.3.1 भूवादयो धातवः."""

    def test_the_kasikas_three_examples_are_the_first_three_entries(self):
        """भू (धा.पा. १), एध (२), स्पर्ध (३) — the sūtra points at a list and
        the list is on disk."""
        entries = load_dhatupatha()
        self.assertEqual(entries["01.0001"].upadesa, "bhū")
        self.assertEqual(analyze(entries["01.0002"].upadesa, DHATU).stem, "edh")
        self.assertEqual(
            analyze(entries["01.0003"].upadesa, DHATU).stem, "spardh"
        )

    def test_it_is_the_whole_enumeration(self):
        self.assertEqual(dhatu_count(), len(load_dhatupatha()))
        self.assertGreater(dhatu_count(), 2000)

    def test_a_root_is_found_by_either_name(self):
        """डुकृञ् and कृ are one root asked for two ways."""
        self.assertTrue(is_dhatu("ḍukṛñ"))
        self.assertTrue(is_dhatu("kṛ"))
        self.assertTrue(is_dhatu("bhū"))

    def test_an_ordinary_word_is_not_a_root(self):
        for word in ("rāma", "agni", "kuṇḍa"):
            self.assertFalse(is_dhatu(word), word)

    def test_the_derived_roots_are_out_of_scope_and_say_so(self):
        """
        3.1.32 सनाद्यन्ता धातवः makes a stem in सन् and the rest a root too.
        Not codified, so is_dhatu answers for the enumerated roots only, and
        the record has to say which.
        """
        from src.astadhyayi.sutra import REGISTRY

        notes = REGISTRY.get("1.3.1").notes
        self.assertIn("SCOPE", notes)
        self.assertIn("3.1.32", notes)


class Yathasamkhya(unittest.TestCase):
    """1.3.10 यथासंख्यमनुदेशः समानाम्."""

    def test_equal_lists_pair_in_order(self):
        """प्रथमात् प्रथमः, द्वितीयाद् द्वितीयः."""
        self.assertEqual(
            reading.yathasamkhya(["a", "b", "c"], ["x", "y", "z"]),
            (("a", "x"), ("b", "y"), ("c", "z")),
        )

    def test_unequal_lists_do_not_pair_at_all(self):
        """
        समानामिति किम्? 1.4.90 has five senses against three words, and the
        answer is that they do NOT correspond — each word holds for any sense.
        Truncating to three pairs would drop two senses and look plausible.
        """
        self.assertIsNone(reading.yathasamkhya(["a", "b", "c"], ["x", "y"]))
        self.assertIsNone(reading.yathasamkhya(["a"], ["x", "y", "z"]))

    def test_the_two_sutras_the_kasika_contrasts(self):
        """4.3.94 pairs, 1.4.90 does not — and the counts are why."""
        four_places = ["tūdī", "śalātura", "varmatī", "kūcavāra"]
        four_affixes = ["ḍhak", "chaṇ", "ḍhañ", "yak"]
        self.assertIsNotNone(
            reading.yathasamkhya(four_places, four_affixes)
        )

        five_senses = ["lakṣaṇa", "itthaṃbhūta", "ākhyāna", "bhāga", "vīpsā"]
        three_words = ["prati", "pari", "anu"]
        self.assertIsNone(reading.yathasamkhya(five_senses, three_words))

    def test_empty_lists_do_not_pair(self):
        self.assertIsNone(reading.yathasamkhya([], []))


class Adhikara(unittest.TestCase):
    """1.3.11 स्वरितेनाधिकारः."""

    #: The six the Kāśikā names, with the end the corpus records.
    NAMED = {
        "3.1.91": "3.4.117",
        "4.1.1": "5.4.160",
        "6.4.1": "7.4.97",
        "6.4.129": "6.4.175",
        "8.1.16": "8.3.55",
    }

    def test_the_kasikas_headings_are_all_marked_in_the_corpus(self):
        """
        Two texts agreeing on six headings is a check on the scope data that
        3,498 sūtras depend on.
        """
        for sutra_id, ends in self.NAMED.items():
            found = reading.adhikara(sutra_id)
            self.assertIsNotNone(found, sutra_id)
            self.assertEqual(found.ends_at, ends, sutra_id)

    def test_a_heading_governs_from_itself_to_its_end(self):
        governed = reading.governs("6.4.1")
        self.assertEqual(governed[0], "6.4.1")
        self.assertEqual(governed[-1], "7.4.97")
        self.assertGreater(len(governed), 500)

    def test_an_ordinary_sutra_is_not_a_heading(self):
        for sutra_id in ("1.1.1", "1.1.9", "6.4.23"):
            self.assertIsNone(reading.adhikara(sutra_id), sutra_id)

    def test_headings_can_nest(self):
        """6.4.23 falls under 6.4.1 and under a nearer heading as well."""
        over = reading.headings_over("6.4.23")
        self.assertIn("6.4.1", over)
        self.assertGreater(len(over), 1)

    def test_the_two_readings_of_scope_agree(self):
        """
        `governs` walks a heading's range; `headings_over` reads what the
        corpus records for each sūtra. They are different data paths and must
        not disagree.
        """
        for heading in self.NAMED:
            for member in reading.governs(heading)[:60]:
                if member == heading:
                    continue
                self.assertIn(heading, reading.headings_over(member),
                              f"{member} under {heading}")

    def test_every_sutra_the_corpus_puts_under_a_heading_has_one(self):
        under = [s for s in all_sutra_ids() if facts(s).adhikara]
        self.assertGreater(len(under), 3000)
        for sutra_id in under[:200]:
            self.assertTrue(reading.headings_over(sutra_id), sutra_id)

    def test_the_open_question_about_3_1_1_is_recorded(self):
        """
        The Kāśikā's sixth example is 3.1.1 प्रत्ययः, which the corpus types a
        saṃjñā with no scope-end. It is plainly both. Not settled here, and the
        record has to say so rather than quietly admitting it.
        """
        from src.astadhyayi.sutra import REGISTRY

        notes = REGISTRY.get("1.3.11").notes
        self.assertIn("OPEN", notes)
        self.assertIn("3.1.1", notes)


class PadaAssignment(unittest.TestCase):
    """1.3.12 अनुदात्तङित आत्मनेपदम् with 1.3.13 भावकर्मणोः."""

    def test_the_kasikas_two_anudatta_roots(self):
        """आस् → आस्ते, वस् → वस्ते. Both carry the accent in the dhātupāṭha."""
        for root in ("āsa̐", "vasa̐"):
            self.assertTrue(is_anudattet(root), root)
            verdict = pada_of(root)
            self.assertIs(verdict.pada, Pada.ATMANEPADA, root)
            self.assertEqual(verdict.by, "1.3.12", root)

    def test_the_kasikas_two_ngit_roots(self):
        """षूङ् → सूते, शीङ् → शेते. Both carry an indicatory ṅ."""
        for root in ("ṣūṅ", "śīṅ"):
            self.assertTrue(is_ngit(root), root)
            self.assertFalse(is_anudattet(root), root)
            self.assertIs(pada_of(root).pada, Pada.ATMANEPADA, root)

    def test_the_four_are_where_the_kasika_says(self):
        """
        Its numbering is the continuous one — 1021, 1023, 1031, 1032 — and
        Vidyut's is gaṇa-and-serial, but the gaps match: two apart, then one.
        """
        entries = load_dhatupatha()
        self.assertEqual(entries["02.0011"].upadesa.rstrip("̐"), "āsa")
        self.assertEqual(entries["02.0013"].upadesa.rstrip("̐"), "vasa")
        self.assertEqual(entries["02.0025"].upadesa, "ṣūṅ")
        self.assertEqual(entries["02.0026"].upadesa, "śīṅ")

    def test_it_is_a_restriction_so_an_unmarked_root_takes_the_other_set(self):
        """
        तेभ्य एवात्मनेपदं भवति नान्येभ्यः. भू carries neither mark, so भवति.
        """
        verdict = pada_of("bhū")
        self.assertIs(verdict.pada, Pada.PARASMAIPADA)
        self.assertFalse(is_anudattet("bhū"))
        self.assertFalse(is_ngit("bhū"))

    def test_1_3_13_overrides_the_marks_entirely(self):
        """
        भावे and कर्मणि take the middle endings whatever the root is marked
        with — क्रियते कटः. So it has to be tested before 1.3.12, not after.
        """
        verdict = pada_of("bhū", bhava_or_karman=True)
        self.assertIs(verdict.pada, Pada.ATMANEPADA)
        self.assertEqual(verdict.by, "1.3.13")

    def test_karmakartari_is_recorded_as_considered(self):
        """लूयते केदारः स्वयमेव — parasmaipada is still withheld."""
        verdict = pada_of("lū", bhava_or_karman=True, karmakartari=True)
        self.assertIs(verdict.pada, Pada.ATMANEPADA)
        self.assertIn("कर्मकर्तरि", verdict.why)

    def test_the_qualifying_roots_are_read_and_not_listed(self):
        """
        A root qualifies by carrying the accent 1.2.30 names or the marker
        1.3.3 finds. Both are in the dhātupāṭha, so the set is derived.
        """
        qualifying = atmanepada_roots()
        self.assertEqual(len(qualifying), 458)

    def test_the_accent_counts_only_where_it_falls_on_an_it(self):
        """
        The count is 404, not the 1,151 entries that carry an anudātta
        somewhere. The dhātupāṭha marks roots and their it-letters with the
        same sign, and 1.3.12 asks about the it — so position is the rule, not
        a detail of the file format.
        """
        entries = load_dhatupatha().values()
        on_an_it = [e for e in entries if is_anudattet(e.upadesa)
                    and len(entries_for(e.upadesa)) == 1]
        anywhere = [e for e in entries if ANUDATTA in e.accent]

        self.assertGreater(len(anywhere), 2 * len(on_an_it))
        self.assertLess(len(on_an_it), 420)

    def test_the_four_roots_whose_accent_sits_on_the_root_not_the_it(self):
        """
        Each is written with an anudātta, and none of them is अनुदात्तेत्. All
        four take parasmaipada, and three of them need a later sūtra of this
        very pāda to get ātmanepada at all — which is the proof that the
        distinction is doing work rather than being pedantry.
        """
        for root, why in [
            ("viś", "1.3.17 grants निविशते separately"),
            ("gam", "गच्छति; 1.3.29 grants संगच्छते separately"),
            ("śru", "शृणोति; 1.3.29 grants संशृणुते separately"),
            ("krī", "क्रीणाति; ñit, so 1.3.72 or 1.3.18"),
        ]:
            self.assertFalse(is_anudattet(root), f"{root} — {why}")
            self.assertIs(pada_of(root).pada, Pada.PARASMAIPADA, root)

    def test_a_name_read_twice_can_carry_different_marks(self):
        """
        वह् is 01.0720 वहि॒ वृद्धौ, anudāttet, and 01.1159 वह॑ प्रापणे, svaritet.
        The Kāśikā on 1.3.81 means the second — «वह प्रापणे» स्वरितेत् — and
        cites the sense to say so. `artha` is how a caller says the same.
        """
        by_entry = dict((code, marks) for code, _, marks in marks_of("vah"))
        self.assertEqual(by_entry["01.0720"], ("anudāttet",))
        self.assertEqual(by_entry["01.1159"], ("svaritet",))

        self.assertTrue(is_svaritet("vah", artha="prApaRe"))
        self.assertFalse(is_anudattet("vah", artha="prApaRe"))

    def test_every_verdict_names_a_sutra_and_gives_a_reason(self):
        for root, ctx in [("bhū", {}), ("āsa̐", {}), ("ṣūṅ", {}),
                          ("bhū", dict(bhava_or_karman=True))]:
            verdict = pada_of(root, **ctx)
            self.assertIn(verdict.by, ("1.3.12", "1.3.13"))
            self.assertTrue(verdict.why)


class Registration(unittest.TestCase):
    IDS = ("1.3.1", "1.3.10", "1.3.11", "1.3.12", "1.3.13")

    def setUp(self):
        from src.astadhyayi.sutra import REGISTRY
        self.registry = REGISTRY

    def test_each_is_registered_and_executable(self):
        for sutra_id in self.IDS:
            sutra = self.registry.get(sutra_id)
            self.assertIsNotNone(sutra, sutra_id)
            self.assertTrue(callable(sutra.apply), sutra_id)

    def test_the_opening_thirteen_of_1_3_are_continuous(self):
        for number in range(1, 14):
            self.assertTrue(
                self.registry.has(f"1.3.{number}"), f"1.3.{number} missing"
            )

    def test_1_3_13_reads_atmanepada_down_from_1_3_12(self):
        carried = " ".join(self.registry.get("1.3.13").anuvrtti)
        self.assertIn("1.3.12", carried)

    def test_1_3_12_joins_the_accent_block_to_the_it_block(self):
        """
        Its two marks come from 1.2.30 and 1.3.3, both already codified. The
        record should name them, because that is what makes the rule runnable
        without a list of roots.
        """
        notes = self.registry.get("1.3.12").notes
        self.assertIn("1.2.30", notes)
        self.assertIn("1.3.3", notes)


if __name__ == "__main__":
    unittest.main()
