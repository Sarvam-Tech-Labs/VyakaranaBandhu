# -*- coding: utf-8 -*-
"""
६.३.३४–४५ — पुंवद्भाव, and the shortening that displaces it.

Two things make this run worth testing rather than tabulating.

**The operation is not a deletion.** **पुंशब्दस्येव रूपं भवति** —
the feminine takes the form the masculine WOULD have had. A
codification that recorded *the ending drops* would get
दर्शनीयभार्यः right and be wrong about what happened.

**And five rules refuse it and a sixth undoes all five.** 6.3.42's
whole content is that it beats 6.3.37–41, and its vṛtti proves it
by walking each one. So the set of stems it reaches has to be
exactly the set those five refuse — no more, and no fewer.
"""

from __future__ import annotations

import re
import unittest

import src.astadhyayi.rules  # noqa: F401 — populates the registry
from src.astadhyayi.anan_dvandva import ANAN_RUN
from src.astadhyayi.pumvadbhava import (
    GHADI, KARMADHARAYA_THREE, PRIYADI, PUMVAT_RUN, PUMVAT_TABLE,
    REFUSED_CLASSES, TASILADI, TASILADI_RUN, UNDONE_BY_6_3_42,
    behaves_as, provisions_for)
from src.astadhyayi.sutra import REGISTRY


def _n(sutra_id):
    return tuple(int(part) for part in sutra_id.split("."))


class TheRunFollowsTheOneBeforeIt(unittest.TestCase):
    def test_it_opens_one_sutra_after_the_dvandva_run_closes(self):
        self.assertEqual(_n(PUMVAT_RUN[0])[2],
                         _n(ANAN_RUN[1])[2] + 1)

    def test_one_row_for_each_sutra_from_34_to_45(self):
        got = [row.sutra for row in PUMVAT_TABLE]
        self.assertEqual(got, ["6.3.%d" % n for n in range(34, 46)])

    def test_every_row_carries_its_reason(self):
        for row in PUMVAT_TABLE:
            self.assertGreater(len(row.why), 60, row.sutra)

    def test_the_run_does_two_things_and_says_which(self):
        does = [row.does for row in PUMVAT_TABLE if not row.refuses]
        self.assertEqual(set(does), {"puṃvat", "hrasva"})
        # and it does them in that order, never going back
        self.assertEqual(does, sorted(does, key=lambda one: (
            one != "puṃvat", one)))


class NothingHappensByDefault(unittest.TestCase):
    def test_an_unreached_stem_stands_as_it_is(self):
        got = behaves_as("khaṭvā")
        self.assertEqual((got.does, got.sutra), ("", ""))
        self.assertIn("stands as it is", got.why)

    def test_the_base_class_alone_is_not_enough_either(self):
        """
        6.3.34 wants an appositional second member, 6.3.35 an
        affix, 6.3.36 one of two. The class by itself reaches
        none of them.
        """
        self.assertEqual(behaves_as("bhāṣitapuṃska-anūṅ").sutra, "")


class TheConditionIsOneCompoundUnpackedTwice(unittest.TestCase):
    """
    **भाषितः पुमान् येन समानायाम् आकृताव् एकस्मिन्
    प्रवृत्तिनिमित्ते स भाषितपुंस्कः शब्दः**, and **ऊङोऽभावोऽनूङ्**
    — two glosses before the term is used once. The codification
    keeps it as one term because the Kāśikā does: **बहुव्रीहिरयम्**.
    """

    def test_the_three_rules_that_grant_it_name_one_class(self):
        for code in ("6.3.34", "6.3.35", "6.3.36"):
            row, = provisions_for(code)
            self.assertEqual(row.stem, ("bhāṣitapuṃska-anūṅ",),
                             code)

    def test_and_the_note_glosses_both_halves(self):
        row, = provisions_for("6.3.34")
        self.assertIn("भाषितः पुमान्", row.why)
        self.assertIn("ऊङोऽभावोऽनूङ्", row.why)

    def test_what_it_does_is_stated_as_taking_a_shape(self):
        row, = provisions_for("6.3.34")
        self.assertIn("पुंशब्दस्येव रूपं भवति", row.why)
        self.assertEqual(row.does, "puṃvat")

    def test_the_appositional_case_is_reached(self):
        got = behaves_as("bhāṣitapuṃska-anūṅ",
                         result="samānādhikaraṇa")
        self.assertEqual((got.sutra, got.does), ("6.3.34", "puṃvat"))

    def test_and_the_priyadi_are_kept_out_of_it(self):
        row, = provisions_for("6.3.34")
        for word in PRIYADI:
            self.assertIn(word, row.excludes, word)
        self.assertEqual(
            behaves_as("bhāṣitapuṃska-anūṅ",
                       result="samānādhikaraṇa",
                       before="kalyāṇī").sutra, "")


