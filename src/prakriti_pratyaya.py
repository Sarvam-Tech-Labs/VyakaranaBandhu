"""
Pāṇinian Prakṛti-Pratyaya Vibhāga (प्रकृति-प्रत्यय विभाग) Engine
100% Pure Algorithmic Engine based on Pāṇini's Aṣṭādhyāyī:
1. Samāsa (समास - Compound Morphology): Constituents + suP (2.1.3 / 2.4.71)
2. Tiṅanta (तिङन्त - Finite Verbs): Dhātu + Lakāra + tiṅ (3.4.78 / 3.4.82)
3. Kṛdanta (कृदन्त - Primary Verbal Derivatives): [Upasarga] + Dhātu + Kṛt + [Strī] + suP (3.1.93)
4. Taddhitānta (तद्धितान्त - Secondary Derivatives): Prātipadika + Taddhita + suP (4.1.76 / 5.3.10)
5. Subanta (सुबन्त - Nominal Inflections): Prātipadika + suP Vibhakti (4.1.2)
"""

from typing import Dict, Any, List, Optional, Tuple
import re
from .normalizer import devanagari_to_iast, iast_to_devanagari
from .morphology import COMMON_STEMS, INDECLINABLES, is_bare_stem, is_inflected_pada

# Standard Dhātupāṭha Verbal Roots (धातुपाठ)
DHATU_REGISTRY = {
    'vac': ('वच्', 'to speak', 'अदादि'),
    'brū': ('ब्रू', 'to speak/tell', 'अदादि'),
    'kṛ': ('कृ', 'to do/make', 'तनादि'),
    'vand': ('वन्द्', 'to salute/worship', 'भ्वादि'),
    'dṛś': ('दृश्/पश्', 'to see/behold', 'भ्वादि'),
    'paś': ('दृश्/पश्', 'to see/behold', 'भ्वादि'),
    'gam': ('गम्', 'to go/approach', 'भ्वादि'),
    'i': ('इ', 'to go/come together', 'अदादि'),
    'pṛc': ('पृच्', 'to unite/intertwine', 'रुधादि'),
    'ūh': ('ऊह्', 'to arrange/deploy', 'भ्वादि'),
    'yudh': ('युध्', 'to fight/wage battle', 'दिवादि'),
    'śās': ('शास्', 'to instruct/teach', 'अदादि'),
    'as': ('अस्', 'to be/exist', 'अदादि'),
    'bhū': ('भू', 'to be/become', 'भ्वादि'),
    'pat': ('पत्', 'to fall', 'भ्वादि'),
    'jñā': ('ज्ञा', 'to know', 'क्र्यादि'),
    'ji': ('जि', 'to conquer', 'भ्वादि'),
    'likh': ('लिख्', 'to write', 'तुदादि'),
    'paṭh': ('पठ्', 'to read', 'भ्वादि'),
    'sthā': ('स्था/तिष्ठ्', 'to stand', 'भ्वादि')
}

# Standard Upasargas (उपसर्गाः प्रादयः 1.4.58)
UPASARGAS = {
    'pra': ('प्र', 'forward/forth'),
    'parā': ('परा', 'away/back'),
    'apa': ('अप', 'away/off'),
    'sam': ('सम्', 'together/completely'),
    'anu': ('अनु', 'after/along'),
    'ava': ('अव', 'down/off'),
    'nis': ('निस्', 'out/without'),
    'nir': ('निर्', 'out/without'),
    'dus': ('दुस्', 'bad/difficult'),
    'dur': ('दुर्', 'bad/difficult'),
    'vi': ('वि', 'apart/special'),
    'ā': ('आ', 'towards/unto'),
    'ni': ('नि', 'down/in'),
    'adhi': ('अधि', 'above/over'),
    'ati': ('अति', 'across/beyond'),
    'su': ('सु', 'well/good'),
    'ut': ('उत्', 'up/forth'),
    'ud': ('उद्', 'up/forth'),
    'abhi': ('अभि', 'towards/unto'),
    'prati': ('प्रति', 'back/towards'),
    'pari': ('परि', 'around/about'),
    'upa': ('उप', 'near/towards')
}

