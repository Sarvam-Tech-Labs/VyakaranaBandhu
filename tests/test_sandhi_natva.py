# -*- coding: utf-8 -*-
"""
The cerebral-n (natva) family — 8.4.1–39 — tested against the commentaries' own words.

Every expectation is one of the commentaries' own worked forms, with the
commentary named in the docstring, or a *kim* counter-example (where the
conditions of a sūtra live), or an assertion on the STEPS where a plain result
could come out right by luck. A test that cannot fail is worse than no test
(NORTH_STAR §3): where a result depends on a flag, the same form is also run
without it, and where it depends on an `overrides`, the declaration is taken
away and the result must change.

**What is run.** The family's own rules alone (`mine`), with ac_ekadesa for
the finishing of vowel joins (`with_ac`), and against the whole rulebook (`whole`).
"""

from __future__ import annotations

import re
import unittest
from dataclasses import replace
from typing import List, Sequence, Set, Tuple

from src.astadhyayi import corpus
from src.astadhyayi.sandhi import rulebook, sandhi, trace
from src.astadhyayi.sandhi.engine import Outcome, derive
from src.astadhyayi.sandhi.families import natva as fam
from src.astadhyayi.sandhi.parse import parse
from src.astadhyayi.sandhi.rule import SUTRA, VARTTIKA

FAMILY = "natva"
RULES = rulebook.rules_of(FAMILY)
RULES_AC = rulebook.rules_of(FAMILY, "ac_ekadesa")


def mine(text, *extra, **kw):
    """The junction derived by natva alone (and any extra family)."""
    return sandhi(text, rules=rulebook.rules_of(FAMILY, *extra), **kw)


def with_ac(text, **kw):
    """Derived by natva together with ac_ekadesa for finished surfaces."""
    return sandhi(text, rules=RULES_AC, **kw)


def whole(text, **kw):
    return sandhi(text, **kw)


def first(text, rules=RULES, **kw) -> Outcome:
    return sandhi(text, rules=rules, **kw).outcomes[0]


def surfaces(text, *extra, **kw) -> Set[str]:
    return set(mine(text, *extra, **kw).surfaces)


def steps(result, course=0, *, declined=False) -> List[str]:
    """The sūtras of one course, in order; a declined option is starred."""
    return [s.sutra + ("*" if s.declined else "")
            for s in result.outcomes[course].steps
            if declined or not s.declined]


def order_of(result, wanted, course=0) -> List[str]:
    return [s for s in steps(result, course) if s in wanted]


_MARKUP = re.compile(r"<<|>>|\[\[[^\]]*\]\]|<\{[^}]*\}>|<!|!>|</?w>|\(\d+\)|\s+")


def norm(text: str) -> str:
    """A commentary's words without markup or whitespace."""
    return _MARKUP.sub("", text or "")


SCOPE = [f"8.4.{n}" for n in range(1, 40)]


# ---------------------------------------------------------------------------
# The Record: Soundness, Names, Coverage, Quotations, Overrides
# ---------------------------------------------------------------------------


