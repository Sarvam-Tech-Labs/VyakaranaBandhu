# -*- coding: utf-8 -*-
"""
Reads the local reference texts in reference/ and makes them addressable by
sūtra id.

Three things live here:

* **SLP1 → IAST**, because Vidyut's sūtrapāṭha is SLP1 encoded.
* **Parsers** for each source's own format.
* **Collation** — the two independent editions of the sūtrapāṭha (GRETIL, from
  Aryendra Sharma's Kāśikā; Vidyut's TSV) are compared against each other.
  Where they agree, the text is corroborated by two witnesses and can be
  recorded VERIFIED; where they differ, the difference is reported rather than
  one being silently preferred.

Nothing here interprets a sūtra. It locates and quotes.
"""

from __future__ import annotations

import os
import unicodedata
from functools import lru_cache
import re
from dataclasses import dataclass, field
from typing import Dict, FrozenSet, List, Optional, Tuple

REFERENCE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
    "reference",
)


class CorpusUnavailable(FileNotFoundError):
    """A reference file is missing — run tools/fetch_reference.py."""


# --- SLP1 -----------------------------------------------------------------

#: SLP1 is a one-byte-per-phoneme ASCII encoding; each key maps to one IAST
#: sound. Order matters only in that every code point is a single character.
_SLP1_TO_IAST: Dict[str, str] = {
    "a": "a", "A": "ā", "i": "i", "I": "ī", "u": "u", "U": "ū",
    "f": "ṛ", "F": "ṝ", "x": "ḷ", "X": "ḹ",
    "e": "e", "E": "ai", "o": "o", "O": "au",
    "M": "ṃ", "H": "ḥ", "~": "m̐",
    "k": "k", "K": "kh", "g": "g", "G": "gh", "N": "ṅ",
    "c": "c", "C": "ch", "j": "j", "J": "jh", "Y": "ñ",
    "w": "ṭ", "W": "ṭh", "q": "ḍ", "Q": "ḍh", "R": "ṇ",
    "t": "t", "T": "th", "d": "d", "D": "dh", "n": "n",
    "p": "p", "P": "ph", "b": "b", "B": "bh", "m": "m",
    "y": "y", "r": "r", "l": "l", "v": "v",
    "S": "ś", "z": "ṣ", "s": "s", "h": "h",
    "L": "ḻ",
    "'": "’",
}


def slp1_to_iast(text: str) -> str:
    """Converts SLP1 to IAST. Unmapped characters (space, punctuation) pass through."""
    return "".join(_SLP1_TO_IAST.get(ch, ch) for ch in text)


# --- records ---------------------------------------------------------------


@dataclass(frozen=True)
class SutraText:
    """One sūtra as one edition gives it."""

    id: str
    text: str
    #: Word-split, where the edition marks it (GRETIL hyphenates).
    padaccheda: Tuple[str, ...] = ()
    edition: str = ""


@dataclass(frozen=True)
class BhasyaSegment:
    """One numbered segment of the Mahābhāṣya on a sūtra."""

    sutra_id: str
    segment: str          # e.g. "3/13"
    #: Kielhorn volume, page and lines — the citable locator, and the one the
    #: BORI (Abhyankar) revision follows.
    kielhorn: str
    text: str

    @property
    def locator(self) -> str:
        return f"Mahābhāṣya on {self.sutra_id}, Kielhorn {self.kielhorn} [{self.segment}]"


