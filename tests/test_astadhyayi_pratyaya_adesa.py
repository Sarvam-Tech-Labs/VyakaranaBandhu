# -*- coding: utf-8 -*-
"""
७.१.१–८ — what an affix is replaced by, in itself.

अध्याय ७ opens on the affix, and the tests follow the Kāśikā's own
worked forms. The three झ rules are where the competition is:
7.1.3 turns every झ into अन्त्, and two rules take it back.
"""

from __future__ import annotations

import unittest

from src.astadhyayi.pratyaya_adesa import (
    ABHYASTA_FOUR,
    ADI_FIVE,
    AFFIX_TABLE,
    CODIFIED_APART,
    NOT_NASAL,
    PRATYAYA_RUN,
    WHERE_THEY_COME_FROM,
    YU_VU,
    becomes,
    provisions_for,
)
from src.astadhyayi.sources import REGISTRY
import src.astadhyayi.rules  # noqa: F401  (populates REGISTRY)


class TheTwoPairings(unittest.TestCase):
    """7.1.1 and 7.1.2, both यथासंख्यम्."""

    def test_yu_becomes_ana_and_vu_becomes_aka(self):
        # नन्दनः from ल्यु, कारकः from ण्वुल्.
        self.assertEqual(YU_VU, (("yu", "ana"), ("vu", "aka")))
        for named, shape in YU_VU:
            got = becomes(named)
            self.assertEqual(got.sutra, "7.1.1", named)
            self.assertEqual(got.does, shape, named)

    def test_a_crossed_pairing_reaches_nothing(self):
        # यु gives अन and not अक; asking for the wrong substitute
        # must not fall back on the same rule.
        self.assertEqual(becomes("yu", wants="aka").sutra, "")

    def test_five_affix_initials_take_five_substitutes(self):
        # नाडायनः, सौपर्णेयः, आढ्यकुलीनः, गार्गीयः, क्षत्रियः.
        self.assertEqual(len(ADI_FIVE), 5)
        for named, shape in ADI_FIVE:
            got = becomes(named)
            self.assertEqual(got.sutra, "7.1.2", named)
            self.assertEqual(got.does, shape, named)

    def test_it_is_the_head_of_the_affix_and_not_the_affix(self):
        # ऊरुदघ्नम् has the घ inside the affix and keeps it.
        self.assertTrue(provisions_for("7.1.2")[0].at_head)

    def test_the_taddhitas_it_works_on_are_codified(self):
        # फक् 4.1.99, ढक् 4.1.120, ख 4.1.139, छ 4.2.114,
        # घ 4.1.138 — the rule is stated about affixes another
        # adhyāya supplies, and all five are live.
        self.assertEqual(len(WHERE_THEY_COME_FROM), 5)
        for named, code in WHERE_THEY_COME_FROM:
            self.assertTrue(REGISTRY.has(code), (named, code))


class TheNasalityIsDeclared(unittest.TestCase):
    """7.1.1's condition is one no writing shows."""

    def test_the_yu_that_is_not_nasal_keeps_its_shape(self):
        # ऊर्णायुः from 5.2.123's युस्, भुज्युः and मृत्युः from
        # the Uṇādi — none of them is this rule's यु.
        self.assertEqual(len(NOT_NASAL), 3)
        for word in NOT_NASAL:
            self.assertEqual(becomes(word).sutra, "", word)

    def test_the_note_says_where_the_condition_comes_from(self):
        # प्रतिज्ञानुनासिक्याः पाणिनीयाः — declared, not marked.
        why = provisions_for("7.1.1")[0].why
        self.assertIn("प्रतिज्ञानुनासिक्याः", why)


class TheJhaRules(unittest.TestCase):
    """7.1.4–7 against 7.1.3, which is codified elsewhere."""

    def test_the_general_rule_is_codified_apart(self):
        # 7.1.3 झोऽन्तः lives in anga.jho_antah, because it had to
        # be settled against 1.3.7 चुटू before पचन्ति could be
        # derived at all. It is registered, and not in this table.
        self.assertEqual(CODIFIED_APART, ("7.1.3",))
        self.assertTrue(REGISTRY.has("7.1.3"))
        self.assertNotIn("7.1.3", [row.sutra for row in AFFIX_TABLE])

    def test_a_reduplicated_stem_gives_at_and_not_ant(self):
        # ददति, दधति, जक्षति, जाग्रति.
        got = becomes("jha", after="abhyasta")
        self.assertEqual(got.sutra, "7.1.4")
        self.assertEqual(got.does, "at")
        self.assertIn("7.1.3", got.blocked_by)

    def test_the_four_stems_are_all_reduplicated(self):
        self.assertEqual(ABHYASTA_FOUR,
                         ("dā", "dhā", "jakṣ", "jāgṛ"))

    def test_the_atmanepada_gives_at_after_a_non_a_stem(self):
        # चिन्वते, पुनते, लुनते.
        got = becomes("jha", after="an-a-anta", pada="ātmanepada")
        self.assertEqual(got.sutra, "7.1.5")
        self.assertEqual(got.does, "at")

    def test_both_halves_of_that_condition_bite(self):
        # चिन्वन्ति is परस्मैपद, च्यवन्ते ends in अ. Neither
        # reaches 7.1.5, and 7.1.3 supplies अन्त् for both.
        self.assertNotEqual(
            becomes("jha", after="an-a-anta").sutra, "7.1.5")
        self.assertNotEqual(
            becomes("jha", pada="ātmanepada").sutra, "7.1.5")


