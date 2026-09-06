# -*- coding: utf-8 -*-
"""
The first operational rules — what it takes to derive one word.

    3.1.68  कर्तरि शप्              the a that comes between root and ending
    3.4.113 तिङ्शित्सार्वधातुकम्   and what makes that a sārvadhātuka
    7.3.84  सार्वधातुकार्धधातुकयोः guṇa of an ik-final stem before one
    6.1.78  एचोऽयवायावः            and e, o, ai, au before a vowel
    7.2.114 मृजेर्वृद्धिः          vṛddhi of मृज्, the other worked example

These were chosen by working backwards from a single word. जयति needs exactly
these five and the interpretive rules already codified, and nothing else —
which is a better way to pick the next sūtras than going down the list,
because the result is checkable against a derivation any grammarian can
confirm rather than against our own worked examples.

What they lean on was already here:

  * **1.1.3 इको गुणवृद्धी** decides *which* vowel guṇa lands on. 7.3.84 says
    गुणः and names no target; the Kāśikā fills it in as इगन्तस्य अङ्गस्य,
    which is 1.1.3's ik.
  * **1.1.50 स्थानेऽन्तरतमः** decides which guṇa vowel. Nothing among अ, ए,
    ओ is identical to इ — ए is कण्ठतालव्य and इ is तालव्य — so the rule picks
    the nearest, and ए wins by sharing the palatal place. "Closest", not
    "same", is the whole reason the sūtra exists.
  * **1.1.51 उरण् रपरः** adds the र् after ऋ's substitute, so वृद्धि of ऋ
    comes out ār in two steps rather than one.
  * **1.3.10 यथासंख्यम्** pairs 6.1.78's four with its four, in order.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Tuple

from src.astadhyayi.adesa import antaratama, antya, raparatva
from src.astadhyayi.reading import yathasamkhya


def _from_1_1_1():
    """
    1.1.1's and 1.1.2's sets, and 1.1.3's test, fetched when wanted.

    Imported inside the function rather than at the top because the pāda
    modules import *this* one to register their sūtras: a module-level
    import here and the rules package cannot finish loading. The rule that
    supplies the vowels is codified in the same place as the rule that
    prescribes them, and that is the right arrangement — it just cannot be
    a module-level import in both directions.
    """
    from src.astadhyayi.rules.adhyaya_1_pada_1 import (
        GUNA, VRDDHI, guna_vrddhi_target)

    return GUNA, VRDDHI, guna_vrddhi_target


# ---------------------------------------------------------------------------
# 3.4.113 तिङ्शित्सार्वधातुकम्
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Name:
    holds: bool
    by: str
    why: str


def sarvadhatuka(*, tin: bool = False, sit: bool = False) -> Name:
    """
    3.4.113: a तिङ् ending, and a शित् affix, are called सार्वधातुक.

    तिङः शितश्च प्रत्ययाः सार्वधातुकसंज्ञा भवन्ति. It is worth codifying
    for one reason: it is what makes शप् sārvadhātuka, and 7.3.84 will not
    fire without that. शप् is शित् — its श् is an it by 1.3.8 — so the name
    reaches it through the very letter that 1.3.9 then removes.
    """
    if tin:
        return Name(True, "3.4.113",
                    "तिङ्शित्सार्वधातुकम् — a तिङ् ending: भवति, नयति")
    if sit:
        return Name(True, "3.4.113",
                    "तिङ्शित्सार्वधातुकम् — a शित् affix, which is how शप् "
                    "comes by the name: पवमानः, यजमानः")
    return Name(False, "3.4.113",
                "neither तिङ् nor शित्, so not सार्वधातुक by this sūtra")


# ---------------------------------------------------------------------------
# 3.4.114 आर्धधातुकं शेषः, and the three that qualify it
# ---------------------------------------------------------------------------


def ardhadhatuka(*, tin: bool = False, sit: bool = False,
                 lakara: str = "", sense: str = "",
                 chandasi: bool = False,
                 after_a_root: bool = True) -> Name:
    """
    3.4.114 आर्धधातुकं शेषः — every other affix given after a root.

    तिङः शितश्च वर्जयित्वान्यः प्रत्ययः शेषो धातुसंशब्दनेन विहित
    आर्धधातुकसंज्ञो भवति. लविता, लवितुम्, लवितव्यम्.

    **The rule is defined by subtraction, so the code subtracts.** शेषः
    means *the remainder*, and there is only one thing it is the
    remainder OF: 3.4.113's तिङ् and शित्. So this asks that rule first
    and takes the name it did not give — which is why `sarvadhatuka`
    is called here rather than its two conditions being tested again.

    धातोरित्येव holds it to affixes given AFTER A ROOT, and the vṛtti
    marks the boundary with four forms that are not: वृक्षत्वम्,
    वृक्षतास्ति — त्व and तल् come after a nominal; लूभ्याम्, लूभिः —
    case-endings come after a stem, though the stem is लू; and
    जुगुप्सते, where सन् comes after a root but is given by 3.1.5 to
    make one, not after one.

    Three rules then qualify it, and all three turn on a single
    syllable borrowed from 3.4.111:

    3.4.115 लिट् च and 3.4.116 लिङाशिषि are अपवाद — a perfect ending,
    and a benedictive, are आर्धधातुक though they are तिङ् and so
    already सार्वधातुक by 3.4.113. **Normally both names would hold at
    once**: ननु चैकसंज्ञाधिकारादन्यत्र समावेशो भवति? सत्यमेतत् — the
    one-name-only heading is elsewhere, so two names may co-apply.
    इह त्वेवकारोऽनुवर्तते, स नियमं करिष्यति: the एव carried down from
    3.4.111 restricts it, and one name REPLACES the other. That एव was
    put in 3.4.111 for exactly this, उत्तरार्थः, four sūtras before it
    is used.

    3.4.117 छन्दसि उभयथा then lets both names hold together after all,
    in the Veda. And it is not read as attaching to the nearest rule
    only: किं लिङेवानन्तरः संबध्यते? नैतदस्ति, सर्वमेव प्रकरणमपेक्ष्य
    — it reaches the whole section. वर्धन्तु त्वा सुष्टुतयः takes
    ārdhadhātuka's णिलोप where वर्धयन्तु was due; नावमिवारुहेम keeps
    the sārvadhātuka; ससवांसो विशृण्विरे makes a perfect
    sārvadhātuka against 3.4.115; and उप स्थेयाम शरणा बृहन्त takes
    both at once — सार्वधातुकत्वाल् लिङः सलोपः, आर्धधातुकत्वादेत्वम्,
    one form drawing one operation from each name. The vṛtti closes
    the pāda by saying what that amounts to: व्यत्ययो बहुलम्
    इत्यस्यैवायं प्रपञ्चः, it is 3.1.85 spelled out.
    """
    if not after_a_root:
        return Name(False, "3.4.114",
                    "धातोरित्येव — the affix is not given after a "
                    "root, so neither name is in question: वृक्षत्वम्, "
                    "वृक्षतास्ति, लूभ्याम्, लूभिः")
    if chandasi and (tin or sit):
        return Name(True, "3.4.117",
                    "छन्दसि उभयथा — in the Veda an affix is BOTH, "
                    "and the vṛtti reads the rule as reaching the "
                    "whole section and not the nearest sūtra alone: "
                    "सर्वमेव प्रकरणमपेक्ष्यैतदुच्यते. उप स्थेयाम "
                    "शरणा बृहन्त takes one operation from each name — "
                    "सार्वधातुकत्वाल् लिङः सलोपः, "
                    "आर्धधातुकत्वादेत्वम्")
    if lakara == "liṭ":
        return Name(True, "3.4.115",
                    "लिट् च — a perfect ending is आर्धधातुक though "
                    "3.4.113 has already called it सार्वधातुक: "
                    "पेचिथ, शेकिथ, जग्ले, मम्ले. The two names would "
                    "normally co-apply — एकसंज्ञाधिकारादन्यत्र "
                    "समावेशो भवति — and what stops them is the एव "
                    "carried down from 3.4.111, four sūtras back, "
                    "which was put there उत्तरार्थः")
    if lakara == "liṅ" and sense == "āśis":
        return Name(True, "3.4.116",
                    "लिङाशिषि — a benedictive is आर्धधातुक: "
                    "लविषीष्ट, पविषीष्ट. आशिषीति किम्? लुनीयात्, "
                    "पुनीयात् keep the other name. Again "
                    "सार्वधातुकसंज्ञाया अपवादः, and again "
                    "समावेशश्चैवकारानुवृत्तेर्न भवति")
    already = sarvadhatuka(tin=tin, sit=sit)
    if already.holds:
        return Name(False, "3.4.114",
                    "शेषः — the remainder. 3.4.113 has already named "
                    "this one: %s. What that rule takes, this rule "
                    "does not" % already.why)
    return Name(True, "3.4.114",
                "आर्धधातुकं शेषः — neither तिङ् nor शित्, so it falls "
                "to the remainder: लविता, लवितुम्, लवितव्यम्")


# ---------------------------------------------------------------------------
# 3.1.68 कर्तरि शप्
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Affix:
    added: Optional[str]
    by: str
    why: str


def sap(*, kartari: bool = True, sarvadhatuka_follows: bool = True) -> Affix:
    """
    3.1.68: शप् comes after a root, before a sārvadhātuka denoting the agent.

    कर्तृवाचिनि सार्वधातुके परतो धातोः शप् प्रत्ययो भवति. Both of its
    letters are indicatory and both are there for a reason the Kāśikā
    states: पकारः स्वरार्थः, शकारः सार्वधातुकसंज्ञार्थः — the प् for accent,
    the श् to bring 3.4.113's name. What survives 1.3.9 is a bare अ, and
    that अ is the one in भवति and पचति.
    """
    if not sarvadhatuka_follows:
        return Affix(None, "3.1.68",
                     "सार्वधातुके — no sārvadhātuka follows, so no शप्")
    if not kartari:
        return Affix(None, "3.1.68",
                     "कर्तरि — the affix does not denote the agent. In the "
                     "passive 3.1.67 gives यक् instead: क्रियते कटः")
    return Affix("śap", "3.1.68",
                 "कर्तरि शप् — शप् after the root: भवति, पचति")


# ---------------------------------------------------------------------------
# 7.3.84 सार्वधातुकार्धधातुकयोः,  7.2.114 मृजेर्वृद्धिः
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Strengthened:
    """A stem after guṇa or vṛddhi, with the rules that decided each part."""

    result: Optional[str]
    by: str
    why: str
    #: 1.1.3 chose the vowel, 1.1.50 chose its replacement, 1.1.51 may have
    #: added the र्. Named because none of them is 7.3.84's own doing.
    through: Tuple[str, ...] = ()


def _as_affix(affix):
    """
    An affix as an `Adesa`, whichever way the caller wrote it.

    A caller — or a form on the playground — naturally writes the affix as
    क्त्वा rather than building an Adesa with its it-letters listed. Which
    letters those are is 1.3.2–1.3.8's business, so it is asked rather than
    demanded of the caller.
    """
    if not isinstance(affix, str):
        return affix
    from src.astadhyayi.adesa import Adesa
    from src.astadhyayi.itsamjna import PRATYAYA, analyze

    return (Adesa(form=affix, its=analyze(affix, PRATYAYA).it_letters)
            if affix else None)


def _substitute_at(stem: str, position: int, among, sutra: str, why: str,
                   affix=None, ardhadhatuka: bool = False,
                   dhatu_lopa: bool = False, item: str = "",
                   restrict_to_ik: bool = True,
                   length: int = 1) -> Strengthened:
    """
    One vowel of a stem replaced by its guṇa or vṛddhi, if nothing stops it.

    The three prohibitions come first. 1.1.4, 1.1.5 and 1.1.6 exist to stop
    guṇa and vṛddhi and nothing else, and they are as much a part of what
    the operation is as the rule prescribing it: without them 7.3.84 turns
    भू before क्त्वा into भो, and भोत्वा is not a word.

    Which vowel is the caller's business, because the sūtras differ on it —
    7.3.84 takes the इगन्त, 7.3.86 the लघु उपधा, 7.2.114 the इक् of one
    named root. Only what happens once the vowel is chosen is shared.
    """
    from src.astadhyayi.rules.adhyaya_1_pada_1 import (
        guna_vrddhi_blocked, is_ik)

    # A vowel is not always one character. ऐ and औ are two, and reading
    # only the first gave 7.2.115 the अ of जै, then a vṛddhi on that, and
    # then another: जि came out जाााा… until this took the sound and not
    # the letter. `scan_phonemes` is what says where a sound ends.
    vowel = stem[position:position + length]
    # 1.1.3 इको गुणवृद्धी — and nothing else. Without this the substitution
    # was asked for अ, whose nearest guṇa by 1.1.50 is अ itself: the rule
    # "applied", changed nothing, and the derivation stopped there.
    #
    # But 1.1.3 holds only where the sūtra has NOT named its own स्थानी.
    # 7.2.115 says अचः and 7.2.116 says अतः, and a rule that names what it
    # replaces is not asking 1.1.3 to find it one.
    if restrict_to_ik and not is_ik(vowel):
        return Strengthened(
            None, sutra,
            f"इको गुणवृद्धी — {vowel} is not an इक्, so 1.1.3 allows no "
            f"substitution here")
    stopped = guna_vrddhi_blocked(
        vowel, affix=_as_affix(affix), ardhadhatuka=ardhadhatuka,
        dhatu_lopa=dhatu_lopa, item=item or stem)
    if stopped is not None:
        return Strengthened(None, stopped.by, stopped.why)
    if vowel in among:
        # The substitution has already been made. A rule prescribing
        # वृद्धि where वृद्धि stands does nothing, and an engine that
        # applies it again applies it for ever.
        return Strengthened(
            None, sutra,
            f"{vowel} is already one of the substitutes this rule "
            f"prescribes, so there is nothing left for it to do")
    nearest = antaratama(vowel, among)
    if not nearest:
        return Strengthened(None, sutra,
                            f"{vowel} has no substitute among the class")
    substitute = nearest[0]
    through = ["1.1.3", "1.1.50"]
    # 1.1.51 उरण् रपरः — ऋ's substitute takes a र् after it.
    expanded = raparatva(vowel, substitute)
    if expanded != substitute:
        through.append("1.1.51")
    return Strengthened(
        stem[:position] + expanded + stem[position + length:],
        sutra, why, tuple(through),
    )


def _strengthen(stem: str, among, sutra: str, why: str,
                affix=None, ardhadhatuka: bool = False,
                dhatu_lopa: bool = False, item: str = "") -> Strengthened:
    """The last इक् of the stem, strengthened — 7.2.114's reading."""
    _guna, _vrddhi, is_target = _from_1_1_1()
    for position in range(len(stem) - 1, -1, -1):
        if not is_target(stem[position]):
            continue
        return _substitute_at(stem, position, among, sutra, why,
                              affix=affix, ardhadhatuka=ardhadhatuka,
                              dhatu_lopa=dhatu_lopa, item=item)
    return Strengthened(None, sutra,
                        f"{stem} has no इक् for the substitution to land on — "
                        f"1.1.3 इको गुणवृद्धी allows no other place")