class FiveRulesRefuseItAndASixthUndoesAllFive(unittest.TestCase):
    """
    The claim 6.3.42 makes is not about an environment but about
    five other rules, and the vṛtti walks them one at a time —
    **न कोपधायाः इत्युक्तम्, तत्रापि भवति** — so what the table has
    to show is that the five it undoes are the five that refuse.
    """

    def test_exactly_five_rules_refuse(self):
        refusing = tuple(row.sutra for row in PUMVAT_TABLE
                         if row.refuses)
        self.assertEqual(refusing, UNDONE_BY_6_3_42)

    def test_each_of_them_names_the_rule_it_takes_the_word_from(
            self):
        for code in UNDONE_BY_6_3_42:
            row, = provisions_for(code)
            self.assertEqual(row.blocks, ("6.3.34",), code)

    def test_and_6_3_42_names_all_five_back(self):
        row, = provisions_for("6.3.42")
        self.assertEqual(row.blocks, UNDONE_BY_6_3_42)

    def test_the_stems_it_reaches_are_exactly_the_ones_refused(self):
        """
        The strong form. If 6.3.42 reached a stem no rule had
        refused it would be granting something new, and if it
        missed one the vṛtti's walk would be incomplete.
        """
        refused = set()
        for code in UNDONE_BY_6_3_42:
            row, = provisions_for(code)
            refused.update(row.stem)
        row, = provisions_for("6.3.42")
        self.assertEqual(set(row.stem), refused)
        self.assertEqual(set(REFUSED_CLASSES), refused)

    def test_each_refused_stem_comes_back_in_each_environment(self):
        for stem in REFUSED_CLASSES:
            for before in KARMADHARAYA_THREE:
                got = behaves_as(stem, before=before)
                self.assertEqual((got.sutra, got.does),
                                 ("6.3.42", "puṃvat"),
                                 "%s / %s" % (stem, before))

    def test_but_outside_those_three_the_refusal_stands(self):
        for stem in REFUSED_CLASSES:
            got = behaves_as(stem)
            self.assertIn(got.sutra, UNDONE_BY_6_3_42, stem)
            self.assertEqual(got.does, "", stem)
            self.assertEqual(got.blocked_by, ("6.3.34",), stem)

    def test_and_the_base_class_is_not_among_what_it_gives_back(
            self):
        """
        **प्रतिषेधार्थोऽयमारम्भः** — the rule is for the refusals.
        For a stem nothing had refused, 6.3.35 is still the rule
        that answers before जातीयर्.
        """
        row, = provisions_for("6.3.42")
        self.assertNotIn("bhāṣitapuṃska-anūṅ", row.stem)
        self.assertEqual(
            behaves_as("bhāṣitapuṃska-anūṅ",
                       before="jātīyar").sutra, "6.3.35")

    def test_and_6_3_34_s_own_two_conditions_still_hold(self):
        """**भाषितपुंस्कादित्येव — खट्वावृन्दारिका। अनूङित्येव —
        ब्रह्मबन्धूवृन्दारिका** — undoing five refusals is not the
        same as widening the rule they refused."""
        row, = provisions_for("6.3.42")
        self.assertIn("भाषितपुंस्कादित्येव", row.why)
        self.assertEqual(
            behaves_as("khaṭvā", before="karmadhāraya").sutra, "")


