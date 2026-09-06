# -*- coding: utf-8 -*-
"""
The operations rules talk *about*, as a closed vocabulary.

Several sūtras do not perform an operation but name one and say something of
it: 1.1.58 lists ten that 1.1.57 shall not reach, 2.1.2 confines itself to
accent and refuses ṣatva and ṇatva, 8.2.2 names the four in which a lost न्
still counts. Each of those was matching a **bare string**, and nothing
checked it:

    sthanivat(operation="dīrgha")   → False, by 1.1.58
    sthanivat(operation="dirgha")   → True,  by 1.1.57     ← no macron
    sthanivat(operation="")         → True,  by 1.1.57

A missing macron did not fail. It silently took the other branch and named a
different sūtra as the authority, which is the failure this codification
keeps meeting: not a crash, but a confident wrong answer. A closed vocabulary
turns that into a refusal.

**What this deliberately does not do.** It does not record whether an
operation is an अल्विधि. That looks like the obvious next field and it is a
trap: whether गुण counts as an operation on sounds is argued in the
commentaries, not settled by the operation's identity, and a boolean here
would quietly turn one reading of a disputed question into the codification's
answer for every rule that asks. The caller states it, as they always did,
and the docstring on 1.1.56 says why.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, Optional, Tuple


@dataclass(frozen=True)
class Operation:
    """One operation a rule can name."""

    #: The key. IAST, as the rest of the codification writes it.
    name: str
    devanagari: str
    #: One line, for the reader and for the playground's hint.
    gist: str
    #: The sūtra that prescribes it, where a single one does. Several of
    #: these — svara, padānta, sandhi — are classes of operation rather than
    #: one rule, and say so by leaving this empty.
    prescribed_by: str = ""


def _op(name, devanagari, gist, prescribed_by=""):
    return Operation(name, devanagari, gist, prescribed_by)


#: Every operation the codified rules name. Sourced from the rules that name
#: them — 1.1.58's ten, 2.1.2's two, 8.2.2's four — plus those the worked
#: examples use. Each sūtra number below was read from the corpus, not
#: recalled.
OPERATIONS: Dict[str, Operation] = {
    op.name: op for op in (
        # --- the ten 1.1.58 withholds from 1.1.57 -----------------------
        _op("padānta", "पदान्त",
            "an operation at the end of a word — कौ स्तः, यौ स्तः"),
        _op("dvirvacana", "द्विर्वचन",
            "reduplication — दद्ध्यत्र, and see 1.1.59 for the case it "
            "lets back in"),
        _op("vare", "वरे",
            "the operation before वर — अप्सु यायावरः"),
        _op("yalopa", "यलोप",
            "elision of य्"),
        _op("svara", "स्वर",
            "an accent operation — 2.1.2 is confined to these and reaches "
            "nothing else"),
        _op("savarṇa", "सवर्ण",
            "an operation resting on two sounds being homogeneous", "1.1.9"),
        _op("anusvāra", "अनुस्वार",
            "substitution of anusvāra for म्", "8.3.23"),
        _op("dīrgha", "दीर्घ",
            "lengthening a vowel", "6.1.101"),
        _op("jaś", "जश्",
            "a jhal at word-end becoming its jaś", "8.2.39"),
        _op("car", "चर्",
            "a jhal before khar becoming its car", "8.4.55"),
        _op("kutva", "कुत्व",
            "a cu becoming the ku of its own place", "8.2.30"),
        _op("dhatva", "धत्व",
            "a त् or थ् after a jhaṣ becoming ध्", "8.2.40"),
        # --- the two 2.1.2 refuses --------------------------------------
        _op("ṣatva", "षत्व",
            "स् becoming ष्", "8.3.59"),
        _op("ṇatva", "णत्व",
            "न् becoming ण्", "8.4.2"),
        # --- the four 8.2.2 names ---------------------------------------
        _op("sup", "सुप्",
            "a rule about the nominal endings"),
        _op("saṃjñā", "संज्ञा",
            "a rule conferring a technical name"),
        _op("tuk", "तुक्",
            "the तुक् augment", "6.1.71"),
        # --- and the ones the worked examples use -----------------------
        _op("guṇa", "गुण",
            "substitution of अ, ए or ओ", "7.3.84"),
        _op("vṛddhi", "वृद्धि",
            "substitution of आ, ऐ or औ", "7.2.115"),
        _op("lopa", "लोप",
            "disappearance — अदर्शनं लोपः", "1.1.60"),
        _op("luk", "लुक्",
            "one of the three named elisions", "1.1.61"),
        _op("ślu", "श्लु",
            "one of the three named elisions", "1.1.61"),
        _op("lup", "लुप्",
            "one of the three named elisions", "1.1.61"),
        _op("samprasāraṇa", "सम्प्रसारण",
            "a semivowel giving way to the vowel of its own class", "1.1.45"),
        _op("yaṇ", "यण्",
            "इ, उ, ऋ, ऌ becoming य्, व्, र्, ल् before a vowel", "6.1.77"),
        _op("sandhi", "सन्धि",
            "a junction operation between sounds"),
        _op("upadhā-dīrgha", "उपधादीर्घ",
            "lengthening the penultimate", "7.2.116"),
        _op("ṭi-lopa", "टिलोप",
            "elision of the final टि portion", "6.4.143"),
        _op("nalopa", "नलोप",
            "loss of a final न्", "8.2.7"),
        _op("root-hood", "धातुत्व",
            "a rule that treats something as a root — not an operation on "
            "sounds, and the standing example of what स्थानिवत् does reach"),
    )
}


class UnknownOperation(ValueError):
    """Raised where a rule is asked about an operation with no such name."""


def resolve(name: Optional[str]) -> Optional[Operation]:
    """
    The operation of this name, None where none was stated.

    Raises :class:`UnknownOperation` for a name that is not in the
    vocabulary — which is the whole point. Before this, `"dirgha"` for
    `"dīrgha"` was answered rather than refused, and the answer named the
    wrong sūtra.
    """
    if name is None:
        return None
    key = name.strip()
    if not key:
        return None
    found = OPERATIONS.get(key)
    if found is None:
        raise UnknownOperation(
            f"no operation named {name!r}. The codified rules name these: "
            + ", ".join(sorted(OPERATIONS))
        )
    return found


def is_operation(name: str) -> bool:
    return bool(name) and name.strip() in OPERATIONS


def names() -> Tuple[str, ...]:
    return tuple(sorted(OPERATIONS))


def among(name: Optional[str], group: Iterable[str]) -> bool:
    """
    Whether the named operation is one of `group`.

    Both sides go through the vocabulary, so a rule cannot quietly hold a
    list of operations that do not exist — 1.1.58's ten are checked against
    the registry at import, not the first time someone asks.
    """
    resolved = resolve(name)
    if resolved is None:
        return False
    wanted = set()
    for entry in group:
        other = resolve(entry)
        if other is not None:
            wanted.add(other.name)
    return resolved.name in wanted


def check_group(group: Iterable[str], where: str) -> Tuple[str, ...]:
    """Validate a rule's list of operations at import. Returns it unchanged."""
    group = tuple(group)
    unknown = [g for g in group if g not in OPERATIONS]
    if unknown:
        raise UnknownOperation(
            f"{where} names operations that are not in the vocabulary: "
            f"{', '.join(sorted(unknown))}"
        )
    return group


__all__ = [
    "Operation", "OPERATIONS", "UnknownOperation",
    "resolve", "is_operation", "names", "among", "check_group",
]
