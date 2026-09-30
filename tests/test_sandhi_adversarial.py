# -*- coding: utf-8 -*-
"""
Adversarial tests for the Paninian sandhi engine.

The purpose of these tests is to verify that the engine cannot be tricked into
producing the right surface form with a WRONG sutra citation, or applying a rule
outside its valid boundary, scope, or precedence.
"""
import unittest

from src.astadhyayi.sandhi import sandhi


class TestAdversarialSutraCitations(unittest.TestCase):
    """Verify that similar or competing rules cite the exact proper sutra."""

    def test_yan_vs_dirgha_boundary(self):
        # ik followed by non-savarna ac -> 6.1.77 (iko yan aci), NEVER 6.1.101
        res_yan = sandhi("dadhi atra")
        sutras_yan = [s.sutra for s in res_yan.outcomes[0].steps]
        self.assertIn("6.1.77", sutras_yan)
        self.assertNotIn("6.1.101", sutras_yan)

        # ik followed by savarna ac -> 6.1.101 (akah savarne dirghah), NEVER 6.1.77
        res_dirgha = sandhi("dadhi īśvaraḥ")
        sutras_dirgha = [s.sutra for s in res_dirgha.outcomes[0].steps]
        self.assertIn("6.1.101", sutras_dirgha)
        self.assertNotIn("6.1.77", sutras_dirgha)

    def test_guna_vs_vrddhi_precedence(self):
        # a + ac (ic) -> 6.1.88 (vrddhir eci) is an apavada to 6.1.87 (ad gunah)
        res_vrddhi = sandhi("kṛṣṇa ekatvam")
        surfaces = [o.surface for o in res_vrddhi.outcomes]
        self.assertIn("kṛṣṇaikatvam", surfaces)
        sutras = [s.sutra for s in res_vrddhi.outcomes[0].steps]
        self.assertIn("6.1.88", sutras)
        self.assertNotIn("6.1.87", sutras)

        # a + ik -> 6.1.87 (ad gunah)
        res_guna = sandhi("upa indraḥ")
        surfaces_guna = [o.surface for o in res_guna.outcomes]
        self.assertIn("upendraḥ", surfaces_guna)
        sutras_g = [s.sutra for s in res_guna.outcomes[0].steps]
        self.assertIn("6.1.87", sutras_g)
        self.assertNotIn("6.1.88", sutras_g)

    def test_scutva_vs_stutva_mutual_exclusion(self):
        # s followed by c -> scutva 8.4.40, NEVER stutva 8.4.41
        res_c = sandhi("haris cinoti")
        sutras_c = [s.sutra for s in res_c.outcomes[0].steps]
        self.assertIn("8.4.40", sutras_c)
        self.assertNotIn("8.4.41", sutras_c)

        # s followed by t -> stutva 8.4.41, NEVER scutva 8.4.40
        res_t = sandhi("haris ṭīkate")
        sutras_t = [s.sutra for s in res_t.outcomes[0].steps]
        self.assertIn("8.4.41", sutras_t)
        self.assertNotIn("8.4.40", sutras_t)

    def test_padanta_torananam_blocks_stutva(self):
        # 8.4.43 'na padāntāt ṭoranānam': padanta tavarga does not cause stutva on s
        # 'ṣaṭ + santaḥ' -> 'ṣaṭsantaḥ', 's' must NOT turn into 'ṣ'
        res = sandhi("ṣaṭ santaḥ")
        surfaces = [o.surface for o in res.outcomes]
        self.assertIn("ṣaṭsantaḥ", surfaces)
        for out in res.outcomes:
            self.assertNotIn("ṣaṭṣantaḥ", out.surface)
            sutras = [s.sutra for s in out.steps]
            self.assertNotIn("8.4.41", sutras)

    def test_padanta_parasavarna_optionality(self):
        # In padanta: 8.4.59 'vā padāntasya' makes parasavarna optional.
        # It must NOT cite 8.4.58 (nitya parasavarna for apadanta).
        res = sandhi("śam karomi")
        surfaces = [o.surface for o in res.outcomes]
        self.assertIn("śaṅkaromi", surfaces)
        self.assertIn("śaṃkaromi", surfaces)
        for out in res.outcomes:
            sutras = [s.sutra for s in out.steps]
            self.assertNotIn("8.4.58", sutras)

    def test_in_ku_condition_for_satva(self):
        # agni + su: after i (in) -> 8.3.59 satva applies -> agniṣu
        res_satva = sandhi("agni~su{pratyaya}")
        surfaces_satva = [o.surface for o in res_satva.outcomes]
        self.assertIn("agniṣu", surfaces_satva)
        sutras_satva = [s.sutra for s in res_satva.outcomes[0].steps]
        self.assertIn("8.3.59", sutras_satva)

        # ramā + su: after ā (not in / ku) -> satva does NOT apply -> ramāsu
        res_nosatva = sandhi("ramā~su{pratyaya}")
        surfaces_nosatva = [o.surface for o in res_nosatva.outcomes]
        self.assertIn("ramāsu", surfaces_nosatva)
        for out in res_nosatva.outcomes:
            self.assertNotIn("ramāṣu", out.surface)
            sutras_no = [s.sutra for s in out.steps]
            self.assertNotIn("8.3.59", sutras_no)

    def test_pragrhya_blocks_yan_and_dirgha(self):
        # Pragrhya (1.1.11 dvivacana) blocks yan: harī{dvivacana} etau -> harī etau (6.1.125)
        res_p = sandhi("harī{dvivacana} etau")
        surfaces_p = [o.surface for o in res_p.outcomes]
        self.assertIn("harīetau", surfaces_p)
        self.assertNotIn("haryetau", surfaces_p)
        sutras_p = [s.sutra for s in res_p.outcomes[0].steps]
        self.assertIn("6.1.125", sutras_p)
        self.assertNotIn("6.1.77", sutras_p)

        # Without dvivacana flag: yan 6.1.77 applies
        res_plain = sandhi("harī etau")
        surfaces_plain = [o.surface for o in res_plain.outcomes]
        self.assertIn("haryetau", surfaces_plain)
        sutras_plain = [s.sutra for s in res_plain.outcomes[0].steps]
        self.assertIn("6.1.77", sutras_plain)

    def test_va_sari_optional_retention(self):
        # rāmas śete -> 8.3.36 'vā śari' yields both rāmaḥ śete and rāmaśśete
        res = sandhi("rāmas śete")
        surfaces = [o.surface for o in res.outcomes]
        self.assertIn("rāmaḥśete", surfaces)
        self.assertIn("rāmaśśete", surfaces)
        # Confirm 8.3.36 is cited
        sutras = {s.sutra for o in res.outcomes for s in o.steps}
        self.assertIn("8.3.36", sutras)

    def test_etattadoh_sulopo_condition(self):
        # saḥ gacchati with stem:tad -> 6.1.132 sulopa: sa gacchati
        res_sa = sandhi("saḥ{stem:tad} gacchati")
        surfaces_sa = [o.surface for o in res_sa.outcomes]
        self.assertIn("sagacchati", surfaces_sa)
        sutras_sa = [s.sutra for s in res_sa.outcomes[0].steps]
        self.assertIn("6.1.132", sutras_sa)

        # With nan_samasa flag: 6.1.132 is blocked (akoranansamase hali)
        res_asa = sandhi("asaḥ{stem:tad,nan_samasa} gacchati")
        for out in res_asa.outcomes:
            sutras = [s.sutra for s in out.steps]
            self.assertNotIn("6.1.132", sutras)


if __name__ == "__main__":
    unittest.main()

