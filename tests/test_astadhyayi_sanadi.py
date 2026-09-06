# -*- coding: utf-8 -*-
"""
यङ् — 3.1.22, 3.1.32, 3.1.134, 2.4.74, and the 6.4.77 that ends the run.

These five exist here for one reason: they are what carries लोलुवः and
मरीमृजः from a root to a finished stem, and those two are the Kāśikā's own
examples under 1.1.4. Until they were written, 1.1.4's `dhatu_lopa` was a
flag a caller set by hand and no derivation could ever set for itself.

So the test that matters most in this file is not that any one of the five
fires. It is that the prohibition is now *reached* — that a rule blocks
because of what an earlier rule in the same derivation did.
"""

from __future__ import annotations

import unittest

from src.astadhyayi.anga import iyan_uvan
from src.astadhyayi.sanadi import (
    Refused, dhatu_by, intensive_stem, pacadi, yan, yan_luk,
)


class TheTwoStemsOfOneOneFour(unittest.TestCase):

    def test_lu_gives_loluva_and_mrj_gives_marimrja(self):
        """
        लोलुवः and मरीमृजः, which is what 1.1.4's Kāśikā lists. The forms
        here are the stems; the visarga is the nominative ending on top.
        """
        self.assertEqual(intensive_stem("lū").form, "loluva")
        self.assertEqual(intensive_stem("mṛj").form, "marīmṛja")

    def test_the_prohibition_is_reached_and_not_asserted(self):
        """
        The point of the whole slice. 1.1.4 appears in both derivations
        because 2.4.74 elided the यङ् earlier in the same run, at the
        instance of the very affix that would have done the strengthening
        — तमेवाचम् आश्रित्य.

        Before these five existed, `dhatu_lopa=True` could only ever be
        typed in by whoever called the rule, which meant the condition was
        never tested against anything.
        """
        for root in ("lū", "mṛj"):
            with self.subTest(root=root):
                rules = intensive_stem(root).rules
                self.assertIn("2.4.74", rules)
                self.assertIn("1.1.4", rules)
                self.assertLess(rules.index("2.4.74"), rules.index("1.1.4"))

    def test_each_derivation_runs_the_rules_in_order(self):
        """
        यङ् added, copy shaped, stem named a root, अच् added, यङ् elided,
        strengthening forbidden, and only then उवङ्.
        """
        self.assertEqual(
            intensive_stem("lū").rules,
            ("3.1.22", "7.4.59", "7.4.82", "3.1.32", "3.1.134", "2.4.74",
             "1.1.4", "6.4.77"))
        self.assertEqual(
            intensive_stem("mṛj").rules,
            ("3.1.22", "7.4.60", "7.4.66", "7.4.90", "3.1.32", "3.1.134",
             "2.4.74", "1.1.4"))

    def test_without_the_block_the_form_would_be_lolava(self):
        """
        इयङुवङ्भ्यां गुणवृद्धी भवतो विप्रतिषेधेन — the strengthening beats
        उवङ् wherever both are available, and the Kāśikā's own लवनम् and
        लावकः are what that looks like.

        So उवङ् reaching the ऊ of लोलू is not the ordinary case; it is what
        happens only because 1.1.4 took the guṇa away. Take the धातुलोप out
        and 6.4.77 stands down and names 1.4.2 for doing so — and the ओ it
        leaves behind becomes अव् by 6.1.78, which is लोलवः.
        """
        blocked = iyan_uvan("lolū", ardhadhatuka=True, dhatu_lopa=True)
        self.assertTrue(blocked.applied)
        self.assertEqual(blocked.form, "loluv")
        self.assertEqual(blocked.by, "6.4.77")

        standing = iyan_uvan("lolū", ardhadhatuka=True, dhatu_lopa=False)
        self.assertFalse(standing.applied)
        self.assertEqual(standing.by, "1.4.2")


