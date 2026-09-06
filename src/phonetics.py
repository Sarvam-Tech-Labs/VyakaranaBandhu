"""
Sanskrit Phonetics & Sandhi Rule Engine
Models Pāṇinian phonological rules (Svara, Vyañjana, Visarga Sandhi) and provides reverse Vichchhed split candidates.
"""

from typing import List, Tuple, Dict, Any

VOWELS = {'a', 'ā', 'i', 'ī', 'u', 'ū', 'ṛ', 'ṝ', 'ḷ', 'ḹ', 'e', 'ai', 'o', 'au'}
SIMPLE_VOWELS = {'a', 'ā', 'i', 'ī', 'u', 'ū', 'ṛ', 'ṝ'}
DIPHTHONGS = {'e', 'ai', 'o', 'au'}
CONSONANTS = {
    'k', 'kh', 'g', 'gh', 'ṅ',
    'c', 'ch', 'j', 'jh', 'ñ',
    'ṭ', 'ṭh', 'ḍ', 'ḍh', 'ṇ',
    't', 'th', 'd', 'dh', 'n',
    'p', 'ph', 'b', 'bh', 'm',
    'y', 'r', 'l', 'v',
    'ś', 'ṣ', 's', 'h'
}

VOICED_CONSONANTS = {
    'g', 'gh', 'ṅ', 'j', 'jh', 'ñ', 'ḍ', 'ḍh', 'ṇ',
    'd', 'dh', 'n', 'b', 'bh', 'm', 'y', 'r', 'l', 'v', 'h'
}

UNVOICED_CONSONANTS = {
    'k', 'kh', 'c', 'ch', 'ṭ', 'ṭh', 't', 'th', 'p', 'ph', 'ś', 'ṣ', 's'
}

# Forward Sandhi Rules: (w1_end, w2_start) -> merged_sound
SANDHI_RULES: Dict[Tuple[str, str], str] = {
    # Dīrgha Sandhi
    ('a', 'a'): 'ā', ('a', 'ā'): 'ā', ('ā', 'a'): 'ā', ('ā', 'ā'): 'ā',
    ('i', 'i'): 'ī', ('i', 'ī'): 'ī', ('ī', 'i'): 'ī', ('ī', 'ī'): 'ī',
    ('u', 'u'): 'ū', ('u', 'ū'): 'ū', ('ū', 'u'): 'ū', ('ū', 'ū'): 'ū',
    ('ṛ', 'ṛ'): 'ṝ', ('ṛ', 'ṝ'): 'ṝ',
    
    # Guṇa Sandhi
    ('a', 'i'): 'e', ('a', 'ī'): 'e', ('ā', 'i'): 'e', ('ā', 'ī'): 'e',
    ('a', 'u'): 'o', ('a', 'ū'): 'o', ('ā', 'u'): 'o', ('ā', 'ū'): 'o',
    ('a', 'ṛ'): 'ar', ('ā', 'ṛ'): 'ar',
    
    # Vṛddhi Sandhi
    ('a', 'e'): 'ai', ('a', 'ai'): 'ai', ('ā', 'e'): 'ai', ('ā', 'ai'): 'ai',
    ('a', 'o'): 'au', ('a', 'au'): 'au', ('ā', 'o'): 'au', ('ā', 'au'): 'au',
    ('a', 'ṛ'): 'ār',
    
    # Yaṇ Sandhi
    ('i', 'a'): 'ya', ('i', 'ā'): 'yā', ('i', 'u'): 'yu', ('i', 'ū'): 'yū', ('i', 'e'): 'ye',
    ('ī', 'a'): 'ya', ('ī', 'ā'): 'yā', ('ī', 'u'): 'yu', ('ī', 'ū'): 'yū', ('ī', 'e'): 'ye',
    ('u', 'a'): 'va', ('u', 'ā'): 'vā', ('u', 'i'): 'vi', ('u', 'ī'): 'vī', ('u', 'e'): 've',
    ('ū', 'a'): 'va', ('ū', 'ā'): 'vā', ('ū', 'i'): 'vi', ('ū', 'ī'): 'vī', ('ū', 'e'): 've',
    ('ṛ', 'a'): 'ra', ('ṛ', 'ā'): 'rā', ('ṛ', 'i'): 'ri', ('ṛ', 'u'): 'ru',
    
    # Visarga Sandhi (Common Patterns)
    ('aḥ', 'a'): "o'",
    ('aḥ', 'c'): 'aśc', ('aḥ', 'ch'): 'aśch',
    ('aḥ', 't'): 'ast', ('aḥ', 'th'): 'asth',
    ('aḥ', 'ṭ'): 'aṣṭ', ('aḥ', 'ṭh'): 'aṣṭh',
    ('aḥ', 'k'): 'aḥ k', ('aḥ', 'p'): 'aḥ p',
    
    # Consonant / Hal Sandhi
    ('t', 'c'): 'cc', ('t', 'ch'): 'cch',
    ('t', 'j'): 'jj', ('t', 'jh'): 'jjh',
    ('t', 't'): 'tt', ('t', 'l'): 'll',
    ('t', 'ś'): 'cch',
    ('d', 'bh'): 'dbbh',
    ('m', 'k'): 'ṃk', ('m', 'c'): 'ṃc', ('m', 't'): 'ṃt', ('m', 'p'): 'ṃp',
}

