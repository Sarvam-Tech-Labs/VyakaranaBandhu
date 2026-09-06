"""
Modular Test Case Registry for Sanskrit Morphological Testing.
To add new test cases, simply append dictionaries to the corresponding lists below.
"""

# =============================================================================
# 1. SAMĀSA ONLY CASES (Nominal Compounds without Phonetic Mutations)
# =============================================================================
SAMASA_CASES = [
    # Ṣaṣṭhī Tatpuruṣa (Genitive Dependency)
    {
        "text": "rājapuruṣaḥ",
        "devanagari": "राजपुरुषः",
        "expected_class": "Samāsa Only",
        "expected_subtype": "Ṣaṣṭhī Tatpuruṣa",
        "notes": "King's officer (rājñaḥ puruṣaḥ)"
    },
    {
        "text": "rāmaputraḥ",
        "devanagari": "रामपुत्रः",
        "expected_class": "Samāsa Only",
        "expected_subtype": "Ṣaṣṭhī Tatpuruṣa",
        "notes": "Rama's son (rāmasya putraḥ)"
    },
    {
        "text": "dharmakṣetre",
        "devanagari": "धर्मक्षेत्रे",
        "expected_class": "Samāsa Only",
        "expected_subtype": "Tatpuruṣa",
        "notes": "In the field of dharma"
    },
    # Pañcamī Tatpuruṣa (Ablative Separation/Fear)
    {
        "text": "vṛkṣapatitaṃ",
        "devanagari": "वृक्षपतितं",
        "expected_class": "Samāsa Only",
        "expected_subtype": "Pañcamī Tatpuruṣa",
        "notes": "Fallen from tree (vṛkṣāt patitaḥ)"
    },
    {
        "text": "vṛkṣapatitam",
        "devanagari": "वृक्षपतितम्",
        "expected_class": "Samāsa Only",
        "expected_subtype": "Pañcamī Tatpuruṣa",
        "notes": "Fallen from tree (vṛkṣāt patitam)"
    },
    # Dvitīyā Tatpuruṣa (Accusative Motion)
    {
        "text": "grāmagataḥ",
        "devanagari": "ग्रामगतः",
        "expected_class": "Samāsa Only",
        "expected_subtype": "Tatpuruṣa",
        "notes": "Gone to village (grāmaṃ gataḥ)"
    },
    # Avyayībhāva (Adverbial Compounds)
    {
        "text": "yathāśakti",
        "devanagari": "यथाशक्ति",
        "expected_class": "Samāsa Only",
        "expected_subtype": "Avyayībhāva",
        "notes": "According to capacity (śaktim anatikramya)"
    },
    {
        "text": "yathāmati",
        "devanagari": "यथामति",
        "expected_class": "Samāsa Only",
        "expected_subtype": "Avyayībhāva",
        "notes": "According to intellect (matim anatikramya)"
    },
    # Dvandva (Copulative Pair without Sandhi)
    {
        "text": "rāmalakṣmaṇau",
        "devanagari": "रामलक्ष्मणौ",
        "expected_class": "Samāsa Only",
        "expected_subtype": "Dvandva",
        "notes": "Rama and Lakshmana (rāmaśca lakṣmaṇaśca)"
    },
]

# =============================================================================
# 2. SANDHI ONLY CASES (Sentential Phonetic Junctions between Independent Padas)
# =============================================================================
SANDHI_CASES = [
    # Consonant-Vowel Saṃhitā (-m + Vowel)
    {
        "text": "phalamapi",
        "devanagari": "फलमपि",
        "expected_class": "Sandhi Only",
        "expected_subtype": "Saṃhitā",
        "expected_left": "phalam",
        "expected_right": "api",
        "notes": "Noun + particle (m + a -> ma)"
    },
    {
        "text": "kimakurvata",
        "devanagari": "किमकुर्वत",
        "expected_class": "Sandhi Only",
        "expected_subtype": "Saṃhitā",
        "expected_left": "kim",
        "expected_right": "akurvata",
        "notes": "Pronoun + verb (m + a -> ma)"
    },
    {
        "text": "ācāryamupasaṅgamya",
        "devanagari": "आचार्यमुपसङ्गम्य",
        "expected_class": "Sandhi Only",
        "expected_subtype": "Saṃhitā",
        "expected_left": "ācāryam",
        "expected_right": "upasaṅgamya",
        "notes": "Noun + gerund (m + u -> mu)"
    },
    {
        "text": "vacanamabravīt",
        "devanagari": "वचनमब्रवीत्",
        "expected_class": "Sandhi Only",
        "expected_subtype": "Saṃhitā",
        "expected_left": "vacanam",
        "expected_right": "abravīt",
        "notes": "Noun + verb (m + a -> ma)"
    },
    # Visarga Sattva / Śatva / Rutva
    {
        "text": "duryodhanastadā",
        "devanagari": "दुर्योधनस्तदा",
        "expected_class": "Sandhi Only",
        "expected_subtype": "Visarga",
        "expected_left": "duryodhanaḥ",
        "expected_right": "tadā",
        "notes": "Visarga before hard dental (ḥ + t -> st)"
    },
    {
        "text": "rāmaśca",
        "devanagari": "रामश्च",
        "expected_class": "Sandhi Only",
        "expected_subtype": "Visarga",
        "expected_left": "rāmaḥ",
        "expected_right": "ca",
        "notes": "Visarga before palatal (ḥ + c -> śc)"
    },
    {
        "text": "muniruvāca",
        "devanagari": "मुनिरुवाच",
        "expected_class": "Sandhi Only",
        "expected_subtype": "Visarga",
        "expected_left": "muniḥ",
        "expected_right": "uvāca",
        "notes": "Visarga rutva before vowel (ḥ + u -> ru)"
    },
    # Sentential Vowel Sandhis
    {
        "text": "tatraiva",
        "devanagari": "तत्रैव",
        "expected_class": "Sandhi Only",
        "expected_subtype": "Vṛddhi",
        "expected_left": "tatra",
        "expected_right": "eva",
        "notes": "Vṛddhi between indeclinables (a + e -> ai)"
    },
    {
        "text": "pāṇḍavāścaiva",
        "devanagari": "पाण्डवाश्चैव",
        "expected_class": "Sandhi Only",
        "expected_subtype": "Sandhi",
        "notes": "Cascading Visarga + Vṛddhi"
    },
]

