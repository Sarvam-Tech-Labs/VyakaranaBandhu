# -*- coding: utf-8 -*-
"""
६.४.२३–३३ — the न् dropped from a stem.

Eleven rules and one sound, so the interest is entirely in how the
run is fenced. Three things:

**A letter in the sūtra that is not part of the affix's sound.**
6.4.23's श् is there to keep two words out that 7.3.102 would
otherwise have made look identical.

**A rule split off for the sake of the rule after it.**
**पृथग्योगकरणमुत्तरार्थम्** — 6.4.26 exists so that रञ्ज् alone
carries into 6.4.27.

**And a refusal that refuses nothing.** 6.4.33 reads as the fourth
of four प्रतिषेधs and is the opposite: **अप्राप्तोऽयं नलोपः पक्षे
विधीयते। ततो नेति नानुवर्तते**.
"""

from __future__ import annotations

import re
import unittest

import src.astadhyayi.rules  # noqa: F401 — populates the registry
from src.astadhyayi.anga_dirgha import DIRGHA_RUN
from src.astadhyayi.nalopa import (
    ASIDDHAVAT, LANGI_KAMPI, NALOPA_RUN, NALOPA_TABLE,
    NIPATANA_FIVE, RANJ, SAPI_ROOTS, n_goes, provisions_for)
from src.astadhyayi.sutra import REGISTRY


def _n(sutra_id):
    return tuple(int(part) for part in sutra_id.split("."))


class TheRunStandsUnderTwoHeadings(unittest.TestCase):
    """
    6.4.1 अङ्गस्य is still running, and 6.4.22 असिद्धवत् stands
    immediately before this run, so everything here is also
    treated as not having happened for what shares its locus.
    """

    def test_it_opens_two_sutras_after_the_lengthening_run(self):
        self.assertEqual(_n(NALOPA_RUN[0])[2],
                         _n(DIRGHA_RUN[1])[2] + 2)

    def test_and_the_sutra_between_them_is_the_asiddhatva(self):
        self.assertEqual(ASIDDHAVAT, "6.4.22")
        self.assertEqual(_n(ASIDDHAVAT)[2], _n(NALOPA_RUN[0])[2] - 1)
        self.assertTrue(REGISTRY.has(ASIDDHAVAT))

    def test_one_row_for_each_sutra_from_23_to_33(self):
        got = [row.sutra for row in NALOPA_TABLE]
        self.assertEqual(got, ["6.4.%d" % n for n in range(23, 34)])

    def test_every_row_carries_its_reason(self):
        for row in NALOPA_TABLE:
            self.assertGreater(len(row.why), 60, row.sutra)

    def test_nothing_answers_where_no_rule_is_reached(self):
        got = n_goes("nand", before="kṅit")
        self.assertEqual((got.does, got.sutra), ("", ""))
        self.assertIn("stays where it is", got.why)


class ALetterInTheSutraThatIsNotThereForItsSound(unittest.TestCase):
    """
    **शकारवतो ग्रहणं किम्? यज्ञानाम्, यत्नानाम्** — 7.3.102's
    lengthening plus स्थानिवद्भाव would have made those look like
    the same shape, and the न् would have gone from them too.
    """

    def test_the_note_says_which_shna_is_meant(self):
        row, = provisions_for("6.4.23")
        self.assertIn("श्नमयम्", row.why)
        self.assertIn("उत्सृष्ट", row.why)

    def test_and_what_the_sh_keeps_out(self):
        row, = provisions_for("6.4.23")
        for word in ("यज्ञानाम्", "यत्नानाम्"):
            self.assertIn(word, row.keeps_out, word)
        self.assertIn("स्थानिवद्भावाद्", row.why)

    def test_the_rule_it_turns_on_is_a_debt(self):
        """7.3.102 सुपि च is what would have made the two shapes
        alike, and it is not codified."""
        # Written as a debt: 7.3.102 सुपि च was not codified.
        # It has landed with पाद ७.३, so the lengthening this
        # note turns on can be asked of the engine directly.
        self.assertTrue(REGISTRY.has("7.3.102"))