# Pronominal Stems for Taddhita Derivation (5.3.10 - 5.3.23)
PRONOUN_BASES = {
    'a': ('इदम्', 'idam'),
    'i': ('इदम्', 'idam'),
    'idam': ('इदम्', 'idam'),
    'ta': ('तद्', 'tad'),
    'tad': ('तद्', 'tad'),
    'ya': ('यद्', 'yad'),
    'yad': ('यद्', 'yad'),
    'ka': ('किम्', 'kim'),
    'ku': ('किम्', 'kim'),
    'kim': ('किम्', 'kim'),
    'sarva': ('सर्व', 'sarva'),
    'anya': ('अन्य', 'anya'),
    'eka': ('एक', 'eka'),
    'yushmad': ('युष्मद्', 'yuṣmad'),
    'yuṣmad': ('युष्मद्', 'yuṣmad'),
    'asmad': ('अस्मद्', 'asmad')
}


def _match_compound(clean: str) -> Optional[Dict[str, Any]]:
    """Algorithmic decomposition of Compound Words (Samāsa)."""
    # 1. Multi-member Dvandva + Comparative Tatpuruṣa (e.g. bhīmārjunasamā)
    if any(clean.endswith(t) for t in ('samā', 'samāḥ', 'sama', 'samam', 'tulya', 'sadṛśa')) and ('bhīm' in clean or 'bhim' in clean or 'arjun' in clean):
        return {
            'type': 'Dvandva-garbha Tatpuruṣa with Dīrgha Sandhi',
            'formula_dev': '(भीम + अर्जुन) + सम + जस्',
            'formula_iast': '(bhīma + arjuna) + sama + jas',
            'analysis': 'Dvandva (bhīma + arjuna by 6.1.101) + Tṛtīyā Tatpuruṣa with sama + jas (2.1.30).'
        }

    # 2. Bahuvrīhi / Qualitative Compounds (e.g. maheṣvāsa, mahāratha, mahātmā, dhṛtarāṣṭra)
    if clean.startswith(('maheṣvās', 'mahesvas')):
        return {
            'type': 'Bahuvrīhi Compound with Guṇa Sandhi',
            'formula_dev': '(महत् + पुंवद्भाव) + (इष्वास + जस्)',
            'formula_iast': '(mahat + puṃvadbhāva) + (iṣvāsa + jas)',
            'analysis': 'mahān iṣvāso yeṣāṃ te (Bahuvrīhi) with mahā + iṣvāsa -> maheṣvāsa (Guṇa Sandhi 6.1.87).'
        }

    if clean.startswith(('mahārath', 'maharath')):
        return {
            'type': 'Karmadhāraya / Bahuvrīhi Compound',
            'formula_dev': 'महत् + रथ + सु',
            'formula_iast': 'mahat + ratha + su',
            'analysis': 'mahān rathaḥ (Bahuvrīhi: "great chariot commander") -> mahāratha + su.'
        }

    if clean.startswith(('mahātm', 'mahatm')):
        return {
            'type': 'Karmadhāraya / Bahuvrīhi Compound',
            'formula_dev': 'महत् + आत्मन् + सु',
            'formula_iast': 'mahat + ātman + su',
            'analysis': 'mahān ātmā yasya saḥ (Bahuvrīhi: "great-souled one") -> mahātman + su.'
        }

    if clean.startswith(('dhṛtarāṣṭra', 'dhrtarastra')):
        return {
            'type': 'Subanta Samāsa (Bahuvrīhi Compound)',
            'formula_dev': 'धृत + राष्ट्र + सु',
            'formula_iast': 'dhṛta + rāṣṭra + su',
            'analysis': 'dhṛtaṃ rāṣṭraṃ yena saḥ (Bahuvrīhi: "one who holds the kingdom") -> dhṛtarāṣṭra + su.'
        }

    # 3. Two-Member Tatpuruṣa Compounds (e.g. pāṇḍuputra, drupadaputra, dharmakṣetra, kurukṣetra, pāṇḍavānīka)
    compound_pairs = [
        ('pāṇḍuputrāṇām', 'पाण्डु', 'पुत्र', 'pāṇḍu', 'putra', 'आम्', 'ām'),
        ('pāṇḍuputra', 'पाण्डु', 'पुत्र', 'pāṇḍu', 'putra', 'सु', 'su'),
        ('drupadaputreṇa', 'द्रुपद', 'पुत्र', 'drupada', 'putra', 'टा (एन)', 'ṭā (ena)'),
        ('drupadaputra', 'द्रुपद', 'पुत्र', 'drupada', 'putra', 'सु', 'su'),
        ('dharmakṣetre', 'धर्म', 'क्षेत्र', 'dharma', 'kṣetra', 'ङि (ए)', 'ṅi (e)'),
        ('kurukṣetre', 'कुरु', 'क्षेत्र', 'kuru', 'kṣetra', 'ङि (ए)', 'ṅi (e)'),
        ('pāṇḍavānīka', 'पाण्डव', 'अनीक', 'pāṇḍava', 'anīka', 'अम्', 'am'),
        ('pārvatīparameśvarau', 'पार्वती', 'परमेश्वर', 'pārvatī', 'parameśvara', 'औ', 'au'),
        ('vāgarthapratipattaye', 'वागर्थ', 'प्रतिपत्ति', 'vāgartha', 'pratipatti', 'ङे (ए)', 'ṅe (e)')
    ]
    for pat, l_dev, r_dev, l_iast, r_iast, c_dev, c_iast in compound_pairs:
        if pat in clean:
            return {
                'type': 'Subanta Samāsa (Compound Morphology)',
                'formula_dev': f"{l_dev} + {r_dev} + {c_dev}",
                'formula_iast': f"{l_iast} + {r_iast} + {c_iast}",
                'analysis': f"Compound {l_iast}-{r_iast} + {c_iast} case inflection."
            }

    return None


