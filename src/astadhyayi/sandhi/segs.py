# -*- coding: utf-8 -*-
"""
The form under derivation, at the level sandhi acts on: sounds.

`prakriya.py` derives words out of *terms* — a dhātu, an affix — and its rules
read a term's text. Sandhi is different in kind. Nearly every rule reads one or
two **sounds** and asks what stands beside them: is this the last sound of a
pada, does a vowel follow, is a खर् next. So the state here is a row of sounds,
each remembering which word it came from and — the part everything else rests
on — **what it was before the last rule changed it**.

**Why every sound carries its past.** 8.2.1 पूर्वत्रासिद्धम् says that a rule of
the tripādī (8.2.1 to 8.4.68) is *asiddha* — as though not done — to every rule
before it, in the सपादसप्ताध्यायी and in the tripādī itself. That is not a
detail of sandhi but its whole shape, and the Laghusiddhāntakaumudī shows it at
work in three places:

  * **हर इह** (*hara iha*) — 8.3.17 makes the ru a य्, and 8.3.19 may then drop
    it. The अ and इ now stand side by side, and 6.1.87 does **not** join them:
    the loss of the य् is asiddha to 6.1.87, which still sees the य्.
  * **मनोरथः** — रु before र is open to 6.1.114 (→ उ) and to 8.3.14 (→ lost).
    8.3.14 is later, so it cannot compete: *पूर्वत्रासिद्धमिति रोरीत्यस्यासिद्ध-
    त्वादुत्वमेव*.
  * **वाक्पतिः** — 8.2.30, 8.2.39 and 8.4.55 turn च् to क् to ग् to क्. A loop
    that let 8.2.39 look again at the क् 8.4.55 has just made would turn it back
    to ग् for ever.

An engine that simply rewrites a string and lets every rule see the result
gets all three wrong. So a sound made by rule R keeps `prior`, the sound(s) it
replaced, and a rule that comes *before* R in the sense of 8.2.1 is shown the
prior. That is `View`: the row as one particular rule is entitled to see it.
Visibility itself is asked of `asiddha.visible`, not decided here — this module
only carries the history that question needs.

**Two things a rule may see that 8.2.1 would hide, and why.** A rule whose own
wording names the product of a tripādī rule — 6.1.113 अतो रोरप्लुतादप्लुते
reads the रु that 8.2.66 makes; 6.3.111 ढ्रलोपे reads the loss 8.3.13–14 make —
would be idle if 8.2.1 shut it out, and the grammar has a general answer:
वचनप्रामाण्यात्, by the force of the rule's own statement. `Rule.consumes`
names the marks such a rule may see through, and `asiddha.py` already records
the same principle for an अपवाद. It is an explicit, per-rule declaration
because it is an exception, and an exception nobody can see is one nobody
can check.

**Why the ru is a flagged र्, not the two sounds र् + उ.** 8.2.66's substitute is
रु with the उ an इत् (1.3.2, 1.3.9), so by the time anything acts on it only the
र् is left — but 6.1.113 must still tell this र् from the र् of *punar*, which it
does not touch. A mark carries that difference (`RU`) without keeping a sound
that no rule can see.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from functools import lru_cache
from typing import Dict, FrozenSet, List, Optional, Sequence, Tuple

from src.astadhyayi.asiddha import ekadesa_visible, visible
from src.astadhyayi.sivasutra import resolve
from src.astadhyayi.varna import (
    ANUNASIKA_MARK, ANUSVARA, JIHVAMULIYA, SVARA, UPADHMANIYA, VISARGA)


# ---------------------------------------------------------------------------
# Boundaries — what lies between two words
# ---------------------------------------------------------------------------

#: Two padas in unbroken speech. The left word ends a pada.
PADA = "pada"
#: The first member of a compound. A pada all the same — 1.4.14 सुप्तिङन्तं
#: पदम् with the सुँ lost by 2.4.71 but still counted by 1.1.62 — which is why
#: *मनस्* + *रथ* takes the रुत्व of a pada.
SAMASA = "samāsa"
#: A preverb before its dhātu. A pada by 1.4.14 (an indeclinable's sup is
#: elided, 2.4.82), so सम् before सुट् is a pada-final म् for 8.3.5.
UPASARGA = "upasarga"
#: Two pieces of ONE pada — stem and affix, root and vikaraṇa. The left piece
#: is *not* pada-final, which is what separates 8.3.24's अपदान्तस्य from 8.3.23.
ANGA = "aṅga"
#: A pause after the last word (1.4.110 विरामोऽवसानम्). Not a word boundary
#: but the condition 8.3.15 खरवसानयोः and 8.4.56 वाऽवसाने name.
AVASANA = "avasāna"
#: The utterance goes on beyond what was given; there is no pause to speak of.
OPEN = "open"

#: A boundary after which the left word is a पद.
PADA_LIKE: FrozenSet[str] = frozenset({PADA, SAMASA, UPASARGA, AVASANA})

#: The boundary kinds a caller may name.
BOUNDARIES: Tuple[str, ...] = (PADA, SAMASA, UPASARGA, ANGA)


# ---------------------------------------------------------------------------
# Marks a sound can bear
# ---------------------------------------------------------------------------

#: This र् is the रु of 8.2.66, whose उँ has gone as an इत्. 6.1.113–114 act on
#: it and not on a र् that was already there (*punar*, *antar*).
RU = "ru"
#: Uttered through nose and mouth together (1.1.8). Kept apart from the sound
#: so `varna.savarna` and the rest are asked about the plain sound.
ANUNASIKA = "anunāsika"
#: A vowel a prakṛtibhāva rule has left as it is: no sandhi at its junction.
PRAKRTYA = "prakṛtyā"
#: Put in by an āgama rule, not part of either word.
AGAMA = "āgama"
#: Three mātrās (1.2.27), and held by 6.1.125 against any sandhi.
PLUTA = "pluta"
#: Made by a single substitute for two sounds (6.1.84). Carried so that 6.1.86
#: षत्वतुकोरसिद्धः can be asked of it: for a ṣatva or a tuk the substitute is
#: asiddha, and those rules see the sounds it replaced.
EKADESA_MARK = "ekādeśa"
#: The written trace of a vowel that pūrvarūpa (6.1.109) has absorbed: the
#: tradition prints हरेऽव, not हरेव, and the ऽ stands where the अ was.
AVAGRAHA = "avagraha"


# ---------------------------------------------------------------------------
# Classes of sound — read from the śivasūtras, never typed
# ---------------------------------------------------------------------------

#: अच्, every length of every vowel. `varna.SVARA` is 1.1.71's aC widened to
#: the long forms by 1.1.69, so this is asked of it and not written again.
AC: FrozenSet[str] = SVARA
#: हल्, every consonant of the śivasūtras.
HAL: FrozenSet[str] = frozenset(resolve("hal").sounds)
#: The four sounds that need a vowel to be uttered and are neither vowel nor
#: consonant — अनुस्वार, विसर्जनीय, जिह्वामूलीय, उपध्मानीय — which the Kāśikā on
#: 1.1.? calls अयोगवाह. None of them is an अच् or a हल्.
AYOGAVAHA: FrozenSet[str] = frozenset(
    {ANUSVARA, VISARGA, JIHVAMULIYA, UPADHMANIYA})


def base_of(sound: str) -> str:
    """A sound without its anunāsika mark."""
    return sound[: -len(ANUNASIKA_MARK)] if sound.endswith(ANUNASIKA_MARK) \
        else sound


# ---------------------------------------------------------------------------
# One sound, and the word it belongs to
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Seg:
    """
    One sound of the form, with its history.

    `s` is the plain sound in IAST — "a", "ai", "kh", "ṃ", "ḥ" — and is "" once
    the sound has been *lost*: a loss is kept as an empty sound rather than
    removed, because the rules before it must still find what it replaced.
    """

    uid: int
    s: str
    #: Index of the word this sound belongs to.
    w: int
    #: Where a single substitute stands for a sound of each of two words (6.1.84
    #: एकः पूर्वपरयोः), the word of the *earlier* one. 6.1.85 अन्तादिवच्च makes
    #: the substitute the end of that word and the beginning of `w`.
    lw: Optional[int] = None
    marks: FrozenSet[str] = frozenset()
    #: The sūtra that made this sound, "" if it is part of the input.
    made_by: str = ""
    #: What stood here before `made_by` acted. Empty for an āgama, which had
    #: no predecessor — so a rule before it sees nothing at all.
    prior: Tuple["Seg", ...] = ()
    #: How a trace should print it where that is not `s` — the रु is printed
    #: "ru", which is what the tradition writes.
    show: str = ""

    @property
    def nasal(self) -> bool:
        return ANUNASIKA in self.marks

    @property
    def sound(self) -> str:
        """The sound as `varna` and `savarna` are asked about it."""
        return self.s + (ANUNASIKA_MARK if self.nasal else "")

    @property
    def elided(self) -> bool:
        return self.s == ""

    def text(self) -> str:
        return self.show or self.sound

    def has(self, mark: str) -> bool:
        return mark in self.marks


@dataclass(frozen=True)
class Word:
    """A word or morpheme as given, and what the letters cannot say about it."""

    text: str
    given: str = ""
    #: Facts about the word no reading of its letters settles — that it is a
    #: dual (1.1.11), a particle (1.1.14), the preverb आङ्, a vocative, that its
    #: root is √इ. The caller says so; see NORTH_STAR §5 on semantic conditions.
    flags: FrozenSet[str] = frozenset()
    #: Flags the parser filled in itself, as (flag, why). Shown in the trace,
    #: so an assumption is never mistaken for something the caller said.
    inferred: Tuple[Tuple[str, str], ...] = ()

    def has(self, flag: str) -> bool:
        return flag in self.flags

    def flag_value(self, name: str) -> Optional[str]:
        """The value of a flag written name:value — "dhātu:i" gives "i"."""
        for flag in self.flags:
            head, _, tail = flag.partition(":")
            if head == name and tail:
                return tail
        return None


@dataclass(frozen=True)
class State:
    """The whole form at one moment."""

    segs: Tuple[Seg, ...]
    words: Tuple[Word, ...]
    #: What follows each word: a boundary kind, or AVASANA / OPEN for the last.
    bounds: Tuple[str, ...]
    veda: bool = False
    next_uid: int = 0
    #: Options the derivation has declined, as (sūtra, site) so a rule that was
    #: offered and refused is not offered again at the same place.
    declined: FrozenSet[Tuple[str, Tuple[int, ...]]] = frozenset()  # (Rule.key, site)

    def fresh(self, count: int = 1) -> Tuple["State", Tuple[int, ...]]:
        uids = tuple(range(self.next_uid, self.next_uid + count))
        return replace(self, next_uid=self.next_uid + count), uids

    def index_of(self, uid: int) -> int:
        for index, seg in enumerate(self.segs):
            if seg.uid == uid:
                return index
        raise KeyError(uid)

    def joined(self) -> str:
        """
        The form as one unbroken saṃhitā: no spaces.

        A रु that nothing has turned into anything else is printed as the र् it
        is — its उ is an इत् (1.3.2) and gone (1.3.9) — so a word that ends in
        one, अग्निर् in *अग्निर् अत्र*, is not printed with a `ru` no one
        speaks. (`text` shows the रु while a derivation is still in progress.)
        """
        return "".join(seg.sound for seg in self.segs)

    def text(self, final: bool = False) -> str:
        """
        The form with a space where two words still stand apart.

        A single substitute of two sounds (an एकादेश) has joined its two words
        at that point, and no space is printed there — the tradition writes
        रामेह and not रामे ह. `final` prints what is spoken, without the
        रु an unfinished derivation shows.
        """
        return _spaced(self.segs, final)


def _words(seg: Seg) -> FrozenSet[int]:
    """
    The words a sound belongs to: one, or — for the single substitute of 6.1.84
    that stands for a sound of each — every word from the earliest one it
    stands for to its own (6.1.85 अन्तादिवच्च).

    A range and not a pair, because substitutes chain: *kṛṣṇa* + *a* + *i*
    joins the first two, and the result joins the third. If the second join
    remembered only its nearest neighbour, the ष्ण् left of *kṛṣṇa* would look
    like the end of the word and 8.2.23 would strip it.
    """
    return frozenset({seg.w}) if seg.lw is None else frozenset(
        range(seg.lw, seg.w + 1))


#: Between two vowels of one word that are still two sounds. Written together
#: they would read as a diphthong — `a` and `u` as `au` — in IAST and,
#: worse, as औ in Devanāgarī, so the trace marks the hiatus. It appears only in
#: the intermediate forms a trace shows; `State.joined()` never carries it.
HIATUS = "·"


def _spaced(segs: Sequence[Seg], final: bool = False) -> str:
    live = [seg for seg in segs if not seg.elided]
    out: List[str] = []
    for index, seg in enumerate(live):
        if index:
            prev = live[index - 1]
            if not (_words(prev) & _words(seg)):
                out.append(" ")
            elif prev.s in AC and seg.s in AC:
                out.append(HIATUS)
        out.append(seg.sound if final else seg.text())
    return "".join(out)


# ---------------------------------------------------------------------------
# What a given rule is entitled to see — 8.2.1
# ---------------------------------------------------------------------------


@lru_cache(maxsize=None)
def _asiddha(done: str, viewer: str) -> bool:
    """Whether the work of sūtra `done` is hidden from sūtra `viewer`."""
    return visible(done, viewer).asiddha


@dataclass(frozen=True)
class Sight:
    """One sound as one rule sees it."""

    seg: Seg
    #: Index in `State.segs` of the sound that really stands here.
    real: int
    #: True when `seg` is an ancestor of the real sound, because the real one
    #: was made by a rule this viewer cannot see. A rule may not edit what it
    #: sees only through its past.
    through: bool = False
    #: The uid of the sound that really stands here — the stable name of a
    #: *place*, which is what two rules contending for it have in common.
    real_uid: int = -1

    @property
    def s(self) -> str:
        return self.seg.s

    @property
    def sound(self) -> str:
        return self.seg.sound

    @property
    def uid(self) -> int:
        return self.seg.uid

    @property
    def w(self) -> int:
        return self.seg.w

    @property
    def marks(self) -> FrozenSet[str]:
        return self.seg.marks

    def has(self, mark: str) -> bool:
        return mark in self.seg.marks

    @property
    def is_vowel(self) -> bool:
        return self.seg.s in AC

    @property
    def is_consonant(self) -> bool:
        return self.seg.s in HAL

    @property
    def is_ayogavaha(self) -> bool:
        return self.seg.s in AYOGAVAHA


#: Two sounds of one word — not a junction of words.
WITHIN = "within"


@dataclass(frozen=True)
class Junction:
    """Two adjacent sounds, and what lies between them."""

    left: Sight
    right: Sight
    #: WITHIN if both belong to one word; otherwise the boundary kind.
    kind: str

    @property
    def between_words(self) -> bool:
        return self.kind != WITHIN


class View:
    """
    The row of sounds as the rule `viewer` is entitled to see it.

    Everything a rule asks — is this a pada's last sound, what follows, does a
    vowel come next — it asks of a View and not of the State, so that 8.2.1 is
    applied in one place and cannot be forgotten in one rule.
    """

    def __init__(self, state: State, viewer: str,
                 consumes: FrozenSet[str] = frozenset(),
                 operation: str = ""):
        self.state = state
        self.viewer = viewer
        self.consumes = consumes
        # 6.1.86 षत्वतुकोरसिद्धः, asked of asiddha.py and not decided here.
        self.ekadesa_hidden = bool(operation) and \
            ekadesa_visible(operation).asiddha
        sights: List[Sight] = []
        for real, seg in enumerate(state.segs):
            self._expand(seg, real, False, sights)
        #: Every sound as seen, including empties (a loss the viewer can see).
        self.sights: Tuple[Sight, ...] = tuple(sights)
        #: Those that are actually there to be heard.
        self.live: Tuple[Sight, ...] = tuple(
            s for s in sights if not s.seg.elided)
        self._position: Dict[int, int] = {
            sight.uid: i for i, sight in enumerate(self.live)}

    # -- provenance ---------------------------------------------------------

    def _hidden(self, seg: Seg) -> bool:
        if not seg.made_by:
            return False
        if self.ekadesa_hidden and EKADESA_MARK in seg.marks:
            return True
        if self.consumes & seg.marks:
            return False
        return _asiddha(seg.made_by, self.viewer)

    def _expand(self, seg: Seg, real: int, through: bool,
                out: List[Sight]) -> None:
        if self._hidden(seg):
            for older in seg.prior:
                self._expand(older, real, True, out)
            return
        out.append(Sight(seg, real, through, self.state.segs[real].uid))

    # -- navigation ---------------------------------------------------------

    def index(self, sight: Sight) -> int:
        return self._position[sight.uid]

    def prev(self, sight: Sight) -> Optional[Sight]:
        i = self.index(sight)
        return self.live[i - 1] if i > 0 else None

    def next(self, sight: Sight) -> Optional[Sight]:
        i = self.index(sight)
        return self.live[i + 1] if i + 1 < len(self.live) else None

    def word(self, sight: Sight) -> Word:
        return self.state.words[sight.w]

    def flags(self, sight: Sight) -> FrozenSet[str]:
        return self.state.words[sight.w].flags

    # -- words and their edges ----------------------------------------------

    def _ended_words(self, sight: Sight, antadivat: bool = False
                     ) -> List[int]:
        """The words this sound is the last live sound of."""
        later = self.live[self.index(sight) + 1:]
        words = _words(sight.seg)
        if not antadivat:
            words = frozenset({sight.w})
        return [x for x in words
                if not any(x in _words(t.seg) for t in later)]

    def _begun_words(self, sight: Sight, antadivat: bool = False
                     ) -> List[int]:
        """The words this sound is the first live sound of."""
        earlier = self.live[:self.index(sight)]
        words = _words(sight.seg)
        if not antadivat:
            words = frozenset({sight.w})
        return [x for x in words
                if not any(x in _words(t.seg) for t in earlier)]

    def pairs(self, *, interior: bool = False) -> List[Junction]:
        """
        Two adjacent sounds, within a word or across a boundary.

        **Only where something is happening.** The words the engine is given
        are finished words, and their insides are as the grammar left them: the
        च्छ् of *गच्छति* is a च् that 8.4.40 made out of a त् long before this
        junction, and 8.2.30 चोः कुः must not read it as a च् before a झल् and
        turn it to क्. So a pair inside one word is offered only if one of its
        sounds was made in THIS derivation (which is how the उ that 6.1.113
        makes out of a रु gets joined to the अ before it), or if `interior` is
        asked for outright.
        """
        out: List[Junction] = []
        for left, right in zip(self.live, self.live[1:]):
            if _words(left.seg) & _words(right.seg):
                if interior or left.seg.made_by or right.seg.made_by:
                    out.append(Junction(left, right, WITHIN))
            else:
                out.append(Junction(left, right, self.boundary_after(left)))
        return out

    def junctions(self) -> List[Junction]:
        """Only the pairs that lie between two words."""
        return [j for j in self.pairs() if j.between_words]

    def vowel_pairs(self) -> List[Junction]:
        """
        Every two adjacent vowels, and no prakṛtibhāva rule has yet claimed
        them — where every rule of अच्-sandhi looks.

        Within a word as well as across a boundary: the two vowels of
        *शिव* + *उ* (the उ that 6.1.113 has just made out of a रु) stand in one
        pada, and 6.1.87 joins them all the same — शिवोऽर्च्यः. A vowel a
        prakṛtibhāva rule has marked `PRAKRTYA` is left alone by the rest, so
        it is not offered.
        """
        return [j for j in self.pairs()
                if j.left.is_vowel and j.right.is_vowel
                and PRAKRTYA not in j.left.marks
                and PRAKRTYA not in j.right.marks]

    def vowel_junctions(self) -> List[Junction]:
        """`vowel_pairs`, kept to those that lie between two words."""
        return [j for j in self.vowel_pairs() if j.between_words]

    def boundary_after(self, sight: Sight) -> str:
        """What follows the (outermost) word this sound ends."""
        ended = self._ended_words(sight)
        return self.state.bounds[max(ended)] if ended \
            else self.state.bounds[sight.w]

    def ends_word(self, sight: Sight, *, antadivat: bool = False) -> bool:
        """
        The last sound of a word.

        By default a substitute that 6.1.84 put in the place of two sounds
        belongs, for this purpose, to the LATER word alone. 6.1.85 अन्तादिवत्
        would also make it the end of the earlier one — but **not for a rule
        that rests on the sounds themselves** (वर्णाश्रयविधौ नेष्यते,
        `asiddha.antadivat`), and every rule of sandhi is one: without the
        restriction the र् of अर् in *महर्षि* is a pada-final र् and 8.3.15
        turns it to a visarga. A rule that is about the *pada* — and the
        tradition says so of it — asks with `antadivat=True`.
        """
        return bool(self._ended_words(sight, antadivat))

    def begins_word(self, sight: Sight, *, antadivat: bool = False) -> bool:
        return bool(self._begun_words(sight, antadivat))

    def pada_final(self, sight: Sight, *, antadivat: bool = False) -> bool:
        """Ends a word that is a पद — 1.4.14, not a bare stem or affix."""
        ended = self._ended_words(sight, antadivat)
        return bool(ended) and \
            self.state.bounds[max(ended)] in PADA_LIKE

    def at_pause(self, sight: Sight) -> bool:
        """The last sound of the utterance, before an अवसान (1.4.110)."""
        return (self.next(sight) is None
                and self.boundary_after(sight) == AVASANA)

    def unit_of(self, sight: Sight, across: Sequence[str] = (ANGA,)
                ) -> List[Sight]:
        """
        The sounds of the run of words joined to `sight`'s word by boundaries of
        the kinds in `across`, in order.

        Sandhi between padas leaves the inside of each pada alone, but the rules
        that reach an INTERIOR sound from further off — 8.4.1 रषाभ्यां नो णः
        turning the न् of *एन* to ण् after the र् of *राम*, 8.3.59 turning the
        स् of *सु* to ष् after the इ of *अग्नि* — act inside one pada, and a
        pada built of a stem and an affix is not a finished word: the affix has
        not yet met the stem. `across` says which joins count as inside: ANGA by
        default; 8.4.14 crosses UPASARGA; 8.4.3 crosses SAMASA.

        A word with no such join is a unit of its own, and a rule that asks for
        one gets the word back — a finished word's interior is still not offered.
        """
        wanted = {sight.w}
        low = high = sight.w
        while low > 0 and self.state.bounds[low - 1] in across:
            low -= 1
            wanted.add(low)
        while high < len(self.state.words) - 1 and \
                self.state.bounds[high] in across:
            high += 1
            wanted.add(high)
        return [t for t in self.live if _words(t.seg) & wanted]

    def joined_pada(self, sight: Sight, across: Sequence[str] = (ANGA,)
                    ) -> bool:
        """True where `sight`'s word is joined to another by an `across` kind
        of boundary — the pada is not a finished word, so a rule may look
        inside it."""
        w = sight.w
        before = w > 0 and self.state.bounds[w - 1] in across
        after = w < len(self.state.words) - 1 and \
            self.state.bounds[w] in across
        return before or after

    def word_sights(self, w: int) -> List[Sight]:
        return [s for s in self.live if s.w == w]

    def final_cluster(self, sight: Sight) -> List[Sight]:
        """The run of consonants ending at `sight` within its own word."""
        run = [sight]
        cur = sight
        while True:
            prv = self.prev(cur)
            if prv is None or prv.w != sight.w or not prv.is_consonant:
                break
            run.insert(0, prv)
            cur = prv
        return run if all(s.is_consonant for s in run) else [sight]

    def refused(self, sutra: str, site: Tuple[int, ...],
                varttika: str = "") -> bool:
        """
        Whether the derivation has already declined (an option) or been refused
        (by a प्रतिषेध) the rule `sutra` — or its vārttika — at `site`.

        Asked of the engine's own record rather than read out of the sounds,
        because a refusal leaves no trace in them: a vārttika that is offered
        only once the rule it qualifies has been settled at the same place has
        no other way to know.
        """
        key = f"{sutra}:{varttika}" if varttika else sutra
        return (key, tuple(sorted(site))) in self.state.declined

    def by_uid(self, uid: int) -> Optional[Sight]:
        pos = self._position.get(uid)
        return self.live[pos] if pos is not None else None


__all__ = [
    "AC", "AGAMA", "ANGA", "ANUNASIKA", "AVAGRAHA", "AVASANA", "AYOGAVAHA",
    "BOUNDARIES", "EKADESA_MARK", "HAL", "HIATUS", "Junction", "OPEN", "PADA", "PADA_LIKE", "PLUTA", "PRAKRTYA", "RU",
    "SAMASA", "Seg", "Sight", "State", "UPASARGA", "View", "WITHIN", "Word",
    "base_of",
]
