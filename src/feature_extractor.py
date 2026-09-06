"""
Feature Extractor for Sanskrit Morphological Classification
Extracts rich linguistic, phonetic, and character-level statistical features.
"""

import re
from typing import List, Dict, Any

try:
    import numpy as np
except ImportError:
    np = None

try:
    from sklearn.feature_extraction.text import TfidfVectorizer
except ImportError:
    TfidfVectorizer = None

from .phonetics import (
    detect_phonetic_junctions, generate_candidate_splits,
    VOWELS, DIPHTHONGS
)
from .morphology import (
    COMMON_STEMS, INDECLINABLES, NOMINAL_INFLECTIONS, VERBAL_INFLECTIONS,
    analyze_morphology, is_inflected_pada, is_bare_stem
)
from .normalizer import clean_text


class SanskritFeatureExtractor:
    """
    Extracts dense linguistic feature vectors and sparse character n-gram matrices.
    """
    def __init__(self, ngram_range=(2, 5), max_features=500):
        self.ngram_range = ngram_range
        self.max_features = max_features
        if TfidfVectorizer is not None:
            self.vectorizer = TfidfVectorizer(
                analyzer='char_wb',
                ngram_range=self.ngram_range,
                max_features=self.max_features
            )
        else:
            self.vectorizer = None
        self.is_fitted = False

    def extract_linguistic_features(self, raw_text: str) -> Dict[str, float]:
        """
        Extracts engineered phonetic and morphological indicators for a single text.
        """
        text = clean_text(raw_text)
        n = len(text)
        if n == 0:
            return {k: 0.0 for k in self.get_feature_names()}
            
        words = text.split()
        num_words = len(words)
        
        # 1. Structural features
        has_space = 1.0 if num_words > 1 else 0.0
        has_avagraha = 1.0 if "'" in text else 0.0
        
        # 2. Phonetic counts
        diphthong_count = sum(1 for c in text if c in {'e', 'o'}) + text.count('ai') + text.count('au')
        long_vowels = sum(1 for c in text if c in {'ā', 'ī', 'ū', 'ṝ'})
        visarga_count = text.count('ḥ')
        anusvara_count = text.count('ṃ')
        retroflex_count = sum(1 for c in text if c in {'ṭ', 'ṭh', 'ḍ', 'ḍh', 'ṇ', 'ṣ'})
        
        # Double consonant clusters
        double_consonants = len(re.findall(r'([a-zāīūṛṝṭḍṇśṣ])\1', text)) + len(re.findall(r'cch|ṣṭ|śc|st|ddh|tth', text))
        
        # 3. Morphological Stem & Prefix Analysis
        starts_with_known_stem = 0.0
        for stem in COMMON_STEMS:
            if text.startswith(stem) and len(text) > len(stem):
                starts_with_known_stem = 1.0
                break
                
        starts_with_avyaya = 0.0
        for avy in INDECLINABLES:
            if text.startswith(avy) and len(text) > len(avy):
                starts_with_avyaya = 1.0
                break
                
        # 4. Endings
        ends_with_case = 1.0 if any(text.endswith(inf) for inf in NOMINAL_INFLECTIONS) else 0.0
        ends_with_verb = 1.0 if any(text.endswith(inf) for inf in VERBAL_INFLECTIONS) else 0.0
        
        # 5. Junction & Candidate Split Analysis
        junctions = detect_phonetic_junctions(text)
        junction_count = float(len(junctions))
        
        splits = generate_candidate_splits(text)
        stem_pada_direct = 0.0
        stem_pada_sandhi = 0.0
        pada_pada_sandhi = 0.0
        
        if num_words > 1:
            # Multi-word string analysis
            w1_morph = analyze_morphology(words[0])
            w2_morph = analyze_morphology(words[1]) if len(words) > 1 else 'unknown'
            
            if w1_morph == 'stem':
                stem_pada_direct = 1.0
            elif w1_morph == 'pada' and w2_morph in ('pada', 'unknown'):
                pada_pada_sandhi = 1.0
        else:
            # Single continuous string analysis
            for left, right, rule_type in splits:
                left_morph = analyze_morphology(left)
                right_morph = analyze_morphology(right)
                
                if "Direct Abutment" in rule_type:
                    if left_morph == 'stem' and right_morph in ('pada', 'stem') and not is_inflected_pada(left):
                        stem_pada_direct = 1.0
                    elif left_morph == 'pada' and right_morph in ('pada', 'avyaya'):
                        pada_pada_sandhi = 1.0
                else: # Sandhi split
                    if left_morph == 'stem' and right_morph in ('pada', 'stem'):
                        stem_pada_sandhi = 1.0
                    elif left_morph == 'pada' and right_morph in ('pada', 'avyaya'):
                        pada_pada_sandhi = 1.0

        features = {
            'length': float(n),
            'num_words': float(num_words),
            'has_space': has_space,
            'has_avagraha': has_avagraha,
            'diphthong_count': float(diphthong_count),
            'long_vowels': float(long_vowels),
            'visarga_count': float(visarga_count),
            'anusvara_count': float(anusvara_count),
            'retroflex_count': float(retroflex_count),
            'double_consonants': float(double_consonants),
            'starts_with_known_stem': starts_with_known_stem,
            'starts_with_avyaya': starts_with_avyaya,
            'ends_with_case': ends_with_case,
            'ends_with_verb': ends_with_verb,
            'junction_count': junction_count,
            'stem_pada_direct': stem_pada_direct,
            'stem_pada_sandhi': stem_pada_sandhi,
            'pada_pada_sandhi': pada_pada_sandhi
        }
        return features

    def get_feature_names(self) -> List[str]:
        return [
            'length', 'num_words', 'has_space', 'has_avagraha',
            'diphthong_count', 'long_vowels', 'visarga_count', 'anusvara_count',
            'retroflex_count', 'double_consonants', 'starts_with_known_stem',
            'starts_with_avyaya', 'ends_with_case', 'ends_with_verb',
            'junction_count', 'stem_pada_direct', 'stem_pada_sandhi', 'pada_pada_sandhi'
        ]

    def fit(self, texts: List[str]):
        """Fit character n-gram TF-IDF vectorizer."""
        if self.vectorizer is not None:
            cleaned_texts = [clean_text(t) for t in texts]
            self.vectorizer.fit(cleaned_texts)
        self.is_fitted = True
        return self

    def transform(self, texts: List[str]):
        """
        Combine sparse TF-IDF character n-grams with dense linguistic features.
        """
        if self.vectorizer is None or np is None:
            # Fallback to returning dense lists
            dense_list = []
            for t in texts:
                feat_dict = self.extract_linguistic_features(t)
                dense_list.append([feat_dict[k] for k in self.get_feature_names()])
            return dense_list

        cleaned_texts = [clean_text(t) for t in texts]
        
        # 1. TF-IDF character n-grams
        if not self.is_fitted:
            self.fit(texts)
        tfidf_features = self.vectorizer.transform(cleaned_texts).toarray()
        
        # 2. Dense linguistic features
        dense_list = []
        for t in texts:
            feat_dict = self.extract_linguistic_features(t)
            dense_list.append([feat_dict[k] for k in self.get_feature_names()])
            
        dense_features = np.array(dense_list)
        
        # Concatenate both
        return np.hstack((tfidf_features, dense_features))

    def fit_transform(self, texts: List[str]):
        self.fit(texts)
        return self.transform(texts)