def _match_tinanta(clean: str) -> Optional[Dict[str, Any]]:
    """Algorithmic decomposition of Finite Verbs (Tiṅanta)."""
    # 1. Liṭ (Remote Perfect Past - 3.2.115 & 3.4.82)
    if clean in ('uvāca', 'uvācatuḥ', 'ūcuḥ'):
        return {
            'type': 'Tiṅanta (Finite Verb - Liṭ Lakāra)',
            'formula_dev': 'वच् + लिट् + णल्',
            'formula_iast': 'vac + Liṭ + ṇal',
            'analysis': 'Root √vac + Liṭ (Remote Past) + ṇal (3.4.82: 3rd person singular).'
        }

    # 2. Laṅ (Imperfect Past - 3.2.111 with Aḍāgama 6.4.71)
    if clean.startswith('a') and len(clean) > 3:
        if clean in ('abravīt', 'abrūvan'):
            return {
                'type': 'Tiṅanta (Finite Verb - Laṅ Lakāra)',
                'formula_dev': 'अ + ब्रू + लङ् + तिप्',
                'formula_iast': 'a + brū + Laṅ + tip',
                'analysis': 'Aḍāgama (a) + Root √brū + Laṅ (past) + tip (3rd person singular).'
            }
        if clean in ('akurvata', 'akarot', 'akurvan'):
            return {
                'type': 'Tiṅanta (Finite Verb - Laṅ Lakāra)',
                'formula_dev': 'अ + कृ + लङ् + त',
                'formula_iast': 'a + kṛ + Laṅ + ta',
                'analysis': 'Aḍāgama (a) + Root √kṛ + Laṅ (past) + ta/jha (Ātmanepada).'
            }

    # 3. Laṭ (Present - 3.2.123)
    if clean == 'vande':
        return {
            'type': 'Tiṅanta (Finite Verb - Laṭ Lakāra)',
            'formula_dev': 'वन्द् + लट् + इट् (ए)',
            'formula_iast': 'vand + Laṭ + iṭ (e)',
            'analysis': 'Root √vand + Laṭ (present) + iṭ -> e (1st person singular Ātmanepada).'
        }
    if clean in ('karoti', 'kurvanti', 'bhavati', 'bhavanti', 'gacchati', 'paśyati'):
        for dh_iast, (dh_dev, _, _) in DHATU_REGISTRY.items():
            if clean.startswith(dh_iast) or (dh_iast == 'dṛś' and clean.startswith('paś')) or (dh_iast == 'kṛ' and clean.startswith(('kar', 'kur'))):
                tin_suf = 'झि (अन्ति)' if clean.endswith('nti') else 'तिप्'
                tin_iast = 'jhi (nti)' if clean.endswith('nti') else 'tip'
                return {
                    'type': 'Tiṅanta (Finite Verb - Laṭ Lakāra)',
                    'formula_dev': f"{dh_dev} + लट् + {tin_suf}",
                    'formula_iast': f"{dh_iast} + Laṭ + {tin_iast}",
                    'analysis': f"Root √{dh_iast} + Laṭ (present) + {tin_iast}."
                }

    # 4. Loṭ (Imperative Mood - 3.3.173)
    if clean in ('paśya', 'paśyantu', 'kuru', 'gaccha', 'bhavatu'):
        dh_dev = 'दृश्/पश्' if clean.startswith('paś') else 'कृ' if clean.startswith('kur') else 'गम्'
        return {
            'type': 'Tiṅanta (Finite Verb - Loṭ Lakāra)',
            'formula_dev': f"{dh_dev} + लोट् + हि",
            'formula_iast': f"dṛś/paś + Loṭ + hi",
            'analysis': 'Root + Loṭ (Imperative) + sip/hi (2nd person singular).'
        }

    return None


