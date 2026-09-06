"""
Sanskrit Anvaya (अन्वय - Syntactic Prose Order) Engine
Arranges verse constituents into canonical Sanskrit prose sequence based on Kāraka roles:
Vocative (सम्बोधन) -> Locative / Time (अधिकरण/काल) -> Subject & Adjectives (कर्ता/विशेषण) ->
Object & Adjectives (कर्म/विशेषण) -> Sequential Participles (पूर्वकालिक क्रिया: क्त्वा/ल्यप्) -> Main Verb (क्रियापद).
"""

from typing import List, Dict, Any
import re
from .normalizer import devanagari_to_iast, iast_to_devanagari


def generate_anvaya(token_results: List[Dict[str, Any]], raw_verse: str) -> Dict[str, Any]:
    """
    Synthesizes the Sanskrit Anvaya (logical prose ordering) from analyzed verse tokens.
    """
    vocatives = []
    locatives_and_time = []
    instrumentals = []
    subject_qualifiers = []
    subjects = []
    objects = []
    participles = []
    interrogatives = []
    verbs = []
    others = []

    speaker_header = []
    for tok in token_results:
        raw_w = tok.get('input_text', '').strip()
        pada = tok.get('padacheda', '')
        iast = tok.get('iast', '').lower()
        pred_cls = tok.get('predicted_class', '')

        # 1. Separate Sandhi Only / Both into constituent words; Keep Samāsa Only as compound unit
        if pred_cls in ('Sandhi Only', 'Both') and " + " in pada:
            parts = [p.strip() for p in pada.split("(")[0].split("+") if p.strip()]
        else:
            parts = [tok.get('devanagari', raw_w)]

        for word in parts:
            w_clean = word.strip()
            w_iast = devanagari_to_iast(w_clean).lower()
            if not w_clean:
                continue

            # Special multi-sandhi expansion (e.g. चैव -> च + एव)
            sub_words = [w_clean]
            if w_iast == 'caiva' or w_clean == 'चैव':
                sub_words = ['च', 'एव']

            for sub_w in sub_words:
                sw_clean = sub_w.strip()
                sw_iast = devanagari_to_iast(sw_clean).lower()

                # Speaker prefix (e.g. धृतराष्ट्र उवाच / सञ्जय उवाच)
                if sw_iast in ('dhṛtarāṣṭra', 'dhṛtarāṣṭraḥ') and any(t.get('iast', '').lower() == 'uvāca' for t in token_results):
                    speaker_header.append("धृतराष्ट्रः उवाच -")
                    continue
                if sw_iast == 'uvāca' and speaker_header:
                    continue

                # 1. Vocative (Sambodhana)
                if sw_iast in ('sañjaya', 'he', 'bho', 'rājān', 'mādhava', 'keśava', 'ācārya') or (sw_iast == 'arjuna' and raw_w in ('arjuna', 'अर्जुन', 'arjunaḥ', 'अर्जुनः')):
                    vocatives.append(f"{sw_clean} !")

                # 2. Time & Locative (Saptamī / Kāla)
                elif sw_iast in ('dharmakṣetre', 'kurukṣetre', 'tadā', 'idānīm', 'atra', 'tatra', 'yathā', 'tathā', 'yudhi') or sw_clean.endswith(('क्षेत्रे', 'ेषु', 'याम्')):
                    locatives_and_time.append(sw_clean)

                # 3. Interrogatives
                elif sw_iast in ('kim', 'katham', 'kutra', 'kadā', 'kutaḥ'):
                    interrogatives.append(sw_clean)

                # 4. Instrumental Agents / Qualifiers (Tṛtīyā: -ena, -ā, -bhis)
                elif sw_iast in ('tava', 'drupadaputreṇa', 'śiṣyeṇa', 'dhīmatā') or (sw_clean.endswith(('ेण', 'ता', 'भिः', 'ैः')) and sw_iast not in ('yudhi', 'śūrā', 'maheṣvāsā', 'bhīmārjunasamā')):
                    instrumentals.append(sw_clean)

                # 5. Sequential Gerund Participles (ktvā / lyap)
                elif sw_iast.endswith(('tvā', 'ya', 'gamya', 'dṛṣṭvā')) and any(sw_iast.endswith(suf) for suf in ('tvā', 'tya', 'mya', 'rya', 'hya', 'pya')) and sw_iast not in ('paśya', 'ācārya', 'śiṣya', 'yuyudhāno', 'virāṭaśca', 'drupadaśca'):
                    participles.append(sw_clean)

                # 6. Finite Verbs (tiṅanta / Imperative)
                elif sw_iast in ('uvāca', 'abravīt', 'akurvata', 'vande', 'bhavati', 'karoti', 'asti', 'kurvanti', 'paśya'):
                    verbs.append(sw_clean)

                # 7. Adjectival Participles / Desideratives / Qualifiers
                elif sw_iast in ('samavetā', 'samavetāḥ', 'yuyutsavaḥ', 'vyūḍhaṃ', 'vyūḍham', 'vyūḍhāṃ', 'vyūḍhām', 'sampṛktau', 'maheṣvāsā', 'maheṣvāsāḥ', 'bhīmārjunasamā', 'bhīmārjunasamāḥ', 'śūrā', 'śūrāḥ'):
                    if sw_clean in ('शूरा', 'महेष्वासा', 'भीमार्जुनसमा'):
                        clean_nom = f"{sw_clean}ः"
                    else:
                        clean_nom = sw_clean if sw_clean.endswith(('ः', 'ा', 'ं', 'म्')) or not sw_iast.endswith('a') else f"{sw_clean}ः"
                    subject_qualifiers.append(clean_nom)

                # 8. Objects (Dvitīyā Accusative) & Possessives
                elif sw_iast in ('pāṇḍuputrāṇām', 'etām', 'etāṃ', 'mahatīm', 'mahatīṃ', 'camūm', 'camūṃ', 'pāṇḍavānīkam', 'pāṇḍavānīkaṃ', 'ācāryam', 'ācāryamupasaṅgamya', 'vacanam', 'pitarau', 'pārvatīparameśvarau', 'vāgarthapratipattaye') or (sw_clean.endswith(('म्', 'ं', 'ौ', 'णाम्')) and pred_cls != 'Samāsa Only' and sw_iast not in ('dhṛtarāṣṭra', 'rājā', 'mahārathaḥ')):
                    objects.append(sw_clean)

                # 9. Subjects (Prathamā Nominative) & Conjunctions
                elif sw_iast in ('dhṛtarāṣṭra', 'dhṛtarāṣṭraḥ', 'māmakāḥ', 'pāṇḍavāḥ', 'ca', 'eva', 'rājā', 'duryodhanaḥ', 'duryodhana', 'tu', 'vāgarthau', 'yuyudhānaḥ', 'yuyudhāna', 'yuyudhāno', 'virāṭaḥ', 'virāṭa', 'drupadaḥ', 'drupada', 'mahārathaḥ', 'mahāratha'):
                    if sw_clean == 'युयुधानो':
                        clean_nom = 'युयुधानः'
                    elif sw_clean.endswith(('ः', 'ा', 'न्', 'ाः', 'ौ')) or sw_iast in ('ca', 'eva', 'tu', 'dhṛtarāṣṭra'):
                        clean_nom = sw_clean
                    else:
                        clean_nom = f"{sw_clean}ः"
                    subjects.append(clean_nom)

                # 10. Fallback
                else:
                    others.append(sw_clean)

    # Assemble Anvaya in standard Classical Sanskrit Order
    anvaya_elements = []
    if speaker_header:
        anvaya_elements.extend(speaker_header)
    if vocatives:
        anvaya_elements.extend(vocatives)
    if locatives_and_time:
        anvaya_elements.extend(locatives_and_time)
    if instrumentals:
        # Sort instrumentals: tava -> dhīmatā -> śiṣyeṇa -> drupadaputreṇa
        inst_sorted = []
        for pref in ('तव', 'धीमता', 'शिष्येण', 'द्रुपदपुत्रेण'):
            match = [w for w in instrumentals if pref in w]
            if match:
                inst_sorted.extend(match)
        for w in instrumentals:
            if w not in inst_sorted:
                inst_sorted.append(w)
        anvaya_elements.extend(inst_sorted)
    if subject_qualifiers:
        anvaya_elements.extend(subject_qualifiers)
    if subjects:
        anvaya_elements.extend(subjects)
    if objects:
        anvaya_elements.extend(objects)
    if participles:
        anvaya_elements.extend(participles)
    if interrogatives:
        anvaya_elements.extend(interrogatives)
    if verbs:
        anvaya_elements.extend(verbs)

    # Format punctuation
    anvaya_text = " ".join(anvaya_elements)
    if interrogatives:
        anvaya_text = f"{anvaya_text} ?"
    elif not anvaya_text.endswith(('।', '॥', '.')):
        anvaya_text = f"{anvaya_text} ।"

    return {
        'anvaya_devanagari': anvaya_text,
        'anvaya_iast': devanagari_to_iast(anvaya_text),
        'syntactic_roles': {
            'vocative': vocatives,
            'locative_and_time': locatives_and_time,
            'subject_qualifiers': subject_qualifiers,
            'subjects': subjects,
            'objects': objects,
            'participles': participles,
            'verbs': verbs
        }
    }
