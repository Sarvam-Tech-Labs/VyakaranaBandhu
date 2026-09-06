# -*- coding: utf-8 -*-
"""
3.1.1 to 3.1.4 — what an affix is, where it goes, and how it is accented.

Four rules open adhyāya 3, and none of them makes a form. They set the
terms on which the next two and a half adhyāyas are read:

    3.1.1  प्रत्ययः          whatever is enumerated from here is an affix
    3.1.2  परश्च             and it stands AFTER what it is added to
    3.1.3  आद्युदात्तश्च      and its first vowel carries the accent
    3.1.4  अनुदात्तौ सुप्पितौ  except these two kinds, which have none

**The range is the largest in the grammar.** आ पञ्चमाध्यायपरिसमाप्तेः —
to the end of adhyāya 5. Everything enumerated across three adhyāyas
bears the name प्रत्यय without any of them saying so again.

**But not everything enumerated there.** The vṛtti excludes five kinds
by name — प्रकृत्युपपदोपाधिविकारागमान् वर्जयित्वा. A rule adding an
affix also names the base it goes on, sometimes a word that must stand
beside it, sometimes a condition, sometimes a change or an augment, and
none of those is the affix. So the heading is read as governing what a
rule PRESCRIBES, not every word the rule contains, and the exclusion
list is codified rather than left to be inferred.

**3.1.4 is an अपवाद of 3.1.3 and not a separate topic.** पूर्वस्यायम्
अपवादः: 3.1.3 gives every affix an initial उदात्त, and this takes it
away again from two kinds — the सुप् endings and anything marked with
प्. दृषदौ and पचति are unaccented where कर्तव्यम् and तैत्तिरीयम् are
not. Codified in that order, since an अपवाद read after the rule it
excepts can never fire.
"""

from dataclasses import dataclass
from typing import Tuple

#: What 3.1.1's heading does NOT cover, though a rule may name it in the
#: same breath as the affix. प्रकृत्युपपदोपाधिविकारागमान् वर्जयित्वा.
NOT_AFFIXES: Tuple[Tuple[str, str], ...] = (
    ("prakṛti", "the base an affix is added to — a root or a stem"),
    ("upapada", "a word that must stand beside it for the rule to reach"),
    ("upādhi", "a condition the rule lays down, such as a sense"),
    ("vikāra", "a change the rule makes to something already there"),
    ("āgama", "an augment inserted into the base, not added after it"),
)

#: 3.1.1's range, as the vṛtti gives it — आ पञ्चमाध्यायपरिसमाप्तेः.
AFFIX_SECTION_FROM, AFFIX_SECTION_THROUGH = "3.1.5", "5.4.160"


@dataclass(frozen=True)
class Affix:
    """What 3.1.1 to 3.1.4 say about something the grammar prescribes."""

    #: Whether the name प्रत्यय reaches it at all.
    is_affix: bool
    by: str
    why: str
    #: Where it stands relative to the base — 3.1.2 leaves only one answer.
    position: str = ""
    #: उदात्त on the first vowel, or अनुदात्त throughout.
    accent: str = ""
    accent_by: str = ""


def named_affix(
    *,
    prescribes: str = "pratyaya",
    sup: bool = False,
    pit: bool = False,
) -> Affix:
    """
    3.1.1 to 3.1.4, asked of one thing a rule prescribes.

    `prescribes` says which of the six things it is. Only the first is an
    affix; the other five are what the vṛtti excludes by name, and each
    is refused with the reason it is not one.
    """
    if prescribes != "pratyaya":
        known = dict(NOT_AFFIXES)
        if prescribes not in known:
            raise ValueError(
                f"{prescribes!r} is not something 3.1.1 speaks about. It is "
                f"either an affix or one of the five the vṛtti excludes: "
                f"{', '.join(k for k, _ in NOT_AFFIXES)}")
        return Affix(
            False, "",
            f"प्रकृत्युपपदोपाधिविकारागमान् वर्जयित्वा — a {prescribes} is "
            f"{known[prescribes]}, and 3.1.1's heading does not reach it. A "
            f"rule names it in the same breath as the affix, which is "
            f"why the exclusion has to be stated",
        )

    # 3.1.4 before 3.1.3, being its अपवाद.
    if sup or pit:
        return Affix(
            True, "3.1.1",
            "प्रत्ययः — an अधिकार to the end of adhyāya 5: आ "
            "पञ्चमाध्यायपरिसमाप्तेः. Whatever is enumerated from 3.1.5 "
            "onward bears this name without any rule saying so again",
            position="after",
            accent="anudātta",
            accent_by="3.1.4",
        )  # position and accent are 3.1.2's and 3.1.4's, cited not claimed
    return Affix(
        True, "3.1.1",
        "प्रत्ययः — an अधिकार to the end of adhyāya 5: आ "
        "पञ्चमाध्यायपरिसमाप्तेः. Whatever is enumerated from 3.1.5 "
        "onward bears this name without any rule saying so again",
        position="after",
        accent="ādyudātta",
        accent_by="3.1.3",
    )


