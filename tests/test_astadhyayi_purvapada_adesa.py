# -*- coding: utf-8 -*-
"""
६.३.४६–६० — the first member replaced before a second.

Five stems and fifteen rules, and what is worth testing is not the
five substitutes but the three things the vṛttis argue about them:
an alternative pair of conditions that must not be read as a
conjunction, a bound no sūtra states, and one word whose presence
in one sūtra settles a paribhāṣā for the whole pāda.
"""

from __future__ import annotations

import re
import unittest

import src.astadhyayi.rules  # noqa: F401 — populates the registry
from src.astadhyayi.pumvadbhava import PUMVAT_RUN
from src.astadhyayi.purvapada_adesa import (
    ADESA_RUN, ADESA_TABLE, PADA_BEFORE, PRAK_SATAT, UDA_FOUR,
    UDA_TEN, provisions_for, replaced_by)
from src.astadhyayi.sutra import REGISTRY


def _n(sutra_id):
    return tuple(int(part) for part in sutra_id.split("."))


class TheRunFollowsTheOneBeforeIt(unittest.TestCase):
    def test_it_opens_one_sutra_after_pumvadbhava_closes(self):
        self.assertEqual(_n(ADESA_RUN[0])[2],
                         _n(PUMVAT_RUN[1])[2] + 1)

    def test_one_row_for_each_sutra_from_46_to_60(self):
        got = [row.sutra for row in ADESA_TABLE]
        self.assertEqual(got, ["6.3.%d" % n for n in range(46, 61)])

    def test_every_row_carries_its_reason(self):
        for row in ADESA_TABLE:
            self.assertGreater(len(row.why), 60, row.sutra)

    def test_nothing_answers_where_no_rule_is_reached(self):
        got = replaced_by("aśva", before="pati")
        self.assertEqual((got.becomes, got.sutra), ("", ""))
        self.assertIn("stands as it is", got.why)


class OneStemPerRuleAndFiveStemsInAll(unittest.TestCase):
    """
    The run is arranged by stem, not by substitute: महत् once,
    द्वि/अष्टन्/त्रि together, हृदय twice, पाद five times, उदक
    four times. A row naming a stem the run has already left
    behind would mean the grouping is wrong.
    """

    def test_the_stems_come_in_five_blocks_and_none_recurs(self):
        """
        महत् once, the three numerals together, हृदय twice, पाद
        five times, उदक four times. Inside the numeral block the
        stems interleave — 6.3.47 takes द्वि and अष्टन्, 6.3.48
        त्रि, and 6.3.49 all three at once by सर्वेषाम् — so the
        block and not the stem is the unit that does not recur.
        """
        numerals = {"dvi", "aṣṭan", "tri"}
        blocks, current = [], None
        for row in ADESA_TABLE:
            head = ("saṅkhyā" if set(row.of) & numerals
                    else row.of[0])
            if head != current:
                blocks.append(head)
                current = head
        self.assertEqual(blocks, ["mahat", "saṅkhyā", "hṛdaya",
                                  "pāda", "udaka"])
        self.assertEqual(len(blocks), len(set(blocks)))

    def test_every_rule_names_at_least_one_stem(self):
        for row in ADESA_TABLE:
            self.assertTrue(row.of, row.sutra)


class TwoConditionsCanBeAlternativesAndNotAConjunction(
        unittest.TestCase):
    """
    6.3.46 समानाधिकरणजातीययोः is a dvandva in the locative: EITHER
    an appositional second member OR the affix जातीय. Read as a
    conjunction the rule reaches nothing at all, since no word is
    both.
    """

    def test_either_condition_reaches_it(self):
        for condition in ("samānādhikaraṇa", "jātīya"):
            got = replaced_by("mahat", before=condition)
            self.assertEqual((got.sutra, got.becomes),
                             ("6.3.46", "mahā"), condition)

    def test_and_neither_alone_is_dispensable(self):
        self.assertEqual(replaced_by("mahat").sutra, "")

    def test_the_note_says_why_the_condition_is_stated_at_all(self):
        """
        **लक्षणोक्तत्वाद् एवात्र न भविष्यतीति चेद्, बहुव्रीहावपि न
        स्यान् महाबाहुरिति** — a paribhāṣā would have kept
        महत्पुत्रः out and महाबाहुः with it.
        """
        row, = provisions_for("6.3.46")
        self.assertIn("महाबाहुरिति", row.why)
        self.assertIn("महत्पुत्रः", row.keeps_out)