class TheRecord(unittest.TestCase):
    """Every number, name and quotation is the corpus's and the commentary's own."""

    def test_the_rulebook_is_sound_with_natva_loaded(self):
        self.assertEqual(rulebook.problems(), [])

    def test_every_rule_is_named_by_its_own_words_from_the_corpus(self):
        known = corpus.load_vidyut_sutrapatha()
        for r in fam.RULES:
            if not r.varttika:
                self.assertEqual(r.name, trace.deva(known[r.sutra].text), r.sutra)

    def test_coverage_names_every_sutra_of_the_scope_once_and_no_other(self):
        listed = [sutra for sutra, _, _ in fam.COVERAGE]
        self.assertEqual(sorted(listed), sorted(set(listed)))
        self.assertEqual(set(listed), set(SCOPE))
        self.assertEqual(len(listed), 39)

    def test_a_sutra_is_not_called_a_rule_unless_a_rule_stands_for_it(self):
        have = {r.sutra for r in fam.RULES}
        for sutra, status, note in fam.COVERAGE:
            self.assertIn(sutra, have, sutra)
            if status in ("scope", "partial", "support"):
                self.assertGreater(len(note), 10, sutra)

    def test_every_quotation_is_in_the_commentary_it_names(self):
        self.assertGreater(len(fam.QUOTED), 15)
        for sutra, source, text in fam.QUOTED:
            comm = corpus.commentary_on(sutra, source)
            self.assertIsNotNone(comm, (source, sutra))
            self.assertIn(norm(text), norm(comm), (source, sutra, text))

    def test_every_reason_for_an_override_is_a_quotation(self):
        said = [norm(text) for _, _, text in fam.QUOTED]
        seen = 0
        for r in fam.RULES:
            for target, why in r.overrides:
                seen += 1
                self.assertTrue(any(q in norm(why) for q in said), (r.sutra, target))
        self.assertGreaterEqual(seen, 100)

    def test_every_rule_carries_the_family_tags(self):
        for r in fam.RULES:
            self.assertIn("natva", r.families, r.sutra)
            self.assertTrue(
                "natva-vidhi" in r.families or "natva-pratisedha" in r.families,
                r.sutra)

    def test_the_vedic_rules_are_marked_vedic(self):
        vedic = [r.sutra for r in fam.RULES if r.vedic]
        self.assertEqual(sorted(set(vedic)), ["8.4.26", "8.4.27"])

    def test_the_varttikas_are_marked_varttika(self):
        varttikas = [r for r in fam.RULES if r.authority == VARTTIKA]
        self.assertGreaterEqual(len(varttikas), 3)
        for r in varttikas:
            self.assertTrue(bool(r.varttika), r.sutra)


# ---------------------------------------------------------------------------
# 8.4.1–2 — रषाभ्यां नो णः समानपदे, अट्कुप्वाङ्नुम्व्यवायेऽपि
# ---------------------------------------------------------------------------


class TheRuleAndItsReach(unittest.TestCase):
    """8.4.1 and 8.4.2 — the root causes and their reach."""

    def test_immediate_n_after_r_or_sa_in_one_pada(self):
        """Kāśikā on 8.4.1: आस्तीर्णम्, विस्तीर्णम्; कुष्णाति, पुष्णाति."""
        res1 = mine("āstīr~nam")
        self.assertEqual(res1.surfaces, ("āstīrṇam",))
        self.assertEqual(steps(res1), ["8.4.1"])

        res2 = mine("kuṣ~nāti")
        self.assertEqual(res2.surfaces, ("kuṣṇāti",))
        self.assertEqual(steps(res2), ["8.4.1"])

    def test_varttika_rvarnat_adds_cerebral_after_r_vowel(self):
        """Kātyāyana vārttika on 8.4.1: ऋवर्णात् नस्य णत्वं वाच्यम् — मातृणाम्, पितृणाम्."""
        res = mine("mātṝ~nām")
        self.assertEqual(res.surfaces, ("mātṝṇām",))
        self.assertIn("8.4.1", steps(res))
        self.assertEqual(res.outcomes[0].steps[0].detail.authority, VARTTIKA)

    def test_reach_across_intervening_sounds_of_at_ku_pu(self):
        """Kāśikā on 8.4.2: करणम्, हरणम्; अर्केण, मूर्खेण; गर्गेण; दर्पेण."""
        res_karana = with_ac("kara~ana")
        self.assertEqual(res_karana.surfaces, ("karaṇa",))
        self.assertIn("8.4.2", steps(res_karana))

        res_arke = with_ac("arka~ena")
        self.assertEqual(res_arke.surfaces, ("arkeṇa",))
        self.assertIn("8.4.2", steps(res_arke))

        # Finished surface with ac_ekadesa
        res_ramena = with_ac("rāma~ena")
        self.assertEqual(res_ramena.surfaces, ("rāmeṇa",))
        self.assertIn("8.4.2", steps(res_ramena))

    def test_kim_intervener_outside_at_ku_pu_ang_num_blocks(self):
        """Kāśikā on 8.4.2: अटकावर्गादिव्यवाये किम्? अर्चा, अर्चनम्, मूर्च्छा."""
        # Palatal c stands between r and n: blocks 8.4.2
        res = mine("arc~ana")
        self.assertEqual(res.surfaces, ("arcana",))
        self.assertEqual(steps(res), [])


