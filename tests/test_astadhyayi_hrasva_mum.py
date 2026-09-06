# -*- coding: utf-8 -*-
"""
६.३.६१–७२ — the shortening, and the augment put into what it left.

Three things here are claims rather than entries.

**The two operations are ordered, and the order is argued from one
word.** 6.3.66 shortens before a खित् and 6.3.67 puts मुम् in
before the same खित्. **मुमा ह्रस्वो न बाध्यते** — and the reason
the shortening goes first is 6.3.67's own **अन्तग्रहणम्**.

**One rule is यथासंख्यम्.** 6.3.65 pairs three stems with three
second members one to one, so a crossed pairing must reach nothing.

**And one augment is likened to an ending.** 6.3.68's
**अम्प्रत्ययवत्** imports five rules at once, and the record has
to say which five or the atideśa is only a word.
"""

from __future__ import annotations

import re
import unittest

import src.astadhyayi.rules  # noqa: F401 — populates the registry
from src.astadhyayi.hrasva_mum import (
    AM_ATIDESA, GALAVA_KEEPS_OUT, HRASVA_RUN, HRASVA_TABLE,
    MUM_STEMS, YATHASAMKHYAM, adjusts, provisions_for)
from src.astadhyayi.purvapada_adesa import ADESA_RUN
from src.astadhyayi.sutra import REGISTRY


def _n(sutra_id):
    return tuple(int(part) for part in sutra_id.split("."))


class TheRunFollowsTheOneBeforeIt(unittest.TestCase):
    def test_it_opens_one_sutra_after_the_substitutions_close(self):
        self.assertEqual(_n(HRASVA_RUN[0])[2],
                         _n(ADESA_RUN[1])[2] + 1)

    def test_one_row_for_each_sutra_from_61_to_72(self):
        got = [row.sutra for row in HRASVA_TABLE]
        self.assertEqual(got, ["6.3.%d" % n for n in range(61, 73)])

    def test_every_row_carries_its_reason(self):
        for row in HRASVA_TABLE:
            self.assertGreater(len(row.why), 60, row.sutra)

    def test_nothing_answers_where_no_rule_is_reached(self):
        got = adjusts("aśva", before="pati")
        self.assertEqual((got.does, got.sutra), ("", ""))
        self.assertIn("no augment", got.why)


class TheRunDoesThreeThingsAndSaysWhich(unittest.TestCase):
    def test_the_operations_are_named(self):
        for row in HRASVA_TABLE:
            self.assertIn(row.does, ("hrasva", "mum", "am"),
                          row.sutra)

    def test_the_shortening_comes_first_and_does_not_come_back(self):
        does = [row.does for row in HRASVA_TABLE]
        self.assertEqual(does[:6], ["hrasva"] * 6)
        self.assertNotIn("hrasva", does[6:])

    def test_and_only_one_rule_gives_am(self):
        giving_am = [row.sutra for row in HRASVA_TABLE
                     if row.does == "am"]
        self.assertEqual(giving_am, ["6.3.68"])


class TheTwoOperationsShareAnEnvironmentAndAreOrdered(
        unittest.TestCase):
    """
    6.3.66 shortens before a खित् and 6.3.67 puts मुम् in before
    the same खित्. Neither displaces the other — **मुमा ह्रस्वो न
    बाध्यते, अन्यथा हि ह्रस्वशासनम् अनर्थकं स्यात्** — and the
    order is read off 6.3.67's word अन्त.
    """

    def test_both_act_before_a_khit(self):
        for code in ("6.3.66", "6.3.67", "6.3.68"):
            row, = provisions_for(code)
            self.assertEqual(row.before, ("khit",), code)

    def test_the_shortening_says_the_augment_does_not_beat_it(self):
        row, = provisions_for("6.3.66")
        self.assertIn("मुमा ह्रस्वो न बाध्यते", row.why)
        self.assertEqual(row.blocks, ())

    def test_and_the_augment_says_it_arrives_after(self):
        row, = provisions_for("6.3.67")
        self.assertIn("अन्तग्रहणं किम्", row.why)
        self.assertIn("ह्रस्वे कृते मुम् भवति", row.why)

    def test_both_except_the_indeclinable(self):
        for code in ("6.3.66", "6.3.67"):
            row, = provisions_for(code)
            self.assertIn("avyaya", row.excludes, code)

    def test_a_vowel_final_stem_gets_the_augment(self):
        got = adjusts(stem="ac-anta", before="khit")
        self.assertEqual((got.sutra, got.does), ("6.3.67", "mum"))

    def test_and_a_non_indeclinable_gets_the_shortening(self):
        got = adjusts(stem="anavyaya", before="khit")
        self.assertEqual((got.sutra, got.does), ("6.3.66", "hrasva"))


