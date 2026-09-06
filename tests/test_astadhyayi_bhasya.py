# -*- coding: utf-8 -*-
"""
६.४.१२९–१५३ — भस्य, what the weak stem loses.

The tests are written against the Kāśikā's own worked forms. Where a
rule and its exception compete, the test asks which one wins and on
what query, not merely that both exist.
"""

from __future__ import annotations

import unittest

from src.astadhyayi.bhasya import (
    BHASYA_RUN,
    BHA_TABLE,
    GRETIL_CORRUPT,
    LOSS_RUN,
    SURYADI,
    SVA_YUVA_MAGHAVAN,
    in_the_weak_stem,
    provisions_for,
)
from src.astadhyayi.sources import REGISTRY
import src.astadhyayi.rules  # noqa: F401  (populates REGISTRY)


class TheHeading(unittest.TestCase):
    """6.4.129 भस्य and how far it reaches."""

    def test_the_heading_runs_to_the_end_of_the_adhyaya(self):
        # भस्येत्ययमधिकारः आ अध्यायपरिसमाप्तेः — 6.4.175 is the last
        # sūtra of अध्याय ६, and the heading covers everything to it.
        self.assertEqual(BHASYA_RUN, ("6.4.129", "6.4.175"))

    def test_this_module_stops_short_of_the_heading(self):
        # The losses are 129-153; 154-175 is the इष्ठ run and the
        # प्रकृतिभाव, codified apart.
        self.assertEqual(LOSS_RUN, ("6.4.129", "6.4.153"))
        self.assertLess(LOSS_RUN[1], BHASYA_RUN[1])
        self.assertEqual(BHA_TABLE[-1].sutra, "6.4.153")

    def test_the_heading_names_no_loss_of_its_own(self):
        heading = provisions_for("6.4.129")[0]
        self.assertTrue(heading.heading)
        self.assertEqual(heading.does, "")


class WhatTheStemLoses(unittest.TestCase):
    """The main losses, each on the Kāśikā's own example."""

    def test_pad_shortens_to_pad(self):
        # द्विपदः पश्य — पाद् becomes पद् when the stem is भ.
        got = in_the_weak_stem(stem="pāda")
        self.assertEqual(got.sutra, "6.4.130")

    def test_vas_vocalises(self):
        # विदुषः, पेचुषः — the वस् of विद्वस् becomes उष्.
        got = in_the_weak_stem(gana="vasu-anta")
        self.assertEqual(got.sutra, "6.4.131")

    def test_vah_takes_uth_and_not_a_plain_u(self):
        # प्रष्ठौहः — the औ is 6.1.89's, and it needs ऊठ् by name.
        got = in_the_weak_stem(gana="vāha-anta")
        self.assertEqual(got.sutra, "6.4.132")
        self.assertIn("ūṭh", got.does)

    def test_an_final_stem_loses_its_a(self):
        # राज्ञः, तक्ष्णः — with 6.4.8's lengthening for the strong
        # cases, this is most of how an न्-final noun declines.
        got = in_the_weak_stem(gana="an-anta")
        self.assertEqual(got.sutra, "6.4.134")

    def test_ac_final_stem_loses_its_a(self):
        # दधीचः — and the अच् meant is अञ्चति with its न् gone.
        got = in_the_weak_stem(gana="ac-anta")
        self.assertEqual(got.sutra, "6.4.138")

    def test_a_final_root_loses_its_a(self):
        # कीलालपः — a ROOT, which is why खट्वाः keeps its आ.
        got = in_the_weak_stem(gana="ā-anta-dhātu")
        self.assertEqual(got.sutra, "6.4.140")


class SvaYuvaMaghavan(unittest.TestCase):
    """6.4.133, and the taddhita that switches it off."""

    def test_the_three_vocalise_before_a_non_taddhita(self):
        # शुनः, यूनः, मघोनः.
        for stem in SVA_YUVA_MAGHAVAN:
            got = in_the_weak_stem(stem=stem, before="not-taddhita")
            self.assertEqual(got.sutra, "6.4.133", stem)

    def test_the_list_is_exactly_the_three(self):
        self.assertEqual(SVA_YUVA_MAGHAVAN,
                         ("śvan", "yuvan", "maghavan"))

    def test_maghavan_was_already_made_maghavat_five_sutras_back(self):
        # 6.4.128 मघवा बहुलम् — so मघवन् reaches this rule only in
        # the shape the earlier sūtra did not take.
        self.assertTrue(REGISTRY.has("6.4.128"))
        self.assertIn("मघव", REGISTRY.get("6.4.128").notes)