def guna_before_affix(
    stem: str, *, sarvadhatuka: bool = False, ardhadhatuka: bool = False,
    affix=None, dhatu_lopa: bool = False, elided_final: bool = False
) -> Strengthened:
    """
    7.3.84: guṇa of an ik-final stem before a sārvadhātuka or ārdhadhātuka.

    सार्वधातुक आर्धधातुके च प्रत्यये परत इगन्तस्याङ्गस्य गुणो भवति —
    तरति, नयति, भवति; and for the ārdhadhātuka, कर्ता, चेता, स्तोता.

    The Kāśikā's सार्वधातुकार्धधातुकयोरिति किम् is the condition, and the
    answer says what would go wrong without it: अग्नित्वम्, अग्निकाम्यति —
    the affix there is neither, and अग्नि keeps its इ.

    Only the word गुणः is read down from 7.3.82; that sūtra is मिदेर्गुणः
    and its own scope is the root मिद्. The general application is this
    sūtra's.
    """
    if not (sarvadhatuka or ardhadhatuka):
        return Strengthened(
            None, "7.3.84",
            "सार्वधातुकार्धधातुकयोः इति किम्? — the affix is neither, so no "
            "guṇa: अग्नित्वम्, अग्निकाम्यति")
    # इगन्तस्य — the sūtra says the aṅga must END in the इक्, and the
    # scan used to take the last इक् wherever it stood. निन्द् has an इ
    # two sounds from the end and came out नेन्दति; बुध् has one and came
    # out बोधति, which is right but by the wrong rule — a light penult
    # is 7.3.86's business and not this one.
    sounds = _sounds_of(stem)
    if not sounds or sounds[-1].kind != "vowel":
        return Strengthened(
            None, "7.3.84",
            f"इगन्तस्य — {stem} does not end in an इक्, so 7.3.84 does not "
            f"reach it. 7.3.86 पुगन्तलघूपधस्य च is the rule for a light "
            f"penult: भेदनम्, छेत्ता")
    return _substitute_at(
        stem, sounds[-1].start, _from_1_1_1()[0], "7.3.84",
        "सार्वधातुकार्धधातुकयोः — guṇa of the इगन्त अङ्ग before it",
        affix=affix, ardhadhatuka=ardhadhatuka, dhatu_lopa=dhatu_lopa,
        length=len(sounds[-1].text))


def _sounds_of(text: str):
    """
    The sounds of a form, aspirates kept whole.

    `scan_phonemes` is the codification's one splitter — `itsamjna` reads a
    root's it-letters with it — so 1.1.65's उपधा and 7.3.84's अन्त are read
    off the same division of the word as everything else.
    """
    from src.chandas.core import scan_phonemes

    return scan_phonemes(text) if text else []


def upadha(stem: str) -> Tuple[int, str]:
    """
    1.1.65 अलोऽन्त्यात् पूर्व उपधा — the sound before the last, and where.

    अन्त्यादलः पूर्वो वर्ण उपधासंज्ञो भवति. Returns (-1, "") where there is
    no such sound — a form of one letter has no penult.
    """
    sounds = _sounds_of(stem)
    if len(sounds) < 2:
        return -1, ""
    return sounds[-2].start, sounds[-2].text


#: 1.4.10 ह्रस्वं लघु — the short vowels, which are what a लघु उपधा must
#: be. 1.1.3 इको गुणवृद्धी narrows it further: only an इक् can be
#: strengthened, so अ is short but never a target.
LAGHU_IK: Tuple[str, ...] = ("i", "u", "ṛ", "ḷ")