# =============================================================================
# 3. BOTH CASES (Compounds containing internal Phonetic Mutations)
# =============================================================================
BOTH_CASES = [
    # Karmadhāraya + Guṇa / Dīrgha
    {
        "text": "nīlotpalam",
        "devanagari": "नीलोत्पलं",
        "expected_class": "Both",
        "expected_samasa": "Karmadhāraya",
        "expected_sandhi": "Guṇa",
        "notes": "Blue lotus (nīla + utpalam)"
    },
    {
        "text": "mahātmā",
        "devanagari": "महात्मा",
        "expected_class": "Both",
        "expected_samasa": "Karmadhāraya",
        "expected_sandhi": "Dīrgha",
        "notes": "Great soul (mahā + ātmā)"
    },
    # Tatpuruṣa + Dīrgha / Guṇa
    {
        "text": "devāgamanam",
        "devanagari": "देवागमनम्",
        "expected_class": "Both",
        "expected_samasa": "Tatpuruṣa",
        "expected_sandhi": "Dīrgha",
        "notes": "Arrival of gods (deva + āgamanam)"
    },
    {
        "text": "vidyālayam",
        "devanagari": "विद्यालयम्",
        "expected_class": "Both",
        "expected_samasa": "Tatpuruṣa",
        "expected_sandhi": "Dīrgha",
        "notes": "Abode of learning (vidyā + ālayaḥ)"
    },
    {
        "text": "sūryodayaḥ",
        "devanagari": "सूर्योदयः",
        "expected_class": "Both",
        "expected_samasa": "Tatpuruṣa",
        "expected_sandhi": "Guṇa",
        "notes": "Sunrise (sūrya + udayaḥ)"
    },
    {
        "text": "pāṇḍavānīkam",
        "devanagari": "पाण्डवानीकम्",
        "expected_class": "Both",
        "expected_samasa": "Tatpuruṣa",
        "expected_sandhi": "Dīrgha",
        "notes": "Pandava army (pāṇḍavasya + anīkam / pāṇḍava + anīka)"
    },
    {
        "text": "pāṇḍuputrāṇāmācārya",
        "devanagari": "पाण्डुपुत्राणामाचार्य",
        "expected_class": "Both",
        "expected_samasa": "Tatpuruṣa",
        "expected_sandhi": "Saṃhitā",
        "notes": "Sons of Pandu, O Teacher (pāṇḍuputrāṇām + ācārya)"
    },
]

# =============================================================================
# 4. NONE CASES (Simplex Words: Inflexible to compounding/sandhi splits)
# =============================================================================
SIMPLEX_CASES = [
    # Finite Verbs (tiṅanta)
    {"text": "pacati", "devanagari": "पचति", "expected_class": "None", "notes": "Present 3rd sing (cooks)"},
    {"text": "gacchati", "devanagari": "गच्छति", "expected_class": "None", "notes": "Present 3rd sing (goes)"},
    {"text": "uvāca", "devanagari": "उवाच", "expected_class": "None", "notes": "Perfect 3rd sing (said)"},
    # Single Substantives / Inflected Nouns (suP)
    {"text": "rājā", "devanagari": "राजा", "expected_class": "None", "notes": "Nominative sing (king)"},
    {"text": "sañjaya", "devanagari": "सञ्जय", "expected_class": "None", "notes": "Vocative sing (O Sanjaya)"},
    {"text": "yuyutsavaḥ", "devanagari": "युयुत्सवः", "expected_class": "None", "notes": "Desiderative noun nominative plural"},
    # Kṛdanta Participles & Gerunds
    {"text": "dṛṣṭvā", "devanagari": "दृष्ट्वा", "expected_class": "None", "notes": "Absolutive gerund (having seen)"},
    {"text": "vyūḍhaṃ", "devanagari": "व्यूढं", "expected_class": "None", "notes": "Kta participle accusative sing"},
    # Indeclinables (Avyaya)
    {"text": "tu", "devanagari": "तु", "expected_class": "None", "notes": "Transition particle"},
]

# =============================================================================
# 5. COMPLETE VERSE CASES (Imported from dedicated test_verse_cases.py)
# =============================================================================
try:
    from .test_verse_cases import VERSE_CASES
except (ImportError, ValueError):
    from tests.test_verse_cases import VERSE_CASES


# =============================================================================
# 6. ROBUSTNESS & EDGE CASES (Whitespace, Daṇḍas, Numbers, Symbols)
# =============================================================================
ROBUSTNESS_CASES = [
    {"input": "   धृतराष्ट्र   ", "expected_clean": "dhṛtarāṣṭra", "notes": "Excessive surrounding whitespace"},
    {"input": "वागर्थाविव ॥ १ ॥", "expected_clean": "vāgarthāviva", "notes": "Trailing verse numbering"},
    {"input": "phalam + api", "expected_clean": "phalam api", "notes": "Explicit plus signs"},
    {"input": "duryodhanaḥ : tadā", "expected_class": "Verse / Shloka", "notes": "Spaced colon visarga notation"},
]