@dataclass
class Collation:
    """How the independent editions compare on one sūtra."""

    id: str
    witnesses: Dict[str, str] = field(default_factory=dict)

    @property
    def agree(self) -> bool:
        """True when every witness gives the same text once normalized."""
        forms = {_normalize(t) for t in self.witnesses.values()}
        return len(forms) == 1

    @property
    def corroborated(self) -> bool:
        """Two or more witnesses, all agreeing."""
        return len(self.witnesses) > 1 and self.agree

    def classify(self) -> str:
        """
        What kind of difference, if any, separates the witnesses:

        ``identical``   the same string once hyphens and spacing are removed
        ``sandhi``      one edition gives pre-sandhi words, the other the
                        sandhied text — the same wording, presented differently
        ``orthographic`` differing only in how a nasal is written
        ``divergent``   a real difference in wording; needs a human eye
        ``single``      only one witness has this sūtra
        """
        if len(self.witnesses) < 2:
            return "single"
        readings = list(self.witnesses.values())
        forms = [_normalize(t) for t in readings]
        if len(set(forms)) == 1:
            return "identical"

        # Sandhi test, pairwise and crossed: does ONE witness, read as
        # pre-sandhi parts and joined, reproduce ANOTHER witness's text?
        # Comparing a witness's joined form against its own proves nothing.
        # Both join strategies are tried, since editions differ on where the
        # spaces fall.
        candidates = [
            {_normalize(_sandhied(t)), _normalize(_sandhied_throughout(t))}
            for t in readings
        ]
        for i in range(len(readings)):
            for j in range(len(readings)):
                if i != j and forms[j] in candidates[i]:
                    return "sandhi"

        if len({_nasal_insensitive(f) for f in forms}) == 1:
            return "orthographic"
        for i in range(len(readings)):
            for j in range(len(readings)):
                if i == j:
                    continue
                if _nasal_insensitive(forms[j]) in {
                    _nasal_insensitive(c) for c in candidates[i]
                }:
                    return "sandhi"
        return "divergent"


def _normalize(text: str) -> str:
    """
    Strips what editions differ on without touching what they say: word-split
    hyphens, sandhi plus-signs, spacing, avagraha shape, and how a letter is
    ENCODED.

    The last of those is not a scribal choice but a Unicode one. GRETIL writes
    ṝ as ṛ plus a combining macron (U+1E5B U+0304); Vidyut uses the
    precomposed ṝ (U+1E5D). Composed under NFC they are one letter, and
    without that three sūtras — 3.3.30, 7.2.38, 8.3.10 — were reported as
    divergent witnesses to texts that agree exactly. A collation that warns
    about agreement is worse than none, because the warnings that matter stop
    being read.
    """
    out = unicodedata.normalize("NFC", text)
    out = out.replace("-", "").replace("+", "")
    out = out.replace("’", "'").replace("ʼ", "'")
    out = re.sub(r"\s+", "", out)
    return out.strip().lower()


# Vowel sandhi at a word join, enough to test whether an unsandhied reading and
# a sandhied one are the same text. Longest first so ā matches before a.
_GUNA_JOIN = {
    ("a", "a"): "ā", ("a", "ā"): "ā", ("ā", "a"): "ā", ("ā", "ā"): "ā",
    ("a", "i"): "e", ("a", "ī"): "e", ("ā", "i"): "e", ("ā", "ī"): "e",
    ("a", "u"): "o", ("a", "ū"): "o", ("ā", "u"): "o", ("ā", "ū"): "o",
    ("a", "ṛ"): "ar", ("ā", "ṛ"): "ar",
    ("a", "e"): "ai", ("ā", "e"): "ai", ("a", "ai"): "ai",
    ("a", "o"): "au", ("ā", "o"): "au", ("a", "au"): "au",
    ("i", "i"): "ī", ("i", "ī"): "ī", ("ī", "i"): "ī", ("ī", "ī"): "ī",
    ("u", "u"): "ū", ("u", "ū"): "ū", ("ū", "u"): "ū", ("ū", "ū"): "ū",
}
_YAN_JOIN = {"i": "y", "ī": "y", "u": "v", "ū": "v", "ṛ": "r"}
#: ayādi (6.1.78 ecoyavāyāvaḥ): a diphthong before a vowel becomes ay/av/āy/āv.
_AYADI_JOIN = {"e": "ay", "o": "av", "ai": "āy", "au": "āv"}


def _ends_with_vowel(word: str) -> Optional[str]:
    for vowel in ("ai", "au", "ā", "ī", "ū", "ṛ", "a", "i", "u", "e", "o"):
        if word.endswith(vowel):
            return vowel
    return None


def _starts_with_vowel(word: str) -> Optional[str]:
    for vowel in ("ai", "au", "ā", "ī", "ū", "ṛ", "a", "i", "u", "e", "o"):
        if word.startswith(vowel):
            return vowel
    return None


