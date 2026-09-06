# -*- coding: utf-8 -*-
"""
६.३.७३–९५ — नञ्, सह, समान before a second member.

Three particles, twenty-three rules, and the shape of the stretch
is the claim: each particle gets a block, the blocks do not
interleave, and each block has the same two halves — the rules
that change the particle, and the ones that hold it back.

The two arguments worth testing apart from that are 6.3.74's
तस्मात्, which fixes what the augment attaches to, and 6.3.83's
exceptions, which do NOT make the substitution compulsory but only
let an earlier option through.
"""

from __future__ import annotations

import re
import unittest

import src.astadhyayi.rules  # noqa: F401 — populates the registry
from src.astadhyayi.hrasva_mum import HRASVA_RUN
from src.astadhyayi.nan_saha_samana import (
    ASIS_EXCEPT, DRKSA_VARTIKA, DRS_THREE, NAN_RUN, NAN_TABLE,
    NA_PRAKRTYA, SAMANA_EXCEPT, SAMANA_TWELVE, provisions_for,
    shaped)
from src.astadhyayi.sutra import REGISTRY


def _n(sutra_id):
    return tuple(int(part) for part in sutra_id.split("."))


class TheRunFollowsTheOneBeforeIt(unittest.TestCase):
    def test_it_opens_one_sutra_after_the_augments_close(self):
        self.assertEqual(_n(NAN_RUN[0])[2], _n(HRASVA_RUN[1])[2] + 1)

    def test_one_row_for_each_sutra_from_73_to_95(self):
        got = sorted({row.sutra for row in NAN_TABLE}, key=_n)
        self.assertEqual(got, ["6.3.%d" % n for n in range(73, 96)])

    def test_every_row_carries_its_reason(self):
        for row in NAN_TABLE:
            self.assertGreater(len(row.why), 60, row.sutra)

    def test_nothing_answers_where_no_rule_is_reached(self):
        got = shaped("aśva", before="pati")
        self.assertEqual((got.becomes, got.sutra), ("", ""))
        self.assertIn("stands as it was", got.why)


class ThreeParticlesInThreeBlocks(unittest.TestCase):
    """
    नञ् 73–77, सह 78–83, समान 84–89, and then the अञ्चति rules,
    where सह comes back once more at the very end. What must not
    happen is a block reopening in the middle of another's.
    """

    def test_the_nan_rules_are_the_first_five(self):
        got = [row.sutra for row in NAN_TABLE
               if row.of == ("nañ",)]
        self.assertEqual(got, ["6.3.%d" % n for n in range(73, 78)])

    def test_the_saha_rules_run_six_together_and_one_at_the_end(
            self):
        got = [row.sutra for row in NAN_TABLE
               if row.of == ("saha",)]
        self.assertEqual(
            got, ["6.3.%d" % n for n in range(78, 84)] + ["6.3.95"])

    def test_the_samana_rules_run_six_together(self):
        got = [row.sutra for row in NAN_TABLE
               if row.of == ("samāna",)]
        self.assertEqual(got, ["6.3.%d" % n for n in range(84, 90)])

    def test_and_the_last_saha_rule_is_the_pada_stretch_s_last(self):
        """
        सहस्य सध्रिः closes the run, which is why सह is the only
        particle whose block is broken — it is picked up again
        eleven sūtras later, under a different heading-word.
        """
        self.assertEqual(NAN_TABLE[-1].sutra, NAN_RUN[1])
        self.assertEqual(NAN_TABLE[-1].of, ("saha",))


class WhatALossAndAnAugmentDoBetweenThem(unittest.TestCase):
    """
    6.3.73 drops the न् and 6.3.74 puts a नुट् back before a
    vowel, so अ- and अन्- are two states of one particle rather
    than two rules pulling opposite ways.
    """

    def test_the_loss_answers_with_nothing_following(self):
        got = shaped("nañ")
        self.assertEqual((got.sutra, got.becomes),
                         ("6.3.73", "na-lopa"))

    def test_and_the_augment_answers_before_a_vowel(self):
        got = shaped("nañ", before="ac")
        self.assertEqual((got.sutra, got.becomes),
                         ("6.3.74", "nuṭ"))

    def test_the_augment_says_what_it_attaches_to(self):
        """
        **तस्मादिति किम्? नञ एव हि स्यात्। पूर्वान्ते हि ङमो
        ह्रस्वादचि ङमुण्नित्यम् इति प्राप्नोति** — without तस्मात्
        the नुट् would attach to नञ् entire, and 8.3.32 would then
        double the ङम् at the end of the first part.
        """
        row, = provisions_for("6.3.74")
        self.assertIn("तस्मादिति किम्", row.why)
        self.assertIn("8.3.32", row.why)

    def test_and_the_rule_that_argument_turns_on_is_a_debt(self):
        """
        Written as the exact shortfall. 6.3.74's whole point is
        what 8.3.32 would otherwise do, and 8.3.32 is not
        codified — so the note cites a rule the engine cannot yet
        be asked. When it lands this becomes a live dependency.
        """
        # 8.3.32 ङमो ह्रस्वादचि ङमुण्नित्यम् has landed with
        # पाद ८.३, so the argument can be checked against the
        # rule it turns on.
        self.assertTrue(REGISTRY.has("8.3.32"))


