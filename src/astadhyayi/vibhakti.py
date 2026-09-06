# -*- coding: utf-8 -*-
"""
The endings, the persons, and the two names adhyāya 1 closes on — 1.4.99 to 1.4.110.

    1.4.99 – 1.4.100   परस्मैपद and आत्मनेपद, as names of the *endings*
    1.4.101 – 1.4.104  प्रथम, मध्यम, उत्तम; the three numbers; विभक्ति
    1.4.105 – 1.4.108  which person a verb takes
    1.4.109 – 1.4.110  संहिता and अवसान

Two of these close loops opened long before. 1.3.12 अनुदात्तङित आत्मनेपदम् used
the name आत्मनेपद ninety-odd sūtras before 1.4.100 gives it, and 1.2.39
स्वरितात् संहितायाम् used संहिता before 1.4.109 defines it. That is ordinary in
the Aṣṭādhyāyī and worth noticing rather than smoothing over: the text is not
written to be read once forwards.

The eighteen तिङ् endings are the Kāśikā's list and not this project's. 3.4.78,
which teaches them, is not codified, so they are taken from the commentary on
1.4.101, which sets them out in six rows of three — exactly the arrangement the
sūtra's त्रीणि त्रीणि describes.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Optional, Tuple

#: The eighteen, as the Kāśikā on 1.4.101 sets them out: nine parasmaipada
#: then nine ātmanepada, each nine in three rows of three.
PARASMAIPADA_ENDINGS: Tuple[Tuple[str, str, str], ...] = (
    ("tip", "tas", "jhi"),      # प्रथम
    ("sip", "thas", "tha"),     # मध्यम
    ("mip", "vas", "mas"),      # उत्तम
)
ATMANEPADA_ENDINGS: Tuple[Tuple[str, str, str], ...] = (
    ("ta", "ātām", "jha"),      # प्रथम
    ("thās", "āthām", "dhvam"), # मध्यम
    ("iṭ", "vahi", "mahiṅ"),    # उत्तम
)

PRATHAMA, MADHYAMA, UTTAMA = "prathama", "madhyama", "uttama"

#: The three persons and the three numbers, in 1.4.101's order — तिङस्त्रीणि
#: त्रीणि, प्रथम (prathama) first and उत्तम (uttama) last, which is the
#: reverse of the European numbering. Public because they name the rows and
#: columns of the ending tables above, and anything that indexes those
#: tables has to say the same three words; a second copy elsewhere would be
#: a second statement of 1.4.101.
PERSONS: Tuple[str, str, str] = (PRATHAMA, MADHYAMA, UTTAMA)
NUMBERS: Tuple[str, str, str] = ("ekavacana", "dvivacana", "bahuvacana")


@dataclass(frozen=True)
class EndingFacts:
    """Everything 1.4.99 to 1.4.104 says about one ending."""

    ending: str
    pada: Optional[str]
    person: Optional[str]
    number: Optional[str]
    vibhakti: bool
    by: Tuple[str, ...]
    why: str


def _index() -> Dict[str, EndingFacts]:
    found: Dict[str, EndingFacts] = {}
    for pada, rows, sutra in (
        ("parasmaipada", PARASMAIPADA_ENDINGS, "1.4.99"),
        ("ātmanepada", ATMANEPADA_ENDINGS, "1.4.100"),
    ):
        for person, row in zip(PERSONS, rows):
            for number, ending in zip(NUMBERS, row):
                found[ending] = EndingFacts(
                    ending=ending, pada=pada, person=person, number=number,
                    vibhakti=True,
                    by=(sutra, "1.4.101", "1.4.102", "1.4.104"),
                    why=(
                        f"{sutra} names it {pada}; 1.4.101 तिङस्त्रीणि त्रीणि "
                        f"puts the nine in three rows of three and calls them "
                        f"प्रथम, मध्यम, उत्तम in order; 1.4.102 takes each row "
                        f"three at a time — एकशः — for the three numbers; and "
                        f"1.4.104 विभक्तिश्च names the whole set विभक्ति."
                    ),
                )
    return found


_ENDINGS = _index()


def ending_facts(ending: str) -> Optional[EndingFacts]:
    """
    What 1.4.99 to 1.4.104 say about one तिङ् ending.

    The four sūtras work together and none of them does anything alone, which
    is why they are answered together: 1.4.101 gives the persons by position,
    1.4.102 the numbers by position within that, and the whole depends on the
    eighteen standing in a fixed order.
    """
    return _ENDINGS.get(ending)


def endings_of(*, pada: Optional[str] = None, person: Optional[str] = None,
               number: Optional[str] = None) -> Tuple[str, ...]:
    """The endings matching a description — the index read backwards."""
    return tuple(
        e.ending for e in _ENDINGS.values()
        if (pada is None or e.pada == pada)
        and (person is None or e.person == person)
        and (number is None or e.number == number)
    )


# --- 1.4.105 to 1.4.108: which person -------------------------------------


@dataclass(frozen=True)
class PersonVerdict:
    """Which person the verb takes, by which sūtra."""

    person: str
    by: str
    why: str
    #: 1.4.106's एकवत् — and in the singular whatever the subject's number.
    singular: bool = False


def person_for(
    *,
    upapada: Optional[str] = None,
    coreferential: bool = True,
    prahasa: bool = False,
    is_manyati: bool = False,
) -> PersonVerdict:
    """
    1.4.105 to 1.4.108 — which of the three persons a verb takes.

    The condition is an उपपद that is समानाधिकरण with the verb's agent, and the
    Kāśikā widens it twice: व्यवहिते चाव्यवहिते, separated or not, and
    प्रयुज्यमानेऽप्यप्रयुज्यमानेऽपि — whether the pronoun is actually uttered
    or not. That second clause is what स्थानिनि in the sūtra means, and it is
    why पचसि alone is second person with no त्वम् anywhere.
    """
    if prahasa and upapada == "manya":
        if is_manyati:
            return PersonVerdict(
                UTTAMA, "1.4.106",
                "मन्यतेरुत्तम एकवच्च — and मन् itself takes the first person, "
                "in the singular whatever the number: एहि मन्ये ओदनं "
                "भोक्ष्यसे. मध्यमोत्तमयोः प्राप्तयोः उत्तममध्यमौ विधीयेते — "
                "the two are swapped, which is the joke.",
                singular=True,
            )
        return PersonVerdict(
            MADHYAMA, "1.4.106",
            "प्रहासे च मन्योपपदे — in derision, with मन् beside it, the verb "
            "takes the second person. प्रहासः परिहासः क्रीडा.",
        )

    if upapada == "yuṣmad" and coreferential:
        return PersonVerdict(
            MADHYAMA, "1.4.105",
            "युष्मद्युपपदे समानाधिकरणे स्थानिन्यपि मध्यमः — त्वं पचसि, and "
            "पचसि too, since अप्रयुज्यमानेऽपि: the pronoun need not be "
            "uttered.",
        )
    if upapada == "asmad" and coreferential:
        return PersonVerdict(
            UTTAMA, "1.4.107",
            "अस्मद्युत्तमः — अहं पचामि, and पचामि alone.",
        )
    return PersonVerdict(
        PRATHAMA, "1.4.108",
        "शेषे प्रथमः — from the remainder, the third person. The residue "
        "clause of the three, as 1.3.78 is of the two padas.",
    )


# --- 1.4.109 and 1.4.110 ---------------------------------------------------

SAMHITA, AVASANA = "saṃhitā", "avasāna"


@dataclass(frozen=True)
class Juncture:
    """What the gap between two sounds is called."""

    name: str
    by: str
    why: str


def juncture(*, gap_matras: Optional[float] = None,
             stopped: bool = False) -> Juncture:
    """
    1.4.109 and 1.4.110 — संहिता and अवसान.

    परः is read as अतिशये, 'in the highest degree', and संनिकर्ष as
    प्रत्यासत्ति: the closest possible proximity, which the Kāśikā measures —
    अर्धमात्राकालव्यवधानम्, a half-mātrā's interval. दध्यत्र, मध्वत्र.

    This is the condition 1.2.39 स्वरितात् संहितायाम् was already using, "
    ninety sūtras before it is defined.
    """
    if stopped:
        return Juncture(
            AVASANA, "1.4.110",
            "विरामोऽवसानम् — विरतिर्विरामः, or विरम्यतेऽनेनेति वा विरामः. "
            "दधिँ, मधुँ. It is what 8.3.15 खरवसानयोर्विसर्जनीयः waits on.",
        )
    if gap_matras is not None and gap_matras <= 0.5:
        return Juncture(
            SAMHITA, "1.4.109",
            "परः सन्निकर्षः संहिता — परशब्दोऽतिशये वर्तते, संनिकर्षः "
            "प्रत्यासत्तिः: the closest proximity, अर्धमात्राकालव्यवधानम्. "
            "दध्यत्र, मध्वत्र.",
        )
    return Juncture(
        "", "—",
        "Neither the closest proximity nor a stop, so neither name applies.",
    )


__all__ = [
    "ATMANEPADA_ENDINGS",
    "AVASANA",
    "EndingFacts",
    "Juncture",
    "MADHYAMA",
    "PARASMAIPADA_ENDINGS",
    "PRATHAMA",
    "PersonVerdict",
    "SAMHITA",
    "UTTAMA",
    "ending_facts",
    "endings_of",
    "juncture",
    "person_for",
]