class TwoRefusalsExceptTheSameWord(unittest.TestCase):
    """
    6.3.40 and 6.3.41 both say **अमानिनि**, so मानिन् escapes both
    — दीर्घकेशमानिनी and कठमानिनी keep the पुंवद्भाव that the rest
    of their class loses.
    """

    def test_both_except_it(self):
        for code in ("6.3.40", "6.3.41"):
            row, = provisions_for(code)
            self.assertIn("mānin", row.excludes, code)

    def test_and_before_manin_neither_refusal_is_reached(self):
        """
        Asked about a word by the class the REFUSAL names, and with
        मानिन् following, nothing in this run answers — which is
        exactly what excepting मानिन् means. The classes are not
        exclusive: दीर्घकेशी is a स्वाङ्ग-ईकारान्त feminine and a
        भाषितपुंस्कादनूङ् one at the same time, so the word is
        still reached, under the other description.
        """
        for stem in ("svāṅga-īkārānta", "jāti"):
            got = behaves_as(stem, before="mānin")
            self.assertNotIn(got.sutra, ("6.3.40", "6.3.41"), stem)
            self.assertEqual(got.sutra, "", stem)

    def test_and_the_rule_that_named_manin_still_supplies(self):
        row, = provisions_for("6.3.36")
        self.assertIn("mānin", row.before)
        self.assertIn("मानिनो ग्रहणम्", row.why)
        got = behaves_as("bhāṣitapuṃska-anūṅ", before="mānin")
        self.assertEqual((got.sutra, got.does), ("6.3.36", "puṃvat"))


class AnAffixListGivenAsARangeIsCountedOutByHand(unittest.TestCase):
    """
    6.3.35 names its affixes by a stretch of sūtras — **तसिल्
    इत्यतः प्रभृति... कृत्वसुच् इति प्राग् एतस्मात्** — and a
    vārttika then lists them, because a range does not say which of
    the affixes inside it are meant: **तसिलादिषु परिगणनं
    कर्तव्यम्**.
    """

    def test_the_range_is_recorded_as_two_sutra_numbers(self):
        self.assertEqual(TASILADI_RUN, ("5.3.7", "5.4.17"))
        for bound in TASILADI_RUN:
            self.assertTrue(REGISTRY.has(bound), bound)

    def test_and_the_list_is_recorded_apart_from_it(self):
        self.assertGreater(len(TASILADI), 12)
        row, = provisions_for("6.3.35")
        self.assertEqual(row.before, TASILADI)
        self.assertIn("परिगणनं कर्तव्यम्", row.why)

    def test_every_affix_of_the_list_reaches_the_rule(self):
        for affix in TASILADI:
            self.assertEqual(
                behaves_as("bhāṣitapuṃska-anūṅ",
                           before=affix).sutra, "6.3.35", affix)

    def test_two_of_them_are_named_again_at_6_3_42(self):
        """
        जातीयर् and देशीयर् are inside 6.3.35's stretch already, so
        6.3.42 does not add the environment — it adds the classes
        of stem that may stand in it. For the base class 6.3.35 is
        still the rule that answers.
        """
        for affix in ("jātīyar", "deśīyar"):
            self.assertIn(affix, TASILADI, affix)
            self.assertIn(affix, KARMADHARAYA_THREE, affix)
            self.assertEqual(
                behaves_as("bhāṣitapuṃska-anūṅ",
                           before=affix).sutra, "6.3.35", affix)
            self.assertEqual(
                behaves_as("kopadhā", before=affix).sutra,
                "6.3.42", affix)