class ElevenWordsKeepTheNAndEachIsAnalysed(unittest.TestCase):
    """
    6.3.75's list is not a list of exceptions to be memorised: the
    vṛtti derives every one — **भ्राजतेः क्विबन्तस्य नञ्समासः;
    पातिः शत्रन्तः; वेत्तिर् असुन्प्रत्ययान्तः** — which is what
    makes them words that KEEP their न् rather than opaque forms.
    """

    def test_there_are_eleven(self):
        self.assertEqual(len(NA_PRAKRTYA), 11)
        row, = provisions_for("6.3.75")
        self.assertEqual(row.before, NA_PRAKRTYA)

    def test_each_of_them_reaches_the_rule(self):
        for word in NA_PRAKRTYA:
            got = shaped("nañ", before=word)
            self.assertEqual((got.sutra, got.becomes),
                             ("6.3.75", "prakṛtyā"), word)

    def test_and_anything_else_loses_the_n(self):
        self.assertEqual(shaped("nañ", before="brāhmaṇa").sutra,
                         "6.3.73")

    def test_the_note_names_the_affix_that_built_them(self):
        row, = provisions_for("6.3.75")
        for cited in ("क्विबन्तस्य", "शत्रन्तः",
                      "असुन्प्रत्ययान्तः"):
            self.assertIn(cited, row.why, cited)


class ThreeRulesSayTheParticleStandsAsItIs(unittest.TestCase):
    def test_they_are_these(self):
        got = tuple(row.sutra for row in NAN_TABLE
                    if row.becomes == "prakṛtyā")
        self.assertEqual(got, ("6.3.75", "6.3.76", "6.3.77",
                               "6.3.83"))

    def test_and_each_holds_back_a_change_an_earlier_rule_made(
            self):
        """
        6.3.75–77 hold back 6.3.73's loss; 6.3.83 holds back the
        सह → स of 6.3.78–82. A प्रकृत्या with nothing to hold back
        would be saying nothing.
        """
        for code, earlier in (("6.3.75", "6.3.73"),
                              ("6.3.76", "6.3.73"),
                              ("6.3.77", "6.3.73"),
                              ("6.3.83", "6.3.78")):
            row, = provisions_for(code)
            before, = provisions_for(earlier)
            self.assertEqual(row.of, before.of, code)
            self.assertLess(_n(earlier), _n(code), code)
            self.assertNotEqual(before.becomes, "prakṛtyā", earlier)


class BeingExceptedFromAHoldBackIsNotBeingCompelled(
        unittest.TestCase):
    """
    6.3.83 holds सह back in a blessing, गो, वत्स and हल excepted.
    That does not make the substitution compulsory for those three
    — **वोपसर्जनस्य इति पक्षे भवत्येव सभावः** — it only lets
    6.3.82's option through, so सहगवे and सगवे both stand.
    """

    def test_the_hold_back_answers_in_a_blessing(self):
        got = shaped("saha", result="āśis")
        self.assertEqual((got.sutra, got.becomes),
                         ("6.3.83", "prakṛtyā"))

    def test_and_the_three_excepted_words_reach_it_not_at_all(self):
        for word in ASIS_EXCEPT:
            self.assertEqual(
                shaped("saha", result="āśis", before=word).sutra,
                "", word)

    def test_but_the_earlier_option_still_reaches_them(self):
        for word in ASIS_EXCEPT:
            got = shaped("saha", result="upasarjana", before=word)
            self.assertEqual(got.sutra, "6.3.82", word)
            self.assertTrue(got.optional, word)

    def test_and_the_note_says_exactly_that(self):
        row, = provisions_for("6.3.83")
        self.assertIn("पक्षे भवत्येव सभावः", row.why)


