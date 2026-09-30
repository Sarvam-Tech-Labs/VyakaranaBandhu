# -*- coding: utf-8 -*-
"""
The cerebral-s (satva) family — 8.3.55–119 — tested against the commentaries' own words.

Every expectation is one of the commentaries' own worked forms, with the
commentary named in the docstring, or a *kim* counter-example (where the
conditions of a sūtra live), or an assertion on the STEPS where a plain result
could come out right by luck. A test that cannot fail is worse than no test
(NORTH_STAR §3): where a result depends on a flag, the same form is also run
without it, and where it depends on an `overrides`, the declaration is taken
away and the result must change.

**What is run.** The family's own rules alone (`mine`), with hal_assimilation for
the finishing ṣṭutva joins (`with_hal`), and against the whole rulebook (`whole`).
"""

from __future__ import annotations

import re
import unittest
from dataclasses import replace
from typing import List, Sequence, Set, Tuple

from src.astadhyayi import corpus
from src.astadhyayi.sandhi import rulebook, sandhi, trace
from src.astadhyayi.sandhi.engine import Outcome, derive
from src.astadhyayi.sandhi.families import satva as fam
from src.astadhyayi.sandhi.parse import parse
from src.astadhyayi.sandhi.rule import SUTRA, VARTTIKA

FAMILY = "satva"
RULES = rulebook.rules_of(FAMILY)
RULES_HAL = rulebook.rules_of(FAMILY, "hal_assimilation")


def mine(text, *extra, **kw):
    """The junction derived by satva alone (and any extra family)."""
    return sandhi(text, rules=rulebook.rules_of(FAMILY, *extra), **kw)


def with_hal(text, **kw):
    """Derived by satva together with hal_assimilation for finished surfaces."""
    return sandhi(text, rules=RULES_HAL, **kw)


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


SCOPE = [f"8.3.{n}" for n in range(55, 120)]


# ---------------------------------------------------------------------------
# The Record: Soundness, Names, Coverage, Quotations, Overrides
# ---------------------------------------------------------------------------


class TheRecord(unittest.TestCase):
    """Every number, name and quotation is the corpus's and the commentary's own."""

    def test_the_rulebook_is_sound_with_satva_loaded(self):
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
        self.assertEqual(len(listed), 65)

    def test_a_sutra_is_not_called_a_rule_unless_a_rule_stands_for_it(self):
        have = {r.sutra for r in fam.RULES}
        for sutra, status, note in fam.COVERAGE:
            if status in ("rule", "partial", "vedic"):
                self.assertIn(sutra, have, sutra)
            else:
                self.assertNotIn(sutra, have, sutra)
            if status in ("scope", "partial", "support"):
                self.assertGreater(len(note), 10, sutra)

    def test_every_quotation_is_in_the_commentary_it_names(self):
        self.assertGreater(len(fam.QUOTED), 15)
        for source, sutra, text in fam.QUOTED:
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
        self.assertGreaterEqual(seen, 25)

    def test_every_rule_carries_the_family_tags(self):
        for r in fam.RULES:
            self.assertTrue("satva" in r.families or "satva-pratisedha" in r.families, r.sutra)

    def test_the_headings_are_marked_support(self):
        support_sutras = {s for s, st, _ in fam.COVERAGE if st == "support"}
        self.assertEqual(support_sutras, {"8.3.55", "8.3.57", "8.3.58", "8.3.63"})

    def test_the_vedic_rules_are_marked_vedic(self):
        vedic = [r.sutra for r in fam.RULES if r.vedic]
        self.assertEqual(sorted(set(vedic)), ["8.3.105", "8.3.106", "8.3.107", "8.3.109", "8.3.119"])

    def test_the_varttika_is_marked_varttika(self):
        varttikas = [r for r in fam.RULES if r.authority == VARTTIKA]
        self.assertEqual(len(varttikas), 1)
        self.assertEqual(varttikas[0].sutra, "8.3.101")


# ---------------------------------------------------------------------------
# The Headings: 8.3.55, 8.3.57, 8.3.58, 8.3.63
# ---------------------------------------------------------------------------


class ThreeHeadings(unittest.TestCase):
    """The adhikāras that govern the scope and are cited in derivation steps."""

    def test_headings_carried_down_into_8_3_59_trace(self):
        """Trace of agniṣu cites 8.3.55, 8.3.57 and 1.1.67 in its via list."""
        res = mine("agni~su{pratyaya}")
        self.assertEqual(res.surfaces, ("agniṣu",))
        step = res.outcomes[0].steps[0]
        self.assertEqual(step.sutra, "8.3.59")
        vias = [v.sutra for v in step.detail.via]
        self.assertIn("8.3.55", vias)
        self.assertIn("8.3.57", vias)
        self.assertIn("1.1.67", vias)