class TheThreeWayCompetition(unittest.TestCase):
    """6.4.134 against 6.4.136 and 6.4.137."""

    def test_the_loss_is_optional_before_ngi_and_si(self):
        # राज्ञि beside राजनि — what 6.4.134 made compulsory is an
        # option before these two endings.
        got = in_the_weak_stem(gana="an-anta", before="ṅi")
        self.assertEqual(got.sutra, "6.4.136")
        self.assertTrue(got.optional)

    def test_the_plain_loss_is_not_optional(self):
        self.assertFalse(in_the_weak_stem(gana="an-anta").optional)

    def test_a_cluster_in_v_or_m_refuses_the_loss_outright(self):
        # पर्वणा, चर्मणा — and this beats both 6.4.134 and 6.4.136.
        got = in_the_weak_stem(gana="an-anta", part="a",
                               result="saṃyoga-va-ma-anta")
        self.assertEqual(got.sutra, "6.4.137")
        self.assertEqual(got.does, "")
        self.assertIn("6.4.134", got.blocked_by)

    def test_the_refusal_beats_the_option_too(self):
        got = in_the_weak_stem(gana="an-anta", part="a",
                               result="saṃyoga-va-ma-anta",
                               before="ṅi")
        self.assertEqual(got.sutra, "6.4.137")
        self.assertFalse(got.optional)


class AhanAndTheFence(unittest.TestCase):
    """6.4.145 is a नियम, not a fresh provision."""

    def test_ahan_loses_its_ti_before_ta_and_kha(self):
        # द्व्यहः, द्व्यहीनः.
        got = in_the_weak_stem(stem="ahan", before="ṭa")
        self.assertEqual(got.sutra, "6.4.145")

    def test_the_rule_it_fences_had_already_supplied_the_loss(self):
        # सिद्धे सत्यारम्भो नियमार्थः — 6.4.144 नस्तद्धिते gives the
        # टि-loss to every न्-final stem before a taddhita; 6.4.145
        # exists to say "before ट and ख and nowhere else".
        self.assertIn("6.4.144", provisions_for("6.4.145")[0].blocks)
        self.assertEqual(in_the_weak_stem(gana="n-anta",
                                          before="taddhita").sutra,
                         "6.4.144")


class UBeforeATaddhita(unittest.TestCase):
    """6.4.146's guṇa against 6.4.147's loss."""

    def test_u_takes_guna_before_a_taddhita(self):
        # बाभ्रव्यः, औपगवः.
        got = in_the_weak_stem(gana="u-anta", before="taddhita")
        self.assertEqual(got.sutra, "6.4.146")
        self.assertEqual(got.does, "guṇa")

    def test_but_before_dha_the_u_is_dropped_instead(self):
        # कामण्डलेयः — a loss, not a strengthening.
        got = in_the_weak_stem(gana="u-anta", before="ḍha")
        self.assertEqual(got.sutra, "6.4.147")
        self.assertEqual(got.does, "lopa")

    def test_kadru_is_named_out_of_the_loss(self):
        # काद्रवेयो मन्त्रमपश्यत् — कद्रू keeps its ऊ before ढ.
        got = in_the_weak_stem(stem="kadrū", gana="u-anta",
                               before="ḍha")
        self.assertNotEqual(got.sutra, "6.4.147")