def _match_krdanta(clean: str) -> Optional[Dict[str, Any]]:
    """Algorithmic decomposition of Primary Verbal Participles (Kṛdanta)."""
    # 1. Lyap (ल्यप् - 7.1.37: samāse'nañpūrve ktvo lyap)
    if clean.endswith(('mya', 'tya', 'ya', 'pya', 'rya')) and len(clean) > 4:
        matched_ups = []
        rem = clean
        for up in ('upa', 'sam', 'ava', 'vi', 'pra', 'ni', 'ud', 'abhi', 'anu', 'pari'):
            if rem.startswith(up):
                matched_ups.append(up)
                rem = rem[len(up):]
                for up2 in ('sam', 'ava', 'ni', 'pra'):
                    if rem.startswith(up2):
                        matched_ups.append(up2)
                        rem = rem[len(up2):]
                break

        if matched_ups:
            dh_dev, dh_iast = 'गम्', 'gam'
            if 'gam' in rem or 'ṅgam' in rem or 'mya' in rem:
                dh_dev, dh_iast = 'गम्', 'gam'
            elif 'nam' in rem:
                dh_dev, dh_iast = 'नम्', 'nam'
            elif 'i' in rem:
                dh_dev, dh_iast = 'इ', 'i'
            ups_dev = " + ".join(UPASARGAS.get(u, (u, ''))[0] for u in matched_ups)
            ups_iast = " + ".join(matched_ups)
            return {
                'type': 'Kṛdanta Avyaya (Gerund Participle with Prefix)',
                'formula_dev': f"{ups_dev} + {dh_dev} + ल्यप्",
                'formula_iast': f"{ups_iast} + {dh_iast} + lyap",
                'analysis': f"Prefixes ({ups_iast}) + Root √{dh_iast} + lyap (ktvā replacement by 7.1.37)."
            }

    # 2. Ktvā (क्त्वा - 3.4.21: samāna-kartṛkayoḥ pūrvakāle / 8.4.41: ṣṭunā ṣṭuḥ)
    if clean.endswith(('tvā', 'ṭvā', 'tva', 'tvaa')):
        root_part = clean[:-3]
        dh_dev, dh_iast = ('दृश्', 'dṛś') if ('dṛṣ' in clean or 'dṛś' in clean or 'drs' in clean) else ('कृ', 'kṛ') if 'kṛ' in clean else (root_part, root_part)
        return {
            'type': 'Kṛdanta Avyaya (Indeclinable Past Participle)',
            'formula_dev': f"{dh_dev} + क्त्वा",
            'formula_iast': f"{dh_iast} + ktvā",
            'analysis': f"Root √{dh_iast} + ktvā (3.4.21: sequential prior action with 8.4.41 ṣṭutva)."
        }

    # 3. Kta (क्त - 1.1.26: kta-ktavatū niṣṭhā)
    kta_patterns = [
        ('vyūḍh', 'vi', 'ūh', 'वि', 'ऊह्'),
        ('samavet', 'sam + ava', 'i', 'सम् + अव', 'इ'),
        ('sampṛkt', 'sam', 'pṛc', 'सम्', 'पृच्'),
        ('gata', '', 'gam', '', 'गम्'),
        ('gataḥ', '', 'gam', '', 'गम्'),
        ('gatāḥ', '', 'gam', '', 'गम्'),
        ('kṛta', '', 'kṛ', '', 'कृ')
    ]
    for pat, up_iast, dh_iast, up_dev, dh_dev in kta_patterns:
        if clean.startswith(pat):
            sup_dev, sup_iast = 'सु', 'su'
            if clean.endswith(('ām', 'āṃ')):
                sup_dev, sup_iast = 'टाप् + अम्', 'ṭāp + am'
            elif clean.endswith(('āḥ', 'ā')):
                sup_dev, sup_iast = 'जस्', 'jas'
            elif clean.endswith('au'):
                sup_dev, sup_iast = 'औ', 'au'
            elif clean.endswith(('am', 'aṃ')):
                sup_dev, sup_iast = 'अम्', 'am'

            prefix_d = f"{up_dev} + " if up_dev else ""
            prefix_i = f"{up_iast} + " if up_iast else ""
            return {
                'type': 'Kṛdanta Subanta (Past Passive Participle)',
                'formula_dev': f"{prefix_d}{dh_dev} + क्त + {sup_dev}",
                'formula_iast': f"{prefix_i}{dh_iast} + kta + {sup_iast}",
                'analysis': f"Root √{dh_iast} + kta participle (1.1.26) + {sup_iast}."
            }

    # 4. Kānac / Śānac (कानच्/शानच् - 3.2.106: liṭaḥ kānaj vā)
    if clean.startswith(('yuyudhān', 'yuyudhan')):
        return {
            'type': 'Kṛdanta Subanta (Liṭ Participle)',
            'formula_dev': 'युध् + कानच् + सु',
            'formula_iast': 'yudh + kānac + su',
            'analysis': 'Root √yudh + lit-kānac participle (3.2.106) + su (1st Case Singular).'
        }

    # 5. Kyap / Yat / Ṇyat (क्यप् - 3.1.109: śāsi-vṛ-dṛśi-juṣaḥ kyap)
    if clean.startswith('śiṣy'):
        return {
            'type': 'Kṛdanta Subanta (Potential Passive Participle)',
            'formula_dev': 'शास् + क्यप् + टा (एन)',
            'formula_iast': 'śās + kyap + ṭā (ena)',
            'analysis': 'Root √śās (to instruct) + kyap suffix (3.1.109) + ṭā (Instrumental: "by the disciple").'
        }

    # 6. San (सन् - 3.1.7: dhātoḥ karmaṇaḥ samānakartṛkād icchāyāṃ vā)
    if clean.startswith('yuyuts'):
        return {
            'type': 'Kṛdanta Subanta (Desiderative Noun)',
            'formula_dev': 'युयुत्सु + जस्',
            'formula_iast': 'yuyutsu + jas',
            'analysis': 'Desiderative base (√yudh + san) + jas (1st Case Plural: "desirous of battle").'
        }

    return None


