# -*- coding: utf-8 -*-
"""
८.४.१–३९ — रषाभ्यां नो णः, and the thirty-eight rules about it, as sandhi steps.

A dental न् becomes the cerebral ण् after a र् or ष् (8.4.1), and the very next
sūtra lets it reach across a vowel, a guttural, a labial, the preverb आङ् or a
नुम् (8.4.2): *rāma + ena* is *rāmeṇa*, *kara + ana* is *karaṇa*, *arka + ena*
is *arkeṇa*. Twenty-seven sūtras then say where else the cerebral goes — across
a compound seam (8.4.3–13), from a preverb into a root (8.4.14–33) — and six at
the end take it back (8.4.34–39): not after a word-final ष् (*niṣpānam*), not of
a word-final न् (*vṛkṣān*), not where a whole word stands between (*pra gāṃ
nayāmaḥ*).

**WHERE THIS FAMILY DIFFERS FROM THE JUNCTION RULES.** The engine acts at
junctions between words. Cerebralisation acts at a न् that is *interior* to a
piece — the न् of an affix, or of a root — and its cause may be several sounds
away, inside one pada. So these rules look across the pieces the caller joined
with an ANGA boundary (8.4.1, 8.4.2), a SAMASA boundary (8.4.3–13) or an
UPASARGA boundary (8.4.14–33), and they **never rewrite the inside of a finished
piece that has no such join**: *arjuna* and *gacchati* stay as they are, and so
does *karana* given as one word.

**THE ONE WALK.** Every provision asks the same geometric question and asks it
once (`_walk`): going left from a न्, through sounds that 8.4.2 lets the
cerebral cross (`anga._across_which`, the project's own codification of the
list, so this module does not restate it), does one reach a र् or ष्? Which
sūtra then owns the न् is decided by *what stands between them* — the same pada
(8.4.1 if nothing stands between, 8.4.2 if something does), a compound seam, a
preverb — and by the lexical facts the caller supplies. The rule sees the row as
its own View shows it, so a ष् that 8.3.59 has made out of a स् (8.3.55–119
stand before 8.4.1) is a ष् for it, and a cerebral 8.4.14 has made is not yet
there for 8.4.1 (8.2.1).

**REFUSALS ARE RULES, AND MEET THEIR TARGETS AT ONE SITE.** 8.4.34–39, and the
niyama halves of 8.4.4, 8.4.22 and 8.4.32, are applications with no edits, on
exactly the sounds of the application they refuse (`hit.site`), winning by
`overrides` whose reasons are quoted from the Kāśikā. Each refusal asks the same
`_hits_*` functions the refused rule asks, so the two cannot disagree about
where they are. Where the tradition says a rule is an अपवाद of a refusal (8.4.20
of 8.4.37) the excepted rule declares it, quoting the Kāśikā.

**WHAT THE CALLER SAYS — the flags this family reads** (NORTH_STAR §5: what no
letter can say is a parameter, and the trace says so). All are word flags,
written in braces (`pra{upasarga}|nam{dhatu:nam}~a~ti`):

======================  ======================================================
`upasarga`              the preverb: the word 8.4.14–33 call उपसर्ग (a र् or ष्
                        in it is the cause). `pra`, `parā`, `pari`, `nir`.
                        दुः is not one for this purpose (vārttika, below).
`ang`                   the preverb आङ् — 8.4.2 names it, and it is a pada of
                        its own that 8.4.38's refusal must not count.
`dhatu:ROOT`            this piece holds the root ROOT, by its bare name
                        (`nam`) or its whole enunciation (`ṇama̐`). Whether it
                        is णोपदेश is READ from the dhātupāṭha (`pada.entries_for`),
                        never guessed; where a bare name is read twice with
                        different marks the step says so.
`krt`                   a piece that is a कृत् affix (8.4.29–34).
`nyanta`                on a `krt` piece: it was added to a णिच् stem (8.4.30).
`lot`                   a piece that is the लोट् substitute आनि (8.4.16).
`sabhyasa`              on a `dhatu:an` piece: the reduplicated root (8.4.21).
`samjna`                on any member: the compound is a NAME (8.4.3–4).
`osadhi`, `vanaspati`   on a first member: it names a herb / a tree (8.4.6).
`ahita`                 on a first member: it names what is loaded (8.4.8).
`desa`                  the compound names a country or a people (8.4.9),
                        or — 8.4.24, 8.4.25 — a *place*, which those refuse.
`bhava`, `karana`       on पान: the act, the instrument (8.4.10).
`vibhakti`, `num`       a case-ending piece; the नुम् (8.4.11–13).
`ksubhnadi`             the word belongs to the आकृतिगण of 8.4.39.
`avagraha`              on a first member: the padapāṭha separates it (8.4.26).
======================  ======================================================

The boundary kinds are the parser's: `~` ANGA (stem | affix — one pada), `-`
SAMASA (a compound member), `|` UPASARGA (preverb | root), a space PADA.

**WHAT THE LETTERS DO SAY, AND IS READ, NOT TYPED.** The सूत्र's own न्, ण् and
cause sounds are read from the corpus text of 8.4.1. The lists a सूत्र spells
out as its own words (the six first members of 8.4.4, the ten of 8.4.5, the
roots of 8.4.15, 8.4.17, 8.4.33, 8.4.34) are read from the Kāśikā's own
enumeration, on disk. The नुम्-आकृतिगण words come from the Kāśikā on 8.4.39, the
युवादि, इरिकादि and गिरिनद्यादि gaṇas from the gaṇapāṭha. The ghu roots are asked
of `samjna.ghu_roots`, the ṇopadeśa status of a root of the dhātupāṭha.

**STANDING NOTES — OPEN and SCOPE.**

* OPEN — 8.4.37 पदान्तस्य. The Tattvabodhinī says the Bhāṣya *rejects* it
  (*पदान्तस्य इति सूत्रं च भाष्ये प्रत्याख्यातम्*): 8.3.55's अपदान्तस्य is carried
  down, so a word-final न् is not reached in the first place. The Kāśikā and the
  Kaumudī keep it as a sūtra, and so does this module, as the visible refusal.
* OPEN — the anuvṛtti of 8.4.2's *vyavāya* into 8.4.3–33 is not stated by the
  Kāśikā; it is taken from the forms (*praṇamati* has an अ between र् and न्).
* OPEN — 8.4.33's Kaumudī adds *कृति परे*; the Kāśikā does not. The Kāśikā's
  reading is followed.
* SCOPE — the vārttika निर्विण्णस्योपसंख्यानम् (8.4.29), the गणसूत्र
  आचार्यादणत्वं च (8.4.39), the अट्-augment between नि and the root
  (*प्रण्यगदत्*, 8.4.17) and the yoga-vibhāga niyama of 8.4.22 that reaches
  *वृत्रघ्नः* are not derived here; their notes are in COVERAGE.
* SCOPE — 8.4.26 needs the padapāṭha (`avagraha`), and 8.4.27–28 are Vedic in
  their examples; the first two run only with `veda=True`.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from functools import lru_cache
from typing import (
    Callable, Dict, FrozenSet, Iterable, Iterator, List, Mapping, Optional,
    Sequence, Tuple)

from src.astadhyayi import corpus, pada
from src.astadhyayi.anga import _across_which
from src.astadhyayi.itsamjna import DHATU, analyze
from src.astadhyayi.samjna import ghu_roots
from src.astadhyayi.sandhi import supports as S
from src.astadhyayi.sandhi import trace as _trace
from src.astadhyayi.sandhi.parse import to_iast, tokenize
from src.astadhyayi.sandhi.rule import (
    ADESA, PRATISEDHA, SUTRA, VARTTIKA, Application, Detail, Via, replace,
    rule, site, sk)
from src.astadhyayi.sandhi.segs import (
    AC, ANGA, HAL, PADA, SAMASA, UPASARGA, Sight, View)
from src.astadhyayi.varna import ANUSVARA, VARGA, savarna

#: Families every rule of this module carries ('hal', because a न् is a
#: consonant; 'natva', so another family can override the whole group).
FAMILY = ("hal", "natva")
#: The two kinds inside the family: a rule that gives ण्, and one that refuses it.
VIDHI = "natva-vidhi"
NISEDHA = "natva-pratisedha"



def _vidhi(sutra_id: str) -> Tuple[str, ...]:
    """The families of a rule that gives ण्: it is a vidhi *of this sūtra*, so a
    refusal can name it by that and not by a sūtra number, which a vārttika
    rule on the same sūtra shares."""
    return FAMILY + (VIDHI, f"vidhi:{sutra_id}")


def _nisedha(sutra_id: str) -> Tuple[str, ...]:
    return FAMILY + (NISEDHA, f"refusal:{sutra_id}")


def _tgt(sutra_id: str) -> str:
    """`overrides` target: every vidhi of that sūtra (and its vārttikas)."""
    return f"@vidhi:{sutra_id}"


def _refusal_tag(sutra_id: str) -> str:
    return f"@refusal:{sutra_id}"


#: The options the सूत्र words themselves (सूत्र 8.4.6 विभाषा, 8.4.10 वा,
#: 8.4.28 बहुलम्), as the engine's `optional=` wants them.
VIBHASA, VA, BAHULAM = "विभाषा", "वा", "बहुलम्"


# ---------------------------------------------------------------------------
# What the corpus says — sounds, lists, quotations — read once
# ---------------------------------------------------------------------------


def _sutra_words(sutra_id: str) -> List[str]:
    return corpus.load_vidyut_sutrapatha()[sutra_id].text.split()


def _consonants(word: str) -> Tuple[str, ...]:
    return tuple(s for s, _ in tokenize(word) if s in HAL)


@lru_cache(maxsize=None)
def _named() -> Tuple[Tuple[str, ...], str, str]:
    """
    The causes, the sthānin and the ādeśa, as 8.4.1 itself writes them:
    *raṣābhyāṃ no ṇaḥ* — the first two consonants of the first word (ra, ṣa),
    the न of *no*, the ण of *ṇaḥ*.
    """
    words = _sutra_words("8.4.1")
    return (_consonants(words[0])[:2], _consonants(words[1])[0],
            _consonants(words[2])[0])


def CAUSES() -> FrozenSet[str]:
    """र् and ष् — 8.4.1's own cause."""
    return frozenset(_named()[0])


def STHANIN() -> str:
    return _named()[1]


def ADESA_N() -> str:
    return _named()[2]


@lru_cache(maxsize=None)
def RVARNA() -> FrozenSet[str]:
    """
    ऋ and ॠ — the cause Kātyāyana adds. They are the savarṇas of ऋ *without*
    the ऌ-extension of 1.1.9's vārttika (`varttika=False`), which is what the
    Kāśikā's *ऋवर्णात्* means: तिसृणाम्, मातॄणाम्, not ऌ.
    """
    return frozenset(v for v in AC if savarna(v, "ṛ", varttika=False))


@lru_cache(maxsize=None)
def VYAVAYA() -> FrozenSet[str]:
    """
    What may stand between the cause and the न्: **8.4.2's अट्, कु, पु, नुम्** —
    asked of the project's codification of that sūtra (`anga._across_which`,
    which closes अट् under 1.1.69 and adds the anusvāra that नुम् stands for) and
    not restated. (आङ् is a *word*, the flag `ang`; its sounds are vowels and
    semivowels and so already in the set.)
    """
    return frozenset(_across_which())


@lru_cache(maxsize=None)
def JHAL() -> FrozenSet[str]:
    return S.members("jhaL")


@lru_cache(maxsize=None)
def _rvarna_vartika() -> str:
    """Kātyāyana's vārttika on 8.4.1, verbatim from the corpus."""
    return corpus.varttikas_on("8.4.1")[0].text


def _vartika_text(sutra_id: str, opening: str) -> str:
    """A vārttika of `sutra_id`, verbatim from the corpus, found by its opening
    words (the corpus files it under the sūtra it comments on)."""
    for found in corpus.varttikas_on(sutra_id):
        if found.text.startswith(opening):
            return found.text
    raise LookupError(f"no vārttika of {sutra_id} begins {opening!r}")


def _name(sutra_id: str) -> str:
    """The rule's name is the sūtra's own words, in both scripts' first."""
    return _trace.deva(_trace.sutra_text(sutra_id))


def _kashika(sutra_id: str) -> str:
    return corpus.commentary_on(sutra_id, "kashika") or ""


@lru_cache(maxsize=None)
def _listed(sutra_id: str, end: str, after: str = "") -> Tuple[str, ...]:
    """
    The words the Kāśikā enumerates ahead of `end` (its *इत्येतेभ्यः*), in IAST —
    the सूत्र's own list, read where the commentary spells it, not retyped.
    """
    text = _kashika(sutra_id)
    head = text[:text.index(end)]
    if after:
        head = head[head.rindex(after) + len(after):]
    return tuple(to_iast(w) for w in head.split())


def PURAGADI() -> Tuple[str, ...]:
    """8.4.4's first members (the Kāśikā: पुरगा मिश्रका सिध्रका शारिका कोटरा अग्र)."""
    return _listed("8.4.4", "इत्येतेभ्यः", "वर्तते।")


def PRANIRADI() -> Tuple[str, ...]:
    """8.4.5's ten first members."""
    return _listed("8.4.5", "इत्येतेभ्य ")


def HINU_MINA() -> Tuple[str, ...]:
    return _listed("8.4.15", "इत्येतयो")


def GADADI_FORMS() -> Tuple[str, ...]:
    """8.4.17's seventeen, as the Kāśikā writes them: गद नद … देग्धि."""
    text = _kashika("8.4.17")
    start = text.index("भवति गद") + len("भवति")
    return tuple(to_iast(w) for w in
                 text[start:text.index("इत्येतेषु परतः")].split())


def NIMSADI() -> Tuple[str, ...]:
    """8.4.33's three: निंस निक्ष निन्द."""
    return _listed("8.4.33", "इत्येतेषां", "वर्तते।")


