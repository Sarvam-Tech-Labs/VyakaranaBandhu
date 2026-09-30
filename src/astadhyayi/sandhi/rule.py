# -*- coding: utf-8 -*-
"""
What a sandhi rule is, and what it hands back.

A rule is asked one question — *where, in what you can see, do you apply?* —
and answers with zero or more `Application`s. Each says **where** (the `site`),
**what to change** (the `edits`), and **why, in the grammar's own terms**
(the `Detail`): the sthānin, the ādeśa, the nimitta, and the sūtras that make
the operation land where it does.

The last of those is what this whole engine is for. A step that says only
"6.1.77 iko yaṇaci" leaves the reader to work out *which* इक् (1.1.69), *which*
यण् (1.1.50 स्थानेऽन्तरतमः, or 1.3.10 यथासंख्यम्), *which side* of the vowel the
change falls on (1.1.66 तस्मिन्निति निर्देशे पूर्वस्य) and *how much* of the
sthānin goes (1.1.52 अलोऽन्त्यस्य). Those are sūtras too, and each is named in
`Detail.via` with the sentence saying what it did *here*.

**Where the sounds come from.** A rule never types a class of sounds. इक् is
`sivasutra.resolve("iK")`, the यण् that goes with it is chosen by 1.1.50 from
`resolve("yaṆ")`, whether two vowels are alike is 1.1.9 (`varna.savarna`). The
repository's `test_astadhyayi_no_restating` reads every module under
`src/astadhyayi/` and fails if one collection of sounds is written out in two,
so a shortcut is caught, not merely discouraged.

**A rule may not edit what it sees only through its past.** `View` shows a rule
an *ancestor* of a sound the rule is not entitled to see (8.2.1). Reading that
ancestor is the point; *changing* the real sound standing there would be to
act on something that did not exist for the rule. The builders below record
that in `Edit.hidden`, and the engine drops such an application rather than
apply it.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, FrozenSet, Iterable, Optional, Tuple, Union

from src.astadhyayi.sandhi.segs import (
    AGAMA, EKADESA_MARK, Seg, Sight, View, _words)
from src.astadhyayi.vipratisedha import Strength


# ---------------------------------------------------------------------------
# The vocabulary a step is described in
# ---------------------------------------------------------------------------

#: What kind of operation a step is — the traditional names.
ADESA = "ādeśa"                    # one sound replaced by another
EKADESA = "ekādeśa"                # one substitute for two sounds (6.1.84)
AGAMA_KIND = "āgama"               # a sound put in (1.1.46 आद्यन्तौ टकितौ)
LOPA = "lopa"                      # a sound lost (1.1.60 अदर्शनं लोपः)
DVITVA = "dvitva"                  # a sound said twice (8.4.46–47)
PRAKRTIBHAVA = "prakṛtibhāva"      # left as it is: no change at all
PRATISEDHA = "pratiṣedha"          # a rule refused: what it would have done is not done
KINDS = (ADESA, EKADESA, AGAMA_KIND, LOPA, DVITVA, PRAKRTIBHAVA, PRATISEDHA)

#: Whose authority a step rests on. Nothing a vārttika teaches is to be
#: passed off as Pāṇini's own.
SUTRA = "sūtra"
VARTTIKA = "vārttika"
BHASYA = "bhāṣya"
AUTHORITIES = (SUTRA, VARTTIKA, BHASYA)


@dataclass(frozen=True)
class Via:
    """A sūtra a step leans on, and what it contributed *here*."""

    sutra: str
    role: str


@dataclass(frozen=True)
class Detail:
    """
    A step in the grammar's terms.

    Text in `because`, `nimitta` and `Via.role` may write Sanskrit terms in IAST
    inside braces — "{ik} before {aC}" — and the trace prints each as
    इक् (ik), so every term appears in both scripts as the project requires.
    """

    kind: str
    #: What was replaced, in IAST ("i", "a+i"). For an āgama, what it was
    #: inserted beside; for prakṛtibhāva, what was kept.
    sthanin: str
    #: What stands there now. "" for a loss.
    adesa: str
    #: The condition that brought the rule to bear.
    nimitta: str
    #: Why the rule applies here — its conditions, checked against this form.
    because: str
    via: Tuple[Via, ...] = ()
    authority: str = SUTRA
    #: The vārttika's own words, when `authority` is VARTTIKA.
    varttika: str = ""
    note: str = ""


# ---------------------------------------------------------------------------
# What to change
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class NewSeg:
    """A sound to be put in, before the engine has given it a history."""

    s: str
    marks: FrozenSet[str] = frozenset()
    #: Word of the new sound; the replaced sound's own if left None.
    w: Optional[int] = None
    lw: Optional[int] = None
    show: str = ""


@dataclass(frozen=True)
class Edit:
    """Replace `segs[start:end]` by `new`. An insertion has start == end."""

    start: int
    end: int
    new: Tuple[NewSeg, ...]
    #: The rule saw only the ancestor of what really stands here; see the
    #: module docstring. The engine will not apply such an edit.
    hidden: bool = False


@dataclass(frozen=True)
class Application:
    """One place a rule applies, and everything needed to apply and explain it."""

    #: The uids of every sound the rule READ or will EDIT. Two applications
    #: whose sites share a sound are contending for one place — that is what
    #: makes 1.4.2 and 8.2.1 the right questions to ask.
    #:
    #: A rule that REFUSES another (8.4.44 शात् refusing 8.4.40; a
    #: प्रतिषेध) has no edit to make and is still an application: it names the
    #: very site of the rule it refuses, wins it by `overrides`, and the engine
    #: then records that neither is to be offered there again.
    site: Tuple[int, ...]
    edits: Tuple[Edit, ...]
    detail: Detail
    #: "" or the kind of option this is (विभाषा, अन्यतरस्याम्). An optional
    #: application makes the derivation fork: once with it, once without.
    optional: str = ""

    @property
    def hidden(self) -> bool:
        return any(edit.hidden for edit in self.edits)


# ---------------------------------------------------------------------------
# Builders — so a rule says what it means and cannot forget the bookkeeping
# ---------------------------------------------------------------------------

Spec = Union[str, NewSeg]


def _spec(item: Spec, w: Optional[int], lw: Optional[int] = None) -> NewSeg:
    if isinstance(item, NewSeg):
        return item if item.w is not None else NewSeg(
            item.s, item.marks, w, item.lw if item.lw is not None else lw,
            item.show)
    return NewSeg(item, frozenset(), w, lw)


def replace(sight: Sight, *new: Spec) -> Edit:
    """The sound at `sight`, replaced by `new` (several sounds if the
    substitute is more than one — अय्, आव्)."""
    return Edit(sight.real, sight.real + 1,
                tuple(_spec(n, sight.w, sight.seg.lw) for n in new),
                hidden=sight.through)


def ekadesa(left: Sight, right: Sight, *new: Spec) -> Edit:
    """
    One substitute for two sounds — 6.1.84 एकः पूर्वपरयोः.

    It belongs to the word of the *later* sound and remembers the earlier
    one's, so 6.1.85 अन्तादिवत् can treat it as the end of the first word and
    the beginning of the second.
    """
    both_words = _words(left.seg) | _words(right.seg)
    lw = min(both_words) if len(both_words) > 1 else None
    made = []
    for n in new:
        spec = _spec(n, max(both_words), lw)
        # Marked, so that a viewer for whom 6.1.86 षत्वतुकोरसिद्धः holds — a
        # ṣatva or a tuk rule — can be shown the two sounds it replaced.
        made.append(NewSeg(spec.s, spec.marks | {EKADESA_MARK}, spec.w,
                           spec.lw, spec.show))
    return Edit(left.real, right.real + 1, tuple(made),
                hidden=left.through or right.through)


def delete(sight: Sight, *marks: str) -> Edit:
    """
    The sound lost — 1.1.60 अदर्शनं लोपः.

    Kept as an empty sound and not removed: an earlier rule must still be able
    to find what the loss took away (8.2.1), and a rule that *names* the loss
    (6.3.111 ढ्रलोपे) must be able to see that it happened.
    """
    return Edit(sight.real, sight.real + 1,
                (NewSeg("", frozenset(marks), sight.w, sight.seg.lw),),
                hidden=sight.through)


def insert_after(sight: Sight, s: str, *marks: str) -> Edit:
    """A sound put in immediately after `sight` — an āgama (1.1.46)."""
    return Edit(sight.real + 1, sight.real + 1,
                (NewSeg(s, frozenset(marks) | {AGAMA}, sight.w),),
                hidden=sight.through)


def insert_before(sight: Sight, s: str, *marks: str) -> Edit:
    """A sound put in immediately before `sight`."""
    return Edit(sight.real, sight.real,
                (NewSeg(s, frozenset(marks) | {AGAMA}, sight.w),),
                hidden=sight.through)


def remark(sight: Sight, *marks: str) -> Edit:
    """The same sound, given a mark — how a prakṛtibhāva rule records that it
    has left a vowel alone, so that no other rule touches it afterwards."""
    seg = sight.seg
    return Edit(sight.real, sight.real + 1,
                (NewSeg(seg.s, seg.marks | frozenset(marks), seg.w, seg.lw,
                        seg.show),),
                hidden=sight.through)


def sk(text: str) -> str:
    """Mark Sanskrit in an explanation, so the trace prints it in both
    scripts: sk("ā") gives "{ā}", printed as आ (ā)."""
    return "{" + text + "}"


def site(*sights: Sight) -> Tuple[int, ...]:
    """The places a rule read or will change, named by the sounds that really
    stand there — so two rules reaching one place compare equal even when one
    of them sees only the past of what stands in it."""
    return tuple(sorted(set(s.real_uid for s in sights)))


# ---------------------------------------------------------------------------
# The rule
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Rule:
    """A sūtra (or a vārttika on one) as something the engine can apply."""

    sutra: str
    name: str
    find: Callable[[View], Iterable[Application]]
    #: Tags for the kinds of rule this is ("ac", "ekadesa", "hal", ...), which
    #: `overrides` can name as a group with a leading "@".
    families: FrozenSet[str] = frozenset()
    #: (target, why) — what this rule displaces when both could apply at one
    #: place. `target` is a sūtra id, or "@family". It is the अपवाद relation,
    #: and it is a fact the tradition states about a *pair*, so each entry
    #: carries the reason and the trace can print it.
    overrides: Tuple[Tuple[str, str], ...] = ()
    #: Marks this rule may see even where 8.2.1 would hide them. The rule's
    #: own wording names them, and 'वचनप्रामाण्यात्' lets it. See `segs`.
    consumes: FrozenSet[str] = frozenset()
    #: Where 1.4.2 is not the right way to weigh this rule against another.
    standing: Strength = Strength.EQUAL
    vedic: bool = False
    authority: str = SUTRA
    varttika: str = ""
    #: The operation this rule performs, named from the closed vocabulary in
    #: `operations.py`, where that matters to what the rule may see. 6.1.86
    #: षत्वतुकोरसिद्धः makes an एकादेश asiddha to exactly two — "ṣatva" and
    #: "tuk" — so a rule that says it is one of them is shown the sounds the
    #: substitute replaced, not the substitute.
    operation: str = ""

    @property
    def order(self) -> Tuple[int, ...]:
        return tuple(int(p) for p in self.sutra.split("."))

    @property
    def key(self) -> str:
        """What names this rule in the engine's bookkeeping: its sūtra, and for
        a vārttika the vārttika too — 6.1.101 and the vārttika on it stand at
        one number and are two rules."""
        return f"{self.sutra}:{self.varttika}" if self.varttika else self.sutra

    @property
    def label(self) -> str:
        """The rule as a reader should be told of it: a vārttika is not Pāṇini."""
        return f"{self.sutra} (vārttika)" if self.varttika else self.sutra

    def overrides_rule(self, other: "Rule") -> Optional[str]:
        """Why this rule displaces `other`, or None if it does not."""
        for target, why in self.overrides:
            if target == other.sutra:
                return why
            if target.startswith("@") and target[1:] in other.families:
                return why
        return None


def rule(
    sutra: str,
    *,
    name: str,
    families: Iterable[str] = (),
    overrides: Iterable[Tuple[str, str]] = (),
    consumes: Iterable[str] = (),
    standing: Strength = Strength.EQUAL,
    vedic: bool = False,
    authority: str = SUTRA,
    varttika: str = "",
    operation: str = "",
) -> Callable[[Callable[[View], Iterable[Application]]], Rule]:
    """
    Declare a rule::

        @rule("6.1.77", name="इको यणचि", families=("ac",))
        def yan(v: View):
            for j in v.junctions():
                ...
                yield Application(...)

    The decorated function becomes a `Rule`; its docstring stays with it.
    """

    def wrap(fn: Callable[[View], Iterable[Application]]) -> Rule:
        built = Rule(
            sutra=sutra, name=name, find=fn,
            families=frozenset(families), overrides=tuple(overrides),
            consumes=frozenset(consumes), standing=standing, vedic=vedic,
            authority=authority, varttika=varttika, operation=operation)
        object.__setattr__(built, "__doc__", fn.__doc__)
        return built

    return wrap


__all__ = [
    "ADESA", "AGAMA_KIND", "AUTHORITIES", "Application", "BHASYA", "DVITVA",
    "Detail", "EKADESA", "Edit", "KINDS", "LOPA", "NewSeg", "PRAKRTIBHAVA",
    "PRATISEDHA", "Rule", "SUTRA", "VARTTIKA", "Via", "delete", "ekadesa", "insert_after",
    "insert_before", "remark", "replace", "rule", "site",
]
