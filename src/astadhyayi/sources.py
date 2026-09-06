# -*- coding: utf-8 -*-
"""
Builds a sūtra's source apparatus from the local reference corpus.

Hand-typing the mūla, padaccheda, anuvṛtti and every commentary into each
record would mean transcribing, by hand, text that is already sitting in
reference/ — 3,983 times, with a transcription error possible at every step.
This module reads it instead.

A rule module therefore says only what it alone knows — the codification, the
working notes, the cross-references — and calls `register`. Everything a
source can supply is supplied by the source, with a locator pointing back at
the file it came from.

What the corpus gives us per sūtra:

  data.json      Devanāgarī, roman, type (V/S/AT/AD/P), padaccheda with case
                 and number per word, anuvṛtti with the sūtra each word is
                 carried from, governing adhikāra, and a one-line paraphrase
  kashika.json   the Kāśikāvṛtti, and eleven further commentaries beside it
  vidyut/gretil  two independent witnesses to the sūtra text, collated
  mahabhasya     Patañjali, with Kielhorn volume/page/line

Only what a source actually says is recorded. Where a source is silent the
slot stays PENDING, exactly as if the book were still on the shelf.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from typing import Dict, List, Optional, Sequence, Tuple

from src.astadhyayi import corpus
from src.normalizer import devanagari_to_iast
from src.astadhyayi.sutra import (
    REGISTRY,
    Reading,
    Source,
    Status,
    Sutra,
    SutraId,
    SutraType,
    pending,
    unreadable,
)

# --- data.json ------------------------------------------------------------

#: ashtadhyayi.com's type codes, mapped onto Pāṇini's own classes of rule.
_TYPE_CODES: Dict[str, SutraType] = {
    "S": SutraType.SAMJNA,
    "P": SutraType.PARIBHASA,
    "V": SutraType.VIDHI,
    "AT": SutraType.ATIDESA,
    "AD": SutraType.ADHIKARA,
}

#: The case each vibhakti number denotes, for reading a padaccheda. 0 marks an
#: indeclinable, which has no case at all.
VIBHAKTI_NAMES: Dict[int, str] = {
    0: "avyaya",
    1: "prathamā",
    2: "dvitīyā",
    3: "tṛtīyā",
    4: "caturthī",
    5: "pañcamī",
    6: "ṣaṣṭhī",
    7: "saptamī",
    8: "sambodhana",
}
VACANA_NAMES: Dict[int, str] = {0: "", 1: "ekavacana", 2: "dvivacana", 3: "bahuvacana"}


@dataclass(frozen=True)
class PadaAnalysis:
    """One word of the sūtra, with the case and number it stands in."""

    word: str
    vibhakti: int
    vacana: int

    @property
    def case_name(self) -> str:
        return VIBHAKTI_NAMES.get(self.vibhakti, f"vibhakti {self.vibhakti}")

    def __str__(self) -> str:
        if self.vibhakti == 0:
            return f"{self.word} (avyaya)"
        number = VACANA_NAMES.get(self.vacana, "")
        return f"{self.word} ({self.case_name}{' ' + number if number else ''})"


@dataclass(frozen=True)
class AnuvrttiItem:
    """A word read into this sūtra from an earlier one."""

    word: str
    from_sutra: str

    def __str__(self) -> str:
        return f"{self.word} (from {self.from_sutra})"


@dataclass(frozen=True)
class AdhikaraItem:
    """A heading whose scope covers this sūtra."""

    text: str
    sutra: str

    def __str__(self) -> str:
        return f"{self.text} ({self.sutra})"


@dataclass(frozen=True)
class SutraFacts:
    """Everything data.json states about one sūtra."""

    id: str
    devanagari: str
    roman: str
    type: SutraType
    type_label: str
    padas: Tuple[PadaAnalysis, ...]
    anuvrtti: Tuple[AnuvrttiItem, ...]
    adhikara: Tuple[AdhikaraItem, ...]
    summary: str
    #: For an adhikāra, the last sūtra its scope reaches. 8.2.1
    #: pūrvatrāsiddham governs to 8.4.68 — the extent of the tripādī.
    scope_end: Optional[str] = None

    @property
    def padaccheda(self) -> Tuple[str, ...]:
        return tuple(p.word for p in self.padas)


def _code_to_id(code: str) -> str:
    """11001 -> 1.1.1"""
    code = str(code).strip()
    return f"{code[0]}.{code[1]}.{int(code[2:])}"


def _split_records(field: str) -> List[str]:
    return [part for part in field.split("##") if part.strip()]


def _parse_padaccheda(field: str) -> Tuple[PadaAnalysis, ...]:
    """`वृद्धिः$S$1$1$##आत्-ऐच्$S$1$1$` -> two words with case and number."""
    out: List[PadaAnalysis] = []
    for record in _split_records(field):
        parts = record.split("$")
        if not parts or not parts[0].strip():
            continue
        word = parts[0].strip()
        numbers = [p for p in parts[1:] if p.strip().isdigit()]
        vibhakti = int(numbers[0]) if numbers else 0
        vacana = int(numbers[1]) if len(numbers) > 1 else 0
        out.append(PadaAnalysis(word=word, vibhakti=vibhakti, vacana=vacana))
    return tuple(out)


def _parse_anuvrtti(field: str) -> Tuple[AnuvrttiItem, ...]:
    """`वृद्धिः$11001##गुणः$11002` -> the words, each with the sūtra it comes from."""
    out: List[AnuvrttiItem] = []
    for record in _split_records(field):
        parts = record.split("$")
        if len(parts) < 2 or not parts[0].strip():
            continue
        code = parts[1].strip()
        if not code.isdigit() or len(code) < 3:
            continue
        out.append(AnuvrttiItem(word=parts[0].strip(), from_sutra=_code_to_id(code)))
    return tuple(out)


def _parse_adhikara(field: str) -> Tuple[AdhikaraItem, ...]:
    """`पदस्य$8$1$16##पूर्वत्रासिद्धम्$8$2$1` -> headings with their sūtra ids."""
    out: List[AdhikaraItem] = []
    for record in _split_records(field):
        parts = [p.strip() for p in record.split("$")]
        if len(parts) < 4 or not parts[0]:
            continue
        numbers = [p for p in parts[1:] if p.isdigit()]
        if len(numbers) < 3:
            continue
        out.append(
            AdhikaraItem(
                text=parts[0],
                sutra=f"{int(numbers[0])}.{int(numbers[1])}.{int(numbers[2])}",
            )
        )
    return tuple(out)


_FACTS_CACHE: Dict[str, SutraFacts] = {}


def _load_facts() -> Dict[str, SutraFacts]:
    if _FACTS_CACHE:
        return _FACTS_CACHE
    raw = json.loads(corpus._read("commentary/data.json"))
    for record in raw["data"]:
        sutra_id = f"{record['a']}.{record['p']}.{record['n']}"
        type_field = record.get("type") or ""
        code, _, rest = type_field.partition("$")
        # An adhikāra entry carries the sūtra its scope reaches, after the
        # label: `AD$…$84068`. Keep it — the extent of a heading is the whole
        # point of a heading.
        label, _, tail = rest.rstrip("$").partition("$")
        scope_end = _code_to_id(tail) if tail.strip().isdigit() else None
        _FACTS_CACHE[sutra_id] = SutraFacts(
            id=sutra_id,
            devanagari=(record.get("s") or "").strip(),
            roman=(record.get("e") or "").strip(),
            type=_TYPE_CODES.get(code.strip(), SutraType.VIDHI),
            type_label=label.strip("$ ").strip(),
            scope_end=scope_end,
            padas=_parse_padaccheda(record.get("pc") or ""),
            anuvrtti=_parse_anuvrtti(record.get("an") or ""),
            adhikara=_parse_adhikara(record.get("ad") or ""),
            summary=(record.get("ss") or "").strip(),
        )
    return _FACTS_CACHE


def facts(sutra_id: str) -> SutraFacts:
    """What the corpus states about this sūtra, parsed."""
    loaded = _load_facts()
    try:
        return loaded[sutra_id]
    except KeyError:
        raise KeyError(f"{sutra_id} is not in the local sūtra data") from None


def all_sutra_ids() -> List[str]:
    """Every sūtra id the corpus knows, in order."""
    return sorted(
        _load_facts(),
        key=lambda i: tuple(int(part) for part in i.split(".")),
    )


# --- readings -------------------------------------------------------------

#: Which commentary file answers for which Source. Sources with no local text
#: are absent here and stay PENDING.
#: The commentaries on disk, in reading order, paired with their filenames.
#: Coverage across the 3,983 sūtras, measured: Kāśikā and Vasu 100%, the
#: Siddhāntakaumudī 99%, the Nyāsa 86%, the Padamañjarī 85%, the Bālamanoramā
#: 73%, the Tattvabodhinī 62%. Where one is silent its slot comes back ABSENT
#: rather than PENDING, since the text is here and simply says nothing.
_COMMENTARY_SOURCES: Sequence[Tuple[Source, str]] = (
    (Source.KASIKA, "kashika"),
    (Source.NYASA, "nyaas"),
    (Source.PADAMANJARI, "padamanjari"),
    (Source.KAUMUDI, "kaumudi"),
    (Source.TATTVABODHINI, "tattvabodhini"),
    (Source.BALAMANORAMA, "balamanorama"),
    (Source.VASU, "vasu_english"),
)

#: Everything the reading method wants that we cannot read from disk.
#:
#: Katre is the odd one here: the file IS downloaded, at
#: reference/translations/katre-astadhyayi.txt, 4.1 MB of it. It is unusable.
#: The scan was OCR'd with a Devanāgarī model, so the English has come out as
#: Devanāgarī glyph noise from the title page onward — measured across the whole
#: file, not one chunk of 4,000 characters in 582 reaches even 70% Latin
#: letters, and the median is zero. What survives is the parenthesised sūtra
#: references and nothing else. So the slot stays PENDING, but for a different
#: reason from the others, and the note says which: the volume has been fetched
#: and looked at, and it cannot be quoted. Re-fetching a different OCR of the
#: archive.org item is the thing to try, not reading this one harder.
_KATRE_NOTE = (
    "Downloaded to reference/translations/katre-astadhyayi.txt and checked: "
    "unusable. The scan was OCR'd with a Devanāgarī model, so the English is "
    "destroyed throughout — 0 of 582 chunks of 4,000 characters reach 70% "
    "Latin letters, median 0. Only the parenthesised sūtra numbers survive. "
    "The archive.org item offers no better text derivative: its _djvu.txt is "
    "4,139,661 bytes, the same file we hold, and the only other candidates are "
    "the 50 MB PDFs. Re-OCRing one of those with a Latin model is the only "
    "route left, and needs tooling this project does not have."
)

_STILL_ON_THE_SHELF: Sequence[Tuple[Source, str]] = (
    (Source.SHARMA, "Sharma, The Aṣṭādhyāyī of Pāṇini, on {id}"),
    (Source.JOSHI_ROODBERGEN, "Joshi & Roodbergen on {id}"),
    (Source.ABHYANKAR_SHUKLA, "Mahābhāṣya, BORI ed., on {id}"),
)

#: Benson's Kārakāhnika treats only these sūtras; elsewhere it is ABSENT, not
#: merely unread.
BENSON_RANGE = ("1.4.23", "1.4.55")


def _in_benson(sutra_id: str) -> bool:
    def key(text: str) -> Tuple[int, int, int]:
        return tuple(int(p) for p in text.split("."))  # type: ignore[return-value]

    return key(BENSON_RANGE[0]) <= key(sutra_id) <= key(BENSON_RANGE[1])


def _trim(text: str, limit: int = 700) -> str:
    """Keeps a quotation short enough to be a citation rather than a copy."""
    flat = re.sub(r"\s+", " ", text).strip()
    return flat if len(flat) <= limit else flat[:limit].rstrip() + " …"


def mula_reading(sutra_id: str) -> Reading:
    """
    The sūtra text, with both witnesses named and their agreement stated.

    A sūtra whose witnesses diverge is still recorded — but the divergence is
    put in the note, so it can never pass unnoticed.
    """
    fact = facts(sutra_id)
    collated = corpus.collate().get(sutra_id)
    witnesses = collated.witnesses if collated else {}
    kind = collated.classify() if collated else "single"

    if kind in ("identical", "sandhi", "orthographic"):
        agreement = {
            "identical": "Both witnesses give the same text.",
            "sandhi": (
                "The witnesses agree in wording; GRETIL prints the pre-sandhi "
                "words, Vidyut the sandhied run."
            ),
            "orthographic": "The witnesses differ only in how a nasal is written.",
        }[kind]
    elif kind == "divergent":
        agreement = (
            "WITNESSES DIVERGE — check before relying on this text. "
            f"GRETIL: {witnesses.get('gretil', '?')} / "
            f"Vidyut: {witnesses.get('vidyut', '?')}"
        )
    else:
        agreement = "Only one witness carries this sūtra."

    return Reading(
        source=Source.MULA,
        status=Status.VERIFIED,
        locator=(
            f"Aṣṭādhyāyī {sutra_id} — reference/commentary/data.json, "
            f"collated against mula/astadhyayi/ (vidyut, gretil)"
        ),
        text=f"{fact.devanagari} · {fact.roman}",
        note=agreement + (f" Paraphrase: {fact.summary}" if fact.summary else ""),
    )


def mahabhasya_reading(sutra_id: str) -> Reading:
    """Patañjali on this sūtra, located by Kielhorn volume/page/line."""
    segments = corpus.bhasya_on(sutra_id)
    if not segments:
        return Reading(
            source=Source.MAHABHASYA,
            status=Status.ABSENT,
            note="Patañjali does not comment on this sūtra.",
        )
    pages = [s.kielhorn for s in segments]
    span = pages[0] if pages[0] == pages[-1] else f"{pages[0]} – {pages[-1]}"
    return Reading(
        source=Source.MAHABHASYA,
        status=Status.VERIFIED,
        locator=(
            f"Mahābhāṣya on {sutra_id}, Kielhorn {span} "
            f"({len(segments)} segments; reference/mula/mahabhasya/)"
        ),
        text=_trim(segments[0].text, 300),
        note=(
            f"{len(segments)} segments. Kielhorn's pagination is the one the BORI "
            f"(Abhyankar) revision follows, so these locators carry over."
        ),
    )


def commentary_reading(sutra_id: str, source: Source, filename: str) -> Reading:
    """One commentary's own words on this sūtra, or an ABSENT slot if silent."""
    try:
        text = corpus.commentary_on(sutra_id, filename)
    except corpus.CorpusUnavailable:
        return pending(source, locator=f"{filename} on {sutra_id}")
    if not text:
        return Reading(
            source=source,
            status=Status.ABSENT,
            note=f"{corpus.COMMENTARIES[filename]} is silent on this sūtra.",
        )
    return Reading(
        source=source,
        status=Status.VERIFIED,
        locator=(
            f"{corpus.COMMENTARIES[filename]} on {sutra_id} — "
            f"reference/commentary/{filename}.json [{corpus.commentary_key(sutra_id)}]"
        ),
        text=_trim(text),
    )