def BHADI() -> Tuple[str, ...]:
    """8.4.34's seven: भा भू पू कमि गमि प्यायी वेप."""
    return _listed("8.4.34", "इत्येतेषामु")


#: 8.4.17 names eleven of its roots by a form of each — the third singular of
#: the present, as the sūtra writes it. Which root each is, is the one thing the
#: Kāśikā's list does not say; it is said here, once, and checked against the
#: dhātupāṭha and the Kāśikā's own list in the tests.
_ROOT_OF_FORM: Mapping[str, str] = {
    "syati": "so", "hanti": "han", "yāti": "yā", "vāti": "vā", "drāti": "drā",
    "psāti": "psā", "vapati": "vap", "vahati": "vah", "śāmyati": "śam",
    "cinoti": "ci", "degdhi": "dih"}


@lru_cache(maxsize=None)
def GHU() -> FrozenSet[str]:
    """The ghu roots (1.1.20), by the names a sūtra uses (6.1.64, 6.1.65 applied)."""
    return frozenset(pada.root_key(u) for u in ghu_roots())


@lru_cache(maxsize=None)
def GADADI() -> FrozenSet[str]:
    """
    The roots 8.4.17 names, as bare names. *गद, नद, पत, पद* are the listed forms
    without their linking अ; *घु* is asked of `samjna.ghu_roots`; *मा* is माङ् and
    मेङ् (the Kāśikā: *मा इति माङ्मेङोर्ग्रहणमिष्यते*); the rest by `_ROOT_OF_FORM`.
    """
    names = set()
    for form in GADADI_FORMS():
        if form in _ROOT_OF_FORM:
            names.add(_ROOT_OF_FORM[form])
        elif form == "ghu":
            names |= GHU()
        elif form == "mā":
            names |= {"mā", "me"}
        else:
            names.add(form[:-1])
    return frozenset(names)


@lru_cache(maxsize=None)
def _rooted(listed: Tuple[str, ...]) -> FrozenSet[str]:
    """A list of forms as the bare names a flag would carry: the form and the
    form without its linking vowel (गद → गद्; कमि → कम्)."""
    out = set()
    for form in listed:
        out.add(form)
        out.add(form[:-1])
    return frozenset(out)


@lru_cache(maxsize=None)
def _uttarapadas_of_ksubhnadi() -> FrozenSet[str]:
    """
    The second members the Kāśikā on 8.4.39 names — *नन्दिन्, नन्दन, नगर* and
    *नर्तन, गहन, नन्दन, निवेश, निवास, अग्नि, अनूप* — read from the commentary.
    """
    text = _kashika("8.4.39")
    found = set()
    for sentence in re.split(r"[।॥]", text):
        if "एतान्युत्तरपदानि" not in sentence:
            continue
        head = sentence[:sentence.index("एतान्युत्तरपदानि")]
        for word in re.split(r"[,\s]+", head):
            if word:
                found.add(to_iast(word))
    return frozenset(found)


@lru_cache(maxsize=None)
def _ksubhna_prefix() -> str:
    """The word 8.4.39 itself names — *क्षुभ्ना* — without its final vowel, since
    the Kāśikā takes the altered shapes too (क्षुभ्नीतः, क्षुभ्नन्ति)."""
    return _sutra_words("8.4.39")[0].split("’")[0][:-1]


@lru_cache(maxsize=None)
def _gana_items(sutra_id: str) -> FrozenSet[str]:
    return frozenset(item for gana in corpus.ganas_for(sutra_id)
                     for item in gana.items)


# ---------------------------------------------------------------------------
# Roots — read from the dhātupāṭha, never guessed
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Root:
    """A root as a caller names it, and what the dhātupāṭha says of it."""

    value: str
    key: str
    entries: Tuple

    def nopadesa(self) -> str:
        """`yes` where every entry is enunciated with an initial ण्, `some`
        where the name is read twice and only some are, `no` otherwise."""
        if self.value.startswith("ṇ"):
            return "yes"
        starts = [e.upadesa.startswith("ṇ") for e in self.entries]
        if not starts or not any(starts):
            return "no"
        return "yes" if all(starts) else "some"

    def shapes(self) -> Tuple[Tuple[str, ...], ...]:
        """The sounds of each entry as a sūtra names the root (it-letters gone)."""
        return tuple(tuple(s for s, _ in tokenize(pada.root_key(e.upadesa)))
                     for e in self.entries)

    def idit(self) -> bool:
        """Some entry is इदित् — so it has a नुम् (7.1.58)."""
        return any("i" in analyze(e.upadesa, DHATU).it_letters
                   for e in self.entries)

    def why(self) -> str:
        """A sentence for the step: which entries were read."""
        seen = ", ".join(sorted({e.upadesa for e in self.entries})) or "none"
        note = ""
        if self.nopadesa() == "some":
            note = (" — the name is read in more than one entry with "
                    "different marks, and the ṇopadeśa reading is taken; "
                    "write the whole enunciation to say which is meant")
        return f"{self.value} is read in the dhātupāṭha as {seen}{note}"


@lru_cache(maxsize=None)
def _root(value: str) -> Root:
    return Root(value, pada.root_key(value), tuple(pada.entries_for(value)))


def _root_of(v: View, sight: Sight) -> Optional[Root]:
    value = v.word(sight).flag_value("dhatu")
    return _root(value) if value else None


def _is(root: Root, names: Iterable[str]) -> bool:
    return bool({root.key, root.value} & set(names))


# ---------------------------------------------------------------------------
# The walk, and the shape of the pada
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Reach:
    """The cause a न् can be reached from, and what stands between."""

    cause: Sight
    between: Tuple[Sight, ...]
    #: The cause is ऋ or ॠ — there by Kātyāyana, not by Pāṇini.
    rvarna: bool


def _ns(v: View) -> List[Sight]:
    return [s for s in v.live if s.s == STHANIN()]


def _walk(v: View, n: Sight, causes: FrozenSet[str]) -> Optional[Reach]:
    """
    Left from `n`, through what 8.4.2 lets the cerebral cross, to a cause.
    The first sound that is neither a cause nor a vyavāya ends the walk: a न्
    or ण् in the way stops it (that is why *praṇayana* keeps its second न्).
    """
    vyavaya = VYAVAYA()
    between: List[Sight] = []
    i = v.index(n) - 1
    while i >= 0:
        s = v.live[i]
        if s.s in causes:
            return Reach(s, tuple(reversed(between)), s.s in RVARNA())
        if s.s not in vyavaya:
            return None
        between.append(s)
        i -= 1
    return None


def _reach(v: View, n: Sight) -> Optional[Reach]:
    """The cause of `n` by Pāṇini's own र्/ष् where there is one, else, failing
    that, by the ऋ Kātyāyana adds."""
    return _walk(v, n, CAUSES()) or _walk(v, n, CAUSES() | RVARNA())


def _padas(v: View) -> Tuple[int, ...]:
    """The pada each word belongs to: words joined by ANGA are one."""
    out, p = [], 0
    for w in range(len(v.state.words)):
        out.append(p)
        if v.state.bounds[w] != ANGA:
            p += 1
    return tuple(out)


def _crossed(v: View, reach: Reach, n: Sight) -> FrozenSet[str]:
    """The boundary kinds between the cause's word and the न्'s."""
    return frozenset(v.state.bounds[w] for w in range(reach.cause.w, n.w))


def _whole_padas_between(v: View, reach: Reach, n: Sight,
                         *, except_ang: bool = True) -> Tuple[int, ...]:
    """The padas that lie wholly between the cause and the न् — 8.4.38's
    *पदव्यवाय* — leaving out the preverb आङ्, which 8.4.2 names."""
    padas = _padas(v)
    lo, hi = padas[reach.cause.w], padas[n.w]
    found: List[int] = []
    for s in reach.between:
        p = padas[s.w]
        if lo < p < hi and p not in found:
            found.append(p)
    if except_ang:
        found = [p for p in found
                 if not all(v.state.words[w].has("ang")
                            for w in range(len(padas)) if padas[w] == p)]
    return tuple(found)


def _pada_words(v: View, p: int) -> List[int]:
    padas = _padas(v)
    return [w for w in range(len(padas)) if padas[w] == p]


def _pada_text(v: View, p: int) -> str:
    return "".join(v.state.words[w].text for w in _pada_words(v, p))


def _unit_has(v: View, n: Sight, flag: str,
              across: Sequence[str] = (ANGA, SAMASA, UPASARGA)) -> bool:
    words = {s.w for s in v.unit_of(n, across=across)}
    return any(v.state.words[w].has(flag) for w in words)


def _left_to_8_3_24(v: View, n: Sight) -> bool:
    """A न् inside a pada before a झल् is an anusvāra by 8.3.24, which stands
    before 8.4.1 and so is what 8.4.1 sees (8.2.1). Where that rule's family has
    already acted there is no न् here; where it has not, this stands in."""
    nxt = v.next(n)
    return nxt is not None and not v.pada_final(n) and nxt.s in JHAL()


def _shown(sights: Iterable[Sight]) -> str:
    return "".join(s.s for s in sights)


def _kinds(between: Sequence[Sight]) -> str:
    """Which of 8.4.2's five each intervening sound is, as a phrase."""
    seen: List[str] = []
    for s in between:
        if s.s in VARGA["ku"]:
            k = "{ku}"
        elif s.s in VARGA["pu"]:
            k = "{pu}"
        elif s.s == ANUSVARA:
            k = "the anusvāra ({num})"
        else:
            k = "{aṭ}"
        if k not in seen:
            seen.append(k)
    return ", ".join(seen)


def _between_phrase(reach: Reach) -> str:
    if not reach.between:
        return "with nothing between"
    return (f"with '{_shown(reach.between)}' between "
            f"({_kinds(reach.between)})")


def _cause_phrase(v: View, reach: Reach) -> str:
    return f"the {sk(reach.cause.s)} of '{v.word(reach.cause).text}'"


def _geometry_via(v: View, n: Sight, reach: Reach) -> Tuple[Via, ...]:
    """The sūtras of the first adhyāya and of 8.4.2 that make the walk land."""
    out: List[Via] = [S.pancami_para(f"{sk(reach.cause.s)} of "
                                     f"'{v.word(reach.cause).text}'")]
    if reach.between:
        out.append(Via(
            "8.4.2", f"'{_shown(reach.between)}' stands between the cause and "
                     f"the {{n}}; it is {_kinds(reach.between)}, which 8.4.2 "
                     f"lets the cerebral reach across"))
        for s in reach.between:
            if s.is_vowel and S.long_form_used(s.s, "aṭ"):
                out.append(S.varna_grahana(s.s, "aṭ"))
                break
    out.append(Via("1.1.49", f"the {{n}} is named in the sixth case, so "
                             f"{sk(ADESA_N())} takes its place"))
    return tuple(out)


# ---------------------------------------------------------------------------
# A hit — where a vidhi would give ण्, before anything refuses it
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Hit:
    """A place where one sūtra gives the cerebral, and everything the step and
    the refusals need. Refusals read hits; they do not recompute them."""

    sutra: str
    n: Sight
    reach: Reach
    nimitta: str
    because: str
    via: Tuple[Via, ...] = ()
    optional: str = ""
    #: More sounds this one step also changes (8.4.21's *both* न्).
    also: Tuple[Sight, ...] = ()
    site: Tuple[int, ...] = ()
    #: What a refusal or a vārttika needs to know of the place, by name.
    facts: Tuple[Tuple[str, str], ...] = ()
    #: The sūtra itself names ऋ as the cause (8.4.26), so it is not Kātyāyana's.
    own_rvarna: bool = False

    def fact(self, name: str, default: str = "") -> str:
        return dict(self.facts).get(name, default)

    @property
    def by_vartika(self) -> bool:
        return self.reach.rvarna and not self.own_rvarna

    @property
    def authority(self) -> str:
        return VARTTIKA if self.by_vartika else SUTRA


def _hit(v: View, sutra: str, n: Sight, reach: Reach, *, nimitta: str,
         because: str, via: Sequence[Via] = (), optional: str = "",
         also: Sequence[Sight] = (), direct: bool = False,
         facts: Mapping[str, str] | Sequence[Tuple[str, str]] = (),
         own_rvarna: bool = False) -> Hit:
    geometry = () if direct is None else _geometry_via(v, n, reach)
    facts_tuple = tuple(facts.items()) if isinstance(facts, dict) else tuple(facts)
    return Hit(sutra, n, reach, nimitta, because,
               tuple(geometry) + tuple(via), optional, tuple(also),
               site(reach.cause, *reach.between, n, *also),
               facts_tuple, own_rvarna)


def _apply(hit: Hit, vartika: str = "") -> Application:
    """The ण् put where the न् stood — and, where a rule says both, both.
    `vartika` is the words of the vārttika the rule is, if it is one; a step
    whose cause is Kātyāyana's ऋ says so of itself."""
    text = vartika or (_rvarna_vartika() if hit.by_vartika else "")
    return Application(
        site=hit.site,
        edits=tuple(replace(s, ADESA_N()) for s in (hit.n, *hit.also)),
        detail=Detail(
            kind=ADESA, sthanin=STHANIN(), adesa=ADESA_N(),
            nimitta=hit.nimitta, because=hit.because, via=hit.via,
            authority=VARTTIKA if text else SUTRA, varttika=text),
        optional=hit.optional)


def _refuse(hit: Hit, *, nimitta: str, because: str,
            via: Sequence[Via] = (), vartika: str = "") -> Application:
    """A refusal: no edits, the very site of the application it refuses."""
    return Application(
        site=hit.site, edits=(),
        detail=Detail(kind=PRATISEDHA, sthanin=STHANIN(), adesa="",
                      nimitta=nimitta, because=because, via=tuple(via),
                      authority=VARTTIKA if vartika else SUTRA,
                      varttika=vartika))


