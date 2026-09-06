# -*- coding: utf-8 -*-
"""
The record for one sūtra of the Aṣṭādhyāyī, and the source apparatus.

The working method this schema encodes, per sūtra:

  1. the mūla — Pāṇini's own text
  2. the Kāśikā-tradition readings — Vasu, Katre, Sharma
  3. the Mahābhāṣya — Patañjali, then Joshi & Roodbergen,
     Abhyankar & Shukla (BORI), Benson (Kārakāhnika)
  4. notes drawn from the above
  5. the codification: an executable rule, tested

Two design rules make this trustworthy rather than merely tidy:

**Nothing is unattributed.** Every substantive claim sits in a `Reading`
carrying its source, a locator, and a status. A slot with no source consulted
yet is `PENDING` — visibly empty, never quietly filled with a plausible
paraphrase. `DERIVED` marks what the engine works out for itself (a pratyāhāra
expansion, say), which is checkable without any book.

**The code is the claim.** `Sutra.apply` is the codification; the tests are
what say it is right. A record whose commentary slots are all pending is still
useful if its rule is derived and tested — it just is not yet *understood* to
the depth the method asks for, and `coverage()` reports exactly that.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Callable, Dict, List, Optional, Tuple


class Source(str, Enum):
    """A text we read a sūtra through. Order is the reading order."""

    MULA = "mūla"                       # Pāṇini, Aṣṭādhyāyī (the sūtra itself)
    VASU = "vasu"                       # Śrīśa Chandra Vasu (1891), public domain
    KATRE = "katre"                     # Sumitra M. Katre, Aṣṭādhyāyī of Pāṇini (1987)
    SHARMA = "sharma"                   # Rama Nath Sharma, The Aṣṭādhyāyī of Pāṇini
    MAHABHASYA = "mahabhasya"           # Patañjali, Vyākaraṇa-Mahābhāṣya (mūla)
    JOSHI_ROODBERGEN = "joshi_roodbergen"
    ABHYANKAR_SHUKLA = "abhyankar_shukla"   # BORI edition
    BENSON = "benson"                   # James Benson, Kārakāhnika
    KASIKA = "kasika"                   # Kāśikāvṛtti (Vāmana & Jayāditya)

    # Kātyāyana's supplements. Not a commentary in the ordinary sense — the
    # tradition treats them as nearly part of the text, and the Mahābhāṣya is
    # largely an examination of them.
    VARTTIKA = "varttika"               # Kātyāyana, Vārttikas

    # The subcommentaries, all on disk and all keyed by sūtra. They are listed
    # after the Kāśikā because that is the order they are read in: a subcomment
    # is read to settle what the Kāśikā meant.
    NYASA = "nyasa"                     # Jinendrabuddhi, Kāśikāvivaraṇapañjikā
    PADAMANJARI = "padamanjari"         # Haradatta, Padamañjarī
    KAUMUDI = "kaumudi"                 # Bhaṭṭoji Dīkṣita, Siddhāntakaumudī
    TATTVABODHINI = "tattvabodhini"     # Jñānendra Sarasvatī, Tattvabodhinī
    BALAMANORAMA = "balamanorama"       # Vāsudeva Dīkṣita, Bālamanoramā


class Status(str, Enum):
    VERIFIED = "verified"       # read in the source; locator points at it
    DERIVED = "derived"         # computed by this engine; no book needed
    PENDING = "pending"         # slot exists, source not consulted yet
    ABSENT = "absent"           # source does not treat this sūtra
    UNREADABLE = "unreadable"   # source is here and cannot be read

    # UNREADABLE is not PENDING. Pending means nobody has opened the book;
    # unreadable means the file is on disk, has been opened, and will not yield
    # a citation — a damaged scan, an OCR run with the wrong model. The two call
    # for different work, and collapsing them loses that: a pending slot waits
    # for a reader, an unreadable one waits for a better copy. It therefore has
    # to carry a note saying what went wrong, or the next person repeats the
    # investigation.


class SutraType(str, Enum):
    """Pāṇini's own functional classes of rule."""

    SAMJNA = "saṃjñā"           # assigns a technical term
    PARIBHASA = "paribhāṣā"     # interpretive metarule
    VIDHI = "vidhi"             # prescribes an operation
    NIYAMA = "niyama"           # restricts an otherwise wider rule
    ATIDESA = "atideśa"         # extends a property by analogy
    ADHIKARA = "adhikāra"       # heading whose scope governs following sūtras
    NIPATANA = "nipātana"       # irregular form given ready-made


@dataclass(frozen=True)
class Reading:
    """What one source says, and where to find it."""

    source: Source
    status: Status
    #: Volume/page/section — precise enough to check. Required when VERIFIED.
    locator: str = ""
    #: The source's own words, quoted only where quotation is warranted.
    text: str = ""
    #: Our summary of this source's contribution.
    note: str = ""

    def __post_init__(self) -> None:
        if self.status is Status.VERIFIED and not self.locator:
            raise ValueError(
                f"{self.source.value}: a VERIFIED reading needs a locator so it "
                f"can be checked"
            )
        if self.status is Status.PENDING and (self.text or self.note):
            raise ValueError(
                f"{self.source.value}: a PENDING reading must stay empty — fill "
                f"it only from the source, or it is not attributable"
            )
        if self.status is Status.UNREADABLE and not self.note:
            raise ValueError(
                f"{self.source.value}: an UNREADABLE reading needs a note "
                f"saying what is wrong with the copy, or the next reader will "
                f"look again for nothing"
            )
        if self.status is Status.UNREADABLE and self.text:
            raise ValueError(
                f"{self.source.value}: an UNREADABLE reading cannot carry text "
                f"— that is what unreadable means"
            )


