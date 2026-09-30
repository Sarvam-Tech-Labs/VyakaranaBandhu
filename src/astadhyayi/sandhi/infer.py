# -*- coding: utf-8 -*-
"""
What can be filled in about a word without being told.

Some rules ask what the letters cannot say: is this a particle (1.1.14), is it
a preverb, is this ī a dual. NORTH_STAR §5 settles the default — *take it as a
parameter and say so* — and the caller's flags always win. But a caller who
writes ``aho īśāḥ`` has plainly not thought to add ``{nipata}``, and a closed
class can be looked up: the particles of the cādi and prādi gaṇas are in the
gaṇapāṭha on disk, and 1.4.56–1.4.98 say which of them are upasargas.

`infer_flags` returns what it can prove **and why**, as (flag, reason) pairs.
`parse` records each on the `Word` so the trace can show the assumption
("taken as a particle: अहो is in the cādi gaṇa, 1.4.57") — an inference is never
mistaken for something the caller said.

**What a closed class proves, and what it does not.**

  * A word that is a member of the **cādi** gaṇa (1.4.57 चादयोऽसत्त्वे) or the
    **prādi** gaṇa (1.4.58 प्रादयः) is a nipāta. The gaṇas are read from the
    gaṇapāṭha (`corpus.ganas_for`), never typed here. The cādi gaṇa is an
    *ākṛtigaṇa* — a list that usage may extend — so being in it proves
    particlehood and **being absent from it proves nothing**: no flag is ever
    withheld on the ground that a word is not listed. And 1.4.57 says *asattve*:
    a word that names a substance (dravya) is no nipāta — ``paśuḥ`` the animal,
    against ``paśu`` in the sense of *samyak* (Kāśikā). The letters cannot say
    which is meant, so the inference is made and its reason says so; the caller
    who means the substance adds the flag ``sattva`` and nothing is inferred.
  * A word before a dhātu across a ``|`` boundary, that is in the prādi gaṇa,
    is an **upasarga** (1.4.59 उपसर्गाः क्रियायोगे — *kriyāyoge*, in connection
    with a verb; the boundary is the caller saying so). If it is ā, it is the
    āṅ of that list (the ṅ is an इत्, 1.3.3 हलन्त्यम्), which is why 1.1.14's
    *anāṅ* leaves it out — a fact of the boundary, not of the letters.
  * A word ending in a **visarga** is read by the parser as coming from स्
    unless it is said to come from र् (8.2.66, 8.3.15). Where exactly one of the
    two readings is a member of the svarādi gaṇa (1.1.37 स्वरादिनिपातमव्ययम् —
    the closed class of indeclinables that includes svar, antar, prātar, punar,
    and also uccais, nīcais, śanais), the word *is* that indeclinable and the
    reading is proved, as ``final:r`` or ``final:s``. Where both readings are
    members (amnas and amnar) nothing is proved and nothing is said.

**A one-vowel word is not inferred to be a particle.** The cādi gaṇa does list
a, i, u, ṛ, ḷ, e, ai, o, au — the one-vowel particles 1.1.14 names (*a apehi,
i indraḥ, u umeśaḥ*). But the letters of a lone ``i`` cannot tell the particle
from the *last sound of some word*, which is exactly how the engine's own
tests write a junction (``i a`` for the meeting of any -i with a vowel). To
call every such letter a particle would protect it from sandhi (6.1.125) and
turn the commonest test input into a refusal. So the caller says
``i{nipata}`` when a particle is meant; nothing is withheld from words of two
or more sounds. This is a limit stated, not a fact of the grammar: see
``COVERAGE`` on 1.4.57 and the OPEN notes of the prakṛtibhāva family.

**Deliberately not inferred:** anything that depends on meaning — a dual, a
vocative, a locative sense, whether an ā is the preverb āṅ or the āṅ-less
particle (Kāśikā on 1.1.14: ईषदर्थे क्रियायोगे मर्यादाभिविधौ च यः — एतमातं ङितं
विद्याद्वाक्यस्मरणयोरङित्) — or on a derivation the letters do not show. For
the same reason a bare ``ā`` is **not** inferred to be a nipāta: the prādi
entry is ``āṅ`` (with its इत्), the cādi gaṇa lists ā only as a savarṇa of
``a`` (1.1.69), and which of the two a lone ā is depends on its sense.
"""

from __future__ import annotations

from functools import lru_cache
from typing import FrozenSet, List, Optional, Sequence, Tuple

from src.astadhyayi import corpus
from src.astadhyayi.sandhi.segs import UPASARGA
from src.astadhyayi.varna import VISARGA

#: The sūtras whose gaṇas are read. (Sūtra numbers, not sounds; each is checked
#: against the corpus by `test_sandhi_prakrtibhava`.)
CADI = "1.4.57"
PRADI = "1.4.58"
SVARADI = "1.1.37"


@lru_cache(maxsize=None)
def gana_words(sutra_id: str) -> FrozenSet[str]:
    """Every member of every gaṇa the sūtra calls on, as the gaṇapāṭha has it."""
    return frozenset(item for gana in corpus.ganas_for(sutra_id)
                     for item in gana.items)


def _it_stripped(item: str) -> str:
    """The gaṇa item without a final ṅ or ñ — its इत् (1.3.3 हलन्त्यम्) —
    so that āṅ is met as ā. Used only where a boundary says an upasarga."""
    return item[:-1] if item[-1:] in ("ṅ", "ñ") and len(item) > 1 else item