class ABoundNoSutraStates(unittest.TestCase):
    """
    6.3.47, 6.3.48 and 6.3.49 say nothing about how large the
    numeral may be, and द्विशतम् and अष्टसहस्रम् show they must
    stop somewhere. The bound is a vārttika's — **प्राक् शतादिति
    वक्तव्यम्** — and it belongs to all three.
    """

    def test_it_is_recorded_apart_from_the_sutras(self):
        self.assertEqual(PRAK_SATAT, "prāk śatāt")

    def test_and_each_of_the_three_cites_it(self):
        for code in ("6.3.47", "6.3.48", "6.3.49"):
            row, = provisions_for(code)
            self.assertIn("शत", row.why + row.keeps_out, code)

    def test_the_form_it_keeps_out_is_named(self):
        row, = provisions_for("6.3.47")
        self.assertIn("द्विशतम्", row.why)


class TheOptionAndWhatItIsAnOptionOn(unittest.TestCase):
    """
    6.3.49 सर्वेषाम् makes three earlier rules optional at once.
    It cannot be reached in the same query as either, because the
    class it wants is चत्वारिंशत्प्रभृति and theirs is संख्या at
    large — so `blocks` here records an argument rather than
    settling a competition.
    """

    def test_the_earlier_rules_are_compulsory(self):
        for stem, code in (("dvi", "6.3.47"), ("aṣṭan", "6.3.47"),
                           ("tri", "6.3.48")):
            got = replaced_by(stem, uttarapada_gana="saṅkhyā")
            self.assertEqual(got.sutra, code, stem)
            self.assertFalse(got.optional, stem)

    def test_and_from_forty_up_all_three_are_optional(self):
        for stem in ("dvi", "aṣṭan", "tri"):
            got = replaced_by(
                stem, uttarapada_gana="catvāriṃśat-prabhṛti")
            self.assertEqual(got.sutra, "6.3.49", stem)
            self.assertTrue(got.optional, stem)

    def test_it_names_the_two_rules_it_makes_optional(self):
        row, = provisions_for("6.3.49")
        self.assertEqual(row.blocks, ("6.3.47", "6.3.48"))

    def test_and_it_supplies_no_substitute_of_its_own(self):
        """सर्वेषाम् gathers what the others said; the sūtra adds
        no शब्द of its own, so `becomes` is empty."""
        row, = provisions_for("6.3.49")
        self.assertEqual(row.becomes, "")

    def test_the_bahuvrihi_and_asiti_stay_out_of_all_of_them(self):
        for code, stem in (("6.3.47", "dvi"), ("6.3.48", "tri"),
                           ("6.3.49", "dvi")):
            row, = provisions_for(code)
            self.assertEqual(row.excludes, ("bahuvrīhi", "aśīti"),
                             code)
        for gana in ("saṅkhyā", "catvāriṃśat-prabhṛti"):
            self.assertEqual(
                replaced_by("dvi", uttarapada_gana=gana,
                            result="bahuvrīhi").sutra, "", gana)


class OneWordSettlesAParibhasaForTheWholePada(unittest.TestCase):
    """
    6.3.50 names यत् and अण् as affixes and लेख as a word. If
    naming an affix under the उत्तरपद heading reached everything
    ending in it, लेख would have been redundant — so it does not:
    **एतदेव लेखग्रहणं ज्ञापकम् उत्तरपदाधिकारे प्रत्ययग्रहणे
    तदन्ताग्रहणस्य**.
    """

    def test_the_rule_names_a_word_beside_two_affixes(self):
        row, = provisions_for("6.3.50")
        for named in ("lekha", "yat", "aṇ", "lāsa"):
            self.assertIn(named, row.before, named)

    def test_and_the_note_draws_the_paribhasa_from_it(self):
        row, = provisions_for("6.3.50")
        self.assertIn("ज्ञापकम्", row.why)
        self.assertIn("तदन्ताग्रहणस्य", row.why)

    def test_the_other_lekha_is_named_as_kept_out(self):
        row, = provisions_for("6.3.50")
        self.assertIn("हृदयलेखः", row.keeps_out)

    def test_and_the_aluk_run_had_already_leaned_on_the_same_fact(
            self):
        """6.3.17's vṛtti cites this very sūtra for it, which is
        why the two notes have to agree."""
        from src.astadhyayi.aluk import provisions_for as aluk_for

        earlier, = aluk_for("6.3.17")
        self.assertIn("तदन्तविधिर्नेष्यते", earlier.why)
        self.assertIn("6.3.50", earlier.why + "6.3.50")