def pugantalaghupadhasya(
    stem: str, *, sarvadhatuka: bool = False, ardhadhatuka: bool = False,
    affix=None, dhatu_lopa: bool = False, elided_final: bool = False
) -> Strengthened:
    """
    7.3.86 पुगन्तलघूपधस्य च — guṇa of a stem whose penult is light.

    पुगन्तस्य लघूपधस्य च अङ्गस्य गुणो भवति सार्वधातुकार्धधातुकयोः परतः:
    **भेदनम्, छेत्ता** from भिद् and छिद्, **बोधति** from बुध्, **कर्षति**
    from कृष्. It is 7.3.84 widened — that rule reaches only an aṅga that
    ENDS in the इक्, and most roots do not.

    Two conditions, and both fall out of 1.1.65's उपधा rather than being
    tested for:

      * the उपधा must be a vowel at all. निन्द् (nind) has न् for its
        penult, so the rule never reaches its इ — निन्दति, and not
        *नेन्दति, which is what a scan for "the last इक् anywhere" gave.
      * it must be **लघु** by 1.4.10 ह्रस्वं लघु. जीव् (jīv) has a long
        ई and keeps it — जीवति, not *जेवति. The संयोग of 1.4.11 is
        judged inside the aṅga, which is why छेत्ता has its guṇa though
        the द् and the त् of तृच् make one: the Kāśikā's own example.

    **पुगन्त is named and not modelled.** The पुक् augment is 7.3.36's,
    which is codified but not built, so a stem does not arrive here with
    one. The other half of the sūtra is what every class of the
    dhātupāṭha needs.
    """
    if not (sarvadhatuka or ardhadhatuka):
        return Strengthened(
            None, "7.3.86",
            "सार्वधातुकार्धधातुकयोः is read down from 7.3.84 — the affix is "
            "neither, so no guṇa")
    if elided_final:
        return _upadha_hidden_by_lopa("7.3.86")
    position, sound = upadha(stem)
    if sound not in LAGHU_IK:
        return Strengthened(
            None, "7.3.86",
            f"लघूपधस्य — the उपधा of {stem} is "
            f"{sound or 'nothing'}, which is not a light इक्: निन्दति, "
            f"जीवति")
    return _substitute_at(
        stem, position, _from_1_1_1()[0], "7.3.86",
        "पुगन्तलघूपधस्य च — guṇa of the light penult: भेदनम्, छेत्ता",
        affix=affix, ardhadhatuka=ardhadhatuka, dhatu_lopa=dhatu_lopa)


@dataclass(frozen=True)
class Dropped:
    """A stem after a sound has been elided, and by which rule."""

    result: Optional[str]
    by: str
    why: str
    #: Whether what went was part of the ROOT. 1.1.4 न धातुलोप आर्धधातुके
    #: turns on exactly that, and nothing downstream can work it out.
    dhatu_lopa: bool = False


def ato_lopah(stem: str, *, ardhadhatuka: bool = True) -> Dropped:
    """
    6.4.48 अतो लोपः — an अ-final aṅga loses its अ before an ārdhadhātuka.

    अकारान्तस्य आर्धधातुके लोपो भवति: **चिकीर्षिता, चिकीर्षितुम्,
    चिकीर्षितव्यम्; धिनुतः, कृणुतः**.

    **अत इति किम्?** चेता, स्तोता — the aṅga ends in another vowel.
    **तपरकरणं किम्?** याता, वाता — a long आ, which the तपर shuts out.
    **आर्धधातुक इति किम्?** वृक्षत्वम्, वृक्षता.

    **AND IT IS DONE THOUGH TWO LATER RULES REACH THE SAME अ.** The
    Kāśikā ends the entry with **वृद्धिदीर्घाभ्यामतो लोपः
    पूर्वविप्रतिषेधेन** — 7.2.115's vṛddhi and 7.3.101's lengthening are
    both later, and 1.4.2 विप्रतिषेधे परं कार्यम् would give them the
    place; the tradition says of this pair that the earlier is done.
    चिकीर्षकः, जिहीर्षकः.

    That is why कथ (katha) gives कथयति and not *काथयति: the अ goes
    first, and 1.1.4 न धातुलोप आर्धधातुके then keeps 7.2.116's vṛddhi off
    the अ that is left, the root having lost a part of itself to the very
    affix that would have caused it.
    """
    if not ardhadhatuka:
        return Dropped(None, "6.4.48",
                       "आर्धधातुक इति किम्? — वृक्षत्वम्, वृक्षता")
    if not stem.endswith("a"):
        return Dropped(None, "6.4.48",
                       f"अत इति किम्? — {stem} does not end in a short अ: "
                       f"चेता, स्तोता, याता")
    return Dropped(stem[:-1], "6.4.48",
                   "अतो लोपः — the अ goes before the ārdhadhātuka: "
                   "चिकीर्षिता, धिनुतः", dhatu_lopa=True)


def _upadha_hidden_by_lopa(sutra: str) -> Strengthened:
    """
    1.1.57 अचः परस्मिन् पूर्वविधौ — an elided vowel still counts as there.

    A rule about the **उपधा** looks leftward, and 1.1.57 makes a vowel
    elided by what follows स्थानिवत् for exactly such a rule. So after
    6.4.48 has taken the अ off कथ (katha), the थ् has not become the
    penult: the अ that went is still standing for the purpose, and
    7.2.116 अत उपधायाः finds no अ to lengthen. **कथयति, गणयति,
    रचयति** — not काथयति.

    The codification of 1.1.57 names this very case in its own note,
    पटयति, so the verdict is asked of it rather than assumed.
    """
    from src.astadhyayi.sthanivat import sthanivat

    verdict = sthanivat(al_vidhi=True, sthanin_is_vowel=True,
                        caused_by_following=True, purva_vidhi=True)
    return Strengthened(None, sutra, f"{verdict.by} {verdict.why}")


def aco_nniti(stem: str, *, affix=None, dhatu_lopa: bool = False,
              elided_final: bool = False) -> Strengthened:
    """
    7.2.115 अचो ञ्णिति — vṛddhi of a root's final vowel before a ञित् or णित्.

    अजन्तस्याङ्गस्य ञिति णिति च प्रत्यये परतो वृद्धिर्भवति: **चेता, चायकः;
    लविता, लावकः**. The affix णिच् is णित्, which is what makes a
    vowel-final root of the tenth class lengthen before it.

    **अचः is a स्थानिनिर्देश**, so 1.1.3's इक् does not narrow it — the
    rule has named what it replaces.
    """
    sounds = _sounds_of(stem)
    if not sounds or sounds[-1].kind != "vowel":
        return Strengthened(
            None, "7.2.115",
            f"अचः — {stem} does not end in a vowel, so 7.2.116 "
            f"अत उपधायाः is the rule to ask: पाठयति")
    return _substitute_at(
        stem, sounds[-1].start, _from_1_1_1()[1], "7.2.115",
        "अचो ञ्णिति — vṛddhi of the final vowel: चेता, लाविता",
        affix=affix, ardhadhatuka=True, restrict_to_ik=False,
        dhatu_lopa=dhatu_lopa, length=len(sounds[-1].text))


def ato_upadhayah(stem: str, *, affix=None, dhatu_lopa: bool = False,
                  elided_final: bool = False) -> Strengthened:
    """
    7.2.116 अत उपधायाः — and vṛddhi of an अ standing as the penult.

    अकारस्य उपधाभूतस्य वृद्धिर्भवति ञिति णिति च: **पाठयति, पाचयति**. It
    is 7.2.115's other half — that rule takes the final vowel, this one
    the penult, and between them every root the causative reaches.

    **अत इति किम्?** भेदयति — the penult is not अ, and 7.3.86's guṇa is
    what acts there instead. **उपधाया इति किम्?** कारयति — the अ of कृ's
    guṇa is not a penult, having been made by another rule.
    """
    if elided_final:
        return _upadha_hidden_by_lopa("7.2.116")
    position, sound = upadha(stem)
    if sound != "a":
        return Strengthened(
            None, "7.2.116",
            f"अत इति किम्? — the उपधा of {stem} is {sound or 'nothing'} "
            f"and not अ: भेदयति")
    return _substitute_at(
        stem, position, _from_1_1_1()[1], "7.2.116",
        "अत उपधायाः — vṛddhi of the penult अ: पाठयति, पाचयति",
        affix=affix, ardhadhatuka=True, restrict_to_ik=False,
        dhatu_lopa=dhatu_lopa)


def sino_guna(stem: str, *, sarvadhatuka: bool = False,
              enunciated: str = "") -> Strengthened:
    """
    7.4.21 शीङः सार्वधातुके गुणः — one root, guṇa, and no exceptions.

    शीङः अङ्गस्य सार्वधातुके परतः गुणो भवति: **शेते, शयाते, शेरते**.
    **सार्वधातुक इति किम्?** शिश्ये.

    The rule exists because 7.3.84 cannot do the work. शीङ् is ङित् and
    takes the middle endings by 1.3.12, every one of them अपित्; 1.2.4
    सार्वधातुकमपित् makes them ङिद्वत् and 1.1.5 क्ङिति च then keeps guṇa
    off — so 7.3.84 gives शीते, and the word is शेते. A rule that names
    one root and one condition, put there to override a prohibition.

    The root is recognised by its **enunciation**: शीङ् and not शी, the
    ङ् being the whole reason the endings are middle and the reason the
    prohibition had to be overridden.
    """
    if not sarvadhatuka:
        return Strengthened(None, "7.4.21",
                            "सार्वधातुक इति किम्? — शिश्ये")
    if (enunciated or stem) not in ("śīṅ", "śī"):
        return Strengthened(None, "7.4.21",
                            f"शीङः — the root is {enunciated or stem}, "
                            f"not शीङ्")
    # 1.1.5 is deliberately not asked. This rule is why शेते exists.
    return _substitute_at(
        stem, len(stem) - 1, _from_1_1_1()[0], "7.4.21",
        "शीङः सार्वधातुके गुणः — शेते, शयाते, शेरते")