def _join_parts(words: Tuple[str, ...]) -> str:
    """Joins pre-sandhi parts of ONE word the way the sandhied text reads it."""
    if not words:
        return ""
    joined = words[0]
    for nxt in words[1:]:
        left = _ends_with_vowel(joined)
        right = _starts_with_vowel(nxt)
        if left and right:
            merged = _GUNA_JOIN.get((left, right))
            if merged is not None:
                joined = joined[: -len(left)] + merged + nxt[len(right):]
                continue
            if left in _AYADI_JOIN:
                joined = joined[: -len(left)] + _AYADI_JOIN[left] + nxt
                continue
            if left in _YAN_JOIN and right != left:
                joined = joined[: -len(left)] + _YAN_JOIN[left] + nxt
                continue
        joined += nxt
    return joined


def _sandhied(text: str) -> str:
    """
    Renders an edition's reading as the continuous text would run.

    Hyphens mark joins inside a word and are resolved; spaces are word gaps and
    are kept, because an edition that writes a space there has not applied
    sandhi across it. (Editions still differ on where they put the space —
    which is why the comparison below also tries joining across spaces.)
    """
    return " ".join(
        _join_parts(tuple(p for p in token.split("-") if p))
        for token in text.split()
        if token
    )


def _sandhied_throughout(text: str) -> str:
    """As `_sandhied`, but joining across the spaces too — for editions that
    write the whole sūtra as one sandhied run."""
    return _join_parts(tuple(p for p in re.split(r"[\s-]+", text) if p))


#: Anusvāra is written variously (ṃ, ṁ, m̐) and editions differ on whether a
#: nasal before a stop is left homorganic (saṅkhyā) or written as anusvāra
#: (saṃkhyā). Neither is a difference in the text.
_NASALS = str.maketrans({"ṁ": "ṃ", "ṅ": "ṃ", "ñ": "ṃ", "ṇ": "ṃ", "n": "ṃ", "m": "ṃ"})


def _nasal_insensitive(text: str) -> str:
    return text.replace("m̐", "ṃ").translate(_NASALS)


# --- parsers ---------------------------------------------------------------

_GRETIL_SUTRA = re.compile(r"(.+?)\s*\|\|\s*ps_(\d),(\d)\.(\d+)\s*\|\|")


def _read(path: str) -> str:
    full = os.path.join(REFERENCE, path)
    if not os.path.exists(full):
        raise CorpusUnavailable(
            f"{path} is not in reference/. Run:  python tools/fetch_reference.py"
        )
    with open(full, encoding="utf-8", errors="replace") as handle:
        return handle.read()


#: Cached, and it matters more than it looks. `sources.readings_for` calls
#: these once for every sūtra it assembles an apparatus for, and
#: load_mahabhasya alone takes about a second. Without the cache,
#: importing the rules package re-read the Mahābhāṣya once per registered
#: sūtra and took a minute and a half.
@lru_cache(maxsize=None)
def load_gretil_sutrapatha() -> Dict[str, SutraText]:
    """
    GRETIL's Aṣṭādhyāyī, extracted from the Kāśikāvṛtti (Aryendra Sharma ed.).

    Its text carries hyphens at word joins, which give a padaccheda for free —
    `vṛddhir ād-aic` splits as vṛddhir / ād / aic.
    """
    raw = _read("mula/astadhyayi/gretil-astadhyayi.txt")
    body = raw.split("# Text", 1)[-1]
    out: Dict[str, SutraText] = {}
    for match in _GRETIL_SUTRA.finditer(body):
        text = match.group(1).strip()
        # Drop any leading junk carried over from the previous match.
        text = text.split("||")[-1].strip()
        sutra_id = f"{match.group(2)}.{match.group(3)}.{match.group(4)}"
        words = tuple(w for w in re.split(r"[\s-]+", text) if w)
        out[sutra_id] = SutraText(
            id=sutra_id, text=text, padaccheda=words, edition="GRETIL / Kāśikā (A. Sharma)"
        )
    return out