@dataclass(frozen=True)
class Position:
    """Where an affix stands — 3.1.2, which says the only answer."""

    position: str
    by: str
    why: str


@dataclass(frozen=True)
class Accent:
    """How an affix is accented — 3.1.3, or 3.1.4 excepting it."""

    accent: str
    by: str
    why: str


def position_of() -> Position:
    """3.1.2 परश्च — an affix follows what it is added to."""
    return Position("after", "3.1.2", why_after())


def accent_of(*, sup: bool = False, pit: bool = False) -> Accent:
    """
    3.1.3 आद्युदात्तश्च, and 3.1.4 अनुदात्तौ सुप्पितौ excepting it.

    3.1.4 is asked first, being the अपवाद: read the other way round the
    general rule would answer for everything and the exception could
    never fire.
    """
    if sup or pit:
        return Accent("anudātta", "3.1.4", why_accented(sup=sup, pit=pit))
    return Accent("ādyudātta", "3.1.3", why_accented())


def why_after() -> str:
    """
    3.1.2 परश्च, and what its च is doing.

    परश्च स भवति धातोर्वा प्रातिपदिकाद् वा — an affix stands after the
    root or the stem: कर्तव्यम्, तैत्तिरीयम्. The vṛtti reads it as an
    अधिकार or a paribhāṣā, either way reaching every rule that follows.

    चकारः पुनरस्यैव समुच्चयार्थः, तेन उणादिषु परत्वं न विकल्प्यते — the
    च joins this to 3.1.1 rather than offering an alternative, so that
    in the उणादि section too an affix cannot be anything but following.
    Without it the position would have been open to doubt exactly where
    the affixes are least regular.
    """
    return (
        "परश्च — after the root or the stem, never before it: कर्तव्यम्, "
        "तैत्तिरीयम्. चकारः पुनरस्यैव समुच्चयार्थः, तेन उणादिषु परत्वं न "
        "विकल्प्यते"
    )


def why_accented(*, sup: bool = False, pit: bool = False) -> str:
    """
    3.1.3 and 3.1.4, and why the general rule had to be written at all.

    अनियतस्वरप्रत्ययप्रसङ्गे अनेकाक्षु च प्रत्ययेषु देशस्यानियमे सति
    वचनमिदम् आदेरुदात्तार्थम् — with an affix of more than one syllable
    there is nothing to say WHICH syllable takes the accent, so 3.1.3
    fixes it on the first: कर्तव्यम्, तैत्तिरीयम्.
    """
    if sup or pit:
        return (
            "अनुदात्तौ सुप्पितौ — पूर्वस्यायमपवादः: the सुप् endings and "
            "anything marked with प् take no accent at all. दृषदौ, "
            "दृषदः; पचति, पठति"
        )
    return (
        "आद्युदात्तश्च — the accent falls on the affix's FIRST vowel. "
        "अनियतस्वरप्रत्ययप्रसङ्गे … देशस्यानियमे सति वचनमिदम् "
        "आदेरुदात्तार्थम्: with more than one syllable there would "
        "otherwise be nothing to say which one takes it"
    )


def in_the_affix_section(sutra_id: str) -> bool:
    """
    Whether 3.1.1's heading reaches this sūtra.

    आ पञ्चमाध्यायपरिसमाप्तेर्यानित ऊर्ध्वमनुक्रमिष्यामः — from the next
    rule to the end of adhyāya 5. The four heading rules themselves are
    outside it: they say what an affix is rather than prescribing one.
    """
    def order(sid: str) -> Tuple[int, ...]:
        return tuple(int(p) for p in sid.split("."))

    return (order(AFFIX_SECTION_FROM) <= order(sutra_id)
            <= order(AFFIX_SECTION_THROUGH))