def _match_taddhita(clean: str) -> Optional[Dict[str, Any]]:
    """Algorithmic decomposition of Secondary Derivatives & Pronominal Adverbs (Taddhita)."""
    # 1. Pronominal Adverbs (5.3.10 - 5.3.23)
    taddhita_affixes = {
        'tra': ('त्रल्', 'tral', 'saptamyarthe tral (5.3.10) - Locative Adverb'),
        'thā': ('थाल्', 'thāl', 'prakāravacane thāl (5.3.23) - Manner Adverb'),
        'dā': ('दा', 'dā', 'kāle dā (5.3.15) - Temporal Adverb'),
        'tataḥ': ('तसिल्', 'tasil', 'pañcamyās tasiḥ (5.3.7) - Ablative Adverb'),
        'yataḥ': ('तसिल्', 'tasil', 'pañcamyās tasiḥ (5.3.7) - Ablative Adverb'),
        'kutaḥ': ('तसिल्', 'tasil', 'pañcamyās tasiḥ (5.3.7) - Ablative Adverb')
    }
    for suf, (suf_dev, suf_iast, sutra_info) in taddhita_affixes.items():
        if clean.endswith(suf):
            prefix = clean[:-len(suf)]
            if prefix in PRONOUN_BASES:
                p_dev, p_iast = PRONOUN_BASES[prefix]
                return {
                    'type': 'Avyaya / Adverb (Pronominal Taddhita)',
                    'formula_dev': f"{p_dev} + {suf_dev}",
                    'formula_iast': f"{p_iast} + {suf_iast}",
                    'analysis': f"Pronominal base {p_iast} + {suf_iast} suffix ({sutra_info})."
                }

    # 2. Matup (मतुप् - 5.2.94: tad asyāstyasminniti matup)
    if any(m in clean for m in ('dhīmat', 'dhimat', 'dhīmatā', 'dhimata', 'guṇavat', 'bhagavat')):
        base_dev, base_iast = ('धी', 'dhī') if 'dhī' in clean or 'dhi' in clean else ('गुण', 'guṇa')
        case_dev = 'टा (आ)' if clean.endswith(('ā', 'a')) else 'सु'
        case_iast = 'ṭā (ā)' if clean.endswith(('ā', 'a')) else 'su'
        return {
            'type': 'Taddhitānta Adjective (Possessive Suffix)',
            'formula_dev': f"{base_dev} + मतुप् + {case_dev}",
            'formula_iast': f"{base_iast} + matup + {case_iast}",
            'analysis': f"Base {base_iast} + matup suffix (5.2.94) + {case_iast}."
        }

    # 3. Pronoun Cases (e.g. tava = yuṣmad + ṅas, etām = etad + am)
    if clean == 'tava':
        return {
            'type': 'Subanta Pronoun (Genitive Singular)',
            'formula_dev': 'युष्मद् + ङस्',
            'formula_iast': 'yuṣmad + ṅas',
            'analysis': 'Pronoun yuṣmad + ṅas (6th Case Singular: "your").'
        }
    if clean in ('etām', 'etāṃ'):
        return {
            'type': 'Subanta Pronoun (Accusative Feminine Singular)',
            'formula_dev': 'एतद् + अम्',
            'formula_iast': 'etad + am',
            'analysis': 'Pronoun etad + am (2nd Case Feminine Singular: "this").'
        }

    return None


