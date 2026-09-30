# -*- coding: utf-8 -*-
"""
८.३.५५–११९ — the स् (and the ध्) that becomes cerebral: ṣatva and ḍhatva.

    रामे + सु → रामेषु      अग्नि + सु → अग्निषु      अभि | सुनोति → अभिषुनोति
    नि | सीदति → निषीदति    परि | सेवते → परिषेवते    अभि | स्तभ्नाति → अभिष्टभ्नाति

**Where this family differs from the junction rules.** The engine acts at
junctions between words; the inside of a finished word is left alone. The
cerebralising sūtras cannot work that way: the sthānin (a स् of an affix, of a
root) is INTERIOR to a piece, and its cause (an इ, उ, ऋ, र्, a guttural…) may be
several sounds off, in the piece before it. So these rules look across the pieces
of ONE pada — pieces joined by an अङ्ग boundary (`~`), a preverb boundary (`|`),
a compound boundary (`-`) — and never rewrite the inside of a single finished
piece: `arjuna`, `gacchati`, `agnisu` (one word, no join) stay as they are. A
piece the caller marks with a flag is the only thing a rule here will touch.

**What the caller says** (NORTH_STAR §5: what the letters cannot say is a
parameter). Each rule below names, in its docstring, the flag it reads. A flag is
written in braces on a piece — `agni~su{pratyaya}`, `abhi|sunoti{dhatu:sunoti}`.

    pratyaya[:NAME]   the piece is an AFFIX (its स् is a प्रत्ययावयव, 8.3.59).
                      NAME, where a sūtra asks which affix follows (san, sya,
                      yaṅ, caṅ, liṭ, luṅ, ṣīdhvam, niṣṭhā), is the affix's name.
    adesa             the piece is, or holds, a SUBSTITUTE स् (8.3.59) — the स् that
                      6.1.64 puts for a root's initial ष्.
    dhatu:ROOT        the piece is a root (or a form of it). ROOT is the sūtra's
                      own word (`sunoti`, `sedha`, `stambh`…) or the root as the
                      dhātupāṭha gives it (`ṣuñ`, `su`); see `ROOT_NAMES`.
    upasarga          the piece is a preverb — also read from the boundary `|`.
    at                the augment अट् / आट् (a piece of one vowel; 8.3.63).
    abhyasa           the reduplicative syllable (8.3.61–64).
    num               the augment नुम् or the anusvāra that stands for it (8.3.58).
    krt, taddhita     kinds of affix (8.3.73, 8.3.101).
    nyanta            a root in its ṇic form (8.3.61, 8.3.62).
    sense:X           the sense a sūtra names — X is the sūtra's own word
                      (`gati`, `gotra`, `saṃjñā`, `kauśala`…); meaning is the
                      caller's.

The boundaries are the engine's own (segs.ANGA, UPASARGA, SAMASA, PADA).

**The shape of every step.** A cerebralisation is 8.3.55 *apadāntasya
mūrdhanyaḥ* — the स् does not end a pada and is replaced by a मूर्धन्य sound
(which one is 1.1.50, asked of `supports.nearest`: ष् and not ठ्, by the Kāśikā's
tie-break on internal effort) — under a cause. The cause is 8.3.57 *iṇkoḥ*: an
इण् or a कु standing immediately before (1.1.67), across at most ONE नुम्, visarga
or शर् (8.3.58), and — for the roots of 8.3.65–8.3.70 up to *sita* — across the
augment अट् (8.3.63), and — for the ten roots from *sthā* — across the
reduplication (8.3.64). None of 8.3.55, 8.3.57, 8.3.58, 8.3.63 can be a step of
its own (each is a heading that only carries a condition down to the sūtras
after it), so each is CITED in the step of the sūtra it carries: the trace of
*agniṣu* names 8.3.59 as the rule and 8.3.55, 8.3.57 and 1.1.67 among the
sūtras it leans on.

**Refusals** (8.3.61, 8.3.62, 8.3.75, 8.3.110–119) are steps of their own with no
edit, at the SAME site as the application they refuse and winning by
`overrides`, each reason quoted from the Kāśikā or the Bālamanoramā. They are
found by asking the refused rule's own finder (`FINDERS`) what it would do here,
so a refusal is only ever offered where there is something to refuse.

**Ordering.** 8.3.55–119 stand before natva (8.4.1–39) and ṣṭutva (8.4.41), so a
ष् made here can cause them — *abhisunoti* takes its ण् from a ष् made by 8.3.65,
which is the other family's step, not tested here. A rule here reads the products
of the tripādī rules BEFORE it (8.3.34's स् from a visarga, 8.2.66's र्) and is
blind to the products of those after it (8.4.55's क् for a ग्: *viṣvaksenaḥ*
keeps the ग् that 8.3.99 names by *agāt*), which is 8.2.1 and is the View's
business, not this module's.

SCOPE, OPEN — read `COVERAGE`. In short: word lists that are only the sūtra's own
words come from the tables of `murdhanya.py` / `murdhanya_nisedha.py` (which
codify these sūtras as questions) and the gaṇapāṭha; the roots' identity is the
caller's flag; 8.3.103–104 (a स् at the END of a pada, out of a visarga) and 8.3.108
are not attempted; the Vedic 8.3.105–109 and 8.3.119 run only when the caller
says the text is Vedic.
"""

from __future__ import annotations

import unicodedata
from dataclasses import dataclass, field
from functools import lru_cache
from typing import (Callable, Dict, FrozenSet, Iterator, List, Optional,
                    Sequence, Tuple)

from src.astadhyayi import corpus, murdhanya, murdhanya_nisedha
from src.astadhyayi.sandhi import supports as S
from src.astadhyayi.sandhi.parse import tokenize
from src.astadhyayi.sandhi.rule import (
    ADESA, PRATISEDHA, VARTTIKA, Application, Detail, Via, replace, rule, sk,
    site)
from src.astadhyayi.sandhi.segs import (
    AC, ANGA, PADA, SAMASA, UPASARGA, Sight, View, Word, _words)
from src.astadhyayi.sandhi.trace import deva
from src.astadhyayi.sivasutra import resolve_all
from src.astadhyayi.svara import is_hrasva
from src.astadhyayi.varna import (
    ANUNASIKA_MARK, VARGA, VARNAS, VISARGA, Sthana, savarna)

FAMILIES = ("hal", "satva")
#: The refusals carry their own tag so that `@satva` names only the rules that
#: DO cerebralise (8.3.110 refuses "@satva"; it must not refuse its fellows).
REFUSAL_FAMILIES = ("hal", "satva-pratisedha")


#: Every place this module quotes the tradition to give a reason, as
#: (commentary, the sūtra it is on, the words quoted). The words are VERBATIM
#: from the commentary on disk — a test reads each back from `corpus`.
QUOTED: List[Tuple[str, str, str]] = []
_CITED = {"kashika": "Kāśikā", "kaumudi": "Kaumudī",
          "balamanorama": "Bālamanoramā", "tattvabodhini": "Tattvabodhinī"}


def _quote(source: str, on: str, words: str, gloss: str = "") -> str:
    """A reason for an `overrides` entry: the words, whose they are, and (if
    the words alone do not say it) what they settle here."""
    QUOTED.append((source, on, words))
    return (f"{words} ({_CITED[source]} on {on})"
            + (f" — {gloss}" if gloss else ""))

#: The boundaries inside one pada: a piece and its affix (aṅga), a preverb and
#: its root (upasarga), the members of a compound (samāsa).
INSIDE = (ANGA, UPASARGA, SAMASA)

# ---------------------------------------------------------------------------
# The vocabulary a caller speaks — flags on a piece
# ---------------------------------------------------------------------------

PRATYAYA = "pratyaya"
ADESA_FLAG = "adesa"
DHATU = "dhatu"
UPASARGA_FLAG = "upasarga"
AT = "at"
ABHYASA = "abhyasa"
NUM = "num"
KRT = "krt"
TADDHITA = "taddhita"
NYANTA = "nyanta"
SENSE = "sense"
IT_AGAMA = "iṭ"
NIPATA = "nipata"

#: Every flag this family reads, so that a state with none of them costs the
#: engine one pass over its words and nothing more (the termination test runs
#: a thousand junctions through every rule of every family).
_VOCABULARY = frozenset({
    PRATYAYA, ADESA_FLAG, DHATU, UPASARGA_FLAG, AT, ABHYASA, NUM, KRT, TADDHITA,
    NYANTA, SENSE, IT_AGAMA, NIPATA, "agama", "uttarapada"})


def _has(word: Word, name: str) -> bool:
    """A flag `name`, or `name:VALUE`."""
    return any(f == name or f.startswith(name + ":") for f in word.flags)


def _values(word: Word, name: str) -> FrozenSet[str]:
    """The VALUEs of every flag `name:VALUE` the piece carries."""
    return frozenset(f.split(":", 1)[1] for f in word.flags
                     if f.startswith(name + ":"))


def _agama(word: Word, name: str) -> bool:
    """The augment `name`, written `name` or `agama:name`."""
    return _has(word, name) or ("agama:" + name) in word.flags


def _live(v: View) -> bool:
    """Whether the form has anything this family could act on: a piece that
    speaks its vocabulary, or a join inside one pada (a preverb, a compound, an
    affix). Two padas and nothing more — a plain junction — cost one pass."""
    return any(b in INSIDE for b in v.state.bounds) or any(
        f.split(":", 1)[0] in _VOCABULARY
        for word in v.state.words for f in word.flags)


# ---------------------------------------------------------------------------
# Classes of sound — read, never typed
# ---------------------------------------------------------------------------


@lru_cache(maxsize=None)
def _ink() -> FrozenSet[str]:
    """
    इण् as 8.3.57 names it: a vowel other than अ (every length, 1.1.69) and ह्,
    य्, व्, र्, ल्.

    The pratyāhāra is read with the SECOND ण् (that of लण्, śivasūtra 6), which is
    the reading every use of इण् in the Aṣṭādhyāyī needs; `sivasutra.resolve`
    returns the first (इ, उ) and says so, so the wide one is asked of
    `resolve_all`. The widening of the vowels is `supports.members`' own (1.1.69).
    """
    listed = resolve_all("iṆ")[-1].sounds
    found = set(listed)
    vowels = [m for m in listed if m in AC]
    found |= {x for x in AC if any(savarna(x, m) for m in vowels)}
    return frozenset(found)


def _ku() -> Tuple[str, ...]:
    return VARGA["ku"]


@lru_cache(maxsize=None)
def _sar() -> FrozenSet[str]:
    return S.members("śaR")


@lru_cache(maxsize=None)
def _murdhanya() -> Tuple[str, ...]:
    """The sounds of the head — the Śikṣā's ऋटुरषाणां मूर्धा — as `varna` has them."""
    return tuple(sorted(x for x, v in VARNAS.items()
                        if v.sthana is Sthana.MURDHANYA))


@lru_cache(maxsize=None)
def _dantya() -> Tuple[str, ...]:
    return tuple(sorted(x for x, v in VARNAS.items()
                        if v.sthana is Sthana.DANTYA and x not in AC))


@lru_cache(maxsize=None)
def _cerebral_of(sound: str) -> Optional[str]:
    """The मूर्धन्य sound nearest `sound` (1.1.50): स् → ष्, ध् → ढ्, न् → ण्."""
    return S.nearest(sound, _murdhanya())


@lru_cache(maxsize=None)
def _dental_of(sound: str) -> Optional[str]:
    return S.nearest(sound, _dantya())


def _is_cause(sight: Sight, *, ku: bool = True) -> bool:
    return sight.s in _ink() or (ku and sight.s in _ku())


# ---------------------------------------------------------------------------
# Names of words — lexical matching
# ---------------------------------------------------------------------------

_ACCENT_MARKS = "\\^॒॑"


def _canon(text: str) -> str:
    """A name without accent marks or the candrabindu of an anunāsika it-vowel,
    and with an initial ष् read as स् (6.1.64 dhātvādeḥ ṣaḥ saḥ), so that the
    root as the dhātupāṭha writes it (ṣuñ) and as it is spoken (suñ) are one."""
    text = unicodedata.normalize("NFC", text).lower()
    text = "".join(c for c in text
                   if c not in _ACCENT_MARKS and c != ANUNASIKA_MARK)
    if text.startswith("ṣ"):
        text = _dental_of("ṣ") + text[1:]
    return text


def _loose(text: str) -> str:
    """`_canon`, with a final र् or visarga read as स् — the same preverb or
    first member (nis, nir, niḥ; jyotis, jyotir) whichever way it ends."""
    text = _canon(text)
    if text and text[-1] in ("r", VISARGA):
        text = text[:-1] + "s"
    return text


def _stem(label: str) -> str:
    """A sūtra's word without its final vowel — the part every form of it keeps
    (saṅga → saṅg: saṅgaḥ, saṅgam, saṅge)."""
    label = _canon(label)
    while label and label[-1] in AC:
        label = label[:-1]
    return label


#: Roots the sūtras name by a vikaraṇa or an ending (सुनोति, सेध, सञ्ज) or by
#: the shape the root takes (सित, सय, सुट्): for each, the dhātupāṭha's own
#: upadeśa first (checked against the dhātupāṭha in the tests; None where the
#: name is not a dhātupāṭha entry), then the other spellings a caller may write.
#: The sūtra's own word is always accepted, and so is any of these.
ROOT_NAMES: Dict[str, Tuple[Optional[str], ...]] = {
    "sunoti": ("suñ", "su", "sunu"),
    "suvati": ("sū", "suv"),
    "syati": ("so", "sya"),
    "stauti": ("stuñ", "stu", "stav"),
    "stobhati": ("stubhu", "stubh", "stobh"),
    "sthā": ("sthā",),
    "senaya": (None, "sena", "senay"),
    "sedha": ("sidhu", "sidh", "sidha", "sedh"),
    "sica": ("sica", "sic", "siñc"),
    "sañja": ("sanja", "sañj", "saj"),
    "svañja": ("svanja", "svañj", "svaj"),
    "sad": ("sadḷ", "sīd", "sīda"),
    "stambh": ("stanbhu", "stambhu", "stanbh", "stabh"),
    "stambhu": ("stanbhu", "stambh", "stanbh", "stabh"),
    "svan": ("svana",),
    "sev": ("sevṛ", "seva"),
    "sita": (None,),
    "saya": (None,),
    "sivu": ("sivu", "siv", "sīv"),
    "sah": ("saha",),
    "suṭ": (None, "sut"),
    "stu": ("stuñ", "stauti"),
    "svañj": ("svanja", "svañja", "svaj"),
    "syand": ("syandū", "syanda"),
    "skand": ("skandir", "skanda"),
    "sphur": ("sphura",),
    "sphul": ("sphula",),
    "skabh": ("skabhi", "skabhnā"),
    "asti": ("asa", "as"),
    "supi": (None, "sup", "svap"),
    "sūti": (None,),
    "sama": (None,),
    "snā": ("sṇā", "snā"),
    "tap": ("tapa", "tapati"),
    "śās": ("śāsu",),
    "vas": ("vasa",),
    "ghas": ("ghasḷ",),
    "svid": ("svidā",),
    "svad": ("svada",),
    "sṛp": ("sṛpḷ",),
    "sṛj": ("sṛja",),
    "spṛś": ("spṛśa",),
    "spṛh": ("spṛha",),
    "sic": ("sica",),
}


