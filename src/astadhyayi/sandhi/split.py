# -*- coding: utf-8 -*-
"""
सन्धिविच्छेद — from the joined form back to the words, by asking the grammar.

No sūtra runs backwards: nothing in the Aṣṭādhyāyī takes a sandhi off a form
(the project's own note on `tinanta` says the same of affixes). So this does what
the project already does for verbs — it works the only way the grammar allows,
**by synthesis**. It proposes a split, derives the joined form from it with the
forward engine, and keeps the split only if that derivation gives back exactly
what was written. Every split it returns therefore comes with the sūtra-by-sūtra
derivation that proves it.

**Where the proposals come from is not a table either.** Building the index
means *running the forward engine* over every final sound meeting every initial
sound, in a few contexts, and recording the region of the surface that comes
out. To split, that index is read backwards: the region `ār` in *punāramate*
came from a final `r` of a word after `a`, meeting an initial `r`. The index is
the grammar's own output, so it cannot disagree with the forward rules, and it
is rebuilt from them whenever they change.

**What this does NOT do — and says so.** Any string can be cut anywhere, and a
cut where nothing changed (*rāma* + *kṛṣṇa*) is always a valid split. Only a
**lexicon** can say which words are words, so without one `split` returns every
split the grammar allows, marked unvalidated, and says so; with one
(`lexicon=`), it keeps the splits whose parts it knows and ranks them. The
forward derivation guarantees a split is *possible*; only the lexicon can say
it is *right*. A word's underlying final (the स् or र् behind a visarga, the
द् behind a त्) is what the derivation starts from, so each word is also
given in its pausal form, which is what a dictionary lists.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import os
from collections import defaultdict
from dataclasses import dataclass
from typing import (
    Callable, Dict, FrozenSet, Iterable, List, Optional, Sequence, Set, Tuple)

from src.astadhyayi.sandhi import trace as _trace
from src.astadhyayi.sandhi.engine import Outcome, derive
from src.astadhyayi.sandhi.harness import joined
from src.astadhyayi.sandhi.parse import (
    SandhiInputError, parse, to_iast, tokenize)
from src.astadhyayi.sandhi.rulebook import all_rules
from src.astadhyayi.sandhi.segs import AC, HAL, PADA
from src.astadhyayi.varna import ANUNASIKA_MARK, ANUSVARA

#: The longest stretch of the joined form one junction is allowed to change.
#: Real junctions change one to three sounds (a doubling and a cluster is the
#: longest); more is a sign that a pattern is not a junction.
MAX_REGION = 5
#: The vowels a final consonant is met after. Some rules read the vowel before
#: a final (8.3.32 wants a short one), so one context is not enough.
LEFT_CONTEXTS: Tuple[str, ...] = ("a", "ā", "i", "ī", "u", "ū")


@dataclass(frozen=True)
class Entry:
    """A pair of sounds that meets in a way that gives a region of surface."""

    final: str          # the last sound of the first word, as the derivation starts
    initial: str        # the first sound of the second
    context: str        # the vowel before a consonant final ("" for a vowel final)


class Lexicon:
    """The words a split may use. Pausal forms, IAST, as a dictionary lists them."""

    def __init__(self, words: Iterable[str] = ()):
        self._words: Set[str] = {joined(w) for w in words}

    def add(self, *words: str) -> None:
        self._words.update(joined(w) for w in words)

    def __contains__(self, word: str) -> bool:
        return joined(word) in self._words

    def __len__(self) -> int:
        return len(self._words)

    @classmethod
    def from_file(cls, path: str) -> "Lexicon":
        with open(path, encoding="utf-8") as handle:
            return cls(to_iast(line.strip()) for line in handle
                       if line.strip() and not line.startswith("#"))


def pausal_forms(word: str, rules=None) -> Tuple[str, ...]:
    """
    Every form a word can take at a pause — the forms a dictionary may list:
    रामस् ⟶ रामः; वाच् ⟶ वाक् or वाग् (8.4.56 वाऽवसाने leaves both standing).
    Asked of the forward engine, not of a table; the first is the one the
    grammar's own order gives.
    """
    try:
        state = parse([word], pause=True)
        outcomes = derive(state, all_rules() if rules is None else rules)
    except SandhiInputError:
        return (word,)
    return tuple(dict.fromkeys(o.surface for o in outcomes)) or (word,)


def pausal(word: str, rules=None) -> str:
    """The first pausal form of a word (see `pausal_forms`)."""
    return pausal_forms(word, rules)[0]


class Index:
    """
    What the grammar makes of every final meeting every initial, read backwards.

    `regions[r]` lists the (final, initial, context) that produce the stretch of
    surface `r`. Built by running the forward engine — expensive once, then
    reused; see `build`.
    """

    def __init__(self) -> None:
        self.regions: Dict[str, List[Entry]] = defaultdict(list)
        self.size = 0

    @classmethod
    def build(cls, *, finals: Optional[Sequence[str]] = None,
              initials: Optional[Sequence[str]] = None,
              contexts: Sequence[str] = LEFT_CONTEXTS,
              boundary: str = PADA, rules=None) -> "Index":
        """
        Run every (final, initial) through the engine and record the regions.

        The words are `k` + [vowel] + final and initial + `ta`/`a`: the `k` and
        the tail stand still and mark where the region begins and ends. A vowel
        final needs no context vowel; a consonant final is tried after each
        context vowel, since a rule may read it.
        """
        rules = all_rules() if rules is None else rules
        vowels = sorted(AC)
        consonants = sorted(HAL) + [ANUSVARA]
        finals = list(finals) if finals is not None else vowels + consonants
        initials = list(initials) if initials is not None \
            else vowels + sorted(HAL)
        index = cls()
        for final in finals:
            ctxs = ("",) if final in AC else tuple(contexts)
            for ctx in ctxs:
                left = "k" + ctx + final
                for initial in initials:
                    tail = "ta" if initial in AC else "a"
                    right = initial + tail
                    try:
                        start = parse([left, right], boundary=boundary,
                                      pause=True)
                        outcomes = derive(start, rules)
                    except SandhiInputError:
                        continue
                    for outcome in outcomes:
                        surface = outcome.surface
                        if not surface.startswith("k") or \
                                not surface.endswith(tail):
                            continue
                        region = surface[1:len(surface) - len(tail)]
                        if len(region) > MAX_REGION:
                            continue
                        entry = Entry(final, initial, ctx)
                        if entry not in index.regions[region]:
                            index.regions[region].append(entry)
                            index.size += 1
        return index

    # -- keeping it: it is expensive to build and cheap to read --------------

    def to_json(self, fingerprint: str) -> Dict[str, object]:
        return {"fingerprint": fingerprint,
                "regions": {r: [[e.final, e.initial, e.context] for e in es]
                            for r, es in self.regions.items()}}

    @classmethod
    def from_json(cls, data: Dict[str, object]) -> "Index":
        index = cls()
        for region, entries in data["regions"].items():        # type: ignore
            for final, initial, context in entries:
                index.regions[region].append(Entry(final, initial, context))
                index.size += 1
        return index


#: Every source file the index depends on. Change any and the saved index is
#: stale, and is rebuilt: an index that outlived a rule would disagree with the
#: forward engine, which is the one thing it must never do.
_DEPENDS_ON = ("anga.py", "adesa.py", "varna.py", "sivasutra.py", "asiddha.py",
               "vipratisedha.py", "pragrhya.py", "reading.py", "operations.py")


def fingerprint() -> str:
    here = os.path.dirname(os.path.abspath(__file__))
    package = os.path.dirname(here)
    digest = hashlib.sha256()
    paths: List[str] = []
    for base, _, files in os.walk(here):
        paths.extend(os.path.join(base, f) for f in files if f.endswith(".py"))
    paths.extend(os.path.join(package, name) for name in _DEPENDS_ON)
    for path in sorted(paths):
        with open(path, "rb") as handle:
            digest.update(os.path.relpath(path, package).encode())
            digest.update(handle.read())
    return digest.hexdigest()


#: Where the built index is kept between runs (git-ignored; see .gitignore).
CACHE_PATH = os.environ.get("SANDHI_INDEX_CACHE") or os.path.join(
    "data", "sandhi", ".cache", "junction_index.json")


@dataclass(frozen=True)
class Split:
    """One way the joined form could have been made, proved by a derivation."""

    #: The words as a dictionary lists them (pausal): what a reader expects.
    words: Tuple[str, ...]
    #: The words as the derivation began: with the स्, र्, द् behind a visarga
    #: or a hard final, which is what the rules acted on.
    underlying: Tuple[str, ...]
    outcome: Outcome
    #: For each word, whether the lexicon knows it; empty when none was given.
    known: Tuple[bool, ...] = ()
    #: Whether any sandhi happened at all (a split at a place where nothing
    #: changed is always possible and says little).
    changed: bool = True
    #: The OTHER ways the same words come to the same joined form: वाक् may be
    #: from वाच्, वाक्, वाग् or वाह् — one split, several underlying finals, each
    #: with its own derivation. (underlying words, outcome) pairs.
    alternatives: Tuple[Tuple[Tuple[str, ...], Outcome], ...] = ()

    @property
    def validated(self) -> bool:
        return bool(self.known) and all(self.known)

    def trace(self) -> str:
        head = " + ".join(_trace.both(w) for w in self.words)
        text = f"{head}\n{_trace.render(self.outcome)}"
        for underlying, outcome in self.alternatives:
            text += (f"\n\n  or, from "
                     f"{' + '.join(_trace.both(w) for w in underlying)}:\n"
                     f"{_trace.render(outcome)}")
        return text

    def to_dict(self):
        return {"words": list(self.words),
                "words_deva": [_trace.deva(w) for w in self.words],
                "underlying": list(self.underlying),
                "known": list(self.known), "validated": self.validated,
                "changed": self.changed,
                "derivation": _trace.outcome_dict(self.outcome),
                "alternatives": [
                    {"underlying": list(u),
                     "derivation": _trace.outcome_dict(o)}
                    for u, o in self.alternatives]}


_DEFAULT_INDEX: Optional[Index] = None


def default_index(cache: Optional[str] = CACHE_PATH) -> Index:
    """
    The index for the whole rulebook: read from `cache` if it was built from
    exactly these rules, otherwise built (about a minute) and saved.
    """
    global _DEFAULT_INDEX
    if _DEFAULT_INDEX is not None:
        return _DEFAULT_INDEX
    stamp = fingerprint()
    if cache and os.path.exists(cache):
        try:
            with open(cache, encoding="utf-8") as handle:
                saved = json.load(handle)
            if saved.get("fingerprint") == stamp:
                _DEFAULT_INDEX = Index.from_json(saved)
                return _DEFAULT_INDEX
        except (OSError, ValueError, KeyError):
            pass
    _DEFAULT_INDEX = Index.build()
    if cache:
        try:
            os.makedirs(os.path.dirname(cache), exist_ok=True)
            with open(cache, "w", encoding="utf-8") as handle:
                json.dump(_DEFAULT_INDEX.to_json(stamp), handle,
                          ensure_ascii=False)
        except OSError:
            pass
    return _DEFAULT_INDEX


#: A word list, one pausal IAST word per line, if the project has one.
LEXICON_PATH = os.path.join("data", "sandhi", "lexicon.txt")


def default_lexicon() -> Optional[Lexicon]:
    """The project's word list, or None if there is not one — in which case a
    split cannot be validated and says so."""
    if os.path.exists(LEXICON_PATH):
        return Lexicon.from_file(LEXICON_PATH)
    return None


#: How many doubled sounds a text may have before only two readings — all
#: undone, none undone — are tried instead of every combination.
MAX_DOUBLED = 6


def _sounds(text: str) -> List[str]:
    """A joined form as sounds (the avagraha a sound of its own)."""
    out: List[str] = []
    for i, piece in enumerate(text.split("'")):
        if i:
            out.append("'")
        out.extend(sound + (ANUNASIKA_MARK if nasal else "")
                   for sound, nasal in tokenize(piece))
    return out


def _doubled_at(sounds: Sequence[str]) -> List[int]:
    """
    Positions i where sounds[i-1], sounds[i] look like a doubling — the sound
    twice (tt), or the unaspirated sound before its aspirate (ddh, cch).

    8.4.46–47 double a consonant, and the doubling stands next to the
    junction that caused it (iti + ādi → itt·yādi), where the index — built
    on single consonants — has nothing to match. A doubling may be spurious
    (pattra is not a doubled patra) and that costs nothing: verification
    checks the ORIGINAL text.
    """
    found = []
    for i in range(1, len(sounds)):
        a, b = sounds[i - 1], sounds[i]
        if a in HAL and (a == b or (b.endswith("h") and len(b) == 2
                                    and b[0] == a and a != "h")):
            found.append(i - 1)
    return found


def _variants(text: str) -> List[str]:
    """`text`, and the texts got by undoing each possible doubling."""
    sounds = _sounds(text)
    positions = _doubled_at(sounds)
    if not positions:
        return [text]
    if len(positions) <= MAX_DOUBLED:
        subsets = [c for r in range(len(positions) + 1)
                   for c in itertools.combinations(positions, r)]
    else:
        subsets = [(), tuple(positions)]
    seen: List[str] = []
    for drop in subsets:
        variant = "".join(x for i, x in enumerate(sounds) if i not in drop)
        if variant not in seen:
            seen.append(variant)
    return seen


def _candidates(text: str, index: Index) -> Iterable[Tuple[str, str, Entry]]:
    """(left, right, entry) for every place the index says a junction could be."""
    for p in range(1, len(text) + 1):
        for length in range(0, MAX_REGION + 1):
            q = p + length
            if q > len(text):
                break
            for entry in index.regions.get(text[p:q], ()):
                left = text[:p] + (entry.context if entry.context else "") \
                    + entry.final
                right = entry.initial + text[q:]
                if right:
                    yield left, right, entry


def split(
    surface: str,
    *,
    lexicon: Optional[Lexicon] = None,
    index: Optional[Index] = None,
    boundary: str = PADA,
    veda: bool = False,
    require_change: bool = False,
    limit: int = 200,
) -> List[Split]:
    """
    The ways `surface` can be split into two words, each proved by derivation.

    With a `lexicon`, only splits whose two words it knows are returned (and
    they come first, ranked by how much sandhi the split explains). Without
    one, every split the grammar allows is returned, `validated` False.
    `require_change` drops the splits where nothing changed at the junction.
    """
    text = joined(to_iast(surface))
    # An unreadable letter is refused, as `sandhi` refuses it — not answered
    # with "no splits", which would read as though the grammar had looked. The
    # avagraha is the one non-sound a joined form may carry.
    body = text.replace("'", "")
    typed = joined(surface).replace("’", "").replace("'", "")
    tokenize(body, given=typed if len(typed) == len(body) else "")
    index = default_index() if index is None else index
    rules = all_rules()
    found: List[Split] = []
    seen: Set[Tuple[str, str]] = set()
    proposals = ((left, right, entry) for variant in _variants(text)
                 for left, right, entry in _candidates(variant, index))
    for left, right, entry in proposals:
        if (left, right) in seen:
            continue
        seen.add((left, right))
        try:
            start = parse([left, right], boundary=boundary, veda=veda,
                          pause=True)
        except SandhiInputError:
            continue
        for outcome in derive(start, rules):
            if joined(outcome.surface) != text:
                continue
            forms = (pausal_forms(left, rules), pausal_forms(right, rules))
            if lexicon is not None:
                # a word is known if ANY of its pausal forms is listed
                chosen = tuple(next((f for f in fs if f in lexicon), fs[0])
                               for fs in forms)
                known = tuple(any(f in lexicon for f in fs) for fs in forms)
                if not all(known):
                    break
            else:
                chosen, known = (forms[0][0], forms[1][0]), ()
            words = chosen
            changed = any(not s.declined for s in outcome.steps)
            if require_change and not changed:
                break
            found.append(Split(words, (left, right), outcome, known, changed))
            break
        if len(found) >= limit:
            break
    return _grouped(found)


def _grouped(found: List[Split]) -> List[Split]:
    """One Split per pair of words; the other underlying finals that give the
    same joined form become its `alternatives`. The reading that needs nothing
    restored (the word as listed) is the primary, then the shortest."""
    by_words: Dict[Tuple[str, ...], List[Split]] = defaultdict(list)
    for item in found:
        by_words[item.words].append(item)
    grouped: List[Split] = []
    for words, group in by_words.items():
        group.sort(key=lambda g: (g.underlying != words,
                                  len(g.outcome.steps), g.underlying))
        first = group[0]
        grouped.append(Split(
            first.words, first.underlying, first.outcome, first.known,
            first.changed,
            tuple((g.underlying, g.outcome) for g in group[1:])))
    grouped.sort(key=lambda s: (not s.validated, not s.changed,
                                -len(s.outcome.steps), s.words))
    return grouped


__all__ = ["CACHE_PATH", "Entry", "Index", "LEXICON_PATH", "Lexicon", "Split",
           "default_index", "default_lexicon", "fingerprint", "pausal",
           "pausal_forms", "split"]