class ARuleSplitOffForTheSakeOfTheNextOne(unittest.TestCase):
    """
    6.4.25 names three roots and 6.4.26 names a fourth, and they
    do the same thing before the same affix. The split is not
    tidiness: **पृथग्योगकरणमुत्तरार्थम्** — 6.4.27 carries रञ्ज्
    down and could not have carried four.
    """

    def test_the_two_rules_do_the_same_thing(self):
        first, = provisions_for("6.4.25")
        second, = provisions_for("6.4.26")
        self.assertEqual(first.does, second.does)
        self.assertEqual(first.before, second.before)

    def test_and_the_second_says_why_it_stands_alone(self):
        second, = provisions_for("6.4.26")
        self.assertIn("पृथग्योगकरणम्", second.why)
        self.assertIn("उत्तरार्थम्", second.why)

    def test_and_only_its_root_carries_into_the_third(self):
        third, = provisions_for("6.4.27")
        self.assertEqual(third.of, RANJ)
        for root in SAPI_ROOTS:
            self.assertNotIn(root, third.of, root)

    def test_all_four_drop_it_before_shap(self):
        for root in SAPI_ROOTS + RANJ:
            got = n_goes(root, before="śap")
            self.assertEqual(got.does, "na-lopa", root)

    def test_but_only_one_of_them_before_ghan(self):
        self.assertEqual(
            n_goes("rañj", before="ghañ", result="bhāva").sutra,
            "6.4.27")
        for root in SAPI_ROOTS:
            self.assertEqual(
                n_goes(root, before="ghañ", result="bhāva").sutra,
                "", root)


class ARefusalThatRefusesNothing(unittest.TestCase):
    """
    Three real प्रतिषेधs and then one that only looks like a
    fourth: **अप्राप्तोऽयं नलोपः पक्षे विधीयते। ततो नेति
    नानुवर्तते** — the loss was never available before चिण्, so
    6.4.33 GRANTS it optionally, and the न of 6.4.30 does not
    carry down.
    """

    def test_three_rules_refuse(self):
        refusing = tuple(row.sutra for row in NALOPA_TABLE
                         if row.refuses)
        self.assertEqual(refusing, ("6.4.30", "6.4.31", "6.4.32"))

    def test_and_each_names_the_rule_it_takes_the_word_from(self):
        for code in ("6.4.30", "6.4.31", "6.4.32"):
            row, = provisions_for(code)
            self.assertEqual(row.blocks, ("6.4.24",), code)

    def test_the_fourth_supplies_rather_than_refuses(self):
        row, = provisions_for("6.4.33")
        self.assertFalse(row.refuses)
        self.assertTrue(row.optional)
        self.assertEqual(row.blocks, ())

    def test_and_its_note_says_the_na_does_not_carry_down(self):
        row, = provisions_for("6.4.33")
        self.assertIn("अप्राप्तोऽयं नलोपः", row.why)
        self.assertIn("नानुवर्तते", row.why)

    def test_so_it_answers_with_the_loss_and_not_without(self):
        got = n_goes("bhañj", before="ciṇ")
        self.assertEqual((got.sutra, got.does),
                         ("6.4.33", "na-lopa"))
        self.assertTrue(got.optional)


class TheWideRuleAndWhatIsCarvedOutOfIt(unittest.TestCase):
    """
    6.4.24 reaches every consonant-final stem with no इ marker,
    which is most of what the run is about. The three refusals each
    name stems to carve a piece out of it.
    """

    def test_the_wide_rule_names_a_class_and_not_a_stem(self):
        row, = provisions_for("6.4.24")
        self.assertEqual(row.of, ())
        self.assertEqual(row.gana, "anidit-hal-anta")

    def test_it_answers_for_the_class(self):
        got = n_goes(gana="anidit-hal-anta", before="kṅit")
        self.assertEqual((got.sutra, got.does),
                         ("6.4.24", "na-lopa"))

    def test_and_a_named_stem_beats_the_class(self):
        for stem, code in (("añc", "6.4.30"), ("skand", "6.4.31"),
                           ("naś", "6.4.32")):
            got = n_goes(stem, gana="anidit-hal-anta",
                         before="ktvā" if code != "6.4.30" else "",
                         result="pūjā" if code == "6.4.30" else "")
            self.assertEqual(got.sutra, code, stem)
            self.assertEqual(got.does, "", stem)

    def test_a_varttika_adds_two_roots_each_in_one_sense(self):
        """**अनिदितां नलोपे लङ्गिकम्प्योर् उपतापशरीरविकारयोर्
        उपसंख्यानम्** — matched one to one."""
        self.assertEqual(len(LANGI_KAMPI), 2)
        self.assertEqual(dict(LANGI_KAMPI)["laṅg"], "upatāpa")
        row, = provisions_for("6.4.24")
        self.assertIn("लङ्गिकम्प्योर्", row.why)