@lru_cache(maxsize=None)
def _aliases(name: str) -> FrozenSet[str]:
    spellings = [name] + [a for a in ROOT_NAMES.get(name, ()) if a]
    return frozenset(_canon(x) for x in spellings)


def _root_named(word: Word, names: Sequence[str]) -> Optional[str]:
    """Which of the sūtra's words `names` this piece is, as its `dhatu:ROOT`
    flag says; None if it is none of them, or is not marked as a root."""
    value = word.flag_value(DHATU)
    if not value:
        return None
    got = _canon(value)
    for name in names:
        if got in _aliases(name):
            return name
    return None


def _senses(word: Word) -> FrozenSet[str]:
    """The senses a piece is marked with; a hyphen cannot be written in a flag,
    so `an-āsevana` is written `anāsevana`."""
    return frozenset(x.replace("-", "") for x in _values(word, SENSE))


def _sense_keys(labels: Sequence[str]) -> FrozenSet[str]:
    return frozenset(x.replace("-", "") for x in labels)


def _first_ok(text: str, labels: Sequence[str]) -> bool:
    """A first member is one of the sūtra's words."""
    got = _loose(text)
    return any(got == _loose(label) for label in labels)


def _second_ok(text: str, label: str, *, exact: bool = False) -> bool:
    """A second member is the sūtra's word: exactly (with a case ending or
    without), or as the start of a longer form of it (saṅga: saṅgaḥ, saṅgā)."""
    got = _canon(text)
    if exact:
        label = _canon(label)
        return got.startswith(label) and got[len(label):] in ("", "s", "m")
    return got.startswith(_stem(label))


# ---------------------------------------------------------------------------
# What the sūtras name — read from the project's own tables
# ---------------------------------------------------------------------------


def _row(sutra: str):
    """The row the project's own question-modules hold for a sūtra: its named
    words (`of`), first members (`after`), senses, optionality."""
    rows = (murdhanya.provisions_for(sutra)
            or murdhanya_nisedha.provisions_for(sutra))
    return rows[0]


def _labels(sutra: str) -> Tuple[str, ...]:
    """The first members a sūtra names, as its row spells them (`pari-ni-vi`)."""
    return tuple(_row(sutra).after.split("-"))


SUNOTI = murdhanya.SUNOTI_ELEVEN
SEVADI = murdhanya.SEVADI_EIGHT
SIVADI = murdhanya.SIVADI

#: Every root named before *sita* in 8.3.70 — the stretch 8.3.63 runs over
#: ("prāk sitāt"): the eleven of 8.3.65, सद्, स्तम्भ्, स्वन्, सेव्.
PRAK_SITAT: Tuple[str, ...] = (
    SUNOTI + _row("8.3.66").of + _row("8.3.67").of + _row("8.3.69").of
    + SEVADI[:SEVADI.index("sita")])

#: 8.3.64's *sthādi*: from स्था to the end of that stretch — ten (the
#: Bālamanoramā: दशस्विति).
STHADI: Tuple[str, ...] = PRAK_SITAT[PRAK_SITAT.index("sthā"):]

#: 8.3.97's eighteen first members. The sūtra is one long compound and the
#: Kāśikā's examples are the words split (अम्बष्ठः … अग्निष्ठः); the test checks
#: each against them.
AMBADI: Tuple[str, ...] = (
    "amba", "āmba", "go", "bhūmi", "savye", "apa", "dvi", "tri", "ku", "śeku",
    "śaṅku", "aṅgu", "mañji", "puñji", "parame", "barhis", "divi", "agni")

#: The two upasarga-like words 1.4.60's vārttika removes from the upasargas for
#: ṣatva: दुरः षत्वणत्वयोरुपसर्गत्वप्रतिषेधो वक्तव्यः.
NOT_UPASARGA_HERE = ("dus",)


# ---------------------------------------------------------------------------
# Where a स् stands, and what stands before it
# ---------------------------------------------------------------------------


def _words_of(sight: Sight) -> FrozenSet[int]:
    return frozenset(_words(sight.seg))


def _in_piece(v: View, sight: Sight, flag: str, *, agama: bool = False) -> bool:
    words = v.state.words
    return any((_agama(words[i], flag) if agama else _has(words[i], flag))
               for i in _words_of(sight))


def _first_sight(v: View, w: int) -> Optional[Sight]:
    sights = v.word_sights(w)
    return sights[0] if sights else None


def _upasarga_index(v: View, sight: Sight) -> Optional[int]:
    """The preverb this sound belongs to, by the boundary `|` after its piece or
    by the flag `upasarga`; None if it belongs to none."""
    for i in sorted(_words_of(sight)):
        if v.state.bounds[i] == UPASARGA or _has(v.state.words[i],
                                                   UPASARGA_FLAG):
            return i
    return None


def _up_in(text: str, labels: Sequence[str]) -> bool:
    return any(_loose(text) == _loose(label) for label in labels)


def _standing(v: View, s: Sight, *, upasarga_end: bool = False) -> bool:
    """8.3.55 अपदान्तस्य, and the guard this family needs: the स् does not end a
    pada, and is either the first sound of its piece or lies in a pada made of
    joined pieces — a finished word's inside is never offered.

    `upasarga_end`: 8.3.102 reaches the final स् of the preverb *nis* itself; at
    that moment the preverb has only joined its root and is not yet a pada
    (*pūrvaṃ dhātur upasargeṇa yujyate*, Kaumudī on 8.3.74)."""
    if v.pada_final(s):
        if not (upasarga_end and v.boundary_after(s) == UPASARGA):
            return False
    return v.begins_word(s) or v.joined_pada(s, across=INSIDE)


@dataclass(frozen=True)
class Reach:
    """What lies between a स् and its cause: the cause, and the sounds the
    cerebral crosses to get there."""

    nimitta: Optional[Sight]
    #: (kind, sounds) with kind one of num, visarga, sar, at, abhyasa.
    crossed: Tuple[Tuple[str, Tuple[Sight, ...]], ...] = ()

    @property
    def kinds(self) -> Tuple[str, ...]:
        return tuple(k for k, _ in self.crossed)

    def sights(self) -> Tuple[Sight, ...]:
        return tuple(x for _, group in self.crossed for x in group)


def _vyavaya_kind(v: View, c: Sight) -> Optional[str]:
    """8.3.58: a नुम्, a visarga, a शर् — each by itself."""
    if _in_piece(v, c, NUM):
        return "num"
    if c.s == VISARGA:
        return "visarga"
    if c.s in _sar():
        return "sar"
    return None


def _reach(v: View, s: Sight, *, at_ok: bool = False,
           abhyasa_ok: bool = False) -> Reach:
    """
    Walk left from `s` to its cause, crossing what the sūtras allow.

    * one नुम्, visarga or शर् (8.3.58 — प्रत्येकं व्यवायशब्दः, never two);
    * the augment अट् where `at_ok` (8.3.63 प्राक्सितादड्व्यवायेऽपि);
    * the reduplicative syllable where `abhyasa_ok` (8.3.64).

    The sound it stops at is returned whether or not it is a cause: each rule
    asks what the cause must be.
    """
    crossed: List[Tuple[str, Tuple[Sight, ...]]] = []
    used = set()
    cur = v.prev(s)
    while cur is not None:
        kind = None
        if at_ok and "at" not in used and _in_piece(v, cur, AT, agama=True):
            kind = "at"
        elif (abhyasa_ok and "abhyasa" not in used
              and _in_piece(v, cur, ABHYASA)):
            kind = "abhyasa"
        elif "vyavaya" not in used:
            kind = _vyavaya_kind(v, cur)
        if kind is None:
            break
        group = [cur]
        if kind in ("at", "abhyasa"):
            flag = AT if kind == "at" else ABHYASA
            while True:
                before = v.prev(group[-1])
                if before is None or not _in_piece(
                        v, before, flag, agama=(kind == "at")):
                    break
                group.append(before)
            used.add(kind)
        else:
            used.add("vyavaya")
        crossed.append((kind, tuple(reversed(group))))
        cur = v.prev(group[-1])
    return Reach(cur, tuple(reversed(crossed)))


# ---------------------------------------------------------------------------
# One place a rule applies
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Hit:
    """
    A cerebralisation a sūtra makes here: the sthānin, the substitute, the cause
    and what it crossed, and the explanation. Both the rule that makes it and
    the refusals that stop it are built from the same Hit, so a refusal always
    has exactly the SITE of what it refuses.
    """

    sutra: str
    s: Sight
    sub: str
    reach: Optional[Reach]
    nimitta_text: str
    because: str
    via: Tuple[Via, ...]
    optional: str = ""
    note: str = ""
    #: What a refusal may need to ask of the place (root, preverb, …).
    info: Dict[str, object] = field(default_factory=dict)

    @property
    def site(self) -> Tuple[int, ...]:
        sights = [self.s]
        if self.reach is not None:
            if self.reach.nimitta is not None:
                sights.append(self.reach.nimitta)
            sights.extend(self.reach.sights())
        return site(*sights)


def _cerebral(sthanin: str) -> str:
    sub = _cerebral_of(sthanin)
    if sub is None:                                    # pragma: no cover
        raise ValueError(f"no cerebral is nearest {sthanin!r}")
    return sub


def _vias(s: Sight, sub: str, reach: Optional[Reach], *, ink: bool = True,
          ku: bool = True, sutra: str = "") -> Tuple[Via, ...]:
    """The sūtras every cerebralisation leans on, each saying what it did HERE."""
    out: List[Via] = [Via(
        "8.3.55",
        f"{sk(s.s)} does not end a pada ({{apadānta}}), so it is replaced by a "
        f"{{mūrdhanya}} sound")]
    if reach is not None and reach.nimitta is not None and ink:
        n = reach.nimitta
        kind = ("an {iṇ}" if n.s in _ink() else "a {ku}")
        out.append(Via(
            "8.3.57",
            f"the cause must be an {{iṇ}}" + (" or a {ku}" if ku else "")
            + f": {sk(n.s)} is {kind}"))
        out.append(S.pancami_para(f"{sk(n.s)}, {kind}"))
    if reach is not None:
        for kind, group in reach.crossed:
            sounds = "+".join(sk(x.s) for x in group)
            if kind in ("num", "visarga", "sar"):
                what = {"num": "the {num} (its anusvāra)",
                        "visarga": "a visarga",
                        "sar": "a {śar}"}[kind]
                out.append(Via(
                    "8.3.58",
                    f"{what} ({sounds}) stands between the cause and "
                    f"{sk(s.s)}; the sūtra lets the cerebral reach across "
                    f"exactly one such sound"))
            elif kind == "at" and sutra == "8.3.71":
                continue                      # 8.3.71 is the sūtra that says so
            elif kind == "at":
                out.append(Via(
                    "8.3.63",
                    f"the augment {{aṭ}} ({sounds}) stands between the cause "
                    f"and {sk(s.s)}; this root lies before *sita* in 8.3.70, "
                    f"where the cerebral reaches across the augment"))
            else:
                out.append(Via(
                    "8.3.64",
                    f"the reduplicative syllable ({sounds}) stands between "
                    f"the cause and {sk(s.s)}; a root of the sthādi ten lets "
                    f"the cerebral reach across it"))
    out.append(S.antaratama(
        s.s, sub, "8.3.55 allows — the {mūrdhanya} sounds ("
        + ", ".join(_murdhanya()) + ") —"))
    return tuple(out)


def _nimitta_text(s: Sight, reach: Optional[Reach], what: str = "an {iṇ}"
                  ) -> str:
    if reach is None or reach.nimitta is None:
        return "no cause is asked for"
    n = reach.nimitta
    kind = "an {iṇ}" if n.s in _ink() else "a {ku}" if n.s in _ku() else what
    across = ""
    if reach.crossed:
        across = (", across "
                  + " and ".join(sk("".join(x.s for x in g))
                                 for _, g in reach.crossed))
    return f"{kind} {sk(n.s)} stands before {sk(s.s)}{across}"


def _hit(sutra: str, s: Sight, reach: Optional[Reach], because: str, *,
         ink: bool = True, ku: bool = True, optional: str = "", note: str = "",
         extra: Tuple[Via, ...] = (), info: Optional[Dict[str, object]] = None,
         nimitta_text: str = "", sthanin: Optional[str] = None) -> Hit:
    sub = _cerebral(sthanin or s.s)
    return Hit(
        sutra=sutra, s=s, sub=sub, reach=reach,
        nimitta_text=nimitta_text or _nimitta_text(s, reach),
        because=because,
        via=_vias(s, sub, reach, ink=ink, ku=ku, sutra=sutra) + extra,
        optional=optional, note=note, info=dict(info or {}))


def _application(hit: Hit) -> Application:
    return Application(
        site=hit.site, edits=(replace(hit.s, hit.sub),),
        detail=Detail(
            kind=ADESA, sthanin=hit.s.s, adesa=hit.sub,
            nimitta=hit.nimitta_text, because=hit.because, via=hit.via,
            note=hit.note),
        optional=hit.optional)


# ---------------------------------------------------------------------------
# The finders — one per sūtra that cerebralises
# ---------------------------------------------------------------------------

Finder = Callable[[View], Iterator[Hit]]
FINDERS: Dict[str, Finder] = {}
_RULES: List = []


def _name(sutra: str) -> str:
    """The sūtra's name as the corpus has it, in Devanāgarī."""
    return deva(corpus.load_vidyut_sutrapatha()[sutra].text)