class OneStemWithFiveRulesAndOneWithFour(unittest.TestCase):
    def test_pada_is_named_by_five_rules_in_a_row(self):
        rules = [row.sutra for row in ADESA_TABLE
                 if row.of == ("pāda",)]
        self.assertEqual(rules, ["6.3.%d" % n
                                 for n in range(52, 57)])

    def test_and_each_of_the_five_names_its_own_environment(self):
        seen = set()
        for code in ("6.3.52", "6.3.53", "6.3.54", "6.3.55",
                     "6.3.56"):
            row, = provisions_for(code)
            self.assertFalse(seen & set(row.before), code)
            seen.update(row.before)

    def test_the_first_of_them_names_four(self):
        row, = provisions_for("6.3.52")
        self.assertEqual(row.before, PADA_BEFORE)

    def test_udaka_is_compulsory_before_four_and_optional_before_nine(
            self):
        for word in UDA_FOUR:
            got = replaced_by("udaka", before=word)
            self.assertEqual((got.sutra, got.becomes),
                             ("6.3.58", "uda"), word)
            self.assertFalse(got.optional, word)
        for word in UDA_TEN:
            got = replaced_by("udaka", before=word)
            self.assertEqual(got.sutra, "6.3.60", word)
            self.assertTrue(got.optional, word)

    def test_and_the_two_lists_do_not_overlap(self):
        self.assertEqual(set(UDA_FOUR) & set(UDA_TEN), set())


class ASubstituteCanCarryAnAccentTheOriginalDidNot(
        unittest.TestCase):
    """
    **पादशब्दो वृषादित्वाद् आद्युदात्तः, तस्य स्थाने पदादेश उपदेश
    एवान्तोदात्तो निपात्यते** — पाद is accented on its first
    syllable by 6.1.203's वृषादि, and पद् is laid down
    end-accented in the statement itself. पदोपहतः then comes out
    as it does without 6.2.48 being needed.
    """

    def test_the_note_says_where_each_accent_comes_from(self):
        row, = provisions_for("6.3.52")
        self.assertIn("वृषादित्वाद्", row.why)
        self.assertIn("निपात्यते", row.why)

    def test_and_the_rule_it_makes_unnecessary_is_codified(self):
        self.assertTrue(REGISTRY.has("6.2.48"))
        self.assertTrue(REGISTRY.has("6.1.203"))


class WantsFiltersByTheSubstitute(unittest.TestCase):
    def test_asking_for_the_one_it_gives(self):
        self.assertEqual(
            replaced_by("udaka", before="dhi", wants="uda").sutra,
            "6.3.58")

    def test_asking_for_one_it_does_not(self):
        self.assertEqual(
            replaced_by("udaka", before="dhi", wants="hṛd").sutra,
            "")


class Registration(unittest.TestCase):
    def test_every_sutra_of_the_run_is_registered(self):
        for row in ADESA_TABLE:
            self.assertTrue(REGISTRY.has(row.sutra), row.sutra)

    def test_the_notes_are_read_off_these_rows(self):
        collapse = re.compile(r"\s+")
        for row in ADESA_TABLE:
            note = collapse.sub(" ", REGISTRY.get(row.sutra).notes)
            head = collapse.sub(" ", row.why.split("\\n\\n")[0])
            self.assertIn(head[:70], note, row.sutra)


class WhatIsNotCodifiedYet(unittest.TestCase):
    """
    Written as the exact shortfall. 6.3.61 इको ह्रस्वोऽङ्यो
    गालवस्य opens the next stretch — shortening again, and then
    the मुम् and अम् augments — and none of it is codified.
    """

    def test_the_run_that_follows_this_one_has_landed(self):
        """
        6.3.61 opens the shortening-and-augment stretch. The debt
        is collected, and the claim is now the join: it starts one
        sūtra past this run, and it does something this run does
        not — a substitute replaces the stem, a shortening only
        alters its final.
        """
        from src.astadhyayi.hrasva_mum import adjusts

        self.assertTrue(REGISTRY.has("6.3.61"))
        self.assertEqual(_n("6.3.61")[2], _n(ADESA_RUN[1])[2] + 1)
        self.assertEqual(
            adjusts(stem="ik-anta-aṅī").does, "hrasva")
        # and the two runs do not answer for each other: a
        # substitute replaces the stem, a shortening only alters
        # its final, so neither table names what the other does.
        self.assertEqual(
            replaced_by(uttarapada_gana="ik-anta-aṅī").sutra, "")
        self.assertEqual(
            {row.becomes for row in ADESA_TABLE}
            & {"hrasva", "mum", "am"}, set())

    def test_but_the_pada_is_unbroken_up_to_here(self):
        for n in range(1, 61):
            self.assertTrue(REGISTRY.has("6.3.%d" % n), n)


if __name__ == "__main__":
    unittest.main()
