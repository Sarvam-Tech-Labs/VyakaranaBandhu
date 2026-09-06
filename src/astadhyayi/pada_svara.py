# -*- coding: utf-8 -*-
"""
६.१.१५८–२२३ — अनुदात्तं पदमेकवर्जम्, and where the one accent falls.

**अनुदात्तं पदमेकवर्जम्** is not a rule. **परिभाषेयं स्वरविधिविषया**
— it is a maxim read into every accent rule that follows: wherever an
उदात्त or a स्वरित is taught, ONE syllable takes it and every other
syllable of the word is अनुदात्त. Sixty-six sūtras then say which
syllable.

**AND THE MAXIM IS THERE TO CANCEL FOUR COMPETING CLAIMS.** The vṛtti
gives the verse:

    आगमस्य विकारस्य प्रकृतेः प्रत्ययस्य च।
    पृथक्स्वरनिवृत्त्यर्थमेकवर्जं पदस्वरः॥

An augment has an accent, a substitute has one, the base has one and
the affix has one — and एकवर्जम् is what stops all four sounding at
once. Which of them wins is settled in turn by
**परनित्यान्तरङ्गापवादैः स्वरैर्व्यवस्था सतिशिष्टेन च। यो हि यस्मिन्
सति शिष्यते, स तस्य बाधको भवति** — the accent taught in the presence
of another displaces it.

**AND ONE RULE BREAKS THE MAXIM OUTRIGHT.** 6.1.200 अन्तश्च तवै
युगपत् gives कर्तवै TWO accents at the same time, and the vṛtti says
the word युगपत् is there for exactly that reason:
**युगपद्ग्रहणं पर्यायनिवृत्त्यर्थम्। एकवर्जमिति वचनाद् यौगपद्यं न
स्यात्** — without it, 6.1.158 would have made the two alternatives
instead of simultaneous.

**AND प्रत्ययलक्षण DOES NOT HOLD HERE AS IT DOES ELSEWHERE.** Three
rules answer the question three ways. 6.1.198 wants it — सर्पिरागच्छ
takes the vocative accent though the affix is gone. 6.1.197 and
6.1.199 refuse it — गर्गाः and पथिप्रियः lose the accent with the
affix. And 6.1.204 exists only to say so: **एतदेव ज्ञापयति क्वचिद्
इह स्वरविधौ प्रत्ययलक्षणं न भवतीति**.

**WHAT THIS MODULE DOES NOT DO.** It reports which rule puts the
accent and where. It does not mark the syllable: the corpus is
accented already, and `svara` holds what an उदात्त, an अनुदात्त and a
स्वरित are.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: Where the परिभाषा governs — to the end of the pāda, which is also
#: where 6.1.72's संहिता stopped. 6.1.158's own words are what bound
#: that heading.
SVARA_RUN: Tuple[str, str] = ("6.1.158", "6.1.223")

#: The verse the vṛtti gives for why एकवर्जम् is said: four things
#: each have an accent of their own, and the word cancels three.
EKAVARJA_VERSE: Tuple[str, str] = (
    "आगमस्य विकारस्य प्रकृतेः प्रत्ययस्य च",
    "पृथक्स्वरनिवृत्त्यर्थमेकवर्जं पदस्वरः",
)

#: And how the four are ordered when they compete.
WHICH_WINS: str = (
    "परनित्यान्तरङ्गापवादैः स्वरैर्व्यवस्था सतिशिष्टेन च — "
    "यो हि यस्मिन् सति शिष्यते, स तस्य बाधको भवति"
)

#: The two आकृतिगण of this pāda, each defined by exclusion rather
#: than by its members: **अविहितमाद्युदात्तत्वं वृषादिषु
#: द्रष्टव्यम्**, and the same shape at 6.1.157's पारस्करप्रभृति.
AKRTIGANA: Tuple[str, ...] = ("uñchādi", "vṛṣādi")

#: What a consonant counts as where an accent is concerned. Used at
#: 6.1.223 to put the उदात्त on the vowel of a consonant-final
#: compound — and DENIED at 6.1.176, where naming the नुट् is what
#: keeps मरुत्वान् out.
VYANJANAM_AVIDYAMANAVAT: str = "स्वरविधौ व्यञ्जनमविद्यमानवत्"


@dataclass(frozen=True)
class Accent:
    """One rule of 6.1.158–223: which syllable takes the accent."""

    sutra: str
    #: What accent: udātta, svarita, or anudātta.
    puts: str = ""
    #: Which syllable: anta, ādi, upottama, pratyayāt-pūrva, or
    #: ādi-anta together at 6.1.200.
    where: str = ""
    #: The words or roots the rule names.
    of: Tuple[str, ...] = ()
    #: A named class instead — उञ्छादि, वृषादि, स्वपादि, षट्.
    gana: str = ""
    #: The affix's marker the rule turns on — cit, kit, ñit, nit,
    #: tit, lit, rit, ghañ.
    marker: str = ""
    #: What follows — a case-ending, an affix, a class of them.
    before: str = ""
    #: What precedes.
    after: str = ""
    #: The sense the word must carry — निवास at 6.1.201, करण at
    #: 6.1.202, कर्तृ at 6.1.207.
    result: str = ""
    #: True where the word must be a NAME.
    samjna: bool = False
    #: True where it must be feminine.
    stri: bool = False
    refuses: bool = False
    optional: bool = False
    #: True where the rule holds in ordinary speech alone — 6.1.181.
    bhasayam: bool = False
    chandasi: bool = False
    mantra: bool = False
    #: True where the row is the परिभाषा rather than a rule.
    heading: bool = False
    #: The rule this one displaces, by ITS own number.
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


ACCENT_TABLE: Tuple[Accent, ...] = (
    Accent(
        "6.1.158", heading=True,
        why="अनुदात्तं पदमेकवर्जम् — **परिभाषेयं स्वरविधिविषया। "
            "यत्रान्यः स्वर उदात्तः स्वरितो वा विधीयते, तत्रानुदात्तं "
            "पदमेकं वर्जयित्वा भवति** — one syllable of a word takes "
            "the accent that is taught and every other is "
            "अनुदात्त.\\n\\n"
            "**AND WHICH ONE IS EXCEPTED IS THE ONE THE RULE NAMES.** "
            "**कः पुनरेको वर्ज्यते? यस्यासौ स्वरो विधीयते** — the "
            "maxim does not choose a syllable; it clears the rest "
            "out of the way of whichever rule speaks.\\n\\n"
            "**AND एकवर्जम् IS SAID TO CANCEL FOUR COMPETING "
            "CLAIMS.** **आगमस्य विकारस्य प्रकृतेः प्रत्ययस्य च। "
            "पृथक्स्वरनिवृत्त्यर्थमेकवर्जं पदस्वरः॥** — an augment "
            "has its own accent (7.1.98's आम् in चत्वारः), a "
            "substitute has one (अनङ् in अस्थनि), the base has one "
            "(गोपायति), the affix has one (कर्तव्यम्); and each of "
            "the four displaces one of the others somewhere.\\n\\n"
            "**AND WHICH OF THEM WINS IS SETTLED BY FIVE THINGS.** "
            "**परनित्यान्तरङ्गापवादैः स्वरैर्व्यवस्था सतिशिष्टेन "
            "च। यो हि यस्मिन् सति शिष्यते, स तस्य बाधको भवति** — the "
            "later, the invariable, the inner, the exception, and "
            "the one taught IN THE PRESENCE of another. The chain "
            "**लुनाति, लुनीतः, लुनीतस्तराम्** shows the last of the "
            "five three times over"),
    Accent(
        "6.1.159", puts="udātta", where="anta", of=("kṛṣ",),
        marker="ghañ", blocks=("6.1.197",),
        keeps_out="कर्षः from the तुदादि root, which keeps the "
                  "first-syllable accent",
        why="कर्षात्वतो घञोऽन्त उदात्तः — a घञ् stem from कृष् or "
            "with a long आ in it takes the accent on its last "
            "syllable: **कर्षः, पाकः, त्यागः, रागः, दायः, धायः**. "
            "**ञ्नित्यादिर्नित्यम् इत्यस्यापवादः** — an exception to "
            "6.1.197, which would put it on the first.\\n\\n"
            "**AND THE ODD SHAPE कर्ष IS WHAT PICKS THE ROOT.** "
            "**कर्ष इति विकृतनिर्देशः कृषतेर्निवृत्त्यर्थः** — "
            "written with its guṇa, it names the भ्वादि root and "
            "leaves the तुदादि one out"),
    Accent(
        "6.1.160", puts="udātta", where="anta", gana="uñchādi",
        why="उञ्छादीनां च — a list, end-accented: **उञ्छः, म्लेच्छः, "
            "जञ्जः, जल्पः, जपः, वधः, युगः**. Some are घञ् stems and "
            "would have taken 6.1.197's accent; some are अप् stems "
            "and would have taken the root's.\\n\\n"
            "**AND HALF THE LIST IS CONFINED BY A SENSE.** "
            "**गरो दूष्ये** — गर is end-accented only of poison; "
            "**वेगवेदवेष्टबन्धाः करणे** — those four only as "
            "instruments, and **भाव आद्युदात्ता एव**; "
            "**वर्तनिः स्तोत्रे**, **श्वभ्रे दरः**, "
            "**साम्बतापौ भावगर्हायाम्**. A list whose members each "
            "carry their own condition"),
    Accent(
        "6.1.161", puts="udātta", where="ādi", after="udātta-lopa",
        keeps_out="भार्गवः — the उदात्त went with the whole affix "
                  "before a case-ending could be added; बैदी, और्वी",
        why="अनुदात्तस्य च यत्रोदात्तलोपः — where an उदात्त is "
            "dropped before an अनुदात्त, that अनुदात्त takes the "
            "accent at its first syllable: **कुमारी** from "
            "कुमार꣡ + ई॒, **पथः, पथा, पथे**, **कुमुद्वान्, नड्वान्, "
            "वेतस्वान्**.\\n\\n"
            "**AND अनुदात्तस्य IS SAID TO PUT IT AT THE FIRST AND "
            "NOT THE LAST.** **तदेतद् अनुदात्तग्रहणम् आदेरनुदात्तस्य "
            "उदात्तार्थम्। अन्त इति हि प्रकृतत्वाद् अन्तस्य स्यात्** "
            "— अन्त is carrying from 6.1.159, so without this word "
            "the accent would land on the wrong end.\\n\\n"
            "**AND A SVARITA CANNOT SET THE RULE OFF.** An objector "
            "offers प्रासङ्ग्यः, where a स्वरित य displaced an "
            "उदात्त. **नैतदस्ति, स्वरिते हि विधीयमाने परिशिष्टम् "
            "अनुदात्तम्, तत् कुतः उदात्तलोपः?** — where a स्वरित is "
            "taught, 6.1.158 makes the rest अनुदात्त, so there was "
            "never an उदात्त to lose"),
    Accent(
        "6.1.162", puts="udātta", where="anta", before="dhātu",
        why="धातोः — a root takes the accent on its last syllable: "
            "**पचति, पठति, ऊर्णोति, गोपायति, याति**. **अन्त इत्येव** "
            "— the word carries down from 6.1.159, and this is the "
            "accent every later rule of the section is stated "
            "against"),
    Accent(
        "6.1.163", puts="udātta", where="anta", marker="cit",
        why="चितः — a stem made by an affix, augment or substitute "
            "marked च् takes the accent at its end: **भङ्गुरम्, "
            "भासुरम्, मेदुरम्** with 3.2.161's घुरच्; **कुण्डिनाः** "
            "with 2.4.70's कुण्डिनच्.\\n\\n"
            "**AND THE END MEANT IS THE WHOLE WORD'S.** "
            "**चिति प्रत्यये प्रकृतिप्रत्ययसमुदायस्यान्त उदात्त "
            "इष्यते** — which is what makes **बहुपटवः** and "
            "**उच्चकैः** work, the affixes बहुच् and अकच् being put "
            "in at the FRONT and in the MIDDLE and the accent still "
            "landing at the end"),
    Accent(
        "6.1.164", puts="udātta", where="anta", marker="cit",
        before="taddhita", blocks=("6.1.197",),
        why="तद्धितस्य — and a taddhita stem marked च् likewise: "
            "**कौञ्जायनाः, भौञ्जायनाः** with 4.1.98's च्फञ्.\\n\\n"
            "**AND THE RULE EXISTS TO SETTLE A CONTEST BETWEEN TWO "
            "MARKERS.** **किमर्थमिदम्? परमपि ञित्स्वरं बाधित्वा "
            "अन्तोदात्तत्वमेव यथा स्यात्** — च्फञ् has both a च् and "
            "a ञ्, and 6.1.197's ञित् accent stands LATER. The rule "
            "gives the च् its way, and the reason is that the ञ् "
            "still has 7.2.117's vṛddhi to do while the च् would "
            "have nothing left"),
    Accent(
        "6.1.165", puts="udātta", where="anta", marker="kit",
        before="taddhita",
        why="कितः — and a taddhita marked क् too: **नाडायनः, "
            "चारायणः** with 4.1.99's फक्; **आक्षिकः, शालाकिकः** with "
            "4.4.1's ठक्"),
    Accent(
        "6.1.166", puts="udātta", where="anta", of=("tisṛ",),
        before="jas", blocks=("8.2.4",),
        why="तिसृभ्यो जसः — **तिस्रस्तिष्ठन्ति**, and the accent "
            "displaces the स्वरित 8.2.4 would give.\\n\\n"
            "**AND जसः IS SAID FOR A CASE THE WORD ITSELF DOES NOT "
            "HAVE.** तिसृ is plural only, and of its seven plural "
            "cases the accusative is 6.1.174's and the five "
            "consonant-initial ones are 6.1.179's — so जस् is the "
            "only one left and naming it looks idle. "
            "**जस्ग्रहणम् उपसमस्तार्थम् एक इच्छन्ति** — it is there "
            "for the compound, where singular and dual endings do "
            "occur: **अतितिस्रौ**"),
    Accent(
        "6.1.167", puts="udātta", where="anta", of=("catur",),
        before="śas",
        keeps_out="चतस्रः पश्य — the feminine चतसृ is first-accented "
                  "by a vārttika, and the र् standing for its ऋ is "
                  "स्थानिवत्",
        why="चतुरः शसि — **चतुरः पश्य**, the accent on तु. And the "
            "feminine is kept out twice over: **चतस्रादेश "
            "आद्युदात्तनिपातनाद् यणादेशस्य च पूर्वविधौ "
            "स्थानिवत्त्वाद् अयं स्वरो न भवति**"),
    Accent(
        "6.1.168", puts="udātta", where="anta",
        before="tṛtīyādi-vibhakti", after="ekāc",
        keeps_out="राज्ञा — not one-syllabled in the locative "
                  "plural; हरिणा, राजसु; वाचौ, वाचः — not from the "
                  "third case on; वाक्तरा — तरप् is no विभक्ति",
        why="सावेकाचस्तृतीयादिर्विभक्तिः — where the stem is "
            "one-syllabled AS IT STANDS IN THE LOCATIVE PLURAL, the "
            "endings from the third case on take the accent: "
            "**वाचा, वाग्भ्याम्, वाग्भिः, वाग्भ्यः; याता, "
            "याद्भ्याम्**.\\n\\n"
            "**AND सौ IS THE LOCATIVE PLURAL AND NOT THE "
            "NOMINATIVE.** **साविति सप्तमीबहुवचनस्य सुशब्दस्य "
            "ग्रहणम्** — which is what keeps त्वया and त्वयि out, "
            "one-syllabled though their stems look"),
    Accent(
        "6.1.169", puts="udātta", where="anta",
        before="tṛtīyādi-vibhakti", after="antodātta-uttarapada",
        optional=True, blocks=("6.1.223",),
        keeps_out="अवाचा, सुवाचा — the second member is not "
                  "end-accented; अग्निचिता, सोमसुता — a नित्य "
                  "compound",
        why="अन्तोदात्तादुत्तरपदादन्यतरस्यामनित्यसमासे — in a "
            "compound that can be unloosened, and whose second "
            "member is one-syllabled and end-accented, the same "
            "endings take the accent optionally: **परमवाचा** beside "
            "**परमवाचा**, **परमत्वचा** beside **परमत्वचा**. "
            "**यदा विभक्तिरुदात्ता न भवति, तदा समासान्तोदात्तत्वमेव** "
            "— on the other side 6.1.223 takes it.\\n\\n"
            "**AND नित्य IS ACCENTED IN THE SŪTRA TO NAME A "
            "HEADING.** **नित्यशब्दः स्वर्यते। तेन "
            "नित्याधिकारविहितः समासः पर्युदस्यते** — a compound made "
            "under 2.2.19's नित्य heading is what is excepted, and "
            "a compound that is नित्य merely for having no analysis "
            "still takes the option: **अवाचा ब्राह्मणेन**"),
    Accent(
        "6.1.170", puts="udātta", where="anta",
        before="asarvanāmasthāna", after="añc", chandasi=True,
        blocks=("6.1.222",),
        why="अञ्चेश्छन्दस्यसर्वनामस्थानम् — in the corpus, after a "
            "stem in अञ्च् the weak endings take the accent: "
            "**इन्द्रो दधीचो अस्थभिः**. It displaces 6.1.222, which "
            "would have put it on the syllable before.\\n\\n"
            "**AND असर्वनामस्थान IS SAID TO REACH ONE MORE ENDING.** "
            "**तृतीयादिरिति वर्तमाने शसोऽपि परिग्रहार्थम् "
            "असर्वनामस्थानग्रहणम्** — तृतीयादि was carrying and "
            "would have left the accusative plural out: "
            "**प्रतीचो बाहून् प्रति भङ्ध्येषाम्**"),
    Accent(
        "6.1.171", puts="udātta", where="anta",
        before="asarvanāmasthāna",
        of=("ūṭh", "idam", "padādi", "ap", "puṃs", "rai", "div"),
        keeps_out="अक्षद्युवा — that ऊठ् is 6.4.19's and not "
                  "6.4.132's; अथो आभ्यां — इदम् is not end-accented "
                  "in the अन्वादेश",
        why="ऊडिदम्पदाद्यप्पुम्रैद्युभ्यः — after seven bases the "
            "weak endings take the accent: **प्रष्ठौहः, प्रष्ठौहा; "
            "आभ्याम्, एभिः; पदश्चतुरो जहि; अपः पश्य, अद्भिः; पुंसः, "
            "पुम्भ्याम्; रायः पश्य; दिवः, दिवा**.\\n\\n"
            "**AND पदादि MEANS A STRETCH AND NOT A WORD.** "
            "**पदादयः पद्दन्नोमास् इत्येवमादयो निश्पर्यन्ता इह "
            "गृह्यन्ते** — 6.1.63's list as far as निश्, and no "
            "further: **असन्प्रभृतिभ्यो विभक्तिरनुदात्तैव भवति**, "
            "so आसनि and उदनि keep their endings unaccented"),
    Accent(
        "6.1.172", puts="udātta", where="anta",
        before="asarvanāmasthāna", after="aṣṭā", of=("aṣṭan",),
        blocks=("6.1.180",),
        keeps_out="अष्टसु — the short form, where 6.1.180 takes it",
        why="अष्टनो दीर्घात् — after the LONG form of अष्टन् the weak "
            "endings take the accent: **अष्टाभिः, अष्टाभ्यः, "
            "अष्टासु**, against अष्टभिः and अष्टसु.\\n\\n"
            "**AND दीर्घात् IS READ AS TWO ज्ञापक AT ONCE.** "
            "**इदमेव दीर्घग्रहणम् अष्टन आत्वविकल्पं ज्ञापयति, "
            "कृतात्वस्य च षट्संज्ञां ज्ञापयति** — 7.2.84's आ would "
            "be fixed and the word would be there whatever, so the "
            "condition is idle unless the lengthening is OPTIONAL; "
            "and it is idle again unless the lengthened form is a "
            "षट् and would otherwise take 6.1.179's accent"),
    Accent(
        "6.1.173", puts="udātta", where="anta", marker="śatṛ",
        before="nadī-ajādi", after="antodātta",
        keeps_out="तुदन्ती — the participle has the नुम्; ददती, "
                  "दधतः — first-accented by 6.1.189; तुदद्भ्याम् — "
                  "the ending is not vowel-initial",
        why="शतुरनुमो नद्यजादी — after an end-accented शतृ participle "
            "without its नुम्, the feminine ई and the vowel-initial "
            "weak endings take the accent: **तुदती, नुदती, लुनती, "
            "पुनती; तुदता, नुदता**.\\n\\n"
            "**AND THE PARTICIPLE IS END-ACCENTED BY A CHAIN OF "
            "THREE RULES.** 6.1.186 makes the शतृ अनुदात्त after a "
            "root taught with अ; 8.2.5 makes the single substitute "
            "उदात्त where one of the two was; and **तस्य "
            "पूर्वत्रासिद्धत्वं नेष्यते** — 8.2.1 is not applied to "
            "it, or the participle would not be end-accented and "
            "this rule would have nothing to work on.\\n\\n"
            "**AND A SUPPLEMENT ADDS TWO MORE.** "
            "**बृहन्महतोरुपसंख्यानम्** — **बृहती, महती; बृहता, "
            "महता**"),
    Accent(
        "6.1.174", puts="udātta", where="anta",
        before="nadī-ajādi", after="udātta-yaṇ-hal-pūrva",
        keeps_out="कर्त्री, कर्त्रा from the तृन् stem, which is "
                  "first-accented; बहुतितवा — the यण् is preceded by "
                  "a vowel and 8.2.4 makes the ending स्वरित",
        why="उदात्तयणो हल्पूर्वात् — where a semivowel stands for an "
            "उदात्त vowel and a consonant stands before it, the same "
            "endings take the accent: **कर्त्री, हर्त्री, "
            "प्रलवित्री; कर्त्रा, हर्त्रा**. The तृच् stems are "
            "end-accented and the तृन् ones are not, which is the "
            "whole of the difference.\\n\\n"
            "**AND A SUPPLEMENT EXTENDS IT TO A NASAL.** "
            "**नकारग्रहणं कर्तव्यम्** — **वाक्पत्नी इयं कन्या**, "
            "where what precedes is no semivowel at all"),
    Accent(
        "6.1.175", refuses=True, before="tṛtīyādi-vibhakti",
        after="ūṅ-dhātu-yaṇ", blocks=("6.1.174",),
        why="न उङ्धात्वोः — but not where the semivowel stands for "
            "the feminine ऊङ् or for a root's own final: "
            "**ब्रह्मबन्ध्वा, ब्रह्मबन्ध्वे; सकृल्ल्वा, "
            "खलप्वे**.\\n\\n"
            "**AND WHAT STANDS INSTEAD IS 8.2.4's स्वरित.** "
            "**उदात्तत्वे प्रतिषिद्धे उदात्तस्वरितयोर्यणः "
            "स्वरितोऽनुदात्तस्य इति विभक्तिः स्वर्यते** — the "
            "refusal does not leave the ending unaccented; it hands "
            "it to the general rule"),
    Accent(
        "6.1.176", puts="udātta", where="anta", before="matup",
        after="hrasva-antodātta",
        keeps_out="वसुमान् — वसु is first-accented; मरुत्वान् — the "
                  "त् makes the vowel heavy, and naming the नुट् is "
                  "what stops the maxim from ignoring it",
        why="ह्रस्वनुड्भ्यां मतुप् — मतुप् takes the accent after an "
            "end-accented stem ending in a light vowel, or after the "
            "augment नुट्: **अग्निमान्, वायुमान्, कर्तृमान्; "
            "अक्षण्वता, शीर्षण्वता**.\\n\\n"
            "**AND THIS IS WHERE स्वरविधौ व्यञ्जनमविद्यमानवत् IS "
            "REFUSED.** **अत्र च स्वरविधौ व्यञ्जनमविद्यमानवद् "
            "इत्येषा परिभाषा नाश्रीयते नुड्ग्रहणात्** — naming the "
            "नुट् separately is only worth doing if a consonant DOES "
            "count, and that is why **मरुत्वान्** is out. The same "
            "maxim 6.1.223 leans on, denied here.\\n\\n"
            "**AND TWO SUPPLEMENTS PULL IT BOTH WAYS.** "
            "**रेशब्दाच्च मतुप उदात्तत्वं वक्तव्यम्** — **आ रेवान्**; "
            "and **त्रेश्च प्रतिषेधो वक्तव्यः** — **त्रिवतीः**"),
    Accent(
        "6.1.177", puts="udātta", where="anta", before="nām",
        after="hrasva-antodātta", optional=True,
        keeps_out="धेन्वाम्, शकट्याम् — नाम् without its सुट्; "
                  "कुमारीणाम् — not a light vowel; त्रपूणाम्, "
                  "वसूनाम् — not end-accented",
        why="नामन्यतरस्याम् — and the genitive plural नाम् "
            "optionally: **अग्नीनाम्** beside **अग्नीनाम्**, "
            "**वायूनाम्**, **कर्तॄणाम्**.\\n\\n"
            "**AND ह्रस्व IS READ AS *SHORT BEFORE मतुप्*, NOT AS "
            "*SHORT HERE*.** The vowels in those forms are long, so "
            "the condition looks unmet. **मतुबग्रहणं च तेन मतुपा "
            "ह्रस्वो विशेष्यते** — मतुप् carries down and the "
            "condition is on the shape the stem HAS before that "
            "affix. Read it the other way and तिसृणाम् and "
            "चतसृणाम् are reached instead, which is not wanted"),
    Accent(
        "6.1.178", puts="udātta", where="anta", before="nām",
        after="ṅī", chandasi=True,
        keeps_out="नदीनां पारे; जयन्तीनां मरुतः — the same corpus, "
                  "unaccented",
        why="ङ्याश्छन्दसि बहुलम् — in the corpus, नाम् takes the "
            "accent variously after the feminine ई: **देवसेनानाम् "
            "अभिभञ्जतीनाम्; बह्वीनां पिता**. And sometimes not — "
            "which is what बहुलम् records"),
    Accent(
        "6.1.179", puts="udātta", where="anta", gana="ṣaṭ",
        before="halādi-vibhakti",
        keeps_out="चतस्रः पश्य — that ending begins with a vowel",
        why="षट्त्रिचतुर्भ्यो हलादिः — after the numerals called षट्, "
            "and after त्रि and चतुर्, a consonant-initial ending "
            "takes the accent: **षड्भिः, षड्भ्यः, पञ्चानाम्, "
            "षण्णाम्, सप्तानाम्; त्रिभिः, त्रयाणाम्; "
            "चतुर्णाम्**.\\n\\n"
            "**AND अन्तोदात्तात् LAPSES HERE.** "
            "**अन्तोदात्तादित्येतद् निवृत्तम्** — पञ्चन् and नवन् "
            "are first-accented and the rule reaches them anyway, "
            "which it could not if the condition still ran"),
    Accent(
        "6.1.180", puts="udātta", where="upottama", gana="ṣaṭ",
        before="jhalādi-vibhakti", blocks=("6.1.179",),
        keeps_out="पञ्चानाम्, सप्तानाम् — the ending does not begin "
                  "with a झल्; षड्भिः, षड्भ्यः — only two syllables, "
                  "so there is no penult",
        why="झल्युपोत्तमम् — where the ending begins with a झल्, the "
            "accent goes to the syllable before the last: "
            "**पञ्चभिः, सप्तभिः, तिसृभिः, चतुर्भिः**.\\n\\n"
            "**AND उपोत्तम IS DEFINED BEFORE IT IS USED.** "
            "**त्रिप्रभृतीनाम् अन्त्यम् उत्तमम्, तत्समीपे च यत् तद् "
            "उपोत्तमम्** — the word itself requires three syllables, "
            "and that is why षड्भिः falls back to 6.1.179"),
    Accent(
        "6.1.181", puts="udātta", where="upottama", gana="ṣaṭ",
        before="jhalādi-vibhakti", optional=True, bhasayam=True,
        blocks=("6.1.180",),
        why="विभाषा भाषायाम् — in ordinary speech the rule before is "
            "a choice: **पञ्चभिः** beside **पञ्चभिः**, "
            "**सप्तभिः**, **तिसृभिः**, **चतुर्भिः**. In the corpus "
            "it is fixed, and this is the only rule of the pāda "
            "whose condition is that the language is NOT Vedic"),
    Accent(
        "6.1.182", refuses=True,
        of=("go", "śvan", "sāv-avarṇa", "rāj", "añc", "kruñc", "kṛt"),
        blocks=("6.1.168", "6.1.169", "6.1.171"),
        keeps_out="प्राचा, प्राचे — there the न् HAS gone, and the "
                  "ending takes its accent after all",
        why="न गोश्वन्सावर्णराडङ्क्रुङ्कृद्भ्यः — after seven bases "
            "everything from 6.1.168 on is refused: **गवा, गवे, "
            "गोभ्याम्; शुना, शुने; येभ्यः, तेभ्यः, केभ्यः; राजा; "
            "प्राञ्चा, प्राङ्भ्याम्; क्रुञ्चा; कृता**.\\n\\n"
            "**AND अङ् IS NAMED WITH ITS न् TO CONFINE THE "
            "REFUSAL.** **अङ् अञ्चतिः क्विन्नन्तस्तस्य सनकारस्य "
            "ग्रहणं विषयावधारणार्थम्, यत्रास्य नलोपो नास्ति तत्र "
            "प्रतिषेधो यथा स्यात्** — where 6.4.30 keeps the न्, the "
            "refusal bites; where the न् is gone, **प्राचा, प्राचे, "
            "प्राग्भ्याम्** take the accent"),
    Accent(
        "6.1.183", refuses=True, of=("div",), before="jhalādi-vibhakti",
        blocks=("6.1.168", "6.1.171"),
        keeps_out="दिवा, दिवे — vowel-initial endings, where 6.1.171 "
                  "still gives the accent",
        why="दिवो झल् — after दिव् a झल्-initial ending is not "
            "accented: **द्युभ्याम्, द्युभिः**. The refusal reaches "
            "two rules at once, since दिव् is named in 6.1.171 and "
            "is one-syllabled for 6.1.168"),
    Accent(
        "6.1.184", refuses=True, of=("nṛ",), before="jhalādi-vibhakti",
        optional=True, blocks=("6.1.179",),
        keeps_out="न्रा, न्रे — vowel-initial",
        why="नृ चान्यतरस्याम् — and after नृ the same refusal is a "
            "choice: **नृभ्याम्, नृभिः, नृभ्यः, नृषु** beside the "
            "accented forms"),
    Accent(
        "6.1.185", puts="svarita", marker="tit", blocks=("3.1.3",),
        why="तित् स्वरितम् — an affix marked त् takes the स्वरित, and "
            "this is the first rule of the pāda that gives one: "
            "**चिकीर्ष्यम्, जिहीर्ष्यम्** with यत्; **कार्यम्, "
            "हार्यम्** with 3.1.124's ण्यत्. "
            "**प्रत्ययाद्युदात्तस्यापवादः** — an exception to "
            "3.1.3, which would put an उदात्त on the affix's first "
            "syllable instead"),
    Accent(
        "6.1.186", puts="anudātta", before="la-sārvadhātuka",
        after="tāsi-anudāttet-ṅit-adupadeśa",
        keeps_out="ह्नुते, यदधीते — ह्नुङ् and इङ् are excepted; "
                  "चिनुतः, चिन्वन्ति — the ङ् of श्नु looks to what "
                  "comes after it and not before; शिश्ये — लिट् is "
                  "no सार्वधातुक",
        why="तास्यनुदात्तेङ्ङिदद्रुपदेशाल्लसार्वधातुकमनुदात्तमह्न्विङोः "
            "— a सार्वधातुक ending is unaccented after the तास् of "
            "the periphrastic future, after a root the धातुपाठ "
            "marked अनुदात्त or ङित्, and after one taught ending in "
            "अ: **कर्ता, कर्तारौ; आस्ते, वस्ते; सूते, शेते; तुदतः, "
            "पचतः, पठतः**.\\n\\n"
            "**AND A ROOT TAKING शप् COUNTS AS TAUGHT WITH AN अ.** "
            "**अनुबन्धस्यानैकान्तिकत्वाद् अकारान्तोपदेश एव शप्** — "
            "the श् and प् being markers, what is left is the अ. "
            "**पचमानः, यजमानः**.\\n\\n"
            "**AND THIS ACCENT DISPLACES 6.1.163's.** "
            "**चित्स्वरोऽप्यनेन लसार्वधातुकानुदात्तत्वेन परत्वाद् "
            "बाध्यते** — being later, it wins"),
    Accent(
        "6.1.187", puts="udātta", where="ādi", before="sic",
        optional=True,
        why="आदिः सिचोऽन्यतरस्याम् — a सिच् aorist may take the "
            "accent on its first syllable: **मा हि कार्ष्टाम्** "
            "beside **मा हि कार्ष्टाम्**; **मा हि लाविष्टाम्** "
            "beside **मा हि लाविष्टाम्**.\\n\\n"
            "**AND THE च् OF सिच् IS WHAT PUTS THE OTHER ACCENT ON "
            "THE AUGMENT.** **सिचश्चित्करणाद् आगमानुदात्तत्वं हि "
            "बाध्यते** — an augment is unaccented as a rule, and "
            "6.1.163's चित् accent overrides it, so the इट् of "
            "लाविष्टाम् can carry the accent"),
    Accent(
        "6.1.188", puts="udātta", where="ādi", gana="svapādi",
        before="ac-aniṭ-la-sārvadhātuka", optional=True,
        keeps_out="स्वप्यात्, हिंस्यात् — consonant-initial; "
                  "स्वपितः, श्वसितः — the ending has its इट्; "
                  "स्वपानि, हिनसानि — not ङित्",
        why="स्वपादिहिंसामच्यनिटि — स्वप् and its list, and हिंस्, "
            "may take the accent on the first syllable before a "
            "vowel-initial सार्वधातुक ending without इट्: "
            "**स्वपन्ति, श्वसन्ति, हिंसन्ति** beside the "
            "middle-accented forms 3.1.3 gives"),
    Accent(
        "6.1.189", puts="udātta", where="ādi", gana="abhyasta",
        before="ac-aniṭ-la-sārvadhātuka", blocks=("6.1.188",),
        keeps_out="दद्यात् — consonant-initial; जक्षितः — with इट्",
        why="अभ्यस्तानामादिः — and for an अभ्यस्त the same accent is "
            "FIXED: **ददति, ददतु, दधति, जक्षति, जाग्रति**. "
            "**आदिरिति वर्तमाने पुनरादिग्रहणं नित्यार्थम्** — आदि "
            "was already carrying, and saying it again is how the "
            "rule sheds the option of the one before. The same "
            "device 6.1.32 and 6.1.57 used.\\n\\n"
            "**AND THIS IS THE RULE 6.1.5's उभे WAS SAID FOR.** The "
            "name अभ्यस्त belongs to the two copies TOGETHER, so the "
            "accent falls once, on the first vowel of the pair"),
    Accent(
        "6.1.190", puts="udātta", where="ādi", gana="abhyasta",
        before="anudātta-la-sārvadhātuka",
        why="अनुदात्ते च — and before an ending that has no उदात्त in "
            "it at all: **ददाति, जहाति, दधाति, जिहीते, मिमीते**. "
            "**अनजाद्यर्थ आरम्भः** — the rule exists for the "
            "consonant-initial endings the one before could not "
            "reach.\\n\\n"
            "**AND अनुदात्ते IS READ AS A बहुव्रीहि.** "
            "**अनुदात्त इति बहुव्रीहिनिर्देशो लोपयणादेशार्थः** — "
            "*that in which there is no उदात्त*, so a form whose "
            "ending has been partly dropped or turned into a "
            "semivowel is still reached: **मा हि स्म दधात्; "
            "दधात्यत्र**"),
    Accent(
        "6.1.191", puts="udātta", where="ādi", of=("sarva",),
        before="sup",
        keeps_out="सर्वतरः, सर्वतमः — तरप् and तमप् are no सुप्; "
                  "सर्वकः — with अकच् in the middle, 6.1.163 takes it",
        why="सर्वस्य सुपि — सर्व takes the accent on its first "
            "syllable before a case-ending: **सर्वः, सर्वौ, "
            "सर्वे**.\\n\\n"
            "**AND HERE प्रत्ययलक्षण DOES HOLD.** "
            "**प्रत्ययलक्षणेनाप्ययं स्वर इष्यते — सर्वस्तोमः** — the "
            "ending is gone and the accent stays, which 6.1.197 and "
            "6.1.199 both refuse to allow. Three rules of this pāda "
            "answer one question three ways"),
    Accent(
        "6.1.192", puts="udātta", where="pratyayāt-pūrva",
        gana="bhyādi", before="pit-la-sārvadhātuka",
        blocks=("6.1.189",),
        keeps_out="ददाति — not one of the nine; दरिद्रति — the "
                  "ending is not पित्",
        why="भीह्रीभृहुमदजनधनदरिद्राजागरां प्रत्ययात् पूर्वं पिति — "
            "nine roots take the accent on the syllable BEFORE the "
            "ending, where that ending is पित्: **बिभेति, जिह्रेति, "
            "बिभर्ति, जुहोति, ममत्तु, जजनत्, दधनत्, दरिद्राति, "
            "जागर्ति**. An exception to 6.1.189, and the first rule "
            "of the pāda to put the accent by counting back from the "
            "affix"),
    Accent(
        "6.1.193", puts="udātta", where="pratyayāt-pūrva",
        marker="lit",
        why="लिति — and before any affix marked ल्, the syllable "
            "before it: **चिकीर्षकः, जिहीर्षकः** with 3.1.133's "
            "ण्वुल्; **भौरिकिविधम्, ऐषुकारिभक्तम्** with 4.2.54's "
            "विधल् and भक्तल्"),
    Accent(
        "6.1.194", puts="udātta", where="ādi", before="ṇamul",
        optional=True, blocks=("6.1.193",),
        why="आदिर्णमुल्यन्यतरस्याम् — before णमुल् the first syllable "
            "may take it: **लोलूयंलोलूयम्** beside "
            "**लोलूयंलोलूयम्**. And the other side is 6.1.193's, the "
            "affix being लित्. The rule reaches only the doubled "
            "absolutives, 8.1.3 having made the second copy "
            "unaccented"),
    Accent(
        "6.1.195", puts="udātta", where="ādi", before="kartṛ-yak",
        after="ajanta-upadeśa", optional=True,
        keeps_out="भिद्यते स्वयमेव — the root does not end in a "
                  "vowel; लूयते केदारो देवदत्तेन — an agent is named, "
                  "so the sense is not reflexive",
        why="अचः कर्तृयकि — a root taught ending in a vowel may take "
            "the accent on its first syllable before the passive "
            "यक् used reflexively: **लूयते केदारः स्वयमेव** beside "
            "**लूयते**; **स्तीर्यते** beside **स्तीर्यते**.\\n\\n"
            "**AND THREE ROOTS COUNT AS VOWEL-FINAL THAT ARE NOT.** "
            "**जनादीनाम् उपदेश एवात्वं द्रष्टव्यम्। तत्राप्ययं स्वर "
            "इष्यते** — जन्, सन् and खन् take 6.4.43's आ, and the "
            "long vowel is treated as theirs from the धातुपाठ: "
            "**जायते, सायते, खायते**"),
    Accent(
        "6.1.196", puts="udātta", where="anywhere", before="thal-seṭ",
        optional=True,
        keeps_out="ययाथ — the थल् has no इट्, and only 6.1.193's "
                  "accent is left",
        why="थलि च सेटीडन्तो वा — before a थल् with its इट्, the "
            "accent may be on the इट्, on the ending, or on the "
            "first syllable — and with 6.1.193's fourth alternative "
            "**तेनैते चत्वारः स्वराः पर्यायेण भवन्ति**: "
            "**लुलविथ, लुलविथ, लुलविथ, लुलविथ**. One form and four "
            "accentuations, which is the largest option in the pāda "
            "and among the largest in the book"),
    Accent(
        "6.1.197", puts="udātta", where="ādi", marker="ñit-nit",
        blocks=("3.1.3",),
        keeps_out="गर्गाः, बिदाः, चञ्चाः — the affix is gone and its "
                  "accent with it",
        why="ञ्नित्यादिर्नित्यम् — whatever is made by an affix "
            "marked ञ् or न् takes the accent on its first syllable, "
            "invariably: **गार्ग्यः, वात्स्यः** with 4.1.105's यञ्; "
            "**वासुदेवकः, अर्जुनकः** with 4.3.98's वुन्. "
            "**प्रत्ययस्वरापवादोऽयं योगः**.\\n\\n"
            "**AND HERE प्रत्ययलक्षण DOES NOT HOLD.** "
            "**प्रत्ययलक्षणमत्र नेष्यते, तेन गर्गाः, बिदाः, चञ्चा "
            "इत्यत्र यञि कनि च लुप्ते न भवति** — the affix elided, "
            "its accent goes with it, where 6.1.191's did not"),
    Accent(
        "6.1.198", puts="udātta", where="ādi", before="āmantrita",
        blocks=("6.2.148",),
        why="आमन्त्रितस्य च — a vocative takes the accent on its "
            "first syllable: **देवदत्त, देवदत्तौ, देवदत्ताः**, "
            "displacing the end-accent 6.2.148 would give.\\n\\n"
            "**AND HERE प्रत्ययलक्षण HOLDS AGAIN, AGAINST 1.1.63.** "
            "**लुमतापि लुप्ते प्रत्ययलक्षणमत्रेष्यते** — even where "
            "a लुक्, लुप् or श्लु took the affix away: "
            "**सर्पिरागच्छ, सप्तागच्छत**. Three rules, three "
            "answers, and the pāda does not reconcile them"),
    Accent(
        "6.1.199", puts="udātta", where="ādi", of=("pathin", "mathin"),
        before="sarvanāmasthāna",
        keeps_out="पथः पश्य, मथः पश्य — a weak ending, and the accent "
                  "goes back to the end",
        why="पथिमथोः सर्वनामस्थाने — before a strong ending these two "
            "take the accent on the first syllable: **पन्थाः, "
            "पन्थानौ, पन्थानः; मन्थाः, मन्थानौ, मन्थानः**. Both are "
            "औणादिक इनि stems and end-accented by 3.1.3.\\n\\n"
            "**AND प्रत्ययलक्षण IS REFUSED HERE TOO.** "
            "**प्रत्ययलक्षणमत्रापि नेष्यते। पथिप्रियः** — in the "
            "compound the word keeps its own end-accent instead"),
    Accent(
        "6.1.200", puts="udātta", where="ādi-anta", before="tavai",
        blocks=("6.1.158", "3.1.3"),
        why="अन्तश्च तवै युगपत् — an infinitive in तवै takes the "
            "accent on its FIRST and LAST syllables AT ONCE: "
            "**कर्तवै, हर्तवै**.\\n\\n"
            "**AND युगपत् IS SAID AGAINST THE PARIBHĀṢĀ THAT GOVERNS "
            "IT.** **युगपद्ग्रहणं पर्यायनिवृत्त्यर्थम्। एकवर्जमिति "
            "वचनाद् यौगपद्यं न स्यात्** — 6.1.158 allows one accent "
            "to a word, so without this word the two would have been "
            "alternatives. The one rule of the pāda that breaks its "
            "own heading, and the heading is named as the reason it "
            "had to"),
    Accent(
        "6.1.201", puts="udātta", where="ādi", of=("kṣaya",),
        result="nivāsa", blocks=("3.1.3",),
        keeps_out="क्षयो वर्तते दस्यूनाम् — of loss, and formed with "
                  "3.3.56's अच् instead",
        why="क्षयो निवासे — क्षय takes the accent on its first "
            "syllable where it means a dwelling: **क्षये जागृहि "
            "प्रपश्यन्** — **क्षियन्ति निवसन्त्यस्मिन्निति क्षयः**. "
            "The word is 3.3.118's घ stem and would have taken the "
            "affix's accent"),
    Accent(
        "6.1.202", puts="udātta", where="ādi", of=("jaya",),
        result="karaṇa", blocks=("3.1.3",),
        keeps_out="जयो वर्तते ब्राह्मणानाम्",
        why="जयः करणम् — and जय where it means what one wins BY: "
            "**जयोऽश्वः** — **जयन्ति तेनेति जयः**. The same घ and "
            "the same displacement as the rule before, and the two "
            "are told apart by nothing but the sense"),
    Accent(
        "6.1.203", puts="udātta", where="ādi", gana="vṛṣādi",
        why="वृषादीनां च — a list, first-accented: **वृषः, जनः, "
            "ज्वरः, ग्रहः, हयः, गयः, नयः, अंशः, वेदः, सूदः, गुहा, "
            "मन्त्रः, शान्तिः, कामः, यामः, आरा, धारा, कारा, कल्पः, "
            "पादः**.\\n\\n"
            "**AND TWO OF ITS MEMBERS CARRY A CONDITION.** "
            "**शमरणौ संज्ञायां संमतौ भावकर्मणोः** — शम in the "
            "abstract sense and रण in the object sense; and "
            "**वहो गोचरादिषु**.\\n\\n"
            "**AND THE LIST IS AN आकृतिगण.** "
            "**वृषादिराकृतिगणः। अविहितमाद्युदात्तत्वं वृषादिषु "
            "द्रष्टव्यम्** — whatever first-syllable accent no rule "
            "accounts for belongs here, exactly as 6.1.157's "
            "पारस्करप्रभृति took whatever सुट् no rule explained. "
            "Two lists of that shape in one pāda"),
    Accent(
        "6.1.204", puts="udātta", where="ādi", before="upamāna",
        samjna=True,
        keeps_out="अग्निर्माणवकः — not a name; देवदत्तः — not a "
                  "likeness",
        why="संज्ञायामुपमानम् — a word used as a LIKENESS and serving "
            "as a name takes the accent on its first syllable: "
            "**चञ्चा, वर्ध्रिका, खरकुटी, दासी**.\\n\\n"
            "**AND THE RULE'S EXISTENCE IS THE ज्ञापक THAT "
            "प्रत्ययलक्षण IS NOT UNIVERSAL IN ACCENT.** The कन् of "
            "5.3.96 is dropped by 5.3.98, and 1.1.62 would have kept "
            "its first-syllable accent behind. **यद्येवं किमर्थम् "
            "इदम् उच्यते? प्रत्ययलक्षणेन सिद्धम् आद्युदात्तत्वम्? "
            "एतदेव ज्ञापयति क्वचिद् इह स्वरविधौ प्रत्ययलक्षणं न "
            "भवतीति** — a rule that would be idle if the maxim held "
            "everywhere, and so proves it does not"),
    Accent(
        "6.1.205", puts="udātta", where="ādi", before="niṣṭhā",
        after="dvyac-anāt", samjna=True, blocks=("3.1.3",),
        keeps_out="देवः, भीमः — not निष्ठा; चिन्तितः, रक्षितः — more "
                  "than two syllables; त्रातः, आप्तः — the first "
                  "syllable has an आ; कृतम्, हृतम् — not a name",
        why="निष्ठा च द्व्यजनात् — a two-syllabled निष्ठा participle "
            "serving as a name takes the accent on its first "
            "syllable, unless that syllable holds an आ: **दत्तः, "
            "गुप्तः, बुद्धः**. Four conditions, and the vṛtti gives "
            "a counter-example for each"),
    Accent(
        "6.1.206", puts="udātta", where="ādi",
        of=("śuṣka", "dhṛṣṭa"),
        why="शुष्कधृष्टौ — two words first-accented, and "
            "**असंज्ञार्थ आरम्भः** — the rule exists because they "
            "are NOT names and 6.1.205 could not reach them: "
            "**शुष्कः, धृष्टः**"),
    Accent(
        "6.1.207", puts="udātta", where="ādi", of=("āśita",),
        result="kartṛ", blocks=("6.2.144",),
        keeps_out="आशितमन्नम्, आशितं देवदत्तेन — the object and the "
                  "action, not the agent",
        why="आशितः कर्ता — आशित takes the accent on its first "
            "syllable where it names the one who has EATEN: "
            "**आशितो देवदत्तः**. Where the same form names the food "
            "or the eating it keeps 6.2.144's end-accent. One "
            "participle, three कारक, two accents"),
    Accent(
        "6.1.208", puts="udātta", where="ādi", of=("rikta",),
        optional=True,
        why="रिक्ते विभाषा — रिक्त optionally: **रिक्तः** beside "
            "**रिक्तः**. And where it IS a name, "
            "**संज्ञायां पूर्वविप्रतिषेधेन नित्यमाद्युदात्तः** — "
            "6.1.205 wins by being stated earlier, and the accent is "
            "fixed"),
    Accent(
        "6.1.209", puts="udātta", where="ādi", of=("juṣṭa", "arpita"),
        optional=True, chandasi=True,
        keeps_out="in ordinary speech both are end-accented by 3.1.3",
        why="जुष्टार्पिते च छन्दसि — two words optionally "
            "first-accented in the corpus: **जुष्टः** beside "
            "**जुष्टः**, **अर्पितः** beside **अर्पितः**"),
    Accent(
        "6.1.210", puts="udātta", where="ādi", of=("juṣṭa", "arpita"),
        mantra=True, blocks=("6.1.209",),
        why="नित्यं मन्त्रे — and in a मन्त्र the same two are fixed: "
            "**जुष्टं देवानाम्; अर्पितं पितॄणाम्**.\\n\\n"
            "**AND THE VṚTTI REPORTS A DISSENT AND A VERSE AGAINST "
            "ITSELF.** **केचिदत्र जुष्ट इत्येतदेवानुवर्तयन्ति। "
            "अर्पितशब्दस्य विभाषा मन्त्रेऽपीच्छन्ति** — some carry "
            "only जुष्ट down and want अर्पित optional even in a "
            "मन्त्र, and quote **शंकवोऽर्पिताः** where it is "
            "end-accented in one"),
    Accent(
        "6.1.211", puts="udātta", where="ādi",
        of=("yuṣmad", "asmad"), before="ṅas",
        why="युष्मदस्मदोर्ङसि — the genitive singular forms take the "
            "accent on the first syllable: **तव स्वम्, मम स्वम्**. "
            "Both stems are end-accented by their औणादिक affix, and "
            "8.2.5 would have put the accent on the second syllable "
            "of तव"),
    Accent(
        "6.1.212", puts="udātta", where="ādi",
        of=("yuṣmad", "asmad"), before="ṅe",
        why="ङयि च — and the dative singular: **तुभ्यम्, मह्यम्**. "
            "**पृथग्योगकरणं यथासंख्यशङ्कानिवृत्त्यर्थम्** — stated "
            "as a second sūtra rather than joined to the first, so "
            "that 1.3.10's pairing does not give the genitive to one "
            "stem and the dative to the other"),
    Accent(
        "6.1.213", puts="udātta", where="ādi", marker="yat",
        after="dvyac", blocks=("6.1.185",),
        keeps_out="नाव्यम् — after नौ; चिकीर्ष्यम्, ललाट्यम् — more "
                  "than two syllables",
        why="यतोऽनावः — a two-syllabled यत् stem takes the accent on "
            "its first syllable: **चेयम्, जेयम्** with 3.1.97's यत्; "
            "**कण्ठ्यम्, ओष्ठ्यम्** with 5.1.6's. "
            "**तित्स्वरितम् इत्यस्यापवादः** — an exception to "
            "6.1.185's स्वरित"),
    Accent(
        "6.1.214", puts="udātta", where="ādi",
        of=("īḍ", "vand", "vṛ", "śaṃs", "duh"), marker="ṇyat",
        blocks=("6.1.185",),
        why="ईडवन्दवृशंसदुहां ण्यतः — five roots before ण्यत्: "
            "**ईड्यम्, वन्द्यम्, वार्यम्, शंस्यम्, दोह्या "
            "धेनुः**.\\n\\n"
            "**AND ण्यत् IS NOT REACHED BY THE यत् OF THE RULE "
            "BEFORE.** **द्व्यनुबन्धकत्वाद् ण्यतो यद्ग्रहणेन ग्रहणं "
            "नास्ति** — having two markers, it is not named by the "
            "word यत्, so 6.1.185's स्वरित would have stood and this "
            "rule is stated against it"),
    Accent(
        "6.1.215", puts="udātta", where="ādi",
        of=("veṇu", "indhāna"), optional=True,
        why="विभाषा वेण्विन्धानयोः — two words optionally "
            "first-accented: **वेणुः** beside **वेणुः**; "
            "**इन्धानः** beside two other accentuations.\\n\\n"
            "**AND THE SECOND WORD WOULD NEVER HAVE HAD IT.** Read "
            "as a चानश् stem इन्धान is end-accented by 6.1.163; read "
            "as a शानच् stem it is middle-accented by 6.1.161. "
            "**तदेवम् इन्धाने सर्वथाप्राप्तम् आद्युदात्तत्वं पक्षे "
            "विधीयते** — no analysis gives it a first-syllable "
            "accent, and the rule supplies one.\\n\\n"
            "**AND THE OPTION LAPSES WHERE THE WORD IS A LIKENESS.** "
            "**वेणुरिव वेणुरित्युपमानं यदा संज्ञा भवति, तदा "
            "संज्ञायामुपमानम् इति नित्यम् आद्युदात्तत्वम् इष्यते**"),
    Accent(
        "6.1.216", puts="udātta", where="ādi",
        of=("tyāga", "rāga", "hāsa", "kuha", "śvaṭha", "kratha"),
        optional=True, blocks=("6.1.159",),
        why="त्यागरागहासकुहश्वठक्रथानाम् — six words optionally "
            "first-accented: **त्यागः, रागः, हासः, कुहः, श्वठः, "
            "क्रथः**, each beside its end-accented form. The first "
            "three are घञ् stems and take 6.1.159's accent on the "
            "other side; the last three are अच् stems"),
    Accent(
        "6.1.217", puts="udātta", where="upottama", marker="rit",
        blocks=("3.1.3",),
        why="उपोत्तमं रिति — a stem made by an affix marked र् takes "
            "the accent on the syllable before its last: "
            "**करणीयम्, हरणीयम्** with 3.1.96's अनीयर्; "
            "**पटुजातीयः, मृदुजातीयः** with 5.3.19's जातीयर्. And "
            "उपोत्तम requires three syllables, as it did at "
            "6.1.180"),
    Accent(
        "6.1.218", puts="udātta", where="upottama", before="caṅ",
        optional=True,
        keeps_out="मा हि दधत् — only two syllables, so there is no "
                  "penult",
        why="चङ्यन्यतरस्याम् — a चङ् aorist may take the accent on "
            "its penult: **मा हि चीकरताम्** beside **मा हि "
            "चीकरताम्**. The other side is the चित् accent of चङ् "
            "itself"),
    Accent(
        "6.1.219", puts="udātta", where="matoḥ-pūrva-āt",
        before="matup", samjna=True, stri=True,
        keeps_out="इक्षुमती, द्रुमवती — the vowel before मत् is not "
                  "आ; खट्वावती — not a name; शरावान् — not feminine; "
                  "गवादिनी — not मतुप्",
        why="मतोः पूर्वमात् संज्ञायां स्त्रियाम् — the आ before मतुप् "
            "takes the accent where the word is a feminine NAME: "
            "**उदुम्बरावती, पुष्करावती, वीरणावती, शरावती**, the "
            "lengthening being 6.3.120's. Four conditions, and the "
            "vṛtti gives a counter-example for each"),
    Accent(
        "6.1.220", puts="udātta", where="anta", after="avatī",
        samjna=True, blocks=("3.1.4",),
        keeps_out="राजवती — really राजन्वती, and the न् dropped is "
                  "not visible to an accent rule",
        why="अन्तोऽवत्याः — a name ending in अवती takes the accent on "
            "its last syllable: **अजिरवती, खदिरवती, हंसवती, "
            "कारण्डवती**. The ङीप् is पित् and would have been "
            "unaccented.\\n\\n"
            "**AND अवती IS WRITTEN WITH ITS अ FOR A REASON.** "
            "**अवत्या इति किमुच्यते, न वत्या इत्येवमुच्येत? नैवं "
            "शक्यम्, इहापि स्यात् — राजवती। स्वरविधौ नलोपस्या"
            "सिद्धत्वाद् नायमवतीशब्दः** — the न् of राजन् is dropped "
            "by a rule of the त्रिपादी, and 8.2.1 makes that "
            "invisible here, so the word is still राजन्वती and is "
            "not reached. **वत्वं पुनराश्रयात् सिद्धम्** — the म् "
            "becoming व् IS visible, being what the rule rests on"),
    Accent(
        "6.1.221", puts="udātta", where="anta", after="īvatī",
        samjna=True, stri=True,
        why="ईवत्याः — and a feminine name ending in ईवती takes "
            "the accent on its last syllable likewise: **अहीवती, "
            "कृषीवती, मुनीवती**. The rule before it named अवती "
            "with its अ for a reason and this one names ईवती with its "
            "ई for the same one — the shape is what is reached, not the "
            "affix that made it"),
    Accent(
        "6.1.222", puts="udātta", where="anta", before="cu",
        blocks=("6.1.161",),
        keeps_out="दाधीचः, माधूचः — a taddhita follows, and the "
                  "affix's own accent takes over",
        why="चौ — before the अञ्च् whose न् has been dropped, the "
            "word in front takes the accent on its last syllable: "
            "**दधीचः पश्य, दधीचा, दधीचे; मधूचः, मधूचा**. "
            "**उदात्तनिवृत्तिस्वरापवादोऽयम्**. And a supplement "
            "confines it — **चावतद्धित इति वक्तव्यम्**"),
    Accent(
        "6.1.223", puts="udātta", where="anta", before="samāsa",
        why="समासस्य — a compound takes the accent on its last "
            "syllable: **राजपुरुषः, ब्राह्मणकम्बलः, कन्यास्वनः, "
            "पटहशब्दः, नदीघोषः; राजपृषत्, ब्राह्मणसमित्**. "
            "**नानापदस्वरस्यापवादः** — the several words each had an "
            "accent and the compound has one.\\n\\n"
            "**AND A CONSONANT-FINAL COMPOUND STILL HAS ITS ACCENT "
            "ON A VOWEL.** **स्वरविधौ व्यञ्जनमविद्यमानवद् इति "
            "हलन्तेऽप्यन्तोदात्तत्वं भवति** — the same maxim 6.1.176 "
            "refused, used here without argument. And this rule "
            "closes the pāda: the exceptions to it are 6.2's whole "
            "business"),
)


@dataclass(frozen=True)
class Accented:
    """What the resolver answers with."""

    puts: str
    where: str
    sutra: str
    why: str
    optional: bool = False
    bhasayam: bool = False
    chandasi: bool = False
    mantra: bool = False
    #: Where a rule displaces or refuses another, that rule's number.
    blocked_by: Tuple[str, ...] = ()


def _reaches(row: Accent, stem: str, gana: str, marker: str,
             before: str, after: str, result: str, samjna: bool,
             stri: bool, chandasi: bool, mantra: bool,
             bhasayam: bool) -> bool:
    # 6.1.158 is a परिभाषा: it clears the other syllables out of the
    # way of whichever rule speaks, and names none of its own.
    if row.heading:
        return False
    if row.chandasi and not chandasi:
        return False
    if row.mantra and not mantra:
        return False
    if row.bhasayam and not bhasayam:
        return False
    if row.samjna and not samjna:
        return False
    if row.stri and not stri:
        return False
    if row.of and stem not in row.of:
        return False
    if row.gana and gana != row.gana:
        return False
    if row.marker and marker != row.marker:
        return False
    if row.before and before != row.before:
        return False
    if row.after and after != row.after:
        return False
    if row.result and result != row.result:
        return False
    return True


def _supplies(row: Accent, wants: str) -> bool:
    if not wants:
        return True
    return wants == row.puts and not row.refuses


def _how_specific(row: Accent) -> int:
    """
    A refusal beats what it refuses, and a named word beats a class.

    A SENSE counts highest after that, because 6.1.201 and 6.1.202
    are told apart by nothing else: both name one word, both put the
    accent on the first syllable, and both displace 3.1.3.

    And the corpus counts, in both directions. 6.1.180 and 6.1.181
    are scored alike otherwise, and the second says only that the
    first is a choice भाषायाम् — the one rule of the pāda whose
    condition is that the language is not Vedic.
    """
    return (
        10 * bool(row.refuses)
        + 8 * bool(row.of)
        + 7 * bool(row.result)
        + 5 * bool(row.marker)
        + 4 * bool(row.after)
        + 3 * bool(row.before)
        + 3 * bool(row.samjna)
        + 2 * bool(row.gana)
        + 2 * bool(row.mantra)
        + 2 * bool(row.chandasi)
        + 2 * bool(row.bhasayam)
        + 1 * bool(row.stri)
    )


def accent_of(stem: str = "", *, gana: str = "", marker: str = "",
              before: str = "", after: str = "", result: str = "",
              samjna: bool = False, stri: bool = False,
              chandasi: bool = False, mantra: bool = False,
              bhasayam: bool = False, wants: str = "") -> Accented:
    """
    6.1.158–223 — which syllable of a word takes the accent.

    6.1.158 supplies nothing. It is a परिभाषा that makes every OTHER
    syllable अनुदात्त once some rule has spoken, so a question no
    rule reaches gets nothing rather than a default.
    """
    matched = [
        row for row in ACCENT_TABLE
        if _reaches(row, stem, gana, marker, before, after, result,
                    samjna, stri, chandasi, mantra, bhasayam)
        and _supplies(row, wants)
    ]
    if not matched:
        return Accented(
            "", "", "", "No rule of 6.1.158–223 is reached. 6.1.158 "
                        "is a परिभाषा — it clears the other "
                        "syllables out of the way of whichever rule "
                        "speaks, and speaks for none itself")
    row = max(matched, key=_how_specific)
    return Accented(
        "" if row.refuses else row.puts,
        "" if row.refuses else row.where,
        row.sutra, row.why, optional=row.optional,
        bhasayam=row.bhasayam, chandasi=row.chandasi,
        mantra=row.mantra, blocked_by=row.blocks)


def ekavarja() -> Accented:
    """
    The परिभाषा itself, with the verse that says why एकवर्जम् is
    said and the line that says which of the four accents wins.
    """
    return Accented(
        "anudātta", "", "6.1.158",
        "अनुदात्तं पदमेकवर्जम् — every syllable but one is अनुदात्त, "
        "and the one excepted is whichever a rule names. %s। %s॥ And "
        "when the four compete: %s"
        % (EKAVARJA_VERSE[0], EKAVARJA_VERSE[1], WHICH_WINS))


def provisions_for(sutra_id: str) -> Tuple[Accent, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in ACCENT_TABLE if row.sutra == sutra_id)