def _operative(sutra: str, *, overrides=(), vedic: bool = False):
    """Register a finder as the rule for `sutra`."""

    def wrap(finder: Finder):
        FINDERS[sutra] = finder

        def find(v: View):
            if not _live(v):
                return
            for hit in finder(v):
                yield _application(hit)

        find.__doc__ = finder.__doc__
        built = rule(sutra, name=_name(sutra), families=FAMILIES,
                     overrides=overrides, vedic=vedic)(find)
        _RULES.append(built)
        return built

    return wrap


# -- 8.3.56 ------------------------------------------------------------------


@_operative("8.3.56")
def _f56(v: View):
    """
    सहेः साडः सः — the स् of सह् in the form साड्: जलाषाट्, तुराषाट्, पृतनाषाट्.

    Reads: `dhatu:sah` on a piece whose text is `sāḍ` (or `sāṭ`, the सूत्र's
    कृतजश्त्वनिर्देशः पदान्तोपलक्षणम्, Bālamanoramā), joined to an earlier member
    by `-`, `~` or `|`. No cause is asked for (the sūtra stands before 8.3.57's
    इण्कोः): जलाषाट् has ष् after आ. Only the स् goes — the आ stays (सः इति किम्?
    आकारस्य मा भूत्). Not सह् at all (सहेरिति किम्? साडिः) and not the other
    shape of the root (साड्ग्रहणं किम्? तुरासाहम्) are left alone.
    """
    for w, word in enumerate(v.state.words):
        if w == 0 or v.state.bounds[w - 1] == PADA:
            continue
        if _root_named(word, ("sah",)) is None:
            continue
        if _canon(word.text) not in ("sāḍ", "sāṭ"):
            continue
        s = _first_sight(v, w)
        if s is None or s.s != "s" or not _standing(v, s):
            continue
        yield _hit(
            "8.3.56", s, None,
            f"{sk('s')} begins the form {sk('sāḍ')} of the root {sk('sah')}, "
            f"after an earlier member, so it becomes {sk(_cerebral('s'))}; the "
            f"{sk('ā')} after it is not touched",
            nimitta_text="the root सह् in the form साड्", ink=False)


# -- 8.3.59 ------------------------------------------------------------------


def _affix_or_substitute(v: View, s: Sight) -> str:
    word = v.word(s)
    if _has(word, PRATYAYA):
        return "affix"
    if _has(word, ADESA_FLAG):
        return "substitute"
    return ""


@_operative("8.3.59")
def _f59(v: View):
    """
    आदेशप्रत्यययोः — the स् that is a SUBSTITUTE or part of an AFFIX, after an इण्
    or a कु: अग्निषु, वायुषु, कर्तृषु, सर्पिषि (the स् of the affix in सर्पिस्);
    सिषेव, सुष्वाप (the स् that stands for a root's ष्).

    Reads: `pratyaya` (or `pratyaya:NAME`) on the piece holding an affix's स्;
    `adesa` on the piece holding a substitute स्. The two genitives are read
    apart (आदेशप्रत्यययोरिति षष्ठी भेदेन सम्बध्यते, Kāśikā) and a प्रत्यय means the
    प्रत्ययावयव (Kaumudī: प्रत्ययावयवश्च यः सकारः). The cause is asked of the sound
    just before, across one नुम्, visarga or शर् (8.3.58), and NOT across an
    augment or a reduplication (this sūtra stands after 8.3.70). Not रामस्य (कोः
    इण्कोः किम्: no इण् before) and not हरिस्तत्र (अपदान्तस्य किम्: the स् ends a
    pada).
    """
    for s in v.live:
        if s.s != "s":
            continue
        kind = _affix_or_substitute(v, s)
        if not kind or not _standing(v, s):
            continue
        reach = _reach(v, s)
        if reach.nimitta is None or not _is_cause(reach.nimitta):
            continue
        what = ("the {s} is part of an affix (a {pratyaya})"
                if kind == "affix" else "the {s} is a substitute (an {ādeśa})")
        yield _hit(
            "8.3.59", s, reach,
            f"{what}, it does not end its pada, and "
            f"{_nimitta_text(s, reach)}, so it becomes {sk(_cerebral('s'))}",
            info={"kind": kind, "w": s.w})


# -- 8.3.60 ------------------------------------------------------------------


@_operative("8.3.60")
def _f60(v: View):
    """
    शासिवसिघसीनां च — the स् of शास्, वस्, घस् after an इण् or a कु, though it is
    neither a substitute nor an affix's: अन्वशिषत्, शिष्टः, उषितः, जक्षतुः.

    Reads: `dhatu:śās`, `dhatu:vas`, `dhatu:ghas` on the piece (the root as it
    stands, शिस्, उस्, घ्स्). Not शास्ति, वसति, जघास (इण्कोरित्येव: the sound before
    is not an इण् or a कु).
    """
    names = _row("8.3.60").of
    for s in v.live:
        if s.s != "s":
            continue
        word = v.word(s)
        root = _root_named(word, names)
        if root is None or not _standing(v, s):
            continue
        reach = _reach(v, s)
        if reach.nimitta is None or not _is_cause(reach.nimitta):
            continue
        yield _hit(
            "8.3.60", s, reach,
            f"{sk('s')} is the स् of the root {sk(root)}, which this sūtra "
            f"names though it is neither a substitute nor an affix's, and "
            f"{_nimitta_text(s, reach)}, so it becomes {sk(_cerebral('s'))}",
            info={"root": root, "w": s.w})


# -- the preverb and the root: 8.3.65 – 8.3.77 -------------------------------


@dataclass(frozen=True)
class PV:
    """One sūtra of the run that puts a preverb before a root."""

    sutra: str
    roots: Tuple[str, ...]
    #: The preverbs the sūtra names; None for any preverb (8.3.65 उपसर्गात्).
    ups: Optional[Tuple[str, ...]] = None
    ups_not: Tuple[str, ...] = ()
    #: Whether the cause must be an इण्. 8.3.68 and 8.3.69 give the cerebral after
    #: अव too, which has none (अपूर्वविधिरयम्, इणः परत्वाऽभावादप्राप्तेः — Bālamanoramā).
    need_in: bool = True
    #: How the root meets the augment अट्: "yes" (8.3.63 carries it), "no", "only".
    at: Callable[[Word], str] = lambda word: "yes"
    sense: Tuple[str, ...] = ()
    when: Optional[Callable[[View, int, Word], bool]] = None
    skip: Optional[Callable[..., bool]] = None
    optional: str = ""


def _next_piece(v: View, w: int, across=(ANGA,)) -> Optional[Word]:
    words, bounds = v.state.words, v.state.bounds
    if w + 1 < len(words) and bounds[w] in across:
        return words[w + 1]
    return None


def _sense_of(labels: Sequence[str]) -> Tuple[str, ...]:
    return tuple(sorted(_sense_keys(labels)))


def _pv_finder(pv: PV) -> Finder:
    sutra = pv.sutra

    def find(v: View):
        words = v.state.words
        for w, word in enumerate(words):
            name = _root_named(word, pv.roots)
            if name is None:
                continue
            s = _first_sight(v, w)
            if s is None or s.s != "s" or not _standing(v, s):
                continue
            if pv.sense and not (_senses(word) & set(_sense_of(pv.sense))):
                continue
            if pv.when is not None and not pv.when(v, w, word):
                continue
            mode = pv.at(word)
            sthadi = _root_named(word, STHADI) is not None
            reach = _reach(v, s, at_ok=(mode != "no"), abhyasa_ok=sthadi)
            n = reach.nimitta
            if n is None or (mode == "only" and "at" not in reach.kinds):
                continue
            u = _upasarga_index(v, n)
            if u is None:
                continue
            up_text = words[u].text
            if pv.ups is None:
                if _up_in(up_text, NOT_UPASARGA_HERE):
                    continue
            elif not _up_in(up_text, pv.ups):
                continue
            if pv.ups_not and _up_in(up_text, pv.ups_not):
                continue
            if pv.need_in and n.s not in _ink():
                continue
            if pv.skip is not None and pv.skip(v, w, word, up_text, reach):
                continue
            root_text = word.text
            yield _hit(
                sutra, s, reach,
                f"{sk(s.s)} begins the root {sk(name)} ({sk(root_text)}), "
                f"which stands after the preverb {sk(up_text)}; "
                f"{_nimitta_text(s, reach)}, so it becomes "
                f"{sk(_cerebral('s'))}",
                ink=pv.need_in, ku=False, optional=pv.optional,
                info={"root": name, "w": w, "upasarga": up_text, "up_w": u,
                      "reach": reach})

    find.__doc__ = None
    return find


def _sivadi_at(word: Word) -> str:
    """8.3.70: the cerebral reaches across the augment only for सेव् (and the
    kṛdantas सित, सय, which never have one); for the five of 8.3.71 it does not."""
    return "no" if _root_named(word, SIVADI) is not None else "yes"


def _supplanted_by_8371(v: View, w: int, word: Word, up_text: str,
                        reach: Reach) -> bool:
    """8.3.65 also names स्तौति and स्वञ्ज. Across the augment, after परि, नि, वि,
    8.3.71 makes the cerebral optional for those two, and 'पूर्वेणैव सिद्धे
    स्तुस्वञ्जिग्रहणमुत्तरार्थम्, अड्व्यवाये विभाषा यथा स्यात्' (Kāśikā on 8.3.70)
    — so 8.3.65 leaves that case to 8.3.71."""
    return ("at" in reach.kinds
            and _up_in(up_text, _labels("8.3.71"))
            and _root_named(word, ("stu", "svañj")) is not None)


def _not_before_niṣṭhā(v: View, w: int, word: Word) -> bool:
    """8.3.73 अनिष्ठायाम् — a कृत् affix that is not a निष्ठा follows."""
    nxt = _next_piece(v, w)
    return (nxt is not None and _has(nxt, KRT)
            and "niṣṭhā" not in _values(nxt, PRATYAYA))


_PVS: Tuple[PV, ...] = (
    PV("8.3.65", roots=_row("8.3.65").of, skip=_supplanted_by_8371),
    PV("8.3.66", roots=_row("8.3.66").of, ups_not=("prati",)),
    PV("8.3.67", roots=_row("8.3.67").of),
    PV("8.3.68", roots=_row("8.3.68").of, ups=_labels("8.3.68"),
       need_in=False, sense=_row("8.3.68").sense),
    PV("8.3.69", roots=_row("8.3.69").of, ups=_labels("8.3.69"),
       need_in=False, sense=_row("8.3.69").sense),
    PV("8.3.70", roots=_row("8.3.70").of, ups=_labels("8.3.70"),
       at=_sivadi_at),
    PV("8.3.71", roots=_row("8.3.71").of, ups=_labels("8.3.71"),
       at=lambda word: "only", optional="वा"),
    PV("8.3.72", roots=_row("8.3.72").of, ups=_labels("8.3.72"),
       at=lambda word: "no", sense=_row("8.3.72").sense, optional="वा"),
    PV("8.3.73", roots=_row("8.3.73").of, ups=_labels("8.3.73"),
       at=lambda word: "no", when=_not_before_niṣṭhā, optional="वा"),
    PV("8.3.74", roots=_row("8.3.74").of, ups=_labels("8.3.74"),
       at=lambda word: "no", optional="वा"),
    PV("8.3.76", roots=_row("8.3.76").of, ups=_labels("8.3.76"),
       at=lambda word: "no", optional="वा"),
    PV("8.3.77", roots=_row("8.3.77").of, ups=_labels("8.3.77"),
       at=lambda word: "no"),
)
PV_BY_SUTRA: Dict[str, PV] = {pv.sutra: pv for pv in _PVS}


_PV_DOC: Dict[str, str] = {}


def _register_pvs() -> None:
    overrides = {
        "8.3.71": (
            ("8.3.65", _quote(
                "kashika", "8.3.70",
                "पूर्वेणैव सिद्धे स्तुस्वञ्जिग्रहणमुत्तरार्थम्, अड्व्यवाये विभाषा "
                "यथा स्यात्")),
            ("8.3.70", _quote(
                "kashika", "8.3.71",
                "सिवादीनामड्व्यवायेऽपि परिनिविभ्य उत्तरस्य सकारस्य वा "
                "मूर्धन्यो भवति"))),
        "8.3.77": (
            ("8.3.76", _quote(
                "tattvabodhini", "8.3.77", "ध्वननार्थमिह नित्यग्रहणम्",
                "वा is not carried down: the cerebral after वि is not "
                "optional for स्कभ्")),),
    }
    for pv in _PVS:
        finder = _pv_finder(pv)
        finder.__doc__ = _PV_DOC.get(pv.sutra)
        _operative(pv.sutra, overrides=overrides.get(pv.sutra, ()))(finder)


# -- 8.3.64: the reduplicative syllable ---------------------------------------


def _pv_for(word: Word) -> Optional[PV]:
    """The sūtra whose word list holds this root, among those that name a
    preverb generally (8.3.65, 8.3.66, 8.3.67, 8.3.70)."""
    for sutra in ("8.3.65", "8.3.66", "8.3.67", "8.3.70"):
        pv = PV_BY_SUTRA[sutra]
        if _root_named(word, pv.roots) is not None:
            return pv
    return None


@_operative("8.3.64")
def _f64(v: View):
    """
    स्थादिष्वभ्यासेन चाभ्यासस्य — for the ten roots from स्था on, the cerebral of
    8.3.65–8.3.70 reaches across the reduplicative syllable (that half is in
    `_reach`, and each such step names 8.3.64 among its sūtras), AND it reaches
    the reduplicative syllable's own स्: अभिषिषेणयिषति, अभिषिषिक्षति, निषिषेध.

    Reads: `abhyasa` on the syllable, `dhatu:ROOT` on the root piece after it
    (`~`), the preverb before by `|`. Only for those ten: अभ्यासस्येति वचनं
    नियमार्थम् — स्थादिष्वेवाभ्याससकारस्य मूर्धन्यो भवति, नान्यत्र (Kāśikā): the
    syllable of सुनोति does not take it (अभिसुसूषति). The preverb conditions are
    the root's own (सद् not after प्रति; the eleven and स्तम्भ् after any preverb).
    """
    words = v.state.words
    for w, word in enumerate(words):
        if not _has(word, ABHYASA):
            continue
        root_word = _next_piece(v, w)
        if root_word is None or _root_named(root_word, STHADI) is None:
            continue
        pv = _pv_for(root_word)
        s = _first_sight(v, w)
        if pv is None or s is None or s.s != "s" or not _standing(v, s):
            continue
        reach = _reach(v, s, at_ok=True)
        n = reach.nimitta
        if n is None or n.s not in _ink():
            continue
        u = _upasarga_index(v, n)
        if u is None:
            continue
        up_text = words[u].text
        if pv.ups is None:
            if _up_in(up_text, NOT_UPASARGA_HERE):
                continue
        elif not _up_in(up_text, pv.ups):
            continue
        if pv.ups_not and _up_in(up_text, pv.ups_not):
            continue
        name = _root_named(root_word, pv.roots)
        yield _hit(
            "8.3.64", s, reach,
            f"{sk(s.s)} is the स् of the reduplicative syllable "
            f"{sk(word.text)} of the root {sk(name)}, one of the ten from "
            f"{sk('sthā')} on, and it stands after the preverb "
            f"{sk(up_text)}; {_nimitta_text(s, reach)}, so it becomes "
            f"{sk(_cerebral('s'))}",
            ku=False,
            info={"root": name, "root_w": w + 1, "w": w, "upasarga": up_text,
                  "up_w": u, "reach": reach, "abhyasa": True})


