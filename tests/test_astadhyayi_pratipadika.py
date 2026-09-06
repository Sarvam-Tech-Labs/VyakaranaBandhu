# -*- coding: utf-8 -*-
"""
Tests for 1.2.41 to 1.2.46 — apṛkta, karmadhāraya, upasarjana, prātipadika.

1.2.43 is the one that reaches furthest. It is a fourth way of reading a case,
beside 1.1.49's sixth, 1.1.66's seventh and 1.1.67's fifth — and unlike those
three it is conditioned, so a first-case word is an upasarjana only in a rule
that makes a compound. Getting that wrong would make `nirdesa` claim an
upasarjana in most of the Aṣṭādhyāyī.

1.2.45's three conditions each have a counter-example in the Kāśikā, and two of
the three exist for the same reason: to save a final न् from being elided.
"""

from __future__ import annotations

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi import samjna as S
from src.astadhyayi.adesa import PRATHAMA, Side, nirdesa, prathama_padas
from src.astadhyayi.sources import facts


class Aprkta(unittest.TestCase):
    """1.2.41 अपृक्त एकाल् प्रत्ययः."""

    def test_one_sound_and_not_one_letter(self):
        self.assertTrue(S.aprkta("v"))
        self.assertTrue(S.aprkta("bh"), "a digraph is one al")
        self.assertFalse(S.aprkta("vi"))
        self.assertFalse(S.aprkta("tara"))

    def test_eka_is_read_as_it_is_at_1_1_14(self):
        """
        असहायवाची एकशब्दः — the Kāśikā gives the same gloss for एक here as for
        एकाच् there, so the two sūtras agree about what "one" means.
        """
        from src.astadhyayi.pragrhya import pragrhya

        self.assertTrue(S.aprkta("a"))
        self.assertIsNotNone(pragrhya("a", nipata=True))
        self.assertFalse(S.aprkta("pra"))
        self.assertIsNone(pragrhya("pra", nipata=True))

    def test_ekaliti_kim(self):
        """दर्विः, जागृविः — more than one sound."""
        self.assertFalse(S.aprkta("darvi"))
        self.assertFalse(S.aprkta("jāgṛvi"))


class Karmadharaya(unittest.TestCase):
    """1.2.42 तत्पुरुषः समानाधिकरणः कर्मधारयः."""

    def test_both_conditions_are_needed(self):
        self.assertTrue(
            S.karmadharaya(tatpurusa=True, samanadhikarana=True)
        )
        # तत्पुरुष इति किम्? पाचिकाभार्यः
        self.assertFalse(
            S.karmadharaya(tatpurusa=False, samanadhikarana=True)
        )
        # समानाधिकरण इति किम्? ब्राह्मणराज्यम्
        self.assertFalse(
            S.karmadharaya(tatpurusa=True, samanadhikarana=False)
        )

    def test_neither_alone(self):
        self.assertFalse(
            S.karmadharaya(tatpurusa=False, samanadhikarana=False)
        )


class Upasarjana(unittest.TestCase):
    """1.2.43 and 1.2.44."""

    def test_it_reads_the_first_case_off_the_rule(self):
        """
        2.1.24 द्वितीया श्रितातीतपतितगतात्यस्तप्राप्तापन्नैः — द्वितीया stands
        in the first case, so it is the upasarjana, and कष्टश्रितः follows.
        """
        self.assertEqual(prathama_padas("2.1.24"), ("द्वितीया",))
        self.assertEqual(S.upasarjana("2.1.24"), ("द्वितीया",))

    def test_it_is_a_fourth_case_reading_beside_the_other_three(self):
        reading = nirdesa("2.1.24", samasa_vidhi=True)
        self.assertEqual([n.side for n in reading], [Side.UPASARJANA])
        self.assertEqual([n.by for n in reading], ["1.2.43"])
        self.assertEqual(len(list(Side)), 4)

    def test_it_is_the_only_conditioned_one(self):
        """
        समास इति समासविधायि शास्त्रं गृह्यते. A first-case word in a sūtra
        that makes no compound is not an upasarjana, and 1.1.1 is full of
        first-case words.
        """
        self.assertEqual(nirdesa("2.1.24"), ())
        self.assertTrue(prathama_padas("1.1.1"))
        self.assertEqual(
            [n for n in nirdesa("1.1.1") if n.side is Side.UPASARJANA], []
        )

    def test_the_case_number_is_the_traditional_one(self):
        self.assertEqual(PRATHAMA, 1)
        cases = {p.word: p.vibhakti for p in facts("2.1.24").padas}
        self.assertEqual(cases["द्वितीया"], PRATHAMA)

    def test_1_1_44_adds_a_second_ground(self):
        """एकविभक्ति — निष्कौशाम्बिः, निष्कौशाम्बिम्, the second member fixed."""
        found = S.upasarjana("2.1.24", ekavibhakti=True)
        self.assertIn("द्वितीया", found)
        self.assertEqual(len(found), 2)

    def test_apurvanipate_withholds_it(self):
        """The exception is of one consequence, not of the name."""
        self.assertEqual(
            S.upasarjana("2.1.24", ekavibhakti=True, purvanipata=True),
            ("द्वितीया",),
        )


