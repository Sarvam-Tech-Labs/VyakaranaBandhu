# -*- coding: utf-8 -*-
"""
Tests for 1.3.14 to 1.3.93 — which set of endings a verb takes.

The bulk of this file is one table. For each sūtra it holds the use the Kāśikā
works out, the pada it says results, and where it gives one, the
counter-example that fails the sūtra's own condition. Those pairs are the
whole point: a rule that fires for its example proves nothing on its own, since
a rule that fired for everything would pass too. A rule that fires for the
example *and not* for the counter-example is being tested.

The other tests are checks on derivations — places where the codification reads
something out of the dhātupāṭha rather than listing it, and can therefore be
wrong in a way a hand-written list could not be:

  1.3.15   its roots are named by sense, and the sense is in the file
  1.3.72   its two marks are in the file, and only in the right position
  1.3.91   its gaṇa is a run in the file, and the Kāśikā fixes both ends
  1.3.62   its atideśa is performed, so the Kāśikā's four counter-examples
           have to fall out rather than be excluded by hand
"""

from __future__ import annotations

import unittest

import src.astadhyayi.rules  # noqa: F401  — populates the registry
from src.astadhyayi.atmanepada import (
    PROVISIONS,
    Pada,
    VerbContext,
    dyutadi,
    near_misses,
    pada_of_usage,
    provisions_for,
    resolve,
    root_senses,
    vrtadi,
)
from src.astadhyayi.pada import entries_for, is_nyit, is_svaritet
from src.astadhyayi.sources import facts
from src.astadhyayi.sutra import REGISTRY

A, P = Pada.ATMANEPADA, Pada.PARASMAIPADA