def mrjer_vrddhi(stem: str, *, dhatu: bool = True, affix=None,
                 ardhadhatuka: bool = True,
                 dhatu_lopa: bool = False) -> Strengthened:
    """
    7.2.114: vṛddhi of the ik of मृज्.

    मृजेरङ्गस्येको वृद्धिर्भवति — मार्ष्टा, मार्ष्टुम्, मार्ष्टव्यम्. The
    Kāśikā adds the limit: मृजेरिति धातुग्रहणमिदम्, धातोश्च कार्यम्
    उच्यमानं धातुप्रत्यय एव वेदितव्यम् — the rule names a *root*, so it
    reaches only what is built on the root as a root. कंसपरिमृड्भ्याम्, a
    noun, is untouched.
    """
    if stem not in ("mṛj", "mṛjū"):
        return Strengthened(None, "7.2.114",
                            f"मृजेः — the sūtra names मृज् and this is "
                            f"{stem}")
    if not dhatu:
        return Strengthened(
            None, "7.2.114",
            "धातुग्रहणमिदम् — मृज् is named as a root, so a noun built on it "
            "is outside: कंसपरिमृड्भ्याम्, कंसपरिमृड्भिः")
    return _strengthen(stem, _from_1_1_1()[1], "7.2.114",
                       "मृजेर्वृद्धिः — vṛddhi of the इक् of मृज्",
                       affix=affix, ardhadhatuka=ardhadhatuka,
                       dhatu_lopa=dhatu_lopa)


# ---------------------------------------------------------------------------
# 6.1.78 एचोऽयवायावः
# ---------------------------------------------------------------------------


def ec() -> Tuple[str, ...]:
    """
    6.1.78's एच्, obtained from the śivasūtras rather than listed.

    The sūtra does not name four sounds; it names a pratyāhāra, and what
    that abbreviation stands for is 1.1.71 आदिरन्त्येन सहेता's business.
    Writing ("e", "o", "ai", "au") here would have been a second definition
    of something the codification already derives — and it was, until an
    audit for duplicated definitions across the package turned up exactly
    two, of which this was the real one.
    """
    from src.astadhyayi.sivasutra import resolve

    return resolve("eC").sounds


#: The four substitutes. These *are* written out, because the sūtra writes
#: them out — अय् अव् आय् आव् is a list, not an abbreviation. 1.3.10 pairs
#: them with what ec() returns.
AYAV: Tuple[str, ...] = ("ay", "av", "āy", "āv")


@dataclass(frozen=True)
class Ayadi:
    result: Optional[str]
    by: str
    why: str


def ayadi(stem: str, *, before_vowel: bool = True) -> Ayadi:
    """
    6.1.78: ए, ओ, ऐ, औ become अय्, अव्, आय्, आव् before a vowel.

    एचः स्थानेऽचि परतोऽय् अव् आय् आव् इत्येते आदेशा **यथासंख्यं** भवन्ति —
    चयनम्, लवनम्, चायकः, लावकः. The अचि is read down from 6.1.77.

    The pairing is not done here. Four go to four in order, which is
    1.3.10's business, and asking it rather than writing the pairs out is
    what makes this rule's correspondence checkable instead of asserted.
    """
    if not before_vowel:
        return Ayadi(None, "6.1.78",
                     "अचि — nothing but a vowel follows, so the एच् stands")

    paired = yathasamkhya(ec(), AYAV)
    if paired is None:            # 1.3.10 refuses unequal lists
        return Ayadi(None, "6.1.78",
                     "1.3.10 will not pair these lists")
    table = dict(paired)

    for length in (2, 1):         # ऐ and औ before ए and ओ
        if len(stem) >= length and stem[-length:] in table:
            found = stem[-length:]
            return Ayadi(stem[:-length] + table[found], "6.1.78",
                         f"एचोऽयवायावः — {found} → {table[found]} before a "
                         f"vowel, यथासंख्यम् by 1.3.10")
    return Ayadi(None, "6.1.78", f"{stem} does not end in एच्")


# ---------------------------------------------------------------------------
# 6.1.64 धात्वादेः षः सः,  6.1.65 णो नः,  3.4.79 टित आत्मनेपदानां टेरे
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Initial:
    """A root's opening after the dhātvādi rules, and which one acted."""

    result: str
    by: str
    why: str
    changed: bool = False



@dataclass(frozen=True)
class Iyanuvan:
    """What the i or u became, and on whose authority."""

    form: str
    by: str
    why: str
    applied: bool = True


def iyan_uvan(
    stem: str,
    *,
    dhatu: bool = True,
    snu: bool = False,
    bhru: bool = False,
    ardhadhatuka: bool = False,
    dhatu_lopa: bool = False,
) -> Optional[Iyanuvan]:
    """
    6.4.77 अचि श्नुधातुभ्रुवां य्वोरियङुवङौ — इयङ् for a final i, उवङ् for a
    final u, before a vowel affix.

    Only for three things: an aṅga ending in the affix श्नु, a धातु, and
    भ्रू. श्नुधातुभ्रुवामिति किम्? लक्ष्म्यै, वध्वै — neither is one of the
    three and neither takes it.

    **It does not ordinarily get to apply at all.** The Kāśikā is explicit:
    इयङुवङ्भ्यां गुणवृद्धी भवतो विप्रतिषेधेन — where guṇa or vṛddhi is also
    available, those win by 1.4.2, and चयनम्, चायकः, लवनम्, लावकः are the
    forms that result. So this rule is reached only where the strengthening
    has been stopped by something else, and the something else is usually
    one of the three prohibitions.

    That is why the guṇa is asked about here rather than assumed away: लू
    with अच् gives लोलवः if the strengthening stands and लोलुवः if it does
    not, and the whole difference is 1.1.4 न धातुलोप आर्धधातुके — which is
    reached because the same अच् elided the यङ्.
    """
    from src.astadhyayi.rules.adhyaya_1_pada_1 import guna_vrddhi_blocked

    if not (dhatu or snu or bhru):
        return None

    final = antya(stem)
    substitute = {"i": "iy", "ī": "iy", "u": "uv", "ū": "uv"}.get(final)
    if substitute is None:
        return None

    stopped = guna_vrddhi_blocked(
        final, ardhadhatuka=ardhadhatuka, dhatu_lopa=dhatu_lopa)
    if stopped is None:
        return Iyanuvan(
            stem, "1.4.2",
            "इयङुवङ्भ्यां गुणवृद्धी भवतो विप्रतिषेधेन — the strengthening "
            "is not stopped here, and where both are available it is the "
            "one that stands: चयनम्, चायकः, लवनम्, लावकः",
            applied=False,
        )

    return Iyanuvan(
        stem[:-len(final)] + substitute, "6.4.77",
        f"अचि श्नुधातुभ्रुवां य्वोरियङुवङौ — {final} becomes {substitute} "
        f"before a vowel affix, the strengthening that would otherwise have "
        f"displaced it having been stopped by {stopped.by}",
    )

def dhatvadeh(root: str, *, dhatu: bool = True) -> Initial:
    """
    6.1.64 and 6.1.65 — a root's initial ष् becomes स्, its ण् becomes न्.

    धातोरादेः षकारस्य स्थाने सकारादेशो भवति: षह gives सहते, षिच gives
    सिञ्चति. And धातोरादेः णकारस्य नकार आदेशो भवति: णीञ् gives नयति, णम
    gives नमति.

    Both conditions in the sūtras are real and the Kāśikā tests each:

      धातुग्रहणं किम्?  षोडश, षण्डः — not roots, so untouched.
      आदेरिति किम्?    कषति, लषति — the ष् is not initial.

    Why the grammar enunciates these roots with sounds it immediately
    replaces is the interesting part, and the Kāśikā says it: the ṣ- and
    ṇ-forms are taught **so that later rules have something to point at** —
    8.3.59 आदेशप्रत्यययोः for षत्व, 8.4.14 for णत्व. A root is marked as
    ṣopadeśa or ṇopadeśa by how it is enunciated, and the enunciation is
    then undone. The mark survives the letter, exactly as with शप्'s श्.

    The logic itself is not written here. `pada._dhatvadeh` has done this
    since the pada rules needed it, and duplicating it would be the very
    thing `test_astadhyayi_no_restating` forbids; this wraps it so that the
    two sūtras it implements are registered rules rather than a private
    helper nobody can cite.
    """
    from src.astadhyayi.pada import _dhatvadeh

    if not dhatu:
        return Initial(root, "6.1.64",
                       "धातुग्रहणं किम्? — षोडश, षण्डः are not roots and "
                       "keep their ष्", changed=False)
    changed = _dhatvadeh(root)
    if changed == root:
        return Initial(root, "6.1.64",
                       "आदेरिति किम्? — no initial ष् or ण् to replace: "
                       "कषति, लषति keep theirs", changed=False)
    which = "6.1.65" if root.startswith("ṇ") else "6.1.64"
    reason = ("णो नः — the root's initial ण् becomes न्: णीञ् गives नयति"
              if which == "6.1.65"
              else "धात्वादेः षः सः — the root's initial ष् becomes स्")
    return Initial(changed, which, reason.replace("गives", "gives"),
                   changed=True)


@dataclass(frozen=True)
class Tite:
    ending: str
    by: str
    why: str
    changed: bool = False


