# -*- coding: utf-8 -*-
"""
६.३.११४–१३९ — संहितायाम्, and twenty-five lengthenings.

The pāda's last heading, and the only one of its four that is
about the CONDITION of speech rather than about a position or an
operation. **संहितायामित्ययम् अधिकारः। यदित ऊर्ध्वम्
अनुक्रमिष्यामः संहितायाम् इत्येवं तद् वेदितव्यम्** — everything
from here happens only in connected speech, and 6.3.114's own
counter-example is the words said apart: **संहितायामिति किम्?
विद्म, हि, त्वा, गोपतिम्, शूर, गोनाम्**.

Under it, twenty-five rules and one operation. Every one of them
lengthens the first member's vowel, and they differ only in what
they are lengthening it before: कर्ण, a क्विप्-formed root, वन
and गिरि, वल, मतुप्, वह, a घञ्, काश, a त्-initial substitute for
दा, and then — from 6.3.131 — the Veda alone, where a मन्त्र
lengthens सोम and अश्व, an ऋच् lengthens eight particles, and
6.3.135 lengthens the final अ of any two-syllabled verb.

**AND TWICE THE RUN GIVES UP ON DESCRIBING ITSELF.** 6.3.137
अन्येषाम् अपि दृश्यते — **यस्य दीर्घत्वं न विहितम्, दृश्यते च
प्रयोगे, तद् अनेन कर्तव्यम्** — the same shape 6.3.109
पृषोदरादीनि had, and for the same reason: what is attested is
correct whether or not a rule reaches it.

**AND THE PĀDA CLOSES ON AN ARGUMENT ABOUT ORDER.** 6.3.139
संप्रसारणस्य lengthens कारीषगन्धी before पुत्र — and 6.3.61
would have SHORTENED the same vowel. The vṛtti settles it twice
over: **व्यवस्थितविभाषा हि सा**, and then **सकृद्गतौ विप्रतिषेधे
यद् बाधितं तद् बाधितम् एव** — once a rule has been set aside in a
conflict it does not come back for a second try.

**WHAT THIS MODULE DOES NOT DO.** It reports whether the first
member lengthens and by which rule. It does not scan: that
6.3.119 wants MANY vowels and 6.3.135 wants exactly two are
conditions the query carries.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: The pāda's last heading, and its last run:
#: **संहितायामित्ययम् अधिकारः**.
SAMHITA_RUN: Tuple[str, str] = ("6.3.114", "6.3.139")

#: 6.3.115's nine exceptions — every one of them a word that
#: could name a mark on an ear and does not lengthen.
KARNA_EXCEPT: Tuple[str, ...] = (
    "viṣṭa", "aṣṭan", "pañcan", "maṇi", "bhinna", "chinna",
    "chidra", "sruva", "svastika")

#: 6.3.116's seven roots, each taken with क्विप् on it.
KVIP_ROOTS: Tuple[str, ...] = (
    "nah", "vṛt", "vṛṣ", "vyadh", "ruc", "sah", "tan")

#: 6.3.117's two gaṇas, matched one to one with वन and गिरि.
KOTARADI: Tuple[str, ...] = (
    "koṭara", "miśraka", "puraga", "sidhraka", "sārika")
KIMSULAKADI: Tuple[str, ...] = (
    "kiṃśulaka", "śālvaka", "añjana", "bhañjana", "lohita",
    "kukkuṭa")

#: 6.3.120's शरादि, which lengthen before मतुप् though 6.3.119's
#: condition of many vowels does not hold of them.
SARADI: Tuple[str, ...] = (
    "śara", "vaṃśa", "dhūma", "ahi", "kapi", "maṇi", "muni",
    "śuci", "hanu")

#: 6.3.131's four, lengthened before मतुप् in a मन्त्र.
MANTRA_FOUR: Tuple[str, ...] = (
    "soma", "aśva", "indriya", "viśvadevya")

#: 6.3.133's eight particles, lengthened in an ऋच्.
RCI_EIGHT: Tuple[str, ...] = (
    "tu", "nu", "gha", "makṣu", "taṅ", "ku", "tra", "uruṣya")

#: What a vārttika on 6.3.137 adds for श्वन् alone.
SVAN_VARTIKA: Tuple[str, ...] = (
    "danta", "daṃṣṭrā", "karṇa", "kunda", "varāha", "puccha",
    "pada")


@dataclass(frozen=True)
class Dirgha:
    """One rule of 6.3.114–139: what lengthens, and before what."""

    sutra: str
    #: dīrgha throughout, or empty for the heading.
    does: str = ""
    #: The first members the rule names outright.
    of: Tuple[str, ...] = ()
    #: A named class of first member instead.
    gana: str = ""
    #: What must FOLLOW.
    before: Tuple[str, ...] = ()
    #: Where a class of first member is matched one to one with a
    #: following word — यथासंख्यम्.
    pairs: Tuple[Tuple[str, str], ...] = ()
    #: The further condition — a sense, a register, a shape.
    result: Tuple[str, ...] = ()
    excludes: Tuple[str, ...] = ()
    optional: bool = False
    bahulam: bool = False
    chandasi: bool = False
    heading: bool = False
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


DIRGHA_TABLE: Tuple[Dirgha, ...] = (
    Dirgha(
        "6.3.114", heading=True,
        why="संहितायाम् — **संहितायामित्ययम् अधिकारः। यदित "
            "ऊर्ध्वम् अनुक्रमिष्यामः संहितायाम् इत्येवं तद् "
            "वेदितव्यम्** — from here everything holds in "
            "CONNECTED SPEECH only. The vṛtti reads the run's own "
            "last-but-four sūtra out as its example: **वक्ष्यति "
            "द्व्यचोऽतस्तिङः इति — विद्मा हि त्वा गोपतिं शूर "
            "गोनाम्**.\\n\\n"
            "**AND THE COUNTER-EXAMPLE IS THE SAME WORDS SAID "
            "APART.** **संहितायामिति किम्? विद्म, हि, त्वा, "
            "गोपतिम्, शूर, गोनाम्** — one line quoted twice over, "
            "joined and then separated, and the lengthening is "
            "there in the first and gone in the second. The "
            "fourth heading of the pāda, and the only one that is "
            "about the condition of speech rather than about a "
            "position or an operation"),
    Dirgha(
        "6.3.115", does="dīrgha", gana="lakṣaṇa", before=("karṇa",),
        excludes=KARNA_EXCEPT,
        keeps_out="शोभनकर्णः — no mark meant; विष्टकर्णः, "
                  "अष्टकर्णः, मणिकर्णः, छिन्नकर्णः — the nine the "
                  "sūtra names out",
        why="कर्णे लक्षणस्याविष्टाष्टपञ्चमणिभिन्नच्छिन्नच्छिद्रस्रुव"
            "स्वस्तिकस्य — a word naming a MARK lengthens before "
            "कर्ण, nine excepted: **दात्राकर्णः, द्विगुणाकर्णः, "
            "त्रिगुणाकर्णः, द्व्यङ्गुलाकर्णः, अङ्गुलाकर्णः**.\\n\\n"
            "**AND लक्षण IS THE SAME BRAND 6.2.112 MEANT.** **यत् "
            "पशूनां स्वामिविशेषसंबन्धज्ञापनार्थं दात्राकारादि "
            "क्रियते, तद् इह लक्षणं गृह्यते** — the nick cut in a "
            "beast's ear to show whose herd it is, word for word "
            "the gloss the accent rule of the pāda before had "
            "given"),
    Dirgha(
        "6.3.116", does="dīrgha", before=KVIP_ROOTS,
        result=("kvip",),
        keeps_out="परिणहनम् — no क्विप्, and no lengthening",
        why="नहिवृतिवृषिव्यधिरुचिसहितनिषु क्वौ — the first member "
            "lengthens before seven roots with क्विप् on them: "
            "**उपानत्, परीणत्** (नह्); **नीवृत्, उपावृत्** (वृत्); "
            "**प्रावृट्** (वृष्); **मर्मावित्, हृदयावित्, "
            "श्वावित्** (व्यध्); **नीरुक्, अभीरुक्** (रुच्); "
            "**ऋतीषट्** (सह्); **परीतत्** (तन्).\\n\\n"
            "**AND THE LAST OF THE SEVEN NEEDS A RULE BORROWED "
            "FROM ANOTHER PLACE.** **गमः क्वौ इति गमादीनाम् "
            "इष्यते। ततस् तनोतेर् अपि अनुनासिकलोपः** — 6.4.40 is "
            "stated of गम् and its fellows, and तन् has to be "
            "read into it or परीतत् loses no nasal"),
    Dirgha(
        "6.3.117", does="dīrgha",
        pairs=(("koṭarādi", "vana"), ("kiṃśulakādi", "giri")),
        result=("saṃjñā",),
        keeps_out="असिपत्रवनम्, कृष्णगिरिः — neither first member "
                  "is in its gaṇa",
        why="वनगिर्योः संज्ञायां कोटरकिंशुलकादीनाम् — before वन "
            "and गिरि, in a NAME, the कोटरादि and किंशुलकादि "
            "words lengthen, matched ONE TO ONE: **कोटरावणम्, "
            "मिश्रकावणम्, सिध्रकावणम्, सारिकावणम्** for वन; "
            "**किंशुलकागिरिः, अञ्जनागिरिः** for गिरि. Crossing "
            "them is not Sanskrit: the gaṇas go **यथासंख्यम्**"),
    Dirgha(
        "6.3.118", does="dīrgha", before=("valac",),
        excludes=("utsāha", "bhrātṛ", "pitṛ"),
        keeps_out="उत्साहवलः, भ्रातृवलः, पितृवलः — the three "
                  "carried down as exceptions",
        why="वले — the first member lengthens before वल: "
            "**आसुतीवलः, कृषीवलः, दन्तावलः**.\\n\\n"
            "**AND वल IS THE AFFIX AND NOT THE WORD.** "
            "**रजःकृष्यासुतिपरिषदो वलच् इति वलच्प्रत्ययो गृह्यते, "
            "न प्रातिपदिकम्** — 5.2.112's affix, so a stem that "
            "merely ends in the syllable is not reached. And "
            "three exceptions come down from the sūtras before: "
            "**अनुत्साहभ्रातृपितृणाम् इत्येव**"),
    Dirgha(
        "6.3.119", does="dīrgha", result=("bahvac-saṃjñā",),
        before=("matup",), excludes=("ajirādi",),
        keeps_out="व्रीहिमती — व्रीहि has few vowels; अजिरवती, "
                  "खदिरवती, पुलिनवती — the अजिरादि words; "
                  "वलयवती — not a name",
        why="मतौ बह्वचोऽनजिरादीनाम् — a first member of MANY "
            "vowels lengthens before मतुप् in a NAME, the "
            "अजिरादि words excepted: **उदुम्बरावती, मशकावती, "
            "वीरणावती, पुष्करावती, अमरावती** — river-names, by "
            "4.2.85's **नद्यां मतुप्**, and the व् of the affix "
            "by 8.2.11's **संज्ञायाम्**"),
    Dirgha(
        "6.3.120", does="dīrgha", gana="śarādi", before=("matup",),
        result=("saṃjñā",),
        why="शरादीनां च — and the शरादि words before मतुप् in a "
            "name: **शरावती, वंशावती**. They are named because "
            "6.3.119's condition of many vowels does not hold of "
            "them. The list runs **शर। वंश। धूम। अहि। कपि। मणि। "
            "मुनि। शुचि। हनु**, and the vṛtti adds why the व् "
            "appears here and not everywhere: **यवादित्वाद् "
            "व्रीह्यादिभ्यो न भवति**"),
    Dirgha(
        "6.3.121", does="dīrgha", gana="ik-anta", before=("vaha",),
        excludes=("pīlu", "dāru"),
        keeps_out="पिण्डवहम् — not इक्-final; पीलुवहम् — named "
                  "out; दारुवहम् — by the vārttika "
                  "**अपील्वादीनाम् इति वक्तव्यम्**",
        why="इको वहेऽपीलोः — an इक्-final first member lengthens "
            "before वह, पीलु excepted: **ऋषीवहम्, कपीवहम्, "
            "मुनीवहम्** — what carries a seer, an ape, a sage"),
    Dirgha(
        "6.3.122", does="dīrgha", gana="upasarga", before=("ghañ",),
        excludes=("manuṣya",), bahulam=True,
        keeps_out="निषादो मनुष्यः — a man, which the sūtra shuts "
                  "out; प्रसेवः, प्रसारः — the conditions hold and "
                  "the lengthening does not, बहुलम् being what it "
                  "is",
        why="उपसर्गस्य घञ्यमनुष्ये बहुलम् — an उपसर्ग lengthens "
            "VARIOUSLY before a घञ्-formed second member, where "
            "no man is named: **वीक्लेदः, वीमार्गः, अपामार्गः**, "
            "and **न च भवति — प्रसेवः, प्रसारः**.\\n\\n"
            "**AND TWO VĀRTTIKAS SPLIT THE बहुलम् INTO CASES.** "
            "**सादकारयोः कृत्रिमे दीर्घो भवति — प्रासादः, "
            "प्राकारः**, and only of what is MADE: **कृत्रिम इति "
            "किम्? प्रसादः, प्रकारः**. And **वेशादिषु विभाषा "
            "दीर्घो भवति — प्रतिवेशः, प्रतीवेशः; प्रतिरोधः, "
            "प्रतीरोधः**"),
    Dirgha(
        "6.3.123", does="dīrgha", gana="ik-anta-upasarga",
        before=("kāśa",),
        keeps_out="प्रकाशः — प्र is not इक्-final",
        why="इकः काशे — an इक्-final उपसर्ग lengthens before काश: "
            "**नीकाशः, वीकाशः, अनूकाशः**. And which काश: "
            "**पचाद्यच्प्रत्ययान्तोऽयं काशशब्दो न तु घञन्तः** — "
            "the अच्-formed one, not the घञ्-formed one 6.3.122 "
            "would have reached"),
    Dirgha(
        "6.3.124", does="dīrgha", gana="ik-anta-upasarga",
        before=("ti-ādeśa",), result=("dā",),
        keeps_out="प्रत्तम्, अवत्तम् — प्र and अव are not "
                  "इक्-final; वितीर्णम्, नितीर्णम् — the root is "
                  "not दा; सुदत्तम् — the substitute does not "
                  "begin with त्",
        why="दस्ति — an इक्-final उपसर्ग lengthens before a "
            "त्-initial substitute for दा: **नीत्तम्, वीत्तम्, "
            "परीत्तम्**.\\n\\n"
            "**AND THE SUBSTITUTE ONLY LOOKS त्-INITIAL AFTER "
            "ANOTHER RULE HAS ACTED.** **अच उपसर्गात् तः "
            "इत्यन्तस्य यद्यपि तकारः क्रियते, तथापि "
            "चर्त्वस्याश्रयात् सिद्धत्वम् इति तकारादिर्भवति** — "
            "7.4.47 makes a त् of the FINAL, and it is only "
            "because चर्त्व is already settled that the whole "
            "substitute counts as beginning with one"),
    Dirgha(
        "6.3.125", does="dīrgha", of=("aṣṭan",),
        result=("saṃjñā",),
        keeps_out="अष्टपुत्रः, अष्टभार्यः — not a name",
        why="अष्टनः संज्ञायाम् — अष्टन् lengthens before a second "
            "member where the compound is a NAME: **अष्टावक्रः, "
            "अष्टाबन्धुरः, अष्टापदम्** — the eight-bent sage, the "
            "chessboard"),
    Dirgha(
        "6.3.126", does="dīrgha", of=("aṣṭan",), chandasi=True,
        why="छन्दसि च — and in the Veda, name or no name: "
            "**आग्नेयम् अष्टाकपालं निर्वपेत्; अष्टाहिरण्या "
            "दक्षिणा; अष्टापदी देवता सुमती**. A vārttika adds one "
            "case outside the Veda: **गवि च युक्ते भाषायाम् "
            "अष्टनो दीर्घो भवतीति वक्तव्यम् — अष्टागवं शकटम्**"),
    Dirgha(
        "6.3.127", does="dīrgha", of=("citi",), before=("kap",),
        why="चितेः कपि — चिति lengthens before कप्: **एकचितीकः, "
            "द्विचितीकः, त्रिचितीकः** — of one layer, of two, of "
            "three"),
    Dirgha(
        "6.3.128", does="dīrgha", of=("viśva",),
        before=("vasu", "rāj"),
        keeps_out="विश्वराजौ, विश्वराजः — the second member is "
                  "राज् and not राज्, **राडिति विकारनिर्देशः**",
        why="विश्वस्य वसुराटोः — विश्व lengthens before वसु and "
            "राज्: **विश्वावसुः, विश्वाराट्**.\\n\\n"
            "**AND राट् IS NAMED IN ITS ALTERED SHAPE ON "
            "PURPOSE.** **राडिति विकारनिर्देशो यत्रास्यैतद् रूपं "
            "तत्रैव यथा स्यात्** — the sūtra writes the word as it "
            "comes out, so the rule reaches only where it comes "
            "out that way. **इह न भवति — विश्वराजौ, विश्वराजः**"),
    Dirgha(
        "6.3.129", does="dīrgha", of=("viśva",), before=("nara",),
        result=("saṃjñā",),
        keeps_out="विश्वनरः — **विश्वे नरा यस्य**, and no name",
        why="नरे संज्ञायाम् — and before नर, in a NAME: "
            "**विश्वानरो नाम यस्य वैश्वानरिः पुत्रः**"),
    Dirgha(
        "6.3.130", does="dīrgha", of=("viśva",), before=("mitra",),
        result=("ṛṣi",),
        keeps_out="विश्वमित्रो माणवकः — a boy of that name and no "
                  "seer",
        why="मित्रे चर्षौ — and before मित्र, where a SEER is "
            "meant: **विश्वामित्रो नाम ऋषिः**. The pāda before "
            "had the same name at 6.2.165, where a vārttika kept "
            "the seers out of an accent rule; here the seer is "
            "the whole condition"),
    Dirgha(
        "6.3.131", does="dīrgha", of=MANTRA_FOUR,
        before=("matup",), result=("mantra",),
        why="मन्त्रे सोमाश्वेन्द्रियविश्वदेव्यस्य मतौ — in a "
            "मन्त्र, four words lengthen before मतुप्: "
            "**सोमावती, अश्वावती, इन्द्रियावती, विश्वदेव्यावती**"),
    Dirgha(
        "6.3.132", does="dīrgha", of=("oṣadhi",),
        before=("vibhakti",), result=("mantra",),
        excludes=("prathamā",),
        keeps_out="ओषधिपते — no case ending follows; स्थिरेयम् "
                  "अस्त्वोषधिः — a nominative, which the sūtra "
                  "shuts out",
        why="ओषधेश्च विभक्तावप्रथमायाम् — and ओषधि lengthens "
            "before any case ending but the nominative, still in "
            "a मन्त्र: **ओषधीभिः पुनीतात्; नमः पृथिव्यै नम "
            "ओषधीभ्यः**. **मन्त्र इति वर्तते**"),
    Dirgha(
        "6.3.133", does="dīrgha", of=RCI_EIGHT, result=("ṛc",),
        keeps_out="शृणोत ग्रावाणः — the थ there is not the ङित् "
                  "substitute तङ्, **तङिति थादेशस्य ङित्त्वपक्षे "
                  "ग्रहणम्**",
        why="ऋचि तुनुघमक्षुतङ्कुत्रोरुष्याणाम् — in an ऋच्, eight "
            "particles lengthen: **आ तू न इन्द्र वृत्रहन्** (तु); "
            "**नू करणे** (नु); **उत वा घा स्यालात्** (घ); "
            "**मक्षू गोमन्तमीमहे** (मक्षु); **भरता जातवेदसम्** "
            "(तङ्); **कूमनः** (कु); **अत्रा गौः** (त्र); "
            "**उरुष्या णो अभिशस्तेः** (उरुष्य)"),
    Dirgha(
        "6.3.134", does="dīrgha", gana="ik-anta", before=("suñ",),
        result=("mantra",),
        why="इकः सुञि — an इक्-final word lengthens before the "
            "particle सु, in a मन्त्र: **अभी षु णः सखीनाम्; "
            "ऊर्ध्व ऊ षु ण ऊतये**. **सुञ् निपातो गृह्यते** — the "
            "particle and not the affix. The ष् is 8.3.105's and "
            "the ण् is 8.4.27's"),
    Dirgha(
        "6.3.135", does="dīrgha", gana="dvyac-tiṅ", result=("ṛc",),
        keeps_out="अश्वा भवत वाजिनः — भवत has three vowels; आ "
                  "देवान् वक्षि यक्षि च — the verb does not end "
                  "in अ",
        why="द्व्यचोऽतस्तिङः — in an ऋच्, a TWO-SYLLABLED finite "
            "verb ending in अ lengthens that अ: **विद्मा हि त्वा "
            "गोपतिं शूर गोनाम्; विद्मा शरस्य पितरम्**. This is "
            "the sūtra 6.3.114's vṛtti read out as the heading's "
            "own example, twenty-one sūtras before reaching it"),
    Dirgha(
        "6.3.136", does="dīrgha", gana="nipāta", result=("ṛc",),
        why="निपातस्य च — and any particle, in an ऋच्: **एवा ते; "
            "अच्छा**. **ऋचीत्येव** — the condition is carried "
            "down and not restated"),
    Dirgha(
        "6.3.137", does="dīrgha", gana="anyeṣām-api",
        why="अन्येषामपि दृश्यते — and a lengthening is SEEN in "
            "other words too: **यस्य दीर्घत्वं न विहितम्, "
            "दृश्यते च प्रयोगे, तद् अनेन कर्तव्यम्। स "
            "शिष्टप्रयोगाद् अनुगन्तव्यः** — **केशाकेशि, कचाकचि, "
            "जलाषाट्, नारकः, पूरुषः**. The same shape 6.3.109 "
            "पृषोदरादीनि had, twenty-eight sūtras earlier, and "
            "for the same reason.\\n\\n"
            "**AND A VĀRTTIKA MAKES ONE STEM'S CASE EXACT.** "
            "**शुनो दन्तदंष्ट्राकर्णकुन्दवराहपुच्छपदेषु — "
            "श्वादन्तः, श्वादंष्ट्रः, श्वाकर्णः, श्वाकुन्दः, "
            "श्वावराहः, श्वापुच्छः, श्वापदः** — seven second "
            "members named for श्वन् alone, so that at least one "
            "corner of the catch-all is decidable"),
    Dirgha(
        "6.3.138", does="dīrgha", before=("cu",),
        why="चौ — the first member lengthens before चु: "
            "**दधीचः पश्य, दधीचा, दधीचे; मधूचः पश्य, मधूचा, "
            "मधूचे**. And चु is अञ्चति in a particular state: "
            "**चावित्यञ्चतिर्लुप्तनकाराकारो गृह्यते** — with its "
            "न् and its अ already gone.\\n\\n"
            "**AND AN INNER RULE IS HELD OFF BY THIS ONE'S MERE "
            "EXISTENCE.** **अन्तरङ्गोऽपि हि यणादेशो "
            "दीर्घविधानसामर्थ्याद् न प्रवर्तते** — the यण् would "
            "ordinarily go first, being inner; if it did, there "
            "would be no vowel left to lengthen and this rule "
            "would be idle, so it does not"),
    Dirgha(
        "6.3.139", does="dīrgha", gana="samprasāraṇa-anta",
        blocks=("6.3.61",),
        why="संप्रसारणस्य — a first member ending in a "
            "संप्रसारण lengthens before a second: "
            "**कारीषगन्धीपुत्रः, कारीषगन्धीपतिः, "
            "कौमुदगन्धीपुत्रः, कौमुदगन्धीपतिः** — **उत्तरपद इति "
            "वर्तते**, the heading opened at 6.3.1 still running "
            "at the pāda's last sūtra.\\n\\n"
            "**AND THE PĀDA CLOSES BY SETTLING A CONFLICT WITH "
            "ITS OWN EARLIER SELF.** 6.3.61 इको ह्रस्वोऽङ्यो "
            "गालवस्य would have SHORTENED the same vowel. The "
            "vṛtti answers twice: **व्यवस्थितविभाषा हि सा** — "
            "that option does not fall here at all; and then, for "
            "the reading on which it might, **अकृत एव दीर्घत्वे "
            "ह्रस्वाभावपक्षे कृतार्थनापि दीर्घेण पक्षान्तरे "
            "परत्वाद् ह्रस्वो बाध्यते। पुनःप्रसङ्गविज्ञानं च न "
            "भवति। सकृद् गतौ विप्रतिषेधे यद् बाधितं तद् बाधितम् "
            "एव** — a rule set aside once in a conflict does not "
            "come back for a second attempt"),
)


def _reaches(row: Dirgha, purvapada: str, gana: str, before: str,
             result: str, chandasi: bool) -> bool:
    if row.heading:
        return False
    if row.pairs and (gana, before) not in row.pairs:
        return False
    named = row.of or row.gana
    if named and not (purvapada in row.of
                      or (row.gana and gana == row.gana)):
        return False
    if row.before and before not in row.before:
        return False
    if row.result and result not in row.result:
        return False
    if row.chandasi and not chandasi:
        return False
    if row.excludes and (purvapada in row.excludes
                         or before in row.excludes
                         or gana in row.excludes
                         or result in row.excludes):
        return False
    return True


def _how_specific(row: Dirgha, purvapada: str, gana: str,
                  before: str) -> int:
    """
    Naming the stem beats naming a class, and naming the following
    word beats both.

    6.3.119 and 6.3.120 are the pair that needs it: both act
    before मतुप् in a name, and 6.3.120 names its stems where
    6.3.119 has only *many vowels*. And 6.3.125 and 6.3.126 both
    name अष्टन्, told apart by the register.
    """
    return (
        6 * bool(row.pairs)
        + 5 * bool(row.of and purvapada in row.of)
        + 4 * bool(row.before and before in row.before)
        + 3 * bool(row.gana and gana == row.gana)
        + 3 * bool(row.result)
        + 2 * bool(row.chandasi)
    )


@dataclass(frozen=True)
class Lengthened:
    """What the run answers: a lengthening, and by which rule."""

    does: str
    sutra: str
    why: str
    optional: bool = False
    bahulam: bool = False
    blocked_by: Tuple[str, ...] = ()


def lengthens(purvapada: str = "", *, gana: str = "",
              before: str = "", result: str = "",
              chandasi: bool = False) -> Lengthened:
    """
    6.3.114–139 — whether the first member's vowel goes long.

    Nothing answers by default: where no rule is reached the vowel
    keeps the length it had. And nothing here answers at all
    outside connected speech, which is what 6.3.114 says.
    """
    matched = [
        row for row in DIRGHA_TABLE
        if _reaches(row, purvapada, gana, before, result, chandasi)
    ]
    if not matched:
        return Lengthened(
            "", "", "No rule of 6.3.114–139 is reached, so the "
                    "first member keeps the length it had")
    row = max(matched, key=lambda one: _how_specific(
        one, purvapada, gana, before))
    return Lengthened(row.does, row.sutra, row.why,
                      optional=row.optional, bahulam=row.bahulam,
                      blocked_by=row.blocks)


def provisions_for(sutra_id: str) -> Tuple[Dirgha, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in DIRGHA_TABLE
                 if row.sutra == sutra_id)


__all__ = [
    "Dirgha", "DIRGHA_TABLE", "SAMHITA_RUN", "KARNA_EXCEPT",
    "KVIP_ROOTS", "KOTARADI", "KIMSULAKADI", "SARADI",
    "MANTRA_FOUR", "RCI_EIGHT", "SVAN_VARTIKA", "Lengthened",
    "lengthens", "provisions_for",
]