#: (sūtra, form the Kāśikā works, the use, expected pada, expected sūtra-or-None)
#:
#: `None` for the last field means "do not care which sūtra, only which pada" —
#: used for counter-examples, where the point is that *this* sūtra did not fire.
WORKED = [
    # 1.3.14 – 1.3.16, the reciprocal
    ("1.3.14", "vyatilunate", dict(root="lū", given=["karmavyatihāra"]), A, "1.3.14"),
    ("1.3.14", "vyatipunate", dict(root="pū", given=["karmavyatihāra"]), A, "1.3.14"),
    ("1.3.14", "lunanti", dict(root="lū"), P, "1.3.78"),
    ("1.3.15", "vyatigacchanti", dict(root="gam", given=["karmavyatihāra"]), P, None),
    ("1.3.15", "vyatisarpanti", dict(root="sṛp", given=["karmavyatihāra"]), P, None),
    ("1.3.15", "vyatighnanti", dict(root="han", given=["karmavyatihāra"]), P, None),
    ("1.3.15", "vyatihasanti", dict(root="has", given=["karmavyatihāra"]), P, None),
    ("1.3.15", "vyatijalpanti", dict(root="jalp", given=["karmavyatihāra"]), P, None),
    ("1.3.16", "itaretarasya vyatilunanti",
     dict(root="lū", given=["karmavyatihāra"], upapada="itaretara"), P, None),
    ("1.3.16", "parasparasya vyatilunanti",
     dict(root="lū", given=["karmavyatihāra"], upapada="paraspara"), P, None),

    # 1.3.17 – 1.3.31, root and upasarga
    ("1.3.17", "niviśate", dict(root="viś", upasargas=["ni"]), A, "1.3.17"),
    ("1.3.17", "praviśati", dict(root="viś", upasargas=["pra"]), P, "1.3.78"),
    ("1.3.18", "vikrīṇīte", dict(root="krī", upasargas=["vi"]), A, "1.3.18"),
    ("1.3.19", "parājayate", dict(root="ji", upasargas=["parā"]), A, "1.3.19"),
    ("1.3.20", "vidyām ādatte", dict(root="dā", upasargas=["ā"]), A, "1.3.20"),
    ("1.3.20", "āsyaṃ vyādadāti",
     dict(root="dā", upasargas=["ā"], sense="āsyavihāraṇa"), P, "1.3.78"),
    ("1.3.21", "saṃkrīḍate", dict(root="krīḍ", upasargas=["sam"]), A, "1.3.21"),
    ("1.3.21", "ākrīḍate", dict(root="krīḍ", upasargas=["ā"]), A, "1.3.21"),
    ("1.3.22", "pratiṣṭhate", dict(root="sthā", upasargas=["pra"]), A, "1.3.22"),
    ("1.3.23", "tiṣṭhate kanyā", dict(root="sthā", sense="prakāśana"), A, "1.3.23"),
    ("1.3.23", "tvayi tiṣṭhate", dict(root="sthā", sense="stheyākhyā"), A, "1.3.23"),
    ("1.3.24", "gehe uttiṣṭhate", dict(root="sthā", upasargas=["ud"]), A, "1.3.24"),
    ("1.3.24", "āsanād uttiṣṭhati",
     dict(root="sthā", upasargas=["ud"], sense="ūrdhvakarman"), P, "1.3.78"),
    ("1.3.25", "gārhapatyam upatiṣṭhate",
     dict(root="sthā", upasargas=["upa"], sense="mantrakaraṇa"), A, "1.3.25"),
    ("1.3.25", "bhartāram upatiṣṭhati", dict(root="sthā", upasargas=["upa"]), P, "1.3.78"),
    ("1.3.26", "yāvadbhuktam upatiṣṭhate",
     dict(root="sthā", upasargas=["upa"], given=["akarmaka"]), A, "1.3.26"),
    ("1.3.26", "rājānam upatiṣṭhati",
     dict(root="sthā", upasargas=["upa"], given=["sakarmaka"]), P, "1.3.78"),
    ("1.3.27", "uttapate", dict(root="tap", artha="santApe", upasargas=["ud"], given=["akarmaka"]), A, "1.3.27"),
    ("1.3.27", "uttapati suvarṇam",
     dict(root="tap", artha="santApe", upasargas=["ud"], given=["sakarmaka"]), P, "1.3.78"),
    ("1.3.28", "āyacchate", dict(root="yam", upasargas=["ā"], given=["akarmaka"]), A, "1.3.28"),
    ("1.3.28", "āhate", dict(root="han", upasargas=["ā"], given=["akarmaka"]), A, "1.3.28"),
    ("1.3.28", "āyacchati rajjum",
     dict(root="yam", upasargas=["ā"], given=["sakarmaka"]), P, "1.3.78"),
    ("1.3.29", "saṃgacchate", dict(root="gam", upasargas=["sam"], given=["akarmaka"]), A, "1.3.29"),
    ("1.3.29", "saṃśṛṇute", dict(root="śru", upasargas=["sam"], given=["akarmaka"]), A, "1.3.29"),
    ("1.3.29", "saṃvitte", dict(root="vid", upasargas=["sam"], given=["akarmaka"]), A, "1.3.29"),
    ("1.3.29", "saṃpaśyate", dict(root="dṛś", upasargas=["sam"], given=["akarmaka"]), A, "1.3.29"),
    ("1.3.29", "grāmaṃ saṃpaśyati",
     dict(root="dṛś", upasargas=["sam"], given=["sakarmaka"]), P, "1.3.78"),
    ("1.3.30", "nihvayate", dict(root="hve", upasargas=["ni"]), A, "1.3.30"),
    ("1.3.31", "mallam āhvayate",
     dict(root="hve", upasargas=["ā"], sense="spardhā"), A, "1.3.31"),
    ("1.3.31", "gām āhvayati gopālaḥ", dict(root="hve", upasargas=["ā"]), P, "1.3.78"),

    # 1.3.32 – 1.3.37, कृ and नी
    ("1.3.32", "gaṇakān upakurute", dict(root="kṛ", upasargas=["upa"], sense="sevana"), A, "1.3.32"),
    ("1.3.32", "śataṃ prakurute", dict(root="kṛ", upasargas=["pra"], sense="upayoga"), A, "1.3.32"),
    ("1.3.32", "kaṭaṃ karoti", dict(root="kṛ"), P, "1.3.78"),
    ("1.3.33", "tam adhicakre",
     dict(root="kṛ", upasargas=["adhi"], sense="prasahana"), A, "1.3.33"),
    ("1.3.33", "artham adhikaroti", dict(root="kṛ", upasargas=["adhi"]), P, "1.3.78"),
    ("1.3.34", "vikurute svarān",
     dict(root="kṛ", upasargas=["vi"], given=["śabdakarman"]), A, "1.3.34"),
    ("1.3.35", "vikurvate saindhavāḥ",
     dict(root="kṛ", upasargas=["vi"], given=["akarmaka"]), A, "1.3.35"),
    ("1.3.35", "kaṭaṃ vikaroti",
     dict(root="kṛ", upasargas=["vi"], given=["sakarmaka"]), P, "1.3.78"),
    ("1.3.36", "māṇavakam upanayate",
     dict(root="nī", upasargas=["upa"], sense="utsañjana"), A, "1.3.36"),
    ("1.3.36", "ajāṃ nayati grāmam", dict(root="nī"), P, "1.3.78"),
    ("1.3.37", "krodhaṃ vinayate",
     dict(root="nī", upasargas=["vi"], given=["kartṛstha-aśarīra-karman"]), A, "1.3.37"),
    ("1.3.37", "gaḍuṃ vinayati", dict(root="nī", upasargas=["vi"]), P, "1.3.78"),

    # 1.3.38 – 1.3.43, क्रम्
    ("1.3.38", "kramate buddhiḥ", dict(root="kram", sense="vṛtti"), A, "1.3.38"),
    ("1.3.38", "apakrāmati", dict(root="kram", upasargas=["apa"]), P, "1.3.78"),
    ("1.3.39", "upakramate", dict(root="kram", upasargas=["upa"], sense="sarga"), A, "1.3.39"),
    ("1.3.39", "saṃkrāmati", dict(root="kram", upasargas=["sam"], sense="sarga"), P, "1.3.78"),
    ("1.3.39", "upakrāmati", dict(root="kram", upasargas=["upa"]), P, "1.3.78"),
    ("1.3.40", "ākramate ādityaḥ",
     dict(root="kram", upasargas=["ā"], sense="udgamana"), A, "1.3.40"),
    ("1.3.41", "suṣṭhu vikramate",
     dict(root="kram", upasargas=["vi"], sense="pādaviharaṇa"), A, "1.3.41"),
    ("1.3.42", "prakramate bhoktum",
     dict(root="kram", upasargas=["pra"], given=["samartha"]), A, "1.3.42"),
    ("1.3.42", "pūrvedyuḥ prakrāmati", dict(root="kram", upasargas=["pra"]), P, "1.3.78"),

    # 1.3.44 – 1.3.50, ज्ञा and वद्
    ("1.3.44", "śatam apajānīte",
     dict(root="jñā", upasargas=["apa"], sense="apahnava"), A, "1.3.44"),
    ("1.3.44", "na tvaṃ jānāsi", dict(root="jñā", sense="apahnava"), P, "1.3.78"),
    ("1.3.45", "sarpiṣo jānīte", dict(root="jñā", given=["akarmaka"]), A, "1.3.45"),
    ("1.3.45", "svareṇa putraṃ jānāti", dict(root="jñā", given=["sakarmaka"]), P, "1.3.78"),
    ("1.3.46", "śataṃ saṃjānīte", dict(root="jñā", upasargas=["sam"]), A, "1.3.46"),
    ("1.3.46", "mātuḥ saṃjānāti",
     dict(root="jñā", upasargas=["sam"], sense="ādhyāna"), P, "1.3.78"),
    ("1.3.47", "kṣetre vadate", dict(root="vad", artha="vyaktAyAM vAci", sense="yatna"), A, "1.3.47"),
    ("1.3.47", "yat kiṃcid vadati", dict(root="vad", artha="vyaktAyAM vAci"), P, "1.3.78"),
    ("1.3.48", "saṃpravadante brāhmaṇāḥ",
     dict(root="vad", artha="vyaktAyAM vAci", upasargas=["sam"], sense="samuccāraṇa", given=["vyaktavāc"]),
     A, "1.3.48"),
    ("1.3.48", "saṃpravadanti kukkuṭāḥ",
     dict(root="vad", artha="vyaktAyAM vAci", upasargas=["sam"], sense="samuccāraṇa"), P, "1.3.78"),
    ("1.3.49", "anuvadate kaṭhaḥ",
     dict(root="vad", artha="vyaktAyAM vAci", upasargas=["anu"], given=["akarmaka", "vyaktavāc"]), A, "1.3.49"),
    ("1.3.49", "anuvadati vīṇā",
     dict(root="vad", artha="vyaktAyAM vAci", upasargas=["anu"], given=["akarmaka"]), P, "1.3.78"),

    # 1.3.51 – 1.3.56
    ("1.3.51", "avagirate", dict(root="gṝ", upasargas=["ava"]), A, "1.3.51"),
    ("1.3.51", "girati", dict(root="gṝ"), P, "1.3.78"),
    ("1.3.52", "śataṃ saṃgirate",
     dict(root="gṝ", upasargas=["sam"], sense="pratijñāna"), A, "1.3.52"),
    ("1.3.52", "saṃgirati grāsam", dict(root="gṝ", upasargas=["sam"]), P, "1.3.78"),
    ("1.3.53", "geham uccarate",
     dict(root="car", upasargas=["ud"], given=["sakarmaka"]), A, "1.3.53"),
    ("1.3.53", "bāṣpam uccarati",
     dict(root="car", upasargas=["ud"], given=["akarmaka"]), P, "1.3.78"),
    ("1.3.54", "aśvena saṃcarate",
     dict(root="car", upasargas=["sam"], given=["tṛtīyāyukta"]), A, "1.3.54"),
    ("1.3.54", "lokau saṃcarasi", dict(root="car", upasargas=["sam"]), P, "1.3.78"),
    ("1.3.55", "dāsyā saṃprayacchate",
     dict(root="dā", upasargas=["sam"], given=["tṛtīyāyukta", "caturthyartha"]),
     A, "1.3.55"),
    ("1.3.55", "pāṇinā saṃprayacchati",
     dict(root="dā", upasargas=["sam"], given=["tṛtīyāyukta"]), P, "1.3.78"),
    ("1.3.56", "bhāryām upayacchate",
     dict(root="yam", upasargas=["upa"], sense="svakaraṇa"), A, "1.3.56"),

    # 1.3.57 – 1.3.61, the desiderative, शद् and मृ
    ("1.3.57", "naṣṭaṃ susmūrṣate", dict(root="smṛ", affixes=["san"]), A, "1.3.57"),
    ("1.3.57", "nṛpaṃ didṛkṣate", dict(root="dṛś", affixes=["san"]), A, "1.3.57"),
    ("1.3.57", "smarati", dict(root="smṛ"), P, "1.3.78"),
    ("1.3.58", "putram anujijñāsati",
     dict(root="jñā", upasargas=["anu"], affixes=["san"]), P, "1.3.78"),
    ("1.3.58", "dharmaṃ jijñāsate", dict(root="jñā", affixes=["san"]), A, "1.3.57"),
    ("1.3.59", "pratiśuśrūṣati",
     dict(root="śru", upasargas=["prati"], affixes=["san"]), P, "1.3.78"),
    ("1.3.60", "śīyate", dict(root="śad", given=["śit"]), A, "1.3.60"),
    ("1.3.60", "śatsyati", dict(root="śad"), P, "1.3.78"),
    ("1.3.61", "amṛta", dict(root="mṛ", lakara="luṅ"), A, "1.3.61"),
    ("1.3.61", "mṛṣīṣṭa", dict(root="mṛ", lakara="liṅ"), A, "1.3.61"),
    ("1.3.61", "mriyate", dict(root="mṛ", given=["śit"]), A, "1.3.61"),
    ("1.3.61", "mariṣyati", dict(root="mṛ", lakara="lṛṭ"), P, "1.3.78"),

    # 1.3.64 – 1.3.66
    ("1.3.64", "prayuṅkte", dict(root="yuj", artha="yoge", upasargas=["pra"]), A, "1.3.64"),
    ("1.3.64", "pātrāṇi prayunakti",
     dict(root="yuj", artha="yoge", upasargas=["pra"], sense="yajñapātra"), P, "1.3.78"),
    ("1.3.65", "saṃkṣṇute śastram", dict(root="kṣṇu", upasargas=["sam"]), A, "1.3.65"),
    ("1.3.66", "bhuṅkte", dict(root="bhuj", artha="pAlanAByavahArayoH"), A, "1.3.66"),
    ("1.3.66", "bhunakty enam", dict(root="bhuj", artha="pAlanAByavahArayoH", sense="avana"), P, "1.3.78"),

    # 1.3.67 – 1.3.71, the causative
    ("1.3.67", "ārohayate hastī",
     dict(root="ruh", affixes=["ṇic"], given=["aṇau-karma-ṇau-kartā"]), A, "1.3.67"),
    ("1.3.67", "smarayaty enam",
     dict(root="smṛ", affixes=["ṇic"], given=["aṇau-karma-ṇau-kartā"],
          sense="ādhyāna"), P, None),
    ("1.3.68", "jaṭilo bhīṣayate",
     dict(root="bhī", affixes=["ṇic"], sense="hetubhaya"), A, "1.3.68"),
    ("1.3.69", "māṇavakaṃ vañcayate",
     dict(root="vañc", affixes=["ṇic"], sense="pralambhana"), A, "1.3.69"),
    ("1.3.69", "ahiṃ vañcayati", dict(root="vañc", affixes=["ṇic"]), P, None),
    ("1.3.70", "jaṭābhir ālāpayate",
     dict(root="lī", affixes=["ṇic"], sense="sammānana"), A, "1.3.70"),
    ("1.3.71", "padaṃ mithyā kārayate",
     dict(root="kṛ", affixes=["ṇic"], upapada="mithyā", sense="abhyāsa"), A, "1.3.71"),

    # 1.3.72 – 1.3.77
    ("1.3.72", "yajate", dict(root="yaj", given=["kartrabhiprāya-kriyāphala"]), A, "1.3.72"),
    ("1.3.72", "kurute", dict(root="kṛ", given=["kartrabhiprāya-kriyāphala"]), A, "1.3.72"),
    ("1.3.72", "yajanti yājakāḥ", dict(root="yaj"), P, "1.3.78"),
    ("1.3.73", "nyāyam apavadate",
     dict(root="vad", artha="vyaktAyAM vAci", upasargas=["apa"], given=["kartrabhiprāya-kriyāphala"]),
     A, "1.3.73"),
    ("1.3.73", "apavadati", dict(root="vad", artha="vyaktAyAM vAci", upasargas=["apa"]), P, "1.3.78"),
    ("1.3.75", "bhāram udyacchate",
     dict(root="yam", upasargas=["ud"], given=["kartrabhiprāya-kriyāphala"]),
     A, "1.3.75"),
    ("1.3.75", "udyacchati cikitsām",
     dict(root="yam", upasargas=["ud"], sense="grantha",
          given=["kartrabhiprāya-kriyāphala"]), P, "1.3.78"),
    ("1.3.76", "gāṃ jānīte",
     dict(root="jñā", given=["kartrabhiprāya-kriyāphala"]), A, "1.3.76"),
    ("1.3.76", "na prajānāti mūḍhaḥ",
     dict(root="jñā", upasargas=["pra"], given=["kartrabhiprāya-kriyāphala"]),
     P, "1.3.78"),

    ("1.3.74", "kaṭaṃ kārayate",
     dict(root="kṛ", affixes=["ṇic"], given=["kartrabhiprāya-kriyāphala"]),
     A, "1.3.74"),
    ("1.3.74", "kaṭaṃ kārayati parasya", dict(root="kṛ", affixes=["ṇic"]), P, "1.3.78"),

    # 1.3.79 – 1.3.93, parasmaipada taken back
    ("1.3.79", "anukaroti",
     dict(root="kṛ", upasargas=["anu"], given=["kartrabhiprāya-kriyāphala"]),
     P, "1.3.79"),
    ("1.3.80", "abhikṣipati", dict(root="kṣip", upasargas=["abhi"],
                                   given=["kartrabhiprāya-kriyāphala"]), P, "1.3.80"),
    ("1.3.80", "ākṣipate", dict(root="kṣip", upasargas=["ā"],
                                given=["kartrabhiprāya-kriyāphala"]), A, "1.3.72"),
    ("1.3.81", "pravahati", dict(root="vah", upasargas=["pra"],
                                 given=["kartrabhiprāya-kriyāphala"]), P, "1.3.81"),
    ("1.3.82", "parimṛṣyati", dict(root="mṛṣ", upasargas=["pari"],
                                   given=["kartrabhiprāya-kriyāphala"]), P, "1.3.82"),
    ("1.3.83", "viramati", dict(root="ram", upasargas=["vi"]), P, "1.3.83"),
    ("1.3.83", "abhiramate", dict(root="ram", upasargas=["abhi"]), A, "1.3.12"),
    ("1.3.84", "devadattam uparamati",
     dict(root="ram", upasargas=["upa"], given=["sakarmaka"]), P, "1.3.84"),
    ("1.3.86", "bodhayati", dict(root="budh", affixes=["ṇic"]), P, "1.3.86"),
    ("1.3.86", "drāvayati", dict(root="dru", affixes=["ṇic"]), P, "1.3.86"),
    ("1.3.87", "bhojayati", dict(root="bhuj", affixes=["ṇic"]), P, "1.3.87"),
    ("1.3.87", "calayati", dict(root="cal", affixes=["ṇic"]), P, "1.3.87"),
    ("1.3.88", "āsayati devadattam",
     dict(root="āsa̐", affixes=["ṇic"],
          given=["aṇau-akarmaka", "cittavat-kartṛka"]), P, "1.3.88"),
    ("1.3.88", "śoṣayate vrīhīn ātapaḥ",
     dict(root="śuṣ", affixes=["ṇic"], given=["aṇau-akarmaka",
                                              "kartrabhiprāya-kriyāphala"]),
     A, "1.3.74"),
    ("1.3.89", "rocayate", dict(root="ruc", affixes=["ṇic"],
                                given=["kartrabhiprāya-kriyāphala"]), A, "1.3.74"),
    ("1.3.89", "nartayate", dict(root="nṛt", affixes=["ṇic"],
                                 given=["kartrabhiprāya-kriyāphala"]), A, "1.3.74"),
    ("1.3.89", "vāsayate", dict(root="vas", affixes=["ṇic"],
                                given=["kartrabhiprāya-kriyāphala"]), A, "1.3.74"),
]

