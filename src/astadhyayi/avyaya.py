# -*- coding: utf-8 -*-
"""
अव्यय — the indeclinables, 1.1.37 to 1.1.41.

    1.1.37  स्वरादिनिपातमव्ययम्      the svarādi words, and the particles
    1.1.38  तद्धितश्चासर्वविभक्तिः    a taddhita-final that lacks a full paradigm
    1.1.39  कृन्मेजन्तः               a kṛt-final in m or in eC
    1.1.40  क्त्वातोसुन्कसुनः          forms in ktvā, tosun, kasun
    1.1.41  अव्ययीभावश्च              and the avyayībhāva compound

Five ways of being indeclinable, and they have nothing in common but the
consequence — 2.4.82 अव्ययादाप्सुपः elides the ending. So this is a union and
not a definition, which is why the codification reports which of the five
applies rather than answering yes or no.

Two of the five point at gaṇas and both are ākṛtigaṇa: स्वरादि has 160 members
listed and is open, चादि 155 and open. So membership is decidable in one
direction only — a word in the list is avyaya, a word absent from it may still
be one, and `Avyaya.certain` says which case is in hand. That is a fact about
the grammar and not a shortcoming of the data.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Tuple

from src.chandas.core import scan_phonemes
from src.astadhyayi.corpus import gana_for
from src.astadhyayi.sivasutra import resolve


#: 1.1.40's three, in upadeśa. The Kāśikā's examples: कृत्वा and हृत्वा for
#: ktvā; पुरा सूर्यस्योदेतोः for tosun; and kasun by 3.4.17.
KTVA_TOSUN_KASUN: Tuple[str, ...] = ("ktvā", "tosun", "kasun")


@dataclass(frozen=True)
class Avyaya:
    """That a form is indeclinable, by which sūtra, and how surely."""

    by: str
    why: str
    #: False where the answer rests on an ākṛtigaṇa, which can only confirm.
    certain: bool = True


def _final(form: str) -> Optional[str]:
    phonemes = scan_phonemes(form)
    return phonemes[-1].text if phonemes else None


def avyaya(
    form: str,
    *,
    nipata: bool = False,
    taddhita_final: bool = False,
    sarvavibhakti: bool = True,
    krt_final: bool = False,
    krt_affix: str = "",
    avyayibhava: bool = False,
) -> Optional[Avyaya]:
    """
    Whether a form is avyaya, and on what ground.

    The conditions are what the five sūtras ask and a string cannot answer:
    whether the word is a particle, whether it ends in a taddhita or a kṛt,
    whether it takes a full set of case endings, whether it is an
    avyayībhāva. Each is a parameter for that reason.
    """
    svaradi = gana_for("1.1.37")
    cadi = gana_for("1.4.57")

    # 1.1.37 स्वरादिनिपातमव्ययम्
    if svaradi and form in svaradi:
        return Avyaya(
            "1.1.37",
            f"a member of स्वरादि: स्वर्, अन्तर्, प्रातर्, पुनर्, सनुतर्, "
            f"उच्चैस्, नीचैस्, शनैस् and the rest ({len(svaradi)} listed)",
        )
    if nipata:
        listed = bool(cadi and form in cadi)
        return Avyaya(
            "1.1.37",
            "a निपात" + (" — and चादि lists it" if listed else
                          " — चादि is an ākṛtigaṇa and does not list it, so "
                          "this rests on the caller's word"),
            certain=listed,
        )

    # 1.1.38 तद्धितश्चासर्वविभक्तिः
    if taddhita_final and not sarvavibhakti:
        return Avyaya(
            "1.1.38",
            "a taddhita-final without a full paradigm — यस्मान्न "
            "सर्वविभक्तेरुत्पत्तिः सोऽसर्वविभक्तिः: ततः, यतः, तत्र, यत्र, "
            "तदा, यदा, सर्वदा. असर्वविभक्तिरिति किम्? औपगवः, औपगवौ, "
            "औपगवाः — a taddhita WITH a paradigm is not avyaya",
        )

    # 1.1.39 कृन्मेजन्तः
    if krt_final and _final(form) in ("m",) + resolve("eC").sounds:
        return Avyaya(
            "1.1.39",
            f"a kṛt-final ending in {_final(form)} — m or an eC: "
            f"स्वादुंकारं भुङ्क्ते for the m, वक्षे and एषे for the eC",
        )

    # 1.1.40 क्त्वातोसुन्कसुनः
    if krt_affix in KTVA_TOSUN_KASUN:
        return Avyaya(
            "1.1.40",
            f"formed with {krt_affix}: कृत्वा, हृत्वा for ktvā, "
            f"पुरा सूर्यस्योदेतोः for tosun",
        )

    # 1.1.41 अव्ययीभावश्च
    if avyayibhava:
        return Avyaya(
            "1.1.41",
            "an अव्ययीभाव compound. The Kāśikā asks किं प्रयोजनम्? and "
            "answers लुङ्मुखस्वरोपचाराः — the elision of 2.4.82 giving "
            "उपाग्नि and प्रत्यग्नि, and the accent that follows from it",
        )
    return None


def is_avyaya(form: str, **conditions) -> bool:
    return avyaya(form, **conditions) is not None


__all__ = ["Avyaya", "KTVA_TOSUN_KASUN", "avyaya", "is_avyaya"]
