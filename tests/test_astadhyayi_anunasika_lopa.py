# -*- coding: utf-8 -*-
"""
६.४.३४–४५ — शास्, हन्, and the nasal that goes or becomes आ.

Three things here are claims rather than entries.

**A class named by an accent and not by a sound.** 6.4.37's
अनुदात्तोपदेश gathers six roots by how the Dhātupāṭha accents
them, which no phonetic test can find.

**An option that is settled rather than free.** 6.4.38's
व्यवस्थितविभाषा gives the choice to the म्-final roots and to no
others: **अन्यत्र नित्यमेव लोपः**.

**And a refusal that has to refuse twice.** 6.4.39 stops the
nasal-loss, and stopping it leaves the root nasal-final so that
6.4.15 would lengthen instead. The word दीर्घश्च is there for the
case the first half of the sūtra creates.
"""

from __future__ import annotations

import re
import unittest

import src.astadhyayi.rules  # noqa: F401 — populates the registry
from src.astadhyayi.anunasika_lopa import (
    AND_TWO_MORE, ANUDATTOPADESA, JANA_SANA_KHANA, LYAP_OPTIONAL,
    NASAL_RUN, NASAL_TABLE, provisions_for, the_nasal)
from src.astadhyayi.nalopa import NALOPA_RUN
from src.astadhyayi.sutra import REGISTRY


def _n(sutra_id):
    return tuple(int(part) for part in sutra_id.split("."))


class TheRunFollowsTheOneBeforeIt(unittest.TestCase):
    def test_it_opens_one_sutra_after_the_n_dropping_run(self):
        self.assertEqual(_n(NASAL_RUN[0])[2],
                         _n(NALOPA_RUN[1])[2] + 1)

    def test_one_row_for_each_sutra_from_34_to_45(self):
        got = [row.sutra for row in NASAL_TABLE]
        self.assertEqual(got, ["6.4.%d" % n for n in range(34, 46)])

    def test_every_row_carries_its_reason(self):
        for row in NASAL_TABLE:
            self.assertGreater(len(row.why), 60, row.sutra)

    def test_nothing_answers_where_no_rule_is_reached(self):
        got = the_nasal("aś", before="hi")
        self.assertEqual((got.does, got.sutra), ("", ""))
        self.assertIn("keeps its nasal", got.why)

    def test_the_run_does_three_things_to_the_nasal(self):
        does = {row.does for row in NASAL_TABLE if not row.refuses}
        self.assertEqual(does, {"it", "śā", "ja",
                                "anunāsika-lopa", "ā"})


class AClassNamedByAnAccentAndNotBySound(unittest.TestCase):
    """
    **अनुदात्तोपदेशा अनुनासिकान्ता यमिरमिनमिगमिहनिमन्यतयः** — six
    roots, gathered by the accent they carry where the Dhātupāṭha
    teaches them. Nothing in how they sound picks them out, so the
    query has to be told, and the record has to list them.
    """

    def test_the_class_is_six_roots(self):
        self.assertEqual(len(ANUDATTOPADESA), 6)
        for root in ("yam", "gam", "han", "man"):
            self.assertIn(root, ANUDATTOPADESA, root)

    def test_and_the_sutra_adds_two_more_by_name(self):
        self.assertEqual(AND_TWO_MORE, ("van", "tan"))
        row, = provisions_for("6.4.37")
        self.assertEqual(row.gana, "anudāttopadeśa")
        self.assertEqual(row.of, AND_TWO_MORE)

    def test_the_note_lists_the_class_out(self):
        row, = provisions_for("6.4.37")
        self.assertIn("अनुदात्तोपदेशा", row.why)
        self.assertIn("यमिरमिनमिगमिहनिमन्यतयः", row.why)

    def test_the_class_answers_and_a_stray_root_does_not(self):
        self.assertEqual(
            the_nasal(gana="anudāttopadeśa", before="jhal",
                      result="kṅit").sutra, "6.4.37")
        self.assertEqual(
            the_nasal("kram", before="jhal", result="kṅit").sutra,
            "")


class ASettledOptionIsNotAFreeOne(unittest.TestCase):
    """
    6.4.38's विभाषा is व्यवस्थित: **तेन मकारान्तानां विकल्पो
    भवति, अन्यत्र नित्यमेव लोपः**. Recording it as a plain option
    would license *आहम्य beside आहत्य, which is not Sanskrit.
    """

    def test_the_option_is_marked_as_settled(self):
        row, = provisions_for("6.4.38")
        self.assertTrue(row.optional)
        self.assertTrue(row.vyavasthita)

    def test_and_it_is_the_only_one_of_the_run(self):
        got = {row.sutra for row in NASAL_TABLE if row.vyavasthita}
        self.assertEqual(got, {"6.4.38"})

    def test_the_note_names_who_gets_the_choice(self):
        row, = provisions_for("6.4.38")
        self.assertIn("व्यवस्थितविभाषा", row.why)
        self.assertIn("मकारान्तानां", row.why)
        self.assertIn("नित्यमेव लोपः", row.why)

    def test_and_who_gets_it_is_recorded_apart(self):
        """The म्-final roots of the class, and no others."""
        for root in LYAP_OPTIONAL:
            self.assertIn(root, ANUDATTOPADESA, root)
            self.assertTrue(root.endswith("m"), root)
        self.assertNotIn("han", LYAP_OPTIONAL)

    def test_the_answer_carries_both_flags_through(self):
        got = the_nasal(gana="anudāttopadeśa", before="lyap")
        self.assertEqual(got.sutra, "6.4.38")
        self.assertTrue(got.optional)
        self.assertTrue(got.vyavasthita)