# ---------------------------------------------------------------------------
# What the tradition says — every reason a rule gives is a quotation
# ---------------------------------------------------------------------------

#: Every (sūtra, commentary, words) this module quotes as a reason, so a test
#: can check that each is really in the commentary it names.
QUOTED: List[Tuple[str, str, str]] = []

_LABEL = {"kashika": "Kāśikā", "kaumudi": "Siddhāntakaumudī",
          "tattvabodhini": "Tattvabodhinī", "balamanorama": "Bālamanoramā"}


def _quote(sutra_id: str, commentary: str, words: str) -> str:
    """A reason, as the tradition words it: «…» and where it stands."""
    QUOTED.append((sutra_id, commentary, words))
    return f"«{words}» ({_LABEL[commentary]} on {sutra_id})"


#: Where a refusal or a vidhi asks for the same places its target does: the
#: generator of each provision's hits, by sūtra (and, for a vārttika, by its
#: opening words), and which of the three kinds of place it works in: `pada`
#: (8.4.1, 8.4.2), `seam` (a compound, 8.4.3–13) or `preverb` (8.4.14–33).
HITS: Dict[str, Callable[[View], Iterator["Hit"]]] = {}
KIND: Dict[str, str] = {}
PADA_KIND, SEAM_KIND, PREVERB_KIND = "pada", "seam", "preverb"


def _provides(key: str, kind: str):
    def wrap(fn):
        HITS[key] = fn
        KIND[key] = kind
        return fn
    return wrap


def _hits_in(v: View, *kinds: str) -> Iterator["Hit"]:
    """Every place any vidhi of the given kinds would give ण् — one place once."""
    seen = set()
    for key, fn in HITS.items():
        if KIND[key] in kinds:
            for hit in fn(v):
                if (hit.site, hit.sutra, hit.optional) not in seen:
                    seen.add((hit.site, hit.sutra, hit.optional))
                    yield hit


# ---------------------------------------------------------------------------
# 8.4.1, 8.4.2 — in one pada
# ---------------------------------------------------------------------------


def _same_pada_hits(v: View, *, direct: bool, rvarna: bool = False
                    ) -> Iterator[Hit]:
    """
    The न् of a joined pada and its cause. `direct` picks 8.4.1 (the cause
    stands next to it) from 8.4.2 (something stands between, as
    `anga.cerebral_n(..., direct=)` asks it too); `rvarna` picks the न् whose
    only cause is Kātyāyana's ऋ, which the sūtra proper does not reach.
    """
    padas = _padas(v)
    for n in _ns(v):
        if not v.joined_pada(n) or _left_to_8_3_24(v, n):
            continue
        proper = _walk(v, n, CAUSES())
        reach = _walk(v, n, CAUSES() | RVARNA()) if rvarna and proper is None \
            else proper
        if reach is None or bool(reach.between) == direct:
            continue
        if padas[reach.cause.w] != padas[n.w]:
            continue
        wc, wn = v.word(reach.cause).text, v.word(n).text
        yield _hit(
            v, "8.4.1" if direct or rvarna else "8.4.2", n, reach,
            nimitta=f"{sk(reach.cause.s)} stands before the {{n}} in the same pada",
            because=(f"the {{n}} of '{wn}' comes after the {sk(reach.cause.s)} of "
                     f"'{wc}', {_between_phrase(reach)}, and the pieces are "
                     f"ONE pada ({{samānapada}}), so the {{n}} is replaced by "
                     f"{sk(ADESA_N())}"))


@_provides("8.4.1", PADA_KIND)
def _hits_8_4_1(v: View) -> Iterator[Hit]:
    yield from _same_pada_hits(v, direct=True)


@_provides("8.4.1 ऋवर्णात्", PADA_KIND)
def _hits_rvarna(v: View) -> Iterator[Hit]:
    for direct in (True, False):
        for hit in _same_pada_hits(v, direct=direct, rvarna=True):
            if hit.reach.rvarna:
                yield hit


@_provides("8.4.2", PADA_KIND)
def _hits_8_4_2(v: View) -> Iterator[Hit]:
    yield from _same_pada_hits(v, direct=False)


@rule("8.4.1", name=_name("8.4.1"), families=_vidhi("8.4.1"))
def raabhyam_no_nah(v: View):
    """रषाभ्यां नो णः समानपदे — रामेण: ण् for the न् after a र् or ष् of the same pada.

    Reads: the pieces joined by ANGA (`v.joined_pada`); no flag. A finished
    word with no join is left alone. आस्तीर्णम्, कुष्णाति; अग्निर्नयति stays.
    """
    for hit in _hits_8_4_1(v):
        yield _apply(hit)


@rule("8.4.1", name=_name("8.4.1") + " — ऋवर्णात्",
      families=_vidhi("8.4.1"), authority=VARTTIKA,
      varttika=_rvarna_vartika())
def rvarnac_ca(v: View):
    """ऋवर्णान्नस्य णत्वं वाच्यम् — मातॄणाम्, कृणोति: the cause is ऋ or ॠ.

    Offered only where the sūtra proper finds no र् or ष् to reach, so the two
    never contend for one न्. Kātyāyana's, and the trace says so.
    """
    for hit in _hits_rvarna(v):
        yield _apply(hit, _rvarna_vartika())


@rule("8.4.2", name=_name("8.4.2"), families=_vidhi("8.4.2"))
def atkupvannumvyavaye_pi(v: View):
    """अट्कुप्वाङ्नुम्व्यवायेऽपि — करणम्, अर्केण, बृंहणम्: across a vowel, a guttural,
    a labial, आङ्, a नुम् (its anusvāra).

    Reads: the pieces joined by ANGA. What may stand between is
    `anga._across_which` (the project's codification). The nasal of a नुम्
    that is heard as न् (*प्रेन्वनम्*) is a न्, not an anusvāra, and stops the walk.
    """
    for hit in _hits_8_4_2(v):
        yield _apply(hit)


# ---------------------------------------------------------------------------
# 8.4.3–13 — across a compound seam
# ---------------------------------------------------------------------------
#
# 8.4.1's *samānapade* keeps the cerebral inside one pada, and a compound's
# members are padas (1.4.14 with 1.1.62; the Bālamanoramā: *तेन रामनामेत्यादौ
# नातिप्रसङ्गः*). These sūtras say where a compound is nevertheless crossed —
# each by a fact about the words (a name, a named first member, a named second
# member, an ending) that no letter says, and that the caller does.


@lru_cache(maxsize=None)
def _agah() -> str:
    """The ग् that 8.4.3's *agaḥ* keeps from standing between."""
    return _consonants(_sutra_words("8.4.3")[-1])[-1]


def _seam_reach(v: View, n: Sight) -> Optional[Reach]:
    """The cause of `n` in an EARLIER member of the compound `n` is in: the walk
    crosses SAMASA seams and nothing else."""
    if _left_to_8_3_24(v, n):
        return None
    reach = _reach(v, n)
    if reach is None:
        return None
    padas = _padas(v)
    if padas[reach.cause.w] == padas[n.w]:
        return None                        # one pada: 8.4.1 and 8.4.2's
    crossed = _crossed(v, reach, n)
    if SAMASA not in crossed or crossed - {ANGA, SAMASA}:
        return None
    return reach


def _seams(v: View, *, adjacent: bool = False):
    """(न्, its cause, the padas) for every न् a seam rule may own; `adjacent`
    keeps those whose cause is in the pada just before the न्'s — the
    *pūrvapada* the named-word rules mean."""
    padas = _padas(v)
    for n in _ns(v):
        reach = _seam_reach(v, n)
        if reach is None:
            continue
        if adjacent and padas[reach.cause.w] != padas[n.w] - 1:
            continue
        yield n, reach, padas


def _first_member(v: View, n: Sight, padas: Sequence[int]) -> str:
    return _pada_text(v, padas[n.w] - 1)


def _pada_flag(v: View, p: int, *flags: str) -> bool:
    return any(v.state.words[w].has(f) for w in _pada_words(v, p)
               for f in flags)


def _is_name(v: View, n: Sight) -> bool:
    return _unit_has(v, n, "samjna", (ANGA, SAMASA))


def _vowels(text: str) -> int:
    return sum(1 for s, _ in tokenize(text) if s in AC)


def _seam_because(v: View, n: Sight, reach: Reach, what: str) -> str:
    return (f"the {{n}} of '{v.word(n).text}' follows {_cause_phrase(v, reach)} "
            f"of an earlier member of the compound, {_between_phrase(reach)}; "
            f"{what}, so it is replaced by {sk(ADESA_N())}")


@_provides("8.4.3", SEAM_KIND)
def _hits_8_4_3(v: View) -> Iterator[Hit]:
    for n, reach, padas in _seams(v):
        if not _is_name(v, n) or any(s.s == _agah() for s in reach.between):
            continue
        yield _hit(
            v, "8.4.3", n, reach,
            nimitta=f"{sk(reach.cause.s)} in the first member of a compound that is a name",
            because=_seam_because(
                v, n, reach,
                f"no {sk(_agah())} stands between ({{agaḥ}}) and the compound "
                f"is a NAME ({{saṃjñā}}, as the caller says)"))


@rule("8.4.3", name=_name("8.4.3"), families=_vidhi("8.4.3"))
def purvapadat_samjnayam_agah(v: View):
    """पूर्वपदात् संज्ञायामगः — द्रुणसः, खरणसः, शूर्पणखा: across a seam, in a NAME, unless a ग् stands between.

    Reads: `samjna` on any member; the boundary SAMASA. चर्मनासिकः (no name)
    and ऋगयनम् (a ग् between) keep their न्.
    """
    for hit in _hits_8_4_3(v):
        yield _apply(hit)


def _vana(v: View, n: Sight) -> bool:
    return v.word(n).text == "vana"


@_provides("8.4.4", SEAM_KIND)
def _hits_8_4_4(v: View) -> Iterator[Hit]:
    for n, reach, padas in _seams(v, adjacent=True):
        first = _first_member(v, n, padas)
        if not (_vana(v, n) and _is_name(v, n) and first in PURAGADI()):
            continue
        yield _hit(
            v, "8.4.4", n, reach,
            nimitta=f"'{first}' is one of the six first members the sūtra names",
            because=_seam_because(
                v, n, reach,
                f"'{first}' is one of the six first members the sūtra names and "
                f"the compound is a NAME ({{saṃjñā}})"))


def _vana_niyama_hits(v: View) -> Iterator[Hit]:
    """The न् of *vana* in a name after a first member 8.4.4–6 do not name."""
    for n, reach, padas in _seams(v, adjacent=True):
        first = _first_member(v, n, padas)
        if not (_vana(v, n) and _is_name(v, n)):
            continue
        if first in PURAGADI() or first in PRANIRADI() or \
                _pada_flag(v, padas[n.w] - 1, "osadhi", "vanaspati"):
            continue
        yield _hit(v, "8.4.4", n, reach, nimitta="", because="",
                   facts={"first": first})


@rule("8.4.4", name=_name("8.4.4"), families=_vidhi("8.4.4"),
      overrides=(("8.4.3", _quote(
          "8.4.4", "kashika",
          "सिद्धे सत्यारम्भो नियमार्थः — एतेभ्य एव परस्य वननकारस्य णकारादेशो "
          "भवति, नान्येभ्य इति")),))
def vanam_puragamisrakadibhyah(v: View):
    """वनं पुरगामिश्रकासिध्रकाशारिकाकोटराऽग्रेभ्यः — पुरगावणम्, कोटरावणम्; कुबेरवनम् stays.

    A niyama: the न् of *vana* in a name is reached after these six and no
    others (Kāśikā). So the rule gives ण् after the six, and REFUSES 8.4.3's
    for any other first member — which is where the trace shows it. Reads:
    `samjna`; the first member's text against the Kāśikā's own list. The list is
    read from the Kāśikā, whose sixth word is *अग्र*; the form the compound
    shows is the locative *अग्रे* (Kaumudī: राजदन्तादिषु निपातनात् सप्तम्या अलुक्).
    """
    for hit in _hits_8_4_4(v):
        yield _apply(hit)
    for hit in _vana_niyama_hits(v):
        first = hit.fact("first")
        yield _refuse(
            hit, nimitta=f"'{first}' is not among the first members 8.4.4–6 name",
            because=(f"the {{n}} of 'vana' stands after '{first}', which is not "
                     f"one of the six first members of 8.4.4 nor of 8.4.5's "
                     f"ten, and names neither a herb nor a tree (8.4.6); "
                     f"8.4.4 is a niyama — the न् of *vana* in a name is "
                     f"reached after those and no others — so it stays "
                     f"{sk(STHANIN())}"))


@_provides("8.4.5", SEAM_KIND)
def _hits_8_4_5(v: View) -> Iterator[Hit]:
    for n, reach, padas in _seams(v, adjacent=True):
        first = _first_member(v, n, padas)
        if not (_vana(v, n) and first in PRANIRADI()):
            continue
        yield _hit(
            v, "8.4.5", n, reach,
            nimitta=f"'{first}' is one of the ten first members the sūtra names",
            because=_seam_because(
                v, n, reach,
                f"'{first}' is one of the ten first members the sūtra names, "
                f"and *asaṃjñāyām api* asks no name"))


@rule("8.4.5", name=_name("8.4.5"), families=_vidhi("8.4.5"))
def pranirantah_sarekshu(v: View):
    """प्रनिरन्तःशरेक्षुप्लक्षाम्रकार्ष्यखदिरपीयूक्षाभ्योऽसंज्ञायामपि — प्रवणे, शरवणम्, कार्ष्यवणम्: name or no name.

    Reads: the first member's text against the Kāśikā's list of ten; no flag.
    """
    for hit in _hits_8_4_5(v):
        yield _apply(hit)


