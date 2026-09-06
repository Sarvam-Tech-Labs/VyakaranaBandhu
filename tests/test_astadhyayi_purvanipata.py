# -*- coding: utf-8 -*-
"""
पूर्वनिपात — 2.2.30 to 2.2.38, which member is spoken first.

This is the first thing in the compound section that is not a question
about whether two words join. Everything before it asks that; these nine
take a pair already joined and say which word comes out in front. The
failures available are therefore new ones: a rule that wins where a
narrower one should, a list of finished forms matched against a pair that
has not been formed yet, and a refusal that claims a rule fired.
"""

from __future__ import annotations

import unittest

from src.astadhyayi.purvanipata import (
    AHITAGNYADI, KADARADI, NoOrder, RAJADANTADI, spoken_first,
)


class TheGeneralRuleAndItsReversal(unittest.TestCase):

    def test_2_2_30_puts_the_subordinate_member_first(self):
        """
        उपसर्जनं पूर्वम्, and the Kāśikā walks every case: कष्टश्रितः,
        शङ्कुलाखण्डः, यूपदारु, वृकभयम्, राजपुरुषः, अक्षशौण्डः.
        """
        got = spoken_first(("rājan", "puruṣa"), upasarjana="rājan")
        self.assertEqual(got.by, "2.2.30")
        self.assertEqual(got.first, "rājan")

    def test_2_2_31_puts_it_last_instead(self):
        """
        राजदन्तादिषु परम्. The gaṇa holds FINISHED compounds — राजदन्तः,
        अग्रेवणम् — not pairs, so the form has to be named. Building it
        back from the two words would mean redoing the sandhi the gaṇa has
        already done, and राजन् + दन्त is not राजदन्तः.
        """
        got = spoken_first(("rājan", "danta"), form="rājadantaḥ",
                           upasarjana="rājan")
        self.assertEqual(got.by, "2.2.31")
        self.assertIn("rājadantaḥ", RAJADANTADI)

        # Without the form there is nothing to match, and 2.2.30 stands.
        self.assertEqual(
            spoken_first(("rājan", "danta"), upasarjana="rājan").by,
            "2.2.30")


class TheThreeDvandvaRules(unittest.TestCase):
    """
    A dvandva has no upasarjana — both members are principal — so 2.2.30
    settles nothing and these three have to.
    """

    def test_2_2_33_beats_2_2_32(self):
        """
        द्वन्द्वे घ्यन्ताद् अजाद्यदन्तं विप्रतिषेधेन. इन्द्र is both
        vowel-initial and अ-final; अग्नि is घि. The narrower wins.
        """
        got = spoken_first(("indra", "agni"), samasa="dvandva")
        self.assertEqual(got.by, "2.2.33")
        self.assertEqual(got.first, "indra")

    def test_2_2_32_where_no_word_is_ajadyadanta(self):
        """पटुगुप्तौ — and which words are घि is 1.4.7's, fetched from it."""
        got = spoken_first(("paṭu", "gupta"), samasa="dvandva")
        self.assertEqual(got.by, "2.2.32")
        self.assertEqual(got.first, "paṭu")

    def test_2_2_34_decides_what_the_other_two_leave(self):
        """अल्पाच्तरम् — प्लक्ष has two vowels, न्यग्रोध three."""
        got = spoken_first(("plakṣa", "nyagrodha"), samasa="dvandva")
        self.assertEqual(got.by, "2.2.34")
        self.assertEqual(got.first, "plakṣa")

    def test_bahusv_aniyamah_refuses_more_than_two(self):
        """
        बहुष्वनियमः, read with all three: अश्वरथेन्द्राः and
        इन्द्ररथाश्वाः both stand, and so do शङ्खदुन्दुभिवीणाः and
        वीणाशङ्खदुन्दुभयः.

        The refusal must not name a rule. Reporting 2.2.34 for it made a
        counter-example indistinguishable from a worked one — the same
        defect the reduplication entry points had.
        """
        got = spoken_first(("aśva", "ratha", "indra"), samasa="dvandva")
        self.assertIsInstance(got, NoOrder)
        self.assertEqual(got.by, "")
        self.assertIn("बहुष्वनियमः", got.why)


