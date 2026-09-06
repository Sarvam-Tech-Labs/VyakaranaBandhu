"""
Unified Sanskrit Morphological Classifier
Combines Pāṇinian Rule Engine with Machine Learning Ensemble for high-accuracy disambiguation.
Includes granular subtyping, Vigraha (compound expansion), Padacheda, and Aṣṭādhyāyī Sūtras.
Supports complete multi-word verses & shlokas automatically.
"""

from typing import Dict, Any, List, Union
from .normalizer import is_devanagari, devanagari_to_iast, iast_to_devanagari, clean_text, normalize_iast
from .phonetics import detect_phonetic_junctions, generate_candidate_splits
from .rule_engine import PaninianRuleEngine
from .ml_model import SanskritMLClassifier
from .subtypes import analyze_samasa_subtype, analyze_sandhi_subtype
from .prakriti_pratyaya import analyze_prakriti_pratyaya
from .morphology import COMMON_STEMS, is_bare_stem, is_inflected_pada
from .verse_analyzer import VerseAnalyzer, is_complete_verse


class SanskritClassifier:
    """
    Main Classifier Interface for Sanskrit Strings.
    Categorizes input into: 'None', 'Sandhi Only', 'Samāsa Only', 'Both'.
    Supports single words, compound phrases, and full multi-line verses.
    """
    def __init__(self, load_pretrained_ml: bool = True):
        self.rule_engine = PaninianRuleEngine()
        self.ml_classifier = SanskritMLClassifier()
        self.verse_analyzer = VerseAnalyzer(self)
        
        # Try loading saved model or train on canonical dataset
        if load_pretrained_ml:
            loaded = self.ml_classifier.load()
            if not loaded:
                self.ml_classifier.train(save=True)

    def classify(self, text: str, is_verse_subcall: bool = False) -> Dict[str, Any]:
        """
        Classifies an input Sanskrit string in IAST or Devanagari.
        Automatically switches to whole-verse analysis if multiple tokens/daṇḍas are provided.
        """
        raw_text = text.strip()
        if not raw_text:
            return {
                "input_text": text,
                "iast": "",
                "devanagari": "",
                "predicted_class": "None",
                "confidence": 1.0,
                "subtype": "None",
                "sutra": "N/A",
                "vigraha_or_padacheda": "",
                "explanation": "Empty input string.",
                "splits": [],
                "ml_probabilities": {}
            }

        # 0. Whole-Verse Mode (When input is a multi-word shloka or sentence)
        if not is_verse_subcall and is_complete_verse(raw_text):
            return self.verse_analyzer.analyze_verse(raw_text)

        # Check script & normalize
        was_devanagari = is_devanagari(raw_text)
        iast_normalized = devanagari_to_iast(raw_text) if was_devanagari else normalize_iast(raw_text)
        devanagari_repr = raw_text if was_devanagari else iast_to_devanagari(iast_normalized)
        cleaned_iast = clean_text(iast_normalized)

        # 1. Evaluate with Pāṇinian Rule Engine
        rule_res = self.rule_engine.evaluate(cleaned_iast)
        rule_class = rule_res['class']
        rule_conf = rule_res['confidence']

        # 2. Evaluate with ML Model
        ml_probs = self.ml_classifier.predict_proba([cleaned_iast])[0]
        ml_best_class = max(ml_probs.items(), key=lambda x: x[1])[0]
        ml_best_prob = ml_probs[ml_best_class]

        # 3. Hybrid Decision Arbiter
        if rule_conf >= 0.90:
            final_class = rule_class
            final_conf = rule_conf
            explanation = rule_res['explanation']
        elif rule_class == ml_best_class:
            final_class = rule_class
            final_conf = max(rule_conf, ml_best_prob)
            explanation = rule_res['explanation']
        elif ml_best_prob > 0.85 and rule_conf < 0.80:
            final_class = ml_best_class
            final_conf = ml_best_prob
            explanation = f"Classified by statistical ML ensemble with high confidence ({ml_best_prob*100:.1f}%). {rule_res['explanation']}"
        else:
            final_class = rule_class
            final_conf = (rule_conf * 0.6) + (ml_probs.get(rule_class, 0.25) * 0.4)
            explanation = rule_res['explanation']

        # 4. Extract Left & Right elements for subtyping
        left_tok, right_tok, rule_desc = "", "", ""
        if rule_res.get('splits') and len(rule_res['splits']) > 0:
            s0 = rule_res['splits'][0]
            if len(s0) >= 3:
                left_tok, right_tok, rule_desc = s0[0], s0[1], s0[2]

        # 5. Granular Subtyping & Vigraha / Padacheda Generation
        clean_key = cleaned_iast.lower().replace(" ", "").replace("'", "").replace("’", "")
        padacheda = ""
        samasa = ""
        sandhi_steps = []
        meaning = ""
        
        if final_class == 'Samāsa Only':
            sub_info = analyze_samasa_subtype(left_tok, right_tok, cleaned_iast)
            subtype = sub_info['subtype']
            sutra = sub_info['sutra']
            padacheda = sub_info.get('padacheda', '')
            samasa = sub_info.get('samasa', '')
            sandhi_steps = sub_info.get('sandhi_steps', [])
            meaning = sub_info.get('meaning', '')
            vigraha_or_padacheda = {
                'type': 'Vigraha (Analytical Compound Expansion)',
                'iast': sub_info.get('vigraha_iast', ''),
                'devanagari': sub_info.get('vigraha_dev', '')
            }
            deep_commentary = sub_info['commentary']

        elif final_class == 'Sandhi Only':
            sub_info = analyze_sandhi_subtype(left_tok, right_tok, rule_desc, cleaned_iast)
            subtype = sub_info['subtype']
            sutra = sub_info['sutra']
            padacheda = sub_info.get('padacheda', '')
            samasa = sub_info.get('samasa', 'N/A')
            sandhi_steps = sub_info.get('sandhi_steps', [])
            meaning = sub_info.get('meaning', '')
            vigraha_or_padacheda = {
                'type': 'Padacheda (Sentential Word Disjunction)',
                'iast': sub_info.get('padacheda_iast', ''),
                'devanagari': sub_info.get('padacheda_dev', '')
            }
            deep_commentary = sub_info['commentary']

        elif final_class == 'Both':
            sam_info = analyze_samasa_subtype(left_tok, right_tok, cleaned_iast)
            san_info = analyze_sandhi_subtype(left_tok, right_tok, rule_desc, cleaned_iast)
            subtype = f"{sam_info['subtype']} + {san_info['subtype']}"
            sutra = f"{sam_info['sutra']} & {san_info['sutra']}"
            # If compound has external sentential phonetic junction (pada + pada), use Sandhi padacheda.
            # Otherwise (compound internal expansion / Vigraha), use Samāsa padacheda.
            if san_info.get('padacheda') and left_tok not in ('mahā', 'dharma', 'kuru', 'pāṇḍava', 'drupada', 'bhīma', 'arjuna') and (left_tok.endswith(('ām', 'm', 'ḥ')) or right_tok in ('ācārya', 'iva', 'ca', 'eva')):
                padacheda = san_info['padacheda']
            else:
                padacheda = sam_info.get('padacheda') or san_info.get('padacheda', '')
            samasa = sam_info.get('samasa', '')
            sandhi_steps = san_info.get('sandhi_steps', [])
            meaning = sam_info.get('meaning', '')
            vigraha_or_padacheda = {
                'type': 'Vigraha & Padacheda (Compound Expansion with Sandhi Split)',
                'iast': f"Vigraha: {sam_info.get('vigraha_iast', '')} | Sandhi Split: {san_info.get('padacheda_iast', '')}",
                'devanagari': f"विग्रहः {sam_info.get('vigraha_dev', '')} | सन्धिच्छेदः {san_info.get('padacheda_dev', '')}"
            }
            deep_commentary = f"{sam_info['commentary']} Concurrently, {sam_info['commentary']}"

        else: # None
            if cleaned_iast.endswith(('ti', 'te', 'nti', 'nte', 'si', 'mi', 'tu', 'at')):
                subtype = "Simplex Verb (Ākhyāta / Dhātu + tiṅ)"
                sutra = "tiṅastiṅ (8.1.28) / bhūvādayo dhātavaḥ (1.3.1)"
                padacheda = f"{devanagari_repr} ({cleaned_iast})"
            # 1. Phonological Restoration: Visarga Utva (haśi ca 6.1.114: -aḥ + voiced -> -o)
            elif cleaned_iast.endswith('o') and len(cleaned_iast) > 3 and not cleaned_iast.startswith(('bho', 'aho')):
                base = cleaned_iast[:-1] + 'a'
                subtype = "Simplex Noun with Visarga Utva (विसर्ग उत्वः / हशि च)"
                sutra = "haśi ca (6.1.114) / ato roraplutād aplute (6.1.113)"
                padacheda = f"{iast_to_devanagari(base)}ः ({base[:-1]}aḥ)"
            # 2. Phonological Restoration: Visarga Lopa (lopaḥ śākalyasya 8.3.19: -āḥ + voiced/vowel -> -ā)
            elif cleaned_iast.endswith('ā') and len(cleaned_iast) > 3 and ((cleaned_iast[:-1] + 'a') in COMMON_STEMS or cleaned_iast in ('śūrā', 'sura')):
                subtype = "Simplex Noun with Visarga Lopa (विसर्ग लोपः / भोभगोअघोअपूर्वस्य)"
                sutra = "lopaḥ śākalyasya (8.3.19) / bho-bhago-adho-apūrvasya yo'śi (8.3.17)"
                padacheda = f"{devanagari_repr}ः ({cleaned_iast}ḥ)"
            else:
                subtype = "Simplex Noun (Nāma / Prātipadika + suP)"
                sutra = "suptiṅantam padam (1.4.14) / arthavad adhātur apratyayaḥ prātipadikam (1.2.45)"
                padacheda = f"{devanagari_repr} ({cleaned_iast})"
            samasa = "N/A (Simplex Word)"
            sandhi_steps = []
            meaning = "Single independent inflected Pada."
            vigraha_or_padacheda = {
                'type': 'Simplex Derivation',
                'iast': f"{cleaned_iast} (Single independent Pada)",
                'devanagari': f"{devanagari_repr} (केवल पद)"
            }
            deep_commentary = "Standalone inflected unit derived with primary/secondary suffixes, without multi-stem compounding or external sentential Sandhi."

        # Prepare candidate split formatting
        splits_formatted = []
        for split in rule_res.get('splits', []):
            if len(split) >= 3:
                l, r, desc = split[0], split[1], split[2]
                splits_formatted.append({
                    "left_iast": l,
                    "left_dev": iast_to_devanagari(l) if l else "",
                    "right_iast": r,
                    "right_dev": iast_to_devanagari(r) if r else "",
                    "description": desc
                })

        # 6. Prakṛti-Pratyaya Vibhāga (Root & Suffix Derivation)
        pp_info = analyze_prakriti_pratyaya(cleaned_iast)

        return {
            "is_verse": False,
            "input_text": raw_text,
            "iast": iast_normalized,
            "devanagari": devanagari_repr,
            "predicted_class": final_class,
            "confidence": round(float(final_conf), 4),
            "subtype": subtype,
            "sutra": sutra,
            "padacheda": padacheda,
            "samasa": samasa,
            "sandhi_steps": sandhi_steps,
            "meaning": meaning,
            "vigraha_or_padacheda": vigraha_or_padacheda,
            "prakriti_pratyaya": pp_info,
            "deep_commentary": deep_commentary,
            "rule_name": rule_res.get('rule_name', 'Hybrid'),
            "explanation": explanation,
            "splits": splits_formatted,
            "ml_probabilities": {k: round(v, 4) for k, v in ml_probs.items()}
        }

    def batch_classify(self, texts: List[str]) -> List[Dict[str, Any]]:
        """Classify a list of Sanskrit strings."""
        return [self.classify(t) for t in texts]
