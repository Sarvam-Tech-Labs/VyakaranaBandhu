# -*- coding: utf-8 -*-
"""
नदी, घि, लघु, गुरु, अङ्ग, पद, भ, and the three numbers — 1.4.3 to 1.4.22.

Eight saṃjñās in twenty sūtras, all of them under 1.4.1's एका संज्ञा. That
adhikāra is not decoration here: three of the eight are in direct competition
with another, and in each case it is 1.4.1 that decides which name stands.

    1.4.10 लघु against 1.4.11 गुरु    a short vowel before a conjunct
    1.4.17 पद against 1.4.18 भ        before a vowel-initial sup affix
    1.4.3  नदी against 1.4.7 घि       an ī- or ū-final feminine

So `vipratisedha.eka_samjna` is called rather than the answer being written
out, and each verdict says which sūtra it lost to. The Kāśikā works the first
of those three itself while glossing 1.4.1 — शिक्षा and भिक्षा come out गुरु
and not लघु, and the consequence it draws is that अततक्षत् does not get
7.4.93's सन्वद्भाव.

One thing in the block cuts against that adhikāra and is worth flagging: the
vārttika on 1.4.20 reads उभयसंज्ञान्यपि, that the अयस्मय group may carry
*both* names. Under 1.4.1 that should be impossible, and the record says so.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Tuple

from src.astadhyayi.adesa import antya
from src.astadhyayi.formation import begins_with
from src.astadhyayi.vipratisedha import Rule, eka_samjna

#: 1.4.3's two finals, and 1.4.7's. यू is ई and ऊ, and the Kāśikā notes the
#: निर्देश is अविभक्तिक — the sūtra's यू carries no case ending.
_LONG_IU = ("ī", "ū")
_SHORT_IU = ("i", "u")


@dataclass(frozen=True)
class Named:
    """A saṃjñā a form takes, by which sūtra, and what it beat."""

    name: Optional[str]
    by: str
    why: str
    optional: bool = False
    instead_of: Tuple[str, ...] = ()


# --- 1.4.3 to 1.4.9: नदी and घि -------------------------------------------


def nadi(
    word: str,
    *,
    stri_akhya: bool = True,
    iyan_uvan_place: bool = False,
    is_stri: bool = False,
    before_am: bool = False,
    before_ngit: bool = False,
) -> Named:
    """
    1.4.3 to 1.4.6 — which words are called नदी.

    यू स्त्र्याख्यौ नदी: a form ending in ī or ū that denotes a woman. The
    Kāśikā is careful about what स्त्र्याख्य means — आख्याग्रहणं किम्?
    शब्दार्थे स्त्रीत्व एव यथा स्यात्, पदान्तराख्ये मा भूत् — the femininity
    must be the word's own meaning and not something a neighbouring word
    supplies, which is why ग्रामण्ये स्त्रियै does not make ग्रामणी a नदी.
    """
    last = antya(word)

    if before_ngit and last in _SHORT_IU and stri_akhya:
        return Named(
            "nadī", "1.4.6",
            "ङिति ह्रस्वश्च — and a short ि or ु before a ṅit affix, "
            "optionally.",
            optional=True,
        )

    if last not in _LONG_IU:
        return Named(
            None, "1.4.3",
            f"यू इति किम्? Only an ī- or ū-final; {word} is neither, as मात्रे "
            f"and दुहित्रे are not.",
        )

    if not stri_akhya:
        return Named(
            None, "1.4.3",
            "स्त्र्याख्याविति किम्? ग्रामणीः, सेनानीः, खलपूः — ī- and ū-final "
            "but not denoting a woman.",
        )

    if iyan_uvan_place and not is_stri:
        if before_am:
            return Named(
                "nadī", "1.4.5",
                "वाऽऽमि — before आम् the prohibition lapses and the name is "
                "optional again.",
                optional=True,
            )
        return Named(
            None, "1.4.4",
            "नेयङुवङ्स्थानावस्त्री — not where the ī or ū is the place of an "
            "इयङ् or उवङ् substitute: हे श्रीः, हे भ्रूः. अस्त्रीति किम्? "
            "हे स्त्रि, which keeps the name.",
            instead_of=("1.4.3",),
        )

    return Named(
        "nadī", "1.4.3",
        "यू स्त्र्याख्यौ नदी — कुमारी, गौरी, लक्ष्मीः; ब्रह्मबन्धूः, यवागूः.",
    )


def ghi(
    word: str,
    *,
    stri_akhya: bool = False,
    before_ngit: bool = False,
    in_compound: bool = False,
    chandas_with_genitive: bool = False,
) -> Named:
    """
    1.4.7 to 1.4.9 — which words are called घि.

    शेषो घ्यसखि, and the Kāśikā spells out what the remainder is: ह्रस्वम्
    इवर्णोवर्णान्तं यन् न स्त्र्याख्यम्, स्त्र्याख्यं च यन् न नदीसंज्ञकम्. Short
    ि- or ु-final and not denoting a woman, or denoting one but not reaching
    नदी. अग्नये, वायवे, कृतये, धेनवे.

    That second clause is where शेष meets 1.4.1: a short ि- or ु-final feminine
    ordinarily falls here, but 1.4.6 makes it नदी before a ṅit affix, and one
    name only may stand. So the exclusion is performed rather than assumed.
    """
    last = antya(word)

    if stri_akhya and before_ngit and last in _SHORT_IU:
        reached = nadi(word, stri_akhya=True, before_ngit=True)
        if reached.name:
            return Named(
                None, "1.4.7",
                "शेषः — the remainder, and this is not in it: 1.4.6 has already "
                "made it नदी before a ṅit affix, and 1.4.1 allows one name "
                "only. स्त्र्याख्यं च यन् न नदीसंज्ञकं स शेषः.",
                instead_of=("1.4.6",),
            )
    stem = word

    if stem == "sakhi":
        return Named(
            None, "1.4.7",
            "असखीति किम्? सख्या, सख्ये, सख्युः — सखि is excepted by name.",
        )

    if stem == "pati":
        if in_compound:
            return Named(
                "ghi", "1.4.8",
                "पतिः समास एव — पति takes the name only inside a compound.",
            )
        if chandas_with_genitive:
            return Named(
                "ghi", "1.4.9",
                "षष्ठीयुक्तश्छन्दसि वा — and in the Veda, construed with a "
                "genitive, optionally.",
                optional=True,
            )
        return Named(
            None, "1.4.8",
            "पतिः समास एव — outside a compound पति does not take it.",
        )

    if last not in _SHORT_IU:
        return Named(
            None, "1.4.7",
            f"ह्रस्वः carries down from 1.4.6, so the final must be a short "
            f"ि or ु; {word} ends otherwise.",
        )

    return Named(
        "ghi", "1.4.7",
        "शेषो घ्यसखि — the remainder after नदी: अग्नये, वायवे, कृतये, धेनवे.",
    )


# --- 1.4.10 to 1.4.12: लघु and गुरु ----------------------------------------

LAGHU, GURU = "laghu", "guru"


def weight(vowel: str, *, before_conjunct: bool = False) -> Named:
    """
    1.4.10 to 1.4.12 — whether a syllable is लघु or गुरु.

    Two of these reach the same syllable and 1.4.1 decides between them, which
    is the Kāśikā's own worked example while glossing that adhikāra: संयोगपरस्य
    ह्रस्वस्य लघुसंज्ञा प्राप्नोति गुरुसंज्ञा च। एका संज्ञेति वचनाद्
    गुरुसंज्ञैव भवति. So the resolution is performed by `eka_samjna` rather
    than written out here.
    """
    long_vowel = vowel not in ("a", "i", "u", "ṛ", "ḷ")

    if long_vowel:
        return Named(
            GURU, "1.4.12",
            "दीर्घं च — a long vowel is गुरु, and संयोगे does not carry down: "
            "सामान्येन संज्ञाविधानम्. ईहांचक्रे, ईक्षांचक्रे.",
        )

    if not before_conjunct:
        return Named(
            LAGHU, "1.4.10",
            "ह्रस्वं लघु — भेत्ता, छेत्ता, अचीकरत्, अजीहरत्. The ह्रस्व saṃjñā "
            "is 1.2.27's, already settled; this names what carries it.",
        )

    settled = eka_samjna([
        Rule("1.4.10", what=LAGHU),
        Rule("1.4.11", what=GURU),
    ])
    return Named(
        settled.winner.what, settled.winner.sutra,
        "संयोगे गुरु — both names reach a short vowel before a conjunct, and "
        "1.4.1 leaves one: " + settled.why + " कुण्डा, हुण्डा, शिक्षा, भिक्षा. "
        "The consequence the Kāśikā draws is that अततक्षत् and अररक्षत् do not "
        "get 7.4.93's सन्वद्भाव, which wants a लघु.",
        instead_of=settled.against,
    )


# --- 1.4.13: अङ्ग ----------------------------------------------------------


def anga(base: str, affix: str, *, prescribed_from: Optional[str] = None) -> Named:
    """
    1.4.13 यस्मात् प्रत्ययविधिस्तदादि प्रत्ययेऽङ्गम्.

    Whatever a suffix is prescribed after — तदादि, that and what follows it —
    is called अङ्ग before that suffix. The three words of the sūtra each earn
    a counter-example:

      प्रत्यय   न्यविशत, व्यक्रीणीत: 1.3.17 prescribes after an upasarga and
                not after a suffix, so नि does not begin an aṅga
      विधि     स्त्री इयती: a suffix merely *following* is not enough
      तदादि    the vārttika तदादिवचनं स्यादिनुमर्थम् — करिष्यावः, कुण्डानि
    """
    if prescribed_from is None:
        return Named(
            None, "1.4.13",
            "प्रत्ययविधि — the suffix must be prescribed after something. Where "
            "it merely follows, there is no aṅga: स्त्री इयती.",
        )
    if not affix:
        return Named(
            None, "1.4.13",
            "प्रत्यये — and a suffix must be there. लुप्तप्रत्यये मा भूत्: "
            "श्र्यर्थम्, भ्र्वर्थम्, where it has gone.",
        )
    return Named(
        base, "1.4.13",
        f"यस्मात् प्रत्ययविधिस्तदादि प्रत्ययेऽङ्गम् — {affix} is prescribed "
        f"after {prescribed_from}, so {prescribed_from} and what follows is "
        f"the aṅga: कर्ता, करिष्यति, औपगवः.",
    )


# --- 1.4.14 to 1.4.20: पद and भ -------------------------------------------

PADA, BHA = "pada", "bha"


def pada_or_bha(
    word: str,
    *,
    ends_in_sup_or_tin: bool = False,
    before_kya: bool = False,
    before_sit: bool = False,
    sup_affix: Optional[str] = None,
    sarvanamasthana: bool = False,
    matvartha: bool = False,
    ayasmayadi: bool = False,
    chandas: bool = False,
) -> Named:
    """
    1.4.14 to 1.4.20 — पद, and भ where it displaces पद.

    1.4.18 is an apavāda to 1.4.17 and the Kāśikā says so: पूर्वेण पदसंज्ञायां
    प्राप्तायां तदपवादो भसंज्ञा विधीयते. That is not a 1.4.2 case — an apavāda
    is not तुल्यबल — so the resolution is 1.4.1's एका संज्ञा, which the two
    sūtras stand under, and the later name stands.
    """
    if ayasmayadi and chandas:
        return Named(
            BHA, "1.4.20",
            "अयस्मयादीनि च्छन्दसि — in the Veda these take भ, optionally.\n\n"
            "The vārttika उभयसंज्ञान्यपि goes further and gives them *both* "
            "names, which under 1.4.1's एका संज्ञा should not be possible. "
            "Recorded rather than modelled.",
            optional=True,
        )

    if matvartha and antya(word) in ("t", "s"):
        return Named(
            BHA, "1.4.19",
            "तसौ मत्वर्थे — a त- or स-final before a matvartha suffix: "
            "उदश्वित्वान् घोषः, यशस्वी, पयस्वी. तसाविति किम्? तक्षवान् ग्रामः.",
        )

    if sup_affix and not sarvanamasthana:
        vowel_or_ya = begins_with(sup_affix, "aC") or sup_affix.startswith("y")
        if vowel_or_ya:
            settled = eka_samjna([
                Rule("1.4.17", what=PADA),
                Rule("1.4.18", what=BHA),
            ])
            return Named(
                settled.winner.what, settled.winner.sutra,
                "यचि भम् — before a य-initial or vowel-initial sup affix that "
                "is not सर्वनामस्थान: गार्ग्यः, वात्स्यः, दाक्षिः, प्लाक्षिः. "
                "पूर्वेण पदसंज्ञायां प्राप्तायां तदपवादो भसंज्ञा विधीयते, and "
                "1.4.1 leaves one name of the two.",
                instead_of=settled.against,
            )
        return Named(
            PADA, "1.4.17",
            "स्वादिष्वसर्वनामस्थाने — राजभ्याम्, राजभिः, राजत्वम्, राजतरः. "
            "असर्वनामस्थान इति किम्? राजानौ, राजानः.",
        )

    if before_kya:
        return Named(
            PADA, "1.4.15",
            "नः क्ये — a न-final before क्य.",
        )
    if before_sit:
        return Named(PADA, "1.4.16", "सिति च — and before a सित् affix.")

    if ends_in_sup_or_tin:
        return Named(
            PADA, "1.4.14",
            "सुप्तिङन्तं पदम् — सुप् and तिङ् are pratyāhāras, so this is "
            "whatever ends in a nominal or verbal ending: ब्राह्मणाः पठन्ति.\n\n"
            "The vārttika notes that the अन्त here bars 1.1.72's tadantavidhi "
            "elsewhere in saṃjñā rules — पदसंज्ञायाम् अन्तग्रहणम् अन्यत्र "
            "संज्ञाविधौ प्रत्ययग्रहणे तदन्तविधेः प्रतिषेधार्थम् — which is why "
            "गौरी ब्राह्मणितरा is not a pada.",
        )

    return Named(None, "—", "Nothing in 1.4.14–1.4.20 reaches this form.")


# --- 1.4.21 and 1.4.22: the three numbers ---------------------------------

EKAVACANA, DVIVACANA, BAHUVACANA = "ekavacana", "dvivacana", "bahuvacana"


def vacana(count: int) -> Named:
    """
    1.4.21 and 1.4.22 — which ending expresses how many.

    These do not prescribe the endings; 4.1.2 and 3.4.78 have already done
    that सामान्येन, in general. What these two add is the meaning: तस्यानेन
    बहुत्वसंख्या वाच्यत्वेन विधीयते, the number is what the ending is *for*.

    And it is the कारक's number and not the word's — कर्मादयोऽप्यपरे
    विभक्तीनाम् अर्था वाच्याः, तदीये बहुत्वे बहुवचनम्, which is why the plural
    of a verb answers to the plurality of its agent.
    """
    if count >= 3:
        return Named(
            BAHUVACANA, "1.4.21",
            "बहुषु बहुवचनम् — ब्राह्मणाः पठन्ति. यत्र च संख्या संभवति "
            "तत्रायम् उपदेशः: where number applies at all. An indeclinable has "
            "none, and takes its endings by the general rule regardless.",
        )
    if count == 2:
        return Named(DVIVACANA, "1.4.22",
                     "द्व्येकयोर्द्विवचनैकवचने — ब्राह्मणौ पठतः.")
    return Named(EKAVACANA, "1.4.22",
                 "द्व्येकयोर्द्विवचनैकवचने — ब्राह्मणः पठति.")


__all__ = [
    "BAHUVACANA",
    "BHA",
    "DVIVACANA",
    "EKAVACANA",
    "GURU",
    "LAGHU",
    "Named",
    "PADA",
    "anga",
    "ghi",
    "nadi",
    "pada_or_bha",
    "vacana",
    "weight",
]