def tit_atmanepada(ending: str, *, tit_lakara: bool = True) -> Tite:
    """
    3.4.79 टित आत्मनेपदानां टेरे — the टि of an ātmanepada ending becomes ए.

    टितो लकारस्य स्थाने यानि आत्मनेपदानि तेषां टेः एकारादेशो भवति. लट् is
    टित्, so its त becomes ते: एधते, पचते.

    The टि is 1.1.64's — from the last vowel to the end of the word — so
    for त it is the अ alone.

    The Kāśikā guards the rule against reaching too far: इह कस्माद् न भवति
    पचमानो यजमानः? प्रकृतैः तिबादिभिः आत्मनेपदानि विशेष्यन्ते — the
    ātmanepada meant are the eighteen of 3.4.78, not शानच् and its like.
    """
    if not tit_lakara:
        return Tite(ending, "3.4.79",
                    "टितः — the लकार is not टित्, so the ending stands")
    for position in range(len(ending) - 1, -1, -1):
        if ending[position] in "aāiīuūṛṝḷ":
            return Tite(ending[:position] + "e", "3.4.79",
                        "टित आत्मनेपदानां टेरे — the टि becomes ए: "
                        "एधते, पचते", changed=True)
    return Tite(ending, "3.4.79", f"{ending} has no टि to replace")


# ---------------------------------------------------------------------------
# 7.3.101, 7.1.3, and the two that make a final स् a visarga
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Lengthened:
    result: Optional[str]
    by: str
    why: str


def ato_dirgho_yani(stem: str, ending: str, *,
                    sarvadhatuka: bool = True) -> Lengthened:
    """
    7.3.101 अतो दीर्घो यञि — an अ-final aṅga lengthens before a यञ् affix.

    अकारान्तस्य अङ्गस्य दीर्घो भवति यञादौ सार्वधातुके परतः: पचामि, पचावः,
    पचामः. Both conditions are tested by the Kāśikā and both are here.

      अत इति किम्?   चिनुवः, चिनुमः — the aṅga does not end in अ.
      यञीति किम्?    पचतः, पचथः — त् and थ् are not यञ्.

    यञ् is not listed. It is resolved from the śivasūtras, and it reaches
    further than one might guess — य् व् र् ल् ञ् म् ङ् ण् न् झ् भ्, eleven
    sounds, because its marker ञ् closes the eighth list and not the sixth.
    """
    from src.astadhyayi.sivasutra import resolve

    if not sarvadhatuka:
        return Lengthened(None, "7.3.101",
                          "सार्वधातुके — the affix is not one: अङ्गना, "
                          "केशवः keep their अ")
    if not stem.endswith("a"):
        return Lengthened(None, "7.3.101",
                          f"अत इति किम्? — {stem} does not end in अ: "
                          f"चिनुवः, चिनुमः")
    if not ending or ending[0] not in resolve("yaÑ").sounds:
        return Lengthened(None, "7.3.101",
                          f"यञीति किम्? — {ending} does not begin with a "
                          f"यञ् sound: पचतः, पचथः")
    return Lengthened(stem[:-1] + "ā", "7.3.101",
                      "अतो दीर्घो यञि — पचामि, पचावः, पचामः")


@dataclass(frozen=True)
class Jhonta:
    result: Optional[str]
    by: str
    why: str


def jho_antah(affix: str) -> Jhonta:
    """
    7.1.3 झोऽन्तः — the झ् of an affix becomes अन्त्.

    प्रत्ययावयवस्य झस्य अन्त इत्ययम् आदेशो भवति: कुर्वन्ति, सुन्वन्ति,
    चिन्वन्ति — and पचन्ति, which is why the engine needs it.

    It is an **अपवाद to 1.3.7 चुटू**, and the commentaries say so rather
    than leaving it to be worked out: the Kāśikā lists झ् among the cu-series
    initials that become इत् and then adds झस्य अन्तादेशं वक्ष्यति, and the
    Nyāsa calls the substitution इत्संज्ञापवादम् outright. Both rules reach
    the झ् of झि; if 1.3.7 wins, the affix is a bare इ and पचन्ति cannot be
    derived. So this is the first genuine conflict in the engine's rule set,
    and it is settled the way 1.4.2 says such a conflict is not — by the
    exception defeating the general rule, whatever the numbers.
    """
    if not affix.startswith("jh"):
        return Jhonta(None, "7.1.3", f"{affix} does not begin with झ्")
    return Jhonta("ant" + affix[2:], "7.1.3",
                  "झोऽन्तः — झि becomes अन्ति: पचन्ति, कुर्वन्ति")


@dataclass(frozen=True)
class Hardened2:
    """A sound changed by one of the two rules that make रुणद्धि."""

    result: Optional[str]
    by: str
    why: str
    #: Where the change falls, and what it puts there for what. A caller
    #: holding the form in pieces needs all three: the sounds are not one
    #: character each, and त् → ध् is one letter for two.
    at: int = -1
    was: str = ""
    now: str = ""


def jhasas_tathoh_dhah(text: str) -> Hardened2:
    """
    8.2.40 झषस्तथोर्धोऽधः — a त् or थ् after a झष् becomes ध्.

    झष उत्तरयोः तकारथकारयोः स्थाने धकार आदेशो भवति, दधातिं वर्जयित्वा:
    **लब्धा, लब्धुम्; दोग्धा; लेढा; बोद्धा**.

    **अध इति किम्?** धत्तः, धत्थः — दधाति is excepted by the sūtra's own
    अधः, and its त् stands.

    झष् is the five voiced aspirates. This is the first of the two rules
    that turn रुणध् + ति into रुणद्धि; 8.4.53 is the other, and it stands
    later, so 8.2.1 पूर्वत्रासिद्धम् is what puts this one first.
    """
    from src.astadhyayi.sivasutra import resolve

    jhas = frozenset(resolve("jhaṣ").sounds)
    sounds = _sounds_of(text)
    for position in range(1, len(sounds)):
        here, before = sounds[position], sounds[position - 1]
        if here.text not in ("t", "th") or before.text not in jhas:
            continue
        return Hardened2(
            text[:here.start] + "dh" + text[here.start + len(here.text):],
            "8.2.40",
            "झषस्तथोर्धोऽधः — the त् becomes ध् after a झष्: लब्धा, दोग्धा",
            at=here.start, was=here.text, now="dh")
    return Hardened2(None, "8.2.40",
                     f"no त् or थ् of {text} stands after a झष्")


@dataclass(frozen=True)
class Abhyasa:
    """The reduplicated syllable after one of the rules that shapes it."""

    result: Optional[str]
    by: str
    why: str


def _varga_of(sound: str):
    """Which varga a stop belongs to, and where in it."""
    from src.astadhyayi.varna import VARGA

    for name, members in VARGA.items():
        if sound in members:
            return name, list(members).index(sound)
    return "", -1


def haladih_sesah(abhyasa: str) -> Abhyasa:
    """
    7.4.60 हलादिः शेषः — of the अभ्यास only the first consonant stays.

    अभ्यासस्य हलादिः शिष्यते, **अनादिर्लुप्यते**: जग्लौ, मम्लौ from ग्लै
    and म्लै — the ल् of the copy goes and the ग् and म् remain. पपाच,
    पपाठ; and for a vowel-initial root आट, आटतुः, आटुः.

    What is kept is the opening consonant and the vowel after it. What
    goes is every other consonant of the copy, before the vowel and after
    it alike.
    """
    sounds = _sounds_of(abhyasa)
    kept = []
    seen_vowel = False
    for sound in sounds:
        if sound.kind == "vowel":
            seen_vowel = True
            kept.append(sound.text)
        elif not seen_vowel and not kept:
            kept.append(sound.text)           # the हलादि, which stays
        # everything else is अनादि and goes
    made = "".join(kept)
    if made == abhyasa:
        return Abhyasa(None, "7.4.60",
                       abhyasa + " is already हलादि and nothing more")
    return Abhyasa(made, "7.4.60",
                   "हलादिः शेषः — अनादिर्लुप्यते: जग्लौ, मम्लौ")


def abhyasa_hrasvah(abhyasa: str) -> Abhyasa:
    """
    7.4.59 ह्रस्वः — and the अभ्यास's vowel is short.

    ह्रस्वो भवति अभ्यासस्य: दुढौकिषते, तुत्रौकिषते. It is why ददाति has
    a short अ in its first syllable where दा has a long आ, and why बिभेति
    has इ for भी's ई.
    """
    for sound in _sounds_of(abhyasa):
        if sound.kind != "vowel":
            continue
        short = _SHORT.get(sound.text)
        if short is None or short == sound.text:
            continue
        return Abhyasa(
            abhyasa[:sound.start] + short
            + abhyasa[sound.start + len(sound.text):],
            "7.4.59",
            "ह्रस्वः — the अभ्यास's vowel is short: ददाति, बिभेति")
    return Abhyasa(None, "7.4.59",
                   "the vowel of " + abhyasa + " is already short")


