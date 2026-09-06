"""
Exhaustive, Deterministic Verse Test Cases & Expected Ground Truths
Contains complete Shloka definitions, token counts, class distribution summaries,
canonical Syntactic Prose Ordering (Anvaya), and word-by-word morphological/Prakṛti-Pratyaya ground truths.
"""

VERSE_CASES = [
    {
        "name": "Bhagavad Gītā (1.1)",
        "verse": "धृतराष्ट्र उवाच धर्मक्षेत्रे कुरुक्षेत्रे समवेता युयुत्सव: । मामका: पाण्डवाश्चैव किमकुर्वत सञ्जय ॥ १ ॥",
        "expected_token_count": 10,
        "expected_class_summary": {
            "Samāsa Only": 3,
            "Sandhi Only": 2,
            "Both": 0,
            "None": 5
        },
        "expected_anvaya": "धृतराष्ट्रः उवाच - सञ्जय ! धर्मक्षेत्रे कुरुक्षेत्रे समवेता युयुत्सवः मामकाः पाण्डवाः च एव किम् अकुर्वत ?",
        "expected_tokens": {
            "धृतराष्ट्र": {
                "class": "Samāsa Only",
                "padacheda": "धृत + राष्ट्र",
                "prakriti_pratyaya": "धृत + राष्ट्र + सु"
            },
            "उवाच": {
                "class": "None",
                "padacheda": "उवाच",
                "prakriti_pratyaya": "वच् + लिट् + णल्"
            },
            "धर्मक्षेत्रे": {
                "class": "Samāsa Only",
                "padacheda": "धर्मस्य + क्षेत्रे",
                "prakriti_pratyaya": "धर्म + क्षेत्र + ङि (ए)"
            },
            "कुरुक्षेत्रे": {
                "class": "Samāsa Only",
                "padacheda": "कुरोः + क्षेत्रे",
                "prakriti_pratyaya": "कुरु + क्षेत्र + ङि (ए)"
            },
            "समवेता": {
                "class": "None",
                "padacheda": "समवेता",
                "prakriti_pratyaya": "सम् + अव + इ + क्त + जस्"
            },
            "युयुत्सवः": {
                "class": "None",
                "padacheda": "युयुत्सवः",
                "prakriti_pratyaya": "युयुत्सु + जस्"
            },
            "मामकाः": {
                "class": "None",
                "padacheda": "मामकाः",
                "prakriti_pratyaya": "मामक + जस्"
            },
            "पाण्डवाश्चैव": {
                "class": "Sandhi Only",
                "padacheda": "पाण्डवाः + चैव",
                "prakriti_pratyaya": "(पाण्डव + जस्) + च + एव"
            },
            "किमकुर्वत": {
                "class": "Sandhi Only",
                "padacheda": "किम् + अकुर्वत",
                "prakriti_pratyaya": "किम् + (अ + कृ + लङ् + त)"
            },
            "सञ्जय": {
                "class": "None",
                "padacheda": "सञ्जय",
                "prakriti_pratyaya": "सञ्जय + सम्बोधन"
            }
        }
    },
    {
        "name": "Bhagavad Gītā (1.2)",
        "verse": "सञ्जय उवाच दृष्ट्वा तु पाण्डवानीकं व्यूढं दुर्योधनस्तदा । आचार्यमुपसङ्गम्य राजा वचनमब्रवीत् ॥ २ ॥",
        "expected_token_count": 10,
        "expected_class_summary": {
            "Samāsa Only": 0,
            "Sandhi Only": 3,
            "Both": 1,
            "None": 6
        },
        "expected_tokens": {
            "सञ्जय": {
                "class": "None",
                "padacheda": "सञ्जय",
                "prakriti_pratyaya": "सञ्जय + सम्बोधन"
            },
            "उवाच": {
                "class": "None",
                "padacheda": "उवाच",
                "prakriti_pratyaya": "वच् + लिट् + णल्"
            },
            "दृष्ट्वा": {
                "class": "None",
                "padacheda": "दृष्ट्वा",
                "prakriti_pratyaya": "दृश् + क्त्वा"
            },
            "तु": {
                "class": "None",
                "padacheda": "तु",
                "prakriti_pratyaya": "तु (अव्यय)"
            },
            "पाण्डवानीकं": {
                "class": "Both",
                "padacheda": "पाण्डवस्य + अनीकं",
                "prakriti_pratyaya": "पाण्डव + अनीक + अम्"
            },
            "व्यूढं": {
                "class": "None",
                "padacheda": "व्यूढं",
                "prakriti_pratyaya": "वि + ऊह् + क्त + अम्"
            },
            "दुर्योधनस्तदा": {
                "class": "Sandhi Only",
                "padacheda": "दुर्योधनः + तदा",
                "prakriti_pratyaya": "(दुर्योधन + सु) + तदा"
            },
            "आचार्यमुपसङ्गम्य": {
                "class": "Sandhi Only",
                "padacheda": "आचार्यम् + उपसङ्गम्य"
            },
            "राजा": {
                "class": "None",
                "padacheda": "राजा",
                "prakriti_pratyaya": "राजन् + सु -> राजा"
            },
            "वचनमब्रवीत्": {
                "class": "Sandhi Only",
                "padacheda": "वचनम् + अब्रवीत्",
                "prakriti_pratyaya": "(वचन + अम्) + (अ + ब्रू + लङ् + तिप्)"
            }
        }
    },
    {
        "name": "Kālidāsa’s Raghuvaṃśa (1.1)",
        "verse": "वागर्थाविव सम्पृक्तौ वागर्थप्रतिपत्तये । जगतः पितरौ वन्दे पार्वतीपरमेश्वरौ ॥",
        "expected_token_count": 7,
        "expected_class_summary": {
            "Samāsa Only": 2,
            "Sandhi Only": 1,
            "Both": 0,
            "None": 4
        },
        "expected_tokens": {
            "वागर्थाविव": {
                "class": "Sandhi Only",
                "padacheda": "वागर्थौ + इव",
                "prakriti_pratyaya": "(वाच् + अर्थ + औ) + इव"
            },
            "सम्पृक्तौ": {
                "class": "None",
                "padacheda": "सम्पृक्तौ",
                "prakriti_pratyaya": "सम् + पृच् + क्त + औ"
            },
            "वागर्थप्रतिपत्तये": {
                "class": "Samāsa Only",
                "padacheda": "वागर्थस्य + प्रतिपत्तये"
            },
            "जगतः": {
                "class": "None",
                "padacheda": "जगतः",
                "prakriti_pratyaya": "जगत् + ङस् (अः)"
            },
            "पितरौ": {
                "class": "None",
                "padacheda": "पितरौ",
                "prakriti_pratyaya": "पितृ + औ"
            },
            "वन्दे": {
                "class": "None",
                "padacheda": "वन्दे",
                "prakriti_pratyaya": "वन्द् + लट् + इट् (ए)"
            },
            "पार्वतीपरमेश्वरौ": {
                "class": "Samāsa Only",
                "padacheda": "पार्वती + परमेश्वरौ",
                "prakriti_pratyaya": "पार्वती + परमेश्वर + औ"
            }
        }
    },
    {
        "name": "Bhagavad Gītā (1.3)",
        "verse": "पश्यैतां पाण्डुपुत्राणामाचार्य महतीं चमूम् । व्यूढां द्रुपदपुत्रेण तव शिष्येण धीमता ॥ ३ ॥",
        "expected_token_count": 9,
        "expected_class_summary": {
            "Samāsa Only": 1,
            "Sandhi Only": 1,
            "Both": 1,
            "None": 6
        },
        "expected_anvaya": "आचार्य ! तव धीमता शिष्येण द्रुपदपुत्रेण व्यूढां एतां पाण्डुपुत्राणाम् महतीं चमूम् पश्य ।",
        "expected_tokens": {
            "पश्यैतां": {
                "class": "Sandhi Only",
                "padacheda": "पश्य + एता",
                "prakriti_pratyaya": "(दृश्/पश् + लोट् + हि) + (एतद् + अम्)"
            },
            "पाण्डुपुत्राणामाचार्य": {
                "class": "Both",
                "padacheda": "पाण्डुपुत्राणाम् + आचार्य",
                "prakriti_pratyaya": "(पाण्डु + पुत्र + आम्) + (आचार्य + सम्बोधन)"
            },
            "महतीं": {
                "class": "None",
                "padacheda": "महतीं",
                "prakriti_pratyaya": "महत् + ङीप् + अम्"
            },
            "चमूम्": {
                "class": "None",
                "padacheda": "चमूम्",
                "prakriti_pratyaya": "चमू + अम्"
            },
            "व्यूढां": {
                "class": "None",
                "padacheda": "व्यूढां",
                "prakriti_pratyaya": "वि + ऊह् + क्त + टाप् + अम्"
            },
            "द्रुपदपुत्रेण": {
                "class": "Samāsa Only",
                "padacheda": "द्रुपदस्य + पुत्रेण",
                "prakriti_pratyaya": "द्रुपद + पुत्र + टा (एन)"
            },
            "तव": {
                "class": "None",
                "padacheda": "तव",
                "prakriti_pratyaya": "युष्मद् + ङस्"
            },
            "शिष्येण": {
                "class": "None",
                "padacheda": "शिष्येण",
                "prakriti_pratyaya": "शास् + क्यप् + टा (एन)"
            },
            "धीमता": {
                "class": "None",
                "padacheda": "धीमता",
                "prakriti_pratyaya": "धी + मतुप् + टा (आ)"
            }
        }
    },
    {
        "name": "Bhagavad Gītā (1.4)",
        "verse": "अत्र शूरा महेष्वासा भीमार्जुनसमा युधि । युयुधानो विराटश्च द्रुपदश्च महारथः ॥ ४ ॥",
        "expected_token_count": 9,
        "expected_class_summary": {
            "Samāsa Only": 1,
            "Sandhi Only": 2,
            "Both": 2,
            "None": 4
        },
        "expected_anvaya": "अत्र युधि शूराः युयुधानः विराटः च द्रुपदः च महारथः ।",
        "expected_tokens": {
            "अत्र": {
                "class": "None",
                "padacheda": "अत्र",
                "prakriti_pratyaya": "इदम् + त्रल्"
            },
            "शूरा": {
                "class": "None",
                "padacheda": "शूराः",
                "prakriti_pratyaya": "शूर + जस् (आः)"
            },
            "महेष्वासा": {
                "class": "Both",
                "padacheda": "महा + इष्वासाः",
                "prakriti_pratyaya": "(महत् + पुंवद्भाव) + (इष्वास + जस्)"
            },
            "भीमार्जुनसमा": {
                "class": "Both",
                "padacheda": "भीम + अर्जुन + समाः",
                "prakriti_pratyaya": "(भीम + अर्जुन) + सम + जस्"
            },
            "युधि": {
                "class": "None",
                "padacheda": "युधि",
                "prakriti_pratyaya": "युध् + ङि (इ)"
            },
            "युयुधानो": {
                "class": "None",
                "padacheda": "युयुधानः",
                "prakriti_pratyaya": "युध् + कानच् + सु"
            },
            "विराटश्च": {
                "class": "Sandhi Only",
                "padacheda": "विराटः + च",
                "prakriti_pratyaya": "(विराट + सु) + च"
            },
            "द्रुपदश्च": {
                "class": "Sandhi Only",
                "padacheda": "द्रुपदः + च",
                "prakriti_pratyaya": "(द्रुपद + सु) + च"
            },
            "महारथः": {
                "class": "Samāsa Only",
                "padacheda": "महा + रथः",
                "prakriti_pratyaya": "महत् + रथ + सु"
            }
        }
    }
]