# -- 8.3.78, 8.3.79: the ध् of ष्वम् ... ------------------------------------


def _dh_finder(sutra: str, *, after_it: bool) -> Finder:
    names = frozenset(_canon(x) for x in _row("8.3.78").before)

    def find(v: View):
        words = v.state.words
        for w, word in enumerate(words):
            if w == 0 or v.state.bounds[w - 1] != ANGA:
                continue
            if not (frozenset(_canon(x) for x in _values(word, PRATYAYA))
                    & names):
                continue
            dh = next((x for x in v.word_sights(w) if x.s == "dh"), None)
            if dh is None or not _standing(v, dh):
                continue
            first = _first_sight(v, w)
            before = v.prev(first) if first is not None else None
            if before is None:
                continue
            with_it = _agama(words[w - 1], IT_AGAMA)
            if after_it:
                # 8.3.79: the aṅga ends in an इट् that stands after an इण्
                if not with_it:
                    continue
                run = [x for x in v.word_sights(w - 1)]
                head = v.prev(run[0]) if run else None
                if head is None or head.s not in _ink():
                    continue
                cause = head
            else:
                # 8.3.78: the aṅga ends in an इण् — a कु is left out (इण्कोः
                # इति वर्तमाने पुनरिण्ग्रहणं कवर्गनिवृत्त्यर्थम्) — and where an इट्
                # stands after it, 8.3.79's option takes the place instead.
                if before.s not in _ink():
                    continue
                if with_it:
                    run = [x for x in v.word_sights(w - 1)]
                    head = v.prev(run[0]) if run else None
                    if head is not None and head.s in _ink():
                        continue
                cause = before
            reach = Reach(cause)
            ending = sorted(_values(word, PRATYAYA) )[0]
            yield _hit(
                sutra, dh, reach,
                f"{sk('dh')} is the ध् of the ending {sk(ending)}, which the "
                f"sūtra names; the aṅga before it ends "
                + ("in an {iṭ} that stands after an {iṇ} — "
                   f"{sk(cause.s)} — " if after_it else
                   f"in an {{iṇ}}, {sk(cause.s)}, ")
                + f"so it becomes {sk(_cerebral('dh'))}",
                ink=False, ku=False,
                optional="विभाषा" if after_it else "",
                nimitta_text=f"the aṅga ends in an {{iṇ}} {sk(cause.s)}",
                extra=(S.pancami_para(f"{sk(cause.s)}, an {{iṇ}} ending the "
                                      f"aṅga"),),
                info={"w": w, "ending": ending})

    return find


_DH_DOC = {
    "8.3.78": """
    इणः षीध्वंलुङ्लिटां धोऽङ्गात् — after an aṅga ending in an इण्, the ध् of
    ष्वम्, of luṅ's ध्वम् and of liṭ's ध्वे becomes ढ्: च्योषीढ्वम्, अच्योढ्वम्,
    चकृढ्वे.

    Reads: `pratyaya:ṣīdhvam`, `pratyaya:luṅ` or `pratyaya:liṭ` on the ending
    (joined to the aṅga by `~`), the aṅga's last sound. A कु does not count
    (पक्षीध्वम्, यक्षीध्वम् — इण्कोः इति वर्तमाने पुनरिण्ग्रहणं कवर्गनिवृत्त्यर्थम्);
    any other ending is left (स्तुध्वे, अस्तुध्वम् — षीध्वंलुङ्लिटामिति किम्); and
    an aṅga that does not end in one is left (परिवेविषीध्वम् — अङ्गादिति किम्).
    """,
    "8.3.79": """
    विभाषेटः — the same ध्, where an इट् stands after the इण्: optional.
    लविषीढ्वम् / लविषीध्वम्, अलविढ्वम् / अलविध्वम्, अयिषीढ्वम् / अयिषीध्वम्.

    Reads: the same endings as 8.3.78, and `iṭ` on the piece before the ending
    (an augment; `agama:iṭ` also serves). An option of the प्राप्तविभाषा kind: it
    replaces 8.3.78 in this case, so 8.3.78 stands aside here rather than
    returning when the option is declined.
    """,
}


def _register_dh() -> None:
    for sutra, after_it in (("8.3.78", False), ("8.3.79", True)):
        finder = _dh_finder(sutra, after_it=after_it)
        finder.__doc__ = _DH_DOC[sutra]
        overrides = ()
        if sutra == "8.3.79":
            overrides = (("8.3.78", _quote(
                "kashika", "8.3.79",
                "षीध्वंलुङ्लिटां यो धकारस्तस्य मूर्धन्यादेशो भवति विभाषा")),)
        _operative(sutra, overrides=overrides)(finder)


# -- the compounds and their kin: 8.3.80 – 8.3.89, 8.3.95 – 8.3.97, 8.3.105 ---


@dataclass(frozen=True)
class CP:
    """One sūtra that names a first member and a second."""

    sutra: str
    firsts: Optional[Tuple[str, ...]]
    seconds: Tuple[str, ...]
    need_in: bool = True
    bounds: Tuple[str, ...] = (SAMASA,)
    #: Second members that must be the word itself and not a longer one.
    exact: FrozenSet[str] = frozenset()
    #: Second members that are a root: named by `dhatu:ROOT`, not by their text.
    roots: FrozenSet[str] = frozenset()
    sense: Tuple[str, ...] = ()
    where: Optional[Callable[..., bool]] = None
    optional: str = ""


def _second_matches(cp: CP, word: Word) -> Optional[str]:
    for label in cp.seconds:
        if label in cp.roots:
            if _root_named(word, (label,)) is not None:
                return label
        elif _second_ok(word.text, label, exact=label in cp.exact):
            return label
    return None


def _cp_finder(cp: CP) -> Finder:
    sutra = cp.sutra

    def find(v: View):
        words, bounds = v.state.words, v.state.bounds
        for w in range(1, len(words)):
            if bounds[w - 1] not in cp.bounds:
                continue
            first, second = words[w - 1], words[w]
            if cp.firsts is not None and not _first_ok(first.text, cp.firsts):
                continue
            label = _second_matches(cp, second)
            if label is None:
                continue
            s = _first_sight(v, w)
            if s is None or s.s != "s" or not _standing(v, s):
                continue
            if cp.sense and not ((_senses(first) | _senses(second))
                                 & set(_sense_of(cp.sense))):
                continue
            if cp.where is not None and not cp.where(v, w, first, second,
                                                     label):
                continue
            reach = _reach(v, s)
            n = reach.nimitta
            if cp.need_in and (n is None or not _is_cause(n)
                               or (w - 1) not in _words_of(n)):
                continue
            yield _hit(
                sutra, s, reach,
                f"{sk(s.s)} begins {sk(second.text)}, the second member of the "
                f"compound {sk(first.text)}-{sk(second.text)}, the sūtra's "
                f"{sk(label)}; "
                + (f"{_nimitta_text(s, reach)}, " if cp.need_in else
                   "the sūtra asks for no cause but the first member, ")
                + f"so it becomes {sk(_cerebral('s'))}",
                ink=cp.need_in, optional=cp.optional,
                nimitta_text=(_nimitta_text(s, reach) if cp.need_in else
                              f"the first member {sk(first.text)} (named by "
                              f"the sūtra)"),
                info={"w": w, "first": first.text, "second": second.text,
                      "label": label})

    return find


def _agni_soma(v: View, w: int, first: Word, second: Word,
               label: str) -> bool:
    """अग्नेर्दीर्घात् सोमस्येष्यते (Kāśikā on 8.3.82): सोम after the LENGTHENED अग्नी
    (अग्नीषोमौ); स्तुत् and स्तोम after the short अग्नि (अग्निष्टोमः)."""
    long_first = _canon(first.text).endswith("ī")
    return long_first if label == "soma" else not long_first


_AMBADI_FIRSTS = AMBADI

_CPS: Tuple[CP, ...] = (
    CP("8.3.80", firsts=_labels("8.3.80"), seconds=_row("8.3.80").of),
    CP("8.3.81", firsts=_labels("8.3.81"), seconds=_row("8.3.81").of),
    CP("8.3.82", firsts=_labels("8.3.82") + ("agnī",),
       seconds=_row("8.3.82").of, exact=frozenset({"stut"}),
       where=_agni_soma),
    CP("8.3.83", firsts=_labels("8.3.83"), seconds=_row("8.3.83").of,
       need_in=False),
    CP("8.3.84", firsts=_labels("8.3.84"), seconds=_row("8.3.84").of),
    CP("8.3.85", firsts=_labels("8.3.85"), seconds=_row("8.3.85").of,
       optional="अन्यतरस्याम्"),
    CP("8.3.86", firsts=_labels("8.3.86"), seconds=_row("8.3.86").of,
       bounds=(SAMASA, UPASARGA, ANGA), sense=_row("8.3.86").sense,
       optional="अन्यतरस्याम्"),
    CP("8.3.88", firsts=_labels("8.3.88"), seconds=_row("8.3.88").of,
       bounds=(SAMASA, UPASARGA), roots=frozenset({"supi"}),
       exact=frozenset({"sūti", "sama"})),
    CP("8.3.89", firsts=_labels("8.3.89"), seconds=_row("8.3.89").of,
       bounds=(SAMASA, UPASARGA), roots=frozenset({"snā"}),
       sense=_row("8.3.89").sense),
    CP("8.3.95", firsts=_labels("8.3.95"), seconds=_row("8.3.95").of),
    CP("8.3.96", firsts=_labels("8.3.96"), seconds=_row("8.3.96").of),
    CP("8.3.97", firsts=_AMBADI_FIRSTS, seconds=_row("8.3.97").of,
       need_in=False, exact=frozenset({"stha"})),
    CP("8.3.105", firsts=None, seconds=_row("8.3.105").of,
       optional="एकेषाम्"),
    CP("8.3.109", firsts=("pṛtanā", "ṛta", "ṛtā"), seconds=_row("8.3.109").of,
       need_in=False, roots=frozenset({"sah"})),
)
CP_BY_SUTRA: Dict[str, CP] = {cp.sutra: cp for cp in _CPS}

def _register_cps() -> None:
    docs = _CP_DOC
    overrides = {
        "8.3.82": (("8.3.111", _quote(
            "balamanorama", "8.3.82", "इति षत्वनिषेधापवादोऽयम्",
            "the second member of a compound begins a pada")),),
        "8.3.95": (("8.3.111", _quote(
            "balamanorama", "8.3.95", "निषेधे प्राप्ते इदमारभ्यते")),),
        "8.3.85": (("8.3.84", _quote(
            "balamanorama", "8.3.85", "पूर्वण नित्ये प्राप्ते विकल्पोऽयम्")),),
    }
    for cp in _CPS:
        finder = _cp_finder(cp)
        finder.__doc__ = docs.get(cp.sutra)
        _operative(cp.sutra, overrides=overrides.get(cp.sutra, ()),
                   vedic=cp.sutra in _VEDIC)(finder)


_VEDIC = frozenset({"8.3.105", "8.3.106", "8.3.107", "8.3.109"})
_CP_DOC: Dict[str, str] = {}


# -- words laid down whole: 8.3.90 – 8.3.94, 8.3.98 --------------------------


def _run(v: View, w: int) -> range:
    """The pieces joined to piece `w` inside one pada or compound."""
    bounds = v.state.bounds
    low = high = w
    while low > 0 and bounds[low - 1] in INSIDE:
        low -= 1
    while high < len(v.state.words) - 1 and bounds[high] in INSIDE:
        high += 1
    return range(low, high + 1)


@lru_cache(maxsize=None)
def _nasals() -> FrozenSet[str]:
    return frozenset(g[-1] for g in VARGA.values()) | {"ṃ"}


@lru_cache(maxsize=None)
def _stem_sounds(stem: str) -> Tuple[str, ...]:
    return tuple(sound for sound, _ in tokenize(stem))


def _match_whole(stem: Tuple[str, ...], sounds: Sequence[str],
                 *, cerebral: bool) -> Optional[List[int]]:
    """
    Whether `sounds` are the laid-down word `stem` (with at most two sounds of
    ending after it), and where: the places at which the stem has a ष् and the
    input a स् (`cerebral`), which is what a nipātana does. Where the stem has a
    ण् for the input's न् (the natva that follows) or a visarga for its
    स्/र्, the two agree and nothing is done there.
    """
    extra = len(sounds) - len(stem)
    if extra < 0 or extra > 2:
        return None
    marks: List[int] = []
    for i, want in enumerate(stem):
        got = sounds[i]
        if got == want:
            continue
        if cerebral and want in _murdhanya() and _dental_of(want) == got:
            if got == "s":
                marks.append(i)
            continue
        if want == VISARGA and got in ("s", "r"):
            continue
        if want == "ṃ" and got in _nasals():
            continue
        return None
    return marks


