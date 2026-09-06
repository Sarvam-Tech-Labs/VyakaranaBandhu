# -*- coding: utf-8 -*-
"""
६.४.४६–७० — आर्धधातुके, and what the stem loses before it.

6.4.46 opens a heading inside a heading. अङ्गस्य is still running
from 6.4.1 and will run to the end of adhyāya 7; आर्धधातुके runs
twenty-three sūtras and stops because 6.4.69 says न ल्यपि —
**आर्धधातुक इत्यधिकारः। न ल्यपि इति प्राग् एतस्माद् यदित ऊर्ध्वम्
अनुक्रमिष्याम आर्धधातुक इत्येवं तद् वेदितव्यम्**.

Under it, the losses that make Sanskrit's derived stems: an अ goes
(6.4.48), a य् after a consonant goes (6.4.49), the causal णि goes
before an इट्-less affix (6.4.51) and before a सेट् निष्ठा
(6.4.52), and an आ goes before an इट् (6.4.64). चिकीर्षिता,
बेभिदिता, अततक्षत्, कारितम्, पपिथ.

**AND WHERE THE णि DOES NOT GO IT BECOMES अय्.** 6.4.55 before
six affixes, 6.4.56 before ल्यप् after a light syllable, 6.4.57
optionally after आप्. कारयांचकार, स्पृहयालुः, स्तनयित्नुः,
प्रणमय्य.

**AND ONE SŪTRA OF THE RUN IS THE LONGEST IN THE PĀDA.** 6.4.62
स्यसिच्सीयुट्तासिषु... चिण्वदिट् च says that four affixes in the
passive and impersonal behave AS THOUGH चिण् were there, and takes
an इट् with it. The vṛtti opens by asking what the sūtra is for at
all — **कानि पुनर् अस्य योगस्य प्रयोजनानि?** — and answers in
verse.

**WHAT THIS MODULE DOES NOT DO.** It reports what is lost or
substituted and by which rule. It does not build the form: that
कारितम् then needs 7.2.35's इट्, and that अध्यगीष्ट needs a लुङ्,
are other rules' business.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: The heading inside the heading, and its bound in its own
#: words: **न ल्यपि इति प्राग् एतस्मात्**.
ARDHADHATUKA_RUN: Tuple[str, str] = ("6.4.46", "6.4.68")

#: And this module's stretch, which runs two sūtras past it to
#: take in the rule that ENDS it and the one beside it.
LOPA_RUN: Tuple[str, str] = ("6.4.46", "6.4.70")

#: 6.4.55's six, before which the causal णि becomes अय्.
AY_BEFORE: Tuple[str, ...] = (
    "ām", "anta", "ālu", "āyya", "itnu", "iṣṇu")

#: 6.4.66's seven — the घु class and six named roots.
GHU_SEVEN: Tuple[str, ...] = (
    "ghu", "mā", "sthā", "gā", "pā", "jahāti", "sā")

#: 6.4.62's four affixes, and the three roots it names beside the
#: vowel-final class.
CINVAT_FOUR: Tuple[str, ...] = ("sya", "sic", "sīyuṭ", "tāsi")
CINVAT_ROOTS: Tuple[str, ...] = ("han", "grah", "dṛś")


@dataclass(frozen=True)
class Loss:
    """One rule of 6.4.46–70: what the stem loses or becomes."""

    sutra: str
    #: lopa, ay, ram, dīrgha, yuṭ, īt, et, it, ciṇvat.
    does: str = ""
    #: The stems the rule names outright.
    of: Tuple[str, ...] = ()
    #: A named class of stem instead.
    gana: str = ""
    #: What must FOLLOW.
    before: Tuple[str, ...] = ()
    #: What part of the stem is affected.
    part: str = ""
    #: The further condition on the environment.
    result: Tuple[str, ...] = ()
    excludes: Tuple[str, ...] = ()
    refuses: bool = False
    optional: bool = False
    nipatana: bool = False
    heading: bool = False
    chandasi: bool = False
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


LOSS_TABLE: Tuple[Loss, ...] = (
    Loss(
        "6.4.46", heading=True,
        why="आर्धधातुके — **आर्धधातुक इत्यधिकारः। न ल्यपि इति "
            "प्राग् एतस्माद् यदित ऊर्ध्वम् अनुक्रमिष्याम "
            "आर्धधातुक इत्येवं तद् वेदितव्यम्** — a heading inside "
            "6.4.1's, running twenty-three sūtras and stopping "
            "because 6.4.69 says न ल्यपि. The vṛtti reads the next "
            "rule out as its example: **वक्ष्यति अतो लोपः — "
            "चिकीर्षिता, जिहीर्षिता। आर्धधातुक इति किम्? भवति, "
            "भवतः**.\\n\\n"
            "**AND THE HEADING HAS TO BE STATED BECAUSE ONE "
            "PARIBHĀṢĀ WOULD OTHERWISE HAVE DONE THE WORK.** "
            "**अदिप्रभृतिभ्यः शपो लुग्वचनं प्रत्ययलोपलक्षणप्रतिषेधार्थं "
            "स्याद् इत्येतद् न** — one might think 2.4.72's लुक् "
            "was stated to keep 1.1.63 from acting, and that the "
            "same reasoning would fence these rules; it does not"),
    Loss(
        "6.4.47", does="ram", of=("bhrasj",), part="ra-upadhā",
        optional=True,
        keeps_out="बरीभृज्ज्यते — **उपदेश इत्येव**, the rule wants "
                  "the root as taught",
        why="भ्रस्जो रोपधयो रमन्यतरस्याम् — the र् AND the penult "
            "of भ्रस्ज् together become रम्, optionally: "
            "**भ्रष्टा / भर्ष्टा; भ्रष्टुम् / भर्ष्टुम्; "
            "भ्रज्जनम् / भर्जनम्**.\\n\\n"
            "**AND THE SUBSTITUTE'S म् PUTS IT WHERE IT GOES.** "
            "**रोपधयोरिति स्थानषष्ठीनिर्देशाद् उपधा रेफश्च "
            "निवर्तेते, मित्त्वात् चायम् अचोऽन्त्यात् परो भवति** "
            "— the genitive says the र् and the penult go, and "
            "the म् marker says the substitute lands after the "
            "last vowel"),
    Loss(
        "6.4.48", does="lopa", gana="a-anta", part="antya",
        keeps_out="चेता, स्तोता — not अ-final; याता, वाता — the "
                  "tapara shuts the long आ out; वृक्षत्वम्, "
                  "वृक्षता — a taddhita and no ārdhadhātuka",
        why="अतो लोपः — an अ-final stem loses that अ before an "
            "ārdhadhātuka: **चिकीर्षिता, चिकीर्षितुम्, "
            "चिकीर्षितव्यम्; धिनुतः, कृणुतः**.\\n\\n"
            "**AND IT BEATS THE STRENGTHENING BY BEING NAMED "
            "EARLIER.** **वृद्धिदीर्घाभ्याम् अतो लोपः "
            "पूर्वविप्रतिषेधेन — चिकीर्षकः, जिहीर्षकः, "
            "चिकीर्ष्यते** — the vṛddhi and the lengthening would "
            "both have reached the same अ, and the earlier rule "
            "takes it"),
    Loss(
        "6.4.49", does="lopa", of=("ya",), result=("hal-pūrva",),
        why="यस्य हलः — a य standing after a consonant is lost "
            "before an ārdhadhātuka: **बेभिदिता, बेभिदितुम्, "
            "बेभिदितव्यम्**.\\n\\n"
            "**AND WHAT IS LOST IS THE WHOLE य AND NOT ITS LAST "
            "SOUND.** **यस्येति संघातग्रहणम् एतत्। तत्र अलोऽन्त्यस्य "
            "इत्येतद् न भवति, अतो लोपः इत्यनेनैव तस्य सिद्धत्वात्** "
            "— read as a whole, so 1.1.52 does not cut it down to "
            "the final अ, which 6.4.48 had already taken anyway. "
            "Or, the vṛtti offers, **हल इति वा पञ्चमीनिर्देशः, "
            "तत्र आदेः परस्य इति यकारोऽनेन लुप्यते**"),
    Loss(
        "6.4.50", does="lopa", of=("kya",), result=("hal-pūrva",),
        optional=True,
        why="क्यस्य विभाषा — and क्य after a consonant is lost "
            "OPTIONALLY: **समिध्यिता / समिधिता; दृषद्यिता / "
            "दृषदिता**. Which क्य the vṛtti leaves to the "
            "derivation: **समिधम् आत्मन इच्छति, समिद् इवाचरति इति "
            "वा क्यच्क्यङौ यथायोगं कर्तव्यौ**"),
    Loss(
        "6.4.51", does="lopa", of=("ṇi",), excludes=("iṭ",),
        keeps_out="कारयिता, हारयिता — the ārdhadhātuka has an इट्",
        why="णेरनिटि — the causal णि is lost before an "
            "ārdhadhātuka that takes NO इट्: **अततक्षत्, "
            "अररक्षत्, आशिशत्, आटिटत्; कारणा, हारणा; कारकः, "
            "हारकः; कार्यते, हार्यते; ज्ञीप्सति**. The vṛtti "
            "names what it displaces in one breath: "
            "**इयङ्यण्गुणवृद्धिदीर्घाणाम् अपवादः**"),
    Loss(
        "6.4.52", does="lopa", of=("ṇi",), before=("niṣṭhā",),
        result=("seṭ",),
        keeps_out="संज्ञपितः पशुः — the इट् is optional there by "
                  "7.2.49, and 7.2.15 then refuses it in the "
                  "निष्ठा",
        why="निष्ठायां सेटि — and the णि is lost before a निष्ठा "
            "WITH an इट्: **कारितम्, हारितम्, गणितम्, लक्षितम्**. "
            "So the णि goes both with the इट् and without it, and "
            "the two sūtras between them leave only कारयिता "
            "standing.\\n\\n"
            "**AND SAYING सेटि IS WHAT KEEPS ONE FORM OUT OF BOTH "
            "RULES.** **सेड्ग्रहणसामर्थ्याद् इह पूर्वेणापि न "
            "भवति** — the mere fact that सेट् had to be said shows "
            "6.4.51 does not reach संज्ञपितः either"),
    Loss(
        "6.4.53", does="lopa", of=("ṇi",), before=("tṛc",),
        result=("mantra",), nipatana=True,
        keeps_out="जनयिता — outside a मन्त्र",
        why="जनिता मन्त्रे — जनिता is laid down for a मन्त्र, "
            "with the णि lost before an इट्-taking affix: **यो नः "
            "पिता जनिता**. Neither 6.4.51 nor 6.4.52 could have "
            "reached it, the affix having an इट् and not being a "
            "निष्ठा"),
    Loss(
        "6.4.54", does="lopa", of=("ṇi",), before=("tṛc",),
        result=("yajña",), nipatana=True,
        keeps_out="शृतं हविः शमयितः — outside the rite",
        why="शमिता यज्ञे — and शमिता in the rite: **शृतं हविः "
            "शमितः**. **तृचि संबुध्यन्तम् एतत्** — the form laid "
            "down is a vocative of the तृच् stem, not the "
            "nominative"),
    Loss(
        "6.4.55", does="ay", of=("ṇi",), before=AY_BEFORE,
        why="अय् आमन्तात्वाय्येत्न्विष्णुषु — before six affixes "
            "the णि becomes अय् instead of going: **कारयांचकार, "
            "हारयांचकार** (आम्); **गण्डयन्तः, मण्डयन्तः** (अन्त); "
            "**स्पृहयालुः, गृहयालुः** (आलु); **स्पृहयाय्यः** "
            "(आय्य); **स्तनयित्नुः** (इत्नु); **पोषयिष्णवः, "
            "पारयिष्णवः** (इष्णु).\\n\\n"
            "**AND SAYING अय् RATHER THAN न IS FOR THE RULE "
            "AFTER.** **नेति वक्तव्येऽयादेशवचनम् उत्तरार्थम्** — "
            "*not* would have sufficed here, since the णि simply "
            "staying would give the same forms; अय् is said so "
            "that 6.4.56 can carry it"),
    Loss(
        "6.4.56", does="ay", of=("ṇi",), before=("lyap",),
        result=("laghu-pūrva",),
        keeps_out="प्रपात्य गतः — the syllable before the णि is "
                  "not light",
        why="ल्यपि लघुपूर्वात् — and before ल्यप्, where the sound "
            "before the णि is LIGHT: **प्रणमय्य, प्रतमय्य, "
            "प्रदमय्य, प्रशमय्य, संदमय्य गतः; प्रबेभिदय्य गतः; "
            "प्रगणय्य गतः**.\\n\\n"
            "**AND 6.4.22's असिद्धत्व DOES NOT REACH HERE.** "
            "**ह्रस्वयलोपाल्लोपानाम् असिद्धत्वं न भवति "
            "असमानाश्रयत्वात्। ह्रस्वादयो हि णौ, ल्यपि णेर् अयादेशो "
            "भवति** — the shortening and the two elisions rest on "
            "the णि, and this substitution rests on the ल्यप्, so "
            "the two do not share a locus and 6.4.22's अत्र fails"),
    Loss(
        "6.4.57", does="ay", of=("ṇi",), before=("lyap",),
        result=("āp-pūrva",), optional=True,
        keeps_out="अध्याप्य गतः — the आप् there is the substitute "
                  "for इङ् and not the root, **इङादेशस्य "
                  "लाक्षणिकत्वाद् न भवति**",
        why="विभाषाऽऽपः — and after आप्, optionally: **प्रापय्य "
            "गतः / प्राप्य गतः**"),
    Loss(
        "6.4.58", does="dīrgha", of=("yu", "plu"), before=("lyap",),
        chandasi=True,
        keeps_out="संयुत्य, आप्लुत्य — outside the Veda",
        why="युप्लुवोर्दीर्घश्छन्दसि — यु and प्लु lengthen before "
            "ल्यप् in the Veda: **दान्त्यनुपूर्वं वियूय; यत्रापो "
            "दक्षिणा परिप्लूय**"),
    Loss(
        "6.4.59", does="dīrgha", of=("kṣi",), before=("lyap",),
        why="क्षियः — and क्षि lengthens before ल्यप्, Veda or no: "
            "**प्रक्षीय**"),
    Loss(
        "6.4.60", does="dīrgha", of=("kṣi",), before=("niṣṭhā",),
        excludes=("ṇyat-artha",),
        keeps_out="अक्षितमसि मा मेक्षेष्ठाः — the निष्ठा is in the "
                  "sense of a ण्यत्, which the sūtra shuts out",
        why="निष्ठायामण्यदर्थे — and क्षि lengthens in a निष्ठा "
            "that is NOT in a ण्यत्'s sense: **आक्षीणः, प्रक्षीणः, "
            "परिक्षीणः**. **ण्यतः कृत्यस्यार्थो भावकर्मणी, "
            "ताभ्याम् अन्यत्र या निष्ठा** — the ण्यत् means the "
            "act or the object, and a निष्ठा meaning either is "
            "out.\\n\\n"
            "**AND THE VṚTTI ACCOUNTS FOR THE क्त IN TWO WAYS.** "
            "**अकर्मकत्वात् क्षियः कर्तरि क्तः** for प्रक्षीणः, "
            "and **प्रक्षीणम् इदं देवदत्तस्येति क्तोऽधिकरणे च "
            "ध्रौव्यगतिप्रत्यवसानार्थेभ्यः इत्यधिकरणे क्तः** for "
            "the other reading"),
    Loss(
        "6.4.61", does="dīrgha", of=("kṣi",), before=("niṣṭhā",),
        result=("ākrośa", "dainya"), optional=True,
        blocks=("6.4.60",),
        why="वाऽऽक्रोशदैन्ययोः — but where ABUSE or MISERY is "
            "meant the lengthening is OPTIONAL: **क्षितायुरेधि / "
            "क्षीणायुरेधि** for abuse; **क्षितकः / क्षीणकः; "
            "क्षितोऽयं तपस्वी / क्षीणोऽयं तपस्वी** for misery"),
    Loss(
        "6.4.62", does="ciṇvat", gana="ac-anta", of=CINVAT_ROOTS,
        before=CINVAT_FOUR, result=("bhāva", "karman"),
        optional=True,
        why="स्यसिच्सीयुट्तासिषु भावकर्मणोरुपदेशेऽज्झनग्रहदृशां "
            "वा चिण्वदिट् च — before स्य, सिच्, सीयुट् and तासि "
            "in the passive or the impersonal, a vowel-final stem "
            "as TAUGHT, and हन्, ग्रह् and दृश्, behave AS THOUGH "
            "चिण् were there, and take an इट् with it.\\n\\n"
            "**AND WHAT THE चिण्वत् REACHES IS THE AFFIX AND NOT "
            "THE STEM.** **यदा चिण्वत् तदा इडागमो भवति। कस्य? "
            "स्यसिच्सीयुट्तासीनाम् एवेति वेदितव्यम्। ते हि "
            "प्रकृताः। अङ्गस्य तु लक्ष्यविरोधाद् न क्रियते** — the "
            "इट् goes to the four affixes, because they are what "
            "the sūtra has in hand, and giving it to the stem "
            "would contradict the forms.\\n\\n"
            "**AND THE VṚTTI OPENS BY ASKING WHAT THE SŪTRA IS "
            "FOR.** **कानि पुनर् अस्य योगस्य प्रयोजनानि?** — and "
            "answers in verse. The longest sūtra of the pāda, and "
            "the only one that makes one thing behave like "
            "another rather than replacing it.\\n\\n"
            "**SCOPE** — the verse's list of प्रयोजनानि, and which "
            "of चिण्'s own effects follow and which do not, is "
            "not modelled here"),
    Loss(
        "6.4.63", does="yuṭ", of=("dīṅ",), before=("ac",),
        result=("kṅit",),
        keeps_out="उपदेदीयते — not a vowel-initial affix; "
                  "उपदानम् — neither कित् nor ङित्",
        why="दीङो युडचि क्ङिति — दीङ् takes the augment युट् "
            "before a vowel-initial कित् or ङित्: **उपदिदीये, "
            "उपदिदीयाते, उपदिदीयिरे**.\\n\\n"
            "**AND THE AUGMENT GOES TO THE AFFIX AND NOT THE "
            "ROOT.** **दीङ इति पञ्चमीनिर्देशाद् अजादेर् युडागमो "
            "भवति** — the ablative says *after दीङ्*, so the "
            "augment is the vowel-initial affix's. And "
            "**विधानसामर्थ्यात् च एरनेकाचः० इति यणादेशे कर्तव्ये "
            "तस्यासिद्धत्वं न भवति** — 6.4.22 would have hidden it "
            "from 6.4.82, and the mere fact of the rule being "
            "stated stops that"),
    Loss(
        "6.4.64", does="lopa", gana="ā-anta", part="antya",
        before=("iṭ", "ac"), result=("kṅit",),
        keeps_out="यान्ति, वान्ति — no ārdhadhātuka; ग्लायते, "
                  "दासीय — the affix does not begin with a vowel",
        why="आतो लोप इटि च — an आ-final stem loses that आ before "
            "an इट्, and before a vowel-initial कित् or ङित्: "
            "**पपिथ, तस्थिथ** for the इट्; **पपतुः, पपुः, "
            "तस्थतुः, तस्थुः; गोदः, कम्बलदः** for the कित्; "
            "**प्रदा, प्रधा** for the ङित्. And **व्यत्यरे, "
            "व्यत्यले** are रा and ला in the लङ् with an इट्"),
    Loss(
        "6.4.65", does="īt", gana="ā-anta", before=("yat",),
        why="ईद्यति — and an आ-final stem takes ई before यत्: "
            "**देयम्, धेयम्, हेयम्, स्तेयम्** — to be given, to "
            "be placed, to be abandoned, to be stolen"),
    Loss(
        "6.4.66", does="īt", gana="ghu", of=GHU_SEVEN[1:],
        before=("hal",), result=("kṅit",),
        keeps_out="पायते — पा of the second class is not meant, "
                  "**पातेर् इह ग्रहणं नास्ति, लुग्विकरणत्वात्**",
        why="घुमास्थागापाजहातिसां हलि — the घु class and six named "
            "roots take ई before a consonant-initial कित् or "
            "ङित्: **दीयते, धीयते, देदीयते** for घु; **मीयते, "
            "मेमीयते; स्थीयते, तेष्ठीयते; गीयते, जेगीयते, "
            "अध्यगीष्ट; पीयते, पेपीयते; हीयते** for the rest"),
    Loss(
        "6.4.67", does="et", gana="ghu", of=GHU_SEVEN[1:],
        before=("liṅ",), result=("kṅit",),
        keeps_out="दासीष्ट, धासीष्ट — the लिङ् is neither कित् "
                  "nor ङित् there",
        why="एर्लिङि — and the same seven take ए before लिङ्: "
            "**देयात्, धेयात्, मेयात्, स्थेयात्, गेयात्, पेयात्, "
            "हेयात्, अवसेयात्**"),
    Loss(
        "6.4.68", does="et", gana="ā-anta-saṃyoga-ādi",
        before=("liṅ",), result=("kṅit",),
        excludes=tuple(GHU_SEVEN), optional=True,
        keeps_out="स्थेयात् — one of the seven, and 6.4.67 makes "
                  "it compulsory; यायात् — no cluster at the "
                  "start; निर्वायात् — **अङ्गस्येत्येव**",
        why="वाऽन्यस्य संयोगादेः — and an आ-final stem BEGINNING "
            "with a cluster, other than those seven, takes ए "
            "before लिङ् optionally: **ग्लेयात् / ग्लायात्; "
            "म्लेयात् / म्लायात्**. This is the last sūtra under "
            "आर्धधातुके; the next word ends the heading"),
    Loss(
        "6.4.69", refuses=True, gana="ghu", of=GHU_SEVEN[1:],
        before=("lyap",), blocks=("6.4.66", "6.4.67"),
        why="न ल्यपि — but before ल्यप्, none of what was said of "
            "the seven holds: **प्रदाय, प्रधाय, प्रमाय, प्रस्थाय, "
            "प्रगाय, प्रपाय, प्रहाय, अवसाय**.\\n\\n"
            "**AND THIS SŪTRA IS ALSO THE BOUND OF THE HEADING.** "
            "6.4.46's आर्धधातुके was read **न ल्यपि इति प्राग् "
            "एतस्मात्** — up to but not including this. So one "
            "sūtra both refuses an operation and closes the run "
            "that granted it"),
    Loss(
        "6.4.70", does="it", of=("may",), before=("lyap",),
        optional=True,
        why="मयतेरिदन्यतरस्याम् — मय् takes इ before ल्यप्, "
            "optionally: **अपमित्य / अपमाय**. Stated after the "
            "heading has closed, and about the same affix that "
            "closed it"),
)


def _reaches(row: Loss, stem: str, gana: str, before: str,
             part: str, result: str, chandasi: bool) -> bool:
    if row.heading:
        return False
    named = row.of or row.gana
    if named and not (stem in row.of
                      or (row.gana and gana == row.gana)):
        return False
    if row.before and before not in row.before:
        return False
    if row.part and part and part != row.part:
        return False
    if row.result and result not in row.result:
        return False
    if row.chandasi and not chandasi:
        return False
    if row.excludes and (stem in row.excludes
                         or gana in row.excludes
                         or before in row.excludes
                         or result in row.excludes):
        return False
    return True


def _supplies(row: Loss, wants: str) -> bool:
    if not wants:
        return True
    return wants == row.does and not row.refuses


def _how_specific(row: Loss, stem: str, gana: str,
                  before: str) -> int:
    """
    A refusal beats what it refuses, and a rule that undoes one
    beats the refusal.

    6.4.60 and 6.4.61 are the pair that needs the second: both
    lengthen क्षि in a निष्ठा, and 6.4.61 differs only by a sense
    and by being optional.
    """
    return (
        12 * (0 if row.refuses else len(row.blocks))
        + 10 * bool(row.refuses)
        + 6 * bool(row.of and stem in row.of)
        + 4 * bool(row.gana and gana == row.gana)
        + 4 * bool(row.result)
        + 2 * bool(row.before and before in row.before)
    )


@dataclass(frozen=True)
class Lost:
    """What the run answers: a loss or a substitute."""

    does: str
    sutra: str
    why: str
    optional: bool = False
    nipatana: bool = False
    blocked_by: Tuple[str, ...] = ()


def before_ardhadhatuka(stem: str = "", *, gana: str = "",
                        before: str = "", part: str = "",
                        result: str = "", chandasi: bool = False,
                        wants: str = "") -> Lost:
    """
    6.4.46–70 — what the stem loses or becomes before the affix.

    Nothing answers by default: where no rule is reached the stem
    stands as it is, which is what भवति and यान्ति are.
    """
    matched = [
        row for row in LOSS_TABLE
        if _reaches(row, stem, gana, before, part, result, chandasi)
        and _supplies(row, wants)
    ]
    if not matched:
        return Lost(
            "", "", "No rule of 6.4.46–70 is reached, so the stem "
                    "stands as it is")
    row = max(matched,
              key=lambda one: _how_specific(one, stem, gana, before))
    return Lost("" if row.refuses else row.does, row.sutra, row.why,
                optional=row.optional, nipatana=row.nipatana,
                blocked_by=row.blocks)


def provisions_for(sutra_id: str) -> Tuple[Loss, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in LOSS_TABLE if row.sutra == sutra_id)


__all__ = [
    "Loss", "LOSS_TABLE", "ARDHADHATUKA_RUN", "LOPA_RUN",
    "AY_BEFORE", "GHU_SEVEN", "CINVAT_FOUR", "CINVAT_ROOTS",
    "Lost", "before_ardhadhatuka", "provisions_for",
]
