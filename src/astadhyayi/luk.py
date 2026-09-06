# -*- coding: utf-8 -*-
"""
Shortening, disappearance, and five sūtras that teach nothing — 1.2.47 to 1.2.57.

    1.2.47  ह्रस्वो नपुंसके प्रातिपदिकस्य     a neuter stem shortens its final
    1.2.48  गोस्त्रियोरुपसर्जनस्य             and so does गो or a feminine, subordinate
    1.2.49  लुक् तद्धितलुकि                   the feminine affix goes instead
    1.2.50  इद्गोण्याः                        but गोणी takes इ
    1.2.51  लुपि युक्तवद्व्यक्तिवचने          under लुप्, gender and number as before
    1.2.52  विशेषणानां चाजातेः                and for the qualifiers too
    1.2.53  तदशिष्यं संज्ञाप्रमाणत्वात्        — and none of that needed teaching
    1.2.54  लुब्योगाप्रख्यानात्
    1.2.55  योगप्रमाणे च तदभावेऽदर्शनं स्यात्
    1.2.56  प्रधानप्रत्ययार्थवचनमर्थस्यान्यप्रमाणत्वात्
    1.2.57  कालोपसर्जने च तुल्यम्

The last five are unlike anything else codified so far. They prescribe nothing.
Each says of some doctrine that it is अशिष्य — not to be taught — and gives the
reason. Four of the five are aimed at the पूर्वाचार्याः, the earlier teachers
whose formulations Pāṇini is discarding: 1.2.56 rejects their account of how a
compound's members share out its meaning, and 1.2.57 their definitions of
'today' and of उपसर्जन, on one and the same ground — अर्थस्यान्यप्रमाणत्वात्,
that meaning is settled elsewhere than in a grammar.

The Kāśikā's gloss on that is the clearest statement in the pāda of what
Pāṇini thought he was doing: यैरपि व्याकरणं न श्रुतं तेऽपि राजपुरुषमानयेत्युक्ते
राजविशिष्टं पुरुषमानयन्ति — even those who have never studied grammar, told to
fetch the king's man, fetch the king's man and not the king. यश्च लोकतोऽर्थः
सिद्धः किं तत्र यत्नेन: what usage already settles needs no rule.

So `asisya` returns a record and not an operation, and that is the honest
shape. A codification that made these five into functions producing forms
would be inventing work they explicitly decline to do.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, FrozenSet, Optional, Tuple

from src.astadhyayi.adesa import antya, hrasva_of, replace_antya
from src.astadhyayi.svara import LONG_VOWELS, SHORT_VOWELS

#: Which short vowel each long one shortens to. ऐ and औ shorten to their own
#: first element rather than to a long-less counterpart, which is why 1.2.47's
#: worked forms are अतिरि and अतिनु and not anything in ऐ.
#: 1.2.47 and 1.2.48 shorten a stem's final vowel, and which vowel that
#: gives is not theirs to say. It stood here as a nine-row table until every
#: row turned out to be something already codified: the four diphthongs are
#: 1.1.48's, the five simple vowels are the savarṇa of one mātrā (1.1.9 with
#: 1.2.27), and ṝ → ṛ rather than ḷ is 1.1.50 breaking the tie. `hrasva_of`
#: asks all of them, so this asks it.

def _shortened(vowel: str) -> Optional[str]:
    """The short counterpart, or None where the final is already short."""
    short = hrasva_of(vowel)
    return None if short is None or short == vowel else short



@dataclass(frozen=True)
class Shortened:
    """What a stem becomes, and by which sūtra."""

    form: str
    by: str
    why: str
    changed: bool = True


def hrasva(
    stem: str,
    *,
    napumsaka: bool = False,
    upasarjana: bool = False,
    ends_in_go: bool = False,
    stri_pratyaya: bool = False,
    taddhita_luk: bool = False,
    ends_in_goni: bool = False,
) -> Shortened:
    """
    1.2.47 to 1.2.50 — what happens to a stem's final vowel.

    The four run in order of increasing specificity and the later displace the
    earlier, which the Kāśikā says each time: पूर्वेण ह्रस्वत्वे प्राप्ते
    लुग्विधीयते at 1.2.49, पूर्वेण लुकि प्राप्ते इकारो विधीयते at 1.2.50. So the
    codification tests them backwards.
    """
    last = antya(stem)

    # 1.2.50 इद्गोण्याः — इ where the shortening or the luk would have come.
    if ends_in_goni and taddhita_luk:
        # अलोऽन्त्यस्य, and this sūtra is the Kāśikā's own example of it: the
        # इ goes in the room of the final ī and not of गोणी entire. So the
        # last sound is replaced by 1.1.52's function rather than by slicing
        # the string here — which is the same edit, until the day it is not.
        return Shortened(
            replace_antya(stem, "i") if stem.endswith("ī") else stem,
            "1.2.50",
            "इद्गोण्याः — गोणी takes इ where 1.2.49 would have dropped the "
            "affix: पञ्चभिर्गोणीभिः क्रीतः पटः पञ्चगोणिः. The Kāśikā adds that "
            "the इत् is a योगविभाग reaching सूची too — पञ्चसूचिः",
        )

    # 1.2.49 लुक् तद्धितलुकि — the feminine affix goes rather than shortens.
    if taddhita_luk and stri_pratyaya and upasarjana:
        dropped = stem
        for ending in ("ī", "ā", "ū"):
            if stem.endswith(ending):
                dropped = stem[: -len(ending)]
                break
        return Shortened(
            dropped, "1.2.49",
            "लुक् तद्धितलुकि — पूर्वेण ह्रस्वत्वे प्राप्ते लुग् विधीयते: where a "
            "taddhita has dropped, the subordinate feminine affix drops too "
            "rather than shortening. पञ्चेन्द्राण्यो देवता अस्य पञ्चेन्द्रः; "
            "आमलक्याः फलम् आमलकम्",
        )

    # 1.2.48 गोस्त्रियोरुपसर्जनस्य
    if upasarjana and (ends_in_go or stri_pratyaya):
        if _shortened(last) is not None:
            return Shortened(
                replace_antya(stem, _shortened(last)), "1.2.48",
                "गोस्त्रियोरुपसर्जनस्य — a stem ending in a subordinate गो or a "
                "subordinate feminine affix shortens: चित्रगुः, निष्कौशाम्बिः, "
                "अतिखट्वः. उपसर्जनस्येति किम्? राजकुमारी",
            )
        return Shortened(stem, "1.2.48", "the final is already short", False)

    # 1.2.47 ह्रस्वो नपुंसके प्रातिपदिकस्य
    if napumsaka:
        if _shortened(last) is not None:
            return Shortened(
                replace_antya(stem, _shortened(last)), "1.2.47",
                "ह्रस्वो नपुंसके प्रातिपदिकस्य — the substitute goes on the last "
                "vowel by 1.1.52 अलोऽन्त्यस्य: अतिरि कुलम्, अतिनु कुलम्. "
                "नपुंसक इति किम्? ग्रामणीः, सेनानीः",
            )
        return Shortened(stem, "1.2.47", "the final is already short", False)

    return Shortened(
        stem, "—",
        "Nothing in 1.2.47–1.2.50 reaches this stem, so it stands as it is.",
        False,
    )


# --- 1.2.51 and 1.2.52, लुप् and युक्तवद्भाव ------------------------------


@dataclass(frozen=True)
class Yuktavat:
    """The gender and number a लुप्-form carries, and where they came from."""

    gender: Optional[str]
    number: Optional[int]
    by: str
    why: str


def yuktavat(
    *,
    gender: Optional[str] = None,
    number: Optional[int] = None,
    lup: bool = True,
    qualifier: bool = False,
    jati: bool = False,
) -> Yuktavat:
    """
    1.2.51 and 1.2.52 — under लुप्, the gender and number of what came before.

    युक्तवत् is glossed by the Kāśikā through the क्तवतु of निष्ठा: युक्तः
    प्रकृत्यर्थः प्रत्ययार्थेन संबद्धः, the base-meaning as it was joined to the
    affix-meaning. So पञ्चालाः, masculine plural as the name of the warriors,
    stays masculine plural as the name of the country.

    व्यक्ति and वचन are the older teachers' words for gender and number —
    पूर्वाचार्यनिर्देशः, and the Kāśikā observes तदीयमेवेदं सूत्रम्, the sūtra
    itself is theirs. Which is why 1.2.53 turns round and discards it.
    """
    if not lup:
        return Yuktavat(
            gender, number, "—",
            "लुपीति किम्? Only under लुप् — not under लुक्, where लवणः सूपः, "
            "लवणा यवागूः, लवणं शाकम. show the gender following the noun "
            "qualified instead.",
        )
    if qualifier and jati:
        return Yuktavat(
            None, None, "1.2.52",
            "अजातेः — the class-word itself is excepted, and with it whatever "
            "qualifies through the class: पञ्चालाः जनपदः, and then पञ्चालाः "
            "जनपदो रमणीयो बह्वन्नः, singular throughout.",
        )
    if qualifier:
        return Yuktavat(
            gender, number, "1.2.52",
            "विशेषणानां चाजातेः — the qualifiers follow too: पञ्चालाः रमणीयाः "
            "बह्वन्नाः, गोदौ रमणीयौ बह्वन्नौ.",
        )
    return Yuktavat(
        gender, number, "1.2.51",
        "लुपि युक्तवद्व्यक्तिवचने — the gender and number are those the word "
        "had before the affix disappeared: पञ्चालाः, कुरवः, मगधाः.",
    )


# --- 1.2.53 to 1.2.57, what needs no teaching -----------------------------


@dataclass(frozen=True)
class Asisya:
    """A doctrine Pāṇini declines to teach, and his reason for declining."""

    topic: str
    sutra: str
    reason: str
    whose: str
    explanation: str


#: The five, each keyed by what it declines. Nothing is computed here and
#: nothing could be: these are positions, and the record is the codification.
ASISYA: Tuple[Asisya, ...] = (
    Asisya(
        topic="yuktadbhāva",
        sutra="1.2.53",
        reason="संज्ञाप्रमाणत्वात्",
        whose="the rule just given, 1.2.51",
        explanation=(
            "पञ्चाल and वरणा are names and not descriptions — नैते योगशब्दाः, "
            "किं तर्हि? जनपदादीनां संज्ञा एताः. A name carries its own gender "
            "and number by nature, तत्र लिङ्गं वचनं च स्वभावसिद्धमेव न "
            "यत्नप्रतिपाद्यम्, as आपः, दाराः, गृहाः, सिकताः and वर्षाः do. So "
            "1.2.51 had nothing to prescribe."
        ),
    ),
    Asisya(
        topic="lup",
        sutra="1.2.54",
        reason="योगाप्रख्यानात्",
        whose="4.2.81 जनपदे लुप् and 4.2.82 वरणादिभ्यश्च",
        explanation=(
            "The connection those rules presuppose is not there to be seen: "
            "न हि पञ्चाला वरणा इति योगः संबन्धः प्रख्यायते. नैतद् उपलभामहे "
            "वृक्षयोगान् नगरे वरणा इति — nobody understands the city to be "
            "called वरणा from any connection with the trees. And if the "
            "taddhita never arose, there is nothing for a लुप् to remove: "
            "किं लुपो विधानेन."
        ),
    ),
    Asisya(
        topic="the-argument-for-it",
        sutra="1.2.55",
        reason="तदभावेऽदर्शनं स्यात्",
        whose="anyone holding that these words do describe a connection",
        explanation=(
            "The argument, and the only one of the five that is one. If "
            "पञ्चाल really denoted the connection, then where the connection "
            "failed the word would fail with it — तदभावेऽदर्शनम् अप्रयोगः "
            "स्यात्. But it does not: दृश्यते च संप्रति विनैव क्षत्रियसंबन्धेन "
            "जनपदेषु पञ्चालादिशब्दः. The word is still used of the country "
            "with no warriors in view, so it was never the connection it "
            "named. रूढिरूपेणैव तत्र प्रवृत्तः."
        ),
    ),
    Asisya(
        topic="how-a-compound-divides-its-meaning",
        sutra="1.2.56",
        reason="अर्थस्यान्यप्रमाणत्वात्",
        whose="the पूर्वाचार्याः",
        explanation=(
            "Their formula was प्रधानोपसर्जने प्रधानार्थं सह ब्रूतः, "
            "प्रकृतिप्रत्ययौ सहार्थं ब्रूतः — head and dependent together state "
            "the head's meaning, base and affix together state theirs. "
            "तत् पाणिनिराचार्यः प्रत्याचष्टे. Words mean what they mean by "
            "nature and not by stipulation, शब्दैरर्थाभिधानं स्वाभाविकं न "
            "पारिभाषिकम्, and the proof offered is that people who have never "
            "studied grammar get it right: told राजपुरुषम् आनय they bring the "
            "king's man, न राजानं नापि पुरुषमात्रम्."
        ),
    ),
    Asisya(
        topic="the-definitions-of-today-and-of-upasarjana",
        sutra="1.2.57",
        reason="अर्थस्यान्यप्रमाणत्वात् (तुल्यम्)",
        whose="the पूर्वाचार्याः again, and other grammarians",
        explanation=(
            "Two more of their definitions go the same way, and the तुल्यम् is "
            "what carries the reason over. One party fixed 'today' as आ "
            "न्याय्यादुत्थानाद् आ न्याय्याच् च संवेशनात्, from getting up to "
            "lying down; another as अहरुभयतोऽर्धरात्रम्, midnight to midnight. "
            "And उपसर्जन they defined as अप्रधानम्. All three are discarded on "
            "the same ground: people who never studied grammar say इदम् "
            "अस्माभिर् अद्य कर्तव्यम् and mean it correctly.\n\n"
            "The Kāśikā asks why this was not folded into 1.2.56 and answers "
            "that the separation is प्रदर्शनार्थः, to show the kind: "
            "अन्यदप्येवंजातीयकम् अशिष्यम्. It then lists four more of the old "
            "definitions that go with them — मत्वर्थे बहुव्रीहिः, "
            "पूर्वपदार्थप्रधानोऽव्ययीभावः, उत्तरपदार्थप्रधानस्तत्पुरुषः, "
            "उभयपदार्थप्रधानो द्वन्द्वः."
        ),
    ),
)


def asisya(topic: Optional[str] = None) -> Tuple[Asisya, ...]:
    """
    What 1.2.53–1.2.57 decline to teach, and why.

    Returns records rather than performing anything, because these five
    prescribe nothing. A codification that turned them into operations would
    be inventing exactly the work they refuse.
    """
    if topic is None:
        return ASISYA
    return tuple(entry for entry in ASISYA if entry.topic == topic)


def is_asisya(topic: str) -> bool:
    return bool(asisya(topic))


__all__ = [
    "ASISYA",
    "Asisya",
    "Shortened",
    "Yuktavat",
    "asisya",
    "hrasva",
    "is_asisya",
    "yuktavat",
]
