# -*- coding: utf-8 -*-
"""
५.३.१–२७ — प्राग्दिशो विभक्तिः, and the affixes stop meaning
anything of their own.

Every heading the project has met so far supplies an AFFIX and is
bounded by a sense-word. This one supplies a **saṃjñā**: 5.3.1's
vṛtti runs **प्रागेतस्माद् दिक्संशब्दनाद् यानित ऊर्ध्वम्
अनुक्रमिष्यामो विभक्तिसंज्ञास्ते वेदितव्याः** — everything named
from here to the rule that says दिक् is CALLED a विभक्ति, and the
rule gives nothing at all.

**AND WITH IT THE समर्थ HEADING LAPSES.** **अतः परं स्वार्थिकाः
प्रत्ययाः, तेषु समर्थाधिकारः प्रथमग्रहणं च प्रतियोग्यपेक्षत्वाद्
नोपयुज्यत इति द्वयमपि निवृत्तम्** — from here the affixes are
स्वार्थिक, added in the base's OWN sense, so there is no second word
for the base to be construed with and 2.1.1's समर्थः पदविधिः has
nothing to do. **वावचनं तु वर्तत एव** — but the *optionally* carries
on, so कुतः stands beside कस्मात्.

That is the whole difference between this pāda and the five before
it. There the question was what a word means with respect to
something else; here it is what happens to a word when nothing is
added to its meaning at all.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: Where the विभक्ति name runs. 5.3.1 lifts दिक् out of 5.3.27
#: exactly as 4.1.83 lifted दीव्यति and 5.1.1 क्रीत — the same
#: device for the sixth time, and the first where what is bounded
#: is a NAME rather than an affix.
VIBHAKTI_RUN: Tuple[str, str] = ("5.3.1", "5.3.26")

#: And the sūtra whose word bounds it.
VIBHAKTI_MARKER: str = "5.3.27"

#: And the ninth heading of the project, at 5.3.70 — which DOES
#: supply an affix. **प्रागेतस्मादिवसंशब्दनाद् यानित
#: ऊर्ध्वमनुक्रमिष्यामः, कप्रत्ययस्तेष्वधिकृतो वेदितव्यः.**
#:
#: And it closes one sūtra short of its marker, in the formula the
#: project has met six times before: **प्रागिवीयस्य पूर्णोऽवधिः**
#: at 5.3.95.
KA_RUN: Tuple[str, str] = ("5.3.70", "5.3.95")
KA_MARKER: str = "5.3.96"

#: Why the name is given at all — the vṛtti says so at 5.3.1:
#: **तसिलादीनां विभक्तित्वे प्रयोजनं त्यदादिविधयः, इदमो
#: विभक्तिस्वरश्च**. Being called a विभक्ति lets the त्यदादि rules
#: reach these forms, and lets 6.1.171 ऊडिदम्… put the accent on
#: the affix in इह.
WHY_THE_NAME: Tuple[str, ...] = (
    "त्यदादिविधयः",
    "इदमो विभक्तिस्वरः — ऊडिदम्… (6.1.171)",
)


@dataclass(frozen=True)
class Svarthika:
    """One rule of 5.3: a base, and an affix adding no meaning."""

    sutra: str
    gives: str = ""
    also_gives: Tuple[str, ...] = ()
    of: Tuple[str, ...] = ()
    gana: str = ""
    #: A class the base belongs to — सर्वनामन् at 5.3.2, दिक्शब्द
    #: at 5.3.27.
    of_samjna: str = ""
    #: The CASE the base stands in, which in this pāda is a
    #: condition on the base and not a relation to another word:
    #: पञ्चमी at 5.3.7, सप्तमी at 5.3.10.
    case: str = ""
    #: What the derived word must mean — काल at 5.3.15, अनद्यतन at
    #: 5.3.21, प्रकार at 5.3.23.
    result: str = ""
    #: The sound the affix must begin with — 5.3.4's र and थ,
    #: 5.3.6's द.
    before: str = ""
    #: What stands in FRONT of the base — 5.3.80's उप.
    pre: str = ""
    #: An आदेश the rule substitutes: इश् for इदम्, अश् for एतद्,
    #: स for सर्व.
    adesa: str = ""
    usage: str = ""
    optional: bool = False
    #: True where the whole form is laid down — 5.3.17 and the
    #: eighteen of 5.3.22.
    nipatana: bool = False
    #: True where the row IS the heading.
    heading: bool = False
    #: What the rule keeps OUT of its own base-class — 5.3.2's
    #: द्व्यादि.
    excludes: Tuple[str, ...] = ()
    excepts: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


SVARTHIKA_TABLE: Tuple[Svarthika, ...] = (
    Svarthika("5.3.1", heading=True,
              why="प्राग्दिशो विभक्तिः — and the heading gives no "
                  "affix. **प्रागेतस्माद् दिक्संशब्दनाद् यानित "
                  "ऊर्ध्वमनुक्रमिष्यामो विभक्तिसंज्ञास्ते "
                  "वेदितव्याः**: everything named from here to "
                  "5.3.27 is CALLED a विभक्ति. The sixth heading "
                  "bounded by lifting a word out of the rule it "
                  "stops at, and the first that bounds a NAME.\\n\\n"
                  "**AND THE NAME IS GIVEN FOR TWO CONSEQUENCES.** "
                  "**तसिलादीनां विभक्तित्वे प्रयोजनं त्यदादिविधयः, "
                  "इदमो विभक्तिस्वरश्च** — being a विभक्ति lets "
                  "the त्यदादि rules reach these forms, and lets "
                  "6.1.171 ऊडिदम्… accent the affix in **इह**.\\n\\n"
                  "**AND THE समर्थ HEADING LAPSES HERE.** "
                  "**अतः परं स्वार्थिकाः प्रत्ययाः, तेषु "
                  "समर्थाधिकारः प्रथमग्रहणं च प्रतियोग्यपेक्षत्वाद् "
                  "नोपयुज्यत इति द्वयमपि निवृत्तम्** — from here "
                  "the affixes add nothing to the base's meaning, "
                  "so there is no second word to construe with and "
                  "2.1.1 has nothing to do. **वावचनं तु वर्तत एव**, "
                  "and the option carries: **कुतः, कस्मात्; कुत्र, "
                  "कस्मिन्**"),
    Svarthika("5.3.2", of=("kim", "bahu"), of_samjna="sarvanāman",
              excludes=("dvi", "tri", "ubha", "dvyādi"),
              why="किंसर्वनामबहुभ्योऽद्व्यादिभ्यः — the bases the "
                  "whole section works on. **प्राग् दिश इत्येव**. "
                  "कुतः, कुत्र; यतः, यत्र; ततः, तत्र; बहुतः, "
                  "बहुत्र.\\n\\n"
                  "**अद्व्यादिभ्य इति किम्?** द्वाभ्याम्, द्वयोः. "
                  "**प्रकृतिपरिसंख्यानं किम्?** वृक्षात्, वृक्षे — "
                  "the rule names its bases so that ordinary nouns "
                  "are left out. **प्राग् दिश इत्येव** — "
                  "वैयाकरणपाशः.\\n\\n"
                  "**सर्वनामत्वादेव सिद्धे किमो ग्रहणं "
                  "द्व्यादिपर्युदासात्** — किम् is a सर्वनामन् "
                  "already and is named anyway, because the "
                  "exclusion of द्वि and the rest would otherwise "
                  "have cut it out too. **बहुग्रहणे संख्याग्रहणम्** "
                  "— and बहु is taken as a NUMERAL: **इह न भवति — "
                  "बहोः सूपात्**",
              keeps_out="द्वाभ्याम्, वृक्षात्, बहोः सूपात्"),
    Svarthika("5.3.3", of=("idam",), adesa="iś",
              why="इदम इश् — a substitution before any affix of "
                  "this section. **शकारः सर्वादेशार्थः** — the श "
                  "makes it replace the WHOLE word and not just its "
                  "last sound (1.1.55). **इह**"),
    Svarthika("5.3.4", of=("idam",), adesa="eta-ita", before="r-th",
              excepts=("5.3.3",),
              why="एतेतौ रथोः, **इशोऽपवादः** — two substitutes "
                  "before an affix beginning with र or थ. "
                  "**रेफेऽकार उच्चारणार्थः** — the अ of रेफ is only "
                  "so the letter can be said. 5.3.16 इदमो र्हिल् → "
                  "**एतर्हि**; 5.3.24 इदमस्थमुः → **इत्थम्**"),
    Svarthika("5.3.5", of=("etad",), adesa="aś",
              why="एतदोऽन् — **शकारः सर्वादेशार्थः** again. "
                  "**अतः, अत्र**.\\n\\n"
                  "**एतद इति योगविभागः कर्तव्यः** — and the rule is "
                  "to be split, so that एतद् also takes the एत and "
                  "इत् of 5.3.4 before र and थ: **एतर्हि, इत्थम्**. "
                  "**रेफादिः अनद्यतने र्हिलन्यतरस्याम् इति विद्यत "
                  "एव; थमुप्रत्ययः पुनरेतद उपसंख्येयः**"),
    Svarthika("5.3.6", of=("sarva",), adesa="sa", before="d",
              optional=True,
              why="सर्वस्य सोऽन्यतरस्यां दि — optionally स for "
                  "सर्व before an affix beginning with द. "
                  "**सर्वदा, सदा**.\\n\\n"
                  "**प्राग्दिशीय इत्येव** — and only before an "
                  "affix of THIS section: **सर्वं ददातीति सर्वदा "
                  "ब्राह्मणी**, a woman who gives everything, where "
                  "the दा is a verb and not one of these affixes",
              keeps_out="सर्वं ददातीति सर्वदा ब्राह्मणी"),
    Svarthika("5.3.7", gives="tasil", of=("kim", "bahu"),
              of_samjna="sarvanāman", case="pañcamī",
              why="पञ्चम्यास्तसिल् — the affix that replaces an "
                  "ablative. **कुतः, यतः, ततः, बहुतः**, and by "
                  "5.3.1's option they stand beside कस्मात्, "
                  "यस्मात्"),
    Svarthika("5.3.8", gives="tasil", adesa="tasi",
              of=("kim", "bahu"), of_samjna="sarvanāman",
              case="pañcamī",
              why="तसेश्च — and here तसिल् replaces not a case-"
                  "ending but ANOTHER AFFIX. 5.4.44 प्रतियोगे "
                  "पञ्चम्यास्तसिः and 5.4.45 give तसि; after these "
                  "bases that तसि becomes तसिल्. **कुत आगतः**, "
                  "यतः, ततः, बहुत आगतः.\\n\\n"
                  "**तसेस्तसिल्वचनं स्वरार्थं विभक्त्यर्थं च** — "
                  "and the point of the substitution is the ACCENT "
                  "and the विभक्ति name, the two things 5.3.1 said "
                  "the name was for"),
    Svarthika("5.3.9", gives="tasil", of=("pari", "abhi"),
              why="पर्यभिभ्यां च. **सर्वोभयार्थे वर्तमानाभ्यां "
                  "प्रत्यय इष्यते** — only where the two mean ALL "
                  "ROUND and ON BOTH SIDES. **परितः**, "
                  "**सर्वत इत्यर्थः**; **अभितः**, "
                  "**उभयत इत्यर्थः**"),
    Svarthika("5.3.10", gives="tral", of=("kim", "bahu"),
              of_samjna="sarvanāman", case="saptamī",
              why="सप्तम्यास्त्रल् — and the locative's affix. "
                  "**कुत्र, यत्र, तत्र, बहुत्र**"),
    Svarthika("5.3.11", gives="ha", of=("idam",), case="saptamī",
              excepts=("5.3.10",),
              why="इदमो हः, **त्रलोऽपवादः**. **इह** — and with "
                  "5.3.3's इश् the whole word is replaced, so इदम् "
                  "+ ह comes out as इह"),
    Svarthika("5.3.12", gives="at", of=("kim",), case="saptamī",
              optional=True, excepts=("5.3.10",),
              why="किमोऽत्, **त्रलोऽपवादः**. **क्व भोक्ष्यसे, "
                  "क्वाध्येष्यसे**.\\n\\n"
                  "**त्रलमपि केचिदिच्छन्ति; तत् कथम्? उत्तरसूत्राद् "
                  "वावचनं पुरस्तादपकृष्यते** — some want कुत्र too, "
                  "and it is got by dragging the *optionally* of "
                  "the NEXT rule BACKWARD. The अपकर्ष again, and "
                  "the second time in two pādas"),
    Svarthika("5.3.13", gives="ha", of=("kim",), case="saptamī",
              usage="chandasi", optional=True,
              excepts=("5.3.12",),
              why="वा ह च छन्दसि — **यथाप्राप्तं च**, so the forms "
                  "of the rules before stand as well. **क्व**, "
                  "**कुह॑** (ऋ० ८.७३.४); कुत्रचिदस्य सा दूरे"),
    Svarthika("5.3.14", gives="tasil", also_gives=("tral",),
              of=("kim", "bahu"), of_samjna="sarvanāman",
              optional=True,
              why="इतराभ्योऽपि दृश्यन्ते — from the OTHER cases "
                  "too, **पञ्चमीसप्तम्यपेक्षमितरत्वम्**. "
                  "**दृशिग्रहणं प्रायिकविध्यर्थम्** — *are seen* "
                  "makes it a rule for the most part, "
                  "**तेन भवदादिभिर्योग एवैतद्विधानम्**: only in "
                  "construction with भवत् and the like.\\n\\n"
                  "**के पुनर्भवदादयः? भवान् दीर्घायुरायुष्मान् "
                  "देवानां प्रिय इति** — the polite second person. "
                  "स भवान्, **ततो भवान्, तत्र भवान्**; तं भवन्तम्, "
                  "ततो भवन्तम्, तत्र भवन्तम्; and so through all "
                  "seven cases"),
    Svarthika("5.3.15", gives="dā",
              of=("sarva", "eka", "anya", "kim", "yad", "tad"),
              case="saptamī", result="kāla", excepts=("5.3.10",),
              why="सर्वैकान्यकिंयत्तदः काले दा, **त्रलोऽपवादः**. "
                  "सर्वस्मिन् काले **सर्वदा**; एकदा, अन्यदा, कदा, "
                  "यदा, तदा. **काल इति किम्?** सर्वत्र देशे — of a "
                  "PLACE the affix of 5.3.10 comes instead",
              keeps_out="सर्वत्र देशे"),
    Svarthika("5.3.16", gives="rhil", of=("idam",), case="saptamī",
              result="kāla", excepts=("5.3.11",),
              why="इदमो र्हिल्, **हस्यापवादः**. **लकारः "
                  "स्वरार्थः**. अस्मिन् काले **एतर्हि** — with "
                  "5.3.4's एत, since the affix begins with र. "
                  "**काल इत्येव** — इह देशे",
              keeps_out="इह देशे"),
    Svarthika("5.3.17", nipatana=True, gives="dhunā", of=("idam",),
              adesa="aś", case="saptamī", result="kāla",
              why="अधुना — **अधुनेति निपात्यते; इदमोऽश्भावो धुना च "
                  "प्रत्ययः**, the substitution and the affix laid "
                  "down together. अस्मिन् काले **अधुना**"),
    Svarthika("5.3.18", gives="dānīm", of=("idam",),
              case="saptamī", result="kāla", excepts=("5.3.11",),
              why="दानीं च. अस्मिन् काले **इदानीम्**"),
    Svarthika("5.3.19", gives="dā", also_gives=("dānīm",),
              of=("tad",), case="saptamī", result="kāla",
              excepts=("5.3.10",),
              why="तदो दा च — **चकाराद् दानीं च**. तस्मिन् काले "
                  "**तदा, तदानीम्**.\\n\\n"
                  "**तदो दावचनमनर्थकम्, विहितत्वात्** — and the दा "
                  "of this rule is idle, 5.3.15 having given it "
                  "already. The vṛtti says so and leaves it"),
    Svarthika("5.3.20", gives="dā", of=("idam",), case="saptamī",
              usage="chandasi", optional=True,
              why="तयोर्दार्हिलौ च छन्दसि, **यथासंख्यम्**; the "
                  "इदम् member, taking दा. "
                  "**तयोरिति प्रातिपदिकनिर्देशः**, and "
                  "**चकाराद् यथाप्राप्तं च**, so the ordinary forms "
                  "stand too: **इदावत्सरीयः**; इदं तर्हि, इदानीम्"),
    Svarthika("5.3.20", gives="rhil", of=("tad",), case="saptamī",
              usage="chandasi", optional=True,
              why="तयोर्दार्हिलौ च छन्दसि, the तद् member, taking "
                  "र्हिल्. **तदानीम्** stands beside it by "
                  "यथाप्राप्तम्"),
    Svarthika("5.3.21", gives="rhil", of=("kim", "bahu"),
              of_samjna="sarvanāman", case="saptamī",
              result="anadyatana", optional=True,
              excepts=("5.3.15",),
              why="अनद्यतने र्हिलन्यतरस्याम् — of a time NOT of "
                  "today. **छन्दसीति न स्वर्यते; सामान्येन "
                  "विधानम्** — the Veda-restriction of the rule "
                  "before is not carried, so this holds "
                  "generally. **कर्हि, कदा; यर्हि, यदा; तर्हि, "
                  "तदा**"),
    Svarthika("5.3.22", nipatana=True, gana="sadyaḥprabhṛti",
              case="saptamī", result="kāla",
              why="सद्यःपरुत्परार्यैषमःपरेद्यव्यद्यपूर्वेद्युर्…"
                  "उत्तरेद्युः. **सद्यःप्रभृतयः शब्दा "
                  "निपात्यन्ते** — eighteen forms laid down, and the "
                  "vṛtti says how much comes from the laying-down: "
                  "**प्रकृतिः, प्रत्ययः, आदेशः, कालविशेष इति "
                  "सर्वमेतद् निपातनाद् लभ्यते** — base, affix, "
                  "substitution AND the particular time, all four "
                  "from the निपातन.\\n\\n"
                  "समानेऽहनि **सद्यः**, today; पूर्वस्मिन् "
                  "संवत्सरे **परुत्**, last year; पूर्वतरे "
                  "संवत्सरे **परारी**, the year before; अस्मिन् "
                  "संवत्सरे **ऐषमः**, this year; परस्मिन्नहनि "
                  "**परेद्यवि**, tomorrow; अस्मिन्नहनि **अद्य**, "
                  "today; and then eight in एद्युस् — **पूर्वेद्युः, "
                  "अन्येद्युः, अन्यतरेद्युः, इतरेद्युः, "
                  "अपरेद्युः, अधरेद्युः, उभयेद्युः, उत्तरेद्युः**. "
                  "**द्युश्चोभयाद् वक्तव्यः** — उभयद्युः"),
    Svarthika("5.3.23", gives="thāl", of=("kim", "bahu"),
              of_samjna="sarvanāman", result="prakāra",
              why="प्रकारवचने थाल् — of the MANNER of a thing. "
                  "**कथा, यथा, तथा**"),
    Svarthika("5.3.24", gives="thamu", of=("idam",),
              adesa="ita", result="prakāra", excepts=("5.3.23",),
              why="इदमस्थमुः. **इत्थम्** — with 5.3.4's इत्, the "
                  "affix beginning with थ"),
    Svarthika("5.3.25", gives="thamu", of=("kim",),
              result="prakāra", excepts=("5.3.23",),
              why="किमश्च. **कथम्**"),
    Svarthika("5.3.26", gives="thā", of=("kim",), result="hetu",
              usage="chandasi",
              why="था हेतौ च छन्दसि — and with it the विभक्ति "
                  "section closes. From किम् in the sense of a "
                  "CAUSE, in the Veda"),
    Svarthika("5.3.27", gives="astāti", of_samjna="dikśabda",
              case="saptamī-pañcamī-prathamā",
              result="dik-deśa-kāla",
              why="दिक्शब्देभ्यः सप्तमीपञ्चमीप्रथमाभ्यो "
                  "दिग्देशकालेष्वस्तातिः — the marker, and the "
                  "sūtra whose word दिक् bounded the whole section "
                  "before it. From the words for the QUARTERS, in "
                  "three cases, of a quarter or a place or a time"),
    Svarthika("5.3.28", gives="atasuc", of=("dakṣiṇa", "uttara"),
              case="saptamī-pañcamī-prathamā", result="dik-deśa",
              excepts=("5.3.27",),
              why="दक्षिणोत्तराभ्यामतसुच्, **अस्तातेरपवादः**. "
                  "**दक्षिणतो वसति, दक्षिणत आगतः, दक्षिणतो "
                  "रमणीयम्** — one form for all three cases, which "
                  "is what a स्वार्थिक affix does.\n\n"
                  "**दक्षिणाशब्दः काले न संभवतीति दिग्देशवृत्तिः "
                  "परिगृह्यते** — *south* cannot be said of a TIME, "
                  "so only the quarter and the place are taken here, "
                  "though 5.3.27 named three. "
                  "**अकारो विशेषणार्थः** — and the अ of the affix's "
                  "name is there for 2.3.30 षष्ठ्यतसर्थप्रत्ययेन"),
    Svarthika("5.3.29", gives="tasuc", of=("para", "avara"),
              optional=True, case="saptamī-pañcamī-prathamā",
              excepts=("5.3.27",),
              why="विभाषा परावराभ्याम् — optionally, so the "
                  "अस्ताति of 5.3.27 stands in the other half. "
                  "**परतो वसति** beside **परस्ताद् वसति**; "
                  "अवरतो वसति beside अवस्ताद् वसति"),
    Svarthika("5.3.30", of_samjna="añcanta", adesa="luk",
              case="saptamī-pañcamī-prathamā",
              excepts=("5.3.27",),
              why="अञ्चेर्लुक् — the अस्ताति is REMOVED after the "
                  "quarter-words ending in अञ्च्. प्राच्यां दिशि "
                  "वसति → **प्राग् वसति**; प्रत्यग् वसति.\n\n"
                  "**लुक् तद्धितलुकि इति स्त्रीप्रत्ययोऽपि "
                  "निवर्तते** (1.2.49) — and when a taddhita goes "
                  "by लुक् the feminine affix goes with it, which "
                  "is why it is प्राग् and not प्राची"),
    Svarthika("5.3.31", nipatana=True, gives="ril",
              also_gives=("riṣṭātil",), of=("ūrdhva",),
              adesa="upa", case="saptamī-pañcamī-prathamā",
              why="उपर्युपरिष्टात् — two forms laid down. "
                  "**ऊर्ध्वस्योपभावो रिल्रिष्टातिलौ च प्रत्ययौ "
                  "निपात्येते**: ऊर्ध्वायां दिशि वसति → **उपरि "
                  "वसति**, **उपरिष्टाद् वसति**"),
    Svarthika("5.3.32", nipatana=True, gives="āti", of=("apara",),
              adesa="paśca", case="saptamī-pañcamī-prathamā",
              why="पश्चात्. **पश्चादित्ययं शब्दो निपात्यते**; "
                  "**अपरस्य पश्चभाव आतिश्च प्रत्ययः**. "
                  "अपरस्यां दिशि वसति → **पश्चाद् वसति**.\n\n"
                  "Three vārttikas widen it: **दिक्पूर्वपदस्य "
                  "अपरस्य पश्चभावो वक्तव्यः, आतिश्च प्रत्ययः** — "
                  "दक्षिणपश्चात्, उत्तरपश्चात्; "
                  "**अर्धोत्तरपदस्य दिक्पूर्वपदस्य पश्चभावः** — "
                  "दक्षिणपश्चार्धः; **विनापि पूर्वपदेन पश्चभावः** "
                  "— पश्चार्धः"),
    Svarthika("5.3.33", nipatana=True, gives="a", also_gives=("ā",),
              of=("apara",), adesa="paśca", usage="chandasi",
              case="saptamī-pañcamī-prathamā",
              why="पश्च पश्चा च छन्दसि. **पश्चपश्चाशब्दौ निपात्येते** "
                  "— **चकारात् पश्चादित्यपि "
                  "भवति**, so three forms. "
                  "**अपरस्य पश्चभावोऽकाराकारौ च प्रत्ययौ "
                  "निपात्येते**: पुरा व्याघ्रो जायते **पश्च "
                  "सिंहः**; **पश्चा सिंहः**; पश्चात् सिंहः"),
    Svarthika("5.3.34", gives="āti",
              of=("uttara", "adhara", "dakṣiṇa"),
              case="saptamī-pañcamī-prathamā",
              excepts=("5.3.27",),
              why="उत्तराधरदक्षिणादातिः. उत्तरस्यां दिशि वसति "
                  "**उत्तराद् वसति**; अधराद् वसति; दक्षिणाद् वसति"),
    Svarthika("5.3.35", gives="enap",
              of=("uttara", "adhara", "dakṣiṇa"), optional=True,
              case="saptamī-prathamā", result="adūra",
              excepts=("5.3.34",),
              why="एनबन्यतरस्यामदूरेऽपञ्चम्याः — and both of the "
                  "conditions are new. **अदूरे** — only where the "
                  "measure from the point of reference is NOT FAR; "
                  "**अपञ्चम्याः** — and not from an ablative, so "
                  "**प्रकृतेऽपि पञ्चमी पर्युदस्यते; तेनायं "
                  "सप्तमीप्रथमान्ताद् विज्ञायते प्रत्ययः**, the "
                  "affix comes from the locative and nominative "
                  "only.\n\n"
                  "**उत्तरेण वसति**, beside उत्तराद् वसति and "
                  "उत्तरतो वसति — three forms. **अदूर इति किम्?** "
                  "उत्तराद् वसति. **अपञ्चम्या इति किम्?** "
                  "उत्तरादागतः.\n\n"
                  "**अपञ्चम्या इति प्रागसेः** — the exclusion runs "
                  "only as far as 5.3.39, **असिप्रत्ययस्तु "
                  "पञ्चम्यन्तादपि भवति**. And "
                  "**केचिदिहोत्तरादिग्रहणं नानुवर्तयन्ति; "
                  "दिक्छब्दमात्रात् प्रत्ययं मन्यन्ते** — some do "
                  "not carry the three words down and give the "
                  "affix after any quarter-word: **पूर्वेण "
                  "ग्रामम्**",
              keeps_out="उत्तराद् वसति, उत्तरादागतः"),
    Svarthika("5.3.36", gives="āc", of=("dakṣiṇa",),
              case="saptamī-prathamā", excepts=("5.3.34",),
              why="दक्षिणादाच्. **अदूर इति न स्वर्यते** — the "
                  "*not far* of the rule before is NOT carried, "
                  "and **अपञ्चम्या इति वर्तते** is. **दक्षिणा "
                  "वसति, दक्षिणा रमणीयम्**. **अपञ्चम्या इत्येव** — "
                  "दक्षिणत आगतः. **चकारो विशेषणार्थः** for 2.3.29 "
                  "अञ्चूत्तरपदाजाहियुक्ते",
              keeps_out="दक्षिणत आगतः"),
    Svarthika("5.3.37", gives="āhi", also_gives=("āc",),
              of=("dakṣiṇa",), case="saptamī-prathamā",
              result="dūra", excepts=("5.3.34",),
              why="आहि च दूरे — and now the OPPOSITE condition, "
                  "**दूरे चेदवधिमानवधेर्भवति**, where the measure "
                  "from the reference point IS far. "
                  "**दक्षिणाहि वसति, दक्षिणा वसति**. "
                  "**दूर इति किम्?** दक्षिणतो वसति",
              keeps_out="दक्षिणतो वसति"),
    Svarthika("5.3.38", gives="āc", also_gives=("āhi",),
              of=("uttara",), case="saptamī-prathamā",
              result="dūra", excepts=("5.3.34",),
              why="उत्तराच्च. **उत्तरा वसति, उत्तराहि वसति**. "
                  "**दूर इत्येव** — उत्तरेण प्रयाति. "
                  "**अपञ्चम्या इत्येव** — उत्तरादागतः",
              keeps_out="उत्तरेण प्रयाति"),
    Svarthika("5.3.39", gives="asi",
              of=("pūrva", "adhara", "avara"),
              adesa="pur-adh-av",
              case="saptamī-pañcamī-prathamā",
              excepts=("5.3.27",),
              why="पूर्वाधरावराणामसि पुरधवश्चैषाम्, "
                  "**यथासंख्यम्** — the affix and three substitutes "
                  "yoked to it. **अपञ्चम्या इति निवृत्तम्; "
                  "तिसृणां विभक्तीनामिह ग्रहणम्** — the exclusion "
                  "of the ablative lapses here, and all three cases "
                  "are taken. **असीत्यविभक्तिको निर्देशः**.\n\n"
                  "**पुरो वसति, पुर आगतः, पुरो रमणीयम्**; अधो "
                  "वसति; अवो वसति"),
    Svarthika("5.3.40", adesa="pur-adh-av",
              of=("pūrva", "adhara", "avara"), before="astāti",
              case="saptamī-pañcamī-prathamā",
              why="अस्ताति च — the same three substitutes before "
                  "the अस्ताति of 5.3.27. **पुरस्ताद् वसति, "
                  "अधस्ताद् वसति**.\n\n"
                  "**इदमेवादेशविधानं ज्ञापकम् — अस्तातिरेभ्यो "
                  "भवति, असिप्रत्ययेन न बाध्यत इति** — that a "
                  "substitute is enjoined before the अस्ताति is the "
                  "evidence that these three DO take the अस्ताति, "
                  "and that the असि of the rule before does not "
                  "displace it. The ज्ञापक device again"),
    Svarthika("5.3.41", adesa="av", of=("avara",),
              before="astāti", optional=True,
              case="saptamī-pañcamī-prathamā",
              excepts=("5.3.40",),
              why="विभाषावरस्य — **पूर्वेण नित्ये प्राप्ते "
                  "विकल्प उच्यते**, what the rule before made "
                  "obligatory becomes a choice for one of the three. "
                  "**अवस्ताद् वसति, अवरस्ताद् वसति**"),
    Svarthika("5.3.42", gives="dhā", of_samjna="saṃkhyā",
              result="vidhā",
              why="संख्याया विधार्थे धा — and with it the "
                  "quarter-words are done and the NUMERALS begin. "
                  "**विधा प्रकारः, स च सर्वक्रियाविषय एव "
                  "गृह्यते** — a विधा is a manner, and it is taken "
                  "of any action whatever. **एकधा भुङ्क्ते, "
                  "द्विधा गच्छति**; त्रिधा, चतुर्धा, पञ्चधा"),
    Svarthika("5.3.43", gives="dhā", of_samjna="saṃkhyā",
              result="adhikaraṇavicāla",
              why="अधिकरणविचाले च — a second sense for the same "
                  "affix. **अधिकरणं द्रव्यम्, तस्य विचालः "
                  "संख्यान्तरापादनम्; एकस्यानेकीकरणम् अनेकस्य वा "
                  "एकीकरणम्** — a substance being brought to a "
                  "different number, one made many or many made "
                  "one. **एकं राशिं पञ्चधा कुरु**; अनेकम् "
                  "**एकधा कुरु**"),
    Svarthika("5.3.44", gives="dhā", adesa="dhyamuñ", of=("eka",),
              of_samjna="saṃkhyā", optional=True,
              excepts=("5.3.42",),
              why="एकाद् धो ध्यमुञन्यतरस्याम् — a substitute for "
                  "the affix after एक. **एकधा राशिं कुरु, "
                  "**ऐकध्यं** कुरु; एकधा भुङ्क्ते, ऐकध्यं "
                  "भुङ्क्ते.\n\n"
                  "**प्रकरणादेव लब्धे पुनर्धाग्रहणं विधार्थे "
                  "विहितस्यापि यथा स्यात्; अनन्तरस्यैव ह्येतत् "
                  "प्राप्नोति** — the affix is named again though "
                  "the section supplies it, so that the धा of the "
                  "*manner* rule is reached too and not only the "
                  "one just before"),
    Svarthika("5.3.45", gives="dhā", adesa="dhamuñ",
              of=("dvi", "tri"), of_samjna="saṃkhyā",
              optional=True, excepts=("5.3.42",),
              why="द्वित्र्योश्च धमुञ् — **चकारो "
                  "विकल्पानुकर्षणार्थः**, the च dragging the option "
                  "down. **द्विधा, द्वैधम्; त्रिधा, त्रैधम्**.\n\n"
                  "**धमुञन्तात् स्वार्थे डदर्शनम्** — and a "
                  "vārttika adds a further affix in the same sense "
                  "on top of that: **मतिद्वैधानि संश्रयन्ते**"),
    Svarthika("5.3.46", gives="dhā", adesa="edhāc",
              of=("dvi", "tri"), of_samjna="saṃkhyā",
              optional=True, excepts=("5.3.42",),
              why="एधाच्च — a third substitute, so three forms "
                  "apiece: **द्वेधा, द्वैधम्, द्विधा**; त्रेधा, "
                  "त्रैधम्, त्रिधा"),
    Svarthika("5.3.47", gives="pāśap", result="yāpya",
              why="याप्ये पाशप् — **याप्यः कुत्सित इत्युच्यते**, "
                  "in CONTEMPT. याप्यो वैयाकरणः "
                  "**वैयाकरणपाशः**; याज्ञिकपाशः.\n\n"
                  "**यो व्याकरणशास्त्रे प्रवीणो दुःशीलः, तत्र "
                  "कस्माद् न भवति?** Why not of a grammarian who is "
                  "skilled but ill-behaved? **यस्य गुणस्य "
                  "सद्भावाद् द्रव्ये शब्दनिवेशः, तस्य कुत्सायां "
                  "प्रत्ययः** — the affix is for contempt of the "
                  "QUALITY the word is applied for, and there the "
                  "contempt is of something else",
              keeps_out="a grammarian contemptible for other reasons"),
    Svarthika("5.3.48", gives="an", of_samjna="tīyānta",
              result="bhāga", excepts=("5.3.42",),
              why="पूरणाद् भागे तीयादन् — from a word ending in the "
                  "ordinal affix तीय, in the sense of a SHARE. "
                  "**स्वरार्थं वचनम्** — the rule is for the accent "
                  "and nothing else, the affix adding no meaning. "
                  "द्वितीयो भागो **द्वितीयः**; तृतीयः. "
                  "**भाग इति किम्?** द्वितीयम्, तृतीयम्.\n\n"
                  "**पूरणग्रहणमुत्तरार्थम्, न ह्यपूरणस्तीयोऽस्ति; "
                  "मुखतीयादिरनर्थकः** — and the word *ordinal* is "
                  "there only for the NEXT rule, since there is no "
                  "तीय that is not an ordinal",
              keeps_out="द्वितीयम्, तृतीयम्"),
    Svarthika("5.3.49", gives="an", of_samjna="pūraṇānta",
              result="bhāga", usage="abhāṣā", excepts=("5.3.48",),
              why="प्रागेकादशभ्योऽच्छन्दसि — from the ordinals of "
                  "the numbers BELOW ELEVEN, outside the Veda. "
                  "**स्वरार्थं वचनम्** again. **पञ्चमः, सप्तमः, "
                  "नवमः, दशमः**.\n\n"
                  "**प्रागेकादशभ्य इति किम्?** एकादशः, द्वादशः. "
                  "**अच्छन्दसीति किम्?** त॑स्य॒ **पञ्च॒म॑म्** "
                  "इ॒न्द्रि॒य॑स्या॑पा॒क्राम॒त् (मै०सं० १.९.४)",
              keeps_out="एकादशः, द्वादशः"),
    Svarthika("5.3.50", gives="ña", also_gives=("an",),
              of=("ṣaṣṭha", "aṣṭama"), result="bhāga",
              usage="abhāṣā", excepts=("5.3.49",),
              why="षष्ठाष्टमाभ्यां ञ च — **चकारादन् च**, so both. "
                  "षष्ठो भागः **षाष्ठः, षष्ठः**; आष्टमः, अष्टमः"),
    Svarthika("5.3.51", gives="kan", of=("ṣaṣṭha",),
              result="māna", excepts=("5.3.50",),
              why="मानपश्वङ्गयोः कन्लुकौ च, **यथासंख्यम्**; the "
                  "षष्ठ member, of a MEASURE. **षष्ठको भागो मानं "
                  "चेत् तद् भवति**. **चकाराद् यथाप्राप्तं च**, so "
                  "षाष्ठः and षष्ठः stand too. "
                  "**मानपश्वङ्गयोरिति किम्?** षाष्ठः, षष्ठः"),
    Svarthika("5.3.51", adesa="luk", of=("aṣṭama",),
              result="paśvaṅga", excepts=("5.3.50",),
              why="मानपश्वङ्गयोः कन्लुकौ च, the अष्टम member, of a "
                  "PART OF A BEAST — and here the affix is removed. "
                  "**कस्य लुक्? ञस्य लुक्, अनो वा** — and which "
                  "affix goes is left open, either of the two the "
                  "rule before gave"),
    Svarthika("5.3.52", gives="ākinic", also_gives=("kan",),
              of=("eka",), result="asahāya", optional=True,
              why="एकादाकिनिच्चासहाये — **चकारात् कन्लुकौ च**, and "
                  "**आकिनिचः कनो वा लुग् विज्ञायते; स च "
                  "विधानसामर्थ्यात् पक्षे भवति**: three forms, "
                  "**एकाकी, एककः, एकः**.\n\n"
                  "**असहायग्रहणं संख्याशब्दनिरासार्थम्; "
                  "तदुपादाने हि द्विबह्वोर्न स्यात्** — *without a "
                  "companion* is said to keep the NUMERAL sense "
                  "out, since a numeral एक would let द्वि and बहु "
                  "in too. एकाकिनौ, एकाकिनः"),
    Svarthika("5.3.53", gives="caraṭ", result="bhūtapūrva",
              why="भूतपूर्वे चरट्. **भूतपूर्वशब्दोऽतिक्रान्तकाल"
                  "वचनः; प्रकृतिविशेषणं चैतत्** — *formerly so* "
                  "describes the BASE. आढ्यो भूतपूर्व **आढ्यचरः**, "
                  "once rich; सुकुमारचरः. **टकारो ङीबर्थः** — "
                  "आढ्यचरी"),
    Svarthika("5.3.54", gives="rūpya", also_gives=("caraṭ",),
              case="ṣaṣṭhī", result="bhūtapūrva",
              excepts=("5.3.53",),
              why="षष्ठ्या रूप्य च — and here the *formerly* has "
                  "moved. **षष्ठ्यन्तात् प्रत्ययविधानात् संप्रति "
                  "भूतपूर्वग्रहणं प्रत्ययार्थस्य विशेषणम्, न तु "
                  "प्रकृत्यर्थविशेषणम्** — because the affix now "
                  "comes after a GENITIVE, *formerly* describes what "
                  "the affix reports and not the base. देवदत्तस्य "
                  "भूतपूर्वो गौर् **देवदत्तरूप्यः**, once "
                  "Devadatta's; **देवदत्तचरः**"),
    Svarthika("5.3.55", gives="tamap", also_gives=("iṣṭhan",),
              result="atiśāyana",
              why="अतिशायने तमबिष्ठनौ — the SUPERLATIVE. "
                  "**अतिशयनमतिशायनम्, प्रकर्षः; निपातनाद् "
                  "दीर्घत्वम्**. सर्व इम आढ्याः, अयमेषामतिशयेन "
                  "आढ्यः **आढ्यतमः**; सर्व इमे पटवः, अयमेषाम् "
                  "अतिशयेन पटुः **पटिष्ठः**, लघिष्ठः, गरिष्ठः.\n\n"
                  "**AND THE VṚTTI STATES WHAT A स्वार्थिक AFFIX "
                  "DOES.** **प्रकृत्यर्थविशेषणं च स्वार्थिकानां "
                  "द्योत्यं भवति** — a qualification of the base's "
                  "own meaning is what these affixes MAKE MANIFEST, "
                  "rather than adding anything.\n\n"
                  "**यदा च प्रकर्षवतां पुनः प्रकर्षो विवक्ष्यते, "
                  "तदा अतिशायिकान्तादपरः प्रत्ययो भवत्येव** — and "
                  "where excellent things are compared again, a "
                  "second superlative comes on top of the first: "
                  "**श्रेष्ठतमाय क॑र्मणे॒**; युधिष्ठिरः **श्रेष्ठतमः** "
                  "कुरूणाम्"),
    Svarthika("5.3.56", gives="tamap", of_samjna="tiṅanta",
              result="atiśāyana",
              why="तिङश्च — and after a FINITE VERB, which needed "
                  "saying: **ङ्याप्प्रातिपदिकात् इत्यधिकारात् "
                  "तिङो न प्राप्नोतीतीदं वचनम्** (4.1.1), the whole "
                  "taddhita section being for nominal stems. सर्व "
                  "इमे पचन्ति, अयमेषामतिशयेन पचति **पचतितमाम्**; "
                  "जल्पतितमाम्.\n\n"
                  "**इष्ठन् नोदाह्रियते, गुणवचने तस्य नियतत्वात्** "
                  "— and the other affix is not exemplified here, "
                  "because 5.3.58 confines it to quality-words"),
    Svarthika("5.3.57", gives="tarap", also_gives=("īyasun",),
              result="dvivacana-vibhajya", excepts=("5.3.55",),
              why="द्विवचनविभज्योपपदे तरबीयसुनौ — the COMPARATIVE, "
                  "**तमबिष्ठनोरपवादौ**. **द्वयोरर्थयोर्वचनं "
                  "द्विवचनम्; विभक्तव्यो विभज्यः** — where a word "
                  "for TWO stands by, or one that DIVIDES.\n\n"
                  "**यथासंख्यमत्र नेष्यते** — and the two affixes "
                  "are not matched to the two conditions. द्वाविमौ "
                  "आढ्यौ, अयमनयोरतिशयेन आढ्यः **आढ्यतरः**; "
                  "पचतितराम्; **पटीयान्**, लघीयान्. And with a "
                  "dividing word: माथुराः पाटलिपुत्रकेभ्य "
                  "**आढ्यतराः**, पटीयांसः"),
    Svarthika("5.3.58", gives="iṣṭhan", also_gives=("īyasun",),
              of_samjna="guṇavacana", result="atiśāyana",
              excepts=("5.3.55",),
              why="अजादी गुणवचनादेव — a NIYAMA and not a विधि. "
                  "**इष्ठन्नीयसुनावजादी सामान्येन विहितौ, तयोरयं "
                  "विषयनियमः क्रियते — गुणवचनादेव भवतस्तौ, "
                  "नान्यस्मादिति**: the two vowel-initial affixes "
                  "were given generally and are here CONFINED to "
                  "quality-words. **पटीयान्, पटिष्ठः**; "
                  "**इह न भवतः — पाचकतरः, पाचकतमः**.\n\n"
                  "**एवकार इष्टतोऽवधारणार्थः, प्रत्ययनियमोऽयं न "
                  "प्रकृतिनियम इति** — and the *only* restricts the "
                  "AFFIX and not the base, so a quality-word may "
                  "still take the others: **पटुतरः, पटुतमः**",
              keeps_out="पाचकतरः, पाचकतमः"),
    Svarthika("5.3.59", gives="iṣṭhan", also_gives=("īyasun",),
              of_samjna="tṛnanta", usage="chandasi",
              result="atiśāyana", excepts=("5.3.58",),
              why="तुश्छन्दसि — **तुरिति तृन्तृचोः सामान्येन "
                  "ग्रहणम्**. **पूर्वेण गुणवचनादेव नियमे कृते "
                  "छन्दसि प्रकृत्यन्तराण्यभ्यनुज्ञायन्ते** — the "
                  "restriction just made is loosened for the Veda, "
                  "and other bases are let in. आसु॒तिं "
                  "**करि॑ष्ठः**; **दोहीयसी** धेनुः"),
    Svarthika("5.3.60", adesa="śra", of=("praśasya",),
              before="ajādi", result="atiśāyana",
              why="प्रशस्यस्य श्रः — a substitute before the two "
                  "vowel-initial affixes. **श्रेष्ठः, श्रेयान्**.\n\n"
                  "**AND THE SUBSTITUTION UNDOES THE RESTRICTION "
                  "JUST MADE.** **ननु च प्रशस्यशब्दस्य "
                  "अगुणवचनत्वाद् अजादी न संभवतः?** प्रशस्य is not "
                  "a quality-word, so by 5.3.58 those affixes "
                  "cannot come after it at all. **एवं तर्हि "
                  "आदेशविधानसामर्थ्यात् तद्विषयो नियमो न "
                  "प्रवर्तते** — the force of a substitute being "
                  "enjoined before them is that the restriction "
                  "does not reach here. **एवमुत्तरेष्वपि योगेषु "
                  "विज्ञेयम्**, and the same holds of the rules "
                  "after this one"),
    Svarthika("5.3.61", adesa="jya", of=("praśasya",),
              before="ajādi", result="atiśāyana",
              excepts=("5.3.60",),
              why="ज्य च — a second substitute for the same word. "
                  "**ज्येष्ठः, ज्यायान्**. 6.4.160 ज्यादादीयसः "
                  "gives the आ"),
    Svarthika("5.3.62", adesa="jya", of=("vṛddha",),
              before="ajādi", result="atiśāyana",
              why="वृद्धस्य च — the same substitute for another "
                  "word. **ज्येष्ठः, ज्यायान्**, and "
                  "**तयोश्च सत्त्वं नियमाभावेन पूर्ववद् ज्ञाप्यते** "
                  "— that the affixes come at all is again read out "
                  "of the substitution.\n\n"
                  "**प्रियस्थिर० इत्यादिना वृद्धशब्दस्य "
                  "वर्षादेशो विधीयते; वचनसामर्थ्यात् पक्षे सोऽपि "
                  "भवति** (6.4.157) — and वर्ष is a substitute too, "
                  "so **वर्षिष्ठः, वर्षीयान्** stand beside"),
    Svarthika("5.3.63", adesa="neda", of=("antika",),
              before="ajādi", result="atiśāyana",
              why="अन्तिकबाढयोर्नेदसाधौ, **यथासंख्यम्**; the "
                  "अन्तिक member. **निमित्तयोर्यथासंख्यमत्र "
                  "नेष्यते**. **नेदिष्ठम्, नेदीयः**"),
    Svarthika("5.3.63", adesa="sādha", of=("bāḍha",),
              before="ajādi", result="atiśāyana",
              why="अन्तिकबाढयोर्नेदसाधौ, the बाढ member. सर्व इमे "
                  "बाढमधीयते, अयमेषामतिशयेन बाढमधीते "
                  "**साधिष्ठम्**; **साधीयः**"),
    Svarthika("5.3.64", adesa="kan", of=("yuvan", "alpa"),
              before="ajādi", result="atiśāyana", optional=True,
              why="युवाल्पयोः कनन्यतरस्याम् — optionally, so both "
                  "sets stand. **कनिष्ठः, कनीयान्**, and "
                  "**यविष्ठः, यवीयान्** beside them; and of अल्प, "
                  "कनिष्ठः, कनीयान्, **अल्पिष्ठः, अल्पीयान्**"),
    Svarthika("5.3.65", adesa="luk", of_samjna="vin-matvanta",
              before="ajādi", result="atiśāyana",
              why="विन्मतोर्लुक् — the possessive affix is REMOVED "
                  "before the two. **इदमेव वचनं ज्ञापकम् "
                  "अजादिसद्भावस्य** — and that its removal is "
                  "enjoined here is the evidence that those affixes "
                  "come after such words at all, which 5.3.58 had "
                  "seemed to forbid. The third time in six rules.\n\n"
                  "सर्व इमे स्रग्विणः, अयमेषामतिशयेन स्रग्वी "
                  "**स्रजिष्ठः, स्रजीयान्**; त्वग्वान् "
                  "**त्वचिष्ठः, त्वचीयान्**"),
    Svarthika("5.3.66", gives="rūpap", result="praśaṃsā",
              why="प्रशंसायां रूपप् — in PRAISE. **प्रशंसा "
                  "स्तुतिः**. प्रशस्तो वैयाकरणो "
                  "**वैयाकरणरूपः**.\n\n"
                  "**स्वार्थिकाश्च प्रत्ययाः प्रकृत्यर्थविशेषस्य "
                  "द्योतका भवन्ति; प्रकृत्यर्थस्य वैशिष्ट्ये "
                  "प्रशंसा भवति** — and the praise may be bitter: "
                  "**वृषलरूपोऽयम्, यः पलाण्डुना सुरां पिबति**, a "
                  "fine sort of low fellow, who drinks his liquor "
                  "with onions; **चोररूपः, दस्युरूपः, योऽक्ष्णोरपि "
                  "अञ्जनं हरेत्**, who would steal the very "
                  "collyrium off your eyes.\n\n"
                  "**तिङश्चेत्यनुवर्तते** — and after a finite verb "
                  "too: **पचतिरूपम्**. **क्रियाप्रधानम् आख्यातम्; "
                  "एका च क्रियेति रूपप्प्रत्ययान्ताद् "
                  "द्विवचनबहुवचने न भवतः; नपुंसकलिङ्गं तु भवति, "
                  "लोकाश्रयत्वाल् लिङ्गस्य** — an action is one, so "
                  "no dual or plural; but the gender is neuter, "
                  "gender resting on usage"),
    Svarthika("5.3.67", gives="kalpab",
              also_gives=("deśya", "deśīyar"),
              result="īṣadasamāpti",
              why="ईषदसमाप्तौ कल्पब्देश्यदेशीयरः — ALMOST, and the "
                  "vṛtti defines it: **संपूर्णता पदार्थानां "
                  "समाप्तिः; स्तोकेनासंपूर्णता ईषदसमाप्तिः**. "
                  "ईषदसमाप्तः पटुः **पटुकल्पः, पटुदेश्यः, "
                  "पटुदेशीयः**. **तिङश्चेत्येव** — पचतिकल्पम्"),
    Svarthika("5.3.68", gives="bahuc", of_samjna="subanta",
              result="īṣadasamāpti", optional=True,
              excepts=("5.3.67",),
              why="विभाषा सुपो बहुच् पुरस्तात्तु — and the affix "
                  "goes IN FRONT. **स तु पुरस्तादेव भवति न "
                  "परतः**. **बहुपटुः, बहुमृदुः**; बहुगुडो "
                  "द्राक्षा. **चित्करणमन्तोदात्तार्थम्**.\n\n"
                  "**विभाषावचनात् कल्पबादयोऽपि भवन्ति** — the "
                  "option lets the affixes of the rule before "
                  "stand. **सुब्ग्रहणं तिङन्ताद् मा भूदिति** — and "
                  "*from a case-form* is said so that a finite verb "
                  "is NOT reached, though the rule before reached "
                  "one",
              keeps_out="a finite verb"),
    Svarthika("5.3.69", gives="jātīyar", of_samjna="subanta",
              result="prakāra",
              why="प्रकारवचने जातीयर् — of a KIND. **सामान्यस्य "
                  "भेदको विशेषः प्रकारः**. पटुप्रकारः "
                  "**पटुजातीयः**; मृदुजातीयः.\n\n"
                  "**प्रकारवति चायं प्रत्ययः; थाल् पुनः "
                  "प्रकारमात्र एव भवति** — and this affix is for "
                  "what HAS a kind, where 5.3.23's थाल् was for the "
                  "kind itself. The same word प्रकार in two rules "
                  "of one pāda, and the vṛtti divides them"),
    Svarthika("5.3.70", gives="ka", heading=True,
              why="प्रागिवात्कः — a heading, and this one DOES "
                  "supply an affix. **इवे प्रतिकृतौ इति वक्ष्यति। "
                  "प्रागेतस्मादिवसंशब्दनाद् यानित "
                  "ऊर्ध्वमनुक्रमिष्यामः, कप्रत्ययस्तेष्वधिकृतो "
                  "वेदितव्यः** — क for every sense named between "
                  "here and 5.3.96, the seventh heading bounded by "
                  "lifting a word out of the rule it stops at. "
                  "**अश्वकः, गर्दभकः**.\n\n"
                  "**तिङन्तादयं प्रत्ययो नेष्यते, अकजिष्यते** — "
                  "and after a FINITE VERB this affix is not "
                  "wanted; the next rule's अकच् comes instead. "
                  "**तिङश्च इत्यनुवृत्तम् उत्तरसूत्रेणैव "
                  "संबन्धनीयम्** — so the *and after a finite verb* "
                  "carried down from 5.3.56 attaches to 5.3.71 and "
                  "not to this rule",
              keeps_out="a finite verb"),
    Svarthika("5.3.71", gives="akac", of_samjna="avyaya-sarvanāman",
              excepts=("5.3.70",),
              why="अव्ययसर्वनाम्नामकच् प्राक् टेः, **कस्यापवादः** "
                  "— and the affix goes INSIDE the word, before its "
                  "last vowel and consonant: **स च प्राक् टेः, न "
                  "परतः**. **उच्चकैः, नीचकैः, शनकैः**; "
                  "**सर्वके, विश्वके, उभयके**.\n\n"
                  "**AND WHETHER IT ENTERS THE STEM OR THE INFLECTED "
                  "WORD IS DECIDED BY USAGE.** **प्रातिपदिकात् सुप "
                  "इति द्वयमपीहानुवर्तते; तत्राभिधानतो व्यवस्था "
                  "भवति** — both headings are running, and which "
                  "applies is settled by what the language actually "
                  "says: **युष्मकाभिः, युवकयोः** show it in the "
                  "STEM, **त्वयका, मयका** in the inflected word.\n\n"
                  "**अकच्प्रकरणे तूष्णीमः काम् प्रत्ययो वक्तव्यः** "
                  "— **तूष्णीकामास्ते**; **शीले को मलोपश्च** — "
                  "तूष्णींशीलः, तूष्णीकः. And by the carried "
                  "तिङश्च: **पचतकि, जल्पतकि**"),
    Svarthika("5.3.72", adesa="da", of_samjna="kānta-avyaya",
              before="akac", excepts=("5.3.71",),
              why="कस्य च दः — the final क of the base becomes द "
                  "when the अकच् goes in. **चकारः सन्नियोगार्थः**, "
                  "and **सामर्थ्याच्च अव्ययग्रहणमनुवर्तते, न "
                  "सर्वनामग्रहणम्, ककारान्तस्य सर्वनाम्नोऽसंभवात्** "
                  "— only the indeclinables are carried, there "
                  "being no pronoun ending in क. धिक् → "
                  "**धकित्**; हिरुक् → हिरकुत्; पृथक् → **पृथकत्**"),
    Svarthika("5.3.73", gives="ka", result="ajñāta",
              why="अज्ञाते — of something whose PARTICULARS are not "
                  "known. **अज्ञातविशेषोऽज्ञातः; स्वेन रूपेण "
                  "ज्ञाते पदार्थे विशेषरूपेणाज्ञाते प्रत्ययविधानम् "
                  "एतत्** — the thing itself is known and something "
                  "about it is not. कस्यायमश्व इति "
                  "स्वस्वामिसंबन्धेनाज्ञाते **अश्वकः**, a horse "
                  "whose owner one does not know; गर्दभकः, "
                  "उष्ट्रकः. **एवमन्यत्रापि यथायोगमज्ञातता "
                  "विज्ञेया**"),
    Svarthika("5.3.74", gives="ka", result="kutsita",
              why="कुत्सिते — in CONTEMPT. **कुत्सितो गर्हितो "
                  "निन्दितः; प्रकृत्यर्थविशेषणं चैतत्**. कुत्सितो "
                  "ऽश्वः **अश्वकः**; उष्ट्रकः, गर्दभकः. And "
                  "through the carried rules: उच्चकैः, सर्वके, "
                  "**पचतकि**"),
    Svarthika("5.3.75", gives="kan", result="kutsita-saṃjñā",
              excepts=("5.3.74",),
              why="संज्ञायां कन्, **कस्यापवादः** — where the "
                  "derived word is a NAME, **प्रत्ययान्तेन चेत् "
                  "संज्ञा गम्यते**. **शूद्रकः, धारकः, पूर्णकः**"),
    Svarthika("5.3.76", gives="ka", result="anukampā",
              why="अनुकम्पायाम् — in PITY. **कारुण्येन "
                  "अभ्युपपत्तिः परस्य अनुकम्पा**, taking another's "
                  "part out of tenderness. **पुत्रकः, वत्सकः, "
                  "दुर्बलकः, बुभुक्षितकः**; and of a finite verb, "
                  "**स्वपितकि, श्वसितकि**"),
    Svarthika("5.3.77", gives="ka", result="nīti-tadyukta",
              excepts=("5.3.76",),
              why="नीतौ च तद्युक्तात् — **सामदानादिरुपायो "
                  "नीतिः**, the arts of winning a man over, and "
                  "from what is JOINED to the pitied thing. "
                  "**हन्त ते धानकाः, हन्त ते तिलकाः** — *here, "
                  "take these grains of yours*.\n\n"
                  "**पूर्वेण प्रत्यासन्नानुकम्पासंबन्धाद् "
                  "अनुकम्प्यमानादेव प्रत्ययो विहितः; सम्प्रति "
                  "व्यवहितादपि यथा स्यादिति वचनम्** — the rule "
                  "before reached only the thing pitied itself; "
                  "this reaches what stands at one remove from it"),
    Svarthika("5.3.78", gives="ṭhac", of_samjna="manuṣyanāman",
              result="anukampā-nīti", optional=True,
              excepts=("5.3.76",),
              why="बह्वचो मनुष्यनाम्नष्ठज्वा — from a MAN'S NAME of "
                  "more than two vowels, optionally. "
                  "**देविकः, देवदत्तकः**; यज्ञिकः, यज्ञदत्तकः.\n\n"
                  "**बह्वच इति किम्?** दत्तकः, गुप्तकः. "
                  "**मनुष्यनाम्न इति किम्?** मद्रबाहुकः, "
                  "भद्रबाहुकः",
              keeps_out="दत्तकः, मद्रबाहुकः"),
    Svarthika("5.3.79", gives="ghan", also_gives=("ilac", "ṭhac"),
              of_samjna="manuṣyanāman", result="anukampā-nīti",
              excepts=("5.3.76",),
              why="घनिलचौ च — **चकाराद् यथाप्राप्तं च**, and "
                  "**पूर्वेण ठचि विकल्पेन प्राप्ते वचनम्**, so "
                  "four forms: **देवियः, देविलः, देविकः, "
                  "देवदत्तकः**"),
    Svarthika("5.3.80", gives="aḍ", also_gives=("vuc", "ghan",
                                                "ilac", "ṭhac"),
              of_samjna="manuṣyanāman", pre="upa",
              result="anukampā-nīti", optional=True,
              excepts=("5.3.79",),
              why="प्राचामुपादेरडज्वुचौ च — from a man's name "
                  "beginning with उप, five affixes in all. "
                  "**उपडः, उपकः, उपियः, उपिलः, उपिकः**, and "
                  "उपेन्द्रदत्तकः. **प्राचांग्रहणं पूजार्थम्; "
                  "वेत्येव हि वर्तते** — *of the Eastern teachers* "
                  "is a courtesy and not a condition, the option "
                  "being already running"),
    Svarthika("5.3.81", gives="kan", of_samjna="jātināman",
              result="anukampā-nīti", excepts=("5.3.76",),
              why="जातिनाम्नः कन् — from a man's name that is also "
                  "a KIND-word. **बह्वच इति नानुवर्तते; सामान्येन "
                  "विधानम्** — the two-vowel condition is not "
                  "carried. **व्याघ्रकः, सिंहकः, शरभकः**, and "
                  "**वावचनानुवृत्तेर्यथादर्शनम् अन्योऽपि भवति**: "
                  "व्याघ्रिलः, सिंहिलः. **नामग्रहणं "
                  "स्वरूपनिवृत्त्यर्थम्**"),
    Svarthika("5.3.82", gives="kan", of_samjna="ajinānta",
              adesa="uttarapadalopa", result="anukampā",
              excepts=("5.3.76",),
              why="अजिनान्तस्योत्तरपदलोपश्च — the affix AND the "
                  "loss of the compound's second member. "
                  "**व्याघ्राजिनो नाम कश्चिद् मनुष्यः, सोऽनुकम्पितो "
                  "व्याघ्रकः**; सिंहकः"),
    Svarthika("5.3.83", adesa="dvitīyād-ūrdhvalopa",
              before="ṭha-ajādi", result="anukampā-nīti",
              why="ठाजादावूर्ध्वं द्वितीयादचः — everything above "
                  "the SECOND VOWEL of the base is lost before ठ "
                  "and the vowel-initial affixes. **ऊर्ध्वग्रहणं "
                  "सर्वलोपार्थम्**. अनुकम्पितो देवदत्तो "
                  "**देविकः, देवियः, देविलः**.\n\n"
                  "**ठग्रहणम् उको द्वितीयत्वे कविधानार्थम्** — the "
                  "ठ is named so that a उ or ऋ as second vowel gets "
                  "the क: **वायुदत्तो वायुकः, पितृदत्तः पितृकः**. "
                  "Five vārttikas widen it: "
                  "**चतुर्थादच ऊर्ध्वस्य लोपः** — बृहस्पतिकः; "
                  "**अनजादौ विभाषा लोपः** — देवदत्तकः, देवकः; "
                  "**लोपः पूर्वपदस्य च ठाजादावनजादौ च** — "
                  "**दत्तिकः**; **विनापि प्रत्ययेन पूर्वोत्तरपदयोर् "
                  "विभाषा लोपः** — देवदत्तो **दत्तः, देवः**; "
                  "**उवर्णाल् ल इलस्य च** — भानुदत्तो **भानुलः**, "
                  "and a kārikā sums the five"),
    Svarthika("5.3.84", adesa="tṛtīyād-ūrdhvalopa",
              gana="śevalādi", before="ṭha-ajādi",
              result="anukampā-nīti", excepts=("5.3.83",),
              why="शेवलसुपरिविशालवरुणार्यमादीनां तृतीयात् — from "
                  "the THIRD vowel for these, **पूर्वस्यायम् "
                  "अपवादः**. शेवलदत्तः **शेवलिकः, शेवलियः, "
                  "शेवलिलः**; सुपरिकः, विशालिकः, वरुणिकः, "
                  "अर्यमिकः.\n\n"
                  "**शेवलादीनां तृतीयादचो लोपः स च "
                  "अकृतसन्धीनाम् इति वक्तव्यम्** — and the count is "
                  "taken BEFORE sandhi has been made: "
                  "शेवलेन्द्रदत्तः gives शेवलिकः and not "
                  "**शेवलयिकः**",
              keeps_out="शेवलयिकः, सुपर्यिकः"),
    Svarthika("5.3.85", gives="ka", result="alpa",
              why="अल्पे — of what is SMALL. **परिमाणापचयेऽल्प"
                  "शब्दः**, a word for a lessening of quantity. "
                  "अल्पं तैलं **तैलकम्**; घृतकम्, सर्वकम्, "
                  "उच्चकैः, **पचतकि**"),
    Svarthika("5.3.86", gives="ka", result="hrasva",
              why="ह्रस्वे — of what is SHORT. **दीर्घप्रतियोगी "
                  "ह्रस्वः**, short being the correlate of long. "
                  "ह्रस्वो वृक्षो **वृक्षकः**; प्लक्षकः, स्तम्भकः"),
    Svarthika("5.3.87", gives="kan", result="hrasva-saṃjñā",
              excepts=("5.3.86",),
              why="संज्ञायां कन् — where the short thing's name is "
                  "made from its shortness, **ह्रस्वत्वहेतुका या "
                  "संज्ञा**. **वंशकः, वेणुकः, दण्डकः**"),
    Svarthika("5.3.88", gives="ra", of=("kuṭī", "śamī", "śuṇḍā"),
              result="hrasva", excepts=("5.3.86",),
              why="कुटीशमीशुण्डाभ्यो रः, **कस्यापवादः**. "
                  "**संज्ञाग्रहणं नानुवर्तते; सामान्येन "
                  "विधानम्**. ह्रस्वा कुटी **कुटीरः**; शमीरः, "
                  "शुण्डारः.\n\n"
                  "**स्वार्थिकत्वेऽपि पुँल्लिङ्गता, लोकाश्रयत्वाल् "
                  "लिङ्गस्य** — though the affix adds no meaning, "
                  "the word turns masculine, gender resting on "
                  "usage and not on the derivation"),
    Svarthika("5.3.89", gives="ḍupac", of=("kutū",),
              result="hrasva", excepts=("5.3.86",),
              why="कुत्वा डुपच्, **कसापवादः**. ह्रस्वा कुतूः "
                  "**कुतुपम्**, **चर्ममयं स्नेहभाजनम् उच्यते**, a "
                  "leather oil-flask; **कुतूरित्यावपनस्याख्या**"),
    Svarthika("5.3.90", gives="ṣṭarac", of=("kāsū", "goṇī"),
              result="hrasva", excepts=("5.3.86",),
              why="कासूगोणीभ्यां ष्टरच्, **कस्यापवादः**. "
                  "**षकारो ङीषर्थः**. ह्रस्वा कासूः "
                  "**कासूतरी**; गोणीतरी. **कासूरिति शक्तिर् "
                  "आयुधविशेष उच्यते**"),
    Svarthika("5.3.91", gives="ṣṭarac",
              of=("vatsa", "ukṣan", "aśva", "ṛṣabha"),
              result="tanutva",
              why="वत्सोक्षाश्वर्षभेभ्यश्च तनुत्वे — **ह्रस्व इति "
                  "निवृत्तम्**, and the sense is now SLIGHTNESS. "
                  "**यस्य गुणस्य हि भावाद् द्रव्ये शब्दनिवेशः, "
                  "तस्य तनुत्वे प्रत्ययः** — the slightness is of "
                  "the quality the word is applied for, and the "
                  "vṛtti works all four out:\n\n"
                  "**प्रथमवया वत्सः, तस्य तनुत्वं "
                  "द्वितीयवयःप्राप्तिः** — **वत्सतरः**, a calf "
                  "less of a calf for being a year older; "
                  "**तरुण उक्षा, तस्य तनुत्वं तृतीयवयःप्राप्तिः** "
                  "— उक्षतरः; **अश्वेनाश्वायामुत्पन्नोऽश्वः, तस्य "
                  "तनुत्वम् अन्यपितृकता** — **अश्वतरः**, a mule, "
                  "less of a horse for having another sire; "
                  "**अनड्वानृषभः, तस्य तनुत्वं भारवहने "
                  "मन्दशक्तिता** — ऋषभतरः, less of a bull for "
                  "drawing poorly"),
    Svarthika("5.3.92", gives="ḍatarac", of=("kim", "yad", "tad"),
              result="nirdhāraṇa-dvayoḥ", optional=True,
              why="किंयत्तदो निर्धारणे द्वयोरेकस्य डतरच् — "
                  "singling ONE OUT OF TWO. **जात्या क्रियया "
                  "गुणेन संज्ञया वा समुदायादेकदेशस्य पृथक्करणं "
                  "निर्धारणम्** — by kind, act, quality or name. "
                  "**कतरो भवतोः कठः**; यतरो भवतोः पटुः; ततर "
                  "आगच्छतु.\n\n"
                  "**महाविभाषया चात्र प्रत्ययो विकल्प्यते** — the "
                  "great option makes it a choice: **को भवतोर् "
                  "देवदत्तः**. **निर्धारण इति विषयसप्तमीनिर्देशः; "
                  "द्वयोरिति समुदायाद् निर्धारणविभक्तिः; एकस्येति "
                  "निर्धार्यमाणनिर्देशः** — each of the three "
                  "words of the rule accounted for"),
    Svarthika("5.3.93", gives="ḍatamac", of=("kim", "yad", "tad"),
              result="nirdhāraṇa-bahūnām", optional=True,
              why="वा बहूनां जातिपरिप्रश्ने डतमच् — one out of "
                  "MANY, where a KIND is asked after. **कतमो "
                  "भवतां कठः**; यतमो भवतां कठः, ततम आगच्छतु.\n\n"
                  "**वावचनमकजर्थम्** — the option is for the अकच् "
                  "of 5.3.71: **यको भवतां कठः, सक आगच्छतु**. "
                  "**जातिपरिप्रश्न इति किम्?** को भवतां देवदत्तः. "
                  "**परिप्रश्नग्रहणं च किम एव विशेषणम्, न "
                  "यत्तदोरसंभवात्; जातिग्रहणं तु सर्वैरेव "
                  "संबध्यते** — the *asking* qualifies किम् alone, "
                  "the *kind* all three",
              keeps_out="को भवतां देवदत्तः"),
    Svarthika("5.3.94", gives="ḍatarac", also_gives=("ḍatamac",),
              of=("eka",), result="nirdhāraṇa", optional=True,
              excepts=("5.3.92",),
              why="एकाच्च प्राचाम् — **चकारो डतरचोऽनुकर्षणार्थः**, "
                  "and **जातिपरिप्रश्न इति नानुवर्तते; सामान्येन "
                  "विधानम्**. **द्वयोर्निर्धारणे डतरच्, बहूनां "
                  "निर्धारणे डतमच्**: एकतरो भवतोर्देवदत्तः, "
                  "**एकतमो भवतां देवदत्तः**. "
                  "**प्राचांग्रहणं पूजार्थम्, विकल्पोऽनुवर्तत एव**"),
    Svarthika("5.3.95", gives="kan", result="avakṣepaṇa",
              excepts=("5.3.70",),
              why="अवक्षेपणे कन् — in REPROACH. **अवक्षिप्यते येन "
                  "तदवक्षेपणम्**. **व्याकरणकेन नाम त्वं "
                  "गर्वितः** — *so it is your GRAMMAR you are proud "
                  "of*.\n\n"
                  "**परस्य कुत्सार्थं यदुपादीयते, तदिहोदाहरणम्; "
                  "यत् पुनः स्वयमेव कुत्सितम्, तत्र कुत्सिते "
                  "इत्यनेन कन् प्रत्ययो भवति** — here the thing "
                  "named is brought in to belittle ANOTHER; where "
                  "the thing itself is contemptible, 5.3.74 gives "
                  "the affix instead. The same affix, and the "
                  "contempt pointing two different ways.\n\n"
                  "**AND THE HEADING CLOSES HERE.** **प्रागिवीयस्य "
                  "पूर्णोऽवधिः** — the seventh time this project "
                  "has met the formula, and the marker 5.3.96 "
                  "stands one sūtra past the last rule"),
    Svarthika("5.3.96", gives="kan", result="iva-pratikṛti",
              why="इवे प्रतिकृतौ — the marker, and the sūtra whose "
                  "word इव bounded the whole क section. "
                  "**इवार्थः सादृश्यम्, तस्य विशेषणं "
                  "प्रतिकृतिग्रहणम्; प्रतिकृतिः प्रतिरूपकं "
                  "प्रतिच्छन्दकम्** — a LIKENESS, and the word "
                  "*image* narrows it to a made likeness. अश्व "
                  "इवायम् अश्वप्रतिकृतिः **अश्वकः**, a horse in "
                  "effigy. **प्रतिकृताविति किम्?** गौरिव गवयः — a "
                  "gayal is like a cow and is not an image of one",
              keeps_out="गौरिव गवयः"),
    Svarthika("5.3.97", gives="kan", result="iva-saṃjñā",
              excepts=("5.3.96",),
              why="संज्ञायां च — where the whole word is a NAME. "
                  "**अप्रतिकृत्यर्थ आरम्भः** — and the rule is "
                  "begun for what is NOT an image: अश्वसदृशस्य "
                  "संज्ञा **अश्वकः**"),
    Svarthika("5.3.98", adesa="lup", result="iva-manuṣya",
              excepts=("5.3.97",),
              why="लुम्मनुष्ये — the affix REMOVED where a man is "
                  "meant. चञ्चेव मनुष्यः **चञ्चा**, a man like a "
                  "straw figure; **दासी, खरकुटी**. "
                  "**मनुष्य इति किम्?** अश्वकः, उष्ट्रकः",
              keeps_out="अश्वकः"),
    Svarthika("5.3.99", adesa="lup", result="jīvikārtha-apaṇya",
              excepts=("5.3.97",),
              why="जीविकार्थे चापण्ये — removed where the image is "
                  "made for a LIVELIHOOD and is not for sale. "
                  "**विक्रीयते यत् तत् पण्यम्**. **वासुदेवः, "
                  "शिवः, स्कन्दः, विष्णुः** — "
                  "**देवलकादीनां जीविकार्था देवप्रतिकृतय उच्यन्ते**, "
                  "the temple-servants' images of the gods. "
                  "**अपण्य इति किम्?** हस्तिकान् विक्रीणीते — an "
                  "image-seller's stock keeps its affix",
              keeps_out="हस्तिकान् विक्रीणीते"),
    Svarthika("5.3.100", adesa="lup", gana="devapathādi",
              excepts=("5.3.96",),
              why="देवपथादिभ्यश्च — removed after an OPEN list, "
                  "**आदिशब्दः प्रकारे; आकृतिगणश्चायम्**. "
                  "**देवपथः, हंसपथः**. And a kārikā gives the "
                  "three settings:\n\n"
                  "    अर्चासु पूजनार्थासु चित्रकर्मध्वजेषु च ।\n"
                  "    इवे प्रतिकृतौ लोपः कनो देवपथादिषु ॥\n\n"
                  "IMAGES for worship — **शिवः, विष्णुः**; "
                  "PAINTINGS — **अर्जुनः, दुर्योधनः**; BANNERS — "
                  "**कपिः, गरुडः, सिंहः**"),
    Svarthika("5.3.101", gives="ḍhañ", of=("vasti",),
              result="iva", excepts=("5.3.96",),
              why="वस्तेर्ढञ् — **इतः प्रभृति प्रत्ययाः सामान्येन "
                  "भवन्ति, प्रतिकृतौ चाप्रतिकृतौ च**, and from "
                  "here the affixes come whether an image is meant "
                  "or not. वस्तिरिव **वास्तेयः, वास्तेयी**"),
    Svarthika("5.3.102", gives="ḍha", also_gives=("ḍhañ",),
              of=("śilā",), result="iva", excepts=("5.3.96",),
              why="शिलाया ढः. शिलेव **शिलेयं दधि**, curd like "
                  "stone. **केचिदत्र ढञमपीच्छन्ति, तदर्थं "
                  "योगविभागः कर्तव्यः** — some want ढञ् too, and "
                  "the rule is split for it: **शैलेयम्**, then "
                  "शिलेयम्"),
    Svarthika("5.3.103", gives="yat", gana="śākhādi",
              result="iva", excepts=("5.3.96",),
              why="शाखादिभ्यो यत्. शाखेव **शाख्यः**; मुख्यः, "
                  "जघन्यः. शाखा, मुख, जघन, शृङ्ग, मेघ, चरण, "
                  "स्कन्ध, शिरस्, उरस्, अग्र, शरण — शाखादिः"),
    Svarthika("5.3.104", nipatana=True, gives="yat", of=("dru",),
              result="bhavya", excepts=("5.3.96",),
              why="द्रव्यं च भव्ये — **द्रव्यशब्दो निपात्यते**. "
                  "**द्रुशब्दादिवार्थे यत् प्रत्ययो निपात्यते**: "
                  "**द्रव्यं भव्यः, आत्मवान्, अभिप्रेतानाम् "
                  "अर्थानां पात्रभूत उच्यते** — one who is a fit "
                  "vessel for what is wished for. **द्रव्योऽयं "
                  "राजपुत्रः**, a prince of promise"),
    Svarthika("5.3.105", gives="cha", of=("kuśāgra",),
              result="iva", excepts=("5.3.96",),
              why="कुशाग्राच्छः. कुशाग्रमिव सूक्ष्मत्वात् "
                  "**कुशाग्रीया बुद्धिः**, a mind as fine as the "
                  "point of a kuśa blade"),
    Svarthika("5.3.106", gives="cha", of_samjna="iva-samāsa",
              result="iva", excepts=("5.3.96",),
              why="समासाच्च तद्विषयात् — from a compound ALREADY "
                  "made in that sense, in that sense again. "
                  "**काकतालीयम्, अजाकृपाणीयम्, "
                  "अन्धकवर्तकीयम्** — **अतर्कितोपनतं "
                  "चित्रीकरणमुच्यते**, a startling coincidence.\n\n"
                  "**AND THE VṚTTI WORKS THE FIGURE OUT.** "
                  "**काकस्यागमनं यादृच्छिकम्, तालस्य पतनं च; तेन "
                  "तालेन पतता काकस्य वधः कृतः** — the crow comes "
                  "by chance and the palm-fruit falls by chance, "
                  "and the fruit kills the crow. So of Devadatta "
                  "and the bandits: **तत्र यो देवदत्तस्य दस्यूनां "
                  "च समागमः स काकतालसमागमसदृश इत्येक उपमार्थः; "
                  "अतश्च देवदत्तस्य वधः, स काकतालवधसदृश इति "
                  "द्वितीय उपमार्थः** — two comparisons, "
                  "**तत्र प्रथमे समासः, द्वितीये प्रत्ययः**: the "
                  "compound carries the first and the affix the "
                  "second. And **समासश्चायमस्मादेव ज्ञापकात्, "
                  "नह्यस्यापरं लक्षणमस्ति** — that compound has no "
                  "rule of its own, and this rule is the evidence "
                  "that it exists"),
    Svarthika("5.3.107", gives="aṇ", gana="śarkarādi",
              result="iva", excepts=("5.3.96",),
              why="शर्करादिभ्योऽण्. शर्करेव **शार्करम्**; "
                  "कापालिकम्. शर्करा, कपालिका, पिष्टिक, पुण्डरीक, "
                  "शतपत्र, गोलोमन्, गोपुच्छ, नरालि, नकुला, सिकता "
                  "— शर्करादिः"),
    Svarthika("5.3.108", gives="ṭhak", gana="aṅgulyādi",
              result="iva", excepts=("5.3.96",),
              why="अङ्गुल्यादिभ्यष्ठक्. अङ्गुलीव **अङ्गुलिकः**; "
                  "भारुजिकः. अङ्गुलि, भरुज, बभ्रु, वल्गु, मण्डर, "
                  "मण्डल, शष्कुल, कपि, उदश्वित्, गोणी, उरस्, "
                  "शिखर, कुलिश — अङ्गुल्यादिः"),
    Svarthika("5.3.109", gives="ṭhac", also_gives=("ṭhak",),
              of=("ekaśālā",), result="iva", optional=True,
              excepts=("5.3.108",),
              why="एकशालायाष्ठजन्यतरस्याम् — "
                  "**अन्यतरस्यांग्रहणेन अनन्तरष्ठक् प्राप्यते**, "
                  "the option letting the ठक् of the rule before "
                  "stand. एकशालेव **एकशालिकः, ऐकशालिकः**"),
    Svarthika("5.3.110", gives="īkak", of=("karka", "lohita"),
              result="iva", excepts=("5.3.96",),
              why="कर्कलोहितादीकक्. **कर्कः शुक्लोऽश्वः, तेन "
                  "सदृशः **कार्कीकः**; **लौहितीकः स्फटिकः**, "
                  "**स्वयमलोहितोऽप्युपाश्रयवशात् तथा प्रतीयते** — "
                  "a crystal not itself red, but taken so from "
                  "what lies behind it"),
    Svarthika("5.3.111", gives="thāl",
              of=("pratna", "pūrva", "viśva", "ima"),
              result="iva", usage="chandasi", excepts=("5.3.96",),
              why="प्रत्नपूर्वविश्वेमात् थाल् छन्दसि. तं "
                  "प्॒**रत्नथा॑** पू॒**र्वथा॑** वि॒**श्वथा** "
                  "इ॒**मथा॑** (ऋ० ५.४४.१)"),
    Svarthika("5.3.112", gives="ñya", of_samjna="pūga",
              result="tadrāja",
              why="पूगाञ् ञ्योऽग्रामणीपूर्वात् — **इवार्थ इति "
                  "निवृत्तम्**, and the pāda's last section begins. "
                  "**नानाजातीया अनियतवृत्तयोऽर्थकामप्रधानाः संघाः "
                  "पूगाः** — a पूग is a troop of mixed birth and no "
                  "settled livelihood, bent on gain and pleasure. "
                  "**लौहध्वज्यः, शैब्यः, चातक्यः**.\n\n"
                  "**अग्रामणीपूर्वादिति किम्?** देवदत्तो "
                  "ग्रामणीरेषां त इमे **देवदत्तकाः** — where the "
                  "troop is named from its LEADER, 5.2.78's affix "
                  "comes instead",
              keeps_out="देवदत्तकाः"),
    Svarthika("5.3.113", gives="ñya", of_samjna="vrāta-cphañanta",
              result="tadrāja",
              why="व्रातच्फञोरस्त्रियाम् — **नानाजातीया "
                  "अनियतवृत्तय उत्सेधजीविनः संघा व्राताः**, the "
                  "same definition 5.2.21 gave. **कापोतपाक्यः, "
                  "व्रैहिमत्यः**; and after a च्फञ्, "
                  "**कौञ्जायन्यः, ब्राध्नायन्यः**. "
                  "**अस्त्रियामिति किम्?** कपोतपाकी, कौञ्जायनी",
              keeps_out="कपोतपाकी, कौञ्जायनी"),
    Svarthika("5.3.114", gives="ñyaṭ",
              of_samjna="āyudhajīvisaṃgha", result="tadrāja",
              excludes=("brāhmaṇa", "rājanya"),
              why="आयुधजीविसंघाञ् ञ्यड् वाहीकेष्वब्राह्मणराजन्यात् "
                  "— from the words for a CONFEDERACY LIVING BY "
                  "ARMS, among the Vāhīkas, brahmins and kṣatriyas "
                  "excepted. **टकारो ङीबर्थः; तेनास्त्रियामिति "
                  "नानुवर्तते** — the ट gives the feminine, so the "
                  "*not in the feminine* of the rule before is not "
                  "carried. **कौण्डीबृस्यः, क्षौद्रक्यः, "
                  "मालव्यः**, and in the feminine कौण्डीबृसी, "
                  "**मालवी**.\n\n"
                  "Four conditions, four counter-examples. "
                  "**आयुधजीविग्रहणं किम्?** मल्लाः, शयण्डाः. "
                  "**संघग्रहणं किम्?** सम्राट्. "
                  "**वाहीकेष्विति किम्?** शबराः, पुलिन्दाः. "
                  "**अब्राह्मणराजन्यादिति किम्?** गोपालवा "
                  "ब्राह्मणाः, शालङ्कायना राजन्याः",
              keeps_out="मल्लाः, सम्राट्, शबराः, गोपालवा ब्राह्मणाः"),
    Svarthika("5.3.115", gives="ṭeṇyaṇ", of=("vṛka",),
              of_samjna="āyudhajīvisaṃgha", result="tadrāja",
              excepts=("5.3.114",),
              why="वृकाट् टेण्यण्. **टकारो ङीबर्थः, णकारो "
                  "वृद्ध्यर्थः**. **वार्केण्यः**, वार्केण्यौ, "
                  "वृकाः.\n\n"
                  "**आयुधजीविसंघविशेषणं जातिशब्दाद् मा भूत्** — "
                  "the condition is there so that the affix does "
                  "not come after the word for the ANIMAL: "
                  "**कामक्रोधौ मनुष्याणां खादितारौ वृकाविव**, "
                  "desire and anger, two wolves that devour men",
              keeps_out="वृकाविव"),
    Svarthika("5.3.116", gives="cha", gana="dāmanyādi",
              of_samjna="āyudhajīvisaṃgha", result="tadrāja",
              excepts=("5.3.114",),
              why="दामन्यादित्रिगर्तषष्ठाच्छः. **दामनीयः, "
                  "औलपीयः**; and from the six of which त्रिगर्त is "
                  "the sixth, **कौण्डोपरथीयः, दाण्डकीयः**. And a "
                  "verse names them:\n\n"
                  "    आहुस्त्रिगर्तषष्ठांस्तु कौण्डोपरथदाण्डकी ।\n"
                  "    क्रौष्टकिर्जालमानिश्च ब्राह्मगुप्तोऽथ "
                  "जानकिः ॥\n\n"
                  "दामनी, औलपि, आकिदन्ती, काकरन्ति, शत्रुन्तपि, "
                  "सार्वसेनि, बिन्दु, मौञ्जायन, उलभ, "
                  "सावित्रीपुत्र — दामन्यादिः"),
    Svarthika("5.3.117", gives="aṇ", gana="parśvādi",
              of_samjna="āyudhajīvisaṃgha", result="tadrāja",
              excepts=("5.3.114",),
              why="पर्श्वादियौधेयादिभ्यामणञौ, the पर्श्वादि half. "
                  "**पार्शवः, आसुरः**. पर्शु, असुर, रक्षस्, "
                  "बाह्लीक, वयस्, मरुत्, दशार्ह, पिशाच, विशाल, "
                  "अशनि, कार्षापण, सत्वत्, वसु — पर्श्वादिः"),
    Svarthika("5.3.117", gives="añ", gana="yaudheyādi",
              of_samjna="āyudhajīvisaṃgha", result="tadrāja",
              excepts=("5.3.114",),
              why="पर्श्वादियौधेयादिभ्यामणञौ, the यौधेयादि half. "
                  "**यौधेयः, शौक्रेयः**. यौधेय, कौशेय, क्रौशेय, "
                  "शौक्रेय, शौभ्रेय, धार्तेय, वार्तेय, जाबालेय, "
                  "त्रिगर्त, भरत, उशीनर — यौधेयादिः"),
    Svarthika("5.3.118", gives="yañ", gana="abhijidādi",
              of_samjna="aṇanta", result="tadrāja",
              why="अभिजिद्विदभृच्छालावच्छिखावच्छमीवदूर्णावच्छ्रुमद"
                  "णो यञ् — **आयुधजीविसंघादिति निवृत्तम्**. "
                  "**अभिजितोऽपत्यमित्यण्; तदन्ताद् यञ्** — the "
                  "affix comes after a stem that already carries "
                  "अण्. **आभिजित्यः, वैदभृत्यः, शालावत्यः**.\n\n"
                  "**गोत्रप्रत्ययस्यात्राणो ग्रहणमिष्यते** — and "
                  "the अण् meant is the LINEAGE affix, so "
                  "**आभिजितो मुहूर्तः, आभिजितः स्थालीपाकः** are "
                  "not reached",
              keeps_out="आभिजितो मुहूर्तः"),
    Svarthika("5.3.119", result="tadrāja",
              why="ञ्यादयस्तद्राजाः — and the pāda ends as it "
                  "began, with a NAME. **पूगाञ् ञ्योऽग्रामणीपूर्वात् "
                  "इत्यतः प्रभृति ये प्रत्ययाः, ते तद्राजसंज्ञा "
                  "भवन्ति** — everything from 5.3.112 to 5.3.118 is "
                  "called a तद्राज.\n\n"
                  "**तद्राजप्रदेशाः — तद्राजस्य बहुषु… "
                  "इत्येवमादयः** (2.4.62) — and the vṛtti names "
                  "where the name is USED, as 5.3.1 did of "
                  "विभक्ति. A pāda opened by a saṃjñā-heading and "
                  "closed by a saṃjñā-rule, and both of them give "
                  "the reason the name is worth giving.\n\n"
                  "इति श्रीजयादित्यविरचितायां काशिकायां वृत्तौ "
                  "पञ्चमाध्यायस्य तृतीयः पादः"),
)


@dataclass(frozen=True)
class OwnSense:
    """What the resolver answers with."""

    affix: str
    sutra: str
    why: str
    also_gives: Tuple[str, ...] = ()
    adesa: str = ""
    optional: bool = False
    nipatana: bool = False
    excepts: Tuple[str, ...] = ()


def _reaches(row: Svarthika, stem: str, gana: str, samjna: str,
             case: str, result: str, before: str,
             usage: str, pre: str) -> bool:
    if row.heading:
        return False
    if row.of and stem not in row.of:
        return False
    if row.gana and gana != row.gana:
        return False
    if row.of_samjna and not (samjna == row.of_samjna
                              or (row.of and stem in row.of)):
        return False
    if row.excludes and stem in row.excludes:
        return False
    if row.case and case and case != row.case:
        return False
    if row.result and result != row.result:
        return False
    if row.before and before != row.before:
        return False
    if row.pre and pre != row.pre:
        return False
    if row.usage and usage != row.usage:
        return False
    return True


def _supplies(row: Svarthika, wants: str) -> bool:
    return (not wants
            or wants == row.gives
            or wants in row.also_gives)


def _how_specific(row: Svarthika) -> int:
    """
    A named base is narrowest, then the class it belongs to. The
    sound the affix begins with counts high, since a rule that
    conditions on it is displacing one that does not.

    And the SENSE counts above everything but a named base, because
    in this pāda almost every rule has one of its own — 5.3.7 gives
    तसिल् to किम् generally, and 5.3.92 gives डतरच् to the same word
    when one of two is being singled out. The narrower is the one
    that names the sense.
    """
    return (
        8 * bool(row.of)
        + 7 * bool(row.gana)
        + 6 * bool(row.result)
        + 5 * bool(row.before)
        + 5 * bool(row.pre)
        + 4 * bool(row.usage)
        + 3 * bool(row.of_samjna)
        + 1 * bool(row.case)
    )


def in_own_sense(stem: str = "", *, gana: str = "", samjna: str = "",
                 case: str = "", result: str = "", before: str = "",
                 usage: str = "", pre: str = "",
                 wants: str = "") -> OwnSense:
    """
    5.3.1–27 — the affixes that add nothing to what the base means.

    Where the pādas before asked what a word means with respect to
    something else, these are स्वार्थिक: **अतः परं स्वार्थिकाः
    प्रत्ययाः**, so the समर्थ heading lapses and only the option
    carries on.

    Nothing stands over the section supplying by default: 5.3.1
    gives a NAME and not an affix, so a question that reaches no
    rule reaches nothing.
    """
    matched = [
        row for row in SVARTHIKA_TABLE
        if _reaches(row, stem, gana, samjna, case, result, before,
                    usage, pre)
        and _supplies(row, wants)
    ]
    if not matched:
        return OwnSense("", "", "No rule of 5.3.1–27 is reached. "
                                "5.3.1 supplies a NAME and not an "
                                "affix, so nothing answers by "
                                "default")
    row = max(matched, key=_how_specific)
    return OwnSense(row.gives, row.sutra, row.why,
                    also_gives=row.also_gives, adesa=row.adesa,
                    optional=row.optional, nipatana=row.nipatana,
                    excepts=row.excepts)


def vibhakti_run() -> OwnSense:
    """
    How far the विभक्ति name reaches — and this heading supplies a
    name rather than an affix, which no heading before it did.

    **प्रागेतस्माद् दिक्संशब्दनाद् यानित ऊर्ध्वमनुक्रमिष्यामो
    विभक्तिसंज्ञास्ते वेदितव्याः.**
    """
    opens, closes = VIBHAKTI_RUN
    return OwnSense(
        "", opens,
        "विभक्ति is the NAME from %s to %s, bounded by the word "
        "दिक् lifted out of %s. The sixth heading built that way "
        "and the first to bound a saṃjñā — and the name is given "
        "for two consequences, the त्यदादि rules and the accent of "
        "इह" % (opens, closes, VIBHAKTI_MARKER))


def provisions_for(sutra_id: str) -> Tuple[Svarthika, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in SVARTHIKA_TABLE
                 if row.sutra == sutra_id)