@lru_cache(maxsize=None)
def load_vidyut_sutrapatha() -> Dict[str, SutraText]:
    """Vidyut's machine-readable sūtrapāṭha, converted from SLP1 to IAST."""
    raw = _read("mula/astadhyayi/vidyut-sutrapatha.tsv")
    out: Dict[str, SutraText] = {}
    for line in raw.splitlines():
        if not line.strip() or line.startswith("code\t"):
            continue
        parts = line.split("\t")
        if len(parts) < 2:
            continue
        sutra_id, text = parts[0].strip(), slp1_to_iast(parts[1].strip())
        out[sutra_id] = SutraText(id=sutra_id, text=text, edition="Ambuda / vidyut-prakriya")
    return out


# The file marks a passage two ways — (p_A,P.S) and (p_A,P.S.n), the latter
# adding a subsection index. Both must be read, or two thirds of the bhāṣya is
# invisible. The Kielhorn locator that follows is the citable reference.
_BHASYA = re.compile(
    r"\(p_(\d),(\d)\.(\d+)(?:\.(\d+))?\)\s+"
    r"ka_([ivx]+),([\d.\-]+)\s+\S+\s+\{(\d+/\d+)\}\s*"
    r"(.*?)(?=\(p_|\Z)",
    re.S,
)


@lru_cache(maxsize=None)
def load_mahabhasya() -> Dict[str, List[BhasyaSegment]]:
    """
    Patañjali's Mahābhāṣya, indexed by the sūtra it comments on.

    Each segment keeps its Kielhorn volume/page/line reference. Note that
    GRETIL's own sūtra segmentation is editorial: when quoting, check that the
    segment really belongs to the sūtra it is filed under.
    """
    raw = _read("mula/mahabhasya/gretil-mahabhasya.txt")
    out: Dict[str, List[BhasyaSegment]] = {}
    for m in _BHASYA.finditer(raw):
        sutra_id = f"{m.group(1)}.{m.group(2)}.{m.group(3)}"
        segment = BhasyaSegment(
            sutra_id=sutra_id,
            segment=m.group(7),
            kielhorn=f"vol. {m.group(5).upper()}, {m.group(6)}",
            text=re.sub(r"\s+", " ", m.group(8)).strip(),
        )
        out.setdefault(sutra_id, []).append(segment)
    return out


def bhasya_on(sutra_id: str) -> List[BhasyaSegment]:
    """The Mahābhāṣya passages filed under one sūtra, in order."""
    return load_mahabhasya().get(sutra_id, [])


# --- collation -------------------------------------------------------------


@lru_cache(maxsize=None)
def collate() -> Dict[str, Collation]:
    """Every sūtra, with each edition's reading side by side."""
    editions = {
        "gretil": load_gretil_sutrapatha(),
        "vidyut": load_vidyut_sutrapatha(),
    }
    ids = sorted(
        {i for texts in editions.values() for i in texts},
        key=lambda i: tuple(int(p) for p in i.split(".")),
    )
    out: Dict[str, Collation] = {}
    for sutra_id in ids:
        collation = Collation(id=sutra_id)
        for name, texts in editions.items():
            if sutra_id in texts:
                collation.witnesses[name] = texts[sutra_id].text
        out[sutra_id] = collation
    return out


def collation_report() -> Dict[str, object]:
    """
    How far the two editions corroborate one another, split by the kind of
    difference. Only `divergent` needs human adjudication; the rest are the
    same text presented differently.
    """
    all_collations = collate()
    buckets: Dict[str, List[str]] = {}
    for collation in all_collations.values():
        buckets.setdefault(collation.classify(), []).append(collation.id)
    return {
        "total_ids": len(all_collations),
        "counts": {k: len(v) for k, v in sorted(buckets.items())},
        "divergent": buckets.get("divergent", []),
        "single_witness": buckets.get("single", []),
    }


# --- the commentary layer --------------------------------------------------

#: ashtadhyayi.com keys every commentary by a five-digit code: adhyāya, pāda,
#: then the sūtra number padded to three digits. 1.1.1 -> "11001".
def commentary_key(sutra_id: str) -> str:
    adhyaya, pada, number = sutra_id.split(".")
    return f"{adhyaya}{pada}{int(number):03d}"