@_provides("8.4.6", SEAM_KIND)
def _hits_8_4_6(v: View) -> Iterator[Hit]:
    for n, reach, padas in _seams(v, adjacent=True):
        first = _first_member(v, n, padas)
        if not (_vana(v, n) and _pada_flag(v, padas[n.w] - 1,
                                           "osadhi", "vanaspati")):
            continue
        yield _hit(
            v, "8.4.6", n, reach,
            nimitta=f"'{first}' names a herb or a tree",
            because=_seam_because(
                v, n, reach,
                f"'{first}' names a herb or a tree (the caller says), and the "
                f"cerebral is an OPTION here ({{vibhāṣā}}, an aprāpta-vibhāṣā: "
                f"no earlier rule gave it)"),
            optional=VIBHASA, facts={"first": first})


@rule("8.4.6", name=_name("8.4.6"), families=_vidhi("8.4.6"))
def vibhasa_osadhivanaspatibhyah(v: View):
    """विभाषौषधिवनस्पतिभ्यः — दूर्वावणम्, दूर्वावनम्; शिरीषवणम्, शिरीषवनम्: optional after a herb or a tree.

    Reads: `osadhi` or `vanaspati` on the first member. Forks: both courses.
    """
    for hit in _hits_8_4_6(v):
        yield _apply(hit)


_DVYAC = _vartika_text("8.4.6", "द्व्यच्")
_IRIKADI = _vartika_text("8.4.6", "इरिकादिभ्यः")


@rule("8.4.6", name=_name("8.4.6") + " — द्व्यच्त्र्यच्", families=_nisedha("8.4.6"),
      authority=VARTTIKA, varttika=_DVYAC,
      overrides=(("8.4.6", _quote(
          "8.4.6", "kashika",
          "द्व्यक्षरत्र्यक्षरेभ्य इति वक्तव्यम्॥ इह मा भूत् — देवदारुवनम्")),))
def dvyac_tryac(v: View):
    """द्व्यच्त्र्यज्भ्यामेव — only a first member of two or three vowels: देवदारुवनम् (four) keeps its न्."""
    for hit in _hits_8_4_6(v):
        first = hit.fact("first")
        if _vowels(first) not in (2, 3):
            yield _refuse(
                hit, vartika=_DVYAC,
                nimitta=f"'{first}' has {_vowels(first)} vowels",
                because=(f"'{first}' has {_vowels(first)} vowels, and Kātyāyana "
                         f"limits 8.4.6's option to first members of two or "
                         f"three ({{dvyac}}, {{tryac}}), so {sk(STHANIN())} stays"))


@rule("8.4.6", name=_name("8.4.6") + " — इरिकादिभ्यः", families=_nisedha("8.4.6"),
      authority=VARTTIKA, varttika=_IRIKADI,
      overrides=(("8.4.6", _quote(
          "8.4.6", "kashika", "इरिकादिभ्यः प्रतिषेधो वक्तव्यः")),))
def irikadibhyah_pratisedhah(v: View):
    """इरिकादिभ्यः प्रतिषेधो वक्तव्यः — इरिकावनम्, तिमिरवनम्: the गणपाठ's irikādi keep their न्."""
    items = _gana_items("8.4.6")
    stems = {i[:-1] for i in items}
    for hit in _hits_8_4_6(v):
        first = hit.fact("first")
        if first in items or first[:-1] in stems:
            yield _refuse(
                hit, vartika=_IRIKADI,
                nimitta=f"'{first}' is in the irikādi gaṇa",
                because=(f"'{first}' is in the irikādi gaṇa (the gaṇapāṭha's "
                         f"*{'*, *'.join(sorted(items))}*), for which Kātyāyana "
                         f"says the option is refused, so {sk(STHANIN())} stays"))


@_provides("8.4.7", SEAM_KIND)
def _hits_8_4_7(v: View) -> Iterator[Hit]:
    for n, reach, padas in _seams(v, adjacent=True):
        first = _first_member(v, n, padas)
        if v.word(n).text != "ahna" or not first.endswith("a"):
            continue
        yield _hit(
            v, "8.4.7", n, reach,
            nimitta=f"'{first}' ends in a short {{a}}",
            because=_seam_because(
                v, n, reach,
                f"the word is *ahna* (the substitute of 5.4.88) and the first "
                f"member '{first}' ends in a short {{a}} ({{adanta}})"),
            via=(Via("5.4.88", "the न् belongs to अह्न, the substitute of अहन्"),))


@rule("8.4.7", name=_name("8.4.7"), families=_vidhi("8.4.7"))
def ahno_dantat(v: View):
    """अह्नोऽदन्तात् — पूर्वाह्णः, अपराह्णः: the न् of *ahna* after an अ-final first member.

    Reads: the second member's text `ahna`. निरह्नः, दुरह्नः (no अ) and
    दीर्घाह्नी (no अ in *ahn*) keep their न्.
    """
    for hit in _hits_8_4_7(v):
        yield _apply(hit)


@_provides("8.4.8", SEAM_KIND)
def _hits_8_4_8(v: View) -> Iterator[Hit]:
    for n, reach, padas in _seams(v, adjacent=True):
        first = _first_member(v, n, padas)
        if v.word(n).text != "vāhana" or \
                not _pada_flag(v, padas[n.w] - 1, "ahita"):
            continue
        yield _hit(
            v, "8.4.8", n, reach,
            nimitta=f"'{first}' names what is loaded on it",
            because=_seam_because(
                v, n, reach,
                f"the word is *vāhana* and '{first}' names what is loaded on it "
                f"({{āhita}}, as the caller says)"))


@rule("8.4.8", name=_name("8.4.8"), families=_vidhi("8.4.8"))
def vahanam_ahitat(v: View):
    """वाहनमाहितात् — इक्षुवाहणम्, शरवाहणम्: the न् of *vāhana* after a word for what is loaded.

    Reads: the text `vāhana`; `ahita` on the first member. दाक्षिवाहनम् (a cart
    belonging to Dākṣi) keeps its न्.
    """
    for hit in _hits_8_4_8(v):
        yield _apply(hit)


@_provides("8.4.9", SEAM_KIND)
def _hits_8_4_9(v: View) -> Iterator[Hit]:
    for n, reach, padas in _seams(v):
        if v.word(n).text != "pāna" or not _unit_has(v, n, "desa"):
            continue
        yield _hit(
            v, "8.4.9", n, reach,
            nimitta="the compound names a country",
            because=_seam_because(
                v, n, reach,
                "the word is *pāna* and the compound names a country or its "
                "people ({deśa}, as the caller says)"))


@rule("8.4.9", name=_name("8.4.9"), families=_vidhi("8.4.9"))
def panam_dese(v: View):
    """पानं देशे — क्षीरपाणा उशीनराः, सुरापाणाः प्राच्याः: the न् of *pāna* where a country is named.

    Reads: the text `pāna`; `desa` on any member. दाक्षिपानम् keeps its न्.
    """
    for hit in _hits_8_4_9(v):
        yield _apply(hit)


@_provides("8.4.10", SEAM_KIND)
def _hits_8_4_10(v: View) -> Iterator[Hit]:
    for n, reach, padas in _seams(v):
        if v.word(n).text != "pāna" or not (
                _unit_has(v, n, "bhava") or _unit_has(v, n, "karana")):
            continue
        yield _hit(
            v, "8.4.10", n, reach,
            nimitta="पान names the act or the instrument",
            because=_seam_because(
                v, n, reach,
                "the word is *pāna* in the sense of the act or the instrument "
                "({bhāva}, {karaṇa}), where the cerebral is an OPTION ({vā})"),
            optional=VA)


@rule("8.4.10", name=_name("8.4.10"), families=_vidhi("8.4.10"))
def va_bhavakaranayoh(v: View):
    """वा भावकरणयोः — क्षीरपाणम्, क्षीरपानम्; क्षीरपाणः कंसः: optional where पान is the act or the instrument.

    Reads: the text `pāna`; `bhava` or `karana`. Forks: both courses.
    """
    for hit in _hits_8_4_10(v):
        yield _apply(hit)


_GIRINADI = _vartika_text("8.4.10", "गिरिनद्यादीनां")


@_provides("8.4.10 गिरिनद्यादीनाम्", SEAM_KIND)
def _hits_girinadi(v: View) -> Iterator[Hit]:
    items = _gana_items("8.4.10")
    for n, reach, padas in _seams(v, adjacent=True):
        if not v.begins_word(n):
            continue
        first = _first_member(v, n, padas)
        together = first + _pada_text(v, padas[n.w])
        item = next((i for i in sorted(items)
                     if len(i) > 4 and together.startswith(i)), "")
        if not item:
            continue
        yield _hit(
            v, "8.4.10", n, reach,
            nimitta=f"'{first}' + '{v.word(n).text}' is *{item}* of the gaṇa",
            because=_seam_because(
                v, n, reach,
                f"'{first}-{v.word(n).text}' is *{item}* of the girinadyādi "
                f"gaṇa, where Kātyāyana makes the cerebral optional ({{vā}})"),
            optional=VA)


@rule("8.4.10", name=_name("8.4.10") + " — गिरिनद्यादीनाम्",
      families=_vidhi("8.4.10"), authority=VARTTIKA, varttika=_GIRINADI)
def girinadyadinam_va(v: View):
    """गिरिनद्यादीनां वा — गिरिणदी, गिरिनदी; चक्रणितम्बा, चक्रनितम्बा: optional in the गणपाठ's girinadyādi.

    Reads: the two members' text against the गणपाठ's items (the `girinadī`,
    `cakranitambā` …), and the न् beginning the second member. Forks.
    """
    for hit in _hits_girinadi(v):
        yield _apply(hit, _GIRINADI)


# 8.4.11–13: the न् that ends a stem, belongs to a नुम्, or to an ending.


def _tail(v: View, n: Sight):
    """
    Which of 8.4.11's three places `n` stands in, and the word of the *stem*
    (the uttarapada): (`num`|`vibhakti`|`stem`, word index) or None.
    A stem's न् is its LAST sound and is followed, in the same pada, by a case
    ending — the Kāśikā: *उत्तरपदस्य प्रातिपदिकस्थो योऽन्त्यो नकारः*.
    """
    words, w = v.state.words, n.w
    if words[w].has("num"):
        kind = "num"
    elif words[w].has("vibhakti"):
        kind = "vibhakti"
    else:
        last = v.word_sights(w)[-1]
        if n.uid != last.uid or v.state.bounds[w] != ANGA \
                or w + 1 >= len(words) or not words[w + 1].has("vibhakti"):
            return None
        kind = "stem"
    u = w
    while u > 0 and (words[u].has("num") or words[u].has("vibhakti")):
        u -= 1
    return kind, u


_PLACE = {"num": "the augment {num}", "vibhakti": "a case ending ({vibhakti})",
          "stem": "the end of the stem ({prātipadikānta})"}


def _tail_hits(v: View, sutra: str, accept: Callable[[str], str], *,
               optional: str = "") -> Iterator[Hit]:
    for n, reach, padas in _seams(v):
        found = _tail(v, n)
        if found is None:
            continue
        kind, u = found
        stem = v.state.words[u].text
        why = accept(stem)
        if not why:
            continue
        yield _hit(
            v, sutra, n, reach,
            nimitta=f"the {{n}} is {_PLACE[kind]} after a first member",
            because=_seam_because(
                v, n, reach,
                f"the {{n}} is {_PLACE[kind]} of the second member '{stem}', {why}"),
            optional=optional, facts={"stem": stem})


@_provides("8.4.11", SEAM_KIND)
def _hits_8_4_11(v: View) -> Iterator[Hit]:
    yield from _tail_hits(
        v, "8.4.11", lambda stem: "and the cerebral is an OPTION ({vā})",
        optional=VA)


@rule("8.4.11", name=_name("8.4.11"), families=_vidhi("8.4.11"))
def pratipadikanta_numvibhaktisu_ca(v: View):
    """प्रातिपदिकान्तनुम्विभक्तिषु च — माषवापिणौ, माषवापिनौ; व्रीहिवापाणि; माषवापेण: optional, after a first member.

    Reads: `num` (the augment), `vibhakti` (the ending) or, for a stem's last
    न्, the ANGA join to a `vibhakti` piece. गर्गभगिनी (the न् is not the stem's
    last) keeps its न्. Forks.
    """
    for hit in _hits_8_4_11(v):
        yield _apply(hit)


_YUVADI = _vartika_text("8.4.11", "युवादेर्न")


@rule("8.4.11", name=_name("8.4.11") + " — युवादेर्न", families=_nisedha("8.4.11"),
      authority=VARTTIKA, varttika=_YUVADI,
      overrides=(("8.4.11", _quote("8.4.11", "kashika", "युवादीनां प्रतिषेधो वक्तव्यः")),
                 ("8.4.12", _quote("8.4.11", "kashika", "युवादीनां प्रतिषेधो वक्तव्यः")),
                 ("8.4.13", _quote("8.4.11", "kashika", "युवादीनां प्रतिषेधो वक्तव्यः"))))
def yuvader_na(v: View):
    """युवादेर्न — आर्ययूना, प्रपक्वानि: the yuvādi words keep their न्.

    Reads: the second member's text against the गणपाठ's yuvādi (`yuvan`,
    `pakva`, `ahan` …).
    """
    items = _gana_items("8.4.11")
    for gen in (_hits_8_4_11, _hits_8_4_12, _hits_8_4_13):
        for hit in gen(v):
            stem = hit.fact("stem")
            if stem in items:
                yield _refuse(
                    hit, vartika=_YUVADI,
                    nimitta=f"'{stem}' is in the yuvādi gaṇa",
                    because=(f"'{stem}' is in the yuvādi gaṇa, for which "
                             f"Kātyāyana lays down a refusal, so "
                             f"{sk(STHANIN())} stays"))


@_provides("8.4.12", SEAM_KIND)
def _hits_8_4_12(v: View) -> Iterator[Hit]:
    yield from _tail_hits(
        v, "8.4.12",
        lambda stem: (f"which has ONE vowel ({{ekāc}}), so it is not optional"
                      if _vowels(stem) == 1 else ""))


