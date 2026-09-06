# -*- coding: utf-8 -*-
"""
६.४.७१–९५ — the augment अट्, and the semivowel for a final vowel.

Four things are worth holding the table to.

**A run with a deliberate gap.** 6.4.77 is not in this table: it
is `anga.iyan_uvan`, which builds the form because it has to ask
1.1.4 whether the strengthening was stopped. The gap has to be
recorded, not left to be noticed.

**A refusal lifted twice over.** 6.4.74 takes both augments away
after मा; 6.4.75 puts them back VARIOUSLY in the Veda, with मा
and without — so one sūtra lifts a refusal and suspends a grant.

**A rule whose existence teaches about another section.** 6.4.87's
हुश्नुग्रहण shows the यङ्लुक् is ordinary Sanskrit.

**And an anuvṛtti that decides whether a refusal reaches.**
6.4.85's सुपि comes down from 6.4.83, and without it the refusal
would have swallowed 6.4.88's वुक् and बभूव with it.
"""

from __future__ import annotations

import re
import unittest

import src.astadhyayi.rules  # noqa: F401 — populates the registry
from src.astadhyayi.anga_agama import (
    AGAMA_RUN, AGAMA_TABLE, BHU_SUDHI, CODIFIED_APART,
    PAST_LAKARAS, augment_or_yan, provisions_for)
from src.astadhyayi.ardhadhatuka_lopa import LOPA_RUN
from src.astadhyayi.sutra import REGISTRY


def _n(sutra_id):
    return tuple(int(part) for part in sutra_id.split("."))


class TheRunHasADeliberateGap(unittest.TestCase):
    """
    6.4.77 अचि श्नुधातुभ्रुवाम् is codified apart, in
    `anga.iyan_uvan`, because it BUILDS the form and has to ask
    1.1.4 whether the strengthening that would displace it was
    stopped. A table row could only have named the operation.
    """

    def test_the_gap_is_recorded_and_not_merely_left(self):
        self.assertEqual(CODIFIED_APART, ("6.4.77",))
        got = [row.sutra for row in AGAMA_TABLE]
        self.assertNotIn("6.4.77", got)

    def test_and_the_sutra_is_codified_all_the_same(self):
        self.assertTrue(REGISTRY.has("6.4.77"))

    def test_the_table_is_the_run_minus_that_one(self):
        got = [row.sutra for row in AGAMA_TABLE]
        want = ["6.4.%d" % n for n in range(71, 96)
                if "6.4.%d" % n not in CODIFIED_APART]
        self.assertEqual(got, want)

    def test_and_the_rule_that_displaces_it_names_it(self):
        """6.4.81 इणो यण् is an अपवाद of 6.4.77, so the two have
        to agree about which is which."""
        row, = provisions_for("6.4.81")
        self.assertEqual(row.blocks, ("6.4.77",))
        self.assertIn("इयङादेशापवादोऽयम्", row.why)

    def test_and_the_other_module_still_answers_for_it(self):
        from src.astadhyayi.anga import iyan_uvan

        got = iyan_uvan("bhrū", bhru=True, ardhadhatuka=True,
                        dhatu_lopa=True)
        self.assertIsNotNone(got)


class TheRunFollowsTheOneBeforeIt(unittest.TestCase):
    def test_it_opens_one_sutra_after_the_lopa_run(self):
        self.assertEqual(_n(AGAMA_RUN[0])[2], _n(LOPA_RUN[1])[2] + 1)

    def test_every_row_carries_its_reason(self):
        for row in AGAMA_TABLE:
            self.assertGreater(len(row.why), 60, row.sutra)

    def test_nothing_answers_where_no_rule_is_reached(self):
        got = augment_or_yan("pac", before="śap")
        self.assertEqual((got.does, got.sutra), ("", ""))
        self.assertIn("no augment", got.why)


