# -*- coding: utf-8 -*-
"""
Cross-family integration tests for the Pāṇinian sandhi engine.

Tests multi-word sentences and compound constructions where multiple rule families
interact across sequential junctions:
  * ac_yan_ayadi (6.1.77-79)
  * ac_ekadesa (6.1.87-111)
  * prakrtibhava (1.1.11-19, 6.1.125-130)
  * hal_assimilation (6.1.71-76, 8.2.24-41, 8.4.40-68)
  * nasal_anusvara (8.3.23-33, 8.4.45, 8.4.58-59)
  * visarga_ru (8.2.66-72, 8.3.14-54, 6.1.113-114, 6.1.132-134)
  * natva (8.4.1-39)
  * satva (8.3.55-119)
"""

from __future__ import annotations

import unittest
from typing import List, Set

from src.astadhyayi.sandhi import rulebook, sandhi
from src.astadhyayi.sandhi.engine import Outcome


def steps(outcome: Outcome) -> List[str]:
    return [s.sutra for s in outcome.steps if not s.declined]


class CrossFamilySentenceSandhi(unittest.TestCase):
    """Multi-word sentence derivations combining rules across different families."""

    def test_visarga_hal_and_ac_ekadesa(self):
        """rāmas + ca + atra -> rāmaścātra
        Involves:
          visarga_ru: 8.2.66 (sasajuṣo ruḥ), 8.3.15 (visarga), 8.3.34 (saḥ)
          hal_assimilation: 8.4.40 (ścutva)
          ac_ekadesa: 6.1.101 (akaḥ savarṇe dīrghaḥ)
        """
        r = sandhi("rāmas ca atra")
        self.assertIn("rāmaścātra", r.surfaces)
        primary = r.outcomes[0]
        st = steps(primary)
        self.assertIn("8.2.66", st)
        self.assertIn("8.4.40", st)
        self.assertIn("6.1.101", st)

    def test_visarga_and_purvarupa(self):
        """haris + śete + atra -> hariḥśete'tra / hariśśete'tra
        Involves:
          visarga_ru: 8.3.36 (vā śari)
          ac_ekadesa: 6.1.109 (eṅaḥ padāntād ati)
        """
        r = sandhi("haris śete atra")
        surfs = set(r.surfaces)
        self.assertTrue(any("śete'tra" in s for s in surfs), surfs)
        self.assertTrue(any("8.3.36" in steps(o) for o in r.outcomes))
        self.assertTrue(any("6.1.109" in steps(o) for o in r.outcomes))

    def test_hal_visarga_and_purvarupa(self):
        """tat + śivaḥ + asti -> tacchivo'sti / tacśivo'sti
        Involves:
          hal_assimilation: 8.2.39 (jaśtva), 8.4.40 (ścutva), 8.4.55 (cartva), 8.4.63 (śaścho 'ṭi)
          visarga_ru: 8.2.66 (rutva), 6.1.113 (utva), 6.1.87 (guṇa)
          ac_ekadesa: 6.1.109 (pūrvarūpa)
        """
        r = sandhi("tat śivaḥ asti")
        self.assertIn("tacchivo'sti", r.surfaces)
        self.assertIn("tacśivo'sti", r.surfaces)
        st = steps(r.outcomes[0])
        self.assertIn("8.4.40", st)
        self.assertIn("6.1.113", st)
        self.assertIn("6.1.109", st)

    def test_natva_and_yan(self):
        """pra-namati + agnau -> praṇamatyagnau
        Involves:
          natva: 8.4.14 (upasargād asunoti...)
          ac_yan_ayadi: 6.1.77 (iko yaṇaci)
        """
        r = sandhi("pra{upasarga}|nam{dhatu:nam}~a~ti agnau")
        self.assertTrue(any(s.startswith("praṇamaty") for s in r.surfaces), r.surfaces)
        st = steps(r.outcomes[0])
        self.assertIn("8.4.14", st)
        self.assertIn("6.1.77", st)

    def test_satva_and_yan(self):
        """agni-su + atra -> agniṣvatra
        Involves:
          satva: 8.3.59 (ādeśapratyayayoḥ)
          ac_yan_ayadi: 6.1.77 (iko yaṇaci)
        """
        r = sandhi("agni~su{pratyaya} atra")
        self.assertTrue(any(s.startswith("agniṣv") for s in r.surfaces), r.surfaces)
        st = steps(r.outcomes[0])
        self.assertIn("8.3.59", st)
        self.assertIn("6.1.77", st)

    def test_prakrtibhava_and_ayadi(self):
        """harī (dual) + etau + atra -> harī etāvatra / harī etāatra
        Involves:
          prakrtibhava: 1.1.11 (īdūded dvivacanam), 6.1.125 (pluta-pragṛhyāḥ)
          ac_yan_ayadi: 6.1.78 (eco 'yavāyāvaḥ), 8.3.19 (lopaḥ śākalyasya)
        """
        r = sandhi("harī{dvivacana} etau atra")
        surfs = set(r.surfaces)
        self.assertTrue("harīetāvatra" in surfs or "harīetāatra" in surfs, surfs)
        st = steps(r.outcomes[0])
        self.assertIn("6.1.125", st)
        self.assertIn("6.1.78", st)

    def test_tuk_and_savarnadirgha(self):
        """śiva + chāyā + atra -> śivacchāyātra
        Involves:
          hal_assimilation: 6.1.73 (che ca tuk), 8.4.40 (ścutva)
          ac_ekadesa: 6.1.101 (akaḥ savarṇe dīrghaḥ)
        """
        r = sandhi("śiva chāyā atra")
        self.assertIn("śivacchāyātra", r.surfaces)
        st = steps(r.outcomes[0])
        self.assertIn("6.1.73", st)
        self.assertIn("6.1.101", st)

    def test_anusvara_parasavarna_and_yan(self):
        """tvam + karoṣi + atra -> tvaṅkaroṣyatra / tvaṃkaroṣyatra
        Involves:
          nasal_anusvara: 8.3.23 (mo 'nusvāraḥ), 8.4.59 (vā padāntasya)
          ac_yan_ayadi: 6.1.77 (iko yaṇaci)
        """
        r = sandhi("tvam karoṣi atra")
        surfs = set(r.surfaces)
        self.assertTrue(any(s.endswith("karoṣyatra") for s in surfs), surfs)
        st = steps(r.outcomes[0])
        self.assertIn("8.3.23", st)
        self.assertIn("6.1.77", st)