@rule("8.4.12", name=_name("8.4.12"), families=_vidhi("8.4.12"),
      overrides=(("8.4.11", _quote(
          "8.4.12", "kashika",
          "ण इति वर्तमाने पुनर्णग्रहणं विकल्पाधिकारनिवृत्तेर्विस्पष्टीकरणार्थम्")),))
def ekajuttarapade_nah(v: View):
    """एकाजुत्तरपदे णः — वृत्रहणौ, क्षीरपाणि, क्षीरपेण: the same, always, where the second member has one vowel.

    Reads: the same as 8.4.11, and the second member's vowels counted. It ends
    8.4.11's option (Kāśikā).
    """
    for hit in _hits_8_4_12(v):
        yield _apply(hit)


@_provides("8.4.13", SEAM_KIND)
def _hits_8_4_13(v: View) -> Iterator[Hit]:
    def gutturals(stem: str) -> str:
        found = [s for s, _ in tokenize(stem) if s in VARGA["ku"]]
        return (f"which has a guttural in it ({{ku}}: '{found[0]}'), so it is "
                f"not optional") if found else ""
    yield from _tail_hits(v, "8.4.13", gutturals)


@rule("8.4.13", name=_name("8.4.13"), families=_vidhi("8.4.13"),
      overrides=(("8.4.11", _quote(
          "8.4.13", "kashika",
          "कवर्गवति चोत्तरपदे प्रातिपदिकान्तनुम्विभक्तिषु पूर्वपदस्थाद् निमित्तादुत्तरस्य "
          "नकारस्य णकारादेशो भवति")),))
def kumati_ca(v: View):
    """कुमति च — वस्त्रयुगिणौ, स्वर्गकामिणौ, वस्त्रयुगेण: the same, always, where the second member has a guttural.

    Reads: as 8.4.12, with a कवर्ग sound in the second member. The Kāśikā
    states it without 8.4.11's *vā*.
    """
    for hit in _hits_8_4_13(v):
        yield _apply(hit)


# ---------------------------------------------------------------------------
# 8.4.14–33 — from a preverb into a root
# ---------------------------------------------------------------------------
#
# The cause stands in the preverb (*upasargasthān nimittāt*), the न् in the
# word that follows — compounded or not (*asamāse 'pi*): the boundary between
# them may be a compound seam, the UPASARGA join of preverb and root, or even
# the pada boundary of a sentence (*pra ṇo muñcatam*). What may NOT stand
# between is a whole word, which is 8.4.38's business and is refused there
# (*pra gāṃ nayāmaḥ*). The preverb āṅ is a word between and is not counted:
# 8.4.2 names it, so *paryāṇaddham*.


def _reach_in(v: View, n: Sight, cause_word: Callable) -> Optional[Reach]:
    """The cause of `n` in a word `cause_word` accepts, in another pada."""
    if _left_to_8_3_24(v, n):
        return None
    reach = _reach(v, n)
    if reach is None:
        return None
    padas = _padas(v)
    if padas[reach.cause.w] == padas[n.w]:
        return None
    if not cause_word(v.state.words[reach.cause.w]):
        return None
    return reach


def _pre_reach(v: View, n: Sight) -> Optional[Reach]:
    return _reach_in(v, n, lambda word: word.has("upasarga"))


def _pre_because(v: View, n: Sight, reach: Reach, what: str) -> str:
    return (f"the {{n}} of '{v.word(n).text}' follows {_cause_phrase(v, reach)} "
            f"of the preverb, {_between_phrase(reach)}; {what}, so it is "
            f"replaced by {sk(ADESA_N())}")


def _ang_via(v: View, reach: Reach, n: Sight) -> Tuple[Via, ...]:
    """Where the preverb āṅ stands between, say why 8.4.38 does not refuse."""
    padas = _padas(v)
    lo, hi = padas[reach.cause.w], padas[n.w]
    if not any(lo < padas[s.w] < hi and v.state.words[s.w].has("ang")
               for s in reach.between):
        return ()
    return (Via("8.4.2", "the preverb आङ् stands between as a pada of its own; "
                         + _quote("8.4.2", "kashika",
                                  "अड्व्यवाय इति सिद्ध आङ्ग्रहणं <<पदव्यवाये०>> "
                                  "[[८.४.३८]] इत्यस्य प्रतिषेधस्य बाधनार्थम्")),)


def _pre_hit(v: View, sutra: str, n: Sight, reach: Reach, *, what: str,
             nimitta: str, optional: str = "", also: Sequence[Sight] = (),
             via: Sequence[Via] = (), facts: Mapping[str, str] = {}) -> Hit:
    return _hit(v, sutra, n, reach, nimitta=nimitta,
                because=_pre_because(v, n, reach, what), optional=optional,
                also=also, via=tuple(via) + _ang_via(v, reach, n), facts=facts)


@lru_cache(maxsize=None)
def _first_consonants(sutra_id: str, count: int, word: int = 0
                      ) -> Tuple[str, ...]:
    return _consonants(_sutra_words(sutra_id)[word])[:count]


def _nimsadi(root: Root) -> bool:
    return _is(root, _rooted(NIMSADI()))


@_provides("8.4.14", PREVERB_KIND)
def _hits_8_4_14(v: View) -> Iterator[Hit]:
    for n in _ns(v):
        root = _root_of(v, n)
        if root is None or root.nopadesa() == "no" or _nimsadi(root):
            continue
        reach = _pre_reach(v, n)
        if reach is None:
            continue
        yield _pre_hit(
            v, "8.4.14", n, reach,
            nimitta=f"the root '{v.word(n).text}' is ṇopadeśa and a preverb stands before it",
            what=f"the root is ṇopadeśa ({{ṇopadeśa}}): {root.why()}")


@rule("8.4.14", name=_name("8.4.14"), families=_vidhi("8.4.14"))
def upasargad_asamase_pi_nopadesasya(v: View):
    """उपसर्गादसमासेऽपि णोपदेशस्य — प्रणमति, परिणमति, प्रणायकः: the root's न् after a preverb's र् or ष्.

    Reads: `upasarga` on the cause's word; `dhatu:ROOT` on the root's, whose
    ṇopadeśa status is READ from the dhātupāṭha (an enunciation that begins
    ण्). प्रनर्दति (नर्द् is न-upadeśa) keeps its न्; प्रनायको देशः (a first member,
    not a preverb) too. निंस, निक्ष, निन्द are 8.4.33's, a choice and not a duty.
    """
    for hit in _hits_8_4_14(v):
        yield _apply(hit)


@_provides("8.4.15", PREVERB_KIND)
def _hits_8_4_15(v: View) -> Iterator[Hit]:
    # the sūtra names the root with its vikaraṇa: hinu = hi + nu, mīnā = mī + nā
    roots = {form[:-2] for form in HINU_MINA()}
    for n in _ns(v):
        if n.w == 0 or not v.begins_word(n):
            continue
        value = v.state.words[n.w - 1].flag_value("dhatu")
        if not value or _root(value).key not in roots:
            continue
        reach = _pre_reach(v, n)
        if reach is None:
            continue
        yield _pre_hit(
            v, "8.4.15", n, reach,
            nimitta=f"the {{n}} of the vikaraṇa of '{value}' after a preverb",
            what=(f"it is the {{n}} of the vikaraṇa (*nu* / *nā*) of the root "
                  f"'{value}', named by the sūtra as *hinu* and *mīnā* — and "
                  f"the altered shapes count as well, the vowel's substitute "
                  f"standing as the vowel (sthānivadbhāva)"),
            via=(Via("1.1.56", "the substitute of the vowel after the न् "
                               "(नु → नो, ना → नी) counts as the original, "
                               "so the altered shapes are reached too"),))


@rule("8.4.15", name=_name("8.4.15"), families=_vidhi("8.4.15"))
def hinumina(v: View):
    """हिनुमीना — प्रहिणोति, प्रमीणाति, प्रमीणीतः: the न् of the vikaraṇa of हि and मी.

    Reads: `dhatu:hi` / `dhatu:mī` on the piece before, and the न् beginning
    the vikaraṇa piece; `upasarga` on the cause's word.
    """
    for hit in _hits_8_4_15(v):
        yield _apply(hit)


@_provides("8.4.16", PREVERB_KIND)
def _hits_8_4_16(v: View) -> Iterator[Hit]:
    ani = _sutra_words("8.4.16")[0]
    for n in _ns(v):
        word = v.word(n)
        if not (word.has("lot") and word.text == ani):
            continue
        reach = _pre_reach(v, n)
        if reach is None:
            continue
        yield _pre_hit(
            v, "8.4.16", n, reach,
            nimitta=f"the {{n}} of *{ani}*, the loṭ substitute, after a preverb",
            what=f"the piece is *{ani}* as the substitute of loṭ ({{loṭ}}, as the caller says)")


@rule("8.4.16", name=_name("8.4.16"), families=_vidhi("8.4.16"))
def ani_lot(v: View):
    """आनि लोट् — प्रवपाणि, परिवपाणि, प्रयाणि: the न् of the लोट् आनि after a preverb.

    Reads: `lot` on the piece *āni*. प्रवपानि मांसानि (the plural ending, no
    `lot`) keeps its न्.
    """
    for hit in _hits_8_4_16(v):
        yield _apply(hit)


def _ni(v: View, n: Sight) -> bool:
    return v.word(n).has("upasarga") and v.word(n).text == "ni"


def _root_after(v: View, n: Sight) -> Optional[Root]:
    """The root of the piece right after the piece of `n`."""
    if n.w + 1 >= len(v.state.words):
        return None
    value = v.state.words[n.w + 1].flag_value("dhatu")
    return _root(value) if value else None


def _ni_hits(v: View, sutra: str, accept, optional: str = "") -> Iterator[Hit]:
    """The न् of the preverb नि, after another preverb, before a root."""
    for n in _ns(v):
        if not _ni(v, n):
            continue
        root = _root_after(v, n)
        if root is None:
            continue
        why = accept(root)
        if not why:
            continue
        reach = _pre_reach(v, n)
        if reach is None or reach.cause.w == n.w:
            continue
        yield _pre_hit(
            v, sutra, n, reach, optional=optional,
            nimitta=f"the preverb नि stands before the root '{root.value}'",
            what=f"the piece is the preverb *ni* and the root that follows, "
                 f"'{root.value}', {why}")


@_provides("8.4.17", PREVERB_KIND)
def _hits_8_4_17(v: View) -> Iterator[Hit]:
    yield from _ni_hits(
        v, "8.4.17",
        lambda root: ("is one the sūtra names (gada, nada, pata, pada, ghu, mā, "
                      "syati, hanti …)" if _is(root, GADADI()) else ""))


@rule("8.4.17", name=_name("8.4.17"), families=_vidhi("8.4.17"))
def ner_gadanadapata(v: View):
    """नेर्गदनदपतपदघुमास्यतिहन्तियातिवातिद्रातिप्सातिवपतिवहतिशाम्यतिचिनोतिदेग्धिषु च —
    प्रणिगदति, प्रणिपतति, प्रणिददाति: the न् of नि before these roots.

    Reads: the text `ni` with `upasarga`; `dhatu:ROOT` on the next piece
    against the Kāśikā's seventeen (ghu by `samjna.ghu_roots`). NOT modelled:
    the अट् augment between नि and the root (प्रण्यगदत्).
    """
    for hit in _hits_8_4_17(v):
        yield _apply(hit)


@lru_cache(maxsize=None)
def _kakha() -> Tuple[str, ...]:
    """क् and ख् — 8.4.18's *akakhādau*, read from the sūtra's own word."""
    return _consonants(_sutra_words("8.4.18")[1].split("’")[1])[:2]


def _shape_ok(root: Root) -> bool:
    """8.4.18's *akakhādau aṣānta upadeśe*: not begun with क्/ख्, not ended in
    ष्, AS ENUNCIATED — the caller's root read in the dhātupāṭha."""
    return bool(root.shapes()) and all(
        shape[0] not in _kakha() and shape[-1] != "ṣ"
        for shape in root.shapes())


@_provides("8.4.18", PREVERB_KIND)
def _hits_8_4_18(v: View) -> Iterator[Hit]:
    def accept(root: Root) -> str:
        if _is(root, GADADI()) or not _shape_ok(root):
            return ""
        return ("is any other root (*śeṣe*) not beginning with क् or ख् and "
                "not ending in ष् as enunciated, where the cerebral is an "
                "OPTION ({vibhāṣā})")
    yield from _ni_hits(v, "8.4.18", accept, optional=VIBHASA)


@rule("8.4.18", name=_name("8.4.18"), families=_vidhi("8.4.18"))
def sese_vibhasa(v: View):
    """शेषे विभाषाऽकखादावषान्त उपदेशे — प्रणिपचति, प्रनिपचति: नि before any other root, optionally.

    Reads: as 8.4.17; the root's enunciation is read from the dhātupāṭha
    (प्रनिकरोति, प्रनिखादति, प्रनिपिनष्टि keep their न्). Forks.
    """
    for hit in _hits_8_4_18(v):
        yield _apply(hit)


def _hits_of_root(v: View, sutra: str, names: Iterable[str], *, final: bool,
                  what: str, optional: str = "", sabhyasa: bool = False
                  ) -> Iterator[Hit]:
    names = tuple(names)
    for n in _ns(v):
        root = _root_of(v, n)
        if root is None or not _is(root, names):
            continue
        if v.pada_final(n) != final or v.word(n).has("sabhyasa") != sabhyasa:
            continue
        reach = _pre_reach(v, n)
        if reach is None:
            continue
        yield _pre_hit(v, sutra, n, reach, nimitta=what, what=what,
                       optional=optional)


@lru_cache(maxsize=None)
def _ani() -> str:
    """The root अन् — the sūtra's *aniteḥ* is the root's form *aniti*."""
    return _sutra_words("8.4.19")[0][:2]