class YasyetiCa(unittest.TestCase):
    """6.4.148 and the three य-losses that follow it."""

    def test_i_or_a_is_lost_before_i_and_a_taddhita(self):
        # दाक्षी, प्लाक्षी, सखी.
        got = in_the_weak_stem(gana="i-a-anta", before="ī")
        self.assertEqual(got.sutra, "6.4.148")

    def test_four_stems_lose_the_ya_of_their_penult(self):
        # सौरी बलाका — and the four are named, not a class.
        self.assertEqual(SURYADI,
                         ("sūrya", "tiṣya", "agastya", "matsya"))
        for stem in SURYADI:
            got = in_the_weak_stem(stem=stem, before="ī")
            self.assertEqual(got.sutra, "6.4.149", stem)

    def test_a_taddhitas_ya_goes_before_i(self):
        # गार्गी, वात्सी — and the य lost is the taddhita's own.
        got = in_the_weak_stem(part="taddhita-ya", before="ī",
                               result="hal-pūrva")
        self.assertEqual(got.sutra, "6.4.150")

    def test_a_patronymics_ya_goes_before_a_taddhita_not_in_a(self):
        # गार्गकम् — but गार्ग्यायणः keeps it, its taddhita
        # beginning with आ.
        got = in_the_weak_stem(part="āpatya-ya", before="taddhita",
                               result="hal-pūrva")
        self.assertEqual(got.sutra, "6.4.151")
        kept = in_the_weak_stem(part="āpatya-ya", before="āt-taddhita",
                                result="hal-pūrva")
        self.assertNotEqual(kept.sutra, "6.4.151")

    def test_and_the_same_before_kya_and_cvi(self):
        # गार्गीयति, गार्गीभूतः.
        for affix in ("kyac", "cvi"):
            got = in_the_weak_stem(part="āpatya-ya", before=affix,
                                   result="hal-pūrva")
            self.assertEqual(got.sutra, "6.4.152", affix)


class TheWitnessesDisagree(unittest.TestCase):
    """6.4.130's text, as the two editions have it."""

    def test_the_disagreement_is_recorded_and_not_inherited(self):
        # GRETIL runs the vṛtti's वक्ष्यति into the sūtra; Vidyut
        # reads the sūtra alone. The module keeps both readings
        # rather than silently choosing.
        corrupt, clean = GRETIL_CORRUPT
        self.assertIn(clean, corrupt)
        self.assertNotEqual(corrupt, clean)
        self.assertIn("GRETIL", provisions_for("6.4.130")[0].why)


class Registration(unittest.TestCase):
    """Every row of this run reaches the registry with real notes."""

    def test_every_sutra_is_registered(self):
        for row in BHA_TABLE:
            self.assertTrue(REGISTRY.has(row.sutra), row.sutra)

    def test_the_run_is_contiguous(self):
        codes = [row.sutra for row in BHA_TABLE]
        self.assertEqual(
            codes, ["6.4.%d" % n for n in range(129, 154)])

    def test_notes_are_written_out_and_not_stubs(self):
        for row in BHA_TABLE:
            notes = REGISTRY.get(row.sutra).notes
            self.assertGreater(len(notes), 100, row.sutra)
            self.assertIn("SETTLED", notes, row.sutra)


class WhatIsNotCodifiedYet(unittest.TestCase):
    """
    The debts, written as the exact shortfall.

    Each is a claim that will fail the moment the thing it names
    lands, and must then be rewritten to say what is true instead.
    """

    def test_the_bha_heading_reaches_past_this_module(self):
        # 6.4.154 तुरिष्ठेमेयस्सु opens the next stretch and 6.4.175
        # closes the pāda and the adhyāya. Both are codified in
        # istha_prakrtibhava, so what this module owes is only that
        # its own table stops at 153 — and it does.
        self.assertTrue(REGISTRY.has("6.4.154"))
        self.assertTrue(REGISTRY.has("6.4.175"))
        self.assertNotIn("6.4.154", [row.sutra for row in BHA_TABLE])

    def test_the_taddhitas_this_run_presupposes_are_live(self):
        # This was written as a debt — 6.4.144's आग्निशर्मिः needs
        # 4.1.95's इञ् and 6.4.150's गार्गी needs 4.1.105's यञ् —
        # and both landed with अध्याय ४. So the claim is now the
        # live dependency: the affixes these losses are stated
        # before are codified, and the तद्धित of 4.1.76 heads them.
        self.assertTrue(REGISTRY.has("4.1.95"))
        self.assertTrue(REGISTRY.has("4.1.105"))
        self.assertTrue(REGISTRY.has("4.1.76"))

    def test_the_sounds_these_losses_expose_are_live_now(self):
        # विदुषः has a ष् that 8.3.59 supplies once the वस् has
        # vocalised, and राज्ञः a ञ् that 8.4.40 gives. Both were
        # debts when this was written and both have landed, so
        # this run's output feeds a live rule at either end.
        self.assertTrue(REGISTRY.has("8.3.59"))
        self.assertTrue(REGISTRY.has("8.4.40"))


if __name__ == "__main__":
    unittest.main()
