"""
Sanskrit Morphology Analyzer
Identifies nominal stems (prātipadika), inflected forms (padas with suP / tiṅ), and indeclinables (avyaya).
"""

from typing import Tuple, Optional, Set

# Common Nominal Inflections (suP vibhakti)
NOMINAL_INFLECTIONS = {
    # a-stem masculine / neuter
    'aḥ', 'am', 'aṃ', 'ena', 'eṇa', 'āya', 'āt', 'asya', 'e',
    'au', 'ābhyām', 'ayoḥ',
    'āḥ', 'ān', 'āni', 'aiḥ', 'ebhyaḥ', 'ānām', 'āṇām', 'eṣu',
    # ā-stem feminine
    'ā', 'ām', 'āṃ', 'ayā', 'āyai', 'āyāḥ', 'āyām',
    'e', 'ābhyām', 'ayoḥ',
    'āḥ', 'ābhiḥ', 'ābhyaḥ', 'ānām', 'āṇām', 'āsu',
    # i-stem / ī-stem
    'iḥ', 'im', 'iṃ', 'inā', 'iṇā', 'aye', 'eḥ', 'au',
    'īḥ', 'īm', 'īṃ', 'yā', 'yai', 'yāḥ', 'yām',
    'ī', 'ibhyām', 'iyoḥ',
    'ayaḥ', 'īn', 'ibhiḥ', 'ibhyaḥ', 'īnām', 'iṣu',
    'yaḥ', 'ībhiḥ', 'ībhyaḥ', 'īnām', 'īṣu',
    # u-stem / ū-stem
    'uḥ', 'um', 'uṃ', 'unā', 'ave', 'oḥ', 'au',
    'ūḥ', 'ūm', 'ūṃ', 'vā', 'vai', 'vāḥ', 'vām',
    'ū', 'ubhyām', 'uvoḥ',
    'avaḥ', 'ūn', 'ubhiḥ', 'ubhyaḥ', 'ūnām', 'uṣu',
    # consonant / in-stems
    'ā', 'anam', 'anaṃ', 'nā', 'ne', 'naḥ', 'ni',
    'ī', 'inam', 'inaṃ', 'inā', 'ine', 'inaḥ', 'ini',
    'inaḥ', 'ibhiḥ', 'ibhyaḥ', 'inām', 'iṣu'
}

# Common Verbal Conjugations (tiṅ pratyaya)
VERBAL_INFLECTIONS = {
    # Present / LAT (Parasmaipada & Ātmanepada)
    'ti', 'taḥ', 'nti',
    'si', 'thaḥ', 'tha',
    'mi', 'vaḥ', 'maḥ',
    'te', 'āte', 'nte',
    'se', 'āthe', 'dhve',
    'e', 'vahe', 'mahe',
    # Imperative / LOT
    'tu', 'tām', 'ntu',
    'hi', 'tam', 'ta',
    'āni', 'āva', 'āma',
    # Past / LAN & Perfect / Aorist
    'at', 'atām', 'an', 'īt', 'ītam', 'īṣu',
    'aḥ', 'atam', 'ata',
    'am', 'āva', 'āma',
    # Kṛdanta / Indeclinable Participles
    'tvā', 'ya', 'tum',
    # Optative / VIDHILIN
    'et', 'etām', 'eyuḥ',
    'eḥ', 'etam', 'eta',
    'eyam', 'eva', 'ema'
}

# Avyayas & Upasargas (Indeclinables & Prefixes)
INDECLINABLES = {
    'kim', 'katham', 'yathā', 'tathā', 'sadā', 'kadā', 'kadācana', 'cana', 'mā', 'sarvadā', 'ekadā',
    'tadā', 'yadā', 'idānīm', 'tataḥ', 'yataḥ', 'kutaḥ', 'adhunā',
    'atra', 'yatra', 'tatra', 'kutra', 'sarvatra', 'anyatra',
    'eva', 'evam', 'iti', 'ca', 'vā', 'api', 'tu', 'hi', 'iva',
    'saha', 'vina', 'alam', 'prati', 'anu', 'upa', 'sam',
    'niḥ', 'nis', 'nir', 'dus', 'dur', 'vi', 'ā', 'ni',
    'adhi', 'ati', 'su', 'ud', 'ut', 'abhi', 'apa', 'ava'
}