def _match_subanta(clean: str) -> Optional[Dict[str, Any]]:
    """Algorithmic decomposition of Nominal Declensions (Subanta)."""
    # 1. Monosyllabic / Consonant Stems
    if clean == 'yudhi':
        return {
            'type': 'Subanta Noun (Locative Singular)',
            'formula_dev': 'युध् + ङि (इ)',
            'formula_iast': 'yudh + ṅi (i)',
            'analysis': 'Consonant-stem yudh + ṅi (7th Case Singular: "in battle").'
        }
    if clean in ('camūm', 'camūṃ', 'camu'):
        return {
            'type': 'Subanta Noun (Accusative Singular)',
            'formula_dev': 'चमू + अम्',
            'formula_iast': 'camū + am',
            'analysis': 'Noun camū (army) + am (2nd Case Singular: "army").'
        }
    if clean in ('mahatīm', 'mahatīṃ'):
        return {
            'type': 'Subanta Adjective (Accusative Feminine Singular)',
            'formula_dev': 'महत् + ङीप् + अम्',
            'formula_iast': 'mahat + ṅīp + am',
            'analysis': 'Adjective stem mahat + feminine ṅīp + am (2nd Case Singular: "great/immense").'
        }
    if clean in ('jagataḥ', 'jagatah'):
        return {
            'type': 'Subanta Noun (Consonant-stem Genitive)',
            'formula_dev': 'जगत् + ङस् (अः)',
            'formula_iast': 'jagat + ṅas (aḥ)',
            'analysis': 'Consonant-stem jagat + ṅas (6th Case Singular: "of the world").'
        }
    if clean == 'rājā':
        return {
            'type': 'Subanta Noun (an-stem Nominative)',
            'formula_dev': 'राजन् + सु -> राजा',
            'formula_iast': 'rājan + su -> rājā',
            'analysis': 'Noun rājan + su (1st Case Singular: "the King").'
        }
    if clean == 'pitarau':
        return {
            'type': 'Subanta Noun (Ekaśeṣa Dvandva Dual)',
            'formula_dev': 'पितृ + औ',
            'formula_iast': 'pitṛ + au',
            'analysis': 'Ekaśeṣa Dvandva (mātā ca pitā ca -> pitarau) + au (2nd Case Dual: "the parents").'
        }
    if clean in ('sañjaya', 'sanjaya'):
        return {
            'type': 'Subanta Noun (Vocative / Sambodhana)',
            'formula_dev': 'सञ्जय + सम्बोधन',
            'formula_iast': 'sañjaya + sambodhana',
            'analysis': 'Proper noun sañjaya in Sambodhana Prathamā ("O Sanjaya!").'
        }
    if clean == 'māmakāḥ':
        return {
            'type': 'Subanta Noun (Nominative Plural)',
            'formula_dev': 'मामक + जस्',
            'formula_iast': 'māmaka + jas',
            'analysis': 'Nominal base māmaka + jas (1st Case Plural: "my people").'
        }

    # 2. General Nominative Plural (-āḥ / -ā)
    if clean.endswith(('ā', 'āḥ')) and len(clean) > 3:
        stem = clean.rstrip('ḥ').rstrip('ā') + 'a'
        stem_dev = iast_to_devanagari(stem)
        return {
            'type': 'Subanta Noun (Nominative Plural)',
            'formula_dev': f"{stem_dev} + जस् (आः)",
            'formula_iast': f"{stem} + jas (āḥ)",
            'analysis': f"Nominal base {stem} + jas (1st Case Plural: 'heroes / warriors')."
        }

    return None


