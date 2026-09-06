# -*- coding: utf-8 -*-
"""
५.१.१–३० — प्राक्क्रीताच्छः, प्राग्वतेष्ठञ्, आर्हादगोपुच्छ…ठक्.

Three प्राक्-headings open inside thirty sūtras, which is the densest
stretch of them in the whole grammar — and the third one is bounded
not by प्राक् but by **आ**, an अभिविधि that takes its own limit in.

**AND THE FIRST OF THEM SETTLES WHAT A प्राक्-HEADING MEASURES.**
5.1.1's vṛtti asks why the rule says *before क्रीत* and not *before
the ठञ्*, since a heading could be bounded either by a SENSE or by an
AFFIX: **अर्थोऽवधित्वेन गृहीतः, न प्रत्ययः; तेन प्राक् ठञः छ इति
नोक्तम्** — the sense is what is taken as the limit, not the affix,
and that is why the rule is not worded the other way. Every one of
the four great headings names a sense-word: दीव्यति, वहति, हित,
क्रीत, वति. The affix is what the heading GIVES; the sense is what
bounds it.

**AND THE FORMULA CLOSES A THIRD TIME.** 5.1.17 ends the छ-and-यत्
stretch with **छयतोः पूर्णोऽवधिः। इतः परमन्यः प्रत्ययो विधीयते** —
the limit of both is complete, and from here another affix is
enjoined. 4.4.74 said it of ठक् and 4.4.144 of यत्, in those words.
Three times now, and it is simply how the Kāśikā closes a heading.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: Where छ is the affix. 5.1.1's vṛtti: **तेन क्रीतम् इति वक्ष्यति।
#: प्रागेतस्मात् क्रीतसंशब्दनाद् यानित ऊर्ध्वमनुक्रमिष्यामः,
#: छप्रत्ययस्तेष्वधिकृतो वेदितव्यः.**
#:
#: And here the MARKER and the LAST RULE come apart for the third
#: time, and by a wider gap than either of the two before: the word
#: क्रीत is lifted out of 5.1.37, but 5.1.18 प्राग्वतेष्ठञ् opens
#: another heading twenty sūtras earlier, and 5.1.17 says so —
#: **छयतोः पूर्णोऽवधिः**.
CHA_RUN: Tuple[str, str] = ("5.1.1", "5.1.17")

#: The sūtra whose word bounds the छ heading, twenty past its end.
CHA_MARKER: str = "5.1.37"

#: Where ठञ् is the affix. 5.1.18's vṛtti: **तेन तुल्यं क्रिया चेद्
#: वतिरिति वक्ष्यति। प्रागेतस्माद् वतिसंशब्दनाद् यानित
#: ऊर्ध्वमनुक्रमिष्यामः, ठञ् प्रत्ययस्तेष्वधिकृतो वेदितव्यः.**
#:
#: And its last rule, which is NOT its marker — 5.1.114 closes with
#: **ठञः पूर्णोऽवधिः**, the same formula 4.4.74, 4.4.144, 5.1.17,
#: 5.1.71 and 5.1.96 used. Six headings now, and not one of them
#: ends where its own name points.
#:
#: This is the narrowest of the six gaps: one sūtra. It is still a
#: gap, and holding the two apart from the start is what kept the
#: range from being guessed.
THAN_RUN: Tuple[str, str] = ("5.1.18", "5.1.114")

THAN_MARKER: str = "5.1.115"

#: And the third, which is bounded differently from all the others.
#: 5.1.19 opens with **आ** and not प्राक्, and the vṛtti draws the
#: consequence: **अभिविधावयमाकारः, तेनार्हत्यर्थेऽपि ठग् भवत्येव** —
#: this आ is an अभिविधि, an inclusive limit, so ठक् applies in the
#: sense of अर्हति TOO, at 5.1.63 itself. A प्राक्-heading stops
#: short of its marker; this one reaches it and takes it in.
ARHIYA_RUN: Tuple[str, str] = ("5.1.19", "5.1.71")

#: And its marker, which it REACHES and takes in — 5.1.63 तदर्हति,
#: the sūtra the heading is named from. Eight rules stand past it
#: still naming अर्हति, and 5.1.71 closes the account: **आर्हीयाणां
#: ठगादीनां पूर्णोऽवधिः। अतः परं प्राग्वतीयष्ठञेव भवति.**
#:
#: So the difference between this heading and the प्राक् ones is not
#: that its marker and its last rule coincide. It is that it takes
#: its marker IN where they stop short of theirs.
ARHIYA_MARKER: str = "5.1.63"

#: And a heading of a different kind altogether: 5.1.78 कालात्,
#: which supplies no affix and only a CONDITION — that the base be a
#: word for TIME. **कालादित्यधिकारः। यदित ऊर्ध्वम् अनुक्रमिष्यामः
#: कालादित्येवं तद् वेदितव्यम्.**
#:
#: Because it carries a condition and not an affix it stands inside
#: the ठञ् heading without competing with it, which is why every
#: rule under it still gives ठञ् unless it says otherwise.
KALA_RUN: Tuple[str, str] = ("5.1.78", "5.1.96")

#: 5.1.78 names 5.1.97 as its boundary — **कालादित्यधिकारो
#: व्युष्टादिभ्योऽण् इति यावत्** — and 5.1.96 closes one short of
#: it: **कालाधिकारस्य पूर्णोऽवधिः। अतः परं सामान्येन
#: प्रत्ययविधानम्.** The fifth heading in this project whose marker
#: is not its last rule, and the fifth time in that formula.
KALA_MARKER: str = "5.1.97"

#: The four kinds of measurement 5.1.19's vṛtti separates, because
#: the rule excepts two of them by name and the distinction decides
#: which affix a base takes:
#:
#:     ऊर्ध्वमानं किलोन्मानं परिमाणं तु सर्वतः ।
#:     आयामस्तु प्रमाणं स्यात् संख्या बाह्या तु सर्वतः ॥
#:
#: **भेदगणनं संख्या** — counting off items, one and two and three.
#: **गुरुत्वमानम् उन्मानम्** — weight, the पल. **आयाममानं प्रमाणम्**
#: — length, the वितस्ति. **आरोहपरिणाहमानं परिमाणम्** — girth and
#: height together, the प्रस्थ. 5.1.19 excepts संख्या and परिमाण
#: and leaves उन्मान and प्रमाण inside.
MEASURES: Tuple[Tuple[str, str], ...] = (
    ("saṃkhyā", "भेदगणनम् — counting items off, एकत्वादि"),
    ("unmāna", "गुरुत्वमानम् — weight, पलादि"),
    ("pramāṇa", "आयाममानम् — length, वितस्त्यादि"),
    ("parimāṇa", "आरोहपरिणाहमानम् — girth and height, प्रस्थादि"),
)

#: The vārttika at 5.1.20 that governs the whole ठञ् heading, and
#: the reason 5.1.20 says असमासे at all:
#: **प्राग् वतेः संख्यापूर्वपदानां तदन्तग्रहणम् अलुकि**
#: (महाभाष्य — वा० ५.१.२०) — before वति, a compound whose first
#: member is a numeral IS taken by a rule that names its last
#: member, provided no लुक् has removed the affix.
#:
#: Held as a constant because it decides four separate rules of this
#: block and one two pādas away, and because 5.1.20's असमासे is what
#: makes it inferable: **निष्कादिष्वसमासग्रहणं ज्ञापकं पूर्वत्र
#: तदन्ताप्रतिषेधस्य** — saying *not in a compound* HERE tells you
#: that compounds were not excluded THERE.
TADANTA_ALUKI: str = (
    "प्राग् वतेः संख्यापूर्वपदानां तदन्तग्रहणमलुकि")


#: The senses the छ heading covers — those named between 5.1.1 and
#: 5.1.17, which is what **प्राक्क्रीतीयेष्वर्थेषु** refers to every
#: time a vṛtti of that stretch says it.
CHA_SENSES: Tuple[str, ...] = ("hita", "tadartha", "tadasya-syāt")

#: And the ones the ठञ् and ठक् headings cover, which the vṛttis of
#: that stretch name collectively as **आर्हीयेष्वर्थेषु**.
#:
#: They are named one by one from 5.1.37 to 5.1.63, and 5.1.37 says
#: so as it opens them: **ठञादयस्त्रयोदश प्रत्ययाः प्रकृताः। तेषाम्
#: इतः प्रभृति समर्थविभक्तयः प्रत्ययार्थाश्च निर्दिश्यन्ते** — the
#: affixes have all been given already, and from here what is stated
#: is the CASE each takes and the SENSE each serves. So 5.1.18–36
#: say which affix and 5.1.37–63 say in what sense, and no rule of
#: the first half states a sense or a case of its own.
#:
#: `ārhīya` heads the list as the name of the set itself, since the
#: rules from 5.1.20 to 5.1.36 are asked under no narrower sense
#: than that.
#: The senses वति serves, 5.1.115–118 — where the ठञ् heading is
#: spent and a single affix answers four different relations.
VATI_SENSES: Tuple[str, ...] = (
    "tulya",              # 5.1.115 तेन तुल्यं क्रिया चेत्
    "iva",                # 5.1.116 तत्र तस्येव — as there, as his
    "arha",               # 5.1.117 तदर्हम् — such as it deserves
    "svārtha",            # 5.1.118 in its own sense, in the Veda
)

#: And the last section of the pāda: the STATE of a thing, and from
#: 5.1.124 its activity as well — **आ पादपरिसमाप्तेर्
#: भावकर्माधिकारः**, to the end of the quarter.
BHAVA_SENSES: Tuple[str, ...] = (
    "bhāva",              # 5.1.119 तस्य भावस्त्वतलौ
    "bhāva-karman",       # 5.1.124 …कर्मणि च, and on to the end
)

#: The senses named between 5.1.37 and 5.1.71 — the stretch the
#: ठक् of 5.1.19 governs.
ARHIYA_SENSES: Tuple[str, ...] = (
    "ārhīya",
    "krīta",              # 5.1.37 तेन क्रीतम् — bought with it
    "nimitta",            # 5.1.38 तस्य निमित्तम् — an omen of it
    "īśvara",             # 5.1.42 तस्येश्वरः — lord of it
    "vidita",             # 5.1.43 तत्र विदितः — known there
    "vāpa",               # 5.1.45 तस्य वापः — a field sown with it
    "vṛddhyādi",          # 5.1.47 वृद्ध्यायलाभशुल्कोपदा दीयते
    "harati",             # 5.1.50 तद् हरति वहति आवहति
    "sambhavati",         # 5.1.52 तद् संभवति अवहरति पचति
    "aṃśa-vasna-bhṛti",   # 5.1.56 तदस्य अंशो वस्नो भृतिः
    "parimāṇa",           # 5.1.57 तदस्य परिमाणम् — its measure
    "arhati",             # 5.1.63 तद् अर्हति — deserves it
)

#: And the senses named after ठक् has run out, where it is the ठञ्
#: of 5.1.18 alone: **अतः परं प्राग्वतीयष्ठञेव भवति.**
LATER_SENSES: Tuple[str, ...] = (
    "vartayati",          # 5.1.72 पारायणं वर्तयति — carries it on
    "āpanna",             # 5.1.73 संशयमापन्नः — fallen into it
    "gacchati",           # 5.1.74 योजनं गच्छति — goes it
    "āhṛta",              # 5.1.77 उत्तरपथेनाहृतम् — brought by it
    "nirvṛtta",           # 5.1.79 तेन निर्वृत्तम् — brought about
    "adhīṣṭādi",          # 5.1.80 अधीष्टो भृतो भूतो भावी
    "nirvṛttādi",         # 5.1.86 the five, carried together
    "pacyate",            # 5.1.90 षष्टिरात्रेण पच्यन्ते
    "parijayya-labhya-kārya-sukara",   # 5.1.93, four at once
    "brahmacarya",        # 5.1.94 तदस्य ब्रह्मचर्यम्
    "dakṣiṇā",            # 5.1.95 तस्य दक्षिणा
    "dīyate-kārya",       # 5.1.96 तत्र दीयते कार्यम्
    "sampādin",           # 5.1.99 तेन संपादिनि — set off by it
    "prabhavati",         # 5.1.101 तस्मै प्रभवति — equal to it
    "prāpta",             # 5.1.104 तदस्य प्राप्तम् — its time come
    "prayojana",          # 5.1.109 तदस्य प्रयोजनम् — its occasion
    "ādyanta",            # 5.1.114 आद्यन्तवचने — beginning and end
)


#: Everything the ठञ् heading of 5.1.18 covers, which is both sets:
#: the आर्हीय ones because ठक् is enjoined inside ठञ् as its
#: exception, and the later ones because ठक् has run out.
THAN_SENSES: Tuple[str, ...] = ARHIYA_SENSES + LATER_SENSES

#: Where त्व and तल् are the affixes. 5.1.120's vṛtti: **ब्रह्मणस्त्वः
#: इति वक्ष्यति। आ एतस्मात् त्वसंशब्दनाद् यानित ऊर्ध्वम्
#: अनुक्रमिष्यामः, तत्र त्वतलौ प्रत्ययावधिकृतौ वेदितव्यौ** — आ
#: again, so 5.1.136 is taken in, and it is also the last rule of
#: the pāda, so this is the one heading whose marker and last rule
#: DO coincide.
#:
#: They coincide because nothing follows: the pāda ends there. Every
#: other heading came apart from its marker because something opened
#: inside its range or its sense ran on past it, and here there is no
#: room for either.
TVA_RUN: Tuple[str, str] = ("5.1.120", "5.1.136")
TVA_MARKER: str = "5.1.136"

#: Every sense the pāda names, in the order the sections come. Held
#: as one tuple because the resolver's scoping and the tests both
#: want to ask *is this a sense of this pāda at all*, and answering
#: that from four tuples would be four chances to forget one.
PADA_SENSES: Tuple[str, ...] = (
    CHA_SENSES + THAN_SENSES + VATI_SENSES + BHAVA_SENSES)


@dataclass(frozen=True)
class Krita:
    """One rule of 5.1: a thing, a purpose, and what comes."""

    sutra: str
    #: What the affix is, or "" where the rule removes one, or where
    #: the rule states only a sense and leaves the affix यथाविहितम्.
    gives: str = ""
    #: The other affixes the same rule gives — 5.1.10's णढञौ,
    #: 5.1.21's ठन् beside its यत्.
    also_gives: Tuple[str, ...] = ()
    of: Tuple[str, ...] = ()
    gana: str = ""
    #: The sense the derived word carries: हित (good for it),
    #: तदर्थ (made for it out of that), तदस्य स्यात् (would belong
    #: to it), आर्हीय (worth it). "" where the rule states no sense
    #: of its own and so serves every sense the heading covers —
    #: which is what प्राक्क्रीतीयेष्वर्थेषु means.
    sense: str = ""
    #: The case the base stands in: चतुर्थी for what a thing is good
    #: for or made for, प्रथमा at 5.1.16, तृतीया for what a thing
    #: is bought with.
    case: str = ""
    #: A further condition on the derived word — संज्ञा at 5.1.3,
    #: असंज्ञा at 5.1.24 and 5.1.28, and 5.1.21's अशत, where the
    #: affix is refused if the thing meant IS the hundred.
    result: str = ""
    #: A class the base belongs to: शरीरावयव, संख्या, विकृति.
    of_samjna: str = ""
    #: The sound the base ends in — 5.1.2's उ, 5.1.22's शद्,
    #: 5.1.23's वतु.
    stem_final: str = ""
    #: How many vowels the base has. 5.1.39 wants द्व्यच्, which is
    #: the condition 4.4.7 stated of नौ and the reason पुत्र needs
    #: 5.1.40 to add anything to what it would already get.
    vowels: str = ""
    #: Which register the rule is confined to. 5.1.61 alone says
    #: छन्दसि, and the rest of the pāda is unrestricted — one column
    #: and not two flags, as in the two modules before this.
    usage: str = ""
    #: The LAST member of the compound the rule names — 5.1.9's भोग.
    uttarapada: str = ""
    #: What stands in FRONT — 5.1.28's अध्यर्ध and द्विगु, 5.1.30's
    #: द्वि and त्रि.
    pre: str = ""
    #: An आदेश the rule substitutes in the same act: नभ for नाभि and
    #: अनङ् for ऊधस् inside the गवादि list, प्रति for कार्षापण.
    adesa: str = ""
    #: An आगम added in the same act — 5.1.23's इट्.
    augment: str = ""
    #: Whether the base may stand in a compound. "no" at 5.1.20 and
    #: 5.1.21, where असमासे is stated and then carried.
    compounded: str = ""
    #: The PENULTIMATE sound of the base — उपधा, 1.1.65. 5.1.131
    #: wants a LIGHT one and 5.1.132 a य, and the column is the one
    #: each of the three pādas before this ended up needing.
    upadha: str = ""
    #: True where the rule REFUSES rather than supplies. 5.1.121 is
    #: the only one in the pāda, and it refuses the special affixes
    #: while leaving 5.1.119's त्व and तल् standing.
    refuses: bool = False
    optional: bool = False
    #: True where the rule takes the affix AWAY — 5.1.28 to 5.1.30,
    #: which are लुक् and not लुप्, so no gender or number is kept.
    lup: bool = False
    #: True where the row IS a heading rather than a rule under one.
    heading: bool = False
    #: True where the rule names only a SENSE and leaves the affix
    #: **यथाविहितम्** — as enjoined. 5.1.5, 5.1.12 and 5.1.16, and
    #: the resolver executes it by asking again without the sense,
    #: which is the same fall-through 4.3.25 uses.
    borrows: bool = False
    #: What the heading itself keeps out — 5.1.19's three.
    excludes: Tuple[str, ...] = ()
    excepts: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


KRITA_TABLE: Tuple[Krita, ...] = (
    Krita("5.1.1", gives="cha", heading=True,
          why="प्राक्क्रीताच्छः. **तेन क्रीतम् इति वक्ष्यति। "
              "प्रागेतस्मात् क्रीतसंशब्दनाद् यानित "
              "ऊर्ध्वमनुक्रमिष्यामः, छप्रत्ययस्तेष्वधिकृतो "
              "वेदितव्यः** — छ is the affix for every sense named "
              "from here to the rule that says क्रीत, unless a rule "
              "says otherwise. वत्सेभ्यो हितो **वत्सीयो** गोधुक्, a "
              "milkman kept for the calves; करभीय उष्ट्रः.\\n\\n"
              "**AND THE VṚTTI SAYS WHAT A प्राक्-HEADING MEASURES.** "
              "The rule could have been worded *before the ठञ्*, "
              "since 5.1.18 is where छ actually stops. It is not: "
              "**अर्थोऽवधित्वेन गृहीतः, न प्रत्ययः; तेन प्राक् ठञः छ "
              "इति नोक्तम्** — the SENSE is taken as the limit and "
              "not the affix. Every one of these headings names a "
              "sense-word, and this is the rule that says why"),
    Krita("5.1.2", gives="yat", stem_final="u", excepts=("5.1.1",),
          why="उगवादिभ्यो यत्, the उवर्णान्त half. **प्राक् "
              "क्रीतादित्येव** — the heading's senses are carried, "
              "and only the affix changes. छस्यापवादः. **शङ्कव्यं** "
              "दारु, wood for a peg; पिचव्यः कार्पासः; कमण्डलव्या "
              "मृत्तिका"),
    Krita("5.1.2", gives="yat", gana="gavādi", excepts=("5.1.1",),
          why="उगवादिभ्यो यत्, the गवादि half. **गव्यम्**; "
              "हविष्यम्.\\n\\n"
              "**AND THREE LATER RULES ARE BEATEN BY AN EARLIER "
              "ONE.** सनङ्गु is a kind of leather, so 5.1.15 "
              "चर्मणोऽञ् would take it by standing later; चरु is an "
              "oblation, so 5.1.4 would; सक्तु is a preparation of "
              "grain, so the अन्नविकारेभ्यश्च of the अपूपादि list "
              "would. **तत्र सर्वत्र पूर्वविप्रतिषेधेन यत् प्रत्यय "
              "एवेष्यते** — in every one of the three the EARLIER "
              "rule is wanted: सनङ्गव्यं चर्म, चरव्यास्तण्डुलाः, "
              "सक्तव्या धानाः.\\n\\n"
              "गो, हविस्, बर्हिस्, खट, अष्टका, युग, मेधा, स्रक्, "
              "नाभि, शुनि, ऊधस्, कूप, उदर, खर, स्खद, अक्षर, विष — "
              "गवादिः"),
    Krita("5.1.2", gives="yat", of=("nābhi",), adesa="nabha",
          excepts=("5.1.1",),
          why="उगवादिभ्यो यत्, the गवादि entry **नाभि नभं च** "
              "(ग०सू०१०८) — and a गण-entry that does two things at "
              "once. **नाभिशब्दो यत्प्रत्ययमुत्पादयति, नभं चादेशम् "
              "आपद्यते**: the word takes यत् AND becomes नभ. "
              "नाभये हितो **नभ्योऽक्षः**, an axle greased for the "
              "nave; नभ्यमञ्जनम्.\\n\\n"
              "**AND THE SUBSTITUTION IS TIED TO THE ENTRY, NOT TO "
              "THE WORD.** नाभि is also a part of the body, and as "
              "that it is taken by 5.1.6 शरीरावयवाद् यत् instead — "
              "same affix, different rule. **गवादिषु यता "
              "सन्नियुक्तो नभभावोऽत्र न भवति**: the नभ that is "
              "yoked to the गवादि यत् does not happen there, and "
              "the form is नाभये हितं **नाभ्यं** तैलम्. One word, "
              "two rules, and only one of them changes its shape",
          keeps_out="नाभ्यं तैलम्"),
    Krita("5.1.2", gives="yat", of=("śvan",), optional=True,
          excepts=("5.1.1",),
          why="उगवादिभ्यो यत्, the गवादि entry **शुनः संप्रसारणं "
              "वा च दीर्घत्वं तत्सन्नियोगेन चान्तोदात्तत्वम्** "
              "(ग०सू०१०९) — श्वन् takes संप्रसारण, optionally with "
              "lengthening, and an end-accent yoked to it: "
              "**शुन्यम्, शून्यम्**.\\n\\n"
              "**AND THE च OF THE ENTRY DOES A JOB.** Without it "
              "6.4.144 नस्तद्धिते would drop the न् of शुन् before "
              "the taddhita and there would be no न to lengthen "
              "around: **चकारस्यानुक्तसमुच्चयार्थत्वाद् नस्तद्धिते "
              "इति लोपो न स्यात्** — the च gathers in what is not "
              "said, and what it gathers in is the blocking of that "
              "elision"),
    Krita("5.1.2", gives="yat", of=("ūdhas",), adesa="anaṅ",
          excepts=("5.1.1",),
          why="उगवादिभ्यो यत्, the गवादि entry **ऊधसोऽनङ् च** "
              "(ग०सू०११०) — the same double duty नाभि had, with a "
              "different substitute. **ऊधन्यः**"),
    Krita("5.1.3", gives="yat", of=("kambala",), result="saṃjñā",
          excepts=("5.1.1",),
          why="कम्बलाच्च संज्ञायाम्, छस्यापवादः. यत् after कम्बल "
              "when the word is a NAME. **कम्बल्यम्** ऊर्णापलशतम्, "
              "a hundred palas of wool that go to make a blanket "
              "— and the name is of that quantity, not of the wool. "
              "संज्ञायामिति किम्? **कम्बलीया ऊर्णा**, wool for a "
              "blanket, which is not a name and so takes the "
              "heading's छ",
          keeps_out="कम्बलीया ऊर्णा"),
    Krita("5.1.4", gives="yat", of=("havis",), optional=True,
          excepts=("5.1.1",),
          why="विभाषा हविरपूपादिभ्यः, the हविस् half — and it names "
              "a CLASS and not the word. **हविर्विशेषवाचिभ्यः**: "
              "from the words that name particular oblations, "
              "optionally यत्. **आमिक्ष्यं दधि, आमिक्षीयं दधि**; "
              "पुरोडाश्यास्तण्डुलाः, पुरोडाशीयाः.\\n\\n"
              "**AND THE WORD हविस् ITSELF IS NOT OPTIONAL.** "
              "**हविश्शब्दात्तु गवादिपाठाद् नित्यमेव भवति** — हविस् "
              "stands in the गवादि list of 5.1.2, so it takes यत् "
              "always, and only the words for particular oblations "
              "get the choice"),
    Krita("5.1.4", gives="yat", gana="apūpādi", optional=True,
          excepts=("5.1.1",),
          why="विभाषा हविरपूपादिभ्यः, the अपूपादि half. **अपूप्यम्, "
              "अपूपीयम्**; तण्डुल्यम्, तण्डुलीयम्. अपूप, तण्डुल, "
              "अभ्यूष, पृथुक, अर्गल, मुसल, सूप, कटक, कर्णवेष्टक, "
              "किण्व, **अन्नविकारेभ्यश्च** (ग०सू०१११), पूप, स्थूणा, "
              "पीप, अश्व, पत्र — अपूपादिः. The last of the fourteen "
              "is not a word but a class: anything that is a "
              "PREPARATION OF FOOD joins the list"),
    Krita("5.1.5", sense="hita", case="caturthī", borrows=True,
          why="तस्मै हितम्. **तस्मा इति चतुर्थीसमर्थाद् हितम् "
              "इत्येतस्मिन्नर्थे यथाविहितं प्रत्ययो भवति** — from a "
              "base in the DATIVE, in the sense *good for that*, "
              "the affix as already enjoined. वत्सेभ्यो हितो गोधुक् "
              "**वत्सीयः**; पटव्यम्; गव्यम्; हविष्यम्; अपूप्यम्, "
              "अपूपीयम्.\\n\\n"
              "**यथाविहितम् IS A FALL-THROUGH, AND THE RESOLVER "
              "EXECUTES IT AS ONE.** The rule gives no affix of its "
              "own; it names a sense and sends the question back to "
              "whatever rule the base itself answers to — छ by the "
              "heading, यत् by 5.1.2, either by 5.1.4. The same "
              "device 4.3.25 used, and asking under this sense asks "
              "again without it.\\n\\n"
              "**AND THIS IS THE SŪTRA THAT BOUNDED यत्.** 4.4.75 "
              "प्राग्घिताद् यत् lifted the word हित out of THIS "
              "rule to fix its own limit, two pādas back and a "
              "chapter away. The debt that named it is paid here"),
    Krita("5.1.6", gives="yat", of_samjna="śarīrāvayava",
          sense="hita", case="caturthī", excepts=("5.1.1",),
          why="शरीरावयवाद् यत्, छस्यापवादः. **शरीरं प्राणिकायः** — "
              "a body is a living creature's frame, and from the "
              "words that name a PART of one, यत्. **दन्त्यम्**, "
              "good for the teeth; कण्ठ्यम्, ओष्ठ्यम्, नाभ्यम्, "
              "नस्यम्. A rule that names no word and no list, only "
              "what the word must mean"),
    Krita("5.1.7", gives="yat", gana="khalādi", sense="hita",
          case="caturthī", excepts=("5.1.1",),
          why="खलयवमाषतिलवृषब्रह्मणश्च, छस्यापवादः. खलाय हितं "
              "**खल्यम्**; यव्यम्, माष्यम्, तिल्यम्, वृष्यम्, "
              "ब्रह्मण्यम्.\\n\\n"
              "**AND TWO OF THE SIX ARE NOT WHAT THEY LOOK LIKE.** "
              "वृष्णे हितम् and ब्राह्मणेभ्यो हितम् — for the BULL, "
              "for the BRĀHMAṆAS — do not take this affix at all: "
              "**वाक्यमेव भवति; छप्रत्ययोऽपि न भवति, अनभिधानात्**, "
              "the phrase stands, and not even the heading's छ "
              "comes, because the language does not say it that "
              "way. So वृष is the plant and ब्रह्मन् the sacred "
              "word, not the animal and not the priest.\\n\\n"
              "**चकारोऽनुक्तसमुच्चयार्थः** — and the च gathers in "
              "what is not listed: रथाय हिता **रथ्या**",
          keeps_out="वृष्णे हितम्, ब्राह्मणेभ्यो हितम्"),
    Krita("5.1.8", gives="thyan", of=("aja", "avi"), sense="hita",
          case="caturthī", excepts=("5.1.1",),
          why="अजाविभ्यां थ्यन्, छस्यापवादः. **अजथ्या** यूथिः, a "
              "herd kept for the goats; अविथ्या"),
    Krita("5.1.9", gives="kha", of=("ātman", "viśvajana"),
          sense="hita", case="caturthī", excepts=("5.1.1",),
          why="आत्मन्विश्वजनभोगोत्तरपदात् खः, छस्यापवादः; the "
              "named-word half. आत्मने हितम् **आत्मनीनम्**; "
              "विश्वजनेभ्यो हितं **विश्वजनीनम्**.\\n\\n"
              "**AND THE RULE SPELLS आत्मन् OUT TO TEACH ITS OWN "
              "SCOPE.** 6.4.134 would drop that न्, so the rule "
              "could have said आत्म; it does not: **आत्मन्निति "
              "नलोपो न कृतः प्रकृतिपरिमाणज्ञापनार्थम्** — the "
              "elision is left undone to show how much of the word "
              "is meant. **तेनोत्तरपदग्रहणं भोगशब्देनैव "
              "संबध्यते, न तु प्रत्येकम्**: the word उत्तरपद goes "
              "with भोग ALONE and not with all three, so आत्मन् and "
              "विश्वजन are taken whole and not as compound-ends. "
              "(6.4.169 आत्माध्वानौ खे then keeps आत्मन् unchanged "
              "before this very affix.)\\n\\n"
              "**AND ONLY ONE KIND OF COMPOUND QUALIFIES.** "
              "**कर्मधारयादेवेष्यते; षष्ठीसमासाद् बहुव्रीहेश्च छ एव "
              "भवति** — from a कर्मधारय, ख; from a genitive "
              "तत्पुरुष or a बहुव्रीहि, the heading's छ: "
              "विश्वजनाय हितं **विश्वजनीयम्**",
          keeps_out="विश्वजनीयम्"),
    Krita("5.1.9", gives="kha", uttarapada="bhoga", sense="hita",
          case="caturthī", excepts=("5.1.1",),
          why="आत्मन्विश्वजनभोगोत्तरपदात् खः, the भोगोत्तरपद half — "
              "and here the word भोग means the BODY. "
              "**मातृभोगीणः**, पितृभोगीणः.\\n\\n"
              "**AND THE COMPOUND IS REQUIRED, NOT INCIDENTAL.** "
              "**केवलेभ्यो मात्रादिभ्यश्छ एव भवति** — from मातृ and "
              "पितृ alone it is the heading's छ: मात्रीयम्, "
              "पित्रीयम्. Two vārttikas press the point: "
              "**राजाचार्याभ्यां तु नित्यम्** — with राजन् and "
              "आचार्य the compound is obligatory, "
              "**भोगोत्तरपदाभ्यामेव खः प्रत्यय इष्यते, न "
              "केवलाभ्याम्**, and **केवलाभ्यां वाक्यमेव भवति**: "
              "alone they take no affix whatever, only the phrase "
              "राज्ञे हितम्. राजभोगीनः; and **आचार्यादणत्वं च** "
              "adds a vowel-strengthening — आचार्यभोगीनः",
          keeps_out="राज्ञे हितम्, आचार्याय हितम्"),
    Krita("5.1.9", gives="kha", of=("pañcajana",), sense="hita",
          case="caturthī", excepts=("5.1.1",),
          why="आत्मन्विश्वजनभोगोत्तरपदात् खः — **पञ्चजनाद् "
              "उपसंख्यानम्**, a vārttika adding a fourth base. "
              "**पञ्चजनीनम्**, and **अत्रापि कर्मधारयादिष्यते**: "
              "here too only from a कर्मधारय, **अन्यत्र "
              "पञ्चजनीयम्**",
          keeps_out="पञ्चजनीयम्"),
    Krita("5.1.9", gives="ṭhañ", also_gives=("kha",),
          of=("sarvajana",), sense="hita", case="caturthī",
          excepts=("5.1.1",),
          why="आत्मन्विश्वजनभोगोत्तरपदात् खः — **सर्वजनाट् ठञ् खश् "
              "च**, a vārttika giving TWO affixes where the sūtra "
              "gives one. **सार्वजनिकम्, सर्वजनीनम्**; and the "
              "same restriction, **अत्रापि कर्मधारयादेव — "
              "सर्वजनीयमन्यत्र**",
          keeps_out="सर्वजनीयम्"),
    Krita("5.1.9", gives="ṭhañ", of=("mahājana",), sense="hita",
          case="caturthī", excepts=("5.1.1",),
          why="आत्मन्विश्वजनभोगोत्तरपदात् खः — **महाजनाद् नित्यं "
              "ठञ् वक्तव्यः**, and this one gives ठञ् ALONE where "
              "the rule before it gave both. महाजनाय हितं "
              "**माहाजनिकम्**, and **तत्पुरुषादेव** — from a "
              "तत्पुरुष only, where the others wanted a कर्मधारय. "
              "**बहुव्रीहेस्तु छ एव भवति**: महाजनीयम्. Four "
              "vārttikas on one sūtra, and each names a different "
              "compound",
          keeps_out="महाजनीयम्"),
    Krita("5.1.10", gives="ṇa", of=("sarva",), sense="hita",
          case="caturthī", excepts=("5.1.1",),
          why="सर्वपुरुषाभ्यां णढञौ, छस्यापवादः; the सर्व member. "
              "**यथासंख्यम्** — the two affixes are matched to the "
              "two bases in order, so सर्व takes ण and पुरुष ढञ्. "
              "सर्वस्मै हितं **सार्वम्**. **सर्वाद् णस्य वा "
              "वचनम्**: a vārttika makes it optional — सर्वीयम्",
          optional=True),
    Krita("5.1.10", gives="ḍhañ", of=("puruṣa",), sense="hita",
          case="caturthī", excepts=("5.1.1",),
          why="सर्वपुरुषाभ्यां णढञौ, the पुरुष member. "
              "**पौरुषेयम्**.\\n\\n"
              "**AND A VĀRTTIKA GIVES THE SAME AFFIX FOUR MORE "
              "SENSES.** **पुरुषाद् वधविकारसमूहतेनकृतेष्विति "
              "वक्तव्यम्** — a killing, an alteration, a group, and "
              "a thing MADE BY: पौरुषेयो वधः, पौरुषेयो विकारः, "
              "पौरुषेयः समूहः, and पौरुषेयो ग्रन्थः, a book made by "
              "a man. One form for five senses"),
    Krita("5.1.11", gives="khañ", of=("māṇava", "caraka"),
          sense="hita", case="caturthī", excepts=("5.1.1",),
          why="माणवचरकाभ्यां खञ्, छस्यापवादः. माणवाय हितं "
              "**माणवीनम्**; चारकीणम्"),
    Krita("5.1.12", sense="tadartha", case="caturthī", borrows=True,
          of_samjna="vikṛti",
          why="तदर्थं विकृतेः प्रकृतौ. **प्रकृतिरुपादानकारणम्, "
              "तस्यैव उत्तरमवस्थान्तरं विकृतिः** — the प्रकृति is "
              "the material a thing is made OF, the विकृति the "
              "later state of that same material. From the word for "
              "the FINISHED thing, in the sense of the MATERIAL: "
              "अङ्गारेभ्यो हितानि काष्ठानि **अङ्गारीयाणि "
              "काष्ठानि**, wood for charcoal; प्राकारीया इष्टकाः; "
              "शङ्कव्यं दारु.\\n\\n"
              "**AND तदर्थम् IS WHAT KEEPS IT FROM BEING MERE "
              "SEQUENCE.** **तदर्थग्रहणेन प्रकृतेरनन्यार्थताख्यायते; "
              "न प्रकृतिविकारसंभवमात्रे प्रत्ययः** — the material "
              "must be FOR nothing else. यवानां धानाः, धानानां "
              "सक्तवः take nothing: barley does become groats and "
              "groats do become meal, but there **प्रकृत्यन्तर"
              "निवृत्तिर्विवक्षिता न तादर्थ्यम्**, what is meant is "
              "*from THIS grain and not another*, not purpose.\\n\\n"
              "**AND EACH OF THE THREE WORDS IS TESTED.** "
              "विकृतेरिति किम्? **उदकार्थः कूपः** — a well is where "
              "water comes to be, so a well is water's source, "
              "**न तूदकं तस्य विकृतिः, अत्यन्तभेदात्**, but water "
              "is not the well's later state, the two being "
              "altogether different things. प्रकृताविति किम्? "
              "**अस्यर्था कोशी** — a scabbard is for a sword, and a "
              "sword IS a modification of iron, but the scabbard is "
              "not what the sword was made of.\\n\\n"
              "The affix is यथाविहितम् again, and the dative comes "
              "not from the rule but from the sense: **प्रत्ययार्थस्य "
              "च तदर्थत्वे सति सामर्थ्याल् लभ्या चतुर्थी "
              "समर्थविभक्तिः**. **केचित् तु तस्मै हितम् "
              "इत्यनुवर्तयन्ति** — and some carry 5.1.5 down instead",
          keeps_out="यवानां धानाः, उदकार्थः कूपः, अस्यर्था कोशी"),
    Krita("5.1.13", gives="ḍhañ", gana="chadirādi", sense="tadartha",
          case="caturthī", excepts=("5.1.1",),
          why="छदिरुपधिबलेर्ढञ्, छस्यापवादः. **छादिषेयाणि तृणानि**, "
              "grass for a roof; औपधेयं दारु; बालेयास्तण्डुलाः.\\n\\n"
              "**AND ONE OF THE THREE ALREADY CARRIES AN AFFIX.** "
              "**उपधीयत इत्युपधिः रथाङ्गम्** — an उपधि is a part of "
              "a chariot, named from being laid on, and "
              "**उपधिशब्दात् स्वार्थे प्रत्ययः**: the affix here is "
              "in its OWN sense, so **औपधेयमपि तदेव दारु** means "
              "the same wood over again"),
    Krita("5.1.14", gives="ñya", of=("ṛṣabha", "upānah"),
          sense="tadartha", case="caturthī", excepts=("5.1.1",),
          why="ऋषभोपानहोर्ञ्यः, छस्यापवादः. **आर्षभ्यो वत्सः**, a "
              "calf to become a bull; औपानह्यो मुञ्जः, grass for a "
              "shoe.\\n\\n"
              "**AND IT BEATS THE RULE THAT STANDS AFTER IT.** "
              "5.1.15 चर्मणोऽञ् would take leather made into shoes "
              "by standing later; it does not: **चर्मण्यपि "
              "प्रकृतित्वेन विवक्षिते पूर्वविप्रतिषेधाद् अयमेव "
              "इष्यते** — even where the material meant is leather, "
              "THIS rule is wanted by पूर्वविप्रतिषेध. "
              "**औपानह्यं चर्म**"),
    Krita("5.1.15", gives="añ", of=("carman",), sense="tadartha",
          case="caturthī", excepts=("5.1.1",),
          why="चर्मणोऽञ्, छस्यापवादः — and the genitive in the "
              "sūtra is doing something the other rules' ablatives "
              "do not. **चर्मण इति षष्ठी; चर्मणो या विकृतिः "
              "तद्वाचिनः प्रातिपदिकाद् अञ्**: the affix comes not "
              "after the word चर्मन् but after the word for "
              "WHATEVER IS MADE of leather. **वार्ध्रं चर्म**, "
              "वारत्रं चर्म — a strap's leather, a thong's"),
    Krita("5.1.16", sense="tadasya-syāt", case="prathamā",
          borrows=True,
          why="तदस्य तदस्मिन् स्यादिति. **तदिति प्रथमा "
              "समर्थविभक्तिः, अस्येति प्रत्ययार्थः, स्यादिति "
              "प्रकृतिविशेषणम्** — the base stands in the "
              "NOMINATIVE, and the affix reports *this would be "
              "OF that* or *would be IN that*. प्राकार आसाम् "
              "इष्टकानां स्यात् **प्राकारीया इष्टकाः**, bricks that "
              "might make a rampart; प्रासादीयं दारु; प्राकारोऽस्मिन् "
              "देशे स्यात् **प्राकारीयो देशः**.\\n\\n"
              "**AND स्यात् IS A REAL OPTATIVE, NOT A FIGURE.** "
              "**स्यादिति संभावनायां लिङ्, संभावनेऽलमिति चेत् "
              "इत्यादिना** (3.3.154) — the mood is the one for "
              "what might be, and what makes it likely is stated "
              "each time: **इष्टकानां बहुत्वेन तत् संभाव्यते**, by "
              "the sheer number of the bricks; **देशस्य च गुणेन**, "
              "by the quality of the ground.\\n\\n"
              "**AND इति IS THE WORD THAT KEEPS THE RULE HONEST.** "
              "**इतिकरणो विवक्षार्थः** — it marks what the speaker "
              "MEANS to say. Otherwise प्रासादो देवदत्तस्य स्यात्, "
              "*Devadatta could come by a palace*, would take the "
              "affix too, and it does not.\\n\\n"
              "**AND THE DOUBLED तद् IS A LESSON IN METHOD.** "
              "**द्विस्तद्ग्रहणं न्यायप्रदर्शनार्थम् — अनेकस्मिन् "
              "प्रत्ययार्थे प्रत्येकं समर्थविभक्तिः संबन्धनीया**: "
              "when one rule states several senses, the "
              "case-relation must be joined to EACH of them "
              "separately, and saying तद् twice shows how. "
              "**प्रकृतिविकारभावस्तादर्थ्यं चेह न विवक्षितम्; किं "
              "तर्हि? योग्यतामात्रम्** — neither material nor "
              "purpose is meant here, only fitness, "
              "**तेन पूर्वस्यायमविषयः**",
          keeps_out="प्रासादो देवदत्तस्य स्यात्"),
    Krita("5.1.17", gives="ḍhañ", of=("parikhā",),
          sense="tadasya-syāt", case="prathamā", excepts=("5.1.1",),
          why="परिखाया ढञ्, छस्यापवादः. **पारिखेयी भूमिः**, ground "
              "where a moat might go.\\n\\n"
              "**AND THE HEADING CLOSES HERE, IN THE WORDS THE "
              "PĀDA BEFORE USED TWICE.** **छयतोः पूर्णोऽवधिः। इतः "
              "परमन्यः प्रत्ययो विधीयते** — the limit of छ and of "
              "यत् both is complete, and from here another affix is "
              "enjoined. 4.4.74 said it of ठक् and 4.4.144 of यत्, "
              "word for word. So छ's marker is 5.1.37, twenty "
              "sūtras further on, and its last rule is this one, "
              "because 5.1.18 opens ठञ् inside the range"),
    Krita("5.1.18", gives="ṭhañ", heading=True,
          why="प्राग्वतेष्ठञ्. **तेन तुल्यं क्रिया चेद् वतिरिति "
              "वक्ष्यति। प्रागेतस्माद् वतिसंशब्दनाद् यानित "
              "ऊर्ध्वमनुक्रमिष्यामः, ठञ् प्रत्ययस्तेष्वधिकृतो "
              "वेदितव्यः** — ठञ् is the affix from here to the rule "
              "that says वति, 5.1.115. **पारायणिकः, तौरायणिकः, "
              "चान्द्रायणिकः** (5.1.72).\\n\\n"
              "**AND THIS IS WHAT 4.3.156 WAS WAITING FOR.** That "
              "rule's अतिदेश pointed forward out of its own pāda to "
              "this heading; the debt was written as a test "
              "asserting this sūtra was ABSENT, and it comes due "
              "here. The fourth of the great प्राक्-headings, and "
              "the second one this chapter opens"),
    Krita("5.1.19", gives="ṭhak",
          heading=True, excepts=("5.1.18",),
          excludes=("gopuccha", "saṃkhyā", "parimāṇa"),
          why="आर्हादगोपुच्छसंख्यापरिमाणाट्ठक्. **तदर्हतीति "
              "वक्ष्यति। आ एतस्माद् अर्हसंशब्दनाद् यानित "
              "ऊर्ध्वमनुक्रमिष्यामः, ठक् प्रत्ययस्तेष्वधिकृतो "
              "वेदितव्यो गोपुच्छादीन् वर्जयित्वा** — ठक् for every "
              "sense named from here to 5.1.63, the three excepted "
              "bases aside. **ठञधिकारमध्ये तदपवादः ठग् विधीयते**: a "
              "heading enjoined INSIDE another heading, as its "
              "exception. तेन क्रीतं **नैष्किकम्**, पाणिकम्.\\n\\n"
              "**AND THE आ IS NOT प्राक्.** **अभिविधावयमाकारः, "
              "तेनार्हत्यर्थेऽपि ठग् भवत्येव** — this आ is an "
              "अभिविधि, an inclusive limit, so ठक् applies in the "
              "sense of अर्हति TOO. Every other great heading stops "
              "SHORT of the sūtra that names it; this one reaches "
              "that sūtra and takes it in.\\n\\n"
              "**AND THE THREE EXCEPTIONS NEED FOUR TERMS TO "
              "SEPARATE.** गोपुच्छेन क्रीतं **गौपुच्छिकम्**, "
              "षाष्टिकम् for a numeral, प्रास्थिकम् and कौडविकम् "
              "for a measure — all ठञ् by the heading above. And "
              "संख्यापरिमाणयोः को विशेषः? **भेदगणनं संख्या "
              "एकत्वादिः; गुरुत्वमानमुन्मानं पलादि; आयाममानं "
              "प्रमाणं वितस्त्यादि; आरोहपरिणाहमानं परिमाणं "
              "प्रस्थादि** — counting, weight, length, and girth, "
              "of which the rule excepts the first and the last "
              "and leaves the middle two inside",
          keeps_out="गौपुच्छिकम्, षाष्टिकम्, प्रास्थिकम्"),
    Krita("5.1.20", gives="ṭhak", gana="niṣkādi", compounded="no", excepts=("5.1.18",),
          why="असमासे निष्कादिभ्यः, ठञोऽपवादः. **आर्हादित्येव** — "
              "the आर्हीय senses are carried. **नैष्किकम्**, "
              "पाणिकम्, पादिकम्, माषिकम्. निष्क, पण, पाद, माष, "
              "वाह, द्रोण, षष्टि — निष्कादिः.\\n\\n"
              "**असमास इति किम्?** द्विनैष्किकम्, त्रिनैष्किकम् — "
              "in a compound it is the heading's ठञ् instead, and "
              "7.3.17 then strengthens the LATTER member.\\n\\n"
              "**AND THE WORD असमासे IS A ज्ञापक FOR THE WHOLE "
              "HEADING.** It should be needless, since **ग्रहणवता "
              "प्रातिपदिकेन तदन्तविधिः प्रतिषिध्यते** — a rule "
              "naming a word does not reach compounds ending in it. "
              "That it is said anyway tells you the opposite holds "
              "elsewhere: **निष्कादिष्वसमासग्रहणं ज्ञापकं पूर्वत्र "
              "तदन्ताप्रतिषेधस्य**. So गव्यम् and सुगव्यम् and "
              "अतिसुगव्यम् by 5.1.2; यवापूप्यम् by 5.1.4; "
              "राजदन्त्यम् by 5.1.6 — all of them compounds, all of "
              "them taken.\\n\\n"
              "**AND FROM HERE ON IT HOLDS ONLY OF NUMERALS, AND "
              "ONLY WITHOUT ELISION.** **प्राग् वतेः "
              "संख्यापूर्वपदानां तदन्तग्रहणमलुकि** (वा० ५.१.२०): "
              "द्वैपारायणिकः, त्रैपारायणिकः. But द्विशूर्पेण "
              "क्रीतम् is **द्विशौर्पिकम्** and not by 5.1.26, "
              "because द्विशूर्पम् already had its affix removed — "
              "**लुगन्तायास्तु प्रकृतेर्नेष्यते**",
          keeps_out="द्विनैष्किकम्, द्विशौर्पिकम्"),
    Krita("5.1.21", gives="ṭhan", also_gives=("yat",), of=("śata",), compounded="no",
          result="aśata", excepts=("5.1.22",),
          why="शताच्च ठन्यतावशते, कनोऽपवादः — and the exception is "
              "of the NEXT rule, not of the heading, since शत is a "
              "numeral and 5.1.22 would take it. शतेन क्रीतं "
              "**शतिकम्, शत्यम्**.\\n\\n"
              "**अशत इति किम्?** शतं परिमाणमस्य **शतकं** निदानम् — "
              "where the thing meant IS the hundred, the affix is "
              "refused, because **प्रत्ययार्थोऽत्र संघः शतमेव "
              "वस्तुतः प्रकृत्यर्थाद् न भिद्यते**: what the affix "
              "would report does not differ from what the base "
              "already says.\\n\\n"
              "**AND THE TEST IS WHETHER THE WORD ITSELF SAYS IT.** "
              "शतेन क्रीतं **शत्यं शाटकशतम्** is allowed, though a "
              "hundred is meant twice over — **वाक्येन ह्यत्र "
              "प्रत्ययार्थस्य तत्त्वं गम्यते, न श्रुत्या**, the "
              "identity is got from the SENTENCE and not from the "
              "word's own sound. **शतप्रतिषेधेऽन्यशतत्वेऽप्रतिषेधः** "
              "(वा० ५.१.२१): the refusal does not apply when it is "
              "a different hundred.\\n\\n"
              "**चकारोऽसमास इत्यनुकर्षणार्थः** — and the च drags "
              "असमासे down from the rule before, though the "
              "vārttika at 5.1.20 lets a numeral-compound in "
              "anyway: द्विशतेन क्रीतं द्विशतकम्, त्रिशतकम्",
          keeps_out="शतकं निदानम्"),
    Krita("5.1.22", gives="kan", of_samjna="saṃkhyā", excepts=("5.1.18",),
          why="संख्याया अतिशदन्तायाः कन्, ठञोऽपवादः. From a NUMERAL "
              "— but not from ति, and not from one ending in शद्. "
              "पञ्चभिः क्रीतः **पञ्चकः** पटः; बहुकः, गणकः.\\n\\n"
              "**अतिशदन्ताया इति किम्?** साप्ततिकम्, "
              "चात्वारिंशत्कम् — seventy ends in ति and forty in "
              "शद्, so both fall back on the heading's ठञ्.\\n\\n"
              "**AND THE ति EXCEPTED IS A MEANINGFUL ONE.** "
              "**अर्थवतस्तिशब्दस्य ग्रहणाद् डतेः पर्युदासो न "
              "भवति** — the exclusion takes the ति that MEANS "
              "something, so the डति of कति is untouched: "
              "**कतिकः**",
          keeps_out="साप्ततिकम्, चात्वारिंशत्कम्"),
    Krita("5.1.23", gives="kan", augment="iṭ", stem_final="vatu", optional=True,
          why="वतोरिड्वा — and the rule adds nothing but an आगम. "
              "**वत्वन्तस्य संख्यात्वात् कन् सिद्ध एव, तस्य "
              "त्वनेन वा इडागमो विधीयते**: a word ending in वतु is "
              "already a numeral, so 5.1.22 gives it कन् without "
              "help; all this rule does is put इट् before that कन्, "
              "optionally. **तावतिकः, तावत्कः**; यावतिकः, "
              "यावत्कः"),
    Krita("5.1.24", gives="ḍvun", of=("viṃśati", "triṃśat"), result="asaṃjñā",
          excepts=("5.1.22",),
          why="विंशतित्रिंशद्भ्यां ड्वुन्नसंज्ञायाम्. **विंशकः, "
              "त्रिंशकः** — and 6.4.142 ति विंशतेर्डिति drops the "
              "ति of विंशति before this ड-marked affix, which is "
              "what the ड is for.\\n\\n"
              "**असंज्ञायामिति किम्?** विंशतिकम्, त्रिंशत्कम्.\\n\\n"
              "**AND THAT COUNTER-EXAMPLE RAISES A PROBLEM THE "
              "VṚTTI SOLVES BY SPLITTING THE RULE.** How can कन् "
              "come there at all, when 5.1.22 excepts what ends in "
              "ति and in शद्, and these two do? "
              "**योगविभागः करिष्यते — विंशतित्रिंशद्भ्यां कन् "
              "प्रत्ययो भवति, ततो ड्वुन्नसंज्ञायाम् इति**: the rule "
              "is read as two, the first restoring कन् to just "
              "these two words against the exception, the second "
              "giving ड्वुन् where they are not names",
          keeps_out="विंशतिकम्, त्रिंशत्कम्"),
    Krita("5.1.25", gives="ṭiṭhan", of=("kaṃsa",), excepts=("5.1.18",),
          why="कंसाट्टिठन्, ठञोऽपवादः — and every letter of the "
              "affix's name is accounted for. **टकारो ङीबर्थः** — "
              "the ट makes the feminine take ङीप् (4.1.15); "
              "**इकार उच्चारणार्थः** — the इ is only so the thing "
              "can be pronounced; **नकारः स्वरार्थः** — the न is "
              "for the accent. **कंसिकः, कंसिकी**.\\n\\n"
              "Three vārttikas add bases: **अर्धाच्चेति वक्तव्यम्** "
              "— अर्धिकः, अर्धिकी; **कार्षापणाट् टिठन् वक्तव्यः** — "
              "कार्षापणिकः, कार्षापणिकी; and **प्रतिशब्दश्चास्यादेशो "
              "वा वक्तव्यः**, which lets प्रति stand in for "
              "कार्षापण: **प्रतिकः, प्रतिकी**"),
    Krita("5.1.25", gives="ṭiṭhan", of=("kārṣāpaṇa",),
          adesa="prati",
          optional=True, excepts=("5.1.18",),
          why="कंसाट्टिठन् — the vārttika base कार्षापण, held "
              "apart because it carries a substitution the others "
              "do not. **कार्षापणिकः**, and optionally "
              "**प्रतिकः** by प्रतिशब्दश्चास्यादेशो वा. The "
              "substitute matters again at 5.1.29, where the "
              "elision is optional and this replacement is "
              "optional inside the non-eliding half"),
    Krita("5.1.26", gives="añ", of=("śūrpa",), optional=True, excepts=("5.1.18",),
          why="शूर्पादञन्यतरस्याम्, ठञोऽपवादः — and an अपवाद that "
              "leaves its own exception standing. **पक्षे सोऽपि "
              "भवति**: in the other alternative the ठञ् comes too. "
              "शूर्पेण क्रीतं **शौर्पम्, शौर्पिकम्**"),
    Krita("5.1.27", gives="aṇ", gana="śatamānādi", excepts=("5.1.18", "5.1.19"),
          why="शतमानविंशतिकसहस्रवसनादण् — and this one displaces "
              "BOTH the heading above it and the heading it stands "
              "under: **ठक्ठञोरपवादः**. शतमानेन क्रीतं "
              "**शातमानं** शतम्; वैंशतिकम्, साहस्रम्, वासनम्"),
    Krita("5.1.28", lup=True, pre="adhyardha", result="asaṃjñā",
          why="अध्यर्धपूर्वद्विगोर्लुगसंज्ञायाम्, the अध्यर्धपूर्व "
              "half. **आर्हादित्येव** — and what is removed is the "
              "आर्हीय affix, whichever of them came. "
              "**अध्यर्धकंसम्, अध्यर्धशूर्पम्**.\\n\\n"
              "**असंज्ञायामिति किम्?** पाञ्चलोहितिकम्, "
              "पाञ्चकलापिकम् — and the word असंज्ञा qualifies the "
              "DERIVED form and not the base: "
              "**प्रत्ययान्तस्य विशेषणमसंज्ञाग्रहणम्, न चेत् "
              "प्रत्ययान्तं संज्ञेति**.\\n\\n"
              "**AND अध्यर्ध IS NAMED SEPARATELY THOUGH IT IS A "
              "NUMERAL ALREADY.** Why? **ज्ञापकार्थम्, क्वचिदस्य "
              "संख्याकार्यं न भवति** — to let you know that "
              "somewhere it does NOT act as one, and 5.4.17 is "
              "where",
          keeps_out="पाञ्चलोहितिकम्"),
    Krita("5.1.28", lup=True, pre="dvigu", result="asaṃjñā",
          why="अध्यर्धपूर्वद्विगोर्लुगसंज्ञायाम्, the द्विगु half. "
              "**द्विकंसम्, त्रिकंसम्; द्विशूर्पम्, त्रिशूर्पम्**. "
              "And this is the elision 5.1.20's vārttika excepts: "
              "once it has run, a rule naming शूर्प no longer "
              "reaches द्विशूर्प, **लुगन्तायास्तु प्रकृतेर्नेष्यते**"),
    Krita("5.1.29", lup=True, optional=True,
          of=("kārṣāpaṇa", "sahasra"), pre="adhyardha", excepts=("5.1.28",),
          why="विभाषा कार्षापणसहस्राभ्याम् — and it does not add an "
              "elision, it loosens one. **पूर्वेण लुकि नित्ये "
              "प्राप्ते विकल्प्यते**: the rule before made it "
              "obligatory, and here it becomes a choice. "
              "**अध्यर्धकार्षापणम्, अध्यर्धकार्षापणिकम्**; "
              "द्विकार्षापणम्, द्विकार्षापणिकम्.\\n\\n"
              "**AND THE OPTION IS DOUBLE.** "
              "**औपसंख्यानिकस्य टिठनो लुक्; अलुक्पक्षे च "
              "प्रतिरादेशो विकल्पितः** — the टिठन् that a vārttika "
              "gave at 5.1.25 is what drops, and in the "
              "non-dropping alternative the प्रति-substitution is "
              "itself optional: अध्यर्धप्रतिकम्, द्विप्रतिकम्.\\n\\n"
              "सहस्रात् — **अध्यर्धसहस्रम्, अध्यर्धसाहस्रम्**, and "
              "in the non-eliding half 7.3.15 strengthens the "
              "latter member. **सुवर्णशतमानयोरुपसंख्यानम्** adds "
              "two more: अध्यर्धसुवर्णम्, अध्यर्धसौवर्णिकम्; "
              "अध्यर्धशतमानम्, अध्यर्धशातमानम्"),
    Krita("5.1.30", lup=True, optional=True, of=("niṣka",),
          pre="dvi-tri",
          excepts=("5.1.28",),
          why="द्वित्रिपूर्वान्निष्कात्. **द्विगोरित्येव** — only "
              "from a द्विगु, and only one whose first member is "
              "two or three. **द्विनिष्कम्, द्विनैष्किकम्**; "
              "त्रिनिष्कम्, त्रिनैष्किकम्. **बहुपूर्वाच्चेति "
              "वक्तव्यम्**: and बहु as well — बहुनिष्कम्, "
              "बहुनैष्किकम्, where 7.3.17 gives the vṛddhi in the "
              "non-eliding half"),

    Krita("5.1.31", lup=True, optional=True, of=("bista",),
          pre="dvi-tri", excepts=("5.1.28",),
          why="बिस्ताच्च. **द्वित्रिपूर्वादिति चकारेणानुकृष्यते** — "
              "the च drags द्वित्रिपूर्व down from the rule before, "
              "so this is the same option over a different word. "
              "**द्विबिस्तम्, द्विबैस्तिकम्**; त्रिबिस्तम्, "
              "त्रिबैस्तिकम्; बहुबिस्तम्, बहुबैस्तिकम्"),
    Krita("5.1.32", gives="kha", pre="adhyardha",
          uttarapada="viṃśatika", excepts=("5.1.18",),
          why="विंशतिकात् खः. From a compound beginning with अध्यर्ध "
              "or a द्विगु and ENDING in विंशतिक. "
              "**अध्यर्धविंशतिकीनम्, द्विविंशतिकीनम्**.\n\n"
              "**AND THE AFFIX SURVIVES THE ELISION THAT WOULD HAVE "
              "TAKEN IT.** 5.1.28 removes the आर्हीय affix after "
              "exactly these compounds, and this one is given after "
              "them too — so it would be removed the moment it "
              "arrived. **विधानसामर्थ्यादस्य लुङ् न भवति**: the "
              "sheer force of its being enjoined here keeps it. An "
              "argument the pāda will use twice more"),
    Krita("5.1.33", gives="īkan", pre="adhyardha",
          uttarapada="khārī", excepts=("5.1.18",),
          why="खार्या ईकन्. **अध्यर्धखारीकम्, द्विखारीकम्**, and "
              "two vārttikas widen it in both directions: "
              "**केवलायाश्चेति वक्तव्यम्** — from the bare word too, "
              "खारीकम्; **काकिण्याश्चोपसंख्यानम्** — and from "
              "काकिणी, अध्यर्धकाकिणीकम्, द्विकाकिणीकम्, and "
              "**केवलायाश्च**, काकिणीकम्"),
    Krita("5.1.34", gives="yat", pre="adhyardha",
          uttarapada="paṇa-pāda-māṣa-śata", excepts=("5.1.18",),
          why="पणपादमाषशताद् यत्. **अध्यर्धपण्यम्, द्विपण्यम्**; "
              "अध्यर्धमाष्यम्; अध्यर्धशत्यम्.\n\n"
              "**AND पाद KEEPS ITS SHAPE HERE BECAUSE IT IS A "
              "MEASURE AND NOT A FOOT.** 6.3.53 पद्यत्यतदर्थे would "
              "turn पाद into पद् before a य-affix; it does not — "
              "**प्राण्यङ्गस्य स इष्यते, इदं तु परिमाणम्**, that "
              "substitution is wanted for the limb of a living "
              "thing, and this is a unit of measure. "
              "**अध्यर्धपाद्यम्**, not अध्यर्धपद्यम्",
          keeps_out="अध्यर्धपद्यम्"),
    Krita("5.1.35", gives="yat", of=("śāṇa",), pre="adhyardha",
          optional=True, excepts=("5.1.18",),
          why="शाणाद् वा, ठञोऽपवादः — and the alternative is not "
              "silence. **पक्षे सोऽपि भवति, तस्य च लुक्**: in the "
              "other half the ठञ् comes and is then removed by "
              "5.1.28, so both members of the option are visible. "
              "**अध्यर्धशाण्यम्, अध्यर्धशाणम्**; द्विशाण्यम्, "
              "द्विशाणम्. **शताच्चेति वक्तव्यम्** adds शत: "
              "अध्यर्धशत्यम्, अध्यर्धशतम्"),
    Krita("5.1.36", gives="aṇ", also_gives=("yat",), of=("śāṇa",),
          pre="dvi-tri", optional=True, excepts=("5.1.18",),
          why="द्वित्रिपूर्वाद् अण् च. **शाणाद् वेत्येव** — and the "
              "च brings the यत् of the rule before along, so THREE "
              "forms stand together: **तेन त्रैरूप्यं संपद्यते** — "
              "द्वैशाणम्, द्विशाण्यम्, द्विशाणम्; त्रैशाणम्, "
              "त्रिशाण्यम्, त्रिशाणम्.\n\n"
              "And 7.3.17 names शाण in its own exclusion, "
              "**परिमाणान्तस्यासंज्ञाशाणयोः**, so the strengthening "
              "falls on the FIRST syllable and not the last: "
              "**आदिवृद्धिरेव भवति**"),
    Krita("5.1.37", sense="krīta", case="tṛtīyā", borrows=True,
          why="तेन क्रीतम् — and the vṛtti here states the "
              "architecture of the whole section. **ठञादयस्त्रयोदश "
              "प्रत्ययाः प्रकृताः। तेषामितः प्रभृति समर्थविभक्तयः "
              "प्रत्ययार्थाश्च निर्दिश्यन्ते**: thirteen affixes "
              "have been given from 5.1.18 on, and FROM HERE what "
              "is stated is the case each takes and the sense each "
              "serves. Two halves — which affix, then in what sense "
              "— and the table is built the way the vṛtti divides "
              "it.\n\n"
              "सप्तत्या क्रीतं **साप्ततिकम्**; नैष्किकम्, पाणिकम्, "
              "शत्यम्, द्विकम्.\n\n"
              "**AND THE INSTRUMENTAL IS THE PRICE AND NOT THE "
              "BUYER.** **तेनेति मूल्यात् करणे तृतीया समर्थविभक्तिः; "
              "अन्यत्रानभिधानाद् न भवति** — देवदत्तेन क्रीतम् takes "
              "nothing, and neither does पाणिना क्रीतम्, *bought "
              "with the hand*.\n\n"
              "**AND THE NUMBER OF THE BASE MATTERS, UNTIL IT DOES "
              "NOT.** प्रस्थाभ्यां क्रीतम् and प्रस्थैः क्रीतम् take "
              "nothing, **अनभिधानादेव**. But **यत्र तु "
              "प्रकृत्यर्थस्य संख्याभेदावगमे प्रमाणमस्ति तत्र "
              "द्विवचनबहुवचनान्तादपि प्रत्ययो भवति**: where the "
              "plurality is itself the point, the affix comes — "
              "द्वाभ्यां क्रीतं **द्विकम्**, and मुद्गैः क्रीतं "
              "**मोद्गिकम्**, because **न ह्येकेन मुद्गेन क्रयः "
              "संभवति**, nobody buys anything with a single bean",
          keeps_out="देवदत्तेन क्रीतम्, पाणिना क्रीतम्"),
    Krita("5.1.38", sense="nimitta", case="ṣaṣṭhī", borrows=True,
          why="तस्य निमित्तं संयोगोत्पातौ — and the sense is "
              "narrowed twice over. **संयोगः संबन्धः** is a "
              "meeting; **प्राणिनां शुभाशुभसूचको महाभूतपरिणाम "
              "उत्पातः** is a portent, an upheaval of the elements "
              "that foretells good or ill for living things.\n\n"
              "शतस्य निमित्तं धनपतिना संयोगः **शत्यः, शतिकः** — a "
              "meeting with a rich man that will bring a hundred. "
              "And as an omen: शतस्य निमित्तम् उत्पातो "
              "**दक्षिणाक्षिस्पन्दनम्**, a twitch of the right eye, "
              "**शत्यम्**.\n\n"
              "Two vārttikas add the humours: **तस्य निमित्तप्रकरणे "
              "वातपित्तश्लेष्मभ्यः शमनकोपनयोरुपसंख्यानम्** — for "
              "what QUIETS or what ROUSES wind, bile or phlegm, "
              "**वातिकम्, पैत्तिकम्, श्लैष्मिकम्**; and "
              "**सन्निपाताच्चेति वक्तव्यम्**, सान्निपातिकम्, for "
              "all three at once"),
    Krita("5.1.39", gives="yat", of=("go",), sense="nimitta",
          case="ṣaṣṭhī", excepts=("5.1.18",),
          why="गोद्व्यचोऽसंख्यापरिमाणाश्वादेर्यत्, ठञादीनामपवादः; "
              "the गो half. गोर्निमित्तं संयोग उत्पातो वा "
              "**गव्यः**"),
    Krita("5.1.39", gives="yat", vowels="dvyac", sense="nimitta",
          case="ṣaṣṭhī", excepts=("5.1.18",),
          excludes=("saṃkhyā", "parimāṇa", "aśvādi"),
          why="गोद्व्यचोऽसंख्यापरिमाणाश्वादेर्यत्, the द्व्यच् half "
              "— from any two-vowelled stem, three kinds excepted. "
              "**धन्यम्, स्वर्ग्यम्, यशस्यम्, आयुष्यम्** — what "
              "portends wealth, heaven, fame, long life.\n\n"
              "**असंख्यापरिमाणाश्वादेरिति किम्?** पञ्चानां निमित्तं "
              "**पञ्चकम्**; परिमाण — प्रास्थिकम्, खारीकम्; अश्वादि "
              "— आश्विकः. **ब्रह्मवर्चसादुपसंख्यानम्** adds one "
              "more: ब्रह्मवर्चसस्य निमित्तं गुरुणा संयोगो "
              "**ब्रह्मवर्चस्यम्**.\n\n"
              "अश्व, अश्मन्, गण, ऊर्णा, उमा, वसु, वर्ष, भङ्ग — "
              "अश्वादिः",
          keeps_out="पञ्चकम्, प्रास्थिकम्, आश्विकः"),
    Krita("5.1.40", gives="cha", also_gives=("yat",), of=("putra",),
          sense="nimitta", case="ṣaṣṭhī", excepts=("5.1.39",),
          why="पुत्राच्छ च. **द्व्यच इति नित्ये यति प्राप्ते "
              "वचनम्** — पुत्र has two vowels, so 5.1.39 would give "
              "it यत् and nothing else; the rule is stated to add छ "
              "beside it, and the च keeps the यत्. पुत्रस्य निमित्तं "
              "संयोग उत्पातो वा **पुत्रीयम्, पुत्र्यम्**"),
    Krita("5.1.41", gives="aṇ", of=("sarvabhūmi",), sense="nimitta",
          case="ṣaṣṭhī", excepts=("5.1.19",),
          why="सर्वभूमिपृथिवीभ्यामणञौ, ठकोऽपवादौ; the सर्वभूमि "
              "member, **यथासंख्यम्**. सर्वभूमेर्निमित्तं संयोग "
              "उत्पातो वा **सार्वभौमः** — and the strengthening "
              "falls on BOTH members, **सर्वभूमेरनुशतिकादिपाठाद् "
              "उभयपदवृद्धिः** (7.3.20)"),
    Krita("5.1.41", gives="añ", of=("pṛthivī",), sense="nimitta",
          case="ṣaṣṭhī", excepts=("5.1.19",),
          why="सर्वभूमिपृथिवीभ्यामणञौ, the पृथिवी member. "
              "**पार्थिवः**"),
    Krita("5.1.42", gives="aṇ", of=("sarvabhūmi",), sense="īśvara",
          case="ṣaṣṭhī", excepts=("5.1.19",),
          why="तस्येश्वरः — the same two words, the same two "
              "affixes, a different sense. सर्वभूमेरीश्वरः "
              "**सार्वभौमः**; पार्थिवः.\n\n"
              "**AND THE GENITIVE IS RESTATED THOUGH IT IS ALREADY "
              "RUNNING.** Why, inside a section of genitives? "
              "**षष्ठीप्रकरणे पुनः षष्ठीसमर्थविभक्तिनिर्देशः "
              "प्रत्ययार्थस्य निवृत्तये** — to stop the SENSE "
              "carrying over. Without it, **अन्यथा संयोगोत्पाताविव "
              "ईश्वरोऽपि प्रत्ययार्थस्य निमित्तस्य विशेषणं "
              "संभाव्येत**: *lord* would have been read as a further "
              "qualification of *omen*, the way *meeting* and "
              "*portent* were. Restating the case is how the sense "
              "is cut off"),
    Krita("5.1.42", gives="añ", of=("pṛthivī",), sense="īśvara",
          case="ṣaṣṭhī", excepts=("5.1.19",),
          why="तस्येश्वरः, the पृथिवी member. **पार्थिवः** — a "
              "king, one who is lord of the earth"),
    Krita("5.1.43", gives="aṇ", of=("sarvabhūmi",), sense="vidita",
          case="saptamī", excepts=("5.1.19",),
          why="तत्र विदित इति च — and now the base stands in the "
              "LOCATIVE. **विदितो ज्ञातः प्रकाशित इत्यर्थः**, known "
              "or famous. सर्वभूमौ विदितः **सार्वभौमः**. The same "
              "form for the third time in three rules, and only the "
              "case and the sense divide them"),
    Krita("5.1.43", gives="añ", of=("pṛthivī",), sense="vidita",
          case="saptamī", excepts=("5.1.19",),
          why="तत्र विदित इति च, the पृथिवी member. **पार्थिवः**"),
    Krita("5.1.44", gives="ṭhañ", of=("loka", "sarvaloka"),
          sense="vidita", case="saptamī",
          why="लोकसर्वलोकाट् ठञ्. लोके विदितो **लौकिकः**, known in "
              "the world; **सार्वलौकिकः**, where 7.3.20's "
              "अनुशतिकादि list again strengthens both members"),
    Krita("5.1.45", sense="vāpa", case="ṣaṣṭhī", borrows=True,
          why="तस्य वापः — and the sense is a FIELD, named from the "
              "sowing. **उप्यतेऽस्मिन् वापः, क्षेत्रमुच्यते**: what "
              "is sown in is a वाप, and that means the field. "
              "प्रस्थस्य वापः क्षेत्रं **प्रास्थिकम्**, land that "
              "takes a prastha of seed; द्रौणिकम्, खारीकम्. A "
              "measure of land given as a measure of grain"),
    Krita("5.1.46", gives="ṣṭhan", of=("pātra",), sense="vāpa",
          case="ṣaṣṭhī", excepts=("5.1.18",),
          why="पात्रात् ष्ठन्, ठञोऽपवादः — and the two letters of "
              "the affix's name are told apart: **नकारः स्वरार्थः; "
              "षकारो ङीषर्थः**, the न for the accent and the ष for "
              "the feminine. **पात्रशब्दः परिमाणवाची** — the word "
              "here is a MEASURE and not a vessel. पात्रस्य वापः "
              "**पात्रिकं क्षेत्रम्**; पात्रिकी क्षेत्रभक्तिः"),
    Krita("5.1.47", sense="vṛddhyādi", case="prathamā", borrows=True,
          why="तदस्मिन् वृद्ध्यायलाभशुल्कोपदा दीयते — five things "
              "given, and each is defined. **यदधमर्णेनोत्तमर्णाय "
              "मूलधनातिरिक्तं देयं तद् वृद्धिः**, interest, what a "
              "debtor pays a creditor above the principal; "
              "**ग्रामादिषु स्वामिग्राह्यो भाग आयः**, revenue; "
              "**पटादीनामुपादानमूलादतिरिक्तं द्रव्यं लाभः**, profit "
              "over cost; **रक्षानिर्वेशो राजभागः शुल्कः**, a toll "
              "paid for protection; **उत्कोच उपदा**, a bribe.\n\n"
              "**दीयत इत्येकवचनान्तं वृद्ध्यादिभिः प्रत्येकम् "
              "अभिसंबध्यते** — the verb is singular and joins each "
              "of the five separately. पञ्च अस्मिन् वृद्धिर्वा आयो "
              "वा दीयते **पञ्चकः**; शत्यः, शतिकः, साहस्रः.\n\n"
              "**चतुर्थ्यर्थ उपसंख्यानम्** adds the dative — पञ्च "
              "अस्मै दीयते पञ्चको देवदत्तः — and then withdraws the "
              "addition as needless: **सिद्धं त्वधिकरणत्वेन "
              "विवक्षितत्वात्**, the man can be MEANT as the place "
              "the thing is given in, **सममब्राह्मणे दानम्** "
              "(मनु० ७.८५) being said the same way"),
    Krita("5.1.48", gives="ṭhan", of_samjna="pūraṇa",
          sense="vṛddhyādi", case="prathamā", excepts=("5.1.19",),
          why="पूरणार्धाट् ठन्, **यथायथं ठक्टिठनोरपवादः** — an "
              "exception to each of two affixes as each applies. "
              "From an ORDINAL: द्वितीयो वृद्ध्यादिरस्मिन् दीयते "
              "**द्वितीयिकः**; तृतीयिकः, पञ्चमिकः, सप्तमिकः"),
    Krita("5.1.48", gives="ṭhan", of=("ardha",), sense="vṛddhyādi",
          case="prathamā", excepts=("5.1.19",),
          why="पूरणार्धाट् ठन्, the अर्ध half — and the word is not "
              "*half* in general. **अर्धशब्दो रूपकार्धस्य रूढिः**: "
              "it is the settled name of half a रूपक, a coin. "
              "**अर्धिकः**"),
    Krita("5.1.49", gives="yat", also_gives=("ṭhan",),
          of=("bhāga",), sense="vṛddhyādi", case="prathamā",
          excepts=("5.1.18",),
          why="भागाद् यच्च, ठञोऽपवादः — and the च brings ठन् in "
              "beside the यत्. भागो वृद्ध्यादिरस्मिन् दीयते "
              "**भाग्यम्, भागिकं शतम्**; भाग्या, भागिका विंशतिः. "
              "**भागशब्दोऽपि रूपकार्धस्य वाचकः** — this word too "
              "means half a coin, like the अर्ध of the rule before"),
    Krita("5.1.50", sense="harati", case="dvitīyā", borrows=True,
          gana="vaṃśādi", uttarapada="bhāra",
          why="तद्धरति वहति आवहति भाराद् वंशादिभ्यः — and the "
              "Kāśikā gives TWO readings and refuses to choose. On "
              "the first, **वंशादिभ्यः परो यो भारशब्दस्तदन्तात् "
              "प्रातिपदिकात्**: from a stem ending in भार preceded "
              "by a वंशादि word — वंशभारं हरति **वांशभारिकः**. On "
              "the second, **अपरा वृत्तिः — भाराद् वंशादिभ्य इति, "
              "भारभूतेभ्यो वंशादिभ्य इत्यर्थः**: from the वंशादि "
              "words themselves when they are a LOAD, भार "
              "qualifying them through the sense — भारभूतान् वंशान् "
              "हरति **वांशिकः**.\n\n"
              "**सूत्रार्थद्वयमपि चैतद् आचार्येण शिष्याः "
              "प्रतिपादिताः। तदुभयमपि ग्राह्यम्** — the teacher "
              "taught his pupils both meanings of the sūtra, and "
              "both are to be accepted. Each reading has its own "
              "counter-examples, and the vṛtti supplies both sets.\n\n"
              "The three verbs are separated too: **हरति देशान्तरं "
              "प्रापयति चोरयति वा** — carries off, or steals; "
              "**वहति उत्क्षिप्य धारयति**, holds up and bears; "
              "**आवहति उत्पादयति**, brings about.\n\n"
              "वंश, कुटज, बल्वज, मूल, अक्ष, स्थूणा, अश्मन्, अश्व, "
              "इक्षु, खट्वा — वंशादिः",
          keeps_out="वंशं हरति, व्रीहिभारं हरति"),
    Krita("5.1.51", gives="ṭhan", of=("vasna",), sense="harati",
          case="dvitīyā", excepts=("5.1.18",),
          why="वस्नद्रव्याभ्यां ठन्कनौ, **यथासंख्यम्**; the वस्न "
              "member. वस्नं हरति वहति वा **वस्निकः**"),
    Krita("5.1.51", gives="kan", of=("dravya",), sense="harati",
          case="dvitīyā", excepts=("5.1.18",),
          why="वस्नद्रव्याभ्यां ठन्कनौ, the द्रव्य member. "
              "**द्रव्यकः**"),
    Krita("5.1.52", sense="sambhavati", case="dvitīyā",
          borrows=True,
          why="संभवत्यवहरति पचति — three more verbs, each defined. "
              "**तत्राधेयस्य प्रमाणानतिरेकः संभवः**, holding, where "
              "what is put in does not exceed the measure; "
              "**उपसंहरणम् अवहारः**, taking up; **विक्लेदनं पाकः**, "
              "cooking, which is a softening. प्रस्थं संभवति "
              "अवहरति पचति वा **प्रास्थिकः**; कौडविकः, खारीकः.\n\n"
              "**ननु च पाके च संभवोऽस्ति?** If a pot cooks a "
              "prastha it also HOLDS one, so why name both? "
              "**नास्त्यत्र नियोगः** — there is no necessity in it, "
              "and the two senses come apart: प्रस्थं पचति ब्राह्मणी "
              "**प्रास्थिकी**, where the woman cooks it and does "
              "not contain it.\n\n"
              "**तत्पचतीति द्रोणादण् च** — a vārttika adds अण् "
              "after द्रोण in the cooking sense alone: द्रोणं पचति "
              "**द्रौणी, द्रौणिकी**"),
    Krita("5.1.53", gives="kha", of=("āḍhaka", "ācita", "pātra"),
          sense="sambhavati", case="dvitīyā", optional=True,
          excepts=("5.1.18",),
          why="आढकाचितपात्रात् खोऽन्यतरस्याम्, ठञोऽपवादः — and "
              "**पक्षे सोऽपि भवति**, in the other half the ठञ् "
              "comes. आढकं संभवति अवहरति पचति वा **आढकीना, "
              "आढकिकी**; आचितीना, आचितिकी; पात्रीणा, पात्रिकी"),
    Krita("5.1.54", gives="ṣṭhan", also_gives=("kha",),
          uttarapada="āḍhaka-ācita-pātra", pre="dvigu",
          sense="sambhavati", case="dvitīyā", optional=True,
          excepts=("5.1.18",),
          why="द्विगोः ष्ठंश्च — and the counting of the forms is "
              "the point. **विधानसामर्थ्याद् अनयोर्लुग् न भवति**: "
              "ष्ठन् and ख are given after a द्विगु and so survive "
              "5.1.28, the same argument 5.1.32 used. **ठञस्तु "
              "पक्षेऽनुज्ञातस्य अध्यर्धपूर्वद्विगोः इति लुग् "
              "भवत्येव** — but the ठञ् allowed in the other "
              "alternative IS removed. So three forms: "
              "**द्व्याढकिकी, द्व्याढकीना, द्व्याढकी**.\n\n"
              "**नकारः स्वरार्थः; षकारो ङीषर्थः** again, and "
              "4.1.22's अपरिमाणबिस्ताचित… blocks ङीप् in "
              "द्व्याचिता"),
    Krita("5.1.55", lup=True, also_gives=("kha", "ṣṭhan"),
          uttarapada="kulija", pre="dvigu", sense="sambhavati",
          case="dvitīyā", optional=True, excepts=("5.1.18",),
          why="कुलिजाल् लुक्खौ च — and now there are FOUR. "
              "**अन्यतरस्यांग्रहणानुवृत्त्या लुगपि विकल्प्यते; "
              "ठञः पक्षे श्रवणं भवति। तेन चातूरूप्यं संपद्यते**: "
              "the elision is itself one of the alternatives, the "
              "ठञ् is heard in another, and ख and ष्ठन् make the "
              "other two. **द्विकुलिजिकी, द्विकुलिजीना, "
              "द्विकुलिजी, द्वैकुलिजिकी**.\n\n"
              "Three forms at 5.1.36, three at 5.1.54, four here — "
              "the vṛtti counts them each time, त्रैरूप्यम् and "
              "चातूरूप्यम्. And 7.3.17's exclusion is read as "
              "covering कुलिज too, **तेनोत्तरपदवृद्धिरपि न भवति**"),
    Krita("5.1.56", sense="aṃśa-vasna-bhṛti", case="prathamā",
          borrows=True,
          why="सोऽस्यांशवस्नभृतयः — three more, and three "
              "one-word glosses. **अंशो भागः**, a share; **वस्नं "
              "मूल्यम्**, a price; **भृतिर्वेतनम्**, wages. पञ्च "
              "अंशो वस्नो वा भृतिर्वास्य **पञ्चकः**; सप्तकः, "
              "साहस्रः"),
    Krita("5.1.57", sense="parimāṇa", case="prathamā", borrows=True,
          why="तदस्य परिमाणम्. प्रस्थः परिमाणमस्य **प्रास्थिको "
              "राशिः**; शत्यः, द्रौणिकः; वर्षशतं परिमाणमस्य "
              "**वार्षशतिकः**; षष्टिर्जीवितपरिमाणमस्य **षाष्टिकः**, "
              "a man of sixty years.\n\n"
              "**AND THE RULE RESTATES WHAT IS ALREADY RUNNING, IN "
              "ORDER TO BEAT AN ELISION.** **समर्थविभक्तिः "
              "प्रत्ययार्थश्च पूर्वसूत्रादेवानुवर्तिष्यते, किमर्थं "
              "पुनरनयोरुपादानम्? पुनर्विधानार्थम्** — the case and "
              "the sense would both have carried down from 5.1.56, "
              "so saying them again must be for the sake of the "
              "ENJOINING being fresh: **पुनर्विधानसामर्थ्याद् "
              "अध्यर्धपूर्वद्विगोर्लुग् न भवति**, and द्वे षष्टी "
              "जीवितपरिमाणमस्य is **द्विषाष्टिकः** with its affix "
              "intact. The third time this pāda saves an affix by "
              "the force of its being enjoined where it is"),
    Krita("5.1.58", gives="kan", of_samjna="saṃkhyā",
          sense="parimāṇa", case="prathamā",
          result="saṃjñā-saṃgha-sūtra-adhyayana", excepts=("5.1.18",),
          why="संख्यायाः संज्ञासंघसूत्राध्ययनेषु — from a numeral, "
              "in four settings, and the four are worked one by "
              "one. A NAME, where **संज्ञायां स्वार्थे प्रत्ययो "
              "वाच्यः**, the affix changing nothing: पञ्चैव "
              "**पञ्चकाः** शकुनयः. A GROUP: पञ्चकः संघः. An "
              "ĀDHYAYANA, a reading: **पञ्चकोऽधीतः**, "
              "**तस्य संख्यापरिमाणं पञ्चावृत्तयः पञ्च वाराः**, five "
              "times through.\n\n"
              "**AND A SŪTRA-WORK, WHERE THE GRAMMAR NAMES "
              "ITSELF.** **अष्टावध्यायाः परिमाणमस्य सूत्रस्य "
              "अष्टकं पाणिनीयम्** — a work of sūtras eight chapters "
              "in measure is *the eight of Pāṇini*. दशकं "
              "वैयाघ्रपदीयम्; त्रिकं काशकृत्स्नम्. The rule by "
              "which the Aṣṭādhyāyī is called the Aṣṭādhyāyī.\n\n"
              "**ननु चाध्यायसमूहः सूत्रसंघ एव भवति?** Is a "
              "collection of chapters not just a GROUP, already "
              "covered? **नैतदस्ति। प्राणिसमूहे संघशब्दो रूढः** — "
              "*group* is settled usage for a collection of living "
              "things.\n\n"
              "Three more supplements: **स्तोमे डविधिः "
              "पञ्चदशाद्यर्थः** — पञ्चदशः स्तोमः; **शन्शतोर्डिनिश् "
              "छन्दसि** — प॑ञ्चद॒शिनो॑ऽर्धमा॒साः; **विंशतेश्चेति "
              "वक्तव्यम्** — विंशिनोऽङ्गिरसः"),
    Krita("5.1.59", of_samjna="saṃkhyā", sense="parimāṇa",
          case="prathamā", excepts=("5.1.58",),
          why="पङ्क्तिविंशतित्रिंशच्चत्वारिंशत्पञ्चाशत्षष्टिसप्तत्यशीति"
              "नवतिशतम् — ten words laid down ready-made. "
              "**यदिह लक्षणेनानुपपन्नं तत्सर्वं निपातनात् सिद्धम्**: "
              "whatever cannot be got by rule is settled by the "
              "laying-down. पञ्चानां टिलोपः, तिश्च प्रत्ययः — "
              "**पङ्क्तिश्छन्दः**; द्वयोर्दशतोर्विन्भावः शतिच् च — "
              "**विंशतिः**; त्रयाणां त्रिन्भावः शत् च — "
              "**त्रिंशत्**; and so to शतम्.\n\n"
              "**AND THE VṚTTI WARNS AGAINST TAKING THE ANALYSIS "
              "SERIOUSLY.** **विंशत्यादयो गुणशब्दाः, ते "
              "यथाकथंचिद् व्युत्पाद्याः। नात्रावयवार्थे "
              "ऽभिनिवेष्टव्यम्** — these are quality-words, to be "
              "derived somehow or other, and one must not insist on "
              "a meaning for the parts. The proof: **पङ्क्तिरिति "
              "क्रमसंनिवेशेऽपि वर्तते** — पङ्क्ति also means a mere "
              "row, ब्राह्मणपङ्क्तिः, पिपीलिकापङ्क्तिः, **न "
              "चात्रावयवार्थः कश्चिदस्ति**, and there is no *five* "
              "in an ant's file at all. **सहस्रादयोऽप्येवंजातीयकाः "
              "तद्वदेव द्रष्टव्याः; उदाहरणमात्रमेतत्** — the list "
              "is examples and not an inventory"),
    Krita("5.1.60", gives="ḍati", of=("pañcan", "daśan"),
          sense="parimāṇa", case="prathamā", result="varga",
          optional=True, excepts=("5.1.58",),
          why="पञ्चद्दशतौ वर्गे वा. **संख्यायाः इति कनि प्राप्ते "
              "डतिर्निपात्यते; वावचनात् पक्षे सोऽपि भवति** — 5.1.58 "
              "would give कन्, and डति is laid down instead, with "
              "the वा letting the कन् stand in the other half. "
              "पञ्च परिमाणमस्य **पञ्चद् वर्गः**, and **पञ्चको "
              "वर्गः**"),
    Krita("5.1.61", gives="añ", of=("saptan",), sense="parimāṇa",
          case="prathamā", result="varga", usage="chandasi",
          excepts=("5.1.58",),
          why="सप्तनोऽञ् छन्दसि. **वर्ग इत्येव** — the group is "
              "carried down, and the register is the Veda. "
              "स॒प्त **साप्ता**नि असृजत्"),
    Krita("5.1.62", gives="ḍaṇ", of=("triṃśat", "catvāriṃśat"),
          sense="parimāṇa", case="prathamā", result="brāhmaṇa",
          excepts=("5.1.58",),
          why="त्रिंशच्चत्वारिंशतोर्ब्राह्मणे संज्ञायां डण्. "
              "**वर्ग इति निवृत्तम्** — the group lapses and a "
              "ब्राह्मण text takes its place. त्रिंशदध्यायाः "
              "परिमाणमेषां ब्राह्मणानां **त्रैंशानि ब्राह्मणानि**; "
              "चात्वारिंशानि.\n\n"
              "**अभिधेयसप्तम्येषा, न विषयसप्तमी** — the locative "
              "ब्राह्मणे says what the word MEANS, not what body of "
              "text the rule is confined to, **तेन "
              "मन्त्रभाषयोरपि भवति**: so the form occurs in mantra "
              "and in ordinary speech as well. A distinction "
              "between two uses of the locative, drawn in five "
              "words"),
    Krita("5.1.63", sense="arhati", case="dvitīyā", borrows=True,
          why="तदर्हति — and the आर्हीय heading closes on the word "
              "that named it. श्वेतच्छत्रमर्हति "
              "**श्वैतच्छत्रिकः**, one who deserves a white "
              "parasol; वास्त्रयुग्मिकः; शत्यः, शतिकः, साहस्रः.\n\n"
              "**AND THE HEADING TAKES THIS RULE IN RATHER THAN "
              "STOPPING BEFORE IT.** 5.1.19 said आ and not प्राक्, "
              "**अभिविधावयमाकारः, तेनार्हत्यर्थेऽपि ठग् भवत्येव** — "
              "so ठक् is the affix HERE too, and श्वैतच्छत्रिकः has "
              "it. Every other great heading of the grammar stops "
              "one short of the sūtra it is named from; this is the "
              "one that reaches it"),
    Krita("5.1.64", gana="chedādi", sense="arhati", case="dvitīyā",
          result="nitya", borrows=True,
          why="छेदादिभ्यो नित्यम्. **नित्यग्रहणं "
              "प्रत्ययार्थविशेषणम्** — the word *always* qualifies "
              "what the affix reports, not the rule's own "
              "application. छेदं नित्यमर्हति **छैदिकः**, one who is "
              "always deserving of being cut; भैदिकः.\n\n"
              "छेद, भेद, द्रोह, दोह, वर्त, कर्ष, संप्रयोग, "
              "विप्रयोग, प्रेषण, संप्रश्न, विप्रकर्ष, **विराग "
              "विरङ्गं च** (ग०सू०११२) — छेदादिः, where the last "
              "entry substitutes as well as listing: वैरङ्गिकः"),
    Krita("5.1.65", gives="yat", of=("śīrṣaccheda",), sense="arhati",
          case="dvitīyā", result="nitya", adesa="śīrṣan",
          excepts=("5.1.64",),
          why="शीर्षच्छेदाद् यच्च — and the च keeps the "
              "यथाविहितम् of the rule before, so both forms stand: "
              "शिरश्छेदं नित्यमर्हति **शीर्षच्छेद्यः, "
              "शैर्षच्छेदिकः**. **प्रत्ययसन्नियोगेन शिरसः "
              "शीर्षभावो निपात्यते**: the change of शिरस् to शीर्ष "
              "is laid down as yoked to the affix, so the "
              "substitution and the affix come together or not at "
              "all"),
    Krita("5.1.66", gives="ya", gana="daṇḍādi", sense="arhati",
          case="dvitīyā", excepts=("5.1.19",),
          why="दण्डादिभ्यः, ठकोऽपवादः. **नित्यमिति निवृत्तम्** — "
              "the *always* of 5.1.64 lapses here. दण्डमर्हति "
              "**दण्ड्यः**, one who deserves the rod; मुसल्यः. "
              "दण्ड, मुसल, मधुपर्क, कशा, अर्घ, मेधा, मेघ, युग, "
              "उदक, वध, गुहा, भाग, इभ — दण्डादिः"),
    Krita("5.1.67", gives="yat", sense="arhati", case="dvitīyā",
          usage="chandasi", excepts=("5.1.19", "5.1.18"),
          why="छन्दसि च, ठञादीनामपवादः — and in the Veda the affix "
              "comes after ANY stem whatever, **प्रातिपदिकमात्रात्**. "
              "**उदक्या** वृत्तयः; यूप्यः पलाशः; गर्त्यो देशः"),
    Krita("5.1.68", gives="ghan", also_gives=("yat",),
          of=("pātra",), sense="arhati", case="dvitīyā",
          excepts=("5.1.19", "5.1.18"),
          why="पात्राद् घंश्च, ठक्ठञोरपवादः — and the च brings यत् "
              "in beside the घन्. **पात्रं परिमाणमप्यस्ति** — the "
              "word is a measure here as it was at 5.1.46. "
              "पात्रमर्हति **पात्रियः, पात्र्यः**"),
    Krita("5.1.69", gives="cha", also_gives=("yat",),
          of=("kaḍaṅkara", "dakṣiṇā"), sense="arhati",
          case="dvitīyā", excepts=("5.1.19",),
          why="कडङ्करदक्षिणाच्छ च, ठकोऽपवादः. कडङ्करमर्हति "
              "**कडङ्करीयो गौः**, कडङ्कर्यः; दक्षिणामर्हति "
              "**दक्षिणीयो भिक्षुः**, दक्षिण्यो ब्राह्मणः.\n\n"
              "**AND THE ORDER OF THE TWO WORDS IS ITSELF A SIGN.** "
              "**दक्षिणाशब्दस्याल्पाच्तरस्यापूर्वनिपातेन "
              "लक्षणव्यभिचारचिह्नेन यथासंख्याभावं सूचयति** — "
              "दक्षिणा has fewer vowels and so should have stood "
              "first in the compound; that it does not breaks a "
              "rule, and the breach is the mark that the two "
              "affixes are NOT to be matched to the two words in "
              "order. Both words take both affixes"),
    Krita("5.1.70", gives="cha", also_gives=("yat",),
          of=("sthālībila",), sense="arhati", case="dvitīyā",
          excepts=("5.1.19",),
          why="स्थालीबिलात्, ठकोऽपवादौ. **छयतावनुवर्तते** — both "
              "affixes of the rule before are carried down. "
              "स्थालीबिलमर्हन्ति **स्थालीबिलीयास्तण्डुलाः**, "
              "स्थालीबिल्याः — grain fit for the pot's hollow, "
              "**पाकयोग्या इत्यर्थः**, fit to be cooked"),
    Krita("5.1.71", gives="gha", of=("yajña",), sense="arhati",
          case="dvitīyā", excepts=("5.1.19",),
          why="यज्ञर्त्विग्भ्यां घखञौ, **यथासंख्यम्**, ठकोऽपवादौ; "
              "the यज्ञ member. **यज्ञियो ब्राह्मणः**.\n\n"
              "**यज्ञर्त्विग्भ्यां तत्कर्मार्हतीत्युपसंख्यानम्** — "
              "a vārttika extends it to deserving the WORK of "
              "these: यज्ञकर्मार्हति **यज्ञियो देशः**, a place fit "
              "for the work of sacrifice.\n\n"
              "**AND THE आर्हीय SECTION ENDS HERE, EIGHT SŪTRAS "
              "PAST ITS OWN MARKER.** **आर्हीयाणां ठगादीनां "
              "पूर्णोऽवधिः। अतः परं प्राग्वतीयष्ठञेव भवति** — the "
              "limit of ठक् and the affixes under it is complete, "
              "and from here it is the ठञ् of 5.1.18 alone. The "
              "same formula 4.4.74, 4.4.144 and 5.1.17 used, for "
              "the fourth time.\n\n"
              "So even the one heading bounded by अभिविधि has a "
              "marker apart from its last rule. The difference is "
              "not that the two coincide — it is that this heading "
              "REACHES its marker and takes it in, where the others "
              "stop short of theirs, and then runs on past it while "
              "the rules keep naming its sense"),
    Krita("5.1.71", gives="khañ", of=("ṛtvij",), sense="arhati",
          case="dvitīyā", excepts=("5.1.19",),
          why="यज्ञर्त्विग्भ्यां घखञौ, the ऋत्विज् member. "
              "**आर्त्विजीनो ब्राह्मणः**, and by the vārttika "
              "ऋत्विक्कर्मार्हति **आर्त्विजीनं ब्राह्मणकुलम्**"),
    Krita("5.1.72", gives="ṭhañ", gana="pārāyaṇādi",
          sense="vartayati", case="dvitīyā",
          why="पारायणतुरायणचान्द्रायणं वर्तयति. "
              "**समर्थविभक्तिरनुवर्तते; अर्हतीति निवृत्तम्** — the "
              "case carries and the sense does not. पारायणं "
              "**वर्तयत्यधीते** — carries on, that is, studies: "
              "**पारायणिकश्छात्रः**; तौरायणिको यजमानः; "
              "चान्द्रायणिकस्तपस्वी.\n\n"
              "This is the rule 5.1.18 named its own examples "
              "from — the first ordinary ठञ् rule after the आर्हीय "
              "section closes"),
    Krita("5.1.73", gives="ṭhañ", of=("saṃśaya",), sense="āpanna",
          case="dvitīyā",
          why="संशयमापन्नः. **संशयमापन्नः प्राप्तः** — one who has "
              "COME INTO doubt. **सांशयिकः स्थाणुः**, a post that "
              "one is in doubt about"),
    Krita("5.1.74", gives="ṭhañ", of=("yojana",), sense="gacchati",
          case="dvitīyā",
          why="योजनं गच्छति. योजनं गच्छति **यौजनिकः**. Two "
              "vārttikas add two long distances: "
              "**क्रोशशतयोजनशतयोरुपसंख्यानम्** — क्रौशशतिकः, "
              "यौजनशतिकः; and **ततोऽभिगमनमर्हतीति च** — and one "
              "who DESERVES to be come to from that far: "
              "क्रोशशतादभिगमनमर्हति **क्रौशशतिको भिक्षुः**, "
              "**यौजनशतिक आचार्यः**, a teacher worth a hundred "
              "leagues' journey"),
    Krita("5.1.75", gives="ṣkan", of=("pathin",), sense="gacchati",
          case="dvitīyā", excepts=("5.1.18",),
          why="पथः ष्कन्. **नकारः स्वरार्थः; षकारो ङीषर्थः** — the "
              "same accounting 5.1.25 and 5.1.46 gave. पन्थानं "
              "गच्छति **पथिकः, पथिकी**"),
    Krita("5.1.76", gives="ṇa", of=("pathin",), adesa="panthan",
          sense="gacchati", case="dvitīyā", result="nitya",
          excepts=("5.1.75",),
          why="पन्थो ण नित्यम् — and again **नित्यग्रहणं "
              "प्रत्ययार्थविशेषणम्**, the *always* qualifying what "
              "is reported. The rule does two things at once: "
              "**पथः पन्थ इत्ययमादेशो भवति णश्च प्रत्ययः**. "
              "पन्थानं नित्यं गच्छति **पान्थो** भिक्षां याचते, a "
              "wayfarer, one always on the road. **नित्यमिति "
              "किम्?** पथिकः",
          keeps_out="पथिकः"),
    Krita("5.1.77", gives="ṭhañ", of=("uttarapatha",),
          sense="āhṛta", case="tṛtīyā",
          why="उत्तरपथेनाहृतं च — and the case is got from the "
              "wording itself, **निर्देशादेव समर्थविभक्तिः**, "
              "since the sūtra shows the instrumental in उत्तरपथेन. "
              "**चकारः प्रत्ययार्थसमुच्चये, गच्छतीति च**: the च "
              "gathers in the sense of the rule three back too, so "
              "one affix serves both — उत्तरपथेनाहृतम् "
              "**औत्तरपथिकम्**, and उत्तरपथेन गच्छति "
              "**औत्तरपथिकः**.\n\n"
              "**आहृतप्रकरणे "
              "वारिजङ्गलस्थलकान्तारपूर्वपदादुपसंख्यानम्** adds four "
              "roads — वारिपथिकम्, जाङ्गलपथिकम्, स्थालपथिकम्, "
              "कान्तारपथिकम् — and "
              "**अजपथशङ्कुपथाभ्यां चोपसंख्यानम्** two more. "
              "**मधुकमरिचयोरण् स्थलात्** gives a different affix "
              "for two goods: **स्थालपथं मधुकम्**, liquorice "
              "brought by the land road"),
    Krita("5.1.78", of_samjna="kāla", heading=True,
          why="कालात्. **कालादित्यधिकारः। यदित ऊर्ध्वम् "
              "अनुक्रमिष्यामः कालादित्येवं तद् वेदितव्यम्** — "
              "everything stated from here on is understood to be "
              "from a word for TIME. मासेन निर्वृत्तं **मासिकम्**; "
              "आर्धमासिकम्, सांवत्सरिकम्.\n\n"
              "**कालादित्यधिकारो व्युष्टादिभ्योऽण् इति यावत्** — "
              "the heading runs as far as 5.1.97. And this heading "
              "is unlike the four great ones: it carries not an "
              "AFFIX but a CONDITION on the base, so it does not "
              "compete with the ठञ् it stands inside"),
    Krita("5.1.79", gives="ṭhañ", of_samjna="kāla",
          sense="nirvṛtta", case="tṛtīyā",
          why="तेन निर्वृत्तम् — brought about by it. अह्ना "
              "निर्वृत्तम् **आह्निकम्**, a day's work; "
              "आर्धमासिकम्, सांवत्सरिकम्"),
    Krita("5.1.80", of_samjna="kāla", sense="adhīṣṭādi",
          case="dvitīyā", borrows=True,
          why="तमधीष्टो भृतो भूतो भावी — four senses, each glossed. "
              "**अधीष्टः सत्कृत्य व्यापारितः**, engaged with "
              "honour; **भृतो वेतनेन क्रीतः**, hired for wages; "
              "**भूतः स्वसत्तया व्याप्तकालः**, one whose own being "
              "has filled that time; **भावी तादृश एवानागतः**, the "
              "same but still to come. 2.3.5 कालाध्वनोः gives the "
              "accusative.\n\n"
              "मासमधीष्टो **मासिकोऽध्यापकः**; मासं भृतो मासिकः "
              "कर्मकरः; मासं भूतो मासिको व्याधिः; मासं भावी मासिक "
              "उत्सवः.\n\n"
              "**AND AN OBJECTION ABOUT WHAT CAN FILL A MONTH.** "
              "**ननु चाध्येषणं भरणं च मुहूर्तं क्रियते, तेन कथं "
              "मासो व्याप्यते?** — the engaging and the hiring take "
              "a moment, so how do they occupy a month? "
              "**अध्येषणभरणे क्रियार्थे, तत्र फलभूतया क्रियया "
              "मासो व्याप्यमानस्ताभ्यामेव व्याप्त इत्युच्यते**: "
              "both are FOR an action, and the month filled by that "
              "resulting action is said to be filled by them"),
    Krita("5.1.81", gives="yat", also_gives=("khañ",),
          of=("māsa",), of_samjna="kāla", sense="adhīṣṭādi",
          case="dvitīyā", result="vayas", excepts=("5.1.18",),
          why="मासाद् वयसि यत्खञौ, ठञोऽपवादौ — and only one of the "
              "four senses reaches here. **अधीष्टादीनां चतुर्णाम् "
              "अधिकारेऽपि सामर्थ्याद् भूत एवात्राभिसंबध्यते**: "
              "though all four are running, only भूत can join, "
              "since an AGE is time already lived. मासं भूतो "
              "**मास्यः, मासीनः**. **वयसीति किम्?** मासिकम्",
          keeps_out="मासिकम्"),
    Krita("5.1.82", gives="yap", uttarapada="māsa", pre="dvigu",
          of_samjna="kāla", sense="adhīṣṭādi", case="dvitīyā",
          result="vayas", excepts=("5.1.18",),
          why="द्विगोर्यप्. **मासाद् वयसीति वर्तते** — from a "
              "numeral compound ending in मास, of an age. द्वौ "
              "मासौ भूतो **द्विमास्यः**; त्रिमास्यः"),
    Krita("5.1.83", gives="ṇyat", also_gives=("yap", "ṭhañ"),
          of=("ṣaṇmāsa",), of_samjna="kāla", sense="adhīṣṭādi",
          case="dvitīyā", result="vayas",
          why="षण्मासाण् ण्यच्च. **वयसीत्येव**, and the counting "
              "again: **औत्सर्गिकष्ठञपीष्यते, स चकारेण "
              "समुच्चेतव्यः; स्वरितत्वाच्चानन्तरोऽनुवर्तिष्यते। "
              "तेन त्रैरूप्यं भवति** — the general ठञ् is wanted "
              "too and is gathered by the च, the यप् of the rule "
              "before carries on by its accent, and so THREE forms: "
              "**षाण्मास्यः, षण्मास्यः, षाण्मासिकः**"),
    Krita("5.1.84", gives="ṭhan", also_gives=("ṇyat",),
          of=("ṣaṇmāsa",), of_samjna="kāla", sense="adhīṣṭādi",
          case="dvitīyā", result="avayas",
          why="अवयसि ठंश्च — the same word, and now NOT of an age. "
              "**चकारेणानन्तरस्य ण्यतः समुच्चयः क्रियते**, the च "
              "gathering the ण्यत् of the rule before. "
              "**षण्मासिको रोगः**, a six-month illness; षाण्मास्यः"),
    Krita("5.1.85", gives="kha", of=("samā",), of_samjna="kāla",
          sense="adhīṣṭādi", case="dvitīyā", excepts=("5.1.18",),
          why="समायाः खः, ठञोऽपवादः. **अधीष्टादयश्चत्वारोऽर्था "
              "अनुवर्तन्ते** — all four senses are back. "
              "समामधीष्टो भृतो भूतो भावी वा **समीनः**. "
              "**केचित् तु तेन निर्वृत्तम् इति सर्वत्रानुवर्तयन्ति** "
              "— and some carry 5.1.79 down everywhere as well, "
              "giving समया निर्वृत्तः समीनः"),
    Krita("5.1.86", gives="kha", uttarapada="samā", pre="dvigu",
          of_samjna="kāla", sense="nirvṛttādi", case="dvitīyā",
          optional=True, excepts=("5.1.85",),
          why="द्विगोर्वा. **पूर्वेण नित्यः प्राप्तो विकल्प्यते** — "
              "what the rule before made obligatory becomes a "
              "choice, and **खेन मुक्ते पक्षे ठञपि भवति**: where "
              "the ख is released the ठञ् comes. **द्विसमीनः, "
              "द्वैसमिकः**.\n\n"
              "And a compound is reached at all only by the "
              "vārttika of 5.1.20: **प्राग्वतेः संख्यापूर्वपदानां "
              "तदन्तग्रहणमलुकि इति प्राप्तिरस्त्येव**"),
    Krita("5.1.87", gives="kha", uttarapada="rātri-ahan-saṃvatsara",
          pre="dvigu", of_samjna="kāla", sense="nirvṛttādi",
          case="dvitīyā", optional=True, excepts=("5.1.18",),
          why="रात्र्यहस्संवत्सराच्च. **खेन मुक्ते पक्षे ठञपि "
              "भवति**. **द्विरात्रीणः, द्वैरात्रिकः**; द्व्यहीनः, "
              "द्वैयह्निकः; द्विसंवत्सरीणः, द्विसांवत्सरिकः, where "
              "7.3.15 संख्यायाः संवत्सरसंख्यस्य च strengthens the "
              "LATTER member"),
    Krita("5.1.88", gives="kha", uttarapada="varṣa", pre="dvigu",
          of_samjna="kāla", sense="nirvṛttādi", case="dvitīyā",
          optional=True, excepts=("5.1.18",),
          why="वर्षाल् लुक् च — and here the elision joins the "
              "option, so **तयोश्च वा लुग् भवति। एवं त्रीणि रूपाणि "
              "भवन्ति**: three forms again. **द्विवर्षीणो "
              "व्याधिः, द्विवार्षिकः, द्विवर्षः**. 7.3.16 "
              "वर्षस्याभविष्यति strengthens the latter member — "
              "**भाविनि तु त्रैवर्षिकः**, and where the sense is "
              "*still to come* the strengthening moves to the "
              "first"),
    Krita("5.1.89", lup=True, uttarapada="varṣa", pre="dvigu",
          of_samjna="kāla", sense="nirvṛttādi", case="dvitīyā",
          result="cittavat", excepts=("5.1.88",),
          why="चित्तवति नित्यम् — and where what is meant HAS A "
              "MIND the elision is no longer a choice. "
              "**पूर्वेण विकल्पे प्राप्ते वचनम्**: the rule before "
              "made it optional and this makes it fixed. "
              "**द्विवर्षो दारकः**, a two-year-old child. "
              "**चित्तवतीति किम्?** द्विवर्षीणो व्याधिः — an "
              "illness has no mind, so it keeps the choice",
          keeps_out="द्विवर्षीणो व्याधिः"),
    Krita("5.1.90", gives="kan", of=("ṣaṣṭirātra",),
          of_samjna="kāla", sense="pacyate", case="tṛtīyā",
          adesa="ṣaṣṭi", result="saṃjñā",
          why="षष्टिकाः षष्टिरात्रेण पच्यन्ते — a laid-down form, "
              "and three things are laid down at once: the affix "
              "कन्, the dropping of रात्रि, and the sense. "
              "**बहुवचनमतन्त्रम्** — the plural in the sūtra is "
              "not binding. षष्टिरात्रेण पच्यन्ते **षष्टिकाः**, "
              "rice that ripens in sixty nights.\n\n"
              "**संज्ञैषा धान्यविशेषस्य। तेन मुद्गादिष्वतिप्रसङ्गो "
              "न भवति** — it is the NAME of one particular grain, "
              "so the rule does not overreach to beans and the "
              "rest that might also take sixty nights"),
    Krita("5.1.91", gives="cha", uttarapada="vatsara",
          of_samjna="kāla", sense="nirvṛttādi", case="tṛtīyā",
          usage="chandasi", excepts=("5.1.18",),
          why="वत्सरान्ताच्छश्छन्दसि, ठञोऽपवादः. **इद्वत्सरीयः, "
              "इदावत्सरीयः** (काठ०सं० १३.१५)"),
    Krita("5.1.92", gives="kha", also_gives=("cha",),
          uttarapada="vatsara", pre="sam-pari", of_samjna="kāla",
          sense="nirvṛttādi", case="tṛtīyā", usage="chandasi",
          excepts=("5.1.91",),
          why="संपरिपूर्वात् ख च — from a वत्सर-final stem with सम् "
              "or परि in front, and the च keeps the छ of the rule "
              "before. सं॒व॒त्स॒**रीणाः**; परिवत्स॒**रीण**म्; "
              "संवत्सरीया, परिवत्सरीया"),
    Krita("5.1.93", gives="ṭhañ", of_samjna="kāla",
          sense="parijayya-labhya-kārya-sukara", case="tṛtīyā",
          why="तेन परिजय्यलभ्यकार्यसुकरम् — four more senses, and "
              "one form answers all four. मासेन परिजय्यः, "
              "**शक्यते जेतुम्**, that can be got the better of in "
              "a month — **मासिको व्याधिः**; मासेन लभ्यो मासिकः "
              "पटः; मासेन कार्यं मासिकं चान्द्रायणम्; मासेन "
              "सुकरो **मासिकः प्रासादः**, a palace easily built in "
              "a month"),
    Krita("5.1.94", gives="ṭhañ", of_samjna="kāla",
          sense="brahmacarya", case="dvitīyā",
          why="तदस्य ब्रह्मचर्यम् — and here too the Kāśikā gives "
              "two readings and keeps both. On the first the base "
              "is in the ACCUSATIVE and **सा चात्यन्तसंयोगे**, of "
              "unbroken connection: मासं ब्रह्मचर्यमस्य **मासिको "
              "ब्रह्मचारी**, and the affix reports the STUDENT. On "
              "the second, **अपरा वृत्तिः**, the base is in the "
              "NOMINATIVE: मासोऽस्य ब्रह्मचर्यस्य **मासिकं "
              "ब्रह्मचर्यम्**, and the affix reports the STUDY. "
              "**पूर्वत्र ब्रह्मचारी प्रत्ययार्थः, उत्तरत्र "
              "ब्रह्मचर्यमेव। उभयमपि प्रमाणम्, उभयथा "
              "सूत्रप्रणयनात्** — both are authoritative, the "
              "sūtra being framed both ways. The second time this "
              "pāda refuses to choose between two readings.\n\n"
              "Five vārttikas follow, on observances rather than "
              "time: **महानाम्न्यादिभ्यः षष्ठीसमर्थेभ्य "
              "उपसंख्यानम्** — माहानामिकम्, गौदानिकम्, "
              "आदित्यव्रतिकम्; **तच्चरतीति च** — and one who "
              "PRACTISES it, **महानाम्न्य ऋचः, तत्सहचरितं व्रतं "
              "तच्छब्देनोच्यते**, the word naming the vow that goes "
              "with those verses: महानाम्नीश्चरति माहानामिकः. "
              "**अवान्तरदीक्षादिभ्यो डिनिर्वक्तव्यः** — "
              "अवान्तरदीक्षी, तिलव्रती; **अष्टाचत्वारिंशतो ड्वुंश्च "
              "डिनिश्च** — अष्टाचत्वारिंशकः, अष्टाचत्वारिंशी; "
              "**चातुर्मास्यानां यलोपश्च** — चातुर्मासकः, "
              "चातुर्मासी"),
    Krita("5.1.95", gives="ṭhañ", of_samjna="yajña-ākhyā",
          sense="dakṣiṇā", case="ṣaṣṭhī",
          why="तस्य च दक्षिणा यज्ञाख्येभ्यः. अग्निष्टोमस्य दक्षिणा "
              "**आग्निष्टोमिकी**; वाजपेयिकी, राजसूयिकी.\n\n"
              "**AND THE WORD आख्या IS WHAT LETS THE RULE OUT OF "
              "THE TIME-HEADING.** **आख्याग्रहणम् अकालादपि "
              "यज्ञवाचिनो यथा स्यादिति। इतरथा हि कालाधिकाराद् "
              "एकाहद्वादशाहप्रभृतय एव यज्ञा गृह्येरन्** — without "
              "it the काल heading would have confined the rule to "
              "sacrifices NAMED FROM their length, the one-day and "
              "the twelve-day; saying *named* takes in every "
              "sacrifice's name"),
    Krita("5.1.96", gives="ṭhañ", of_samjna="kāla",
          sense="dīyate-kārya", case="saptamī",
          why="तत्र च दीयते कार्यं भववत् — and the affix is "
              "borrowed from the *born in* rules: **भववत् "
              "प्रत्ययो भवति**, as in मासे भवं **मासिकम्**, so "
              "मासे दीयते मासिकम्. प्रावृषेण्यम्, वासन्तिकम्, "
              "हैमन्तिकम्, शारदम्. **वतिः सर्वसादृश्यार्थः** — the "
              "वति takes in every likeness, the same words 4.2.34 "
              "and 4.3.156 used.\n\n"
              "**योगविभागश्चात्र कर्तव्यः। तत्र च दीयते, "
              "यज्ञाख्येभ्य इति** — and the rule is to be split, so "
              "that the sacrifice-names of 5.1.95 are reached too: "
              "**आग्निष्टोमिकं भक्तम्**, food given at an "
              "अग्निष्टोम.\n\n"
              "**AND THE TIME-HEADING ENDS HERE.** "
              "**कालाधिकारस्य पूर्णोऽवधिः। अतः परं सामान्येन "
              "प्रत्ययविधानम्** — its limit is complete, and from "
              "here the affixes are given generally. 5.1.78 named "
              "5.1.97 as the boundary and the heading stops one "
              "short of it, which is the fifth time this project "
              "has met the formula and the fifth heading whose "
              "marker is not its last rule"),
    Krita("5.1.97", gives="aṇ", gana="vyuṣṭādi",
          sense="dīyate-kārya", case="saptamī", excepts=("5.1.18",),
          why="व्युष्टादिभ्योऽण् — and the base is no longer a word "
              "for time, which is why the heading stopped before "
              "this rule. व्युष्टे दीयते कार्यं वा **वैयुष्टम्**; "
              "नैत्यम्.\n\n"
              "**अण्प्रकरणे अग्निपदादिभ्य उपसंख्यानम्** proposes "
              "adding two words, and the vṛtti refuses the addition "
              "as needless: **किं वक्तव्यम्? न वक्तव्यम्। अत्रैव "
              "ते पठितव्याः** — put them in the list itself.\n\n"
              "व्युष्ट, नित्य, निष्क्रमण, प्रवेशन, तीर्थ, संभ्रम, "
              "आस्तरण, संग्राम, संघात, अग्निपद, पीलुमूल, प्रवास, "
              "उपसंक्रमण — व्युष्टादिः, and the last four are the "
              "words the vārttika wanted added"),
    Krita("5.1.98", gives="ṇa", also_gives=("yat",),
          of=("yathākathāca", "hasta"), sense="dīyate-kārya",
          case="tṛtīyā",
          why="तेन यथाकथाचहस्ताभ्यां णयतौ — two affixes and two "
              "words, and the vṛtti refuses to match them in order. "
              "**दीयते कार्यमित्येतयोरर्थयोः प्रत्येकम् "
              "अभिसंबन्धः, यथासंख्यं नेष्यते**: each affix goes "
              "with each sense, and the pairing is not wanted.\n\n"
              "**यथाकथाचशब्दोऽव्ययसमुदायोऽनादरे वर्तते** — "
              "यथाकथाच is a bundle of indeclinables meaning "
              "*anyhow*, carelessly. And being indeclinable it "
              "cannot really stand in a case: **तृतीयार्थमात्रं "
              "चात्र संभवति, न तु तृतीया समर्थविभक्तिः**, only the "
              "MEANING of the instrumental is possible here, not "
              "the instrumental itself. **याथाकथाचम्**; हस्तेन "
              "दीयते कार्यं वा **हस्त्यम्**"),
    Krita("5.1.99", gives="ṭhañ", sense="sampādin", case="tṛtīyā",
          why="संपादिनि. **गुणोत्कर्षः संपत्तिः** — a संपत्ति is "
              "an excellence of quality, so the sense is *what sets "
              "a thing off*. कर्णवेष्टकाभ्यां संपादि मुखं "
              "**कार्णवेष्टकिकं मुखम्**, a face that earrings set "
              "off; **वास्त्रययुगिकं शरीरम्**, "
              "**वस्त्रयुगेण विशेषतः शोभत इत्यर्थः**.\n\n"
              "(3.3.170's णिनि is what made संपादिन् itself, "
              "**आवश्यके णिनिः**)"),
    Krita("5.1.100", gives="yat", of=("karman", "veṣa"),
          sense="sampādin", case="tṛtīyā", excepts=("5.1.18",),
          why="कर्मवेषाद् यत्, ठञोऽपवादः. कर्मणा संपद्यते "
              "**कर्मण्यं शरीरम्**, a body that work sets off; "
              "वेषेण संपद्यते **वेष्यो नटः**, an actor his costume "
              "sets off"),
    Krita("5.1.101", gives="ṭhañ", gana="saṃtāpādi",
          sense="prabhavati", case="caturthī",
          why="तस्मै प्रभवति संतापादिभ्यः. **समर्थः शक्तः "
              "प्रभवतीत्युच्यते** — one who is able, equal to it; "
              "**अलमर्थे चतुर्थी**, the dative of being adequate. "
              "संतापाय प्रभवति **सान्तापिकः**; सान्नाहिकः.\n\n"
              "संताप, संनाह, संग्राम, संयोग, संपराय, संपेष, "
              "निष्पेष, निसर्ग, असर्ग, विसर्ग, उपसर्ग, उपवास, "
              "प्रवास, संघात, संमोदन, **सक्तुमांसौदनाद् "
              "विगृहीतादपि** (ग०सू०११३) — संतापादिः, and the last "
              "entry lets three words in even UNCOMPOUNDED"),
    Krita("5.1.102", gives="yat", also_gives=("ṭhañ",),
          of=("yoga",), sense="prabhavati", case="caturthī",
          why="योगाद् यच्च — and the च keeps the ठञ्, so both "
              "stand. योगाय प्रभवति **योग्यः, यौगिकः**"),
    Krita("5.1.103", gives="ukañ", of=("karman",),
          sense="prabhavati", case="caturthī", result="dhanus",
          excepts=("5.1.18",),
          why="कर्मण उकञ्, ठञोऽपवादः. कर्मणे प्रभवति **कार्मुकं "
              "धनुः**, a bow, *equal to the work*.\n\n"
              "**धनुषोऽन्यत्र न भवति, अनभिधानात्** — and of "
              "nothing but a bow, because the language does not say "
              "it of anything else. A rule whose scope is fixed not "
              "by a word in it but by usage",
          keeps_out="कार्मुकम् of anything but a bow"),
    Krita("5.1.104", gives="ṭhañ", of=("samaya",), sense="prāpta",
          case="prathamā",
          why="समयस्तदस्य प्राप्तम्. समयः प्राप्तोऽस्य "
              "**सामयिकं कार्यम्**, **उपनतकालम् इत्यर्थः** — a "
              "thing whose time has come round.\n\n"
              "**समर्थविभक्तिनिर्देश उत्तरार्थः** — and the case is "
              "spelled out here for the sake of the rules AFTER "
              "this one, which carry it down"),
    Krita("5.1.105", gives="aṇ", of=("ṛtu",), sense="prāpta",
          case="prathamā", excepts=("5.1.104",),
          why="ऋतोरण्. ऋतुः प्राप्तोऽस्य **आर्तवं पुष्पम्**, a "
              "flower whose season has come. **तदस्य प्रकरण "
              "उपवस्त्रादिभ्य उपसंख्यानम्** adds two more: "
              "औपवस्त्रम्, प्राशित्रम्"),
    Krita("5.1.106", gives="ghas", of=("ṛtu",), sense="prāpta",
          case="prathamā", usage="chandasi", excepts=("5.1.105",),
          why="छन्दसि घस्, अणोऽपवादः. अ॒यं ते॒ योनि॑र्**ऋ॒त्वियः**॒ "
              "(ऋ०३.२९.१०) — and the affix is given for one word "
              "in one register, where the rule before gave another "
              "for the same word everywhere else"),
    Krita("5.1.107", gives="yat", of=("kāla",), sense="prāpta",
          case="prathamā", excepts=("5.1.104",),
          why="कालाद् यत्. कालः प्राप्तोऽस्य **काल्यस्तापः**, heat "
              "that has come in its time; **काल्यं शीतम्**"),
    Krita("5.1.108", gives="ṭhañ", of=("kāla",), result="prakṛṣṭa",
          case="prathamā",
          why="प्रकृष्टे ठञ्. **प्राप्तमिति निवृत्तम्** — the "
              "*come round* sense lapses and only काल is carried. "
              "**प्रकर्षेण कालो विशेष्यते**: the time is qualified "
              "as LONG. प्रकृष्टो दीर्घः कालोऽस्य **कालिकमृणम्**, "
              "a debt of long standing; **कालिकं वैरम्**, an old "
              "enmity.\n\n"
              "**ठञ्ग्रहणं विस्पष्टार्थम्** — and the ठञ् is named "
              "though it is already the heading's, merely for "
              "clarity"),
    Krita("5.1.109", gives="ṭhañ", sense="prayojana",
          case="prathamā",
          why="प्रयोजनम्. इन्द्रमहः प्रयोजनमस्य "
              "**ऐन्द्रमहिकम्**, a thing whose occasion is the "
              "festival of Indra; गाङ्गामहिकम्"),
    Krita("5.1.110", gives="aṇ", of=("viśākhā", "āṣāḍhā"),
          sense="prayojana", case="prathamā",
          result="mantha-daṇḍa", excepts=("5.1.109",),
          why="विशाखाषाढादण् मन्थदण्डयोः — two words, two affixes "
              "and two THINGS MEANT, matched **यथासंख्यम्**. "
              "विशाखा प्रयोजनमस्य **वैशाखो मन्थः**, a churning "
              "stick; **आषाढो दण्डः**, a staff. "
              "**चूडादिभ्य उपसंख्यानम्** adds a list: चौडम्, "
              "**श्राद्धम्** — the rite whose occasion is faith"),
    Krita("5.1.111", gives="cha", gana="anupravacanādi",
          sense="prayojana", case="prathamā", excepts=("5.1.18",),
          why="अनुप्रवचनादिभ्यश्छः, ठञोऽपवादः. अनुप्रवचनं "
              "प्रयोजनमस्य **अनुप्रवचनीयम्**, उत्त्थापनीयम्.\n\n"
              "Three vārttikas widen and one narrows. "
              "**विशिपूरिपतिरुहिप्रकृतेरनात् सपूर्वपदाद् "
              "उपसंख्यानम्** — any अन-form of four roots with a "
              "word before it: गृहप्रवेशनीयम्, प्रपापूरणीयम्, "
              "अश्वप्रपतनीयम्, प्रासादारोहणीयम्. "
              "**स्वर्गादिभ्यो यद् वक्तव्यः** — a different affix "
              "for a list: **स्वर्ग्यम्, यशस्यम्, आयुष्यम्, "
              "काम्यम्, धन्यम्**. And "
              "**पुण्याहवाचनादिभ्यो लुग् वक्तव्यः** — no affix at "
              "all for three: पुण्याहवाचनं प्रयोजनमस्य "
              "**पुण्याहवाचनम्**, the word standing unchanged"),
    Krita("5.1.112", gives="cha", uttarapada="samāpana",
          sense="prayojana", case="prathamā", excepts=("5.1.18",),
          why="समापनात् सपूर्वपदात्, ठञोऽपवादः — from समापन with a "
              "word before it. छन्दस्समापनं प्रयोजनमस्य "
              "**छन्दःसमापनीयम्**; व्याकरणसमापनीयम्.\n\n"
              "**पदग्रहणं बहुच्पूर्वनिरासार्थम्** — the word पद is "
              "there to shut out a बहुच् standing in front, which "
              "is a prefix and not a word"),
    Krita("5.1.113", gives="ikaṭ", of=("ekāgāra",),
          sense="prayojana", case="prathamā", result="caura",
          why="ऐकागारिकट् चौरे — a form laid down, and the whole "
              "point of laying it down is to NARROW it. एकागारं "
              "प्रयोजनमस्य **ऐकागारिकः चौरः**, a burglar, one "
              "whose object is a single house; ऐकागारिकी.\n\n"
              "**किमर्थमिदं निपात्यते, यावता प्रयोजनमित्येव "
              "सिद्धष्ठञ्? चौरे नियमार्थं वचनम्** — 5.1.109 would "
              "have given the same ठञ् anyway; the rule is stated "
              "to CONFINE the word to a thief, **इह मा भूत् — "
              "एकागारं प्रयोजनमस्य भिक्षोरिति**, so that a monk "
              "with the same single-house object is not called it. "
              "**टकारः कार्यावधारणार्थः; ङीबेव भवति, न ञित्स्वर "
              "इति** — the ट settles which operations follow. "
              "**अपरे पुनरिकट् प्रत्ययं वृद्धिं च निपातयन्ति**",
          keeps_out="ऐकागारिको भिक्षुः"),
    Krita("5.1.114", gives="ikaṭ", also_gives=("ṭhan", "ṭhañ"),
          of=("samānakāla",), adesa="ākāla", sense="ādyanta",
          case="prathamā",
          why="आकालिकड् आद्यन्तवचने — another laid-down form, and "
              "again several things at once: **समानकालशब्दस्य "
              "आकालशब्द आदेशः** and **इकट् प्रत्ययश्च निपात्यते**, "
              "the substitution and the affix together. "
              "**आद्यन्तयोश्चैतद् विशेषणम्** — the sense qualifies "
              "the BEGINNING and the END.\n\n"
              "समानकालावाद्यन्तावस्य **आकालिकः स्तनयित्नुः**, a "
              "thunderclap; **आकालिकी विद्युत्**, lightning, "
              "**जन्मना तुल्यकालविनाशा; उत्पादानन्तरं विनाशिनी "
              "इत्यर्थः** — whose ending is of one time with its "
              "beginning, perishing the instant it arises. A whole "
              "rule for a word meaning *momentary*.\n\n"
              "**आकालाट् ठंश्च; चात् ठञ् च** — a vārttika adds two "
              "more affixes: आकालिका विद्युत्.\n\n"
              "**AND THE ठञ् HEADING ENDS HERE.** **ठञः "
              "पूर्णोऽवधिः** — the sixth time this project has met "
              "the formula, and the narrowest gap yet: the marker "
              "5.1.115 stands one sūtra past the last rule"),
    Krita("5.1.115", gives="vati", sense="tulya", case="tṛtīyā",
          result="kriyā",
          why="तेन तुल्यं क्रिया चेद् वतिः — the sūtra whose word "
              "bounded the ठञ् heading. ब्राह्मणेन तुल्यं वर्तते "
              "**ब्राह्मणवत्**; राजवत्.\n\n"
              "**क्रियाग्रहणं किम्? गुणद्रव्यतुल्ये मा भूत्** — the "
              "likeness must be one of ACTION and not of quality or "
              "substance: पुत्रेण तुल्यः स्थूलः, पुत्रेण तुल्यः "
              "पिङ्गलः, पुत्रेण तुल्यो गोमान् take nothing",
          keeps_out="पुत्रेण तुल्यः स्थूलः"),
    Krita("5.1.116", gives="vati", sense="iva", case="saptamī",
          why="तत्र तस्येव — and one rule for two cases at once. "
              "**तत्रेति सप्तमीसमर्थात् तस्येति षष्ठीसमर्थात् च "
              "इवार्थे वतिः**: मथुरायामिव **मथुरावत्** स्रुघ्ने "
              "प्राकारः, a rampart in Srughna as in Mathurā; "
              "पाटलिपुत्रवत् साकेते परिखा"),
    Krita("5.1.116", gives="vati", sense="iva", case="ṣaṣṭhī",
          why="तत्र तस्येव, the genitive half. देवदत्तस्येव "
              "**देवदत्तवत्** यज्ञदत्तस्य गावः — Yajñadatta's cows "
              "like Devadatta's; यज्ञदत्तवत् देवदत्तस्य दन्ताः"),
    Krita("5.1.117", gives="vati", sense="arha", case="dvitīyā",
          why="तदर्हम्. राजानमर्हति **राजवत् पालनम्**, protection "
              "such as a king deserves; ब्राह्मणवत्, ऋषिवत्, "
              "क्षत्रियवत्"),
    Krita("5.1.118", gives="vati", of_samjna="upasarga",
          sense="svārtha", usage="chandasi",
          why="उपसर्गाच्छन्दसि धात्वर्थे — and the affix changes "
              "nothing but the shape. **उपसर्गात् ससाधने धात्वर्थे "
              "वर्तमानात् स्वार्थे वतिः**: from a preverb standing "
              "for a verbal sense together with its means. "
              "यद्**उद्वतो॑ नि॒वतो॒** यासि॒ बप्स॒द् (ऋ०१०.१४२.४) — "
              "**उद्गतानि निगतानि च**"),
    Krita("5.1.119", gives="tva", also_gives=("tal",), sense="bhāva",
          case="ṣaṣṭhī",
          why="तस्य भावस्त्वतलौ — and the vṛtti says what भाव means "
              "in this grammar. **भवतोऽस्मादभिधानप्रत्ययाविति "
              "भावः; शब्दस्य प्रवृत्तिनिमित्तं भावशब्देनोच्यते** — "
              "a भाव is that from which the naming and the notion "
              "arise, the GROUND on which a word is applied at all. "
              "अश्वस्य भावः **अश्वत्वम्, अश्वता**; गोत्वम्, गोता"),
    Krita("5.1.120", gives="tva", also_gives=("tal",),
          sense="bhāva", case="ṣaṣṭhī", heading=True,
          why="आ च त्वात्. **ब्रह्मणस्त्वः इति वक्ष्यति। आ एतस्मात् "
              "त्वसंशब्दनाद् यानित ऊर्ध्वमनुक्रमिष्यामः, तत्र "
              "त्वतलौ प्रत्ययावधिकृतौ वेदितव्यौ** — त्व and तल् are "
              "governed as far as 5.1.136, and the आ is अभिविधि "
              "again, so that rule is taken in.\n\n"
              "**AND THIS HEADING DOES NOT DISPLACE WHAT IT MEETS — "
              "IT STANDS BESIDE IT.** **अपवादैः सह समावेशार्थं "
              "वचनम्**: the rule is stated so that त्व and तल् come "
              "TOGETHER WITH the affixes that would otherwise "
              "displace them. प्रथिमा by 5.1.122 and पार्थवम् and "
              "**पृथुत्वम्** and **पृथुता**, all four standing. "
              "Every other heading of this pāda was displaced by its "
              "own exceptions; this one is not.\n\n"
              "**कर्मणि च विधानार्थम्** — and it reaches the "
              "कर्मन् sense 5.1.124 will add. **चकारो "
              "नञ्स्नञ्भ्यामपि समावेशार्थः**: the च puts them "
              "beside नञ् and स्नञ् too — स्त्रैणम् and "
              "**स्त्रीत्वम्** and स्त्रीता; पौंस्नम् and "
              "पुंस्त्वम् and पुंस्ता"),
    Krita("5.1.121", pre="nañ", sense="bhāva", case="ṣaṣṭhī",
          refuses=True, excludes=("catur", "saṃgata", "lavaṇa",
                                  "vaṭa", "yudha", "katara", "sala",
                                  "sa"),
          why="न नञ्पूर्वात् तत्पुरुषाद् "
              "अचतुरसंगतलवणवटयुधकतरसलसेभ्यः — a प्रतिषेध, and it "
              "governs the whole stretch: **इत उत्तरे ये "
              "भावप्रत्ययाः ते नञ्पूर्वात् तत्पुरुषाद् न भवन्ति "
              "चतुरादीन् वर्जयित्वा**. अपतित्वम्, अपतिता — the "
              "त्व and तल् stand, and the special affixes do not.\n\n"
              "Three conditions, each with its counter-example. "
              "**नञ्पूर्वादिति किम्?** बार्हस्पत्यम्, "
              "प्राजापत्यम् — no नञ् there. "
              "**तत्पुरुषादिति किम्?** नास्य पटवः सन्तीत्यपटुः, "
              "तस्य भाव **आपटवम्** — a बहुव्रीहि, not a तत्पुरुष. "
              "**अचतुरादिभ्य इति किम्?** आचतुर्यम्, आसंगत्यम्, "
              "आलवण्यम्, आवट्यम्, आबुध्यम्, आकत्यम्, आरस्यम्, "
              "**आलस्यम्** — the eight the rule excepts",
          keeps_out="बार्हस्पत्यम्, आपटवम्, आलस्यम्"),
    Krita("5.1.122", gives="imanic", gana="pṛthvādi", sense="bhāva",
          case="ṣaṣṭhī", optional=True,
          why="पृथ्वादिभ्य इमनिच् वा. **वावचनम् अणादेः "
              "समावेशार्थम्** — and the option is there so that the "
              "अण् and the rest come TOO, not so that one is "
              "chosen. पृथोर्भावः **प्रथिमा, पार्थवम्**, and "
              "**त्वतलौ सर्वत्र भवत एव**: पृथुत्वम्, पृथुता stand "
              "everywhere. Four forms for one sense.\n\n"
              "6.4.154 तुरिष्ठेमेयस्सु and 6.4.155 टेः give the "
              "टि-elision, 6.4.161 र ऋतो हलादेर्लघोः the र.\n\n"
              "पृथु, मृदु, महत्, पटु, तनु, लघु, बहु, साधु, वेणु, "
              "आशु, बहुल, गुरु, दण्ड, ऊरु, खण्ड, चण्ड, बाल, "
              "अकिंचन, होड, पाक, वत्स, मन्द, स्वादु, ह्रस्व, दीर्घ, "
              "प्रिय, वृष, ऋजु, क्षिप्र, क्षुद्र — पृथ्वादिः"),
    Krita("5.1.123", gives="ṣyañ", also_gives=("imanic",),
          of_samjna="varṇa", sense="bhāva", case="ṣaṣṭhī",
          why="वर्णदृढादिभ्यः ष्यञ् च; the वर्ण half — from the "
              "words for COLOURS. शुक्लस्य भावः **शौक्ल्यम्, "
              "शुक्लिमा, शुक्लत्वम्, शुक्लता**; कार्ष्ण्यम्, "
              "कृष्णिमा. **षकारो ङीषर्थः** — the ष is for the "
              "feminine: औचिती, याथाकामी"),
    Krita("5.1.123", gives="ṣyañ", also_gives=("imanic",),
          gana="dṛḍhādi", sense="bhāva", case="ṣaṣṭhī",
          why="वर्णदृढादिभ्यः ष्यञ् च, the दृढादि half. "
              "**दार्ढ्यम्, द्रढिमा, दृढत्वम्, दृढता**. दृढ, "
              "परिवृढ, भृश, कृश, चक्र, आम्र, लवण, ताम्र, अम्ल, "
              "शीत, उष्ण, जड, बधिर, पण्डित, मधुर, मूर्ख, मूक, "
              "**वेर्यातलाभमतिमनःशारदानाम्** (ग०सू०११४), "
              "**समो मतिमनसोः** (ग०सू०११५) — दृढादिः"),
    Krita("5.1.124", gives="ṣyañ", of_samjna="guṇavacana",
          sense="bhāva-karman", case="ṣaṣṭhī",
          why="गुणवचनब्राह्मणादिभ्यः कर्मणि च; the गुणवचन half. "
              "**गुणमुक्तवन्तो गुणवचनाः** — the words that have "
              "spoken a quality. And the च adds a second sense: "
              "**कर्मशब्दः क्रियावचनः**, कर्मन् here means an "
              "ACTIVITY. जडस्य भावः कर्म वा **जाड्यम्**.\n\n"
              "**आ पादपरिसमाप्तेर्भावकर्माधिकारः** — and from here "
              "the भाव-and-कर्मन् sense governs to the END OF THE "
              "PĀDA, so every rule after this one has both"),
    Krita("5.1.124", gives="ṣyañ", gana="brāhmaṇādi",
          sense="bhāva-karman", case="ṣaṣṭhī",
          why="गुणवचनब्राह्मणादिभ्यः कर्मणि च, the ब्राह्मणादि "
              "half — and the list is open. "
              "**ब्राह्मणादिराकृतिगणः; आदिशब्दः प्रकारवचनः**: an "
              "आकृतिगण, a list defined by its shape and not its "
              "members, and the word *and the rest* means *and "
              "things of that kind*. **ब्राह्मण्यम्**, माणव्यम्.\n\n"
              "**चातुर्वर्ण्यादीनां स्वार्थ उपसंख्यानम्** adds a "
              "set in their OWN sense: **चत्वार एव वर्णाश् "
              "चातुर्वर्ण्यम्**, the four classes as such; "
              "त्रैलोक्यम्, षाड्गुण्यम्, सैन्यम्, सामीप्यम्, "
              "औपम्यम्, सौख्यम्"),
    Krita("5.1.125", gives="yat", of=("stena",), adesa="stey",
          sense="bhāva-karman", case="ṣaṣṭhī", excepts=("5.1.124",),
          why="स्तेनाद् यन्नलोपश्च — the affix and the dropping of "
              "the न् together. स्तेनस्य भावः कर्म वा "
              "**स्तेयम्**, theft.\n\n"
              "**स्तेनादिति केचिद् योगविभागं कुर्वन्ति** — some "
              "split the rule in two: **स्तेनात् ष्यञ् भवति**, "
              "स्तैन्यम्, **ततो यन्नलोपश्च**, स्तेयम्. Two forms "
              "where the unsplit rule gives one"),
    Krita("5.1.126", gives="ya", of=("sakhi",),
          sense="bhāva-karman", case="ṣaṣṭhī", excepts=("5.1.124",),
          why="सख्युर्यः. सख्युर्भावः कर्म वा **सख्यम्**, "
              "friendship. **दूतवणिग्भ्यां चेति वक्तव्यम्** adds "
              "two: दूत्यम्, वणिज्यम्. **कथं वाणिज्यम्? "
              "ब्राह्मणादित्वात्** — and the other form comes from "
              "the open list of 5.1.124"),
    Krita("5.1.127", gives="ḍhak", of=("kapi", "jñāti"),
          sense="bhāva-karman", case="ṣaṣṭhī", excepts=("5.1.124",),
          why="कपिज्ञात्योर्ढक्. कपेर्भावः कर्म वा **कापेयम्**; "
              "**ज्ञातेयम्**, kinship.\n\n"
              "**यथासंख्यम् अर्थयोः सर्वत्रैवात्र प्रकरणे न "
              "इष्यते** — and the matching in order is not wanted "
              "anywhere in this section BETWEEN THE TWO SENSES. So "
              "each of भाव and कर्मन् goes with each base, and no "
              "rule of the stretch pairs them off"),
    Krita("5.1.128", gives="yak", uttarapada="pati",
          sense="bhāva-karman", case="ṣaṣṭhī", excepts=("5.1.124",),
          why="पत्यन्तपुरोहितादिभ्यो यक्; the पत्यन्त half — from "
              "any stem ending in पति. सेनापतेर्भावः कर्म वा "
              "**सैनापत्यम्**; गार्हपत्यम्, प्राजापत्यम्"),
    Krita("5.1.128", gives="yak", gana="purohitādi",
          sense="bhāva-karman", case="ṣaṣṭhī", excepts=("5.1.124",),
          why="पत्यन्तपुरोहितादिभ्यो यक्, the पुरोहितादि half. "
              "**पौरोहित्यम्, राज्यम्**. पुरोहित, राजन्, "
              "संग्रामिक, एषिक, वर्मित, खण्डिक, दण्डिक, छत्रिक, "
              "बाल, मन्द, कृषिक, पत्रिक, सूचिक, सारथिक, अञ्जलिक, "
              "**राजासे** (ग०सू०११९) — पुरोहितादिः"),
    Krita("5.1.129", gives="añ", of_samjna="prāṇabhṛj-jāti",
          sense="bhāva-karman", case="ṣaṣṭhī", excepts=("5.1.124",),
          why="प्राणभृज्जातिवयोवचनोद्गात्रादिभ्योऽञ्; the "
              "प्राणभृज्जाति half — from the words for KINDS of "
              "living creature. अश्वस्य भावः कर्म वा **आश्वम्**; "
              "औष्ट्रम्"),
    Krita("5.1.129", gives="añ", of_samjna="vayovacana",
          sense="bhāva-karman", case="ṣaṣṭhī", excepts=("5.1.124",),
          why="प्राणभृज्जातिवयोवचनोद्गात्रादिभ्योऽञ्, the वयोवचन "
              "half — from the words for stages of life. "
              "**कौमारम्, कैशोरम्**"),
    Krita("5.1.129", gives="añ", gana="udgātrādi",
          sense="bhāva-karman", case="ṣaṣṭhī", excepts=("5.1.124",),
          why="प्राणभृज्जातिवयोवचनोद्गात्रादिभ्योऽञ्, the "
              "उद्गात्रादि half — priests and a few besides. "
              "**औद्गात्रम्, औन्नेत्रम्**. उद्गातृ, उन्नेतृ, "
              "प्रतिहर्तृ, रथगणक, पक्षिगणक, सुष्ठु, दुष्ठु, "
              "अध्वर्यु, वधू, **सुभग मन्त्रे** (ग०सू०१२०) — "
              "उद्गात्रादिः"),
    Krita("5.1.130", gives="aṇ", uttarapada="hāyana",
          sense="bhāva-karman", case="ṣaṣṭhī", excepts=("5.1.124",),
          why="हायनान्तयुवादिभ्योऽण्; the हायनान्त half. "
              "द्विहायनस्य भावः कर्म वा **द्वैहायनम्**; "
              "त्रैहायनम्"),
    Krita("5.1.130", gives="aṇ", gana="yuvādi",
          sense="bhāva-karman", case="ṣaṣṭhī", excepts=("5.1.124",),
          why="हायनान्तयुवादिभ्योऽण्, the युवादि half. "
              "**यौवनम्, स्थाविरम्**. **श्रोत्रियस्य यलोपश्च "
              "वाच्यः** — and श्रोत्रिय drops its य: "
              "**श्रौत्रम्**. युवन्, स्थविर, होतृ, यजमान, "
              "कमण्डलु, सुहृद्, यातृ, श्रवण, कुस्त्री, सुभ्रातृ, "
              "वृषल, क्षेत्रज्ञ, परिव्राजक, कुशल, चपल, निपुण, "
              "पिशुन, सब्रह्मचारिन्, कुतूहल, अनृशंस — युवादिः"),
    Krita("5.1.131", gives="aṇ", stem_final="ik", upadha="laghu",
          sense="bhāva-karman", case="ṣaṣṭhī", excepts=("5.1.124",),
          why="इगन्ताच्च लघुपूर्वात् — and the vṛtti gives two "
              "analyses of the compound. On the first, "
              "**लघुः पूर्वो यस्मादिकः तदन्तात् प्रातिपदिकात्**: "
              "from a stem ending in an इक् that has a LIGHT sound "
              "before it — **इक्संनिधानादिक इति विज्ञायते**, the "
              "*it* being the इक् from its standing next to it. "
              "**अपरे तत्पुरुषकर्मधारयं वर्णयन्ति**, and on that "
              "reading **अस्मिन् व्याख्यानेऽन्तग्रहणमतिरिच्यते; "
              "लघुपूर्वादिक इत्येतावदेव वाच्यं स्यात्** — the word "
              "अन्त would be redundant. A reading rejected because "
              "it makes a word of the sūtra idle.\n\n"
              "शुचेर्भावः कर्म वा **शौचम्**; मौनम्, नागरम्, "
              "पाटवम्, लाघवम्. **इगन्तादिति किम्?** पटत्वम्. "
              "**लघुपूर्वादिति किम्?** कण्डूत्वम्, पाण्डुत्वम्. "
              "**कथं काव्यम्? ब्राह्मणादिषु कविशब्दो द्रष्टव्यः** — "
              "and the open list of 5.1.124 catches what this rule "
              "misses",
          keeps_out="पटत्वम्, कण्डूत्वम्"),
    Krita("5.1.132", gives="vuñ", upadha="ya", result="gurūpottama",
          sense="bhāva-karman", case="ṣaṣṭhī", excepts=("5.1.124",),
          why="योपधाद् गुरूपोत्तमाद् वुञ् — and उपोत्तम is defined "
              "on the spot. **त्रिप्रभृतीनाम् अन्तस्य समीपम् "
              "उपोत्तमम्** — in a word of three syllables or more, "
              "the one next to the last; **गुरुरुपोत्तमं यस्य तद् "
              "गुरूपोत्तमम्**, and that syllable must be heavy. "
              "रमणीयस्य भावः कर्म वा **रामणीयकम्**; वासनीयकम्.\n\n"
              "**योपधादिति किम्?** विमानत्वम्. "
              "**गुरूपोत्तमादिति किम्?** क्षत्रियत्वम्. "
              "**सहायाद् वेति वक्तव्यम्**: साहायकम्, साहाय्यम्",
          keeps_out="विमानत्वम्, क्षत्रियत्वम्"),
    Krita("5.1.133", gives="vuñ", of_samjna="dvandva",
          sense="bhāva-karman", case="ṣaṣṭhī", excepts=("5.1.124",),
          why="द्वन्द्वमनोज्ञादिभ्यश्च; the द्वन्द्व half — from a "
              "copulative compound. गोपालपशुपालानां भावः कर्म वा "
              "**गौपालपशुपालिका**; शैष्योपाध्यायिका, "
              "कौत्सकुशिकिका"),
    Krita("5.1.133", gives="vuñ", gana="manojñādi",
          sense="bhāva-karman", case="ṣaṣṭhī", excepts=("5.1.124",),
          why="द्वन्द्वमनोज्ञादिभ्यश्च, the मनोज्ञादि half. "
              "**मानोज्ञकम्, काल्याणकम्**. मनोज्ञ, कल्याण, "
              "प्रियरूप, छान्दस, छात्र, मेधाविन्, अभिरूप, आढ्य, "
              "कुलपुत्र, श्रोत्रिय, चोर, धूर्त, वैश्वदेव, युवन्, "
              "ग्रामपुत्र, अमुष्यपुत्र, शतपुत्र, कुशल — मनोज्ञादिः"),
    Krita("5.1.134", gives="vuñ", of_samjna="gotra-caraṇa",
          sense="bhāva-karman", case="ṣaṣṭhī",
          result="ślāghā-atyākāra-tadaveta", excepts=("5.1.124",),
          why="गोत्रचरणाच्छ्लाघात्याकारतदवेतेषु — three settings, "
              "each glossed. **श्लाघा विकत्थनम्**, boasting; "
              "**अत्याकारः पराधिक्षेपः**, running others down; "
              "**तदवेतस्तत्प्राप्तस्तज्ज्ञो वा**, one who has come "
              "to it or knows it.\n\n"
              "**गार्गिकया श्लाघते** — boasts of being a Gārgya, "
              "**गार्ग्यत्वेन विकत्थत इत्यर्थः**; "
              "**गार्गिकयात्याकुरुते**, uses it to put others down; "
              "**गार्गिकामवेतः**, has come into it. "
              "**श्लाघादिष्विति किम्?** गार्ग्यत्वम्, कठत्वम् — "
              "outside those three it is the plain त्व",
          keeps_out="गार्ग्यत्वम्"),
    Krita("5.1.135", gives="cha", of_samjna="hotrā",
          sense="bhāva-karman", case="ṣaṣṭhī", excepts=("5.1.124",),
          why="होत्राभ्यश्छः. **होत्राशब्द ऋत्विग्विशेषवचनः** — "
              "होत्रा names a PARTICULAR kind of officiant. "
              "अच्छावाकस्य भावः कर्म वा **अच्छावाकीयम्**; "
              "मित्रावरुणीयम्, ब्राह्मणाच्छंसीयम्, आग्नीध्रीयम्, "
              "पोत्रीयम्. **बहुवचनं स्वरूपविधिनिरासार्थम्** — the "
              "plural in the sūtra is there to stop the rule "
              "applying to the WORD होत्रा itself"),
    Krita("5.1.136", gives="tva", of=("brahman",),
          of_samjna="hotrā", sense="bhāva-karman", case="ṣaṣṭhī",
          excepts=("5.1.135",),
          why="ब्रह्मणस्त्वः, छस्यापवादः — and the last rule of the "
              "pāda. **होत्राभ्य इत्यनुवर्तते**, so the ब्रह्मन् "
              "meant is the officiant of that name. ब्रह्मणो भावः "
              "कर्म वा **ब्रह्मत्वम्**.\n\n"
              "**AND THE AFFIX IS NAMED WHERE A REFUSAL WOULD HAVE "
              "DONE.** **नेति वक्तव्ये त्ववचनं तलो बाधनार्थम्** — "
              "the rule could have said *not छ*, and the त्व would "
              "have come by 5.1.119 anyway. Naming त्व instead "
              "shuts out the तल् that would have come with it. A "
              "प्रतिषेध would have left two affixes; a विधि leaves "
              "one.\n\n"
              "**यस्तु जातिशब्दो ब्राह्मणपर्यायो ब्रह्मन्शब्दः, "
              "ततस्त्वतलौ भवत एव** — and where ब्रह्मन् is the "
              "ordinary word for a brahmin, both come back: "
              "ब्रह्मत्वम्, ब्रह्मता.\n\n"
              "**भवनावधिकयोर्नञ्स्नञोरधिकारः समाप्तः** — and with "
              "that the heading closes. इति श्रीजयादित्यविरचितायां "
              "काशिकायां वृत्तौ पञ्चमाध्यायस्य प्रथमः पादः",
          keeps_out="ब्रह्मता of the officiant"),
)


@dataclass(frozen=True)
class FitFor:
    """What the resolver answers with."""

    affix: str
    sutra: str
    why: str
    also_gives: Tuple[str, ...] = ()
    case: str = ""
    optional: bool = False
    #: True where the affix was REMOVED rather than given.
    lup: bool = False
    #: True where the answer came through 5.1.5, 5.1.12 or 5.1.16's
    #: यथाविहितम् rather than from a rule that names an affix.
    borrowed: bool = False
    #: The rule that REFUSED what would otherwise have come. The
    #: answer's own `sutra` names what supplies, since a प्रतिषेध
    #: does not govern what it excepts.
    blocked_by: str = ""
    adesa: str = ""
    augment: str = ""
    excepts: Tuple[str, ...] = ()


def _senses_under(row: Krita) -> Tuple[str, ...]:
    """
    Which senses a row serves when it names none of its own — and it
    is decided by where the row STANDS, since a heading governs a
    stretch and every rule inside that stretch inherits its senses.

    5.1.17 is the boundary, on its own vṛtti's word: **छयतोः
    पूर्णोऽवधिः। इतः परमन्यः प्रत्ययो विधीयते.**
    """
    _, _, number = row.sutra.rsplit(".", 2)
    where = int(number)
    if where <= 17:
        return CHA_SENSES
    if where <= 114:
        return THAN_SENSES
    if where <= 118:
        return VATI_SENSES
    return BHAVA_SENSES


def _reaches(row: Krita, stem: str, gana: str, sense: str, case: str,
             result: str, samjna: str, stem_final: str,
             uttarapada: str, pre: str, compounded: str,
             vowels: str, usage: str, upadha: str) -> bool:
    if row.heading:
        # A heading answers where nothing else does, and `_default`
        # picks which one. Left in the match it would tie at zero
        # conditions with the other two and the earliest would win.
        return False
    if row.of and stem not in row.of:
        return False
    if row.gana and gana != row.gana:
        return False
    if row.sense:
        if sense and sense != row.sense:
            return False
    elif sense and sense not in _senses_under(row):
        # A row naming no sense of its own is not free of sense: it
        # serves the senses of ITS heading, which is what
        # प्राक्क्रीतीयेष्वर्थेषु and आर्हीयेष्वर्थेषु each mean.
        # That is also how 5.1.5's यथाविहितम् finds 5.1.2 for गो
        # and cannot find 5.1.20 for it.
        return False
    if row.case and case and case != row.case:
        return False
    if row.result and result != row.result:
        return False
    if row.of_samjna and samjna != row.of_samjna:
        return False
    if row.stem_final and stem_final != row.stem_final:
        return False
    if row.vowels and vowels != row.vowels:
        return False
    if row.usage and usage != row.usage:
        return False
    if row.upadha and upadha != row.upadha:
        return False
    if row.uttarapada and uttarapada != row.uttarapada:
        return False
    if row.pre and pre != row.pre:
        return False
    if row.compounded == "no" and compounded == "yes":
        return False
    if row.excludes and (stem in row.excludes
                         or samjna in row.excludes):
        return False
    return True


def _supplies(row: Krita, wants: str) -> bool:
    """Whether the row gives the affix asked for."""
    return (not wants
            or wants == row.gives
            or wants in row.also_gives)


def _how_specific(row: Krita) -> int:
    """
    A named base is narrowest; the sense and the case are widest,
    since both are carried down from a heading.
    """
    return (
        7 * bool(row.of)
        + 6 * bool(row.gana)
        + 5 * bool(row.of_samjna)
        + 5 * bool(row.uttarapada)
        + 4 * bool(row.pre)
        + 4 * bool(row.stem_final)
        + 3 * bool(row.vowels)
        + 3 * bool(row.upadha)
        + 3 * bool(row.usage)
        + 3 * bool(row.result)
        + 3 * (row.compounded == "no")
        + 2 * bool(row.sense)
        + 1 * bool(row.case)
    )


def _answer(row: Krita, case: str = "") -> FitFor:
    """
    The case an answer carries is the row's where the row states one
    and the question's otherwise — because from 5.1.19 to 5.1.36 the
    rules state an affix and no case at all, and the case those
    affixes stand with is whatever the sense-rule reaching them said.
    """
    with_case = row.case or case
    if row.lup:
        return FitFor("", row.sutra, row.why, case=with_case,
                      optional=row.optional, lup=True,
                      excepts=row.excepts)
    return FitFor(row.gives, row.sutra, row.why,
                  also_gives=row.also_gives, case=with_case,
                  optional=row.optional, adesa=row.adesa,
                  augment=row.augment, excepts=row.excepts)


def fit_for(stem: str = "", *, gana: str = "", sense: str = "",
            case: str = "", result: str = "", samjna: str = "",
            stem_final: str = "", uttarapada: str = "",
            pre: str = "", compounded: str = "", vowels: str = "",
            usage: str = "", upadha: str = "",
            wants: str = "") -> FitFor:
    """
    5.1.1–30 — the affix for what a thing is good for, made for,
    might belong to, or is worth.

    `sense` is हित, तदर्थ, तदस्य-स्यात् or आर्हीय; `case` the
    relation the base stands in — चतुर्थी for a purpose, प्रथमा at
    5.1.16, तृतीया for a price.

    Three of these rules name only a sense and leave the affix
    **यथाविहितम्**. Where one of those wins, the question is asked
    again without the sense, and whatever answers it is the answer —
    which is the fall-through executing the अतिदेश, not a shortcut
    around it.

    Where nothing is reached the answer is the heading whose range
    the sense falls in: छ up to 5.1.17, ठञ् from 5.1.18.
    """
    matched = [
        row for row in KRITA_TABLE
        if _reaches(row, stem, gana, sense, case, result, samjna,
                    stem_final, uttarapada, pre, compounded,
                    vowels, usage, upadha)
        and _supplies(row, wants)
    ]
    if not matched:
        return _default(sense, stem, samjna)
    row = max(matched, key=_how_specific)
    if row.refuses:
        # **न नञ्पूर्वात् तत्पुरुषात्** takes away the special भाव
        # affixes and leaves 5.1.119's त्व and तल्. So the answer
        # names the rule that SUPPLIES and records the refusal
        # beside it: a प्रतिषेध does not govern what it excepts.
        supplying = [other for other in matched
                     if not other.refuses and other.gives]
        beaten = (max(supplying, key=_how_specific) if supplying
                  else _by_sutra("5.1.119"))
        answer = _answer(beaten, case)
        return FitFor(answer.affix, beaten.sutra, row.why,
                      also_gives=answer.also_gives, case=answer.case,
                      blocked_by=row.sutra, excepts=row.excepts)
    if not row.borrows:
        return _answer(row, case)

    # यथाविहितम् — the sense is named and the affix is not, so ask
    # again as though this rule were not there and let the base
    # answer for itself. Only the sense-rules are held out, since a
    # fall-through cannot fall into another; the sense itself stays,
    # because a rule under one heading must not answer a question
    # asked under a different heading's sense.
    again = [
        r for r in KRITA_TABLE
        if not r.borrows
        and _reaches(r, stem, gana, sense, case, result, samjna,
                     stem_final, uttarapada, pre, compounded,
                     vowels, usage, upadha)
        and _supplies(r, wants)
    ]
    if not again:
        found = _default(sense, stem, samjna)
    else:
        found = _answer(max(again, key=_how_specific), case)
    return FitFor(found.affix, found.sutra, found.why,
                  also_gives=found.also_gives, case=row.case,
                  optional=found.optional, lup=found.lup,
                  borrowed=True, adesa=found.adesa,
                  augment=found.augment, excepts=found.excepts)


def _default(sense: str, stem: str = "", samjna: str = "") -> FitFor:
    """
    The heading that governs where no rule of the section is reached
    — and which heading that is depends on the sense AND on the base.

    छ covers हित, तदर्थ and तदस्य-स्यात्, the senses named between
    5.1.1 and 5.1.17. आर्हीय is ठक् by 5.1.19 — except for the three
    the rule keeps out by name, and those fall through to the ठञ् of
    5.1.18, which is exactly the vṛtti's own counter-examples:
    गौपुच्छिकम्, षाष्टिकम्, प्रास्थिकम्.
    """
    if sense in BHAVA_SENSES:
        # **अपवादैः सह समावेशार्थं वचनम्** — 5.1.120's त्व and तल्
        # are not displaced by the rules under them; they stand
        # beside whatever those give.
        row = _by_sutra("5.1.120")
    elif sense in VATI_SENSES:
        row = _by_sutra("5.1.115")
    elif sense in CHA_SENSES or (
            sense and sense not in THAN_SENSES):
        row = _by_sutra("5.1.1")
    elif sense in LATER_SENSES:
        # **अतः परं प्राग्वतीयष्ठञेव भवति** — past 5.1.71 the ठक्
        # is spent and the ठञ् of 5.1.18 answers alone.
        row = _by_sutra("5.1.18")
    else:
        arhiya = _by_sutra("5.1.19")
        kept_out = (stem in arhiya.excludes or samjna in arhiya.excludes)
        row = _by_sutra("5.1.18") if kept_out else arhiya
    return FitFor(row.gives, row.sutra, row.why, case=row.case)


def _by_sutra(sutra_id: str) -> Krita:
    for row in KRITA_TABLE:
        if row.sutra == sutra_id:
            return row
    raise KeyError(sutra_id)


def cha_run() -> FitFor:
    """
    How far छ is the affix — and the marker is twenty sūtras past
    the end, which is the widest of the four gaps.

    5.1.1 lifts क्रीत out of 5.1.37 to fix its limit, but 5.1.18
    opens ठञ् inside that range, and 5.1.17 closes the account:
    **छयतोः पूर्णोऽवधिः। इतः परमन्यः प्रत्ययो विधीयते.**
    """
    opens, closes = CHA_RUN
    return FitFor(
        "cha", opens,
        "छ is the affix from %s to %s. The marker is %s तेन "
        "क्रीतम् — but 5.1.18 opens ठञ् inside the range, and %s "
        "says छयतोः पूर्णोऽवधिः, the same formula 4.4.74 and "
        "4.4.144 used" % (opens, closes, CHA_MARKER, closes))


def than_run() -> FitFor:
    """
    ठञ् from 5.1.18, bounded by lifting वति out of 5.1.115 — and
    closing one sūtra short of it, **ठञः पूर्णोऽवधिः**.

    The narrowest of the six gaps between a heading's marker and its
    last rule, and the reason is the plainest: 5.1.115 gives वति
    itself, so the heading cannot reach the rule it is named from.
    """
    opens, closes = THAN_RUN
    return FitFor(
        "ṭhañ", opens,
        "ठञ् is the affix from %s to %s. The marker is %s तेन "
        "तुल्यं क्रिया चेद् वतिः, one sūtra further on, and %s "
        "says ठञः पूर्णोऽवधिः — the sixth heading in this project "
        "to close somewhere other than where its own name points"
        % (opens, closes, THAN_MARKER, closes))


def arhiya_run() -> FitFor:
    """
    And ठक् inside ठञ् — the one heading of the four that INCLUDES
    the sūtra bounding it, because 5.1.19 opens with आ and not
    प्राक्: **अभिविधावयमाकारः, तेनार्हत्यर्थेऽपि ठग् भवत्येव.**
    """
    opens, closes = ARHIYA_RUN
    return FitFor(
        "ṭhak", opens,
        "ठक् is the affix from %s to %s. Its marker is %s तदर्हति, "
        "and this heading REACHES that marker instead of stopping "
        "short of it — an अभिविधि and not a प्राक्, तेनार्हत्यर्थे "
        "ऽपि ठग् भवत्येव — then runs eight rules further, until "
        "%s says आर्हीयाणां ठगादीनां पूर्णोऽवधिः. Enjoined inside "
        "the ठञ् heading as its exception, गोपुच्छ and संख्या and "
        "परिमाण left out"
        % (opens, closes, ARHIYA_MARKER, closes))


def tva_run() -> FitFor:
    """
    त्व and तल् from 5.1.120 — and the one heading of the seven that
    is not displaced by its own exceptions.

    **अपवादैः सह समावेशार्थं वचनम्; त्वतलौ सर्वत्र भवत एव** — the
    rule is stated so that they come TOGETHER WITH the special
    affixes, which is why पृथु has four forms and not one.
    """
    opens, closes = TVA_RUN
    return FitFor(
        "tva", opens,
        "त्व and तल् are the affixes from %s to %s INCLUSIVE — आ "
        "and not प्राक्, so 5.1.136 ब्रह्मणस्त्वः is taken in, and "
        "that rule ends the pāda. The one heading whose marker and "
        "last rule are the same sūtra, and the one that stands "
        "BESIDE its exceptions rather than being beaten by them"
        % (opens, closes),
        also_gives=("tal",))


def kala_run() -> FitFor:
    """
    And a heading that gives no affix — only the condition that the
    base be a word for TIME.

    **कालादित्यधिकारः। यदित ऊर्ध्वम् अनुक्रमिष्यामः कालादित्येवं
    तद् वेदितव्यम्.** It stands inside the ठञ् heading and does not
    compete with it, which is why the rules under it still give ठञ्.
    """
    opens, closes = KALA_RUN
    return FitFor(
        "", opens,
        "कालात् governs from %s to %s — a heading that carries a "
        "CONDITION and not an affix, so the ठञ् of 5.1.18 goes on "
        "supplying underneath it. Its marker is %s, which 5.1.78 "
        "names as कालादित्यधिकारो व्युष्टादिभ्योऽण् इति यावत्, and "
        "%s stops one short of it: कालाधिकारस्य पूर्णोऽवधिः"
        % (opens, closes, KALA_MARKER, closes))


def provisions_for(sutra_id: str) -> Tuple[Krita, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in KRITA_TABLE if row.sutra == sutra_id)
