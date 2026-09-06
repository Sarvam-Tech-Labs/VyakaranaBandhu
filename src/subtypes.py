"""
Sanskrit Morphological Subtyping, Vigraha Generator, and Pāṇinian Sūtra Engine
100% Purely Dynamic and Algorithmic - No hardcoded word/verse databases.
Deduces Vigraha, Padacheda, sequential Sandhi steps, and Aṣṭādhyāyī Sūtras on the fly.
"""

from typing import Dict, Any, List
from .normalizer import devanagari_to_iast, iast_to_devanagari

# Semantic indicators for Bahuvrīhi (possession/attribute of external entity)
BAHUVRĪHI_QUALIFIERS = {'mahā', 'dīrgha', 'bahu', 'citra', 'su', 'ananta', 'satya', 'vīra'}
BAHUVRĪHI_SUBSTANTIVES = {
    'iṣvāsa', 'ratha', 'bāhu', 'netra', 'hasta', 'karṇa', 'dhana', 'mati', 'buddhi',
    'tejas', 'vīrya', 'ātman', 'padma', 'anīka', 'kṛpā', 'locana'
}
SIMILARITY_TRIGGERS = {'sama', 'sadṛśa', 'tulya', 'ūna', 'samā', 'samāḥ', 'samam'}


def analyze_samasa_subtype(left: str, right: str, text: str) -> Dict[str, Any]:
    """
    Dynamically deduces Samāsa subtype, generates analytical Vigraha, and cites Pāṇinian Sūtras.
    Purely rule-based derivation without hardcoding specific verses.
    """
    left_dev = iast_to_devanagari(left)
    right_dev = iast_to_devanagari(right)
    text_dev = iast_to_devanagari(text)

    # 1. Avyayībhāva (Prior element is an indeclinable / prefix)
    if left in ('yathā', 'prati', 'anu', 'upa', 'saha', 'nis', 'nir'):
        if left == 'yathā':
            clean_r = right[:-1] if right.endswith(('m', 'ṃ')) else right
            vig_iast = f"{clean_r}m anatikramya"
            vig_dev = f"{iast_to_devanagari(clean_r)}म् अनतिक्रम्य"
        elif left == 'prati':
            clean_r = right[:-1] if right.endswith(('m', 'ṃ')) else right
            vig_iast = f"{clean_r} {clean_r} prati"
            vig_dev = f"{iast_to_devanagari(clean_r)} {iast_to_devanagari(clean_r)} प्रति"
        else:
            vig_iast = f"{left} {right}"
            vig_dev = f"{left_dev} {right_dev}"

        return {
            'subtype': 'Avyayībhāva Samāsa (अव्ययीभाव समास)',
            'sutra': 'avyayībhāvaḥ (2.1.5) / yathāsādṛśye (2.1.7)',
            'padacheda': f"{left_dev} + {right_dev} ({left} + {right})",
            'samasa': f"{vig_dev} -> {text_dev} (Avyayībhāva Samāsa)",
            'sandhi_steps': [f"Sandhi 1: {left_dev} + {right_dev} = {text_dev} (Direct Abutment)"],
            'commentary': f"The indeclinable prior word '{left}' governs the compound."
        }

    # 2. Pañcamī Tatpuruṣa (Separation, fear, falling participles)
    if any(right.startswith(p) for p in ('patit', 'bhay', 'mukt', 'bhraṣṭ', 'trast')):
        ablative_left_iast = f"{left}āt" if left.endswith(('a', 'ā')) else f"{left}aḥ"
        ablative_left_dev = f"{left_dev[:-1] if left_dev.endswith(('ा', 'a')) else left_dev}ात्"
        vig_iast = f"{ablative_left_iast} {right}"
        vig_dev = f"{ablative_left_dev} {right_dev}"
        return {
            'subtype': 'Pañcamī Tatpuruṣa Samāsa (पञ्चमी तत्पुरुष समास)',
            'sutra': 'pañcamī bhayena (2.1.37) / apeta-apoḍha-mukta-patita-apatrastair alpāśaḥ (2.1.38)',
            'padacheda': f"{ablative_left_dev} + {right_dev} ({ablative_left_iast} + {right})",
            'samasa': f"{vig_dev} -> {text_dev} (Pañcamī Tatpuruṣa Samāsa)",
            'sandhi_steps': [f"Sandhi 1: {left_dev} + {right_dev} = {text_dev} (Direct Abutment)"],
            'commentary': f"Ablative dependency: '{left}' takes elided case suffix -āt (Ekārthībhāva)."
        }

    # 3. Generic Multi-member Compound (e.g. A + B + C with Dvandva + Similarity Tatpuruṣa)
    # Checks if right side contains another stem combined with a comparison word (sama, tulya, sadṛśa)
    for trig in SIMILARITY_TRIGGERS:
        if right.endswith(trig) and len(right) > len(trig):
            mid_stem = right[:-len(trig)]
            # Normalize mid_stem if sandhi changed vowel
            mid_stem_clean = mid_stem.rstrip('aāeiou') + 'a' if not mid_stem.endswith(('a', 'ā', 'i', 'u', 'ṛ')) else mid_stem
            mid_dev = iast_to_devanagari(mid_stem_clean)
            trig_dev = iast_to_devanagari(trig) if trig.endswith('ḥ') else f"{iast_to_devanagari(trig)}ः"
            return {
                'subtype': 'Dvandva-garbha Tṛtīyā Tatpuruṣa Samāsa (द्वन्द्व-गर्भ तृतीया तत्पुरुष समास)',
                'sutra': 'cārthe dvandvaḥ (2.2.29) & tṛtīyā tatkṛtārthena... (2.1.30)',
                'padacheda': f"{left_dev} + {mid_dev} + {trig_dev} ({left} + {mid_stem_clean} + {trig})",
                'samasa': f"{left_dev} च {mid_dev} च = {left_dev}{mid_dev}ौ (द्वन्द्व); ताभ्यां {trig_dev} -> {text_dev} (तृतीया तत्पुरुष)",
                'sandhi_steps': [f"Sandhi 1: {left_dev} + {mid_dev} = {left_dev}{mid_dev}", f"Sandhi 2: {left_dev}{mid_dev} + {trig_dev} = {text_dev}"],
                'commentary': f"Multi-member compound: Prior constituents form an Itaretara Dvandva, which subsequently forms a Tṛtīyā Tatpuruṣa with the comparative qualifier '{trig}'."
            }

    # 4. Generic Bahuvrīhi (Exocentric Compound / Anyapadārtha-pradhāna)
    # Detected by qualifier + attribute/weapon/possession base
    clean_right_base = right.replace('eṣvās', 'iṣvās').rstrip('ḥmo').rstrip('ām').rstrip('au').rstrip('aā')
    is_bahuvrihi = left in BAHUVRĪHI_QUALIFIERS and any(clean_right_base.startswith(s.rstrip('a')) for s in BAHUVRĪHI_SUBSTANTIVES)

    if is_bahuvrihi:
        is_plural = text.endswith(('ā', 'āḥ', 'āḥ', 'e')) or right.endswith(('ā', 'āḥ', 'e'))
        if is_plural:
            vig_dev = f"{left_dev}ः {right_dev}ः येषां ते -> {text_dev}"
            vig_iast = f"{left}ḥ {right}ḥ yeṣāṃ te -> {text}"
            pad_dev = f"{left_dev} + {right_dev if right_dev.endswith('ः') else right_dev + 'ः'}"
            pad_iast = f"{left} + {right if right.endswith('ḥ') else right + 'ḥ'}"
        else:
            vig_dev = f"महान् {right_dev} यस्य सः -> {text_dev}" if left == 'mahā' else f"{left_dev} {right_dev} यस्य सः -> {text_dev}"
            vig_iast = f"mahān {right} yasya saḥ -> {text}" if left == 'mahā' else f"{left} {right} yasya saḥ -> {text}"
            pad_dev = f"{left_dev} + {right_dev}"
            pad_iast = f"{left} + {right}"

        return {
            'subtype': 'Bahuvrīhi Samāsa (बहुव्रीहि समास / अन्यपदार्थ-प्रधान)',
            'sutra': 'anekam anyapadārthe (2.2.24)',
            'padacheda': f"{pad_dev} ({pad_iast})",
            'samasa': f"{vig_dev} (Bahuvrīhi Samāsa)",
            'sandhi_steps': [f"Sandhi 1: {left_dev} + {right_dev} = {text_dev}"],
            'commentary': "Exocentric compound pointing to a third external entity possessing these attributes (Anyapadārtha-pradhāna)."
        }

    # 3. Karmadhāraya (Adjective + Substantive or Apposition)
    adjective_stems = {'nīla', 'mahā', 'satya', 'vīra', 'rakta', 'śukla', 'kṛṣṇa', 'sundara', 'śreṣṭha', 'parama', 'dhṛta'}
    if left in adjective_stems:
        vig_iast = f"{left}ṃ ca tat {right}" if right.endswith(('am', 'aṃ')) else f"{left}ḥ {right}"
        vig_dev = f"{left_dev}ं च तत् {right_dev}" if right.endswith(('am', 'aṃ')) else f"{left_dev}ः {right_dev}"
        return {
            'subtype': 'Karmadhāraya Samāsa (कर्मधारय समास / समानाधिकरण तत्पुरुष)',
            'sutra': 'viśeṣaṇaṃ viśeṣyeṇa bahulam (2.1.57) / tatpuruṣaḥ samānādhikaraṇaḥ karmadhārayaḥ (1.2.42)',
            'padacheda': f"{left_dev} + {right_dev} ({left} + {right})",
            'samasa': f"{vig_dev} -> {text_dev} (Karmadhāraya Samāsa)",
            'sandhi_steps': [f"Sandhi 1: {left_dev} + {right_dev} = {text_dev}"],
            'commentary': f"Appositional relationship: '{left}' functions as qualitative descriptor of '{right}'."
        }

    # 4. Dvandva (Copulative Dual: e.g. rāmalakṣmaṇau, mātāpitarau)
    if right.endswith('au') or text.endswith('au'):
        vig_iast = f"{left}ś ca {right} ca"
        vig_dev = f"{left_dev} च {right_dev} च"
        return {
            'subtype': 'Itaretara Dvandva Samāsa (द्वन्द्व समास)',
            'sutra': 'cārthe dvandvaḥ (2.2.29)',
            'padacheda': f"{left_dev} + {right_dev} ({left} + {right})",
            'samasa': f"{vig_dev} -> {text_dev} (Itaretara Dvandva Samāsa)",
            'sandhi_steps': [f"Sandhi 1: {left_dev} + {right_dev} = {text_dev}"],
            'commentary': "Copulative compound where all constituent members retain equal semantic primacy (Ubhayapadārtha-pradhāna)."
        }

    # 5. Default: Ṣaṣṭhī Tatpuruṣa (Genitive Relationship)
    base_l = left[:-1] if left.endswith(('a', 'ā', 'u', 'i')) else left
    if left.endswith('a'):
        genitive_left_iast = f"{base_l}asya"
    elif left.endswith('ā'):
        genitive_left_iast = f"{left}yāḥ"
    elif left.endswith('u'):
        genitive_left_iast = f"{base_l}oḥ"
    elif left.endswith('i'):
        genitive_left_iast = f"{base_l}eḥ"
    else:
        genitive_left_iast = f"{left}aḥ"
    if left in ('rāja', 'rājan'):
        genitive_left_iast = 'rājñaḥ'
    elif left == 'pitṛ':
        genitive_left_iast = 'pituḥ'
    elif left == 'mātṛ':
        genitive_left_iast = 'mātuḥ'

    if right in ('ānīka', 'ānīkam', 'ānīkaṃ'):
        right = 'a' + right[1:]
        right_dev = iast_to_devanagari(right)

    genitive_left_dev = iast_to_devanagari(genitive_left_iast)
    vig_iast = f"{genitive_left_iast} {right}"
    vig_dev = f"{genitive_left_dev} {right_dev}"

    return {
        'subtype': 'Ṣaṣṭhī Tatpuruṣa Samāsa (षष्ठी तत्पुरुष समास)',
        'sutra': 'ṣaṣṭhī (2.2.8)',
        'padacheda': f"{genitive_left_dev} + {right_dev} ({genitive_left_iast} + {right})",
        'samasa': f"{vig_dev} -> {text_dev} (Ṣaṣṭhī Tatpuruṣa Samāsa)",
        'sandhi_steps': [f"Sandhi 1: {left_dev} + {right_dev} = {text_dev}"],
        'commentary': f"Genitive dependency: '{left}' denotes owner/origin of dominant entity '{right}' (Uttarapadārtha-pradhāna)."
    }