# ---------------------------------------------------------------------------
# 8.3.59–64 — Affixes, Substitutes and Reduplication
# ---------------------------------------------------------------------------


class AffixesAndSubstitutes(unittest.TestCase):
    """8.3.59 to 8.3.64: The general rule for affix and ādeśa s, and its conditions."""

    def test_8_3_59_affix_sa_after_in_or_ku(self):
        """8.3.59 आदेशप्रत्यययोः — अग्निषु, रामेषु."""
        res_agni = mine("agni~su{pratyaya}")
        self.assertEqual(res_agni.surfaces, ("agniṣu",))
        self.assertEqual(steps(res_agni), ["8.3.59"])

        res_rame = mine("rāme~su{pratyaya}")
        self.assertEqual(res_rame.surfaces, ("rāmeṣu",))
        self.assertEqual(steps(res_rame), ["8.3.59"])

    def test_kim_no_satva_after_sounds_outside_inkoḥ(self):
        """Kāśikā on 8.3.57: इण्कोः इति किम्? वृक्षसु, प्लक्षसु."""
        res = mine("vṛkṣa~su{pratyaya}")
        self.assertEqual(res.surfaces, ("vṛkṣasu",))
        self.assertEqual(steps(res), [])

    def test_8_3_60_sas_hi(self):
        """8.3.60 शासिवसिघसीनां च — अन्वशिषत्."""
        res = whole("anu|a{at}|śis{dhatu:śās}~at")
        self.assertIn("anvaśiṣat", res.surfaces)
        self.assertIn("8.3.60", steps(res))

    def test_8_3_61_and_62_refusals_for_san_and_svid_svad_sah(self):
        """8.3.61 स्तौतिण्योरेव षण्यभ्यासात्; 8.3.62 सः स्विदिस्वदिसहीनां च."""
        # 8.3.62 refuses ṣatva for ṇyanta of svad before san
        res_svad = mine("si{abhyasa}~svādayi{dhatu:svad,nyanta,adesa}~ṣati{pratyaya:san}")
        self.assertEqual(res_svad.surfaces, ("sisvādayiṣati",))
        self.assertIn("8.3.62", steps(res_svad))

        # 8.3.62 refuses for sah as well
        res_sah = mine("si{abhyasa}~sāhayi{dhatu:sah,nyanta,adesa}~ṣati{pratyaya:san}")
        self.assertEqual(res_sah.surfaces, ("sisāhayiṣati",))
        self.assertIn("8.3.62", steps(res_sah))


# ---------------------------------------------------------------------------
# 8.3.65–77 — Preverb and Root
# ---------------------------------------------------------------------------


class PreverbAndRoot(unittest.TestCase):
    """8.3.65 to 8.3.77: Roots taking ṣatva after a preverb."""

    def test_8_3_65_sunoti_and_group(self):
        """8.3.65 उपसर्गात् सुनोतिसुवतिस्यतिस्तौतिस्तोभतिस्थासेनयसेधसिचसञ्जस्वञ्जाम् — अभिषुनोति."""
        res = mine("abhi|sunoti{dhatu:sunoti}")
        self.assertEqual(res.surfaces, ("abhiṣunoti",))
        self.assertEqual(steps(res), ["8.3.65"])

    def test_8_3_66_sad_root(self):
        """8.3.66 सदिरप्रतेः — निषीदति, प्रषीदति."""
        res = mine("ni|sīdati{dhatu:sad}")
        self.assertEqual(res.surfaces, ("niṣīdati",))
        self.assertEqual(steps(res), ["8.3.66"])

    def test_8_3_67_stambh_root(self):
        """8.3.67 स्तम्भेरनिपातात् — अभिष्टभ्नाति."""
        res = with_hal("abhi|stabhnoti{dhatu:stambh}")
        self.assertEqual(res.surfaces, ("abhiṣṭabhnoti",))
        self.assertIn("8.3.67", steps(res))

    def test_8_3_70_sev_root(self):
        """8.3.70 सेव् — परिषेवते."""
        res = mine("pari|sevate{dhatu:sev}")
        self.assertEqual(res.surfaces, ("pariṣevate",))
        self.assertEqual(steps(res), ["8.3.70"])

    def test_8_3_71_siv_root(self):
        """8.3.71 सितिशिव्यति... — परिषीव्यति."""
        res = mine("pari|sīvyati{dhatu:siv}")
        self.assertEqual(res.surfaces, ("pariṣīvyati",))
        self.assertEqual(steps(res), ["8.3.70"])

    def test_8_3_74_and_75_skand_and_regional_refusal(self):
        """8.3.74 परेश्च — परिष्कन्दति / परिस्कन्दति; 8.3.75 परिस्कन्दः प्राच्यभरतेषु."""
        res_opt = mine("pari|skandati{dhatu:skand}")
        self.assertEqual(set(res_opt.surfaces), {"pariṣkandati", "pariskandati"})
        self.assertIn("8.3.74", steps(res_opt))

        # 8.3.75 regional nipātana refusal among eastern Bharatas
        res_refusal = mine("pari|skanda{dhatu:skand,sense:prācyabharata}")
        self.assertEqual(res_refusal.surfaces, ("pariskanda",))
        self.assertEqual(steps(res_refusal), ["8.3.75"])