class ASubstituteMatchedOneToOne(unittest.TestCase):
    """
    6.3.90 इदंकिमोरीश्की — इदम् takes ईश् and किम् takes की, and
    crossing them is not Sanskrit. And both are pronouns, so
    6.3.91's सर्वनाम्नः reaches them too: only their being named
    outright puts 6.3.90 first.
    """

    def test_each_stem_gets_its_own_substitute(self):
        self.assertEqual(shaped("idam", before="dṛś").becomes, "īś")
        self.assertEqual(shaped("kim", before="dṛś").becomes, "kī")

    def test_both_come_from_the_same_sutra(self):
        for stem in ("idam", "kim"):
            self.assertEqual(shaped(stem, before="dṛś").sutra,
                             "6.3.90", stem)

    def test_the_wider_pronoun_rule_would_have_reached_them(self):
        wider, = provisions_for("6.3.91")
        self.assertEqual(wider.gana, "sarvanāman")
        self.assertEqual(wider.becomes, "ā")
        self.assertEqual(
            shaped("tad", gana="sarvanāman", before="dṛś").becomes,
            "ā")

    def test_and_naming_them_is_what_keeps_them_from_it(self):
        for stem in ("idam", "kim"):
            got = shaped(stem, gana="sarvanāman", before="dṛś")
            self.assertEqual(got.sutra, "6.3.90", stem)
            self.assertNotEqual(got.becomes, "ā", stem)


class AVarttikaAddsAFourthEnvironmentToThreeRulesAtOnce(
        unittest.TestCase):
    """
    **दृक्षे चेति वक्तव्यम्** is stated three times over, once
    under each of 6.3.89, 6.3.90 and 6.3.91 — सदृक्षः, ईदृक्षः,
    तादृक्षः — so all three rows have to carry it or one of the
    three forms is unaccounted for.
    """

    def test_the_sutras_name_three_and_the_varttika_a_fourth(self):
        self.assertEqual(len(DRS_THREE), 3)
        self.assertEqual(DRKSA_VARTIKA, ("dṛkṣa",))

    def test_all_three_rules_reach_the_fourth(self):
        for stem, code in (("samāna", "6.3.89"),
                           ("idam", "6.3.90")):
            self.assertEqual(shaped(stem, before="dṛkṣa").sutra,
                             code, stem)
        self.assertEqual(
            shaped("tad", gana="sarvanāman", before="dṛkṣa").sutra,
            "6.3.91")

    def test_and_each_note_cites_it(self):
        for code in ("6.3.89", "6.3.90", "6.3.91"):
            row, = provisions_for(code)
            self.assertIn("दृक्षे", row.why, code)


class TheAncatiRulesShareOneEnvironment(unittest.TestCase):
    """
    6.3.92–95 all want an अञ्चति with व on it, and each names a
    different first member. Four stems, four substitutes, one
    condition — so a query that omits the व must reach none of
    them.
    """

    def test_four_rules_and_four_substitutes(self):
        got = {row.sutra: row.becomes for row in NAN_TABLE
               if "añcati" in row.before}
        self.assertEqual(got, {"6.3.92": "adri", "6.3.93": "sami",
                               "6.3.94": "tiri", "6.3.95": "sadhri"})

    def test_each_is_reached_by_its_own_stem(self):
        for stem, code in (("viṣvak", "6.3.92"), ("sam", "6.3.93"),
                           ("tiras", "6.3.94"), ("saha", "6.3.95")):
            got = shaped(stem, before="añcati", result="va")
            self.assertEqual(got.sutra, code, stem)

    def test_and_without_the_va_none_of_them_is(self):
        for stem in ("viṣvak", "sam", "tiras"):
            self.assertEqual(
                shaped(stem, before="añcati").sutra, "", stem)

    def test_one_of_them_turns_on_a_deletion_not_happening(self):
        """**अलोप इति किम्? तिरश्चा, तिरश्चे** — 6.4.138 अचः takes
        the अ out there, and 6.3.94's condition is that it has
        not."""
        row, = provisions_for("6.3.94")
        self.assertIn("alopa", row.excludes)
        self.assertIn("6.4.138", row.why)
        self.assertEqual(
            shaped("tiras", before="añcati", result="alopa").sutra,
            "")


