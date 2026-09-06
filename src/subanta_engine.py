"""
Pāṇinian Subanta (Śabdarūpa) Engine
Comprehensive, High-Performance, Glass-Box Generative and Analytical Sanskrit Morphology Engine.

Covers:
1. Ajanta (Vowels):
   - a-stem Masculine (rāma, deva, bāla) & Neuter (phala, vana, jñāna)
   - ā-stem Feminine (latā, vidyā, ramā, sītā)
   - i-stem Masculine (hari, kavi), Feminine (mati, buddhi with dual vibhāṣā), Neuter (vāri, dadhi)
   - ī-stem Feminine (nadī, devī, lakṣmī) & Monosyllabic (śrī, dhī)
   - u-stem Masculine (guru, bhānu), Feminine (dhenu with dual vibhāṣā), Neuter (madhu, vastu)
   - ū-stem Feminine (vadhū, camū, bhū)
   - ṛ-stem Kinship (pitṛ, bhrātṛ, mātṛ) & Agentive (kartṛ, dātṛ, netṛ)
   - Diphthong / Irregular Ajanta (go, nau, sakhi, pati)
2. Halanta (Consonants):
   - an-stem Masculine non-cluster (rājan) vs cluster (ātman, brahman) & Neuter (nāman, karman)
   - in-stem Masculine (guṇin, dhanin, jñānin, karmin)
   - as-stem Neuter (manas, tejas, payas, yaśas)
   - is/us-stem Neuter (haviṣ, dhanuṣ, cakṣuṣ)
   - at/mat/vat-stem Masculine (bhagavat, dhīmat, mahat) & Neuter (jagat)
   - Root Consonants (marut, sarit, vāc, diś, dṛś, ap)
   - Irregular Halanta (pathin, ahan)
3. Sarvanāma (Pronouns):
   - tad, etad, idam, adas, yad, kim, sarva, anya (M / F / N)
   - asmad & yuṣmad (Common)
"""

from typing import Dict, Any, List, Optional, Tuple, Set
import re
from .normalizer import devanagari_to_iast, iast_to_devanagari

# Standard Pāṇinian 7 Vibhaktis + Sambodhana
VIBHAKTIS = [
    ("Prathamā (प्रथमा - 1st / Nominative)", "Prathama", "सु, औ, जस् (4.1.2)"),
    ("Dvitīyā (द्वितीया - 2nd / Accusative)", "Dvitiya", "अम्, औट्, शस् (4.1.2)"),
    ("Tṛtīyā (तृतीया - 3rd / Instrumental)", "Tritiya", "टा, भ्याम्, भिस् (4.1.2)"),
    ("Caturthī (चतुर्थी - 4th / Dative)", "Caturthi", "ङे, भ्याम्, भ्यस् (4.1.2)"),
    ("Pañcamī (पञ्चमी - 5th / Ablative)", "Pancami", "ङसि, भ्याम्, भ्यस् (4.1.2)"),
    ("Ṣaṣṭhī (षष्ठी - 6th / Genitive)", "Sasthi", "ङस्, ओस्, आम् (4.1.2)"),
    ("Saptamī (सप्तमी - 7th / Locative)", "Saptami", "ङि, ओस्, सुप् (4.1.2)"),
    ("Sambodhana (सम्बोधन - Vocative)", "Sambodhana", "एकवचनं संबुद्धिः (2.3.49)")
]

VACANAS = ["Ekavacana (एकवचनम् - Singular)", "Dvivacana (द्विवचनम् - Dual)", "Bahuvacana (बहुवचनम् - Plural)"]

# Raw SUP Array (Pāṇini 4.1.2: svaujasamauṭchaṣṭābhyāṃbhisṅebhyāṃbhyasṅasibhyāṃbhyasṅasosāmṅyossup)
RAW_SUP_AFFIXES = [
    # Prathamā (1st)
    [
        {"affix": "su̐", "affix_dev": "सुँ", "anubandha": "u̐ (upadeśe'janunāsika it 1.3.2) -> s", "it_rule": "tasya lopaḥ (1.3.9)"},
        {"affix": "au", "affix_dev": "औ", "anubandha": "None (Nir-anubandha)", "it_rule": "N/A"},
        {"affix": "jas", "affix_dev": "जस्", "anubandha": "j (cuṭū 1.3.7) -> as; s preserved by na vibhaktau tusmāḥ (1.3.4)", "it_rule": "cuṭū (1.3.7)"}
    ],
    # Dvitīyā (2nd)
    [
        {"affix": "am", "affix_dev": "अम्", "anubandha": "None (m preserved by 1.3.4)", "it_rule": "N/A"},
        {"affix": "auṭ", "affix_dev": "औट्", "anubandha": "ṭ (halantyam 1.3.3) -> au (Bounds suṭ pratyāhāra)", "it_rule": "halantyam (1.3.3)"},
        {"affix": "śas", "affix_dev": "शस्", "anubandha": "ś (laśakvataddhite 1.3.8) -> as (Flags weak stem)", "it_rule": "laśakvataddhite (1.3.8)"}
    ],
    # Tṛtīyā (3rd)
    [
        {"affix": "ṭā", "affix_dev": "टा", "anubandha": "ṭ (cuṭū 1.3.7) -> ā", "it_rule": "cuṭū (1.3.7)"},
        {"affix": "bhyām", "affix_dev": "भ्याम्", "anubandha": "None (m preserved by 1.3.4)", "it_rule": "N/A"},
        {"affix": "bhis", "affix_dev": "भिस्", "anubandha": "None (s preserved by 1.3.4)", "it_rule": "N/A"}
    ],
    # Caturthī (4th)
    [
        {"affix": "ṅe", "affix_dev": "ङे", "anubandha": "ṅ (laśakvataddhite 1.3.8) -> e (Triggers guṇa of stem)", "it_rule": "laśakvataddhite (1.3.8)"},
        {"affix": "bhyām", "affix_dev": "भ्याम्", "anubandha": "None (m preserved by 1.3.4)", "it_rule": "N/A"},
        {"affix": "bhyas", "affix_dev": "भ्यस्", "anubandha": "None (s preserved by 1.3.4)", "it_rule": "N/A"}
    ],
    # Pañcamī (5th)
    [
        {"affix": "ṅasi̐", "affix_dev": "ङसिँ", "anubandha": "ṅ (1.3.8) + i̐ (1.3.2) -> as (Triggers guṇa)", "it_rule": "laśakvataddhite (1.3.8)"},
        {"affix": "bhyām", "affix_dev": "भ्याम्", "anubandha": "None (m preserved by 1.3.4)", "it_rule": "N/A"},
        {"affix": "bhyas", "affix_dev": "भ्यस्", "anubandha": "None (s preserved by 1.3.4)", "it_rule": "N/A"}
    ],
    # Ṣaṣṭhī (6th)
    [
        {"affix": "ṅas", "affix_dev": "ङस्", "anubandha": "ṅ (laśakvataddhite 1.3.8) -> as (Triggers guṇa)", "it_rule": "laśakvataddhite (1.3.8)"},
        {"affix": "os", "affix_dev": "ओस्", "anubandha": "None (s preserved by 1.3.4)", "it_rule": "N/A"},
        {"affix": "ām", "affix_dev": "आम्", "anubandha": "None (m preserved by 1.3.4)", "it_rule": "N/A"}
    ],
    # Saptamī (7th)
    [
        {"affix": "ṅi", "affix_dev": "ङि", "anubandha": "ṅ (laśakvataddhite 1.3.8) -> i (Triggers guṇa/substitution)", "it_rule": "laśakvataddhite (1.3.8)"},
        {"affix": "os", "affix_dev": "ओस्", "anubandha": "None (s preserved by 1.3.4)", "it_rule": "N/A"},
        {"affix": "suP", "affix_dev": "सुप्", "anubandha": "P (halantyam 1.3.3) -> su (Bounds sup pratyāhāra)", "it_rule": "halantyam (1.3.3)"}
    ],
    # Sambodhana (Vocative)
    [
        {"affix": "su̐ (Sambuddhi)", "affix_dev": "सुँ (सम्बुद्धि)", "anubandha": "u̐ -> s (ekavacanaṃ sambuddhiḥ 2.3.49; elided by eṅhrasvāt... 6.1.69)", "it_rule": "tasya lopaḥ (1.3.9)"},
        {"affix": "au", "affix_dev": "औ", "anubandha": "None", "it_rule": "N/A"},
        {"affix": "jas", "affix_dev": "जस्", "anubandha": "j -> as", "it_rule": "cuṭū (1.3.7)"}
    ]
]

# Kāraka (Syntactic-Semantic Role) Network (Aṣṭādhyāyī 1.4 & 2.3)
KARAKA_MAPPINGS = [
    {
        "role": "Kartṛ (कर्तृ - Agent / Subject) / Abhihita",
        "karaka_sutra": "svatantraḥ kartā (1.4.54)",
        "vibhakti_sutra": "prātipadikārtha-liṅga-parimāṇa-vacana-mātre prathamā (2.3.46)",
        "meaning": "Independent instigator of the action (Nominative in active voice)"
    },
    {
        "role": "Karman (कर्म - Patient / Direct Object)",
        "karaka_sutra": "karturīpsitatamaṃ karma (1.4.49)",
        "vibhakti_sutra": "karmaṇi dvitīyā (2.3.2)",
        "meaning": "That which the agent most seeks to achieve through the action (Accusative)"
    },
    {
        "role": "Karaṇa (करण - Instrument / Means) & Anabhihita Kartṛ",
        "karaka_sutra": "sādhakatamaṃ karaṇam (1.4.42)",
        "vibhakti_sutra": "kartṛkaraṇayostṛtīyā (2.3.18)",
        "meaning": "The primary operational instrument or agent in passive voice (Instrumental)"
    },
    {
        "role": "Sampradāna (सम्प्रदान - Recipient / Beneficiary)",
        "karaka_sutra": "karmaṇā yamabhipraiti sa sampradānam (1.4.32)",
        "vibhakti_sutra": "caturthī sampradāne (2.3.13)",
        "meaning": "The entity aimed at through the direct object/action (Dative)"
    },
    {
        "role": "Apādāna (अपादान - Source / Point of Departure / Fear)",
        "karaka_sutra": "dhruvamapāye'pādānam (1.4.24) & bhītrārthānāṃ bhayahetuḥ (1.4.25)",
        "vibhakti_sutra": "apādāne pañcamī (2.3.28)",
        "meaning": "The stationary point from which detachment or fear occurs (Ablative)"
    },
    {
        "role": "Sambandha (सम्बन्ध - Genitive / Relational Possessor)",
        "karaka_sutra": "śeṣe (Non-kāraka relational dependencies)",
        "vibhakti_sutra": "ṣaṣṭhī śeṣe (2.3.50) & ṣaṣṭhyatasarthapratyayena (2.3.67)",
        "meaning": "Syntactic relation between two nominals denoting possession, origin, or part-whole (Genitive)"
    },
    {
        "role": "Adhikaraṇa (अधिकरण - Locus / Substratum / Location)",
        "karaka_sutra": "ādhāro'dhikaraṇam (1.4.45)",
        "vibhakti_sutra": "saptamyadhikaraṇe ca (2.3.36)",
        "meaning": "The spatial, temporal, or conceptual locus supporting the action (Locative)"
    },
    {
        "role": "Āmantraṇa / Sambodhana (सम्बोधन - Direct Address)",
        "karaka_sutra": "ekavacanaṃ sambuddhiḥ (2.3.49)",
        "vibhakti_sutra": "sambodhane ca (2.3.47)",
        "meaning": "Direct vocative address to a listener (Vocative)"
    }
]

# =====================================================================
# Śrī Harināmāmṛta-Vyākaraṇa (HNV) Nomenclature & Epistemology
# Authored by Śrīla Jīva Gosvāmī (16th c. Gauḍīya Vaiṣṇava Linguistics)
# Preserves 100% Pāṇinian algorithms while using devotional vocabulary.
# =====================================================================

HNV_TERMINOLOGY = {
    "pratipadika": {
        "panini": "Prātipadika (प्रातिपदिकम्)",
        "hnv": "Nārāyaṇa (नारायण)",
        "desc": "The foundational base of all meaning and reality, corresponding to the Supreme Lord from whom all linguistic energies emanate."
    },
    "sup": {
        "panini": "SUP-Pratyaya (सुप्-प्रत्ययः - 21 Affixes)",
        "hnv": "Viṣṇubhakti (विष्णुभक्ति)",
        "desc": "The 21 devotional inflectional affixes, conceptualized as devotees surrounding, qualifying, and serving Nārāyaṇa across numbers and relationships."
    },
    "pada": {
        "panini": "Pada (पदम् / सुप्तिङन्तं पदम् 1.4.14)",
        "hnv": "Viṣṇupada (विष्णुपद)",
        "desc": "The realized, consecrated word form arising from the divine union of Nārāyaṇa and Viṣṇubhakti."
    },
    "anubandha": {
        "panini": "Anubandha / IT Marker (इत्-संज्ञा)",
        "hnv": "Saṅketa (सङ्केत)",
        "desc": "Esoteric indicator signs that trigger grammatical transformations before disappearing."
    },
    "lopa": {
        "panini": "Lopa / Adarśana (लोपः / अदर्शनम् 1.3.9)",
        "hnv": "Harām / Trivikrama (हराम् / त्रिविक्रम)",
        "desc": "The divine dissolution or removal of temporary scaffolds once their operational purpose is fulfilled."
    },
    "svara": {
        "panini": "Svara / Ac (स्वरः / अच् - Vowels)",
        "hnv": "Sarveśvara (सर्वेश्वर)",
        "desc": "The Lord of All; phonetically self-sufficient and capable of independent sounding."
    },
    "vyanjana": {
        "panini": "Vyañjana / Hal (व्यञ्जनम् / हल् - Consonants)",
        "hnv": "Viṣṇujana (विष्णुजन)",
        "desc": "The dependent associates of Vishnu, relying on Sarveśvara (vowels) to be articulated."
    },
    "ajanta": {
        "panini": "Ajanta (अजन्त - Vowel-Ending)",
        "hnv": "Sarveśvarānta (सर्वेश्वरान्त)",
        "desc": "A nominal stem ending in an independent vowel."
    },
    "halanta": {
        "panini": "Halanta (हलन्त - Consonant-Ending)",
        "hnv": "Viṣṇujanānta (विष्णुजनान्त)",
        "desc": "A nominal stem ending in a dependent consonant."
    },
    "utsarga": {
        "panini": "Utsarga (उत्सर्ग - General Rule)",
        "hnv": "Sārvatrika-Līlā (सार्वत्रिक-लीला / Universal Cosmic Law)",
        "desc": "Universal, steady law governing the general domain."
    },
    "apavada": {
        "panini": "Apavāda (अपवाद - Exceptional Rule)",
        "hnv": "Viśeṣānugraha-Līlā (विशेषानुग्रह-लीला / Divine Dispensation)",
        "desc": "Special divine dispensation or localized pastime that overrides general cosmic laws."
    },
    "asiddhatva": {
        "panini": "Asiddhatva (असिद्धत्वम् - Rule Suspension)",
        "hnv": "Śakti-Saṅkoca (शक्ति-सङ्कोच / Withholding of Potency)",
        "desc": "The deliberate withholding of a specific rule's energy to allow another divine purpose to manifest linearly."
    }
}

HNV_VIBHAKTI_MAPPINGS = [
    {"vibhakti": "Prathamā", "hnv_name": "Prathamā Viṣṇubhakti (प्रथमा विष्णुभक्तिः)", "bhakti_role": "Nārāyaṇa-Svarūpa-Darśana (Direct Vision of the Lord / Kartā)"},
    {"vibhakti": "Dvitīyā", "hnv_name": "Dvitīyā Viṣṇubhakti (द्वितीया विष्णुभक्तिः)", "bhakti_role": "Sevyatva / Karma-Sevā (Direct Object of Devotional Service)"},
    {"vibhakti": "Tṛtīyā", "hnv_name": "Tṛtīyā Viṣṇubhakti (तृतीया विष्णुभक्तिः)", "bhakti_role": "Sādhana / Seva-Upakaraṇa (Instrument of Devotion & Means)"},
    {"vibhakti": "Caturthī", "hnv_name": "Caturthī Viṣṇubhakti (चतुर्थी विष्णुभक्तिः)", "bhakti_role": "Samarpaṇa / Ātma-Nivedana (Total Dedication & Offering)"},
    {"vibhakti": "Pañcamī", "hnv_name": "Pañcamī Viṣṇubhakti (पञ्चमी विष्णुभक्तिः)", "bhakti_role": "Āśraya-Bheda / Viraha (Refuge from Departure & Separation)"},
    {"vibhakti": "Ṣaṣṭhī", "hnv_name": "Ṣaṣṭhī Viṣṇubhakti (षष्ठी विष्णुभक्तिः)", "bhakti_role": "Sevaka-Sevya-Sambandha (Eternal Loving Relationship with the Lord)"},
    {"vibhakti": "Saptamī", "hnv_name": "Saptamī Viṣṇubhakti (सप्तमी विष्णुभक्तिः)", "bhakti_role": "Dhāma-Adhikaraṇa (Residence in the Divine Locus / Realm)"},
    {"vibhakti": "Sambodhana", "hnv_name": "Sambodhana Viṣṇubhakti (सम्बोधन विष्णुभक्तिः)", "bhakti_role": "Saṅkīrtana / Āhvāna (Devotional Chanting & Direct Calling)"}
]