@_provides("8.4.19", PREVERB_KIND)
def _hits_8_4_19(v: View) -> Iterator[Hit]:
    yield from _hits_of_root(
        v, "8.4.19", (_ani(),), final=False,
        what="the root is अन् (*aniti*), 'to breathe'")


@rule("8.4.19", name=_name("8.4.19"), families=_vidhi("8.4.19"))
def aniteh(v: View):
    """अनितेः — प्राणिति, पराणिति: the न् of अन् after a preverb's र्.

    Reads: `dhatu:an` on the piece; the न् not at the end of a pada (that is
    8.4.20's); not `sabhyasa` (8.4.21's).
    """
    for hit in _hits_8_4_19(v):
        yield _apply(hit)


@_provides("8.4.20", PREVERB_KIND)
def _hits_8_4_20(v: View) -> Iterator[Hit]:
    yield from _hits_of_root(
        v, "8.4.20", (_ani(),), final=True,
        what="the root is अन् and its न् ends a pada")


@rule("8.4.20", name=_name("8.4.20"), families=_vidhi("8.4.20"),
      overrides=(("8.4.37", _quote(
          "8.4.20", "kashika", "पदान्तस्य इति प्रतिषेधस्यापवादोऽयम्")),))
def antah(v: View):
    """अन्तः — हे प्राण्, हे पराण्: अन्'s न् even at a word's end.

    An अपवाद of 8.4.37's refusal (Kāśikā). Reads: `dhatu:an`, and that the न्
    ends a pada (`v.pada_final`).
    """
    for hit in _hits_8_4_20(v):
        yield _apply(hit)


@_provides("8.4.21", PREVERB_KIND)
def _hits_8_4_21(v: View) -> Iterator[Hit]:
    for w, word in enumerate(v.state.words):
        value = word.flag_value("dhatu")
        if not value or not word.has("sabhyasa") or _root(value).key != _ani():
            continue
        ns = [s for s in v.word_sights(w) if s.s == STHANIN()]
        if not ns:
            continue
        reach = _pre_reach(v, ns[0])
        if reach is None:
            continue
        yield _pre_hit(
            v, "8.4.21", ns[0], reach, also=ns[1:],
            nimitta=f"the reduplicated अन् has {len(ns)} न् and a preverb stands before it",
            what=(f"the root अन् is reduplicated ({{sābhyāsa}}), and "
                  f"*ubhau* makes BOTH its {{n}} sounds cerebral — {len(ns)} of them"))


@rule("8.4.21", name=_name("8.4.21"), families=_vidhi("8.4.21"),
      overrides=(("8.4.19", _quote(
          "8.4.21", "kashika",
          "साभ्यासस्यानितेरुपसर्गस्थाद् निमित्तादुत्तरस्योभयोर्नकारयोर्णकार आदेशो भवति")),))
def ubhau_sabhyasasya(v: View):
    """उभौ साभ्यासस्य — प्राणिणिषति, प्राणिणत्: both न् of the reduplicated अन्, in one step.

    Reads: `dhatu:an` with `sabhyasa`; every न् of that piece. The reduplication
    itself is not derived here — the caller gives the reduplicated piece.
    """
    for hit in _hits_8_4_21(v):
        yield _apply(hit)


def _han(v: View, n: Sight) -> Optional[Root]:
    root = _root_of(v, n)
    return root if root is not None and root.key == "han" else None


def _a_before(v: View, n: Sight) -> bool:
    """*atpūrva*: a short अ right before the न् (1.1.70's तपर keeps out the long)."""
    prev = v.prev(n)
    return prev is not None and prev.s == "a"


@_provides("8.4.22", PREVERB_KIND)
def _hits_8_4_22(v: View) -> Iterator[Hit]:
    vam = _first_consonants("8.4.23", 2)
    for n in _ns(v):
        if _han(v, n) is None or not _a_before(v, n):
            continue
        nxt = v.next(n)
        if nxt is not None and nxt.s in vam:
            continue                     # 8.4.23 makes that an option
        reach = _pre_reach(v, n)
        if reach is None:
            continue
        yield _pre_hit(
            v, "8.4.22", n, reach,
            nimitta="a short अ stands before the न् of हन्",
            what="the root is हन् and a SHORT {a} stands right before its {n}",
            via=(S.tapara("a"),))


@rule("8.4.22", name=_name("8.4.22"), families=_vidhi("8.4.22"))
def hanter_atpurvasya(v: View):
    """हन्तेरत्पूर्वस्य — प्रहण्यते, परिहणनम्: the न् of हन् after a short अ, and a preverb.

    Reads: `dhatu:han`; the sound before the न्. प्रघ्नन्ति (no अ) and
    प्राघानि (a long आ, kept out by तपर) keep their न्. NOT modelled: the
    yoga-vibhāga niyama that reaches वृत्रघ्नः (see COVERAGE).
    """
    for hit in _hits_8_4_22(v):
        yield _apply(hit)


@_provides("8.4.23", PREVERB_KIND)
def _hits_8_4_23(v: View) -> Iterator[Hit]:
    vam = _first_consonants("8.4.23", 2)
    for n in _ns(v):
        if _han(v, n) is None:
            continue
        nxt = v.next(n)
        if nxt is None or nxt.s not in vam:
            continue
        reach = _pre_reach(v, n)
        if reach is None:
            continue
        yield _pre_hit(
            v, "8.4.23", n, reach,
            nimitta=f"{sk(nxt.s)} follows the न् of हन्",
            what=(f"the root is हन् and {sk(nxt.s)} follows its {{n}}; the "
                  f"cerebral 8.4.22 would give is an OPTION here ({{vā}}, a "
                  f"prāpta-vibhāṣā: it takes the place of the certain rule)"),
            optional=VA)


@rule("8.4.23", name=_name("8.4.23"), families=_vidhi("8.4.23"))
def vamor_va(v: View):
    """वमोर्वा — प्रहण्वः, प्रहन्वः; प्रहण्मः, प्रहन्मः: optional before व् or म्.

    Reads: `dhatu:han`; the sound after the न्. Forks. 8.4.22 leaves these
    न् to it (a प्राप्तविभाषा displaces the certain rule, it does not wait on it).
    """
    for hit in _hits_8_4_23(v):
        yield _apply(hit)


ANTAR = "antar"


def _antar_reach(v: View, n: Sight) -> Optional[Reach]:
    return _reach_in(v, n, lambda word: word.text == ANTAR)


def _antar_hits(v: View, sutra: str, n_ok, what: str) -> Iterator[Hit]:
    for n in _ns(v):
        if not n_ok(v, n) or _unit_has(v, n, "desa"):
            continue
        reach = _antar_reach(v, n)
        if reach is None:
            continue
        yield _hit(
            v, sutra, n, reach,
            nimitta=f"*{ANTAR}* stands before it and no place is named",
            because=(f"the {{n}} of '{v.word(n).text}' follows the "
                     f"{sk(reach.cause.s)} of *{ANTAR}*, {_between_phrase(reach)}; "
                     f"{what}, and no PLACE is named ({{adeśa}}: the caller "
                     f"gave no `desa`), so it is replaced by {sk(ADESA_N())}"))


@_provides("8.4.24", PREVERB_KIND)
def _hits_8_4_24(v: View) -> Iterator[Hit]:
    yield from _antar_hits(
        v, "8.4.24", lambda v, n: _han(v, n) is not None and _a_before(v, n),
        "the root is हन् with a short {a} before its {n}")


@rule("8.4.24", name=_name("8.4.24"), families=_vidhi("8.4.24"))
def antaradese(v: View):
    """अन्तरदेशे — अन्तर्हण्यते, अन्तर्हणनं वर्तते: हन्'s न् after अन्तर्, where no place is named.

    Reads: the text `antar` (which is no preverb by itself — the Kaumudī's
    vārttika on 8.4.16 makes it one for these); `dhatu:han`; no `desa`.
    अन्तर्हननो देशः keeps its न्.
    """
    for hit in _hits_8_4_24(v):
        yield _apply(hit)


@_provides("8.4.25", PREVERB_KIND)
def _hits_8_4_25(v: View) -> Iterator[Hit]:
    yield from _antar_hits(
        v, "8.4.25", lambda v, n: v.word(n).text == "ayana",
        "the word is *ayana*")


@rule("8.4.25", name=_name("8.4.25"), families=_vidhi("8.4.25"))
def ayanam_ca(v: View):
    """अयनं च — अन्तरयणं वर्तते: अयन's न् after अन्तर्, where no place is named.

    Reads: the text `ayana`; the text `antar`; no `desa`. अन्तरयनो देशः keeps its न्.
    """
    for hit in _hits_8_4_25(v):
        yield _apply(hit)


@_provides("8.4.26", SEAM_KIND)
def _hits_8_4_26(v: View) -> Iterator[Hit]:
    padas = _padas(v)
    for n in _ns(v):
        if _left_to_8_3_24(v, n):
            continue
        reach = _walk(v, n, RVARNA())
        if reach is None or padas[reach.cause.w] == padas[n.w]:
            continue
        if not v.state.words[reach.cause.w].has("avagraha") \
                or SAMASA not in _crossed(v, reach, n):
            continue
        yield _hit(
            v, "8.4.26", n, reach, own_rvarna=True,
            nimitta="the first member ends in ऋ and the padapāṭha separates it",
            because=_seam_because(
                v, n, reach,
                "the first member ends in ऋ and the padapāṭha separates it "
                "(*avagraha*, as the caller says) — in the Veda"))


@rule("8.4.26", name=_name("8.4.26"), families=_vidhi("8.4.26"), vedic=True)
def chandasy_ravagrahat(v: View):
    """छन्दस्यृदवग्रहात् — नृमणाः, पितृयाणम्: after an ऋ-final first member the padapāṭha splits (Vedic).

    Reads: `avagraha` on the first member; `veda=True`. The cause is the ऋ
    itself, named by the sūtra (so no vārttika here).
    """
    for hit in _hits_8_4_26(v):
        yield _apply(hit)


@_provides("8.4.27", PREVERB_KIND)
def _hits_8_4_27(v: View) -> Iterator[Hit]:
    uru_su = ("uru", "ṣu")
    for n in _ns(v):
        if v.word(n).text != "nas":
            continue
        reach = _reach_in(v, n, lambda w: w.flag_value("dhatu") is not None
                          or w.text in uru_su)
        if reach is None:
            continue
        word = v.word(reach.cause)
        where = (f"the root '{word.flag_value('dhatu')}' (dhātusthāt)"
                 if word.flag_value("dhatu") else f"*{word.text}*")
        yield _hit(
            v, "8.4.27", n, reach,
            nimitta=f"{sk(reach.cause.s)} stands in {where}",
            because=(f"the {{n}} of *nas* follows the {sk(reach.cause.s)} of "
                     f"{where}, {_between_phrase(reach)}, in the Veda, so it "
                     f"is replaced by {sk(ADESA_N())}"),
            via=_ang_via(v, reach, n))


@rule("8.4.27", name=_name("8.4.27"), families=_vidhi("8.4.27"), vedic=True)
def nas_ca_dhatusthoru(v: View):
    """नश्च धातुस्थोरुषुभ्यः — अग्ने रक्षा णः, उरु णस्कृधि, अभी षु णः (Vedic).

    Reads: the text `nas`; a `dhatu:` piece, or the text `uru` or `ṣu`, before
    it; `veda=True`.
    """
    for hit in _hits_8_4_27(v):
        yield _apply(hit)


@_provides("8.4.28", PREVERB_KIND)
def _hits_8_4_28(v: View) -> Iterator[Hit]:
    for n in _ns(v):
        if v.word(n).text not in ("nas", "nasa"):
            continue
        reach = _pre_reach(v, n)
        if reach is None:
            continue
        yield _pre_hit(
            v, "8.4.28", n, reach,
            nimitta="नस् after a preverb",
            what=(f"the word is *{v.word(n).text}* and *bahulam* makes it "
                  f"'sometimes so, sometimes not' — in the language as well "
                  f"as the Veda (Kāśikā)"),
            optional=BAHULAM)


@rule("8.4.28", name=_name("8.4.28"), families=_vidhi("8.4.28"))
def upasargad_bahulam(v: View):
    """उपसर्गाद् बहुलम् — प्रणसः, प्रणसं मुखम्; प्र नो मुञ्चतम् (unchanged): varied, after a preverb.

    Reads: the text `nas` or `nasa`; `upasarga`. Forks: बहुलम् is the
    sūtra's own word for the option.
    """
    for hit in _hits_8_4_28(v):
        yield _apply(hit)


# 8.4.29–33: the न् of a कृत् after a vowel, and what the root does to it.


def _root_before(v: View, w: int) -> Optional[Root]:
    """The root of the कृत् piece `w`: the nearest earlier piece flagged `dhatu`."""
    for x in range(w - 1, -1, -1):
        value = v.state.words[x].flag_value("dhatu")
        if value:
            return _root(value)
        if v.state.bounds[x] == PADA:
            break
    return None


def _krt_places(v: View):
    """(न्, its cause, the root) for every न् of a कृत् that stands after a vowel
    (*acaḥ*) with a preverb's cause before it."""
    for n in _ns(v):
        if not v.word(n).has("krt"):
            continue
        prev = v.prev(n)
        if prev is None or not prev.is_vowel:
            continue
        reach = _pre_reach(v, n)
        if reach is None:
            continue
        yield n, reach, _root_before(v, n.w)


def _hal_ik(root: Optional[Root]) -> bool:
    """8.4.31's *halaś ca ijupadhāt*: a root beginning with a consonant whose
    penultimate sound is an इक् — as enunciated in the dhātupāṭha."""
    return root is not None and bool(root.shapes()) and all(
        len(shape) > 1 and shape[0] in HAL and S.is_member(shape[-2], "iK")
        for shape in root.shapes())