class TheBahuvrihiRules(unittest.TestCase):
    """
    सर्वोपसर्जनत्वाद् बहुव्रीहेः — every member is subordinate here, so
    2.2.30 names them all and settles nothing.
    """

    def test_2_2_35_takes_the_locative_or_the_qualifier(self):
        for kw, first in ((dict(saptami="kaṇṭha"), "kaṇṭha"),
                          (dict(visesana="citra"), "citra")):
            with self.subTest(**kw):
                got = spoken_first(("kaṇṭha", "kāla") if "saptami" in kw
                                   else ("citra", "go"),
                                   samasa="bahuvrīhi", **kw)
                self.assertEqual(got.by, "2.2.35")
                self.assertEqual(got.first, first)

    def test_2_2_36_takes_the_nistha(self):
        """कृतकटः — and 1.1.26 cannot be asked here, so it is stated."""
        got = spoken_first(("kṛta", "kaṭa"), samasa="bahuvrīhi",
                           nistha="kṛta")
        self.assertEqual(got.by, "2.2.36")
        self.assertEqual(got.first, "kṛta")

    def test_the_varttika_sends_it_to_second_place(self):
        """
        निष्ठायाः पूर्वनिपाते जातिकालसुखादिभ्यः परवचनम् — मासजातः,
        शार्ङ्गजग्धी. It reverses the rule rather than qualifying it,
        which is why it is codified and not merely recorded.
        """
        got = spoken_first(("jāta", "māsa"), samasa="bahuvrīhi",
                           nistha="jāta", jati_kala_sukha="māsa")
        self.assertEqual(got.first, "māsa")
        self.assertEqual(got.second, "jāta")


class TheTwoOptions(unittest.TestCase):

    def test_2_2_37_makes_2_2_36_a_choice(self):
        """अग्न्याहितः beside आहिताग्निः, and both are reported."""
        got = spoken_first(("āhita", "agni"), form="āhitāgniḥ",
                           nistha="āhita")
        self.assertEqual(got.by, "2.2.37")
        self.assertTrue(got.optional)
        self.assertEqual(got.alternative, ("agni", "āhita"))

    def test_2_2_38_makes_2_2_35_a_choice_and_closes_the_section(self):
        """
        कडारजैमिनिः beside जैमिनिकडारः. कर्मधारय इति किम्? कडारपुरुषो
        ग्रामः — outside a karmadhāraya there is no choice, and 2.2.35's
        qualifier rule would simply have applied.
        """
        got = spoken_first(("kaḍāra", "jaimini"), samasa="karmadhāraya")
        self.assertEqual(got.by, "2.2.38")
        self.assertTrue(got.optional)
        self.assertIn("kaḍāra", KADARADI)

        elsewhere = spoken_first(("kaḍāra", "puruṣa"),
                                 samasa="bahuvrīhi", visesana="kaḍāra")
        self.assertEqual(elsewhere.by, "2.2.35")
        self.assertFalse(elsewhere.optional)


class TheGanasAreReadFromDisk(unittest.TestCase):

    def test_all_three(self):
        """
        Fifty-seven, thirteen and nineteen, none of them retyped — the
        same reason as तिष्ठद्गु and शौण्डादि before them.
        """
        from src.astadhyayi.corpus import load_ganapatha

        for sutra, name, holding in (
                ("2.2.31", "rājadantādi", RAJADANTADI),
                ("2.2.37", "āhitāgnyādi", AHITAGNYADI),
                ("2.2.38", "kaḍārādi", KADARADI)):
            with self.subTest(sutra=sutra):
                gana = next(g for g in load_ganapatha()[sutra]
                            if g.name.startswith(name))
                self.assertEqual(holding, gana.items)

    def test_the_open_one_is_the_one_the_kasika_calls_open(self):
        """आकृतिगणश्चायम् is said of आहिताग्न्यादि and of no other here."""
        from src.astadhyayi.corpus import load_ganapatha

        openness = {}
        for sutra in ("2.2.31", "2.2.37", "2.2.38"):
            gana, = [g for g in load_ganapatha()[sutra]]
            openness[sutra] = gana.open_ended
        self.assertTrue(openness["2.2.37"])
        self.assertFalse(openness["2.2.31"])
        self.assertFalse(openness["2.2.38"])


if __name__ == "__main__":
    unittest.main()