def _laid_finder(sutra: str, stems: Sequence[str], *,
                 sense: Sequence[str] = ()) -> Finder:
    prepared = [(stem, _stem_sounds(stem)) for stem in stems]

    def find(v: View):
        words = v.state.words
        seen = set()
        for w in range(len(words)):
            if w in seen:
                continue
            run = _run(v, w)
            seen.update(run)
            if len(run) < 2:
                continue
            if sense and not any(_senses(words[i]) & set(_sense_of(sense))
                                 for i in run):
                continue
            head = _first_sight(v, run[0])
            if head is None:
                continue
            unit = v.unit_of(head, across=INSIDE)
            sounds = [x.s for x in unit]
            for stem, stem_sounds in prepared:
                marks = _match_whole(stem_sounds, sounds, cerebral=True)
                for i in marks or ():
                    s = unit[i]
                    if not _standing(v, s):
                        continue
                    yield _hit(
                        sutra, s, None,
                        f"the pieces make up {sk(stem)}, a word the sūtra "
                        f"lays down with {sk(_cerebral('s'))}: its {sk('s')} is "
                        f"not made by a rule but fixed as a form, so it "
                        f"becomes {sk(_cerebral('s'))}",
                        ink=False, nimitta_text=f"the whole word {sk(stem)} "
                        f"is laid down ({{nipātana}})",
                        note="निपातन — the form is laid down whole; no cause "
                             "is asked of the sounds before it",
                        info={"stem": stem})

    return find


def _register_laid() -> None:
    for sutra in ("8.3.90", "8.3.91", "8.3.92", "8.3.93", "8.3.94"):
        row = _row(sutra)
        finder = _laid_finder(sutra, row.of, sense=row.sense)
        finder.__doc__ = _LAID_DOC[sutra]
        _operative(sutra)(finder)
    gana = corpus.ganas_for("8.3.98")[0]
    finder = _laid_finder("8.3.98", [x for x in gana.items if "ṣ" in x])
    finder.__doc__ = _LAID_DOC["8.3.98"]
    _operative("8.3.98", overrides=(
        ("8.3.111", _quote("kashika", "8.3.98",
                           "इति वा प्रतिषेधबाधनार्थः")),))(finder)


_LAID_DOC: Dict[str, str] = {}


# -- 8.3.87: अस् after a preverb --------------------------------------------


@_operative("8.3.87")
def _f87(v: View):
    """
    उपसर्गप्रादुर्भ्यामस्तिर्यच्परः — the स् of अस् (its अ lost: सन्ति, स्यात्) after a
    preverb's इण् or after प्रादुस्, when a य् or a vowel follows: अभिषन्ति, निषन्ति,
    अभिष्यात्, निष्यात्, प्रादुःषन्ति.

    Reads: `dhatu:asti` (or `as`) on the piece — the स् only, an अ having been
    lost; the preverb by `|`; प्रादुस् as a first member (text `prādus`). Not
    दधि स्यात् (उपसर्गादिति किम्), not अनुसृतम् (अस्तीति किम्: the root is सृ), not
    निस्तः (यच्पर इति किम्: a त् follows). Not the preverb's own स् — परस्येति
    is said of the स् of अस् (प्रादुरासीदित्यत्र न षत्वम्, Bālamanoramā).
    """
    words = v.state.words
    for w, word in enumerate(words):
        if _root_named(word, ("asti",)) is None:
            continue
        s = _first_sight(v, w)
        if s is None or s.s != "s" or not _standing(v, s):
            continue
        nxt = v.next(s)
        if nxt is None or not (nxt.s == "y" or nxt.s in AC):
            continue
        reach = _reach(v, s)
        n = reach.nimitta
        if n is None or n.s not in _ink():
            continue
        u = _upasarga_index(v, n)
        if u is not None:
            up_text = words[u].text
            if _up_in(up_text, NOT_UPASARGA_HERE):
                continue
        else:
            owners = [i for i in _words_of(n)
                      if _loose(words[i].text) == _loose("prādus")]
            if not owners:
                continue
            up_text = words[owners[0]].text
        yield _hit(
            "8.3.87", s, reach,
            f"{sk(s.s)} is the स् of {sk('as')} (its {sk('a')} lost), it "
            f"stands after {sk(up_text)}, and "
            + ("a {y} follows" if nxt.s == "y" else "a vowel follows")
            + f"; {_nimitta_text(s, reach)}, so it becomes "
            f"{sk(_cerebral('s'))}",
            ku=False, info={"root": "asti", "w": w, "upasarga": up_text})


# -- 8.3.99, 8.3.100: सेन ... in a name ------------------------------------


def _eti_finder(sutra: str, *, nakshatra: bool) -> Finder:
    name_sense = _sense_of(_row("8.3.99").sense)

    def find(v: View):
        words, bounds = v.state.words, v.state.bounds
        for w in range(1, len(words)):
            if bounds[w - 1] != SAMASA:
                continue
            first, second = words[w - 1], words[w]
            if not ((_senses(first) | _senses(second)) & set(name_sense)):
                continue
            if ("nakṣatra" in _senses(first)) != nakshatra:
                continue
            s = _first_sight(v, w)
            if s is None or s.s != "s" or not _standing(v, s):
                continue
            nxt = v.next(s)
            if nxt is None or nxt.s != "e":
                continue
            reach = _reach(v, s)
            n = reach.nimitta
            if (n is None or not _is_cause(n) or (w - 1) not in _words_of(n)
                    or n.s == "g"):
                continue
            yield _hit(
                sutra, s, reach,
                f"{sk(s.s)} begins {sk(second.text)}, a name after "
                f"{sk(first.text)}; an {sk('e')} follows it, "
                f"{_nimitta_text(s, reach)}, and that sound is not a "
                f"{sk('g')} (अगात्), so it becomes {sk(_cerebral('s'))}",
                optional="वा" if nakshatra else "",
                info={"w": w, "first": first.text, "second": second.text})

    return find


# -- 8.3.101 -----------------------------------------------------------------


@_operative("8.3.101")
def _f101(v: View):
    """
    ह्रस्वात् तादौ तद्धिते — the स् after a SHORT इण् before a त-initial taddhita:
    सर्पिष्टरम्, यजुष्टमम्, सर्पिष्ट्वम्, सर्पिष्टः, चतुष्टये.

    Reads: `taddhita` on the affix piece (joined by `~`), whose first sound is
    त्; the स् is the last sound of the stem before it. Not गीस्तरा, धूस्तरा (ह्रस्वादिति
    किम्: a long vowel), not सर्पिस्साद् (तादाविति किम्), not सर्पिस्तरति (तद्धित इति
    किम्: no taddhita follows). With a तिङन्त, भिन्द्युस्तराम्, the vārttika refuses.
    """
    for s in v.live:
        if s.s != "s" or not v.ends_word(s):
            continue
        nxt_word = _next_piece(v, s.w)
        if nxt_word is None or not _has(nxt_word, TADDHITA):
            continue
        t = _first_sight(v, s.w + 1)
        if t is None or t.s != "t" or not _standing(v, s):
            continue
        reach = _reach(v, s)
        n = reach.nimitta
        if n is None or n.s not in _ink() or not is_hrasva(n.s):
            continue
        yield _hit(
            "8.3.101", s, reach,
            f"{sk(s.s)} ends the stem before the taddhita {sk(nxt_word.text)}, "
            f"which begins with {sk('t')}; the sound before is a short "
            f"{{iṇ}}, {sk(n.s)}, so it becomes {sk(_cerebral('s'))}",
            ku=False, nimitta_text=f"a short {{iṇ}} {sk(n.s)} stands before "
            f"{sk(s.s)}", info={"w": s.w})


# -- 8.3.102 -----------------------------------------------------------------


@_operative("8.3.102")
def _f102(v: View):
    """
    निसस्तपतावनासेवने — the स् of निस् before तप्, where the doing is not repeated:
    निष्टपति सुवर्णम् (he puts the gold to the fire once). Repeated, निस्तपति.

    Reads: `dhatu:tap` on the root with `sense:anāsevana`, the preverb निस् before
    it by `|`. At this moment the preverb has only joined its root and is not yet
    a pada (पूर्वं धातुरुपसर्गेण युज्यते, Kaumudī on 8.3.74), so its final स् is
    reached though the engine counts a preverb's end as a pada's.
    """
    words = v.state.words
    for w in range(1, len(words)):
        if v.state.bounds[w - 1] not in (UPASARGA, ANGA):
            continue
        root = words[w]
        if _root_named(root, ("tap",)) is None:
            continue
        if "anāsevana" not in _senses(root):
            continue
        if _loose(words[w - 1].text) != _loose("nis"):
            continue
        sights = v.word_sights(w - 1)
        s = sights[-1] if sights else None
        if s is None or s.s != "s" or not _standing(v, s, upasarga_end=True):
            continue
        reach = _reach(v, s)
        n = reach.nimitta
        if n is None or n.s not in _ink() or (w - 1) not in _words_of(n):
            continue
        yield _hit(
            "8.3.102", s, reach,
            f"{sk(s.s)} ends the preverb {sk('nis')}, before the root "
            f"{sk('tap')} used of a doing that is not repeated "
            f"({{anāsevana}}); {_nimitta_text(s, reach)}, so it becomes "
            f"{sk(_cerebral('s'))}",
            ku=False, info={"w": w - 1})


# -- 8.3.107 (Vedic): सुञ् ------------------------------------------------


@_operative("8.3.107", vedic=True)
def _f107(v: View):
    """
    सुञः — in the Veda, the particle सु after a first member's इण्: अभी षु णः
    सखीनाम्, ऊर्ध्व ऊ षु ण ऊतये.

    Reads: `nipata` on the piece `su` (a word of its own; the sound before it may
    stand across a word boundary — the sūtra says पूर्वपदात्). Runs only when the
    caller says the text is Vedic.
    """
    for w, word in enumerate(v.state.words):
        if w == 0 or not _has(word, NIPATA) or _canon(word.text) != "su":
            continue
        s = _first_sight(v, w)
        if s is None or s.s != "s" or not _standing(v, s):
            continue
        reach = _reach(v, s)
        n = reach.nimitta
        if n is None or n.s not in _ink():
            continue
        yield _hit(
            "8.3.107", s, reach,
            f"{sk('s')} is the particle {sk('su')} ({{suñ}}), after a first "
            f"member; {_nimitta_text(s, reach)}, so it becomes "
            f"{sk(_cerebral('s'))}",
            ku=False, info={"w": w})


# -- 8.3.106 (Vedic) ---------------------------------------------------------


@_operative("8.3.106", vedic=True)
def _f106(v: View):
    """
    पूर्वपदात् — in the Veda, some teachers hold, the स् beginning an uttarapada
    after a first member's इण् or कु: द्विषन्धिः / द्विसन्धिः, मधुष्ठानम् / मधुस्थानम्.

    Reads: `uttarapada` on the second member (a piece of a compound joined by
    `-`), and asks for the cause in the first. An option (एकेषाम् — a named
    school's view). Runs only for Vedic text.
    """
    words, bounds = v.state.words, v.state.bounds
    for w in range(1, len(words)):
        if bounds[w - 1] != SAMASA or not _has(words[w], "uttarapada"):
            continue
        s = _first_sight(v, w)
        if s is None or s.s != "s" or not _standing(v, s):
            continue
        reach = _reach(v, s)
        n = reach.nimitta
        if n is None or not _is_cause(n) or (w - 1) not in _words_of(n):
            continue
        yield _hit(
            "8.3.106", s, reach,
            f"{sk('s')} begins the uttarapada {sk(words[w].text)}; "
            f"{_nimitta_text(s, reach)}, so it becomes {sk(_cerebral('s'))} "
            f"(some teachers' view)",
            optional="एकेषाम्", info={"w": w})

def _register_eti() -> None:
    docs = {
        "8.3.99": """
    एति संज्ञायामगात् — the स् before an ए in a NAME, after an इण् or a कु other
    than ग्: हरिषेणः, वारिषेणः, जानुषेणी.

    Reads: `sense:saṃjñā` on one of the two members (the caller says it is a
    name; meaning is not computed — पृथुसेनः is no name), the members joined by
    `-`. Not हरिसक्थम् (एतीति किम्: no ए follows), not सर्वसेनः (इण्कोरित्येव), not
    विष्वक्सेनः (अगकारादिति किम्): the cause the sūtra excludes is the ग् the word
    ends in — give विष्वग्, for 8.4.55's क् is asiddha to this sūtra (8.2.1).
    """,
        "8.3.100": """
    नक्षत्राद्वा — the same, optional, after the name of a constellation:
    रोहिणीषेणः / रोहिणीसेनः, भरणीषेणः / भरणीसेनः.

    Reads: `sense:nakṣatra` on the first member, `sense:saṃjñā` as in 8.3.99. An
    option of the प्राप्तविभाषा kind: it takes the place of 8.3.99 in this case
    (8.3.99 stands aside here rather than returning when the option is
    declined). The exception for ग् is carried down (अगकारादित्येव —
    शतभिषक्सेनः has neither form).
    """}
    reason = _quote(
        "kashika", "8.3.100",
        "नक्षत्रवाचिनः शब्दादुत्तरस्य सकारस्य वा एति संज्ञायामगकाराद् "
        "मूर्धन्यो भवति")
    for sutra, nak in (("8.3.99", False), ("8.3.100", True)):
        finder = _eti_finder(sutra, nakshatra=nak)
        finder.__doc__ = docs[sutra]
        _operative(sutra, overrides=(("8.3.99", reason),) if nak else ())(
            finder)


# ---------------------------------------------------------------------------
# The refusals: 8.3.61, 8.3.62, 8.3.75, 8.3.110 – 8.3.119
# ---------------------------------------------------------------------------


def _chain_after(v: View, w: int) -> Iterator[Tuple[int, Word]]:
    """The pieces after piece `w`, joined to it by `~`, nearest first."""
    words, bounds = v.state.words, v.state.bounds
    j = w
    while j + 1 < len(words) and bounds[j] == ANGA:
        j += 1
        yield j, words[j]


def _affix_after(v: View, w: int, names: Sequence[str]) -> bool:
    wanted = {_canon(n) for n in names}
    return any({_canon(x) for x in _values(word, PRATYAYA)} & wanted
               for _, word in _chain_after(v, w))


def _root_piece(v: View, hit: Hit) -> Optional[int]:
    """The root a hit belongs to: its own piece if that is a root, or the root
    after its reduplicative syllable."""
    w = hit.s.w
    word = v.state.words[w]
    if _has(word, DHATU):
        return w
    if _has(word, ABHYASA):
        nxt = _next_piece(v, w)
        if nxt is not None and _has(nxt, DHATU):
            return w + 1
    return None


def _sanbhuta(v: View, w: int) -> bool:
    """A सन् that is षभूत (8.3.61, 8.3.62): its स् is a ष् — or is one that 8.3.59
    is about to make, an इण् or कु standing before it."""
    for j, word in _chain_after(v, w):
        if "san" not in {_canon(x) for x in _values(word, PRATYAYA)}:
            continue
        s = next((x for x in v.word_sights(j) if x.s in ("s", "ṣ")), None)
        if s is None:
            return False
        if s.s == "ṣ":
            return True
        reach = _reach(v, s)
        return reach.nimitta is not None and _is_cause(reach.nimitta)
    return False


