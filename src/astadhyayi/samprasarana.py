# -*- coding: utf-8 -*-
"""
६.१.१३–४४ — संप्रसारण, and a semivowel gives up its consonant.

1.1.45 already gave the name: **इग्यणः संप्रसारणम्** — where an इक्
stands in the room of a यण्, that vowel is called संप्रसारण. This
section is where it is ORDERED. य् becomes इ, व् becomes उ, र् becomes
ऋ, ल् becomes ऌ, and the root that had a consonant cluster now has a
vowel: वच् → उच्, यज् → इज्, ग्रह् → गृह्, ह्वे → हू.

The heading is carried by अनुवृत्ति and the Kāśikā says exactly how
far: at 6.1.13, **संप्रसारणमिति चाधिक्रियते विभाषा परेः इति यावत्** —
the word governs down to 6.1.44 and stops there. Thirty-two sūtras.

**WHAT THE SECTION IS ARRANGED BY.** Not by root and not by affix, but
by the pairing of the two. 6.1.15 names eleven roots and one condition
(किति); 6.1.16 names nine more and adds ङिति; and from 6.1.18 onward
each rule is one root with one affix — स्वापि before चङ्, ह्व before
णि, व्ये before ल्यप्. Five of them substitute a finished form instead
(की, स्फी, पी, शृ, व), and seven REFUSE.

**THE ORDER IS FIXED BY 6.1.37.** न संप्रसारणे संप्रसारणम् — once one
semivowel has been vocalised, the one before it is not. व्यध् has both
व् and य्, and only the य् goes: विद्धः, never *उद्धः. The Kāśikā
reads the very existence of the rule as the proof of which one goes
first — **पूर्वस्य च प्रसक्तं प्रतिषिध्यते**: had the FIRST been the
one vocalised, no semivowel would ever stand before a vocalised one and
the prohibition would have nothing to forbid.

**AND ONE MAXIM DECIDES EVERY CONTEST.** **संप्रसारणं संप्रसारणाश्रयं
च बलीयो भवति** — vocalisation, and whatever depends on it, wins. It is
why 6.1.31 does the संप्रसारण of श्वि before the vṛddhi that is
अन्तरङ्ग, and why 6.1.32's ह्वा never takes the युक् of 7.3.37.

**WHAT THIS MODULE DOES NOT DO.** It reports which rule of 6.1.13–44
applies and what it orders. It does not rewrite the root: turning वच्
into उक्तः needs 8.2.30, 6.4.2 and the निष्ठा rules, none of which is
codified. The forms in the notes are the Kāśikā's own.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: Where the word संप्रसारणम् governs, on the Kāśikā's own statement
#: at 6.1.13: **संप्रसारणमिति चाधिक्रियते विभाषा परेः इति यावत्**.
SAMPRASARANA_RUN: Tuple[str, str] = ("6.1.13", "6.1.44")

#: 6.1.15's eleven — वचि, स्वपि, and the nine यजादि that close the
#: भ्वादि gaṇa. The Kāśikā names the run by its ends: **यजादयो
#: यज देवपूजासंगतिकरणदानेषु इत्यतः प्रभृति आगणान्ताः**.
VACYADI: Tuple[str, ...] = (
    "vac", "svap",
    "yaj", "vap", "vah", "vas", "veñ", "vyeñ", "hveñ", "vad", "śvi",
)

#: 6.1.16's nine, which take the same treatment before a ङित् affix
#: as well. वयि is the आदेश 2.4.41 puts in for वेञ् before लिट्.
GRAHYADI: Tuple[str, ...] = (
    "grah", "jyā", "vayi", "vyadh", "vaś", "vyac", "vraśc",
    "prach", "bhrasj",
)

#: The maxim that settles every ordering contest in the section, cited
#: at 6.1.31 and again at 6.1.32.
BALIYAS: str = "संप्रसारणं संप्रसारणाश्रयं च बलीयो भवति"

#: What 6.1.36 lays down whole, for the छन्दस् alone. Each is a form
#: no rule derives — the vocalisation is part of the citation.
CHANDASI_NIPATANA: Tuple[str, ...] = (
    "अपस्पृधेथाम्", "आनृचुः", "आनृहुः", "चिच्युषे", "तित्याज",
    "श्राताः", "श्रितम्", "आशीः", "आशीर्तः",
)


@dataclass(frozen=True)
class Samprasarana:
    """One rule of 6.1.13–44: a base, an affix, and what is ordered."""

    sutra: str
    #: The roots or bases the rule names.
    of: Tuple[str, ...] = ()
    #: A named group instead of a list — यजादि at 6.1.15.
    gana: str = ""
    #: The affix or its marker that must follow: kit, ṅit, liṭ, yaṅ,
    #: caṅ, niṣṭhā, lyap, or ṇau-saṃ-caṅoḥ.
    before: str = ""
    #: A second affix the same row reaches, where the rule names two —
    #: 6.1.16's च pulls किति down beside ङिति, and 6.1.29 names both
    #: लिट् and यङ्.
    also_before: str = ""
    #: What must stand in front of the root — प्र at 6.1.23, प्रति at
    #: 6.1.25, परि at 6.1.44. A tuple because 6.1.26 names two,
    #: अभि and अव, and the rule is one rule.
    pre: Tuple[str, ...] = ()
    #: The sense the derived word must carry — द्रवमूर्ति and स्पर्श
    #: at 6.1.24, पाक at 6.1.27. Two at 6.1.24 for the same reason.
    result: Tuple[str, ...] = ()
    #: The word that must FOLLOW in the compound — पुत्र and पति at
    #: 6.1.13, बन्धु at 6.1.14. Nothing else in the section is
    #: conditioned on a compound at all.
    uttarapada: Tuple[str, ...] = ()
    #: And which compound it must be.
    samasa: str = ""
    #: What the vocalisation lands on: the धातु, or the अभ्यास alone
    #: (6.1.17), or the अभ्यस्त, which is both (6.1.33).
    on: str = "dhātu"
    #: A finished substitute the rule puts in instead of ordering a
    #: vocalisation — की, स्फी, पी, शृ, व.
    adesa: str = ""
    #: True where the rule REFUSES what an earlier one gave.
    refuses: bool = False
    optional: bool = False
    #: True where the option is व्यवस्थितविभाषा — settled by what the
    #: word is used of, not free. 6.1.26, 6.1.27 and 6.1.28.
    vyavasthita: bool = False
    #: True where the rule says बहुलम् — 6.1.34 and 6.1.35.
    bahulam: bool = False
    #: True where the rule holds in the छन्दस् only.
    chandasi: bool = False
    #: True where the forms are laid down whole — 6.1.36.
    nipatana: bool = False
    #: True where what the rule turns on is that a vocalisation has
    #: ALREADY happened further along in the word — 6.1.37 alone.
    #: It names no root and no affix, so without this it would
    #: match every question asked.
    after_samprasarana: bool = False
    #: The rule this one refuses or narrows, by its own number.
    blocks: Tuple[str, ...] = ()
    #: What the rule keeps out, in one phrase.
    keeps_out: str = ""
    why: str = ""


SAMPRASARANA_TABLE: Tuple[Samprasarana, ...] = (
    Samprasarana(
        "6.1.13", of=("ṣyaṅ",), uttarapada=("putra", "pati"),
        samasa="tatpuruṣa",
        keeps_out="इभ्यापुत्रः, क्षत्रियापुत्रः — no ष्यङ् in either",
        why="ष्यङः संप्रसारणं पुत्रपत्योस्तत्पुरुषे — and the "
            "section opens on a base that is not a root at all. "
            "ष्यङ् is 4.1.78's feminine affix, and its य् vocalises "
            "when पुत्र or पति follows in a तत्पुरुष: "
            "**कारीषगन्धीपुत्रः, कारीषगन्धीपतिः**.\\n\\n"
            "**AND THE HEADING IS DECLARED HERE.** "
            "**संप्रसारणमिति चाधिक्रियते विभाषा परेः इति यावत्** — "
            "the word governs to 6.1.44 and no further. Thirty-two "
            "sūtras, and this is the first.\\n\\n"
            "**AND THE RULE NAMES ONE SEMIVOWEL AMONG SEVERAL.** "
            "कारीषगन्ध्या has more than one यण् in it, and only the "
            "ष्यङ् vocalises: **ष्यङन्ते च यद्यप्यन्ये यणः सन्ति, "
            "तथापि ष्यङ एव संप्रसारणम् — निर्दिश्यमानस्यादेशा "
            "भवन्ति**. What a rule POINTS AT is what a substitute "
            "replaces.\\n\\n"
            "**AND A FEMININE AFFIX IS READ BY ITS OWN PARIBHĀṢĀ.** "
            "The ordinary maxim would make ष्यङ् mean the whole word "
            "beginning with what it was added to; but **न "
            "स्त्रीप्रत्यये चानुपसर्जने** holds instead, so a "
            "feminine affix means only what ENDS in it. Hence "
            "**परमकारीषगन्धीपुत्रः** does vocalise — and "
            "**अतिकारीषगन्ध्यापुत्रः** does not, the base there "
            "being उपसर्जन.\\n\\n"
            "**AND THE FOLLOWING WORD MUST BE THAT WORD ALONE.** "
            "**पुत्रपत्योः केवलयोरुत्तरपदयोरिदं संप्रसारणम्, "
            "तदादौ तदन्ते च न भवति** — कारीषगन्ध्यापुत्रकुलम् and "
            "कारीषगन्ध्यापरमपुत्रः both stay unvocalised. And "
            "तत्पुरुषे matters: कारीषगन्ध्यापतिरयं ग्रामः is a "
            "बहुव्रीहि and keeps its य्"),
    Samprasarana(
        "6.1.14", of=("ṣyaṅ",), uttarapada=("bandhu",),
        samasa="bahuvrīhi",
        keeps_out="कारीषगन्ध्याबन्धुः, the तत्पुरुष",
        why="बन्धुनि बहुव्रीहौ — the same vocalisation before बन्धु, "
            "and now the compound must be a बहुव्रीहि: "
            "**कारीषगन्ध्या बन्धुरस्य कारीषगन्धीबन्धुः**. Where it "
            "is a तत्पुरुष — कारीषगन्ध्याया बन्धुः — the य् "
            "stands.\\n\\n"
            "**A GENDER IN THE RULE IS THE WORD-FORM'S, NOT THE "
            "WORD'S.** बन्धुनि is neuter and बन्धु is masculine. "
            "**बन्धुनीति नपुंसकलिङ्गनिर्देशः शब्दरूपापेक्षया, "
            "पुँल्लिङ्गाभिधेयस्त्वयं बन्धुशब्दः** — the sūtra is "
            "naming a shape, and a shape has no gender of its "
            "own.\\n\\n"
            "**AND A SUPPLEMENT ADDS THREE MORE, OPTIONALLY.** "
            "**मातच्मातृकमातृषु वा** — कारीषगन्धीमातः beside "
            "कारीषगन्ध्यामातः. Two things fall out of it: the चित् "
            "of मातच् puts the accent at the end and so overrides "
            "6.2.1's बहुव्रीहि accent, and मातृ and मातृक being "
            "listed SEPARATELY shows that 5.4.153's कप् is itself "
            "optional here"),
    Samprasarana(
        "6.1.15", of=("vac", "svap"), gana="yajādi", before="kit",
        keeps_out="वाच्यति, वाचिकः — the affix is not one a धातु "
                  "takes",
        why="वचिस्वपियजादीनां किति — and the ष्यङ् of the two rules "
            "before drops away. Eleven roots: वच्, स्वप्, and the "
            "यजादि that close the भ्वादि gaṇa — "
            "**यजादयो यज देवपूजासंगतिकरणदानेषु इत्यतः प्रभृति "
            "आगणान्ताः**. Before a कित् affix each vocalises: "
            "**उक्तः, सुप्तः, इष्टः, उप्तः, ऊढः, उषितः, उतः, "
            "संवीतः, आहूतः, उदितः, शूनः**.\\n\\n"
            "**AND NAMING A ROOT IS NOT NAMING ITS SHAPE.** "
            "**धातोः स्वरूपग्रहणे तत्प्रत्यये कार्यं विज्ञायते** — "
            "where a rule names a particular root rather than "
            "saying धातोः, the operation holds only before an affix "
            "that comes AFTER A ROOT. So वाच्यति and वाचिकः do not "
            "vocalise: क्यच् is given after a सुबन्त and ठक् after a "
            "प्रातिपदिक, whatever वाच् may be in itself"),
    Samprasarana(
        "6.1.16", gana="grahyādi", before="ṅit", also_before="kit",
        why="ग्रहिज्यावयिव्यधिवष्टिविचतिवृश्चतिपृच्छतिभृज्जतीनां "
            "ङिति च — nine more roots, and the च carries किति down "
            "from the rule before, so these vocalise before EITHER "
            "marker. **गृहीतः, गृह्णाति; जीनः, जिनाति; विद्धः, "
            "विध्यति; उशितः, उष्टः; विचितः, विचति; वृक्णः, वृश्चति; "
            "पृष्टः, पृच्छति; भृष्टः, भृज्जति**.\\n\\n"
            "**AND ONE OF THE NINE IS ITSELF A SUBSTITUTE.** वयि is "
            "what 2.4.41 puts in for वेञ् before लिट्, and वेञ् is "
            "already in 6.1.15's list — so why name it? "
            "**लिटि तस्य वेञः इति प्रतिषेधो वक्ष्यते** — 6.1.40 will "
            "REFUSE वेञ् in the perfect, and by स्थानिवद्भाव the "
            "refusal would reach वयि too. Naming वयि here fixes it "
            "on the giving side and off the refusing side: "
            "**वयेर्विधौ ग्रहणं प्रतिषेधे चाग्रहणम्**.\\n\\n"
            "**AND A ROOT'S GAṆA CAN WIDEN THE AFFIXES THAT COUNT.** "
            "व्यच is कुटादि by a vārttika on 1.2.1, so every affix "
            "after it but a णित् or ञित् is treated as ङित् — "
            "**उद्विचिता, उद्विचितुम्, उद्विचितव्यम्**"),
    Samprasarana(
        "6.1.17", gana="ubhaya", before="liṭ", on="abhyāsa",
        why="लिट्यभ्यासस्योभयेषाम् — and now the vocalisation lands "
            "not on the root but on the COPY. Both lists, 6.1.15's "
            "and 6.1.16's, before लिट्: **उवाच, सुष्वाप, इयाज, "
            "उवाप; जग्राह, जिज्यौ, उवाय, विव्याध, उवाश, विव्याच, "
            "वव्रश्च**.\\n\\n"
            "**AND THE RULE IS FOR THE NON-कित् HALF OF लिट्.** "
            "**अकिदर्थं चेदमभ्यासस्य संप्रसारणं विधीयते** — where "
            "the perfect ending IS कित्, 6.1.15 has already "
            "vocalised the root, and the copy is taken from what is "
            "already vocalised: ऊचतुः, ऊचुः. The order is settled by "
            "**पुनःप्रसङ्गविज्ञानात्** — vocalise, then "
            "double.\\n\\n"
            "**AND उभयेषाम् IS SAID ONLY TO BEAT 7.4.60.** The "
            "अनुवृत्ति already carried both lists, so the word is "
            "idle as a list: **अधिकारादेवोभयेषां ग्रहणे सिद्धे "
            "पुनरुभयेषामिति वचनं हलादिशेषम् अपि बाधित्वा "
            "संप्रसारणमेव यथा स्यात्**. In व्यध् + णल् the copy is "
            "व्य, and हलादिः शेषः would strike the य् out before "
            "anything could vocalise it. The idle word says: "
            "vocalise anyway"),
    Samprasarana(
        "6.1.18", of=("svāpi",), before="caṅ",
        keeps_out="स्वाप्यते, स्वापितः",
        why="स्वापेश्चङि — and the root named is the CAUSATIVE, "
            "**स्वापेरिति स्वपेर्ण्यन्तस्य ग्रहणम्**. Before चङ्: "
            "**असूषुपत्, असूषुपताम्, असूषुपन्**.\\n\\n"
            "**AND THE FIVE STEPS ARE IN ONE ORDER ONLY.** "
            "**द्विर्वचनात् पूर्वमत्र संप्रसारणम्** — vocalise "
            "first, then guṇa the light penult, then 7.4.1 shortens "
            "it before चङ्, then the doubling, then 7.4.94 lengthens "
            "the copy. Take them in any other order and the form is "
            "not reached.\\n\\n"
            "**AND THE VṚTTI ADMITS IT CANNOT TELL WHAT CARRIES.** "
            "**कितीति निवृत्तम्, ङितीति केवलमिहानुवर्तत इत्येतद् "
            "दुर्विज्ञानम्** — किति has lapsed; whether ङिति alone "
            "still runs is *hard to know*. A commentary saying so in "
            "as many words is worth keeping"),
    Samprasarana(
        "6.1.19", of=("svap", "syam", "vyeñ"), before="yaṅ",
        keeps_out="स्वप्नक्, formed with नजिङ्",
        why="स्वपिस्यमिव्येञां यङि — three roots before यङ्: "
            "**सोषुप्यते, सेसिम्यते, वेवीयते**. स्वप् and व्येञ् are "
            "already in 6.1.15's list, but that rule wants a कित् "
            "affix and यङ् is not one"),
    Samprasarana(
        "6.1.20", of=("vaś",), before="yaṅ", refuses=True,
        blocks=("6.1.16",),
        keeps_out="उष्टः, उशन्ति — those are not before यङ्",
        why="न वशः — the first refusal of the section. वश् is one of "
            "6.1.16's nine and would vocalise before the ङित् यङ्; "
            "here it does not: **वावश्यते, वावश्येते, "
            "वावश्यन्ते**.\\n\\n"
            "**AND THE PROHIBITION DOES NOT GOVERN WHAT IT "
            "EXCEPTS.** Outside यङ् the giving rule stands "
            "untouched — उष्टः and उशन्ति are 6.1.16's, and this "
            "rule has nothing to say about them"),
    Samprasarana(
        "6.1.21", of=("cāy",), before="yaṅ", adesa="kī",
        why="चायः की — and the rule substitutes a finished form "
            "instead of ordering a vocalisation. Before यङ्: "
            "**चेकीयते, चेकीयेते, चेकीयन्ते**.\\n\\n"
            "**AND THE LONG ई IN THE SŪTRA IS FOR A CASE THE SŪTRA "
            "DOES NOT MENTION.** **दीर्घोच्चारणं यङ्लुगर्थम्** — "
            "with यङ् present, 7.4.25 would lengthen a short इ "
            "anyway and कि would have served; but where the यङ् is "
            "dropped there is nothing to lengthen, and the निष्ठा "
            "would come out **चेकितः** instead of **चेकीतः**. The "
            "vowel is written long for the form the rule is silent "
            "about"),
    Samprasarana(
        "6.1.22", of=("sphāy",), before="niṣṭhā", adesa="sphī",
        keeps_out="स्फातिः, which is क्तिन् and not निष्ठा",
        why="स्फायः स्फी निष्ठायाम् — **स्फीतः, स्फीतवान्**.\\n\\n"
            "**AND निष्ठायाम् IS ITSELF A HEADING.** "
            "**निष्ठायामित्येतदधिक्रियते लिड्यङोश्च इति "
            "प्रागेतस्मात् सूत्रात्** — the word governs the seven "
            "rules from here to 6.1.28, and stops where 6.1.29 names "
            "two other affixes. A heading inside a heading, and both "
            "of them declared by the vṛtti rather than by a "
            "word.\\n\\n"
            "**AND स्फाती भवति IS NOT A COUNTER-EXAMPLE.** "
            "**स्फातीभवतीत्येतदपि क्तिन्नन्तस्यैव रूपम्, न "
            "निष्ठान्तस्य** — the ई there is the feminine of the "
            "क्तिन् form, not a निष्ठा at all"),
    Samprasarana(
        "6.1.23", of=("styā",), before="niṣṭhā", pre=("pra",),
        keeps_out="संस्त्यानः, संस्त्यानवान्",
        why="स्त्यः प्रपूर्वस्य — **प्रस्तीतः, प्रस्तीतवान्**, and "
            "both स्त्यै and ष्ट्यै are meant, the two having the "
            "same shape स्त्या.\\n\\n"
            "**AND THE VOCALISATION UNDOES A LATER RULE'S "
            "CONDITION.** 8.2.43 turns the त of निष्ठा into न after "
            "a root that has a यण् and ends in आ. Vocalise the य् "
            "and the root no longer has one: **संप्रसारणे कृते "
            "यण्वत्त्वं विहतमिति निष्ठानत्वं न भवति**. What is left "
            "is 8.2.54's optional म — प्रस्तीमः.\\n\\n"
            "**AND पूर्वस्य IS SAID SO THAT प्र NEED NOT BE "
            "ADJACENT.** प्रस्त्यः would have done for प्र alone. "
            "The compound is read as a बहुव्रीहि — **प्रः पूर्वो "
            "यस्य धातूपसर्गसमुदायस्य स प्रपूर्वः** — that whole of "
            "root-and-preverbs which has प्र first. So "
            "**प्रसंस्तीतः** is reached with सम् standing "
            "between"),
    Samprasarana(
        "6.1.24", of=("śyā",), before="niṣṭhā",
        result=("dravamūrti", "sparśa"),
        keeps_out="संश्यानो वृश्चिकः — a scorpion curled up is "
                  "neither",
        why="द्रवमूर्तिस्पर्शयोः श्यः — and a SENSE decides it. "
            "द्रवमूर्ति is a liquid gone stiff: **शीनं घृतम्, शीना "
            "वसा, शीनं मेदः** — **द्रवावस्थायाः काठिन्यं "
            "गतम्**.\\n\\n"
            "**AND THE TWO SENSES PART COMPANY LATER IN THE BOOK.** "
            "8.2.47 श्योऽस्पर्शे turns the त into न where the sense "
            "is NOT touch, which is why the congealed thing is शीनम् "
            "and the cold thing is शीतम् — **शीतो वायुः, "
            "शीतमुदकम्** — from the very same vocalisation. One rule "
            "here, two forms there"),
    Samprasarana(
        "6.1.25", of=("śyā",), before="niṣṭhā", pre=("prati",),
        why="प्रतेश्च — the same root after प्रति, and now no sense "
            "is required: **प्रतिशीनः, प्रतिशीनवान्**. The vṛtti "
            "says why the rule exists at all — "
            "**द्रवमूर्तिस्पर्शाभ्यामन्यत्रापि यथा स्यादिति "
            "सूत्रारम्भः**: to reach the cases the rule before "
            "cannot"),
    Samprasarana(
        "6.1.26", of=("śyā",), before="niṣṭhā", pre=("abhi", "ava"),
        optional=True, vyavasthita=True,
        why="विभाषाभ्यवपूर्वस्य — after अभि or अव the vocalisation "
            "is a choice: **अभिशीनम्, अभिश्यानम्; अवशीनम्, "
            "अवश्यानम्**.\\n\\n"
            "**AND THE CHOICE REACHES THE SENSES 6.1.24 MADE "
            "FIXED.** **द्रवमूर्तिस्पर्शविवक्षायामपि विकल्पो भवति** — "
            "अभिशीनं घृतम् beside अभिश्यानं घृतम्. **सेयम् "
            "उभयत्रविभाषा द्रष्टव्या**: an option that both supplies "
            "where nothing did and loosens what was "
            "obligatory.\\n\\n"
            "**AND THE VṚTTI REFUSES TO SETTLE ONE QUESTION.** Some "
            "read पूर्व as keeping समभिश्यान and समवश्यान out. The "
            "Kāśikā answers **तस्मादत्र भवितव्यमेव** — the option "
            "ought to hold there too; and if it is not wanted, "
            "**यत्नान्तरमास्थेयम्**, some other device must be "
            "found, and another use for पूर्व stated. A commentary "
            "declining to paper over a gap"),
    Samprasarana(
        "6.1.27", of=("śrā",), before="kta", result=("pāka",),
        adesa="śṛ", optional=True, vyavasthita=True, nipatana=True,
        keeps_out="श्राणा यवागूः, श्रपिता यवागूः",
        why="शृतं पाके — the whole form is laid down: **शृतं क्षीरम्, "
            "शृतं हविः**, and the root may be causative or not.\\n\\n"
            "**AND THE OPTION IS SETTLED BY WHAT THE WORD IS USED "
            "OF.** **व्यवस्थितविभाषा चेयम्, तेन क्षीरहविषोर्नित्यं "
            "शृभावो भवति, अन्यत्र न भवति** — always for milk and "
            "oblation, never elsewhere. And पाके is in the rule to "
            "SHOW that field: **पाकग्रहणं "
            "निपातनविषयप्रदर्शनार्थम्**.\\n\\n"
            "**AND A SECOND CAUSATIVE IS SHUT OUT.** **श्रपितं "
            "क्षीरं देवदत्तेन यज्ञदत्तेन** is not wanted — where one "
            "man has another cook the milk the form stays श्रपित. "
            "But श्रा being intransitive, both the reflexive and the "
            "plain agent give शृतम्: **शृतं क्षीरं स्वयमेव, शृतं "
            "क्षीरं देवदत्तेन**"),
    Samprasarana(
        "6.1.28", of=("pyāy",), before="niṣṭhā", adesa="pī",
        optional=True, vyavasthita=True,
        why="प्यायः पी — **पीनं मुखम्, पीनौ बाहू, पीनमुरः**.\\n\\n"
            "**AND THIS OPTION TOO IS SETTLED, AND SETTLED THE OTHER "
            "WAY ROUND.** **इयमपि व्यवस्थितविभाषैव। तेनानुपसर्गस्य "
            "नित्यं भवति, सोपसर्गस्य तु नैव भवति** — always without "
            "a preverb, never with one: आप्यानश्चन्द्रमाः. Where "
            "6.1.27 fixed the option by the OBJECT spoken of, this "
            "one fixes it by whether a preverb stands there.\\n\\n"
            "**AND ONE PREVERB IS PULLED BACK IN.** "
            "**आङ्पूर्वस्यान्धूधसोर्भवत्येव** — with आङ् before it "
            "and अन्धु or ऊधस् in the compound, the substitute "
            "returns: **आपीनोऽन्धुः, आपीनमूधः**"),
    Samprasarana(
        "6.1.29", of=("pyāy",), before="liṭ", also_before="yaṅ",
        adesa="pī",
        why="लिड्यङोश्च — the same substitute before लिट् and यङ्, "
            "and **विभाषेति निवृत्तम्**: the option of the rule "
            "before has lapsed, so here it is fixed. **आपिप्ये, "
            "आपिप्याते, आपिप्यिरे; आपेपीयते, आपेपीयेते, "
            "आपेपीयन्ते**.\\n\\n"
            "**AND THE SUBSTITUTE COMES BEFORE THE DOUBLING THAT "
            "PRECEDES IT.** पी is ordered by a later rule than "
            "6.1.8's doubling and so wins on परत्व; and then the "
            "doubling happens anyway, by **पुनःप्रसङ्गविज्ञानात्** — "
            "a rule that has been set aside once is allowed to apply "
            "again. पी → पिपी → पिप्ये by 6.4.82. The same maxim "
            "6.1.17 used, in the opposite direction"),
    Samprasarana(
        "6.1.30", of=("śvi",), before="liṭ", also_before="yaṅ",
        optional=True,
        why="विभाषा श्वेः — **शुशाव, शिश्वाय; शुशुवतुः, शिश्वियतुः; "
            "शोशूयते, शेश्वीयते**.\\n\\n"
            "**AND THE ONE OPTION DOES TWO DIFFERENT THINGS.** "
            "**यङि संप्रसारणमप्राप्तं विभाषा विधीयते, लिटि तु किति "
            "यजादित्वाद् नित्यं प्राप्तम्** — before यङ् nothing "
            "reached श्वि at all, so the option SUPPLIES; before "
            "लिट् 6.1.15 already reached it as a यजादि root, so the "
            "option LOOSENS. **तत्र सर्वत्र विकल्पो भवतीत्येष "
            "उभयत्रविभाषा**.\\n\\n"
            "**AND REFUSING THE ROOT REFUSES THE COPY WITH IT.** "
            "**यदा च धातोर्न भवति, तदा लिट्यभ्यासस्योभयेषाम् "
            "इत्यभ्यासस्यापि न भवति** — this is what makes शिश्वाय "
            "possible. Take the option away and 6.1.17 would "
            "vocalise the copy and give शुश्वाय, which is not a "
            "form"),
    Samprasarana(
        "6.1.31", of=("śvi",), before="ṇau-saṃ-caṅoḥ", optional=True,
        why="णौ च संश्चङोः — before णि with सन् or चङ् after it, the "
            "same choice: **शुशावयिषति, शिश्वाययिषति; अशूशवत्, "
            "अशिश्वयत्**.\\n\\n"
            "**AND THIS IS WHERE THE MAXIM IS CITED.** "
            "**संप्रसारणं संप्रसारणाश्रयं च बलीयो भवति** — "
            "vocalisation and whatever rests on it are stronger. "
            "Vṛddhi here is अन्तरङ्ग and would ordinarily go first; "
            "**अन्तरङ्गमपि वृद्ध्यादिकं संप्रसारणेन बाध्यते**, and "
            "the vṛddhi and the आव् come afterwards.\\n\\n"
            "**AND ONE RULE ELSEWHERE IS READ AS A ज्ञापक.** "
            "7.4.80's ओः पुयण्ज्यपरे presupposes a उ to work on in "
            "the copy — **एतद् वचनं ज्ञापकं णौ कृतस्थानिवद्भावस्य** "
            "— so what णि caused counts as what it replaced, and it "
            "is शु that doubles"),
    Samprasarana(
        "6.1.32", of=("hve",), before="ṇau-saṃ-caṅoḥ",
        why="ह्वः संप्रसारणम् — **जुहावयिषति, अजूहवत्**, and this "
            "one is NOT a choice.\\n\\n"
            "**AND THE IDLE WORD IS WHAT DROPS THE OPTION.** "
            "संप्रसारणम् was already carrying by अनुवृत्ति. "
            "**संप्रसारणमिति वर्तमाने पुनः संप्रसारणमित्युक्तं "
            "विभाषेत्यस्य निवृत्त्यर्थम्** — saying it again is how "
            "the rule sheds the विभाषा it would otherwise have "
            "inherited from 6.1.31. A word that adds nothing to the "
            "sense, and everything to the force.\\n\\n"
            "**AND THE MAXIM KEEPS AN AUGMENT OUT.** 7.3.37 would "
            "give ह्वा the augment युक् before णि; "
            "**संप्रसारणस्य बलीयस्त्वात् प्रागेव युग् न भवति** — "
            "vocalise first and there is no आ left for the augment "
            "to attach to.\\n\\n"
            "**AND SPLITTING THIS FROM THE NEXT RULE IS ITSELF A "
            "SIGNAL.** The two could have been one. "
            "**पृथग्योगकरणम् अनभ्यस्तनिमित्तप्रत्ययव्यवधाने "
            "संप्रसारणाभावज्ञापनार्थम्** — where an affix that "
            "causes no doubling stands between, there is no "
            "vocalisation: ह्वायकीयति, and its desiderative "
            "जिह्वायकीयिषति"),
    Samprasarana(
        "6.1.33", of=("hve",), on="abhyasta",
        why="अभ्यस्तस्य च — and the genitive does not agree with "
            "ह्वः. **अभ्यस्तस्य यो ह्वयतिः। कश्चाभ्यस्तस्य "
            "ह्वयतिः? कारणम्** — the ह्वयति that BRINGS ABOUT an "
            "अभ्यस्त, not one that is already inside it. So the "
            "vocalisation happens BEFORE the doubling: **जुहाव, "
            "जोहूयते, जुहूषति**.\\n\\n"
            "**AND 6.1.5's NAME IS WHAT THE RULE LEANS ON.** "
            "अभ्यस्त is both copies together, so vocalising the "
            "root before the split gives both — and no separate rule "
            "for the copy is needed here as 6.1.17 was needed "
            "there"),
    Samprasarana(
        "6.1.34", of=("hve",), chandasi=True, bahulam=True,
        keeps_out="ह्वयामि मरुतः शिवान् — the same root, "
                  "unvocalised, in the same corpus",
        why="बहुलं छन्दसि — in the Vedic corpus the same root "
            "vocalises variously: **इन्द्राग्नी हुवे, देवीं "
            "सरस्वतीं हुवे**, but also **ह्वयामि विश्वान् "
            "देवान्**.\\n\\n"
            "**AND बहुलम् IS NOT विभाषा.** An option gives two forms "
            "for one condition; बहुलम् says the rule is found "
            "sometimes present, sometimes absent, and the corpus is "
            "the only evidence for which. Here हुवे needs 2.4.73's "
            "own बहुलं छन्दसि to drop the शप् first, and then the "
            "vocalisation and उवङ्"),
    Samprasarana(
        "6.1.35", of=("cāy",), adesa="kī", chandasi=True,
        bahulam=True,
        keeps_out="अग्निर्ज्योतिर्निचाय्य",
        why="चायः की — the substitute of 6.1.21 again, now in the "
            "छन्दस् and without the यङ् that rule required: "
            "**न्यन्यं चिक्युर्न नि चिक्युरन्यम्**, forms in the "
            "उस् of लिट्. And sometimes not at all — "
            "**अग्निर्ज्योतिर्निचाय्य**"),
    Samprasarana(
        "6.1.36", of=("spardh", "arc", "arh", "cyu", "tyaj", "śrī"),
        chandasi=True, nipatana=True,
        why="अपस्पृधेथामानृचुरानृहुश्चिच्युषेतित्याजश्राताः "
            "श्रितमाशीराशीर्ताः — nine forms laid down whole, each "
            "with its irregularity named.\\n\\n"
            "**अपस्पृधेथाम्**: from स्पर्ध in लङ्, the र् vocalised "
            "and the अ dropped — **इन्द्रश्च विष्णो यदपस्पृधेथाम्**. "
            "In ordinary speech अस्पर्धेथाम्. A second reading takes "
            "अप as the preverb and the missing अट् as 6.4.75's, and "
            "then the counter-example is अपास्पर्धेथाम्.\\n\\n"
            "**आनृचुः, आनृहुः**: from अर्च् and अर्ह् in लिट्, and "
            "the derivation runs through four other rules — 7.4.66 "
            "for the अ, 7.4.70 for its lengthening, 7.4.71 for the "
            "नुट्.\\n\\n"
            "**चिच्युषे**: the COPY vocalised, and no इट्. "
            "Ordinarily चुच्युविषे. **तित्याज**: the copy again, for "
            "तत्याज.\\n\\n"
            "**श्राताः, श्रितम्, आशीः, आशीर्तः**: all from श्रीञ्. "
            "The vṛtti reports a division of territory — **सोमेषु "
            "बहुषु श्राभाव एव, अन्यत्र श्रिभावः** — and then "
            "immediately reports a verse against it, **यदि श्रातो "
            "जुहोतन**, with श्रात in the singular and no soma. Its "
            "answer is that the plural श्राताः in the sūtra is not "
            "meant strictly: **बहुवचनस्याविवक्षितत्वाद् उपसंग्रहो "
            "द्रष्टव्यः**"),
    Samprasarana(
        "6.1.37", refuses=True, after_samprasarana=True,
        keeps_out="विद्धः, विचितः, संवीतः — one vocalisation each, "
                  "never two",
        why="न संप्रसारणे संप्रसारणम् — where one semivowel has been "
            "vocalised, the one before it is not. व्यध् has both व् "
            "and य्, and only the य् goes.\\n\\n"
            "**AND THE RULE IS THE PROOF OF ITS OWN ORDER.** No "
            "giving rule says WHICH semivowel of a cluster "
            "vocalises. **एकयोगलक्षणमपि संप्रसारणमत एव वचनात् "
            "प्रथमं परस्य यणः क्रियते, पूर्वस्य च प्रसक्तं "
            "प्रतिषिध्यते** — this very prohibition settles it, "
            "because if the FIRST were the one vocalised there would "
            "never be a semivowel standing before a vocalised one, "
            "and the rule would forbid nothing.\\n\\n"
            "**AND THE WORD IS REPEATED TO REACH ACROSS A GAP.** "
            "**पुनः संप्रसारणग्रहणं विदेशस्थस्यापि संप्रसारणस्य "
            "प्रतिषेधो यथा स्यात्** — the two need not be adjacent. "
            "6.4.133 vocalises the व् of युवन् and the य् stays: "
            "यूनः, यूना. And the long ऊ that swallowed the two "
            "उ-sounds is no help to the objector — a single "
            "substitute for two vowels is not स्थानिवत् by 1.1.58, "
            "and even if it were, **व्यवधानम् एतावद् "
            "आश्रयिष्यते**, it is still something standing "
            "between.\\n\\n"
            "**AND TWO SUPPLEMENTS ADD WHAT THE RULE DOES NOT.** "
            "**ऋचि त्रेरुत्तरपदादिलोपश्छन्दसि** — तिस्र ऋचो यस्मिन् "
            "is तृचं सूक्तम्, with the ऋ of ऋच् gone too, and only "
            "of a metre: त्र्यृचं कर्म otherwise. And "
            "**रयेर्मतौ बहुलम्** — आ रेवानेतु नो विशः beside "
            "रयिमान् पुष्टिवर्धनः"),
    Samprasarana(
        "6.1.38", of=("vayi",), before="liṭ", refuses=True,
        blocks=("6.1.16",),
        why="लिटि व्यो यः — of the substitute वय्, the य् does not "
            "vocalise in the perfect: **उवाय, ऊयतुः, ऊयुः**. The व् "
            "does, by 6.1.16, and that is what makes ऊयतुः.\\n\\n"
            "**AND लिटि IS SAID FOR THE RULES AFTER IT.** "
            "**लिड्ग्रहणमुत्तरार्थम्** — वय् takes no other affix, "
            "so the word is idle here; it is put in so that 6.1.39 "
            "and 6.1.40 can carry it"),
    Samprasarana(
        "6.1.39", of=("vayi",), before="kit-liṭ", adesa="v",
        optional=True,
        keeps_out="उवाय, उवयिथ — those endings are not कित्",
        why="वश्चास्यान्यतरस्यां किति — and the substitute is a "
            "CONSONANT, the only such row in the section: व् may "
            "stand for the य् of वय् before a कित् perfect ending. "
            "**ऊवतुः, ऊवुः** beside **ऊयतुः, ऊयुः**.\\n\\n"
            "**AND PATAÑJALI SAYS THE RULE IS UNNECESSARY.** "
            "अन्यतरस्यां किति वेञः would have done: refuse the "
            "vocalisation and वेञ् gives ववतुः, ववुः; allow it and "
            "वे → उ → उवङ् by 6.1.77 gives ऊवतुः, ऊवुः; and वय्, "
            "whose य् 6.1.38 never vocalises, gives ऊयतुः, ऊयुः. "
            "**तथा सर्वाणि त्रीणि रूपाणि वश्चास्येत्यनुक्त्वैव "
            "सिद्धानि** — all three forms, without this rule"),
    Samprasarana(
        "6.1.40", of=("veñ",), before="liṭ", refuses=True,
        blocks=("6.1.15", "6.1.17"),
        why="वेञः — in the perfect वेञ् does not vocalise, and "
            "neither does its copy: **ववौ, ववतुः, ववुः**.\\n\\n"
            "**AND THE REFUSAL HAS TO REACH TWO RULES.** "
            "**किति यजादित्वाद् धातोः प्राप्तम्, अकित्यपि "
            "लिट्यभ्यासस्योभयेषाम् इत्यभ्यासस्य, अत उभयं "
            "प्रतिषिध्यते** — 6.1.15 would take the root before a "
            "कित् ending and 6.1.17 the copy before the rest, so the "
            "one refusal has to cover both. And this is the "
            "prohibition 6.1.16 was careful to keep वयि out of"),
    Samprasarana(
        "6.1.41", of=("veñ",), before="lyap", refuses=True,
        blocks=("6.1.15",),
        why="ल्यपि च — and before ल्यप् too: **प्रवाय, उपवाय**. "
            "**पृथग्योगकरणमुत्तरार्थम्** — the rule is split off "
            "from 6.1.40 so that only ल्यप्, and not लिट्, carries "
            "into the three that follow"),
    Samprasarana(
        "6.1.42", of=("jyā",), before="lyap", refuses=True,
        blocks=("6.1.16",),
        why="ज्यश्च — **प्रज्याय, उपज्याय**. ज्या is one of 6.1.16's "
            "nine and ल्यप् is कित् by 1.1.5's reading of it, so the "
            "vocalisation would otherwise hold"),
    Samprasarana(
        "6.1.43", of=("vyeñ",), before="lyap", refuses=True,
        blocks=("6.1.15",),
        why="व्यश्च — **प्रव्याय, उपव्याय**, and again "
            "**योगविभाग उत्तरार्थः**: the rule is kept separate so "
            "that व्येञ् alone carries into 6.1.44"),
    Samprasarana(
        "6.1.44", of=("vyeñ",), before="lyap", pre=("pari",),
        refuses=True, optional=True, blocks=("6.1.43",),
        why="विभाषा परेः — after परि the refusal is a choice, so the "
            "vocalisation comes back in one of the two forms: "
            "**परिवीय यूपम्, परिव्याय**. The last rule the heading "
            "reaches.\\n\\n"
            "**AND THE VOCALISED FORM SETS OFF A CONTEST TWO PĀDAS "
            "AWAY.** With परि · वी, 6.1.71 would give the तुक् "
            "augment after a short vowel; **स हलः इति दीर्घत्वेन "
            "परत्वाद् बाध्यते** — 6.4.2 lengthens instead, and wins "
            "on परत्व. परिवीय, not *परिवित्य"),
)


@dataclass(frozen=True)
class Vocalised:
    """What the resolver answers with."""

    does: str
    sutra: str
    why: str
    #: The finished substitute where the rule gives one instead.
    adesa: str = ""
    #: धातु, अभ्यास or अभ्यस्त.
    on: str = ""
    optional: bool = False
    vyavasthita: bool = False
    bahulam: bool = False
    chandasi: bool = False
    nipatana: bool = False
    #: Where a refusal answers, the rules it takes the form away
    #: from — each named with ITS own number, not this one.
    blocked_by: Tuple[str, ...] = ()


#: The gaṇa names, and the tuple each one stands for. 6.1.15 names
#: two roots AND a gaṇa, and the base-set is the union of both — so
#: membership can never be read off `row.of` alone.
BASE_SETS = {
    "yajādi": VACYADI,
    "grahyādi": GRAHYADI,
    "ubhaya": VACYADI + GRAHYADI,
}


def _names(row: Samprasarana, root: str) -> bool:
    """Whether the row's base-set holds this root, by name or by gaṇa."""
    if root in row.of:
        return True
    return root in BASE_SETS.get(row.gana, ())