class ARefusalThatHasToRefuseTwice(unittest.TestCase):
    """
    **अनुनासिकलोपे प्रतिषिद्धे अनुनासिकस्य क्विझलोः क्ङिति इति
    दीर्घः प्राप्नोति, सोऽपि प्रतिषिध्यते** — stopping the loss
    leaves the root nasal-final, and 6.4.15 then lengthens the
    penult. So 6.4.39 says दीर्घश्च and refuses that too.
    """

    def test_it_is_the_only_refusal_of_the_run(self):
        refusing = {row.sutra for row in NASAL_TABLE if row.refuses}
        self.assertEqual(refusing, {"6.4.39"})

    def test_it_names_two_rules_and_not_one(self):
        row, = provisions_for("6.4.39")
        self.assertEqual(row.blocks, ("6.4.37", "6.4.15"))

    def test_the_second_of_them_is_in_another_module(self):
        """6.4.15 is the lengthening of 6.4.1–21, so the two
        modules have to agree about what it does."""
        from src.astadhyayi.anga_dirgha import (
            provisions_for as dirgha_for)

        other, = dirgha_for("6.4.15")
        self.assertEqual(other.does, "dīrgha")
        self.assertEqual(other.part, "upadhā")

    def test_and_the_note_says_why_the_second_was_needed(self):
        row, = provisions_for("6.4.39")
        self.assertIn("प्रतिषिद्धे", row.why)
        self.assertIn("दीर्घः प्राप्नोति", row.why)

    def test_the_answer_supplies_nothing(self):
        got = the_nasal(gana="anudāttopadeśa", before="ktic")
        self.assertEqual((got.sutra, got.does), ("6.4.39", ""))
        self.assertEqual(got.blocked_by, ("6.4.37", "6.4.15"))


class TwoRootsReplacedWholeBeforeOneAffix(unittest.TestCase):
    """
    6.4.35 and 6.4.36 both act before हि, and both replace the
    whole root rather than a part of it. 6.4.35 says so by
    dropping उपधायाः, which changes what its genitive means.
    """

    def test_both_act_before_hi(self):
        for code in ("6.4.35", "6.4.36"):
            row, = provisions_for(code)
            self.assertEqual(row.before, ("hi",), code)

    def test_and_the_first_says_the_genitive_changed_sense(self):
        row, = provisions_for("6.4.35")
        self.assertIn("उपधाया इति निवृत्तम्", row.why)
        self.assertIn("स्थानेयोगा", row.why)
        self.assertIn("1.1.49", row.why)

    def test_the_rule_that_gives_it_that_sense_is_codified(self):
        self.assertTrue(REGISTRY.has("1.1.49"))

    def test_and_dropping_the_second_condition_widens_it_too(self):
        """**क्ङितीत्येतदपि निवृत्तम्** — so the substitute holds
        even where 3.4.88 makes हि पित्."""
        row, = provisions_for("6.4.35")
        self.assertEqual(row.result, ())
        self.assertIn("3.4.88", row.why)

    def test_each_is_reached_by_its_own_root(self):
        self.assertEqual(the_nasal("śās", before="hi").does, "śā")
        self.assertEqual(the_nasal("han", before="hi").does, "ja")


class TheSameRootUnderTwoRules(unittest.TestCase):
    """
    गम् drops its nasal by 6.4.37 as one of the accent-class, and
    by 6.4.40 by being named. The two are told apart by the affix
    — a झल्-initial कित् for the first, क्विप् for the second —
    and naming the root has to beat naming the class.
    """

    def test_the_class_reaches_it(self):
        self.assertIn("gam", ANUDATTOPADESA)
        self.assertEqual(
            the_nasal("gam", gana="anudāttopadeśa", before="jhal",
                      result="kṅit").sutra, "6.4.37")

    def test_and_naming_it_reaches_it_elsewhere(self):
        self.assertEqual(the_nasal("gam", before="kvip").sutra,
                         "6.4.40")

    def test_and_a_varttika_widens_that_for_another_pada(self):
        """**गमादीनाम् इति वक्तव्यम्** — 6.3.116 leans on it for
        तन्, which is how परीतत् loses its nasal."""
        row, = provisions_for("6.4.40")
        self.assertIn("गमादीनाम्", row.why)
        self.assertIn("परीतत्", row.why)
        from src.astadhyayi.dirgha_samhita import (
            provisions_for as dirgha_for)

        other, = dirgha_for("6.3.116")
        self.assertIn("6.4.40", other.why)