class OneRefusalIsNotNeededOnOneReading(unittest.TestCase):
    """
    6.4.31 refuses the loss for स्कन्द् and स्यन्द् before क्त्वा.
    For स्यन्द् on the इट् reading it was never due: **न क्त्वा
    सेट् इति कित्त्वप्रतिषेधाद् एव नलोपाभावः** — 1.2.18 takes the
    कित् away and 6.4.24's own condition fails.
    """

    def test_the_note_says_so(self):
        row, = provisions_for("6.4.31")
        self.assertIn("न क्त्वा सेट्", row.why)
        self.assertIn("कित्त्वप्रतिषेधाद्", row.why)

    def test_and_the_rule_it_leans_on_is_codified(self):
        self.assertTrue(REGISTRY.has("1.2.18"))

    def test_the_refusal_still_answers_for_both_stems(self):
        for stem in ("skand", "syand"):
            got = n_goes(stem, before="ktvā")
            self.assertEqual(got.sutra, "6.4.31", stem)


class WhatIsLaidDownWholeIsMarkedAsSuch(unittest.TestCase):
    """
    6.4.28 and 6.4.29 are निपातन, and two of the forms are laid
    down for TWO things apiece — the न् gone and a guṇa made that
    1.1.4 would have refused.
    """

    def test_those_two_are_the_only_ones(self):
        got = {row.sutra for row in NALOPA_TABLE if row.nipatana}
        self.assertEqual(got, {"6.4.28", "6.4.29"})

    def test_one_of_them_lays_down_two_things_at_once(self):
        row, = provisions_for("6.4.28")
        self.assertIn("नलोपो वृद्ध्यभावश्च", row.why)

    def test_and_the_other_lays_down_five_forms(self):
        self.assertEqual(len(NIPATANA_FIVE), 5)
        row, = provisions_for("6.4.29")
        self.assertEqual(row.of, NIPATANA_FIVE)
        for word in NIPATANA_FIVE:
            got = n_goes(word)
            self.assertEqual(got.sutra, "6.4.29", word)
            self.assertTrue(got.nipatana, word)

    def test_and_the_rule_they_step_around_is_the_same_one(self):
        """1.1.4 न धातुलोप आर्धधातुके — 6.4.28 says it does not
        reach there, 6.4.29 says it would have and the निपातन is
        what gets past it."""
        first, = provisions_for("6.4.28")
        second, = provisions_for("6.4.29")
        self.assertIn("1.1.4", first.why)
        self.assertIn("न धातुलोप आर्धधातुके", second.why)
        self.assertTrue(REGISTRY.has("1.1.4"))


class WantsFiltersByTheOperation(unittest.TestCase):
    def test_asking_for_the_one_it_does(self):
        self.assertEqual(
            n_goes(before="śna", wants="na-lopa").sutra, "6.4.23")

    def test_asking_for_one_it_does_not(self):
        self.assertEqual(
            n_goes(before="śna", wants="nipātana").sutra, "")


class Registration(unittest.TestCase):
    def test_every_sutra_of_the_run_is_registered(self):
        for row in NALOPA_TABLE:
            self.assertTrue(REGISTRY.has(row.sutra), row.sutra)

    def test_the_notes_are_read_off_these_rows(self):
        collapse = re.compile(r"\s+")
        for row in NALOPA_TABLE:
            note = collapse.sub(" ", REGISTRY.get(row.sutra).notes)
            head = collapse.sub(" ", row.why.split("\\n\\n")[0])
            self.assertIn(head[:70], note, row.sutra)

    def test_and_the_two_rules_codified_before_the_run_survive(self):
        """
        6.4.22 and 6.4.77 were codified long before this pāda was
        read through, and both are registered from other modules
        in the same file. A patch that appends to that file must
        not disturb them.
        """
        for code in ("6.4.22", "6.4.77"):
            self.assertTrue(REGISTRY.has(code), code)
            self.assertGreater(len(REGISTRY.get(code).notes), 200,
                               code)


class WhatIsNotCodifiedYet(unittest.TestCase):
    """
    Written as the exact shortfall. 6.4.34 शास इदङ्हलोः opens the
    next stretch, and 6.4.35 to 6.4.175 is ahead of it, 6.4.77
    excepted.
    """

    def test_the_run_that_follows_this_one_has_landed(self):
        """
        6.4.34 शास इदङ्हलोः opens the next stretch. The debt
        is collected, and the claim is the join: it starts one
        sūtra past this run and it does something else to the
        nasal — this run drops it, that one replaces it or turns
        it to आ.
        """
        from src.astadhyayi.anunasika_lopa import the_nasal

        self.assertTrue(REGISTRY.has("6.4.34"))
        self.assertEqual(_n("6.4.34")[2], _n(NALOPA_RUN[1])[2] + 1)
        self.assertEqual(the_nasal("śās", before="hi").does, "śā")
        self.assertEqual(n_goes("śās", before="hi").sutra, "")

    def test_but_the_pada_is_unbroken_up_to_here(self):
        for n in range(1, 34):
            self.assertTrue(REGISTRY.has("6.4.%d" % n), n)


if __name__ == "__main__":
    unittest.main()