#: The Kāśikā marks these as वा or विभाषा — both sets stand.
OPTIONAL = [
    ("1.3.43", "kramate / krāmati", dict(root="kram")),
    ("1.3.50", "vipravadante / vipravadanti",
     dict(root="vad", artha="vyaktAyAM vAci", upasargas=["vi"], sense="vipralāpa",
          given=["vyaktavāc", "samuccāraṇa"])),
    ("1.3.77", "svaṃ yajñaṃ yajati / yajate",
     dict(root="yaj", upapada="sva", given=["upapadena-pratīyamāna"])),
    ("1.3.85", "uparamati / uparamate",
     dict(root="ram", upasargas=["upa"], given=["akarmaka"])),
    ("1.3.90", "lohitāyati / lohitāyate", dict(root="lohitāya", affixes=["kyaṣ"])),
    ("1.3.91", "vyadyutat / vyadyotiṣṭa", dict(root="dyut", lakara="luṅ")),
    ("1.3.92", "vartsyati / vartiṣyate", dict(root="vṛt", affixes=["sya"])),
    ("1.3.93", "kalptā / kalpitā", dict(root="kḷp", lakara="luṭ")),
]


class WorkedForms(unittest.TestCase):
    """Every use the Kāśikā works out, against what it says results."""

    def test_each_worked_form_comes_out_as_the_kasika_says(self):
        for sutra, form, use, expected, by in WORKED:
            with self.subTest(sutra=sutra, form=form):
                verdict = pada_of_usage(**use)
                self.assertIs(verdict.pada, expected,
                              f"{sutra} {form}: got {verdict.by} — {verdict.why}")
                if by is not None:
                    self.assertEqual(verdict.by, by, f"{sutra} {form}")

    def test_the_counter_examples_really_fail_the_condition(self):
        """
        Not the same test as the one above. A counter-example is only
        evidence if the *same* use with the condition restored flips the
        answer — otherwise the rule might be inert.
        """
        flipped = 0
        for sutra, form, use, expected, by in WORKED:
            if expected is not P or by != "1.3.78":
                continue
            flipped += 1
            self.assertIs(pada_of_usage(**use).pada, P, f"{sutra} {form}")
        self.assertGreater(flipped, 25)

    def test_every_optional_rule_reports_both_sets(self):
        for sutra, form, use in OPTIONAL:
            with self.subTest(sutra=sutra, form=form):
                verdict = pada_of_usage(**use)
                self.assertTrue(verdict.optional, f"{sutra} {form} not optional")
                self.assertEqual(verdict.by, sutra, form)

    def test_the_table_covers_the_block(self):
        """A sūtra with no worked form in this file is a sūtra nothing tests."""
        tested = {row[0] for row in WORKED} | {row[0] for row in OPTIONAL}
        # 1.3.62 and 1.3.63 have their own tests; 1.3.78 is exercised by every
        # counter-example above.
        untested = [
            f"1.3.{n}" for n in range(14, 94)
            if f"1.3.{n}" not in tested and n not in (62, 63, 78)
        ]
        self.assertEqual(untested, [])


