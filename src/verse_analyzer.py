"""
Sanskrit Complete Verse & Shloka Analyzer (Purely Algorithmic - No Hardcoded Lookups)
Processes multi-word verses & sentences dynamically:
1. Tokenizes by whitespace, daṇḍas (। , ॥), and punctuation.
2. Runs morphological classification and Subanta validation on every constituent token.
3. Assembles dynamic Padacheda, Prakṛti-Pratyaya pipeline, and Anvaya.
4. Identifies Viśeṣya-Viśeṣaṇa (Substantive vs Adjective) dependencies via Sāmānādhikaraṇya.
"""

import re
from typing import Dict, Any, List
from .normalizer import is_devanagari, devanagari_to_iast, iast_to_devanagari, normalize_iast
from .anvaya import generate_anvaya
from .viseshya_viseshana import ViseshyaViseshanaEngine
from .chandas import meter_summary


def is_complete_verse(text: str) -> bool:
    """
    Determines if input is a complete verse/sentence (multiple words, punctuation, or daṇḍas).
    """
    raw = text.strip()
    words = [w for w in re.split(r'[\s।॥|,;]+', raw) if w.strip() and not re.match(r'^[\d०-९\(\)\[\]\.\-]+$', w.strip())]
    if len(words) <= 1:
        return False
    has_dandas = '।' in raw or '॥' in raw or '|' in raw or '\n' in raw
    return has_dandas or len(words) >= 3


def extract_verse_tokens(text: str) -> List[str]:
    """
    Tokenizes verse into constituent words/compounds while preserving sequence.
    Strips verse numbering (e.g. ॥ १ ॥, 1, etc.) and punctuation.
    """
    normalized = text.replace(' :', 'ः').replace(':', 'ः')
    raw_tokens = re.split(r'[\s।॥|,\n]+', normalized)
    clean_tokens = [
        t.strip() for t in raw_tokens 
        if t.strip() 
        and not t.strip() in ('।', '॥', '|', '||') 
        and not re.match(r'^[\d०-९\(\)\[\]\.\-]+$', t.strip())
    ]
    return clean_tokens


class VerseAnalyzer:
    """
    Coordinates whole-verse analysis, token-level classification, and padacheda assembly.
    100% Purely dynamic without hardcoded database lookups.
    """
    def __init__(self, classifier_instance):
        self.classifier = classifier_instance
        self.viseshya_engine = ViseshyaViseshanaEngine()

    def analyze_verse(self, verse_text: str) -> Dict[str, Any]:
        raw_text = verse_text.strip()
        tokens = extract_verse_tokens(raw_text)

        was_devanagari = is_devanagari(raw_text)
        iast_verse = devanagari_to_iast(raw_text) if was_devanagari else normalize_iast(raw_text)
        devanagari_verse = raw_text if was_devanagari else iast_to_devanagari(iast_verse)

        # Classify each token individually using the dynamic classifier
        token_results = []
        class_counts = {"None": 0, "Sandhi Only": 0, "Samāsa Only": 0, "Both": 0}
        full_padacheda_list = []
        prakriti_pratyaya_list = []

        for tok in tokens:
            res = self.classifier.classify(tok, is_verse_subcall=True)
            token_results.append(res)
            cls = res.get('predicted_class', 'None')
            class_counts[cls] = class_counts.get(cls, 0) + 1
            
            # Extract Padacheda or stem form
            pada = res.get('padacheda') or res.get('devanagari') or tok
            full_padacheda_list.append(pada)

            # Extract Prakṛti-Pratyaya formula if available
            if res.get('prakriti_pratyaya') and res['prakriti_pratyaya'].get('formula_dev'):
                pp = f"{res['prakriti_pratyaya']['formula_dev']} ({res['prakriti_pratyaya']['formula_iast']})"
                prakriti_pratyaya_list.append(pp)

        # Synthesize Syntactic Prose Order (Anvaya)
        anvaya_res = generate_anvaya(token_results, raw_text)

        # Compute Viśeṣya-Viśeṣaṇa syntactic relationships via Sāmānādhikaraṇya
        viseshya_res = self.viseshya_engine.analyze_verse_relationships(token_results)

        # Chandas: real akṣara scansion and catalog-backed meter identification
        # (src/chandas). Runs on the source text so the Devanāgarī clusters keep
        # their own spans; falls back to an honest "unidentified" rather than a
        # count-based guess. See meter_summary — it never raises.
        chandas = meter_summary(raw_text)
        meter_name = chandas["label"]

        return {
            "is_verse": True,
            "predicted_class": "Verse / Shloka",
            "input_text": raw_text,
            "iast": iast_verse,
            "devanagari": devanagari_verse,
            "token_count": len(tokens),
            "meter": meter_name,
            "chandas": chandas,
            "token_results": token_results,
            "class_summary": class_counts,
            "full_padacheda": "  •  ".join(full_padacheda_list),
            "anvaya": anvaya_res['anvaya_devanagari'],
            "anvaya_iast": anvaya_res['anvaya_iast'],
            "syntactic_roles": anvaya_res['syntactic_roles'],
            "viseshya_viseshana_map": viseshya_res,
            "prakriti_pratyaya_pipeline": "  •  ".join(prakriti_pratyaya_list)
        }