class ThreeRootsTakeAcrossFourRules(unittest.TestCase):
    def test_jana_sana_khana_are_named_together(self):
        self.assertEqual(JANA_SANA_KHANA, ("jan", "san", "khan"))
        row, = provisions_for("6.4.42")
        self.assertEqual(row.of, JANA_SANA_KHANA)

    def test_the_first_is_compulsory_and_the_second_optional(self):
        firm = the_nasal("jan", before="san", result="kṅit")
        self.assertEqual(firm.sutra, "6.4.42")
        self.assertFalse(firm.optional)
        loose = the_nasal("jan", before="ya", result="kṅit")
        self.assertEqual(loose.sutra, "6.4.43")
        self.assertTrue(loose.optional)

    def test_and_one_of_the_three_has_no_option_before_shyan(self):
        """**जनेः श्यनि ज्ञाजनोर्जा इति नित्यं जादेशो भवति** —
        7.3.79 gives it outright there, so 6.4.43's option never
        arises."""
        # Written as a debt: 7.3.79 was not codified, so the
        # claim was its absence. It has landed with पाद ७.३, so
        # the claim is now the live one — the rule that makes
        # 6.4.43's option never arise can be asked directly.
        row, = provisions_for("6.4.43")
        self.assertIn("ज्ञाजनोर्जा", row.why)
        self.assertTrue(REGISTRY.has("7.3.79"))

    def test_the_last_of_the_four_gives_three_forms(self):
        """सातिः, सन्तिः, सतिः — the आ, the nasal kept, and the आ
        itself dropped."""
        row, = provisions_for("6.4.45")
        for form in ("सातिः", "सन्तिः", "सतिः"):
            self.assertIn(form, row.why, form)

    def test_and_it_says_its_option_again_on_purpose(self):
        """**अन्यतरस्यांग्रहणं विस्पष्टार्थम्** — 6.4.43's विभाषा
        was tied to its ये, and one might have thought it had
        lapsed."""
        row, = provisions_for("6.4.45")
        self.assertIn("विस्पष्टार्थम्", row.why)
        self.assertTrue(row.optional)


class WantsFiltersByWhatBecomesOfIt(unittest.TestCase):
    def test_asking_for_the_one_it_does(self):
        self.assertEqual(
            the_nasal("jan", before="san", result="kṅit",
                      wants="ā").sutra, "6.4.42")

    def test_asking_for_one_it_does_not(self):
        self.assertEqual(
            the_nasal("jan", before="san", result="kṅit",
                      wants="anunāsika-lopa").sutra, "")

    def test_a_refusal_supplies_nothing_to_ask_for(self):
        self.assertEqual(
            the_nasal(gana="anudāttopadeśa", before="ktic",
                      wants="anunāsika-lopa").sutra, "")


class Registration(unittest.TestCase):
    def test_every_sutra_of_the_run_is_registered(self):
        for row in NASAL_TABLE:
            self.assertTrue(REGISTRY.has(row.sutra), row.sutra)

    def test_the_notes_are_read_off_these_rows(self):
        collapse = re.compile(r"\s+")
        for row in NASAL_TABLE:
            note = collapse.sub(" ", REGISTRY.get(row.sutra).notes)
            head = collapse.sub(" ", row.why.split("\\n\\n")[0])
            self.assertIn(head[:70], note, row.sutra)


class WhatIsNotCodifiedYet(unittest.TestCase):
    """
    Written as the exact shortfall. 6.4.46 आर्धधातुके opens a
    heading of its own — **प्राग् एतस्माद् न ल्यपि इति**, to
    6.4.68 — and everything from there to 6.4.175 is ahead of it,
    6.4.77 excepted.
    """

    def test_the_heading_that_follows_has_landed(self):
        """
        6.4.46 आर्धधातुके opens a heading inside 6.4.1's. The debt
        is collected, and the claim is the join: it starts one
        sūtra past this run, and it is bounded by 6.4.69, which is
        codified too.
        """
        from src.astadhyayi.ardhadhatuka_lopa import (
            ARDHADHATUKA_RUN)

        self.assertTrue(REGISTRY.has("6.4.46"))
        self.assertEqual(_n("6.4.46")[2], _n(NASAL_RUN[1])[2] + 1)
        self.assertEqual(ARDHADHATUKA_RUN, ("6.4.46", "6.4.68"))

    def test_and_the_sutra_that_bounds_it_has_landed_too(self):
        """6.4.69 न ल्यपि both refuses and bounds, and both halves
        are recorded."""
        from src.astadhyayi.ardhadhatuka_lopa import (
            provisions_for as ardha_for)

        self.assertTrue(REGISTRY.has("6.4.69"))
        row, = ardha_for("6.4.69")
        self.assertTrue(row.refuses)
        self.assertEqual(row.blocks, ("6.4.66", "6.4.67"))

    def test_but_the_pada_is_unbroken_up_to_here(self):
        for n in range(1, 46):
            self.assertTrue(REGISTRY.has("6.4.%d" % n), n)


if __name__ == "__main__":
    unittest.main()