def varttika_reading(sutra_id: str) -> Reading:
    """
    Kātyāyana on this sūtra, where he says anything: 921 vārttikas over 516 of
    the 3,983.

    Kept as its own source and not folded in with the commentaries, because a
    vārttika is not a comment on the rule but a correction or extension of it,
    and the record should show when one is in play. Several are already
    load-bearing: ऋऌवर्णयोर्मिथः सावर्ण्यं वाच्यम् is what joins ṛ and ḷ under
    1.1.9, and वर्णाश्रये नास्ति प्रत्ययलक्षणम् restricts 1.1.62.

    Where there is none the slot is ABSENT rather than PENDING — the collection
    is complete and it simply has nothing here.
    """
    found = corpus.varttikas_on(sutra_id)
    if not found:
        return Reading(
            source=Source.VARTTIKA,
            status=Status.ABSENT,
            note=f"No vārttika on {sutra_id} in the collection.",
        )
    return Reading(
        source=Source.VARTTIKA,
        status=Status.VERIFIED,
        locator=f"vārttika on {sutra_id} — reference/commentary/vartika.json",
        text=_trim(" ".join(v.text for v in found)),
        note=(
            f"{len(found)} vārttika{'s' if len(found) > 1 else ''} on this "
            f"sūtra."
        ),
    )