class Pratipadika(unittest.TestCase):
    """1.2.45 and 1.2.46."""

    def test_the_plain_case(self):
        """डित्थः, कपित्थः, कुण्डम्, पीठम्."""
        for form in ("ḍittha", "kapittha", "kuṇḍa", "pīṭha"):
            self.assertEqual(S.pratipadika(form).by, "1.2.45", form)

    def test_arthavaditi_kim(self):
        """वनम्, धनम् — the final -अन् means nothing by itself."""
        self.assertIsNone(S.pratipadika("an", arthavat=False))

    def test_adhaturiti_kim(self):
        """अहन् — a root is excluded, and for the same न् as above."""
        self.assertIsNone(S.pratipadika("ahan", dhatu=True))

    def test_apratyaya_iti_kim(self):
        """काण्डे, कुड्ये — else 1.2.47 would shorten them."""
        self.assertIsNone(S.pratipadika("e", pratyaya=True))

    def test_1_2_46_puts_back_what_apratyaya_excluded(self):
        for form, kind in [("kāraka", "krdanta"), ("aupagava", "taddhitanta"),
                           ("rājapuruṣa", "samasa")]:
            found = S.pratipadika(form, **{kind: True})
            self.assertEqual(found.by, "1.2.46", form)

    def test_a_krdanta_would_have_been_excluded_as_an_affix(self):
        """
        अप्रत्ययः इति पूर्वसूत्रे पर्युदासात् — which is why 1.2.46 is needed
        at all. Without it कारकः would fall foul of 1.2.45's third condition.
        """
        self.assertIsNone(S.pratipadika("kāraka", pratyaya=True))
        self.assertEqual(S.pratipadika("kāraka", krdanta=True).by, "1.2.46")

    def test_naming_the_compound_restricts_rather_than_adds(self):
        """
        समासग्रहणं नियमार्थम्, and the consequence: वाक्यस्यार्थवतः संज्ञा न
        भवति. A meaningful phrase satisfies 1.2.45 on its face and must not
        take the name — so the refusal has to be explicit.
        """
        self.assertIsNone(S.pratipadika("rājñaḥ puruṣaḥ", vakya=True))
        self.assertEqual(S.pratipadika("rājapuruṣa", samasa=True).by, "1.2.46")

    def test_the_nipata_varttika(self):
        """निपातस्यानर्थकस्य प्रातिपदिकसंज्ञा वक्तव्या — अध्यागच्छति, प्रलम्बते."""
        found = S.pratipadika("adhi", nipata=True, arthavat=False)
        self.assertEqual(found.by, "1.2.45")
        self.assertIn("निपातस्यानर्थकस्य", found.why,
                      "the vārttika it rests on has to be quoted")
        # and it holds although the word means nothing, which is the point
        self.assertIsNone(S.pratipadika("adhi", arthavat=False))

    def test_the_varttika_is_in_the_apparatus_for_1_2_45(self):
        from src.astadhyayi.corpus import varttikas_on

        texts = [v.text for v in varttikas_on("1.2.45")]
        self.assertTrue(
            any("निपातस्य" in t for t in texts), texts
        )

    def test_is_pratipadika_agrees_with_pratipadika(self):
        for form, ctx in [("ḍittha", {}), ("kāraka", dict(krdanta=True)),
                          ("an", dict(arthavat=False))]:
            self.assertEqual(
                S.is_pratipadika(form, **ctx),
                S.pratipadika(form, **ctx) is not None,
                form,
            )


class Registration(unittest.TestCase):
    IDS = tuple(f"1.2.{n}" for n in range(41, 47))

    def setUp(self):
        from src.astadhyayi.sutra import REGISTRY
        self.registry = REGISTRY

    def test_each_is_registered_and_executable(self):
        for sutra_id in self.IDS:
            sutra = self.registry.get(sutra_id)
            self.assertIsNotNone(sutra, sutra_id)
            self.assertTrue(callable(sutra.apply), sutra_id)

    def test_1_2_44_and_1_2_46_read_from_their_predecessors(self):
        self.assertIn(
            "1.2.43", " ".join(self.registry.get("1.2.44").anuvrtti)
        )
        self.assertIn(
            "1.2.45", " ".join(self.registry.get("1.2.46").anuvrtti)
        )

    def test_the_ucccaranartha_gap_is_recorded_again_on_1_2_41(self):
        """
        क्विन् and ण्वि cannot be run end to end for the same reason recorded
        under 1.3.9. The record has to say so where the reader meets it.
        """
        notes = self.registry.get("1.2.41").notes
        self.assertIn("SCOPE", notes)
        self.assertIn("उच्चारणार्थ", notes)
        self.assertIn("1.3.9", notes)

    def test_the_new_samjnas_are_registered(self):
        from src.astadhyayi.grahana import samjna_source

        for name, sutra_id in [("apṛkta", "1.2.41"),
                               ("karmadhāraya", "1.2.42"),
                               ("upasarjana", "1.2.43"),
                               ("prātipadika", "1.2.45")]:
            self.assertEqual(samjna_source(name), sutra_id, name)


if __name__ == "__main__":
    unittest.main()