def _reaches(row: Samprasarana, root: str, before: str,
             pre: str, result: str, uttarapada: str, samasa: str,
             chandasi: bool, already: bool) -> bool:
    if row.chandasi and not chandasi:
        return False
    if row.after_samprasarana and not already:
        return False
    if (row.of or row.gana) and not _names(row, root):
        return False
    allowed = tuple(one for one in (row.before, row.also_before) if one)
    if allowed and before not in allowed:
        return False
    if row.pre and pre not in row.pre:
        return False
    if row.result and result not in row.result:
        return False
    if row.uttarapada and uttarapada not in row.uttarapada:
        return False
    if row.samasa and samasa != row.samasa:
        return False
    return True


def _supplies(row: Samprasarana, wants: str) -> bool:
    """
    Filter by what is asked for. A refusal is never an answer to a
    question that asked for one — you cannot ask *which rule gives me
    संप्रसारण here* and be handed the rule that takes it away.
    """
    if not wants:
        return True
    if wants == "samprasāraṇa":
        return not row.refuses and not row.adesa
    return wants == row.adesa


def _how_specific(row: Samprasarana, root: str) -> int:
    """
    A named root beats a gaṇa, and a refusal beats what it refuses.

    The score is of HOW THIS ROW MATCHED THIS ROOT, not of what
    columns the row happens to fill. 6.1.15 names वच् and स्वप् by
    name and the rest through यजादि; श्वि is one of the rest, and
    6.1.30 names it outright, so 6.1.30 must be the narrower for श्वि
    and the wider for वच् — which a score read off `bool(row.of)`
    could never give, since the same row would carry the same eight
    points whichever root asked.

    The preverb counts high because in this section it is what
    separates three rules on one root: 6.1.24 reaches श्या by a
    SENSE, 6.1.25 by प्रति, 6.1.26 by अभि or अव, and each is
    narrower than the sense alone.

    And the corpus counts, because a छन्दसि rule adds a
    condition to one that has none: ह्वे answers 6.1.33 in ordinary
    speech and 6.1.34 in the Vedic corpus, and the two rows are
    otherwise scored alike.
    """
    return (
        9 * bool(row.refuses)
        + 8 * (root in row.of)
        + 6 * bool(row.pre)
        + 5 * bool(row.uttarapada)
        + 4 * bool(row.result)
        + 3 * bool(row.before)
        + 2 * bool(row.samasa)
        + 2 * bool(row.chandasi)
        + 1 * bool(row.gana)
    )