#: filename -> how to cite it.
COMMENTARIES: Dict[str, str] = {
    "kashika": "Kāśikāvṛtti (Vāmana & Jayāditya)",
    "nyaas": "Nyāsa (Jinendrabuddhi)",
    "padamanjari": "Padamañjarī (Haradatta)",
    "bhashya": "Mahābhāṣya (Patañjali)",
    "vartika": "Vārttikas (Kātyāyana)",
    "kaumudi": "Siddhāntakaumudī (Bhaṭṭoji Dīkṣita)",
    "laghukaumudi": "Laghusiddhāntakaumudī (Varadarāja)",
    "balamanorama": "Bālamanoramā",
    "tattvabodhini": "Tattvabodhinī",
    "praudhamanorama": "Prauḍhamanoramā",
    "laghushabdendushekhar": "Laghuśabdenduśekhara (Nāgeśa)",
    "vasu_english": "Ś. C. Vasu, English translation",
    "sutrartha_english": "Sūtrārtha (English)",
    "sutra_prayogas": "Attested usages",
    "data": "Core sūtra data",
}

_COMMENTARY_CACHE: Dict[str, Dict[str, object]] = {}


def load_commentary(name: str) -> Dict[str, object]:
    """Loads one commentary file, keyed by five-digit sūtra code."""
    import json

    if name not in COMMENTARIES:
        raise KeyError(f"{name!r} is not one of: {', '.join(sorted(COMMENTARIES))}")
    if name not in _COMMENTARY_CACHE:
        _COMMENTARY_CACHE[name] = json.loads(_read(f"commentary/{name}.json"))
    return _COMMENTARY_CACHE[name]


def commentary_on(sutra_id: str, name: str) -> Optional[str]:
    """One commentary's text on one sūtra, or None where it is silent."""
    entry = load_commentary(name).get(commentary_key(sutra_id))
    if entry is None:
        return None
    if isinstance(entry, str):
        return entry.strip() or None
    return str(entry)


def all_commentary_on(sutra_id: str) -> Dict[str, str]:
    """
    Every commentary that says anything about this sūtra, keyed by its citable
    name. What comes back is the evidence to read before codifying.
    """
    out: Dict[str, str] = {}
    for name, citation in COMMENTARIES.items():
        try:
            text = commentary_on(sutra_id, name)
        except CorpusUnavailable:
            continue
        if text:
            out[citation] = text
    return out


# --- the dhātupāṭha --------------------------------------------------------

#: SLP1 accent marks. In the dhātupāṭha these are not decoration: 1.3.12
#: अनुदात्तङित आत्मनेपदम् makes an anudātta root take ātmanepada endings, so the
#: mark is grammatical information and is kept beside the form rather than
#: dropped into it.
ANUDATTA = "\\"
SVARITA = "^"
_ACCENTS = (ANUDATTA, SVARITA)


@dataclass(frozen=True)
class Dhatu:
    """One root as the dhātupāṭha enunciates it — an upadeśa, it-marks and all."""

    code: str            # "01.0002", gaṇa and serial
    upadesa: str         # IAST, anunāsika vowels carrying a combining candrabindu
    accent: str          # the accent marks found, in order
    artha: str           # the sense given
    #: Where each mark falls, as (index into `upadesa`, mark). Position is not
    #: decoration here: 1.3.12 अनुदात्तङितः asks whether the root's *it* is
    #: anudātta, and the same mark on the root's own vowel says nothing.
    #: आसँ॒ is `Asa~\` — the mark follows the anunāsika it, so आस्ते. विँशँ is
    #: `vi\Sa~` — the mark is on the root vowel और the it is bare, so विशति,
    #: and 1.3.17 has to grant निविशते its ātmanepada separately. Dropping the
    #: position makes those two roots identical.
    accent_positions: Tuple[Tuple[int, str], ...] = ()

    @property
    def gana(self) -> int:
        return int(self.code.split(".")[0])

    @property
    def anudatta(self) -> bool:
        return ANUDATTA in self.accent

    @property
    def svarita(self) -> bool:
        return SVARITA in self.accent