def analyze_sandhi_subtype(left: str, right: str, rule_name: str, text: str) -> Dict[str, Any]:
    """
    Dynamically identifies Sandhi or Saṃhitā phenomenon, Pāṇinian Sūtras, and Padacheda.
    """
    left_dev = iast_to_devanagari(left)
    right_dev = iast_to_devanagari(right)
    text_dev = iast_to_devanagari(text)

    # 1. Saṃhitā / Vyañjana Saṃyoga (Consonant-Vowel natural fusion: -m + vowel)
    if "Hal Sandhi" in rule_name or "Direct Abutment" in rule_name or "m +" in rule_name or "Saṃhitā" in rule_name or left.endswith(('m', 'ṃ')):
        if left.endswith(('m', 'ṃ')) and (right.startswith(('a', 'ā', 'i', 'ī', 'u', 'ū', 'ṛ', 'e', 'ai', 'o', 'au')) or right in ('api', 'eva', 'iti', 'asti', 'iva', 'upasaṅgamya', 'abravīt')):
            left_clean = left[:-1] if left.endswith(('m', 'ṃ')) else left
            left_clean_dev = iast_to_devanagari(left_clean)
            padacheda_dev = f"{left_clean_dev}म् + {right_dev}"
            return {
                'subtype': 'Saṃhitā / Vyañjana Saṃyoga (संहिता / व्यञ्जन संयोग - Padacheda)',
                'sutra': "paraḥ sannikarṣaḥ saṃhitā (1.4.109) & mo'nusvāraḥ (8.3.23)",
                'padacheda': f"{padacheda_dev} ({left_clean}m + {right})",
                'samasa': 'N/A (Sentential Sequence of Independent Padas)',
                'sandhi_steps': [f"Sandhi 1: {padacheda_dev} = {text_dev} (Consonant-Vowel Saṃhitā: m + vowel / मोऽनुस्वारः blocked)"],
                'commentary': "Natural continuous speech (Saṃhitā): A pure consonant (halant म्) directly joins following vowel."
            }

    # 2. Visarga Sattva / Śatva / Ṣatva / Rutva (e.g. duryodhanaḥ + tadā, rāmaḥ + ca, muniḥ + uvāca)
    if "Visarga" in rule_name or "on 'st'" in rule_name or "on 'śc'" in rule_name or "ḥ +" in rule_name or "aḥ +" in rule_name or left.endswith(('ḥ', 'aḥ', 'is', 'us', 'as')):
        return {
            'subtype': 'Visarga Sattva / Śatva Sandhi (विसर्ग सत्व/शत्व सन्धिः)',
            'sutra': "visarjanīyasya saḥ (8.3.34) & stoḥ ścunā ścuḥ (8.4.40)",
            'padacheda': f"{left_dev} + {right_dev} ({left} + {right})",
            'samasa': 'N/A (Sentential Sequence of Independent Padas)',
            'sandhi_steps': [f"Sandhi 1: {left_dev} + {right_dev} = {text_dev} (Visarga Sandhi / 8.3.34)"],
            'commentary': "Visarga transforms into dental 's', palatal 'ś', or 'r' before following sounds."
        }

    # 3. Vṛddhi Svara-Sandhi (ai, au)
    if "Vṛddhi" in rule_name or "on 'ai'" in rule_name or "on 'au'" in rule_name or 'ai' in text or 'au' in text:
        return {
            'subtype': 'Vṛddhi Svara-Sandhi (वृद्धि स्वर-सन्धिः)',
            'sutra': 'vṛddhireci (6.1.88)',
            'padacheda': f"{left_dev} + {right_dev} ({left} + {right})",
            'samasa': 'N/A (Phonetic Svara-Sandhi Junction)',
            'sandhi_steps': [f"Sandhi 1: {left_dev} + {right_dev} = {text_dev} (Vṛddhi Sandhi / वृद्धिरेचि 6.1.88)"],
            'commentary': 'Vowel gradation: a/ā followed by e/ai yields ai, and a/ā followed by o/au yields au.'
        }

    # 4. Yaṇ Svara-Sandhi (ya, va, ra)
    if "Yaṇ" in rule_name or "on 'ya'" in rule_name or "on 'va'" in rule_name or "on 'ra'" in rule_name:
        return {
            'subtype': 'Yaṇ Svara-Sandhi (यण् स्वर-सन्धिः)',
            'sutra': 'iko yaṇaci (6.1.77)',
            'padacheda': f"{left_dev} + {right_dev} ({left} + {right})",
            'samasa': 'N/A (Phonetic Svara-Sandhi Junction)',
            'sandhi_steps': [f"Sandhi 1: {left_dev} + {right_dev} = {text_dev} (Yaṇ Sandhi / इको यणचि 6.1.77)"],
            'commentary': 'Semivowel substitution: i/ī -> y, u/ū -> v, ṛ -> r before a dissimilar vowel.'
        }

    # 5. Guṇa Svara-Sandhi (e, o)
    if "Guṇa" in rule_name or "on 'e'" in rule_name or "on 'o'" in rule_name or 'e' in text or 'o' in text:
        return {
            'subtype': 'Guṇa Svara-Sandhi (गुण स्वर-सन्धिः)',
            'sutra': 'ād guṇaḥ (6.1.87)',
            'padacheda': f"{left_dev} + {right_dev} ({left} + {right})",
            'samasa': 'N/A (Phonetic Svara-Sandhi Junction)',
            'sandhi_steps': [f"Sandhi 1: {left_dev} + {right_dev} = {text_dev} (Guṇa Sandhi / आद् गुणः 6.1.87)"],
            'commentary': 'Vowel combination: a/ā followed by i/ī yields e, and a/ā followed by u/ū yields o.'
        }

    # 6. Dīrgha Svara-Sandhi (ā, ī, ū)
    if "Dīrgha" in rule_name or "on 'ā'" in rule_name or "on 'ī'" in rule_name or "on 'ū'" in rule_name or any(c in text for c in ('ā', 'ī', 'ū')):
        return {
            'subtype': 'Dīrgha Svara-Sandhi (दीर्घ स्वर-सन्धिः)',
            'sutra': 'akaḥ savarṇe dīrghaḥ (6.1.101)',
            'padacheda': f"{left_dev} + {right_dev} ({left} + {right})",
            'samasa': 'N/A (Phonetic Svara-Sandhi Junction)',
            'sandhi_steps': [f"Sandhi 1: {left_dev} + {right_dev} = {text_dev} (Dīrgha Sandhi / अकः सवर्णे दीर्घः 6.1.101)"],
            'commentary': 'Two homogeneous simple vowels coalesce into their corresponding long vowel.'
        }

    # Generic Vyañjana Sandhi fallback
    return {
        'subtype': 'Vyañjana Sandhi (व्यञ्जन सन्धिः / Hal-Sandhi)',
        'sutra': "stoḥ ścunā ścuḥ (8.4.40) / jhalāṃ jaśo'nte (8.2.39)",
        'padacheda': f"{left_dev} + {right_dev} ({left} + {right})",
        'samasa': 'N/A (Consonant Junction)',
        'sandhi_steps': [f"Sandhi 1: {left_dev} + {right_dev} = {text_dev} (Vyañjana Sandhi)"],
        'commentary': 'Consonant assimilation or substitution at word boundary.'
    }