class TheRutAugment(unittest.TestCase):
    """7.1.6–8, and what the augment is attached to."""

    def test_sin_takes_the_rut(self):
        # शेरते, शेरताम्, अशेरत.
        got = becomes("jha-ādeśa", root="śīṅ")
        self.assertEqual(got.sutra, "7.1.6")
        self.assertEqual(got.does, "ruṭ")

    def test_it_is_an_augment_and_not_a_substitute(self):
        # The distinction is the sūtra's own point: attached to
        # the झ itself it would have blocked 7.1.5's अत्, and
        # शेरते needs both.
        self.assertTrue(becomes("jha-ādeśa", root="śīṅ").augment)
        self.assertFalse(becomes("jha", after="abhyasta").augment)

    def test_vid_takes_it_optionally(self):
        # संविदते beside संविद्रते.
        got = becomes("jha-ādeśa", root="vid")
        self.assertEqual(got.sutra, "7.1.7")
        self.assertTrue(got.optional)

    def test_sin_is_not_optional(self):
        self.assertFalse(becomes("jha-ādeśa", root="śīṅ").optional)

    def test_the_veda_takes_it_bahulam(self):
        # देवा अदुह्र.
        got = becomes("jha-ādeśa", chandasi=True)
        self.assertEqual(got.sutra, "7.1.8")
        self.assertTrue(provisions_for("7.1.8")[0].bahulam)

    def test_and_not_outside_the_veda(self):
        # A झ-substitute after no named root reaches nothing.
        self.assertEqual(becomes("jha-ādeśa").sutra, "")


class NothingHappensByDefault(unittest.TestCase):
    """Most affixes go into the word as they were taught."""

    def test_an_unnamed_affix_reaches_nothing(self):
        got = becomes("ghañ")
        self.assertEqual(got.sutra, "")
        self.assertEqual(got.does, "")

    def test_and_the_answer_says_so_in_words(self):
        self.assertIn("keeps the shape", becomes("ghañ").why)


class Registration(unittest.TestCase):
    """Every row reaches the registry with real notes."""

    def test_the_run_is_the_pada_s_opening(self):
        self.assertEqual(PRATYAYA_RUN, ("7.1.1", "7.1.8"))

    def test_the_table_is_the_run_less_what_is_codified_apart(self):
        codes = [row.sutra for row in AFFIX_TABLE]
        self.assertEqual(
            codes,
            [code for code in ("7.1.%d" % n for n in range(1, 9))
             if code not in CODIFIED_APART])

    def test_every_sutra_is_registered_with_real_notes(self):
        for row in AFFIX_TABLE:
            self.assertTrue(REGISTRY.has(row.sutra), row.sutra)
            notes = REGISTRY.get(row.sutra).notes
            self.assertGreater(len(notes), 100, row.sutra)
            self.assertIn("SETTLED", notes, row.sutra)

    def test_the_rule_codified_apart_still_has_its_own_notes(self):
        # It was registered long before this pāda was read, and a
        # patch that appends to this file must not disturb it.
        notes = REGISTRY.get("7.1.3").notes
        self.assertGreater(len(notes), 200)
        self.assertIn("अन्त इत्ययम् आदेशो", notes)


class WhatIsNotCodifiedYet(unittest.TestCase):
    """
    The debts, written as the exact shortfall.

    Each fails the moment the thing it names lands, and must then
    be rewritten to state the live dependency instead.
    """

    def test_the_krt_affixes_this_run_reshapes_are_live(self):
        # 3.1.133's ण्वुल् gives कारकः and 3.1.134's ल्यु gives
        # नन्दनः. Both are codified, so the यु and वु this run
        # replaces are affixes the engine can already supply.
        self.assertTrue(REGISTRY.has("3.1.133"))
        self.assertTrue(REGISTRY.has("3.1.134"))

    def test_the_lakara_endings_the_jha_rules_act_on_are_live(self):
        # 3.4.78 तिप्तस्झि० supplies the झि these rules reshape,
        # and 3.4.109 सिजभ्यस्तविदिभ्यश्च the जुस् the vṛtti says
        # displaces 7.1.4. Both are codified, so the whole chain
        # from ending to substitute is in the engine.
        self.assertTrue(REGISTRY.has("3.4.78"))
        self.assertTrue(REGISTRY.has("3.4.109"))

    def test_what_the_run_hands_on_to_is_not_codified_yet(self):
        # 7.1.5's चिन्वते needs 7.1.58's नुम् nowhere, but 7.1.8's
        # अदुह्र needs 7.1.41's त्-loss and 7.4.16's guṇa, and
        # neither is read yet. When either lands this assertion
        # fails and the note must state the live dependency.
        # 7.1.41 landed with the rest of the pāda while this
        # was being written, so it is a live edge now; 7.4.16 is
        # still ahead, and when it lands this fails.
        self.assertTrue(REGISTRY.has("7.1.41"))
        # 7.4.16 ऋदृशोऽङि गुणः has landed with पाद ७.४, so
        # अदुह्र can be asked against both the त्-loss and the
        # guṇa it needs.
        self.assertTrue(REGISTRY.has("7.4.16"))


if __name__ == "__main__":
    unittest.main()