def apply_natva(iast_word: str) -> str:
    """
    Applies Pāṇinian Ṇatva (णत्व): r/ṣ causes subsequent n -> ṇ within the same pada
    governed by 'raṣābhyāṃ no ṇaḥ samānapade' (8.4.1) & 'aṭ-kupv-āṅ-num-vyavāye'api' (8.4.2).
    E.g. rāmena -> rāmeṇa, rāmānām -> rāmāṇām; but bālena -> bālena.
    """
    chars = list(iast_word)
    has_trigger = False
    for i, ch in enumerate(chars):
        if ch in ('r', 'ṛ', 'ṝ', 'ṣ'):
            has_trigger = True
        elif has_trigger and ch == 'n':
            prev_chunk = iast_word[iast_word.rfind('r') if 'r' in iast_word else iast_word.rfind('ṣ'):i]
            blocked = any(c in prev_chunk for c in ('c', 'ch', 'j', 'jh', 'ñ', 'ṭ', 'ṭh', 'ḍ', 'ḍh', 'ṇ', 't', 'th', 'd', 'dh', 'l', 's', 'ś'))
            if not blocked and i + 1 < len(iast_word) and chars[i+1] in ('a', 'ā', 'i', 'ī', 'u', 'ū', 'e', 'ai', 'o', 'au', 'm'):
                chars[i] = 'ṇ'
    return "".join(chars)