class TheConditionsOfThreeOneTwentyTwo(unittest.TestCase):
    """The Kāśikā tests each word of the sūtra, and so does this."""

    def test_it_reaches_the_four_worked_roots(self):
        """पापच्यते, यायज्यते, जाज्वल्यते, देदीप्यते."""
        for root, stem in (("pac", "pāpacya"), ("yaj", "yāyajya"),
                           ("jval", "jājvalya"), ("dīp", "dedīpya")):
            with self.subTest(root=root):
                made = yan(root)
                self.assertNotIsInstance(made, Refused)
                self.assertEqual(made.stem, stem)

    def test_dhatoh_iti_kim_a_root_with_a_preverb(self):
        """धातोरिति किम्? भृशं प्राटति — सोपसर्गाद् उत्पत्तिर्मा भूत्."""
        self.assertIsInstance(yan("aṭ", sopasarga=True), Refused)

    def test_ekac_iti_kim_jagarti(self):
        """एकाच इति किम्? भृशं जागर्ति — जागृ holds more than one vowel."""
        refused = yan("jāgṛ")
        self.assertIsInstance(refused, Refused)
        self.assertIn("एकाच", refused.why)

    def test_haladeh_iti_kim_ikshate(self):
        """हलादेरिति किम्? भृशम् ईक्षते — ईक्ष् begins with a vowel."""
        refused = yan("īkṣ")
        self.assertIsInstance(refused, Refused)
        self.assertIn("हलादे", refused.why)

    def test_the_sense_is_required_and_cannot_be_read_off_the_root(self):
        """
        क्रियासमभिहारे. भृशं शोभते and भृशं रोचते are refused अनभिधानात्,
        on usage alone — so the sense is asked for rather than inferred.
        """
        self.assertIsInstance(yan("pac", kriyasamabhihara=False), Refused)

    def test_the_varttika_root_ati_is_admitted_though_it_fails_both(self):
        """
        सूचिसूत्रिमूत्र्यट्यर्त्यशूर्णोतीनां ग्रहणं यङ्विधावनेकाजहलाद्यर्थम्.
        अट् begins with a vowel and would fail हलादि, and it is let in.
        """
        made = yan("aṭ")
        self.assertNotIsInstance(made, Refused)
        self.assertEqual(made.stem, "aṭāṭya")


class TheNameAndTheAffixAndTheElision(unittest.TestCase):

    def test_two_rules_confer_dhatu_and_the_right_one_answers(self):
        """
        लू is a root because a list says so; लोलूय is a root because the
        grammar built it. 3.1.32 is for the second and only the second —
        मरीमृज्य and लोलूय are in no dhātupāṭha.
        """
        self.assertEqual(dhatu_by("lū").by, "1.3.1")
        self.assertEqual(
            dhatu_by("lolūya", sanadyanta=True).by, "3.1.32")
        self.assertIsNone(dhatu_by("lolūya"))

    def test_pacadi_admits_a_yananta_because_the_gana_is_open(self):
        """
        The gaṇapāṭha on disk marks पचादि open-ended, and that flag is the
        reason a stem the grammar built can join a list of thirty-six.
        Read from the file rather than asserted here.
        """
        from src.astadhyayi.corpus import load_ganapatha

        gana = next(g for g in load_ganapatha()["3.1.134"]
                    if g.name.startswith("pacādi"))
        self.assertTrue(gana.open_ended)
        self.assertNotIn("lolūya", gana.items)

        self.assertEqual(pacadi("lolūya", yananta=True).by, "3.1.134")
        self.assertIsNone(pacadi("lolūya"))
        self.assertEqual(pacadi("paca").by, "3.1.134")

    def test_the_luk_takes_the_affix_and_leaves_its_work(self):
        """
        यङो लुग् भवत्यचि प्रत्यये परतः. The यङ् goes; the doubling it
        occasioned does not. That is the only reason there is a लोलू to
        speak of rather than a लू.
        """
        dropped = yan_luk("lolūya")
        self.assertEqual(dropped.stem, "lolū")
        self.assertEqual(dropped.by, "2.4.74")
        self.assertIsNone(yan_luk("lolūya", before_ac=False))
        self.assertIsNone(yan_luk("lolū"))


class WhatSixFourSeventySevenReaches(unittest.TestCase):

    def test_only_a_dhatu_a_snu_stem_or_bhru(self):
        """श्नुधातुभ्रुवामिति किम्? लक्ष्म्यै, वध्वै."""
        self.assertIsNone(
            iyan_uvan("lakṣmī", dhatu=False, ardhadhatuka=True,
                      dhatu_lopa=True))

    def test_the_final_must_be_an_i_or_a_u(self):
        """य्वोरिति किम्? चक्रतुः — the ऋ is neither."""
        self.assertIsNone(
            iyan_uvan("marīmṛj", ardhadhatuka=True, dhatu_lopa=True))


if __name__ == "__main__":
    unittest.main()