class TheAugmentThatMakesAPastTense(unittest.TestCase):
    """
    6.4.71 gives अट् and 6.4.72 आट्, and both are laid down as
    उदात्त. The accent is part of the rule, so a codification that
    dropped it would be recording less than the sūtra says.
    """

    def test_both_are_udatta_and_they_are_the_only_two(self):
        got = {row.sutra for row in AGAMA_TABLE if row.udatta}
        self.assertEqual(got, {"6.4.71", "6.4.72"})

    def test_and_the_answer_carries_that_through(self):
        for lakara in PAST_LAKARAS:
            got = augment_or_yan(before=lakara)
            self.assertEqual(got.sutra, "6.4.71", lakara)
            self.assertTrue(got.udatta, lakara)

    def test_a_vowel_initial_stem_takes_the_other(self):
        got = augment_or_yan(gana="ac-ādi", before="luṅ")
        self.assertEqual((got.sutra, got.does), ("6.4.72", "āṭ"))
        self.assertEqual(got.blocked_by, ("6.4.71",))

    def test_and_the_veda_has_it_where_no_rule_puts_it(self):
        got = augment_or_yan(chandasi=True)
        self.assertEqual(got.sutra, "6.4.73")
        row, = provisions_for("6.4.73")
        self.assertIn("अनजादीनाम् अपि दृश्यते", row.why)


class ARefusalLiftedAndAGrantSuspendedAtOnce(unittest.TestCase):
    """
    6.4.74 refuses both augments after मा. 6.4.75 then says that
    in the Veda they come and go VARIOUSLY, with मा and without —
    so it lifts the refusal AND suspends the grant, in one sūtra.
    """

    def test_the_refusal_names_both_rules(self):
        row, = provisions_for("6.4.74")
        self.assertTrue(row.refuses)
        self.assertEqual(row.blocks, ("6.4.71", "6.4.72"))

    def test_it_answers_with_nothing_after_ma(self):
        got = augment_or_yan(before="luṅ", result="māṅ-yoga")
        self.assertEqual((got.sutra, got.does), ("6.4.74", ""))

    def test_and_the_veda_lifts_it(self):
        got = augment_or_yan(before="luṅ", chandasi=True)
        self.assertEqual(got.sutra, "6.4.75")
        self.assertTrue(got.bahulam)
        self.assertEqual(got.blocked_by, ("6.4.74",))

    def test_the_note_gives_both_directions(self):
        """Forms without मा that have no augment, and forms with
        मा that do — the two halves of बहुलम्."""
        row, = provisions_for("6.4.75")
        self.assertIn("जनिष्ठा", row.why)
        self.assertIn("मा वः क्षेत्रे", row.why)

    def test_and_it_is_bahulam_and_not_an_option(self):
        row, = provisions_for("6.4.75")
        self.assertTrue(row.bahulam)
        self.assertFalse(row.optional)


class AnAnuvrttiThatDecidesWhetherARefusalReaches(unittest.TestCase):
    """
    6.4.85 न भूसुधियोः names two stems and no environment, and
    सुपि is still running from 6.4.83. Without that anuvṛtti the
    refusal would swallow 6.4.88's वुक् and बभूव with it.
    """

    def test_the_refusal_carries_the_environment_down(self):
        row, = provisions_for("6.4.85")
        self.assertEqual(row.before, ("sup",))
        self.assertEqual(row.of, BHU_SUDHI)

    def test_and_the_rule_it_comes_from_named_it(self):
        earlier, = provisions_for("6.4.83")
        self.assertEqual(earlier.before, ("sup",))

    def test_so_the_refusal_reaches_before_a_sup(self):
        got = augment_or_yan("bhū", before="sup")
        self.assertEqual((got.sutra, got.does), ("6.4.85", ""))

    def test_and_leaves_the_vuk_alone_before_a_lakara(self):
        got = augment_or_yan("bhū", before="liṭ")
        self.assertEqual((got.sutra, got.does), ("6.4.88", "vuk"))

    def test_and_the_note_says_that_is_why(self):
        row, = provisions_for("6.4.85")
        self.assertIn("6.4.88", row.why)
        self.assertIn("सुपि", row.why)

    def test_the_veda_then_lifts_the_refusal_both_ways(self):
        got = augment_or_yan("bhū", before="sup", chandasi=True)
        self.assertEqual(got.sutra, "6.4.86")
        self.assertTrue(got.optional)
        self.assertEqual(got.blocked_by, ("6.4.85",))