def _krt_hit(v: View, sutra: str, n: Sight, reach: Reach, what: str,
             optional: str = "", root: Optional[Root] = None) -> Hit:
    prev = v.prev(n)
    return _pre_hit(
        v, sutra, n, reach, optional=optional,
        nimitta=f"the {{n}} of a कृत् after the vowel {sk(prev.s)}",
        what=(f"the {{n}} belongs to a कृत् ({{kṛt}}, as the caller says) and "
              f"stands after the vowel {sk(prev.s)} ({{ac}}); {what}"),
        facts={"root": root.value if root else ""})


@_provides("8.4.29", PREVERB_KIND)
def _hits_8_4_29(v: View) -> Iterator[Hit]:
    for n, reach, root in _krt_places(v):
        if v.word(n).has("nyanta") or _hal_ik(root):
            continue                       # 8.4.30, 8.4.31: an option instead
        yield _krt_hit(v, "8.4.29", n, reach, "8.4.29 asks nothing more of the root",
                       root=root)


@rule("8.4.29", name=_name("8.4.29"), families=_vidhi("8.4.29"))
def krt_acah(v: View):
    """कृत्यचः — प्रयाणम्, प्रमाणम्, प्रयाणीयम्, प्रहीणः: the कृत् न् after a vowel, after a preverb.

    Reads: `krt` on the piece; `upasarga`; the vowel before the न्. प्रमग्नः (the
    न् after ग्) keeps its न्. Where the कृत् is on a णिच् stem (`nyanta`, 8.4.30)
    or the root is halādi with an इक्-उपधा (8.4.31) the choice is theirs.
    """
    for hit in _hits_8_4_29(v):
        yield _apply(hit)


@_provides("8.4.30", PREVERB_KIND)
def _hits_8_4_30(v: View) -> Iterator[Hit]:
    for n, reach, root in _krt_places(v):
        if v.word(n).has("nyanta"):
            yield _krt_hit(
                v, "8.4.30", n, reach,
                "the कृत् was added to a णिच् stem ({ṇyanta}, as the caller says), "
                "where the cerebral is an OPTION ({vibhāṣā}, a prāpta-vibhāṣā: "
                "it takes the place of 8.4.29's)", optional=VIBHASA, root=root)


@rule("8.4.30", name=_name("8.4.30"), families=_vidhi("8.4.30"),
      overrides=(("8.4.29", _quote(
          "8.4.30", "kashika",
          "ण्यन्ताद् यो विहितः कृत्प्रत्ययः तत्स्थस्य नकारस्योपसर्गस्थाद् निमित्तादुत्तरस्य "
          "विभाषा णकारादेशो भवति")),))
def nervibhasa(v: View):
    """णेर्विभाषा — प्रयापणम्, प्रयापनम्; प्रयाप्यमाणम्, प्रयाप्यमानम्: optional, for a कृत् on a णिच् stem.

    Reads: `nyanta` on the कृत् piece (the *vihita* is why a यक् between does not
    matter). Forks.
    """
    for hit in _hits_8_4_30(v):
        yield _apply(hit)


@_provides("8.4.31", PREVERB_KIND)
def _hits_8_4_31(v: View) -> Iterator[Hit]:
    for n, reach, root in _krt_places(v):
        if not v.word(n).has("nyanta") and _hal_ik(root):
            yield _krt_hit(
                v, "8.4.31", n, reach,
                f"the root {root.why()}, begins with a consonant and has an इक् "
                f"before its last sound ({{ijupadha}}), so the cerebral is an "
                f"OPTION ({{vibhāṣā}})", optional=VIBHASA, root=root)


@rule("8.4.31", name=_name("8.4.31"), families=_vidhi("8.4.31"),
      overrides=(("8.4.29", _quote("8.4.31", "kashika",
                                   "कृत्यच इति नित्ये प्राप्ते विकल्पः")),))
def halas_ca_ijupadhat(v: View):
    """हलश्चेजुपधात् — प्रकोपणम्, प्रकोपनम्: optional, when the root begins with a consonant and has an इक् उपधा.

    Reads: `dhatu:ROOT` on the root piece before the कृत्, its shape from the
    dhātupāṭha. प्रेहणम् (a vowel-initial root), प्रवपणम् (उपधा अ) are 8.4.29's.
    Forks.
    """
    for hit in _hits_8_4_31(v):
        yield _apply(hit)


def _sanuma(root: Optional[Root]) -> bool:
    """A root that ends in a consonant and has a नुम् (is इदित्, 7.1.58)."""
    return root is not None and root.idit() and all(
        shape[-1] in HAL for shape in root.shapes())


def _ijadi(root: Root) -> bool:
    return all(S.is_member(shape[0], "ic") for shape in root.shapes())


@_provides("8.4.32", PREVERB_KIND)
def _hits_8_4_32(v: View) -> Iterator[Hit]:
    for n, reach, root in _krt_places(v):
        if _sanuma(root) and _ijadi(root) and not v.word(n).has("nyanta"):
            yield _krt_hit(
                v, "8.4.32", n, reach,
                f"the root {root.why()}, begins with an इच् vowel ({{ijādi}}) "
                f"and has a नुम् ({{sanuma}}), so the cerebral is certain",
                root=root)


def _niyama_8_4_32(v: View) -> Iterator[Tuple[Hit, Root]]:
    for n, reach, root in _krt_places(v):
        if _sanuma(root) and not _ijadi(root):
            yield _krt_hit(v, "8.4.32", n, reach, "", root=root), root


@rule("8.4.32", name=_name("8.4.32"), families=_vidhi("8.4.32"),
      overrides=(("8.4.29", _quote(
          "8.4.32", "kashika",
          "सिद्धे सत्यारम्भो नियमार्थः — इजादेरेव सनुमः नान्यस्मादिति")),
                 ("8.4.31", _quote(
          "8.4.32", "kashika",
          "सिद्धे सत्यारम्भो नियमार्थः — इजादेरेव सनुमः नान्यस्मादिति"))))
def ijader_sanumah(v: View):
    """इजादेः सनुमः — प्रेङ्खणम्, प्रेङ्गणम्, प्रोम्भणम्: the कृत् न् when the root is इजादि and has a नुम्.

    A niyama (Kāśikā): only an इजादि root that has a नुम् — so प्रमङ्गनम्, परिमङ्गनम्
    (मङ्ग् has a नुम् and begins with म्) is REFUSED here. Reads: `dhatu:ROOT`, its
    enunciation from the dhātupāṭha (इदित् → नुम्). Where the name is read in
    entries with and without the mark, the mark is taken and the step says so.
    """
    for hit in _hits_8_4_32(v):
        yield _apply(hit)
    for hit, root in _niyama_8_4_32(v):
        yield _refuse(
            hit, nimitta=f"the root '{root.value}' has a नुम् but is not इजादि",
            because=(f"the root {root.why()}, has a नुम् ({{sanuma}}) but does not "
                     f"begin with an इच् vowel; 8.4.32 is a niyama — a नुम्-root "
                     f"takes the cerebral only if it is इजादि — so {sk(STHANIN())} "
                     f"stays"))


@_provides("8.4.33", PREVERB_KIND)
def _hits_8_4_33(v: View) -> Iterator[Hit]:
    for n in _ns(v):
        root = _root_of(v, n)
        if root is None or not _nimsadi(root):
            continue
        reach = _pre_reach(v, n)
        if reach is None:
            continue
        yield _pre_hit(
            v, "8.4.33", n, reach, optional=VA,
            nimitta=f"the root '{root.value}' is one of निंस्, निक्ष्, निन्द्",
            what=(f"the root is one of निंस्, निक्ष्, निन्द् — "
                  + _quote("8.4.33", "kashika",
                           "णोपदेशत्वादेतेषां नित्ये प्राप्ते विकल्पः")))


@rule("8.4.33", name=_name("8.4.33"), families=_vidhi("8.4.33"))
def va_nimsanikshanindam(v: View):
    """वा निंसनिक्षनिन्दाम् — प्रणिंसनम्, प्रनिंसनम्; प्रणिक्षणम्; प्रणिन्दनम्: optional for these three roots.

    Reads: `dhatu:ROOT` (`niṃs`, `nikṣ`, `nind`); `upasarga`. They are
    ṇopadeśa, so 8.4.14 would make the cerebral certain — it leaves them to this
    (a प्राप्तविभाषा). OPEN: the Kaumudī adds *कृति परे*; the Kāśikā does not,
    and is followed. Forks.
    """
    for hit in _hits_8_4_33(v):
        yield _apply(hit)


# ---------------------------------------------------------------------------
# 8.4.34–39 — what takes it back
# ---------------------------------------------------------------------------
#
# Each refusal asks the vidhis' own generators (`HITS`) where they would give ण्
# and refuses those places, on exactly their sounds. What each refuses is a
# list of sūtras, so the engine's `overrides` can say so, with the Kāśikā's
# words for a reason.


def _ids(*kinds: str, without: Sequence[str] = ()) -> Tuple[str, ...]:
    """The sūtras whose vidhis work in these kinds of place."""
    found: List[str] = []
    for key in HITS:
        sid = key.split()[0]
        if KIND[key] in kinds and sid not in found and sid not in without:
            found.append(sid)
    return tuple(found)


ALL_KINDS = (PADA_KIND, SEAM_KIND, PREVERB_KIND)


def _refusing(reason: str, ids: Iterable[str]) -> Tuple[Tuple[str, str], ...]:
    return tuple((_tgt(sid), reason) for sid in ids)


def _once(apps: Iterable[Application]) -> Iterator[Application]:
    seen = set()
    for app in apps:
        if app.site not in seen:
            seen.add(app.site)
            yield app


_BHADI_NAMES = None


def _bhadi() -> FrozenSet[str]:
    return _rooted(BHADI())


_Q34 = _quote("8.4.34", "kashika",
              "भा भू पू कमि गमि प्यायी वेप इत्येतेषामुपसर्गस्थाद् निमित्तादुत्तरस्य "
              "कृत्स्थस्य नकारस्य णकारादेशो न भवति")


def _hits_bhadi(v: View) -> Iterator[Tuple[Hit, Root]]:
    for hit in _hits_in(v, PREVERB_KIND):
        if hit.sutra not in ("8.4.29", "8.4.30", "8.4.31", "8.4.32"):
            continue
        root = _root(hit.fact("root")) if hit.fact("root") else None
        if root is None or not _is(root, _bhadi()):
            continue
        if root.key == "pū" and root.value.startswith("pūṅ"):
            continue   # Kātyāyana: पूञ एवेह ग्रहणम् — the ṅit पूङ् does take it
        yield hit, root


@rule("8.4.34", name=_name("8.4.34"), families=_nisedha("8.4.34"),
      overrides=_refusing(_Q34, ("8.4.29", "8.4.30", "8.4.31", "8.4.32")))
def na_bhabhupukamigamipyayivepam(v: View):
    """न भाभूपूकमिगमिप्यायीवेपाम् — प्रभानम्, प्रभवनम्, प्रपवनम्, प्रगमनम्: not for these seven roots.

    Refuses 8.4.29–32 where the कृत्'s root is one of the seven (the Kāśikā's
    list, read from it). Reads: `dhatu:ROOT`. पूङ् (the ṅit) is not पू here
    (Kātyāyana): प्रपवणं सोमस्य takes ण्.
    """
    yield from _once(
        _refuse(hit, nimitta=f"the root of the कृत् is '{root.value}'",
                because=(f"the कृत् is on the root '{root.value}', one of the "
                         f"seven the sūtra names (bhā, bhū, pū, kam, gam, "
                         f"pyāy, vep), so the cerebral of {hit.sutra} is refused "
                         f"and the {{n}} stays"))
        for hit, root in _hits_bhadi(v))


_Q35 = _quote("8.4.35", "kashika",
              "षकारात् पदान्तादुत्तरस्य नकारस्य णकारादेशो न भवति")


@rule("8.4.35", name=_name("8.4.35"), families=_nisedha("8.4.35"),
      overrides=_refusing(_Q35, _ids(SEAM_KIND, PREVERB_KIND,
                                     without=("8.4.39",))))
def sat_padantat(v: View):
    """षात् पदान्तात् — निष्पानम्, दुष्पानम्, सर्पिष्पानम्, यजुष्पानम्: not after a ष् that ends a pada.

    Refuses any vidhi of 8.4.3–33 whose cause is a ष् ending its pada
    (`v.pada_final`). निर्णयः (a र्, so no) and कुष्णाति (the ष् is inside its pada)
    are not this rule's; सुसर्पिष्केण keeps its ण् — *padānta* is a locative
    compound, the end IN a pada (Kāśikā).
    """
    sha = _first_consonants("8.4.35", 1)[0]
    yield from _once(
        _refuse(hit, nimitta=f"the cause {sk(sha)} ends a pada",
                because=(f"the cause, the {sk(sha)} of "
                         f"'{v.word(hit.reach.cause).text}', is the LAST sound of "
                         f"a pada ({{padānta}}), so the cerebral of {hit.sutra} "
                         f"is refused and the {{n}} stays"))
        for hit in _hits_in(v, SEAM_KIND, PREVERB_KIND)
        if hit.reach.cause.s == sha and v.pada_final(hit.reach.cause))


_Q36 = _quote("8.4.36", "kashika", "नशेः षकारान्तस्य णकारादेशो न भवति")


def _nash(v: View, n: Sight) -> bool:
    root = _root_of(v, n)
    word = v.word(n)
    return (root is not None
            and root.key == _sutra_words("8.4.36")[0][:-2]
            and (word.text.endswith("ṣ") or word.has("santa")))


@rule("8.4.36", name=_name("8.4.36"), families=_nisedha("8.4.36"),
      overrides=_refusing(_Q36, _ids(PREVERB_KIND, without=("8.4.39",))))