def readings_for(sutra_id: str) -> Tuple[Reading, ...]:
    """
    The full source apparatus for one sūtra, assembled from what is on disk.

    Read from the corpus: the mūla (two witnesses, collated), the Mahābhāṣya
    with Kielhorn locators, the Kāśikā, and Vasu's translation. Everything
    else keeps an honest PENDING or ABSENT slot.
    """
    out: List[Reading] = [mula_reading(sutra_id)]
    for source, filename in _COMMENTARY_SOURCES:
        out.append(commentary_reading(sutra_id, source, filename))
    out.append(mahabhasya_reading(sutra_id))
    out.append(varttika_reading(sutra_id))
    for source, template in _STILL_ON_THE_SHELF:
        out.append(pending(source, locator=template.format(id=sutra_id)))
    out.append(
        unreadable(
            Source.KATRE,
            note=_KATRE_NOTE,
            locator=f"Katre (1987) on {sutra_id}",
        )
    )
    out.append(
        pending(Source.BENSON, locator=f"Benson, Kārakāhnika, on {sutra_id}")
        if _in_benson(sutra_id)
        else Reading(
            source=Source.BENSON,
            status=Status.ABSENT,
            note=(
                f"Kārakāhnika treats {BENSON_RANGE[0]}–{BENSON_RANGE[1]}; "
                f"it does not reach {sutra_id}."
            ),
        )
    )
    return tuple(out)


