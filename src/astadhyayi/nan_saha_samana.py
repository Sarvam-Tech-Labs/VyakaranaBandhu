# -*- coding: utf-8 -*-
"""
६.३.७३–९५ — नञ्, सह, समान, and the words that go before अञ्चति.

Three particles lose most of themselves inside a compound, and the
pāda spends twenty-three sūtras saying exactly how much.

**नञ् loses its न्.** 6.3.73 नलोपो नञः — अब्राह्मणः, not
*नब्राह्मणः. Then 6.3.74 puts a नुट् back before a vowel —
अनश्वः — and 6.3.75 names eleven words in which the न् never went
at all: नभ्राट्, नपात्, नासत्या, नमुचि, नकुल, नख, नपुंसक,
नक्षत्र, नक्र, नाक.

**सह becomes स.** 6.3.78 in a name — साश्वत्थम्; then before a
book's end and before an excess, in the second of two, in an
अव्ययीभाव, and optionally wherever it is subordinate. And 6.3.83
holds it back in a blessing: **स्वस्ति देवदत्ताय सहपुत्राय**.

**समान becomes स too.** 6.3.84 in the Veda, and then before
twelve named words, before ब्रह्मचारिन्, before तीर्थ, and
optionally before उदर — सज्योतिः, सनाभिः, सब्रह्मचारी,
सतीर्थ्यः, सोदर्यः.

**AND THEN THE SAME स MEETS दृश् AND अञ्चति.** 6.3.89 सदृक्,
सदृशः; 6.3.90 ईदृक् and कीदृक् for इदम् and किम्, matched one to
one; 6.3.91 तादृक् and यादृक् for any pronoun. And before an
अञ्चति with व on it, the first member's last vowel becomes अद्रि
— विष्वद्र्यङ्, देवद्र्यङ्, तद्र्यङ् — while सम् becomes समि,
तिरस् becomes तिरि, and सह becomes सध्रि.

**WHAT THIS MODULE DOES NOT DO.** It reports the shape and the
rule. It does not carry the derivation on: that विष्वद्र्यङ् then
gets its accent from 8.2.4 after the यण्, and that सोदर्यः needs
4.4.108's यत्, are other rules' business.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: Where these twenty-three stand, closing on 6.3.95 सहस्य सध्रिः.
NAN_RUN: Tuple[str, str] = ("6.3.73", "6.3.95")

#: 6.3.75's eleven, in which नञ् keeps its न् — every one of them
#: a word the grammar can build and none of them a नञ् compound in
#: use any longer.
NA_PRAKRTYA: Tuple[str, ...] = (
    "nabhrāj", "napāt", "navedas", "nāsatya", "namuci", "nakula",
    "nakha", "napuṃsaka", "nakṣatra", "nakra", "nāka")

#: 6.3.85's twelve, before which समान becomes स.
SAMANA_TWELVE: Tuple[str, ...] = (
    "jyotis", "janapada", "rātri", "nābhi", "nāman", "gotra",
    "rūpa", "sthāna", "varṇa", "vayas", "vacana", "bandhu")

#: What 6.3.83 keeps out of its own हold-back, so that सगवे and
#: सवत्साय stand beside सहगवे and सहवत्साय.
ASIS_EXCEPT: Tuple[str, ...] = ("go", "vatsa", "hala")

#: The three before which the substitutions of 6.3.89–91 apply.
DRS_THREE: Tuple[str, ...] = ("dṛś", "dṛśa", "vatu")

#: And a vārttika adds a fourth to each of them, one at a time:
#: **दृक्षे चेति वक्तव्यम्**.
DRKSA_VARTIKA: Tuple[str, ...] = ("dṛkṣa",)

#: What 6.3.84 shuts out of the Vedic स: **अमूर्धप्रभृत्युदर्केषु**.
SAMANA_EXCEPT: Tuple[str, ...] = ("mūrdhan", "prabhṛti", "udarka")


@dataclass(frozen=True)
class Shape:
    """One rule of 6.3.73–95: what the first member comes out as."""

    sutra: str
    #: The substitute, or `prakṛtyā` where the rule's whole content
    #: is that nothing happens.
    becomes: str = ""
    #: The first members the rule names outright.
    of: Tuple[str, ...] = ()
    #: Where stem and substitute are matched one to one.
    pairs: Tuple[Tuple[str, str], ...] = ()
    #: A named class of first member instead — सर्वनामन्.
    gana: str = ""
    #: What must FOLLOW.
    before: Tuple[str, ...] = ()
    samasa: str = ""
    #: The further condition — a sense, a register, a shape.
    result: Tuple[str, ...] = ()
    excludes: Tuple[str, ...] = ()
    optional: bool = False
    chandasi: bool = False
    nipatana: bool = False
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


NAN_TABLE: Tuple[Shape, ...] = (
    Shape(
        "6.3.73", becomes="na-lopa", of=("nañ",),
        why="नलोपो नञः — the न् of नञ् is dropped before a second "
            "member: **अब्राह्मणः, अवृषलः, असुरापः, असोमपः**. The "
            "particle is नञ् and what survives of it is a.\\n\\n"
            "**AND A VĀRTTIKA CARRIES IT OUTSIDE COMPOUNDS "
            "ALTOGETHER.** **नञो नलोपोऽवक्षेपे तिङ्युपसंख्यानम् — "
            "अपचसि त्वं जाल्म, अकरोषि त्वं जाल्म** — before a "
            "FINITE VERB, where scorn is meant. There is no "
            "compound there at all, so the sūtra as written cannot "
            "reach it"),
    Shape(
        "6.3.74", becomes="nuṭ", of=("nañ",), before=("ac",),
        why="तस्मान्नुडचि — and after that न्-less नञ्, a नुट् is "
            "put in before a vowel: **अनजः, अनश्वः**. So the a "
            "that 6.3.73 left comes back out as an-.\\n\\n"
            "**AND तस्मात् IS THERE TO SAY AFTER WHICH नञ्.** "
            "**तस्मादिति किम्? नञ एव हि स्यात्। पूर्वान्ते हि ङमो "
            "ह्रस्वादचि ङमुण्नित्यम् इति प्राप्नोति** — without "
            "it the augment would attach to नञ् entire, and 8.3.32 "
            "would then double the ङम् at the end of the first "
            "part. Saying *after that* fixes it to the residue"),
    Shape(
        "6.3.75", becomes="prakṛtyā", of=("nañ",),
        before=NA_PRAKRTYA,
        why="नभ्राण्नपान्नवेदानासत्यानमुचिनकुलनखनपुंसकनक्षत्रनक्रनाकेषु "
            "प्रकृत्या — but in eleven words नञ् stands as it is, "
            "न् and all: **न भ्राजत इति नभ्राट्; न पातीति नपात्; "
            "न वेत्तीति नवेदाः; न सत्या असत्याः, न असत्या "
            "नासत्याः; न मुञ्चतीति नमुचिः; नास्य कुलमस्ति नकुलः; "
            "नास्य खमस्तीति नखम्**.\\n\\n"
            "**AND EVERY ONE OF THEM IS ANALYSED BEFORE IT IS "
            "LISTED.** The vṛtti does not name the words and stop: "
            "it says which affix built each — **भ्राजतेः "
            "क्विबन्तस्य नञ्समासः; पातिः शत्रन्तः; वेत्तिर् "
            "असुन्प्रत्ययान्तः; मुचेर् औणादिकः किप्रत्ययः** — "
            "which is what makes them derivations that keep their "
            "न् rather than opaque words"),
    Shape(
        "6.3.76", becomes="prakṛtyā", of=("nañ",),
        before=("eka",),
        why="एकादिश्च एकस्य चादुक् — and नञ् stands as it is where "
            "एक begins the compound, and एक itself takes the "
            "augment आदुक्: **एकेन न विंशतिर् एकान्नविंशतिः; "
            "एकान्नत्रिंशत्** — twenty less one, thirty less one. "
            "The compound is **तृतीयेति योगविभागात्**.\\n\\n"
            "**AND THE AUGMENT IS PUT AT THE END OF THE FIRST PART "
            "AND NOT THE START OF THE SECOND.** **पूर्वान्तोऽयम् "
            "आदुक् क्रियते, पदान्तलक्षणोऽत्रानुनासिको विकल्पेन यथा "
            "स्यादिति** — so that the nasal standing at a word's "
            "end may be optional, which it could not be if the "
            "augment belonged to what follows"),
    Shape(
        "6.3.77", becomes="prakṛtyā", of=("nañ",),
        before=("ga",), result=("aprāṇin",), optional=True,
        keeps_out="अगो वृषलः शीतेन — a man, and so alive",
        why="नगोऽप्राणिष्वन्यतरस्याम् — and in नग, of things NOT "
            "ALIVE, नञ् stands as it is optionally: **नगा वृक्षाः "
            "/ अगा वृक्षाः; नगाः पर्वताः / अगाः पर्वताः** — trees "
            "and mountains, which do not go. **न गच्छन्तीति नगाः**, "
            "with 4.1.114's ड"),
    Shape(
        "6.3.78", becomes="sa", of=("saha",), result=("saṃjñā",),
        keeps_out="सहयुध्वा, सहकृत्वा — not a name",
        why="सहस्य सः संज्ञायाम् — सह becomes स where the compound "
            "is a NAME: **साश्वत्थम्, सपलाशम्, सशिंशपम्** — "
            "places named for the tree that stands there.\\n\\n"
            "**AND THE SUBSTITUTE IS LAID DOWN WITH AN ACCENT.** "
            "**सादेश उदात्तो निपात्यते। उदात्तानुदात्तवतो हि "
            "सहशब्दस्य आन्तर्यतः स्वरितः स्यात्** — सह has an "
            "उदात्त and an अनुदात्त, so the nearest single accent "
            "for a one-syllable substitute would have been a "
            "स्वरित; the निपातन makes it उदात्त instead. And it "
            "matters only sometimes: **स च निपातनस्वरः "
            "पूर्वपदप्रकृतिस्वरत्वं यत्र, तत्र उपयुज्यते। अन्यत्र "
            "समासान्तोदात्तत्वेन बाध्यत एव — सेष्टि, "
            "सपशुबन्धम्**"),
    Shape(
        "6.3.79", becomes="sa", of=("saha",),
        result=("granthānta", "adhika"),
        why="ग्रन्थान्ताधिके च — and where सह names the END OF A "
            "BOOK or an EXCESS: **सकलं ज्यौतिषम् अधीते; "
            "समुहूर्तम्; ससंग्रहं व्याकरणम् अधीयते** for the "
            "first, and **सद्रोणा खारी; समाषः कार्षापणः** for the "
            "second — a khārī with a droṇa over.\\n\\n"
            "**AND IT IS STATED BECAUSE THE NEXT RULE WOULD NOT "
            "HAVE REACHED THESE.** **कलान्तं मुहूर्तान्तं "
            "संग्रहान्तम् इति अन्तवचने इत्यव्ययीभावः समासः। तत्र "
            "अव्ययीभावे चाकाले इति कालवाचिनि उत्तरपदे सभावो न "
            "प्राप्नोतीत्ययमारम्भः** — these are अव्ययीभावs with a "
            "time-word after them, and 6.3.81 excepts exactly that"),
    Shape(
        "6.3.80", becomes="sa", of=("saha",),
        result=("dvitīya-anupākhya",),
        why="द्वितीये चानुपाख्ये — and where सह names the SECOND "
            "of two, the one that cannot be seen: **साग्निः "
            "कपोतः; सपिशाचा वात्या; सराक्षसीका शाला** — a dove "
            "with fire in it, a whirlwind with a demon in it.\\n\\n"
            "**AND BOTH WORDS ARE GLOSSED BEFORE USE.** **द्वयोः "
            "सहयुक्तयोर् अप्रधानो यः, स द्वितीयः** — of two things "
            "together, the one that is not the point; **उपाख्यायते "
            "प्रत्यक्षत उपलभ्यते यः, स उपाख्यः, उपाख्याद् अन्योऽ"
            "नुपाख्योऽनुमेयः** — and not seen but inferred. "
            "**अग्न्यादयः साक्षाद् अनुपलभ्यमानाः कपोतादिभिर् "
            "अनुमीयमाना अनुपाख्या भवन्ति**"),
    Shape(
        "6.3.81", becomes="sa", of=("saha",), samasa="avyayībhāva",
        excludes=("kāla",),
        keeps_out="सहपूर्वाह्णम् — a time-word, which the sūtra "
                  "shuts out",
        why="अव्ययीभावे चाकाले — and in an अव्ययीभाव, where the "
            "second member does NOT name a time: **सचक्रं धेहि; "
            "सधुरं प्राज** — set it down with the wheel, drive it "
            "with the yoke-pole"),
    Shape(
        "6.3.82", becomes="sa", of=("saha",),
        result=("upasarjana",), optional=True,
        keeps_out="सहयुध्वा, सहकृत्वा — सह is the principal word "
                  "there; प्रियसहकृत्वा — the सह is not the one "
                  "the बहुव्रीहि's second member follows",
        why="वोपसर्जनस्य — and optionally wherever सह is "
            "SUBORDINATE: **सपुत्रः / सहपुत्रः; सच्छात्रः / "
            "सहच्छात्रः**.\\n\\n"
            "**AND उपसर्जन HERE MEANS THE WHOLE COMPOUND AND NOT "
            "A MEMBER.** **उपसर्जनसर्वावयवः समास उपसर्जनम्। यस्य "
            "सर्वेऽवयवा उपसर्जनीभूताः स सर्वोपसर्जनो बहुव्रीहिर् "
            "गृह्यते** — a बहुव्रीहि, in which every member is "
            "subordinate to something outside the compound"),
    Shape(
        "6.3.83", becomes="prakṛtyā", of=("saha",),
        result=("āśis",), excludes=ASIS_EXCEPT,
        why="प्रकृत्याशिष्यगोवत्सहलेषु — but in a BLESSING सह "
            "stands as it is, except before गो, वत्स and हल: "
            "**स्वस्ति देवदत्ताय सहपुत्राय सहच्छात्राय "
            "सहामात्याय**.\\n\\n"
            "**AND THE THREE EXCEPTED WORDS STILL HAVE THE OPTION "
            "OF THE RULE BEFORE.** **अगोवत्सहलेष्विति किम्? "
            "स्वस्ति भवते सहगवे, सगवे। सहवत्साय, सवत्साय। "
            "सहहलाय, सहलाय। वोपसर्जनस्य इति पक्षे भवत्येव सभावः** "
            "— being excepted from a hold-back does not make the "
            "substitution compulsory; it only lets 6.3.82's "
            "option through"),
    Shape(
        "6.3.84", becomes="sa", of=("samāna",), chandasi=True,
        excludes=SAMANA_EXCEPT,
        keeps_out="समानमूर्धा, समानप्रभृतयः, समानोदर्काः — the "
                  "three the sūtra names out",
        why="समानस्य छन्दस्यमूर्धप्रभृत्युदर्केषु — समान becomes "
            "स in the Veda, except before मूर्धन्, प्रभृति and "
            "उदर्क: **अनु भ्राता सगर्भ्यः; अनु सखा सयूथ्यः; यो नः "
            "सनुत्यः** — born of the same womb, of the same herd. "
            "**समानो गर्भः सगर्भः, तत्र भवः सगर्भ्यः**, with "
            "4.4.114's यन्. And the vṛtti records a reading that "
            "splits the sūtra: **समानस्येति योगविभाग इष्यते**"),
    Shape(
        "6.3.85", becomes="sa", of=("samāna",),
        before=SAMANA_TWELVE,
        why="ज्योतिर्जनपदरात्रिनाभिनामगोत्ररूपस्थानवर्णवयोवचनबन्धुषु "
            "— and outside the Veda before twelve named words: "
            "**सज्योतिः, सजनपदः, सरात्रिः, सनाभिः, सनामा, "
            "सगोत्रः, सरूपः, सस्थानः, सवर्णः, सवयाः, सवचनः, "
            "सबन्धुः** — of the same light, the same country, the "
            "same night, the same navel, the same name, the same "
            "lineage. सवर्ण is the term 1.1.9 defines, and this is "
            "where its शब्द comes from"),
    Shape(
        "6.3.86", becomes="sa", of=("samāna",),
        before=("brahmacārin",), result=("caraṇa",),
        why="चरणे ब्रह्मचारिणि — and before ब्रह्मचारिन्, where a "
            "SCHOOL is meant: **समानो ब्रह्मचारी सब्रह्मचारी**. "
            "The vṛtti works the sense out in full: **ब्रह्म "
            "वेदः, तदध्ययनार्थं यद् व्रतं तदपि ब्रह्म, तच्चरतीति "
            "ब्रह्मचारी, समानस् तस्यैव ब्रह्मणः समानत्वाद् "
            "इत्ययमर्थो भवति — समाने ब्रह्मणि व्रतचारी "
            "सब्रह्मचारीति** — not a fellow-student in general but "
            "one keeping the same vow over the same Veda"),
    Shape(
        "6.3.87", becomes="sa", of=("samāna",), before=("tīrtha",),
        result=("yat",),
        why="तीर्थे ये — and before तीर्थ with यत् on it: "
            "**सतीर्थ्यः** — one who studies at the same teacher's. "
            "The यत् is 4.4.107's, **समानतीर्थे वासी**"),
    Shape(
        "6.3.88", becomes="sa", of=("samāna",), before=("udara",),
        result=("yat",), optional=True,
        why="विभाषोदरे — and optionally before उदर with यत् on it: "
            "**सोदर्यः / समानोदर्यः** — born of the same belly. "
            "The यत् is 4.4.108's, **समानोदरे शयित ओ चोदात्तः**, "
            "which supplies the accent too"),
    Shape(
        "6.3.89", becomes="sa", of=("samāna",),
        before=DRS_THREE + DRKSA_VARTIKA,
        why="दृग्दृशवतुषु — and before दृक्, दृश and वतु: "
            "**सदृक्, सदृशः** — of the same look. The affixes are "
            "from a vārttika on 3.2.60: **त्यदादिषु दृशोऽनालोचने "
            "कञ् च इत्यत्र समानान्ययोश्चेति वक्तव्यम् इति कञ्क्विनौ "
            "प्रत्ययौ क्रियेते**, and another adds a fourth "
            "environment — **दृक्षे चेति वक्तव्यम् — सदृक्षः**. "
            "The vṛtti notes why वतु is named at all: "
            "**वतुग्रहणम् उत्तरार्थम्**, for the two sūtras after"),
    Shape(
        "6.3.90", pairs=(("idam", "īś"), ("kim", "kī")),
        of=("idam", "kim"), before=DRS_THREE + DRKSA_VARTIKA,
        why="इदंकिमोरीश्की — इदम् and किम् become ईश् and की in "
            "the same place, matched ONE TO ONE: **ईदृक्, ईदृशः, "
            "इयान्; कीदृक्, कीदृशः, कियान्**. The वतुप् of इयान् "
            "and कियान् is 5.2.40's, **किमिदम्भ्यां वो घः**, and "
            "the vārttika reaches here too — **दृक्षे चेति "
            "वक्तव्यम् — ईदृक्षः, कीदृक्षः**"),
    Shape(
        "6.3.91", becomes="ā", gana="sarvanāman",
        before=DRS_THREE + DRKSA_VARTIKA,
        why="आ सर्वनाम्नः — and any PRONOUN takes आ in the same "
            "place: **तादृक्, तादृशः, तावान्; यादृक्, यादृशः, "
            "यावान्** — of that sort, of which sort. **दृक्षे चेति "
            "वक्तव्यम् — तादृक्षः, यादृक्षः**"),
    Shape(
        "6.3.92", becomes="adri", of=("viṣvak", "deva"),
        gana="sarvanāman", before=("añcati",), result=("va",),
        keeps_out="अश्वाची — not विष्वक् or देव or a pronoun; "
                  "विष्वग्युक् — no अञ्चति; and without the व it "
                  "is not this rule's case either",
        why="विष्वग्देवयोश्च टेरद्र्यञ्चतौ वप्रत्यये — before an "
            "अञ्चति with व on it, the last vowel and what follows "
            "it in विष्वक्, देव and any pronoun becomes अद्रि: "
            "**विष्वगञ्चतीति विष्वद्र्यङ्; देवद्र्यङ्; तद्र्यङ्, "
            "यद्र्यङ्**.\\n\\n"
            "**AND THE SUBSTITUTE IS LAID DOWN END-ACCENTED FOR A "
            "REASON.** **अद्रिसध्र्योर् अन्तोदात्तनिपातनं "
            "कृत्स्वरनिवृत्त्यर्थम्। तत्र यणादेशे कृते "
            "उदात्तस्वरितयोर्यणः स्वरितोऽनुदात्तस्य इत्येष स्वरो "
            "भवति** — to cancel the accent the कृत् would have "
            "given, and so that 8.2.4 can then make the following "
            "vowel svarita once the य् appears"),
    Shape(
        "6.3.93", becomes="sami", of=("sam",), before=("añcati",),
        result=("va",),
        why="समः समि — सम् becomes समि in the same place: "
            "**सम्यङ्, सम्यञ्चौ, सम्यञ्चः** — going together, and "
            "so straight, and so right"),
    Shape(
        "6.3.94", becomes="tiri", of=("tiras",),
        before=("añcati",), result=("va",), excludes=("alopa",),
        keeps_out="तिरश्चा, तिरश्चे — there the अ IS dropped, by "
                  "6.4.138 अचः, so the condition fails",
        why="तिरसस्तिर्यलोपे — तिरस् becomes तिरि in the same "
            "place, where the अ is NOT dropped: **तिर्यङ्, "
            "तिर्यञ्चौ, तिर्यञ्चः**. **अलोप इति किम्? तिरश्चा, "
            "तिरश्चे** — 6.4.138's अचः takes the अ out there, and "
            "this rule's condition is that it has not"),
    Shape(
        "6.3.95", becomes="sadhri", of=("saha",),
        before=("añcati",), result=("va",),
        why="सहस्य सध्रिः — and सह becomes सध्रि: **सध्र्यङ्, "
            "सध्र्यञ्चौ, सध्र्यञ्चः; सध्रीचः, सध्रीचा**. The last "
            "of the pāda's three particles, and the last of its "
            "substitutions for them — सह has now become स by six "
            "rules, stood unchanged by one, and become सध्रि by "
            "this"),
)


def _reaches(row: Shape, purvapada: str, gana: str, before: str,
             samasa: str, result: str, chandasi: bool) -> bool:
    named = row.of or row.gana
    if named and not (purvapada in row.of
                      or (row.gana and gana == row.gana)):
        return False
    if row.before and before not in row.before:
        return False
    if row.samasa and samasa != row.samasa:
        return False
    if row.result and result not in row.result:
        return False
    if row.chandasi and not chandasi:
        return False
    if row.excludes and (before in row.excludes
                         or result in row.excludes):
        return False
    return True


def _becomes(row: Shape, purvapada: str) -> str:
    """The substitute, looked up where the rule matches one to one."""
    for stem, shape in row.pairs:
        if stem == purvapada:
            return shape
    return row.becomes


def _supplies(row: Shape, purvapada: str, wants: str) -> bool:
    return not wants or wants == _becomes(row, purvapada)


def _how_specific(row: Shape, purvapada: str, gana: str,
                  before: str) -> int:
    """
    Naming the stem beats naming a class it falls in, and naming
    the following word beats both.

    6.3.90 and 6.3.91 are the case that needs it: इदम् and किम्
    are pronouns, so 6.3.91's सर्वनाम्नः reaches them, and only
    their being named outright puts 6.3.90 first.
    """
    return (
        6 * bool(row.pairs and _becomes(row, purvapada))
        + 5 * bool(row.of and purvapada in row.of)
        + 4 * bool(row.before and before in row.before)
        + 3 * bool(row.result)
        + 2 * bool(row.gana and gana == row.gana)
        + 2 * bool(row.samasa)
        + 2 * bool(row.chandasi)
    )


@dataclass(frozen=True)
class Shaped:
    """What the run answers: a shape, and by which rule."""

    becomes: str
    sutra: str
    why: str
    optional: bool = False
    blocked_by: Tuple[str, ...] = ()


def shaped(purvapada: str = "", *, gana: str = "",
           before: str = "", samasa: str = "", result: str = "",
           chandasi: bool = False, wants: str = "") -> Shaped:
    """
    6.3.73–95 — what नञ्, सह, समान and their fellows come out as.

    Nothing answers by default: where no rule is reached the first
    member stands as it was, unaltered and unsubstituted.
    """
    matched = [
        row for row in NAN_TABLE
        if _reaches(row, purvapada, gana, before, samasa, result,
                    chandasi)
        and _supplies(row, purvapada, wants)
    ]
    if not matched:
        return Shaped(
            "", "", "No rule of 6.3.73–95 is reached, so the first "
                    "member stands as it was")
    row = max(matched, key=lambda one: _how_specific(
        one, purvapada, gana, before))
    return Shaped(_becomes(row, purvapada), row.sutra, row.why,
                  optional=row.optional, blocked_by=row.blocks)


def provisions_for(sutra_id: str) -> Tuple[Shape, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in NAN_TABLE if row.sutra == sutra_id)


__all__ = [
    "Shape", "NAN_TABLE", "NAN_RUN", "NA_PRAKRTYA",
    "SAMANA_TWELVE", "SAMANA_EXCEPT", "ASIS_EXCEPT", "DRS_THREE",
    "DRKSA_VARTIKA", "Shaped", "shaped", "provisions_for",
]