# Common Sanskrit Bare Nominal Stems (Prātipadika / In Initio Compositi - iic)
COMMON_STEMS = {
    'rāma', 'lakṣmaṇa', 'rāja', 'rājan', 'nīla', 'deva', 'mahā', 'dharma', 'satya', 'vīra',
    'bāla', 'vidyā', 'guru', 'pitṛ', 'mātṛ', 'bhrātṛ', 'agni', 'kṛṣṇa',
    'śiva', 'sūrya', 'candra', 'jñāna', 'karma', 'loka', 'bhakta', 'yajña',
    'gaja', 'aśva', 'vṛkṣa', 'nagara', 'grāma', 'vana', 'phala', 'puṣpa',
    'kamala', 'padma', 'jala', 'vāyu', 'ākāśa', 'bhūmi', 'pṛthvī', 'puruṣa',
    'nārī', 'strī', 'putra', 'kanyā', 'mitra', 'śatru', 'kāvya', 'śāstra',
    'veda', 'mantra', 'tīrtha', 'puṇya', 'pāpa', 'sukha', 'duḥkha', 'krodha',
    'kāma', 'lobha', 'moha', 'bhaya', 'tejas', 'tapas', 'manas', 'citta',
    'ātman', 'brahman', 'prāṇa', 'śakti', 'bhakti', 'mukti', 'śānti', 'kṣamā',
    'dayā', 'sneha', 'prema', 'ananta', 'sarva', 'eka', 'dvi', 'tri',
    'catuḥ', 'pañca', 'ṣaṭ', 'sapta', 'aṣṭa', 'nava', 'daśa', 'śata', 'sahasra',
    'ālaya', 'udaya', 'āgama', 'āgamana', 'dhṛta', 'rāṣṭra', 'kuru', 'anīka', 'māmaka', 'parameśvara',
    'pāṇḍava', 'vāgartha', 'pratipatti', 'pārvatī', 'īśvara', 'samaveta', 'sampṛkta',
    'pāṇḍu', 'drupada', 'camū', 'śiṣya', 'dhīmat', 'mahat', 'etad',
    'bhīma', 'arjuna', 'sama', 'iṣvāsa', 'yuyudhāna', 'virāṭa', 'śūra', 'yudh', 'ratha'
}

# Known Standalone Root Words / Standard Grammar Examples
KNOWN_LEXICON = {
    # Generic Verbs
    'pacati', 'gacchati', 'paṭhati', 'likhati', 'karoti', 'paśyati',
    'bhavati', 'tiṣṭhati', 'nayati', 'smarati', 'hasati', 'vadati',
    'kurvanti', 'gacchanti', 'paṭhanti', 'bhavanti', 'jānāti',
    # Standard Nouns
    'rāmaḥ', 'rāmam', 'rāmeṇa', 'rāmāya', 'rāmāt', 'rāmasya', 'rāme',
    'devaḥ', 'devam', 'devena', 'devāya', 'devāt', 'devasya', 'deve',
    'bālaḥ', 'bālam', 'vṛkṣaḥ', 'vṛkṣam', 'vṛkṣāt', 'gṛham', 'jalam',
    'phalam', 'puṣpam', 'pustakam', 'nagaram', 'mitram',
    'rājā', 'rājānaḥ', 'rājñaḥ', 'pitā', 'mātā', 'bhrātā',
    'guruḥ', 'gurum', 'guruṇā', 'gurave', 'guroḥ', 'gurau',
    'hariḥ', 'harim', 'hariṇā', 'haraye', 'hareḥ', 'harau',
    'nadī', 'nadīm', 'nadyā', 'nadyai', 'nadyāḥ', 'nadyām'
}


_SUBANTA_ENGINE = None


def get_subanta_engine():
    global _SUBANTA_ENGINE
    if _SUBANTA_ENGINE is None:
        from .subanta_engine import SubantaEngine
        _SUBANTA_ENGINE = SubantaEngine()
    return _SUBANTA_ENGINE


