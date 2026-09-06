# -*- coding: utf-8 -*-
"""
७.२.८–३४ — where the इट् does NOT come, stated before it is given.

Twenty-seven sūtras, and every one of them refuses an augment
that has not been prescribed yet: 7.2.35 आर्धधातुकस्येड् वलादेः
is what gives the इट्, and it stands AFTER all of these. The
Aṣṭādhyāyī states the exceptions first and the rule last, and
this run is the largest place it does so.

**THE REFUSALS ARE OF TWO KINDS.** Some turn on the affix —
7.2.8's वश् class of कृत् affixes, 7.2.9's ति तु त्र त थ सि सु
सर क स, 7.2.11's कित्, 7.2.13's लिट् — and give ईश्वरः, भस्म,
तन्तिः, हस्तः, श्रितः, चकृव. Others turn on the root: 7.2.10's
अनुदात्त monosyllable, which the vṛtti sets out in two whole
verses of अनिट्कारिका, and gives दाता, नेता, कर्ता, हर्ता.

**AND FROM 7.2.14 THE WORD IS निष्ठा FOR TWENTY-ONE SŪTRAS.**
The vṛtti says how far: **निष्ठायाम् इत्यधिकार आर्धधातुकस्येड्
वलादेः इति यावत्** — to 7.2.34, and no further. Inside it the
grammar turns lexical: शूनः, लग्नः, दीप्तः, कष्टम्, दृढः,
परिवृढः, वृत्तम्, दान्तः — words laid down one at a time, each
with the SENSE that licenses it. कष् gives कष्टम् only of
hardship and thickets, and कषितं सुवर्णम् of gold.

**AND ONE OF THEM IS ITSELF A यथासंख्यम् OF EIGHT.** 7.2.18
lays down क्षुब्ध, स्वान्त, ध्वान्त, लग्न, म्लिष्ट, विरिब्ध,
फाण्ट, बाढ against मन्थ, मनस्, तमस्, सक्त, अविस्पष्ट, स्वर,
अनायास, भृश — eight forms and eight senses, matched one to one,
and every one of them has an ordinary इट् form beside it in any
other sense.

**WHAT THIS MODULE DOES NOT DO.** It says where the इट् is
refused. Where it IS given is 7.2.35's, and what the निष्ठा's
त् then becomes is 8.2's.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: This module's stretch.
ANIT_RUN: Tuple[str, str] = ("7.2.8", "7.2.34")

#: Where निष्ठायाम् starts governing, and where the vṛtti says it
#: stops — **आर्धधातुकस्येड् वलादेः इति यावत्**.
NISTHA_FROM: str = "7.2.14"
NISTHA_TO: str = "7.2.34"

#: The rule this whole run is stated before.
THE_RULE_ITSELF: str = "7.2.35"

#: 7.2.9's ten कृत् affixes, named by their first sounds.
TITUTRA: Tuple[str, ...] = (
    "ti", "tu", "tra", "ta", "tha", "si", "su", "sara", "ka", "sa")

#: 7.2.13's eight roots, अनिट् in the perfect and no others.
KRADI_EIGHT: Tuple[str, ...] = (
    "kṛ", "sṛ", "bhṛ", "vṛ", "stu", "dru", "sru", "śru")

#: 7.2.18's eight forms, matched one to one with eight senses.
NIPATANA_EIGHT: Tuple[Tuple[str, str], ...] = (
    ("kṣubdha", "mantha"), ("svānta", "manas"),
    ("dhvānta", "tamas"), ("lagna", "sakta"),
    ("mliṣṭa", "avispaṣṭa"), ("viribdha", "svara"),
    ("phāṇṭa", "anāyāsa"), ("bāḍha", "bhṛśa"))

#: 7.2.27's seven causal stems, अनिट् or not as one pleases.
DANTA_SEVEN: Tuple[str, ...] = (
    "dam", "śam", "pūrī", "das", "spaś", "chad", "jñap")

#: 7.2.28's five, likewise optional.
RUSYAMADI: Tuple[str, ...] = (
    "ruṣ", "am", "tvar", "saṃghuṣ", "āsvan")

#: 7.2.34's Vedic list, where the इट् is laid down for roots that
#: would have refused it.
CHANDASI_ISLANDS: Tuple[str, ...] = (
    "grasita", "skabhita", "stabhita", "uttabhita", "catta",
    "vikasta", "viśastṛ", "śaṃstṛ", "śāstṛ", "tarutṛ", "tarūtṛ",
    "varutṛ", "varūtṛ", "varūtrī", "ujjvaliti", "kṣariti",
    "kṣamiti", "vamiti", "amiti")


@dataclass(frozen=True)
class Anit:
    """One rule of 7.2.8–34: the इट् refused, or a form laid down."""

    sutra: str
    #: The roots or forms named outright.
    of: Tuple[str, ...] = ()
    #: The root class instead.
    gana: str = ""
    #: Where form and sense are matched one to one.
    pairs: Tuple[Tuple[str, str], ...] = ()
    #: What must follow.
    before: Tuple[str, ...] = ()
    #: The preverb the root must carry.
    upasarga: Tuple[str, ...] = ()
    #: The sense that licenses the form.
    sense: str = ""
    #: True where the rule LAYS DOWN a form rather than merely
    #: refusing the augment.
    nipatana: bool = False
    #: True where the rule GIVES the इट् — 7.2.33 and 7.2.34 do.
    supplies: bool = False
    optional: bool = False
    chandasi: bool = False
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


ANIT_TABLE: Tuple[Anit, ...] = (
    Anit(
        "7.2.8", before=("vaś-kṛt",),
        keeps_out="रुदिवः, रुदिमः — a तिङ् ending and no कृत्",
        why="नेड् वशि कृति — no इट् before a कृत् affix beginning "
            "with a वश् sound: **ईश्वरः, दीप्रः, भस्म, "
            "याच्ञा**.\\n\\n"
            "**AND THE THREE AFFIXES THE vṛtti NAMES ARE AN "
            "ILLUSTRATION AND NOT A LIST.** **वरमनादौ "
            "इत्युदाहरणप्रदर्शनार्थम्, न परिगणनम्** — so the "
            "Uṇādi **ञमन्ताड् डः** is refused too, or else "
            "**उणादयो बहुलम्** answers for it. And this is the "
            "first rule of the run: every one of the "
            "twenty-seven refuses an augment 7.2.35 has not yet "
            "given"),
    Anit(
        "7.2.9", before=TITUTRA,
        why="तितुत्रतथसिसुसरकसेषु च — nor before ति तु त्र त थ सि "
            "सु सर क स: **तन्तिः, दीप्तिः, सक्तुः, पत्त्रम्, "
            "तन्त्रम्, हस्तः, लोतः, पोतः, धूर्तः**.\\n\\n"
            "**AND ति IS TWO AFFIXES AND त IS NOT THE OBVIOUS "
            "ONE.** **तीति क्तिन्क्तिचोः सामान्यग्रहणम्** — one "
            "syllable naming both. And the त meant is the "
            "Uṇādi's तन् and not the निष्ठा's क्त: "
            "**औणादिकस्यैव तशब्दस्य ग्रहणम् इष्यते, न पुनः "
            "क्तस्य। हसितम् इत्येव हि तत्र भवति**"),
    Anit(
        "7.2.10", gana="ekāc-anudātta",
        keeps_out="आवधिष्ट — an अ-final root, and those are "
                  "उदात्त",
        why="एकाच उपदेशेऽनुदात्तात् — nor after a root that is "
            "ONE SYLLABLE and अनुदात्त as it is taught: "
            "**दाता, नेता, चेता, स्तोता, कर्ता, हर्ता**. "
            "**प्रकृत्याश्रयोऽयं प्रतिषेधः** — this refusal "
            "turns on the root and not on the affix, and it is "
            "the widest of the twenty-seven.\\n\\n"
            "**AND THE vṛtti ANSWERS *WHICH ROOTS* WITH TWO "
            "VERSES.** **के पुनर् उपदेशेऽनुदात्ताः? ये तथा गणे "
            "पठ्यन्ते** — those so read in the धातुपाठ; and "
            "then, **विस्पष्टार्थम्**, the अनिट्कारिका verses "
            "set them out: **अनिट् स्वरान्तो भवति** with the "
            "exceptions **अदन्तम् ऋदन्तम् ऋतां च वृङ्वृञौ "
            "श्विडीङिवर्णेष्वथ शीङ्श्रिञावपि**, and a second "
            "verse for the vowel-final rest before the "
            "consonant-final roots begin"),
    Anit(
        "7.2.11", of=("śri",), gana="uk-anta", before=("kit",),
        keeps_out="विदितः — neither श्रि nor उक्-final; श्रयिता, "
                  "श्रयितुम् — no कित् affix",
        why="श्र्युकः किति — nor for श्रि and an उक्-final root "
            "before a कित् affix: **श्रित्वा, श्रितः; युत्वा, "
            "युतः; लूत्वा, लूनः; वृत्वा, वृतः; तीर्त्वा, "
            "तीर्णः**.\\n\\n"
            "**AND SOME READ A ग् INTO THE DOUBLED क्.** "
            "**केचिदत्र द्विककारनिर्देशेन गकारप्रश्लेषं "
            "वर्णयन्ति, भूष्णुरित्येवं यथा स्यात्** — to catch "
            "the गित् affixes too. The vṛtti answers that "
            "3.2.139 already provides for that, **न किंचिद् "
            "एतत्**. And उपदेशे is still running, which is what "
            "gets तीर्णः: with the इ substituted first there "
            "would be no ॠ left"),
    Anit(
        "7.2.12", of=("grah", "guh"), gana="uk-anta",
        before=("san",),
        why="सनि ग्रहगुहोश्च — nor for ग्रह्, गुह् and an "
            "उक्-final root before सन्: **जिघृक्षति, "
            "जुघुक्षति; रुरूषति, लुलूषति**. And श्रि is NOT "
            "carried down from 7.2.11, since 7.2.49 makes its "
            "इट् optional. For ग्रह् the refusal is absolute; "
            "for गुह्, being ऊदित्, there is an option — "
            "**ग्रहेर् नित्यं प्राप्तः, गुहेर् ऊदित्त्वाद् "
            "विकल्पः**"),
    Anit(
        "7.2.13", of=KRADI_EIGHT, before=("liṭ",),
        keeps_out="बिभिदिव, बिभिदिम; लुलुविव, लुलविम — roots "
                  "outside the eight, which keep the इट् in the "
                  "perfect",
        why="कृसृभृवृस्तुद्रुस्रुश्रुवो लिटि — eight roots take "
            "no इट् in the perfect: **चकृव, ससृव, बभृव, ववृव, "
            "तुष्टुव, दुद्रुव, सुस्रुव, शुश्रुव**.\\n\\n"
            "**AND IT IS A नियम AND NOT A FRESH REFUSAL.** "
            "**सिद्धे सत्यारम्भो नियमार्थः। क्रादय एव लिट्य् "
            "अनिटस् ततोऽन्ये सेट इति** — these eight and no "
            "others are अनिट् in the perfect, which is what "
            "gives बिभिदिव its इट्. And the restriction cuts "
            "two ways at once: for the अनुदात्तोपदेश roots it "
            "turns on the root, for वृञ् and वृङ् on the affix, "
            "**तदुभयस्याप्ययं नियमः**. It even overrides 7.2.63, "
            "so तुष्टोथ and दुद्रोथ have no इट् either"),
    Anit(
        "7.2.14", of=("śvi",), gana="īdit", before=("niṣṭhā",),
        why="श्वीदितो निष्ठायाम् — nor for श्वि and an ईदित् root "
            "in the निष्ठा: **शूनः; लग्नः; उद्विग्नः; "
            "दीप्तः**.\\n\\n"
            "**AND THE WORD निष्ठा NOW GOVERNS FOR TWENTY-ONE "
            "SŪTRAS.** **निष्ठायाम् इत्यधिकार आर्धधातुकस्येड् "
            "वलादेः इति यावत्** — to 7.2.34, where the run "
            "ends because 7.2.35 finally gives the इट्.\\n\\n"
            "**AND डीङ् BEING READ AMONG THE ओदित् ROOTS IS A "
            "ज्ञापक.** 8.2.45 turns the निष्ठा's त् into न् "
            "after an ओदित्, and that could only bite if the "
            "त् were there without an इट् in front — "
            "**स हि नत्वार्थः, नत्वं च निष्ठातोऽनन्तरस्य "
            "विधीयते। उड्डीनः**"),
    Anit(
        "7.2.15", gana="vibhāṣā-iṭ", before=("niṣṭhā",),
        why="यस्य विभाषा — nor for any root whose इट् is made "
            "OPTIONAL somewhere else: **विधूतः** by 7.2.44's "
            "option, **गूढः** for गुह्, **वृद्धः** by 7.2.56's. "
            "An option elsewhere becomes a refusal here.\\n\\n"
            "**AND ONE WORD ESCAPES IT BY BEING LAID DOWN.** "
            "पत् has an optional इट् by a vārttika on 7.2.49, so "
            "this rule should refuse it in the निष्ठा; and "
            "2.1.24's **द्वितीया श्रितातीतपतित०** reads पतित "
            "WITH its इट्, **निपातनाद् इडागमः**"),
    Anit(
        "7.2.16", gana="ādit", before=("niṣṭhā",),
        why="आदितश्च — nor for an आदित् root: **मिन्नः, "
            "क्ष्विण्णः, स्विन्नः**, and by the च also "
            "**आश्वस्तः, वान्तः**.\\n\\n"
            "**AND THE SPLIT FROM THE NEXT SŪTRA IS A ज्ञापक.** "
            "The two could have been one — *आदितश्च विभाषा "
            "भावादिकर्मणोः* — and 7.2.15 would have covered the "
            "rest. Split, they teach a principle: "
            "**यद् उपाधेर् विभाषा तद् उपाधेः प्रतिषेध इति** — "
            "where an option is given under a condition, the "
            "refusal that follows from it holds under that same "
            "condition only. Which is how विदितः keeps its इट्, "
            "7.2.68's option being for विद् *to get*"),
    Anit(
        "7.2.17", gana="ādit", before=("niṣṭhā",),
        sense="bhāva-ādikarman", optional=True, blocks=("7.2.16",),
        why="विभाषा भावादिकर्मणोः — but in the ABSTRACT and at "
            "the START of an action the refusal is optional: "
            "**मिन्नमनेन, मेदितमनेन; प्रमिन्नः, प्रमेदितः**. "
            "The Saunāgas want शक् optional in the object sense "
            "too — **शकितो घटः कर्तुम्, शक्तो घटः कर्तुम्** — "
            "and not in the abstract, **शक्तमनेन**"),
    Anit(
        "7.2.18", pairs=NIPATANA_EIGHT,
        of=tuple(one for one, _ in NIPATANA_EIGHT),
        before=("niṣṭhā",), nipatana=True,
        keeps_out="क्षुभितमन्यत्, स्वनितो मृदङ्गः, ध्वनितं मनसा, "
                  "लगितमन्यत्, म्लेच्छितमन्यत्, विरेभितमन्यत् — "
                  "each form in any other sense keeps its इट्",
        why="क्षुब्धस्वान्तध्वान्तलग्नम्लिष्टविरिब्धफाण्टबाढानि "
            "मन्थमनस्तमःसक्ताविस्पष्टस्वरानायासभृशेषु — eight "
            "forms laid down against eight senses, ONE TO ONE: "
            "**क्षुब्धो मन्थः** but **क्षुभितं मन्थेन**; "
            "**स्वान्तम्** of the mind but **स्वनितो मृदङ्गः**; "
            "**ध्वान्तम्** of darkness; **लग्नम्** of what "
            "sticks; **म्लिष्टम्** of what is indistinct; "
            "**विरिब्धम्** of a sound. A comparison lets the "
            "sense in sideways — **क्षुब्धा गिरिनदी इत्येवमाद्य् "
            "उपमानाद् भविष्यति** — and म्लिष्ट's इ is laid down "
            "with the rest, **इत्वमप्येकारस्य निपातनादेव**"),
    Anit(
        "7.2.19", of=("dhṛṣ", "śas"), before=("niṣṭhā",),
        sense="vaiyātya",
        keeps_out="धर्षितः, विशसितः — no boldness meant",
        why="धृषिशसी वैयात्ये — धृष् and शस् take no इट् in the "
            "निष्ठा where BOLDNESS is meant: **धृष्टोऽयम्, "
            "विशस्तोऽयम्**. **वियातस्य भावो वैयात्यम्, "
            "प्रागल्भ्यम्, अविनीतता**.\\n\\n"
            "**AND IT IS A नियम, BOTH REFUSALS BEING ALREADY "
            "SUPPLIED.** धृष् is आदित् and caught by 7.2.16; "
            "शस् is उदित् and caught through 7.2.15. "
            "**नियमार्थं वचनम्। धृषिशस्योर् वैयात्य एवेड् न "
            "भवति** — in that sense only, and 7.2.17's option "
            "does not reach it: **भावादिकर्मणोरपि वैयात्ये "
            "धृषिर् नास्ति**"),
    Anit(
        "7.2.20", of=("dṛḍha",), before=("niṣṭhā",),
        sense="sthūla-bala", nipatana=True,
        keeps_out="दृंहितम्, दृहितम् — neither thickness nor "
                  "strength meant",
        why="दृढः स्थूलबलयोः — दृढ is laid down whole where "
            "THICKNESS or STRENGTH is meant: **दृढः स्थूलः; "
            "दृढो बलवान्**. Four things at once: **दृंहेः "
            "क्तप्रत्यय इडभावः, हकारनकारयोर् लोपः, परस्य "
            "ढत्वम्**.\\n\\n"
            "**AND THE ह्-LOSS IS LAID DOWN RATHER THAN "
            "DERIVED, TO ESCAPE 8.2.1.** Lose the ढ instead and "
            "the loss is असिद्ध for everything earlier, and "
            "then 6.4.161's र would not reach द्रढिमा; 6.4.56's "
            "अय् would not reach परिद्रढय्य; and 4.1.78's ष्यङ् "
            "would wrongly reach पारिदृढी. Three rules saved by "
            "one choice of what to lay down"),
    Anit(
        "7.2.21", of=("parivṛḍha",), before=("niṣṭhā",),
        sense="prabhu", nipatana=True,
        keeps_out="परिवृंहितम्, परिवृहितम् — no lord meant",
        why="प्रभौ परिवृढः — and परिवृढ where a LORD is meant: "
            "**परिवृढः कुटुम्बी**. **पूर्वेण तुल्यम् एतत्** — "
            "built exactly as दृढ was, from वृंह्, and the "
            "ह्-loss laid down for the same three reasons: "
            "**परिव्रढयति, परिव्रढय्य गतः, पारिवृढी कन्या**"),
    Anit(
        "7.2.22", of=("kaṣ",), before=("niṣṭhā",),
        sense="kṛcchra-gahana",
        keeps_out="कषितं सुवर्णम् — gold rubbed on a touchstone, "
                  "and neither hardship nor thicket",
        why="कृच्छ्रगहनयोः कषः — कष् takes no इट् where HARDSHIP "
            "or a THICKET is meant: **कष्टोऽग्निः; कष्टं "
            "व्याकरणम्; ततोऽपि कष्टतराणि सामानि; कष्टानि वनानि; "
            "कष्टाः पर्वताः**. **कृच्छ्रं दुःखम्, तत्कारणमप्य् "
            "अग्न्यादिकं कृच्छ्रम् इत्युच्यते** — the cause of "
            "the difficulty is called by the difficulty's name, "
            "which is how fire and grammar get on the same list"),
    Anit(
        "7.2.23", of=("ghuṣ",), before=("niṣṭhā",),
        sense="a-viśabdana",
        keeps_out="अवघुषितं वाक्यम् — a thing declared, and "
                  "विशब्दनं प्रतिज्ञानम्",
        why="घुषिरविशब्दने — घुष् takes none where no DECLARING "
            "is meant: **घुष्टा रज्जुः; घुष्टौ पादौ**. There "
            "are two घुष् roots, one in भ्वादि and one in "
            "चुरादि, and **तयोर् इह सामान्येन ग्रहणम्**.\\n\\n"
            "**AND THE EXCEPTION IS ITSELF A ज्ञापक.** "
            "**विशब्दनप्रतिषेधश्च ज्ञापकश् चुरादिणिज् "
            "विशब्दनार्थस्यानित्य इति** — the चुरादि णिच् is "
            "not compulsory in that sense, which lets "
            "**जुघुषुः पुष्यमाणवाः** stand"),
    Anit(
        "7.2.24", of=("ard",), upasarga=("sam", "ni", "vi"),
        before=("niṣṭhā",),
        keeps_out="समेधितः — another root; अर्दितः — no preverb",
        why="अर्देः संनिविभ्यः — अर्द् takes none after सम्, नि "
            "and वि: **समर्णः, न्यर्णः, व्यर्णः**. Three "
            "preverbs and no fourth, and the vṛtti tests both "
            "halves of the condition: **अर्देरिति किम्? "
            "समेधितः। संनिविभ्य इति किम्? अर्दितः**"),
    Anit(
        "7.2.25", of=("ard",), upasarga=("abhi",),
        before=("niṣṭhā",), sense="āvidūrya",
        keeps_out="अभ्यर्दितो वृषलः — pained with cold, and no "
                  "nearness meant",
        why="अभेश्चाविदूर्येऽर्थे — and after अभि where NEARNESS "
            "is meant: **अभ्यर्णा सेना; अभ्यर्णा शरत्**. "
            "**विदूरं विप्रकृष्टम्, ततोऽन्यद् अविदूरम्, तस्य "
            "भाव आविदूर्यम्** — and the word being laid down "
            "here is what lets it escape 5.1.121's refusal of "
            "an abstract affix after a नञ्-compound"),
    Anit(
        "7.2.26", of=("vṛt",), before=("niṣṭhā",),
        sense="adhyayana", nipatana=True,
        keeps_out="वर्तितमन्यत् — no recitation meant",
        why="णेरध्ययने वृत्तम् — वृत्त is laid down for the "
            "causal of वृत् where RECITATION is meant, with "
            "both the इट् refused and the णि dropped: **वृत्तो "
            "गुणो देवदत्तेन; वृत्तं पारायणं देवदत्तेन**.\\n\\n"
            "**AND THE vṛtti ASKS WHETHER THE SŪTRA IS NEEDED "
            "AND GIVES TWO ANSWERS.** वृत् is intransitive and "
            "becomes transitive in the causal sense, so 5.1.79's "
            "pattern would have given the form anyway. "
            "**तत् क्रियते यदापि णिचैव ण्यर्थोऽभिधीयते, तदा "
            "वर्तितम् इत्यध्ययने मा भूद् इति केचित्। अपरे तु "
            "वर्तितो गुणो देवदत्तेनेत्यपीच्छन्ति** — some make "
            "it exclusive, others allow both"),
    Anit(
        "7.2.27", of=DANTA_SEVEN, before=("niṣṭhā",),
        gana="ṇyanta", optional=True, nipatana=True,
        why="वा दान्तशान्तपूर्णदस्तस्पष्टच्छन्नज्ञप्ताः — seven "
            "causal stems are laid down OPTIONALLY without the "
            "इट्, and with the णि dropped: **दान्तः, दमितः; "
            "शान्तः, शमितः; पूर्णः, पूरितः; दस्तः, दासितः; "
            "स्पष्टः, स्पाशितः; छन्नः, छादितः; ज्ञप्तः, "
            "ज्ञपितः**. ज्ञप् is there for a different reason "
            "from the rest: 7.2.49 makes its इट् optional, "
            "7.2.15 would then have refused it outright, and "
            "this sūtra gives the option back"),
    Anit(
        "7.2.28", of=RUSYAMADI, before=("niṣṭhā",), optional=True,
        why="रुष्यमत्वरसंघुषास्वनाम् — and five roots, likewise "
            "optionally: **रुष्टः, रुषितः; अभ्यान्तः, "
            "अभ्यमितः; तूर्णः, त्वरितः; संघुष्टौ पादौ, "
            "संघुषितौ पादौ; आस्वान्तो देवदत्तः, आस्वनितो "
            "देवदत्तः**.\\n\\n"
            "**AND TWO OF THE FIVE DISPLACE EARLIER RULES BY "
            "BEING LATER.** संघुष् would have been refused "
            "outright by 7.2.23 even where declaring is meant, "
            "and आस्वन् laid down by 7.2.18 where the mind is "
            "meant; **परत्वाद् अयम् एव विकल्पो भवति** — this "
            "option wins over both, and संघुष्टं वाक्यम् and "
            "आस्वान्तं मनः have their इट् forms beside them"),
    Anit(
        "7.2.29", of=("hṛṣ",), before=("niṣṭhā",), sense="loman",
        optional=True,
        keeps_out="हृष्टो देवदत्तः, हृषितो देवदत्तः — of a man "
                  "and not of hair, where the two roots are "
                  "simply different words",
        why="हृषेर्लोमसु — हृष् takes the इट् optionally where "
            "HAIR is meant: **हृष्टानि लोमानि, हृषितानि "
            "लोमानि; हृष्टाः केशाः, हृषिताः केशाः**.\\n\\n"
            "**AND THE OPTION IS THERE BECAUSE THERE ARE TWO "
            "ROOTS.** **हृषु अलीके** is उदित् and so अनिट् in "
            "the निष्ठा; **हृष तुष्टौ** is सेट्. Naming both "
            "makes an option out of two settled facts — "
            "**तयोर् उभयोर् इह ग्रहणम् इत्युभयत्रविभाषेयम्**. A "
            "vārttika adds two more senses: "
            "**विस्मितप्रतिघातयोश्चेति वक्तव्यम्**"),
    Anit(
        "7.2.30", of=("apacita",), before=("niṣṭhā",),
        nipatana=True, optional=True,
        why="अपचितश्च — अपचित is laid down beside अपचायित, with "
            "the इट् refused and चि standing for चाय्: "
            "**अपचितोऽनेन गुरुः, अपचायितोऽनेन गुरुः**. And a "
            "vārttika makes it compulsory before क्तिन् — "
            "**क्तिनि नित्यम् इति वक्तव्यम्। अपचितिः**"),
    Anit(
        "7.2.31", of=("hvṛ",), before=("niṣṭhā",), chandasi=True,
        nipatana=True,
        keeps_out="ह्वृतम् — outside the Veda",
        why="ह्रु ह्वरेश्छन्दसि — ह्वृ becomes ह्रु in the "
            "निष्ठा in the Veda: **ह्रुतस्य चाह्रुतस्य च; "
            "अह्रुतमसि हविर्धानम्**"),
    Anit(
        "7.2.32", of=("aparihvṛta",), chandasi=True, nipatana=True,
        blocks=("7.2.31",),
        why="अपरिह्वृताश्च — but अपरिह्वृत is laid down WITHOUT "
            "that substitution: **अपरिह्वृताः सनुयाम वाजम्**. "
            "A निपातन whose whole content is that the sūtra "
            "before does not apply"),
    Anit(
        "7.2.33", of=("hvṛ",), before=("niṣṭhā",), sense="soma",
        chandasi=True, nipatana=True, supplies=True,
        blocks=("7.2.31",),
        why="सोमे ह्वरितः — and ह्वरित is laid down of SOMA, with "
            "the इट् GIVEN and guṇa besides: **मा नः सोमो "
            "ह्वरितः; विह्वरितस्त्वम्**. The first of the run's "
            "two rules that supply the augment instead of "
            "refusing it"),
    Anit(
        "7.2.34", of=CHANDASI_ISLANDS, chandasi=True,
        nipatana=True, supplies=True,
        why="ग्रसितस्कभितस्तभितोत्तभितचत्तविकस्तविशस्तॄशंस्तृ"
            "शास्तृतरुतृतरूतृवरुतृवरूतृवरुत्रीरुज्ज्वलितिक्षरिति"
            "क्षमितिवमित्यमितीति च — nineteen Vedic forms laid "
            "down, and most of them WITH the इट् that the "
            "ordinary grammar refuses: **ग्रसितं वा एतत् "
            "सोमस्य** where the language has ग्रस्तम्; "
            "**विष्कभिते अजरे** for विष्कब्धम्; **येन स्वः "
            "स्तभितम्** for स्तब्धम्; **सत्येनोत्तभिता भूमिः** "
            "for उत्तब्धा. ग्रस्, स्कम्भ् and स्तम्भ् are all "
            "उदित् and so अनिट् in the निष्ठा, and the Veda has "
            "them the other way.\\n\\n"
            "**AND उत्तभित IS NAMED WITH ITS PREVERB ON "
            "PURPOSE.** **उत्तभितेति उत्पूर्वस्य "
            "निपातनसामर्थ्याद् अन्योपसर्गपूर्वः स्तभितशब्दो न "
            "भवति** — laid down with उत्, it is available with "
            "उत् and with nothing else.\\n\\n"
            "**AND THIS CLOSES THE निष्ठा HEADING.** The next "
            "sūtra is आर्धधातुकस्येड् वलादेः, which finally "
            "gives the इट् that all twenty-seven of these have "
            "been refusing"),
)


def _reaches(row: Anit, root: str, gana: str, before: str,
             upasarga: str, sense: str, chandasi: bool) -> bool:
    if row.pairs and root and root not in dict(row.pairs):
        return False
    named = row.of or row.gana
    if named and not (root in row.of
                      or (row.gana and gana == row.gana)):
        return False
    if row.before and before not in row.before:
        return False
    if row.upasarga and upasarga not in row.upasarga:
        return False
    if row.sense and sense != row.sense:
        return False
    if row.chandasi and not chandasi:
        return False
    return True


def _how_specific(row: Anit, root: str, gana: str) -> int:
    """
    A rule that names what it displaces beats it, a named sense
    beats a named root, and a named root beats a named class.

    7.2.16 against 7.2.17 needs the first, 7.2.23 against 7.2.28
    the whole of it: घुष् is refused outright where no declaring
    is meant, and then a later sūtra makes संघुष् optional in
    every sense at once.
    """
    return (
        12 * len(row.blocks)
        + 8 * bool(row.of and root in row.of)
        + 6 * bool(row.sense)
        + 5 * bool(row.gana and gana == row.gana)
        + 4 * bool(row.upasarga)
        + 3 * bool(row.before)
        + 2 * bool(row.chandasi)
    )


@dataclass(frozen=True)
class Augmentless:
    """What the run answers: the इट् refused, given, or optional."""

    #: "" where the इट् is refused, "iṭ" where this run supplies
    #: it, and the sense-paired form where one is laid down.
    does: str
    sutra: str
    why: str
    nipatana: bool = False
    optional: bool = False
    blocked_by: Tuple[str, ...] = ()


def _becomes(row: Anit, root: str) -> str:
    if row.supplies:
        return "iṭ"
    for named, sense in row.pairs:
        if named == root:
            return sense
    return ""


def no_it(root: str = "", *, gana: str = "", before: str = "",
          upasarga: str = "", sense: str = "",
          chandasi: bool = False) -> Augmentless:
    """
    7.2.8–34 — where the इट् is refused before it is ever given.

    Nothing answers by default, and the default is the इट्: 7.2.35
    supplies it to every ārdhadhātuka beginning with a वल् sound,
    and this run is the list of places that rule does not reach.
    """
    matched = [
        row for row in ANIT_TABLE
        if _reaches(row, root, gana, before, upasarga, sense,
                    chandasi)
    ]
    if not matched:
        return Augmentless(
            "iṭ", "", "No rule of 7.2.8-34 refuses the augment, "
                      "so 7.2.35 gives it")
    row = max(matched, key=lambda one: _how_specific(one, root, gana))
    return Augmentless(_becomes(row, root), row.sutra, row.why,
                       nipatana=row.nipatana, optional=row.optional,
                       blocked_by=row.blocks)


def provisions_for(sutra_id: str) -> Tuple[Anit, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in ANIT_TABLE if row.sutra == sutra_id)


__all__ = [
    "Anit", "ANIT_TABLE", "ANIT_RUN", "NISTHA_FROM", "NISTHA_TO",
    "THE_RULE_ITSELF", "TITUTRA", "KRADI_EIGHT", "NIPATANA_EIGHT",
    "DANTA_SEVEN", "RUSYAMADI", "CHANDASI_ISLANDS",
    "Augmentless", "no_it", "provisions_for",
]