class ASutrasExistenceTeachesAboutAnotherSection(unittest.TestCase):
    """
    **इदम् एव हुश्नुग्रहणं ज्ञापकं भाषायाम् अपि यङ्लुग् अस्तीति**
    — if the यङ्लुक् were Vedic only, योयुवति and रोरुवति would
    never arise outside the Veda and there would have been nothing
    for 6.4.87 to keep out by naming हु and श्नु.
    """

    def test_the_note_carries_the_argument(self):
        row, = provisions_for("6.4.87")
        self.assertIn("ज्ञापकं", row.why)
        self.assertIn("यङ्लुग्", row.why)

    def test_and_names_the_forms_it_turns_on(self):
        row, = provisions_for("6.4.87")
        for form in ("योयुवति", "रोरुवति"):
            self.assertIn(form, row.keeps_out, form)

    def test_the_rule_still_answers_for_what_it_does_reach(self):
        for stem, gana in (("hu", ""), ("", "śnu-anta")):
            got = augment_or_yan(stem, gana=gana,
                                 before="sārvadhātuka")
            self.assertEqual(got.sutra, "6.4.87", stem or gana)
            self.assertEqual(got.does, "yaṇ")


class TwoRootsNamedInTheirAlteredShape(unittest.TestCase):
    """
    6.4.89 writes गोह and 6.4.90 writes दोष, and both are the
    roots as they come out rather than as they are taught:
    **विकृतग्रहणं विषयार्थम्** — so the rule reaches only where
    the root has that shape.
    """

    def test_both_notes_say_so(self):
        for code in ("6.4.89", "6.4.90"):
            row, = provisions_for(code)
            self.assertIn("विकृतग्रहणं", row.why, code)

    def test_and_the_second_says_why_it_follows_the_first(self):
        row, = provisions_for("6.4.90")
        self.assertIn("प्रक्रमाभेदार्थम्", row.why)
        self.assertIn("पूर्वत्र हि गोह", row.why)

    def test_the_first_also_stops_a_paribhasa(self):
        """**उपधाया इति किम्? अलोऽन्त्यस्य मा भूत्** — without it
        1.1.52 would have put the substitute at the end."""
        row, = provisions_for("6.4.89")
        self.assertEqual(row.part, "upadhā")
        self.assertIn("अलोऽन्त्यस्य", row.why)
        self.assertTrue(REGISTRY.has("1.1.52"))

    def test_and_a_sense_makes_the_second_optional(self):
        firm = augment_or_yan("doṣ", before="ṇi")
        self.assertEqual(firm.sutra, "6.4.90")
        self.assertFalse(firm.optional)
        loose = augment_or_yan("doṣ", before="ṇi",
                               result="cittavirāga")
        self.assertEqual(loose.sutra, "6.4.91")
        self.assertTrue(loose.optional)


class WhyTheLengthIsGrantedRatherThanTheShorteningMadeOptional(
        unittest.TestCase):
    """
    6.4.93 could have been written as an option on 6.4.92's
    shortening and is not: **दीर्घग्रहणं किम्, न ह्रस्वविकल्प एव
    विधीयते? नैवं शक्यम्** — with a second णि the shortening is
    compulsory by स्थानिवद्भाव, so an option on it would not have
    reached these forms.
    """

    def test_the_shortening_is_compulsory(self):
        got = augment_or_yan(gana="mit", before="ṇi")
        self.assertEqual((got.sutra, got.does), ("6.4.92", "hrasva"))
        self.assertFalse(got.optional)

    def test_and_the_length_is_the_option(self):
        for affix in ("ciṇ", "ṇamul"):
            got = augment_or_yan(gana="mit", before=affix)
            self.assertEqual(got.sutra, "6.4.93", affix)
            self.assertEqual(got.does, "dīrgha", affix)
            self.assertTrue(got.optional, affix)

    def test_and_the_note_says_why_it_was_written_that_way(self):
        row, = provisions_for("6.4.93")
        self.assertIn("दीर्घग्रहणं किम्", row.why)
        self.assertIn("स्थानिवद्भावात्", row.why)

    def test_the_next_rule_shortens_without_the_mit_class(self):
        row, = provisions_for("6.4.94")
        self.assertEqual(row.gana, "")
        self.assertEqual(
            augment_or_yan(before="khac").does, "hrasva")