class ANarrowerClassInsideAWiderOne(unittest.TestCase):
    """
    6.3.67's अजन्त contains 6.3.68's इजन्त एकाच् entirely — गो is
    vowel-final and one-vowelled at once — so only 6.3.68's saying
    it displaces the other can put it first.
    """

    def test_the_wider_rule_names_a_class_that_covers_the_narrower(
            self):
        self.assertIn("ac-anta", MUM_STEMS)
        narrower, = provisions_for("6.3.68")
        self.assertEqual(narrower.stem, "ic-anta-ekāc")

    def test_and_the_narrower_says_what_it_displaces(self):
        narrower, = provisions_for("6.3.68")
        self.assertEqual(narrower.blocks, ("6.3.67",))

    def test_so_a_one_vowelled_ic_final_stem_takes_am(self):
        got = adjusts(stem="ic-anta-ekāc", before="khit")
        self.assertEqual((got.sutra, got.does), ("6.3.68", "am"))

    def test_the_two_words_it_keeps_out_are_named(self):
        narrower, = provisions_for("6.3.68")
        self.assertIn("त्वङ्मन्यः", narrower.keeps_out)
        self.assertIn("लेखाभ्रुंमन्यः", narrower.keeps_out)


class AnAtidesaImportsRulesAndTheRecordNamesThem(unittest.TestCase):
    """
    **अम्प्रत्ययवच्चेत्यतिदेशाद्
    आत्वपूर्वसवर्णगुणेयङुवङादेशा भवन्ति** — five operations follow
    from one word. Recording the atideśa without recording what it
    brings would leave गांमन्यः unexplained.
    """

    def test_five_are_named(self):
        self.assertEqual(len(AM_ATIDESA), 5)
        for one in ("ātva", "guṇa", "iyaṅ", "uvaṅ"):
            self.assertIn(one, AM_ATIDESA, one)

    def test_and_the_note_carries_the_vrtti_that_lists_them(self):
        row, = provisions_for("6.3.68")
        self.assertIn("अम्प्रत्ययवच्चेत्यतिदेशाद्", row.why)

    def test_the_note_also_records_a_form_left_unsettled(self):
        """**कथं भवितव्यम्... इति भाष्ये** — the vṛtti reports the
        Mahābhāṣya's reading of श्रिमन्यम् without resolving it,
        and so does the record."""
        row, = provisions_for("6.3.68")
        self.assertIn("भाष्ये", row.why)


class OneRuleIsMatchedOneToOne(unittest.TestCase):
    """
    6.3.65 यथासंख्यम् — three stems and three second members in
    order. A table that merely listed both sides would accept
    इष्टका before तूल, which is not Sanskrit.
    """

    def test_there_are_three_pairs(self):
        self.assertEqual(len(YATHASAMKHYAM), 3)
        row, = provisions_for("6.3.65")
        self.assertEqual(row.pairs, YATHASAMKHYAM)

    def test_each_pairing_is_reached(self):
        for stem, follows in YATHASAMKHYAM:
            got = adjusts(stem, before=follows)
            self.assertEqual((got.sutra, got.does),
                             ("6.3.65", "hrasva"),
                             "%s / %s" % (stem, follows))

    def test_and_no_crossed_pairing_is(self):
        crossed = 0
        for stem, _ in YATHASAMKHYAM:
            for _, follows in YATHASAMKHYAM:
                if (stem, follows) in YATHASAMKHYAM:
                    continue
                self.assertEqual(adjusts(stem, before=follows).sutra,
                                 "", "%s / %s" % (stem, follows))
                crossed += 1
        self.assertEqual(crossed, 6)

    def test_a_word_named_here_reaches_what_ends_in_it(self):
        """
        **इष्टकादिभ्यस् तदन्तस्यापि ग्रहणं भवति** — the opposite of
        what 6.3.50 established for an AFFIX named under the same
        heading, and the two notes have to say so.
        """
        row, = provisions_for("6.3.65")
        self.assertIn("तदन्तस्यापि ग्रहणं भवति", row.why)
        from src.astadhyayi.purvapada_adesa import (
            provisions_for as adesa_for)
        other, = adesa_for("6.3.50")
        self.assertIn("तदन्ताग्रहणस्य", other.why)


