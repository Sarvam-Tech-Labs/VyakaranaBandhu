"""
Pāṇinian & Harināmāmṛta Kṛdanta & Taddhitānta Derivative Engine
================================================================
Implements primary verbal derivatives (Kṛt / कृदन्त) and secondary nominal
derivatives (Taddhita / तद्धितान्त) with dual canonical sūtra citations:
1. Pāṇini's Aṣṭādhyāyī (Books 3, 4, 5)
2. Harināmāmṛta-Vyākaraṇa & Gopī Caraṇa Dāsa's Taddhitoddīpanī
"""

from typing import Dict, Any, List, Optional, Tuple
import re
from .normalizer import devanagari_to_iast, iast_to_devanagari
from .prakriti_pratyaya import DHATU_REGISTRY, UPASARGAS

# =====================================================================
# 1. Kṛdanta Affixes (Primary Verbal Derivatives / कृत्-प्रत्ययाः)
# =====================================================================

KRDANTA_AFFIXES = {
    # 1.1 Non-finite / Avyaya Kṛt Affixes (अव्यय-कृतः)
    "ktvā": {
        "name": "Ktvā (क्त्वा)",
        "anubandhas": "k (kniti ca 1.1.5 prevents guṇa) + vā",
        "category": "Avyaya (पूर्वकालिक क्रिया / Prior Action)",
        "meaning": "having done / having performed (e.g. kṛtvā, gatvā)",
        "sutra_panini": "samānakartṛkayoḥ pūrvakāle (3.4.21)",
        "sutra_hnv": "HNV Kṛdanta 3.21: pūrvakāle dhātoḥ ktvā-saṅketaḥ",
        "tika_exegesis": "Bāla-Toṣaṇī: Indicates consecutive devotional service where the prior act is consecrated to the Lord."
    },
    "lyap": {
        "name": "Lyap (ल्यप्)",
        "anubandhas": "l + ya + p (substitutes ktvā when preceded by upasarga)",
        "category": "Avyaya (सोपसर्ग पूर्वकालिक क्रिया / Prefixed Prior Action)",
        "meaning": "having thoroughly done / approached (e.g. sametya, praṇamya)",
        "sutra_panini": "samāse'nañpūrve ktvo lyap (7.1.37)",
        "sutra_hnv": "HNV Kṛdanta 3.24: sopasargasya ktvo lyab-ādeśaḥ",
        "tika_exegesis": "Bāla-Toṣaṇī: Upasarga intensifies devotion, converting the raw ktvā into sweet lyap."
    },
    "tumun": {
        "name": "Tumun (तुमुन्)",
        "anubandhas": "u + m + u + n -> tum (Triggers guṇa)",
        "category": "Avyaya (हेत्वर्थक / Infinitive of Purpose)",
        "meaning": "in order to / for the purpose of (e.g. kartum, gantum)",
        "sutra_panini": "tumunṇvulau kriyāyāṃ kriyārthāyām (3.3.10) & samāna-kartṛkeṣu tumun (3.3.158)",
        "sutra_hnv": "HNV Kṛdanta 3.12: hetvarthāyāṃ kriyāyāṃ tumun",
        "tika_exegesis": "Bāla-Toṣaṇī: Expresses devotional purpose (Seva-sādhana-hetu)."
    },

    # 1.2 Participial Subanta Kṛt Affixes (कृदन्त-सुबन्त-प्रत्ययाः)
    "kta": {
        "name": "Kta (क्त - Past Passive Participle)",
        "anubandhas": "k (prevents guṇa) + ta -> ta",
        "category": "Subanta Base (भूतकालिक कृदन्त / Past Passive)",
        "meaning": "done / gone / manifested (e.g. kṛtaḥ, gataḥ, dṛṣṭaḥ)",
        "sutra_panini": "niṣṭhā (1.1.26) & kto'dhikaraṇe ca ca dhrauvyagatipratyavasānārthebhyaḥ (3.4.76) / niṣṭhā (3.2.102)",
        "sutra_hnv": "HNV Kṛdanta 3.45: atīte karmani kta-saṅketaḥ",
        "tika_exegesis": "Bāla-Toṣaṇī: Niṣṭhā affix seals the completed past pastime of the Lord."
    },
    "ktavatu": {
        "name": "Ktavatu (क्तवतु - Past Active Participle)",
        "anubandhas": "k + t + a + vat + u -> tavat (Declines like dhīmat)",
        "category": "Subanta Base (भूतकालिक कर्तरि कृदन्त / Past Active)",
        "meaning": "one who has done / acted (e.g. kṛtavān, gatavān)",
        "sutra_panini": "niṣṭhā (1.1.26) & kartari kṛt (3.4.67) / ktaktavatū niṣṭhā (3.2.102)",
        "sutra_hnv": "HNV Kṛdanta 3.47: kartari bhūte ktavatu-pratyayaḥ",
        "tika_exegesis": "Bāla-Toṣaṇī: Declines across all genders, qualifying the conscious agent of service."
    },
    "satr": {
        "name": "Śatṛ (शतृ - Present Active Participle)",
        "anubandhas": "ś + a + t + ṛ -> at (Declines like gacchat / bhavat)",
        "category": "Subanta Base (वर्तमानकालिक कर्तरि / Present Continuous Active)",
        "meaning": "while doing / going / seeing (e.g. kurvan, gacchan, paśyan)",
        "sutra_panini": "laṭaḥ śatṛśānacāvaprathamāsamānādhikaraṇe (3.2.124)",
        "sutra_hnv": "HNV Kṛdanta 3.52: vartamāne laṭ-sthāne śatṛ-śānacau",
        "tika_exegesis": "Bāla-Toṣaṇī: Represents unceasing, uninterrupted engagement in service."
    },
    "sanac": {
        "name": "Śānac (शानच् - Present Middle Participle)",
        "anubandhas": "ś + ā + n + a + c -> māna (Declines like rāma/latā/phala)",
        "category": "Subanta Base (वर्तमानकालिक आत्मनेपद / Present Continuous Middle)",
        "meaning": "while doing for oneself (e.g. kurvāṇaḥ, yudhyamānaḥ)",
        "sutra_panini": "laṭaḥ śatṛśānacāvaprathamāsamānādhikaraṇe (3.2.124) & tṅānāvātmanepadam (1.4.100)",
        "sutra_hnv": "HNV Kṛdanta 3.54: ātmanepada-dhātor māna-saṅketaḥ",
        "tika_exegesis": "Bāla-Toṣaṇī: Expresses continuous internal contemplation and devotion."
    },
    "tavya": {
        "name": "Tavya (तव्य - Gerundive / Obligation)",
        "anubandhas": "tavya (Triggers guṇa of root vowel)",
        "category": "Subanta Base (कृत्य / Potential & Obligation)",
        "meaning": "ought to be done / worthy of action (e.g. kartavyam, gantavyam)",
        "sutra_panini": "tavyattavyānīyaraḥ (3.1.96) & kṛtyāḥ (3.1.95)",
        "sutra_hnv": "HNV Kṛdanta 3.70: yogyārthe tavyānīyādayaḥ",
        "tika_exegesis": "Bāla-Toṣaṇī: Highlights prescribed duty (dharma) and spiritual mandate."
    },
    "aniya": {
        "name": "Anīya (अनीय - Worthy of / Deserving)",
        "anubandhas": "anīya (Triggers guṇa of root vowel)",
        "category": "Subanta Base (कृत्य / Potential & Worthiness)",
        "meaning": "fit to be remembered / worshiped (e.g. karaṇīyam, smaraṇīyam)",
        "sutra_panini": "tavyattavyānīyaraḥ (3.1.96)",
        "sutra_hnv": "HNV Kṛdanta 3.71: sevanīya-pūjanīyārthe anīya-saṅketaḥ",
        "tika_exegesis": "Bāla-Toṣaṇī: Designates qualities worthy of eternal adoration."
    }
}

