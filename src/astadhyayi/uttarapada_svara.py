# -*- coding: utf-8 -*-
"""
६.२.१११–१९९ — the accent moves to the SECOND member, and stays there
to the end of the pāda.

6.2.1–110 were all about the पूर्वपद: it kept its own accent, or was
given one on its first or its last syllable. 6.2.111 turns the pāda
over. **उत्तरपदादिरित्येतदधिकृतम्। यदित ऊर्ध्वमनुक्रमिष्याम
उत्तरपदस्यादिरुदात्तो भवतीत्येवं तद् वेदितव्यम्** — from here it is
the SECOND member that is accented, and **उत्तरपदस्येत्येतदा
पादपरिसमाप्तेः**: that word runs to the last sūtra of the pāda.

**AND ONE HEADING'S TWO WORDS AGAIN STOP IN DIFFERENT PLACES.** The
same shape 6.2.1 and 6.2.64 had, for the third and last time.
6.2.111's own vṛtti: **आदिरिति प्रकृत्या भगालम् इति यावत्** — the
word आदिः holds only to 6.2.136, and 6.2.137 प्रकृत्या भगालम्
replaces it with a third placement, **प्रकृत्येत्येतदधिकृतम् अन्तः
इति यावद् वेदितव्यम्**, which itself lasts only to 6.2.142. Then
6.2.143 अन्तः takes the remaining fifty-seven sūtras: **अन्त
इत्यधिकारः... समासस्योत्तरपदस्यान्त उदात्तो भवति**.

So the pāda's second half is three runs end to end, under one
scope-word:

    उत्तरपद  ६.२.१११ ─────────────────────────────── ६.२.१९९
    आदिः     ६.२.१११ ── ६.२.१३६
    प्रकृत्या            ६.२.१३७ ── ६.२.१४२
    अन्तः                          ६.२.१४३ ──────── ६.२.१९९

**AND TWO RULES ACCENT NEITHER MEMBER BUT BOTH.** 6.2.140 उभे
वनस्पत्यादिषु युगपत् and 6.2.141 देवताद्वन्द्वे च leave पूर्वपद and
उत्तरपद each with its own accent AT THE SAME TIME — **युगपदुभे
पूर्वोत्तरपदे प्रकृतिस्वरे भवतः** — so वनस्पतिः carries two उदात्तs
and इन्द्राबृहस्पती three. Nothing else in the Aṣṭādhyāyī puts three
उदात्तs in one word.

**AND THREE RULES ACCENT SOMETHING THAT IS NEITHER FIRST NOR LAST.**
6.2.173 कपि पूर्वम् accents what stands BEFORE the कप्; 6.2.174
ह्रस्वान्तेऽन्त्यात् पूर्वम् the syllable before the last; and
6.2.199 परादिश्छन्दसि बहुलम् the first syllable of the word that
FOLLOWS. The pāda ends by loosening its own grip: **परादिश्च
परान्तश्च पूर्वान्तश्चापि दृश्यते। पूर्वादयश्च दृश्यन्ते व्यत्ययो
बहुलं ततः**.

**WHAT THIS MODULE DOES NOT DO.** It reports which rule accents the
second member and where. It does not count syllables or read affixes
off a form: 6.2.119's *two vowels and already ādi-accented*,
6.2.138's *not many-voweled*, 6.2.174's *ending in a short vowel* are
conditions the query carries, not ones the code works out.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

from src.astadhyayi.purvapada_udatta import Accented, BAHUVRIHI_RUN

#: The scope-word उत्तरपदम्, which lasts to the end of the pāda:
#: **उत्तरपदस्येत्येतदा पादपरिसमाप्तेः**.
UTTARAPADA_RUN: Tuple[str, str] = ("6.2.111", "6.2.199")

#: आदिः, which does not: **आदिरिति प्रकृत्या भगालम् इति यावत्**.
ADI_RUN: Tuple[str, str] = ("6.2.111", "6.2.136")

#: प्रकृत्या, which replaces it: **प्रकृत्येत्येतदधिकृतम् अन्तः इति
#: यावद् वेदितव्यम्**.
PRAKRTI_RUN: Tuple[str, str] = ("6.2.137", "6.2.142")

#: And अन्तः, which takes the rest: **अन्त इत्यधिकारः। यदित
#: ऊर्ध्वमनुक्रमिष्यामस्तत्र समासस्योत्तरपदस्यान्त उदात्तो भवति**.
ANTA_RUN: Tuple[str, str] = ("6.2.143", "6.2.199")

#: क्रत्वादि, read out at the end of 6.2.118's vṛtti.
KRATVADI: Tuple[str, ...] = (
    "kratu", "dṛśīka", "pratīka", "pratūrti", "havya", "bhaga")

#: चिहणादि, at 6.2.125 — with the vṛtti's own three variant readings
#: kept, since it names them as readings and not as errors:
#: **मडुर इति केचित् पठन्ति... चित्कण इत्यपरे पठन्ति**.
CIHANADI: Tuple[str, ...] = (
    "cihaṇa", "maḍara", "maḍḍara", "maḍura", "vaitula", "paṭatka",
    "caittālikarṇa", "caittālikarṇi", "kukkuṭa", "cikkaṇa", "citkaṇa")

#: चूर्णादि, at 6.2.134.
CURNADI: Tuple[str, ...] = (
    "cūrṇa", "karipa", "kariva", "śākina", "śākaṭa", "drākṣā",
    "tūsta", "kundama", "dalapa", "camasī", "cakkana", "caula")

#: The six of 6.2.135 षट् च काण्डादीनि — every one of them a word
#: 6.2.126–129 had already accented under a sense-condition, now
#: freed of it after a non-living genitive.
THE_SIX: Tuple[str, ...] = (
    "kāṇḍa", "cīra", "palala", "sūpa", "śāka", "kūla")

#: वर्ग्यादि, at 6.2.131 — and the vṛtti says where to find it:
#: **वर्ग्यादयः प्रातिपदिकेषु न पठ्यन्ते। दिगादिषु तु वर्ग पूग गण
#: पक्ष इत्येवमादयो ये पठिताः, त एव यत्प्रत्ययान्ता वर्ग्यादय इह
#: प्रतिपत्तव्याः** — दिगादि's members with यत् on them.
VARGYADI: Tuple[str, ...] = ("vargya", "pūgya", "gaṇya", "pakṣya")

#: चार्वादि, at 6.2.160.
CARVADI: Tuple[str, ...] = ("cāru", "sādhu", "yaudhika", "vadānya")

#: गौरादि, which 6.2.194 keeps OUT.
GAURADI: Tuple[str, ...] = (
    "gaura", "taiṣa", "taiṭa", "laṭa", "loṭa", "jihvā", "kṛṣṇā",
    "kanyā", "guḍa", "kalpa", "pāda")

#: अंश्वादि, at 6.2.193.
AMSVADI: Tuple[str, ...] = (
    "aṃśu", "jana", "rājan", "uṣṭra", "kheṭaka", "ajira", "ārdrā",
    "śravaṇa", "kṛttikā", "ardha", "pura")

#: निरुदकादि, at 6.2.184 — a list of whole COMPOUNDS, not of second
#: members: **निरुदकादीनि च शब्दरूपाणि**.
NIRUDAKADI: Tuple[str, ...] = (
    "nirudaka", "nirulapa", "nirupala", "nirmaśaka", "nirmakṣika",
    "niṣkālaka", "niṣkālika", "niṣpeṣa", "dustarīpa")

#: The gaṇas of this stretch the vṛtti itself calls open-ended.
AKRTIGANA: Tuple[str, ...] = ("pravṛddhādi", "guṇādi")

#: What 6.2.133 refuses 6.2.132 for, in the vṛtti's own glosses:
#: **आचार्य उपाध्यायः। राजा ईश्वरः। ऋत्विजो याजकाः। संयुक्ताः
#: स्त्रीसंबन्धिनः श्यालादयः। ज्ञातयो मातृपितृसंबन्धिनो बान्धवाः**.
ACARYADI: Tuple[str, ...] = (
    "ācārya", "rājan", "ṛtvij", "saṃyukta", "jñāti")

#: 6.2.142's four exceptions — the दैवत pairs that keep both accents
#: even though the second word does not begin अनुदात्त.
DEVATA_EXCEPTIONS: Tuple[str, ...] = (
    "pṛthivī", "rudra", "pūṣan", "manthin")

#: The verse 6.2.199's vṛtti closes the pāda with.
VYATYAYA_VERSE: str = (
    "परादिश्च परान्तश्च पूर्वान्तश्चापि दृश्यते।\n"
    "पूर्वादयश्च दृश्यन्ते व्यत्ययो बहुलं ततः॥")


@dataclass(frozen=True)
class Uttarapada:
    """One rule of 6.2.111–199: what it does to the second member."""

    sutra: str
    #: ādi, prakṛti, anta — and the four odd ones: ubhe-prakṛti,
    #: pūrvapada-ādi, pūrva-anta, antyāt-pūrva, para-ādi, nañvat.
    where: str = ""
    #: The second members the rule names outright.
    of: Tuple[str, ...] = ()
    #: A named class of second member instead.
    gana: str = ""
    #: What the second member ends in — any one of these.
    affix: Tuple[str, ...] = ()
    #: The first members the rule names outright.
    purvapada: Tuple[str, ...] = ()
    #: A named class of first member instead.
    purvapada_gana: Tuple[str, ...] = ()
    samasa: str = ""
    case: str = ""
    #: The further condition — a sense (गर्हा, आक्रोश, संज्ञा) or a
    #: shape (द्व्यच्, ह्रस्वान्त). Any one of them suffices.
    result: Tuple[str, ...] = ()
    #: What the rule keeps out of its own reach.
    excludes: Tuple[str, ...] = ()
    refuses: bool = False
    optional: bool = False
    heading: bool = False
    chandasi: bool = False
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


UTTARAPADA_TABLE: Tuple[Uttarapada, ...] = (
    Uttarapada(
        "6.2.111", where="ādi", heading=True,
        why="उत्तरपदादिः — **उत्तरपदादिरित्येतदधिकृतम्। यदित "
            "ऊर्ध्वमनुक्रमिष्याम उत्तरपदस्यादिरुदात्तो भवतीत्येवं "
            "तद् वेदितव्यम्** — from here it is the SECOND member "
            "that is accented, on its first syllable. The vṛtti "
            "reads the next sūtra out as its example: **वक्ष्यति "
            "कर्णो वर्णलक्षणात् — शुक्लकर्णः, कृष्णकर्णः**.\\n\\n"
            "**AND THE HEADING'S TWO WORDS STOP IN DIFFERENT "
            "PLACES, FOR THE THIRD TIME IN THIS PĀDA.** "
            "**उत्तरपदस्येत्येतदा पादपरिसमाप्तेः। आदिरिति प्रकृत्या "
            "भगालम् इति यावत्** — उत्तरपदम् to the last sūtra of "
            "the pāda, आदिः only to 6.2.136. 6.2.1 split प्रकृत्या "
            "from पूर्वपदम् the same way, and 6.2.64 split आदिः "
            "from उदात्तः"),
    Uttarapada(
        "6.2.112", where="ādi", of=("karṇa",),
        purvapada_gana=("varṇa", "lakṣaṇa"), samasa="bahuvrīhi",
        keeps_out="शोभनकर्णः — neither a colour nor a mark; "
                  "श्वेतपादः, कूटशृङ्गः — not कर्ण; स्थूलकर्णः — "
                  "thickness is not a MARK",
        why="कर्णो वर्णलक्षणात् — कर्ण as second member of a "
            "बहुव्रीहि takes the accent on its first syllable when "
            "the first member names a COLOUR or a MARK: "
            "**शुक्लकर्णः, कृष्णकर्णः; दात्राकर्णः, "
            "शङ्कूकर्णः**.\\n\\n"
            "**AND लक्षण HERE IS A BRAND AND NOT A PROPERTY.** "
            "**पशूनां विभागज्ञापनार्थं दात्रशङ्कुप्रतिरूपकं "
            "कर्णादिषु चिह्नं यत् क्रियते तदिह लक्षणं गृह्यते** — "
            "the sickle-shaped or peg-shaped nick cut in a beast's "
            "ear to show whose herd it belongs to. **तेन "
            "स्थूलकर्ण इत्यत्र न भवति**"),
    Uttarapada(
        "6.2.113", where="ādi", of=("karṇa",),
        result=("saṃjñā", "aupamya"), samasa="bahuvrīhi",
        why="संज्ञायामौपम्ययोश्च — and कर्ण takes the same accent "
            "where the बहुव्रीहि is a NAME or a COMPARISON: "
            "**कुञ्चिकर्णः, मणिकर्णः** for names, **गोकर्णः, "
            "खरकर्णः** for comparisons — one whose ears are like a "
            "cow's, like a donkey's"),
    Uttarapada(
        "6.2.114", where="ādi",
        of=("kaṇṭha", "pṛṣṭha", "grīvā", "jaṅghā"),
        result=("saṃjñā", "aupamya"), samasa="bahuvrīhi",
        why="कण्ठपृष्ठग्रीवाजङ्घं च — and four more body-words go "
            "the same way in a बहुव्रीहि that is a name or a "
            "comparison: **शितिकण्ठाः, नीलकण्ठः** beside **खरकण्ठः, "
            "उष्ट्रकण्ठः**; **काण्डपृष्ठः, नाकपृष्ठः** beside "
            "**गोपृष्ठः, अजपृष्ठः**; **सुग्रीवः, नीलग्रीवः, "
            "दशग्रीवः** beside **गोग्रीवः, अश्वग्रीवः**; "
            "**नाडीजङ्घः, तालजङ्घः** beside **गोजङ्घः, अश्वजङ्घः, "
            "एणीजङ्घः**"),
    Uttarapada(
        "6.2.115", where="ādi", of=("śṛṅga",),
        result=("avasthā", "saṃjñā", "aupamya"), samasa="bahuvrīhi",
        keeps_out="स्थूलशृङ्गः — no stage of life, no name, no "
                  "comparison",
        why="शृङ्गमवस्थायां च — शृङ्ग adds a third sense to the two "
            "before it, a STAGE OF LIFE: **उद्गतशृङ्गः, "
            "द्व्यङ्गुलशृङ्गः, त्र्यङ्गुलशृङ्गः**, and the vṛtti "
            "says what the stage is — **शृङ्गोद्गमनादिकृतो गवादेर् "
            "वयोविशेषोऽवस्था**, the age of an ox told by how far "
            "its horns have come up. With the name and the "
            "comparison too: **ऋष्यशृङ्गः; गोशृङ्गः, मेषशृङ्गः**"),
    Uttarapada(
        "6.2.116", where="ādi", purvapada=("nañ",),
        of=("jara", "mara", "mitra", "mṛta"), samasa="bahuvrīhi",
        blocks=("6.2.172",),
        keeps_out="ब्राह्मणमित्रः — the first member is not नञ्; "
                  "अशत्रुः — शत्रु is not one of the four",
        why="नञो जरमरमित्रमृताः — after नञ्, these four second "
            "members are accented on their first syllable in a "
            "बहुव्रीहि: **अजरः, अमरः, अमित्रः, अमृतः**.\\n\\n"
            "**AND WHAT IT IS AN EXCEPTION TO COMES LATER THAN "
            "IT.** **जरादय इति किम्? अशत्रुः। नञ्सुभ्याम् इति "
            "उत्तरपदान्तोदात्तत्वमेवात्र भवति** — outside the four, "
            "6.2.172 accents the LAST syllable instead. A rule "
            "carving four words out of a rule fifty-six sūtras "
            "further on"),
    Uttarapada(
        "6.2.117", where="ādi", purvapada=("su",),
        affix=("man", "as"), excludes=("loman", "uṣas"),
        samasa="bahuvrīhi", blocks=("6.2.172",),
        keeps_out="कृतकर्मा, कृतयशाः — the first member is not सु; "
                  "सुराजा, सुतक्षा — neither मन् nor अस्; सुलोमा, "
                  "सूषाः — the two the sūtra names",
        why="सोर्मनसी अलोमोषसी — after सु, a second member ending "
            "in मन् or in अस् is accented on its first syllable, "
            "except लोमन् and उषस्: **सुकर्मा, सुधर्मा, सुप्रथिमा; "
            "सुपयाः, सुयशाः, सुस्रोताः**.\\n\\n"
            "**AND THE TWO ENDINGS ARE TAKEN WHETHER THEY MEAN "
            "ANYTHING OR NOT.** **अनिनस्मन्ग्रहणान्यर्थवता चानर्थकेन "
            "च इत्यनर्थकयोरपि मनसोरिह ग्रहणम्** — मन् and अस् count "
            "even where they are not affixes carrying a sense but "
            "merely the shape the word ends in.\\n\\n"
            "**AND IT LOSES TO 6.2.173 BY BEING EARLIER.** It is "
            "an अपवाद of 6.2.172 — **नञ्सुभ्याम् इत्यस्यायमपवादः** "
            "— but **कपि तु परत्वात् कपि पूर्वम् इत्येतद् भवति**: "
            "add कप् and the later rule takes over"),
    Uttarapada(
        "6.2.118", where="ādi", purvapada=("su",), gana="kratvādi",
        samasa="bahuvrīhi",
        why="क्रत्वादयश्च — and the क्रत्वादि words after सु: "
            "**सुक्रतुः, सुदृशीकः**. The gaṇa is six long — "
            "**क्रतु। दृशीक। प्रतीक। प्रतूर्ति। हव्य। भग। "
            "क्रत्वादिः**"),
    Uttarapada(
        "6.2.119", where="ādi", purvapada=("su",),
        result=("ādyudātta-dvyac",), chandasi=True,
        samasa="bahuvrīhi", blocks=("6.2.172",),
        keeps_out="या सुबाहुः स्वङ्गुरिः — बाहु is end-accented by "
                  "its affix; सुगुरसत् सुहिरण्यः — हिरण्य has three "
                  "vowels; स्वश्वः outside the Veda",
        why="आद्युदात्तं द्व्यच्छन्दसि — in the Veda, a second "
            "member after सु that has TWO vowels and was ALREADY "
            "accented on its first syllable stays so: **स्वश्वास्त्वा "
            "सुरथा मर्जयेम**.\\n\\n"
            "**SO THE RULE CHANGES NOTHING AND STILL DOES "
            "SOMETHING.** **नित्स्वरेणाश्वरथशब्दावाद्युदात्तौ** — "
            "अश्व and रथ are already ādi-accented by 6.1.197. What "
            "6.2.119 does is stop 6.2.172 from moving that accent "
            "to the end: **नञ्सुभ्याम् इत्यस्यायमपवादः**"),
    Uttarapada(
        "6.2.120", where="ādi", purvapada=("su",),
        of=("vīra", "vīrya"), chandasi=True, samasa="bahuvrīhi",
        why="वीरवीर्यौ च — and these two after सु, in the Veda: "
            "**सुवीरस्ते; सुवीर्यस्य पतयः स्याम**.\\n\\n"
            "**AND NAMING वीर्य TEACHES SOMETHING ABOUT ANOTHER "
            "RULE.** **वीर्यमिति यत्प्रत्ययान्तं तत्र यतोऽनावः "
            "इत्याद्युदात्तत्वं न भवतीत्येतदेव वीर्यग्रहणं ज्ञापकम्। "
            "तत्र हि सति पूर्वेणैव सिद्धं स्यात्** — if 6.1.213 "
            "यतोऽनावः reached वीर्य, 6.2.119 would already have "
            "covered it and this sūtra would name it for nothing. "
            "Naming it says 6.1.213 does not"),
    Uttarapada(
        "6.2.121", where="ādi",
        of=("kūla", "tīra", "tūla", "mūla", "śālā", "akṣa", "sama"),
        samasa="avyayībhāva", blocks=("6.2.33",),
        keeps_out="उपकुम्भम् — कुम्भ is not in the seven; "
                  "परमकूलम्, उत्तमकूलम् — not an अव्ययीभाव",
        why="कूलतीरतूलमूलशालाक्षसमम् अव्ययीभावे — seven second "
            "members are accented on their first syllable in an "
            "अव्ययीभाव: **परिकूलम्, उपकूलम्, परितीरम्, उपतीरम्, "
            "परितूलम्, उपतूलम्, परिमूलम्, उपमूलम्, परिशालम्, "
            "उपशालम्, पर्यक्षम्, उपाक्षम्, सुषमम्, विषमम्, निषमम्, "
            "दुःषमम्**. They come in with the compound itself: "
            "**तिष्ठद्गुप्रभृतिषु एते पठ्यन्ते**.\\n\\n"
            "**AND IT WINS AGAINST AN EARLIER RULE OF THIS PĀDA BY "
            "BEING LATER.** **पर्यादिभ्यः कूलादीनामाद्युदात्तत्वं "
            "विप्रतिषेधेन भवति** — where 6.2.33 would keep the "
            "first member's accent instead, 6.2.121 takes it"),
    Uttarapada(
        "6.2.122", where="ādi",
        of=("kaṃsa", "mantha", "śūrpa", "pāyya", "kāṇḍa"),
        samasa="dvigu",
        keeps_out="परमकंसः, उत्तमकंसः — not a द्विगु",
        why="कंसमन्थशूर्पपाय्यकाण्डं द्विगौ — five second members "
            "are accented on their first syllable in a द्विगु: "
            "**द्विकंसः, त्रिकंसः, द्विमन्थः, त्रिमन्थः, द्विशूर्पः, "
            "त्रिशूर्पः, द्विपाय्यः, त्रिपाय्यः, द्विकाण्डः, "
            "त्रिकाण्डः** — worth two कंसas, worth three, and so on"),
    Uttarapada(
        "6.2.123", where="ādi", of=("śālā",), samasa="tatpuruṣa",
        result=("napuṃsaka",),
        keeps_out="दृढशालं ब्राह्मणकुलम् — a बहुव्रीहि; "
                  "ब्राह्मणसेनम् — not शाला; ब्राह्मणशाला — not "
                  "neuter",
        why="तत्पुरुषे शालायां नपुंसके — शाला at the end of a "
            "NEUTER तत्पुरुष is accented on its first syllable: "
            "**ब्राह्मणशालम्, क्षत्रियशालम्**. The neuter is not "
            "chosen here but supplied by another rule — **विभाषा "
            "सेनासुराच्छायाशालानिशानाम् इति नपुंसकलिङ्गता**"),
    Uttarapada(
        "6.2.124", where="ādi", of=("kanthā",), samasa="tatpuruṣa",
        result=("napuṃsaka",),
        keeps_out="दाक्षिकन्था — not neuter",
        why="कन्था च — and कन्था likewise, in a neuter तत्पुरुष: "
            "**सौशमिकन्थम्, आह्वकन्थम्, चप्पकन्थम्**. The neuter "
            "again comes from elsewhere — **संज्ञायां कन्थोशीनरेषु "
            "इति नपुंसकलिङ्गता** — and the vṛtti records what kind "
            "of compound these are: **षष्ठीसमासा एते**"),
    Uttarapada(
        "6.2.125", where="pūrvapada-ādi", of=("kanthā",),
        purvapada_gana=("cihaṇādi",), samasa="tatpuruṣa",
        result=("napuṃsaka",),
        why="आदिश्चिहणादीनाम् — before कन्था, the चिहणादि words "
            "are accented on THEIR first syllable, not on the "
            "second member's: **चिहणकन्थम्, मडरकन्थम्, "
            "मडुरकन्थम्**.\\n\\n"
            "**AND THE REPEATED WORD आदिः IS WHAT TURNS THE RULE "
            "ROUND.** **आदिरिति वर्तमाने पुनरादिग्रहणं "
            "पूर्वपदाद्युदात्तार्थम्** — आदिः was already running "
            "from 6.2.111; saying it again can only be to move it "
            "off the second member and onto the first. The one "
            "rule in this whole run that accents the पूर्वपद"),
    Uttarapada(
        "6.2.126", where="ādi",
        of=("cela", "kheṭa", "kaṭuka", "kāṇḍa"), samasa="tatpuruṣa",
        result=("garhā",),
        keeps_out="परमचेलम् — no contempt meant",
        why="चेलखेटकटुककाण्डं गर्हायाम् — four second members are "
            "accented on their first syllable in a तत्पुरुष where "
            "CONTEMPT is meant: **पुत्रचेलम्, भार्याचेलम्, "
            "उपानत्खेटम्, नगरखेटम्, दधिकटुकम्, उदश्वित्कटुकम्, "
            "भूतकाण्डम्, प्रजाकाण्डम्**.\\n\\n"
            "**AND THE CONTEMPT IS CARRIED BY A COMPARISON.** "
            "**चेलादीनां सादृश्येन पुत्रादीनां गर्हा। तत्र पुत्रश् "
            "चेलम् इवेति विगृह्य व्याघ्रादेराकृतिगणत्वाद् उपमितं "
            "व्याघ्रादिभिः इति समासः** — a son who is a mere rag, "
            "compounded by 2.1.56, whose व्याघ्रादि is open-ended "
            "enough to admit चेल"),
    Uttarapada(
        "6.2.127", where="ādi", of=("cīra",), samasa="tatpuruṣa",
        result=("upamāna",),
        keeps_out="परमचीरम् — चीर is not the thing compared TO",
        why="चीरमुपमानम् — चीर is accented on its first syllable "
            "where it is what something is COMPARED TO: **वस्त्रं "
            "चीरम् इव वस्त्रचीरम्, पटचीरम्, कम्बलचीरम्** — cloth no "
            "better than a rag"),
    Uttarapada(
        "6.2.128", where="ādi", of=("palala", "sūpa", "śāka"),
        samasa="tatpuruṣa", result=("miśra",),
        keeps_out="परमपललम् — nothing mixed in",
        why="पललसूपशाकं मिश्रे — three second members naming food "
            "are accented on their first syllable where a MIXTURE "
            "is meant: **गुडपललम्, घृतपललम्, घृतसूपः, मूलकसूपः, "
            "घृतशाकम्, मुद्गशाकम्**. The compound is 2.1.35's — "
            "**गुडेन मिश्रं पललं गुडपललम्, भक्ष्येण मिश्रीकरणम् इति "
            "समासः**"),
    Uttarapada(
        "6.2.129", where="ādi",
        of=("kūla", "sūda", "sthala", "karṣa"), samasa="tatpuruṣa",
        result=("saṃjñā",),
        keeps_out="परमकूलम् — not a name",
        why="कूलसूदस्थलकर्षाः संज्ञायाम् — four second members are "
            "accented on their first syllable where the compound "
            "is a NAME: **दाक्षिकूलम्, माहकिकूलम्, देवसूदम्, "
            "भाजीसूदम्, दाण्डायनस्थली, माहकिस्थली, दाक्षिकर्षः** — "
            "and the vṛtti says of what: **ग्रामनामधेयान्येतानि**, "
            "these are the names of villages.\\n\\n"
            "**AND स्थल COVERS स्थली TOO.** **स्थलग्रहणे "
            "लिङ्गविशिष्टत्वात् स्थलीशब्दोऽपि गृह्यते** — naming a "
            "stem names its feminine, here made by ङीष् under "
            "4.1.42"),
    Uttarapada(
        "6.2.130", where="ādi", of=("rājya",), samasa="tatpuruṣa",
        excludes=("karmadhāraya",),
        keeps_out="परमराज्यम् — a कर्मधारय, which the sūtra shuts "
                  "out by name",
        why="अकर्मधारये राज्यम् — राज्य is accented on its first "
            "syllable in a तत्पुरुष that is NOT a कर्मधारय: "
            "**ब्राह्मणराज्यम्, क्षत्रियराज्यम्**.\\n\\n"
            "**AND THE अव्यय ACCENT BEATS IT BY BEING EARLIER.** "
            "**चेलराज्यादिस्वराद् अव्ययस्वरो भवति पूर्वविप्रतिषेधेन "
            "— कुचेलम्, कुराज्यम्** — where the first member is an "
            "indeclinable, 6.2.2 wins over both 6.2.126 and this "
            "rule, and it wins by being the EARLIER of the two"),
    Uttarapada(
        "6.2.131", where="ādi", gana="vargyādi", samasa="tatpuruṣa",
        excludes=("karmadhāraya",),
        keeps_out="परमवर्ग्यः — a कर्मधारय",
        why="वर्ग्यादयश्च — and the वर्ग्यादि words in a "
            "non-कर्मधारय तत्पुरुष: **वासुदेववर्ग्यः, "
            "वासुदेवपक्ष्यः, अर्जुनवर्ग्यः, अर्जुनपक्ष्यः** — of "
            "Vāsudeva's party, of Arjuna's side.\\n\\n"
            "**AND THE GAṆA IS NOT WHERE ONE WOULD LOOK FOR IT.** "
            "**वर्ग्यादयः प्रातिपदिकेषु न पठ्यन्ते। दिगादिषु तु वर्ग "
            "पूग गण पक्ष इत्येवमादयो ये पठिताः, त एव यत्प्रत्ययान्ता "
            "वर्ग्यादय इह प्रतिपत्तव्याः** — take दिगादि's members "
            "and put यत् on them, and that is this list"),
    Uttarapada(
        "6.2.132", where="ādi", of=("putra",),
        purvapada_gana=("puṃs",), samasa="tatpuruṣa",
        keeps_out="कौनटिमातुलः — not पुत्र; गार्गीपुत्रः, "
                  "वात्सीपुत्रः — the first member is a woman",
        why="पुत्रः पुम्भ्यः — पुत्र after a word for a MAN is "
            "accented on its first syllable in a तत्पुरुष: "
            "**कौनटिपुत्रः, दामकपुत्रः, माहिषकपुत्रः** — the son of "
            "Kaunaṭi, of Dāmaka. Named after the father the accent "
            "moves forward; named after the mother it does not"),
    Uttarapada(
        "6.2.133", refuses=True, of=("putra",),
        purvapada_gana=("ācārya-ādi-ākhyā",), samasa="tatpuruṣa",
        blocks=("6.2.132",),
        why="न आचार्यराजर्त्विक्संयुक्तज्ञात्याख्येभ्यः — but not "
            "after a word naming a teacher, a king, a priest, a "
            "wife's kinsman or a blood relation: "
            "**आचार्यपुत्रः, उपाध्यायपुत्रः, शाकटायनपुत्रः, "
            "राजपुत्रः, ईश्वरपुत्रः, ऋत्विक्पुत्रः, याजकपुत्रः, "
            "संयुक्तपुत्रः, श्यालपुत्रः, ज्ञातिपुत्रः**. The accent "
            "6.2.132 would have moved stays where 6.1.223 put it, "
            "at the end.\\n\\n"
            "**AND THE WORD आख्या OPENS THE FIVE OUT.** "
            "**आख्याग्रहणात् स्वरूपस्य पर्यायाणां विशेषाणां च "
            "ग्रहणं भवति** — the word itself, its synonyms, AND "
            "its species. So not आचार्य alone but उपाध्याय and "
            "शाकटायन too; not राजन् alone but ईश्वर and नन्द. Each "
            "of the five is glossed before use: **आचार्य "
            "उपाध्यायः। राजा ईश्वरः। ऋत्विजो याजकाः। संयुक्ताः "
            "स्त्रीसंबन्धिनः श्यालादयः। ज्ञातयो "
            "मातृपितृसंबन्धिनो बान्धवाः**"),
    Uttarapada(
        "6.2.134", where="ādi", gana="cūrṇādi",
        purvapada_gana=("aprāṇin",), case="ṣaṣṭhī",
        samasa="tatpuruṣa",
        keeps_out="मत्स्यचूर्णम् — a fish is alive; परमचूर्णम् — "
                  "not a genitive compound",
        why="चूर्णादीन्यप्राणिषष्ठ्याः — the चूर्णादि second "
            "members are accented on their first syllable after a "
            "genitive naming something NOT ALIVE: **मुद्गचूर्णम्, "
            "मसूरचूर्णम्** — flour of beans, flour of lentils. The "
            "vṛtti carries both headings down: **उत्तरपदादिरिति "
            "वर्तते, तत्पुरुष इति च**.\\n\\n"
            "**AND THE SŪTRA HAS A SECOND READING.** "
            "**चूर्णादीन्यप्राण्युपग्रहाद् इति सूत्रस्य "
            "पाठान्तरम्। तत्रोपग्रह इति षष्ठ्यन्तमेव "
            "पूर्वाचार्योपचारेण गृह्यते** — where it reads उपग्रह, "
            "उपग्रह is the older teachers' word for the genitive, "
            "and nothing changes"),
    Uttarapada(
        "6.2.135", where="ādi", of=THE_SIX,
        purvapada_gana=("aprāṇin",), case="ṣaṣṭhī",
        samasa="tatpuruṣa",
        keeps_out="राजसूदः — a king is alive, and सूद is not one "
                  "of the six",
        why="षट् च काण्डादीनि — and six words already accented "
            "earlier in this pāda are accented here too, now "
            "WITHOUT the sense-conditions those rules attached. "
            "The vṛtti walks them one by one: **काण्डं गर्हायाम् "
            "इत्युक्तम् अगर्हायामपि भवति — दर्भकाण्डम्, "
            "शरकाण्डम्; चीरम् उपमानम् इत्युक्तम् अनुपमानमपि भवति — "
            "दर्भचीरम्, कुशचीरम्; पललसूपशाकं मिश्रे इत्युक्तम् "
            "अमिश्रेऽपि भवति — तिलपललम्, मुद्गसूपः, मूलकशाकम्; "
            "कूलं संज्ञायाम् इत्युक्तम् असंज्ञायामपि भवति — "
            "नदीकूलम्, समुद्रकूलम्**. Four rules widened by one, "
            "at the price of a new condition: a non-living "
            "genitive in front"),
    Uttarapada(
        "6.2.136", where="ādi", of=("kuṇḍa",), samasa="tatpuruṣa",
        result=("vana",),
        keeps_out="मृत्कुण्डम् — a pot and not a thicket",
        why="कुण्डं वनम् — कुण्ड is accented on its first syllable "
            "where it names a THICKET: **दर्भकुण्डम्, "
            "शरकुण्डम्**. The vṛtti says how a pot came to mean a "
            "wood: **कुण्डशब्दोऽत्र कुण्डसादृश्येन वने वर्तते** — "
            "by the likeness of the shape. This is the last rule "
            "under आदिः; 6.2.137 replaces the word"),
    Uttarapada(
        "6.2.137", where="prakṛti", of=("bhagāla",),
        samasa="tatpuruṣa", heading=True,
        why="प्रकृत्या भगालम् — a second member meaning SKULL "
            "keeps its own accent in a तत्पुरुष: "
            "**कुम्भीभगालम्, कुम्भीकपालम्, कुम्भीनदालम्**, and the "
            "vṛtti says what that accent is — **भगालादयो "
            "मध्योदात्ताः**, accented in the middle, which is "
            "exactly what neither आदिः nor अन्तः could have "
            "given.\\n\\n"
            "**AND THE WORD प्रकृत्या STAYS ON AFTER THE RULE "
            "ENDS.** **प्रकृत्येत्येतदधिकृतम् अन्तः इति यावद् "
            "वेदितव्यम्** — through 6.2.142, six sūtras, until "
            "6.2.143 अन्तः displaces it. The shortest of the "
            "pāda's five headings, and the third placement-word to "
            "hold the second member"),
    Uttarapada(
        "6.2.138", where="prakṛti", purvapada=("śiti",),
        samasa="bahuvrīhi", excludes=("bhasat",),
        result=("nitya-abahvac",),
        keeps_out="दर्शनीयपादः — the first member is not शिति; "
                  "शितिललाटः — ललाट has many vowels; शितिभसत् — "
                  "the word the sūtra shuts out",
        why="शितेर्नित्याबह्वज्बहुव्रीहावभसत् — after शिति, a "
            "second member that ALWAYS has few vowels keeps its "
            "own accent in a बहुव्रीहि, भसत् excepted: "
            "**शितिपादः, शित्यंसः, शित्योष्ठः** — and the vṛtti "
            "says which accents are thereby kept: **पादशब्दो "
            "वृषादित्वादाद्युदात्तः। अंसौष्ठशब्दौ च "
            "प्रत्ययस्य नित्त्वात्**.\\n\\n"
            "**AND THE WORD नित्यम् IS THERE FOR ONE WORD.** "
            "**नित्यग्रहणं किम्? शितिककुत्** — ककुद् loses its द् "
            "by 5.4.146, so ककुत् is short-voweled SOMETIMES and "
            "not always. नित्यम् shuts out exactly that: a word "
            "that has to lose something first does not count"),
    Uttarapada(
        "6.2.139", where="prakṛti", affix=("kṛt",),
        purvapada_gana=("gati", "kāraka", "upapada"),
        samasa="tatpuruṣa", excludes=("bahuvrīhi",),
        keeps_out="देवदत्तकारकः — the genitive is none of the "
                  "three, being **शेषलक्षणा षष्ठी**",
        why="गतिकारकोपपदात् कृत् — a कृत्-formed second member "
            "keeps its own accent after a गति, a कारक or an "
            "उपपद: **प्रकारकः, प्रकरणम्, प्रहारकः, प्रहरणम्; "
            "इध्मप्रव्रश्चनः, पलाशशातनः, श्मश्रुकल्पनः; इषत्करः, "
            "दुष्करः, सुकरः** — and the vṛtti names the accent "
            "kept: **सर्वत्रैवात्र लित्स्वरः**, the one 6.1.193 "
            "gives a लित् affix.\\n\\n"
            "**AND THE WORD कृत् IS THERE ONLY TO BE CLEAR.** "
            "**कृद्ग्रहणं विस्पष्टार्थम्** — with a note on what "
            "it does not reach: **प्रपचतितराम्, प्रपचतितमाम् "
            "इत्यत्र तरबाद्यन्तेन समासः**, where the second member "
            "ends in तरप् and is no कृदन्त. This is the rule the "
            "commentaries call उत्तरपदप्रकृतिस्वर, and 6.2.144 is "
            "built to override it"),
    Uttarapada(
        "6.2.140", where="ubhe-prakṛti", gana="vanaspatyādi",
        why="उभे वनस्पत्यादिषु युगपत् — in the वनस्पत्यादि "
            "compounds BOTH members keep their own accents AT "
            "ONCE: **वनस्पतिः, बृहस्पतिः, शचीपतिः**. Two उदात्तs "
            "in one word, where every other rule of the pāda "
            "leaves exactly one.\\n\\n"
            "**AND THE VṚTTI ACCOUNTS FOR EACH ACCENT SEPARATELY.** "
            "**वनपतिशब्दावाद्युदात्तौ पारस्करप्रभृतित्वात् सुट्** — "
            "6.1.157's list supplies the स् and both words are "
            "ādi-accented; **तद्बृहतोः करपत्योश्चोरदेवतयोः सुट् "
            "तलोपश्च इति सुट् तकारलोपश्च** for बृहस्पति; and for "
            "शचीपति, **शचीशब्दः कृदिकारादक्तिनः इति ङीषन्तत्वाद् "
            "अन्तोदात्तः**. Three words, three different reasons"),
    Uttarapada(
        "6.2.141", where="ubhe-prakṛti", samasa="devatā-dvandva",
        keeps_out="प्लक्षन्यग्रोधौ — no gods; अग्निष्टोमः — no "
                  "द्वन्द्व",
        why="देवताद्वन्द्वे च — and in a द्वन्द्व of GODS both "
            "members keep their accents at once: **इन्द्रासोमौ, "
            "इन्द्रावरुणौ, इन्द्राबृहस्पती**.\\n\\n"
            "**AND THE THIRD OF THOSE CARRIES THREE उदात्तs.** "
            "**बृहस्पतिशब्दे वनस्पत्यादित्वाद् द्वावुदात्तौ, "
            "तेनेन्द्राबृहस्पती इत्यत्र त्रय उदात्ता भवन्ति** — "
            "6.2.140 has already given बृहस्पति two, and इन्द्र "
            "brings a third. Nowhere else in the Aṣṭādhyāyī does "
            "one word end with three"),
    Uttarapada(
        "6.2.142", refuses=True, samasa="devatā-dvandva",
        result=("anudāttādi",), excludes=DEVATA_EXCEPTIONS,
        blocks=("6.2.141",),
        why="न उत्तरपदेऽनुदात्तादावपृथिवीरुद्रपूषमन्थिषु — but not "
            "where the SECOND word begins अनुदात्त, unless it is "
            "पृथिवी, रुद्र, पूषन् or मन्थिन्: **इन्द्राग्नी, "
            "इन्द्रवायू** — **अग्निवायुशब्दावन्तोदात्तौ**, so they "
            "begin low and 6.2.141 is refused. The four exceptions "
            "keep it: **द्यावापृथिव्यौ, सोमारुद्रौ**.\\n\\n"
            "**AND THE WORD उत्तरपदे IS THERE TO SAY WHOSE FIRST "
            "SYLLABLE IS MEANT.** **उत्तरपदग्रहणम् अनुदात्तादाव् "
            "इत्युत्तरपदविशेषणं यथा स्याद्, द्वन्द्वविशेषणं मा "
            "भूदिति** — अनुदात्तादि qualifies the second member, "
            "not the compound. And the condition is stated at all "
            "**विधिप्रतिषेधयोर्विषयविभागार्थम्**, to divide the "
            "ground cleanly between 6.2.141 and this refusal"),
    Uttarapada(
        "6.2.143", where="anta", heading=True,
        why="अन्तः — **अन्त इत्यधिकारः। यदित "
            "ऊर्ध्वमनुक्रमिष्यामस्तत्र समासस्योत्तरपदस्यान्त "
            "उदात्तो भवतीत्येवं तद् वेदितव्यम्** — from here to "
            "the end of the pāda the accent goes on the second "
            "member's LAST syllable. The vṛtti reads the next "
            "sūtra out as its example: **वक्ष्यति "
            "थाथघञ्क्ताजबित्रकाणाम् इति — सुनीथः, अवभृथः**.\\n\\n"
            "The longest of the three runs: fifty-seven sūtras, "
            "6.2.143 to 6.2.199, and the pāda has nothing else "
            "after it"),
    Uttarapada(
        "6.2.144", where="anta",
        affix=("tha", "atha", "ghañ", "kta", "ac", "ap", "itra",
               "ka"),
        purvapada_gana=("gati", "kāraka", "upapada"),
        blocks=("6.2.139",),
        why="थाथघञ्क्ताजबित्रकाणाम् — a second member ending in "
            "any of eight affixes takes the accent on its LAST "
            "syllable after a गति, a कारक or an उपपद: **सुनीथः, "
            "अवभृथः** (थ), **आवसथः, उपवसथः** (अथ), **प्रभेदः, "
            "काष्ठभेदः, रज्जुभेदः** (घञ्), **दूरादागतः, विशुष्कः** "
            "(क्त).\\n\\n"
            "**AND IT EXISTS ONLY TO UNDO 6.2.139.** **तत्र "
            "कृदुत्तरपदप्रकृतिस्वरत्वेनाद्युदात्तम् उत्तरपदं "
            "स्यात्** — without this rule the कृदन्त would keep "
            "its own accent under 6.2.139 five sūtras back, and "
            "for these eight affixes that accent is at the front. "
            "6.2.144 moves it to the end"),
    Uttarapada(
        "6.2.145", where="anta", affix=("kta",), purvapada=("su",),
        purvapada_gana=("upamāna",), blocks=("6.2.48", "6.2.49"),
        keeps_out="सुस्तुतं भवता — not a compound at all, so "
                  "गतिकारकोपपदात् is not satisfied",
        why="सूपमानात् क्तः — a क्त-formed second member takes the "
            "accent on its last syllable after सु or after what "
            "something is COMPARED TO: **सुकृतम्, सुभुक्तम्, "
            "सुपीतम्; वृकावलुप्तम्, शशप्लुतम्, सिंहविनर्दितम्** — "
            "torn as a wolf tears, leaping as a hare leaps.\\n\\n"
            "**AND EACH HALF OVERRIDES A DIFFERENT EARLIER "
            "RULE.** **सुशब्दाद् गतिरनन्तरः इति प्राप्त उपमानादपि "
            "तृतीया कर्मणि इत्ययमपवादः** — after सु it displaces "
            "6.2.49, after a comparison 6.2.48. One sūtra, two "
            "अपवादs"),
    Uttarapada(
        "6.2.146", where="anta", affix=("kta",),
        purvapada_gana=("gati", "kāraka", "upapada"),
        result=("saṃjñā",), excludes=("ācitādi",),
        blocks=("6.2.48", "6.2.49"),
        keeps_out="आचितम्, पर्याचितम्, आस्थापितम्, परिगृहीतम्, "
                  "निरुक्तम् — the आचितादि words",
        why="संज्ञायामनाचितादीनाम् — a क्त-formed second member "
            "takes the accent on its last syllable where the "
            "compound is a NAME, the आचितादि words excepted: "
            "**संभूतो रामायणः, उपहूतः शाकल्यः, परिजग्धः "
            "कौण्डिन्यः; धनुष्खाता नदी, कुद्दालखातं नगरम्, "
            "हस्तिमृदिता भूमिः** — men and rivers and towns "
            "called by what was done to them.\\n\\n"
            "**AND IT DISPLACES TWO RULES AT ONCE, EACH FOR ITS "
            "OWN HALF.** **गतिरनन्तरः इत्यत्र हि कर्मणीत्यनुवर्तते, "
            "तद्बाधनार्थं चेदम्** for the first three; **तृतीया "
            "कर्मणि इति प्राप्तिरिह बाध्यते** for the last three"),
    Uttarapada(
        "6.2.147", where="anta", gana="pravṛddhādi",
        why="प्रवृद्धादीनां च — and the प्रवृद्धादि words, all of "
            "them क्त-formed, take the accent on their last "
            "syllable: **प्रवृद्धं यानम्, प्रवृद्धो वृषलः, "
            "प्रयुक्ताः सक्तवः, अवहितो भोगेषु, खट्वारूढः, "
            "कविशस्तः**.\\n\\n"
            "**AND THE VṚTTI LEAVES A DISPUTE STANDING.** The "
            "gaṇa lists each word beside a noun — यान for "
            "प्रवृद्ध, and so on. Are those nouns binding? "
            "**यानादीनामत्र गणे पाठः प्रायोवृत्तिप्रदर्शनार्थः, न "
            "विषयनियमार्थः... विषयनियमार्थ एवेत्येके** — most say "
            "they only show the usual case, some say they fix it, "
            "and the vṛtti reports both without choosing. It adds "
            "two things it is sure of: **असंज्ञार्थोऽयमारम्भः** — "
            "this rule is for where 6.2.146 does not reach, the "
            "compound not being a name — and **आकृतिगणश्च "
            "प्रवृद्धादिर्द्रष्टव्यः**, the list is open"),
    Uttarapada(
        "6.2.148", where="anta", of=("datta", "śruta"),
        purvapada_gana=("kāraka",), result=("āśis",),
        blocks=("6.2.146",),
        keeps_out="देवपालितः — पालित is neither दत्त nor श्रुत, so "
                  "6.2.48 stands",
        why="कारकाद् दत्तश्रुतयोरेवाशिषि — where a NAME carries a "
            "BLESSING, only दत्त and श्रुत take the accent on "
            "their last syllable, and only after a कारक: **देवा "
            "एनं देयासुर् देवदत्तः; विष्णुर् एनं श्रुयाद् "
            "विष्णुश्रुतः** — may the gods grant him, may Viṣṇu "
            "hear him.\\n\\n"
            "**AND THE WORD एव MAKES THE RULE A RESTRICTION AND "
            "NOT A GRANT.** **एतस्माद् नियमाद् अत्र "
            "संज्ञायामनाचितादीनाम् इत्यन्तोदात्तत्वं न भवति** — in "
            "a blessing-name, 6.2.146's wider grant is shut off "
            "and 6.2.48 takes what is left. And the vṛtti asks "
            "which of the two words एव restricts: **एवकारकरणं "
            "किम्? कारकावधारणं यथा स्याद्, दत्तश्रुतावधारणं मा "
            "भूत्** — it restricts the source, not the pair"),
    Uttarapada(
        "6.2.149", where="anta", affix=("kta",),
        result=("itthaṃbhūtena-kṛta",), blocks=("6.2.48",),
        why="इत्थंभूतेन कृतम् इति च — where the compound means "
            "DONE BY ONE IN SUCH A STATE, the क्त-formed second "
            "member takes the accent on its last syllable: "
            "**सुप्तप्रलपितम्, उन्मत्तप्रलपितम्, प्रमत्तगीतम्, "
            "विपन्नश्रुतम्** — babbled by a sleeper, sung by a "
            "drunk man. **इमं प्रकारम् आपन्न इत्थंभूतः**.\\n\\n"
            "**AND कृतम् IS TAKEN AS WIDELY AS POSSIBLE.** "
            "**कृतमिति क्रियासामान्ये करोतिर्वर्तते, नाभूतप्रादुर्भाव "
            "एव। तेन प्रलपिताद्यपि कृतं भवति** — done, in the sense "
            "of any action at all and not only of bringing "
            "something into being; otherwise babbling would not "
            "count as done. And the vṛtti notes where the rule is "
            "not needed: **भावे तु यदा प्रलपितादयस्तदा "
            "थाथादिस्वरेणैव सिद्धम्** — read as abstract nouns "
            "they are already end-accented by 6.2.144"),
    Uttarapada(
        "6.2.150", where="anta", affix=("ana",),
        purvapada_gana=("kāraka",), result=("bhāva", "karman"),
        keeps_out="हस्तहार्यमुदश्वित् — not an अन-ending word",
        why="अनो भावकर्मवचनः — a second member ending in अन takes "
            "the accent on its last syllable after a कारक, where "
            "it names the ACTION or the OBJECT: **ओदनभोजनं सुखम्, "
            "पयःपानं सुखम्, चन्दनप्रियङ्गुकालेपनं सुखम्** for the "
            "action; **राजभोजनाः शालयः, राजाच्छादनानि वासांसि** "
            "for the object — rice for a king to eat, cloth for a "
            "king to wear.\\n\\n"
            "**AND THE TWO SENSES COME FROM TWO READINGS OF ONE "
            "EARLIER SŪTRA.** **कर्मणि च येन संस्पर्शात् कर्तुः "
            "शरीरसुखम् इत्ययं योग उभयथा वर्ण्यते — कर्मण्युपपदे भावे "
            "ल्युड् भवति, कर्मण्यभिधेये ल्युड् भवतीति** — 3.3.116 "
            "is read two ways, and each reading supplies one half "
            "of this rule's examples"),
    Uttarapada(
        "6.2.151", where="anta", affix=("man", "ktin"),
        of=("vyākhyāna", "śayana", "āsana", "sthāna", "krīta"),
        gana="yājakādi",
        why="मन्क्तिन्व्याख्यानशयनासनस्थानयाजकादिक्रीताः — six "
            "kinds of second member take the accent on their last "
            "syllable: **रथवर्त्म, शकटवर्त्म** (मन्), "
            "**पाणिनिकृतिः, आपिशलिकृतिः** (क्तिन्), "
            "**ऋगयनव्याख्यानम्, छन्दोव्याख्यानम्**, "
            "**राजशयनम्, ब्राह्मणशयनम्**, **राजासनम्, "
            "ब्राह्मणासनम्**, **गोस्थानम्, अश्वस्थानम्**, and the "
            "याजकादि words — **ब्राह्मणयाजकः, क्षत्रिययाजकः, "
            "ब्राह्मणपूजकः, क्षत्रियपूजकः**"),
    Uttarapada(
        "6.2.152", where="anta", of=("puṇya",), case="saptamī",
        blocks=("6.2.2",),
        keeps_out="वेदेन पुण्यं वेदपुण्यम् — an instrumental "
                  "compound, where 6.2.2 stands",
        why="सप्तम्याः पुण्यम् — पुण्य after a LOCATIVE first "
            "member takes the accent on its last syllable: "
            "**अध्ययने पुण्यम् अध्ययनपुण्यम्, वेदे पुण्यं "
            "वेदपुण्यम्** — merit in study, merit in the Veda. "
            "The compound comes from splitting 2.1.40 in two: "
            "**सप्तमी इति योगविभागात् समासः**.\\n\\n"
            "**AND WITHOUT IT THE FIRST MEMBER WOULD HAVE KEPT "
            "THE ACCENT.** **तत्पुरुषे तुल्यार्थ० इति "
            "पूर्वपदप्रकृतिस्वरत्वं प्राप्तम् इत्यन्तोदात्तत्वं "
            "विधीयते** — 6.2.2 would have reached it. The vṛtti "
            "adds a caveat about the other party's derivation: "
            "**उणादीनां तु व्युत्पत्तिपक्षे कृत्स्वरेणाद्युदात्तः "
            "पुण्यशब्दः स्यात्**"),
    Uttarapada(
        "6.2.153", where="anta", of=("kalaha",), gana="ūnārtha",
        case="tṛtīyā", blocks=("6.2.48",),
        why="ऊनार्थकलहं तृतीयायाः — words meaning SHORT BY, and "
            "the word कलह, take the accent on their last syllable "
            "after an instrumental: **माषोनम्, कार्षापणोनम्, "
            "माषविकलम्, कार्षापणविकलम्; असिकलहः, वाक्कलहः** — "
            "short by a bean, short by a coin; a quarrel with "
            "swords, a quarrel with words. **तृतीयापूर्वपदप्रकृति"
            "स्वरापवादो योगः**.\\n\\n"
            "**AND ONE PARTY WOULD READ अर्थ AS A WORD AND NOT AS "
            "A SENSE.** **अत्र केचिदर्थ इति स्वरूपग्रहणम् "
            "इच्छन्ति — धान्येनार्थो धान्यार्थः** — they would "
            "have the sūtra reach the word अर्थ itself. The vṛtti "
            "answers that ऊन already carries the sense-reading, "
            "and that तृतीया is then merely **विस्पष्टार्थम्**"),
    Uttarapada(
        "6.2.154", where="anta", of=("miśra",), case="tṛtīyā",
        result=("asandhi",), excludes=("sopasarga",),
        keeps_out="गुडधानाः — not मिश्र; गुडसंमिश्राः — an "
                  "उपसर्ग in front; ब्राह्मणमिश्रो राजा — an "
                  "alliance, which is the सन्धि the rule excludes",
        why="मिश्रं च अनुपसर्गम् असंधौ — मिश्र takes the accent "
            "on its last syllable after an instrumental, with no "
            "उपसर्ग on it and no ALLIANCE meant: **गुडमिश्राः, "
            "तिलमिश्राः, सर्पिर्मिश्राः**. The vṛtti glosses the "
            "excluded sense: **संधिरिति हि पणबन्धेनैकार्थ्यम् "
            "उच्यते**, a common purpose struck by agreement.\\n\\n"
            "**AND SAYING अनुपसर्गम् HERE TEACHES SOMETHING "
            "ELSEWHERE.** **इहानुपसर्गग्रहणं ज्ञापकम् अन्यत्र "
            "मिश्रग्रहणे सोपसर्गग्रहणस्य। तेन मिश्रश्लक्ष्णैः इति "
            "सोपसर्गेणापि मिश्रशब्देन तृतीयासमासो भवति** — the "
            "need to exclude an उपसर्ग here shows that where "
            "2.1.31 names मिश्र it does not exclude one"),
    Uttarapada(
        "6.2.155", where="anta", purvapada=("nañ",),
        affix=("taddhita",), result=("guṇapratiṣedha",),
        keeps_out="विगार्दभरथिकः — the first member is not नञ्; "
                  "गार्दभरथिकः uncompounded — no denial of a "
                  "quality",
        why="नञो गुणप्रतिषेधे संपाद्यर्हहितालमर्थास्तद्धिताः — "
            "after नञ् used to DENY A QUALITY, a taddhita-formed "
            "second member meaning fit for, deserving, good for, "
            "or equal to takes the accent on its last syllable: "
            "**अकार्णवेष्टकिकम्** (not fit to be made into "
            "earrings), **अच्छैदिकः** (not deserving to be cut), "
            "**अवत्सीयः** (not good for calves), **असांतापिकः** "
            "(not equal to causing pain). Each is glossed in "
            "full: **कर्णवेष्टकाभ्यां संपादि मुखं कार्णवेष्टकिकम्, "
            "न कार्णवेष्टकिकम्**"),
    Uttarapada(
        "6.2.156", where="anta", purvapada=("nañ",),
        affix=("ya", "yat"), result=("atadartha",),
        keeps_out="अपाद्यम् — पाद्यम् is water FOR the feet, so "
                  "the sense is तदर्थ; अदेयम् — देय is no "
                  "taddhita; अदन्त्यम् meaning merely other than "
                  "दन्त्य — no denial of a quality",
        why="ययतोश्च अतदर्थे — and taddhita य or यत् in the same "
            "position, where the sense is NOT for-that-purpose: "
            "**पाशानां समूहः पाश्या, न पाश्या अपाश्या; अतृण्या**; "
            "**दन्तेषु भवं दन्त्यम्, न दन्त्यम् अदन्त्यम्; "
            "अकर्ण्यम्**.\\n\\n"
            "**AND ONLY THE BARE AFFIXES ARE MEANT.** "
            "**निरनुबन्धकैकानुबन्धकयोर् ययतोर्ग्रहणाद् इह न भवति** "
            "— य with no it-marker and यत् with one; an affix "
            "carrying two markers is not named by either"),
    Uttarapada(
        "6.2.157", where="anta", purvapada=("nañ",),
        affix=("ac", "ka"), result=("aśakti",),
        keeps_out="अपचो दीक्षितः, अपचः परिव्राजकः — one who does "
                  "not cook by vow or by rule, and not from "
                  "inability",
        why="अच्कावशक्तौ — after नञ्, a second member ending in "
            "अच् or क takes the accent on its last syllable where "
            "INABILITY is meant: **अपचो यः पक्तुं न शक्नोति; "
            "अजयः; अविक्षिपः, अविलिखः** — one who cannot cook, "
            "cannot win, cannot throw"),
    Uttarapada(
        "6.2.158", where="anta", purvapada=("nañ",),
        affix=("ac", "ka"), result=("ākrośa",),
        why="आक्रोशे च — and where ABUSE is meant: **अपचोऽयं "
            "जाल्मः, अपठोऽयं जाल्मः; अविक्षिपः, अविलिखः**. The "
            "vṛtti marks the difference from the sūtra before: "
            "**पक्तुं पठितुं शक्तोऽप्येवमाक्रुश्यते** — he CAN "
            "cook, he CAN recite, and is called this anyway"),
    Uttarapada(
        "6.2.159", where="anta", purvapada=("nañ",),
        result=("saṃjñā",),
        why="संज्ञायाम् — and where the नञ्-compound is a NAME, "
            "still in the sense of abuse: **अदेवदत्तः, "
            "अयज्ञदत्तः, अविष्णुमित्रः** — a no-Devadatta, a "
            "worthless Devadatta. Here no affix is named at all: "
            "any second member will do"),
    Uttarapada(
        "6.2.160", where="anta", purvapada=("nañ",),
        affix=("kṛtya", "uka", "iṣṇuc"), gana="cārvādi",
        why="कृत्युकेष्णुच्चार्वादयश्च — three affixes and a gaṇa, "
            "all after नञ्: **अकर्तव्यम्, अकरणीयम्** (कृत्य), "
            "**अनागामुकम्, अनपलाषुकम्** (उक), "
            "**अनलंकरिष्णुः, अनिराकरिष्णुः** (इष्णुच्), and "
            "**अचारुः, असाधुः, अयौधिकः, अवदान्यः** — **चारु। "
            "साधु। यौधिक। वदान्य**.\\n\\n"
            "**AND NAMING इष्णुच् REACHES A SECOND AFFIX IT DOES "
            "NOT NAME.** **इष्णुज्ग्रहणे कर्तरि भुवः खिष्णुच् "
            "इत्यस्य द्व्यनुबन्धकस्यापि ग्रहणम् इकारादेर् "
            "विधानसामर्थ्याद् भवति** — खिष्णुच् carries two "
            "markers and so is not named; but since इष्णुच् is "
            "prescribed with an initial इ, the shape reaches it "
            "anyway: **अनाढ्यंभविष्णुः, असुभगंभविष्णुः**"),
    Uttarapada(
        "6.2.161", where="anta", purvapada=("nañ",),
        of=("anna", "tīkṣṇa", "śuci"), affix=("tṛn",),
        optional=True,
        why="विभाषा तृन्नन्नतीक्ष्णशुचिषु — after नञ्, a "
            "तृन्-formed second member and three named words are "
            "OPTIONALLY end-accented: **अकर्ता / अकर्ता, अनन्नम् "
            "/ अनन्नम्, अतीक्ष्णम् / अतीक्ष्णम्, अशुचिः / "
            "अशुचिः**. And the vṛtti says what the other option "
            "is: **पक्षेऽव्ययस्वर एव भवति** — 6.2.2's accent for "
            "an indeclinable first member, नञ् being one"),
    Uttarapada(
        "6.2.162", where="anta", purvapada=("idam", "etad", "tad"),
        of=("prathama",), affix=("pūraṇa",), samasa="bahuvrīhi",
        result=("kriyāgaṇana",),
        keeps_out="अनेन प्रथम इदंप्रथमः — not a बहुव्रीहि; "
                  "यत्प्रथमः — the first member is none of the "
                  "three",
        why="बहुव्रीहाविदमेतत्तद्भ्यः प्रथमपूरणयोः क्रियागणने — "
            "after इदम्, एतद् or तद्, the word प्रथम or an "
            "ordinal takes the accent on its last syllable in a "
            "बहुव्रीहि COUNTING AN ACT: **इदं प्रथमं गमनं भोजनं "
            "वा यस्य स इदंप्रथमः; इदंद्वितीयः, इदंतृतीयः, "
            "एतत्प्रथमः, तत्प्रथमः, तत्तृतीयः** — one for whom "
            "this is a first going or a first eating"),
    Uttarapada(
        "6.2.163", where="anta", of=("stana",),
        purvapada_gana=("saṅkhyā",), samasa="bahuvrīhi",
        keeps_out="दर्शनीयस्तना — no numeral; द्विशिराः — not "
                  "स्तन",
        why="संख्यायाः स्तनः — स्तन after a NUMERAL takes the "
            "accent on its last syllable in a बहुव्रीहि: "
            "**द्विस्तना, त्रिस्तना, चतुःस्तना**"),
    Uttarapada(
        "6.2.164", where="anta", of=("stana",),
        purvapada_gana=("saṅkhyā",), samasa="bahuvrīhi",
        chandasi=True, optional=True,
        why="विभाषा — and in the Veda the same accent is "
            "OPTIONAL: **द्विस्तनां कुर्याद् वामदेवः** beside "
            "**द्विस्तनां करोति द्यावापृथिव्योर् दोहाय चतुःस्तनां "
            "करोति पशूनां दोहाय**. The same words, accented both "
            "ways in the same passage"),
    Uttarapada(
        "6.2.165", where="anta", of=("mitra", "ajina"),
        result=("saṃjñā",), samasa="bahuvrīhi",
        excludes=("ṛṣi",),
        keeps_out="प्रियमित्रः, महाजिनः — not a name; "
                  "विश्वामित्र ऋषिः — the vārttika "
                  "**ऋषिप्रतिषेधो मित्रे**",
        why="संज्ञायां मित्राजिनयोः — मित्र and अजिन take the "
            "accent on their last syllable in a बहुव्रीहि that is "
            "a NAME: **देवमित्रः, ब्रह्ममित्रः; वृकाजिनः, "
            "कूलाजिनः, कृष्णाजिनः**.\\n\\n"
            "**AND A VĀRTTIKA TAKES THE ṚṢIS BACK OUT.** "
            "**ऋषिप्रतिषेधो मित्रे — विश्वामित्र ऋषिः** — a seer's "
            "name in मित्र is not end-accented, however much of a "
            "name it is"),
    Uttarapada(
        "6.2.166", where="anta", of=("antara",),
        purvapada_gana=("vyavāyin",), samasa="bahuvrīhi",
        keeps_out="आत्मान्तरः — **आत्मा स्वभावोऽन्तरोऽन्यो "
                  "यस्य**, where अन्तर means other and nothing "
                  "stands between",
        why="व्यवायिनोऽन्तरम् — अन्तर takes the accent on its "
            "last syllable in a बहुव्रीहि after a word naming "
            "what COMES BETWEEN: **वस्त्रान्तरः, पटान्तरः, "
            "कम्बलान्तरः** — **वस्त्रम् अन्तरं व्यवधायकं यस्य स "
            "वस्त्रान्तरः**, one with a cloth in between. "
            "**व्यवायी व्यवधाता**"),
    Uttarapada(
        "6.2.167", where="anta", of=("mukha",), result=("svāṅga",),
        samasa="bahuvrīhi",
        keeps_out="दीर्घमुखा शाला — a hall has no body, so मुख is "
                  "no limb of it",
        why="मुखं स्वाङ्गम् — मुख takes the accent on its last "
            "syllable in a बहुव्रीहि where it names a PART OF THE "
            "BODY: **गौरमुखः, भद्रमुखः**. And स्वाङ्ग is not "
            "loose here: **स्वाङ्गम् अद्रवादिलक्षणम् इह गृह्यते** "
            "— the technical sense 1.1.54's vārttika fixes"),
    Uttarapada(
        "6.2.168", refuses=True, of=("mukha",),
        purvapada=("avyaya", "diś", "go", "mahat", "sthūla",
                   "muṣṭi", "pṛthu", "vatsa"),
        samasa="bahuvrīhi", blocks=("6.2.167",),
        why="न अव्ययदिक्शब्दगोमहत्स्थूलमुष्टिपृथुवत्सेभ्यः — but "
            "not after eight kinds of first member: "
            "**उच्चैर्मुखः, नीचैर्मुखः** (indeclinable), "
            "**प्राङ्मुखः, प्रत्यङ्मुखः** (direction), "
            "**गोमुखः, महामुखः, स्थूलमुखः, मुष्टिमुखः, "
            "पृथुमुखः, वत्समुखः**. **पूर्वपदप्रकृतिस्वरो "
            "यथायोगमेषु भवति** — each falls back to whichever "
            "rule of 6.2.1–63 keeps the first member's accent.\\n\\n"
            "**AND THE REFUSAL ALSO KILLS AN OPTION.** "
            "**गोमुष्टिवत्सपूर्वस्योपमानलक्षणो विकल्पः "
            "पूर्वविप्रतिषेधेन बाध्यते** — गो, मुष्टि and वत्स "
            "could be read as comparisons and so fall under "
            "6.2.169's option; being named here, they do not"),
    Uttarapada(
        "6.2.169", where="anta", of=("mukha",),
        purvapada_gana=("niṣṭhā", "upamāna"), samasa="bahuvrīhi",
        optional=True,
        why="निष्ठोपमानादन्यतरस्याम् — after a निष्ठा or a "
            "comparison, मुख as a part of the body is OPTIONALLY "
            "end-accented: **सिंहमुखः / सिंहमुखः, व्याघ्रमुखः / "
            "व्याघ्रमुखः**.\\n\\n"
            "**AND THE OPTION MAKES THREE ACCENTUATIONS, NOT "
            "TWO.** **प्रक्षालितमुखः, प्रक्षालितमुखः, "
            "प्रक्षालितमुखः** — this rule's end-accent; failing "
            "that, 6.2.110's option putting the accent at the end "
            "of the FIRST member; and failing that too, the first "
            "member simply keeping what it had. One word, three "
            "readings, from two options meeting"),
    Uttarapada(
        "6.2.170", where="anta", affix=("kta",),
        purvapada_gana=("jāti", "kāla", "sukhādi"),
        excludes=("ācchādana", "kṛta", "mita", "pratipanna"),
        samasa="bahuvrīhi",
        keeps_out="पुत्रजातः — पुत्र names no class, and the "
                  "order is reversed **आहिताग्न्यादित्वात्**; "
                  "वस्त्रच्छन्नः, वसनच्छन्नः — clothing",
        why="जातिकालसुखादिभ्योऽनाच्छादनात् क्तोऽकृतमितप्रतिपन्नाः "
            "— a क्त-formed second member takes the accent on its "
            "last syllable in a बहुव्रीहि after a word for a "
            "CLASS (not of clothing), for a TIME, or one of the "
            "सुखादि: **सारङ्गजग्धः, पलाण्डुभक्षितः, सुरापीतः; "
            "मासजातः, संवत्सरजातः, द्व्यहजातः, त्र्यहजातः; "
            "सुखजातः, दुःखजातः, तृप्रजातः** — one who has eaten "
            "venison, one born a month ago. कृत, मित and "
            "प्रतिपन्न are shut out by name"),
    Uttarapada(
        "6.2.171", where="anta", of=("jāta",),
        purvapada_gana=("jāti", "kāla", "sukhādi"),
        samasa="bahuvrīhi", optional=True,
        why="वा जाते — and with जात the accent is OPTIONAL, "
            "after the same three kinds of first member: "
            "**दन्तजातः / दन्तजातः, स्तनजातः / स्तनजातः; "
            "मासजातः / मासजातः, संवत्सरजातः / संवत्सरजातः; "
            "सुखजातः / सुखजातः, दुःखजातः / दुःखजातः** — one whose "
            "teeth have come in, one born a month ago, one who "
            "has grown happy"),
    Uttarapada(
        "6.2.172", where="anta", purvapada=("nañ", "su"),
        samasa="bahuvrīhi",
        why="नञ्सुभ्याम् — after नञ् or सु, the second member of "
            "a बहुव्रीहि takes the accent on its last syllable, "
            "whatever it is: **अयवो देशः, अव्रीहिः, अमाषः; "
            "सुयवः, सुव्रीहिः, सुमाषः** — a land with no barley, "
            "a land with good barley.\\n\\n"
            "**AND THE ACCENT IS THE COMPOUND'S END, NOT THE "
            "STEM'S.** **समासस्यैतद् अन्तोदात्तत्वम् इष्यते। "
            "समासान्ताश्चावयवा भवन्ति इति अनृचो बह्वृच इत्यत्र "
            "कृते समासान्तेऽन्तोदात्तत्वं भवति** — where a "
            "समासान्त has been added, the accent falls at the end "
            "of THAT. This is the rule 6.2.116, 6.2.117 and "
            "6.2.119 are each carved out of"),
    Uttarapada(
        "6.2.173", where="pūrva-anta", purvapada=("nañ", "su"),
        affix=("kap",), samasa="bahuvrīhi",
        blocks=("6.2.117", "6.2.172"),
        why="कपि पूर्वम् — but before कप्, it is what stands "
            "BEFORE the कप् that is end-accented, not the "
            "compound: **अकुमारीको देशः, अवृषलीकः, "
            "अब्रह्मबन्धूकः; सुकुमारीकः, सुवृषलीकः, "
            "सुब्रह्मबन्धूकः**. The accent sits on the last "
            "syllable of the part preceding the affix, and the "
            "affix itself is left low.\\n\\n"
            "**AND IT BEATS 6.2.117 SIMPLY BY COMING LATER.** "
            "**कपि तु परत्वात् कपि पूर्वम् इत्येतद् भवति** — "
            "सुकर्मा is ādi-accented by 6.2.117, but add कप् and "
            "this rule takes it"),
    Uttarapada(
        "6.2.174", where="antyāt-pūrva", purvapada=("nañ", "su"),
        affix=("kap",), result=("hrasvānta",), samasa="bahuvrīhi",
        blocks=("6.2.173",),
        keeps_out="अज्ञकः, सुज्ञकः — the part before कप् does not "
                  "end in a short vowel, so 6.2.173 stands",
        why="ह्रस्वान्तेऽन्त्यात् पूर्वम् — and where what "
            "precedes the कप् ends in a SHORT vowel, the accent "
            "moves back one more: not the last syllable but the "
            "one before it. **अयवको देशः, अव्रीहिकः, अमाषकः; "
            "सुयवकः, सुव्रीहिकः, सुमाषकः**.\\n\\n"
            "**AND THE REPEATED WORD पूर्वम् MAKES IT A "
            "RESTRICTION.** **पूर्वमिति वर्तमाने पुनःपूर्वग्रहणं "
            "प्रवृत्तिभेदेन नियमप्रतिपत्त्यर्थम् — ह्रस्वान्तेऽन्त्याद् "
            "एव पूर्वम् उदात्तं भवति, न कपि पूर्वम् इति** — पूर्वम् "
            "was already running from 6.2.173; saying it again "
            "shuts 6.2.173 out entirely wherever this rule "
            "applies. **तेन अज्ञकः सुज्ञक इत्यत्र कबन्तस्यैव "
            "अन्तोदात्तत्वं भवति**"),
    Uttarapada(
        "6.2.175", where="nañvat", purvapada=("bahu",),
        result=("uttarapada-bhūman",),
        why="बहोर्नञ्वद् उत्तरपदभूम्नि — where बहु states that "
            "there is MUCH of what the second member names, बहु "
            "is accented AS THOUGH IT WERE नञ्. Not one rule but "
            "four at once, the vṛtti stepping through them: "
            "**नञ्सुभ्याम् इत्युक्तम्, बहोरपि तथा भवति — "
            "बहुयवो देशः, बहुव्रीहिः, बहुतिलः; कपि पूर्वम् "
            "इत्युक्तम्, बहोरपि तथा भवति — बहुकुमारीको देशः, "
            "बहुवृषलीकः; ह्रस्वान्तेऽन्त्यात् पूर्वम् इत्युक्तम्, "
            "बहोरपि तथा भवति — बहुयवको देशः, बहुव्रीहिकः, "
            "बहुमाषकः**. And 6.2.116's four words follow too. A "
            "single word नञ्वत् importing a whole run"),
    Uttarapada(
        "6.2.176", refuses=True, purvapada=("bahu",),
        gana="guṇādi", result=("avayava",), blocks=("6.2.175",),
        keeps_out="बहुगुणो ब्राह्मणः — **अध्ययनश्रुतसदाचारादयोऽत्र "
                  "गुणाः**, qualities and not parts",
        why="न गुणादयोऽवयवाः — but not where the गुणादि words "
            "name PARTS of the thing: **बहुगुणा रज्जुः, "
            "बह्वक्षरं पदम्, बहुच्छन्दोमानम्, बहुसूक्तः, "
            "बह्वध्यायः** — a rope of many strands, a word of "
            "many syllables. **गुणादिराकृतिगणो द्रष्टव्यः**, and "
            "the difference the rule turns on is the vṛtti's own: "
            "a strand is part of the rope, learning is not part "
            "of the brahmin"),
    Uttarapada(
        "6.2.177", where="anta", purvapada_gana=("upasarga",),
        result=("svāṅga",), excludes=("parśu",),
        samasa="bahuvrīhi",
        keeps_out="दर्शनीयललाटः — no उपसर्ग; प्रशाखो वृक्षः — a "
                  "tree's branch is no limb; उद्बाहुः क्रोशति — "
                  "raised for the moment and not FIXED; "
                  "उत्पर्शुः, विपर्शुः — the word named out",
        why="उपसर्गात् स्वाङ्गं ध्रुवम् अपर्शु — after an "
            "उपसर्ग, a second member naming a FIXED part of the "
            "body, पर्शु excepted, is end-accented in a "
            "बहुव्रीहि: **प्रपृष्ठः, प्रोदरः, प्रललाटः**. And "
            "ध्रुवम् is glossed: **ध्रुवम् इत्येकरूपम् उच्यते। "
            "ध्रुवम् अस्य शीलम् इति यथा। सततं यस्य प्रगतं पृष्ठं "
            "भवति स प्रपृष्ठः** — one whose back is permanently "
            "thrust forward, not one who has just now raised his "
            "arms"),
    Uttarapada(
        "6.2.178", where="anta", of=("vana",),
        purvapada_gana=("upasarga",),
        why="वनं समासे — वन after an उपसर्ग is end-accented in "
            "ANY compound: **प्रवणे यष्टव्यम्, निर्वणे "
            "प्रणिधीयते** — the ण् coming from 8.4.5. **समासग्रहणं "
            "समासमात्रपरिग्रहार्थम्, बहुव्रीहावेव हि स्यात्** — "
            "without the word समासे the बहुव्रीहि heading running "
            "from 6.2.106 would have confined it"),
    Uttarapada(
        "6.2.179", where="anta", of=("vana",), purvapada=("antar",),
        why="अन्तः — and वन after अन्तर् likewise: "
            "**अन्तर्वणो देशः**. The vṛtti says why a separate "
            "sūtra was needed at all: **अनुपसर्गार्थ आरम्भः** — "
            "अन्तर् is no उपसर्ग, so 6.2.178 could not have "
            "reached it"),
    Uttarapada(
        "6.2.180", where="anta", of=("antar",),
        purvapada_gana=("upasarga",),
        why="अन्तश्च — and the word अन्तर् ITSELF is end-accented "
            "after an उपसर्ग: **प्रान्तः, पर्यन्तः**. Which "
            "compound this is the vṛtti leaves open: "
            "**बहुव्रीहिरयं प्रादिसमासो वा**"),
    Uttarapada(
        "6.2.181", refuses=True, of=("antar",),
        purvapada=("ni", "vi"), blocks=("6.2.180",),
        why="न निविभ्याम् — but not after नि or वि: **न्यन्तः, "
            "व्यन्तः**.\\n\\n"
            "**AND THE REFUSAL LEAVES A SVARITA BEHIND.** "
            "**पूर्वपदप्रकृतिस्वरत्वे कृते यणादेशः। तत्र "
            "उदात्तस्वरितयोर्यणः स्वरितोऽनुदात्तस्य इति स्वरितो "
            "भवति** — the first member keeps its accent, then its "
            "इ becomes य्, and 8.2.4 turns the following low "
            "vowel svarita. न्यन्तः is not merely un-end-accented "
            "but carries a third kind of accent altogether"),
    Uttarapada(
        "6.2.182", where="anta", of=("maṇḍala",),
        purvapada=("pari",), result=("abhitobhāvin",),
        blocks=("6.2.33",),
        why="परेरभितोभावि मण्डलम् — after परि, a second member "
            "naming what lies ON BOTH SIDES, and the word मण्डल, "
            "are end-accented: **परिकूलम्, परितीरम्, "
            "परिमण्डलम्**. **अभित इत्युभयतः। अभितो भावोऽस्यास्तीति "
            "तदभितोभावि**.\\n\\n"
            "**AND IT OVERRIDES AN EARLIER RULE ON EITHER "
            "READING.** **बहुव्रीहिरयं प्रादिसमासोऽव्ययीभावो वा। "
            "अव्ययीभावपक्षेऽपि हि परिप्रत्युपापावर्ज्यमानाहोरात्रा"
            "वयवेषु इति पूर्वपदप्रकृतिस्वरत्वं प्राप्तम् अनेन "
            "बाध्यते** — read as an अव्ययीभाव, 6.2.33 would have "
            "kept परि's accent; this rule takes it"),
    Uttarapada(
        "6.2.183", where="anta", purvapada=("pra",),
        result=("saṃjñā",), excludes=("svāṅga",),
        keeps_out="प्रहस्तम्, प्रपदम् — parts of the body; "
                  "प्रपीठम् — not a name",
        why="प्राद् अस्वाङ्गं संज्ञायाम् — after प्र, a second "
            "member NOT naming a part of the body is "
            "end-accented where the compound is a NAME: "
            "**प्रकोष्ठम्, प्रगृहम्, प्रद्वारम्** — the forearm, "
            "the front room, the gateway"),
    Uttarapada(
        "6.2.184", where="anta", gana="nirudakādi",
        why="निरुदकादीनि च — and the निरुदकादि words are "
            "end-accented: **निरुदकम्, निरुलपम्, निरुपलम्, "
            "निर्मशकम्, निर्मक्षिकम्, निष्कालकः, निष्पेषः, "
            "दुस्तरीपः**. The list is of whole COMPOUNDS — "
            "**निरुदकादीनि च शब्दरूपाणि** — not of second "
            "members, and the vṛtti leaves each one's analysis "
            "open: **एषां प्रादिसमासो बहुव्रीहिर्वा। "
            "अव्ययीभावे तु समासान्तोदात्तत्वेनैव सिद्धम्**"),
    Uttarapada(
        "6.2.185", where="anta", of=("mukha",), purvapada=("abhi",),
        why="अभेर्मुखम् — मुख after अभि is end-accented: "
            "**अभिमुखः**.\\n\\n"
            "**AND IT IS STATED THOUGH 6.2.177 ALREADY COVERED "
            "IT — FOR THREE REASONS.** **उपसर्गात् स्वाङ्गम् इति "
            "सिद्धे वचनम् अबहुव्रीह्यर्थम् अध्रुवार्थम् "
            "अस्वाङ्गार्थं च** — 6.2.177 wanted a बहुव्रीहि, a "
            "FIXED part, and a part of the BODY; this rule wants "
            "none of the three, so it reaches **अभिमुखा शाला**, "
            "a hall that faces one"),
    Uttarapada(
        "6.2.186", where="anta", of=("mukha",), purvapada=("apa",),
        why="अपाच्च — and मुख after अप: **अपमुखः, अपमुखम्**. "
            "The vṛtti says what it is for even where 6.2.177 "
            "would reach: **अव्ययीभावेऽप्यत्र प्रयोजयति। तत्रापि "
            "हि परिप्रत्युपापा वर्ज्यमानाहोरात्रावयवेषु "
            "इत्युक्तम्** — as an अव्ययीभाव it would have fallen "
            "to 6.2.33 instead. And why it is a separate sūtra at "
            "all: **योगविभाग उत्तरार्थः**, so that अप may carry "
            "into the next rule"),
    Uttarapada(
        "6.2.187", where="anta",
        of=("sphij", "pūta", "vīṇā", "añjas", "adhvan", "kukṣi",
            "nāman"),
        gana="sīranāman", purvapada=("apa",),
        why="स्फिगपूतवीणाञ्जोऽध्वकुक्षिसीरनामनामानि च — six named "
            "words, the words for a PLOUGH, and the word नामन्, "
            "are end-accented after अप: **अपस्फिगम्, अपपूतम्, "
            "अपवीणम्, अपाञ्जः, अपाध्वा, अपकुक्षिः; अपसीरः, "
            "अपहलम्, अपलाङ्गलम्; अपनाम**.\\n\\n"
            "**AND अध्वन् IS NAMED BECAUSE A समासान्त MAY FAIL TO "
            "APPEAR.** **उपसर्गादध्वनः इति यदा समासान्तो नास्ति, "
            "तदानेनान्तोदात्तत्वं भवति। तस्मिन् हि सत्यच्प्रत्ययस्य "
            "चित्त्वादेव सिद्धम्। अनित्यश्च समासान्तः इत्येतदेव "
            "ज्ञापकम्** — with 5.4.85's अच् in place the accent "
            "follows from its चित् marker; naming अध्वन् here "
            "shows that the समासान्त is not compulsory"),
    Uttarapada(
        "6.2.188", where="anta", purvapada=("adhi",),
        result=("uparistha",),
        keeps_out="अधिकरणम् — करण does not stand ABOVE anything",
        why="अधेरुपरिस्थम् — after अधि, a second member naming "
            "what stands ABOVE is end-accented: **अधिदन्तः, "
            "अधिकर्णः, अधिकेशः**. The vṛtti explains the first: "
            "**दन्तस्योपरि योऽन्यो दन्तो जायते स उच्यतेऽधिदन्त "
            "इति** — a tooth grown over a tooth. And it offers "
            "the compound two analyses, **अध्यारूढो दन्त इति "
            "प्रादिसमासः। अध्यारूढो वा दन्त इति समानाधिकरण "
            "उत्तरपदलोपी समासः**"),
    Uttarapada(
        "6.2.189", where="anta", purvapada=("anu",),
        of=("kanīyas",), result=("apradhāna",),
        keeps_out="अनुगतो ज्येष्ठः अनुज्येष्ठः — where ज्येष्ठ IS "
                  "the principal word",
        why="अनोरप्रधानकनीयसी — after अनु, a second member that "
            "is NOT the principal word, and the word कनीयस्, are "
            "end-accented: **अनुगतो ज्येष्ठम् अनुज्येष्ठः, "
            "अनुमध्यमः; अनुगतः कनीयान् अनुकनीयान्**.\\n\\n"
            "**AND कनीयस् IS NAMED BECAUSE IT IS THE PRINCIPAL "
            "WORD.** **पूर्वपदार्थप्रधानः प्रादिसमासोऽयम्** for "
            "the first two, but **उत्तरपदार्थप्रधानोऽयम्** for "
            "अनुकनीयान् — **प्रधानार्थं च कनीयोग्रहणम्**. The "
            "sūtra names it precisely because अप्रधान would have "
            "shut it out"),
    Uttarapada(
        "6.2.190", where="anta", of=("puruṣa",), purvapada=("anu",),
        result=("anvādiṣṭa",),
        keeps_out="अनुगतः पुरुषः अनुपुरुषः — a man merely "
                  "followed, not one spoken of after",
        why="पुरुषश्चान्वादिष्टः — and पुरुष after अनु, where it "
            "means one SPOKEN OF AFTERWARDS: **अन्वादिष्टः "
            "पुरुषः अनुपुरुषः**. The vṛtti glosses the sense "
            "three ways: **अन्वादिष्टोऽन्वाचितः कथितानुकथितो वा**"),
    Uttarapada(
        "6.2.191", where="anta", purvapada=("ati",),
        excludes=("kṛt",),
        keeps_out="अतिकारकः — a कृदन्त; अतिगार्ग्यः — no verbal "
                  "root has been elided",
        why="अतेरकृत्पदे — after अति, a second member that is NOT "
            "a कृदन्त, and the word पद, are end-accented: "
            "**अत्यङ्कुशो नागः, अतिकशोऽश्वः** — an elephant past "
            "the goad, a horse past the whip; **अतिपदा शक्वरी** "
            "for पद.\\n\\n"
            "**AND A VĀRTTIKA ADDS A CONDITION THE SŪTRA DOES NOT "
            "STATE.** **अतेर्धातुलोप इति वक्तव्यम्** — a verbal "
            "root must have been dropped from the analysis. "
            "**इह मा भूत् — शोभनो गार्ग्यः अतिगार्ग्यः। इह च यथा "
            "स्यात् — अतिक्रान्तः कारकाद् अतिकारक इति** — so "
            "अतिकारक IS reached when it means gone past the "
            "agent, the verb क्रान्त having dropped out, though "
            "अतिकारकः meaning a fine agent is not"),
    Uttarapada(
        "6.2.192", where="anta", purvapada=("ni",),
        excludes=("nidhāna",),
        keeps_out="निवाग् वृषलः, निदण्डः — **निहितवाक्, "
                  "निहितदण्ड इत्यर्थः**, where नि does mean laid "
                  "away",
        why="नेरनिधाने — after नि, the second member is "
            "end-accented where CONCEALMENT is not meant: "
            "**निमूलम्, न्यक्षम्, नितृणम्**. **निधानम् "
            "अप्रकाशता**.\\n\\n"
            "**AND WHY AN उपसर्ग CAN CARRY A SENSE AT ALL.** "
            "**निशब्दोऽत्र निधानार्थं ब्रवीति। प्रादयो हि "
            "वृत्तिविषये ससाधनां क्रियाम् आहुः** — inside a "
            "compound a प्रादि states a whole action along with "
            "its means, and that is how नि can mean laid away and "
            "not merely down"),
    Uttarapada(
        "6.2.193", where="anta", purvapada=("prati",),
        gana="aṃśvādi", samasa="tatpuruṣa",
        keeps_out="प्रतिगता अंशवोऽस्य प्रत्यंशुरयमुष्ट्रः — a "
                  "बहुव्रीहि",
        why="प्रतेरंश्वादयस्तत्पुरुषे — after प्रति, the "
            "अंश्वादि words are end-accented in a तत्पुरुष: "
            "**प्रतिगतः अंशुः प्रत्यंशुः, प्रतिजनः, प्रतिराजा**. "
            "The gaṇa runs **अंशु। जन। राजन्। उष्ट्र। खेटक। "
            "अजिर। आर्द्रा। श्रवण। कृत्तिका। अर्ध। पुर**, and "
            "राजन् is in it for a reason: **राजशब्दः "
            "समासान्तस्यानित्यत्वाद् यदा टज् नास्ति, तदा "
            "प्रयोजयति**"),
    Uttarapada(
        "6.2.194", where="anta", purvapada=("upa",), of=("ajina",),
        result=("dvyac",), excludes=("gaurādi",),
        samasa="tatpuruṣa",
        keeps_out="उपगौरः, उपतैषः — the गौरादि words; उपगतः "
                  "सोमोऽस्य उपसोमः — a बहुव्रीहि",
        why="उपाद् द्व्यजजिनमगौरादयः — after उप, a second member "
            "of TWO VOWELS, and the word अजिन, are end-accented "
            "in a तत्पुरुष, the गौरादि words excepted: **उपगतो "
            "देवम् उपदेवः, उपसोमः, उपेन्द्रः, उपहोडः; "
            "उपाजिनम्**. The gaṇa closes **गौर। तैष। तैट। लट। "
            "लोट। जिह्वा। कृष्णा। कन्या। गुड। कल्प। पाद। "
            "गौरादिः**"),
    Uttarapada(
        "6.2.195", where="anta", purvapada=("su",),
        samasa="tatpuruṣa", result=("avakṣepaṇa",),
        keeps_out="कुब्राह्मणः — the first member is not सु; "
                  "शोभनेषु तृणेषु सुतृणेषु — praise and no scorn",
        why="सोरवक्षेपणे — after सु, the second member of a "
            "तत्पुरुष is end-accented where SCORN is meant: "
            "**इह खल्विदानीं सुस्थण्डिले सुस्फिगाभ्यां "
            "सुप्रत्यवसितः**. **अवक्षेपणं निन्दा**.\\n\\n"
            "**AND सु ITSELF STILL MEANS PRAISE.** **सुशब्दोऽत्र "
            "पूजायामेव। वाक्यार्थस्तु अवक्षेपणम् असूयया तथा"
            "भिधानात्** — the scorn is not in the word but in the "
            "sentence: one says *nicely* out of spite"),
    Uttarapada(
        "6.2.196", where="anta", of=("utpuccha",),
        samasa="tatpuruṣa", optional=True,
        keeps_out="उदस्तं पुच्छमस्य उत्पुच्छः — a बहुव्रीहि",
        why="विभाषोत्पुच्छे — उत्पुच्छ in a तत्पुरुष is "
            "OPTIONALLY end-accented: **उत्क्रान्तः पुच्छाद् "
            "उत्पुच्छः / उत्पुच्छः**.\\n\\n"
            "**AND THE OPTION WORKS BOTH WAYS AT ONCE.** **यदा "
            "तु पुच्छमुदस्यति उत्पुच्छयति, उत्पुच्छयतेरच्, "
            "उत्पुच्छः, तदा थाथादिसूत्रेण नित्यम् अन्तोदात्तत्वे "
            "प्राप्ते विकल्पोऽयम् इति सेयम् उभयत्रविभाषा भवति** — "
            "read one way the end-accent was not otherwise "
            "available and the option grants it; read the other, "
            "6.2.144 had already made it compulsory and the "
            "option takes it away. An उभयत्रविभाषा"),
    Uttarapada(
        "6.2.197", where="anta", purvapada=("dvi", "tri"),
        of=("pād", "dat", "mūrdhan"), samasa="bahuvrīhi",
        optional=True,
        why="द्वित्रिभ्यां पाद्दन्मूर्धसु बहुव्रीहौ — after द्वि "
            "or त्रि, these three are OPTIONALLY end-accented in "
            "a बहुव्रीहि: **द्वौ पादावस्य द्विपात् / द्विपात्; "
            "त्रिपात् / त्रिपात्; द्विदन् / द्विदन्; द्विमूर्धा "
            "/ द्विमूर्धा**.\\n\\n"
            "**AND EACH OF THE THREE IS NAMED IN A DIFFERENT "
            "STATE.** **पादिति कृताकारलोपः पादशब्दो गृह्यते। "
            "ददिति कृतददादेशो दन्तशब्दः। मूर्धन्निति त्वकृत"
            "समासान्तो नान्त एव मूर्धन्शब्दः** — पाद् after its "
            "आ has gone, दत् after the दद्-substitution has "
            "happened, but मूर्धन् before any समासान्त is added. "
            "Three words, three different points in the "
            "derivation"),
    Uttarapada(
        "6.2.198", where="anta", of=("saktha",),
        excludes=("ka-anta",), optional=True,
        keeps_out="चक्रसक्थः — चक्र ends in क, and **षचश्चित्त्वाद् "
                  "नित्यम् अन्तोदात्तत्वं भवति** there anyway",
        why="सक्थं च अक्रान्तात् — सक्थ is OPTIONALLY "
            "end-accented after a first member NOT ending in क: "
            "**गौरसक्थः / गौरसक्थः, श्लक्ष्णसक्थः / "
            "श्लक्ष्णसक्थः**. And the word is named in a "
            "particular state: **सक्थमिति कृतसमासान्तः "
            "सक्थिशब्दोऽत्र गृह्यते** — सक्थि after its समासान्त "
            "has been added"),
    Uttarapada(
        "6.2.199", where="para-ādi", chandasi=True, optional=True,
        why="परादिश्छन्दसि बहुलम् — in the Veda, VARIOUSLY, the "
            "accent falls on the first syllable of the FOLLOWING "
            "word: **अञ्जिसक्थमालभेत; त्वाष्ट्रौ लोमशसक्थौ; "
            "ऋजुबाहुः, वाक्पतिः, चित्पतिः**. And पर here is not "
            "any following word: **परशब्देनात्र सक्थशब्द एव "
            "गृह्यते**, it carries सक्थ down from 6.2.198.\\n\\n"
            "**AND THE PĀDA ENDS BY ADMITTING THAT ITS OWN RULES "
            "ARE NOT THE WHOLE STORY.** **परादिश्च परान्तश्च "
            "पूर्वान्तश्चापि दृश्यते। पूर्वादयश्च दृश्यन्ते "
            "व्यत्ययो बहुलं ततः** — first-of-the-second, "
            "last-of-the-second, last-of-the-first and "
            "first-of-the-first are all attested, and the "
            "exchange between them is many-sided. A vārttika adds "
            "one more list: **अन्तोदात्तप्रकरणे त्रिचक्रादीनां "
            "छन्दस्युपसंख्यानम् — त्रिबन्धुरेण, त्रिवृता रथेन "
            "त्रिचक्रेण**"),
)


def _reaches(row: Uttarapada, uttarapada: str, gana: str,
             affix: str, purvapada: str, purvapada_gana: str,
             samasa: str, case: str, result: str,
             chandasi: bool) -> bool:
    """
    Whether one row is even in play for this query.

    Two groups of columns are read as ALTERNATIVES inside
    themselves and as requirements between themselves: a rule names
    what the second member may be — a word, a class, an affix — and
    separately what the first member may be. 6.2.151 names two
    affixes, four words and a gaṇa, any of which does; 6.2.145 names
    सु and the class उपमान, either of which does. But 6.2.112 wants
    कर्ण in the second place AND a colour-word in the first, and
    both have to hold.
    """
    if row.heading and not (row.of or row.gana or row.affix
                            or row.purvapada or row.samasa):
        return False
    named = row.of or row.gana or row.affix
    if named and not (uttarapada in row.of
                      or (row.gana and gana == row.gana)
                      or (row.affix and affix in row.affix)):
        return False
    before = row.purvapada or row.purvapada_gana
    if before and not (purvapada in row.purvapada
                       or purvapada_gana in row.purvapada_gana):
        return False
    if row.samasa and samasa != row.samasa:
        return False
    if row.case and case != row.case:
        return False
    if row.result and result not in row.result:
        return False
    if row.chandasi and not chandasi:
        return False
    if row.excludes and (uttarapada in row.excludes
                         or purvapada in row.excludes
                         or result in row.excludes
                         or samasa in row.excludes
                         or gana in row.excludes):
        return False
    return True


def _supplies(row: Uttarapada, wants: str) -> bool:
    if not wants:
        return True
    return wants == row.where and not row.refuses


def _how_specific(row: Uttarapada, uttarapada: str, gana: str,
                  affix: str, purvapada: str,
                  purvapada_gana: str) -> int:
    """
    A refusal beats what it refuses, and a named second member beats
    a named first one.

    That is 6.2.64–110's ordering turned round again, and for the
    same reason: this run is about the उत्तरपद, so the word it names
    in second place is the sharper of the two. 6.2.185 अभेर्मुखम्
    and 6.2.167 मुखं स्वाङ्गम् both name मुख, and the one that also
    names अभि is the one meant.

    And every column is scored on whether THIS query matched
    through it, never on whether the row happens to fill it.
    6.2.151 names four words, a gaṇa and two affixes; reached by
    its affix alone it must not outrank 6.2.117, which names सु
    and the same affix and means the narrower thing.
    """
    return (
        12 * bool(row.refuses)
        + 9 * bool(row.of and uttarapada in row.of)
        + 8 * bool(row.purvapada and purvapada in row.purvapada)
        + 7 * bool(row.affix and affix in row.affix)
        + 6 * bool(row.gana and gana == row.gana)
        + 5 * bool(row.purvapada_gana
                   and purvapada_gana in row.purvapada_gana)
        + 4 * bool(row.result)
        + 3 * bool(row.case)
        + 2 * bool(row.samasa)
        + 2 * bool(row.chandasi)
    )


def second_member(uttarapada: str = "", *, gana: str = "",
                  affix: str = "", purvapada: str = "",
                  purvapada_gana: str = "", samasa: str = "",
                  case: str = "", result: str = "",
                  chandasi: bool = False,
                  wants: str = "") -> Accented:
    """
    6.2.111–199 — what happens to the second member of a compound.

    Nothing answers by default: where no rule of this run is
    reached, 6.1.223 समासस्य stands and the accent is at the end of
    the whole compound.
    """
    matched = [
        row for row in UTTARAPADA_TABLE
        if _reaches(row, uttarapada, gana, affix, purvapada,
                    purvapada_gana, samasa, case, result, chandasi)
        and _supplies(row, wants)
    ]
    if not matched:
        return Accented(
            "", "", "No rule of 6.2.111–199 is reached, so 6.1.223 "
                    "समासस्य stands and the accent is at the end of "
                    "the compound")
    row = max(matched, key=lambda one: _how_specific(
        one, uttarapada, gana, affix, purvapada,
        purvapada_gana))
    return Accented("" if row.refuses else row.where, row.sutra,
                    row.why, optional=row.optional,
                    blocked_by=row.blocks)


def uttarapada_runs() -> Accented:
    """
    The three placements this stretch is divided into, and the one
    scope-word that outlives all three.

    **उत्तरपदस्येत्येतदा पादपरिसमाप्तेः। आदिरिति प्रकृत्या भगालम्
    इति यावत्**, then **प्रकृत्येत्येतदधिकृतम् अन्तः इति यावद्
    वेदितव्यम्**, then अन्तः to the end.
    """
    return Accented(
        "ādi", UTTARAPADA_RUN[0],
        "उत्तरपदम् governs %s–%s, the whole of the pāda's second "
        "half. Inside it आदिः holds %s–%s, प्रकृत्या %s–%s and "
        "अन्तः %s–%s. And बहुव्रीहि, opened back at %s, reaches "
        "into this run as far as %s"
        % (UTTARAPADA_RUN[0], UTTARAPADA_RUN[1],
           ADI_RUN[0], ADI_RUN[1], PRAKRTI_RUN[0], PRAKRTI_RUN[1],
           ANTA_RUN[0], ANTA_RUN[1],
           BAHUVRIHI_RUN[0], BAHUVRIHI_RUN[1]))


def provisions_for(sutra_id: str) -> Tuple[Uttarapada, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in UTTARAPADA_TABLE
                 if row.sutra == sutra_id)


__all__ = [
    "Uttarapada", "UTTARAPADA_TABLE", "UTTARAPADA_RUN", "ADI_RUN",
    "PRAKRTI_RUN", "ANTA_RUN", "KRATVADI", "CIHANADI", "CURNADI",
    "THE_SIX", "VARGYADI", "CARVADI", "GAURADI", "AMSVADI",
    "NIRUDAKADI", "AKRTIGANA", "ACARYADI", "DEVATA_EXCEPTIONS",
    "VYATYAYA_VERSE", "second_member", "uttarapada_runs",
    "provisions_for",
]