def _in_class(text: str, sutra_id: str) -> bool:
    return text in gana_words(sutra_id)


def _one_vowel_word(text: str) -> bool:
    """True for a word that is a single vowel — ``i``, ``u``, ``e``, ``ai`` —
    which the letters cannot tell from the last sound of another word."""
    from src.astadhyayi.sandhi.parse import SandhiInputError, tokenize
    from src.astadhyayi.sandhi.segs import AC

    try:
        sounds = tokenize(text)
    except SandhiInputError:
        return False          # not a word of sounds: parse will say so itself
    return len(sounds) == 1 and sounds[0][0] in AC


def nipata_source(text: str) -> Optional[str]:
    """
    The sūtra whose gaṇa makes `text` a nipāta — 1.4.57 or 1.4.58 — or None.

    What a trace cites when it says *why* a word is a particle, so the sūtra
    is named from the gaṇa that holds the word and not from the sound of the
    word. A visarga-final word is read as either of its two finals, as
    `infer_flags` reads it.
    """
    for sutra in (CADI, PRADI):
        if any(_in_class(r, sutra) for r in _readings(text)):
            return sutra
    return None


def _readings(text: str) -> Tuple[str, ...]:
    """The two words a final visarga may stand for, स् first (the parser's
    default) and र् second; the word itself if it ends in no visarga."""
    if len(text) > 1 and text.endswith(VISARGA):
        stem = text[:-1]
        return (stem + "s", stem + "r")
    return (text,)


def infer_flags(text: str, *, position: int, words: Sequence[str],
                given: frozenset,
                bounds: Optional[Sequence[str]] = None,
                ) -> List[Tuple[str, str]]:
    """
    Flags provable for the word `text` at `position` among `words`, that the
    caller has not already given, each with its reason.

    `bounds`, when the caller has it, is what follows each word (see
    `segs.State.bounds`): it is how a preverb is recognised, since the letters
    of a word do not say it is one. `parse` does not yet hand it over, so the
    rules of this family read the boundary themselves as well.
    """
    from src.astadhyayi.sandhi.parse import to_iast
    from src.astadhyayi.sandhi.trace import both

    text = to_iast(text)
    found: List[Tuple[str, str]] = []
    have = set(given)
    shown = both(text)

    def add(flag: str, reason: str) -> None:
        if flag not in have and not any(flag == f for f, _ in found):
            found.append((flag, reason))

    # -- nipāta: the cādi and prādi gaṇas -----------------------------------
    if "nipata" not in have and "sattva" not in have \
            and not _one_vowel_word(text):
        readings = _readings(text)
        classes = ((CADI, "cādi", "1.4.57 चादयोऽसत्त्वे"),
                   (PRADI, "prādi", "1.4.58 प्रादयः"))
        for sutra, name, cited in classes:
            if all(_in_class(r, sutra) for r in readings) or \
                    _in_class(text, sutra):
                add("nipata",
                    f"{shown} is in the {{{name}}} gaṇa of the gaṇapāṭha "
                    f"({cited}), so it is a nipāta — as long as it names no "
                    f"substance here (asattve); if it does, give the flag "
                    f"sattva")
                break

    # -- the visarga: which indeclinable, hence which final ------------------
    if len(text) > 1 and text.endswith(VISARGA) \
            and not any(f.startswith("final:") for f in have):
        s_form, r_form = _readings(text)
        in_s, in_r = _in_class(s_form, SVARADI), _in_class(r_form, SVARADI)
        if in_r and not in_s:
            add("final:r",
                f"{shown} is read as {both(r_form)}: that is in the "
                f"{{svarādi}} gaṇa of indeclinables (1.1.37 "
                f"स्वरादिनिपातमव्ययम्) and {both(s_form)} is not, so the "
                f"visarga comes from र् and not from स्")
        elif in_s and not in_r:
            add("final:s",
                f"{shown} is read as {both(s_form)}: that is in the "
                f"{{svarādi}} gaṇa of indeclinables (1.1.37 "
                f"स्वरादिनिपातमव्ययम्) and {both(r_form)} is not, so the "
                f"visarga comes from स्")

    # -- the preverb: a prādi word across a `|` boundary ---------------------
    if bounds is not None and 0 <= position < len(bounds) \
            and bounds[position] == UPASARGA and "upasarga" not in have:
        stripped = {_it_stripped(i) for i in gana_words(PRADI)}
        if text in gana_words(PRADI) or text in stripped:
            add("upasarga",
                f"{shown} is in the {{prādi}} gaṇa (1.4.58 प्रादयः) and a "
                f"dhātu follows across a preverb boundary, so it is in "
                f"connection with a verb (kriyāyoge) and is an upasarga "
                f"(1.4.59 उपसर्गाः क्रियायोगे)")
            if "sattva" not in have:
                add("nipata",
                    f"{shown} is one of the {{prādi}}: 1.4.58 gives each "
                    f"the name nipāta before 1.4.59 gives it the name "
                    f"upasarga (1.4.56 leaves the two names together)")
            if text not in gana_words(PRADI):
                add("ang",
                    f"{shown} is the āṅ of the prādi gaṇa (its ṅ is an इत्, "
                    f"1.3.3), and an upasarga ā is always that: 1.1.14 "
                    f"leaves āṅ out (अनाङिति)")
    return found


__all__ = ["CADI", "PRADI", "SVARADI", "gana_words", "infer_flags",
           "nipata_source"]