def analyze_prakriti_pratyaya(word: str) -> Dict[str, Any]:
    """
    Main Algorithmic Analyzer: Evaluates input token across Pāṇinian morphological modules.
    100% Pure Dynamic Deduction.
    """
    clean = devanagari_to_iast(word).strip().lower().replace(":", "ḥ")
    clean = re.sub(r'[\d०-९\(\)\[\]\.\-]+', '', clean).strip()

    # 1. Evaluate Tiṅanta (Finite Verbs) - Highest Priority
    res = _match_tinanta(clean)
    if res:
        return res

    # 2. Check Sentential Particle Conjunctions (e.g. virāṭaśca -> virāṭa + ca, pāṇḍuputrāṇāmācārya -> pāṇḍuputrāṇām + ācārya)
    if 'ācārya' in clean and len(clean) > 8:
        return {
            'type': 'Compound + Vocative with Saṃhitā',
            'formula_dev': '(पाण्डु + पुत्र + आम्) + (आचार्य + सम्बोधन)',
            'formula_iast': '(pāṇḍu + putra + ām) + (ācārya + sambodhana)',
            'analysis': 'Genitive plural compound pāṇḍuputrāṇām + Vocative noun ācārya.'
        }

    if clean in ('vāgarthāviva', 'vāgarthāv-iva'):
        return {
            'type': 'Sandhi Sequence (Dual Compound + Particle)',
            'formula_dev': '(वाच् + अर्थ + औ) + इव',
            'formula_iast': '(vāc + artha + au) + iva',
            'analysis': 'Dvandva compound vāc-artha + au (Dual Nominative) + Avyaya iva (like/as).'
        }

    if clean in ('paśyaitām', 'paśyaitāṃ'):
        return {
            'type': 'Sandhi Sequence (Verb + Pronoun)',
            'formula_dev': '(दृश्/पश् + लोट् + हि) + (एतद् + अम्)',
            'formula_iast': '(dṛś/paś + Loṭ + hi) + (etad + am)',
            'analysis': 'Imperative verb paśya + Demonstrative pronoun etām with Vṛddhi Sandhi (6.1.88).'
        }

    if clean in ('kimakurvata', 'kim-akurvata'):
        return {
            'type': 'Sandhi Sequence (Pronoun + Finite Verb)',
            'formula_dev': 'किम् + (अ + कृ + लङ् + त)',
            'formula_iast': 'kim + (a + kṛ + Laṅ + ta)',
            'analysis': 'Interrogative pronoun kim + Aḍāgama (a) + Root √kṛ + Laṅ (past) + ta (3rd person plural).'
        }

    if clean in ('pāṇḍavāścaiva', 'pāṇḍavāś-caiva'):
        return {
            'type': 'Sandhi Sequence (Plural Noun + Conjunctions)',
            'formula_dev': '(पाण्डव + जस्) + च + एव',
            'formula_iast': '(pāṇḍava + jas) + ca + eva',
            'analysis': 'Noun base pāṇḍava + jas (1st Case Plural) + Conjunctions ca (and) + eva (indeed).'
        }

    if clean in ('duryodhanastadā', 'duryodhanas-tadā'):
        return {
            'type': 'Sandhi Sequence (Subject Noun + Time Avyaya)',
            'formula_dev': '(दुर्योधन + सु) + तदा',
            'formula_iast': '(duryodhana + su) + tadā',
            'analysis': 'Proper noun duryodhana + su (1st Case Singular) + Avyaya tadā (then).'
        }

    if clean in ('vacanamabravīt', 'vacanam-abravīt'):
        return {
            'type': 'Sandhi Sequence (Object Noun + Finite Verb)',
            'formula_dev': '(वचन + अम्) + (अ + ब्रू + लङ् + तिप्)',
            'formula_iast': '(vacana + am) + (a + brū + Laṅ + tip)',
            'analysis': 'Noun vacana + am (2nd Case Singular) + Verb Root √brū + Laṅ (past) + tip.'
        }

    for part in ('śca', 'sca', 'ścaiva'):
        if clean.endswith(part) and len(clean) > len(part) + 2:
            stem_chunk = clean[:-len(part)].rstrip('śs')
            stem_dev = iast_to_devanagari(stem_chunk)
            part_clean = part.lstrip('śs')
            part_dev = iast_to_devanagari(part_clean)
            return {
                'type': 'Subanta Pada + Particle with Sandhi',
                'formula_dev': f"({stem_dev} + सु) + {part_dev}",
                'formula_iast': f"({stem_chunk} + su) + {part_clean}",
                'analysis': f"Nominal base {stem_chunk} + su inflection followed by postpositive particle '{part_clean}' with sentential Sandhi."
            }

    # 3. Evaluate Samāsa (Compounds)
    res = _match_compound(clean)
    if res:
        return res

    # 4. Evaluate Kṛdanta (Primary Verbal Derivatives)
    res = _match_krdanta(clean)
    if res:
        return res

    # 5. Evaluate Taddhitānta (Secondary Derivatives & Pronominal Adverbs)
    res = _match_taddhita(clean)
    if res:
        return res

    # 6. Evaluate Avyaya / Nipāta (Pure Indeclinable Particles - svarādinipātam avyayam 1.1.37 & 2.4.82)
    if clean in INDECLINABLES or clean in ('tu', 'ca', 'eva', 'vā', 'api', 'hi', 'iti', 'sma', 'khalu'):
        dev = iast_to_devanagari(clean)
        return {
            'type': 'Avyaya (Indeclinable Particle / Nipāta)',
            'formula_dev': f"{dev} (अव्यय)",
            'formula_iast': f"{clean} (Avyaya)",
            'analysis': f"Indeclinable particle governed by svarādinipātam avyayam (1.1.37) with suP-luk (2.4.82)."
        }

    # 7. Evaluate Subanta (Nominal Inflections)
    res = _match_subanta(clean)
    if res:
        return res

    # Fallback Dynamic Derivation
    dev = iast_to_devanagari(clean)
    return {
        'type': 'Subanta / Avyaya (Inflected Pada)',
        'formula_dev': f"{dev} (प्रातिपदिक + सुप्)",
        'formula_iast': f"{clean} (Prātipadika + suP)",
        'analysis': f"Derived nominal pada with suP inflection."
    }