class TwoKindsOfOption(unittest.TestCase):
    """
    अप्राप्तविभाषा and प्राप्तविभाषा — the Kāśikā names both, and they behave
    oppositely when an option meets an invariable rule.
    """

    def test_an_aprapta_option_yields_to_the_invariable_rule(self):
        """
        1.3.43 offers क्रमते / क्रामति for क्रम् without an upasarga. But in the
        senses 1.3.38 names, the ātmanepada is already had, so ऋक्ष्वस्य क्रमते
        बुद्धिः is not optional — अप्राप्तविभाषेयम्.
        """
        settled = pada_of_usage("kram", sense="vṛtti")
        self.assertEqual(settled.by, "1.3.38")
        self.assertFalse(settled.optional)

    def test_and_still_offers_the_option_where_nothing_else_reaches(self):
        offered = pada_of_usage("kram")
        self.assertTrue(offered.optional)
        self.assertEqual(offered.by, "1.3.43")

    def test_a_prapta_option_displaces_the_invariable_rule(self):
        """
        1.3.85 is the other kind — पूर्वेण नित्ये परस्मैपदे प्राप्ते विकल्प
        आरभ्यते. 1.3.84 made उपरमति invariable and this makes it optional, so
        here the later rule wins rather than yielding.
        """
        invariable = pada_of_usage("ram", upasargas=["upa"], given=["sakarmaka"])
        self.assertEqual(invariable.by, "1.3.84")
        self.assertFalse(invariable.optional)

        offered = pada_of_usage("ram", upasargas=["upa"], given=["akarmaka"])
        self.assertEqual(offered.by, "1.3.85")
        self.assertTrue(offered.optional)

    def test_the_distinction_is_recorded_in_both_notes(self):
        self.assertIn("अप्राप्तविभाष", REGISTRY.get("1.3.43").notes)
        self.assertIn("प्राप्तविभाषेयम्", REGISTRY.get("1.3.50").notes)
        self.assertNotIn("अप्राप्त", REGISTRY.get("1.3.50").notes)