def vocalises(root: str = "", *, before: str = "", pre: str = "",
              result: str = "", uttarapada: str = "", samasa: str = "",
              chandasi: bool = False, already: bool = False,
              wants: str = "") -> Vocalised:
    """
    6.1.13–44 — what a semivowel does before this affix.

    The answer names the rule that acts, and where a प्रतिषेध wins it
    reports on `blocked_by` the rules the form is being taken away
    FROM, each with its own number. A refusal does not govern what it
    excepts.

    Nothing stands over the section supplying by default: 6.1.13 is a
    rule and not a heading, and a root no rule names simply keeps its
    semivowel.

    `already` is what 6.1.37 turns on — that a vocalisation has been
    made further along in the same word. It names no root and no
    affix, so it is the one row reached by a state rather than by a
    base.
    """
    matched = [
        row for row in SAMPRASARANA_TABLE
        if _reaches(row, root, before, pre, result, uttarapada,
                    samasa, chandasi, already)
        and _supplies(row, wants)
    ]
    if not matched:
        return Vocalised(
            "", "", "No rule of 6.1.13–44 is reached, so the "
                    "semivowel stands. The section has no heading "
                    "that supplies — 6.1.13 is itself a rule")
    row = max(matched, key=lambda one: _how_specific(one, root))
    does = "" if row.refuses else (row.adesa or "samprasāraṇa")
    return Vocalised(
        does, row.sutra, row.why, adesa=row.adesa,
        on=("" if row.refuses else row.on),
        optional=row.optional, vyavasthita=row.vyavasthita,
        bahulam=row.bahulam, chandasi=row.chandasi,
        nipatana=row.nipatana, blocked_by=row.blocks)


def samprasarana_run() -> Vocalised:
    """
    How far the word संप्रसारणम् governs, on the vṛtti's own
    statement at 6.1.13.

    **संप्रसारणमिति चाधिक्रियते विभाषा परेः इति यावत्.**
    """
    opens, closes = SAMPRASARANA_RUN
    return Vocalised(
        "", opens,
        "संप्रसारणम् governs from %s to %s — the vṛtti on %s names "
        "the far end by its words, विभाषा परेः, and the name itself "
        "was given long before at 1.1.45" % (opens, closes, opens))


def provisions_for(sutra_id: str) -> Tuple[Samprasarana, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in SAMPRASARANA_TABLE
                 if row.sutra == sutra_id)