def _from_abhyasa(v: View, hit: Hit) -> bool:
    n = hit.reach.nimitta if hit.reach is not None else None
    return n is not None and _in_piece(v, n, ABHYASA)


def _check_61(v: View, hit: Hit) -> Optional[str]:
    word = v.word(hit.s)
    if not (_from_abhyasa(v, hit) and _has(word, DHATU)):
        return None
    if _root_named(word, ("stu",)) is not None or _has(word, NYANTA):
        return None
    if not _sanbhuta(v, hit.s.w):
        return None
    return ("the cause is the reduplicative syllable's इण् and a षभूत सन् "
            "follows, but the cerebral is kept for स्तु and the णिजन्त roots "
            "alone (स्तौतिण्योरेव षण्यभ्यासात्) — this root is neither")


def _check_62(v: View, hit: Hit) -> Optional[str]:
    word = v.word(hit.s)
    if not (_from_abhyasa(v, hit) and _has(word, DHATU)
            and _has(word, NYANTA)):
        return None
    root = _root_named(word, _row("8.3.62").of)
    if root is None or not _sanbhuta(v, hit.s.w):
        return None
    return (f"the root {sk(root)} in its णिजन्त form, after its reduplicative "
            f"syllable and before a षभूत सन्, keeps a plain {sk('s')} "
            f"(सस्य सकारवचनं मूर्धन्यनिवृत्त्यर्थम्)")


def _check_110(v: View, hit: Hit) -> Optional[str]:
    nxt = v.next(hit.s)
    if nxt is not None and nxt.s == "r":
        return f"a repha ({sk('r')}) follows the {sk('s')} (रेफपर)"
    roots = tuple(x for x in _row("8.3.110").of if x in ROOT_NAMES)
    root = _root_named(v.word(hit.s), roots)
    if root is not None:
        return f"the {sk('s')} belongs to the root {sk(root)}, which the sūtra names"
    listed = _in_savanadi(v, hit)
    if listed:
        return f"the {sk('s')} lies in {sk(listed)}, a word of the सवनादि gaṇa"
    return None


def _in_savanadi(v: View, hit: Hit) -> Optional[str]:
    """The word of the सवनादि gaṇa (gaṇapāṭha) the स् stands in, if any."""
    live = list(v.live)
    sounds = [x.s for x in live]
    at = next((i for i, x in enumerate(live) if x.uid == hit.s.uid), None)
    if at is None:
        return None
    for gana in corpus.ganas_for("8.3.110"):
        for item in gana.items:
            want = _stem_sounds(item)
            n = len(want)
            for start in range(max(0, at - n + 1), at + 1):
                if tuple(sounds[start:start + n]) == want:
                    return item
    return None


def _check_111(v: View, hit: Hit) -> Optional[str]:
    words, bounds = v.state.words, v.state.bounds
    w = hit.s.w
    if _canon(words[w].text) == "sāt" and v.begins_word(hit.s):
        return (f"the {sk('s')} is the {sk('s')} of the affix {sk('sāt')} "
                f"({{sāt}}), which the sūtra names")
    if v.begins_word(hit.s) and w > 0 and bounds[w - 1] in (PADA, SAMASA):
        return (f"the {sk('s')} begins a pada ({{padādi}}): a "
                f"{'compound member' if bounds[w - 1] == SAMASA else 'word'} "
                f"that was a pada of its own")
    return None


def _check_112(v: View, hit: Hit) -> Optional[str]:
    w = _root_piece(v, hit)
    if w is None or _root_named(v.state.words[w], ("sic",)) is None:
        return None
    if not _affix_after(v, w, ("yaṅ",)):
        return None
    return (f"the root {sk('sic')} stands before {sk('yaṅ')}")


def _check_113(v: View, hit: Hit) -> Optional[str]:
    w = _root_piece(v, hit)
    if w is None:
        return None
    word = v.state.words[w]
    if _root_named(word, ("sedha",)) is None:
        return None
    if _row("8.3.113").sense[0] not in _senses(word):
        return None
    return f"the root {sk('sedh')} is used of MOTION ({{gati}}), driving cattle"


def _check_114(v: View, hit: Hit) -> Optional[str]:
    unit = v.unit_of(hit.s, across=INSIDE)
    sounds = [x.s for x in unit]
    for stem in _row("8.3.114").of:
        if _match_whole(_stem_sounds(stem), sounds, cerebral=False) is not None:
            return (f"the word {sk(stem)} is laid down without the cerebral "
                    f"(a निपातन)")
    return None


def _check_115(v: View, hit: Hit) -> Optional[str]:
    w = _root_piece(v, hit)
    if w is None:
        return None
    word = v.state.words[w]
    if _root_named(word, ("sah",)) is None:
        return None
    if not _canon(word.text).startswith("soḍh"):
        return None
    return f"the root {sk('sah')} stands in the shape {sk('soḍh')}"


def _check_116(v: View, hit: Hit) -> Optional[str]:
    w = _root_piece(v, hit)
    if w is None:
        return None
    if _root_named(v.state.words[w], _row("8.3.116").of) is None:
        return None
    if not _affix_after(v, w, ("caṅ",)):
        return None
    n = hit.reach.nimitta if hit.reach is not None else None
    if n is None or _in_piece(v, n, ABHYASA) or _upasarga_index(v, n) is None:
        return None
    return (f"the root stands before {sk('caṅ')}, and the cause is the "
            f"preverb's (उपसर्गाद् या प्राप्तिस्तस्या एव प्रतिषेधः)")


def _check_117(v: View, hit: Hit) -> Optional[str]:
    w = _root_piece(v, hit)
    if w is None or _root_named(v.state.words[w], ("sunoti",)) is None:
        return None
    if not _affix_after(v, w, _row("8.3.117").before):
        return None
    return f"the root {sk('su')} stands before {sk('sya')} or {sk('san')}"


def _check_118(v: View, hit: Hit) -> Optional[str]:
    w = _root_piece(v, hit)
    if w is None or hit.s.w != w or w == 0:
        return None
    if not _has(v.state.words[w - 1], ABHYASA):
        return None
    if _root_named(v.state.words[w], ("sad", "svañja")) is None:
        return None
    if not _affix_after(v, w, ("liṭ",)):
        return None
    return (f"the root is in the perfect ({{liṭ}}), and this is the LATER "
            f"{sk('s')} — the root's, after the reduplication (परस्य)")


def _check_119(v: View, hit: Hit) -> Optional[str]:
    if hit.reach is None or "at" not in hit.reach.kinds:
        return None
    up = hit.info.get("upasarga")
    if not up or not _up_in(str(up), _labels("8.3.119")):
        return None
    return (f"the {sk('s')} would be reached across the augment {sk('aṭ')} "
            f"after {sk(str(up))}, in Vedic text — where this reach is optional")


def _check_75(v: View, hit: Hit) -> Optional[str]:
    words = v.state.words
    run = _run(v, hit.s.w)
    if not any(_row("8.3.75").sense[0] in _senses(words[i]) for i in run):
        return None
    unit = v.unit_of(hit.s, across=INSIDE)
    sounds = [x.s for x in unit]
    for stem in _row("8.3.75").of:
        if _match_whole(_stem_sounds(stem), sounds, cerebral=False) is not None:
            return (f"the word {sk(stem)} is laid down without the cerebral "
                    f"among the eastern Bharatas (a निपातन)")
    return None


def _check_101v(v: View, hit: Hit) -> Optional[str]:
    if _has(v.state.words[hit.s.w], "tinanta"):
        return "the stem is a तिङन्त (भिन्द्युस्तराम्)"
    return None


def _refusal(sutra: str, victims: Callable[[], Sequence[str]], check, *,
             reason: str, targets: Sequence[str], vedic: bool = False,
             optional: str = "", authority: str = "sūtra",
             varttika: str = "", doc: str = ""):
    """Register a refusal: an application with no edit, at the SITE of what it
    refuses, winning by `overrides` (see 8.4.44 in hal_assimilation)."""

    def find(v: View):
        if not _live(v):
            return
        offered = set()
        for victim in victims():
            for hit in FINDERS[victim](v):
                # A sound that a later rule has already changed is seen by this
                # rule through its past (8.2.1): there is nothing here to refuse.
                if hit.site in offered or hit.s.through:
                    continue
                why = check(v, hit)
                if not why:
                    continue
                offered.add(hit.site)
                yield Application(
                    site=hit.site, edits=(),
                    detail=Detail(
                        kind=PRATISEDHA, sthanin=hit.s.s, adesa="",
                        nimitta=hit.nimitta_text,
                        because=(f"{hit.sutra} would make {sk(hit.s.s)} into "
                                 f"{sk(hit.sub)} here, but {why}, so it stays "
                                 f"{sk(hit.s.s)}"),
                        via=(Via(hit.sutra, f"would have applied here: "
                                            f"{hit.because}"),),
                        authority=authority, varttika=varttika),
                    optional=optional)

    find.__doc__ = doc
    built = rule(sutra, name=_name(sutra), families=REFUSAL_FAMILIES,
                 overrides=tuple((t, reason) for t in targets), vedic=vedic,
                 authority=authority, varttika=varttika)(find)
    _RULES.append(built)
    return built


def _all_operative() -> Tuple[str, ...]:
    return tuple(FINDERS)


_REFUSAL_DOC: Dict[str, str] = {}


def _register_refusals() -> None:
    doc = _REFUSAL_DOC.get
    _refusal(
        "8.3.61", lambda: ("8.3.59",), _check_61, targets=("8.3.59",),
        reason=_quote("kashika", "8.3.61", "सिद्धे सत्यारम्भो नियमार्थः"),
        doc=doc("8.3.61"))
    _refusal(
        "8.3.62", lambda: ("8.3.59",), _check_62, targets=("8.3.59",),
        reason=_quote("kashika", "8.3.62",
                      "सकारस्य सकारवचनं मूर्धन्यनिवृत्त्यर्थम्"),
        doc=doc("8.3.62"))
    _refusal(
        "8.3.75", lambda: ("8.3.74",), _check_75, targets=("8.3.74",),
        reason=_quote("kashika", "8.3.75",
                      "पूर्वेण मूर्धन्ये प्राप्ते तदभावो निपात्यते"),
        doc=doc("8.3.75"))
    _refusal(
        "8.3.110", _all_operative, _check_110, targets=("@satva",),
        reason=_quote(
            "kaumudi", "8.3.110", "इति वृत्तिर्भूयोऽभिप्राया",
            "the vṛtti names 8.3.106's cerebral, and means more: every one "
            "before it"),
        doc=doc("8.3.110"))
    _refusal(
        "8.3.111", lambda: ("8.3.59",), _check_111, targets=("8.3.59",),
        reason=_quote("kashika", "8.3.111",
                      "प्रत्ययसकारत्वात् प्राप्तिः, पदादेश्चादेशसकारत्वात्"),
        doc=doc("8.3.111"))
    _refusal(
        "8.3.112", _all_operative, _check_112, targets=("@satva",),
        reason=_quote("kashika", "8.3.112",
                      "तस्मादयं प्रतिषेधः सर्वत्र भवति"),
        doc=doc("8.3.112"))
    _refusal(
        "8.3.113", lambda: ("8.3.65",), _check_113, targets=("8.3.65",),
        reason=_quote(
            "kashika", "8.3.113",
            "गतौ वर्तमानस्य सेधतेः सकारस्य मूर्धन्यादेशो न भवति"),
        doc=doc("8.3.113"))
    _refusal(
        "8.3.114", lambda: ("8.3.67",), _check_114, targets=("8.3.67",),
        reason=_quote("kashika", "8.3.114",
                      "इति प्राप्तं षत्वं प्रतिषिध्यते"),
        doc=doc("8.3.114"))
    _refusal(
        "8.3.115", lambda: ("8.3.70",), _check_115, targets=("8.3.70",),
        reason=_quote(
            "kashika", "8.3.115",
            "सहिरयं सोड्भूतो गृह्यते, तस्य सकारस्य मूर्धन्यादेशो न भवति"),
        doc=doc("8.3.115"))
    _refusal(
        "8.3.116", lambda: ("8.3.67", "8.3.70", "8.3.71"), _check_116,
        targets=("8.3.67", "8.3.70", "8.3.71"),
        reason=_quote("kashika", "8.3.116",
                      "इति च प्राप्तो मूर्धन्यः प्रतिषिध्यते"),
        doc=doc("8.3.116"))
    _refusal(
        "8.3.117", lambda: ("8.3.65",), _check_117, targets=("8.3.65",),
        reason=_quote(
            "kashika", "8.3.117",
            "सुनोतेः सकारस्य मूर्धन्योदेशो न भवति स्ये सनि च परतः"),
        doc=doc("8.3.117"))
    _refusal(
        "8.3.118", lambda: ("8.3.65", "8.3.66", "8.3.70", "8.3.71"),
        _check_118, targets=("8.3.65", "8.3.66", "8.3.70", "8.3.71"),
        reason=_quote("kashika", "8.3.118",
                      "सकारस्य परस्य मूर्धन्यो न भवति"),
        doc=doc("8.3.118"))
    _refusal(
        "8.3.119", lambda: ("8.3.65", "8.3.66", "8.3.67", "8.3.68", "8.3.69",
                            "8.3.70", "8.3.71"), _check_119,
        targets=("8.3.65", "8.3.66", "8.3.67", "8.3.68", "8.3.69", "8.3.70",
                 "8.3.71"),
        reason=_quote("kashika", "8.3.119",
                      "मूर्दह्न्यादेशो न भवति वा"),
        vedic=True, optional="वा", doc=doc("8.3.119"))

def _register_varttika_101() -> None:
    text = "तिङन्तस्य प्रतिषेधो वक्तव्यः"
    _refusal(
        "8.3.101", lambda: ("8.3.101",), _check_101v, targets=("8.3.101",),
        reason=_quote("kashika", "8.3.101", text), authority=VARTTIKA,
        varttika=text,
        doc="""
    ह्रस्वात् तादौ तद्धिते, वार्त्तिकम् — तिङन्तस्य प्रतिषेधो वक्तव्यः: भिन्द्युस्तराम्,
    छिन्द्युस्तराम्. Reads: `tinanta` on the stem's piece (a verb form).""")


