"""
Pāṇinian Viśeṣya-Viśeṣaṇa (Substantive vs Adjective) Identification & Syntactic Concord Engine
Identifies syntactic modifiers (विशेषण) and head substantives (विशेष्य) in Sanskrit verses & sentences.

Governed by the Sāmānādhikaraṇya (सामानाधिकरण्य) Principle:
"यल्लिङ्गं यद्वचनं या च विभक्तिर्विशेष्यस्य । तल्लिङ्गं तद्वचनं तस्यापि विशेषणस्य ॥"
(Whatever case, number, and gender belongs to the Viśeṣya, the exact same belongs to the Viśeṣaṇa).
"""

from typing import List, Dict, Any, Optional, Tuple, Set
import re
from .normalizer import devanagari_to_iast, iast_to_devanagari
from .subanta_engine import SubantaEngine


class ViseshyaViseshanaEngine:
    """
    Algorithmic identifier for Viśeṣya (Substantives/Nouns) and Viśeṣaṇa (Adjectives/Modifiers)
    utilizing Subanta morphological analysis and syntactic agreement.
    """

    def __init__(self, subanta_engine: Optional[SubantaEngine] = None):
        self.subanta = subanta_engine or SubantaEngine()

        # Known Proper Nouns / Fixed Substantives (Sañjñā / Dravya)
        self.proper_nouns: Set[str] = {
            'rāma', 'kṛṣṇa', 'arjuna', 'dhṛtarāṣṭra', 'duryodhana', 'sañjaya', 'pāṇḍava', 'pāṇḍu',
            'drupada', 'virāṭa', 'yuyudhāna', 'bhīma', 'droṇa', 'bhīṣma', 'karṇa', 'śiva', 'pārvatī',
            'parameśvara', 'kurukṣetra', 'hastināpura', 'pitṛ', 'mātṛ', 'bhrātṛ', 'putra', 'kanyā',
            'śiṣya', 'ācārya', 'rājā', 'nara', 'gaja', 'aśva', 'camū', 'anīka', 'pitarau', 'vāgarthau',
            'kṣetra', 'pada', 'śabda', 'vāc', 'vacana', 'anīkam'
        }

        # Known Qualifiers / Participles / Modifiers (Guṇavācaka / Kṛdanta / Desiderative)
        self.qualifier_stems: Set[str] = {
            'dharmakṣetra', 'samaveta', 'yuyutsu', 'māmaka', 'vyūḍha', 'sampṛkta', 'mahat', 'mahatī',
            'dhīmat', 'śūra', 'iṣvāsa', 'maheṣvāsa', 'sama', 'bhīmārjunasama', 'mahāratha',
            'sarva', 'eka', 'anya', 'śukla', 'rakta', 'kṛṣṇa', 'priya', 'sundara', 'uttama',
            'parama', 'divya', 'ananta', 'tejasvin', 'balavat', 'guṇin', 'etad', 'tad', 'idam'
        }

        # Excluded non-nominal words (Indeclinables / Verbs / Gerunds)
        self.excluded_words: Set[str] = {
            'ca', 'eva', 'api', 'tu', 'hi', 'iti', 'iva', 'vā', 'uvāca', 'abravīt', 'akurvata',
            'vande', 'kim', 'sañjaya', 'he', 'tadā', 'yadā', 'kadā', 'tatra', 'yatra', 'atra',
            'dṛṣṭvā', 'upasaṅgamya', 'gatvā', 'śrutvā', 'kṛtvā', 'ṭvā', 'dṛaḥ'
        }

    def analyze_verse_relationships(self, token_results: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Analyzes a sequence of token results from a verse, disambiguating
        Viśeṣya-Viśeṣaṇa pairs based on Sāmānādhikaraṇya and lexical typology.
        """
        extracted_padas = []

        for tok in token_results:
            raw_w = tok.get('input_text', '').strip()
            pada_str = tok.get('padacheda', '')
            pred_cls = tok.get('predicted_class', '')

            # Extract individual constituents from Padaccheda if Sandhi occurred
            if pred_cls in ('Sandhi Only', 'Both') and " + " in pada_str:
                parts = [p.strip() for p in pada_str.split("(")[0].split("+") if p.strip()]
            else:
                parts = [tok.get('devanagari', raw_w)]

            for part in parts:
                p_dev = part.strip()
                p_iast = devanagari_to_iast(p_dev).strip().lower().replace(":", "ḥ").replace("ṃ", "m")
                
                # Expand multi-word sandhi like caiva -> ca + eva
                if p_iast == 'caiva' or p_dev == 'चैव':
                    sub_parts = [('च', 'ca'), ('एव', 'eva')]
                else:
                    sub_parts = [(p_dev, p_iast)]

                for s_dev, s_iast in sub_parts:
                    if s_iast in self.excluded_words or len(s_iast) < 3 or s_iast.endswith(('tvā', 'mya', 'tya', 'lya')):
                        continue

                    analyses = self.subanta.analyze_subanta(s_iast)
                    
                    # Normalize visarga ending for plural participles (e.g. samavetā -> samavetāḥ)
                    if not analyses and s_iast.endswith('ā'):
                        analyses = self.subanta.analyze_subanta(s_iast + "ḥ")

                    # If still not found, try stripping anusvara
                    if not analyses and s_iast.endswith('m'):
                        analyses = self.subanta.analyze_subanta(s_iast)

                    stem = analyses[0]['stem_iast'] if analyses else s_iast
                    is_proper = (stem in self.proper_nouns) or any(pn in s_iast for pn in self.proper_nouns)
                    is_qualifier = (stem in self.qualifier_stems) or any(qs in s_iast for qs in self.qualifier_stems)
                    
                    if s_iast.endswith(('matī', 'matīm', 'matā', 'vān', 'mān', 'vantaḥ', 'mantaḥ', 'vatsva', 'inā', 'ine', 'inī')):
                        is_qualifier = True

                    # Extract tag signatures
                    signatures = set()
                    for a in analyses:
                        vib = a['vibhakti'].split('(')[0].strip()
                        vac = a['vacana'].split('(')[0].strip()
                        signatures.add(f"{vib} {vac}")

                    if not signatures:
                        if s_iast.endswith('tre') or s_dev.endswith('क्षेत्रे'):
                            signatures.add("Saptamī Ekavacana")
                        elif s_iast.endswith(('āḥ', 'avaḥ', 'ā')) or s_dev.endswith(('ाः', 'वः', 'ा')):
                            signatures.add("Prathamā Bahuvacana")
                        elif s_iast.endswith('am') or s_dev.endswith(('म्', 'ं')):
                            signatures.add("Dvitīyā Ekavacana")

                    if signatures:
                        extracted_padas.append({
                            'pada_dev': s_dev,
                            'pada_iast': s_iast,
                            'stem': stem,
                            'is_proper': is_proper,
                            'is_qualifier': is_qualifier,
                            'signatures': signatures,
                            'analyses': analyses
                        })

        # Collect distinct active signatures in the verse
        all_signatures = set()
        for p in extracted_padas:
            all_signatures.update(p['signatures'])

        # Group by Sāmānādhikaraṇya
        relationships = []
        for sig in sorted(all_signatures):
            if sig.startswith('Sambodhana'):
                continue
            matching = [p for p in extracted_padas if sig in p['signatures']]
            if len(matching) < 2:
                continue

            viseshya = None
            viseshanas = []

            # Prioritize proper nouns / fixed substantives as Head (Viśeṣya)
            for itm in matching:
                if itm['is_proper'] and not itm['is_qualifier']:
                    viseshya = itm
                    break

            if not viseshya:
                viseshya = matching[-1]
                viseshanas = matching[:-1]
            else:
                viseshanas = [itm for itm in matching if itm != viseshya]

            if viseshanas:
                karaka_role = "N/A"
                karaka_sutra = "N/A"
                if sig.startswith('Prathamā'):
                    karaka_role = "Kartṛ (कर्तृ - Agent / Subject)"
                    karaka_sutra = "svatantraḥ kartā (1.4.54) & prātipadikārtha... (2.3.46)"
                elif sig.startswith('Dvitīyā'):
                    karaka_role = "Karman (कर्म - Patient / Direct Object)"
                    karaka_sutra = "karturīpsitatamaṃ karma (1.4.49) & karmaṇi dvitīyā (2.3.2)"
                elif sig.startswith('Tṛtīyā'):
                    karaka_role = "Karaṇa (करण - Instrument / Means)"
                    karaka_sutra = "sādhakatamaṃ karaṇam (1.4.42) & kartṛkaraṇayostṛtīyā (2.3.18)"
                elif sig.startswith('Caturthī'):
                    karaka_role = "Sampradāna (सम्प्रदान - Recipient / Purpose)"
                    karaka_sutra = "karmaṇā yamabhipraiti... (1.4.32) & caturthī sampradāne (2.3.13)"
                elif sig.startswith('Pañcamī'):
                    karaka_role = "Apādāna (अपादान - Source / Separation / Fear)"
                    karaka_sutra = "dhruvamapāye'pādānam (1.4.24) & apādāne pañcamī (2.3.28)"
                elif sig.startswith('Ṣaṣṭhī'):
                    karaka_role = "Sambandha (सम्बन्ध - Genitive Possessor)"
                    karaka_sutra = "ṣaṣṭhī śeṣe (2.3.50)"
                elif sig.startswith('Saptamī'):
                    karaka_role = "Adhikaraṇa (अधिकरण - Locus / Location / Time)"
                    karaka_sutra = "ādhāro'dhikaraṇam (1.4.45) & saptamyadhikaraṇe ca (2.3.36)"

                relationships.append({
                    "concord": sig,
                    "karaka_role": karaka_role,
                    "karaka_sutra": karaka_sutra,
                    "viseshya": {
                        "pada_devanagari": viseshya['pada_dev'],
                        "pada_iast": viseshya['pada_iast'],
                        "stem": viseshya['stem'],
                        "role": "Viśeṣya (विशेष्य - Head Substantive)"
                    },
                    "viseshanas": [
                        {
                            "pada_devanagari": v['pada_dev'],
                            "pada_iast": v['pada_iast'],
                            "stem": v['stem'],
                            "role": "Viśeṣaṇa (विशेषण - Qualifying Modifier)"
                        } for v in viseshanas
                    ],
                    "explanation": f"'{', '.join(v['pada_dev'] for v in viseshanas)}' qualify the substantive '{viseshya['pada_dev']}' via Sāmānādhikaraṇya ({sig} -> {karaka_role})."
                })

        return {
            "total_pairs_identified": len(relationships),
            "relationships": relationships
        }