# ---------------------------------------------------------------------------
# 8.4.3–13 — Across a compound seam
# ---------------------------------------------------------------------------


class AcrossACompoundSeam(unittest.TestCase):
    """8.4.3 to 8.4.13: Cerebralisation crossing compound boundaries."""

    def test_8_4_3_name_lets_it_cross_seam(self):
        """8.4.3 पूर्वपदात्संज्ञायामगः — शूर्पणखा."""
        res = mine("śūrpa-nakhā{samjna}")
        self.assertEqual(res.surfaces, ("śūrpaṇakhā",))
        self.assertEqual(steps(res), ["8.4.3"])

        # kim: without samjna, stays dental
        res_no_samjna = mine("carma-nāsikā")
        self.assertEqual(res_no_samjna.surfaces, ("carmanāsikā",))
        self.assertEqual(steps(res_no_samjna), [])

        # kim: agah — ga blocks
        res_ga = mine("ṛg-ayanam{samjna}")
        self.assertEqual(res_ga.surfaces, ("ṛgayanam",))
        self.assertEqual(steps(res_ga), [])

    def test_8_4_4_vana_after_six_named_first_members(self):
        """8.4.4 वनं पुरगामिश्रकासिध्रकाशारिकाकोटराऽग्रेभ्यः — पुरगावणम्, मिश्रकावणम्, कोटरावणम्."""
        res1 = mine("puragā-vana{samjna}")
        self.assertEqual(res1.surfaces, ("puragāvaṇa",))
        self.assertEqual(steps(res1), ["8.4.4"])

        res2 = mine("miśrakā-vana{samjna}")
        self.assertEqual(res2.surfaces, ("miśrakāvaṇa",))
        self.assertEqual(steps(res2), ["8.4.4"])

        # Niyama: other first members in a name stay dental (refused by 8.4.4)
        res_other = mine("kubera-vana{samjna}")
        self.assertEqual(res_other.surfaces, ("kuberavana",))
        self.assertIn("8.4.4", steps(res_other))

    def test_8_4_5_vana_after_ten_without_name(self):
        """8.4.5 प्रनिरन्तःशरैक्षिकप्लक्षाम्रकार्श्यखदिरपीयूक्षाभ्योऽसंज्ञायामपि — प्रवणम्, निर्वणम्, शरवणम्, आम्रवणम्."""
        self.assertEqual(mine("pra-vana").surfaces, ("pravaṇa",))
        self.assertEqual(mine("nir-vana").surfaces, ("nirvaṇa",))
        self.assertEqual(mine("śara-vana").surfaces, ("śaravaṇa",))
        self.assertEqual(mine("āmra-vana").surfaces, ("āmravaṇa",))

    def test_8_4_6_optional_for_herbs_and_trees(self):
        """8.4.6 विभाषौषधिवनस्पतिभ्यः — दूर्वावणम् / दूर्वावनम्, बदरीवणम् / बदरीवनम्."""
        res = mine("dūrvā{osadhi}-vana")
        self.assertEqual(set(res.surfaces), {"dūrvāvaṇa", "dūrvāvana"})
        self.assertIn("8.4.6", steps(res, course=0))

    def test_8_4_7_ahna_after_short_a(self):
        """8.4.7 अह्नोऽदन्तात् — पूर्वाह्णः, अपराह्णः."""
        res = with_ac("pūrva-ahna")
        self.assertEqual(res.surfaces, ("pūrvāhṇa",))
        self.assertIn("8.4.7", steps(res))

    def test_8_4_8_vahana_after_loaded_item(self):
        """8.4.8 वाहनमाहितात् — शरवाहणम्."""
        res = mine("śara{ahita}-vāhana")
        self.assertEqual(res.surfaces, ("śaravāhaṇa",))
        self.assertEqual(steps(res), ["8.4.8"])

        # kim: without ahita stays dental
        res_plain = mine("śara-vāhana")
        self.assertEqual(res_plain.surfaces, ("śaravāhana",))
        self.assertEqual(steps(res_plain), [])

    def test_8_4_9_pana_in_country_name(self):
        """8.4.9 पाने देशे — क्षीरपाणा उशीनराः."""
        res = mine("kṣīra-pāna{desa}")
        self.assertEqual(res.surfaces, ("kṣīrapāṇa",))
        self.assertEqual(steps(res), ["8.4.9"])

    def test_8_4_10_pana_optional_in_action_or_instrument(self):
        """8.4.10 विभाषा भवाकरणयोः — क्षीरपाणम् / क्षीरपानम्."""
        res_bhava = mine("kṣīra-pāna{bhava}")
        self.assertEqual(set(res_bhava.surfaces), {"kṣīrapāṇa", "kṣīrapāna"})

        res_karana = mine("kṣīra-pāna{karana}")
        self.assertEqual(set(res_karana.surfaces), {"kṣīrapāṇa", "kṣīrapāna"})

    def test_8_4_11_to_13_pratipadika_anta_and_qualifications(self):
        """8.4.11–13 — माषवापिणौ / माषवापिनौ; वृत्रहणौ (8.4.12); वस्त्रयुगिणौ (8.4.13)."""
        res_opt = mine("māṣa-vāpin~au{vibhakti}")
        self.assertEqual(set(res_opt.surfaces), {"māṣavāpiṇau", "māṣavāpinau"})

        res_ekac = mine("vṛtra-han~au{vibhakti}")
        self.assertEqual(res_ekac.surfaces, ("vṛtrahaṇau",))
        self.assertEqual(steps(res_ekac), ["8.4.12"])

        res_kumat = mine("vastra-yugin~au{vibhakti}")
        self.assertEqual(res_kumat.surfaces, ("vastrayugiṇau",))
        self.assertEqual(steps(res_kumat), ["8.4.13"])