def kuhos_cuh(abhyasa: str) -> Abhyasa:
    """
    7.4.62 कुहोश्चुः — a कवर्ग or ह् in the अभ्यास becomes a चवर्ग.

    अभ्यासस्य कवर्गहकारयोः चवर्गादेशो भवति: **चकार, चखान; जगाम, जघान**;
    and of the ह्, **जहार, जिहीर्षति, जहौ**.

    1.1.50 स्थानेऽन्तरतमः picks which चवर्ग by nearness, so क् goes to च्
    and ग् to ज्, voice and aspiration kept. The ह् has no varga of its
    own and the tradition pairs it with the voiced aspirate: हु gives झु,
    which 8.4.54 then makes जु — **जुहोति**.
    """
    from src.astadhyayi.varna import VARGA

    sounds = _sounds_of(abhyasa)
    if not sounds or sounds[0].kind == "vowel":
        return Abhyasa(None, "7.4.62",
                       abhyasa + " does not open on a कवर्ग or ह्")
    first = sounds[0].text
    if first == "h":
        made = "jh"
    else:
        name, place = _varga_of(first)
        if name != "ku":
            return Abhyasa(None, "7.4.62",
                           first + " is neither a कवर्ग nor ह्")
        made = VARGA["cu"][place]
    return Abhyasa(made + abhyasa[len(first):], "7.4.62",
                   "कुहोश्चुः — चकार, जगाम, जहार, जुहोति")


def abhyase_car(abhyasa: str) -> Abhyasa:
    """
    8.4.54 अभ्यासे चर् च — and a झल् in the अभ्यास loses its aspiration.

    अभ्यासे वर्तमानानां झलां चरादेशो भवति, चकाराद् जश् च: बुभूषति,
    ददौ, डुढौकिषते.

    Which of the two is not left to be worked out — the vṛtti says it:
    **प्रकृतिचरां प्रकृतिचरो भवन्ति** (चिचीषति, तितनिषति), **प्रकृतिजशां
    प्रकृतिजशो भवन्ति** (जिजनिषते, बुबुधे, ददौ). A voiceless sound takes
    the voiceless unaspirated of its own varga and a voiced one the
    voiced: ध् gives द् and दधाति, भ् gives ब् and बिभेति, and the झ्
    that 7.4.62 made of हु's ह् gives ज् and **जुहोति**.

    The varga is what settles it, and not `antaratama`: asked for the
    nearest of चर् and जश् to थ्, that function answers स्, both being
    dental — and तितनिषति is the vṛtti's own form.
    """
    from src.astadhyayi.varna import VARGA

    sounds = _sounds_of(abhyasa)
    if not sounds:
        return Abhyasa(None, "8.4.54", "nothing to change")
    first = sounds[0].text
    name, place = _varga_of(first)
    if place not in (1, 3):
        return Abhyasa(None, "8.4.54",
                       first + " is not an aspirate, so it is already its "
                       "own चर् or जश्")
    return Abhyasa(VARGA[name][place - 1] + abhyasa[len(first):], "8.4.54",
                   "अभ्यासे चर् च — बुभूषति, दधाति, जुहोति")


def urat(abhyasa: str) -> Abhyasa:
    """
    7.4.66 उरत् — an ऋ-final अभ्यास takes अ.

    ऋवर्णान्तस्य अभ्यासस्य अकारादेशो भवति: **ववृते, ववृधे, शशृधे**.
    """
    sounds = _sounds_of(abhyasa)
    if not sounds or sounds[-1].text not in ("ṛ", "ṝ"):
        return Abhyasa(None, "7.4.66",
                       abhyasa + " does not end in ऋ or ॠ")
    return Abhyasa(abhyasa[:sounds[-1].start] + "a", "7.4.66",
                   "उरत् — ववृते, ववृधे")


#: 7.4.76's three roots, as the dhātupāṭha enunciates them.
BHRNAM_THREE: Tuple[str, ...] = ("ḍubhṛñ", "māṅ", "ohāṅ")


def bhrnam_it(abhyasa: str, *, root: str = "") -> Abhyasa:
    """
    7.4.76 भृञामित् — three roots take इ in the अभ्यास under श्लु.

    भृञादीनां त्रयाणाम् अभ्यासस्य इकारादेशो भवति श्लौ सति: **भृञ्
    बिभर्ति; माङ् मिमीते; ओहाङ् जिहीते**. **त्रयाणाम् इत्येव** — जहाति,
    from ओहाक् which is not one of the three. **श्लौ इत्येव** — बभार,
    where the doubling is लिट्'s and not श्लु's.

    It displaces 7.4.66's अ for भृ, which would otherwise have given
    बभर्ति.
    """
    if root not in BHRNAM_THREE:
        return Abhyasa(None, "7.4.76",
                       "त्रयाणाम् इत्येव — " + (root or "this root")
                       + " is not one of भृञ्, माङ्, ओहाङ्: जहाति")
    for sound in _sounds_of(abhyasa):
        if sound.kind != "vowel":
            continue
        if sound.text == "i":
            return Abhyasa(None, "7.4.76", "the अभ्यास already has its इ")
        return Abhyasa(
            abhyasa[:sound.start] + "i"
            + abhyasa[sound.start + len(sound.text):],
            "7.4.76", "भृञामित् — बिभर्ति, मिमीते, जिहीते")
    return Abhyasa(None, "7.4.76", abhyasa + " has no vowel")


def coh_kuh(text: str, *, at_pada_end: bool = False) -> Hardened2:
    """
    8.2.30 चोः कुः — a चु becomes the corresponding कु before a झल्.

    चवर्गस्य कवर्गादेशो भवति झलि परतः पदान्ते च: **पक्ता, पक्तुम्,
    पक्तव्यम्; ओदनपक्; वक्ता, वक्तुम्, वाक्**.

    It is why युनक्ति has a क् where युज् has a ज्: the ज् stands before
    त्, a झल्, and becomes ग् — and 8.4.55 खरि च then hardens that to
    क्. Two rules, and 8.2.1 पूर्वत्रासिद्धम् puts them in that order,
    the later one being unable to contend with the earlier.

    1.1.50 स्थानेऽन्तरतमः picks which कु: the nearest in effort, so ज्
    goes to ग् and च् to क्, voice and aspiration kept.
    """
    from src.astadhyayi.sivasutra import resolve
    from src.astadhyayi.varna import VARGA

    jhal = frozenset(resolve("jhaL").sounds)
    cu, ku = VARGA["cu"], tuple(VARGA["ku"])
    sounds = _sounds_of(text)
    for position, sound in enumerate(sounds):
        if sound.text not in cu:
            continue
        following = (sounds[position + 1]
                     if position + 1 < len(sounds) else None)
        if following is None:
            if not at_pada_end:
                continue
        elif following.text not in jhal:
            continue
        nearest = antaratama(sound.text, ku)
        if not nearest:
            continue
        return Hardened2(
            text[:sound.start] + nearest[0]
            + text[sound.start + len(sound.text):],
            "8.2.30", "चोः कुः — the चु becomes its कु: पक्ता, वक्ता, "
                      "युनक्ति",
            at=sound.start, was=sound.text, now=nearest[0])
    return Hardened2(None, "8.2.30",
                     f"no चु of {text} stands before a झल् or at a "
                     f"pada's end")


def jhalam_jas_jhasi(text: str) -> Hardened2:
    """
    8.4.53 झलां जश् झशि — a झल् becomes its जश् before a झश्.

    झलां स्थाने जशादेशो भवति झशि परतः: **लब्धा, दोग्धा, बोद्धा** — the
    same three words 8.2.40 makes, finished. **झशीति किम्?** दत्तः,
    दत्थः, दध्मः.

    जश् is ज् ब् ग् ड् द्, and 1.1.50 स्थानेऽन्तरतमः picks the one of its
    own place: ध् before ध् gives द्, and रुणध्धि becomes **रुणद्धि**.
    """
    from src.astadhyayi.sivasutra import resolve

    jhal = frozenset(resolve("jhaL").sounds)
    jhas_following = frozenset(resolve("jhaś").sounds)
    jas = tuple(resolve("jaś").sounds)
    sounds = _sounds_of(text)
    for position in range(len(sounds) - 1):
        here, after = sounds[position], sounds[position + 1]
        if here.text not in jhal or after.text not in jhas_following:
            continue
        nearest = antaratama(here.text, jas)
        if not nearest or nearest[0] == here.text:
            continue
        return Hardened2(
            text[:here.start] + nearest[0]
            + text[here.start + len(here.text):],
            "8.4.53",
            "झलां जश् झशि — the झल् takes its जश्: लब्धा, रुणद्धि",
            at=here.start, was=here.text, now=nearest[0])
    return Hardened2(None, "8.4.53",
                     f"no झल् of {text} stands before a झश्")


def hali_ca(stem: str, following: str) -> Lengthened:
    """
    8.2.77 हलि च — a र्- or व्-final root lengthens its इक् before a हल्.

    हलि च परतो रेफवकारान्तस्य धातोः उपधाया इको दीर्घो भवति:
    **आस्तीर्णम्, विस्तीर्णम्, विशीर्णम्, अवगूर्णम्**; and of a व्-final
    root, **दीव्यति, सीव्यति** — which is why the fourth class's own
    example in the vṛtti on 3.1.69 has a long ई that दिव् does not.

    **धातोरित्येव** — दिवमिच्छति दिव्यति, चतुर इच्छति चतुर्यति: the same
    shapes from a noun, and no lengthening. **इक इत्येव** — स्मर्यते,
    भव्यम्, where the उपधा is not an इक्.
    """
    from src.astadhyayi.sivasutra import resolve

    if not following or following[0] not in resolve("hal").sounds:
        return Lengthened(None, "8.2.77",
                          f"हलि — {following or 'nothing'} does not begin "
                          f"with a consonant")
    if not stem or stem[-1] not in ("r", "v"):
        return Lengthened(None, "8.2.77",
                          f"रेफवकारान्तस्य — {stem} ends in neither र् nor व्")
    position, sound = upadha(stem)
    if sound not in ("i", "u", "ṛ", "ḷ"):
        return Lengthened(
            None, "8.2.77",
            f"इक इत्येव — the उपधा of {stem} is {sound or 'nothing'}, "
            f"which is not a short इक्: स्मर्यते, भव्यम्")
    return Lengthened(stem[:position] + _LONG[sound] + stem[position + 1:],
                      "8.2.77",
                      "हलि च — the इक् उपधा lengthens: दीव्यति, सीव्यति")