# Reverse Sandhi Map: substring -> list of (w1_end_candidate, w2_start_candidate)
REVERSE_SANDHI: Dict[str, List[Tuple[str, str]]] = {
    'ā': [('a', 'a'), ('a', 'ā'), ('ā', 'a'), ('ā', 'ā')],
    'ī': [('i', 'i'), ('i', 'ī'), ('ī', 'i'), ('ī', 'ī')],
    'ū': [('u', 'u'), ('u', 'ū'), ('ū', 'u'), ('ū', 'ū')],
    'e': [('a', 'i'), ('a', 'ī'), ('ā', 'i'), ('ā', 'ī')],
    'o': [('a', 'u'), ('a', 'ū'), ('ā', 'u'), ('ā', 'ū')],
    "o'": [('aḥ', 'a'), ('as', 'a'), ('o', 'a')],
    'ai': [('a', 'e'), ('ā', 'e'), ('a', 'ai'), ('ā', 'ai')],
    'au': [('a', 'o'), ('ā', 'o'), ('a', 'au'), ('ā', 'au')],
    'ya': [('i', 'a'), ('ī', 'a')],
    'yā': [('i', 'ā'), ('ī', 'ā')],
    'yu': [('i', 'u'), ('ī', 'u')],
    'ye': [('i', 'e'), ('ī', 'e')],
    'yo': [('i', 'o'), ('ī', 'o')],
    'va': [('u', 'a'), ('ū', 'a')],
    'vā': [('u', 'ā'), ('ū', 'ā')],
    'vi': [('u', 'i'), ('ū', 'i')],
    've': [('u', 'e'), ('ū', 'e')],
    'āv': [('au', '')],
    'āy': [('ai', '')],
    'av': [('o', '')],
    'ay': [('e', '')],
    'ra': [('ṛ', 'a'), ('r', 'a')],
    'rā': [('ṛ', 'ā'), ('r', 'ā')],
    'cc': [('t', 'c'), ('d', 'c')],
    'cch': [('t', 'ch'), ('t', 'ś'), ('d', 'ch')],
    'jj': [('t', 'j'), ('d', 'j')],
    'll': [('t', 'l'), ('d', 'l')],
    'nn': [('t', 'n'), ('n', 'n')],
    'mm': [('t', 'm'), ('m', 'm')],
    'śc': [('ḥ', 'c'), ('s', 'c'), ('aḥ', 'c')],
    'ṣṭ': [('ḥ', 'ṭ'), ('s', 'ṭ'), ('aḥ', 'ṭ')],
    'st': [('aḥ', 't'), ('ḥ', 't'), ('s', 't')],
    'ma': [('m', 'a'), ('m', 'ā')],
    'mā': [('m', 'ā'), ('m', 'a')],
    'mi': [('m', 'i'), ('m', 'ī')],
    'mī': [('m', 'ī'), ('m', 'i')],
    'mu': [('m', 'u'), ('m', 'ū')],
    'ru': [('ḥ', 'u'), ('aḥ', 'u'), ('uḥ', 'u'), ('iḥ', 'u')],
    're': [('ḥ', 'e'), ('aḥ', 'e'), ('iḥ', 'e'), ('uḥ', 'e')]
}

# Substrings to search for in text
SANDHI_MARKERS = list(REVERSE_SANDHI.keys())


