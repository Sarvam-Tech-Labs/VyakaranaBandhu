# -*- coding: utf-8 -*-
"""
पूर्वनिपात — which member of a compound is spoken first.

    2.2.30  उपसर्जनं पूर्वम्        the subordinate member leads
    2.2.31  राजदन्तादिषु परम्       except in one list, where it follows
    2.2.32  द्वन्द्वे घि             in a dvandva, a घि-ending leads
    2.2.33  अजाद्यदन्तम्            vowel-initial and अ-final leads instead
    2.2.34  अल्पाच्तरम्              failing those, the shorter one
    2.2.35  सप्तमीविशेषणे बहुव्रीहौ  in a bahuvrīhi, a locative or a qualifier
    2.2.36  निष्ठा                   or a निष्ठा
    2.2.37  वाहितग्न्यादिषु          in one list, the निष्ठा leads optionally
    2.2.38  कडाराः कर्मधारये        and कडार's class, optionally

This is a different question from the one `samasa` answers. That module
says whether two words compound and under what name; none of its rules
says a word about which comes out first, and none of its fields could hold
the answer without meaning something else. So the order is asked here.

**One rule and its exceptions.** 2.2.30 is the whole of the general case —
the उपसर्जन, the member some rule marked subordinate, is spoken first — and
everything after it either reverses that for a named list or settles the
order where 2.2.30 leaves it open. A dvandva has no upasarjana at all
(both members are principal), which is why 2.2.32 to 2.2.34 exist; a
bahuvrīhi's members are ALL upasarjana, सर्वोपसर्जनत्वात्, which is why
2.2.35 has to narrow it.

**Two members only.** 2.2.32, 2.2.33 and 2.2.34 are each read with
बहुष्वनियमः — where more than two words join, no order is laid down. The
Kāśikā's own अश्वरथेन्द्राः beside इन्द्ररथाश्वाः, and शङ्खदुन्दुभिवीणाः
beside वीणाशङ्खदुन्दुभयः, are pairs of forms both allowed. So a call with
more than two members is refused rather than answered.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Sequence, Tuple

from src.astadhyayi.formation import gana_items
from src.chandas.core import scan_phonemes


#: 2.2.31's राजदन्तादि — fifty-seven forms, given whole. The compound is
#: निपातित along with the order: राजदन्तः, अग्रेवणम्, and निपातनाद् अलुक्
#: keeps the locative ending of the second.
RAJADANTADI: Tuple[str, ...] = gana_items("2.2.31", "rājadantādi")

#: 2.2.37's आहिताग्न्यादि — thirteen, and आकृतिगणश्चायम्, so गडुकण्ठ and
#: its like belong here too without being written down.
AHITAGNYADI: Tuple[str, ...] = gana_items("2.2.37", "āhitāgnyādi")

#: 2.2.38's कडारादि — nineteen words, and the last gaṇa of the section.
KADARADI: Tuple[str, ...] = gana_items("2.2.38", "kaḍārādi")


@dataclass(frozen=True)
class Order:
    """Which word is spoken first, on whose authority."""

    first: str
    second: str
    by: str
    why: str
    #: Where the rule offers a choice, the other order it also allows.
    alternative: Optional[Tuple[str, str]] = None

    @property
    def optional(self) -> bool:
        return self.alternative is not None

    @property
    def text(self) -> str:
        return self.first + self.second


@dataclass(frozen=True)
class NoOrder:
    """Why no rule lays an order down here."""

    by: str
    why: str


def _vowels(word: str) -> int:
    return sum(1 for p in scan_phonemes(word) if p.kind == "vowel")


def _is_ajadyadanta(word: str) -> bool:
    """
    2.2.33's अजाद्यदन्त — beginning with a vowel and ending in short अ.

    तपरकरणं किम्? the Kāśikā asks, and answers with अश्वावृषौ beside
    वृषाश्वौ: the अ is tapara, so a long ā at the end does not qualify and
    the rule leaves that pair unordered.
    """
    sounds = list(scan_phonemes(word))
    if not sounds:
        return False
    return sounds[0].kind == "vowel" and sounds[-1].text == "a"


def _in(word: str, gana: Sequence[str]) -> bool:
    return word in gana


def spoken_first(
    members: Sequence[str],
    *,
    samasa: str = "tatpuruṣa",
    upasarjana: str = "",
    saptami: str = "",
    visesana: str = "",
    nistha: str = "",
    jati_kala_sukha: str = "",
    form: str = "",
) -> object:
    """
    The order, and the rule that fixes it.

    `upasarjana` names the member some rule marked subordinate — 1.2.43
    decides that, and it is stated here because which member is
    subordinate depends on the rule that formed the compound, not on the
    words. The same for `saptami`, `visesana` and `nistha`: each names a
    member, or is empty.

    `jati_kala_sukha` is the vārttika on 2.2.36 — निष्ठायाः पूर्वनिपाते
    जातिकालसुखादिभ्यः परवचनम् — naming a member after which the निष्ठा
    goes second instead: शार्ङ्गजग्धी, मासजातः.

    घि is NOT asked for, because 1.4.7 can answer it from the word: a
    short i- or u-final that is not सखि. That one is fetched. The others
    cannot be — 1.1.26 decides whether an AFFIX is निष्ठा and is given a
    word here, and 1.2.43's upasarjana depends on the rule that formed the
    compound rather than on either word. Where a rule can be asked it is
    asked, and where it cannot the caller says so.
    """
    from src.astadhyayi.nominal import ghi as ghi_of
    # 2.2.31 and 2.2.37 list FINISHED compounds, not pairs — राजदन्तः,
    # आहिताग्निः — so membership is tested on the form when one is named.
    # Building those strings back from the two words would mean redoing the
    # sandhi the gaṇa has already done.
    whole = form or ("".join(members) if len(members) == 2 else "")

    if len(members) != 2:
        return NoOrder(
            "",
            "बहुष्वनियमः — where more than two words join, no order is "
            "laid down: अश्वरथेन्द्राः and इन्द्ररथाश्वाः both stand, and "
            "so do शङ्खदुन्दुभिवीणाः and वीणाशङ्खदुन्दुभयः",
        )
    a, b = members

    # 2.2.38 कडाराः कर्मधारये — an option, and the last rule of the section.
    if samasa == "karmadhāraya":
        for lead, other in ((a, b), (b, a)):
            if _in(lead, KADARADI):
                return Order(
                    lead, other, "2.2.38",
                    "कडाराः कर्मधारये — these are quality-words and 2.2.35 "
                    "would have put them first as qualifiers; the sūtra "
                    "makes it a choice instead. कडारजैमिनिः beside "
                    "जैमिनिकडारः. कर्मधारय इति किम्? कडारपुरुषो ग्रामः",
                    alternative=(other, lead),
                )

    # 2.2.37 वाहितग्न्यादिषु — the same shape, against 2.2.36.
    if _in(whole, AHITAGNYADI):
        lead = nistha or a
        other = b if lead == a else a
        return Order(
            lead, other, "2.2.37",
            "वाहितग्न्यादिषु — 2.2.36 would have put the निष्ठा first "
            "without appeal; here it is a choice. अग्न्याहितः beside "
            "आहिताग्निः, जातपुत्रः beside पुत्रजातः. आकृतिगणश्चायम्",
            alternative=(other, lead),
        )

    # 2.2.31 राजदन्तादिषु परम् — the upasarjana goes LAST.
    if _in(whole, RAJADANTADI):
        lead = b if upasarjana == a else a
        other = a if lead == b else b
        return Order(
            lead, other, "2.2.31",
            "राजदन्तादिषु परम् — 2.2.30 would have put the subordinate "
            "member first and this puts it last. दन्तानां राजा gives "
            "राजदन्तः. The Kāśikā widens it past the upasarjana: न "
            "केवलम् उपसर्जनस्य, अन्यस्यापि यथालक्षणं विहितस्य "
            "पूर्वनिपातस्य अयम् अपवादः",
        )

    if samasa == "bahuvrīhi":
        # 2.2.36 निष्ठा, and the vārttika that reverses it.
        if nistha:
            other = b if nistha == a else a
            if jati_kala_sukha and jati_kala_sukha == other:
                return Order(
                    other, nistha, "2.2.36",
                    "निष्ठायाः पूर्वनिपाते जातिकालसुखादिभ्यः परवचनम् — the "
                    "vārttika puts the निष्ठा SECOND after a word of "
                    "kind, of time, or of ease: शार्ङ्गजग्धी, "
                    "पलाण्डुभक्षिती, मासजातः",
                )
            return Order(
                nistha, other, "2.2.36",
                "निष्ठा — a निष्ठा-ending word is spoken first in a "
                "bahuvrīhi: कृतकटः, भिक्षितभिक्षः, अवमुक्तोपानत्कः. The "
                "Kāśikā heads off the objection that a निष्ठा is anyway "
                "the qualifier — नैष नियमः, since which member qualifies "
                "which is a matter of how it is meant",
            )
        # 2.2.35 सप्तमीविशेषणे बहुव्रीहौ.
        lead = saptami or visesana
        if lead:
            other = b if lead == a else a
            which = "a locative" if lead == saptami else "a qualifier"
            return Order(
                lead, other, "2.2.35",
                f"सप्तमीविशेषणे बहुव्रीहौ — {which} is spoken first. A "
                f"bahuvrīhi's members are all subordinate — "
                f"सर्वोपसर्जनत्वाद् बहुव्रीहेः — so 2.2.30 settles "
                f"nothing and this has to. कण्ठेकालः, उरसिलोमा, चित्रगुः",
            )

    if samasa == "dvandva":
        # 2.2.33 beats 2.2.32, and the Kāśikā says so: द्वन्द्वे
        # घ्यन्तादजाद्यदन्तं विप्रतिषेधेन.
        for lead, other in ((a, b), (b, a)):
            if _is_ajadyadanta(lead) and not _is_ajadyadanta(other):
                return Order(
                    lead, other, "2.2.33",
                    "अजाद्यदन्तम् — a word beginning with a vowel and "
                    "ending in short अ leads: उष्ट्रखरम्. And it beats "
                    "2.2.32 where both could apply — द्वन्द्वे घ्यन्ताद् "
                    "अजाद्यदन्तं विप्रतिषेधेन: इन्द्राग्नी, इन्द्रवायू",
                )
        leads = [w for w in (a, b) if ghi_of(w).name is not None]
        if len(leads) == 1:
            lead = leads[0]
            other = b if lead == a else a
            return Order(
                lead, other, "2.2.32",
                "द्वन्द्वे घि — a घि-ending word leads: पटुगुप्तौ, "
                "मृदुगुप्तौ. Which words are घि is 1.4.7's and is "
                "fetched from it. अनेकप्राप्तावेकस्य नियमः, शेषे "
                "त्वनियमः — the rule fixes one place and leaves the rest",
            )
        if _vowels(a) != _vowels(b):
            lead, other = (a, b) if _vowels(a) < _vowels(b) else (b, a)
            return Order(
                lead, other, "2.2.34",
                f"अल्पाच्तरम् — the word with fewer vowels leads: "
                f"{lead} has {_vowels(lead)} against {_vowels(other)}. "
                f"प्लक्षन्यग्रोधौ, धवखदिरपलाशाः",
            )
        return NoOrder(
            "2.2.34",
            "अल्पाच्तरम् — and neither is shorter, so nothing here "
            "settles it",
        )

    # 2.2.30 उपसर्जनं पूर्वम् — the general case, and the whole of it.
    if upasarjana:
        other = b if upasarjana == a else a
        return Order(
            upasarjana, other, "2.2.30",
            "उपसर्जनं पूर्वम् — the subordinate member is spoken first, "
            "and the सूत्र says पूर्वम् to shut the other order out: "
            "पूर्ववचनं परप्रयोगनिवृत्त्यर्थम्, अनियमो हि स्यात्. "
            "कष्टश्रितः, शङ्कुलाखण्डः, यूपदारु, वृकभयम्, राजपुरुषः, "
            "अक्षशौण्डः — one for each case",
        )

    return NoOrder(
        "2.2.30",
        "उपसर्जनं पूर्वम् — but no member has been named the "
        "upasarjana, and 1.2.43 decides that from the rule that formed "
        "the compound. Without it the order is not settled",
    )


__all__ = [
    "AHITAGNYADI", "KADARADI", "NoOrder", "Order", "RAJADANTADI",
    "spoken_first",
]