@dataclass(frozen=True)
class Cerebral:
    """A form after 8.4.1 or 8.4.2 has turned a न् into a ण्."""

    result: Optional[str]
    by: str
    why: str
    #: What stood between the र्/ष् and the न्, where anything did.
    across: str = ""
    #: Where in `text` the न् stood, so a caller holding the form in
    #: pieces can put the ण् back in the right one.
    at: int = -1


#: 8.4.2's list, as sounds. **अट्** is the pratyāhāra — the vowels with
#: ह य व र — **कु** the k-varga, **पु** the p-varga; आङ् is a preverb and
#: नुम् an augment, both of which reach the surface as sounds already in
#: those two sets or as the anusvāra the Kāśikā says नुम् stands for
#: (नुम्ग्रहणमनुस्वारोपलक्षणार्थम्).
def _across_which():
    """
    अट् कु पु, with the vowels closed under **1.1.69 अणुदित् सवर्णस्य
    चाप्रत्ययः**.

    A pratyāhāra names the short vowels, and 1.1.69 makes each of them
    stand for every vowel of its own kind. Without that closure the ई of
    क्रीणाति was not an अट् and 8.4.2 did not reach the न् — the Nyāsa on
    this very sūtra invokes the rule, अण् सवर्णान् गृह्णाति.
    """
    from src.astadhyayi.rules.adhyaya_1_pada_1 import savarna
    from src.astadhyayi.sivasutra import resolve
    from src.astadhyayi.varna import SVARA, VARGA

    named = frozenset(resolve("aṭ").sounds)
    vowels = [sound for sound in named if sound in SVARA]
    closed = set(named)
    for sound in SVARA:
        if any(savarna(sound, one) for one in vowels):
            closed.add(sound)
    return frozenset(closed) | frozenset(VARGA["ku"])         | frozenset(VARGA["pu"]) | {"ṃ"}


def cerebral_n(text: str, *, direct: bool = False) -> Cerebral:
    """
    8.4.1 रषाभ्यां नो णः समानपदे, and 8.4.2 for what may stand between.

    रेफषकाराभ्याम् उत्तरस्य नकारस्य णकारादेशो भवति, समानपदस्थौ चेद्
    निमित्तनिमित्तिनौ: **आस्तीर्णम्, विशीर्णम्; कुष्णाति, पुष्णाति**. And
    with 8.4.2, अट् कु पु आङ् नुम् may stand between and it happens all
    the same: **करणम्, हरणम्, अर्केण, चर्मणा, बृंहणम्**.

    **ऋवर्णाच्च** — the Kāśikā's vārttika adds ऋ and ॠ to the र् and ष्
    that occasion it: तिसृणाम्, चतसृणाम्, मातॄणाम्, पितॄणाम्. So गृभ्णाति
    has its ण् from a vowel.

    **AND WHY चरन्ति KEEPS ITS न्.** The rule looks like it should reach
    it — र्, then अ which is an अट्, then न् — and the Kāśikā writes
    चरन्ति and स्मरन्ति all through. The reason is a rule three pādas
    earlier: **8.3.24 नश्चापदान्तस्य झलि** has already turned that न् into
    an anusvāra, त् being a झल्, and **8.2.1 पूर्वत्रासिद्धम्** means
    8.4.1 cannot see past what the tripādī has done. There is no न् left
    for it. 8.4.58 अनुस्वारस्य ययि परसवर्णः then gives the anusvāra back
    as the न् one hears — so the two rules cancel on the surface, and the
    net condition is the one stated here: **a न् followed by a झल् is
    out of this rule's reach.**

    `direct` picks which of the two sūtras is being asked about — 8.4.1
    where the र् or ष् stands next to the न्, 8.4.2 where it does not.
    """
    from src.astadhyayi.sivasutra import resolve

    jhal = frozenset(resolve("jhaL").sounds)
    across_which = _across_which()
    sounds = _sounds_of(text)
    for position, sound in enumerate(sounds):
        if sound.text != "n":
            continue
        # 8.4.37 पदान्तस्य — a word-final न् is not touched; and a न्
        # before a झल् is an anusvāra by 8.3.24 long before this.
        following = sounds[position + 1] if position + 1 < len(sounds) else None
        if following is None or following.text in jhal:
            continue
        across = []
        for earlier in reversed(sounds[:position]):
            if earlier.text in ("r", "ṣ", "ṛ", "ṝ"):
                if direct != (not across):
                    break
                return Cerebral(
                    text[:sound.start] + "ṇ" + text[sound.start + 1:],
                    "8.4.1" if direct else "8.4.2",
                    "रषाभ्यां नो णः समानपदे — आस्तीर्णम्, कुष्णाति"
                    if direct else
                    "अट्कुप्वाङ्नुम्व्यवायेऽपि — करणम्, अर्केण, चर्मणा",
                    across="".join(reversed(across)), at=sound.start)
            if earlier.text not in across_which:
                break
            across.append(earlier.text)
    return Cerebral(None, "8.4.1" if direct else "8.4.2",
                    f"no न् of {text} stands after a र्, ष् or ऋ "
                    f"{'next to it' if direct else 'across an अट्, कु, पु'}")


@dataclass(frozen=True)
class Visarga:
    result: Optional[str]
    by: str
    why: str


def sasajuso_ruh(pada: str) -> Visarga:
    """
    8.2.66 ससजुषो रुः — a pada ending in स् takes रु in its place.

    सकारान्तस्य पदस्य सजुष् इत्येतस्य च रुर्भवति: अग्निरत्र, वायुरत्र. The
    रु is a step, not a result — 8.3.15 turns it into the visarga one
    actually hears, and the two are worth keeping apart because they part
    company before a vowel, where the र् stays a र्.
    """
    if not pada.endswith("s"):
        return Visarga(None, "8.2.66", f"{pada} does not end in स्")
    return Visarga(pada[:-1] + "r", "8.2.66",
                   "ससजुषो रुः — the final स् becomes रु")


def kharavasanayoh(pada: str, *, at_pause: bool = True,
                   following: str = "") -> Visarga:
    """
    8.3.15 खरवसानयोर्विसर्जनीयः — र् becomes a visarga before खर् or a pause.

    रेफान्तस्य पदस्य खरि परतः अवसाने च विसर्जनीयादेशो भवति: वृक्षः,
    प्लक्षः at a pause, वृक्षस्तरति before खर्.

    खरवसानयोरिति किम्? अग्निर्नयति, वायुर्नयति — न् is neither, so the र्
    stands. That condition is why this is not simply "final र् becomes ः".
    """
    from src.astadhyayi.sivasutra import resolve

    if not pada.endswith("r"):
        return Visarga(None, "8.3.15", f"{pada} does not end in र्")
    if not at_pause and (
            not following or following[0] not in resolve("khaR").sounds):
        return Visarga(None, "8.3.15",
                       "खरवसानयोरिति किम्? — neither खर् nor a pause "
                       "follows: अग्निर्नयति")
    return Visarga(pada[:-1] + "ḥ", "8.3.15",
                   "खरवसानयोर्विसर्जनीयः — वृक्षः, पचतः")


# ---------------------------------------------------------------------------
# 6.1.101 अकः सवर्णे दीर्घः, and 6.1.97 अतो गुणे which excepts it
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Ekadesa:
    """The single sound put in place of two, and the rule that chose it."""

    result: Optional[str]
    by: str
    why: str


#: The short counterpart of each vowel, for 7.4.59's ह्रस्वः. ए and ओ
#: have none of their own, and 1.1.48 एच इग्घ्रस्वादेशे gives them the
#: इक् nearest in place — इ for ए and ऐ, उ for ओ and औ.
_SHORT = {"ā": "a", "ī": "i", "ū": "u", "ṝ": "ṛ", "ḹ": "ḷ",
          "e": "i", "ai": "i", "o": "u", "au": "u"}

#: The long counterpart of each अक् vowel, for 6.1.101.
_LONG = {"a": "ā", "ā": "ā", "i": "ī", "ī": "ī", "u": "ū", "ū": "ū",
         "ṛ": "ṝ", "ṝ": "ṝ", "ḷ": "ḷ"}


def akah_savarne_dirghah(first: str, second: str) -> Ekadesa:
    """
    6.1.101: अक् followed by a vowel of its own kind gives the long one.

    अकः सवर्णे अचि परतः पूर्वपरयोः स्थाने दीर्घ एकादेशो भवति: दण्डाग्रम्,
    दधीन्द्रः, मधूदके.

    अक इति किम्? अग्नये. सवर्ण इति किम्? दध्यत्र — इ and अ are not of one
    kind, so यण् applies instead.

    Whether two sounds are सवर्ण is not decided here. 1.1.9
    तुल्यास्यप्रयत्नं सवर्णम् decides it and is codified; this asks.
    """
    from src.astadhyayi.rules.adhyaya_1_pada_1 import savarna

    if first not in _LONG:
        return Ekadesa(None, "6.1.101",
                       f"अक इति किम्? — {first} is not an अक् vowel")
    # 1.1.9's function answers with a plain bool. Reading it as a record —
    # getattr(verdict, "savarna", False) — took the default every time and
    # the rule silently never fired.
    if not savarna(first, second):
        return Ekadesa(None, "6.1.101",
                       f"सवर्ण इति किम्? — {first} and {second} are not of "
                       f"one kind: दध्यत्र")
    return Ekadesa(_LONG[first], "6.1.101",
                   "अकः सवर्णे दीर्घः — दण्डाग्रम्, दधीन्द्रः")