def apply_sandhi(word1: str, word2: str) -> str:
    """Apply forward Sandhi rules to join two Sanskrit words."""
    if not word1 or not word2:
        return word1 + word2
        
    w1 = word1.strip()
    w2 = word2.strip()
    
    # Check 2-character endings first (e.g. 'aḥ')
    for end_len in (2, 1):
        if len(w1) >= end_len:
            end1 = w1[-end_len:]
            base1 = w1[:-end_len]
            
            for start_len in (2, 1):
                if len(w2) >= start_len:
                    start2 = w2[:start_len]
                    rest2 = w2[start_len:]
                    
                    if (end1, start2) in SANDHI_RULES:
                        return base1 + SANDHI_RULES[(end1, start2)] + rest2
                        
    # Visarga with following voiced consonant
    if w1.endswith('aḥ') and w2[0] in VOICED_CONSONANTS:
        return w1[:-2] + 'o ' + w2
        
    # Standard fallback: just concatenation with space or direct abutment
    return f"{w1} {w2}"


def detect_phonetic_junctions(text: str) -> List[Dict[str, Any]]:
    """
    Identifies potential sandhi junction points in a word.
    """
    junctions = []
    text_clean = text.lower()
    for marker in SANDHI_MARKERS:
        start = 0
        while True:
            idx = text_clean.find(marker, start)
            if idx == -1:
                break
            # Ignore boundaries at word edges for internal markers
            if 1 <= idx <= len(text_clean) - len(marker) - 1:
                junctions.append({
                    'index': idx,
                    'marker': marker,
                    'left_sub': text[:idx],
                    'right_sub': text[idx + len(marker):]
                })
            start = idx + 1

    return sorted(junctions, key=lambda x: x['index'])


ILLEGAL_INITIAL_CLUSTERS = ('rv', 'rk', 'rt', 'rd', 'rn', 'rm', 'ry', 'rṣ', 'ts', 'itr', 'nt', 'mps', 'ṅk', 'ñc', 'ṇṭ', 'ṇḍ')
VALID_SHORT_WORDS = {'tu', 'ca', 'vā', 'hi', 'mā', 'sa', 'te', 'me', 'na', 'tad', 'yad', 'kim', 'eva', 'api', 'iti', 'iva'}
INVALID_PADA_FRAGMENTS = {'eṇa', 'ena', 'eṣu', 'ebhiḥ', 'ānām', 'āṇām', 'asya', 'āya', 'ibhiḥ', 'ubhiḥ', 'iparameśvarau', 'īparameśvarau'}


def is_phonotactically_valid_split(left: str, right: str) -> bool:
    """Ensures candidate words satisfy Sanskrit phonotactic constraints (e.g. valid short words and clusters)."""
    if len(left) < 2 or len(right) < 2:
        return False
    if right in INVALID_PADA_FRAGMENTS:
        return False
    if len(left) == 2 and left not in VALID_SHORT_WORDS:
        return False
    if len(right) == 2 and right not in VALID_SHORT_WORDS:
        return False
    if left.endswith('ḥ') and len(left) <= 3 and left not in ('saḥ', 'kaḥ', 'yaḥ', 'bhoḥ'):
        return False
    if any(right.startswith(cl) for cl in ILLEGAL_INITIAL_CLUSTERS):
        return False
    return True


def generate_candidate_splits(compound: str) -> List[Tuple[str, str, str]]:
    """
    Reverse-engineers possible phonetic splits (Vichchhed).
    Returns list of tuples: (left_word, right_word, rule_description)
    """
    candidates = []
    n = len(compound)
    
    # 1. Direct concatenation (Samāsa without Sandhi)
    for i in range(2, n - 1):
        left = compound[:i]
        right = compound[i:]
        if is_phonotactically_valid_split(left, right):
            candidates.append((left, right, "Direct Abutment (No Sandhi)"))
        
    # 2. Phonetic Sandhi reversals
    for marker, rules in REVERSE_SANDHI.items():
        idx = 0
        while True:
            pos = compound.find(marker, idx)
            if pos == -1:
                break
            if 1 <= pos <= n - len(marker) - 1:
                left_prefix = compound[:pos]
                right_suffix = compound[pos + len(marker):]
                
                for end_c, start_c in rules:
                    if end_c.startswith(('a', 'ā', 'i', 'ī', 'u', 'ū', 'ṛ', 'e', 'o', 'ai', 'au', 'aḥ')) and left_prefix.endswith(('a', 'ā', 'i', 'ī', 'u', 'ū')):
                        base_left = left_prefix[:-1]
                    else:
                        base_left = left_prefix
                    cand_left = base_left + end_c
                    cand_right = start_c + right_suffix
                    if is_phonotactically_valid_split(cand_left, cand_right):
                        candidates.append((cand_left, cand_right, f"Sandhi Split on '{marker}' ({end_c} + {start_c})"))
            idx = pos + 1
            
    return candidates