class DerivedFromTheDhatupatha(unittest.TestCase):
    """The places where the codification reads rather than lists."""

    def test_1_3_15_names_its_roots_by_sense_and_the_sense_is_in_the_file(self):
        """
        गम् and सृप् are `gatO`; हन् is `hiMsAgatyoH` and falls under both. लू
        and पू are neither, which is exactly why 1.3.14 keeps them.
        """
        self.assertIn("gati", root_senses("gam"))
        self.assertIn("gati", root_senses("sṛp"))
        self.assertEqual(root_senses("han"), frozenset({"gati", "hiṃsā"}))
        self.assertEqual(root_senses("lū"), frozenset())
        self.assertEqual(root_senses("pū"), frozenset())

    def test_the_vartika_on_1_3_15_is_not_redundant(self):
        """
        हसादीनामुपसंख्यानम् adds three roots, and the point is that the sūtra
        could not have reached them: none of the three is गत्यर्थ or हिंसार्थ by
        the file's own gloss. If it could, the vārttika would be idle and the
        codification would be listing them for nothing.
        """
        for root in ("has", "jalp", "paṭh"):
            self.assertEqual(root_senses(root), frozenset(), root)
            self.assertIs(
                pada_of_usage(root, given=["karmavyatihāra"]).pada, P, root
            )

    def test_the_second_vartika_on_1_3_15_is_confirmatory_here(self):
        """
        हरतेरप्रतिषेधः. On this recension हृ is `haraRe`/`prasahyakaraRe` and so
        was never reached by the prohibition — the ātmanepada stands with or
        without the vārttika. Recording that is more useful than pretending
        the supplement changed the answer.
        """
        self.assertEqual(root_senses("hṛ"), frozenset())
        self.assertIs(pada_of_usage("hṛ", given=["karmavyatihāra"]).pada, A)

    def test_1_3_87_derives_its_roots_the_same_way(self):
        """निगरण is अभ्यवहार and चलन is कम्पन, both the Kāśikā's own glosses."""
        self.assertIn("nigaraṇa", root_senses("bhuj"))
        self.assertIn("nigaraṇa", root_senses("pā"))
        self.assertIn("calana", root_senses("cal"))
        self.assertNotIn("calana", root_senses("kṛ"))

    def test_the_vartika_on_1_3_87_is_recorded_as_not_codified(self):
        """
        अदेः प्रतिषेधः exempts अद्, and अद् *is* reached by the derivation —
        the file glosses it `BakzaRe`. So आदयते देवदत्तेन comes out wrong, and
        the note has to say so rather than the test quietly skipping it.
        """
        self.assertIn("nigaraṇa", root_senses("ad"))
        self.assertIs(pada_of_usage("ad", affixes=["ṇic"]).pada, P)
        self.assertIn("अदेः प्रतिषेधः", REGISTRY.get("1.3.87").notes)
        self.assertIn("SCOPE", REGISTRY.get("1.3.87").notes)

    def test_1_3_91s_gana_is_a_run_with_the_ends_the_kasika_fixes(self):
        """द्युत (धा.पा. ७४१) … कृपू (७६२), by साहचर्य."""
        gana = dyutadi()
        self.assertEqual(gana[0], "dyut")
        self.assertEqual(gana[-1], "kṛp")
        self.assertGreater(len(gana), 20)

    def test_1_3_92s_gana_is_named_member_by_member_and_all_five_match(self):
        """
        वृतु, वृधु, शृधु, स्यन्दू, कृपू — the Kāśikā lists every one while
        glossing the sūtra, so this is checkable at each member and not only
        at the ends.
        """
        self.assertEqual(vrtadi(), ("vṛt", "vṛdh", "śṛdh", "syand", "kṛp"))

    def test_the_two_ganas_nest(self):
        """वृतादि is a tail of द्युतादि — द्युतादिष्वेव वृतादयः पठ्यन्ते."""
        self.assertEqual(dyutadi()[-len(vrtadi()):], vrtadi())

    def test_the_dyut_gana_is_anudattet_which_is_why_1_3_91_is_optional(self):
        """अनुदात्तेत्त्वान्नित्यमेवात्मनेपदे प्राप्ते — the option withdraws."""
        self.assertIs(pada_of_usage("dyut").pada, A)
        self.assertEqual(pada_of_usage("dyut").by, "1.3.12")
        self.assertTrue(pada_of_usage("dyut", lakara="luṅ").optional)