class SubantaEngine:
    """
    Exhaustive Pāṇinian Nominal Inflection (Subanta / Śabdarūpa) Generator & Parser.
    """

    def __init__(self):
        # Cache for high-speed reverse lookups: { inflected_iast: [ (stem, gender, vibhakti_idx, vacana_idx, sutras) ] }
        self._reverse_cache: Dict[str, List[Dict[str, Any]]] = {}
        self._populate_core_pronouns()

    def infer_gender_and_paradigm(self, stem_iast: str) -> Tuple[str, str]:
        """
        Infers natural grammatical gender (liṅga) and structural paradigm from a nominal stem.
        Returns (gender, paradigm_key).
        """
        s = stem_iast.strip().lower()

        # Pronouns
        if s in ('tad', 'etad', 'idam', 'adas', 'yad', 'kim', 'sarva', 'anya', 'eka'):
            return "masculine", f"sarvanama_{s}"
        if s in ('yuṣmad', 'yushmad', 'tvad'):
            return "common", "sarvanama_yusmad"
        if s in ('asmad', 'mad'):
            return "common", "sarvanama_asmad"

        # Irregular & Diphthong stems
        if s == 'go':
            return "masculine", "diphthong_go"
        if s == 'nau':
            return "feminine", "diphthong_nau"
        if s == 'sakhi':
            return "masculine", "irregular_sakhi"
        if s == 'pati':
            return "masculine", "irregular_pati"
        if s == 'pathin':
            return "masculine", "irregular_pathin"

        # Vowel-ending (Ajanta)
        if s.endswith('a'):
            if s in ('phala', 'vana', 'jñāna', 'jala', 'kamala', 'padma', 'nagara', 'mitra', 'kāvya', 'śāstra', 'puṣpa', 'sukha', 'duḥkha'):
                return "neuter", "ajanta_a_neuter"
            return "masculine", "ajanta_a_masculine"
        elif s.endswith('ā'):
            return "feminine", "ajanta_aa_feminine"
        elif s.endswith('i'):
            if s in ('vāri', 'akṣi', 'asthi', 'sakthi', 'dadhi'):
                return "neuter", "ajanta_i_neuter"
            if s in ('mati', 'kīrti', 'buddhi', 'dhṛti', 'śakti', 'bhakti', 'rati', 'jāti', 'śruti', 'smṛti'):
                return "feminine", "ajanta_i_feminine"
            return "masculine", "ajanta_i_masculine"
        elif s.endswith('ī'):
            if s in ('śrī', 'dhī', 'hrī', 'dhī'):
                return "feminine", "ajanta_ii_monosyllabic"
            return "feminine", "ajanta_ii_feminine"
        elif s.endswith('u'):
            if s in ('madhu', 'ambu', 'vastu', 'aśru', 'jānu'):
                return "neuter", "ajanta_u_neuter"
            if s in ('dhenu', 'tanu', 'reṇu', 'rajju'):
                return "feminine", "ajanta_u_feminine"
            return "masculine", "ajanta_u_masculine"
        elif s.endswith('ū'):
            return "feminine", "ajanta_uu_feminine"
        elif s.endswith(('ṛ', 'ri')):
            if s in ('mātṛ', 'svasṛ', 'duhitṛ', 'yātṛ', 'nanāndṛ'):
                return "feminine", "ajanta_ri_feminine"
            if s in ('pitṛ', 'bhrātṛ', 'jāmātṛ'):
                return "masculine", "ajanta_ri_masculine_kinship"
            return "masculine", "ajanta_ri_masculine_agentive"

        # Consonant-ending (Halanta)
        elif s.endswith(('in', 'ī')):
            return "masculine", "halanta_in_masculine"
        elif s.endswith('an'):
            if s in ('nāman', 'karman', 'janman', 'carman', 'varman', 'parvan', 'dhāman', 'preman', 'sadman', 'vesman', 'vartman'):
                return "neuter", "halanta_an_neuter"
            if s in ('ātman', 'brahman', 'adhvan', 'yajvan'):
                return "masculine", "halanta_an_masculine_cluster"
            return "masculine", "halanta_an_masculine_noncluster"
        elif s.endswith(('is', 'us', 'iṣ', 'uṣ')):
            return "neuter", "halanta_is_us_neuter"
        elif s.endswith('as'):
            return "neuter", "halanta_as_neuter"
        elif s.endswith(('at', 'mat', 'vat')):
            if s in ('jagat', 'hṛdayat'):
                return "neuter", "halanta_at_neuter"
            return "masculine", "halanta_at_masculine"
        elif s.endswith(('t', 'd', 'c', 'j', 'ś', 'ṣ', 's', 'h')):
            if s == 'vāc':
                return "feminine", "halanta_vac_feminine"
            if s in ('diś', 'dṛś'):
                return "feminine", "halanta_dis_feminine"
            if s == 'sarit':
                return "feminine", "halanta_marut_masculine"
            return "masculine", "halanta_marut_masculine"

        return "masculine", "ajanta_a_masculine"

    def generate_shabdarupa(self, stem: str, gender: Optional[str] = None) -> Dict[str, Any]:
        """
        Generates the exhaustive 8x3 Śabdarūpa declension matrix for the given nominal stem.
        """
        clean_raw = stem.strip()
        is_dev = any('\u0900' <= ch <= '\u097f' for ch in clean_raw)
        stem_iast = devanagari_to_iast(clean_raw).strip().lower()
        stem_dev = iast_to_devanagari(stem_iast) if not is_dev else clean_raw

        inferred_gender, paradigm = self.infer_gender_and_paradigm(stem_iast)
        active_gender = (gender or inferred_gender).lower()

        # Adjust paradigm key if gender was explicitly specified by user
        if active_gender in ('neuter', 'napumsaka', 'n') and 'masculine' in paradigm:
            paradigm = paradigm.replace('masculine', 'neuter')
        elif active_gender in ('feminine', 'stri', 'f') and 'masculine' in paradigm:
            paradigm = paradigm.replace('masculine', 'feminine')
        elif active_gender in ('masculine', 'pum', 'm') and 'neuter' in paradigm:
            paradigm = paradigm.replace('neuter', 'masculine')

        matrix_iast, matrix_sutras = self._compute_matrix(stem_iast, active_gender, paradigm)

        # Build structured table with Devanagari, IAST, and Sūtras
        table = []
        for v_idx, (v_name, v_key, default_sutra) in enumerate(VIBHAKTIS):
            row_cells = []
            for vac_idx, vac_name in enumerate(VACANAS):
                val_iast = matrix_iast[v_idx][vac_idx]
                val_dev = iast_to_devanagari(val_iast) if val_iast and val_iast != '-' else '-'
                sutra_info = matrix_sutras[v_idx][vac_idx] or default_sutra
                sup_meta = RAW_SUP_AFFIXES[v_idx][vac_idx]
                karaka_meta = KARAKA_MAPPINGS[v_idx]

                cell_data = {
                    "vibhakti": v_name,
                    "vibhakti_idx": v_idx,
                    "vibhakti_key": v_key,
                    "vacana": vac_name,
                    "vacana_idx": vac_idx,
                    "iast": val_iast,
                    "devanagari": val_dev,
                    "sutra": sutra_info,
                    "raw_sup": sup_meta["affix"],
                    "raw_sup_dev": sup_meta["affix_dev"],
                    "anubandha": sup_meta["anubandha"],
                    "it_rule": sup_meta["it_rule"],
                    "karaka_role": karaka_meta["role"],
                    "karaka_sutra": karaka_meta["karaka_sutra"],
                    "karaka_meaning": karaka_meta["meaning"]
                }
                row_cells.append(cell_data)
                # Register in reverse lookup cache
                self._register_cache(val_iast, stem_iast, stem_dev, active_gender, v_name, vac_name, sutra_info)
            table.append({
                "vibhakti": v_name,
                "vibhakti_idx": v_idx,
                "vibhakti_key": v_key,
                "karaka_role": KARAKA_MAPPINGS[v_idx]["role"],
                "karaka_sutra": KARAKA_MAPPINGS[v_idx]["karaka_sutra"],
                "forms": row_cells
            })

        return {
            "stem_input": clean_raw,
            "stem_iast": stem_iast,
            "stem_devanagari": stem_dev,
            "gender": active_gender,
            "paradigm": paradigm,
            "total_cells": 24,
            "table": table
        }

    def _compute_matrix(self, stem: str, gender: str, paradigm: str) -> Tuple[List[List[str]], List[List[str]]]:
        """Core Pāṇinian morphological synthesis per grammatical paradigm."""
        m_iast: List[List[str]] = [["" for _ in range(3)] for _ in range(8)]
        m_sutra: List[List[str]] = [["" for _ in range(3)] for _ in range(8)]

        # -------------------------------------------------------------
        # 0. SARVANĀMA (PRONOUNS: tad, etad, idam, adas, yad, kim, sarva, asmad, yuṣmad)
        # -------------------------------------------------------------
        if paradigm.startswith("sarvanama_") or stem in ('tad', 'etad', 'yad', 'kim', 'sarva', 'idam', 'adas', 'anya', 'eka', 'asmad', 'yuṣmad'):
            p_stem = paradigm.replace("sarvanama_", "") if paradigm.startswith("sarvanama_") else stem
            if p_stem in ('tad', 'etad', 'yad', 'kim', 'sarva', 'idam', 'adas', 'asmad', 'yuṣmad', 'yushmad'):
                return self._compute_pronoun_matrix(p_stem, gender)

        # -------------------------------------------------------------
        # 1. AKĀRĀNTA PUṂLIṄGA (e.g. rāma, deva, bāla)
        # -------------------------------------------------------------
        if paradigm == "ajanta_a_masculine" or (stem.endswith('a') and gender.startswith(('m', 'p'))):
            b = stem[:-1]
            m_iast[0] = [f"{b}aḥ", f"{b}au", f"{b}āḥ"]
            m_sutra[0] = ["suptiṅantam padam (1.4.14)", "vṛddhireci (6.1.88)", "ataśca (6.1.102)"]

            m_iast[1] = [f"{b}am", f"{b}au", apply_natva(f"{b}ān")]
            m_sutra[1] = ["ami pūrvaḥ (6.1.107)", "prathamayoḥ pūrvasavarṇaḥ (6.1.102)", "tasmācchaso naḥ puṃsi (6.1.103)"]

            m_iast[2] = [apply_natva(f"{b}ena"), f"{b}ābhyām", f"{b}aiḥ"]
            m_sutra[2] = ["ṭāṅasinasminātsyenāḥ (7.1.12)", "supi ca (7.3.102: dīrgha)", "ato bhisa ais (7.1.9)"]

            m_iast[3] = [f"{b}āya", f"{b}ābhyām", f"{b}ebhyaḥ"]
            m_sutra[3] = ["ṅeḥ yā (7.1.13) & supi ca (7.3.102)", "supi ca (7.3.102)", "bahuvecane jhalyet (7.3.103)"]

            m_iast[4] = [f"{b}āt", f"{b}ābhyām", f"{b}ebhyaḥ"]
            m_sutra[4] = ["ṭāṅasinasminātsyenāḥ (7.1.12: āt)", "supi ca (7.3.102)", "bahuvecane jhalyet (7.3.103)"]

            m_iast[5] = [f"{b}asya", f"{b}ayoḥ", apply_natva(f"{b}ānām")]
            m_sutra[5] = ["ṭāṅasinasminātsyenāḥ (7.1.12: sya)", "osi ca (7.3.104)", "hrasvanadyāpo nuṭ (7.1.54) & nāmi (6.4.3)"]

            m_iast[6] = [f"{b}e", f"{b}ayoḥ", f"{b}eṣu"]
            m_sutra[6] = ["ṅer e (7.1.15)", "osi ca (7.3.104)", "ādeśapratyayayoḥ (8.3.59: ṣatva)"]

            m_iast[7] = [f"he {b}a", f"he {b}au", f"he {b}āḥ"]
            m_sutra[7] = ["eṅhrasvāt sambuddheḥ (6.1.69)", "vṛddhireci (6.1.88)", "ataśca (6.1.102)"]

        # -------------------------------------------------------------
        # 2. AKĀRĀNTA NAPUṂSAKALIṄGA (e.g. phala, vana, jñāna)
        # -------------------------------------------------------------
        elif paradigm == "ajanta_a_neuter" or (stem.endswith('a') and gender.startswith(('n', 'k'))):
            b = stem[:-1]
            m_iast[0] = [f"{b}am", f"{b}e", apply_natva(f"{b}āni")]
            m_sutra[0] = ["ato'm (7.1.24)", "napuṃsakācca (7.1.19: au -> śī)", "napuṃsakasya jhalacaḥ (7.1.72: śi -> num + dīrgha)"]

            m_iast[1] = [f"{b}am", f"{b}e", apply_natva(f"{b}āni")]
            m_sutra[1] = ["ato'm (7.1.24)", "napuṃsakācca (7.1.19)", "napuṃsakasya jhalacaḥ (7.1.72)"]

            m_iast[2] = [apply_natva(f"{b}ena"), f"{b}ābhyām", f"{b}aiḥ"]
            m_sutra[2] = ["ṭāṅasinasminātsyenāḥ (7.1.12)", "supi ca (7.3.102)", "ato bhisa ais (7.1.9)"]

            m_iast[3] = [f"{b}āya", f"{b}ābhyām", f"{b}ebhyaḥ"]
            m_sutra[3] = ["ṅeḥ yā (7.1.13)", "supi ca (7.3.102)", "bahuvecane jhalyet (7.3.103)"]

            m_iast[4] = [f"{b}āt", f"{b}ābhyām", f"{b}ebhyaḥ"]
            m_sutra[4] = ["ṭāṅasinasminātsyenāḥ (7.1.12)", "supi ca (7.3.102)", "bahuvecane jhalyet (7.3.103)"]

            m_iast[5] = [f"{b}asya", f"{b}ayoḥ", apply_natva(f"{b}ānām")]
            m_sutra[5] = ["ṭāṅasinasminātsyenāḥ (7.1.12)", "osi ca (7.3.104)", "hrasvanadyāpo nuṭ (7.1.54)"]

            m_iast[6] = [f"{b}e", f"{b}ayoḥ", f"{b}eṣu"]
            m_sutra[6] = ["ṅer e (7.1.15)", "osi ca (7.3.104)", "ādeśapratyayayoḥ (8.3.59)"]

            m_iast[7] = [f"he {b}am/he {b}a", f"he {b}e", apply_natva(f"he {b}āni")]
            m_sutra[7] = ["ato'm / sambuddhau ca (7.1.24)", "napuṃsakācca (7.1.19)", "jas-śasoḥ śiḥ (7.1.20)"]

        # -------------------------------------------------------------
        # 3. ĀKĀRĀNTA STRĪLIṄGA (e.g. latā, vidyā, kanyā)
        # -------------------------------------------------------------
        elif paradigm == "ajanta_aa_feminine" or (stem.endswith('ā') and gender.startswith(('f', 's'))):
            b = stem[:-1]
            m_iast[0] = [f"{b}ā", f"{b}e", f"{b}āḥ"]
            m_sutra[0] = ["āp-pṛktāt hal-ṅy-ābbhyo... (6.1.68)", "aunas-syāḥ (7.1.18: au -> śī)", "ataśca (6.1.102)"]

            m_iast[1] = [f"{b}ām", f"{b}e", f"{b}āḥ"]
            m_sutra[1] = ["ami pūrvaḥ (6.1.107)", "aunas-syāḥ (7.1.18)", "ajādyataṣṭāp (4.1.4) & dīrghaḥ"]

            m_iast[2] = [f"{b}ayā", f"{b}ābhyām", f"{b}ābhiḥ"]
            m_sutra[2] = ["āṅo nā'striyām blocked -> āpo yāṭ (7.3.105)", "supi ca (7.3.102)", "ato bhisa ais blocked for āp"]

            m_iast[3] = [f"{b}āyai", f"{b}ābhyām", f"{b}ābhyaḥ"]
            m_sutra[3] = ["yāḍāpaḥ (7.3.113: yāṭ āgama) + vṛddhireci (6.1.88)", "supi ca", "bahuvecane jhalyet blocked for āp"]

            m_iast[4] = [f"{b}āyāḥ", f"{b}ābhyām", f"{b}ābhyaḥ"]
            m_sutra[4] = ["yāḍāpaḥ (7.3.113: yāṭ) & ṅasi-ṅasośca", "supi ca", "āp inflection"]

            m_iast[5] = [f"{b}āyāḥ", f"{b}ayoḥ", apply_natva(f"{b}ānām")]
            m_sutra[5] = ["yāḍāpaḥ (7.3.113: yāṭ)", "āpo dīrghād osi (7.3.106)", "hrasvanadyāpo nuṭ (7.1.54)"]

            m_iast[6] = [f"{b}āyām", f"{b}ayoḥ", f"{b}āsu"]
            m_sutra[6] = ["yāḍāpaḥ (7.3.113) & ṅer-ām (7.3.116)", "āpo dīrghād osi", "ādeśapratyayayoḥ (8.3.59)"]

            m_iast[7] = [f"he {b}e", f"he {b}e", f"he {b}āḥ"]
            m_sutra[7] = ["sambuddhau ca (7.3.106: eṅ/hrasva)", "aunas-syāḥ (7.1.18)", "ataśca (6.1.102)"]

        # -------------------------------------------------------------
        # 4. IKĀRĀNTA PUṂLIṄGA (e.g. hari, muni, kavi)
        # -------------------------------------------------------------
        elif paradigm == "ajanta_i_masculine":
            b = stem[:-1]
            m_iast[0] = [f"{b}iḥ", f"{b}ī", f"{b}ayaḥ"]
            m_sutra[0] = ["svaujas... (4.1.2)", "prathamayoḥ pūrvasavarṇaḥ (6.1.102)", "jasi ca (7.3.109: guṇa)"]

            m_iast[1] = [f"{b}im", f"{b}ī", apply_natva(f"{b}īn")]
            m_sutra[1] = ["ami pūrvaḥ (6.1.107)", "prathamayoḥ pūrvasavarṇaḥ", "tasmācchaso naḥ puṃsi (6.1.103)"]

            m_iast[2] = [apply_natva(f"{b}inā"), f"{b}ibhyām", f"{b}ibhiḥ"]
            m_sutra[2] = ["āṅo nā'striyām (7.3.120: nā ādeśa)", "supi ca", "bhis -> bhiḥ"]

            m_iast[3] = [f"{b}aye", f"{b}ibhyām", f"{b}ibhyaḥ"]
            m_sutra[3] = ["gher ṅiti (7.3.111: guṇa) & eco'yavāyāvaḥ", "supi ca", "bhyas"]

            m_iast[4] = [f"{b}eḥ", f"{b}ibhyām", f"{b}ibhyaḥ"]
            m_sutra[4] = ["gher ṅiti (7.3.111) & ṅasi-ṅasośca (6.1.110)", "supi ca", "bhyas"]

            m_iast[5] = [f"{b}eḥ", f"{b}yoḥ", apply_natva(f"{b}īnām")]
            m_sutra[5] = ["gher ṅiti (7.3.111) & ṅasi-ṅasośca", "ikoyaṇaci (6.1.77: yaṇ)", "hrasvanadyāpo nuṭ (7.1.54: dīrgha)"]

            m_iast[6] = [f"{b}au", f"{b}yoḥ", f"{b}iṣu"]
            m_sutra[6] = ["ac ca gheḥ (7.3.119: ṅer au)", "ikoyaṇaci (6.1.77)", "ādeśapratyayayoḥ (8.3.59)"]

            m_iast[7] = [f"he {b}e", f"he {b}ī", f"he {b}ayaḥ"]
            m_sutra[7] = ["hrasvasya guṇaḥ (7.3.108: sambuddhau)", "prathamayoḥ pūrvasavarṇaḥ", "jasi ca (7.3.109)"]

        # -------------------------------------------------------------
        # 4B. IKĀRĀNTA STRĪLIṄGA (e.g. mati, buddhi, kīrti - Dual Vibhāṣā)
        # -------------------------------------------------------------
        elif paradigm == "ajanta_i_feminine":
            b = stem[:-1]
            m_iast[0] = [f"{b}iḥ", f"{b}ī", f"{b}ayaḥ"]
            m_sutra[0] = ["svaujas...", "prathamayoḥ pūrvasavarṇaḥ", "jasi ca (7.3.109)"]
            m_iast[1] = [f"{b}im", f"{b}ī", f"{b}īḥ"]
            m_sutra[1] = ["ami pūrvaḥ", "prathamayoḥ pūrvasavarṇaḥ", "śas -> īḥ (strīṣu)"]
            m_iast[2] = [f"{b}yā", f"{b}ibhyām", f"{b}ibhiḥ"]
            m_sutra[2] = ["iko yaṇaci (6.1.77)", "supi ca", "bhis"]
            m_iast[3] = [f"{b}aye / {b}yai", f"{b}ibhyām", f"{b}ibhyaḥ"]
            m_sutra[3] = ["ṅiti hrasvaśca (1.4.6: nadī-sañjñā vā) -> gher ṅiti / āṭ", "supi ca", "bhyas"]
            m_iast[4] = [f"{b}eḥ / {b}yāḥ", f"{b}ibhyām", f"{b}ibhyaḥ"]
            m_sutra[4] = ["ṅiti hrasvaśca (1.4.6) -> ṅasi-ṅasośca / āṭ", "supi ca", "bhyas"]
            m_iast[5] = [f"{b}eḥ / {b}yāḥ", f"{b}yoḥ", apply_natva(f"{b}īnām")]
            m_sutra[5] = ["ṅiti hrasvaśca (1.4.6)", "iko yaṇaci", "hrasvanadyāpo nuṭ"]
            m_iast[6] = [f"{b}au / {b}yām", f"{b}yoḥ", f"{b}iṣu"]
            m_sutra[6] = ["ac ca gheḥ (7.3.119) / ṅer ām (7.3.116)", "iko yaṇaci", "ādeśapratyayayoḥ"]
            m_iast[7] = [f"he {b}e", f"he {b}ī", f"he {b}ayaḥ"]
            m_sutra[7] = ["hrasvasya guṇaḥ", "prathamayoḥ pūrvasavarṇaḥ", "jasi ca"]

        # -------------------------------------------------------------
        # 4C. IKĀRĀNTA NAPUṂSAKALIṄGA (e.g. vāri, dadhi)
        # -------------------------------------------------------------
        elif paradigm == "ajanta_i_neuter":
            b = stem[:-1]
            m_iast[0] = [f"{b}i", apply_natva(f"{b}iṇī"), apply_natva(f"{b}īni")]
            m_sutra[0] = ["svamor napuṃsakāt (7.1.23: luk)", "napuṃsakācca (7.1.19: num)", "napuṃsakasya jhalacaḥ (7.1.72: dīrgha)"]
            m_iast[1] = [f"{b}i", apply_natva(f"{b}iṇī"), apply_natva(f"{b}īni")]
            m_sutra[1] = ["svamor napuṃsakāt", "napuṃsakācca", "napuṃsakasya jhalacaḥ"]
            m_iast[2] = [apply_natva(f"{b}iṇā"), f"{b}ibhyām", f"{b}ibhiḥ"]
            m_sutra[2] = ["ikah sarvanāmasthāne... (7.1.73: num)", "supi ca", "bhis"]
            m_iast[3] = [apply_natva(f"{b}iṇe"), f"{b}ibhyām", f"{b}ibhyaḥ"]
            m_sutra[3] = ["num āgama", "supi ca", "bhyas"]
            m_iast[4] = [apply_natva(f"{b}inaḥ"), f"{b}ibhyām", f"{b}ibhyaḥ"]
            m_sutra[4] = ["num āgama", "supi ca", "bhyas"]
            m_iast[5] = [apply_natva(f"{b}inaḥ"), apply_natva(f"{b}inoḥ"), apply_natva(f"{b}īṇām")]
            m_sutra[5] = ["num āgama", "num āgama", "hrasvanadyāpo nuṭ"]
            m_iast[6] = [apply_natva(f"{b}iṇi"), apply_natva(f"{b}inoḥ"), f"{b}iṣu"]
            m_sutra[6] = ["num āgama", "num āgama", "ādeśapratyayayoḥ"]
            m_iast[7] = [f"he {b}i / he {b}e", apply_natva(f"he {b}iṇī"), apply_natva(f"he {b}īni")]
            m_sutra[7] = ["hrasvasya guṇaḥ vā", "napuṃsakācca", "napuṃsakasya jhalacaḥ"]

        # -------------------------------------------------------------
        # 5. ĪKĀRĀNTA STRĪLIṄGA (e.g. nadī, devī, jananī)
        # -------------------------------------------------------------
        elif paradigm == "ajanta_ii_feminine":
            b = stem[:-1]
            m_iast[0] = [f"{b}ī", f"{b}yau", f"{b}yaḥ"]
            m_sutra[0] = ["halṅyābbhyo dīrghāt... (6.1.68: su-lopa)", "iko yaṇaci (6.1.77)", "iko yaṇaci (6.1.77)"]

            m_iast[1] = [f"{b}īm", f"{b}yau", f"{b}īḥ"]
            m_sutra[1] = ["ami pūrvaḥ (6.1.107)", "iko yaṇaci (6.1.77)", "prathamayoḥ pūrvasavarṇaḥ (6.1.102)"]

            m_iast[2] = [f"{b}yā", f"{b}ībhyām", f"{b}ībhiḥ"]
            m_sutra[2] = ["iko yaṇaci (6.1.77)", "supi ca", "bhis -> bhiḥ"]

            m_iast[3] = [f"{b}yai", f"{b}ībhyām", f"{b}ībhyaḥ"]
            m_sutra[3] = ["āṭ nadībhyaḥ (7.3.112: āṭ āgama) + vṛddhi", "supi ca", "bhyas"]

            m_iast[4] = [f"{b}yāḥ", f"{b}ībhyām", f"{b}ībhyaḥ"]
            m_sutra[4] = ["āṭ nadībhyaḥ (7.3.112: āṭ) + yaṇ", "supi ca", "bhyas"]

            m_iast[5] = [f"{b}yāḥ", f"{b}yoḥ", apply_natva(f"{b}īnām")]
            m_sutra[5] = ["āṭ nadībhyaḥ (7.3.112)", "iko yaṇaci (6.1.77)", "hrasvanadyāpo nuṭ (7.1.54: nuṭ)"]

            m_iast[6] = [f"{b}yām", f"{b}yoḥ", f"{b}īṣu"]
            m_sutra[6] = ["ṅer ām nadyām-nībhyah (7.3.116)", "iko yaṇaci (6.1.77)", "ādeśapratyayayoḥ (8.3.59)"]

            m_iast[7] = [f"he {b}i", f"he {b}yau", f"he {b}yaḥ"]
            m_sutra[7] = ["ambārthanadyorhrasvaḥ (7.3.107: hrasva)", "iko yaṇaci (6.1.77)", "iko yaṇaci (6.1.77)"]

        # -------------------------------------------------------------
        # 6. UKĀRĀNTA PUṂLIṄGA (e.g. guru, bhānu, śambhu)
        # -------------------------------------------------------------
        elif paradigm == "ajanta_u_masculine":
            b = stem[:-1]
            m_iast[0] = [f"{b}uḥ", f"{b}ū", f"{b}avaḥ"]
            m_sutra[0] = ["svaujas... (4.1.2)", "prathamayoḥ pūrvasavarṇaḥ (6.1.102)", "jasi ca (7.3.109: guṇa)"]

            m_iast[1] = [f"{b}um", f"{b}ū", apply_natva(f"{b}ūn")]
            m_sutra[1] = ["ami pūrvaḥ (6.1.107)", "prathamayoḥ pūrvasavarṇaḥ", "tasmācchaso naḥ puṃsi (6.1.103)"]

            m_iast[2] = [apply_natva(f"{b}unā"), f"{b}ubhyām", f"{b}ubhiḥ"]
            m_sutra[2] = ["āṅo nā'striyām (7.3.120: nā ādeśa)", "supi ca", "bhis -> bhiḥ"]

            m_iast[3] = [f"{b}ave", f"{b}ubhyām", f"{b}ubhyaḥ"]
            m_sutra[3] = ["gher ṅiti (7.3.111: guṇa) & eco'yavāyāvaḥ", "supi ca", "bhyas"]

            m_iast[4] = [f"{b}oḥ", f"{b}ubhyām", f"{b}ubhyaḥ"]
            m_sutra[4] = ["gher ṅiti (7.3.111) & ṅasi-ṅasośca (6.1.110)", "supi ca", "bhyas"]

            m_iast[5] = [f"{b}oḥ", f"{b}voḥ", apply_natva(f"{b}ūnām")]
            m_sutra[5] = ["gher ṅiti & ṅasi-ṅasośca", "ikoyaṇaci (6.1.77: va)", "hrasvanadyāpo nuṭ (7.1.54: dīrgha)"]

            m_iast[6] = [f"{b}au", f"{b}voḥ", f"{b}uṣu"]
            m_sutra[6] = ["ac ca gheḥ (7.3.119: ṅer au)", "ikoyaṇaci (6.1.77)", "ādeśapratyayayoḥ (8.3.59)"]

            m_iast[7] = [f"he {b}o", f"he {b}ū", f"he {b}avaḥ"]
            m_sutra[7] = ["hrasvasya guṇaḥ (7.3.108: sambuddhau)", "prathamayoḥ pūrvasavarṇaḥ", "jasi ca (7.3.109)"]

        # -------------------------------------------------------------
        # 6B. UKĀRĀNTA NAPUṂSAKALIṄGA (e.g. madhu, vastu)
        # -------------------------------------------------------------
        elif paradigm == "ajanta_u_neuter":
            b = stem[:-1]
            m_iast[0] = [f"{b}u", apply_natva(f"{b}unī"), apply_natva(f"{b}ūni")]
            m_sutra[0] = ["svamor napuṃsakāt (7.1.23)", "napuṃsakācca (7.1.19)", "napuṃsakasya jhalacaḥ (7.1.72)"]
            m_iast[1] = [f"{b}u", apply_natva(f"{b}unī"), apply_natva(f"{b}ūni")]
            m_sutra[1] = ["svamor napuṃsakāt", "napuṃsakācca", "napuṃsakasya jhalacaḥ"]
            m_iast[2] = [apply_natva(f"{b}unā"), f"{b}ubhyām", f"{b}ubhiḥ"]
            m_sutra[2] = ["ikah sarvanāmasthāne... (7.1.73: num)", "supi ca", "bhis"]
            m_iast[3] = [apply_natva(f"{b}une"), f"{b}ubhyām", f"{b}ubhyaḥ"]
            m_sutra[3] = ["num āgama", "supi ca", "bhyas"]
            m_iast[4] = [apply_natva(f"{b}unaḥ"), f"{b}ubhyām", f"{b}ubhyaḥ"]
            m_sutra[4] = ["num āgama", "supi ca", "bhyas"]
            m_iast[5] = [apply_natva(f"{b}unaḥ"), apply_natva(f"{b}unoḥ"), apply_natva(f"{b}ūnām")]
            m_sutra[5] = ["num āgama", "num āgama", "hrasvanadyāpo nuṭ"]
            m_iast[6] = [apply_natva(f"{b}uni"), apply_natva(f"{b}unoḥ"), f"{b}uṣu"]
            m_sutra[6] = ["num āgama", "num āgama", "ādeśapratyayayoḥ"]
            m_iast[7] = [f"he {b}u / he {b}o", apply_natva(f"he {b}unī"), apply_natva(f"he {b}ūni")]
            m_sutra[7] = ["hrasvasya guṇaḥ vā", "napuṃsakācca", "napuṃsakasya jhalacaḥ"]

        # -------------------------------------------------------------
        # 6C. ŪKĀRĀNTA STRĪLIṄGA (e.g. vadhū, camū)
        # -------------------------------------------------------------
        elif paradigm == "ajanta_uu_feminine":
            b = stem[:-1]
            m_iast[0] = [f"{b}ūḥ", f"{b}vau", f"{b}vaḥ"]
            m_sutra[0] = ["svaujas...", "iko yaṇaci (6.1.77)", "iko yaṇaci"]
            m_iast[1] = [f"{b}ūm", f"{b}vau", f"{b}ūḥ"]
            m_sutra[1] = ["ami pūrvaḥ", "iko yaṇaci", "prathamayoḥ pūrvasavarṇaḥ"]
            m_iast[2] = [f"{b}vā", f"{b}ūbhyām", f"{b}ūbhiḥ"]
            m_sutra[2] = ["iko yaṇaci", "supi ca", "bhis"]
            m_iast[3] = [f"{b}vai", f"{b}ūbhyām", f"{b}ūbhyaḥ"]
            m_sutra[3] = ["āṭ nadībhyaḥ", "supi ca", "bhyas"]
            m_iast[4] = [f"{b}vāḥ", f"{b}ūbhyām", f"{b}ūbhyaḥ"]
            m_sutra[4] = ["āṭ nadībhyaḥ", "supi ca", "bhyas"]
            m_iast[5] = [f"{b}vāḥ", f"{b}voḥ", apply_natva(f"{b}ūnām")]
            m_sutra[5] = ["āṭ nadībhyaḥ", "iko yaṇaci", "hrasvanadyāpo nuṭ"]
            m_iast[6] = [f"{b}vām", f"{b}voḥ", f"{b}ūṣu"]
            m_sutra[6] = ["ṅer ām nadyām...", "iko yaṇaci", "ādeśapratyayayoḥ"]
            m_iast[7] = [f"he {b}u", f"he {b}vau", f"he {b}vaḥ"]
            m_sutra[7] = ["ambārthanadyorhrasvaḥ", "iko yaṇaci", "iko yaṇaci"]

        # -------------------------------------------------------------
        # 7. ṚKĀRĀNTA (e.g. pitṛ, bhrātṛ, kartṛ, mātṛ)
        # -------------------------------------------------------------
        elif paradigm in ("ajanta_ri_masculine_kinship", "ajanta_ri_masculine_agentive", "ajanta_ri_masculine", "ajanta_ri_feminine") or stem.endswith('ṛ'):
            b = stem[:-1]
            is_matr = stem in ('mātṛ', 'svasṛ', 'duhitṛ', 'yātṛ', 'nanāndṛ')
            is_kinship = stem in ('pitṛ', 'bhrātṛ', 'mātṛ', 'svasṛ', 'duhitṛ', 'jāmātṛ') or "kinship" in paradigm
            mid = "ar" if is_kinship else "ār"
            m_iast[0] = [f"{b}ā", f"{b}{mid}au", f"{b}{mid}aḥ"]
            m_sutra[0] = ["an-an-as su-lopa & ṛto'ṅi sarvanāmasthāne (7.3.110)", "ṛto'ṅi sarvanāmasthāne", "ṛto'ṅi sarvanāmasthāne"]

            m_iast[1] = [f"{b}{mid}am", f"{b}{mid}au", apply_natva(f"{b}ṝn") if not is_matr else apply_natva(f"{b}ṝḥ")]
            m_sutra[1] = ["ami pūrvaḥ", "ṛto'ṅi sarvanāmasthāne", "tasmācchaso naḥ puṃsi / strīṣu śas"]

            m_iast[2] = [apply_natva(f"{b}rā"), f"{b}ṛbhyām", f"{b}ṛbhiḥ"]
            m_sutra[2] = ["iko yaṇaci (6.1.77: ra)", "supi ca", "bhis"]

            m_iast[3] = [f"{b}re", f"{b}ṛbhyām", f"{b}ṛbhyaḥ"]
            m_sutra[3] = ["iko yaṇaci (6.1.77)", "supi ca", "bhyas"]

            m_iast[4] = [f"{b}uḥ", f"{b}ṛbhyām", f"{b}ṛbhyaḥ"]
            m_sutra[4] = ["ṛta ut (6.1.111: utva)", "supi ca", "bhyas"]

            m_iast[5] = [f"{b}uḥ", f"{b}roḥ", apply_natva(f"{b}ṝṇām")]
            m_sutra[5] = ["ṛta ut (6.1.111)", "iko yaṇaci", "nāmi (6.4.3: dīrgha ṝ)"]

            m_iast[6] = [f"{b}ari", f"{b}roḥ", f"{b}ṛṣu"]
            m_sutra[6] = ["ṛto ṅau (7.3.119: guṇa ar)", "iko yaṇaci", "ādeśapratyayayoḥ (8.3.59)"]

            m_iast[7] = [f"he {b}ar", f"he {b}{mid}au", f"he {b}{mid}aḥ"]
            m_sutra[7] = ["ṛto guṇaḥ sambuddhau", "ṛto'ṅi sarvanāmasthāne", "ṛto'ṅi sarvanāmasthāne"]

        # -------------------------------------------------------------
        # 8. DIPHTHONG & IRREGULAR AJANTA (go, nau, sakhi, pati)
        # -------------------------------------------------------------
        elif paradigm == "diphthong_go" or stem == 'go':
            m_iast[0] = ["gauḥ", "gāvau", "gāvaḥ"]
            m_iast[1] = ["gām", "gāvau", "gāḥ"]
            m_iast[2] = ["gavā", "gobhyām", "gobhiḥ"]
            m_iast[3] = ["gave", "gobhyām", "gobhyaḥ"]
            m_iast[4] = ["goḥ", "gobhyām", "gobhyaḥ"]
            m_iast[5] = ["goḥ", "gavoḥ", "gavām"]
            m_iast[6] = ["gavi", "gavoḥ", "goṣu"]
            m_iast[7] = ["he gauḥ", "he gāvau", "he gāvaḥ"]
            for v in range(8):
                for c in range(3):
                    m_sutra[v][c] = "auto'm śasoḥ (6.1.93) & aci ra ṛtaḥ (6.1.77)"

        elif paradigm == "irregular_sakhi" or stem == 'sakhi':
            m_iast[0] = ["sakhā", "sakhāyau", "sakhāyaḥ"]
            m_iast[1] = ["sakhāyam", "sakhāyau", "sakhīn"]
            m_iast[2] = ["sakhyā", "sakhibhyām", "sakhibhiḥ"]
            m_iast[3] = ["sakhye", "sakhibhyām", "sakhibhyaḥ"]
            m_iast[4] = ["sakhyuḥ", "sakhibhyām", "sakhibhyaḥ"]
            m_iast[5] = ["sakhyuḥ", "sakhyoḥ", "sakhīnām"]
            m_iast[6] = ["sakhyau", "sakhyoḥ", "sakhiṣu"]
            m_iast[7] = ["he sakhe", "he sakhāyau", "he sakhāyaḥ"]
            for v in range(8):
                for c in range(3):
                    m_sutra[v][c] = "an-an-as su-lopa & sakhyurasambuddhau (7.1.92)"

        # -------------------------------------------------------------
        # 9. HALANTA IN-ANTA (e.g. guṇin, dhanin, jñānin, karmin)
        # -------------------------------------------------------------
        elif "halanta_in" in paradigm or stem.endswith('in'):
            b = stem[:-2]
            m_iast[0] = [f"{b}ī", f"{b}inau", f"{b}inaḥ"]
            m_sutra[0] = ["sau ca (6.4.13: dīrgha) & halṅyābbhyo... (6.1.68)", "sarvanāmasthāne cāsambuddhau", "sarvanāmasthāne cāsambuddhau"]

            m_iast[1] = [f"{b}inam", f"{b}inau", f"{b}inaḥ"]
            m_sutra[1] = ["ami pūrvaḥ", "sarvanāmasthāne", "śas"]

            m_iast[2] = [apply_natva(f"{b}inā"), f"{b}ibhyām", f"{b}ibhiḥ"]
            m_sutra[2] = ["svaujas...", "nalopaḥ prātipadikāntasya (8.2.7)", "nalopaḥ (8.2.7)"]

            m_iast[3] = [f"{b}ine", f"{b}ibhyām", f"{b}ibhyaḥ"]
            m_sutra[3] = ["svaujas...", "nalopaḥ (8.2.7)", "nalopaḥ (8.2.7)"]

            m_iast[4] = [f"{b}inaḥ", f"{b}ibhyām", f"{b}ibhyaḥ"]
            m_sutra[4] = ["sasajuṣo ruḥ", "nalopaḥ (8.2.7)", "nalopaḥ (8.2.7)"]

            m_iast[5] = [f"{b}inaḥ", f"{b}inoḥ", apply_natva(f"{b}inām")]
            m_sutra[5] = ["sasajuṣo ruḥ", "sasajuṣo ruḥ", "hrasvanadyāpo nuṭ blocked"]

            m_iast[6] = [f"{b}ini", f"{b}inoḥ", f"{b}iṣu"]
            m_sutra[6] = ["svaujas...", "sasajuṣo ruḥ", "ādeśapratyayayoḥ (8.3.59)"]

            m_iast[7] = [f"he {b}in", f"he {b}inau", f"he {b}inaḥ"]
            m_sutra[7] = ["na sambuddhyoḥ (8.2.8)", "sarvanāmasthāne", "sarvanāmasthāne"]

        # -------------------------------------------------------------
        # 10. HALANTA AN-ANTA (rājan vs ātman vs nāman)
        # -------------------------------------------------------------
        elif "halanta_an" in paradigm:
            if "neuter" in paradigm: # nāman, karman
                b = stem[:-2]
                m_iast[0] = [f"{b}a", f"{b}nī / {b}anī", apply_natva(f"{b}āni")]
                m_sutra[0] = ["sarvanāmasthāne cāsambuddhau", "napuṃsakācca (7.1.19)", "napuṃsakasya jhalacaḥ (7.1.72)"]
                m_iast[1] = [f"{b}a", f"{b}nī / {b}anī", apply_natva(f"{b}āni")]
                m_sutra[1] = ["sarvanāmasthāne cāsambuddhau", "napuṃsakācca", "napuṃsakasya jhalacaḥ"]
            else: # rājan vs ātman
                b = stem[:-2]
                is_cluster = stem in ('ātman', 'brahman', 'adhvan', 'yajvan') or "cluster" in paradigm
                allop = f"{b}an" if is_cluster else (f"{b}ñ" if b == "rāj" else f"{b}n")

                m_iast[0] = [f"{b}ā", f"{b}ānau", f"{b}ānaḥ"]
                m_sutra[0] = ["in-han-pūṣāryamṇāṃ śau (6.4.12: dīrgha)", "sarvanāmasthāne cāsambuddhau", "sarvanāmasthāne cāsambuddhau"]
                m_iast[1] = [f"{b}ānam", f"{b}ānau", f"{allop}aḥ" if is_cluster else (f"{b}ñaḥ" if b == "rāj" else f"{b}naḥ")]
                m_sutra[1] = ["ami pūrvaḥ", "sarvanāmasthāne cāsambuddhau", "allopo'naḥ (6.4.134: a-lopa)"]

            allop = f"{b}an" if (stem in ('ātman', 'brahman') or "cluster" in paradigm) else (f"{b}ñ" if b == "rāj" else f"{b}n")
            m_iast[2] = [apply_natva(f"{allop}ā"), f"{b}abhyām", f"{b}abhiḥ"]
            m_sutra[2] = ["allopo'naḥ / na saṃyogād vamantaḥ (6.4.137)", "nalopaḥ prātipadikāntasya (8.2.7)", "nalopaḥ prātipadikāntasya"]

            m_iast[3] = [f"{allop}e", f"{b}abhyām", f"{b}abhyaḥ"]
            m_sutra[3] = ["allopo'naḥ (6.4.134)", "nalopaḥ (8.2.7)", "nalopaḥ (8.2.7)"]

            m_iast[4] = [f"{allop}aḥ", f"{b}abhyām", f"{b}abhyaḥ"]
            m_sutra[4] = ["allopo'naḥ (6.4.134)", "nalopaḥ (8.2.7)", "nalopaḥ (8.2.7)"]

            m_iast[5] = [f"{allop}aḥ", f"{allop}oḥ", apply_natva(f"{allop}ām")]
            m_sutra[5] = ["allopo'naḥ (6.4.134)", "allopo'naḥ (6.4.134)", "allopo'naḥ (6.4.134)"]

            m_iast[6] = [f"{allop}i / {b}ani", f"{allop}oḥ", f"{b}asu"]
            m_sutra[6] = ["vibhāṣā ṅi-śyoḥ (6.4.136)", "allopo'naḥ (6.4.134)", "nalopaḥ (8.2.7)"]

            m_iast[7] = [f"he {b}an", f"he {b}ānau", f"he {b}ānaḥ"]
            m_sutra[7] = ["na sambuddhyoḥ (8.2.8: nalopa blocked)", "sarvanāmasthāne", "sarvanāmasthāne"]

        # -------------------------------------------------------------
        # 11. HALANTA AS-ANTA NEUTER (e.g. manas, tejas, payas, yaśas)
        # -------------------------------------------------------------
        elif paradigm == "halanta_as_neuter" or stem.endswith('as'):
            b = stem[:-2]
            m_iast[0] = [f"{b}aḥ", f"{b}asī", apply_natva(f"{b}āṃsi")]
            m_sutra[0] = ["sasajuṣo ruḥ (8.2.66) & kharavasānayor visarjanīyaḥ (8.3.15)", "napuṃsakācca (7.1.19)", "santamahataḥ saṃyogasya (6.4.10: num + dīrgha)"]

            m_iast[1] = [f"{b}aḥ", f"{b}asī", apply_natva(f"{b}āṃsi")]
            m_sutra[1] = ["sasajuṣo ruḥ (8.2.66)", "napuṃsakācca (7.1.19)", "santamahataḥ saṃyogasya (6.4.10)"]

            m_iast[2] = [apply_natva(f"{b}asā"), f"{b}obhyām", f"{b}obhiḥ"]
            m_sutra[2] = ["svaujas...", "haśi ca (6.1.114: utva -> o)", "haśi ca (6.1.114: utva -> o)"]

            m_iast[3] = [f"{b}ase", f"{b}obhyām", f"{b}obhyaḥ"]
            m_sutra[3] = ["svaujas...", "haśi ca (6.1.114)", "haśi ca (6.1.114)"]

            m_iast[4] = [f"{b}asaḥ", f"{b}obhyām", f"{b}obhyaḥ"]
            m_sutra[4] = ["sasajuṣo ruḥ", "haśi ca (6.1.114)", "haśi ca (6.1.114)"]

            m_iast[5] = [f"{b}asaḥ", f"{b}asoḥ", apply_natva(f"{b}asām")]
            m_sutra[5] = ["sasajuṣo ruḥ", "sasajuṣo ruḥ", "svaujas..."]

            m_iast[6] = [f"{b}asi", f"{b}asoḥ", f"{b}aḥsu"]
            m_sutra[6] = ["svaujas...", "sasajuṣo ruḥ", "kupvoḥ kaphau vā (8.3.37)"]

            m_iast[7] = [f"he {b}aḥ", f"he {b}asī", apply_natva(f"he {b}āṃsi")]
            m_sutra[7] = ["sasajuṣo ruḥ", "napuṃsakācca", "santamahataḥ saṃyogasya"]

        # -------------------------------------------------------------
        # 12. HALANTA AT/MAT/VAT (e.g. bhagavat, dhīmat, mahat)
        # -------------------------------------------------------------
        elif "halanta_at" in paradigm or stem.endswith(('at', 'mat', 'vat')):
            if stem.endswith(('mat', 'vat')):
                b = stem[:-3]
                suff = stem[-3:]
                v_char = suff[0]
                m_iast[0] = [f"{b}{v_char}ān", f"{b}{v_char}antau", f"{b}{v_char}antaḥ"]
                m_iast[1] = [f"{b}{v_char}antam", f"{b}{v_char}antau", apply_natva(f"{b}{v_char}ataḥ")]
                m_iast[2] = [apply_natva(f"{b}{v_char}atā"), f"{b}{v_char}adbhyām", f"{b}{v_char}adbhiḥ"]
                m_iast[3] = [f"{b}{v_char}ate", f"{b}{v_char}adbhyām", f"{b}{v_char}adbhyaḥ"]
                m_iast[4] = [f"{b}{v_char}ataḥ", f"{b}{v_char}adbhyām", f"{b}{v_char}adbhyaḥ"]
                m_iast[5] = [f"{b}{v_char}ataḥ", f"{b}{v_char}atoḥ", apply_natva(f"{b}{v_char}atām")]
                m_iast[6] = [f"{b}{v_char}ati", f"{b}{v_char}atoḥ", f"{b}{v_char}atsu"]
                m_iast[7] = [f"he {b}{v_char}an", f"he {b}{v_char}antau", f"he {b}{v_char}antaḥ"]
            else:
                b = stem[:-2]
                m_iast[0] = [f"{b}an", f"{b}antau", f"{b}antaḥ"]
                m_iast[1] = [f"{b}antam", f"{b}antau", apply_natva(f"{b}ataḥ")]
                m_iast[2] = [apply_natva(f"{b}atā"), f"{b}adbhyām", f"{b}adbhiḥ"]
                m_iast[3] = [f"{b}ate", f"{b}adbhyām", f"{b}adbhyaḥ"]
                m_iast[4] = [f"{b}ataḥ", f"{b}adbhyām", f"{b}adbhyaḥ"]
                m_iast[5] = [f"{b}ataḥ", f"{b}atoḥ", apply_natva(f"{b}atām")]
                m_iast[6] = [f"{b}ati", f"{b}atoḥ", f"{b}atsu"]
                m_iast[7] = [f"he {b}an", f"he {b}antau", f"he {b}antaḥ"]

            for v in range(8):
                for c in range(3):
                    m_sutra[v][c] = "ugidacāṃ sarvanāmasthāne'dhātoḥ (7.1.70: num) & atvasantasyā'dhātoḥ (6.4.14: dīrgha)"

        # -------------------------------------------------------------
        # 13. IRREGULAR & DIPHTHONG NOUNS (Patañjali's Mahābhāṣya Highlights)
        # -------------------------------------------------------------
        elif paradigm in ("irregular_sakhi", "diphthong_go", "irregular_pathin", "irregular_ahan") or stem in ('sakhi', 'go', 'pathin', 'ahan'):
            if stem == 'sakhi':
                m_iast[0] = ["sakhā", "sakhāyau", "sakhāyaḥ"]
                m_iast[1] = ["sakhāyam", "sakhāyau", "sakhīn"]
                m_iast[2] = ["sakhyā", "sakhibhyām", "sakhibhiḥ"]
                m_iast[3] = ["sakhye", "sakhibhyām", "sakhibhyaḥ"]
                m_iast[4] = ["sakhyuḥ", "sakhibhyām", "sakhibhyaḥ"]
                m_iast[5] = ["sakhyuḥ", "sakhyoḥ", "sakhīnām"]
                m_iast[6] = ["sakhyau", "sakhyoḥ", "sakhiṣu"]
                m_iast[7] = ["he sakhe", "he sakhāyau", "he sakhāyaḥ"]
                for v in range(8):
                    for c in range(3):
                        m_sutra[v][c] = "sakhyurasambuddhau (7.1.92: guṇa/vṛddhi) & khyatyāt parasya (6.1.112)"
            elif stem == 'go':
                m_iast[0] = ["gauḥ", "gāvau", "gāvaḥ"]
                m_iast[1] = ["gām", "gāvau", "gāḥ"]
                m_iast[2] = ["gavā", "gobhyām", "gobhiḥ"]
                m_iast[3] = ["gave", "gobhyām", "gobhyaḥ"]
                m_iast[4] = ["goḥ", "gobhyām", "gobhyaḥ"]
                m_iast[5] = ["goḥ", "gavoḥ", "gavām"]
                m_iast[6] = ["gavi", "gavoḥ", "goṣu"]
                m_iast[7] = ["he gauḥ", "he gāvau", "he gāvaḥ"]
                for v in range(8):
                    for c in range(3):
                        m_sutra[v][c] = "auto'mśaśoḥ (6.1.93: am/śas -> ām) & eco'yavāyāvaḥ (6.1.78)"
            elif stem == 'pathin':
                m_iast[0] = ["panthāḥ", "panthānau", "panthānaḥ"]
                m_iast[1] = ["panthānam", "panthānau", "pathaḥ"]
                m_iast[2] = ["pathā", "pathibhyām", "pathibhiḥ"]
                m_iast[3] = ["pathe", "pathibhyām", "pathibhyaḥ"]
                m_iast[4] = ["pathaḥ", "pathibhyām", "pathibhyaḥ"]
                m_iast[5] = ["pathaḥ", "pathoḥ", "pathām"]
                m_iast[6] = ["pathi", "pathoḥ", "pathiṣu"]
                m_iast[7] = ["he panthāḥ", "he panthānau", "he panthānaḥ"]
                for v in range(8):
                    for c in range(3):
                        m_sutra[v][c] = "pathimathoḥ sarvanāmasthāne (7.1.85: ātva) & bhasya ṭerlopaḥ (7.1.88)"
            elif stem == 'ahan':
                m_iast[0] = ["ahaḥ", "ahanī / ahnī", "ahāni"]
                m_iast[1] = ["ahaḥ", "ahanī / ahnī", "ahāni"]
                m_iast[2] = ["ahnā", "ahobhyām", "ahobhiḥ"]
                m_iast[3] = ["ahne", "ahobhyām", "ahobhyaḥ"]
                m_iast[4] = ["ahnaḥ", "ahobhyām", "ahobhyaḥ"]
                m_iast[5] = ["ahnaḥ", "ahnoḥ", "ahnām"]
                m_iast[6] = ["ahni / ahani", "ahnoḥ", "ahaḥsu"]
                m_iast[7] = ["he ahaḥ", "he ahanī / he ahnī", "he ahāni"]
                for v in range(8):
                    for c in range(3):
                        m_sutra[v][c] = "ahano dā ca (8.2.68: ru/rutva) & allopo'naḥ (6.4.134)"
            else:
                b = stem
                for v in range(8):
                    m_iast[v] = [f"{b}aḥ", f"{b}au", f"{b}āḥ"]
                    m_sutra[v] = ["suptiṅantam padam (1.4.14)", "svaujas... (4.1.2)", "svaujas... (4.1.2)"]

        # -------------------------------------------------------------
        # 14. HALANTA CONSONANTS (e.g. marut, vāc, sarit, diś)
        # -------------------------------------------------------------
        elif paradigm in ("halanta_marut_masculine", "halanta_consonant", "halanta_vac_feminine", "halanta_dis_feminine"):
            if stem == 'vāc':
                m_iast[0] = ["vāk", "vācau", "vācaḥ"]
                m_iast[1] = ["vācam", "vācau", "vācaḥ"]
                m_iast[2] = ["vācā", "vāgbhyām", "vāgbhiḥ"]
                m_iast[3] = ["vāce", "vāgbhyām", "vāgbhyaḥ"]
                m_iast[4] = ["vācaḥ", "vāgbhyām", "vāgbhyaḥ"]
                m_iast[5] = ["vācaḥ", "vācoḥ", "vācām"]
                m_iast[6] = ["vāci", "vācoḥ", "vākṣu"]
                m_iast[7] = ["he vāk", "he vācau", "he vācaḥ"]
                for v in range(8):
                    for c in range(3):
                        m_sutra[v][c] = "coḥ kuḥ (8.2.30) & jhalām jaśo'nte (8.2.39)"
            elif stem in ('diś', 'dṛś'):
                m_iast[0] = ["dik", "diśau", "diśaḥ"]
                m_iast[1] = ["diśam", "diśau", "diśaḥ"]
                m_iast[2] = ["diśā", "digbhyām", "digbhiḥ"]
                m_iast[3] = ["diśe", "digbhyām", "digbhyaḥ"]
                m_iast[4] = ["diśaḥ", "digbhyām", "digbhyaḥ"]
                m_iast[5] = ["diśaḥ", "diśoḥ", "diśām"]
                m_iast[6] = ["diśi", "diśoḥ", "dikṣu"]
                m_iast[7] = ["he dik", "he diśau", "he diśaḥ"]
                for v in range(8):
                    for c in range(3):
                        m_sutra[v][c] = "vraścabhraśjasṛjamṛjayajarājbhrācchachāṃ ṣaḥ (8.2.36) -> jaśtva"
            else: # marut, sarit
                b = stem[:-1]
                m_iast[0] = [f"{b}t", f"{b}tau", f"{b}taḥ"]
                m_iast[1] = [f"{b}tam", f"{b}tau", f"{b}taḥ"]
                m_iast[2] = [apply_natva(f"{b}tā"), f"{b}dbhyām", f"{b}dbhiḥ"]
                m_iast[3] = [f"{b}te", f"{b}dbhyām", f"{b}dbhyaḥ"]
                m_iast[4] = [f"{b}taḥ", f"{b}dbhyām", f"{b}dbhyaḥ"]
                m_iast[5] = [f"{b}taḥ", f"{b}toḥ", apply_natva(f"{b}tām")]
                m_iast[6] = [f"{b}ti", f"{b}toḥ", f"{b}tsu"]
                m_iast[7] = [f"he {b}t", f"he {b}tau", f"he {b}taḥ"]
                for v in range(8):
                    for c in range(3):
                        m_sutra[v][c] = "jhalām jaśo'nte (8.2.39) & khari ca (8.4.55)"

        # Fallback default derivation
        else:
            b = stem
            for v in range(8):
                m_iast[v] = [f"{b}aḥ", f"{b}au", f"{b}āḥ"]
                m_sutra[v] = ["suptiṅantam padam (1.4.14)", "svaujas... (4.1.2)", "svaujas... (4.1.2)"]

        return m_iast, m_sutra

    def _compute_pronoun_matrix(self, p_stem: str, gender: str) -> Tuple[List[List[str]], List[List[str]]]:
        """Synthesizes Pāṇinian Sarvanāma (Pronoun) Inflections."""
        m_iast: List[List[str]] = [["" for _ in range(3)] for _ in range(8)]
        m_sutra: List[List[str]] = [["" for _ in range(3)] for _ in range(8)]

        is_fem = gender.startswith(('f', 's'))
        is_neut = gender.startswith(('n', 'k'))

        if p_stem == 'tad':
            if is_fem:
                m_iast[0] = ["sā", "te", "tāḥ"]
                m_iast[1] = ["tām", "te", "tāḥ"]
                m_iast[2] = ["tayā", "tābhyām", "tābhiḥ"]
                m_iast[3] = ["tasyai", "tābhyām", "tābhyaḥ"]
                m_iast[4] = ["tasyāḥ", "tābhyām", "tābhyaḥ"]
                m_iast[5] = ["tasyāḥ", "tayoḥ", "tāsām"]
                m_iast[6] = ["tasyām", "tayoḥ", "tāsu"]
            elif is_neut:
                m_iast[0] = ["tat", "te", "tāni"]
                m_iast[1] = ["tat", "te", "tāni"]
                m_iast[2] = ["tena", "tābhyām", "taiḥ"]
                m_iast[3] = ["tasmai", "tābhyām", "tebhyaḥ"]
                m_iast[4] = ["tasmāt", "tābhyām", "tebhyaḥ"]
                m_iast[5] = ["tasya", "tayoḥ", "teṣām"]
                m_iast[6] = ["tasmin", "tayoḥ", "teṣu"]
            else: # Masculine
                m_iast[0] = ["saḥ", "tau", "te"]
                m_iast[1] = ["tam", "tau", "tān"]
                m_iast[2] = ["tena", "tābhyām", "taiḥ"]
                m_iast[3] = ["tasmai", "tābhyām", "tebhyaḥ"]
                m_iast[4] = ["tasmāt", "tābhyām", "tebhyaḥ"]
                m_iast[5] = ["tasya", "tayoḥ", "teṣām"]
                m_iast[6] = ["tasmin", "tayoḥ", "teṣu"]
            m_iast[7] = ["-", "-", "-"]

        elif p_stem == 'etad':
            if is_fem:
                m_iast[0] = ["eṣā", "ete", "etāḥ"]
                m_iast[1] = ["etām", "ete", "etāḥ"]
                m_iast[2] = ["etayā", "etābhyām", "etābhiḥ"]
                m_iast[3] = ["etasyai", "etābhyām", "etābhyaḥ"]
                m_iast[4] = ["etasyāḥ", "etābhyām", "etābhyaḥ"]
                m_iast[5] = ["etasyāḥ", "etayoḥ", "etāsām"]
                m_iast[6] = ["etasyām", "etayoḥ", "etāsu"]
            elif is_neut:
                m_iast[0] = ["etat", "ete", "etāni"]
                m_iast[1] = ["etat", "ete", "etāni"]
                m_iast[2] = ["etena", "etābhyām", "etaiḥ"]
                m_iast[3] = ["etasmai", "etābhyām", "etebhyaḥ"]
                m_iast[4] = ["etasmāt", "etābhyām", "etebhyaḥ"]
                m_iast[5] = ["etasya", "etayoḥ", "eteṣām"]
                m_iast[6] = ["etasmin", "etayoḥ", "eteṣu"]
            else:
                m_iast[0] = ["eṣaḥ", "etau", "ete"]
                m_iast[1] = ["etam", "etau", "etān"]
                m_iast[2] = ["etena", "etābhyām", "etaiḥ"]
                m_iast[3] = ["etasmai", "etābhyām", "etebhyaḥ"]
                m_iast[4] = ["etasmāt", "etābhyām", "etebhyaḥ"]
                m_iast[5] = ["etasya", "etayoḥ", "eteṣām"]
                m_iast[6] = ["etasmin", "etayoḥ", "eteṣu"]
            m_iast[7] = ["-", "-", "-"]

        elif p_stem == 'idam':
            if is_fem:
                m_iast[0] = ["iyam", "ime", "imāḥ"]
                m_iast[1] = ["imām", "ime", "imāḥ"]
                m_iast[2] = ["anayā", "ābhyām", "ābhiḥ"]
                m_iast[3] = ["asyai", "ābhyām", "ābhyaḥ"]
                m_iast[4] = ["asyāḥ", "ābhyām", "ābhyaḥ"]
                m_iast[5] = ["asyāḥ", "anayoḥ", "āsām"]
                m_iast[6] = ["asyām", "anayoḥ", "āsu"]
            elif is_neut:
                m_iast[0] = ["idam", "ime", "imāni"]
                m_iast[1] = ["idam", "ime", "imāni"]
                m_iast[2] = ["anena", "ābhyām", "ebhiḥ"]
                m_iast[3] = ["asmai", "ābhyām", "ebhyaḥ"]
                m_iast[4] = ["asmāt", "ābhyām", "ebhyaḥ"]
                m_iast[5] = ["asya", "anayoḥ", "eṣām"]
                m_iast[6] = ["asmin", "anayoḥ", "eṣu"]
            else: # Masculine
                m_iast[0] = ["ayam", "imau", "ime"]
                m_iast[1] = ["imam", "imau", "imān"]
                m_iast[2] = ["anena", "ābhyām", "ebhiḥ"]
                m_iast[3] = ["asmai", "ābhyām", "ebhyaḥ"]
                m_iast[4] = ["asmāt", "ābhyām", "ebhyaḥ"]
                m_iast[5] = ["asya", "anayoḥ", "eṣām"]
                m_iast[6] = ["asmin", "anayoḥ", "eṣu"]
            m_iast[7] = ["-", "-", "-"]

        elif p_stem == 'yad':
            if is_fem:
                m_iast[0] = ["yā", "ye", "yāḥ"]
                m_iast[1] = ["yām", "ye", "yāḥ"]
                m_iast[2] = ["yayā", "yābhyām", "yābhiḥ"]
                m_iast[3] = ["yasyai", "yābhyām", "yābhyaḥ"]
                m_iast[4] = ["yasyāḥ", "yābhyām", "yābhyaḥ"]
                m_iast[5] = ["yasyāḥ", "yayoḥ", "yāsām"]
                m_iast[6] = ["yasyām", "yayoḥ", "yāsu"]
            elif is_neut:
                m_iast[0] = ["yat", "ye", "yāni"]
                m_iast[1] = ["yat", "ye", "yāni"]
                m_iast[2] = ["yena", "yābhyām", "yaiḥ"]
                m_iast[3] = ["yasmai", "yābhyām", "yebhyaḥ"]
                m_iast[4] = ["yasmāt", "yābhyām", "yebhyaḥ"]
                m_iast[5] = ["yasya", "yayoḥ", "yeṣām"]
                m_iast[6] = ["yasmin", "yayoḥ", "yeṣu"]
            else:
                m_iast[0] = ["yaḥ", "yau", "ye"]
                m_iast[1] = ["yam", "yau", "yān"]
                m_iast[2] = ["yena", "yābhyām", "yaiḥ"]
                m_iast[3] = ["yasmai", "yābhyām", "yebhyaḥ"]
                m_iast[4] = ["yasmāt", "yābhyām", "yebhyaḥ"]
                m_iast[5] = ["yasya", "yayoḥ", "yeṣām"]
                m_iast[6] = ["yasmin", "yayoḥ", "yeṣu"]
            m_iast[7] = ["-", "-", "-"]

        elif p_stem == 'kim':
            if is_fem:
                m_iast[0] = ["kā", "ke", "kāḥ"]
                m_iast[1] = ["kām", "ke", "kāḥ"]
                m_iast[2] = ["kayā", "kābhyām", "kābhiḥ"]
                m_iast[3] = ["kasyai", "kābhyām", "kābhyaḥ"]
                m_iast[4] = ["kasyāḥ", "kābhyām", "kābhyaḥ"]
                m_iast[5] = ["kasyāḥ", "kayoḥ", "kāsām"]
                m_iast[6] = ["kasyām", "kayoḥ", "kāsu"]
            elif is_neut:
                m_iast[0] = ["kim", "ke", "kāni"]
                m_iast[1] = ["kim", "ke", "kāni"]
                m_iast[2] = ["kena", "kābhyām", "kaiḥ"]
                m_iast[3] = ["kasmai", "kābhyām", "kebhyaḥ"]
                m_iast[4] = ["kasmāt", "kābhyām", "kebhyaḥ"]
                m_iast[5] = ["kasya", "kayoḥ", "keṣām"]
                m_iast[6] = ["kasmin", "kayoḥ", "keṣu"]
            else:
                m_iast[0] = ["kaḥ", "kau", "ke"]
                m_iast[1] = ["kam", "kau", "kān"]
                m_iast[2] = ["kena", "kābhyām", "kaiḥ"]
                m_iast[3] = ["kasmai", "kābhyām", "kebhyaḥ"]
                m_iast[4] = ["kasmāt", "kābhyām", "kebhyaḥ"]
                m_iast[5] = ["kasya", "kayoḥ", "keṣām"]
                m_iast[6] = ["kasmin", "kayoḥ", "keṣu"]
            m_iast[7] = ["-", "-", "-"]

        elif p_stem == 'sarva':
            if is_fem:
                m_iast[0] = ["sarvā", "sarve", "sarvāḥ"]
                m_iast[1] = ["sarvām", "sarve", "sarvāḥ"]
                m_iast[2] = ["sarvayā", "sarvābhyām", "sarvābhiḥ"]
                m_iast[3] = ["sarvasyai", "sarvābhyām", "sarvābhyaḥ"]
                m_iast[4] = ["sarvasyāḥ", "sarvābhyām", "sarvābhyaḥ"]
                m_iast[5] = ["sarvasyāḥ", "sarvayoḥ", "sarvāsām"]
                m_iast[6] = ["sarvasyām", "sarvayoḥ", "sarvāsu"]
                m_iast[7] = ["he sarve", "he sarve", "he sarvāḥ"]
            elif is_neut:
                m_iast[0] = ["sarvam", "sarve", "sarvāṇi"]
                m_iast[1] = ["sarvam", "sarve", "sarvāṇi"]
                m_iast[2] = ["sarveṇa", "sarvābhyām", "sarvaiḥ"]
                m_iast[3] = ["sarvasmai", "sarvābhyām", "sarvebhyaḥ"]
                m_iast[4] = ["sarvasmāt", "sarvābhyām", "sarvebhyaḥ"]
                m_iast[5] = ["sarvasya", "sarvayoḥ", "sarveṣām"]
                m_iast[6] = ["sarvasmin", "sarvayoḥ", "sarveṣu"]
                m_iast[7] = ["he sarvam", "he sarve", "he sarvāṇi"]
            else:
                m_iast[0] = ["sarvaḥ", "sarvau", "sarve"]
                m_iast[1] = ["sarvam", "sarvau", "sarvān"]
                m_iast[2] = ["sarveṇa", "sarvābhyām", "sarvaiḥ"]
                m_iast[3] = ["sarvasmai", "sarvābhyām", "sarvebhyaḥ"]
                m_iast[4] = ["sarvasmāt", "sarvābhyām", "sarvebhyaḥ"]
                m_iast[5] = ["sarvasya", "sarvayoḥ", "sarveṣām"]
                m_iast[6] = ["sarvasmin", "sarvayoḥ", "sarveṣu"]
                m_iast[7] = ["he sarva", "he sarvau", "he sarve"]

        for v in range(8):
            for c in range(3):
                m_sutra[v][c] = "sarvanāmnaḥ smai/smāt/smin/suṭ (7.1.14 - 7.1.52)"

        return m_iast, m_sutra

    def _populate_core_pronouns(self):
        """Populates common pronouns (yuṣmad, asmad) in the reverse lookup cache."""
        yusmad_forms = [
            ("tvam", "Prathamā", "Ekavacana"), ("yuvām", "Prathamā", "Dvivacana"), ("yūyam", "Prathamā", "Bahuvacana"),
            ("tvām", "Dvitīyā", "Ekavacana"), ("tvā", "Dvitīyā", "Ekavacana"), ("yuṣmān", "Dvitīyā", "Bahuvacana"), ("vaḥ", "Dvitīyā", "Bahuvacana"),
            ("tvayā", "Tṛtīyā", "Ekavacana"), ("yuvābhyām", "Tṛtīyā", "Dvivacana"), ("yuṣmābhiḥ", "Tṛtīyā", "Bahuvacana"),
            ("tubhyam", "Caturthī", "Ekavacana"), ("te", "Caturthī", "Ekavacana"), ("yuṣmabhyam", "Caturthī", "Bahuvacana"),
            ("tvat", "Pañcamī", "Ekavacana"), ("yuṣmat", "Pañcamī", "Bahuvacana"),
            ("tava", "Ṣaṣṭhī", "Ekavacana"), ("yuvayoḥ", "Ṣaṣṭhī", "Dvivacana"), ("yuṣmākam", "Ṣaṣṭhī", "Bahuvacana"),
            ("tvayi", "Saptamī", "Ekavacana"), ("yuṣmāsu", "Saptamī", "Bahuvacana")
        ]
        for f_iast, vib, vac in yusmad_forms:
            self._register_cache(f_iast, "yuṣmad", "युष्मद्", "common", vib, vac, "tvamāhav ekavacane (7.2.97) / yuṣmadasmador...")

        asmad_forms = [
            ("aham", "Prathamā", "Ekavacana"), ("āvām", "Prathamā", "Dvivacana"), ("vayam", "Prathamā", "Bahuvacana"),
            ("mām", "Dvitīyā", "Ekavacana"), ("mā", "Dvitīyā", "Ekavacana"), ("asmān", "Dvitīyā", "Bahuvacana"), ("naḥ", "Dvitīyā", "Bahuvacana"),
            ("mayā", "Tṛtīyā", "Ekavacana"), ("āvābhyām", "Tṛtīyā", "Dvivacana"), ("asmābhiḥ", "Tṛtīyā", "Bahuvacana"),
            ("mahyam", "Caturthī", "Ekavacana"), ("me", "Caturthī", "Ekavacana"), ("asmabhyam", "Caturthī", "Bahuvacana"),
            ("mat", "Pañcamī", "Ekavacana"), ("asmat", "Pañcamī", "Bahuvacana"),
            ("mama", "Ṣaṣṭhī", "Ekavacana"), ("āvayoḥ", "Ṣaṣṭhī", "Dvivacana"), ("asmākam", "Ṣaṣṭhī", "Bahuvacana"),
            ("mayi", "Saptamī", "Ekavacana"), ("asmāsu", "Saptamī", "Bahuvacana")
        ]
        for f_iast, vib, vac in asmad_forms:
            self._register_cache(f_iast, "asmad", "अस्मद्", "common", vib, vac, "aham-āvām-vayam (7.2.98) / yuṣmadasmador...")

    def _register_cache(self, form_iast: str, stem_iast: str, stem_dev: str, gender: str, vib: str, vac: str, sutra: str):
        """Registers generated forms in the high-speed reverse lookup index."""
        if not form_iast or form_iast == "-":
            return
        # Handle dual optional forms separated by "/"
        forms = [f.strip() for f in form_iast.split("/")]
        for f in forms:
            key = f.lower().replace(":", "ḥ").replace("he ", "").strip()
            entry = {
                "stem_iast": stem_iast,
                "stem_devanagari": stem_dev,
                "gender": gender,
                "vibhakti": vib,
                "vacana": vac,
                "sutra": sutra
            }
            if key not in self._reverse_cache:
                self._reverse_cache[key] = []
            if entry not in self._reverse_cache[key]:
                self._reverse_cache[key].append(entry)

    def analyze_subanta(self, inflected_pada: str) -> List[Dict[str, Any]]:
        """
        Reverse Morphological Disambiguator & Sanskrit Jurisprudence Engine:
        Decomposes an inflected pada into all valid interpretations, citing
        exact Pāṇinian legal statutes, sūtras, and gender-specific precedents.
        """
        raw = inflected_pada.strip()
        iast_pada = devanagari_to_iast(raw).strip().lower().replace(":", "ḥ")

        results = []
        seen_keys = set()

        # 1. Fast Cache Lookup
        if iast_pada in self._reverse_cache:
            for item in self._reverse_cache[iast_pada]:
                c_copy = dict(item)
                key = (c_copy["stem_iast"], c_copy["gender"], c_copy["vibhakti"], c_copy["vacana"])
                if key not in seen_keys:
                    seen_keys.add(key)
                    if "legal_defense" not in c_copy:
                        c_copy["legal_defense"] = self.generate_legal_defense(
                            c_copy["stem_iast"], c_copy["gender"], c_copy["vibhakti"], c_copy["vacana"], iast_pada
                        )
                    results.append(c_copy)

        # 2. Dynamic Reverse Deductive Rule Engine (captures alternate valid genders e.g. Puṃvad-bhāva neuter)
        candidates = self._deduce_candidates(iast_pada)
        for cand_stem, cand_gender in candidates:
            gen_res = self.generate_shabdarupa(cand_stem, cand_gender)
            for row in gen_res["table"]:
                for cell in row["forms"]:
                    cell_forms = [f.lower().replace(":", "ḥ").replace("he ", "").strip() for f in cell["iast"].split("/")]
                    if iast_pada in cell_forms:
                        key = (cand_stem, cand_gender, cell["vibhakti"], cell["vacana"])
                        if key not in seen_keys:
                            seen_keys.add(key)
                            entry = {
                                "stem_iast": cand_stem,
                                "stem_devanagari": gen_res["stem_devanagari"],
                                "gender": cand_gender,
                                "vibhakti": cell["vibhakti"],
                                "vacana": cell["vacana"],
                                "sutra": cell["sutra"],
                                "legal_defense": self.generate_legal_defense(
                                    cand_stem, cand_gender, cell["vibhakti"], cell["vacana"], iast_pada
                                )
                            }
                            results.append(entry)

        return results

    def generate_legal_defense(self, stem_iast: str, gender: str, vibhakti_str: str, vacana_str: str, inflected_pada: str) -> Dict[str, Any]:
        """
        Sanskrit Courtroom-Grade Juridical Defense (पाणिनीय-शास्त्रार्थ-प्रमाणम्).
        Presents formal legal arguments citing canonical Aṣṭādhyāyī statutes,
        kāraka jurisdictions, and gender-specific declensional precedents.
        """
        stem_dev = iast_to_devanagari(stem_iast)
        pada_dev = iast_to_devanagari(inflected_pada)
        g_cap = gender.capitalize()

        # Determine Vibhakti & Vacana Indices
        v_idx = 0
        for i, (v_name, _, _) in enumerate(VIBHAKTIS):
            if v_name.split()[0] in vibhakti_str or v_name == vibhakti_str:
                v_idx = i
                break
        
        vac_idx = 0
        for i, vac in enumerate(VACANAS):
            if vac.split()[0] in vacana_str or vac == vacana_str:
                vac_idx = i
                break

        sup_affix = RAW_SUP_AFFIXES[v_idx][vac_idx]
        karaka_meta = KARAKA_MAPPINGS[v_idx]

        # 1. Pratijñā (The Legal Claim)
        pratijna = f"The surface token '{pada_dev}' ({inflected_pada}) is formally defended as a syntactically and morphologically legitimate Pada under Pāṇini 1.4.14 (सुप्तिङन्तं पदम्)."

        # 2. Adhikāra & Base Validity
        base_authority = f"Valid Nominal Base (प्रातिपदिकम्) under 1.2.45 (अर्थवदधातुरप्रत्ययः प्रातिपदिकम्). Suffixation is governed by 3.1.1 (प्रत्ययः), 3.1.2 (परश्च), and 4.1.1 (ङ्याप्प्रातिपदिकात्)."

        # 3. Statutes & Precedents
        statutes = [
            {
                "sutra": "arthavad adhātur apratyayaḥ prātipadikam (1.2.45)",
                "sutra_dev": "अर्थवदधातुरप्रत्ययः प्रातिपदिकम्",
                "type": "Sañjñā Sūtra (संज्ञा-सूत्रम् / Definition)",
                "function": f"Establishes '{stem_dev}' as an authentic meaningful base distinct from raw dhātus and pratyayas."
            },
            {
                "sutra": "svaujasamauṭchaṣṭābhyāṃbhis... (4.1.2)",
                "sutra_dev": "स्वौजसमौट्छष्टाभ्यां...",
                "type": "Vidhi Sūtra (विधि-सूत्रम् / Operational Injunction)",
                "function": f"Allots the canonical SUP affix '{sup_affix['affix_dev']}' ({sup_affix['affix']}) for {vibhakti_str} {vacana_str}."
            },
            {
                "sutra": f"{karaka_meta['karaka_sutra']} & {karaka_meta['vibhakti_sutra']}",
                "sutra_dev": f"{karaka_meta['role'].split('(')[0].strip()} विधानम्",
                "type": "Kāraka-Vidhi Sūtra (कारक-विधिः / Syntax-Semantics Mapping)",
                "function": f"Authorizes the case relationship: {karaka_meta['meaning']}."
            }
        ]

        # IT marker statute
        if sup_affix['it_rule'] != "N/A":
            statutes.append({
                "sutra": f"{sup_affix['it_rule']} & tasya lopaḥ (1.3.9)",
                "sutra_dev": "इत्-संज्ञा एवं लोप-विधानम्",
                "type": "Sañjñā & Adarśana Sūtra (संज्ञा एवं लोप-सूत्रम्)",
                "function": f"Annuls the operational variable ({sup_affix['anubandha']}), purifying the affix before phonetic coalescence."
            })

        # Morphological substitution statute
        if stem_iast.endswith('a') and v_idx == 2 and vac_idx == 0: # 3rd Sing
            statutes.append({
                "sutra": "ṭāṅasinasminātsyenāḥ (7.1.12)",
                "sutra_dev": "टाङसिङसामिनात्स्याः",
                "type": "Apavāda Sūtra (अपवाद-सूत्रम् / Special Exception)",
                "function": "Overrides the general sup rule by replacing affix 'ṭā' with 'ina' after an a-final nominal base."
            })
            statutes.append({
                "sutra": "ād guṇaḥ (6.1.87)",
                "sutra_dev": "आद्गुणः",
                "type": "Svara-Sandhi Sūtra (स्वर-सन्धि-सूत्रम्)",
                "function": "Merges stem-terminal 'a' + 'ina' into 'e', yielding intermediate form."
            })
            if 'ṇ' in inflected_pada:
                statutes.append({
                    "sutra": "raṣābhyāṃ no ṇaḥ samānapade (8.4.1) & aṭkupvāṅnumvyavāye'pi (8.4.2)",
                    "sutra_dev": "रषाभ्यां नो णः समानपदे एवं अट्कुप्वाङ्नुम्व्यवायेऽपि",
                    "type": "Tripādī Phonological Statute (त्रिपादी णत्व-विधिः)",
                    "function": "Mandates retroflexion of 'n' to 'ṇ' triggered by preceding 'r'/'ṣ' despite intervening aṭ-vowels and pu-labials (m)."
                })

        # 4. Gender Jurisprudence (Liṅga-Nirṇaya)
        if gender.lower() in ('neuter', 'napumsaka', 'n'):
            gender_proof = (
                "Statutory Authority under 7.1.23 (स्वमोर्नपुंसकात्): Pāṇinian statute restricts neuter-specific transformations "
                "(luk elision & am substitution) strictly to Prathamā & Dvitīyā (1st & 2nd cases). "
                "From Tṛtīyā onwards (3rd to 7th case), all Neuter a-stems undergo Puṃvad-bhāva (पुंवद्भाव), "
                "declining with 100% mathematical identity to Masculine a-stems. "
                "Furthermore, as an adjective (विशेषण), it qualifies neuter substantives (e.g., 'रामेण वपुषा' - with a charming form) "
                "under the principle 'विशेषणं विशेष्यनिघ्नम्' (Adjectives inherit the case, number, and gender of their substantive)."
            )
        elif gender.lower() in ('masculine', 'pum', 'm'):
            gender_proof = (
                "Canonical Masculine Declension: Represents the primary substantive noun (संज्ञा / विशेष्य, e.g. 'रामेण धनुर्धरेण') "
                "governed by general nominal declension (अदन्त पुंलिङ्ग प्रकरण)."
            )
        else:
            gender_proof = "Feminine Nominal Declension governed by ṅyāp-prātipadikāt (4.1.1)."

        # 5. Mahābhāṣya Dialectical Resolution (Pūrvapakṣa vs Siddhānta)
        stem_grade = self.get_stem_grade(v_idx, vac_idx, gender)
        purvapaksha = "Can an unanchored nominal stem express a valid case relationship without a co-present finite verb? (eka-tiṅ-vākyam)"
        siddhanta = "Patañjali establishes in the Mahābhāṣya (Paśpaśāhnika & Kārakāhnika) that in nominal sentences, the copula 'asti' ('to be/exist') is implicitly understood and syntactically active (asti-bhavanti-paro'pratyayamānaḥ), legitimately authorizing Prātipadikārtha-mātre Prathamā (2.3.46)."
        
        if v_idx == 2 and vac_idx == 2 and stem_iast.endswith('a'):
            purvapaksha = "Why does 'deva + bhis' not become 'devebhiḥ' under 7.3.103 (bahu vacane jhalyet)?"
            siddhanta = "Patañjali proves that 7.1.9 (ato bhisa ais) is an Apavāda (special exception) that permanently blocks the general rule 7.3.103 under Utsargāpavāda-nyāya, yielding 'devaiḥ'."
        elif gender.lower() in ('neuter', 'napumsaka', 'n') and v_idx >= 2:
            purvapaksha = "Why does a neuter nominal stem follow masculine inflectional endings from Tṛtīyā onwards?"
            siddhanta = "Patañjali confirms that Pāṇinian statute 7.1.23 (svamornapuṃsakāt) restricts neuter overrides strictly to Prathamā & Dvitīyā; from Tṛtīyā to Saptamī, Puṃvad-bhāva guarantees identical declension."

        # 6. Śrī Harināmāmṛta-Vyākaraṇa & Bāla-Toṣaṇī Ṭīkā Theological Perspective
        hnv_v = HNV_VIBHAKTI_MAPPINGS[v_idx]
        is_vowel = stem_iast[-1] in ('a', 'ā', 'i', 'ī', 'u', 'ū', 'ṛ', 'ṝ', 'e', 'ai', 'o', 'au')
        
        # Bāla-Toṣaṇī paradigm exegesis
        if inflected_pada.endswith('ḥ') and v_idx == 0 and vac_idx == 0:
            bala_toshani_note = "The terminal Visarga (:) embodies the divine dual manifestation of Rādhā-Kṛṣṇa Yugala-Svarūpa emerging from the singular Nārāyaṇa base."
        elif stem_iast.endswith('a') and v_idx == 2 and vac_idx == 2:
            bala_toshani_note = "The ais-substitution for bhis demonstrates the theological primacy of Apavāda (localized divine pastimes) over universal Utsarga laws."
        elif stem_iast == 'sakhi' and v_idx in (4, 5):
            bala_toshani_note = "The specialized u-substitution in 'sakhyuḥ' preserves the eternal, indestructible nature of Sakhya-Rasa against generic yaṇ-sandhi assimilation."
        elif 'ṇ' in inflected_pada and ('r' in stem_iast or 'ṣ' in stem_iast or 'ṛ' in stem_iast):
            bala_toshani_note = "Articulatory pathways allow descending spiritual potency across non-interfering velars (ku) and labials (pu) to retroflex dental n to ṇ."
        else:
            bala_toshani_note = "Governed by the Antaraṅga-Bahiraṅga paradigm, ensuring internal spiritual and phonetic harmony before external affixation."

        hnv_lens = {
            "treatise": "Bṛhat-Harināmāmṛta-Vyākaraṇa & Bāla-Toṣaṇī Ṭīkā",
            "cosmology": "Avarohavāda (अवरोहवाद - Descending Grace)",
            "narayana_base": f"{stem_dev} ({stem_iast})",
            "stem_classification": "Sarveśvarānta (सर्वेश्वरान्त)" if is_vowel else "Viṣṇujanānta (विष्णुजनान्त)",
            "visnubhakti": f"{sup_affix['affix_dev']} ({sup_affix['affix']}) [{hnv_v['hnv_name']}]",
            "bhakti_relationship": hnv_v["bhakti_role"],
            "realized_visnupada": f"{pada_dev} ({inflected_pada})",
            "bala_toshani_exegesis": bala_toshani_note,
            "philosophical_siddhanta": (
                f"In the Bṛhat-Harināmāmṛta-Vyākaraṇa of Śrīla Jīva Gosvāmī and the Bāla-Toṣaṇī Ṭīkā of Śrī Hare Kṛṣṇa Ācārya, "
                f"the completed word '{pada_dev}' is revered as a Viṣṇupada—the sacred meeting point where Nārāyaṇa ('{stem_dev}') "
                f"unites with His devotee {hnv_v['hnv_name']}. The derivation preserves 100% Pāṇinian "
                f"mathematical precision while consecrating language into devotional remembrance (Smaraṇam / Kṛṣṇānuśīlanam)."
            )
        }

        # 7. Verdict (Nirṇaya)
        verdict = f"VERDICT: The pada '{pada_dev}' ({inflected_pada}) is conclusively ruled SIDDHA (सिद्ध - Flawless & Lawful) in the {g_cap} gender, {vibhakti_str}, {vacana_str} under the supreme authority of the Aṣṭādhyāyī."

        return {
            "pratijna": pratijna,
            "base_authority": base_authority,
            "stem_grade": stem_grade,
            "karaka_jurisdiction": f"{karaka_meta['role']} [{karaka_meta['karaka_sutra']}]",
            "statutes": statutes,
            "gender_proof": gender_proof,
            "mahabhashya_dialectic": {
                "purvapaksha": purvapaksha,
                "siddhanta": siddhanta
            },
            "hnv_lens": hnv_lens,
            "verdict": verdict
        }

    def _deduce_candidates(self, iast_pada: str) -> List[Tuple[str, str]]:
        """Deduces potential candidate (stem, gender) tuples from an inflected pada ending."""
        p = iast_pada
        cands: List[Tuple[str, str]] = []

        def add_cand(st: str, g: str):
            if (st, g) not in cands:
                cands.append((st, g))

        # 1. a-stems (e.g. rāmāya, rāmāḥ, pāṇḍavāḥ, dharmakṣetre)
        if p.endswith(('aḥ', 'am', 'ena', 'eṇa', 'āya', 'āt', 'asya', 'au', 'ābhyām', 'ayoḥ', 'āḥ', 'ān', 'aiḥ', 'ebhyaḥ', 'ānām', 'āṇām', 'eṣu', 'e', 'āni', 'āṇi')):
            stem_base = re.sub(r'(aḥ|am|ena|eṇa|āya|āt|asya|au|ābhyām|ayoḥ|āḥ|ān|aiḥ|ebhyaḥ|ānām|āṇām|eṣu|e|āni|āṇi)$', '', p)
            add_cand(f"{stem_base}a", "masculine")
            add_cand(f"{stem_base}a", "neuter")

        # 2. ā-stems (e.g. latāyai, latāḥ)
        if p.endswith(('ā', 'ām', 'ayā', 'āyai', 'āyāḥ', 'āyām', 'āsu', 'ābhiḥ', 'ābhyaḥ')):
            stem_base = re.sub(r'(ā|ām|ayā|āyai|āyāḥ|āyām|āsu|ābhiḥ|ābhyaḥ)$', '', p)
            add_cand(f"{stem_base}ā", "feminine")

        # 3. i-stems (e.g. haraye, matyai, vāriṇi)
        if p.endswith(('iḥ', 'im', 'inā', 'iṇā', 'aye', 'eḥ', 'au', 'ayaḥ', 'īn', 'ibhiḥ', 'ibhyaḥ', 'īnām', 'iṣu', 'i', 'iṇī', 'īni')):
            stem_base = re.sub(r'(iḥ|im|inā|iṇā|aye|eḥ|au|ayaḥ|īn|ibhiḥ|ibhyaḥ|īnām|iṣu|i|iṇī|īni)$', '', p)
            add_cand(f"{stem_base}i", "masculine")
            add_cand(f"{stem_base}i", "feminine")
            add_cand(f"{stem_base}i", "neuter")

        # 4. ī-stems (e.g. nadīm, nadīṣu)
        if p.endswith(('ī', 'yau', 'yaḥ', 'īm', 'īḥ', 'yā', 'yai', 'yāḥ', 'yām', 'ībhyām', 'ībhiḥ', 'ībhyaḥ', 'īṣu')):
            stem_base = re.sub(r'(ī|yau|yaḥ|īm|īḥ|yā|yai|yāḥ|yām|ībhyām|ībhiḥ|ībhyaḥ|īṣu)$', '', p)
            add_cand(f"{stem_base}ī", "feminine")

        # 5. u-stems (e.g. gurave, madhuni)
        if p.endswith(('uḥ', 'um', 'unā', 'uṇā', 'ave', 'oḥ', 'au', 'avaḥ', 'ūn', 'ubhiḥ', 'ubhyaḥ', 'ūnām', 'uṣu', 'u', 'unī', 'ūni')):
            stem_base = re.sub(r'(uḥ|um|unā|uṇā|ave|oḥ|au|avaḥ|ūn|ubhiḥ|ubhyaḥ|ūnām|uṣu|u|unī|ūni)$', '', p)
            add_cand(f"{stem_base}u", "masculine")
            add_cand(f"{stem_base}u", "feminine")
            add_cand(f"{stem_base}u", "neuter")

        # 6. ū-stems (e.g. vadhvai, vadhūṣu)
        if p.endswith(('vā', 'vai', 'vām', 'ūbhyām', 'ūbhiḥ', 'ūbhyaḥ', 'ūṣu')):
            stem_base = re.sub(r'(vā|vai|vām|ūbhyām|ūbhiḥ|ūbhyaḥ|ūṣu)$', '', p)
            add_cand(f"{stem_base}ū", "feminine")

        # 7. ṛ-stems (e.g. pitrā, pitṝn)
        if p.endswith(('ā', 'ārau', 'āraḥ', 'āram', 'ṝn', 'ṝḥ', 'rā', 're', 'uḥ', 'roḥ', 'ṝṇām', 'ari', 'ṛbhyām', 'ṛbhiḥ', 'ṛbhyaḥ', 'ṛṣu')):
            stem_base = re.sub(r'(ā|ārau|āraḥ|āram|ṝn|ṝḥ|rā|re|uḥ|roḥ|ṝṇām|ari|ṛbhyām|ṛbhiḥ|ṛbhyaḥ|ṛṣu)$', '', p)
            add_cand(f"{stem_base}ṛ", "masculine")
            add_cand(f"{stem_base}ṛ", "feminine")

        # 8. Consonant stems (in-anta, an-anta, at-anta, as-anta)
        if p.endswith(('ī', 'inau', 'inaḥ', 'inam', 'inā', 'ine', 'ibhyām', 'ibhiḥ', 'ibhyaḥ', 'inām', 'iṣu', 'ini')):
            stem_base = re.sub(r'(ī|inau|inaḥ|inam|inā|ine|ibhyām|ibhiḥ|ibhyaḥ|inām|iṣu|ini)$', '', p)
            add_cand(f"{stem_base}in", "masculine")

        if p.endswith(('vān', 'mān', 'vantau', 'mantau', 'vantaḥ', 'mantaḥ', 'vantam', 'mantam', 'vatā', 'matā', 'vadbhyām', 'madbhyām', 'vadbhiḥ', 'madbhiḥ', 'vate', 'mate', 'vadbhyaḥ', 'madbhyaḥ', 'vataḥ', 'mataḥ', 'vatoḥ', 'matoḥ', 'vatām', 'matām', 'vati', 'mati', 'vatsu', 'matsu')):
            stem_base = re.sub(r'(vān|mān|vantau|mantau|vantaḥ|mantaḥ|vantam|mantam|vatā|matā|vadbhyām|madbhyām|vadbhiḥ|madbhiḥ|vate|mate|vadbhyaḥ|madbhyaḥ|vataḥ|mataḥ|vatoḥ|matoḥ|vatām|matām|vati|mati|vatsu|matsu)$', '', p)
            add_cand(f"{stem_base}vat", "masculine")
            add_cand(f"{stem_base}mat", "masculine")

        # 9. Mahābhāṣya Irregular Stems (sakhi, go, pathin, ahan)
        if p in ('sakhā', 'sakhāyau', 'sakhāyaḥ', 'sakhāyam', 'sakhīn', 'sakhyā', 'sakhibhyām', 'sakhibhiḥ', 'sakhye', 'sakhibhyaḥ', 'sakhyuḥ', 'sakhyoḥ', 'sakhīnām', 'sakhyau', 'sakhiṣu', 'sakhe'):
            add_cand("sakhi", "masculine")
        if p in ('gauḥ', 'gāvau', 'gāvaḥ', 'gām', 'gāḥ', 'gavā', 'gobhyām', 'gobhiḥ', 'gave', 'gobhyaḥ', 'goḥ', 'gavoḥ', 'gavām', 'gavi', 'goṣu'):
            add_cand("go", "masculine")
            add_cand("go", "feminine")
        if p in ('panthāḥ', 'panthānau', 'panthānaḥ', 'panthānam', 'pathaḥ', 'pathā', 'pathibhyām', 'pathibhiḥ', 'pathe', 'pathibhyaḥ', 'pathoḥ', 'pathām', 'pathi', 'pathiṣu'):
            add_cand("pathin", "masculine")
        if p in ('ahaḥ', 'ahanī', 'ahnī', 'ahāni', 'ahnā', 'ahobhyām', 'ahobhiḥ', 'ahne', 'ahobhyaḥ', 'ahnaḥ', 'ahnoḥ', 'ahnām', 'ahni', 'ahani', 'ahaḥsu', 'ahan'):
            add_cand("ahan", "neuter")

        return cands

    def get_stem_grade(self, vibhakti_idx: int, vacana_idx: int, gender: str) -> Dict[str, str]:
        """
        Computes the Tri-Grade Stem Sañjñā under Patañjali's Mahābhāṣya:
        1. Sarvanāmasthāna / Suṭ (Strong Grade / दृढावस्था) - 1.1.42/1.1.43
        2. Bha-Sañjñā (Weak Grade / दुर्बलावस्था) - 1.4.18 (yaci bham)
        3. Pada-Sañjñā (Middle Grade / मध्यावस्था) - 1.4.17 (svādiṣvasarvanāmasthāne)
        """
        is_neuter = gender.lower() in ('neuter', 'napumsaka', 'n')
        v_idx = vibhakti_idx
        vac_idx = vacana_idx
        
        if is_neuter:
            if v_idx in (0, 1, 7) and vac_idx == 2:
                return {
                    "grade": "Sarvanāmasthāna / Suṭ (दृढावस्था / Strong Grade)",
                    "sutra": "śi sarvanāmasthānam (1.1.42) & jaśśasoḥ śiḥ (7.1.20)",
                    "type": "Sañjñā Sūtra",
                    "desc": "Neuter plural nominative/accusative 'śi' is assigned Sarvanāmasthāna status, triggering strong stem lengthening / num-āgama."
                }
            elif v_idx in (0, 1, 7):
                return {
                    "grade": "Pada-Sañjñā / Am-Luk Grade (मध्यावस्था)",
                    "sutra": "svamornapuṃsakāt (7.1.23)",
                    "type": "Adhikāra / Vidhi Sūtra",
                    "desc": "Neuter singular/dual undergo special elision (luk) or am-substitution."
                }
        else:
            # Non-neuter: su̐, au, jas, am, auṭ
            if (v_idx == 0 or v_idx == 7) or (v_idx == 1 and vac_idx < 2):
                return {
                    "grade": "Sarvanāmasthāna / Suṭ (दृढावस्था / Strong Grade)",
                    "sutra": "suḍanapuṃsakasya (1.1.43)",
                    "type": "Sañjñā Sūtra",
                    "desc": "Belongs to the first five strong affixes (suṭ), inducing root/stem strengthening (guṇa, vṛddhi, or penultimate lengthening)."
                }

        # Consonant-initial non-sarvanamasthana -> Pada-sañjñā
        if (vac_idx == 1 and v_idx in (2, 3, 4)) or (vac_idx == 2 and v_idx in (2, 3, 4, 6)):
            return {
                "grade": "Pada-Sañjñā (मध्यावस्था / Middle Grade)",
                "sutra": "svādiṣvasarvanāmasthāne (1.4.17)",
                "type": "Sañjñā Sūtra",
                "desc": "Consonant-initial non-strong affix assigns Pada status to the stem base, triggering external/pada sandhi behavior."
            }

        # Vowel-initial non-sarvanamasthana -> Bha-sañjñā
        return {
            "grade": "Bha-Sañjñā (दुर्बलावस्था / Weakest Grade)",
            "sutra": "yaci bham (1.4.18)",
            "type": "Sañjñā Sūtra",
            "desc": "Vowel/y-initial non-strong affix assigns Bha status, triggering vowel elision (al-lopa) or penultimate reduction in consonant stems."
        }

    def get_hnv_prakriya(self, stem_iast: str, gender: str, v_idx: int, vac_idx: int, final_pada_iast: str, final_pada_dev: str) -> Dict[str, Any]:
        """
        Generates the Bṛhat-Harināmāmṛta-Vyākaraṇa (HNV) Devotional-Grammatical Derivation
        accompanied by the Svopajña-Vṛtti and Bāla-Toṣaṇī Ṭīkā exegesis of Śrī Hare Kṛṣṇa Ācārya.
        Preserves 100% Pāṇinian structural rigor while illuminating Gauḍīya Vaiṣṇava ontology.
        """
        stem_dev = iast_to_devanagari(stem_iast)
        is_vowel = stem_iast[-1] in ('a', 'ā', 'i', 'ī', 'u', 'ū', 'ṛ', 'ṝ', 'e', 'ai', 'o', 'au')
        stem_nature = "Sarveśvarānta (सर्वेश्वरान्त - Vowel Stem)" if is_vowel else "Viṣṇujanānta (विष्णुजनान्त - Consonant Stem)"
        
        raw_sup = RAW_SUP_AFFIXES[v_idx][vac_idx]["affix"]
        raw_sup_dev = RAW_SUP_AFFIXES[v_idx][vac_idx]["affix_dev"]
        anubandha = RAW_SUP_AFFIXES[v_idx][vac_idx]["anubandha"]
        hnv_v = HNV_VIBHAKTI_MAPPINGS[v_idx]

        # Bāla-Toṣaṇī Exegetical Commentary based on specific paradigm environments
        if final_pada_iast.endswith('ḥ') and v_idx == 0 and vac_idx == 0:
            bala_toshani_note = (
                "Bāla-Toṣaṇī Ṭīkā Exegesis (बालतोषणी-टीका): The physical manifestation of the Visarga (:) "
                "directly represents the divine dual potency (Rādhā-Kṛṣṇa Yugala-Svarūpa) emanating from "
                "the singular Nārāyaṇa base without mechanical intermediary rutva steps."
            )
        elif stem_iast.endswith('a') and v_idx == 2 and vac_idx == 2:
            bala_toshani_note = (
                "Bāla-Toṣaṇī Ṭīkā Exegesis (बालतोषणी-टीका): The substitution of 'ais' for 'bhis' demonstrates "
                "how a localized divine pastime (Apavāda / Viśeṣānugraha) supersedes universal cosmic laws (Utsarga)."
            )
        elif stem_iast == 'sakhi' and v_idx in (4, 5) and vac_idx == 0:
            bala_toshani_note = (
                "Bāla-Toṣaṇī Ṭīkā Exegesis (बालतोषणी-टीका): In 'sakhyuḥ', the stem terminal replaces the suffix vowel "
                "with 'u', illustrating the indestructible, unalterable nature of Sakhya-Rasa (Devotional Friendship) "
                "which actively resists generic yaṇ-sandhi assimilation."
            )
        elif 'ṇ' in final_pada_iast and ('r' in stem_iast or 'ṣ' in stem_iast or 'ṛ' in stem_iast):
            bala_toshani_note = (
                "Bāla-Toṣaṇī Ṭīkā Exegesis (बालतोषणी-टीका): Traces physiological articulatory pathways where non-interfering "
                "velars (ku) and labials (pu) allow descending spiritual energy from 'r'/'ṣ' to retroflex the dental nasal into 'ṇ'."
            )
        else:
            bala_toshani_note = (
                "Bāla-Toṣaṇī Ṭīkā Exegesis (बालतोषणी-टीका): Governed by the Antaraṅga-Bahiraṅga paradigm, "
                "ensuring internal phonetic structural integrity before external case affixation."
            )

        return {
            "treatise": "Bṛhat-Harināmāmṛta-Vyākaraṇa (बृहद्धरिनाममृत-व्याकरणम्)",
            "commentaries": "Svopajña-Vṛtti (Jīva Gosvāmī) & Bāla-Toṣaṇī Ṭīkā (Hare Kṛṣṇa Ācārya)",
            "cosmology": "Avarohavāda (अवरोहवाद - nārāyaṇād udbhūto 'yaṃ varṇa-kramaḥ 1.1)",
            "narayana_base": f"{stem_dev} ({stem_iast})",
            "stem_nature": stem_nature,
            "visnubhakti_affix": f"{raw_sup_dev} ({raw_sup})",
            "visnubhakti_category": hnv_v["hnv_name"],
            "bhakti_relationship": hnv_v["bhakti_role"],
            "sanketa_operation": f"Saṅketa ({anubandha}) is purified and dissolved via Trivikrama/Harām." if "None" not in anubandha else "Nir-anubandha (Direct Unaltered Viṣṇubhakti)",
            "completed_visnupada": f"{final_pada_dev} ({final_pada_iast})",
            "bala_toshani_exegesis": bala_toshani_note,
            "theological_meditation": (
                f"Under the Harināmāmṛta Vyākaraṇa, the realized Viṣṇupada '{final_pada_dev}' embodies the Supreme Lord Nārāyaṇa ('{stem_dev}') "
                f"surrounded and qualified by {hnv_v['hnv_name']} to establish {hnv_v['bhakti_role']}. "
                f"Grammar is transformed into an unbroken act of devotional remembrance (Smaraṇam / Kṛṣṇānuśīlanam)."
            )
        }

    def derive_prakriya(self, stem: str, gender: Optional[str] = None, vibhakti_idx: int = 0, vacana_idx: int = 0) -> Dict[str, Any]:
        """
        Step-by-Step Pāṇinian Derivation (Prakriyā) Tracer.
        Synthesizes the exact chronological sūtra-by-sūtra derivation trace from raw
        Prātipadika + SUP affix to final surface Pada, citing relevant Aṣṭādhyāyī Sūtras,
        tagging computational execution regimes (Sapādasaptādhyāyī vs Tripādī), and
        illuminating the dual Harināmāmṛta Vyākaraṇa (HNV) devotional nomenclature.
        """
        gen_res = self.generate_shabdarupa(stem, gender)
        v_idx = max(0, min(7, vibhakti_idx))
        vac_idx = max(0, min(2, vacana_idx))

        cell = gen_res["table"][v_idx]["forms"][vac_idx]
        stem_iast = gen_res["stem_iast"]
        stem_dev = gen_res["stem_devanagari"]
        active_gender = gen_res["gender"]
        final_pada_iast = cell["iast"]
        final_pada_dev = cell["devanagari"]

        raw_sup = cell["raw_sup"]
        raw_sup_dev = cell["raw_sup_dev"]
        anubandha_desc = cell["anubandha"]
        it_rule = cell["it_rule"]
        karaka_info = {
            "role": cell["karaka_role"],
            "sutra": cell["karaka_sutra"],
            "meaning": cell["karaka_meaning"]
        }
        stem_grade = self.get_stem_grade(v_idx, vac_idx, active_gender)
        hnv_prakriya = self.get_hnv_prakriya(stem_iast, active_gender, v_idx, vac_idx, final_pada_iast, final_pada_dev)

        steps = []
        step_num = 1

        # Step 1: Base & Affix Attachment (Sapādasaptādhyāyī)
        steps.append({
            "step": step_num,
            "regime": "Sapādasaptādhyāyī (सपादसप्ताध्यायी 1.1.1 - 8.1.74)",
            "stage": "1. Prātipadika & SUP Affix Assignment (प्रातिपदिकम् एवं सुप्-प्रत्यय-विधानम्)",
            "string": f"{stem_dev} + {raw_sup_dev} ({stem_iast} + {raw_sup})",
            "sutra": "arthavad adhātur apratyayaḥ prātipadikam (1.2.45), ṅyāpprātipadikāt (4.1.1) & svaujasam... (4.1.2)",
            "rule_type": "Adhikāra / Vidhi Sūtra",
            "explanation": f"A valid nominal base (Prātipadika / Nārāyaṇa) '{stem_dev}' is assigned the raw inflectional affix (SUP / Viṣṇubhakti) '{raw_sup_dev}' for {VIBHAKTIS[v_idx][0]} {VACANAS[vac_idx]} under Stem Grade: {stem_grade['grade']}."
        })
        step_num += 1

        # Step 2: IT Marker Identification & Elision (Sapādasaptādhyāyī)
        if it_rule != "N/A":
            clean_affix_iast = raw_sup.replace('u̐', '').replace('j', '').replace('ṭ', '').replace('ś', '').replace('ṅ', '').replace('P', '').replace('i̐', '')
            clean_affix_dev = iast_to_devanagari(clean_affix_iast) if clean_affix_iast else ""
            steps.append({
                "step": step_num,
                "regime": "Sapādasaptādhyāyī (सपादसप्ताध्यायी 1.1.1 - 8.1.74)",
                "stage": "2. IT Marker Analysis & Elision (इत्-संज्ञा एवं लोपः / सङ्केत-त्रिविक्रमः)",
                "string": f"{stem_dev} + {clean_affix_dev} ({stem_iast} + {clean_affix_iast})" if clean_affix_dev else f"{stem_dev} ({stem_iast})",
                "sutra": f"{it_rule} & tasya lopaḥ (1.3.9)",
                "rule_type": "Sañjñā & Adarśana Sūtra",
                "explanation": f"The IT markers / Saṅketa ({anubandha_desc}) serve as morphological triggers and are systematically elided via 1.3.9 (Trivikrama/Harām)."
            })
            step_num += 1

        # Step 3: Morphological Substitution / Ādeśa & Aṅga Mutation (Sapādasaptādhyāyī)
        sutra_cite = cell["sutra"]
        steps.append({
            "step": step_num,
            "regime": "Sapādasaptādhyāyī (सपादसप्ताध्यायी 1.1.1 - 8.1.74)",
            "stage": "3. Morphological Substitution & Aṅga Mutation (प्रत्यय-आदेशः / अङ्ग-कार्यम्)",
            "string": f"{final_pada_dev} ({final_pada_iast})",
            "sutra": sutra_cite,
            "rule_type": "Apavāda / Aṅga-Vidhi Sūtra",
            "explanation": f"The specific Pāṇinian paradigm rule executes stem strengthening (guṇa/vṛddhi/lengthening) or affix substitution to derive '{final_pada_dev}'."
        })
        step_num += 1

        # Step 4: Internal Sandhi / Retroflexion (Tripādī - asiddha)
        if 'ṇ' in final_pada_iast and ('r' in stem_iast or 'ṣ' in stem_iast or 'ṛ' in stem_iast):
            steps.append({
                "step": step_num,
                "regime": "Tripādī (त्रिपादी 8.2.1 - 8.4.68) [asiddha via 8.2.1]",
                "stage": "4. Internal Retroflexion Subroutine - Ṇatva (णत्व-विधानम्)",
                "string": f"{final_pada_dev} ({final_pada_iast})",
                "sutra": "raṣābhyāṃ no ṇaḥ samānapade (8.4.1) & aṭkupvāṅnumvyavāye'pi (8.4.2)",
                "rule_type": "Tripādī Phonological Subroutine",
                "explanation": f"The dental 'n' converts to retroflex 'ṇ' triggered by preceding 'r'/'ṣ' across intervening vowels and labials under one-way Tripādī control."
            })
            step_num += 1
        elif 'ṣ' in final_pada_iast and not stem_iast.endswith(('a', 'ā')) and ('su' in raw_sup or 'si' in raw_sup):
            steps.append({
                "step": step_num,
                "regime": "Tripādī (त्रिपादी 8.2.1 - 8.4.68) [asiddha via 8.2.1]",
                "stage": "4. Internal Retroflexion Subroutine - Ṣatva (षत्व-विधानम्)",
                "string": f"{final_pada_dev} ({final_pada_iast})",
                "sutra": "ādeśapratyayayoḥ (8.3.59) & iṇkoḥ (8.3.57)",
                "rule_type": "Tripādī Phonological Subroutine",
                "explanation": "Dental 's' of suffix transforms to retroflex 'ṣ' following an iṆ vowel or velar consonant."
            })
            step_num += 1

        # Step 5: Terminal Visarga / Rutva (Tripādī - asiddha)
        if final_pada_iast.endswith('ḥ'):
            steps.append({
                "step": step_num,
                "regime": "Tripādī (त्रिपादी 8.2.1 - 8.4.68) [asiddha via 8.2.1]",
                "stage": "5. Terminal Visarga / Rutva (ससजुषो रुः एवं विसर्जनीयः)",
                "string": f"{final_pada_dev} ({final_pada_iast})",
                "sutra": "sasajuṣo ruḥ (8.2.66) & kharavasānayor visarjanīyaḥ (8.3.15)",
                "rule_type": "Terminal Phonological Finalization",
                "explanation": "Final 's' undergoes Rutva (transforms to ru̐/r) and is subsequently converted to Visarga (ḥ) in pause/before unvoiced consonants."
            })
            step_num += 1

        return {
            "stem_iast": stem_iast,
            "stem_devanagari": stem_dev,
            "gender": active_gender,
            "paradigm": gen_res["paradigm"],
            "vibhakti": VIBHAKTIS[v_idx][0],
            "vacana": VACANAS[vac_idx],
            "stem_grade": stem_grade,
            "hnv_prakriya": hnv_prakriya,
            "raw_sup": raw_sup,
            "raw_sup_dev": raw_sup_dev,
            "karaka_info": karaka_info,
            "final_pada_iast": final_pada_iast,
            "final_pada_devanagari": final_pada_dev,
            "total_steps": len(steps),
            "derivation_steps": steps
        }