def _dhatu_to_iast(raw: str) -> Tuple[str, str, Tuple[Tuple[int, str], ...]]:
    """
    An SLP1 dhātupāṭha form, as IAST plus its accent marks.

    `~` is handled here rather than by `slp1_to_iast`, and differently. That
    function renders the candrabindu as m̐, which is how the sūtrapāṭha's ऊँ and
    सँ are conventionally written and how the Devanāgarī witness comes out too,
    so the two agree and it should stay. But 1.3.2 asks whether a *vowel* is
    anunāsika, and m̐ reads as a consonant. So in this one place the mark is put
    on the vowel as a combining candrabindu — the same character
    varna.nasalize produces, so varna.is_anunasika can answer the question.
    """
    out: List[str] = []
    marks: List[Tuple[int, str]] = []
    written = 0
    for ch in raw:
        if ch in _ACCENTS:
            # An SLP1 accent follows the syllable it marks, so its position is
            # however much has been written out by the time it is reached.
            marks.append((written, ch))
            continue
        piece = "\u0310" if ch == "~" else _SLP1_TO_IAST.get(ch, ch)
        out.append(piece)
        written += len(piece)
    return "".join(out), "".join(m for _, m in marks), tuple(marks)


@lru_cache(maxsize=None)
def load_dhatupatha() -> Dict[str, Dhatu]:
    """
    Vidyut's dhātupāṭha, ~2,000 roots as enunciated.

    This is upadeśa in the strict sense 1.3.2 means — उपदिश्यतेऽनेनेत्युपदेशः
    शास्त्रवाक्यानि, सूत्रपाठः खिलपाठश्च — so it is where the anunāsika it-marks
    actually live. The Kāśikā's two examples for that sūtra, एध and स्पर्ध, are
    entries 01.0002 and 01.0003 here.
    """
    out: Dict[str, Dhatu] = {}
    for line in _read("mula/ancillary/vidyut-dhatupatha.tsv").splitlines()[1:]:
        parts = line.split("\t")
        if len(parts) < 2 or not parts[0].strip():
            continue
        code, raw = parts[0].strip(), parts[1].strip()
        upadesa, accent, positions = _dhatu_to_iast(raw)
        out[code] = Dhatu(
            code=code,
            upadesa=upadesa,
            accent=accent,
            accent_positions=positions,
            artha=parts[2].strip() if len(parts) > 2 else "",
        )
    return out


def dhatu(code: str) -> Optional[Dhatu]:
    return load_dhatupatha().get(code)


# --- Kātyāyana's vārttikas -------------------------------------------------


@dataclass(frozen=True)
class Varttika:
    """One vārttika, with the sūtra it comments on."""

    sutra_id: str
    text: str


@lru_cache(maxsize=None)
def load_varttikas() -> Dict[str, Tuple[Varttika, ...]]:
    """
    The vārttikas, grouped by the sūtra they attach to.

    Kātyāyana's supplements are not a commentary in the ordinary sense — they
    are corrections and extensions that the tradition treats as almost part of
    the text, and the Mahābhāṣya is largely an examination of them. Several are
    already load-bearing here: the savarṇatva of ṛ and ḷ, cited on 1.1.9, is
    ऋऌवर्णयोर्मिथः सावर्ण्यं वाच्यम्, the first entry in this file.

    Stored differently from the other commentaries: a flat list keyed by sūtra
    id rather than a map from the five-digit code, so it needs its own reader.
    """
    raw = load_commentary("vartika")
    out: Dict[str, list] = {}
    for entry in raw.get("data", []):
        sutra_id = str(entry.get("sutra", "")).strip()
        text = str(entry.get("vartika", "")).strip()
        if sutra_id and text:
            out.setdefault(sutra_id, []).append(Varttika(sutra_id, text))
    return {k: tuple(v) for k, v in out.items()}


def varttikas_on(sutra_id: str) -> Tuple[Varttika, ...]:
    """Kātyāyana on this sūtra, or nothing."""
    return load_varttikas().get(sutra_id, ())


# --- attested usages -------------------------------------------------------