# ---------------------------------------------------------------------------
# What each rule is, in words
# ---------------------------------------------------------------------------

_PV_DOC.update({
    "8.3.65": """
    उपसर्गात् सुनोतिसुवतिस्यतिस्तौतिस्तोभतिस्थासेनयसेधसिचसञ्जस्वञ्जाम् — the स् of
    eleven roots after a PREVERB's इण्: अभिषुणोति, अभिषुवति, अभिष्यति, अभिष्टौति,
    अभिष्टोभते, अभिष्ठास्यति, अभिषेणयति, अभिषेधति, अभिषिञ्चति, अभिषजति, अभिष्वजते;
    and across the augment अट् (8.3.63): अभ्यषुणोत्, पर्यषेधत्.

    Reads: `dhatu:ROOT` on the root piece — the sūtra's own word (`sunoti`,
    `sedha`, …) or the dhātupāṭha's (`ROOT_NAMES`); the preverb before it by `|`
    (or the flag `upasarga`); the augment by `at`. The cause must be an इण् in
    the preverb (`koḥ` cannot reach a preverb: असम्भवात्, Bālamanoramā). Not दधि
    सिञ्चति (उपसर्गादिति किम्: दधि is no preverb); not दुःसुनोति (the vārttika
    दुरः षत्वणत्वयोरुपसर्गत्वप्रतिषेधः on 1.4.60: दुस् is not a preverb here); not
    प्रति…सीदति (that is 8.3.66). The root is named by its śap/śnu form: सेध इति
    शब्विकरणनिर्देशः सिध्यतिनिवृत्त्यर्थः — only the bhvādi root.
    """,
    "8.3.66": """
    सदिरप्रतेः — the स् of सद् after a preverb other than प्रति: निषीदति, विषीदति,
    न्यषीदत्, व्यषीदत्, निषसाद, विषसाद. Reads: `dhatu:sad`, the preverb by `|`, `at`
    for the augment. Not प्रतिसीदति (अप्रतेरिति किम्).
    """,
    "8.3.67": """
    स्तम्भेः — the स् of स्तम्भ् after a preverb: अभिष्टभ्नाति, परिष्टभ्नाति,
    अभ्यष्टभ्नात्, पर्यष्टभ्नात्, अभितष्टम्भ. Reads: `dhatu:stambh` (the root the
    sūtra writes with न्: स्तन्भुस्तुन्भु), the preverb by `|`. अप्रतेः is NOT carried
    here (योगविभाग उत्तरार्थः, Kaumudī): प्रतिष्टभ्नाति, प्रत्यष्टभ्नात्.
    """,
    "8.3.68": """
    अवाच्चालम्बनाविदूर्ययोः — the स् of स्तम्भ् after अव, where SUPPORT or NEARNESS
    is meant: अवष्टभ्यास्ते, अवष्टब्धा सेना. अवस्तब्धो वृषलः शीतेन — neither.

    Reads: `dhatu:stambh` with `sense:ālambana` or `sense:āvidūrya`, the preverb अव
    by `|`. No इण् is asked (अपूर्वविधिरयम्, इणः परत्वाऽभावादप्राप्तेः — अव ends in अ).
    """,
    "8.3.69": """
    वेश्च स्वनो भोजने — the स् of स्वन् after वि and अव where EATING is meant:
    विष्वणति, व्यष्वणत्, अवष्वणति. विस्वनति मृदङ्गः (भोजन इति किम्).

    Reads: `dhatu:svan` with `sense:bhojana`, the preverb वि or अव by `|`.
    """,
    "8.3.70": """
    परिनिविभ्यः सेवसितसयसिवुसहसुट्स्तुस्वञ्जाम् — the स् of eight roots after परि,
    नि, वि: परिषेवते, निषेवते, विषेवते, पर्यषेवत, परिषितः, परिषयः, परिषीव्यति,
    परिषहते, परिष्करोति, परिष्टौति, परिष्वजते.

    Reads: `dhatu:ROOT` (सेव्, सित, सय, सिवु, सह, सुट् — the piece is the augment,
    written `dhatu:suṭ` — स्तु, स्वञ्ज), the preverb by `|`. Across the augment अट्
    only सेव् reaches (8.3.63 stops at *sita*); for the five of 8.3.71 the augment
    case is left to that sūtra.
    """,
    "8.3.71": """
    सिवादीनां वाऽड्व्यवायेऽपि — for सिवु, सह, सुट्, स्तु, स्वञ्ज after परि, नि, वि the
    cerebral reaches across the augment अट् OPTIONALLY: पर्यषीव्यत् / पर्यसीव्यत्,
    पर्यषहत / पर्यसहत, पर्यष्करोत् / पर्यस्करोत्, पर्यष्टौत् / पर्यस्तौत्,
    पर्यष्वजत / पर्यस्वजत.

    Reads what 8.3.70 reads, and `at`. An option of the प्राप्तविभाषा kind for स्तु
    and स्वञ्ज (8.3.65 had given it): those two are left out of 8.3.65's reach here,
    so that declining the option leaves the स्.
    """,
    "8.3.72": """
    अनुविपर्यभिनिभ्यः स्यन्दतेरप्राणिषु — the स् of स्यन्द् after अनु, वि, परि, अभि,
    नि, where what flows is not alive: OPTIONAL — अनुष्यन्दते / अनुस्यन्दते तैलम्.
    अनुस्यन्दते मत्स्य उदके (अप्राणिष्विति किम्; but a flow of both, अनुष्यन्देते
    मत्स्योदके, has it: पर्युदासोऽयम्, न प्रसज्यप्रतिषेधः).

    Reads: `dhatu:syand` with `sense:aprāṇi` (the caller says the subject is not,
    or not only, a living thing), the preverb by `|`.
    """,
    "8.3.73": """
    वेः स्कन्देरनिष्ठायाम् — the स् of स्कन्द् after वि, optionally, not before a
    निष्ठा: विष्कन्ता / विस्कन्ता, विष्कन्तुम्, विष्कन्तव्यम्; विस्कन्नः (a निष्ठा).

    Reads: `dhatu:skand`, the preverb वि by `|`, a `krt` affix after it (`~`) that
    is not `pratyaya:niṣṭhā` (कृत्येवेदम्, Kaumudī: not a tiṅ).
    """,
    "8.3.74": """
    परेश्च — the same after परि, optionally, and a निष्ठा is not excepted here
    (पृथग्योगकरणसामर्थ्यात्): परिष्कन्ता / परिस्कन्ता, परिष्कण्णः / परिस्कन्नः.

    Reads: `dhatu:skand`, the preverb परि by `|`.
    """,
    "8.3.76": """
    स्फुरतिस्फुलत्योर्निर्निविभ्यः — the स् of स्फुर्, स्फुल् after निस्, नि, वि,
    optionally: निष्ष्फुरति / निस्स्फुरति, निष्फुरति / निस्फुरति, विष्फुरति / विस्फुरति.

    Reads: `dhatu:sphur` or `dhatu:sphul`, the preverb by `|`.
    """,
    "8.3.77": """
    वेः स्कभ्नातेर्नित्यम् — the स् of स्कभ् after वि ALWAYS: विष्कभ्नाति, विष्कम्भिता,
    विष्कम्भितुम्. नित्यम् is said because the words about it are all optional.

    Reads: `dhatu:skabh`, the preverb वि by `|`.
    """,
})

_CP_DOC.update({
    "8.3.80": """
    समासेऽङ्गुलेः सङ्गः — the स् of सङ्ग after अङ्गुलि in a compound: अङ्गुलिषङ्गः,
    अङ्गुलिषङ्गा यवागूः. अङ्गुलेः सङ्गं पश्य (समास इति किम्): two words, no compound.

    Reads: the members as pieces joined by `-` (a compound), the first `aṅguli`
    and the second beginning `saṅga`.
    """,
    "8.3.81": """
    भीरोः स्थानम् — the स् of स्थान after भीरु in a compound: भीरुष्ठानम्. भीरोः
    स्थानं पश्य (समास इत्येव).
    """,
    "8.3.82": """
    अग्नेः स्तुत्स्तोमसोमाः — the स् of स्तुत्, स्तोम, सोम after अग्नि in a compound:
    अग्निष्टुत्, अग्निष्टोमः, अग्नीषोमौ. अग्नेर्दीर्घात् सोमस्येष्यते (Kāśikā): सोम
    takes it only after the LENGTHENED अग्नी — अग्निसोमौ माणवकौ does not.

    An अपवाद of 8.3.111's word-head refusal (इति षत्वनिषेधापवादोऽयम्).
    """,
    "8.3.83": """
    ज्योतिरायुषः स्तोमः — the स् of स्तोम after ज्योतिस्, आयुस्: ज्योतिष्टोमः,
    आयुष्टोमः. ज्योतिः स्तोमं दर्शयति (समास इत्येव). No इण् is asked of the
    member itself (नेह इण्कोरित्यनुवर्तते, व्याख्यानात् — Bālamanoramā).
    """,
    "8.3.84": """
    मातृपितृभ्यां स्वसा — the स् of स्वसृ after मातृ, पितृ in a compound: मातृष्वसा,
    पितृष्वसा. मातुः स्वसा (असमासे).
    """,
    "8.3.85": """
    मातुःपितुर्भ्यामन्यतरस्याम् — after the genitives मातुः, पितुः the same, OPTIONALLY:
    मातुःष्वसा / मातुःस्वसा. एकदेशविकृतस्यानन्यत्वात् visarga-final and स्-final alike
    (Kāśikā): the cerebral reaches across the visarga (8.3.58).
    """,
    "8.3.86": """
    अभिनिसः स्तनः शब्दसंज्ञायाम् — the स् of स्तन after अभिनिस्, optionally, where a
    SOUND is named: अभिनिष्टानो वर्णः / अभिनिस्तानो वर्णः. अभिनिस्स्तनति मृदङ्गः
    (शब्दसंज्ञायामिति किम्). Reads `sense:śabdasaṃjñā`. समास इत्यतः प्रभृति निवृत्तम् —
    the members need not be a compound.
    """,
    "8.3.88": """
    सुविनिर्दुर्भ्यः सुपिसूतिसमाः — the स् of सुपि, सूति, सम after सु, वि, निस्, दुस्:
    सुषुप्तः, विषुप्तः, निःषुप्तः, दुःषुप्तः; सुषूतिः; सुषमम्, विषमम्, निःषमम्, दुःषमम्.

    Reads: the members joined by `-` or `|`; `dhatu:supi` on the piece (स्वप् with its
    संप्रसारण made: सुपीति स्वपिः कृतसम्प्रसारणो गृह्यते); the words सूति, सम by their
    text.
    """,
    "8.3.89": """
    निनदीभ्यां स्नातेः कौशले — the स् of स्ना after नि, नदी where SKILL is meant:
    निष्णातः कटकरणे, नदीष्णः. निस्नातः (कौशल इति किम्).

    Reads: `dhatu:snā` with `sense:kauśala`, the members joined by `-` or `|`.
    """,
    "8.3.95": """
    गवियुधिभ्यां स्थिरः — the स् of स्थिर after गवि, युधि: गविष्ठिरः, युधिष्ठिरः. An
    अपवाद of 8.3.111's word-head refusal.
    """,
    "8.3.96": """
    विकुशमिपरिभ्यः स्थलम् — the स् of स्थल after वि, कु, शमि, परि: विष्ठलम्, कुष्ठलम्,
    शमिष्ठलम्, परिष्ठलम्.
    """,
    "8.3.97": """
    अम्बाम्बगोभूमिसव्यापद्वित्रिकुशेकुशङ्क्वङ्गुमञ्जिपुञ्जिपरमेबर्हिर्दिव्यग्निभ्यः स्थः —
    the स् of स्थ after eighteen first members: अम्बष्ठः, गोष्ठः, भूमिष्ठः, सव्येष्ठः,
    अपष्ठः, द्विष्ठः, कुष्ठः, अङ्गुष्ठः, परमेष्ठः, बर्हिष्ठः, अग्निष्ठः.

    स्थ is the FORM, not the root (Bhāṣya: स्थ इति किमिदं धातुग्रहणमाहो स्विद्रूपग्रहणम्?
    … अस्तु तावद्धातुग्रहणम् — the words गोस्थानम् etc. are met by the सवनादि gaṇa;
    Padamañjarī: स्थशब्दसकारस्येति), so स्थान is left alone. No इण् is asked: अम्ब,
    आम्ब, अप end in अ. The vārttika स्थास्थिन्स्थॄणाम् is not done (SCOPE).
    """,
    "8.3.105": """
    स्तुतस्तोमयोश्छन्दसि — in the Veda, some teachers hold, the स् of स्तुत, स्तोम
    after an इण् or कु: त्रिभिष्टुतस्य / त्रिभिस्तुतस्य, गोष्टोमम् / गोस्तोमम्.
    An option (एकेषाम्); runs only for Vedic text.
    """,
    "8.3.109": """
    सहेः पृतनर्ताभ्यां च — in the Veda, the स् of सह् after पृतना, ऋत: पृतनाषाहम्,
    ऋताषाहम्. Reads `dhatu:sah` on the second member. No इण् is asked (आ before).
    Runs only for Vedic text. The चकार's ऋतीषहम् is not done (SCOPE).
    """,
})