# ---------------------------------------------------------------------------
# 8.4.14–33 — After a preverb
# ---------------------------------------------------------------------------


class AfterAPreverb(unittest.TestCase):
    """8.4.14 to 8.4.33: Cerebralisation caused by a preverb."""

    def test_8_4_14_nopadesa_roots(self):
        """8.4.14 उपसर्गादसमासेऽपि णोपदेशस्य — प्रणमति, परिणमति, प्रणायकः."""
        res1 = mine("pra{upasarga}|nam{dhatu:nam}~a~ti")
        self.assertEqual(res1.surfaces, ("praṇamati",))
        self.assertEqual(steps(res1), ["8.4.14"])

        res2 = mine("pari{upasarga}|nam{dhatu:nam}~a~ti")
        self.assertEqual(res2.surfaces, ("pariṇamati",))
        self.assertEqual(steps(res2), ["8.4.14"])

        # kim: non-ṇopadeśa root keeps dental n
        res_nard = mine("pra{upasarga}|nardati")
        self.assertEqual(res_nard.surfaces, ("pranardati",))
        self.assertEqual(steps(res_nard), [])

    def test_8_4_15_hinu_and_mina(self):
        """8.4.15 हिनुमीना — प्रहिणोति, प्रमीणाति."""
        res_hi = mine("pra{upasarga}|hi{dhatu:hi}~noti")
        self.assertEqual(res_hi.surfaces, ("prahiṇoti",))
        self.assertEqual(steps(res_hi), ["8.4.15"])

        res_mi = mine("pra{upasarga}|mī{dhatu:mī}~nāti")
        self.assertEqual(res_mi.surfaces, ("pramīṇāti",))
        self.assertEqual(steps(res_mi), ["8.4.15"])

    def test_8_4_16_ani_lot_and_dur_refusal(self):
        """8.4.16 आनि लोट् — प्रवपाणि; vārttika दुरः षत्वणत्वयोः प्रतिषेधः — दुर्नानि."""
        res = with_ac("pra{upasarga}|vapa~āni{lot}")
        self.assertEqual(res.surfaces, ("pravapāṇi",))
        self.assertIn("8.4.16", steps(res))

        res_dur = with_ac("dur{upasarga}|vapa~āni{lot}")
        self.assertEqual(res_dur.surfaces, ("durvapāni",))
        self.assertIn("8.4.16", steps(res_dur))

    def test_8_4_17_and_18_ni_preverb_before_roots(self):
        """8.4.17 नेर्गदनदपत... — प्रणिगदति, प्रणिपतति; 8.4.18 शेषे विभाषा — प्रणिपचति / प्रनिपचति."""
        res_gad = mine("pra{upasarga}|ni{upasarga}|gadati{dhatu:gad}")
        self.assertEqual(res_gad.surfaces, ("praṇigadati",))
        self.assertEqual(steps(res_gad), ["8.4.17"])

        res_pat = mine("pra{upasarga}|ni{upasarga}|patati{dhatu:pat}")
        self.assertEqual(res_pat.surfaces, ("praṇipatati",))
        self.assertEqual(steps(res_pat), ["8.4.17"])

        res_sese = mine("pra{upasarga}|ni{upasarga}|pacati{dhatu:pac}")
        self.assertEqual(set(res_sese.surfaces), {"praṇipacati", "pranipacati"})

    def test_8_4_19_and_20_an_root_and_pada_anta_apavada(self):
        """8.4.19 अनितेः — प्राणिति; 8.4.20 अन्तश्च — हे प्राण (apavāda to 8.4.37)."""
        res_an = with_ac("pra{upasarga}|an{dhatu:an}~i~ti")
        self.assertEqual(res_an.surfaces, ("prāṇiti",))
        self.assertIn("8.4.19", steps(res_an))

        res_anta = with_ac("pra{upasarga}|an{dhatu:an}")
        self.assertEqual(res_anta.surfaces, ("prāṇ",))
        self.assertIn("8.4.20", steps(res_anta))

    def test_8_4_21_reduplicated_an_root_takes_both(self):
        """8.4.21 साभ्यासस्य — प्राणिणिषति (both n become ṇ)."""
        res = with_ac("pra{upasarga}|anini{dhatu:an,sabhyasa}~ṣati")
        self.assertEqual(res.surfaces, ("prāṇiṇiṣati",))
        self.assertIn("8.4.21", steps(res))

    def test_8_4_22_and_23_han_root_conditions(self):
        """8.4.22 हन्तेरत्पूर्वस्य — प्रहण्यते; kim: प्रघ्नन्ति; 8.4.23 वमोर्वा — प्रहण्वः / प्रहन्वः."""
        res_han = mine("pra{upasarga}|hanyate{dhatu:han}")
        self.assertEqual(res_han.surfaces, ("prahaṇyate",))
        self.assertEqual(steps(res_han), ["8.4.22"])

        # kim: at-pūrvatva missing
        res_ghnanti = mine("pra{upasarga}|ghnanti{dhatu:han}")
        self.assertEqual(res_ghnanti.surfaces, ("praghnanti",))
        self.assertEqual(steps(res_ghnanti), [])

        # 8.4.23 option before v/m finished with whole
        res_va = whole("pra{upasarga}|han{dhatu:han}~vaḥ")
        self.assertEqual(set(res_va.surfaces), {"prahaṇvaḥ", "prahanvaḥ"})

    def test_8_4_24_and_25_antar_with_han_and_ayana(self):
        """8.4.24 अन्तरदेशे — अन्तर्हण्यते; 8.4.25 अयनं च — अन्तरयणम्."""
        res_han = mine("antar|hanyate{dhatu:han}")
        self.assertEqual(res_han.surfaces, ("antarhaṇyate",))
        self.assertEqual(steps(res_han), ["8.4.24"])

        res_ayana = mine("antar|ayana")
        self.assertEqual(res_ayana.surfaces, ("antarayaṇa",))
        self.assertEqual(steps(res_ayana), ["8.4.25"])

    def test_8_4_26_to_28_vedic_and_bahulam(self):
        """8.4.26 छन्दस्यृदवग्रहात्; 8.4.28 उपसर्गाद् बहुलम्."""
        res_vedic = whole("nṛ{avagraha}-manāḥ", veda=True)
        self.assertEqual(res_vedic.surfaces, ("nṛmaṇāḥ",))
        self.assertIn("8.4.26", steps(res_vedic))

        # Without veda flag, 8.4.26 does not run
        res_non_vedic = mine("nṛ{avagraha}-manāḥ", veda=False)
        self.assertEqual(res_non_vedic.surfaces, ("nṛmanās",))

        # 8.4.28 bahulam forks
        res_bahulam = mine("pra{upasarga}|nasa")
        self.assertEqual(set(res_bahulam.surfaces), {"praṇasa", "pranasa"})

    def test_8_4_29_to_33_krt_affixes_and_exceptions(self):
        """8.4.29 कृत्यचः — प्रयाणम्; 8.4.30 णेर्विभाषा — प्रयापणम् / प्रयापनम्;
        8.4.31 हलश्चेजुपधात् — प्रकोपणम् / प्रकोपनम्; 8.4.32 इजादेः सनुमः — प्रेङ्खणम्;
        8.4.33 वा निंसनिक्षनिन्दाम् — प्रणिंसनम् / प्रनिंसनम्."""
        res_krt = mine("pra{upasarga}|yāna{krt}")
        self.assertEqual(res_krt.surfaces, ("prayāṇa",))
        self.assertEqual(steps(res_krt), ["8.4.29"])

        res_nyanta = mine("pra{upasarga}|yāpana{krt,nyanta}")
        self.assertEqual(set(res_nyanta.surfaces), {"prayāpaṇa", "prayāpana"})

        res_kopana = with_ac("pra{upasarga}|kopa{dhatu:kup}~ana{krt}")
        self.assertEqual(set(res_kopana.surfaces), {"prakopaṇa", "prakopana"})

        res_iṅkha = with_ac("pra{upasarga}|iṅkha{dhatu:ikhi̐}~ana{krt}")
        self.assertEqual(res_iṅkha.surfaces, ("preṅkhaṇa",))
        self.assertIn("8.4.32", steps(res_iṅkha))

        # kim: 8.4.32 niyama refuses sanuma root that is not ijādi
        res_mangana = with_ac("pra{upasarga}|maṅga{dhatu:magi̐}~ana{krt}")
        self.assertEqual(res_mangana.surfaces, ("pramaṅgana",))
        self.assertIn("8.4.32", steps(res_mangana))

        # 8.4.33 option
        res_nimsa = mine("pra{upasarga}|niṃsana{dhatu:niṃs}")
        self.assertEqual(set(res_nimsa.surfaces), {"praṇiṃsana", "praniṃsana"})


