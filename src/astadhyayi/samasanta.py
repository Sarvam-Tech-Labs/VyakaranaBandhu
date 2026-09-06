# -*- coding: utf-8 -*-
"""
५.४.१–३० — the स्वार्थिक affixes go on, and one of them is proved
to exist by a rule that forbids it.

अध्याय ५ पाद ३ opened by saying that from there the affixes add
nothing to the base's meaning. This pāda continues that, and then at
5.4.68 turns to the समासान्त affixes — the endings a compound takes
because it is a compound — which is what the module is named for.

**AND A PROHIBITION IS READ AS EVIDENCE.** 5.4.5 forbids कन् after a
past participle when a word for *half* stands by. The vṛtti objects
that the prohibition is idle, the base already saying it —
**सामिवचने प्रतिषेधानर्थक्यम्, प्रकृत्याभिहितत्वात्** — and answers:
**एवं तर्हि नैवायम् अनत्यन्तगतौ विहितस्य कनः प्रतिषेधः; किं तर्हि?
स्वार्थिकस्य। केन पुनः स्वार्थिकः कन् विहितः? एतदेव ज्ञापकम् —
भवति स्वार्थे कन्निति.** No rule anywhere gives a कन् in the base's
own sense; that this rule forbids one is the only evidence that it
exists. And with that the Mahābhāṣya's own **अभिन्नतरकम्** and
**बहुतरकम्** are accounted for.

**AND THE स्वार्थिक AFFIXES OVERRIDE THE BASE'S GENDER AND NUMBER.**
5.4.14 states the word *feminine* where it need not, and the vṛtti
reads that too: **एतज् ज्ञापयति — स्वार्थिकाः प्रत्ययाः प्रकृतितो
लिङ्गवचनान्यतिवर्तन्तेऽपि इति.** Which is why गुडकल्पा द्राक्षा and
देव एव देवता are possible at all.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: The स्वार्थिक affixes that are OBLIGATORY, listed at 5.4.7 —
#: everywhere else in this section the great option makes them a
#: choice. **नित्यश्चायं प्रत्ययः, उत्तरत्र विभाषाग्रहणात्;
#: अन्येऽपि स्वार्थिका नित्याः प्रत्ययाः स्मर्यन्ते.**
ALWAYS_APPLY: Tuple[str, ...] = (
    "5.3.55–5.3.63",   # तमबादयः प्राक् कनः
    "5.3.112–5.3.118",  # ञ्यादयः प्राग् वुनः
    "5.4.11–5.4.20",   # आमादयः प्राङ् मयटः
    "5.4.6",           # बृहतीजात्यन्ताः
    "5.4.9",
    "समासान्ताः",
)


@dataclass(frozen=True)
class Samasanta:
    """One rule of 5.4: a base, and an affix adding no meaning."""

    sutra: str
    gives: str = ""
    also_gives: Tuple[str, ...] = ()
    of: Tuple[str, ...] = ()
    gana: str = ""
    #: A class the base belongs to — क्तान्त at 5.4.4, अञ्चन्त at
    #: 5.4.8, देवतान्त at 5.4.24.
    of_samjna: str = ""
    #: The case the base stands in — चतुर्थी for the *for that*
    #: sense at 5.4.24, प्रथमा at 5.4.21.
    case: str = ""
    #: What the derived word must mean or be used of — वीप्सा at
    #: 5.4.1, आच्छादन at 5.4.6, बन्धु at 5.4.9, मत्स्य at 5.4.16.
    result: str = ""
    #: What stands BY the base as an उपपद — 5.4.5's सामिवचन.
    upapada: str = ""
    #: An आदेश or लोप the rule brings with the affix.
    adesa: str = ""
    #: What the rule keeps OUT by name — 5.4.45's हा and रुह्.
    excludes: Tuple[str, ...] = ()
    #: The affix the rule's substitution stands BEFORE — 5.4.88's
    #: टच्.
    before: str = ""
    usage: str = ""
    optional: bool = False
    #: True where the rule REFUSES rather than supplies. 5.4.5 is
    #: the only one of the opening, and the refusal is what proves
    #: the affix exists.
    refuses: bool = False
    #: True where the whole form is laid down.
    nipatana: bool = False
    heading: bool = False
    excepts: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


SAMASANTA_TABLE: Tuple[Samasanta, ...] = (
    Samasanta("5.4.1", gives="vun", adesa="antalopa",
              of_samjna="pādaśatānta-saṃkhyādi", result="vīpsā",
              why="पादशतस्य संख्यादेर्वीप्सायां वुन् लोपश्च — the "
                  "affix and the loss of the base's ending "
                  "together. द्वौद्वौ पादौ ददाति **द्विपदिकां "
                  "ददाति**; द्वेद्वे शते ददाति **द्विशतिकां "
                  "ददाति**.\\n\\n"
                  "**AND THE LOSS IS STATED THOUGH ANOTHER RULE "
                  "GIVES IT.** **यस्येति लोपेनैव सिद्धे पुनर्वचनम् "
                  "अनैमित्तिकार्थम्** (6.4.148) — 6.4.148's "
                  "elision is caused by what FOLLOWS, so 1.1.56 "
                  "would treat the lost sound as still there and "
                  "6.4.130 पादः पत् would not apply. **अस्य तु "
                  "अनैमित्तिकत्वाद् न स्थानिवत्त्वम्**: an elision "
                  "with no cause is not treated that way. A rule "
                  "restated to escape a substitution-principle.\\n\\n"
                  "**पादशतस्येति किम्?** द्वौद्वौ माषौ ददाति. "
                  "**संख्यादेरिति किम्?** पादंपादं ददाति. "
                  "**वीप्सायामिति किम्?** द्वौ पादौ ददाति. And "
                  "**पादशतग्रहणमनर्थकम्, अन्यत्रापि दर्शनात्** — "
                  "द्विमोदकिकां ददाति",
              keeps_out="द्वौद्वौ माषौ ददाति, पादंपादं ददाति"),
    Samasanta("5.4.2", gives="vun", adesa="antalopa",
              of_samjna="pādaśatānta-saṃkhyādi",
              result="daṇḍa-vyavasarga", excepts=("5.4.1",),
              why="दण्डव्यवसर्गयोश्च — **दमनं दण्डः; दानं "
                  "व्यवसर्गः**, and **अवीप्सार्थोऽयमारम्भः**, the "
                  "rule begun so that the repetition is not "
                  "needed. द्वौ पादौ दण्डितो **द्विपदिकां "
                  "दण्डितः**; द्विशतिकां व्यवसृजति"),
    Samasanta("5.4.3", gives="kan", gana="sthūlādi",
              result="prakāra", excepts=("5.3.69",),
              why="स्थूलादिभ्यः प्रकारवचने कन्, **जातीयरोऽपवादः**. "
                  "**प्रकारो विशेषः**. स्थूलप्रकारः **स्थूलकः**; "
                  "अणुकः, माषकः.\\n\\n"
                  "**कन्प्रकरणे चञ्चद्बृहतोरुपसंख्यानम्** — "
                  "चञ्चत्कः, बृहत्कः, and **चञ्चबृहयोरिति केचित् "
                  "पठन्ति; तेषां चञ्चकः, बृहकः**. स्थूल, अणु, "
                  "माष, इषु, **कृष्ण तिलेषु**, **यव व्रीहिषु**, "
                  "**गोमूत्र आच्छादने**, **सुरा अहौ**, "
                  "**जीर्ण शालिषु**, **पत्रमूले समस्तव्यस्ते**, "
                  "कुमारीपुत्र, कुमार, श्वशुर, मणि — स्थूलादिः, "
                  "and half its entries carry a sense of their own"),
    Samasanta("5.4.4", gives="kan", of_samjna="ktānta",
              result="anatyantagati",
              why="अनत्यन्तगतौ क्तात् — **अत्यन्तगतिरशेषसंबन्धः, "
                  "तदभावोऽनत्यन्तगतिः**, a thing gone through NOT "
                  "wholly. **भिन्नकः, छिन्नकः**, partly broken. "
                  "**अनत्यन्तगताविति किम्?** भिन्नम्, छिन्नम्",
              keeps_out="भिन्नम्, छिन्नम्"),
    Samasanta("5.4.5", refuses=True, of_samjna="ktānta",
              result="anatyantagati", upapada="sāmivacana",
              excepts=("5.4.4",),
              why="न सामिवचने — a प्रतिषेध, and the vṛtti finds "
                  "the whole of a missing rule inside it.\\n\\n"
                  "**सामिकृतम्, सामिभुक्तम्**; and "
                  "**वचनग्रहणं पर्यायार्थम्** brings the synonyms "
                  "in — अर्धकृतम्, नेमकृतम्.\\n\\n"
                  "**BUT THE PROHIBITION IS IDLE AS IT STANDS.** "
                  "**सामिवचने प्रतिषेधानर्थक्यम्, "
                  "प्रकृत्याभिहितत्वात्** — the base already says "
                  "*half*, and 5.4.4's affix is for something NOT "
                  "wholly done, so there was nothing to forbid. "
                  "**एवं तर्हि नैवायम् अनत्यन्तगतौ विहितस्य कनः "
                  "प्रतिषेधः; किं तर्हि? स्वार्थिकस्य। केन पुनः "
                  "स्वार्थिकः कन् विहितः? एतदेव ज्ञापकम् — भवति "
                  "स्वार्थे कन्निति**: it forbids a कन् given in "
                  "the base's OWN sense, and no rule gives one — so "
                  "this prohibition is the only evidence that such "
                  "an affix exists at all.\\n\\n"
                  "**तत्र यदेतदुच्यते — एवं हि सूत्रम् "
                  "अभिन्नतरकं भवति, एतैर्हि बहुतरकं व्याप्यते "
                  "इत्येवमादि, तदुपपन्नं भवति** — and the "
                  "Mahābhāṣya's own अभिन्नतरक and बहुतरक, which no "
                  "rule accounted for, are accounted for by it"),
    Samasanta("5.4.6", gives="kan", of=("bṛhatī",),
              result="ācchādana",
              why="बृहत्या आच्छादने — **कन्ननुवर्तते, न प्रतिषेधः**, "
                  "the affix carries down and the prohibition does "
                  "not. **बृहतिका**, a cloak. "
                  "**आच्छादन इति किम्?** बृहती छन्दः",
              keeps_out="बृहती छन्दः"),
    Samasanta("5.4.7", gives="kha",
              of=("aṣaḍakṣa", "āśitaṅgu", "alaṃkarman",
                  "alaṃpuruṣa"),
              why="अषडक्षाशितङ्ग्वलंकर्मालंपुरुषाध्युत्तरपदात् खः. "
                  "**अविद्यमानानि षडक्षीण्यस्येति बहुव्रीहिः** — "
                  "**अषडक्षीणो मन्त्रः**, **यो द्वाभ्यामेव क्रियते "
                  "न बहुभिः**, counsel taken by two and not by six "
                  "eyes. आशिता गावोऽस्मिन् **आशितंगवीनम् "
                  "अरण्यम्**, a wood where the cattle have fed "
                  "their fill; **अलंकर्मीणः, अलंपुरुषीणः**.\\n\\n"
                  "**AND THIS AFFIX IS OBLIGATORY, WHICH IS READ "
                  "FROM THE NEXT RULE.** **नित्यश्चायं प्रत्ययः, "
                  "उत्तरत्र विभाषाग्रहणात्** — 5.4.8 says "
                  "*optionally*, so this one is not. And the vṛtti "
                  "then lists every स्वार्थिक affix that is "
                  "obligatory: **तमबादयः प्राक् कनः, ञ्यादयः "
                  "प्राग् वुनः, आमादयः प्राङ् मयटः, "
                  "बृहतीजात्यन्ताः समासान्ताश्चेति** — five "
                  "stretches, named by their limits"),
    Samasanta("5.4.7", gives="kha", of_samjna="adhyuttarapada",
              why="अषडक्षाशितङ्ग्वलंकर्मालंपुरुषाध्युत्तरपदात् खः, "
                  "the अध्युत्तरपद half — a तत्पुरुष whose second "
                  "member is अधि, **अधिशब्दः शौण्डादिषु पठ्यते**. "
                  "**राजाधीनः**, subject to a king"),
    Samasanta("5.4.8", gives="kha", of_samjna="añcanta",
              optional=True, result="adiksṛī",
              why="विभाषा अञ्चेरदिक्स्त्रियाम् — optionally, and "
                  "NOT of a quarter in the feminine. "
                  "**प्राक्, प्राचीनम्**; अर्वाक्, अर्वाचीनम्.\\n\\n"
                  "**अदिक्स्त्रियामिति किम्?** प्राची दिक्. "
                  "**दिग्ग्रहणं किम्?** प्राचीना ब्राह्मणी. "
                  "**स्त्रीग्रहणं किम्?** प्राचीनं दिग् रमणीयम् — "
                  "three counter-examples for one compound word, "
                  "each showing which half of it is doing the work",
              keeps_out="प्राची दिक्"),
    Samasanta("5.4.9", gives="cha", of_samjna="jātyanta",
              result="bandhu",
              why="जात्यन्ताच्छ बन्धुनि. **बध्यतेऽस्मिन् जातिरिति "
                  "बन्धुशब्देन द्रव्यमुच्यते; येन ब्राह्मणत्वादि"
                  "जातिर्व्यज्यते तद् बन्धु द्रव्यम्** — the "
                  "SUBSTANCE in which a kind is bound up, that by "
                  "which brahmin-hood shows. **ब्राह्मणजातीयः, "
                  "क्षत्रियजातीयः**. **बन्धुनीति किम्?** "
                  "ब्राह्मणजातिः शोभना",
              keeps_out="ब्राह्मणजातिः शोभना"),
    Samasanta("5.4.10", gives="cha", of_samjna="sthānānta",
              optional=True, result="sasthāna",
              why="स्थानान्ताद् विभाषा सस्थानेनेति चेत् — "
                  "**सस्थान इति तुल्य उच्यते, समानं स्थानमस्येति "
                  "कृत्वा**. पित्रा तुल्यः **पितृस्थानीयः, "
                  "पितृस्थानः**; राजस्थानीयः. "
                  "**सस्थानेनेति किम्?** गोस्थानम्.\\n\\n"
                  "**इतिकरणो विवक्षार्थः; तेन बहुव्रीहिः "
                  "सस्थानशब्दार्थम् उपस्थापयति, न तत्पुरुषः** — "
                  "the इति makes सस्थान a बहुव्रीहि and not a "
                  "तत्पुरुष. And **द्वयोर्विभाषयोर्मध्ये नित्या "
                  "विधय इति पूर्वत्र नित्यः प्रत्ययः**: a rule "
                  "standing BETWEEN two optional ones is itself "
                  "obligatory, which is how 5.4.9 was settled",
              keeps_out="गोस्थानम्"),
    Samasanta("5.4.11", gives="āmu", of_samjna="kim-et-tiṅ-avyaya-gha",
              result="adravyaprakarṣa",
              why="किमेत्तिङव्ययघाद् आमु अद्रव्यप्रकर्षे — after "
                  "the घ (तर and तम) that किम्, an ए-final, a "
                  "finite verb or an indeclinable took, where the "
                  "excess is NOT of a substance. "
                  "**किंतराम्, पूर्वाह्णेतराम्, पचतितराम्, "
                  "उच्चैस्तराम्**.\\n\\n"
                  "**यद्यपि द्रव्यस्य स्वतः प्रकर्षो नास्ति, तथापि "
                  "क्रियागुणस्थः प्रकर्षो यदा द्रव्य उपचर्यते तदा "
                  "अयं प्रतिषेधः; क्रियागुणयोरेवायं प्रकर्षे "
                  "प्रत्ययः** — a substance has no degrees of its "
                  "own, but a degree belonging to an act or a "
                  "quality may be transferred to one, and THAT is "
                  "what the rule excludes. **अद्रव्यप्रकर्ष इति "
                  "किम्?** उच्चैस्तरः",
              keeps_out="उच्चैस्तरः"),
    Samasanta("5.4.12", gives="amu", also_gives=("āmu",),
              of_samjna="kim-et-tiṅ-avyaya-gha",
              result="adravyaprakarṣa", usage="chandasi",
              why="अमु च छन्दसि — **चकारादामु च**. प्रत॒**रं** न "
                  "आयुः॑; प्रत॒**रां** नय. **स्वरादिषु अम् आम् इति "
                  "पठ्यते; तस्मात् तदन्तस्याव्ययत्वम्** — and both "
                  "are in the स्वरादि list, so a word ending in "
                  "them is an indeclinable"),
    Samasanta("5.4.13", gives="ṭhak", of=("anugādin",),
              why="अनुगादिनष्ठक् — **अनुगदतीत्यनुगादी**, one who "
                  "repeats after. **आनुगादिकः**"),
    Samasanta("5.4.14", gives="añ", of_samjna="ṇacanta",
              result="strī",
              why="णचः स्त्रियामञ् — after the णच् of 3.3.43 "
                  "कर्मव्यतिहारे णच् स्त्रियाम्. **व्यावक्रोशी, "
                  "व्यावहासी वर्तते**, a mutual reviling.\\n\\n"
                  "**AND THE WORD *FEMININE* IS IDLE AND IS READ AS "
                  "A ज्ञापक.** **स्त्रीग्रहणं किमर्थं यावता णच् "
                  "स्त्रियामेव विहितः?** — the णच् is given in the "
                  "feminine already. **एवं तर्ह्येतज् ज्ञापयति — "
                  "स्वार्थिकाः प्रत्ययाः प्रकृतितो "
                  "लिङ्गवचनान्यतिवर्तन्तेऽपि इति**: a स्वार्थिक "
                  "affix may OVERRIDE the base's gender and number. "
                  "**तेन गुडकल्पा द्राक्षा, तैलकल्पा प्रसन्ना, देव "
                  "एव देवता इत्येवमादि उपपन्नं भवति** — and that "
                  "is what makes those forms possible"),
    Samasanta("5.4.15", gives="aṇ", of_samjna="inuṇanta",
              why="अणिनुणः — after the इनुण् of 3.3.44 "
                  "अभिविधौ भाव इनुण्. **सांराविणं वर्तते**, a "
                  "clamour all round; सांकूटिनम्"),
    Samasanta("5.4.16", gives="aṇ", of=("visārin",),
              result="matsya",
              why="विसारिणो मत्स्ये — **विसरतीति विसारी**, one "
                  "that spreads out, and only of a FISH. "
                  "**वैसारिणो मत्स्यः**. **मत्स्य इति किम्?** "
                  "विसारी देवदत्तः",
              keeps_out="विसारी देवदत्तः"),
    Samasanta("5.4.17", gives="kṛtvasuc", of_samjna="saṃkhyā",
              result="kriyābhyāvṛttigaṇana",
              why="संख्यायाः क्रियाभ्यावृत्तिगणने कृत्वसुच् — "
                  "counting how often an act RECURS. "
                  "**पौनःपुन्यम् अभ्यावृत्तिः; एककर्तृकाणां "
                  "तुल्यजातीयानां क्रियाणां जन्मसंख्यानं "
                  "क्रियाभ्यावृत्तिगणनम्** — counting the "
                  "occurrences of acts of one kind by one agent. "
                  "पञ्च वारान् भुङ्क्ते **पञ्चकृत्वः**.\\n\\n"
                  "Every word of the rule is tested. "
                  "**संख्याया इति किम्?** भूरीन् वारान् भुङ्क्ते. "
                  "**क्रियाग्रहणं किमर्थम्?** **उत्तरार्थम्**, for "
                  "5.4.19, where **क्रियैव गण्यते, नाभ्यावृत्तिः, "
                  "असंभवात्**. **अभ्यावृत्तिग्रहणं किम्?** "
                  "पञ्च पाकाः. **गणनग्रहणं किमर्थम्, यावता "
                  "गणनात्मिकैव संख्या?** — so that the affix "
                  "reaches **शतं वाराणां भुङ्क्ते** as well as "
                  "शतं वारान्",
              keeps_out="भूरीन् वारान् भुङ्क्ते, पञ्च पाकाः"),
    Samasanta("5.4.18", gives="suc", of=("dvi", "tri", "catur"),
              of_samjna="saṃkhyā", result="kriyābhyāvṛttigaṇana",
              excepts=("5.4.17",),
              why="द्वित्रिचतुर्भ्यः सुच्, **कृत्वसुचोऽपवादः**. "
                  "**द्विर्भुङ्क्ते, त्रिर्भुङ्क्ते**, चतुर्भुक्तम्. "
                  "**चकारः स्वरार्थः**"),
    Samasanta("5.4.19", gives="suc", of=("eka",), adesa="sakṛt",
              of_samjna="saṃkhyā", result="kriyāgaṇana",
              excepts=("5.4.17",),
              why="एकस्य सकृच्च — the affix and the substitution "
                  "together, **कृत्वसुचोऽपवादः**. "
                  "**अभ्यावृत्तिस्त्विह न संभवति** — one "
                  "occurrence is not a RECURRENCE, which is why "
                  "5.4.17 said *act* separately. **सकृद् भुङ्क्ते, "
                  "सकृदधीते**. **एकः पाक इत्यत्र न भवति, "
                  "अनभिधानात्**",
              keeps_out="एकः पाकः"),
    Samasanta("5.4.20", gives="dhā", of=("bahu",),
              of_samjna="saṃkhyā", optional=True,
              result="aviprakṛṣṭakāla", excepts=("5.4.17",),
              why="विभाषा बहोर्धाविप्रकृष्टकाले, "
                  "**कृत्वसुचोऽपवादः; पक्षे सोऽपि भवति**. "
                  "**अविप्रकृष्टग्रहणं क्रियाभ्यावृत्तिविशेषणम्; "
                  "क्रियाणाम् उत्पत्तयश्चेद् आसन्नकाला भवन्ति** — "
                  "only where the recurrences come CLOSE TOGETHER. "
                  "**बहुधा दिवसस्य भुङ्क्ते**, many times in a "
                  "day; **अविप्रकृष्टकाल इति किम्?** बहुकृत्वो "
                  "मासस्य भुङ्क्ते",
              keeps_out="बहुकृत्वो मासस्य भुङ्क्ते"),
    Samasanta("5.4.21", gives="mayaṭ", case="prathamā",
              result="prakṛta",
              why="तत्प्रकृतवचने मयट् — **प्राचुर्येण प्रस्तुतं "
                  "प्रकृतम्**, what is chiefly on hand. **टकारो "
                  "ङीबर्थः**. अन्नं प्रकृतम् **अन्नमयम्**; "
                  "अपूपमयम्.\\n\\n"
                  "**AND THE COMMENTARY GIVES A SECOND READING AND "
                  "KEEPS BOTH.** **अपरे पुनरेवं सूत्रार्थमाहुः — "
                  "प्रकृतमित्युच्यतेऽस्मिन्निति प्रकृतवचनम्**: on "
                  "that reading the affix reports the OCCASION and "
                  "not the thing, **अन्नमयो यज्ञः, अपूपमयं पर्व, "
                  "वटकमयी यात्रा**. **द्वयमपि प्रमाणम्, उभयथा "
                  "सूत्रप्रणयनात्** — the fourth place in these "
                  "pādas where the Kāśikā declines to choose"),
    Samasanta("5.4.22", gives="mayaṭ", also_gives=("samūhavat",),
              case="prathamā", result="prakṛta-bahuṣu",
              excepts=("5.4.21",),
              why="समूहवच्च बहुषु — where MANY things are on hand, "
                  "the affixes of the *collection* section come, "
                  "**चकाराद् मयट् च**. मोदकाः प्रकृताः "
                  "**मौदकिकम्, मोदकमयम्**; शाष्कुलिकम्, "
                  "शष्कुलीमयम्.\\n\\n"
                  "**अतिवर्तन्तेऽपि स्वार्थिकाः प्रकृतितो "
                  "लिङ्गवचनानि** — and the gender and number "
                  "override again, the base being plural and the "
                  "derived word singular"),
    Samasanta("5.4.23", gives="ñya", gana="anantādi",
              optional=True,
              why="अनन्तावसथेतिहभेषजाञ् ञ्यः. अनन्त एव "
                  "**आनन्त्यम्**; आवसथ एव **आवसथ्यम्**; "
                  "इति ह **ऐतिह्यम्**, **निपातसमुदायोऽयम् "
                  "उपदेशपारम्पर्ये वर्तते** — a bundle of "
                  "particles meaning *tradition*, what is handed "
                  "down; भेषजमेव **भैषज्यम्**. "
                  "**महाविभाषया विकल्पते प्रत्ययः**"),
    Samasanta("5.4.24", gives="yat", of_samjna="devatānta",
              case="caturthī", result="tādarthya",
              why="देवतान्तात् तादर्थ्ये यत् — **तदर्थ एव "
                  "तादर्थ्यम्; चातुर्वर्ण्यादित्वात् ष्यञ्**. "
                  "अग्निदेवतायै इदम् **अग्निदेवत्यम्**; "
                  "पितृदेवत्यम्, वायुदेवत्यम्"),
    Samasanta("5.4.25", gives="yat", of=("pāda", "argha"),
              case="caturthī", result="tādarthya",
              why="पादार्घाभ्यां च. पादार्थमुदकं **पाद्यम्**; "
                  "**अर्घ्यम्**.\\n\\n"
                  "**अनुक्तसमुच्चयार्थश्चकारः; यथादर्शनम् "
                  "अन्यत्रापि प्रत्ययो भवति** — and the च gathers "
                  "in what is not said, which the vṛtti then fills "
                  "with fifteen Vedic bases: वसु, अपस्, ओक, कवि, "
                  "क्षेम, उदक, वर्चस्, निष्केवल, उक्थ, जन, पूर्व, "
                  "नव, सूर, मर्त, यविष्ठ — **वस॒व्य॑स्य, "
                  "**ओ॒क्ये॑**, **क॒व्यः**, **उक्थ्यम्**, "
                  "**पू॒र्व्या**, **सूर्यः॑**, **मर्त्यः॑**, "
                  "**य॒वि॒ष्ठ्यः॑**.\\n\\n"
                  "And eight vārttikas besides: "
                  "**समशब्दादावतुप्रत्ययो वक्तव्यः** — स॒मा॑व॒त्; "
                  "**नवस्य नू आदेशस्त्नप्तनप्खाश्च प्रत्ययाः** — "
                  "**नूत्नम्, नूतनम्, नवीनम्**; "
                  "**नश्च पुराणे प्रात्** — **प्॒रत्नम्**, प्रतनम्; "
                  "**भागरूपनामभ्यो धेयः** — **भागधेयम्, "
                  "नामधेयम्**; **आग्नीध्रसाधारणादञ्** — "
                  "आग्नी॑ध्रम्, साधा॑रणम्. And "
                  "**वाप्रकरणाच्च विकल्पन्त एतान्युपसंख्यानानि** — "
                  "all of them optional, the section being under an "
                  "option"),
    Samasanta("5.4.26", gives="ñya", of=("atithi",),
              case="caturthī", result="tādarthya",
              excepts=("5.4.24",),
              why="अतिथेर्ञ्यः. अतिथय इदम् **आतिथ्यम्**, the "
                  "hospitality due to a guest"),
    Samasanta("5.4.27", gives="tal", of=("deva",),
              why="देवात् तल् — **तादर्थ्य इति निवृत्तम्**. "
                  "देव एव **देवता**, and the word is feminine "
                  "where the base was masculine, which is the "
                  "override 5.4.14 was read as teaching"),
    Samasanta("5.4.28", gives="ka", of=("avi",),
              why="अवेः कः. अविरेव **अविकः**"),
    Samasanta("5.4.29", gives="kan", gana="yāvādi",
              why="यावादिभ्यः कन्. याव एव **यावकः**; मणिकः. "
                  "याव, मणि, अस्थि, चण्ड, पीत, स्तम्ब, "
                  "**ऋतावुष्णशीते**, **पशौ लूनवियाते**, "
                  "**अणु निपुणे**, **पुत्र कृत्रिमे**, "
                  "**स्नात वेदसमाप्तौ**, **शून्य रिक्ते**, "
                  "**दान कुत्सिते**, **तनु सूत्रे**, **ईयसश्च** — "
                  "श्रेयस्कः, ज्ञात, "
                  "**कुमारीक्रीडनकानि च** — यावादिः, and eleven "
                  "of the entries carry a sense of their own"),
    Samasanta("5.4.30", gives="kan", of=("lohita",),
              result="maṇi", excepts=("5.4.29",),
              why="लोहितान्मणौ. लोहितो मणिर् **लोहितकः**. "
                  "**मणाविति किम्?** लोहितः",
              keeps_out="लोहितः"),
    Samasanta("5.4.31", gives="kan", of=("lohita",),
              result="anitya-varṇa", excepts=("5.4.29",),
              why="वर्णे चानित्ये — of a colour that does NOT last. "
                  "**लोहितकः कोपेन**, red with anger; लोहितकः "
                  "पीडनेन. **अनित्य इति किम्?** लोहितो गौः, "
                  "लोहितं रुधिरम्. "
                  "**लोहिताल् लिङ्गबाधनं वा वक्तव्यम्** — and a "
                  "vārttika lets the gender be overridden: "
                  "**लोहितिका कोपेन, लोहिनिका कोपेन**",
              keeps_out="लोहितो गौः, लोहितं रुधिरम्"),
    Samasanta("5.4.32", gives="kan", of=("lohita",), result="rakta",
              excepts=("5.4.29",),
              why="रक्ते — of what has been DYED that colour, "
                  "**लाक्षादिना रक्ते**. **लोहितकः कम्बलः**, a red "
                  "blanket. **लिङ्गबाधनं वेत्येव** — लोहितिका, "
                  "लोहिनिका शाटी"),
    Samasanta("5.4.33", gives="kan", of=("kāla",),
              result="anitya-varṇa-rakta", excepts=("5.4.29",),
              why="कालाच्च — **वर्णे चानित्ये रक्त इति द्वयमपि "
                  "अनुवर्तते**, both conditions carried. "
                  "**कालकं मुखं वैलक्ष्येण**, a face gone dark with "
                  "shame; and dyed, **कालकः पटः, कालिका शाटी**"),
    Samasanta("5.4.34", gives="ṭhak", gana="vinayādi",
              optional=True,
              why="विनयादिभ्यष्ठक्. विनय एव **वैनयिकः**; "
                  "सामयिकः, औपयिकः. **विभाषाग्रहणेन विकल्प्यते "
                  "प्रत्ययः**. विनय, समय, "
                  "**उपायाद् ध्रस्वत्वं च**, संगति, कथंचित्, "
                  "अकस्मात्, समयाचार, उपचार, समाचार, व्यवहार, "
                  "संप्रदान, समुत्कर्ष, समूह, विशेष, अत्यय — "
                  "विनयादिः"),
    Samasanta("5.4.35", gives="ṭhak", of=("vāc",),
              result="vyāhṛtārthā",
              why="वाचो व्याहृतार्थायाम् — of a speech whose "
                  "meaning has ALREADY BEEN DECLARED. "
                  "**पूर्वमन्येनोक्तार्थत्वात् संदेशवाग् "
                  "व्याहृतार्थेत्युच्यते** — a message, saying "
                  "again what another said first. "
                  "**वाचिकं कथयति**. **व्याहृतार्थायामिति किम्?** "
                  "मधुरा वाक् देवदत्तस्य",
              keeps_out="मधुरा वाक् देवदत्तस्य"),
    Samasanta("5.4.36", gives="aṇ", of=("karman",),
              result="tadyukta",
              why="तद्युक्तात् कर्मणोऽण् — of the ACTION that goes "
                  "with such a message. **वाचिकं श्रुत्वा तथैव यत् "
                  "कर्म क्रियते तत् कार्मणम् इत्युच्यते**. "
                  "**कार्मणम्**.\n\n"
                  "**अण्प्रकरणे कुलालवरुडनिषादकर्मारचण्डाल"
                  "मित्रामित्रेभ्यश्छन्दस्युपसंख्यानम्** — seven "
                  "more in the Veda: **कौला॒लः, वारु॒डः, नैषा॒दः, "
                  "का॒र्मा॒रः, चाण्डा॒लः, मैत्रः, आमि॒त्रः**. And "
                  "a second vārttika adds thirteen, "
                  "**एतेऽणन्ताः स्वार्थिकाश्छन्दसि भाषायां च "
                  "इष्यन्ते** — in the Veda AND in speech: "
                  "सांना॒य्यम्, आनुजाव॒रः, राक्षो॒घ्नम्, "
                  "आग्राय॒णः॑, सान्तप॒नः"),
    Samasanta("5.4.37", gives="aṇ", of=("oṣadhi",),
              result="ajāti",
              why="ओषधेरजातौ — and NOT of the plant as a kind. "
                  "**औषधं पिबति**, drinks the medicine. "
                  "**अजाताविति किम्?** ओषधयः क्षेत्रे रूढा भवन्ति",
              keeps_out="ओषधयः क्षेत्रे रूढाः"),
    Samasanta("5.4.38", gives="aṇ", gana="prajñādi",
              why="प्रज्ञादिभ्यश्च — **प्रजानातीति प्रज्ञः**. "
                  "प्रज्ञ एव **प्राज्ञः**; **प्राज्ञी स्त्री**, an "
                  "intelligent woman.\n\n"
                  "**यस्यास्तु प्रज्ञा विद्यते सा प्राज्ञा भवति** "
                  "— but a woman who HAS understanding is प्राज्ञा "
                  "by 5.2.101, a different rule and a different "
                  "feminine. Two words alike but for the ending, "
                  "and the vṛtti separates them.\n\n"
                  "प्रज्ञ, वणिज्, उशिज्, प्रत्यक्ष, विद्वस्, "
                  "विदन्, षोडश, विद्या, मनस्, **श्रोत्र शरीरे**, "
                  "**जुह्वत् कृष्णमृगे**, चिकीर्षत्, चोर, शत्रु, "
                  "योध, चक्षुस्, धूर्त, मरुत्, राजन्, दशार्ह, "
                  "वयस्, आतुर, रक्षस्, पिशाच, अशनि, कार्षापण, "
                  "देवता, बन्धु — प्रज्ञादिः"),
    Samasanta("5.4.39", gives="tikan", of=("mṛd",), optional=True,
              why="मृदस्तिकन् — **विकल्पः सर्वत्रानुवर्तते**, the "
                  "option running through the whole section. "
                  "मृदेव **मृत्तिका**"),
    Samasanta("5.4.40", gives="sa", also_gives=("sna",),
              of=("mṛd",), result="praśaṃsā", excepts=("5.3.66",),
              why="सस्नौ प्रशंसायाम्, **रूपपोऽपवादः**. प्रशस्ता "
                  "मृद् **मृत्सा, मृत्स्ना**.\n\n"
                  "**नित्यश्चायं प्रत्ययः, उत्तरसूत्रे "
                  "अन्यतरस्यांग्रहणात्** — obligatory, and read so "
                  "from the NEXT rule saying *optionally*. The same "
                  "argument 5.4.7 used"),
    Samasanta("5.4.41", gives="til", of=("vṛka",),
              result="praśaṃsā", usage="chandasi",
              excepts=("5.3.66",),
              why="वृकज्येष्ठाभ्यां तिल्तातिलौ च छन्दसि, "
                  "**यथासंख्यम्**, **रूपपोऽपवादौ**; the वृक "
                  "member. **वृ॒कतिः॑** (ऋ० ४.४१.४)"),
    Samasanta("5.4.41", gives="tātil", of=("jyeṣṭha",),
              result="praśaṃsā", usage="chandasi",
              excepts=("5.3.66",),
              why="वृकज्येष्ठाभ्यां तिल्तातिलौ च छन्दसि, the "
                  "ज्येष्ठ member. **ज्ये॒ष्ठता॑तिः** (ऋ० ५.४४.१)"),
    Samasanta("5.4.42", gives="śas", of_samjna="bahvalpārtha",
              case="kāraka", optional=True,
              why="बह्वल्पार्थाच्छस् कारकादन्यतरस्याम् — after a "
                  "word meaning MUCH or LITTLE, standing as any "
                  "कारक. **विशेषानभिधानाच्च सर्वं कर्मादिकारकं "
                  "गृह्यते**. बहूनि ददाति **बहुशो ददाति**; "
                  "अल्पशः; बहुभिर्ददाति बहुशो ददाति.\n\n"
                  "**बह्वल्पार्थादिति किम्?** गां ददाति. "
                  "**कारकादिति किम्?** बहूनां स्वामी. "
                  "**अर्थग्रहणात् पर्यायेभ्योऽपि भवति** — "
                  "**भूरिशो ददाति, स्तोकशो ददाति**.\n\n"
                  "**बह्वल्पार्थान् मङ्गलवचनम्** — and a vārttika "
                  "adds that the affix is wanted where a GOOD OMEN "
                  "is meant: **बहुशो ददाति** of auspicious acts, "
                  "**अल्पशो ददाति** of unwelcome ones",
              keeps_out="गां ददाति, बहूनां स्वामी"),
    Samasanta("5.4.43", gives="śas", of_samjna="saṃkhyā-ekavacana",
              case="kāraka", result="vīpsā", optional=True,
              excepts=("5.4.42",),
              why="संख्यैकवचनाच्च वीप्सायाम् — after a numeral, "
                  "and after a word for ONE THING, where the sense "
                  "is repeated. **द्वौद्वौ मोदकौ ददाति द्विशः**; "
                  "कार्षापणंकार्षापणं ददाति **कार्षापणशः**, "
                  "**पादशो ददाति**.\n\n"
                  "**एकोऽर्थ उच्यते येन तदेकवचनम्; कार्षापणादयश्च "
                  "परिमाणशब्दा वृत्तावेकार्था एव भवन्ति**. "
                  "**संख्यैकवचनादिति किम्?** घटंघटं ददाति. "
                  "**वीप्सायामिति किम्?** द्वौ ददाति. "
                  "**कारकादित्येव** — द्वयोर्द्वयोः स्वामी",
              keeps_out="घटंघटं ददाति, द्वयोर्द्वयोः स्वामी"),
    Samasanta("5.4.44", gives="tasi", case="pañcamī",
              upapada="prati", result="pratiyoga", optional=True,
              why="प्रतियोगे पञ्चम्यास्तसिः — after the ablative "
                  "that goes with प्रति as a कर्मप्रवचनीय. "
                  "**प्रद्युम्नो वासुदेवतः प्रति**; अभिमन्युर् "
                  "अर्जुनतः प्रति. **वाग्रहणानुवृत्तेर्विकल्पेन "
                  "भवति** — वासुदेवात्, अर्जुनात् stand too.\n\n"
                  "**तसिप्रकरण आद्यादिभ्य उपसंख्यानम्** — "
                  "**आदितः, मध्यतः, पार्श्वतः, पृष्ठतः**; "
                  "**आकृतिगणश्चायम्**.\n\n"
                  "(And 5.3.8 replaced THIS affix by तसिल् after "
                  "किम् and the pronouns — the debt of that rule "
                  "pointing here, and paid.)"),
    Samasanta("5.4.45", gives="tasi", case="pañcamī",
              result="apādāna", optional=True,
              excludes=("hī", "ruh"),
              why="अपादाने चाहीयरुहोः — after an ablative of the "
                  "point of departure, provided the verb is not "
                  "हा or रुह्. **ग्रामत आगच्छति**, ग्रामात्; "
                  "**चोरतो बिभेति**; अध्ययनतः पराजयते.\n\n"
                  "**अहीयरुहोरिति किम्?** सार्थाद् हीयते, "
                  "पर्वतादवरोहति. **हीयत इति विकारनिर्देशो "
                  "जहातेः प्रतिपत्त्यर्थः, जिहीतेर्मा भूत्** — the "
                  "passive form is used to show WHICH root is "
                  "meant, so भूमित उज्जिहीते is not excluded.\n\n"
                  "**कथं मन्त्रो हीनः स्वरतो वर्णतो वा इति? "
                  "नैषा पञ्चमी; किं तर्हि? तृतीया** — that famous "
                  "line is not an ablative at all but an "
                  "instrumental",
              keeps_out="सार्थाद् हीयते, पर्वतादवरोहति"),
    Samasanta("5.4.46", gives="tasi", case="tṛtīyā-akartari",
              result="atigraha-avyathana-kṣepa", optional=True,
              why="अतिग्रहाव्यथनक्षेपेष्वकर्तरि तृतीयायाः — "
                  "**अतिक्रम्य ग्रहोऽतिग्रहः; अचलनम् अव्यथनम्; "
                  "क्षेपो निन्दा**, and the instrumental must not "
                  "be the AGENT. वृत्तेनातिगृह्यते "
                  "**वृत्ततोऽतिगृह्यते**, **सुष्ठुवृत्तवान् "
                  "अन्यानतिक्रम्य वृत्तेन गृह्यते**; वृत्तेन न "
                  "व्यथते **वृत्ततो न व्यथते**; वृत्तेन क्षिप्तः "
                  "**वृत्ततः क्षिप्तः**. **अकर्तरीति किम्?** "
                  "देवदत्तेन क्षिप्तः",
              keeps_out="देवदत्तेन क्षिप्तः"),
    Samasanta("5.4.47", gives="tasi", case="tṛtīyā-akartari",
              result="hīyamāna-pāpayoga", optional=True,
              excepts=("5.4.46",),
              why="हीयमानपापयोगाच्च. वृत्तेन हीयते **वृत्ततो "
                  "हीयते**; वृत्तेन पापः **वृत्ततः पापः**.\n\n"
                  "**क्षेपस्य चाविवक्षायां तत्त्वाख्यायाम् इदम् "
                  "उदाहरणम्; क्षेपे हि पूर्वेणैव सिद्धम्** — this "
                  "is for a plain statement of fact, the "
                  "reproachful sense being covered by the rule "
                  "before. **अकर्तरीत्येव** — देवदत्तेन हीयते",
              keeps_out="देवदत्तेन हीयते"),
    Samasanta("5.4.48", gives="tasi", case="ṣaṣṭhī",
              result="vyāśraya", optional=True,
              why="षष्ठ्या व्याश्रये — **नानापक्षसमाश्रयो "
                  "व्याश्रयः**, a taking of different sides. "
                  "**देवा अर्जुनतोऽभवन्**, the gods were on "
                  "Arjuna's side; आदित्याः कर्णतोऽभवन्. "
                  "**षष्ठी चात्र पक्षापेक्षैव**. "
                  "**व्याश्रय इति किम्?** वृक्षस्य शाखा",
              keeps_out="वृक्षस्य शाखा"),
    Samasanta("5.4.49", gives="tasi", case="ṣaṣṭhī",
              result="roga-apanayana", optional=True,
              excepts=("5.4.48",),
              why="रोगाच्चापनयने — after the genitive of a "
                  "DISEASE, where a REMEDY is meant, "
                  "**अपनयनं प्रतीकारः, चिकित्सेत्यर्थः**. "
                  "**प्रवाहिकातः कुरु**, do something for the "
                  "dysentery; कासतः कुरु. "
                  "**अपनयन इति किम्?** प्रवाहिकायाः प्रकोपनं कुरु",
              keeps_out="प्रवाहिकायाः प्रकोपनं कुरु"),
    Samasanta("5.4.50", gives="cvi", result="abhūtatadbhāva",
              upapada="kṛ-bhū-as",
              why="अभूततद्भावे कृभ्वस्तियोगे संपद्यकर्तरि च्विः — "
                  "the affix of BECOMING. **कारणस्य "
                  "विकाररूपेणाभूतस्य तदात्मना भावोऽभूततद्भावः** — "
                  "a thing coming to be what it was not. अशुक्लः "
                  "शुक्लः संपद्यते, तं करोति **शुक्लीकरोति**; "
                  "**शुक्लीभवति, शुक्लीस्यात्**; **घटीकरोति "
                  "मृदम्**.\n\n"
                  "Three conditions, three counter-examples. "
                  "**अभूततद्भाव इति किम्?** शुक्लं करोति, "
                  "**नात्र प्रकृतिर्विवक्षिता**. "
                  "**कृभ्वस्तियोग इति किम्?** अशुक्लः शुक्लो "
                  "जायते. **संपद्यकर्तरीति किम्?** — and the "
                  "vṛtti asks why that is needed, the sense giving "
                  "it already: **कारकान्तरसंपत्तौ मा भूत् — "
                  "अदेवगृहे देवगृहे संपद्यते**, where the becoming "
                  "belongs to a LOCUS and not to an agent",
              keeps_out="शुक्लं करोति, अशुक्लः शुक्लो जायते"),
    Samasanta("5.4.51", gives="cvi", adesa="antalopa",
              gana="aruḥprabhṛti", result="abhūtatadbhāva",
              upapada="kṛ-bhū-as", excepts=("5.4.50",),
              why="अरुर्मनश्चक्षुश्चेतोरहोरजसां लोपश्च — the "
                  "affix and the loss of the base's ending. "
                  "**अत्र सर्वविशेषणसंबन्धात् पूर्वेणैव प्रत्ययः "
                  "सिद्धः, लोपमात्रार्थ आरम्भः** — the affix was "
                  "coming already and the rule is for the loss "
                  "alone. **अरूकरोति; उन्मनीकरोति, उच्चक्षूकरोति, "
                  "विचेतीकरोति, विरहीकरोति, विरजीकरोति**"),
    Samasanta("5.4.52", gives="sāti", result="kārtsnya",
              upapada="kṛ-bhū-as", optional=True,
              excepts=("5.4.50",),
              why="विभाषा साति कार्त्स्न्ये — where the change is "
                  "COMPLETE, **यदि प्रकृतिः कृत्स्नां "
                  "विकारात्मतामापद्यते**. **अग्निसाद्भवति "
                  "शस्त्रम्**, the weapon turns wholly to fire; "
                  "अग्नीभवति शस्त्रम्. **कार्त्स्न्य इति किम्?** "
                  "एकदेशेन पटः शुक्लीभवति.\n\n"
                  "**विभाषाग्रहणं च्वेः प्रापकम्; प्रत्ययविकल्पस्तु "
                  "महाविभाषयैव सिद्धः** — the *optionally* is "
                  "there to bring the च्वि in, the choice itself "
                  "being had from the great option anyway",
              keeps_out="एकदेशेन पटः शुक्लीभवति"),
    Samasanta("5.4.53", gives="sāti", result="abhividhi",
              upapada="kṛ-bhū-as-sampad", optional=True,
              excepts=("5.4.52",),
              why="अभिविधौ संपदा च — **अभिविधिरभिव्याप्तिः**, and "
                  "the च adds संपद् to the three verbs. "
                  "**अग्निसात्संपद्यते, अग्निसाद्भवति**.\n\n"
                  "**AND THE VṚTTI SEPARATES TWO SENSES THAT LOOK "
                  "ALIKE.** **अथाभिविधेः कार्त्स्न्यस्य च को "
                  "विशेषः? यत्रैकदेशेनापि सर्वा प्रकृतिर् "
                  "विकारमापद्यते सोऽभिविधिः** — where EVERY "
                  "instance of the thing changes, though each only "
                  "in part: **यथास्यां सेनायाम् उत्पातेन सर्वं "
                  "शस्त्रम् अग्निसात्संपद्यते**, every weapon in "
                  "the army takes fire. **कार्त्स्न्यं तु "
                  "सर्वात्मना द्रव्यस्य विकाररूपापत्तौ भवति** — "
                  "where ONE thing changes wholly. Extent against "
                  "completeness"),
    Samasanta("5.4.54", gives="sāti", of_samjna="svāmivicaeṣa",
              result="tadadhīna", upapada="kṛ-bhū-as-sampad",
              why="तदधीनवचने — **अभूततद्भाव इति निवृत्तम्, "
                  "अर्थान्तरोपादानात्**, the *becoming* lapses. "
                  "**तदधीनं तदायत्तं तत्स्वामिकम् इत्यर्थः** — "
                  "made subject to someone. राजाधीनं करोति "
                  "**राजसात्करोति**; **ब्राह्मणसाद्भवति**"),
    Samasanta("5.4.55", gives="trā", also_gives=("sāti",),
              of_samjna="svāmivicaeṣa", result="tadadhīna-deya",
              upapada="kṛ-bhū-as-sampad", excepts=("5.4.54",),
              why="देये त्रा च — where what is made subject is a "
                  "thing TO BE GIVEN, **दातव्यं देयम्**. "
                  "**ब्राह्मणेभ्यो देयमिति यद् विज्ञातम्, तद् यदा "
                  "तेषां समर्पणेन तदधीनं क्रियते तदा त्रा "
                  "प्रत्ययः**: **ब्राह्मणत्राकरोति**, and "
                  "ब्राह्मणसात्करोति by the च. "
                  "**देय इति किम्?** राजसाद्भवति राष्ट्रम्",
              keeps_out="राजसाद्भवति राष्ट्रम्"),
    Samasanta("5.4.56", gives="trā",
              of=("deva", "manuṣya", "puruṣa", "puru", "martya"),
              case="dvitīyā-saptamī", optional=True,
              excepts=("5.4.55",),
              why="देवमनुष्यपुरुषपुरुमर्त्येभ्यो द्वितीयासप्तम्योर् "
                  "बहुलम् — **कृभ्वस्तिभिरिति नात्र संबध्यते; "
                  "सामान्येन विधानम्**, the three verbs not "
                  "carried. देवान् गच्छति **देवत्रा गच्छति**; "
                  "देवेषु वसति देवत्रा वसति; मनुष्यत्रा, "
                  "पुरुषत्रा, पुरुत्रा, मर्त्यत्रा.\n\n"
                  "**बहुलवचनाद् अन्यत्रापि भवति** — **बहु॒त्रा "
                  "जीव॑तो॒ मनः॑** (ऋ० १०.१६४.२)"),
    Samasanta("5.4.57", gives="ḍāc",
              of_samjna="avyaktānukaraṇa-dvyajavarārdha",
              upapada="kṛ-bhū-as", excludes=("iti",),
              why="अव्यक्तानुकरणाद् द्व्यजवरार्धाद् अनितौ डाच् — "
                  "an affix for the ECHO OF A SOUND. "
                  "**यत्र ध्वनावकारादयो वर्णा विशेषरूपेण न "
                  "व्यज्यन्ते सोऽव्यक्तः**, a noise in which no "
                  "letters can be told apart; and the LATTER HALF "
                  "of it must have two vowels, **यस्यापकर्षे "
                  "क्रियमाणे सुष्ठु न्यूनम् अर्धं द्व्यच्कं "
                  "संपद्यते**.\n\n"
                  "**डाचि बहुलं द्वे भवतः इति विषयसप्तमी; डाचि "
                  "विवक्षिते द्विर्वचनमेव पूर्वं क्रियते, पश्चात् "
                  "प्रत्ययः** (वा० ८.१.१२) — the doubling happens "
                  "FIRST and the affix after, though the affix is "
                  "what calls for it. **पटपटाकरोति, "
                  "दमदमाकरोति**.\n\n"
                  "**अव्यक्तानुकरणादिति किम्?** दृषत्करोति. "
                  "**द्व्यजवरार्धादिति किम्?** श्रत्करोति. "
                  "**अवरग्रहणं किम्?** खरटखरटाकरोति. "
                  "**अनिताविति किम्?** पटिति करोति",
              keeps_out="दृषत्करोति, श्रत्करोति, पटिति करोति"),
    Samasanta("5.4.58", gives="ḍāc",
              of=("dvitīya", "tṛtīya", "śamba", "bīja"),
              result="kṛṣi", upapada="kṛ",
              why="कृञो द्वितीयतृतीयशम्बबीजात् कृषौ — of "
                  "PLOUGHING, and with कृ alone: "
                  "**पुनः कृञ्ग्रहणं भ्वस्त्योर्निवृत्त्यर्थम्**. "
                  "**द्वितीयाकरोति**, ploughs it a second time; "
                  "**शम्बाकरोति**, **अनुलोमकृष्टं क्षेत्रं पुनः "
                  "प्रतिलोमं कृषति**, ploughs it crossways; "
                  "**बीजाकरोति**, ploughs and sows at once. "
                  "**कृषाविति किम्?** द्वितीयं करोति पदम्",
              keeps_out="द्वितीयं करोति पदम्"),
    Samasanta("5.4.59", gives="ḍāc", of_samjna="saṃkhyā-guṇāntā",
              result="kṛṣi", upapada="kṛ", excepts=("5.4.58",),
              why="संख्यायाश्च गुणान्तायाः — from a numeral with "
                  "the word गुण after it. **द्विगुणाकरोति "
                  "क्षेत्रम्**, ploughs the field twice over. "
                  "**कृषाविति किम्?** द्विगुणां करोति रज्जुम्",
              keeps_out="द्विगुणां करोति रज्जुम्"),
    Samasanta("5.4.60", gives="ḍāc", of=("samaya",),
              result="yāpanā", upapada="kṛ", excepts=("5.4.58",),
              why="समयाच्च यापनायाम् — **कर्तव्यस्यावसरप्राप्तिः "
                  "समयः, तस्यातिक्रमणं यापना**, letting the time "
                  "for a thing go by. **समयाकरोति**, "
                  "**कालक्षेपं करोति**. **यापनायामिति किम्?** "
                  "समयं करोति",
              keeps_out="समयं करोति"),
    Samasanta("5.4.61", gives="ḍāc", of=("sapatra", "niṣpatra"),
              result="ativyathana", upapada="kṛ",
              excepts=("5.4.58",),
              why="सपत्रनिष्पत्रादतिव्यथने — **अतिव्यथनम् "
                  "अतिपीडनम्**. **सपत्राकरोति मृगं व्याधः**, "
                  "**सपत्रं शरमस्य शरीरे प्रवेशयति**, drives the "
                  "arrow in feathers and all; **निष्पत्राकरोति**, "
                  "**शरीराच्छरम् अपरपार्श्वे निष्क्रामयति**, "
                  "drives it clean through. **अतिव्यथन इति "
                  "किम्?** सपत्रं वृक्षं करोति जलसेचकः",
              keeps_out="सपत्रं वृक्षं करोति जलसेचकः"),
    Samasanta("5.4.62", gives="ḍāc", of=("niṣkula",),
              result="niṣkoṣaṇa", upapada="kṛ",
              excepts=("5.4.58",),
              why="निष्कुलान्निष्कोषणे — **निष्कोषणम् "
                  "अन्तरवयवानां बहिर्निष्कासनम्**, taking the "
                  "insides out. **निष्कुलाकरोति पशून्**. "
                  "**निष्कोषण इति किम्?** निष्कुलान् करोति "
                  "शत्रून्",
              keeps_out="निष्कुलान् करोति शत्रून्"),
    Samasanta("5.4.63", gives="ḍāc", of=("sukha", "priya"),
              result="ānulomya", upapada="kṛ",
              excepts=("5.4.58",),
              why="सुखप्रियादानुलोम्ये — **आनुलोम्यम् अनुकूलता, "
                  "आराध्यचित्तानुवर्तनम्**, falling in with "
                  "another's wishes. **सुखाकरोति, प्रियाकरोति**, "
                  "**स्वाम्यादेश्चित्तम् आराधयति**. And "
                  "**सुखं प्रियं वा कुर्वन्नपि आनुलोम्येऽवस्थित "
                  "एवमुच्यते** — one who really does please him is "
                  "called so too, so long as it is compliance. "
                  "**आनुलोम्य इति किम्?** सुखं करोत्यौषधपानम्",
              keeps_out="सुखं करोत्यौषधपानम्"),
    Samasanta("5.4.64", gives="ḍāc", of=("duḥkha",),
              result="prātilomya", upapada="kṛ",
              excepts=("5.4.58",),
              why="दुःखात् प्रातिलोम्ये — **प्रातिलोम्यं "
                  "प्रतिकूलता, स्वाम्यादेश्चित्तपीडनम्**. "
                  "**दुःखाकरोति भृत्यः**. **प्रातिलोम्य इति "
                  "किम्?** दुःखं करोति कदन्नम्",
              keeps_out="दुःखं करोति कदन्नम्"),
    Samasanta("5.4.65", gives="ḍāc", of=("śūla",), result="pāka",
              upapada="kṛ", excepts=("5.4.58",),
              why="शूलात् पाके. शूले पचति **शूलाकरोति मांसम्**, "
                  "roasts the meat on a spit. **पाक इति किम्?** "
                  "शूलं करोति कदन्नम्",
              keeps_out="शूलं करोति कदन्नम्"),
    Samasanta("5.4.66", gives="ḍāc", of=("satya",),
              result="aśapatha", upapada="kṛ",
              excepts=("5.4.58",),
              why="सत्यादशपथे — **सत्यशब्दोऽनृतप्रतिपक्षवचनः; "
                  "क्वचित् तु शपथे च वर्तते — सत्येन शापयेद् "
                  "विप्रम् इति, तस्यायं प्रतिषेधः**: the word can "
                  "mean an OATH, and that sense is excluded. "
                  "**सत्याकरोति वणिक् भाण्डम्**, "
                  "**मयैतत् क्रेतव्यमिति तथ्यं करोति**, the "
                  "merchant makes his word good. "
                  "**अशपथ इति किम्?** सत्यं करोति ब्राह्मणः",
              keeps_out="सत्यं करोति ब्राह्मणः"),
    Samasanta("5.4.67", gives="ḍāc", of=("madra",),
              result="parivāpaṇa", upapada="kṛ",
              excepts=("5.4.58",),
              why="मद्रात् परिवापणे — **परिवापणं मुण्डनम्**, "
                  "shaving. **मद्रशब्दो मङ्गलार्थः; मङ्गलं मुण्डनं "
                  "करोति, मद्राकरोति** — an auspicious shaving. "
                  "**भद्राच्चेति वक्तव्यम्** — **भद्राकरोति "
                  "नापितः कुमारम्**, the barber shaves the boy. "
                  "**परिवापण इति किम्?** भद्रं करोति",
              keeps_out="भद्रं करोति"),
    Samasanta("5.4.68", heading=True,
              why="समासान्ताः — and the whole of the rest of the "
                  "pāda is under this one word. From here the "
                  "affixes given are called समासान्त, the endings "
                  "a compound takes BECAUSE it is a compound, and "
                  "they are among the affixes 5.4.7 named as "
                  "obligatory: **समासान्ताश्चेति**.\n\n"
                  "The module is named for this heading, since "
                  "ninety-three of the pāda's hundred and sixty "
                  "sūtras stand under it"),
    Samasanta("5.4.69", refuses=True, upapada="pūjana",
              excepts=("5.4.68",),
              why="न पूजनात् — no compound-final after a word of "
                  "PRAISE. **सुराजा, अतिराजा; सुगौः, अतिगौः**.\n\n"
                  "**पूजायां स्वतिग्रहणं कर्तव्यम्** — and the "
                  "vārttika narrows it to सु and अति alone: "
                  "**इह मा भूत् — परमराजः, परमगवः**. "
                  "**प्राग्बहुव्रीहिग्रहणं च कर्तव्यम्** — and the "
                  "refusal stops before 5.4.113, so **सुसक्थः, "
                  "स्वक्षः** keep theirs",
              keeps_out="परमराजः, सुसक्थः"),
    Samasanta("5.4.70", refuses=True, of=("kim",),
              result="kṣepa", excepts=("5.4.68",),
              why="किमः क्षेपे — none after किम् in CONTEMPT. "
                  "**किंराजा यो न रक्षति**, a fine king who does "
                  "not protect; **किंगौर्यो न वहति**. "
                  "**क्षेप इति किम्?** कस्य राजा **किंराजः**",
              keeps_out="किंराजः, किंगवः"),
    Samasanta("5.4.71", refuses=True, upapada="nañ",
              of_samjna="tatpuruṣa", excepts=("5.4.68",),
              why="नञस्तत्पुरुषात् — none after a negative "
                  "तत्पुरुष. **अराजा, असखा, अगौः**. "
                  "**तत्पुरुषादिति किम्?** अनृचो माणवकः, अधुरं "
                  "शकटम् — those are बहुव्रीहि and keep theirs",
              keeps_out="अनृचो माणवकः"),
    Samasanta("5.4.72", refuses=True, upapada="nañ",
              of_samjna="pathin-anta-tatpuruṣa", optional=True,
              excepts=("5.4.71",),
              why="पथो विभाषा — **पूर्वेण नित्यः प्रतिषेधः "
                  "प्राप्तो विकल्प्यते**, what the rule before "
                  "refused outright is here a choice. **अपथम्, "
                  "अपन्थाः**"),
    Samasanta("5.4.73", gives="ḍac", of_samjna="bahuvrīhi",
              result="saṃkhyeya", excludes=("bahu", "gaṇa"),
              why="बहुव्रीहौ संख्येये डजबहुगणात् — after a "
                  "बहुव्रीहि meaning a NUMBER counted, बहु and गण "
                  "excepted. **उपदशाः, उपविंशाः**; "
                  "**द्वित्राः, पञ्चषाः**.\n\n"
                  "**संख्येय इति किम्?** चित्रगुः. "
                  "**अबहुगणादिति किम्?** उपबहवः, उपगणाः, "
                  "**अत्र स्वरे विशेषः**. And a vārttika adds the "
                  "तत्पुरुष: **निस्त्रिंशानि वर्षाणि**, "
                  "**निस्त्रिंशः खड्गः**, a sword over thirty "
                  "fingers long",
              keeps_out="चित्रगुः, उपबहवः"),
    Samasanta("5.4.74", gives="a",
              of_samjna="ṛk-pur-ap-dhur-pathin-anta",
              excludes=("akṣa-dhur",),
              why="ऋक्पूरब्धूःपथामानक्षे — after a compound ending "
                  "in one of five words. **बहुव्रीहाविति न "
                  "स्वर्यते; सामान्येन विधानम्**. "
                  "**अर्धर्चः; ललाटपुरम्; द्वीपम्, अन्तरीपम्, "
                  "समीपम्; राजधुरा; स्थलपथः, जलपथः**.\n\n"
                  "**सामर्थ्याद् धुर एतद्विशेषणम् ऋगादीनां न "
                  "भवति** — the exception belongs to धुर् alone. "
                  "**अनक्ष इति किम्?** अक्षस्य धूः **अक्षधूः**.\n\n"
                  "**अनृचो माणवके ज्ञेयः, बह्वृचश्चरणाख्यायाम्** "
                  "(महाभाष्य) — and the affix is confined by usage: "
                  "**अनृक्कं साम, बह्वृक्कं सूक्तम्** do not have "
                  "it",
              keeps_out="अक्षधूः, अनृक्कं साम"),
    Samasanta("5.4.75", gives="ac", upapada="prati-anu-ava",
              of_samjna="sāma-loman-anta",
              why="अच् प्रत्यन्ववपूर्वात् सामलोम्नः. "
                  "**प्रतिसामम्, अनुसामम्, अवसामम्; प्रतिलोमम्, "
                  "अनुलोमम्, अवलोमम्**.\n\n"
                  "And a kārikā adds four more bases:\n\n"
                  "    कृष्णोदक्पाण्डुपूर्वाया भूमेरच्प्रत्ययः "
                  "स्मृतः ।\n"
                  "    गोदावर्याश्च नद्याश्च संख्याया उत्तरे "
                  "यदि ॥\n\n"
                  "**कृष्णभूमः, पाण्डुभूमः; पञ्चनदम्, "
                  "पञ्चगोदावरम्**. **भूमेरपि संख्यापूर्वायाः** — "
                  "**द्विभूमः प्रासादः**, a two-storeyed palace. "
                  "**अन्यत्रापि च दृश्यते** — पद्मनाभः, "
                  "दीर्घरात्रः, **तदेतत् सर्वमिह योगविभागं कृत्वा "
                  "साधयन्ति**"),
    Samasanta("5.4.76", gives="ac", of_samjna="akṣyanta",
              excludes=("darśana",),
              why="अक्ष्णोऽदर्शनात् — after a compound ending in "
                  "अक्षि when it does NOT mean the organ of sight. "
                  "**लवणाक्षम्, पुष्कराक्षम्**. "
                  "**अदर्शनादिति किम्?** ब्राह्मणाक्षि.\n\n"
                  "**कथं कबराक्षं गवाक्षमिति?** — a lattice is "
                  "seen through, and a window; are they not "
                  "*sight*? **नैष दोषः। चक्षुःपर्यायवचनो "
                  "दर्शनशब्दः, प्राण्यङ्गवचन इहाश्रीयते** — the "
                  "word means the EYE, a part of a living body, "
                  "not seeing in general",
              keeps_out="ब्राह्मणाक्षि"),
    Samasanta("5.4.77", nipatana=True, gives="ac",
              gana="acaturādi",
              why="अचतुरविचतुरसुचतुर… — thirty-odd forms laid "
                  "down, **समासे व्यवस्थापि निपातनादेव "
                  "प्रतिपत्तव्या**, the KIND of compound got from "
                  "the laying-down too. And the vṛtti sorts them: "
                  "**आद्यास्त्रयो बहुव्रीहयः** — अचतुरः, विचतुरः, "
                  "सुचतुरः. **ततः पर एकादश द्वन्द्वाः** — "
                  "**स्त्रीपुंसौ**, धेन्वनडुहौ, ऋक्सामे, "
                  "**वाङ्मनसे**, अक्षिभ्रुवम्, दारगवम्, "
                  "ऊर्वष्ठीवम्, पदष्ठीवम्, **नक्तंदिवम्**, "
                  "रात्रिंदिवम्, अहर्दिवम्.\n\n"
                  "**एकोऽव्ययीभावः साकल्ये** — **सरजसम् "
                  "अभ्यवहरति**, eats it dust and all; and not in a "
                  "बहुव्रीहि, सरजः पङ्कजम्. **ततस्तत्पुरुषः** — "
                  "**निश्श्रेयसम्**. **ततः षष्ठीसमासः** — "
                  "**पुरुषायुषम्**, and not the द्वन्द्व "
                  "पुरुषायुषी. **ततो द्विगू** — द्व्यायुषम्, "
                  "त्र्यायुषम्. **ततो द्वन्द्वः** — ऋग्यजुषम्. "
                  "**जातादिपूर्वपदा उक्षशब्दान्तास्त्रयः "
                  "कर्मधारयाः** — **महोक्षः**, and not the "
                  "बहुव्रीहि महोक्षा. **ततोऽव्ययीभावः** — "
                  "उपशुनम्. **ततः सप्तमीसमासः** — गोष्ठश्वः.\n\n"
                  "One sūtra, nine kinds of compound, and each "
                  "with its own counter-example",
              keeps_out="स्त्रीपुमान्, सरजः पङ्कजम्, महोक्षा"),
    Samasanta("5.4.78", gives="ac", upapada="brahman-hastin",
              of_samjna="varcasanta",
              why="ब्रह्महस्तिभ्यां वर्चसः. **ब्रह्मवर्चसम्, "
                  "हस्तिवर्चसम्**. **पल्यराजभ्यां चेति "
                  "वक्तव्यम्** — पल्यवर्चसम्, राजवर्चसम्"),
    Samasanta("5.4.79", gives="ac", upapada="ava-sam-andha",
              of_samjna="tamasanta",
              why="अवसमन्धेभ्यस्तमसः. **अवतमसम्, सन्तमसम्, "
                  "अन्धतमसम्**"),
    Samasanta("5.4.80", gives="ac", upapada="śvas",
              of_samjna="vasīyas-śreyas-anta",
              why="श्वसो वसीयःश्रेयसः. **श्वोवसीयसम्, "
                  "श्वःश्रेयसम्**, **मयूरव्यंसकादित्वात् "
                  "समासः**.\n\n"
                  "**स्वभावाच्चेह श्वःशब्द उत्तरपदार्थस्य "
                  "प्रशंसाम् आशीर्विषयाम् आचष्टे** — the *tomorrow* "
                  "here is not a time but a BLESSING: "
                  "**श्वःश्रेयसं ते भूयात्**, *may good be yours*"),
    Samasanta("5.4.81", gives="ac", upapada="anu-ava-tapta",
              of_samjna="rahasanta",
              why="अन्ववतप्ताद् रहसः. **अनुरहसम्, अवरहसम्, "
                  "तप्तरहसम्**"),
    Samasanta("5.4.82", gives="ac", upapada="prati",
              of_samjna="urasanta", result="saptamīstha",
              why="प्रतेरुरसः सप्तमीस्थात् — where the word उरस् "
                  "stands in the sense of a LOCATIVE, **उरसि "
                  "वर्तते**. **प्रत्युरसम्**. "
                  "**सप्तमीस्थादिति किम्?** प्रतिगतमुरः "
                  "**प्रत्युरः**",
              keeps_out="प्रत्युरः"),
    Samasanta("5.4.83", nipatana=True, gives="ac",
              of=("anugu",), result="āyāma",
              why="अनुगवमायामे — laid down, of LENGTH. "
                  "**अनुगवं यानम्**, a cart as long as an ox. "
                  "**आयाम इति किम्?** गवां पश्चाद् **अनुगु**",
              keeps_out="अनुगु"),
    Samasanta("5.4.84", nipatana=True, gives="ac",
              of=("dvistāva", "tristāva"), result="vedi",
              why="द्विस्तावा त्रिस्तावा वेदिः — laid down with "
                  "the affix, the loss of the ending AND the "
                  "compound. **यावती प्रकृतौ वेदिस्ततो द्विगुणा वा "
                  "त्रिगुणा वा कस्याञ्चिद् विकृतौ** — an altar "
                  "twice or three times the standard size. "
                  "**द्विस्तावा वेदिः**. **वेदिरिति किम्?** "
                  "द्विस्तावती रज्जुः",
              keeps_out="द्विस्तावती रज्जुः"),
    Samasanta("5.4.85", gives="ac", of_samjna="adhvananta",
              upapada="upasarga",
              why="उपसर्गादध्वनः. प्रगतोऽध्वानं **प्राध्वो रथः**; "
                  "निरध्वम्, प्रत्यध्वम्. **उपसर्गादिति किम्?** "
                  "परमाध्वा, उत्तमाध्वा",
              keeps_out="परमाध्वा"),
    Samasanta("5.4.86", gives="ac", of_samjna="aṅguly-anta",
              upapada="saṃkhyā-avyaya",
              why="तत्पुरुषस्याङ्गुलेः संख्याव्ययादेः. द्वे अङ्गुली "
                  "प्रमाणमस्य **द्व्यङ्गुलम्**; and from an "
                  "indeclinable, **निरङ्गुलम्, अत्यङ्गुलम्**. "
                  "**प्रमाणे लो द्विगोर्नित्यम् इति मात्रचो लोपः** "
                  "(वा० ५.२.३७).\n\n"
                  "**तत्पुरुषस्येति किम्?** पञ्चाङ्गुलिः, "
                  "अत्यङ्गुलिः पुरुषः. And "
                  "**तत्पुरुषाधिकारश्च द्वन्द्वाच्चुदषहान्तात् "
                  "इति यावत्** — the तत्पुरुष heading runs from "
                  "here to 5.4.106",
              keeps_out="पञ्चाङ्गुलिः"),
    Samasanta("5.4.87", gives="ac", of_samjna="rātry-anta",
              upapada="ahar-sarva-ekadeśa-saṃkhyāta-puṇya",
              why="अहस्सर्वैकदेशसंख्यातपुण्याच्च रात्रेः — "
                  "**चकारात् संख्यादेरव्ययादेश्च**, and "
                  "**अहर्ग्रहणं द्वन्द्वार्थम्**. "
                  "**अहोरात्रः**; सर्वरात्रः; a PART — "
                  "**पूर्वरात्रः, अपररात्रः**; counted — "
                  "**संख्यातरात्रः**; **पुण्यरात्रः**; and from a "
                  "numeral or indeclinable, **द्विरात्रः, "
                  "अतिरात्रः, नीरात्रः**"),
    Samasanta("5.4.88", adesa="ahna", of_samjna="ahan-anta",
              upapada="saṃkhyā-avyaya-sarvādi", before="ṭac",
              why="अह्नोऽह्न एतेभ्यः — the word अहन् becomes अह्न "
                  "before the टच् of 5.4.91, after the same bases "
                  "the rule before named. **संख्याव्ययादयः "
                  "प्रक्रान्ताः सर्वनाम्ना प्रत्यवमृश्यन्ते; "
                  "सामर्थ्याच्चाहःशब्दः पूर्वत्वेन नाश्रीयते; "
                  "न ह्यहःशब्दात् परोऽहःशब्दः संभवति** — the "
                  "*those* takes in all of 5.4.87's bases EXCEPT "
                  "अहन् itself, since no अहन् follows an अहन्. "
                  "**द्व्यह्नः, अत्यह्नः, सर्वाह्णः, पूर्वाह्णः, "
                  "संख्याताह्नः**"),
    Samasanta("5.4.89", refuses=True, adesa="ahna",
              of_samjna="ahan-anta", upapada="saṃkhyā",
              result="samāhāra", excepts=("5.4.88",),
              why="न संख्यादेः समाहारे — not where a numeral "
                  "stands first and the compound is a COLLECTION. "
                  "**पूर्वेण प्राप्तः प्रतिषिध्यते**. द्वे अहनी "
                  "समाहृते **द्व्यहः**. **समाहार इति किम्?** "
                  "द्वयोरह्नोर्भवो **द्व्यह्नः**",
              keeps_out="द्व्यह्नः"),
    Samasanta("5.4.90", refuses=True, adesa="ahna",
              of_samjna="ahan-anta", upapada="uttama-eka",
              excepts=("5.4.88",),
              why="उत्तमैकाभ्यां च — and not after two more. "
                  "**उत्तमशब्दोऽन्त्यवचनः पुण्यशब्दमाचष्टे; "
                  "पुण्यग्रहणमेव न कृतं वैचित्र्यार्थम्** — "
                  "*last* is used for *holy* just for variety. "
                  "**पुण्याहः, एकाहः**. **केचित् तु उपोत्तमस्यापि "
                  "प्रतिपत्त्यर्थं वर्णयन्ति** — and some read the "
                  "next-to-last in too, giving संख्याताहः"),
    Samasanta("5.4.91", gives="ṭac",
              of_samjna="rājan-ahan-sakhi-anta-tatpuruṣa",
              why="राजाहःसखिभ्यष्टच्. **महाराजः, मद्रराजः; "
                  "परमाहः; राजसखः, ब्राह्मणसखः**.\n\n"
                  "**AND THE ORDER OF THE WORDS IN THE RULE IS A "
                  "ज्ञापक.** **इह कस्माद् न भवति — मद्राणां राज्ञी "
                  "मद्रराज्ञी?** — the feminine should be reached "
                  "by लिङ्गविशिष्टपरिभाषा. "
                  "**लघ्वक्षरस्य पूर्वनिपाते प्राप्ते राजशब्दस्य "
                  "सवर्णदीर्घार्थं प्रथमं प्रयोगं कुर्वन्नेतद् "
                  "ज्ञापयति — यस्याकारेण सवर्णदीर्घत्वं संभवति "
                  "तस्येदं ग्रहणमिति**: राजन् should have come "
                  "second, being the longer; that it is put first "
                  "so as to make a long vowel with what follows "
                  "shows that only what CAN make that vowel is "
                  "meant, and राज्ञी cannot",
              keeps_out="मद्रराज्ञी"),
    Samasanta("5.4.92", gives="ṭac", of_samjna="go-anta-tatpuruṣa",
              excludes=("taddhita-luk",),
              why="गोरतद्धितलुकि — after a तत्पुरुष ending in गो, "
                  "provided no taddhita has been REMOVED in it. "
                  "**परमगवः; पञ्चगवम्, दशगवम्**.\n\n"
                  "**अतद्धितलुकीति किम्?** पञ्चभिर्गोभिः क्रीतः "
                  "**पञ्चगुः** — there 5.1.28 removed the आर्हीय "
                  "affix. **तद्धितग्रहणं किम्?** so the refusal "
                  "does not reach a dropped case-ending, "
                  "**राजगवीयति**. **लुग्ग्रहणं किम्?** so it does "
                  "not reach a taddhita that STANDS: "
                  "**पञ्चगवरूप्यम्, पञ्चगवमयम्**",
              keeps_out="पञ्चगुः"),
    Samasanta("5.4.93", gives="ṭac",
              of_samjna="uras-anta-tatpuruṣa", result="agrākhyā",
              why="अग्राख्यायामुरसः — where उरस् means the CHIEF "
                  "part, **अग्रं प्रधानमुच्यते; यथा "
                  "शरीरावयवानामुच्यत उरः प्रधानम्, एवमन्योऽपि "
                  "प्रधानभूत उरःशब्देनोच्यते**. **अश्वोरसम्**, the "
                  "pick of the horses; हस्त्युरसम्. "
                  "**अग्राख्यायामिति किम्?** देवदत्तोरः",
              keeps_out="देवदत्तोरः"),
    Samasanta("5.4.94", gives="ṭac",
              of_samjna="anas-aśman-ayas-saras-anta-tatpuruṣa",
              result="jāti-saṃjñā",
              why="अनोऽश्मायस्सरसां जातिसंज्ञयोः — of a KIND or a "
                  "NAME. **उपानसम्** a kind and **महानसम्** a "
                  "name; अमृताश्म / पिण्डाश्म; **कालायसम्** / "
                  "लोहितायसम्; मण्डूकसरसम् / जलसरसम् — four bases, "
                  "and each shown twice over. "
                  "**जातिसंज्ञयोरिति किम्?** सदनः, सदश्मा, सत्सरः",
              keeps_out="सदनः, सदश्मा"),
    Samasanta("5.4.95", gives="ṭac",
              of_samjna="takṣan-anta-tatpuruṣa",
              upapada="grāma-kauṭa",
              why="ग्रामकौटाभ्यां च तक्ष्णः — "
                  "**जातिसंज्ञयोरिति नानुवर्तते**. "
                  "**ग्रामतक्षः**, **बहूनां साधारणः**, a "
                  "carpenter who works for the whole village; "
                  "कुट्यां भवः कौटः, तस्य तक्षा **कौटतक्षः**, "
                  "**स्वतन्त्रः कर्मजीवी, न कस्यचित् प्रतिबद्धः**, "
                  "one who works for himself. "
                  "**ग्रामकौटाभ्यामिति किम्?** राजतक्षा",
              keeps_out="राजतक्षा"),
    Samasanta("5.4.96", gives="ṭac",
              of_samjna="śvan-anta-tatpuruṣa", upapada="ati",
              why="अतेः शुनः. अतिक्रान्तः श्वानम् **अतिश्वो "
                  "वराहः**, **जववानित्यर्थः**, a boar that "
                  "outruns a dog; **अतिश्वः सेवकः**, "
                  "**सुष्ठु स्वामिभक्तः**; **अतिश्वी सेवा**, "
                  "**अतिनीचा**. One word, three senses, and the "
                  "vṛtti gives each"),
    Samasanta("5.4.97", gives="ṭac",
              of_samjna="śvan-anta-tatpuruṣa", upapada="upamāna",
              result="aprāṇin", excepts=("5.4.96",),
              why="उपमानादप्राणिषु — where श्वन् is what a thing "
                  "is LIKENED to, and the thing is not alive. "
                  "आकर्षः श्वेव **आकर्षश्वः**; फलकश्वः. "
                  "**उपमानादिति किम्?** न श्वा **अश्वा** लोष्टः. "
                  "**अप्राणिष्विति किम्?** वानरः श्वेव "
                  "**वानरश्वा**",
              keeps_out="अश्वा लोष्टः, वानरश्वा"),
    Samasanta("5.4.98", gives="ṭac",
              of_samjna="sakthi-anta-tatpuruṣa",
              upapada="uttara-mṛga-pūrva-upamāna",
              why="उत्तरमृगपूर्वाच्च सक्थ्नः — **चकाराद् "
                  "उपमानाच्च**. **उत्तरसक्थम्, मृगसक्थम्, "
                  "पूर्वसक्थम्**; and from a likeness, "
                  "फलकमिव सक्थि **फलकसक्थम्**"),
    Samasanta("5.4.99", gives="ṭac", of_samjna="nau-anta-dvigu",
              excludes=("taddhita-luk",),
              why="नावो द्विगोः. द्वे नावौ समाहृते **द्विनावम्**; "
                  "द्विनावधनः, **द्विनावरूप्यम्**. "
                  "**द्विगोरिति किम्?** राजनौः. "
                  "**अतद्धितलुकीत्येव** — पञ्चभिर्नौभिः क्रीतः "
                  "**पञ्चनौः**",
              keeps_out="राजनौः, पञ्चनौः"),
    Samasanta("5.4.100", gives="ṭac",
              of_samjna="nau-anta-tatpuruṣa", upapada="ardha",
              excepts=("5.4.99",),
              why="अर्धाच्च. अर्धं नावो **अर्धनावम्**, and "
                  "**परवल्लिङ्गं न भवति, लोकाश्रयत्वाल् "
                  "लिङ्गस्य** — 2.4.26 would give it the gender of "
                  "the second member and does not, gender resting "
                  "on usage. The third time in these two pādas"),
    Samasanta("5.4.101", gives="ṭac",
              of_samjna="khārī-anta-dvigu-ardha", optional=True,
              why="खार्याः प्राचाम् — **प्राचामाचार्याणां "
                  "मतेन**, so the affix is a choice. द्वे "
                  "खार्यौ समाहृते **द्विखारम्, द्विखारि**; "
                  "अर्धं खार्या **अर्धखारम्, अर्धखारी**"),
    Samasanta("5.4.102", gives="ṭac",
              of_samjna="añjali-anta-dvigu", upapada="dvi-tri",
              excludes=("taddhita-luk",),
              why="द्वित्रिभ्यामञ्जलेः. द्वावञ्जली समाहृतौ "
                  "**द्व्यञ्जलम्**; त्र्यञ्जलम्. "
                  "**द्विगोरित्येव** — द्वयोरञ्जलिर् "
                  "**द्व्यञ्जलिः**. **अतद्धितलुकीत्येव** — "
                  "द्वाभ्यामञ्जलिभ्यां क्रीतो द्व्यञ्जलिः. "
                  "**प्राचामित्येव** — द्व्यञ्जलिप्रियः",
              keeps_out="द्व्यञ्जलिः"),
    Samasanta("5.4.103", gives="ṭac",
              of_samjna="an-as-anta-napuṃsaka-tatpuruṣa",
              usage="chandasi", optional=True,
              why="अनसन्तान्नपुंसकाच्छन्दसि — after a NEUTER "
                  "तत्पुरुष ending in अन् or अस्, in the Veda. "
                  "**हस्तिचर्मे जुहोति**; **देवच्छन्द॒सा॑नि**, "
                  "मनुष्यच्छन्द॒सम्.\n\n"
                  "**अनसन्तादिति किम्?** बिल्वदारु जुहोति. "
                  "**नपुंसकादिति किम्?** सु॒त्रामा॑णं पृथि॒वीम्. "
                  "**अनसन्तान्नपुंसकाच्छन्दसि वावचनम्** — and a "
                  "vārttika makes it optional: **ब्रह्मसाम** "
                  "beside **ब्रह्मसा॒मम्**",
              keeps_out="बिल्वदारु जुहोति"),
    Samasanta("5.4.104", gives="ṭac",
              of_samjna="brahman-anta-tatpuruṣa",
              result="jānapadākhyā",
              why="ब्रह्मणो जानपदाख्यायाम् — where the compound "
                  "names a brahman of a COUNTRY, **जनपदेषु भवो "
                  "जानपदः**. सुराष्ट्रेषु ब्रह्मा **सुराष्ट्रब्रह्मः**; "
                  "अवन्तिब्रह्मः. **योगविभागात् सप्तमीसमासः**. "
                  "**जानपदाख्यायामिति किम्?** देवब्रह्मा नारदः",
              keeps_out="देवब्रह्मा नारदः"),
    Samasanta("5.4.105", gives="ṭac",
              of_samjna="brahman-anta-tatpuruṣa",
              upapada="ku-mahat", optional=True,
              excepts=("5.4.104",),
              why="कुमहद्भ्यामन्यतरस्याम्. **कुब्रह्मः, कुब्रह्मा; "
                  "महाब्रह्मः, महाब्रह्मा**. "
                  "**ब्राह्मणपर्यायो ब्रह्मन्शब्दः** — and here "
                  "the word is the ordinary one for a brahmin, not "
                  "the officiant"),
    Samasanta("5.4.106", gives="ṭac",
              of_samjna="cu-ḍa-ṣa-ha-anta-dvandva",
              result="samāhāra",
              why="द्वन्द्वाच्चुदषहान्तात् समाहारे — "
                  "**तत्पुरुषाधिकारो निवृत्तः**, and the compound "
                  "must be a COLLECTIVE द्वन्द्व and not an "
                  "इतरेतरयोग. **वाक्त्वचम्, स्रक्त्वचम्, "
                  "श्रीस्रजम्, इडूर्जम्, समिद्दृषदम्, "
                  "संपद्विपदम्, वाग्विप्रुषम्, छत्रोपानहम्, "
                  "धेनुगोदुहम्** — one example for each of the "
                  "four endings and more.\n\n"
                  "**द्वन्द्वादिति किम्?** पञ्चवाक्. "
                  "**चुदषहान्तादिति किम्?** वाक्समित्. "
                  "**समाहार इति किम्?** प्रावृट्शरदौ",
              keeps_out="पञ्चवाक्, प्रावृट्शरदौ"),
    Samasanta("5.4.107", gives="ṭac", gana="śaratprabhṛti",
              of_samjna="avyayībhāva",
              why="अव्ययीभावे शरत्प्रभृतिभ्यः. शरदः समीपम् "
                  "**उपशरदम्**; प्रतिशरदम्, उपविपाशम्. "
                  "**अव्ययीभाव इति किम्?** परमशरत्.\n\n"
                  "**येऽत्र झयन्ताः पठ्यन्ते तेषां नित्यार्थं "
                  "ग्रहणम्** — the stop-final members are listed "
                  "so that the affix is OBLIGATORY for them. "
                  "**स्वर्यते चेदम् अव्ययीभावग्रहणं प्राग् "
                  "बहुव्रीहेः**. शरत्, विपाश्, अनस्, मनस्, "
                  "उपानह्, दिव्, हिमवत्, अनडुह्, दिश्, दृश्, "
                  "चतुर्, यद्, तद्, **जराया जरश्च**, "
                  "**प्रतिपरसमनुभ्योऽक्ष्णः** — प्रत्यक्षम्, "
                  "परोक्षम्, समक्षम् — पथिन् — शरत्प्रभृतिः",
              keeps_out="परमशरत्"),
    Samasanta("5.4.108", gives="ṭac", of_samjna="an-anta",
              upapada="avyayībhāva", excepts=("5.4.107",),
              why="अनश्च — after an अव्ययीभाव ending in अन्. "
                  "**उपराजम्, प्रतिराजम्; अध्यात्मम्, "
                  "प्रत्यात्मम्**"),
    Samasanta("5.4.109", gives="ṭac", of_samjna="an-anta-napuṃsaka",
              upapada="avyayībhāva", optional=True,
              excepts=("5.4.108",),
              why="नपुंसकादन्यतरस्याम् — **पूर्वेण नित्ये प्राप्ते "
                  "विकल्प्यते**. **प्रतिचर्मम्, प्रतिचर्म; "
                  "उपचर्मम्, उपचर्म**"),
    Samasanta("5.4.110", gives="ṭac",
              of_samjna="nadī-paurṇamāsī-āgrahāyaṇī-anta",
              upapada="avyayībhāva", optional=True,
              excepts=("5.4.107",),
              why="नदीपौर्णमास्याग्रहायणीभ्यः. नद्याः समीपम् "
                  "**उपनदम्, उपनदि**; उपपौर्णमासम्, उपपौर्णमासि"),
    Samasanta("5.4.111", gives="ṭac", of_samjna="jhayanta",
              upapada="avyayībhāva", optional=True,
              excepts=("5.4.107",),
              why="झयः — **झय इति प्रत्याहारग्रहणम्**, a stop or "
                  "an aspirate. **उपसमिधम्, उपसमित्; उपदृषदम्, "
                  "उपदृषत्**"),
    Samasanta("5.4.112", gives="ṭac", of_samjna="giry-anta",
              upapada="avyayībhāva", optional=True,
              excepts=("5.4.107",),
              why="गिरेश्च सेनकस्य — **सेनकग्रहणं पूजार्थम्; "
                  "विकल्पोऽनुवर्तत एव**. **अन्तर्गिरम्, "
                  "अन्तर्गिरि; उपगिरम्, उपगिरि**"),
    Samasanta("5.4.113", gives="ṣac", of_samjna="bahuvrīhi-svāṅga",
              upapada="sakthi-akṣi",
              why="बहुव्रीहौ सक्थ्यक्ष्णोः स्वाङ्गात् षच् — the "
                  "बहुव्रीहि heading opens, **आ पादपरिसमाप्तेर् "
                  "अनुवर्तते**. **दीर्घसक्थः; कल्याणाक्षः, "
                  "लोहिताक्षः, विशालाक्षः**.\n\n"
                  "**अयमर्थोऽभिप्रेतः। सूत्रे तु दुःश्लिष्ट"
                  "विभक्तीनि पदानि** — the sense is that, but the "
                  "case-endings of the sūtra fit it badly, and the "
                  "vṛtti says so plainly.\n\n"
                  "**बहुव्रीहाविति किम्?** परमसक्थि. "
                  "**सक्थ्यक्ष्णोरिति किम्?** दीर्घजानुः. "
                  "**स्वाङ्गादिति किम्?** दीर्घसक्थि शकटम्. "
                  "**टचि प्रकृते षज्ग्रहणं स्वरार्थम्** — the ष is "
                  "for the accent, through the feminine ङीष्",
              keeps_out="परमसक्थि, दीर्घजानुः, दीर्घसक्थि शकटम्"),
    Samasanta("5.4.114", gives="ṣac", of_samjna="bahuvrīhi",
              upapada="aṅguli", result="dāru",
              excepts=("5.4.113",),
              why="अङ्गुलेर्दारुणि — of a piece of WOOD. "
                  "**द्व्यङ्गुलं दारु**, **अङ्गुलिसदृशावयवं "
                  "धान्यादीनां विक्षेपणकाष्ठम् उच्यते**, a "
                  "winnowing-stick with finger-like prongs. And "
                  "where two fingers are the MEASURE, 5.4.86's अच् "
                  "comes instead. **दारुणीति किम्?** पञ्चाङ्गुलिर् "
                  "हस्तः",
              keeps_out="पञ्चाङ्गुलिर्हस्तः"),
    Samasanta("5.4.115", gives="ṣa", of_samjna="bahuvrīhi",
              upapada="dvi-tri-mūrdhan", excepts=("5.4.113",),
              why="द्वित्रिभ्यां ष मूर्ध्नः. **द्विमूर्धः, "
                  "त्रिमूर्धः**. **द्वित्रिभ्यामिति किम्?** "
                  "उच्चैर्मूर्धा",
              keeps_out="उच्चैर्मूर्धा"),
    Samasanta("5.4.116", gives="ap", of_samjna="bahuvrīhi",
              upapada="pūraṇī-pramāṇī",
              why="अप् पूरणीप्रमाण्योः. कल्याणी पञ्चमी आसां "
                  "रात्रीणां **कल्याणीपञ्चमा रात्रयः**; स्त्री "
                  "प्रमाणी एषां **स्त्रीप्रमाणाः कुटुम्बिनः**, "
                  "**भार्याप्रधानाः**.\n\n"
                  "**अपि प्रधानपूरणीग्रहणं कर्तव्यम्** — the "
                  "ordinal must be the PRINCIPAL word, "
                  "**यत्रान्यपदार्थे पूरण्यनुप्रविशति न केवलं "
                  "वर्तिपदार्थ एव**: **इह न भवति — "
                  "कल्याणपञ्चमीकः पक्षः**. "
                  "**नेतुर्नक्षत्र उपसंख्यानम्** — **मृगनेत्रा "
                  "रात्रयः**; and **छन्दसि च नेतुः** — "
                  "बृह॒स्पति॑नेत्रा दे॒वाः",
              keeps_out="कल्याणपञ्चमीकः पक्षः"),
    Samasanta("5.4.117", gives="ap", of_samjna="bahuvrīhi",
              upapada="antar-bahis-loman", excepts=("5.4.116",),
              why="अन्तर्बहिर्भ्यां च लोम्नः. **अन्तर्लोमः "
                  "प्रावारः**, a cloak with the fleece inside; "
                  "**बहिर्लोमः पटः**"),
    Samasanta("5.4.118", gives="ac", adesa="nas",
              of_samjna="bahuvrīhi", upapada="nāsikā",
              result="saṃjñā", excludes=("sthūla",),
              why="अञ्नासिकायाः संज्ञायां नसं चास्थूलात् — the "
                  "affix AND the change of नासिका to नस्, where "
                  "the whole word is a NAME and the first member is "
                  "not स्थूल. **द्रुणसः, वाद्ध्रीणसः, गोनसः** — "
                  "and 8.4.3 पूर्वपदात् संज्ञायामगः gives the ण.\n\n"
                  "**संज्ञायामिति किम्?** तुङ्गनासिकः. "
                  "**अस्थूलादिति किम्?** स्थूलनासिको वराहः. "
                  "**खुरखराभ्यां नस् वक्तव्यः** — **खुरणाः, "
                  "खरणाः**, and in the other half खुरणसः",
              keeps_out="तुङ्गनासिकः, स्थूलनासिको वराहः"),
    Samasanta("5.4.119", gives="ac", adesa="nas",
              of_samjna="bahuvrīhi", upapada="upasarga-nāsikā",
              excepts=("5.4.118",),
              why="उपसर्गाच्च — **असंज्ञार्थं वचनम्**, and here no "
                  "name is needed. उन्नता नासिकास्य **उन्नसः**; "
                  "प्रणसः, by 8.4.28 उपसर्गाद् बहुलम्. "
                  "**वेर्ग्रो वक्तव्यः** — विगता नासिकास्य "
                  "**विग्रः**"),
    Samasanta("5.4.120", nipatana=True, gives="ac",
              gana="suprātādi", of_samjna="bahuvrīhi",
              why="सुप्रातसुश्वसुदिवशारिकुक्षचतुरश्रैणीपदाजपद"
                  "प्रोष्ठपदाः — eight बहुव्रीहि compounds laid "
                  "down with the affix. **अन्यदपि च टिलोपादिकं "
                  "निपातनादेव सिद्धम्**. **सुप्रा॒तः, सुश्वः, "
                  "सु॒दिवः॑, शारिकुक्षः, चतुरश्रः, एणीपदः, "
                  "अजपदः, प्रोष्ठप॒दः**"),
    Samasanta("5.4.121", gives="ac", of_samjna="bahuvrīhi",
              upapada="nañ-dus-su-hali-sakthi", optional=True,
              excepts=("5.4.113",),
              why="नञ्दुःसुभ्यो हलिसक्थ्योरन्यतरस्याम्. "
                  "**अहलः, अहलिः; दुर्हलः, सुहलः; असक्थः, "
                  "असक्थिः**. **हलिशक्त्योरिति केचित् पठन्ति** — "
                  "and some read शक्ति for सक्थि: अशक्तः, अशक्तिः"),
    Samasanta("5.4.122", gives="asic", of_samjna="bahuvrīhi",
              upapada="nañ-dus-su-prajā-medhā",
              excepts=("5.4.121",),
              why="नित्यमसिच् प्रजामेधयोः. **अप्रजाः, दुष्प्रजाः, "
                  "सुप्रजाः; अमेधाः, दुर्मेधाः, सुमेधाः**.\n\n"
                  "**नित्यग्रहणं किम्? यावता पूर्वसूत्रे "
                  "अन्यतरस्यांग्रहणं नैव स्वर्यते? एवं तर्हि "
                  "नित्यग्रहणाद् अन्यत्रापि भवतीति सूच्यते** — "
                  "the *always* is idle where it stands and is read "
                  "as showing the affix comes elsewhere too, which "
                  "a verse illustrates: **श्रोत्रियस्येव ते राजन् "
                  "मन्दकस्याल्पमेधसः**"),
    Samasanta("5.4.123", nipatana=True, gives="asic",
              of=("bahuprajā",), of_samjna="bahuvrīhi",
              usage="chandasi", excepts=("5.4.122",),
              why="बहुप्रजाश्छन्दसि — laid down for the Veda. "
                  "**बहुप्॒रजा निर्ऋ॑ति॒मावि॑वेश** (ऋ० १.१६४.३२). "
                  "**छन्दसीति किम्?** बहुप्रजो ब्राह्मणः",
              keeps_out="बहुप्रजो ब्राह्मणः"),
    Samasanta("5.4.124", gives="anic", of_samjna="bahuvrīhi",
              upapada="kevala-dharma", excepts=("5.4.113",),
              why="धर्मादनिच् केवलात्. **कल्याणधर्मा, "
                  "प्रियधर्मा**. **केवलादिति किम्?** परमः स्वो "
                  "धर्मोऽस्य **परमस्वधर्मः**, and the vṛtti asks "
                  "how a three-word बहुव्रीहि is kept out at all: "
                  "**केवलादिति पूर्वपदं निर्दिश्यते, केवलात् पदाद् "
                  "यो धर्मशब्दो न पदसमुदायात्** — *alone* "
                  "describes the WORD before it and not the "
                  "compound",
              keeps_out="परमस्वधर्मः"),
    Samasanta("5.4.125", nipatana=True, of=("jambha",),
              of_samjna="bahuvrīhi",
              upapada="su-harita-tṛṇa-soma",
              why="जम्भा सुहरिततृणसोमेभ्यः — the compound-final "
                  "already made, and laid down. "
                  "**जम्भशब्दोऽभ्यवहार्यवाची दन्तविशेषवाची च** — "
                  "the word means FOOD and also a kind of TOOTH. "
                  "**सुजम्भा देवदत्तः**, either well fed or well "
                  "toothed; हरितजम्भा, तृणजम्भा, सोमजम्भा. "
                  "**सुहरिततृणसोमेभ्य इति किम्?** पतितजम्भः",
              keeps_out="पतितजम्भः"),
    Samasanta("5.4.126", nipatana=True, of=("dakṣiṇerman",),
              of_samjna="bahuvrīhi", result="lubdhayoga",
              why="दक्षिणेर्मा लुब्धयोगे — **लुब्धो व्याधः; ईर्मं "
                  "व्रणमुच्यते**. **दक्षिणेर्मा मृगः**, "
                  "**दक्षिणमङ्गं व्रणितमस्य व्याधेन**, a deer "
                  "wounded on the right side by the hunter. "
                  "**लुब्धयोग इति किम्?** दक्षिणेर्मं शकटम्",
              keeps_out="दक्षिणेर्मं शकटम्"),
    Samasanta("5.4.127", gives="ic", of_samjna="bahuvrīhi",
              result="karmavyatihāra",
              why="इच् कर्मव्यतिहारे — of a fight in which each "
                  "does to the other what the other does to him, "
                  "the बहुव्रीहि of 2.2.27. **केशेषु केशेषु "
                  "गृहीत्वा इदं युद्धं प्रवृत्तं केशाकेशि**, a "
                  "fight of pulling one another's hair; कचाकचि, "
                  "**मुसलामुसलि, दण्डादण्डि**"),
    Samasanta("5.4.128", nipatana=True, gives="ic",
              gana="dvidaṇḍyādi", of_samjna="bahuvrīhi",
              why="द्विदण्ड्यादिभ्यश्च — **द्विदण्ड्यादिभ्य इति "
                  "तादर्थ्ये एषा चतुर्थी, न पञ्चमी; "
                  "द्विदण्ड्याद्यर्थम् इच् प्रत्ययो भवति** — the "
                  "case in the rule is a dative of purpose and not "
                  "an ablative: the affix comes SO THAT these forms "
                  "come out. **द्विदण्डि प्रहरति**; and "
                  "**इह न भवति — द्विदण्डा शाला**.\n\n"
                  "**बहुव्रीह्यधिकारेऽपि तत्पुरुषात् क्वचिद् "
                  "विधानमिच्छन्ति** — and a तत्पुरुष is admitted "
                  "here and there: **निकुच्यकर्णि धावति**, "
                  "**प्रोह्यपादि हस्तिनं वाहयति**",
              keeps_out="द्विदण्डा शाला"),
    Samasanta("5.4.129", adesa="jñu", of_samjna="bahuvrīhi",
              upapada="pra-sam-jānu",
              why="प्रसम्भ्यां जानुनोर्ज्ञुः. प्रकृष्टे जानुनी "
                  "अस्य **प्रज्ञुः**; **संज्ञुः**"),
    Samasanta("5.4.130", adesa="jñu", of_samjna="bahuvrīhi",
              upapada="ūrdhva-jānu", optional=True,
              excepts=("5.4.129",),
              why="ऊर्ध्वाद् विभाषा. **ऊर्ध्वजानुः, ऊर्ध्वज्ञुः**"),
    Samasanta("5.4.131", adesa="anaṅ", of_samjna="bahuvrīhi",
              upapada="ūdhas", result="strī",
              why="ऊधसोऽनङ्. कुण्डमिव ऊधोऽस्याः **कुण्डोध्नी**; "
                  "घटोध्नी. **ऊधसोऽनङि स्त्रीग्रहणं कर्तव्यम्** — "
                  "and a vārttika adds *in the feminine*: "
                  "**इह मा भूत् — महोधाः पर्जन्यः**",
              keeps_out="महोधाः पर्जन्यः"),
    Samasanta("5.4.132", adesa="anaṅ", of_samjna="bahuvrīhi",
              upapada="dhanus",
              why="धनुषश्च. शार्ङ्गं धनुरस्य **शार्ङ्गधन्वा**; "
                  "**गाण्डीवधन्वा**, पुष्पधन्वा, अधिज्यधन्वा"),
    Samasanta("5.4.133", adesa="anaṅ", of_samjna="bahuvrīhi",
              upapada="dhanus", result="saṃjñā", optional=True,
              excepts=("5.4.132",),
              why="वा संज्ञायाम् — **पूर्वेण नित्यः प्राप्तो "
                  "विकल्प्यते**. **शतधनुः, शतधन्वा; दृढधनुः, "
                  "दृढधन्वा**"),
    Samasanta("5.4.134", adesa="niṅ", of_samjna="bahuvrīhi",
              upapada="jāyā",
              why="जायाया निङ्. युवतिर्जाया यस्य **युवजानिः**; "
                  "वृद्धजानिः"),
    Samasanta("5.4.135", adesa="i", of_samjna="bahuvrīhi",
              upapada="ut-pūti-su-surabhi-gandha",
              why="गन्धस्येदुत्पूतिसुसुरभिभ्यः. **तकार "
                  "उच्चारणार्थः**. उद्गतो गन्धोऽस्य "
                  "**उद्गन्धिः**; पूतिगन्धिः, **सुगन्धिः**, "
                  "सुरभिगन्धिः. **एतेभ्य इति किम्?** तीव्रगन्धो "
                  "वातः. **गन्धस्येत्वे तदेकान्तग्रहणम्** — "
                  "and the word must END the compound, "
                  "**सुगन्ध आपणिकः**",
              keeps_out="तीव्रगन्धो वातः, सुगन्ध आपणिकः"),
    Samasanta("5.4.136", adesa="i", of_samjna="bahuvrīhi",
              upapada="gandha", result="alpākhyā",
              excepts=("5.4.135",),
              why="अल्पाख्यायाम् — where गन्ध means A LITTLE. "
                  "**अल्पपर्यायो गन्धशब्दः**. सूपोऽल्पोऽस्मिन् "
                  "**सूपगन्धि भोजनम्**, food with a little sauce "
                  "in it; **घृतगन्धि, क्षीरगन्धि**"),
    Samasanta("5.4.137", adesa="i", of_samjna="bahuvrīhi",
              upapada="upamāna-gandha", excepts=("5.4.135",),
              why="उपमानाच्च. पद्मस्येव गन्धोऽस्य "
                  "**पद्मगन्धिः**; उत्पलगन्धिः, करीषगन्धिः"),
    Samasanta("5.4.138", adesa="pādalopa", of_samjna="bahuvrīhi",
              upapada="upamāna-pāda", excludes=("hastyādi",),
              why="पादस्य लोपोऽहस्त्यादिभ्यः — the loss of पाद, "
                  "and **स्थानिद्वारेण लोपस्य समासान्तता "
                  "विज्ञायते**: a LOSS counts as a compound-final "
                  "through what it stands in place of. "
                  "व्याघ्रस्येव पादावस्य **व्याघ्रपात्**; "
                  "**सिंहपात्**. **अहस्त्यादिभ्य इति किम्?** "
                  "हस्तिपादः, कटोलपादः",
              keeps_out="हस्तिपादः"),
    Samasanta("5.4.139", adesa="pādalopa", gana="kumbhapadyādi",
              of_samjna="bahuvrīhi", result="strī",
              excepts=("5.4.138",),
              why="कुम्भपदीषु च — **कुम्भपदीप्रभृतयः कृतपादलोपाः "
                  "समुदाया एव पठ्यन्ते**, the forms listed WITH "
                  "the loss already made. "
                  "**समुदायपाठस्य च प्रयोजनं विषयनियमः — "
                  "स्त्रियामेव, तत्र ङीप्प्रत्यय एव, नान्यदा** — "
                  "and listing them whole confines the loss to the "
                  "feminine and to that one feminine affix, "
                  "4.1.8's option not applying. **कुम्भपदी, "
                  "शतपदी, अष्टापदी, एकपदी**"),
    Samasanta("5.4.140", adesa="pādalopa", of_samjna="bahuvrīhi",
              upapada="saṃkhyā-su-pāda", excepts=("5.4.138",),
              why="संख्यासुपूर्वस्य. द्वौ पादावस्य **द्विपात्**; "
                  "त्रिपात्, **सुपात्**"),
    Samasanta("5.4.141", adesa="datṛ", of_samjna="bahuvrīhi",
              upapada="saṃkhyā-su-danta", result="vayas",
              why="वयसि दन्तस्य दतृ — where an AGE is meant. "
                  "**ऋकार उगित्कार्यार्थः**. द्वौ दन्तावस्य "
                  "**द्विदन्**; **सुदन् कुमारः**, a boy with a "
                  "full set. **वयसीति किम्?** द्विदन्तः कुञ्जरः, "
                  "सुदन्तो दाक्षिणात्यः",
              keeps_out="द्विदन्तः कुञ्जरः"),
    Samasanta("5.4.142", adesa="datṛ", of_samjna="bahuvrīhi",
              upapada="danta", usage="chandasi",
              excepts=("5.4.141",),
              why="छन्दसि च. **पत्रदतमालभेत**; उ॒भ॒**याद॑तः** "
                  "(ऋ० १०.९०.१०) आलभते"),
    Samasanta("5.4.143", adesa="datṛ", of_samjna="bahuvrīhi",
              upapada="danta", result="strī-saṃjñā",
              excepts=("5.4.141",),
              why="स्त्रियां संज्ञायाम् — in the feminine, where "
                  "the whole word is a name. **अयोदती, फालदती**. "
                  "**संज्ञायामिति किम्?** समदन्ती, स्निग्धदन्ती",
              keeps_out="समदन्ती"),
    Samasanta("5.4.144", adesa="datṛ", of_samjna="bahuvrīhi",
              upapada="śyāva-aroka-danta", optional=True,
              excepts=("5.4.141",),
              why="विभाषा श्यावारोकाभ्याम्. **श्यावदन्, "
                  "श्यावदन्तः; अरोकदन्, अरोकदन्तः** — "
                  "**अरोको निर्दीप्तिः**, without lustre"),
    Samasanta("5.4.145", adesa="datṛ", of_samjna="bahuvrīhi",
              upapada="agrānta-śuddha-śubhra-vṛṣa-varāha-danta",
              optional=True, excepts=("5.4.141",),
              why="अग्रान्तशुद्धशुभ्रवृषवराहेभ्यश्च. "
                  "**कुड्मलाग्रदन्, शुद्धदन्, शुभ्रदन्, वृषदन्, "
                  "वराहदन्**, each beside its दन्त form. "
                  "**अनुक्तसमुच्चयार्थश्चकारः** — **अहिदन्, "
                  "मूषिकदन्, गर्दभदन्, शिखरदन्**"),
    Samasanta("5.4.146", adesa="kakudalopa",
              of_samjna="bahuvrīhi", upapada="kakuda",
              result="avasthā",
              why="ककुदस्यावस्थायां लोपः — where a STAGE OF LIFE "
                  "is meant, **कालादिकृता वस्तुधर्मा वयःप्रभृतयो "
                  "ऽवस्थेत्युच्यते**. And the vṛtti gives five and "
                  "glosses each: **असंजातककुत्**, a calf; "
                  "**पूर्णककुत्**, middle-aged; **उन्नतककुत्**, "
                  "old; **स्थूलककुत्**, strong; **यष्टिककुत्**, "
                  "**नातिस्थूलो नातिकृशः**. "
                  "**अवस्थायामिति किम्?** श्वेतककुदः",
              keeps_out="श्वेतककुदः"),
    Samasanta("5.4.147", nipatana=True, adesa="kakudalopa",
              of=("trikakud",), of_samjna="bahuvrīhi",
              result="parvata", excepts=("5.4.146",),
              why="त्रिककुत् पर्वते. **त्रिककुत् पर्वतः**, and "
                  "**न च सर्वस्त्रिशिखरः पर्वतस्त्रिककुत्; किं "
                  "तर्हि? संज्ञैषा पर्वतविशेषस्य** — not every "
                  "three-peaked mountain, but the name of one. "
                  "**पर्वत इति किम्?** त्रिककुदोऽन्यः",
              keeps_out="त्रिककुदोऽन्यः"),
    Samasanta("5.4.148", adesa="kākudalopa",
              of_samjna="bahuvrīhi", upapada="ud-vi-kākuda",
              why="उद्विभ्यां काकुदस्य — **तालु काकुदम् उच्यते**, "
                  "the palate. **उत्काकुत्, विकाकुत्**"),
    Samasanta("5.4.149", adesa="kākudalopa",
              of_samjna="bahuvrīhi", upapada="pūrṇa-kākuda",
              optional=True, excepts=("5.4.148",),
              why="पूर्णाद् विभाषा. **पूर्णकाकुत्, पूर्णकाकुदः**"),
    Samasanta("5.4.150", nipatana=True, adesa="hṛd",
              of=("suhṛd", "durhṛd"), of_samjna="bahuvrīhi",
              result="mitra-amitra",
              why="सुहृद्दुर्हृदौ मित्रामित्रयोः, "
                  "**यथासंख्यम्**. शोभनं हृदयमस्य **सुहृद् "
                  "मित्रम्**; दुष्टं हृदयमस्य **दुर्हृद् "
                  "अमित्रम्**. **मित्रामित्रयोरिति किम्?** "
                  "**सुहृदयः कारुणिकः**, a tender-hearted man, "
                  "who is not therefore a friend",
              keeps_out="सुहृदयः कारुणिकः"),
    Samasanta("5.4.151", gives="kap", gana="uraḥprabhṛti",
              of_samjna="bahuvrīhi",
              why="उरःप्रभृतिभ्यः कप्. **व्यूढोरस्कः, "
                  "प्रियसर्पिष्कः, अवमुक्तोपानत्कः**.\n\n"
                  "**AND FOUR OF THE LIST ARE READ AS INFLECTED "
                  "WORDS.** **पुमान् अनड्वान् पयो नौर्लक्ष्मीरिति "
                  "विभक्त्यन्ताः पठ्यन्ते, न प्रातिपदिकानि** — "
                  "and the point is **एकवचनान्तानामेव ग्रहणमिह "
                  "विज्ञायेत, द्विवचनबहुवचनान्तानां मा भूत्**: "
                  "only the SINGULAR is taken, so a dual or plural "
                  "falls to 5.4.154's option — **द्विपुमान्, "
                  "द्विपुंस्कः**"),
    Samasanta("5.4.152", gives="kap", of_samjna="bahuvrīhi",
              upapada="in-anta", result="strī",
              excepts=("5.4.151",),
              why="इनः स्त्रियाम्. बहवो दण्डिनोऽस्यां शालायां "
                  "**बहुदण्डिका शाला**; **बहुस्वामिका नगरी**, "
                  "बहुवाग्ग्मिका सभा. **स्त्रियामिति किम्?** "
                  "बहुदण्डी राजा, बहुदण्डिकः by 5.4.154"),
    Samasanta("5.4.153", gives="kap", of_samjna="bahuvrīhi",
              upapada="nadī-ṛkārānta", excepts=("5.4.151",),
              why="नद्यृतश्च. बह्व्यः कुमार्योऽस्मिन् देशे "
                  "**बहुकुमारीको देशः**; बहुब्रह्मबन्धूकः; and "
                  "from an ऋ-final, **बहुकर्तृकः**. "
                  "**तकारो मुखसुखोच्चारणार्थः**"),
    Samasanta("5.4.154", gives="kap", of_samjna="bahuvrīhi",
              result="śeṣa", optional=True,
              why="शेषाद् विभाषा — **यस्माद् बहुव्रीहेः समासान्तो "
                  "न विहितः स शेषः**, whatever the rules before "
                  "have not reached. **बहुखट्वकः, बहुमालकः**, "
                  "and beside them बहुखट्वाकः and बहुखट्वः — three "
                  "forms.\n\n"
                  "**कथम् अनृक्कं साम बह्वृक्कं सूक्तम्?** — "
                  "5.4.74 gave those an affix generally. "
                  "**नैतदस्ति; विशेषे स इष्यते, अनृचो माणवके "
                  "ज्ञेयो बह्वृचश्चरणाख्यायाम्**: that rule is "
                  "wanted only in its particular senses, so these "
                  "fall to the remainder. **शेषादिति किम्?** "
                  "प्रियपथः, प्रियधुरः",
              keeps_out="प्रियपथः, प्रियधुरः"),
    Samasanta("5.4.155", refuses=True, of_samjna="bahuvrīhi",
              result="saṃjñā", excepts=("5.4.154",),
              why="न संज्ञायाम् — **पूर्वेण प्राप्तः "
                  "प्रतिषिध्यते**. विश्वे देवा अस्य "
                  "**विश्वदेवः**; विश्वयशाः"),
    Samasanta("5.4.156", refuses=True, of_samjna="bahuvrīhi",
              upapada="īyas-anta", excepts=("5.4.154",),
              why="ईयसश्च — **सर्वा प्राप्तिः प्रतिषिध्यते**, "
                  "every one of the rules is refused. "
                  "**बहुश्रेयान्** against 5.4.154, "
                  "**बहुश्रेयसी** against 5.4.153. "
                  "**ह्रस्वत्वमपि न भवति, ईयसो बहुव्रीहौ पुंवद् "
                  "इति वचनात्**"),
    Samasanta("5.4.157", refuses=True, of_samjna="bahuvrīhi",
              upapada="bhrātṛ", result="vandita",
              excepts=("5.4.153",),
              why="वन्दिते भ्रातुः — **वन्दितः स्तुतः पूजितः**. "
                  "शोभनो भ्रातास्य **सुभ्राता**. "
                  "**वन्दित इति किम्?** मूर्खभ्रातृकः, "
                  "दुष्टभ्रातृकः — where the brother is no credit "
                  "to him, the affix comes",
              keeps_out="मूर्खभ्रातृकः"),
    Samasanta("5.4.158", refuses=True, of_samjna="bahuvrīhi",
              upapada="ṛvarṇānta", usage="chandasi",
              excepts=("5.4.153",),
              why="ऋतश्छन्दसि. हता मातास्य **ह॒तमा॑ता॑**; "
                  "हतपिता, **ह॒तस्व॑सा**, **सुहो॑ता**"),
    Samasanta("5.4.159", refuses=True, of_samjna="bahuvrīhi",
              upapada="nāḍī-tantrī", result="svāṅga",
              excepts=("5.4.153",),
              why="नाडीतन्त्र्योः स्वाङ्गे — where the two words "
                  "name PARTS OF THE BODY, **धमनीवचनस्तन्त्रीशब्दः**. "
                  "**बहुनाडिः कायः**, a body with many vessels; "
                  "**बहुतन्त्रीर्ग्रीवा**. **स्वाङ्ग इति किम्?** "
                  "बहुनाडीकः स्तम्भः, **बहुतन्त्रीका वीणा** — a "
                  "lute with many strings keeps its affix",
              keeps_out="बहुतन्त्रीका वीणा"),
    Samasanta("5.4.160", nipatana=True, refuses=True,
              of=("niṣpravāṇi",), of_samjna="bahuvrīhi",
              excepts=("5.4.153",),
              why="निष्प्रवाणिश्च — the last sūtra of the chapter, "
                  "and a refusal laid down. "
                  "**प्रोयतेऽस्यामिति प्रवाणी; प्रवयन्ति तयेति वा "
                  "प्रवाणी; करणसाधनोऽयं ल्युट्; तन्तुवायशलाका "
                  "भण्यते** — a weaver's rod, named either as what "
                  "one weaves ON or what one weaves WITH. "
                  "निर्गता प्रवाणी अस्य **निष्प्रवाणिः पटः**, "
                  "**अपनीतशलाकः समाप्तवानः प्रत्यग्रो नवकः** — "
                  "cloth just off the loom with the rod taken "
                  "out.\n\n"
                  "इति श्रीजयादित्यविरचितायां काशिकायां वृत्तौ "
                  "पञ्चमाध्यायस्य चतुर्थः पादः"),
)


@dataclass(frozen=True)
class Added:
    """What the resolver answers with."""

    affix: str
    sutra: str
    why: str
    also_gives: Tuple[str, ...] = ()
    adesa: str = ""
    optional: bool = False
    nipatana: bool = False
    #: The rule that REFUSED, where one did. The answer's own
    #: `sutra` names what supplies.
    blocked_by: str = ""
    excepts: Tuple[str, ...] = ()


def _reaches(row: Samasanta, stem: str, gana: str, samjna: str,
             case: str, result: str, upapada: str,
             usage: str, before: str) -> bool:
    if row.heading:
        return False
    if row.of and stem not in row.of:
        return False
    if row.gana and gana != row.gana:
        return False
    if row.of_samjna and samjna != row.of_samjna:
        return False
    if row.case and case and case != row.case:
        return False
    if row.result and result != row.result:
        return False
    if row.upapada and upapada != row.upapada:
        return False
    if row.before and before != row.before:
        return False
    if row.usage and usage != row.usage:
        return False
    return True


def _supplies(row: Samasanta, wants: str) -> bool:
    return (not wants
            or wants == row.gives
            or wants in row.also_gives)


def _how_specific(row: Samasanta) -> int:
    """A named base is narrowest; the sense counts next."""
    return (
        8 * bool(row.of)
        + 7 * bool(row.gana)
        + 6 * bool(row.result)
        + 5 * bool(row.upapada)
        + 5 * bool(row.before)
        + 4 * bool(row.usage)
        + 3 * bool(row.of_samjna)
        + 1 * bool(row.case)
    )


def affix_for(stem: str = "", *, gana: str = "", samjna: str = "",
              case: str = "", result: str = "", upapada: str = "",
              usage: str = "", before: str = "",
              wants: str = "") -> Added:
    """
    5.4.1–30 — the affix added to a base in its own sense.

    Nothing stands over the section supplying by default, so a
    question that reaches no rule reaches nothing.
    """
    matched = [
        row for row in SAMASANTA_TABLE
        if _reaches(row, stem, gana, samjna, case, result, upapada,
                    usage, before)
        and _supplies(row, wants)
    ]
    if not matched:
        return Added("", "", "No rule of 5.4.1–30 is reached. "
                             "Nothing stands over the section "
                             "supplying by default")
    row = max(matched, key=_how_specific)
    if row.refuses:
        # 5.4.5 alone. A प्रतिषेध does not govern what it excepts,
        # so the answer names the rule that would have supplied and
        # records the refusal beside it.
        supplying = [other for other in matched
                     if not other.refuses and other.gives]
        if not supplying:
            return Added("", row.sutra, row.why,
                         blocked_by=row.sutra, excepts=row.excepts)
        beaten = max(supplying, key=_how_specific)
        return Added("", beaten.sutra, row.why,
                     blocked_by=row.sutra, excepts=row.excepts)
    return Added(row.gives, row.sutra, row.why,
                 also_gives=row.also_gives, adesa=row.adesa,
                 optional=row.optional, nipatana=row.nipatana,
                 excepts=row.excepts)


def provisions_for(sutra_id: str) -> Tuple[Samasanta, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in SAMASANTA_TABLE
                 if row.sutra == sutra_id)