def pending(source: Source, locator: str = "") -> Reading:
    """A slot awaiting its book."""
    return Reading(source=source, status=Status.PENDING, locator=locator)


def unreadable(source: Source, note: str, locator: str = "") -> Reading:
    """A slot whose book is here but illegible. The note says why."""
    return Reading(
        source=source, status=Status.UNREADABLE, locator=locator, note=note
    )


@dataclass(frozen=True)
class SutraId:
    adhyaya: int
    pada: int
    number: int

    def __str__(self) -> str:
        return f"{self.adhyaya}.{self.pada}.{self.number}"

    @classmethod
    def parse(cls, text: str) -> "SutraId":
        parts = text.strip().split(".")
        if len(parts) != 3:
            raise ValueError(f"{text!r} is not an a.p.n sūtra id")
        adhyaya, pada, number = (int(p) for p in parts)
        if not 1 <= adhyaya <= 8:
            raise ValueError(f"{text}: adhyāya must be 1–8")
        if not 1 <= pada <= 4:
            raise ValueError(f"{text}: pāda must be 1–4")
        if number < 1:
            raise ValueError(f"{text}: sūtra number must be positive")
        return cls(adhyaya, pada, number)

    @property
    def sort_key(self) -> Tuple[int, int, int]:
        return (self.adhyaya, self.pada, self.number)

    @property
    def in_tripadi(self) -> bool:
        """
        True for 8.2.1 onward — the tripādī, whose rules are asiddha
        (treated as not having taken effect) with respect to what precedes.
        """
        return self.adhyaya == 8 and self.pada >= 2


@dataclass
class Sutra:
    """One sūtra: its text, how each source reads it, and its codification."""

    id: SutraId
    devanagari: str
    iast: str
    type: SutraType

    #: Word-split of the sūtra as it stands.
    padaccheda: Tuple[str, ...] = ()
    #: Words carried over from earlier sūtras that must be read into this one.
    anuvrtti: Tuple[str, ...] = ()
    #: The adhikāra heading in force here, as a sūtra id.
    adhikara: Optional[str] = None
    #: Sūtras this one depends on, restricts, or is restricted by.
    related: Tuple[str, ...] = ()
    #: Sūtras this rule's *implementation* actually leans on — not every
    #: rule it is textually connected to. 1.1.3 is `reuses` for 1.1.4,
    #: because the prohibition asks `is_ik` before it blocks anything;
    #: 1.1.2 is merely `related` to 1.1.1, since neither calls the other.
    #: Declared rather than inferred: see test_astadhyayi_reuse.
    reuses: Tuple[str, ...] = ()

    readings: Tuple[Reading, ...] = ()
    #: Our own working notes, distinct from any source's.
    notes: str = ""

    #: The codification. Signature varies by rule; documented per sūtra.
    apply: Optional[Callable] = field(default=None, repr=False)
    #: One-line statement of what `apply` computes.
    codification: str = ""

    def reading(self, source: Source) -> Optional[Reading]:
        return next((r for r in self.readings if r.source is source), None)

    def status_of(self, source: Source) -> Status:
        found = self.reading(source)
        return found.status if found else Status.PENDING

    @property
    def is_codified(self) -> bool:
        return self.apply is not None

    def coverage(self) -> Dict[str, List[str]]:
        """
        Which sources have been read and which are still outstanding — the
        honest progress report for this sūtra.
        """
        by_status: Dict[str, List[str]] = {s.value: [] for s in Status}
        for source in Source:
            by_status[self.status_of(source).value].append(source.value)
        return {k: v for k, v in by_status.items() if v}

    def __str__(self) -> str:
        return f"{self.id} {self.devanagari} ({self.iast})"


class SutraRegistry:
    """Every codified sūtra, addressable by id."""

    def __init__(self) -> None:
        self._sutras: Dict[str, Sutra] = {}

    def add(self, sutra: Sutra) -> Sutra:
        key = str(sutra.id)
        if key in self._sutras:
            raise ValueError(f"{key} is already registered")
        self._sutras[key] = sutra
        return sutra

    def get(self, sutra_id: str) -> Sutra:
        try:
            return self._sutras[sutra_id]
        except KeyError:
            raise KeyError(
                f"{sutra_id} is not codified yet"
            ) from None

    def has(self, sutra_id: str) -> bool:
        return sutra_id in self._sutras

    def all(self) -> List[Sutra]:
        return sorted(self._sutras.values(), key=lambda s: s.id.sort_key)

    def __len__(self) -> int:
        return len(self._sutras)

    def __contains__(self, sutra_id: str) -> bool:
        return sutra_id in self._sutras

    def progress(self) -> Dict[str, object]:
        """
        Where the whole effort stands. `total_sutras` is the traditional count
        of the Aṣṭādhyāyī; editions differ by a few, so it is a yardstick, not
        a target to be gamed.
        """
        codified = [s for s in self.all() if s.is_codified]
        fully_read = [
            s
            for s in self.all()
            if all(
                s.status_of(src) in (Status.VERIFIED, Status.ABSENT)
                for src in (Source.MULA, Source.VASU, Source.KATRE, Source.SHARMA)
            )
        ]
        return {
            "registered": len(self._sutras),
            "codified": len(codified),
            "primary_sources_read": len(fully_read),
            # 3,983 is the count of the text this codification
            # follows — the Kāśikā's numbering, which is what
            # `all_sutra_ids` enumerates and what every module has
            # been read against. The figure here was 3,959 for a
            # long time, from a recension that counts some sūtras
            # together; with the work finished it would have read
            # as 3,983 codified out of 3,959, so it is corrected
            # to the count actually being measured against.
            "total_sutras_traditional": 3983,
        }


#: The single registry the rule modules populate on import.
REGISTRY = SutraRegistry()