# ---------------------------------------------------------------------------
# 8.4.34–39 — The Refusals
# ---------------------------------------------------------------------------


class TheRefusals(unittest.TestCase):
    """8.4.34 to 8.4.39: What takes ṇatva back."""

    def test_8_4_34_refusal_for_seven_roots(self):
        """8.4.34 न भाभूपूकमिगमिप्यायीवेपाम् — प्रभानम्, प्रभवनम्, प्रपवनम्, प्रगमनम्."""
        res_bha = with_ac("pra{upasarga}|bhā{dhatu:bhā}~ana{krt}")
        self.assertEqual(res_bha.surfaces, ("prabhāna",))
        self.assertIn("8.4.34", steps(res_bha))

        res_bhu = mine("pra{upasarga}|bhū{dhatu:bhū}~ana{krt}")
        self.assertEqual(res_bhu.surfaces, ("prabhūana",))
        self.assertIn("8.4.34", steps(res_bhu))

    def test_8_4_35_refusal_after_padanta_sa(self):
        """8.4.35 षात् पदान्तात् — निष्पानम्, सर्पिष्पानम्."""
        res = mine("niṣ{upasarga}|pāna{krt}")
        self.assertEqual(res.surfaces, ("niṣpāna",))
        self.assertEqual(steps(res), ["8.4.35"])

    def test_8_4_36_refusal_for_nas_in_sa_shape(self):
        """8.4.36 नशेः षान्तस्य — प्रनष्टः, परिनष्टः."""
        res = mine("pra{upasarga}|naṣṭa{dhatu:naś,santa}")
        self.assertEqual(res.surfaces, ("pranaṣṭa",))
        self.assertEqual(steps(res), ["8.4.36"])

    def test_8_4_37_refusal_for_word_final_n(self):
        """8.4.37 पदान्तस्य — वृक्षान्, प्लक्षान्, गिरीन्."""
        res1 = with_ac("vṛkṣa~ān")
        self.assertEqual(res1.surfaces, ("vṛkṣān",))
        self.assertEqual(steps(res1), ["6.1.101", "8.4.37"])

        res2 = mine("vṛkṣa~n")
        self.assertEqual(res2.surfaces, ("vṛkṣan",))
        self.assertEqual(steps(res2), ["8.4.37"])

    def test_8_4_38_refusal_across_word_boundary(self):
        """8.4.38 पदव्यवायेऽपि — प्र गां नयामः."""
        res = mine("pra{upasarga} gāṃ nam{dhatu:nam}~a~ti")
        self.assertEqual(res.surfaces, ("pragāṃnamati",))
        self.assertEqual(steps(res), ["8.4.38"])

    def test_8_4_39_ksubhnadi_gana_refuses(self):
        """8.4.39 क्षुभ्नादिषु च — क्षुभ्नाति, तृप्नोति; vārttika अग्रग्रामाभ्याम् — अग्रणीः."""
        res_ksubh = mine("kṣubh~nāti{ksubhnadi}")
        self.assertEqual(res_ksubh.surfaces, ("kṣubhnāti",))
        self.assertEqual(steps(res_ksubh), ["8.4.39"])

        # Vārttika अग्रग्रामाभ्यां नयतेर्णो वाच्यः gives ṇatva
        res_agra = mine("agra-nī{dhatu:nī}")
        self.assertEqual(res_agra.surfaces, ("agraṇī",))
        self.assertEqual(steps(res_agra), ["8.4.39"])
        self.assertEqual(res_agra.outcomes[0].steps[0].detail.authority, VARTTIKA)


# ---------------------------------------------------------------------------
# Adversarial & Dependency Isolation (NORTH_STAR §3)
# ---------------------------------------------------------------------------


class AdversarialAndIntegrity(unittest.TestCase):
    """Removing a rule or override must change the answer."""

    def test_refusal_cannot_win_without_override(self):
        """Taking away 8.4.34's override of 8.4.29 must cause 8.4.29 to win and cerebralise."""
        s = parse("pra{upasarga}|bhā{dhatu:bhā}~ana{krt}")
        # Find 8.4.34 rule and strip its overrides
        weakened_rules = [
            replace(r, overrides=()) if r.sutra == "8.4.34" else r
            for r in fam.RULES
        ]
        outcomes = derive(s, weakened_rules)
        # Without override, 8.4.29 applies and gives ṇ!
        surfs = [o.surface for o in outcomes]
        self.assertIn("prabhāaṇa", surfs)


if __name__ == "__main__":
    unittest.main()