class Akartrabhipraya(unittest.TestCase):
    """
    The thirteen sūtras the Kāśikā opens with अकर्त्रभिप्रायार्थोऽयमारम्भः.

    Each says: this root already has ātmanepada by 1.3.72 where the fruit
    reaches the agent, so the sūtra is for the case where it does not. The
    claim is checkable, because 1.3.72's two marks are in the dhātupāṭha.
    """

    #: root, and which mark the Kāśikā says it carries
    CLAIMED = [
        ("krī", "ñit", "1.3.18"),
        ("hve", "ñit", "1.3.30"),
        ("nī", "ñit", "1.3.36"),
        ("kṛ", "ñit", "1.3.32"),
        ("yuj", "svaritet", "1.3.64"),
    ]

    def test_each_root_carries_the_mark_the_kasika_claims(self):
        for root, mark, sutra in self.CLAIMED:
            with self.subTest(root=root, sutra=sutra):
                test = is_nyit if mark == "ñit" else is_svaritet
                self.assertTrue(test(root), f"{root} should be {mark}")

    def test_and_so_1_3_72_would_already_have_covered_the_other_case(self):
        for root, _, _ in self.CLAIMED:
            verdict = pada_of_usage(root, given=["kartrabhiprāya-kriyāphala"])
            self.assertIs(verdict.pada, A, root)
            self.assertEqual(verdict.by, "1.3.72", root)

    def test_which_is_why_the_sutras_are_not_redundant(self):
        """
        Without the fruit-to-agent condition, 1.3.72 does nothing and the
        sūtra is the only thing granting the middle endings.
        """
        for root, sutra, use in [
            ("krī", "1.3.18", dict(upasargas=["vi"])),
            ("hve", "1.3.30", dict(upasargas=["ni"])),
            ("nī", "1.3.36", dict(sense="utsañjana")),
            ("yuj", "1.3.64", dict(upasargas=["pra"])),
        ]:
            verdict = pada_of_usage(root, **use)
            self.assertIs(verdict.pada, A, root)
            self.assertEqual(verdict.by, sutra, root)

    def test_the_svaritet_roots_1_3_79_to_1_3_82_take_back(self):
        """
        Those four sūtras only make sense if their roots have the ātmanepada
        to lose, and the Kāśikā says each is svaritet. क्षिप is the sharp
        case: the file reads it twice and only the sixth-gaṇa entry is marked.
        """
        for root, sutra in [("kṣip", "1.3.80"), ("vah", "1.3.81"),
                            ("mṛṣ", "1.3.82")]:
            self.assertTrue(is_svaritet(root), f"{root} — {sutra}")

        by_code = {e.code: e for e in entries_for("kṣip")}
        self.assertEqual(sorted(by_code), ["04.0015", "06.0005"])