class ASettledOptionIsNotAFreeOne(unittest.TestCase):
    """
    6.3.61's विभाषा is व्यवस्थित: it holds in some places and not
    in others, and the vṛtti names the places it does not hold.
    Recording it as a plain option would license कारीषगन्धिपुत्रः.
    """

    def test_the_option_is_carried_through(self):
        self.assertTrue(adjusts(stem="ik-anta-aṅī").optional)

    def test_and_what_it_does_not_reach_is_named(self):
        self.assertIn("kārīṣagandhī", GALAVA_KEEPS_OUT)
        row, = provisions_for("6.3.61")
        self.assertIn("व्यवस्थितविभाषा", row.why)
        for word in GALAVA_KEEPS_OUT:
            self.assertEqual(
                adjusts(word, stem="ik-anta-aṅī").sutra, "", word)

    def test_naming_the_acarya_is_honour_and_not_option(self):
        """**गालवग्रहणं पूजार्थम्। अन्यतरस्यामिति हि वर्तते** —
        the same distinction 6.1.92 and 6.1.130 turned on."""
        row, = provisions_for("6.3.61")
        self.assertIn("पूजार्थम्", row.why)
        self.assertTrue(REGISTRY.has("6.1.130"))


class BahulamAndVibhasaAreKeptApart(unittest.TestCase):
    def test_two_rules_say_bahulam(self):
        got = tuple(row.sutra for row in HRASVA_TABLE if row.bahulam)
        self.assertEqual(got, ("6.3.63", "6.3.64"))

    def test_two_others_say_vibhasa_or_anyatarasyam(self):
        got = tuple(row.sutra for row in HRASVA_TABLE
                    if row.optional and not row.bahulam)
        self.assertEqual(got, ("6.3.61", "6.3.72"))

    def test_the_answer_reports_them_separately(self):
        varied = adjusts(stem="ṅī-āp", result="saṃjñā")
        self.assertTrue(varied.bahulam)
        self.assertFalse(varied.optional)
        optional = adjusts("rātri", before="kṛt")
        self.assertTrue(optional.optional)
        self.assertFalse(optional.bahulam)

    def test_and_the_bahulam_notes_show_it_going_both_ways(self):
        row, = provisions_for("6.3.63")
        self.assertIn("न च भवति", row.why)


class AnOptionThatOnlyGivesWhatWasNotDue(unittest.TestCase):
    """
    6.3.72's विभाषा is अप्राप्त: before a खित् the मुम् is
    compulsory by 6.3.67, so the option can only be about the
    कृदन्तs that are not खित्.
    """

    def test_the_note_says_so(self):
        row, = provisions_for("6.3.72")
        self.assertIn("अप्राप्तविभाषेयम्", row.why)
        self.assertIn("खिति हि नित्यं मुम् भवति", row.why)

    def test_and_before_a_khit_the_compulsory_rule_answers(self):
        got = adjusts("rātri", stem="ac-anta", before="khit")
        self.assertEqual(got.sutra, "6.3.67")
        self.assertFalse(got.optional)

    def test_while_before_an_ordinary_krt_the_option_does(self):
        got = adjusts("rātri", before="kṛt")
        self.assertEqual(got.sutra, "6.3.72")
        self.assertTrue(got.optional)


class WantsFiltersByTheOperation(unittest.TestCase):
    def test_asking_for_the_one_it_does(self):
        self.assertEqual(
            adjusts("arus", before="khit", wants="mum").sutra,
            "6.3.67")

    def test_asking_for_one_it_does_not(self):
        self.assertEqual(
            adjusts("arus", before="khit", wants="hrasva").sutra,
            "")


class Registration(unittest.TestCase):
    def test_every_sutra_of_the_run_is_registered(self):
        for row in HRASVA_TABLE:
            self.assertTrue(REGISTRY.has(row.sutra), row.sutra)

    def test_the_notes_are_read_off_these_rows(self):
        collapse = re.compile(r"\s+")
        for row in HRASVA_TABLE:
            note = collapse.sub(" ", REGISTRY.get(row.sutra).notes)
            head = collapse.sub(" ", row.why.split("\\n\\n")[0])
            self.assertIn(head[:70], note, row.sutra)


class WhatIsNotCodifiedYet(unittest.TestCase):
    """
    Written as the exact shortfall. 6.3.73 नलोपो नञः opens the
    नञ् run — the न् of नञ् dropping, the नुट् put back before a
    vowel, and eleven words in which नञ् keeps its न् — and none
    of it is codified.
    """

    def test_the_run_that_follows_this_one_has_landed(self):
        """
        6.3.73 नलोपो नञः opens the नञ् run. The debt is collected,
        and the claim is the join: it starts one sūtra past this
        run, and what it does is a third thing again — neither a
        shortening nor an augment but the loss of a sound.
        """
        from src.astadhyayi.nan_saha_samana import shaped

        self.assertTrue(REGISTRY.has("6.3.73"))
        self.assertEqual(_n("6.3.73")[2], _n(HRASVA_RUN[1])[2] + 1)
        self.assertEqual(shaped("nañ").becomes, "na-lopa")
        self.assertEqual(adjusts("nañ").sutra, "")

    def test_but_the_pada_is_unbroken_up_to_here(self):
        for n in range(1, 73):
            self.assertTrue(REGISTRY.has("6.3.%d" % n), n)


if __name__ == "__main__":
    unittest.main()