@dataclass(frozen=True)
class Prayoga:
    """A word in a literary text that a sūtra accounts for."""

    sutra_id: str
    word: str
    work: str
    locator: str
    url: str = ""

    def __str__(self) -> str:
        return f"{self.word} ({self.work} {self.locator})"


@lru_cache(maxsize=None)
def load_prayogas() -> Dict[str, Tuple[Prayoga, ...]]:
    """
    Attested forms, by sūtra: 1,712 of them, with work and verse reference.

    This is evidence of a different kind from a commentary. A commentary says
    what a rule means; these say where the rule is actually doing work in
    literature — मृदितकिसलयः in the Kirātārjunīya for 1.1.5, रावणाद् in the
    Bhaṭṭikāvya for 1.1.25. Useful both as worked examples and as a check that a
    codification has not drifted into something no text needs.
    """
    raw = load_commentary("sutra_prayogas")
    out: Dict[str, list] = {}
    dropped: List[str] = []
    for sutra_id, entries in raw.get("data", {}).items():
        sutra_id = str(sutra_id)
        if not _is_wellformed_id(sutra_id):
            dropped.append(f"{sutra_id}: no such sūtra")
            continue
        for entry in entries or ():
            word = str(entry.get("word", "")).strip()
            if not word:
                dropped.append(f"{sutra_id}: entry with no word")
                continue
            out.setdefault(sutra_id, []).append(
                Prayoga(
                    sutra_id=sutra_id,
                    word=word,
                    work=str(entry.get("text", "")),
                    locator=str(entry.get("loc", "")),
                    url=str(entry.get("url", "")),
                )
            )
    PRAYOGA_DROPPED[:] = dropped
    return {k: tuple(v) for k, v in out.items()}


#: What `load_prayogas` refused, and why. Filled on each load. The file has a
#: few flaws of its own — 35 entries name a work and a verse but no word, and
#: two attach to sūtras that do not exist (3.5.35, when no adhyāya has a fifth
#: pāda, and 6.3.161, when 6.3 ends at 139). They are dropped rather than
#: carried, and counted rather than dropped silently.
PRAYOGA_DROPPED: List[str] = []


def _is_wellformed_id(sutra_id: str) -> bool:
    """Four pādas to an adhyāya, eight adhyāyas, and the sūtra must exist."""
    parts = sutra_id.split(".")
    if len(parts) != 3 or not all(p.isdigit() for p in parts):
        return False
    adhyaya, pada, _ = (int(p) for p in parts)
    if not (1 <= adhyaya <= 8 and 1 <= pada <= 4):
        return False
    return sutra_id in _known_sutra_ids()


@lru_cache(maxsize=None)
def _known_sutra_ids() -> FrozenSet[str]:
    global _KNOWN_IDS
    if _KNOWN_IDS is None:
        entries = load_commentary("data").get("data", [])
        _KNOWN_IDS = frozenset(
            f"{e['a']}.{e['p']}.{e['n']}" for e in entries
        )
    return _KNOWN_IDS


_KNOWN_IDS = None


def prayogas_on(sutra_id: str) -> Tuple[Prayoga, ...]:
    """Attested forms this sūtra accounts for."""
    return load_prayogas().get(sutra_id, ())


# --- the gaṇapāṭha ---------------------------------------------------------

_GANA_ENTRY = re.compile(
    r"GanapathaEntry::(basic|akrti)\(\s*"
    r'"([^"]+)"\s*,\s*'          # name, e.g. sarvAdiH
    r"(\d+)\s*,\s*"
    r'"([^"]*)"\s*,\s*'          # the sūtra that first uses it
    r"&\[(.*?)\]\s*,?\s*\)",
    re.DOTALL,
)
_GANA_ITEM = re.compile(r'"([^"]*)"')
_GANA_COMMENT = re.compile(r"//.*?$", re.MULTILINE)


@dataclass(frozen=True)
class UnadiSutra:
    """One sūtra of the उणादिपाठ, keyed as it cites itself: "1.1"."""

    code: str
    text: str

    @property
    def pada(self) -> int:
        return int(self.code.split(".")[0])


