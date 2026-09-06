# -*- coding: utf-8 -*-
"""
३.३.१–३ — three rules that license words the Aṣṭādhyāyī does not derive.

Each of the three points OUTSIDE the sūtrapāṭha. 3.3.1 उणादयो बहुलम्
licenses the affixes of the उणादिपाठ, a separate text of 748 sūtras
which is on disk and is read here rather than restated. 3.3.2 lets the
same affixes be seen in the past. 3.3.3 भविष्यति गम्यादयः licenses a
list of finished words for the future.

So the pāda opens by handing three questions to authorities other than
itself, and the codification's job for these three is to say WHICH
authority and to be able to quote it — not to derive anything.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Optional, Tuple

from src.astadhyayi.corpus import UnadiSutra, load_unadipatha, unadi_sutra
from src.astadhyayi.upapada_krt import NotAdded

#: The three tenses the opening rules divide between them. वर्तमाने and
#: संज्ञायाम् run into 3.3.1 from 3.2.123 and 3.2.185 respectively —
#: वर्तमान इत्येव, संज्ञायामिति च — so 3.3.1 states neither and needs
#: both.
UNADI_TIME = "vartamāna"


@dataclass(frozen=True)
class Licensed:
    """
    A word the grammar admits without deriving it here, and the
    authority that admits it.

    `source` names the text — the उणादिपाठ, or the vṛtti's own list —
    and `locator` is where in it, so the claim is checkable.
    """

    by: str
    source: str
    why: str
    locator: str = ""
    text: str = ""


#: 3.3.1's own worked examples, each with the उणादि sūtra the Kāśikā
#: cites for it. The affixes are NOT restated: `locator` indexes the
#: उणादिपाठ on disk, and `unadi_text` reads the sūtra back out of it.
UNADI_EXAMPLES: Dict[str, str] = {
    "kāru": "1.1",
    "vāyu": "1.1",
    "pāyu": "1.1",
    "jāyu": "1.1",
    "māyu": "1.1",
    "svādu": "1.1",
    "sādhu": "1.1",
    "āśu": "1.1",
}

#: 3.3.2's — the same affixes seen in the PAST. भूतेऽपि दृश्यन्ते.
UNADI_PAST: Tuple[Tuple[str, str], ...] = (
    ("vartman", "वृत्तमिदं वर्त्म — this has happened, hence a track"),
    ("carman", "चरितं तदिति चर्म — it has been ranged over, hence a hide"),
    ("bhasman", "भसितं तदिति भस्म — it has been burnt, hence ashes"),
)

def _gamyadi() -> Tuple[str, ...]:
    """
    3.3.3's गम्यादि, READ FROM THE गणपाठ rather than typed out.

    It was typed out first, from the vṛtti's running text, and came to
    ten members where the corpus has nine — आगामी for आगमी, and an
    आयायी the list does not carry. 3.2.5 and 3.2.15 had already taught
    that the गणपाठ is the authority for its own lists; the lesson was
    applied in that pāda and not carried into this one.

    Falls back to nothing if the corpus is unavailable, so a missing
    file is an empty answer and never a wrong one.
    """
    try:
        from src.astadhyayi.corpus import load_ganapatha

        return tuple(
            item
            for gana in load_ganapatha().get("3.3.3", ())
            for item in gana.items
        )
    except Exception:
        return ()


#: 3.3.3's गम्यादि — finished words good for the FUTURE, given whole.
#: The vṛtti's point is that the AFFIX carries the future and not the
#: root: प्रत्ययस्यैव भविष्यत्कालता विधीयते न प्रकृतेः.
GAMYADI: Tuple[str, ...] = _gamyadi()


def unadi_text(locator: str) -> Optional[UnadiSutra]:
    """
    The उणादि sūtra at a locator, read from the corpus.

    Kept as its own function so both entry points can quote the source
    without either calling the other.
    """
    return unadi_sutra(locator)


def unadi(word: str = "", *, past: bool = False,
          samjna: bool = True) -> object:
    """
    3.3.1 and 3.3.2 — words formed by उणादि affixes.

    3.3.1 उणादयो बहुलम् admits them in the PRESENT where a name is
    meant; 3.3.2 भूतेऽपि दृश्यन्ते admits them in the past as well.

    बहुलम् is the whole difficulty and it is not resolved here. The
    vṛtti states its reach in three directions —
    यतो विहितास्ततोऽन्यत्रापि भवन्ति, they occur beyond where they were
    prescribed; केचिदविहिता एव प्रयोगत उन्नीयन्ते, some are inferred
    from usage having never been prescribed at all. So a word absent
    from the उणादिपाठ is not thereby refused, and this function says so
    rather than pretending to decide.
    """
    if past:
        for form, why in UNADI_PAST:
            if word in ("", form):
                if word:
                    return Licensed(
                        by="3.3.2",
                        source="Kāśikā on 3.3.2",
                        why="भूतेऽपि दृश्यन्ते — the उणादि affixes are "
                            "SEEN in the past too. " + why + ". And "
                            "दृशिग्रहणं प्रयोगानुसारार्थम्: the word "
                            "'seen' means the rule follows usage, the "
                            "same reading 3.2.75 was given and the "
                            "opposite of 3.2.178's.",
                    )
        return NotAdded(
            "",
            "3.3.2 admits उणादि affixes in the past, but बहुलम् runs "
            "down into it and the vṛtti gives only वर्त्म, चर्म and "
            "भस्म. That a word is not among them settles nothing")

    if not samjna:
        return NotAdded(
            "3.3.1",
            "संज्ञायामिति च — संज्ञायाम् runs down into 3.3.1 from "
            "3.2.185, so the उणादि affixes come where a NAME is "
            "meant. Neither condition is stated in the rule itself")

    locator = UNADI_EXAMPLES.get(word, "")
    quoted = unadi_text(locator) if locator else None
    return Licensed(
        by="3.3.1",
        source="उणादिपाठ (प०उ०)",
        locator=locator,
        text=quoted.text if quoted else "",
        why="उणादयो बहुलम् — the उणादि affixes come बहुलम् in the "
            "present where a name is meant. वर्तमान इत्येव, "
            "संज्ञायामिति च: the rule states neither condition and "
            "needs both, one running down from 3.2.123 and one from "
            "3.2.185. What it licenses is a SEPARATE TEXT of 748 "
            "sūtras, which is why the answer names a locator in it "
            "rather than an affix. बहुलम् then loosens even that: "
            "यतो विहितास्ततोऽन्यत्रापि भवन्ति, and केचिदविहिता एव "
            "प्रयोगत उन्नीयन्ते — some are inferred from usage having "
            "never been prescribed.",
    )


def gamyadi(word: str = "", *, anadyatana: bool = False) -> object:
    """
    3.3.3 भविष्यति गम्यादयः — words good for the future, given whole.

    The vṛtti makes a point the shape of the rule hides:
    प्रत्ययस्यैव भविष्यत्कालता विधीयते न प्रकृतेः — it is the AFFIX
    that is given the future sense, not the root. So these are not
    roots that mean something future; they are finished words whose
    affix carries the time.

    A vārttika adds अनद्यतन उपसंख्यानम् — श्वो गमी ग्रामम्, tomorrow —
    so the list reaches the not-today future as well.
    """
    if word and word not in GAMYADI:
        return NotAdded(
            "",
            "3.3.3 licenses the गम्यादि words for the future, and %s "
            "is not among the ten the vṛtti gives" % word)
    why = ("भविष्यति गम्यादयः — गमी ग्रामम्, आगामी, प्रस्थायी and the "
           "rest stand for the FUTURE. प्रत्ययस्यैव भविष्यत्कालता "
           "विधीयते न प्रकृतेः: it is the affix that is given the "
           "future, not the root — so what the rule licenses is a "
           "finished word and not a way of making one.")
    if anadyatana:
        why += (" अनद्यतन उपसंख्यानम् is a vārttika reaching the "
                "not-today future: श्वो गमी ग्रामम्.")
    return Licensed(
        by="3.3.3",
        source="Kāśikā on 3.3.3" + (" (vārttika)" if anadyatana else ""),
        why=why,
    )


def unadi_count() -> int:
    """
    How many sūtras the licensed text actually has.

    Asked from the corpus rather than written down, so it cannot go
    stale — the lesson four census tests taught in the pāda before.
    """
    return len(load_unadipatha())