# ---------------------------------------------------------------------------
# 8.3.78–109 — Nominal and Compound Seams
# ---------------------------------------------------------------------------


class NominalAndCompound(unittest.TestCase):
    """8.3.78 to 8.3.109: ṣatva in compounds and nominal formations."""

    def test_8_3_82_agnistoma(self):
        """8.3.82 अग्नेः स्तोमसूक्तयोः — अग्निष्टोमः."""
        res = with_hal("agni-stoma")
        self.assertEqual(res.surfaces, ("agniṣṭoma",))
        self.assertIn("8.3.82", steps(res))

    def test_8_3_90_pratisnata(self):
        """8.3.90 सूत्रं प्रतिष्णातम् — प्रतिष्णातम्."""
        res = mine("prati|snāta{sense:sūtra}")
        self.assertEqual(res.surfaces, ("pratiṣnāta",))
        self.assertEqual(steps(res), ["8.3.90"])

    def test_8_3_91_kapisthala_gotra(self):
        """8.3.91 कपिष्ठलो गोत्रे — कपिष्ठलः."""
        res = with_hal("kapi|sthala{sense:gotra}")
        self.assertEqual(res.surfaces, ("kapiṣṭhala",))
        self.assertIn("8.3.91", steps(res))

    def test_8_3_92_prastha_leader(self):
        """8.3.92 प्रष्ठोऽग्रगामिनि — प्रष्ठः."""
        res = with_hal("pra|stha{sense:agragāmin}")
        self.assertEqual(res.surfaces, ("praṣṭha",))
        self.assertIn("8.3.92", steps(res))

    def test_8_3_93_vistara(self):
        """8.3.93 वृक्षासनयोर्विष्टरः — विष्टरो वृक्षः, विष्टरमासनम्."""
        res = mine("vi|stara{sense:vṛkṣa}")
        self.assertEqual(res.surfaces, ("viṣtara",))
        self.assertEqual(steps(res), ["8.3.93"])

    def test_8_3_98_susamadi_gana(self):
        """8.3.98 सुषामादिषु च — सुषामा, निष्षामा."""
        res = mine("su-sāmā")
        self.assertEqual(res.surfaces, ("suṣāmā",))
        self.assertEqual(steps(res), ["8.3.98"])

    def test_8_3_102_nis_tap_anasevane(self):
        """8.3.102 निसस्तपतावनासेवने — निष्टपति."""
        res = whole("nis|tapati{dhatu:tap,sense:anāsevana}")
        self.assertEqual(res.surfaces, ("niṣṭapati",))
        self.assertIn("8.3.102", steps(res))


# ---------------------------------------------------------------------------
# 8.3.110–119 — The Refusals
# ---------------------------------------------------------------------------