class TheShorteningIsADifferentOperation(unittest.TestCase):
    """
    6.3.43–45 do not make the feminine look masculine; they make
    its final short. Where both could apply the vṛtti gives the
    shortening — **पुंवद्भावाद् ह्रस्वत्वं खिद्घादिकेषु भवति
    विप्रतिषेधेन** — and the eight things it happens before are of
    two kinds.
    """

    def test_the_three_that_shorten(self):
        got = tuple(row.sutra for row in PUMVAT_TABLE
                    if row.does == "hrasva")
        self.assertEqual(got, ("6.3.43", "6.3.44", "6.3.45"))

    def test_all_three_share_the_same_eight_environments(self):
        for code in ("6.3.43", "6.3.44", "6.3.45"):
            row, = provisions_for(code)
            self.assertEqual(row.before, GHADI, code)

    def test_the_eight_are_three_affixes_and_five_second_members(
            self):
        """**घरूपकल्पाः प्रत्ययाश्चेलडादीन्युत्तरपदानि**."""
        self.assertEqual(len(GHADI), 8)
        self.assertEqual(GHADI[:3], ("gha", "rūpa", "kalpa"))
        row, = provisions_for("6.3.43")
        self.assertIn("प्रत्ययाश्चेलडादीन्युत्तरपदानि", row.why)

    def test_the_first_is_compulsory_and_the_other_two_optional(
            self):
        self.assertFalse(
            behaves_as("ṅī-anta-anekāc", before="gha").optional)
        for stem in ("nadī-śeṣa", "ugit"):
            self.assertTrue(
                behaves_as(stem, before="gha").optional, stem)

    def test_the_remainder_is_what_the_first_rule_left_out(self):
        """
        **कश्च शेषः? अङी च या नदी, ङ्यन्तं च यदेकाच्** — exactly
        the two things 6.3.43's ङ्यः and अनेकाचः had between them
        excluded, which is why 6.3.44 is called the remainder.
        """
        first, = provisions_for("6.3.43")
        rest, = provisions_for("6.3.44")
        self.assertEqual(first.stem, ("ṅī-anta-anekāc",))
        self.assertEqual(rest.stem, ("nadī-śeṣa",))
        self.assertIn("कश्च शेषः", rest.why)

    def test_and_the_last_of_them_attests_three_forms_not_two(self):
        """
        **श्रेयसितरा, श्रेयसीतरा, श्रेयस्तरा** — the option gives
        two and the third is the masculine's shape, from elsewhere.
        """
        row, = provisions_for("6.3.45")
        self.assertTrue(row.optional)
        self.assertIn("श्रेयस्तरा", row.why)
        self.assertIn("पुंवद्भावोऽप्यत्र पक्षे वक्तव्यः", row.why)


class WantsFiltersByWhichOperation(unittest.TestCase):
    def test_asking_for_the_one_it_does(self):
        self.assertEqual(
            behaves_as("ṅī-anta-anekāc", before="gha",
                       wants="hrasva").sutra, "6.3.43")

    def test_asking_for_the_one_it_does_not(self):
        self.assertEqual(
            behaves_as("ṅī-anta-anekāc", before="gha",
                       wants="puṃvat").sutra, "")

    def test_a_refusal_supplies_nothing_to_ask_for(self):
        self.assertEqual(
            behaves_as("kopadhā", wants="puṃvat").sutra, "")


class Registration(unittest.TestCase):
    def test_every_sutra_of_the_run_is_registered(self):
        for row in PUMVAT_TABLE:
            self.assertTrue(REGISTRY.has(row.sutra), row.sutra)

    def test_the_notes_are_read_off_these_rows(self):
        collapse = re.compile(r"\s+")
        for row in PUMVAT_TABLE:
            note = collapse.sub(" ", REGISTRY.get(row.sutra).notes)
            head = collapse.sub(" ", row.why.split("\\n\\n")[0])
            self.assertIn(head[:70], note, row.sutra)


class WhatIsNotCodifiedYet(unittest.TestCase):
    """
    Written as the exact shortfall. 6.3.46 आन्महतः opens the run of
    substitutions before a second member — महत् → महा, हृदय → हृद्,
    पाद → पद्, उदक → उद — and none of it is codified.
    """

    def test_the_run_that_follows_this_one_has_landed(self):
        """
        6.3.46 आन्महतः opens the run of substitutions. The debt is
        collected, and the claim is the join: it starts one sūtra
        past this run, and it replaces a stem where this run only
        reshapes or shortens one — so neither answers for the
        other.
        """
        from src.astadhyayi.purvapada_adesa import replaced_by

        self.assertTrue(REGISTRY.has("6.3.46"))
        self.assertEqual(_n("6.3.46")[2], _n(PUMVAT_RUN[1])[2] + 1)
        self.assertEqual(
            replaced_by("mahat", before="jātīya").becomes, "mahā")
        self.assertEqual(behaves_as("mahat").sutra, "")

    def test_but_the_pada_is_unbroken_up_to_here(self):
        for n in range(1, 46):
            self.assertTrue(REGISTRY.has("6.3.%d" % n), n)


if __name__ == "__main__":
    unittest.main()