def naseh_santasya(v: View):
    """नशेः षान्तस्य — प्रनष्टः, परिनष्टः, प्रनङ्क्ष्यति: not the न् of नश् in its ष्-final shape.

    Reads: `dhatu:naś` and that the piece ends in ष् — or `santa`, the caller's
    word that it once did (the *antagrahaṇa*: प्रनङ्क्ष्यति). प्रणश्यति (श्-final)
    takes ण्. OPEN/SCOPE: the past ष् is a flag, not derived.
    """
    yield from _once(
        _refuse(hit, nimitta="नश् in its ष्-final shape",
                because=(f"the root नश् stands here as '{v.word(hit.n).text}', "
                         f"ष्-final (or once so: the caller's `santa`), so the "
                         f"cerebral of {hit.sutra} is refused and the {{n}} stays"))
        for hit in _hits_in(v, PREVERB_KIND) if _nash(v, hit.n))


_Q37 = _quote("8.4.37", "kashika", "पदान्तो यो नकारस्तस्य णकारादेशो न भवति")


@rule("8.4.37", name=_name("8.4.37"), families=_nisedha("8.4.37"),
      overrides=_refusing(_Q37, _ids(*ALL_KINDS, without=("8.4.39", "8.4.20"))))
def padantasya(v: View):
    """पदान्तस्य — वृक्षान्, प्लक्षान्, अरीन्, गिरीन्: not the न् that ends a pada.

    Refuses every vidhi at a न् that is the last sound of a pada, except
    8.4.20, which is its अपवाद. OPEN: the Bhāṣya rejects this sūtra
    (Tattvabodhinī on 8.4.1) as carried down from 8.3.55; the Kāśikā and Kaumudī
    keep it, and it is what shows the refusal.
    """
    yield from _once(
        _refuse(hit, nimitta="the न् ends a pada",
                because=(f"the {{n}} of '{v.word(hit.n).text}' is the LAST sound "
                         f"of a pada ({{padānta}}), so the cerebral of "
                         f"{hit.sutra} is refused and it stays"))
        for hit in _hits_in(v, *ALL_KINDS) if v.pada_final(hit.n))


_Q38 = _quote("8.4.38", "kashika",
              "पदेन व्यवायेऽपि सति निमित्तनिमित्तिनोर्नकारस्य णकारादेशो न भवति")


@rule("8.4.38", name=_name("8.4.38"), families=_nisedha("8.4.38"),
      overrides=_refusing(_Q38, _ids(SEAM_KIND, PREVERB_KIND,
                                     without=("8.4.39",))))
def padavyavaye_pi(v: View):
    """पदव्यवायेऽपि — माषकुम्भवापेन, प्र गां नयामः, परि गां नयामः: not where a whole word stands between.

    Refuses every vidhi of 8.4.3–33 whose cause and न् have a whole pada
    (`_whole_padas_between`) between them. The preverb आङ् is not counted —
    8.4.2 names it (*पर्याणद्धम्*) — and neither is a piece joined to the न्'s
    pada by ANGA (a तद्धित: आर्द्रगोमयेण, Kātyāyana's *अतद्धिते*).
    """
    yield from _once(
        _refuse(hit, nimitta="a whole word stands between",
                because=(f"the cause, the {sk(hit.reach.cause.s)} of "
                         f"'{v.word(hit.reach.cause).text}', and the {{n}} of "
                         f"'{v.word(hit.n).text}' have "
                         f"'{_shown(s for s in hit.reach.between if _padas(v)[s.w] in _whole_padas_between(v, hit.reach, hit.n))}' "
                         f"— a whole pada ({{pada}}) — between them "
                         f"({{padavyavāya}}), so the cerebral of {hit.sutra} "
                         f"is refused and the {{n}} stays"))
        for hit in _hits_in(v, SEAM_KIND, PREVERB_KIND)
        if _whole_padas_between(v, hit.reach, hit.n))


_Q39 = _quote("8.4.39", "kashika",
              "क्षुभ्ना इत्येवमादिषु शब्देषु नकारस्य णकारादेशो न भवति")


def _ksubhnadi(v: View, n: Sight) -> str:
    """Why `n` belongs to the क्षुभ्नादि, or "". Only what can be read: the word the
    sūtra names, the Kāśikā's second members (in a name), the caller's flag."""
    unit = v.unit_of(n, across=(ANGA,))
    upto = "".join(s.s for s in unit if v.index(s) <= v.index(n))
    if upto.endswith(_ksubhna_prefix()):
        return "it is the न् of *kṣubhnā*, the word the sūtra names (and its altered shapes)"
    if _unit_has(v, n, "ksubhnadi"):
        return "the caller says the word belongs to the आकृतिगण"
    if v.word(n).text in _uttarapadas_of_ksubhnadi() \
            and _unit_has(v, n, "samjna"):
        return (f"'{v.word(n).text}' is one of the second members the Kāśikā "
                f"names, which keep it in a NAME")
    return ""


@rule("8.4.39", name=_name("8.4.39"), families=_nisedha("8.4.39"),
      overrides=_refusing(_Q39, _ids(*ALL_KINDS, without=("8.4.39",))))
def ksubhnadisu_ca(v: View):
    """क्षुभ्नादिषु च — क्षुभ्नाति, क्षुभ्नीतः, हरिनन्दी, परिनन्दनम्, गिरिनगरम्: not in these words.

    Refuses every vidhi at a न् of the क्षुभ्नादि. An आकृतिगण: what is read is
    the word the sūtra names (*kṣubhnā* with its altered shapes), the second
    members the Kāśikā names (in a name: `samjna`), and the caller's
    `ksubhnadi`. The gaṇasūtra आचार्यादणत्वं च and the Kāśikā's नृनमनः, तृप्नु
    are only by the flag.
    """
    yield from _once(
        _refuse(hit, nimitta="the word is in the क्षुभ्नादि",
                because=(f"the {{n}} of '{v.word(hit.n).text}' is in the "
                         f"क्षुभ्नादि: {why}, so the cerebral of {hit.sutra} "
                         f"is refused and it stays"))
        for hit in _hits_in(v, *ALL_KINDS)
        for why in [_ksubhnadi(v, hit.n)] if why)


_DUR = "दुरः षत्वणत्वयोरुपसर्गत्वप्रतिषेधो वक्तव्यः"
_QDUR = _quote("8.4.16", "kaumudi", _DUR)


@rule("8.4.16", name=_name("8.4.16") + " — दुरः", families=_nisedha("8.4.16"),
      authority=VARTTIKA, varttika=_DUR,
      overrides=_refusing(_QDUR, _ids(PREVERB_KIND, without=("8.4.39",))))
def duras_natva_upasargatva_pratisedhah(v: View):
    """दुरः षत्वणत्वयोरुपसर्गत्वप्रतिषेधो वक्तव्यः — दुर्भवानि, दुर्यानम्: दुर् is no preverb for this.

    Refuses 8.4.14–33 where the cause stands in दुर् even if the caller
    flagged it `upasarga`. Kātyāyana's; the trace says so.
    """
    yield from _once(
        _refuse(hit, vartika=_DUR, nimitta="the preverb is दुर्",
                because=(f"the cause is in दुर् ('{v.word(hit.reach.cause).text}'), "
                         f"which for cerebralisation is not an उपसर्ग, so the "
                         f"cerebral of {hit.sutra} is refused and the {{n}} stays"))
        for hit in _hits_in(v, PREVERB_KIND)
        if v.word(hit.reach.cause).text == "dur"
        and v.word(hit.reach.cause).has("upasarga"))


_AGRA = _vartika_text("8.4.39", "अग्रग्रामाभ्यां")


@_provides("8.4.39 अग्रग्रामाभ्याम्", SEAM_KIND)
def _hits_agragrama(v: View) -> Iterator[Hit]:
    firsts = ("agra", "grāma")
    for n, reach, padas in _seams(v, adjacent=True):
        first = _first_member(v, n, padas)
        root = _root_of(v, n)
        if first not in firsts or root is None or root.key != "nī":
            continue
        yield _hit(
            v, "8.4.39", n, reach,
            nimitta=f"the root नी after '{first}'",
            because=_seam_because(
                v, n, reach,
                f"the root is नी after '{first}' (*agraṇīḥ*, *grāmaṇīḥ*) — "
                f"Kātyāyana's addition, whose ण् is laid down whole"))


@rule("8.4.39", name=_name("8.4.39") + " — अग्रग्रामाभ्याम्", families=_vidhi("8.4.39"),
      authority=VARTTIKA, varttika=_AGRA)
def agragramabhyam_nayer_nah(v: View):
    """अग्रग्रामाभ्यां नयतेर्णो वाच्यः — अग्रणीः, ग्रामणीः: the root नी's न् after अग्र or ग्राम.

    Kātyāyana's, and the trace says so. Reads: `dhatu:nī`; the first member's text.
    """
    for hit in _hits_agragrama(v):
        yield _apply(hit, _AGRA)


RULES = (
    raabhyam_no_nah, rvarnac_ca, atkupvannumvyavaye_pi,
    purvapadat_samjnayam_agah, vanam_puragamisrakadibhyah,
    pranirantah_sarekshu, vibhasa_osadhivanaspatibhyah, dvyac_tryac,
    irikadibhyah_pratisedhah, ahno_dantat, vahanam_ahitat, panam_dese,
    va_bhavakaranayoh, girinadyadinam_va, pratipadikanta_numvibhaktisu_ca,
    yuvader_na, ekajuttarapade_nah, kumati_ca,
    upasargad_asamase_pi_nopadesasya, hinumina, ani_lot, ner_gadanadapata,
    sese_vibhasa, aniteh, antah, ubhau_sabhyasasya, hanter_atpurvasya,
    vamor_va, antaradese, ayanam_ca, chandasy_ravagrahat, nas_ca_dhatusthoru,
    upasargad_bahulam, krt_acah, nervibhasa, halas_ca_ijupadhat,
    ijader_sanumah, va_nimsanikshanindam, na_bhabhupukamigamipyayivepam,
    sat_padantat, naseh_santasya, padantasya, padavyavaye_pi, ksubhnadisu_ca,
    duras_natva_upasargatva_pratisedhah, agragramabhyam_nayer_nah,
)


#: Which sūtras of 8.4.1–39 this module implements, and how — the honest
#: account. `partial` and `scope` say what is not done and why.
COVERAGE = (
    ("8.4.1", "rule", "with Kātyāyana's ऋवर्णात् as its own vārttika rule; a finished word with no join is not offered"),
    ("8.4.2", "rule", ""),
    ("8.4.3", "rule", "the name is the caller's flag `samjna`"),
    ("8.4.4", "rule", "a niyama: ण् after the six, a refusal of 8.4.3 after any other first member"),
    ("8.4.5", "rule", ""),
    ("8.4.6", "rule", "with Kātyāyana's two restrictions as vārttika rules; herb and tree are the caller's flags"),
    ("8.4.7", "rule", ""),
    ("8.4.8", "rule", "what is loaded is the caller's flag `ahita`"),
    ("8.4.9", "rule", "the country is the caller's flag `desa`"),
    ("8.4.10", "partial", "पान is done; of the vārttika's गिरिनद्यादि items only the compounds with a seam are reached (not तर्यमान, माषोन, आर्गयन)"),
    ("8.4.11", "rule", "with the vārttika युवादेर्न as a refusal; num and vibhakti are the caller's flags"),
    ("8.4.12", "rule", ""),
    ("8.4.13", "rule", ""),
    ("8.4.14", "rule", "the root's ṇopadeśa status is read from the dhātupāṭha; where the bare name is read in entries with and without ण् the ण् reading is taken and the step says so"),
    ("8.4.15", "rule", ""),
    ("8.4.16", "rule", "with Kātyāyana's दुरः refusal; अन्तर् counts as a preverb only if the caller flags it"),
    ("8.4.17", "partial", "the अट् augment between नि and the root (प्रण्यगदत्) is not modelled"),
    ("8.4.18", "rule", ""),
    ("8.4.19", "rule", ""),
    ("8.4.20", "rule", "the अपवाद of 8.4.37"),
    ("8.4.21", "partial", "the reduplication is not derived here: the caller gives the reduplicated piece"),
    ("8.4.22", "partial", "only the preverb context; the yoga-vibhāga niyama that the Kaumudī reads to reach वृत्रघ्नः is not modelled"),
    ("8.4.23", "rule", ""),
    ("8.4.24", "rule", "no place is named: the caller's absence of `desa`"),
    ("8.4.25", "rule", "no place is named: the caller's absence of `desa`"),
    ("8.4.26", "vedic", "runs with veda=True; the avagraha is the caller's flag"),
    ("8.4.27", "vedic", "runs with veda=True"),
    ("8.4.28", "rule", "बहुलम् is offered as an option (both courses)"),
    ("8.4.29", "rule", "Kātyāyana's निर्विण्णस्योपसंख्यानम् is not derived"),
    ("8.4.30", "rule", "णिच् is the caller's flag `nyanta`"),
    ("8.4.31", "rule", ""),
    ("8.4.32", "rule", "a niyama: ण् for an इजादि नुम्-root, a refusal for any other नुम्-root"),
    ("8.4.33", "rule", "the Kaumudī's *कृति परे* is not required (Kāśikā followed)"),
    ("8.4.34", "rule", ""),
    ("8.4.35", "rule", ""),
    ("8.4.36", "partial", "the once-ṣ-final shape (प्रनङ्क्ष्यति) is read from the caller's flag `santa`, not derived"),
    ("8.4.37", "rule", "the Bhāṣya rejects it as carried down from 8.3.55; kept here as the visible refusal (OPEN)"),
    ("8.4.38", "rule", ""),
    ("8.4.39", "partial", "an आकृतिगण: only kṣubhnā, the Kāśikā's second members and the caller's flag are read; the गणसूत्र आचार्यादणत्वं च is not; Kātyāyana's अग्रग्रामाभ्याम् is its own vārttika rule"),
)