class OneSubstitutionIsHiddenFromTheRuleAfterIt(unittest.TestCase):
    """
    6.4.76's रे is not seen by 6.4.64, so the आ of धा is still
    there to be dropped: **धाञो रेभावस्यासिद्धत्वाद् आतो लोपः
    भवति** — 6.4.22's असिद्धवत् at work inside its own pāda.
    """

    def test_the_note_names_the_rule_it_is_hidden_from(self):
        row, = provisions_for("6.4.76")
        self.assertIn("6.4.64", row.why)
        # The fragment begins after the junction: रेभावस्य + असिद्धत्वात्
        # swallows the अ, so quoting the word whole would not match.
        self.assertIn("सिद्धत्वाद्", row.why)

    def test_and_that_rule_is_codified(self):
        from src.astadhyayi.ardhadhatuka_lopa import (
            provisions_for as ardha_for)

        self.assertTrue(REGISTRY.has("6.4.64"))
        other, = ardha_for("6.4.64")
        self.assertEqual(other.does, "lopa")

    def test_and_the_heading_that_hides_it_is_codified_too(self):
        self.assertTrue(REGISTRY.has("6.4.22"))


class WantsFiltersByTheOperation(unittest.TestCase):
    def test_asking_for_the_one_it_does(self):
        self.assertEqual(
            augment_or_yan(before="luṅ", wants="aṭ").sutra,
            "6.4.71")

    def test_asking_for_one_it_does_not(self):
        self.assertEqual(
            augment_or_yan(before="luṅ", wants="āṭ").sutra, "")

    def test_a_refusal_supplies_nothing_to_ask_for(self):
        self.assertEqual(
            augment_or_yan("bhū", before="sup", wants="yaṇ").sutra,
            "")


class Registration(unittest.TestCase):
    def test_every_sutra_of_the_table_is_registered(self):
        for row in AGAMA_TABLE:
            self.assertTrue(REGISTRY.has(row.sutra), row.sutra)

    def test_and_so_is_the_one_the_table_leaves_out(self):
        for code in CODIFIED_APART:
            self.assertTrue(REGISTRY.has(code), code)

    def test_the_notes_are_read_off_these_rows(self):
        collapse = re.compile(r"\s+")
        for row in AGAMA_TABLE:
            note = collapse.sub(" ", REGISTRY.get(row.sutra).notes)
            head = collapse.sub(" ", row.why.split("\\n\\n")[0])
            self.assertIn(head[:70], note, row.sutra)


class WhatIsNotCodifiedYet(unittest.TestCase):
    """
    Written as the exact shortfall. 6.4.96 छादेर्घेऽद्व्युपसर्गस्य
    opens the next stretch, and 6.4.96 to 6.4.175 is ahead.
    """

    def test_the_run_that_follows_this_one_has_landed(self):
        """
        6.4.96 opens the losses that make a present tense. The
        debt is collected, and the claim is the join: it starts
        one sūtra past this run, and it takes sounds away where
        this run puts augments in.
        """
        from src.astadhyayi.sarvadhatuka_lopa import (
            before_sarvadhatuka)

        self.assertTrue(REGISTRY.has("6.4.96"))
        self.assertEqual(_n("6.4.96")[2], _n(AGAMA_RUN[1])[2] + 1)
        self.assertEqual(
            before_sarvadhatuka(before="ciṇ").does, "luk")
        self.assertEqual(
            {row.does for row in AGAMA_TABLE} & {"luk"}, set())

    def test_and_the_pada_is_complete_now(self):
        # Written as a debt while 6.4.175 was far off; the pāda
        # has been read through, so the claim is the live one.
        self.assertTrue(REGISTRY.has("6.4.175"))
        self.assertFalse(REGISTRY.has("6.4.176"))

    def test_but_the_pada_is_unbroken_up_to_here(self):
        for n in range(1, 96):
            self.assertTrue(REGISTRY.has("6.4.%d" % n), n)


if __name__ == "__main__":
    unittest.main()