class Purvavat(unittest.TestCase):
    """1.3.62 पूर्ववत् सनः — the atideśa, and what it does not carry."""

    def test_the_kasikas_four_positives(self):
        for form, use, expect_by in [
            ("āsisiṣate", dict(root="āsa̐"), "1.3.12"),
            ("śiśayiṣate", dict(root="śīṅ"), "1.3.12"),
            ("nivivikṣate", dict(root="viś", upasargas=["ni"]), "1.3.17"),
            ("ācikraṃsate",
             dict(root="kram", upasargas=["ā"], sense="udgamana"), "1.3.40"),
        ]:
            with self.subTest(form=form):
                verdict = pada_of_usage(affixes=["san"], **use)
                self.assertIs(verdict.pada, A, form)
                self.assertIn(expect_by, (verdict.by,) + verdict.also_by, form)

    def test_the_kasikas_four_negatives_fall_out_of_the_mechanism(self):
        """
        न हि शदिम्रियतिमात्रमात्मनेपदनिमित्तम् — being शद् or मृ is not itself the
        cause; the cause is the शित् or the lakāra, and neither survives under
        सन्. Nothing excludes these by name: they fail because the atideśa
        carries the cause and the cause is absent.
        """
        for form, use in [
            ("śiśatsati", dict(root="śad")),
            ("mumūrṣati", dict(root="mṛ")),
            ("anucikīrṣati", dict(root="kṛ", upasargas=["anu"])),
            ("parācikīrṣati", dict(root="kṛ", upasargas=["parā"])),
        ]:
            with self.subTest(form=form):
                self.assertIs(pada_of_usage(affixes=["san"], **use).pada, P, form)

    def test_the_cause_is_present_without_san_for_the_first_two(self):
        """
        The other half of the same point: शद् and मृ *do* take ātmanepada when
        their cause holds. If they did not, the negatives above would prove
        nothing.
        """
        self.assertIs(pada_of_usage("śad", given=["śit"]).pada, A)
        self.assertIs(pada_of_usage("mṛ", lakara="luṅ").pada, A)

    def test_1_3_63_is_recorded_as_not_codified(self):
        notes = REGISTRY.get("1.3.63").notes
        self.assertIn("SCOPE", notes)
        self.assertIn("लिट्", notes)