#: 1.1.50 स्थानेऽन्तरतमः picks each इक्'s यण् — इ takes य्, उ takes व्,
#: ऋ takes र्, ऌ takes ल्. The pairing is यथासंख्यम् by 1.3.10, and it is
#: written out because 6.1.77's यण् is a pratyāhāra of four sounds set
#: against a pratyāhāra of four, which is the one thing `antaratama`
#: cannot work out from place of articulation alone: ऌ and ल् are the
#: only pair it would get right unaided.
_YAN = {"i": "y", "ī": "y", "u": "v", "ū": "v",
        "ṛ": "r", "ṝ": "r", "ḷ": "l"}


def yan_sandhi(first: str, second: str) -> Ekadesa:
    """
    6.1.77 इको यणचि — an इक् before a dissimilar vowel becomes its यण्.

    इकः स्थाने यण् आदेशो भवति अचि परतः: **दध्यत्र, मध्वत्र, धातॄश्रितम्,
    लाकृतिः**. यथासंख्यम् by 1.3.10 — इ and ई take य्, उ and ऊ take व्, ऋ
    and ॠ take र्, ऌ takes ल्.

    **अचि इति किम्?** दधि सिञ्चति — a consonant follows, so the इ stands.

    **And where the two vowels ARE of one kind this rule must not act:**
    6.1.101 अकः सवर्णे दीर्घः reaches दधीन्द्रः, and 1.4.2 विप्रतिषेधे परं
    कार्यम् gives it the later number. Both are asked, and the सवर्ण test
    is 1.1.9's, not a second one written here.
    """
    from src.astadhyayi.rules.adhyaya_1_pada_1 import is_ik, savarna
    from src.astadhyayi.varna import SVARA

    if first not in _YAN or not is_ik(first):
        return Ekadesa(None, "6.1.77",
                       f"इकः इति किम्? — {first} is not an इक्")
    if not second or second[0] not in SVARA:
        return Ekadesa(None, "6.1.77",
                       f"अचि इति किम्? — {second or 'nothing'} does not "
                       f"begin with a vowel: दधि सिञ्चति")
    if savarna(first, second[0]):
        return Ekadesa(None, "6.1.77",
                       f"{first} and {second[0]} are सवर्ण, and 6.1.101 "
                       f"अकः सवर्णे दीर्घः is the rule for that: दधीन्द्रः")
    return Ekadesa(_YAN[first], "6.1.77",
                   "इको यणचि — दध्यत्र, मध्वत्र")


def ato_gune(first: str, second: str) -> Ekadesa:
    """
    6.1.97 अतो गुणे — a non-final अ before a guṇa vowel yields to it.

    अकारात् अपदान्तात् गुणे परतः पूर्वपरयोः स्थाने **पररूपम्** एकादेशो
    भवति — the *later* of the two stands: पचन्ति, यजन्ति.

    अत इति किम्? यान्ति, वान्ति. गुण इति किम्? अपचे, अयजे.

    The Kāśikā names the relationship this rule has to its neighbour rather
    than leaving it to be worked out: **अकः सवर्णे दीर्घस्य अपवादः**. Both
    reach the अ + अ of पच + अन्ति, and 6.1.101 would give पचान्ति. The
    exception is what makes the received form derivable, and 1.4.2 does not
    decide between them by position — an अपवाद defeats its उत्सर्ग whatever
    the numbers.

    Which guṇa vowels there are is 1.1.2's business, not this rule's.
    """
    from src.astadhyayi.rules.adhyaya_1_pada_1 import GUNA

    if first != "a":
        return Ekadesa(None, "6.1.97",
                       f"अत इति किम्? — the first is {first}, not अ: "
                       f"यान्ति, वान्ति")
    if second not in GUNA:
        return Ekadesa(None, "6.1.97",
                       f"गुण इति किम्? — {second} is not a guṇa vowel: "
                       f"अपचे, अयजे")
    return Ekadesa(second, "6.1.97",
                   "अतो गुणे — the later form stands: पचन्ति, यजन्ति")


# ---------------------------------------------------------------------------
# 2.4.72 अदिप्रभृतिभ्यः शपः
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Elided:
    """Whether शप् is elided after this root, and on what ground."""

    elided: bool
    by: str
    why: str
    #: लुक्, not लोप. 1.1.61 names the three elisions apart, and which one
    #: it is decides what 1.1.63 will and will not let through.
    elision: str = ""


def adiprabhrtibhyah_sapah(root: str) -> Elided:
    """
    2.4.72: शप् is elided by लुक् after अद् and the roots listed with it.

    अदिप्रभृतिभ्य उत्तरस्य शपो लुग् भवति: अत्ति, हन्ति, द्वेष्टि. It is
    what makes the second conjugation look different from the first — एति
    beside भवति, with no अ between root and ending.

    Which roots those are is not written here. अदिप्रभृति is the second
    gaṇa, and the dhātupāṭha on disk already numbers its entries; asking it
    is both shorter and safer than a list that could fall out of step with
    the corpus it is copied from. A root given as its full upadeśa is looked
    up exactly, so इण् finds 02.0040 and not something else called इ.
    """
    from src.astadhyayi.pada import verbal_gana

    ganas = verbal_gana(root)
    if not ganas:
        return Elided(False, "2.4.72",
                      f"{root} is not in the dhātupāṭha, so its gaṇa "
                      f"cannot be read")
    if "02" not in ganas:
        return Elided(False, "2.4.72",
                      f"अदिप्रभृतिभ्यः — {root} is not of the second gaṇa "
                      f"(it is {', '.join(sorted(ganas))}), so शप् stands: "
                      f"भवति, पचति")
    return Elided(True, "2.4.72",
                  "अदिप्रभृतिभ्यः शपः — शप् is elided by लुक् after the "
                  "अदादि roots: अत्ति, हन्ति, द्वेष्टि",
                  elision="luk")


# ---------------------------------------------------------------------------
# 8.4.55 खरि च
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Hardened:
    result: Optional[str]
    by: str
    why: str


def khari_ca(sound: str, following: str) -> Hardened:
    """
    8.4.55: a झल् before a खर् becomes its चर् — its own voiceless mate.

    खरि च परतो झलां चरादेशो भवति: भेत्ता, भेत्तुम्, भेत्तव्यम्. It is what
    makes अद् + ति into अत्ति.

    Which sound replaces which is not tabulated. चर् is the first member of
    each varga, and `varna.VARGA` already holds the vargas in the alphabet's
    own order — कादयो मावसानाः स्पर्शाः — so the substitute is read off the
    row the sound stands in. A table mapping द् to त्, ध् to त्, ब् to प्
    and so on would be that same fact written twice.

    Both pratyāhāras come from the śivasūtras through 1.1.71.
    """
    from src.astadhyayi.sivasutra import resolve
    from src.astadhyayi.varna import VARGA

    if not following or following[0] not in resolve("caR").sounds:
        # चर् and खर् share their members; खर् is the wider of the two and
        # is what the sūtra names.
        khar = resolve("khaR").sounds
        if not following or following[0] not in khar:
            return Hardened(None, "8.4.55",
                            f"खरि — {following or 'nothing'} does not begin "
                            f"with a खर् sound")
    # झलाम् — the sūtra names झल्, and the nasals are not in it. Checking
    # only that the sound sits in a varga row let न् through, and हन् + ति
    # came out हत्ति.
    if sound not in resolve("jhaL").sounds:
        return Hardened(None, "8.4.55",
                        f"झलाम् — {sound} is not a झल् sound; the nasals "
                        f"are outside it, so हन्ति keeps its न्")
    for row in VARGA.values():
        if sound in row:
            hardened = row[0]
            if hardened == sound:
                return Hardened(None, "8.4.55",
                                f"{sound} is already its own चर्")
            return Hardened(hardened, "8.4.55",
                            f"खरि च — {sound} becomes {hardened} before a "
                            f"खर्: अत्ति, भेत्ता")
    return Hardened(None, "8.4.55", f"{sound} is not a स्पर्श")



__all__ = [
    "Name", "sarvadhatuka", "Affix", "sap",
    "LAGHU_IK", "Strengthened", "guna_before_affix", "mrjer_vrddhi",
    "Cerebral", "Dropped", "aco_nniti", "ato_lopah",
    "Abhyasa", "BHRNAM_THREE", "abhyasa_hrasvah", "abhyase_car",
    "ato_upadhayah", "bhrnam_it", "cerebral_n", "coh_kuh",
    "haladih_sesah", "hali_ca", "kuhos_cuh", "urat",
    "jhalam_jas_jhasi", "jhasas_tathoh_dhah",
    "sino_guna",
    "pugantalaghupadhasya", "upadha", "yan_sandhi",
    "ec", "AYAV", "Ayadi", "ayadi",
    "Initial", "dhatvadeh", "Tite", "tit_atmanepada",
    "Lengthened", "ato_dirgho_yani", "Jhonta", "jho_antah",
    "Visarga", "sasajuso_ruh", "kharavasanayoh",
    "Ekadesa", "akah_savarne_dirghah", "ato_gune",
    "Elided", "adiprabhrtibhyah_sapah",
    "Hardened", "khari_ca",
]