# =====================================================================
# 2. Taddhitānta Affixes (Secondary Derivatives / तद्धित-प्रत्ययाः)
# =====================================================================

TADDHITA_AFFIXES = {
    "matup": {
        "name": "Matup (मतुप् - Possessive)",
        "anubandhas": "m + a + t + u + p -> mat / vat",
        "category": "Matvarthīya Taddhita (मत्वर्थीय / Possession & Endowed With)",
        "meaning": "possessing / endowed with (e.g. dhīmat -> dhīmān, bhagavat -> bhagavān)",
        "sutra_panini": "tad asyāstyasminniti matup (5.2.94) & mād upadhāyāś ca matvo vo'yavādibhyaḥ (8.2.9)",
        "sutra_hnv": "HNV Taddhita 4.12: tadvān iti matup",
        "tika_exegesis": "Gopī Caraṇa Dāsa (Taddhitoddīpanī): Bhagavat signifies one who possesses all 6 divine opulences in full."
    },
    "inith": {
        "name": "Ini / Inith (इनि / इनिठ् - Possessor)",
        "anubandhas": "in -> in (Declines as guṇin -> guṇī, balin -> balī)",
        "category": "Matvarthīya Taddhita (मत्वर्थीय / Inherent Possessor)",
        "meaning": "having / endowed with quality (e.g. guṇin -> guṇī, jñānin -> jñānī)",
        "sutra_panini": "ata iniṭhanau (5.2.115)",
        "sutra_hnv": "HNV Taddhita 4.25: adantāt tadavato'rthe iniḥ",
        "tika_exegesis": "Gopī Caraṇa Dāsa (Taddhitoddīpanī): Inherent possession of spiritual wisdom (jñāna) or virtue (guṇa)."
    },
    "tva": {
        "name": "Tva (त्व - Abstract Neuter Noun)",
        "anubandhas": "tva -> tva (Forms neuter stem e.g. kṛṣṇatvam, devatvam)",
        "category": "Bhāvārthaka Taddhita (भावार्थक / Essential Nature)",
        "meaning": "the state of being / -ness (e.g. kṛṣṇatvam = state of being Kṛṣṇa)",
        "sutra_panini": "tasya bhāvastvatalau (5.1.119)",
        "sutra_hnv": "HNV Taddhita 4.60: bhāvārthe tva-talau",
        "tika_exegesis": "Gopī Caraṇa Dāsa (Taddhitoddīpanī): Reveals the fundamental ontological essence (tattva) of the base."
    },
    "tal": {
        "name": "Tal (तल् - Abstract Feminine Noun)",
        "anubandhas": "t + a + l -> tā (Forms ā-feminine stem e.g. devatā, kavitā)",
        "category": "Bhāvārthaka Taddhita (भावार्थक / Essential Quality - Feminine)",
        "meaning": "the state / quality of being (e.g. pavitratā = purity, bandhutā = kinship)",
        "sutra_panini": "tasya bhāvastvatalau (5.1.119)",
        "sutra_hnv": "HNV Taddhita 4.61: strīliṅge bhāvārthe tal",
        "tika_exegesis": "Gopī Caraṇa Dāsa (Taddhitoddīpanī): Manifests the gentle, sheltering nature of the attribute."
    },
    "an": {
        "name": "Aṇ (अण् - Offspring / Patronymic / Relation)",
        "anubandhas": "a + ṇ (Triggers initial vowel vṛddhi via 7.2.117)",
        "category": "Apatyārthaka Taddhita (अपत्यार्थक / Lineage & Descendant)",
        "meaning": "son of / descendant of / relating to (e.g. vasudeva -> vāsudeva, pāṇḍu -> pāṇḍava)",
        "sutra_panini": "tasyāpatyam (4.1.92) & taddhiteṣvacāmādeḥ (7.2.117)",
        "sutra_hnv": "HNV Taddhita 4.4: apatyārthe aṇ āder vṛddhiḥ",
        "tika_exegesis": "Gopī Caraṇa Dāsa (Taddhitoddīpanī): Demonstrates divine descent (Vāsudeva = son of Vasudeva)."
    },
    "thak": {
        "name": "Ṭhak (ठक् - Pertaining to / Relational)",
        "anubandhas": "ṭh -> ika (7.3.50) + k (Triggers initial vṛddhi 7.2.118)",
        "category": "Śaiṣika Taddhita (शैषिक / Pertaining to / Practicing)",
        "meaning": "relating to / observant of (e.g. dharma -> dhārmika, veda -> vaidika)",
        "sutra_panini": "tena dīvyati khanati jayati jitam (4.4.2) & ṭhasyekaḥ (7.3.50)",
        "sutra_hnv": "HNV Taddhita 4.85: ṭha-saṅketasya ikādeśaḥ",
        "tika_exegesis": "Gopī Caraṇa Dāsa (Taddhitoddīpanī): Elevates the nominal base into a steadfast way of life (dhārmika)."
    },
    "mayat": {
        "name": "Mayaṭ (मयट् - Composed of / Full of)",
        "anubandhas": "m + a + y + a + ṭ -> maya",
        "category": "Vikārārthaka / Prācuryārthaka (विकार / प्राचुर्य - Abundance)",
        "meaning": "composed of / full of / transformation of (e.g. ānandamaya, cinmaya)",
        "sutra_panini": "tatprakṛtavacane mayaṭ (5.4.21) & mayaḍ vaitayoḥ (4.3.143)",
        "sutra_hnv": "HNV Taddhita 4.95: prācurye vikāre ca mayaṭ",
        "tika_exegesis": "Gopī Caraṇa Dāsa (Taddhitoddīpanī): Ānandamaya represents the Supreme Lord brimming with spiritual bliss."
    }
}


