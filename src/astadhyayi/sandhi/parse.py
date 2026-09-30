# -*- coding: utf-8 -*-
"""
Reading what the caller typed into a `State`.

**Either script.** Devanāgarī is converted to IAST at this one boundary, as the
project's standing decision has it (NORTH_STAR §5), and every form in a trace is
printed in both. The shared converter turns a candrabindu into an ``m`` — right
for ``सँ`` as a nasal syllable, wrong for a nasalised vowel, which is what 8.3.2
makes — so the candrabindu is split off first and put back on the vowel.

**The syntax is small on purpose.** Words are separated by a space or ``+``
(two padas in saṃhitā). Anything else says what *kind* of junction it is,
because the rules ask:

    ``deva-indra``    ``-``  a compound (समास): the first member is a pada
    ``pra|ejate``     ``|``  a preverb and its dhātu
    ``ne~a``          ``~``  two pieces of one pada (aṅga | affix)

and a word may carry what its letters cannot say, in braces: ``harī{dvivacana}
etau``. That is deliberate. Whether an ī is a dual ending decides 1.1.11 and no
reading of the letters settles it; NORTH_STAR §5 — *when a rule needs something
we cannot compute, take it as a parameter and say so*.

**A visarga does not say what it came from.** ``रामः`` is *rāmas* (8.2.66) and
``पुनः`` is *punar* (8.3.15), and they behave differently before a vowel. Write
the underlying final where it matters. A visarga given is read as coming from
``s`` — the commoner — and the trace says that was assumed.
"""

from __future__ import annotations

import re
import unicodedata
from typing import Dict, Iterable, List, Optional, Sequence, Tuple, Union

from src.chandas.core import CONSONANTS, NASAL_MARKS, VOWELS
from src.normalizer import devanagari_to_iast, is_devanagari

from src.astadhyayi.sandhi.segs import (
    ANGA, ANUNASIKA, AVASANA, BOUNDARIES, OPEN, PADA, SAMASA, UPASARGA,
    Seg, State, Word)
from src.astadhyayi.varna import ANUNASIKA_MARK, ANUSVARA, VISARGA

#: The characters that separate words, and the kind of junction each makes.
_SEPARATORS: Dict[str, Optional[str]] = {
    " ": None,          # the caller's default
    "+": None,
    "-": SAMASA,
    "|": UPASARGA,
    "~": ANGA,
}
_SPLIT = re.compile(r"[ +\-|~]+")
_FLAGS = re.compile(r"\{([^{}]*)\}")
_AVAGRAHA = ("'", "’", "ऽ")


class SandhiInputError(ValueError):
    """The input cannot be read as Sanskrit sounds; the message says where."""


def to_iast(text: str) -> str:
    """Devanāgarī or IAST → IAST, NFC, lower case, candrabindu kept on its
    vowel."""
    text = unicodedata.normalize("NFC", text)
    if is_devanagari(text):
        pieces = text.split("ँ")            # ँ
        text = ANUNASIKA_MARK.join(devanagari_to_iast(p) for p in pieces)
    return unicodedata.normalize("NFC", text).lower()


#: Longest match first: "kh" before "k", "ai" before "a".
_TOKENS: Tuple[str, ...] = tuple(sorted(
    set(VOWELS) | set(CONSONANTS) | set(NASAL_MARKS) | {ANUSVARA, VISARGA},
    key=lambda t: (-len(t), t)))


def tokenize(word: str, given: str = "") -> List[Tuple[str, bool]]:
    """
    A word as a list of (sound, nasal).

    ``m̐`` (candrabindu written after m) is read as anusvāra, which is what a
    candrabindu after a nasal consonant stands for; a candrabindu after any
    other sound nasalises that sound.
    """
    out: List[Tuple[str, bool]] = []
    i = 0
    while i < len(word):
        ch = word[i]
        if ch == ANUNASIKA_MARK:
            if not out:
                raise SandhiInputError(
                    f"a candrabindu with nothing before it, in {word!r}")
            sound, _ = out[-1]
            out[-1] = (sound, True)
            i += 1
            continue
        for token in _TOKENS:
            if word.startswith(token, i):
                if token == "m̐":
                    out.append((ANUSVARA, False))
                elif token == "ṁ":
                    out.append((ANUSVARA, False))
                else:
                    out.append((token, False))
                i += len(token)
                break
        else:
            # Say what the caller typed, not what lower-casing made of it.
            shown = given[i] if len(given) == len(word) else ch
            raise SandhiInputError(
                f"{shown!r} (U+{ord(shown):04X}) in {(given or word)!r} is "
                f"not a Sanskrit sound this engine reads")
    return out


def _split_flags(piece: str) -> Tuple[str, Tuple[str, ...]]:
    match = _FLAGS.search(piece)
    if not match:
        return piece, ()
    flags = tuple(f.strip() for f in match.group(1).split(",") if f.strip())
    return _FLAGS.sub("", piece), flags