class TheListsAreTheVrttisOwn(unittest.TestCase):
    def test_the_twelve_before_which_samana_becomes_sa(self):
        self.assertEqual(len(SAMANA_TWELVE), 12)
        row, = provisions_for("6.3.85")
        self.assertEqual(row.before, SAMANA_TWELVE)
        for word in SAMANA_TWELVE:
            self.assertEqual(shaped("samāna", before=word).sutra,
                             "6.3.85", word)

    def test_one_of_them_supplies_a_term_the_grammar_leans_on(self):
        """सवर्ण is 1.1.9's term, and this is the rule that makes
        the word."""
        self.assertIn("varṇa", SAMANA_TWELVE)
        row, = provisions_for("6.3.85")
        self.assertIn("1.1.9", row.why)
        self.assertTrue(REGISTRY.has("1.1.9"))

    def test_the_three_the_vedic_rule_shuts_out(self):
        self.assertEqual(len(SAMANA_EXCEPT), 3)
        row, = provisions_for("6.3.84")
        self.assertEqual(row.excludes, SAMANA_EXCEPT)
        for word in SAMANA_EXCEPT:
            self.assertEqual(
                shaped("samāna", chandasi=True, before=word).sutra,
                "", word)


class WantsFiltersByTheShape(unittest.TestCase):
    def test_asking_for_the_one_it_gives(self):
        self.assertEqual(
            shaped("saha", result="saṃjñā", wants="sa").sutra,
            "6.3.78")

    def test_asking_for_one_it_does_not(self):
        self.assertEqual(
            shaped("saha", result="saṃjñā", wants="sadhri").sutra,
            "")

    def test_and_it_works_through_a_one_to_one_pairing(self):
        self.assertEqual(
            shaped("idam", before="dṛś", wants="īś").sutra,
            "6.3.90")
        self.assertEqual(
            shaped("idam", before="dṛś", wants="kī").sutra, "")


class Registration(unittest.TestCase):
    def test_every_sutra_of_the_run_is_registered(self):
        for row in NAN_TABLE:
            self.assertTrue(REGISTRY.has(row.sutra), row.sutra)

    def test_the_notes_are_read_off_these_rows(self):
        collapse = re.compile(r"\s+")
        for row in NAN_TABLE:
            note = collapse.sub(" ", REGISTRY.get(row.sutra).notes)
            head = collapse.sub(" ", row.why.split("\\n\\n")[0])
            self.assertIn(head[:70], note, row.sutra)


class WhatIsNotCodifiedYet(unittest.TestCase):
    """
    Written as the exact shortfall. 6.3.96 opens the last stretch
    of the pāda — forty-four sūtras of Vedic lengthening and
    substitution, ending at 6.3.139 where 6.3.1's उत्तरपदे runs
    out.
    """

    def test_the_run_that_follows_this_one_has_landed(self):
        """
        6.3.96 सध मादस्थयोश्छन्दसि opens the next stretch, and it
        gives सह a THIRD substitute — after स here and सध्रि at the
        very end of this run. The debt is collected, so the claim
        is now that the three shapes are three and are recorded
        apart.
        """
        from src.astadhyayi.purvapada_vikara import (
            altered, provisions_for as vikara_for)

        self.assertTrue(REGISTRY.has("6.3.96"))
        self.assertEqual(_n("6.3.96")[2], _n(NAN_RUN[1])[2] + 1)
        third, = vikara_for("6.3.96")
        here = {row.becomes for row in NAN_TABLE
                if row.of == ("saha",)} - {"prakṛtyā"}
        self.assertNotIn(third.becomes, here)
        self.assertEqual(
            altered("saha", before="māda", chandasi=True).becomes,
            "sadha")

    def test_and_the_end_of_the_pada_has_landed_too(self):
        """
        6.3.139 संप्रसारणस्य closes the pāda, and it closes it by
        settling a conflict with 6.3.61 — a rule of the stretch
        two before this one. The debt is collected, so the claim
        is now that the conflict is recorded on both sides.
        """
        from src.astadhyayi.dirgha_samhita import (
            provisions_for as dirgha_for)

        self.assertTrue(REGISTRY.has("6.3.139"))
        last, = dirgha_for("6.3.139")
        self.assertEqual(last.blocks, ("6.3.61",))

    def test_but_the_pada_is_unbroken_up_to_here(self):
        for n in range(1, 96):
            self.assertTrue(REGISTRY.has("6.3.%d" % n), n)

    def test_and_the_heading_that_governs_it_all_is_codified(self):
        from src.astadhyayi.aluk import UTTARAPADE_RUN

        self.assertTrue(REGISTRY.has(UTTARAPADE_RUN[0]))
        self.assertEqual(UTTARAPADE_RUN[1], "6.3.139")


if __name__ == "__main__":
    unittest.main()