class KrdantaTaddhitaEngine:
    """
    Computes primary (Kṛt) and secondary (Taddhita) morphological derivatives
    with dual Pāṇini and Harināmāmṛta / Taddhitoddīpanī sūtra citations.
    """

    def derive_krdanta(self, root: str, affix_key: str, upasarga: Optional[str] = None) -> Dict[str, Any]:
        """
        Derives a Kṛdanta (primary verbal derivative) form from a Dhātu and Kṛt affix.
        """
        r = root.strip().lower()
        up = upasarga.strip().lower() if upasarga else None
        aff_raw = affix_key.strip().lower()

        # Normalize key
        key_map = {
            "ktva": "ktvā", "ktvā": "ktvā",
            "lyap": "lyap",
            "tumun": "tumun",
            "kta": "kta",
            "ktavatu": "ktavatu",
            "satr": "satr", "śatṛ": "satr", "shatr": "satr",
            "sanac": "sanac", "śānac": "sanac", "shanac": "sanac",
            "tavya": "tavya",
            "aniya": "aniya", "anīya": "aniya"
        }
        aff = key_map.get(aff_raw, aff_raw)

        if aff not in KRDANTA_AFFIXES:
            raise ValueError(f"Unknown Kṛdanta affix '{affix_key}'. Available: {list(key_map.keys())}")

        aff_info = KRDANTA_AFFIXES[aff]

        # Fetch root info from registry or fallback
        dhatu_info = DHATU_REGISTRY.get(r, (iast_to_devanagari(r), 'generic action', 'भ्वादि'))
        root_dev = dhatu_info[0]
        root_meaning = dhatu_info[1]
        root_gana = dhatu_info[2]

        # Compute phonological derivation
        intermediate_steps = []
        
        # Step 1: Base identification
        up_str = f"{up} + " if up else ""
        up_dev = f"{iast_to_devanagari(up)} + " if up else ""
        intermediate_steps.append({
            "step": 1,
            "stage": "Dhātu & Kṛt Affix Assignment (धातु-विधानम्)",
            "form": f"{up_str}{r} + {aff_info['name'].split()[0]}",
            "sutra": aff_info["sutra_panini"],
            "hnv": aff_info["sutra_hnv"],
            "desc": f"Root '{root_dev}' ({r}) is assigned the Kṛt affix '{aff_info['name']}' to denote {aff_info['category']}."
        })

        # Morphophonemic stem builder
        final_stem_iast, final_stem_dev = self._compute_krdanta_surface(r, aff, up)

        intermediate_steps.append({
            "step": 2,
            "stage": "Anubandha Lopa & Aṅga Saṃskāra (इत्-लोप एवं अङ्ग-कार्यम्)",
            "form": f"{final_stem_dev} ({final_stem_iast})",
            "sutra": "tasya lopaḥ (1.3.9) & guṇa/vṛddhi aṅga-kāryam",
            "hnv": "tasya saṅketa-harāmaḥ (HNV 2.2)",
            "desc": f"Anubandhas ({aff_info['anubandhas']}) are elided, executing root vowel strengthening/sandhi to yield '{final_stem_dev}'."
        })

        is_avyaya = "Avyaya" in aff_info["category"]

        return {
            "root_iast": r,
            "root_devanagari": root_dev,
            "root_meaning": root_meaning,
            "root_gana": root_gana,
            "upasarga": up,
            "affix_name": aff_info["name"],
            "affix_category": aff_info["category"],
            "semantic_meaning": aff_info["meaning"],
            "derived_stem_iast": final_stem_iast,
            "derived_stem_devanagari": final_stem_dev,
            "is_avyaya": is_avyaya,
            "sutra_panini": aff_info["sutra_panini"],
            "sutra_hnv": aff_info["sutra_hnv"],
            "tika_exegesis": aff_info["tika_exegesis"],
            "derivation_steps": intermediate_steps
        }

    def _compute_krdanta_surface(self, r: str, aff: str, up: Optional[str]) -> Tuple[str, str]:
        """Computes surface Kṛdanta word/stem."""
        # Special root exceptions
        prefix = up or ""

        if aff in ("ktva", "ktvā"):
            if prefix:
                # If prefix is present, ktva becomes lyap via 7.1.37!
                return self._compute_krdanta_surface(r, "lyap", up)
            if r == "kṛ": return "kṛtvā", "कृत्वा"
            if r == "gam": return "gatvā", "गत्वा"
            if r == "dṛś" or r == "paś": return "dṛṣṭvā", "दृष्ट्वा"
            if r == "sthā": return "sthitvā", "स्थित्वा"
            if r == "jñā": return "jñātvā", "ज्ञात्वा"
            if r == "bhū": return "bhūtvā", "भूत्वा"
            if r == "paṭh": return "paṭhitvā", "पठित्वा"
            if r == "likh": return "likhitvā", "लिखित्वा"
            if r == "vac": return "uktvā", "उक्त्वा"
            if r.endswith('i') or r.endswith('ī'): return f"{r[:-1]}itvā", iast_to_devanagari(f"{r[:-1]}itvā")
            return f"{r}itvā", iast_to_devanagari(f"{r}itvā")

        if aff == "lyap":
            p_iast = prefix if prefix else "sam"
            if r == "gam": res = f"{p_iast}etya" if p_iast.endswith('a') else f"{p_iast}gatya"
            elif r == "kṛ": res = f"{p_iast}kṛtya"
            elif r == "dṛś" or r == "paś": res = f"{p_iast}dṛśya"
            elif r == "bhū": res = f"{p_iast}bhūya"
            elif r == "sthā": res = f"{p_iast}sthāya"
            elif r == "jñā": res = f"{p_iast}jñāya"
            elif r == "nam": res = f"{p_iast}namya"
            else: res = f"{p_iast}{r}ya"
            return res, iast_to_devanagari(res)

        if aff == "tumun":
            if r == "kṛ": res = "kartum"
            elif r == "gam": res = "gantum"
            elif r == "dṛś" or r == "paś": res = "draṣṭum"
            elif r == "sthā": res = "sthātum"
            elif r == "bhū": res = "bhavitum"
            elif r == "jñā": res = "jñātum"
            elif r == "paṭh": res = "paṭhitum"
            elif r == "likh": res = "lekhitum"
            elif r == "vac": res = "vaktum"
            else: res = f"{r}itum"
            full = f"{prefix}{res}" if prefix else res
            return full, iast_to_devanagari(full)

        if aff == "kta":
            if r == "kṛ": res = "kṛta"
            elif r == "gam": res = "gata"
            elif r == "dṛś" or r == "paś": res = "dṛṣṭa"
            elif r == "sthā": res = "sthita"
            elif r == "bhū": res = "bhūta"
            elif r == "jñā": res = "jñāta"
            elif r == "paṭh": res = "paṭhita"
            elif r == "likh": res = "likhita"
            elif r == "vac": res = "ukta"
            else: res = f"{r}ta"
            full = f"{prefix}{res}" if prefix else res
            return full, iast_to_devanagari(full)

        if aff == "ktavatu":
            kta_stem, _ = self._compute_krdanta_surface(r, "kta", up)
            res = f"{kta_stem}vat"
            return res, iast_to_devanagari(res)

        if aff == "satr":
            if r == "kṛ": res = "kurvat"
            elif r == "gam": res = "gacchat"
            elif r == "dṛś" or r == "paś": res = "paśyat"
            elif r == "bhū": res = "bhavat"
            elif r == "sthā": res = "tiṣṭhat"
            elif r == "paṭh": res = "paṭhat"
            elif r == "likh": res = "likhat"
            elif r == "vac": res = "bruvat"
            else: res = f"{r}at"
            full = f"{prefix}{res}" if prefix else res
            return full, iast_to_devanagari(full)

        if aff == "sanac":
            if r == "kṛ": res = "kurvāṇa"
            elif r == "yudh": res = "yudhyamāna"
            elif r == "bhū": res = "bhavamāna"
            elif r == "vand": res = "vandamāna"
            else: res = f"{r}amāna"
            full = f"{prefix}{res}" if prefix else res
            return full, iast_to_devanagari(full)

        if aff == "tavya":
            if r == "kṛ": res = "kartavya"
            elif r == "gam": res = "gantavya"
            elif r == "dṛś" or r == "paś": res = "draṣṭavya"
            elif r == "bhū": res = "bhavitavya"
            elif r == "sthā": res = "sthātavya"
            elif r == "paṭh": res = "paṭhitavya"
            elif r == "vac": res = "vaktavya"
            else: res = f"{r}itavya"
            full = f"{prefix}{res}" if prefix else res
            return full, iast_to_devanagari(full)

        if aff == "aniya":
            if r == "kṛ": res = "karaṇīya"
            elif r == "gam": res = "gamanīya"
            elif r == "dṛś" or r == "paś": res = "darśanīya"
            elif r == "bhū": res = "bhavanīya"
            elif r == "sthā": res = "sthānīya"
            elif r == "smṛ": res = "smaraṇīya"
            elif r == "pūj": res = "pūjanīya"
            else: res = f"{r}anīya"
            full = f"{prefix}{res}" if prefix else res
            return full, iast_to_devanagari(full)

        return f"{r}{aff}", iast_to_devanagari(f"{r}{aff}")

    def derive_taddhita(self, stem: str, affix_key: str) -> Dict[str, Any]:
        """
        Derives a Taddhitānta (secondary nominal derivative) form from a Prātipadika and Taddhita affix.
        """
        st = stem.strip().lower()
        aff = affix_key.strip().lower()

        if aff not in TADDHITA_AFFIXES:
            raise ValueError(f"Unknown Taddhita affix '{affix_key}'. Available: {list(TADDHITA_AFFIXES.keys())}")

        aff_info = TADDHITA_AFFIXES[aff]
        stem_dev = iast_to_devanagari(st)

        # Compute surface derivative
        derived_stem_iast, derived_stem_dev = self._compute_taddhita_surface(st, aff)

        intermediate_steps = [
            {
                "step": 1,
                "stage": "Prātipadika & Taddhita Suffixation (प्रातिपदिक-तद्धित-विधानम्)",
                "form": f"{stem_dev} + {aff_info['name'].split()[0]}",
                "sutra": aff_info["sutra_panini"],
                "hnv": aff_info["sutra_hnv"],
                "desc": f"Base '{stem_dev}' ({st}) takes secondary affix '{aff_info['name']}' under jurisdiction 4.1.76."
            },
            {
                "step": 2,
                "stage": "Vṛddhi / Aṅga Mutation (वृद्धि एवं अङ्ग-संस्कारः)",
                "form": f"{derived_stem_dev} ({derived_stem_iast})",
                "sutra": "taddhiteṣvacāmādeḥ (7.2.117) / ṭhasyekaḥ (7.3.50)",
                "hnv": "taddhitoddīpanī paribhāṣā",
                "desc": f"Operational variables fire initial vowel strengthening or suffix substitution to yield '{derived_stem_dev}'."
            }
        ]

        return {
            "base_stem_iast": st,
            "base_stem_devanagari": stem_dev,
            "affix_name": aff_info["name"],
            "affix_category": aff_info["category"],
            "semantic_meaning": aff_info["meaning"],
            "derived_stem_iast": derived_stem_iast,
            "derived_stem_devanagari": derived_stem_dev,
            "sutra_panini": aff_info["sutra_panini"],
            "sutra_hnv": aff_info["sutra_hnv"],
            "tika_exegesis": aff_info["tika_exegesis"],
            "derivation_steps": intermediate_steps
        }

    def _compute_taddhita_surface(self, st: str, aff: str) -> Tuple[str, str]:
        """Computes surface Taddhita derivative stem."""
        clean_st = st.rstrip('aāiīuū')

        if aff == "matup":
            # 8.2.9: If stem ends in 'a/ā' or m-upadhā, matup becomes vatup
            if st.endswith(('a', 'ā')):
                res = f"{st}vat"
            else:
                res = f"{st}mat"
            return res, iast_to_devanagari(res)

        if aff == "inith":
            # 5.2.115: ata iniṭhanau (a-stem drops 'a' and adds 'in')
            res = f"{clean_st}in"
            return res, iast_to_devanagari(res)

        if aff == "tva":
            res = f"{st}tva"
            return res, iast_to_devanagari(res)

        if aff == "tal":
            res = f"{st}tā"
            return res, iast_to_devanagari(res)

        if aff == "an":
            # Initial vowel vṛddhi via 7.2.117
            v_iast = self._apply_adi_vriddhi(st)
            res = f"{v_iast}a" if not v_iast.endswith('a') else v_iast
            return res, iast_to_devanagari(res)

        if aff == "thak":
            # Initial vowel vṛddhi + ika via 7.3.50
            v_iast = self._apply_adi_vriddhi(clean_st)
            res = f"{v_iast}ika"
            return res, iast_to_devanagari(res)

        if aff == "mayat":
            res = f"{st}maya"
            return res, iast_to_devanagari(res)

        return f"{st}{aff}", iast_to_devanagari(f"{st}{aff}")

    def _apply_adi_vriddhi(self, word: str) -> str:
        """Applies initial vowel Vṛddhi (आदिवृद्धि 7.2.117)."""
        w = word.lower()
        if w.startswith('a'): return 'ā' + w[1:]
        if w.startswith('i') or w.startswith('e'): return 'ai' + w[1:]
        if w.startswith('u') or w.startswith('o'): return 'au' + w[1:]
        if w.startswith('ṛ'): return 'ār' + w[1:]

        # Check second letter if word starts with consonant
        m = re.match(r'^([^aeiouṛāīūaiou]+)(a|i|u|ṛ|e|o)(.*)$', w)
        if m:
            cons, vowel, rest = m.groups()
            vriddhi_map = {'a': 'ā', 'i': 'ai', 'u': 'au', 'ṛ': 'ār', 'e': 'ai', 'o': 'au'}
            new_v = vriddhi_map.get(vowel, vowel)
            return cons + new_v + rest

        return w
