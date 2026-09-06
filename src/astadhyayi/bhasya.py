# -*- coding: utf-8 -*-
"""
६.४.१२९–१५३ — भस्य, and what the weak stem loses.

6.4.129 opens the pāda's last heading, and it runs to the end:
**भस्येत्ययमधिकारः, आ अध्यायपरिसमाप्तेः**. भ is 1.4.18's name for
the stem before a vowel-initial weak ending or a taddhita, and
everything from here is about what happens to it there.

Almost all of it is subtraction. राज्ञः has lost the अ of अन्;
दधीचः has lost the अ of अच्; विदुषः has vocalised its वस्; शुनः,
यूनः, मघोनः have vocalised their न्; गार्गी has lost the य of its
patronymic. What is left of a Sanskrit weak stem is what these
twenty-five rules leave.

**AND THE HEADING'S OWN EXAMPLE IS A SŪTRA WHOSE TEXT IS CORRUPT
IN ONE WITNESS.** GRETIL gives 6.4.130 as *vakṣyati - pādaḥ pat*,
with the vṛtti's **वक्ष्यति** run into the sūtra; Vidyut gives
**पादः पत्**, which is the text. Recorded here rather than
inherited.

**AND ONE SUBSTITUTE REACHES ONLY WHAT IS NAMED AND NOT WHAT ENDS
IN IT.** 6.4.130's पद् replaces पाद् and not the whole stem that
ends in it — **निर्दिश्यमानस्यादेशा भवन्ति इति पाच्छब्दस्यैव
भवति, न तदन्तस्य सर्वस्य** — so द्विपदः is द्वि + पद् and not a
new word.

**WHAT THIS MODULE DOES NOT DO.** It reports what the भ stem
loses or becomes and by which rule. It does not decline: whether
a stem IS भ is 1.4.18's question, and the query answers it.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: The pāda's last heading: **भस्येत्ययमधिकारः, आ
#: अध्यायपरिसमाप्तेः**.
BHASYA_RUN: Tuple[str, str] = ("6.4.129", "6.4.175")

#: And this module's stretch inside it, closing before the
#: इष्ठेमेयस् block opens at 6.4.154.
LOSS_RUN: Tuple[str, str] = ("6.4.129", "6.4.153")

#: What 6.4.133 vocalises, and 6.4.128 had just been making into
#: a त्-final stem: मघवन् is worked over twice, five sūtras apart.
SVA_YUVA_MAGHAVAN: Tuple[str, ...] = ("śvan", "yuvan", "maghavan")

#: 6.4.149's four, whose य goes before ई and a taddhita.
SURYADI: Tuple[str, ...] = ("sūrya", "tiṣya", "agastya", "matsya")

#: The witness disagreement at 6.4.130, recorded rather than
#: inherited.
GRETIL_CORRUPT: Tuple[str, str] = (
    "vakṣyati - pādaḥ pat", "pādaḥ pat")


@dataclass(frozen=True)
class Bha:
    """One rule of 6.4.129–153: what the भ stem loses."""

    sutra: str
    #: pad, saṃprasāraṇa, ūṭh, al-lopa, lopa, luk, īt, guṇa,
    #: ṭi-lopa.
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
    heading: bool = False
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


BHA_TABLE: Tuple[Bha, ...] = (
    Bha(
        "6.4.129", heading=True,
        why="भस्य — **भस्येत्ययमधिकारः, आ अध्यायपरिसमाप्तेः। यदित "
            "ऊर्ध्वम् अनुक्रमिष्यामो भस्येत्येवं तद् वेदितव्यम्** "
            "— the pāda's last heading, and it runs to the end of "
            "the adhyāya. भ is 1.4.18's name for the stem before a "
            "vowel-initial weak ending or a taddhita.\\n\\n"
            "**AND THE VṚTTI READS THE NEXT SŪTRA OUT AS ITS "
            "EXAMPLE, WITH A COUNTER-EXAMPLE.** **वक्ष्यति पादः "
            "पत् — द्विपदः पश्य, द्विपदा कृतम्। भस्येति किम्? "
            "द्विपादौ, द्विपादः** — the same stem before a strong "
            "ending is not भ and keeps its आ"),
    Bha(
        "6.4.130", does="pad", of=("pāda",),
        keeps_out="द्विपादौ, द्विपादः — a strong ending, so the "
                  "stem is not भ",
        why="पादः पत् — a stem ending in पाद् becomes पद् when it "
            "is भ: **द्विपदः पश्य; द्विपदा; द्विपदे; द्विपदिकां "
            "ददाति; वैयाघ्रपद्यः**. And the पाद meant is the one "
            "that has already lost its आ — **पाद इति पादशब्दो "
            "लुप्ताकारो गृह्यते**.\\n\\n"
            "**AND THE SUBSTITUTE TAKES THE NAMED WORD AND NOT "
            "WHAT ENDS IN IT.** **स च निर्दिश्यमानस्यादेशा भवन्ति "
            "इति पाच्छब्दस्यैव भवति, न तदन्तस्य सर्वस्य** — so "
            "द्विपदः is द्वि followed by पद्, and not one new "
            "word.\\n\\n"
            "**AND THE WITNESSES DISAGREE ABOUT THE TEXT.** GRETIL "
            "reads *vakṣyati - pādaḥ pat*, with the vṛtti's "
            "**वक्ष्यति** run into the sūtra; Vidyut reads **पादः "
            "पत्**, which is the sūtra. Recorded rather than "
            "inherited"),
    Bha(
        "6.4.131", does="saṃprasāraṇa", gana="vasu-anta",
        why="वसोः संप्रसारणम् — a वस्-final भ stem vocalises: "
            "**विदुषः पश्य; विदुषा; विदुषे; पेचुषः; पपुषः**.\\n\\n"
            "**AND 6.4.22 DOES NOT HIDE IT FROM WHAT COMES "
            "NEXT.** **आकारलोपे कर्तव्ये वसुसंप्रसारणस्य "
            "व्याश्रयत्वाद् असिद्धत्वं न भवति** — the vocalisation "
            "and the आ-loss rest on different things, so the अत्र "
            "of 6.4.22 fails and the second sees the first. And "
            "**वसुग्रहणे क्वसोरपि ग्रहणम् इष्यते** — the क्वसु "
            "affix is taken along with the bare वस्"),
    Bha(
        "6.4.132", does="ūṭh", gana="vāha-anta",
        why="वाह ऊठ् — a वाह्-final भ stem vocalises to ऊठ् and "
            "not to the plain उ: **प्रष्ठौहः, प्रष्ठौहा, "
            "प्रष्ठौहे; दित्यौहः, दित्यौहा, दित्यौहे**. The औ is "
            "6.1.89's, **एत्येधत्यूठ्सु**, which names ऊठ् by "
            "name.\\n\\n"
            "**AND THE VṚTTI ASKS WHY ऊठ् AT ALL.** **अथ "
            "किमर्थम् ऊठ् क्रियते, संप्रसारण एव कृते गुणे च "
            "वृद्धिरेचि इति वृद्धौ सत्याम्...** — a plain "
            "vocalisation with guṇa and then 6.1.88's vṛddhi "
            "would have reached the same shape, and the ठ् is "
            "what makes 6.1.89 apply instead"),
    Bha(
        "6.4.133", does="saṃprasāraṇa", of=SVA_YUVA_MAGHAVAN,
        excludes=("taddhita",),
        keeps_out="शौवनं मांसम्, यौवनं वर्तते, माघवनः स्थालीपाकः "
                  "— a taddhita follows, which the sūtra shuts out",
        why="श्वयुवमघोनामतद्धिते — श्वन्, युवन् and मघवन् "
            "vocalise before an affix that is NOT a taddhita: "
            "**शुनः, शुना, शुने; यूनः, यूना, यूने; मघोनः, "
            "मघोना, मघोने**.\\n\\n"
            "**AND ONE OF THE THREE WAS WORKED OVER FIVE SŪTRAS "
            "AGO.** 6.4.128 मघवा बहुलम् made मघवन् into मघवत्, "
            "variously; this makes it मघोन्. The same stem, two "
            "rules, and the vṛtti of 6.4.128 gives both sets of "
            "forms side by side"),
    Bha(
        "6.4.134", does="al-lopa", gana="an-anta", part="a",
        keeps_out="राजकीयम् — **अनो नकारान्तस्यायं लोप इष्यते**, "
                  "and there the न् is not final",
        why="अल्लोपोऽनः — an अन्-final भ stem loses that अ: "
            "**राज्ञः पश्य; राज्ञा; राज्ञे; तक्ष्णः पश्य; "
            "तक्ष्णा; तक्ष्णे**. This is the rule that makes "
            "राज्ञः out of राजन्, and with 6.4.8's lengthening "
            "for the strong cases it is most of how an "
            "न्-final noun declines"),
    Bha(
        "6.4.135", does="al-lopa", gana="ṣa-pūrva-an",
        of=("han", "dhṛtarājan"), part="a", before=("aṇ",),
        keeps_out="सामनः, वैमनः — **अन् इति प्रकृतिभावेन "
                  "अल्लोपटिलोपाव् उभाव् अपि न भवतः**, by 6.4.167; "
                  "ताक्षण्यः — no अण्",
        why="षपूर्वहन्धृतराज्ञामणि — and before अण्, the same loss "
            "for an अन् with a ष् before it, and for हन् and "
            "धृतराजन्: **औक्ष्णः, ताक्ष्णः; भ्रौणघ्नः; "
            "धार्तराज्ञः**"),
    Bha(
        "6.4.136", does="al-lopa", gana="an-anta", part="a",
        before=("ṅi", "śī"), optional=True, blocks=("6.4.134",),
        why="विभाषा ङिश्योः — and before ङि and शी the loss is "
            "OPTIONAL: **राज्ञि / राजनि; साम्नि / सामनि; साम्नी "
            "/ सामनी**"),
    Bha(
        "6.4.137", refuses=True, gana="an-anta", part="a",
        result=("saṃyoga-va-ma-anta",), blocks=("6.4.134", "6.4.136"),
        keeps_out="प्रतिदीव्ना, साम्ना — no cluster; तक्ष्णा — the "
                  "cluster does not end in व् or म्",
        why="न संयोगाद् वमन्तात् — but not after a cluster ending "
            "in व् or म्: **पर्वणा, पर्वणे; अथर्वणा, अथर्वणे; "
            "चर्मणा, चर्मणे**. Both halves of the condition are "
            "tested — a cluster, and one ending in one of those "
            "two sounds"),
    Bha(
        "6.4.138", does="lopa", gana="ac-anta", part="a",
        why="अचः — an अच्-final भ stem loses its अ: **दधीचः "
            "पश्य; दधीचा; दधीचे; मधूचः पश्य; मधूचा; मधूचे**. "
            "And अच् here is अञ्चति with its न् already gone — "
            "**अच इत्ययम् अञ्चतिर् लुप्तनकारो गृह्यते** — the "
            "same word 6.3.138 called चु"),
    Bha(
        "6.4.139", does="īt", gana="ac-anta", of=("ud",),
        why="उद ईत् — and after उद् the अच् becomes ई: "
            "**उदीचः, उदीचा, उदीचे** — northern, and the word "
            "for the north"),
    Bha(
        "6.4.140", does="lopa", gana="ā-anta-dhātu", part="antya",
        keeps_out="निया, निये — not आ-final; खट्वाः पश्य, मालाः "
                  "पश्य — not a root",
        why="आतो धातोः — an आ-final ROOT that is भ loses that आ: "
            "**कीलालपः पश्य; कीलालपा; कीलालपे; शुभंयः पश्य; "
            "शुभंया; शुभंये**.\\n\\n"
            "**AND THE SŪTRA IS SPLIT SO THAT आतः CAN CARRY "
            "ALONE.** **आत इति योगविभागः। तेन क्त्वो ल्यप्, हलः "
            "श्नः शानच्० इत्येवमादि...** — divided, the word आतः "
            "reaches further than the whole sūtra could"),
    Bha(
        "6.4.141", does="lopa", of=("ātman",), part="ādi",
        before=("āṅ",), result=("mantra",),
        keeps_out="आत्मना कृतम् — not a मन्त्र; यदात्मनस् तन् नो "
                  "वरिष्ठा — no आङ्",
        why="मन्त्रेष्वाङ्यादेरात्मनः — in a मन्त्र, आत्मन् loses "
            "its FIRST sound before आङ्: **त्मना देवेभ्यः; "
            "त्मना सोमेषु**. A vārttika widens it: **आङोऽन्यत्रापि "
            "दृश्यते — त्मन्या समञ्जन्**"),
    Bha(
        "6.4.142", does="lopa", of=("viṃśati",), part="ti",
        before=("ḍit",),
        keeps_out="विंशत्या — no डित्",
        why="ति विंशतेर्डिति — विंशति loses its ति before a डित् "
            "affix: **विंशत्या क्रीतो विंशकः; विंशतेः पूरणो "
            "विंशः; एकविंशः**"),
    Bha(
        "6.4.143", does="ṭi-lopa", part="ṭi", before=("ḍit",),
        why="टेः — and any stem loses its टि before a डित्: "
            "**कुमुद्वान्, नड्वान्, वेतस्वान्; उपसरजः, मन्दुरजः; "
            "त्रिंशता क्रीतस् त्रिंशकः**.\\n\\n"
            "**AND THIS ONE REACHES PAST THE HEADING.** **डित्य् "
            "अभस्याप्य् अनुबन्धकरणसामर्थ्यात् टिलोपो भवति** — भस्य "
            "is running, and the mere fact that the ड् marker was "
            "put on the affix at all shows the loss reaches a stem "
            "that is not भ as well"),
    Bha(
        "6.4.144", does="ṭi-lopa", gana="n-anta", part="ṭi",
        before=("taddhita",),
        keeps_out="सात्वतः — not न्-final; शर्मणा, शर्मणे — no "
                  "taddhita",
        why="नस्तद्धिते — an न्-final भ stem loses its टि before a "
            "taddhita: **आग्निशर्मिः, औडुलोमिः**, the इञ् by "
            "4.1.96's बाह्वादि. A vārttika adds a long list of "
            "stems the rule would otherwise miss — "
            "**सब्रह्मचारिपीठसर्पिकलापिकुथुमि...**"),
    Bha(
        "6.4.145", does="ṭi-lopa", of=("ahan",), part="ṭi",
        before=("ṭa", "kha"),
        keeps_out="अह्ना — neither ट nor ख, and the नियम shuts "
                  "everything else out",
        blocks=("6.4.144",),
        why="अह्नष्टखोरेव — अहन् loses its टि before ट and ख and "
            "NOWHERE ELSE: **द्वे अहनी समाहृते द्व्यहः; त्र्यहः; "
            "द्व्यहीनः, त्र्यहीनः; अह्नां समूहः क्रतुर् अहीनः**. "
            "**सिद्धे सत्यारम्भो नियमार्थः** — 6.4.144 had already "
            "supplied it, and the एव is what fences it"),
    Bha(
        "6.4.146", does="guṇa", gana="u-anta",
        before=("taddhita",),
        why="ओर्गुणः — a उ-final भ stem takes guṇa before a "
            "taddhita: **बाभ्रव्यः, माण्डव्यः; शङ्कव्यं दारु; "
            "पिचव्यः कार्पासः; कमण्डलव्या मृत्तिका; परशव्यम् अयः; "
            "औपगवः; कापटवः**.\\n\\n"
            "**AND SAYING गुण RATHER THAN ओ IS WHAT LETS ANOTHER "
            "FORM THROUGH.** **ओरोद् इति वक्तव्ये गुणग्रहणं "
            "संज्ञापूर्वको विधिर् अनित्यः यथा स्यात्। तेन "
            "स्वायंभुव इति सिद्धं भवति** — an operation stated by "
            "its technical name is not compulsory, and that is "
            "how स्वायंभुव comes out"),
    Bha(
        "6.4.147", does="lopa", gana="u-anta", before=("ḍha",),
        excludes=("kadrū",),
        keeps_out="काद्रवेयो मन्त्रमपश्यत् — कद्रू, named out",
        why="ढे लोपोऽकद्र्वाः — and before ढ the उ is simply "
            "DROPPED instead, कद्रू excepted: **कामण्डलेयः, "
            "शैतवाहेयः, जाम्बेयः, माद्रबाहेयः**"),
    Bha(
        "6.4.148", does="lopa", gana="i-a-anta", part="antya",
        before=("ī", "taddhita"),
        why="यस्येति च — an इ-final or अ-final भ stem loses that "
            "vowel before ई and before a taddhita: **दाक्षी, "
            "प्लाक्षी, सखी**.\\n\\n"
            "**AND THE LOSS IS STATED RATHER THAN LEFT TO THE "
            "SINGLE-VOWEL RULE FOR A REASON.** "
            "**सवर्णदीर्घत्वे हि सत्य् अतिसखेर् आगच्छतीत्यत्र "
            "एकादेशस्यान्तवत्त्वाद् असखि इति घिसंज्ञायाः "
            "प्रतिषेधः स्यात्** — 6.1.101 would have given one "
            "long vowel for two, 6.1.85 would then treat it as "
            "the stem's end, and 1.4.7's exception for सखि would "
            "wrongly bite"),
    Bha(
        "6.4.149", does="lopa", of=SURYADI, part="upadhā-ya",
        before=("ī", "taddhita"),
        why="सूर्यतिष्यागस्त्यमत्स्यानां य उपधायाः — four stems "
            "lose the य of their penult before ई and a taddhita: "
            "**सूर्येणैकदिक् सौरी बलाका**.\\n\\n"
            "**AND WHETHER 6.4.22 HIDES IT DEPENDS ON WHICH AFFIX "
            "FOLLOWS.** **अणि यो यस्येति लोपस् तस्यासिद्धत्वं "
            "नास्ति, व्याश्रयत्वात्। ईकारे तु यस् तस्यासिद्धत्वाद् "
            "उपधायकारो भस्याणन्तस्य सूर्यस्य संबन्धीति लुप्यते** — "
            "before अण् the two rest on different things and the "
            "असिद्धत्व fails; before ई they rest on the same thing "
            "and it holds"),
    Bha(
        "6.4.150", does="lopa", part="taddhita-ya",
        result=("hal-pūrva",), before=("ī",),
        keeps_out="कारिकेयी — no consonant before the य; "
                  "वैद्यस्य भार्या वैद्यी — the य is not a "
                  "taddhita's",
        why="हलस्तद्धितस्य — a TADDHITA's य after a consonant is "
            "lost before ई: **गार्गी, वात्सी**. **तद्धित इति "
            "निवृत्तम्** — the taddhita is no longer the "
            "environment but the thing lost"),
    Bha(
        "6.4.151", does="lopa", part="āpatya-ya",
        result=("hal-pūrva",), before=("taddhita",),
        excludes=("āt-ādi",),
        keeps_out="सांकाश्यकः, काम्पिल्यकः — the य is no "
                  "patronymic's; गार्ग्यायणः, वात्स्यायनः — the "
                  "taddhita begins with आ; कारिकेयस्यापत्यम् — no "
                  "consonant before the य",
        why="आपत्यस्य च तद्धितेऽनाति — a PATRONYMIC's य after a "
            "consonant is lost before a taddhita that does not "
            "begin with आ: **गर्गाणां समूहो गार्गकम्; "
            "वात्सकम्**. And **तद्धितग्रहणम् ईत्य् अनापत्यस्यापि "
            "लोपार्थम् — सौमी इष्टिः**"),
    Bha(
        "6.4.152", does="lopa", part="āpatya-ya",
        result=("hal-pūrva",), before=("kyac", "cvi"),
        keeps_out="सांकाश्यायते, सांकाश्यीभूतः — no patronymic; "
                  "कारिकेयीयति — no consonant before the य",
        why="क्यच्व्योश्च — and before क्य and च्वि: "
            "**वात्सीयति, गार्गीयति; वात्सायते, गार्गायते; "
            "गार्गीभूतः, वात्सीभूतः**"),
    Bha(
        "6.4.153", does="luk", gana="bilvakādi", part="cha",
        before=("taddhita",),
        why="बिल्वकादिभ्यश्छस्य लुक् — after the बिल्वकादि stems "
            "the छ of a भ stem is dropped before a taddhita: "
            "**बिल्वा यस्यां सन्ति बिल्वकीया, तस्यां भवा "
            "बैल्वकाः; वेणुकीया — वैणुकाः; वेत्रकीया — वैत्रकाः**. "
            "The बिल्वकादि are the नडादि words with 4.2.91's कुक् "
            "already on them — **नडादिषु बिल्वादयः पठ्यन्ते। "
            "नडादीनां कुक् च इति कृतकुगागमा बिल्वकादयो भवन्ति**"),
)


def _reaches(row: Bha, stem: str, gana: str, before: str,
             part: str, result: str) -> bool:
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
    if row.excludes and (stem in row.excludes
                         or gana in row.excludes
                         or before in row.excludes
                         or result in row.excludes):
        return False
    return True


def _supplies(row: Bha, wants: str) -> bool:
    if not wants:
        return True
    return wants == row.does and not row.refuses


def _how_specific(row: Bha, stem: str, gana: str) -> int:
    """
    A refusal beats what it refuses, a rule that names what it
    displaces beats it, and a named stem beats a named class.

    6.4.134, 6.4.136 and 6.4.137 are the three that need all of
    it: one drops the अ of अन्, one makes that optional before two
    affixes, and one refuses it after a cluster.

    **AND THE REFUSAL OUTWEIGHS A ROW THAT MERELY DISPLACES.**
    `blocks` means two things — a supplying row naming what it
    replaces, and a प्रतिषेध naming what it holds off — so it is
    zeroed for a refusing row and the refusal is weighed instead,
    at more than one displacement is worth. Without that, 6.4.136's
    विभाषा would beat 6.4.137 on पर्वणि and offer an option the
    Kāśikā does not: चर्मणि has no *चर्म्णि beside it. Nothing in
    this run undoes a refusal, which is what the opposite ordering
    would have been for.
    """
    return (
        12 * (0 if row.refuses else len(row.blocks))
        + 14 * bool(row.refuses)
        + 6 * bool(row.of and stem in row.of)
        + 4 * bool(row.gana and gana == row.gana)
        + 3 * bool(row.result)
        + 2 * bool(row.before)
        + 2 * bool(row.part)
    )


@dataclass(frozen=True)
class Weak:
    """What the run answers: a loss or a substitute in the भ stem."""

    does: str
    sutra: str
    why: str
    optional: bool = False
    blocked_by: Tuple[str, ...] = ()


def in_the_weak_stem(stem: str = "", *, gana: str = "",
                     before: str = "", part: str = "",
                     result: str = "", wants: str = "") -> Weak:
    """
    6.4.129–153 — what the भ stem loses or becomes.

    Nothing answers by default: where no rule is reached the stem
    stands as it is, which is what द्विपादौ and शर्मणा are.
    """
    matched = [
        row for row in BHA_TABLE
        if _reaches(row, stem, gana, before, part, result)
        and _supplies(row, wants)
    ]
    if not matched:
        return Weak(
            "", "", "No rule of 6.4.129–153 is reached, so the "
                    "stem stands as it is")
    row = max(matched, key=lambda one: _how_specific(one, stem, gana))
    return Weak("" if row.refuses else row.does, row.sutra, row.why,
                optional=row.optional, blocked_by=row.blocks)


def provisions_for(sutra_id: str) -> Tuple[Bha, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in BHA_TABLE if row.sutra == sutra_id)


__all__ = [
    "Bha", "BHA_TABLE", "BHASYA_RUN", "LOSS_RUN",
    "SVA_YUVA_MAGHAVAN", "SURYADI", "GRETIL_CORRUPT", "Weak",
    "in_the_weak_stem", "provisions_for",
]