class TheResidue(unittest.TestCase):
    """1.3.78 शेषात् कर्तरि परस्मैपदम् and what carries down to it."""

    def test_it_fires_only_when_nothing_else_has(self):
        counted = sum(
            1 for _, _, use, _, by in WORKED
            if by == "1.3.78" and pada_of_usage(**use).by == "1.3.78"
        )
        self.assertGreater(counted, 25)

    def test_it_never_fires_where_an_atmanepada_rule_applies(self):
        for sutra, form, use, expected, _ in WORKED:
            if expected is not A:
                continue
            self.assertNotEqual(pada_of_usage(**use).by, "1.3.78", f"{sutra} {form}")

    def test_the_second_kartrgrahana_reaches_karmakartari(self):
        """
        पच्यत ओदनः स्वयमेव. The Kāśikā's reason is that 1.3.14's second
        कर्तृग्रहण carries down: तेन कर्तैव यः कर्ता, तत्र परस्मैपदं भवति,
        कर्मकर्तरि न भवति. So the residue does not reach it.
        """
        verdict = pada_of_usage("pac", karmakartari=True)
        self.assertIs(verdict.pada, A)
        self.assertNotEqual(verdict.by, "1.3.78")

    def test_the_passive_is_out_by_kartari(self):
        self.assertIs(pada_of_usage("pac", bhava_or_karman=True).pada, A)


class Transparency(unittest.TestCase):
    """What the codification says about itself."""

    def test_a_rule_blocked_by_a_prohibition_says_so(self):
        verdict = pada_of_usage("gam", given=["karmavyatihāra"])
        self.assertIn("1.3.15", verdict.blocked)

    def test_a_rule_that_nearly_fired_is_reported(self):
        """
        उपतिष्ठति with the transitivity unstated: 1.3.26 wanted one more fact,
        and the answer should say which rather than fall silently to 1.3.78.
        """
        ctx = VerbContext(root="sthā", upasargas=("upa",))
        wanting = dict(near_misses(ctx))
        self.assertIn("1.3.26", wanting)
        self.assertEqual(wanting["1.3.26"], ("akarmaka not stated",))
        self.assertIs(resolve(ctx).pada, P)

    def test_the_near_miss_disappears_once_the_fact_is_supplied(self):
        ctx = VerbContext(root="sthā", upasargas=("upa",), given=("akarmaka",))
        self.assertNotIn("1.3.26", dict(near_misses(ctx)))
        self.assertEqual(resolve(ctx).by, "1.3.26")

    def test_every_verdict_names_a_sutra_that_exists(self):
        for _, form, use, _, _ in WORKED:
            by = pada_of_usage(**use).by
            self.assertTrue(REGISTRY.has(by.split("niyama")[0]), f"{form}: {by}")

    def test_the_ambiguity_of_a_name_read_twice_is_reachable(self):
        """
        वह् is anudāttet in one entry and svaritet in the other, and the
        resolver picks the more generous reading. That is a real limitation,
        so it has to be visible: `entries_for` takes the artha the way the
        commentaries cite it.
        """
        self.assertEqual(len(entries_for("vah")), 2)
        self.assertEqual(len(entries_for("vah", artha="prApaRe")), 1)


class Registration(unittest.TestCase):
    def test_the_whole_pada_is_codified_with_no_gaps(self):
        missing = [f"1.3.{n}" for n in range(1, 94) if not REGISTRY.has(f"1.3.{n}")]
        self.assertEqual(missing, [])

    def test_each_record_carries_the_conditions_it_tests(self):
        """
        The codification line is generated from the provision table, so it
        cannot say something the resolver does not do.
        """
        for number in range(14, 94):
            sutra = f"1.3.{number}"
            provisions = provisions_for(sutra)
            if not provisions:
                continue
            line = REGISTRY.get(sutra).codification
            for provision in provisions:
                self.assertIn(provision.describe(), line, sutra)

    def test_the_generated_notes_are_not_empty_and_cite_a_form(self):
        for number in range(14, 94):
            notes = REGISTRY.get(f"1.3.{number}").notes
            self.assertGreater(len(notes), 60, f"1.3.{number}")
            self.assertTrue(
                notes.startswith("SETTLED") or notes.startswith("SCOPE"),
                f"1.3.{number}: {notes[:40]}",
            )

    def test_the_anuvrtti_of_akarmaka_stops_where_the_kasika_says(self):
        """
        अकर्मकात् is introduced at 1.3.26 and the Kāśikā closes it at 1.3.30
        with अकर्मकादिति निवृत्तम्. The corpus's anuvṛtti, which nobody here
        wrote, agrees exactly: 27, 28 and 29 carry it and 30 does not.
        """
        def carries(sutra_id):
            return any(item.from_sutra == "1.3.26" for item in facts(sutra_id).anuvrtti)

        for sutra_id in ("1.3.27", "1.3.28", "1.3.29"):
            self.assertTrue(carries(sutra_id), sutra_id)
        self.assertFalse(carries("1.3.30"))

    def test_the_codification_honours_that_window(self):
        """And the provisions require it in exactly those three and no more."""
        needs = {
            f"1.3.{n}" for n in range(26, 31)
            for p in provisions_for(f"1.3.{n}") if "akarmaka" in p.requires
        }
        self.assertEqual(needs, {"1.3.26", "1.3.27", "1.3.28", "1.3.29"})

    def test_no_provision_names_a_root_the_dhatupatha_does_not_have(self):
        """
        A misspelt root is a rule that silently never fires, which is the
        worst kind of bug here because everything still passes.
        """
        unknown = sorted({
            root for provision in PROVISIONS for root in provision.roots
            if not entries_for(root)
        })
        self.assertEqual(unknown, [])


if __name__ == "__main__":
    unittest.main()