# --- registration ---------------------------------------------------------


def register(
    sutra_id: str,
    *,
    apply=None,
    codification: str = "",
    notes: str = "",
    related: Sequence[str] = (),
    reuses: Sequence[str] = (),
    type_override: Optional[SutraType] = None,
    samjna: Optional[str] = None,
) -> Sutra:
    """
    Registers a sūtra, taking everything the corpus can supply from the corpus.

    A rule module passes only what it alone knows: the executable rule, a line
    saying what that rule computes, the working notes, and cross-references
    that the data does not already give as anuvṛtti or adhikāra.

    `samjna` names the technical term a saṃjñā-sūtra defines. It is stated per
    sūtra because it cannot be read off the corpus: a saṃjñā-sūtra's padas hold
    both the name and the thing named, and no mechanical test tells them apart
    (1.1.1 offers वृद्धिः and आत्-ऐच् alike). What it feeds is 1.1.68's
    अशब्दसंज्ञा clause, which has to know which words are terms of art.
    """
    fact = facts(sutra_id)
    adhikara = fact.adhikara[-1].sutra if fact.adhikara else None
    # Anuvṛtti already names the sūtras this one draws on; listing them again
    # under `related` would be noise.
    carried = {item.from_sutra for item in fact.anuvrtti}
    if samjna:
        from src.astadhyayi.grahana import register_samjna

        register_samjna(samjna, sutra_id)
    return REGISTRY.add(
        Sutra(
            id=SutraId.parse(sutra_id),
            devanagari=fact.devanagari,
            # data.json's own `e` field uses an ASCII scheme of its own
            # (vruddhiraadaich), which is not IAST and reads badly in a
            # report. The Devanāgarī is rendered instead, with the
            # project's transliterator — the same one whose agreement
            # with Vidyut across all 3,983 sūtras is 99.9%.
            iast=devanagari_to_iast(fact.devanagari),
            type=type_override or fact.type,
            padaccheda=fact.padaccheda,
            anuvrtti=tuple(str(item) for item in fact.anuvrtti),
            adhikara=adhikara,
            related=tuple(r for r in related if r not in carried),
            reuses=tuple(reuses),
            readings=readings_for(sutra_id),
            notes=notes,
            apply=apply,
            codification=codification,
        )
    )