class ClassicLiterarySentences(unittest.TestCase):
    """Classical sentences and idiom patterns testing multiple interactions."""

    def test_so_pi_vs_sa_gacchati(self):
        """saḥ + api -> so'pi (no sulopa before ac, 6.1.113 applies).
        saḥ + gacchati -> sa gacchati (6.1.132 sulopa before hal).
        """
        r_ac = sandhi("sas api")
        self.assertIn("so'pi", r_ac.surfaces)

        r_hal = sandhi("sas gacchati")
        self.assertIn("sagacchati", r_hal.surfaces)
        self.assertIn("6.1.132", steps(r_hal.outcomes[0]))

    def test_esa_visnuh_vs_eso_tra(self):
        """eṣaḥ + viṣṇuḥ -> eṣa viṣṇuḥ (6.1.132 sulopa).
        eṣaḥ + atra -> eṣo'tra (6.1.113 utva + 6.1.109 pūrvarūpa).
        """
        r_hal = sandhi("eṣas viṣṇuḥ")
        self.assertIn("eṣaviṣṇuḥ", r_hal.surfaces)

        r_ac = sandhi("eṣas atra")
        self.assertIn("eṣo'tra", r_ac.surfaces)

    def test_bho_brahmanah(self):
        """bhos + brāhmaṇāḥ -> bho brāhmaṇāḥ (8.3.17 + 8.3.22 hali sarveṣām)."""
        r = sandhi("bhos brāhmaṇāḥ")
        self.assertIn("bhobrāhmaṇāḥ", r.surfaces)
        st = steps(r.outcomes[0])
        self.assertIn("8.3.17", st)
        self.assertIn("8.3.22", st)

    def test_puna_ramate_iha(self):
        """punar + ramate + iha -> punāramata iha / punāramateha
        Involves ro ri (8.3.14) + dīrgha (6.3.111) + ayādi (6.1.78).
        """
        r = sandhi("punar ramate iha")
        surfs = set(r.surfaces)
        self.assertTrue(any(s.startswith("punāramat") for s in surfs), surfs)
        self.assertTrue(any("8.3.14" in steps(o) for o in r.outcomes))


class InterlockAndOrder(unittest.TestCase):
    """The tripādī and sapādasaptādhyāyī boundary holds cleanly across families."""

    def test_tripadi_does_not_feed_sapadadi_unless_prescribed(self):
        """When 8.2.66 produces ru -> visarga -> s (8.3.34), this is tripādī.
        8.4.40 (ścutva) is further down in tripādī and sees the s made by 8.3.34."""
        r = sandhi("rāmas ca")
        st = steps(r.outcomes[0])
        self.assertEqual(st, ["8.2.66", "8.3.15", "8.3.34", "8.4.40"])

    def test_jas_tva_before_scutva_and_cartva(self):
        """sat + cit -> saccit: 8.2.39 (jaśtva) -> 8.4.40 (ścutva) -> 8.4.55 (cartva)."""
        r = sandhi("sat cit")
        st = [s.sutra for s in r.outcomes[0].steps[:3] if s.sutra in ("8.2.39", "8.4.40", "8.4.55")]
        self.assertEqual(st, ["8.2.39", "8.4.40", "8.4.55"])

    def test_rulebook_is_sound_with_all_families_active(self):
        """Every family is loaded and rulebook has zero problems."""
        self.assertEqual(rulebook.problems(), [])


if __name__ == "__main__":
    unittest.main()