@lru_cache(maxsize=None)
def load_unadipatha() -> Dict[str, UnadiSutra]:
    """
    The उणादिपाठ — 748 sūtras in five pādas, converted from SLP1.

    3.3.1 उणादयो बहुलम् licenses these affixes rather than listing
    them; the list is a separate text, and this is it. The Kāśikā
    cites it as प०उ०, and its first citation under 3.3.1 is 1.1
    कृवापाजिमिस्वदिसाध्यशूभ्य उण्, which is this file's first row.
    """
    raw = _read("mula/ancillary/vidyut-unadipatha.tsv")
    out: Dict[str, UnadiSutra] = {}
    for line in raw.splitlines()[1:]:
        if not line.strip():
            continue
        parts = line.split("\t")
        if len(parts) < 2:
            continue
        code, text = parts[0].strip(), parts[1].strip()
        if not code or not text:
            continue
        out[code] = UnadiSutra(code=code, text=slp1_to_iast(text))
    return out


def unadi_sutra(code: str) -> Optional[UnadiSutra]:
    """One उणादि sūtra by its code, e.g. "1.1"."""
    return load_unadipatha().get(code)


@dataclass(frozen=True)
class Gana:
    """
    One list from the Gaṇapāṭha.

    `open_ended` is the tradition's आकृतिगण: a list whose members cannot all be
    enumerated, and which is completed by observing usage. Pāṇini uses both
    kinds and the difference matters — a closed gaṇa can be tested for
    membership and an open one cannot, so a rule that reads one is decidable
    and a rule that reads the other is not.
    """

    name: str            # sarvAdiH, svarAdiH ...
    number: int
    sutra_id: str        # the sūtra that first calls on it
    items: Tuple[str, ...]      # IAST
    slp1: Tuple[str, ...]       # as the file has them
    open_ended: bool

    def __contains__(self, word: str) -> bool:
        return word in self.items or word in self.slp1

    def __len__(self) -> int:
        return len(self.items)


def all_ganas() -> Tuple[Gana, ...]:
    """Every gaṇa in the file, in order — 262 of them."""
    return _parse_ganapatha()


@lru_cache(maxsize=None)
def load_ganapatha() -> Dict[str, Tuple[Gana, ...]]:
    """
    The Gaṇapāṭha — 262 lists, keyed by the sūtra that first uses each.

    Pāṇini refers to a great many word-lists by their first member and a
    suffix: सर्वादि means "sarva and the rest", and 1.1.27 cannot be applied
    without knowing what the rest are. The list is a separate text, and it is
    here, so those sūtras can be codified rather than stubbed.

    The file is Rust — Vidyut's generated source — because that is the form the
    data is published in. Parsing it is worth the small ugliness: the
    alternative is an incomplete list typed by hand.
    """
    out: Dict[str, list] = {}
    for gana in _parse_ganapatha():
        out.setdefault(gana.sutra_id, []).append(gana)
    return {k: tuple(v) for k, v in out.items()}


@lru_cache(maxsize=None)
def _parse_ganapatha() -> Tuple[Gana, ...]:
    raw = _read("mula/ancillary/vidyut-ganapatha.rs")
    out = []
    for kind, name, number, sutra_id, body in _GANA_ENTRY.findall(raw):
        items = tuple(_GANA_ITEM.findall(_GANA_COMMENT.sub("", body)))
        out.append(
            Gana(
                name=slp1_to_iast(name),
                number=int(number),
                sutra_id=sutra_id,
                items=tuple(slp1_to_iast(i) for i in items),
                slp1=items,
                open_ended=(kind == "akrti"),
            )
        )
    return tuple(out)


def ganas_for(sutra_id: str) -> Tuple[Gana, ...]:
    """Every gaṇa a sūtra calls on. A few sūtras call on more than one."""
    return load_ganapatha().get(sutra_id, ())


def gana_for(sutra_id: str) -> Optional[Gana]:
    """The first gaṇa a sūtra calls on, or None."""
    found = ganas_for(sutra_id)
    return found[0] if found else None


def in_gana(word: str, sutra_id: str) -> bool:
    """Whether a word belongs to any gaṇa the sūtra names."""
    return any(word in gana for gana in ganas_for(sutra_id))