def _words_from(spec: Union[str, Sequence[Union[str, Word]]],
                boundary: str) -> Tuple[List[Word], List[str]]:
    """The words, and the boundary that follows each but the last."""
    if isinstance(spec, str):
        pieces: List[str] = []
        kinds: List[str] = []
        last = 0
        for match in _SPLIT.finditer(spec):
            pieces.append(spec[last:match.start()])
            marks = [c for c in match.group(0) if c in "-|~"]
            kinds.append(_SEPARATORS[marks[0]] if marks else boundary)
            last = match.end()
        pieces.append(spec[last:])
        pieces = [p for p in pieces]
        if not pieces or all(not p.strip() for p in pieces):
            raise SandhiInputError("nothing to join: give at least one word")
        # a leading or trailing separator leaves an empty piece; drop it
        cleaned: List[str] = []
        joins: List[str] = []
        for index, piece in enumerate(pieces):
            if piece.strip():
                if cleaned:
                    joins.append(kinds[index - 1])
                cleaned.append(piece)
        words = []
        for piece in cleaned:
            text, flags = _split_flags(piece)
            words.append(Word(text=to_iast(text), given=text,
                              flags=frozenset(flags)))
        return words, joins

    words = []
    for item in spec:
        if isinstance(item, Word):
            words.append(Word(text=to_iast(item.text), given=item.given
                              or item.text, flags=item.flags,
                              inferred=item.inferred))
        else:
            text, flags = _split_flags(item)
            words.append(Word(text=to_iast(text), given=text,
                              flags=frozenset(flags)))
    if not words:
        raise SandhiInputError("nothing to join: give at least one word")
    return words, [boundary] * (len(words) - 1)


def _with_inferences(words: List[Word]) -> List[Word]:
    """Add the flags `infer.infer_flags` can prove, marked as inferred."""
    from src.astadhyayi.sandhi.infer import infer_flags

    texts = [w.text for w in words]
    out: List[Word] = []
    for position, word in enumerate(words):
        found = infer_flags(word.text, position=position, words=texts,
                            given=word.flags)
        new = [(flag, why) for flag, why in found if flag not in word.flags]
        out.append(Word(
            text=word.text, given=word.given,
            flags=word.flags | frozenset(flag for flag, _ in new),
            inferred=word.inferred + tuple(new)) if new else word)
    return out


def _plain(text: str) -> str:
    """A word without its diacritics, lower case — so 'anga' and 'aṅga'
    are the same boundary to an API caller who types ASCII."""
    stripped = unicodedata.normalize("NFD", text)
    return "".join(c for c in stripped
                   if not unicodedata.combining(c)).lower()


def boundary_kind(name: str) -> str:
    """The boundary kind named, in either spelling; SandhiInputError if none."""
    for kind in BOUNDARIES:
        if _plain(kind) == _plain(name):
            return kind
    raise SandhiInputError(
        f"boundary must be one of {', '.join(BOUNDARIES)}, not {name!r}")


def _read_visarga(words: List[Word]) -> List[Word]:
    """
    Read a word-final visarga as the स् or र् it came from.

    A visarga is not where the grammar starts. 8.3.15 makes it out of a रु
    (or a र्), and 8.2.66 makes that रु out of a pada-final स् — and what
    happens to the word before a vowel depends on which it was: *रामस्* + *अत्र*
    is रामोऽत्र (6.1.113), *पुनर्* + *अत्र* is पुनरत्र. Nothing in the letters
    says which, so the default is the commoner, स्, and the word is given
    the reading `final:s`; a word from र् says so with `{final:r}`, or
    `infer.py` proves it from a closed class (the स्वरादि gaṇa). Either way the
    reading is recorded on the Word as an assumption for the trace to print.
    """
    out: List[Word] = []
    for word in words:
        if len(word.text) < 2 or not word.text.endswith(VISARGA):
            out.append(word)
            continue
        final = "r" if word.has("final:r") else "s"
        flag = f"final:{final}"
        if word.has(flag):
            reason = "given by the caller"
            inferred = word.inferred
        else:
            reason = ("a final visarga is read as coming from "
                      + ("र् — the closed class of र्-final indeclinables"
                         if final == "r" else
                         "स् (8.2.66 ससजुषो रुः, then 8.3.15); write "
                         "the word with its underlying final, or add the "
                         "flag final:r, where it comes from र्"))
            inferred = word.inferred + ((flag, reason),)
        out.append(Word(text=word.text[:-1] + final, given=word.given,
                        flags=word.flags | {flag}, inferred=inferred))
    return out


def parse(
    spec: Union[str, Sequence[Union[str, Word]]],
    *,
    boundary: str = PADA,
    veda: bool = False,
    pause: bool = True,
    infer: bool = True,
) -> State:
    """
    The input as a `State`.

    `pause` says whether the last word is followed by an अवसान (1.4.110 —
    the utterance ends there). It matters to 8.3.15 and 8.4.56, which name it;
    say ``pause=False`` for a fragment that goes on. `infer` lets the parser
    fill in flags it can prove (see `infer.py`); each is recorded as inferred.
    """
    boundary = boundary_kind(boundary)
    words, joins = _words_from(spec, boundary)
    if infer:
        words = _with_inferences(words)
    words = _read_visarga(words)
    segs: List[Seg] = []
    uid = 0
    for w, word in enumerate(words):
        if any(a in word.text for a in _AVAGRAHA):
            raise SandhiInputError(
                f"{word.given!r} carries an avagraha, which marks a "
                f"junction already joined; give the words as they stand "
                f"before sandhi")
        for sound, nasal in tokenize(word.text, word.given):
            marks = frozenset({ANUNASIKA}) if nasal else frozenset()
            segs.append(Seg(uid=uid, s=sound, w=w, marks=marks))
            uid += 1
        if not any(seg.w == w for seg in segs):
            raise SandhiInputError(f"{word.given!r} has no sounds")
    bounds = tuple(joins) + (AVASANA if pause else OPEN,)
    return State(segs=tuple(segs), words=tuple(words), bounds=bounds,
                 veda=veda, next_uid=uid)


__all__ = ["SandhiInputError", "boundary_kind", "parse", "to_iast",
           "tokenize"]