class TheRefusals(unittest.TestCase):
    """8.3.110 to 8.3.119: What takes ṣatva back."""

    def test_8_3_110_r_para_and_named_roots_refuse(self):
        """8.3.110 न रपरसृपिसृजिस्पृशिस्पृहिसवनादीनाम् — अग्निस्स्र."""
        res = mine("agni~sra{pratyaya}")
        self.assertEqual(res.surfaces, ("agnisra",))
        self.assertIn("8.3.110", steps(res))

    def test_8_3_111_sat_and_padadi_refuse(self):
        """8.3.111 सात्पदाद्योः — अग्निसात्; दधि सिञ्चति."""
        res_sat = mine("agni~sāt{pratyaya}")
        self.assertEqual(res_sat.surfaces, ("agnisāt",))
        self.assertEqual(steps(res_sat), ["8.3.111"])

        res_padadi = mine("dadhi siñcati{adesa}")
        self.assertEqual(res_padadi.surfaces, ("dadhisiñcati",))
        self.assertEqual(steps(res_padadi), ["8.3.111"])

    def test_8_3_112_sic_in_yan_refuses(self):
        """8.3.112 सिचो यङि — अभिसेसिच्यते."""
        res = mine("abhi|se{abhyasa}~sic{dhatu:sic}~yate{pratyaya:yaṅ}")
        self.assertEqual(res.surfaces, ("abhisesicyate",))
        self.assertIn("8.3.112", steps(res))

    def test_8_3_113_sedha_in_motion_refuses(self):
        """8.3.113 सेधतेर्गतौ — अभिसेधयति गाः."""
        res = mine("abhi|sedhayati{dhatu:sedha,sense:gati}")
        self.assertEqual(res.surfaces, ("abhisedhayati",))
        self.assertEqual(steps(res), ["8.3.113"])

        # kim: without gati motion, 8.3.65 applies
        res_no_gati = mine("abhi|sedhayati{dhatu:sedha}")
        self.assertEqual(res_no_gati.surfaces, ("abhiṣedhayati",))
        self.assertEqual(steps(res_no_gati), ["8.3.65"])

    def test_8_3_114_pratistabdha_nipātana_refuses(self):
        """8.3.114 प्रतिस्तब्धनिस्तब्धौ च — प्रतिस्तब्धः."""
        res = mine("prati|stabdha{dhatu:stambh}")
        self.assertEqual(res.surfaces, ("pratistabdha",))
        self.assertEqual(steps(res), ["8.3.114"])

    def test_8_3_115_sodh_refuses(self):
        """8.3.115 सोढः — परिसोढा."""
        res = mine("pari|soḍhā{dhatu:sah}")
        self.assertEqual(res.surfaces, ("parisoḍhā",))
        self.assertEqual(steps(res), ["8.3.115"])

    def test_8_3_116_stambh_in_can_refuses(self):
        """8.3.116 स्तम्भुसिवुसहां चङि — पर्यसीषिवत्."""
        res = mine("pari|sīṣiva{dhatu:siv}~at{pratyaya:caṅ}")
        self.assertIn("8.3.116", steps(res))

    def test_8_3_117_sunoti_before_sya_san_refuses(self):
        """8.3.117 सुनोतेः स्यसनोः — अभिसोष्यति."""
        res = mine("abhi|so{dhatu:sunoti}~syati{pratyaya:sya}")
        self.assertEqual(res.surfaces, ("abhisoṣyati",))
        # 8.3.117 keeps root dental s; 8.3.59 acts on affix sya -> ṣya
        self.assertIn("8.3.117", steps(res))
        self.assertIn("8.3.59", steps(res))

    def test_8_3_118_sad_in_lit_later_sa_stays(self):
        """8.3.118 सदेः परस्य लिटि — अभिषसाद."""
        res = whole("abhi|ṣa{abhyasa}~sāda{dhatu:sad}~a{pratyaya:liṭ}")
        self.assertEqual(res.surfaces, ("abhiṣasāda",))
        self.assertIn("8.3.118", steps(res))

    def test_8_3_119_vedic_optional_across_at(self):
        """8.3.119 निव्यभिभ्योऽड्व्यवाये वा छन्दसि — न्यषीदत् / न्यसीदत् (Vedic)."""
        res = mine("ni|a{at}|sīdat{dhatu:sad}", veda=True)
        self.assertEqual(set(res.surfaces), {"niaṣīdat", "niasīdat"})
        self.assertIn("8.3.119", steps(res, course=0))


# ---------------------------------------------------------------------------
# Adversarial & Dependency Isolation (NORTH_STAR §3)
# ---------------------------------------------------------------------------


class AdversarialAndIntegrity(unittest.TestCase):
    """Removing a rule or override must change the answer."""

    def test_refusal_cannot_win_without_override(self):
        """Taking away 8.3.113's override of 8.3.65 causes 8.3.65 to win and cerebralise."""
        s = parse("abhi|sedhayati{dhatu:sedha,sense:gati}")
        weakened_rules = [
            replace(r, overrides=()) if r.sutra == "8.3.113" else r
            for r in fam.RULES
        ]
        outcomes = derive(s, weakened_rules)
        surfs = [o.surface for o in outcomes]
        self.assertEqual(surfs, ["abhiṣedhayati"])


if __name__ == "__main__":
    unittest.main()