def is_inflected_pada(token: str) -> bool:
    """
    Checks if a token has valid nominal or verbal case inflections (Pada).
    """
    token = token.strip()
    if not token or len(token) < 2:
        return False
        
    if token in KNOWN_LEXICON or token in INDECLINABLES:
        return True

    # Bare stems ending in short 'a' without non-zero inflection are Prātipadikas (compounding stems)
    if token in COMMON_STEMS and token.endswith(('a', 'i', 'u', 'ṛ')) and not token.endswith(('aḥ', 'am', 'aṃ', 'ena', 'eṇa', 'āya', 'āt', 'asya', 'e', 'āḥ', 'ān', 'aiḥ', 'ebhyaḥ', 'ānām', 'eṣu')):
        return False
        
    # Check Pāṇinian Subanta Engine for non-vocative nominal inflection validity
    try:
        eng = get_subanta_engine()
        analyses = eng.analyze_subanta(token)
        if analyses:
            # If the only reading is vocative singular for a short-a stem, it's structurally a bare stem
            non_sambodhana = [a for a in analyses if not a['vibhakti'].startswith('Sambodhana')]
            if non_sambodhana:
                return True
    except Exception:
        pass

    # Check verbal inflections (tiṅ & kṛdanta suffixes)
    for infl in ('tvā', 'tum', 'ya'):
        if token.endswith(infl) and len(token) > len(infl):
            stem_candidate = token[:-len(infl)]
            if infl == 'ya':
                if any(token.startswith(u) for u in ('upa', 'sam', 'vi', 'pra', 'ni', 'abhi', 'anu', 'ā', 'ud', 'ava', 'apa', 'pari', 'prati')):
                    return True
            else:
                if len(stem_candidate) >= 2:
                    return True

    for infl in sorted(VERBAL_INFLECTIONS, key=len, reverse=True):
        if infl in ('tvā', 'tum', 'ya'):
            continue
        if token.endswith(infl) and len(token) > len(infl):
            stem_candidate = token[:-len(infl)]
            if len(stem_candidate) >= 2:
                return True
            
    # Check multi-character nominal inflections (strong morphological cues)
    strong_infls = [inf for inf in NOMINAL_INFLECTIONS if len(inf) >= 2]
    for infl in sorted(strong_infls, key=len, reverse=True):
        if token.endswith(infl) and len(token) > len(infl):
            stem_candidate = token[:-len(infl)]
            if len(stem_candidate) >= 2:
                return True

    # Check 1-character nominal inflections only if stem is recognized in COMMON_STEMS or is a valid bare stem
    single_infls = [inf for inf in NOMINAL_INFLECTIONS if len(inf) == 1]
    for infl in single_infls:
        if token.endswith(infl) and len(token) > len(infl):
            stem_candidate = token[:-len(infl)]
            if stem_candidate in COMMON_STEMS or (len(stem_candidate) >= 4 and stem_candidate.endswith(('a', 'i', 'u', 'ṛ'))):
                return True
                
    return False


def is_bare_stem(token: str) -> bool:
    """
    Checks if a token represents an uninflected nominal stem (Prātipadika).
    """
    token = token.strip()
    if not token or len(token) < 3:
        return False
        
    if token in COMMON_STEMS:
        return True
        
    # Generic stem ending patterns requiring minimum stem length >= 4
    stem_endings = ('a', 'ā', 'i', 'ī', 'u', 'ū', 'ṛ', 'an', 'in', 'as', 'is', 'us')
    if len(token) >= 4 and token.endswith(stem_endings):
        if not token.endswith(('aḥ', 'am', 'aṃ', 'āt', 'asya', 'āya', 'ena', 'ebhiḥ', 'ebhyaḥ', 'ānām')):
            return True
        
    return False


def analyze_morphology(token: str) -> str:
    """
    Returns the morphological category of the token:
    'pada' (inflected word), 'stem' (prātipadika), 'avyaya' (indeclinable), or 'unknown'.
    """
    token = token.strip()
    if not token:
        return 'unknown'
        
    if token in INDECLINABLES:
        return 'avyaya'
        
    if token in KNOWN_LEXICON:
        return 'pada'

    if token in COMMON_STEMS:
        return 'stem'
        
    if is_inflected_pada(token):
        return 'pada'
        
    if is_bare_stem(token):
        return 'stem'
        
    return 'unknown'