_LAID_DOC.update({
    "8.3.90": """
    सूत्रं प्रतिष्णातम् — प्रतिष्णातम् is laid down, where thread is meant: प्रतिष्णातं
    सूत्रम् (clean). प्रतिस्नातमित्येवान्यत्र. Reads: `sense:sūtra` and the pieces
    prati|snāta (a निपातन: the whole word is fixed, so no cause is asked).
    """,
    "8.3.91": """
    कपिष्ठलो गोत्रे — कपिष्ठल is laid down as a family name: कपिष्ठलो नाम स यस्य
    कापिष्ठलिः पुत्रः. कपेः स्थलं कपिस्थलम् (गोत्र इति किम्). Reads `sense:gotra`.
    """,
    "8.3.92": """
    प्रष्ठोऽग्रगामिनि — प्रष्ठ is laid down of one that goes in front: प्रतिष्ठत इति
    प्रष्ठोऽश्वः. प्रस्थे हिमवतः पुण्ये, प्रस्थो व्रीहीणाम् (अग्रगामिनीति किम्).
    Reads `sense:agragāmin`.
    """,
    "8.3.93": """
    वृक्षासनयोर्विष्टरः — विष्टर is laid down of a tree or a seat: विष्टरो वृक्षः,
    विष्टरमासनम्. औलपिवाक्यस्य विस्तरः (वृक्षासनयोरिति किम्). Reads `sense:vṛkṣa`
    or `sense:āsana`.
    """,
    "8.3.94": """
    छन्दोनाम्नि च — विष्टार is laid down as the name of a metre: विष्टारपङ्क्तिः
    छन्दः. पटस्य विस्तारः (छन्दोनाम्नीति किम्). Reads `sense:chandonāman`.
    """,
    "8.3.98": """
    सुषामादिषु च — the words of the सुषामादि gaṇa, laid down whole with their
    ष्: सुषामा, निष्षामा, दुष्षामा, सुषेधः, निष्षेधः, सुषन्धिः, दुष्ठु, गौरिषक्थः,
    प्रतिष्णिका, जलाषाहम्, नौषेचनम्, दुन्दुभिषेवणम्.

    The gaṇa is read from the gaṇapāṭha (`corpus.ganas_for`), the words that
    carry a ष्; the pieces are matched to a word sound by sound (a visarga for a
    स् or र्, a ष् for a स्, a ण् for a न् are the same word), and the स् goes
    where the word has a ष्. It is an आकृतिगण: only the words the gaṇapāṭha lists are
    known (SCOPE). An अपवाद of 8.3.111 (Kāśikā).
    """,
})

_REFUSAL_DOC.update({
    "8.3.61": """
    स्तौतिण्योरेव षण्यभ्यासात् — a NIYAMA: of the स् that would take ष् after the
    reduplicative syllable's इण् before a षभूत सन्, only the स् of स्तु and of the णिजन्त
    roots does (तुष्टूषति, सिषेचयिषति); सिसिक्षति, सुसूषते keep it. सिद्धे सत्यारम्भो
    नियमार्थः — 8.3.59 had reached them all, and this stands there to take the rest
    away. So the refusal is what it does here; the positive cases are 8.3.59's.

    Reads: `abhyasa` before the root, `nyanta` on the root, a `pratyaya:san` after
    it. Not from the preverb's इण् (अभ्यासादिति किम्: प्रतीषिषति, अधीषिषति — that ṣatva
    comes from another cause, which 8.3.64 restores across the syllable).
    """,
    "8.3.62": """
    सः स्विदिस्वदिसहीनां च — the णिजन्त of स्विद्, स्वद्, सह् keep the स्: सिस्वेदयिषति,
    सिस्वादयिषति, सिसाहयिषति. सकारस्य सकारवचनं मूर्धन्यनिवृत्त्यर्थम्. A refusal of
    8.3.59. Reads `dhatu:svid` (svad, sah) with `nyanta`, as 8.3.61.
    """,
    "8.3.75": """
    परिस्कन्दः प्राच्यभरतेषु — परिस्कन्द is laid down WITHOUT the cerebral among the
    eastern Bharatas; elsewhere परिष्कन्दः. पूर्वेण मूर्धन्ये प्राप्ते तदभावो निपात्यते.
    A refusal of 8.3.74's option. Reads `sense:prācyabharata`.
    """,
    "8.3.110": """
    न रपरसृपिसृजिस्पृशिस्पृहिसवनादीनाम् — no cerebral for a स् with a र् after it, nor
    for the स् of सृप्, सृज्, स्पृश्, स्पृह्, nor in the सवनादि gaṇa: विस्रब्धः कथयति,
    पुनःसृजति, निस्पृहं कथयति, उस्रा गौः (वस् before र), सवनेसवने.

    A refusal of every cerebralisation before it (the Kaumudī: इति वृत्तिर्भूयोऽभिप्राया
    — the vṛtti names 8.3.106's, and it means more), so it overrides `@satva`.
    """,
    "8.3.111": """
    सात्पदाद्योः — no cerebral for the स् of the affix सात्, nor for a स् that BEGINS a
    pada: अग्निसात्, दधिसात्, मधुसात्; दधि सिञ्चति, मधु सिञ्चति. प्रत्ययसकारत्वात्
    प्राप्तिः, पदादेश्चादेशसकारत्वात् — 8.3.59's two halves. Reads: `pratyaya` on
    सात्; for the word-head, the स् begins a piece after a word or compound
    boundary. A preverb's boundary is not one: 8.3.65's cerebral is not held
    off (उपसर्गादिति या प्राप्तिः सा पदादिलक्षणमेव प्रतिषेधं बाधते, Kāśikā on 8.3.112).
    """,
    "8.3.112": """
    सिचो यङि — no cerebral for the स् of सिच् before यङ्: सेसिच्यते, अभिसेसिच्यते. The
    refusal holds EVERYWHERE — the preverb's cerebral does not get past it (तस्मादयं
    प्रतिषेधः सर्वत्र भवति). Reads `dhatu:sic` and `pratyaya:yaṅ` after it.
    """,
    "8.3.113": """
    सेधतेर्गतौ — no cerebral for सेध् where MOTION is meant: अभिसेधयति गाः, परिसेधयति
    गाः. शिष्यमकार्यात् प्रतिषेधयति (गताविति किम्). Reads `sense:gati`.
    """,
    "8.3.114": """
    प्रतिस्तब्धनिस्तब्धौ च — प्रतिस्तब्धः, निस्तब्धः are laid down without the cerebral
    that 8.3.67 gave. Reads the pieces prati|stabdha, ni|stabdha.
    """,
    "8.3.115": """
    सोढः — no cerebral for सह् in the shape सोढ्: परिसोढा, परिसोढुम्, परिसोढव्यम्.
    सोड्भूतग्रहणं किम्? परिषहते. Reads `dhatu:sah` on a piece that begins soḍh.
    """,
    "8.3.116": """
    स्तम्भुसिवुसहां चङि — no cerebral for स्तम्भ्, सिव्, सह् before चङ्: पर्यतस्तम्भत्,
    पर्यसीषिवत्, पर्यसीषहत्. उपसर्गाद् या प्राप्तिस्तस्या एव प्रतिषेधः — the cerebral
    that comes from the reduplicative syllable's इण् stays (the root's स् in
    पर्यसीषिवत्). Reads `pratyaya:caṅ` after the root.
    """,
    "8.3.117": """
    सुनोतेः स्यसनोः — no cerebral for the स् of सुनोति before स्य and सन्: अभिसोष्यति,
    परिसोष्यति, अभ्यसोष्यत्. Reads `pratyaya:sya` or `pratyaya:san` after the root.
    """,
    "8.3.118": """
    सदेः परस्य लिटि — in the PERFECT of सद् and स्वञ्ज् the LATER स् — the root's, after
    the reduplication — is not made cerebral: अभिषसाद, परिषसाद, निषसाद, परिषस्वजे. The
    first स् is; the second is not. Reads `pratyaya:liṭ` after the root.
    """,
    "8.3.119": """
    निव्यभिभ्योऽड्व्यवाये वा छन्दसि — in the Veda, after नि, वि, अभि, the cerebral
    optionally does not reach across the augment: न्यषीदत् / न्यसीदत्, व्यषीदत् /
    व्यसीदत्, अभ्यष्टौत् / अभ्यस्तौत्. 8.3.63 had made that reach obligatory. Runs
    only for Vedic text.
    """,
})

def _finish() -> Tuple:
    _register_pvs()
    _register_dh()
    _register_cps()
    _register_laid()
    _register_eti()
    _register_refusals()
    _register_varttika_101()
    return tuple(sorted(_RULES, key=lambda r: (r.order, r.varttika)))


RULES = _finish()

#: Which sūtras of this family's scope the module implements — the honest
#: account, kept beside the code. See `rulebook.COVERAGE_STATUS`.
COVERAGE = (
    ("8.3.55", "support",
     "A heading (अपदान्तस्य मूर्धन्यः) that carries 'not the last sound of a pada' "
     "and 'a मूर्धन्य sound' down to 8.3.119; it cannot be a step of its own, so "
     "`_standing` asks the first half and `_cerebral` (1.1.50 via "
     "supports.nearest) the second, and every step cites 8.3.55 among its sūtras."),
    ("8.3.56", "rule", ""),
    ("8.3.57", "support",
     "A heading (इण्कोः) carrying the cause — an इण् or a कु standing immediately "
     "before — to 8.3.119; `_reach` and `_is_cause` ask it, and every step it "
     "conditions cites it. 8.3.56, the preverb rules 8.3.65–8.3.77 (no कु can end a "
     "preverb) and 8.3.68, 8.3.69, 8.3.83, 8.3.97, 8.3.109 ask for less or other."),
    ("8.3.58", "support",
     "A heading (नुम्विसर्जनीयशर्व्यवायेऽपि) letting the cause be reached across ONE "
     "नुम्, visarga or शर् (प्रत्येकं, never two: निंस्से, निंस्स्वे). It is `_reach`; "
     "the step that crosses one cites 8.3.58. The नुम् is the caller's flag `num` "
     "(a bare anusvāra is not the नुम् — सुहिन्सु, पुंसु)."),
    ("8.3.59", "rule", ""),
    ("8.3.60", "rule", ""),
    ("8.3.61", "rule",
     "A niyama, done as what it does — a refusal of 8.3.59's cerebral for the स् "
     "after a reduplicative syllable's इण् before a षभूत सन्, unless the root is "
     "स्तु or णिजन्त. Its positive cases (तुष्टूषति) are 8.3.59's own."),
    ("8.3.62", "rule", ""),
    ("8.3.63", "support",
     "A heading (प्राक्सितादड्व्यवायेऽपि) letting the cerebral of 8.3.65–8.3.70 up to "
     "*sita* cross the augment अट्. It is `_reach(at_ok=True)`, and the step that "
     "crosses cites 8.3.63. The augment is the caller's flag `at`."),
    ("8.3.64", "rule",
     "The reduplicative syllable's own स् for the ten roots from स्था on, and "
     "(in `_reach`) the reach across the syllable. The abhyāsa's स् is "
     "reached where a caller marks the syllable `abhyasa`."),
    ("8.3.65", "rule", ""),
    ("8.3.66", "rule", ""),
    ("8.3.67", "rule", ""),
    ("8.3.68", "rule", ""),
    ("8.3.69", "rule", ""),
    ("8.3.70", "rule", ""),
    ("8.3.71", "rule", ""),
    ("8.3.72", "rule", ""),
    ("8.3.73", "rule", ""),
    ("8.3.74", "rule", ""),
    ("8.3.75", "rule", ""),
    ("8.3.76", "rule", ""),
    ("8.3.77", "rule", ""),
    ("8.3.78", "rule", ""),
    ("8.3.79", "rule", ""),
    ("8.3.80", "rule", ""),
    ("8.3.81", "rule", ""),
    ("8.3.82", "rule", ""),
    ("8.3.83", "rule", ""),
    ("8.3.84", "rule", ""),
    ("8.3.85", "rule", ""),
    ("8.3.86", "rule", ""),
    ("8.3.87", "rule", ""),
    ("8.3.88", "rule", ""),
    ("8.3.89", "rule", ""),
    ("8.3.90", "rule", ""),
    ("8.3.91", "rule", ""),
    ("8.3.92", "rule", ""),
    ("8.3.93", "rule", ""),
    ("8.3.94", "rule", ""),
    ("8.3.95", "rule", ""),
    ("8.3.96", "rule", ""),
    ("8.3.97", "partial",
     "The eighteen first members and the exact form स्थ are done; the vārttika "
     "स्थास्थिन्स्थॄणाम् (सव्येष्ठाः, परमेष्ठी, सव्येष्ठृसारथिः) is not."),
    ("8.3.98", "partial",
     "The words of the सुषामादि gaṇa as the gaṇapāṭha lists them. It is an "
     "आकृतिगण, whose completion is by usage, so a word outside the list is not "
     "recognised."),
    ("8.3.99", "rule", ""),
    ("8.3.100", "rule", ""),
    ("8.3.101", "rule",
     "With the vārttika तिङन्तस्य प्रतिषेधो वक्तव्यः as a rule of its own "
     "(authority: vārttika). The list of seven taddhitas the Kāśikā gives is "
     "not enforced: any `taddhita` piece that begins with त् is taken."),
    ("8.3.102", "rule", ""),
    ("8.3.103", "scope",
     "Its sthānin is the स् at the END of a pada, out of a visarga "
     "(अग्निष्ट्वं नामासीत्), and stands on how 8.3.55's अपदान्तस्य is met by a स् "
     "that 8.3.34 made from a visarga, and on a metrical position (अन्तःपादम्) no "
     "letters give: contested, and the visarga family's to settle first. OPEN."),
    ("8.3.104", "scope",
     "As 8.3.103 (the same sthānin, in the Yajus, by some teachers' view). OPEN."),
    ("8.3.105", "vedic", ""),
    ("8.3.106", "vedic",
     "Only where the caller marks the member `uttarapada` (the sūtra names no "
     "first member, so nothing else limits it); non-compound first members "
     "(त्रिःषमृद्धत्वाय) are not reached."),
    ("8.3.107", "vedic", ""),
    ("8.3.108", "scope",
     "सनोतेरनः: the exception (अनः) is read differently — the Kāśikā's "
     "अनकारान्तस्य with the example गोसनिम्, which ends in इ — and no flag can "
     "say which shape a form has taken. OPEN."),
    ("8.3.109", "vedic",
     "पृतना, ऋत — the चकार's ऋतीषहम् (a lengthened ऋति, by 6.3.116) is not done."),
    ("8.3.110", "rule",
     "The gaṇa सवनादि is read from the gaṇapāṭha, which holds four words; the "
     "Kāśikā's longer list (सवनेसवने, सूतेसूते …) is not on disk as data."),
    ("8.3.111", "rule", ""),
    ("8.3.112", "rule", ""),
    ("8.3.113", "rule", ""),
    ("8.3.114", "rule", ""),
    ("8.3.115", "rule", ""),
    ("8.3.116", "rule",
     "For सिवु and सह् the refusal has nothing to refuse in this model: their "
     "reduplicative syllable's स् is not reached (8.3.64 confines that to the ten "
     "sthādi roots), and the root's स् after it comes from the syllable's इण् — "
     "which 8.3.116 leaves. The Kāśikā's पर्यसीषिवत्, पर्यसीषहत् come out right "
     "without a step; स्तम्भ् (पर्यतस्तम्भत्) is refused by a step. OPEN."),
    ("8.3.117", "rule", ""),
    ("8.3.118", "rule", ""),
    ("8.3.119", "vedic", ""),
)