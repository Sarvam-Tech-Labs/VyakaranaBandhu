# -*- coding: utf-8 -*-
"""
Worked inputs for each sūtra's playground.

A form with eight empty fields is not usable by someone meeting a rule for the
first time — they would have to know the answer already to fill it in. So each
sūtra carries a few ready-made inputs: click one and the form fills with a case
the Kāśikā actually works, and the rule fires in front of you.

**Most of them are not written here.** For the four blocks driven by a
provision table — 1.2.1–26, 1.3.14–93, 1.4.23–55 and 1.4.56–98, 182 sūtras
between them — a rule's *conditions are* the input that makes it fire. The
first root it names, the first upasarga, the sense it wants, the assertions it
requires: put those together and the rule applies. So they are derived, and
adding a provision gets a worked input free.

That is worth more than the saving. A hand-written input can drift from the
rule it belongs to and nothing notices; a derived one cannot, and the test that
every case actually fires its own sūtra then has something to catch.

What is written by hand is the rest — 177 sūtras across 76 shapes of function,
where there is no table to read the conditions off. Each of those is one of the
Kāśikā's own worked forms, the same one the sūtra's note cites.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Tuple


@dataclass(frozen=True)
class Case:
    """One ready-made input, and what it is meant to show."""

    label: str
    values: Dict[str, Any]
    #: "worked" — the rule fires. "counter" — it does not, and that is the
    #: point: a form the Kāśikā gives to show what the condition keeps out.
    kind: str = "worked"
    note: str = ""


# --- derived from the provision tables ------------------------------------

#: Two sūtras require *some* upasarga without naming one — 1.3.44's
#: सोपसर्गश्चायम्, अपह्नवे वर्तते, न केवलः, and 1.4.38's उपसृष्टयोः. The
#: conditions cannot say which, so the worked form is taken from the Kāśikā's
#: own example: शतम् अपजानीते and देवदत्तम् अभिक्रुध्यति.
_SOME_UPASARGA = {"1.3.44": "apa", "1.4.38": "abhi"}


def _atmanepada(p) -> List[Case]:
    """1.3.14–1.3.93. The root, an upasarga, a sense, the assertions."""
    values: Dict[str, Any] = {}
    if p.roots:
        values["root"] = p.roots[0]
    elif p.marks:
        # A rule that names no root but a mark: pick a root that carries it.
        values["root"] = {"svaritet": "vah", "ñit": "kṛ",
                          "anudāttet": "āsa̐", "ṅit": "śīṅ"}[p.marks[0]]
    else:
        values["root"] = "lū"
    if p.root_senses:
        values["root"] = {"gati": "gam", "hiṃsā": "han",
                          "nigaraṇa": "bhuj", "calana": "cal"}[p.root_senses[0]]
    if p.upasargas:
        values["upasargas"] = [p.upasargas[0]]
    elif p.upasarga is True:
        values["upasargas"] = [_SOME_UPASARGA[p.sutra]]
    if p.senses:
        values["sense"] = p.senses[0]
    if p.upapadas:
        values["upapada"] = p.upapadas[0]
    if p.affixes:
        values["affixes"] = [p.affixes[0]]
    if p.lakaras:
        values["lakara"] = p.lakaras[0]
    if p.requires:
        values["given"] = list(p.requires)
    return [Case(p.example or p.sutra, values, note=p.gloss)]


def _kittva(p) -> List[Case]:
    """1.2.1–1.2.26. The root and the affix, plus what is asserted."""
    values: Dict[str, Any] = {}
    if p.roots:
        values["root"] = p.roots[0]
    elif p.gana:
        values["root"] = p.gana[0]
    else:
        values["root"] = "bhid"
    if p.shapes:
        # A shape condition needs a root that satisfies it.
        values["root"] = {
            "asaṃyogānta": "bhid", "ik-final": "ci",
            "ik-then-consonant": "bhid", "ṛ-final": "kṛ",
            "u-penult": "dyut", "n-penult": "granth",
            "th-or-ph-final": "granth", "ral-final": "dyut",
            "u-or-i-penult": "dyut", "hal-initial": "dyut",
        }.get(p.shapes[0], values["root"])
    values["affix"] = p.affixes[0] if p.affixes else "tṛc"
    if p.senses:
        values["sense"] = p.senses[0]
    given = list(p.requires)
    if p.affixes and "jhalādi" not in p.shapes and "seṭ" not in given:
        pass
    if given:
        values["given"] = given
    return [Case(p.example or p.sutra, values, note=p.gloss)]


def _karaka(p) -> List[Case]:
    """1.4.23–1.4.55. The verb, its class, and the semantic assertion."""
    values: Dict[str, Any] = {}
    if p.roots:
        values["verb"] = p.roots[0]
    if p.senses:
        values["verb_sense"] = [p.senses[0]]
    if p.upasargas:
        values["upasargas"] = [p.upasargas[0]]
    elif p.upasarga is True:
        values["upasargas"] = [_SOME_UPASARGA[p.sutra]]
    if p.requires:
        values["given"] = list(p.requires)
    if p.causative:
        values["causative"] = True
    return [Case(p.example or p.sutra, values, note=p.gloss)]


def _nipata(p) -> List[Case]:
    """1.4.56–1.4.98. The word, and whether a verb is there."""
    values: Dict[str, Any] = {}
    if p.words:
        values["form"] = p.words[0]
    elif p.gana:
        values["form"] = p.gana[0]
    if p.kriya_yoga:
        values["kriya_yoga"] = True
    if p.senses:
        values["sense"] = p.senses[0]
    if p.with_kr:
        values["with_kr"] = True
    if p.anukarana:
        values["anukarana"] = True
    return [Case(p.example or p.sutra, values, note=p.gloss)]



#: The partner word, from the Kāśikā's own worked form for each rule.
#:
#: Everything else a case needs — the named word, the sense, the case the
#: other member stands in, the facts to assert — is read off the provision,
#: so it cannot drift from the rule. What the table genuinely cannot supply
#: is *which* noun to compound with, since no condition constrains it: any
#: pot will do for उपकुम्भम्. That one word per rule is named here.
_SAMASA_PARTNER = {
    "2.1.6": {"first": "upa", "second": "kumbha", "sense": "samīpa"},
    "2.1.7": {"second": "vṛddha"},
    "2.1.8": {"second": "amatra"},
    "2.1.9": {"first": "śāka"},
    "2.1.10": {"first": "akṣa"},
    "2.1.12": {"second": "trigarta"},
    "2.1.13": {"second": "pāṭaliputra", "sense": "maryādā"},
    "2.1.14": {"second": "agni"},
    "2.1.15": {"second": "vana"},
    "2.1.16": {"second": "gaṅgā"},
    "2.1.17": {"first": "tiṣṭhadgu", "second": "tiṣṭhadgu"},
    # 2.1.48 is the other nipātana rule: its forms are given whole,
    # so there is no pair to build one from and the gaṇa supplies it.
    "2.1.48": {"first": "pātresamitāḥ", "second": "pātresamitāḥ"},
    "2.1.18": {"second": "gaṅgā"},
    "2.1.19": {"first": "dvi", "second": "muni"},
    "2.1.20": {"first": "pañcan", "second": "nada"},
    "2.1.21": {"first": "unmatta", "second": "gaṅgā"},
    # From 2.1.30 the conditions stop naming words and start asserting
    # facts, so the pair has to come from here or the form comes up empty.
    # A list gives one seed per row, in the order the rows are written.
    "2.1.24": [{"first": "kaṣṭa"}, {"first": "grāma"}],
    "2.1.25": {"second": "dhauta"},
    "2.1.26": {"second": "ārūḍha"},
    "2.1.27": {"second": "kṛta"},
    "2.1.28": {"first": "ahar", "second": "saṃkrānta"},
    "2.1.29": {"first": "muhūrta", "second": "sukha"},
    "2.1.30": [{"first": "śaṅkulā", "second": "khaṇḍa"},
               {"first": "dhānya"}],
    "2.1.31": [{"first": "māsa"}, {"first": "māsa"}],
    "2.1.32": {"first": "ahi", "second": "hata"},
    "2.1.33": {"first": "kāka", "second": "peya"},
    "2.1.34": {"first": "dadhi", "second": "odana"},
    "2.1.35": {"first": "guḍa", "second": "dhānā"},
    "2.1.36": [{"first": "yūpa", "second": "dāru"},
               {"first": "brāhmaṇa"}, {"first": "kubera"}],
    "2.1.37": [{"first": "vṛka"}, {"first": "vṛka"}],
    "2.1.38": {"first": "sukha"},
    "2.1.39": {"second": "mukta"},
    "2.1.40": {"first": "akṣa"},
    "2.1.41": {"first": "sthālī"},
    "2.1.42": {"first": "tīrtha", "second": "dhvāṅkṣa"},
    "2.1.43": {"first": "māsa", "second": "deya"},
    "2.1.44": {"first": "araṇya", "second": "tilaka"},
    "2.1.45": {"first": "pūrvāhṇa", "second": "kṛta"},
    "2.1.46": {"second": "bhukta"},
    "2.1.47": {"first": "bhasman", "second": "huta"},
    "2.1.49": {"second": "anulipta"},
    "2.1.50": [{"first": "pūrva", "second": "iṣukāmaśamī"},
               {"first": "pañcan", "second": "āmra"}],
    "2.1.53": {"first": "vaiyākaraṇa", "second": "khasūci"},
    "2.1.54": {"second": "nāpita"},
    "2.1.55": {"first": "śastrī", "second": "śyāmā"},
    "2.1.56": {"first": "puruṣa"},
    "2.1.57": {"first": "nīla", "second": "utpala"},
    "2.1.58": {"second": "puruṣa"},
    # 2.1.59 names BOTH members, and the generator reads only `words`,
    # so the second gaṇa has to come from here.
    "2.1.59": {"second": "kṛta"},
    "2.1.60": {"first": "kṛta", "second": "akṛta"},
    "2.2.24": {"first": "prāptodaka", "second": "grāma"},
    "2.2.25": [{"second": "daśan"}, {"first": "dvi",
                                     "second": "tri"}],
    "2.2.26": {"first": "dakṣiṇa", "second": "pūrva"},
    "2.2.27": {"first": "daṇḍa", "second": "daṇḍa"},
    "2.2.28": {"second": "putra"},
    "2.2.29": {"first": "plakṣa", "second": "nyagrodha"},
    "2.2.12": {"first": "rājan", "second": "mata"},
    "2.2.13": {"first": "etad", "second": "āsita"},
    "2.2.14": {"first": "go", "second": "doha"},
    "2.2.15": {"first": "bhavat", "second": "śāyikā"},
    "2.2.16": {"first": "ap", "second": "sraṣṭṛ"},
    "2.2.17": {"first": "danta", "second": "lekhaka"},
    "2.2.18": {"first": "ku", "second": "puruṣa"},
    "2.2.19": {"first": "kumbha", "second": "kāra"},
    "2.2.20": {"first": "svādum", "second": "kāra"},
    "2.2.21": {"first": "mūlaka", "second": "upadaṃśa"},
    "2.2.22": {"first": "uccais", "second": "kṛtvā"},
    "2.2.1": {"second": "kāya"},
    "2.2.2": {"second": "pippalī"},
    "2.2.3": {"second": "bhikṣā"},
    "2.2.4": {"second": "jīvikā"},
    "2.2.5": {"first": "māsa", "second": "jāta"},
    "2.2.6": {"second": "brāhmaṇa"},
    "2.2.7": {"second": "piṅgala"},
    "2.2.8": {"first": "rājan", "second": "puruṣa"},
    "2.2.9": {"first": "brāhmaṇa"},
    "2.2.10": {"first": "manuṣya", "second": "śūratama"},
    "2.2.11": {"first": "chātra", "second": "pañcama"},
    "2.1.62": {"first": "go"},
    "2.1.63": {"second": "kaṭha"},
    "2.1.64": {"second": "rājan"},
    "2.1.65": {"first": "go"},
    "2.1.66": {"first": "go", "second": "matallikā"},
    # Both members named, and the generator reads only `words`.
    "2.1.67": {"second": "khalati"},
    "2.1.68": [{"second": "śveta"},
               {"first": "bhojya", "second": "uṣṇa"}],
    "2.1.69": {"first": "kṛṣṇa", "second": "sāraṅga"},
    "2.1.70": {"second": "śramaṇā"},
    "2.1.71": {"first": "go"},
    "2.1.72": {"first": "mayūravyaṃsaka",
               "second": "mayūravyaṃsaka"},
    "2.1.61": {"second": "puruṣa"},
    "2.1.51": [{"first": "pañcan", "second": "pūlī"},
               {"first": "pañcan", "second": "kapāla"},
               {"first": "pañcan", "second": "gavadhana"}],
    "2.1.24": {"first": "kaṣṭa"},
    "2.1.25": {"second": "dhauta"},
    "2.1.26": {"second": "ārūḍha"},
    "2.1.27": {"second": "kṛta"},
    "2.1.28": {"first": "ahar", "second": "saṃkrānta"},
    "2.1.29": {"first": "muhūrta", "second": "sukha"},
}


def _row_of(p) -> int:
    """Which row of its sūtra this provision is, counting from zero."""
    from src.astadhyayi import samasa

    same = [q for q in samasa.PROVISIONS if q.sutra == p.sutra]
    return same.index(p) if p in same else 0


def _samasa(p) -> List[Case]:
    """
    2.1.6 onward. The two words, the sense, and what must be asserted.

    A sūtra's seed may be one dict for all its rows, or a list with one
    per row — 2.1.50 covers a direction-word and a numeral, and no single
    pair illustrates both.
    """
    found = _SAMASA_PARTNER.get(p.sutra, {})
    if isinstance(found, list):
        row = _row_of(p)
        found = found[row] if row < len(found) else (found[-1] if found
                                                     else {})
    seed = dict(found)
    values: Dict[str, Any] = {
        "first": seed.pop("first", None),
        "second": seed.pop("second", None),
    }
    if p.words:
        values[p.slot] = p.words[0]
    sense = seed.pop("sense", None) or (p.senses[0] if p.senses else None)
    if sense:
        values["sense"] = sense
    # Whose case is whose. The rule names one member and constrains the
    # other, and which is which flips with `slot` — writing both to
    # `second_vibhakti` worked only while every rule named the first.
    other = "first" if p.slot == "second" else "second"
    if p.other_vibhakti is not None:
        values[f"{other}_vibhakti"] = p.other_vibhakti
    if p.vibhakti is not None:
        values[f"{p.slot}_vibhakti"] = p.vibhakti
    if p.requires:
        values["given"] = list(p.requires)
    elif p.prohibits_when:
        # A prohibition has no form to show — it exists to stop one. Its
        # worked input is therefore a pair it actually refuses, and what
        # makes it refuse comes from `prohibits_when`.
        values["given"] = [p.prohibits_when[0]]
    values.update(seed)
    values = {k: v for k, v in values.items() if v is not None}
    return [Case(p.example.split(",")[0] or p.sutra, values, note=p.gloss)]


def _derived(sutra_id: str) -> List[Case]:
    """Whatever the provision tables can supply for this sūtra."""
    from src.astadhyayi import atmanepada, karaka, kittva, nipata, samasa

    found: List[Case] = []
    for table, adapt in (
        (atmanepada.PROVISIONS, _atmanepada),
        (kittva.PROVISIONS, _kittva),
        (karaka.PROVISIONS, _karaka),
        (nipata.PROVISIONS, _nipata),
        (samasa.PROVISIONS, _samasa),
    ):
        for provision in table:
            stem = provision.sutra.split("v")[0].split("niyama")[0]
            # A prohibition assigns nothing, so there is no worked form to
            # show for it; the sūtra it cancels carries the pair instead.
            if stem == sutra_id and not getattr(provision, "blocks", ()):
                found.extend(adapt(provision))
    return found


# --- and the rest, hand-written -------------------------------------------
#
# One of the Kāśikā's own worked forms per sūtra, the same one the note cites.
# Where it gives a counter-example that the codification can show — a case
# where the rule does *not* fire — that is here too, marked as such, because a
# reader learns more from the pair than from either alone.

def _c(label, values, note="", kind="worked") -> Case:
    return Case(label, values, kind=kind, note=note)


CURATED: Dict[str, Tuple[Case, ...]] = {
    # --- 1.1.1 to 1.1.10: vṛddhi, guṇa, and the phonetic saṃjñās ---------
    "1.1.1": (_c("आ is vṛddhi", {"sound": "ā"}),
              _c("ऐ is vṛddhi", {"sound": "ai"}),
              _c("ए is not वृद्धि — it is गुण", {"sound": "e"}, kind="counter")),
    "1.1.2": (_c("ए is guṇa", {"sound": "e"}),
              _c("अ is guṇa", {"sound": "a"}),
              _c("ई is not गुण — merely a long vowel", {"sound": "ī"}, kind="counter")),
    "1.1.3": (_c("इ is what guṇa replaces", {"sound": "i"}),
              _c("ऋ is what guṇa replaces", {"sound": "ṛ"}),
              _c("अ is not an इक्", {"sound": "a"}, kind="counter")),
    "1.1.4": (_c("धातुलोप in an ārdhadhātuka blocks it",
                 {"target": "i", "ardhadhatuka": True, "dhatu_lopa": True}),
              _c("with no elision, nothing is blocked",
                 {"target": "i", "ardhadhatuka": True}, kind="counter")),
    "1.1.5": (_c("a कित् affix blocks it",
                 {"target": "i", "affix.form": "kta", "affix.its": ["k"]}),
              _c("a ङित् affix blocks it",
                 {"target": "i", "affix.form": "ktvā", "affix.its": ["ṅ"]}),
              _c("an unmarked affix does not block it",
                 {"target": "i", "affix.form": "tṛc", "affix.its": []},
                 kind="counter")),
    "1.1.6": (_c("दीधी is exempt", {"target": "i", "item": "dīdhī"}),
              _c("वेवी is exempt", {"target": "i", "item": "vevī"}),
              _c("इट् is exempt", {"target": "i", "item": "iṭ"})),
    "1.1.7": (_c("इन्द्र — न्द्र is a conjunct", {"text": "indra"}),
              _c("भिद् — no conjunct", {"text": "bhid"}, kind="counter")),
    "1.1.8": (_c("ङ् is anunāsika", {"sound": "ṅ"}),
              _c("ञ् is anunāsika", {"sound": "ñ"}),
              _c("क् is not anunāsika", {"sound": "k"}, kind="counter")),
    "1.1.9": (_c("अ and आ are savarṇa", {"first": "a", "second": "ā"}),
              _c("क् and ग् — same place and effort",
                 {"first": "k", "second": "g"}),
              _c("अ and इ are not सवर्ण", {"first": "a", "second": "i"},
                 kind="counter")),
    "1.1.10": (_c("the fourfold scheme rescues 24 pairs",
                  {"scheme": "kāśikā-4"}),
               _c("the fivefold scheme leaves it nothing to do",
                  {"scheme": "kaumudī-5"}, kind="counter")),

    # --- 1.1.11 to 1.1.19: प्रगृह्य --------------------------------------
    "1.1.11": (_c("हरी — an ī-final dual",
                  {"form": "harī", "dvivacana": True}),
               _c("विष्णू — an ऊ-final dual", {"form": "viṣṇū", "dvivacana": True}),
               _c("हरी not a dual — so not प्रगृह्य", {"form": "harī"}, kind="counter")),
    "1.1.12": (_c("अमू — from अदस्, and not as a dual",
                  {"form": "amū", "stem": "adas"}),),
    "1.1.13": (_c("शे", {"form": "śe"}),),
    "1.1.14": (_c("आ — a one-vowel particle",
                  {"form": "ā", "nipata": True}),
               _c("आङ् is excepted — not प्रगृह्य",
                  {"form": "ā", "nipata": True, "ang": True},
                  kind="counter")),
    "1.1.15": (_c("अहो — a particle in ओ",
                  {"form": "aho", "nipata": True}),),
    "1.1.16": (_c("वायो इति — a vocative before इति",
                  {"form": "vāyo", "sambuddhi": True, "before_iti": True}),
               _c("in the वेद the option does not arise",
                  {"form": "vāyo", "sambuddhi": True, "before_iti": True,
                   "arsa": True}, kind="counter")),
    "1.1.17": (_c("उञ् before इति", {"form": "u", "before_iti": True}),),
    "1.1.18": (_c("ऊँ", {"form": "ū̐"}),),
    "1.1.19": (_c("अमी — ī or ū in a locative sense",
                  {"form": "amī", "saptami_artha": True}),),

    # --- 1.1.20 to 1.1.27 -------------------------------------------------
    "1.1.20": (_c("डुदाञ् is घु", {"root": "ḍudāñ"}),
               _c("धेट् is घु", {"root": "dheṭ"}),
               _c("दाप् is excepted — not घु", {"root": "dāp"}, kind="counter")),
    "1.1.21": (_c("first and last of five", {"length": 5, "index": 0}),
               _c("the middle of five", {"length": 5, "index": 2})),
    "1.1.22": (_c("तरप् is घ", {"affix": "tarap"}),
               _c("तमप् is घ", {"affix": "tamap"}),
               _c("ण्वुल् is not घ", {"affix": "ṇvul"}, kind="counter")),
    "1.1.23": (_c("बहु is a numeral", {"word": "bahu"}),
               _c("गण is a numeral", {"word": "gaṇa"}),
               _c("वृक्ष is not संख्या", {"word": "vṛkṣa"}, kind="counter")),
    "1.1.24": (_c("पञ्चन् — a ṣ- or n-final numeral", {"word": "pañcan"}),
               _c("सप्तन् — an न्-final numeral", {"word": "saptan"}),
               _c("द्वि is not षट्", {"word": "dvi"}, kind="counter")),
    "1.1.25": (_c("डति-final", {"word": "ḍati"}),),
    "1.1.26": (_c("क्त is निष्ठा", {"affix": "kta"}),
               _c("क्तवतु is निष्ठा", {"affix": "ktavatu"}),
               _c("क्त्वा is not निष्ठा", {"affix": "ktvā"}, kind="counter")),
    "1.1.27": (_c("सर्व", {"word": "sarva"}),
               _c("विश्व", {"word": "viśva"}),
               _c("वृक्ष is not सर्वनामन्", {"word": "vṛkṣa"}, kind="counter")),

    # --- 1.1.28 to 1.1.36: सर्वनामन् and its eight qualifiers -------------
    "1.1.28": (_c("उत्तरपूर्वस्यै — a bahuvrīhi of directions",
                  {"word": "pūrva", "samasa": "diksamāsa-bahuvrīhi",
                   "before_jas": True}),),
    "1.1.29": (_c("in a bahuvrīhi the name goes",
                  {"word": "sarva", "samasa": "bahuvrīhi"}),),
    "1.1.30": (_c("in a तृतीयासमास, not सर्वनामन्",
                  {"word": "sarva", "samasa": "tṛtīyā-tatpuruṣa"},
                  kind="counter"),),
    "1.1.31": (_c("in a द्वन्द्व, not सर्वनामन्",
                  {"word": "sarva", "samasa": "dvandva"}),),
    "1.1.32": (_c("before जस्, optionally",
                  {"word": "sarva", "samasa": "dvandva",
                   "before_jas": True}),),
    "1.1.33": (_c("प्रथमे — before जस्, optionally",
                  {"word": "prathama", "before_jas": True}),
               _c("चरमे — before जस्, optionally",
                  {"word": "carama", "before_jas": True})),
    "1.1.34": (_c("पूर्वे — a settled sense, and no proper name",
                  {"word": "pūrva", "before_jas": True,
                   "vyavastha": True}),
               _c("a proper name is out",
                  {"word": "pūrva", "before_jas": True,
                   "vyavastha": True, "is_name": True}, kind="counter")),
    "1.1.35": (_c("स्वे — not meaning kin or wealth",
                  {"word": "sva", "before_jas": True}),
               _c("स्वाः meaning kinsmen is out",
                  {"word": "sva", "before_jas": True,
                   "means_kin_or_wealth": True}, kind="counter")),
    "1.1.36": (_c("अन्तरे — an outer garment or an outside connection",
                  {"word": "antara", "before_jas": True,
                   "bahiryoga_or_upasamvyana": True}),),

    # --- 1.1.37 to 1.1.41: अव्यय -----------------------------------------
    "1.1.37": (_c("स्वर् — a स्वरादि word", {"form": "svar"}),
               _c("च — a particle", {"form": "ca", "nipata": True})),
    "1.1.38": (_c("तत्र — a taddhita-final with no full paradigm",
                  {"form": "tatra", "taddhita_final": True,
                   "sarvavibhakti": False}),
               _c("औपगवः has a full paradigm",
                  {"form": "aupagava", "taddhita_final": True},
                  kind="counter")),
    "1.1.39": (_c("दर्शम् — a कृत् ending in म्",
                  {"form": "darśam", "krt_final": True,
                   "krt_affix": "ṇamul"}),),
    "1.1.40": (_c("क्त्वा, तोसुन्, कसुन्",
                  {"form": "kṛtvā", "krt_final": True,
                   "krt_affix": "ktvā"}),),
    "1.1.41": (_c("उपकुम्भम् — an avyayībhāva",
                  {"form": "upakumbham", "avyayibhava": True}),),

    # --- 1.1.42 to 1.1.55: the substitution machinery ---------------------
    "1.1.42": (_c("शि", {"affix": "śi"}),),
    "1.1.43": (_c("सु — one of the first five",
                  {"affix": "su"}),
               _c("in a neuter, not सर्वनामस्थान",
                  {"affix": "su", "napumsaka": True}, kind="counter")),
    "1.1.44": (_c("न वेति विभाषा — an option", {"word": "vā"}),),
    "1.1.45": (_c("य् → इ, as in इष्टम्", {"before": "y", "after": "i"}),
               _c("व् → उ, as in उप्तम्", {"before": "v", "after": "u"}),
               _c("र् → ऋ, as in गृहीतम्", {"before": "r", "after": "ṛ"})),
    "1.1.46": (_c("a टित् augment goes in front", {"its": "ṭ"}),
               _c("a कित् augment at the end", {"its": "k"}),
               _c("a मित् augment after the last vowel", {"its": "m"})),
    "1.1.47": (_c("मित् — after the last vowel", {"its": "m"}),),
    "1.1.48": (_c("ए shortens to इ", {"vowel": "e"}),
               _c("ओ shortens to उ", {"vowel": "o"}),
               _c("ऐ likewise to इ", {"vowel": "ai"})),
    "1.1.49": (_c("1.1.52 अलोऽन्त्यस्य — two sixth-case words",
                  {"sutra_id": "1.1.52"}),),
    "1.1.50": (_c("nearest to इ among these",
                  {"sthanin": "i", "candidates": ["a", "u", "ī"]}),
               _c("nearest to क्",
                  {"sthanin": "k", "candidates": ["c", "g", "p"]})),
    "1.1.51": (_c("ऋ replaced by अ takes र्",
                  {"sthanin": "ṛ", "substitute": "a"}),
               _c("ऌ by the vārttika",
                  {"sthanin": "ḷ", "substitute": "a", "varttika": True})),
    "1.1.52": (_c("the last sound of अग्नि",
                  {"text": "agni", "substitute": "e"}),),
    "1.1.53": (_c("आनङ् — ṅit, so the last sound only",
                  {"adesa.form": "āna", "adesa.its": ["ṅ"]}),),
    "1.1.54": (_c("आदेः परस्य — the first sound of what follows",
                  {"sutra_id": "6.1.87", "adesa.form": "e",
                   "adesa.its": []}),),
    "1.1.55": (_c("अनेकाल् — the whole is replaced",
                  {"adesa.form": "atra", "adesa.its": []}),),
    "1.1.56": (_c("an ordinary operation — sthānivat holds",
                  {"al_vidhi": False, "operation": "guṇa"}),
               _c("an अल्विधि is not inherited",
                  {"al_vidhi": True, "operation": "dīrgha"})),
    "1.1.57": (_c("a vowel substitute, in an अल्विधि on what precedes",
                  {"al_vidhi": True, "sthanin_is_vowel": True,
                   "purva_vidhi": True, "caused_by_following": True}),),
    "1.1.58": (_c("reduplication is excluded",
                  {"al_vidhi": True, "sthanin_is_vowel": True,
                   "purva_vidhi": True, "operation": "dvirvacana"},
                  kind="counter"),),
    "1.1.59": (_c("unless the reduplication is caused by a vowel",
                  {"al_vidhi": True, "sthanin_is_vowel": True,
                   "purva_vidhi": True, "operation": "dvirvacana",
                   "dvirvacana_caused_by_vowel": True}),),

    # --- 1.1.60 to 1.1.75 -------------------------------------------------
    "1.1.60": (_c("nothing there — that absence is लोप", {}),
               _c("something present is not लोप", {"present": "a"},
                  kind="counter")),
    "1.1.61": ((_c("the four lu-elisions", {})),),
    "1.1.62": (_c("an ordinary lopa — the operation holds",
                  {"elision": "lopa"}),),
    "1.1.63": (_c("a lu-elision on the अङ्ग refuses it",
                  {"elision": "luk", "anga": True}),),
    "1.1.64": (_c("the टि of अग्नि", {"text": "agni"}),
               _c("the टि of राजन्", {"text": "rājan"})),
    "1.1.65": (_c("the उपधा of भिद्", {"text": "bhid"}),
               _c("the उपधा of राजन्", {"text": "rājan"})),
    "1.1.66": (_c("1.1.66's seventh-case reading", {"sutra_id": "1.1.66"}),
               _c("1.3.17 नेर्विशः", {"sutra_id": "1.3.17"})),
    "1.1.67": (_c("1.1.67's fifth-case reading", {"sutra_id": "1.1.67"}),),
    "1.1.68": (_c("अच् — the term denotes its own form",
                  {"term": "aC"}),
               _c("इक् — the term denotes its own form", {"term": "iK"})),
    "1.1.69": (_c("अण् stands for its सवर्णs", {"term": "aṇ"}),
               _c("इक् stands for its सवर्णs", {"term": "iK"})),
    "1.1.70": (_c("a tapara takes its own measure", {"term": "at"}),),
    "1.1.71": (_c("अच्", {"name": "aC"}),
               _c("हल्", {"name": "haL"}),
               _c("इक्", {"name": "iK"})),
    "1.1.72": (_c("अच् reaches a word ending in one",
                  {"term": "aC", "word": "agni"}),
               _c("a word not ending in it is not reached",
                  {"term": "aC", "word": "vāc"}, kind="counter")),
    "1.1.73": (_c("आमलक — a vṛddhi in the first syllable",
                  {"word": "āmalaka"}),),
    "1.1.74": (_c("त्यद् and the rest count as vṛddha",
                  {"word": "tyad"}),),
    "1.1.75": (_c("गोनर्द — first vowel an एङ्, an eastern place",
                  {"word": "gonarda", "praci_desa": True}),
               _c("आहिच्छत्र begins with आ, not ए or ओ",
                  {"word": "āhicchatra", "praci_desa": True},
                  kind="counter")),

    # --- 1.2.27 to 1.2.46 -------------------------------------------------
    "1.2.27": (_c("अ — one mātrā", {"vowel": "a"}),
               _c("आ — two", {"vowel": "ā"}),
               _c("आ३ — three", {"vowel": "ā3"})),
    "1.2.28": (_c("what a duration replaces", {"sthanin": "a"}),),
    "1.2.29": (_c("a high vowel", {"marked": "\\u0301"}),
               _c("unmarked", {"marked": ""})),
    "1.2.30": (_c("a low vowel", {"marked": "\\\\"}),),
    "1.2.31": (_c("udātta and anudātta together",
                  {"first": "udātta", "second": "anudātta"}),),
    "1.2.32": (_c("the svarita of अ", {"vowel": "a"}),
               _c("of आ", {"vowel": "ā"})),
    "1.2.41": (_c("a one-sound affix", {"affix": "s"}),
               _c("a longer affix is not अपृक्त", {"affix": "tas"}, kind="counter")),
    "1.2.42": (_c("a tatpuruṣa with one referent",
                  {"tatpurusa": True, "samanadhikarana": True}),
               _c("without sameness of reference, no कर्मधारय",
                  {"tatpurusa": True}, kind="counter")),
    "1.2.43": (_c("1.2.43's own first-case word", {"sutra_id": "1.2.43"}),
               _c("2.2.8 षष्ठी", {"sutra_id": "2.2.8"})),
    "1.2.44": (_c("one that stands in a single case",
                  {"sutra_id": "1.2.43", "ekavibhakti": True}),),
    "1.2.45": (_c("वृक्ष — meaningful and neither root nor affix",
                  {"form": "vṛkṣa", "arthavat": True}),
               _c("a root is not प्रातिपदिक",
                  {"form": "bhū", "arthavat": True, "dhatu": True},
                  kind="counter")),
    "1.2.46": (_c("a kṛt-final", {"form": "kartṛ", "krdanta": True}),
               _c("a compound", {"form": "rājapuruṣa", "samasa": True}),
               _c("a phrase is not प्रातिपदिक",
                  {"form": "rājñaḥ puruṣaḥ", "vakya": True},
                  kind="counter")),

    # --- 1.2.47 to 1.2.57 -------------------------------------------------
    "1.2.47": (_c("अतिरै → अतिरि",
                  {"stem": "atirai", "napumsaka": True}),
               _c("ग्रामणी is masculine — no shortening",
                  {"stem": "grāmaṇī"}, kind="counter")),
    "1.2.48": (_c("चित्रगू → चित्रगु",
                  {"stem": "citragū", "upasarjana": True,
                   "ends_in_go": True}),
               _c("अतिखट्वा → अतिखट्व",
                  {"stem": "atikhaṭvā", "upasarjana": True,
                   "stri_pratyaya": True}),
               _c("राजकुमारी is the head — no shortening",
                  {"stem": "rājakumārī", "stri_pratyaya": True},
                  kind="counter")),
    "1.2.49": (_c("आमलकी → आमलक",
                  {"stem": "āmalakī", "upasarjana": True,
                   "stri_pratyaya": True, "taddhita_luk": True}),),
    "1.2.50": (_c("गोणी → गोणि",
                  {"stem": "goṇī", "upasarjana": True,
                   "stri_pratyaya": True, "taddhita_luk": True,
                   "ends_in_goni": True}),),
    "1.2.51": (_c("पञ्चालाः — masculine plural carried over",
                  {"gender": "puṃs", "number": 3}),
               _c("under लुक्, gender and number are not kept",
                  {"gender": "puṃs", "number": 3, "lup": False},
                  kind="counter")),
    "1.2.52": (_c("the qualifiers follow the elided word",
                  {"gender": "puṃs", "number": 3, "qualifier": True}),
               _c("the class-word does not follow",
                  {"gender": "puṃs", "number": 3, "qualifier": True,
                   "jati": True})),
    "1.2.53": (_c("युक्तवद्भाव needs no teaching",
                  {"topic": "yuktadbhāva"}),),
    "1.2.54": (_c("the लुप् rule is as unnecessary", {"topic": "lup"}),),
    "1.2.55": (_c("the argument for reading it so",
                  {"topic": "the-argument-for-it"}),),
    "1.2.56": (_c("how a compound shares out its meaning need not be stated",
                  {"topic": "how-a-compound-divides-its-meaning"}),),
    "1.2.57": (_c("'today' and उपसर्जन need no defining",
                  {"topic":
                   "the-definitions-of-today-and-of-upasarjana"}),),

    # --- 1.2.58 to 1.2.63: number ----------------------------------------
    "1.2.58": (_c("संपन्ना व्रीहयः — a class-name for one",
                  {"counted": 1, "jati": True}),
               _c("with a numeral, no plural for one",
                  {"counted": 1, "jati": True, "with_numeral": True})),
    "1.2.59": (_c("अहं / वयम् — अस्मद् for one",
                  {"counted": 1, "asmad": True}),
               _c("आवाम् / वयम् — for two",
                  {"counted": 2, "asmad": True})),
    "1.2.60": (_c("पूर्वाः फल्गुन्यः — the stars",
                  {"counted": 2, "star": "phalgunī", "nakshatra": True}),
               _c("फल्गुन्यौ माणविके are girls, not stars",
                  {"counted": 2, "star": "phalgunī"}, kind="counter")),
    "1.2.61": (_c("पुनर्वसुर् नक्षत्रम् — in the Veda",
                  {"counted": 2, "star": "punarvasū", "nakshatra": True,
                   "chandas": True}),),
    "1.2.62": (_c("विशाखा नक्षत्रम् — in the Veda",
                  {"counted": 2, "star": "viśākhā", "nakshatra": True,
                   "chandas": True}),),
    "1.2.63": (_c("तिष्यपुनर्वसू — one star and two",
                  {"counted": 3, "nakshatra": True,
                   "dvandva_of": ["tiṣya", "punarvasū"]}),),

    # --- 1.2.64 to 1.2.73: एकशेष -----------------------------------------
    "1.2.64": (_c("वृक्षश्च वृक्षश्च → वृक्षौ",
                  {"words": ["vṛkṣa", "vṛkṣa"]}),
               _c("प्लक्षन्यग्रोधाः are different trees — both stand",
                  {"words": ["plakṣa", "nyagrodha"]}, kind="counter")),
    "1.2.65": (_c("गार्ग्य and गार्ग्यायण → गार्ग्यौ",
                  {"words": ["gārgya:vṛddha", "gārgya:yuvan"]}),),
    "1.2.66": (_c("गार्गी and गार्ग्यायण → गार्ग्यौ",
                  {"words": ["gārgya:vṛddha:strī", "gārgya:yuvan"]}),),
    "1.2.67": (_c("ब्राह्मण and ब्राह्मणी → ब्राह्मणौ",
                  {"words": ["brāhmaṇa", "brāhmaṇa:strī"]}),),
    "1.2.68": (_c("भ्रातृ and स्वसृ → भ्रातरौ",
                  {"words": ["bhrātṛ", "svasṛ"]}),
               _c("पुत्र and दुहितृ → पुत्रौ",
                  {"words": ["putra", "duhitṛ"]})),
    "1.2.69": (_c("शुक्ल m, f and n → शुक्लम्",
                  {"words": ["śukla", "śukla:strī", "śukla:napuṃsaka"]}),),
    "1.2.70": (_c("माता and पिता → पितरौ, optionally",
                  {"words": ["pitṛ", "mātṛ"]}),),
    "1.2.71": (_c("श्वशुर and श्वश्रू → श्वशुरौ, optionally",
                  {"words": ["śvaśura", "śvaśrū"]}),),
    "1.2.72": (_c("स and देवदत्त → तौ", {"words": ["tad", "devadatta"]}),
               _c("स and य → यौ", {"words": ["tad", "yad"]}),
               _c("य and क → कौ", {"words": ["yad", "kim"]})),
    "1.2.73": (_c("गाव इमाः — a herd of cattle",
                  {"words": ["go:strī:herd", "go:herd"]}),),

    # --- 1.3.1 to 1.3.13 --------------------------------------------------
    "1.3.1": (_c("भू is a root", {"form": "bhū"}),
              _c("डुकृञ् is a root", {"form": "ḍukṛñ"}),
              _c("राम is not a धातु", {"form": "rāma"}, kind="counter")),
    "1.3.2": (_c("एध — the anunāsika vowel is an it",
                 {"form": "edha̐", "context.dhatu": True}),),
    "1.3.3": (_c("ṣūṅ — the final consonant is an it",
                 {"form": "ṣūṅ", "context.dhatu": True}),),
    "1.3.4": (_c("in a विभक्ति those finals are not इत्",
                 {"form": "tas", "context.vibhakti": True},
                 kind="counter"),),
    "1.3.5": (_c("डुकृञ् — the opening डु",
                 {"form": "ḍukṛñ", "context.dhatu": True}),),
    "1.3.6": (_c("an affix's initial ष्",
                 {"form": "ṣvun", "context.pratyaya": True}),),
    "1.3.7": (_c("an affix's initial च, छ, ज, झ, ञ, ट…",
                 {"form": "ṭāp", "context.pratyaya": True}),),
    "1.3.8": (_c("क्त्वा — the initial क्",
                 {"form": "ktvā", "context.pratyaya": True}),
              _c("on a तद्धित those initials are not इत्",
                 {"form": "ka", "context.pratyaya": True,
                  "context.taddhita": True}, kind="counter")),
    "1.3.9": (_c("डुकृञ् → कृ, both marks gone",
                 {"form": "ḍukṛñ", "dhatu": True}),
              _c("ṣūṅ → सू", {"form": "ṣūṅ", "dhatu": True})),
    "1.3.10": (_c("four against four — they pair off",
                  {"uddesin": ["tūdī", "śalātura", "varmatī", "kūcavāra"],
                   "anudesin": ["ḍhak", "chaṇ", "ḍhañ", "yak"]}),
               _c("five senses against three words do not pair",
                  {"uddesin": ["lakṣaṇa", "itthaṃbhūta", "ākhyāna",
                               "bhāga", "vīpsā"],
                   "anudesin": ["prati", "pari", "anu"]}, kind="counter")),
    "1.3.11": (_c("6.4.1 अङ्गस्य", {"sutra_id": "6.4.1"}),
               _c("4.1.1 ङ्याप्प्रातिपदिकात्", {"sutra_id": "4.1.1"}),
               _c("1.1.1 is no heading", {"sutra_id": "1.1.1"},
                  kind="counter")),
    "1.3.13": (_c("क्रियते कटः — the passive",
                  {"root": "kṛ", "bhava_or_karman": True}),
               _c("ग्लायते भवता — the impersonal",
                  {"root": "glai", "bhava_or_karman": True})),

    # --- the prohibitions of 1.3, which fire by *not* applying ----------
    "1.3.15": (_c("व्यतिगच्छन्ति — गति, so no middle endings",
                  {"root": "gam", "given": ["karmavyatihāra"]},
                  kind="counter"),
               _c("व्यतिघ्नन्ति — हिंसा, so no middle endings",
                  {"root": "han", "given": ["karmavyatihāra"]},
                  kind="counter")),
    "1.3.16": (_c("इतरेतरस्य व्यतिलुनन्ति",
                  {"root": "lū", "given": ["karmavyatihāra"],
                   "upapada": "itaretara"}, kind="counter"),),
    "1.3.58": (_c("पुत्रम् अनुजिज्ञासति",
                  {"root": "jñā", "upasargas": ["anu"], "affixes": ["san"]},
                  kind="counter"),),
    "1.3.59": (_c("प्रतिशुश्रूषति",
                  {"root": "śru", "upasargas": ["prati"],
                   "affixes": ["san"]}, kind="counter"),),
    "1.3.62": (_c("आचिक्रंसते — the desiderative carries the cause",
                  {"root": "kram", "upasargas": ["ā"], "sense": "udgamana",
                   "affixes": ["san"]}),
               _c("शिशत्सति does not — the cause is absent",
                  {"root": "śad", "affixes": ["san"]}, kind="counter"),
               _c("मुमूर्षति does not either — no cause to inherit", {"root": "mṛ", "affixes": ["san"]},
                  kind="counter")),
    "1.3.63": (_c("ईक्षांचक्रे — not codified",
                  {"root": "kṛ", "affixes": ["san"]}, kind="counter"),),
    "1.3.78": (_c("याति — nothing else reaches it", {"root": "yā"}),
               _c("भवति — nothing else reaches it", {"root": "bhū"})),
    "1.3.89": (_c("रोचयते — the prohibition leaves 1.3.74 standing",
                  {"root": "ruc", "affixes": ["ṇic"],
                   "given": ["kartrabhiprāya-kriyāphala"]}, kind="counter"),),

    # --- 1.4.1 to 1.4.22 --------------------------------------------------
    "1.4.1": (_c("लघु against गुरु — one name only",
                 {"candidates": ["1.4.10", "1.4.11"]}),
              _c("पद against भ", {"candidates": ["1.4.17", "1.4.18"]})),
    "1.4.2": (_c("7.3.101 against 7.3.103 — the later is done",
                 {"candidates": ["7.3.101", "7.3.103"]}),),
    "1.4.3": (_c("कुमारी", {"word": "kumārī"}),
              _c("ब्रह्मबन्धू", {"word": "brahmabandhū"}),
              _c("ग्रामणी does not mean a woman — so not नदी",
                 {"word": "grāmaṇī", "stri_akhya": False})),
    "1.4.4": (_c("श्री — an इयङ् place, so no नदी",
                 {"word": "śrī", "iyan_uvan_place": True}),
              _c("भ्रू — an उवङ् place, so no नदी",
                 {"word": "bhrū", "iyan_uvan_place": True}),
              _c("स्त्री is excepted by name",
                 {"word": "strī", "iyan_uvan_place": True,
                  "is_stri": True}, kind="counter")),
    "1.4.5": (_c("before आम्, optionally",
                 {"word": "śrī", "iyan_uvan_place": True,
                  "before_am": True}),),
    "1.4.6": (_c("मति before a ṅit affix, optionally",
                 {"word": "mati", "before_ngit": True}),),
    "1.4.7": (_c("अग्नि", {"word": "agni"}),
              _c("धेनु", {"word": "dhenu"}),
              _c("सखि is excepted — not घि", {"word": "sakhi"})),
    "1.4.8": (_c("पति inside a compound",
                 {"word": "pati", "in_compound": True}),
              _c("पति on its own is not घि", {"word": "pati"})),
    "1.4.9": (_c("पति with a genitive, in the Veda",
                 {"word": "pati", "chandas_with_genitive": True}),),
    "1.4.10": (_c("इ — a short vowel", {"vowel": "i"}),
               _c("अ — a short vowel", {"vowel": "a"})),
    "1.4.11": (_c("इ before a conjunct — शिक्षा",
                  {"vowel": "i", "before_conjunct": True}),),
    "1.4.12": (_c("ई — long, so heavy", {"vowel": "ī"}),
               _c("ऐ — long, so heavy", {"vowel": "ai"})),
    "1.4.13": (_c("कृ before तृच्",
                  {"base": "kṛ", "affix": "tṛc", "prescribed_from": "kṛ"}),
               _c("स्त्री इयती — merely following is not enough",
                  {"base": "strī", "affix": "iyatī"})),
    "1.4.14": (_c("ब्राह्मणाः — a sup-final",
                  {"word": "brāhmaṇāḥ", "ends_in_sup_or_tin": True}),),
    "1.4.15": (_c("a न-final before क्य",
                  {"word": "rājan", "before_kya": True}),),
    "1.4.16": (_c("before a सित् affix",
                  {"word": "rājan", "before_sit": True}),),
    "1.4.17": (_c("राजभ्याम्", {"word": "rājan", "sup_affix": "bhyām"}),
               _c("राजानौ is सर्वनामस्थान — so not पद",
                  {"word": "rājan", "sup_affix": "au",
                   "sarvanamasthana": True}, kind="counter")),
    "1.4.18": (_c("गार्ग्यः — a य-initial ending",
                  {"word": "gārga", "sup_affix": "ya"}),
               _c("दाक्षिः — a vowel-initial one",
                  {"word": "dākṣa", "sup_affix": "i"})),
    "1.4.19": (_c("यशस्वी — a स-final before a matvartha",
                  {"word": "yaśas", "matvartha": True}),
               _c("तक्षवान् is neither त- nor स-final",
                  {"word": "takṣan", "matvartha": True}, kind="counter")),
    "1.4.20": (_c("the अयस्मय group, in the Veda",
                  {"word": "ayasmaya", "ayasmayadi": True,
                   "chandas": True}),),
    "1.4.21": (_c("many — the plural", {"count": 5}),),
    "1.4.22": (_c("two — the dual", {"count": 2}),
               _c("one — the singular", {"count": 1})),
    "1.4.23": (_c("nothing asserted, so no name at all", {}),),

    # --- 1.4.56 to 1.4.110 ------------------------------------------------
    "1.4.56": (_c("च — a particle", {"form": "ca"}),),
    "1.4.60": (_c("प्र with a verb — गति as well as उपसर्ग",
                  {"form": "pra", "kriya_yoga": True}),),
    "1.4.80": (_c("प्र before the root", {"form": "pra",
                                          "kriya_yoga": True}),),
    "1.4.81": (_c("in the Veda it may follow",
                  {"form": "pra", "kriya_yoga": True, "chandas": True}),),
    "1.4.82": (_c("in the वेद they may stand apart",
                  {"form": "pra", "kriya_yoga": True, "chandas": True}),),
    "1.4.83": (_c("अनु without a verb", {"form": "anu",
                                         "sense": "lakṣaṇa"}),),
    "1.4.99": (_c("तिप्", {"ending": "tip"}),
               _c("तस्", {"ending": "tas"}),
               _c("मिप्", {"ending": "mip"})),
    "1.4.100": (_c("त", {"ending": "ta"}),
                _c("महिङ्", {"ending": "mahiṅ"})),
    "1.4.101": (_c("झि — प्रथम, plural", {"ending": "jhi"}),
                _c("सिप् — मध्यम, singular", {"ending": "sip"})),
    "1.4.102": (_c("वस् — dual", {"ending": "vas"}),),
    "1.4.103": (_c("सुप् endings, the same", {"ending": "tip"}),),
    "1.4.104": (_c("both sets are विभक्ति", {"ending": "ta"}),),
    "1.4.105": (_c("त्वं पचसि — and पचसि alone",
                   {"upapada": "yuṣmad"}),),
    "1.4.106": (_c("एहि मन्ये भोक्ष्यसे — the main verb",
                   {"upapada": "manya", "prahasa": True}),
                _c("मन्ये itself takes the change",
                   {"upapada": "manya", "prahasa": True,
                    "is_manyati": True})),
    "1.4.107": (_c("अहं पचामि", {"upapada": "asmad"}),),
    "1.4.108": (_c("देवदत्तः पचति — the remainder", {}),),
    "1.4.109": (_c("दध्यत्र — half a mātrā apart",
                   {"gap_matras": 0.5}),),
    "1.4.110": (_c("दधिँ — a stop", {"stopped": True}),),

    # --- 1.2.18 to 1.2.22: the कित्त्व denials -----------------------------
    # A denial assigns nothing, so the derivation skips it; what shows these
    # is the form that *loses* its kit-ness.
    "1.2.18": (_c("देवित्वा — a seṭ क्त्वा loses it",
                  {"root": "div", "affix": "ktvā", "given": ["seṭ"]}),
               _c("कृत्वा is अनिट् and keeps its कित् by 1.3.8",
                  {"root": "kṛ", "affix": "ktvā"}, kind="counter")),
    "1.2.19": (_c("शयितः — a seṭ निष्ठा after शीङ्",
                  {"root": "śī", "affix": "niṣṭhā", "given": ["seṭ"]}),
               _c("स्विन्नः is अनिट् and keeps its कित् by 1.3.8",
                  {"root": "svid", "affix": "niṣṭhā"}, kind="counter")),
    "1.2.20": (_c("मर्षितः — मृष् in forbearance",
                  {"root": "mṛṣ", "affix": "niṣṭhā", "sense": "titikṣā",
                   "given": ["seṭ"]}),),
    "1.2.22": (_c("पवितः — after पूङ्",
                  {"root": "pū", "affix": "niṣṭhā", "given": ["seṭ"]}),),

    # --- 1.2.33 to 1.2.40: how the accents are recited --------------------
    "1.2.33": (_c("calling from afar — one tone",
                  {"accents": ["udātta", "anudātta", "svarita"],
                   "setting": "dūrāt-sambuddhi"}),
               _c("near at hand, the three tones stand",
                  {"accents": ["udātta", "anudātta", "svarita"]},
                  kind="counter")),
    "1.2.34": (_c("in the rite — one tone",
                  {"accents": ["udātta", "anudātta", "svarita"],
                   "setting": "yajña"}),
               _c("in a सामन्, not एकश्रुति",
                  {"accents": ["udātta", "anudātta", "svarita"],
                   "setting": "yajña", "saman": True},
                  kind="counter")),
    "1.2.35": (_c("the वषट् — higher still",
                  {"accents": ["udātta"], "setting": "yajña",
                   "vasatkara": True}),),
    "1.2.36": (_c("in the Veda — optionally",
                  {"accents": ["udātta", "anudātta"],
                   "setting": "chandas"}),),
    "1.2.37": (_c("the subrahmaṇyā keeps its accents, svarita → udātta",
                  {"accents": ["udātta", "svarita", "anudātta"],
                   "setting": "subrahmaṇyā"}),),
    "1.2.38": (_c("देव and ब्रह्मन् go the other way",
                  {"accents": ["svarita", "udātta"],
                   "setting": "subrahmaṇyā",
                   "words": ["deva", "x"]}),),
    "1.2.39": (_c("after a svarita, in continuous speech",
                  {"accents": ["udātta", "svarita", "anudātta", "anudātta"],
                   "samhita": True}),
               _c("word by word, each keeps its own tone",
                  {"accents": ["udātta", "svarita", "anudātta", "anudātta"]},
                  kind="counter")),
    "1.2.40": (_c("an anudātta before an udātta — सन्नतर",
                  {"accents": ["anudātta", "udātta"]}),
               _c("before a स्वरित, the same",
                  {"accents": ["anudātta", "svarita"]})),

    # --- the paribhāṣās beyond adhyāya 1 ----------------------------------
    "2.1.1": (_c("connected — the rule applies", {"connected": True}),
              _c("unconnected — no rule about words reaches them", {"connected": False}),
              _c("a वर्णविधि is untouched",
                 {"connected": False, "padavidhi": False})),
    "3.1.94": (_c("क against ण्वुल् — optional",
                  {"utsarga": "3.1.133", "apavada": "3.1.135",
                   "utsarga_affix": "ṇvul", "apavada_affix": "ka"}),
               _c("अण् and क are alike — the exception wins outright",
                  {"utsarga": "3.2.1", "apavada": "3.2.3",
                   "utsarga_affix": "aṇ", "apavada_affix": "ka"})),
    "6.1.85": (_c("counts as both ends", {}),
               _c("for a वर्णविधि it is not अन्तादिवत्", {"varna_vidhi": True})),
    "6.1.86": (_c("षत्व — asiddha", {"operation": "ṣatva"}),
               _c("तुक् — asiddha", {"operation": "tuk"}),
               _c("गुण sees it — only षत्व and तुक् find it असिद्ध", {"operation": "guṇa"})),
    "6.4.22": (_c("same locus — asiddhavat",
                  {"done": "6.4.101", "to": "6.4.105",
                   "same_locus": True}),
               _c("different loci — so not असिद्धवत्",
                  {"done": "6.4.101", "to": "6.4.105",
                   "same_locus": False})),
    "8.2.1": (_c("the tripādī, to what precedes",
                 {"done": "8.2.31", "to": "6.1.87"}),
              _c("within the त्रिपादी itself",
                 {"done": "8.4.40", "to": "8.2.31"}),
              _c("an अपवाद is still seen",
                 {"done": "8.2.31", "to": "6.1.87",
                  "done_is_apavada": True})),
    "8.2.2": (_c("नलोप in a sup operation",
                 {"done": "8.2.7", "to": "7.1.9", "done_is_nalopa": True,
                  "operation": "sup"}),
              _c("in a sandhi the न्-loss does count",
                 {"done": "8.2.7", "to": "6.1.87", "done_is_nalopa": True,
                  "operation": "sandhi"})),
    "8.2.3": (_c("मु before the नाभाव",
                 {"done": "8.2.80", "to": "7.3.120", "done_is_mu": True,
                  "applying_nabhava": True}),),
    # --- 2.1.2 to 2.1.21 : the compound section opens ----------------------
    "2.1.2": (
        _c("kuṇḍenāṭan — accented as one",
           {"preceding_is_sup": True, "following_is_amantrita": True,
            "operation": "svara"},
           note="6.1.198 makes the vocative initially udātta, and the "
                "atideśa carries that back over the noun before it."),
        _c("kūpe siñcan — ṣatva is not accent",
           {"preceding_is_sup": True, "following_is_amantrita": True,
            "operation": "ṣatva"},
           note="स्वर इति किम्? The atideśa reaches accent and nothing "
                "else, so 8.3.59 does not see a limb here. Worked, not a "
                "counter: refusing is what the sūtra's स्वरे does."),
        _c("gehe gārgyaḥ — nothing is being addressed",
           {"preceding_is_sup": True, "following_is_amantrita": False},
           note="आमन्त्रिते इति किम्? The rule answers, and its answer is "
                "no."),
    ),
    "2.1.3": (
        _c("2.1.6 — inside the range", {"sutra_id": "2.1.6"},
           note="Two names at once, समास and अव्ययीभाव, which is what the "
                "प्राक् phrasing is for: प्राग्वचनं संज्ञासमावेशार्थम्."),
        _c("2.1.24 — samāsa but not avyayībhāva",
           {"sutra_id": "2.1.24"},
           note="Past 2.1.21, so the inner heading has run out and only "
                "the outer one reaches."),
        _c("1.4.1 — before the range starts", {"sutra_id": "1.4.1"},
           kind="counter",
           note="No compound name at all; the heading has not opened."),
    ),
    "2.1.4": (
        _c("kaṣṭaśritaḥ — a noun with a noun", {"second_is": "sup"}),
        _c("anuvyacalat — with a finite verb, in Vedic",
           {"second_is": "tiṅ", "chandas": True},
           note="The yoga split: सहग्रहणं योगविभागार्थम्, तिङापि सह यथा "
                "स्यात्. The Kaumudī confines it — स च छन्दस्येव."),
        _c("a finite verb outside Vedic", {"second_is": "tiṅ"},
           note="The split is granted and then confined — स च छन्दस्येव — "
                "so 2.1.4 answers here too, and its answer is no. Worked, "
                "for the same reason 2.1.2's ṣatva case is."),
    ),
    "2.1.5": (
        _c("upakumbham", {"first": "upa", "second": "kumbha",
                          "sense": "samīpa"},
           note="पूर्वपदार्थप्राधान्यम् — a nearness, not a pot."),
    ),
    "3.1.22": (
        _c("pāpacyate — cooking over and over", {"root": "pac"},
           note="क्रियासमभिहारे यङ्. The doubling that follows is 6.1.9's."),
        _c("jāgṛ is refused — it holds more than one vowel",
           {"root": "jāgṛ"},
           note="एकाच इति किम्? भृशं जागर्ति. The rule declines and says "
                "which condition failed."),
        _c("īkṣ is refused — it begins with a vowel", {"root": "īkṣ"},
           note="हलादेरिति किम्? भृशम् ईक्षते."),
    ),
    "3.1.32": (
        _c("lolūya is a root, though no list holds it",
           {"stem": "lolūya", "sanadyanta": True},
           note="सनाद्यन्ता धातवः. This is what makes the यङ् inside it a "
                "धात्वेकदेश, which 1.1.4 then needs."),
        _c("lū is a root, but not by this rule", {"stem": "lū"},
           kind="counter",
           note="1.3.1 भूवादयो धातवः answers first where it can. Two rules "
                "confer the one name, and this stem gets it from the "
                "list — 3.1.32 is for what the grammar builds."),
    ),
    "3.1.134": (
        _c("aC comes after lolūya", {"stem": "lolūya", "yananta": True},
           note="पचादिभ्योऽच्, and पचादि is an आकृतिगण — the Kāśikā puts "
                "the यङन्त stems in it by name."),
        _c("pac is in the gaṇa as it stands", {"stem": "paca"},
           note="One of the thirty-six the gaṇapāṭha lists."),
    ),
    "2.4.74": (
        _c("lolūya loses its yaṅ and keeps its doubling",
           {"stem": "lolūya"},
           note="यङोऽचि च. A luk takes the affix and leaves its work."),
    ),
    "6.4.77": (
        _c("loluv — uvaṅ reaches the ū because 1.1.4 stopped the guṇa",
           {"stem": "lolū", "ardhadhatuka": True, "dhatu_lopa": True},
           note="The whole of लोलुवः hangs on this."),
        _c("lū is untouched — nothing stopped the strengthening",
           {"stem": "lū", "ardhadhatuka": True}, kind="counter",
           note="इयङुवङ्भ्यां गुणवृद्धी भवतो विप्रतिषेधेन: लवनम्, लावकः."),
    ),
    "6.1.1": (
        _c("pāpacya — the whole of पच् copies", {"root": "pac"},
           note="एकाचो द्वे प्रथमस्य. पच् holds one vowel, so the opening "
                "one-vowelled stretch is the whole root."),
        _c("marīmṛjya — only मृज् copies, not मृज्य",
           {"root": "mṛj"},
           note="The stretch stops before the consonant that opens the "
                "next syllable, which is why 7.4.60 has a ज् to drop."),
    ),
    "6.1.2": (
        _c("aṭāṭya — the अ stays put and ट्य doubles behind it",
           {"root": "aṭ"},
           note="अजादेर्द्वितीयस्य. The only rule in this run that leaves "
                "anything standing in front of the copy."),
    ),
    "6.1.9": (
        _c("yāyajya — sacrificing over and over", {"root": "yaj"},
           note="सन्यङोः. यङ् is what occasions the doubling here."),
    ),
    "7.4.59": (
        _c("lolūya — लू shortens to लु before it is strengthened",
           {"root": "lū"},
           note="ह्रस्वः, and then 7.4.82 raises the short उ to ओ."),
    ),
    "7.4.60": (
        _c("marīmṛjya — the ज् of the copy is dropped", {"root": "mṛj"},
           note="हलादिः शेषः. Only the initial consonant of the copy "
                "survives."),
        _c("lolūya — nothing to drop here", {"root": "lū"}, kind="counter",
           note="लू ends in its vowel, so the rule has no work. A wrong "
                "split of the stem is invisible on a root like this."),
    ),
    "7.4.66": (
        _c("marīmṛjya — the ऋ of the copy becomes a plain अ",
           {"root": "mṛj"},
           note="उरत्. No र् comes from this rule; the री arrives next, "
                "by 7.4.90."),
    ),
    "7.4.82": (
        _c("lolūya — लु is raised to लो", {"root": "lū"},
           note="गुणो यङ्लुकोः, for a copy ending in इ, उ or ऋ."),
    ),
    "7.4.83": (
        _c("pāpacya — प is lengthened to पा", {"root": "pac"},
           note="दीर्घोऽकितः, where 7.4.82 has not already acted."),
    ),
    "7.4.90": (
        _c("varīvṛtya — the copy takes री", {"root": "vṛt"},
           note="रीगृदुपधस्य च, for a root with ऋ in it. कित्, so 1.1.46 "
                "puts the addition at the end of the copy."),
    ),
    "7.4.91": (
        _c("narnarti — the copy takes a bare र्",
           {"root": "nṛt", "yan_luk": True, "augment": "ruk"},
           note="रुग्रिकौ च लुकि, available only where यङ् has dropped."),
        _c("narinarti — the same copy with रि instead",
           {"root": "nṛt", "yan_luk": True, "augment": "rik"},
           note="One copy न, three additions: र्, रि, री."),
    ),
    "2.1.52": (
        _c("pañcapūlī is a dvigu", {"first": "pañcan", "second": "pūlī",
                                    "given": ["samānādhikaraṇa",
                                              "samāhāra"]},
           note="संख्यापूर्वो द्विगुः — 2.1.51 formed it and this names "
                "it. The name is what 2.1.23 extends तत्पुरुष to."),
        _c("pañcāmrāḥ is not — 2.1.50 formed it, not 2.1.51",
           {"first": "pañcan", "second": "āmra",
            "given": ["samānādhikaraṇa", "saṃjñā"]},
           kind="counter",
           note="A numeral first is not enough; the compound must be the "
                "one 2.1.51 makes."),
    ),
    "2.3.58": (
        _c("śatasya dīvyati", {"div": True},
           note="दिवस्तदर्थस्य — the sense व्यवहृ and पण् share."),
    ),
    "2.3.59": (
        _c("śatasya pratidīvyati", {"div": True, "upasarga": True},
           note="विभाषोपसर्गे — a preverb makes it a choice."),
    ),
    "2.3.60": (
        _c("a Brāhmaṇa usage takes the second",
           {"div": True, "brahmana": True},
           note="द्वितीया ब्राह्मणे."),
    ),
    "2.3.61": (
        _c("chāgasya haviṣaḥ preṣya", {"presya_bruva": True},
           note="प्रेष्यब्रुवोर्हविषो देवतासम्प्रदाने — one exact form "
                "of one root."),
    ),
    "2.3.62": (
        _c("candramasaḥ for candramase", {"chandas": True},
           note="चतुर्थ्यर्थे बहुलं छन्दसि."),
    ),
    "2.3.63": (
        _c("ghṛtasya yajate", {"yaj_karana": True, "chandas": True},
           note="यजेश्च करणे — the instrument, in the Veda."),
    ),
    "2.3.64": (
        _c("pañcakṛtvo'hno bhuṅkte", {"krtvo_artha": True},
           note="कृत्वोऽर्थप्रयोगे कालेऽधिकरणे — the affix must be used, "
                "not merely meant."),
    ),
    "2.3.65": (
        _c("apāṃ sraṣṭā", {"krt": "tṛc"},
           note="कर्तृकर्मणोः कृति — and 2.2.15 and 2.2.16 then forbid "
                "the compound."),
    ),
    "2.3.66": (
        _c("gavāṃ doho'gopālakena",
           {"krt": "ghañ", "ubhaya_prapti": True},
           note="उभयप्राप्तौ कर्मणि — only the object, and the doer "
                "falls to a third."),
    ),
    "2.3.67": (
        _c("rājñāṃ mataḥ", {"krt": "kta", "kta_vartamana": True},
           note="क्तस्य च वर्तमाने — the sixth taken back from 2.3.69, "
                "and 2.2.12 then keeps the words apart."),
    ),
    "2.3.68": (
        _c("idam eṣām āsitam", {"krt": "kta", "kta_adhikarana": True},
           note="अधिकरणवाचिनश्च, by 3.4.76."),
    ),
    "2.3.69": (
        _c("odanaṃ pacan — no genitive here", {"krt": "la"},
           note="न लोकाव्ययनिष्ठाखलर्थतृनाम् — and the Kāśikā spells the "
                "abbreviation out."),
    ),
    "2.3.70": (
        _c("kaṭaṃ kārako vrajati — nor here", {"krt": "aka"},
           note="अकेनोर्भविष्यदाधमर्ण्ययोः."),
    ),
    "2.3.71": (
        _c("bhavataḥ kaṭaḥ kartavyaḥ", {"krt": "tavya", "krtya": True},
           note="कृत्यानां कर्तरि वा — the doer only, and optionally."),
    ),
    "2.3.72": (
        _c("tulyo devadattena", {"tulya_artha": "tulya"},
           note="तुल्यार्थैरतुलोपमाभ्यां तृतीयाऽन्यतरस्याम्."),
        _c("tulā is excepted by name", {"tulya_artha": "tulā"},
           kind="counter",
           note="अतुलोपमाभ्यामिति किम्? though it means the same."),
    ),
    "2.3.73": (
        _c("āyuṣyaṃ devadattāya", {"blessing_with": "āyuṣya"},
           note="चतुर्थी चाशिष्य… — and the च drags the option down, so "
                "the sixth stands beside it. The last rule of the pāda."),
    ),
    "2.3.42": (
        _c("māthurāḥ pāṭaliputrakebhyaḥ", {"vibhakta": True},
           note="पञ्चमी विभक्ते, षष्ठीसप्तम्यपवादो योगः."),
    ),
    "2.3.43": (
        _c("mātari sādhuḥ", {"sadhu_nipuna": True},
           note="साधुनिपुणाभ्यामर्चायां सप्तम्यप्रतेः."),
    ),
    "2.3.44": (
        _c("keśaiḥ prasitaḥ", {"prasita_utsuka": True},
           note="प्रसितोत्सुकाभ्यां तृतीया च — a third and a seventh."),
    ),
    "2.3.45": (
        _c("puṣyeṇa pāyasam", {"naksatra_lup": True},
           note="नक्षत्रे च लुपि."),
    ),
    "2.3.46": (
        _c("droṇaḥ — a measure and nothing more",
           {"pratipadika_artha": True},
           note="प्रातिपदिकार्थलिङ्गपरिमाणवचनमात्रे प्रथमा, and मात्र "
                "attaches to each of the four."),
    ),
    "2.3.47": (
        _c("he devadatta", {"sambodhana": True},
           note="सम्बोधने च — calling out adds to the bare stem-meaning, "
                "which is why 2.3.46 alone would not reach it."),
    ),
    "2.3.48": (
        _c("he devadattāḥ is an āmantrita", {"vacana": 3},
           note="सामन्त्रितम् — the name, not an ending."),
    ),
    "2.3.49": (
        _c("he paṭo is a saṃbuddhi", {"vacana": 1},
           note="एकवचनं संबुद्धिः — and that name is what lets 6.1.69 "
                "shorten the ending."),
    ),
    "2.3.50": (
        _c("rājñaḥ puruṣaḥ", {"sesa": True},
           note="षष्ठी शेषे — asked last, because a remainder cannot be "
                "found before the things it is left over from."),
    ),
    "2.3.51": (
        _c("sarpiṣo jānīte", {"jna_avidartha": True},
           note="ज्ञोऽविदर्थस्य करणे — the INSTRUMENT takes the sixth."),
    ),
    "2.3.52": (
        _c("mātuḥ smarati", {"sixth_object_verb": "adhīgartha"},
           note="अधीगर्थदयेशां कर्मणि, शेषत्वेन विवक्षिते."),
    ),
    "2.3.53": (
        _c("edhodakasyopaskurute", {"sixth_object_verb": "kṛñ-pratiyatna"},
           note="कृञः प्रतियत्ने — bettering, not making."),
    ),
    "2.3.54": (
        _c("caurasya rujati rogaḥ", {"sixth_object_verb": "rujārtha"},
           note="रुजार्थानां… अज्वरेः."),
    ),
    "2.3.55": (
        _c("sarpiṣo nāthate", {"sixth_object_verb": "nāth"},
           note="आशिषि नाथः — one of that root's four senses."),
    ),
    "2.3.56": (
        _c("caurasyojjāsayati", {"sixth_object_verb": "jasi"},
           note="जासिनिप्रहणनाटक्राथपिषां हिंसायाम्, and the Kāśikā "
                "picks which जसु is meant."),
    ),
    "2.3.57": (
        _c("śatasya vyavaharati", {"sixth_object_verb": "vyavahṛ"},
           note="व्यवहृपणोः समर्थयोः — only where the two mean the same."),
    ),
    "2.3.27": (
        _c("kena hetunā vasati",
           {"sarvanaman": True, "hetu_prayoga": True},
           note="सर्वनाम्नस्तृतीया च — a third beside 2.3.26's sixth."),
    ),
    "2.3.28": (
        _c("grāmād āgacchati", {"karaka": "apādāna"},
           note="अपादाने पञ्चमी, and 1.4.24 decided the कारक."),
    ),
    "2.3.29": (
        _c("anyo devadattāt", {"fifth_after": "anya"},
           note="अन्यारादितरर्ते…, and अन्य इत्यर्थग्रहणम्."),
        _c("bhinno devadattāt", {"fifth_after": "bhinna"},
           note="The sense-reading admits words the sūtra does not name."),
    ),
    "2.3.30": (
        _c("dakṣiṇato grāmasya", {"atas_affix": True},
           note="षष्ठ्यतसर्थप्रत्ययेन."),
    ),
    "2.3.31": (
        _c("dakṣiṇena grāmam", {"enap": True},
           note="एनपा द्वितीया, and षष्ठ्यपीष्यते too."),
    ),
    "2.3.32": (
        _c("pṛthag devadattena", {"prthag_vina_nana": True},
           note="पृथग्विनानानाभिस्तृतीयाऽन्यतरस्याम्."),
    ),
    "2.3.33": (
        _c("stokād muktaḥ", {"little_and_hard": "stoka"},
           note="करणे च स्तोकाल्प… — the fifth is what this adds."),
    ),
    "2.3.34": (
        _c("dūraṃ grāmasya", {"dura_antika": True},
           note="दूरान्तिकार्थैः षष्ठ्यन्यतरस्याम्, and four cases in "
                "all across the three rules."),
    ),
    "2.3.35": (
        _c("dūreṇa grāmasya", {"dura_antika": True},
           note="दूरान्तिकार्थेभ्यो द्वितीया च — the second and third of "
                "the four."),
    ),
    "2.3.36": (
        _c("sthālyāṃ pacati", {"karaka": "adhikaraṇa"},
           note="सप्तम्यधिकरणे च, and 1.4.45 decided the कारक."),
    ),
    "2.3.37": (
        _c("goṣu duhyamānāsu gataḥ", {"bhava_laksana": True},
           note="यस्य च भावेन भावलक्षणम्."),
    ),
    "2.3.38": (
        _c("rudataḥ prāvrājīt", {"bhava_laksana": True, "anadara": True},
           note="षष्ठी चानादरे — a sixth beside 2.3.37's seventh."),
    ),
    "2.3.39": (
        _c("gavāṃ svāmī", {"holding": "svāmin"},
           note="स्वामीश्वराधिपति… — a sixth or a seventh."),
    ),
    "2.3.40": (
        _c("āyuktaḥ kaṭakaraṇe", {"holding": "āyukta"},
           note="आयुक्तकुशलाभ्यां चासेवायाम्."),
    ),
    "2.3.41": (
        _c("manuṣyāṇāṃ kṣatriyaḥ", {"nirdharana": True},
           note="यतश्च निर्धारणम्, and 2.2.10 keeps it from compounding."),
    ),
    "2.3.14": (
        _c("edhebhyo vrajati", {"kriyartha_upapada": True},
           note="क्रियार्थोपपदस्य च कर्मणि स्थानिनः, and द्वितीयापवादो "
                "योगः."),
    ),
    "2.3.15": (
        _c("pākāya vrajati", {"tumartha_bhava": True},
           note="तुमर्थाच्च भाववचनात्."),
    ),
    "2.3.16": (
        _c("namo devebhyaḥ", {"namas_yoga": "namas"},
           note="नमःस्वस्तिस्वाहास्वधालंवषड्योगाच्च."),
        _c("prabhur mallo mallāya", {"namas_yoga": "prabhu"},
           note="अलमिति पर्याप्त्यर्थग्रहणम् — the sense-reading admits "
                "words the list does not name."),
    ),
    "2.3.17": (
        _c("na tvā tṛṇāya manye",
           {"karaka": "karman", "manya_karman": True, "anadara": True},
           note="मन्यकर्मण्यनादरे विभाषाऽप्राणिषु."),
    ),
    "2.3.18": (
        _c("devadattena kṛtam", {"karaka": "kartṛ"},
           note="कर्तृकरणयोस्तृतीया, for the doer."),
        _c("dātreṇa lunāti", {"karaka": "karaṇa"},
           note="And for the tool."),
    ),
    "2.3.19": (
        _c("putreṇa sahāgataḥ pitā",
           {"saha_yukta": True, "apradhana": True},
           note="सहयुक्तेऽप्रधाने."),
    ),
    "2.3.20": (
        _c("akṣṇā kāṇaḥ", {"anga_vikara": True},
           note="येनाङ्गविकारः — and 2.1.30 uses the same phrase as ITS "
                "counter: blind in the eye, not blinded by it."),
    ),
    "2.3.21": (
        _c("kamaṇḍalunā chātram", {"itthambhuta_laksana": True},
           note="इत्थंभूतलक्षणे."),
    ),
    "2.3.22": (
        _c("pitrā saṃjānīte", {"samjna_karman": True},
           note="संज्ञोऽन्यतरस्यां कर्मणि — a third or the second, "
                "either."),
    ),
    "2.3.23": (
        _c("dhanena kulam", {"hetu": True},
           note="हेतौ, and it heads a run of four."),
    ),
    "2.3.24": (
        _c("śatād baddhaḥ", {"hetu": True, "rna": True},
           note="अकर्तर्यृणे पञ्चमी, तृतीयापवादो योगः."),
    ),
    "2.3.25": (
        _c("jāḍyād baddhaḥ", {"hetu": True, "guna": True},
           note="विभाषा गुणेऽस्त्रियाम् — a fifth or a third."),
        _c("buddhyā muktaḥ — feminine, so only the third",
           {"hetu": True, "guna": True, "astri": False}, kind="counter",
           note="अस्त्रियामिति किम्?"),
    ),
    "2.3.26": (
        _c("annasya hetor vasati", {"hetu_prayoga": True},
           note="षष्ठी हेतुप्रयोगे, the last of the four."),
    ),
    "2.3.1": (
        _c("kriyate kaṭaḥ — the verb has said it already",
           {"karaka": "karman", "expressed_by": "tiṅ"},
           note="अनभिहिते. Four things can express a kāraka and the list "
                "is closed: तिङ्कृत्तद्धितसमासैः परिसंख्यानम्."),
        _c("kaṭaṃ karoti — nothing has, so an ending is given",
           {"karaka": "karman"}, kind="counter",
           note="Without one of the four, 2.3.2 reaches it."),
    ),
    "2.3.2": (
        _c("kaṭaṃ karoti — the object takes the second",
           {"karaka": "karman"},
           note="कर्मणि द्वितीया, and 1.4.49 decided which participant "
                "is the कर्म."),
    ),
    "2.3.3": (
        _c("yavāgvā juhoti — a third, in the Veda",
           {"karaka": "karman", "chandas_hu": True},
           note="तृतीया च होश्छन्दसि, and the च keeps the second too."),
    ),
    "2.3.4": (
        _c("antarā tvāṃ ca māṃ ca", {"antara": True},
           note="अन्तराऽन्तरेण युक्ते, displacing a genitive."),
    ),
    "2.3.5": (
        _c("māsam adhīte — the whole month",
           {"kala_adhvan": True, "atyanta_samyoga": True},
           note="कालाध्वनोरत्यन्तसंयोगे."),
    ),
    "2.3.6": (
        _c("māsenānuvāko'dhītaḥ — and it was learnt",
           {"kala_adhvan": True, "apavarga": True},
           note="अपवर्गे तृतीया — the act carried through to its result."),
    ),
    "2.3.7": (
        _c("dvyahe bhoktā and dvyahād bhoktā both stand",
           {"kala_adhvan": True, "karaka_madhye": True},
           note="सप्तमीपञ्चम्यौ कारकमध्ये. संख्यातानुदेशो न भवति — the "
                "two are not paired off."),
    ),
    "2.3.8": (
        _c("saṃhitām anu", {"karmapravacaniya": "anu"},
           note="कर्मप्रवचनीययुक्ते द्वितीया."),
    ),
    "2.3.9": (
        _c("upa khāryāṃ droṇaḥ",
           {"karmapravacaniya": "upa", "adhika": True},
           note="यस्मादधिकम् — a seventh, displacing 2.3.8's second."),
    ),
    "2.3.10": (
        _c("ā pāṭaliputrāt", {"karmapravacaniya": "āṅ"},
           note="पञ्चम्यपाङ्परिभिः."),
    ),
    "2.3.11": (
        _c("arjunataḥ prati",
           {"karmapravacaniya": "prati", "pratinidhi_pratidana": True},
           note="प्रतिनिधिप्रतिदाने च यस्मात्."),
    ),
    "2.3.12": (
        _c("grāmaṃ gacchati and grāmāya gacchati both stand",
           {"karaka": "karman", "gati_artha": True},
           note="गत्यर्थकर्मणि द्वितीयाचतुर्थ्यौ चेष्टायामनध्वनि."),
        _c("adhvānaṃ gacchati — a road, and only the second",
           {"karaka": "karman", "gati_artha": True, "adhvan": True},
           kind="counter",
           note="अनध्वनीति किम्? and अध्वनीत्यर्थग्रहणम् takes पन्थानम् "
                "with it."),
    ),
    "2.3.13": (
        _c("upādhyāyāya gāṃ dadāti", {"karaka": "sampradāna"},
           note="चतुर्थी सम्प्रदाने, and 1.4.32 decided the कारक."),
    ),
    "2.2.30": (
        _c("rājapuruṣaḥ — the subordinate member leads",
           {"members": ["rājan", "puruṣa"], "upasarjana": "rājan"},
           note="उपसर्जनं पूर्वम्, and the सूत्र says पूर्वम् to shut "
                "the other order out."),
    ),
    "2.2.31": (
        _c("rājadantaḥ — and here it follows instead",
           {"members": ["rājan", "danta"], "form": "rājadantaḥ",
            "upasarjana": "rājan"},
           note="राजदन्तादिषु परम्. Fifty-seven forms given whole."),
    ),
    "2.2.32": (
        _c("paṭuguptau — the घि-ending leads",
           {"members": ["paṭu", "gupta"], "samasa": "dvandva"},
           note="द्वन्द्वे घि, and which words are घि is 1.4.7's — "
                "fetched from it rather than stated."),
    ),
    "2.2.33": (
        _c("indrāgnī — vowel-initial and अ-final wins over घि",
           {"members": ["indra", "agni"], "samasa": "dvandva"},
           note="अजाद्यदन्तम्, and द्वन्द्वे घ्यन्ताद् अजाद्यदन्तं "
                "विप्रतिषेधेन."),
    ),
    "2.2.34": (
        _c("plakṣanyagrodhau — the shorter word leads",
           {"members": ["plakṣa", "nyagrodha"], "samasa": "dvandva"},
           note="अल्पाच्तरम्, the last of the three dvandva rules."),
    ),
    "2.2.35": (
        _c("kaṇṭhekālaḥ — the locative leads",
           {"members": ["kaṇṭha", "kāla"], "samasa": "bahuvrīhi",
            "saptami": "kaṇṭha"},
           note="सप्तमीविशेषणे बहुव्रीहौ. Every member of a bahuvrīhi is "
                "subordinate, so 2.2.30 settles nothing."),
    ),
    "2.2.36": (
        _c("kṛtakaṭaḥ — the निष्ठा leads",
           {"members": ["kṛta", "kaṭa"], "samasa": "bahuvrīhi",
            "nistha": "kṛta"},
           note="निष्ठा."),
        _c("māsajātaḥ — and here it follows a word of time",
           {"members": ["jāta", "māsa"], "samasa": "bahuvrīhi",
            "nistha": "jāta", "jati_kala_sukha": "māsa"},
           note="निष्ठायाः पूर्वनिपाते जातिकालसुखादिभ्यः परवचनम्."),
    ),
    "2.2.37": (
        _c("agnyāhitaḥ — or āhitāgniḥ, either way",
           {"members": ["āhita", "agni"], "form": "āhitāgniḥ",
            "nistha": "āhita"},
           note="वाहितग्न्यादिषु — 2.2.36 becomes a choice here."),
    ),
    "2.2.38": (
        _c("kaḍārajaiminiḥ — or jaiminikaḍāraḥ, either way",
           {"members": ["kaḍāra", "jaimini"], "samasa": "karmadhāraya"},
           note="कडाराः कर्मधारये, and the last rule of the section."),
    ),
    "2.2.23": (
        _c("prāptodako grāmaḥ", {"first": "prāptodaka", "second": "grāma",
                                 "given": ["anya-padārtha-bv"]},
           note="शेषो बहुव्रीहिः — the heading names whatever the section "
                "has not already named, and 2.2.24 is the first rule "
                "under it. The compound means the village."),
        _c("unmattagaṅgam — named already, so not left over",
           {"first": "unmatta", "second": "gaṅgā",
            "given": ["nadī", "anya-padārtha", "saṃjñā"]},
           kind="counter",
           note="शेष इति किम्? 2.1.21 reached this one, so it is an "
                "अव्ययीभाव and never falls to the remainder."),
    ),
    "2.1.22": (
        _c("kaṣṭaśritaḥ",
           {"first": "kaṣṭa", "second": "śrita", "first_vibhakti": 2},
           note="उत्तरपदार्थप्रधानः — a person resorted, not a hardship. "
                "The heading names what 2.1.24 joins; it joins nothing "
                "itself."),
        _c("upakumbham — the heading above, running the other way",
           {"first": "upa", "second": "kumbha", "sense": "samīpa"},
           kind="counter",
           note="अव्ययीभाव, and there the FIRST member's meaning leads. "
                "The two headings differ in exactly this."),
    ),
    "2.1.23": (
        _c("which names 2.1.23 confers", {"sutra_id": "2.1.23"},
           note="द्विगुश्च — a द्विगु is called तत्पुरुष as well. This "
                "sūtra joins no pair, so what there is to run is the "
                "name-lookup: it comes back {samāsa, tatpuruṣa}, read off "
                "the ranges of 2.1.3 and 2.1.22. The extension is wanted "
                "because the samāsānta affixes of 5.4 are prescribed for "
                "a तत्पुरुष — द्विगोस् तत्पुरुषत्वे समासान्ताः प्रयोजनम् "
                "— and neither द्विगु (2.1.52) nor those affixes is "
                "codified, so what runs here is the name and not the "
                "ending."),
    ),
    "2.1.11": (
        _c("apatrigartam — optional, by the heading",
           {"first": "apa", "second": "trigarta", "second_vibhakti": 5},
           note="Under 2.1.11, so अप त्रिगर्तेभ्यः stands beside it."),
        _c("upakumbham — before the heading, so obligatory",
           {"first": "upa", "second": "kumbha", "sense": "samīpa"},
           kind="counter",
           note="2.1.6 is above 2.1.11 and the option does not reach it."),
        _c("unmattagaṅgam — under the heading and still obligatory",
           {"first": "unmatta", "second": "gaṅgā",
            "given": ["nadī", "anya-padārtha", "saṃjñā"]},
           kind="counter",
           note="नहि वाक्येन संज्ञा गम्यते — there is no phrase to fall "
                "back to, so 2.1.21 escapes the heading it stands under."),
    ),
    "2.1.7": (
        _c("yathā devadattas tathā yajñadattaḥ",
           {"first": "yathā", "second": "vṛddha", "sense": "sādṛśya"},
           note="The sense this sūtra exists to take away, so the refusal "
                "is the rule working rather than a case escaping it: "
                "सादृश्यप्रतिषेधार्थम्. Compounds by nothing — not even by "
                "2.1.6, whose list of sixteen holds सादृश्य."),
    ),
    "2.1.9": (
        _c("vṛkṣaṃ prati vidyotate vidyut",
           {"first": "vṛkṣa", "second": "prati"},
           kind="counter",
           note="प्रति in its ordinary sense, not मात्रा."),
    ),
    "2.1.10": (
        _c("akṣau pari — not in the singular",
           {"first": "akṣa", "second": "pari", "first_vacana": 2,
            "given": ["kitava-vyavahāra"]},
           kind="counter",
           note="एकत्वे अक्षशलाकयोः. The numerals beside them are not so "
                "confined — द्विपरि and त्रिपरि stand."),
        _c("dvipari — a numeral, so no singular condition",
           {"first": "dvi", "second": "pari",
            "given": ["kitava-vyavahāra"]}),
    ),
    "2.1.14": (
        _c("srughnaṃ pratigataḥ — no mark",
           {"first": "prati", "second": "srughna", "sense": "ābhimukhya"},
           kind="counter",
           note="लक्षणेन इति किम्? Nothing here is being made a target."),
    ),
    "2.1.15": (
        _c("vṛkṣam anu vidyotate vidyut",
           {"first": "anu", "second": "vṛkṣa", "given": ["lakṣaṇa"]},
           kind="counter",
           note="अनु, and a mark, but not in the sense of nearness."),
    ),
    "2.1.21": (
        _c("śīghragaṅgo deśaḥ — a description, not a name",
           {"first": "śīghra", "second": "gaṅgā",
            "given": ["nadī", "anya-padārtha"]},
           kind="counter",
           note="संज्ञायाम् इति किम्?"),
        _c("kṛṣṇaveṇṇā — no third thing",
           {"first": "kṛṣṇa", "second": "veṇṇā",
            "given": ["nadī", "saṃjñā"]},
           kind="counter",
           note="अन्यपदार्थे इति किम्? The compound names the river "
                "itself."),
    ),
    # --- 3.1.68 to 7.3.84 : the rules that derive जयति --------------------
    "3.1.68": (
        _c("भवति (bhavati) — शप् after the root",
           {"kartari": True, "sarvadhatuka_follows": True},
           note="कर्तृवाचिनि सार्वधातुके परतो धातोः शप् प्रत्ययो भवति."),
        _c("क्रियते (kriyate) — the passive takes यक् instead",
           {"kartari": False, "sarvadhatuka_follows": True},
           note="कर्तरि इति किम्? Where the affix denotes the object, "
                "3.1.67 gives यक् instead. Worked rather than counter: "
                "refusing is what 3.1.68's कर्तरि does."),
    ),
    "3.4.113": (
        _c("भवति (bhavati) — a तिङ् ending", {"tin": True}),
        _c("शप् (śap) — a शित् affix", {"sit": True},
           note="Which is how शप् becomes सार्वधातुक, and so how 7.3.84 "
                "reaches जि in जयति."),
        _c("neither तिङ् nor शित्", {},
           note="The rule answers here too, and its answer is no. Worked "
                "rather than counter, for the same reason 2.1.2's ṣatva "
                "case is: a rule declining is that rule working."),
    ),
    "7.3.84": (
        _c("जि (ji) → जे (je) before शप्",
           {"stem": "ji", "sarvadhatuka": True},
           note="The guṇa of जयति. 1.1.3 says the substitution lands on "
                "the इक्, and 1.1.50 says which guṇa vowel goes there."),
        _c("नी (nī) → ने (ne)", {"stem": "nī", "sarvadhatuka": True}),
        _c("अग्नि (agni) — neither affix follows",
           {"stem": "agni"},
           note="सार्वधातुकार्धधातुकयोरिति किम्? अग्नित्वम्, "
                "अग्निकाम्यति — the इ stands. Worked, not counter: the "
                "condition refusing is the rule doing its work."),
    ),
    "7.2.114": (
        _c("मृज् (mṛj) → मार्ज् (mārj)", {"stem": "mṛj"},
           note="Two rules, not one: 1.1.50 gives आ as nearest to ऋ, and "
                "1.1.51 उरण् रपरः adds the र्."),
        _c("मृज् (mṛj) as a noun, not a root",
           {"stem": "mṛj", "dhatu": False},
           note="धातुग्रहणम् इदम् — कंसपरिमृड्भ्याम् is untouched. The rule "
                "answers, and its answer is no."),
        _c("भू (bhū) — the sūtra names मृज् only",
           {"stem": "bhū"},
           note="मृजेः — a rule that names one root reaches no other, and "
                "says so rather than falling silent."),
    ),
    "6.1.78": (
        _c("जे (je) + अ (a) → जय् (jay)", {"stem": "je"},
           note="The step that finishes जयति."),
        _c("लो (lo) → लव् (lav)", {"stem": "lo"}, note="लवनम्."),
        _c("चै (cai) → चाय् (cāy)", {"stem": "cai"}, note="चायकः."),
        _c("लौ (lau) → लाव् (lāv)", {"stem": "lau"}, note="लावकः."),
        _c("जे (je) with no vowel after it",
           {"stem": "je", "before_vowel": False},
           note="अचि — read down from 6.1.77. Without a vowel following, "
                "the एच् stands, and 6.1.78 is what says so."),
    ),
    # --- 6.1.64, 6.1.65, 3.4.79 : what नयति and एधते need -----------------
    "6.1.64": (
        _c("षह (ṣaha) → सह (saha)", {"root": "ṣaha"},
           note="धातोरादेः षकारस्य स्थाने सकारादेशो भवति — सहते."),
        _c("कष् (kaṣ) — the ष् is not initial", {"root": "kaṣ"},
           note="आदेरिति किम्? कषति keeps its ष्."),
        _c("षोडश (ṣoḍaśa) — not a root at all",
           {"root": "ṣoḍaśa", "dhatu": False},
           note="धातुग्रहणं किम्? A numeral is untouched."),
    ),
    "6.1.65": (
        _c("णीञ् (ṇīñ) → नीञ् (nīñ)", {"root": "ṇīñ"},
           note="धातोरादेः णकारस्य नकार आदेशो भवति — नयति, which is the "
                "Kāśikā's own example and the engine's."),
        _c("णम (ṇama) → नम (nama)", {"root": "ṇama"}, note="नमति."),
        _c("णह (ṇaha) → नह (naha)", {"root": "ṇaha"}, note="नह्यति."),
    ),
    "3.4.79": (
        _c("त (ta) → ते (te)", {"ending": "ta"},
           note="टितो लकारस्य आत्मनेपदानां टेः एकारादेशः — एधते, पचते. "
                "लट् is टित्, so the rule reaches it."),
        _c("आताम् (ātām) → आते (āte)", {"ending": "ātām"}),
        _c("त (ta) under a लकार that is not टित्",
           {"ending": "ta", "tit_lakara": False},
           note="टितः — the condition. Without it the ending stands."),
    ),
    # --- what completes the present paradigm of पच् ------------------------
    "7.1.3": (
        _c("झि (jhi) → अन्ति (anti)", {"affix": "jhi"},
           note="पचन्ति, कुर्वन्ति. An अपवाद to 1.3.7, which would make the "
                "झ् an इत् and leave a bare इ."),
        _c("ति (ti) — no झ् to replace", {"affix": "ti"}),
    ),
    "7.3.101": (
        _c("पच (paca) + मि (mi) → पचा (pacā)",
           {"stem": "paca", "ending": "mi"}, note="पचामि."),
        _c("पच (paca) + वस् (vas) → पचा (pacā)",
           {"stem": "paca", "ending": "vas"}, note="पचावः."),
        _c("पच (paca) + तस् (tas) — त् is not यञ्",
           {"stem": "paca", "ending": "tas"},
           note="यञीति किम्? पचतः, पचथः keep the short अ."),
        _c("चिनु (cinu) — the aṅga is not अ-final",
           {"stem": "cinu", "ending": "mas"},
           note="अत इति किम्? चिनुमः."),
    ),
    "8.2.66": (
        _c("पचतस् (pacatas) → पचतर् (pacatar)", {"pada": "pacatas"},
           note="The रु is a step, not the result — 8.3.15 finishes it."),
        _c("पचति (pacati) — no final स्", {"pada": "pacati"}),
    ),
    "8.3.15": (
        _c("पचतर् (pacatar) → पचतः (pacataḥ)", {"pada": "pacatar"},
           note="अवसाने — at a pause."),
        _c("अग्निर् (agnir) before नयति (nayati)",
           {"pada": "agnir", "at_pause": False, "following": "nayati"},
           note="खरवसानयोरिति किम्? न् is neither, so the र् stands."),
    ),
    "6.1.97": (
        _c("अ (a) + अ (a) → अ (a)", {"first": "a", "second": "a"},
           note="पररूपम् — the later stands: पचन्ति, and not पचान्ति."),
        _c("अ (a) + ए (e) → ए (e)", {"first": "a", "second": "e"}),
        _c("या (yā) — the first is not अ",
           {"first": "ā", "second": "a"},
           note="अत इति किम्? यान्ति, वान्ति."),
    ),
    "6.1.101": (
        _c("अ (a) + अ (a) → आ (ā)", {"first": "a", "second": "a"},
           note="दण्डाग्रम्. Where 6.1.97 also reaches, that अपवाद wins."),
        _c("इ (i) + ई (ī) → ई (ī)", {"first": "i", "second": "ī"},
           note="दधीन्द्रः."),
        _c("अ (a) + इ (i) — not सवर्ण",
           {"first": "a", "second": "i"},
           note="सवर्ण इति किम्? दध्यत्र — यण् applies instead."),
    ),
    # --- the second gaṇa ---------------------------------------------------
    "2.4.73": (
        _c("trādhvaṃ no devāḥ — śap gone in the Veda",
           {"affix": "śap", "chandas": True},
           note="बहुलं छन्दसि, and बहुलम् cuts both ways: "
                "अदिप्रभृतिभ्य उक्तस्ततो न भवत्यपि, अन्येभ्यश्च भवति."),
    ),
    "2.4.75": (
        _c("juhoti, bibharti", {"affix": "śap", "gana": "juhotyādi"},
           note="जुहोत्यादिभ्यः श्लुः — and श्लु rather than लुक्, "
                "द्विर्वचनार्थम्: only a श्लु makes the root double."),
    ),
    "2.4.76": (
        _c("dāti — the ślu fails, in the Veda",
           {"affix": "śap", "gana": "juhotyādi", "chandas": True},
           note="बहुलं छन्दसि, again in both directions: यत्रोक्तं तत्र "
                "न भवति, अन्यत्रापि भवति."),
    ),
    "2.4.77": (
        _c("abhūt — the sic goes", {"affix": "sic", "root": "bhū"},
           note="गातिस्थाघुपाभूभ्यः सिचः परस्मैपदेषु, and the गा meant "
                "is the one इण् became at 2.4.45."),
        _c("agāsātāṃ grāmau — the middle voice",
           {"affix": "sic", "root": "gā", "parasmaipada": False},
           kind="counter", note="परस्मैपदेष्विति किम्?"),
    ),
    "2.4.78": (
        _c("aghrāt, beside aghrāsīt",
           {"affix": "sic", "root": "ghrā"},
           note="विभाषा घ्राधेट्शाच्छासः — granting the option to four "
                "and loosening it for धेट्, which 2.4.77 already had."),
    ),
    "2.4.79": (
        _c("atata, beside ataniṣṭa",
           {"affix": "sic", "gana": "tanādi", "before": "ta"},
           note="तनादिभ्यस्तथासोः — and the त meant is the middle one, "
                "थासा साहचर्यात्."),
    ),
    "2.4.80": (
        _c("agman, akran — in a mantra",
           {"affix": "le", "root": "kṛ", "mantra": True},
           note="मन्त्रे घसह्वरणशवृदहाद्वृच्कृगमिजनिभ्यो लेः."),
        _c("outside a mantra the le stands",
           {"affix": "le", "root": "kṛ"}, kind="counter",
           note="मन्त्रे is a condition, not a note."),
    ),
    "2.4.81": (
        _c("īhāṃcakre", {"affix": "le", "root": "ām"},
           note="आमः — and मन्त्रे does not carry down from 2.4.80."),
    ),
    "2.4.82": (
        _c("kṛtvā, tatra śālāyām", {},
           note="अव्ययादाप्सुपः — what makes an indeclinable look "
                "uninflected: the ending is added and then taken away."),
    ),
    "2.4.83": (
        _c("upakumbhaṃ tiṣṭhati",
           {"avyayibhava": True, "ends_in_a": True, "vibhakti": 2},
           note="नाव्ययीभावादतोऽम्त्वपञ्चम्याः — the elision refused and "
                "अम् put there instead."),
        _c("upakumbhādānaya — the fifth case",
           {"avyayibhava": True, "ends_in_a": True, "vibhakti": 5},
           kind="counter",
           note="अपञ्चम्या इति किम्? एतस्मिन् प्रतिषिद्धे पञ्चम्याः "
                "श्रवणमेव भवति."),
        _c("adhistri — no final a, so the ending goes outright",
           {"avyayibhava": True, "vibhakti": 2}, kind="counter",
           note="अत इति किम्? It falls back to 2.4.82 and loses the "
                "ending outright."),
    ),
    "2.4.84": (
        _c("upakumbhena kṛtam, beside upakumbhaṃ kṛtam",
           {"avyayibhava": True, "ends_in_a": True, "vibhakti": 3},
           note="तृतीयासप्तम्योर्बहुलम् — पूर्वेण नित्यमम्भावे प्राप्ते "
                "वचनमिदम्, the third time this pāda reopens what the "
                "rule before had shut."),
    ),
    "2.4.85": (
        _c("kartā — the singular", {"number": 1},
           note="लुटः प्रथमस्य डारौरसः, यथाक्रमम् — and it serves the "
                "middle as well: अध्येता. The last rule of adhyāya 2."),
        _c("kartāraḥ — the plural", {"number": 3},
           note="The third of the three, रस्."),
    ),
    "2.4.58": (
        _c("kauravyaḥ pitā, kauravyaḥ putraḥ",
           {"descendant": "yuvan", "stem_kind": "ṇya", "affix": "iñ"},
           note="ण्यक्षत्रियार्षञितो यूनि लुगणिञोः — the yuvan affix goes "
                "and father and son are named alike."),
    ),
    "2.4.59": (
        _c("pailaḥ pitā, pailaḥ putraḥ",
           {"descendant": "yuvan", "stem": "paila"},
           note="पैलादिभ्यश्च, आकृतिगणोऽयम् — read from the gaṇapāṭha on "
                "disk, and open."),
    ),
    "2.4.60": (
        _c("pānnāgāriḥ pitā, pānnāgāriḥ putraḥ",
           {"descendant": "yuvan", "affix": "iñ", "region": "prāc"},
           note="इञः प्राचाम्, and गोत्रविशेषणं प्राग्ग्रहणम्, न "
                "विकल्पार्थम्."),
        _c("ārjuniḥ pitā, ārjunāyanaḥ putraḥ — the Bharatas",
           {"descendant": "yuvan", "affix": "iñ", "region": "bharata"},
           kind="counter",
           note="2.4.66 names भरत where it need not, and that ज्ञापन "
                "keeps them out of प्राच् here."),
    ),
    "2.4.61": (
        _c("taulvaliḥ pitā, taulvalāyanaḥ putraḥ",
           {"descendant": "yuvan", "stem": "taulvali", "affix": "iñ",
            "region": "prāc"},
           note="न तौल्वलिभ्यः — a प्रतिषेध, so refusing IS this rule "
                "acting and it reports itself."),
    ),
    "2.4.62": (
        _c("aṅgāḥ — a country-name in the plural",
           {"affix": "tadrāja", "plural": True},
           note="तद्राजस्य बहुषु तेनैवास्त्रियाम्."),
        _c("āṅgaḥ — singular", {"affix": "tadrāja"}, kind="counter",
           note="बहुष्विति किम्?"),
        _c("āṅgyaḥ striyaḥ — feminine",
           {"affix": "tadrāja", "plural": True, "feminine": True},
           kind="counter", note="अस्त्रियामिति किम्?"),
        _c("priyavāṅgāḥ — plural by the bahuvrīhi",
           {"affix": "tadrāja", "plural": True, "by_that_affix": False},
           kind="counter", note="तेनैवग्रहणं किम्?"),
    ),
    "2.4.63": (
        _c("yaskāḥ", {"descendant": "gotra", "stem": "yaska",
                      "plural": True},
           note="यस्कादिभ्यो गोत्रे, and the गोत्र is the everyday one: "
                "प्रत्ययविधेश्चान्यत्र लौकिकस्य गोत्रस्य ग्रहणम्."),
    ),
    "2.4.64": (
        _c("gargāḥ, bidāḥ", {"descendant": "gotra", "affix": "yañ",
                             "plural": True},
           note="यञञोश्च — यञ् by 4.1.105 and अञ् by 4.1.104."),
    ),
    "2.4.65": (
        _c("bhṛgavaḥ", {"descendant": "gotra", "stem": "bhṛgu",
                        "plural": True},
           note="अत्रिभृगुकुत्सवसिष्ठगोतमाङ्गिरोभ्यश्च — six names read "
                "from the sūtra itself."),
    ),
    "2.4.66": (
        _c("yudhiṣṭhirāḥ",
           {"descendant": "gotra", "affix": "iñ", "bahvac": True,
            "region": "bharata", "plural": True},
           note="बह्वच इञः प्राच्यभरतेषु, and the भरत named here is what "
                "keeps them out of 2.4.60."),
        _c("baikayaḥ — only two syllables",
           {"descendant": "gotra", "affix": "iñ", "region": "prācya",
            "plural": True}, kind="counter",
           note="बह्वच इति किम्?"),
    ),
    "2.4.67": (
        _c("gaupavanāḥ — the affix stays",
           {"descendant": "gotra", "stem": "gopavana", "affix": "añ",
            "plural": True},
           note="न गोपवनादिभ्यः — and the list is the Kāśikā's eight, "
                "not the gaṇapāṭha's eleven: एतावन्त एवाष्टौ."),
    ),
    "2.4.68": (
        _c("tikakitavāḥ — in a dvandva",
           {"stem": "tikakitavāḥ", "dvandva": True, "plural": True},
           note="तिककितवादिभ्यो द्वन्द्वे, and the gaṇa holds finished "
                "compounds as 2.4.11's गवाश्वादि does."),
    ),
    "2.4.69": (
        _c("upakāḥ, beside aupakāyanāḥ",
           {"stem": "kapiṣṭhala", "plural": True},
           note="उपकादिभ्योऽन्यतरस्यामद्वन्द्वे — a choice, outside a "
                "द्वन्द्व."),
    ),
    "2.4.70": (
        _c("agastayaḥ — affix gone, stem replaced",
           {"stem": "āgastya", "plural": True},
           note="आगस्त्यकौण्डिन्ययोरगस्तिकुण्डिनच्, यथासंख्यम् — the only "
                "rule of the run that replaces as well as elides."),
    ),
    "2.4.71": (
        _c("rājapuruṣaḥ — a compound", {"becomes": "prātipadika"},
           note="सुपो धातुप्रातिपदिकयोः — what lets 2.1 and 2.2 build a "
                "compound out of inflected words."),
        _c("putrīyati — a noun made into a verb",
           {"becomes": "dhātu"},
           note="तदन्तर्गतास्तद्ग्रहणेन गृह्यन्ते."),
        _c("vṛkṣaḥ — an ordinary word keeps its ending", {},
           kind="counter", note="धातुप्रातिपदिकयोरिति किम्?"),
    ),
    "2.4.32": (
        _c("atho ābhyām — a second mention",
           {"of": "idam", "before_vibhakti": 3, "given": "anvādeśa"},
           note="इदमोऽन्वादेशेऽशनुदात्तस्तृतीयादौ, and तृतीयादौ means the "
                "third case ONWARD."),
        _c("the second case goes elsewhere",
           {"of": "idam", "before_vibhakti": 2, "given": "anvādeśa"},
           kind="counter",
           note="Below the third, so 2.4.34 answers instead — which is "
                "what तृतीयादौ is for."),
    ),
    "2.4.33": (
        _c("atho atra", {"of": "etad", "before": "tra",
                         "given": "anvādeśa"},
           note="एतदस्त्रतसोस्त्रतसौ चानुदात्तौ — written for the accent, "
                "since 5.3.5 gives the substitute already."),
    ),
    "2.4.34": (
        _c("atho enam", {"of": "idam", "before": "2",
                         "given": "anvādeśa"},
           note="द्वितीयाटौस्स्वेनः, with इदम् carried down "
                "मण्डूकप्लुतिन्यायेन."),
        _c("atho enayoḥ — etad, before os",
           {"of": "etad", "before": "os", "given": "anvādeśa"},
           note="एतद् is on this row too, alongside इदम्."),
    ),
    "2.4.35": (
        _c("bhavitā — the heading at work",
           {"of": "as", "given": "ārdhadhātuka"},
           note="आर्धधातुके is an अधिकार through 2.4.57, and a "
                "विषयसप्तमी: the substitution happens where an "
                "आर्धधातुक is INTENDED and the affix follows after."),
        _c("without it, nothing is replaced", {"of": "as"},
           kind="counter",
           note="Every row from 2.4.36 needs the heading asserted."),
    ),
    "2.4.36": (
        _c("jagdhaḥ", {"of": "ad", "before": "kit-t", "given": "ārdhadhātuka"},
           note="अदो जग्धिर्ल्यप्ति किति."),
        _c("atyate — neither ल्यप् nor a त-initial कित्",
           {"of": "ad", "before": "yak", "given": "ārdhadhātuka"}, kind="counter",
           note="तीति किम्? अद्यते."),
    ),
    "2.4.37": (
        _c("aghasat, jighatsati",
           {"of": "ad", "before": "luṅ", "given": "ārdhadhātuka"},
           note="लुङ्सनोर्घस्लृ, and ऌदित्करणमङर्थम्."),
    ),
    "2.4.38": (
        _c("ghāsaḥ", {"of": "ad", "before": "ghañ", "given": "ārdhadhātuka"},
           note="घञपोश्च."),
    ),
    "2.4.39": (
        _c("sagdhiśca me", {"of": "ad", "chandas": True, "given": "ārdhadhātuka"},
           note="बहुलं छन्दसि — बहुलम् and not अन्यतरस्याम्, "
                "कार्यान्तरार्थम्."),
    ),
    "2.4.40": (
        _c("jaghāsa, beside āda",
           {"of": "ad", "before": "liṭ", "given": "ārdhadhātuka"},
           note="लिट्यन्यतरस्याम्."),
    ),
    "2.4.41": (
        _c("uvāya, beside ūvatuḥ",
           {"of": "veñ", "before": "liṭ", "given": "ārdhadhātuka"},
           note="वेञो वयिः, with the option carried down from 2.4.40."),
    ),
    "2.4.42": (
        _c("vadhyāt", {"of": "han", "before": "liṅ", "given": "ārdhadhātuka"},
           note="हनो वध लिङि, and the dropped अ still keeps 7.2.7's "
                "वृद्धि away by 1.1.56."),
    ),
    "2.4.43": (
        _c("avadhīt", {"of": "han", "before": "luṅ", "given": "ārdhadhātuka"},
           note="लुङि च — योगविभाग उत्तरार्थः, split so that 2.4.44's "
                "option reaches the aorist and not the benedictive."),
    ),
    "2.4.44": (
        _c("āvadhiṣṭa, beside āhata",
           {"of": "han", "before": "luṅ", "atmanepada": True,
            "given": "ārdhadhātuka"},
           note="आत्मनेपदेष्वन्यतरस्याम् — पूर्वेण नित्ये प्राप्ते विकल्प "
                "उच्यते, so the LAST matching row wins."),
    ),
    "2.4.45": (
        _c("agāt", {"of": "iṇ", "before": "luṅ", "given": "ārdhadhātuka"},
           note="इणो गा लुङि, and लुङ् is repeated so 2.4.44's option "
                "does not carry: पुनर्लुङ्ग्रहणम्."),
    ),
    "2.4.46": (
        _c("gamayati", {"of": "iṇ", "before": "ṇi", "given": "ārdhadhātuka"},
           note="णौ गमिरबोधने."),
        _c("pratyāyayati — making someone know",
           {"of": "iṇ", "before": "ṇi", "sense": "bodhana",
            "given": "ārdhadhātuka"}, kind="counter",
           note="अबोधन इति किम्?"),
    ),
    "2.4.47": (
        _c("jigamiṣati", {"of": "iṇ", "before": "san", "given": "ārdhadhātuka"},
           note="सनि च — the second योगविभाग, so that 2.4.48 gets सन् "
                "alone."),
    ),
    "2.4.48": (
        _c("adhijigāṃsate", {"of": "iṅ", "before": "san", "given": "ārdhadhātuka"},
           note="इङश्च, before सन् only."),
        _c("iṅ before ṇi is not reached",
           {"of": "iṅ", "before": "ṇi", "given": "ārdhadhātuka"}, kind="counter",
           note="Which is exactly what 2.4.47's split bought."),
    ),
    "2.4.49": (
        _c("adhijage", {"of": "iṅ", "before": "liṭ", "given": "ārdhadhātuka"},
           note="गाङ् लिटि — the ङ् marked विशेषणार्थम्, so 1.2.1 can "
                "reach it: नहि स्थानिवद्भावेन गाङिति रूपं लभ्यते."),
    ),
    "2.4.50": (
        _c("adhyagīṣṭa, beside adhyaiṣṭa",
           {"of": "iṅ", "before": "luṅ", "given": "ārdhadhātuka"},
           note="विभाषा लुङ्लृङोः."),
    ),
    "2.4.51": (
        _c("adhyajīgapat, beside adhyāpipat",
           {"of": "iṅ", "before": "ṇi-caṅ", "given": "ārdhadhātuka"},
           note="णौ च संश्चङोः — two locatives at different depths, so "
                "the row is keyed on the pair."),
    ),
    "2.4.52": (
        _c("bhavitā", {"of": "as", "given": "ārdhadhātuka"},
           note="अस्तेर्भूः, with no affix named — it holds through the "
                "whole heading."),
    ),
    "2.4.53": (
        _c("vaktā", {"of": "brū", "given": "ārdhadhātuka"},
           note="ब्रुवो वचिः, and स्थानिवद्भाव keeps ब्रू's middle: ऊचे."),
    ),
    "2.4.54": (
        _c("ākhyātā", {"of": "cakṣiṅ", "given": "ārdhadhātuka"},
           note="चक्षिङः ख्याञ् — the ञ् marked so the substitute does "
                "NOT keep चक्षिङ्'s obligatory middle."),
    ),
    "2.4.55": (
        _c("ācakhyau, beside ācacakṣe",
           {"of": "cakṣiṅ", "before": "liṭ", "given": "ārdhadhātuka"},
           note="वा लिटि, the same shape as 2.4.44 over 2.4.43."),
    ),
    "2.4.56": (
        _c("pravāyakaḥ", {"of": "aj", "given": "ārdhadhātuka"},
           note="अजेर्व्यघञपोः, and दीर्घोच्चारणं किम्? प्रवीताः."),
        _c("samājaḥ — before घञ्",
           {"of": "aj", "before": "ghañ", "given": "ārdhadhātuka"}, kind="counter",
           note="अघञपोरिति किम्?"),
    ),
    "2.4.57": (
        _c("pravayaṇo daṇḍaḥ, beside prājano",
           {"of": "aj", "before": "lyuṭ", "given": "ārdhadhātuka"},
           note="वा यौ — यु stands for ल्युट्, and this closes 2.4.35's "
                "heading."),
    ),
    "3.2.1": (
        _c("kumbhakāraḥ — a potter",
           {"root": "kṛ", "beside": "kumbha", "role": "karman"},
           note="कर्मण्यण् — the widest rule of the run, and the one "
                "3.1.92's उपपद was named for."),
        _c("grāmaṃ gacchati — reached by the rule, refused by usage",
           {"root": "gam", "beside": "grāma", "role": "karman"},
           note="NOT a counter-example: 3.2.1 fires here, and the "
                "vṛtti stops it from outside — न भवति, अनभिधानात्, "
                "there being no such word in use. A limit checked "
                "against usage rather than against the root or the "
                "companion, so no condition can carry it and the "
                "registration note carries the scar instead. Labelling "
                "this a counter-example was wrong and the case guard "
                "said so."),
    ),
    "3.2.2": (
        _c("tantuvāyaḥ — a weaver",
           {"root": "veñ", "beside": "tantu", "role": "karman"},
           note="ह्वावामश्च, कप्रत्ययस्यापवादः — three roots named so "
                "as to keep अण् against the rule after."),
    ),
    "3.2.3": (
        _c("godaḥ — a giver of cows",
           {"root": "dā", "beside": "go", "role": "karman"},
           note="आतोऽनुपसर्गे कः, अणोऽपवादः."),
        _c("gosaṃdāyaḥ — with a preverb",
           {"root": "dā", "beside": "go", "role": "karman",
            "upasarga": "sam"}, kind="counter",
           note="अनुपसर्ग इति किम्? — and the preverb is 1.4.59's "
                "question, asked and not restated."),
    ),
    "3.2.4": (
        _c("samasthaḥ — standing level",
           {"root": "sthā", "beside": "sama", "role": "sup"},
           note="सुपि स्थः. अत्र योगविभागः कर्तव्यः — the split buys "
                "the भाव sense, आखूत्थः."),
    ),
    "3.2.5": (
        _c("tundaparimṛjaḥ — an idler",
           {"root": "parimṛj", "beside": "tunda", "role": "karman"},
           note="तुन्दशोकयोः परिमृजापनुदोः, यथासंख्यम् — and a "
                "vārttika fixes the sense as आलस्य."),
        _c("the pair crossed",
           {"root": "parimṛj", "beside": "śoka", "role": "karman"},
           kind="counter",
           note="यथासंख्यम् binds them crosswise, so this is not "
                "3.2.5's — it falls to the general rule."),
    ),
    "3.2.6": (
        _c("sarvapradaḥ — one who gives all",
           {"root": "dā", "beside": "sarva", "role": "karman",
            "upasarga": "pra"},
           note="प्रे दाज्ञः, सोपसर्गार्थ आरम्भः — the rule exists to "
                "let back in what 3.2.3 shut out."),
    ),
    "3.2.7": (
        _c("gosaṃkhyaḥ — a cowherd",
           {"root": "khyā", "beside": "go", "role": "karman",
            "upasarga": "sam"},
           note="समि ख्यः — and ख्या is what चक्षिङ् became by 2.4.54, "
                "which is codified."),
    ),
    "3.2.8": (
        _c("sāmagaḥ — a singer of chants",
           {"root": "gai", "beside": "sāman", "role": "karman"},
           note="गापोष्टक्, कस्यापवादः. अनुपसर्ग इत्येव: शक्रसंगायः."),
    ),
    "3.2.9": (
        _c("aṃśaharaḥ — one who takes a share",
           {"root": "hṛ", "beside": "aṃśa", "role": "karman"},
           note="हरतेरनुद्यमनेऽच्, अणोऽपवादः. उद्यमनम् उत्क्षेपणम्."),
        _c("bhāraharaḥ — of lifting",
           {"root": "hṛ", "beside": "bhāra", "role": "karman",
            "sense": "udyamana"}, kind="counter",
           note="अनुद्यमन इति किम्? — the general अण् stands."),
    ),
    "3.2.10": (
        _c("asthiharaḥ śvā — a dog old enough",
           {"root": "hṛ", "beside": "asthi", "role": "karman",
            "sense": "vayas"},
           note="वयसि च, उद्यमनार्थोऽयम् आरम्भः — the rule gives back "
                "the very sense 3.2.9 refused."),
    ),
    "3.2.11": (
        _c("puṣpāharaḥ — a flower-picker by habit",
           {"root": "hṛ", "beside": "puṣpa", "role": "karman",
            "upasarga": "āṅ", "sense": "tācchīlya"},
           note="आङि ताच्छील्ये — ताच्छील्यं तत्स्वभावता."),
    ),
    "3.2.12": (
        _c("pūjārhā — she who deserves honour",
           {"root": "arh", "beside": "pūjā", "role": "karman"},
           note="अर्हः, अणोऽपवादः — स्त्रीलिङ्गे विशेषः."),
    ),
    "3.2.13": (
        _c("karṇejapaḥ — an informer",
           {"root": "jap", "beside": "karṇa", "role": "sup"},
           note="स्तम्बकर्णयो रमिजपोः — सुपि and not कर्मणि, and the "
                "vṛtti reasons it out: रमेरकर्मकत्वात्, जपेः "
                "शब्दकर्मकत्वात् कर्म न संभवति."),
    ),
    "3.2.14": (
        _c("śaṃkaraḥ — the doer of good",
           {"root": "kṛ", "beside": "śam", "role": "sup",
            "sense": "saṃjñā"},
           note="शमि धातोः संज्ञायाम् — धातुग्रहणं कृञो हेत्वादिषु "
                "टप्रतिषेधार्थम्, a word repeated to fence off 3.2.20."),
    ),
    "3.2.15": (
        _c("khaśayaḥ — one who lies in the open",
           {"root": "śī", "beside": "kha", "role": "adhikaraṇa"},
           note="अधिकरणे शेतेः — four vārttikas widen it."),
    ),
    "3.2.16": (
        _c("kurucaraḥ, kurucarī",
           {"root": "car", "beside": "kuru", "role": "adhikaraṇa"},
           note="चरेष्टः — प्रत्ययान्तरकरणं ङीबर्थम्, an affix chosen "
                "for what a rule in adhyāya 4 does with its marker."),
    ),
    "3.2.17": (
        _c("bhikṣācaraḥ — one who goes about begging",
           {"root": "car", "beside": "bhikṣā", "role": "sup"},
           note="भिक्षासेनादायेषु च — अनधिकरणार्थ आरम्भः."),
    ),
    "3.2.18": (
        _c("puraḥsaraḥ — a forerunner",
           {"root": "sṛ", "beside": "puras", "role": "sup"},
           note="पुरोऽग्रतोऽग्रेषु सर्तेः."),
    ),
    "3.2.19": (
        _c("pūrvasaraḥ — he who goes first",
           {"root": "sṛ", "beside": "pūrva", "role": "kartṛ"},
           note="पूर्वे कर्तरि."),
        _c("pūrvasāraḥ — the place gone to",
           {"root": "sṛ", "beside": "pūrva", "role": "karman"},
           kind="counter",
           note="कर्तरीति किम्? — one word, one root, and the kāraka "
                "is the whole of the difference."),
    ),
    "3.2.20": (
        _c("śokakarī — she who causes grief",
           {"root": "kṛ", "beside": "śoka", "role": "karman",
            "sense": "hetu-tācchīlya-ānulomya"},
           note="कृञो हेतुताच्छील्यानुलोम्येषु — हेतुरैकान्तिकं "
                "कारणम्, ताच्छील्यं तत्स्वभावता, आनुलोम्यम् अनुकूलता."),
        _c("kumbhakāraḥ — outside the three senses",
           {"root": "kṛ", "beside": "kumbha", "role": "karman"},
           kind="counter",
           note="एतेष्विति किम्? — the run closes by handing the "
                "ground back to 3.2.1."),
    ),
    "3.2.21": (
        _c("divākaraḥ — the sun",
           {"root": "kṛ", "beside": "divā", "role": "sup"},
           note="अहेत्वाद्यर्थ आरम्भः — the rule covers what 3.2.20's "
                "three senses left out, so it names its companions. "
                "दिवाशब्दोऽधिकरणवचनः, and both कर्मणि and सुपि run "
                "down यथायोगम्."),
    ),
    "3.2.22": (
        _c("karmakaraḥ — a hired labourer",
           {"root": "kṛ", "beside": "karman", "role": "karman",
            "sense": "bhṛti"},
           note="कर्मणीति स्वरूपग्रहणम् — the WORD कर्मन्, not the "
                "kāraka 3.2.1 meant by the same word."),
        _c("karmakāraḥ — no wages meant",
           {"root": "kṛ", "beside": "karman", "role": "karman"},
           kind="counter", note="भृताविति किम्?"),
    ),
    "3.2.23": (
        _c("śabdakāraḥ — the ṭa refused, the aṇ supplied",
           {"root": "kṛ", "beside": "śabda", "role": "karman",
            "sense": "hetu-tācchīlya-ānulomya"},
           note="न शब्दश्लोक… — हेत्वादिषु प्राप्तः प्रतिषिध्यते. The "
                "answer names 3.2.1, which SUPPLIES the affix, and "
                "carries 3.2.23 as what blocked the nearer rule."),
    ),
    "3.2.24": (
        _c("stambakariḥ — rice that forms clumps",
           {"root": "kṛ", "beside": "stamba", "role": "karman",
            "names_a": "vrīhi-vatsa"},
           note="स्तम्बशकृतोरिन्, with the vārttika व्रीहिवत्सयोरिति "
                "वक्तव्यम् codified as a condition."),
        _c("stambakāraḥ — neither rice nor calf",
           {"root": "kṛ", "beside": "stamba", "role": "karman"},
           kind="counter", note="व्रीहिवत्सयोरिति किम्?"),
    ),
    "3.2.25": (
        _c("dṛtihariḥ paśuḥ — a beast that carries a waterskin",
           {"root": "hṛ", "beside": "dṛti", "role": "karman",
            "names_a": "paśu"},
           note="हरतेर्दृतिनाथयोः पशौ — and the condition is on what "
                "the WORD names, which is why it needed a field of "
                "its own."),
        _c("dṛtihāraḥ — carrying is lifting",
           {"root": "hṛ", "beside": "dṛti", "role": "karman",
            "sense": "udyamana"}, kind="counter",
           note="पशाविति किम्? — and 3.2.9's अच् is out too, since "
                "carrying a waterskin IS उद्यमन. Both conditions at "
                "once, which one field could not hold."),
    ),
    "3.2.26": (
        _c("ātmambhariḥ — one who feeds only himself",
           {"word": "ātmambhari"},
           note="फलेग्रहिरात्मम्भरिश्च — a निपातन, so it has its own "
                "entry point: आत्मशब्दस्योपपदस्य मुमागम इन्प्रत्ययश्च "
                "भृञो निपात्यते, the augment and the affix both simply "
                "fixed. A table deriving these would be pretending."),
        _c("kukṣimbhariḥ — gathered in by the ca",
           {"word": "kukṣimbhari"},
           note="अनुक्तसमुच्चयार्थश्चकारः — the two words the sūtra "
                "states are not the whole of it."),
    ),
    "3.2.27": (
        _c("brahmavaniḥ — in the Veda",
           {"root": "van", "beside": "brahman", "role": "karman",
            "chandasi": True},
           note="छन्दसि वनसनरक्षिमथाम् — the vṛtti cites a passage "
                "for each of the four roots."),
        _c("outside the Veda",
           {"root": "van", "beside": "brahman", "role": "karman"},
           kind="counter", note="छन्दसि विषये — the rule does not "
                                "reach ordinary usage."),
    ),
    "3.2.28": (
        _c("janamejayaḥ — who makes people tremble",
           {"root": "ej", "beside": "jana", "role": "karman",
            "causative": True},
           note="एजेः खश्, ण्यन्तात्. खकारो मुमर्थः; शकारः "
                "सार्वधातुकसंज्ञार्थः, by 3.4.113 — cited, since what "
                "the marker buys happens downstream of this choice."),
    ),
    "3.2.29": (
        _c("stanandhayaḥ — a suckling",
           {"root": "dheṭ", "beside": "stana", "role": "karman"},
           note="नासिकास्तनयोर्ध्माधेटोः — and यथासंख्यमत्र नेष्यते: "
                "स्तने धेटः, but नासिकायां तु ध्मश्च धेटश्च."),
        _c("stana with the other root — not licensed",
           {"root": "dhmā", "beside": "stana", "role": "karman"},
           kind="counter",
           note="स्तने धेटः — the pairing here is neither one-to-one "
                "nor the full product, and the sign is in the "
                "wording: लक्षणव्यभिचारचिह्नाद् "
                "अल्पाच्तरस्यापूर्वनिपातनाल्लभ्यते."),
    ),
    "3.2.30": (
        _c("nāḍindhamaḥ — a pipe-blower",
           {"root": "dhmā", "beside": "nāḍī", "role": "karman"},
           note="नाडीमुष्ट्योश्च — here every combination stands, and "
                "अनुक्तसमुच्चयार्थश्चकारः adds घटि, खारि, वात."),
    ),
    "3.2.31": (
        _c("kūlamudvahaḥ", {"root": "vah", "beside": "kūla",
                            "role": "karman", "upasarga": "ud"},
           note="उदि कूले रुजिवहोः — the preverb is a condition here, "
                "not a bar as at 3.2.3."),
    ),
    "3.2.32": (
        _c("abhraṃlihaḥ vāyuḥ — the cloud-licking wind",
           {"root": "lih", "beside": "abhra", "role": "karman"},
           note="वहाभ्रे लिहः."),
    ),
    "3.2.33": (
        _c("prasthaṃpacā sthālī",
           {"root": "pac", "beside": "prastha", "role": "karman"},
           note="परिमाणे पचः — परिमाणं प्रस्थादि, an आकृतिगण, so the "
                "class is open and the members named are examples."),
    ),
    "3.2.34": (
        _c("nakhampacā yavāgūḥ",
           {"root": "pac", "beside": "nakha", "role": "karman"},
           note="मितनखे च — अपरिमाणार्थ आरम्भः, since neither word is "
                "a measure."),
    ),
    "3.2.35": (
        _c("aruntudaḥ — one who strikes a sore",
           {"root": "tud", "beside": "arus", "role": "karman"},
           note="विध्वरुषोस्तुदः."),
    ),
    "3.2.36": (
        _c("asūryampaśyā rājadārāḥ",
           {"root": "dṛś", "beside": "asūrya", "role": "karman"},
           note="असूर्यललाटयोर्दृशितपोः, यथासंख्यम् — bound here, "
                "seven rules after 3.2.29 refused it. And असूर्य is "
                "an असमर्थसमास: सूर्यं न पश्यन्तीति."),
        _c("the pair crossed",
           {"root": "tap", "beside": "asūrya", "role": "karman"},
           kind="counter",
           note="ललाट goes with तप् and असूर्य with दृश्, not "
                "either with either."),
    ),
    "3.2.37": (
        _c("pāṇindhamāḥ panthānaḥ — roads that make one blow on his "
           "hands", {"word": "pāṇindhama"},
           note="निपात्यन्ते — and this one shows why: पाणयो ध्मायन्त "
                "एष्विति, the companion is the PLACE and not the "
                "object, so no rule of the run could reach it."),
    ),
    "3.2.38": (
        _c("priyaṃvadaḥ — one who speaks kindly",
           {"root": "vad", "beside": "priya", "role": "karman"},
           note="प्रियवशे वदः खच्. खकारो मुमर्थः; चकारः खचि ह्रस्वः "
                "इति विशेषणार्थः; प्रत्ययान्तरकरणमुत्तरार्थम्."),
    ),
    "3.2.39": (
        _c("parantapaḥ — scorcher of foes",
           {"root": "tap", "beside": "para", "role": "karman"},
           note="द्विषत्परयोस्तापेः — द्वयोरपि ग्रहणम्, both roots "
                "spelt alike are meant, unlike 3.2.28's causative "
                "only. And द्वितकारको निर्देशः keeps the feminine out."),
    ),
    "3.2.40": (
        _c("vācaṃyamaḥ — under a vow of silence",
           {"root": "yam", "beside": "vāc", "role": "karman",
            "sense": "vrata"},
           note="वाचि यमो व्रते — व्रत इति शास्त्रितो नियम उच्यते."),
        _c("vāgyāmaḥ — no vow meant",
           {"root": "yam", "beside": "vāc", "role": "karman"},
           kind="counter", note="व्रत इति किम्?"),
    ),
    "3.2.41": (
        _c("puraṃdaraḥ — breaker of strongholds",
           {"root": "dṝ", "beside": "pur", "role": "karman"},
           note="पूःसर्वयोर्दारिसहोः, यथासंख्यम्. SCOPE: भगे च दारेः, "
                "भगन्दरः."),
    ),
    "3.2.42": (
        _c("kūlaṃkaṣā nadī — a river that scours its banks",
           {"root": "kaṣ", "beside": "kūla", "role": "karman"},
           note="सर्वकूलाभ्रकरीषेषु कषः."),
    ),
    "3.2.43": (
        _c("bhayaṃkaraḥ", {"root": "kṛ", "beside": "bhaya",
                           "role": "karman"},
           note="मेघर्तिभयेषु कृञः."),
        _c("abhayaṃkaraḥ — reached through 1.1.72",
           {"root": "kṛ", "beside": "abhaya", "role": "karman"},
           note="उपपदविधौ भयादिग्रहणं तदन्तविधिं प्रयोजयति — naming "
                "भय reaches what ENDS in भय, and 1.1.72 येन "
                "विधिस्तदन्तस्य is codified, so it is asked."),
    ),
    "3.2.44": (
        _c("kṣemakāraḥ, and kṣemaṃkaraḥ beside it",
           {"root": "kṛ", "beside": "kṣema", "role": "karman"},
           note="क्षेमप्रियमद्रेऽण् च — चकारात् खच्च, so both stand. "
                "वेति वक्तव्ये पुनरण्ग्रहणं हेत्वादिषु "
                "टप्रतिषेधार्थम्, keeping 3.2.20's ट out."),
    ),
    "3.2.45": (
        _c("āśitaṃbhavaḥ odanaḥ — the rice by which one is fed",
           {"root": "bhū", "beside": "āśita", "role": "sup",
            "sense": "karaṇa-bhāva"},
           note="आशिते भुवः करणभावयोः — two senses at once, the means "
                "and the act. अत्र सुपीत्युपतिष्ठते."),
    ),
    "3.2.46": (
        _c("patiṃvarā kanyā — a girl who chooses her husband",
           {"root": "vṛ", "beside": "pati", "role": "sup",
            "sense": "saṃjñā"},
           note="संज्ञायां भृतॄवृजिधारिसहितनिषु — कर्मणीति सुपीति च "
                "प्रकृतं संज्ञावशाद् यथासंभवं संबध्यते."),
        _c("kuṭumbabhāraḥ — no name meant",
           {"root": "bhṛ", "beside": "kuṭumba", "role": "sup"},
           kind="counter", note="संज्ञायामिति किम्?"),
    ),
    "3.2.47": (
        _c("sutaṃgamaḥ — a proper name",
           {"root": "gam", "beside": "suta", "role": "sup",
            "sense": "saṃjñā"},
           note="गमश्च — योगविभाग उत्तरार्थः, as at 3.1.147."),
    ),
    "3.2.48": (
        _c("dūragaḥ — one who goes far",
           {"root": "gam", "beside": "dūra", "role": "karman"},
           note="अन्तात्यन्ताध्वदूरपारसर्वानन्तेषु डः. डकारः "
                "टिलोपार्थः, and संज्ञायामिति नानुवर्तते — the "
                "condition of 3.2.46 stops here."),
        _c("uragaḥ — added by a vārttika",
           {"root": "gam", "beside": "uras", "role": "karman"},
           note="उरसो लोपश्च — and the vṛtti then declines to close "
                "the list at all: डप्रकरणेऽन्येष्वपि दृश्यते."),
    ),
    "3.2.49": (
        _c("śatruhaḥ — may he kill his enemies",
           {"root": "han", "beside": "śatru", "role": "karman",
            "sense": "āśis"},
           note="आशिषि हनः."),
        _c("śatrughātaḥ — no blessing meant",
           {"root": "han", "beside": "śatru", "role": "karman"},
           kind="counter", note="आशिषीति किम्?"),
    ),
    "3.2.50": (
        _c("tamo'pahaḥ sūryaḥ — the sun, dispeller of dark",
           {"root": "han", "beside": "tamas", "role": "karman",
            "upasarga": "apa"},
           note="अपे क्लेशतमसोः — अनाशीरर्थ आरम्भः, the rule reaching "
                "the sense 3.2.49 left out."),
    ),
    "3.2.51": (
        _c("kumāraghātī — a killer of children",
           {"root": "han", "beside": "kumāra", "role": "karman"},
           note="कुमारशीर्षयोर्णिनिः — निपातनाच्छिरसः शीर्षभावः, "
                "शिरस् becoming शीर्ष by this fixing and by no rule."),
    ),
    "3.2.52": (
        _c("patighnī vṛṣalī — marked as husband-killing",
           {"root": "han", "beside": "pati", "role": "karman",
            "sense": "lakṣaṇa"},
           note="लक्षणे जायापत्योष्टक् — and the vṛtti offers two "
                "readings, लक्षणवति कर्तरि and लक्षणे द्योत्ये, "
                "settling neither since both give this form."),
    ),
    "3.2.53": (
        _c("śleṣmaghnaṃ madhu — honey, which kills phlegm",
           {"root": "han", "beside": "śleṣman", "role": "karman",
            "agent": "amanuṣya"},
           note="अमनुष्यकर्तृके च. अमनुष्यकर्तृक इति किम्? आखुघातः "
                "शूद्रः. DEBT: चौरघातो हस्ती is answered by 3.3.113, "
                "which is not codified."),
    ),
    "3.2.54": (
        _c("hastighnaḥ manuṣyaḥ — a man able to kill an elephant",
           {"root": "han", "beside": "hastin", "role": "karman",
            "sense": "śakti"},
           note="शक्तौ हस्तिकपाटयोः — मनुष्यकर्तृकार्थ आरम्भः is the "
                "REASON for the rule; शक्तौ is the condition in it. "
                "शक्ताविति किम्? हस्तिघातः."),
    ),
    "3.2.55": (
        _c("pāṇighaḥ — a striker by trade", {"word": "pāṇigha"},
           note="पाणिघताडघौ शिल्पिनि — a निपातन fixing three things at "
                "once: the affix, the टि dropped, and the घ."),
    ),
    "3.2.56": (
        _c("āḍhyaṃkaraṇam — the means of making one rich",
           {"root": "kṛ", "beside": "āḍhya", "role": "karman",
            "sense": "karaṇa", "cvi_sense": True},
           note="च्व्यर्थेष्वच्वौ कृञः करणे ख्युन् — अनाढ्यमाढ्यं "
                "कुर्वन्त्यनेन."),
        _c("āḍhyīkurvanti — the cvi actually present",
           {"root": "kṛ", "beside": "āḍhya", "role": "karman",
            "sense": "karaṇa", "cvi_sense": True, "cvi_ending": True},
           kind="counter", note="अच्वाविति किम्? — the rule wants the "
                                "MEANING without the affix."),
    ),
    "3.2.57": (
        _c("āḍhyaṃbhaviṣṇuḥ, and āḍhyaṃbhāvukaḥ beside it",
           {"root": "bhū", "beside": "āḍhya", "role": "sup",
            "cvi_sense": True},
           note="कर्तरि भुवः खिष्णुच्खुकञौ — both affixes stand. "
                "कर्तरीति किम्? करणे मा भूत् — the agent here, where "
                "3.2.56 wanted the instrument."),
    ),
    "3.2.58": (
        _c("ghṛtaspṛk — one who touches ghee",
           {"root": "spṛś", "beside": "ghṛta", "role": "sup"},
           note="स्पृशोऽनुदके क्विन् — and the companion is any सुबन्त, "
                "which the vṛtti reasons out: कर्तृप्रचयार्थं "
                "विज्ञायते, so मन्त्रस्पृक् has an instrument beside."),
        _c("udakasparśaḥ — the one word refused",
           {"root": "spṛś", "beside": "udaka", "role": "sup"},
           kind="counter", note="अनुदक इति किम्?"),
    ),
    "3.2.59": (
        _c("prāṅ — facing east",
           {"root": "añc", "beside": "pra", "role": "sup"},
           note="अञ्चतेः सुबन्तमात्र उपपदे — one of the three roots "
                "this sūtra names, as against the five words it fixes."),
        _c("yuṅ — from the bare root", {"root": "yuj"},
           note="युजेः क्रुञ्चेश्च केवलादेव — with a companion it is "
                "3.2.61's क्विप् instead, अश्वयुक्."),
        _c("ṛtvik — a priest", {"word": "ṛtvij"},
           note="रूढिरेषा यथाकथंचिदनुगन्तव्या — three derivations "
                "offered and none chosen: the word is settled."),
    ),
    "3.2.60": (
        _c("tādṛśaḥ, and tādṛk beside it",
           {"root": "dṛś", "beside": "tad", "role": "sup"},
           note="त्यदादिषु दृशोऽनालोचने कञ् च — चकारात् क्विन् च, both "
                "affixes. कञो ञकारो विशेषणार्थः, for 4.1.15."),
        _c("taddarśaḥ — where seeing IS meant",
           {"root": "dṛś", "beside": "tad", "role": "sup",
            "sense": "ālocana"}, kind="counter",
           note="अनालोचन इति किम्? — त्यादृगादयो रूढिशब्दप्रकारा, "
                "नैवात्र दर्शनक्रिया विद्यते."),
    ),
    "3.2.61": (
        _c("mitradviṭ — one who hates a friend",
           {"root": "dviṣ", "beside": "mitra", "role": "sup"},
           note="सत्सूद्विष… उपसर्गेऽपि क्विप्. उपसर्गग्रहणं "
                "ज्ञापनार्थम् — a ज्ञापक about every other rule."),
        _c("pradviṭ — with a preverb",
           {"root": "dviṣ", "beside": "pra", "role": "sup",
            "upasarga": "pra"},
           note="उपसर्गेऽपि — both stand, which is what the rule adds."),
    ),
    "3.2.62": (
        _c("ardhabhāk — one who takes half",
           {"root": "bhaj", "beside": "ardha", "role": "sup"},
           note="भजो ण्विः."),
    ),
    "3.2.63": (
        _c("turāṣāṭ — overpowering the strong",
           {"root": "sah", "beside": "turā", "role": "sup",
            "chandasi": True},
           note="छन्दसि सहः."),
    ),
    "3.2.64": (
        _c("praṣṭhavāṭ — drawing the foremost",
           {"root": "vah", "beside": "praṣṭha", "role": "sup",
            "chandasi": True},
           note="वहश्च — योगविभाग उत्तरार्थः."),
    ),
    "3.2.65": (
        _c("kavyavāhanaḥ — carrier of offerings to the fathers",
           {"root": "vah", "beside": "kavya", "chandasi": True},
           note="कव्यपुरीषपुरीष्येषु ञ्युट्."),
    ),
    "3.2.66": (
        _c("havyavāhanaḥ — within the line",
           {"root": "vah", "beside": "havya", "chandasi": True},
           note="हव्येऽनन्तः पादम् — the one PROSODIC condition in the "
                "pāda."),
        _c("havyavāṭ — at the quarter's end",
           {"root": "vah", "beside": "havya", "chandasi": True,
            "pada_final": True}, kind="counter",
           note="अनन्तः पादमिति किम्? हव्यवाडग्निरजरः पिता नः."),
    ),
    "3.2.67": (
        _c("gojāḥ — born of cows",
           {"root": "jan", "beside": "go", "role": "sup",
            "chandasi": True},
           note="जनसनखनक्रमगमो विट् — and two of the five names cover "
                "a pair of roots each, द्वयोरपि ग्रहणम्."),
    ),
    "3.2.68": (
        _c("āmāt — one who eats raw food",
           {"root": "ad", "beside": "āma", "role": "sup"},
           note="अदोऽनन्ने — and छन्दसीति निवृत्तम्, the Vedic "
                "condition stopping here."),
        _c("annādaḥ — the one word refused",
           {"root": "ad", "beside": "anna", "role": "sup"},
           kind="counter", note="अनन्न इति किम्?"),
    ),
    "3.2.69": (
        _c("kravyāt — an eater of raw flesh",
           {"root": "ad", "beside": "kravya", "role": "sup"},
           note="क्रव्ये च — पूर्वेणैव सिद्धे वचनम् असरूपबाधनार्थम्, "
                "keeping 3.1.94's असरूप अण् out. And क्रव्यादः is a "
                "different word with a different sense."),
    ),
    "3.2.70": (
        _c("kāmadughā dhenuḥ — the cow that milks out wishes",
           {"root": "duh", "beside": "kāma", "role": "sup"},
           note="दुहः कब् घश्च — and दुह् is among 3.2.61's twelve "
                "too, so the narrower rule has to win."),
    ),
    "3.2.71": (
        _c("śvetavā indraḥ — Indra, whom white horses draw",
           {"root": "vah", "beside": "śveta", "role": "karman",
            "mantra": True},
           note="मन्त्रे … ण्विन्. धातूपपदसमुदाया निपात्यन्ते "
                "अलाक्षणिककार्यसिद्ध्यर्थम्, प्रत्ययस्तु विधीयत एव — "
                "the compounds fixed, the affix prescribed."),
    ),
    "3.2.72": (
        _c("avayāḥ — one who sacrifices away",
           {"root": "yaj", "upasarga": "ava", "mantra": True},
           note="अवे यजः — योगविभाग उत्तरार्थः."),
    ),
    "3.2.73": (
        _c("upayaṭ — one who sacrifices in addition",
           {"root": "yaj", "upasarga": "upa", "chandasi": True},
           note="विजुपे छन्दसि — यजेर्नियमार्थमेतत्, a rule that "
                "RESTRICTS rather than provides: उपयजेश्छन्दस्येव, न "
                "भाषायाम्."),
    ),
    "3.2.74": (
        _c("sudāmā — generous",
           {"root": "dā", "beside": "su", "role": "sup",
            "chandasi": True},
           note="आतो मनिन्क्वनिब्वनिपश्च — and चकाराद् विज् भवति, a "
                "fourth affix out of the च."),
    ),
    "3.2.75": (
        _c("suśarmā — well-sheltering",
           {"root": "śṛ", "beside": "su", "attested": True},
           note="अन्येभ्योऽपि दृश्यन्ते. अपिशब्दः "
                "सर्वोपाधिव्यभिचारार्थः, and निरुपपदादपि भवति — open "
                "at every joint. दृशिग्रहणं प्रयोगानुसरणार्थम् is what "
                "holds it back: it follows usage rather than making "
                "forms."),
    ),
    "3.2.76": (
        _c("ukhāsrat — slipping from the pot",
           {"root": "sraṃs", "beside": "ukhā", "attested": True,
            "wants": "kvip"},
           note="क्विप् च — सर्वधातुभ्यः, छन्दसि भाषायां च. Named by "
                "`wants` because 3.2.75 is open too and reaches the "
                "same root with other affixes."),
    ),
    "3.2.77": (
        _c("śaṃsthaḥ — standing in welfare",
           {"root": "sthā", "beside": "śam", "role": "sup"},
           note="स्थः क च — बाधकबाधनार्थं पुनर्वचनम्, beating 3.2.14's "
                "अच्. Elsewhere 3.2.4 already gives the same क."),
    ),
    "3.2.78": (
        _c("uṣṇabhojī — one who eats his food hot",
           {"root": "bhuj", "beside": "uṣṇa", "role": "sup",
            "sense": "tācchīlya"},
           note="सुप्यजातौ णिनिस्ताच्छील्ये. पुनः सुब्ग्रहणम् "
                "उपसर्गनिवृत्त्यर्थम् — a word repeated to END an "
                "anuvṛtti."),
        _c("brāhmaṇānām āmantrayitā — a class-word beside",
           {"root": "āmantray", "beside": "brāhmaṇa", "role": "sup",
            "sense": "tācchīlya", "jati": True}, kind="counter",
           note="अजाताविति किम्?"),
    ),
    "3.2.79": (
        _c("uṣṭrakrośī — one who cries like a camel",
           {"root": "kruś", "beside": "uṣṭra", "role": "sup",
            "upamana": "kartṛ"},
           note="कर्तर्युपमाने — अताच्छील्यार्थ आरम्भः."),
    ),
    "3.2.80": (
        _c("sthaṇḍilaśāyī — vowed to sleep on bare ground",
           {"root": "śī", "beside": "sthaṇḍila", "role": "sup",
            "sense": "vrata"},
           note="व्रते — समुदायोपाधिश्चायम्, the condition on the "
                "WHOLE and not on a part."),
    ),
    "3.2.81": (
        _c("kṣīrapāyiṇaḥ uśīnarāḥ — the milk-drinking Uśīnaras",
           {"root": "pā", "beside": "kṣīra", "role": "sup",
            "sense": "ābhīkṣṇya"},
           note="बहुलमाभीक्ष्ण्ये — आभीक्ष्ण्यं पौनःपुन्यम्, "
                "ताच्छील्याद् अन्यत्, expressly not 3.2.78's sense."),
    ),
    "3.2.82": (
        _c("darśanīyamānī — one who thinks himself good-looking",
           {"root": "man", "beside": "darśanīya", "role": "sup"},
           note="मनः — मन्यतेर्ग्रहणम्, न मनुतेः, and the reason lies "
                "one rule downstream."),
    ),
    "3.2.83": (
        _c("paṇḍitaṃmanyaḥ — thinking himself learned",
           {"root": "man", "beside": "paṇḍita", "role": "sup",
            "sense": "ātmamāna"},
           note="आत्ममाने खश् च — चकाराद् णिनिश्च, so पण्डितमानी "
                "stands beside it."),
    ),
    "3.2.84": (
        _c("what भूते covers", {},
           note="An अधिकार, not a provision: it adds no affix and puts "
                "3.2.85 to 3.2.122 under a condition none of them "
                "states. धात्वर्थे भूत इति विज्ञायते."),
        _c("whether 3.2.90 falls under it", {"sutra_id": "3.2.90"},
           note="यदित ऊर्ध्वम् अनुक्रमिष्यामो भूत इत्येवं तद् "
                "वेदितव्यम्."),
    ),
    "3.2.85": (
        _c("agniṣṭomayājī — one who has sacrificed with the Agniṣṭoma",
           {"root": "yaj", "beside": "agniṣṭoma", "role": "karaṇa",
            "past": True},
           note="करणे यजः — णिनिरनुवर्तते, न खश्."),
        _c("agniṣṭomena yajate — sacrificing now",
           {"root": "yaj", "beside": "agniṣṭoma", "role": "karaṇa"},
           kind="counter", note="भूत इति किम्? — 3.2.84's heading."),
    ),
    "3.2.86": (
        _c("pitṛvyaghātī — one who has killed his uncle",
           {"root": "han", "beside": "pitṛvya", "role": "karman",
            "past": True, "sense": "kutsā"},
           note="कर्मणि हनः, with the vārttika कुत्सितग्रहणं कर्तव्यम् "
                "codified: इह मा भूत् चौरं हतवान्."),
    ),
    "3.2.87": (
        _c("brahmahā — a brahmin-killer",
           {"root": "han", "beside": "brahman", "role": "karman",
            "past": True},
           note="ब्रह्मभ्रूणवृत्रेषु क्विप् — नियमार्थम्, and the "
                "restriction is FOURFOLD, got by dragging 3.2.88's "
                "बहुल backward."),
    ),
    "3.2.88": (
        _c("mātṛhā — a matricide",
           {"root": "han", "beside": "mātṛ", "role": "karman",
            "past": True, "chandasi": True},
           note="बहुलं छन्दसि — पूर्वेण नियमाद् अप्राप्तः क्विप् "
                "विधीयते, giving back what the नियम shut out."),
    ),
    "3.2.89": (
        _c("puṇyakṛt — a doer of good",
           {"root": "kṛ", "beside": "puṇya", "role": "karman",
            "past": True},
           note="सुकर्मपापमन्त्रपुण्येषु कृञः — नियमार्थ आरम्भः, but "
                "THREEFOLD: धातुनियमं वर्जयित्वा, so शास्त्रकृत् too."),
    ),
    "3.2.90": (
        _c("somasut — a presser of soma",
           {"root": "su", "beside": "soma", "role": "karman",
            "past": True},
           note="सोमे सुञः — चतुर्विधो नियमः, the root restricted here."),
    ),
    "3.2.91": (
        _c("agnicit — one who has piled the fire-altar",
           {"root": "ci", "beside": "agni", "role": "karman",
            "past": True},
           note="अग्नौ चेः — पूर्ववच्चतुर्विधो नियमः."),
    ),
    "3.2.92": (
        _c("śyenacit — the hawk-shaped altar",
           {"root": "ci", "beside": "śyena", "role": "karman",
            "past": True, "names_a": "agni"},
           note="कर्मण्यग्न्याख्यायाम् — समुदायेन अग्न्याख्या गम्यते, "
                "and आख्याग्रहणं रूढिसंप्रत्ययार्थम्."),
    ),
    "3.2.93": (
        _c("somavikrayī — a seller of soma",
           {"root": "krī", "beside": "soma", "role": "karman",
            "past": True, "upasarga": "vi", "sense": "kutsā"},
           note="कर्मणीनिविक्रयः — पुनः कर्मग्रहणं कर्तुः "
                "कुत्सानिमित्ते कर्मणि यथा स्यात्. इह न भवति "
                "धान्यविक्रायः."),
    ),
    "3.2.94": (
        _c("merudṛśvā — one who has seen Meru",
           {"root": "dṛś", "beside": "meru", "role": "karman",
            "past": True},
           note="दृशेः क्वनिप् — पुनर्वचनं प्रत्ययान्तरनिवृत्त्यर्थम्, "
                "a repetition that shuts out one rule's OTHER affixes."),
    ),
    "3.2.95": (
        _c("rājayudhvā — one who has fought a king",
           {"root": "yudh", "beside": "rājan", "role": "karman",
            "past": True},
           note="राजनि युधिकृञः — ननु च युधिरकर्मकः? "
                "अन्तर्भावितण्यर्थः सकर्मको भवति."),
    ),
    "3.2.96": (
        _c("sahayudhvā — one who has fought alongside",
           {"root": "yudh", "beside": "saha", "past": True},
           note="सहे च — असत्त्ववाचित्वाद् नोपपदं कर्मणा विशेष्यते."),
    ),
    "3.2.97": (
        _c("upasarajaḥ — born in the season of approach",
           {"root": "jan", "beside": "upasara", "role": "adhikaraṇa",
            "past": True},
           note="सप्तम्यां जनेर्डः."),
    ),
    "3.2.98": (
        _c("buddhijaḥ — born of thought",
           {"root": "jan", "beside": "buddhi", "role": "apādāna",
            "past": True},
           note="पञ्चम्यामजातौ. अजाताविति किम्? हस्तिनो जातः."),
    ),
    "3.2.99": (
        _c("prajāḥ — creatures, the born-forth",
           {"root": "jan", "beside": "pra", "upasarga": "pra",
            "sense": "saṃjñā", "past": True},
           note="उपसर्गे च संज्ञायाम् — समुदायोपाधिः संज्ञा, the third "
                "of that shape in this pāda."),
    ),
    "3.2.100": (
        _c("pumanujaḥ — born after a male",
           {"root": "jan", "beside": "puṃs", "upasarga": "anu",
            "role": "karman", "past": True},
           note="अनौ कर्मणि."),
    ),
    "3.2.101": (
        _c("ajaḥ, dvijāḥ — seen without the conditions",
           {"root": "jan", "beside": "a", "attested": True,
            "past": True},
           note="अन्येष्वपि दृश्यते — and the vṛtti undoes all four "
                "rules before it in turn. अपिशब्दः "
                "सर्वोपाधिव्यभिचारार्थः, and even from another root: "
                "परिखा."),
    ),
    "3.2.102": (
        _c("kṛtam, kṛtavān — the affix named निष्ठा",
           {"affix": "kta"},
           note="निष्ठा — a संज्ञा rule. Which affixes bear the name "
                "is 1.1.26's, asked and not restated."),
        _c("kta where the act is NOT past — the rule refuses",
           {"affix": "kta", "past": False},
           note="भूते. Not a counter-example: 3.2.102 does act here, "
                "and what it does is refuse. A rule may name itself "
                "in a refusal exactly when refusing is the whole of "
                "what it did — which is why an affix bearing no such "
                "name comes back nameless instead, 1.1.26 having been "
                "what withheld it."),
    ),
    "3.2.103": (
        _c("yajvā — one who has sacrificed",
           {"root": "yaj", "past": True},
           note="सुयजोर्ङ्वनिप् — no companion wanted at all."),
    ),
    "3.2.104": (
        _c("jaran — aged, with jīrṇaḥ beside it",
           {"root": "jṝ", "past": True},
           note="जीर्यतेरतृन् — वासरूपेण निष्ठा, so 3.1.94 lets the "
                "other affix stand too."),
    ),
    "3.2.105": (
        _c("dadarśa — the perfect, in the Veda", {"chandasi": True},
           note="छन्दसि लिट् — and 3.4.6 gives it already: धातुसंबन्धे "
                "स विधिः, अयं त्वविशेषेण."),
    ),
    "3.2.106": (
        _c("suṣuvāṇaḥ — having pressed soma",
           {"chandasi": True, "wants": "kānac"},
           note="लिटः कानज् वा — optional, so the ordinary perfect "
                "still stands: न च भवति अहं सूर्यमुभयतो ददर्श. And "
                "लिड्ग्रहणं किम्? लिण्मात्रस्य यथा स्यात् — naming "
                "लिट् again makes the substitution reach EVERY लिट्."),
    ),
    "3.2.107": (
        _c("papivān — having drunk",
           {"chandasi": True, "wants": "kvasu"},
           note="क्वसुश्च — योगविभाग उत्तरार्थः, split from 3.2.106 "
                "for the rule after, which wants क्वसु and not कानच्."),
    ),
    "3.2.108": (
        _c("upasedivān — having approached", {"root": "sad"},
           note="भाषायां सदवसश्रुवः — क्वसु in ordinary speech, by "
                "choice. आदेशविधानाद् एव लिडपि तद्विषयोऽनुमीयते."),
    ),
    "3.2.109": (
        _c("anūcānaḥ — one who has recited", {"word": "anūcāna"},
           note="वचेर् अनुपूर्वात् कर्तरि कानज् निपात्यते — and the "
                "other two words of this sūtra fix a DIFFERENT affix."),
        _c("upeyivān — having approached", {"word": "upeyivān"},
           note="उपपूर्वाद् इणः क्वसुः, with a chain of consequences "
                "the vṛtti works out. न चात्रोपसर्गस्तन्त्रम्."),
    ),
    "3.2.110": (
        _c("akārṣīt — he did", {},
           note="लुङ् — भूतेऽर्थे, the widest of the tense rules."),
    ),
    "3.2.111": (
        _c("akarot — he did, before today", {"anadyatana": True},
           note="अनद्यतने लङ् — and बहुव्रीहिनिर्देशः किमर्थः? so a "
                "MIXED case is left out."),
    ),
    "3.2.112": (
        _c("abhijānāsi … vatsyāmaḥ — the FUTURE ending for a past act",
           {"beside": "abhijānāsi", "anadyatana": True},
           note="अभिज्ञावचने लृट्, लङोऽपवादः — what is remembered was "
                "future to the remembering. वचनग्रहणं पर्यायार्थम्, "
                "so स्मरसि and बुध्यसे count too."),
    ),
    "3.2.113": (
        _c("abhijānāsi yat … avasāma — the refusal, and what supplies",
           {"beside": "abhijānāsi", "anadyatana": True,
            "with_yad": True},
           note="न यदि — पूर्वेण प्राप्तः प्रतिषिध्यते. The answer "
                "names 3.2.111, which SUPPLIES the ending, and carries "
                "this rule as what blocked the nearer one."),
    ),
    "3.2.114": (
        _c("… vatsyāmaḥ, tatraudanaṃ bhokṣyāmahe",
           {"beside": "abhijānāsi", "anadyatana": True,
            "sakanksa": True},
           note="विभाषा साकाङ्क्षे — यदीति नानुवर्तते, उभयत्र "
                "विभाषेयम्, so it holds with यद् as well."),
    ),
    "3.2.115": (
        _c("cakāra — he did, unseen",
           {"anadyatana": True, "paroksa": True},
           note="परोक्षे लिट् — ननु च धात्वर्थः सर्वः परोक्ष एव? and "
                "the answer: प्रत्यक्षाभिमानः, what speakers take "
                "themselves to see."),
    ),
    "3.2.116": (
        _c("iti ha akarot, and iti ha cakāra",
           {"beside": "ha", "anadyatana": True, "paroksa": True},
           note="हशश्वतोर्लङ् च — चकाराल् लिट् च, so both endings."),
    ),
    "3.2.117": (
        _c("agacchad devadattaḥ? — asked about lately",
           {"anadyatana": True, "paroksa": True, "question": True,
            "recent": True},
           note="प्रश्ने चासन्नकाले. प्रश्न इति किम्? जगाम देवदत्तः."),
    ),
    "3.2.118": (
        _c("naḍena sma purādhīyate — the PRESENT ending for the past",
           {"beside": "sma", "anadyatana": True, "paroksa": True},
           note="लट् स्मे, लिटोऽपवादः."),
    ),
    "3.2.119": (
        _c("evaṃ sma pitā bravīti — and where it was NOT unseen",
           {"beside": "sma", "anadyatana": True},
           note="अपरोक्षे च — which is why परोक्ष is tri-state: two "
                "rules take opposite sides of it."),
    ),
    "3.2.120": (
        _c("nanu karomi bhoḥ — answering a question",
           {"beside": "nanu", "answer": True},
           note="ननौ पृष्टप्रतिवचने, लुङोऽपवादः. अनद्यतने परोक्षे इति "
                "निवृत्तम् — two conditions stop running here."),
    ),
    "3.2.121": (
        _c("na karomi bhoḥ, or nākārṣam",
           {"beside": "na", "answer": True},
           note="नन्वोर्विभाषा — the option is real, so both endings."),
    ),
    "3.2.122": (
        _c("avātsuriha purā chātrāḥ",
           {"beside": "purā", "anadyatana": True},
           note="पुरि लुङ् चास्मे — and अनद्यतनग्रहणम् इह "
                "मण्डूकप्लुत्या अनुवर्तते: the condition arrives by "
                "LEAPING over the rules between."),
    ),
    "3.2.123": (
        _c("pacati — he is cooking", {"time": "vartamāna"},
           note="वर्तमाने लट् — प्रारब्धोऽपरिसमाप्तश्च वर्तमानः, and "
                "this is where 3.2.84's भूते heading stops."),
    ),
    "3.2.124": (
        _c("pacantaṃ devadattaṃ paśya", {"aprathama": True},
           note="लटः शतृशानचावप्रथमासमानाधिकरणे — and लड्ग्रहणम् "
                "अधिकविधानार्थम्, a repetition that WIDENS: सन् "
                "ब्राह्मणः, अधीयानः."),
    ),
    "3.2.125": (
        _c("he pacan — you there, cooking", {"sambodhana": True},
           note="संबोधने च — प्रथमासमानाधिकरणार्थ आरम्भः, reaching "
                "past what 3.2.124 shut out."),
    ),
    "3.2.126": (
        _c("śayānā bhuñjate yavanāḥ", {"lakshana_hetu": True},
           note="लक्षणहेत्वोः क्रियायाः. क्रियाया इति किम्? "
                "द्रव्यगुणयोर्मा भूत्. And लक्षणहेत्वोरिति निर्देशः "
                "पूर्वनिपातव्यभिचारलिङ्गम् — the compound's order is "
                "itself the evidence."),
    ),
    "3.2.127": (
        _c("śatṛ bears the name सत्", {"affix": "śatṛ"},
           note="तौ सत् — तौग्रहणम् उपाध्यसंसर्गार्थम्, so the name "
                "attaches at large: ब्राह्मणस्य करिष्यन् too."),
    ),
    "3.2.128": (
        _c("pavamānaḥ — flowing clear", {"root": "pū"},
           note="पूङ्यजोः शानन् — and तृन्निति प्रत्ययाहारनिर्देशात्, "
                "a pratyāhāra whose members are RULES: from 3.2.124 "
                "to the न of तृन् at 3.2.135."),
    ),
    "3.2.129": (
        _c("katīha pacamānāḥ — how many can cook?",
           {"sense": "tācchīlya"},
           note="ताच्छील्यवयोवचनशक्तिषु चानश् — ताच्छील्यं "
                "तत्स्वभावता, the same gloss 3.2.78 gave, so the "
                "field is shared."),
    ),
    "3.2.130": (
        _c("adhīyan pārāyaṇam — reciting with ease",
           {"root": "iṅ", "akrcchri": True},
           note="इङ्धार्योः शत्रकृच्छ्रिणि. अकृच्छ्रिणीति किम्? "
                "कृच्छ्रेणाधीते."),
    ),
    "3.2.131": (
        _c("dviṣan — hating, of a foe",
           {"root": "dviṣ", "amitra": True},
           note="द्विषोऽमित्रे. अमित्र इति किम्? द्वेष्टि भार्या "
                "पतिम्."),
    ),
    "3.2.132": (
        _c("sarve sunvantaḥ — all the pressers",
           {"root": "su", "yajna": True},
           note="सुञो यज्ञसंयोगे — संयोगग्रहणं "
                "प्रधानकर्तृप्रतिपत्त्यर्थम्, याजकेषु मा भूत्."),
    ),
    "3.2.133": (
        _c("arhan — deserving, worthy",
           {"root": "arh", "sense": "praśaṃsā"},
           note="अर्हः प्रशंसायाम्. प्रशंसायामिति किम्? अर्हति चौरो "
                "वधम्."),
    ),
    "3.2.134": (
        _c("what the heading covers", {},
           note="आ क्वेस्तच्छीलतद्धर्मतत्साधुकारिषु — a heading, and "
                "its extent is named by a RULE, आ क्वेः, inclusive by "
                "अभिविधौ चायम् आङ्."),
        _c("whether 3.2.139 falls under it", {"sutra_id": "3.2.139"},
           note="यानित ऊर्ध्वम् अनुक्रमिष्यामः तच्छीलादिषु कर्तृषु ते "
                "वेदितव्याः."),
    ),
    "3.2.135": (
        _c("kartā — a doer, by habit or duty or well", {"root": "kṛ"},
           note="तृन्, सर्वधातुभ्यः — the widest of the run, and the "
                "vṛtti gives an example under each of the heading's "
                "three senses."),
    ),
    "3.2.136": (
        _c("sahiṣṇuḥ — patient by nature", {"root": "sah"},
           note="अलंकृञ्… इष्णुच्. SCOPE: अलंकृञो मण्डनार्थाद् युचः "
                "पूर्वविप्रतिषेधेन — a PRIOR rule beating a later one."),
    ),
    "3.2.137": (
        _c("dhārayiṣṇavaḥ — upholding",
           {"root": "dhṛ", "causative": True, "chandasi": True},
           note="णेश्छन्दसि — from the causative stem, in the Veda."),
    ),
    "3.2.138": (
        _c("bhaviṣṇuḥ — becoming, in the Veda",
           {"root": "bhū", "chandasi": True},
           note="भुवश्च, and छन्दसि विषये: the Vedic condition runs on "
                "from 3.2.137 and stops only at 3.2.139."),
    ),
    "3.2.139": (
        _c("bhūṣṇuḥ — thriving, outside the Veda", {"root": "bhū"},
           note="ग्लाजिस्थश्च क्स्नुः — छन्दसीति निवृत्तम्, so the "
                "same root divides by register: भविष्णुः in the Veda, "
                "भूष्णुः outside."),
        _c("jiṣṇuḥ — victorious", {"root": "ji"},
           note="गिच् चायं प्रत्ययः, न कित् — three consequences, and "
                "the vṛtti puts them in a verse."),
    ),
    "3.2.140": (
        _c("gṛdhnuḥ — greedy", {"root": "gṛdh"},
           note="त्रसिगृधिधृषिक्षिपेः क्नुः."),
    ),
    "3.2.141": (
        _c("śamī — calm by nature", {"root": "śam"},
           note="शमित्यष्टाभ्यो घिनुण् — a गण named by both its ends. "
                "घकार कुत्वार्थः, उकार उच्चारणार्थः, णकारो "
                "वृद्ध्यर्थः: three marks, three jobs."),
    ),
    "3.2.142": (
        _c("dveṣī — hostile", {"root": "dviṣ"},
           note="संपृचानुरुध… — and four root ambiguities settled "
                "first: पृची is रुधादि, लुग्विकरणत्वात्."),
    ),
    "3.2.143": (
        _c("vilāsī — sportive", {"root": "las", "upasarga": "vi"},
           note="वौ कषलसकत्थस्रम्भः."),
    ),
    "3.2.144": (
        _c("apalāṣī — craving", {"root": "laṣ", "upasarga": "apa"},
           note="अपे च लषः — चकाराद् वौ च, the च borrowing वि from "
                "3.2.143."),
    ),
    "3.2.145": (
        _c("pralāpī — given to prattling",
           {"root": "lap", "upasarga": "pra"},
           note="प्रे लपसृद्रुमथवदवसः — and वस् is निवासे, "
                "लुग्विकरणत्वात्, the same ground as 3.2.142's पृची."),
    ),
    "3.2.146": (
        _c("nindakaḥ — a fault-finder", {"root": "nind"},
           note="ण्वुलैव सिद्धे वुञ्विधानं ज्ञापनार्थम् — ताच्छीलिकेषु "
                "वासरूपन्यायेन तृजादयो न भवन्ति. 3.1.94 is codified, "
                "and this heading suspends it."),
    ),
    "3.2.147": (
        _c("ākrośakaḥ — abusive", {"root": "kruś", "upasarga": "ā"},
           note="देविक्रुशोश्चोपसर्गे — ANY preverb, where the three "
                "rules before each named one. उपसर्ग इति किम्? क्रोष्टा."),
    ),
    "3.2.148": (
        _c("calanaḥ — restless",
           {"akarmaka": True, "sense": "calana-śabda"},
           note="चलनशब्दार्थादकर्मकाद् युच् — no root named at all, "
                "only a meaning. अकर्मकादिति किम्? पठिता विद्याम्."),
    ),
    "3.2.149": (
        _c("vardhanaḥ — thriving",
           {"anudattet": True, "hal_adi": True, "akarmaka": True},
           note="अनुदात्तेतश्च हलादेः — three conditions, and the "
                "vṛtti asks after each. आदिग्रहणं किम्? जुगुप्सनः."),
    ),
    "3.2.150": (
        _c("jvalanaḥ — blazing", {"root": "jval"},
           note="जुचङ्क्रम्य… — जु इति सौत्रो धातुः. And प्रायिकं "
                "चैतद् ज्ञापकम्, क्वचित् समावेश इष्यत एव."),
    ),
    "3.2.151": (
        _c("krodhanaḥ — irascible",
           {"root": "krudh", "sense": "krodha-bhūṣā"},
           note="क्रुधमण्डार्थेभ्यश्च — by MEANING, so रोषणः and "
                "भूषणः stand beside the two named."),
    ),
    "3.2.152": (
        _c("knūyitā — the refusal, and what supplies",
           {"y_final": True, "anudattet": True, "hal_adi": True,
            "akarmaka": True},
           note="न यः — पूर्वेण प्राप्तः प्रतिषिध्यते. The answer "
                "names 3.2.135, which SUPPLIES the तृन्, and carries "
                "this rule as what blocked the nearer one."),
    ),
    "3.2.153": (
        _c("sūditā — a destroyer",
           {"root": "sūd", "anudattet": True, "hal_adi": True,
            "akarmaka": True},
           note="सूददीपदीक्षश्च — needed because वासरूपेण युजपि "
                "प्राप्नोति, the suspension being प्रायिक. SCAR: "
                "मधुसूदनः gets three explanations and no decision."),
    ),
    "3.2.154": (
        _c("kāmukaḥ — desirous", {"root": "kam"},
           note="लषपतपद… उकञ् — and every example the vṛtti gives is "
                "a whole sentence, these forms being quoted from use."),
    ),
    "3.2.155": (
        _c("jalpākaḥ — talkative", {"root": "jalp"},
           note="जल्पभिक्ष… षाकन् — षकारो ङीषर्थः, the ष written for "
                "the feminine वराकी, two adhyāyas away."),
    ),
    "3.2.156": (
        _c("prajavī — swift", {"root": "ju", "upasarga": "pra"},
           note="प्रजोरिनिः."),
    ),
    "3.2.157": (
        _c("jayī — victorious", {"root": "ji", "wants": "ini"},
           note="जिदृक्षिविश्रीण्वम… — क्षि taken in both senses, "
                "प्रसू being षू प्रेरणे. Named by affix because जि is "
                "3.2.139's too, and जिष्णुः stands beside जयी."),
    ),
    "3.2.158": (
        _c("dayāluḥ — compassionate", {"root": "day"},
           note="स्पृहिगृहिपति… आलुच् — and three of the seven are "
                "compounds the sūtra fixes, not roots of a list."),
    ),
    "3.2.159": (
        _c("dhāruḥ — suckling", {"root": "dheṭ"},
           note="दाधेट्सिशदसदो रुः — and 2.3.69's ban on the genitive "
                "does not reach these, उकारप्रश्लेषात्."),
    ),
    "3.2.160": (
        _c("ghasmaraḥ — voracious", {"root": "ghas"},
           note="सृघस्यदः क्मरच्."),
    ),
    "3.2.161": (
        _c("bhaṅguraṃ kāṣṭham — brittle wood", {"root": "bhañj"},
           note="भञ्जभासमिदो घुरच् — घित्त्वात् कुत्वम्. And "
                "भञ्जेः कर्मकर्तरि प्रत्ययः, स्वभावात्."),
    ),
    "3.2.162": (
        _c("viduraḥ paṇḍitaḥ — a knowing man", {"root": "vid"},
           note="विदिभिदिच्छिदेः कुरच् — ज्ञानार्थस्य विदेः ग्रहणम्, "
                "स्वभावात्, the second such argument in two rules."),
    ),
    "3.2.163": (
        _c("itvaraḥ — a goer", {"root": "iṇ"},
           note="इण्नश्जिसर्तिभ्यः क्वरप् — पकारस्तुगर्थः, and 7.2.8 "
                "keeps the इट् out."),
    ),
    "3.2.164": (
        _c("gatvaraḥ — transient",
           {"root": "gam", "wants": "kvarap"},
           note="गत्वरश्च — a निपातन inside the table: the nasal's "
                "loss is fixed, the affix prescribed."),
    ),
    "3.2.165": (
        _c("jāgarūkaḥ — watchful", {"root": "jāgṛ"},
           note="जागुरूकः."),
    ),
    "3.2.166": (
        _c("yāyajūkaḥ — constantly sacrificing",
           {"root": "yaj", "yan_anta": True},
           note="यजजपदशां यङः — after the यङन्त STEM, not the bare "
                "root."),
    ),
    "3.2.167": (
        _c("kamrā yuvatiḥ — a lovely young woman",
           {"root": "kam", "wants": "ra"},
           note="नमिकम्पिस्म्यजसकमहिंसदीपो रः — and कम्रा, कम्प्रा "
                "are the very forms 3.2.153 cites as standing beside "
                "कमना, कम्पना."),
    ),
    "3.2.168": (
        _c("bhikṣuḥ — a mendicant",
           {"root": "bhikṣ", "san_anta": True},
           note="सनाशंसभिक्ष उः — and सन् is the AFFIX, on either of "
                "two grounds the vṛtti offers without choosing."),
    ),
    "3.2.169": (
        _c("icchuḥ — desirous", {"root": "iṣ"},
           note="विन्दुरिच्छुः — each with its own irregularity fixed "
                "alongside the affix."),
    ),
    "3.2.170": (
        _c("mitrayuḥ — seeking a friend",
           {"kya_anta": True, "chandasi": True},
           note="क्याच्छन्दसि — क्य standing for क्यच्, क्यङ् and "
                "क्यष् together. छन्दसीति किम्? मित्रीयिता."),
    ),
    "3.2.171": (
        _c("jagmir yuvā — the youth who goes",
           {"root": "gam", "chandasi": True},
           note="आदृगमहनजनः किकिनौ लिट् च — and the कित् marking is "
                "there to defeat 7.4.11, which 1.2.5 alone would not."),
    ),
    "3.2.172": (
        _c("svapnak — sleepy", {"root": "svap"},
           note="स्वपितृषोर्नजिङ् — छन्दसीति निवृत्तम्."),
    ),
    "3.2.173": (
        _c("vandāruḥ — given to praising", {"root": "vand"},
           note="शॄवन्द्योरारुः."),
    ),
    "3.2.174": (
        _c("bhīruḥ, and bhīlukaḥ beside it", {"root": "bhī"},
           note="भियः क्रुक्लुकनौ — two affixes, and a vārttika adds "
                "a third, भीरुकः."),
    ),
    "3.2.175": (
        _c("sthāvaraḥ — immovable",
           {"root": "sthā", "wants": "varac"},
           note="स्थेशभासपिसकसो वरच् — and स्था is named by 3.2.139 "
                "too, so both स्थास्नुः and स्थावरः stand. `wants` "
                "names which affix is asked after."),
    ),
    "3.2.176": (
        _c("yāyāvaraḥ — a wanderer",
           {"root": "yā", "yan_anta": True},
           note="यश्च यङः — the second rule of the run to want a "
                "यङन्त stem."),
    ),
    "3.2.177": (
        _c("vidyut — lightning", {"root": "vidyut"},
           note="भ्राजभासधुर्विद्युतोर्जि… क्विप् — and it exists "
                "BECAUSE वासरूप is suspended: 3.2.76 gives क्विप् "
                "already, but the ताच्छीलिक affixes would displace it "
                "and it could not stand beside them. Also the far end "
                "of 3.2.134's आ क्वेः."),
    ),
    "3.2.178": (
        _c("yuk — joined",
           {"root": "yuj", "attested": True, "wants": "kvip"},
           note="अन्येभ्योऽपि दृश्यते — and दृशिग्रहणं "
                "विध्यन्तरोपसंग्रहार्थम् here, where at 3.2.75 it was "
                "प्रयोगानुसरणार्थम्. One word, two jobs."),
    ),
    "3.2.179": (
        _c("pratibhūḥ — a surety", {"root": "bhū", "samjna": True},
           note="भुवः संज्ञान्तरयोः — धनिकाधमर्णयोरन्तरे यस्तिष्ठति "
                "स प्रतिभूः, a definition by circumstance."),
    ),
    "3.2.180": (
        _c("prabhuḥ — a master",
           {"root": "bhū", "upasarga": "pra"},
           note="विप्रसम्भ्यो ड्वसंज्ञायाम्. असंज्ञायामिति किम्? "
                "विभूर्नाम कश्चित् — 3.2.179's own example."),
    ),
    "3.2.181": (
        _c("dhātrī — a wet-nurse, and the myrobalan",
           {"root": "dhe", "karaka": "karman"},
           note="धः कर्मणि ष्ट्रन् — षकारो ङीषर्थः."),
    ),
    "3.2.182": (
        _c("netram — an eye", {"root": "nī", "karaka": "karaṇa"},
           note="दाम्नीशस… करणे. And दंशेरनुनासिकलोपेन निर्देशो "
                "ज्ञापनार्थः — a spelling licensing an operation "
                "elsewhere, दशनम्."),
    ),
    "3.2.183": (
        _c("potram — a ploughshare",
           {"root": "pū", "karaka": "karaṇa", "part_of": "hala"},
           note="हलसूकरयोः पुवः — a condition on what the instrument "
                "is PART OF."),
    ),
    "3.2.184": (
        _c("aritram — an oar", {"root": "ṛ", "karaka": "karaṇa"},
           note="अर्तिलूधूसूखनसहचर इत्रः."),
    ),
    "3.2.185": (
        _c("pavitram — sacred grass",
           {"root": "pū", "karaka": "karaṇa", "samjna": True},
           note="पुवः संज्ञायाम् — समुदायेन चेत् संज्ञा गम्यते, the "
                "fourth समुदायोपाधि of the pāda."),
    ),
    "3.2.186": (
        _c("pavitro'yam ṛṣiḥ — this seer, a means of purifying",
           {"root": "pū", "karaka": "karaṇa", "rsi_devata": "ṛṣi"},
           note="कर्तरि चर्षिदेवतयोः — ऋषौ करणे, देवतायां कर्तरि, "
                "paired crosswise between a kāraka and a kind of "
                "being."),
    ),
    "3.2.187": (
        _c("dhṛṣṭaḥ — bold, in the PRESENT", {"nit": True},
           note="ञीतः क्तः — भूते निष्ठा विहिता वर्तमाने न "
                "प्राप्नोतीति विधीयते: it excepts 3.2.102, which the "
                "vṛtti names."),
    ),
    "3.2.188": (
        _c("rājñāṃ mataḥ — esteemed by kings", {"sense": "mati"},
           note="मतिबुद्धिपूजार्थेभ्यश्च — by MEANING, no root named. "
                "अनुक्तसमुच्चयार्थश्चकारः, and the vṛtti adds a long "
                "list in verse."),
    ),
    "3.3.1": (
        _c("kāru — a craftsman", {"word": "kāru"},
           note="उणादयो बहुलम्. वर्तमान इत्येव, संज्ञायामिति च — "
                "neither condition is in the sūtra. The affix is at "
                "प०उ० १.१ कृवापाजिमिस्वदिसाध्यशूभ्य उण्, which is "
                "read from the corpus, not restated."),
    ),
    "3.3.2": (
        _c("carma — a hide", {"word": "carman", "past": True},
           note="भूतेऽपि दृश्यन्ते. दृशिग्रहणं प्रयोगानुसारार्थम् — "
                "3.2.75's reading of दृश्यते, not 3.2.178's."),
    ),
    "3.3.3": (
        _c("gamī grāmam — he will go", {"word": "gamī"},
           note="भविष्यति गम्यादयः. प्रत्ययस्यैव भविष्यत्कालता "
                "विधीयते न प्रकृतेः — the affix carries the time."),
    ),
    "3.3.4": (
        _c("yāvad bhuṅkte — while he will eat",
           {"time": "bhaviṣyat", "beside": "yāvat", "nipata": True},
           note="यावत्पुरानिपातयोर्लट्. निपातयोरिति किम्? यावद् "
                "दास्यति तावद् भोक्ष्यते — as a case-form it falls "
                "to 3.3.13's लृट्, which the counter itself uses."),
    ),
    "3.3.5": (
        _c("kadā bhuṅkte — when will he eat?",
           {"time": "bhaviṣyat", "beside": "kadā"},
           note="विभाषा कदाकर्ह्योः. All three stand: कदा भुङ्क्ते, "
                "कदा भोक्ष्यते, कदा भोक्ता."),
    ),
    "3.3.6": (
        _c("kaṃ bhavanto bhojayanti — whom do you feed?",
           {"time": "bhaviṣyat", "kimvrtta": True, "lipsa": True},
           note="किंवृत्ते लिप्सायाम्. वृत्तग्रहणेन तद् विभक्त्यन्तं "
                "प्रतीयात्, डतरडतमौ चेति परिसंख्यानं स्मर्यते — the "
                "extent is a remembered list, not the word."),
    ),
    "3.3.7": (
        _c("yo bhaktaṃ dadāti — whoever gives food",
           {"time": "bhaviṣyat", "lipsyamana_siddhi": True},
           note="लिप्स्यमानसिद्धौ च. अकिंवृत्तार्थोऽयमारम्भः — it "
                "exists for the ground 3.3.6 could not reach."),
    ),
    "3.3.8": (
        _c("upādhyāyaś ced āgacchati — if the teacher comes",
           {"time": "bhaviṣyat", "lodartha": True},
           note="लोडर्थलक्षणे च. उपाध्यायागमनमध्ययनप्रैषस्य लक्षणम् — "
                "the act is the SIGN of the order, not the order."),
    ),
    "3.3.9": (
        _c("upādhyāyaś ced āgacchet — should the teacher come",
           {"time": "bhaviṣyat", "lodartha": True,
            "urdhvamauhurtika": True},
           note="लिङ् चोर्ध्वमौहूर्तिके, चकाराल्लट् च. "
                "भविष्यतश्चैतद् विशेषणम्, and the compound in the "
                "rule is itself a निपातन."),
    ),
    "3.3.10": (
        _c("bhoktuṃ vrajati — he goes in order to eat", {},
           note="तुमुन्ण्वुलौ क्रियायां क्रियार्थायाम्. And the "
                "ज्ञापक: क्रियायामुपपदे क्रियार्थायां वासरूपेण "
                "तृजादयो न भवन्ति — the third section to suspend "
                "3.1.94, after 3.2.146 and 3.2.177."),
    ),
    "3.3.11": (
        _c("pākāya vrajati — he goes for the cooking",
           {"bhava": True},
           note="भाववचनाश्च. It exists because of the suspension: "
                "क्रियार्थोपपदे विहितेनास्मिन्विषये तुमुना "
                "बाध्येरन्, वासरूपविधिश्चात्र नास्तीत्युक्तम्."),
    ),
    "3.3.12": (
        _c("kāṇḍalāvo vrajati — he goes to cut reeds",
           {"karman": True},
           note="अण् कर्मणि च. कर्मण्यण् इति सामान्येन विहितो "
                "वासरूपविधेरभावाद् ण्वुला बाधितः पुनरण् विधीयते — "
                "3.2.1's own affix, and the code ASKS 3.2.1 for it."),
    ),
    "3.3.13": (
        _c("kariṣyati — he will do", {"time": "bhaviṣyat"},
           note="लृट् शेषे च. शेषः क्रियार्थोपपदादन्यः, and चकारात् "
                "क्रियायां चोपपदे क्रियार्थायाम् — the rest, and "
                "also what the rest was defined against."),
    ),
    "3.3.14": (
        _c("kariṣyantaṃ devadattaṃ paśya — see him who will do it",
           {"aprathama": True},
           note="लृटः सद्वा. It names its affixes by 3.2.127's संज्ञा "
                "and takes its conditions from 3.2.124: "
                "अप्रथमासमानाधिकरणादिषु नित्यम्, अन्यत्र विकल्पः."),
    ),
    "3.3.15": (
        _c("śvo bhoktā — he will eat tomorrow",
           {"time": "bhaviṣyat", "anadyatana": True},
           note="अनद्यतने लुट्, लृटोऽपवादः. अनद्यतन इति "
                "बहुव्रीहिनिर्देशः, तेन व्यामिश्रे न भवति — the same "
                "device, wording and reason as 3.2.111's."),
    ),
    "3.3.16": (
        _c("rogaḥ — a disease", {"root": "ruj"},
           note="पदरुजविशस्पृशो घञ्. भविष्यतीति निवृत्तम्, इत उत्तरं "
                "त्रिष्वपि कालेषु प्रत्ययाः."),
        _c("sparśa upatāpaḥ — an afflicting touch",
           {"root": "spṛś", "sense": "upatāpa"},
           note="स्पृश उपताप इति वक्तव्यम् — a vārttika that CHANGES "
                "the output, so a row and not a note. ततोऽन्यत्र "
                "पचाद्यच्, स्पर्शो देवदत्तः, स्वरे विशेषः."),
    ),
    "3.3.17": (
        _c("candanasāraḥ — sandal essence",
           {"root": "sṛ", "sense": "sthira"},
           note="सृ स्थिरे. स चिरं तिष्ठन् कालान्तरं सरतीति "
                "धात्वर्थस्य कर्ता युज्यते — the root argued into the "
                "sense. स्थिर इति किम्? सर्ता."),
    ),
    "3.3.18": (
        _c("pākaḥ — cooking", {"root": "pac", "bhava": True},
           note="भावे. क्रियासामान्यवाची भवतिः, and धात्वर्थश्च "
                "धातुनैवोच्यते — the affix adds the act's सिद्धता, "
                "not its meaning. पुँल्लिङ्गमेकवचनं चात्र न तन्त्रम्."),
    ),
    "3.3.19": (
        _c("āhāraḥ — food",
           {"root": "pra-as", "akartari_karake": True,
            "samjna": True},
           note="अकर्तरि च कारके संज्ञायाम्. अकर्तरीति किम्? "
                "मिषत्यसौ मेषः. कारकग्रहणं ... ज्ञापनार्थम् for "
                "6.1.45, and both conditions run forward from here."),
    ),
    "3.3.20": (
        _c("dvau kārau — two scatterings",
           {"root": "kṛ", "parimana": True},
           note="परिमाणाख्यायां सर्वेभ्यः. सर्वग्रहणमपोऽपि "
                "बाधनार्थम् — पुरस्तादपवादन्यायेन an अपवाद displaces "
                "only what precedes, and अप् is at 3.3.57."),
    ),
    "3.3.21": (
        _c("upādhyāyaḥ — a teacher", {"root": "iṅ"},
           note="इङश्च, अचोऽपवादः. उपेत्यास्मादधीत उपाध्यायः."),
    ),
    "3.3.22": (
        _c("saṃrāvaḥ — a shout", {"root": "ru", "upasarga": "sam"},
           note="उपसर्गे रुवः — A preverb, without saying which. "
                "उपसर्ग इति किम्? रवः."),
    ),
    "3.3.23": (
        _c("saṃyāvaḥ — a mixing", {"root": "yu", "upasarga": "sam"},
           note="समि युद्रुदुवः. समीति किम्? प्रयवः."),
    ),
    "3.3.24": (
        _c("bhāvaḥ — being", {"root": "bhū"},
           note="श्रिणीभुवोऽनुपसर्गे. कथं प्रभावो राज्ञः? "
                "प्रादिसमासो भविष्यति. कथं च नयो राज्ञः? "
                "कृत्यल्युटो बहुलम् इत्यज् भविष्यति."),
    ),
    "3.3.25": (
        _c("viśrāvaḥ — a proclaiming",
           {"root": "śru", "upasarga": "vi"},
           note="वौ क्षुश्रुवः. वाविति किम्? क्षवः, श्रवः."),
    ),
    "3.3.26": (
        _c("unnāyaḥ — a lifting up",
           {"root": "nī", "upasarga": "ud"},
           note="अवोदोर्नियः. कथमुन्नयः पदार्थानाम्? कृत्यल्युटो "
                "बहुलम् — the second appeal to 3.3.113 in three."),
    ),
    "3.3.27": (
        _c("prastāvaḥ — an introduction",
           {"root": "stu", "upasarga": "pra"},
           note="प्रे द्रुस्तुस्रुवः. प्र इति किम्? स्तवः."),
    ),
    "3.3.28": (
        _c("niṣpāvaḥ — a winnowing",
           {"root": "pū", "upasarga": "nis"},
           note="निरभ्योः पूल्वोः, यथासंख्यमुपसर्गसंबन्धः. पू इति "
                "पूङ्पूञोः सामान्येन ग्रहणम्."),
    ),
    "3.3.29": (
        _c("udgāraḥ — a belch", {"root": "gṝ", "upasarga": "ud"},
           note="उन्न्योर्ग्रः. गृ शब्दे, गृ निगरणे — द्वयोरपि "
                "ग्रहणम्, one sūtra after 3.3.28 used the formula."),
    ),
    "3.3.30": (
        _c("utkāro dhānyasya — a heap of grain",
           {"root": "kṝ", "upasarga": "ud", "names_a": "dhānya"},
           note="कॄ धान्ये. विक्षेपार्थस्य किरतेर्ग्रहणम्, न "
                "हिंसार्थस्य, अनभिधानात्. धान्य इति किम्? "
                "भैक्ष्योत्करः."),
    ),
    "3.3.31": (
        _c("saṃstāvaḥ — the chanters' place",
           {"root": "stu", "upasarga": "sam", "sense": "yajña"},
           note="यज्ञे समि स्तुवः. समेत्य स्तुवन्ति यस्मिन् देशे "
                "छन्दोगाः, स देशः संस्ताव इत्युच्यते."),
    ),
    "3.3.32": (
        _c("śaṅkhaprastāraḥ — a spread of shells",
           {"root": "stṝ", "upasarga": "pra"},
           note="प्रे स्त्रोऽयज्ञे. अयज्ञ इति किम्? बर्हिष्प्रस्तरः "
                "— the rule before REQUIRED what this refuses."),
    ),
    "3.3.33": (
        _c("paṭasya vistāraḥ — the spread of a cloth",
           {"root": "stṝ", "upasarga": "vi", "sense": "prathana"},
           note="प्रथने वावशब्दे. प्रथन इति किम्? तृणविस्तरः. "
                "अशब्द इति किम्? विस्तरो वचसाम् — two conditions on "
                "different axes."),
    ),
    "3.3.34": (
        _c("viṣṭārapaṅktiḥ — a metre so called",
           {"root": "stṝ", "upasarga": "vi",
            "names_a": "chandonāman"},
           note="छन्दोनाम्नि च. वृत्तमत्र छन्दो गृह्यते ... "
                "नामग्रहणात्, and the NAME is the whole word: "
                "न घञन्तं शब्दरूपम्, तत्र त्ववयवत्वेन वर्तते."),
    ),
    "3.3.35": (
        _c("udgrāhaḥ — a taking up",
           {"root": "grah", "upasarga": "ud"},
           note="उदि ग्रहः, अपोऽपवादः. छन्दसि निपूर्वादपीष्यते ..., "
                "हकारस्य भकारः: उद्ग्राभं च निग्राभं च (मा०सं० "
                "१७.६४)."),
    ),
    "3.3.36": (
        _c("saṃgrāhaḥ — a grip",
           {"root": "grah", "upasarga": "sam", "sense": "muṣṭi"},
           note="समि मुष्टौ. मुष्टिरङ्गुलिसंनिवेशः. मुष्टाविति "
                "किम्? संग्रहो धान्यस्य."),
    ),
    "3.3.37": (
        _c("pariṇāyaḥ — moving the pieces at dice",
           {"root": "nī", "upasarga": "pari", "sense": "dyūta"},
           note="परिन्योर्नीणोर्द्यूताभ्रेषयोः — यथासंख्यम् binding "
                "THREE lists: द्यूतविषयश्चेन्नयतेरर्थः, "
                "अभ्रेषविषयश्चेदिणर्थः."),
    ),
    "3.3.38": (
        _c("tava paryāyaḥ — your turn",
           {"root": "i", "upasarga": "pari", "sense": "anupātyaya"},
           note="परावनुपात्यय इणः. अनुपात्यय इति किम्? कालस्य "
                "पर्ययः, अतिपात इत्यर्थः — one sound apart, and "
                "contrary in sense."),
    ),
    "3.3.39": (
        _c("tava viśāyaḥ — your turn to lie down",
           {"root": "śī", "upasarga": "vi", "sense": "paryāya"},
           note="व्युपयोः शेतेः पर्याये. तव राजानमुपशयितुं पर्याय "
                "इत्यर्थः. पर्याय इति किम्? विशयः."),
    ),
    "3.3.40": (
        _c("puṣpapracāyaḥ — flower-gathering",
           {"root": "ci", "sense": "hastādāna"},
           note="हस्तादाने चेरस्तेये. हस्तादानग्रहणेन "
                "प्रत्यासत्तिरादेयस्य लक्ष्यते. अस्तेय इति किम्? "
                "फलप्रचयश्चौर्येण — within reach and still refused."),
    ),
    "3.3.41": (
        _c("anityakāyaḥ — the impermanent body",
           {"root": "ci", "sense": "śarīra"},
           note="निवासचितिशरीरोपसमाधानेष्वादेश्च कः — four senses, "
                "and the root's first sound becomes क. महान् "
                "काष्ठनिचयः: बहुत्वमत्र विवक्षितं नोपसमाधानम्."),
    ),
    "3.3.42": (
        _c("bhikṣukanikāyaḥ — an order of monks",
           {"root": "ci", "sense": "saṅgha"},
           note="संघे चानौत्तराधर्ये. प्राणिनां समुदायः संघः ... "
                "औत्तराधर्यपर्युदासादितरो गृह्यते — one half named "
                "to exclude it, the other never stated."),
    ),
    "3.3.43": (
        _c("vyāvakrośī — a slanging-match",
           {"sense": "karmavyatihāra", "stri": True},
           note="कर्मव्यतिहारे णच् स्त्रियाम्. चकारो विशेषणार्थः "
                "for 5.4.14. स्त्रियामिति किम्? व्यतिपाको वर्तते."),
    ),
    "3.3.44": (
        _c("sāṃkūṭinam — utterly heaped",
           {"sense": "abhividhi", "bhava": True},
           note="अभिविधौ भाव इनुण्. पुनर्भावग्रहणं "
                "वासरूपनिरासार्थम् — the fourth suspension of "
                "3.1.94, and the first by repeating a word."),
    ),
    "3.3.45": (
        _c("avagrāho hanta te bhūyāt — a curse on you",
           {"root": "grah", "upasarga": "ava", "sense": "ākrośa"},
           note="आक्रोशेऽवन्योर्ग्रहः. दृष्टानुवृत्तिसामर्थ्याद् "
                "घञनुवर्तते, नानन्तर इनुण् — the nearer affix is "
                "NOT the one carried down."),
    ),
    "3.3.46": (
        _c("pātrapragrāhaḥ — holding out the bowl",
           {"root": "grah", "upasarga": "pra", "sense": "lipsā"},
           note="प्रे लिप्सायाम्. लिप्सा was 3.3.6's condition too, "
                "for a tense-ending rather than an affix."),
    ),
    "3.3.47": (
        _c("uttaraparigrāhaḥ — a further taking",
           {"root": "grah", "upasarga": "pari", "sense": "yajña"},
           note="परौ यज्ञे. यज्ञविषयश्चेत् प्रत्ययान्ताभिधेयः "
                "स्यात् — on what the finished WORD denotes."),
    ),
    "3.3.48": (
        _c("nīvārāḥ — wild rice",
           {"root": "vṛ", "upasarga": "ni", "names_a": "dhānya"},
           note="नौ वृ धान्ये. वृ इति वृङ्वृञोः सामान्येन ग्रहणम् — "
                "the third such in twenty sūtras. धान्य इति किम्? "
                "निवरा कन्या."),
    ),
    "3.3.49": (
        _c("ucchrāyaḥ — a rising up",
           {"root": "śri", "upasarga": "ud"},
           note="उदि श्रयतियौतिपूद्रुवः. वक्ष्यमाणं विभाषाग्रहणमिह "
                "सिंहावलोकितन्यायेन संबध्यते — 3.3.50's विभाषा read "
                "BACKWARD into this rule."),
    ),
    "3.3.50": (
        _c("ārāvaḥ / āravaḥ — a cry",
           {"root": "ru", "upasarga": "āṅ"},
           note="विभाषाङि रुप्लुवोः — both forms stand, and the "
                "विभाषा is spent backward as well as forward."),
    ),
    "3.3.51": (
        _c("avagrāho devasya — a drought",
           {"root": "grah", "upasarga": "ava",
            "sense": "varṣapratibandha"},
           note="अवे ग्रहो वर्षप्रतिबन्धे. प्राप्तकालस्य वर्षस्य ... "
                "अभावो वर्षप्रतिबन्धः. वर्षप्रतिबन्ध इति किम्? "
                "अवग्रहः पदस्य."),
    ),
    "3.3.52": (
        _c("tulāpragrāhaḥ — the balance-cord",
           {"root": "grah", "upasarga": "pra", "names_a": "vaṇij"},
           note="प्रे वणिजाम्. वणिक्संबन्धेन च तुलासूत्रं लक्ष्यते, "
                "न तु वणिजस्तन्त्रम् — so वणिगन्यो वा."),
    ),
    "3.3.53": (
        _c("pragrāhaḥ — a rein",
           {"root": "grah", "upasarga": "pra", "names_a": "raśmi"},
           note="रश्मौ च. ग्रहो विभाषा प्र इति वर्तते — three things "
                "carried down at once."),
    ),
    "3.3.54": (
        _c("prāvāraḥ — a cloak",
           {"root": "vṛ", "upasarga": "pra", "sense": "ācchādana"},
           note="वृणोतेराच्छादने. आच्छादन इति किम्? प्रवरा गौः."),
    ),
    "3.3.55": (
        _c("paribhavaḥ — contempt",
           {"root": "bhū", "upasarga": "pari", "sense": "avajñāna"},
           note="परौ भुवोऽवज्ञाने. GRETIL reads प्रौ and Vidyut परौ; "
                "the Kāśikā decides it — परिशब्द उपपदे भवतेः, "
                "परिभावः. अवज्ञान इति किम्? सर्वतो भवनं परिभवः."),
    ),
    "3.3.56": (
        _c("jayaḥ — victory", {"root": "ji", "root_final": "i"},
           note="एरच्, घञोऽपवादः. भावे, अकर्तरि च कारक इति "
                "प्रकृतमनुवर्तते यावत् कृत्यल्युटो बहुलम् इति — the "
                "headings reach to 3.3.113."),
    ),
    "3.3.57": (
        _c("karaḥ — a doer", {"root": "kṛ", "root_final": "ṝ"},
           note="ॠदोरप्. पित्करणं स्वरार्थम्; दकारो मुखसुखार्थः, मा "
                "भूत् तादपि परस्तपरः — a letter for sayability."),
    ),
    "3.3.58": (
        _c("gamaḥ — going", {"root": "gam"},
           note="ग्रहवृदृनिश्चिगमश्च. निश्चिग्रहणं स्वरार्थम् — one "
                "root named for the accent alone."),
    ),
    "3.3.59": (
        _c("vighasaḥ — leavings", {"root": "ad", "upasarga": "vi"},
           note="उपसर्गेऽदः — a preverb, without saying which. "
                "उपसर्ग इति किम्? घासः."),
    ),
    "3.3.60": (
        _c("nyādaḥ — eating up", {"root": "ad", "upasarga": "ni"},
           note="नौ णश्च, चकारादप् च — two affixes from one rule, so "
                "न्यादः and निघसः both stand."),
    ),
    "3.3.61": (
        _c("japaḥ — muttering", {"root": "jap"},
           note="व्यधजपोरनुपसर्गे. अनुपसर्ग इति किम्? उपजापः."),
    ),
    "3.3.62": (
        _c("svanaḥ / svānaḥ — a sound", {"root": "svan"},
           note="स्वनहसोर्वा — and the वा runs down to 3.3.65."),
    ),
    "3.3.63": (
        _c("niyamaḥ — a restraint",
           {"root": "yam", "upasarga": "ni"},
           note="यमः समुपनिविषु च — four preverbs ADDED to a "
                "condition of no preverb; अनुपसर्गात् खल्वपि यमः."),
    ),
    "3.3.64": (
        _c("nigadaḥ — a recitation",
           {"root": "gad", "upasarga": "ni"},
           note="नौ गदनदपठस्वनः, घञोऽपवादः."),
    ),
    "3.3.65": (
        _c("kvaṇaḥ — a twang", {"root": "kvaṇ", "sense": "vīṇā"},
           note="क्वणो वीणायां च. सोपसर्गार्थं वीणाया ग्रहणम् — the "
                "sense WIDENS the rule. एतेष्विति किम्? अतिक्वाणः."),
    ),
    "3.3.66": (
        _c("mūlakapaṇaḥ — a bundle of radishes",
           {"root": "paṇ", "parimana": True},
           note="नित्यं पणः परिमाणे. नित्यग्रहणं "
                "विकल्पनिवृत्त्यर्थम् — it stops 3.3.62's option. "
                "परिमाण इति किम्? पाणः."),
    ),
    "3.3.67": (
        _c("vidyāmadaḥ — pride of learning", {"root": "mad"},
           note="मदोऽनुपसर्गे. अनुपसर्ग इति किम्? उन्मादः, प्रमादः."),
    ),
    "3.3.68": (
        _c("kanyānāṃ pramadaḥ — the delight of girls",
           {"word": "pramada"},
           note="प्रमदसंमदौ हर्षे, both निपातन. प्रसंभ्यामिति "
                "नोक्तम्, निपातनं रूढ्यर्थम्. हर्ष इति किम्? "
                "प्रमादः."),
    ),
    "3.3.69": (
        _c("samajaḥ paśūnām — a herd",
           {"root": "aj", "upasarga": "sam", "names_a": "paśu"},
           note="समुदोरजः पशुषु. पशुष्विति किम्? समाजो "
                "ब्राह्मणानाम्. स संपूर्वः समुदाये, उत्पूर्वश्च "
                "प्रेरणे."),
    ),
    "3.3.70": (
        _c("akṣasya glahaḥ — a throw at dice", {"word": "glaha"},
           note="अक्षेषु ग्लहः. ग्रहेरप् सिद्ध एव, लत्वार्थं "
                "निपातनम् — a fixed word stated for one letter."),
    ),
    "3.3.71": (
        _c("gavām upasaraḥ — the covering of cows",
           {"root": "sṛ", "sense": "prajana"},
           note="प्रजने सर्तेः. प्रजनं प्रथमं गर्भग्रहणम्."),
    ),
    "3.3.72": (
        _c("nihavaḥ — a calling",
           {"root": "hve", "upasarga": "ni"},
           note="ह्वः संप्रसारणं च न्यभ्युपविषु — the root is "
                "vocalised too. एतेष्विति किम्? प्रह्वायः."),
    ),
    "3.3.73": (
        _c("āhavaḥ — a battle",
           {"root": "hve", "upasarga": "āṅ", "sense": "yuddha"},
           note="आङि युद्धे. आहूयन्तेऽस्मिन्नित्याहवः. युद्ध इति "
                "किम्? आह्वायः."),
    ),
    "3.3.74": (
        _c("āhāvaḥ paśūnām — a cattle-trough", {"word": "āhāva"},
           note="निपानमाहावः — संप्रसारणम्, अप् and वृद्धि all fixed "
                "at once. निपानमिति किम्? आह्वायः."),
    ),
    "3.3.75": (
        _c("havaḥ — a call", {"root": "hve", "bhava": True},
           note="भावेऽनुपसर्गस्य. हवे हवे सुहवं शूरमिन्द्रम् (ऋ० "
                "६.४७.११). भावग्रहणम् ... 3.3.19 इत्यस्य "
                "निरासार्थम्."),
    ),
    "3.3.76": (
        _c("vadhaś corāṇām — the killing of thieves",
           {"root": "han", "bhava": True},
           note="हनश्च वधः. चकारो भिन्नक्रमत्वाद् नादेशेन "
                "संबध्यते ... तेन घञपि भवति — word order set aside."),
    ),
    "3.3.77": (
        _c("dadhighanaḥ — curd",
           {"root": "han", "sense": "mūrti"},
           note="मूर्तौ घनः. कथं घनं दधीति? धर्मशब्देन धर्मी "
                "भण्यते."),
    ),
    "3.3.78": (
        _c("antarghanaḥ — a district so called",
           {"root": "han", "upasarga": "antar", "names_a": "deśa"},
           note="अन्तर्घनो देशे. अन्ये णकारं पठन्ति ... तदपि "
                "ग्राह्यमेव — a variant recorded, not chosen."),
    ),
    "3.3.79": (
        _c("praghaṇaḥ — a porch", {"word": "praghaṇa"},
           note="अगारैकदेशे प्रघणः प्रघाणश्च — two forms fixed by one "
                "rule. अगारैकदेश इति किम्? प्रघातोऽन्यः."),
    ),
    "3.3.80": (
        _c("udghanaḥ — a chopping-block", {"word": "udghana"},
           note="उद्घनोऽत्याधाने. यस्मिन् काष्ठे स्थापयित्वा "
                "अन्यानि काष्ठानि तक्ष्यन्ते तदभिधीयते."),
    ),
    "3.3.81": (
        _c("apaghanaḥ — a limb", {"word": "apaghana"},
           note="अपघनोऽङ्गम्. अवयवः, एकदेशो न सर्वः; किं तर्हि? "
                "पाणिः पादश्चाभिधीयते."),
    ),
    "3.3.82": (
        _c('ayoghanaḥ — an iron hammer',
           {'root': 'han', 'upasarga': 'vi', 'karaka': 'karaṇa'},
           note='अयस्विद्रुहनः, करणे कारके, घनादेशः.'),
    ),
    "3.3.83": (
        _c('stambaghnaḥ — a clump-cutter',
           {'root': 'han', 'upasarga': 'stamba', 'karaka': 'karaṇa'},
           note='स्तम्बे क च — क and, by the च, अप्. करण इत्येव: स्तम्बघातः.'),
    ),
    "3.3.84": (
        _c('parighaḥ — a door-bar',
           {'root': 'han', 'upasarga': 'pari', 'karaka': 'karaṇa'},
           note='परौ घः — the substitute is घ where 3.3.82 had घन.'),
    ),
    "3.3.85": (
        _c('parvatopaghnaḥ — a place under a hill',
           {'word': 'parvatopaghna'},
           note='उपघ्नमाश्रये, a निपातन: अप् and उपधालोप both fixed. आश्रयशब्दः सामीप्यं प्रत्यासत्तिं लक्षयति.'),
    ),
    "3.3.86": (
        _c('saṅghaḥ paśūnām — a herd',
           {'root': 'han', 'upasarga': 'sam', 'sense': 'praśaṃsā', 'names_a': 'gaṇa'},
           note='संघोद्घौ गणप्रशंसयोः, यथासंख्यम्. गणप्रशंसयोरिति किम्? संघातः.'),
    ),
    "3.3.87": (
        _c('nighā vṛkṣāḥ — evenly grown trees',
           {'word': 'nigha'},
           note='निघो निमितम्. समन्ताद् मितं निमितम्, समारोहपरिणाहम्.'),
    ),
    "3.3.88": (
        _c('kṛtrimam — artificial',
           {'root': 'kṛ', 'marked': 'ḍvit'},
           note='ड्वितः क्त्रिः. क्त्रेर्मम् नित्यम् इति वचनात् केवलो न प्रयुज्यते — the affix is never seen alone.'),
    ),
    "3.3.89": (
        _c('vepathuḥ — trembling',
           {'root': 'vep', 'marked': 'ṭvit'},
           note='ट्वितोऽथुच् — the pair to 3.3.88, dividing roots by mark.'),
    ),
    "3.3.90": (
        _c('praśnaḥ — a question',
           {'root': 'pracch'},
           note="यजयाचयतविच्छप्रच्छरक्षो नङ्. ङकारो गुणप्रतिषेधार्थः. प्रच्छेरसंप्रसारणं ज्ञापकात् प्रश्ने चासन्नकाले इति — 3.2.117's WORDING as evidence."),
    ),
    "3.3.91": (
        _c('svapnaḥ — sleep',
           {'root': 'svap'},
           note='स्वपो नन्. नकारः स्वरार्थः.'),
    ),
    "3.3.92": (
        _c('antardhiḥ — concealment',
           {'root': 'ḍudhāñ', 'upasarga': 'antar'},
           note="उपसर्गे घोः किः — the roots come from 1.1.20's संज्ञा, which the resolver ASKS. कित्करणमातो लोपार्थम्."),
    ),
    "3.3.93": (
        _c('jaladhiḥ — the sea',
           {'root': 'ḍudhāñ', 'karaka': 'adhikaraṇa'},
           note='कर्मण्यधिकरणे च. अधिकरणग्रहणमर्थान्तरनिरासार्थम्, चकारः प्रत्ययानुकर्षणार्थः.'),
    ),
    "3.3.94": (
        _c('matiḥ — thought',
           {'root': 'man', 'stri': True},
           note='स्त्रियां क्तिन्, घञजपामपवादः. Six vārttikas, and आबादयः प्रयोगतोऽनुसर्तव्याः leaves one list open.'),
    ),
    "3.3.95": (
        _c('paktiḥ — cooking',
           {'root': 'pac', 'stri': True, 'bhava': True},
           note='स्थागापापचो भावे, अङोऽपवादस्य बाधकः. कथमवस्था संस्थेति? 1.1.34 इति ज्ञापकाद् नात्यन्ताय बाधा भवति.'),
    ),
    "3.3.96": (
        _c('vṛṣṭiḥ — rain',
           {'root': 'vṛṣ', 'stri': True, 'bhava': True, 'mantra': True},
           note='मन्त्रे ... उदात्तः (ऋ० १.३.८.८). उदात्तार्थं वचनम् — the affix comes from 3.3.94 already.'),
    ),
    "3.3.97": (
        _c('ūtiḥ — help',
           {'word': 'ūti'},
           note='ऊतियूतिजूतिसातिहेतिकीर्तयश्च — six words, six grounds.'),
    ),
    "3.3.98": (
        _c('ijyā — sacrifice',
           {'root': 'yaj', 'stri': True, 'bhava': True},
           note='व्रजयजोर्भावे क्यप्. पित्करणमुत्तरत्र तुगर्थम्.'),
    ),
    "3.3.99": (
        _c('vidyā — knowledge',
           {'root': 'vid', 'stri': True, 'samjna': True},
           note='संज्ञायां समजनिषद… क्यप्. भाव इति न स्वर्यते, पूर्व एवात्रार्थाधिकारः.'),
    ),
    "3.3.100": (
        _c('kriyā — action',
           {'root': 'kṛñ', 'stri': True},
           note='कृञः श च. योगविभागोऽत्र कर्तव्यः, क्तिन्नपि यथा स्यात्.'),
    ),
    "3.3.101": (
        _c('icchā — a wish',
           {'word': 'icchā'},
           note='इच्छा — शः and the absence of यक् both fixed. 3.3.96 pointed forward to it.'),
    ),
    "3.3.102": (
        _c('cikīrṣā — a wish to do',
           {'root': 'cikīrṣ', 'stri': True, 'pratyayanta': True},
           note='अ प्रत्ययात्, क्तिनोऽपवादः — the stem is already made.'),
    ),
    "3.3.103": (
        _c('īhā — an effort',
           {'root': 'īh', 'stri': True, 'gurumat': True, 'hal_final': True},
           note='गुरोश्च हलः. गुरोरिति किम्? भक्तिः. हल इति किम्? नीतिः.'),
    ),
    "3.3.104": (
        _c('śraddhā — trust',
           {'root': 'śraddhā', 'stri': True},
           note='षिद्भिदादिभ्योऽङ् — the members read from the गणपाठ on disk, not typed out.'),
    ),
    "3.3.105": (
        _c('cintā — thought',
           {'root': 'cint', 'stri': True},
           note='चिन्तिपूजिकथिकुम्बिचर्चश्च, युचि प्राप्ते; चकाराद् युजपि भवति, चिन्तना.'),
    ),
    "3.3.106": (
        _c('pradā — a gift',
           {'root': 'dā', 'stri': True, 'root_final': 'ā', 'upasarga': 'pra'},
           note='आतश्चोपसर्गे. श्रदन्तरोरुपसर्गवद् वृत्तिः — two words that are not preverbs behaving like them.'),
    ),
    "3.3.107": (
        _c('kāraṇā — a cause',
           {'root': 'ās', 'stri': True},
           note='ण्यासश्रन्थो युच्. श्रन्थिः क्र्यादिर्गृह्यते, न चुरादिः, ण्यन्तत्वेनैव सिद्धत्वात् — settled from redundancy.'),
    ),
    "3.3.108": (
        _c('pravāhikā — dysentery',
           {'root': 'pra-vah', 'names_a': 'roga'},
           note='रोगाख्यायां ण्वुल् बहुलम्. बहुलग्रहणं व्यभिचारार्थम्: न च भवति शिरोऽर्तिः.'),
    ),
    "3.3.109": (
        _c('śālabhañjikā — a doll',
           {'root': 'bhañj', 'samjna': True},
           note='संज्ञायाम् — names of games and festivals, each a whole compound.'),
    ),
    "3.3.110": (
        _c('kāṃ kārim akārṣīḥ — what did you do?',
           {'root': 'kṛ', 'sense': 'paripraśna'},
           note='विभाषाख्यानपरिप्रश्नयोरिञ् च. विभाषाग्रहणात् परोऽपि यः प्राप्नोति सोऽपि भवति — five forms for one question.'),
    ),
    "3.3.111": (
        _c('ikṣubhakṣikā — a turn at sugarcane',
           {'root': 'bhakṣ', 'sense': 'ṛṇa'},
           note='पर्यायार्हर्णोत्पत्तिषु ण्वुच्. ण्वुलि प्रकृते प्रत्ययान्तरकरणं स्वरार्थम्.'),
    ),
    "3.3.112": (
        _c('akaraṇis te bhūyāt — may you fail',
           {'root': 'kṛ', 'upasarga': 'nañ', 'sense': 'ākrośa'},
           note='आक्रोशे नञ्यनिः. आक्रोश इति किम्? अकृतिस्तस्य कटस्य. नञीति किम्? मृतिस्ते वृषल भूयात्.'),
    ),
    "3.3.113": (
        _c('snānīyaṃ cūrṇam — powder for bathing',
           {'group': 'kṛtya-kāraka'},
           note='कृत्यल्युटो बहुलम् — यत्र विहितास्ततोऽन्यत्रापि भवन्ति. And भावे अकर्तरि च कारक इति निवृत्तम्, closing the two headings where 3.3.56 said they would close.'),
    ),
    "3.3.114": (
        _c('hasitam — laughing',
           {'root': 'has', 'napumsaka': True, 'bhava': True, 'wants': 'kta'},
           note='नपुंसके भावे क्तः. भावे is stated AFRESH here — the heading carrying it stopped at 3.3.113.'),
    ),
    "3.3.115": (
        _c('hasanam — laughing',
           {'root': 'has', 'napumsaka': True, 'bhava': True, 'wants': 'lyuṭ'},
           note='ल्युट् च. योगविभाग उत्तरार्थः — split for the sake of the two rules after, not for itself.'),
    ),
    "3.3.116": (
        _c('payaḥpānaṃ sukham — drinking milk is pleasant',
           {'root': 'pā', 'napumsaka': True, 'bhava': True, 'sense': 'sukha', 'karaka': 'karman'},
           note='कर्मण्यधिकरणे च. पूर्वेणैव सिद्धे प्रत्यये नित्यसमासार्थं वचनम् — the whole rule is for the compound. सर्वत्रासमासः प्रत्युदाह्रियते.'),
    ),
    "3.3.117": (
        _c('godohanī — a milking-pail',
           {'root': 'duh', 'karaka': 'karaṇa'},
           note='करणाधिकरणयोश्च — the two kārakas 3.3.19 left general.'),
    ),
    "3.3.118": (
        _c('ākaraḥ — a mine',
           {'root': 'kṛ', 'pum': True, 'samjna': True, 'karaka': 'karaṇa'},
           note='पुंसि संज्ञायां घः प्रायेण. प्रायग्रहणमकार्त्स्न्यार्थम् — the rule admits its own leaks. समुदायेन चेत् संज्ञा गम्यते.'),
    ),
    "3.3.119": (
        _c('gocaraḥ — a pasture',
           {'word': 'gocara'},
           note='गोचरादयः, निपातन — and an अपवाद to 3.3.121, stated TWO SŪTRAS BEFORE it. निपातनाद् वीभावो न भवति for व्यज.'),
    ),
    "3.3.120": (
        _c('avatāraḥ — a descent',
           {'root': 'tṝ', 'upasarga': 'ava', 'pum': True, 'samjna': True, 'karaka': 'karaṇa'},
           note="अवे तॄस्त्रोर्घञ्. कथमवतारो नद्याः? प्रायानुवृत्तेरसंज्ञायामपि भवति — 3.3.118's hedge working two rules on."),
    ),
    "3.3.121": (
        _c('bandhaḥ — a bond',
           {'root': 'bandh', 'pum': True, 'samjna': True, 'karaka': 'karaṇa', 'hal_final': True},
           note='हलश्च, घस्यापवादः. Four conditions carried, one stated.'),
    ),
    "3.3.122": (
        _c('adhyāyaḥ — a lesson',
           {'word': 'adhyāya'},
           note='अध्यायादयः, निपातन. अहलन्तार्थ आरम्भः.'),
    ),
    "3.3.123": (
        _c('tailodaṅkaḥ — an oil-vessel',
           {'word': 'udaṅka'},
           note='उदङ्कोऽनुदके. ननु च हलश्च इति सिद्ध एव घञ्? उदके प्रतिषेधार्थमिदं वचनम् — a निपातन whose work is negative.'),
    ),
    "3.3.124": (
        _c('ānāyo matsyānām — a fishing-net',
           {'word': 'ānāya'},
           note='आनायोऽनहः — fixed only where a NET is meant.'),
    ),
    "3.3.125": (
        _c('ākhanaḥ — a digging tool',
           {'root': 'khan', 'karaka': 'karaṇa'},
           note='खनो घ च — and five vārttikas add डो, डरो, इको, इकवको: seven words from one root.'),
    ),
    "3.3.126": (
        _c('duṣkaraḥ — hard to do',
           {'root': 'kṛ', 'isadadi': True},
           note='ईषद्दुःसुषु कृच्छ्राकृच्छ्रार्थेषु खल्. कृच्छ्रं दुःखम्, तद् दुरो विशेषणम् ... संभवात् — divided by FIT, not by counting off.'),
    ),
    "3.3.127": (
        _c('svāḍhyaṃkaraḥ — easily made rich',
           {'root': 'kṛñ', 'isadadi': True, 'karaka': 'kartṛ'},
           note='कर्तृकर्मणोश्च भूकृञोः, यथासंख्यम्. कर्तृकर्मणोश्च्व्यर्थयोरिति वक्तव्यम्.'),
    ),
    "3.3.128": (
        _c('supānaḥ — easy to drink',
           {'root': 'pā', 'isadadi': True, 'root_final': 'ā'},
           note='आतो युच्, खलोऽपवादः. ईषदादयोऽनुवर्तन्ते, कर्तृकर्मणोरिति न स्वर्यते — which of two adjacent conditions travels.'),
    ),
    "3.3.129": (
        _c("sūpasadano'gniḥ — a fire easy to approach",
           {'root': 'sad', 'isadadi': True, 'gati_artha': True, 'chandasi': True},
           note='छन्दसि गत्यर्थेभ्यः (तै०सं० ७.५.२०.१).'),
    ),
    "3.3.130": (
        _c('duryodhanaḥ — hard to fight',
           {'root': 'yudh', 'gati_artha': True, 'chandasi': True},
           note='अन्येभ्योऽपि दृश्यते (ऋ० १०.११२.८) — दृश्यते a fourth time, usage-following. And भाषायां ... युज् वक्तव्यः gives five roots the affix OUTSIDE the Veda.'),
    ),
    "3.3.131": (
        _c('ayam āgacchāmi — I am just come',
           {'like': 'vartamāna'},
           note='वर्तमानसामीप्ये वर्तमानवद् वा. वत्करणं सर्वसादृश्यार्थम् — the transfer carries every condition with it.'),
    ),
    "3.3.132": (
        _c('upādhyāyaś ced āgamat — if the teacher comes',
           {'like': 'bhūta', 'sense': 'āśaṃsā'},
           note='आशंसायां भूतवच्च. सामान्यातिदेशे विशेषानतिदेशात् लङ्लिटौ न भवतः.'),
    ),
    "3.3.133": (
        _c('kṣipram āgamiṣyati — he will come soon',
           {'time': 'bhaviṣyat', 'beside': 'kṣipra', 'sense': 'āśaṃsā'},
           note="क्षिप्रवचने लृट्. वचनग्रहणं पर्यायार्थम् — any synonym of 'soon', as 3.2.112's अभिज्ञावचने."),
    ),
    "3.3.134": (
        _c('upādhyāyaś ced āgacchet — should he come',
           {'time': 'bhaviṣyat', 'beside': 'āśaṃsāvacana', 'sense': 'āśaṃsā'},
           note='आशंसावचने लिङ् — आशंसा येनोच्यते तदाशंसावचनम्.'),
    ),
    "3.3.135": (
        _c('yāvajjīvam annam adāt — he gave food all his life',
           {'like': 'anadyatana', 'sense': 'kriyāprabandha'},
           note='नानद्यतनवत् क्रियाप्रबन्धसामीप्ययोः. द्वौ प्रतिषेधौ यथाप्राप्तस्याभ्यनुज्ञापनाय.'),
    ),
    "3.3.136": (
        _c('tatra dvir odanaṃ bhokṣyāmahe — twice we shall eat',
           {'like': 'anadyatana', 'sense': 'deśa-maryādā'},
           note='भविष्यति मर्यादावचनेऽवरस्मिन्. इह सूत्रे देशकृता मर्यादा, उत्तरत्र कालकृता, तत्र न विशेषं वक्ष्यति.'),
    ),
    "3.3.137": (
        _c('tatra adhyeṣyāmahe — there we shall study',
           {'like': 'anadyatana', 'sense': 'kāla-maryādā'},
           note='कालविभागे चानहोरात्राणाम्. पूर्वेणैव सिद्धे वचनमिदम् अहोरात्रनिषेधार्थम्.'),
    ),
    "3.3.138": (
        _c('adhyeṣyāmahe, adhyetāsmahe — we shall study',
           {'like': 'anadyatana', 'sense': 'kāla-maryādā-para'},
           note='परस्मिन् विभाषा. अवरस्मिन्वर्जं पूर्वमनुवर्तते — an अनुवृत्ति with one word cut out.'),
    ),
    "3.3.139": (
        _c('na śakaṭaṃ paryābhaviṣyat — it would not have overturned',
           {'time': 'bhaviṣyat', 'kriyatipatti': True, 'lin_nimitta': True},
           note='लिङ्निमित्ते लृङ् क्रियातिपत्तौ — a condition about ANOTHER RULE having applied. 3.3.156 is what it means.'),
    ),
    "3.3.140": (
        _c('tadābhokṣyata — then he would have eaten',
           {'kriyatipatti': True, 'lin_nimitta': True},
           note='भूते च — the same ending for a failed past act.'),
    ),
    "3.3.141": (
        _c("kathaṃ nāma ... ayājayiṣyat — how could you have?",
           {"sutra_id": "3.3.145"},
           note="वोताप्योः — 3.3.140's लृङ् is OPTIONAL, and the "
                "extent is read off a prefix: मर्यादायामयमाङ् "
                "नाभिविधौ, so it runs to 3.3.151 and stops before "
                "3.3.152."),
    ),
    "3.3.142": (
        _c('api ... yājayati — you actually make him sacrifice',
           {'beside': 'api', 'sense': 'garhā'},
           note='गर्हायां लडपिजात्वोः. कालविशेषविहितांश्चापि प्रत्ययानयं परत्वाद् बाधते — it wins by standing LATER.'),
    ),
    "3.3.143": (
        _c('kathaṃ nāma ... yājayet — how could you!',
           {'beside': 'katham', 'sense': 'garhā'},
           note='विभाषा कथमि लिङ् च. विभाषाग्रहणं यथास्वं कालविषये विहितानामबाधनार्थम्.'),
    ),
    "3.3.144": (
        _c('ko nāma vṛṣalaḥ — what śūdra indeed',
           {'kimvrtta': True, 'sense': 'garhā'},
           note='किंवृत्ते लिङ्लृटौ. लिङ्ग्रहणं लटोऽपरिग्रहार्थम्.'),
    ),
    "3.3.145": (
        _c('nāvakalpayāmi — I cannot believe it',
           {'sense': 'anavakḷpti'},
           note="अनवक्ऌप्त्यमर्षयोरकिंवृत्तेऽपि. बह्वचः पूर्वनिपातो लक्षणव्यभिचारचिह्नम्, तेन यथासंख्यं न भवति — 3.2.29's argument again."),
    ),
    "3.3.146": (
        _c('kiṃkila nāma ... — as if he would!',
           {'beside': 'kiṃkila', 'sense': 'amarṣa'},
           note="किंकिलास्त्यर्थेषु लृट्. लिङ्निमित्तमिह नास्ति तेन लृङ् न भवति — a rule's absence as a condition."),
    ),
    "3.3.147": (
        _c('jātu ... yājayet — as though he ever would',
           {'beside': 'jātu', 'sense': 'amarṣa'},
           note='जातुयदोर्लिङ्, and यदायद्योरुपसंख्यानम् adds two more.'),
    ),
    "3.3.148": (
        _c('yac ca ... yājayet — that he should!',
           {'beside': 'yac', 'sense': 'anavakḷpti'},
           note='यच्चयत्रयोः. योगविभाग उत्तरार्थः, यथासंख्यं नेष्यते.'),
    ),
    "3.3.149": (
        _c('yatra ... yājayet — and he a brahmin',
           {'beside': 'yac', 'sense': 'garhā'},
           note='गर्हायां च — the same two companions, another sense.'),
    ),
    "3.3.150": (
        _c('āścaryam etat — how astonishing',
           {'beside': 'yac', 'sense': 'citrīkaraṇa'},
           note='चित्रीकरणे च — the third sense for one pair in three sūtras, which the योगविभाग bought.'),
    ),
    "3.3.151": (
        _c('andho nāma parvatam ārokṣyati — a blind man climbing!',
           {'sense': 'citrīkaraṇa'},
           note='शेषे लृडयदौ. अयदाविति किम्? आश्चर्यं यदि स भुञ्जीत.'),
    ),
    "3.3.152": (
        _c('uta kuryāt — he certainly would',
           {'beside': 'uta'},
           note="उताप्योः समर्थयोर्लिङ्. वोताप्योः इति विकल्पो निवृत्तः — the far end of 3.3.141's option, excluded by it."),
    ),
    "3.3.153": (
        _c('kāmo me bhuñjīta bhavān — I wish you would eat',
           {'sense': 'kāmapravedana'},
           note='कामप्रवेदनेऽकच्चिति. अकच्चितीति किम्? — answered with a VERSE, कच्चिज्जीवति ते माता.'),
    ),
    "3.3.154": (
        _c('api parvataṃ śirasā bhindyāt — he could split a hill',
           {'sense': 'saṃbhāvanā', 'beside': 'alam'},
           note="संभावनेऽलमिति चेत् सिद्धाप्रयोगे — अलम् must be MEANT and NOT uttered. A condition on a word's absence."),
    ),
    "3.3.155": (
        _c('saṃbhāvayāmi bhuñjīta bhavān — I expect you will eat',
           {'sense': 'saṃbhāvanā'},
           note='विभाषा धातौ संभावनवचनेऽयदि. पूर्वेण नित्यप्राप्तौ विकल्पार्थं वचनम्.'),
    ),
    "3.3.156": (
        _c('dakṣiṇena ced yāyāt — if he went south',
           {'sense': 'hetuhetumat'},
           note="हेतुहेतुमतोर्लिङ् — THIS is what 3.3.139's लिङ्निमित्त meant. पुनर्लिङ्ग्रहणं कालविशेषप्रतिपत्त्यर्थम्."),
    ),
    "3.3.157": (
        _c('icchāmi bhuñjīta bhavān — I want you to eat',
           {'sense': 'icchā'},
           note='इच्छार्थेषु लिङ्लोटौ, सर्वलकाराणामपवादः.'),
    ),
    "3.3.158": (
        _c('icchati bhoktum — he wants to eat',
           {'sense': 'icchā', 'samana_kartrka': True},
           note='समानकर्तृकेषु तुमुन्. तुमुन्प्रकृत्यपेक्षमेव समानकर्तृकत्वम्. इच्छन् करोति? अनभिधानात्.'),
    ),
    "3.3.159": (
        _c('bhuñjīyeti icchati — he wishes, may I eat',
           {'sense': 'icchā-samānakartṛka', 'wants': 'liṅ'},
           note='लिङ् च. योगविभाग उत्तरार्थः — the fourth such split here.'),
    ),
    "3.3.160": (
        _c('icchati, icchet — he wishes',
           {'time': 'vartamāna', 'sense': 'icchā'},
           note='इच्छार्थेभ्यो विभाषा वर्तमाने. लटि प्राप्ते वचनम्.'),
    ),
    "3.3.161": (
        _c('kaṭaṃ kuryāt — let him make a mat',
           {'sense': 'vidhi'},
           note='विधिनिमन्त्रणामन्त्रणाधीष्टसंप्रश्नप्रार्थनेषु लिङ्. विध्यादयश्च प्रत्ययार्थविशेषणम् — they qualify the AFFIX.'),
    ),
    "3.3.162": (
        _c('kaṭaṃ karotu — let him make a mat',
           {'sense': 'vidhi', 'wants': 'loṭ'},
           note='लोट् च. योगविभाग उत्तरार्थः — and what it creates is what 3.3.163 must protect the कृत्य affixes from.'),
    ),
    "3.3.163": (
        _c('bhavatā kaṭaḥ karaṇīyaḥ — the mat is to be made by you',
           {'sense': 'praiṣa'},
           note='प्रैषातिसर्गप्राप्तकालेषु कृत्याश्च. And the sixth वासरूप suspension: स्त्र्यधिकारात् परेण वासरूपविधिर्नावश्यं भवति.'),
    ),
    "3.3.164": (
        _c('ūrdhvaṃ muhūrtāt ... kuryāt — after an hour, let him',
           {'sense': 'praiṣa', 'urdhvamauhurtika': True},
           note="लिङ् चोर्ध्वमौहूर्तिके — 3.3.9's condition again, 155 sūtras on and for the same ending."),
    ),
    "3.3.165": (
        _c('kaṭaṃ karotu sma — do make the mat',
           {'sense': 'praiṣa', 'urdhvamauhurtika': True, 'beside': 'sma'},
           note='स्मे लोट्, लिङ्कृत्यानामपवादः — it displaces two rules answering from two different entry points.'),
    ),
    "3.3.166": (
        _c('aṅga sma rājan ... — pray, king, ...',
           {'sense': 'adhīṣṭa', 'beside': 'sma'},
           note='अधीष्टे च. अधीष्टं व्याख्यातम् — the vṛtti points back rather than glossing again.'),
    ),
    "3.3.167": (
        _c('kālo bhoktum — time to eat',
           {'beside': 'kāla'},
           note='कालसमयवेलासु तुमुन्. प्रैषादिग्रहणमिहाभिसंबध्यते, and वासरूपविधिरनित्यः — both borrowed from 3.3.163.'),
    ),
    "3.3.168": (
        _c('kālo yad bhuñjīta bhavān — time you ate',
           {'beside': 'yad', 'sense': 'kāla'},
           note='लिङ् यदि, तुमुनोऽपवादः — it displaces 3.3.167 on the very same companions.'),
    ),
    "3.3.169": (
        _c('bhavatā kanyā voḍhavyā — you should marry the girl',
           {'sense': 'arha'},
           note='अर्हे कृत्यतृचश्च. योऽयमिह लिङ् विधीयते, तेन बाधा मा भूदिति — protecting half of itself from the other half.'),
    ),
    "3.3.170": (
        _c('śataṃ dāyī — owing a hundred',
           {'sense': 'ādhamarṇya'},
           note='आवश्यकाधमर्ण्ययोर्णिनिः. उपाधिरयम्, नोपपदम्.'),
    ),
    "3.3.171": (
        _c('avaśyaṃ kartavyaḥ — must be done',
           {'sense': 'āvaśyaka', 'wants': 'kṛtya'},
           note='कृत्याश्च. कर्तरि णिनिः, भावकर्मणोः कृत्याः, तत्र कुतो बाधप्रसङ्गः? — an objection left standing.'),
    ),
    "3.3.172": (
        _c('bhavān bhāraṃ vahet — you could carry the load',
           {'sense': 'śakti'},
           note="शकि लिङ् च. शकीति प्रकृत्यर्थविशेषणम् — the opposite of 3.3.161's प्रत्ययार्थविशेषणम्."),
    ),
    "3.3.173": (
        _c('ciraṃ jīvyād bhavān — may you live long',
           {'sense': 'āśis'},
           note="आशिषि लिङ्लोटौ. Its gloss of आशीः is word for word 3.3.132's gloss of आशंसा."),
    ),
    "3.3.174": (
        _c('bhavatāt bhūtiḥ — may there be prosperity',
           {'sense': 'āśis', 'samjna': True},
           note='क्तिच्क्तौ च संज्ञायाम्, समुदायेन चेत् संज्ञा गम्यते — the seventh समुदायोपाधि.'),
    ),
    "3.3.175": (
        _c('mā kārṣīt — let him not do it',
           {'beside': 'māṅ'},
           note='माङि लुङ्. कथं मा भवतु तस्य पापम्? असाधुरेवायम् — a form in use called wrong, then half-saved by others.'),
    ),
    "3.3.176": (
        _c('mā sma karot — do not do it',
           {'beside': 'sma-māṅ'},
           note="स्मोत्तरे लङ् च, चकाराल्लुङ् च. The last sūtra of the pāda, and the Kāśikā's colophon follows."),
    ),
    "3.4.1": (
        _c('putro janitā — a son will be born',
           {'related': True},
           note='धातुसंबन्धे प्रत्ययाः — अयथाकालोक्ता अपि प्रत्ययाः साधवो भवन्ति. विशेषणं ... विशेष्यकालमनुरुध्यते, तेन विपर्ययो न भवति — one way round only.'),
    ),
    "3.4.2": (
        _c('lunīhi lunīhi ... lunāti — he cuts and cuts',
           {'time': 'sarva', 'sense': 'kriyāsamabhihāra', 'doubled': True},
           note='क्रियासमभिहारे लोट्, सर्वेषु कालेषु. योगविभागोऽत्र कर्तव्यः, so लोड्धर्माणौ हिस्वौ भवतः and the voice distinction survives.'),
    ),
    "3.4.3": (
        _c('bhrāṣṭram aṭa, maṭham aṭa — go to the oven, the hut',
           {'time': 'sarva', 'sense': 'samuccaya', 'doubled': True},
           note='समुच्चये सामान्यवचनस्य, अन्यतरस्याम् — and the vṛtti writes out the whole paradigm twice, in both voices.'),
    ),
    "3.4.4": (
        _c('lunātīti — ... he cuts',
           {},
           note='यथाविध्यनुप्रयोगः — स एव धातुरनुप्रयोक्तव्यः. छिनत्तीति नानुप्रयुज्यते.'),
    ),
    "3.4.5": (
        _c('ity evāyam abhyavaharati — so he takes food',
           {'gathered': True},
           note='समुच्चयेऽन्यतरस्याम्. लाघवं च लौकिके शब्दव्यवहारे नाद्रियते — brevity is no consideration in ordinary speech.'),
    ),
    "3.4.6": (
        _c('adyā mamāra — today he dies',
           {'time': 'sarva', 'chandasi': True},
           note='छन्दसि लुङ्लङ्लिटः (ऋ० १०.५५.५) — the rule 3.2.105 has been citing. अन्यतरस्यामिति वर्तते, तेनान्येऽपि लकारा यथायथं भवन्ति.'),
    ),
    "3.4.7": (
        _c('patāti didyut — may the lightning fall',
           {'time': 'sarva', 'chandasi': True, 'lin_nimitta': True},
           note='लिङर्थे लेट् (ऋ० ७.२५.१) — लिङर्थे, यत्र लिङ् विधीयते ... हेतुहेतुमतोर्लिङ् इत्येवमादिः, which is 3.3.156.'),
    ),
    "3.4.8": (
        _c('narakaṃ patāma — lest we fall into hell',
           {'time': 'sarva', 'chandasi': True, 'sense': 'upasaṃvāda'},
           note='उपसंवादाशङ्कयोश्च. उपसंवादः परिभाषणम्, कर्तव्ये पणबन्धः. लिङर्थ एवायं नित्यार्थं तु वचनम्.'),
    ),
    "3.4.9": (
        _c('jīvase — to live',
           {},
           note='तुमर्थे से-सेन्-असे-असेन्... (शौ०सं० ६.१९.२) — fifteen affixes. तुमर्थो भावः, argued in four steps from परि० ११३.'),
    ),
    "3.4.10": (
        _c('prayai devebhyaḥ — to go to the gods',
           {'word': 'prayai'},
           note='प्रयै रोहिष्यै अव्यथिष्यै च (ऋ० १.१४२.६) — three निपातन, two different affixes, and one of them on a NEGATED stem.'),
    ),
    "3.4.11": (
        _c('dṛśe viśvāya sūryam — the sun, for all to see',
           {'word': 'dṛśe'},
           note='दृशे विख्ये च (ऋ० १.५०.१) — दृशेः केप्रत्ययः. And विख्ये rests on ख्या, which 2.4.54 makes out of चक्षिङ्.'),
    ),
    "3.4.12": (
        _c('vibhājaṃ nāśaknuvan — they could not divide it',
           {'beside': 'śak'},
           note='शकि णमुल्कमुलौ (मै०सं० १.६.४). णकारो वृद्ध्यर्थः, ककारो गुणवृद्धिप्रतिषेधार्थः — one letter apart and contrary.'),
    ),
    "3.4.13": (
        _c("īśvaro'bhicaritoḥ — able to bewitch",
           {'beside': 'īśvara'},
           note='ईश्वरे तोसुन्कसुनौ — two affixes, and the three examples divide between them with no ground stated.'),
    ),
    "3.4.14": (
        _c('anvetavai — to be followed (ऋ० ७.४४.५)',
           {'krtya_artha': True},
           note='कृत्यार्थे तवैकेन्केन्यत्वनः. तवै was given at 3.4.9 already, तस्य तुमर्थादन्यत्र कारके विधिर्द्रष्टव्यः.'),
    ),
    "3.4.15": (
        _c('nāvacakṣe — not to be looked at (मा०सं० १७.९३)',
           {'word': 'avacakṣe'},
           note="अवचक्षे च — a निपातन sharing the run's कृत्य sense rather than standing alone."),
    ),
    "3.4.16": (
        _c('purā sūryasyodetoḥ — before sunrise',
           {'root': 'iṇ', 'bhava_laksana': True},
           note="भावलक्षणे स्थेण्कृञ्... तोसुन् (काठ०सं० ८.३). भावो लक्ष्यते येन — the word means 'before', not the act."),
    ),
    "3.4.17": (
        _c('purā jatrubhya ātṛdaḥ — before piercing',
           {'root': 'tṛd', 'bhava_laksana': True},
           note='सृपितृदोः कसुन् (ऋ० ८.१.१२).'),
    ),
    "3.4.18": (
        _c('alaṃ kṛtvā — enough of doing',
           {'beside': 'alam'},
           note='अलंखल्वोः प्रतिषेधयोः प्राचां क्त्वा — attributed to the EASTERN teachers, and प्राचांग्रहणं विकल्पार्थम्. प्रतिषेधयोरिति किम्? अलंकारः.'),
    ),
    "3.4.19": (
        _c('apamitya yācate — having borrowed, he asks',
           {'root': 'mā', 'vyatihara': True},
           note='उदीचां माङो व्यतीहारे. मेङः कृतात्वस्यायं निर्देशः कृतो ज्ञापनार्थः — नानुबन्धकृतमनेजन्तत्वम्, reaching 1.1.20.'),
    ),
    "3.4.20": (
        _c('aprāpya nadīṃ — short of the river',
           {'paravara': True},
           note='परावरयोगे च — a condition about how two things are PLACED.'),
    ),
    "3.4.21": (
        _c('bhuktvā vrajati — having eaten, he goes',
           {'samana_kartrka': True, 'purvakala': True},
           note='समानकर्तृकयोः पूर्वकाले. शक्तिशक्तिमतोर्भेदस्यअविवक्षितत्वात्, and द्विवचनमतन्त्रम्.'),
    ),
    "3.4.22": (
        _c('bhojaṃbhojaṃ vrajati — eating and eating',
           {'samana_kartrka': True, 'purvakala': True, 'abhiksnya': True},
           note='आभीक्ष्ण्ये णमुल् च. द्विर्वचनसहितौ ... द्योतयतः, न केवलौ — the affix cannot carry its own sense.'),
    ),
    "3.4.23": (
        _c('yad ayaṃ bhuṅkte tataḥ paṭhati — when he eats, he reads',
           {'beside': 'yad', 'anakanksa': True},
           note='न यद्यनाकाङ्क्षे. णमुलनन्तरः, क्त्वा तु पूर्वसूत्रविहितोऽपि प्रतिषिध्यते — a refusal reaching past its neighbour.'),
    ),
    "3.4.24": (
        _c('agre bhuktvā vrajati — having eaten first, he goes',
           {'beside': 'agre', 'samana_kartrka': True, 'purvakala': True},
           note='विभाषाग्रेप्रथमपूर्वेषु. क्त्वाणमुलौ यत्र सह विधीयेते तत्र वासरूपविधिर्नास्ति — the seventh suspension, bounded by a PAIR OF AFFIXES rather than by a section.'),
    ),
    "3.4.25": (
        _c('coraṃkāram ākrośati — he abuses him as a thief',
           {'root': 'kṛ', 'karman': True, 'sense': 'ākrośa'},
           note='कर्मणि भृत्यादिषु खमुञ्. चोरकरणम् आक्रोशसंपादनार्थमेव, न त्वसौ चोरः क्रियते — the act the rule names is not done.'),
    ),
    "3.4.26": (
        _c('svāduṃkāraṃ bhuṅkte — he makes it tasty and eats',
           {'root': 'kṛ', 'karman': True, 'beside': 'svādu', 'samana_kartrka': True, 'purvakala': True},
           note="स्वादुमि णमुल्. स्वादुमीति मकारान्तनिपातनम् — one spelling doing three jobs. And शक्तिशक्तिमतोर्भेदो न विवक्ष्यते, 3.4.21's ground the other way round."),
    ),
    "3.4.27": (
        _c('anyathākāraṃ bhuṅkte — he eats otherwise',
           {'root': 'kṛ', 'beside': 'anyathā', 'siddha_aprayoga': True},
           note='कर्मण्यन्यथैवंकथमित्थंसु सिद्धाप्रयोगश्चेत् — निरर्थकत्वाद् न प्रयोगमर्हति. सिद्धाप्रयोग इति किम्? अन्यथा कृत्वा शिरो भुङ्क्ते.'),
    ),
    "3.4.28": (
        _c('yathākāram ahaṃ bhokṣye — I shall eat as I shall',
           {'root': 'kṛ', 'beside': 'yathā', 'siddha_aprayoga': True, 'sense': 'asūyā-prativacana'},
           note='यथातथयोरसूयाप्रतिवचने — यद्यसूयन् पृच्छति प्रतिवक्ति तत्र प्रतिवचनम्, a condition on a whole exchange.'),
    ),
    "3.4.29": (
        _c('kanyādarśaṃ varayati — he woos every girl he sees',
           {'root': 'dṛś', 'karman': True, 'sense': 'sākalya'},
           note='कर्मणि दृशिविदोः साकल्ये. साकल्य इति किम्? ब्राह्मणं दृष्ट्वा भोजयति — the exhaustiveness is of the OBJECTS.'),
    ),
    "3.4.30": (
        _c('yāvajjīvam adhīte — he studies as long as he lives',
           {'root': 'vid', 'beside': 'yāvat'},
           note="यावति विन्दजीवोः — 'as much as' with one root and 'as long as' with the other, and the rule says neither."),
    ),
    "3.4.31": (
        _c('udarapūraṃ bhuṅkte — he eats his fill',
           {'root': 'pūr', 'karman': True, 'beside': 'udara'},
           note='चर्मोदरयोः पूरेः.'),
    ),
    "3.4.32": (
        _c('goṣpadapūraṃ vṛṣṭo devaḥ — a hoofprint of rain',
           {'root': 'pūr', 'karman': True, 'sense': 'varṣa-pramāṇa'},
           note='वर्षप्रमाण ऊलोपश्चास्यान्यतरस्याम्. अस्यग्रहणं किमर्थम्? उपपदस्य मा भूत् — a word spent entirely on scope.'),
    ),
    "3.4.33": (
        _c('celaknopaṃ vṛṣṭo devaḥ — rain enough to wet a cloth',
           {'root': 'knūy', 'karman': True, 'beside': 'cela', 'sense': 'varṣa-pramāṇa'},
           note='चेलार्थेषु क्नूयेर्ण्यन्तस्य वर्षप्रमाणे — the companion named BY SENSE, so the three given are examples.'),
    ),
    "3.4.34": (
        _c('samūlakāṣaṃ kaṣati — he scrapes it out root and all',
           {'root': 'kaṣ', 'karman': True, 'beside': 'nimūla'},
           note='निमूलसमूलयोः कषः. इतः प्रभृति कषादीन् यान् वक्ष्यति — the कषादि class starts here and 3.4.46 will govern it.'),
    ),
    "3.4.35": (
        _c('śuṣkapeṣaṃ pinaṣṭi — he grinds it dry',
           {'root': 'piṣ', 'karman': True, 'beside': 'śuṣka'},
           note='शुष्कचूर्णरूक्षेषु पिषः — each glossed by dropping the affix, शुष्कं पिनष्टीत्यर्थः.'),
    ),
    "3.4.36": (
        _c('jīvagrāhaṃ gṛhṇāti — he takes him alive',
           {'root': 'grah', 'karman': True, 'beside': 'jīva'},
           note='समूलाकृतजीवेषु हन्कृञ्ग्रहः, यथासंख्यम् — three companions bound to three roots.'),
    ),
    "3.4.37": (
        _c('pāṇighātaṃ vediṃ hanti — he strikes the altar',
           {'root': 'han', 'karaka': 'karaṇa'},
           note='करणे हनः. पूर्वविप्रतिषेधेन हन्तेर्हिंसार्थस्यापि प्रत्ययोऽनेनैवेष्यते — an EARLIER rule made to beat a later one.'),
    ),
    "3.4.38": (
        _c('tailapeṣaṃ pinaṣṭi — he grinds it with oil',
           {'root': 'piṣ', 'karaka': 'karaṇa', 'sense': 'snehana'},
           note='स्नेहने पिषः. स्निह्यते येन तत् स्नेहनम्.'),
    ),
    "3.4.39": (
        _c('hastagrāhaṃ gṛhṇāti — he takes it in his hand',
           {'root': 'vṛt', 'karaka': 'karaṇa', 'beside': 'hasta'},
           note='हस्ते वर्तिग्रहोः. हस्त इत्यर्थग्रहणम् — taken by SENSE, so कर and पाणि are reached.'),
    ),
    "3.4.40": (
        _c('svapoṣaṃ puṣṇāti — he nourishes with his own',
           {'root': 'puṣ', 'karaka': 'karaṇa', 'beside': 'sva'},
           note='स्वे पुषः. आत्मात्मीयज्ञातिधनवचनः स्वशब्दः — four senses of one word, seven examples across them.'),
    ),
    "3.4.41": (
        _c('cakrabandhaṃ badhnāti — he ties a wheel-knot',
           {'root': 'bandh', 'karaka': 'adhikaraṇa'},
           note='अधिकरणे बन्धः.'),
    ),
    "3.4.42": (
        _c('krauñcabandhaṃ badhnāti — a heron-knot',
           {'root': 'bandh', 'samjna': True},
           note='संज्ञायाम् — बन्धविशेषाणां नामधेयान्येतानि, and no kāraka named.'),
    ),
    "3.4.43": (
        _c('puruṣavāhaṃ vahati — a man carries it',
           {'root': 'vah', 'karaka': 'kartṛ', 'beside': 'puruṣa'},
           note='जीवपुरुषयोर्नशिवहोः, यथासंख्यम्. कर्तरीति किम्? पुरुषेणोढः.'),
    ),
    "3.4.44": (
        _c('ūrdhvaśoṣaṃ śuṣyati — it dries standing up',
           {'root': 'śuṣ', 'karaka': 'kartṛ', 'beside': 'ūrdhva'},
           note='ऊर्ध्वे शुषिपूरोः, कर्तृग्रहणम् running down.'),
    ),
    "3.4.45": (
        _c('ghṛtanidhāyaṃ nihitaḥ — laid down like ghee',
           {'karaka': 'upamāna'},
           note='उपमाने कर्मणि च — and by the च the agent too, अजकनाशं नष्टः.'),
    ),
    "3.4.46": (
        _c('samūlakāṣaṃ kaṣati — he scrapes it root and all',
           {'kashadi': True},
           note='कषादिषु यथाविध्यनुप्रयोगः — the class 3.4.34 opened. यथाविधीति नियमार्थं वचनम्, restrictive not prescriptive.'),
    ),
    "3.4.47": (
        _c('mūlakopadaṃśaṃ bhuṅkte — he eats it with radish',
           {'root': 'daṃś', 'vibhakti': 'tṛtīyā'},
           note="उपदंशस्तृतीयायाम् — the first rule to divide by the companion's CASE. मूलकादि चोपदंशेः कर्म, भुजेः करणम्."),
    ),
    "3.4.48": (
        _c('daṇḍopaghātaṃ gāḥ kālayati — driving them with a stick',
           {'vibhakti': 'tṛtīyā', 'sense': 'hiṃsā'},
           note='हिंसार्थानां च समानकर्मकाणाम्. समानकर्मकाणामिति किम्? चोरं दण्डेनोपहत्य गोपालको गाः कालयति.'),
    ),
    "3.4.49": (
        _c('pārśvopapīḍaṃ śete — he lies pressing his side',
           {'root': 'pīḍ', 'vibhakti': 'saptamī'},
           note='सप्तम्यां चोपपीडरुधकर्षः. उपशब्दः प्रत्येकमभिसंबध्यते, and कर्षतेरिदं ग्रहणम्, न कृषतेः.'),
    ),
    "3.4.50": (
        _c('keśagrāhaṃ yudhyante — they fight by the hair',
           {'vibhakti': 'tṛtīyā', 'sense': 'samāsatti'},
           note='समासत्तौ — युद्धसंरम्भादत्यन्तं सन्निकृष्यन्त इत्यर्थः.'),
    ),
    "3.4.51": (
        _c('dvyaṅgulotkarṣaṃ chinatti — he cuts two fingers up',
           {'vibhakti': 'tṛtīyā', 'sense': 'pramāṇa'},
           note='प्रमाणे — प्रमाणमायामः, दैर्घ्यम्, narrowed to LENGTH.'),
    ),
    "3.4.52": (
        _c('śayyotthāyaṃ dhāvati — he runs, leaping from bed',
           {'karaka': 'apādāna', 'sense': 'parīpsā'},
           note='अपादाने परीप्सायाम् — एवं नाम त्वरते यदवश्यं कर्तव्यमपि नापेक्षते.'),
    ),
    "3.4.53": (
        _c('yaṣṭigrāhaṃ yudhyante — snatching up sticks',
           {'vibhakti': 'dvitīyā', 'sense': 'parīpsā'},
           note='द्वितीयायां च — यद् आयुधग्रहणमपि नाद्रियते.'),
    ),
    "3.4.54": (
        _c('akṣinikāṇaṃ jalpati — he talks with a wink',
           {'vibhakti': 'dvitīyā', 'svanga': True, 'adhruva': True},
           note='स्वाङ्गेऽध्रुवे — यस्मिन्नङ्गे छिन्नेऽपि प्राणी न म्रियते तदध्रुवम्.'),
    ),
    "3.4.55": (
        _c('uraḥpeṣaṃ yudhyante — they fight chest to chest',
           {'vibhakti': 'dvitīyā', 'svanga': True, 'sense': 'parikleśa'},
           note='परिक्लिश्यमाने च, ध्रुवार्थोऽयमारम्भः — for the limbs 3.4.54 shut out.'),
    ),
    "3.4.56": (
        _c('gehānupraveśam āste — he keeps going into the houses',
           {'root': 'viś', 'vibhakti': 'dvitīyā', 'sense': 'vyāpti'},
           note='विशिपतिपदिस्कन्दां व्याप्यमानासेव्यमानयोः — द्रव्ये व्याप्तिः, क्रियायामासेवा, and the doubling falls differently in each.'),
    ),
    "3.4.57": (
        _c('dvyahātyāsaṃ gāḥ pāyayati — watering every third day',
           {'root': 'as', 'vibhakti': 'dvitīyā', 'sense': 'kriyāntara'},
           note='अस्यतितृषोः क्रियान्तरे कालेषु — अध्वकर्मकमत्यसनं व्यवधायकम्, न कालकर्मकम्.'),
    ),
    "3.4.58": (
        _c('nāmagrāham ācaṣṭe — he tells it naming names',
           {'root': 'ādiś', 'vibhakti': 'dvitīyā', 'beside': 'nāman'},
           note='नाम्न्यादिशिग्रहोः — passed without comment, which is rare in these four pādas.'),
    ),
    "3.4.59": (
        _c('nīcaiḥkāram ācaṣṭe — he tells it in a low voice',
           {'root': 'kṛ', 'beside': 'avyaya', 'sense': 'ayathābhipretākhyāna'},
           note='अव्यये यथाभिप्रेताख्याने कृञः क्त्वाणमुलौ. क्त्वाग्रहणं समासार्थम्; णमुल्ग्रहणं तुल्यकक्षत्वज्ञापनार्थम्.'),
    ),
    "3.4.60": (
        _c('tiryakkṛtya gataḥ — having finished, he went',
           {'root': 'kṛ', 'beside': 'tiryac', 'sense': 'apavarga'},
           note='तिर्यच्यपवर्गे. तिर्यचीति शब्दानुकरणम् — an imitation must not behave like its original, अनुक्रियमाणरूपविनाशप्रसङ्गात्.'),
    ),
    "3.4.61": (
        _c('mukhataḥkṛtya gataḥ — having put it in front',
           {'root': 'kṛ', 'beside': 'mukhatas', 'svanga': True},
           note='स्वाङ्गे तस्प्रत्यये कृभ्वोः. यथासंख्यमत्र नेष्यते, अस्वरितत्वात् — an argument from an accent the corpus cannot show.'),
    ),
    "3.4.62": (
        _c('nānākṛtya gataḥ — having separated them',
           {'root': 'kṛ', 'beside': 'nānā', 'sense': 'cvi'},
           note='नाधार्थप्रत्यये च्व्यर्थे. धार्थमर्थग्रहणम्, ना पुनरेक एव — one compound read two ways.'),
    ),
    "3.4.63": (
        _c('tūṣṇīṃbhūya gataḥ — having fallen silent',
           {'root': 'bhū', 'beside': 'tūṣṇīm'},
           note='तूष्णीमि भुवः. भूग्रहणं कृञो निवृत्त्यर्थम् — a root named to exclude another.'),
    ),
    "3.4.64": (
        _c('anvagbhūyāste — he sits complying',
           {'root': 'bhū', 'beside': 'anvac', 'sense': 'ānulomya'},
           note='अन्वच्यानुलोम्ये. आनुलोम्यमनुलोमता, अनुकूलत्वम्, परचित्तानुविधानम् — three glosses, the last a description.'),
    ),
    "3.4.65": (
        _c('śaknoti bhoktum — he can eat',
           {'beside': 'śak'},
           note='शकधृषज्ञा… अस्त्यर्थेषु तुमुन्. अक्रियार्थोपपदार्थोऽयम् आरम्भः — defined by the condition it drops.'),
    ),
    "3.4.66": (
        _c('alaṃ bhoktum — enough to eat',
           {'beside': 'alam', 'sense': 'paryāpti'},
           note='पर्याप्तिवचनेष्वलमर्थेषु. पर्याप्तिवचनेष्विति किम्? अलं कृत्वा. अलमर्थेष्विति किम्? पर्याप्तं भुङ्क्ते — the two counters cross.'),
    ),
    "3.4.67": (
        _c('kārakaḥ, kartā — a doer, an agent',
           {'affix': 'ṇvul'},
           note='कर्तरि कृत् — a HEADING, and the question changes from which affix comes to what it stands for. तत्र येष्वर्थादेशो नास्ति तत्रेदमुपतिष्ठते.'),
    ),
    "3.4.68": (
        _c('geyo māṇavakaḥ — the boy who sings',
           {'word': 'geya'},
           note='भव्यगेयप्रवचनीय… वा — seven words allowed to denote the DOER where 3.4.70 would hold them to the act and object.'),
    ),
    "3.4.69": (
        _c('gacchati grāmaṃ devadattaḥ — he goes to the village',
           {'affix': 'la'},
           note='लः कर्मणि च भावे चाकर्मकेभ्यः — WHAT A लकार DENOTES, the debt carried since 3.2.110. ल इत्युत्सृष्टानुबन्धं सामान्यं गृह्यते, so one rule answers for all ten.'),
    ),
    "3.4.70": (
        _c('kartavyaḥ kaṭo bhavatā — the mat is to be made',
           {'affix': 'kṛtya'},
           note="तयोरेव कृत्यक्तखलर्थाः. एवकारः कर्तुरपकर्षणार्थः — a word spent to undo 3.4.67's heading for one class."),
    ),
    "3.4.71": (
        _c('prakṛtaḥ kaṭaṃ devadattaḥ — he has begun the mat',
           {'affix': 'kta', 'adikarman': True},
           note='आदिकर्मणि क्तः कर्तरि च. आदिभूतः क्रियाक्षण आदिकर्म, तस्मिन् भूतत्वेन विवक्षिते — the beginning spoken of as past.'),
    ),
    "3.4.72": (
        _c('gato devadatto grāmam — he has gone to the village',
           {'affix': 'kta', 'root_sense': 'gati'},
           note='गत्यर्थाकर्मकश्लिष… क्तः कर्तरि. श्लिषादयः सोपसर्गाः सकर्मका भवन्ति, तदर्थमेषामुपादानम्.'),
    ),
    "3.4.73": (
        _c('goghnaḥ — a guest, for whom a cow is killed',
           {'word': 'goghna'},
           note='दाशगोघ्नौ संप्रदाने. निपातनसामर्थ्यादेव गोघ्न ऋत्विगादिरुच्यते, and असत्यपि च गोहनने तस्य योग्यतया.'),
    ),
    "3.4.74": (
        _c('bhīmaḥ — terrible, that from which one fears',
           {'word': 'bhīma'},
           note='भीमादयोऽपादाने. उणादिप्रत्ययान्ता एते — श्याधूसूभ्यो मक् (प०उ० १.१४५), cited by number into the text on disk.'),
    ),
    "3.4.75": (
        _c('carma — a hide, what has been ranged over',
           {'unadi': True},
           note='ताभ्यामन्यत्रोणादयः. ताभ्यामिति संप्रदानप्रत्यवमर्शार्थम्, अन्यथा ह्यपादानमेव पर्युदस्येत, अनन्तरत्वात्.'),
    ),
    "3.4.76": (
        _c('idam eṣām āsitam — this is where they sat',
           {'affix': 'kta', 'root_sense': 'dhrauvya'},
           note='ध्रौव्यगतिप्रत्यवसानार्थेभ्यश्च. कथं भुक्ता ब्राह्मणाः? अकारो मत्वर्थीयः — a form saved by parsing it otherwise.'),
    ),
    "3.4.77": (
        _c('laṭ — the first of the ten',
           {'name': 'laṭ'},
           note='लस्य — दश लकारा ... तेषां विशेषकराननुबन्धानुत्सृज्य यत् सामान्यं तद् गृह्यते. षट् टितः, चत्वारो ङितः.'),
    ),
    "3.4.78": (
        _c('pacati — he cooks',
           {'lakara': 'laṭ'},
           note='लस्य तिबादय आदेशाः. महिङो ङकारस्तिङ् इति प्रत्याहारग्रहणार्थः — the last letter of the last substitute is what names the whole set, and 3.4.113 stands on that name.'),
    ),
    "3.4.80": (
        _c('pacase — you cook, in the middle voice',
           {'of': 'thās', 'lakara': 'laṭ'},
           note="थासः से. टित इत्येव — the rule names no लकार and takes six of the ten from 3.4.79's word."),
    ),
    "3.4.81": (
        _c('pece — he cooked, in the middle voice',
           {'of': 'ta', 'lakara': 'liṭ', 'ending_pada': 'ātmanepada'},
           note='लिटस्तझयोरेशिरेच्, यथासंख्यम्. शकारः सर्वादेशार्थः, चकारः स्वरार्थः.'),
    ),
    "3.4.82": (
        _c('papāca — he cooked',
           {'of': 'tip', 'lakara': 'liṭ', 'ending_pada': 'parasmaipada'},
           note='परस्मैपदानां णलतुसुस्थलथुसणल्वमाः. णल् stands twice in the nine, so पपाच is both *he cooked* and *I cooked*.'),
    ),
    "3.4.83": (
        _c('veda — he knows, a present sense in a perfect shape',
           {'of': 'tip', 'lakara': 'laṭ', 'root': 'vid', 'ending_pada': 'parasmaipada'},
           note='विदो लटो वा. वेद, विदतुः, विदुः beside वेत्ति, वित्तः, विदन्ति — and this वा outlives the rule by sixteen sūtras.'),
    ),
    "3.4.84": (
        _c('āha — he says, and the root replaced in the same act',
           {'of': 'tip', 'lakara': 'laṭ', 'root': 'brū', 'ending_pada': 'parasmaipada'},
           note='ब्रुवः पञ्चानामादित आहो ब्रुवः. पञ्चानामिति किम्? ब्रूथ — the sixth stands, so the paradigm breaks in the middle.'),
    ),
    "3.4.85": (
        _c('pacatām — let them two cook, by borrowing the imperfect',
           {'lakara': 'loṭ'},
           note='लोटो लङ्वत्, अतिदेशोयम्. तामादयस्सलोपश्च — and अडाटौ कस्माद् न भवतः is what the rule does NOT carry.'),
    ),
    "3.4.86": (
        _c('pacatu — let him cook',
           {'of': 'i', 'lakara': 'loṭ'},
           note='एरुः. हिन्योरुत्वप्रतिषेधो वक्तव्यः (म०भा० वा० १); न वोच्चारणसामर्थ्यात्.'),
    ),
    "3.4.87": (
        _c('lunīhi — cut!',
           {'of': 'sip', 'lakara': 'loṭ'},
           note='सेर्ह्यपिच्च. स्थानिवद्भावात् पित्त्वं प्राप्तं प्रतिषिध्यते — half the rule cancels an inheritance.'),
    ),
    "3.4.88": (
        _c('yuyodhi — ward off!, in the Veda',
           {'of': 'hi', 'lakara': 'loṭ', 'chandasi': True},
           note='वा छन्दसि, अपित्त्वं विकल्प्यते. युयोध्यस्मज्जुहुराणमेनः (ऋ० १.१८९.१), and प्रीणाहि beside प्रीणीहि.'),
    ),
    "3.4.89": (
        _c('pacāni — let me cook',
           {'of': 'mip', 'lakara': 'loṭ'},
           note='मेर्निः, उत्वलोपयोरपवादः — one rule excepting two, three sūtras away in opposite directions.'),
    ),
    "3.4.90": (
        _c('pacatām — let him cook, in the middle voice',
           {'of': 'e', 'lakara': 'loṭ'},
           note="आमेतः. The ए is 3.4.79's, so this works on the output of a rule eleven sūtras back."),
    ),
    "3.4.91": (
        _c('pacasva — cook!, in the middle voice',
           {'of': 'e', 'lakara': 'loṭ', 'preceded_by': 'sa/va'},
           note='सवाभ्यां वामौ, आमोऽपवादः. The condition is a SOUND, and the स is there because 3.4.80 put it there.'),
    ),
    "3.4.92": (
        _c('karavāṇi — let me do',
           {'lakara': 'loṭ', 'person': 'uttama', 'wants': 'āgama'},
           note='आडुत्तमस्य पिच्च. The आ is what makes an imperative *let me* audibly longer than the indicative.'),
    ),
    "3.4.93": (
        _c('karavai — let me do, in the middle voice',
           {'of': 'e', 'lakara': 'loṭ', 'person': 'uttama'},
           note='एत ऐ, आमोऽपवादः. इह कस्माद् न भवति पचावेदम्? बहिरङ्गलक्षणत्वाद् गुणस्य.'),
    ),
    "3.4.94": (
        _c('joṣiṣat — may he enjoy',
           {'lakara': 'leṭ', 'wants': 'āgama'},
           note='लेटोऽडाटौ, पर्यायेण. जोषिषत् (ऋ० २.३५.१), पताति दिद्युत् (ऋ० ७.२५.१).'),
    ),
    "3.4.95": (
        _c('mantrayaite — may they two take counsel',
           {'of': 'ā', 'lakara': 'leṭ', 'ending_pada': 'ātmanepada'},
           note='आत ऐ, in the dual of the third and second person middle alone. आटः कस्माद् न भवति? विधानसामर्थ्यात्.'),
    ),
    "3.4.96": (
        _c('śāsai — may I rule',
           {'of': 'e', 'lakara': 'leṭ'},
           note="वैतोऽन्यत्र. अन्यत्रेत्यनन्तरो विधिरपेक्ष्यते — 'elsewhere' looks exactly one rule back."),
    ),
    "3.4.97": (
        _c('joṣiṣat — may he enjoy, with the इ dropped',
           {'of': 'i', 'lakara': 'leṭ', 'ending_pada': 'parasmaipada'},
           note='इतश्च लोपः परस्मैपदेषु. परस्मैपदग्रहणमिड्वहिमहिङां मा भूत् — three of the eighteen protected by one word.'),
    ),
    "3.4.98": (
        _c('karavāva — may we two do',
           {'of': 's', 'lakara': 'leṭ', 'person': 'uttama'},
           note="स उत्तमस्य. The last rule 3.4.83's वा reaches, and the next spends a word to end it."),
    ),
    "3.4.99": (
        _c('apacāva — we two cooked',
           {'of': 's', 'lakara': 'laṅ', 'person': 'uttama'},
           note='नित्यं ङितः. नित्यग्रहणं विकल्पनिवृत्त्यर्थम् — one syllable to kill an option the rule does not state.'),
    ),
    "3.4.100": (
        _c('apacat — he cooked',
           {'of': 'i', 'lakara': 'laṅ', 'ending_pada': 'parasmaipada'},
           note='इतश्च. परस्मैपदेष्वित्येव — अपचावहि, अपचामहि keep their इ.'),
    ),
    "3.4.101": (
        _c('apacatām — they two cooked',
           {'of': 'tas', 'lakara': 'laṅ'},
           note='तस्थस्थमिपां तांतंतामः, यथासंख्यम्. Four of the eighteen, and not a natural class in the paradigm.'),
    ),
    "3.4.102": (
        _c('paceta — he might cook, in the middle voice',
           {'lakara': 'liṅ', 'wants': 'āgama'},
           note='लिङः सीयुट्. टकारो देशविध्यर्थः, उकार उच्चारणार्थः — two letters of four doing no work in the word.'),
    ),
    "3.4.103": (
        _c('kuryāt — he should do',
           {'lakara': 'liṅ', 'ending_pada': 'parasmaipada', 'wants': 'āgama'},
           note='यासुट् परस्मैपदेषूदात्तो ङिच्च, सीयुटोऽपवादः. The ङित् is said redundantly, and the redundancy teaches लकाराश्रयङित्त्वमादेशानां न भवति.'),
    ),
    "3.4.104": (
        _c('ucyāt — may he speak',
           {'of': 'yāsuṭ', 'lakara': 'liṅ', 'sense': 'āśis'},
           note='किदाशिषि. आशिषीति किम्? वच्यात्, जागृयात् — the same roots without the blessing.'),
    ),
    "3.4.105": (
        _c('paceran — they might cook, in the middle voice',
           {'of': 'jha', 'lakara': 'liṅ'},
           note='झस्य रन्, झोऽन्तापवादः — it reaches झ before 7.1.3 could.'),
    ),
    "3.4.106": (
        _c('paceya — I might cook, in the middle voice',
           {'of': 'iṭ', 'lakara': 'liṅ'},
           note='इटोऽत्. आगमस्येटो ग्रहणं न भवति, अर्थवद्ग्रहणे नानर्थकस्य (परि० १४) — two things wearing one name.'),
    ),
    "3.4.107": (
        _c('kṛṣīṣṭa — may he plough',
           {'of': 'ta', 'lakara': 'liṅ', 'wants': 'āgama'},
           note='सुट् तिथोः. तेन भिन्नविषयत्वात् सुटा बाधनं न भवति — two augments on different grounds do not compete.'),
    ),
    "3.4.108": (
        _c('paceyuḥ — they might cook',
           {'of': 'jhi', 'lakara': 'liṅ'},
           note='झेर्जुस्, झोऽन्तापवादः. The first of five rules in the pāda to give जुस्.'),
    ),
    "3.4.109": (
        _c('akārṣuḥ — they did',
           {'of': 'jhi', 'lakara': 'laṅ', 'preceded_by': 'sic/abhyasta/vid'},
           note='सिजभ्यस्तविदिभ्यश्च, अलिङर्थ आरम्भः. अभ्यस्तविदिग्रहणमसिजर्थम् — one condition and two exemptions from it.'),
    ),
    "3.4.110": (
        _c('aduḥ — they gave',
           {'of': 'jhi', 'lakara': 'luṅ', 'preceded_by': 'ā'},
           note='आतः. पूर्वेणैव सिद्धे नियमार्थं वचनम् — stated to restrict, and अभूवन् is the proof.'),
    ),
    "3.4.111": (
        _c("ayuḥ — they went, in Śākaṭāyana's view",
           {'of': 'jhi', 'lakara': 'laṅ', 'preceded_by': 'ā'},
           note='लङः शाकटायनस्यैव. अन्येषां मते अयान्. एवकार उत्तरार्थः — the एव is spent at 3.4.115.'),
    ),
    "3.4.112": (
        _c('adviṣuḥ — they hated',
           {'of': 'jhi', 'lakara': 'laṅ', 'root': 'dviṣ'},
           note='द्विषश्च. अन्येषां मते अद्विषन् — the named teacher carried into a second rule.'),
    ),
    "3.4.114": (
        _c('lavitā — a cutter, an affix that is neither तिङ् nor शित्',
           {},
           note='आर्धधातुकं शेषः. The remainder of 3.4.113, so the code asks that rule and takes the name it did not give.'),
    ),
    "3.4.115": (
        _c('pecitha — you cooked, a perfect ending',
           {'tin': True, 'lakara': 'liṭ'},
           note='लिट् च, सार्वधातुकसंज्ञाया अपवादः. इह त्वेवकारोऽनुवर्तते, स नियमं करिष्यति — the एव comes from 3.4.111.'),
    ),
    "3.4.116": (
        _c('laviṣīṣṭa — may he cut',
           {'tin': True, 'lakara': 'liṅ', 'sense': 'āśis'},
           note='लिङाशिषि. आशिषीति किम्? लुनीयात्, पुनीयात् keep the other name.'),
    ),
    "3.4.117": (
        _c('upa stheyāma — may we stand near, taking both names',
           {'tin': True, 'chandasi': True},
           note='छन्दसि उभयथा. सार्वधातुकत्वाल् लिङः सलोपः, आर्धधातुकत्वादेत्वम् — one operation from each name.'),
    ),
    "4.1.1": (
        _c('kumārī — the base every affix of two chapters attaches to',
           {'ngi': True},
           note='ङ्याप्प्रातिपदिकात्, अधिकारोऽयम्. आ पञ्चमाध्यायपरिसमाप्तेः — it governs to the end of अध्याय ५.'),
    ),
    "4.1.2": (
        _c('su — the first of the twenty-one case-endings',
           {},
           note='स्वौजसमौट्छष्टाभ्याम्भिस् ... सुप्. औटष्टकारः सुडिति प्रत्याहारग्रहणार्थः, पकारः सुबिति प्रत्याहारार्थः.'),
    ),
    "4.1.3": (
        _c('ajā — the heading the feminine affixes stand under',
           {},
           note='स्त्रियाम्, अधिकारोऽयम्. प्रातिपदिकमात्रमत्र प्रकरणे संबध्यते, ङ्यापोरनेनैव विधानात्.'),
    ),
    "4.1.4": (
        _c('khaṭvā — a couch, from a stem in short अ',
           {'stem_final': 'a'},
           note='अजाद्यतष्टाप्. तपरकरणं तत्कालार्थम् — the त holds it to the short vowel.'),
    ),
    "4.1.5": (
        _c('kartrī — a doer, from a stem in ऋ',
           {'stem_final': 'ṛ'},
           note='ऋन्नेभ्यो ङीप्. ङकारः सामान्यग्रहणार्थः.'),
    ),
    "4.1.6": (
        _c('bhavatī — from a stem whose affix was उगित्',
           {'marked': 'ugit'},
           note='उगितश्च. उग् इद् यत्र संभवति यथाकथंचित् तदुगिच्छब्दरूपम्.'),
    ),
    "4.1.7": (
        _c('dhīvarī — with र replacing the final of वन्',
           {'stem_final': 'van'},
           note='वनो र च. ऋन्नेभ्यः इत्येव ङीपि सिद्धे तत्सन्नियोगेन रेफविधानार्थं वचनम्.'),
    ),
    "4.1.8": (
        _c('dvipadī — two-footed, optionally',
           {'stem_final': 'pāda'},
           note='पादोऽन्यतरस्याम्. पाद इति कृतसमासान्तः पादशब्दो निर्दिश्यते.'),
    ),
    "4.1.9": (
        _c('dvipadā ṛk — a verse of two feet',
           {'stem_final': 'pāda', 'sense': 'ṛc'},
           note='टाब् ऋचि, ङीपोऽपवादः. ऋचीत्यभिधेयनिर्देशः.'),
    ),
    "4.1.10": (
        _c('pañca brāhmaṇyaḥ — five brahmin women, and no affix',
           {'samjna': 'ṣaṭ'},
           note='न षट्स्वस्रादिभ्यः. यो यतः प्राप्नोति स सर्वः प्रतिषिध्यते.'),
    ),
    "4.1.11": (
        _c('dāmā — a garland, refused the affix a न्-stem would take',
           {'stem_final': 'man', 'wants': 'ṅīp'},
           note='मनः. And by परि० १६ also सीमा and अतिमहिमा, where the मन् carries no meaning of its own.'),
    ),
    "4.1.12": (
        _c('suparvā — having good joints',
           {'stem_final': 'an', 'compound': 'bahuvrīhi',
            'wants': 'ṅīp'},
           note='अनो बहुव्रीहेः. अनुपधालोपी बहुव्रीहिरिहोदाहरणम्.'),
    ),
    "4.1.13": (
        _c('pāme — from both the stems the last two rules refused',
           {'stem_final': 'man', 'wants': 'ḍāp'},
           note='डाब् उभाभ्यामन्यतरस्याम्. अन्यतरस्यांग्रहणं किमर्थम्? बहुव्रीहौ वनो र च इत्यस्यापि विकल्पो यथा स्यात्.'),
    ),
    "4.1.14": (
        _c('bahukukkuṭā — a subordinate member takes nothing',
           {'upasarjana': True},
           note='अनुपसर्जनात्, अधिकारोऽयम्. अस्त्यत्र प्रकरणे तदन्तविधिरिति, तथा च प्रधानेन तदन्तविधिर्भवति.'),
    ),
    "4.1.15": (
        _c('kurucarī — from a stem whose affix was टित्',
           {'marked': 'ṭit'},
           note='टिड्ढाणञ् ... ख्युनाम्, टापोऽपवादः. इह कस्माद् न भवति पचमाना? द्व्यनुबन्धकत्वाल् लटः.'),
    ),
    "4.1.16": (
        _c('gārgī — a daughter of Garga',
           {'marked': 'yañ'},
           note='यञश्च. आपत्यग्रहणं कर्तव्यम्. योगविभाग उत्तरार्थः.'),
    ),
    "4.1.17": (
        _c("gārgyāyaṇī — in the eastern teachers' view",
           {'marked': 'yañ', 'wants': 'ṣpha'},
           note='प्राचां ष्फ तद्धितः. षकारो ङीषर्थः, तद्धितग्रहणं प्रातिपदिकसंज्ञार्थम्.'),
    ),
    "4.1.18": (
        _c('lauhityāyanī — where the option closes',
           {'gana': 'lohitādi'},
           note='सर्वत्र लोहितादिकतन्तेभ्यः. सर्वत्रग्रहणम् उत्तरसूत्रादिहापकृष्यते, बाधकबाधनार्थम्.'),
    ),
    "4.1.19": (
        _c('kauravyāyaṇī — of the Kurus',
           {'stem': 'kauravya'},
           note='कौरव्यमाण्डूकाभ्यां च, यथाक्रमं टाब्ङीपोरपवादः.'),
    ),
    "4.1.20": (
        _c('kumārī — a girl, from a stem denoting the first age',
           {'sense': 'vayas-prathama'},
           note='वयसि प्रथमे. कालकृतशरीरावस्था यौवनादिर्वयः. वयस्यचरम इति वक्तव्यम्.'),
    ),
    "4.1.21": (
        _c('pañcapūlī — five bundles',
           {'compound': 'dvigu'},
           note='द्विगोः. कथं त्रिफला? अजादिषु दृश्यते.'),
    ),
    "4.1.22": (
        _c('pañcāśvā — bought with five horses, and no affix',
           {'compound': 'dvigu', 'samjna': 'taddhita-luk'},
           note='अपरिमाणबिस्ताचितकम्बल्येभ्यो न तद्धितलुकि. कालः संख्या च न परिमाणम्.'),
    ),
    "4.1.23": (
        _c('dvikāṇḍā kṣetrabhaktiḥ — a field of two measures',
           {'compound': 'dvigu', 'stem_final': 'kāṇḍa',
            'samjna': 'taddhita-luk', 'sense': 'kṣetra'},
           note='काण्डान्तात्क्षेत्रे. पूर्वेणैव प्रतिषेधे सिद्धे क्षेत्रे नियमार्थं वचनम्.'),
    ),
    "4.1.24": (
        _c('dvipuruṣā — two men deep, where the refusal is optional',
           {'compound': 'dvigu', 'stem_final': 'puruṣa',
            'samjna': 'taddhita-luk', 'sense': 'pramāṇa'},
           note='पुरुषात्प्रमाणेऽन्यतरस्याम्. नित्ये प्रतिषेधे प्राप्ते विकल्पार्थं वचनम्.'),
    ),
    "4.1.25": (
        _c('ghaṭodhnī — pot-uddered',
           {'stem_final': 'ūdhas', 'compound': 'bahuvrīhi'},
           note='बहुव्रीहेरूधसो ङीष्. समासान्तश्च स्त्रियामेव.'),
    ),
    "4.1.26": (
        _c('dvyūdhnī — two-uddered, differing only in accent',
           {'stem_final': 'ūdhas', 'compound': 'bahuvrīhi', 'samjna': 'saṃkhyā-avyaya-ādi'},
           note='संख्याव्ययादेर्ङीप्. पूर्वेण ङीषि प्राप्ते ङीब् विधीयते. आदिग्रहणं किम्? द्विविधोध्नी.'),
    ),
    "4.1.27": (
        _c('dvidāmnī — two-garlanded',
           {'stem_final': 'dāman', 'samjna': 'saṃkhyā-ādi'},
           note='दामहायनान्ताच्च. संख्याग्रहणमनुवर्तते, नाव्ययग्रहणम्.'),
    ),
    "4.1.28": (
        _c('bahurājñī — having many kings',
           {'stem_final': 'an', 'compound': 'bahuvrīhi', 'samjna': 'upadhālopin'},
           note='अन उपधालोपिनोऽन्यतरस्याम्. अनुपधालोपिनो ङीप्प्रतिषेधार्थं वचनम्.'),
    ),
    "4.1.29": (
        _c('atirājñī — a village so named, where the option closes',
           {'stem_final': 'an', 'compound': 'bahuvrīhi', 'samjna': 'upadhālopin', 'sense': 'saṃjñā'},
           note='नित्यं संज्ञाछन्दसोः, विकल्पस्यापवादः.'),
    ),
    "4.1.30": (
        _c('kevalī — one of nine words, each cited to a Vedic text',
           {'gana': 'kevalādi', 'sense': 'saṃjñā'},
           note='केवलमामक ... भेषजाच्च. केवली (पै०सं० १६.२०.१), and केवलेति भाषायाम् beside it.'),
    ),
    "4.1.31": (
        _c('rātrī — night, everywhere but before one ending',
           {'stem': 'rātri', 'sense': 'saṃjñā'},
           note='रात्रेश्चाजसौ. कथं रात्र्यः? ङीषयं बह्वादिलक्षणः — a different affix by a different rule.'),
    ),
    "4.1.32": (
        _c('antarvatnī — with child',
           {'stem': 'antarvat'},
           note='अन्तर्वत्पतिवतोर्नुक्. अन्तर्वदिति मतुब् निपात्यते, वत्वं सिद्धम्; पतिवदिति वत्वं निपात्यते, मतुप् सिद्धः.'),
    ),
    "4.1.33": (
        _c('patnī — a wife, where a sacrifice is in question',
           {'stem': 'pati', 'sense': 'yajña-saṃyoga'},
           note='पत्युर्नो यज्ञसंयोगे. तत्साधनत्वात् फलग्रहीतृत्वाद् वा यजमानस्य पत्नी.'),
    ),
    "4.1.34": (
        _c('vṛddhapatnī — an option where the last rule gave nothing',
           {'stem_final': 'pati'},
           note='विभाषा सपूर्वस्य. अप्राप्तविभाषेयम् अयज्ञसंयोगत्वात्.'),
    ),
    "4.1.35": (
        _c('sapatnī — a co-wife',
           {'gana': 'sapatnyādi'},
           note='नित्यं सपत्न्यादिषु. नित्यग्रहणं विस्पष्टार्थम्. समानादिष्विति वक्तव्ये समानस्य सभावार्थं वचनम्.'),
    ),
    "4.1.36": (
        _c('pūtakratāyī — with ऐ replacing the final',
           {'stem': 'pūtakratu', 'sense': 'puṃyoga'},
           note='पूतक्रतोरै च. त्रय एते योगाः पुंयोगप्रकरणे द्रष्टव्याः.'),
    ),
    "4.1.37": (
        _c('vṛṣākapāyī — and the substitute accented',
           {'stem': 'vṛṣākapi', 'sense': 'puṃyoga'},
           note='वृषाकप्यग्निकुसितकुसीदानामुदात्तः. वृषाकपिशब्दो मध्योदात्त उदात्तत्वं प्रयोजयति; अग्न्यादिषु स्थानिवद्भावादेव सिद्धम्.'),
    ),
    "4.1.38": (
        _c('manāvī — one of three forms from one option',
           {'stem': 'manu', 'sense': 'puṃyoga'},
           note='मनोरौ वा. वाग्रहणेन द्वावपि विकल्प्येते, तेन त्रैरूप्यं भवति.'),
    ),
    "4.1.39": (
        _c('enī — a spotted mare, with the त become न',
           {'sense': 'varṇa', 'accent': 'anudāttānta', 'upadha': 't'},
           note='वर्णादनुदात्तात्तोपधात्तो नः. वर्णादिति किम्? प्रकृता. अनुदात्तादिति किम्? श्वेता.'),
    ),
    "4.1.40": (
        _c('sāraṅgī — dappled, and only the accent differs',
           {'sense': 'varṇa', 'accent': 'anudāttānta'},
           note='अन्यतो ङीष्, वेति निवृत्तम्. स्वरे विशेषः — the two affixes give the same ई.'),
    ),
    "4.1.41": (
        _c('nartakī — a dancer, from a षित् affix',
           {'marked': 'ṣit'},
           note='षिद्गौरादिभ्यश्च. षित्त्वादेव सिद्धे ज्ञापनार्थं वचनम् — अनित्यः षिल्लक्षणो ङीषिति.'),
    ),
    "4.1.42": (
        _c('kuṇḍī — a bowl, one of eleven words paired with eleven senses',
           {'stem': 'kuṇḍa', 'sense': 'amatra'},
           note='जानपदकुण्ड ... केशवेषेषु, यथासंख्यम्. कुण्डी भवति, अमत्रं चेत्; कुण्डान्या otherwise.'),
    ),
    "4.1.43": (
        _c("śoṇī — a red mare, in the eastern teachers' view",
           {'stem': 'śoṇa'},
           note='शोणात्प्राचाम्. शोणी, शोणा वडवा.'),
    ),
    "4.1.44": (
        _c('paṭvī — clever, from a quality-word in उ',
           {'stem_final': 'u', 'sense': 'guṇavacana'},
           note='वोतो गुणवचनात्. सत्त्वे निविशतेऽपैति पृथग् जातिषु दृश्यते — the condition defined in verse.'),
    ),
    "4.1.45": (
        _c('bahvī — much',
           {'gana': 'bahvādi'},
           note='बह्वादिभ्यश्च. बहुशब्दो गुणवचन एव, तस्येह पाठ उत्तरार्थः.'),
    ),
    "4.1.46": (
        _c('bahvīṣu — among many, in the Veda',
           {'gana': 'bahvādi', 'chandasi': True},
           note='नित्यं छन्दसि. नित्यग्रहणमुत्तरार्थम्.'),
    ),
    "4.1.47": (
        _c('vibhvī — far-reaching, in the Veda',
           {'stem': 'bhū', 'chandasi': True},
           note='भुवश्च. इह कस्माद् न भवति स्वयम्भूः? उत इति तपरकरणमनुवर्तते.'),
    ),
    "4.1.48": (
        _c("gaṇakī — an astrologer's wife",
           {'sense': 'puṃyoga'},
           note='पुंयोगादाख्यायाम्. आख्याग्रहणं किम्? परिसृष्टा, प्रजाता — न तु पुमांसमाचक्षते.'),
    ),
    "4.1.49": (
        _c("indrāṇī — Indra's consort, with the augment आनुक्",
           {'gana': 'indrādi'},
           note='इन्द्रवरुण ... आचार्याणामानुक्. येषामत्र पुंयोग एवेष्यते, तेषामानुगागममात्रं विधीयते.'),
    ),
    "4.1.50": (
        _c('vastrakrītī — bought with a cloth',
           {'stem_final': 'krīta', 'pre': 'karaṇa'},
           note='क्रीतात्करणपूर्वात्. करणपूर्वादिति किम्? सुक्रीता.'),
    ),
    "4.1.51": (
        _c('sūpaviliptī pātrī — a dish with a little sauce',
           {'stem_final': 'kta', 'pre': 'karaṇa', 'sense': 'alpākhyā'},
           note='क्तादल्पाख्यायाम्. अल्पाख्यायामिति समुदायोपाधिः.'),
    ),
    "4.1.52": (
        _c('śaṅkhabhinnī — with a broken temple-bone',
           {'stem_final': 'kta', 'compound': 'bahuvrīhi', 'accent': 'antodātta'},
           note='बहुव्रीहेश्चान्तोदात्तात्. बहुव्रीहेरिति किम्? पादपतिता.'),
    ),
    "4.1.53": (
        _c('śārṅgajagdhī — where the first member is no body part',
           {'stem_final': 'kta', 'compound': 'bahuvrīhi', 'accent': 'antodātta', 'pre': 'asvāṅga'},
           note='अस्वाङ्गपूर्वपदाद्वा. पूर्वेण नित्ये प्राप्ते विकल्प उच्यते.'),
    ),
    "4.1.54": (
        _c('candramukhī — moon-faced',
           {'samjna': 'svāṅga'},
           note='स्वाङ्गाच्चोपसर्जनादसंयोगोपधात्. अद्रवं मूर्तिमत् स्वाङ्गं प्राणिस्थमविकारजम् — defined in verse.'),
    ),
    "4.1.55": (
        _c('bimboṣṭhī — with lips like a gourd',
           {'gana': 'nāsikādi'},
           note='नासिकोदरौष्ठजङ्घादन्तकर्णशृङ्गाच्च. बह्वज्लक्षणे संयोगोपधलक्षणे च प्रतिषेधे प्राप्ते वचनम्.'),
    ),
    "4.1.56": (
        _c('kalyāṇakroḍā — from an आकृतिगण, and no affix',
           {'gana': 'kroḍādi', 'samjna': 'svāṅga'},
           note='न क्रोडादिबह्वचः. क्रोडादिराकृतिगणः — an open list, recognised by shape rather than enumerated.'),
    ),
    "4.1.57": (
        _c('sakeśā — with hair, and no affix',
           {'pre': 'saha-nañ-vidyamāna', 'samjna': 'svāṅga'},
           note="सहनञ्विद्यमानपूर्वाच्च. It refuses both 4.1.54 and 4.1.55, and 4.1.55's vṛtti says so."),
    ),
    "4.1.58": (
        _c('śūrpaṇakhā — a name, and no affix',
           {'stem_final': 'nakha', 'samjna': 'svāṅga', 'sense': 'saṃjñā'},
           note='नखमुखात्संज्ञायाम्. संज्ञायामिति किम्? ताम्रनखी कन्या.'),
    ),
    "4.1.59": (
        _c('dīrghajihvī — long-tongued, in the Veda',
           {'stem': 'dīrghajihva', 'chandasi': True},
           note='दीर्घजिह्वी च छन्दसि. संयोगोपधत्वादप्राप्तो ङीष् विधीयते.'),
    ),
    "4.1.60": (
        _c('prāṅmukhī — facing east',
           {'pre': 'dik'},
           note='दिक्पूर्वपदान्ङीप्. यत्र ङीष् विहितस्तत्र तदपवादः — इह न भवति प्राग्गुल्फा.'),
    ),
    "4.1.61": (
        _c('dityauhī — a two-year-old heifer',
           {'stem_final': 'vāh'},
           note='वाहः. ङीषेव स्वर्यते, न ङीप् — the accent of the sūtra shows which affix is meant.'),
    ),
    "4.1.62": (
        _c('sakhī — a friend, in ordinary speech only',
           {'stem': 'sakhi', 'sense': 'bhāṣā'},
           note='सख्यशिश्वी इति भाषायाम्. भाषायामिति किम्? सखा सप्तपदी भव.'),
    ),
    "4.1.63": (
        _c('kukkuṭī — a hen, from a class-word',
           {'sense': 'jāti', 'samjna': 'astrīviṣaya'},
           note='जातेरस्त्रीविषयादयोपधात्. आकृतिग्रहणा जातिर्लिङ्गानां च न सर्वभाक् — defined in verse.'),
    ),
    "4.1.64": (
        _c('śālaparṇī — a plant',
           {'gana': 'pākādi', 'sense': 'jāti'},
           note='पाककर्णपर्णपुष्पफलमूलवालोत्तरपदाच्च. स्त्रीविषयत्वादेतेषां पूर्वेणाप्राप्तः प्रत्ययो विधीयते.'),
    ),
    "4.1.65": (
        _c('avantī — a woman of Avanti',
           {'stem_final': 'i', 'sense': 'manuṣya-jāti'},
           note='इतो मनुष्यजातेः. जातेरिति वर्तमाने पुनर्जातिग्रहणं योपधादपि यथा स्यात्.'),
    ),
    "4.1.66": (
        _c('kurūḥ — a Kuru woman',
           {'stem_final': 'u', 'sense': 'manuṣya-jāti'},
           note='ऊङुतः. ङकारो नोङ्धात्वोः इति विशेषणार्थः, दीर्घोच्चारणं कपो बाधनार्थम्.'),
    ),
    "4.1.67": (
        _c('bhadrabāhūḥ — a name',
           {'stem_final': 'bāhu', 'sense': 'saṃjñā'},
           note='बाह्वन्तात्संज्ञायाम्. संज्ञायामिति किम्? वृत्तबाहुः.'),
    ),
    "4.1.68": (
        _c('paṅgūḥ — lame',
           {'stem': 'paṅgu'},
           note='पङ्गोश्च. श्वशुरस्योकाराकारयोर्लोपश्च वक्तव्यः — श्वश्रूः.'),
    ),
    "4.1.69": (
        _c("karabhorūḥ — with thighs like an elephant's trunk",
           {'stem_final': 'ūru', 'sense': 'aupamye'},
           note='ऊरूत्तरपदादौपम्ये. औपम्य इति किम्? वृत्तोरुः स्त्री.'),
    ),
    "4.1.70": (
        _c('vāmorūḥ — fair-thighed, with no comparison meant',
           {'stem_final': 'ūru', 'gana': 'saṃhitādi'},
           note='संहितशफलक्षणवामादेश्च. अनौपम्यार्थ आरम्भः.'),
    ),
    "4.1.71": (
        _c('kadrūḥ — in the Veda',
           {'stem': 'kadru', 'chandasi': True},
           note='कद्रुकमण्डल्वोश्छन्दसि. छन्दसीति किम्? कद्रुः, कमण्डलुः.'),
    ),
    "4.1.72": (
        _c('kadrūḥ — and outside it, as a name',
           {'stem': 'kadru', 'sense': 'saṃjñā'},
           note='संज्ञायाम्, अच्छन्दोऽर्थं वचनम्.'),
    ),
    "4.1.73": (
        _c('śārṅgaravī — the seventh of the eight affixes',
           {'gana': 'śārṅgaravādi'},
           note='शार्ङ्गरवाद्यञो ङीन्. जातिग्रहणं चेहानुवर्तते, तेन जातिलक्षणो ङीषनेन बाध्यते, न पुंयोगलक्षणः.'),
    ),
    "4.1.74": (
        _c('kausalyā — the eighth and last',
           {'marked': 'yaṅ'},
           note='यङश्चाप्. ञ्यङः ष्यङश्च सामान्यग्रहणमेतत्.'),
    ),
    "4.1.75": (
        _c('āvaṭyā — and beaten in turn by 4.1.17',
           {'stem': 'āvaṭya'},
           note='आवट्याच्च. प्राचां ष्फ एव, सर्वत्रग्रहणात् — आवट्यायनी.'),
    ),
    "4.1.76": (
        _c('yuvatiḥ — the name every affix of two chapters bears',
           {},
           note='तद्धिताः, अधिकारोऽयम्. बहुवचनमनुक्ततद्धितपरिग्रहार्थम् — the plural read as a scope.'),
    ),
    "4.1.77": (
        _c('yuvatiḥ — a young woman',
           {'stem': 'yuvan'},
           note='यूनस्तिः, ङीपोऽपवादः. स च तद्धितसंज्ञो भवति.'),
    ),
    "4.1.78": (
        _c('kārīṣagandhyā — with a heavy next-to-last syllable',
           {'marked': 'aṇ', 'sense': 'gotra', 'samjna': 'guru-upottama'},
           note='अणिञोरनार्षयोर्गुरूपोत्तमयोः ष्यङ् गोत्रे. निर्दिश्यमानस्यादेशा भवन्ति इत्यणिञोरेव विज्ञायते.'),
    ),
    "4.1.79": (
        _c('pauṇikyā — a family name taken as part of a lineage',
           {'samjna': 'gotra-avayava', 'sense': 'gotra'},
           note='गोत्रावयवात्. अगुरूपोत्तमार्थ आरम्भः.'),
    ),
    "4.1.80": (
        _c('krauḍyā — from a list lifting both conditions',
           {'gana': 'krauḍyādi'},
           note='क्रौड्यादिभ्यश्च. अगुरूपोत्तमार्थ आरम्भः, अनणिञर्थश्च.'),
    ),
    "4.1.81": (
        _c('daivayajñyā — one option doing two different things',
           {'gana': 'daivayajñyādi'},
           note='दैवयज्ञि ... काण्ठेविद्धिभ्योऽन्यतरस्याम्. गोत्रग्रहणं च नानुवर्तते, तेनोभयत्रविभाषेयम्.'),
    ),
    "4.1.82": (
        _c('aupagavaḥ — from the first of the connected words',
           {'position': 1, 'connected': True},
           note='समर्थानां प्रथमाद्वा. त्रयमप्यधिक्रियते समर्थानामिति च, प्रथमादिति च, वेति च.'),
    ),
    "4.1.83": (
        _c('aupagavaḥ — the affix where no rule says otherwise',
           {},
           note='प्राग्दीव्यतोऽण्. अधिकारः, परिभाषा, विधिर्वेति त्रिष्वपि दर्शनेष्वपवादविषयं परिहृत्याण् प्रवर्तते.'),
    ),
    "4.1.84": (
        _c('āśvapatam — the default given again, against a later rule',
           {'of': 'aśvapatyādi'},
           note='अश्वपत्यादिभ्यश्च. पत्युत्तरपदाद् ण्यं वक्ष्यति, तस्यापवादः.'),
    ),
    "4.1.85": (
        _c('daityaḥ — a son of Diti',
           {'of': 'dity-adity-āditya-paty-uttarapada'},
           note='दित्यदित्यादित्यपत्युत्तरपदाण्ण्यः. ण्यादयोऽर्थविशेषलक्षणादणपवादात् पूर्वविप्रतिषेधेन.'),
    ),
    "4.1.86": (
        _c('autsaḥ — beating the default and its exceptions',
           {'of': 'utsādi'},
           note='उत्सादिभ्योऽञ्, अणस्तदपवादानां च बाधकः. छन्दश्चेह वृत्तं गृह्यते न वेदः.'),
    ),
    "4.1.87": (
        _c('straiṇam — one affix serving four senses',
           {'of': 'strī'},
           note='स्त्रीपुंसाभ्यां नञ्स्नञौ भवनात्, यथाक्रमम्. स्त्रीषु भवं, स्त्रीणां समूहः, स्त्रीभ्य आगतं, स्त्रीभ्यो हितं — all स्त्रैणम्.'),
    ),
    "4.1.88": (
        _c('pañcakapālaḥ — prepared in five bowls, the affix elided',
           {},
           note='द्विगोर्लुगनपत्ये. उपचारेण तु लक्षणया द्विगुनिमित्तभूतः प्रत्यय एव द्विगुः, तस्य लुग् भवति.'),
    ),
    "4.1.89": (
        _c('gārgīyāḥ — the elision refused before a vowel',
           {'gotra': True, 'before_ac': True},
           note='गोत्रेऽलुगचि. अचीति किम्? गर्गरूप्यम्, गर्गमयम्.'),
    ),
    "4.1.90": (
        _c('phāṇṭāhṛtaḥ — the affix dropped before it is formed',
           {'yuvan': True, 'before_ac': True},
           note='यूनि लुक्. बुद्धिस्थेऽनुत्पन्न एव युवप्रत्ययस्य लुग् भवति, तस्मिन्निवृत्ते सति यो यतः प्राप्नोति स ततो भवति.'),
    ),
    "4.1.91": (
        _c('gārgīyāḥ — and optionally, so both forms stand',
           {'yuvan': True, 'before_ac': True, 'of': 'phak'},
           note='फक्फिञोरन्यतरस्याम्. पूर्वसूत्रेण नित्ये लुकि प्राप्ते विकल्प उच्यते.'),
    ),
    "4.1.92": (
        _c('aupagavaḥ — the sense that governs the whole run',
           {},
           note='तस्यापत्यम्, अर्थनिर्देशोऽयम्. पूर्वैरुत्तरैश्च प्रत्ययैरभिसंबध्यते — it faces both ways.'),
    ),
    "4.1.93": (
        _c('gārgyaḥ — one affix for a whole lineage',
           {},
           note='एको गोत्रे. योऽपि व्यवहितेन जनितः, सोऽपि प्रथमप्रकृतेरपत्यं भवत्येव.'),
    ),
    "4.1.94": (
        _c('gārgyāyaṇaḥ — added to the lineage-form, not the base',
           {'kind': 'yuvan'},
           note='गोत्राद् यून्यस्त्रियाम्. तस्माद् योगविभागः कर्तव्यः — the rule split because neither whole reading works.'),
    ),
    "4.1.95": (
        _c('dākṣiḥ — from a stem in short अ',
           {'stem_final': 'a'},
           note='अत इञ्, अणोऽपवादः. तपरकरणं किम्? शुभंयाः, कीलालपा इत्यतो मा भूत्.'),
    ),
    "4.1.96": (
        _c('bāhaviḥ — from an open list',
           {'gana': 'bāhvādi'},
           note='बाह्वादिभ्यश्च. चकारोऽनुक्तसमुच्चयार्थ आकृतिगणतामस्य बोधयति.'),
    ),
    "4.1.97": (
        _c('saudhātakiḥ — the affix and a substitution in one act',
           {'stem': 'sudhātṛ'},
           note='सुधातुरकङ् च, तत्सन्नियोगेन.'),
    ),
    "4.1.98": (
        _c('kauñjāyanyaḥ — and the accent changes with the number',
           {'gana': 'kuñjādi', 'kind': 'gotra'},
           note='कुञ्जादिभ्यश्च्फञ्, इञोऽपवादः. एकवचनद्विवचनयोः ञित्स्वरेणैव, बहुवचने तु चित्स्वर एवेष्यते.'),
    ),
    "4.1.99": (
        _c('nāḍāyanaḥ — and one member is in two lists',
           {'gana': 'naḍādi', 'kind': 'gotra'},
           note='नडादिभ्यः फक्. अथवा पैलादिपाठ एव ज्ञापक इञो भावस्य.'),
    ),
    "4.1.100": (
        _c('hāritāyanaḥ — the heading overridden by capacity',
           {'gana': 'haritādi', 'marked': 'añ', 'kind': 'yuvan'},
           note='हरितादिभ्योऽञः. इह तु गोत्राधिकारेऽपि सामर्थ्याद् यूनि प्रत्ययो विज्ञायते.'),
    ),
    "4.1.101": (
        _c('gārgyāyaṇaḥ — after a यञ्-final stem',
           {'marked': 'yañ', 'kind': 'yuvan'},
           note='यञिञोश्च. गोत्रग्रहणेन यञिञौ विशेष्येते, तदन्तात् तु यून्येवायं प्रत्ययः.'),
    ),
    "4.1.102": (
        _c('śāradvatāyanaḥ — only if a Bhārgava is meant',
           {'stem': 'śaradvat', 'among': 'bhārgava', 'kind': 'gotra'},
           note='शरद्वच्छुनकदर्भाद् भृगुवत्साग्रायणेषु, यथासंख्यम्. शारद्वतोऽन्यः.'),
    ),
    "4.1.103": (
        _c('drauṇāyanaḥ — optionally',
           {'gana': 'droṇādi', 'kind': 'gotra'},
           note='द्रोणपर्वतजीवन्तादन्यतरस्याम्, इञोऽपवादः. इदानीन्तनात् तु श्रुतिसामान्यादध्यारोपेण तथाभिधानं भवति.'),
    ),
    "4.1.104": (
        _c('baidaḥ — the immediate descendant of a non-sage',
           {'gana': 'bidādi', 'kind': 'gotra'},
           note='अनृष्यानन्तर्ये बिदादिभ्योऽञ्. ऋष्यपत्यनैरन्तर्यविषये प्रतिषेधे विज्ञायमाने कौशिको विश्वामित्र इति दुष्यति.'),
    ),
    "4.1.105": (
        _c('gārgyaḥ — from the largest list of the run',
           {'gana': 'gargādi', 'kind': 'gotra'},
           note='गर्गादिभ्यो यञ्. कथमनन्तरो रामो जामदग्न्यः? गोत्ररूपाध्यारोपेण भविष्यति.'),
    ),
    "4.1.106": (
        _c('mādhavyaḥ — only if a brahmin is meant',
           {'stem': 'madhu', 'among': 'brāhmaṇa', 'kind': 'gotra'},
           note='मधुबभ्र्वोर्ब्राह्मणकौशिकयोः. ततः सिद्धे यञि कौशिके नियमार्थं वचनम्.'),
    ),
    "4.1.107": (
        _c('kāpyaḥ — in the Āṅgirasa line',
           {'stem': 'kapi', 'among': 'āṅgirasa', 'kind': 'gotra'},
           note='कपिबोधादाङ्गिरसे. आङ्गिरस इति किम्? कापेयः, बौधिः.'),
    ),
    "4.1.108": (
        _c('vātaṇḍyaḥ — and outside that line, both forms stand',
           {'stem': 'vataṇḍa', 'among': 'āṅgirasa', 'kind': 'gotra'},
           note='वतण्डाच्च. अनाङ्गिरसे तूभयत्र पाठसामर्थ्यात् प्रत्ययद्वयमपि भवति.'),
    ),
    "4.1.109": (
        _c('vataṇḍī — the affix gone, and another arriving',
           {'among': 'āṅgirasa'},
           note='लुक् स्त्रियाम्. लुकि कृते शार्ङ्गरवादिपाठाद् ङीन् भवति.'),
    ),
    "4.1.110": (
        _c('āśvāyanaḥ — and members already carrying an affix',
           {'gana': 'aśvādi', 'kind': 'gotra'},
           note='अश्वादिभ्यः फञ्. ये त्वत्र प्रत्ययान्ताः पठ्यन्ते, तेभ्यः सामर्थ्याद् यूनि प्रत्ययो विज्ञायते.'),
    ),
    "4.1.111": (
        _c('bhārgāyaṇaḥ — only if a Traigarta is meant',
           {'stem': 'bharga', 'among': 'traigarta', 'kind': 'gotra'},
           note='भर्गात्त्रैगर्ते. भार्गिरन्यः.'),
    ),
    "4.1.112": (
        _c('śaivaḥ — and here the lineage section ends',
           {'gana': 'śivādi'},
           note='शिवादिभ्योऽण्. गोत्र इति निवृत्तम्, अतः प्रभृति सामान्येन प्रत्यया विज्ञायन्ते. गङ्गाशब्दः पठ्यते ... समावेशार्थम्, तेन त्रैरूप्यं भवति.'),
    ),
    "4.1.113": (
        _c("yāmunaḥ — from a river's name",
           {'samjna': 'avṛddha-nadī-mānuṣī'},
           note='अवृद्धाभ्यो नदीमानुषीभ्यस्तन्नामिकाभ्यः. अवृद्धाभ्य इति शब्दधर्मः, नदीमानुषीभ्य इति अर्थधर्मः.'),
    ),
    "4.1.114": (
        _c("vāsiṣṭhaḥ — from a sage's name",
           {'gana': 'ṛṣyandhakavṛṣṇikuru'},
           note='ऋष्यन्धकवृष्णिकुरुभ्यश्च. कथं पुनर्नित्यानां शब्दानामन्धकादिवंशसमाश्रयणेनान्वाख्यानं युज्यते?'),
    ),
    "4.1.115": (
        _c('dvaimāturaḥ — of two mothers',
           {'stem': 'mātṛ', 'pre': 'saṃkhyā-sam-bhadra'},
           note='मातुरुत्संख्यासंभद्रपूर्वायाः. उकारादेशार्थं वचनम्, प्रत्ययः पुनरुत्सर्गेणैव सिद्धः.'),
    ),
    "4.1.116": (
        _c('kānīnaḥ — Karṇa, son of an unmarried mother',
           {'stem': 'kanyā'},
           note='कन्यायाः कनीन च, ढकोऽपवादः.'),
    ),
    "4.1.117": (
        _c('vaikarṇaḥ — only if a Vātsya is meant',
           {'stem': 'vikarṇa', 'among': 'vātsya'},
           note='विकर्णशुङ्गच्छगलाद् वत्सभरद्वाजात्रिषु. द्वयमपि चैतत् प्रमाणमुभयथा सूत्रप्रणयनात्.'),
    ),
    "4.1.118": (
        _c('pailaḥ — the earlier affix, optionally',
           {'stem': 'pīlā'},
           note='पीलाया वा. पैलः, पैलेयः.'),
    ),
    "4.1.119": (
        _c('māṇḍūkeyaḥ — one of three forms',
           {'stem': 'maṇḍūka'},
           note='ढक् च मण्डूकात्. चकारादण् च वा, तेन त्रैरूप्यं भवति.'),
    ),
    "4.1.120": (
        _c('sauparṇeyaḥ — from a stem ending in a feminine affix',
           {'stri_pratyaya': True},
           note='स्त्रीभ्यो ढक्. स्त्रीप्रत्ययविज्ञापनादसत्यर्थग्रहणे इह न भवति — ऐडबिडः, दारदः.'),
    ),
    "4.1.121": (
        _c('dātteyaḥ — and of exactly two vowels',
           {'stri_pratyaya': True, 'dvyac': True},
           note='द्व्यचः, तन्नामिकाणोऽपवादः. द्व्यच इति किम्? यामुनः.'),
    ),
    "4.1.122": (
        _c('ātreyaḥ — in इ, but not the इञ् of 4.1.95',
           {'stem_final': 'i', 'dvyac': True},
           note='इतश्चानिञः. अनिञ इति किम्? दाक्षायणः, प्लाक्षायणः.'),
    ),
    "4.1.123": (
        _c('śaubhreyaḥ — from the third open list of the pāda',
           {'gana': 'śubhrādi'},
           note='शुभ्रादिभ्यश्च. चकारोऽनुक्तसमुच्चयार्थ आकृतिगणतामस्य बोधयति — तेन गाङ्गेयः पाण्डवेय इति सिद्धम्.'),
    ),
    "4.1.124": (
        _c('vaikarṇeyaḥ — the same word in another family',
           {'stem': 'vikarṇa', 'among': 'kāśyapa'},
           note='विकर्णकुषीतकात् काश्यपे. काश्यप इति किम्? वैकर्णिः.'),
    ),
    "4.1.125": (
        _c('bhrauveyaḥ — the affix and an augment together',
           {'stem': 'bhrū'},
           note='भ्रुवो वुक् च, तत्सन्नियोगेन.'),
    ),
    "4.1.126": (
        _c('kālyāṇineyaḥ — a list serving two purposes at once',
           {'gana': 'kalyāṇyādi'},
           note='कल्याण्यादीनामिनङ्. स्त्रीप्रत्ययान्तानाम् आदेशार्थं ग्रहणम्, अन्येषामुभयार्थम्.'),
    ),
    "4.1.127": (
        _c('kaulaṭineyaḥ — and the sense decides the affix',
           {'stem': 'kulaṭā'},
           note='कुलटाया वा. या तु कुलान्यटन्ती शीलं भिनत्ति, ततः परत्वाड् ढ्रका भवितव्यम् — कौलटेरः.'),
    ),
    "4.1.128": (
        _c('cāṭakairaḥ — an affix found nowhere else',
           {'stem': 'caṭakā'},
           note='चटकाया ऐरक्. स्त्रियामपत्ये लुग् वक्तव्यः — चटकाया अपत्यं स्त्री चटका.'),
    ),
    "4.1.129": (
        _c('gaudheraḥ — and गौधेयः too, by another list',
           {'stem': 'godhā', 'wants': 'ḍhrak'},
           note='गोधाया ढ्रक्. शुभ्रादिष्वयं पठ्यते, तेन गौधेयोऽपि भवति.'),
    ),
    "4.1.130": (
        _c("gaudhāraḥ — in the northern teachers' view",
           {'stem': 'godhā', 'authority': 'udīcām'},
           note='आरगुदीचाम्. आचार्यग्रहणं पूजार्थम्. ज्ञापकं त्वयमन्येभ्योऽपि भवतीति — जाडारः, पाण्डारः.'),
    ),
    "4.1.131": (
        _c('kāṇeraḥ — from words for the maimed and disgraced',
           {'samjna': 'kṣudrā'},
           note='क्षुद्राभ्यो वा, ढकोऽपवादः. ढ्रगनुवर्तते, न आरक्.'),
    ),
    "4.1.132": (
        _c("paitṛṣvasrīyaḥ — from a father's sister",
           {'stem': 'pitṛṣvasṛ'},
           note='पितृष्वसुश्छण्, अणोऽपवादः.'),
    ),
    "4.1.133": (
        _c('paitṛṣvaseyaḥ — a rule that is its own evidence',
           {'stem': 'pitṛṣvasṛ', 'wants': 'ḍhak'},
           note='ढकि लोपः. कथं पुनरिह ढक् प्रत्ययः? एतदेव ज्ञापकं ढको भावस्य.'),
    ),
    "4.1.134": (
        _c("mātṛṣvasrīyaḥ — and the same for a mother's sister",
           {'stem': 'mātṛṣvasṛ'},
           note='मातुश्च. पितृष्वसुर्यदुक्तं तद् मातृष्वसुरपि भवति — an अतिदेश carrying two rules at once.'),
    ),
    "4.1.135": (
        _c('kāmaṇḍaleyaḥ — from words for four-footed things',
           {'samjna': 'catuṣpād'},
           note='चतुष्पाद्भ्यो ढञ्, अणादीनामपवादः.'),
    ),
    "4.1.136": (
        _c('gārṣṭeyaḥ — from a list, where the last rule cannot reach',
           {'gana': 'gṛṣṭyādi'},
           note='गृष्ट्यादिभ्यश्च. अचतुष्पादर्थं वचनम्.'),
    ),
    "4.1.137": (
        _c('rājanyaḥ — only where the kṣatriya class is meant',
           {'stem': 'rājan', 'samjna': 'jāti'},
           note='राजश्वशुरयोर्यत्. राज्ञोऽपत्ये जातिग्रहणम् — राजनोऽन्यः.'),
    ),
    "4.1.138": (
        _c('kṣatriyaḥ — a class-word, not a patronymic',
           {'stem': 'kṣatra', 'samjna': 'jāti'},
           note='क्षत्राद् घः. अयमपि जातिशब्द एव — क्षात्रिरन्यः.'),
    ),
    "4.1.139": (
        _c('kulīnaḥ — of good family',
           {'stem_final': 'kula'},
           note='कुलात् खः. उत्तरसूत्रे पूर्वपदप्रतिषेधाद् इह तदन्तः केवलश्च दृश्यते.'),
    ),
    "4.1.140": (
        _c('kulyaḥ — where no first member stands',
           {'stem_final': 'kula', 'pre': 'none'},
           note='अपूर्वपदाद् यत् ढकञौ बहुलम्. ताभ्यां मुक्ते खोऽपि भवति — कुलीनः.'),
    ),
    "4.1.141": (
        _c('māhākulaḥ — of a great family',
           {'stem': 'mahākula'},
           note='महाकुलाद् अञ्खञौ. पक्षे खः — महाकुलीनः.'),
    ),
    "4.1.142": (
        _c('dauṣkuleyaḥ — of a bad family',
           {'stem': 'duṣkula'},
           note='दुष्कुलाड् ढक्. अन्यतरस्यामित्यनुवृत्तेः खश्च.'),
    ),
    "4.1.143": (
        _c("svasrīyaḥ — a sister's son",
           {'stem': 'svasṛ'},
           note='स्वसुश्छः, अणोऽपवादः.'),
    ),
    "4.1.144": (
        _c("bhrātṛvyaḥ — a brother's son",
           {'stem': 'bhrātṛ'},
           note='भ्रातुर्व्यच्च. चकाराच्छश्च — भ्रात्रीयः.'),
    ),
    "4.1.145": (
        _c('bhrātṛvyaḥ — an enemy, and no descendant at all',
           {'stem': 'bhrātṛ', 'samjna': 'amitra'},
           note='व्यन् सपत्ने. अपत्यार्थोऽत्र नास्त्येव — समुदायेन चेदमित्रः सपत्न उच्यते.'),
    ),
    "4.1.146": (
        _c('raivatikaḥ — from a list',
           {'gana': 'revatyādi'},
           note='रेवत्यादिभ्यष्ठक्.'),
    ),
    "4.1.147": (
        _c('gārgo jālmaḥ — where contempt is meant',
           {'samjna': 'gotra-strī', 'attitude': 'kutsana'},
           note='गोत्रस्त्रियाः कुत्सने ण च. पितुरसंविज्ञाने मात्रा व्यपदेशोऽपत्यस्य कुत्सा.'),
    ),
    "4.1.148": (
        _c('bhāgavittikaḥ — variously, in one region',
           {'samjna': 'sauvīra-gotra', 'attitude': 'kutsana'},
           note='वृद्धाट् ठक् सौवीरेषु बहुलम्. बहुलग्रहणम् उपाधिवैचित्र्यार्थम्.'),
    ),
    "4.1.149": (
        _c('yāmundāyanīyaḥ — after one affix, in the same region',
           {'marked': 'phiñ', 'samjna': 'sauvīra-gotra', 'attitude': 'kutsana'},
           note='फेश्छ च. फेरिति फिञो ग्रहणं न फिनः, वृद्धाधिकारात्.'),
    ),
    "4.1.150": (
        _c('phāṇṭāhṛtaḥ — and NOT taken in order',
           {'stem': 'phāṇṭāhṛti', 'samjna': 'sauvīra'},
           note='फाण्टाहृतिमिमताभ्यां णफिञौ. अल्पाच्तरस्यापूर्वनिपातो लक्षणव्यभिचारचिह्नम्.'),
    ),
    "4.1.151": (
        _c('kauravyaḥ — from a list',
           {'gana': 'kurvādi'},
           note='कुर्वादिभ्यो ण्यः. कथं भाषायां वैन्यो राजेति? छान्दस एवायं प्रमादात् कविभिः प्रयुक्तः.'),
    ),
    "4.1.152": (
        _c('kāriṣeṇyaḥ — from a compound in *army*',
           {'stem_final': 'senā'},
           note='सेनान्तलक्षणकारिभ्यश्च.'),
    ),
    "4.1.153": (
        _c("kāriṣeṇiḥ — in the northern teachers' view",
           {'stem_final': 'senā', 'authority': 'udīcām'},
           note='उदीचामिञ्. आचार्यग्रहणं वैचित्र्यार्थम्.'),
    ),
    "4.1.154": (
        _c('taikāyaniḥ — from a long list',
           {'gana': 'tikādi'},
           note='तिकादिभ्यः फिञ्.'),
    ),
    "4.1.155": (
        _c('kausalyāyaniḥ — the affix wanted after the ultimate base',
           {'stem': 'kosala'},
           note='कौसल्यकार्मार्याभ्यां च. परमप्रकृतेरेवायं प्रत्यय इष्यते.'),
    ),
    "4.1.156": (
        _c('kārtrāyaṇiḥ — from a two-vowel stem in अण्',
           {'marked': 'aṇ', 'dvyac': True},
           note='अणो द्व्यचः, इञोऽपवादः.'),
    ),
    "4.1.157": (
        _c('āmraguptāyaṇiḥ — strengthened, and no lineage-name',
           {'samjna': 'vṛddha-agotra', 'authority': 'udīcām'},
           note='उदीचां वृद्धादगोत्रात्. अगोत्रादिति किम्? औपगविः.'),
    ),
    "4.1.158": (
        _c('vākinakāyaniḥ — the affix with an augment',
           {'gana': 'vākinādi'},
           note='वाकिनादीनां कुक् च. यदिह वृद्धमगोत्रं शब्दरूपं तस्यागमार्थमेव ग्रहणम्, अन्येषामुभयार्थम्.'),
    ),
    "4.1.159": (
        _c('gārgīputrakāyaṇiḥ — one of three forms',
           {'stem_final': 'putra', 'authority': 'udīcām'},
           note='पुत्रान्तादन्यतरस्याम्. तेन त्रैरूप्यं संपद्यते.'),
    ),
    "4.1.160": (
        _c("glucukāyaniḥ — in the eastern teachers' view",
           {'authority': 'prācām'},
           note='प्राचामवृद्धात् फिन् बहुलम्. सर्व एते विकल्पार्थास्तेषामेकेनैव सिध्यति.'),
    ),
    "4.1.161": (
        _c('mānuṣaḥ — a human being, and no descendant',
           {'stem': 'manu', 'samjna': 'jāti'},
           note='मनोर्जातावञ्यतौ षुक् च. अपत्यार्थोऽत्र नास्त्येव. तथा च मानुषा इति बहुषु न लुग् भवति.'),
    ),
    "4.1.162": (
        _c('gārgyaḥ — a descendant from the grandson onward',
           {},
           note='अपत्यं पौत्रप्रभृति गोत्रम्. संबन्धिशब्दत्वादपत्यशब्दस्य यस्य यदपत्यं तदपेक्षया पौत्रप्रभृतेर्गोत्रसंज्ञा विधीयते.'),
    ),
    "4.1.163": (
        _c('gārgyāyaṇaḥ — while an elder of the line lives',
           {'elder_alive': True},
           note='जीवति तु वंश्ये युवा. षष्ठ्या विपरिणम्यते — तेन चतुर्थादारभ्य युवसंज्ञा विधीयते.'),
    ),
    "4.1.164": (
        _c('gārgyāyaṇaḥ — and while an elder brother lives',
           {'elder_alive': True, 'elder': 'bhrātṛ'},
           note='भ्रातरि च ज्यायसि. भ्राता तु न वंश्यः, अकारणत्वात्.'),
    ),
    "4.1.165": (
        _c('gārgyāyaṇaḥ — or any older kinsman, optionally',
           {'elder_alive': True, 'elder': 'sapiṇḍa'},
           note='वान्यस्मिन् सपिण्डे स्थविरतरे जीवति. सप्तमपुरुषावधयः सपिण्डाः स्मर्यन्ते.'),
    ),
    "4.1.166": (
        _c('tatra bhavān gārgyāyaṇaḥ — of an elder, out of respect',
           {'attitude': 'pūjā'},
           note='वृद्धस्य च पूजायाम्. वृद्धस्येति षष्ठीनिर्देशो विचित्रा सूत्रस्य कृतिः.'),
    ),
    "4.1.167": (
        _c('gārgyo jālmaḥ — of a young man, out of contempt',
           {'attitude': 'kutsā'},
           note='यूनश्च कुत्सायाम्. निवृत्तिप्रधानो विकल्पः — प्रतिपक्षाभावात्.'),
    ),
    "4.1.168": (
        _c('pāñcālaḥ — from a country whose people are warriors',
           {'janapada': True},
           note='जनपदशब्दात् क्षत्रियादञ्. तस्य राजन्यपत्यवत् — पञ्चालानां राजा पाञ्चालः.'),
    ),
    "4.1.169": (
        _c('sālveyaḥ — holding off a rule two ahead',
           {'stem': 'sālveya', 'janapada': True},
           note='साल्वेयगान्धारिभ्यां च. ञ्यङि प्राप्ते पुनरञ् विधीयते.'),
    ),
    "4.1.170": (
        _c('āṅgaḥ — from a two-vowel country name',
           {'janapada': True, 'dvyac': True},
           note='द्व्यञ्मगधकलिङ्गसूरमसादण्, अञोऽपवादः.'),
    ),
    "4.1.171": (
        _c('āmbaṣṭhyaḥ — from a strengthened one',
           {'janapada': True, 'samjna': 'vṛddha'},
           note='वृद्धेत्कोसलाजादाञ् ञ्यङ्. तपरकरणं किम्? कौमारः.'),
    ),
    "4.1.172": (
        _c('kauravyaḥ — and this one vanishes in the plural',
           {'stem': 'kuru', 'janapada': True},
           note='कुरुनादिभ्यो ण्यः, अणञोरपवादः. तस्य बहुषु लुका भवितव्यम्.'),
    ),
    "4.1.173": (
        _c('audumbariḥ — from a district of one country',
           {'samjna': 'sālva-avayava', 'janapada': True},
           note='साल्वावयवप्रत्यग्रथकलकूटाश्मकादिञ्. तस्य निवासः साल्वो जनपदः, तदवयवा उदुम्बरादयः.'),
    ),
    "4.1.174": (
        _c('pāñcālaḥ — and the name those affixes bear',
           {},
           note='ते तद्राजाः. सर्वनाम्ना प्रत्यवमृश्यन्ते न तु पूर्वे, गोत्रयुवसंज्ञाकाण्डेन व्यवहितत्वात्.'),
    ),
    "4.1.175": (
        _c('kambojaḥ — the affix elided',
           {'stem': 'kamboja', 'janapada': True},
           note='कम्बोजाल्लुक्. कम्बोजादिभ्यो लुग्वचनं चोलाद्यर्थम्.'),
    ),
    "4.1.176": (
        _c('avantī — three names lose it in the feminine',
           {'feminine': True, 'of': 'avanti'},
           note='अवन्तिकुन्तिकुरुभ्यश्च. स्त्रियामिति किम्? आवन्त्यः.'),
    ),
    "4.1.177": (
        _c('śūrasenī — and so does any such affix in अ',
           {'feminine': True, 'affix': 'añ'},
           note='अतश्च. अवन्त्यादिभ्यो लुग्वचनात् तदन्तविधिरत्र नास्ति — आम्बष्ठ्या, सौवीर्या.'),
    ),
    "4.1.178": (
        _c('yaudheyī — but not for these, and the refusal proves a rule',
           {'feminine': True, 'gana': 'yaudheyādi'},
           note='न प्राच्यभर्गादियौधेयादिभ्यः. एतदेव विज्ञापयति पाञ्चमिकस्यापि तद्राजस्य अतश्च इत्यनेन लुग् भवतीति.'),
    ),
    "4.2.1": (
        _c('kāṣāyaṃ vastram — cloth dyed with an astringent',
           {'case': 'tṛtīyā', 'sense': 'rakta', 'samjna': 'rāga'},
           note='तेन रक्तं रागात्. रागादिति किम्? देवदत्तेन रक्तं वस्त्रम्. द्वैपवैयाघ्रादञ् इति यावत् तृतीयासमर्थविभक्तिरनुवर्तते.'),
    ),
    "4.2.2": (
        _c('lākṣikam — dyed with lac',
           {'case': 'tṛtīyā', 'sense': 'rakta', 'gana': 'lākṣādi'},
           note='लाक्षारोचनाशकलकर्दमाट् ठक्, अणोऽपवादः.'),
    ),
    "4.2.3": (
        _c('pauṣī rātriḥ — the night joined with Puṣya',
           {'case': 'tṛtīyā', 'sense': 'yukta', 'result': 'kāla', 'samjna': 'nakṣatra'},
           note='नक्षत्रेण युक्तः कालः. पुष्यादिसमीपस्थे चन्द्रमसि वर्तमानाः पुष्यादिशब्दाः प्रत्ययमुत्पादयन्ति.'),
    ),
    "4.2.4": (
        _c('adya puṣyaḥ — today is Puṣya, the affix dropped',
           {'case': 'tṛtīyā', 'sense': 'yukta', 'result': 'kāla', 'samjna': 'nakṣatra', 'unspecified': True},
           note='लुबविशेषे. अविशेष इति किम्? पौषी रात्रिः.'),
    ),
    "4.2.5": (
        _c('śravaṇā rātriḥ — a night so named',
           {'case': 'tṛtīyā', 'sense': 'yukta', 'result': 'kāla', 'stem': 'śravaṇa', 'samjna': 'saṃjñā'},
           note='संज्ञायां श्रवणाश्वत्थाभ्याम्. विशेषार्थोऽयमारम्भः.'),
    ),
    "4.2.6": (
        _c('rādhānurādhīyā rātriḥ — from a pair of star-names',
           {'case': 'tṛtīyā', 'sense': 'yukta', 'result': 'kāla', 'samjna': 'nakṣatra-dvandva'},
           note='द्वन्द्वाच्छः. लुपं परत्वाद् बाधते.'),
    ),
    "4.2.7": (
        _c('krauñcaṃ sāma — the chant seen by Kruñca',
           {'case': 'tṛtīyā', 'sense': 'dṛṣṭa', 'result': 'sāman'},
           note='तेन दृष्टम्.'),
    ),
    "4.2.8": (
        _c('kāleyam — the chant seen by Kali',
           {'case': 'tṛtīyā', 'sense': 'dṛṣṭa', 'result': 'sāman', 'stem': 'kali'},
           note='कलेर्ढक्, अणोऽपवादः. सर्वत्राग्निकलिभ्यां ढग् वक्तव्यः.'),
    ),
    "4.2.9": (
        _c('vāmadevyaṃ sāma — and its silent letter keeps it out of 6.2.156',
           {'case': 'tṛtīyā', 'sense': 'dṛṣṭa', 'result': 'sāman', 'stem': 'vāmadeva'},
           note='वामदेवाड् ड्यड्ड्यौ. डित्करणं किमर्थम्? अनयोर्ग्रहणं मा भूत्.'),
    ),
    "4.2.10": (
        _c('vāstro rathaḥ — a chariot wrapped in cloth',
           {'case': 'tṛtīyā', 'sense': 'parivṛta', 'result': 'ratha'},
           note='तेन परिवृतो रथः. यस्य न कश्चिदवयवो वस्त्रादिभिर् अवेष्टितः — छात्रैः परिवृतो रथः is not.'),
    ),
    "4.2.11": (
        _c('pāṇḍukambalī rathaḥ — a rule stated for what it prevents',
           {'case': 'tṛtīyā', 'sense': 'parivṛta', 'result': 'ratha', 'stem': 'pāṇḍukambala'},
           note='पाण्डुकम्बलादिनिः. मत्वर्थीयेनैव सिद्धे वचनमणो निवृत्त्यर्थम्.'),
    ),
    "4.2.12": (
        _c('dvaipo rathaḥ — and where the instrumental stops',
           {'case': 'tṛtīyā', 'sense': 'parivṛta', 'result': 'ratha', 'stem': 'dvaipa'},
           note='द्वैपवैयाघ्रादञ्, अणोऽपवादः, स्वरे विशेषः.'),
    ),
    "4.2.13": (
        _c("kaumāraḥ patiḥ — a girl's first husband",
           {'case': 'dvitīyā', 'stem': 'kumārī', 'samjna': 'apūrva'},
           note='कौमारापूर्ववचने. उभयतः स्त्रिया अपूर्वत्वे निपातनमेतत्.'),
    ),
    "4.2.14": (
        _c('śārāva odanaḥ — rice taken up in a dish',
           {'case': 'saptamī', 'sense': 'uddhṛta', 'samjna': 'amatra'},
           note='तत्रोद्धृतममत्रेभ्यः. क्षीराड् ढञ् इति यावत् सप्तमी समर्थविभक्तिरनुवर्तते.'),
    ),
    "4.2.15": (
        _c('sthāṇḍilo bhikṣuḥ — vowed to sleep on bare ground',
           {'case': 'saptamī', 'sense': 'śayita', 'stem': 'sthaṇḍila', 'samjna': 'vrata'},
           note='स्थण्डिलाच्छयितरि व्रते. व्रत इति किम्? स्थण्डिले शेते ब्रह्मदत्तः.'),
    ),
    "4.2.16": (
        _c('bhrāṣṭrā apūpāḥ — cakes prepared in a pan',
           {'case': 'saptamī', 'sense': 'saṃskṛta', 'result': 'bhakṣa'},
           note='संस्कृतं भक्षाः. सत उत्कर्षाधानं संस्कारः.'),
    ),
    "4.2.17": (
        _c('śūlyaṃ māṃsam — meat prepared on a spit',
           {'case': 'saptamī', 'sense': 'saṃskṛta', 'result': 'bhakṣa', 'stem': 'śūla'},
           note='शूलोखाद् यत्, अणोऽपवादः.'),
    ),
    "4.2.18": (
        _c('dādhikam — prepared in curds, and not BY them',
           {'case': 'saptamī', 'sense': 'saṃskṛta', 'result': 'bhakṣa', 'stem': 'dadhi'},
           note='दध्नष्ठक्. इह तु दधि केवलमाधारभूतम्, द्रव्यान्तरेण लवणादिना संस्कारः क्रियते.'),
    ),
    "4.2.19": (
        _c('audaśvitkam — optionally, the default standing otherwise',
           {'case': 'saptamī', 'sense': 'saṃskṛta', 'result': 'bhakṣa', 'stem': 'udaśvit'},
           note='उदश्वितोऽन्यतरस्याम्. पक्षे यथाप्राप्तमण् — औदश्वितम्.'),
    ),
    "4.2.20": (
        _c('kṣaireyī yavāgūḥ — and where the locative stops',
           {'case': 'saptamī', 'sense': 'saṃskṛta', 'result': 'bhakṣa', 'stem': 'kṣīra'},
           note='क्षीराड् ढञ्, अणोऽपवादः.'),
    ),
    "4.2.21": (
        _c('pauṣo māsaḥ — the month that holds the full moon',
           {'case': 'prathamā', 'sense': 'asmin', 'samjna': 'paurṇamāsī-saṃjñā'},
           note='सास्मिन् पौर्णमासीति संज्ञायाम्. संज्ञाशब्देन तुल्यताम् इतिकरणस्य ज्ञापयितुम्.'),
    ),
    "4.2.22": (
        _c('āgrahāyaṇiko māsaḥ — the month of Āgrahāyaṇī',
           {'case': 'prathamā', 'sense': 'asmin', 'stem': 'āgrahāyaṇī', 'samjna': 'paurṇamāsī-saṃjñā'},
           note='आग्रहायण्यश्वत्थाट् ठक्, अणोऽपवादः.'),
    ),
    "4.2.23": (
        _c('phālgunikaḥ — optionally, beside phālgunaḥ',
           {'case': 'prathamā', 'sense': 'asmin', 'gana': 'phālgunyādi', 'samjna': 'paurṇamāsī-saṃjñā'},
           note='विभाषा फाल्गुनीश्रवणाकार्तिकीचैत्रीभ्यः. नित्यमणि प्राप्ते पक्षे ठग् विधीयते.'),
    ),
    "4.2.24": (
        _c('aindraṃ haviḥ — the offering whose deity is Indra',
           {'case': 'prathamā', 'sense': 'devatā'},
           note='सास्य देवता. यागसंप्रदानं देवता, देयस्य पुरोडाशादेः स्वामिनी. देवतेति किम्? कन्या देवदत्तस्य.'),
    ),
    "4.2.25": (
        _c('kāyaṃ haviḥ — and the rule is the vowel, not the affix',
           {'case': 'prathamā', 'sense': 'devatā', 'stem': 'ka'},
           note='कस्येत्. ततः पूर्वेणैवाण्प्रत्ययः सिद्धः, इकारादेशार्थं वचनम्.'),
    ),
    "4.2.26": (
        _c('śukriyaṃ haviḥ — whose deity is Śukra',
           {'case': 'prathamā', 'sense': 'devatā', 'stem': 'śukra'},
           note='शुक्राद् घन्, अणोऽपवादः.'),
    ),
    "4.2.27": (
        _c("aponaptriyaṃ haviḥ — and the base's own shape fixed here",
           {'case': 'prathamā', 'sense': 'devatā', 'stem': 'aponaptṛ', 'wants': 'gha'},
           note='अपोनप्तृ अपांनप्तृभ्यां घः. तयोस्तु प्रत्ययसन्नियोगेन रूपमिदं निपात्यते.'),
    ),
    "4.2.28": (
        _c('aponaptrīyaṃ haviḥ — a rule split to prevent a pairing',
           {'case': 'prathamā', 'sense': 'devatā', 'stem': 'aponaptṛ', 'wants': 'cha'},
           note='छ च. योगविभागः सङ्ख्यातानुदेशपरिहारार्थः.'),
    ),
    "4.2.29": (
        _c('mahendriyaṃ haviḥ — one of three attested forms',
           {'case': 'prathamā', 'sense': 'devatā', 'stem': 'mahendra'},
           note='महेन्द्राद् घाणौ च. माहेन्द्रम् (तै०सं० ६.५.५.४), महेन्द्रीयम् (काठ०सं० १५.१).'),
    ),
    "4.2.30": (
        _c('saumyaṃ haviḥ — two marks doing two jobs',
           {'case': 'prathamā', 'sense': 'devatā', 'stem': 'soma'},
           note='सोमाट् ट्यण्. ण्कारो वृद्ध्यर्थः, टकारो ङीबर्थः.'),
    ),
    "4.2.31": (
        _c('vāyavyam — whose deity is Vāyu',
           {'case': 'prathamā', 'sense': 'devatā', 'gana': 'vāyvādi'},
           note='वायुऋतुपित्रुषसो यत्, अणोऽपवादः.'),
    ),
    "4.2.32": (
        _c('dyāvāpṛthivīyam — and dyāvāpṛthivyam beside it',
           {'case': 'prathamā', 'sense': 'devatā', 'gana': 'dyāvāpṛthivyādi'},
           note='द्यावापृथिवी ... गृहमेधाच् छः, चकाराद् यत् च. शुनो वायुः, सीर आदित्यः.'),
    ),
    "4.2.33": (
        _c("āgneyo'ṣṭākapālaḥ — whose deity is Agni",
           {'case': 'prathamā', 'sense': 'devatā', 'stem': 'agni'},
           note='अग्नेर्ढक्. सर्वत्राग्निकलिभ्यां ढग् वक्तव्यः.'),
    ),
    "4.2.34": (
        _c('māsikam — the affixes a later section will give',
           {'case': 'prathamā', 'sense': 'devatā', 'samjna': 'kāla'},
           note='कालेभ्यो भववत्. वत्करणं सर्वसादृश्यपरिग्रहार्थम्.'),
    ),
    "4.2.35": (
        _c('māhārājikam — and where the deity-sense stops',
           {'case': 'prathamā', 'sense': 'devatā', 'stem': 'mahārāja'},
           note='महाराजप्रोष्ठपदाट् ठञ्. ठञ्प्रकरणे तदस्मिन् वर्तत इति नवयज्ञादिभ्य उपसंख्यानम्.'),
    ),
    "4.2.36": (
        _c("pitṛvyaḥ — a father's brother, and everything fixed",
           {'stem': 'pitṛ', 'samjna': 'nipātana'},
           note='पितृव्यमातुलमातामहपितामहाः. समर्थविभक्तिः प्रत्ययः प्रत्ययार्थोऽनुबन्ध इति सर्वं निपातनाद् विज्ञेयम्.'),
    ),
    "4.2.37": (
        _c('kākānāṃ samūhaḥ kākam — a flock of crows',
           {'case': 'ṣaṣṭhī', 'sense': 'samūha'},
           note='तस्य समूहः. किमिहोदाहरणम्? चित्तवद् आद्युदात्तम् अगोत्रम् यस्य च नान्यत् प्रतिपदं ग्रहणम्.'),
    ),
    "4.2.38": (
        _c('bhaikṣam — a quantity of alms',
           {'case': 'ṣaṣṭhī', 'sense': 'samūha', 'gana': 'bhikṣādi'},
           note='भिक्षादिभ्योऽण्. अण्ग्रहणं बाधकबाधनार्थम्. युवतेर्ग्रहणसामर्थ्यात् पुंवद्भावो न भवति.'),
    ),
    "4.2.39": (
        _c('aupagavakam — and गोत्र read in its ordinary sense',
           {'case': 'ṣaṣṭhī', 'sense': 'samūha', 'gana': 'gotrādi'},
           note='गोत्रोक्षोष्ट्र ... अजाद् वुञ्. अपत्याधिकारादन्यत्र लौकिकं गोत्रं गृह्यते.'),
    ),
    "4.2.40": (
        _c('kaidāryam — a group of fields',
           {'case': 'ṣaṣṭhī', 'sense': 'samūha', 'stem': 'kedāra', 'wants': 'yañ'},
           note='केदाराद् यञ् च, अचित्तलक्षणस्य ठकोऽपवादः.'),
    ),
    "4.2.41": (
        _c('kāvacikam — and कैदारिकम् by the conjunction',
           {'case': 'ṣaṣṭhī', 'sense': 'samūha', 'stem': 'kavacin'},
           note='ठञ् कवचिनश्च. चकारः केदारादित्यस्यानुकर्षणार्थः.'),
    ),
    "4.2.42": (
        _c('brāhmaṇyam — a body of brahmins',
           {'case': 'ṣaṣṭhī', 'sense': 'samūha', 'gana': 'brāhmaṇādi'},
           note='ब्राह्मणमाणववाडवाद् यन्. नकारः स्वरार्थः. अह्नः खः क्रतौ — अहीनः क्रतुः.'),
    ),
    "4.2.43": (
        _c('grāmatā — a crowd of villages',
           {'case': 'ṣaṣṭhī', 'sense': 'samūha', 'gana': 'grāmādi'},
           note='ग्रामजनबन्धुसहायेभ्यस्तल्. जनता, बन्धुता, सहायता.'),
    ),
    "4.2.44": (
        _c('kāpotam — a flock of pigeons',
           {'case': 'ṣaṣṭhī', 'sense': 'samūha', 'samjna': 'anudāttādi'},
           note='अनुदात्तादेरञ्. One of the four rules 4.2.37 had to subtract.'),
    ),
    "4.2.45": (
        _c('khāṇḍikam — and one list-entry teaching two principles',
           {'case': 'ṣaṣṭhī', 'sense': 'samūha', 'gana': 'khaṇḍikādi'},
           note='खण्डिकादिभ्यश्च. एतज् ज्ञापयति — वुञि पूर्वविप्रतिषेधः, सामूहिकेषु च तदन्तविधिरस्तीति.'),
    ),
    "4.2.46": (
        _c('kāṭhakam — the same form for a practice and a group',
           {'case': 'ṣaṣṭhī', 'sense': 'samūha', 'samjna': 'caraṇa'},
           note='चरणेभ्यो धर्मवत्. वतिः सर्वसादृश्यार्थः.'),
    ),
    "4.2.47": (
        _c('āpūpikam — a quantity of cakes',
           {'case': 'ṣaṣṭhī', 'sense': 'samūha', 'samjna': 'acitta'},
           note='अचित्तहस्तिधेनोष्ठक्, अणञोरपवादः.'),
    ),
    "4.2.48": (
        _c('kaiśyam — a head of hair, and कैशिकम् beside it',
           {'case': 'ṣaṣṭhī', 'sense': 'samūha', 'stem': 'keśa', 'wants': 'yañ'},
           note='केशाश्वाभ्यां यञ्छावन्यतरस्याम्, यथासंख्यम्.'),
    ),
    "4.2.49": (
        _c('pāśyā — a bundle of snares',
           {'case': 'ṣaṣṭhī', 'sense': 'samūha', 'gana': 'pāśādi'},
           note='पाशादिभ्यो यः.'),
    ),
    "4.2.50": (
        _c('khalyā — and the three withheld from the last list',
           {'case': 'ṣaṣṭhī', 'sense': 'samūha', 'stem': 'khala', 'wants': 'ya'},
           note='खलगोरथात्. पाशादिष्वपाठ उत्तरार्थः.'),
    ),
    "4.2.51": (
        _c('khalinī — and where the collection-sense stops',
           {'case': 'ṣaṣṭhī', 'sense': 'samūha', 'stem': 'khala', 'wants': 'ini'},
           note='इनित्रकट्यचश्च, यथासंख्यम्. कमलादिभ्यः खण्डच् — कमलखण्डम्.'),
    ),
    "4.2.52": (
        _c('śaibo deśaḥ — the country of the Śibis',
           {'case': 'ṣaṣṭhī', 'sense': 'viṣaya', 'result': 'deśa'},
           note='तस्य विषयो देशः. विषयशब्दोऽयं बह्वर्थः. तत्र देशग्रहणं ग्रामसमुदायप्रतिपत्त्यर्थम्.'),
    ),
    "4.2.53": (
        _c('rājanyakaḥ — from an open list of peoples',
           {'case': 'ṣaṣṭhī', 'sense': 'viṣaya', 'result': 'deśa', 'gana': 'rājanyādi'},
           note='राजन्यादिभ्यो वुञ्. आकृतिगणश्चायम् — मालवकः, त्रैगर्तकः.'),
    ),
    "4.2.54": (
        _c('bhaurikividhaḥ — an affix that is a whole word',
           {'case': 'ṣaṣṭhī', 'sense': 'viṣaya', 'result': 'deśa', 'gana': 'bhaurikyādi'},
           note='भौरिक्याद्यैषुकार्यादिभ्यो विधल्भक्तलौ, यथासंख्यम्.'),
    ),
    "4.2.55": (
        _c('pāṅktaḥ pragāthaḥ — the metre that begins it',
           {'case': 'prathamā', 'sense': 'ādi', 'result': 'pragātha', 'samjna': 'chandas'},
           note='सोऽस्यादिरिति छन्दसः प्रगाथेषु. यत्र द्वे ऋचौ प्रग्रथनेन तिस्रः क्रियन्ते, स प्रगाथः.'),
    ),
    "4.2.56": (
        _c('bhādraḥ saṃgrāmaḥ — the battle fought for Bhadrā',
           {'case': 'prathamā', 'sense': 'asya', 'result': 'saṃgrāma', 'samjna': 'prayojana-yoddhṛ'},
           note='संग्रामे प्रयोजनयोद्धृभ्यः. प्रयोजनयोद्धृभ्य इति किम्? सुभद्रा प्रेक्षिकास्य संग्रामस्य.'),
    ),
    "4.2.57": (
        _c('dāṇḍā — the game whose weapon is a staff',
           {'case': 'prathamā', 'sense': 'asyām', 'result': 'krīḍā', 'samjna': 'praharaṇa'},
           note='तदस्मिन् प्रहरणमिति क्रीडायाम्. क्रीडायामिति किम्? खङ्गः प्रहरणमस्यां सेनायाम्.'),
    ),
    "4.2.58": (
        _c('śyainaṃpātā — and a bundle broken by restating it',
           {'case': 'prathamā', 'sense': 'asyām', 'samjna': 'ghañ-kriyā'},
           note='घञः स्त्रियाम्. क्रीडायामित्यनेन तत् संबद्धम्, अतस्तदनुवृत्तौ क्रीडानुवृत्तिरपि संभाव्येत.'),
    ),
    "4.2.59": (
        _c('chāndasaḥ — one who studies the Veda',
           {'case': 'dvitīyā', 'sense': 'adhīte-veda'},
           note='तदधीते तद्वेद. द्विस्तद्ग्रहणमधीयानविदुषोः पृथग्विधानार्थम्.'),
    ),
    "4.2.60": (
        _c('āgniṣṭomikaḥ — one who studies the Agniṣṭoma',
           {'case': 'dvitīyā', 'sense': 'adhīte-veda', 'gana': 'ukthādi'},
           note='क्रतूक्थादिसूत्रान्ताट् ठक्. औक्थिक्यशब्दाच्च प्रत्ययो न भवत्येव, अनभिधानात्.'),
    ),
    "4.2.61": (
        _c('kramakaḥ — one who studies the krama recitation',
           {'case': 'dvitīyā', 'sense': 'adhīte-veda', 'gana': 'kramādi'},
           note='क्रमादिभ्यो वुन्, अणोऽपवादः.'),
    ),
    "4.2.62": (
        _c('anubrāhmaṇī — and a rule kept for what it prevents',
           {'case': 'dvitīyā', 'sense': 'adhīte-veda', 'stem': 'anubrāhmaṇa'},
           note='अनुब्राह्मणादिनिः. अणो निवृत्त्यर्थं तर्हि वचनम्.'),
    ),
    "4.2.63": (
        _c('vāsantikaḥ — one who studies the spring text',
           {'case': 'dvitīyā', 'sense': 'adhīte-veda', 'gana': 'vasantādi'},
           note='वसन्तादिभ्यष्ठक्. वसन्तसहचरितोऽयं ग्रन्थो वसन्तः.'),
    ),
    "4.2.64": (
        _c('pāṇinīyaḥ — the student and the work in one word',
           {'case': 'dvitīyā', 'sense': 'adhīte-veda', 'samjna': 'prokta'},
           note='प्रोक्ताल्लुक्. प्रोक्तसहचरितः प्रत्ययः प्रोक्तः.'),
    ),
    "4.2.65": (
        _c('aṣṭakāḥ pāṇinīyāḥ — students named by the sections of a book',
           {'case': 'dvitīyā', 'sense': 'adhīte-veda', 'samjna': 'sūtra-ka-upadha'},
           note='सूत्राच्च कोपधात्. अप्रोक्तार्थ आरम्भः. कोपधादिति किम्? चातुष्टयः.'),
    ),
    "4.2.66": (
        _c('kaṭhāḥ — used of that subject only',
           {'samjna': 'prokta-chandas-brāhmaṇa'},
           note='छन्दोब्राह्मणानि च तद्विषयाणि. अनन्यभावो विषयार्थः, तेन स्वातन्त्र्यमुपाध्यन्तरयोगो वाक्यं च निवर्तते.'),
    ),
    "4.2.67": (
        _c('audumbaro deśaḥ — the country where fig-trees grow',
           {'case': 'prathamā', 'sense': 'cāturarthika', 'result': 'asti-deśe'},
           note='तदस्मिन्नस्तीति देशे तन्नाम्नि. मत्वर्थीयापवादो योगः.'),
    ),
    "4.2.68": (
        _c('kauśāmbī nagarī — the city Kuśāmba founded',
           {'case': 'tṛtīyā', 'sense': 'cāturarthika', 'result': 'nirvṛtta'},
           note='तेन निर्वृत्तम्. हेतौ कर्तरि च यथायोगं तृतीया समर्थविभक्तिः.'),
    ),
    "4.2.69": (
        _c('ārjunāvo deśaḥ — where the Ṛjunāvas dwell',
           {'case': 'ṣaṣṭhī', 'sense': 'cāturarthika', 'result': 'nivāsa'},
           note='तस्य निवासः. निवसन्त्यस्मिन्निति निवासः.'),
    ),
    "4.2.70": (
        _c('vaidiśaṃ nagaram — the town near Vidiśā',
           {'case': 'ṣaṣṭhī', 'sense': 'cāturarthika', 'result': 'adūrabhava'},
           note='अदूरभवश्च. चकारः पूर्वेषां त्रयाणामर्थानामिह सन्निधानार्थः.'),
    ),
    "4.2.71": (
        _c('āraḍavam — from a stem in उ',
           {'sense': 'cāturarthika', 'stem_final': 'u'},
           note='ओरञ्. अञधिकारः प्राक् सुवास्त्वादिभ्योऽणः.'),
    ),
    "4.2.72": (
        _c('aiṣukāvatam — and the word that fixes what is qualified',
           {'sense': 'cāturarthika', 'samjna': 'matup-bahvac-aṅga'},
           note='मतोश्च बह्वजङ्गात्. अङ्गग्रहणं किम्? बह्वजिति तद्विशेषणं यथा विज्ञायेत.'),
    ),
    "4.2.73": (
        _c('dairghavaratraḥ kūpaḥ — a well of that name',
           {'sense': 'cāturarthika', 'dvyac': True, 'result': 'kūpa'},
           note='बह्वचः कूपेषु. यथासंभवमर्थाः संबध्यन्ते.'),
    ),
    "4.2.74": (
        _c('dāttaḥ — a well on the north bank of the Vipāś',
           {'sense': 'cāturarthika', 'result': 'kūpa', 'samjna': 'udak-vipāś'},
           note='उदक् च विपाशः. महती सूक्ष्मेक्षिका वर्तते सूत्रकारस्य.'),
    ),
    "4.2.75": (
        _c('sāṃkalaḥ — from a list, and the wells stop here',
           {'sense': 'cāturarthika', 'gana': 'saṃkalādi'},
           note='संकलादिभ्यश्च. कूपेष्विति निवृत्तम्.'),
    ),
    "4.2.76": (
        _c('kākandī — a feminine place-name in one of three regions',
           {'sense': 'cāturarthika', 'samjna': 'strī-sauvīra-sālva-prāc'},
           note='स्त्रीषु सौवीरसाल्वप्राक्षु.'),
    ),
    "4.2.77": (
        _c('sauvāstavam — the default named to beat a later rule',
           {'sense': 'cāturarthika', 'gana': 'suvāstvādi'},
           note='सुवास्त्वादिभ्योऽण्. अण्ग्रहणं नद्यां मतुपो बाधनार्थम्.'),
    ),
    "4.2.78": (
        _c('rauṇaḥ — the base named in the wrong case on purpose',
           {'sense': 'cāturarthika', 'stem': 'roṇī'},
           note='रोणी. सर्वावस्थप्रतिपत्त्यर्थमेवमुच्यते.'),
    ),
    "4.2.79": (
        _c('kārṇacchidrikaḥ kūpaḥ — from a stem with क before its last',
           {'sense': 'cāturarthika', 'samjna': 'ka-upadha'},
           note='कोपधाच्च.'),
    ),
    "4.2.80": (
        _c('ārīhaṇakam — one of seventeen affixes matched to seventeen lists',
           {'sense': 'cāturarthika', 'gana': 'arīhaṇādi'},
           note='वुञ्छण् ... कुमुदादिभ्यः. वुञादयः सप्तदश प्रत्ययाः, अरीहणादयोऽपि सप्तदशैव प्रातिपदिकगणाः.'),
    ),
    "4.2.81": (
        _c("pañcālāḥ — the people's name serving as the country's",
           {'sense': 'cāturarthika', 'samjna': 'janapada'},
           note='जनपदे लुप्. तन्नाम्नीति वर्तते, न चात्र लुबन्तं तन्नामधेयं भवति.'),
    ),
    "4.2.82": (
        _c('varaṇāḥ — and where it is not a country',
           {'sense': 'cāturarthika', 'gana': 'varaṇādi'},
           note='वरणादिभ्यश्च. अजनपदार्थ आरम्भः.'),
    ),
    "4.2.83": (
        _c('śarkarā — one of six forms of one word',
           {'sense': 'cāturarthika', 'stem': 'śarkarā', 'wants': ''},
           note='शर्करायां वा. तदेवं षड् रूपाणि भवन्ति.'),
    ),
    "4.2.84": (
        _c('śārkarikam — two of the six',
           {'sense': 'cāturarthika', 'stem': 'śarkarā', 'wants': 'ṭhak'},
           note='ठक्छौ च.'),
    ),
    "4.2.85": (
        _c('udumbarāvatī — a river of that name',
           {'sense': 'cāturarthika', 'result': 'nadī'},
           note='नद्यां मतुप्. मतुबन्तस्यातन्नामधेयत्वात् — भागीरथी is outside it.'),
    ),
    "4.2.86": (
        _c('madhumān — and where it is not a river',
           {'sense': 'cāturarthika', 'gana': 'madhvādi'},
           note='मध्वादिभ्यश्च. अनद्यर्थ आरम्भः.'),
    ),
    "4.2.87": (
        _c('kumudvān — a marked form of the same affix',
           {'sense': 'cāturarthika', 'stem': 'kumuda'},
           note='कुमुदनडवेतसेभ्यो ड्मतुप्.'),
    ),
    "4.2.88": (
        _c('naḍvalam — a place full of reeds',
           {'sense': 'cāturarthika', 'stem': 'naḍa', 'wants': 'ḍvalac'},
           note='नडशादाड् ड्वलच्.'),
    ),
    "4.2.89": (
        _c('śikhāvalaṃ nagaram — and 5.2.113 gives the same affix elsewhere',
           {'sense': 'cāturarthika', 'stem': 'śikhā'},
           note='शिखाया वलच्. तददेशार्थं वचनम्.'),
    ),
    "4.2.90": (
        _c('utkarīyam — from a list',
           {'sense': 'cāturarthika', 'gana': 'utkarādi'},
           note='उत्करादिभ्यश्छः.'),
    ),
    "4.2.91": (
        _c('naḍakīyam — the affix with an augment, and the run stops',
           {'sense': 'cāturarthika', 'gana': 'naḍādi'},
           note='नडादीनां कुक् च.'),
    ),
    "4.2.92": (
        _c('cākṣuṣaṃ rūpam — in the remainder',
           {'sense': 'śeṣa'},
           note='शेषे, अधिकारोऽयम्. उपयुक्तादन्यः शेषः. शेष इति लक्षणं चाधिकारश्च.'),
    ),
    "4.2.93": (
        _c('rāṣṭriyaḥ — the affix given before its sense is stated',
           {'sense': 'śeṣa', 'stem': 'rāṣṭra'},
           note='राष्ट्रावारपाराद् घखौ. प्रकृतिविशेषोपादानमात्रेण तावत् प्रत्यया विधीयन्ते; तेषां तु जातादयोऽर्थाः पुरस्ताद् वक्ष्यन्ते.'),
    ),
    "4.2.94": (
        _c('grāmyaḥ — and grāmīṇaḥ, both standing',
           {'sense': 'śeṣa', 'stem': 'grāma'},
           note='ग्रामाद् यखञौ.'),
    ),
    "4.2.95": (
        _c('kātreyakaḥ — from a list',
           {'sense': 'śeṣa', 'gana': 'katryādi'},
           note='कत्र्यादिभ्यो ढकञ्.'),
    ),
    "4.2.96": (
        _c('kauleyakaḥ — a dog of the household',
           {'sense': 'śeṣa', 'stem': 'kula', 'result': 'śvan'},
           note='कुलकुक्षिग्रीवाभ्यः श्वास्यलंकारेषु. कौलोऽन्यः.'),
    ),
    "4.2.97": (
        _c('nādeyam — and a list-entry read two ways',
           {'sense': 'śeṣa', 'gana': 'nadyādi'},
           note='नद्यादिभ्यो ढक्. तदुभयमपि दर्शनं प्रमाणम्.'),
    ),
    "4.2.98": (
        _c('dākṣiṇātyaḥ — southern',
           {'sense': 'śeṣa', 'stem': 'dakṣiṇā'},
           note='दक्षिणापश्चात्पुरसस्त्यक्.'),
    ),
    "4.2.99": (
        _c('kāpiśāyanaṃ madhu — wine of Kāpiśī',
           {'sense': 'śeṣa', 'stem': 'kāpiśī'},
           note='कापिश्याः ष्फक्. षकारो ङीषर्थः.'),
    ),
    "4.2.100": (
        _c('rāṅkavo gauḥ — and the negative read as a comparison',
           {'sense': 'śeṣa', 'stem': 'raṅku', 'samjna': 'amanuṣya'},
           note='रङ्कोरमनुष्येऽण् च. नञिवयुक्तन्यायेन मनुष्यसदृशे प्राणिनि प्रतिपत्तिः क्रियते.'),
    ),
    "4.2.101": (
        _c('divyam — heavenly',
           {'sense': 'śeṣa', 'stem': 'div'},
           note='दिक्प्रागपागुदक्प्रतीचो यत्.'),
    ),
    "4.2.102": (
        _c('kānthikaḥ — of a patched garment',
           {'sense': 'śeṣa', 'stem': 'kanthā', 'wants': 'ṭhak'},
           note='कन्थायाष्ठक्.'),
    ),
    "4.2.103": (
        _c('kānthakam — the same word in one particular country',
           {'sense': 'śeṣa', 'stem': 'kanthā', 'samjna': 'varṇu'},
           note='वर्णौ वुक्, ठकोऽपवादः. वर्णुर्नाम नदः, तत्समीपो देशो वर्णुः.'),
    ),
    "4.2.104": (
        _c('amātyaḥ — and a verse counting which indeclinables',
           {'sense': 'śeṣa', 'samjna': 'avyaya'},
           note='अव्ययात् त्यप्. परिगणनं किम्? औपरिष्टः, पौरस्तः.'),
    ),
    "4.2.105": (
        _c('hyastyam — and hyastanam beside it',
           {'sense': 'śeṣa', 'stem': 'hyas'},
           note='ऐषमोह्यःश्वसोऽन्यतरस्याम्. श्वसस्तुट् च इति ठञपि तृतीयो भवति.'),
    ),
    "4.2.106": (
        _c('kākatīram — having तीर as its last member',
           {'sense': 'śeṣa', 'stem_final': 'tīra'},
           note='तीररूप्योत्तरपदादञ्ञौ. तीररूप्यान्तादिति नोक्तम्, बहुच्प्रत्ययपूर्वाद् मा भूदिति.'),
    ),
    "4.2.107": (
        _c('paurvaśālaḥ — a direction in front, and not a name',
           {'sense': 'śeṣa', 'pre': 'dik', 'samjna': 'asaṃjñā'},
           note='दिक्पूर्वपदादसंज्ञायां ञः. पदग्रहणं स्वरूपविधिनिरासार्थम्.'),
    ),
    "4.2.108": (
        _c('paurvamadraḥ — and 7.3.13 excepts the word by name',
           {'sense': 'śeṣa', 'stem': 'madra', 'pre': 'dik'},
           note='मद्रेभ्योऽञ्. दिशोऽमद्राणाम् इति पर्युदासाद् आदिवृद्धिरेव.'),
    ),
    "4.2.109": (
        _c('śaivapuram — a northern village-name',
           {'sense': 'śeṣa', 'samjna': 'udīcya-grāma', 'dvyac': True, 'accent': 'antodātta'},
           note='उदीच्यग्रामाच्च बह्वचोऽन्तोदात्तात्. अन्तोदात्तादिति किम्? शार्करीधानम्.'),
    ),
    "4.2.110": (
        _c('mādrīprasthaḥ — the default named to beat its beaters',
           {'sense': 'śeṣa', 'stem_final': 'prastha'},
           note='प्रस्थोत्तरपदपलद्यादिकोपधादण्. अण्ग्रहणं बाधकबाधनार्थम्.'),
    ),
    "4.2.111": (
        _c('kāṇvāś chātrāḥ — a rule pointing at another rule',
           {'sense': 'śeṣa', 'marked': 'kaṇvādi-gotra'},
           note='कण्वादिभ्यो गोत्रे. गोत्रमिह न प्रत्ययार्थो न च प्रकृतिविशेषणम्.'),
    ),
    "4.2.112": (
        _c('dākṣāḥ — from a lineage-affix, and only from one',
           {'sense': 'śeṣa', 'marked': 'iñ-gotra'},
           note='इञश्च. गोत्र इत्येव — सौतङ्गमीयम्.'),
    ),
    "4.2.113": (
        _c('paiṅgīyāḥ — refused, so the other affix supplies',
           {'sense': 'śeṣa', 'dvyac': True, 'samjna': 'prācya-bharata-gotra'},
           note='न द्व्यचः प्राच्यभरतेषु. ज्ञापकाद् अन्यत्र प्राच्यग्रहणेन भरतग्रहणं न भवतीति.'),
    ),
    "4.2.114": (
        _c('gārgīyaḥ — general now, and beating four rules by परत्व',
           {'sense': 'śeṣa', 'samjna': 'vṛddha'},
           note='वृद्धाच्छः. गोत्र इति नानुवर्तते, सामान्येन विधानम्.'),
    ),
    "4.2.115": (
        _c('bhāvatkaḥ — strengthened by class, not by its own vowel',
           {'sense': 'śeṣa', 'stem': 'bhavat', 'samjna': 'vṛddha'},
           note='भवतष्ठक्छसौ. भवतस्त्यदादित्वाद् वृद्धसंज्ञा.'),
    ),
    "4.2.116": (
        _c('kāśikī — and kāśikā, differing only in the feminine',
           {'sense': 'śeṣa', 'gana': 'kāśyādi', 'samjna': 'vṛddha'},
           note='काश्यादिभ्यष्ठञ्ञिठौ. वा नामधेयस्येति व्यवस्थितविभाषेयम्, सा छे कर्तव्ये भवति.'),
    ),
    "4.2.117": (
        _c('śākalikī — from a village-name of one region',
           {'sense': 'śeṣa', 'samjna': 'vāhīka-grāma-vṛddha'},
           note='वाहीकग्रामेभ्यश्च, छस्यापवादौ.'),
    ),
    "4.2.118": (
        _c('āhvajālikī — a third form, from the option',
           {'sense': 'śeṣa', 'samjna': 'uśīnara-vāhīka-grāma-vṛddha'},
           note='विभाषोशीनरेषु. आह्वजालिकी, आह्वजालिका, आह्वजालीया.'),
    ),
    "4.2.119": (
        _c('naiṣādakarṣukaḥ — and वृद्ध lapses, proved by the next rule naming it',
           {'sense': 'śeṣa', 'stem_final': 'u', 'desa': True},
           note='ओर्देशे ठञ्. वृद्धादिति नानुवर्तते, उत्तरसूत्रे पुनर्वृद्धग्रहणात्.'),
    ),
    "4.2.120": (
        _c('āḍhakajambukaḥ — a rule that adds nothing, so it restricts',
           {'sense': 'śeṣa', 'stem_final': 'u', 'desa': True, 'samjna': 'prāc-vṛddha'},
           note='वृद्धात् प्राचाम्. पूर्वेणैव ठञि सिद्धे नियमार्थं वचनम्.'),
    ),
    "4.2.121": (
        _c('sāṃkāśyakaḥ — the first rule of the pāda stated on the penultimate sound',
           {'sense': 'śeṣa', 'desa': True, 'samjna': 'vṛddha', 'upadha': 'y'},
           note='धन्वयोपधाद्वुञ्. धन्वशब्दो मरुदेशवचनः.'),
    ),
    "4.2.122": (
        _c('mālāprasthakaḥ — and *ending* attaches to each of the three words',
           {'sense': 'śeṣa', 'desa': True, 'samjna': 'vṛddha', 'ends_with': 'prastha'},
           note='प्रस्थपुरवहान्ताच्च. अन्तशब्दः प्रत्येकमभिसंबध्यते.'),
    ),
    "4.2.123": (
        _c('pāṭaliputrakāḥ — eastern, and the ta is only for plainness',
           {'sense': 'śeṣa', 'desa': True, 'samjna': 'prāc-vṛddha', 'upadha': 'r'},
           note='रोपधेतोः प्राचाम्. तपरकरणं विस्पष्टार्थम्.'),
    ),
    "4.2.124": (
        _c('traigartakaḥ — a boundary named to beat a later rule',
           {'sense': 'śeṣa', 'desa': True, 'samjna': 'janapada-avadhi-vṛddha'},
           note='जनपदतदवध्योश्च. किमर्थं तर्हि अवधिग्रहणम्? बाधकबाधनार्थम्.'),
    ),
    "4.2.125": (
        _c('āṅgakaḥ — and *also* gathers, by the maxim of buttermilk for Kauṇḍinya',
           {'sense': 'śeṣa', 'desa': True, 'samjna': 'janapada-bahuvacana'},
           note='अवृद्धादपि बहुवचनविषयात्. तक्रकौण्डिन्यन्यायेन बाधा मा विज्ञायीति समुच्चीयते.'),
    ),
    "4.2.126": (
        _c('dārukacchakaḥ — four last members, with or without the lengthening',
           {'sense': 'śeṣa', 'desa': True, 'ends_with': 'kaccha'},
           note='कच्छाग्निवक्त्रवर्त्तोत्तरपदात्. उत्तरपदशब्दः प्रत्येकमभिसंबध्यते.'),
    ),
    "4.2.127": (
        _c('dhaumakaḥ — a list holding entries that widen one rule and narrow another',
           {'sense': 'śeṣa', 'desa': True, 'gana': 'dhūmādi'},
           note='धूमादिभ्यश्च. सामर्थ्याददेशार्थं ग्रहणम्.'),
    ),
    "4.2.128": (
        _c('nāgarakaḥ — blame in one verse and skill in the next',
           {'sense': 'śeṣa', 'stem': 'nagara', 'result': 'kutsana-prāvīṇya'},
           note='नगरात् कुत्सनप्रावीण्ययोः. चोरा हि नागरका भवन्ति. प्रवीणा हि नागरका भवन्ति.'),
    ),
    "4.2.129": (
        _c('āraṇyako manuṣyaḥ — and a road, a lesson, a rule, a grove, an elephant',
           {'sense': 'śeṣa', 'stem': 'araṇya', 'result': 'manuṣya'},
           note='अरण्यान्मनुष्ये. पथ्यध्यायन्यायविहारमनुष्यहस्तिष्विति वक्तव्यम्.'),
    ),
    "4.2.130": (
        _c('kauravakaḥ — an option that turns out to be for one word only',
           {'sense': 'śeṣa', 'stem': 'kuru'},
           note='विभाषा कुरुयुगन्धराभ्याम्. सैषा युगन्धरार्था विभाषा.'),
    ),
    "4.2.131": (
        _c('madrakaḥ — a different affix for two districts',
           {'sense': 'śeṣa', 'stem': 'madra'},
           note='मद्रवृज्योः कन्, जनपदवुञोऽपवादः.'),
    ),
    "4.2.132": (
        _c('ārṣikaḥ — a penultimate k, and the affix named to beat a rival',
           {'sense': 'śeṣa', 'desa': True, 'upadha': 'k'},
           note='कोपधादण्. अण्ग्रहणमुवर्णान्तादपि यथा स्यात्.'),
    ),
    "4.2.133": (
        _c('kācchaḥ — a list with two entries read for the sake of later rules',
           {'sense': 'śeṣa', 'desa': True, 'gana': 'kacchādi'},
           note='कच्छादिभ्यश्च. तस्य मनुष्यतत्स्थयोर्वुञर्थः पाठः.'),
    ),
    "4.2.134": (
        _c('kācchako manuṣyaḥ — a man, or the laughter and the hair that stand in him',
           {'sense': 'śeṣa', 'gana': 'kacchādi', 'result': 'manuṣya-tatstha'},
           note='मनुष्यतत्स्थयोर्वुञ्. मनुष्यतत्स्थयोरिति किम्? काच्छो गौः.'),
    ),
    "4.2.135": (
        _c('sālvako manuṣyaḥ — but not if the man is on foot',
           {'sense': 'śeṣa', 'stem': 'sālva', 'result': 'apadāti-manuṣya-tatstha'},
           note='अपदातौ साल्वात्. पूर्वेणैव मनुष्यतत्स्थयोर्वुञि सिद्धे नियमार्थं वचनम्.'),
    ),
    "4.2.136": (
        _c('sālvako gauḥ — an ox and a gruel, which no man could have covered',
           {'sense': 'śeṣa', 'stem': 'sālva', 'result': 'go-yavāgū'},
           note='गोयवाग्वोश्च, कच्छाद्यणोऽपवादः. साल्वमन्यत्.'),
    ),
    "4.2.137": (
        _c('vṛkagartīyam — and *last member* keeps a prefix out',
           {'sense': 'śeṣa', 'desa': True, 'ends_with': 'garta'},
           note='गर्तोत्तरपदाच्छः. उत्तरपदग्रहणं बहुच्पूर्वनिरासार्थम्.'),
    ),
    "4.2.138": (
        _c('gahīyaḥ — a heading that qualifies only the entries it can',
           {'sense': 'śeṣa', 'gana': 'gahādi'},
           note='गहादिभ्यश्च. देशाधिकारेऽपि संभवापेक्षं विशेषणम्, न सर्वेषाम्.'),
    ),
    "4.2.139": (
        _c('kaṭanagarīyam — a list, and the east qualifies the country',
           {'sense': 'śeṣa', 'desa': True, 'gana': 'kaṭādi', 'samjna': 'prāc'},
           note='प्राचां कटादेः, अणोऽपवादः.'),
    ),
    "4.2.140": (
        _c('rājakīyam — a substitute enjoined, and the affix left standing',
           {'sense': 'śeṣa', 'stem': 'rājan', 'samjna': 'vṛddha'},
           note='राज्ञः क च. आदेशमात्रमिह विधेयम्, प्रत्ययस्तु वृद्धाच्छ इत्येव सिद्धः.'),
    ),
    "4.2.141": (
        _c('āśvapathikīyam — three earlier rules beaten at once',
           {'sense': 'śeṣa', 'desa': True, 'samjna': 'vṛddha', 'ends_with': 'aka'},
           note='वृद्धादकेकान्तखोपधात्. अकेकान्तग्रहणे कोपधग्रहणं सौसुकाद्यर्थम्.'),
    ),
    "4.2.142": (
        _c('dākṣikanthīyam — five last members, one pair of first members',
           {'sense': 'śeṣa', 'desa': True, 'samjna': 'vṛddha', 'ends_with': 'kanthā'},
           note='कन्थापलदनगरग्रामह्रदोत्तरपदात्, वाहीकग्रामादिलक्षणस्य प्रत्ययस्यापवादः.'),
    ),
    "4.2.143": (
        _c('parvatīyo rājā — the king of the mountain',
           {'sense': 'śeṣa', 'stem': 'parvata'},
           note='पर्वताच्च, अणोऽपवादः. पर्वतीयः पुरुषः.'),
    ),
    "4.2.144": (
        _c('parvatīyāni phalāni — the option for everything but the man',
           {'sense': 'śeṣa', 'stem': 'parvata', 'result': 'amanuṣya'},
           note='विभाषाऽमनुष्ये. पूर्वेण नित्ये प्राप्ते विकल्प उच्यते.'),
    ),
    "4.2.145": (
        _c('kṛkaṇīyam — the country of that name, not the lineage',
           {'sense': 'śeṣa', 'desa': True, 'stem': 'kṛkaṇa', 'samjna': 'bhāradvāja-deśa'},
           note='कृकणपर्णाद्भारद्वाजे. भारद्वाजशब्दोऽपि देशवचन एव, न गोत्रशब्दः.'),
    ),
    "4.3.1": (
        _c('yauṣmākīṇaḥ — three affixes, and no pairing to be had',
           {'sense': 'śeṣa', 'stem': 'yuṣmad'},
           note='युष्मदस्मदोरन्यतरस्यां खञ् च. वैषम्याद् यथासंख्यं न भवति.'),
    ),
    "4.3.2": (
        _c('yuṣmāka — a substitute before the affix that was stated outright',
           {'sense': 'śeṣa', 'stem': 'yuṣmad', 'before': 'khañ'},
           note='तस्मिन्नणि च युष्माकास्माकौ. तस्मिन्निति साक्षाद् विहितः खञ् निर्दिश्यते, न चकारानुकृष्टश्छः.'),
    ),
    "4.3.3": (
        _c('tavaka — and another when one person is meant',
           {'sense': 'śeṣa', 'stem': 'yuṣmad', 'before': 'khañ', 'samjna': 'ekavacana'},
           note='तवकममकावेकवचने. नैवेदं प्रत्ययग्रहणम्, अन्वर्थग्रहणम्.'),
    ),
    "4.3.4": (
        _c('ardhyam — from the word for half',
           {'sense': 'śeṣa', 'stem': 'ardha'},
           note='अर्धाद् यत्, अणोऽपवादः. सपूर्वपदाट् ठञ् वक्तव्यः.'),
    ),
    "4.3.5": (
        _c('parārdhyam — four words in front, and one of them doing double duty',
           {'sense': 'śeṣa', 'stem': 'ardha', 'pre': 'para-avara-adhama-uttama'},
           note='परावराधमोत्तमपूर्वाच्च. परावरशब्दौ अदिग्ग्रहणावपि स्तः.'),
    ),
    "4.3.6": (
        _c('paurvārdhikam — a direction in front, and two affixes',
           {'sense': 'śeṣa', 'pre': 'dik', 'stem_final': 'ardha'},
           note='दिक्पूर्वपदाट् ठञ् च. पदग्रहणं स्वरूपविधिनिवारणार्थम्.'),
    ),
    "4.3.7": (
        _c('paurvārdhikāḥ — a part of a village, by its direction',
           {'sense': 'śeṣa', 'pre': 'dik', 'stem_final': 'ardha', 'samjna': 'grāma-janapada-ekadeśa'},
           note='ग्रामजनपदैकदेशादञ्ठञौ, यतोऽपवादौ.'),
    ),
    "4.3.8": (
        _c('madhyamaḥ — and two supplements make three ordinals',
           {'sense': 'śeṣa', 'stem': 'madhya'},
           note='मध्यान्मः, अणोऽपवादः. अवोऽधसोर्लोपश्च.'),
    ),
    "4.3.9": (
        _c('madhyo vaiyākaraṇaḥ — a grammarian of the middling sort',
           {'sense': 'śeṣa', 'stem': 'madhya', 'result': 'sāmpratika'},
           note='अ साम्प्रतिके, मस्यापवादः. सांप्रतिकं न्याय्यं युक्तमुचितं सममुच्यते.'),
    ),
    "4.3.10": (
        _c('dvaipyam — an island near the sea, beating two rules',
           {'sense': 'śeṣa', 'stem': 'dvīpa', 'samjna': 'anusamudra'},
           note='द्वीपादनुसमुद्रं यञ्. कच्छादिपाठाद् अणो मनुष्यवुञश्चापवादः.'),
    ),
    "4.3.11": (
        _c('sāṃvatsarikaḥ — a heading of time, with its end stated',
           {'sense': 'śeṣa', 'samjna': 'kāla'},
           note='कालाट् ठञ्. तत्र जातः इति प्रागतः कालाधिकारः.'),
    ),
    "4.3.12": (
        _c('śāradikaṃ śrāddham — the rite, excluded by usage from meaning a man',
           {'sense': 'śeṣa', 'stem': 'śarad', 'result': 'śrāddha'},
           note='श्राद्धे शरदः. श्राद्ध इति च कर्म गृह्यते, न श्रद्धावान् पुरुषः, अनभिधानात्.'),
    ),
    "4.3.13": (
        _c('śāradiko rogaḥ — the autumn fever, and both forms stand',
           {'sense': 'śeṣa', 'stem': 'śarad', 'result': 'roga-ātapa'},
           note='विभाषा रोगातपयोः. रोगातपयोरिति किम्? शारदं दधि.'),
    ),
    "4.3.14": (
        _c('naiśikam — an option spoken against a fixed affix',
           {'sense': 'śeṣa', 'stem': 'niśā'},
           note='निशाप्रदोषाभ्यां च. कालाट् ठञ् इति नित्ये ठञि प्राप्ते विकल्प उच्यते.'),
    ),
    "4.3.15": (
        _c('śauvastikaḥ — and two more rules waiting behind the option',
           {'sense': 'śeṣa', 'stem': 'śvas'},
           note='श्वसस्तुट् च. एताभ्यां मुक्ते ट्युट्युलावपि भवतः.'),
    ),
    "4.3.16": (
        _c('taiṣam — a lunar mansion, and the months named from it',
           {'sense': 'śeṣa', 'samjna': 'nakṣatra'},
           note='संधिवेलाद्यृतुनक्षत्रेभ्योऽण्. अण्ग्रहणं वृद्धाच्छस्य बाधनार्थम्.'),
    ),
    "4.3.17": (
        _c('prāvṛṣeṇyo balāhakaḥ — the cloud of the rains',
           {'sense': 'śeṣa', 'stem': 'prāvṛṣ'},
           note='प्रावृष एण्यः, ऋत्वणोऽपवादः.'),
    ),
    "4.3.18": (
        _c('vārṣikaṃ vāsaḥ — the cloak for the rains',
           {'sense': 'śeṣa', 'stem': 'varṣā'},
           note='वर्षाभ्यष्ठक्, ऋत्वणोऽपवादः.'),
    ),
    "4.3.19": (
        _c('vārṣikāvṛtū — an affix differing only in the accent',
           {'sense': 'śeṣa', 'stem': 'varṣā', 'usage': 'chandasi'},
           note='छन्दसि ठञ्, ठकोऽपवादः. स्वरे भेदः.'),
    ),
    "4.3.20": (
        _c('vāsantikāvṛtū — from the same verse as its neighbours',
           {'sense': 'śeṣa', 'stem': 'vasanta', 'usage': 'chandasi'},
           note='वसन्ताच्च, छन्दसीत्येव; ऋत्वणोऽपवादः.'),
    ),
    "4.3.21": (
        _c("haimantikāvṛtū — a rule split off for the next one's sake",
           {'sense': 'śeṣa', 'stem': 'hemanta', 'usage': 'chandasi'},
           note='हेमन्ताच्च. योगविभाग उत्तरार्थः.'),
    ),
    "4.3.22": (
        _c('haimanaṃ vāsaḥ — a cancellation said aloud so it reaches backward',
           {'sense': 'śeṣa', 'stem': 'hemanta'},
           note='सर्वत्राण् च तलोपश्च. सर्वत्रग्रहणं छन्दोऽधिकारनिवृत्त्यर्थम्.'),
    ),
    "4.3.23": (
        _c('sāyaṃtanam — a rule that makes the words it attaches to',
           {'sense': 'śeṣa', 'stem': 'sāyam'},
           note='सायंचिरम्प्राह्णेप्रगेऽव्ययेभ्यष्ट्युट्युलौ तुट् च. प्रत्ययसन्नियोगेन निपात्यते.'),
    ),
    "4.3.24": (
        _c('pūrvāhṇetanam — a case-ending kept, and reporting itself',
           {'sense': 'śeṣa', 'stem': 'pūrvāhṇa'},
           note='विभाषा पूर्वाह्णापराह्णाभ्याम्. घकालतनेषु कालनाम्नः इति सप्तम्या अलुक्.'),
    ),
    "4.3.25": (
        _c('grāmyaḥ — born there, and the affix is whichever was already prescribed',
           {'sense': 'jāta', 'case': 'saptamī', 'stem': 'grāma'},
           note='तत्र जातः. अणादयो घादयश्च प्रत्ययाः प्रकृताः, तेषामतः प्रभृत्यर्थाः समर्थविभक्तयश्च निर्दिश्यन्ते.'),
    ),
    "4.3.26": (
        _c('prāvṛṣi jātaḥ prāvṛṣikaḥ — and a letter spent on the accent',
           {'sense': 'jāta', 'case': 'saptamī', 'stem': 'prāvṛṣ'},
           note='प्रावृषष्ठप्, एण्यस्यापवादः. पकारः स्वरार्थः.'),
    ),
    "4.3.27": (
        _c('śāradakā darbhāḥ — a name understood from the whole',
           {'sense': 'jāta', 'case': 'saptamī', 'stem': 'śarad', 'samjna': 'saṃjñā'},
           note='संज्ञायां शरदो वुञ्. समुदायेन चेत् संज्ञा गम्यते.'),
    ),
    "4.3.28": (
        _c('pūrvāhṇakaḥ — six bases, and four rules displaced',
           {'sense': 'jāta', 'case': 'saptamī', 'gana': 'pūrvāhṇādi', 'samjna': 'saṃjñā'},
           note='पूर्वाह्णापराह्णार्द्रामूलप्रदोषावस्करादद्वुन्. असंज्ञायां तु यथाप्राप्तं ठञादय एव भवन्ति.'),
    ),
    "4.3.29": (
        _c('pathi jātaḥ panthakaḥ — an affix and a substitute in one act',
           {'sense': 'jāta', 'case': 'saptamī', 'stem': 'pathin'},
           note='पथः पन्थ च, अणोऽपवादः. प्रत्ययसन्नियोगेन.'),
    ),
    "4.3.30": (
        _c('amāvāsyakaḥ — and a maxim carries it to a variant spelling',
           {'sense': 'jāta', 'case': 'saptamī', 'stem': 'amāvāsyā'},
           note='अमावास्याया वा. एकदेशविकृतस्यानन्यत्वात्.'),
    ),
    "4.3.31": (
        _c('amāvāsyaḥ — a third affix, and six forms in all',
           {'sense': 'jāta', 'case': 'saptamī', 'stem': 'amāvāsyā', 'wants': 'a'},
           note='अ च. पूर्वेण वुन्नणोः प्राप्तयोरयं तृतीयः प्रत्ययो विधीयते.'),
    ),
    "4.3.32": (
        _c('sindhukaḥ — two rules of the last quarter displaced',
           {'sense': 'jāta', 'case': 'saptamī', 'stem': 'sindhu', 'wants': 'kan'},
           note='सिन्ध्वपकराभ्यां कन्. सिन्धुशब्दः कच्छादिः.'),
    ),
    "4.3.33": (
        _c('saindhavaḥ — and here the matching-in-order runs',
           {'sense': 'jāta', 'case': 'saptamī', 'stem': 'sindhu', 'wants': 'aṇ'},
           note='अणञौ च, यथासंख्यम्. पूर्वेण कनि प्राप्ते वचनम्.'),
    ),
    "4.3.34": (
        _c('śraviṣṭhaḥ — the affix taken away, and the feminine affix with it',
           {'sense': 'jāta', 'case': 'saptamī', 'gana': 'śraviṣṭhādi', 'samjna': 'nakṣatra'},
           note='श्रविष्ठादिभ्यो लुक्. तस्मिन् स्त्रीप्रत्ययस्यापि लुक् तद्धितलुकि इति लुग् भवति.'),
    ),
    "4.3.35": (
        _c("gosthānaḥ — called by the shed's own name",
           {'sense': 'jāta', 'case': 'saptamī', 'stem_final': 'sthāna'},
           note='स्थानान्तगोशालखरशालाच्च. गोस्थाने जातो गोस्थानः.'),
    ),
    "4.3.36": (
        _c('vatsaśālaḥ — an unfolding of one word of the next rule',
           {'sense': 'jāta', 'case': 'saptamī', 'stem': 'vatsaśālā'},
           note='वत्सशालाभिजिदश्वयुक्छतभिषजो वा. बहुलग्रहणस्यायं प्रपञ्चः.'),
    ),
    "4.3.37": (
        _c('rohiṇaḥ — variously, which is not optionally',
           {'sense': 'jāta', 'case': 'saptamī', 'samjna': 'nakṣatra'},
           note='नक्षत्रेभ्यो बहुलम्. रोहिणः, रौहिणः.'),
    ),
    "4.3.38": (
        _c('sraughnaḥ — four senses the facts do not keep apart',
           {'sense': 'kṛta-labdha-krīta-kuśala', 'case': 'saptamī'},
           note='कृतलब्धक्रीतकुशलाः. शब्दार्थस्य भिन्नत्वाद् वस्तुमात्रेण क्रीतं लब्धं भवति, शब्दार्थस्तु भिद्यत एव.'),
    ),
    "4.3.39": (
        _c('sraughnaḥ — and the commentary calls the rule pointless',
           {'sense': 'prāya-bhava', 'case': 'saptamī'},
           note='प्रायभवः. प्रायभवग्रहणमनर्थकम्, तत्रभवेन कृतार्थत्वात्.'),
    ),
    "4.3.40": (
        _c('aupajānukaḥ — mostly about the knee',
           {'sense': 'prāya-bhava', 'case': 'saptamī', 'stem': 'upajānu'},
           note='उपजान्वुपकर्णोपनीवेष्ठक्, अणोऽपवादः.'),
    ),
    "4.3.41": (
        _c('sraughnaḥ — a sense narrowed by subtracting its neighbours',
           {'sense': 'saṃbhūta', 'case': 'saptamī'},
           note='संभूते. नोत्पत्तिः सत्ता वा, जातभवाभ्यां गतत्वात्.'),
    ),
    "4.3.42": (
        _c('kauśeyaṃ vastram — conventional, so not of the worm',
           {'sense': 'saṃbhūta', 'case': 'saptamī', 'stem': 'kośa'},
           note='कोशाड्ढञ्. रूढिरेषा, तेन क्रिमौ न भवति, खड्गकोशाच्च.'),
    ),
    "4.3.43": (
        _c('vāsantyaḥ kundalatāḥ — and the time-word spoken a second time',
           {'sense': 'sādhu-puṣpyat-pacyamāna', 'case': 'saptamī', 'samjna': 'kāla'},
           note='कालात् साधुपुष्प्यत्पच्यमानेषु. वसन्ते पुष्प्यन्ति वासन्त्यः कुन्दलताः.'),
    ),
    "4.3.44": (
        _c("haimantā yavāḥ — a rule split off for the next one's sake",
           {'sense': 'upta', 'case': 'saptamī', 'samjna': 'kāla'},
           note='उप्ते च. योगविभाग उत्तरार्थः.'),
    ),
    "4.3.45": (
        _c('āśvayujakā māṣāḥ — and the base derived before use',
           {'sense': 'upta', 'case': 'saptamī', 'stem': 'āśvayujī'},
           note='आश्वयुज्या वुञ्. अश्विनीभ्यां युक्ता पौर्णमासी, आश्वयुजी.'),
    ),
    "4.3.46": (
        _c('graiṣmakam — beside the form without the option',
           {'sense': 'upta', 'case': 'saptamī', 'stem': 'grīṣma'},
           note='ग्रीष्मवसन्तादन्यतरस्याम्, ऋत्वणोऽपवादः.'),
    ),
    "4.3.47": (
        _c('māsikam — but only if what is owed is a debt',
           {'sense': 'deya-ṛṇa', 'case': 'saptamī', 'samjna': 'kāla'},
           note='देयमृणे. ऋण इति किम्? मासे देया भिक्षा.'),
    ),
    "4.3.48": (
        _c('kalāpakam — a season named by what happens in it',
           {'sense': 'deya-ṛṇa', 'case': 'saptamī', 'stem': 'kalāpin'},
           note='कलाप्यश्वत्थयवबुसाद् वुन्. कलाप्यादयः शब्दाः साहचर्यात् काले वर्तन्ते.'),
    ),
    "4.3.49": (
        _c('graiṣmakam — an affix chosen for the strengthening',
           {'sense': 'deya-ṛṇa', 'case': 'saptamī', 'stem': 'grīṣma'},
           note='ग्रीष्मावरसमाद् वुञ्. प्रत्ययान्तरकरणं वृद्ध्यर्थम्.'),
    ),
    "4.3.50": (
        _c('sāṃvatsarikam — named, not optioned, because the reach differs',
           {'sense': 'deya-ṛṇa', 'case': 'saptamī', 'stem': 'saṃvatsara'},
           note='संवत्सराग्रहायणीभ्यां ठञ् च. वेति वक्तव्ये ठञ्ग्रहणम्.'),
    ),
    "4.3.51": (
        _c('naiśaḥ — the time at which a deer calls',
           {'sense': 'vyāharati-mṛgaḥ', 'case': 'saptamī', 'samjna': 'kāla'},
           note='व्याहरति मृगः. मृग इति किम्? निशायां व्याहरत्युलूकः.'),
    ),
    "4.3.52": (
        _c('naiśaḥ — and the case changes for one rule only',
           {'sense': 'soḍha', 'case': 'prathamā', 'samjna': 'kāla'},
           note='तदस्य सोढम्. सोढं जितमभ्यस्तमित्यर्थः.'),
    ),
    "4.3.53": (
        _c('sraughnaḥ — being, not birth, and the time-heading over',
           {'sense': 'bhava', 'case': 'saptamī'},
           note='तत्र भवः. कालादिति निवृत्तम्. पुनस्तत्रग्रहणं तदस्येति निवृत्त्यर्थम्.'),
    ),
    "4.3.54": (
        _c('diśyam — and two entries read for what is not a body-part',
           {'sense': 'bhava', 'case': 'saptamī', 'gana': 'digādi'},
           note='दिगादिभ्यो यत्. मुखजघनशब्दयोरशरीरावयवार्थः पाठः.'),
    ),
    "4.3.55": (
        _c('dantyam — and the phonetic terms come from this rule',
           {'sense': 'bhava', 'case': 'saptamī', 'samjna': 'śarīra-avayava'},
           note='शरीरावयवाच्च, अणोऽपवादः. शरीरं प्राणिकायः.'),
    ),
    "4.3.56": (
        _c('āheyam — and one base is a stem, not the verb it looks like',
           {'sense': 'bhava', 'case': 'saptamī', 'stem': 'dṛti'},
           note='दृतिकुक्षिकलशिवस्त्यस्त्यहेर्ढञ्. अस्तिशब्दः प्रातिपदिकम्, न तिङन्तम्.'),
    ),
    "4.3.57": (
        _c('graivam — and a plural in the rule explained by anatomy',
           {'sense': 'bhava', 'case': 'saptamī', 'stem': 'grīvā'},
           note='ग्रीवाभ्योऽण् च. ग्रीवाशब्दो धमनीवचनः, तासां बहुत्वाद् बहुवचनं कृतम्.'),
    ),
    "4.3.58": (
        _c('gāmbhīryam — depth, by asking what is in the deep',
           {'sense': 'bhava', 'case': 'saptamī', 'stem': 'gambhīra'},
           note='गम्भीराञ्ञ्यः, अणोऽपवादः. बहिर्देवपञ्चजनेभ्यश्चेति वक्तव्यम्.'),
    ),
    "4.3.59": (
        _c("pārimukhyam — a compound's name qualifying a list",
           {'sense': 'bhava', 'case': 'saptamī', 'samjna': 'avyayībhāva', 'gana': 'parimukhādi'},
           note='अव्ययीभावाच्च. तेषां विशेषणमव्ययीभावग्रहणम्.'),
    ),
    "4.3.60": (
        _c('āntarveśmikam — and thirteen supplements in two verses',
           {'sense': 'bhava', 'case': 'saptamī', 'pre': 'antar', 'samjna': 'avyayībhāva'},
           note='अन्तःपूर्वपदाट् ठञ्. अन्तःशब्दो विभक्त्यर्थे समस्यते.'),
    ),
    "4.3.61": (
        _c('pārigrāmikaḥ — the country round the village',
           {'sense': 'bhava', 'case': 'saptamī', 'pre': 'pari-anu', 'stem_final': 'grāma', 'samjna': 'avyayībhāva'},
           note='ग्रामात् पर्यनुपूर्वात्, अणोऽपवादः.'),
    ),
    "4.3.62": (
        _c('jihvāmūlīyam — the same word names a speech sound',
           {'sense': 'bhava', 'case': 'saptamī', 'stem': 'jihvāmūla'},
           note='जिह्वामूलाङ्गुलेश्छः, यतोऽपवादः.'),
    ),
    "4.3.63": (
        _c('kavargīyam — the rows of the alphabet named',
           {'sense': 'bhava', 'case': 'saptamī', 'stem_final': 'varga'},
           note='वर्गान्ताच्च, अणोऽपवादः.'),
    ),
    "4.3.64": (
        _c('vāsudevavargyaḥ — three forms, but only for a party of men',
           {'sense': 'bhava', 'case': 'saptamī', 'stem_final': 'varga', 'result': 'aśabda'},
           note='अशब्दे यत्खावन्यतरस्याम्. अशब्द इति किम्? कवर्गीयो वर्णः.'),
    ),
    "4.3.65": (
        _c('karṇikā — the ear-ornament',
           {'sense': 'bhava', 'case': 'saptamī', 'stem': 'karṇa', 'result': 'alaṃkāra'},
           note='कर्णललाटात् कनलंकारे, यतोऽपवादः.'),
    ),
    "4.3.66": (
        _c('saupo granthaḥ — a book expounding the endings',
           {'sense': 'vyākhyāna', 'case': 'ṣaṣṭhī', 'samjna': 'vyākhyātavya-nāman'},
           note='तस्य व्याख्यान इति च व्याख्यातव्यनाम्नः. भवव्याख्यानयोर्युगपदधिकारोऽपवादविधानार्थः.'),
    ),
    "4.3.67": (
        _c('ṣātvaṇatvikam — many vowels, and the accent at the end',
           {'sense': 'vyākhyāna', 'samjna': 'vyākhyātavya-nāman', 'vowels': 'bahvac', 'accent': 'antodātta'},
           note='बह्वचोऽन्तोदात्ताट् ठञ्. बह्वच इति किम्? द्व्यचष्ठकं वक्ष्यति.'),
    ),
    "4.3.68": (
        _c('āgniṣṭomikaḥ — and *sacrifice* named for the non-soma rites',
           {'sense': 'vyākhyāna', 'samjna': 'kratu'},
           note='क्रतुयज्ञेभ्यश्च. क्रतुभ्य इत्येव सिद्धे यज्ञग्रहणमसोमयागेभ्योऽपि यथा स्यात्.'),
    ),
    "4.3.69": (
        _c("vāsiṣṭhiko’dhyāyaḥ — a seer's name meaning his book",
           {'sense': 'vyākhyāna', 'samjna': 'ṛṣi', 'result': 'adhyāya'},
           note='अध्यायेष्वेवर्षेः. तत्साहचर्यादृषिशब्दैर्ग्रन्थ उच्यते.'),
    ),
    "4.3.70": (
        _c('pauroḍāśikaḥ — and a silent letter for the feminine',
           {'sense': 'vyākhyāna', 'stem': 'pauroḍāśa'},
           note='पौरोडाशपुरोडाशात् ष्ठन्. षकारो ङीषर्थः.'),
    ),
    "4.3.71": (
        _c('chandasyaḥ — both forms cited from texts',
           {'sense': 'vyākhyāna', 'stem': 'chandas'},
           note='छन्दसो यदणौ. द्व्यच इति ठकि प्राप्ते वचनम्.'),
    ),
    "4.3.72": (
        _c('nāmākhyātikaḥ — nouns, verbs, and both',
           {'sense': 'vyākhyāna', 'samjna': 'vyākhyātavya-nāman', 'vowels': 'dvyac'},
           note='द्व्यजृद्ब्राह्मणर्क्प्रथमाध्वरपुरश्चरणनामाख्याताट् ठक्. नामाख्यातग्रहणं संघातविगृहीतार्थम्.'),
    ),
    "4.3.73": (
        _c('ārgayanaḥ — a list that is a catalogue of the sciences',
           {'sense': 'vyākhyāna', 'gana': 'ṛgayanādi'},
           note='अणृगयनादिभ्यः. अण्ग्रहणं बाधकबाधनार्थम्.'),
    ),
    "4.3.74": (
        _c('sraughnaḥ — come from there, and the ablative meant is the principal one',
           {'sense': 'āgata', 'case': 'pañcamī'},
           note='तत आगतः. तत इति मुख्यमपादानं विवक्षितं यत् तदिह गृह्यते, न नान्तरीयकम्.'),
    ),
    "4.3.75": (
        _c('śaulkaśālikaḥ — from the customs-house',
           {'sense': 'āgata', 'case': 'pañcamī', 'samjna': 'āyasthāna'},
           note='ठगायस्थानेभ्यः. आय इति स्वामिग्राह्यो भाग उच्यते.'),
    ),
    "4.3.76": (
        _c('śauṇḍikaḥ — the default named to beat its beater',
           {'sense': 'āgata', 'case': 'pañcamī', 'gana': 'śuṇḍikādi'},
           note='शुण्डिकादिभ्योऽण्, आयस्थानठकोऽपवादः.'),
    ),
    "4.3.77": (
        _c('aupādhyāyakam — connected by learning or by birth',
           {'sense': 'āgata', 'case': 'pañcamī', 'samjna': 'vidyā-yoni-saṃbandha'},
           note='विद्यायोनिसंबन्धेभ्यो वुञ्, अणोऽपवादः.'),
    ),
    "4.3.78": (
        _c('hautṛkam — and the same relation, from an ṛ-final word',
           {'sense': 'āgata', 'case': 'pañcamī', 'samjna': 'vidyā-yoni-saṃbandha', 'stem_final': 'ṛ'},
           note='ऋतष्ठञ्, वुञोऽपवादः. तपरकरणं मुखसुखार्थम्.'),
    ),
    "4.3.79": (
        _c('pitryam — two affixes where the class rule gave one',
           {'sense': 'āgata', 'case': 'pañcamī', 'stem': 'pitṛ'},
           note='पितुर्यच्च. पितुरागतं पित्र्यम्, पैतृकम्.'),
    ),
    "4.3.80": (
        _c('aupagavakam — affixes borrowed from a rule not yet reached',
           {'sense': 'āgata', 'case': 'pañcamī', 'samjna': 'gotra-pratyayānta'},
           note='गोत्रादङ्कवत्. तस्माद् वुञप्यतिदिश्यते नाणेव.'),
    ),
    "4.3.81": (
        _c('samarūpyam — and *man* named for where he is not the cause',
           {'sense': 'āgata', 'case': 'pañcamī', 'samjna': 'hetu-manuṣya', 'wants': 'rūpya'},
           note='हेतुमनुष्येभ्योऽन्यतरस्यां रूप्यः. मनुष्यग्रहणमहेत्वर्थम्.'),
    ),
    "4.3.82": (
        _c('samamayam — a split made to stop a pairing',
           {'sense': 'āgata', 'case': 'pañcamī', 'samjna': 'hetu-manuṣya', 'wants': 'mayaṭ'},
           note='मयट् च. योगविभागो यथासंख्यनिरासार्थः.'),
    ),
    "4.3.83": (
        _c('haimavatī gaṅgā — the river that rises from the mountain',
           {'sense': 'prabhavati', 'case': 'pañcamī'},
           note='प्रभवति. प्रभवति प्रकाशते, प्रथमत उपलभ्यत इत्यर्थः.'),
    ),
    "4.3.84": (
        _c('vaidūryo maṇiḥ — and a verse offering two ways out',
           {'sense': 'prabhavati', 'case': 'pañcamī', 'stem': 'vidūra'},
           note='विदूराञ्ञ्यः. वालवायो विदूरं च प्रकृत्यन्तरमेव वा.'),
    ),
    "4.3.85": (
        _c('sraughnaḥ panthāḥ — a road that goes because what is on it goes',
           {'sense': 'gacchati', 'case': 'dvitīyā', 'result': 'pathi-dūta'},
           note='तद् गच्छति पथिदूतयोः. तत्स्थेषु गच्छत्सु पन्था गच्छतीत्युच्यते.'),
    ),
    "4.3.86": (
        _c('sraughnaṃ dvāram — an instrument spoken of as an agent',
           {'sense': 'abhiniṣkrāmati', 'case': 'dvitīyā', 'result': 'dvāra'},
           note='अभिनिष्क्रामति द्वारम्. तदिह स्वातन्त्र्येण विवक्ष्यते, तथा साध्वसिश्छिनत्ति.'),
    ),
    "4.3.87": (
        _c('saubhadraḥ — a book about her, and a romance named for her',
           {'sense': 'adhikṛtya-kṛta', 'case': 'dvitīyā', 'result': 'grantha'},
           note='अधिकृत्य कृते ग्रन्थे. लुबाख्यायिकाभ्यः प्रत्ययस्य बहुलम्.'),
    ),
    "4.3.88": (
        _c('vākyapadīyam — a list followed from usage and written nowhere',
           {'sense': 'adhikṛtya-kṛta', 'case': 'dvitīyā', 'gana': 'śiśukrandādi', 'result': 'grantha'},
           note='शिशुक्रन्दयमसभद्वन्द्वेन्द्रजननादिभ्यश्छः. इन्द्रजननादिराकृतिगणः प्रयोगतोऽनुसर्तव्यः, प्रातिपदिकेषु न पठ्यते.'),
    ),
    "4.3.89": (
        _c('sraughnaḥ — where he lives now',
           {'sense': 'nivāsa', 'case': 'prathamā'},
           note='सोऽस्य निवासः. निवसन्त्यस्मिन्निवासो देश उच्यते.'),
    ),
    "4.3.90": (
        _c('sraughnaḥ — and where his forebears lived',
           {'sense': 'abhijana', 'case': 'prathamā'},
           note='अभिजनश्च. यत्र संप्रत्युष्यते स निवासः, यत्र पूर्वैरुषितं सोऽभिजनः.'),
    ),
    "4.3.91": (
        _c('hṛdgolīyāḥ — a mountain, and men who live by arms',
           {'sense': 'abhijana', 'case': 'prathamā', 'samjna': 'parvata', 'result': 'āyudhajīvin'},
           note='आयुधजीविभ्यश्छः पर्वते. आयुधजीविभ्य इति तादर्थ्ये चतुर्थी, पर्वत इति प्रकृतिविशेषणम्.'),
    ),
    "4.3.92": (
        _c('śāṇḍikyaḥ — a list in the same meaning',
           {'sense': 'abhijana', 'case': 'prathamā', 'gana': 'śaṇḍikādi'},
           note='शण्डिकादिभ्यो ञ्यः, अणादेरपवादः.'),
    ),
    "4.3.93": (
        _c('saindhavaḥ — two lists, and the entries kept a rival out',
           {'sense': 'abhijana', 'case': 'prathamā', 'gana': 'sindhvādi'},
           note='सिन्धुतक्षशिलादिभ्योऽणञौ. आदिशब्दः प्रत्येकमभिसंबध्यते.'),
    ),
    "4.3.94": (
        _c('śālāturīyaḥ — the word by which Pāṇini is known',
           {'sense': 'abhijana', 'case': 'prathamā', 'stem': 'śalātura'},
           note='तूदीशलातुरवर्मतीकूचवाराड्ढक्छण्ढञ्यकः, यथासंख्यम्.'),
    ),
    "4.3.95": (
        _c('sraughnaḥ — a one-word rule, everything else carried',
           {'sense': 'bhakti', 'case': 'prathamā'},
           note='भक्तिः. भज्यते सेव्यत इति भक्तिः.'),
    ),
    "4.3.96": (
        _c('āpūpikaḥ — neither sentient, nor a place, nor a time',
           {'sense': 'bhakti', 'case': 'prathamā', 'samjna': 'acitta'},
           note='अचित्तादेशकालाट् ठक्. अचित्तादिति किम्? दैवदत्तः.'),
    ),
    "4.3.97": (
        _c('māhārājikaḥ — an affix chosen for its accent',
           {'sense': 'bhakti', 'case': 'prathamā', 'stem': 'mahārāja'},
           note='महाराजाट् ठञ्. प्रत्ययान्तरकरणं स्वरार्थम्.'),
    ),
    "4.3.98": (
        _c('vāsudevakaḥ — and word order teaching a principle',
           {'sense': 'bhakti', 'case': 'prathamā', 'stem': 'vāsudeva'},
           note='वासुदेवार्जुनाभ्यां वुन्. ज्ञापयति — अभ्यर्हितं पूर्वं निपततीति.'),
    ),
    "4.3.99": (
        _c('glaucukāyanakaḥ — variously, so sometimes not at all',
           {'sense': 'bhakti', 'case': 'prathamā', 'samjna': 'gotra-kṣatriya-ākhyā'},
           note='गोत्रक्षत्रियाख्येभ्यो बहुलं वुञ्. बहुलग्रहणात् क्वचिदप्रवृत्तिरेव.'),
    ),
    "4.3.100": (
        _c('āṅgakaḥ — the rulers treated exactly as the district',
           {'sense': 'bhakti', 'case': 'prathamā', 'samjna': 'janapadin'},
           note='जनपदिनां जनपदवत् सर्वम्. सर्वग्रहणं प्रकृत्यतिदेशार्थम्.'),
    ),
    "4.3.101": (
        _c('māthurī vṛttiḥ — set forth, and not made',
           {'sense': 'prokta', 'case': 'tṛtīyā'},
           note='तेन प्रोक्तम्. प्रकर्षेणोक्तं प्रोक्तमित्युच्यते, न तु कृतम्.'),
    ),
    "4.3.102": (
        _c('taittirīyāḥ — a recension named by its teacher',
           {'sense': 'prokta', 'case': 'tṛtīyā', 'gana': 'tittiryādi'},
           note='तित्तिरिवरतन्तुखण्डिकोखाच्छण्, अणोऽपवादः.'),
    ),
    "4.3.103": (
        _c('kāśyapinaḥ — the seer, not a man of his line today',
           {'sense': 'prokta', 'case': 'tṛtīyā', 'stem': 'kāśyapa', 'samjna': 'ṛṣi'},
           note='काश्यपकौशिकाभ्यामृषिभ्यां णिनिः. ऋषिभ्यामिति किम्? काश्यपीयम्.'),
    ),
    "4.3.104": (
        _c('ālambinaḥ — direct pupils only, proved from the lists',
           {'sense': 'prokta', 'case': 'tṛtīyā', 'samjna': 'vaiśampāyana-antevāsin'},
           note='कलापिवैशंपायनान्तेवासिभ्यश्च. प्रत्यक्षकारिणो गृह्यन्ते, न तु व्यवहिताः शिष्यशिष्याः.'),
    ),
    "4.3.105": (
        _c('bhāllavinaḥ — an ancient sage, by what the tradition says',
           {'sense': 'prokta', 'case': 'tṛtīyā', 'result': 'purāṇa-prokta-brāhmaṇa-kalpa'},
           note='पुराणप्रोक्तेषु ब्राह्मणकल्पेषु. याज्ञवल्क्यादयो ऽचिरकाला इत्याख्यानेषु वार्ता, तया व्यवहरति सूत्रकारः.'),
    ),
    "4.3.106": (
        _c('vājasaneyinaḥ — a school of the Veda named',
           {'sense': 'prokta', 'case': 'tṛtīyā', 'gana': 'śaunakādi', 'usage': 'chandasi'},
           note='शौनकादिभ्यश्छन्दसि, छाणोरपवादः. छन्दसीति किम्? शौनकीया शिक्षा.'),
    ),
    "4.3.107": (
        _c("kaṭhāḥ — the affix gone, and the teacher's own name left",
           {'sense': 'prokta', 'case': 'tṛtīyā', 'stem': 'kaṭha'},
           note='कठचरकाल्लुक्. कठेन प्रोक्तमधीयते कठाः, चरकाः.'),
    ),
    "4.3.108": (
        _c('kālāpāḥ — the default named to give more than it owed',
           {'sense': 'prokta', 'case': 'tṛtīyā', 'stem': 'kalāpin'},
           note='कलापिनोऽण्. अथाण्ग्रहणं किम्? अधिकविधानार्थम्.'),
    ),
    "4.3.109": (
        _c('chāgaleyinaḥ — one pupil of the four',
           {'sense': 'prokta', 'case': 'tṛtīyā', 'stem': 'chagalin'},
           note='छगलिनो ढिनुक्. कलाप्यन्तेवासित्वाद् णिनेरपवादः.'),
    ),
    "4.3.110": (
        _c("pārāśariṇo bhikṣavaḥ — the beggars' aphorisms",
           {'sense': 'prokta', 'case': 'tṛtīyā', 'stem': 'pārāśarya', 'result': 'bhikṣu-naṭa-sūtra'},
           note='पाराशर्यशिलालिभ्यां भिक्षुनटसूत्रयोः. सूत्रशब्दः प्रत्येकमभिसंबध्यते.'),
    ),
    "4.3.111": (
        _c('karmandino bhikṣavaḥ — two more, matched in order',
           {'sense': 'prokta', 'case': 'tṛtīyā', 'stem': 'karmanda', 'result': 'bhikṣu-naṭa-sūtra'},
           note='कर्मन्दकृशाश्वादिनिः, अणोऽपवादः.'),
    ),
    "4.3.112": (
        _c('saudāmanī vidyut — and a word repeated to cancel a heading',
           {'sense': 'ekadik', 'case': 'tṛtīyā'},
           note='तेनैकदिक्. पुनः समर्थविभक्तिग्रहणं छन्दोऽधिकारनिवृत्त्यर्थम्.'),
    ),
    "4.3.113": (
        _c('sudāmataḥ — one more affix, and an indeclinable',
           {'sense': 'ekadik', 'case': 'tṛtīyā', 'wants': 'tasi'},
           note='तसिश्च. स्वरादिपाठादव्ययत्वम्.'),
    ),
    "4.3.114": (
        _c('urasyaḥ — and the chest takes two',
           {'sense': 'ekadik', 'case': 'tṛtīyā', 'stem': 'uras'},
           note='उरसो यच्च, अणोऽपवादः. उरस्यः, उरस्तः.'),
    ),
    "4.3.115": (
        _c('pāṇinīyaṃ vyākaraṇam — worked out without being taught',
           {'sense': 'upajñāta', 'case': 'tṛtīyā'},
           note='उपज्ञाते. विनोपदेशेन ज्ञातमुपज्ञातम्, स्वयमभिसंबुद्धमित्यर्थः.'),
    ),
    "4.3.116": (
        _c('vārarucāḥ ślokāḥ — made, where the last rule was found',
           {'sense': 'kṛta', 'case': 'tṛtīyā', 'result': 'grantha'},
           note='कृते ग्रन्थे. उत्पादितं कृतम्, विद्यमानमेव ज्ञातम् उपज्ञातम्.'),
    ),
    "4.3.117": (
        _c('mākṣikam — four names, and all of them honey',
           {'sense': 'kṛta', 'case': 'tṛtīyā', 'samjna': 'saṃjñā'},
           note='संज्ञायाम्. समुदायेन चेत् संज्ञा ज्ञायते.'),
    ),
    "4.3.118": (
        _c('kaulālakam — a list, with three conditions carried',
           {'sense': 'kṛta', 'case': 'tṛtīyā', 'gana': 'kulālādi', 'samjna': 'saṃjñā'},
           note='कुलालादिभ्यो वुञ्. तेन, कृते, संज्ञायामिति चैतत् सर्वमनुवर्तते.'),
    ),
    "4.3.119": (
        _c('kṣaudram — honey named by the bee that made it',
           {'sense': 'kṛta', 'case': 'tṛtīyā', 'gana': 'kṣudrādi', 'samjna': 'saṃjñā'},
           note='क्षुद्राभ्रमरवटरपादपादञ्. स्वरे विशेषः.'),
    ),
    "4.3.120": (
        _c('aupagavam — the relation, and nothing else, is meant',
           {'sense': 'idam', 'case': 'ṣaṣṭhī'},
           note='तस्येदम्. षष्ठ्यर्थमात्रं तत्संबन्धिमात्रं च विवक्षितम्.'),
    ),
    "4.3.121": (
        _c('rathyam — a part of the chariot, and no more',
           {'sense': 'idam', 'case': 'ṣaṣṭhī', 'stem': 'ratha'},
           note='रथाद् यत्, अणोऽपवादः. रथाङ्ग एवेष्यते नान्यत्र, अनभिधानात्.'),
    ),
    "4.3.122": (
        _c('āśvarathaṃ cakram — a draught animal in front',
           {'sense': 'idam', 'case': 'ṣaṣṭhī', 'stem': 'ratha', 'pre': 'patra'},
           note='पत्रपूर्वादञ्. पतन्ति तेनेति पत्रम्.'),
    ),
    "4.3.123": (
        _c('āśvam — and only of what the animal carries',
           {'sense': 'idam', 'case': 'ṣaṣṭhī', 'samjna': 'patra'},
           note='पत्राध्वर्युपरिषदश्च. पत्राद् वाह्ये.'),
    ),
    "4.3.124": (
        _c('hālikam — what belongs to the plough',
           {'sense': 'idam', 'case': 'ṣaṣṭhī', 'stem': 'hala'},
           note='हलसीराट् ठक्, अणोऽपवादः.'),
    ),
    "4.3.125": (
        _c('kākolūkikā — the feud of the crows and the owls',
           {'sense': 'idam', 'case': 'ṣaṣṭhī', 'samjna': 'dvandva', 'result': 'vaira-maithunika'},
           note='द्वन्द्वाद् वुन् वैरमैथुनिकयोः. वैरस्य नपुंसकत्वेऽप्यमी स्वभावतः स्त्रीलिङ्गाः.'),
    ),
    "4.3.126": (
        _c('aupagavakam — and a school only for its rule of life',
           {'sense': 'idam', 'case': 'ṣaṣṭhī', 'samjna': 'gotra-caraṇa'},
           note='गोत्रचरणाद् वुञ्. चरणाद् धर्माम्नाययोरिष्यते.'),
    ),
    "4.3.127": (
        _c('baido’ṅkaḥ — four senses against three bases',
           {'sense': 'idam', 'case': 'ṣaṣṭhī', 'samjna': 'añ-yañ-iñ-anta'},
           note='संघाङ्कलक्षणेष्वञ्यञिञामण्. तेन वैषम्याद् यथासंख्यं न भवति.'),
    ),
    "4.3.128": (
        _c('śākalaḥ — beside śākalakaḥ, in each of the four',
           {'sense': 'idam', 'case': 'ṣaṣṭhī', 'stem': 'śākala', 'result': 'saṃgha-aṅka-lakṣaṇa-ghoṣa'},
           note='शाकलाद् वा, वुञोऽपवादः.'),
    ),
    "4.3.129": (
        _c('nāṭyam — a restriction carried to a word it cannot fit',
           {'sense': 'idam', 'case': 'ṣaṣṭhī', 'gana': 'chandogādi', 'result': 'dharma-āmnāya'},
           note='छन्दोगौक्थिकयाज्ञिकबह्वृचनटाञ् ञ्यः. तत्साहचर्याद् नटशब्दादपि धर्माम्नाययोरेव भवति.'),
    ),
    "4.3.130": (
        _c('gaukakṣāḥ — refused, and the refusal names its target',
           {'sense': 'idam', 'case': 'ṣaṣṭhī', 'samjna': 'gotra-caraṇa', 'result': 'daṇḍamāṇava-antevāsin'},
           note='न दण्डमाणवान्तेवासिषु. गोत्रग्रहणमिहानुवर्तते, तेन वुञ्प्रतिषेधो विज्ञायते.'),
    ),
    "4.3.131": (
        _c('raivatikīyaḥ — a list that already had its affix',
           {'sense': 'idam', 'case': 'ṣaṣṭhī', 'gana': 'raivatikādi'},
           note='रैवतिकादिभ्यश्छः. गोत्रप्रत्ययान्ता एते.'),
    ),
    "4.3.132": (
        _c('kaupiñjalaḥ — and the heading is why this beats it',
           {'sense': 'idam', 'case': 'ṣaṣṭhī', 'stem': 'kaupiñjala'},
           note='कौपिञ्जलहास्तिपदादण्, गोत्रवुञोऽपवादः, गोत्राधिकारात्.'),
    ),
    "4.3.133": (
        _c('ātharvaṇo dharmaḥ — the affix and a loss in one act',
           {'sense': 'idam', 'case': 'ṣaṣṭhī', 'stem': 'ātharvaṇika'},
           note='आथर्वणिकस्येकलोपश्च, चरणवुञोऽपवादः.'),
    ),
    "4.3.134": (
        _c('āśmanaḥ — and what is left is found by subtraction',
           {'sense': 'vikāra', 'case': 'ṣaṣṭhī'},
           note='तस्य विकारः. अप्राण्याद्युदात्तमवृद्धम्, यस्य च नान्यत् प्रतिपदं विधानम्.'),
    ),
    "4.3.135": (
        _c('kāpotaḥ — two headings at once, in the same words as 4.3.66',
           {'sense': 'avayava', 'case': 'ṣaṣṭhī', 'samjna': 'prāṇi-oṣadhi-vṛkṣa'},
           note='अवयवे च प्राण्योषधिवृक्षेभ्यः. विकारावयवयोर्युगपदधिकारोऽपवादविधानार्थः, कृतनिर्देशौ हि तौ.'),
    ),
    "4.3.136": (
        _c('bailvaḥ — and one entry read to beat a later rule',
           {'sense': 'vikāra', 'case': 'ṣaṣṭhī', 'gana': 'bilvādi'},
           note='बिल्वादिभ्योऽण्. गवेधुकाशब्दोऽत्र पठ्यते, मयड्बाधनार्थं ग्रहणम्.'),
    ),
    "4.3.137": (
        _c('tārkavam — the second-to-last sound, not the last',
           {'sense': 'vikāra', 'case': 'ṣaṣṭhī', 'upadha': 'k'},
           note='कोपधाच्च, अञोऽपवादः.'),
    ),
    "4.3.138": (
        _c('trāpuṣam — an affix and an augment together',
           {'sense': 'vikāra', 'case': 'ṣaṣṭhī', 'stem': 'trapu'},
           note='त्रपुजतुनोः षुक्. अप्राण्यादित्वाद् नावयवे.'),
    ),
    "4.3.139": (
        _c('daivadāravam — a u-final base, but not an unaccented one',
           {'sense': 'vikāra', 'case': 'ṣaṣṭhī', 'stem_final': 'u'},
           note='ओरञ्. अनुदात्तादेरन्यदिहोदाहरणम्.'),
    ),
    "4.3.140": (
        _c('dādhitthaṃ — the first vowel unaccented',
           {'sense': 'vikāra', 'case': 'ṣaṣṭhī', 'accent': 'anudāttādi'},
           note='अनुदात्तादेश्च, अणोऽपवादः.'),
    ),
    "4.3.141": (
        _c('pālāśam — one option denying and granting at once',
           {'sense': 'vikāra', 'case': 'ṣaṣṭhī', 'gana': 'palāśādi'},
           note='पलाशादिभ्यो वा. उभयत्र विभाषेयम्.'),
    ),
    "4.3.142": (
        _c('śāmīlaṃ bhasma — ash of the śamī wood',
           {'sense': 'vikāra', 'case': 'ṣaṣṭhī', 'stem': 'śamī'},
           note='शम्यष्ट्लञ्, अञोऽपवादः.'),
    ),
    "4.3.143": (
        _c('aśmamayam — in the spoken language, and not of food or cloth',
           {'sense': 'vikāra', 'case': 'ṣaṣṭhī', 'usage': 'bhāṣā', 'result': 'abhakṣya-ācchādana'},
           note='मयड्वैतयोर्भाषायामभक्ष्याच्छादनयोः. भाषायामिति किम्? बैल्वः खादिरो वा यूपः.'),
    ),
    "4.3.144": (
        _c('vāṅmayam — always, and that is what makes literature',
           {'sense': 'vikāra', 'case': 'ṣaṣṭhī', 'usage': 'bhāṣā', 'samjna': 'vṛddha', 'result': 'abhakṣya-ācchādana'},
           note='नित्यं वृद्धशरादिभ्यः. एकाचो नित्यं मयटमिच्छन्ति, तदनेन क्रियते.'),
    ),
    "4.3.145": (
        _c('gomayam — neither a modification nor a part',
           {'sense': 'idam', 'case': 'ṣaṣṭhī', 'stem': 'go', 'result': 'purīṣa'},
           note='गोश्च पुरीषे. पुरीषं न विकारो नाप्यवयवः, तस्येदंविषये विधानम्.'),
    ),
    "4.3.146": (
        _c('piṣṭamayaṃ bhasma — fixed here, optional three rules back',
           {'sense': 'vikāra', 'case': 'ṣaṣṭhī', 'stem': 'piṣṭa', 'wants': 'mayaṭ'},
           note='पिष्टाच्च, अणोऽपवादः.'),
    ),
    "4.3.147": (
        _c('piṣṭakaḥ — a cake, where the word is a name',
           {'sense': 'vikāra', 'case': 'ṣaṣṭhī', 'stem': 'piṣṭa', 'samjna': 'saṃjñā'},
           note='संज्ञायां कन्, मयटोऽपवादः.'),
    ),
    "4.3.148": (
        _c('vrīhimayaḥ puroḍāśaḥ — the sacrificial cake of rice',
           {'sense': 'vikāra', 'case': 'ṣaṣṭhī', 'stem': 'vrīhi', 'result': 'puroḍāśa'},
           note='व्रीहेः पुरोडाशे. व्रैहमन्यत्.'),
    ),
    "4.3.149": (
        _c('tilamayam — and not where the result is a name',
           {'sense': 'vikāra', 'case': 'ṣaṣṭhī', 'stem': 'tila'},
           note='असंज्ञायां तिलयवाभ्याम्. असंज्ञायामिति किम्? तैलम्.'),
    ),
    "4.3.150": (
        _c('parṇamayī juhūḥ — supplying in the Veda what the spoken rule missed',
           {'sense': 'vikāra', 'case': 'ṣaṣṭhī', 'vowels': 'dvyac', 'usage': 'chandasi'},
           note='द्व्यचश्छन्दसि. भाषायां मयडुक्तः, छन्दस्यप्राप्तो विधीयते.'),
    ),
    "4.3.151": (
        _c('mauñjaṃ śikyam — refused, and *having* is not *ending in*',
           {'sense': 'vikāra', 'case': 'ṣaṣṭhī', 'samjna': 'utvat', 'vowels': 'dvyac', 'usage': 'chandasi'},
           note='नोत्वद्वर्ध्रबिल्वात्. मतुब्निर्देशस्तदन्तविधिनिरासार्थः.'),
    ),
    "4.3.152": (
        _c('tālaṃ dhanuḥ — and a supplement confines it to a bow',
           {'sense': 'vikāra', 'case': 'ṣaṣṭhī', 'gana': 'tālādi'},
           note='तालादिभ्योऽण्. तालाद् धनुषि.'),
    ),
    "4.3.153": (
        _c('hāṭako niṣkaḥ — gold, and only as a measure',
           {'sense': 'vikāra', 'case': 'ṣaṣṭhī', 'samjna': 'jātarūpa', 'result': 'parimāṇa'},
           note='जातरूपेभ्यः परिमाणे. परिमाण इति किम्? यष्टिरियं हाटकमयी.'),
    ),
    "4.3.154": (
        _c('kāpotam — the affix promised nineteen rules back',
           {'sense': 'vikāra', 'case': 'ṣaṣṭhī', 'samjna': 'prāṇin'},
           note='प्राणिरजतादिभ्योऽञ्, अणादीनामपवादः.'),
    ),
    "4.3.155": (
        _c('daivadāravam — and the six rules are named by number',
           {'sense': 'vikāra', 'case': 'ṣaṣṭhī', 'samjna': 'ñit-pratyayānta'},
           note='ञितश्च तत्प्रत्ययात्. ञित इति किम्? बैल्वमयम्.'),
    ),
    "4.3.156": (
        _c('naiṣkikaḥ — borrowed from a quarter not yet reached',
           {'sense': 'vikāra', 'case': 'ṣaṣṭhī', 'samjna': 'parimāṇa'},
           note='क्रीतवत् परिमाणात्. वतिः सर्वसादृश्यार्थः.'),
    ),
    "4.3.157": (
        _c('auṣṭrakaḥ — one of the six ñ-marked affixes',
           {'sense': 'vikāra', 'case': 'ṣaṣṭhī', 'stem': 'uṣṭra'},
           note='उष्ट्राद् वुञ्, प्राण्यञोऽपवादः.'),
    ),
    "4.3.158": (
        _c('aumakam — beside aumam, from flax',
           {'sense': 'vikāra', 'case': 'ṣaṣṭhī', 'stem': 'umā'},
           note='उमोर्णयोर्वा.'),
    ),
    "4.3.159": (
        _c('aiṇeyaṃ māṃsam — one affix for the doe, another for the buck',
           {'sense': 'vikāra', 'case': 'ṣaṣṭhī', 'stem': 'eṇī'},
           note='एण्या ढञ्. पुंसस्त्वञेव भवति, ऐणम्.'),
    ),
    "4.3.160": (
        _c('gavyam — the rule 4.3.145 named',
           {'sense': 'vikāra', 'case': 'ṣaṣṭhī', 'stem': 'go'},
           note='गोपयसोर्यत्.'),
    ),
    "4.3.161": (
        _c('dravyam — matter, from what wood is turned into',
           {'sense': 'vikāra', 'case': 'ṣaṣṭhī', 'stem': 'dru'},
           note='द्रोश्च, ओरञोऽपवादः.'),
    ),
    "4.3.162": (
        _c('druvayam — a wooden measure',
           {'sense': 'vikāra', 'case': 'ṣaṣṭhī', 'stem': 'dru', 'result': 'māna'},
           note='माने वयः, यतोऽपवादः.'),
    ),
    "4.3.163": (
        _c('āmalakam — a fruit is a part and a modification at once',
           {'sense': 'vikāra', 'case': 'ṣaṣṭhī', 'result': 'phala', 'elided': True},
           note='फले लुक्. फलितस्य वृक्षस्य फलमवयवो भवति विकारश्च, पल्लवितस्येव पल्लवः.'),
    ),
    "4.3.164": (
        _c('plākṣam — and the elision cannot touch it',
           {'sense': 'vikāra', 'case': 'ṣaṣṭhī', 'gana': 'plakṣādi', 'result': 'phala'},
           note='प्लक्षादिभ्योऽण्. विधानसामर्थ्यात् तस्य न लुग् भवति.'),
    ),
    "4.3.165": (
        _c("jāmbavāni phalāni — the option's other side does elide",
           {'sense': 'vikāra', 'case': 'ṣaṣṭhī', 'stem': 'jambū', 'result': 'phala'},
           note='जम्ब्वा वा. अत्राणो विधानसामर्थ्याल् लुग् न भवति, अञस्तु भवत्येव.'),
    ),
    "4.3.166": (
        _c('jambūḥ phalam — a different removal, and it keeps the gender',
           {'sense': 'vikāra', 'case': 'ṣaṣṭhī', 'stem': 'jambū', 'result': 'phala', 'elided': True},
           note='लुप् च. युक्तवद्भावे विशेषः.'),
    ),
    "4.3.167": (
        _c('harītakyaḥ — gender from the tree, number from the fruits',
           {'sense': 'vikāra', 'case': 'ṣaṣṭhī', 'gana': 'harītakyādi', 'result': 'phala', 'elided': True},
           note='हरीतक्यादिभ्यश्च. अत्र च व्यक्तिर्युक्तवद्भावेनेष्यते, वचनं त्वभिधेयवदेव भवति.'),
    ),
    "4.3.168": (
        _c('kāṃsyaḥ — the affix that made the base removed as the new one comes',
           {'sense': 'vikāra', 'case': 'ṣaṣṭhī', 'stem': 'kaṃsīya', 'elided': True},
           note='कंसीयपरशव्ययोर्यञञौ लुक् च. नैतदस्ति; ईतीति तत्र वर्तते.'),
    ),
    "4.4.1": (
        _c('ākṣikaḥ — the heading, and where the affix runs',
           {'case': 'tṛtīyā'},
           note='प्राग्वहतेष्ठक्. प्रागेतस्माद् वहतिसंशब्दनात्, ठक् प्रत्ययस्तेष्वधिकृतो वेदितव्यः.'),
    ),
    "4.4.2": (
        _c('ākṣikaḥ — a dicer, and the affix names the means',
           {'case': 'tṛtīyā', 'sense': 'dīvyati'},
           note='तेन दीव्यति खनति जयति जितम्. क्रियाप्रधानत्वेऽपि चाख्यातस्य तद्धितः स्वभावात् साधनप्रधानः.'),
    ),
    "4.4.3": (
        _c('dādhikam — a refinement of what already exists',
           {'case': 'tṛtīyā', 'sense': 'saṃskṛta'},
           note='संस्कृतम्. सत उत्कर्षाधानं संस्कारः.'),
    ),
    "4.4.4": (
        _c('kaulattham — and a rule on the penultimate again',
           {'case': 'tṛtīyā', 'sense': 'saṃskṛta', 'stem': 'kulattha', 'wants': 'aṇ'},
           note='कुलत्थकोपधादण्, ठकोऽपवादः.'),
    ),
    "4.4.5": (
        _c('kāṇḍaplavikaḥ — one who crosses by a raft',
           {'case': 'tṛtīyā', 'sense': 'tarati'},
           note='तरति. तरति प्लवत इत्यर्थः.'),
    ),
    "4.4.6": (
        _c('gaupucchikaḥ — differing from the heading in the accent',
           {'case': 'tṛtīyā', 'sense': 'tarati', 'stem': 'gopuccha'},
           note='गोपुच्छाट् ठञ्, ठकोऽपवादः. स्वरे विशेषः.'),
    ),
    "4.4.7": (
        _c('nāvikaḥ — a sailor, and a verse that corrects its own count',
           {'case': 'tṛtīyā', 'sense': 'tarati', 'stem': 'nau'},
           note='नौद्व्यचष्ठन्. विधिवाक्यापेक्षं च षट्त्वम्, प्रत्ययास्तु सप्त.'),
    ),
    "4.4.8": (
        _c('dādhikaḥ — the verb covers eating and going alike',
           {'case': 'tṛtīyā', 'sense': 'carati'},
           note='चरति. चरतिर्भक्षणे गतौ च वर्तते.'),
    ),
    "4.4.9": (
        _c('ākarṣikaḥ — the man who goes about with a touchstone',
           {'case': 'tṛtīyā', 'sense': 'carati', 'stem': 'ākarṣa'},
           note='आकर्षात् ष्ठल्. आकर्ष इति सुवर्णपरीक्षार्थो निकषोपल उच्यते.'),
    ),
    "4.4.10": (
        _c('parpikaḥ — silent letters for the accent and the feminine',
           {'case': 'tṛtīyā', 'sense': 'carati', 'gana': 'parpādi'},
           note='पर्पादिभ्यः ष्ठन्. नकारः स्वरार्थः, षकारो ङीषर्थः.'),
    ),
    "4.4.11": (
        _c('śvāgaṇikaḥ — and a vārttika three chapters away',
           {'case': 'tṛtīyā', 'sense': 'carati', 'stem': 'śvagaṇa'},
           note='श्वगणाट् ठञ् च. इकारादिग्रहणं च कर्तव्यं श्वागणिकाद्यर्थम्.'),
    ),
    "4.4.12": (
        _c('vaitanikaḥ karmakaraḥ — one who lives by his wage',
           {'case': 'tṛtīyā', 'sense': 'jīvati', 'gana': 'vetanādi'},
           note='वेतनादिभ्यो जीवति. धनुर्दण्डग्रहणमत्र संघातविगृहीतार्थम्.'),
    ),
    "4.4.13": (
        _c('vasnikaḥ — and one entry read as compound and parts',
           {'case': 'tṛtīyā', 'sense': 'jīvati', 'stem': 'vasna'},
           note='वस्नक्रयविक्रयाट् ठन्. क्रयविक्रयग्रहणं संघातविगृहीतार्थम्.'),
    ),
    "4.4.14": (
        _c('āyudhīyaḥ — and āyudhikaḥ beside it',
           {'case': 'tṛtīyā', 'sense': 'jīvati', 'stem': 'āyudha'},
           note='आयुधाच्छ च.'),
    ),
    "4.4.15": (
        _c('autsaṅgikaḥ — one who carries in his lap',
           {'case': 'tṛtīyā', 'sense': 'harati', 'gana': 'utsaṅgādi'},
           note='हरत्युत्सङ्गादिभ्यः. हरतिर्देशान्तरप्रापणे वर्तते.'),
    ),
    "4.4.16": (
        _c('bhastrikaḥ — one who carries in a leather bag',
           {'case': 'tṛtīyā', 'sense': 'harati', 'gana': 'bhastrādi'},
           note='भस्त्रादिभ्यः ष्ठन्.'),
    ),
    "4.4.17": (
        _c("vivadhikaḥ — and the heading's affix on the other side",
           {'case': 'tṛtīyā', 'sense': 'harati', 'stem': 'vivadha'},
           note='विभाषा विवधवीवधात्. तेन मुक्ते प्रकृतष्ठग् भवति.'),
    ),
    "4.4.18": (
        _c('kauṭiliko mṛgaḥ — and the smith, from one word',
           {'case': 'tṛtīyā', 'sense': 'harati', 'stem': 'kuṭilikā'},
           note='अण् कुटिलिकायाः. कुटिलिका वक्रगतिः, कर्माराणामायुधकर्षणी लोहमयी यष्टिश्चोच्यते.'),
    ),
    "4.4.19": (
        _c('ākṣadyūtikaṃ vairam — a feud caused by dice',
           {'case': 'tṛtīyā', 'sense': 'nirvṛtta', 'gana': 'akṣadyūtādi'},
           note='निर्वृत्तेऽक्षद्यूतादिभ्यः.'),
    ),
    "4.4.20": (
        _c('kṛtrimam — and the base may never stand without it',
           {'case': 'tṛtīyā', 'sense': 'nirvṛtta', 'samjna': 'ktri-anta'},
           note='क्त्रेर्मम् नित्यम्. नित्यग्रहणं स्वातन्त्र्यनिवृत्त्यर्थम्.'),
    ),
    "4.4.21": (
        _c('āpamityakam — brought about by borrowing',
           {'case': 'tṛtīyā', 'sense': 'nirvṛtta', 'stem': 'apamitya'},
           note='अपमित्ययाचिताभ्यां कक्कनौ, यथासंख्यम्.'),
    ),
    "4.4.22": (
        _c('dādhikam — mixed, and no longer separable',
           {'case': 'tṛtīyā', 'sense': 'saṃsṛṣṭa'},
           note='संसृष्टे. संसृष्टमेकीभूतमभिन्नमित्यर्थः.'),
    ),
    "4.4.23": (
        _c('cūrṇino’pūpāḥ — cakes mixed with powder',
           {'case': 'tṛtīyā', 'sense': 'saṃsṛṣṭa', 'stem': 'cūrṇa'},
           note='चूर्णादिनिः, ठकोऽपवादः.'),
    ),
    "4.4.24": (
        _c('lavaṇaḥ sūpaḥ — the affix gone, and only for one sense of the word',
           {'case': 'tṛtīyā', 'sense': 'saṃsṛṣṭa', 'stem': 'lavaṇa', 'elided': True},
           note='लवणाल्लुक्. द्रव्यवाची लवणशब्दो लुकं प्रयोजयति, न गुणवाची.'),
    ),
    "4.4.25": (
        _c('maudga odanaḥ — rice mixed with beans',
           {'case': 'tṛtīyā', 'sense': 'saṃsṛṣṭa', 'stem': 'mudga'},
           note='मुद्गादण्, ठकोऽपवादः.'),
    ),
    "4.4.26": (
        _c('dādhikam — sprinkled, and only with a seasoning',
           {'case': 'tṛtīyā', 'sense': 'upasikta', 'samjna': 'vyañjana'},
           note='व्यञ्जनैरुपसिक्ते. व्यञ्जनैरिति किम्? उदकेनोपसिक्त ओदनः.'),
    ),
    "4.4.27": (
        _c('aujasikaḥ śūraḥ — a hero named by his strength',
           {'case': 'tṛtīyā', 'sense': 'vartate', 'stem': 'ojas'},
           note='ओजःसहोऽम्भसा वर्तते.'),
    ),
    "4.4.28": (
        _c('prātīpikaḥ — and an intransitive verb given an object',
           {'case': 'dvitīyā', 'sense': 'vartate', 'stem': 'īpa', 'pre': 'prati-anu'},
           note='तत् प्रत्यनुपूर्वमीपलोमकूलम्. क्रियाविशेषणमकर्मकाणामपि कर्म भवति.'),
    ),
    "4.4.29": (
        _c('pārimukhikaḥ — and the conjunction gathers what is unsaid',
           {'case': 'dvitīyā', 'sense': 'vartate', 'stem': 'parimukha'},
           note='परिमुखं च. चकारोऽनुक्तसमुच्चयार्थः.'),
    ),
    "4.4.30": (
        _c('dvaiguṇikaḥ — the usurer, and not the debtor',
           {'case': 'dvitīyā', 'sense': 'prayacchati', 'result': 'garhya'},
           note='प्रयच्छति गर्ह्यम्. गर्ह्यमिति किम्? द्विगुणं प्रयच्छत्यधमर्णः.'),
    ),
    "4.4.31": (
        _c('kusīdikaḥ — and this is the rule that made the count seven',
           {'case': 'dvitīyā', 'sense': 'prayacchati', 'result': 'garhya', 'stem': 'kusīda'},
           note='कुसीददशैकादशात् ष्ठन्ष्ठचौ, यथासंख्यम्. विधिवाक्यापेक्षं च षट्त्वम्, प्रत्ययास्तु सप्त.'),
    ),
    "4.4.32": (
        _c('bādarikaḥ — picking up the fallen grains one by one',
           {'case': 'dvitīyā', 'sense': 'uñchati'},
           note='उञ्छति. भूमौ पतितस्यैकैकस्य कणस्योपादानमुञ्छः.'),
    ),
    "4.4.33": (
        _c('sāmājikaḥ — one who keeps order at an assembly',
           {'case': 'dvitīyā', 'sense': 'rakṣati'},
           note='रक्षति. समाजं रक्षति सामाजिकः.'),
    ),
    "4.4.34": (
        _c('śābdiko vaiyākaraṇaḥ — the grammar naming its own practitioner',
           {'case': 'dvitīyā', 'sense': 'karoti', 'stem': 'śabda'},
           note='शब्ददर्दुरं करोति. शब्दं करोति शाब्दिको वैयाकरणः.'),
    ),
    "4.4.35": (
        _c('pākṣikaḥ — and the name reaches synonyms and species',
           {'case': 'dvitīyā', 'sense': 'hanti', 'stem': 'pakṣin'},
           note='पक्षिमत्स्यमृगान् हन्ति. स्वरूपस्य पर्यायाणां तद्विशेषाणां च ग्रहणमिहेष्यते.'),
    ),
    "4.4.36": (
        _c('pāripanthikaś cauraḥ — and a conjunction out of place',
           {'case': 'dvitīyā', 'sense': 'tiṣṭhati', 'stem': 'paripantha'},
           note='परिपन्थं च तिष्ठति. चकारो भिन्नक्रमः प्रत्ययार्थं समुच्चिनोति.'),
    ),
    "4.4.37": (
        _c('dāṇḍamāthikaḥ — and māṭha is another word for a road',
           {'case': 'dvitīyā', 'sense': 'dhāvati', 'stem_final': 'mātha'},
           note='माथोत्तरपदपदव्यनुपदं धावति. माथशब्दः पथिपर्यायः.'),
    ),
    "4.4.38": (
        _c('ākrandikaḥ — a base read two ways and both kept',
           {'case': 'dvitīyā', 'sense': 'dhāvati', 'stem': 'ākranda'},
           note='आक्रन्दाट् ठञ् च. विशेषाभावाद् द्वयोरपि ग्रहणम्.'),
    ),
    "4.4.39": (
        _c('paurvapadikaḥ — and *last member* keeps a prefix out',
           {'case': 'dvitīyā', 'sense': 'gṛhṇāti', 'stem_final': 'pada'},
           note='पदोत्तरपदं गृह्णाति. पदान्तादिति नोक्तम् — बहुच्पूर्वान् मा भूदिति.'),
    ),
    "4.4.40": (
        _c('prātikaṇṭhikaḥ — one who learns by heart',
           {'case': 'dvitīyā', 'sense': 'gṛhṇāti', 'stem': 'pratikaṇṭha'},
           note='प्रतिकण्ठार्थललामं च.'),
    ),
    "4.4.41": (
        _c('dhārmikaḥ — habitual practice, not one performance',
           {'case': 'dvitīyā', 'sense': 'carati', 'stem': 'dharma'},
           note='धर्मं चरति. चरतिरासेवायां नानुष्ठानमात्रे.'),
    ),
    "4.4.42": (
        _c('pratipathikaḥ — and prātipathikaḥ beside it',
           {'case': 'dvitīyā', 'sense': 'eti', 'stem': 'pratipatha'},
           note='प्रतिपथमेति ठंश्च.'),
    ),
    "4.4.43": (
        _c('sāmavāyikaḥ — a gathering, and not a deliberation',
           {'case': 'dvitīyā', 'sense': 'samavaiti', 'samjna': 'samavāya'},
           note='समवायान् समवैति. समवायः समूह उच्यते, न संप्रधारणा.'),
    ),
    "4.4.44": (
        _c('pāriṣadyaḥ — one who attends an assembly',
           {'case': 'dvitīyā', 'sense': 'samavaiti', 'stem': 'pariṣad'},
           note='परिषदो ण्यः, ठकोऽपवादः.'),
    ),
    "4.4.45": (
        _c('sainyaḥ — and sainikaḥ, one by each side of the option',
           {'case': 'dvitīyā', 'sense': 'samavaiti', 'stem': 'senā'},
           note='सेनाया वा. पक्षे सोऽपि भवति.'),
    ),
    "4.4.46": (
        _c('lālāṭikaḥ sevakaḥ — the servant who keeps his distance',
           {'case': 'dvitīyā', 'sense': 'paśyati', 'stem': 'lalāṭa', 'result': 'saṃjñā'},
           note='संज्ञायां ललाटकुक्कुट्यौ पश्यति. सर्वावयवेभ्यो ललाटं दूरे दृश्यते.'),
    ),
    "4.4.47": (
        _c("śaulkaśālikam — the customs-house's due",
           {'case': 'ṣaṣṭhī', 'sense': 'dharmya'},
           note='तस्य धर्म्यम्. धर्म्यं न्याय्यम्, आचारयुक्तमित्यर्थः.'),
    ),
    "4.4.48": (
        _c('māhiṣam — what is due to the chief queen',
           {'case': 'ṣaṣṭhī', 'sense': 'dharmya', 'gana': 'mahiṣyādi'},
           note='अण् महिष्यादिभ्यः, ठकोऽपवादः.'),
    ),
    "4.4.49": (
        _c('pautram — and a supplement makes the word for a woman',
           {'case': 'ṣaṣṭhī', 'sense': 'dharmya', 'stem_final': 'ṛ'},
           note='ऋतोऽञ्. नराच्चेति वक्तव्यम् — नरस्य धर्म्या नारी.'),
    ),
    "4.4.50": (
        _c('śaulkaśālikaḥ — rent, which is not the same as what is due',
           {'case': 'ṣaṣṭhī', 'sense': 'avakraya'},
           note='अवक्रयः. लोकपीडया धर्मातिक्रमेणाप्यवक्रयो भवति.'),
    ),
    "4.4.51": (
        _c('āpūpikaḥ — and the qualifier absorbed into the word',
           {'case': 'prathamā', 'sense': 'paṇya'},
           note='तदस्य पण्यम्. पण्यमिति विशेषणं तद्धितवृत्तावन्तर्भूतम्, अतः पण्यशब्दो न प्रयुज्यते.'),
    ),
    "4.4.52": (
        _c('lāvaṇikaḥ — the salt-merchant',
           {'case': 'prathamā', 'sense': 'paṇya', 'stem': 'lavaṇa'},
           note='लवणाट् ठञ्, ठकोऽपवादः. स्वरे विशेषः.'),
    ),
    "4.4.53": (
        _c('kiśarikaḥ — a list of perfumes',
           {'case': 'prathamā', 'sense': 'paṇya', 'gana': 'kiśarādi'},
           note='किशरादिभ्यः ष्ठन्. किशरादयो गन्धविशेषवचनाः.'),
    ),
    "4.4.54": (
        _c('śalālukaḥ — and śālālukaḥ by the option',
           {'case': 'prathamā', 'sense': 'paṇya', 'stem': 'śalālu'},
           note='शलालुनोऽन्यतरस्याम्. पक्षे सोऽपि भवति.'),
    ),
    "4.4.55": (
        _c("mārdaṅgikaḥ — and the drum's name stands for the playing",
           {'case': 'prathamā', 'sense': 'śilpa'},
           note='शिल्पम्. मृदङ्गवादने वर्तमानो मृदङ्गशब्दः प्रत्ययमुत्पादयति.'),
    ),
    "4.4.56": (
        _c('māḍḍukaḥ — two more drums, two forms each',
           {'case': 'prathamā', 'sense': 'śilpa', 'stem': 'maḍḍuka'},
           note='मड्डुकझर्झरादण् अन्यतरस्याम्, ठकोऽपवादः.'),
    ),
    "4.4.57": (
        _c('āsikaḥ — and dhānuṣkaḥ, which another rule made otherwise',
           {'case': 'prathamā', 'sense': 'praharaṇa'},
           note='प्रहरणम्. असिः प्रहरणमस्य आसिकः. धानुष्कः.'),
    ),
    "4.4.58": (
        _c('pāraśvadhikaḥ — an axeman',
           {'case': 'prathamā', 'sense': 'praharaṇa', 'stem': 'paraśvadha'},
           note='परश्वधाट् ठञ् च. स्वरे विशेषः.'),
    ),
    "4.4.59": (
        _c('śāktīkaḥ, yāṣṭīkaḥ — the spearman and the staff-fighter',
           {'case': 'prathamā', 'sense': 'praharaṇa', 'stem': 'śakti'},
           note='शक्तियष्ट्योरीकक्, ठकोऽपवादः.'),
    ),
    "4.4.60": (
        _c('āstikaḥ — a conviction, and not merely an opinion',
           {'case': 'prathamā', 'sense': 'mati', 'stem': 'asti'},
           note='अस्तिनास्तिदिष्टं मतिः. न च मतिसत्तामात्रे प्रत्यय इष्यते.'),
    ),
    "4.4.61": (
        _c('āpūpikaḥ — a habit, and a habit is a nature',
           {'case': 'prathamā', 'sense': 'śīla'},
           note='शीलम्. शीलं स्वभावः.'),
    ),
    "4.4.62": (
        _c("chātraḥ — the pupil who covers his teacher's faults",
           {'case': 'prathamā', 'sense': 'śīla', 'gana': 'chatrādi'},
           note='छत्रादिभ्यो णः. गुरुकार्येष्ववहितस्तच्छिद्रावरणप्रवृत्तश्छत्रशीलः शिष्यश्छात्रः.'),
    ),
    "4.4.63": (
        _c('aikānyikaḥ — one slip in the recitation',
           {'case': 'prathamā', 'sense': 'karma-adhyayane-vṛtta'},
           note='कर्माध्ययने वृत्तम्. यस्याध्ययनप्रयुक्तस्य परीक्षाकाले पठतः स्खलितमपपाठरूपमेकं जातम्.'),
    ),
    "4.4.64": (
        _c('caturdaśānyikaḥ — fourteen of them',
           {'case': 'prathamā', 'sense': 'karma-adhyayane-vṛtta', 'pre': 'bahvac'},
           note='बह्वच्पूर्वपदाट् ठच्. उदात्ते कर्तव्ये योऽनुदात्तं करोति, स उच्यतेऽन्यत् त्वं करोषीति.'),
    ),
    "4.4.65": (
        _c('āpūpikaḥ — and the construction turns the case',
           {'case': 'prathamā', 'sense': 'hita', 'result': 'bhakṣa'},
           note='हितं भक्षाः. एवं तर्हि सामर्थ्याद् विभक्तिविपरिणामो भविष्यति.'),
    ),
    "4.4.66": (
        _c('āgrabhojanikaḥ — given by appointment, without fail',
           {'case': 'prathamā', 'sense': 'dīyate-niyukta'},
           note='तदस्मै दीयते नियुक्तम्. नियोगेनाव्यभिचारेण दीयते इत्यर्थः.'),
    ),
    "4.4.67": (
        _c('śrāṇikaḥ — and the strengthening is what tells them apart',
           {'case': 'prathamā', 'sense': 'dīyate-niyukta', 'stem': 'śrāṇā'},
           note='श्राणामांसौदनाट् टिठन्. तत्र वृद्ध्यभावो विशेषः.'),
    ),
    "4.4.68": (
        _c('bhāktaḥ — and bhāktikaḥ by the option',
           {'case': 'prathamā', 'sense': 'dīyate-niyukta', 'stem': 'bhakta'},
           note='भक्तादण् अन्यतरस्याम्, ठकोऽपवादः.'),
    ),
    "4.4.69": (
        _c('dauvārikaḥ — the same bases in a third sense',
           {'case': 'saptamī', 'sense': 'niyukta'},
           note='तत्र नियुक्तः. नियुक्तोऽधिकृतो व्यापारित इत्यर्थः.'),
    ),
    "4.4.70": (
        _c('bhāṇḍāgārikaḥ — the storekeeper',
           {'case': 'saptamī', 'sense': 'niyukta', 'stem_final': 'agāra'},
           note='अगारान्ताट् ठन्, ठकोऽपवादः.'),
    ),
    "4.4.71": (
        _c("śmāśānikaḥ — a rule grounded in another text's prohibition",
           {'case': 'saptamī', 'sense': 'adhyāyin', 'samjna': 'adeśa-akāla'},
           note='अध्यायिन्यदेशकालात्. अध्ययनस्य यौ देशकालौ शास्त्रेण प्रतिषिद्धौ तावदेशकालशब्देनोच्येते.'),
    ),
    "4.4.72": (
        _c('vāṃśakaṭhinikaḥ — the acrobat on the bamboo frame',
           {'case': 'saptamī', 'sense': 'vyavaharati', 'stem_final': 'kaṭhina'},
           note='कठिनान्तप्रस्तारसंस्थानेषु व्यवहरति. व्यवहारः क्रियातत्त्वम्.'),
    ),
    "4.4.73": (
        _c('naikaṭiko bhikṣuḥ — a krośa from the village, by rule',
           {'case': 'saptamī', 'sense': 'vasati', 'stem': 'nikaṭa'},
           note='निकटे वसति. आरण्यकेन भिक्षुणा ग्रामात् क्रोशे वस्तव्यमिति शास्त्रम्.'),
    ),
    "4.4.74": (
        _c('āvasathikaḥ — the sixth of the six, and the heading closes',
           {'case': 'saptamī', 'sense': 'vasati', 'stem': 'āvasatha'},
           note='आवसथात् ष्ठल्. ठकः पूर्णोऽवधिः, अतः परमन्यः प्रत्ययो विधीयते.'),
    ),
    "4.4.75": (
        _c('rathyaḥ — a second heading, reaching into the next chapter',
           {'wants': 'yat'},
           note='प्राग्घिताद् यत्. प्रागेतस्माद् हितसंशब्दनाद् यानित ऊर्ध्वमनुक्रमिष्यामः.'),
    ),
    "4.4.76": (
        _c('rathyaḥ — the boundary-post rule, governed by the other heading',
           {'case': 'dvitīyā', 'sense': 'vahati', 'stem': 'ratha'},
           note='तद्वहति रथयुगप्रासङ्गम्. रथं वहति रथ्यः.'),
    ),
    "4.4.77": (
        _c('dhuryaḥ, dhaureyaḥ — both still words for a leader',
           {'case': 'dvitīyā', 'sense': 'vahati', 'stem': 'dhur'},
           note='धुरो यड्ढकौ.'),
    ),
    "4.4.78": (
        _c('sarvadhurīṇaḥ — and the rule split to gather two more',
           {'case': 'dvitīyā', 'sense': 'vahati', 'stem': 'sarvadhurā'},
           note='खः सर्वधुरात्. ख इति योगविभागः कर्तव्य इष्टसंग्रहार्थः.'),
    ),
    "4.4.79": (
        _c('ekadhurīṇaḥ — and ekadhuraḥ, the affix removed',
           {'case': 'dvitīyā', 'sense': 'vahati', 'stem': 'ekadhurā', 'elided': True},
           note='एकधुराल्लुक् च. वचनसामर्थ्यात् पक्षे लुग् विधीयते.'),
    ),
    "4.4.80": (
        _c('śākaṭo gauḥ — the ox that draws a cart',
           {'case': 'dvitīyā', 'sense': 'vahati', 'stem': 'śakaṭa'},
           note='शकटादण्.'),
    ),
    "4.4.81": (
        _c('hālikaḥ — the same affix as a rule a pāda back, in another sense',
           {'case': 'dvitīyā', 'sense': 'vahati', 'stem': 'hala'},
           note='हलसीराट् ठक्. हलं वहति हालिकः.'),
    ),
    "4.4.82": (
        _c('janyā — the one who brings the bride to him',
           {'case': 'dvitīyā', 'sense': 'vahati', 'stem': 'janī', 'result': 'saṃjñā'},
           note='संज्ञायां जन्याः. जनी वधूरुच्यते.'),
    ),
    "4.4.83": (
        _c('padyāḥ śarkarāḥ — and the exclusion moved to the act',
           {'case': 'dvitīyā', 'sense': 'vidhyati', 'result': 'adhanuṣā'},
           note='विध्यत्यधनुषा. धनुष्प्रतिषेधेन व्यधनक्रिया विशेष्यते.'),
    ),
    "4.4.84": (
        _c('dhanyaḥ — and the agent-noun is why an accusative fits',
           {'case': 'dvitīyā', 'sense': 'labdhā', 'stem': 'dhana'},
           note='धनगणं लब्धा. लब्धेति तृन्नन्तम्.'),
    ),
    "4.4.85": (
        _c('ānnaḥ — one who gets food',
           {'case': 'dvitīyā', 'sense': 'labdhā', 'stem': 'anna'},
           note='अन्नाण्णः.'),
    ),
    "4.4.86": (
        _c("vaśyaḥ — brought under another's will",
           {'case': 'dvitīyā', 'sense': 'gata', 'stem': 'vaśa'},
           note='वशं गतः. कामप्राप्तो विधेय इत्यर्थः.'),
    ),
    "4.4.87": (
        _c('padyaḥ kardamaḥ — a rule about the consistency of mud',
           {'case': 'prathamā', 'sense': 'dṛśya', 'stem': 'pada'},
           note='पदमस्मिन् दृश्यम्. कर्दमस्यावस्थोच्यते नातिद्रवो नातिशुष्क इति.'),
    ),
    "4.4.88": (
        _c('mūlyā māṣāḥ — ripeness told by how one harvests it',
           {'case': 'prathamā', 'sense': 'ābarhi', 'stem': 'mūla'},
           note='मूलमस्याबर्हि. मूलोत्पाटनेन विना ग्रहीतुं न शक्यन्ते.'),
    ),
    "4.4.89": (
        _c('dhenuṣyā — the cow given in place of interest',
           {'case': 'prathamā', 'sense': 'dohana-dattā', 'stem': 'dhenu', 'result': 'saṃjñā'},
           note='संज्ञायां धेनुष्या. या धेनुरुत्तमर्णाय ऋणप्रदानाद् दोहनार्थं दीयते सा धेनुष्या.'),
    ),
    "4.4.90": (
        _c('gārhapatyo’gniḥ — and the name-condition keeps the rest out',
           {'case': 'tṛtīyā', 'sense': 'saṃyukta', 'stem': 'gṛhapati', 'result': 'saṃjñā'},
           note='गृहपतिना संयुक्ते ञ्यः. संज्ञाधिकारादतिप्रसङ्गनिवृत्तिः.'),
    ),
    "4.4.91": (
        _c('nāvyam udakam — eight bases against eight senses',
           {'stem': 'nau', 'sense': 'tārya-tulya-prāpya-vadhya-ānāmya-sama-samita-sammita', 'case': 'tṛtīyā', 'result': 'saṃjñā', 'wants': 'yat'},
           note='नौवयोधर्मविषमूलसीतातुलाभ्यस्तार्यतुल्यप्राप्यवध्यानाम्यसमसमितसंमितेषु — अष्टभ्यः शब्देभ्योऽष्टस्वेव तार्यादिष्वर्थेषु यथासंख्यम्: eight bases against eight senses, matched in order, and मूल.'),
    ),
    "4.4.92": (
        _c('dharmyam — not departing from what is right',
           {'stem': 'dharma', 'sense': 'anapeta', 'case': 'pañcamī', 'result': 'saṃjñā', 'wants': 'yat'},
           note='धर्मपथ्यर्थन्यायादनपेते. निर्देशादेव पञ्चमी समर्थविभक्तिः — the ablative is read off the wording. धर्मादनपेतं धर्म्यम्; पथ्यम्, अर्थ्यम्, न्याय्यम् — and all four are still the ordinary words for.'),
    ),
    "4.4.93": (
        _c('chandasyaḥ — and the base means will, not metre',
           {'stem': 'chandas', 'sense': 'nirmita', 'case': 'tṛtīyā', 'wants': 'yat'},
           note='छन्दसो निर्मिते. निर्मित उत्पादितः. छन्दसा निर्मितश् छन्दस्यः, इच्छया कृत इत्यर्थः — and इच्छापर्यायश्छन्दःशब्द इह गृह्यते: the छन्दस् here is not metre but WILL, a synonym of *wish*'),
    ),
    "4.4.94": (
        _c("aurasaḥ putraḥ — a son of one's own breast",
           {'stem': 'uras', 'sense': 'nirmita', 'case': 'tṛtīyā', 'result': 'saṃjñā', 'wants': 'aṇ'},
           note="उरसोऽण् च — the अण्, and by the च the यत्. उरसा निर्मित औरसः पुत्रः, उरस्यः पुत्रः: a son made of one's own breast, the legitimate son"),
    ),
    "4.4.95": (
        _c('hṛdyo deśaḥ — a place dear to the heart',
           {'stem': 'hṛdaya', 'sense': 'priya', 'case': 'ṣaṣṭhī', 'result': 'saṃjñā', 'wants': 'yat'},
           note='हृदयस्य प्रियः. हृदयस्य प्रियो हृद्यो देशः, हृद्यं वनम् — a place dear to the heart. And the संज्ञा heading narrows what may be meant: इह न भवति — हृदयस्य प्रियः पुत्रः, a beloved SON is not what.'),
    ),
    "4.4.96": (
        _c("hṛdyaḥ — the verse that binds another's heart",
           {'stem': 'hṛdaya', 'sense': 'bandhana', 'case': 'ṣaṣṭhī', 'result': 'ṛṣi', 'wants': 'yat'},
           note="बन्धने चर्षौ, हृदयस्येत्येव. बध्यते येन तद् बन्धनम्; ऋषिर्वेदो गृह्यते. हृदयस्य बन्धनम् ऋषिर् हृद्यः — परहृदयं येन बध्यते वशीक्रियते, स वशीकरणमन्त्रो हृद्य इत्युच्यते: the verse by which another's."),
    ),
    "4.4.97": (
        _c('matyam — three bases against three senses',
           {'stem': 'mata', 'sense': 'karaṇa-jalpa-karṣa', 'case': 'ṣaṣṭhī', 'wants': 'yat'},
           note='मतजनहलात् करणजल्पकर्षेषु, यथासंख्यम्. Three bases against three senses. मतं ज्ञानं तस्य करणं मत्यम्; जनस्य जल्पो जन्यः; हलस्य कर्षो हल्यः, द्विहल्यः, त्रिहल्यः. भावसाधनं वा — or each may be read.'),
    ),
    "4.4.98": (
        _c('sāmanyaḥ — skilled, and not helpful',
           {'sense': 'sādhu', 'case': 'saptamī', 'wants': 'yat'},
           note='तत्र साधुः, सप्तमीसमर्थात्. सामसु साधुः सामन्यः; वेमन्यः, कर्मण्यः, शरण्यः.'),
    ),
    "4.4.99": (
        _c('prātijanīnaḥ — good with every man he meets',
           {'gana': 'pratijanādi', 'sense': 'sādhu', 'case': 'saptamī', 'wants': 'khañ'},
           note='प्रतिजनादिभ्यः खञ्, यतोऽपवादः. प्रतिजने साधुः प्रातिजनीनः, जनेजने साधुरित्यर्थः — good with every man he meets. ऐदंयुगीनः, सांयुगीनः.'),
    ),
    "4.4.100": (
        _c('bhāktaḥ śāliḥ — rice that does well as a meal',
           {'stem': 'bhakta', 'sense': 'sādhu', 'case': 'saptamī', 'wants': 'ṇa'},
           note='भक्ताण्णः, यतोऽपवादः. भक्ते साधुर् भाक्तः शालिः, rice that does well as a meal; भाक्तास्तण्डुलाः'),
    ),
    "4.4.101": (
        _c('pāriṣadyaḥ — and the rule read as two for a second affix',
           {'stem': 'pariṣad', 'sense': 'sādhu', 'case': 'saptamī', 'wants': 'ṇya'},
           note='परिषदो ण्यः, यतोऽपवादः. परिषदि साधुः पारिषद्यः.'),
    ),
    "4.4.102": (
        _c('kāthikaḥ — a good story-teller',
           {'gana': 'kathādi', 'sense': 'sādhu', 'case': 'saptamī', 'wants': 'ṭhak'},
           note='कथादिभ्यष्ठक्, यतोऽपवादः. कथायां साधुः काथिकः, a good story-teller; वैकथिकः'),
    ),
    "4.4.103": (
        _c('gauḍika ikṣuḥ — cane that makes good molasses',
           {'gana': 'guḍādi', 'sense': 'sādhu', 'case': 'saptamī', 'wants': 'ṭhañ'},
           note='गुडादिभ्यष्ठञ्, यतोऽपवादः. गुडे साधुर् गौडिक इक्षुः, sugarcane that makes good molasses; कौल्माषिको मुद्गः, साक्तुको यवः — beans good for porridge, barley good for meal. A list of what each crop.'),
    ),
    "4.4.104": (
        _c('pātheyam — provision for the road',
           {'stem': 'pathin', 'sense': 'sādhu', 'case': 'saptamī', 'wants': 'ḍhañ'},
           note='पथ्यतिथिवसतिस्वपतेर्ढञ्, यतोऽपवादः. पथि साधु पाथेयम्, provision for the road; आतिथेयम्, what is fit for a guest; वासतेयम्, स्वापतेयम्'),
    ),
    "4.4.105": (
        _c('sabhyaḥ — fit for an assembly, and so civil',
           {'stem': 'sabhā', 'sense': 'sādhu', 'case': 'saptamī', 'wants': 'ya'},
           note='सभाया यः, यतोऽपवादः; स्वरे विशेषः, and the two differ only in the accent. सभायां साधुः सभ्यः — one fit for an assembly, and so *civil*'),
    ),
    "4.4.106": (
        _c('sabheyaḥ — the same, in the Veda',
           {'stem': 'sabhā', 'sense': 'sādhu', 'case': 'saptamī', 'usage': 'chandasi', 'wants': 'ḍha'},
           note='ढश्छन्दसि, यस्यापवादः. सभेयो युवास्य यजमानस्य वीरो जायताम् (माध्यन्दिनसंहिता २२.२२) — *let a hero be born to this sacrificer, a youth fit for the assembly*'),
    ),
    "4.4.107": (
        _c('satīrthyaḥ — and the ford is the teacher',
           {'stem': 'samānatīrtha', 'sense': 'vāsin', 'case': 'saptamī', 'wants': 'yat'},
           note='समानतीर्थे वासी. साधुरिति निवृत्तम् — *fit* has lapsed. समाने तीर्थे वासीति सतीर्थ्यः, समानोपाध्याय इत्यर्थः: a fellow-student. तीर्थशब्देनेह गुरुरुच्यते — तीर्थ here means the TEACHER, and the.'),
    ),
    "4.4.108": (
        _c('samānodaryaḥ — lain in the same womb',
           {'stem': 'samānodara', 'sense': 'śayita', 'case': 'saptamī', 'wants': 'yat'},
           note='समानोदरे शयित ओ चोदात्तः. शयितः स्थित इत्यर्थः — *lain* means *been*. समानोदरे शयितः समानोदर्यो भ्राता, a brother born of the same womb; and the ओ is made acute in the same act'),
    ),
    "4.4.109": (
        _c('sodaryaḥ — shortened before the affix is added',
           {'stem': 'sodara', 'sense': 'śayita', 'case': 'saptamī', 'wants': 'ya'},
           note='सोदराद् यः. विभाषोदरे [6.3.88] इति सूत्रेण यकारादौ प्रत्यये विवक्षिते प्रागेव समानस्य सभावः — समान becomes स before the affix is even added, by a rule of the sixth chapter. समानोदरे शयितः सोदर्यो.'),
    ),
    "4.4.110": (
        _c('meghyāya — being there, in the Veda',
           {'sense': 'bhava', 'case': 'saptamī', 'usage': 'chandasi', 'wants': 'yat'},
           note='भवे छन्दसि, तत्रेत्येव; अणादीनां घादीनां चापवादः. नमो मेघ्याय च विद्युत्याय च नमः (तैत्तिरीयसंहिता ४.५.७.२).'),
    ),
    "4.4.111": (
        _c('pāthyaḥ — and pāthas is the middle air',
           {'stem': 'pāthas', 'sense': 'bhava', 'case': 'saptamī', 'usage': 'chandasi', 'wants': 'ḍyaṇ'},
           note='पाथोनदीभ्यां ड्यण्, यतोऽपवादः. पाथसि भवः पाथ्यो वृषा (ऋग्वेद ६.१६.१५); चनो दधीत नाद्यो गिरो मे (ऋग्वेद २.३५.१). पाथोऽन्तरिक्षम् — पाथस् is the middle air'),
    ),
    "4.4.112": (
        _c('vaiśantībhyaḥ — the default in the Veda',
           {'stem': 'veśanta', 'sense': 'bhava', 'case': 'saptamī', 'usage': 'chandasi', 'wants': 'aṇ'},
           note='वेशन्तहिमवद्भ्यामण्, यतोऽपवादः. वैशन्तीभ्यः स्वाहा (तैत्तिरीयसंहिता ७.४.१३.९); हैमवतीभ्यः स्वाहा'),
    ),
    "4.4.113": (
        _c('srotyaḥ — and srotasyaḥ, differing in accent',
           {'stem': 'srotas', 'sense': 'bhava', 'case': 'saptamī', 'usage': 'chandasi', 'wants': 'ḍyat'},
           note='स्रोतसो विभाषा ड्यड्ड्यौ, यतोऽपवादः; पक्षे सोऽपि भवति. स्रोतसि भवः स्रोत्यः (ऋग्वेद १०.१०४.८), स्रोतस्यः. ड्यड्ड्ययोः स्वरे विशेषः — the two differ in the accent alone'),
    ),
    "4.4.114": (
        _c('sagarbhyaḥ — the brother of the same womb',
           {'stem': 'sagarbha', 'sense': 'bhava', 'case': 'saptamī', 'usage': 'chandasi', 'wants': 'yan'},
           note='सगर्भसयूथसनुताद् यन्, यतोऽपवादः; स्वरे विशेषः. अनु भ्राता सगर्भ्यः; अनु सखा सयूथ्यः; यो नः सनुत्यः. सर्वत्र समानस्य छन्दसि [6.3.84] इति सभावः — समान becomes स in all three, by a Vedic rule of the.'),
    ),
    "4.4.115": (
        _c('tugriyāṇām — one word carrying four senses',
           {'stem': 'tugra', 'sense': 'bhava', 'case': 'saptamī', 'usage': 'chandasi', 'wants': 'ghan'},
           note='तुग्राद् घन्, यतोऽपवादः. त्वमग्ने वृषभस्तुग्रियाणाम्. अन्नाकाशयज्ञवरिष्ठेषु तुग्रशब्दः — तुग्र is food, sky, sacrifice and the best of anything, four senses for one word'),
    ),
    "4.4.116": (
        _c('agryam — restated against its own successor',
           {'stem': 'agra', 'sense': 'bhava', 'case': 'saptamī', 'usage': 'chandasi', 'wants': 'yat'},
           note='अग्राद् यत्. अग्रे भवम् अग्र्यम्.'),
    ),
    "4.4.117": (
        _c('agriyam — three forms from one base',
           {'stem': 'agra', 'sense': 'bhava', 'case': 'saptamī', 'usage': 'chandasi', 'wants': 'gha'},
           note="घच्छौ च. अग्र्यम् (खिल १.३.७), अग्रियम् (ऋग्वेद १.१३.१०), अग्रीयम् (मैत्रायणीसंहिता २.७.१३). चकारः तुग्राद् घन् इत्यस्यानुकर्षणार्थः — the च drags in 4.4.115's घन् as well, so अग्रियम् comes by."),
    ),
    "4.4.118": (
        _c('samudriyā — and the being-heading stops here',
           {'stem': 'samudra', 'sense': 'bhava', 'case': 'saptamī', 'usage': 'chandasi', 'wants': 'gha'},
           note='समुद्राभ्राद् घः, यतोऽपवादः. समुद्रिया नदीनाम् (ऋग्वेद ७.८७.१); अभ्रियस्येव घोषाः (ऋग्वेद १०.६८.१).'),
    ),
    "4.4.119": (
        _c('barhiṣyeṣu — given on the sacred grass',
           {'stem': 'barhis', 'sense': 'datta', 'case': 'saptamī', 'usage': 'chandasi', 'wants': 'yat'},
           note='बर्हिषि दत्तम्. भव इति निवृत्तम् — *being* has lapsed. बर्हिष्येषु निधिषु प्रियेषु (ऋग्वेद १०.१५.५) — of the dear treasures laid on the sacred grass'),
    ),
    "4.4.120": (
        _c("dūtyam — the messenger's own work",
           {'stem': 'dūta', 'sense': 'bhāga-karman', 'case': 'ṣaṣṭhī', 'usage': 'chandasi', 'wants': 'yat'},
           note='दूतस्य भागकर्मणी. भागोंऽशः; कर्म क्रिया. यदग्ने यासि दूत्यम् (ऋग्वेद १.१२.४) — *when, Agni, you go on your embassy*: दूतभागः, दूतकर्म वा'),
    ),
    "4.4.121": (
        _c('rakṣasyā tanūḥ — and the plural marks the praise',
           {'stem': 'rakṣas', 'sense': 'hananī', 'case': 'ṣaṣṭhī', 'usage': 'chandasi', 'wants': 'yat'},
           note='रक्षोयातूनां हननी. हन्यतेऽनयेति हननी — that by which they are killed. या वां मित्रावरुणौ रक्षस्या तनूः; यातव्या.'),
    ),
    "4.4.122": (
        _c('revatyam — praise of them, three clauses of one verse',
           {'stem': 'revatī', 'sense': 'praśasya', 'case': 'ṣaṣṭhī', 'usage': 'chandasi', 'wants': 'yat'},
           note='रेवतीजगतीहविष्याभ्यः प्रशस्ये. प्रशंसनं प्रशस्यम्; भावे क्यप् प्रत्ययो भवति. यद्वो रेवती रेवत्यम्, यद्वो जगतीर्जगत्यम्, यद्वो हविष्या हविष्यम् (काठकसंहिता १.८) — *what praise of you there is*,.'),
    ),
    "4.4.123": (
        _c("asuryam — the Asuras' own",
           {'stem': 'asura', 'sense': 'sva', 'case': 'ṣaṣṭhī', 'usage': 'chandasi', 'wants': 'yat'},
           note="असुरस्य स्वम्, अणोऽपवादः. असुर्यं वा एतत् पात्रं यत् कुलालकृतं चक्रवृत्तम् (मैत्रायणीसंहिता १.८.३) — *that vessel is the Asuras' own, the one the potter made and the wheel turned*"),
    ),
    "4.4.124": (
        _c('āsurī māyā — but only where their magic is meant',
           {'stem': 'asura', 'sense': 'sva', 'case': 'ṣaṣṭhī', 'result': 'māyā', 'usage': 'chandasi', 'wants': 'aṇ'},
           note="मायायामण्, पूर्वस्य यतोऽपवादः. आसुरी माया स्वधया कृतासि (माध्यन्दिनसंहिता ११.६९) — the Asuras' own, but only where the MAGIC of them is meant"),
    ),
    "4.4.125": (
        _c('varcasyā — the longest rule, and every word a condition',
           {'sense': 'āsām', 'case': 'prathamā', 'result': 'upadhāna-mantra-iṣṭakā', 'samjna': 'matup-anta', 'usage': 'chandasi', 'elided': True, 'wants': 'yat'},
           note='तद्वानासामुपधानो मन्त्र इतीष्टकासु लुक् च मतोः. The longest rule of the pāda, and every word of it is conditional. A stem ending in मतुप् takes यत् where the thing named is BRICKS and the first.'),
    ),
    "4.4.126": (
        _c('āśvinīḥ — and the stem stays whole',
           {'stem': 'aśvimat', 'sense': 'āsām', 'case': 'prathamā', 'result': 'upadhāna-mantra-iṣṭakā', 'usage': 'chandasi', 'elided': True, 'wants': 'aṇ'},
           note='अश्विमानण्, पूर्वस्य यतोऽपवादः. अश्विनीरुपदधाति (शतपथब्राह्मण ८.२.१.१). And when the मतुप् goes, इनण्यनपत्ये [6.4.164] इति प्रकृतिभावः keeps the stem whole where 4.3.108 needed a vārttika to cut it'),
    ),
    "4.4.127": (
        _c('mūrdhanvatīḥ — worded for a state not yet reached',
           {'stem': 'mūrdhan', 'sense': 'āsām', 'case': 'prathamā', 'result': 'vayasyā', 'usage': 'chandasi', 'wants': 'matup'},
           note='वयस्यासु मूर्ध्नो मतुप्, पूर्वस्य यतोऽपवादः. मूर्धा वयः प्रजापतिश्छन्दः — where one mantra has BOTH words, it is वयस्वान् and मूर्धन्वान् alike, and from the second the यत् would have come; मतुप्.'),
    ),
    "4.4.128": (
        _c('nabhasyaḥ — the Vedic month-names',
           {'sense': 'matvartha', 'case': 'prathamā', 'result': 'māsa-tanū', 'usage': 'chandasi', 'wants': 'yat'},
           note='मत्वर्थे मासतन्वोः. मत्वर्थीयानामपवादः — an exception to the whole class of possessive affixes, where the thing is a MONTH or a BODY. नभांसि विद्यन्ते यस्मिन् मासे नभस्यः; सहस्यः, तपस्यः, मधव्यः —.'),
    ),
    "4.4.129": (
        _c('mādhavaḥ — and the ordinary word for spring',
           {'stem': 'madhu', 'sense': 'matvartha', 'case': 'prathamā', 'usage': 'chandasi', 'wants': 'ña'},
           note='मधोर्ञ च — the ञ, and by the च the यत्; and उपसंख्यानात् लुक् च, the elision by a supplement. माधवः, मधव्यः, मधुः — three names for one month, and the first is the ordinary word for spring'),
    ),
    "4.4.130": (
        _c('ojasyam ahaḥ — a day with vigour in it',
           {'stem': 'ojas', 'sense': 'matvartha', 'case': 'prathamā', 'result': 'ahan', 'usage': 'chandasi', 'wants': 'yat'},
           note='ओजसोऽहनि यत्खौ, मत्वर्थ इत्येव. ओजस्यमहः, ओजसीनमहः — a day that has vigour in it'),
    ),
    "4.4.131": (
        _c('veśobhagyaḥ — six senses in the second member',
           {'sense': 'matvartha', 'case': 'prathamā', 'samjna': 'veśo-yaśa-ādi-bhaga-anta', 'usage': 'chandasi', 'wants': 'yal'},
           note='वेशोयशआदेर्भगाद् यल्, मत्वर्थ इत्येव. लकारः स्वरार्थः. वेशोभगो विद्यते यस्य स वेशोभग्यः; यशोभग्यः.'),
    ),
    "4.4.132": (
        _c('veśobhagīnaḥ — a split made for two purposes',
           {'sense': 'matvartha', 'case': 'prathamā', 'samjna': 'veśo-yaśa-ādi-bhaga-anta', 'usage': 'chandasi', 'wants': 'kha'},
           note='ख च. योगविभागो यथासंख्यनिरासार्थ उत्तरार्थश्च — the rule is split BOTH to stop a pairing and for the sake of what follows, which is the first time in the project a split has been given two.'),
    ),
    "4.4.133": (
        _c('pūrviṇebhiḥ — roads the men of old made',
           {'stem': 'pūrva', 'sense': 'kṛta', 'case': 'tṛtīyā', 'usage': 'chandasi', 'wants': 'ina'},
           note='पूर्वैः कृतमिनयौ च. मत्वर्थ इति निवृत्तम्. गम्भीरेभिः पथिभिः पूर्विणेभिः; पूर्व्यैः; पूर्वीणैः.'),
    ),
    "4.4.134": (
        _c('apyaṃ haviḥ — the offering made ready with water',
           {'stem': 'ap', 'sense': 'saṃskṛta', 'case': 'tṛtīyā', 'usage': 'chandasi', 'wants': 'yat'},
           note='अद्भिः संस्कृतम्. यस्येदमप्यं हविः (ऋग्वेद १०.८६.१२) — the offering prepared with water'),
    ),
    "4.4.135": (
        _c('sahasriyaḥ — worth a thousand',
           {'stem': 'sahasra', 'sense': 'sammita', 'case': 'tṛtīyā', 'usage': 'chandasi', 'wants': 'gha'},
           note='सहस्रेण संमितौ घः. संमितस्तुल्यः सदृशः. अयमग्निः सहस्रियः (तैत्तिरीयसंहिता ४.७.१३.४), *worth a thousand*.'),
    ),
    "4.4.136": (
        _c('sahasriyaḥ — and the same affix for having it',
           {'stem': 'sahasra', 'sense': 'matvartha', 'case': 'prathamā', 'usage': 'chandasi', 'wants': 'gha'},
           note='मतौ च. सहस्रमस्य विद्यते सहस्रियः — an exception to तपःसहस्राभ्यां विनीनी [5.2.102] and अण् च [5.2.103], two rules in the chapter after this one'),
    ),
    "4.4.137": (
        _c('somyā brāhmaṇāḥ — fit to receive the soma',
           {'stem': 'soma', 'sense': 'arhati', 'case': 'dvitīyā', 'usage': 'chandasi', 'wants': 'ya'},
           note='सोममर्हति यः. सोममर्हन्ति सोम्या ब्राह्मणाः (काठकसंहिता ५.२), यज्ञार्हा इत्यर्थः — brahmins fit to receive the soma. यति प्रकृते यग्रहणम्; स्वरे विशेषः: यत् was already carrying, and य is named.'),
    ),
    "4.4.138": (
        _c('somyaṃ madhu — and four rules gathered under one name',
           {'stem': 'soma', 'sense': 'mayaṭ-artha', 'case': 'ṣaṣṭhī', 'usage': 'chandasi', 'wants': 'ya'},
           note='मये च. मय इति मयडर्थो लक्ष्यते — the syllable stands for the sense of मयट्, and the vṛtti lists every rule that gives it: 4.3.81, 4.3.82, 4.3.143 and 5.4.21. आगतविकारावयवप्रकृता मयडर्थाः, four.'),
    ),
    "4.4.139": (
        _c("madhavyān — the heading's affix returning",
           {'stem': 'madhu', 'sense': 'mayaṭ-artha', 'case': 'ṣaṣṭhī', 'usage': 'chandasi', 'wants': 'yat'},
           note="मधोः. यशब्दो निवृत्तः — the य of the last rule has lapsed and the heading's यत् returns. मधव्यान् स्तोकान् (पैप्पलादसंहिता १.८८.२), मधुमयान्"),
    ),
    "4.4.140": (
        _c('vasavyaḥ samūhaḥ — and a count worked to seventeen',
           {'stem': 'vasu', 'sense': 'samūha', 'case': 'ṣaṣṭhī', 'usage': 'chandasi', 'wants': 'yat'},
           note='वसोः समूहे च. वसव्यः समूहः, and by the च in the मयट् sense too.'),
    ),
    "4.4.141": (
        _c('nakṣatriyebhyaḥ — an affix that changes only the shape',
           {'stem': 'nakṣatra', 'sense': 'svārtha', 'case': 'prathamā', 'usage': 'chandasi', 'wants': 'gha'},
           note='नक्षत्राद् घः, स्वार्थे. समूह इति नानुवर्तते — the collection-sense does not carry. नक्षत्रियेभ्यः स्वाहा (माध्यन्दिनसंहिता २२.२८)'),
    ),
    "4.4.142": (
        _c('sarvatātim — two more in their own sense',
           {'stem': 'sarva', 'sense': 'svārtha', 'case': 'prathamā', 'usage': 'chandasi', 'wants': 'tātil'},
           note='सर्वदेवात् तातिल्, छन्दसि; स्वार्थिकः. सर्वतातिम् (ऋग्वेद १०.३६.१४), देवतातिम् (ऋग्वेद ३.१९.२) — an affix that changes nothing but the shape'),
    ),
    "4.4.143": (
        _c('śivatātiḥ — making blessed',
           {'gana': 'śivādi', 'sense': 'kara', 'case': 'ṣaṣṭhī', 'usage': 'chandasi', 'wants': 'tātil'},
           note='शिवशमरिष्टस्य करे. करोतीति करः प्रत्ययार्थः. शिवं करोतीति शिवतातिः; शंतातिः, अरिष्टतातिः — *making blessed*, *making peace*, *making unharmed*'),
    ),
    "4.4.144": (
        _c('śivatātiḥ — and the same form for the state',
           {'gana': 'śivādi', 'sense': 'bhāva', 'case': 'ṣaṣṭhī', 'usage': 'chandasi', 'wants': 'tātil'},
           note='भावे च. शिवस्य भावः शिवतातिः — the same three words and the same affix, now for the STATE and not the making. One form for both, and only the context divides them.'),
    ),
    "5.1.1": (
        _c('vatsīyo godhuk — the heading, and what bounds it',
           {'stem': 'vatsa', 'sense': 'hita', 'case': 'caturthī'},
           note='प्राक्क्रीताच्छः. अर्थोऽवधित्वेन गृहीतः, न प्रत्ययः; तेन प्राक् ठञः छ इति नोक्तम्.'),
    ),
    "5.1.2": (
        _c('gavyam — a list and a final sound share one rule',
           {'stem': 'gav', 'gana': 'gavādi', 'sense': 'hita', 'case': 'caturthī'},
           note='उगवादिभ्यो यत्, छस्यापवादः. तत्र सर्वत्र पूर्वविप्रतिषेधेन यत् प्रत्यय एवेष्यते.'),
        _c('nabhyo ’kṣaḥ — the entry gives an affix and a substitute',
           {'stem': 'nābhi', 'gana': 'gavādi', 'sense': 'hita', 'case': 'caturthī'},
           note='नाभि नभं च. नाभिशब्दो यत्प्रत्ययमुत्पादयति, नभं चादेशमापद्यते.'),
    ),
    "5.1.3": (
        _c('kambalyam — only where the word formed is a name',
           {'stem': 'kambala', 'result': 'saṃjñā', 'sense': 'hita', 'case': 'caturthī'},
           note='कम्बलाच्च संज्ञायाम्. संज्ञायामिति किम्? कम्बलीया ऊर्णा.'),
    ),
    "5.1.4": (
        _c('apūpyam, apūpīyam — an option, and both forms stand',
           {'stem': 'apūpa', 'gana': 'apūpādi', 'sense': 'hita', 'case': 'caturthī'},
           note='विभाषा हविरपूपादिभ्यः. हविश्शब्दात्तु गवादिपाठाद् नित्यमेव भवति.'),
    ),
    "5.1.5": (
        _c('vatsīyaḥ — the sense named, the affix left as enjoined',
           {'stem': 'vatsa', 'sense': 'hita', 'case': 'caturthī'},
           note='तस्मै हितम्. चतुर्थीसमर्थाद् हितमित्येतस्मिन्नर्थे यथाविहितं प्रत्ययो भवति.'),
    ),
    "5.1.6": (
        _c('dantyam — a rule that names only what the word means',
           {'samjna': 'śarīrāvayava', 'sense': 'hita', 'case': 'caturthī'},
           note='शरीरावयवाद् यत्, छस्यापवादः. शरीरं प्राणिकायः.'),
    ),
    "5.1.7": (
        _c('khalyam — six words, and two are not what they look like',
           {'gana': 'khalādi', 'sense': 'hita', 'case': 'caturthī'},
           note='खलयवमाषतिलवृषब्रह्मणश्च. छप्रत्ययोऽपि न भवति, अनभिधानात्.'),
    ),
    "5.1.8": (
        _c('ajathyā yūthiḥ — a herd kept for the goats',
           {'stem': 'aja', 'sense': 'hita', 'case': 'caturthī'},
           note='अजाविभ्यां थ्यन्, छस्यापवादः.'),
    ),
    "5.1.9": (
        _c('ātmanīnam — the word spelt out to show its own scope',
           {'stem': 'ātman', 'sense': 'hita', 'case': 'caturthī'},
           note='आत्मन्विश्वजनभोगोत्तरपदात् खः. आत्मन्निति नलोपो न कृतः प्रकृतिपरिमाणज्ञापनार्थम्.'),
        _c('mātṛbhogīṇaḥ — and any compound ending in that word',
           {'uttarapada': 'bhoga', 'sense': 'hita', 'case': 'caturthī'},
           note='भोगोत्तरपदात् खः. केवलेभ्यो मात्रादिभ्यश्छ एव भवति.'),
    ),
    "5.1.10": (
        _c('sārvam, pauruṣeyam — two affixes matched to two words',
           {'stem': 'puruṣa', 'sense': 'hita', 'case': 'caturthī'},
           note='सर्वपुरुषाभ्यां णढञौ, छस्यापवादः. यथासंख्यम्.'),
    ),
    "5.1.11": (
        _c('māṇavīnam — a fourth affix for the same sense',
           {'stem': 'māṇava', 'sense': 'hita', 'case': 'caturthī'},
           note='माणवचरकाभ्यां खञ्, छस्यापवादः.'),
    ),
    "5.1.12": (
        _c('aṅgārīyāṇi kāṣṭhāni — wood that is for charcoal only',
           {'stem': 'aṅgāra', 'samjna': 'vikṛti', 'sense': 'tadartha', 'case': 'caturthī'},
           note='तदर्थं विकृतेः प्रकृतौ. न प्रकृतिविकारसंभवमात्रे प्रत्ययः.'),
    ),
    "5.1.13": (
        _c('chādiṣeyāṇi tṛṇāni — grass for a roof',
           {'gana': 'chadirādi', 'sense': 'tadartha', 'case': 'caturthī'},
           note='छदिरुपधिबलेर्ढञ्, छस्यापवादः. उपधिशब्दात् स्वार्थे प्रत्ययः.'),
    ),
    "5.1.14": (
        _c('aupānahyo muñjaḥ — grass meant to become a shoe',
           {'stem': 'upānah', 'sense': 'tadartha', 'case': 'caturthī'},
           note='ऋषभोपानहोर्ञ्यः. चर्मण्यपि प्रकृतित्वेन विवक्षिते पूर्वविप्रतिषेधाद् अयमेव इष्यते.'),
    ),
    "5.1.15": (
        _c('vārdhraṃ carma — the affix comes after the FINISHED thing',
           {'stem': 'carman', 'sense': 'tadartha', 'case': 'caturthī'},
           note='चर्मणोऽञ्. चर्मण इति षष्ठी; चर्मणो या विकृतिः तद्वाचिनः प्रातिपदिकादञ्.'),
    ),
    "5.1.16": (
        _c('prākārīyā iṣṭakāḥ — bricks that might make a rampart',
           {'stem': 'prākāra', 'sense': 'tadasya-syāt', 'case': 'prathamā'},
           note='तदस्य तदस्मिन् स्यादिति. इतिकरणो विवक्षार्थः; योग्यतामात्रम्.'),
    ),
    "5.1.17": (
        _c('pārikheyī bhūmiḥ — and the heading closes here',
           {'stem': 'parikhā', 'sense': 'tadasya-syāt', 'case': 'prathamā'},
           note='परिखाया ढञ्. छयतोः पूर्णोऽवधिः। इतः परमन्यः प्रत्ययो विधीयते.'),
    ),
    "5.1.18": (
        _c('pārāyaṇikaḥ — a second heading, bounded by another word',
           {'sense': 'ārhīya'},
           note='प्राग्वतेष्ठञ्. प्रागेतस्माद् वतिसंशब्दनात्, ठञ् प्रत्ययस्तेष्वधिकृतो वेदितव्यः.'),
    ),
    "5.1.19": (
        _c('naiṣkikam — a heading inside a heading, and inclusive',
           {'stem': 'pāṇi', 'sense': 'krīta', 'case': 'tṛtīyā'},
           note='आर्हादगोपुच्छसंख्यापरिमाणाट्ठक्. अभिविधावयमाकारः, तेनार्हत्यर्थेऽपि ठग् भवत्येव.'),
    ),
    "5.1.20": (
        _c('naiṣkikam — and not from a compound',
           {'stem': 'niṣka', 'gana': 'niṣkādi', 'sense': 'krīta', 'case': 'tṛtīyā'},
           note='असमासे निष्कादिभ्यः, ठञोऽपवादः. निष्कादिष्वसमासग्रहणं ज्ञापकं पूर्वत्र तदन्ताप्रतिषेधस्य.'),
    ),
    "5.1.21": (
        _c('śatikam, śatyam — refused where the thing meant is that',
           {'stem': 'śata', 'result': 'aśata', 'sense': 'krīta', 'case': 'tṛtīyā'},
           note='शताच्च ठन्यतावशते, कनोऽपवादः. प्रत्ययार्थोऽत्र संघः शतमेव वस्तुतः प्रकृत्यर्थाद् न भिद्यते.'),
    ),
    "5.1.22": (
        _c('pañcakaḥ paṭaḥ — a numeral, but not one ending in ति or शद्',
           {'samjna': 'saṃkhyā', 'sense': 'krīta', 'case': 'tṛtīyā'},
           note='संख्याया अतिशदन्तायाः कन्, ठञोऽपवादः. अर्थवतस्तिशब्दस्य ग्रहणाद् डतेः पर्युदासो न भवति.'),
    ),
    "5.1.23": (
        _c('tāvatikaḥ, tāvatkaḥ — a rule that adds only an insert',
           {'stem_final': 'vatu', 'sense': 'krīta', 'case': 'tṛtīyā'},
           note='वतोरिड्वा. वत्वन्तस्य संख्यात्वात् कन् सिद्ध एव, तस्य त्वनेन वा इडागमो विधीयते.'),
    ),
    "5.1.24": (
        _c('viṃśakaḥ — and the rule is read as two to allow it',
           {'stem': 'viṃśati', 'result': 'asaṃjñā', 'sense': 'krīta', 'case': 'tṛtīyā'},
           note='विंशतित्रिंशद्भ्यां ड्वुन्नसंज्ञायाम्. योगविभागः करिष्यते.'),
    ),
    "5.1.25": (
        _c('kaṃsikaḥ, kaṃsikī — the vṛtti accounts for every letter',
           {'stem': 'kaṃsa', 'sense': 'krīta', 'case': 'tṛtīyā'},
           note='कंसाट्टिठन्. टकारो ङीबर्थः; इकार उच्चारणार्थः; नकारः स्वरार्थः.'),
    ),
    "5.1.26": (
        _c('śaurpam, śaurpikam — an exception that leaves the other',
           {'stem': 'śūrpa', 'sense': 'krīta', 'case': 'tṛtīyā'},
           note='शूर्पादञन्यतरस्याम्, ठञोऽपवादः. पक्षे सोऽपि भवति.'),
    ),
    "5.1.27": (
        _c('śātamānaṃ śatam — displacing both headings at once',
           {'stem': 'śatamāna', 'gana': 'śatamānādi', 'sense': 'krīta', 'case': 'tṛtīyā'},
           note='शतमानविंशतिकसहस्रवसनादण्, ठक्ठञोरपवादः.'),
    ),
    "5.1.28": (
        _c('adhyardhakaṃsam — and now the affix is removed',
           {'pre': 'adhyardha', 'result': 'asaṃjñā', 'sense': 'krīta', 'case': 'tṛtīyā'},
           note='अध्यर्धपूर्वद्विगोर्लुगसंज्ञायाम्. प्रत्ययान्तस्य विशेषणमसंज्ञाग्रहणम्.'),
    ),
    "5.1.29": (
        _c('adhyardhakārṣāpaṇam, adhyardhakārṣāpaṇikam — now a choice',
           {'stem': 'kārṣāpaṇa', 'pre': 'adhyardha', 'sense': 'krīta', 'case': 'tṛtīyā'},
           note='विभाषा कार्षापणसहस्राभ्याम्. पूर्वेण लुकि नित्ये प्राप्ते विकल्प्यते.'),
    ),
    "5.1.30": (
        _c('dviniṣkam, dvinaiṣkikam — and only after two or three',
           {'stem': 'niṣka', 'pre': 'dvi-tri', 'sense': 'krīta', 'case': 'tṛtīyā'},
           note='द्वित्रिपूर्वान्निष्कात्. बहुपूर्वाच्चेति वक्तव्यम्.'),
    ),
    "5.1.31": (
        _c('dvibistam, dvibaistikam — the same option, one more word',
           {'stem': 'bista', 'pre': 'dvi-tri', 'sense': 'krīta', 'case': 'tṛtīyā'},
           note='बिस्ताच्च. द्वित्रिपूर्वादिति चकारेणानुकृष्यते.'),
    ),
    "5.1.32": (
        _c('adhyardhaviṃśatikīnam — an affix that outlives its eliser',
           {'pre': 'adhyardha', 'uttarapada': 'viṃśatika', 'sense': 'krīta', 'case': 'tṛtīyā'},
           note='विंशतिकात् खः. विधानसामर्थ्यादस्य लुङ् न भवति.'),
    ),
    "5.1.33": (
        _c('adhyardhakhārīkam — and two supplements widen it',
           {'pre': 'adhyardha', 'uttarapada': 'khārī', 'sense': 'krīta', 'case': 'tṛtīyā'},
           note='खार्या ईकन्. केवलायाश्चेति वक्तव्यम्; काकिण्याश्चोपसंख्यानम्.'),
    ),
    "5.1.34": (
        _c('adhyardhapādyam — a measure, so the foot rule stays away',
           {'pre': 'adhyardha', 'uttarapada': 'paṇa-pāda-māṣa-śata', 'sense': 'krīta', 'case': 'tṛtīyā'},
           note='पणपादमाषशताद् यत्. प्राण्यङ्गस्य स इष्यते, इदं तु परिमाणम्.'),
    ),
    "5.1.35": (
        _c('adhyardhaśāṇyam, adhyardhaśāṇam — and both halves show',
           {'stem': 'śāṇa', 'pre': 'adhyardha', 'sense': 'krīta', 'case': 'tṛtīyā'},
           note='शाणाद् वा, ठञोऽपवादः. पक्षे सोऽपि भवति, तस्य च लुक्.'),
    ),
    "5.1.36": (
        _c('dvaiśāṇam, dviśāṇyam, dviśāṇam — three forms counted',
           {'stem': 'śāṇa', 'pre': 'dvi-tri', 'sense': 'krīta', 'case': 'tṛtīyā'},
           note='द्वित्रिपूर्वाद् अण् च. तेन त्रैरूप्यं संपद्यते.'),
    ),
    "5.1.37": (
        _c('sāptatikam — the marker, and the plan of the section',
           {'stem': 'saptati', 'sense': 'krīta', 'case': 'tṛtīyā'},
           note='तेन क्रीतम्. ठञादयस्त्रयोदश प्रत्ययाः प्रकृताः; तेषामितः प्रभृति समर्थविभक्तयः प्रत्ययार्थाश्च निर्दिश्यन्ते.'),
    ),
    "5.1.38": (
        _c('śatyam — a twitch of the right eye that means a hundred',
           {'stem': 'śata', 'sense': 'nimitta', 'case': 'ṣaṣṭhī'},
           note='तस्य निमित्तं संयोगोत्पातौ. प्राणिनां शुभाशुभसूचको महाभूतपरिणाम उत्पातः.'),
    ),
    "5.1.39": (
        _c('dhanyam, āyuṣyam — from any stem of two vowels',
           {'vowels': 'dvyac', 'sense': 'nimitta', 'case': 'ṣaṣṭhī'},
           note='गोद्व्यचोऽसंख्यापरिमाणाश्वादेर्यत्. असंख्यापरिमाणाश्वादेरिति किम्? पञ्चकम्.'),
    ),
    "5.1.40": (
        _c('putrīyam, putryam — an affix added to one already due',
           {'stem': 'putra', 'vowels': 'dvyac', 'sense': 'nimitta', 'case': 'ṣaṣṭhī'},
           note='पुत्राच्छ च. द्व्यच इति नित्ये यति प्राप्ते वचनम्.'),
    ),
    "5.1.41": (
        _c('sārvabhaumaḥ — and the strengthening falls on both members',
           {'stem': 'sarvabhūmi', 'sense': 'nimitta', 'case': 'ṣaṣṭhī'},
           note='सर्वभूमिपृथिवीभ्यामणञौ, ठकोऽपवादौ. यथासंख्यम्.'),
    ),
    "5.1.42": (
        _c('sārvabhaumaḥ — lord of it, and the case is said again',
           {'stem': 'sarvabhūmi', 'sense': 'īśvara', 'case': 'ṣaṣṭhī'},
           note='तस्येश्वरः. षष्ठीप्रकरणे पुनः षष्ठीसमर्थविभक्तिनिर्देशः प्रत्ययार्थस्य निवृत्तये.'),
    ),
    "5.1.43": (
        _c('sārvabhaumaḥ — known there, and now a locative',
           {'stem': 'sarvabhūmi', 'sense': 'vidita', 'case': 'saptamī'},
           note='तत्र विदित इति च. विदितो ज्ञातः प्रकाशित इत्यर्थः.'),
    ),
    "5.1.44": (
        _c('laukikaḥ — known in the world',
           {'stem': 'loka', 'sense': 'vidita', 'case': 'saptamī'},
           note='लोकसर्वलोकाट् ठञ्. अनुशतिकादित्वाद् उभयपदवृद्धिः.'),
    ),
    "5.1.45": (
        _c('prāsthikam — land measured by the seed it takes',
           {'stem': 'prastha', 'sense': 'vāpa', 'case': 'ṣaṣṭhī'},
           note='तस्य वापः. उप्यतेऽस्मिन् वापः, क्षेत्रमुच्यते.'),
    ),
    "5.1.46": (
        _c('pātrikaṃ kṣetram — a measure, not a vessel',
           {'stem': 'pātra', 'sense': 'vāpa', 'case': 'ṣaṣṭhī'},
           note='पात्रात् ष्ठन्, ठञोऽपवादः. नकारः स्वरार्थः; षकारो ङीषर्थः.'),
    ),
    "5.1.47": (
        _c('pañcakaḥ — five things given, and each one defined',
           {'sense': 'vṛddhyādi', 'case': 'prathamā'},
           note='तदस्मिन् वृद्ध्यायलाभशुल्कोपदा दीयते. दीयत इत्येकवचनान्तं वृद्ध्यादिभिः प्रत्येकमभिसंबध्यते.'),
    ),
    "5.1.48": (
        _c('dvitīyikaḥ — from an ordinal, and from half a coin',
           {'samjna': 'pūraṇa', 'sense': 'vṛddhyādi', 'case': 'prathamā'},
           note='पूरणार्धाट् ठन्, यथायथं ठक्टिठनोरपवादः. अर्धशब्दो रूपकार्धस्य रूढिः.'),
    ),
    "5.1.49": (
        _c('bhāgyam, bhāgikaṃ śatam — half a coin again',
           {'stem': 'bhāga', 'sense': 'vṛddhyādi', 'case': 'prathamā'},
           note='भागाद् यच्च, ठञोऽपवादः. भागशब्दोऽपि रूपकार्धस्य वाचकः.'),
    ),
    "5.1.50": (
        _c('vāṃśabhārikaḥ, vāṃśikaḥ — two readings, and both stand',
           {'gana': 'vaṃśādi', 'uttarapada': 'bhāra', 'sense': 'harati', 'case': 'dvitīyā'},
           note='तद्धरति वहति आवहति भाराद् वंशादिभ्यः. सूत्रार्थद्वयमपि चैतद् आचार्येण शिष्याः प्रतिपादिताः; तदुभयमपि ग्राह्यम्.'),
    ),
    "5.1.51": (
        _c('vasnikaḥ, dravyakaḥ — two words, two affixes, in order',
           {'stem': 'vasna', 'sense': 'harati', 'case': 'dvitīyā'},
           note='वस्नद्रव्याभ्यां ठन्कनौ, यथासंख्यम्.'),
    ),
    "5.1.52": (
        _c('prāsthikaḥ — holds it, takes it up, cooks it',
           {'stem': 'prastha', 'sense': 'sambhavati', 'case': 'dvitīyā'},
           note='संभवत्यवहरति पचति. तत्राधेयस्य प्रमाणानतिरेकः संभवः; विक्लेदनं पाकः.'),
    ),
    "5.1.53": (
        _c('āḍhakīnā, āḍhakikī — an option, and the heading in the other',
           {'stem': 'āḍhaka', 'sense': 'sambhavati', 'case': 'dvitīyā'},
           note='आढकाचितपात्रात् खोऽन्यतरस्याम्, ठञोऽपवादः. पक्षे सोऽपि भवति.'),
    ),
    "5.1.54": (
        _c('dvyāḍhakikī, dvyāḍhakīnā, dvyāḍhakī — three forms',
           {'uttarapada': 'āḍhaka-ācita-pātra', 'pre': 'dvigu', 'sense': 'sambhavati', 'case': 'dvitīyā'},
           note='द्विगोः ष्ठंश्च. विधानसामर्थ्यादनयोर्लुग् न भवति.'),
    ),
    "5.1.55": (
        _c('dvikulijikī, dvikulijī — four forms, the elision one of them',
           {'uttarapada': 'kulija', 'pre': 'dvigu', 'sense': 'sambhavati', 'case': 'dvitīyā'},
           note='कुलिजाल् लुक्खौ च. अन्यतरस्यांग्रहणानुवृत्त्या लुगपि विकल्प्यते; तेन चातूरूप्यं संपद्यते.'),
    ),
    "5.1.56": (
        _c('pañcakaḥ — its share, its price, its wages',
           {'sense': 'aṃśa-vasna-bhṛti', 'case': 'prathamā'},
           note='सोऽस्यांशवस्नभृतयः. अंशो भागः; वस्नं मूल्यम्; भृतिर्वेतनम्.'),
    ),
    "5.1.57": (
        _c('prāsthiko rāśiḥ — and the restating keeps the affix',
           {'stem': 'prastha', 'sense': 'parimāṇa', 'case': 'prathamā'},
           note='तदस्य परिमाणम्. पुनर्विधानसामर्थ्याद् अध्यर्धपूर्वद्विगोर्लुग् न भवति.'),
    ),
    "5.1.58": (
        _c('aṣṭakaṃ pāṇinīyam — the rule by which this book is named',
           {'samjna': 'saṃkhyā', 'sense': 'parimāṇa', 'case': 'prathamā', 'result': 'saṃjñā-saṃgha-sūtra-adhyayana'},
           note='संख्यायाः संज्ञासंघसूत्राध्ययनेषु. अष्टावध्यायाः परिमाणमस्य सूत्रस्य अष्टकं पाणिनीयम्.'),
    ),
    "5.1.59": (
        _c('paṅktiḥ, viṃśatiḥ, śatam — ten words laid down whole',
           {'samjna': 'saṃkhyā', 'sense': 'parimāṇa', 'case': 'prathamā'},
           note='पङ्क्तिविंशति… नात्रावयवार्थेऽभिनिवेष्टव्यम्; उदाहरणमात्रमेतत्.'),
    ),
    "5.1.60": (
        _c('pañcad vargaḥ, pañcako vargaḥ — a class, and a choice',
           {'stem': 'pañcan', 'sense': 'parimāṇa', 'case': 'prathamā', 'result': 'varga'},
           note='पञ्चद्दशतौ वर्गे वा. संख्यायाः इति कनि प्राप्ते डतिर्निपात्यते.'),
    ),
    "5.1.61": (
        _c('sapta sāptāni — the one Vedic rule of the quarter',
           {'stem': 'saptan', 'sense': 'parimāṇa', 'case': 'prathamā', 'result': 'varga', 'usage': 'chandasi'},
           note='सप्तनोऽञ् छन्दसि. वर्ग इत्येव.'),
    ),
    "5.1.62": (
        _c('traiṃśāni brāhmaṇāni — a locative of what the word means',
           {'stem': 'triṃśat', 'sense': 'parimāṇa', 'case': 'prathamā', 'result': 'brāhmaṇa'},
           note='त्रिंशच्चत्वारिंशतोर्ब्राह्मणे संज्ञायां डण्. अभिधेयसप्तम्येषा, न विषयसप्तमी.'),
    ),
    "5.1.63": (
        _c('śvaitacchatrikaḥ — the heading closes on its own word',
           {'stem': 'śvetacchatra', 'sense': 'arhati', 'case': 'dvitīyā'},
           note='तदर्हति. अभिविधावयमाकारः, तेनार्हत्यर्थेऽपि ठग् भवत्येव.'),
    ),
    "5.1.64": (
        _c('chaidikaḥ — deserving it always, and *always* is the sense',
           {'gana': 'chedādi', 'sense': 'arhati', 'case': 'dvitīyā', 'result': 'nitya'},
           note='छेदादिभ्यो नित्यम्. नित्यग्रहणं प्रत्ययार्थविशेषणम्.'),
    ),
    "5.1.65": (
        _c('śīrṣacchedyaḥ — the shape change is yoked to the affix',
           {'stem': 'śīrṣaccheda', 'sense': 'arhati', 'case': 'dvitīyā', 'result': 'nitya'},
           note='शीर्षच्छेदाद् यच्च. प्रत्ययसन्नियोगेन शिरसः शीर्षभावो निपात्यते.'),
    ),
    "5.1.66": (
        _c('daṇḍyaḥ — one who deserves the rod',
           {'gana': 'daṇḍādi', 'sense': 'arhati', 'case': 'dvitīyā'},
           note='दण्डादिभ्यः, ठकोऽपवादः. नित्यमिति निवृत्तम्.'),
    ),
    "5.1.67": (
        _c('yūpyaḥ palāśaḥ — in the Veda, after any stem at all',
           {'sense': 'arhati', 'case': 'dvitīyā', 'usage': 'chandasi'},
           note='छन्दसि च, ठञादीनामपवादः. प्रातिपदिकमात्रात्.'),
    ),
    "5.1.68": (
        _c('pātriyaḥ, pātryaḥ — a measure again, not a vessel',
           {'stem': 'pātra', 'sense': 'arhati', 'case': 'dvitīyā'},
           note='पात्राद् घंश्च, ठक्ठञोरपवादः. पात्रं परिमाणमप्यस्ति.'),
    ),
    "5.1.69": (
        _c('dakṣiṇīyo bhikṣuḥ — and the word order is itself a sign',
           {'stem': 'dakṣiṇā', 'sense': 'arhati', 'case': 'dvitīyā'},
           note='कडङ्करदक्षिणाच्छ च, ठकोऽपवादः. अल्पाच्तरस्यापूर्वनिपातेन यथासंख्याभावं सूचयति.'),
    ),
    "5.1.70": (
        _c('sthālībilīyās taṇḍulāḥ — grain fit to be cooked',
           {'stem': 'sthālībila', 'sense': 'arhati', 'case': 'dvitīyā'},
           note='स्थालीबिलात्, ठकोऽपवादौ. छयतावनुवर्तते; पाकयोग्या इत्यर्थः.'),
    ),
    "5.1.71": (
        _c('yajñiyo brāhmaṇaḥ — and the section closes here',
           {'stem': 'yajña', 'sense': 'arhati', 'case': 'dvitīyā'},
           note='यज्ञर्त्विग्भ्यां घखञौ. आर्हीयाणां ठगादीनां पूर्णोऽवधिः; अतः परं प्राग्वतीयष्ठञेव भवति.'),
    ),
    "5.1.72": (
        _c('pārāyaṇikaś chātraḥ — carries it on, that is, studies it',
           {'gana': 'pārāyaṇādi', 'sense': 'vartayati', 'case': 'dvitīyā'},
           note='पारायणतुरायणचान्द्रायणं वर्तयति. समर्थविभक्तिरनुवर्तते; अर्हतीति निवृत्तम्.'),
    ),
    "5.1.73": (
        _c('sāṃśayikaḥ sthāṇuḥ — a post one has come to doubt about',
           {'stem': 'saṃśaya', 'sense': 'āpanna', 'case': 'dvitīyā'},
           note='संशयमापन्नः. संशयमापन्नः प्राप्तः.'),
    ),
    "5.1.74": (
        _c('yaujanikaḥ — and a teacher worth a hundred leagues',
           {'stem': 'yojana', 'sense': 'gacchati', 'case': 'dvitīyā'},
           note='योजनं गच्छति. ततोऽभिगमनमर्हतीति च क्रोशशतयोजनशतयोरुपसंख्यानम्.'),
    ),
    "5.1.75": (
        _c('pathikaḥ, pathikī — one letter for accent, one for gender',
           {'stem': 'pathin', 'sense': 'gacchati', 'case': 'dvitīyā'},
           note='पथः ष्कन्. नकारः स्वरार्थः; षकारो ङीषर्थः.'),
    ),
    "5.1.76": (
        _c('pāntho bhikṣāṃ yācate — always on the road',
           {'stem': 'pathin', 'sense': 'gacchati', 'case': 'dvitīyā', 'result': 'nitya'},
           note='पन्थो ण नित्यम्. पथः पन्थ इत्ययमादेशो भवति णश्च प्रत्ययः. नित्यमिति किम्? पथिकः.'),
    ),
    "5.1.77": (
        _c('auttarapathikam — one affix for two senses at once',
           {'stem': 'uttarapatha', 'sense': 'āhṛta', 'case': 'tṛtīyā'},
           note='उत्तरपथेनाहृतं च. निर्देशादेव समर्थविभक्तिः; चकारः प्रत्ययार्थसमुच्चये, गच्छतीति च.'),
    ),
    "5.1.78": (
        _c('māsikam — a heading that carries a condition, not an affix',
           {'samjna': 'kāla', 'sense': 'nirvṛtta', 'case': 'tṛtīyā'},
           note='कालात्. कालादित्यधिकारः; कालादित्यधिकारो व्युष्टादिभ्योऽण् इति यावत्.'),
    ),
    "5.1.79": (
        _c('ahnā nirvṛttam āhnikam — a day work',
           {'samjna': 'kāla', 'sense': 'nirvṛtta', 'case': 'tṛtīyā'},
           note='तेन निर्वृत्तम्.'),
    ),
    "5.1.80": (
        _c('māsiko ’dhyāpakaḥ — four senses, and each one glossed',
           {'samjna': 'kāla', 'sense': 'adhīṣṭādi', 'case': 'dvitīyā'},
           note='तमधीष्टो भृतो भूतो भावी. अधीष्टः सत्कृत्य व्यापारितः; भृतो वेतनेन क्रीतः.'),
    ),
    "5.1.81": (
        _c('māsyaḥ, māsīnaḥ — of an AGE, so only one sense joins',
           {'stem': 'māsa', 'samjna': 'kāla', 'sense': 'adhīṣṭādi', 'case': 'dvitīyā', 'result': 'vayas'},
           note='मासाद् वयसि यत्खञौ. सामर्थ्याद् भूत एवात्राभिसंबध्यते.'),
    ),
    "5.1.82": (
        _c('dvimāsyaḥ — and after a numeral compound',
           {'uttarapada': 'māsa', 'pre': 'dvigu', 'samjna': 'kāla', 'sense': 'adhīṣṭādi', 'case': 'dvitīyā', 'result': 'vayas'},
           note='द्विगोर्यप्. मासाद् वयसीति वर्तते.'),
    ),
    "5.1.83": (
        _c('ṣāṇmāsyaḥ, ṣaṇmāsyaḥ, ṣāṇmāsikaḥ — three forms again',
           {'stem': 'ṣaṇmāsa', 'samjna': 'kāla', 'sense': 'adhīṣṭādi', 'case': 'dvitīyā', 'result': 'vayas'},
           note='षण्मासाण् ण्यच्च. स्वरितत्वाच्चानन्तरोऽनुवर्तिष्यते; तेन त्रैरूप्यं भवति.'),
    ),
    "5.1.84": (
        _c('ṣaṇmāsiko rogaḥ — the same word, and NOT of an age',
           {'stem': 'ṣaṇmāsa', 'samjna': 'kāla', 'sense': 'adhīṣṭādi', 'case': 'dvitīyā', 'result': 'avayas'},
           note='अवयसि ठंश्च. चकारेणानन्तरस्य ण्यतः समुच्चयः क्रियते.'),
    ),
    "5.1.85": (
        _c('samām adhīṣṭaḥ samīnaḥ — all four senses back',
           {'stem': 'samā', 'samjna': 'kāla', 'sense': 'adhīṣṭādi', 'case': 'dvitīyā'},
           note='समायाः खः, ठञोऽपवादः. अधीष्टादयश्चत्वारोऽर्था अनुवर्तन्ते.'),
    ),
    "5.1.86": (
        _c('dvisamīnaḥ, dvaisamikaḥ — obligatory turned to a choice',
           {'uttarapada': 'samā', 'pre': 'dvigu', 'samjna': 'kāla', 'sense': 'nirvṛttādi', 'case': 'dvitīyā'},
           note='द्विगोर्वा. पूर्वेण नित्यः प्राप्तो विकल्प्यते; खेन मुक्ते पक्षे ठञपि भवति.'),
    ),
    "5.1.87": (
        _c('dvirātrīṇaḥ, dvairātrikaḥ — three more words of time',
           {'uttarapada': 'rātri-ahan-saṃvatsara', 'pre': 'dvigu', 'samjna': 'kāla', 'sense': 'nirvṛttādi', 'case': 'dvitīyā'},
           note='रात्र्यहस्संवत्सराच्च. संख्यायाः संवत्सरसंख्यस्य च इत्युत्तरपदवृद्धिः.'),
    ),
    "5.1.88": (
        _c('dvivarṣīṇo vyādhiḥ, dvivārṣikaḥ, dvivarṣaḥ — three forms',
           {'uttarapada': 'varṣa', 'pre': 'dvigu', 'samjna': 'kāla', 'sense': 'nirvṛttādi', 'case': 'dvitīyā'},
           note='वर्षाल् लुक् च. तयोश्च वा लुग् भवति; एवं त्रीणि रूपाणि भवन्ति.'),
    ),
    "5.1.89": (
        _c('dvivarṣo dārakaḥ — where the thing meant has a mind',
           {'uttarapada': 'varṣa', 'pre': 'dvigu', 'samjna': 'kāla', 'sense': 'nirvṛttādi', 'case': 'dvitīyā', 'result': 'cittavat'},
           note='चित्तवति नित्यम्. पूर्वेण विकल्पे प्राप्ते वचनम्. चित्तवतीति किम्? द्विवर्षीणो व्याधिः.'),
    ),
    "5.1.90": (
        _c('ṣaṣṭikāḥ — rice that ripens in sixty nights',
           {'stem': 'ṣaṣṭirātra', 'samjna': 'kāla', 'sense': 'pacyate', 'case': 'tṛtīyā', 'result': 'saṃjñā'},
           note='षष्टिकाः षष्टिरात्रेण पच्यन्ते. संज्ञैषा धान्यविशेषस्य; तेन मुद्गादिष्वतिप्रसङ्गो न भवति.'),
    ),
    "5.1.91": (
        _c('idvatsarīyaḥ — in the Veda, after a year-final stem',
           {'uttarapada': 'vatsara', 'samjna': 'kāla', 'sense': 'nirvṛttādi', 'case': 'tṛtīyā', 'usage': 'chandasi'},
           note='वत्सरान्ताच्छश्छन्दसि, ठञोऽपवादः.'),
    ),
    "5.1.92": (
        _c('saṃvatsarīṇāḥ — with two particular words in front',
           {'uttarapada': 'vatsara', 'pre': 'sam-pari', 'samjna': 'kāla', 'sense': 'nirvṛttādi', 'case': 'tṛtīyā', 'usage': 'chandasi'},
           note='संपरिपूर्वात् ख च.'),
    ),
    "5.1.93": (
        _c('māsikaḥ prāsādaḥ — a palace easily built in a month',
           {'samjna': 'kāla', 'sense': 'parijayya-labhya-kārya-sukara', 'case': 'tṛtīyā'},
           note='तेन परिजय्यलभ्यकार्यसुकरम्. मासेन परिजय्यः, शक्यते जेतुम्.'),
    ),
    "5.1.94": (
        _c('māsiko brahmacārī — two readings, and both authoritative',
           {'samjna': 'kāla', 'sense': 'brahmacarya', 'case': 'dvitīyā'},
           note='तदस्य ब्रह्मचर्यम्. उभयमपि प्रमाणम्, उभयथा सूत्रप्रणयनात्.'),
    ),
    "5.1.95": (
        _c('āgniṣṭomikī dakṣiṇā — and the word *named* frees the rule',
           {'samjna': 'yajña-ākhyā', 'sense': 'dakṣiṇā', 'case': 'ṣaṣṭhī'},
           note='तस्य च दक्षिणा यज्ञाख्येभ्यः. आख्याग्रहणमकालादपि यज्ञवाचिनो यथा स्यादिति.'),
    ),
    "5.1.96": (
        _c('māse dīyate māsikam — and the time heading ends here',
           {'samjna': 'kāla', 'sense': 'dīyate-kārya', 'case': 'saptamī'},
           note='तत्र च दीयते कार्यं भववत्. कालाधिकारस्य पूर्णोऽवधिः; अतः परं सामान्येन प्रत्ययविधानम्.'),
    ),
    "5.1.97": (
        _c('vyuṣṭe dīyate vaiyuṣṭam — no longer a word for time',
           {'gana': 'vyuṣṭādi', 'sense': 'dīyate-kārya', 'case': 'saptamī'},
           note='व्युष्टादिभ्योऽण्. किं वक्तव्यम्? न वक्तव्यम्; अत्रैव ते पठितव्याः.'),
    ),
    "5.1.98": (
        _c('yāthākathācam — a word that cannot really take a case',
           {'stem': 'yathākathāca', 'sense': 'dīyate-kārya', 'case': 'tṛtīyā'},
           note='तेन यथाकथाचहस्ताभ्यां णयतौ. तृतीयार्थमात्रं चात्र संभवति, न तु तृतीया समर्थविभक्तिः.'),
    ),
    "5.1.99": (
        _c('kārṇaveṣṭakikaṃ mukham — a face that earrings set off',
           {'sense': 'sampādin', 'case': 'tṛtīyā'},
           note='संपादिनि. गुणोत्कर्षः संपत्तिः.'),
    ),
    "5.1.100": (
        _c('karmaṇyaṃ śarīram — a body that work sets off',
           {'stem': 'karman', 'sense': 'sampādin', 'case': 'tṛtīyā'},
           note='कर्मवेषाद् यत्, ठञोऽपवादः.'),
    ),
    "5.1.101": (
        _c('sāntāpikaḥ — equal to it, and the dative of adequacy',
           {'gana': 'saṃtāpādi', 'sense': 'prabhavati', 'case': 'caturthī'},
           note='तस्मै प्रभवति संतापादिभ्यः. समर्थः शक्तः प्रभवतीत्युच्यते; अलमर्थे चतुर्थी.'),
    ),
    "5.1.102": (
        _c('yogyaḥ, yaugikaḥ — a conjunction keeping both',
           {'stem': 'yoga', 'sense': 'prabhavati', 'case': 'caturthī'},
           note='योगाद् यच्च.'),
    ),
    "5.1.103": (
        _c('kārmukaṃ dhanuḥ — used of a bow and of nothing else',
           {'stem': 'karman', 'sense': 'prabhavati', 'case': 'caturthī', 'result': 'dhanus'},
           note='कर्मण उकञ्, ठञोऽपवादः. धनुषोऽन्यत्र न भवति, अनभिधानात्.'),
    ),
    "5.1.104": (
        _c('sāmayikaṃ kāryam — a matter whose time has come round',
           {'stem': 'samaya', 'sense': 'prāpta', 'case': 'prathamā'},
           note='समयस्तदस्य प्राप्तम्. समर्थविभक्तिनिर्देश उत्तरार्थः.'),
    ),
    "5.1.105": (
        _c('ārtavaṃ puṣpam — a flower whose season has come',
           {'stem': 'ṛtu', 'sense': 'prāpta', 'case': 'prathamā'},
           note='ऋतोरण्. तदस्य प्रकरण उपवस्त्रादिभ्य उपसंख्यानम्.'),
    ),
    "5.1.106": (
        _c('ṛtviyaḥ — one word, two affixes, divided by register',
           {'stem': 'ṛtu', 'sense': 'prāpta', 'case': 'prathamā', 'usage': 'chandasi'},
           note='छन्दसि घस्, अणोऽपवादः.'),
    ),
    "5.1.107": (
        _c('kālyas tāpaḥ — heat that has come in its time',
           {'stem': 'kāla', 'sense': 'prāpta', 'case': 'prathamā'},
           note='कालाद् यत्.'),
    ),
    "5.1.108": (
        _c('kālikam ṛṇam — a debt of long standing',
           {'stem': 'kāla', 'case': 'prathamā', 'result': 'prakṛṣṭa'},
           note='प्रकृष्टे ठञ्. प्राप्तमिति निवृत्तम्; ठञ्ग्रहणं विस्पष्टार्थम्.'),
    ),
    "5.1.109": (
        _c('aindramahikam — a thing whose occasion is a festival',
           {'sense': 'prayojana', 'case': 'prathamā'},
           note='प्रयोजनम्.'),
    ),
    "5.1.110": (
        _c('vaiśākho manthaḥ — two words matched to two things meant',
           {'stem': 'viśākhā', 'sense': 'prayojana', 'case': 'prathamā', 'result': 'mantha-daṇḍa'},
           note='विशाखाषाढादण् मन्थदण्डयोः. चूडादिभ्य उपसंख्यानम्.'),
    ),
    "5.1.111": (
        _c('anupravacanīyam — and one supplement removes the affix',
           {'gana': 'anupravacanādi', 'sense': 'prayojana', 'case': 'prathamā'},
           note='अनुप्रवचनादिभ्यश्छः, ठञोऽपवादः. पुण्याहवाचनादिभ्यो लुग् वक्तव्यः.'),
    ),
    "5.1.112": (
        _c('chandaḥsamāpanīyam — and *word* shuts out a prefix',
           {'uttarapada': 'samāpana', 'sense': 'prayojana', 'case': 'prathamā'},
           note='समापनात् सपूर्वपदात्, ठञोऽपवादः. पदग्रहणं बहुच्पूर्वनिरासार्थम्.'),
    ),
    "5.1.113": (
        _c('aikāgārikaḥ cauraḥ — laid down in order to narrow it',
           {'stem': 'ekāgāra', 'sense': 'prayojana', 'case': 'prathamā', 'result': 'caura'},
           note='ऐकागारिकट् चौरे. चौरे नियमार्थं वचनम्; इह मा भूत् — एकागारं प्रयोजनमस्य भिक्षोरिति.'),
    ),
    "5.1.114": (
        _c('ākālikī vidyut — perishing the instant it arises',
           {'stem': 'samānakāla', 'sense': 'ādyanta', 'case': 'prathamā'},
           note='आकालिकड् आद्यन्तवचने. जन्मना तुल्यकालविनाशा; उत्पादानन्तरं विनाशिनीत्यर्थः. ठञः पूर्णोऽवधिः.'),
    ),
    "5.1.115": (
        _c('brāhmaṇavat — a likeness of action and of nothing else',
           {'sense': 'tulya', 'case': 'tṛtīyā', 'result': 'kriyā'},
           note='तेन तुल्यं क्रिया चेद् वतिः. क्रियाग्रहणं किम्? गुणद्रव्यतुल्ये मा भूत्.'),
    ),
    "5.1.116": (
        _c('mathurāvat srughne prākāraḥ — one rule, two cases',
           {'stem': 'mathurā', 'sense': 'iva', 'case': 'saptamī'},
           note='तत्र तस्येव. सप्तमीसमर्थात् षष्ठीसमर्थात् च इवार्थे वतिः.'),
    ),
    "5.1.117": (
        _c('rājavat pālanam — such as a king deserves',
           {'sense': 'arha', 'case': 'dvitīyā'},
           note='तदर्हम्.'),
    ),
    "5.1.118": (
        _c('udvato nivato — after a preverb, in its own sense',
           {'samjna': 'upasarga', 'sense': 'svārtha', 'usage': 'chandasi'},
           note='उपसर्गाच्छन्दसि धात्वर्थे. उपसर्गात् ससाधने धात्वर्थे वर्तमानात् स्वार्थे वतिः.'),
    ),
    "5.1.119": (
        _c('aśvatvam, aśvatā — the ground for applying a word',
           {'stem': 'aśva', 'sense': 'bhāva', 'case': 'ṣaṣṭhī'},
           note='तस्य भावस्त्वतलौ. शब्दस्य प्रवृत्तिनिमित्तं भावशब्देनोच्यते.'),
    ),
    "5.1.120": (
        _c('pṛthutvam beside prathimā — a heading that is not beaten',
           {'sense': 'bhāva', 'case': 'ṣaṣṭhī'},
           note='आ च त्वात्. अपवादैः सह समावेशार्थं वचनम्; त्वतलौ सर्वत्र भवत एव.'),
    ),
    "5.1.121": (
        _c('apatitvam — the special affixes refused, the two left',
           {'pre': 'nañ', 'sense': 'bhāva', 'case': 'ṣaṣṭhī'},
           note='न नञ्पूर्वात् तत्पुरुषात्…. नञ्पूर्वादिति किम्? बार्हस्पत्यम्. तत्पुरुषादिति किम्? आपटवम्.'),
    ),
    "5.1.122": (
        _c('prathimā, pārthavam — the option admits both forms',
           {'stem': 'pṛthu', 'gana': 'pṛthvādi', 'sense': 'bhāva', 'case': 'ṣaṣṭhī'},
           note='पृथ्वादिभ्य इमनिच् वा. वावचनमणादेः समावेशार्थम्.'),
    ),
    "5.1.123": (
        _c('śauklyam, śuklimā — from the words for colours',
           {'samjna': 'varṇa', 'sense': 'bhāva', 'case': 'ṣaṣṭhī'},
           note='वर्णदृढादिभ्यः ष्यञ् च. षकारो ङीषर्थः.'),
    ),
    "5.1.124": (
        _c('jāḍyam — a quality word, and an activity beside',
           {'samjna': 'guṇavacana', 'sense': 'bhāva-karman', 'case': 'ṣaṣṭhī'},
           note='गुणवचनब्राह्मणादिभ्यः कर्मणि च. आ पादपरिसमाप्तेर्भावकर्माधिकारः; ब्राह्मणादिराकृतिगणः.'),
    ),
    "5.1.125": (
        _c('steyam — the affix and a dropped sound together',
           {'stem': 'stena', 'sense': 'bhāva-karman', 'case': 'ṣaṣṭhī'},
           note='स्तेनाद् यन्नलोपश्च. स्तेनादिति केचिद् योगविभागं कुर्वन्ति.'),
    ),
    "5.1.126": (
        _c('sakhyam — friendship',
           {'stem': 'sakhi', 'sense': 'bhāva-karman', 'case': 'ṣaṣṭhī'},
           note='सख्युर्यः. दूतवणिग्भ्यां चेति वक्तव्यम्.'),
    ),
    "5.1.127": (
        _c('kāpeyam, jñāteyam — and the senses are never paired off',
           {'stem': 'jñāti', 'sense': 'bhāva-karman', 'case': 'ṣaṣṭhī'},
           note='कपिज्ञात्योर्ढक्. यथासंख्यमर्थयोः सर्वत्रैवात्र प्रकरणे नेष्यते.'),
    ),
    "5.1.128": (
        _c('saināpatyam — from any stem ending in that word',
           {'uttarapada': 'pati', 'sense': 'bhāva-karman', 'case': 'ṣaṣṭhī'},
           note='पत्यन्तपुरोहितादिभ्यो यक्.'),
    ),
    "5.1.129": (
        _c('āśvam, kaumāram — kinds of creature, and stages of life',
           {'samjna': 'prāṇabhṛj-jāti', 'sense': 'bhāva-karman', 'case': 'ṣaṣṭhī'},
           note='प्राणभृज्जातिवयोवचनोद्गात्रादिभ्योऽञ्.'),
    ),
    "5.1.130": (
        _c('dvaihāyanam, yauvanam — and one word drops a sound',
           {'uttarapada': 'hāyana', 'sense': 'bhāva-karman', 'case': 'ṣaṣṭhī'},
           note='हायनान्तयुवादिभ्योऽण्. श्रोत्रियस्य यलोपश्च वाच्यः.'),
    ),
    "5.1.131": (
        _c('śaucam, lāghavam — and a parsing rejected as wasteful',
           {'stem_final': 'ik', 'upadha': 'laghu', 'sense': 'bhāva-karman', 'case': 'ṣaṣṭhī'},
           note='इगन्ताच्च लघुपूर्वात्. अस्मिन् व्याख्यानेऽन्तग्रहणमतिरिच्यते.'),
    ),
    "5.1.132": (
        _c('rāmaṇīyakam — and upottama is defined on the spot',
           {'upadha': 'ya', 'result': 'gurūpottama', 'sense': 'bhāva-karman', 'case': 'ṣaṣṭhī'},
           note='योपधाद् गुरूपोत्तमाद् वुञ्. त्रिप्रभृतीनामन्तस्य समीपमुपोत्तमम्.'),
    ),
    "5.1.133": (
        _c('gaupālapaśupālikā — from a copulative compound',
           {'samjna': 'dvandva', 'sense': 'bhāva-karman', 'case': 'ṣaṣṭhī'},
           note='द्वन्द्वमनोज्ञादिभ्यश्च.'),
    ),
    "5.1.134": (
        _c('gārgikayā ślāghate — boasting of a lineage',
           {'samjna': 'gotra-caraṇa', 'sense': 'bhāva-karman', 'case': 'ṣaṣṭhī', 'result': 'ślāghā-atyākāra-tadaveta'},
           note='गोत्रचरणाच्छ्लाघात्याकारतदवेतेषु. श्लाघा विकत्थनम्; अत्याकारः पराधिक्षेपः.'),
    ),
    "5.1.135": (
        _c('acchāvākīyam — the words for particular officiants',
           {'samjna': 'hotrā', 'sense': 'bhāva-karman', 'case': 'ṣaṣṭhī'},
           note='होत्राभ्यश्छः. बहुवचनं स्वरूपविधिनिरासार्थम्.'),
    ),
    "5.1.136": (
        _c('brahmatvam — an affix named where a refusal would do',
           {'stem': 'brahman', 'samjna': 'hotrā', 'sense': 'bhāva-karman', 'case': 'ṣaṣṭhī'},
           note='ब्रह्मणस्त्वः, छस्यापवादः. नेति वक्तव्ये त्ववचनं तलो बाधनार्थम्.'),
    ),
    "5.2.1": (
        _c('maudgīnam — a field, and a granary is not one',
           {'samjna': 'dhānya', 'sense': 'bhavana', 'case': 'ṣaṣṭhī', 'result': 'kṣetra'},
           note='धान्यानां भवने क्षेत्रे खञ्. भवन्ति जायन्तेऽस्मिन्निति भवनम्. क्षेत्रमिति किम्? मुद्गानां भवनं कुसूलम्.'),
    ),
    "5.2.2": (
        _c('vraiheyam — a different affix for two of the grains',
           {'stem': 'vrīhi', 'sense': 'bhavana', 'case': 'ṣaṣṭhī', 'result': 'kṣetra'},
           note='व्रीहिशाल्योर्ढक्, खञोऽपवादः.'),
    ),
    "5.2.3": (
        _c('yavyam — and a third affix for three more',
           {'gana': 'yavādi', 'sense': 'bhavana', 'case': 'ṣaṣṭhī', 'result': 'kṣetra'},
           note='यवयवकषष्टिकाद् यत्, खञोऽपवादः.'),
    ),
    "5.2.4": (
        _c('tilyam, tailīnam — an option, so both affixes stand',
           {'stem': 'tila', 'sense': 'bhavana', 'case': 'ṣaṣṭhī', 'result': 'kṣetra'},
           note='विभाषा तिलमाषोमाभङ्गाणुभ्यः. उमाभङ्गयोरपि धान्यत्वमाश्रितमेव.'),
    ),
    "5.2.5": (
        _c('sarvacarmīṇaḥ — a compound whose members do not agree',
           {'stem': 'sarvacarman', 'sense': 'kṛta', 'case': 'tṛtīyā'},
           note='सर्वचर्मणः कृतः खखञौ. तत्रायमसमर्थसमासो द्रष्टव्यः.'),
    ),
    "5.2.6": (
        _c('yathāmukhīnaḥ — a mirror, or whatever holds a reflection',
           {'stem': 'yathāmukha', 'sense': 'darśana', 'case': 'ṣaṣṭhī'},
           note='यथामुखसंमुखस्य दर्शनः खः. दृश्यतेऽस्मिन्निति दर्शनः.'),
    ),
    "5.2.7": (
        _c('sarvapathīno rathaḥ — a chariot covering the whole road',
           {'pre': 'sarvādi', 'uttarapada': 'pathin-aṅga-karman-patra-pātra', 'sense': 'vyāpnoti', 'case': 'dvitīyā'},
           note='तत्सर्वादेः पथ्यङ्गकर्मपत्रपात्रं व्याप्नोति. परिशिष्टं प्रकृतिविशेषणम्.'),
    ),
    "5.2.8": (
        _c('āprapadīnaḥ paṭaḥ — a cloth reaching the toes',
           {'stem': 'āprapada', 'sense': 'prāpnoti', 'case': 'dvitīyā'},
           note='आप्रपदं प्राप्नोति. शरीरेणासंबद्धस्यापि पटस्य प्रमाणमाख्यायते.'),
    ),
    "5.2.9": (
        _c('anupadīnā upānat — a sandal of the foot measure',
           {'stem': 'anupada', 'sense': 'baddhā', 'case': 'dvitīyā'},
           note='अनुपदसर्वान्नायानयं बद्धाभक्षयतिनेयेषु, यथासंख्यम्.'),
        _c('ayānayīnaḥ śāraḥ — a piece at the head of the board',
           {'stem': 'ayānaya', 'sense': 'neya', 'case': 'dvitīyā'},
           note='अयः प्रदक्षिणम्, अनयः प्रसव्यम्. फलकशिरसि स्थित इत्यर्थः.'),
    ),
    "5.2.10": (
        _c('parovarīṇaḥ — one who lives through high and low',
           {'stem': 'parovara', 'sense': 'anubhavati', 'case': 'dvitīyā'},
           note='परोवरपरम्परपुत्रपौत्रमनुभवति. परस्योत्वं प्रत्ययसंनियोगेन निपात्यते.'),
    ),
    "5.2.11": (
        _c('avārapārīṇaḥ — one who will cross to the far bank',
           {'stem': 'avārapāra', 'sense': 'gāmī', 'case': 'dvitīyā'},
           note='अवारपारात्यन्तानुकामं गामी. विगृहीतादपीष्यते; विपरीताच्च.'),
    ),
    "5.2.12": (
        _c('samāṃsamīnā gauḥ — a cow that calves every year',
           {'stem': 'samāṃsamā', 'sense': 'vijāyate', 'case': 'dvitīyā'},
           note='समांसमां विजायते. गर्भधारणेन सकलापि समा व्याप्यत इति अत्यन्तसंयोगे द्वितीया.'),
    ),
    "5.2.13": (
        _c('adyaśvīnā gauḥ — calving today or tomorrow',
           {'stem': 'adyaśvīna', 'sense': 'avaṣṭabdha'},
           note='अद्यश्वीनावष्टब्धे. आविदूर्ये हि मूर्धन्यो विधीयते.'),
    ),
    "5.2.14": (
        _c('āgavīnaḥ karmakaraḥ — hired until the cow is handed over',
           {'stem': 'go', 'pre': 'āṅ', 'sense': 'karmakārin'},
           note='आगवीनः. यो गवा भृतः कर्म करोति आ तस्य गोः प्रत्यर्पणात्.'),
    ),
    "5.2.15": (
        _c('anugavīno gopālakaḥ — equal to following the cattle',
           {'stem': 'anugu', 'sense': 'alaṃgāmī'},
           note='अनुग्वलंगामी. गोः पश्चाद् अनुगु.'),
    ),
    "5.2.16": (
        _c('adhvanyaḥ, adhvanīnaḥ — one equal to the journey',
           {'stem': 'adhvan', 'sense': 'alaṃgāmī', 'case': 'dvitīyā'},
           note='अध्वनो यत्खौ. ये चाभावकर्मणोः, आत्माध्वानौ खे इति प्रकृतिभावः.'),
    ),
    "5.2.17": (
        _c('abhyamitrīyaḥ — and a third affix beside those two',
           {'stem': 'abhyamitra', 'sense': 'alaṃgāmī', 'case': 'dvitīyā'},
           note='अभ्यमित्राच्छ च. अमित्राभिमुखं सुष्ठु गच्छतीत्यर्थः.'),
    ),
    "5.2.18": (
        _c('gauṣṭhīno deśaḥ — a place that used to be a cow-pen',
           {'stem': 'goṣṭha', 'sense': 'svārtha', 'result': 'bhūtapūrva'},
           note='गोष्ठात् खञ् भूतपूर्वे. भूतपूर्वग्रहणं किम्? गोष्ठो वर्तते.'),
    ),
    "5.2.19": (
        _c('āśvīno ’dhvā — as far as a horse goes in a day',
           {'stem': 'aśva', 'sense': 'ekāhagama', 'case': 'ṣaṣṭhī'},
           note='अश्वस्यैकाहगमः. एकाहेन गम्यत इत्येकाहगमः.'),
    ),
    "5.2.20": (
        _c('śālīno jaḍaḥ — bashful, and derived somehow or other',
           {'stem': 'śālīna', 'sense': 'adhṛṣṭa'},
           note='शालीनकौपीने अधृष्टाकार्ययोः. पर्यायौ यथाकथंचिद् व्युत्पादयितव्यौ.'),
    ),
    "5.2.21": (
        _c('vrātīnaḥ — one OF the troop, not one living off it',
           {'stem': 'vrāta', 'sense': 'jīvati', 'case': 'tṛtīyā'},
           note='व्रातेन जीवति. नानाजातीया अनियतवृत्तय उत्सेधजीविनः संघा व्राताः.'),
    ),
    "5.2.22": (
        _c('sakhyaṃ sāptapadīnam — friendship won in seven steps',
           {'stem': 'sāptapadīna', 'result': 'sakhya'},
           note='साप्तपदीनं सख्यम्. सप्तभिः पदैरवाप्यते साप्तपदीनम्.'),
    ),
    "5.2.23": (
        _c('haiyaṅgavīnam — butter from yesterday milking',
           {'stem': 'hyogodoha', 'result': 'saṃjñā'},
           note='हैयङ्गवीनं संज्ञायाम्. घृतस्य संज्ञा; तेनेह न भवति — ह्योगोदोहस्य विकार उदश्वित्.'),
    ),
    "5.2.24": (
        _c('karṇajāham — the root of a part of the body',
           {'gana': 'karṇādi', 'sense': 'mūla', 'case': 'ṣaṣṭhī'},
           note='तस्य पाकमूले पील्वादिकर्णादिभ्यः कुणब्जाहचौ, यथासंख्यम्.'),
    ),
    "5.2.25": (
        _c('pakṣatiḥ — and only the second of the two senses carries',
           {'stem': 'pakṣa', 'sense': 'mūla', 'case': 'ṣaṣṭhī'},
           note='पक्षात् तिः. एकयोगनिर्दिष्टानामप्येकदेशोऽनुवर्तते.'),
    ),
    "5.2.26": (
        _c('vidyācuñcuḥ — famous for learning',
           {'sense': 'vitta', 'case': 'tṛtīyā'},
           note='तेन वित्तश्चुञ्चुप्चणपौ. वित्तः प्रतीतो ज्ञातः.'),
    ),
    "5.2.27": (
        _c('vinā, nānā — and only where separation is meant',
           {'stem': 'vi', 'sense': 'svārtha', 'result': 'asaha'},
           note='विनञ्भ्यां नानाञौ नसह. न सहेति प्रकृतिविशेषणम्.'),
    ),
    "5.2.28": (
        _c('viśāle, viśaṅkaṭe — of a beast whose horns are gone',
           {'stem': 'vi', 'sense': 'svārtha'},
           note='वेः शालच्छङ्कटचौ. नात्र प्रकृतिप्रत्ययार्थयोरभिनिवेशः.'),
    ),
    "5.2.29": (
        _c('saṃkaṭam, prakaṭam — and eight supplements hang off it',
           {'stem': 'sam', 'sense': 'svārtha'},
           note='संप्रोदश्च कटच्. चकाराद् वेश्च. विकारे स्नेहे तैलच् — एरण्डतैलम्.'),
    ),
    "5.2.30": (
        _c('avakuṭāram, avakaṭam — a conjunction keeping both',
           {'stem': 'ava', 'sense': 'svārtha'},
           note='अवात् कुटारच्च. चकारात् कटच्.'),
    ),
    "5.2.31": (
        _c('avaṭīṭam — three affixes for a flat nose',
           {'stem': 'ava', 'sense': 'nata', 'result': 'saṃjñā', 'samjna': 'nāsikā'},
           note='नते नासिकायाः संज्ञायां टीटञ्नाटज्भ्रटचः. नमनं नतम्; तद्योगाद् नासिकापि, पुरुषोऽपि तथोच्यते.'),
    ),
    "5.2.32": (
        _c('nibiḍam — and thick hair is called so by comparison only',
           {'stem': 'ni', 'sense': 'nata', 'result': 'saṃjñā', 'samjna': 'nāsikā'},
           note='नेर्बिडज्बिरीसचौ. कथं निबिडाः केशाः? उपमानाद् भविष्यति.'),
    ),
    "5.2.33": (
        _c('cikinaḥ, cipiṭaḥ — each affix with its own substitution',
           {'stem': 'ni', 'sense': 'nata', 'result': 'saṃjñā', 'samjna': 'nāsikā', 'wants': 'inac'},
           note='इनच्पिटच्चिकचि च. तत्संनियोगेन च निशब्दस्य यथासंख्यं चिक चि इत्येतावादेशौ भवतः.'),
    ),
    "5.2.34": (
        _c('upatyakā — the land at a mountain foot',
           {'stem': 'upa', 'sense': 'āsanna', 'result': 'saṃjñā'},
           note='उपाधिभ्यां त्यकन्नासन्नारूढयोः. संज्ञाधिकाराच्च नियतविषयमासन्नारूढं गम्यते.'),
    ),
    "5.2.35": (
        _c('karmaṭhaḥ puruṣaḥ — a man who throws himself into it',
           {'stem': 'karman', 'sense': 'ghaṭa', 'case': 'saptamī'},
           note='कर्मणि घटोऽठच्. घटत इति घटः.'),
    ),
    "5.2.36": (
        _c('tārakitaṃ nabhaḥ — a sky that has come to have stars',
           {'gana': 'tārakādi', 'sense': 'saṃjāta', 'case': 'prathamā'},
           note='तदस्य संजातं तारकादिभ्य इतच्. तारकादिराकृतिगणः.'),
    ),
    "5.2.37": (
        _c('ūrudvayasam — water thigh-deep, and a verse divides three',
           {'sense': 'pramāṇa', 'case': 'prathamā'},
           note='प्रमाणे द्वयसज्दघ्नञ्मात्रचः. मात्रच् पुनरविशेषेण प्रस्थमात्रमित्यपि भवति.'),
    ),
    "5.2.38": (
        _c('pauruṣam — four forms, and none after a numeral compound',
           {'stem': 'puruṣa', 'sense': 'pramāṇa', 'case': 'prathamā'},
           note='पुरुषहस्तिभ्यामण् च. द्विगोर्नित्यं लुक् — द्विपुरुषमुदकम्.'),
    ),
    "5.2.39": (
        _c('yāvān, tāvān — and in the Veda, none like you',
           {'stem': 'yad', 'sense': 'parimāṇa', 'case': 'prathamā'},
           note='यत्तदेतेभ्यः परिमाणे वतुप्. युष्मदस्मद्भ्यां छन्दसि सादृश्य उपसंख्यानम्.'),
    ),
    "5.2.40": (
        _c('kiyān, iyān — the affix read out of its own substitute',
           {'stem': 'kim', 'sense': 'parimāṇa', 'case': 'prathamā'},
           note='किमिदंभ्यां वो घः. एतदेव चादेशविधानं ज्ञापकं किमिदंभ्यां वतुप् प्रत्ययो भवतीति.'),
    ),
    "5.2.41": (
        _c('kati brāhmaṇāḥ — a number being determined, not derided',
           {'stem': 'kim', 'sense': 'saṃkhyā-parimāṇa', 'case': 'prathamā'},
           note='किमः संख्यापरिमाणे डति च. क्षेपे हि परिच्छेदो नास्ति — केयमेषां संख्या दशानाम्.'),
    ),
    "5.2.42": (
        _c('pañcatayam — parts belong to a whole, so it names the whole',
           {'samjna': 'saṃkhyā', 'sense': 'avayava', 'case': 'prathamā'},
           note='संख्याया अवयवे तयप्. सामर्थ्यादवयवी प्रत्ययार्थो विज्ञायते.'),
    ),
    "5.2.43": (
        _c('dvayam, dvitayam — a substitute keeps what the original had',
           {'stem': 'dvi', 'samjna': 'saṃkhyā', 'sense': 'avayava', 'case': 'prathamā'},
           note='द्वित्रिभ्यां तयस्यायज् वा. तयग्रहणं स्थानिनिर्देशार्थम्; अन्यथा त्रयी गतिरिति ईकारो न स्यात्.'),
    ),
    "5.2.44": (
        _c('ubhayo maṇiḥ — obligatory, and accented on the first',
           {'stem': 'ubha', 'samjna': 'saṃkhyā', 'sense': 'avayava', 'case': 'prathamā'},
           note='उभादुदात्तो नित्यम्. वचनसामर्थ्यादादेरुदात्तत्वं विज्ञायते.'),
    ),
    "5.2.45": (
        _c('ekādaśaṃ śatam — a hundred and eleven, of the same kind',
           {'uttarapada': 'daśan', 'sense': 'adhika', 'case': 'prathamā'},
           note='तदस्मिन्नधिकमिति दशान्ताड् डः. प्रत्ययार्थेन च समानजातीये प्रकृत्यर्थे सति प्रत्यय इष्यते.'),
    ),
    "5.2.46": (
        _c('triṃśaṃ śatam — and *numeral* keeps a look-alike out',
           {'stem_final': 'śad-viṃśati', 'sense': 'adhika', 'case': 'prathamā'},
           note='शदन्तविंशतेश्च. संख्याग्रहणं च कर्तव्यम्; इह मा भूद् — गोत्रिंशदधिका अस्मिन् गोशते.'),
    ),
    "5.2.47": (
        _c('dvimayam udaśvid yavānām — four conditions, none stated',
           {'samjna': 'saṃkhyā', 'sense': 'guṇa-nimāna', 'case': 'prathamā'},
           note='संख्याया गुणस्य निमाने मयट्. गुणो भागः; निमानं मूल्यम्. गुणशब्दः समानावयववचनः.'),
    ),
    "5.2.48": (
        _c('ekādaśaḥ — what fills a count out, and starts a new one',
           {'samjna': 'saṃkhyā', 'sense': 'pūraṇa', 'case': 'ṣaṣṭhī'},
           note='तस्य पूरणे डट्. यस्मिन्नुपसंजातेऽन्या संख्या संपद्यते, स प्रत्ययार्थः.'),
    ),
    "5.2.49": (
        _c('pañcamaḥ, saptamaḥ — an insert, and the case it needs',
           {'samjna': 'saṃkhyā', 'stem_final': 'n', 'sense': 'pūraṇa', 'case': 'ṣaṣṭhī'},
           note='नान्तादसंख्यादेर्मट्. नान्तादिति पञ्चमी डट आगमसंबन्धे षष्ठीं प्रकल्पयति.'),
    ),
    "5.2.50": (
        _c('pañcathāni — a second insert, and the first still stands',
           {'samjna': 'saṃkhyā', 'stem_final': 'n', 'sense': 'pūraṇa', 'case': 'ṣaṣṭhī', 'usage': 'chandasi'},
           note='थट् च छन्दसि. चकारात् पक्षे मडपि भवति.'),
    ),
    "5.2.51": (
        _c('ṣaṣṭhaḥ, caturthaḥ — and one of the four is no numeral',
           {'stem': 'ṣaṣ', 'samjna': 'saṃkhyā', 'sense': 'pūraṇa', 'case': 'ṣaṣṭhī'},
           note='षट्कतिकतिपयचतुरां थुक्. कतिपयशब्दो न संख्या, तस्यास्मादेव ज्ञापकाद् डट् प्रत्ययो विज्ञायते.'),
    ),
    "5.2.52": (
        _c('bahutithaḥ — the same reading made a second time',
           {'stem': 'bahu', 'sense': 'pūraṇa', 'case': 'ṣaṣṭhī'},
           note='बहुपूगगणसंघस्य तिथुक्. पूगसंघशब्दयोरसंख्यात्वादिदमेव ज्ञापकं डटो भावस्य.'),
    ),
    "5.2.53": (
        _c('yāvatithaḥ — a numeral already, so only the insert is new',
           {'samjna': 'saṃkhyā', 'stem_final': 'vatu', 'sense': 'pūraṇa', 'case': 'ṣaṣṭhī'},
           note='वतोरिथुक्. वत्वन्तस्य संख्यात्वात् पूर्वेण डड् विहितः.'),
    ),
    "5.2.54": (
        _c('dvitīyaḥ — a different ordinal affix for the word two',
           {'stem': 'dvi', 'samjna': 'saṃkhyā', 'sense': 'pūraṇa', 'case': 'ṣaṣṭhī'},
           note='द्वेस्तीयः, डटोऽपवादः.'),
    ),
    "5.2.55": (
        _c('tṛtīyaḥ — and a vowel change yoked to the affix',
           {'stem': 'tri', 'samjna': 'saṃkhyā', 'sense': 'pūraṇa', 'case': 'ṣaṣṭhī'},
           note='त्रेः संप्रसारणं च. हलः इति संप्रसारणस्य दीर्घत्वं न भवति.'),
    ),
    "5.2.56": (
        _c('viṃśatitamaḥ, viṃśaḥ — an optional insert, so both stand',
           {'gana': 'viṃśatyādi', 'samjna': 'saṃkhyā', 'sense': 'pūraṇa', 'case': 'ṣaṣṭhī'},
           note='विंशत्यादिभ्यस्तमडन्यतरस्याम्. विंशत्यादयो लौकिकाः संख्याशब्दा गृह्यन्ते, न पङ्क्त्यादिसूत्रसंनिविष्टाः.'),
    ),
    "5.2.57": (
        _c('śatatamaḥ, māsatamo divasaḥ — and here it is obligatory',
           {'gana': 'śatādi', 'samjna': 'saṃkhyā', 'sense': 'pūraṇa', 'case': 'ṣaṣṭhī'},
           note='नित्यं शतादिमासार्धमाससंवत्सराच्च. मासादयः संख्याशब्दा न भवन्ति, तेभ्योऽस्मादेव ज्ञापकाद् डट् प्रत्ययो विज्ञायते.'),
    ),
    "5.2.58": (
        _c('ṣaṣṭitamaḥ — unless a numeral stands first',
           {'gana': 'ṣaṣṭyādi', 'samjna': 'saṃkhyā', 'sense': 'pūraṇa', 'case': 'ṣaṣṭhī'},
           note='षष्ट्यादेश्चासंख्यादेः. असंख्यादेरिति किम्? एकषष्टः, एकषष्टितमः.'),
    ),
    "5.2.59": (
        _c('acchāvākīyaṃ sūktam — one word supplying case and sense',
           {'sense': 'matvartha', 'result': 'sūkta-sāman'},
           note='मतौ छः सूक्तसाम्नोः. मत्वर्थग्रहणेन समर्थविभक्तिः, प्रकृतिविशेषणं प्रत्ययार्थ इति सर्वमाक्षिप्यते.'),
    ),
    "5.2.60": (
        _c('gardabhāṇḍo ’dhyāyaḥ — a removal that proves a giving',
           {'sense': 'matvartha', 'result': 'adhyāya-anuvāka'},
           note='अध्यायानुवाकयोर्लुक्. इदमेव लुग्वचनं ज्ञापकं तद्विधानस्य.'),
    ),
    "5.2.61": (
        _c('vaimukto ’dhyāyaḥ — a different affix for the same thing',
           {'gana': 'vimuktādi', 'sense': 'matvartha', 'result': 'adhyāya-anuvāka'},
           note='विमुक्तादिभ्योऽण्.'),
    ),
    "5.2.62": (
        _c('goṣadako ’dhyāyaḥ — named from its own opening words',
           {'gana': 'goṣadādi', 'sense': 'matvartha', 'result': 'adhyāya-anuvāka'},
           note='गोषदादिभ्यो वुन्.'),
    ),
    "5.2.63": (
        _c('pathi kuśalaḥ pathakaḥ — one who knows the road',
           {'stem': 'pathin', 'sense': 'kuśala', 'case': 'saptamī'},
           note='तत्र कुशलः पथः.'),
    ),
    "5.2.64": (
        _c('ākarṣe kuśala ākarṣakaḥ — kan, for a dozen senses to come',
           {'gana': 'ākarṣādi', 'sense': 'kuśala', 'case': 'saptamī'},
           note='आकर्षादिभ्यः कन्.'),
    ),
    "5.2.65": (
        _c('dhane kāmo dhanakaḥ — one who wants it',
           {'stem': 'dhana', 'sense': 'kāma', 'case': 'saptamī'},
           note='धनहिरण्यात् कामे. काम इच्छा अभिलाषः.'),
    ),
    "5.2.66": (
        _c('keśakaḥ — a man always at his hair',
           {'samjna': 'svāṅga', 'sense': 'prasita', 'case': 'saptamī'},
           note='स्वाङ्गेभ्यः प्रसिते. बहुवचनं स्वाङ्गसमुदायशब्दादपि यथा स्यात्.'),
    ),
    "5.2.67": (
        _c('audarika ādyūnaḥ — one who cannot master his belly',
           {'stem': 'udara', 'sense': 'prasita', 'case': 'saptamī', 'result': 'ādyūna'},
           note='उदराट् ठगाद्यूने. यो बुभुक्षयात्यन्तं पीड्यते, स एवमुच्यते. आद्यून इति किम्? उदरकः.'),
    ),
    "5.2.68": (
        _c('sasyako maṇiḥ — flawless from the mine',
           {'stem': 'sasya', 'sense': 'parijāta', 'case': 'tṛtīyā'},
           note='सस्येन परिजातः. यस्य किंचिदपि वैगुण्यं नास्ति, तस्येदमभिधानम्.'),
    ),
    "5.2.69": (
        _c('aṃśako dāyādaḥ — an heir with a share coming',
           {'stem': 'aṃśa', 'sense': 'hārin', 'case': 'dvitīyā'},
           note='अंशं हारी. हारीत्यावश्यके णिनिः; तत्र षष्ठीप्रतिषेधात् कर्मणि द्वितीयैव भवति.'),
    ),
    "5.2.70": (
        _c('tantrakaḥ paṭaḥ — cloth fresh from the loom',
           {'stem': 'tantra', 'sense': 'acirāpahṛta', 'case': 'pañcamī'},
           note='तन्त्रादचिरापहृते. अचिरापहृतः स्तोककालापहृत इत्यर्थः.'),
    ),
    "5.2.71": (
        _c('brāhmaṇako deśaḥ — where the brahmins live by arms',
           {'stem': 'brāhmaṇaka', 'result': 'saṃjñā'},
           note='ब्राह्मणकोष्णिके संज्ञायाम्. यत्रायुधजीविनो ब्राह्मणाः सन्ति, तस्य ब्राह्मणक इति संज्ञा.'),
    ),
    "5.2.72": (
        _c('śītakaḥ, uṣṇakaḥ — cold for slow, hot for brisk',
           {'stem': 'śīta', 'sense': 'kārin', 'case': 'dvitīyā'},
           note='शीतोष्णाभ्यां कारिणि. क्रियाविशेषणाद् द्वितीयासमर्थादयं प्रत्ययः.'),
    ),
    "5.2.73": (
        _c('adhiko droṇaḥ khāryām — and it works both ways round',
           {'stem': 'adhyārūḍha', 'sense': 'adhika'},
           note='अधिकम्. अध्यारूढशब्दस्योत्तरपदलोपः कंश्च प्रत्ययः; कर्तरि कर्मणि चाध्यारूढशब्दः.'),
    ),
    "5.2.74": (
        _c('anukaḥ, abhikaḥ, abhīkaḥ — three forms for one who wants',
           {'stem': 'anu', 'sense': 'kamitṛ'},
           note='अनुकाभिकाभीकः कमिता. अभेः पक्षे दीर्घत्वं च निपात्यते.'),
    ),
    "5.2.75": (
        _c('pārśvakaḥ — one who seeks his ends by crooked means',
           {'stem': 'pārśva', 'sense': 'anvicchati', 'case': 'tṛtīyā'},
           note='पार्श्वेनान्विच्छति. अनृजुरुपायः पार्श्वम्; मायावी कौसृतिको जालिक उच्यते.'),
    ),
    "5.2.76": (
        _c('āyaḥśūlikaḥ — an iron spike, for a man of violence',
           {'stem': 'ayaḥśūla', 'sense': 'anvicchati', 'case': 'tṛtīyā'},
           note='अयःशूलदण्डाजिनाभ्यां ठक्ठञौ. तीक्ष्ण उपायोऽयःशूलमुच्यते; दम्भो दण्डाजिनम्.'),
    ),
    "5.2.77": (
        _c('dvikaṃ grahaṇam — from a word an ordinal affix already made',
           {'samjna': 'pūraṇānta', 'sense': 'svārtha', 'result': 'grahaṇa'},
           note='तावतिथं ग्रहणमिति लुग् वा. इतिकरणो विवक्षार्थः; तेन ग्रन्थविषयमेव ग्रहणं विज्ञायते.'),
    ),
    "5.2.78": (
        _c('devadattakāḥ — a leader, not merely a shared acquaintance',
           {'sense': 'grāmaṇī', 'case': 'prathamā'},
           note='स एषां ग्रामणीः. ग्रामणीरिति किम्? देवदत्तः शत्रुरेषाम्.'),
    ),
    "5.2.79": (
        _c('śṛṅkhalakaḥ — the hobble that takes its freedom away',
           {'stem': 'śṛṅkhala', 'sense': 'bandhana', 'case': 'prathamā', 'result': 'karabha'},
           note='शृङ्खलमस्य बन्धनं करभे. उष्ट्राणां बालकाः करभाः.'),
    ),
    "5.2.80": (
        _c('utkaḥ pravāsī — a man away from home and longing',
           {'stem': 'ud', 'sense': 'unmanas'},
           note='उत्क उन्मनाः. उद्गतं मनो यस्य स उन्मनाः.'),
    ),
    "5.2.81": (
        _c('dvitīyako jvaraḥ — a fever of the second day',
           {'sense': 'roga'},
           note='कालप्रयोजनाद् रोगे. उत्तरसूत्रादिह संज्ञाग्रहणमपकृष्यते.'),
    ),
    "5.2.82": (
        _c('guḍāpūpikā paurṇamāsī — a day of molasses cakes',
           {'sense': 'anna', 'case': 'prathamā', 'result': 'prāya-saṃjñā'},
           note='तदस्मिन्नन्नं प्राये संज्ञायाम्. प्रायो बाहुल्यम्.'),
    ),
    "5.2.83": (
        _c('kaulmāṣī paurṇamāsī — a different affix, one word',
           {'stem': 'kulmāṣa', 'sense': 'anna', 'case': 'prathamā', 'result': 'prāya-saṃjñā'},
           note='कुल्माषादञ्. ञकारो वृद्धिस्वरार्थः.'),
    ),
    "5.2.84": (
        _c('śrotriyo brāhmaṇaḥ — one word for a whole sentence',
           {'stem': 'chandas', 'sense': 'adhīta'},
           note='श्रोत्रियंश्छन्दोऽधीते. वाक्यार्थे पदवचनम्.'),
    ),
    "5.2.85": (
        _c('śrāddhī — and only of the day he ate',
           {'stem': 'śrāddha', 'sense': 'anena', 'result': 'bhukta'},
           note='श्राद्धमनेन भुक्तमिनिठनौ. इनिठनोः समानकालग्रहणम्.'),
    ),
    "5.2.86": (
        _c('pūrvī — and an agent needs an action supplied',
           {'stem': 'pūrva', 'sense': 'anena'},
           note='पूर्वादिनिः. यां कांचित् क्रियामध्याहृत्य प्रत्ययो विधेयः.'),
    ),
    "5.2.87": (
        _c('kṛtapūrvī kaṭam — and two paribhāṣās read out of it',
           {'uttarapada': 'pūrva', 'sense': 'anena'},
           note='सपूर्वाच्च. योगद्वयेन चानेन परिभाषाद्वयं ज्ञाप्यते.'),
    ),
    "5.2.88": (
        _c('iṣṭī yajñe — a list of past participles',
           {'gana': 'iṣṭādi', 'sense': 'anena'},
           note='इष्टादिभ्यश्च. क्तस्येन्विषयस्य कर्मणि इति सप्तम्युपसंख्यायते.'),
    ),
    "5.2.89": (
        _c('paripanthinaḥ — one who stands in the way',
           {'stem': 'paripanthin', 'sense': 'paryavasthātṛ', 'usage': 'chandasi'},
           note='छन्दसि परिपन्थिपरिपरिणौ पर्यवस्थातरि. पर्यवस्थाता प्रतिपक्षः सपत्न उच्यते.'),
    ),
    "5.2.90": (
        _c('anupadī gavām — one who follows cattle to find them',
           {'stem': 'anupadī', 'sense': 'anveṣṭṛ'},
           note='अनुपद्यन्वेष्टा. पदस्य पश्चादनुपदम्.'),
    ),
    "5.2.91": (
        _c('sākṣī — the onlooker, not the man who gives evidence',
           {'stem': 'sākṣāt', 'sense': 'draṣṭṛ', 'result': 'saṃjñā'},
           note='साक्षाद् द्रष्टरि संज्ञायाम्. संज्ञाग्रहणादुपद्रष्टैवोच्यते, न दाता ग्रहीता वा.'),
    ),
    "5.2.92": (
        _c('kṣetriyo vyādhiḥ — four readings, and all authoritative',
           {'stem': 'parakṣetra', 'sense': 'cikitsya', 'case': 'saptamī'},
           note='क्षेत्रियच् परक्षेत्रे चिकित्स्यः. सर्वं चैतत् प्रमाणम्.'),
    ),
    "5.2.93": (
        _c('indriyam — six derivations, and none of them binding',
           {'stem': 'indra', 'sense': 'indriya'},
           note='इन्द्रियमिन्द्रलिङ्गम्…इति वा. रूढिरेषा चक्षुरादीनां करणानाम्; व्युत्पत्तेरनियमं दर्शयति.'),
    ),
    "5.2.94": (
        _c('gomān devadattaḥ — and a verse names seven grounds',
           {'stem': 'go', 'sense': 'asti', 'case': 'prathamā'},
           note='तदस्यास्त्यस्मिन्निति मतुप्. भूमनिन्दाप्रशंसासु नित्ययोगेऽतिशायने संसर्गेऽस्तिविवक्षायां भवन्ति मतुबादयः.'),
    ),
    "5.2.95": (
        _c('rasavān — stated again to shut the other affixes out',
           {'gana': 'rasādi', 'sense': 'asti', 'case': 'prathamā'},
           note='रसादिभ्यश्च. रसादिभ्यः पुनर्वचनमन्यनिवृत्त्यर्थम्; अन्ये मत्वर्थीया मा भूवन्.'),
    ),
    "5.2.96": (
        _c('cūḍālaḥ, cūḍāvān — and a lamp crest is not a limb',
           {'samjna': 'prāṇyaṅga', 'stem_final': 'ā', 'sense': 'asti', 'case': 'prathamā'},
           note='प्राणिस्थादातो लजन्यतरस्याम्. प्राणिस्थादिति किम्? शिखावान् प्रदीपः.'),
    ),
    "5.2.97": (
        _c('sidhmalaḥ, sidhmavān — the option gathers rather than picks',
           {'gana': 'sidhmādi', 'sense': 'asti', 'case': 'prathamā'},
           note='सिध्मादिभ्यश्च. अन्यतरस्यांग्रहणेन मतुप् समुच्चीयते न तु प्रत्ययो विकल्प्यते.'),
    ),
    "5.2.98": (
        _c('vatsalaḥ pitā — and the calf is not in the word at all',
           {'stem': 'vatsa', 'sense': 'asti', 'result': 'kāmavat'},
           note='वत्सांसाभ्यां कामबले. न ह्यत्र वत्सार्थोंऽसार्थो वा विद्यते; न चायमर्थो मतुपि संभवति.'),
    ),
    "5.2.99": (
        _c('phenilaḥ, phenalaḥ, phenavān — three forms',
           {'stem': 'phena', 'sense': 'asti'},
           note='फेनादिलच् च. अन्यतरस्यांग्रहणं मतुप्समुच्चयार्थं सर्वत्रैवानुवर्तते.'),
    ),
    "5.2.100": (
        _c('lomaśaḥ — three affixes for three lists, in order',
           {'gana': 'lomādi', 'sense': 'asti'},
           note='लोमादिपामादिपिच्छादिभ्यः शनेलचः, यथासंख्यम्.'),
    ),
    "5.2.101": (
        _c('prājñaḥ, prajñāvān — and the general affix beside it',
           {'stem': 'prajñā', 'sense': 'asti'},
           note='प्रज्ञाश्रद्धार्चाभ्यो णः. मतुप् सर्वत्र समुच्चीयते.'),
    ),
    "5.2.102": (
        _c('tapasvī — and the two are not matched to the two words',
           {'stem': 'tapas', 'sense': 'asti'},
           note='तपःसहस्राभ्यां विनीनी. यथासंख्यं सर्वत्रैवास्मिन् प्रकरणे नेष्यते.'),
    ),
    "5.2.103": (
        _c('tāpasaḥ, sāhasraḥ — a split serving two purposes',
           {'stem': 'tapas', 'sense': 'asti', 'wants': 'aṇ'},
           note='अण् च. योगविभाग उत्तरार्थो यथासंख्यार्थश्च.'),
    ),
    "5.2.104": (
        _c('saikato ghaṭaḥ — a sandy pot, deliberately not a place',
           {'stem': 'sikatā', 'sense': 'asti'},
           note='सिकताशर्कराभ्यां च. अदेश इहोदाहरणम्; देशे तु लुबिलचौ भविष्यतः.'),
    ),
    "5.2.105": (
        _c('sikatā deśaḥ — and any of the affixes may be the one lost',
           {'stem': 'sikatā', 'sense': 'asti', 'result': 'deśa'},
           note='देशे लुबिलचौ च. कस्य पुनरयं लुप्? मतुबादीनामन्यतमस्य, विशेषाभावात्.'),
    ),
    "5.2.106": (
        _c('danturaḥ — buck-toothed, and prominence is the condition',
           {'stem': 'danta', 'sense': 'asti', 'result': 'unnata'},
           note='दन्त उन्नत उरच्. उन्नत इति प्रकृतिविशेषणम्. उन्नत इति किम्? दन्तवान्.'),
    ),
    "5.2.107": (
        _c('ūṣaraṃ kṣetram — saline ground, and not salt in a pot',
           {'stem': 'ūṣa', 'sense': 'asti'},
           note='ऊषसुषिमुष्कमधो रः. इतिकरणो विवक्षार्थः सर्वत्राभिधेयनियमं करोति.'),
    ),
    "5.2.108": (
        _c('dyumaḥ, drumaḥ — settled names, so no second form',
           {'stem': 'dyu', 'sense': 'asti'},
           note='द्युद्रुभ्यां मः. रूढिशब्दावेतौ; रूढिषु मतुप् पुनर्न विकल्प्यते.'),
    ),
    "5.2.109": (
        _c('keśavaḥ, keśī, keśikaḥ, keśavān — four forms',
           {'stem': 'keśa', 'sense': 'asti'},
           note='केशाद् वोऽन्यतरस्याम्. अनेन त्विनिठनौ प्राप्येते; ततश्चातूरूप्यं भवति.'),
    ),
    "5.2.110": (
        _c('gāṇḍīvaṃ dhanuḥ — and the rule framed to be read two ways',
           {'stem': 'gāṇḍī', 'sense': 'asti', 'result': 'saṃjñā'},
           note='गाण्ड्यजगात् संज्ञायाम्. तुल्या हि संहिता दीर्घह्रस्वयोः; उभयथा च सूत्रं प्रणीतम्.'),
    ),
    "5.2.111": (
        _c('kāṇḍīraḥ, aṇḍīraḥ — two affixes, two words, in order',
           {'stem': 'kāṇḍa', 'sense': 'asti'},
           note='काण्डाण्डादीरन्नीरचौ.'),
    ),
    "5.2.112": (
        _c('kṛṣīvalaḥ kuṭumbī — a householder who ploughs',
           {'gana': 'rajaḥprabhṛti', 'sense': 'asti'},
           note='रजःकृष्यासुतिपरिषदो वलच्. इतिकरणो विषयनियमार्थः सर्वत्र संबध्यते.'),
    ),
    "5.2.113": (
        _c('dantāvalo gajaḥ — an elephant, named from its tusks',
           {'stem': 'danta', 'sense': 'asti', 'result': 'saṃjñā'},
           note='दन्तशिखात् संज्ञायाम्.'),
    ),
    "5.2.114": (
        _c('jyotsnā, tamisrā rātriḥ — eight forms, eight irregularities',
           {'gana': 'jyotsnādi', 'sense': 'asti', 'result': 'saṃjñā'},
           note='ज्योत्स्नातमिस्रा…. स्त्रीत्वमतन्त्रम्; अन्यत्रापि दृश्यते — तमिस्रं नभः.'),
    ),
    "5.2.115": (
        _c('daṇḍī, daṇḍikaḥ, daṇḍavān — and a verse names four bars',
           {'stem_final': 'a', 'sense': 'asti'},
           note='अत इनिठनौ. एकाक्षरात् कृतो जातेः सप्तम्यां च न तौ स्मृतौ.'),
    ),
    "5.2.116": (
        _c('vrīhī, vrīhikaḥ, vrīhimān — and the list is not uniform',
           {'gana': 'vrīhyādi', 'sense': 'asti'},
           note='व्रीह्यादिभ्यश्च. शिखादिभ्य इनिर्वाच्य इकन् यवखदादिषु; परिशिष्टेभ्य उभयम्.'),
    ),
    "5.2.117": (
        _c('tundilaḥ, tundī, tundikaḥ, tundavān — four at once',
           {'gana': 'tundādi', 'sense': 'asti'},
           note='तुन्दादिभ्य इलच् च. स्वाङ्गाद् विवृद्धौ च.'),
    ),
    "5.2.118": (
        _c('aikaśatikaḥ — and *always* keeps the general affix out',
           {'pre': 'eka-go', 'stem_final': 'a', 'sense': 'asti'},
           note='एकगोपूर्वाट् ठञ् नित्यम्. नित्यग्रहणं मतुपो बाधनार्थम्.'),
    ),
    "5.2.119": (
        _c('naiṣkaśatikaḥ — and no other word may stand in front',
           {'uttarapada': 'śata-sahasra', 'pre': 'niṣka', 'sense': 'asti'},
           note='शतसहस्रान्ताच्च निष्कात्. सुवर्णनिष्कशतमस्तीत्यनभिधानाद् न भवति.'),
    ),
    "5.2.120": (
        _c('rūpyo dīnāraḥ — a struck coin, and a handsome man',
           {'stem': 'rūpa', 'sense': 'asti', 'result': 'āhata-praśaṃsā'},
           note='रूपादाहतप्रशंसयोर्यप्. आहतप्रशंसयोरिति किम्? रूपवान्.'),
    ),
    "5.2.121": (
        _c('yaśasvī, medhāvī — a sound, and three named words',
           {'stem_final': 'as', 'sense': 'asti'},
           note='असो मायामेधास्रजो विनिः. मतुप् सर्वत्र समुच्चीयत एव.'),
    ),
    "5.2.122": (
        _c('tejasvin — and one word carrying eight supplements',
           {'sense': 'asti', 'usage': 'chandasi'},
           note='बहुलं छन्दसि. तदेतत् सर्वं बहुलग्रहणेन सम्पद्यते.'),
    ),
    "5.2.123": (
        _c('ūrṇāyuḥ — and one letter makes the result a word',
           {'stem': 'ūrṇā', 'sense': 'asti'},
           note='ऊर्णाया युस्. सकारः पदसंज्ञार्थः.'),
    ),
    "5.2.124": (
        _c('vāggmī — eloquent',
           {'stem': 'vāc', 'sense': 'asti'},
           note='वाचो ग्मिनिः.'),
    ),
    "5.2.125": (
        _c('vācālaḥ, vācāṭaḥ — the garrulous, not the fluent',
           {'stem': 'vāc', 'sense': 'asti', 'result': 'bahubhāṣin-kutsita'},
           note='आलजाटचौ बहुभाषिणि. कुत्सित इति वक्तव्यम्; यो हि सम्यग् बहु भाषते, वाग्ग्मीत्येव स भवति.'),
    ),
    "5.2.126": (
        _c('svāmī — lordship, not merely property',
           {'stem': 'sva', 'sense': 'asti', 'result': 'aiśvarya'},
           note='स्वामिन्नैश्वर्ये. ऐश्वर्य इति किम्? स्ववान्.'),
    ),
    "5.2.127": (
        _c('arśasaḥ, urasaḥ — a list defined by what its members do',
           {'gana': 'arśaādi', 'sense': 'asti'},
           note='अर्शआदिभ्योऽच्. यत्राभिन्नरूपेण शब्देन तद्वतोऽभिधानं तत् सर्वमिह द्रष्टव्यम्.'),
    ),
    "5.2.128": (
        _c('kaṭakavalayinī, kuṣṭhī — and a tree is not a living body',
           {'samjna': 'prāṇistha', 'stem_final': 'a', 'sense': 'asti', 'result': 'dvandva-upatāpa-garhya'},
           note='द्वन्द्वोपतापगर्ह्यात् प्राणिस्थादिनिः. प्राणिस्थादिति किम्? पुष्पफलवान् वृक्षः.'),
    ),
    "5.2.129": (
        _c('vātakī, atisārakī — the rule is for the insert alone',
           {'stem': 'vāta', 'sense': 'asti', 'result': 'upatāpa'},
           note='वातातिसाराभ्यां कुक् च. पूर्वेणैव सिद्धे प्रत्यये कुगर्थमेवेदं वचनम्.'),
    ),
    "5.2.130": (
        _c('pañcamī uṣṭraḥ — a camel in its fifth year',
           {'samjna': 'pūraṇānta', 'sense': 'asti', 'result': 'vayas'},
           note='वयसि पूरणात्. सिद्धे सति नियमार्थं वचनम्. वयसीति किम्? पञ्चमवान् ग्रामरागः.'),
    ),
    "5.2.131": (
        _c('sukhī, duḥkhī — and one entry shuts a rival out',
           {'gana': 'sukhādi', 'sense': 'asti'},
           note='सुखादिभ्यश्च. माला क्षेप इति पठ्यते; तदिह क्षेपे मतुब्बाधनार्थं वचनम्.'),
    ),
    "5.2.132": (
        _c('brāhmaṇadharmī — *ending in* going with each of three',
           {'uttarapada': 'dharma-śīla-varṇa', 'sense': 'asti'},
           note='धर्मशीलवर्णान्ताच्च. अन्तशब्दः प्रत्येकमभिसंबध्यते.'),
    ),
    "5.2.133": (
        _c('hastī — and a man with hands is not a kind of thing',
           {'stem': 'hasta', 'sense': 'asti', 'result': 'jāti'},
           note='हस्ताज् जातौ. जाताविति किम्? हस्तवान् पुरुषः.'),
    ),
    "5.2.134": (
        _c('varṇī — one initiated, who keeps the observances',
           {'stem': 'varṇa', 'sense': 'asti', 'result': 'brahmacārin'},
           note='वर्णाद् ब्रह्मचारिणि. ब्रह्मचारिणीति किम्? वर्णवान्.'),
    ),
    "5.2.135": (
        _c('puṣkariṇī — a lotus-pond, and not an elephant with a lotus',
           {'gana': 'puṣkarādi', 'sense': 'asti', 'result': 'deśa'},
           note='पुष्करादिभ्यो देशे. देश इति किम्? पुष्करवान् हस्ती.'),
    ),
    "5.2.136": (
        _c('balavān, balī — and the two affixes change places',
           {'gana': 'balādi', 'sense': 'asti'},
           note='बलादिभ्यो मतुबन्यतरस्याम्. अन्यतरस्यांग्रहणेन प्रकृत इनिः समुच्चीयते.'),
    ),
    "5.2.137": (
        _c('prathiminī, sominī — where the whole word is a name',
           {'stem_final': 'man-ma', 'sense': 'asti', 'result': 'saṃjñā'},
           note='संज्ञायां मन्माभ्याम्. संज्ञायामिति किम्? सोमवान्, होमवान्.'),
    ),
    "5.2.138": (
        _c('kambaḥ, śambaḥ, kaṃyuḥ — seven affixes in one rule',
           {'stem': 'kam', 'sense': 'asti'},
           note='कंशंभ्यां बभयुस्तितुतयसः. सकारः पदसंज्ञार्थः, तेनानुस्वारपरसवर्णौ सिद्धौ भवतः.'),
    ),
    "5.2.139": (
        _c('tundibhaḥ — from a word meaning a swollen navel',
           {'stem': 'tundi', 'sense': 'asti'},
           note='तुन्दिबलिवटेर्भः. तुन्दिरिति वृद्धा नाभिरुच्यते.'),
    ),
    "5.2.140": (
        _c('ahaṃyuḥ, śubhaṃyuḥ — and the quarter ends',
           {'stem': 'aham', 'sense': 'asti'},
           note='अहंशुभमोर्युस्. अहमिति शब्दान्तरमहंकारे वर्तते; अहंकारवानित्यर्थः.'),
    ),
    "5.3.1": (
        _c('iha — a heading that supplies a NAME and no affix',
           {'stem': 'idam', 'case': 'saptamī'},
           note='प्राग्दिशो विभक्तिः. अतः परं स्वार्थिकाः प्रत्ययाः; समर्थाधिकारः प्रथमग्रहणं च द्वयमपि निवृत्तम्.'),
    ),
    "5.3.2": (
        _c('kutaḥ, bahutaḥ — and the numerals are kept out',
           {'stem': 'kim', 'samjna': 'sarvanāman', 'case': 'pañcamī'},
           note='किंसर्वनामबहुभ्योऽद्व्यादिभ्यः. अद्व्यादिभ्य इति किम्? द्वाभ्याम्, द्वयोः.'),
    ),
    "5.3.3": (
        _c('iha — the whole word replaced, not its last sound',
           {'stem': 'idam'},
           note='इदम इश्. शकारः सर्वादेशार्थः.'),
    ),
    "5.3.4": (
        _c('etarhi, ittham — two substitutes before two sounds',
           {'stem': 'idam', 'before': 'r-th'},
           note='एतेतौ रथोः, इशोऽपवादः. रेफेऽकार उच्चारणार्थः.'),
    ),
    "5.3.5": (
        _c('ataḥ, atra — and the rule split to reach two more forms',
           {'stem': 'etad'},
           note='एतदोऽन्. एतद इति योगविभागः कर्तव्यः.'),
    ),
    "5.3.6": (
        _c('sarvadā, sadā — and only before an affix of this section',
           {'stem': 'sarva', 'before': 'd'},
           note='सर्वस्य सोऽन्यतरस्यां दि. प्राग्दिशीय इत्येव — सर्वं ददातीति सर्वदा ब्राह्मणी.'),
    ),
    "5.3.7": (
        _c('kutaḥ beside kasmāt — an ablative replaced',
           {'stem': 'kim', 'samjna': 'sarvanāman', 'case': 'pañcamī'},
           note='पञ्चम्यास्तसिल्.'),
    ),
    "5.3.8": (
        _c('kuta āgataḥ — and here another affix is replaced',
           {'stem': 'kim', 'samjna': 'sarvanāman', 'case': 'pañcamī', 'wants': 'tasil'},
           note='तसेश्च. तसेस्तसिल्वचनं स्वरार्थं विभक्त्यर्थं च.'),
    ),
    "5.3.9": (
        _c('paritaḥ, abhitaḥ — all round, and on both sides',
           {'stem': 'pari'},
           note='पर्यभिभ्यां च. सर्वोभयार्थे वर्तमानाभ्यां प्रत्यय इष्यते.'),
    ),
    "5.3.10": (
        _c('kutra, yatra, tatra — a locative replaced',
           {'stem': 'kim', 'samjna': 'sarvanāman', 'case': 'saptamī'},
           note='सप्तम्यास्त्रल्.'),
    ),
    "5.3.11": (
        _c('iha — one pronoun taking a different affix',
           {'stem': 'idam', 'case': 'saptamī'},
           note='इदमो हः, त्रलोऽपवादः.'),
    ),
    "5.3.12": (
        _c('kva bhokṣyase — and a word dragged backward for kutra',
           {'stem': 'kim', 'case': 'saptamī', 'wants': 'at'},
           note='किमोऽत्, त्रलोऽपवादः. उत्तरसूत्राद् वावचनं पुरस्तादपकृष्यते.'),
    ),
    "5.3.13": (
        _c('kva, kuha — a Vedic affix beside the ordinary ones',
           {'stem': 'kim', 'case': 'saptamī', 'usage': 'chandasi'},
           note='वा ह च छन्दसि. यथाप्राप्तं च.'),
    ),
    "5.3.14": (
        _c('tato bhavān — from the other cases, and only politely',
           {'stem': 'tad', 'samjna': 'sarvanāman', 'wants': 'tasil'},
           note='इतराभ्योऽपि दृश्यन्ते. दृशिग्रहणं प्रायिकविध्यर्थम्; भवदादिभिर्योग एवैतद्विधानम्.'),
    ),
    "5.3.15": (
        _c('sarvadā, kadā, tadā — of a time, not of a place',
           {'stem': 'sarva', 'case': 'saptamī', 'result': 'kāla'},
           note='सर्वैकान्यकिंयत्तदः काले दा, त्रलोऽपवादः. काल इति किम्? सर्वत्र देशे.'),
    ),
    "5.3.16": (
        _c('asmin kāle etarhi — and the base changes for the sound',
           {'stem': 'idam', 'case': 'saptamī', 'result': 'kāla'},
           note='इदमो र्हिल्, हस्यापवादः. लकारः स्वरार्थः. काल इत्येव — इह देशे.'),
    ),
    "5.3.17": (
        _c('adhunā — substitution and affix laid down together',
           {'stem': 'idam', 'case': 'saptamī', 'result': 'kāla', 'wants': 'dhunā'},
           note='अधुना. इदमोऽश्भावो धुना च प्रत्ययः.'),
    ),
    "5.3.18": (
        _c('idānīm — a third affix for that pronoun',
           {'stem': 'idam', 'case': 'saptamī', 'result': 'kāla', 'wants': 'dānīm'},
           note='दानीं च.'),
    ),
    "5.3.19": (
        _c('tadā, tadānīm — and the first of the two is idle',
           {'stem': 'tad', 'case': 'saptamī', 'result': 'kāla', 'wants': 'dānīm'},
           note='तदो दा च. तदो दावचनमनर्थकम्, विहितत्वात्.'),
    ),
    "5.3.20": (
        _c('idāvatsarīyaḥ — a Vedic pair, matched to two pronouns',
           {'stem': 'idam', 'case': 'saptamī', 'usage': 'chandasi'},
           note='तयोर्दार्हिलौ च छन्दसि, यथासंख्यम्. चकाराद् यथाप्राप्तं च.'),
    ),
    "5.3.21": (
        _c('karhi, tarhi — of a time that is not today',
           {'stem': 'kim', 'samjna': 'sarvanāman', 'case': 'saptamī', 'result': 'anadyatana'},
           note='अनद्यतने र्हिलन्यतरस्याम्. छन्दसीति न स्वर्यते; सामान्येन विधानम्.'),
    ),
    "5.3.22": (
        _c('sadyaḥ, parut, adya — eighteen laid down at once',
           {'gana': 'sadyaḥprabhṛti', 'case': 'saptamī', 'result': 'kāla'},
           note='सद्यःपरुत्…. प्रकृतिः, प्रत्ययः, आदेशः, कालविशेष इति सर्वमेतद् निपातनाद् लभ्यते.'),
    ),
    "5.3.23": (
        _c('kathā, yathā, tathā — of the manner of a thing',
           {'stem': 'kim', 'samjna': 'sarvanāman', 'result': 'prakāra'},
           note='प्रकारवचने थाल्.'),
    ),
    "5.3.24": (
        _c('ittham — the base changing for the sound again',
           {'stem': 'idam', 'result': 'prakāra'},
           note='इदमस्थमुः.'),
    ),
    "5.3.25": (
        _c('katham — the same affix on the interrogative',
           {'stem': 'kim', 'result': 'prakāra'},
           note='किमश्च.'),
    ),
    "5.3.26": (
        _c('kathā — in the Veda, of a cause',
           {'stem': 'kim', 'result': 'hetu', 'usage': 'chandasi'},
           note='था हेतौ च छन्दसि.'),
    ),
    "5.3.27": (
        _c('dakṣiṇataḥ — the marker the whole section was bounded by',
           {'samjna': 'dikśabda', 'case': 'saptamī-pañcamī-prathamā', 'result': 'dik-deśa-kāla'},
           note='दिक्शब्देभ्यः सप्तमीपञ्चमीप्रथमाभ्यो दिग्देशकालेष्वस्तातिः.'),
    ),
    "5.3.28": (
        _c('dakṣiṇato vasati — one form for all three cases',
           {'stem': 'dakṣiṇa', 'case': 'saptamī-pañcamī-prathamā', 'result': 'dik-deśa'},
           note='दक्षिणोत्तराभ्यामतसुच्, अस्तातेरपवादः. दक्षिणाशब्दः काले न संभवतीति दिग्देशवृत्तिः परिगृह्यते.'),
    ),
    "5.3.29": (
        _c('parato vasati, parastād vasati — an option, and both',
           {'stem': 'para', 'case': 'saptamī-pañcamī-prathamā'},
           note='विभाषा परावराभ्याम्.'),
    ),
    "5.3.30": (
        _c('prāg vasati — and the feminine goes with the affix',
           {'samjna': 'añcanta', 'case': 'saptamī-pañcamī-prathamā'},
           note='अञ्चेर्लुक्. लुक् तद्धितलुकि इति स्त्रीप्रत्ययोऽपि निवर्तते.'),
    ),
    "5.3.31": (
        _c('upari vasati, upariṣṭād vasati — two laid down',
           {'stem': 'ūrdhva', 'case': 'saptamī-pañcamī-prathamā'},
           note='उपर्युपरिष्टात्. ऊर्ध्वस्योपभावो रिल्रिष्टातिलौ च प्रत्ययौ निपात्येते.'),
    ),
    "5.3.32": (
        _c('paścād vasati — and three supplements for compounds',
           {'stem': 'apara', 'case': 'saptamī-pañcamī-prathamā'},
           note='पश्चात्. अपरस्य पश्चभाव आतिश्च प्रत्ययः. विनापि पूर्वपदेन पश्चभावो वक्तव्यः.'),
    ),
    "5.3.33": (
        _c('paśca siṃhaḥ — two Vedic forms beside the ordinary',
           {'stem': 'apara', 'case': 'saptamī-pañcamī-prathamā', 'usage': 'chandasi'},
           note='पश्च पश्चा च छन्दसि. चकारात् पश्चादित्यपि भवति.'),
    ),
    "5.3.34": (
        _c('uttarād vasati — a third affix for three words',
           {'stem': 'uttara', 'case': 'saptamī-pañcamī-prathamā'},
           note='उत्तराधरदक्षिणादातिः.'),
    ),
    "5.3.35": (
        _c('uttareṇa vasati — only near, and not from an ablative',
           {'stem': 'uttara', 'case': 'saptamī-prathamā', 'result': 'adūra'},
           note='एनबन्यतरस्यामदूरेऽपञ्चम्याः. अदूर इति किम्? उत्तराद् वसति. अपञ्चम्या इति किम्? उत्तरादागतः.'),
    ),
    "5.3.36": (
        _c('dakṣiṇā vasati — the *not far* lapses, the bar carries',
           {'stem': 'dakṣiṇa', 'case': 'saptamī-prathamā'},
           note='दक्षिणादाच्. अदूर इति न स्वर्यते; अपञ्चम्या इति वर्तते.'),
    ),
    "5.3.37": (
        _c('dakṣiṇāhi vasati — and now only where the distance is far',
           {'stem': 'dakṣiṇa', 'case': 'saptamī-prathamā', 'result': 'dūra'},
           note='आहि च दूरे. दूर इति किम्? दक्षिणतो वसति.'),
    ),
    "5.3.38": (
        _c('uttarā vasati, uttarāhi vasati — a far distance again',
           {'stem': 'uttara', 'case': 'saptamī-prathamā', 'result': 'dūra'},
           note='उत्तराच्च. दूर इत्येव — उत्तरेण प्रयाति.'),
    ),
    "5.3.39": (
        _c('puro vasati, adho vasati — and the ablative bar lapses',
           {'stem': 'pūrva', 'case': 'saptamī-pañcamī-prathamā'},
           note='पूर्वाधरावराणामसि पुरधवश्चैषाम्. अपञ्चम्या इति निवृत्तम्; तिसृणां विभक्तीनामिह ग्रहणम्.'),
    ),
    "5.3.40": (
        _c('purastād vasati — a substitute that proves an affix',
           {'stem': 'pūrva', 'before': 'astāti', 'case': 'saptamī-pañcamī-prathamā'},
           note='अस्ताति च. इदमेवादेशविधानं ज्ञापकम् — अस्तातिरेभ्यो भवति, असिप्रत्ययेन न बाध्यत इति.'),
    ),
    "5.3.41": (
        _c('avastād, avarastād — obligatory turned to a choice',
           {'stem': 'avara', 'before': 'astāti', 'case': 'saptamī-pañcamī-prathamā'},
           note='विभाषावरस्य. पूर्वेण नित्ये प्राप्ते विकल्प उच्यते.'),
    ),
    "5.3.42": (
        _c('ekadhā bhuṅkte — of the manner of any action whatever',
           {'samjna': 'saṃkhyā', 'result': 'vidhā'},
           note='संख्याया विधार्थे धा. विधा प्रकारः, स च सर्वक्रियाविषय एव गृह्यते.'),
    ),
    "5.3.43": (
        _c('ekaṃ rāśiṃ pañcadhā kuru — one made many, many made one',
           {'samjna': 'saṃkhyā', 'result': 'adhikaraṇavicāla'},
           note='अधिकरणविचाले च. अधिकरणं द्रव्यम्, तस्य विचालः संख्यान्तरापादनम्.'),
    ),
    "5.3.44": (
        _c('ekadhā, aikadhyam — and the affix named to reach both senses',
           {'stem': 'eka', 'samjna': 'saṃkhyā', 'result': 'vidhā'},
           note='एकाद् धो ध्यमुञन्यतरस्याम्. प्रकरणादेव लब्धे पुनर्धाग्रहणं विधार्थे विहितस्यापि यथा स्यात्.'),
    ),
    "5.3.45": (
        _c('dvidhā, dvaidham — and a supplement adds one more',
           {'stem': 'dvi', 'samjna': 'saṃkhyā', 'result': 'vidhā'},
           note='द्वित्र्योश्च धमुञ्. धमुञन्तात् स्वार्थे डदर्शनम् — मतिद्वैधानि संश्रयन्ते.'),
    ),
    "5.3.46": (
        _c('dvedhā, dvaidham, dvidhā — three forms apiece',
           {'stem': 'dvi', 'samjna': 'saṃkhyā', 'result': 'vidhā', 'wants': 'dhā'},
           note='एधाच्च.'),
    ),
    "5.3.47": (
        _c('vaiyākaraṇapāśaḥ — contempt of the quality, not the man',
           {'result': 'yāpya'},
           note='याप्ये पाशप्. यस्य गुणस्य सद्भावाद् द्रव्ये शब्दनिवेशः, तस्य कुत्सायां प्रत्ययः.'),
    ),
    "5.3.48": (
        _c('dvitīyo bhāgo dvitīyaḥ — a rule for the accent alone',
           {'samjna': 'tīyānta', 'result': 'bhāga'},
           note='पूरणाद् भागे तीयादन्. स्वरार्थं वचनम्. भाग इति किम्? द्वितीयम्.'),
    ),
    "5.3.49": (
        _c('pañcamaḥ, daśamaḥ — and only below eleven, outside the Veda',
           {'samjna': 'pūraṇānta', 'result': 'bhāga', 'usage': 'abhāṣā'},
           note='प्रागेकादशभ्योऽच्छन्दसि. प्रागेकादशभ्य इति किम्? एकादशः, द्वादशः.'),
    ),
    "5.3.50": (
        _c('ṣāṣṭhaḥ, ṣaṣṭhaḥ — two affixes for two ordinals',
           {'stem': 'ṣaṣṭha', 'result': 'bhāga', 'usage': 'abhāṣā'},
           note='षष्ठाष्टमाभ्यां ञ च. चकारादन् च.'),
    ),
    "5.3.51": (
        _c('ṣaṣṭhako bhāgaḥ — an affix and a removal, matched in order',
           {'stem': 'ṣaṣṭha', 'result': 'māna'},
           note='मानपश्वङ्गयोः कन्लुकौ च. कस्य लुक्? ञस्य लुक्, अनो वा.'),
    ),
    "5.3.52": (
        _c('ekākī, ekakaḥ, ekaḥ — and the numeral sense kept out',
           {'stem': 'eka', 'result': 'asahāya'},
           note='एकादाकिनिच्चासहाये. असहायग्रहणं संख्याशब्दनिरासार्थम्.'),
    ),
    "5.3.53": (
        _c('āḍhyacaraḥ — once rich',
           {'result': 'bhūtapūrva'},
           note='भूतपूर्वे चरट्. भूतपूर्वशब्दोऽतिक्रान्तकालवचनः; प्रकृतिविशेषणं चैतत्.'),
    ),
    "5.3.54": (
        _c('devadattarūpyaḥ — and now *formerly* describes the sense',
           {'case': 'ṣaṣṭhī', 'result': 'bhūtapūrva'},
           note='षष्ठ्या रूप्य च. संप्रति भूतपूर्वग्रहणं प्रत्ययार्थस्य विशेषणम्, न तु प्रकृत्यर्थविशेषणम्.'),
    ),
    "5.3.55": (
        _c('āḍhyatamaḥ, paṭiṣṭhaḥ — the superlative',
           {'result': 'atiśāyana'},
           note='अतिशायने तमबिष्ठनौ. प्रकृत्यर्थविशेषणं च स्वार्थिकानां द्योत्यं भवति.'),
    ),
    "5.3.56": (
        _c('pacatitamām — and after a finite verb, which needed saying',
           {'samjna': 'tiṅanta', 'result': 'atiśāyana'},
           note='तिङश्च. ङ्याप्प्रातिपदिकात् इत्यधिकारात् तिङो न प्राप्नोतीतीदं वचनम्.'),
    ),
    "5.3.57": (
        _c('āḍhyataraḥ, paṭīyān — the comparative',
           {'result': 'dvivacana-vibhajya'},
           note='द्विवचनविभज्योपपदे तरबीयसुनौ, तमबिष्ठनोरपवादौ. यथासंख्यमत्र नेष्यते.'),
    ),
    "5.3.58": (
        _c('paṭīyān, paṭiṣṭhaḥ — a restriction on the affix, not the base',
           {'samjna': 'guṇavacana', 'result': 'atiśāyana'},
           note='अजादी गुणवचनादेव. एवकार इष्टतोऽवधारणार्थः, प्रत्ययनियमोऽयं न प्रकृतिनियम इति.'),
    ),
    "5.3.59": (
        _c('kariṣṭhaḥ — and in the Veda the restriction is loosened',
           {'samjna': 'tṛnanta', 'result': 'atiśāyana', 'usage': 'chandasi'},
           note='तुश्छन्दसि. छन्दसि प्रकृत्यन्तराण्यभ्यनुज्ञायन्ते.'),
    ),
    "5.3.60": (
        _c('śreṣṭhaḥ, śreyān — a substitute that undoes a restriction',
           {'stem': 'praśasya', 'before': 'ajādi', 'result': 'atiśāyana'},
           note='प्रशस्यस्य श्रः. आदेशविधानसामर्थ्यात् तद्विषयो नियमो न प्रवर्तते.'),
    ),
    "5.3.61": (
        _c('jyeṣṭhaḥ, jyāyān — a second substitute for the same word',
           {'stem': 'praśasya', 'before': 'ajādi', 'result': 'atiśāyana', 'wants': ''},
           note='ज्य च. ज्यादादीयसः इत्याकारः.'),
    ),
    "5.3.62": (
        _c('jyeṣṭhaḥ, varṣiṣṭhaḥ — and one more word, with two forms',
           {'stem': 'vṛddha', 'before': 'ajādi', 'result': 'atiśāyana'},
           note='वृद्धस्य च. वचनसामर्थ्यात् पक्षे सोऽपि भवति — वर्षिष्ठः, वर्षीयान्.'),
    ),
    "5.3.63": (
        _c('nediṣṭham, sādhiṣṭham — two substitutes, two words',
           {'stem': 'antika', 'before': 'ajādi', 'result': 'atiśāyana'},
           note='अन्तिकबाढयोर्नेदसाधौ. निमित्तयोर्यथासंख्यमत्र नेष्यते.'),
    ),
    "5.3.64": (
        _c('kaniṣṭhaḥ, yaviṣṭhaḥ — an option, so both sets stand',
           {'stem': 'yuvan', 'before': 'ajādi', 'result': 'atiśāyana'},
           note='युवाल्पयोः कनन्यतरस्याम्.'),
    ),
    "5.3.65": (
        _c('srajiṣṭhaḥ — a removal that proves the affixes come',
           {'samjna': 'vin-matvanta', 'before': 'ajādi', 'result': 'atiśāyana'},
           note='विन्मतोर्लुक्. इदमेव वचनं ज्ञापकमजादिसद्भावस्य.'),
    ),
    "5.3.66": (
        _c('vaiyākaraṇarūpaḥ — and the praise may be bitter',
           {'result': 'praśaṃsā'},
           note='प्रशंसायां रूपप्. वृषलरूपोऽयम्, यः पलाण्डुना सुरां पिबति.'),
    ),
    "5.3.67": (
        _c('paṭukalpaḥ — a slight falling short of completeness',
           {'result': 'īṣadasamāpti'},
           note='ईषदसमाप्तौ कल्पब्देश्यदेशीयरः. स्तोकेनासंपूर्णता ईषदसमाप्तिः.'),
    ),
    "5.3.68": (
        _c('bahupaṭuḥ — and this one goes in front of the word',
           {'samjna': 'subanta', 'result': 'īṣadasamāpti'},
           note='विभाषा सुपो बहुच् पुरस्तात्तु. स तु पुरस्तादेव भवति न परतः.'),
    ),
    "5.3.69": (
        _c('paṭujātīyaḥ — for what HAS a kind, not for the kind',
           {'samjna': 'subanta', 'result': 'prakāra'},
           note='प्रकारवचने जातीयर्. थाल् पुनः प्रकारमात्र एव भवति.'),
    ),
    "5.3.70": (
        _c('aśvakaḥ — a heading, and this one supplies an affix',
           {'result': 'ajñāta'},
           note='प्रागिवात्कः. प्रागेतस्मादिवसंशब्दनात्, कप्रत्ययस्तेष्वधिकृतो वेदितव्यः.'),
    ),
    "5.3.71": (
        _c('uccakaiḥ, sarvake — an affix that goes inside the word',
           {'samjna': 'avyaya-sarvanāman'},
           note='अव्ययसर्वनाम्नामकच् प्राक् टेः. तत्राभिधानतो व्यवस्था भवति.'),
    ),
    "5.3.72": (
        _c('dhakit, pṛthakat — a final sound changing with the affix',
           {'samjna': 'kānta-avyaya', 'before': 'akac'},
           note='कस्य च दः. सामर्थ्याच्चाव्ययग्रहणमनुवर्तते, न सर्वनामग्रहणम्.'),
    ),
    "5.3.73": (
        _c('aśvakaḥ — a horse whose owner one cannot say',
           {'result': 'ajñāta'},
           note='अज्ञाते. स्वेन रूपेण ज्ञाते पदार्थे विशेषरूपेणाज्ञाते प्रत्ययविधानमेतत्.'),
    ),
    "5.3.74": (
        _c('kutsito ’śvaḥ aśvakaḥ — in contempt',
           {'result': 'kutsita'},
           note='कुत्सिते. कुत्सितो गर्हितो निन्दितः.'),
    ),
    "5.3.75": (
        _c('śūdrakaḥ — where the word formed is a name',
           {'result': 'kutsita-saṃjñā'},
           note='संज्ञायां कन्, कस्यापवादः.'),
    ),
    "5.3.76": (
        _c('putrakaḥ, vatsakaḥ — in pity',
           {'result': 'anukampā'},
           note='अनुकम्पायाम्. कारुण्येनाभ्युपपत्तिः परस्यानुकम्पा.'),
    ),
    "5.3.77": (
        _c('hanta te dhānakāḥ — and from what stands at one remove',
           {'result': 'nīti-tadyukta'},
           note='नीतौ च तद्युक्तात्. सम्प्रति व्यवहितादपि यथा स्यादिति वचनम्.'),
    ),
    "5.3.78": (
        _c('devikaḥ, devadattakaḥ — from a man name of many vowels',
           {'samjna': 'manuṣyanāman', 'result': 'anukampā-nīti'},
           note='बह्वचो मनुष्यनाम्नष्ठज्वा. बह्वच इति किम्? दत्तकः.'),
    ),
    "5.3.79": (
        _c('deviyaḥ, devilaḥ — and four forms in all',
           {'samjna': 'manuṣyanāman', 'result': 'anukampā-nīti', 'wants': 'ghan'},
           note='घनिलचौ च. पूर्वेण ठचि विकल्पेन प्राप्ते वचनम्.'),
    ),
    "5.3.80": (
        _c('upaḍaḥ, upakaḥ — five affixes for one kind of name',
           {'samjna': 'manuṣyanāman', 'pre': 'upa', 'result': 'anukampā-nīti'},
           note='प्राचामुपादेरडज्वुचौ च. प्राचांग्रहणं पूजार्थम्.'),
    ),
    "5.3.81": (
        _c('vyāghrakaḥ, siṃhakaḥ — a name that is also a kind-word',
           {'samjna': 'jātināman', 'result': 'anukampā-nīti'},
           note='जातिनाम्नः कन्. बह्वच इति नानुवर्तते; सामान्येन विधानम्.'),
    ),
    "5.3.82": (
        _c('vyāghrājino vyāghrakaḥ — the affix and a loss together',
           {'samjna': 'ajinānta', 'result': 'anukampā'},
           note='अजिनान्तस्योत्तरपदलोपश्च.'),
    ),
    "5.3.83": (
        _c('devikaḥ — everything above the second vowel is lost',
           {'before': 'ṭha-ajādi', 'result': 'anukampā-nīti'},
           note='ठाजादावूर्ध्वं द्वितीयादचः. ऊर्ध्वग्रहणं सर्वलोपार्थम्.'),
    ),
    "5.3.84": (
        _c('śevalikaḥ — from the third vowel, and before sandhi',
           {'gana': 'śevalādi', 'before': 'ṭha-ajādi', 'result': 'anukampā-nīti'},
           note='शेवलसुपरिविशालवरुणार्यमादीनां तृतीयात्. स चाकृतसन्धीनामिति वक्तव्यम्.'),
    ),
    "5.3.85": (
        _c('alpaṃ tailaṃ tailakam — of what is small',
           {'result': 'alpa'},
           note='अल्पे. परिमाणापचयेऽल्पशब्दः.'),
    ),
    "5.3.86": (
        _c('hrasvo vṛkṣo vṛkṣakaḥ — short, the correlate of long',
           {'result': 'hrasva'},
           note='ह्रस्वे. दीर्घप्रतियोगी ह्रस्वः.'),
    ),
    "5.3.87": (
        _c('vaṃśakaḥ, veṇukaḥ — where the name comes from the shortness',
           {'result': 'hrasva-saṃjñā'},
           note='संज्ञायां कन्. ह्रस्वत्वहेतुका या संज्ञा.'),
    ),
    "5.3.88": (
        _c('hrasvā kuṭī kuṭīraḥ — and the word turns masculine',
           {'stem': 'kuṭī', 'result': 'hrasva'},
           note='कुटीशमीशुण्डाभ्यो रः. स्वार्थिकत्वेऽपि पुँल्लिङ्गता, लोकाश्रयत्वाल्लिङ्गस्य.'),
    ),
    "5.3.89": (
        _c('kutupam — a small leather oil-flask',
           {'stem': 'kutū', 'result': 'hrasva'},
           note='कुत्वा डुपच्. चर्ममयं स्नेहभाजनमुच्यते.'),
    ),
    "5.3.90": (
        _c('kāsūtarī, goṇītarī — and one letter for the feminine',
           {'stem': 'kāsū', 'result': 'hrasva'},
           note='कासूगोणीभ्यां ष्टरच्. षकारो ङीषर्थः.'),
    ),
    "5.3.91": (
        _c('vatsataraḥ, aśvataraḥ — slightness, worked out four ways',
           {'stem': 'aśva', 'result': 'tanutva'},
           note='वत्सोक्षाश्वर्षभेभ्यश्च तनुत्वे. अश्वेनाश्वायामुत्पन्नोऽश्वः, तस्य तनुत्वमन्यपितृकता.'),
    ),
    "5.3.92": (
        _c('kataro bhavatoḥ kaṭhaḥ — singling one out of two',
           {'stem': 'kim', 'result': 'nirdhāraṇa-dvayoḥ'},
           note='किंयत्तदो निर्धारणे द्वयोरेकस्य डतरच्. जात्या क्रियया गुणेन संज्ञया वा समुदायादेकदेशस्य पृथक्करणं निर्धारणम्.'),
    ),
    "5.3.93": (
        _c('katamo bhavatāṃ kaṭhaḥ — one of many, and a kind asked after',
           {'stem': 'kim', 'result': 'nirdhāraṇa-bahūnām'},
           note='वा बहूनां जातिपरिप्रश्ने डतमच्. जातिग्रहणं तु सर्वैरेव संबध्यते.'),
    ),
    "5.3.94": (
        _c('ekataro, ekatamo — both affixes, and the kind not carried',
           {'stem': 'eka', 'result': 'nirdhāraṇa'},
           note='एकाच्च प्राचाम्. जातिपरिप्रश्न इति नानुवर्तते; सामान्येन विधानम्.'),
    ),
    "5.3.95": (
        _c('vyākaraṇakena nāma tvaṃ garvitaḥ — reproach of another',
           {'result': 'avakṣepaṇa'},
           note='अवक्षेपणे कन्. परस्य कुत्सार्थं यदुपादीयते, तदिहोदाहरणम्. प्रागिवीयस्य पूर्णोऽवधिः.'),
    ),
    "5.3.96": (
        _c('aśvapratikṛtir aśvakaḥ — a made likeness, not a mere one',
           {'result': 'iva-pratikṛti'},
           note='इवे प्रतिकृतौ. प्रतिकृताविति किम्? गौरिव गवयः.'),
    ),
    "5.3.97": (
        _c('aśvakaḥ — where the whole word is a name',
           {'result': 'iva-saṃjñā'},
           note='संज्ञायां च. अप्रतिकृत्यर्थ आरम्भः.'),
    ),
    "5.3.98": (
        _c('cañceva manuṣyaḥ cañcā — the affix removed for a man',
           {'result': 'iva-manuṣya'},
           note='लुम्मनुष्ये. मनुष्य इति किम्? अश्वकः.'),
    ),
    "5.3.99": (
        _c('vāsudevaḥ, śivaḥ — images made for a livelihood',
           {'result': 'jīvikārtha-apaṇya'},
           note='जीविकार्थे चापण्ये. अपण्य इति किम्? हस्तिकान् विक्रीणीते.'),
    ),
    "5.3.100": (
        _c('śivaḥ, arjunaḥ, garuḍaḥ — worship, painting, banner',
           {'gana': 'devapathādi'},
           note='देवपथादिभ्यश्च. अर्चासु पूजनार्थासु चित्रकर्मध्वजेषु च.'),
    ),
    "5.3.101": (
        _c('vastir iva vāsteyaḥ — a likeness, image or no image',
           {'stem': 'vasti', 'result': 'iva'},
           note='वस्तेर्ढञ्. इतः प्रभृति प्रत्ययाः सामान्येन भवन्ति, प्रतिकृतौ चाप्रतिकृतौ च.'),
    ),
    "5.3.102": (
        _c('śileyaṃ dadhi — curd like stone',
           {'stem': 'śilā', 'result': 'iva'},
           note='शिलाया ढः. केचिदत्र ढञमपीच्छन्ति, तदर्थं योगविभागः कर्तव्यः.'),
    ),
    "5.3.103": (
        _c('śākheva śākhyaḥ — yat after a list',
           {'gana': 'śākhādi', 'result': 'iva'},
           note='शाखादिभ्यो यत्.'),
    ),
    "5.3.104": (
        _c('dravyo ’yaṃ rājaputraḥ — a prince of promise',
           {'stem': 'dru', 'result': 'bhavya'},
           note='द्रव्यं च भव्ये. अभिप्रेतानामर्थानां पात्रभूत उच्यते.'),
    ),
    "5.3.105": (
        _c('kuśāgrīyā buddhiḥ — a mind fine as a blade point',
           {'stem': 'kuśāgra', 'result': 'iva'},
           note='कुशाग्राच्छः.'),
    ),
    "5.3.106": (
        _c('kākatālīyam — the crow, the palm-fruit, and two figures',
           {'samjna': 'iva-samāsa', 'result': 'iva'},
           note='समासाच्च तद्विषयात्. तत्र प्रथमे समासः, द्वितीये प्रत्ययः.'),
    ),
    "5.3.107": (
        _c('śarkareva śārkaram — aṇ after a list',
           {'gana': 'śarkarādi', 'result': 'iva'},
           note='शर्करादिभ्योऽण्.'),
    ),
    "5.3.108": (
        _c('aṅgulīvāṅgulikaḥ — ṭhak after another list',
           {'gana': 'aṅgulyādi', 'result': 'iva'},
           note='अङ्गुल्यादिभ्यष्ठक्.'),
    ),
    "5.3.109": (
        _c('ekaśālikaḥ, aikaśālikaḥ — an option keeping both',
           {'stem': 'ekaśālā', 'result': 'iva'},
           note='एकशालायाष्ठजन्यतरस्याम्. अन्यतरस्यांग्रहणेनानन्तरष्ठक् प्राप्यते.'),
    ),
    "5.3.110": (
        _c('lauhitīkaḥ sphaṭikaḥ — red from what lies behind it',
           {'stem': 'lohita', 'result': 'iva'},
           note='कर्कलोहितादीकक्. स्वयमलोहितोऽप्युपाश्रयवशात् तथा प्रतीयते.'),
    ),
    "5.3.111": (
        _c('pratnathā, pūrvathā — four pronouns, in the Veda',
           {'stem': 'pratna', 'result': 'iva', 'usage': 'chandasi'},
           note='प्रत्नपूर्वविश्वेमात् थाल् छन्दसि.'),
    ),
    "5.3.112": (
        _c('lauhadhvajyaḥ, śaibyaḥ — a troop, not named from a leader',
           {'samjna': 'pūga', 'result': 'tadrāja'},
           note='पूगाञ् ञ्योऽग्रामणीपूर्वात्. अग्रामणीपूर्वादिति किम्? देवदत्तकाः.'),
    ),
    "5.3.113": (
        _c('kāpotapākyaḥ — a band, and not in the feminine',
           {'samjna': 'vrāta-cphañanta', 'result': 'tadrāja'},
           note='व्रातच्फञोरस्त्रियाम्. अस्त्रियामिति किम्? कपोतपाकी.'),
    ),
    "5.3.114": (
        _c('kṣaudrakyaḥ, mālavyaḥ — a confederacy living by arms',
           {'samjna': 'āyudhajīvisaṃgha', 'result': 'tadrāja'},
           note='आयुधजीविसंघाञ् ञ्यड् वाहीकेष्वब्राह्मणराजन्यात्. संघग्रहणं किम्? सम्राट्.'),
    ),
    "5.3.115": (
        _c('vārkeṇyaḥ — and not of the animal of the same name',
           {'stem': 'vṛka', 'samjna': 'āyudhajīvisaṃgha', 'result': 'tadrāja'},
           note='वृकाट् टेण्यण्. आयुधजीविसंघविशेषणं जातिशब्दाद् मा भूत्.'),
    ),
    "5.3.116": (
        _c('dāmanīyaḥ, kauṇḍoparathīyaḥ — and a verse names the six',
           {'gana': 'dāmanyādi', 'samjna': 'āyudhajīvisaṃgha', 'result': 'tadrāja'},
           note='दामन्यादित्रिगर्तषष्ठाच्छः. आहुस्त्रिगर्तषष्ठांस्तु कौण्डोपरथदाण्डकी.'),
    ),
    "5.3.117": (
        _c('pārśavaḥ, yaudheyaḥ — two affixes for two lists',
           {'gana': 'parśvādi', 'samjna': 'āyudhajīvisaṃgha', 'result': 'tadrāja'},
           note='पर्श्वादियौधेयादिभ्यामणञौ.'),
    ),
    "5.3.118": (
        _c('ābhijityaḥ — after stems that already carry an affix',
           {'gana': 'abhijidādi', 'samjna': 'aṇanta', 'result': 'tadrāja'},
           note='अभिजिद्…अणो यञ्. गोत्रप्रत्ययस्यात्राणो ग्रहणमिष्यते.'),
    ),
    "5.3.119": (
        _c('ñyādayas tadrājāḥ — the quarter closes with a name',
           {'result': 'tadrāja'},
           note='ञ्यादयस्तद्राजाः. तद्राजप्रदेशाः — तद्राजस्य बहुषु० इत्येवमादयः.'),
    ),
    "5.4.1": (
        _c('dvipadikāṃ dadāti — and a loss with no cause of its own',
           {'samjna': 'pādaśatānta-saṃkhyādi', 'result': 'vīpsā'},
           note='पादशतस्य संख्यादेर्वीप्सायां वुन् लोपश्च. अस्य त्वनैमित्तिकत्वाद् न स्थानिवत्त्वम्.'),
    ),
    "5.4.2": (
        _c('dvipadikāṃ daṇḍitaḥ — a fine, and no repetition needed',
           {'samjna': 'pādaśatānta-saṃkhyādi', 'result': 'daṇḍa-vyavasarga'},
           note='दण्डव्यवसर्गयोश्च. अवीप्सार्थोऽयमारम्भः.'),
    ),
    "5.4.3": (
        _c('sthūlaprakāraḥ sthūlakaḥ — a kind of thing',
           {'gana': 'sthūlādi', 'result': 'prakāra'},
           note='स्थूलादिभ्यः प्रकारवचने कन्, जातीयरोऽपवादः.'),
    ),
    "5.4.4": (
        _c('bhinnakaḥ, chinnakaḥ — partly broken, partly cut',
           {'samjna': 'ktānta', 'result': 'anatyantagati'},
           note='अनत्यन्तगतौ क्तात्. अत्यन्तगतिरशेषसंबन्धः, तदभावोऽनत्यन्तगतिः.'),
    ),
    "5.4.5": (
        _c('sāmikṛtam — a refusal that proves what it forbids',
           {'samjna': 'ktānta', 'result': 'anatyantagati', 'upapada': 'sāmivacana'},
           note='न सामिवचने. एतदेव ज्ञापकम् — भवति स्वार्थे कन्निति.'),
    ),
    "5.4.6": (
        _c('bṛhatikā — a cloak, and the refusal not carried down',
           {'stem': 'bṛhatī', 'result': 'ācchādana'},
           note='बृहत्या आच्छादने. कन्ननुवर्तते, न प्रतिषेधः. आच्छादन इति किम्? बृहती छन्दः.'),
    ),
    "5.4.7": (
        _c('aṣaḍakṣīṇo mantraḥ — counsel taken by two, not six eyes',
           {'stem': 'aṣaḍakṣa'},
           note='अषडक्षाशितङ्ग्वलंकर्मालंपुरुषाध्युत्तरपदात् खः. नित्यश्चायं प्रत्ययः, उत्तरत्र विभाषाग्रहणात्.'),
    ),
    "5.4.8": (
        _c('prāk, prācīnam — and not of a quarter in the feminine',
           {'samjna': 'añcanta', 'result': 'adiksṛī'},
           note='विभाषा अञ्चेरदिक्स्त्रियाम्. स्त्रीग्रहणं किम्? प्राचीनं दिग् रमणीयम्.'),
    ),
    "5.4.9": (
        _c('brāhmaṇajātīyaḥ — that by which brahmin-hood shows',
           {'samjna': 'jātyanta', 'result': 'bandhu'},
           note='जात्यन्ताच्छ बन्धुनि. बध्यतेऽस्मिन् जातिरिति बन्धुशब्देन द्रव्यमुच्यते.'),
    ),
    "5.4.10": (
        _c('pitṛsthānīyaḥ — and a rule between two options is fixed',
           {'samjna': 'sthānānta', 'result': 'sasthāna'},
           note='स्थानान्ताद् विभाषा सस्थानेनेति चेत्. द्वयोर्विभाषयोर्मध्ये नित्या विधय इति.'),
    ),
    "5.4.11": (
        _c('kiṃtarām, pacatitarām — a substance has no degrees',
           {'samjna': 'kim-et-tiṅ-avyaya-gha', 'result': 'adravyaprakarṣa'},
           note='किमेत्तिङव्ययघादामु अद्रव्यप्रकर्षे. क्रियागुणयोरेवायं प्रकर्षे प्रत्ययः.'),
    ),
    "5.4.12": (
        _c('prataraṃ na āyuḥ — and both endings make an indeclinable',
           {'samjna': 'kim-et-tiṅ-avyaya-gha', 'result': 'adravyaprakarṣa', 'usage': 'chandasi'},
           note='अमु च छन्दसि. स्वरादिषु अम् आम् इति पठ्यते.'),
    ),
    "5.4.13": (
        _c('ānugādikaḥ — one who repeats after another',
           {'stem': 'anugādin'},
           note='अनुगादिनष्ठक्. अनुगदतीत्यनुगादी.'),
    ),
    "5.4.14": (
        _c('vyāvakrośī vartate — an idle word read as a jñāpaka',
           {'samjna': 'ṇacanta', 'result': 'strī'},
           note='णचः स्त्रियामञ्. स्वार्थिकाः प्रत्ययाः प्रकृतितो लिङ्गवचनान्यतिवर्तन्तेऽपि इति.'),
    ),
    "5.4.15": (
        _c('sāṃrāviṇaṃ vartate — a clamour all round',
           {'samjna': 'inuṇanta'},
           note='अणिनुणः.'),
    ),
    "5.4.16": (
        _c('vaisāriṇo matsyaḥ — of a fish, and of nothing else',
           {'stem': 'visārin', 'result': 'matsya'},
           note='विसारिणो मत्स्ये. मत्स्य इति किम्? विसारी देवदत्तः.'),
    ),
    "5.4.17": (
        _c('pañcakṛtvaḥ — counting how often an act recurs',
           {'samjna': 'saṃkhyā', 'result': 'kriyābhyāvṛttigaṇana'},
           note='संख्यायाः क्रियाभ्यावृत्तिगणने कृत्वसुच्. एककर्तृकाणां तुल्यजातीयानां क्रियाणां जन्मसंख्यानम्.'),
    ),
    "5.4.18": (
        _c('dvir bhuṅkte, trir bhuṅkte — three numerals apart',
           {'stem': 'dvi', 'samjna': 'saṃkhyā', 'result': 'kriyābhyāvṛttigaṇana'},
           note='द्वित्रिचतुर्भ्यः सुच्, कृत्वसुचोऽपवादः.'),
    ),
    "5.4.19": (
        _c('sakṛd bhuṅkte — one occurrence is not a recurrence',
           {'stem': 'eka', 'samjna': 'saṃkhyā', 'result': 'kriyāgaṇana'},
           note='एकस्य सकृच्च. अभ्यावृत्तिस्त्विह न संभवति.'),
    ),
    "5.4.20": (
        _c('bahudhā divasasya bhuṅkte — recurrences close together',
           {'stem': 'bahu', 'samjna': 'saṃkhyā', 'result': 'aviprakṛṣṭakāla'},
           note='विभाषा बहोर्धाविप्रकृष्टकाले. अविप्रकृष्टकाल इति किम्? बहुकृत्वो मासस्य भुङ्क्ते.'),
    ),
    "5.4.21": (
        _c('annamayam — and a second reading kept beside the first',
           {'case': 'prathamā', 'result': 'prakṛta'},
           note='तत्प्रकृतवचने मयट्. द्वयमपि प्रमाणम्, उभयथा सूत्रप्रणयनात्.'),
    ),
    "5.4.22": (
        _c('maudakikam, modakamayam — where many things are on hand',
           {'case': 'prathamā', 'result': 'prakṛta-bahuṣu'},
           note='समूहवच्च बहुषु. अतिवर्तन्तेऽपि स्वार्थिकाः प्रकृतितो लिङ्गवचनानि.'),
    ),
    "5.4.23": (
        _c('ānantyam, aitihyam — what is handed down',
           {'gana': 'anantādi'},
           note='अनन्तावसथेतिहभेषजाञ् ञ्यः. निपातसमुदायोऽयमुपदेशपारम्पर्ये वर्तते.'),
    ),
    "5.4.24": (
        _c('agnidevatyam — what is for that deity',
           {'samjna': 'devatānta', 'case': 'caturthī', 'result': 'tādarthya'},
           note='देवतान्तात् तादर्थ्ये यत्. तदर्थ एव तादर्थ्यम्.'),
    ),
    "5.4.25": (
        _c('pādyam, arghyam — and a conjunction gathering fifteen more',
           {'stem': 'pāda', 'case': 'caturthī', 'result': 'tādarthya'},
           note='पादार्घाभ्यां च. अनुक्तसमुच्चयार्थश्चकारः; यथादर्शनमन्यत्रापि प्रत्ययो भवति.'),
    ),
    "5.4.26": (
        _c('atithaya idam ātithyam — the hospitality due to a guest',
           {'stem': 'atithi', 'case': 'caturthī', 'result': 'tādarthya'},
           note='अतिथेर्ञ्यः.'),
    ),
    "5.4.27": (
        _c('deva eva devatā — and the gender overridden',
           {'stem': 'deva'},
           note='देवात् तल्. तादर्थ्य इति निवृत्तम्.'),
    ),
    "5.4.28": (
        _c('avir eva avikaḥ — one word, one affix',
           {'stem': 'avi'},
           note='अवेः कः.'),
    ),
    "5.4.29": (
        _c('yāva eva yāvakaḥ — and eleven entries with senses of their own',
           {'gana': 'yāvādi'},
           note='यावादिभ्यः कन्.'),
    ),
    "5.4.30": (
        _c('lohito maṇir lohitakaḥ — of a gem, and of nothing else',
           {'stem': 'lohita', 'result': 'maṇi'},
           note='लोहितान्मणौ. मणाविति किम्? लोहितः.'),
    ),
    "5.4.31": (
        _c('lohitakaḥ kopena — red with anger, not a red cow',
           {'stem': 'lohita', 'result': 'anitya-varṇa'},
           note='वर्णे चानित्ये. अनित्य इति किम्? लोहितो गौः.'),
    ),
    "5.4.32": (
        _c('lohitakaḥ kambalaḥ — of what has been dyed that colour',
           {'stem': 'lohita', 'result': 'rakta'},
           note='रक्ते. लाक्षादिना रक्ते यो लोहितशब्दः.'),
    ),
    "5.4.33": (
        _c('kālakaṃ mukham — a face gone dark with shame',
           {'stem': 'kāla', 'result': 'anitya-varṇa-rakta'},
           note='कालाच्च. वर्णे चानित्ये रक्त इति द्वयमप्यनुवर्तते.'),
    ),
    "5.4.34": (
        _c('vinaya eva vainayikaḥ — ṭhak after a list',
           {'gana': 'vinayādi'},
           note='विनयादिभ्यष्ठक्. विभाषाग्रहणेन विकल्प्यते प्रत्ययः.'),
    ),
    "5.4.35": (
        _c('vācikaṃ kathayati — a message, saying again what was said',
           {'stem': 'vāc', 'result': 'vyāhṛtārthā'},
           note='वाचो व्याहृतार्थायाम्. पूर्वमन्येनोक्तार्थत्वात् संदेशवाग् व्याहृतार्थेत्युच्यते.'),
    ),
    "5.4.36": (
        _c('kārmaṇam — what is done on hearing the message',
           {'stem': 'karman', 'result': 'tadyukta'},
           note='तद्युक्तात् कर्मणोऽण्. वाचिकं श्रुत्वा तथैव यत् कर्म क्रियते तत् कार्मणम्.'),
    ),
    "5.4.37": (
        _c('auṣadhaṃ pibati — the medicine, not the plant as a kind',
           {'stem': 'oṣadhi', 'result': 'ajāti'},
           note='ओषधेरजातौ. अजाताविति किम्? ओषधयः क्षेत्रे रूढा भवन्ति.'),
    ),
    "5.4.38": (
        _c('prajña eva prājñaḥ — and two feminines told apart',
           {'gana': 'prajñādi'},
           note='प्रज्ञादिभ्यश्च. यस्यास्तु प्रज्ञा विद्यते सा प्राज्ञा भवति.'),
    ),
    "5.4.39": (
        _c('mṛd eva mṛttikā — and the option runs throughout',
           {'stem': 'mṛd'},
           note='मृदस्तिकन्. विकल्पः सर्वत्रानुवर्तते.'),
    ),
    "5.4.40": (
        _c('mṛtsā, mṛtsnā — obligatory, read from the next rule',
           {'stem': 'mṛd', 'result': 'praśaṃsā'},
           note='सस्नौ प्रशंसायाम्. नित्यश्चायं प्रत्ययः, उत्तरसूत्रेऽन्यतरस्यांग्रहणात्.'),
    ),
    "5.4.41": (
        _c('vṛkatiḥ, jyeṣṭhatātiḥ — two words, two affixes, in order',
           {'stem': 'vṛka', 'result': 'praśaṃsā', 'usage': 'chandasi'},
           note='वृकज्येष्ठाभ्यां तिल्तातिलौ च छन्दसि, यथासंख्यम्.'),
    ),
    "5.4.42": (
        _c('bahuśo dadāti — and a supplement makes it a good omen',
           {'samjna': 'bahvalpārtha', 'case': 'kāraka'},
           note='बह्वल्पार्थाच्छस् कारकादन्यतरस्याम्. बह्वल्पार्थान् मङ्गलवचनम्.'),
    ),
    "5.4.43": (
        _c('dviśaḥ, kārṣāpaṇaśaḥ — a numeral, and a word for one thing',
           {'samjna': 'saṃkhyā-ekavacana', 'case': 'kāraka', 'result': 'vīpsā'},
           note='संख्यैकवचनाच्च वीप्सायाम्. एकोऽर्थ उच्यते येन तदेकवचनम्.'),
    ),
    "5.4.44": (
        _c('vāsudevataḥ prati — the affix 5.3.8 replaced',
           {'case': 'pañcamī', 'upapada': 'prati', 'result': 'pratiyoga'},
           note='प्रतियोगे पञ्चम्यास्तसिः. तसिप्रकरण आद्यादिभ्य उपसंख्यानम्.'),
    ),
    "5.4.45": (
        _c('grāmata āgacchati — and the passive shows which root',
           {'case': 'pañcamī', 'result': 'apādāna'},
           note='अपादाने चाहीयरुहोः. हीयत इति विकारनिर्देशो जहातेः प्रतिपत्त्यर्थः.'),
    ),
    "5.4.46": (
        _c('vṛttato ’tigṛhyate — and never with the agent',
           {'case': 'tṛtīyā-akartari', 'result': 'atigraha-avyathana-kṣepa'},
           note='अतिग्रहाव्यथनक्षेपेष्वकर्तरि तृतीयायाः. अकर्तरीति किम्? देवदत्तेन क्षिप्तः.'),
    ),
    "5.4.47": (
        _c('vṛttato hīyate — a plain statement, not a reproach',
           {'case': 'tṛtīyā-akartari', 'result': 'hīyamāna-pāpayoga'},
           note='हीयमानपापयोगाच्च. क्षेपे हि पूर्वेणैव सिद्धम्.'),
    ),
    "5.4.48": (
        _c('devā arjunato ’bhavan — taking sides',
           {'case': 'ṣaṣṭhī', 'result': 'vyāśraya'},
           note='षष्ठ्या व्याश्रये. नानापक्षसमाश्रयो व्याश्रयः.'),
    ),
    "5.4.49": (
        _c('pravāhikātaḥ kuru — do something for the dysentery',
           {'case': 'ṣaṣṭhī', 'result': 'roga-apanayana'},
           note='रोगाच्चापनयने. अपनयनं प्रतीकारः, चिकित्सेत्यर्थः.'),
    ),
    "5.4.50": (
        _c('śuklīkaroti — coming to be what one was not before',
           {'result': 'abhūtatadbhāva', 'upapada': 'kṛ-bhū-as'},
           note='अभूततद्भावे कृभ्वस्तियोगे संपद्यकर्तरि च्विः. कारकान्तरसंपत्तौ मा भूत्.'),
    ),
    "5.4.51": (
        _c('unmanīkaroti — the rule stated for the loss alone',
           {'gana': 'aruḥprabhṛti', 'result': 'abhūtatadbhāva', 'upapada': 'kṛ-bhū-as'},
           note='अरुर्मनश्चक्षुश्चेतोरहोरजसां लोपश्च. लोपमात्रार्थ आरम्भः.'),
    ),
    "5.4.52": (
        _c('agnisād bhavati śastram — turning wholly to fire',
           {'result': 'kārtsnya', 'upapada': 'kṛ-bhū-as'},
           note='विभाषा साति कार्त्स्न्ये. कार्त्स्न्य इति किम्? एकदेशेन पटः शुक्लीभवति.'),
    ),
    "5.4.53": (
        _c('agnisāt sampadyate — extent, as against completeness',
           {'result': 'abhividhi', 'upapada': 'kṛ-bhū-as-sampad'},
           note='अभिविधौ संपदा च. यत्रैकदेशेनापि सर्वा प्रकृतिर्विकारमापद्यते सोऽभिविधिः.'),
    ),
    "5.4.54": (
        _c('rājasāt karoti — made subject to someone',
           {'samjna': 'svāmivicaeṣa', 'result': 'tadadhīna', 'upapada': 'kṛ-bhū-as-sampad'},
           note='तदधीनवचने. तदधीनं तदायत्तं तत्स्वामिकमित्यर्थः.'),
    ),
    "5.4.55": (
        _c('brāhmaṇatrā karoti — where the thing is to be given',
           {'samjna': 'svāmivicaeṣa', 'result': 'tadadhīna-deya', 'upapada': 'kṛ-bhū-as-sampad'},
           note='देये त्रा च. देय इति किम्? राजसाद्भवति राष्ट्रम्.'),
    ),
    "5.4.56": (
        _c('devatrā gacchati — and the three verbs not carried here',
           {'stem': 'deva', 'case': 'dvitīyā-saptamī'},
           note='देवमनुष्यपुरुषपुरुमर्त्येभ्यो द्वितीयासप्तम्योर्बहुलम्. सामान्येन विधानम्.'),
    ),
    "5.4.57": (
        _c('paṭapaṭākaroti — and the doubling happens first',
           {'samjna': 'avyaktānukaraṇa-dvyajavarārdha', 'upapada': 'kṛ-bhū-as'},
           note='अव्यक्तानुकरणाद् द्व्यजवरार्धादनितौ डाच्. डाचि विवक्षिते द्विर्वचनमेव पूर्वं क्रियते.'),
    ),
    "5.4.58": (
        _c('dvitīyākaroti — ploughing it a second time',
           {'stem': 'dvitīya', 'result': 'kṛṣi', 'upapada': 'kṛ'},
           note='कृञो द्वितीयतृतीयशम्बबीजात् कृषौ. पुनः कृञ्ग्रहणं भ्वस्त्योर्निवृत्त्यर्थम्.'),
    ),
    "5.4.59": (
        _c('dviguṇākaroti kṣetram — ploughing the field twice over',
           {'samjna': 'saṃkhyā-guṇāntā', 'result': 'kṛṣi', 'upapada': 'kṛ'},
           note='संख्यायाश्च गुणान्तायाः. कृषाविति किम्? द्विगुणां करोति रज्जुम्.'),
    ),
    "5.4.60": (
        _c('samayākaroti — letting the time for a thing go by',
           {'stem': 'samaya', 'result': 'yāpanā', 'upapada': 'kṛ'},
           note='समयाच्च यापनायाम्. कर्तव्यस्यावसरप्राप्तिः समयः, तस्यातिक्रमणं यापना.'),
    ),
    "5.4.61": (
        _c('sapatrākaroti mṛgaṃ vyādhaḥ — feathers and all',
           {'stem': 'sapatra', 'result': 'ativyathana', 'upapada': 'kṛ'},
           note='सपत्रनिष्पत्रादतिव्यथने. सपत्रं शरमस्य शरीरे प्रवेशयतीत्यर्थः.'),
    ),
    "5.4.62": (
        _c('niṣkulākaroti paśūn — taking the insides out',
           {'stem': 'niṣkula', 'result': 'niṣkoṣaṇa', 'upapada': 'kṛ'},
           note='निष्कुलान्निष्कोषणे. निष्कोषणमन्तरवयवानां बहिर्निष्कासनम्.'),
    ),
    "5.4.63": (
        _c('sukhākaroti — falling in with another wishes',
           {'stem': 'sukha', 'result': 'ānulomya', 'upapada': 'kṛ'},
           note='सुखप्रियादानुलोम्ये. आनुलोम्यमनुकूलता, आराध्यचित्तानुवर्तनम्.'),
    ),
    "5.4.64": (
        _c('duḥkhākaroti bhṛtyaḥ — and crossing him instead',
           {'stem': 'duḥkha', 'result': 'prātilomya', 'upapada': 'kṛ'},
           note='दुःखात् प्रातिलोम्ये. प्रातिलोम्यं प्रतिकूलता.'),
    ),
    "5.4.65": (
        _c('śūlākaroti māṃsam — roasting the meat on a spit',
           {'stem': 'śūla', 'result': 'pāka', 'upapada': 'kṛ'},
           note='शूलात् पाके. पाक इति किम्? शूलं करोति कदन्नम्.'),
    ),
    "5.4.66": (
        _c('satyākaroti vaṇik bhāṇḍam — making his word good',
           {'stem': 'satya', 'result': 'aśapatha', 'upapada': 'kṛ'},
           note='सत्यादशपथे. क्वचित् तु शपथे च वर्तते, तस्यायं प्रतिषेधः.'),
    ),
    "5.4.67": (
        _c('madrākaroti — an auspicious shaving',
           {'stem': 'madra', 'result': 'parivāpaṇa', 'upapada': 'kṛ'},
           note='मद्रात् परिवापणे. परिवापणं मुण्डनम्. भद्राच्चेति वक्तव्यम्.'),
    ),
    "5.4.68": (
        _c('samāsāntāḥ — the endings a compound takes as a compound',
           {'result': 'kṛṣi', 'upapada': 'kṛ', 'stem': 'dvitīya'},
           note='समासान्ताः. समासान्ताश्चेति — among the affixes 5.4.7 named as obligatory.'),
    ),
    '5.4.69': (
        _c('surājā — no ending after a word of praise',
           {'upapada': 'pūjana'},
           note='न पूजनात् — no compound-final after a word of PRAISE. सुराजा, अतिराजा; सुगौः, अतिगौः. पूजायां स्वतिग्रहणं कर्तव्यम् — and the vārttika narrows it to सु and अति alone: इह'),
    ),
    '5.4.70': (
        _c('kiṃrājā — a fine king who does not protect',
           {'stem': 'kim', 'result': 'kṣepa'},
           note='किमः क्षेपे — none after किम् in CONTEMPT. किंराजा यो न रक्षति, a fine king who does not protect; किंगौर्यो न वहति. क्षेप इति किम्? कस्य राजा किंराजः'),
    ),
    '5.4.71': (
        _c('arājā, asakhā — none after a negative compound',
           {'samjna': 'tatpuruṣa', 'upapada': 'nañ'},
           note='नञस्तत्पुरुषात् — none after a negative तत्पुरुष. अराजा, असखा, अगौः. तत्पुरुषादिति किम्? अनृचो माणवकः, अधुरं शकटम् — those are बहुव्रीहि and keep theirs'),
    ),
    '5.4.72': (
        _c('apatham, apanthāḥ — and there the refusal is a choice',
           {'samjna': 'pathin-anta-tatpuruṣa', 'upapada': 'nañ'},
           note='पथो विभाषा — पूर्वेण नित्यः प्रतिषेधः प्राप्तो विकल्प्यते, what the rule before refused outright is here a choice. अपथम्, अपन्थाः'),
    ),
    '5.4.73': (
        _c('upadaśāḥ, dvitrāḥ — a number counted, two words apart',
           {'samjna': 'bahuvrīhi', 'result': 'saṃkhyeya'},
           note='बहुव्रीहौ संख्येये डजबहुगणात् — after a बहुव्रीहि meaning a NUMBER counted, बहु and गण excepted. उपदशाः, उपविंशाः; द्वित्राः, पञ्चषाः. संख्येय इति किम्? चित्रगुः.'),
    ),
    '5.4.74': (
        _c('ardharcaḥ, dvīpam — five endings, one exception',
           {'samjna': 'ṛk-pur-ap-dhur-pathin-anta'},
           note='ऋक्पूरब्धूःपथामानक्षे — after a compound ending in one of five words. बहुव्रीहाविति न स्वर्यते; सामान्येन विधानम्. अर्धर्चः; ललाटपुरम्; द्वीपम्, अन्तरीपम्, समीपम्;'),
    ),
    '5.4.75': (
        _c('pratilomam — and a verse adds four more bases',
           {'samjna': 'sāma-loman-anta', 'upapada': 'prati-anu-ava'},
           note='अच् प्रत्यन्ववपूर्वात् सामलोम्नः. प्रतिसामम्, अनुसामम्, अवसामम्; प्रतिलोमम्, अनुलोमम्, अवलोमम्. And a kārikā adds four more bases: कृष्णोदक्पाण्डुपूर्वाया'),
    ),
    '5.4.76': (
        _c('lavaṇākṣam — the eye as a part of a living body',
           {'samjna': 'akṣyanta'},
           note='अक्ष्णोऽदर्शनात् — after a compound ending in अक्षि when it does NOT mean the organ of sight. लवणाक्षम्, पुष्कराक्षम्. अदर्शनादिति किम्? ब्राह्मणाक्षि. कथं कबराक्षं'),
    ),
    '5.4.77': (
        _c('strīpuṃsau, mahokṣaḥ — thirty forms, nine kinds of compound',
           {'gana': 'acaturādi'},
           note='अचतुरविचतुरसुचतुर… — thirty-odd forms laid down, समासे व्यवस्थापि निपातनादेव प्रतिपत्तव्या, the KIND of compound got from the laying-down too. And the vṛtti sorts them:'),
    ),
    '5.4.78': (
        _c('brahmavarcasam — two words before it, and two more added',
           {'samjna': 'varcasanta', 'upapada': 'brahman-hastin'},
           note='ब्रह्महस्तिभ्यां वर्चसः. ब्रह्मवर्चसम्, हस्तिवर्चसम्. पल्यराजभ्यां चेति वक्तव्यम् — पल्यवर्चसम्, राजवर्चसम्'),
    ),
    '5.4.79': (
        _c('avatamasam — three preverbs before the word for dark',
           {'samjna': 'tamasanta', 'upapada': 'ava-sam-andha'},
           note='अवसमन्धेभ्यस्तमसः. अवतमसम्, सन्तमसम्, अन्धतमसम्'),
    ),
    '5.4.80': (
        _c('śvaḥśreyasam — a blessing, not a time',
           {'samjna': 'vasīyas-śreyas-anta', 'upapada': 'śvas'},
           note='श्वसो वसीयःश्रेयसः. श्वोवसीयसम्, श्वःश्रेयसम्, मयूरव्यंसकादित्वात् समासः. स्वभावाच्चेह श्वःशब्द उत्तरपदार्थस्य प्रशंसाम् आशीर्विषयाम् आचष्टे — the *tomorrow* here is not'),
    ),
    '5.4.81': (
        _c('anurahasam — three preverbs before the word for secret',
           {'samjna': 'rahasanta', 'upapada': 'anu-ava-tapta'},
           note='अन्ववतप्ताद् रहसः. अनुरहसम्, अवरहसम्, तप्तरहसम्'),
    ),
    '5.4.82': (
        _c('pratyurasam — only where the word stands as a locative',
           {'samjna': 'urasanta', 'result': 'saptamīstha', 'upapada': 'prati'},
           note='प्रतेरुरसः सप्तमीस्थात् — where the word उरस् stands in the sense of a LOCATIVE, उरसि वर्तते. प्रत्युरसम्. सप्तमीस्थादिति किम्? प्रतिगतमुरः प्रत्युरः'),
    ),
    '5.4.83': (
        _c('anugavaṃ yānam — a cart as long as an ox',
           {'stem': 'anugu', 'result': 'āyāma'},
           note='अनुगवमायामे — laid down, of LENGTH. अनुगवं यानम्, a cart as long as an ox. आयाम इति किम्? गवां पश्चाद् अनुगु'),
    ),
    '5.4.84': (
        _c('dvistāvā vediḥ — an altar twice the standard size',
           {'stem': 'dvistāva', 'result': 'vedi'},
           note='द्विस्तावा त्रिस्तावा वेदिः — laid down with the affix, the loss of the ending AND the compound. यावती प्रकृतौ वेदिस्ततो द्विगुणा वा त्रिगुणा वा कस्याञ्चिद् विकृतौ — an'),
    ),
    '5.4.85': (
        _c('prādhvo rathaḥ — a preverb before the word for a road',
           {'samjna': 'adhvananta', 'upapada': 'upasarga'},
           note='उपसर्गादध्वनः. प्रगतोऽध्वानं प्राध्वो रथः; निरध्वम्, प्रत्यध्वम्. उपसर्गादिति किम्? परमाध्वा, उत्तमाध्वा'),
    ),
    '5.4.86': (
        _c('dvyaṅgulam — and the heading for twenty rules to come',
           {'samjna': 'aṅguly-anta', 'upapada': 'saṃkhyā-avyaya'},
           note='तत्पुरुषस्याङ्गुलेः संख्याव्ययादेः. द्वे अङ्गुली प्रमाणमस्य द्व्यङ्गुलम्; and from an indeclinable, निरङ्गुलम्, अत्यङ्गुलम्. प्रमाणे लो द्विगोर्नित्यम् इति मात्रचो लोपः'),
    ),
    '5.4.87': (
        _c('ahorātraḥ — five words before the word for a night',
           {'samjna': 'rātry-anta', 'upapada': 'ahar-sarva-ekadeśa-saṃkhyāta-puṇya'},
           note='अहस्सर्वैकदेशसंख्यातपुण्याच्च रात्रेः — चकारात् संख्यादेरव्ययादेश्च, and अहर्ग्रहणं द्वन्द्वार्थम्. अहोरात्रः; सर्वरात्रः; a PART — पूर्वरात्रः, अपररात्रः; counted —'),
    ),
    '5.4.88': (
        _c('dvyahnaḥ — and no day can follow a day',
           {'samjna': 'ahan-anta', 'upapada': 'saṃkhyā-avyaya-sarvādi', 'before': 'ṭac'},
           note='अह्नोऽह्न एतेभ्यः — the word अहन् becomes अह्न before the टच् of 5.4.91, after the same bases the rule before named. संख्याव्ययादयः प्रक्रान्ताः सर्वनाम्ना'),
    ),
    '5.4.89': (
        _c('dvyahaḥ — but not of a collection',
           {'samjna': 'ahan-anta', 'result': 'samāhāra', 'upapada': 'saṃkhyā'},
           note='न संख्यादेः समाहारे — not where a numeral stands first and the compound is a COLLECTION. पूर्वेण प्राप्तः प्रतिषिध्यते. द्वे अहनी समाहृते द्व्यहः. समाहार इति किम्?'),
    ),
    '5.4.90': (
        _c('puṇyāhaḥ, ekāhaḥ — and *last* used for *holy*',
           {'samjna': 'ahan-anta', 'upapada': 'uttama-eka'},
           note='उत्तमैकाभ्यां च — and not after two more. उत्तमशब्दोऽन्त्यवचनः पुण्यशब्दमाचष्टे; पुण्यग्रहणमेव न कृतं वैचित्र्यार्थम् — *last* is used for *holy* just for variety.'),
    ),
    '5.4.91': (
        _c('mahārājaḥ — and the word order itself a signal',
           {'samjna': 'rājan-ahan-sakhi-anta-tatpuruṣa'},
           note='राजाहःसखिभ्यष्टच्. महाराजः, मद्रराजः; परमाहः; राजसखः, ब्राह्मणसखः. AND THE ORDER OF THE WORDS IN THE RULE IS A ज्ञापक. इह कस्माद् न भवति — मद्राणां राज्ञी मद्रराज्ञी? —'),
    ),
    '5.4.92': (
        _c('paramagavaḥ — provided no taddhita has been removed',
           {'samjna': 'go-anta-tatpuruṣa'},
           note='गोरतद्धितलुकि — after a तत्पुरुष ending in गो, provided no taddhita has been REMOVED in it. परमगवः; पञ्चगवम्, दशगवम्. अतद्धितलुकीति किम्? पञ्चभिर्गोभिः क्रीतः पञ्चगुः —'),
    ),
    '5.4.93': (
        _c('aśvorasam — the pick of the horses',
           {'samjna': 'uras-anta-tatpuruṣa', 'result': 'agrākhyā'},
           note='अग्राख्यायामुरसः — where उरस् means the CHIEF part, अग्रं प्रधानमुच्यते; यथा शरीरावयवानामुच्यत उरः प्रधानम्, एवमन्योऽपि प्रधानभूत उरःशब्देनोच्यते. अश्वोरसम्, the pick of'),
    ),
    '5.4.94': (
        _c('mahānasam — four words, each shown twice over',
           {'samjna': 'anas-aśman-ayas-saras-anta-tatpuruṣa', 'result': 'jāti-saṃjñā'},
           note='अनोऽश्मायस्सरसां जातिसंज्ञयोः — of a KIND or a NAME. उपानसम् a kind and महानसम् a name; अमृताश्म / पिण्डाश्म; कालायसम् / लोहितायसम्; मण्डूकसरसम् / जलसरसम् — four bases,'),
    ),
    '5.4.95': (
        _c('grāmatakṣaḥ — a carpenter for the whole village',
           {'samjna': 'takṣan-anta-tatpuruṣa', 'upapada': 'grāma-kauṭa'},
           note='ग्रामकौटाभ्यां च तक्ष्णः — जातिसंज्ञयोरिति नानुवर्तते. ग्रामतक्षः, बहूनां साधारणः, a carpenter who works for the whole village; कुट्यां भवः कौटः, तस्य तक्षा कौटतक्षः,'),
    ),
    '5.4.96': (
        _c('atiśvo varāhaḥ — one word, three senses',
           {'samjna': 'śvan-anta-tatpuruṣa', 'upapada': 'ati'},
           note='अतेः शुनः. अतिक्रान्तः श्वानम् अतिश्वो वराहः, जववानित्यर्थः, a boar that outruns a dog; अतिश्वः सेवकः, सुष्ठु स्वामिभक्तः; अतिश्वी सेवा, अतिनीचा. One word, three senses,'),
    ),
    '5.4.97': (
        _c('ākarṣaśvaḥ — a likeness, and the thing not alive',
           {'samjna': 'śvan-anta-tatpuruṣa', 'result': 'aprāṇin', 'upapada': 'upamāna'},
           note='उपमानादप्राणिषु — where श्वन् is what a thing is LIKENED to, and the thing is not alive. आकर्षः श्वेव आकर्षश्वः; फलकश्वः. उपमानादिति किम्? न श्वा अश्वा लोष्टः.'),
    ),
    '5.4.98': (
        _c('uttarasaktham — three words, and a likeness besides',
           {'samjna': 'sakthi-anta-tatpuruṣa', 'upapada': 'uttara-mṛga-pūrva-upamāna'},
           note='उत्तरमृगपूर्वाच्च सक्थ्नः — चकाराद् उपमानाच्च. उत्तरसक्थम्, मृगसक्थम्, पूर्वसक्थम्; and from a likeness, फलकमिव सक्थि फलकसक्थम्'),
    ),
    '5.4.99': (
        _c('dvināvam — a numeral compound of boats',
           {'samjna': 'nau-anta-dvigu'},
           note='नावो द्विगोः. द्वे नावौ समाहृते द्विनावम्; द्विनावधनः, द्विनावरूप्यम्. द्विगोरिति किम्? राजनौः. अतद्धितलुकीत्येव — पञ्चभिर्नौभिः क्रीतः पञ्चनौः'),
    ),
    '5.4.100': (
        _c('ardhanāvam — and the gender still from usage',
           {'samjna': 'nau-anta-tatpuruṣa', 'upapada': 'ardha'},
           note='अर्धाच्च. अर्धं नावो अर्धनावम्, and परवल्लिङ्गं न भवति, लोकाश्रयत्वाल् लिङ्गस्य — 2.4.26 would give it the gender of the second member and does not, gender resting on'),
    ),
    '5.4.101': (
        _c('dvikhāram, dvikhāri — by the Eastern teachers, so a choice',
           {'samjna': 'khārī-anta-dvigu-ardha'},
           note='खार्याः प्राचाम् — प्राचामाचार्याणां मतेन, so the affix is a choice. द्वे खार्यौ समाहृते द्विखारम्, द्विखारि; अर्धं खार्या अर्धखारम्, अर्धखारी'),
    ),
    '5.4.102': (
        _c('dvyañjalam — two numerals before the word',
           {'samjna': 'añjali-anta-dvigu', 'upapada': 'dvi-tri'},
           note='द्वित्रिभ्यामञ्जलेः. द्वावञ्जली समाहृतौ द्व्यञ्जलम्; त्र्यञ्जलम्. द्विगोरित्येव — द्वयोरञ्जलिर् द्व्यञ्जलिः. अतद्धितलुकीत्येव — द्वाभ्यामञ्जलिभ्यां क्रीतो द्व्यञ्जलिः.'),
    ),
    '5.4.103': (
        _c('hasticarme juhoti — a neuter compound, in the Veda',
           {'samjna': 'an-as-anta-napuṃsaka-tatpuruṣa', 'usage': 'chandasi'},
           note='अनसन्तान्नपुंसकाच्छन्दसि — after a NEUTER तत्पुरुष ending in अन् or अस्, in the Veda. हस्तिचर्मे जुहोति; देवच्छन्द॒सा॑नि, मनुष्यच्छन्द॒सम्. अनसन्तादिति किम्? बिल्वदारु'),
    ),
    '5.4.104': (
        _c('surāṣṭrabrahmaḥ — a brahman of a country',
           {'samjna': 'brahman-anta-tatpuruṣa', 'result': 'jānapadākhyā'},
           note='ब्रह्मणो जानपदाख्यायाम् — where the compound names a brahman of a COUNTRY, जनपदेषु भवो जानपदः. सुराष्ट्रेषु ब्रह्मा सुराष्ट्रब्रह्मः; अवन्तिब्रह्मः. योगविभागात्'),
    ),
    '5.4.105': (
        _c('kubrahmaḥ, kubrahmā — and here the ordinary brahmin',
           {'samjna': 'brahman-anta-tatpuruṣa', 'upapada': 'ku-mahat'},
           note='कुमहद्भ्यामन्यतरस्याम्. कुब्रह्मः, कुब्रह्मा; महाब्रह्मः, महाब्रह्मा. ब्राह्मणपर्यायो ब्रह्मन्शब्दः — and here the word is the ordinary one for a brahmin, not the'),
    ),
    '5.4.106': (
        _c('vāktvacam — a collective copulative compound',
           {'samjna': 'cu-ḍa-ṣa-ha-anta-dvandva', 'result': 'samāhāra'},
           note='द्वन्द्वाच्चुदषहान्तात् समाहारे — तत्पुरुषाधिकारो निवृत्तः, and the compound must be a COLLECTIVE द्वन्द्व and not an इतरेतरयोग. वाक्त्वचम्, स्रक्त्वचम्, श्रीस्रजम्,'),
    ),
    '5.4.107': (
        _c('upaśaradam — an indeclinable compound from a list',
           {'gana': 'śaratprabhṛti', 'samjna': 'avyayībhāva'},
           note='अव्ययीभावे शरत्प्रभृतिभ्यः. शरदः समीपम् उपशरदम्; प्रतिशरदम्, उपविपाशम्. अव्ययीभाव इति किम्? परमशरत्. येऽत्र झयन्ताः पठ्यन्ते तेषां नित्यार्थं ग्रहणम् — the stop-final'),
    ),
    '5.4.108': (
        _c('uparājam, adhyātmam — such a compound in one sound',
           {'samjna': 'an-anta', 'upapada': 'avyayībhāva'},
           note='अनश्च — after an अव्ययीभाव ending in अन्. उपराजम्, प्रतिराजम्; अध्यात्मम्, प्रत्यात्मम्'),
    ),
    '5.4.109': (
        _c('praticarmam, praticarma — and now the fixed rule is a choice',
           {'samjna': 'an-anta-napuṃsaka', 'upapada': 'avyayībhāva'},
           note='नपुंसकादन्यतरस्याम् — पूर्वेण नित्ये प्राप्ते विकल्प्यते. प्रतिचर्मम्, प्रतिचर्म; उपचर्मम्, उपचर्म'),
    ),
    '5.4.110': (
        _c('upanadam, upanadi — three feminine endings',
           {'samjna': 'nadī-paurṇamāsī-āgrahāyaṇī-anta', 'upapada': 'avyayībhāva'},
           note='नदीपौर्णमास्याग्रहायणीभ्यः. नद्याः समीपम् उपनदम्, उपनदि; उपपौर्णमासम्, उपपौर्णमासि'),
    ),
    '5.4.111': (
        _c('upasamidham, upasamit — a stop or an aspirate at the end',
           {'samjna': 'jhayanta', 'upapada': 'avyayībhāva'},
           note='झयः — झय इति प्रत्याहारग्रहणम्, a stop or an aspirate. उपसमिधम्, उपसमित्; उपदृषदम्, उपदृषत्'),
    ),
    '5.4.112': (
        _c("antargiram — by one teacher's opinion",
           {'samjna': 'giry-anta', 'upapada': 'avyayībhāva'},
           note='गिरेश्च सेनकस्य — सेनकग्रहणं पूजार्थम्; विकल्पोऽनुवर्तत एव. अन्तर्गिरम्, अन्तर्गिरि; उपगिरम्, उपगिरि'),
    ),
    '5.4.113': (
        _c('dīrghasakthaḥ — and the case-endings fit the sense badly',
           {'samjna': 'bahuvrīhi-svāṅga', 'upapada': 'sakthi-akṣi'},
           note='बहुव्रीहौ सक्थ्यक्ष्णोः स्वाङ्गात् षच् — the बहुव्रीहि heading opens, आ पादपरिसमाप्तेर् अनुवर्तते. दीर्घसक्थः; कल्याणाक्षः, लोहिताक्षः, विशालाक्षः. अयमर्थोऽभिप्रेतः।'),
    ),
    '5.4.114': (
        _c('dvyaṅgulaṃ dāru — a winnowing-stick with prongs',
           {'samjna': 'bahuvrīhi', 'result': 'dāru', 'upapada': 'aṅguli'},
           note='अङ्गुलेर्दारुणि — of a piece of WOOD. द्व्यङ्गुलं दारु, अङ्गुलिसदृशावयवं धान्यादीनां विक्षेपणकाष्ठम् उच्यते, a winnowing-stick with finger-like prongs. And where two'),
    ),
    '5.4.115': (
        _c('dvimūrdhaḥ — two numerals before the word for a head',
           {'samjna': 'bahuvrīhi', 'upapada': 'dvi-tri-mūrdhan'},
           note='द्वित्रिभ्यां ष मूर्ध्नः. द्विमूर्धः, त्रिमूर्धः. द्वित्रिभ्यामिति किम्? उच्चैर्मूर्धा'),
    ),
    '5.4.116': (
        _c('kalyāṇīpañcamā rātrayaḥ — and the ordinal the principal word',
           {'samjna': 'bahuvrīhi', 'upapada': 'pūraṇī-pramāṇī'},
           note='अप् पूरणीप्रमाण्योः. कल्याणी पञ्चमी आसां रात्रीणां कल्याणीपञ्चमा रात्रयः; स्त्री प्रमाणी एषां स्त्रीप्रमाणाः कुटुम्बिनः, भार्याप्रधानाः. अपि प्रधानपूरणीग्रहणं कर्तव्यम्'),
    ),
    '5.4.117': (
        _c('antarlomaḥ prāvāraḥ — a cloak with the fleece inside',
           {'samjna': 'bahuvrīhi', 'upapada': 'antar-bahis-loman'},
           note='अन्तर्बहिर्भ्यां च लोम्नः. अन्तर्लोमः प्रावारः, a cloak with the fleece inside; बहिर्लोमः पटः'),
    ),
    '5.4.118': (
        _c('druṇasaḥ, gonasaḥ — a name, and not from one word',
           {'samjna': 'bahuvrīhi', 'result': 'saṃjñā', 'upapada': 'nāsikā'},
           note='अञ्नासिकायाः संज्ञायां नसं चास्थूलात् — the affix AND the change of नासिका to नस्, where the whole word is a NAME and the first member is not स्थूल. द्रुणसः,'),
    ),
    '5.4.119': (
        _c('unnasaḥ, praṇasaḥ — a preverb, and no name needed',
           {'samjna': 'bahuvrīhi', 'upapada': 'upasarga-nāsikā'},
           note='उपसर्गाच्च — असंज्ञार्थं वचनम्, and here no name is needed. उन्नता नासिकास्य उन्नसः; प्रणसः, by 8.4.28 उपसर्गाद् बहुलम्. वेर्ग्रो वक्तव्यः — विगता नासिकास्य विग्रः'),
    ),
    '5.4.120': (
        _c('suprātaḥ, caturaśraḥ — eight compounds laid down',
           {'gana': 'suprātādi', 'samjna': 'bahuvrīhi'},
           note='सुप्रातसुश्वसुदिवशारिकुक्षचतुरश्रैणीपदाजपदप्रोष्ठपदाः — eight बहुव्रीहि compounds laid down with the affix. अन्यदपि च टिलोपादिकं निपातनादेव सिद्धम्. सुप्रा॒तः, सुश्वः,'),
    ),
    '5.4.121': (
        _c('ahalaḥ, ahaliḥ — three words before either of two',
           {'samjna': 'bahuvrīhi', 'upapada': 'nañ-dus-su-hali-sakthi'},
           note='नञ्दुःसुभ्यो हलिसक्थ्योरन्यतरस्याम्. अहलः, अहलिः; दुर्हलः, सुहलः; असक्थः, असक्थिः. हलिशक्त्योरिति केचित् पठन्ति — and some read शक्ति for सक्थि: अशक्तः, अशक्तिः'),
    ),
    '5.4.122': (
        _c('aprajāḥ, sumedhāḥ — always, and the *always* read as a hint',
           {'samjna': 'bahuvrīhi', 'upapada': 'nañ-dus-su-prajā-medhā'},
           note='नित्यमसिच् प्रजामेधयोः. अप्रजाः, दुष्प्रजाः, सुप्रजाः; अमेधाः, दुर्मेधाः, सुमेधाः. नित्यग्रहणं किम्? यावता पूर्वसूत्रे अन्यतरस्यांग्रहणं नैव स्वर्यते? एवं तर्हि'),
    ),
    '5.4.123': (
        _c('bahuprajāḥ — one form laid down for the Veda',
           {'stem': 'bahuprajā', 'samjna': 'bahuvrīhi', 'usage': 'chandasi'},
           note='बहुप्रजाश्छन्दसि — laid down for the Veda. बहुप्॒रजा निर्ऋ॑ति॒मावि॑वेश (ऋ० १.१६४.३२). छन्दसीति किम्? बहुप्रजो ब्राह्मणः'),
    ),
    '5.4.124': (
        _c('kalyāṇadharmā — and *alone* describes the word before',
           {'samjna': 'bahuvrīhi', 'upapada': 'kevala-dharma'},
           note='धर्मादनिच् केवलात्. कल्याणधर्मा, प्रियधर्मा. केवलादिति किम्? परमः स्वो धर्मोऽस्य परमस्वधर्मः, and the vṛtti asks how a three-word बहुव्रीहि is kept out at all: केवलादिति'),
    ),
    '5.4.125': (
        _c('sujambhā devadattaḥ — well fed, or well toothed',
           {'stem': 'jambha', 'samjna': 'bahuvrīhi', 'upapada': 'su-harita-tṛṇa-soma'},
           note='जम्भा सुहरिततृणसोमेभ्यः — the compound-final already made, and laid down. जम्भशब्दोऽभ्यवहार्यवाची दन्तविशेषवाची च — the word means FOOD and also a kind of TOOTH. सुजम्भा'),
    ),
    '5.4.126': (
        _c('dakṣiṇermā mṛgaḥ — a deer wounded by the hunter',
           {'stem': 'dakṣiṇerman', 'samjna': 'bahuvrīhi', 'result': 'lubdhayoga'},
           note='दक्षिणेर्मा लुब्धयोगे — लुब्धो व्याधः; ईर्मं व्रणमुच्यते. दक्षिणेर्मा मृगः, दक्षिणमङ्गं व्रणितमस्य व्याधेन, a deer wounded on the right side by the hunter. लुब्धयोग इति'),
    ),
    '5.4.127': (
        _c("keśākeśi — a fight of pulling one another's hair",
           {'samjna': 'bahuvrīhi', 'result': 'karmavyatihāra'},
           note='इच् कर्मव्यतिहारे — of a fight in which each does to the other what the other does to him, the बहुव्रीहि of 2.2.27. केशेषु केशेषु गृहीत्वा इदं युद्धं प्रवृत्तं केशाकेशि,'),
    ),
    '5.4.128': (
        _c('dvidaṇḍi praharati — a dative of purpose, not an ablative',
           {'gana': 'dvidaṇḍyādi', 'samjna': 'bahuvrīhi'},
           note='द्विदण्ड्यादिभ्यश्च — द्विदण्ड्यादिभ्य इति तादर्थ्ये एषा चतुर्थी, न पञ्चमी; द्विदण्ड्याद्यर्थम् इच् प्रत्ययो भवति — the case in the rule is a dative of purpose and not'),
    ),
    '5.4.129': (
        _c('prajñuḥ, saṃjñuḥ — the word for a knee, changed',
           {'samjna': 'bahuvrīhi', 'upapada': 'pra-sam-jānu'},
           note='प्रसम्भ्यां जानुनोर्ज्ञुः. प्रकृष्टे जानुनी अस्य प्रज्ञुः; संज्ञुः'),
    ),
    '5.4.130': (
        _c('ūrdhvajānuḥ, ūrdhvajñuḥ — and after one more, optionally',
           {'samjna': 'bahuvrīhi', 'upapada': 'ūrdhva-jānu'},
           note='ऊर्ध्वाद् विभाषा. ऊर्ध्वजानुः, ऊर्ध्वज्ञुः'),
    ),
    '5.4.131': (
        _c('kuṇḍodhnī — and a supplement confines it to the feminine',
           {'samjna': 'bahuvrīhi', 'result': 'strī', 'upapada': 'ūdhas'},
           note='ऊधसोऽनङ्. कुण्डमिव ऊधोऽस्याः कुण्डोध्नी; घटोध्नी. ऊधसोऽनङि स्त्रीग्रहणं कर्तव्यम् — and a vārttika adds *in the feminine*: इह मा भूत् — महोधाः पर्जन्यः'),
    ),
    '5.4.132': (
        _c('śārṅgadhanvā — a compound ending in the word for a bow',
           {'samjna': 'bahuvrīhi', 'upapada': 'dhanus'},
           note='धनुषश्च. शार्ङ्गं धनुरस्य शार्ङ्गधन्वा; गाण्डीवधन्वा, पुष्पधन्वा, अधिज्यधन्वा'),
    ),
    '5.4.133': (
        _c('śatadhanuḥ, śatadhanvā — and where the word is a name, a choice',
           {'samjna': 'bahuvrīhi', 'result': 'saṃjñā', 'upapada': 'dhanus'},
           note='वा संज्ञायाम् — पूर्वेण नित्यः प्राप्तो विकल्प्यते. शतधनुः, शतधन्वा; दृढधनुः, दृढधन्वा'),
    ),
    '5.4.134': (
        _c('yuvajāniḥ — the word for a wife, changed',
           {'samjna': 'bahuvrīhi', 'upapada': 'jāyā'},
           note='जायाया निङ्. युवतिर्जाया यस्य युवजानिः; वृद्धजानिः'),
    ),
    '5.4.135': (
        _c('udgandhiḥ, sugandhiḥ — and the word must end the compound',
           {'samjna': 'bahuvrīhi', 'upapada': 'ut-pūti-su-surabhi-gandha'},
           note='गन्धस्येदुत्पूतिसुसुरभिभ्यः. तकार उच्चारणार्थः. उद्गतो गन्धोऽस्य उद्गन्धिः; पूतिगन्धिः, सुगन्धिः, सुरभिगन्धिः. एतेभ्य इति किम्? तीव्रगन्धो वातः. गन्धस्येत्वे'),
    ),
    '5.4.136': (
        _c('sūpagandhi bhojanam — food with a little sauce in it',
           {'samjna': 'bahuvrīhi', 'result': 'alpākhyā', 'upapada': 'gandha'},
           note='अल्पाख्यायाम् — where गन्ध means A LITTLE. अल्पपर्यायो गन्धशब्दः. सूपोऽल्पोऽस्मिन् सूपगन्धि भोजनम्, food with a little sauce in it; घृतगन्धि, क्षीरगन्धि'),
    ),
    '5.4.137': (
        _c('padmagandhiḥ — a word it is likened to',
           {'samjna': 'bahuvrīhi', 'upapada': 'upamāna-gandha'},
           note='उपमानाच्च. पद्मस्येव गन्धोऽस्य पद्मगन्धिः; उत्पलगन्धिः, करीषगन्धिः'),
    ),
    '5.4.138': (
        _c('vyāghrapāt — a loss counting as a compound-final',
           {'samjna': 'bahuvrīhi', 'upapada': 'upamāna-pāda'},
           note='पादस्य लोपोऽहस्त्यादिभ्यः — the loss of पाद, and स्थानिद्वारेण लोपस्य समासान्तता विज्ञायते: a LOSS counts as a compound-final through what it stands in place of.'),
    ),
    '5.4.139': (
        _c('kumbhapadī, śatapadī — the forms listed with the loss made',
           {'gana': 'kumbhapadyādi', 'samjna': 'bahuvrīhi', 'result': 'strī'},
           note='कुम्भपदीषु च — कुम्भपदीप्रभृतयः कृतपादलोपाः समुदाया एव पठ्यन्ते, the forms listed WITH the loss already made. समुदायपाठस्य च प्रयोजनं विषयनियमः — स्त्रियामेव, तत्र'),
    ),
    '5.4.140': (
        _c('dvipāt, supāt — a numeral or one other word first',
           {'samjna': 'bahuvrīhi', 'upapada': 'saṃkhyā-su-pāda'},
           note='संख्यासुपूर्वस्य. द्वौ पादावस्य द्विपात्; त्रिपात्, सुपात्'),
    ),
    '5.4.141': (
        _c('dvidan, sudan kumāraḥ — a boy with his full set',
           {'samjna': 'bahuvrīhi', 'result': 'vayas', 'upapada': 'saṃkhyā-su-danta'},
           note='वयसि दन्तस्य दतृ — where an AGE is meant. ऋकार उगित्कार्यार्थः. द्वौ दन्तावस्य द्विदन्; सुदन् कुमारः, a boy with a full set. वयसीति किम्? द्विदन्तः कुञ्जरः, सुदन्तो'),
    ),
    '5.4.142': (
        _c('ubhayādataḥ — and in the Veda',
           {'samjna': 'bahuvrīhi', 'upapada': 'danta', 'usage': 'chandasi'},
           note='छन्दसि च. पत्रदतमालभेत; उ॒भ॒याद॑तः (ऋ० १०.९०.१०) आलभते'),
    ),
    '5.4.143': (
        _c('ayodatī, phāladatī — the feminine, where the word is a name',
           {'samjna': 'bahuvrīhi', 'result': 'strī-saṃjñā', 'upapada': 'danta'},
           note='स्त्रियां संज्ञायाम् — in the feminine, where the whole word is a name. अयोदती, फालदती. संज्ञायामिति किम्? समदन्ती, स्निग्धदन्ती'),
    ),
    '5.4.144': (
        _c('śyāvadan, śyāvadantaḥ — and after two words, optionally',
           {'samjna': 'bahuvrīhi', 'upapada': 'śyāva-aroka-danta'},
           note='विभाषा श्यावारोकाभ्याम्. श्यावदन्, श्यावदन्तः; अरोकदन्, अरोकदन्तः — अरोको निर्दीप्तिः, without lustre'),
    ),
    '5.4.145': (
        _c('śuddhadan, vṛṣadan — one ending and four words more',
           {'samjna': 'bahuvrīhi', 'upapada': 'agrānta-śuddha-śubhra-vṛṣa-varāha-danta'},
           note='अग्रान्तशुद्धशुभ्रवृषवराहेभ्यश्च. कुड्मलाग्रदन्, शुद्धदन्, शुभ्रदन्, वृषदन्, वराहदन्, each beside its दन्त form. अनुक्तसमुच्चयार्थश्चकारः — अहिदन्, मूषिकदन्, गर्दभदन्,'),
    ),
    '5.4.146': (
        _c('asaṃjātakakut — a stage of life, glossed five ways',
           {'samjna': 'bahuvrīhi', 'result': 'avasthā', 'upapada': 'kakuda'},
           note='ककुदस्यावस्थायां लोपः — where a STAGE OF LIFE is meant, कालादिकृता वस्तुधर्मा वयःप्रभृतयो ऽवस्थेत्युच्यते. And the vṛtti gives five and glosses each: असंजातककुत्, a'),
    ),
    '5.4.147': (
        _c('trikakut parvataḥ — the name of one mountain',
           {'stem': 'trikakud', 'samjna': 'bahuvrīhi', 'result': 'parvata'},
           note='त्रिककुत् पर्वते. त्रिककुत् पर्वतः, and न च सर्वस्त्रिशिखरः पर्वतस्त्रिककुत्; किं तर्हि? संज्ञैषा पर्वतविशेषस्य — not every three-peaked mountain, but the name of one.'),
    ),
    '5.4.148': (
        _c('utkākut, vikākut — the palate, lost after two preverbs',
           {'samjna': 'bahuvrīhi', 'upapada': 'ud-vi-kākuda'},
           note='उद्विभ्यां काकुदस्य — तालु काकुदम् उच्यते, the palate. उत्काकुत्, विकाकुत्'),
    ),
    '5.4.149': (
        _c('pūrṇakākut — and after one more, optionally',
           {'samjna': 'bahuvrīhi', 'upapada': 'pūrṇa-kākuda'},
           note='पूर्णाद् विभाषा. पूर्णकाकुत्, पूर्णकाकुदः'),
    ),
    '5.4.150': (
        _c('suhṛd mitram — a friend, and a tender-hearted man',
           {'stem': 'suhṛd', 'samjna': 'bahuvrīhi', 'result': 'mitra-amitra'},
           note='सुहृद्दुर्हृदौ मित्रामित्रयोः, यथासंख्यम्. शोभनं हृदयमस्य सुहृद् मित्रम्; दुष्टं हृदयमस्य दुर्हृद् अमित्रम्. मित्रामित्रयोरिति किम्? सुहृदयः कारुणिकः, a tender-hearted'),
    ),
    '5.4.151': (
        _c('vyūḍhoraskaḥ — and four of the list as inflected words',
           {'gana': 'uraḥprabhṛti', 'samjna': 'bahuvrīhi'},
           note='उरःप्रभृतिभ्यः कप्. व्यूढोरस्कः, प्रियसर्पिष्कः, अवमुक्तोपानत्कः. AND FOUR OF THE LIST ARE READ AS INFLECTED WORDS. पुमान् अनड्वान् पयो नौर्लक्ष्मीरिति विभक्त्यन्ताः'),
    ),
    '5.4.152': (
        _c('bahudaṇḍikā śālā — one affix at the end, in the feminine',
           {'samjna': 'bahuvrīhi', 'result': 'strī', 'upapada': 'in-anta'},
           note='इनः स्त्रियाम्. बहवो दण्डिनोऽस्यां शालायां बहुदण्डिका शाला; बहुस्वामिका नगरी, बहुवाग्ग्मिका सभा. स्त्रियामिति किम्? बहुदण्डी राजा, बहुदण्डिकः by 5.4.154'),
    ),
    '5.4.153': (
        _c('bahukumārīko deśaḥ — a feminine of one class, or one vowel',
           {'samjna': 'bahuvrīhi', 'upapada': 'nadī-ṛkārānta'},
           note='नद्यृतश्च. बह्व्यः कुमार्योऽस्मिन् देशे बहुकुमारीको देशः; बहुब्रह्मबन्धूकः; and from an ऋ-final, बहुकर्तृकः. तकारो मुखसुखोच्चारणार्थः'),
    ),
    '5.4.154': (
        _c('bahukhaṭvakaḥ — whatever the rules before have not reached',
           {'samjna': 'bahuvrīhi', 'result': 'śeṣa'},
           note='शेषाद् विभाषा — यस्माद् बहुव्रीहेः समासान्तो न विहितः स शेषः, whatever the rules before have not reached. बहुखट्वकः, बहुमालकः, and beside them बहुखट्वाकः and बहुखट्वः —'),
    ),
    '5.4.155': (
        _c('viśvadevaḥ — but not where the whole word is a name',
           {'samjna': 'bahuvrīhi', 'result': 'saṃjñā'},
           note='न संज्ञायाम् — पूर्वेण प्राप्तः प्रतिषिध्यते. विश्वे देवा अस्य विश्वदेवः; विश्वयशाः'),
    ),
    '5.4.156': (
        _c('bahuśreyān — and here every one of the rules is refused',
           {'samjna': 'bahuvrīhi', 'upapada': 'īyas-anta'},
           note='ईयसश्च — सर्वा प्राप्तिः प्रतिषिध्यते, every one of the rules is refused. बहुश्रेयान् against 5.4.154, बहुश्रेयसी against 5.4.153. ह्रस्वत्वमपि न भवति, ईयसो बहुव्रीहौ'),
    ),
    '5.4.157': (
        _c('subhrātā — a brother who is praised',
           {'samjna': 'bahuvrīhi', 'result': 'vandita', 'upapada': 'bhrātṛ'},
           note='वन्दिते भ्रातुः — वन्दितः स्तुतः पूजितः. शोभनो भ्रातास्य सुभ्राता. वन्दित इति किम्? मूर्खभ्रातृकः, दुष्टभ्रातृकः — where the brother is no credit to him, the affix comes'),
    ),
    '5.4.158': (
        _c('hatamātā, hatasvasā — one class of vowel, in the Veda',
           {'samjna': 'bahuvrīhi', 'upapada': 'ṛvarṇānta', 'usage': 'chandasi'},
           note='ऋतश्छन्दसि. हता मातास्य ह॒तमा॑ता॑; हतपिता, ह॒तस्व॑सा, सुहो॑ता'),
    ),
    '5.4.159': (
        _c('bahunāḍiḥ kāyaḥ — and a lute with many strings keeps its own',
           {'samjna': 'bahuvrīhi', 'result': 'svāṅga', 'upapada': 'nāḍī-tantrī'},
           note='नाडीतन्त्र्योः स्वाङ्गे — where the two words name PARTS OF THE BODY, धमनीवचनस्तन्त्रीशब्दः. बहुनाडिः कायः, a body with many vessels; बहुतन्त्रीर्ग्रीवा. स्वाङ्ग इति'),
    ),
    '5.4.160': (
        _c('niṣpravāṇiḥ paṭaḥ — cloth just off the loom',
           {'stem': 'niṣpravāṇi', 'samjna': 'bahuvrīhi'},
           note='निष्प्रवाणिश्च — the last sūtra of the chapter, and a refusal laid down. प्रोयतेऽस्यामिति प्रवाणी; प्रवयन्ति तयेति वा प्रवाणी; करणसाधनोऽयं ल्युट्; तन्तुवायशलाका भण्यते —'),
    ),
    '6.1.3': (
        _c('उन्दिदिषति (undidiṣati) — the न् left out of the copy',
           {'sound': 'n', 'at': 'saṃyogādi'},
           note="न न्द्राः संयोगादयः — and the rule needs 6.1.2's द्वितीयस्य carried down: द्वितीयस्येति वर्तते. Of a vowel-initial root it is the SECOND one-vowelled portion that"),
    ),
    '6.1.4': (
        _c('पपाच (papāca) — the first half is the अभ्यास',
           {'part': 'pūrva'},
           note='पूर्वोऽभ्यासः — the first of the two is the अभ्यास, and this is the term every rule from 7.4.58 onward is addressed to. पपाच, पिपक्षति, पापच्यते, जुहोति, अपीपचत्.'),
    ),
    '6.1.5': (
        _c('ददति (dadati) — both halves together are the अभ्यस्त',
           {'part': 'ubhe'},
           note='उभे अभ्यस्तम् — the two together are the अभ्यस्त. ददति, ददत्, दधतु.'),
    ),
    '6.1.6': (
        _c('जक्षति (jakṣati) — called doubled without any doubling',
           {'root': 'jakṣ'},
           note='जक्षित्यादयः षट् — seven roots are CALLED अभ्यस्त without any rule having doubled them. जक्षति, जाग्रति, दरिद्रति, चकासति, शासति, दीध्यते, वेव्यते.'),
    ),
    '6.1.7': (
        _c('तूतुजानः (tūtujānaḥ) — a long vowel in the copy, in the Veda',
           {'root': 'tuj', 'chandasi': True},
           note="तुजादीनां दीर्घोऽभ्यासस्य — the copy's vowel comes out long: तूतुजानः, मामहानः, दाधान, मीमाय, दाधार, तूताव."),
    ),
    '6.1.8': (
        _c('पपाच (papāca) — doubling before the perfect ending',
           {'before': 'liṭ'},
           note='लिटि धातोरनभ्यासस्य — before लिट्, a root that is not already a copy doubles, first portion or second according to 6.1.1 and 6.1.2. पपाच, पपाठ, प्रोर्णुनाव.'),
    ),
    '6.1.10': (
        _c('जुहोति (juhoti) — doubling where शप् has been dropped',
           {'before': 'ślu'},
           note='श्लौ — where श्लु has taken the शप् away, the root doubles: जुहोति, बिभेति, जिह्रेति. श्लु is the mark of the third class, and the doubling is what the class sounds'),
    ),
    '6.1.11': (
        _c('अपीपचत् (apīpacat) — doubling before the aorist चङ्',
           {'before': 'caṅ'},
           note='चङि — before the चङ् of the reduplicated aorist: अपीपचत्, अपीपठत्, आटिटत्, आशिशत्, आर्दिदत्.'),
    ),
    '6.1.12': (
        _c('दाश्वान् (dāśvān) — a participle that never doubles',
           {'root': 'dāś', 'before': 'kvasu'},
           note='दाश्वान् साह्वान् मीढ्वांश्च — three forms laid down whole, in the Vedic corpus and in ordinary speech alike: छन्दसि भाषायां च अविशेषेण निपात्यन्ते. Each is क्वसु on a'),
    ),
    '6.1.13': (
        _c('कारीषगन्धीपुत्रः (kārīṣagandhīputraḥ) — her son',
           {'root': 'ṣyaṅ', 'uttarapada': 'putra', 'samasa': 'tatpuruṣa'},
           note="ष्यङः संप्रसारणं पुत्रपत्योस्तत्पुरुषे — and the section opens on a base that is not a root at all. ष्यङ् is 4.1.78's feminine affix, and its य् vocalises when पुत्र or"),
    ),
    '6.1.14': (
        _c('कारीषगन्धीबन्धुः (kārīṣagandhībandhuḥ) — a man with her for kinswoman',
           {'root': 'ṣyaṅ', 'uttarapada': 'bandhu', 'samasa': 'bahuvrīhi'},
           note='बन्धुनि बहुव्रीहौ — the same vocalisation before बन्धु, and now the compound must be a बहुव्रीहि: कारीषगन्ध्या बन्धुरस्य कारीषगन्धीबन्धुः. Where it is a तत्पुरुष —'),
    ),
    '6.1.15': (
        _c('उक्तः (uktaḥ) — the व् of वच् turned into a vowel',
           {'root': 'vac', 'before': 'kit'},
           note='वचिस्वपियजादीनां किति — and the ष्यङ् of the two rules before drops away. Eleven roots: वच्, स्वप्, and the यजादि that close the भ्वादि gaṇa — यजादयो यज'),
    ),
    '6.1.16': (
        _c('गृह्णाति (gṛhṇāti) — before an affix marked ङ्',
           {'root': 'grah', 'before': 'ṅit'},
           note='ग्रहिज्यावयिव्यधिवष्टिविचतिवृश्चतिपृच्छतिभृज्जतीनां ङिति च — nine more roots, and the च carries किति down from the rule before, so these vocalise before EITHER marker.'),
    ),
    '6.1.17': (
        _c('उवाच (uvāca) — the copy vocalised in the perfect',
           {'root': 'vac', 'before': 'liṭ'},
           note="लिट्यभ्यासस्योभयेषाम् — and now the vocalisation lands not on the root but on the COPY. Both lists, 6.1.15's and 6.1.16's, before लिट्: उवाच, सुष्वाप, इयाज, उवाप;"),
    ),
    '6.1.18': (
        _c('असूषुपत् (asūṣupat) — the causative of स्वप् before चङ्',
           {'root': 'svāpi', 'before': 'caṅ'},
           note='स्वापेश्चङि — and the root named is the CAUSATIVE, स्वापेरिति स्वपेर्ण्यन्तस्य ग्रहणम्. Before चङ्: असूषुपत्, असूषुपताम्, असूषुपन्.'),
    ),
    '6.1.19': (
        _c('सोषुप्यते (soṣupyate) — before the intensive यङ्',
           {'root': 'svap', 'before': 'yaṅ'},
           note="स्वपिस्यमिव्येञां यङि — three roots before यङ्: सोषुप्यते, सेसिम्यते, वेवीयते. स्वप् and व्येञ् are already in 6.1.15's list, but that rule wants a कित् affix and यङ् is"),
    ),
    '6.1.20': (
        _c('वावश्यते (vāvaśyate) — वश् keeping its semivowel',
           {'root': 'vaś', 'before': 'yaṅ'},
           note="न वशः — the first refusal of the section. वश् is one of 6.1.16's nine and would vocalise before the ङित् यङ्; here it does not: वावश्यते, वावश्येते, वावश्यन्ते."),
    ),
    '6.1.21': (
        _c('चेकीयते (cekīyate) — की standing in for चाय्',
           {'root': 'cāy', 'before': 'yaṅ'},
           note='चायः की — and the rule substitutes a finished form instead of ordering a vocalisation. Before यङ्: चेकीयते, चेकीयेते, चेकीयन्ते.'),
    ),
    '6.1.22': (
        _c('स्फीतः (sphītaḥ) — स्फी before a निष्ठा affix',
           {'root': 'sphāy', 'before': 'niṣṭhā'},
           note='स्फायः स्फी निष्ठायाम् — स्फीतः, स्फीतवान्.'),
    ),
    '6.1.23': (
        _c('प्रस्तीतः (prastītaḥ) — स्त्या with प्र standing first',
           {'root': 'styā', 'before': 'niṣṭhā', 'pre': 'pra'},
           note='स्त्यः प्रपूर्वस्य — प्रस्तीतः, प्रस्तीतवान्, and both स्त्यै and ष्ट्यै are meant, the two having the same shape स्त्या.'),
    ),
    '6.1.24': (
        _c('शीनं घृतम् (śīnaṃ ghṛtam) — butter gone stiff',
           {'root': 'śyā', 'before': 'niṣṭhā', 'result': 'dravamūrti'},
           note='द्रवमूर्तिस्पर्शयोः श्यः — and a SENSE decides it. द्रवमूर्ति is a liquid gone stiff: शीनं घृतम्, शीना वसा, शीनं मेदः — द्रवावस्थायाः काठिन्यं गतम्.'),
    ),
    '6.1.25': (
        _c('प्रतिशीनः (pratiśīnaḥ) — after प्रति, in any sense at all',
           {'root': 'śyā', 'before': 'niṣṭhā', 'pre': 'prati'},
           note='प्रतेश्च — the same root after प्रति, and now no sense is required: प्रतिशीनः, प्रतिशीनवान्. The vṛtti says why the rule exists at all — द्रवमूर्तिस्पर्शाभ्यामन्यत्रापि'),
    ),
    '6.1.26': (
        _c('अभिशीनम् (abhiśīnam) — beside अभिश्यानम्',
           {'root': 'śyā', 'before': 'niṣṭhā', 'pre': 'abhi'},
           note='विभाषाभ्यवपूर्वस्य — after अभि or अव the vocalisation is a choice: अभिशीनम्, अभिश्यानम्; अवशीनम्, अवश्यानम्.'),
    ),
    '6.1.27': (
        _c('शृतं क्षीरम् (śṛtaṃ kṣīram) — milk that has been boiled',
           {'root': 'śrā', 'before': 'kta', 'result': 'pāka'},
           note='शृतं पाके — the whole form is laid down: शृतं क्षीरम्, शृतं हविः, and the root may be causative or not.'),
    ),
    '6.1.28': (
        _c('पीनं मुखम् (pīnaṃ mukham) — a full face',
           {'root': 'pyāy', 'before': 'niṣṭhā'},
           note='प्यायः पी — पीनं मुखम्, पीनौ बाहू, पीनमुरः.'),
    ),
    '6.1.29': (
        _c('आपिप्ये (āpipye) — पी before the perfect and the intensive',
           {'root': 'pyāy', 'before': 'liṭ'},
           note='लिड्यङोश्च — the same substitute before लिट् and यङ्, and विभाषेति निवृत्तम्: the option of the rule before has lapsed, so here it is fixed. आपिप्ये, आपिप्याते,'),
    ),
    '6.1.30': (
        _c('शुशाव (śuśāva) — beside शिश्वाय',
           {'root': 'śvi', 'before': 'liṭ'},
           note='विभाषा श्वेः — शुशाव, शिश्वाय; शुशुवतुः, शिश्वियतुः; शोशूयते, शेश्वीयते.'),
    ),
    '6.1.31': (
        _c('शुशावयिषति (śuśāvayiṣati) — the causative desiderative',
           {'root': 'śvi', 'before': 'ṇau-saṃ-caṅoḥ'},
           note='णौ च संश्चङोः — before णि with सन् or चङ् after it, the same choice: शुशावयिषति, शिश्वाययिषति; अशूशवत्, अशिश्वयत्.'),
    ),
    '6.1.32': (
        _c('जुहावयिषति (juhāvayiṣati) — no choice about it',
           {'root': 'hve', 'before': 'ṇau-saṃ-caṅoḥ'},
           note='ह्वः संप्रसारणम् — जुहावयिषति, अजूहवत्, and this one is NOT a choice.'),
    ),
    '6.1.33': (
        _c('जुहाव (juhāva) — vocalised before the doubling happens',
           {'root': 'hve'},
           note='अभ्यस्तस्य च — and the genitive does not agree with ह्वः. अभ्यस्तस्य यो ह्वयतिः। कश्चाभ्यस्तस्य ह्वयतिः? कारणम् — the ह्वयति that BRINGS ABOUT an अभ्यस्त, not one that'),
    ),
    '6.1.34': (
        _c('हुवे (huve) — the Vedic form, beside ह्वयामि',
           {'root': 'hve', 'chandasi': True},
           note='बहुलं छन्दसि — in the Vedic corpus the same root vocalises variously: इन्द्राग्नी हुवे, देवीं सरस्वतीं हुवे, but also ह्वयामि विश्वान् देवान्.'),
    ),
    '6.1.35': (
        _c('चिक्युः (cikyuḥ) — की in the Veda, with no यङ् in sight',
           {'root': 'cāy', 'chandasi': True},
           note='चायः की — the substitute of 6.1.21 again, now in the छन्दस् and without the यङ् that rule required: न्यन्यं चिक्युर्न नि चिक्युरन्यम्, forms in the उस् of लिट्. And'),
    ),
    '6.1.36': (
        _c('तित्याज (tityāja) — the copy vocalised, laid down whole',
           {'root': 'tyaj', 'chandasi': True},
           note='अपस्पृधेथामानृचुरानृहुश्चिच्युषेतित्याजश्राताः श्रितमाशीराशीर्ताः — nine forms laid down whole, each with its irregularity named.'),
    ),
    '6.1.37': (
        _c('विद्धः (viddhaḥ) — one vocalisation and never a second',
           {'root': 'vyadh', 'before': 'kit', 'already': True},
           note='न संप्रसारणे संप्रसारणम् — where one semivowel has been vocalised, the one before it is not. व्यध् has both व् and य्, and only the य् goes.'),
    ),
    '6.1.38': (
        _c('ऊयतुः (ūyatuḥ) — the य् of वय् left alone',
           {'root': 'vayi', 'before': 'liṭ'},
           note='लिटि व्यो यः — of the substitute वय्, the य् does not vocalise in the perfect: उवाय, ऊयतुः, ऊयुः. The व् does, by 6.1.16, and that is what makes ऊयतुः.'),
    ),
    '6.1.39': (
        _c('ऊवतुः (ūvatuḥ) — व् for that य्, as a choice',
           {'root': 'vayi', 'before': 'kit-liṭ'},
           note='वश्चास्यान्यतरस्यां किति — and the substitute is a CONSONANT, the only such row in the section: व् may stand for the य् of वय् before a कित् perfect ending. ऊवतुः, ऊवुः'),
    ),
    '6.1.40': (
        _c('ववौ (vavau) — वेञ् unvocalised in the perfect',
           {'root': 'veñ', 'before': 'liṭ'},
           note='वेञः — in the perfect वेञ् does not vocalise, and neither does its copy: ववौ, ववतुः, ववुः.'),
    ),
    '6.1.41': (
        _c('प्रवाय (pravāya) — वेञ् keeping its semivowel before ल्यप्',
           {'root': 'veñ', 'before': 'lyap'},
           note='ल्यपि च — and before ल्यप् too: प्रवाय, उपवाय. पृथग्योगकरणमुत्तरार्थम् — the rule is split off from 6.1.40 so that only ल्यप्, and not लिट्, carries into the three that'),
    ),
    '6.1.42': (
        _c('प्रज्याय (prajyāya) — ज्या keeping its य्',
           {'root': 'jyā', 'before': 'lyap'},
           note="ज्यश्च — प्रज्याय, उपज्याय. ज्या is one of 6.1.16's nine and ल्यप् is कित् by 1.1.5's reading of it, so the vocalisation would otherwise hold"),
    ),
    '6.1.43': (
        _c('प्रव्याय (pravyāya) — व्ये keeping its य्',
           {'root': 'vyeñ', 'before': 'lyap'},
           note='व्यश्च — प्रव्याय, उपव्याय, and again योगविभाग उत्तरार्थः: the rule is kept separate so that व्येञ् alone carries into 6.1.44'),
    ),
    '6.1.44': (
        _c('परिवीय यूपम् (parivīya yūpam) — beside परिव्याय',
           {'root': 'vyeñ', 'before': 'lyap', 'pre': 'pari'},
           note='विभाषा परेः — after परि the refusal is a choice, so the vocalisation comes back in one of the two forms: परिवीय यूपम्, परिव्याय. The last rule the heading reaches.'),
    ),
    '6.1.45': (
        _c('ग्लाता (glātā) — ग्लै with आ for its ऐ',
           {'root': 'glai', 'final': 'ai'},
           note='आदेच उपदेशेऽशिति — a root whose final in the धातुपाठ is an एच् has आ put in its place, and धातोः carries down from 6.1.8. ग्लाता, ग्लातुम्, ग्लातव्यम्; निशाता, निशातुम्,'),
    ),
    '6.1.46': (
        _c('संविव्याय (saṃvivyāya) — व्ये keeping its ए in the perfect',
           {'root': 'vyeñ', 'before': 'liṭ'},
           note='न व्यो लिटि — व्येञ् keeps its diphthong in the perfect: संविव्याय, संविव्ययिथ.'),
    ),
    '6.1.47': (
        _c('विस्फारः (visphāraḥ) — आ where guṇa would have given ओ',
           {'root': 'sphur', 'before': 'ghañ'},
           note='स्फुरतिस्फुलत्योर्घञि — before घञ् these two give आ where guṇa would have given ओ: विस्फारः, विस्फालः, not विस्फोरः and विस्फोलः. And 8.3.76 makes the स् optionally ष्'),
    ),
    '6.1.48': (
        _c('अध्यापयति (adhyāpayati) — इ made आ before the causative',
           {'root': 'iṅ', 'before': 'ṇi'},
           note='क्रीङ्जीनां णौ — three roots before णि: क्रापयति, अध्यापयति, जापयति.'),
    ),
    '6.1.49': (
        _c('अन्नं साधयति (annaṃ sādhayati) — food got ready',
           {'root': 'sidh', 'before': 'ṇi', 'result': 'apāralaukika'},
           note='सिध्यतेरपारलौकिके — before णि, and only where what is brought about is NOT for the next world: अन्नं साधयति, ग्रामं साधयति.'),
    ),
    '6.1.50': (
        _c('प्रमाय (pramāya) — मी made आ before ल्यप्',
           {'root': 'mī', 'before': 'lyap'},
           note='मीनातिमिनोतिदीङां ल्यपि च — before ल्यप्, and by the च before whatever else the आकार section reaches: प्रमाता, प्रमातव्यम्, प्रमातुम्, प्रमाय; निमाता, निमाय; उपदाता,'),
    ),
    '6.1.51': (
        _c('विलाता (vilātā) — beside विलेता',
           {'root': 'lī', 'before': 'lyap'},
           note='विभाषा लीयतेः — विलाता, विलातुम्, विलातव्यम्, विलाय beside विलेता, विलेतुम्, विलेतव्यम्, विलीय. Both लीङ् of the दिवादि and ली of the क्र्यादि are meant.'),
    ),
    '6.1.52': (
        _c('चित्तं चखाद (cittaṃ cakhāda) — a Vedic form beside चिखेद',
           {'root': 'khid', 'chandasi': True},
           note='खिदेश्छन्दसि — in the Vedic corpus the option reaches खिद् as well: चित्तं चखाद beside चित्तं चिखेद. Outside it there is no choice and no substitution'),
    ),
    '6.1.53': (
        _c('अपगारम् (apagāram) — with a weapon raised over and over',
           {'root': 'gur', 'before': 'ṇamul', 'pre': 'apa'},
           note="अपगुरो णमुलि — after अप and before णमुल्: अपगारमपगारम् beside अपगोरमपगोरम्. The णमुल् is 3.4.22's, given for repeated action, and the word is doubled with it. 3.4.53"),
    ),
    '6.1.54': (
        _c('चापयति (cāpayati) — beside चाययति',
           {'root': 'ci', 'before': 'ṇi'},
           note='चिस्फुरोर्णौ — before णि, optionally: चापयति, चाययति; स्फारयति, स्फोरयति. स्फुर् is here for the second time in the section — 6.1.47 took it before घञ् and made it'),
    ),
    '6.1.55': (
        _c('प्रवापयति (pravāpayati) — the wind makes the cows conceive',
           {'root': 'vī', 'before': 'ṇi', 'result': 'prajana'},
           note='प्रजने वीयतेः — before णि, in the sense of conceiving: पुरोवातो गाः प्रवापयति beside प्रवाययति, which the vṛtti glosses गर्भं ग्राहयति. And it says what the sense-word'),
    ),
    '6.1.56': (
        _c('मुण्डो भापयते (muṇḍo bhāpayate) — the shaven man frightens him',
           {'root': 'bhī', 'before': 'ṇi', 'result': 'hetubhaya'},
           note='बिभेतेर्हेतुभये — before णि, where the fear comes STRAIGHT from the causative agent: मुण्डो भापयते, जटिलो भापयते beside भीषयते.'),
    ),
    '6.1.57': (
        _c('मुण्डो विस्मापयते (muṇḍo vismāpayate) — a man who astonishes',
           {'root': 'smi', 'before': 'ṇi', 'result': 'hetubhaya'},
           note='नित्यं स्मयतेः — the same condition as the rule before, the same affix, the same sense — and no choice: मुण्डो विस्मापयते, जटिलो विस्मापयते.'),
    ),
    '6.1.58': (
        _c('स्रष्टा (sraṣṭā) — अम् put in, and no guṇa',
           {'stem': 'sṛj', 'before': 'jhal-akit'},
           note='सृजिदृशोर्झल्यमकिति — before an affix beginning with a झल् and not marked क्, these two take the augment अम्: स्रष्टा, स्रष्टुम्, स्रष्टव्यम्; द्रष्टा, द्रष्टुम्,'),
    ),
    '6.1.59': (
        _c('त्रप्ता (traptā) — the same augment, as a choice',
           {'before': 'jhal-akit', 'upadha': 'ṛ', 'accent': 'anudātta'},
           note='अनुदात्तस्य च ऋदुपधस्यान्यतरस्याम् — the same augment, optionally, for a root the धातुपाठ marked अनुदात्त with ऋ for its penult: त्रप्ता, तर्पिता, तर्प्ता; द्रप्ता,'),
    ),
    '6.1.60': (
        _c('शीर्ष्णा (śīrṣṇā) — a Vedic word, not a substitute',
           {'stem': 'śiras', 'chandasi': True},
           note='शीर्षंश्छन्दसि — in the Vedic corpus शीर्षन् is laid down as a word of its own, meaning what शिरस् means: शीर्ष्णा हि तत्र सोमं क्रीतं हरन्ति; यत्ते शीर्ष्णो दौर्भाग्यम्.'),
    ),
    '6.1.61': (
        _c('शीर्षण्यः स्वरः (śīrṣaṇyaḥ svaraḥ) — a tone made in the head',
           {'stem': 'śiras', 'before': 'ya-taddhita'},
           note="ये च तद्धिते — before a taddhita affix beginning with य्, शिरस् is replaced by शीर्षन्: शीर्षण्यः स्वरः, with 4.3.55's यत् and 6.4.168's प्रकृतिभाव keeping the अन्"),
    ),
    '6.1.62': (
        _c('हास्तिशीर्षिः (hāstiśīrṣiḥ) — the शीर्ष without its न्',
           {'stem': 'śiras', 'before': 'ac-taddhita'},
           note='अचि शीर्षः — before a taddhita beginning with a vowel the substitute is शीर्ष, without the न्: हास्तिशीर्षिः, स्थौलशीर्षम्.'),
    ),
    '6.1.63': (
        _c('पदा (padā) — पाद in the weak cases',
           {'stem': 'pāda', 'before': 'śas-prabhṛti'},
           note='पद्दन्नोमास्हृन्निश्असन्यूषन्दोषन्यकञ्शकन्नुदन्नासञ् छस्प्रभृतिषु — thirteen stems and thirteen substitutes, paired off यथासंख्यम् before शस् and the endings after it.'),
    ),
    '6.1.66': (
        _c('ऊतम् (ūtam) — the य् gone before a consonant',
           {'before': 'val'},
           note='लोपो व्योर्वलि — a व् or य् is dropped before a consonant other than य्, and धातोः has lapsed: धातोरिति प्रकृतं यत् तद् धात्वादेरिति पुनर्धातुग्रहणाद् निवृत्तम्। तेन'),
    ),
    '6.1.67': (
        _c('ब्रह्महा (brahmahā) — the whole affix gone',
           {'before': 'apṛkta'},
           note='वेरपृक्तस्य — the affix वि, reduced to a single sound, is dropped. वेरिति क्विबादयो विशेषाननुबन्धानुत्सृज्य सामान्येन गृह्यन्ते — क्विप्, क्विन् and ण्वि are all meant,'),
    ),
    '6.1.68': (
        _c('राजा (rājā) — the nominative स् gone after a consonant',
           {'before': 'su-ti-si', 'after': 'hal'},
           note='हल्ङ्याब्भ्यो दीर्घात् सुतिस्यपृक्तं हल् — after a consonant, or a long ङी or आप्, the single consonant left of सु, ति or सि is dropped: राजा, तक्षा; कुमारी, गौरी;'),
    ),
    '6.1.69': (
        _c('हे अग्ने (he agne) — the vocative with nothing after it',
           {'before': 'sambuddhi', 'after': 'eṅ'},
           note='एङ् ह्रस्वात् सम्बुद्धेः — in the vocative singular the consonant of the ending is dropped after ए or ओ and after a short vowel: हे अग्ने, हे वायो; हे देवदत्त, हे नदि,'),
    ),
    '6.1.70': (
        _c('या क्षेत्रा (yā kṣetrā) — beside यानि क्षेत्राणि',
           {'before': 'śi', 'chandasi': True},
           note='शेश्छन्दसि बहुलम् — in the Vedic corpus the शि of the neuter plural is dropped variously: या क्षेत्रा, या वना beside यानि क्षेत्राणि, यानि वनानि. Both shapes are found'),
    ),
    '6.1.71': (
        _c('अग्निचित् (agnicit) — a त् added after a short vowel',
           {'before': 'pit-kṛt', 'after': 'hrasva'},
           note='ह्रस्वस्य पिति कृति तुक् — a root ending in a short vowel takes the augment तुक् before a कृत् affix marked प्: अग्निचित्, सोमसुत्; प्रकृत्य, प्रहृत्य, उपस्तुत्य.'),
    ),
    '6.1.72': (
        _c('दध्यत्र (dadhyatra) — spoken in one breath, and the vowels join',
           {},
           note='संहितायाम् — अधिकारोऽयम् अनुदात्तं पदमेकवर्जम् इति यावत्। प्रागेतस्मात् सूत्रादित उत्तरं यद् वक्ष्यामः संहितायामित्येवं तद् वेदितव्यम् — everything from here to 6.1.157'),
    ),
    '6.1.73': (
        _c('इच्छति (icchati) — a त् put in before छ',
           {'before': 'cha', 'after': 'hrasva'},
           note='छे च — a short vowel takes the augment तुक् before छ, and ह्रस्वस्य तुक् carries down from 6.1.71: इच्छति, यच्छति. 8.4.40 then makes the त् a च्.'),
    ),
    '6.1.74': (
        _c('आच्छादयति (ācchādayati) — and here the त् is not a choice',
           {'stem': 'āṅ', 'before': 'cha'},
           note='आङ्माङोश्च — for आङ् in its four senses and for the prohibitive माङ्, the augment before छ: ईषच्छाया, आच्छादयति, आच्छायम्; माच् छैत्सीत्, माच् छिदत्.'),
    ),
    '6.1.75': (
        _c('म्लेच्छति (mlecchati) — the same त् after a long vowel',
           {'before': 'cha', 'after': 'dīrgha'},
           note='दीर्घात् — a long vowel too: ह्रीच्छति, म्लेच्छति, अपचाच्छायते, विचाच्छायते. And the augment belongs to the long vowel itself, on the same reading 6.1.73 was given —'),
    ),
    '6.1.76': (
        _c('कुटीच्छाया (kuṭīcchāyā) — beside कुटीछाया',
           {'before': 'cha', 'after': 'padānta-dīrgha'},
           note='पदान्ताद् वा — where the long vowel ends a पद the augment is a choice: कुटीच्छाया, कुटीछाया; कुवलीच्छाया, कुवलीछाया.'),
    ),
    '6.1.77': (
        _c('दध्यत्र (dadhyatra) — इ turned into य् before a vowel',
           {'before': 'ac'},
           note='इको यणचि — an इक् becomes the matching semivowel before a vowel: दध्यत्र, मध्वत्र, कर्त्रर्थम्, हर्त्रर्थम्, लाकृतिः.'),
    ),
    '6.1.79': (
        _c('बाभ्रव्यः (bābhravyaḥ) — ओ turned into अव् before a य-affix',
           {'before': 'ya-pratyaya'},
           note='वान्तो यि प्रत्यये — of the four substitutes 6.1.78 gives for an एच्, the two that END in व् — अव् and आव् — come also before an affix beginning with य्: बाभ्रव्यः,'),
    ),
    '6.1.80': (
        _c('लव्यम् (lavyam) — where the affix itself made the ओ',
           {'before': 'ya-pratyaya'},
           note='धातोस्तन्निमित्तस्यैव — and the rule supplies nothing. It NARROWS 6.1.79: for a ROOT, the substitution holds only where the diphthong was itself brought about by that'),
    ),
    '6.1.81': (
        _c('क्षय्यः (kṣayyaḥ) — what CAN be destroyed',
           {'stem': 'kṣi', 'before': 'yat', 'result': 'śakya'},
           note='क्षय्यजय्यौ शक्यार्थे — two forms laid down whole, with अय् for the ए before यत्, and only where the sense is *able to be*: शक्यः क्षेतुं क्षय्यः, शक्यो जेतुं जय्यः.'),
    ),
    '6.1.82': (
        _c('क्रय्यो गौः (krayyo gauḥ) — an ox put out for sale',
           {'stem': 'krī', 'before': 'yat', 'result': 'tadartha'},
           note='क्रय्यस्तदर्थे — the same substitution for क्री, and only in the sense of being put out FOR that, for buying: क्रय्यो गौः, क्रय्यः कम्बलः, and the vṛtti glosses it'),
    ),
    '6.1.83': (
        _c('भय्यम् (bhayyam) — that from which one fears',
           {'stem': 'bhī', 'before': 'yat', 'chandasi': True},
           note='भय्यप्रवय्ये च छन्दसि — two more laid down, for the corpus: भय्यं किलासीत्; वत्सतरी प्रवय्या.'),
    ),
    '6.1.84': (
        _c('खट्वेन्द्रः (khaṭvendraḥ) — one ए for the आ and the इ at once',
           {},
           note='एकः पूर्वपरयोः — अधिकारोऽयम्। ख्यत्यात् परस्य इति प्रागेतस्मात् सूत्रादित उत्तरं यद् वक्ष्यामस्तत्र पूर्वस्य परस्य द्वयोरपि स्थान एकादेशो भवति — from here to 6.1.111,'),
    ),
    '6.1.87': (
        _c('तवेदम् (tavedam) — अ and इ giving one ए',
           {'after': 'a-ā', 'before': 'ac'},
           note='आद् गुणः — where अ or आ stands before a vowel, one guṇa replaces both: तवेदम्, खट्वेन्द्रः, मालेन्द्रः; तवोदकम्, खट्वोदकम्; तवर्श्यः, खट्वर्श्यः; तवल्कारः, खट्वल्कारः.'),
    ),
    '6.1.88': (
        _c('ब्रह्मौदनः (brahmaudanaḥ) — vṛddhi where a diphthong follows',
           {'after': 'a-ā', 'before': 'ec'},
           note='वृद्धिरेचि — where the later sound is an एच्, vṛddhi instead of guṇa: ब्रह्मैडका, खट्वैडका; ब्रह्मौदनः, खट्वौदनः; ब्रह्मौपगवः, खट्वौपगवः. The vṛtti names the relation'),
    ),
    '6.1.89': (
        _c('उपैति (upaiti) — vṛddhi before three named things',
           {'after': 'a-ā', 'before': 'eti-edhati-ūṭh'},
           note='एत्येधत्यूठ्सु — vṛddhi before the ए of एति, the एध् of एधति, and the ऊठ्: उपैति, उपैषि, उपैमि; उपैधते, प्रैधते; प्रष्ठौहः, प्रष्ठौहा.'),
    ),
    '6.1.90': (
        _c('ऐक्षिष्ट (aikṣiṣṭa) — vṛddhi after the augment आट्',
           {'after': 'āṭ', 'before': 'ac'},
           note='आटश्च — after the augment आट्, vṛddhi before any vowel: ऐक्षिष्ट, ऐक्षत, ऐक्षिष्यत; औभीत्, औब्जीत्. एचीति निवृत्तम् — the एच् of 6.1.88 has lapsed.'),
    ),
    '6.1.91': (
        _c('उपार्च्छति (upārcchati) — a preverb before an ऋ-initial root',
           {'after': 'upasarga-a', 'before': 'ṛ-dhātu'},
           note='उपसर्गादृति धातौ — after a preverb ending in अ or आ and before a root beginning with ऋ, vṛddhi: उपार्च्छति, प्रार्च्छति, उपार्ध्नोति. आद्गुणापवादः.'),
    ),
    '6.1.92': (
        _c('उपार्षभीयति (upārṣabhīyati) — beside उपर्षभीयति',
           {'after': 'upasarga-a', 'before': 'ṛ-sup-dhātu', 'teacher': 'Āpiśali'},
           note='वा सुप्यापिशलेः — where the ऋ-initial root is a denominative made from a सुबन्त, the vṛddhi is a choice, आपिशलेराचार्यस्य मतेन: उपार्षभीयति, उपर्षभीयति; उपाल्कारीयति,'),
    ),
    '6.1.93': (
        _c('गां पश्य (gāṃ paśya) — आ for ओ and the accusative',
           {'after': 'o', 'before': 'am-śas'},
           note='ओतोऽम्शसोः — where a stem ending in ओ meets the accusative अम् or शस्, आ stands for both: गां पश्य, गाः पश्य; द्यां पश्य, द्याः पश्य.'),
    ),
    '6.1.94': (
        _c('उपेलयति (upelayati) — the LATER form stands for both',
           {'after': 'upasarga-a', 'before': 'eṅ-dhātu'},
           note='एङि पररूपम् — after a preverb in अ or आ and before a root beginning with ए or ओ, the LATER form stands for both: उपेलयति, प्रेलयति; उपोषति, प्रोषति. वृद्धिरेचि'),
    ),
    '6.1.95': (
        _c('अद्योढा (adyoḍhā) — the later form before ओम् and आङ्',
           {'after': 'a-ā', 'before': 'om-āṅ'},
           note='ओमाङोश्च — before ओम् and before the preverb आङ्, the later form again: कोमित्यवोचत्, योमित्यवोचत्; अद्योढा, कदोढा, तदोढा.'),
    ),
    '6.1.96': (
        _c('भिन्द्युः (bhindyuḥ) — the later form before the ending उस्',
           {'after': 'a-apadānta', 'before': 'us'},
           note='उस्यपदान्तात् — before the ending उस्, where the अ does not end a पद, the later form: भिन्द्युः, छिन्द्युः; अदुः, अयुः. आद्गुणापवादः.'),
    ),
    '6.1.98': (
        _c('पटिति (paṭiti) — a word imitating a sound, before इति',
           {'after': 'avyakta-at', 'before': 'iti'},
           note='अव्यक्तानुकरणस्यात इतौ — where a word imitating an inarticulate sound ends in अत् and इति follows, the later form stands: पटिति, घटिति, झटिति, छमिति.'),
    ),
    '6.1.99': (
        _c('पटत्पटदिति (paṭatpaṭaditi) — beside पटत्पटेति',
           {'after': 'āmreḍita-at', 'before': 'iti'},
           note='नाम्रेडितस्यान्त्यस्य तु वा — where the imitation has been doubled by 8.1.4, the later form does NOT stand for its अत् — and for the final त् alone it stands optionally:'),
    ),
    '6.1.100': (
        _c('पटपटा करोति (paṭapaṭā karoti) — and now with no choice',
           {'after': 'āmreḍita', 'before': 'ḍāc'},
           note='नित्यमाम्रेडिते डाचि — with the affix डाच् after the doubled imitation, the later form is FIXED, and now for the final त् and the following consonant: पटपटा करोति, दमदमा'),
    ),
    '6.1.102': (
        _c('अग्नी (agnī) — the long vowel matching the EARLIER sound',
           {'after': 'ak', 'before': 'prathamā-dvitīyā'},
           note='प्रथमयोः पूर्वसवर्णः — before the endings of the first and second cases, the long vowel HOMOGENEOUS WITH THE EARLIER sound stands for both: अग्नी, वायू; वृक्षाः,'),
    ),
    '6.1.103': (
        _c('वृक्षान् (vṛkṣān) — the स् of शस् turned into न्',
           {'after': 'pūrvasavarṇa-dīrgha', 'before': 'śas', 'result': 'puṃs'},
           note='तस्माच्छसो नः पुंसि — after the long vowel THAT rule gave, the स् of शस् becomes न् in the masculine: वृक्षान्, अग्नीन्, वायून्, कर्तॄन्.'),
    ),
    '6.1.104': (
        _c('वृक्षौ (vṛkṣau) — no lengthening after अ',
           {'after': 'a-ā', 'before': 'ic'},
           note='नादिचि — after अ or आ, and before a first- or second-case ending beginning with a vowel other than अ, the homogeneous long vowel does NOT stand: वृक्षौ, प्लक्षौ; खट्वे,'),
    ),
    '6.1.105': (
        _c('कुमार्यौ (kumāryau) — no lengthening after a long vowel',
           {'after': 'dīrgha', 'before': 'jas-ic'},
           note='दीर्घाज्जसि च — and after a long vowel the same refusal, before जस् as well as before an इच्: कुमार्यौ, कुमार्यः; ब्रह्मबन्ध्वौ, ब्रह्मबन्ध्वः. What stands instead is'),
    ),
    '6.1.106': (
        _c('मारुतीः (marutīḥ) — beside मारुत्यः, in the Veda',
           {'after': 'dīrgha', 'before': 'jas-ic', 'chandasi': True},
           note='वा छन्दसि — in the Vedic corpus the refusal of the rule before is itself a choice, so the long vowel comes back: मारुतीश्चतस्रः पिण्डीः beside मारुत्यश्चतस्रः पिण्ड्यः;'),
    ),
    '6.1.107': (
        _c('वृक्षम् (vṛkṣam) — the EARLIER form standing for both',
           {'after': 'ak', 'before': 'am'},
           note='अमि पूर्वः — before the ending अम्, the EARLIER form stands for both: वृक्षम्, प्लक्षम्; अग्निम्, वायुम्.'),
    ),
    '6.1.108': (
        _c('इष्टम् (iṣṭam) — the vocalised vowel swallowing what follows',
           {'after': 'samprasāraṇa', 'before': 'ac'},
           note='संप्रसारणाच्च — after a vocalised semivowel the earlier form again: इष्टम्, उप्तम्, गृहीतम्. And this is the rule whose words bound the अचि heading opened at 6.1.77.'),
    ),
    '6.1.109': (
        _c("अग्नेऽत्र (agne'tra) — ए keeping its place before a short अ",
           {'after': 'eṅ-padānta', 'before': 'at'},
           note="एङः पदान्तादति — where ए or ओ ends a पद and a short अ follows, the earlier form stands: अग्नेऽत्र, वायोऽत्र. अयवादेशयोरयमपवादः — an exception to 6.1.78's अय् and अव्."),
    ),
    '6.1.110': (
        _c('अग्नेः (agneḥ) — the earlier form, now inside the word',
           {'after': 'eṅ', 'before': 'ṅasi-ṅas'},
           note='ङसिङसोश्च — and before the ablative and genitive singular, whether or not the ए or ओ ends a पद: अग्नेरागच्छति, वायोरागच्छति; अग्नेः स्वम्, वायोः स्वम्. अपदान्तार्थ'),
    ),
    '6.1.111': (
        _c('होतुः (hotuḥ) — उ standing for ऋ and अ together',
           {'after': 'ṛ', 'before': 'ṅasi-ṅas'},
           note='ऋत उत् — after a ऋ-final stem and before the same two endings, उ stands for both: होतुरागच्छति, होतुः स्वम्. The last rule the एकादेश heading reaches.'),
    ),
    '6.1.112': (
        _c('सख्युः (sakhyuḥ) — the same उ after सखि and पति',
           {'stem': 'sakhi', 'after': 'khy-ty', 'before': 'ṅasi-ṅas'},
           note='ख्यत्यात् परस्य — after सखि and पति with their इ already turned into य्, the same उ for the अ of the ending: सख्युरागच्छति, सख्युः स्वम्; पत्युरागच्छति, पत्युः स्वम्.'),
    ),
    '6.1.113': (
        _c("वृक्षोऽत्र (vṛkṣo'tra) — रु turned into उ between two अ",
           {'stem': 'ru', 'after': 'a-apluta', 'before': 'at-apluta'},
           note='अतो रोरप्लुतादप्लुते — where रु stands between a short अ and a short अ, उ replaces it: वृक्षोऽत्र, प्लक्षोऽत्र.'),
    ),
    '6.1.114': (
        _c('पुरुषो याति (puruṣo yāti) — रु before a soft consonant',
           {'stem': 'ru', 'after': 'a', 'before': 'haś'},
           note='हशि च — and before a soft consonant the same उ for रु: पुरुषो याति, पुरुषो हसति, पुरुषो ददाति. The one rule of the pāda that acts before a consonant rather than a vowel'),
    ),
    '6.1.115': (
        _c('ते अग्ने (te agne) — the vowels standing apart, in a Vedic foot',
           {'after': 'eṅ', 'before': 'at', 'result': 'antaḥpāda', 'chandasi': True},
           note='प्रकृत्यान्तःपादमव्यपरे — where ए or ओ meets a short अ inside a Vedic पाद, and no व् or य् follows that अ, both stand as they are: ते अग्ने अश्वमायुञ्जन्; उपप्रयन्तो'),
    ),
    '6.1.116': (
        _c('नो अव्यात् (no avyāt) — seven words that keep the gap open',
           {'after': 'eṅ', 'before': 'avyādi', 'result': 'antaḥpāda', 'chandasi': True},
           note='अव्यादवद्यादवक्रमुरव्रतायमवन्त्ववस्युषु च — seven words that hold the junction open THOUGH a व् or य् follows their अ, which is the one thing 6.1.115 refuses on: नो'),
    ),
    '6.1.117': (
        _c('उरो अन्तरिक्षम् (uro antarikṣam) — in prose, where there is no foot',
           {'stem': 'uras', 'before': 'at', 'yajusi': True},
           note='यजुष्युरः — in the Yajurveda the word उरस् keeps its ओ and the अ after it: उरो अन्तरिक्षम्.'),
    ),
    '6.1.118': (
        _c('आपो अस्मान् (āpo asmān) — six more, for that corpus alone',
           {'stem': 'āpo', 'before': 'at', 'yajusi': True},
           note='आपोजुषाणोवृष्णोवर्षिष्ठेऽम्बेऽम्बालेऽम्बिकेपूर्वे — six more for the Yajurveda: आपो अस्मान् मातरः शुन्धयन्तु; जुषाणो अप्तुराज्यस्य; वृष्णो अंशुभ्यां गभस्तिपूतः;'),
    ),
    '6.1.119': (
        _c('अङ्गेअङ्गे अदीध्यत् (aṅge aṅge adīdhyat) — held open twice over',
           {'stem': 'aṅga', 'before': 'at', 'yajusi': True},
           note='अङ्ग इत्यादौ च — and where अङ्गे is followed by अङ्गे, both the ए and the अ stand: ऐन्द्रः प्राणो अङ्गेअङ्गे अदीध्यत्; ऐन्द्रः प्राणो अङ्गेअङ्गे निदीध्यत्. The rule'),
    ),
    '6.1.120': (
        _c('अयं नो अग्निः (ayaṃ no agniḥ) — the accent deciding it',
           {'after': 'eṅ', 'before': 'at-anudātta-ku-dha', 'yajusi': True},
           note='अनुदात्ते च कुधपरे — in the Yajurveda, where the short अ is अनुदात्त and a guttural or a ध follows it, the junction stands open: अयं नो अग्निः; अयं सो अध्वरः. Two'),
    ),
    '6.1.121': (
        _c("रुद्रेभ्यो अवपथाः (rudrebhyo avapathāḥ) — one word's own accent",
           {'stem': 'avapathās', 'before': 'at-anudātta', 'yajusi': True},
           note='अवपथासि च — and before the word अवपथाः with its अ अनुदात्त: त्री रुद्रेभ्यो अवपथाः.'),
    ),
    '6.1.122': (
        _c('गो अग्रम् (go agram) — beside गोऽग्रम्, everywhere',
           {'stem': 'go', 'before': 'at'},
           note='सर्वत्र विभाषा गोः — after गो the short अ may stand open, and सर्वत्र means in ordinary speech as well as in the corpus: गोऽग्रम्, गो अग्रम्; and in the corpus अपशवो वा'),
    ),
    '6.1.123': (
        _c('गवाग्रम् (gavāgram) — स्फोटायन putting अवङ् in instead',
           {'stem': 'go', 'before': 'ac', 'teacher': 'Sphoṭāyana'},
           note='अवङ् स्फोटायनस्य — and instead of holding the junction open, स्फोटायन puts अवङ् in for the ओ of गो before any vowel: गवाग्रम्, गवाजिनम्, गवौदनम् beside गोऽग्रम्,'),
    ),
    '6.1.124': (
        _c('गवेन्द्रः (gavendraḥ) — and before that one word, no choice',
           {'stem': 'go', 'before': 'indra'},
           note='इन्द्रे च नित्यम् — before a vowel of the word इन्द्र the substitute is FIXED: गवेन्द्रः, गवेन्द्रयज्ञस्वरः. The word नित्यम् is what takes the option away, as नित्यम्'),
    ),
    '6.1.125': (
        _c('अग्नी इति (agnī iti) — a प्रगृह्य vowel touched by nothing',
           {'after': 'pluta-pragṛhya', 'before': 'ac'},
           note='प्लुतप्रगृह्या अचि — a प्लुत vowel and a प्रगृह्य one stand open before any vowel: देवदत्त३ अत्र न्वसि; अग्नी इति, वायू इति, खट्वे इति, माले इति.'),
    ),
    '6.1.126': (
        _c('अभ्र आँ अपः (abhra āṃ apaḥ) — the preverb nasalised',
           {'stem': 'āṅ', 'before': 'ac', 'chandasi': True},
           note='आङोऽनुनासिकश्छन्दसि — in the corpus the preverb आ becomes nasalised before a vowel, and stands open: अभ्र आँ अपः; गभीर आँ उग्रपुत्रे जिघांसतः. And केचिद्'),
    ),
    '6.1.127': (
        _c('दधि अत्र (dadhi atra) — शाकल्य leaving the vowels apart',
           {'after': 'ik', 'before': 'asavarṇa-ac', 'teacher': 'Śākalya'},
           note='इकोऽसवर्णे शाकल्यस्य ह्रस्वश्च — शाकल्य holds that an इक् before an unlike vowel stands open, AND is shortened if it was long: दधि अत्र, मधु अत्र, कुमारि अत्र, किशोरि'),
    ),
    '6.1.128': (
        _c('खट्व ऋश्यः (khaṭva ṛśyaḥ) — the same, now before ऋ',
           {'after': 'ak', 'before': 'ṛ', 'teacher': 'Śākalya'},
           note='ऋत्यकः — and before ऋ the same, now for an अक् and not only an इक्: खट्व ऋश्यः, माल ऋश्यः, कुमारि ऋश्यः, होतृ ऋश्यः.'),
    ),
    '6.1.129': (
        _c('सुश्लोकेति (suśloketi) — before the इति of a पदपाठ',
           {'after': 'pluta', 'before': 'upasthita'},
           note="अप्लुतवदुपस्थिते — before the इति of a पदपाठ, a प्लुत vowel is treated LIKE a non-प्लुत one, so 6.1.125's प्रकृतिभाव does not hold and the junction closes: सुश्लोक३ इति"),
    ),
    '6.1.130': (
        _c('अस्तु हीति (astu hīti) — and here the name IS the option',
           {'after': 'ī3', 'before': 'ac', 'teacher': 'Cākravarmaṇa'},
           note='ई३ चाक्रवर्मणस्य — चाक्रवर्मण holds that a प्लुत ई३ before a vowel is treated like a non-प्लुत one: अस्तु हीत्यब्रूताम् beside अस्ति ही३ इत्यब्रूताम्; चिनु हीदम् beside'),
    ),
    '6.1.131': (
        _c('द्युभ्याम् (dyubhyām) — दिव् as a पद ending in उ',
           {'stem': 'div', 'result': 'pada'},
           note='दिव उत् — where दिव् is a पद, उ stands for its final: द्युकामः, द्युमान्, विमलद्यु दिनम्, द्युभ्याम्, द्युभिः.'),
    ),
    '6.1.132': (
        _c('एष ददाति (eṣa dadāti) — the nominative स् gone',
           {'stem': 'etad', 'before': 'hal'},
           note='एतत्तदोः सुलोपोऽकोरनञ्समासे हलि — the nominative singular स् of एतद् and तद् is dropped before a consonant: एष ददाति, स ददाति; एष भुङ्क्ते, स भुङ्क्ते.'),
    ),
    '6.1.133': (
        _c('उत स्य वाजी (uta sya vājī) — variously, in the corpus',
           {'stem': 'sya', 'before': 'hal', 'chandasi': True},
           note='स्यश्छन्दसि बहुलम् — in the corpus the nominative singular ending is variously dropped after स्य before a consonant: उत स्य वाजी क्षिपणिं तुरण्यति; एष स्य ते पवत इन्द्र'),
    ),
    '6.1.134': (
        _c('सेदु राजा (sedu rājā) — dropped to fill out the foot',
           {'stem': 'sa', 'before': 'ac', 'result': 'pādapūraṇa', 'chandasi': True},
           note='सोऽचि लोपे चेत् पादपूरणम् — the ending of सस् is dropped before a vowel, IF dropping it fills out the foot: सेदु राजा क्षयति चर्षणीनाम्; सौषधीरनुरुध्यसे. A condition on'),
    ),
    '6.1.135': (
        _c('संस्कर्ता (saṃskartā) — a स् put in that never joins the root',
           {},
           note='सुट् कात् पूर्वः — अधिकारोऽयम्, पारस्करप्रभृतीनि च संज्ञायाम् इति यावत्। इत उत्तरं यद् वक्ष्यामस्तत्र सुडिति कात् पूर्व इति चैतदधिकृतं वेदितव्यम् — every rule to 6.1.157'),
    ),
    '6.1.136': (
        _c('समस्करोत् (samaskarot) — the augment reaching across another',
           {'across': 'aṭ'},
           note='अडभ्यासव्यवायेऽपि — the augment goes in before the क् even where the अट् of the imperfect or the reduplicated syllable stands between: समस्करोत्, समस्कार्षीत्; संचस्कार,'),
    ),
    '6.1.137': (
        _c('संस्कर्ता (saṃskartā) — one who makes a thing fine',
           {'stem': 'kṛ', 'pre': 'sam', 'result': 'bhūṣaṇa'},
           note='संपर्युपेभ्यः करोतौ भूषणे — after सम्, परि or उप, before करोति, in the sense of ADORNING: संस्कर्ता, परिष्कर्ता, उपस्कर्ता.'),
    ),
    '6.1.138': (
        _c('तत्र नः संस्कृतम् (tatra naḥ saṃskṛtam) — we gathered there',
           {'stem': 'kṛ', 'pre': 'sam', 'result': 'samavāya'},
           note='समवाये च — and in the sense of coming together: तत्र नः संस्कृतम्; तत्र नः परिष्कृतम्; तत्र न उपस्कृतम्, which the vṛtti glosses समुदितम्. समवायः समुदायः — the word'),
    ),
    '6.1.139': (
        _c('एधोदकस्योपस्कुरुते (edhodakasyopaskurute) — taking pains over it',
           {'stem': 'kṛ', 'pre': 'upa', 'result': 'pratiyatna'},
           note='उपात् प्रतियत्नवैकृतवाक्याध्याहारेषु — after उप alone, in three further senses, and the vṛtti defines each before using it.'),
    ),
    '6.1.140': (
        _c('उपस्कारं लुनन्ति (upaskāraṃ lunanti) — reaping and scattering',
           {'stem': 'kṝ', 'pre': 'upa', 'result': 'lavana'},
           note='किरतौ लवने — before किरति and in the sense of reaping: उपस्कारं मद्रका लुनन्ति; उपस्कारं काश्मीरका लुनन्ति — विक्षिप्य लुनन्ति, they scatter as they cut. And णमुलत्र'),
    ),
    '6.1.141': (
        _c('प्रतिस्कीर्णम् (pratiskīrṇam) — a scattering meant to hurt',
           {'stem': 'kṝ', 'pre': 'prati', 'result': 'hiṃsā'},
           note='हिंसायां प्रतेश्च — and after प्रति as well as उप, where harm is meant: उपस्कीर्णं हन्त ते वृषल भूयात्; प्रतिस्कीर्णं हन्त ते वृषल भूयात् — the vṛtti glossing it तथा ते'),
    ),
    '6.1.142': (
        _c('अपस्किरते वृषभः (apaskirate vṛṣabhaḥ) — a bull scraping the ground',
           {'stem': 'kṝ', 'pre': 'apa', 'result': 'ālekhana', 'agent': 'catuṣpād-śakuni'},
           note='अपाच्चतुष्पाच्छकुनिष्वालेखने — after अप, of a four-footed animal or a bird scratching the ground: अपस्किरते वृषभो हृष्टः; अपस्किरते कुक्कुटो भक्ष्यार्थी; अपस्किरते श्वा'),
    ),
    '6.1.143': (
        _c('कुस्तुम्बुरूणि (kustumburūṇi) — coriander, as a species',
           {'stem': 'kustumburu', 'result': 'jāti'},
           note='कुस्तुम्बुरूणि जातिः — the word is laid down with its सुट्, and only where a SPECIES is meant: कुस्तुम्बुरुर् नाम ओषधिजातिर्धान्यकम्, coriander, and its seeds besides.'),
    ),
    '6.1.144': (
        _c('अपरस्पराः सार्थाः (aparasparāḥ sārthāḥ) — caravans without a break',
           {'stem': 'aparaspara', 'result': 'kriyāsātatya'},
           note='अपरस्पराः क्रियासातत्ये — laid down with its सुट् where an action goes on without a break: अपरस्पराः सार्था गच्छन्ति — सन्ततमविच्छेदेन गच्छन्ति.'),
    ),
    '6.1.145': (
        _c('गोष्पदो देशः (goṣpado deśaḥ) — land that cows go over',
           {'stem': 'goṣpada', 'result': 'sevita'},
           note='गोष्पदं सेवितासेवितप्रमाणेषु — laid down with its सुट् and its ष्, in three senses: land cows go over — गोष्पदो देशः; land they do not — अगोष्पदान्यरण्यानि; and a'),
    ),
    '6.1.146': (
        _c('आस्पदम् (āspadam) — a standing, a place one holds',
           {'stem': 'āspada', 'result': 'pratiṣṭhā'},
           note='आस्पदं प्रतिष्ठायाम् — laid down where a standing or a position is meant: आस्पदमनेन लब्धम्. And the sense is defined before it is used — आत्मयापनाय स्थानं प्रतिष्ठा, the'),
    ),
    '6.1.147': (
        _c('आश्चर्यं यदि स भुञ्जीत (āścaryaṃ yadi sa bhuñjīta)',
           {'stem': 'āścarya', 'result': 'anitya'},
           note='आश्चर्यमनित्ये — laid down where what is wonderful is meant, and the vṛtti derives the sense from the word: अनित्यतया विषयभूतया अद्भुतत्वमिह लक्ष्यते — what astonishes'),
    ),
    '6.1.148': (
        _c('अवस्करः (avaskaraḥ) — what the body throws out',
           {'stem': 'avaskara', 'result': 'varcaska'},
           note="वर्चस्केऽवस्करः — laid down for excrement, and the vṛtti reads the sense-word out: कुत्सितं वर्चो वर्चस्कम् अन्नमलम्. The word is किरति with अव and 3.3.57's अप् in the"),
    ),
    '6.1.149': (
        _c('अपस्करः (apaskaraḥ) — a part of a chariot',
           {'stem': 'apaskara', 'result': 'rathāṅga'},
           note='अपस्करो रथाङ्गम् — laid down for a part of a chariot: अपस्करो रथावयवः. The same root and the same 3.3.57 as the rule before, and only the preverb and the sense differ'),
    ),
    '6.1.150': (
        _c('विष्किरः (viṣkiraḥ) — beside विकिरः, of a bird',
           {'stem': 'viṣkira', 'agent': 'śakuni'},
           note="विष्किरः शकुनिर्विकिरो वा — laid down for a bird, and optionally, विकिर standing beside it: सर्वे शकुनयो भक्ष्या विष्किराः कुक्कुटादृते. The affix is 3.1.135's क."),
    ),
    '6.1.151': (
        _c('सुश्चन्द्र (suścandra) — in a मन्त्र, after a short vowel',
           {'uttarapada': 'candra', 'mantra': True},
           note='ह्रस्वाच्चन्द्रोत्तरपदे मन्त्रे — in a मन्त्र, after a short vowel, before चन्द्र standing as the second member of a compound: सुश्चन्द्र युष्मान्.'),
    ),
    '6.1.152': (
        _c('प्रतिष्कशः (pratiṣkaśaḥ) — a man sent on ahead',
           {'stem': 'kaś', 'pre': 'prati'},
           note="प्रतिष्कशश्च कशेः — before कश् with प्रति and 3.1.134's अच्, laid down with its सुट् and its ष्: ग्राममद्य प्रवेक्ष्यामि भव मे त्वं प्रतिष्कशः — वार्तापुरुषः, सहायः,"),
    ),
    '6.1.153': (
        _c('प्रस्कण्व ऋषिः (praskaṇva ṛṣiḥ) — two names, of the seers alone',
           {'stem': 'praskaṇva', 'result': 'ṛṣi'},
           note='प्रस्कण्वहरिश्चन्द्रावृषी — two names laid down, and only of the ṛṣis who bear them: प्रस्कण्व ऋषिः; हरिश्चन्द्र ऋषिः. And the second is here for a reason 6.1.151 makes'),
    ),
    '6.1.154': (
        _c('मस्करो वेणुः (maskaro veṇuḥ) — a bamboo, and a wandering monk',
           {'stem': 'maskara'},
           note='मस्करमस्करिणौ वेणुपरिव्राजकयोः — two words यथासंख्यम्, a bamboo and a wandering mendicant: मस्करो वेणुः; मस्करी परिव्राजकः. On the plain reading मकर is अव्युत्पन्नं'),
    ),
    '6.1.155': (
        _c('कास्तीरं नाम नगरम् (kāstīraṃ nāma nagaram)',
           {'stem': 'kāstīra', 'result': 'nagara'},
           note='कास्तीराजस्तुन्दे नगरे — two city names laid down: कास्तीरं नाम नगरम्; अजस्तुन्दं नाम नगरम्. The vṛtti gives each an etymology and then sets it aside: ईषत्तीरमस्य,'),
    ),
    '6.1.156': (
        _c('कारस्करो वृक्षः (kāraskaro vṛkṣaḥ) — a tree of that name',
           {'stem': 'kāraskara', 'result': 'vṛkṣa'},
           note="कारस्करो वृक्षः — laid down for the tree of that name, with 3.2.21's ट: कारस्करो वृक्षः."),
    ),
    '6.1.157': (
        _c('पारस्करो देशः (pāraskaro deśaḥ) — a list that cannot be closed',
           {'stem': 'pāraskara'},
           note='पारस्करप्रभृतीनि च संज्ञायाम् — a list of names laid down with their सुट्, and the rule whose words bound the heading opened at 6.1.135: पारस्करो देशः; रथस्पा नदी;'),
    ),
    '6.1.158': (
        _c('अनुदात्तं पदम् (anudāttaṃ padam) — a maxim that names no syllable itself',
           {},
           note='अनुदात्तं पदमेकवर्जम् — परिभाषेयं स्वरविधिविषया। यत्रान्यः स्वर उदात्तः स्वरितो वा विधीयते, तत्रानुदात्तं पदमेकं वर्जयित्वा भवति — one syllable of a word takes the'),
    ),
    '6.1.159': (
        _c('पाकः (pākaḥ) — a घञ् stem accented at its end',
           {'stem': 'kṛṣ', 'marker': 'ghañ'},
           note='कर्षात्वतो घञोऽन्त उदात्तः — a घञ् stem from कृष् or with a long आ in it takes the accent on its last syllable: कर्षः, पाकः, त्यागः, रागः, दायः, धायः.'),
    ),
    '6.1.160': (
        _c('उञ्छः (uñchaḥ) — a list of words accented at the end',
           {'gana': 'uñchādi'},
           note="उञ्छादीनां च — a list, end-accented: उञ्छः, म्लेच्छः, जञ्जः, जल्पः, जपः, वधः, युगः. Some are घञ् stems and would have taken 6.1.197's accent; some are अप् stems and"),
    ),
    '6.1.161': (
        _c('कुमारी (kumārī) — the accent moving onto what displaced it',
           {'after': 'udātta-lopa'},
           note='अनुदात्तस्य च यत्रोदात्तलोपः — where an उदात्त is dropped before an अनुदात्त, that अनुदात्त takes the accent at its first syllable: कुमारी from कुमार꣡ + ई॒, पथः, पथा,'),
    ),
    '6.1.162': (
        _c('पचति (pacati) — a root accented on its last syllable',
           {'before': 'dhātu'},
           note='धातोः — a root takes the accent on its last syllable: पचति, पठति, ऊर्णोति, गोपायति, याति. अन्त इत्येव — the word carries down from 6.1.159, and this is the accent every'),
    ),
    '6.1.163': (
        _c('भङ्गुरम् (bhaṅguram) — an affix marked च् accenting the end',
           {'marker': 'cit'},
           note="चितः — a stem made by an affix, augment or substitute marked च् takes the accent at its end: भङ्गुरम्, भासुरम्, मेदुरम् with 3.2.161's घुरच्; कुण्डिनाः with 2.4.70's"),
    ),
    '6.1.164': (
        _c('कौञ्जायनाः (kauñjāyanāḥ) — a taddhita marked च्, accented at its end',
           {'marker': 'cit', 'before': 'taddhita'},
           note="तद्धितस्य — and a taddhita stem marked च् likewise: कौञ्जायनाः, भौञ्जायनाः with 4.1.98's च्फञ्."),
    ),
    '6.1.165': (
        _c('नाडायनः (nāḍāyanaḥ) — a taddhita marked क्, accented at its end',
           {'marker': 'kit', 'before': 'taddhita'},
           note="कितः — and a taddhita marked क् too: नाडायनः, चारायणः with 4.1.99's फक्; आक्षिकः, शालाकिकः with 4.4.1's ठक्"),
    ),
    '6.1.166': (
        _c('तिस्रः (tisraḥ) — the nominative plural of the word for three',
           {'stem': 'tisṛ', 'before': 'jas'},
           note='तिसृभ्यो जसः — तिस्रस्तिष्ठन्ति, and the accent displaces the स्वरित 8.2.4 would give.'),
    ),
    '6.1.167': (
        _c('चतुरः पश्य (caturaḥ paśya) — the word for four, in the accusative',
           {'stem': 'catur', 'before': 'śas'},
           note='चतुरः शसि — चतुरः पश्य, the accent on तु. And the feminine is kept out twice over: चतस्रादेश आद्युदात्तनिपातनाद् यणादेशस्य च पूर्वविधौ स्थानिवत्त्वाद् अयं स्वरो न भवति'),
    ),
    '6.1.168': (
        _c('वाचा (vācā) — the case-endings accented after a short stem',
           {'before': 'tṛtīyādi-vibhakti', 'after': 'ekāc'},
           note='सावेकाचस्तृतीयादिर्विभक्तिः — where the stem is one-syllabled AS IT STANDS IN THE LOCATIVE PLURAL, the endings from the third case on take the accent: वाचा, वाग्भ्याम्,'),
    ),
    '6.1.169': (
        _c('परमवाचा (paramavācā) — the same endings, as a choice',
           {'before': 'tṛtīyādi-vibhakti', 'after': 'antodātta-uttarapada'},
           note='अन्तोदात्तादुत्तरपदादन्यतरस्यामनित्यसमासे — in a compound that can be unloosened, and whose second member is one-syllabled and end-accented, the same endings take the'),
    ),
    '6.1.170': (
        _c('दधीचो अस्थभिः (dadhīco asthabhiḥ) — in the Veda, after अञ्च्',
           {'before': 'asarvanāmasthāna', 'after': 'añc', 'chandasi': True},
           note='अञ्चेश्छन्दस्यसर्वनामस्थानम् — in the corpus, after a stem in अञ्च् the weak endings take the accent: इन्द्रो दधीचो अस्थभिः. It displaces 6.1.222, which would have put'),
    ),
    '6.1.171': (
        _c('अद्भिः (adbhiḥ) — seven bases whose weak endings are accented',
           {'stem': 'ūṭh', 'before': 'asarvanāmasthāna'},
           note='ऊडिदम्पदाद्यप्पुम्रैद्युभ्यः — after seven bases the weak endings take the accent: प्रष्ठौहः, प्रष्ठौहा; आभ्याम्, एभिः; पदश्चतुरो जहि; अपः पश्य, अद्भिः; पुंसः,'),
    ),
    '6.1.172': (
        _c('अष्टाभिः (aṣṭābhiḥ) — but only after the LONG form',
           {'stem': 'aṣṭan', 'before': 'asarvanāmasthāna', 'after': 'aṣṭā'},
           note='अष्टनो दीर्घात् — after the LONG form of अष्टन् the weak endings take the accent: अष्टाभिः, अष्टाभ्यः, अष्टासु, against अष्टभिः and अष्टसु.'),
    ),
    '6.1.173': (
        _c('तुदती (tudatī) — after a participle without its न्',
           {'marker': 'śatṛ', 'before': 'nadī-ajādi', 'after': 'antodātta'},
           note='शतुरनुमो नद्यजादी — after an end-accented शतृ participle without its नुम्, the feminine ई and the vowel-initial weak endings take the accent: तुदती, नुदती, लुनती, पुनती;'),
    ),
    '6.1.174': (
        _c('कर्त्री (kartrī) — after a semivowel that stood for an accent',
           {'before': 'nadī-ajādi', 'after': 'udātta-yaṇ-hal-pūrva'},
           note='उदात्तयणो हल्पूर्वात् — where a semivowel stands for an उदात्त vowel and a consonant stands before it, the same endings take the accent: कर्त्री, हर्त्री, प्रलवित्री;'),
    ),
    '6.1.175': (
        _c('ब्रह्मबन्ध्वा (brahmabandhvā) — the feminine ऊ excepted',
           {'before': 'tṛtīyādi-vibhakti', 'after': 'ūṅ-dhātu-yaṇ'},
           note="न उङ्धात्वोः — but not where the semivowel stands for the feminine ऊङ् or for a root's own final: ब्रह्मबन्ध्वा, ब्रह्मबन्ध्वे; सकृल्ल्वा, खलप्वे."),
    ),
    '6.1.176': (
        _c('अग्निमान् (agnimān) — the affix मत् taking the accent',
           {'before': 'matup', 'after': 'hrasva-antodātta'},
           note='ह्रस्वनुड्भ्यां मतुप् — मतुप् takes the accent after an end-accented stem ending in a light vowel, or after the augment नुट्: अग्निमान्, वायुमान्, कर्तृमान्; अक्षण्वता,'),
    ),
    '6.1.177': (
        _c('अग्नीनाम् (agnīnām) — the genitive plural, as a choice',
           {'before': 'nām', 'after': 'hrasva-antodātta'},
           note='नामन्यतरस्याम् — and the genitive plural नाम् optionally: अग्नीनाम् beside अग्नीनाम्, वायूनाम्, कर्तॄणाम्.'),
    ),
    '6.1.178': (
        _c('बह्वीनाम् (bahvīnām) — variously, in the Veda',
           {'before': 'nām', 'after': 'ṅī', 'chandasi': True},
           note='ङ्याश्छन्दसि बहुलम् — in the corpus, नाम् takes the accent variously after the feminine ई: देवसेनानाम् अभिभञ्जतीनाम्; बह्वीनां पिता. And sometimes not — which is what'),
    ),
    '6.1.179': (
        _c('षड्भिः (ṣaḍbhiḥ) — the numerals, before a consonant',
           {'gana': 'ṣaṭ', 'before': 'halādi-vibhakti'},
           note='षट्त्रिचतुर्भ्यो हलादिः — after the numerals called षट्, and after त्रि and चतुर्, a consonant-initial ending takes the accent: षड्भिः, षड्भ्यः, पञ्चानाम्, षण्णाम्,'),
    ),
    '6.1.180': (
        _c('पञ्चभिः (pañcabhiḥ) — and now on the syllable before the last',
           {'gana': 'ṣaṭ', 'before': 'jhalādi-vibhakti'},
           note='झल्युपोत्तमम् — where the ending begins with a झल्, the accent goes to the syllable before the last: पञ्चभिः, सप्तभिः, तिसृभिः, चतुर्भिः.'),
    ),
    '6.1.181': (
        _c('पञ्चभिः (pañcabhiḥ) — a choice in ordinary speech',
           {'gana': 'ṣaṭ', 'before': 'jhalādi-vibhakti', 'bhasayam': True},
           note='विभाषा भाषायाम् — in ordinary speech the rule before is a choice: पञ्चभिः beside पञ्चभिः, सप्तभिः, तिसृभिः, चतुर्भिः. In the corpus it is fixed, and this is the only'),
    ),
    '6.1.182': (
        _c('गवा (gavā) — seven bases where none of it applies',
           {'stem': 'go'},
           note='न गोश्वन्सावर्णराडङ्क्रुङ्कृद्भ्यः — after seven bases everything from 6.1.168 on is refused: गवा, गवे, गोभ्याम्; शुना, शुने; येभ्यः, तेभ्यः, केभ्यः; राजा; प्राञ्चा,'),
    ),
    '6.1.183': (
        _c('द्युभ्याम् (dyubhyām) — दिव् before a झल् ending',
           {'stem': 'div', 'before': 'jhalādi-vibhakti'},
           note='दिवो झल् — after दिव् a झल्-initial ending is not accented: द्युभ्याम्, द्युभिः. The refusal reaches two rules at once, since दिव् is named in 6.1.171 and is'),
    ),
    '6.1.184': (
        _c('नृभिः (nṛbhiḥ) — and after नृ, as a choice',
           {'stem': 'nṛ', 'before': 'jhalādi-vibhakti'},
           note='नृ चान्यतरस्याम् — and after नृ the same refusal is a choice: नृभ्याम्, नृभिः, नृभ्यः, नृषु beside the accented forms'),
    ),
    '6.1.185': (
        _c('कार्यम् (kāryam) — an affix marked त् taking the स्वरित',
           {'marker': 'tit'},
           note='तित् स्वरितम् — an affix marked त् takes the स्वरित, and this is the first rule of the pāda that gives one: चिकीर्ष्यम्, जिहीर्ष्यम् with यत्; कार्यम्, हार्यम् with'),
    ),
    '6.1.186': (
        _c('पचतः (pacataḥ) — a personal ending left unaccented',
           {'before': 'la-sārvadhātuka', 'after': 'tāsi-anudāttet-ṅit-adupadeśa'},
           note='तास्यनुदात्तेङ्ङिदद्रुपदेशाल्लसार्वधातुकमनुदात्तमह्न्विङोः — a सार्वधातुक ending is unaccented after the तास् of the periphrastic future, after a root the धातुपाठ marked'),
    ),
    '6.1.187': (
        _c('मा हि कार्ष्टाम् (mā hi kārṣṭām) — the aorist, as a choice',
           {'before': 'sic'},
           note='आदिः सिचोऽन्यतरस्याम् — a सिच् aorist may take the accent on its first syllable: मा हि कार्ष्टाम् beside मा हि कार्ष्टाम्; मा हि लाविष्टाम् beside मा हि लाविष्टाम्.'),
    ),
    '6.1.188': (
        _c('स्वपन्ति (svapanti) — one list of roots, as a choice',
           {'gana': 'svapādi', 'before': 'ac-aniṭ-la-sārvadhātuka'},
           note='स्वपादिहिंसामच्यनिटि — स्वप् and its list, and हिंस्, may take the accent on the first syllable before a vowel-initial सार्वधातुक ending without इट्: स्वपन्ति, श्वसन्ति,'),
    ),
    '6.1.189': (
        _c('ददति (dadati) — and for a doubled stem, no choice',
           {'gana': 'abhyasta', 'before': 'ac-aniṭ-la-sārvadhātuka'},
           note='अभ्यस्तानामादिः — and for an अभ्यस्त the same accent is FIXED: ददति, ददतु, दधति, जक्षति, जाग्रति. आदिरिति वर्तमाने पुनरादिग्रहणं नित्यार्थम् — आदि was already carrying,'),
    ),
    '6.1.190': (
        _c('ददाति (dadāti) — and before a wholly unaccented ending',
           {'gana': 'abhyasta', 'before': 'anudātta-la-sārvadhātuka'},
           note='अनुदात्ते च — and before an ending that has no उदात्त in it at all: ददाति, जहाति, दधाति, जिहीते, मिमीते. अनजाद्यर्थ आरम्भः — the rule exists for the consonant-initial'),
    ),
    '6.1.191': (
        _c('सर्वे (sarve) — the word for *all*, before a case-ending',
           {'stem': 'sarva', 'before': 'sup'},
           note='सर्वस्य सुपि — सर्व takes the accent on its first syllable before a case-ending: सर्वः, सर्वौ, सर्वे.'),
    ),
    '6.1.192': (
        _c('बिभेति (bibheti) — nine roots accented before the ending',
           {'gana': 'bhyādi', 'before': 'pit-la-sārvadhātuka'},
           note='भीह्रीभृहुमदजनधनदरिद्राजागरां प्रत्ययात् पूर्वं पिति — nine roots take the accent on the syllable BEFORE the ending, where that ending is पित्: बिभेति, जिह्रेति,'),
    ),
    '6.1.193': (
        _c('चिकीर्षकः (cikīrṣakaḥ) — before any affix marked ल्',
           {'marker': 'lit'},
           note="लिति — and before any affix marked ल्, the syllable before it: चिकीर्षकः, जिहीर्षकः with 3.1.133's ण्वुल्; भौरिकिविधम्, ऐषुकारिभक्तम् with 4.2.54's विधल् and भक्तल्"),
    ),
    '6.1.194': (
        _c('लोलूयम् (lolūyam) — before णमुल्, as a choice',
           {'before': 'ṇamul'},
           note="आदिर्णमुल्यन्यतरस्याम् — before णमुल् the first syllable may take it: लोलूयंलोलूयम् beside लोलूयंलोलूयम्. And the other side is 6.1.193's, the affix being लित्. The rule"),
    ),
    '6.1.195': (
        _c('लूयते (lūyate) — a passive used reflexively, as a choice',
           {'before': 'kartṛ-yak', 'after': 'ajanta-upadeśa'},
           note='अचः कर्तृयकि — a root taught ending in a vowel may take the accent on its first syllable before the passive यक् used reflexively: लूयते केदारः स्वयमेव beside लूयते;'),
    ),
    '6.1.196': (
        _c('लुलविथ (lulavitha) — one form and four accentuations',
           {'before': 'thal-seṭ'},
           note="थलि च सेटीडन्तो वा — before a थल् with its इट्, the accent may be on the इट्, on the ending, or on the first syllable — and with 6.1.193's fourth alternative तेनैते"),
    ),
    '6.1.197': (
        _c('गार्ग्यः (gārgyaḥ) — an affix marked ञ् or न्',
           {'marker': 'ñit-nit'},
           note="ञ्नित्यादिर्नित्यम् — whatever is made by an affix marked ञ् or न् takes the accent on its first syllable, invariably: गार्ग्यः, वात्स्यः with 4.1.105's यञ्; वासुदेवकः,"),
    ),
    '6.1.198': (
        _c('देवदत्त (devadatta) — a vocative accented at the front',
           {'before': 'āmantrita'},
           note='आमन्त्रितस्य च — a vocative takes the accent on its first syllable: देवदत्त, देवदत्तौ, देवदत्ताः, displacing the end-accent 6.2.148 would give.'),
    ),
    '6.1.199': (
        _c('पन्थाः (panthāḥ) — two stems, before a strong ending',
           {'stem': 'pathin', 'before': 'sarvanāmasthāna'},
           note='पथिमथोः सर्वनामस्थाने — before a strong ending these two take the accent on the first syllable: पन्थाः, पन्थानौ, पन्थानः; मन्थाः, मन्थानौ, मन्थानः. Both are औणादिक इनि'),
    ),
    '6.1.200': (
        _c('कर्तवै (kartavai) — two accents at once, in one word',
           {'before': 'tavai'},
           note='अन्तश्च तवै युगपत् — an infinitive in तवै takes the accent on its FIRST and LAST syllables AT ONCE: कर्तवै, हर्तवै.'),
    ),
    '6.1.201': (
        _c('क्षये (kṣaye) — the word for a dwelling',
           {'stem': 'kṣaya', 'result': 'nivāsa'},
           note="क्षयो निवासे — क्षय takes the accent on its first syllable where it means a dwelling: क्षये जागृहि प्रपश्यन् — क्षियन्ति निवसन्त्यस्मिन्निति क्षयः. The word is 3.3.118's"),
    ),
    '6.1.202': (
        _c("जयोऽश्वः (jayo'śvaḥ) — the horse one wins by",
           {'stem': 'jaya', 'result': 'karaṇa'},
           note='जयः करणम् — and जय where it means what one wins BY: जयोऽश्वः — जयन्ति तेनेति जयः. The same घ and the same displacement as the rule before, and the two are told apart by'),
    ),
    '6.1.203': (
        _c('वृषः (vṛṣaḥ) — a list accented on the first syllable',
           {'gana': 'vṛṣādi'},
           note='वृषादीनां च — a list, first-accented: वृषः, जनः, ज्वरः, ग्रहः, हयः, गयः, नयः, अंशः, वेदः, सूदः, गुहा, मन्त्रः, शान्तिः, कामः, यामः, आरा, धारा, कारा, कल्पः, पादः.'),
    ),
    '6.1.204': (
        _c('चञ्चा (cañcā) — a likeness serving as a name',
           {'before': 'upamāna', 'samjna': True},
           note='संज्ञायामुपमानम् — a word used as a LIKENESS and serving as a name takes the accent on its first syllable: चञ्चा, वर्ध्रिका, खरकुटी, दासी.'),
    ),
    '6.1.205': (
        _c('बुद्धः (buddhaḥ) — a two-syllabled participle used as a name',
           {'before': 'niṣṭhā', 'after': 'dvyac-anāt', 'samjna': True},
           note='निष्ठा च द्व्यजनात् — a two-syllabled निष्ठा participle serving as a name takes the accent on its first syllable, unless that syllable holds an आ: दत्तः, गुप्तः, बुद्धः.'),
    ),
    '6.1.206': (
        _c('शुष्कः (śuṣkaḥ) — two words that are not names at all',
           {'stem': 'śuṣka'},
           note='शुष्कधृष्टौ — two words first-accented, and असंज्ञार्थ आरम्भः — the rule exists because they are NOT names and 6.1.205 could not reach them: शुष्कः, धृष्टः'),
    ),
    '6.1.207': (
        _c('आशितो देवदत्तः (āśito devadattaḥ) — the one who has eaten',
           {'stem': 'āśita', 'result': 'kartṛ'},
           note='आशितः कर्ता — आशित takes the accent on its first syllable where it names the one who has EATEN: आशितो देवदत्तः. Where the same form names the food or the eating it keeps'),
    ),
    '6.1.208': (
        _c('रिक्तः (riktaḥ) — one word, as a choice',
           {'stem': 'rikta'},
           note='रिक्ते विभाषा — रिक्त optionally: रिक्तः beside रिक्तः. And where it IS a name, संज्ञायां पूर्वविप्रतिषेधेन नित्यमाद्युदात्तः — 6.1.205 wins by being stated earlier, and'),
    ),
    '6.1.209': (
        _c('जुष्टः (juṣṭaḥ) — two words, as a choice in the Veda',
           {'stem': 'juṣṭa', 'chandasi': True},
           note='जुष्टार्पिते च छन्दसि — two words optionally first-accented in the corpus: जुष्टः beside जुष्टः, अर्पितः beside अर्पितः'),
    ),
    '6.1.210': (
        _c('जुष्टं देवानाम् (juṣṭaṃ devānām) — and in a मन्त्र, fixed',
           {'stem': 'juṣṭa', 'mantra': True},
           note='नित्यं मन्त्रे — and in a मन्त्र the same two are fixed: जुष्टं देवानाम्; अर्पितं पितॄणाम्.'),
    ),
    '6.1.211': (
        _c('तव स्वम् (tava svam) — the genitive of *you* and *I*',
           {'stem': 'yuṣmad', 'before': 'ṅas'},
           note='युष्मदस्मदोर्ङसि — the genitive singular forms take the accent on the first syllable: तव स्वम्, मम स्वम्. Both stems are end-accented by their औणादिक affix, and 8.2.5'),
    ),
    '6.1.212': (
        _c('तुभ्यम् (tubhyam) — and the dative of the same two',
           {'stem': 'yuṣmad', 'before': 'ṅe'},
           note="ङयि च — and the dative singular: तुभ्यम्, मह्यम्. पृथग्योगकरणं यथासंख्यशङ्कानिवृत्त्यर्थम् — stated as a second sūtra rather than joined to the first, so that 1.3.10's"),
    ),
    '6.1.213': (
        _c('चेयम् (ceyam) — a two-syllabled यत् stem',
           {'marker': 'yat', 'after': 'dvyac'},
           note="यतोऽनावः — a two-syllabled यत् stem takes the accent on its first syllable: चेयम्, जेयम् with 3.1.97's यत्; कण्ठ्यम्, ओष्ठ्यम् with 5.1.6's. तित्स्वरितम् इत्यस्यापवादः —"),
    ),
    '6.1.214': (
        _c('ईड्यम् (īḍyam) — five roots before the affix ण्यत्',
           {'stem': 'īḍ', 'marker': 'ṇyat'},
           note='ईडवन्दवृशंसदुहां ण्यतः — five roots before ण्यत्: ईड्यम्, वन्द्यम्, वार्यम्, शंस्यम्, दोह्या धेनुः.'),
    ),
    '6.1.215': (
        _c('वेणुः (veṇuḥ) — two words, as a choice',
           {'stem': 'veṇu'},
           note='विभाषा वेण्विन्धानयोः — two words optionally first-accented: वेणुः beside वेणुः; इन्धानः beside two other accentuations.'),
    ),
    '6.1.216': (
        _c('त्यागः (tyāgaḥ) — six words, as a choice',
           {'stem': 'tyāga'},
           note='त्यागरागहासकुहश्वठक्रथानाम् — six words optionally first-accented: त्यागः, रागः, हासः, कुहः, श्वठः, क्रथः, each beside its end-accented form. The first three are घञ्'),
    ),
    '6.1.217': (
        _c('करणीयम् (karaṇīyam) — an affix marked र्',
           {'marker': 'rit'},
           note="उपोत्तमं रिति — a stem made by an affix marked र् takes the accent on the syllable before its last: करणीयम्, हरणीयम् with 3.1.96's अनीयर्; पटुजातीयः, मृदुजातीयः with"),
    ),
    '6.1.218': (
        _c('मा हि चीकरताम् (mā hi cīkaratām) — the चङ् aorist, as a choice',
           {'before': 'caṅ'},
           note='चङ्यन्यतरस्याम् — a चङ् aorist may take the accent on its penult: मा हि चीकरताम् beside मा हि चीकरताम्. The other side is the चित् accent of चङ् itself'),
    ),
    '6.1.219': (
        _c('शरावती (śarāvatī) — the आ before मत्, in a feminine name',
           {'before': 'matup', 'samjna': True, 'stri': True},
           note='मतोः पूर्वमात् संज्ञायां स्त्रियाम् — the आ before मतुप् takes the accent where the word is a feminine NAME: उदुम्बरावती, पुष्करावती, वीरणावती, शरावती, the lengthening'),
    ),
    '6.1.220': (
        _c('हंसवती (haṃsavatī) — a name ending in अवती',
           {'after': 'avatī', 'samjna': True},
           note='अन्तोऽवत्याः — a name ending in अवती takes the accent on its last syllable: अजिरवती, खदिरवती, हंसवती, कारण्डवती. The ङीप् is पित् and would have been unaccented.'),
    ),
    '6.1.221': (
        _c('अहीवती (ahīvatī) — and a name ending in ईवती',
           {'after': 'īvatī', 'samjna': True, 'stri': True},
           note='ईवत्याः — and a feminine name ending in ईवती likewise: अहीवती, कृषीवती, मुनीवती'),
    ),
    '6.1.222': (
        _c('दधीचः (dadhīcaḥ) — before the अञ्च् that lost its न्',
           {'before': 'cu'},
           note='चौ — before the अञ्च् whose न् has been dropped, the word in front takes the accent on its last syllable: दधीचः पश्य, दधीचा, दधीचे; मधूचः, मधूचा.'),
    ),
    '6.1.223': (
        _c('राजपुरुषः (rājapuruṣaḥ) — a compound accented at its end',
           {'before': 'samāsa'},
           note='समासस्य — a compound takes the accent on its last syllable: राजपुरुषः, ब्राह्मणकम्बलः, कन्यास्वनः, पटहशब्दः, नदीघोषः; राजपृषत्, ब्राह्मणसमित्. नानापदस्वरस्यापवादः — the'),
    ),
    '6.2.1': (
        _c('कार्ष्णोत्तरासङ्गाः (kārṣṇottarāsaṅgāḥ) — the first member keeping its accent',
           {'samasa': 'bahuvrīhi'},
           note='बहुव्रीहौ प्रकृत्या पूर्वपदम् — in a बहुव्रीहि the first member keeps the accent it had: कार्ष्णोत्तरासङ्गाः, यूपवलजः, ब्रह्मचारिपरिस्कन्दः, स्नातकपुत्रः, अध्यापकपुत्रः,'),
    ),
    '6.2.2': (
        _c('तुल्यश्वेतः (tulyaśvetaḥ) — seven kinds of first member in a तत्पुरुष',
           {'kind': 'tulyārtha', 'samasa': 'tatpuruṣa'},
           note='तत्पुरुषे तुल्यार्थतृतीयासप्तम्युपमानाव्ययद्वितीयाकृत्याः — seven kinds of first member keep their accent in a तत्पुरुष, and they are described rather than listed: a'),
    ),
    '6.2.3': (
        _c('कृष्णसारङ्गः (kṛṣṇasāraṅgaḥ) — one colour before another',
           {'purvapada': 'varṇa', 'uttarapada': 'varṇa', 'samasa': 'tatpuruṣa'},
           note='वर्णो वर्णेष्वनेते — a colour-word before another colour-word, and not before एत: कृष्णसारङ्गः, लोहितकल्माषः. Three conditions and the vṛtti gives a counter-example for'),
    ),
    '6.2.4': (
        _c('शम्बगाधम् (śambagādham) — water as deep as an oar',
           {'uttarapada': 'gādha', 'samasa': 'tatpuruṣa', 'result': 'pramāṇa'},
           note='गाधलवणयोः प्रमाणे — before गाध or लवण where a MEASURE is meant: शम्बगाधमुदकम् — water only as deep as an oar; गोलवणम् — as much salt as is given to a cow.'),
    ),
    '6.2.5': (
        _c('विद्यादायादः (vidyādāyādaḥ) — heir to a learning',
           {'uttarapada': 'dāyāda', 'samasa': 'tatpuruṣa', 'result': 'dāyādya'},
           note='दायाद्यं दायादे — before दायाद, where the first member names what is INHERITED: विद्यादायादः, धनदायादः.'),
    ),
    '6.2.6': (
        _c('गमनचिरम् (gamanaciram) — a going held up',
           {'uttarapada': 'cira', 'samasa': 'tatpuruṣa', 'result': 'pratibandhin'},
           note='प्रतिबन्धि चिरकृच्छ्रयोः — before चिर or कृच्छ्र, where the first member names what MEETS an obstacle: गमनचिरम्, गमनकृच्छ्रम्, व्याहरणचिरम्. And the vṛtti glosses the'),
    ),
    '6.2.7': (
        _c('मूत्रपदेन (mūtrapadena) — on a pretext',
           {'uttarapada': 'pada', 'samasa': 'tatpuruṣa', 'result': 'apadeśa'},
           note='पदेऽपदेशे — before पद in the sense of a PRETEXT, which the vṛtti glosses अपदेशो व्याजः: मूत्रपदेन प्रस्थितः, उच्चारपदेन प्रस्थितः — gone on the pretext of relieving'),
    ),
    '6.2.8': (
        _c('कुटीनिवातम् (kuṭīnivātam) — a hut against the wind',
           {'uttarapada': 'nivāta', 'samasa': 'tatpuruṣa', 'result': 'vātatrāṇa'},
           note='निवाते वातत्राणे — before निवात where a SHELTER FROM WIND is meant: कुटीनिवातम्, शमीनिवातम्, कुड्यनिवातम् — a hut, an acacia or a wall as the one thing between you and'),
    ),
    '6.2.9': (
        _c('रज्जुशारदम् (rajjuśāradam) — water freshly drawn',
           {'uttarapada': 'śārada', 'samasa': 'tatpuruṣa', 'result': 'anārtava'},
           note='शारदेऽनार्तवे — before शारद where it does NOT mean *of the autumn*: रज्जुशारदमुदकम् — water fresh drawn; दृषत्शारदाः सक्तवः — flour fresh from the grindstone.'),
    ),
    '6.2.10': (
        _c('प्राच्याध्वर्युः (prācyādhvaryuḥ) — a priest of a kind',
           {'uttarapada': 'adhvaryu', 'samasa': 'tatpuruṣa', 'result': 'jāti'},
           note='अध्वर्युकषाययोर्जातौ — before these two where a KIND is meant: प्राच्याध्वर्युः, कठाध्वर्युः, कालापाध्वर्युः; सर्पिर्मण्डकषायम्, उमापुष्पकषायम्. एते समानाधिकरणसमासा'),
    ),
    '6.2.11': (
        _c('पितृसदृशः (pitṛsadṛśaḥ) — like his father',
           {'uttarapada': 'sadṛśa', 'samasa': 'tatpuruṣa', 'result': 'sādṛśya'},
           note='सदृशप्रतिरूपयोः सादृश्ये — before these two where RESEMBLANCE is meant: पितृसदृशः, मातृसदृशः; पितृप्रतिरूपः.'),
    ),
    '6.2.12': (
        _c('प्राच्यसप्तशमः (prācyasaptaśamaḥ) — seven measures long',
           {'uttarapada': 'dvigu', 'samasa': 'dvigu', 'result': 'pramāṇa'},
           note='द्विगौ प्रमाणे — before a द्विगु where a measure is meant: प्राच्यसप्तशमः, गान्धारिसप्तशमः — seven *śama* being its measure, with the मात्रच् dropped by a vārttika on'),
    ),
    '6.2.13': (
        _c('मद्रवाणिजः (madravāṇijaḥ) — a trader who goes to Madra',
           {'purvapada': 'gantavya', 'uttarapada': 'vāṇija', 'samasa': 'tatpuruṣa'},
           note='गन्तव्यपण्यं वाणिजे — before वाणिज, where the first member names either where the trader GOES or what he SELLS: मद्रवाणिजः, काश्मीरवाणिजः — one who trades by going to'),
    ),
    '6.2.14': (
        _c("भिक्षामात्रम् (bhikṣāmātram) — no more than a beggar's share",
           {'uttarapada': 'mātra', 'samasa': 'tatpuruṣa', 'result': 'napuṃsaka'},
           note='मात्रोपज्ञोपक्रमच्छाये नपुंसके — before four words where the compound is NEUTER: भिक्षामात्रं न ददाति याचितः; समुद्रमात्रं न सरोऽस्ति किंचन; पाणिनोपज्ञम् अकालकं'),
    ),
    '6.2.15': (
        _c('गमनसुखम् (gamanasukham) — a going that does one good',
           {'uttarapada': 'sukha', 'samasa': 'tatpuruṣa', 'result': 'hita'},
           note='सुखप्रिययोर्हिते — before सुख or प्रिय where what is GOOD FOR one is meant: गमनसुखम्, वचनसुखम्; गमनप्रियम्. And the vṛtti defines हित by what it does: तद्धि हितं'),
    ),
    '6.2.16': (
        _c('ब्राह्मणसुखं पायसम् (brāhmaṇasukhaṃ pāyasam)',
           {'uttarapada': 'sukha', 'samasa': 'tatpuruṣa', 'result': 'prīti'},
           note='प्रीतौ च — and where PLEASURE itself is meant: ब्राह्मणसुखं पायसम्; छात्रप्रियोऽनध्यायः; कन्याप्रियो मृदङ्गः.'),
    ),
    '6.2.17': (
        _c('गोस्वामी (gosvāmī) — the owner of the cattle',
           {'purvapada': 'sva', 'uttarapada': 'svāmin', 'samasa': 'tatpuruṣa'},
           note='स्वं स्वामिनि — before स्वामिन्, where the first member names what is OWNED: गोस्वामी, अश्वस्वामी, धनस्वामी'),
    ),
    '6.2.18': (
        _c('गृहपतिः (gṛhapatiḥ) — the master of a house',
           {'uttarapada': 'pati', 'samasa': 'tatpuruṣa', 'result': 'aiśvarya'},
           note='पत्यावैश्वर्ये — before पति where LORDSHIP is meant: गृहपतिः, सेनापतिः, नरपतिः, धान्यपतिः. Where the word means a husband instead the compound falls back to 6.1.223'),
    ),
    '6.2.19': (
        _c('भूपतिः (bhūpatiḥ) — four first members refused',
           {'purvapada': 'bhū', 'uttarapada': 'pati', 'samasa': 'tatpuruṣa', 'result': 'aiśvarya'},
           note='न भूवाक्चिद्दिधिषु — four first members are refused what the rule before gives: भूपतिः, वाक्पतिः, चित्पतिः, दिधिषूपतिः, and समासस्वरेणान्तोदात्ता भवन्ति — 6.1.223 takes'),
    ),
    '6.2.20': (
        _c('भुवनपतिः (bhuvanapatiḥ) — and this one, as a choice',
           {'purvapada': 'bhuvana', 'uttarapada': 'pati', 'samasa': 'tatpuruṣa', 'result': 'aiśvarya'},
           note='वा भुवनम् — and भुवन optionally: भुवनपतिः with the first syllable accented, beside the end-accented form.'),
    ),
    '6.2.21': (
        _c('गमनाशङ्कम् (gamanāśaṅkam) — a going one supposes feared',
           {'uttarapada': 'āśaṅka', 'samasa': 'tatpuruṣa', 'result': 'sambhāvana'},
           note='आशङ्काबाधनेदीयस्सु संभावने — before three words where SUPPOSING is meant, and the vṛtti defines it: अस्तित्वाध्यवसायः संभावनम्, settling that a thing is so. गमनाशङ्कं'),
    ),
    '6.2.22': (
        _c('आढ्यपूर्वः (āḍhyapūrvaḥ) — rich, formerly',
           {'uttarapada': 'pūrva', 'samasa': 'tatpuruṣa', 'result': 'bhūtapūrva'},
           note='पूर्वे भूतपूर्वे — before पूर्व in the sense of *formerly so*: आढ्यो भूतपूर्व आढ्यपूर्वः; दर्शनीयपूर्वः, सुकुमारपूर्वः. And the counter-example turns on how the compound'),
    ),
    '6.2.23': (
        _c('मद्रसविधम् (madrasavidham) — near the Madras',
           {'uttarapada': 'savidha', 'samasa': 'tatpuruṣa', 'result': 'sāmīpya'},
           note='सविधसनीडसमर्यादसवेशसदेशेषु सामीप्ये — before five words where NEARNESS is meant: मद्रसविधम्, गान्धारिसनीडम्, काश्मीरसमर्यादम्.'),
    ),
    '6.2.24': (
        _c('विस्पष्टकटुकम् (vispaṣṭakaṭukam) — plainly pungent',
           {'gana': 'vispaṣṭādi', 'uttarapada': 'guṇavacana'},
           note='विस्पष्टादीनि गुणवचनेषु — a list of first members before any quality-word: विस्पष्टकटुकम्, विचित्रकटुकम्, व्यक्तलवणम्.'),
    ),
    '6.2.25': (
        _c('गमनश्रेष्ठम् (gamanaśreṣṭham) — best in the going',
           {'uttarapada': 'śra', 'samasa': 'karmadhāraya', 'result': 'bhāva'},
           note='श्रज्यावमकन्पापवत्सु भावे कर्मधारये — before five, in a कर्मधारय, where the first member names an ACTION: गमनश्रेष्ठम्, वचनज्येष्ठम्, गमनावमम्, गमनकनिष्ठम्, गमनपापिष्ठम्.'),
    ),
    '6.2.26': (
        _c('कुमारश्रमणा (kumāraśramaṇā) — a girl ascetic',
           {'purvapada': 'kumāra', 'samasa': 'karmadhāraya'},
           note='कुमारश्च — कुमार as first member of a कर्मधारय: कुमारश्रमणा, कुमारकुलटा, कुमारतापसी.'),
    ),
    '6.2.27': (
        _c('कुमारप्रत्येनाः (kumārapratyenāḥ) — and now the FIRST syllable',
           {'purvapada': 'kumāra', 'uttarapada': 'pratyenas', 'samasa': 'karmadhāraya'},
           note='आदिः प्रत्येनसि — and before प्रत्येनस् it is the FIRST SYLLABLE of कुमार that takes the accent, not whatever accent the word had: कुमारप्रत्येनाः. The first rule of the'),
    ),
    '6.2.28': (
        _c('कुमारचातकाः (kumāracātakāḥ) — before a word for a guild',
           {'purvapada': 'kumāra', 'uttarapada': 'pūga', 'samasa': 'karmadhāraya'},
           note='पूगेष्वन्यतरस्याम् — and before a word for a GUILD, optionally: कुमारचातकाः, कुमारलोहध्वजाः, कुमारबलाहकाः, कुमारजीमूताः, each in three accentuations.'),
    ),
    '6.2.29': (
        _c('पञ्चारत्निः (pañcāratniḥ) — five cubits long',
           {'uttarapada': 'iganta', 'samasa': 'dvigu'},
           note='इगन्तकालकपालभगालशरावेषु द्विगौ — in a द्विगु, before a second member ending in an इक्, or naming a time, or one of three vessels: पञ्चारत्निः, दशारत्निः; पञ्चमास्यः,'),
    ),
    '6.2.30': (
        _c('बह्वरत्निः (bahvaratniḥ) — and for बहु, as a choice',
           {'purvapada': 'bahu', 'samasa': 'dvigu'},
           note='बह्वन्यतरस्याम् — and for बहु the rule before is a CHOICE: बह्वरत्निः, बहुमास्यः, बहुकपालः each beside its end-accented form. पूर्वेण नित्ये प्राप्ते विकल्पः — what was'),
    ),
    '6.2.31': (
        _c('पञ्चदिष्टिः (pañcadiṣṭiḥ) — five spans',
           {'uttarapada': 'diṣṭi', 'samasa': 'dvigu'},
           note='दिष्टिवितस्त्योश्च — and before these two, optionally: पञ्चदिष्टिः, पञ्चवितस्तिः. Both are measures, so the मात्रच् drops here as it did at 6.2.29'),
    ),
    '6.2.32': (
        _c('सांकाश्यसिद्धः (sāṃkāśyasiddhaḥ) — accomplished at Sāṃkāśya',
           {'uttarapada': 'siddha', 'case': 'saptamī'},
           note='सप्तमी सिद्धशुष्कपक्वबन्धेष्वकालात् — a locative first member before four words, and not where it names a TIME: सांकाश्यसिद्धः, काम्पिल्यसिद्धः; ऊकशुष्कः, निधनशुष्कः;'),
    ),
    '6.2.33': (
        _c('परित्रिगर्तम् (paritrigartam) — all but Trigarta',
           {'purvapada': 'pari', 'result': 'varjyamāna'},
           note='परिप्रत्युपापा वर्ज्यमानाहोरात्रावयवेषु — four preverbs as first member, before a word naming what is LEFT OUT or a part of a day or a night: परित्रिगर्तं वृष्टो देवः;'),
    ),
    '6.2.34': (
        _c('श्वाफल्कचैत्रकाः (śvāphalkacaitrakāḥ) — princes of two houses',
           {'samasa': 'dvandva', 'result': 'andhaka-vṛṣṇi'},
           note='राजन्यबहुवचनद्वन्द्वेऽन्धकवृष्णिषु — in a द्वन्द्व of plural words for princes of the Andhaka and Vṛṣṇi houses: श्वाफल्कचैत्रकाः, चैत्रकरोधकाः, शिनिवासुदेवाः. And राजन्य'),
    ),
    '6.2.35': (
        _c('एकादश (ekādaśa) — a numeral first in a द्वन्द्व',
           {'gana': 'saṅkhyā', 'samasa': 'dvandva'},
           note='संख्या — a numeral as first member of a द्वन्द्व: एकादश, द्वादश, त्रयोदश. एक is first-accented by a नित् उणादि affix, and the त्रयस् that stands for त्रि is laid down'),
    ),
    '6.2.36': (
        _c('आपिशलपाणिनीयाः (āpiśalapāṇinīyāḥ) — two schools of pupils',
           {'samasa': 'dvandva', 'result': 'ācāryopasarjana-antevāsin'},
           note='आचार्योपसर्जनश्चान्तेवासी — in a द्वन्द्व of words for pupils named after their teachers: आपिशलपाणिनीयाः, पाणिनीयरौढीयाः, रौढीयकाशकृत्स्नाः.'),
    ),
    '6.2.37': (
        _c('कार्तकौजपौ (kārtakaujapau) — a list of pairs',
           {'gana': 'kārtakaujapādi', 'samasa': 'dvandva'},
           note='कार्तकौजपादयश्च — a list of द्वन्द्व compounds whose first member keeps its accent: कार्तकौजपौ, सावर्णिमाण्डूकेयौ, अवन्त्यश्मकाः, पैलश्यापर्णेयाः. विभक्त्यन्तानां पाठो'),
    ),
    '6.2.38': (
        _c('महाव्रीहिः (mahāvrīhiḥ) — great rice',
           {'purvapada': 'mahat', 'uttarapada': 'vrīhi'},
           note='महान् व्रीह्यपराह्णगृष्ट्येष्वासजाबालभारभारतहैलिहिलरौरवप्रवृद्धेषु — महत् before ten words: महाव्रीहिः, महापराह्णः, महेष्वासः, महाभारतः, महाप्रवृद्धः.'),
    ),
    '6.2.39': (
        _c('क्षुल्लकवैश्वदेवम् (kṣullakavaiśvadevam)',
           {'purvapada': 'kṣullaka', 'uttarapada': 'vaiśvadeva'},
           note='क्षुल्लकश्च वैश्वदेवे — क्षुल्लक, and महत् carrying down, before वैश्वदेव: क्षुल्लकवैश्वदेवम्, महावैश्वदेवम्'),
    ),
    '6.2.40': (
        _c('उष्ट्रसादि (uṣṭrasādi) — a rider of camels',
           {'purvapada': 'uṣṭra', 'uttarapada': 'sādin'},
           note='उष्ट्रः सादिवाम्योः — उष्ट्र before these two: उष्ट्रसादि, उष्ट्रवामि. The compound is read either as a कर्मधारय or as a genitive one'),
    ),
    '6.2.41': (
        _c('गोसादः (gosādaḥ) — one who drives cattle',
           {'purvapada': 'go', 'uttarapada': 'sāda'},
           note='गौः सादसादिसारथिषु — गो before three: गोसादः, गोसादिः, गोसारथिः, and the first is read two ways — गोः सादो or गां सादयति'),
    ),
    '6.2.42': (
        _c('कुरुगार्हपतम् (kurugārhapatam) — eight named compounds',
           {'gana': 'dāsībhārādi'},
           note='कुरुगार्हपतरिक्तगुर्वसूतजरत्यश्लीलदृढरूपापारेवडवातैतिलकद्रूपण्यकम्बलो दासीभाराणां च — eight named compounds and the दासीभार list: कुरुगार्हपतम्, रिक्तगुरुः, असूतजरती,'),
    ),
    '6.2.43': (
        _c('यूपदारु (yūpadāru) — wood for a sacrificial post',
           {'case': 'caturthī', 'result': 'tadartha'},
           note='चतुर्थी तदर्थे — a dative first member before a word naming what is made FOR it: यूपदारु — wood for a sacrificial post; कुण्डलहिरण्यम्, रथदारु, वल्लीहिरण्यम्.'),
    ),
    '6.2.44': (
        _c("मात्रर्थम् (mātrartham) — for one's mother",
           {'uttarapada': 'artha', 'case': 'caturthī'},
           note='अर्थे — and before the word अर्थ itself: मात्रर्थम्, पित्रर्थम्, देवतार्थम्, अतिथ्यर्थम्. The rule before reached only particular materials — दारु, हिरण्य — and not the'),
    ),
    '6.2.45': (
        _c('गोहितम् (gohitam) — good for the cattle',
           {'uttarapada_affix': 'kta', 'case': 'caturthī'},
           note='क्ते च — and before a क्त participle: गोहितम्, अश्वहितम्, मनुष्यहितम्; गोरक्षितम्, अश्वरक्षितम्, तापसरक्षितम्, with the dative of the person the thing is for'),
    ),
    '6.2.46': (
        _c('श्रेणिकृताः (śreṇikṛtāḥ) — made into rows',
           {'uttarapada_affix': 'kta', 'samasa': 'karmadhāraya'},
           note='कर्मधारयेऽनिष्ठा — in a कर्मधारय before a क्त participle, where the first member is NOT itself one: श्रेणिकृताः, ऊककृताः, पूगकृताः, निधनकृताः'),
    ),
    '6.2.47': (
        _c('ग्रामगतः (grāmagataḥ) — gone to the village',
           {'uttarapada_affix': 'kta', 'case': 'dvitīyā', 'result': 'ahīna'},
           note='अहीने द्वितीया — an accusative first member before a क्त participle, where nothing is FALLEN SHORT OF: कष्टश्रितः, त्रिशकलपतितः, ग्रामगतः. And a supplement adds a'),
    ),
    '6.2.48': (
        _c('अहिहतः (ahihataḥ) — killed by a snake',
           {'uttarapada_affix': 'kta', 'case': 'tṛtīyā', 'result': 'karman'},
           note='तृतीया कर्मणि — an instrumental first member before a क्त participle used in the OBJECT sense: अहिहतः, वज्रहतः, महाराजहतः, नखनिर्भिन्ना, दात्रलूना'),
    ),
    '6.2.49': (
        _c('प्रकृतः (prakṛtaḥ) — a preverb next to the participle',
           {'purvapada': 'gati', 'uttarapada_affix': 'kta', 'result': 'karman'},
           note='गतिरनन्तरः — a गति standing IMMEDIATELY before a क्त participle used in the object sense: प्रकृतः, प्रहृतः. थाथादिस्वरापवादो योगः.'),
    ),
    '6.2.50': (
        _c('प्रकर्ता (prakartā) — and before an affix marked न्',
           {'purvapada': 'gati', 'uttarapada_affix': 'ta-ādi-nit-kṛt'},
           note='तादौ च निति कृत्यतौ — and before a कृत् affix beginning with त् and marked न्, तु excepted: प्रकर्ता with तृन्, प्रकर्तुम्, प्रकृतिः. कृत्स्वरबाधनार्थं वचनम् — stated to'),
    ),
    '6.2.51': (
        _c('अन्वेतवै (anvetavai) — two accents at once',
           {'purvapada': 'gati', 'uttarapada': 'tavai'},
           note='तवै चान्तश्च युगपत् — the तवै takes the accent at its END and the गति keeps its own at the same time: अन्वेतवै, परिस्तरितवै, परिपातवै; तस्मात् पिता नाभिचरितवै.'),
    ),
    '6.2.52': (
        _c('प्राञ्चः (prāñcaḥ) — a preverb before अञ्च्',
           {'purvapada': 'gati', 'uttarapada': 'añc', 'uttarapada_affix': 'va-pratyaya'},
           note='अनिगन्तोऽञ्चतौ वप्रत्यये — a गति not ending in an इक्, before अञ्च् with the affix वि: प्राङ्, प्राञ्चौ, प्राञ्चः; पराङ्, पराञ्चः. And the single substitute is उदात्त or'),
    ),
    '6.2.53': (
        _c('न्यञ्चः (nyañcaḥ) — and these two, which do end in इक्',
           {'purvapada': 'ni', 'uttarapada': 'añc', 'uttarapada_affix': 'va-pratyaya'},
           note='न्यधी च — and these two, which DO end in an इक् and so were kept out by the rule before: न्यङ्, न्यञ्चौ; अध्यङ्, अध्यञ्चः, अधीचः. 8.2.4 then makes the अ of अञ्च् स्वरित'),
    ),
    '6.2.54': (
        _c('ईषत्कडारः (īṣatkaḍāraḥ) — slightly tawny',
           {'purvapada': 'īṣad'},
           note='ईषदन्यतरस्याम् — ईषद् optionally: ईषत्कडारः, ईषत्पिङ्गलः, each beside its end-accented form'),
    ),
    '6.2.55': (
        _c('द्विसुवर्णधनम् (dvisuvarṇadhanam) — wealth of two gold pieces',
           {'purvapada': 'hiraṇyaparimāṇa', 'uttarapada': 'dhana'},
           note='हिरण्यपरिमाणं धने — a first member naming a WEIGHT OF GOLD, before धन, optionally: द्विसुवर्णधनम् beside the end-accented form. And the option reaches the बहुव्रीहि too,'),
    ),
    '6.2.56': (
        _c('प्रथमवैयाकरणः (prathamavaiyākaraṇaḥ) — new to grammar',
           {'purvapada': 'prathama', 'result': 'acira-upasampatti'},
           note='प्रथमोऽचिरोपसंपत्तौ — प्रथम optionally, where NEWNESS is meant, which the vṛtti glosses अचिरोपश्लेषोऽभिनवत्वम्: प्रथमवैयाकरणः — one who has just begun grammar, beside'),
    ),
    '6.2.57': (
        _c('कतरकठः (katarakaṭhaḥ) — which of two Kaṭhas',
           {'purvapada': 'katara', 'samasa': 'karmadhāraya'},
           note='कतरकतमौ कर्मधारये — these two optionally in a कर्मधारय: कतरकठः, कतमकठः, each beside the end-accented form. कर्मधारयग्रहणमुत्तरार्थम् — the word is put in for the rules'),
    ),
    '6.2.58': (
        _c('आर्यब्राह्मणः (āryabrāhmaṇaḥ) — a noble brahmin',
           {'purvapada': 'ārya', 'uttarapada': 'brāhmaṇa', 'samasa': 'karmadhāraya'},
           note='आर्यो ब्राह्मणकुमारयोः — आर्य optionally before these two in a कर्मधारय: आर्यब्राह्मणः, आर्यकुमारः'),
    ),
    '6.2.59': (
        _c('राजब्राह्मणः (rājabrāhmaṇaḥ) — a kingly brahmin',
           {'purvapada': 'rājan', 'uttarapada': 'brāhmaṇa', 'samasa': 'karmadhāraya'},
           note='राजा च — and राजन् likewise: राजब्राह्मणः, राजकुमारः. पृथग्योगकरणमुत्तरार्थम् — split off from the rule before so that राजन् alone carries into the next'),
    ),
    '6.2.60': (
        _c("राजप्रत्येनाः (rājapratyenāḥ) — the king's offender",
           {'purvapada': 'rājan', 'uttarapada': 'pratyenas', 'case': 'ṣaṣṭhī'},
           note='षष्ठी प्रत्येनसि — राजन् in the GENITIVE before प्रत्येनस्, optionally: राजप्रत्येनाः beside the end-accented form'),
    ),
    '6.2.61': (
        _c('नित्यप्रहसितः (nityaprahasitaḥ) — always laughing',
           {'uttarapada_affix': 'kta', 'result': 'nityārtha'},
           note='क्ते नित्यार्थे — before a क्त participle where the compound means ALWAYS, optionally: नित्यप्रहसितः, सततप्रहसितः, each beside its end-accented form'),
    ),
    '6.2.62': (
        _c('ग्रामनापितः (grāmanāpitaḥ) — the village barber',
           {'purvapada': 'grāma', 'result': 'śilpin'},
           note="ग्रामः शिल्पिनि — ग्राम before a word for a CRAFTSMAN, optionally: ग्रामनापितः, ग्रामकुलालः — the village's barber, the village's potter"),
    ),
    '6.2.63': (
        _c('राजनापितः (rājanāpitaḥ) — a barber fit for a king',
           {'purvapada': 'rājan', 'result': 'śilpin-praśaṃsā'},
           note='राजा च प्रशंसायाम् — and राजन् before a craftsman-word where PRAISE is meant, optionally: राजनापितः, राजकुलालः.'),
    ),
    '6.2.64': (
        _c('आदिरुदात्तः (ādir udāttaḥ) — a heading that places and supplies nothing',
           {},
           note="आदिरुदात्तः — आदिरुदात्त इत्येतदधिकृतम्। इत उत्तरं यद् वक्ष्यामस्तत्र पूर्वपदस्यादिरुदात्तो भवतीत्येवं तद् वेदितव्यम् — from here the first member's FIRST SYLLABLE takes"),
    ),
    '6.2.65': (
        _c('याज्ञिकाश्वः (yājñikāśvaḥ) — the horse due to a ritualist',
           {'case': 'saptamī', 'result': 'dharmya'},
           note='सप्तमीहारिणौ धर्म्येऽहरणे — a locative first member, or one naming the TAKER, before a word for what is due by custom, and not before हरण: स्तूपेशाणः, मुकुटेकार्षापणम्,'),
    ),
    '6.2.66': (
        _c('गोबल्लवः (goballavaḥ) — the man set over the cattle',
           {'result': 'yukta'},
           note='युक्ते च — where the compound names one SET TO a task, which the vṛtti glosses युक्त इति समाहितः, कर्तव्ये तत्परो यः: गोबल्लवः, अश्वबल्लवः, गोमणिन्दः, गोसंख्यः'),
    ),
    '6.2.67': (
        _c('गवाध्यक्षः (gavādhyakṣaḥ) — before अध्यक्ष, as a choice',
           {'uttarapada': 'adhyakṣa'},
           note='विभाषाध्यक्षे — before अध्यक्ष, optionally: गवाध्यक्षः, अश्वाध्यक्षः, each beside its end-accented form'),
    ),
    '6.2.68': (
        _c('पापनापितः (pāpanāpitaḥ) — a bad barber',
           {'purvapada': 'pāpa', 'result': 'śilpin'},
           note='पापं च शिल्पिनि — पाप before a craftsman-word, optionally: पापनापितः, पापकुलालः.'),
    ),
    '6.2.69': (
        _c('जङ्घावात्स्यः (jaṅghāvātsyaḥ) — a Vātsya at the price of his shanks',
           {'uttarapada_gana': 'gotra-antevāsin', 'result': 'kṣepa'},
           note='गोत्रान्तेवासिमाणवब्राह्मणेषु क्षेपे — before a word for a lineage or a pupil, and before माणव or ब्राह्मण, where ABUSE is meant: जङ्घावात्स्यः — one who becomes a'),
    ),
    '6.2.70': (
        _c('गुडमैरेयः (guḍamaireyaḥ) — liquor made of molasses',
           {'uttarapada': 'maireya', 'result': 'aṅga'},
           note='अङ्गानि मैरेये — before मैरेय, where the first member names an INGREDIENT of it: गुडमैरेयः, मधुमैरेयः — the liquor made of molasses, the liquor made of honey'),
    ),
    '6.2.71': (
        _c('भिक्षाकंसः (bhikṣākaṃsaḥ) — a bowl for alms-food',
           {'purvapada': 'bhaktākhyā', 'result': 'tadartha'},
           note='भक्ताख्यास्तदर्थेषु — a word for FOOD before a word for what holds it: भिक्षाकंसः, श्राणाकंसः, भाजीकंसः. भक्तमन्नम्, तदाख्यास्तद्वाचिनः शब्दाः — the vṛtti reads the'),
    ),
    '6.2.72': (
        _c('धान्यगवः (dhānyagavaḥ) — grain heaped like a cow',
           {'uttarapada': 'go', 'result': 'upamāna'},
           note='गोबिडालसिंहसैन्धवेषूपमाने — before four words used as a LIKENESS: धान्यगवः — grain heaped in the shape of a cow; भिक्षाबिडालः, तृणसिंहः, सक्तुसैन्धवः. And the vṛtti'),
    ),
    '6.2.73': (
        _c('दन्तलेखकः (dantalekhakaḥ) — one who lives by scratching teeth',
           {'uttarapada_affix': 'aka', 'result': 'jīvikārtha'},
           note='अके जीविकार्थे — before a stem in अक where the compound names a LIVELIHOOD: दन्तलेखकः, नखलेखकः, अवस्करशोधकः — men who live by scratching teeth, by trimming nails, by'),
    ),
    '6.2.74': (
        _c('शालभञ्जिका (śālabhañjikā) — an eastern game',
           {'uttarapada_affix': 'aka', 'result': 'krīḍā-prācām'},
           note='प्राचां क्रीडायाम् — before the same stem where an EASTERN game is named: उद्दालकपुष्पभञ्जिका, वीरणपुष्पप्रचायिका, शालभञ्जिका. A rule whose condition is where in the'),
    ),
    '6.2.75': (
        _c('छत्रधारः (chatradhāraḥ) — the appointed parasol-bearer',
           {'uttarapada_affix': 'aṇ', 'result': 'niyukta'},
           note='अणि नियुक्ते — before a stem in अण् where the compound names one APPOINTED to a charge: छत्रधारः, तूणीरधारः, कमण्डलुग्राहः.'),
    ),
    '6.2.76': (
        _c('तन्तुवायः (tantuvāyaḥ) — a weaver',
           {'uttarapada_affix': 'aṇ', 'result': 'śilpin'},
           note='शिल्पिनि चाकृञः — before a stem in अण् naming a CRAFTSMAN, so long as the affix is not on कृञ्: तन्तुवायः, तुन्नवायः, वालवायः'),
    ),
    '6.2.77': (
        _c('तन्तुवायो नाम कीटः (tantuvāyo nāma kīṭaḥ)',
           {'uttarapada_affix': 'aṇ', 'samjna': True},
           note='संज्ञायां च — and where the compound is a NAME: तन्तुवायो नाम कीटः, वालवायो नाम पर्वतः. The कृञ् exception carries down'),
    ),
    '6.2.78': (
        _c('गोपालः (gopālaḥ) — a cowherd',
           {'purvapada': 'go', 'uttarapada': 'pāla'},
           note='गोतन्तियवं पाले — three first members before पाल: गोपालः, तन्तिपालः, यवपालः. अनियुक्तार्थ आरम्भः — the rule exists for the cowherd who was not APPOINTED one, whom 6.2.75'),
    ),
    '6.2.79': (
        _c('पुष्पहारी (puṣpahārī) — a flower-gatherer',
           {'uttarapada_affix': 'ṇini'},
           note='णिनि — before a stem in णिनि: पुष्पहारी, फलहारी, पर्णहारी. The shortest sūtra of the section, and the widest'),
    ),
    '6.2.80': (
        _c('उष्ट्रक्रोशी (uṣṭrakrośī) — one who cries like a camel',
           {'purvapada': 'upamāna', 'uttarapada_affix': 'ṇini', 'result': 'śabdārtha-prakṛti'},
           note='उपमानं शब्दार्थप्रकृतावेव — where the first member is a LIKENESS, the rule before holds only if the root names a SOUND and does so of itself: उष्ट्रक्रोशी,'),
    ),
    '6.2.81': (
        _c('युक्तारोही (yuktārohī) — a list of whole compounds',
           {'gana': 'yuktārohyādi'},
           note='युक्तारोह्यादयश्च — a list of whole compounds: युक्तारोही, आगतरोही, आगतयोधी, आगतवञ्ची; क्षीरहोता, भगिनीभर्ता; ग्रामगोधुक्, अश्वत्रिरात्रः, एकशितिपात्.'),
    ),
    '6.2.82': (
        _c('कुटीजः (kuṭījaḥ) — born in a hut',
           {'purvapada': 'kāśa', 'uttarapada': 'ja'},
           note='दीर्घकाशतुषभ्राष्ट्रवटं जे — before ज, for a first member ending in a long vowel and for four named words: कुटीजः, शमीजः; काशजः, तुषजः, भ्राष्ट्रजः, वटजः'),
    ),
    '6.2.83': (
        _c('उपसरजः (upasarajaḥ) — and now the syllable before the last',
           {'purvapada': 'bahvac', 'uttarapada': 'ja'},
           note='अन्त्यात् पूर्वं बह्वचः — and where the first member has MANY VOWELS, it is the syllable before the last that takes the accent: उपसरजः, मन्दुरजः, आमलकीजः, वडवाजः.'),
    ),
    '6.2.84': (
        _c('मल्लग्रामः (mallagrāmaḥ) — a body of wrestlers',
           {'uttarapada': 'grāma'},
           note='ग्रामेऽनिवसन्तः — before ग्राम, where the first member does NOT name who lives there: मल्लग्रामः, वणिग्ग्रामः — with ग्राम meaning a body of men; देवग्रामः — the village'),
    ),
    '6.2.85': (
        _c('दाक्षिघोषः (dākṣighoṣaḥ) — before a list of second members',
           {'uttarapada_gana': 'ghoṣādi'},
           note='घोषादिषु च — before a list of second members: दाक्षिघोषः, दाक्षिकटः, दाक्षिह्रदः, दाक्षिबदरी, दाक्ष्यश्वत्थः, आश्रममुनिः.'),
    ),
    '6.2.86': (
        _c("छात्रिशाला (chātriśālā) — a pupils' hall",
           {'gana': 'chātryādi', 'uttarapada': 'śālā'},
           note='छात्र्यादयः शालायाम् — a list of first members before शाला: छात्रिशाला, ऐलिशाला, भाण्डिशाला.'),
    ),
    '6.2.87': (
        _c("इन्द्रप्रस्थः (indraprasthaḥ) — Indra's plain",
           {'uttarapada': 'prastha'},
           note='प्रस्थेऽवृद्धमकर्क्यादीनाम् — before प्रस्थ, for a first member that is not वृद्ध and not on the कर्क्यादि list: इन्द्रप्रस्थः, कुण्डप्रस्थः, ह्रदप्रस्थः, सुवर्णप्रस्थः'),
    ),
    '6.2.88': (
        _c('मालाप्रस्थः (mālāprasthaḥ) — and a list, for the excepted case',
           {'gana': 'mālādi', 'uttarapada': 'prastha'},
           note='मालादीनां च — and a list of first members before प्रस्थ: मालाप्रस्थः, शालाप्रस्थः. वृद्धार्थ आरम्भः — the rule exists for exactly the वृद्ध words the one before it'),
    ),
    '6.2.89': (
        _c('सुह्मनगरम् (suhmanagaram) — a city of the Suhmas',
           {'uttarapada': 'nagara'},
           note='अमहन्नवं नगरेऽनुदीचाम् — before नगर, for a first member that is neither महत् nor नव, and not a northern name: सुह्मनगरम्, पुण्ड्रनगरम्. Three conditions and a'),
    ),
    '6.2.90': (
        _c('दत्तार्मम् (dattārmam) — before अर्म',
           {'uttarapada': 'arma'},
           note='अर्मे चावर्णं द्व्यच् त्र्यच् — before अर्म, for a first member ending in अ or आ and having two or three vowels: दत्तार्मम्, गुप्तार्मम्, कुक्कुटार्मम्, वायसार्मम्. And'),
    ),
    '6.2.91': (
        _c('भूतार्मम् (bhūtārmam) — six first members refused',
           {'purvapada': 'bhūta', 'uttarapada': 'arma'},
           note='न भूताधिकसंजीवमद्राश्मकज्जलम् — six first members are refused what the rule before gives: भूतार्मम्, अधिकार्मम्, संजीवार्मम्, मद्रार्मम्, अश्मार्मम्, कज्जलार्मम्, and'),
    ),
    '6.2.92': (
        _c('अन्तः (antaḥ) — and now the placement moves to the last syllable',
           {},
           note='अन्तः — अन्त इत्यधिकृतम्। इत उत्तरं यद् वक्ष्यामस्तत्र पूर्वपदस्यान्त उदात्तो भवति — from here it is the LAST syllable of the first member, where 6.2.64 gave the first.'),
    ),
    '6.2.93': (
        _c('सर्वश्वेतः (sarvaśvetaḥ) — white all through',
           {'purvapada': 'sarva', 'result': 'guṇakārtsnya'},
           note='सर्वं गुणकार्त्स्न्ये — सर्व where a QUALITY is meant IN FULL: सर्वश्वेतः, सर्वकृष्णः, सर्वमहान्. Three words of the rule and three counter-examples, and the third turns'),
    ),
    '6.2.94': (
        _c("अञ्जनागिरिः (añjanāgiriḥ) — a mountain's name",
           {'uttarapada': 'giri', 'samjna': True},
           note='संज्ञायां गिरिनिकाययोः — before गिरि or निकाय where the compound is a NAME: अञ्जनागिरिः, भञ्जनागिरिः; शापिण्डिनिकायः, मौण्डिनिकायः'),
    ),
    '6.2.95': (
        _c('वृद्धकुमारी (vṛddhakumārī) — an unmarried woman grown old',
           {'uttarapada': 'kumārī', 'result': 'vayas'},
           note='कुमार्यां वयसि — before कुमारी where an AGE is meant: वृद्धकुमारी, जरत्कुमारी. And the vṛtti is careful about which sense of कुमारी is in play: कुमारीशब्दः पुंसा'),
    ),
    '6.2.96': (
        _c('गुडोदकम् (guḍodakam) — water with molasses in it',
           {'uttarapada': 'udaka', 'result': 'akevala'},
           note='उदकेऽकेवले — before उदक where the water is MIXED, अकेवलं मिश्रम्: गुडोदकम्, तिलोदकम्. And the single substitute is then उदात्त or स्वरित by 8.2.6'),
    ),
    '6.2.97': (
        _c('गर्गत्रिरात्रः (gargatrirātraḥ) — a three-night rite of the Gargas',
           {'samasa': 'dvigu', 'result': 'kratu'},
           note='द्विगौ क्रतौ — before a द्विगु naming a SACRIFICE: गर्गत्रिरात्रः, चरकत्रिरात्रः, कुसुरविन्दसप्तरात्रः'),
    ),
    '6.2.98': (
        _c("गोपालसभम् (gopālasabham) — a herdsmen's hall",
           {'uttarapada': 'sabhā', 'result': 'napuṃsaka'},
           note='सभायां नपुंसके — before सभा where the compound is NEUTER: गोपालसभम्, पशुपालसभम्, स्त्रीसभम्, दासीसभम्. And the neuter meant is the one 2.4.23 gives सभा by name: सभायां'),
    ),
    '6.2.99': (
        _c('काञ्चीपुरम् (kāñcīpuram) — an eastern city',
           {'uttarapada': 'pura', 'result': 'prācām'},
           note='पुरे प्राचाम् — before पुर in an EASTERN name: ललाटपुरम्, काञ्चीपुरम्, शिवदत्तपुरम्, कार्णिपुरम्'),
    ),
    '6.2.100': (
        _c('अरिष्टपुरम् (ariṣṭapuram) — where two words stand first',
           {'purvapada': 'ariṣṭa', 'uttarapada': 'pura'},
           note='अरिष्टगौडपूर्वे च — and where अरिष्ट or गौड stands FIRST: अरिष्टपुरम्, गौडपुरम्. And पूर्वे is what lets a third word come between: पूर्वग्रहणं किम्? इहापि यथा स्यात् —'),
    ),
    '6.2.101': (
        _c('हास्तिनपुरम् (hāstinapuram) — three first members refused',
           {'purvapada': 'hāstina', 'uttarapada': 'pura'},
           note='न हास्तिनफलकमार्देयाः — three first members are refused what 6.2.99 gives: हास्तिनपुरम्, फलकपुरम्, मार्देयपुरम्'),
    ),
    '6.2.102': (
        _c('कुसूलबिलम् (kusūlabilam) — the mouth of a granary',
           {'purvapada': 'kusūla', 'uttarapada': 'bila'},
           note='कुसूलकूपकुम्भशालं बिले — four first members before बिल: कुसूलबिलम्, कूपबिलम्, कुम्भबिलम्, शालाबिलम्'),
    ),
    '6.2.103': (
        _c('पूर्वपञ्चालाः (pūrvapañcālāḥ) — the eastern Pañcālas',
           {'purvapada': 'dikśabda', 'uttarapada_gana': 'grāma-janapada-ākhyāna'},
           note='दिक्शब्दा ग्रामजनपदाख्यानचानराटेषु — a direction-word before a village-name, a country-name, a title, or चानराट: पूर्वेषुकामशमी; पूर्वपञ्चालाः; पूर्वाधिरामम्,'),
    ),
    '6.2.104': (
        _c('पूर्वपाणिनीयाः (pūrvapāṇinīyāḥ) — the earlier Pāṇinīyas',
           {'purvapada': 'dikśabda', 'uttarapada_gana': 'ācāryopasarjana-antevāsin'},
           note='आचार्योपसर्जनश्चान्तेवासिनि — and before a word for pupils named after their teacher: पूर्वपाणिनीयाः, अपरपाणिनीयाः, पूर्वकाशकृत्स्नाः'),
    ),
    '6.2.105': (
        _c('सर्वपाञ्चालकः (sarvapāñcālakaḥ) — before a second member with vṛddhi',
           {'purvapada': 'sarva', 'uttarapada': 'vṛddha'},
           note='उत्तरपदवृद्धौ सर्वं च — before a second member that has taken the vṛddhi 7.3.10 heads, for सर्व and for a direction-word: सर्वपाञ्चालकः, पूर्वपाञ्चालकः, उत्तरपाञ्चालकः'),
    ),
    '6.2.106': (
        _c('विश्वदेवः (viśvadevaḥ) — a name, in a बहुव्रीहि',
           {'purvapada': 'viśva', 'samasa': 'bahuvrīhi', 'samjna': True},
           note='बहुव्रीहौ विश्वं संज्ञायाम् — विश्व in a बहुव्रीहि that is a NAME: विश्वदेवः, विश्वयशाः, विश्वमहान्. पूर्वपदप्रकृतिस्वरत्वेनाद्युदात्तत्वं प्राप्तम् — 6.2.1 would have'),
    ),
    '6.2.107': (
        _c('वृकोदरः (vṛkodaraḥ) — wolf-bellied',
           {'uttarapada': 'udara', 'samasa': 'bahuvrīhi', 'samjna': True},
           note='उदराश्वेषुषु — before three words, in a बहुव्रीहि that is a name: वृकोदरः, दामोदरः; हर्यश्वः, यौवनाश्वः; सुवर्णपुङ्खेषुः, महेषुः'),
    ),
    '6.2.108': (
        _c('कुण्डोदरः (kuṇḍodaraḥ) — pot-bellied, said in scorn',
           {'uttarapada': 'udara', 'samasa': 'bahuvrīhi', 'result': 'kṣepa'},
           note='क्षेपे — and before the same three where ABUSE is meant, name or no name: कुण्डोदरः, घटोदरः; कटुकाश्वः, स्पन्दिताश्वः; अनिघातेषुः, चलाचलेषुः. And where a नञ् or a सु'),
    ),
    '6.2.109': (
        _c('गार्गीबन्धुः (gārgībandhuḥ) — kinsman of a Gārgī',
           {'purvapada': 'nadī', 'uttarapada': 'bandhu', 'samasa': 'bahuvrīhi'},
           note='नदी बन्धुनि — a नदी-final first member before बन्धु, in a बहुव्रीहि: गार्गीबन्धुः, वात्सीबन्धुः'),
    ),
    '6.2.110': (
        _c('प्रधौतमुखः (pradhautamukhaḥ) — with his face washed',
           {'uttarapada_affix': 'niṣṭhā-upasarga-pūrva', 'samasa': 'bahuvrīhi'},
           note='निष्ठोपसर्गपूर्वमन्यतरस्याम् — a निष्ठा first member with a preverb before it, in a बहुव्रीहि, optionally: प्रधौतमुखः, प्रक्षालितपादः, in three accentuations between'),
    ),
    '6.2.111': (
        _c("शुक्लकर्णः (śuklakarṇaḥ) — the heading's own example, at 6.2.112",
           {'uttarapada': 'karṇa', 'purvapada_gana': 'varṇa', 'samasa': 'bahuvrīhi'},
           note='उत्तरपदादिः — the vṛtti reads the next sūtra out as its example: वक्ष्यति कर्णो वर्णलक्षणात्'),
    ),
    '6.2.112': (
        _c('शुक्लकर्णः (śuklakarṇaḥ) — white-eared, from a colour-word',
           {'uttarapada': 'karṇa', 'purvapada_gana': 'varṇa', 'samasa': 'bahuvrīhi'},
           note='कर्णो वर्णलक्षणात् — and लक्षण is a brand and not a property, so स्थूलकर्णः is out'),
    ),
    '6.2.113': (
        _c('गोकर्णः (gokarṇaḥ) — cow-eared, the ears compared',
           {'uttarapada': 'karṇa', 'samasa': 'bahuvrīhi', 'result': 'saṃjñā'},
           note='संज्ञायामौपम्ययोश्च — a name or a likeness, where 6.2.112 wanted a colour or a brand'),
    ),
    '6.2.114': (
        _c('नीलकण्ठः (nīlakaṇṭhaḥ) — the blue-throated one, a name',
           {'uttarapada': 'kaṇṭha', 'samasa': 'bahuvrīhi', 'result': 'saṃjñā'},
           note='कण्ठपृष्ठग्रीवाजङ्घं च — throat, back, neck and shank, each with a name and a likeness'),
    ),
    '6.2.115': (
        _c('उद्गतशृङ्गः (udgataśṛṅgaḥ) — horns come up, a stage of life',
           {'uttarapada': 'śṛṅga', 'samasa': 'bahuvrīhi', 'result': 'avasthā'},
           note='शृङ्गमवस्थायां च — शृङ्गोद्गमनादिकृतो गवादेर्वयोविशेषोऽवस्था, the age read off the horns'),
    ),
    '6.2.116': (
        _c('अजरः (ajaraḥ) — ageless, one of the four words named',
           {'uttarapada': 'jara', 'purvapada': 'nañ', 'samasa': 'bahuvrīhi'},
           note='नञो जरमरमित्रमृताः — an exception to 6.2.172, which stands fifty-six sūtras further on'),
    ),
    '6.2.117': (
        _c('सुकर्मा (sukarmā) — of good works, a मन्-ending word',
           {'affix': 'man', 'purvapada': 'su', 'samasa': 'bahuvrīhi'},
           note='सोर्मनसी अलोमोषसी — and कपि तु परत्वात्, so adding कप् hands the word to 6.2.173'),
    ),
    '6.2.118': (
        _c('सुक्रतुः (sukratuḥ) — of good purpose, first of the क्रत्वादि',
           {'gana': 'kratvādi', 'purvapada': 'su', 'samasa': 'bahuvrīhi'},
           note='क्रत्वादयश्च — a six-word gaṇa read out at the end of the vṛtti'),
    ),
    '6.2.119': (
        _c('स्वश्वाः (svaśvāḥ) — of good horses, in the Veda',
           {'purvapada': 'su', 'samasa': 'bahuvrīhi', 'result': 'ādyudātta-dvyac', 'chandasi': True},
           note='आद्युदात्तं द्व्यच्छन्दसि — अश्व is already ādi-accented by its नित्, and this keeps it so'),
    ),
    '6.2.120': (
        _c('सुवीरः (suvīraḥ) — having good heroes, in the Veda',
           {'uttarapada': 'vīra', 'purvapada': 'su', 'samasa': 'bahuvrīhi', 'chandasi': True},
           note='वीरवीर्यौ च — and वीर्यग्रहणं ज्ञापकम्, since otherwise 6.2.119 would already have covered it'),
    ),
    '6.2.121': (
        _c('परिकूलम् (parikūlam) — along the bank, an अव्ययीभाव',
           {'uttarapada': 'kūla', 'samasa': 'avyayībhāva'},
           note='कूलतीरतूलमूलशालाक्षसमम् अव्ययीभावे — and it beats 6.2.33 विप्रतिषेधेन, by standing later'),
    ),
    '6.2.122': (
        _c('द्विकंसः (dvikaṃsaḥ) — worth two कंसas, a द्विगु',
           {'uttarapada': 'kaṃsa', 'samasa': 'dvigu'},
           note='कंसमन्थशूर्पपाय्यकाण्डं द्विगौ — परमकंसः stays out, being no numeral compound'),
    ),
    '6.2.123': (
        _c("ब्राह्मणशालम् (brāhmaṇaśālam) — a brahmin's hall, neuter",
           {'uttarapada': 'śālā', 'samasa': 'tatpuruṣa', 'result': 'napuṃsaka'},
           note='तत्पुरुषे शालायां नपुंसके — ब्राह्मणशाला, left feminine, keeps the accent it had'),
    ),
    '6.2.124': (
        _c('आह्वकन्थम् (āhvakantham) — the rag-quilt of Āhva, neuter',
           {'uttarapada': 'kanthā', 'samasa': 'tatpuruṣa', 'result': 'napuṃsaka'},
           note='कन्था च — and दाक्षिकन्था, left feminine, is out'),
    ),
    '6.2.125': (
        _c('चिहणकन्थम् (cihaṇakantham) — the accent moved to the FIRST member',
           {'uttarapada': 'kanthā', 'purvapada_gana': 'cihaṇādi', 'samasa': 'tatpuruṣa', 'result': 'napuṃsaka'},
           note='आदिश्चिहणादीनाम् — पुनरादिग्रहणं पूर्वपदाद्युदात्तार्थम्, the repeated word turning the rule round'),
    ),
    '6.2.126': (
        _c('पुत्रचेलम् (putracelam) — a son no better than a rag',
           {'uttarapada': 'cela', 'samasa': 'tatpuruṣa', 'result': 'garhā'},
           note='चेलखेटकटुककाण्डं गर्हायाम् — the contempt carried by a likeness, compounded under 2.1.56'),
    ),
    '6.2.127': (
        _c('वस्त्रचीरम् (vastracīram) — cloth like a rag, the rag compared to',
           {'uttarapada': 'cīra', 'samasa': 'tatpuruṣa', 'result': 'upamāna'},
           note='चीरमुपमानम् — परमचीरम् is out, चीर there being no standard of comparison'),
    ),
    '6.2.128': (
        _c('गुडपललम् (guḍapalalam) — sesame paste mixed with molasses',
           {'uttarapada': 'palala', 'samasa': 'tatpuruṣa', 'result': 'miśra'},
           note='पललसूपशाकं मिश्रे — भक्ष्येण मिश्रीकरणम्, the compound of a food with what it is mixed into'),
    ),
    '6.2.129': (
        _c("दाक्षिकूलम् (dākṣikūlam) — Dākṣi's Bank, the name of a village",
           {'uttarapada': 'kūla', 'samasa': 'tatpuruṣa', 'result': 'saṃjñā'},
           note='कूलसूदस्थलकर्षाः संज्ञायाम् — and स्थल names स्थली too, लिङ्गविशिष्टत्वात्'),
    ),
    '6.2.130': (
        _c('ब्राह्मणराज्यम् (brāhmaṇarājyam) — rule by brahmins, no कर्मधारय',
           {'uttarapada': 'rājya', 'samasa': 'tatpuruṣa'},
           note='अकर्मधारये राज्यम् — and कुराज्यम् goes to 6.2.2 instead, पूर्वविप्रतिषेधेन'),
    ),
    '6.2.131': (
        _c("वासुदेववर्ग्यः (vāsudevavargyaḥ) — one of Vāsudeva's party",
           {'gana': 'vargyādi', 'samasa': 'tatpuruṣa'},
           note="वर्ग्यादयश्च — the gaṇa is दिगादि's members with यत् on them, and is listed nowhere else"),
    ),
    '6.2.132': (
        _c("कौनटिपुत्रः (kaunaṭiputraḥ) — Kaunaṭi's son, named for the father",
           {'uttarapada': 'putra', 'purvapada_gana': 'puṃs', 'samasa': 'tatpuruṣa'},
           note='पुत्रः पुम्भ्यः — गार्गीपुत्रः, named for the mother, keeps the end-accent 6.1.223 gave'),
    ),
    '6.2.133': (
        _c("आचार्यपुत्रः (ācāryaputraḥ) — a teacher's son, and 6.2.132 refused",
           {'uttarapada': 'putra', 'purvapada_gana': 'ācārya-ādi-ākhyā', 'samasa': 'tatpuruṣa'},
           note='न आचार्यराजर्त्विक्संयुक्तज्ञात्याख्येभ्यः — the accent stays at the end, where 6.1.223 put it'),
    ),
    '6.2.134': (
        _c('मुद्गचूर्णम् (mudgacūrṇam) — bean flour, from a non-living genitive',
           {'gana': 'cūrṇādi', 'purvapada_gana': 'aprāṇin', 'samasa': 'tatpuruṣa', 'case': 'ṣaṣṭhī'},
           note='चूर्णादीन्यप्राणिषष्ठ्याः — and the sūtra has a second reading in उपग्रह, the older word for the genitive'),
    ),
    '6.2.135': (
        _c('दर्भकाण्डम् (darbhakāṇḍam) — a stalk of darbha, no contempt meant',
           {'uttarapada': 'kāṇḍa', 'purvapada_gana': 'aprāṇin', 'samasa': 'tatpuruṣa', 'case': 'ṣaṣṭhī'},
           note='षट् च काण्डादीनि — four rules widened at the price of one new condition, a non-living genitive'),
    ),
    '6.2.136': (
        _c('दर्भकुण्डम् (darbhakuṇḍam) — a thicket of darbha grass',
           {'uttarapada': 'kuṇḍa', 'samasa': 'tatpuruṣa', 'result': 'vana'},
           note='कुण्डं वनम् — मृत्कुण्डम् is out, being a pot; and 6.2.137 then replaces the word आदिः'),
    ),
    '6.2.137': (
        _c('कुम्भीभगालम् (kumbhībhagālam) — a potsherd skull, accented in the middle',
           {'uttarapada': 'bhagāla', 'samasa': 'tatpuruṣa'},
           note='प्रकृत्या भगालम् — भगालादयो मध्योदात्ताः, and प्रकृत्या then runs on to 6.2.142'),
    ),
    '6.2.138': (
        _c('शितिपादः (śitipādaḥ) — white-footed, and पाद keeps its own accent',
           {'purvapada': 'śiti', 'samasa': 'bahuvrīhi', 'result': 'nitya-abahvac'},
           note='शितेर्नित्याबह्वज्बहुव्रीहावभसत् — नित्यम् shuts out ककुत्, which is short-voweled only after 5.4.146'),
    ),
    '6.2.139': (
        _c('प्रकारकः (prakārakaḥ) — the doer, and the कृदन्त keeps its own accent',
           {'affix': 'kṛt', 'purvapada_gana': 'gati', 'samasa': 'tatpuruṣa'},
           note='गतिकारकोपपदात् कृत् — the उत्तरपदप्रकृतिस्वर, which 6.2.144 is built to override'),
    ),
    '6.2.140': (
        _c('वनस्पतिः (vanaspatiḥ) — lord of the wood, with two accents at once',
           {'gana': 'vanaspatyādi'},
           note="उभे वनस्पत्यादिषु युगपत् — and the स् comes from 6.1.157's पारस्करप्रभृति list"),
    ),
    '6.2.141': (
        _c('इन्द्राबृहस्पती (indrābṛhaspatī) — three उदात्तs in one word',
           {'samasa': 'devatā-dvandva'},
           note='देवताद्वन्द्वे च — त्रय उदात्ता भवन्ति, and nowhere else does one word end with three'),
    ),
    '6.2.142': (
        _c('इन्द्राग्नी (indrāgnī) — अग्नि begins low, so 6.2.141 is refused',
           {'samasa': 'devatā-dvandva', 'result': 'anudāttādi'},
           note='न उत्तरपदेऽनुदात्तादावपृथिवीरुद्रपूषमन्थिषु — उत्तरपदग्रहणम् fixes whose first syllable is meant'),
    ),
    '6.2.143': (
        _c("सुनीथः (sunīthaḥ) — the heading's own example, at 6.2.144",
           {'affix': 'tha', 'purvapada_gana': 'gati'},
           note='अन्तः — वक्ष्यति थाथघञ्क्ताजबित्रकाणाम् इति, which the vṛtti reads out as the example'),
    ),
    '6.2.144': (
        _c('सुनीथः (sunīthaḥ) — well led, a थ-ending second member',
           {'affix': 'tha', 'purvapada_gana': 'gati'},
           note='थाथघञ्क्ताजबित्रकाणाम् — it exists only to undo 6.2.139, five sūtras back'),
    ),
    '6.2.145': (
        _c('सुकृतम् (sukṛtam) — well done, after सु',
           {'affix': 'kta', 'purvapada': 'su'},
           note='सूपमानात् क्तः — one sūtra and two अपवादs, displacing 6.2.49 after सु and 6.2.48 after a likeness'),
    ),
    '6.2.146': (
        _c('संभूतः (saṃbhūtaḥ) — a man called by what befell him',
           {'affix': 'kta', 'purvapada_gana': 'gati', 'result': 'saṃjñā'},
           note='संज्ञायामनाचितादीनाम् — it displaces 6.2.49 for the one half and 6.2.48 for the other'),
    ),
    '6.2.147': (
        _c('प्रवृद्धम् (pravṛddham) — grown large, first of the प्रवृद्धादि',
           {'gana': 'pravṛddhādi'},
           note='प्रवृद्धादीनां च — असंज्ञार्थोऽयमारम्भः, for where 6.2.146 does not reach; and the gaṇa is आकृतिगण'),
    ),
    '6.2.148': (
        _c('देवदत्तः (devadattaḥ) — may the gods grant him, a name and a blessing',
           {'uttarapada': 'datta', 'purvapada_gana': 'kāraka', 'result': 'āśis'},
           note='कारकाद् दत्तश्रुतयोरेवाशिषि — the एव restricts the source and not the pair, and it shuts 6.2.146 off'),
    ),
    '6.2.149': (
        _c('सुप्तप्रलपितम् (suptapralapitam) — babbling done by a sleeper',
           {'affix': 'kta', 'result': 'itthaṃbhūtena-kṛta'},
           note='इत्थंभूतेन कृतम् इति च — कृतम् is any action at all, else babbling would not count as done'),
    ),
    '6.2.150': (
        _c('ओदनभोजनम् (odanabhojanam) — the eating of rice, an act named',
           {'affix': 'ana', 'purvapada_gana': 'kāraka', 'result': 'bhāva'},
           note='अनो भावकर्मवचनः — the two senses come from the two readings the vṛtti gives 3.3.116'),
    ),
    '6.2.151': (
        _c('ऋगयनव्याख्यानम् (ṛgayanavyākhyānam) — an exposition of the Ṛgayana',
           {'uttarapada': 'vyākhyāna'},
           note='मन्क्तिन्व्याख्यानशयनासनस्थानयाजकादिक्रीताः — two affixes, four words and a gaṇa, any of which does'),
    ),
    '6.2.152': (
        _c('अध्ययनपुण्यम् (adhyayanapuṇyam) — merit in study, a locative compound',
           {'uttarapada': 'puṇya', 'case': 'saptamī'},
           note="सप्तम्याः पुण्यम् — without it 6.2.2 would have kept the first member's accent"),
    ),
    '6.2.153': (
        _c('माषोनम् (māṣonam) — short by a bean, after an instrumental',
           {'uttarapada': 'kalaha', 'case': 'tṛtīyā'},
           note="ऊनार्थकलहं तृतीयायाः — an अपवाद of the तृतीया rule that keeps the first member's accent"),
    ),
    '6.2.154': (
        _c('गुडमिश्राः (guḍamiśrāḥ) — mixed with molasses, no alliance meant',
           {'uttarapada': 'miśra', 'case': 'tṛtīyā', 'result': 'asandhi'},
           note='मिश्रं च अनुपसर्गम् असंधौ — and saying अनुपसर्गम् here shows that 2.1.31 does not exclude one'),
    ),
    '6.2.155': (
        _c('अच्छैदिकः (acchaidikaḥ) — not deserving to be cut',
           {'affix': 'taddhita', 'purvapada': 'nañ', 'result': 'guṇapratiṣedha'},
           note='नञो गुणप्रतिषेधे संपाद्यर्हहितालमर्थास्तद्धिताः — four taddhita senses, all after a नञ् denying a quality'),
    ),
    '6.2.156': (
        _c('अदन्त्यम् (adantyam) — not of the teeth, a यत्-formed word',
           {'affix': 'ya', 'purvapada': 'nañ', 'result': 'atadartha'},
           note='ययतोश्च अतदर्थे — only the bare affixes, निरनुबन्धकैकानुबन्धकयोर्ग्रहणात्'),
    ),
    '6.2.157': (
        _c('अपचः (apacaḥ) — one who cannot cook, inability meant',
           {'affix': 'ac', 'purvapada': 'nañ', 'result': 'aśakti'},
           note='अच्कावशक्तौ — अपचो दीक्षितः is out, where the man does not cook by vow and not from inability'),
    ),
    '6.2.158': (
        _c("अपचोऽयं जाल्मः (apaco'yaṃ jālmaḥ) — abuse, not inability",
           {'affix': 'ac', 'purvapada': 'nañ', 'result': 'ākrośa'},
           note='आक्रोशे च — पक्तुं पठितुं शक्तोऽप्येवमाक्रुश्यते, he can do it and is abused all the same'),
    ),
    '6.2.159': (
        _c('अदेवदत्तः (adevadattaḥ) — a worthless Devadatta, abuse in a name',
           {'purvapada': 'nañ', 'result': 'saṃjñā'},
           note='संज्ञायाम् — the sūtra names no affix, so any second member is reached'),
    ),
    '6.2.160': (
        _c('अचारुः (acāruḥ) — not lovely, first of the चार्वादि',
           {'gana': 'cārvādi', 'purvapada': 'nañ'},
           note='कृत्युकेष्णुच्चार्वादयश्च — and naming इष्णुच् reaches खिष्णुच् too, विधानसामर्थ्यात्'),
    ),
    '6.2.161': (
        _c('अनन्नम् (anannam) — not food, optionally end-accented',
           {'uttarapada': 'anna', 'purvapada': 'nañ'},
           note='विभाषा तृन्नन्नतीक्ष्णशुचिषु — पक्षेऽव्ययस्वर एव भवति, नञ् being an indeclinable'),
    ),
    '6.2.162': (
        _c('इदंप्रथमः (idaṃprathamaḥ) — one for whom this is a first going',
           {'uttarapada': 'prathama', 'purvapada': 'idam', 'samasa': 'bahuvrīhi', 'result': 'kriyāgaṇana'},
           note='बहुव्रीहाविदमेतत्तद्भ्यः प्रथमपूरणयोः क्रियागणने — यत्प्रथमः is out, यद् being none of the three'),
    ),
    '6.2.163': (
        _c('द्विस्तना (dvistanā) — two-uddered, after a numeral',
           {'uttarapada': 'stana', 'purvapada_gana': 'saṅkhyā', 'samasa': 'bahuvrīhi'},
           note='संख्यायाः स्तनः — दर्शनीयस्तना is out, दर्शनीय being no numeral'),
    ),
    '6.2.164': (
        _c('द्विस्तनाम् (dvistanām) — accented both ways in one passage',
           {'uttarapada': 'stana', 'purvapada_gana': 'saṅkhyā', 'samasa': 'bahuvrīhi', 'chandasi': True},
           note='विभाषा — द्विस्तनां करोति द्यावापृथिव्योर्दोहाय, and the option is exercised in the Veda itself'),
    ),
    '6.2.165': (
        _c('देवमित्रः (devamitraḥ) — Devamitra, a name in मित्र',
           {'uttarapada': 'mitra', 'samasa': 'bahuvrīhi', 'result': 'saṃjñā'},
           note="संज्ञायां मित्राजिनयोः — and ऋषिप्रतिषेधो मित्रे keeps a seer's name out however much a name it is"),
    ),
    '6.2.166': (
        _c('वस्त्रान्तरः (vastrāntaraḥ) — one with a cloth in between',
           {'uttarapada': 'antara', 'purvapada_gana': 'vyavāyin', 'samasa': 'bahuvrīhi'},
           note='व्यवायिनोऽन्तरम् — आत्मान्तरः is out, अन्तर there meaning other and nothing standing between'),
    ),
    '6.2.167': (
        _c('गौरमुखः (gauramukhaḥ) — fair-faced, मुख a part of the body',
           {'uttarapada': 'mukha', 'samasa': 'bahuvrīhi', 'result': 'svāṅga'},
           note='मुखं स्वाङ्गम् — and स्वाङ्ग is the technical sense, स्वाङ्गम् अद्रवादिलक्षणम् इह गृह्यते'),
    ),
    '6.2.168': (
        _c('उच्चैर्मुखः (uccairmukhaḥ) — face upturned, and 6.2.167 refused',
           {'uttarapada': 'mukha', 'purvapada': 'avyaya', 'samasa': 'bahuvrīhi'},
           note='न अव्ययदिक्शब्दगोमहत्स्थूलमुष्टिपृथुवत्सेभ्यः — पूर्वपदप्रकृतिस्वरो यथायोगम् एषु भवति'),
    ),
    '6.2.169': (
        _c('सिंहमुखः (siṃhamukhaḥ) — lion-faced, optionally end-accented',
           {'uttarapada': 'mukha', 'purvapada_gana': 'niṣṭhā', 'samasa': 'bahuvrīhi'},
           note="निष्ठोपमानादन्यतरस्याम् — with 6.2.110's option beside it, प्रक्षालितमुखः has three readings"),
    ),
    '6.2.170': (
        _c('सारङ्गजग्धः (sāraṅgajagdhaḥ) — one who has eaten venison',
           {'affix': 'kta', 'purvapada_gana': 'jāti', 'samasa': 'bahuvrīhi'},
           note='जातिकालसुखादिभ्योऽनाच्छादनात् क्तोऽकृतमितप्रतिपन्नाः — वस्त्रच्छन्नः is out, clothing being excepted'),
    ),
    '6.2.171': (
        _c('दन्तजातः (dantajātaḥ) — one whose teeth have already come through',
           {'uttarapada': 'jāta', 'purvapada_gana': 'jāti', 'samasa': 'bahuvrīhi'},
           note='वा जाते — the same three first members as 6.2.170, and the accent now optional'),
    ),
    '6.2.172': (
        _c('अयवः (ayavaḥ) — having no barley, after नञ्',
           {'purvapada': 'nañ', 'samasa': 'bahuvrīhi'},
           note='नञ्सुभ्याम् — and where a समासान्त has been added the accent falls at the end of THAT'),
    ),
    '6.2.173': (
        _c('अकुमारीकः (akumārīkaḥ) — the accent before the कप्, not on it',
           {'affix': 'kap', 'purvapada': 'nañ', 'samasa': 'bahuvrīhi'},
           note='कपि पूर्वम् — कपि तु परत्वात्, so it takes सुकर्मा back from 6.2.117 by standing later'),
    ),
    '6.2.174': (
        _c('अयवकः (ayavakaḥ) — the accent one syllable further back still',
           {'affix': 'kap', 'purvapada': 'nañ', 'samasa': 'bahuvrīhi', 'result': 'hrasvānta'},
           note='ह्रस्वान्तेऽन्त्यात् पूर्वम् — the repeated पूर्वम् shuts 6.2.173 out wherever this rule applies'),
    ),
    '6.2.175': (
        _c('बहुयवः (bahuyavaḥ) — having much barley, बहु read as a नञ्',
           {'purvapada': 'bahu', 'result': 'uttarapada-bhūman'},
           note='बहोर्नञ्वद् उत्तरपदभूम्नि — 6.2.172, 6.2.173, 6.2.174 and 6.2.116 all follow at once'),
    ),
    '6.2.176': (
        _c('बहुगुणा रज्जुः (bahuguṇā rajjuḥ) — a rope of many strands',
           {'gana': 'guṇādi', 'purvapada': 'bahu', 'result': 'avayava'},
           note='न गुणादयोऽवयवाः — बहुगुणो ब्राह्मणः keeps 6.2.175, learning being a quality and no part'),
    ),
    '6.2.177': (
        _c('प्रपृष्ठः (prapṛṣṭhaḥ) — back permanently thrust forward',
           {'purvapada_gana': 'upasarga', 'samasa': 'bahuvrīhi', 'result': 'svāṅga'},
           note='उपसर्गात् स्वाङ्गं ध्रुवम् अपर्शु — उद्बाहुः क्रोशति is out, the arms being raised only for the moment'),
    ),
    '6.2.178': (
        _c('प्रवणम् (pravaṇam) — a slope, and any compound will do',
           {'uttarapada': 'vana', 'purvapada_gana': 'upasarga'},
           note='वनं समासे — समासग्रहणं समासमात्रपरिग्रहार्थम्, बहुव्रीहावेव हि स्यात्'),
    ),
    '6.2.179': (
        _c('अन्तर्वणः (antarvaṇaḥ) — a place within the wood',
           {'uttarapada': 'vana', 'purvapada': 'antar'},
           note='अन्तः — अनुपसर्गार्थ आरम्भः, अन्तर् being no उपसर्ग for 6.2.178 to work on'),
    ),
    '6.2.180': (
        _c('प्रान्तः (prāntaḥ) — the far edge, अन्तर् itself end-accented',
           {'uttarapada': 'antar', 'purvapada_gana': 'upasarga'},
           note='अन्तश्च — बहुव्रीहिरयं प्रादिसमासो वा, and the vṛtti does not choose between them'),
    ),
    '6.2.181': (
        _c('न्यन्तः (nyantaḥ) — 6.2.180 refused, and a स्वरित left behind',
           {'uttarapada': 'antar', 'purvapada': 'ni'},
           note='न निविभ्याम् — उदात्तस्वरितयोर्यणः स्वरितोऽनुदात्तस्य, so a third kind of accent appears'),
    ),
    '6.2.182': (
        _c('परिमण्डलम् (parimaṇḍalam) — round about, and 6.2.33 overridden',
           {'uttarapada': 'maṇḍala', 'purvapada': 'pari', 'result': 'abhitobhāvin'},
           note='परेरभितोभावि मण्डलम् — अभित इत्युभयतः, and the compound may be read three ways'),
    ),
    '6.2.183': (
        _c('प्रगृहम् (pragṛham) — the front room, a name',
           {'purvapada': 'pra', 'result': 'saṃjñā'},
           note='प्राद् अस्वाङ्गं संज्ञायाम् — प्रहस्तम् and प्रपदम् are out, being parts of the body'),
    ),
    '6.2.184': (
        _c('निरुदकम् (nirudakam) — waterless, first of the निरुदकादि',
           {'gana': 'nirudakādi'},
           note="निरुदकादीनि च — शब्दरूपाणि, whole compounds; and each one's analysis is left open"),
    ),
    '6.2.185': (
        _c('अभिमुखा शाला (abhimukhā śālā) — a hall that faces one',
           {'uttarapada': 'mukha', 'purvapada': 'abhi'},
           note='अभेर्मुखम् — वचनम् अबहुव्रीह्यर्थम् अध्रुवार्थम् अस्वाङ्गार्थं च, three reasons for a rule already had'),
    ),
    '6.2.186': (
        _c('अपमुखः (apamukhaḥ) — face turned away, after अप',
           {'uttarapada': 'mukha', 'purvapada': 'apa'},
           note='अपाच्च — योगविभाग उत्तरार्थः, split off so that अप carries into 6.2.187'),
    ),
    '6.2.187': (
        _c('अपस्फिगम् (apasphigam) — away from the hip, after अप',
           {'uttarapada': 'sphij', 'purvapada': 'apa'},
           note='स्फिगपूतवीणाञ्जोऽध्वकुक्षिसीरनामनामानि च — naming अध्वन् shows the समासान्त is not compulsory'),
    ),
    '6.2.188': (
        _c('अधिदन्तः (adhidantaḥ) — a tooth grown over a tooth',
           {'purvapada': 'adhi', 'result': 'uparistha'},
           note='अधेरुपरिस्थम् — अधिकरणम् is out, करण standing above nothing'),
    ),
    '6.2.189': (
        _c('अनुकनीयान् (anukanīyān) — the younger, named because it IS principal',
           {'uttarapada': 'kanīyas', 'purvapada': 'anu', 'result': 'apradhāna'},
           note='अनोरप्रधानकनीयसी — प्रधानार्थं च कनीयोग्रहणम्, since अप्रधान would have shut it out'),
    ),
    '6.2.190': (
        _c('अनुपुरुषः (anupuruṣaḥ) — the man spoken of afterwards',
           {'uttarapada': 'puruṣa', 'purvapada': 'anu', 'result': 'anvādiṣṭa'},
           note='पुरुषश्चान्वादिष्टः — अन्वादिष्टोऽन्वाचितः कथितानुकथितो वा, the vṛtti glossing the sense three ways'),
    ),
    '6.2.191': (
        _c('अत्यङ्कुशः (atyaṅkuśaḥ) — an elephant past the goad',
           {'purvapada': 'ati'},
           note='अतेरकृत्पदे — and a vārttika adds अतेर्धातुलोप इति वक्तव्यम्, a verb having to have dropped out'),
    ),
    '6.2.192': (
        _c('निमूलम् (nimūlam) — down to the root, no concealment meant',
           {'purvapada': 'ni'},
           note='नेरनिधाने — प्रादयो हि वृत्तिविषये ससाधनां क्रियाम् आहुः, which is how नि can mean laid away'),
    ),
    '6.2.193': (
        _c('प्रत्यंशुः (pratyaṃśuḥ) — a counter-ray, first of the अंश्वादि',
           {'gana': 'aṃśvādi', 'purvapada': 'prati', 'samasa': 'tatpuruṣa'},
           note='प्रतेरंश्वादयस्तत्पुरुषे — राजन् is in the list for where the समासान्त टच् fails to appear'),
    ),
    '6.2.194': (
        _c('उपदेवः (upadevaḥ) — near the god, a two-voweled second member',
           {'uttarapada': 'ajina', 'purvapada': 'upa', 'samasa': 'tatpuruṣa', 'result': 'dvyac'},
           note='उपाद् द्व्यजजिनमगौरादयः — उपगौरः is out, गौर standing in the गौरादि list'),
    ),
    '6.2.195': (
        _c('सुप्रत्यवसितः (supratyavasitaḥ) — a fine feeder, said with scorn',
           {'purvapada': 'su', 'samasa': 'tatpuruṣa', 'result': 'avakṣepaṇa'},
           note='सोरवक्षेपणे — सुशब्दोऽत्र पूजायामेव, the scorn lying in the sentence and not in the word'),
    ),
    '6.2.196': (
        _c('उत्पुच्छः (utpucchaḥ) — tail lifted, and the option works both ways',
           {'uttarapada': 'utpuccha', 'samasa': 'tatpuruṣa'},
           note='विभाषोत्पुच्छे — सेयम् उभयत्रविभाषा भवति, granting on one reading and withdrawing on the other'),
    ),
    '6.2.197': (
        _c('द्विपात् (dvipāt) — two-footed, optionally end-accented',
           {'uttarapada': 'pād', 'purvapada': 'dvi', 'samasa': 'bahuvrīhi'},
           note='द्वित्रिभ्यां पाद्दन्मूर्धसु बहुव्रीहौ — each of the three named at a different point in the derivation'),
    ),
    '6.2.198': (
        _c('गौरसक्थः (gaurasakthaḥ) — fair-thighed, optionally end-accented',
           {'uttarapada': 'saktha'},
           note='सक्थं च अक्रान्तात् — सक्थम् इति कृतसमासान्तः सक्थिशब्दोऽत्र गृह्यते, the word taken after its समासान्त'),
    ),
    '6.2.199': (
        _c('अञ्जिसक्थम् (añjisaktham) — the accent on the following word',
           {'chandasi': True},
           note='परादिश्छन्दसि बहुलम् — परादिश्च परान्तश्च पूर्वान्तश्चापि दृश्यते, व्यत्ययो बहुलं ततः'),
    ),
    '6.3.1': (
        _c("स्तोकान्मुक्तः (stokānmuktaḥ) — the heading's own example, at 6.3.2",
           {'gana': 'stokādi'},
           note='अलुगुत्तरपदे — अलुगधिकारः प्रागानङः, उत्तरपदाधिकारः प्रागङ्गाधिकारात्, both bounds in one line'),
    ),
    '6.3.2': (
        _c('दूरादागतः (dūrādāgataḥ) — come from far off, the ablative kept',
           {'gana': 'stokādi'},
           note='पञ्चम्याः स्तोकादिभ्यः — and the dual and plural form no compound at all, अनभिधानात्'),
    ),
    '6.3.3': (
        _c('ओजसाकृतम् (ojasākṛtam) — done by sheer force',
           {'purvapada': 'ojas'},
           note='ओजःसहोऽम्भस्तमसस्तृतीयायाः — and a second vārttika adds two whole compounds, पुंसानुजः and जनुषान्धः'),
    ),
    '6.3.4': (
        _c("मनसादत्ता (manasādattā) — Manasādattā, a woman's name",
           {'purvapada': 'manas', 'result': 'saṃjñā'},
           note='मनसः संज्ञायाम् — मनोदत्ता, the same words not used as a name, drops the ending'),
    ),
    '6.3.5': (
        _c('मनसाज्ञायी (manasājñāyī) — understanding by the mind alone',
           {'purvapada': 'manas', 'uttarapada': 'ājñāyin'},
           note='आज्ञायिनि च — मनसा आज्ञातुं शीलमस्य, and no संज्ञा is required here'),
    ),
    '6.3.6': (
        _c('आत्मनापञ्चमः (ātmanāpañcamaḥ) — himself making the fifth',
           {'purvapada': 'ātman', 'uttarapada_gana': 'pūraṇa'},
           note='आत्मनश्च पूरणे — and आत्मचतुर्थः is a बहुव्रीहि instead, with no instrumental to keep'),
    ),
    '6.3.7': (
        _c("आत्मनेपदम् (ātmanepadam) — the ātmanepada, a grammarians' term",
           {'purvapada': 'ātman', 'result': 'vaiyākaraṇākhyā'},
           note='वैयाकरणाख्यायां चतुर्थ्याः — the dative is तादर्थ्ये चतुर्थी and the compound is by योगविभाग'),
    ),
    '6.3.8': (
        _c('परस्मैपदम् (parasmaipadam) — the parasmaipada, the other half',
           {'purvapada': 'para', 'result': 'vaiyākaraṇākhyā'},
           note="परस्य च — the second of two sūtras naming one pair of grammarians' terms"),
    ),
    '6.3.9': (
        _c('युधिष्ठिरः (yudhiṣṭhiraḥ) — steady in battle, a name',
           {'gana': 'hal-adanta', 'result': 'saṃjñā'},
           note='हलदन्तात् सप्तम्याः संज्ञायाम् — but गविष्ठिरः is kept by 8.3.95 naming it, गो ending in neither'),
    ),
    '6.3.10': (
        _c('स्तूपेशाणः (stūpeśāṇaḥ) — a śāṇa due at the mound',
           {'gana': 'hal-adanta', 'result': 'kāranāman'},
           note='कारनाम्नि च प्राचां हलादौ — पूर्वेणैव सिद्धे नियमार्थम्, three restrictions from one sūtra'),
    ),
    '6.3.11': (
        _c('मध्येगुरुः (madhyeguruḥ) — a foot heavy in the middle',
           {'purvapada': 'madhya', 'uttarapada': 'guru'},
           note='मध्याद्गुरौ — and अन्ताच्चेति वक्तव्यम् adds अन्तेगुरुः, heavy at the end'),
    ),
    '6.3.12': (
        _c('कण्ठेकालः (kaṇṭhekālaḥ) — one with the mark on his throat',
           {'gana': 'svāṅga'},
           note='अमूर्धमस्तकात् स्वाङ्गादकामे — and हलदन्तात् still runs, which keeps अङ्गुलित्राणः out'),
    ),
    '6.3.13': (
        _c('हस्तेबन्धः (hastebandhaḥ) — bound at the hand, optionally so written',
           {'uttarapada': 'bandha'},
           note='बन्धे च विभाषा — उभयत्रविभाषेयम्, granting in a तत्पुरुष and withdrawing in a बहुव्रीहि'),
    ),
    '6.3.14': (
        _c('कर्णेजपः (karṇejapaḥ) — a whisperer in the ear, a talebearer',
           {'uttarapada_gana': 'kṛt', 'samasa': 'tatpuruṣa'},
           note='तत्पुरुषे कृति बहुलम् — बहुलम् states that both happen, without saying which word takes which'),
    ),
    '6.3.15': (
        _c('दिविजः (divijaḥ) — heaven-born, the locative kept',
           {'purvapada': 'prāvṛṣ', 'uttarapada': 'ja'},
           note='प्रावृट्शरत्कालदिवां जे — पूर्वस्यैवायं प्रपञ्चः, the vṛtti calling it a spelling-out of 6.3.14'),
    ),
    '6.3.16': (
        _c('वर्षेजः (varṣejaḥ) — rain-born, and वर्षजः beside it',
           {'purvapada': 'varṣa', 'uttarapada': 'ja'},
           note='विभाषा — a sūtra of one word, taking ज and the locative from the rule before it'),
    ),
    '6.3.17': (
        _c('पूर्वाह्णेतरे (pūrvāhṇetare) — earlier in the forenoon',
           {'gana': 'kālanāman', 'uttarapada': 'kāla'},
           note='घकालतनेषु कालनाम्नः — and under उत्तरपद, naming an affix does not reach a stem ending in it'),
    ),
    '6.3.18': (
        _c('खेशयः (kheśayaḥ) — lying out under the sky',
           {'uttarapada': 'śaya'},
           note='शयवासवासिष्वकालात् — and a vārttika adds अप्सुयोनिः, अप्सव्यः, अप्सुमन्तौ'),
    ),
    '6.3.19': (
        _c('चक्रबद्धः (cakrabaddhaḥ) — bound to a wheel, and 6.3.14 refused',
           {'uttarapada': 'siddha'},
           note='नेन्सिद्धबध्नातिषु च — each of its examples a कृदन्त that 6.3.14 would otherwise have reached'),
    ),
    '6.3.20': (
        _c('कूटस्थः (kūṭasthaḥ) — standing at the summit, unchanging',
           {'uttarapada': 'stha', 'result': 'bhāṣā'},
           note='स्थे च भाषायाम् — naming the register is what leaves the Vedic आखरेष्ठः alone'),
    ),
    '6.3.21': (
        _c("चौरस्यकुलम् (caurasyakulam) — a thief's family, said in contempt",
           {'result': 'ākrośa'},
           note='षष्ठ्या आक्रोशे — and the vārttikas add वाचोयुक्तिः, पश्यतोहरः, देवानांप्रियः, शुनःशेपः, दिवोदासः'),
    ),
    '6.3.22': (
        _c('दास्याःपुत्रः (dāsyāḥputraḥ) — son of a slave woman, said in scorn',
           {'uttarapada': 'putra', 'result': 'ākrośa'},
           note='पुत्रेऽन्यतरस्याम् — आक्रोश is still running, so ब्राह्मणीपुत्रः gets no option'),
    ),
    '6.3.23': (
        _c("पितुःपुत्रः (pituḥputraḥ) — the father's son, a relation of birth",
           {'gana': 'ṛd-anta-vidyā-yoni', 'uttarapada_gana': 'vidyā-yoni-sambandha'},
           note='ऋतो विद्यायोनिसम्बन्धेभ्यः — होतृधनम् is out, money being no relation of learning'),
    ),
    '6.3.24': (
        _c("मातुःष्वसा (mātuḥṣvasā) — the mother's sister, the ending kept",
           {'gana': 'ṛd-anta-vidyā-yoni', 'uttarapada': 'svasṛ'},
           note='विभाषा स्वसृपत्योः — drop it and 8.3.84 gives ष् always; keep it and 8.3.85 gives ष् only optionally'),
    ),
    '6.3.25': (
        _c('होतापोतारौ (hotāpotārau) — the Hotṛ and the Potṛ, two priests',
           {'gana': 'ṛd-anta-vidyā-yoni', 'dvandva': 'ṛd-anta'},
           note='आनङ् ऋतो द्वन्द्वे — and पुत्र carries down from 6.3.22, so पितापुत्रौ goes the same way'),
    ),
    '6.3.26': (
        _c('इन्द्रावरुणौ (indrāvaruṇau) — Indra and Varuṇa, a settled pair',
           {'dvandva': 'devatā'},
           note='देवताद्वन्द्वे च — प्रसिद्धसाहचर्यार्थम्, and a vārttika keeps वायु out in either order'),
    ),
    '6.3.27': (
        _c('अग्नीषोमौ (agnīṣomau) — Agni and Soma, the ī displacing आनङ्',
           {'purvapada': 'agni', 'uttarapada': 'soma', 'dvandva': 'devatā'},
           note='ईदग्नेः सोमवरुणयोः — अग्नेःस्तुत्स्तोमसोमाः इति षत्वम् gives the ष्'),
    ),
    '6.3.28': (
        _c('आग्निवारुणी (āgnivāruṇī) — of Agni and Varuṇa, वृद्धि already made',
           {'purvapada': 'agni', 'dvandva': 'devatā', 'result': 'vṛddhi'},
           note='इद् वृद्धौ — आनङम् ईत्वं च बाधितुम् इकारः क्रियते, a substitute that arrives last'),
    ),
    '6.3.29': (
        _c('द्यावाभूमी (dyāvābhūmī) — Heaven and Earth, दिव् replaced whole',
           {'purvapada': 'div', 'dvandva': 'devatā'},
           note='देवो द्यावा — दिवित्येतस्य द्यावा इत्ययमादेशो भवति, the vṛtti reading देवः as दिव्'),
    ),
    '6.3.30': (
        _c('दिवस्पृथिव्यौ (divaspṛthivyau) — Heaven and Earth, the other form',
           {'purvapada': 'div', 'uttarapada': 'pṛthivī', 'dvandva': 'devatā'},
           note='दिवसश्च पृथिव्याम् — the अ is written so the स् is not the kind 8.2.66 turns to रु'),
    ),
    '6.3.31': (
        _c('उषासानक्ता (uṣāsānaktā) — Dawn and Night, a Vedic pair',
           {'purvapada': 'uṣas', 'dvandva': 'devatā'},
           note='उषासोषसः — one stem, one substitute, and the द्वन्द्व of gods still running'),
    ),
    '6.3.32': (
        _c('मातरपितरौ (mātarapitarau) — mother and father, as the north says it',
           {'purvapada': 'mātṛ', 'uttarapada': 'pitṛ', 'result': 'udīcām'},
           note='मातरपितरावुदीचाम् — निपात्यते, laid down whole and credited to a school by name'),
    ),
    '6.3.33': (
        _c('पितरामातरा (pitarāmātarā) — father and mother, the Vedic order',
           {'purvapada': 'pitṛ', 'uttarapada': 'mātṛ', 'chandasi': True},
           note='पितरामातरा च छन्दसि — half a निपातन and half a derivation, in one word'),
    ),
    '6.3.34': (
        _c('दर्शनीयभार्यः (darśanīyabhāryaḥ) — the man whose wife is good-looking',
           {'stem': 'bhāṣitapuṃska-anūṅ', 'result': 'samānādhikaraṇa'},
           note='स्त्रियाः पुंवद्भाषितपुंस्कादनूङ् समानाधिकरणे स्त्रियामपूरणीप्रियादिषु — खट्वाभार्यः is out, खट्वा having no masculine of the same sense'),
    ),
    '6.3.35': (
        _c('ततः (tataḥ) — from her, the feminine gone from the form',
           {'stem': 'bhāṣitapuṃska-anūṅ', 'before': 'tral'},
           note='तसिलादिष्वा कृत्वसुचः — तसिलादिषु परिगणनं कर्तव्यम्, and four more vārttikas add four more places'),
    ),
    '6.3.36': (
        _c('एतायते (etāyate) — she behaves like a doe, the ई gone',
           {'stem': 'bhāṣitapuṃska-anūṅ', 'before': 'kyaṅ'},
           note='क्यङ्मानिनोश्च — मानिनो ग्रहणमस्त्र्यर्थमसमानाधिकरणार्थं च'),
    ),
    '6.3.37': (
        _c('पाचिकाभार्यः (pācikābhāryaḥ) — a क before the ending, so no पुंवद्भाव',
           {'stem': 'kopadhā'},
           note='न कोपधायाः — कोपधप्रतिषेधे तद्धितवुग्रहणं कर्तव्यम्, so पाकभार्यः is not reached'),
    ),
    '6.3.38': (
        _c('दत्ताभार्यः (dattābhāryaḥ) — his wife is called Dattā, and the ā stays',
           {'stem': 'saṃjñā'},
           note='संज्ञापूरण्योश्च — a name and an ordinal, each refused through every environment'),
    ),
    '6.3.39': (
        _c('स्रौघ्नीभार्यः (sraughnībhāryaḥ) — his wife is from Srughna',
           {'stem': 'vṛddhi-nimitta-taddhita'},
           note='वृद्धिनिमित्तस्य च तद्धितस्यारक्तविकारे — and काषायी बृहतिका is out, the taddhita being for a dye'),
    ),
    '6.3.40': (
        _c('दीर्घकेशीभार्यः (dīrghakeśībhāryaḥ) — his wife is long-haired',
           {'stem': 'svāṅga-īkārānta'},
           note='स्वाङ्गाच्चेतोऽमानिनि — दीर्घकेशमानिनी does take it, मानिन् being excepted'),
    ),
    '6.3.41': (
        _c('कठीभार्यः (kaṭhībhāryaḥ) — his wife is of the Kaṭha school',
           {'stem': 'jāti'},
           note='जातेश्च — अयं प्रतिषेध औपसंख्यानिकस्य पुंवद्भावस्य नेष्यते, so हास्तिकम् stands'),
    ),
    '6.3.42': (
        _c('पाचकवृन्दारिका (pācakavṛndārikā) — an excellent cook, 6.3.37 undone',
           {'stem': 'kopadhā', 'before': 'karmadhāraya'},
           note='पुंवत् कर्मधारयजातीयदेशीयेषु — प्रतिषेधार्थोऽयमारम्भः, but भाषितपुंस्क and अनूङ् still hold'),
    ),
    '6.3.43': (
        _c('ब्राह्मणितरा (brāhmaṇitarā) — more of a brahmin woman, the ī short',
           {'stem': 'ṅī-anta-anekāc', 'before': 'gha'},
           note='घरूपकल्पचेलड्ब्रुवगोत्रमतहतेषु ङ्योऽनेकाचो ह्रस्वः — दत्तातरा is out, its ending not being ङी'),
    ),
    '6.3.44': (
        _c('ब्रह्मबन्धुतरा (brahmabandhutarā) — the shortening now optional',
           {'stem': 'nadī-śeṣa', 'before': 'gha'},
           note='नद्याः शेषस्यान्यतरस्याम् — कश्च शेषः? अङी च या नदी, ङ्यन्तं च यदेकाच्'),
    ),
    '6.3.45': (
        _c('श्रेयसितरा (śreyasitarā) — better, one of three attested forms',
           {'stem': 'ugit', 'before': 'gha'},
           note='उगितश्च — प्रकर्षयोगात् प्राक् स्त्रीत्वस्याविवक्षितत्वाद् वा सिद्धम्, for the third form'),
    ),
    '6.3.46': (
        _c('महादेवः (mahādevaḥ) — the great god, महत् in apposition',
           {'purvapada': 'mahat', 'before': 'samānādhikaraṇa'},
           note='आन्महतः समानाधिकरणजातीययोः — the condition is stated so that महाबाहुः is not lost with महत्पुत्रः'),
    ),
    '6.3.47': (
        _c('द्वादश (dvādaśa) — twelve, द्वि lengthened before a numeral',
           {'purvapada': 'dvi', 'uttarapada_gana': 'saṅkhyā'},
           note='द्व्यष्टनः संख्यायामबहुव्रीह्यशीत्योः — प्राक् शतादिति वक्तव्यम्, else द्विशतम् would go the same way'),
    ),
    '6.3.48': (
        _c('त्रयोदश (trayodaśa) — thirteen, त्रि replaced whole',
           {'purvapada': 'tri', 'uttarapada_gana': 'saṅkhyā'},
           note='त्रेस्त्रयः — त्रिदशाः is out as a बहुव्रीहि and त्र्यशीतिः as अशीति'),
    ),
    '6.3.49': (
        _c('द्वाचत्वारिंशत् (dvācatvāriṃśat) — forty-two, and द्विचत्वारिंशत् beside it',
           {'purvapada': 'dvi', 'uttarapada_gana': 'catvāriṃśat-prabhṛti'},
           note='विभाषा चत्वारिंशत्प्रभृतौ सर्वेषाम् — सर्वेषाम् gathers all three earlier rules under one option'),
    ),
    '6.3.50': (
        _c('हृल्लेखः (hṛllekhaḥ) — what scratches at the heart',
           {'purvapada': 'hṛdaya', 'before': 'lekha'},
           note='हृदयस्य हृल्लेखयदण्लासेषु — लेखग्रहणं ज्ञापकम्, that naming an affix here does not reach what ends in it'),
    ),
    '6.3.51': (
        _c('हृद्रोगः (hṛdrogaḥ) — heart disease, and हृदयरोगः beside it',
           {'purvapada': 'hṛdaya', 'before': 'śoka'},
           note='वा शोकष्यञ्रोगेषु — हृद् is an independent stem anyway, so the option is प्रपञ्चार्थम्'),
    ),
    '6.3.52': (
        _c('पदातिः (padātiḥ) — one who goes on foot, a foot-soldier',
           {'purvapada': 'pāda', 'before': 'āji'},
           note='पादस्य पदाज्यातिगोपहतेषु — and पद् is laid down end-accented, where पाद was accented on its first syllable'),
    ),
    '6.3.53': (
        _c('पद्याः शर्कराः (padyāḥ śarkarāḥ) — gravel that pricks the feet',
           {'purvapada': 'pāda', 'before': 'yat'},
           note="पद्यत्यतदर्थे — and only the limb is meant, so 5.1.34's पाद, a quarter, is untouched"),
    ),
    '6.3.54': (
        _c('पद्धतिः (paddhatiḥ) — a beaten track, a way of doing',
           {'purvapada': 'pāda', 'before': 'hima'},
           note='हिमकाषिहतिषु च — three more second members, and no sense-condition on any of them'),
    ),
    '6.3.55': (
        _c('पच्छो गायत्रीं शंसति (paccho gāyatrīṃ śaṃsati) — foot by foot',
           {'purvapada': 'pāda', 'before': 'śas', 'result': 'ṛc'},
           note="ऋचः शे — the शस् is 5.4.43's, संख्यैकवचनाच्च वीप्सायाम्"),
    ),
    '6.3.56': (
        _c('पद्घोषः (padghoṣaḥ) — the sound of footsteps, and पादघोषः beside it',
           {'purvapada': 'pāda', 'before': 'ghoṣa'},
           note='वा घोषमिश्रशब्देषु — निष्के चेति वक्तव्यम् adds पन्निष्कः beside पादनिष्कः'),
    ),
    '6.3.57': (
        _c("उदमेघः (udameghaḥ) — Udamegha, a man's name",
           {'purvapada': 'udaka', 'result': 'saṃjñā'},
           note='उदकस्योदः संज्ञायाम् — and a vārttika supplies the same substitute for उदक as second member'),
    ),
    '6.3.58': (
        _c('उदधिः (udadhiḥ) — the sea, where water is held',
           {'purvapada': 'udaka', 'before': 'peṣam'},
           note="पेषंवासवाहनधिषु च — the णमुल् of उदपेषम् is 3.4.38's, स्नेहने पिषः"),
    ),
    '6.3.59': (
        _c('उदकुम्भः (udakumbhaḥ) — a water-jar, one to be filled',
           {'purvapada': 'udaka', 'result': 'ekahalādi-pūrayitavya'},
           note='एकहलादौ पूरयितव्येऽन्यतरस्याम् — उदकस्थालम् is out, स्थ् being two consonants'),
    ),
    '6.3.60': (
        _c('उदबिन्दुः (udabinduḥ) — a drop of water, and उदकबिन्दुः beside it',
           {'purvapada': 'udaka', 'before': 'mantha'},
           note='मन्थौदनसक्तुबिन्दुवज्रभारहारवीवधगाहेषु च — nine named second members, and the option throughout'),
    ),
    '6.3.61': (
        _c("ग्रामणिपुत्रः (grāmaṇiputraḥ) — the headman's son, the ī shortened",
           {'stem': 'ik-anta-aṅī'},
           note='इको ह्रस्वोऽङ्यो गालवस्य — गालवग्रहणं पूजार्थम्, and व्यवस्थितविभाषा चेयम्, so श्रीकुलम् is out'),
    ),
    '6.3.62': (
        _c('एकत्वम् (ekatvam) — oneness, एका shortened before the taddhita',
           {'purvapada': 'eka', 'before': 'taddhita'},
           note='एक तद्धिते च — लिङ्गिविशिष्टस्य ग्रहणम् एकशब्दह्रस्वत्वं प्रयोजयति'),
    ),
    '6.3.63': (
        _c("रेवतिपुत्रः (revatiputraḥ) — Revatī's son, a name",
           {'stem': 'ṅī-āp', 'result': 'saṃjñā'},
           note='ङ्यापोः संज्ञाछन्दसोर्बहुलम् — नान्दीकरः and जगतीछन्दः meet the conditions and are not shortened'),
    ),
    '6.3.64': (
        _c('अजत्वम् (ajatvam) — being a she-goat, the ā shortened',
           {'stem': 'ṅī-āp', 'before': 'tva'},
           note='त्वे च — संज्ञायामसंभवाच्छन्दस्येवोदाहरणानि भवन्ति'),
    ),
    '6.3.65': (
        _c('इष्टकचितम् (iṣṭakacitam) — built of bricks, the pairing fixed',
           {'purvapada': 'iṣṭakā', 'before': 'cita'},
           note='इष्टकेषीकामालानां चिततूलभारिषु — and naming a WORD here does reach what ends in it: पक्वेष्टकचितम्'),
    ),
    '6.3.66': (
        _c('कालिंमन्या (kāliṃmanyā) — she who thinks herself a black antelope',
           {'stem': 'anavyaya', 'before': 'khit'},
           note='खित्यनव्ययस्य — मुमा ह्रस्वो न बाध्यते, else the shortening would never apply at all'),
    ),
    '6.3.67': (
        _c('अरुंतुदः (aruṃtudaḥ) — one who probes a wound, cruel of speech',
           {'purvapada': 'arus', 'before': 'khit'},
           note='अरुर्द्विषदजन्तस्य मुम् — अन्तग्रहणं कृताजन्तकार्यप्रतिपत्त्यर्थम्, अतो ह्रस्वे कृते मुम् भवति'),
    ),
    '6.3.68': (
        _c('गांमन्यः (gāṃmanyaḥ) — one who thinks himself an ox',
           {'stem': 'ic-anta-ekāc', 'before': 'khit'},
           note='इच एकाचोऽम्प्रत्ययवच्च — अतिदेशाद् आत्वपूर्वसवर्णगुणेयङुवङादेशा भवन्ति'),
    ),
    '6.3.69': (
        _c('वाचंयमः (vācaṃyamaḥ) — one who holds his speech, laid down whole',
           {'purvapada': 'vāc', 'before': 'yama'},
           note='वाचंयमपुरन्दरौ च — निपात्येते, and the pairing of stem to second member is fixed'),
    ),
    '6.3.70': (
        _c('सत्यंकारः (satyaṃkāraḥ) — an earnest given to make a bargain good',
           {'purvapada': 'satya', 'before': 'kāra'},
           note='कारे सत्यागदस्य — and vārttikas add अस्तुंकारः, भक्षंकारः, धेनुंभव्या, लोकंपृणा'),
    ),
    '6.3.71': (
        _c('श्यैनंपाता (śyainaṃpātā) — the swooping of a hawk, with the ञ',
           {'purvapada': 'śyena', 'before': 'pāta', 'result': 'ña'},
           note='श्येनतिलस्य पाते ञे — the condition is on what follows the SECOND member, not on it'),
    ),
    '6.3.72': (
        _c('रात्रिंचरः (rātriṃcaraḥ) — one who goes about by night',
           {'purvapada': 'rātri', 'before': 'kṛt'},
           note='रात्रेः कृति विभाषा — अप्राप्तविभाषेयम्, since खिति हि नित्यं मुम् भवति'),
    ),
    '6.3.73': (
        _c('अब्राह्मणः (abrāhmaṇaḥ) — not a brahmin, the न् gone',
           {'purvapada': 'nañ'},
           note='नलोपो नञः — and नञो नलोपोऽवक्षेपे तिङ्युपसंख्यानम् reaches अपचसि त्वं जाल्म, where there is no compound'),
    ),
    '6.3.74': (
        _c('अनश्वः (anaśvaḥ) — having no horse, the नुट् before the vowel',
           {'purvapada': 'nañ', 'before': 'ac'},
           note='तस्मान्नुडचि — तस्मात् is there so the augment attaches to the residue and not to नञ् entire'),
    ),
    '6.3.75': (
        _c('नकुलः (nakulaḥ) — a mongoose, नास्य कुलमस्ति, and the न् kept',
           {'purvapada': 'nañ', 'before': 'nabhrāj'},
           note='नभ्राण्नपान्नवेदानासत्या० प्रकृत्या — and the vṛtti analyses every one, naming the affix that built it'),
    ),
    '6.3.76': (
        _c('एकान्नविंशतिः (ekānnaviṃśatiḥ) — nineteen, twenty less one',
           {'purvapada': 'nañ', 'before': 'eka'},
           note='एकादिश्च एकस्य चादुक् — the augment is put at the end of the FIRST part, so the nasal may be optional'),
    ),
    '6.3.77': (
        _c('नगाः (nagāḥ) — trees, or mountains, that do not go',
           {'purvapada': 'nañ', 'before': 'ga', 'result': 'aprāṇin'},
           note='नगोऽप्राणिष्वन्यतरस्याम् — अगो वृषलः शीतेन is out, a man being alive'),
    ),
    '6.3.78': (
        _c('साश्वत्थम् (sāśvattham) — the place with the aśvattha tree',
           {'purvapada': 'saha', 'result': 'saṃjñā'},
           note='सहस्य सः संज्ञायाम् — सादेश उदात्तो निपात्यते, since आन्तर्य would have given a स्वरित'),
    ),
    '6.3.79': (
        _c('सकलं ज्यौतिषम् (sakalaṃ jyautiṣam) — astronomy down to the last kalā',
           {'purvapada': 'saha', 'result': 'granthānta'},
           note='ग्रन्थान्ताधिके च — stated because 6.3.81 excepts a time-word and these are अव्ययीभावs with one'),
    ),
    '6.3.80': (
        _c('साग्निः कपोतः (sāgniḥ kapotaḥ) — a dove with fire in it',
           {'purvapada': 'saha', 'result': 'dvitīya-anupākhya'},
           note='द्वितीये चानुपाख्ये — अनुपाख्य is glossed as अनुमेय, inferred and not seen'),
    ),
    '6.3.81': (
        _c('सचक्रम् (sacakram) — together with the wheel, an अव्ययीभाव',
           {'purvapada': 'saha', 'samasa': 'avyayībhāva'},
           note='अव्ययीभावे चाकाले — सहपूर्वाह्णम् is out, पूर्वाह्ण being a time-word'),
    ),
    '6.3.82': (
        _c('सपुत्रः (saputraḥ) — with his son, and सहपुत्रः beside it',
           {'purvapada': 'saha', 'result': 'upasarjana'},
           note='वोपसर्जनस्य — यस्य सर्वेऽवयवा उपसर्जनीभूताः स सर्वोपसर्जनो बहुव्रीहिर्गृह्यते'),
    ),
    '6.3.83': (
        _c('स्वस्ति सहपुत्राय (svasti sahaputrāya) — good luck to him and his son',
           {'purvapada': 'saha', 'result': 'āśis'},
           note='प्रकृत्याशिष्यगोवत्सहलेषु — being excepted from a hold-back does not make the substitution compulsory'),
    ),
    '6.3.84': (
        _c('सगर्भ्यः (sagarbhyaḥ) — born of the same womb, in the Veda',
           {'purvapada': 'samāna', 'chandasi': True},
           note='समानस्य छन्दस्यमूर्धप्रभृत्युदर्केषु — and a reading splits the sūtra, समानस्येति योगविभाग इष्यते'),
    ),
    '6.3.85': (
        _c('सनाभिः (sanābhiḥ) — of the same navel, a blood relation',
           {'purvapada': 'samāna', 'before': 'jyotis'},
           note='ज्योतिर्जनपदरात्रिनाभिनाम० — and सवर्ण, the term 1.1.9 defines, gets its शब्द here'),
    ),
    '6.3.86': (
        _c('सब्रह्मचारी (sabrahmacārī) — one keeping the same vow as another',
           {'purvapada': 'samāna', 'before': 'brahmacārin', 'result': 'caraṇa'},
           note='चरणे ब्रह्मचारिणि — the vṛtti works the sense out through ब्रह्म twice over'),
    ),
    '6.3.87': (
        _c('सतीर्थ्यः (satīrthyaḥ) — a fellow-pupil of the same teacher',
           {'purvapada': 'samāna', 'before': 'tīrtha', 'result': 'yat'},
           note='तीर्थे ये — the यत् is what the rule waits for, not तीर्थ alone'),
    ),
    '6.3.88': (
        _c('सोदर्यः (sodaryaḥ) — a full brother, born of the same belly',
           {'purvapada': 'samāna', 'before': 'udara', 'result': 'yat'},
           note='विभाषोदरे — समानोदरे शयित ओ चोदात्तः gives the यत् and the accent together'),
    ),
    '6.3.89': (
        _c('सदृक् (sadṛk) — of the same look, alike',
           {'purvapada': 'samāna', 'before': 'dṛś'},
           note='दृग्दृशवतुषु — वतुग्रहणमुत्तरार्थम्, named here for the two sūtras that follow'),
    ),
    '6.3.90': (
        _c('ईदृक् (īdṛk) — of this sort, इदम् replaced by ईश्',
           {'purvapada': 'idam', 'before': 'dṛś'},
           note="इदंकिमोरीश्की — यथासंख्यम्, and the वतुप् of इयान् is 5.2.40's किमिदम्भ्यां वो घः"),
    ),
    '6.3.91': (
        _c('तादृक् (tādṛk) — of that sort, तद् lengthened to ता',
           {'gana': 'sarvanāman', 'before': 'dṛś'},
           note='आ सर्वनाम्नः — and इदम् and किम्, being pronouns too, are taken first by 6.3.90 naming them'),
    ),
    '6.3.92': (
        _c('विष्वद्र्यङ् (viṣvadryaṅ) — going all ways at once',
           {'purvapada': 'viṣvak', 'before': 'añcati', 'result': 'va'},
           note='विष्वग्देवयोश्च टेरद्र्यञ्चतौ वप्रत्यये — अन्तोदात्तनिपातनं कृत्स्वरनिवृत्त्यर्थम्'),
    ),
    '6.3.93': (
        _c('सम्यङ् (samyaṅ) — going together, and so straight',
           {'purvapada': 'sam', 'before': 'añcati', 'result': 'va'},
           note='समः समि — one stem, one substitute, and the अञ्चति with व still running'),
    ),
    '6.3.94': (
        _c('तिर्यङ् (tiryaṅ) — going crosswise, an animal',
           {'purvapada': 'tiras', 'before': 'añcati', 'result': 'va'},
           note='तिरसस्तिर्यलोपे — तिरश्चा and तिरश्चे are out, 6.4.138 अचः having taken the अ'),
    ),
    '6.3.95': (
        _c('सध्र्यङ् (sadhryaṅ) — going along with, in company',
           {'purvapada': 'saha', 'before': 'añcati', 'result': 'va'},
           note='सहस्य सध्रिः — and the substitute is end-accented by निपातन, as अद्रि was at 6.3.92'),
    ),
    '6.3.96': (
        _c('सधमादः (sadhamādaḥ) — rejoicing together, in the Veda',
           {'purvapada': 'saha', 'before': 'māda', 'chandasi': True},
           note='सध मादस्थयोश्छन्दसि — after स at 6.3.78 and सध्रि at 6.3.95, a third substitute for सह'),
    ),
    '6.3.97': (
        _c('द्वीपम् (dvīpam) — an island, water on both sides',
           {'purvapada': 'dvi', 'gana': 'upasarga', 'before': 'ap'},
           note='द्व्यन्तरुपसर्गेभ्योऽप ईत् — उपसर्गग्रहणं प्राद्युपलक्षणार्थम्, nothing here being joined to a verb'),
    ),
    '6.3.98': (
        _c('अनूपो देशः (anūpo deśaḥ) — a watery country',
           {'purvapada': 'anu', 'before': 'ap', 'result': 'deśa'},
           note="ऊदनोर्देशे — अन्वीपम् is out, no region meant, and 6.3.97's ī stands there"),
    ),
    '6.3.99': (
        _c('अन्यदाशीः (anyadāśīḥ) — a different blessing, the दुक् between',
           {'purvapada': 'anya', 'before': 'āśis'},
           note='अषष्ठ्यतृतीयास्थस्यान्यस्य दुक् — nine second members, and two cases in which the rule does not reach'),
    ),
    '6.3.100': (
        _c('अन्यदर्थः (anyadarthaḥ) — a different purpose, and अन्यार्थः beside it',
           {'purvapada': 'anya', 'before': 'artha'},
           note="अर्थे विभाषा — one word added to 6.3.99's nine, and the augment now optional"),
    ),
    '6.3.101': (
        _c('कदश्वः (kadaśvaḥ) — a wretched horse, the कद् before a vowel',
           {'purvapada': 'ku', 'before': 'ac', 'samasa': 'tatpuruṣa'},
           note='कोः कत् तत्पुरुषेऽचि — कुब्राह्मणः is out, and a vārttika adds कत्त्रयः'),
    ),
    '6.3.102': (
        _c('कद्रथः (kadrathaḥ) — a poor chariot',
           {'purvapada': 'ku', 'before': 'ratha'},
           note="रथवदयोश्च — two second members named, so 6.3.101's vowel condition is not wanted"),
    ),
    '6.3.103': (
        _c('कत्तृणा (kattṛṇā) — the plant so called, a species',
           {'purvapada': 'ku', 'before': 'tṛṇa', 'result': 'jāti'},
           note='तृणे च जातौ — कुत्सितानि तृणानि कुतृणानि is out, being no species'),
    ),
    '6.3.104': (
        _c('कापथः (kāpathaḥ) — a bad road, कु lengthened to का',
           {'purvapada': 'ku', 'before': 'pathin'},
           note="का पथ्यक्षयोः — the second of कु's three shapes, and the first rule to give it"),
    ),
    '6.3.105': (
        _c('कामधुरम् (kāmadhuram) — slightly sweet',
           {'purvapada': 'ku', 'result': 'īṣad'},
           note='ईषदर्थे च — अजादावपि परत्वात् कादेश एव भवति, so it takes काम्लम् from 6.3.101'),
    ),
    '6.3.106': (
        _c('कापुरुषः (kāpuruṣaḥ) — a wretch, and कुपुरुषः beside it',
           {'purvapada': 'ku', 'before': 'puruṣa'},
           note='विभाषा पुरुषे — अप्राप्तविभाषेयम्, since ईषत्पुरुषः कापुरुषः is compulsory by पूर्वविप्रतिषेध'),
    ),
    '6.3.107': (
        _c('कवोष्णम् (kavoṣṇam) — lukewarm, one of three attested forms',
           {'purvapada': 'ku', 'before': 'uṣṇa'},
           note="कवं चोष्णे — and the third form कदुष्णम् is 6.3.101's, उष्ण beginning with a vowel"),
    ),
    '6.3.108': (
        _c('कवपथः (kavapathaḥ) — a bad road, in the Veda',
           {'purvapada': 'ku', 'before': 'pathin', 'chandasi': True},
           note="पथि च छन्दसि — कापथः is 6.3.104's and कुपथः is कु untouched, so three forms stand"),
    ),
    '6.3.109': (
        _c('पृषोदरम् (pṛṣodaram) — speckle-bellied, with the त् simply gone',
           {'gana': 'pṛṣodarādi'},
           note='पृषोदरादीनि यथोपदिष्टम् — and the vṛtti analyses each anyway, so only the operation is unlicensed'),
    ),
    '6.3.110': (
        _c('द्व्यहनि (dvyahani) — on a two-day period, and द्व्यह्नि beside it',
           {'purvapada': 'ahna', 'gana': 'saṅkhyā-vi-sāya-pūrva', 'before': 'ṅi'},
           note='संख्याविसायपूर्वस्याह्नस्याहन्नन्यतरस्यां ङौ — and naming वि and साय shows a part-whole compound is not confined to पूर्वादि'),
    ),
    '6.3.111': (
        _c('लीढम् (līḍham) — licked, the vowel long where the ḍh went',
           {'result': 'ḍhra-lopa'},
           note='ढ्रलोपे पूर्वस्य दीर्घोऽणः — पूर्वग्रहणमनुत्तरपदेऽपि पूर्वमात्रस्य दीर्घार्थम्, since लीढम् is one word'),
    ),
    '6.3.112': (
        _c('वोढा (voḍhā) — one who carries, the a become o',
           {'purvapada': 'sah', 'result': 'ḍhra-lopa'},
           note='सहिवहोरोदवर्णस्य — वर्णग्रहणं कृतायामपि वृद्धौ यथा स्यात्, so उदवोढाम् is reached too'),
    ),
    '6.3.113': (
        _c('साढ्वा (sāḍhvā) — having overcome, laid down for the Veda',
           {'purvapada': 'sah', 'result': 'nigama'},
           note='साढ्यै साढ्वा साढेति निगमे — क्त्वा with no ओ, that same क्त्वा turned to ध्यै, and तृच्'),
    ),
    '6.3.114': (
        _c("विद्मा हि त्वा (vidmā hi tvā) — the heading's own example, at 6.3.135",
           {'gana': 'lakṣaṇa', 'before': 'karṇa'},
           note='संहितायाम् — the fourth heading of the pāda, and the only one about the condition of speech'),
    ),
    '6.3.115': (
        _c('दात्राकर्णः (dātrākarṇaḥ) — sickle-eared, from the brand cut there',
           {'gana': 'lakṣaṇa', 'before': 'karṇa'},
           note="कर्णे लक्षणस्याविष्ट० — the same gloss of लक्षण that 6.2.112's vṛtti gave, word for word"),
    ),
    '6.3.116': (
        _c('उपानत् (upānat) — a sandal, what is bound on below',
           {'before': 'nah', 'result': 'kvip'},
           note='नहिवृतिवृषिव्यधिरुचिसहितनिषु क्वौ — and तन् has to be read into 6.4.40 or परीतत् loses no nasal'),
    ),
    '6.3.117': (
        _c('कोटरावणम् (koṭarāvaṇam) — Koṭara Wood, the name of a place',
           {'gana': 'koṭarādi', 'before': 'vana', 'result': 'saṃjñā'},
           note='वनगिर्योः संज्ञायां कोटरकिंशुलकादीनाम् — यथासंख्यम्, so crossing the two gaṇas is not Sanskrit'),
    ),
    '6.3.118': (
        _c('कृषीवलः (kṛṣīvalaḥ) — a ploughman, one given to ploughing',
           {'before': 'valac'},
           note='वले — वलच्प्रत्ययो गृह्यते न प्रातिपदिकम्, and उत्साह, भ्रातृ, पितृ come down as exceptions'),
    ),
    '6.3.119': (
        _c('अमरावती (amarāvatī) — Amarāvatī, a river and a city',
           {'before': 'matup', 'result': 'bahvac-saṃjñā'},
           note='मतौ बह्वचोऽनजिरादीनाम् — व्रीहिमती is out for few vowels and वलयवती for not being a name'),
    ),
    '6.3.120': (
        _c('शरावती (śarāvatī) — Śarāvatī, reed-bearing',
           {'gana': 'śarādi', 'before': 'matup', 'result': 'saṃjñā'},
           note='शरादीनां च — शर, वंश, धूम, अहि, कपि, मणि, मुनि, शुचि, हनु, none of them many-voweled'),
    ),
    '6.3.121': (
        _c('ऋषीवहम् (ṛṣīvaham) — what carries a seer',
           {'gana': 'ik-anta', 'before': 'vaha'},
           note='इको वहेऽपीलोः — पिण्डवहम् is not इक्-final, and दारुवहम् is out by a vārttika'),
    ),
    '6.3.122': (
        _c('अपामार्गः (apāmārgaḥ) — the plant that wipes away',
           {'gana': 'upasarga', 'before': 'ghañ'},
           note='उपसर्गस्य घञ्यमनुष्ये बहुलम् — and vārttikas fix प्रासादः and प्राकारः for what is MADE'),
    ),
    '6.3.123': (
        _c('नीकाशः (nīkāśaḥ) — the look of a thing, its appearance',
           {'gana': 'ik-anta-upasarga', 'before': 'kāśa'},
           note='इकः काशे — प्रकाशः is out, प्र not being इक्-final'),
    ),
    '6.3.124': (
        _c('नीत्तम् (nīttam) — given down, handed over',
           {'gana': 'ik-anta-upasarga', 'before': 'ti-ādeśa', 'result': 'dā'},
           note='दस्ति — 7.4.47 makes a त् of the FINAL, and चर्त्वस्याश्रयात् सिद्धत्वम् is what makes it initial'),
    ),
    '6.3.125': (
        _c('अष्टावक्रः (aṣṭāvakraḥ) — Aṣṭāvakra, bent in eight places',
           {'purvapada': 'aṣṭan', 'result': 'saṃjñā'},
           note='अष्टनः संज्ञायाम् — अष्टपुत्रः and अष्टभार्यः are out, being no names'),
    ),
    '6.3.126': (
        _c('अष्टाकपालम् (aṣṭākapālam) — an oblation on eight potsherds',
           {'purvapada': 'aṣṭan', 'chandasi': True},
           note='छन्दसि च — and गवि च युक्ते भाषायाम् adds the eight-ox cart'),
    ),
    '6.3.127': (
        _c('एकचितीकः (ekacitīkaḥ) — of a single layer',
           {'purvapada': 'citi', 'before': 'kap'},
           note='चितेः कपि — one stem, one following affix, and no further condition'),
    ),
    '6.3.128': (
        _c('विश्वावसुः (viśvāvasuḥ) — Viśvāvasu, whose wealth is all',
           {'purvapada': 'viśva', 'before': 'vasu'},
           note='विश्वस्य वसुराटोः — राडिति विकारनिर्देशः, so विश्वराजौ and विश्वराजः are out'),
    ),
    '6.3.129': (
        _c("विश्वानरः (viśvānaraḥ) — Viśvānara, a man's name",
           {'purvapada': 'viśva', 'before': 'nara', 'result': 'saṃjñā'},
           note='नरे संज्ञायाम् — विश्वे नरा यस्य स विश्वनरः keeps its length, being no name'),
    ),
    '6.3.130': (
        _c('विश्वामित्रः (viśvāmitraḥ) — Viśvāmitra, the seer',
           {'purvapada': 'viśva', 'before': 'mitra', 'result': 'ṛṣi'},
           note='मित्रे चर्षौ — 6.2.165 had kept the seers OUT of an accent rule; here the seer is the whole condition'),
    ),
    '6.3.131': (
        _c('सोमावती (somāvatī) — having soma, said of the waters',
           {'purvapada': 'soma', 'before': 'matup', 'result': 'mantra'},
           note='मन्त्रे सोमाश्वेन्द्रियविश्वदेव्यस्य मतौ — four stems, one affix, and the register doing the work'),
    ),
    '6.3.132': (
        _c('ओषधीभिः (oṣadhībhiḥ) — with the healing plants, in a mantra',
           {'purvapada': 'oṣadhi', 'before': 'vibhakti', 'result': 'mantra'},
           note='ओषधेश्च विभक्तावप्रथमायाम् — मन्त्र इति वर्तते, the register carried down from 6.3.131'),
    ),
    '6.3.133': (
        _c('आ तू न इन्द्र (ā tū na indra) — the particle तु lengthened in a verse',
           {'purvapada': 'tu', 'result': 'ṛc'},
           note='ऋचि तुनुघमक्षुतङ्कुत्रोरुष्याणाम् — शृणोत ग्रावाणः is out, its थ not being the ङित् substitute'),
    ),
    '6.3.134': (
        _c('अभी षु णः (abhī ṣu ṇaḥ) — the particle सु after a lengthened अभि',
           {'gana': 'ik-anta', 'before': 'suñ', 'result': 'mantra'},
           note="इकः सुञि — सुञ् निपातो गृह्यते, and the ष् is 8.3.105's and the ण् 8.4.27's"),
    ),
    '6.3.135': (
        _c('विद्मा हि त्वा (vidmā hi tvā) — we know thee, in a verse',
           {'gana': 'dvyac-tiṅ', 'result': 'ṛc'},
           note='द्व्यचोऽतस्तिङः — भवत has three vowels and वक्षि does not end in अ, so neither is reached'),
    ),
    '6.3.136': (
        _c('एवा ते (evā te) — thus for thee, the particle lengthened',
           {'gana': 'nipāta', 'result': 'ṛc'},
           note='निपातस्य च — the widest rule of the run, and its whole content is one word plus an anuvṛtti'),
    ),
    '6.3.137': (
        _c('केशाकेशि (keśākeśi) — a fight hair against hair',
           {'gana': 'anyeṣām-api'},
           note="अन्येषामपि दृश्यते — and a vārttika makes श्वन्'s case exact, श्वादन्तः, श्वापदः and five more"),
    ),
    '6.3.138': (
        _c('दधीचः (dadhīcaḥ) — Dadhīca, and the यण् held off to allow it',
           {'before': 'cu'},
           note='चौ — अन्तरङ्गोऽपि हि यणादेशो दीर्घविधानसामर्थ्याद् न प्रवर्तते'),
    ),
    '6.3.139': (
        _c('कारीषगन्धीपुत्रः (kārīṣagandhīputraḥ) — the son of Kārīṣagandhyā',
           {'gana': 'samprasāraṇa-anta'},
           note='संप्रसारणस्य — and 6.3.61 would have shortened the same vowel: सकृद्गतौ विप्रतिषेधे यद्बाधितं तद्बाधितमेव'),
    ),
    '6.4.1': (
        _c("अग्नीनाम् (agnīnām) — the heading's own example, at 6.4.3",
           {'before': 'nām'},
           note='अङ्गस्य — and the vṛtti proves the scope three times over, once from this pāda, once from further on, once from 7.1'),
    ),
    '6.4.2': (
        _c('हूतः (hūtaḥ) — called, the vocalised vowel lengthened',
           {'part': 'saṃprasāraṇa', 'result': 'hal-pūrva'},
           note='हलः — अङ्गग्रहणमावर्तयितव्यं हल्विशेषणार्थम्, अङ्गकार्यप्रतिपत्त्यर्थं च, so the word is read in twice'),
    ),
    '6.4.3': (
        _c('अग्नीनाम् (agnīnām) — of the fires, the ि lengthened before नाम्',
           {'before': 'nām'},
           note='नामि — नामि दीर्घ आमि चेत्स्यात् कृते दीर्घे न नुड् भवेत्, the vṛtti settling the circle by verse'),
    ),
    '6.4.4': (
        _c('तिसृणाम् (tisṛṇām) — of three, and 6.4.3 refused',
           {'stem': 'tisṛ', 'before': 'nām'},
           note='न तिसृचतसृ — दीर्घप्रतिषेधवचनं ज्ञापकम्, that 7.1.54 beats 7.2.100 by पूर्वविप्रतिषेध'),
    ),
    '6.4.5': (
        _c('तिसृणां मध्यन्दिने (tisṛṇāṃ madhyandine) — the long form, in the Veda',
           {'stem': 'tisṛ', 'before': 'nām', 'chandasi': True},
           note="छन्दस्युभयथा — उभयथा दृश्यते, दीर्घश्चादीर्घश्च, so 6.4.4's refusal is lifted for the Veda"),
    ),
    '6.4.6': (
        _c('नृणाम् (nṛṇām) — of men, in both lengths',
           {'stem': 'nṛ', 'before': 'nām'},
           note='नृ च — केचिदत्र छन्दसीति नानुवर्तयन्ति, on whose reading the option holds outside the Veda too'),
    ),
    '6.4.7': (
        _c('पञ्चानाम् (pañcānām) — of five, the penult lengthened',
           {'before': 'nām', 'part': 'upadhā', 'result': 'n-anta'},
           note='नोपधायाः — चतुर्णाम् is out, चतुर् not ending in न्'),
    ),
    '6.4.8': (
        _c('राजा (rājā) — the king, the penult long before the ending',
           {'before': 'sarvanāmasthāna', 'part': 'upadhā', 'result': 'n-anta'},
           note='सर्वनामस्थाने चासम्बुद्धौ — हे राजन् and हे तक्षन् are out, being vocative singulars'),
    ),
    '6.4.9': (
        _c('तक्षाणम् (takṣāṇam) — the carpenter, optionally so in the Veda',
           {'before': 'sarvanāmasthāna', 'part': 'upadhā', 'result': 'ṣa-pūrva'},
           note='वा षपूर्वस्य निगमे — outside the Veda तक्षा, तक्षाणौ, तक्षाणः, and 6.4.8 is compulsory'),
    ),
    '6.4.10': (
        _c('महान् (mahān) — great, the penult lengthened before the ending',
           {'stem': 'mahat', 'gana': 'sānta-saṃyoga', 'before': 'sarvanāmasthāna', 'part': 'upadhā'},
           note='सान्तमहतः संयोगस्य — 6.3.46 made महा of महत् before a second member; this makes महान् before an ending'),
    ),
    '6.4.11': (
        _c('कर्तारौ कटान् (kartārau kaṭān) — the two makers of mats',
           {'stem': 'ap', 'before': 'sarvanāmasthāna', 'part': 'upadhā'},
           note='अप्तृन्तृच्स्वसृ० — and अप् needs two paribhāṣās, one to leave off a समासान्त and one to hold back a नुम्'),
    ),
    '6.4.12': (
        _c('बहुदण्डीनि (bahudaṇḍīni) — many-staffed things, before शि',
           {'gana': 'in-han-four', 'before': 'śi', 'part': 'upadhā'},
           note='इन्हन्पूषार्यम्णां शौ — सिद्धे सत्यारम्भो नियमार्थः, शावेव दीर्घो भवति नान्यत्र'),
    ),
    '6.4.13': (
        _c('दण्डी (daṇḍī) — the staff-bearer, with सु let back into the rule',
           {'gana': 'in-han-four', 'before': 'su', 'part': 'upadhā'},
           note='सौ च — हे दण्डिन् and हे वृत्रहन् are out, being vocative singulars'),
    ),
    '6.4.14': (
        _c('गोमान् (gomān) — having cattle, the penult long',
           {'gana': 'atu-as-anta', 'before': 'su', 'part': 'upadhā'},
           note='अत्वसन्तस्य चाधातोः — and the lengthening must happen before the नुम्, or there is no vowel left to lengthen'),
    ),
    '6.4.15': (
        _c('शान्तः (śāntaḥ) — calmed, the penult lengthened',
           {'gana': 'anunāsika-anta', 'before': 'kvip', 'part': 'upadhā', 'result': 'kṅit'},
           note='अनुनासिकस्य क्विझलोः क्ङिति — गन्ता and रन्ता are out, the affix being neither कित् nor ङित्'),
    ),
    '6.4.16': (
        _c('चिकीर्षति (cikīrṣati) — he wants to do, the vowel lengthened',
           {'stem': 'han', 'gana': 'ac-anta', 'before': 'san', 'result': 'jhal-ādi'},
           note='अज्झनगमां सनि — and the Vedic समजिगांसत् is sent to 6.3.137, the catch-all of the pāda before'),
    ),
    '6.4.17': (
        _c('तितांसति (titāṃsati) — he wants to stretch, and तितंसति beside it',
           {'stem': 'tan', 'before': 'san', 'result': 'jhal-ādi'},
           note='तनोतेर्विभाषा — the इट् comes from a vārttika on 7.2.49, and gives a third form'),
    ),
    '6.4.18': (
        _c('क्रान्त्वा (krāntvā) — having stepped, and क्रन्त्वा beside it',
           {'stem': 'kram', 'before': 'ktvā', 'part': 'upadhā', 'result': 'jhal-ādi'},
           note='क्रमश्च क्त्वि — बहिरङ्गोऽपि ल्यबादेशोऽन्तरङ्गानपि विधीन् बाधते, so प्रक्रम्य never has a क्त्वा left'),
    ),
    '6.4.19': (
        _c('प्रश्नः (praśnaḥ) — a question, the छ् become श्',
           {'before': 'anunāsika', 'part': 'cha-va', 'result': 'kṅit'},
           note='छ्वोः शूडनुनासिके च — and what श् replaces is छ् WITH its तुक्, 6.1.73 being inner and going first'),
    ),
    '6.4.20': (
        _c('जूः (jūḥ) — fever, two sounds replaced by one',
           {'stem': 'jvar', 'before': 'kvip', 'part': 'va-upadhā', 'result': 'kṅit'},
           note='ज्वरत्वरस्रिव्यविमवामुपधायाश्च — ज्वरत्वरोरुपधा वकारात् परा, स्रिव्यवमवां पूर्वा'),
    ),
    '6.4.21': (
        _c('मूः (mūḥ) — from मुर्छ्, the छ् simply gone',
           {'before': 'kvip', 'part': 'cha-va', 'result': 'r-pūrva'},
           note='राल्लोपः — सतुक्कस्य छस्याभावात् केवलो गृह्यते, a र् before it meaning 6.1.73 never applied'),
    ),
    '6.4.23': (
        _c('अनक्ति (anakti) — he anoints, the न् of the infix gone',
           {'before': 'śna'},
           note='श्नान्नलोपः — शकारवतो ग्रहणं किम्? यज्ञानाम्, यत्नानाम्, which 7.3.102 would otherwise make look alike'),
    ),
    '6.4.24': (
        _c('स्रस्तः (srastaḥ) — fallen, the न् of the penult gone',
           {'gana': 'anidit-hal-anta', 'before': 'kṅit'},
           note='अनिदितां हल उपधायाः क्ङिति — and a vārttika adds लङ्ग् for illness and कम्प् for bodily change'),
    ),
    '6.4.25': (
        _c('दशति (daśati) — he bites, the nasal gone before शप्',
           {'stem': 'daṃś', 'before': 'śap'},
           note='दंशसञ्जस्वञ्जां शपि — three roots named, and one affix'),
    ),
    '6.4.26': (
        _c('रजति (rajati) — he dyes, and रञ्ज् now stands alone',
           {'stem': 'rañj', 'before': 'śap'},
           note='रञ्जेश्च — split off so that रञ्ज् alone carries down into 6.4.27'),
    ),
    '6.4.27': (
        _c('रागः (rāgaḥ) — the dyeing, or the dye that does it',
           {'stem': 'rañj', 'before': 'ghañ', 'result': 'bhāva'},
           note='घञि च भावकरणयोः — रजन्ति तस्मिन्निति रङ्गः keeps its न्, being neither act nor means'),
    ),
    '6.4.28': (
        _c('गोस्यदः (gosyadaḥ) — the speed of a cow, laid down whole',
           {'stem': 'syand', 'before': 'ghañ', 'result': 'java'},
           note='स्यदो जवे — तैलस्यन्दः keeps its न्, no speed being meant'),
    ),
    '6.4.29': (
        _c('एधः (edhaḥ) — fuel, with the न् gone and the guṇa made',
           {'stem': 'avoda'},
           note='अवोदैधोद्मप्रश्रथहिमश्रथाः — न धातुलोप आर्धधातुके इति हि प्रतिषेधः स्यात्, so the guṇa is निपातन too'),
    ),
    '6.4.30': (
        _c('अञ्चितम् (añcitam) — honoured, and the न् kept',
           {'stem': 'añc', 'result': 'pūjā'},
           note="न अञ्चेः पूजायाम् — and the इट् of अञ्चिता is 7.2.53's, stated for the same sense"),
    ),
    '6.4.31': (
        _c('स्कन्त्वा (skantvā) — having leapt, and the न् kept',
           {'stem': 'skand', 'before': 'ktvā'},
           note='क्त्वि स्कन्दिस्यन्दोः — स्यन्दित्वा needs no refusal, 1.2.18 having removed the कित् already'),
    ),
    '6.4.32': (
        _c('रङ्क्त्वा (raṅktvā) — having dyed, and रक्त्वा beside it',
           {'stem': 'naś', 'gana': 'j-anta', 'before': 'ktvā'},
           note='जान्तनशां विभाषा — three forms for नश्, the third from the इट् option'),
    ),
    '6.4.33': (
        _c('अभाजि (abhāji) — it was broken, and अभञ्जि beside it',
           {'stem': 'bhañj', 'before': 'ciṇ'},
           note='भञ्जेश्च चिणि — अप्राप्तोऽयं नलोपः पक्षे विधीयते, ततो नेति नानुवर्तते'),
    ),
    '6.4.34': (
        _c('शिष्टः (śiṣṭaḥ) — instructed, the penult become इ',
           {'stem': 'śās', 'before': 'aṅ', 'result': 'kṅit'},
           note='शास इदङ्हलोः — and a vārttika adds क्विप्, giving मित्रशीः'),
    ),
    '6.4.35': (
        _c('प्रशाधि (praśādhi) — rule thou, the whole root replaced',
           {'stem': 'śās', 'before': 'hi'},
           note='शा हौ — उपधाया इति निवृत्तम्, ततः शास इति स्थानेयोगा षष्ठी भवति'),
    ),
    '6.4.36': (
        _c('जहि शत्रून् (jahi śatrūn) — slay the foes',
           {'stem': 'han', 'before': 'hi'},
           note='हन्तेर्जः — the second of two roots replaced whole before one affix'),
    ),
    '6.4.37': (
        _c('यत्वा (yatvā) — having restrained, the nasal gone',
           {'stem': 'van', 'gana': 'anudāttopadeśa', 'before': 'jhal', 'result': 'kṅit'},
           note='अनुदात्तोपदेशवनतितनोत्यादीनाम् — a class gathered by the accent the Dhātupāṭha teaches, not by sound'),
    ),
    '6.4.38': (
        _c('प्रयत्य (prayatya) — having restrained, and प्रयम्य beside it',
           {'stem': 'van', 'gana': 'anudāttopadeśa', 'before': 'lyap'},
           note='वा ल्यपि — व्यवस्थितविभाषा चेयम्, तेन मकारान्तानां विकल्पो भवति, अन्यत्र नित्यमेव लोपः'),
    ),
    '6.4.39': (
        _c('यन्तिः (yantiḥ) — restraint, the nasal kept and not lengthened',
           {'stem': 'van', 'gana': 'anudāttopadeśa', 'before': 'ktic'},
           note='न क्तिचि दीर्घश्च — a refusal that has to refuse twice, because refusing once creates the second case'),
    ),
    '6.4.40': (
        _c('अङ्गगत् (aṅgagat) — going to Aṅga, the nasal gone',
           {'stem': 'gam', 'before': 'kvip'},
           note='गमः क्वौ — and 6.3.116 leans on the गमादि vārttika for तन्, giving परीतत्'),
    ),
    '6.4.41': (
        _c('अब्जा (abjā) — water-born, the nasal become आ',
           {'gana': 'anunāsika-anta', 'before': 'viṭ'},
           note="विड्वनोरनुनासिकस्यात् — the विट् is 3.2.67's and the ष् of गोषाः is 8.3.106's"),
    ),
    '6.4.42': (
        _c('जातः (jātaḥ) — born, the nasal become आ',
           {'stem': 'jan', 'before': 'san', 'result': 'kṅit'},
           note='जनसनखनां सञ्झलोः — झल् is carried down to qualify the सन्, so जिजनिषति is out'),
    ),
    '6.4.43': (
        _c('जायते (jāyate) — he is born, and जन्यते beside it',
           {'stem': 'jan', 'before': 'ya', 'result': 'kṅit'},
           note='ये विभाषा — but before श्यन् 7.3.79 gives जन् a जा outright and no option arises'),
    ),
    '6.4.44': (
        _c('तायते (tāyate) — it is stretched, and तन्यते beside it',
           {'stem': 'tan', 'before': 'yak'},
           note='तनोतेर्यकि — यकीति किम्? तन्तन्यते, where the affix is a यङ्'),
    ),
    '6.4.45': (
        _c('सातिः (sātiḥ) — winning, one of three forms the sūtra gives',
           {'stem': 'san', 'before': 'ktic'},
           note="सनः क्तिचि लोपश्चास्यान्यतरस्याम् — अन्यतरस्यांग्रहणं विस्पष्टार्थम्, lest 6.4.43's विभाषा seem to have lapsed"),
    ),
    '6.4.46': (
        _c("चिकीर्षिता (cikīrṣitā) — the heading's own example, at 6.4.48",
           {'gana': 'a-anta'},
           note='आर्धधातुके — न ल्यपि इति प्राग् एतस्मात्, so one sūtra both refuses and closes the run'),
    ),
    '6.4.47': (
        _c('भर्ष्टा (bharṣṭā) — a roaster, and भ्रष्टा beside it',
           {'stem': 'bhrasj', 'part': 'ra-upadhā'},
           note='भ्रस्जो रोपधयो रमन्यतरस्याम् — the म् marker is what puts the substitute after the last vowel'),
    ),
    '6.4.48': (
        _c('चिकीर्षिता (cikīrṣitā) — one who wants to do, the अ gone',
           {'gana': 'a-anta', 'part': 'antya'},
           note='अतो लोपः — वृद्धिदीर्घाभ्यामतो लोपः पूर्वविप्रतिषेधेन, so the loss takes the vowel first'),
    ),
    '6.4.49': (
        _c('बेभिदिता (bebhiditā) — one who splits repeatedly',
           {'stem': 'ya', 'result': 'hal-pūrva'},
           note='यस्य हलः — read as a whole, so 1.1.52 does not cut it down to the अ that 6.4.48 had taken anyway'),
    ),
    '6.4.50': (
        _c('समिधिता (samidhitā) — and समिध्यिता beside it',
           {'stem': 'kya', 'result': 'hal-pūrva'},
           note='क्यस्य विभाषा — which क्य the vṛtti leaves to the derivation, क्यच् or क्यङ् यथायोगम्'),
    ),
    '6.4.51': (
        _c('कारकः (kārakaḥ) — a doer, the causal णि gone',
           {'stem': 'ṇi'},
           note='णेरनिटि — इयङ्यण्गुणवृद्धिदीर्घाणामपवादः, the vṛtti naming five rules it displaces at once'),
    ),
    '6.4.52': (
        _c('कारितम् (kāritam) — caused to be done, the णि gone',
           {'stem': 'ṇi', 'before': 'niṣṭhā', 'result': 'seṭ'},
           note='निष्ठायां सेटि — सेड्ग्रहणसामर्थ्यादिह पूर्वेणापि न भवति, so संज्ञपितः escapes both rules'),
    ),
    '6.4.53': (
        _c('जनिता (janitā) — the begetter, in a mantra',
           {'stem': 'ṇi', 'before': 'tṛc', 'result': 'mantra'},
           note='जनिता मन्त्रे — neither 6.4.51 nor 6.4.52 could have reached it, the affix having an इट् and being no निष्ठा'),
    ),
    '6.4.54': (
        _c('शमितः (śamitaḥ) — O slaughterer, in the rite',
           {'stem': 'ṇi', 'before': 'tṛc', 'result': 'yajña'},
           note='शमिता यज्ञे — शृतं हविः शमयितः outside the rite, and the णि stays'),
    ),
    '6.4.55': (
        _c('कारयांचकार (kārayāṃcakāra) — he caused to be done',
           {'stem': 'ṇi', 'before': 'ām'},
           note="अय् आमन्तात्वाय्येत्न्विष्णुषु — नेति वक्तव्येऽयादेशवचनमुत्तरार्थम्, said as अय् for the next rule's sake"),
    ),
    '6.4.56': (
        _c('प्रणमय्य (praṇamayya) — having caused to bend',
           {'stem': 'ṇi', 'before': 'lyap', 'result': 'laghu-pūrva'},
           note="ल्यपि लघुपूर्वात् — and 6.4.22's असिद्धत्व does not reach, the two operations resting on different things"),
    ),
    '6.4.57': (
        _c('प्रापय्य (prāpayya) — having caused to reach',
           {'stem': 'ṇi', 'before': 'lyap', 'result': 'āp-pūrva'},
           note='विभाषाऽऽपः — इङादेशस्य लाक्षणिकत्वाद् न भवति, so अध्याप्य keeps no अय्'),
    ),
    '6.4.58': (
        _c('वियूय (viyūya) — having separated, in the Veda',
           {'stem': 'yu', 'before': 'lyap', 'chandasi': True},
           note='युप्लुवोर्दीर्घश्छन्दसि — छन्दसीति किम्? संयुत्य, आप्लुत्य'),
    ),
    '6.4.59': (
        _c('प्रक्षीय (prakṣīya) — having wasted away',
           {'stem': 'kṣi', 'before': 'lyap'},
           note='क्षियः — a one-word sūtra taking दीर्घ and ल्यप् from the one before it'),
    ),
    '6.4.60': (
        _c('प्रक्षीणः (prakṣīṇaḥ) — wasted away, worn out',
           {'stem': 'kṣi', 'before': 'niṣṭhā'},
           note='निष्ठायामण्यदर्थे — the ण्यत् means the act or the object, and a निष्ठा meaning either is out'),
    ),
    '6.4.61': (
        _c('क्षितायुरेधि (kṣitāyuredhi) — may your life be spent, in abuse',
           {'stem': 'kṣi', 'before': 'niṣṭhā', 'result': 'ākrośa'},
           note='वाऽऽक्रोशदैन्ययोः — क्षितोऽयं तपस्वी beside क्षीणोऽयं तपस्वी for misery'),
    ),
    '6.4.62': (
        _c('अकारि (akāri) — it was done, the stem behaving as before चिण्',
           {'stem': 'han', 'gana': 'ac-anta', 'before': 'sya', 'result': 'bhāva'},
           note='स्यसिच्सीयुट्तासिषु० चिण्वदिट् च — the इट् goes to the four affixes and not the stem, अङ्गस्य तु लक्ष्यविरोधाद् न क्रियते'),
    ),
    '6.4.63': (
        _c('उपदिदीये (upadidīye) — he wasted away, the युट् between',
           {'stem': 'dīṅ', 'before': 'ac', 'result': 'kṅit'},
           note="दीङो युडचि क्ङिति — and the rule's mere existence stops 6.4.22 hiding it from 6.4.82"),
    ),
    '6.4.64': (
        _c('पपिथ (papitha) — thou hast drunk, the आ gone',
           {'gana': 'ā-anta', 'before': 'iṭ', 'part': 'antya', 'result': 'kṅit'},
           note='आतो लोप इटि च — यान्ति and वान्ति keep theirs, no ārdhadhātuka following'),
    ),
    '6.4.65': (
        _c('देयम् (deyam) — to be given, the आ become ई',
           {'gana': 'ā-anta', 'before': 'yat'},
           note='ईद्यति — one affix, one substitute, and the आ-final class taken from the rule before'),
    ),
    '6.4.66': (
        _c('दीयते (dīyate) — it is given, the आ become ई',
           {'stem': 'mā', 'gana': 'ghu', 'before': 'hal', 'result': 'kṅit'},
           note='घुमास्थागापाजहातिसां हलि — पायते is out, पा of the second class not being meant'),
    ),
    '6.4.67': (
        _c('देयात् (deyāt) — may he give, the आ become ए',
           {'stem': 'mā', 'gana': 'ghu', 'before': 'liṅ', 'result': 'kṅit'},
           note='एर्लिङि — क्ङितीत्येव, so दासीष्ट and धासीष्ट keep their आ'),
    ),
    '6.4.68': (
        _c('ग्लेयात् (gleyāt) — may he droop, and ग्लायात् beside it',
           {'gana': 'ā-anta-saṃyoga-ādi', 'before': 'liṅ', 'result': 'kṅit'},
           note="वाऽन्यस्य संयोगादेः — यायात् is out, having no cluster at the start; this is the heading's last sūtra"),
    ),
    '6.4.69': (
        _c('प्रदाय (pradāya) — having given, the आ kept',
           {'stem': 'mā', 'gana': 'ghu', 'before': 'lyap'},
           note='न ल्यपि — one sūtra both refuses an operation and bounds the run that granted it'),
    ),
    '6.4.70': (
        _c('अपमित्य (apamitya) — having bartered, and अपमाय beside it',
           {'stem': 'may', 'before': 'lyap'},
           note='मयतेरिदन्यतरस्याम् — the first sūtra past the आर्धधातुके heading, and still about ल्यप्'),
    ),
    '6.4.71': (
        _c('अकरोत् (akarot) — he did, with the augment अट् in front',
           {'before': 'luṅ'},
           note='लुङ्लङ्लृङ्क्ष्वडुदात्तः — the accent is part of the rule and not a consequence of it'),
    ),
    '6.4.72': (
        _c('ऐक्षिष्ट (aikṣiṣṭa) — he saw, the आट् before a vowel',
           {'gana': 'ac-ādi', 'before': 'luṅ'},
           note='आडजादीनाम् — and ऐज्यत needs the ending substituted first, being inner, and the class-marker then beating the augment'),
    ),
    '6.4.73': (
        _c('आवः (āvaḥ) — he covered, the आट् where no rule puts it',
           {'chandasi': True},
           note='छन्दस्यपि दृश्यते — आडजादीनामित्युक्तमनजादीनामपि दृश्यते'),
    ),
    '6.4.74': (
        _c('मा भवान् कार्षीत् (mā bhavān kārṣīt) — let him not do it',
           {'before': 'luṅ', 'result': 'māṅ-yoga'},
           note="न माङ्योगे — both 6.4.71's अट् and 6.4.72's आट् are refused together"),
    ),
    '6.4.75': (
        _c('जनिष्ठाः (janiṣṭhāḥ) — thou wast born, with no augment',
           {'before': 'luṅ', 'chandasi': True},
           note="बहुलं छन्दस्यमाङ्योगेऽपि — 6.4.74's refusal lifted and 6.4.71's grant suspended, in one sūtra"),
    ),
    '6.4.76': (
        _c('दध्रे (dadhre) — they held, इर become रे',
           {'stem': 'ira', 'chandasi': True},
           note='इरयो रे — धाञो रेभावस्यासिद्धत्वादातो लोपो भवति'),
    ),
    '6.4.78': (
        _c("इयेष (iyeṣa) — he wished, the copy's इ become इय्",
           {'before': 'ac', 'part': 'abhyāsa'},
           note='अभ्यासस्यासवर्णे — ईषतुः and ऊषुः are out, the vowel that follows being of the same class'),
    ),
    '6.4.79': (
        _c('स्त्रियौ (striyau) — two women, the ī become iy',
           {'stem': 'strī', 'before': 'ac'},
           note='स्त्रियाः — and स्त्रीणाम् keeps its ī, the नुट् winning there by being later'),
    ),
    '6.4.80': (
        _c('स्त्रियं पश्य (striyaṃ paśya) — see the woman, and स्त्रीं beside it',
           {'stem': 'strī', 'before': 'am'},
           note='वाऽंशसोः — this is what 6.4.79 was split off for'),
    ),
    '6.4.81': (
        _c('यन्ति (yanti) — they go, the इ become य्',
           {'stem': 'iṇ', 'before': 'ac'},
           note='इणो यण् — मध्येऽपवादाः पूर्वान् विधीन् बाधन्ते, and गुणवृद्धि beat it by being later'),
    ),
    '6.4.82': (
        _c('निन्युः (ninyuḥ) — they led, the ī become y',
           {'gana': 'i-anta-anekāc', 'before': 'ac'},
           note='एरनेकाचोऽसंयोगपूर्वस्य — असंयोगपूर्वग्रहणमिवर्णविशेषणं यथा स्याद्, अङ्गविशेषणं मा भूत्'),
    ),
    '6.4.83': (
        _c('खलप्वौ (khalapvau) — two threshing-floor sweepers',
           {'gana': 'u-anta-anekāc', 'before': 'sup'},
           note='ओः सुपि — narrower than 6.4.82, wanting a सुप् and not any vowel affix'),
    ),
    '6.4.84': (
        _c('वर्षाभ्वौ (varṣābhvau) — two rain-born creatures',
           {'stem': 'varṣābhū', 'before': 'sup'},
           note='वर्षाभ्वश्च — पुनर्भ्वश्चेति वक्तव्यम्, and कारापूर्वस्यापीष्यते'),
    ),
    '6.4.85': (
        _c('प्रतिभुवौ (pratibhuvau) — two sureties, and no यण्',
           {'stem': 'bhū', 'before': 'sup'},
           note="न भूसुधियोः — सुपि is still running from 6.4.83, so भू's वुक् at 6.4.88 is untouched"),
    ),
    '6.4.86': (
        _c('विभ्वम् (vibhvam) — the pervading one, and विभुवम् beside it',
           {'stem': 'bhū', 'before': 'sup', 'chandasi': True},
           note='छन्दस्युभयथा — the refusal of 6.4.85 lifted, and both forms attested'),
    ),
    '6.4.87': (
        _c('जुह्वति (juhvati) — they offer, the उ become व्',
           {'stem': 'hu', 'gana': 'śnu-anta', 'before': 'sārvadhātuka'},
           note='हुश्नुवोः सार्वधातुके — इदमेव हुश्नुग्रहणं ज्ञापकं भाषायामपि यङ्लुगस्तीति'),
    ),
    '6.4.88': (
        _c('बभूव (babhūva) — he became, and the वुक् gives the second व्',
           {'stem': 'bhū', 'before': 'luṅ'},
           note='भुवो वुग्लुङ्लिटोः — the rule that gives बभूव its second व्'),
    ),
    '6.4.89': (
        _c('निगूहयति (nigūhayati) — he conceals, the penult long',
           {'stem': 'gūh', 'before': 'ac', 'part': 'upadhā'},
           note='ऊदुपधाया गोहः — विकृतग्रहणं विषयार्थम्, so निजुगुहतुः is untouched'),
    ),
    '6.4.90': (
        _c('दूषयति (dūṣayati) — he spoils, the penult become ū',
           {'stem': 'doṣ', 'before': 'ṇi', 'part': 'upadhā'},
           note='दोषो णौ — विकृतग्रहणं प्रक्रमाभेदार्थम्, पूर्वत्र हि गोह इत्युक्तम्'),
    ),
    '6.4.91': (
        _c('चित्तं दोषयति (cittaṃ doṣayati) — he corrupts the mind',
           {'stem': 'doṣ', 'before': 'ṇi', 'part': 'upadhā', 'result': 'cittavirāga'},
           note='वा चित्तविरागे — the sense makes what 6.4.90 made compulsory into an option'),
    ),
    '6.4.92': (
        _c('घटयति (ghaṭayati) — he brings about, the penult short',
           {'gana': 'mit', 'before': 'ṇi', 'part': 'upadhā'},
           note='मितां ह्रस्वः — केचिदत्र वेत्यनुवर्तयन्ति, and that option is व्यवस्थित, so उत्क्रामयति comes out'),
    ),
    '6.4.93': (
        _c('अशामि (aśāmi) — it was calmed, and अशमि beside it',
           {'gana': 'mit', 'before': 'ciṇ', 'part': 'upadhā'},
           note='चिण्णमुलोर्दीर्घोऽन्यतरस्याम् — दीर्घग्रहणं किम्? an option on the shortening would not reach a second णि'),
    ),
    '6.4.94': (
        _c('परंतपः (paraṃtapaḥ) — one who scorches his foes',
           {'before': 'khac', 'part': 'upadhā'},
           note='खचि ह्रस्वः — no मित् class wanted here, only the affix'),
    ),
    '6.4.95': (
        _c('प्रह्लन्नः (prahlannaḥ) — delighted, the penult short',
           {'stem': 'hlād', 'before': 'niṣṭhā', 'part': 'upadhā'},
           note='ह्लादो निष्ठायाम् — योगविभागः क्रियते, क्तिन्यपि यथा स्यात्'),
    ),
    '6.4.96': (
        _c('उरश्छदः (uraśchadaḥ) — a breast-covering, the penult short',
           {'stem': 'chad', 'before': 'gha', 'part': 'upadhā'},
           note="छादेर्घेऽद्व्युपसर्गस्य — the rule's mere existence sets aside both 6.4.22's असिद्धत्व and 1.1.56"),
    ),
    '6.4.97': (
        _c('छत्त्रम् (chattram) — an umbrella, the penult short',
           {'stem': 'chad', 'before': 'is', 'part': 'upadhā'},
           note='इस्मन्त्रन्क्विषु च — four affixes, and the two-preverb condition dropped'),
    ),
    '6.4.98': (
        _c('जग्मुः (jagmuḥ) — they went, the penult gone',
           {'stem': 'gam', 'before': 'ac', 'part': 'upadhā', 'result': 'kṅit'},
           note='गमहनजनखनघसां लोपः क्ङित्यनङि — अगमत् is out, its affix being an अङ्'),
    ),
    '6.4.99': (
        _c('वितत्निरे (vitatnire) — they stretched out, in the Veda',
           {'stem': 'tan', 'before': 'ac', 'part': 'upadhā', 'result': 'kṅit', 'chandasi': True},
           note='तनिपत्योश्छन्दसि — छन्दसीति किम्? वितेनिरे, पेतिम'),
    ),
    '6.4.100': (
        _c('सग्धिः (sagdhiḥ) — eating together, in the Veda',
           {'stem': 'ghas', 'before': 'hal', 'part': 'upadhā', 'result': 'kṅit', 'chandasi': True},
           note='घसिभसोर्हलि च — and the vṛtti walks सग्धि through 2.4.39, this rule, and 8.2.26'),
    ),
    '6.4.101': (
        _c('जुहुधि (juhudhi) — offer thou, the हि become धि',
           {'stem': 'hu', 'gana': 'jhal-anta', 'before': 'hi', 'result': 'hal-ādi'},
           note='हुझल्भ्यो हेर्धिः — क्रीणीहि is out, being neither हु nor झल्-final'),
    ),
    '6.4.102': (
        _c('श्रुधी हवम् (śrudhī havam) — hear the call, in the Veda',
           {'stem': 'śru', 'before': 'hi', 'chandasi': True},
           note='श्रुशृणुपॄकृवृभ्यश्छन्दसि — धिभावविधानसामर्थ्याद् उतश्च प्रत्ययाद् न भवति'),
    ),
    '6.4.103': (
        _c('सोम रारन्धि (soma rārandhi) — Soma, delight us',
           {'before': 'hi', 'result': 'aṅit', 'chandasi': True},
           note='अङितश्च — वा छन्दसि इति पित्त्वेनास्याङित्त्वम्'),
    ),
    '6.4.104': (
        _c('अकारि (akāri) — it was done, the ending dropped whole',
           {'before': 'ciṇ'},
           note='चिणो लुक् — and अकारितराम् keeps its तरप्, the तिप् being gone and 6.4.22 hiding that'),
    ),
    '6.4.105': (
        _c('पच (paca) — cook thou, the हि simply gone',
           {'gana': 'a-anta', 'before': 'hi'},
           note='अतो हेः — युहि and रुहि keep theirs, and the tapara shuts the long आ out'),
    ),
    '6.4.106': (
        _c('सुनु (sunu) — press thou, the हि gone after the उ',
           {'gana': 'u-pratyaya-anta', 'before': 'hi'},
           note='उतश्च प्रत्ययादसंयोगपूर्वात् — and a vārttika makes it optional in the Veda'),
    ),
    '6.4.107': (
        _c('सुन्वः (sunvaḥ) — we two press, and सुनुवः beside it',
           {'gana': 'u-pratyaya-anta', 'before': 'va'},
           note='लोपश्चास्यान्यतरस्यां म्वोः — लुगिति वर्तमाने लोपग्रहणमन्त्यलोपार्थम्, so only the उ goes'),
    ),
    '6.4.108': (
        _c('कुर्वः (kurvaḥ) — we two do, and no second form',
           {'stem': 'kṛ', 'gana': 'u-pratyaya-anta', 'before': 'va'},
           note="नित्यं करोतेः — and 8.2.79 then names कुर् out of 8.2.77's lengthening"),
    ),
    '6.4.109': (
        _c('कुर्यात् (kuryāt) — he should do, the उ gone',
           {'stem': 'kṛ', 'gana': 'u-pratyaya-anta', 'before': 'ya'},
           note='ये च — नित्यम् still running, so no option here either'),
    ),
    '6.4.110': (
        _c('कुरुतः (kurutaḥ) — they two do, the अ become उ',
           {'stem': 'kṛ', 'gana': 'u-pratyaya-anta', 'before': 'sārvadhātuka', 'part': 'a', 'result': 'kṅit'},
           note='अत उत् सार्वधातुके — सार्वधातुकग्रहणं भूतपूर्वेऽपि सार्वधातुके यथा स्यात्, for कुरु'),
    ),
    '6.4.111': (
        _c('सन्ति (santi) — they are, the अ of अस् gone',
           {'stem': 'as', 'gana': 'śna', 'before': 'sārvadhātuka', 'part': 'a', 'result': 'kṅit'},
           note='श्नसोरल्लोपः — the rule that makes the seventh class conjugate as it does'),
    ),
    '6.4.112': (
        _c('लुनते (lunate) — they cut, the आ of श्ना gone',
           {'stem': 'śnā', 'gana': 'abhyasta', 'before': 'sārvadhātuka', 'part': 'ā', 'result': 'kṅit'},
           note='श्नाभ्यस्तयोरातः — बिभ्रति is out, having no आ to drop'),
    ),
    '6.4.113': (
        _c('लुनीतः (lunītaḥ) — they two cut, the आ become ī',
           {'gana': 'śnā-abhyasta', 'before': 'sārvadhātuka', 'part': 'ā', 'result': 'kṅit'},
           note="ई हल्यघोः — so the ninth class's ना becomes नी before a consonant and goes before a vowel"),
    ),
    '6.4.114': (
        _c('दरिद्रितः (daridritaḥ) — they two are poor, the आ become इ',
           {'stem': 'daridrā', 'before': 'sārvadhātuka', 'result': 'kṅit'},
           note='इद् दरिद्रस्य — and two vārttikas add the loss before an ārdhadhātuka and its counting as done'),
    ),
    '6.4.115': (
        _c('बिभितः (bibhitaḥ) — they two fear, and बिभीतः beside it',
           {'stem': 'bhī', 'before': 'sārvadhātuka', 'result': 'kṅit'},
           note='भियोऽन्यतरस्याम् — बिभ्यति is out, its affix beginning with a vowel'),
    ),
    '6.4.116': (
        _c('जहितः (jahitaḥ) — they two abandon, and जहीतः beside it',
           {'stem': 'hā', 'before': 'sārvadhātuka', 'result': 'kṅit'},
           note='जहातेश्च — split off so that जहाति alone carries into 6.4.117 and 6.4.118'),
    ),
    '6.4.117': (
        _c('जहाहि (jahāhi) — abandon thou, one of three attested forms',
           {'stem': 'hā', 'before': 'hi'},
           note='आ च हौ — the आ from this rule, the इ from 6.4.116 carried down, and the ई from neither'),
    ),
    '6.4.118': (
        _c('जह्यात् (jahyāt) — he should abandon, the आ gone',
           {'stem': 'hā', 'before': 'sārvadhātuka', 'result': 'ya-ādi'},
           note='लोपो यि — the third thing done to one root in four sūtras: इ, आ, and now nothing at all'),
    ),
    '6.4.119': (
        _c('देहि (dehi) — give thou, and the copy gone with it',
           {'stem': 'as', 'gana': 'ghu', 'before': 'hi'},
           note='घ्वसोरेद्धावभ्यासलोपश्च — शिदयं लोपः, तेन सर्वस्याभ्यासस्य भवति'),
    ),
    '6.4.120': (
        _c('पेचतुः (pecatuḥ) — they two cooked, and no copy left',
           {'before': 'liṭ', 'result': 'kṅit'},
           note='अत एकहल्मध्येऽनादेशादेर्लिटि — one rule replacing a vowel and deleting a syllable at once'),
    ),
    '6.4.121': (
        _c('पेचिथ (pecitha) — thou hast cooked, the copy gone',
           {'before': 'thal', 'result': 'seṭ'},
           note='थलि च सेटि — थल्ग्रहणं विस्पष्टार्थम्, no other perfect affix taking an इट् anyway'),
    ),
    '6.4.122': (
        _c('तेरतुः (teratuḥ) — they two crossed, though the conditions missed it',
           {'stem': 'tṝ', 'before': 'liṭ', 'result': 'kṅit'},
           note='तॄफलभजत्रपश्च — तरतेर्गुणार्थम्, फलिभजोरादेशाद्यर्थम्, त्रपेरनेकहल्मध्यार्थम्'),
    ),
    '6.4.123': (
        _c('अपरेधतुः (aparedhatuḥ) — they two injured',
           {'stem': 'rādh', 'before': 'liṭ', 'result': 'hiṃsā'},
           note='राधो हिंसायाम् — and the tapara of 6.4.120 is set aside, राध् having no short अ at all'),
    ),
    '6.4.124': (
        _c('जेरतुः (jeratuḥ) — they two aged, and जजरतुः beside it',
           {'stem': 'jṝ', 'before': 'liṭ'},
           note='वा जॄभ्रमुत्रसाम् — each of the three given both ways, with the copy gone and with it kept'),
    ),
    '6.4.125': (
        _c('फेणतुः (pheṇatuḥ) — they two moved, and पफणतुः beside it',
           {'gana': 'phaṇādi', 'before': 'liṭ'},
           note='फणां च सप्तानाम् — seven roots and one option, and the vṛtti works each pair out'),
    ),
    '6.4.126': (
        _c('विशशसतुः (viśaśasatuḥ) — they two cut up, and the copy kept',
           {'stem': 'śas', 'gana': 'v-ādi'},
           note='न शसददवादिगुणानाम् — and the last of the four is a class of vowels rather than of roots'),
    ),
    '6.4.127': (
        _c('अर्वतः (arvataḥ) — the coursers, अर्वन् become अर्वत्',
           {'stem': 'arvan'},
           note='अर्वणस्त्रसावनञः — two conditions in one compound, one about what follows and one about what precedes'),
    ),
    '6.4.128': (
        _c('मघवतः (maghavataḥ) — the bounteous ones, and मघोनः beside it',
           {'stem': 'maghavan'},
           note='मघवा बहुलम् — every form given twice over, which is what बहुलम् means here'),
    ),
    '6.4.129': (
        _c("द्विपदः (dvipadaḥ) — the heading's own example, at 6.4.130",
           {'stem': 'pāda'},
           note='भस्य — भस्येति किम्? द्विपादौ, द्विपादः, where a strong ending leaves the stem no भ'),
    ),
    '6.4.130': (
        _c('द्विपदः (dvipadaḥ) — two-footed, in a weak case',
           {'stem': 'pāda'},
           note="पादः पत् — and GRETIL runs the vṛtti's वक्ष्यति into the sūtra where Vidyut has the text alone"),
    ),
    '6.4.131': (
        _c('विदुषः (viduṣaḥ) — of the learned man, the वस् vocalised',
           {'gana': 'vasu-anta'},
           note='वसोः संप्रसारणम् — व्याश्रयत्वादसिद्धत्वं न भवति, and वसुग्रहणे क्वसोरपि ग्रहणमिष्यते'),
    ),
    '6.4.132': (
        _c('प्रष्ठौहः (praṣṭhauhaḥ) — of the lead ox, the वाह् vocalised',
           {'gana': 'vāha-anta'},
           note='वाह ऊठ् — and the vṛtti asks why ऊठ् at all, guṇa and 6.1.88 having reached the same shape'),
    ),
    '6.4.133': (
        _c('शुनः (śunaḥ) — of the dog, the न् vocalised',
           {'stem': 'śvan'},
           note='श्वयुवमघोनामतद्धिते — and मघवन् was made मघवत् five sūtras ago, by 6.4.128'),
    ),
    '6.4.134': (
        _c('राज्ञः (rājñaḥ) — of the king, the अ of अन् gone',
           {'gana': 'an-anta', 'part': 'a'},
           note='अल्लोपोऽनः — राजकीयम् is out, अनो नकारान्तस्यायं लोप इष्यते'),
    ),
    '6.4.135': (
        _c('औक्ष्णः (aukṣṇaḥ) — of an ox, the अ gone before अण्',
           {'stem': 'han', 'gana': 'ṣa-pūrva-an', 'before': 'aṇ', 'part': 'a'},
           note="षपूर्वहन्धृतराज्ञामणि — सामनः and वैमनः are out by 6.4.167's प्रकृतिभाव"),
    ),
    '6.4.136': (
        _c('राज्ञि (rājñi) — in the king, and राजनि beside it',
           {'gana': 'an-anta', 'before': 'ṅi', 'part': 'a'},
           note='विभाषा ङिश्योः — what 6.4.134 made compulsory is an option before these two'),
    ),
    '6.4.137': (
        _c('पर्वणा (parvaṇā) — by the joint, and the अ kept',
           {'gana': 'an-anta', 'part': 'a', 'result': 'saṃyoga-va-ma-anta'},
           note='न संयोगाद् वमन्तात् — a cluster, and one ending in one of those two sounds'),
    ),
    '6.4.138': (
        _c('दधीचः (dadhīcaḥ) — of Dadhīca, the अ gone',
           {'gana': 'ac-anta', 'part': 'a'},
           note='अचः — अच इत्ययमञ्चतिर्लुप्तनकारो गृह्यते'),
    ),
    '6.4.139': (
        _c('उदीचः (udīcaḥ) — of the northern one',
           {'stem': 'ud', 'gana': 'ac-anta'},
           note='उद ईत् — one preverb, one substitute, and the अच् taken from the rule before'),
    ),
    '6.4.140': (
        _c('कीलालपः (kīlālapaḥ) — of the nectar-drinker',
           {'gana': 'ā-anta-dhātu', 'part': 'antya'},
           note='आतो धातोः — आत इति योगविभागः, divided so that आतः may reach further than the whole sūtra could'),
    ),
    '6.4.141': (
        _c('त्मना देवेभ्यः (tmanā devebhyaḥ) — by himself, for the gods',
           {'stem': 'ātman', 'before': 'āṅ', 'part': 'ādi', 'result': 'mantra'},
           note='मन्त्रेष्वाङ्यादेरात्मनः — and a vārttika widens it, आङोऽन्यत्रापि दृश्यते'),
    ),
    '6.4.142': (
        _c('विंशकः (viṃśakaḥ) — bought for twenty, the ति gone',
           {'stem': 'viṃśati', 'before': 'ḍit', 'part': 'ti'},
           note='ति विंशतेर्डिति — डितीति किम्? विंशत्या, where no डित् follows'),
    ),
    '6.4.143': (
        _c('कुमुद्वान् (kumudvān) — lotus-bearing, the टि gone',
           {'before': 'ḍit', 'part': 'ṭi'},
           note='टेः — डित्यभस्याप्यनुबन्धकरणसामर्थ्यात् टिलोपो भवति'),
    ),
    '6.4.144': (
        _c("आग्निशर्मिः (āgniśarmiḥ) — Agniśarman's son",
           {'gana': 'n-anta', 'before': 'taddhita', 'part': 'ṭi'},
           note='नस्तद्धिते — and a vārttika adds a long list the rule would otherwise miss'),
    ),
    '6.4.145': (
        _c('द्व्यहः (dvyahaḥ) — a two-day period',
           {'stem': 'ahan', 'before': 'ṭa', 'part': 'ṭi'},
           note='अह्नष्टखोरेव — सिद्धे सत्यारम्भो नियमार्थः, so अह्ना is out'),
    ),
    '6.4.146': (
        _c("बाभ्रव्यः (bābhravyaḥ) — Babhru's descendant",
           {'gana': 'u-anta', 'before': 'taddhita'},
           note='ओर्गुणः — गुणग्रहणं संज्ञापूर्वको विधिरनित्यः यथा स्यात्, and that is how स्वायंभुव comes out'),
    ),
    '6.4.147': (
        _c("कामण्डलेयः (kāmaṇḍaleyaḥ) — of Kamaṇḍalu's line",
           {'gana': 'u-anta', 'before': 'ḍha'},
           note='ढे लोपोऽकद्र्वाः — काद्रवेयो मन्त्रमपश्यत् keeps its उ, कद्रू being named out'),
    ),
    '6.4.148': (
        _c("दाक्षी (dākṣī) — Dākṣi's daughter, the इ gone",
           {'gana': 'i-a-anta', 'before': 'ī', 'part': 'antya'},
           note="यस्येति च — stated rather than left to 6.1.101, or 1.4.7's exception for सखि would wrongly bite"),
    ),
    '6.4.149': (
        _c('सौरी बलाका (saurī balākā) — a crane facing the sun',
           {'stem': 'sūrya', 'before': 'ī', 'part': 'upadhā-ya'},
           note='सूर्यतिष्यागस्त्यमत्स्यानां य उपधायाः — and whether 6.4.22 hides it depends on which affix follows'),
    ),
    '6.4.150': (
        _c("गार्गी (gārgī) — Garga's descendant, feminine",
           {'before': 'ī', 'part': 'taddhita-ya', 'result': 'hal-pūrva'},
           note='हलस्तद्धितस्य — तद्धित इति निवृत्तम्, the taddhita now being the thing lost and not the environment'),
    ),
    '6.4.151': (
        _c('गार्गकम् (gārgakam) — a group of Gargas',
           {'before': 'taddhita', 'part': 'āpatya-ya', 'result': 'hal-pūrva'},
           note='आपत्यस्य च तद्धितेऽनाति — and तद्धितग्रहणमीत्यनापत्यस्यापि लोपार्थम्, giving सौमी इष्टिः'),
    ),
    '6.4.152': (
        _c('गार्गीयति (gārgīyati) — he wants a Gārgya',
           {'before': 'kyac', 'part': 'āpatya-ya', 'result': 'hal-pūrva'},
           note="क्यच्व्योश्च — सांकाश्यायते is out, its य being no patronymic's"),
    ),
    '6.4.153': (
        _c('बैल्वकाः (bailvakāḥ) — those of the bilva grove',
           {'gana': 'bilvakādi', 'before': 'taddhita', 'part': 'cha'},
           note="बिल्वकादिभ्यश्छस्य लुक् — the बिल्वकादि are the नडादि words with 4.2.91's कुक् already on them"),
    ),
    '6.4.154': (
        _c('करिष्ठः (kariṣṭhaḥ) — the best doer, the तृ gone whole',
           {'stem': 'tṛ', 'before': 'iṣṭhan'},
           note="तुरिष्ठेमेयस्सु — सर्वस्य तृशब्दस्य लोपार्थं वचनम्, and a लुक् would have stopped the affix's own effects"),
    ),
    '6.4.155': (
        _c('पटिष्ठः (paṭiṣṭhaḥ) — the cleverest, the टि gone',
           {'part': 'ṭi', 'before': 'iṣṭhan'},
           note='टेः — णाविष्ठवत् प्रातिपदिकस्य कार्यं भवति, which carries this run into the causal'),
    ),
    '6.4.156': (
        _c('स्थविष्ठः (sthaviṣṭhaḥ) — the stoutest, from स्थूल',
           {'stem': 'sthūla', 'part': 'yaṇ-ādi-para', 'before': 'iṣṭhan'},
           note='स्थूलदूरयुवह्रस्वक्षिप्रक्षुद्राणां यणादिपरं पूर्वस्य च गुणः — one rule doing two things'),
    ),
    '6.4.157': (
        _c('प्रेष्ठः (preṣṭhaḥ) — the dearest, प्रिय replaced by प्र',
           {'stem': 'priya', 'before': 'iṣṭhan'},
           note='प्रियस्थिरस्फिरोरुबहुलगुरुवृद्धतृप्रदीर्घवृन्दारकाणां प्रस्थस्फवर्बंहिगर्वर्षित्रब्द्राघिवृन्दाः'),
    ),
    '6.4.158': (
        _c('भूमा (bhūmā) — abundance, बहु become भू',
           {'stem': 'bahu', 'before': 'imanic'},
           note='बहोर्लोपो भू च बहोः — पुनर्ग्रहणं स्थानित्वप्रतिपत्त्यर्थम्'),
    ),
    '6.4.159': (
        _c('भूयिष्ठः (bhūyiṣṭhaḥ) — the most, with यिट् kept',
           {'stem': 'bahu', 'before': 'iṣṭhan'},
           note='इष्ठस्य यिट् च — लोपापवादो यिडागमः, तस्मिन् इकार उच्चारणार्थः'),
    ),
    '6.4.160': (
        _c('ज्यायान् (jyāyān) — the elder, the greater',
           {'stem': 'jya', 'before': 'īyasun'},
           note='ज्यादाद् ईयसः — लोपस्य यिटा व्यवहितत्वाद् आद् इत्युच्यते'),
    ),
    '6.4.161': (
        _c('प्रथिष्ठः (prathiṣṭhaḥ) — the broadest, ऋ become र',
           {'part': 'ṛ', 'before': 'iṣṭhan', 'result': 'hal-ādi-laghu'},
           note='र ऋतो हलादेर्लघोः — ऋजिष्ठः has no consonant before, कृष्णिष्ठः is not light'),
    ),
    '6.4.162': (
        _c('रजिष्ठम् (rajiṣṭham) — the straightest, in the Veda',
           {'stem': 'ṛju', 'part': 'ṛ', 'before': 'iṣṭhan', 'chandasi': True},
           note='विभाषर्जोश्छन्दसि — and ऋजिष्ठः stands beside it, the rule being optional'),
    ),
    '6.4.163': (
        _c('स्रजिष्ठः (srajiṣṭhaḥ) — the best garlanded, the stem intact',
           {'gana': 'ekāc', 'before': 'iṣṭhan'},
           note='प्रकृत्यैकाच् — एकाजिति किम्? वसिष्ठः, वसीयान्, where the stem has more than one vowel'),
    ),
    '6.4.164': (
        _c('स्राग्विणम् (srāgviṇam) — belonging to the garlanded one',
           {'gana': 'in-anta', 'before': 'aṇ'},
           note='इन्नण्यनपत्ये — दाण्डम् is out, अनुदात्तादेरञ् giving अञ् and not अण्'),
    ),
    '6.4.165': (
        _c("गाथिनः (gāthinaḥ) — Gāthin's descendant",
           {'stem': 'gāthin', 'before': 'aṇ'},
           note='गाथिविदथिकेशिगणिपणिनश्च — अपत्यार्थोऽयम् आरम्भः, and पाणिनि is one of the five'),
    ),
    '6.4.166': (
        _c("शाङ्खिनः (śāṅkhinaḥ) — Śaṅkhin's descendant",
           {'gana': 'saṃyoga-ādi-in', 'before': 'aṇ'},
           note='संयोगादिश्च — the cluster at the head of the stem is the whole condition'),
    ),
    '6.4.167': (
        _c('सामनः (sāmanaḥ) — of the Sāman, the अन् kept whole',
           {'gana': 'an-anta', 'before': 'aṇ'},
           note="अन् — अल्लोपटिलोपाव् उभाव् अपि न भवतः, which is what 6.4.135's counter-examples pointed at"),
    ),
    '6.4.168': (
        _c('सामन्यः (sāmanyaḥ) — good at the Sāman chants',
           {'gana': 'an-anta', 'before': 'ya-taddhita'},
           note='ये चाभावकर्मणोः — राज्ञो भावः कर्म वा gives राज्यम्, which the sūtra shuts out'),
    ),
    '6.4.169': (
        _c('आत्मनीनः (ātmanīnaḥ) — what is good for oneself',
           {'stem': 'ātman', 'before': 'kha'},
           note='आत्माध्वानौ खे — प्रत्यात्मम् and प्राध्वम् are out, being समासान्त and no ख'),
    ),
    '6.4.170': (
        _c("सौषामः (sauṣāmaḥ) — Suṣāman's descendant, the अन् not kept",
           {'gana': 'ma-pūrva-an', 'before': 'aṇ', 'result': 'apatya'},
           note='न मपूर्वोऽपत्येऽवर्मणः — चाक्रवर्मणः keeps its अन्, वर्मन् being named out'),
    ),
    '6.4.171': (
        _c('ब्राह्मो गर्भः (brāhmo garbhaḥ) — a Brahman embryo',
           {'stem': 'brahman', 'before': 'aṇ'},
           note='ब्राह्मोऽजातौ — योगविभागोऽत्र क्रियते, the sūtra divided so that ब्राह्म may be laid down apart'),
    ),
    '6.4.172': (
        _c('कार्मः (kārmaḥ) — one whose habit is work',
           {'stem': 'karman', 'result': 'tācchīlya'},
           note='कार्मस्ताच्छील्ये — नस्तद्धिते इत्येव टिलोपः सिद्धः, ज्ञापकार्थं तु'),
    ),
    '6.4.173': (
        _c("औक्षं पदम् (aukṣaṃ padam) — an ox's footprint",
           {'stem': 'ukṣan', 'before': 'aṇ'},
           note='औक्षमनपत्ये — उक्ष्णोऽपत्यम् औक्ष्णः, so the two rules divide उक्षन् between them by sense'),
    ),
    '6.4.174': (
        _c('दाण्डिनायनः (dāṇḍināyanaḥ) — laid down whole, the इन् kept',
           {'stem': 'dāṇḍināyana'},
           note='केषांचित् तु हस्तिन् इति नडादिषु न पठ्यते — a disagreement the vṛtti records rather than settles'),
    ),
    '6.4.175': (
        _c('ऋत्व्यम् (ṛtvyam) — what belongs to the season',
           {'stem': 'ṛtvya', 'chandasi': True},
           note='ऋत्व्यवास्त्व्यवास्त्वमाध्वीहिरण्ययानि छन्दसि — यणादेशो निपात्यते, and the adhyāya ends'),
    ),
    '7.1.1': (
        _c('नन्दनः (nandanaḥ) — the delighting one, from ल्यु',
           {'affix': 'yu'},
           note='युवोरनाकौ — प्रतिज्ञानुनासिक्याः पाणिनीयाः, so ऊर्णायुः keeps its यु'),
    ),
    '7.1.2': (
        _c("नाडायनः (nāḍāyanaḥ) — of Naḍa's line, the फ become आयन्",
           {'affix': 'pha'},
           note='आयनेयीनीयियः फढखच्छघां प्रत्ययादीनाम् — आदिग्रहणं किम्? ऊरुदघ्नम्'),
    ),
    '7.1.4': (
        _c('ददति (dadati) — they give, the झ become अत्',
           {'affix': 'jha', 'after': 'abhyasta'},
           note='अदभ्यस्तात् — अन्तादेशापवादोऽयम्, जुसादेशेन तु बाध्यते'),
    ),
    '7.1.5': (
        _c('चिन्वते (cinvate) — they gather for themselves',
           {'affix': 'jha', 'after': 'an-a-anta', 'pada': 'ātmanepada'},
           note='आत्मनेपदेष्वनतः — अनकारान्तेनाङ्गेन झकारविशेषणं किम्? इह मा भूत् — शयान्तै'),
    ),
    '7.1.6': (
        _c('शेरते (śerate) — they lie down',
           {'affix': 'jha-ādeśa', 'root': 'śīṅ'},
           note='शीङो रुट् — सानुबन्धग्रहणमयङ्लुगर्थम्, so व्यतिशेश्यते is out'),
    ),
    '7.1.7': (
        _c('संविद्रते (saṃvidrate) — they know together',
           {'affix': 'jha-ādeśa', 'root': 'vid'},
           note='वेत्तेर्विभाषा — वेत्तेरिति लुग्विकरणस्य ग्रहणम्'),
    ),
    '7.1.8': (
        _c('अदुह्र (aduhra) — they milked, in the Veda',
           {'affix': 'jha-ādeśa', 'chandasi': True},
           note='बहुलं छन्दसि — ऋदृशोऽङि गुणः इत्येतदपि बहुलवचनादेवात्र न भवति'),
    ),
    '7.1.9': (
        _c('वृक्षैः (vṛkṣaiḥ) — by the trees',
           {'ending': 'bhis', 'after': 'a-anta'},
           note='अतो भिस ऐस् — अत इत्यधिकारो जसः शी इति यावत्'),
    ),
    '7.1.10': (
        _c('नद्यैः (nadyaiḥ) — by the rivers, in the Veda',
           {'ending': 'bhis', 'chandasi': True},
           note='बहुलं छन्दसि — अतो न भवति, देवेभिः सर्वेभिः प्रोक्तम्'),
    ),
    '7.1.11': (
        _c('एभिः (ebhiḥ) — by these, the ऐस् refused',
           {'ending': 'bhis', 'stem': 'idam'},
           note='नेदमदसोरकोः — तन्मध्यपतितस्तद्ग्रहणेन गृह्यते, which the अकोः shows'),
    ),
    '7.1.12': (
        _c('वृक्षेण (vṛkṣeṇa) — by the tree',
           {'ending': 'ṭā', 'after': 'a-anta'},
           note='टाङसिङसामिनात्स्याः — यथा तु भाष्ये तथा नैतदिष्यते, on अतिजरसिना'),
    ),
    '7.1.13': (
        _c('वृक्षाय (vṛkṣāya) — for the tree',
           {'ending': 'ṅe', 'after': 'a-anta'},
           note='ङेर्यः — संनिपातलक्षणो विधिरनिमित्तं तद्विघातस्य, a maxim held not universal'),
    ),
    '7.1.14': (
        _c('सर्वस्मै (sarvasmai) — for all',
           {'ending': 'ṅe', 'after': 'sarvanāma'},
           note='सर्वनाम्नः स्मै — अन्तरङ्गत्वादेकादेशात् पूर्वं स्मैभावः क्रियते'),
    ),
    '7.1.15': (
        _c('सर्वस्मिन् (sarvasmin) — in all',
           {'ending': 'ṅi', 'after': 'sarvanāma'},
           note='ङसिङ्योः स्मात्स्मिनौ — सर्वनाम्न इत्येव, so वृक्षे stands'),
    ),
    '7.1.16': (
        _c('पूर्वात् (pūrvāt) — from the earlier one, beside पूर्वस्मात्',
           {'ending': 'ṅasi', 'stem': 'pūrva', 'after': 'sarvanāma'},
           note='पूर्वादिभ्यो नवभ्यो वा — नवभ्य इति किम्? त्यस्मात्, त्यस्मिन्'),
    ),
    '7.1.17': (
        _c('सर्वे (sarve) — all of them',
           {'ending': 'jas', 'after': 'sarvanāma'},
           note='जसः शी — दीर्घोच्चारणमुत्तरार्थम्'),
    ),
    '7.1.18': (
        _c('खट्वे तिष्ठतः (khaṭve tiṣṭhataḥ) — two cots stand',
           {'ending': 'auṅ', 'after': 'āp-anta'},
           note='औङ आपः — ङित्त्वे विद्याद् वर्णनिर्देशमात्रं, so no ङित् effect follows'),
    ),
    '7.1.19': (
        _c('कुण्डे तिष्ठतः (kuṇḍe tiṣṭhataḥ) — two bowls stand',
           {'ending': 'auṅ', 'after': 'napuṃsaka'},
           note='नपुंसकाच्च — श्यां प्रतिषेधो वक्तव्यः, holding off 6.4.148'),
    ),
    '7.1.20': (
        _c('कुण्डानि (kuṇḍāni) — the bowls',
           {'ending': 'jas', 'after': 'napuṃsaka'},
           note='जश्शसोः शिः — जसा सहचरितस्य शसो ग्रहणात्'),
    ),
    '7.1.21': (
        _c('अष्टौ तिष्ठन्ति (aṣṭau tiṣṭhanti) — eight stand',
           {'ending': 'jas', 'stem': 'aṣṭan', 'case': 'kṛta-ātva'},
           note='अष्टाभ्य औश् — षड्भ्यो लुक् इत्यस्यायमपवादः, but 2.4.71 is not set aside'),
    ),
    '7.1.22': (
        _c('षट् तिष्ठन्ति (ṣaṭ tiṣṭhanti) — six stand',
           {'ending': 'jas', 'after': 'ṣaṭ'},
           note='षड्भ्यो लुक् — षट्प्रधानात् तदन्तादपि भवति, परमषट्'),
    ),
    '7.1.23': (
        _c('दधि तिष्ठति (dadhi tiṣṭhati) — the curd stands',
           {'ending': 'su', 'after': 'napuṃsaka'},
           note='स्वमोर्नपुंसकात् — यस्य च लक्षणान्तरेण निमित्तं विहन्यते न तदनित्यं भवति'),
    ),
    '7.1.24': (
        _c('कुण्डं तिष्ठति (kuṇḍaṃ tiṣṭhati) — the bowl stands',
           {'ending': 'su', 'after': 'a-anta-napuṃsaka'},
           note='अतोऽम् — मकारः कस्माद् न क्रियते? दीर्घत्वं प्राप्नोति'),
    ),
    '7.1.25': (
        _c('कतरत् तिष्ठति (katarat tiṣṭhati) — which of the two stands',
           {'ending': 'su', 'stem': 'ḍatara'},
           note='अद्ड् डतरादिभ्यः पञ्चभ्यः — अद्ड्डित्त्वाड् डतरादीनां न लोपो नापि दीर्घता'),
    ),
    '7.1.26': (
        _c('इतरम् आण्डम् (itaram āṇḍam) — the other egg, in the Veda',
           {'ending': 'su', 'stem': 'itara', 'chandasi': True},
           note='नेतराच्छन्दसि — एकतराद्धि सर्वत्र छन्दसि भाषायां प्रतिषेध इष्यते'),
    ),
    '7.1.27': (
        _c('तव स्वम् (tava svam) — your own',
           {'ending': 'ṅas', 'stem': 'yuṣmad'},
           note='युष्मदस्मद्भ्यां ङसोऽश् — शित्करणं सर्वादेशार्थम्'),
    ),
    '7.1.28': (
        _c('तुभ्यं दीयते (tubhyaṃ dīyate) — it is given to you',
           {'ending': 'ṅe', 'stem': 'yuṣmad'},
           note='ङे प्रथमयोरम् — ङे इत्यविभक्तिकोऽयं निर्देशः'),
    ),
    '7.1.29': (
        _c('युष्मान् ब्राह्मणान् (yuṣmān brāhmaṇān) — you brahmins',
           {'ending': 'śas', 'stem': 'yuṣmad'},
           note='शसो न — the one form for every gender it stands beside'),
    ),
    '7.1.30': (
        _c('युष्मभ्यं दीयते (yuṣmabhyaṃ dīyate) — it is given to you all',
           {'ending': 'bhyas', 'stem': 'yuṣmad'},
           note='भ्यसो भ्यम् — अङ्गवृत्ते पुनर्वृत्तावविधिर्निष्ठितस्य'),
    ),
    '7.1.31': (
        _c('युष्मद् गच्छन्ति (yuṣmad gacchanti) — they go from you',
           {'ending': 'bhyas', 'stem': 'yuṣmad', 'case': 'pañcamī'},
           note='पञ्चम्या अत् — the same भ्यस् going two ways by its case'),
    ),
    '7.1.32': (
        _c('त्वद् गच्छन्ति (tvad gacchanti) — they go from you',
           {'ending': 'ṅasi', 'stem': 'yuṣmad', 'case': 'pañcamī-ekavacana'},
           note='एकवचनस्य च — पञ्चम्या अत् carried over from the sūtra before'),
    ),
    '7.1.33': (
        _c('युष्माकम् (yuṣmākam) — of you all',
           {'ending': 'sām', 'stem': 'yuṣmad', 'case': 'āgata-suṭ'},
           note='साम आकम् — तस्यैव तु भाविनः सुटो निवृत्त्यर्थम्'),
    ),
    '7.1.34': (
        _c('पपौ (papau) — he drank, the णल् become औ',
           {'what': 'ṇal', 'after': 'ā-anta'},
           note='आत औ णलः — एकादेशादनवकाशत्वादौत्वम्, द्विर्वचनादपि परत्वादेकादेशः'),
    ),
    '7.1.35': (
        _c('जीवताद् भवान् (jīvatād bhavān) — may you live',
           {'what': 'tu', 'sense': 'āśis'},
           note='तुह्योस्तातङाशिष्यन्यतरस्याम् — ङित् च पिद् न भवति, so ब्रूताद् भवान् has no ईट्'),
    ),
    '7.1.36': (
        _c('विद्वान् (vidvān) — the one who knows',
           {'what': 'śatṛ', 'root': 'vid'},
           note='विदेः शतुर्वसुः — वसोरुकारकरणं क्वसोरपि सामान्यग्रहणार्थम्'),
    ),
    '7.1.37': (
        _c('प्रकृत्य (prakṛtya) — having done, in a compound',
           {'what': 'ktvā', 'samasa': 'an-añ-pūrva'},
           note='समासेऽनञ्पूर्वे क्त्वो ल्यप् — अनञिति नञोऽन्यदनञ् नञ्सदृशमव्ययं परिगृह्यते'),
    ),
    '7.1.38': (
        _c('परिधापयित्वा (paridhāpayitvā) — having clothed, in the Veda',
           {'what': 'ktvā', 'samasa': 'an-añ-pūrva', 'chandasi': True},
           note='क्त्वाऽपि छन्दसि — वा छन्दसीति नोक्तं सर्वोपाधिव्यभिचारार्थम्'),
    ),
    '7.1.39': (
        _c('ऋजवः सन्तु पन्थाः (ṛjavaḥ santu panthāḥ) — may the paths be straight',
           {'what': 'sup', 'chandasi': True},
           note='सुपां सुलुक्० — सुपां सुपो भवन्ति, तिङां तिङो भवन्ति, both by vārttika'),
    ),
    '7.1.40': (
        _c('वधीं वृत्रम् (vadhīṃ vṛtram) — I slew Vṛtra',
           {'what': 'am', 'chandasi': True},
           note='अमो मश् — शित्करणं सर्वादेशार्थम्'),
    ),
    '7.1.41': (
        _c('देवा अदुह्र (devā aduhra) — the gods milked',
           {'what': 'ta', 'after': 'ātmanepada', 'chandasi': True},
           note='लोपस्त आत्मनेपदेषु — उत्सं दुहन्ति कलशम् is परस्मैपद, and keeps its त्'),
    ),
    '7.1.42': (
        _c('वारयध्वात् (vārayadhvāt) — hold it back',
           {'what': 'dhvam', 'chandasi': True},
           note='ध्वमो ध्वात् — वारयध्वमिति प्राप्ते'),
    ),
    '7.1.43': (
        _c('यजध्वैनम् (yajadhvainam) — worship him',
           {'what': 'yajadhvam', 'before': 'enam', 'chandasi': True},
           note='यजध्वैनमिति च — मकारलोपो निपात्यते वकारस्य च यकारः'),
    ),
    '7.1.44': (
        _c('कृणुतात् (kṛṇutāt) — make it, in the Veda',
           {'what': 'ta', 'chandasi': True},
           note='तस्य तात् — कृणुतेति प्राप्ते, and so for all four'),
    ),
    '7.1.45': (
        _c('शृणोत ग्रावाणः (śṛṇota grāvāṇaḥ) — hear, you stones',
           {'what': 'ta', 'chandasi': True, 'wants': 'tap-tanap-tan-than'},
           note='तप्तनप्तनथनाश्च — पित्करणमङित्त्वार्थम्'),
    ),
    '7.1.46': (
        _c('उद्दीपयामसि (uddīpayāmasi) — we kindle up',
           {'what': 'masi', 'chandasi': True},
           note='इदन्तो मसि — स च तस्यान्तो भवति, तद्ग्रहणेन गृह्यत इत्यर्थः'),
    ),
    '7.1.47': (
        _c('दत्त्वाय (dattvāya) — having given, in the Veda',
           {'what': 'ktvā', 'samasa': 'an-añ-pūrva', 'chandasi': True, 'wants': 'yak'},
           note='क्त्वो यक् — समास इति तत्रानुवर्तते, which is why it stands here'),
    ),
    '7.1.48': (
        _c('इष्ट्वीनं देवान् (iṣṭvīnaṃ devān) — having worshipped the gods',
           {'what': 'iṣṭvīnam', 'chandasi': True},
           note='इष्ट्वीनमिति च — चकारस्यानुक्तसमुच्चयार्थत्वात् सिद्धम्'),
    ),
    '7.1.49': (
        _c('स्नात्वी मलादिव (snātvī malādiva) — as if bathed of impurity',
           {'what': 'snātvī', 'chandasi': True},
           note='स्नात्व्यादयश्च — प्रकारार्थोऽयमादिशब्दः, so the class is open'),
    ),
    '7.1.50': (
        _c('ब्राह्मणासः पितरः (brāhmaṇāsaḥ pitaraḥ) — the brahmin fathers',
           {'what': 'jas', 'after': 'a-varṇa-anta', 'chandasi': True},
           note='आज्जसेरसुक् — सकृद्गतौ विप्रतिषेधे यद् बाधितं तद् बाधितमेव'),
    ),
    '7.1.51': (
        _c('अश्वस्यति वडवा (aśvasyati vaḍavā) — the mare wants a stallion',
           {'ending': 'kyac', 'stem': 'aśva', 'sense': 'ātma-prīti'},
           note='अश्वक्षीरवृषलवणानामात्मप्रीतौ क्यचि — अश्ववृषयोर्मैथुनेच्छायाम्, क्षीरलवणयोर्लालसायाम्'),
    ),
    '7.1.52': (
        _c('सर्वेषाम् (sarveṣām) — of all of them',
           {'ending': 'ām', 'after': 'a-varṇa-sarvanāma'},
           note='आमि सर्वनाम्नः सुट् — सानुबन्धकाविति वा तौ न गृह्येते'),
    ),
    '7.1.53': (
        _c('त्रयाणाम् (trayāṇām) — of the three',
           {'ending': 'ām', 'stem': 'tri'},
           note='त्रेस्त्रयः — त्रीवामित्यपि छन्दसीष्यते'),
    ),
    '7.1.54': (
        _c('वृक्षाणाम् (vṛkṣāṇām) — of the trees',
           {'ending': 'ām', 'after': 'hrasva-nadī-āp'},
           note='ह्रस्वनद्यापो नुट् — three conditions, and the vṛtti works every one'),
    ),
    '7.1.55': (
        _c('षण्णाम् (ṣaṇṇām) — of the six',
           {'ending': 'ām', 'after': 'ṣaṭ-catur'},
           note='षट्चतुर्भ्यश्च — रेफान्तायाः संख्यायाः षट्संज्ञा न विहिता'),
    ),
    '7.1.56': (
        _c('श्रीणाम् (śrīṇām) — of the splendours, in the Veda',
           {'ending': 'ām', 'stem': 'śrī', 'chandasi': True},
           note='श्रीग्रामण्योश्छन्दसि — वामीति विकल्पेन नदीसंज्ञा, तत्र नित्यार्थं वचनम्'),
    ),
    '7.1.57': (
        _c("गोनाम् (gonām) — of the cattle, at a verse-quarter's end",
           {'ending': 'ām', 'stem': 'go', 'before': 'pāda-anta', 'chandasi': True},
           note='गोः पादान्ते — सर्वे विधयश्छन्दसि विकल्प्यन्ते'),
    ),
    '7.1.58': (
        _c('कुण्डिता (kuṇḍitā) — one who makes round',
           {'gana': 'idit-dhātu'},
           note='इदितो नुम् धातोः — अयं धातूपदेशावस्थायामेव नुमागमो भवति'),
    ),
    '7.1.59': (
        _c('मुञ्चति (muñcati) — he releases',
           {'stem': 'muc', 'before': 'śa'},
           note='शे मुचादीनाम् — शे तृम्फादीनामुपसंख्यानं कर्तव्यम्, and स च विधानसामर्थ्याद् न लुप्यते'),
    ),
    '7.1.60': (
        _c('मङ्क्ता (maṅktā) — one who sinks',
           {'stem': 'masj', 'before': 'jhal'},
           note='मस्जिनशोर्झलि — मस्जेरन्त्यात् पूर्वं नुममिच्छन्त्यनुषङ्गादिलोपार्थम्'),
    ),
    '7.1.61': (
        _c('रन्धयति (randhayati) — he destroys',
           {'stem': 'radh', 'before': 'ac'},
           note='रधिजभोरचि — परापि सती वृद्धिर्नुमा बाध्यते, नित्यत्वात्'),
    ),
    '7.1.62': (
        _c('रधिता (radhitā) — one who destroys, without the nasal',
           {'stem': 'radh', 'before': 'iṭ'},
           note='नेट्यलिटि रधेः — विपरीतमप्यवधारणं संभाव्येत'),
    ),
    '7.1.63': (
        _c('आरम्भयति (ārambhayati) — he causes to begin',
           {'stem': 'rabh', 'before': 'ac'},
           note='रभेरशब्लिटोः — आरभते, आरेभे are what the two exclusions keep out'),
    ),
    '7.1.64': (
        _c('लम्भयति (lambhayati) — he causes to obtain',
           {'stem': 'labh', 'before': 'ac'},
           note='लभेश्च — लभेश्च पृथग्योगकरणमुत्तरार्थम्'),
    ),
    '7.1.65': (
        _c('आलम्भ्या गौः (ālambhyā gauḥ) — a cow fit for sacrifice',
           {'stem': 'labh', 'upasarga': 'āṅ', 'before': 'ya-ādi'},
           note='आङो यि — प्राक् प्रत्ययोत्पत्तेर्नुमि कृते विहतमदुपधत्वम्'),
    ),
    '7.1.66': (
        _c('उपलम्भ्या विद्या (upalambhyā vidyā) — knowledge worth gaining',
           {'stem': 'labh', 'upasarga': 'upa', 'before': 'ya-ādi', 'sense': 'praśaṃsā'},
           note='उपात् प्रशंसायाम् — प्रशंसायामिति किम्? उपलभ्यमस्माद् वृषलात् किंचित्'),
    ),
    '7.1.67': (
        _c('ईषत्प्रलम्भः (īṣatpralambhaḥ) — easily obtained',
           {'stem': 'labh', 'upasarga': 'upasarga', 'before': 'khal'},
           note='उपसर्गात् खल्घञोः — सिद्धे सत्यारम्भो नियमार्थः'),
    ),
    '7.1.68': (
        _c('सुलभम् (sulabham) — easy to get',
           {'stem': 'labh', 'upasarga': 'su-dur-kevala', 'before': 'khal'},
           note='न सुदुर्भ्यां केवलाभ्याम् — अतिसुलम्भः, where अति is a preverb and not a कर्मप्रवचनीय'),
    ),
    '7.1.69': (
        _c('अलम्भि (alambhi) — it was obtained, beside अलाभि',
           {'stem': 'labh', 'before': 'ciṇ'},
           note='विभाषा चिण्णमुलोः — व्यवस्थितविभाषा चेयम्, प्रालम्भि being compulsory'),
    ),
    '7.1.70': (
        _c('भवान् (bhavān) — your honour, in the nominative',
           {'gana': 'ugit-añcati', 'before': 'sarvanāmasthāna'},
           note='उगिदचां सर्वनामस्थानेऽधातोः — अधातुभूतपूर्वस्यापि यथा स्यात्, giving गोमान्'),
    ),
    '7.1.71': (
        _c('युङ् (yuṅ) — the yoked one',
           {'stem': 'yuj', 'before': 'sarvanāmasthāna'},
           note='युजेरसमासे — युजेरितीकारनिर्देशाद् युज समाधौ इत्यस्य ग्रहणं न भवति'),
    ),
    '7.1.72': (
        _c('यशांसि (yaśāṃsi) — glories',
           {'gender': 'napuṃsaka', 'gana': 'jhal-ac-anta', 'before': 'sarvanāmasthāna'},
           note='नपुंसकस्य झलचः — परत्वादनेनैव नुम् भवति, giving श्रेयांसि'),
    ),
    '7.1.73': (
        _c('त्रपुणी (trapuṇī) — two pieces of tin',
           {'gender': 'napuṃsaka', 'gana': 'ik-anta', 'before': 'ac-ādi-vibhakti'},
           note='इकोऽचि विभक्तौ — एतदेवाज्ग्रहणं ज्ञापकं प्रत्ययलक्षणप्रतिषेधोऽत्र न भवतीति'),
    ),
    '7.1.74': (
        _c('ग्रामण्या ब्राह्मणकुलेन (grāmaṇyā brāhmaṇakulena) — by the leading family',
           {'gender': 'napuṃsaka', 'gana': 'bhāṣitapuṃska-ik-anta', 'before': 'tṛtīyā-ādi-ac'},
           note='तृतीयादिषु भाषितपुंस्कं पुंवद्गालवस्य — यथा पुंसि ह्रस्वनुमौ न भवतः'),
    ),
    '7.1.75': (
        _c('अस्थ्ना (asthnā) — with the bone',
           {'gender': 'napuṃsaka', 'before': 'tṛtīyā-ādi-ac', 'stem': 'asthi'},
           note='अस्थिदधिसक्थ्यक्ष्णामनङुदात्तः — स्थानिवद्भावादनुदात्तः स्यादित्युदात्तवचनम्'),
    ),
    '7.1.76': (
        _c("दधीचो अस्थभिः (dadhīco asthabhiḥ) — with Dadhīca's bones",
           {'chandasi': True, 'stem': 'asthi'},
           note='छन्दस्यपि दृश्यते — यत्र विहितस्ततोऽन्यत्रापि दृश्यते'),
    ),
    '7.1.77': (
        _c('अक्षी ते इन्द्र (akṣī te indra) — your two eyes, Indra',
           {'before': 'dvivacana', 'chandasi': True, 'stem': 'akṣi'},
           note='ई च द्विवचने — सकृद्गतौ विप्रतिषेधे यद् बाधितं तद् बाधितमेव'),
    ),
    '7.1.78': (
        _c('ददत् (dadat) — giving, with no nasal',
           {'gana': 'abhyasta', 'stem': 'śatṛ'},
           note='नाभ्यस्ताच्छतुः — व्यवहितस्यापि नुमः प्रतिषेधो विज्ञायते'),
    ),
    '7.1.79': (
        _c('ददन्ति कुलानि (dadanti kulāni) — the families giving',
           {'gana': 'abhyasta', 'gender': 'napuṃsaka', 'stem': 'śatṛ'},
           note='वा नपुंसकस्य — ददति, ददन्ति कुलानि, both standing'),
    ),
    '7.1.80': (
        _c('तुदती कुले (tudatī kule) — two striking families',
           {'gana': 'a-varṇa-anta', 'before': 'śī', 'stem': 'śatṛ'},
           note='आच्छीनद्योर्नुम् — केचिदाहुः, अपरे पुनराहुः, and the vṛtti chooses neither'),
    ),
    '7.1.81': (
        _c('पचन्ती ब्राह्मणी (pacantī brāhmaṇī) — the cooking brahmin woman',
           {'gana': 'śap-śyan', 'before': 'śī', 'stem': 'śatṛ'},
           note='शप्श्यनोर्नित्यम् — नित्यग्रहणं वेत्यस्याधिकारस्य निवृत्त्यर्थम्'),
    ),
    '7.1.82': (
        _c('अनड्वान् (anaḍvān) — the ox',
           {'before': 'su', 'stem': 'anaḍuh'},
           note='सावनडुहः — केचिदादित्यधिकारादाममोः कृतयोर्नुमं कुर्वन्ति'),
    ),
    '7.1.83': (
        _c('ईदृङ् (īdṛṅ) — of such a kind, in the Veda',
           {'before': 'su', 'chandasi': True, 'stem': 'dṛk'},
           note='दृक्स्ववस्स्वतवसां छन्दसि — स्वतवाँः पायुरग्ने'),
    ),
    '7.1.84': (
        _c('द्यौः (dyauḥ) — the sky, in the nominative',
           {'stem': 'div', 'before': 'su'},
           note='दिव औत् — दिविति प्रातिपदिकमस्ति निरनुबन्धकम्'),
    ),
    '7.1.85': (
        _c('पन्थाः (panthāḥ) — the road, in the nominative',
           {'stem': 'pathin', 'before': 'su'},
           note='पथिमथ्यृभुक्षामात् — भाव्यमानेन सवर्णानां ग्रहणं न भवति'),
    ),
    '7.1.86': (
        _c('पन्थानौ (panthānau) — two roads',
           {'stem': 'pathin', 'part': 'i', 'before': 'sarvanāmasthāna'},
           note='इतोऽत् सर्वनामस्थाने — पुनरद्वचनं षपूर्वार्थम्, giving ऋभुक्षणम्'),
    ),
    '7.1.87': (
        _c('पन्थानः (panthānaḥ) — the roads',
           {'stem': 'pathin', 'part': 'th', 'before': 'sarvanāmasthāna'},
           note='थो न्थः — and 7.1.85 and 7.1.86 must both have applied first'),
    ),
    '7.1.88': (
        _c('पथः (pathaḥ) — of the road',
           {'stem': 'pathin', 'part': 'ṭi', 'result': 'bha'},
           note='भस्य टेर्लोपः — सर्वनामस्थानमनुवर्तमानमपि विरोधादिह न सम्बध्यते'),
    ),
    '7.1.89': (
        _c('पुमान् (pumān) — a man',
           {'stem': 'puṃs', 'before': 'sarvanāmasthāna'},
           note="पुंसोऽसुङ् — असुङ्युपदेशिवद्वचनं कर्तव्यम्, for परमपुमान्'s accent"),
    ),
    '7.1.90': (
        _c('गौः (gauḥ) — the cow',
           {'stem': 'go', 'before': 'sarvanāmasthāna'},
           note='गोतो णित् — केचिद् ओतो णित् इति पठन्ति, for द्यौः, द्यावौ'),
    ),
    '7.1.91': (
        _c('अहं चकार (ahaṃ cakāra) — I did it, beside अहं चकर',
           {'stem': 'ṇal', 'result': 'uttama'},
           note='णलुत्तमो वा — णित्कार्यं तत्र वा भवतीत्यर्थः'),
    ),
    '7.1.92': (
        _c('सखायौ (sakhāyau) — two friends',
           {'stem': 'sakhi', 'before': 'sarvanāmasthāna'},
           note='सख्युरसम्बुद्धौ — असंबुद्धाविति किम्? हे सखे'),
    ),
    '7.1.93': (
        _c('सखा (sakhā) — a friend',
           {'stem': 'sakhi', 'before': 'su'},
           note='अनङ् सौ — स चेत् सुशब्दः संबुद्धिर्न भवति'),
    ),
    '7.1.94': (
        _c('कर्ता (kartā) — the doer',
           {'gana': 'ṛ-anta', 'before': 'su'},
           note='ऋदुशनस्पुरुदंसोऽनेहसां च — संबोधने तूशनसस्त्रिरूपं सान्तं तथा नान्तमथाप्यदन्तम्'),
    ),
    '7.1.95': (
        _c('क्रोष्टा (kroṣṭā) — the jackal',
           {'stem': 'kroṣṭu', 'before': 'sarvanāmasthāna'},
           note='तृज्वत् क्रोष्टुः — रूपातिदेशोऽयम्, प्रत्यासत्तेश्च क्रुशेरेव'),
    ),
    '7.1.96': (
        _c('क्रोष्ट्री (kroṣṭrī) — a she-jackal',
           {'stem': 'kroṣṭu', 'result': 'strī'},
           note='स्त्रियां च — असर्वनामस्थानार्थमारम्भः, तत्र प्रतिविधेयम्'),
    ),
    '7.1.97': (
        _c('क्रोष्ट्रा (kroṣṭrā) — by the jackal, beside क्रोष्टुना',
           {'stem': 'kroṣṭu', 'before': 'tṛtīyā-ādi-ac'},
           note='विभाषा तृतीयाऽऽदिष्वचि — तृज्वद्भावात् पूर्वविप्रतिषेधेन नुम्नुटौ भवतः'),
    ),
    '7.1.98': (
        _c('चत्वारः (catvāraḥ) — four of them',
           {'stem': 'catur', 'before': 'sarvanāmasthāna'},
           note='चतुरनडुहोरामुदात्तः — अनडुहः स्त्रियां वेति वक्तव्यम्'),
    ),
    '7.1.99': (
        _c('हे प्रियचत्वः (he priyacatvaḥ) — O you who like four',
           {'stem': 'catur', 'before': 'sambuddhi'},
           note='अम् सम्बुद्धौ — पूर्वस्यायमपवादः'),
    ),
    '7.1.100': (
        _c('किरति (kirati) — he scatters',
           {'gana': 'ṝ-anta-dhātu', 'part': 'ṝ'},
           note='ॠत इद्धातोः — लाक्षणिकस्याप्यत्र ग्रहणमिष्यते, giving चिकीर्षति'),
    ),
    '7.1.101': (
        _c('कीर्तयति (kīrtayati) — he proclaims',
           {'gana': 'ṝ-upadha-dhātu', 'part': 'ṝ-upadhā'},
           note='उपधायाश्च — the इ carried over, the position new'),
    ),
    '7.1.102': (
        _c('पूर्ताः पिण्डाः (pūrtāḥ piṇḍāḥ) — the balls once filled',
           {'gana': 'oṣṭhya-pūrva-ṝ-anta', 'part': 'ṝ'},
           note='उदोष्ठ्यपूर्वस्य — इत्त्वोत्त्वाभ्यां गुणवृद्धी भवतो विप्रतिषेधेन'),
    ),
    '7.1.103': (
        _c('मित्रावरुणा ततुरिम् (mitrāvaruṇā taturim) — Mitra and Varuṇa, the crosser',
           {'gana': 'ṝ-anta-dhātu', 'chandasi': True},
           note='बहुलं छन्दसि — ओष्ठ्यपूर्वस्यापि न भवति, पप्रितमम्, वव्रितमम्'),
    ),
    '7.2.1': (
        _c('अचैषीत् (acaiṣīt) — he gathered',
           {'gana': 'ik-anta', 'before': 'sic', 'pada': 'parasmaipada'},
           note='सिचि वृद्धिः परस्मैपदेषु — अन्तरङ्गमपि गुणमेषां वृद्धिर्वचनाद् बाधते'),
    ),
    '7.2.2': (
        _c('अक्षारीत् (akṣārīt) — it flowed',
           {'gana': 'r-l-anta', 'part': 'a', 'before': 'sic', 'pada': 'parasmaipada'},
           note='अतो र्लान्तस्य — अतो हलादेर्लघोः इति विकल्पस्यायमपवादः'),
    ),
    '7.2.3': (
        _c('अवादीत् (avādīt) — he spoke',
           {'gana': 'hal-anta', 'part': 'ac', 'before': 'sic', 'pada': 'parasmaipada'},
           note='वदव्रजहलन्तस्याचः — हल्ग्रहणं हल्समुदायपरिग्रहार्थम्, giving अराङ्क्षीत्'),
    ),
    '7.2.4': (
        _c('अदेवीत् (adevīt) — he played',
           {'gana': 'hal-anta', 'before': 'iṭ-sic'},
           note='नेटि — अन्तरङ्गमपि गुणं वचनारम्भसामर्थ्यात् सिचि वृद्धिर्बाधते'),
    ),
    '7.2.5': (
        _c('अग्रहीत् (agrahīt) — he seized',
           {'gana': 'hmy-anta', 'before': 'iṭ-sic', 'pada': 'parasmaipada'},
           note='ह्म्यन्तक्षणश्वसजागृणिश्व्येदिताम् — सा च नेटि इति न प्रतिषिध्यते'),
    ),
    '7.2.6': (
        _c('प्रौर्णवीत् (praurṇavīt) — he covered over',
           {'stem': 'ūrṇu', 'before': 'iṭ-sic', 'pada': 'parasmaipada'},
           note='ऊर्णोतेर्विभाषा — ङित्त्वपक्षे तु गुणवृद्ध्योरभाव उवङ् भवति'),
    ),
    '7.2.7': (
        _c('अकणीत् (akaṇīt) — it sounded, beside अकाणीत्',
           {'gana': 'hal-ādi', 'part': 'laghu-a', 'before': 'iṭ-sic', 'pada': 'parasmaipada'},
           note='अतो हलादेर्लघोः — तत्राज्लक्षणा वृद्धिरिग्लक्षणा न भवतीति क्ङिति च इति प्रतिषेधो न स्यात्'),
    ),
    '7.2.8': (
        _c('ईश्वरः (īśvaraḥ) — the lord, without an इट्',
           {'before': 'vaś-kṛt'},
           note='नेड् वशि कृति — वरमनादौ इत्युदाहरणप्रदर्शनार्थम्, न परिगणनम्'),
    ),
    '7.2.9': (
        _c('तन्तिः (tantiḥ) — a cord, without an इट्',
           {'before': 'ti'},
           note='तितुत्रतथसिसुसरकसेषु च — औणादिकस्यैव तशब्दस्य ग्रहणमिष्यते, न पुनः क्तस्य'),
    ),
    '7.2.10': (
        _c('दाता (dātā) — the giver, without an इट्',
           {'gana': 'ekāc-anudātta'},
           note='एकाच उपदेशेऽनुदात्तात् — के पुनरुपदेशेऽनुदात्ताः? ये तथा गणे पठ्यन्ते'),
    ),
    '7.2.11': (
        _c('श्रितः (śritaḥ) — resorted to, without an इट्',
           {'root': 'śri', 'before': 'kit'},
           note='श्र्युकः किति — उपदेश इत्येव, तीर्ण इत्यत्रापि यथा स्यात्'),
    ),
    '7.2.12': (
        _c('जिघृक्षति (jighṛkṣati) — he wants to seize',
           {'root': 'grah', 'before': 'san'},
           note='सनि ग्रहगुहोश्च — ग्रहेर्नित्यं प्राप्तः, गुहेरूदित्त्वाद् विकल्पः'),
    ),
    '7.2.13': (
        _c('चकृव (cakṛva) — we two did, without an इट्',
           {'root': 'kṛ', 'before': 'liṭ'},
           note='कृसृभृवृस्तुद्रुस्रुश्रुवो लिटि — क्रादय एव लिट्यनिटस्ततोऽन्ये सेटः'),
    ),
    '7.2.14': (
        _c('शूनः (śūnaḥ) — swollen, without an इट्',
           {'root': 'śvi', 'before': 'niṣṭhā'},
           note='श्वीदितो निष्ठायाम् — निष्ठायामित्यधिकार आर्धधातुकस्येड् वलादेः इति यावत्'),
    ),
    '7.2.15': (
        _c('विधूतः (vidhūtaḥ) — shaken off, without an इट्',
           {'gana': 'vibhāṣā-iṭ', 'before': 'niṣṭhā'},
           note='यस्य विभाषा — पतेर्विभाषितेट्कस्यापि निपातनादिडागमः'),
    ),
    '7.2.16': (
        _c('मिन्नः (minnaḥ) — moistened, without an इट्',
           {'gana': 'ādit', 'before': 'niṣṭhā'},
           note='आदितश्च — यदुपाधेर्विभाषा तदुपाधेः प्रतिषेध इति'),
    ),
    '7.2.17': (
        _c('मिन्नमनेन (minnamanena) — moistened by him',
           {'gana': 'ādit', 'before': 'niṣṭhā', 'sense': 'bhāva-ādikarman'},
           note='विभाषा भावादिकर्मणोः — सौनागाः कर्मणि निष्ठायां शकेरिटमिच्छन्ति विकल्पेन'),
    ),
    '7.2.18': (
        _c('क्षुब्धो मन्थः (kṣubdho manthaḥ) — the churning-stick',
           {'root': 'kṣubdha', 'before': 'niṣṭhā'},
           note='क्षुब्धस्वान्तध्वान्त० — क्षुभितमन्यत्, क्षुभितं मन्थेन'),
    ),
    '7.2.19': (
        _c("धृष्टोऽयम् (dhṛṣṭo'yam) — this one is bold",
           {'root': 'dhṛṣ', 'before': 'niṣṭhā', 'sense': 'vaiyātya'},
           note='धृषिशसी वैयात्ये — नियमार्थं वचनम्, धृषिशस्योर्वैयात्य एवेड् न भवति'),
    ),
    '7.2.20': (
        _c('दृढो बलवान् (dṛḍho balavān) — firm, strong',
           {'root': 'dṛḍha', 'before': 'niṣṭhā', 'sense': 'sthūla-bala'},
           note='दृढः स्थूलबलयोः — हलोपनिपातनं पूर्वत्रासिद्धत्वनिवृत्त्यर्थम्'),
    ),
    '7.2.21': (
        _c('परिवृढः कुटुम्बी (parivṛḍhaḥ kuṭumbī) — the head of a household',
           {'root': 'parivṛḍha', 'before': 'niṣṭhā', 'sense': 'prabhu'},
           note='प्रभौ परिवृढः — पूर्वेण तुल्यमेतत्'),
    ),
    '7.2.22': (
        _c('कष्टं व्याकरणम् (kaṣṭaṃ vyākaraṇam) — grammar is hard',
           {'root': 'kaṣ', 'before': 'niṣṭhā', 'sense': 'kṛcchra-gahana'},
           note='कृच्छ्रगहनयोः कषः — कषितं सुवर्णम्, where neither sense holds'),
    ),
    '7.2.23': (
        _c('घुष्टा रज्जुः (ghuṣṭā rajjuḥ) — the rope, rubbed',
           {'root': 'ghuṣ', 'before': 'niṣṭhā', 'sense': 'a-viśabdana'},
           note='घुषिरविशब्दने — विशब्दनप्रतिषेधश्च ज्ञापकश्चुरादिणिज् विशब्दनार्थस्यानित्य इति'),
    ),
    '7.2.24': (
        _c('समर्णः (samarṇaḥ) — afflicted',
           {'root': 'ard', 'upasarga': 'sam', 'before': 'niṣṭhā'},
           note='अर्देः संनिविभ्यः — संनिविभ्य इति किम्? अर्दितः'),
    ),
    '7.2.25': (
        _c('अभ्यर्णा सेना (abhyarṇā senā) — the army close at hand',
           {'root': 'ard', 'upasarga': 'abhi', 'before': 'niṣṭhā', 'sense': 'āvidūrya'},
           note='अभेश्चाविदूर्ये — विदूरं विप्रकृष्टम्, ततोऽन्यदविदूरम्'),
    ),
    '7.2.26': (
        _c('वृत्तं पारायणम् (vṛttaṃ pārāyaṇam) — the recitation completed',
           {'root': 'vṛt', 'before': 'niṣṭhā', 'sense': 'adhyayana'},
           note='णेरध्ययने वृत्तम् — अपरे तु वर्तितो गुणो देवदत्तेनेत्यपीच्छन्ति'),
    ),
    '7.2.27': (
        _c('दान्तः (dāntaḥ) — tamed, beside दमितः',
           {'root': 'dam', 'gana': 'ṇyanta', 'before': 'niṣṭhā'},
           note='वा दान्तशान्तपूर्णदस्तस्पष्टच्छन्नज्ञप्ताः — इट्प्रतिषेधो णिलुक् च निपात्यते'),
    ),
    '7.2.28': (
        _c('रुष्टः (ruṣṭaḥ) — angered, beside रुषितः',
           {'root': 'ruṣ', 'before': 'niṣṭhā'},
           note='रुष्यमत्वरसंघुषास्वनाम् — परत्वादयमेव विकल्पो भवति'),
    ),
    '7.2.29': (
        _c('हृष्टानि लोमानि (hṛṣṭāni lomāni) — the hair bristling',
           {'root': 'hṛṣ', 'before': 'niṣṭhā', 'sense': 'loman'},
           note='हृषेर्लोमसु — तयोरुभयोरिह ग्रहणमित्युभयत्रविभाषेयम्'),
    ),
    '7.2.30': (
        _c("अपचितोऽनेन गुरुः (apacito'nena guruḥ) — the teacher honoured by him",
           {'root': 'apacita', 'before': 'niṣṭhā'},
           note='अपचितश्च — क्तिनि नित्यमिति वक्तव्यम्, अपचितिः'),
    ),
    '7.2.31': (
        _c('अह्रुतमसि हविर्धानम् (ahrutamasi havirdhānam) — you are the unbent oblation-holder',
           {'root': 'hvṛ', 'before': 'niṣṭhā', 'chandasi': True},
           note='ह्रु ह्वरेश्छन्दसि — छन्दसीति किम्? ह्वृतम्'),
    ),
    '7.2.32': (
        _c('अपरिह्वृताः सनुयाम वाजम् (aparihvṛtāḥ sanuyāma vājam) — unswerving, may we win the prize',
           {'root': 'aparihvṛta', 'chandasi': True},
           note='अपरिह्वृताश्च — ह्रु इत्येतस्यादेशस्याभावो निपात्यते'),
    ),
    '7.2.33': (
        _c('मा नः सोमो ह्वरितः (mā naḥ somo hvaritaḥ) — let our Soma not go astray',
           {'root': 'hvṛ', 'before': 'niṣṭhā', 'sense': 'soma', 'chandasi': True},
           note='सोमे ह्वरितः — इडागमो गुणश्च निपात्यते छन्दसि विषये'),
    ),
    '7.2.34': (
        _c('ग्रसितं वा एतत् सोमस्य (grasitaṃ vā etat somasya) — this is a swallowing of Soma',
           {'root': 'grasita', 'chandasi': True},
           note='ग्रसितस्कभितस्तभितोत्तभित० — उत्पूर्वस्य निपातनसामर्थ्यादन्योपसर्गपूर्वः स्तभितशब्दो न भवति'),
    ),
    '7.2.35': (
        _c('लविता (lavitā) — the cutter',
           {'before': 'val-ādi-ārdhadhātuka'},
           note='आर्धधातुकस्येड् वलादेः — इडिति वर्तमाने पुनरिड्ग्रहणं प्रतिषेधनिवृत्त्यर्थम्'),
    ),
    '7.2.36': (
        _c('प्रस्नविता (prasnavitā) — one who flows forth',
           {'root': 'snu', 'before': 'val-ādi-ārdhadhātuka'},
           note='स्नुक्रमोरनात्मनेपदनिमित्ते — प्रतिषेधफलं चेदं सूत्रम्'),
    ),
    '7.2.37': (
        _c('ग्रहीता (grahītā) — the seizer',
           {'root': 'grah'},
           note='ग्रहोऽलिटि दीर्घः — अलिटीति किम्? जगृहिव, जगृहिम'),
    ),
    '7.2.38': (
        _c('वरिता (varitā) — the chooser, beside वरीता',
           {'root': 'vṛ'},
           note='वॄतो वा — वृ इति वृङ्वृञोः सामान्येन ग्रहणम्'),
    ),
    '7.2.39': (
        _c('विवरिषीष्ट (vivariṣīṣṭa) — may he choose',
           {'root': 'vṛ', 'before': 'liṅ'},
           note='न लिङि — the short इ only, the option not reaching'),
    ),
    '7.2.40': (
        _c('अतारिष्टाम् (atāriṣṭām) — those two crossed',
           {'root': 'vṛ', 'before': 'sic', 'pada': 'parasmaipada'},
           note='सिचि च परस्मैपदेषु — परस्मैपदेष्विति किम्? प्रावरिष्ट, प्रावरीष्ट'),
    ),
    '7.2.41': (
        _c('विवरिषते (vivariṣate) — he wants to choose',
           {'root': 'vṛ', 'before': 'san'},
           note='इट् सनि वा — सनि ग्रहगुहोश्च इतीट्प्रतिषेधे प्राप्ते पक्ष इडागमो विधीयते'),
    ),
    '7.2.42': (
        _c('अवृत (avṛta) — he chose, beside अवरिष्ट',
           {'root': 'vṛ', 'before': 'sic', 'pada': 'ātmanepada'},
           note='लिङ्सिचोरात्मनेपदेषु — असंभवाद् यासुटोऽवलादित्वादिति'),
    ),
    '7.2.43': (
        _c('ध्वृषीष्ट (dhvṛṣīṣṭa) — may he bend',
           {'gana': 'ṛ-anta-saṃyoga-ādi', 'before': 'liṅ', 'pada': 'ātmanepada'},
           note='ऋतश्च संयोगादेः — संयोगादेरिति किम्? कृषीष्ट, हृषीष्ट'),
    ),
    '7.2.44': (
        _c('स्वर्ता (svartā) — the sounder, beside स्वरिता',
           {'root': 'svṛ', 'before': 'val-ādi-ārdhadhātuka'},
           note='स्वरतिसूतिसूयतिधूञूदितो वा — धूञिति सानुबन्धकस्य निर्देशो धू विधूनने इत्यस्य निवृत्त्यर्थः'),
    ),
    '7.2.45': (
        _c('रद्धा (raddhā) — the destroyer, beside रधिता',
           {'root': 'radh', 'before': 'val-ādi-ārdhadhātuka'},
           note='रधादिभ्यश्च — अपरे पुनराहुः, बलीयस्त्वं प्रतिषेधनियमस्येति'),
    ),
    '7.2.46': (
        _c('निष्कोष्टा (niṣkoṣṭā) — one who extracts',
           {'root': 'kuṣ', 'upasarga': 'nir', 'before': 'val-ādi-ārdhadhātuka'},
           note='निरः कुषः — रेफान्तमुपसर्गान्तरमस्तीति ज्ञाप्यते'),
    ),
    '7.2.47': (
        _c('निष्कुषितः (niṣkuṣitaḥ) — extracted',
           {'root': 'kuṣ', 'upasarga': 'nir', 'before': 'niṣṭhā'},
           note='इण्निष्ठायाम् — इड्ग्रहणं नित्यार्थम्'),
    ),
    '7.2.48': (
        _c('सोढा (soḍhā) — the endurer, beside सहिता',
           {'root': 'sah', 'before': 'ta-ādi-ārdhadhātuka'},
           note='तीषसहलुभरुषरिषः — इषु इच्छायाम् इत्यस्यायं विकल्प इष्यते'),
    ),
    '7.2.49': (
        _c('दिदेविषति (dideviṣati) — he wants to play',
           {'gana': 'i-anta', 'before': 'san'},
           note='सनीवन्तर्धभ्रस्जदम्भुश्रिस्वृयूर्णुभरज्ञपिसनाम् — भर इति भृञित्येतस्य भौवादिकस्य ग्रहणं शपा निर्देशात्'),
    ),
    '7.2.50': (
        _c('क्लिष्ट्वा (kliṣṭvā) — having troubled, beside क्लिशित्वा',
           {'root': 'kliś', 'before': 'ktvā'},
           note='क्लिशः क्त्वानिष्ठयोः — तदर्थं क्त्वाग्रहणं क्रियते'),
    ),
    '7.2.51': (
        _c('पूत्वा (pūtvā) — having purified, beside पवित्वा',
           {'root': 'pūṅ', 'before': 'ktvā'},
           note='पूङश्च — श्र्युकः किति इति प्रतिषेधे प्राप्ते विकल्पो विधीयते'),
    ),
    '7.2.52': (
        _c('उषित्वा (uṣitvā) — having dwelt',
           {'root': 'vas', 'before': 'ktvā'},
           note='वसतिक्षुधोरिट् — वसतीति विकरणो निर्देशार्थ एव'),
    ),
    '7.2.53': (
        _c('अञ्चित्वा जानु जुहोति (añcitvā jānu juhoti) — bending the knee, he offers',
           {'root': 'añc', 'before': 'ktvā', 'sense': 'pūjā'},
           note='अञ्चेः पूजायाम् — पूजायामिति किम्? उदक्तमुदकं कूपात्'),
    ),
    '7.2.54': (
        _c('विलुभिताः केशाः (vilubhitāḥ keśāḥ) — the hair in disarray',
           {'root': 'lubh', 'before': 'niṣṭhā', 'sense': 'vimohana'},
           note='लुभो विमोचने — गार्ध्ये यथाप्राप्तमेव भवति'),
    ),
    '7.2.55': (
        _c('जरित्वा (jaritvā) — having aged',
           {'root': 'jṝ', 'before': 'ktvā'},
           note='जॄव्रश्च्योः क्त्वि — क्त्वाग्रहणं निष्ठानिवृत्त्यर्थम्'),
    ),
    '7.2.56': (
        _c('शमित्वा (śamitvā) — having calmed, beside शान्त्वा',
           {'gana': 'udit', 'before': 'ktvā'},
           note='उदितो वा — the ऊ marker in the धातुपाठ is the whole condition'),
    ),
    '7.2.57': (
        _c('कर्त्स्यति (kartsyati) — he will cut, beside कर्तिष्यति',
           {'root': 'kṛt', 'before': 'sa-ādi-ārdhadhātuka'},
           note='सेऽसिचि कृतचृतच्छृदतृदनृतः — स इति किम्? कर्ता'),
    ),
    '7.2.58': (
        _c('गमिष्यति (gamiṣyati) — he will go',
           {'root': 'gam', 'before': 'sa-ādi-ārdhadhātuka', 'pada': 'parasmaipada'},
           note='गमेरिट् परस्मैपदेषु — आत्मनेपदेन समानपदस्थस्य गमेरयमिडागमो नेष्यते'),
    ),
    '7.2.59': (
        _c('वर्त्स्यति (vartsyati) — it will turn, without an इट्',
           {'root': 'vṛt', 'before': 'sa-ādi-ārdhadhātuka', 'pada': 'parasmaipada'},
           note='न वृद्भ्यश्चतुर्भ्यः — स्यन्देरूदिल्लक्षणमन्तरङ्गमपि विकल्पं प्रतिषेधो यथा बाधेत'),
    ),
    '7.2.60': (
        _c('श्वः कल्प्ता (śvaḥ kalptā) — he will manage tomorrow',
           {'root': 'kḷp', 'before': 'tāsi', 'pada': 'parasmaipada'},
           note='तासि च कॢपः — क्ऌपेरप्यात्मनेपदेन समानपदस्थस्येडागम इष्यते'),
    ),
    '7.2.61': (
        _c('ययाथ (yayātha) — you went, without an इट्',
           {'gana': 'ac-anta-tāsi-anit', 'before': 'thal'},
           note='अचस्तास्वत् थल्यनिटो नित्यम् — तासौ सतस्थलि प्रतिषेधार्थः'),
    ),
    '7.2.62': (
        _c('पपक्थ (papaktha) — you cooked, without an इट्',
           {'gana': 'a-vat-upadeśa-tāsi-anit', 'before': 'thal'},
           note='उपदेशेऽत्वतः — तपरकरणं किम्? राद्धा, रराधिथ'),
    ),
    '7.2.63': (
        _c('सस्मर्थ (sasmartha) — you remembered',
           {'gana': 'ṛ-anta', 'before': 'thal'},
           note='ऋतो भारद्वाजस्य — ऋत एव भारद्वाजस्य, नान्येषां धातूनाम्'),
    ),
    '7.2.64': (
        _c('त्वं हि होता प्रथमो बभूथ (tvaṃ hi hotā prathamo babhūtha) — you were the first priest',
           {'root': 'babhūtha', 'chandasi': True},
           note='बभूथाततन्थजगृम्भववर्थेति निगमे — निगम एव न भाषायामिति'),
    ),
    '7.2.65': (
        _c('सस्रष्ठ (sasraṣṭha) — you created, beside ससर्जिथ',
           {'root': 'sṛj', 'before': 'thal'},
           note='विभाषा सृजिदृषोः — both forms standing'),
    ),
    '7.2.66': (
        _c('आदिथ (āditha) — you ate',
           {'root': 'ad', 'before': 'thal'},
           note='इडत्त्यर्तिव्ययतीनाम् — अत्रेड्ग्रहणं विस्पष्टार्थम्'),
    ),
    '7.2.67': (
        _c('पेचिवान् (pecivān) — having cooked',
           {'gana': 'eka-ac-ā-anta-ghas', 'before': 'vasu'},
           note='वस्वेकाजाद्घसाम् — कृतद्विर्वचना एत एकाचो भवन्ति'),
    ),
    '7.2.68': (
        _c('जग्मिवान् (jagmivān) — having gone, beside जगन्वान्',
           {'root': 'gam', 'before': 'vasu'},
           note='विभाषा गमहनविदविशाम् — दृशेश्चेति वक्तव्यम्, ददृशिवान्'),
    ),
    '7.2.69': (
        _c('सनिं ससनिवांसम् (saniṃ sasanivāṃsam) — having won the winning',
           {'root': 'san', 'chandasi': True},
           note='सनिंससनिवांसम् — भाषायां सेनिवांसमिति भवति'),
    ),
    '7.2.70': (
        _c('करिष्यति (kariṣyati) — he will do',
           {'gana': 'ṛ-anta', 'before': 'sya'},
           note='ऋद्धनोः स्ये — स्वरतेर्वेट्त्वाद् ऋद्धनोः स्य इत्येतद् भवति विप्रतिषेधेन'),
    ),
    '7.2.71': (
        _c('आञ्जीत् (āñjīt) — he anointed',
           {'root': 'añj', 'before': 'sic'},
           note='अञ्जेः सिचि — सिचीति किम्? अङ्क्ता, अञ्जिता'),
    ),
    '7.2.72': (
        _c('अस्तावीत् (astāvīt) — he praised',
           {'root': 'stu', 'before': 'sic', 'pada': 'parasmaipada'},
           note='स्तुसुधूञ्भ्यः परस्मैपदेषु — परस्मैपदेष्विति किम्? अस्तोष्ट, असोष्ट'),
    ),
    '7.2.73': (
        _c('अयंसीत् (ayaṃsīt) — he restrained',
           {'root': 'yam', 'before': 'sic', 'pada': 'parasmaipada'},
           note='यमरमनमातां सक् च — यमादीनां हलन्तलक्षणा वृद्धिः प्राप्ता, सा नेटि इति प्रतिषिध्यते'),
    ),
    '7.2.74': (
        _c('सिस्मयिषते (sismayiṣate) — he wants to smile',
           {'root': 'smiṅ', 'before': 'san'},
           note='स्मिपूङ्रञ्ज्वशां सनि — ङकारग्रहणं पूञो मा भूत्'),
    ),
    '7.2.75': (
        _c('चिकरिषति (cikariṣati) — he wants to scatter',
           {'root': 'kṛ', 'before': 'san'},
           note='किरश्च पञ्चभ्यः — वृतो वा इति चास्येटो दीर्घत्वं नेच्छन्ति'),
    ),
    '7.2.76': (
        _c('रोदिति (roditi) — he weeps',
           {'root': 'rud', 'before': 'val-ādi-sārvadhātuka'},
           note='रुदादिभ्यः सार्वधातुके — सार्वधातुक इति किम्? स्वप्ता'),
    ),
    '7.2.77': (
        _c('ईशिषे (īśiṣe) — you rule',
           {'root': 'īś', 'before': 'se'},
           note='ईशः से — one root and one ending'),
    ),
    '7.2.78': (
        _c('ईडिध्वे (īḍidhve) — you praise',
           {'root': 'īḍ', 'before': 'dhve'},
           note='ईडजनोर्ध्वे च — तदर्थं केचिद् ईडिजनोः स्ध्वे च इति सूत्रं पठन्ति'),
    ),
    '7.2.79': (
        _c('कुर्यात् (kuryāt) — he would do',
           {'stem': 'liṅ', 'part': 'an-antya-s', 'before': 'sārvadhātuka'},
           note='लिङः सलोपोऽनन्त्यस्य — कः पुनरनन्त्यो लिङः सकारः? यो यासुट्सुट्सीयुटाम्'),
    ),
    '7.2.80': (
        _c('पचेत् (pacet) — he would cook',
           {'stem': 'yā', 'gana': 'a-anta', 'before': 'sārvadhātuka'},
           note='अतो येयः — तदनेनावश्यं विध्यन्तरं बाधितव्यम्'),
    ),
    '7.2.81': (
        _c('पचेते (pacete) — those two cook for themselves',
           {'part': 'ā-of-ṅit', 'gana': 'a-anta', 'before': 'sārvadhātuka'},
           note='आतो ङितः — ङित इव ङिद्वदिति'),
    ),
    '7.2.82': (
        _c('पचमानः (pacamānaḥ) — cooking for himself',
           {'part': 'a', 'before': 'āna'},
           note='आने मुक् — अकारमात्रभक्तोऽयं मुक् अदुपदेशग्रहणेन गृह्यते'),
    ),
    '7.2.83': (
        _c('आसीनो यजते (āsīno yajate) — seated, he sacrifices',
           {'stem': 'ās', 'before': 'āna'},
           note='ईदासः — अत्र पञ्चम्या परस्य षष्ठी कल्प्यते'),
    ),
    '7.2.84': (
        _c('अष्टाभिः (aṣṭābhiḥ) — by eight',
           {'stem': 'aṣṭan', 'before': 'vibhakti'},
           note='अष्टन आ विभक्तौ — मृजेर्वृद्धिः इत्यतः प्राग् विभक्त्यधिकारः'),
    ),
    '7.2.85': (
        _c('राभ्याम् (rābhyām) — with two riches',
           {'stem': 'rai', 'before': 'hal-vibhakti'},
           note='रायो हलि — हलीति किम्? रायौ, रायः'),
    ),
    '7.2.86': (
        _c('युष्माभिः (yuṣmābhiḥ) — by you all',
           {'stem': 'yuṣmad', 'before': 'vibhakti'},
           note='युष्मदस्मदोरनादेशे — उत्तरत्र त्वनादेशग्रहणेन प्रयोजनम्'),
    ),
    '7.2.87': (
        _c('त्वाम् (tvām) — you, as object',
           {'stem': 'yuṣmad', 'before': 'dvitīyā'},
           note='द्वितीयायां च — आदेशार्थं वचनम्'),
    ),
    '7.2.88': (
        _c('युवाम् (yuvām) — you two',
           {'stem': 'yuṣmad', 'before': 'prathamā', 'number': 'dvivacana'},
           note='प्रथमायाश्च द्विवचने भाषायाम् — भाषायामिति किम्? युवं वस्त्राणि'),
    ),
    '7.2.89': (
        _c('त्वया (tvayā) — by you',
           {'stem': 'yuṣmad', 'before': 'ac-vibhakti'},
           note='योऽचि — अचीति किम्? युवाभ्याम्, आवाभ्याम्'),
    ),
    '7.2.90': (
        _c('त्वम् (tvam) — you',
           {'stem': 'yuṣmad', 'before': 'śeṣa'},
           note='शेषे लोपः — अलिङ्गे वा युष्मदस्मदी इति'),
    ),
    '7.2.91': (
        _c('युवकाम् (yuvakām) — you two, with कच्, and untouched',
           {'stem': 'yuṣmad'},
           note='मपर्यन्तस्य — मपर्यन्तस्येति किम्? युवकाम्, आवकामिति साकच्कस्य मा भूत्'),
    ),
    '7.2.92': (
        _c('युवाम् (yuvām) — you two',
           {'stem': 'yuṣmad', 'part': 'ma-paryanta', 'number': 'dvivacana'},
           note='युवावौ द्विवचने — द्विवचने इत्यर्थग्रहणम्'),
    ),
    '7.2.93': (
        _c('यूयम् (yūyam) — you all',
           {'stem': 'yuṣmad', 'part': 'ma-paryanta', 'before': 'jas'},
           note='यूयवयौ जसि — तदन्तविधिरत्र भवति'),
    ),
    '7.2.94': (
        _c('त्वम् (tvam) — you, as subject',
           {'stem': 'yuṣmad', 'part': 'ma-paryanta', 'before': 'su'},
           note='त्वाहौ सौ — परमत्वम्, परमाहम्'),
    ),
    '7.2.95': (
        _c('तुभ्यम् (tubhyam) — to you',
           {'stem': 'yuṣmad', 'part': 'ma-paryanta', 'before': 'ṅayi'},
           note='तुभ्यमह्यौ ङयि — परमतुभ्यम्, परममह्यम्'),
    ),
    '7.2.96': (
        _c('तव (tava) — your',
           {'stem': 'yuṣmad', 'part': 'ma-paryanta', 'before': 'ṅasi-ṣaṣṭhī'},
           note='तवममौ ङसि — परमतव, परममम'),
    ),
    '7.2.97': (
        _c('त्वाम् (tvām) — you, one person',
           {'stem': 'yuṣmad', 'part': 'ma-paryanta', 'number': 'ekavacana'},
           note='त्वमावेकवचने — एकवचने इत्यर्थनिर्देशः'),
    ),
    '7.2.98': (
        _c('त्वदीयः (tvadīyaḥ) — yours',
           {'stem': 'yuṣmad', 'part': 'ma-paryanta', 'number': 'ekavacana', 'before': 'pratyaya'},
           note='प्रत्ययोत्तरपदयोश्च — ततोऽन्यत्रापि प्रत्यय उत्तरपदे च यथा स्यात्'),
    ),
    '7.2.99': (
        _c('तिस्रः (tisraḥ) — three women',
           {'stem': 'tri', 'gender': 'strī', 'before': 'vibhakti'},
           note='त्रिचतुरोः स्त्रियां तिसृचतसृ — स्त्रियामिति चैतत् त्रिचतुरोरेव विशेषणं नाङ्गस्य'),
    ),
    '7.2.100': (
        _c('तिस्रस्तिष्ठन्ति (tisrastiṣṭhanti) — three women stand',
           {'stem': 'tisṛ', 'part': 'ṛ', 'before': 'ac-vibhakti'},
           note='अचि र ऋतः — पूर्वसवर्णोत्त्वङिसर्वनामस्थानगुणानामपवादः'),
    ),
    '7.2.101': (
        _c('जरसा दन्ताः शीर्यन्ते (jarasā dantāḥ śīryante) — teeth fall with age',
           {'stem': 'jarā', 'before': 'ac-vibhakti'},
           note='जराया जरसन्यतरस्याम् — न च पुनर्लुक्शास्त्रं प्रवर्तते, भ्रष्टावसरत्वात्'),
    ),
    '7.2.102': (
        _c('सः (saḥ) — he',
           {'stem': 'tad', 'before': 'vibhakti'},
           note='त्यदादीनामः — द्विपर्यन्तानां त्यदादीनामत्वमिष्यते'),
    ),
    '7.2.103': (
        _c('कः (kaḥ) — who',
           {'stem': 'kim', 'before': 'vibhakti'},
           note='किमः कः — साकच्कस्याप्ययमादेशो भवति'),
    ),
    '7.2.104': (
        _c('कुतः (kutaḥ) — from where',
           {'stem': 'kim', 'before': 'ta-ādi-vibhakti'},
           note='कु तिहोः — तिहोरितीकार उच्चारणार्थः'),
    ),
    '7.2.105': (
        _c('क्व गमिष्यसि (kva gamiṣyasi) — where will you go',
           {'stem': 'kim', 'before': 'ati'},
           note='क्वाति — आदेशान्तरवचनम् ओर्गुणनिवृत्त्यर्थम्'),
    ),
    '7.2.106': (
        _c('सः (saḥ) — he, the द् become स्',
           {'gana': 'tyadādi', 'part': 'an-antya-t-d', 'before': 'su'},
           note='तदोः सः सावनन्त्ययोः — अनन्त्ययोरिति किम्? हे स, सा'),
    ),
    '7.2.107': (
        _c('असौ (asau) — that one, yonder',
           {'stem': 'adas', 'part': 's', 'before': 'su'},
           note='अदस औ सुलोपश्च — अदसः सोर्भवेदौत्वं किं सुलोपो विधीयते'),
    ),
    '7.2.108': (
        _c('अयम् (ayam) — this one',
           {'stem': 'idam', 'part': 'antya', 'before': 'su'},
           note='इदमो मः — इदमो मकारस्य मकारवचनं त्यदाद्यत्वबाधनार्थम्'),
    ),
    '7.2.109': (
        _c('इमौ (imau) — these two',
           {'stem': 'idam', 'part': 'd', 'before': 'vibhakti'},
           note='दश्च — इमौ, इमे, इमम्, इमान्'),
    ),
    '7.2.110': (
        _c('इयम् (iyam) — this woman',
           {'stem': 'idam', 'part': 'd', 'before': 'su'},
           note='यः सौ — उत्तरसूत्रे पुंसीति वचनात् स्त्रियामयं यकारः'),
    ),
    '7.2.111': (
        _c('अयं ब्राह्मणः (ayaṃ brāhmaṇaḥ) — this brahmin',
           {'stem': 'idam', 'part': 'id', 'before': 'su', 'gender': 'puṃs'},
           note='इदोऽय् पुंसि — पुंसीति किम्? इयं ब्राह्मणी'),
    ),
    '7.2.112': (
        _c('अनेन (anena) — by this one',
           {'stem': 'idam', 'part': 'id', 'before': 'āp-vibhakti'},
           note='अनाप्यकः — आपीति प्रत्याहारः तृतीयैकवचनात् प्रभृति सुपः पकारेण'),
    ),
    '7.2.113': (
        _c('एभिः (ebhiḥ) — by these',
           {'stem': 'idam', 'part': 'id', 'before': 'hal-vibhakti'},
           note='हलि लोपः — नानर्थकेऽलोन्त्यविधिः इति सर्वस्यायमिद्रूपस्य लोपः'),
    ),
    '7.2.115': (
        _c('कारः (kāraḥ) — the making',
           {'gana': 'ac-anta', 'before': 'ñit'},
           note='अचो ञ्णिति — ञिति एकस्तण्डुलनिश्चायः, णिति गौः, गावौ, गावः'),
    ),
    '7.2.116': (
        _c('पाकः (pākaḥ) — the cooking',
           {'part': 'upadhā-a', 'before': 'ñit'},
           note='अत उपधायाः — अत इति किम्? भेदयति, भेदकः'),
    ),
    '7.2.117': (
        _c("गार्ग्यः (gārgyaḥ) — Garga's descendant",
           {'part': 'acām-ādi', 'before': 'ñit', 'taddhita': True},
           note='तद्धितेष्वचामादेः — अचामादेर्वृद्धिरन्त्योपधालक्षणां वृद्धिं बाधते'),
    ),
    '7.2.118': (
        _c("नाडायनः (nāḍāyanaḥ) — of Naḍa's line",
           {'part': 'acām-ādi', 'before': 'kit', 'taddhita': True},
           note='किति च — नडादिभ्यः फक् gives नाडायनः, प्राग् वहतेष्ठक् gives आक्षिकः'),
    ),
    '7.3.1': (
        _c('दाविकम् उदकम् (dāvikam udakam) — water of the Devikā',
           {'stem': 'devikā', 'before': 'ñit'},
           note='देविकाशिंशपादित्यवाड्दीर्घसत्रश्रेयसामात् — प्राचां ग्रामनगराणाम् इत्युत्तरपदवृद्धिः, साप्याकार एव भवति'),
    ),
    '7.3.2': (
        _c('कैकेयः (kaikeyaḥ) — of the Kekayas',
           {'stem': 'kekaya', 'before': 'ñit'},
           note='केकयमित्त्रययुप्रलयानां यादेरियः — जनपदशब्दात् क्षत्रियादञ् इत्यञ्प्रत्ययः'),
    ),
    '7.3.3': (
        _c('वैयाकरणः (vaiyākaraṇaḥ) — a grammarian',
           {'gana': 'y-v-pada-anta-pūrva', 'before': 'ñit'},
           note='न य्वाभ्यां पदान्ताभ्याम् पूर्वौ तु ताभ्यामैच् — प्रतिषेधवचनमैचोर्विषयप्रक्ऌप्त्यर्थम्'),
    ),
    '7.3.4': (
        _c('दौवारिकः (dauvārikaḥ) — a doorkeeper',
           {'gana': 'dvāra-ādi', 'before': 'ñit'},
           note='द्वारादीनां च — स्वाध्याय इति केचित् पठन्ति, तदनर्थकम्'),
    ),
    '7.3.5': (
        _c('नैयग्रोधश्चमसः (naiyagrodhaścamasaḥ) — a banyan-wood cup',
           {'stem': 'nyagrodha', 'before': 'ñit'},
           note='न्यग्रोधस्य च केवलस्य — व्युत्पत्तिपक्षे नियमार्थम्, अव्युत्पत्तिपक्षे विध्यर्थम्'),
    ),
    '7.3.6': (
        _c('व्यावक्रोशी वर्तते (vyāvakrośī vartate) — they revile one another',
           {'sense': 'karma-vyatihāra', 'before': 'ñit'},
           note='न कर्मव्यतिहारे — प्रतिषेधागमयोरयं प्रतिषेधः'),
    ),
    '7.3.7': (
        _c('स्वागतिकः (svāgatikaḥ) — one who says welcome',
           {'stem': 'svāgata', 'before': 'ñit'},
           note='स्वागतादीनां च — व्यवहारशब्दोऽयं लौकिके वृत्ते वर्तते, न तु कर्मव्यतिहारे'),
    ),
    '7.3.8': (
        _c("श्वाभस्त्रिः (śvābhastriḥ) — Śvabhastrā's descendant",
           {'gana': 'śvan-ādi', 'before': 'iñ'},
           note='श्वादेरिञि — तत्र च तदादिविधिर्भवतीत्येतदेव वचनं ज्ञापकम्'),
    ),
    '7.3.9': (
        _c('श्वापदम् (śvāpadam) — a beast of prey, beside शौवापदम्',
           {'gana': 'śvan-ādi', 'uttarapada': 'pada'},
           note='पदान्तस्यान्यतरस्याम् — श्वपदस्येदं श्वापदम्, शौवापदम्'),
    ),
    '7.3.10': (
        _c('पूर्ववार्षिकम् (pūrvavārṣikam) — of the early rains, at 7.3.11',
           {'purvapada': 'avayava', 'uttarapada': 'ṛtu', 'before': 'ñit'},
           note='उत्तरपदस्य — हनस्तोऽचिण्णलोः इति प्रागेतस्मात्'),
    ),
    '7.3.11': (
        _c('पूर्ववार्षिकम् (pūrvavārṣikam) — of the early rains',
           {'purvapada': 'avayava', 'uttarapada': 'ṛtu', 'before': 'ñit'},
           note='अवयवादृतोः — ऋतोर्वृद्धिमद्विधाववयवानाम् इति तदन्तविधिः'),
    ),
    '7.3.12': (
        _c('सुपाञ्चालकः (supāñcālakaḥ) — of the good Pañcālas',
           {'purvapada': 'su-sarva-ardha', 'uttarapada': 'janapada', 'before': 'ñit'},
           note='सुसर्वार्धाज्जनपदस्य — सुसर्वार्धदिक्शब्देभ्यो जनपदस्य इति तदन्तविधिः'),
    ),
    '7.3.13': (
        _c('पूर्वपाञ्चालकः (pūrvapāñcālakaḥ) — of the eastern Pañcālas',
           {'purvapada': 'diś', 'uttarapada': 'janapada', 'before': 'ñit'},
           note='दिशोऽमद्राणाम् — अमद्राणामिति किम्? पौर्वमद्रः, आपरमद्रः'),
    ),
    '7.3.14': (
        _c('पूर्वैषुकामशमः (pūrvaiṣukāmaśamaḥ) — of eastern Iṣukāmaśamī',
           {'purvapada': 'diś', 'uttarapada': 'grāma-nagara', 'sense': 'prācām', 'before': 'ñit'},
           note='प्राचां ग्रामनगराणाम् — संबन्धभेदप्रतिपत्त्यर्थम्, which is why both are named'),
    ),
    '7.3.15': (
        _c('द्विसांवत्सरिकः (dvisāṃvatsarikaḥ) — engaged for two years',
           {'purvapada': 'saṃkhyā', 'uttarapada': 'saṃvatsara-saṃkhyā', 'before': 'ñit'},
           note='संख्यायाः संवत्सरसंख्यस्य च — परिमाणग्रहणे कालपरिमाणस्याग्रहणार्थम्'),
    ),
    '7.3.16': (
        _c('द्विवार्षिकः (dvivārṣikaḥ) — engaged for two years',
           {'purvapada': 'saṃkhyā', 'uttarapada': 'varṣa', 'before': 'ñit'},
           note='वर्षस्याभविष्यति — गम्यते हि तत्र भविष्यत्ता, न तु तद्धितार्थः'),
    ),
    '7.3.17': (
        _c('द्विकौडविकः (dvikauḍavikaḥ) — worth two kuḍavas',
           {'purvapada': 'saṃkhyā', 'uttarapada': 'parimāṇa', 'before': 'ñit'},
           note='परिमाणान्तस्यासंज्ञाशाणयोः — असंज्ञाशाणयोरिति किम्?'),
    ),
    '7.3.18': (
        _c('प्रोष्ठपादो माणवकः (proṣṭhapādo māṇavakaḥ) — a boy born under those stars',
           {'uttarapada': 'proṣṭhapadā', 'sense': 'jāta', 'before': 'ñit'},
           note='जे प्रोष्ठपदानाम् — बहुवचननिर्देशात् पर्यायोऽपि गृह्यते, भद्रपाद इति'),
    ),
    '7.3.19': (
        _c('सौहार्दम् (sauhārdam) — friendship',
           {'gana': 'hṛd-bhaga-sindhu-anta', 'before': 'ñit'},
           note='हृद्भगसिन्ध्वन्ते पूर्वपदस्य च — छन्दसि सर्वविधीनां विकल्पितत्वात्'),
    ),
    '7.3.20': (
        _c('आनुशातिकम् (ānuśātikam) — of the anuśatika',
           {'gana': 'anuśatika-ādi', 'before': 'ñit'},
           note='अनुशतिकादीनां च — अस्यहत्य इति केचित् पठन्ति, अस्यहेतिरित्येवमपरे'),
    ),
    '7.3.21': (
        _c('आग्निमारुतं कर्म (āgnimārutaṃ karma) — the rite of Agni and the Maruts',
           {'gana': 'devatā-dvandva', 'before': 'ñit'},
           note='देवताद्वंद्वे च — यो देवताद्वन्द्वः सूक्तहविःसंबन्धी, तत्रायं विधिः'),
    ),
    '7.3.22': (
        _c('सौमेन्द्रः (saumendraḥ) — of Soma and Indra',
           {'uttarapada': 'indra', 'before': 'ñit'},
           note='नेन्द्रस्य परस्य — बहिरङ्गमपि पूर्वोत्तरपदयोः पूर्वं कार्यं भवति पश्चादेकादेशः'),
    ),
    '7.3.23': (
        _c('ऐन्द्रावरुणम् (aindrāvaruṇam) — of Indra and Varuṇa',
           {'uttarapada': 'varuṇa', 'purvapada': 'dīrgha-anta', 'before': 'ñit'},
           note='दीर्घाच्च वरुणस्य — दीर्घादिति किम्? आग्निवारुणीमनड्वाहीमालभेत'),
    ),
    '7.3.24': (
        _c('सौह्मनागरः (sauhmanāgaraḥ) — of the town of Suhma',
           {'uttarapada': 'nagara-anta', 'sense': 'prācām', 'before': 'ñit'},
           note='प्राचां नगरान्ते — प्राचामिति किम्? माद्रनगरः'),
    ),
    '7.3.25': (
        _c('कौरुजङ्गलम् (kaurujaṅgalam) — of the Kuru jungle',
           {'gana': 'jaṅgala-dhenu-valaja-anta', 'before': 'ñit'},
           note='जङ्गलधेनुवलजान्तस्य विभाषितमुत्तरम् — सौवर्णवलजः, सौवर्णवालजः'),
    ),
    '7.3.26': (
        _c('आर्धद्रौणिकम् (ārdhadrauṇikam) — bought for half a droṇa',
           {'purvapada': 'ardha', 'uttarapada': 'parimāṇa', 'before': 'ñit'},
           note='अर्धात् परिमाणस्य पूर्वस्य तु वा — परिमाणस्येति किम्? आर्धक्रोशिकम्'),
    ),
    '7.3.27': (
        _c('अर्धप्रस्थिकः (ardhaprasthikaḥ) — worth half a prastha',
           {'purvapada': 'ardha', 'uttarapada': 'a-parimāṇa', 'before': 'ñit'},
           note='नातः परस्य — तपरकरणं किम्? अर्धखार्यां भवा अर्धखारी'),
    ),
    '7.3.28': (
        _c("प्रावाहणेयः (prāvāhaṇeyaḥ) — Pravāhaṇa's descendant",
           {'stem': 'pravāhaṇa', 'before': 'ḍha'},
           note='प्रवाहणस्य ढे — शुभ्रादिभ्यश्च इति ढक् प्रत्ययः'),
    ),
    '7.3.29': (
        _c("प्रावाहणेयिः (prāvāhaṇeyiḥ) — Prāvāhaṇeya's descendant",
           {'stem': 'pravāhaṇeya', 'before': 'taddhita'},
           note='तत्प्रत्ययस्य च — बाह्यतद्धितनिमित्ता वृद्धिर्ढाश्रयेण विकल्पेन बाधितुमशक्या'),
    ),
    '7.3.30': (
        _c('अशौचम् (aśaucam) — impurity, beside आशौचम्',
           {'stem': 'śuci', 'purvapada': 'nañ', 'before': 'ñit'},
           note='नञः शुचीश्वरक्षेत्रज्ञकुशलनिपुणानाम् — इयं पूर्वपदस्य वृद्धिरप्राप्तैव विभाषा विधीयते'),
    ),
    '7.3.31': (
        _c('आयथातथ्यम् (āyathātathyam) — unfitness, beside अयाथातथ्यम्',
           {'stem': 'yathātatha', 'purvapada': 'nañ', 'before': 'ñit'},
           note='यथातथयथापुरयोः पर्यायेण — तथा नपुंसकाश्रयं ह्रस्वत्वं कृतम्'),
    ),
    '7.3.32': (
        _c('घातयति (ghātayati) — he has it killed',
           {'root': 'han', 'before': 'ñit'},
           note='हनस्तोऽचिण्णलोः — तद्धितेष्विति निवृत्तम्, तत्संबद्धं कितीत्यपि'),
    ),
    '7.3.33': (
        _c('अदायि (adāyi) — it was given',
           {'gana': 'ā-anta', 'before': 'ciṇ'},
           note='आतो युक् चिण्कृतोः — चिण्कृतोरिति किम्? ददौ, दधौ'),
    ),
    '7.3.34': (
        _c('अशमि (aśami) — it was calmed',
           {'gana': 'udātta-upadeśa-m-anta', 'before': 'ciṇ'},
           note='नोदात्तोपदेशस्य मान्तस्यानाचमेः — किं चोक्तम्? अत उपधायाः इति वृद्धिः'),
    ),
    '7.3.35': (
        _c('अजनि (ajani) — it was born',
           {'root': 'jan', 'before': 'ciṇ'},
           note='जनिवध्योश्च — वधिः प्रकृत्यन्तरं व्यञ्जनान्तोऽस्ति तस्यायं प्रतिषेधो विधीयते'),
    ),
    '7.3.36': (
        _c('अर्पयति (arpayati) — he hands over',
           {'root': 'ṛ', 'before': 'ṇi'},
           note='अर्त्तिह्रीब्लीरीक्नूयीक्ष्माय्यातां पुङ्णौ — पुकः पूर्वान्तकरणमदीदपदित्यत्रोपधाह्रस्वो यथा स्यात्'),
    ),
    '7.3.37': (
        _c('पाययति (pāyayati) — he gives to drink',
           {'root': 'śā', 'before': 'ṇi'},
           note='शाच्छासाह्वाव्यावेपां युक् — धूञ्प्रीञोर्नुग् वक्तव्यः'),
    ),
    '7.3.38': (
        _c('पक्षेणोपवाजयति (pakṣeṇopavājayati) — he fans with a wing',
           {'root': 'vā', 'before': 'ṇi', 'sense': 'vidhūnana'},
           note='वो विधूनने जुक् — विधूनन इति किम्? आवापयति केशान्'),
    ),
    '7.3.39': (
        _c('घृतं विलीनयति (ghṛtaṃ vilīnayati) — he melts the ghee',
           {'root': 'lī', 'before': 'ṇi', 'sense': 'sneha-vipātana'},
           note='लीलोर्नुग्लुकावन्यतरस्यां स्नेहविपातने — स्नेहविपातन इति किम्? जतु विलापयति'),
    ),
    '7.3.40': (
        _c('मुण्डो भीषयते (muṇḍo bhīṣayate) — the shaven man frightens',
           {'root': 'bhī', 'before': 'ṇi', 'sense': 'hetu-bhaya'},
           note='भियो हेतुभये षुक् — नात्र हेतुः प्रयोजको भयकारणम्, किं तर्हि? कुञ्चिका'),
    ),
    '7.3.41': (
        _c('स्फावयति (sphāvayati) — he makes it swell',
           {'root': 'sphāy', 'before': 'ṇi'},
           note='स्फायो वः — one root and one substitute'),
    ),
    '7.3.42': (
        _c('पुष्पाणि शातयति (puṣpāṇi śātayati) — he makes the flowers fall',
           {'root': 'śad', 'before': 'ṇi', 'sense': 'a-gati'},
           note='शदेरगतौ तः — अगताविति किम्? गाः शादयति गोपालकः'),
    ),
    '7.3.43': (
        _c('व्रीहीन् रोपयति (vrīhīn ropayati) — he plants the rice',
           {'root': 'ruh', 'before': 'ṇi'},
           note='रुहः पोऽन्यतरस्याम् — व्रीहीन् रोपयति, व्रीहीन् रोहयति'),
    ),
    '7.3.44': (
        _c('जटिलिका (jaṭilikā) — a little matted-haired one',
           {'what': 'a-before-pratyaya-ka', 'before': 'āp'},
           note='प्रत्ययस्थात् कात् पूर्वस्यात इदाप्यसुपः — कादिति किम्? मण्डना, रमणा'),
    ),
    '7.3.45': (
        _c('यका (yakā) — she who, with the क',
           {'what': 'yā', 'before': 'āp'},
           note='न यासयोः — या सा इति निर्देशोऽतन्त्रम्, यत्तदोरुपलक्षणार्थमेतत्'),
    ),
    '7.3.46': (
        _c('इभ्यका (ibhyakā) — a little rich woman, beside इभ्यिका',
           {'gana': 'ya-ka-pūrva-ā', 'before': 'āp'},
           note='उदीचामातः स्थाने यकपूर्वायाः — उदीचांग्रहणं विकल्पार्थम्'),
    ),
    '7.3.47': (
        _c('भस्त्रका (bhastrakā) — a little bellows, beside भस्त्रिका',
           {'what': 'bhastrā', 'before': 'āp'},
           note='भस्त्रैषाऽजाज्ञाद्वास्वानञ्पूर्वाणामपि — एषाद्वे नञ्पूर्वे न प्रयोजयतः'),
    ),
    '7.3.48': (
        _c('खट्वका (khaṭvakā) — a little cot, beside खट्विका',
           {'gana': 'a-bhāṣitapuṃska', 'before': 'āp'},
           note='अभाषितपुंस्काच्च — तदा न भवति, अविद्यमाना खट्वा अस्या अखट्वा'),
    ),
    '7.3.49': (
        _c("खट्वाका (khaṭvākā) — a little cot, in the teachers' view",
           {'gana': 'a-bhāṣitapuṃska', 'before': 'āp', 'view': 'ācāryāṇām matena'},
           note='आदाचार्याणाम् — खट्वाका, अखट्वाका, परमखट्वाका'),
    ),
    '7.3.50': (
        _c('आक्षिकः (ākṣikaḥ) — a gambler',
           {'what': 'ṭha', 'before': 'taddhita'},
           note='ठस्येकः — संघातग्रहणे तु प्रत्ययेऽत्रापि संघातग्रहणमेव'),
    ),
    '7.3.51': (
        _c('सार्पिष्कः (sārpiṣkaḥ) — cooked with ghee',
           {'what': 'ṭha', 'gana': 'is-us-uk-ta-anta'},
           note='इसुसुक्तान्तात् कः — इसुसोः प्रतिपदोक्तयोर्ग्रहणादिह न भवति'),
    ),
    '7.3.52': (
        _c('पाकः (pākaḥ) — the cooking',
           {'gana': 'c-j-anta', 'before': 'ghit'},
           note='चजोः कु घिन्ण्यतोः — घिति पाकः, ण्यति पाक्यम्'),
    ),
    '7.3.53': (
        _c('न्यङ्कुः (nyaṅkuḥ) — an antelope',
           {'gana': 'nyaṅku-ādi'},
           note='न्यङ्क्वादीनां च — क्षणेपाक इत्यपि हि केचित् पठन्ति'),
    ),
    '7.3.54': (
        _c('घ्नन्ति (ghnanti) — they kill',
           {'root': 'han', 'before': 'na'},
           note='हो हन्तेर्ञ्णिन्नेषु — तच्चानन्तर्यं संनिपातकृतमाश्रीयते'),
    ),
    '7.3.55': (
        _c('जिघांसति (jighāṃsati) — he wants to kill',
           {'root': 'han', 'abhyasa': True},
           note='अभ्यासाच्च — इह न भवति, हननीयितुमिच्छति जिहननीयिषति'),
    ),
    '7.3.56': (
        _c('प्रजिघीषति (prajighīṣati) — he wants to send forth',
           {'root': 'hi', 'abhyasa': True},
           note='हेरचङि — चङोऽन्यत्र हेर्ण्यधिकस्यापि कुत्वं भवति'),
    ),
    '7.3.57': (
        _c('जिगीषति (jigīṣati) — he wants to win',
           {'root': 'ji', 'before': 'san', 'abhyasa': True},
           note='सन्लिटोर्जेः — लाक्षणिकत्वात् तस्य ग्रहणं न भवति'),
    ),
    '7.3.58': (
        _c('चिकीषति (cikīṣati) — he wants to gather, beside चिचीषति',
           {'root': 'ci', 'before': 'san', 'abhyasa': True},
           note='विभाषा चेः — सन्लिटोरित्येव, चेचीयते'),
    ),
    '7.3.59': (
        _c('कूजो वर्तते (kūjo vartate) — a humming is heard',
           {'gana': 'ku-ādi', 'before': 'ghit'},
           note='न क्वादेः — कूज्यं भवता, खर्ज्यम्, गर्ज्यं भवता'),
    ),
    '7.3.60': (
        _c('समाजः (samājaḥ) — an assembly',
           {'root': 'aj', 'before': 'ghit'},
           note='अजिवृज्योश्च — अजेर्व्यघञपोः इति वीभावस्य विधानाद् ण्यति नास्त्युदाहरणम्'),
    ),
    '7.3.61': (
        _c('भुजः पाणिः (bhujaḥ pāṇiḥ) — the hand, the arm',
           {'root': 'bhuja', 'before': 'ghañ', 'sense': 'pāṇi-upatāpa'},
           note='भुजन्युब्जौ पाण्युपतापयोः — पाण्युपतापयोरिति किम्? भोगः, समुद्गः'),
    ),
    '7.3.62': (
        _c('पञ्च प्रयाजाः (pañca prayājāḥ) — the five fore-offerings',
           {'root': 'prayāja', 'sense': 'yajña-aṅga'},
           note='प्रयाजानुयाजौ यज्ञाङ्गे — प्रदर्शनार्थम्, अन्यत्राप्येवंप्रकारे कुत्वं न भवति'),
    ),
    '7.3.63': (
        _c('वञ्च्यं वञ्चन्ति वणिजः (vañcyaṃ vañcanti vaṇijaḥ) — the traders travel',
           {'root': 'vañc', 'sense': 'gati'},
           note='वञ्चेर्गतौ — गताविति किम्? वङ्कं काष्ठम्'),
    ),
    '7.3.64': (
        _c('न्योको गृहम् (nyoko gṛham) — the house, a dwelling',
           {'root': 'uc', 'before': 'ka'},
           note='ओक उचः के — स्वरार्थम्, अन्तोदात्तोऽयमिष्यते, घञि सत्याद्युदात्तः स्यात्'),
    ),
    '7.3.65': (
        _c('अवश्यपाच्यम् (avaśyapācyam) — what must be cooked',
           {'before': 'ṇya', 'sense': 'āvaśyaka'},
           note='ण्य आवश्यके — आवश्यक इति किम्? पाक्यम्, वाक्यम्, रेक्यम्'),
    ),
    '7.3.66': (
        _c('याज्यम् (yājyam) — what is to be offered',
           {'root': 'yaj', 'before': 'ṇya'},
           note='यजयाचरुचप्रवचर्चश्च — प्रवाच्यो नाम पाठविशेषोपलक्षितो ग्रन्थोऽस्ति'),
    ),
    '7.3.67': (
        _c('वाच्यमाह (vācyamāha) — he says what is to be said',
           {'root': 'vac', 'before': 'ṇyat'},
           note='वचोऽशब्दसंज्ञायाम् — अशब्दसंज्ञायामिति किम्? अवघुषितं वाक्यमाह'),
    ),
    '7.3.68': (
        _c('शक्यः प्रयोक्तुं प्रयोज्यः (śakyaḥ prayoktuṃ prayojyaḥ) — what can be employed',
           {'root': 'prayojya', 'sense': 'śakya'},
           note='प्रयोज्यनियोज्यौ शक्यार्थे — शक्यार्थ इति किम्? प्रयोग्यः, नियोग्यः'),
    ),
    '7.3.69': (
        _c('भोज्य ओदनः (bhojya odanaḥ) — rice, which is food',
           {'root': 'bhojya', 'sense': 'bhakṣya'},
           note='भोज्यं भक्ष्ये — भक्ष्य इति किम्? भोग्यः कम्बलः'),
    ),
    '7.3.70': (
        _c('सोमो ददद् गन्धर्वाय (somo dadad gandharvāya) — Soma giving to the Gandharva',
           {'gana': 'ghu', 'before': 'leṭ'},
           note='घोर्लोपो लेटि वा — तत्र वावचनं विस्पष्टार्थम्'),
    ),
    '7.3.71': (
        _c('निश्यति (niśyati) — he sharpens',
           {'gana': 'o-anta', 'before': 'śyan'},
           note='ओतः श्यनि — शो, छो, दो, सो'),
    ),
    '7.3.72': (
        _c('अधुक्षाताम् (adhukṣātām) — those two milked',
           {'root': 'ksa', 'before': 'ac'},
           note='क्सस्याचि — ककारवत उपादानं किम्? इह मा भूत् — उत्सौ, वत्साः'),
    ),
    '7.3.73': (
        _c('अदुग्ध (adugdha) — he milked, beside अधुक्षत',
           {'root': 'duh', 'before': 'dantya', 'pada': 'ātmanepada'},
           note='लुग्वा दुहदिहलिहगुहामात्मनेपदे दन्त्ये — लुग्ग्रहणं सर्वादेशार्थम्, तच्च वह्यर्थम्'),
    ),
    '7.3.74': (
        _c('शाम्यति (śāmyati) — he grows calm',
           {'root': 'śam', 'before': 'śyan'},
           note='शमामष्टानां दीर्घः श्यनि — श्यनीति किम्? भ्रमति'),
    ),
    '7.3.75': (
        _c('ष्ठीवति (ṣṭhīvati) — he spits',
           {'root': 'ṣṭhivu', 'before': 'śit'},
           note='ष्ठिवुक्लम्याचमां शिति — क्लमिग्रहणं शबर्थम्'),
    ),
    '7.3.76': (
        _c('क्रामति (krāmati) — he strides',
           {'root': 'kram', 'before': 'śit', 'pada': 'parasmaipada'},
           note='क्रमः परस्मैपदेषु — न च हौ क्रमिरङ्गम्, किं तर्हि? शपि'),
    ),
    '7.3.77': (
        _c('गच्छति (gacchati) — he goes',
           {'root': 'gam', 'before': 'śit'},
           note='इषुगमियमां छः — इषेरुदितो ग्रहणम्, इह मा भूत् — इष्यति, इष्णाति'),
    ),
    '7.3.78': (
        _c('पिबति (pibati) — he drinks',
           {'root': 'pā', 'before': 'śit'},
           note='पाघ्राध्मास्थाम्नादाण्दृश्यर्त्तिसर्त्तिशदसदाम् — पिबतेर्लघूपधगुणः प्राप्नोति, सोऽङ्गवृत्ते पुनर्वृत्तावविधिर्निष्ठितस्य इति न भवति'),
    ),
    '7.3.79': (
        _c('जानाति (jānāti) — he knows',
           {'root': 'jñā', 'before': 'śit'},
           note='ज्ञाजनोर्जा — जनेर्दैवादिकस्य ग्रहणम्'),
    ),
    '7.3.80': (
        _c('पुनाति (punāti) — he purifies',
           {'gana': 'pū-ādi', 'before': 'śit'},
           note='प्वादीनां ह्रस्वः — आगणान्ताः प्वादय इति, on the second reading'),
    ),
    '7.3.81': (
        _c('प्रमिणन्ति व्रतानि (pramiṇanti vratāni) — they transgress the vows',
           {'root': 'mī', 'before': 'śit', 'chandasi': True},
           note='मीनातेर्निगमे — निगम इति किम्? प्रमीणाति'),
    ),
    '7.3.82': (
        _c('मेद्यति (medyati) — he grows fat',
           {'root': 'mid', 'before': 'śit'},
           note='मिदेर्गुणः — शितीत्येव, मिद्यते'),
    ),
    '7.3.83': (
        _c('अजुहवुः (ajuhavuḥ) — they offered',
           {'gana': 'ik-anta', 'before': 'jus'},
           note='जुसि च — तत्र हि प्राप्ते चाप्राप्ते चारभ्यत इति'),
    ),
    '7.3.85': (
        _c('जागरयति (jāgarayati) — he keeps someone awake',
           {'root': 'jāgṛ'},
           note='जाग्रोऽविचिण्णल्ङित्सु — यदि हि स्यादनर्थक एव गुणः स्यात्'),
    ),
    '7.3.86': (
        _c('भेदनम् (bhedanam) — the splitting',
           {'gana': 'pug-anta-laghu-upadha', 'before': 'ārdhadhātuka'},
           note="पुगन्तलघूपधस्य च — संयोगे गुरुसंज्ञायां गुणो भेत्तुर्न सिध्यति, and the verse's answer"),
    ),
    '7.3.87': (
        _c('नेनिजानि (nenijāni) — let me wash clean',
           {'gana': 'abhyasta-laghu-upadha', 'before': 'ac-ādi-pit-sārvadhātuka'},
           note='नाभ्यस्तस्याचि पिति सार्वधातुके — बहुलं छन्दसीति वक्तव्यम्'),
    ),
    '7.3.88': (
        _c('अभूत् (abhūt) — it was',
           {'root': 'bhū', 'before': 'tiṅ'},
           note='भूसुवोस्तिङि — ज्ञापकात्, यदयं बोभूतु इति गुणाभावार्थं निपातनं करोति'),
    ),
    '7.3.89': (
        _c('यौति (yauti) — he joins',
           {'gana': 'u-anta', 'before': 'hal-ādi-pit-sārvadhātuka', 'result': 'luk'},
           note='उतो वृद्धिर्लुकि हलि — लुकीति किम्? सुनोति, सुनोषि'),
    ),
    '7.3.90': (
        _c('प्रोर्णौति (prorṇauti) — he covers over, beside प्रोर्णोति',
           {'root': 'ūrṇu', 'before': 'hal-ādi-pit-sārvadhātuka'},
           note='ऊर्णोतेर्विभाषा — हलीत्येव, प्रोर्णवानि'),
    ),
    '7.3.91': (
        _c('प्रौर्णोत् (praurṇot) — he covered over',
           {'root': 'ūrṇu', 'before': 'apṛkta-hal-pit-sārvadhātuka'},
           note='गुणोऽपृक्ते — यस्मिन् विधिस्तदादावल्ग्रहणे इति'),
    ),
    '7.3.92': (
        _c('तृणेढि (tṛṇeḍhi) — he crushes',
           {'root': 'tṛṇah', 'before': 'hal-ādi-pit-sārvadhātuka'},
           note='तृणह इम् — श्नमि कृत इमागमो यथा स्यादिति'),
    ),
    '7.3.93': (
        _c('ब्रवीति (bravīti) — he speaks',
           {'root': 'brū', 'before': 'hal-ādi-pit-sārvadhātuka'},
           note='ब्रुव ईट् — हलीत्येव, ब्रवाणि; पितीत्येव, ब्रूतः'),
    ),
    '7.3.94': (
        _c('शाकुनिको लालपीति (śākuniko lālapīti) — the fowler keeps chattering',
           {'gana': 'yaṅ-anta', 'before': 'hal-ādi-pit-sārvadhātuka'},
           note='यङो वा — न च भवति, वर्वर्ति, चर्करिति चक्रम्'),
    ),
    '7.3.95': (
        _c('उपस्तवीति (upastavīti) — he praises, beside उपस्तौति',
           {'root': 'tu', 'before': 'hal-ādi-sārvadhātuka'},
           note='तुरुस्तुशम्यमः सार्वधातुके — तु इति सौत्रोऽयं धातुः'),
    ),
    '7.3.96': (
        _c('आसीत् (āsīt) — he was',
           {'root': 'as', 'before': 'apṛkta-sārvadhātuka'},
           note='अस्तिसिचोऽपृक्ते — आहिभुवोरीटि प्रतिषेधः'),
    ),
    '7.3.97': (
        _c('अहर्वाव तर्ह्यासीत् (aharvāva tarhyāsīt) — it was day then',
           {'root': 'as', 'before': 'apṛkta-sārvadhātuka', 'chandasi': True},
           note='बहुलं छन्दसि — छान्दसत्वाद् माङ्योगेऽप्यडागमो भवति'),
    ),
    '7.3.98': (
        _c('अरोदीत् (arodīt) — he wept',
           {'root': 'rud', 'before': 'apṛkta-hal-sārvadhātuka'},
           note='रुदश्च पञ्चभ्यः — पञ्चभ्य इति किम्? अजागर्भवान्'),
    ),
    '7.3.99': (
        _c('अरोदत् (arodat) — he wept, beside अरोदीत्',
           {'root': 'rud', 'before': 'apṛkta-sārvadhātuka', 'wants': 'aṭ'},
           note='अड्गार्ग्यगालवयोः — गार्ग्यगालवयोर्ग्रहणं पूजार्थम्'),
    ),
    '7.3.100': (
        _c('आदत् (ādat) — he ate',
           {'root': 'ad', 'before': 'apṛkta-sārvadhātuka'},
           note='अदः सर्वेषाम् — अपृक्तस्येत्येव, अत्ति, अत्सि'),
    ),
    '7.3.102': (
        _c('वृक्षाय (vṛkṣāya) — for the tree',
           {'gana': 'a-anta', 'before': 'yañ-ādi-sup'},
           note='सुपि च — अत इत्येव, अग्निभ्याम्; यञीत्येव, वृक्षस्य'),
    ),
    '7.3.103': (
        _c('वृक्षेभ्यः (vṛkṣebhyaḥ) — for the trees',
           {'gana': 'a-anta', 'before': 'jhal-ādi-bahuvacana-sup'},
           note='बहुवचने झल्येत् — बहुवचन इति किम्? वृक्षाभ्याम्'),
    ),
    '7.3.104': (
        _c('वृक्षयोः स्वम् (vṛkṣayoḥ svam) — the property of the two trees',
           {'gana': 'a-anta', 'before': 'os'},
           note='ओसि च — वृक्षयोर्निधेहि, प्लक्षयोर्निधेहि'),
    ),
    '7.3.105': (
        _c('खट्वया (khaṭvayā) — by the cot',
           {'gana': 'āp-anta', 'before': 'āṅ'},
           note='आङि चापः — आङिति पूर्वाचार्यनिर्देशेन तृतीयैकवचनं गृह्यते'),
    ),
    '7.3.106': (
        _c('हे खट्वे (he khaṭve) — O cot',
           {'gana': 'āp-anta', 'before': 'sambuddhi'},
           note='सम्बुद्धौ च — आप इति वर्तते'),
    ),
    '7.3.107': (
        _c('हे अम्ब (he amba) — O mother',
           {'gana': 'ambā-artha-nadī', 'before': 'sambuddhi'},
           note='अम्बाऽर्थनद्योर्ह्रस्वः — डलकवतीनां प्रतिषेधो वक्तव्यः'),
    ),
    '7.3.108': (
        _c('हे अग्ने (he agne) — O Agni',
           {'gana': 'hrasva-anta', 'before': 'sambuddhi'},
           note='ह्रस्वस्य गुणः — ह्रस्वविधानसामर्थ्याद् गुणो न भवति'),
    ),
    '7.3.109': (
        _c('अग्नयः (agnayaḥ) — fires',
           {'gana': 'hrasva-anta', 'before': 'jas'},
           note='जसि च — इतः प्रकरणात् प्रभृति छन्दसि वेति वक्तव्यम्'),
    ),
    '7.3.110': (
        _c('मातरि (mātari) — in the mother',
           {'gana': 'ṛ-anta', 'before': 'ṅi'},
           note='ऋतो ङिसर्वनामस्थानयोः — तपरकरणं मुखसुखार्थम्'),
    ),
    '7.3.111': (
        _c('अग्नये (agnaye) — to Agni',
           {'gana': 'ghi', 'before': 'ṅit'},
           note='घेर्ङिति — घेरिति किम्? सख्ये, पत्ये'),
    ),
    '7.3.112': (
        _c('कुमार्यै (kumāryai) — to the girl',
           {'gana': 'nadī-anta', 'before': 'ṅit'},
           note='आण्नद्याः — कुमार्यै, ब्रह्मबन्ध्वै'),
    ),
    '7.3.113': (
        _c('खट्वायै (khaṭvāyai) — to the cot',
           {'gana': 'āp-anta', 'before': 'ṅit'},
           note='याडापः — ङ्याब्ग्रहणेऽदीर्घः इति वचनाद् याडागमो न भवति'),
    ),
    '7.3.114': (
        _c('सर्वस्यै (sarvasyai) — to all of them',
           {'gana': 'sarvanāma-āp', 'before': 'ṅit'},
           note='सर्वनाम्नः स्याड्ढ्रस्वश्च — आप इत्येव, भवति, भवते'),
    ),
    '7.3.115': (
        _c('द्वितीयस्यै (dvitīyasyai) — to the second, beside द्वितीयायै',
           {'stem': 'dvitīya', 'before': 'ṅit'},
           note='विभाषा द्वितीयातृतीयाभ्याम् — द्वितीयातृतीययोश्च ह्रस्वो भवति'),
    ),
    '7.3.116': (
        _c('कुमार्याम् (kumāryām) — in the girl',
           {'gana': 'nadī-āp-nī', 'before': 'ṅi'},
           note='ङेराम्नद्याम्नीभ्यः — नी — राजन्याम्, सेनान्याम्, ग्रामण्याम्'),
    ),
    '7.3.117': (
        _c('कृत्याम् (kṛtyām) — in the deed',
           {'gana': 'id-ud-nadī', 'before': 'ṅi'},
           note='इदुद्भ्याम् — कृत्याम्, धेन्वाम्'),
    ),
    '7.3.118': (
        _c('सख्यौ (sakhyau) — in the friend',
           {'gana': 'id-ud', 'before': 'ṅi'},
           note='औत् — यद् न नदीसंज्ञं नापि घिसंज्ञमिकारान्तम्, तदिहोदाहरणम्'),
    ),
    '7.3.119': (
        _c('अग्नौ (agnau) — in the fire',
           {'gana': 'ghi', 'before': 'ṅi'},
           note='अच्च घेः — औदच्च घेरिति येषामेकमेवेदं सूत्रम्'),
    ),
    '7.3.120': (
        _c('अग्निना (agninā) — by the fire',
           {'gana': 'ghi', 'before': 'āṅ', 'gender': 'a-strī'},
           note='आङो नाऽस्त्रियाम् — पुंसि इति नोक्तम्, अमुना ब्राह्मणकुलेन'),
    ),
    '7.4.1': (
        _c('अचीकरत् (acīkarat) — he had it done',
           {'part': 'upadhā', 'before': 'caṅ-ṇi'},
           note='णौ चङ्युपधाया ह्रस्वः — ओणेः ऋदित्करणं ज्ञापकम्'),
    ),
    '7.4.2': (
        _c('अममालत् (amamālat) — he called her a garland',
           {'gana': 'a-glopi-śās-ṛdit', 'before': 'caṅ-ṇi'},
           note='नाग्लोपिशास्वृदिताम् — हलचोरादेशे तु न सिध्यतीति तदर्थमेतद् वचनम्'),
    ),
    '7.4.3': (
        _c('अबिभ्रजत् (abibhrajat) — he made it shine, beside अबभ्राजत्',
           {'root': 'bhrāj', 'part': 'upadhā', 'before': 'caṅ-ṇi'},
           note='भ्राजभासभाषदीपजीवमीलपीडामन्यतरस्याम् — भ्राजभासोरृदित्करणमपाणिनीयम्'),
    ),
    '7.4.4': (
        _c('अपीप्यत् (apīpyat) — he gave it to drink',
           {'root': 'pib', 'part': 'upadhā', 'before': 'caṅ-ṇi'},
           note='लोपः पिबतेरीच्चाभ्यासस्य — ओः पुयण् वचनं ज्ञापकं णौ स्थानिवद्भावस्य'),
    ),
    '7.4.5': (
        _c('अतिष्ठिपत् (atiṣṭhipat) — he made it stand',
           {'root': 'tiṣṭh', 'part': 'upadhā', 'before': 'caṅ-ṇi'},
           note='तिष्ठतेरित् — अतिष्ठिपत्, अतिष्ठिपताम्, अतिष्ठिपन्'),
    ),
    '7.4.6': (
        _c('अजिघ्रिपत् (ajighripat) — he made it smell, beside अजिघ्रपत्',
           {'root': 'jighr', 'part': 'upadhā', 'before': 'caṅ-ṇi'},
           note='जिघ्रतेर्वा — अजिघ्रिपत्, अजिघ्रपत्'),
    ),
    '7.4.7': (
        _c('अचीकृतत् (acīkṛtat) — he had it cut, beside अचिकीर्तत्',
           {'part': 'ṛ-varṇa', 'before': 'caṅ-ṇi'},
           note='उर्ऋत् — वचनसामर्थ्यादन्तरङ्गा अपि इररारो बाध्यन्ते'),
    ),
    '7.4.8': (
        _c('अवीवृधत् पुरोडाशेन (avīvṛdhat puroḍāśena) — he strengthened it with the cake',
           {'part': 'ṛ-varṇa', 'before': 'caṅ-ṇi', 'chandasi': True},
           note='नित्यं छन्दसि — the option of 7.4.7 does not reach the Veda'),
    ),
    '7.4.9': (
        _c('अवदिग्ये (avadigye) — he flew down',
           {'root': 'day', 'before': 'liṭ'},
           note='दयतेर्दिगि लिटि — दिग्यादेशेन द्विर्वचनस्य बाधनमिष्यते'),
    ),
    '7.4.10': (
        _c('सस्वरतुः (sasvaratuḥ) — those two sounded',
           {'gana': 'ṛ-anta-saṃyoga-ādi', 'before': 'liṭ'},
           note='ऋतश्च संयोगादेर्गुणः — प्रतिषेधविषयेऽपि गुणो यथा स्यात्'),
    ),
    '7.4.11': (
        _c('आनर्च्छ (ānarccha) — he went',
           {'root': 'ṛcch', 'before': 'liṭ'},
           note='ऋच्छत्यॄताम् — ऋच्छेरलघूपधत्वादप्राप्तो गुणो विधीयते, ॠतां तु प्रतिषिद्धः'),
    ),
    '7.4.12': (
        _c('विशश्रतुः (viśaśratuḥ) — those two broke apart',
           {'root': 'śṝ', 'before': 'liṭ'},
           note='शृदॄप्रां ह्रस्वो वा — ह्रस्ववचनमित्वोत्वनिवृत्त्यर्थम्'),
    ),
    '7.4.13': (
        _c('कुमारिका (kumārikā) — a little girl',
           {'gana': 'aṇ-anta', 'before': 'ka'},
           note='केऽणः — अणः इति किम्? गोका, नौका'),
    ),
    '7.4.14': (
        _c('बहुकुमारीकः (bahukumārīkaḥ) — having many girls',
           {'gana': 'aṇ-anta', 'before': 'kap'},
           note='न कपि — स्त्रीप्रत्ययान्तसमासप्रातिपदिकं न भवति'),
    ),
    '7.4.15': (
        _c('बहुखट्वाकः (bahukhaṭvākaḥ) — having many cots, beside बहुखट्वकः',
           {'gana': 'āp-anta', 'before': 'kap'},
           note='आपोऽन्यतरस्याम् — बहुखट्वाकः, बहुखट्वकः'),
    ),
    '7.4.16': (
        _c("शकलाङ्गुष्ठकोऽकरत् (śakalāṅguṣṭhako'karat) — the small-thumbed one did it",
           {'gana': 'ṛ-varṇa-anta', 'before': 'aṅ'},
           note='ऋदृशोऽङि गुणः — दृशेः अदर्शत्, अदर्शताम्, अदर्शन्'),
    ),
    '7.4.17': (
        _c('आस्थत् (āsthat) — he threw',
           {'root': 'as', 'before': 'aṅ'},
           note='अस्यतेस्थुक् — आस्थत्, आस्थताम्, आस्थन्'),
    ),
    '7.4.18': (
        _c('अश्वत् (aśvat) — it swelled',
           {'root': 'śvi', 'before': 'aṅ'},
           note='श्वयतेरः — अश्वत्, अश्वताम्, अश्वन्'),
    ),
    '7.4.19': (
        _c('अपप्तत् (apaptat) — it fell',
           {'root': 'pat', 'before': 'aṅ'},
           note='पतः पुम् — अपप्तत्, अपप्तताम्, अपप्तन्'),
    ),
    '7.4.20': (
        _c('अवोचत् (avocat) — he said',
           {'root': 'vac', 'before': 'aṅ'},
           note='वच उम् — the augment inside the stem, and the vowels merged'),
    ),
    '7.4.21': (
        _c('शेते (śete) — he lies down',
           {'root': 'śīṅ', 'before': 'sārvadhātuka'},
           note='शीङः सार्वधातुके गुणः — सार्वधातुके इति किम्? शिश्ये'),
    ),
    '7.4.22': (
        _c('शय्यते (śayyate) — it is lain upon',
           {'root': 'śīṅ', 'before': 'ya-kṅit'},
           note='अयङ् यि क्ङिति — क्ङितीति किम्? शेयम्'),
    ),
    '7.4.23': (
        _c('समुह्यते (samuhyate) — it is gathered up',
           {'root': 'ūh', 'upasarga': 'upasarga', 'before': 'ya-kṅit'},
           note='उपसर्गाद्ध्रस्व ऊहतेः — उपसर्गादिति किम्? ऊह्यते'),
    ),
    '7.4.24': (
        _c('उदियात् (udiyāt) — may he go up',
           {'root': 'i', 'upasarga': 'upasarga', 'before': 'liṅ'},
           note='एतेर्लिङि — दीर्घत्वे कृते ह्रस्वोऽनेन भवति'),
    ),
    '7.4.25': (
        _c('चीयते (cīyate) — it is gathered',
           {'gana': 'ac-anta', 'before': 'a-kṛt-a-sārvadhātuka-ya-kṅit'},
           note='अकृत्सार्वधातुकयोर्दीर्घः — अकृतिति किम्? प्रकृत्य, प्रहृत्य'),
    ),
    '7.4.26': (
        _c('शुचीकरोति (śucīkaroti) — he makes it clean',
           {'gana': 'ac-anta', 'before': 'cvi'},
           note='च्वौ च — शुचीकरोति, शुचीभवति, शुचीस्यात्'),
    ),
    '7.4.27': (
        _c('मात्रीयति (mātrīyati) — he treats her as a mother',
           {'gana': 'ṛ-anta', 'before': 'a-kṛt-a-sārvadhātuka-ya'},
           note='रीङ् ऋतः — क्ङिति इत्येतन् निवृत्तम्'),
    ),
    '7.4.28': (
        _c('क्रियते (kriyate) — it is done',
           {'gana': 'ṛ-anta', 'before': 'yak'},
           note='रिङ् शयग्लिङ्क्षु — रिङ्वचनं दीर्घनिवृत्त्यर्थम्'),
    ),
    '7.4.29': (
        _c('स्मर्यते (smaryate) — it is remembered',
           {'gana': 'ṛ-anta-saṃyoga-ādi', 'before': 'yak'},
           note='गुणोऽर्तिसंयोगाद्योः — बहिरङ्गलक्षणस्यासिद्धत्वादभक्तत्वाद् वा'),
    ),
    '7.4.30': (
        _c('सास्मर्यते (sāsmaryate) — he remembers over and over',
           {'gana': 'ṛ-anta-saṃyoga-ādi', 'before': 'yaṅ'},
           note='यङि च — हन्तेर्हिंसायां यङि घ्नीभावो वक्तव्यः'),
    ),
    '7.4.31': (
        _c('जेघ्रीयते (jeghrīyate) — he keeps smelling',
           {'stem': 'ghrā', 'before': 'yaṅ'},
           note='ई घ्राध्मोः — जेघ्रीयते, देध्मीयते'),
    ),
    '7.4.32': (
        _c('शुक्लीभवति (śuklībhavati) — it turns white',
           {'gana': 'a-varṇa-anta', 'before': 'cvi'},
           note='अस्य च्वौ — शुक्लीभवति, खट्वीकरोति'),
    ),
    '7.4.33': (
        _c('पुत्रीयति (putrīyati) — he treats him as a son',
           {'gana': 'a-varṇa-anta', 'before': 'kyac'},
           note='क्यचि च — पृथग्योगकरणमुत्तरार्थम्'),
    ),
    '7.4.34': (
        _c('अशनायति (aśanāyati) — he is hungry',
           {'stem': 'aśanāya', 'before': 'kyac'},
           note='अशनायोदन्यधनाया बुभुक्षापिपासागर्द्धेषु — अशनीयति इत्येव अन्यत्र'),
    ),
    '7.4.35': (
        _c('मित्रयुः (mitrayuḥ) — seeking a friend',
           {'gana': 'a-varṇa-anta', 'before': 'kyac', 'chandasi': True},
           note='न च्छन्दस्यपुत्रस्य — किं चोक्तम्? दीर्घत्वम् ईत्वं च'),
    ),
    '7.4.36': (
        _c('अवियोना दुरस्युः (aviyonā durasyuḥ) — ill-disposed',
           {'stem': 'durasyu', 'chandasi': True},
           note='दुरस्युर्द्रविणस्युर्वृषण्यतिरिषण्यति — दुष्टीयतीति प्राप्ते'),
    ),
    '7.4.37': (
        _c('अश्वायन्तो मघवन् (aśvāyanto maghavan) — desiring horses, O bounteous one',
           {'stem': 'aśva', 'before': 'kyac', 'chandasi': True},
           note='अश्वाघस्यात् — एतदेव आत्ववचनं ज्ञापकम्'),
    ),
    '7.4.38': (
        _c('देवायते यजमानाय (devāyate yajamānāya) — he acts as a god for the sacrificer',
           {'stem': 'deva', 'before': 'kyac', 'chandasi': True, 'sense': 'kāṭhaka-yajus'},
           note='देवसुम्नयोर्यजुषि काठके — यजुषि इति किम्? देवाञ् जिगाति सुम्नयुः'),
    ),
    '7.4.39': (
        _c('कव्यन्तः सुमनसः (kavyantaḥ sumanasaḥ) — wishing to be poets',
           {'stem': 'kavi', 'before': 'kyac', 'chandasi': True, 'sense': 'ṛc'},
           note='कव्यध्वरपृतनस्यर्चि लोपः — ऋचि विषये'),
    ),
    '7.4.40': (
        _c('स्थितः (sthitaḥ) — standing',
           {'stem': 'dyati', 'before': 'ta-ādi-kit'},
           note='द्यतिस्यतिमास्थामित्ति किति — तीति किम्? अवदाय'),
    ),
    '7.4.41': (
        _c('निशितम् (niśitam) — sharpened, beside निशातम्',
           {'root': 'śā', 'before': 'ta-ādi-kit'},
           note='शाछोरन्यतरस्याम् — श्यतेरित्त्वं व्रते नित्यम् इति वक्तव्यम्'),
    ),
    '7.4.42': (
        _c('हितः (hitaḥ) — placed, beneficial',
           {'root': 'dhā', 'before': 'ta-ādi-kit'},
           note='दधातेर्हिः — हितः, हितवान्, हित्वा'),
    ),
    '7.4.43': (
        _c('हित्वा राज्यं वनं गतः (hitvā rājyaṃ vanaṃ gataḥ) — leaving the kingdom, he went to the forest',
           {'root': 'hā', 'before': 'ktvā'},
           note='जहातेश्च क्त्वि — जहातेर्निदेशाज् जिहीतेर्न भवति'),
    ),
    '7.4.44': (
        _c('हित्वा शरीरं यातव्यम् (hitvā śarīraṃ yātavyam) — one must go, leaving the body',
           {'root': 'hā', 'before': 'ktvā', 'chandasi': True},
           note='विभाषा छन्दसि — हित्वा, हात्वा'),
    ),
    '7.4.45': (
        _c('गर्भं माता सुधितम् (garbhaṃ mātā sudhitam) — the mother, the embryo well placed',
           {'root': 'sudhita', 'chandasi': True},
           note='सुधितवसुधितनेमधितधिष्वधिषीय च — सुहितम् इति प्राप्ते'),
    ),
    '7.4.46': (
        _c('दत्तः (dattaḥ) — given',
           {'root': 'dā', 'before': 'ta-ādi-kit'},
           note='दो दद् घोः — थान्तेऽदोषस्तस्मात् थान्तम्'),
    ),
    '7.4.47': (
        _c('प्रत्तम् (prattam) — given over',
           {'root': 'dā', 'upasarga': 'ac-anta-upasarga', 'before': 'ta-ādi-kit'},
           note='अच उपसर्गात्तः — अचः इत्येतद् द्विरावर्तयितव्यम्'),
    ),
    '7.4.48': (
        _c('अद्भिः (adbhiḥ) — by the waters',
           {'root': 'ap', 'before': 'bha-ādi'},
           note='अपो भि — भि इति किम्? अप्सु'),
    ),
    '7.4.49': (
        _c('वत्स्यति (vatsyati) — he will dwell',
           {'gana': 's-anta', 'before': 'sa-ādi-ārdhadhātuka'},
           note='सः स्यार्द्धधातुके — आर्धधातुके इति किम्? आस्से, वस्से'),
    ),
    '7.4.50': (
        _c('कर्तासे (kartāse) — you will do',
           {'root': 'tās', 'before': 'sa-ādi'},
           note='तासस्त्योर्लोपः — से इति प्रत्ययमात्रमेतत् पदम्'),
    ),
    '7.4.51': (
        _c('कर्तारौ (kartārau) — those two will do',
           {'root': 'tās', 'before': 'ra-ādi'},
           note='रि च — कर्तारौ, कर्तारः'),
    ),
    '7.4.52': (
        _c('कर्ताहे (kartāhe) — I will do',
           {'root': 'tās', 'before': 'e'},
           note='ह एति — कर्ताहे, अस्तेर्व्यतिहे'),
    ),
    '7.4.53': (
        _c('आदीध्य गतः (ādīdhya gataḥ) — having reflected, he went',
           {'root': 'dīdhī', 'before': 'ya-ādi'},
           note='यीवर्णयोर्दीधीवेव्योः — यीवर्णयोरिति किम्? आदीध्यनम्'),
    ),
    '7.4.54': (
        _c('दित्सति (ditsati) — he wants to give',
           {'root': 'mī', 'before': 'sa-ādi-san'},
           note='सनि मीमाघुरभलभशकपतपदामच इस् — सनि इति किम्? दास्यति'),
    ),
    '7.4.55': (
        _c('आपीप्सति (āpīpsati) — he wants to obtain',
           {'root': 'āp', 'before': 'sa-ādi-san'},
           note='आप्ज्ञप्यृधामीत् — णेः पूर्वविप्रतिषेधेन लोपः, इतरस्य तु ईत्वम्'),
    ),
    '7.4.56': (
        _c('धिप्सति (dhipsati) — he wants to deceive, beside धीप्सति',
           {'root': 'dambh', 'before': 'sa-ādi-san'},
           note='दम्भ इच्च — चकारातीत् च'),
    ),
    '7.4.57': (
        _c('मोक्षते वत्सः स्वयमेव (mokṣate vatsaḥ svayameva) — the calf frees itself',
           {'root': 'muc', 'before': 'sa-ādi-san', 'result': 'akarmaka'},
           note='मुचोऽकर्मकस्य गुणो वा — हलन्ताच् च इति कित्त्वप्रतिषेधो विकल्प्यते'),
    ),
    '7.4.58': (
        _c('मित्सति (mitsati) — he wants to lessen',
           {'root': 'mī', 'before': 'sa-ādi-san'},
           note='अत्र लोपोऽभ्यासस्य — अभ्यासस्य इत्यधिकृतं वेदितव्यमा '
                'अध्यायपरिसमाप्तेः'),
    ),
    '7.4.61': (
        _c('तिष्ठासति (tiṣṭhāsati) — the copy keeps its second sound',
           {'gana': 'śar-pūrva-khay'},
           note='शर्पूर्वाः खयः — शर्पूर्वाः इति किम्? पपाच। खयः इति किम्? '
                'सस्नौ'),
    ),
    '7.4.62': (
        _c('जगाम (jagāma) — the copy of ग is ज',
           {'gana': 'ku-ha'},
           note='कुहोश्चुः — अभ्यासस्य कवर्गहकारयोश् चवर्गादेशो भवति'),
    ),
    '7.4.63': (
        _c('कोकूयते उष्ट्रः (kokūyate uṣṭraḥ) — the camel cries',
           {'root': 'kav', 'before': 'yaṅ'},
           note='न कवतेर्यङि — कवतेः इति विकरणनिर्देशः कौतेः कुवतेश्च '
                'निवृत्त्यर्थः'),
    ),
    '7.4.64': (
        _c('करिकृष्यते (karikṛṣyate) — in the Veda only',
           {'root': 'kṛṣ', 'before': 'yaṅ', 'chandasi': True},
           note='कृषेश्छन्दसि — छन्दसि इति किम्? चरीकृष्यते कृषीवलः'),
    ),
    '7.4.65': (
        _c('दाधर्ति (dādharti) — one of eighteen Vedic forms',
           {'root': 'dādharti', 'chandasi': True},
           note='दाधर्तिदर्धर्ति…आगनीगन्तीति च — अष्टादश छन्दसि विषये '
                'निपात्यन्ते'),
    ),
    '7.4.67': (
        _c('विदिद्युते (vididyute) — it shone forth',
           {'root': 'dyut'},
           note='द्युतिस्वाप्योः सम्प्रसारणम् — स्वापिर् ण्यन्तो गृह्यते'),
    ),
    '7.4.68': (
        _c('विव्यथे (vivyathe) — he wavered',
           {'root': 'vyath', 'before': 'liṭ'},
           note='व्यथो लिटि — हलादिः शेषेण यकारस्य निवृत्तौ प्राप्तायां '
                'सम्प्रसारणं क्रियते'),
    ),
    '7.4.69': (
        _c('ईयतुः (īyatuḥ) — the two went',
           {'root': 'iṇ', 'before': 'liṭ-kit'},
           note='दीर्घ इणः किति — इणो यण् इति यणादेशे कृते स्थानिवद्भावाद् '
                'द्विर्वचनम्'),
    ),
    '7.4.70': (
        _c('आटतुः (āṭatuḥ) — the two wandered',
           {'gana': 'a-ādi', 'before': 'liṭ'},
           note='अत आदेः — अतो गुणे पररूपत्वस्यापवादः। आदेः इति किम्? पपाच'),
    ),
    '7.4.71': (
        _c('आनङ्ग (ānaṅga) — a stem of two consonants',
           {'gana': 'dvi-hal', 'before': 'liṭ', 'part': 'para'},
           note='तस्मान्नुड् द्विहलः — ऋकारैकदेशो रेफो हल्ग्रहणेन गृह्यते'),
    ),
    '7.4.72': (
        _c('व्यानशे (vyānaśe) — it pervaded',
           {'root': 'aśnoti', 'before': 'liṭ', 'part': 'para'},
           note='अश्नोतेश्च — अश्नोतेः इति विकरणनिर्देशोऽश्नातेर् मा भूदिति'),
    ),
    '7.4.73': (
        _c('बभूव (babhūva) — he was',
           {'root': 'bhavati', 'before': 'liṭ'},
           note='भवतेरः — लिटि इत्येव, बुभूषति। बोभूयते'),
    ),
    '7.4.74': (
        _c('ससूव (sasūva) — in the Veda, beside सुषुवे',
           {'root': 'sasūva', 'chandasi': True},
           note='ससूवेति निगमे — सूतेर् लिटि परस्मैपदं वुगागमोऽभ्यासस्य '
                'चात्वं निपात्यते'),
    ),
    '7.4.75': (
        _c('नेनेक्ति (nenekti) — he washes',
           {'root': 'ṇij', 'before': 'ślu'},
           note='निजां त्रयाणां गुणः श्लौ — त्रिग्रहणमुत्तरार्थम्। श्लौ इति '
                'किम्? निनेज'),
    ),
    '7.4.76': (
        _c('बिभर्ति (bibharti) — he bears',
           {'root': 'bhṛñ', 'before': 'ślu'},
           note='भृञामित् — त्रयाणाम् इत्येव, जहाति। श्लौ इत्येव, बभार'),
    ),
    '7.4.77': (
        _c('इयर्ति (iyarti) — he sets in motion',
           {'root': 'ṛ', 'before': 'ślu'},
           note='अर्तिपिपर्त्योश्च — अभ्यासस्य इकारादेशो भवति श्लौ'),
    ),
    '7.4.78': (
        _c('विवष्टि (vivaṣṭi) — he desires, in the Veda',
           {'root': 'vaś', 'before': 'ślu', 'chandasi': True},
           note='बहुलं छन्दसि — न च भवति। ददाति इत्येवं ब्रूयात्'),
    ),
    '7.4.79': (
        _c('पिपक्षति (pipakṣati) — he wants to cook',
           {'gana': 'a-anta', 'before': 'san'},
           note='सन्यतः — अतः इति किम्? लुलूषति। तपरकरणं किम्? पापचिषते'),
    ),
    '7.4.80': (
        _c('यियविषति (yiyaviṣati) — a यण् with अ after it',
           {'gana': 'u-anta', 'before': 'san', 'result': 'yaṇ-a-para'},
           note='ओः पुयण्ज्यपरे — एतदेव पुयण्ज्यपरे इति वचनं ज्ञापकम्'),
    ),
    '7.4.81': (
        _c('सिस्रावयिषति (sisrāvayiṣati) — beside सुस्रावयिषति',
           {'root': 'sru', 'before': 'san', 'result': 'yaṇ-a-para'},
           note='स्रवतिशृणोतिद्रवतिप्रवतिप्लवतिच्यवतीनां वा — ओर् इकारादेशो '
                'वा भवति सनि परतः'),
    ),
    '7.4.84': (
        _c('वनीवच्यते (vanīvacyate) — he goes crookedly',
           {'root': 'vañc', 'before': 'yaṅ'},
           note='नीग्वञ्चुस्रंसुध्वंसुभ्रंसुकसपतपदस्कन्दाम् — यङि यङ्लुकि च'),
    ),
    '7.4.85': (
        _c('जङ्गम्यते (jaṅgamyate) — a nasal-final stem',
           {'gana': 'anunāsika-anta', 'before': 'yaṅ'},
           note='नुगतोऽनुनासिकान्तस्य — नुगित्येतदनुस्वारोपलक्षणार्थं '
                'द्रष्टव्यम्'),
    ),
    '7.4.86': (
        _c('दन्दह्यते (dandahyate) — it burns again and again',
           {'root': 'dah', 'before': 'yaṅ'},
           note='जपजभदहदशभञ्जपशां च — दश इति दंशिर् नकारलोपार्थमेव '
                'निर्दिष्टः'),
    ),
    '7.4.87': (
        _c('चञ्चूर्यते (cañcūryate) — he roams about',
           {'root': 'car', 'before': 'yaṅ'},
           note='चरफलोश्च — अभ्यासस्य नुगागमो भवति यङ्यङ्लुकोः परतः'),
    ),
    '7.4.88': (
        _c('चञ्चूरीति (cañcūrīti) — the अ after the copy',
           {'root': 'car', 'before': 'yaṅ-luk', 'part': 'para'},
           note='उत् परस्यातः — परस्य इति किम्? अभ्यासस्य मा भूत्'),
    ),
    '7.4.89': (
        _c('चूर्तिः (cūrtiḥ) — a going, with no doubling in it',
           {'root': 'car', 'before': 'ta-ādi', 'part': 'para'},
           note='ति च — अनुवर्तमानमपि वचनसामर्थ्यादिह न अभिसम्बध्यते'),
    ),
    '7.4.92': (
        _c('चरीकर्ति (carīkarti) — beside चर्कर्ति and चरिकर्ति',
           {'gana': 'ṛ-anta', 'before': 'yaṅ-luk'},
           note='ऋतश्च — तपरकरणं किम्? किरतेश् चाकर्ति'),
    ),
    '7.4.93': (
        _c('अचीकरत् (acīkarat) — the copy acts as before सन्',
           {'before': 'caṅ-para-ṇi', 'result': 'laghu-anaglopa'},
           note='सन्वल्लघुनि चङ्परेऽनग्लोपे — सन्यतः इत्युक्तम्, चङ्परेऽपि '
                'तथा'),
    ),
    '7.4.94': (
        _c('अजीहरत् (ajīharat) — a light copy lengthens',
           {'gana': 'laghu-abhyāsa', 'before': 'caṅ-para-ṇi', 'result': 'laghu-anaglopa'},
           note='दीर्घो लघोः — लघोः इति किम्? अबिभ्रजत्। अनग्लोपे इत्येव, '
                'अचकथत्'),
    ),
    '7.4.95': (
        _c('अददरत् (adadarat) — a short अ and no lengthening',
           {'root': 'dṝ', 'before': 'caṅ-para-ṇi', 'result': 'laghu-anaglopa'},
           note='अत् स्मृदृत्वरप्रथम्रदस्तॄस्पशाम् — सन्वद्भावादित्त्वं '
                'प्राप्तमनेन बाध्यते'),
    ),
    '7.4.96': (
        _c('अववेष्टत् (avaveṣṭat) — beside अविवेष्टत्',
           {'root': 'veṣṭ', 'before': 'caṅ-para-ṇi', 'result': 'laghu-anaglopa'},
           note='विभाषा वेष्टिचेष्ट्योः — अभ्यासह्रस्वत्वे कृतेऽत्त्वं '
                'पक्षे भवति'),
    ),
    '7.4.97': (
        _c('अजीगणत् (ajīgaṇat) — beside अजगणत्',
           {'root': 'gaṇ', 'before': 'caṅ-para-ṇi', 'result': 'laghu-anaglopa'},
           note='ई च गणः — चकारादत् च। इति सप्तमाध्यायस्य चतुर्थः पादः'),
    ),
    '8.1.1': (
        _c('पचतिपचति (pacatipacati) — the whole word twice, at 8.1.4',
           {'sense': 'nitya'},
           note='सर्वस्य द्वे — शब्दतश्चार्थतश्चोभयथान्तरतमे। प्राक् पदस्य '
                'इत्यतः'),
    ),
    '8.1.2': (
        _c('चौरचौर (cauracaura) — the second copy gets a name',
           {'gana': 'dvirukta-para'},
           note='तस्य परमाम्रेडितम् — आम्रेडितप्रदेशाः आम्रेडितं भर्त्सने '
                'इत्येवमादयः'),
    ),
    '8.1.3': (
        _c('भुङ्क्तेभुङ्क्ते (bhuṅktebhuṅkte) — one accent for two words',
           {'gana': 'āmreḍita'},
           note='अनुदात्तं च — अनुदात्तं च तद् भवति यदाम्रेडितसंज्ञम्'),
    ),
    '8.1.4': (
        _c('ग्रामोग्रामो रमणीयः (grāmogrāmo ramaṇīyaḥ) — every village',
           {'sense': 'vīpsā'},
           note='नित्यवीप्सयोः — केषु नित्यता? तिङ्षु नित्यताव्ययकृत्सु च'),
    ),
    '8.1.5': (
        _c('परिपरि त्रिगर्तेभ्यः (paripari trigartebhyaḥ) — all but them',
           {'word': 'pari', 'sense': 'varjana'},
           note='परेर्वर्जने — वर्जनं परिहारः। परेर्वर्जनेऽसमासे वेति '
                'वक्तव्यम्'),
    ),
    '8.1.6': (
        _c('प्रप्रायमग्निः (praprāyamagniḥ) — the quarter is filled',
           {'word': 'pra', 'sense': 'pāda-pūraṇa', 'chandasi': True},
           note='प्रसमुपोदः पादपूरणे — सामर्थ्यात् छन्दस्येवैतद् विधानम्'),
    ),
    '8.1.7': (
        _c('उपर्युपरि ग्रामम् (uparyupari grāmam) — close by the village',
           {'word': 'upari', 'sense': 'sāmīpya'},
           note='उपर्यध्यधसः सामीप्ये — सामीप्यं प्रत्यासत्तिः कालकृता '
                'देशकृता च'),
    ),
    '8.1.8': (
        _c('माणवक माणवक (māṇavaka māṇavaka) — said in envy',
           {'gana': 'āmantrita', 'position': 'vākya-ādi', 'sense': 'asūyā'},
           note='वाक्यादेरामन्त्रितस्य… — एते च प्रयोक्तृधर्माः, '
                'नाभिधेयधर्माः'),
    ),
    '8.1.9': (
        _c('एकैकमक्षरं पठति (ekaikamakṣaraṃ paṭhati) — one letter at a time',
           {'word': 'eka'},
           note='एकं बहुव्रीहिवत् — बहुव्रीहिवत्त्वे प्रयोजनं '
                'सुब्लोपपुंवद्भावौ'),
    ),
    '8.1.10': (
        _c('गतगतः (gatagataḥ) — gone and gone again, said in distress',
           {'sense': 'ābādha'},
           note='आबाधे च — पीडा प्रयोक्तृधर्मः, नाभिधेयधर्मः'),
    ),
    '8.1.11': (
        _c('पटुपटुः (paṭupaṭuḥ) — like a karmadhāraya, at 8.1.12',
           {'gana': 'guṇavacana', 'sense': 'prakāra'},
           note='कर्मधारयवदुत्तरेषु — प्रयोजनं '
                'सुब्लोपपुंवद्भावान्तोदात्तत्वानि'),
    ),
    '8.1.12': (
        _c('मृदुमृदुः (mṛdumṛduḥ) — soft, in a manner of speaking',
           {'gana': 'guṇavacana', 'sense': 'prakāra'},
           note='प्रकारे गुणवचनस्य — जातीयरोऽनेन द्विर्वचनेन बाधनं नेष्यते'),
    ),
    '8.1.13': (
        _c('प्रियप्रियेण ददाति (priyapriyeṇa dadāti) — he gives freely',
           {'word': 'priya', 'sense': 'akṛcchra'},
           note='अकृच्छ्रे प्रियसुखयोरन्यतरस्याम् — कृच्छ्रं दुःखम्, '
                'तदभावोऽकृच्छ्रम्'),
    ),
    '8.1.14': (
        _c('यथायथम् (yathāyatham) — each according to its own',
           {'word': 'yathāyatham', 'sense': 'yathāsva'},
           note='यथास्वे यथायथम् — यथाशब्दस्य द्विर्वचनं नपुंसकलिङ्गता च '
                'निपात्यते'),
    ),
    '8.1.15': (
        _c('द्वन्द्वं मन्त्रयन्ते (dvandvaṃ mantrayante) — they speak apart',
           {'word': 'dvandvam', 'sense': 'rahasya'},
           note='द्वन्द्वं रहस्यमर्यादावचन… — रहस्यं द्वन्द्वशब्दवाच्यम्, '
                'इतरे विषयभूताः'),
    ),
    '8.1.16': (
        _c('पचसि देवदत्त (pacasi devadatta) — of a word, at 8.1.19',
           {'gana': 'āmantrita', 'after': 'pada', 'position': 'a-pādādi'},
           note='पदस्य — प्रागपदान्ताधिकारात्। क्वचित् स्थानषष्ठी '
                'क्वचिदवयवषष्ठी'),
    ),
    '8.1.17': (
        _c('देवदत्त पचसि (devadatta pacasi) — nothing stands before it',
           {'gana': 'āmantrita', 'position': 'a-pādādi'},
           note='पदात् — प्राक् कुत्सने च सुप्यगोत्रादौ इत्येतस्मात्'),
    ),
    '8.1.18': (
        _c('पचसि देवदत्त (pacasi devadatta) — toneless throughout',
           {'gana': 'āmantrita', 'after': 'pada', 'position': 'a-pādādi'},
           note='अनुदात्तं सर्वमपादादौ — एतत् त्रयमधिकृतमापादपरिसमाप्तेः'),
    ),
    '8.1.19': (
        _c('पचसि देवदत्त (pacasi devadatta) — the vocative loses its accent',
           {'gana': 'āmantrita', 'after': 'pada', 'position': 'a-pādādi'},
           note='आमन्त्रितस्य च — समानवाक्ये निघातयुष्मदस्मदादेशा वक्तव्याः'),
    ),
    '8.1.20': (
        _c('ग्रामो वां स्वम् (grāmo vāṃ svam) — the village is yours',
           {'gana': 'yuṣmad-asmad', 'case': 'dvivacana', 'after': 'pada', 'position': 'a-pādādi'},
           note='युष्मदस्मदोः… वान्नावौ — द्विवचनान्तयोरेतावादेशौ '
                'विज्ञायेते'),
    ),
    '8.1.21': (
        _c('ग्रामो वः स्वम् (grāmo vaḥ svam) — the village is yours',
           {'gana': 'yuṣmad-asmad', 'case': 'bahuvacana', 'after': 'pada', 'position': 'a-pādādi'},
           note='बहुवचने वस्नसौ — षष्ठीचतुर्थीद्वितीयास्थयोर्यथासंख्यम्'),
    ),
    '8.1.22': (
        _c('ग्रामस्ते स्वम् (grāmaste svam) — the village is yours',
           {'gana': 'yuṣmad-asmad', 'case': 'ekavacana', 'after': 'pada', 'position': 'a-pādādi'},
           note='तेमयावेकवचनस्य — द्वितीयान्तस्यादेशान्तरविधानसामर्थ्यात्'),
    ),
    '8.1.23': (
        _c('ग्रामस्त्वा पश्यति (grāmastvā paśyati) — the village sees you',
           {'gana': 'yuṣmad-asmad', 'case': 'ekavacana-dvitīyā', 'after': 'pada', 'position': 'a-pādādi'},
           note='त्वामौ द्वितीयायाः — एकवचनस्येति वर्तते'),
    ),
    '8.1.24': (
        _c('ग्रामस्तव च स्वम् (grāmastava ca svam) — with च, no enclitic',
           {'gana': 'yuṣmad-asmad', 'case': 'dvivacana', 'after': 'pada', 'joined': 'ca', 'position': 'a-pādādi'},
           note='न चवाहाहैवयुक्ते — पूर्वेण प्रकरणेन प्राप्ताः '
                'प्रतिषिध्यन्ते'),
    ),
    '8.1.25': (
        _c('ग्रामस्तव स्वं समीक्ष्यागतः (samīkṣyāgataḥ) — having considered',
           {'gana': 'yuṣmad-asmad', 'after': 'pada', 'joined': 'paśyārtha'},
           note='पश्यार्थैश्चानालोचने — आलोचनं चक्षुर्विज्ञानम्'),
    ),
    '8.1.26': (
        _c('ग्रामे कम्बलस्तव स्वम् (kambalastava svam) — beside कम्बलस्ते',
           {'gana': 'yuṣmad-asmad', 'after': 'sa-pūrvā-prathamā'},
           note='सपूर्वायाः प्रथमाया विभाषा — विद्यमानपूर्वात् प्रथमान्तात् '
                'पदात्'),
    ),
    '8.1.27': (
        _c('पचति गोत्रम् (pacati gotram) — said in contempt',
           {'gana': 'gotrādi', 'after': 'tiṅ', 'sense': 'kutsana'},
           note='तिङो गोत्रादीनि कुत्सनाभीक्ष्ण्ययोः — ब्रुवः कन् निपातनात्'),
    ),
    '8.1.28': (
        _c('देवदत्तः पचति (devadattaḥ pacati) — the verb goes toneless',
           {'gana': 'tiṅ', 'after': 'a-tiṅ'},
           note='तिङ्ङतिङः — तिङिति किम्? नीलमुत्पलम्। अतिङ इति किम्? भवति '
                'पचति'),
    ),
    '8.1.29': (
        _c('श्वः कर्ता (śvaḥ kartā) — he will do it tomorrow',
           {'gana': 'luṭ', 'after': 'a-tiṅ'},
           note='न लुट् — पूर्वेणातिप्रसक्ते प्रतिषेध आरभ्यते'),
    ),
    '8.1.30': (
        _c('यत् करोति (yat karoti) — with यत्, the accent stays',
           {'gana': 'tiṅ', 'after': 'a-tiṅ', 'joined': 'yat'},
           note='निपातैर्यद्यदिहन्त… — नेति वर्तते'),
    ),
    '8.1.31': (
        _c('नह भोक्ष्यसे (naha bhokṣyase) — will you not eat, then',
           {'gana': 'tiṅ', 'after': 'a-tiṅ', 'joined': 'naha', 'sense': 'pratyārambha'},
           note='नह प्रत्यारम्भे — चोदितस्यावधीरणे उपालिप्सया'),
    ),
    '8.1.32': (
        _c('सत्यं भोक्ष्यसे (satyaṃ bhokṣyase) — will you really eat',
           {'gana': 'tiṅ', 'after': 'a-tiṅ', 'joined': 'satyam', 'sense': 'praśna'},
           note='सत्यं प्रश्ने — प्रश्न इति किम्? सत्यं वक्ष्यामि नानृतम्'),
    ),
    '8.1.33': (
        _c('अङ्ग कुरु (aṅga kuru) — do it, then',
           {'gana': 'tiṅ', 'after': 'a-tiṅ', 'joined': 'aṅga', 'sense': 'aprātilomya'},
           note='अङ्गाप्रातिलोम्ये — कूजनमनभिमतमसौ कुर्वन् प्रतिलोमो भवति'),
    ),
    '8.1.34': (
        _c('स हि कुरु (sa hi kuru) — do it, you',
           {'gana': 'tiṅ', 'after': 'a-tiṅ', 'joined': 'hi', 'sense': 'aprātilomya'},
           note='हि च — अप्रातिलोम्य इत्येव, स हि कूज३ वृषल'),
    ),
    '8.1.35': (
        _c('अनृतं हि मत्तो वदति (anṛtaṃ hi matto vadati) — neither is toneless',
           {'gana': 'tiṅ', 'after': 'a-tiṅ', 'joined': 'hi', 'chandasi': True},
           note='छन्दस्यनेकमपि साकाङ्क्षम् — कदाचिदेकं कदाचिदनेकम्'),
    ),
    '8.1.36': (
        _c('यावद् भुङ्क्ते (yāvad bhuṅkte) — as long as he eats',
           {'gana': 'tiṅ', 'after': 'a-tiṅ', 'joined': 'yāvat'},
           note='यावद्यथाभ्याम् — परेणापि योगे भवति प्रतिषेधः'),
    ),
    '8.1.37': (
        _c('यावत् पचति शोभनम् (yāvat pacati śobhanam) — how well he cooks',
           {'gana': 'tiṅ', 'after': 'a-tiṅ', 'joined': 'yāvat', 'sense': 'pūjā', 'position': 'anantara'},
           note='पूजायां नानन्तरम् — किं तर्हि? अनुदात्तमेव'),
    ),
    '8.1.38': (
        _c('यावत् प्रपचति शोभनम् (yāvat prapacati śobhanam) — a preverb makes the gap',
           {'gana': 'tiṅ', 'after': 'a-tiṅ', 'joined': 'yāvat', 'sense': 'pūjā', 'position': 'upasarga-vyapeta'},
           note='उपसर्गव्यपेतं च — उपसर्गव्यवधानार्थोऽयमारम्भः'),
    ),
    '8.1.39': (
        _c('पश्य माणवको भुङ्क्ते शोभनम् (paśya māṇavako bhuṅkte) — see how he eats',
           {'gana': 'tiṅ', 'after': 'a-tiṅ', 'joined': 'paśya', 'sense': 'pūjā'},
           note='तुपश्यपश्यताहैः पूजायाम् — पुनः पूजायामित्युच्यते '
                'निघातप्रतिषेधार्थम्'),
    ),
    '8.1.40': (
        _c('अहो देवदत्तः पचति शोभनम् (aho devadattaḥ pacati) — how well he cooks',
           {'gana': 'tiṅ', 'after': 'a-tiṅ', 'joined': 'aho', 'sense': 'pūjā'},
           note='अहो च — पृथग्योगकरणमुत्तरार्थम्'),
    ),
    '8.1.41': (
        _c('कटमहो करिष्यसि (kaṭamaho kariṣyasi) — you, make a mat',
           {'gana': 'tiṅ', 'after': 'a-tiṅ', 'joined': 'aho', 'sense': 'śeṣa'},
           note='शेषे विभाषा — असूयावचनमेतत्। शेषवचनं विस्पष्टार्थम्'),
    ),
    '8.1.42': (
        _c('पुरा विद्योतते विद्युत् (purā vidyotate vidyut) — before it flashes',
           {'gana': 'tiṅ', 'after': 'a-tiṅ', 'joined': 'purā', 'sense': 'parīpsā'},
           note='पुरा च परीप्सायाम् — परीप्सा त्वरा। भविष्यदासत्तिं '
                'द्योतयति'),
    ),
    '8.1.43': (
        _c('ननु करोमि भोः (nanu karomi bhoḥ) — may I do it, sir',
           {'gana': 'tiṅ', 'after': 'a-tiṅ', 'joined': 'nanu', 'sense': 'anujñaiṣaṇā'},
           note='नन्वित्यनुज्ञैषणायाम् — अनुज्ञायाः एषणा प्रार्थना'),
    ),
    '8.1.44': (
        _c('किं देवदत्तः पचति (kiṃ devadattaḥ pacati) — is he cooking',
           {'gana': 'tiṅ', 'after': 'a-tiṅ', 'joined': 'kim', 'sense': 'kriyāpraśna', 'position': 'anupasarga-apratiṣiddha'},
           note='किं क्रियाप्रश्नेऽनुपसर्गमप्रतिषिद्धम् — अत्र केचिदाहुः, '
                'अपरे त्वाहुः'),
    ),
    '8.1.45': (
        _c('देवदत्तः पचति, आहोस्वित् पठति (āhosvit paṭhati) — or is he reading',
           {'gana': 'tiṅ', 'after': 'a-tiṅ', 'joined': 'kim-lopa', 'sense': 'kriyāpraśna', 'position': 'anupasarga-apratiṣiddha'},
           note='लोपे विभाषा — प्राप्तविभाषेयं किमर्थेन योगात्'),
    ),
    '8.1.46': (
        _c('एहि मन्ये ओदनं भोक्ष्यसे (ehi manye odanaṃ bhokṣyase) — in jest',
           {'gana': 'lṛṭ', 'after': 'a-tiṅ', 'joined': 'ehi-manye', 'sense': 'prahāsa'},
           note='एहिमन्ये प्रहासे लृट् — प्रकृष्टो हासः प्रहासः, क्रीडा'),
    ),
    '8.1.47': (
        _c('जातु भोक्ष्यसे (jātu bhokṣyase) — you may eat sometime',
           {'gana': 'tiṅ', 'after': 'a-tiṅ', 'joined': 'jātu', 'position': 'a-pūrva'},
           note='जात्वपूर्वम् — अपूर्वमिति किम्? कटं जातु करिष्यति'),
    ),
    '8.1.48': (
        _c('कश्चिद् भुङ्क्ते (kaścid bhuṅkte) — someone is eating',
           {'gana': 'kiṃvṛtta', 'after': 'a-tiṅ', 'joined': 'cit', 'position': 'a-pūrva'},
           note='किम्वृत्तं च चिदुत्तरम् — डतरडतमौ च प्रत्ययौ'),
    ),
    '8.1.49': (
        _c('आहो भुङ्क्ते (āho bhuṅkte) — or is he eating',
           {'gana': 'tiṅ', 'after': 'a-tiṅ', 'joined': 'āho', 'position': 'anantara-a-pūrva'},
           note='आहो उताहो चानन्तरम् — अपूर्वमित्येव, देवदत्त आहो भुङ्क्ते'),
    ),
    '8.1.50': (
        _c('आहो देवदत्तः पचति (āho devadattaḥ pacati) — a word stands in the gap',
           {'gana': 'tiṅ', 'after': 'a-tiṅ', 'joined': 'āho'},
           note='शेषे विभाषा — कश्च शेषः? यदन्यदनन्तरात्'),
    ),
    '8.1.51': (
        _c('आगच्छ देवदत्त, ग्रामं द्रक्ष्यसि (grāmaṃ drakṣyasi) — come and see',
           {'gana': 'lṛṭ', 'joined': 'gatyartha-loṭ', 'position': 'samāna-kāraka'},
           note='गत्यर्थलोटा लृण्न चेत् कारकं सर्वान्यत् — कर्तृकर्मणी '
                'एवात्र गृह्येते'),
    ),
    '8.1.52': (
        _c('आगच्छ देवदत्त, ग्रामं पश्य (grāmaṃ paśya) — come and see it',
           {'gana': 'loṭ', 'joined': 'gatyartha-loṭ', 'position': 'samāna-kāraka'},
           note='लोट् च — लोडन्तयोरेकं कारकं यदि भवतीत्यर्थः'),
    ),
    '8.1.53': (
        _c('आगच्छ देवदत्त ग्रामं प्रविश (grāmaṃ praviśa) — come and enter',
           {'gana': 'loṭ', 'joined': 'gatyartha-loṭ', 'position': 'sopasarga-anuttama'},
           note='विभाषितं सोपसर्गमनुत्तमम् — प्राप्तविभाषेयम्'),
    ),
    '8.1.54': (
        _c('हन्त प्रविश (hanta praviśa) — go in, then',
           {'gana': 'loṭ', 'joined': 'hanta', 'position': 'sopasarga-anuttama'},
           note='हन्त च — गत्यर्थलोटं वर्जयित्वा पूर्वं सर्वमनुवर्तते'),
    ),
    '8.1.55': (
        _c('आम् पचसि देवदत्त (ām pacasi devadatta) — one word between',
           {'gana': 'āmantrita', 'joined': 'ām', 'position': 'ekāntara', 'sense': 'anantika'},
           note='आम एकान्तरमामन्त्रितमनन्तिके — भो इत्यामन्त्रितान्तमपि'),
    ),
    '8.1.56': (
        _c('इन्दवो वामुशन्ति हि (indavo vām uśanti hi) — हि after the verb',
           {'gana': 'tiṅ', 'before': 'yat-hi-tu-para', 'chandasi': True},
           note='यद्धितुपरं छन्दसि — आमन्त्रितमस्वरितत्वान्नानुवर्तते'),
    ),
    '8.1.57': (
        _c('देवदत्तः पचति चन (devadattaḥ pacati cana) — चन after the verb',
           {'gana': 'tiṅ', 'after': 'a-gati', 'before': 'cana-cid-iva-gotrādi-taddhita-āmreḍita'},
           note='चनचिदिवगोत्रादितद्धिताम्रेडितेष्वगतेः — गोत्रादयः '
                'कुत्सनाभीक्ष्ण्ययोरेव'),
    ),
    '8.1.58': (
        _c('देवदत्तः पचति च, खादति च (pacati ca, khādati ca) — both accented',
           {'gana': 'tiṅ', 'after': 'a-gati', 'before': 'cādi'},
           note='चादिषु च — न चवाहाहैवयुक्ते इत्यत्र ये निर्दिष्टास्त इह '
                'परिगृह्यन्ते'),
    ),
    '8.1.59': (
        _c('गर्दभांश्च कालयति (gardabhāṃśca kālayati) — the first keeps its accent',
           {'gana': 'prathamā-tiṅ', 'joined': 'ca'},
           note='चवायोगे प्रथमा — प्रथमाग्रहणं द्वितीयादेस्तिङन्तस्य मा '
                'भूदिति'),
    ),
    '8.1.60': (
        _c('स्वयं ह रथेन याति (svayaṃ ha rathena yāti) — a breach of custom',
           {'gana': 'prathamā-tiṅ', 'joined': 'ha', 'sense': 'kṣiyā'},
           note='हेति क्षियायाम् — क्षिया धर्मव्यतिक्रमः, आचारभेदः'),
    ),
    '8.1.61': (
        _c('त्वमह ग्रामं गच्छ (tvamaha grāmaṃ gaccha) — you to the village',
           {'gana': 'prathamā-tiṅ', 'joined': 'aha', 'sense': 'viniyoga'},
           note='अहेति विनियोगे च — नानाप्रयोजनो नियोगो विनियोगः'),
    ),
    '8.1.62': (
        _c('देवदत्त एव ग्रामं गच्छतु (devadatta eva grāmaṃ gacchatu) — with च unsaid',
           {'gana': 'prathamā-tiṅ', 'joined': 'ca-lopa', 'sense': 'avadhāraṇa'},
           note='चाहलोप एवेत्यवधारणम् — समानकर्तृके चलोपः, '
                'नानाकर्तृकेऽहलोपः'),
    ),
    '8.1.63': (
        _c('शुक्ला व्रीहयो भवन्ति (śuklā vrīhayo bhavanti) — with च unsaid',
           {'gana': 'prathamā-tiṅ', 'joined': 'cādi-lopa'},
           note='चादिलोपे विभाषा — चादयो न चवाहाहैवयुक्ते इति '
                'सूत्रनिर्दिष्टाः'),
    ),
    '8.1.64': (
        _c('अहर्वै देवानामासीत् (aharvai devānām āsīt) — the first is spared',
           {'gana': 'prathamā-tiṅ', 'joined': 'vai', 'chandasi': True},
           note='वैवावेति च च्छन्दसि — प्रथमा तिङ्विभक्तिर्विभाषा'),
    ),
    '8.1.65': (
        _c('प्रजामेका जिन्वति (prajām ekā jinvati) — one quickens offspring',
           {'gana': 'prathamā-tiṅ', 'joined': 'eka', 'chandasi': True},
           note='एकान्याभ्यां समर्थाभ्याम् — जिन्वतीत्येतत् पक्षे न '
                'निहन्यते'),
    ),
    '8.1.66': (
        _c('यो भुङ्क्ते (yo bhuṅkte) — he who eats',
           {'gana': 'tiṅ', 'after': 'yadvṛtta'},
           note='यद्वृत्तान्नित्यम् — यत्र पदे यच्छब्दो वर्तते तत् सर्वं '
                'यद्वृत्तम्'),
    ),
    '8.1.67': (
        _c('काष्ठाध्यापकः (kāṣṭhādhyāpakaḥ) — a teacher and a half',
           {'gana': 'pūjita', 'after': 'pūjana-kāṣṭhādi'},
           note='पूजनात् पूजितमनुदात्तम् — पूजनवचनेभ्यः काष्ठादिभ्यः'),
    ),
    '8.1.68': (
        _c('यत् काष्ठं प्रपचति (yat kāṣṭhaṃ prapacati) — preverb and verb both toneless',
           {'gana': 'tiṅ', 'after': 'pūjana-kāṣṭhādi', 'position': 'sagati'},
           note='सगतिरपि तिङ् — प्रतिषेधे प्राप्ते पुनर्विधानम्'),
    ),
    '8.1.69': (
        _c('पचति पूति (pacati pūti) — he cooks it foully',
           {'gana': 'tiṅ', 'before': 'sup-kutsana-a-gotrādi', 'position': 'sagati'},
           note='कुत्सने च सुप्यगोत्रादौ — पदादिति निवृत्तम्'),
    ),
    '8.1.70': (
        _c('अभ्युद्धरति (abhyuddharati) — a string heard as one word',
           {'gana': 'gati', 'before': 'gati'},
           note='गतिर्गतौ — गताविति किम्? आ मन्द्रैरिन्द्र हरिभिर्याहि'),
    ),
    '8.1.71': (
        _c('यत् प्रपचति (yat prapacati) — the preverb before an accented verb',
           {'gana': 'gati', 'before': 'udāttavat-tiṅ'},
           note='तिङि चोदात्तवति — तिङ्ग्रहणमुदात्तवतः परिमाणार्थम्'),
    ),
    '8.1.72': (
        _c('देवदत्त यज्ञदत्त (devadatta yajñadatta) — the first counts as absent',
           {'gana': 'āmantrita', 'position': 'pūrva'},
           note='आमन्त्रितं पूर्वमविद्यमानवत् — प्रयोजनानि '
                'आमन्त्रिततिङ्निघातयुष्मदस्मदादेशाभावाः'),
    ),
    '8.1.73': (
        _c('अग्ने गृहपते (agne gṛhapate) — the first is there after all',
           {'gana': 'āmantrita-sāmānyavacana', 'before': 'āmantrita-samānādhikaraṇa'},
           note='नामन्त्रिते समानाधिकरणे सामान्यवचनम् — किं तर्हि? '
                'विद्यमानवदेव'),
    ),
    '8.1.74': (
        _c('देवाः शरण्याः (devāḥ śaraṇyāḥ) — O gods who give refuge',
           {'gana': 'āmantrita-bahuvacana', 'before': 'āmantrita-viśeṣavacana'},
           note='विभाषितं विशेषवचने बहुवचनम् — विशेषवचनग्रहणं '
                'विस्पष्टार्थम्'),
    ),
    '8.2.4': (
        _c('कुमार्यौ (kumāryau) — the semivowel hands its accent forward',
           {'gana': 'udātta-svarita-yaṇ-para'},
           note='उदात्तस्वरितयोर्यणः स्वरितोऽनुदात्तस्य — '
                'उदात्तनिवृत्तिस्वरेणायमीकार उदात्तः'),
    ),
    '8.2.5': (
        _c('अग्नी (agnī) — the merged vowel keeps the high tone',
           {'gana': 'ekādeśa-udātta'},
           note='एकादेश उदात्तेनोदात्तः — पररूपे कर्तव्ये '
                'स्वरितस्यासिद्धत्वात्'),
    ),
    '8.2.6': (
        _c('सूत्थितः (sūtthitaḥ) — heard with either accent',
           {'gana': 'ekādeśa-udātta', 'before': 'pada-ādi-anudātta'},
           note='स्वरितो वाऽनुदात्ते पदादौ — सुः पूजायाम् इति कर्मप्रवचनीयः'),
    ),
    '8.2.7': (
        _c("राजा (rājā) — the stem's final न् is gone",
           {'gana': 'prātipadika-n-anta'},
           note='नलोपः प्रातिपदिकान्तस्य — अन्तग्रहणं किम्? राजानौ'),
    ),
    '8.2.8': (
        _c('हे राजन् (he rājan) — the vocative keeps its न्',
           {'gana': 'prātipadika-n-anta', 'before': 'sambuddhi'},
           note='न ङिसम्बुद्ध्योः — प्रत्ययलक्षणेन प्रातिपदिकसंज्ञा न '
                'प्रतिषिध्यते'),
    ),
    '8.2.9': (
        _c('किंवान् (kiṃvān) — मतुप् after a म्',
           {'gana': 'ma-a-anta-upadha', 'before': 'matup'},
           note='मादुपधायाश्च मतोर्वोऽयवादिभ्यः — मकारावर्णविशिष्टया चोपधया'),
    ),
    '8.2.10': (
        _c('अग्निचित्वान् (agnicitvān) — मतुप् after a stop',
           {'gana': 'jhay-anta', 'before': 'matup'},
           note='झयः — झयन्तादुत्तरस्य मतोर्व इत्ययमादेशो भवति'),
    ),
    '8.2.11': (
        _c('अहीवती (ahīvatī) — a name, and the व् comes',
           {'before': 'matup', 'sense': 'saṃjñā'},
           note='संज्ञायाम् — संज्ञायां विषये मतोर्व इत्ययमादेशो भवति'),
    ),
    '8.2.12': (
        _c('आसन्दीवान् ग्रामः (āsandīvān grāmaḥ) — a laid-down name',
           {'word': 'āsandīvat', 'sense': 'saṃjñā'},
           note='आसन्दीवदष्ठीवत्… — वत्वं पूर्वेणैव सिद्धम्, आदेशार्थानि '
                'निपातनानि'),
    ),
    '8.2.13': (
        _c('उदन्वान् (udanvān) — that in which water is held',
           {'word': 'udanvat', 'sense': 'udadhi'},
           note='उदन्वानुदधौ च — उदकवान् घट इत्यत्र दधात्यर्थो न विवक्ष्यते'),
    ),
    '8.2.14': (
        _c('राजन्वान् देशः (rājanvān deśaḥ) — a well-governed country',
           {'word': 'rājanvat', 'sense': 'saurājya'},
           note='राजन्वान् सौराज्ये — राजवानित्येवान्यत्र'),
    ),
    '8.2.15': (
        _c('त्रिवती (trivatī) — in the Veda, after an इ',
           {'gana': 'i-varṇa-repha-anta', 'before': 'matup', 'chandasi': True},
           note='छन्दसीरः — इवर्णान्ताद् रेफान्ताच्चोत्तरस्य मतोर्वत्वम्'),
    ),
    '8.2.16': (
        _c('अक्षण्वन्तः (akṣaṇvantaḥ) — having eyes, in the Veda',
           {'gana': 'an-anta', 'before': 'matup', 'chandasi': True},
           note='अनो नुट् — नुटोऽसिद्धत्वात्तस्य च वत्वं न भवति'),
    ),
    '8.2.17': (
        _c('सुपथिन्तरः (supathintaraḥ) — on a better road',
           {'gana': 'n-anta', 'before': 'gha', 'chandasi': True},
           note='नाद्घस्य — भूरिदाव्नस्तुड् वक्तव्यः। ईद्रथिनः'),
    ),
    '8.2.18': (
        _c('कल्प्ता (kalptā) — the र् is heard as ल्',
           {'word': 'kṛp'},
           note='कृपो रो लः — र इति श्रुतिसामान्यमुपादीयते'),
    ),
    '8.2.19': (
        _c('पलायते (palāyate) — he runs away',
           {'gana': 'upasarga', 'before': 'ayati'},
           note='उपसर्गस्यायतौ — येन नाव्यवधानं तेन व्यवहितेऽपि '
                'वचनप्रामाण्यात्'),
    ),
    '8.2.20': (
        _c('निजेगिल्यते (nijegilyate) — he keeps swallowing',
           {'word': 'gṝ', 'before': 'yaṅ'},
           note='ग्रो यङि — केचिद् गिरतेर्गृणातेश्च, अपरे गिरतेरेव'),
    ),
    '8.2.21': (
        _c('निगिलति (nigilati) — beside निगिरति, by a fixed option',
           {'word': 'gṝ', 'before': 'ac-ādi'},
           note='अचि विभाषा — इयं तु व्यवस्थितविभाषा'),
    ),
    '8.2.22': (
        _c('पल्यङ्कः (palyaṅkaḥ) — a couch, beside पर्यङ्कः',
           {'word': 'pari', 'before': 'aṅka'},
           note='परेश्च घाङ्कयोः — घ इति स्वरूपग्रहणमत्रेष्यते'),
    ),
    '8.2.23': (
        _c('गोमान् (gomān) — the cluster loses its last sound',
           {'gana': 'saṃyoga-anta', 'before': 'pada-anta'},
           note='संयोगान्तस्य लोपः — जश्त्वे तु नाप्राप्ते तदारभ्यते'),
    ),
    '8.2.24': (
        _c('गोभिरक्षाः (gobhirakṣāḥ) — the स् goes, not the र्',
           {'gana': 'repha-saṃyoga-anta', 'before': 'pada-anta'},
           note='रात् सस्य — सिचश्छान्दसत्वादीडभावो बहुलं छन्दसीति वचनात्'),
    ),
    '8.2.25': (
        _c('अलविध्वम् (alavidhvam) — you cut, and the स् is gone',
           {'gana': 'sic', 'before': 'dha-ādi'},
           note='धि च — इतः प्रभृति सिचः सकारस्य लोप इष्यते'),
    ),
    '8.2.26': (
        _c('अभित्त (abhitta) — he split it',
           {'gana': 'jhal-anta-sic', 'before': 'jhal'},
           note='झलो झलि — सिचः सकारलोपस्यासिद्धत्वात् सः स्यार्धधातुके'),
    ),
    '8.2.27': (
        _c('अकृत (akṛta) — he made it for himself',
           {'gana': 'hrasva-anta-aṅga', 'before': 'jhal'},
           note='ह्रस्वादङ्गात् — ह्रस्वादिति किम्? अच्योष्ट'),
    ),
    '8.2.28': (
        _c('अदेवीत् (adevīt) — he played',
           {'gana': 'iṭ-anta', 'before': 'īṭ'},
           note='इट ईटि — इट इति किम्? अकार्षीत्'),
    ),
    '8.2.29': (
        _c('लग्नः (lagnaḥ) — attached, with the स् gone',
           {'gana': 'sa-ka-saṃyoga-ādi', 'before': 'pada-anta'},
           note='स्कोः संयोगाद्योरन्ते च — झलि सङीति वक्तव्यम्'),
    ),
    '8.2.30': (
        _c('वाक् (vāk) — speech, with the palatal gone hard',
           {'gana': 'cu', 'before': 'jhal'},
           note='चोः कुः — चवर्गस्य कवर्गादेशो झलि परतः पदान्ते च'),
    ),
    '8.2.31': (
        _c('सोढा (soḍhā) — one who bears it',
           {'gana': 'ha', 'before': 'jhal'},
           note='हो ढः — हकारस्य ढकारादेशो भवति झलि परतः पदान्ते च'),
    ),
    '8.2.32': (
        _c('दग्धा (dagdhā) — one who burns it',
           {'root': 'da-ādi-dhātu', 'before': 'jhal'},
           note='दादेर्धातोर्घः — दादेरिति किम्? लेढा'),
    ),
    '8.2.33': (
        _c('मित्रध्रुक् (mitradhruk) — beside मित्रध्रुट्',
           {'root': 'druh', 'before': 'jhal'},
           note='वा द्रुहमुहष्णुहष्णिहाम् — हकारस्य वा घकारादेशः'),
    ),
    '8.2.34': (
        _c('उपानत् (upānat) — a sandal, bound to the foot',
           {'root': 'nah', 'before': 'jhal'},
           note='नहो धः — नहो हकारस्य धकारादेशो झलि परे पदान्ते च'),
    ),
    '8.2.35': (
        _c('इदमात्थ (idamāttha) — this you have said',
           {'root': 'āh', 'before': 'jhal'},
           note='आहस्थः — आदेशान्तरकरणं झषस्तथोर्धोऽध इत्यस्य '
                'निवृत्त्यर्थम्'),
    ),
    '8.2.36': (
        _c('मूलवृट् (mūlavṛṭ) — a root-cutter',
           {'root': 'yaj', 'before': 'jhal'},
           note='व्रश्चभ्रस्जसृजमृजयजराजभ्राजच्छशां षः'),
    ),
    '8.2.37': (
        _c('बोद्धा (boddhā) — the aspiration moves to the front',
           {'gana': 'ekāc-jhaṣ-anta-baś', 'before': 'dhva'},
           note='एकाचो बशो भष् झषन्तस्य स्ध्वोः — चत्वारो बशः स्थानिनो '
                'भषादेशाश्चत्वार एव'),
    ),
    '8.2.38': (
        _c('धत्तः (dhattaḥ) — the two of them place it',
           {'root': 'dadh', 'before': 'ta'},
           note='दधस्तथोश्च — वचनसामर्थ्यादातो लोपस्य स्थानिवद्भावः'),
    ),
    '8.2.39': (
        _c('वागत्र (vāgatra) — speech here, and the क् goes soft',
           {'gana': 'jhal-anta', 'before': 'pada-anta'},
           note='झलां जशोऽन्ते — अन्तग्रहणं झलीत्येतस्य निवृत्त्यर्थम्'),
    ),
    '8.2.40': (
        _c('लब्धा (labdhā) — one who obtains it',
           {'gana': 'jhaṣ', 'before': 'ta'},
           note='झषस्तथोर्धोऽधः — दधातिं वर्जयित्वा'),
    ),
    '8.2.41': (
        _c('लेक्ष्यति (lekṣyati) — he will lick',
           {'gana': 'ṣa-ḍha', 'before': 'sa'},
           note='षढोः कः सि — सीति किम्? पिनष्टि, लेढि'),
    ),
    '8.2.42': (
        _c('भिन्नः (bhinnaḥ) — split, with both sounds turned न्',
           {'gana': 'ra-da-para'},
           note='रदाभ्यां निष्ठातो नः पूर्वस्य च दः'),
    ),
    '8.2.43': (
        _c('म्लानः (mlānaḥ) — withered',
           {'gana': 'saṃyoga-ādi-āt-anta-yaṇvat'},
           note='संयोगादेरातो धातोर्यण्वतः — आत इति किम्? च्युतः'),
    ),
    '8.2.44': (
        _c('लूनः (lūnaḥ) — cut',
           {'gana': 'lvādi'},
           note='ल्वादिभ्यः — लूञ् छेदने इत्येतत्प्रभृति व्री वरणे इति '
                'यावत्'),
    ),
    '8.2.45': (
        _c('उद्विग्नः (udvignaḥ) — agitated',
           {'gana': 'odit'},
           note='ओदितश्च — ओकारेतो धातोरुत्तरस्य निष्ठातकारस्य नकारादेशः'),
    ),
    '8.2.46': (
        _c('क्षीणस्तपस्वी (kṣīṇastapasvī) — the ascetic is worn away',
           {'root': 'kṣi', 'gana': 'dīrgha'},
           note='क्षियो दीर्घात् — क्षियः, निष्ठायामण्यदर्थे, '
                'वाक्रोशदैन्ययोरिति दीर्घत्वम्'),
    ),
    '8.2.47': (
        _c('शीनं घृतम् (śīnaṃ ghṛtam) — the ghee has set',
           {'root': 'śyai', 'sense': 'a-sparśa'},
           note='श्योऽस्पर्शे — अस्पर्श इति किम्? शीतो वायुः'),
    ),
    '8.2.48': (
        _c("समक्नौ शकुनेः पादौ (samaknau) — the bird has drawn its feet up",
           {'root': 'añc', 'sense': 'an-apādāna'},
           note='अञ्चोऽनपादाने — व्यक्तमित्येतदञ्जे रूपम्'),
    ),
    '8.2.49': (
        _c('आद्यूनः (ādyūnaḥ) — a wretch, played out',
           {'root': 'div', 'sense': 'a-vijigīṣā'},
           note='दिवोऽविजिगीषायाम् — विजिगीषया हि तत्राक्षपातनादि क्रियते'),
    ),
    '8.2.50': (
        _c('निर्वाणः प्रदीपः (nirvāṇaḥ pradīpaḥ) — the lamp is out',
           {'root': 'nirvāṇa', 'sense': 'a-vāta'},
           note='निर्वाणोऽवाते — अवात इति किम्? निर्वातो वातः'),
    ),
    '8.2.51': (
        _c('शुष्कः (śuṣkaḥ) — dried up',
           {'root': 'śuṣ'},
           note='शुषः कः — शुषेर्धातोरुत्तरस्य निष्ठातकारस्य ककारादेशः'),
    ),
    '8.2.52': (
        _c('पक्वः (pakvaḥ) — cooked, or ripe',
           {'root': 'pac'},
           note='पचो वः — पचेर्धातोरुत्तरस्य निष्ठातकारस्य वकारादेशः'),
    ),
    '8.2.53': (
        _c('क्षामः (kṣāmaḥ) — wasted away',
           {'root': 'kṣai'},
           note='क्षायो मः — क्षैधातोरुत्तरस्य निष्ठातकारस्य मकारादेशः'),
    ),
    '8.2.54': (
        _c('प्रस्तीमः (prastīmaḥ) — beside प्रस्तीतः',
           {'root': 'styai', 'upasarga': 'pra'},
           note='प्रस्त्योऽन्यतरस्याम् — संयोगादेरातो धातोर्यण्वत इत्यस्य '
                'पूर्वत्रासिद्धत्वात्'),
    ),
    '8.2.55': (
        _c('फुल्लः (phullaḥ) — in full bloom, with no preverb',
           {'root': 'phulla', 'upasarga': 'anupasarga'},
           note='अनुपसर्गात् फुल्लक्षीबकृशोल्लाघाः — उत्वमिडभावश्च सिद्ध एव'),
    ),
    '8.2.56': (
        _c('नुन्नः (nunnaḥ) — pushed, beside नुत्तः',
           {'root': 'nud'},
           note='नुदविदोन्दत्राघ्राह्रीभ्योऽन्यतरस्याम्'),
    ),
    '8.2.57': (
        _c('मत्तः (mattaḥ) — drunk, and the त् stands',
           {'root': 'mad'},
           note='न ध्याख्यापॄमूर्छिमदाम् — रदाभ्यां, संयोगादेः, '
                'अन्यतरस्यामिति प्राप्ते प्रतिषेधः'),
    ),
    '8.2.58': (
        _c('वित्तमस्य बहु (vittam asya bahu) — his wealth is great',
           {'root': 'vitta', 'sense': 'bhoga'},
           note='वित्तो भोगप्रत्यययोः — धनं हि भुज्यत इति भोगोऽभिधीयते'),
    ),
    '8.2.59': (
        _c('भित्तं तिष्ठति (bhittaṃ tiṣṭhati) — a chip lies there',
           {'root': 'bhitta', 'sense': 'śakala'},
           note='भित्तं शकलम् — भिदिक्रिया शब्दव्युत्पत्तेरेव निमित्तम्'),
    ),
    '8.2.60': (
        _c('अधमर्णः (adhamarṇaḥ) — a debtor',
           {'root': 'ṛṇa', 'sense': 'ādhamarṇya'},
           note='ऋणमाधमर्ण्ये — एतस्मादेव निपातनात् सप्तम्यन्तेनोत्तरपदेन '
                'समासः'),
    ),
    '8.2.61': (
        _c('निषत्तः (niṣattaḥ) — seated, in the Veda',
           {'root': 'niṣatta', 'chandasi': True},
           note='नसत्तनिषत्तानुत्तप्रतूर्तसूर्तगूर्तानि छन्दसि — नत्वाभावो '
                'निपात्यते'),
    ),
    '8.2.62': (
        _c('घृतस्पृक् (ghṛtaspṛk) — touching the ghee',
           {'gana': 'kvin-pratyaya'},
           note='क्विन्प्रत्ययस्य कुः — सर्वत्र पदान्ते कुत्वमिष्यते'),
    ),
    '8.2.63': (
        _c('जीवनट् (jīvanaṭ) — beside जीवनक्',
           {'word': 'naś'},
           note='नशेर्वा — षत्वे प्राप्ते कुत्वविकल्पः'),
    ),
    '8.2.64': (
        _c('प्रशान् (praśān) — calmed',
           {'gana': 'ma-anta-dhātu'},
           note='मो नो धातोः — नत्वस्यासिद्धत्वान्नलोपो न भवति'),
    ),
    '8.2.65': (
        _c('अगन्म तमसस्पारम् (aganma) — we have crossed the dark',
           {'gana': 'ma-anta-dhātu', 'before': 'ma'},
           note='म्वोश्च — गमेर्लङि बहुलं छन्दसीति शपो लुक्'),
    ),
    '8.2.67': (
        _c('अवयाः (avayāḥ) — one who sacrifices away',
           {'word': 'avayāḥ'},
           note='अवयाःश्वेतवाःपुरोडाश्च — श्वेतवहादीनामिति निपातनम्'),
    ),
    '8.2.68': (
        _c('अहोभ्याम् (ahobhyām) — with two days',
           {'word': 'ahan'},
           note='अहन् — नलोपमकृत्वा निर्देशो ज्ञापकः'),
    ),
    '8.2.69': (
        _c('अहर्भुङ्क्ते (aharbhuṅkte) — he eats by day',
           {'word': 'ahan', 'before': 'a-sup'},
           note='रोऽसुपि — असुपीति किम्? अहोभ्याम्'),
    ),
    '8.2.70': (
        _c('ऊधर् (ūdhar) — an udder, beside ऊधः',
           {'word': 'ūdhas', 'chandasi': True},
           note='अम्नरूधरवरित्युभयथा छन्दसि — रुर्वा रेफो वा'),
    ),
    '8.2.71': (
        _c('भुवर् (bhuvar) — the mid-air, as an utterance',
           {'word': 'bhuvas', 'gana': 'mahāvyāhṛti', 'chandasi': True},
           note='भुवश्च महाव्याहृतेः — महाव्याहृतेरिति किम्? भुवो विश्वेषु '
                'सवनेषु'),
    ),
    '8.2.72': (
        _c('अनडुद् (anaḍud) — an ox, ending in द्',
           {'word': 'anaḍuh'},
           note='वसुस्रंसुध्वंस्वनडुहां दः — व्यभिचारात् वसुरेव विशेष्यते'),
    ),
    '8.2.73': (
        _c('अचकाद् भवान् (acakād bhavān) — you shone',
           {'gana': 'sa-anta-a-asti', 'before': 'tip'},
           note='तिप्यनस्तेः — अनस्तेरिति किम्? आप एवेदं सलिलं सर्वमाः'),
    ),
    '8.2.74': (
        _c('अचकास्त्वम् (acakās tvam) — beside अचकात्त्वम्',
           {'gana': 'sa-anta-dhātu', 'before': 'sip'},
           note='सिपि धातो रुर्वा — धातुग्रहणं चोत्तरार्थं रुग्रहणं च'),
    ),
    '8.2.75': (
        _c('अभिनस्त्वम् (abhinas tvam) — beside अभिनत्त्वम्',
           {'gana': 'da-anta-dhātu', 'before': 'sip'},
           note='दश्च — दकारान्तस्य धातोः पदस्य सिपि परतो रुर्भवति'),
    ),
    '8.2.76': (
        _c('गीः (gīḥ) — speech, with its vowel lengthened',
           {'gana': 'ra-va-anta-dhātu'},
           note='र्वोरुपधाया दीर्घ इकः — वकारग्रहणमुत्तरार्थम्'),
    ),
    '8.2.77': (
        _c('दीव्यति (dīvyati) — he plays',
           {'gana': 'ra-va-anta-dhātu', 'before': 'hal'},
           note='हलि च — धातोरित्येव, दिवमिच्छति दिव्यति'),
    ),
    '8.2.78': (
        _c('मूर्छिता (mūrchitā) — one who faints',
           {'gana': 'ra-va-upadha-hal-para', 'before': 'hal'},
           note='उपधायां च — हलीत्येव, चिरिणोति, जिरिणोति'),
    ),
    '8.2.79': (
        _c('कुर्यात् (kuryāt) — let him do it, with no lengthening',
           {'word': 'kur'},
           note='न भकुर्छुराम् — रेफवकाराभ्यां भविशेषणं किम्? प्रतिदीव्ना'),
    ),
    '8.2.80': (
        _c('अमुम् (amum) — that one, in the accusative',
           {'word': 'adas', 'gana': 'a-sa-anta'},
           note='अदसोऽसेर्दादु दो मः — भाव्यमानेनाप्युकारेण सवर्णानां '
                'ग्रहणम्'),
    ),
    '8.2.81': (
        _c('अमी (amī) — those ones',
           {'word': 'adas', 'gana': 'bahuvacana'},
           note='एत ईद्बहुवचने — बहुवचन इत्यर्थनिर्देशोऽयम्'),
    ),
    '8.2.82': (
        _c('आयुष्मानेधि देवदत्त३ (devadatta3) — the heading, at 8.2.83',
           {'sense': 'pratyabhivāda'},
           note='वाक्यस्य टेः प्लुत उदात्तः — '
                'एतत्त्रयमप्यधिकृतमापादपरिसमाप्तेः'),
    ),
    '8.2.83': (
        _c('आयुष्मानेधि देवदत्त३ (āyuṣmānedhi) — long life to you',
           {'sense': 'pratyabhivāda'},
           note='प्रत्यभिवादेऽशूद्रे — अशूद्र इति किम्? अभिवादये '
                'तुषजातीयोऽहं भोः'),
    ),
    '8.2.84': (
        _c('आगच्छ भो माणवक देवदत्त३ (devadatta3) — called from afar',
           {'sense': 'dūrād-dhūta'},
           note='दूराद्धूते च — दूरं हूतापेक्षं यत्रोच्चैः शब्दः प्रयुज्यते'),
    ),
    '8.2.85': (
        _c('है३ देवदत्त (hai3 devadatta) — the particle is lengthened',
           {'word': 'hai', 'sense': 'dūrād-dhūta', 'position': 'anantya'},
           note='हैहेप्रयोगे हैहयोः — पुनर्हैहयोर्ग्रहणमनन्त्ययोरपि यथा '
                'स्यात्'),
    ),
    '8.2.86': (
        _c('अग्नि३भूते (agni3bhūte) — one heavy vowel at a time',
           {'gana': 'guru-an-ṛt', 'position': 'anantya', 'view': 'prācām'},
           note='गुरोरनृतोऽनन्त्यस्याप्येकैकस्य प्राचाम् — तस्यैवायं '
                'स्थानिविशेष उच्यते'),
    ),
    '8.2.87': (
        _c('ओ३म् अग्निमीळे (o3m agnim īḷe) — at the opening',
           {'word': 'om', 'sense': 'abhyādāna'},
           note='ओमभ्यादाने — अभ्यादान इति किम्? '
                'ओमित्येतदक्षरमुद्गीथमुपासीत'),
    ),
    '8.2.88': (
        _c('ये३ यजामहे (ye3 yajāmahe) — in the rite itself',
           {'word': 'ye', 'sense': 'yajña-karman'},
           note='ये यज्ञकर्मणि — ये यजामह इत्यत्रैवायं प्लुत इष्यते'),
    ),
    '8.2.89': (
        _c('जिन्वो३म् (jinvo3m) — the प्रणव for the last syllable',
           {'sense': 'yajña-karman', 'position': 'ṭi'},
           note='प्रणवष्टेः — त्रिमात्रमोकारमोङ्कारं वा विदधति'),
    ),
    '8.2.90': (
        _c('स्तोमैर्विधेमाग्नये३ (agnaye3) — the last of the formula',
           {'gana': 'yājyā', 'sense': 'yajña-karman', 'position': 'anta'},
           note='याज्याऽन्तः — अन्तग्रहणं किम्? याज्या न'),
    ),
    '8.2.91': (
        _c('अग्नयेऽनुब्रू३हि (anubrū3hi) — recite for Agni',
           {'word': 'brūhi', 'sense': 'yajña-karman', 'position': 'ādi'},
           note='ब्रूहिप्रेष्यश्रौषड्वौषडावहानामादेः'),
    ),
    '8.2.92': (
        _c('आ३श्रा३वय (ā3śrā3vaya) — two lengthenings in one word',
           {'sense': 'agnīt-preṣaṇa', 'position': 'ādi-para'},
           note='अग्नीत्प्रेषणे परस्य च — अत्रैवायं प्लुत इष्यते'),
    ),
    '8.2.93': (
        _c('अकार्षं हि३ (akārṣaṃ hi3) — I did make it',
           {'word': 'hi', 'sense': 'pṛṣṭa-prativacana'},
           note='विभाषा पृष्टप्रतिवचने हेः — हेरिति किम्? करोमि ननु'),
    ),
    '8.2.94': (
        _c('अनित्यः शब्द इति ते३ (te3) — put back to the loser',
           {'sense': 'nigṛhya-anuyoga'},
           note='निगृह्यानुयोगे च — स्वमतात् प्रच्यावनं निग्रहः'),
    ),
    '8.2.95': (
        _c('चौरचौ३र (cauracau3ra) — thief, thief, said in threat',
           {'gana': 'āmreḍita', 'sense': 'bhartsana'},
           note='आम्रेडितं भर्त्सने — भर्त्सने पर्यायेणेति वक्तव्यम्'),
    ),
    '8.2.96': (
        _c('अङ्ग कू३ज (aṅga kū3ja) — go on and coo, then',
           {'word': 'aṅga', 'gana': 'tiṅ', 'sense': 'bhartsana', 'position': 'ākāṅkṣa'},
           note='अङ्गयुक्तं तिङ् आकाङ्क्षम् — आकाङ्क्षमिति किम्? अङ्ग पच'),
    ),
    '8.2.97': (
        _c('होतव्यं दीक्षितस्य गृहा३इ (gṛhā3i) — one of two things weighed',
           {'sense': 'vicāryamāṇa'},
           note='विचार्यमाणानाम् — प्रमाणेन वस्तुपरीक्षणं विचारः'),
    ),
    '8.2.98': (
        _c('अहिर्नु३ रज्जुर्नु (ahir nu3) — a snake, or a rope',
           {'sense': 'vicāryamāṇa', 'position': 'pūrva'},
           note='पूर्वं तु भाषायाम् — प्रयोगापेक्षं पूर्वत्वम्'),
    ),
    '8.2.99': (
        _c('किमात्थ३ (kim āttha3) — what is it you say',
           {'sense': 'pratiśravaṇa'},
           note='प्रतिश्रवणे च — तत्राविशेषात् सर्वस्य ग्रहणम्'),
    ),
    '8.2.100': (
        _c("अग्निभूता३इ (agnibhūtā3i) — at a question's close",
           {'sense': 'praśna-anta'},
           note='अनुदात्तं प्रश्नान्ताभिपूजितयोः'),
    ),
    '8.2.101': (
        _c('अग्निचिद् भाया३त् (agnicid bhāyā3t) — let him blaze',
           {'word': 'cit', 'sense': 'upamā'},
           note='चिदिति चोपमाऽर्थे प्रयुज्यमाने — प्लुतोऽप्यत्र विधीयते, न '
                'गुणमात्रम्'),
    ),
    '8.2.102': (
        _c('उपरि स्विदासी३त् (upari svid āsī3t) — or was it above',
           {'word': 'upari-svid-āsīt'},
           note='उपरिस्विदासीदिति च — अधःस्विदासीदित्यत्र विचार्यमाणानाम् '
                'इत्युदात्तः'),
    ),
    '8.2.103': (
        _c('माणव३क माणवक (māṇava3ka) — said in envy',
           {'gana': 'āmreḍita-pūrva', 'sense': 'kopa'},
           note='स्वरितमाम्रेडितेऽसूयासम्मतिकोपकुत्सनेषु'),
    ),
    '8.2.104': (
        _c('स्वयं ह रथेन याति३ (rathena yāti3) — he rides, himself',
           {'gana': 'tiṅ', 'sense': 'kṣiyā', 'position': 'ākāṅkṣa'},
           note='क्षियाऽऽशीःप्रैषेषु तिङ् आकाङ्क्षम् — शब्देन व्यापारणं '
                'प्रैषः'),
    ),
    '8.2.105': (
        _c('अगम३ः पूर्वा३न् ग्रामा३न् (grāmā3n) — did you go, then',
           {'sense': 'praśna', 'position': 'anantya'},
           note='अनन्त्यस्यापि प्रश्नाख्यानयोः — सर्वेषामेव पदानामेष '
                'स्वरितः प्लुतः'),
    ),
    '8.2.106': (
        _c('ऐ३तिकायन (ai3tikāyana) — the इ inside the ऐ is lengthened',
           {'gana': 'aic'},
           note='प्लुतावैच इदुतौ — तदवयवभूतावि दुतौ प्लुतौ'),
    ),
    '8.2.107': (
        _c('अग्ना३इ (agnā3i) — the ए splits into आ and इ',
           {'gana': 'ec-a-pragṛhya'},
           note='एचोऽप्रगृह्यस्यादूराद्धूते पूर्वस्यार्धस्यादुत्तरस्येदुतौ'),
    ),
    '8.2.108': (
        _c('अग्ना३याशा (agnā3yāśā) — the इ becomes य् before a vowel',
           {'gana': 'id-ut', 'position': 'ac-para'},
           note='तयोर्य्वावचि संहितायाम् — '
                'संहितायामित्येतच्चाधिकृतमाध्यायपरिसमाप्तेः'),
    ),
    '8.3.1': (
        _c('इन्द्र मरुत्व इह पाहि (marutva) — a vocative in the Veda',
           {'gana': 'matup-vasu-anta', 'before': 'sambuddhi', 'chandasi': True},
           note='मतुवसो रु सम्बुद्धौ छन्दसि — संहितायामिति वर्तते'),
    ),
    '8.3.2': (
        _c('सँस्स्कर्ता (sam̐sskartā) — the heading, at 8.3.5',
           {'word': 'sam', 'before': 'suṭ'},
           note='अत्रानुनासिकः पूर्वस्य तु वा — इत उत्तरं यस्य स्थाने '
                'रुर्विधीयते'),
    ),
    '8.3.3': (
        _c('महाँ असि (mahām̐ asi) — you are great',
           {'gana': 'ā-anta-ru-pūrva', 'before': 'aṭ'},
           note='आतोऽटि नित्यम् — नित्यार्थं वचनम्'),
    ),
    '8.3.4': (
        _c('संस्स्कर्ता (saṃsskartā) — with an anusvāra instead',
           {'gana': 'a-anunāsika-ru-pūrva'},
           note='अनुनासिकात् परोऽनुस्वारः — अन्यशब्दोऽत्राध्याहर्तव्यः'),
    ),
    '8.3.5': (
        _c('सँस्स्कर्ता (sam̐sskartā) — one who puts in order',
           {'word': 'sam', 'before': 'suṭ'},
           note='समः सुटि — रोर्विसर्जनीये कृते वा शरीति'),
    ),
    '8.3.6': (
        _c('पुंस्कामा (puṃskāmā) — a woman wanting a man',
           {'word': 'pum', 'before': 'khay-am-para'},
           note='पुमः खय्यम्परे — कुप्वोः क पौ चेति प्राप्नोति'),
    ),
    '8.3.7': (
        _c('भवांस्तरति (bhavāṃstarati) — you cross over',
           {'gana': 'na-anta', 'before': 'chav-am-para'},
           note='नश्छव्यप्रशान् — अम्पर इति वर्तते'),
    ),
    '8.3.8': (
        _c('तस्मिन्त्वा दधाति (tasmin tvā) — in a ṛc, either way',
           {'gana': 'na-anta', 'before': 'chav-am-para', 'chandasi': True},
           note='उभयथर्क्षु — पूर्वेण नित्ये प्राप्ते विकल्पः क्रियते'),
    ),
    '8.3.9': (
        _c('देवाँ अच्छा दीद्यत् (devām̐ acchā) — within one quarter',
           {'gana': 'dīrgha-para-na-anta', 'before': 'aṭ-samāna-pāda', 'chandasi': True},
           note='दीर्घादटि समानपादे — ऋक्पाद इह गृह्यते'),
    ),
    '8.3.10': (
        _c('नॄँः पाहि (nṝm̐ḥ pāhi) — protect the men',
           {'word': 'nṝn', 'before': 'pa', 'chandasi': True},
           note='नॄन् पे — अकार उच्चारणार्थः'),
    ),
    '8.3.11': (
        _c('स्वतवाँः पायुरग्ने (svatavām̐ḥ pāyuḥ) — one line of the Ṛgveda',
           {'word': 'svatavān', 'before': 'pāyu', 'chandasi': True},
           note='स्वतवान् पायौ — स्वतवाँः पायुरग्ने'),
    ),
    '8.3.12': (
        _c('कांस्कान् भोजयति (kāṃskān bhojayati) — whom does he feed',
           {'word': 'kān', 'before': 'āmreḍita'},
           note='कानाम्रेडिते — अस्य कस्कादिषु पाठो द्रष्टव्यः'),
    ),
    '8.3.13': (
        _c('लीढम् (līḍham) — licked',
           {'gana': 'ḍha', 'before': 'ḍha'},
           note='ढो ढे लोपः — अपदान्तस्य ढकारस्यायं लोपो विज्ञायते'),
    ),
    '8.3.14': (
        _c('अग्नी रथः (agnī rathaḥ) — the fire, the chariot',
           {'gana': 'repha', 'before': 'repha'},
           note='रो रि — तेनापदान्तस्यापि रेफस्य लोपो भवति'),
    ),
    '8.3.16': (
        _c('पयःसु (payaḥsu) — in the waters',
           {'gana': 'ru', 'before': 'sup'},
           note='रोः सुपि — सिद्धे सत्यारम्भो नियमार्थः'),
    ),
    '8.3.17': (
        _c('ब्राह्मणा ददति (brāhmaṇā dadati) — the brahmins give',
           {'gana': 'bho-bhago-agho-a-pūrva-ru', 'before': 'aś'},
           note='भोभगोअघोअपूर्वस्य योऽशि'),
    ),
    '8.3.18': (
        _c("भोयत्र (bhoyatra) — in Śākaṭāyana's view",
           {'gana': 'ya-va-pada-anta', 'before': 'aś', 'view': 'śākaṭāyana'},
           note='व्योर्लघुप्रयत्नतरः शाकटायनस्य'),
    ),
    '8.3.19': (
        _c("क आस्ते (ka āste) — in Śākalya's view",
           {'gana': 'ya-va-pada-anta', 'before': 'aś', 'view': 'śākalya'},
           note='लोपः शाकल्यस्य'),
    ),
    '8.3.20': (
        _c("भगो इदम् (bhago idam) — compulsorily, in Gārgya's honour",
           {'gana': 'o-para-ya', 'before': 'aś', 'view': 'gārgya'},
           note='ओतो गार्ग्यस्य — गार्ग्यग्रहणं पूजार्थम्'),
    ),
    '8.3.21': (
        _c('स उ एकाग्निः (sa u ekāgniḥ) — उ standing as a word',
           {'gana': 'a-pūrva-ya-va', 'before': 'uñ-pada'},
           note='उञि च पदे — पद इति किम्? तन्त्र उतम्'),
    ),
    '8.3.22': (
        _c('वृक्षा हसन्ति (vṛkṣā hasanti) — every teacher agrees',
           {'gana': 'bho-bhago-agho-a-pūrva-ya', 'before': 'hal'},
           note='हलि सर्वेषाम् — शाकटायनस्यापि लोपो यथा स्यात्'),
    ),
    '8.3.23': (
        _c('कुण्डं हसति (kuṇḍaṃ hasati) — the pot, laughing',
           {'gana': 'ma-anta', 'before': 'hal'},
           note='मोऽनुस्वारः — हलीत्येव, त्वमत्र। पदान्तस्येत्येव, गम्यते'),
    ),
    '8.3.24': (
        _c('पयांसि (payāṃsi) — waters, with the नुम् inside',
           {'gana': 'na-ma-a-pada-anta', 'before': 'jhal'},
           note='नश्चापदान्तस्य झलि — अपदान्तस्येति किम्? राजन् भुङ्क्ष्व'),
    ),
    '8.3.25': (
        _c('सम्राट् (samrāṭ) — a sovereign',
           {'word': 'sam', 'before': 'rāj-kvip'},
           note='मो राजि समः क्वौ — मकारस्य मकारवचनमनुस्वारनिवृत्त्यर्थम्'),
    ),
    '8.3.26': (
        _c('किम् ह्मलयति (kim hmalayati) — the म् stays before ह्म',
           {'gana': 'ma-anta', 'before': 'ha-ma-para'},
           note='हे मपरे वा — यवलपरे यवला वा'),
    ),
    '8.3.27': (
        _c('किन् ह्नुते (kin hnute) — what does he conceal',
           {'gana': 'ma-anta', 'before': 'ha-na-para'},
           note='नपरे नः — कथन् ह्नुते, कथं ह्नुते'),
    ),
    '8.3.28': (
        _c('प्राङ्क् शेते (prāṅk śete) — he lies facing east',
           {'gana': 'ṅa-ṇa-anta', 'before': 'śar'},
           note='ङ्णोः कुक्टुक् शरि — पूर्वान्तकरणम्'),
    ),
    '8.3.29': (
        _c('श्वलिट्त्साये (śvaliṭtsāye) — with the augment between',
           {'gana': 'ḍa-anta-para-sa-ādi'},
           note='डः सि धुट् — परादिकरणं ष्टुत्वप्रतिषेधार्थम्'),
    ),
    '8.3.30': (
        _c('भवान्त्साये (bhavāntsāye) — and the न् survives',
           {'gana': 'na-anta-para-sa-ādi'},
           note='नश्च — धुटश्चर्त्वस्य चासिद्धत्वाद् रुत्वं न भवति'),
    ),
    '8.3.31': (
        _c('भवाञ्च्छेते (bhavāñchete) — you lie down',
           {'gana': 'na-anta', 'before': 'śa'},
           note='शि तुक् — पूर्वान्तकरणं छत्वार्थम्'),
    ),
    '8.3.32': (
        _c('प्रत्यङ्ङास्ते (pratyaṅṅāste) — he sits facing west',
           {'gana': 'hrasva-para-ṅam-anta', 'before': 'ac'},
           note='ङमो ह्रस्वादचि ङमुण्नित्यम् — ङणनेभ्यो यथासंख्यम्'),
    ),
    '8.3.33': (
        _c('शम्वस्तु वेदिः (śamvastu vediḥ) — let the altar be well',
           {'word': 'uñ', 'gana': 'may-para', 'before': 'ac'},
           note='मय उञो वो वा — प्रगृह्यसंज्ञा'),
    ),
    '8.3.34': (
        _c('वृक्षस्तरति (vṛkṣastarati) — the tree crosses over',
           {'gana': 'visarjanīya', 'before': 'khar'},
           note='विसर्जनीयस्य सः — खरीत्यनुवर्तते'),
    ),
    '8.3.35': (
        _c("शशः क्षुरम् (śaśaḥ kṣuram) — the hare's razor",
           {'gana': 'visarjanīya', 'before': 'khar-śar-para'},
           note='शर्परे विसर्जनीयः'),
    ),
    '8.3.36': (
        _c('वृक्षः शेते (vṛkṣaḥ śete) — beside वृक्षश्शेते',
           {'gana': 'visarjanīya', 'before': 'śar'},
           note='वा शरि — खर्परे शरि वा लोपः'),
    ),
    '8.3.37': (
        _c('वृक्षः करोति (vṛkṣaḥ karoti) — or with a jihvāmūlīya',
           {'gana': 'visarjanīya', 'before': 'ku'},
           note='कुप्वोः क पौ च — चकाराद् विसर्जनीयश्च'),
    ),
    '8.3.38': (
        _c('पयस्पाशम् (payaspāśam) — wretched milk',
           {'gana': 'visarjanīya', 'before': 'ku-pu-a-pada-ādi'},
           note='सोऽपदादौ — पाशकल्पककाम्येषु'),
    ),
    '8.3.39': (
        _c('सर्पिष्पाशम् (sarpiṣpāśam) — wretched ghee',
           {'gana': 'iṇ-para-visarjanīya', 'before': 'ku-pu-a-pada-ādi'},
           note='इणः षः — अपदादाविति वर्तते'),
    ),
    '8.3.40': (
        _c('नमस्कर्ता (namaskartā) — one who does homage',
           {'word': 'namas', 'gana': 'gati', 'before': 'ku'},
           note='नमस्पुरसोर्गत्योः — गत्योरिति किम्? नमः कृत्वा'),
    ),
    '8.3.41': (
        _c('निष्कृतम् (niṣkṛtam) — set right',
           {'word': 'nis', 'gana': 'i-u-upadha-a-pratyaya', 'before': 'ku'},
           note='इदुदुपधस्य चाप्रत्ययस्य — निर्दुर्बहिराविश्चतुर्प्रादुस्'),
    ),
    '8.3.42': (
        _c('तिरस्कर्ता (tiraskartā) — beside तिरः कर्ता',
           {'word': 'tiras', 'gana': 'gati', 'before': 'ku'},
           note='तिरसोऽन्यतरस्याम् — गतेरित्येव'),
    ),
    '8.3.43': (
        _c('द्विष्करोति (dviṣkaroti) — he does it twice',
           {'word': 'dvis', 'before': 'ku', 'sense': "kṛtvo'rtha"},
           note='द्विस्त्रिश्चतुरिति कृत्वोऽर्थे — ष इति सम्बध्यते'),
    ),
    '8.3.44': (
        _c('सर्पिष्करोति (sarpiṣkaroti) — beside सर्पिः करोति',
           {'gana': 'is-us-anta', 'before': 'ku', 'sense': 'sāmarthya'},
           note='इसुसोः सामर्थ्ये — सामर्थ्य इति किम्? तिष्ठतु सर्पिः'),
    ),
    '8.3.45': (
        _c('सर्पिष्कुण्डिका (sarpiṣkuṇḍikā) — a ghee-pot',
           {'gana': 'is-us-anta', 'before': 'ku', 'sense': 'samāsa'},
           note='नित्यं समासेऽनुत्तरपदस्थस्य'),
    ),
    '8.3.46': (
        _c('अयस्कारः (ayaskāraḥ) — a smith',
           {'gana': 'a-anta-an-avyaya', 'before': 'kṛ', 'sense': 'samāsa'},
           note='अतः कृकमिकंसकुम्भपात्रकुशाकर्णीष्वनव्ययस्य'),
    ),
    '8.3.47': (
        _c('अधस्पदम् (adhaspadam) — underfoot',
           {'word': 'adhas', 'before': 'pada', 'sense': 'samāsa'},
           note='अधःशिरसी पदे — समास इत्येव, अधः पदम्'),
    ),
    '8.3.48': (
        _c("भ्रातुष्पुत्रः (bhrātuṣputraḥ) — a brother's son",
           {'gana': 'kaskādi', 'before': 'ku'},
           note='कस्कादिषु च — यथायोगमादेशो भवति'),
    ),
    '8.3.49': (
        _c('अयस्पात्रम् (ayaspātram) — an iron vessel, in the Veda',
           {'gana': 'visarjanīya', 'before': 'ku', 'chandasi': True},
           note='छन्दसि वाऽप्राम्रेडितयोः'),
    ),
    '8.3.50': (
        _c('उरु णस्कृधि (uru ṇaskṛdhi) — make wide room for us',
           {'gana': 'a-aditi-visarjanīya', 'before': 'kaḥ', 'chandasi': True},
           note='कःकरत्करतिकृधिकृतेष्वनदितेः'),
    ),
    '8.3.51': (
        _c('दिवस्परि प्रथमं जज्ञे (divas pari) — born first from heaven',
           {'case': 'pañcamī', 'before': 'pari', 'sense': 'adhi', 'chandasi': True},
           note='पञ्चम्याः परावध्यर्थे'),
    ),
    '8.3.52': (
        _c('दिवस्पातु (divas pātu) — may he guard from heaven',
           {'case': 'pañcamī', 'before': 'pātu', 'chandasi': True},
           note='पातौ च बहुलम् — न च भवति, परिषदः पातु'),
    ),
    '8.3.53': (
        _c('वाचस्पतिं विश्वकर्माणम् (vācaspatim) — the lord of speech',
           {'case': 'ṣaṣṭhī', 'before': 'pati', 'chandasi': True},
           note='षष्ठ्याः पतिपुत्रपृष्ठपारपदपयस्पोषेषु'),
    ),
    '8.3.54': (
        _c('इडायास्पतिः (iḍāyās patiḥ) — beside इडायाः पतिः',
           {'word': 'iḍā', 'case': 'ṣaṣṭhī', 'before': 'pati', 'chandasi': True},
           note='इडाया वा — पत्यादिषु परतश्छन्दसि विषये'),
    ),
    '8.3.55': (
        _c('अग्निषु (agniṣu) — the heading, at 8.3.59',
           {'gana': 'ādeśa-pratyaya-sa', 'after': 'iṇ-ku'},
           note='अपदान्तस्य मूर्धन्यः — पदाधिकारो निवृत्तः'),
    ),
    '8.3.56': (
        _c('जलाषाट् (jalāṣāṭ) — overcoming the waters',
           {'root': 'sah', 'gana': 'sāḍ'},
           note='सहेः साडः सः — सहेरिति किम्? साडिः'),
    ),
    '8.3.57': (
        _c('कर्तृषु (kartṛṣu) — the heading, at 8.3.59',
           {'gana': 'ādeśa-pratyaya-sa', 'after': 'iṇ-ku'},
           note='इण्कोः — इणः कवर्गाच्चेत्येवं तद् वेदितव्यम्'),
    ),
    '8.3.58': (
        _c('सर्पींषि (sarpīṃṣi) — the ष् across the नुम्',
           {'gana': 'num-visarjanīya-śar-vyavāya', 'after': 'iṇ-ku'},
           note='नुम्विसर्जनीयशर्व्यवायेऽपि — व्यवायशब्दः प्रत्येकम्'),
    ),
    '8.3.59': (
        _c('अग्निषु (agniṣu) — in the fires',
           {'gana': 'ādeśa-pratyaya-sa', 'after': 'iṇ-ku'},
           note='आदेशप्रत्यययोः — षष्ठी भेदेन सम्बध्यते'),
    ),
    '8.3.60': (
        _c('उषितः (uṣitaḥ) — having dwelt',
           {'root': 'vas', 'after': 'iṇ-ku'},
           note='शासिवसिघसीनां च'),
    ),
    '8.3.61': (
        _c('तुष्टूषति (tuṣṭūṣati) — he wants to praise',
           {'root': 'stu', 'after': 'abhyāsa-iṇ', 'before': 'ṣa-san'},
           note='स्तौतिण्योरेव षण्यभ्यासात् — सिद्धे सत्यारम्भो नियमार्थः'),
    ),
    '8.3.62': (
        _c('सिस्वेदयिषति (sisvedayiṣati) — the स् stays plain',
           {'root': 'svid', 'after': 'abhyāsa', 'before': 'ṣa-san'},
           note='सः स्विदिस्वदिसहीनां च — सकारस्य सकारवचनम्'),
    ),
    '8.3.63': (
        _c('न्यषीदत् (nyaṣīdat) — across the augment, at 8.3.66',
           {'root': 'sad', 'after': 'upasarga'},
           note='प्राक्सितादड्व्यवायेऽपि — अपिशब्दादनड्व्यवायेऽपि'),
    ),
    '8.3.64': (
        _c('अभितिष्ठति (abhitiṣṭhati) — across the reduplication',
           {'gana': 'sthādi', 'after': 'abhyāsa'},
           note='स्थादिष्वभ्यासेन चाभ्यासस्य'),
    ),
    '8.3.65': (
        _c('अभिषुणोति (abhiṣuṇoti) — he presses out',
           {'root': 'sunoti', 'after': 'upasarga'},
           note='उपसर्गात् सुनोतिसुवतिस्यतिस्तौतिस्तोभति…'),
    ),
    '8.3.66': (
        _c('निषीदति (niṣīdati) — he sits down',
           {'root': 'sad', 'after': 'upasarga'},
           note='सदिरप्रतेः — अप्रतेरिति किम्? प्रतिसीदति'),
    ),
    '8.3.67': (
        _c('अभिष्टभ्नाति (abhiṣṭabhnāti) — he props it up',
           {'root': 'stambh', 'after': 'upasarga'},
           note='स्तम्भेः — उपसर्गादिति वर्तते'),
    ),
    '8.3.68': (
        _c('अवष्टभ्यास्ते (avaṣṭabhyāste) — he sits leaning on it',
           {'root': 'stambh', 'after': 'ava', 'sense': 'ālambana'},
           note='अवाच्चालम्बनाविदूर्ययोः — आलम्बनमाश्रयणम्'),
    ),
    '8.3.69': (
        _c('विष्वणति (viṣvaṇati) — he eats',
           {'root': 'svan', 'after': 'vi-ava', 'sense': 'bhojana'},
           note='वेश्च स्वनो भोजने — अभ्यवहारक्रियाविशेषोऽभिधीयते'),
    ),
    '8.3.70': (
        _c('परिषेवते (pariṣevate) — he attends upon',
           {'root': 'sev', 'after': 'pari-ni-vi'},
           note='परिनिविभ्यः सेवसितसयसिवुसहसुट्स्तुस्वञ्जाम्'),
    ),
    '8.3.71': (
        _c('पर्यषीव्यत् (paryaṣīvyat) — beside पर्यसीव्यत्',
           {'root': 'sivu', 'gana': 'aṭ-vyavāya', 'after': 'pari-ni-vi'},
           note='सिवादीनां वाऽड्व्यवायेऽपि — तथा चैवोदाहृतम्'),
    ),
    '8.3.72': (
        _c('अभिष्यन्दते तैलम् (abhiṣyandate tailam) — the oil flows',
           {'root': 'syand', 'after': 'anu-vi-pari-abhi-ni', 'sense': 'aprāṇi'},
           note='अनुविपर्यभिनिभ्यः स्यन्दतेरप्राणिषु'),
    ),
    '8.3.73': (
        _c('विष्कन्ता (viṣkantā) — beside विस्कन्ता',
           {'root': 'skand', 'after': 'vi', 'before': 'a-niṣṭhā'},
           note='वेः स्कन्देरनिष्ठायाम् — अनिष्ठायामिति किम्?'),
    ),
    '8.3.74': (
        _c('परिष्कन्ता (pariṣkantā) — beside परिस्कन्ता',
           {'root': 'skand', 'after': 'pari'},
           note='परेश्च — पृथग्योगकरणसामर्थ्यात्'),
    ),
    '8.3.75': (
        _c('परिस्कन्दः (pariskandaḥ) — as the eastern Bharatas say it',
           {'root': 'pariskanda', 'sense': 'prācyabharata'},
           note='परिस्कन्दः प्राच्यभरतेषु — अन्यत्र परिष्कन्दः'),
    ),
    '8.3.76': (
        _c('निष्फुरति (niṣphurati) — beside निस्फुरति',
           {'root': 'sphur', 'after': 'nis-ni-vi'},
           note='स्फुरतिस्फुलत्योर्निर्निविभ्यः'),
    ),
    '8.3.77': (
        _c('विष्कभ्नाति (viṣkabhnāti) — he props apart',
           {'root': 'skabh', 'after': 'vi'},
           note='वेः स्कभ्नातेर्नित्यम्'),
    ),
    '8.3.78': (
        _c('च्योषीढ्वम् (cyoṣīḍhvam) — may you fall away',
           {'gana': 'iṇ-anta-aṅga', 'before': 'liṭ'},
           note='इणः षीध्वंलुङ्लिटां धोऽङ्गात्'),
    ),
    '8.3.79': (
        _c('लविषीढ्वम् (laviṣīḍhvam) — beside लविषीध्वम्',
           {'gana': 'iṭ-para', 'before': 'liṭ'},
           note='विभाषेटः'),
    ),
    '8.3.80': (
        _c('अङ्गुलिषङ्गः (aṅguliṣaṅgaḥ) — clinging to the finger',
           {'root': 'saṅga', 'after': 'aṅguli', 'sense': 'samāsa'},
           note='समासेऽङ्गुलेः सङ्गः — समास इति किम्?'),
    ),
    '8.3.81': (
        _c("भीरुष्ठानम् (bhīruṣṭhānam) — a coward's refuge",
           {'root': 'sthāna', 'after': 'bhīru', 'sense': 'samāsa'},
           note='भीरोः स्थानम् — समास इत्येव'),
    ),
    '8.3.82': (
        _c('अग्निष्टोमः (agniṣṭomaḥ) — the Agniṣṭoma rite',
           {'root': 'soma', 'after': 'agni', 'sense': 'samāsa'},
           note='अग्नेः स्तुत्स्तोमसोमाः — अग्नेर्दीर्घात् सोमस्येष्यते'),
    ),
    '8.3.83': (
        _c('ज्योतिष्टोमः (jyotiṣṭomaḥ) — the Jyotiṣṭoma rite',
           {'root': 'stoma', 'after': 'jyotis-āyus', 'sense': 'samāsa'},
           note='ज्योतिरायुषः स्तोमः — समास इत्येव'),
    ),
    '8.3.84': (
        _c("मातृष्वसा (mātṛṣvasā) — a mother's sister",
           {'root': 'svasṛ', 'after': 'mātṛ-pitṛ', 'sense': 'samāsa'},
           note='मातृपितृभ्यां स्वसा'),
    ),
    '8.3.85': (
        _c('मातुःष्वसा (mātuḥṣvasā) — beside मातुःस्वसा',
           {'root': 'svasṛ', 'after': 'mātuḥ-pituḥ', 'sense': 'samāsa'},
           note='मातुःपितुर्भ्यामन्यतरस्याम् — रेफान्तयोरेतद् रूपम्'),
    ),
    '8.3.86': (
        _c('अभिनिष्टानो वर्णः (abhiniṣṭāno varṇaḥ) — a sounded letter',
           {'root': 'stana', 'after': 'abhinis', 'sense': 'śabdasaṃjñā'},
           note='अभिनिसः स्तनः शब्दसंज्ञायाम्'),
    ),
    '8.3.87': (
        _c('अभिषन्ति (abhiṣanti) — they are present',
           {'root': 'asti', 'after': 'upasarga-prādus', 'before': 'yac-para'},
           note='उपसर्गप्रादुर्भ्यामस्तिर्यच्परः'),
    ),
    '8.3.88': (
        _c('सुषुप्तः (suṣuptaḥ) — deeply asleep',
           {'root': 'supi', 'after': 'su-vi-nis-dus'},
           note='सुविनिर्दुर्भ्यः सुपिसूतिसमाः — कृतसम्प्रसारणो गृह्यते'),
    ),
    '8.3.89': (
        _c('निष्णातः कटकरणे (niṣṇātaḥ) — expert at making mats',
           {'root': 'snā', 'after': 'ni-nadī', 'sense': 'kauśala'},
           note='निनदीभ्यां स्नातेः कौशले'),
    ),
    '8.3.90': (
        _c('प्रतिष्णातं सूत्रम् (pratiṣṇātaṃ sūtram) — clean thread',
           {'root': 'pratiṣṇāta', 'sense': 'sūtra'},
           note='सूत्रं प्रतिष्णातम् — शुद्धमित्यर्थः'),
    ),
    '8.3.91': (
        _c('कपिष्ठलः (kapiṣṭhalaḥ) — a family name',
           {'root': 'kapiṣṭhala', 'sense': 'gotra'},
           note='कपिष्ठलो गोत्रे — गोत्र इति किम्? कपिस्थलम्'),
    ),
    '8.3.92': (
        _c("प्रष्ठोऽश्वः (praṣṭho'śvaḥ) — the lead horse",
           {'root': 'praṣṭha', 'sense': 'agragāmin'},
           note='प्रष्ठोऽग्रगामिनि — अग्रगामिनीति किम्? प्रस्थो व्रीहीणाम्'),
    ),
    '8.3.93': (
        _c('विष्टरमासनम् (viṣṭaram āsanam) — a seat of grass',
           {'root': 'viṣṭara', 'sense': 'vṛkṣa'},
           note='वृक्षासनयोर्विष्टरः — विपूर्वस्य स्तृणातेः षत्वं निपात्यते'),
    ),
    '8.3.94': (
        _c('विष्टारः (viṣṭāraḥ) — the name of a metre',
           {'root': 'viṣṭāra', 'sense': 'chandonāman'},
           note='छन्दोनाम्नि च — छन्दोनाम्नि चेति विहितो घञ्'),
    ),
    '8.3.95': (
        _c('युधिष्ठिरः (yudhiṣṭhiraḥ) — steady in battle',
           {'root': 'sthira', 'after': 'gavi-yudhi'},
           note='गवियुधिभ्यां स्थिरः — सप्तम्या अलुग् भवति'),
    ),
    '8.3.96': (
        _c('विष्ठलम् (viṣṭhalam) — a place apart',
           {'root': 'sthala', 'after': 'vi-ku-śami-pari'},
           note='विकुशमिपरिभ्यः स्थलम्'),
    ),
    '8.3.97': (
        _c('अम्बष्ठः (ambaṣṭhaḥ) — one of eighteen first members',
           {'root': 'stha', 'after': 'ambādi'},
           note='अम्बाम्बगोभूमिसव्यापद्वित्रिकुशेकुशङ्क्वङ्गु…'),
    ),
    '8.3.98': (
        _c('सुषामा ब्राह्मणः (suṣāmā brāhmaṇaḥ) — a fine chanter',
           {'gana': 'suṣāmādi'},
           note='सुषामादिषु च — सुशब्दस्य कर्मप्रवचनीयसंज्ञकत्वात्'),
    ),
    '8.3.99': (
        _c("हरिषेणः (hariṣeṇaḥ) — a man's name",
           {'before': 'e', 'sense': 'saṃjñā', 'after': 'iṇ-ku-a-ga'},
           note='ऐति संज्ञायामगात् — एतीति किम्? हरिसक्थम्'),
    ),
    '8.3.100': (
        _c('रोहिणीषेणः (rohiṇīṣeṇaḥ) — beside रोहिणीसेनः',
           {'after': 'nakṣatra', 'before': 'e', 'sense': 'saṃjñā'},
           note='नक्षत्राद्वा — अगकारादित्येव, शतभिषक्सेनः'),
    ),
    '8.3.101': (
        _c('सर्पिष्टरम् (sarpiṣṭaram) — richer in ghee',
           {'after': 'hrasva', 'before': 'ta-ādi-taddhita'},
           note='ह्रस्वात् तादौ तद्धिते'),
    ),
    '8.3.102': (
        _c('निष्टपति सुवर्णम् (niṣṭapati suvarṇam) — he heats the gold',
           {'root': 'tap', 'after': 'nis', 'sense': 'an-āsevana'},
           note='निसस्तपतावनासेवने — आसेवनं पुनःपुनः करणम्'),
    ),
    '8.3.103': (
        _c('अग्निष्ट्वं नामासीत् (agniṣṭvam) — Agni was your name',
           {'before': 'tat', 'gana': 'antaḥ-pāda', 'chandasi': True},
           note='युष्मत्तत्ततक्षुःष्वन्तःपादम्'),
    ),
    '8.3.104': (
        _c("अर्चिर्भिष्ट्वम् (arcirbhiṣṭvam) — in some teachers' view",
           {'before': 'tat', 'sense': 'yajus', 'view': 'ekeṣām'},
           note='यजुष्येकेषाम्'),
    ),
    '8.3.105': (
        _c('त्रिभिष्टुतस्य (tribhiṣṭutasya) — beside त्रिभिस्तुतस्य',
           {'root': 'stuta', 'chandasi': True, 'view': 'ekeṣām'},
           note='स्तुतस्तोमयोश्छन्दसि — एकेषामिति वर्तते'),
    ),
    '8.3.106': (
        _c('द्विषन्धिः (dviṣandhiḥ) — beside द्विसन्धिः',
           {'after': 'pūrvapada', 'chandasi': True, 'view': 'ekeṣām'},
           note='पूर्वपदात् — छन्दसीति वर्तते, एकेषामिति च'),
    ),
    '8.3.107': (
        _c('अभी षु णः सखीनाम् (abhī ṣu ṇaḥ) — the particle सु',
           {'root': 'suñ', 'after': 'pūrvapada', 'chandasi': True},
           note='सुञः — पूर्वपदस्थाद् निमित्तादुत्तरस्य'),
    ),
    '8.3.108': (
        _c('गोषाः (goṣāḥ) — winning cattle',
           {'root': 'san', 'gana': 'a-an-anta', 'chandasi': True},
           note='सनोतेरनः — अन इति किम्? गोसनिं वाचम्'),
    ),
    '8.3.109': (
        _c('पृतनाषाहम् (pṛtanāṣāham) — overcoming armies',
           {'root': 'sah', 'after': 'pṛtanā-ṛta', 'chandasi': True},
           note='सहेः पृतनर्ताभ्यां च — केचिद् योगविभागं कुर्वन्ति'),
    ),
    '8.3.110': (
        _c('विस्रब्धः कथयति (visrabdhaḥ kathayati) — he speaks freely',
           {'root': 'sṛj'},
           note='न रपरसृपिसृजिस्पृशिस्पृहिसवनादीनाम्'),
    ),
    '8.3.111': (
        _c('अग्निसात् (agnisāt) — reduced to fire',
           {'root': 'sāt'},
           note='सात्पदाद्योः — प्रत्ययसकारत्वात् प्राप्तिः'),
    ),
    '8.3.112': (
        _c('अभिसेसिच्यते (abhisesicyate) — he keeps sprinkling',
           {'root': 'sic', 'before': 'yaṅ'},
           note='सिचो यङि — पदादिलक्षणमेव प्रतिषेधं बाधते'),
    ),
    '8.3.113': (
        _c('अभिसेधयति गाः (abhisedhayati gāḥ) — he drives the cows',
           {'root': 'sedh', 'sense': 'gati'},
           note='सेधतेर्गतौ — गताविति किम्? प्रतिषेधयति'),
    ),
    '8.3.114': (
        _c('निस्तब्धः (nistabdhaḥ) — motionless, with no cerebral',
           {'root': 'nistabdha'},
           note='प्रतिस्तब्धनिस्तब्धौ च — स्तन्भेरिति प्राप्तं प्रतिषिध्यते'),
    ),
    '8.3.115': (
        _c('परिसोढा (parisoḍhā) — one who endures',
           {'root': 'sah', 'gana': 'soḍha'},
           note='सोढः — सोड्भूतग्रहणं किम्? परिषहते'),
    ),
    '8.3.116': (
        _c('पर्यसीषिवत् (paryasīṣivat) — no cerebral before चङ्',
           {'root': 'sivu', 'before': 'caṅ'},
           note='स्तम्भुसिवुसहां चङि'),
    ),
    '8.3.117': (
        _c('अभिसोष्यति (abhisoṣyati) — he will press out',
           {'root': 'sunoti', 'before': 'sya'},
           note='सुनोतेः स्यसनोः — सनि किमुदाहरणम्? नैतदस्ति प्रयोजनम्'),
    ),
    '8.3.118': (
        _c('अभिषसाद (abhiṣasāda) — the second स् stays plain',
           {'root': 'sad', 'before': 'liṭ', 'gana': 'para'},
           note='सदिष्वञ्जोः परस्य लिटि'),
    ),
    '8.3.119': (
        _c('न्यसीदत् पिता नः (nyasīdat pitā naḥ) — beside न्यषीदत्',
           {'after': 'ni-vi-abhi', 'gana': 'aṭ-vyavāya', 'chandasi': True},
           note='निव्यभिभ्योऽड्व्यवाये वा छन्दसि'),
    ),
    '8.4.1': (
        _c('आस्तीर्णम् (āstīrṇam) — spread out',
           {'gana': 'ra-ṣa-para-na', 'after': 'samāna-pada'},
           note='रषाभ्यां नो णः समानपदे — षग्रहणमुत्तरार्थम्'),
    ),
    '8.4.2': (
        _c('करणम् (karaṇam) — a doing, the ण् two sounds from its र्',
           {'gana': 'ra-ṣa-para-na', 'after': 'vyavāya'},
           note='अट्कुप्वाङ्नुम्व्यवायेऽपि'),
    ),
    '8.4.3': (
        _c('शूर्पणखा (śūrpaṇakhā) — she of the winnowing-basket nails',
           {'after': 'pūrvapada', 'sense': 'saṃjñā'},
           note='पूर्वपदात् संज्ञायामगः — अग इति किम्? ऋगयनम्'),
    ),
    '8.4.4': (
        _c('पुरगावणम् (puragāvaṇam) — a named wood',
           {'root': 'vana', 'after': 'puragādi', 'sense': 'saṃjñā'},
           note='वनं पुरगामिश्रकासिध्रकाशारिकाकोटराऽग्रेभ्यः'),
    ),
    '8.4.5': (
        _c('शरवणम् (śaravaṇam) — a reed-thicket',
           {'root': 'vana', 'after': 'pranirādi'},
           note=' '
                'प्रनिरन्तःशरेक्षुप्लक्षाम्रकार्ष्यखदिरपियूक्षाभ्योऽसंज्ञायामपि'),
    ),
    '8.4.6': (
        _c('दूर्वावणम् (dūrvāvaṇam) — beside दूर्वावनम्',
           {'root': 'vana', 'after': 'oṣadhi-vanaspati'},
           note='विभाषौषधिवनस्पतिभ्यः'),
    ),
    '8.4.7': (
        _c('पूर्वाह्णः (pūrvāhṇaḥ) — the earlier half of the day',
           {'root': 'ahna', 'after': 'a-anta-pūrvapada'},
           note='अह्नोऽदन्तात् — अदन्तादिति किम्? निरह्नः'),
    ),
    '8.4.8': (
        _c('इक्षुवाहणम् (ikṣuvāhaṇam) — a cane-cart',
           {'root': 'vāhana', 'after': 'āhita'},
           note='वाहनमाहितात् — आहितादिति किम्? दाक्षिवाहनम्'),
    ),
    '8.4.9': (
        _c('क्षीरपाणा उशीनराः (kṣīrapāṇāḥ) — the milk-drinking Uśīnaras',
           {'root': 'pāna', 'after': 'pūrvapada', 'sense': 'deśa'},
           note='पानं देशे — कृत्यल्युटो बहुलमिति कर्मणि ल्युट्'),
    ),
    '8.4.10': (
        _c('क्षीरपाणं वर्तते (kṣīrapāṇam) — beside क्षीरपानम्',
           {'root': 'pāna', 'after': 'pūrvapada', 'sense': 'bhāva'},
           note='वा भावकरणयोः'),
    ),
    '8.4.11': (
        _c('माषवापिणौ (māṣavāpiṇau) — beside माषवापिनौ',
           {'gana': 'prātipadika-anta-num-vibhakti', 'after': 'pūrvapada'},
           note='प्रातिपदिकान्तनुम्विभक्तिषु च — वेति वर्तते'),
    ),
    '8.4.12': (
        _c('वृत्रहणौ (vṛtrahaṇau) — the two slayers of Vṛtra',
           {'gana': 'prātipadika-anta-num-vibhakti', 'after': 'ekāc-uttarapada'},
           note='एकाजुत्तरपदे णः'),
    ),
    '8.4.13': (
        _c('वस्त्रयुगिणौ (vastrayugiṇau) — the two in paired garments',
           {'gana': 'prātipadika-anta-num-vibhakti', 'after': 'kumat-uttarapada'},
           note='कुमति च'),
    ),
    '8.4.14': (
        _c('प्रणमति (praṇamati) — he bows down',
           {'gana': 'ṇopadeśa', 'after': 'upasarga'},
           note='उपसर्गादसमासेऽपि णोपदेशस्य — ण उपदेशे यस्यासौ णोपदेशः'),
    ),
    '8.4.15': (
        _c('प्रहिणोति (prahiṇoti) — he sends forth',
           {'root': 'hinu', 'after': 'upasarga'},
           note='हिनुमीना — अजादेशस्य स्थानिवत्त्वात्'),
    ),
    '8.4.16': (
        _c('प्रवपाणि (pravapāṇi) — let me scatter',
           {'root': 'āni', 'before': 'loṭ', 'after': 'upasarga'},
           note='आनि लोट् — लोडिति किम्? प्रवपानि मांसानि'),
    ),
    '8.4.17': (
        _c('प्रणिगदति (praṇigadati) — he recites',
           {'root': 'ni', 'gana': 'gadādi', 'after': 'upasarga'},
           note='नेर्गदनदपतपदघुमास्यतिहन्तियातिवाति…'),
    ),
    '8.4.18': (
        _c('प्रणिपचति (praṇipacati) — beside प्रनिपचति',
           {'root': 'ni', 'gana': 'śeṣa-dhātu', 'after': 'upasarga'},
           note='शेषे विभाषाऽकखादावषान्त उपदेशे'),
    ),
    '8.4.19': (
        _c('प्राणिति (prāṇiti) — he breathes',
           {'root': 'ani', 'after': 'upasarga'},
           note='अनितेः'),
    ),
    '8.4.20': (
        _c('हे प्राण् (he prāṇ) — O breath',
           {'root': 'ani', 'gana': 'pada-anta', 'after': 'upasarga'},
           note='अन्तः — पदान्तस्येति प्रतिषेधस्यापवादोऽयम्'),
    ),
    '8.4.21': (
        _c('प्राणिणिषति (prāṇiṇiṣati) — he wants to breathe',
           {'root': 'ani', 'gana': 'sābhyāsa', 'after': 'upasarga'},
           note='उभौ साभ्यासस्य — पूर्वत्रासिद्धीयमद्विर्वचने'),
    ),
    '8.4.22': (
        _c('प्रहण्यते (prahaṇyate) — he is struck',
           {'root': 'hanti', 'gana': 'at-pūrva', 'after': 'upasarga'},
           note='हन्तेरत्पूर्वस्य — अत्पूर्वस्येति किम्? प्रघ्नन्ति'),
    ),
    '8.4.23': (
        _c('प्रहण्वः (prahaṇvaḥ) — beside प्रहन्वः',
           {'root': 'hanti', 'before': 'va', 'after': 'upasarga'},
           note='वमोर्वा — हन्तेरिति वर्तते'),
    ),
    '8.4.24': (
        _c('अन्तर्हण्यते (antarhaṇyate) — he is struck within',
           {'root': 'hanti', 'gana': 'at-pūrva', 'after': 'antar', 'sense': 'a-deśa'},
           note='अन्तरदेशे — आदेश इति किम्? अन्तर्हननो देशः'),
    ),
    '8.4.25': (
        _c('अन्तरयणं शोभनम् (antarayaṇam) — the passage within is fine',
           {'root': 'ayana', 'after': 'antar', 'sense': 'a-deśa'},
           note='अयनं च — अदेश इत्येव, अन्तरयनो देशः'),
    ),
    '8.4.26': (
        _c('नृमणाः (nṛmaṇāḥ) — minded toward men',
           {'after': 'ṛ-anta-avagraha', 'chandasi': True},
           note='छन्दस्यृदवग्रहात् — ऋकारोऽवगृह्यते'),
    ),
    '8.4.27': (
        _c('अग्ने रक्षा णः (agne rakṣā ṇaḥ) — Agni, protect us',
           {'root': 'nas', 'after': 'dhātustha-uru-ṣu', 'chandasi': True},
           note='नश्च धातुस्थोरुषुभ्यः'),
    ),
    '8.4.28': (
        _c('प्रणो राजा (praṇo rājā) — our king',
           {'root': 'nas', 'after': 'upasarga'},
           note='उपसर्गाद् बहुलम् — बहुलग्रहणाद् भाषायामपि भवति'),
    ),
    '8.4.29': (
        _c('प्रयाणम् (prayāṇam) — a setting out',
           {'gana': 'kṛt-ac-para-na', 'after': 'upasarga'},
           note='कृत्यचः'),
    ),
    '8.4.30': (
        _c('प्रयापणम् (prayāpaṇam) — beside प्रयापनम्',
           {'gana': 'ṇi-kṛt', 'after': 'upasarga'},
           note='णेर्विभाषा'),
    ),
    '8.4.31': (
        _c('प्रकोपणम् (prakopaṇam) — beside प्रकोपनम्',
           {'gana': 'hal-ādi-ik-upadha-kṛt', 'after': 'upasarga'},
           note='हलश्च इजुपधात्'),
    ),
    '8.4.32': (
        _c('प्रेङ्खणम् (preṅkhaṇam) — a swinging',
           {'gana': 'ic-ādi-sanum-kṛt', 'after': 'upasarga'},
           note='इजादेः सनुमः — सामर्थ्यात् तदन्तविधिः'),
    ),
    '8.4.33': (
        _c('प्रणिन्दनम् (praṇindanam) — beside प्रनिन्दनम्',
           {'root': 'niṃs', 'after': 'upasarga'},
           note='वा निंसनिक्षनिन्दाम् — णोपदेशत्वादेतेषाम्'),
    ),
    '8.4.34': (
        _c('प्रभवनम् (prabhavanam) — an arising, with a plain न्',
           {'root': 'bhū', 'after': 'upasarga'},
           note='न भाभूपूकमिगमिप्यायीवेपाम्'),
    ),
    '8.4.35': (
        _c('निष्पानम् (niṣpānam) — a drinking-place',
           {'gana': 'ṣa-pada-anta-para'},
           note='षात् पदान्तात् — पदे अन्तः पदान्त इति सप्तमीसमासोऽयम्'),
    ),
    '8.4.36': (
        _c('प्रनष्टः (pranaṣṭaḥ) — lost, with a plain न्',
           {'root': 'naś', 'gana': 'ṣa-anta'},
           note='नशेः षान्तस्य — षान्तस्येति किम्? प्रणश्यति'),
    ),
    '8.4.37': (
        _c('वृक्षान् (vṛkṣān) — the trees, in the accusative',
           {'gana': 'pada-anta-na'},
           note='पदान्तस्य'),
    ),
    '8.4.38': (
        _c('प्र गां नयामः (pra gāṃ nayāmaḥ) — we lead the cow forth',
           {'gana': 'pada-vyavāya'},
           note='पदव्यवायेऽपि — पदेन व्यवायः पदव्यवधानम्'),
    ),
    '8.4.39': (
        _c('क्षुभ्नाति (kṣubhnāti) — he is agitated',
           {'gana': 'kṣubhnādi'},
           note='क्षुभ्नादिषु च — अजादेशस्य स्थानिवद्भावात्'),
    ),
    '8.4.40': (
        _c('तच्छिवः (tacchivaḥ) — that Śiva',
           {'gana': 'stu', 'before': 'ścu'},
           note='स्तोः श्चुना श्चुः — यथासंख्यमत्र नेष्यते'),
    ),
    '8.4.41': (
        _c('वृक्षष्षण्डे (vṛkṣaṣṣaṇḍe) — the tree in the grove',
           {'gana': 'stu', 'before': 'ṣṭu'},
           note='ष्टुना ष्टुः — अत्रापि तथैव संख्यातानुदेशाभावः'),
    ),
    '8.4.42': (
        _c('श्वलिट् साये (śvaliṭ sāye) — the dog-licker at evening',
           {'gana': 'stu', 'after': 'pada-anta-ṭu'},
           note='न पदान्ताट्टोरनाम् — अत्यल्पमिदमुच्यते'),
    ),
    '8.4.43': (
        _c('अग्निचित् षण्डे (agnicit ṣaṇḍe) — the fire-piler in the grove',
           {'gana': 'tu', 'before': 'ṣa'},
           note='तोः षि — नेति वर्तते'),
    ),
    '8.4.44': (
        _c('प्रश्नः (praśnaḥ) — a question',
           {'gana': 'tu', 'after': 'śa'},
           note='शात् — तोरिति वर्तते'),
    ),
    '8.4.45': (
        _c('वाङ् नयति (vāṅ nayati) — speech leads',
           {'gana': 'yar-pada-anta', 'before': 'anunāsika'},
           note='यरोऽनुनासिकेऽनुनासिको वा'),
    ),
    '8.4.46': (
        _c('अर्क्कः (arkkaḥ) — the sun, with the क् doubled',
           {'gana': 'yar', 'after': 'ac-ra-ha'},
           note='अचो रहाभ्यां द्वे — अच इति किम्? किन् ह्नुते'),
    ),
    '8.4.47': (
        _c('दद्ध्यत्र (daddhyatra) — curds here',
           {'gana': 'yar', 'after': 'ac', 'before': 'an-ac'},
           note='अनचि च — यणो मयो द्वे भवत इति वक्तव्यम्'),
    ),
    '8.4.48': (
        _c('पुत्रादिनी त्वमसि पापे (putrādinī) — you child-eater',
           {'word': 'putra', 'before': 'ādinī', 'sense': 'ākrośa'},
           note='नादिन्याक्रोशे पुत्रस्य — आक्रोश इति किम्?'),
    ),
    '8.4.49': (
        _c('कर्षति (karṣati) — he ploughs',
           {'gana': 'śar', 'before': 'ac'},
           note='शरोऽचि — अचीति किम्? दर्श्श्यते'),
    ),
    '8.4.50': (
        _c("इन्द्रः (indraḥ) — in Śākaṭāyana's view",
           {'gana': 'tri-prabhṛti', 'view': 'śākaṭāyana'},
           note='त्रिप्रभृतिषु शाकटायनस्य'),
    ),
    '8.4.51': (
        _c("अर्कः (arkaḥ) — in Śākalya's view",
           {'view': 'śākalya'},
           note='सर्वत्र शाकल्यस्य'),
    ),
    '8.4.52': (
        _c('सूत्रम् (sūtram) — after a long vowel, undoubled',
           {'after': 'dīrgha', 'view': 'ācārya'},
           note='दीर्घादाचार्याणाम्'),
    ),
    '8.4.53': (
        _c('लब्धा (labdhā) — one who obtains',
           {'gana': 'jhal', 'before': 'jhaś'},
           note='झलां जश् झशि — झशीति किम्? दत्तः'),
    ),
    '8.4.54': (
        _c('बुभूषति (bubhūṣati) — he wants to be',
           {'gana': 'abhyāsa-jhal'},
           note='अभ्यासे चर्च — प्रकृतिचरां प्रकृतिचरो भवन्ति'),
    ),
    '8.4.56': (
        _c('वाक् (vāk) — beside वाग्, at a pause',
           {'gana': 'jhal', 'after': 'avasāna'},
           note='वाऽवसाने — झलां चरिति वर्तते'),
    ),
    '8.4.57': (
        _c('दधिँ (dadhim̐) — beside दधि, at a pause',
           {'gana': 'aṇ-a-pragṛhya', 'after': 'avasāna'},
           note='अणोऽप्रगृह्यस्यानुनासिकः — अण इति किम्? कर्तृ'),
    ),
    '8.4.58': (
        _c('शङ्किता (śaṅkitā) — the anusvāra takes the ka-class',
           {'gana': 'anusvāra', 'before': 'yay'},
           note='अनुस्वारस्य ययि परसवर्णः'),
    ),
    '8.4.59': (
        _c('तङ् कथञ् चित्रपक्षण् (taṅ kathañ) — beside तं कथं',
           {'gana': 'anusvāra-pada-anta', 'before': 'yay'},
           note='वा पदान्तस्य'),
    ),
    '8.4.60': (
        _c('अग्निचिल्लुनाति (agnicillunāti) — the fire-piler cuts',
           {'gana': 'tu', 'before': 'la'},
           note='तोर्लि'),
    ),
    '8.4.61': (
        _c('उत्त्थाता (uttthātā) — one who rises',
           {'word': 'sthā', 'after': 'ud'},
           note='उदः स्थास्तम्भोः पूर्वस्य — सवर्ण इति वर्तते'),
    ),
    '8.4.62': (
        _c('वाग्घसति (vāgghasati) — beside वाग् हसति',
           {'gana': 'ha', 'after': 'jhay'},
           note='झयो होऽन्यतरस्याम्'),
    ),
    '8.4.63': (
        _c('वाक्छेते (vākchete) — beside वाक् शेते',
           {'gana': 'śa', 'after': 'jhay', 'before': 'aṭ'},
           note='शश्छोऽटि — झय इति वर्तते, अन्यतरस्यामिति च'),
    ),
    '8.4.64': (
        _c('शय्या (śayyā) — beside शय्य्या',
           {'gana': 'yam', 'after': 'hal', 'before': 'yam'},
           note='हलो यमां यमि लोपः'),
    ),
    '8.4.65': (
        _c('प्रत्तम् (prattam) — given away',
           {'gana': 'jhar', 'after': 'hal', 'before': 'jhar-savarṇa'},
           note='झरो झरि सवर्णे'),
    ),
    '8.4.66': (
        _c('गार्ग्यः (gārgyaḥ) — the low tone becomes svarita',
           {'gana': 'anudātta', 'after': 'udātta'},
           note='उदात्तादनुदात्तस्य स्वरितः — अस्य स्वरितस्यासिद्धत्वात्'),
    ),
    '8.4.67': (
        _c('गार्ग्यः (gārgyaḥ) — the low tone stays, for most teachers',
           {'gana': 'anudātta', 'after': 'udātta', 'before': 'udātta-svarita-udaya', 'view': 'a-gārgya-kāśyapa-gālava'},
           note='नोदात्तस्वरितोदयमगार्ग्यकाश्यपगालवानाम्'),
    ),
    '8.4.68': (
        _c('वृक्षः (vṛkṣaḥ) — the last rule of the work',
           {'word': 'a'},
           note='अ अ इति — विवृतस्य संवृतः क्रियते'),
    ),
    "3.1.133": (
        _c("kārakaḥ, kartā — any root", {"root": "bhaj"},
           note="ण्वुल्तृचौ, सर्वधातुभ्यः — the widest rule of the run, "
                "and the one 3.1.95's heading stopped before."),
    ),
    "3.1.135": (
        _c("vikṣipaḥ — an ik penult", {"root": "kṣip"},
           note="इगुपधज्ञाप्रीकिरः कः — इगुपध asked of 1.1.65 and the "
                "pratyāhāra इक्, not restated."),
        _c("jñaḥ — named, having no ik penult", {"root": "jñā"},
           note="ज्ञा's penult is ञ्, which is why it had to be named: "
                "asking 1.1.65 is what shows that."),
    ),
    "3.1.136": (
        _c("prasthaḥ", {"root": "sthā", "upasarga": "pra"},
           note="आतश्चोपसर्गे, णस्यापवादः — and the preverb is asked of "
                "1.4.59."),
    ),
    "3.1.137": (
        _c("utpaśyaḥ", {"root": "dṛś", "upasarga": "ud"},
           note="पाघ्राध्माधेट्दृशः शः. उपसर्ग इति केचिन् "
                "नानुवर्तयन्ति — a reading the vṛtti reports."),
    ),
    "3.1.138": (
        _c("limpaḥ — no preverb", {"root": "limp"},
           note="अनुपसर्गाल्लिम्प… — सातिः सौत्रो धातुः, one the sūtra "
                "supplies itself."),
        _c("pralipaḥ — with a preverb",
           {"root": "limp", "upasarga": "pra"}, kind="counter",
           note="अनुपसर्गादिति किम्?"),
    ),
    "3.1.139": (
        _c("dadaḥ, beside dāyaḥ", {"root": "dā"},
           note="ददातिदधात्योर्विभाषा, णस्यापवादः."),
    ),
    "3.1.140": (
        _c("jvālaḥ, beside jvalaḥ", {"root": "jval"},
           note="ज्वलितिकसन्तेभ्यो णः — and the गण is a STRETCH of the "
                "dhātupāṭha, read off by its codes."),
    ),
    "3.1.141": (
        _c("vyādhaḥ", {"root": "vyadh"},
           note="श्यादव्यधास्रु…श्च — अनुपसर्गादिति विभाषेति च "
                "निवृत्तम्."),
        _c("avaśyāyaḥ — named to defeat 3.1.136",
           {"root": "śyai", "upasarga": "ava"},
           note="आकारान्तत्वादेव सिद्धे पुनर्वचनं बाधकबाधनार्थम् — "
                "श्यै is आ-final and reached anyway, so the naming is "
                "to beat the क a preverb would have given."),
    ),
    "3.1.142": (
        _c("dāvaḥ, nāyaḥ", {"root": "du"},
           note="दुन्योरनुपसर्गे. अनुपसर्ग इति किम्? प्रदवः."),
    ),
    "3.1.143": (
        _c("grāhaḥ, beside grahaḥ", {"root": "grah"},
           note="विभाषा ग्रहः — व्यवस्थितविभाषा: जलचरे नित्यं ग्राहः, "
                "ज्योतिषि ग्रह एव."),
    ),
    "3.1.144": (
        _c("gṛham — a house", {"root": "grah", "sense": "geha"},
           note="गेहे कः, and तात्स्थ्याद् दाराश्च reaches a household "
                "by what stands in it."),
    ),
    "3.1.145": (
        _c("nartakaḥ — a craftsman", {"root": "nṛt", "craftsman": True},
           note="शिल्पिनि ष्वुन्, held to three roots by a परिगणन."),
    ),
    "3.1.146": (
        _c("gāthakaḥ", {"root": "gai", "craftsman": True},
           note="गस्थकन् — and 3.1.147 gives the same root ण्युट् "
                "beside it, गायनः."),
    ),
    "3.1.147": (
        _c("gāyanaḥ — the second affix for the same root",
           {"root": "gā", "craftsman": True},
           note="ण्युट् च, चकारेण ग इत्यनुकृष्यते. योगविभाग "
                "उत्तरार्थः — the split is for 3.1.148."),
    ),
    "3.1.148": (
        _c("hāyanāḥ — a kind of rice",
           {"root": "hā", "sense": "vrīhi"},
           note="हश्च व्रीहिकालयोः — जहत्युदकम् इति कृत्वा."),
        _c("hāyanaḥ — a year", {"root": "hā", "sense": "kāla"},
           note="जिहीते भावान् इति कृत्वा — the other of two roots "
                "written alike."),
    ),
    "3.1.149": (
        _c("pravakaḥ — doing a thing well",
           {"root": "pru", "sense": "samabhihāra"},
           note="प्रुसृल्वः समभिहारे वुन् — and समभिहार here is "
                "साधुकारित्व, NOT 3.1.22's पौनःपुन्य."),
    ),
    "3.1.150": (
        _c("jīvakaḥ — may he live", {"root": "jīv", "sense": "āśis"},
           note="आशिषि च, धातुमात्रात् — the last rule of the pāda, and "
                "as wide as the first."),
    ),
    "3.1.96": (
        _c("kartavyam — any root at all", {},
           note="तव्यत्तव्यानीयरः — three affixes, and the widest rule "
                "of the run: everything after it cuts into its ground."),
    ),
    "3.1.97": (
        _c("geyam — a vowel-final root", {"root_ends_in": "ac"},
           note="अचो यत्, and अज्ग्रहणम् reaches a root that USED to "
                "end in a vowel: दित्स्यम्."),
    ),
    "3.1.98": (
        _c("śapyam — a labial with short a before it",
           {"root_ends_in": "pu", "penult": "a"},
           note="पोरदुपधात्, ण्यतोऽपवादः. तपरकरणं तत्कालार्थम् — the "
                "अ must be short."),
    ),
    "3.1.99": (
        _c("śakyam", {"root": "śak"},
           note="शकिसहोश्च — consonant-final, so the same अपवाद against "
                "3.1.124, made by name."),
    ),
    "3.1.100": (
        _c("gadyam — no preverb", {"root": "gad"},
           note="गदमदचरयमश्चानुपसर्गे, and यम् is named "
                "अनुपसर्गनियमार्थम् — to be restricted, not granted."),
        _c("pragādyam — with a preverb",
           {"root": "gad", "upasarga": "pra"}, kind="counter",
           note="अनुपसर्ग इति किम्?"),
    ),
    "3.1.106": (
        _c("brahmodyam, beside brahmavadyam",
           {"root": "vad", "upapada": True},
           note="वदः सुपि क्यप् च — the च gives यत् too, so both stand. "
                "And the सुबन्त beside it is 3.1.92's उपपद."),
    ),
    "3.1.107": (
        _c("brahmabhūyaṃ gataḥ",
           {"root": "bhū", "upapada": True, "sense": "bhāva"},
           note="भुवो भावे — यत् तु नानुवर्तते, so क्यप् alone."),
    ),
    "3.1.108": (
        _c("brahmahatyā",
           {"root": "han", "upapada": True, "sense": "bhāva"},
           note="हनस्त च — and ण्यत् तु भावे न भवति अनभिधानात्, usage "
                "rather than a rule keeping the rival out."),
    ),
    "3.1.109": (
        _c("stutyaḥ", {"root": "stu"},
           note="एतिस्तुशास्वृदृजुषः क्यप् — and क्यप् said again "
                "बाधकबाधनार्थम्, to defeat 3.1.125: अवश्यस्तुत्यः."),
    ),
    "3.1.110": (
        _c("vṛtyam — an ṛ penult", {"penult": "ṛ"},
           note="ऋदुपधाच्चाकॢपिचृतेः."),
        _c("kalpyam — excepted by name",
           {"root": "kḷp", "penult": "ṛ"}, kind="counter",
           note="अक्ऌपिचृतेरिति किम्?"),
    ),
    "3.1.111": (
        _c("kheyam", {"root": "khan"},
           note="ई च खनः — दीर्घनिर्देशः प्रश्लेषार्थः, the long ī read "
                "as two so the second blocks 6.4.43."),
    ),
    "3.1.112": (
        _c("bhṛtyāḥ", {"root": "bhṛ", "sense": "not-a-name"},
           note="भृञोऽसंज्ञायाम्. असंज्ञायामिति किम्? भार्यो नाम "
                "क्षत्रियः."),
    ),
    "3.1.113": (
        _c("parimṛjyaḥ, beside parimārgyaḥ", {"root": "mṛj"},
           note="मृजेर्विभाषा — प्राप्तविभाषेयम्, 3.1.110 had it "
                "already by its ऋ penult."),
    ),
    "3.1.118": (
        _c("pratigṛhyam — in the Veda",
           {"root": "grah", "upasarga": "prati", "chandas": True},
           note="प्रत्यपिभ्यां ग्रहेश्छन्दसि. छन्दसीति किम्? "
                "प्रतिग्राह्यम्."),
    ),
    "3.1.119": (
        _c("grāmagṛhyā senā", {"root": "grah", "sense": "grah-four"},
           note="पदास्वैरिबाह्यापक्ष्येषु च, and "
                "स्त्रीलिङ्गनिर्देशाद् अन्यत्र न भवति."),
    ),
    "3.1.120": (
        _c("kṛtyam, beside kāryam", {"root": "kṛ"},
           note="विभाषा कृवृषोः — and the two are reached from opposite "
                "sides, कृ against ण्यत् and वृष् against क्यप्."),
    ),
    "3.1.122": (
        _c("amāvāsyā, beside amāvasyā",
           {"root": "vas", "upapada": True},
           note="अमावस्यदन्यतरस्याम् — the option is about the "
                "STRENGTHENING, not the affix."),
    ),
    "3.1.124": (
        _c("kāryam — ṛ or a consonant", {"root_ends_in": "ṛ-or-hal"},
           note="ऋहलोर्ण्यत्, पञ्चम्यर्थे षष्ठी — the general rule three "
                "earlier ones were taking ground from."),
    ),
    "3.1.125": (
        _c("lāvyam — where a thing must be done",
           {"root_ends_in": "u", "sense": "āvaśyaka"},
           note="ओरावश्यके, यतोऽपवादः — ण्यत् taking ground back from "
                "3.1.97."),
        _c("lavyam — without that sense", {"root_ends_in": "u"},
           kind="counter", note="आवश्यक इति किम्?"),
    ),
    "3.1.126": (
        _c("vāpyam", {"root": "vap"},
           note="आसुयुवपिरपिलपित्रपिचमश्च, यतोऽपवादः. "
                "अनुक्तसमुच्चयार्थश्चकारः, and दभ् is added on it."),
    ),
    "3.1.101": (
        _c("avadyaṃ pāpam — fixed whole", {"sutra_id": "3.1.101"},
           note="A निपातन: यदिह लक्षणेनानुपपन्नं तत् सर्वं "
                "निपातनात् सिद्धम् — recorded as the sūtra gives "
                "it, with the sense it holds in, and not derived."),
    ),
    "3.1.102": (
        _c("vahyaṃ śakaṭam — fixed whole", {"sutra_id": "3.1.102"},
           note="A निपातन: यदिह लक्षणेनानुपपन्नं तत् सर्वं "
                "निपातनात् सिद्धम् — recorded as the sūtra gives "
                "it, with the sense it holds in, and not derived."),
    ),
    "3.1.103": (
        _c("aryaḥ svāmī — fixed whole", {"sutra_id": "3.1.103"},
           note="A निपातन: यदिह लक्षणेनानुपपन्नं तत् सर्वं "
                "निपातनात् सिद्धम् — recorded as the sūtra gives "
                "it, with the sense it holds in, and not derived."),
    ),
    "3.1.104": (
        _c("upasaryā gauḥ — fixed whole", {"sutra_id": "3.1.104"},
           note="A निपातन: यदिह लक्षणेनानुपपन्नं तत् सर्वं "
                "निपातनात् सिद्धम् — recorded as the sūtra gives "
                "it, with the sense it holds in, and not derived."),
    ),
    "3.1.105": (
        _c("ajaryaṃ saṃgatam — fixed whole", {"sutra_id": "3.1.105"},
           note="A निपातन: यदिह लक्षणेनानुपपन्नं तत् सर्वं "
                "निपातनात् सिद्धम् — recorded as the sūtra gives "
                "it, with the sense it holds in, and not derived."),
    ),
    "3.1.114": (
        _c("rājasūyaḥ kratuḥ — fixed whole", {"sutra_id": "3.1.114"},
           note="A निपातन: यदिह लक्षणेनानुपपन्नं तत् सर्वं "
                "निपातनात् सिद्धम् — recorded as the sūtra gives "
                "it, with the sense it holds in, and not derived."),
    ),
    "3.1.115": (
        _c("bhidyaḥ, uddhyaḥ — fixed whole", {"sutra_id": "3.1.115"},
           note="A निपातन: यदिह लक्षणेनानुपपन्नं तत् सर्वं "
                "निपातनात् सिद्धम् — recorded as the sūtra gives "
                "it, with the sense it holds in, and not derived."),
    ),
    "3.1.116": (
        _c("puṣyaḥ, siddhyaḥ — fixed whole", {"sutra_id": "3.1.116"},
           note="A निपातन: यदिह लक्षणेनानुपपन्नं तत् सर्वं "
                "निपातनात् सिद्धम् — recorded as the sūtra gives "
                "it, with the sense it holds in, and not derived."),
    ),
    "3.1.117": (
        _c("vipūyo muñjaḥ — fixed whole", {"sutra_id": "3.1.117"},
           note="A निपातन: यदिह लक्षणेनानुपपन्नं तत् सर्वं "
                "निपातनात् सिद्धम् — recorded as the sūtra gives "
                "it, with the sense it holds in, and not derived."),
    ),
    "3.1.121": (
        _c("yugyo gauḥ — fixed whole", {"sutra_id": "3.1.121"},
           note="A निपातन: यदिह लक्षणेनानुपपन्नं तत् सर्वं "
                "निपातनात् सिद्धम् — recorded as the sūtra gives "
                "it, with the sense it holds in, and not derived."),
    ),
    "3.1.123": (
        _c("niṣṭarkyam — eighteen Vedic forms — fixed whole", {"sutra_id": "3.1.123"},
           note="A निपातन: यदिह लक्षणेनानुपपन्नं तत् सर्वं "
                "निपातनात् सिद्धम् — recorded as the sūtra gives "
                "it, with the sense it holds in, and not derived."),
    ),
    "3.1.127": (
        _c("ānāyyo dakṣiṇāgniḥ — fixed whole", {"sutra_id": "3.1.127"},
           note="A निपातन: यदिह लक्षणेनानुपपन्नं तत् सर्वं "
                "निपातनात् सिद्धम् — recorded as the sūtra gives "
                "it, with the sense it holds in, and not derived."),
    ),
    "3.1.128": (
        _c("praṇāyyaścoraḥ — fixed whole", {"sutra_id": "3.1.128"},
           note="A निपातन: यदिह लक्षणेनानुपपन्नं तत् सर्वं "
                "निपातनात् सिद्धम् — recorded as the sūtra gives "
                "it, with the sense it holds in, and not derived."),
    ),
    "3.1.129": (
        _c("pāyyaṃ mānam — fixed whole", {"sutra_id": "3.1.129"},
           note="A निपातन: यदिह लक्षणेनानुपपन्नं तत् सर्वं "
                "निपातनात् सिद्धम् — recorded as the sūtra gives "
                "it, with the sense it holds in, and not derived."),
    ),
    "3.1.130": (
        _c("kuṇḍapāyyaḥ kratuḥ — fixed whole", {"sutra_id": "3.1.130"},
           note="A निपातन: यदिह लक्षणेनानुपपन्नं तत् सर्वं "
                "निपातनात् सिद्धम् — recorded as the sūtra gives "
                "it, with the sense it holds in, and not derived."),
    ),
    "3.1.131": (
        _c("paricāyyam — fixed whole", {"sutra_id": "3.1.131"},
           note="A निपातन: यदिह लक्षणेनानुपपन्नं तत् सर्वं "
                "निपातनात् सिद्धम् — recorded as the sūtra gives "
                "it, with the sense it holds in, and not derived."),
    ),
    "3.1.132": (
        _c("cityo'gniḥ — fixed whole", {"sutra_id": "3.1.132"},
           note="A निपातन: यदिह लक्षणेनानुपपन्नं तत् सर्वं "
                "निपातनात् सिद्धम् — recorded as the sūtra gives "
                "it, with the sense it holds in, and not derived."),
    ),
    "3.1.69": (
        _c("dīvyati — the fourth class", {"root": "div", "gana": "04"},
           note="दिवादिभ्यः श्यन्, शपोऽपवादः. दिव् is read in three "
                "classes, so which is meant has to be said."),
    ),
    "3.1.70": (
        _c("bhrāmyati, beside bhramati", {"root": "bhramu"},
           note="वा भ्राशभ्लाश… — and भ्रमु is read twice in the "
                "dhātupāṭha, द्वयोरपि ग्रहणम्."),
    ),
    "3.1.71": (
        _c("yasyati, beside yasati", {"root": "yas"},
           note="यसोऽनुपसर्गात् — a fourth-class root, so the marker "
                "was obligatory and this makes it a choice."),
        _c("āyasyati — with a preverb",
           {"root": "yas", "upasarga": "ā"}, kind="counter",
           note="अनुपसर्गादिति किम्?"),
    ),
    "3.1.72": (
        _c("saṃyasyati, beside saṃyasati",
           {"root": "yas", "upasarga": "sam"},
           note="संयसश्च — सोपसर्गार्थ आरम्भः."),
    ),
    "3.1.73": (
        _c("sunoti — the fifth class", {"root": "ṣuñ"},
           note="स्वादिभ्यः श्नुः, शपोऽपवादः."),
    ),
    "3.1.74": (
        _c("śṛṇoti", {"root": "śru"},
           note="श्रुवः शृ च — the marker and a change of shape, "
                "तत्संनियोगेन."),
    ),
    "3.1.75": (
        _c("akṣṇoti, beside akṣati", {"root": "akṣ"},
           note="अक्षोऽन्यतरस्याम् — भौवादिकः, so the choice is against "
                "शप् and not against nothing."),
    ),
    "3.1.76": (
        _c("takṣṇoti kāṣṭham", {"root": "takṣ", "sense": "tanūkaraṇa"},
           note="तनूकरणे तक्षः, and अनेकार्थत्वाद् धातूनां "
                "विशेषणोपादानम्."),
        _c("saṃtakṣati vāgbhiḥ — another sense", {"root": "takṣ"},
           kind="counter", note="तनूकरण इति किम्?"),
    ),
    "3.1.77": (
        _c("tudati — the sixth class", {"root": "tud"},
           note="तुदादिभ्यः शः."),
    ),
    "3.1.78": (
        _c("ruṇaddhi — the seventh", {"root": "rudh", "gana": "07"},
           note="रुधादिभ्यः श्नम् — मकारो देशविध्यर्थः, so by 1.1.47 it "
                "goes INSIDE the root. रुध् is read in 04 too, so the "
                "class has to be said."),
    ),
    "3.1.79": (
        _c("tanoti — the eighth class", {"root": "tan", "gana": "08"},
           note="तनादिकृञ्भ्य उः."),
        _c("karoti — named though already in the class", {"root": "kṛ"},
           note="करोतेरुपादानं नियमार्थम् — it restricts, so 2.4.79's "
                "optional elision of सिच् does not reach कृ: अकृत."),
    ),
    "3.1.80": (
        _c("dhinoti", {"root": "dhinvi"},
           note="धिन्विकृण्व्योर अ च — and the dropped अ still keeps "
                "guṇa away, being स्थानिवत् by 1.1.56."),
    ),
    "3.1.81": (
        _c("krīṇāti — the ninth class", {"root": "ḍukrīñ"},
           note="क्र्यादिभ्यः श्ना."),
    ),
    "3.1.82": (
        _c("stabhnāti and stabhnoti — both markers",
           {"root": "stanbhu"},
           note="…श्नुश्च — BOTH markers. आद्याश्चत्वारो धातवः सौत्राः, "
                "supplied by the sūtra itself."),
    ),
    "3.1.83": (
        _c("muṣāṇa — before hi, after a consonant",
           {"root": "muṣ", "before_hi": True},
           note="हलः श्नः शानज्झौ — and श्नः is a स्थानिनिर्देश "
                "आदेशसंप्रत्ययार्थः."),
    ),
    "3.1.84": (
        _c("gṛbhāya — in the Veda",
           {"root": "grah", "chandas": True},
           note="छन्दसि शायजपि — शानच् stands beside it, the अपि adding "
                "rather than replacing."),
    ),
    "3.1.85": (
        _c("bhedati, where bhinatti was due", {},
           note="व्यत्ययो बहुलम् — a licence, not a rule with an output. "
                "बहुलग्रहणं सर्वविधिव्यभिचारार्थम्."),
    ),
    "3.1.86": (
        _c("gamema — a Vedic benedictive", {"lakara": "liṅ"},
           note="लिङ्याशिष्यङ् — and 3.4.117 छन्दस्युभयथा is what lets "
                "a विकरण stand before it at all."),
    ),
    "3.1.87": (
        _c("bhidyate kāṣṭhaṃ svayameva", {},
           note="कर्मवत् कर्मणा तुल्यक्रियः — four effects, named by the "
                "vṛtti: यक्, the middle, चिण्, चिण्वद्भाव."),
        _c("where the actions are not alike", {"tulyakriya": False},
           kind="counter", note="कर्मणा तुल्यक्रियः is a condition."),
    ),
    "3.1.88": (
        _c("tapyate tapastāpasaḥ",
           {"root": "tap", "object_of_tap": True},
           note="तपस्तपःकर्मकस्यैव — पूर्वेणाप्राप्तः कर्मवद्भावो "
                "विधीयते, so it grants despite the एव."),
        _c("uttapati suvarṇaṃ suvarṇakāraḥ", {"root": "tap"},
           kind="counter", note="तपःकर्मकस्यैवेति किम्?"),
    ),
    "3.1.89": (
        _c("dugdhe gauḥ svayameva — two effects refused",
           {"root": "duh"},
           note="न दुहस्नुनमां यक्चिणौ — and for दुह् the चिण् was "
                "already a choice by 3.1.63, so only the यक् is newly "
                "refused."),
    ),
    "3.1.90": (
        _c("kuṣyati pādaḥ svayameva",
           {"root": "kuṣ", "pracam": True},
           note="कुषिरजोः प्राचां श्यन् परस्मैपदं च — यगात्मनेपदयोरपवादौ."),
        _c("cukuṣe — the perfect keeps the middle",
           {"root": "kuṣ", "pracam": True, "lakara": "liṭ"},
           kind="counter",
           note="व्यवस्थितविभाषा — तेन लिट्लिङोः स्यादिविषये च न भवतः."),
    ),
    "3.1.91": (
        _c("dhātoḥ — the heading over adhyāya 3", {},
           note="आ तृतीयाध्यायपरिसमाप्तेः, and the vṛtti defends the "
                "word by naming what would go wrong without it."),
    ),
    "3.1.92": (
        _c("kumbhakāraḥ — karmaṇi is in the locative",
           {"in_locative": True},
           note="तत्रोपपदं सप्तमीस्थम्, and स्थग्रहणात्तु सर्वत्र भवति."),
        _c("a word named in another case", {}, kind="counter",
           note="सप्तमीस्थम् is the condition."),
    ),
    "3.1.93": (
        _c("kartavyam — a kṛt affix", {"affix": "tavya"},
           note="कृदतिङ् — and 1.2.46 then makes the finished word a "
                "प्रातिपदिक."),
        _c("cīyāt — a tiṅ ending", {"is_tin": True}, kind="counter",
           note="अतिङिति किम्?"),
    ),
    "3.1.95": (
        _c("the name 2.1.33 and 2.3.71 invoke", {},
           note="कृत्याः — प्राक् एतस्मात् ण्वुल्संशब्दनात्, the range "
                "given by naming where it stops. Both rules that use "
                "the name are codified."),
        _c("outside its range", {"sutra_id": "3.1.133"}, kind="counter",
           note="3.1.133 ण्वुल्तृचौ is where the heading stops."),
    ),
    "3.1.33": (
        _c("kariṣyati — the future", {"lakara": "lṛṭ"},
           note="स्यतासी लृलुटोः, यथासंख्यम्, and लृ covers लृट् and "
                "लृङ् both."),
        _c("śvaḥ kartā — the periphrastic future", {"lakara": "luṭ"},
           note="The second of the two, with its इ marked "
                "अनुनासिकलोपप्रतिबन्धार्थम्."),
    ),
    "3.1.34": (
        _c("joṣiṣat — sip in leṭ", {"lakara": "leṭ"},
           note="सिब्बहुलं लेटि — बहुलम्, so both are attested and "
                "neither is a choice offered."),
    ),
    "3.1.35": (
        _c("kāsāñcakre", {"lakara": "liṭ", "root": "kās"},
           note="कास्प्रत्ययादाममन्त्रे लिटि."),
        _c("lolūyāñcake — an affix-final stem",
           {"lakara": "liṭ", "affix_final": True},
           note="प्रत्ययात् — what carries the whole सनादि run of "
                "3.1.5 to 3.1.31 into the perfect."),
        _c("kṛṣṇo nonāva — in a mantra",
           {"lakara": "liṭ", "root": "kās", "mantra": True},
           kind="counter", note="अमन्त्र इति किम्?"),
    ),
    "3.1.36": (
        _c("īhāñcakre", {"lakara": "liṭ", "ijadi_guru": True},
           note="इजादेश्च गुरुमतोऽनृच्छः."),
        _c("ānarccha — ṛcch excepted by name",
           {"lakara": "liṭ", "ijadi_guru": True, "root": "ṛcch"},
           kind="counter",
           note="अनृच्छ इति किम्? It meets both conditions and is still "
                "left out."),
    ),
    "3.1.37": (
        _c("āsāñcakre", {"lakara": "liṭ", "root": "ās"},
           note="दयायासश्च."),
    ),
    "3.1.38": (
        _c("vidāñcakāra, beside viveda",
           {"lakara": "liṭ", "root": "vid"},
           note="उषविदजागृभ्योऽन्यतरस्याम्."),
    ),
    "3.1.39": (
        _c("bibhayāñcakāra", {"lakara": "liṭ", "root": "bhī"},
           note="भीह्रीभृहुवां श्लुवच्च — and किं पुनस्तत्? द्वित्वम् "
                "इत्त्वं च."),
    ),
    "3.1.40": (
        _c("pācayāmāsa — a second verb follows", {"after_am": True},
           note="कृञ् चानुप्रयुज्यते लिटि, and तत्सामर्थ्यात् "
                "अस्तेर्भूभावो न भवति — 2.4.52 is kept off."),
    ),
    "3.1.41": (
        _c("vidāṅkurvantu — fixed whole", {"sutra_id": "3.1.41"},
           note="विदाङ्कुर्वन्त्वित्यन्यतरस्याम्, a निपातन; and "
                "इतिकरणः प्रदर्शनार्थः, so the whole paradigm follows."),
    ),
    "3.1.42": (
        _c("abhyutsādayāmakaḥ — fixed whole, in the Veda",
           {"sutra_id": "3.1.42"},
           note="A निपातन: what a form is fixed as, it is. These are "
                "recorded as the sūtra gives them and are not derived, "
                "which is why they answer through their own entry point "
                "rather than through the table."),
    ),
    "3.1.43": (
        _c("the slot the aorist opens", {},
           note="च्लि लुङि — a placeholder. अस्य सिजादीन् आदेशान् "
                "वक्ष्यति, तत्रैवोदाहरिष्यामः."),
    ),
    "3.1.44": (
        _c("akārṣīt — the default", {"root": "kṛ"},
           note="च्लेः सिच्, and every rule after it is an अपवाद."),
    ),
    "3.1.45": (
        _c("adhukṣat", {"root": "duh", "shal_igupadha_anit": True},
           note="शल इगुपधादनिटः क्सः — three conditions together."),
        _c("abhaitsīt — one condition short", {"root": "bhid"},
           kind="counter", note="शल इति किम्?"),
    ),
    "3.1.46": (
        _c("āślikṣat kanyām", {"root": "śliṣ", "sense": "āliṅgana"},
           note="श्लिष आलिङ्गने — अत्र नियमार्थमेतत्, restricting what "
                "3.1.45 had already granted."),
    ),
    "3.1.47": (
        _c("na dṛśaḥ — the ksa refused",
           {"root": "dṛś", "shal_igupadha_anit": True},
           note="And अस्मिन् प्रतिषिद्धे इरितो वा इत्यङ्सिचौ भवतः — "
                "3.1.57 answers instead, so both अदर्शत् and अद्राक्षीत् "
                "stand."),
    ),
    "3.1.48": (
        _c("aśiśriyat", {"root": "śri"},
           note="णिश्रिद्रुस्रुभ्यः कर्तरि चङ् — two marks, two later "
                "rules."),
        _c("acīkarat — any causative stem", {"root": "kṛ",
                                             "nyanta": True},
           note="ण्यन्तेभ्यो धातुभ्यः, the other half of the same rule."),
    ),
    "3.1.49": (
        _c("adadhat", {"root": "dheṭ"},
           note="विभाषा धेट्श्व्योः — and on the सिच् side 2.4.78 "
                "elides it, अधात् beside अधासीत्."),
    ),
    "3.1.50": (
        _c("ajūgupatam — in the Veda",
           {"root": "gup", "chandas": True},
           note="गुपेश्छन्दसि, यत्र आयप्रत्ययो नास्ति."),
    ),
    "3.1.51": (
        _c("kāmamūnayīḥ — the caṅ refused, in the Veda",
           {"root": "ūna", "nyanta": True, "chandas": True},
           note="नोनयति… — and outside the Veda it comes: औनिनत्."),
    ),
    "3.1.52": (
        _c("avocat", {"root": "vac"},
           note="अस्यतिवक्तिख्यातिभ्योऽङ् — and वच् may itself be what "
                "ब्रू became by 2.4.53."),
    ),
    "3.1.53": (
        _c("alipat", {"root": "lip"},
           note="लिपिसिचिह्वश्च, पृथग्योग उत्तरार्थः."),
    ),
    "3.1.54": (
        _c("alipata, beside alipta",
           {"root": "lip", "atmanepada": True},
           note="आत्मनेपदेष्वन्यतरस्याम् — पूर्वेण प्राप्ते "
                "विभाषारभ्यते."),
    ),
    "3.1.55": (
        _c("agamat — a ḷdit root", {"root": "gam"},
           note="…ॢदितः परस्मैपदेषु, and the mark is read from the "
                "dhātupāṭha by asking 1.3.2."),
        _c("apuṣat — the puṣādi sub-gaṇa",
           {"root": "puṣ", "gana": "puṣādi"},
           note="पुषादिर् दिवाद्यन्तर्गणो गृह्यते — and that list is "
                "not on disk, so it is asserted."),
    ),
    "3.1.56": (
        _c("asarat", {"root": "sṛ"},
           note="सर्तिशास्त्यर्तिभ्यश्च, पृथग्योगकरणम् आत्मनेपदार्थम्."),
    ),
    "3.1.57": (
        _c("abhidat, beside abhaitsīt", {"root": "bhid"},
           note="इरितो वा — भिदिर् carries the mark, and 1.3.2 is what "
                "makes it an इत्."),
        _c("abhitta — the middle keeps the sic",
           {"root": "bhid", "atmanepada": True}, kind="counter",
           note="परस्मैपदेष्वित्येव, carried by 3.1.56's च."),
    ),
    "3.1.58": (
        _c("ajarat, beside ajārīt", {"root": "jṝ"},
           note="जॄस्तम्भु…च, वेति वर्तते."),
    ),
    "3.1.59": (
        _c("āruhat — in the Veda", {"root": "ruh", "chandas": True},
           note="कृमृदृरुहिभ्यश्छन्दसि. छन्दसीति किम्? अरुक्षत्."),
    ),
    "3.1.60": (
        _c("udapādi sasyam",
           {"root": "pad", "before": "ta", "atmanepada": True},
           note="चिण् ते पदः — and सामर्थ्यात् आत्मनेपदैकवचनं गृह्यते."),
    ),
    "3.1.61": (
        _c("abodhi, beside abuddha",
           {"root": "budh", "before": "ta", "atmanepada": True},
           note="दीपजनबुध…अन्यतरस्याम्, with चिण् त carried down."),
    ),
    "3.1.62": (
        _c("akāri kaṭaḥ svayameva",
           {"root": "kṛ", "ac_final": True, "voice": "karmakartari",
            "before": "ta", "atmanepada": True},
           note="अचः कर्मकर्तरि — प्राप्तविभाषेयम्, an option over what "
                "was already optional."),
    ),
    "3.1.63": (
        _c("adohi gauḥ svayameva",
           {"root": "duh", "voice": "karmakartari", "before": "ta",
            "atmanepada": True},
           note="दुहश्च — दुह् is consonant-final, so 3.1.62 could not "
                "have reached it."),
    ),
    "3.1.64": (
        _c("anvavāruddha gauḥ svayameva — the ciṇ refused",
           {"root": "rudh", "voice": "karmakartari"},
           note="न रुधः."),
    ),
    "3.1.65": (
        _c("atapta tapastāpasaḥ — refused, of remorse",
           {"root": "tap", "sense": "anutāpa"},
           note="तपोऽनुतापे च — and तस्य ग्रहणम् अकर्मकर्त्रर्थम्, so "
                "the refusal reaches भाव and कर्मन् too."),
    ),
    "3.1.66": (
        _c("aśāyi bhavatā",
           {"voice": "bhāvakarmaṇoḥ", "before": "ta",
            "atmanepada": True},
           note="चिण् भावकर्मणोः — चिण्ग्रहणं विस्पष्टार्थम्."),
    ),
    "3.1.67": (
        _c("kriyate kaṭaḥ", {"voice": "bhāvakarmaṇoḥ"},
           note="सार्वधातुके यक् — ककारो गुणवृद्धिप्रतिषेधार्थः."),
        _c("kriyate kaṭaḥ svayameva — yak beats śap",
           {"voice": "karmakartari"},
           note="विप्रतिषेधाद्धि यकः शपो बलीयस्त्वम्, and 3.1.68 is "
                "codified, so the two genuinely meet."),
    ),
    "3.1.1": (
        _c("tavya in kartavyam is an affix", {"prescribes": "pratyaya"},
           note="प्रत्ययः — an अधिकार to the end of adhyāya 5."),
        _c("an āgama is not one", {"prescribes": "āgama"}, kind="counter",
           note="प्रकृत्युपपदोपाधिविकारागमान् वर्जयित्वा — an augment is "
                "inserted INTO the base, not added after it."),
        _c("a prakṛti is the base, not the affix",
           {"prescribes": "prakṛti"}, kind="counter",
           note="The first of the five the vṛtti excludes."),
    ),
    "3.1.2": (
        _c("kartavyam — the affix follows the root", {},
           note="परश्च, and चकारः समुच्चयार्थः so that in उणादि too the "
                "position is not open to doubt."),
    ),
    "3.1.3": (
        _c("kartavyam — accent on the affix's first vowel", {},
           note="आद्युदात्तश्च — needed because a multi-syllable affix "
                "would else leave the place unfixed."),
    ),
    "3.1.4": (
        _c("pacati — a pit affix, unaccented", {"pit": True},
           note="अनुदात्तौ सुप्पितौ, पूर्वस्यायमपवादः."),
        _c("dṛṣadau — a sup ending, unaccented", {"sup": True},
           note="The other half of the same exception."),
    ),
    "3.1.5": (
        _c("jugupsate", {"base": "gup",
                         "sense": "nindā-kṣamā-vyādhipratīkāra"},
           note="गुप्तिज्किद्भ्यः सन्, held to three senses by a "
                "vārttika."),
        _c("gopayati — another sense", {"base": "gup"}, kind="counter",
           note="अन्यत्र यथाप्राप्तं प्रत्यया भवन्ति."),
    ),
    "3.1.6": (
        _c("mīmāṃsate", {"base": "mān"},
           note="मान्बधदान्शान्भ्यो दीर्घश्चाभ्यासस्य — the affix and the "
                "lengthening in one rule."),
    ),
    "3.1.7": (
        _c("cikīrṣati", {"base": "kṛ", "sense": "icchā"},
           note="धातोः कर्मणः समानकर्तृकादिच्छायां वा — and this सन् is "
                "आर्धधातुक where 3.1.5's is not, धातोरिति विधानात्."),
    ),
    "3.1.8": (
        _c("putrīyati", {"base": "putra", "is_root": False,
                         "sense": "icchā"},
           note="सुप आत्मनः क्यच् — the base is a finished word from here."),
    ),
    "3.1.9": (
        _c("putrakāmyati", {"base": "putra", "is_root": False,
                            "sense": "icchā", "affix": "kāmyac"},
           note="काम्यच्च, and योगविभाग उत्तरत्र क्यचोऽनुवृत्त्यर्थः."),
    ),
    "3.1.10": (
        _c("putrīyati chātram", {"base": "putra", "is_root": False,
                                 "sense": "ācāra", "upamana": "karman"},
           note="उपमानादाचारे — the thing compared is the OBJECT."),
    ),
    "3.1.11": (
        _c("śyenāyate", {"base": "śyena", "is_root": False,
                         "sense": "ācāra", "upamana": "kartṛ"},
           note="कर्तुः क्यङ् सलोपश्च — the comparison with the AGENT, "
                "and अन्वाचयशिष्टः सलोपः."),
    ),
    "3.1.12": (
        _c("śīghrāyate", {"base": "śīghra", "is_root": False,
                          "sense": "bhū"},
           note="भृशादिभ्यो भुव्यच्वेर्लोपश्च हलः, अभूततद्भावविषये."),
    ),
    "3.1.13": (
        _c("lohitāyati", {"base": "lohita", "is_root": False,
                          "sense": "bhū"},
           note="लोहितादिडाज्भ्यः क्यष् — and the vārttika divides the "
                "two affixes by the lists themselves."),
    ),
    "3.1.14": (
        _c("kaṣṭāyate", {"base": "kaṣṭa", "is_root": False,
                         "sense": "kramaṇa"},
           note="कष्टाय क्रमणे, and अत्यल्पमिदमुच्यते."),
    ),
    "3.1.15": (
        _c("romanthāyate gauḥ", {"base": "romantha", "is_root": False,
                                 "sense": "varti-cara"},
           note="कर्मणो रोमन्थतपोभ्यां वर्तिचरोः, यथाक्रमम्."),
    ),
    "3.1.16": (
        _c("bāṣpāyate", {"base": "bāṣpa", "is_root": False,
                         "sense": "udvamana"},
           note="बाष्पोष्मभ्यामुद्वमने."),
    ),
    "3.1.17": (
        _c("śabdāyate", {"base": "śabda", "is_root": False,
                         "sense": "karaṇa"},
           note="शब्दवैरकलहाभ्रकण्वमेघेभ्यः करणे."),
    ),
    "3.1.18": (
        _c("sukhāyate", {"base": "sukha", "is_root": False,
                         "sense": "kartṛvedanā"},
           note="सुखादिभ्यः कर्तृवेदनायाम् — the feeling must be the "
                "feeler's own."),
    ),
    "3.1.19": (
        _c("namasyati devān", {"base": "namas", "is_root": False,
                               "sense": "karaṇa"},
           note="नमोवरिवश्चित्रङः क्यच् — three words, three senses, and "
                "the ङ् on the third alone."),
    ),
    "3.1.20": (
        _c("saṃcīvarayate bhikṣuḥ", {"base": "cīvara", "is_root": False,
                                     "sense": "karaṇa"},
           note="पुच्छभाण्डचीवरात् णिङ् — two marks, two jobs."),
    ),
    "3.1.21": (
        _c("muṇḍayati", {"base": "muṇḍa", "is_root": False,
                         "sense": "karaṇa"},
           note="मुण्डमिश्र… णिच्, and हलिकल्योरदन्तत्वनिपातनं "
                "सन्वद्भावप्रतिषेधार्थम्."),
    ),
    "3.1.23": (
        _c("caṅkramyate", {"base": "kram", "sense": "kauṭilya"},
           note="नित्यं कौटिल्ये गतौ — and नित्यग्रहणं विषयनियमार्थम्, "
                "narrowing the ground rather than removing an option."),
    ),
    "3.1.24": (
        _c("lolupyate", {"base": "lup", "sense": "bhāvagarhā"},
           note="लुपसदचरजपजभदहदशगॄभ्यो भावगर्हायाम् — the ACT blamed, "
                "not the agent."),
    ),
    "3.1.25": (
        _c("satyāpayati — one of the thirteen",
           {"base": "satya", "is_root": False},
           note="सत्यापपाश… णिच्, the named stems."),
        _c("corayati — the tenth class", {"base": "cur"},
           note="…चुरादिभ्यो णिच् — the other base the same sūtra names, "
                "read from the dhātupāṭha by its class code."),
    ),
    "3.1.26": (
        _c("odanaṃ pācayati", {"base": "pac", "sense": "hetumat"},
           note="हेतुमति च — what the affix means is the prompting, not "
                "the prompter."),
    ),
    "3.1.27": (
        _c("kaṇḍūyati", {"base": "kaṇḍūñ"},
           note="कण्ड्वादिभ्यो यक् — and धात्वधिकाराद् धातुभ्य एव, the "
                "rule's position settling which half of the list is "
                "meant."),
    ),
    "3.1.28": (
        _c("gopāyati", {"base": "gupū"},
           note="गुपूधूपविच्छिपणिपनिभ्य आयः, and पण् taken in the sense "
                "of praise स्तुत्यर्थेन पनिना साहचर्यात्."),
    ),
    "3.1.29": (
        _c("ṛtīyate", {"base": "ṛti"},
           note="ऋतेरीयङ् — written where it was not needed, and the "
                "vṛtti reads that as a ज्ञापन."),
    ),
    "3.1.30": (
        _c("kāmayate", {"base": "kam"},
           note="कमेर्णिङ् — णकारो वृद्ध्यर्थः, ङकार आत्मनेपदार्थः."),
    ),
    "3.1.31": (
        _c("goptā, beside gopāyitā",
           {"affix": "āya", "ardhadhatuka": True},
           note="आयादय आर्धधातुके वा — what is made optional is the "
                "ADDING of the affix."),
        _c("elsewhere it is obligatory", {"affix": "āya"},
           kind="counter",
           note="The rule holds before an आर्धधातुक only."),
    ),
    "2.4.1": (
        _c("pañcapūlī — five bundles as one",
           {"c.samasa": "DVIGU", "c.given": "samāhāra"},
           note="द्विगुरेकवचनम्, and एकवचन in its own sense — that which "
                "speaks of one."),
        _c("a dvigu that is not a collection",
           {"c.samasa": "DVIGU"}, kind="counter",
           note="समाहारद्विगोश्चेदं ग्रहणम्, नान्यस्य."),
    ),
    "2.4.2": (
        _c("pāṇipādam — hand-and-foot", {"c.anga_of": "prāṇin"},
           note="द्वन्द्वश्च प्राणितूर्यसेनाङ्गानाम्, the first of three."),
        _c("mārdaṅgikapāṇavikam — drum-parts",
           {"c.anga_of": "tūrya"},
           note="The second sentence of the three the vṛtti divides it "
                "into."),
    ),
    "2.4.3": (
        _c("udagāt kaṭhakālāpam",
           {"c.people": "caraṇa",
            "c.given": "anuvāda, aorist-sthā-iṇ"},
           note="अनुवादे चरणानाम्, with the vārttika's two roots."),
        _c("said for the first time", {"c.people": "caraṇa"},
           kind="counter",
           note="अनुवाद इति किम्? उदगुः कठकालापाः."),
    ),
    "2.4.4": (
        _c("arkāśvamedham",
           {"c.names": "kratu", "c.given": "anapuṃsaka"},
           note="अध्वर्युक्रतुरनपुंसकम्."),
        _c("rājasūyavājapeye — neuter rite-names",
           {"c.names": "kratu"}, kind="counter",
           note="अनपुंसकमिति किम्?"),
    ),
    "2.4.5": (
        _c("padakakramakam", {"c.given": "adhyayana-āsanna"},
           note="अध्ययनतोऽविप्रकृष्टाख्यानाम्."),
    ),
    "2.4.6": (
        _c("ārāśastri — awls and knives", {"c.jati_of": "dravya"},
           note="जातिरप्राणिनाम्, and only a द्रव्यजाति."),
        _c("rūparasagandhasparśāḥ — a class of QUALITIES",
           {"c.jati_of": "guṇa"}, kind="counter",
           note="न गुणक्रियाजातीनाम्, by नञिवयुक्तन्याय."),
        _c("brāhmaṇakṣatriyaviṭśūdrāḥ — living things",
           {"c.jati_of": "dravya", "c.given": "prāṇin"}, kind="counter",
           note="अप्राणिनामिति किम्?"),
    ),
    "2.4.7": (
        _c("gaṅgāśoṇam", {"c.names": "nadī", "c.given": "viśiṣṭaliṅga"},
           note="विशिष्टलिङ्गो नदी देशोऽग्रामाः."),
        _c("gaṅgāyamune — one gender between them",
           {"c.names": "nadī"}, kind="counter",
           note="विशिष्टलिङ्ग इति किम्?"),
        _c("a village among them",
           {"c.names": "deśa", "c.given": "viśiṣṭaliṅga, grāma"},
           kind="counter", note="अग्रामाः — जाम्बवशालूकिन्यौ."),
    ),
    "2.4.8": (
        _c("daṃśamaśakam", {"c.given": "kṣudra-jantu"},
           note="क्षुद्रजन्तवः, आ नकुलादपि."),
    ),
    "2.4.9": (
        _c("ahinakulam", {"c.given": "śāśvatika-virodha"},
           note="येषां च विरोधः शाश्वतिकः."),
        _c("aśvamahiṣam — enemies, so no choice",
           {"c.group": "paśu", "c.given": "śāśvatika-virodha"},
           note="The च at work: 2.4.12 would have offered पशु a choice, "
                "and this shuts it — तेन पशुशकुनिद्वन्द्वे विरोधिनाम् "
                "अनेन नित्यम् एकवद्भावो भवति."),
    ),
    "2.4.10": (
        _c("takṣāyaskāram", {"c.people": "śūdra"},
           note="शूद्राणामनिरवसितानाम्."),
        _c("caṇḍālamṛtapāḥ",
           {"c.people": "śūdra", "c.given": "niravasita"},
           kind="counter", note="अनिरवसितानामिति किम्?"),
    ),
    "2.4.11": (
        _c("gavāśvam", {"c.form": "gavāśvam"},
           note="गवाश्वप्रभृतीनि च, यथोच्चारितं द्वन्द्ववृत्तम् — the form "
                "as given, from the gaṇapāṭha on disk."),
    ),
    "2.4.12": (
        _c("plakṣanyagrodham, beside plakṣanyagrodhāḥ",
           {"c.group": "vṛkṣa"},
           note="विभाषा, and वृक्ष is not one of the eight the vārttika "
                "holds to more than two."),
        _c("badarāmalake — only two, so no option",
           {"c.group": "phala", "c.member_count": 2}, kind="counter",
           note="बहुप्रकृतिः …, न द्विप्रकृतिः."),
    ),
    "2.4.13": (
        _c("śītoṣṇam, beside śītoṣṇe", {"c.given": "vipratiṣiddha"},
           note="विप्रतिषिद्धं चानधिकरणवाचि, and the च drags 2.4.12's "
                "option down."),
        _c("śītoṣṇe udake — the water, not the qualities",
           {"c.given": "vipratiṣiddha, adhikaraṇa-vācin"},
           kind="counter", note="अनधिकरणवाचीति किम्?"),
    ),
    "2.4.14": (
        _c("vāṅmanase — kept out", {"c.form": "vāṅmanase"},
           note="न दधिपयआदीनि. Refusing IS this rule acting, so it "
                "reports itself."),
    ),
    "2.4.15": (
        _c("daśa dantoṣṭhāḥ — the locus counted",
           {"c.given": "etāvattva"},
           note="अधिकरणैतावत्त्वे च, the second प्रतिषेध."),
    ),
    "2.4.16": (
        _c("upadaśaṃ dantoṣṭham",
           {"c.given": "etāvattva, samīpa"},
           note="विभाषा समीपे — read BEFORE the prohibition it answers, "
                "or the prohibition would swallow it."),
    ),
    "2.4.17": (
        _c("pañcagavam — neuter because it counts as one",
           {"c.samasa": "DVIGU", "c.given": "samāhāra"},
           note="स नपुंसकम्. The rule asks 2.4.1 to 2.4.16 rather than "
                "restating them — स has no content but the back-"
                "reference."),
    ),
    "2.4.18": (
        _c("upakumāri", {"c.samasa": "AVYAYIBHAVA"},
           note="अव्ययीभावश्च — needed because such a compound would "
                "otherwise have had no gender at all."),
    ),
    "2.4.19": (
        # A heading confers nothing itself, so its worked input is a
        # compound it GOVERNS, which then fires a rule inside its range.
        _c("brāhmaṇasenam — inside the heading's range",
           {"c.samasa": "TATPURUSA", "c.ends_in": "senā"},
           note="तत्पुरुषोऽनञ् कर्मधारयः is an अधिकार over 2.4.20 to "
                "2.4.25, so what it governs answers under one of those "
                "— here 2.4.25's विभाषा."),
        _c("paramasenā — a karmadhāraya, so left out",
           {"c.samasa": "TATPURUSA", "c.ends_in": "senā",
            "c.given": "samānādhikaraṇa"}, kind="counter",
           note="अकर्मधारय इति किम्? And कर्मधारय is fetched from 1.2.42 "
                "rather than restated."),
        _c("asenā — a nañ compound, so left out",
           {"c.samasa": "TATPURUSA", "c.ends_in": "senā",
            "c.given": "nañ"}, kind="counter",
           note="अनञिति किम्? The other of the two the heading excludes."),
    ),
    "2.4.20": (
        _c("sauśamikantham",
           {"c.samasa": "TATPURUSA", "c.ends_in": "kanthā",
            "c.given": "saṃjñā, uśīnara"},
           note="संज्ञायां कन्थोशीनरेषु, परवल्लिङ्गतापवाद."),
        _c("vīraṇakanthā — no name",
           {"c.samasa": "TATPURUSA", "c.ends_in": "kanthā"},
           kind="counter", note="संज्ञायामिति किम्?"),
    ),
    "2.4.21": (
        _c("pāṇinyupajñam",
           {"c.samasa": "TATPURUSA", "c.ends_in": "upajñā",
            "c.given": "ācikhyāsā"},
           note="उपज्ञोपक्रमं तदाद्याचिख्यासायाम्."),
        _c("devadattopajño rathaḥ",
           {"c.samasa": "TATPURUSA", "c.ends_in": "upajñā"},
           kind="counter", note="तदाद्याचिख्यासायामिति किम्?"),
    ),
    "2.4.22": (
        _c("śalabhacchāyam",
           {"c.samasa": "TATPURUSA", "c.ends_in": "chāyā",
            "c.given": "bāhulya"},
           note="छाया बाहुल्ये, नित्यार्थमिदं वचनम् — obligatory where "
                "2.4.25 would have left a choice."),
    ),
    "2.4.23": (
        _c("īśvarasabham",
           {"c.samasa": "TATPURUSA", "c.ends_in": "sabhā",
            "c.given": "rājan-pūrva"},
           note="सभा राजामनुष्यपूर्वा, and only SYNONYMS of राजन् — "
                "पर्यायवचनस्यैवेष्यते."),
    ),
    "2.4.24": (
        _c("dāsīsabham — a company, not a hall",
           {"c.samasa": "TATPURUSA", "c.ends_in": "sabhā",
            "c.given": "aśālā"},
           note="अशाला च, सङ्घातवचनोऽत्र सभाशब्दो गृह्यते."),
    ),
    "2.4.25": (
        _c("gośālam, beside gośālā",
           {"c.samasa": "TATPURUSA", "c.ends_in": "śālā"},
           note="विभाषा सेनासुराच्छायाशालानिशानाम्."),
    ),
    "2.4.26": (
        _c("ardhapippalī — the gender of the LAST member",
           {"c.samasa": "TATPURUSA"},
           note="परवल्लिङ्गं द्वन्द्वतत्पुरुषयोः. It names a member, not "
                "a gender, so the answer is a slot."),
        _c("pañcakapālaḥ — a dvigu, which the vārttika excludes",
           {"c.samasa": "TATPURUSA", "c.kind": "dvigu"}, kind="counter",
           note="द्विगुप्राप्तापन्नालंपूर्वगतिसमासेषु प्रतिषेधो वक्तव्यः."),
    ),
    "2.4.27": (
        _c("aśvavaḍavau — the FIRST member's gender",
           {"c.form": "aśvavaḍavau"},
           note="पूर्ववदश्ववडवौ, अर्थातिदेशश्चायम् न निपातनम्."),
    ),
    "2.4.28": (
        _c("hemantaśiśirau, in the Veda",
           {"c.form": "hemantaśiśirau", "c.given": "chandas"},
           note="Codified from the Nyāsa, Padamañjarī and "
                "Siddhāntakaumudī: the Kāśikā on disk for this sūtra is "
                "another rule's text."),
        _c("ahorātre — overriding 2.4.29 instead",
           {"c.form": "ahorātre", "c.given": "chandas"},
           note="पुंल्लिङ्गत्वापवाद, छन्दसि लिङ्गव्यत्ययः by 3.1.85."),
    ),
    "2.4.29": (
        _c("dvirātraḥ", {"c.ends_in": "rātra"},
           note="रात्राह्नाहाः पुंसि, कृतसमासान्तानां निर्देशः."),
    ),
    "2.4.30": (
        _c("apatham", {"c.form": "apatha"},
           note="अपथं नपुंसकम्, with तत्पुरुष इति वर्तते from 2.4.19."),
    ),
    "2.4.31": (
        _c("gomayaḥ and gomayam both stand", {"c.form": "gomaya"},
           note="अर्धर्चाः पुंसि च — both genders, so the answer carries "
                "`also`. Read from the gaṇapāṭha on disk."),
    ),
    "2.4.72": (
        _c("इण् (iṇ) — a second-gaṇa root", {"root": "iṇ"},
           note="अदिप्रभृतिभ्यः शपः — एति, with no अ."),
        _c("अद् (ada̐) — also second gaṇa", {"root": "ada̐"},
           note="अत्ति."),
        _c("भू (bhū) — first gaṇa, so शप् stands", {"root": "bhū"},
           note="भवति keeps its अ."),
    ),
    "8.4.55": (
        _c("द् (d) before ति (ti) → त् (t)",
           {"sound": "d", "following": "ti"}, note="अत्ति."),
        _c("न् (n) before ति (ti) — a nasal is not झल्",
           {"sound": "n", "following": "ti"},
           note="झलाम् — हन्ति keeps its न्."),
        _c("द् (d) before न (na) — न् is not खर्",
           {"sound": "d", "following": "na"}, note="खरि — the condition."),
    ),
}


def _shape(text: str) -> str:
    """Neither script alone — the same two conventions the glosses use."""
    from src.astadhyayi.glosses import (
        add_devanagari, bracket_iast, pair_bare_devanagari)

    return pair_bare_devanagari(add_devanagari(bracket_iast(text)))


def cases_for(sutra_id: str) -> Tuple[Case, ...]:
    """
    The ready-made inputs for one sūtra's playground.

    Derived ones first, then anything written by hand. A sūtra with neither
    gets an empty tuple, and the UI then shows the form bare — which is
    honest, but the coverage test treats it as a gap.
    """
    found = tuple(_derived(sutra_id)) + CURATED.get(sutra_id, ())
    # The same convention the glosses use — a case label is read by the same
    # person in the same panel, and देवनागरी (iast) there and देवनागरी iast
    # here would be one interface with two habits.
    return tuple(
        Case(_shape(case.label), case.values, case.kind,
             _shape(case.note))
        for case in found
    )


def coverage() -> Tuple[Tuple[str, ...], Tuple[str, ...]]:
    """Which registered sūtras have a worked input, and which do not."""
    from src.astadhyayi.sutra import REGISTRY

    have, missing = [], []
    for sutra in REGISTRY.all():
        (have if cases_for(str(sutra.id)) else missing).append(str(sutra.id))
    return tuple(have), tuple(missing)


__all__ = ["CURATED", "Case", "cases_for", "coverage"]
