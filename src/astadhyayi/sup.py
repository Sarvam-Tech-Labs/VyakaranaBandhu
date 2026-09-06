# -*- coding: utf-8 -*-
"""
४.१.१–२ — the nominal base, and the twenty-one case-endings.

अध्याय ३ ended with the eighteen endings that replace a लकार and the
name तिङ् made from the last letter of the last of them. **अध्याय ४
opens by doing the same thing for nouns**, and the parallel is exact
enough to be worth stating plainly:

    3.4.78 gives eighteen endings ...  4.1.2 gives twenty-one
    ... and the ङ् of महिङ् exists   ... and the प् of सुप् exists
    so that तिङ् may be named,        so that सुप् may be named,
    प्रत्याहारग्रहणार्थम्             प्रत्याहारार्थम्

**And 4.1.2 does it twice.** औटष्टकारः सुडिति प्रत्याहारग्रहणार्थः —
the ट् on the fifth ending makes a SECOND name, सुट्, covering the
first five alone. One enumeration, two pratyāhāras cut out of it by
two silent letters, where 3.4.78 needed one.

4.1.1 ङ्याप्प्रातिपदिकात् is the अधिकार under which all of it stands,
and it runs **आ पञ्चमाध्यायपरिसमाप्तेः** — to the end of अध्याय ५.
That is the longest range any heading in this project has yet claimed:
3.2.84's भूते covered a pāda, 3.4.67's कर्तरि कृत् filled gaps in one,
and this one governs two whole chapters.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: 4.1.2's twenty-one, in the rule's own order: three numbers in each
#: of seven cases, read as the सूत्र spells them with their marks.
#: सु and औ and जस् for the first, and so to सुप् for the seventh.
SUP: Tuple[str, ...] = (
    "su", "au", "jas",
    "am", "auṭ", "śas",
    "ṭā", "bhyām", "bhis",
    "ṅe", "bhyām", "bhyas",
    "ṅasi", "bhyām", "bhyas",
    "ṅas", "os", "ām",
    "ṅi", "os", "sup",
)

#: The first five, which the ट् of औट् cuts out as सुट्. It is not an
#: arbitrary slice: 1.1.42's शि सर्वनामस्थानम् and the rules about a
#: strong stem all turn on it.
SUT: Tuple[str, ...] = SUP[:5]

#: What 4.1.1 governs. ङी covers ङीप्, ङीष् and ङीन् taken together —
#: ङीब्ङीष्ङीनां सामान्येन ग्रहणं ङीति — and आप् covers टाप्, डाप्
#: and चाप्: टाप्डाप्चापामाबिति. Two class-words and one name, given
#: as a समाहार.
NGI: Tuple[str, ...] = ("ṅīp", "ṅīṣ", "ṅīn")
AP: Tuple[str, ...] = ("ṭāp", "ḍāp", "cāp")


@dataclass(frozen=True)
class Governed:
    """What a heading covers, and how far."""

    covers: Tuple[str, ...]
    by: str
    why: str
    #: The sūtra the heading runs to, where the vṛtti states one.
    through: str = ""


@dataclass(frozen=True)
class Endings:
    """An enumeration, and the names cut out of it."""

    gives: Tuple[str, ...]
    by: str
    why: str
    name: str = ""


def nominal_base(*, ngi: bool = False, ap: bool = False,
                 pratipadika: bool = False) -> Governed:
    """
    4.1.1 ङ्याप्प्रातिपदिकात् — the base every affix of the next two
    chapters is added to.

    अधिकारोऽयम्, आ पञ्चमाध्यायपरिसमाप्तेः: it governs to the end of
    अध्याय ५, which is the longest range any heading in this project
    has claimed. स्वादिषु कप्पर्यन्तेषु प्रकृतिरधिक्रियते — from the
    case-endings to कप्, what is being governed is the BASE and not
    the affix.

    **The two class-words.** ङीब्ङीष्ङीनां सामान्येन ग्रहणं ङीति,
    टाप्डाप्चापामाबिति — ङी stands for three affixes and आप् for
    three others, and the three names are given as one compound.

    **And the vṛtti asks why they are named at all**, since
    प्रातिपदिकग्रहणे लिङ्गविशिष्टस्यापि ग्रहणं भवति (परि० ७१) would
    already bring a feminine stem under प्रातिपदिक. नैतदस्ति: that
    paribhāṣā holds only where the base is named AS ITSELF —
    स्वरूपविधिविषये परिभाषेयम् — and 2.1.67's युवा
    खलतिपलितवलिनजरतीभिः is the ज्ञापक for reading it so. There is a
    second reason as well: तदन्तात् तद्धितविधानार्थम्, so that a
    taddhita may come after a feminine stem — कालितरा, हरिणितरा,
    खट्वातरा, मालातरा — since विप्रतिषेधाद्धि तद्धितबलीयस्त्वं
    स्यात्.
    """
    # Nothing asked means the whole heading. Every one of the three
    # defaults to False so that "not asked" and "asked and answered
    # no" are not the same value — the fallback below could never fire
    # while `pratipadika` defaulted to True.
    covers = ()
    if pratipadika:
        covers += ("prātipadika",)
    if ngi:
        covers += NGI
    if ap:
        covers += AP
    return Governed(
        covers or ("prātipadika",) + NGI + AP, "4.1.1",
        "ङ्याप्प्रातिपदिकात् — अधिकारोऽयम्. यदित ऊर्ध्वमनुक्रमिष्याम "
        "आ पञ्चमाध्यायपरिसमाप्तेर्ङ्याप्प्रातिपदिकादित्येवं तद् "
        "वेदितव्यम्: everything from here to the END OF अध्याय ५ is "
        "added to one of these. स्वादिषु कप्पर्यन्तेषु प्रकृतिर् "
        "अधिक्रियते — what is governed is the base, not the affix.\n\n"
        "TWO CLASS-WORDS AND ONE NAME, GIVEN AS ONE COMPOUND. "
        "ङीब्ङीष्ङीनां सामान्येन ग्रहणं ङीति, टाप्डाप्चापामाबिति — "
        "ङी stands for the three ङी-affixes and आप् for the three "
        "आप्-affixes; प्रातिपदिक is 1.2.45 and 1.2.46's name. "
        "तेषां समाहारनिर्देशो ङ्याप्प्रातिपदिकादिति.\n\n"
        "AND THE VṚTTI ASKS WHY THE FEMININE STEMS ARE NAMED AT ALL. "
        "अथ ङ्याब्ग्रहणं किम्, न प्रातिपदिकग्रहणे "
        "लिङ्गविशिष्टस्यापि ग्रहणं भवति (परि० ७१) इत्येव सिद्धम्? "
        "नैतदस्ति — स्वरूपविधिविषये परिभाषेयम्, that principle holds "
        "only where the base is named as itself, and 2.1.67's युवा "
        "खलतिपलितवलिनजरतीभिः is the ज्ञापक for reading it so. There "
        "is a second reason: तदन्तात् तद्धितविधानार्थम् — कालितरा, "
        "हरिणितरा, खट्वातरा, मालातरा — since otherwise "
        "विप्रतिषेधाद्धि तद्धितबलीयस्त्वं स्यात्",
        through="5.4.160")


def sup_endings(*, name: str = "") -> Endings:
    """
    4.1.2 स्वौजसमौट्छष्टाभ्याम्भिस्ङेभ्याम्भ्यस्ङसिभ्याम्भ्यस्-
    ङसोसाम्ङ्योस्सुप् — the twenty-one case-endings.

    The nominal counterpart of 3.4.78, and built the same way: an
    enumeration whose silent letters make the names the rest of the
    grammar uses. उकारादयोऽनुबन्धा यथायोगमुच्चारणविशेषणार्थाः.

    **Two pratyāhāras out of one list.** औटष्टकारः सुडिति
    प्रत्याहारग्रहणार्थः — the ट् on the fifth makes सुट्, the first
    five taken together. पकारः सुबिति प्रत्याहारार्थः — the प् on
    the twenty-first makes सुप्, the whole. 3.4.78 spent its last
    letter on one name; this rule spends two letters on two.

    **And the senses come from outside.** संख्याकर्मादयश्च स्वादीनाम्
    अर्थाः शास्त्रान्तरेण विहिताः, तेन सहास्यैकवाक्यता — number is
    given by 1.4.21-22 and the kāraka by 2.3, and this rule and those
    are read as ONE SENTENCE. The endings are enumerated here and
    given their meanings elsewhere, which is the reverse of how the
    कृत् affixes were handled: those were given IN a sense.

    `name` asks for one of the two pratyāhāras rather than the list.
    """
    if name == "suṭ":
        return Endings(
            SUT, "4.1.2",
            "सुट् — the first five of the twenty-one, cut out by the "
            "ट् of औट्: औटष्टकारः सुडिति प्रत्याहारग्रहणार्थः. "
            "The slice is not arbitrary — the rules about a strong "
            "stem turn on exactly these",
            name="suṭ")
    if name and name != "sup":
        return Endings(
            (), "4.1.2",
            "%s is not a name this rule makes. It cuts out two: सुट्, "
            "the first five, and सुप्, all twenty-one" % name)
    return Endings(
        SUP, "4.1.2",
        "स्वौजसमौट्छष्टाभ्याम्भिस्ङेभ्याम्भ्यस्ङसिभ्याम्भ्यस्"
        "ङसोसाम्ङ्योस्सुप् — TWENTY-ONE ENDINGS, three numbers in "
        "each of seven cases: कुमारी, कुमार्यौ, कुमार्यः and so "
        "through, दृषद्, दृषदौ, दृषदः for a bare stem.\n\n"
        "TWO NAMES CUT OUT OF ONE LIST BY TWO SILENT LETTERS. "
        "औटष्टकारः सुडिति प्रत्याहारग्रहणार्थः — the ट् of the fifth "
        "makes सुट्; पकारः सुबिति प्रत्याहारार्थः — the प् of the "
        "twenty-first makes सुप्. 3.4.78 spent the last letter of its "
        "last ending on ONE name, तिङ्; this rule spends two letters "
        "on two, and the rest — उकारादयोऽनुबन्धा — are only there to "
        "make the list sayable.\n\n"
        "AND THE SENSES ARE NOT GIVEN HERE. संख्याकर्मादयश्च "
        "स्वादीनामर्थाः शास्त्रान्तरेण विहिताः, तेन सहास्यैकवाक्यता "
        "— number comes from 1.4.21 and the kāraka from अध्याय २, and "
        "this rule is read as ONE SENTENCE with those. The endings "
        "are enumerated in one place and given their meanings in "
        "another, which is the reverse of the कृत् affixes: those "
        "were each given IN a sense and 3.4.67 had to supply one only "
        "where a rule had not",
        name="sup")
