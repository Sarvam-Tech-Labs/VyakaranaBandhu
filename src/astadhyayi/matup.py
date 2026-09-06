# -*- coding: utf-8 -*-
"""
५.२.१–२८ — from a field of grain to a word that means *anyhow*.

अध्याय ५ पाद १ was seven headings deep: every rule of it stood under
one, and the question at each was which affix displaced which. This
pāda opens with none at all. Each rule names its own affix and its
own sense, and the senses do not run in families — a field where
grain grows, a cloth reaching the toes, a cow that calves every
year, a burglar's single house, butter churned from yesterday's
milking.

**AND SO THE COMMENTARY HAS TO SAY WHAT THE WORDS MEAN.** Where the
pāda before argued about ranges, this one glosses: **भवन्ति
जायन्तेऽस्मिन्निति भवनम्**, a growing-place is where things come to
be; **गावस्तिष्ठन्त्यस्मिन्निति गोष्ठम्**; **गोः पश्चाद् अनुगु**;
**नानाजातीया अनियतवृत्तय उत्सेधजीविनः संघा व्राताः**, a व्रात is a
troop of mixed birth and no settled livelihood who live by their
bodies.

The module is named for 5.2.94 तदस्यास्त्यस्मिन्निति मतुप्, which
governs the whole second half of the pāda and is the rule by which
Sanskrit says a thing HAS something.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class Matup:
    """One rule of 5.2: a base, a sense, and what comes."""

    sutra: str
    gives: str = ""
    #: The other affixes the same rule gives — 5.2.5's खखञौ,
    #: 5.2.17's three at once.
    also_gives: Tuple[str, ...] = ()
    of: Tuple[str, ...] = ()
    gana: str = ""
    #: The sense the derived word carries. No two rules of the
    #: opening stretch share one, which is what makes this pāda
    #: unlike the last.
    sense: str = ""
    case: str = ""
    #: A further condition on the derived word — क्षेत्र at 5.2.1,
    #: संज्ञा at 5.2.23, भूतपूर्व at 5.2.18.
    result: str = ""
    #: A class the base belongs to: धान्य at 5.2.1.
    of_samjna: str = ""
    #: The LAST member of the compound the rule names — 5.2.7's five.
    uttarapada: str = ""
    #: The sound or word the base ENDS in — 5.2.46's शद् and
    #: विंशति, 5.2.49's न्. Distinct from `uttarapada`, which asks
    #: after a compound's second member rather than a stem ending.
    stem_final: str = ""
    #: What stands in FRONT — 5.2.7's सर्वादि.
    pre: str = ""
    #: An आदेश the rule substitutes in the same act: 5.2.10's
    #: परोवर, 5.2.23's हियङ्गु.
    adesa: str = ""
    usage: str = ""
    optional: bool = False
    #: True where the whole FORM is laid down rather than derived —
    #: **निपात्यते**. Five of the first twenty-eight are, and the
    #: vṛtti is explicit each time that the analysis is a courtesy:
    #: **यथाकथंचिद् व्युत्पादयितव्यौ**, derive them somehow.
    nipatana: bool = False
    heading: bool = False
    excepts: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


MATUP_TABLE: Tuple[Matup, ...] = (
    Matup("5.2.1", gives="khañ", of_samjna="dhānya", sense="bhavana",
          case="ṣaṣṭhī", result="kṣetra",
          why="धान्यानां भवने क्षेत्रे खञ्. **निर्देशादेव "
              "समर्थविभक्तिः** — the case is got from the wording. "
              "**भवन्ति जायन्तेऽस्मिन्निति भवनम्**: a भवन is where "
              "things come to be. मुद्गानां भवनं क्षेत्रं "
              "**मौद्गीनम्**; कौद्रवीणम्, कौलत्थीनम्.\\n\\n"
              "**धान्यानामिति किम्?** तृणानां भवनं क्षेत्रम् — "
              "grass is not grain. **क्षेत्रमिति किम्?** मुद्गानां "
              "भवनं **कुसूलम्**, a granary, which is a growing-"
              "place of a sort and not a FIELD. "
              "**बहुवचनं स्वरूपविधिनिरासार्थम्** — and the plural "
              "stops the rule applying to the word धान्य itself",
          keeps_out="तृणानां भवनं क्षेत्रम्, मुद्गानां भवनं कुसूलम्"),
    Matup("5.2.2", gives="ḍhak", of=("vrīhi", "śāli"),
          sense="bhavana", case="ṣaṣṭhī", result="kṣetra",
          excepts=("5.2.1",),
          why="व्रीहिशाल्योर्ढक्, खञोऽपवादः. व्रीहीणां भवनं "
              "क्षेत्रं **व्रैहेयम्**; शालेयम्"),
    Matup("5.2.3", gives="yat", gana="yavādi", sense="bhavana",
          case="ṣaṣṭhī", result="kṣetra", excepts=("5.2.1",),
          why="यवयवकषष्टिकाद् यत्, खञोऽपवादः. यवानां भवनं क्षेत्रं "
              "**यव्यम्**; यवक्यम्, षष्टिक्यम्"),
    Matup("5.2.4", gives="yat", optional=True,
          of=("tila", "māṣa", "umā", "bhaṅgā", "aṇu"),
          sense="bhavana", case="ṣaṣṭhī", result="kṣetra",
          excepts=("5.2.1",),
          why="विभाषा तिलमाषोमाभङ्गाणुभ्यः. **खञि प्राप्ते वचनम्, "
              "पक्षे सोऽपि भवति** — the खञ् was coming and this "
              "makes the यत् an alternative to it, so both stand: "
              "**तिल्यम्, तैलीनम्**; माष्यम्, माषीणम्; उम्यम्, "
              "औमीनम्; भङ्ग्यम्, भाङ्गीनम्; अणव्यम्, आणवीनम्.\\n\\n"
              "**उमाभङ्गयोरपि धान्यत्वमाश्रितमेव** — and flax and "
              "hemp are treated as grain here, though they are not "
              "eaten, or 5.2.1 could not have reached them at all"),
    Matup("5.2.5", gives="kha", also_gives=("khañ",),
          of=("sarvacarman",), sense="kṛta", case="tṛtīyā",
          why="सर्वचर्मणः कृतः खखञौ. **सर्वचर्मीणः, "
              "सार्वचर्मीणः**.\\n\\n"
              "**AND THE COMPOUND IN THE RULE IS ONE THAT SHOULD "
              "NOT EXIST.** **सर्वशब्दश्चात्र प्रत्ययार्थेन कृतेन "
              "संबध्यते, न चर्मणा** — the *all* goes with the "
              "MAKING, which is what the affix reports, and not "
              "with the leather. So सर्व and चर्मन् have no "
              "relation to each other and yet stand compounded: "
              "**तत्रायम् असमर्थसमासो द्रष्टव्यः**, an "
              "असमर्थसमास, **सर्वश्चर्मणा कृत इत्येतस्मिन् "
              "वाक्यार्थे वृत्तिः** — the compound holds the sense "
              "of the whole sentence and not of its own two parts"),
    Matup("5.2.6", gives="kha", of=("yathāmukha", "saṃmukha"),
          sense="darśana", case="ṣaṣṭhī",
          why="यथामुखसंमुखस्य दर्शनः खः. **दृश्यतेऽस्मिन्निति "
              "दर्शनः, आदर्शादिः प्रतिबिम्बाश्रय उच्यते** — a "
              "दर्शन is what one is seen IN, a mirror or anything "
              "that holds a reflection. यथामुखं दर्शनो "
              "**यथामुखीनः**; सर्वस्य मुखस्य दर्शनः "
              "**सम्मुखीनः**.\\n\\n"
              "**निपातनात् सादृश्येऽव्ययीभावः** — and the "
              "अव्ययीभाव in the sense of LIKENESS is got from the "
              "laying-down, since 2.1.6's यथा compounds are for "
              "conformity and not resemblance"),
    Matup("5.2.7", gives="kha", pre="sarvādi",
          uttarapada="pathin-aṅga-karman-patra-pātra",
          sense="vyāpnoti", case="dvitīyā",
          why="तत्सर्वादेः पथ्यङ्गकर्मपत्रपात्रं व्याप्नोति. "
              "**तदिति द्वितीया समर्थविभक्तिः; व्याप्नोतीति "
              "प्रत्ययार्थः; परिशिष्टं प्रकृतिविशेषणम्** — the "
              "first word gives the case, the verb gives the sense, "
              "and everything left over describes the base. So: "
              "from a compound beginning with सर्व and ending in "
              "one of five words.\\n\\n"
              "सर्वपथं व्याप्नोति **सर्वपथीनो रथः**, a chariot that "
              "covers the whole road; **सर्वाङ्गीणस्तापः**, a fever "
              "through every limb; सर्वकर्मीणः पुरुषः; सर्वपत्रीणः "
              "सारथिः; **सर्वपात्रीण ओदनः**, rice enough to fill "
              "every dish"),
    Matup("5.2.8", gives="kha", of=("āprapada",), sense="prāpnoti",
          case="dvitīyā",
          why="आप्रपदं प्राप्नोति. **प्रपदमिति पादस्याग्रम् "
              "उच्यते; आङ् मर्यादायाम्; तयोरव्ययीभावः** — प्रपद is "
              "the front of the foot and आ marks the limit, and the "
              "two make an अव्ययीभाव. आप्रपदं प्राप्नोति "
              "**आप्रपदीनः पटः**, a cloth reaching the toes.\\n\\n"
              "**शरीरेणासंबद्धस्यापि पटस्य प्रमाणमाख्यायते** — and "
              "it states the cloth's MEASURE even when the cloth is "
              "not on a body at all"),
    Matup("5.2.9", gives="kha", of=("anupada",), sense="baddhā",
          case="dvitīyā",
          why="अनुपदसर्वान्नायानयं बद्धाभक्षयतिनेयेषु, "
              "**यथासंख्यम्**; the अनुपद member. **अनुरायामे "
              "सादृश्ये वा** — अनु of length or of likeness. "
              "अनुपदं बद्धा उपानत् **अनुपदीना**, a sandal bound to "
              "the foot, **पदप्रमाणा इत्यर्थः**, of the foot's "
              "measure"),
    Matup("5.2.9", gives="kha", of=("sarvānna",),
          sense="bhakṣayati", case="dvitīyā",
          why="अनुपदसर्वान्नायानयं बद्धाभक्षयतिनेयेषु, the "
              "सर्वान्न member. सर्वान्नानि भक्षयति "
              "**सर्वान्नीनो भिक्षुः**, a beggar who eats any food "
              "at all"),
    Matup("5.2.9", gives="kha", of=("ayānaya",), sense="neya",
          case="dvitīyā",
          why="अनुपदसर्वान्नायानयं बद्धाभक्षयतिनेयेषु, the "
              "अयानय member — and the word is from the board-game. "
              "**अयः प्रदक्षिणम्, अनयः प्रसव्यम्; "
              "प्रदक्षिणप्रसव्यगामिनां शाराणां यस्मिन् परशारैः "
              "पदानाम् असमावेशः सोऽयानयः**: अय is the rightward "
              "course and अनय the leftward, and the square where "
              "the opponent's pieces cannot come is the अयानय. "
              "अयानयं नेयः **अयानयीनः शारः**, "
              "**फलकशिरसि स्थित इत्यर्थः**, a piece standing at the "
              "head of the board"),
    Matup("5.2.10", gives="kha", of=("parovara",), adesa="parovara",
          sense="anubhavati", case="dvitīyā",
          why="परोवरपरम्परपुत्रपौत्रमनुभवति; the परोवर member, and "
              "the substitution comes with the affix. "
              "**परस्योत्वं प्रत्ययसंनियोगेन निपात्यते** — the उ "
              "of परस् is laid down as yoked to the affix. "
              "परांश्चावरांश्चानुभवति **परोवरीणः**, one who lives "
              "through high and low alike"),
    Matup("5.2.10", gives="kha", of=("parampara",),
          adesa="parampara", sense="anubhavati", case="dvitīyā",
          why="परोवरपरम्परपुत्रपौत्रमनुभवति, the परम्पर member. "
              "**परपरतराणां च परम्परभावो निपात्यते** — the shape "
              "परम्पर is laid down for परपरतर. परांश्च "
              "परतरांश्चानुभवति **परम्परीणः**.\\n\\n"
              "**परम्परशब्दो विनापि प्रत्ययेन दृश्यते** — and the "
              "word is seen without any affix, मन्त्रिपरम्परा मन्त्रं "
              "भिनत्ति, *a chain of ministers breaks a secret*. "
              "**तच्छब्दान्तरमेव द्रष्टव्यम्**: that is simply a "
              "different word"),
    Matup("5.2.10", gives="kha", of=("putrapautra",),
          sense="anubhavati", case="dvitīyā",
          why="परोवरपरम्परपुत्रपौत्रमनुभवति, the पुत्रपौत्र member "
              "— and the only one of the three that needs no "
              "laying-down. पुत्रपौत्राननुभवति **पुत्रपौत्रीणः**"),
    Matup("5.2.11", gives="kha", of=("avārapāra", "atyanta",
                                     "anukāma"),
          sense="gāmī", case="dvitīyā",
          why="अवारपारात्यन्तानुकामं गामी. **गमिष्यतीति गामी**, "
              "3.3.3 भविष्यति गम्यादयः — the participle is future, "
              "and 2.3.70 अकेनोर्भविष्यदाधमर्ण्ययोः forbids the "
              "genitive with it, which is why the base stands in "
              "the accusative.\\n\\n"
              "अवारपारं गामी **अवारपारीणः**, one who will cross "
              "from this bank to the far one. **विगृहीतादपीष्यते** "
              "— and from the members separately too: अवारीणः, "
              "पारीणः; **विपरीताच्च**, and reversed: पारावारीणः. "
              "अत्यन्तं गामी **अत्यन्तीनः**, **भृशं गन्ता**; "
              "अनुकामं गामी **अनुकामीनः**, **यथेष्टं गन्ता**"),
    Matup("5.2.12", gives="kha", of=("samāṃsamā",),
          sense="vijāyate", case="dvitīyā",
          why="समांसमां विजायते. **समांसमामिति वीप्सा**, a "
              "distributive doubling, and **सुबन्तसमुदायः "
              "प्रकृतिः** — the base is a bundle of inflected "
              "words. **गर्भधारणेन सकलापि समा व्याप्यत इति "
              "अत्यन्तसंयोगे द्वितीया** (2.1.29): the whole year is "
              "occupied by the carrying, so the accusative of "
              "unbroken connection. समांसमां विजायते **समांसमीना "
              "गौः**, a cow that calves every year.\\n\\n"
              "**पूर्वपदे सुपोऽलुग् वक्तव्यः** — the case-ending of "
              "the first member is not dropped. And a second "
              "reading: **केचित् तु समायांसमायां विजायत इति "
              "विगृह्णन्ति, गर्भविमोचने तु विजनिर्वर्तत इत्याहुः** "
              "— some read a locative and take विजनि of the "
              "delivery rather than the carrying"),
    Matup("5.2.13", nipatana=True, of=("adyaśvīna",),
          sense="avaṣṭabdha",
          why="अद्यश्वीनावष्टब्धे. **अद्यश्वीन इति निपात्यते** — a "
              "form laid down, and laid down "
              "for something imminent. **आसन्ने प्रसवे**: अद्य वा "
              "श्वो वा विजायते **अद्यश्वीना गौः**, a cow that will "
              "calve today or tomorrow.\\n\\n"
              "**आविदूर्ये हि मूर्धन्यो विधीयते** — 8.3.68 "
              "अवाच्चालम्बनाविदूर्ययोः gives the cerebral only in "
              "the sense of nearness, so the ष of अवष्टब्ध is "
              "itself evidence of what the rule means.\\n\\n"
              "**केचित् तु विजायत इति नानुवर्तयन्ति, "
              "अवष्टब्धमात्रे निपातनमित्याहुः** — and some do not "
              "carry the calving down, taking the form for anything "
              "imminent at all: **अद्यश्वीनं मरणम्**, a death "
              "expected today or tomorrow"),
    Matup("5.2.14", nipatana=True, gives="kha", of=("go",),
          pre="āṅ", sense="karmakārin",
          why="आगवीनः — a laid-down form, and the whole of a "
              "contract in one word. **गोराङ्पूर्वाद् आ तस्य गोः "
              "प्रतिदानात् कर्मकारिणि खः प्रत्ययो निपात्यते**: "
              "**आगवीनः कर्मकरः**, **यो गवा भृतः कर्म करोति आ "
              "तस्य गोः प्रत्यर्पणात्** — a hired man who works for "
              "a cow, UNTIL THE COW IS HANDED OVER. The आ of the "
              "compound is the term of the hire"),
    Matup("5.2.15", gives="kha", of=("anugu",), sense="alaṃgāmī",
          why="अनुग्वलंगामी. **गोः पश्चाद् अनुगु** — अनुगु is "
              "*behind the cattle*. अनुगु पर्याप्तं गच्छति "
              "**अनुगवीनो गोपालकः**, a herdsman equal to following "
              "them"),
    Matup("5.2.16", gives="yat", also_gives=("kha",),
          of=("adhvan",), sense="alaṃgāmī", case="dvitīyā",
          why="अध्वनो यत्खौ. अध्वानमलंगामी **अध्वन्यः, "
              "अध्वनीनः** — one equal to the road. 6.4.168 "
              "ये चाभावकर्मणोः and 6.4.169 आत्माध्वानौ खे keep the "
              "stem unchanged before each of the two"),
    Matup("5.2.17", gives="cha", also_gives=("yat", "kha"),
          of=("abhyamitra",), sense="alaṃgāmī", case="dvitīyā",
          excepts=("5.2.16",),
          why="अभ्यमित्राच्छ च — and the च keeps both affixes of "
              "the rule before, so three stand: अभ्यमित्रमलंगामी "
              "**अभ्यमित्रीयः, अभ्यमित्र्यः, अभ्यमित्रीणः**, "
              "**अमित्राभिमुखं सुष्ठु गच्छतीत्यर्थः** — one who "
              "goes well against the enemy"),
    Matup("5.2.18", gives="khañ", of=("goṣṭha",), sense="svārtha",
          result="bhūtapūrva",
          why="गोष्ठात् खञ् भूतपूर्वे — and the affix changes "
              "nothing but the shape. **गावस्तिष्ठन्त्यस्मिन्निति "
              "गोष्ठम्**; **गोष्ठशब्देन सन्निहितगोसमूहो देश "
              "उच्यते**, the word means the place with the cattle "
              "standing in it. **भूतपूर्वग्रहणं तस्यैव "
              "विशेषणम्**: and *formerly* qualifies THAT — गोष्ठो "
              "भूतपूर्वो **गौष्ठीनो देशः**, a place that used to be "
              "a cow-pen. **भूतपूर्वग्रहणं किम्?** गोष्ठो वर्तते",
          keeps_out="गोष्ठो वर्तते"),
    Matup("5.2.19", gives="khañ", of=("aśva",), sense="ekāhagama",
          case="ṣaṣṭhī",
          why="अश्वस्यैकाहगमः. **निर्देशादेव समर्थविभक्तिः**, and "
              "**एकाहेन गम्यत इत्येकाहगमः**. अश्वस्यैकाहगमोऽध्वा "
              "**आश्वीनः** — a day's ride, measured as a distance. "
              "**आश्वीनानि** शतं पतित्वा (तां०ब्रा० २१.१.९)"),
    Matup("5.2.20", nipatana=True, gives="khañ", of=("śālīna",),
          sense="adhṛṣṭa",
          why="शालीनकौपीने अधृष्टाकार्ययोः, **यथासंख्यम्**; the "
              "शालीन member. **अधृष्टोऽप्रगल्भः** — bashful. "
              "**शालाप्रवेशनमर्हति इति खञ् प्रत्यय उत्तरपदलोपश्च "
              "निपात्यते**: *one who deserves to go indoors*, with "
              "the affix and the loss of the compound's second "
              "member both laid down. **शालीनो जडः**.\\n\\n"
              "**शालीनकौपीने अधृष्टाकार्ययोः पर्यायौ यथाकथंचिद् "
              "व्युत्पादयितव्यौ** — the two are simply synonyms of "
              "*bashful* and *not to be done*, and are to be "
              "derived somehow or other. The vṛtti's own warning "
              "against reading the analysis too hard"),
    Matup("5.2.20", nipatana=True, gives="khañ", of=("kaupīna",),
          sense="akārya",
          why="शालीनकौपीने अधृष्टाकार्ययोः, the कौपीन member. "
              "**अकार्यम् अकरणार्हं विरुद्धम्** — what ought not to "
              "be done. कूपावतारमर्हति, *deserving to be thrown "
              "down a well*: **कौपीनं पापम्**"),
    Matup("5.2.21", gives="khañ", of=("vrāta",), sense="jīvati",
          case="tṛtīyā",
          why="व्रातेन जीवति. **निर्देशादेव तृतीया "
              "समर्थविभक्तिः**, and the vṛtti has to say what a "
              "व्रात is: **नानाजातीया अनियतवृत्तय उत्सेधजीविनः "
              "संघा व्राताः** — troops of mixed birth and no "
              "settled livelihood who live by their bodies, "
              "**उत्सेधः शरीरम्, तदायास्य ये जीवन्ति**. तेन "
              "व्रातेन जीवति **व्रातीनः**.\\n\\n"
              "**तेषामेव व्रातानाम् अन्यतम उच्यते; यस्त्वन्यस् "
              "तदीयेन जीवति, तत्र नेष्यते** — and it means one OF "
              "the troop, not an outsider living off their work",
          keeps_out="one who lives off another's व्रात"),
    Matup("5.2.22", nipatana=True, of=("sāptapadīna",),
          result="sakhya",
          why="साप्तपदीनं सख्यम्. **निपात्यते** — a laid-down form for "
              "FRIENDSHIP. **सप्तभिः पदैरवाप्यते साप्तपदीनम्**, "
              "won in seven steps: **सख्यं जनाः साप्तपदीनम् "
              "आहुः**.\\n\\n"
              "**कथं साप्तपदीनः सखा?** How then can the word be "
              "used of the FRIEND? **यदा गुणप्रधानः "
              "साप्तपदीनशब्दः सखिभावे तत्कर्मणि च वर्तते, तदा "
              "सख्यशब्देन सामानाधिकरण्यं भवति; यदा तु लक्षणया "
              "वर्तते, तदा पुरुषेण** — when it stands for the state "
              "it agrees with the word for friendship, and when it "
              "is used figuratively it agrees with the person"),
    Matup("5.2.23", nipatana=True, gives="khañ", of=("hyogodoha",),
          adesa="hiyaṅgu", result="saṃjñā",
          why="हैयङ्गवीनं संज्ञायाम्. **निपात्यते** — laid down, with a "
              "substitution inside it. **ह्योगोदोहस्य "
              "हियङ्ग्वादेशः, तस्य विकारे खञ् प्रत्ययो भवति "
              "संज्ञायाम्**: what is made from YESTERDAY'S MILKING "
              "— **ह्योगोदोहस्य विकारो हैयङ्गवीनम्**, and it is "
              "**घृतस्य संज्ञा**, a name for clarified butter. "
              "**तेनेह न भवति — ह्योगोदोहस्य विकार उदश्वित्**, and "
              "so not of buttermilk, which is also made from it",
          keeps_out="ह्योगोदोहस्य विकार उदश्वित्"),
    Matup("5.2.24", gives="kuṇap", gana="pīlvādi", sense="pāka",
          case="ṣaṣṭhī",
          why="तस्य पाकमूले पील्वादिकर्णादिभ्यः कुणब्जाहचौ, "
              "**यथासंख्यम्**; the पील्वादि half, in the sense of "
              "RIPENING. पीलूनां पाकः **पीलुकुणः**; कर्कन्धुकुणः. "
              "पीलु, कर्कन्धु, शमी, करीर, कुवल, बदर, अश्वत्थ, "
              "खदिर — पील्वादिः"),
    Matup("5.2.24", gives="jāhac", gana="karṇādi", sense="mūla",
          case="ṣaṣṭhī",
          why="तस्य पाकमूले पील्वादिकर्णादिभ्यः कुणब्जाहचौ, the "
              "कर्णादि half, in the sense of the ROOT of a thing. "
              "कर्णस्य मूलं **कर्णजाहम्**. कर्ण, अक्षि, नख, मुख, "
              "मख, केश, पाद, गुल्फ, भ्रूभङ्ग, दन्त, ओष्ठ, पृष्ठ, "
              "अङ्गुष्ठ — कर्णादिः"),
    Matup("5.2.25", gives="ti", of=("pakṣa",), sense="mūla",
          case="ṣaṣṭhī", excepts=("5.2.24",),
          why="पक्षात् तिः. **मूलग्रहणम् अनुवर्तते, न "
              "पाकग्रहणम्** — the ROOT carries down and the "
              "ripening does not, though the rule before stated "
              "them in one breath: "
              "**एकयोगनिर्दिष्टानाम् अप्येकदेशोऽनुवर्तते**, even "
              "of things named in a single rule a PART may carry "
              "on alone. पक्षस्य मूलं **पक्षतिः प्रतिपत्**"),
    Matup("5.2.26", gives="cuñcup", also_gives=("caṇap",),
          sense="vitta", case="tṛtīyā",
          why="तेन वित्तश्चुञ्चुप्चणपौ. **वित्तः प्रतीतो ज्ञातः** "
              "— known, famous BY something. विद्यया वित्तो "
              "**विद्याचुञ्चुः, विद्याचणः**, famous for learning"),
    Matup("5.2.27", gives="nā", of=("vi",), sense="svārtha",
          result="asaha",
          why="विनञ्भ्यां नानाञौ नसह, **यथासंख्यम्**; the वि "
              "member. **न सहेति प्रकृतिविशेषणम्** — the words "
              "must be standing for SEPARATION and not for "
              "togetherness. **विना**"),
    Matup("5.2.27", gives="nāñ", of=("nañ",), sense="svārtha",
          result="asaha",
          why="विनञ्भ्यां नानाञौ नसह, the नञ् member. **नाना** — "
              "and both affixes are स्वार्थे, changing nothing but "
              "the shape of an indeclinable"),
    Matup("5.2.28", gives="śālac", also_gives=("śaṅkaṭac",),
          of=("vi",), sense="svārtha",
          why="वेः शालच्छङ्कटचौ. **ससाधनक्रियावचनाद् उपसर्गात् "
              "स्वार्थे प्रत्ययौ भवतः** — from a preverb standing "
              "for an action together with its means. विगते शृङ्गे "
              "**विशाले, विशङ्कटे**, of a beast whose horns are "
              "gone, **तद्योगाद् गौरपि विशालो विशङ्कट इत्युच्यते**, "
              "and by association the animal itself.\\n\\n"
              "**परमार्थतस्तु गुणशब्दा एते यथाकथंचिद् "
              "व्युत्पाद्यन्ते। नात्र प्रकृतिप्रत्ययार्थयोर् "
              "अभिनिवेशः** — but in truth these are quality-words "
              "and are derived somehow or other; there is no "
              "insisting here on a sense for the base and a sense "
              "for the affix. The same warning 5.1.59 gave of the "
              "numerals"),
    Matup("5.2.29", gives="kaṭac", of=("sam", "pra", "ud", "vi"),
          sense="svārtha",
          why="संप्रोदश्च कटच्. **चकाराद् वेश्च** — and the च "
              "brings वि in as a fourth. **संकटम्, प्रकटम्, "
              "उत्कटम्, विकटम्**.\n\n"
              "**AND THIS ONE SŪTRA CARRIES EIGHT VĀRTTIKAS, EACH "
              "GIVING AN AFFIX OF ITS OWN.** "
              "**कटच्प्रकरणेऽलाबूतिलोमाभङ्गाभ्यो रजस्युपसंख्यानम्** "
              "— the same affix for POLLEN: अलाबूकटम्, तिलकटम्. "
              "**गोष्ठादयः स्थानादिषु पशुनामादिभ्यः** — गोगोष्ठम्, "
              "महिषीगोष्ठम्. **संघाते कटज् वक्तव्यः** — a herd, "
              "अविकटम्. **विस्तारे पटज्** — a spread, अविपटम्. "
              "**द्वित्वे गोयुगच्** — a pair, उष्ट्रगोयुगम्. "
              "**प्रकृत्यर्थस्य षट्त्वे षड्गवच्** — a set of six, "
              "**हस्तिषड्गवम्**. **विकारे स्नेहे तैलच्** — an oil "
              "made from something, **एरण्डतैलम्**, and by that "
              "vārttika तैल is *sesame-oil* only by usage. "
              "**भवने क्षेत्र इक्ष्वादिभ्यः शाकटशाकिनौ** — "
              "इक्षुशाकटम्, and the sense is 5.2.1's over again"),
    Matup("5.2.30", gives="kuṭārac", also_gives=("kaṭac",),
          of=("ava",), sense="svārtha",
          why="अवात् कुटारच्च — **चकारात् कटच्**, so both. "
              "**अवकुटारम्, अवकटम्**"),
    Matup("5.2.31", gives="ṭīṭac", also_gives=("nāṭac", "bhraṭac"),
          of=("ava",), sense="nata", result="saṃjñā",
          of_samjna="nāsikā",
          why="नते नासिकायाः संज्ञायां टीटञ्नाटज्भ्रटचः — three "
              "affixes for one preverb, and the sense is a FLAT "
              "NOSE. **नमनं नतम्**. नासिकाया नतम् **अवटीटम्, "
              "अवनाटम्, अवभ्रटम्**.\n\n"
              "**तद्योगाद् नासिकापि, पुरुषोऽपि तथोच्यते** — and by "
              "association the nose is called that, and so is the "
              "man: **अवटीटः, अवनाटः, अवभ्रटः**"),
    Matup("5.2.32", gives="biḍac", also_gives=("birīsac",),
          of=("ni",), sense="nata", result="saṃjñā",
          of_samjna="nāsikā",
          why="नेर्बिडज्बिरीसचौ. **नते नासिकाया इत्यनुवर्तते, "
              "संज्ञायामिति च**. **निबिडम्, निबिरीसम्**, and by "
              "association निबिडः, निबिरीसः.\n\n"
              "**कथं निबिडाः केशाः, निबिडं वस्त्रम्?** How then is "
              "hair called निबिड, or cloth? **उपमानाद् भविष्यति** "
              "— by comparison, and not by this rule"),
    Matup("5.2.33", gives="inac", also_gives=("piṭac", "ka"),
          of=("ni",), adesa="cika-ci", sense="nata",
          result="saṃjñā", of_samjna="nāsikā",
          why="इनच्पिटच्चिकचि च — and the affixes come with "
              "substitutions matched to them. **तत्संनियोगेन च "
              "निशब्दस्य यथासंख्यं चिक चि इत्येतावादेशौ भवतः**: "
              "**चिकिनः, चिपिटः**.\n\n"
              "**ककारः प्रत्ययो वक्तव्यश्चिक् च प्रकृत्यादेशः** — "
              "a vārttika adds a third, क with चिक्: **चिक्कः**, "
              "and the Mahābhāṣya states the whole set: "
              "**इनच्पिटच्काश्चिकचिचिकादेशाश्च**.\n\n"
              "**क्लिन्नस्य चिल्पिल्लश्चास्य चक्षुषी** — and a "
              "further vārttika for RUNNING EYES: क्लिन्ने अस्य "
              "चक्षुषी **चिल्लः, पिल्लः**, and **चुलादेशो "
              "वक्तव्यः**, चुल्लः. And a correction: "
              "**अस्येत्यनेन नार्थः; चक्षुषोरेवाभिधाने प्रत्यय "
              "इष्यते** — the *of him* is not wanted, the affix "
              "being for naming the EYES themselves: क्लिन्ने "
              "चक्षुषी **चिल्ले**; **तद्योगात् तु पुरुषस् "
              "तथोच्यते**"),
    Matup("5.2.34", gives="tyakan", of=("upa",), sense="āsanna",
          result="saṃjñā",
          why="उपाधिभ्यां त्यकन्नासन्नारूढयोः, **यथासंख्यम्**; the "
              "उप member. पर्वतस्यासन्नम् **उपत्यका**, the land at "
              "a mountain's foot.\n\n"
              "**संज्ञाधिकाराच्च नियतविषयमासन्नारूढं गम्यते** — "
              "the naming-heading makes the *near* and the *risen* "
              "definite things and not any nearness at all. And it "
              "does one more job: **प्रत्ययस्थात् कात् पूर्वस्य "
              "इति इत्वमत्र न भवति, संज्ञाधिकारादेव** (7.3.44), "
              "the आ before the क is not shortened, and it is the "
              "naming-heading that stops it"),
    Matup("5.2.34", gives="tyakan", of=("adhi",), sense="ārūḍha",
          result="saṃjñā",
          why="उपाधिभ्यां त्यकन्नासन्नारूढयोः, the अधि member. "
              "पर्वतस्यैवारूढम् **अधित्यका**, the tableland above"),
    Matup("5.2.35", gives="aṭhac", of=("karman",), sense="ghaṭa",
          case="saptamī",
          why="कर्मणि घटोऽठच्. **निर्देशादेव समर्थविभक्तिः**, and "
              "**घटत इति घटः** — one who exerts himself. कर्मणि "
              "घटते **कर्मठः पुरुषः**, a man who throws himself "
              "into the work"),
    Matup("5.2.36", gives="itac", gana="tārakādi",
          sense="saṃjāta", case="prathamā",
          why="तदस्य संजातं तारकादिभ्य इतच्. **संजातग्रहणं "
              "प्रकृतिविशेषणम्** — *come to be* describes the "
              "BASE. तारकाः संजाता अस्य नभसः **तारकितं नभः**, a "
              "sky that has come to have stars; **पुष्पितो "
              "वृक्षः**, a tree come into flower.\n\n"
              "तारका, पुष्प, मुकुल, कण्टक, पिपासा, सुख, दुःख, "
              "ऋजीष, कुड्मल, रोग, विचार, व्याधि, निष्क्रमण, "
              "किसलय, कुसुम, तन्द्रा, वेग, श्रद्धा, उत्कण्ठा, "
              "**गर्भादप्राणिनि** (ग०सू०१२३) — "
              "**तारकादिराकृतिगणः**, an open list"),
    Matup("5.2.37", gives="dvayasac",
          also_gives=("daghnac", "mātrac"), sense="pramāṇa",
          case="prathamā",
          why="प्रमाणे द्वयसज्दघ्नञ्मात्रचः — three affixes for "
              "the MEASURE of a thing. ऊरुः प्रमाणमस्य "
              "**ऊरुद्वयसम्, ऊरुदघ्नम्, ऊरुमात्रम्**; जानुद्वयसम्, "
              "जानुदघ्नम्, जानुमात्रम्.\n\n"
              "**AND A KĀRIKĀ DIVIDES THEM.**\n\n"
              "    प्रथमश्च द्वितीयश्च ऊर्ध्वमाने मतौ मम ।\n\n"
              "The first two are for HEIGHT — ऊरुद्वयसमुदकम्, "
              "water thigh-deep — and **मात्रच् पुनरविशेषेण "
              "प्रस्थमात्रमित्यपि भवति**, the third for measure of "
              "any kind.\n\n"
              "**प्रमाणे लो वक्तव्यः** — after a word that is "
              "ITSELF a measure-word the affix drops: शमः "
              "प्रमाणमस्य **शमः**; दिष्टिः, वितस्तिः. "
              "**द्विगोर्नित्यम्**, and after a numeral compound "
              "always: **द्विशमः**. **नित्यग्रहणं किम्?** so that "
              "the elision holds even where a doubt-affix would "
              "come: द्वे दिष्टी स्यातां वा न वा **द्विदिष्टिः**. "
              "**डट् स्तोमे**: पञ्चदशः स्तोमः. "
              "**प्रमाणपरिमाणाभ्यां संख्यायाश्चापि संशये मात्रज्**: "
              "शममात्रम्, **दशमात्रा गावः**, about ten cows"),
    Matup("5.2.38", gives="aṇ",
          also_gives=("dvayasac", "daghnac", "mātrac"),
          of=("puruṣa", "hastin"), sense="pramāṇa",
          case="prathamā", excepts=("5.2.37",),
          why="पुरुषहस्तिभ्यामण् च — and the च keeps all three of "
              "the rule before, so four forms apiece. पुरुषः "
              "प्रमाणमस्य **पौरुषम्**, पुरुषद्वयसम्, पुरुषदघ्नम्, "
              "पुरुषमात्रम्; **हास्तिनम्**, हस्तिद्वयसम्.\n\n"
              "**द्विगोर्नित्यं लुक्** — after a numeral compound "
              "the affix always drops: **द्विपुरुषमुदकम्**, water "
              "two men deep; द्विहस्ति, and in the feminine "
              "द्विपुरुषी, द्विहस्तिनी"),
    Matup("5.2.39", gives="vatup", of=("yad", "tad", "etad"),
          sense="parimāṇa", case="prathamā",
          why="यत्तदेतेभ्यः परिमाणे वतुप्. यत् परिमाणमस्य "
              "**यावान्**; तावान्, एतावान्.\n\n"
              "**AND परिमाण IS SAID THOUGH प्रमाण IS ALREADY "
              "RUNNING**, because the two are different things, and "
              "a kārikā gives the reason:\n\n"
              "    डावतावर्थवैशेष्यान् निर्देशः पृथगुच्यते ।\n"
              "    मात्राद्यप्रतिघाताय भावः सिद्धश्च डावतोः ॥\n\n"
              "**वतुप्प्रकरणे युष्मदस्मद्भ्यां छन्दसि सादृश्य "
              "उपसंख्यानम्** — and in the Veda the same affix for "
              "LIKENESS after the pronouns: न **त्वावाँ** अन्यो "
              "दिव्यो न पार्थिवः (ऋ० ७.३२.२३); यज्ञं विप्रस्य "
              "**मावतः** (ऋ० १.१४२.२), **त्वत्सदृशस्य "
              "मत्सदृशस्येत्यर्थः**"),
    Matup("5.2.40", gives="vatup", of=("kim", "idam"), adesa="gha",
          sense="parimāṇa", case="prathamā",
          why="किमिदंभ्यां वो घः — a substitution, and the vṛtti "
              "reads the affix out of it. **एतदेव चादेशविधानं "
              "ज्ञापकं किमिदंभ्यां वतुप् प्रत्ययो भवतीति**: that a "
              "substitute is enjoined for the व of वतुप् after "
              "these two TELLS you the affix comes after them at "
              "all, which no rule had said. **कियान्, इयान्**. "
              "**अथ वा योगविभागेन वतुपं विधाय पश्चाद् वो घो "
              "विधीयते** — or else the rule is split in two"),
    Matup("5.2.41", gives="ḍati", also_gives=("vatup",),
          of=("kim",), adesa="gha", sense="saṃkhyā-parimāṇa",
          case="prathamā",
          why="किमः संख्यापरिमाणे डति च. **संख्यायाः परिमाणं "
              "संख्यापरिच्छेद इत्यर्थः** — the measuring OF a "
              "number, that is, its being determined. का संख्या "
              "परिमाणमेषाम् **कति ब्राह्मणाः**, and by the च with "
              "the substitution, **कियन्तो ब्राह्मणाः**.\n\n"
              "**AND WHY संख्या IS QUALIFIED BY परिमाण AT ALL**, "
              "since a number is a determining thing already: "
              "**यत्रापरिच्छेदकत्वेन विवक्ष्यते तत्र मा भूदिति; "
              "क्षेपे हि परिच्छेदो नास्ति** — where a number is "
              "used in CONTEMPT nothing is being determined, "
              "**केयमेषां संख्या दशानाम्**, *what sort of number "
              "is this, ten?*",
          keeps_out="केयमेषां संख्या दशानाम्"),
    Matup("5.2.42", gives="tayap", of_samjna="saṃkhyā",
          sense="avayava", case="prathamā",
          why="संख्याया अवयवे तयप्. **अवयवा अवयविनः संबन्धिन इति "
              "सामर्थ्याद् अवयवी प्रत्ययार्थो विज्ञायते** — parts "
              "belong to a WHOLE, so what the affix reports is the "
              "whole and not the parts. पञ्च अवयवा अस्य "
              "**पञ्चतयम्**; दशतयम्, चतुष्टयम्, चतुष्टयी"),
    Matup("5.2.43", gives="ayaj", of=("dvi", "tri"), adesa="ayaj",
          optional=True, of_samjna="saṃkhyā", sense="avayava",
          case="prathamā", excepts=("5.2.42",),
          why="द्वित्रिभ्यां तयस्यायज् वा — and it replaces the "
              "affix rather than adding one. **द्वयम्, "
              "द्वितयम्**; त्रयम्, त्रितयम्.\n\n"
              "**AND THE RULE NAMES THE AFFIX IT REPLACES FOR A "
              "REASON.** **तयग्रहणं स्थानिनिर्देशार्थम्; अन्यथा "
              "प्रत्ययान्तरमयज् विज्ञायेत। तत्र को दोषः?** — if "
              "अयज् were a separate affix instead of a substitute, "
              "then **त्रयी गतिरिति तयनिबन्धन ईकारो न स्यात्**, "
              "the feminine ई that hangs on तय would not come, and "
              "1.1.33 प्रथमचरमतया… would not apply either. A "
              "substitution keeps what the original was entitled to"),
    Matup("5.2.44", gives="ayaj", of=("ubha",), adesa="ayaj",
          of_samjna="saṃkhyā", sense="avayava", case="prathamā",
          excepts=("5.2.42",),
          why="उभादुदात्तो नित्यम् — the same substitute, but "
              "obligatory and accented. **वचनसामर्थ्याद् आदेर् "
              "उदात्तत्वं विज्ञायते** — the force of the statement "
              "shows the accent is on the FIRST syllable. "
              "**उभयो मणिः**; उ॒भये॑ऽस्य देवमनु॒ष्याः.\n\n"
              "**उभशब्दो यदि लौकिकी संख्या, ततः पूर्वेणैव विहितस्य "
              "तयप आदेशविधानार्थं वचनम्; अथ न संख्या, ततो "
              "योगविभागेन तयपं विधाय** — and whether the rule adds "
              "a substitute or first supplies the affix too depends "
              "on whether उभ counts as a numeral at all"),
    Matup("5.2.45", gives="ḍa", uttarapada="daśan", sense="adhika",
          case="prathamā",
          why="तदस्मिन्नधिकमिति दशान्ताड् डः — and every word of "
              "it is tested. एकादश अधिका अस्मिन् शते **एकादशं "
              "शतम्**, a hundred and eleven.\n\n"
              "**दशान्तादिति किम्?** पञ्चाधिका अस्मिन् शते. "
              "**अन्तग्रहणं किम्?** दशाधिका अस्मिन् शते. And two "
              "restrictions the rule does not state: "
              "**प्रत्ययार्थेन च समानजातीये प्रकृत्यर्थे सति "
              "प्रत्यय इष्यते** — the excess must be of the SAME "
              "KIND, so एकादश माषा अधिका अस्मिन् कार्षापणशते takes "
              "nothing; and **शतसहस्रयोश्चेष्यते**, only of a "
              "hundred or a thousand, so not एकादशाधिका अस्यां "
              "त्रिंशति. Both are got from the word इति: "
              "**इतिकरणो विवक्षार्थ इत्युक्तम्, तत इदं सर्वं "
              "लभ्यते**. A kārikā sums it:\n\n"
              "    अधिके समानजाताविष्टं शतसहस्रयोः ।\n"
              "    यस्य संख्या तदाधिक्ये डः कर्तव्यो मतो मम ॥",
          keeps_out="एकादश माषा अधिका अस्मिन् कार्षापणशते"),
    Matup("5.2.46", gives="ḍa", stem_final="śad-viṃśati",
          sense="adhika", case="prathamā",
          why="शदन्तविंशतेश्च. त्रिंशदधिका अस्मिञ् छते **त्रिंशं "
              "शतम्**; विंशं शतम्.\n\n"
              "**शद्ग्रहणेऽन्तग्रहणं प्रत्ययग्रहणे यस्मात् स "
              "तदादेः अधिकार्थम्** — the word *ending in* is there "
              "so that a compound ENDING in शद् is reached: "
              "**एकत्रिंशं शतम्**, एकचत्वारिंशं शतम्. And "
              "**तदन्तादपीति वक्तव्यम्** does the same for विंशति: "
              "एकविंशं शतम्.\n\n"
              "**संख्याग्रहणं च कर्तव्यम्** — twice, and both "
              "times to keep out a compound that merely ends in the "
              "sound: **इह मा भूद् — गोत्रिंशदधिका अस्मिन् गोशते**",
          keeps_out="गोत्रिंशदधिका अस्मिन् गोशते"),
    Matup("5.2.47", gives="mayaṭ", of_samjna="saṃkhyā",
          sense="guṇa-nimāna", case="prathamā",
          why="संख्याया गुणस्य निमाने मयट्. **गुणो भागः; निमानं "
              "मूल्यम्** — a part, and a price. यवानां द्वौ भागौ "
              "निमानमस्योदश्विद्भागस्य **द्विमयमुदश्विद् यवानाम्**, "
              "buttermilk worth two parts of barley.\n\n"
              "**भागेऽपि तु विधीयमानः प्रत्ययः प्राधान्येन "
              "भागवन्तमाचष्टे** — though given for the part, the "
              "affix names what HAS the part, which is why the "
              "words agree.\n\n"
              "Four conditions, none of them in the sūtra. "
              "**गुणस्येति चैकत्वं विवक्षितम्** — one kind of part "
              "only, so not द्वौ भागौ यवानां त्रय उदश्वितः. "
              "**भूयसश्च वाचिकायाः संख्यायाः प्रत्यय इष्यते** — a "
              "number greater than one, so not एको भागो निमानमस्य, "
              "**बहुत्वमतन्त्रम्**, though two is enough. "
              "**गुणशब्दः समानावयववचनः** — the parts must be "
              "EQUAL, so not अध्यर्ध उदश्वित्. **निमेये चापि "
              "दृश्यते** — and the affix is seen for the thing "
              "PRICED as well: **द्विमया यवा उदश्वितः**. "
              "**निमान इति किम्?** द्विगुणं पच्यते तैलं क्षीरेण",
          keeps_out="एको भागो निमानमस्य, द्विगुणं पच्यते तैलम्"),
    Matup("5.2.48", gives="ḍaṭ", of_samjna="saṃkhyā",
          sense="pūraṇa", case="ṣaṣṭhī",
          why="तस्य पूरणे डट् — the ORDINALS. **पूर्यतेऽनेनेति "
              "पूरणम्; येन संख्या संख्यानं पूर्यते संपद्यते, स "
              "तस्याः पूरणः** — what fills a count out. एकादशानां "
              "पूरण **एकादशः**; त्रयोदशः.\n\n"
              "**यस्मिन्नुपसंजाते अन्या संख्या संपद्यते, स "
              "प्रत्ययार्थः** — what the affix reports is that on "
              "whose arrival a NEW number comes about. So "
              "**इह न भवति — पञ्चानां मुष्टिकानां पूरणो घटः**: a "
              "pot that five handfuls fill is not a *fifth*",
          keeps_out="पञ्चानां मुष्टिकानां पूरणो घटः"),
    Matup("5.2.49", gives="ḍaṭ", stem_final="n", adesa="maṭ",
          of_samjna="saṃkhyā", sense="pūraṇa", case="ṣaṣṭhī",
          excepts=("5.2.48",),
          why="नान्तादसंख्यादेर्मट् — an आगम on the affix the rule "
              "before gave, after a numeral ending in न् that does "
              "not begin with a numeral. **पञ्चानां पूरणः "
              "पञ्चमः**; सप्तमः.\n\n"
              "**नान्तादिति पञ्चमी डट आगमसंबन्धे षष्ठीं "
              "प्रकल्पयति** — the ablative in the rule creates the "
              "genitive that an आगम needs, since an augment belongs "
              "TO something. **नान्तादिति किम्?** विंशतेः पूरणो "
              "**विंशः**. **असंख्यादेरिति किम्?** एकादशानां पूरण "
              "**एकादशः**",
          keeps_out="विंशः, एकादशः"),
    Matup("5.2.50", gives="ḍaṭ", also_gives=("ḍaṭ",),
          stem_final="n", adesa="thaṭ", of_samjna="saṃkhyā",
          sense="pūraṇa", case="ṣaṣṭhī", usage="chandasi",
          excepts=("5.2.49",),
          why="थट् च छन्दसि — a second augment for the same affix "
              "in the Veda, **चकारात् पक्षे मडपि भवति**, the मट् "
              "of the rule before standing in the other half. "
              "पर्णम॑यानि **पञ्चथा॑नि** भवन्ति (काठ०सं० ८.२); "
              "सप्तथः॑. And the मट् too: **पञ्चम॑म्** "
              "इन्द्रिय॑स्या॑पाक्रामत्"),
    Matup("5.2.51", gives="ḍaṭ", of=("ṣaṣ", "kati", "katipaya",
                                     "catur"),
          adesa="thuk", of_samjna="saṃkhyā", sense="pūraṇa",
          case="ṣaṣṭhī", excepts=("5.2.49",),
          why="षट्कतिकतिपयचतुरां थुक् — an augment for four named "
              "words. षण्णां पूरणः **षष्ठः**; कतिथः, कतिपयथः, "
              "**चतुर्थः**.\n\n"
              "**AND ONE OF THE FOUR IS NOT A NUMERAL AT ALL.** "
              "**कतिपयशब्दो न संख्या, तस्यास्मादेव ज्ञापकाद् डट् "
              "प्रत्ययो विज्ञायते** — 5.2.48 gives the ordinal "
              "affix after a NUMERAL, and कतिपय is none; that this "
              "rule adds an augment to it is the evidence that it "
              "gets the affix at all. The same reading a "
              "substitution gave at 5.2.40.\n\n"
              "**चतुरश्छयतावाद्यक्षरलोपश्च** — a vārttika gives "
              "चतुर् two more affixes with the loss of its first "
              "syllable: **तुरीयः, तुर्यः**"),
    Matup("5.2.52", gives="ḍaṭ",
          of=("bahu", "pūga", "gaṇa", "saṃgha"), adesa="tithuk",
          sense="pūraṇa", case="ṣaṣṭhī", excepts=("5.2.49",),
          why="बहुपूगगणसंघस्य तिथुक्. बहूनां पूरणो **बहुतिथः**; "
              "पूगतिथः, गणतिथः, संघतिथः.\n\n"
              "**पूगसंघशब्दयोरसंख्यात्वाद् इदमेव ज्ञापकं डटो "
              "भावस्य** — and the same reading a second time: "
              "पूग and संघ are not numerals either, so this rule "
              "is what tells you they take the ordinal affix"),
    Matup("5.2.53", gives="ḍaṭ", stem_final="vatu", adesa="ithuk",
          of_samjna="saṃkhyā", sense="pūraṇa", case="ṣaṣṭhī",
          excepts=("5.2.49",),
          why="वतोरिथुक्. **वत्वन्तस्य संख्यात्वात् पूर्वेण डड् "
              "विहितः, तस्मिन्नयमागमो विधीयते** — a word in वतु is "
              "a numeral already, so 5.2.48 gave it the affix and "
              "this only adds the augment. **यावतिथः, तावतिथः, "
              "एतावतिथः**"),
    Matup("5.2.54", gives="tīya", of=("dvi",), of_samjna="saṃkhyā",
          sense="pūraṇa", case="ṣaṣṭhī", excepts=("5.2.48",),
          why="द्वेस्तीयः, डटोऽपवादः. द्वयोः पूरणो **द्वितीयः**"),
    Matup("5.2.55", gives="tīya", of=("tri",), adesa="saṃprasāraṇa",
          of_samjna="saṃkhyā", sense="pūraṇa", case="ṣaṣṭhī",
          excepts=("5.2.48",),
          why="त्रेः संप्रसारणं च, डटोऽपवादः — the same affix and "
              "a vowel-substitution yoked to it, "
              "**तत्सन्नियोगेन**. त्रयाणां पूरणः **तृतीयः**.\n\n"
              "And two rules that would have applied do not: "
              "**हलः इति संप्रसारणस्य दीर्घत्वं न भवति** (6.4.2), "
              "the substituted vowel is not lengthened; and the "
              "अण् of 6.3.111 is carried into that rule from "
              "ढ्रलोपे…, **पूर्वेण च णकारेणाण्ग्रहणम्**"),
    Matup("5.2.56", gives="ḍaṭ", gana="viṃśatyādi", adesa="tamaṭ",
          optional=True, of_samjna="saṃkhyā", sense="pūraṇa",
          case="ṣaṣṭhī", excepts=("5.2.48",),
          why="विंशत्यादिभ्यस्तमडन्यतरस्याम् — an optional augment, "
              "so both forms stand. विंशतेः पूरणो **विंशतितमः, "
              "विंशः**; एकविंशतितमः, एकविंशः; त्रिंशत्तमः, "
              "त्रिंशः.\n\n"
              "**AND THE LIST IS THE ORDINARY NUMBER-WORDS AND NOT "
              "THE ONES 5.1.59 LAID DOWN.** **विंशत्यादयो लौकिकाः "
              "संख्याशब्दा गृह्यन्ते, न पङ्क्त्यादिसूत्रसंनिविष्टाः; "
              "तद्ग्रहणे ह्येकविंशतिप्रभृतिभ्यो न स्यात्, "
              "ग्रहणवता प्रातिपदिकेन तदन्तविधिप्रतिषेधात्** — if "
              "the sūtra's own words were meant, a rule naming them "
              "could not reach compounds ending in them, and "
              "एकविंशति would be left out. **एवं च सति "
              "षष्ट्यादेश्चासंख्यादेः इति पर्युदासो युज्यत एव**"),
    Matup("5.2.57", gives="ḍaṭ", gana="śatādi", adesa="tamaṭ",
          of_samjna="saṃkhyā", sense="pūraṇa", case="ṣaṣṭhī",
          excepts=("5.2.56",),
          why="नित्यं शतादिमासार्धमाससंवत्सराच्च — and here the "
              "augment is obligatory. शतस्य पूरणः **शततमः**; "
              "सहस्रतमः, लक्षतमः; **मासतमो दिवसः**, अर्धमासतमः, "
              "संवत्सरतमः.\n\n"
              "**मासादयः संख्याशब्दा न भवन्ति, तेभ्योऽस्मादेव "
              "ज्ञापकाद् डट् प्रत्ययो विज्ञायते** — a third time "
              "the same reading: month and fortnight and year are "
              "not numerals, and this rule is the evidence that "
              "they take the ordinal affix.\n\n"
              "**षष्ट्यादेश्चासंख्यादेः इति वक्ष्यमाणेन सिद्धे "
              "शतादिग्रहणं संख्याद्यर्थम्** — 5.2.58 would cover "
              "शत anyway, so naming it here is for the compounds "
              "that BEGIN with a numeral: **एकशततमः, द्विशततमः**"),
    Matup("5.2.58", gives="ḍaṭ", gana="ṣaṣṭyādi", adesa="tamaṭ",
          of_samjna="saṃkhyā", sense="pūraṇa", case="ṣaṣṭhī",
          excepts=("5.2.56",),
          why="षष्ट्यादेश्चासंख्यादेः. **विंशत्यादिभ्यः इति "
              "विकल्पेन प्राप्ते नित्यार्थम्** — 5.2.56 made it "
              "optional and this makes it fixed. **षष्टितमः, "
              "सप्ततितमः**. **असंख्यादेरिति किम्?** एकषष्टः, "
              "एकषष्टितमः — where a numeral stands first the "
              "choice comes back",
          keeps_out="एकषष्टः"),
    Matup("5.2.59", gives="cha", sense="matvartha",
          result="sūkta-sāman",
          why="मतौ छः सूक्तसाम्नोः. **मताविति मत्वर्थ उच्यते** — "
              "*having it*, and the whole relation is got from that "
              "one word: **मत्वर्थग्रहणेन समर्थविभक्तिः, "
              "प्रकृतिविशेषणं प्रत्ययार्थ इति सर्वम् आक्षिप्यते**. "
              "अच्छावाकशब्दोऽस्मिन्निति **अच्छावाकीयं सूक्तम्**; "
              "**यज्ञायज्ञीयं साम**.\n\n"
              "**अनुकरणशब्दाश्च स्वरूपमात्रप्रधानाः प्रत्ययम् "
              "उत्पादयन्ति; तेनानेकपदादपि सिद्धम्** — a quoted "
              "string counts as one word for this, so the affix "
              "comes after a whole phrase: **अस्यवामीयम्**, "
              "**कयाशुभीयम्**, hymns named from their first words"),
    Matup("5.2.60", gives="cha", sense="matvartha",
          result="adhyāya-anuvāka", optional=True,
          excepts=("5.2.59",),
          why="अध्यायानुवाकयोर्लुक् — the affix removed where the "
              "thing named is a CHAPTER or a section.\n\n"
              "**केन पुनरध्यायानुवाकयोः प्रत्ययः? इदमेव लुग्वचनं "
              "ज्ञापकं तद्विधानस्य** — and by what rule did they "
              "have the affix at all? By this one: that its removal "
              "is enjoined is the evidence that it was given. The "
              "reading a fourth time in twenty sūtras.\n\n"
              "**विकल्पेन च लुगयमिष्यते** — and the removal is "
              "optional, so **गर्दभाण्डोऽध्यायः** stands beside "
              "गर्दभाण्डीयः"),
    Matup("5.2.61", gives="aṇ", gana="vimuktādi",
          sense="matvartha", result="adhyāya-anuvāka",
          excepts=("5.2.59",),
          why="विमुक्तादिभ्योऽण्. विमुक्तशब्दोऽस्मिन्नस्ति "
              "**वैमुक्तोऽध्यायोऽनुवाको वा**; दैवासुरः. विमुक्त, "
              "देवासुर, वसुमत्, सत्वत्, उपसत्, हविर्धान, मित्री, "
              "सोमापूषन्, अग्नाविष्णु, वृत्रहति, इडा, रक्षोसुर, "
              "सदसत्, वसु, मरुत्वत्, पत्नीवत्, दशार्ह, वयस्, "
              "पतत्रि, सोम, हेतु — विमुक्तादिः"),
    Matup("5.2.62", gives="vun", gana="goṣadādi",
          sense="matvartha", result="adhyāya-anuvāka",
          excepts=("5.2.59",),
          why="गोषदादिभ्यो वुन्. **गोषदकोऽध्यायोऽनुवाको वा**; "
              "इषेत्वकः, मातरिश्वकः. गोषद, इषेत्वा, मातरिश्वन्, "
              "देवस्यत्वा, देवीरापः, कृष्णोस्याखरेष्टः, "
              "दैवींधियम्, रक्षोहण, अञ्जन, प्रभूत, प्रतूर्त, "
              "कृशानु — गोषदादिः, and most of them are the opening "
              "words of what they name"),
    Matup("5.2.63", gives="vun", of=("pathin",), sense="kuśala",
          case="saptamī",
          why="तत्र कुशलः पथः. पथि कुशलः **पथकः**, one who knows "
              "the road"),
    Matup("5.2.64", gives="kan", gana="ākarṣādi", sense="kuśala",
          case="saptamī", excepts=("5.2.63",),
          why="आकर्षादिभ्यः कन्. आकर्षे कुशल **आकर्षकः**; "
              "त्सरुकः. आकर्ष, त्सरु, पिपासा, पिचण्ड, अशनि, "
              "अश्मन्, विचय, चय, जय, आचय, अय, नय, निपाद, गद्गद, "
              "दीप, ह्रद, ह्लाद, शकुनि — आकर्षादिः"),
    Matup("5.2.65", gives="kan", of=("dhana", "hiraṇya"),
          sense="kāma", case="saptamī",
          why="धनहिरण्यात् कामे. **काम इच्छा अभिलाषः**. धने कामो "
              "**धनको देवदत्तस्य**; हिरण्यको देवदत्तस्य"),
    Matup("5.2.66", gives="kan", of_samjna="svāṅga",
          sense="prasita", case="saptamī",
          why="स्वाङ्गेभ्यः प्रसिते. **प्रसितः प्रसक्तस्तत्पर "
              "इत्यर्थः** — taken up with, intent on. केशेषु "
              "प्रसितः **केशकः**, **केशादिरचनायां प्रसक्त एवम् "
              "उच्यते**, one always at his hair.\n\n"
              "**बहुवचनं स्वाङ्गसमुदायशब्दादपि यथा स्यात्** — the "
              "plural in the rule lets a compound of several limbs "
              "in: **दन्तौष्ठकः, केशनखकः**"),
    Matup("5.2.67", gives="ṭhak", of=("udara",), sense="prasita",
          case="saptamī", result="ādyūna", excepts=("5.2.66",),
          why="उदराट् ठगाद्यूने. **आद्यून इति "
              "प्रत्ययार्थविशेषणम्; उदरेऽविजिगीषुर्भण्यते; यो "
              "बुभुक्षयात्यन्तं पीड्यते, स एवमुच्यते** — one who "
              "cannot master his belly, tormented by hunger. उदरे "
              "प्रसित **औदरिक आद्यूनः**. **आद्यून इति किम्?** "
              "उदरकः — for anyone else merely intent on his "
              "stomach, the affix of the rule before",
          keeps_out="उदरकः"),
    Matup("5.2.68", gives="kan", of=("sasya",), sense="parijāta",
          case="tṛtīyā",
          why="सस्येन परिजातः. **कन् प्रत्यय इत्येव स्वर्यते, न "
              "ठक्** — the कन् of 5.2.64 carries down and the ठक् "
              "of the rule just before does not. **सस्यशब्दोऽयं "
              "गुणवाची; परिः सर्वतो भावे वर्तते; यो गुणैः "
              "संबद्धो जायते, यस्य किंचिदपि वैगुण्यं नास्ति** — "
              "born with every quality and no flaw anywhere: "
              "**सस्यकः शालिः**, सस्यकः साधुः, सस्यको मणिः, "
              "**आकरशुद्ध इत्यर्थः**, flawless from the mine"),
    Matup("5.2.69", gives="kan", of=("aṃśa",), sense="hārin",
          case="dvitīyā",
          why="अंशं हारी. अंशं हारी **अंशको दायादः**, an heir with "
              "a share coming. **हारीत्यावश्यके णिनिः** (3.3.170), "
              "and **तत्र षष्ठीप्रतिषेधात् कर्मणि द्वितीयैव "
              "भवति** — the genitive being forbidden with that "
              "participle, the object stands in the accusative"),
    Matup("5.2.70", gives="kan", of=("tantra",),
          sense="acirāpahṛta", case="pañcamī",
          why="तन्त्रादचिरापहृते. **अचिरापहृतः स्तोककालापहृत "
              "इत्यर्थः** — taken off a short time ago. "
              "तन्त्रादचिरापहृतः **तन्त्रकः पटः**, cloth fresh "
              "from the loom, **प्रत्यग्रो नव उच्यते**"),
    Matup("5.2.71", nipatana=True, gives="kan",
          of=("brāhmaṇaka", "uṣṇika"), result="saṃjñā",
          why="ब्राह्मणकोष्णिके संज्ञायाम्. **निपात्येते** — two "
              "forms laid down "
              "with that affix, as NAMES. **ब्राह्मणको देशः**, "
              "**यत्रायुधजीविनो ब्राह्मणाः सन्ति**, a country where "
              "the brahmins live by arms; **उष्णिका यवागूः**, "
              "**अल्पान्ना यवागूः**, a thin gruel"),
    Matup("5.2.72", gives="kan", of=("śīta", "uṣṇa"),
          sense="kārin", case="dvitīyā",
          why="शीतोष्णाभ्यां कारिणि. **क्रियाविशेषणाद् "
              "द्वितीयासमर्थादयं प्रत्ययः** — the base is an "
              "adverb standing in the accusative. शीतं करोति "
              "**शीतकः**, **अलसो जड उच्यते**, a sluggard; उष्णं "
              "करोति **उष्णकः**, **शीघ्रकारी दक्ष उच्यते**, a "
              "quick worker. Cold and hot for slow and brisk"),
    Matup("5.2.73", nipatana=True, gives="ka", of=("adhyārūḍha",),
          sense="adhika",
          why="अधिकम्. **अधिकमिति निपात्यते.** **अध्यारूढशब्दस्योत्तरपदलोपः "
              "कंश्च प्रत्ययः**, the second member dropped and क "
              "given. **अधिको द्रोणः खार्याम्; अधिका खारी "
              "द्रोणेन** — and it works both ways, "
              "**कर्तरि कर्मणि चाध्यारूढशब्दः**"),
    Matup("5.2.74", nipatana=True, gives="kan",
          of=("anu", "abhi"), sense="kamitṛ",
          why="अनुकाभिकाभीकः कमिता. **निपात्यन्ते** — three forms "
              "laid down for one "
              "who DESIRES. **अभेः पक्षे दीर्घत्वं च निपात्यते** — "
              "and the lengthening of अभि in one of them is laid "
              "down too. अनुकामयत **अनुकः**; **अभिकः, अभीकः**"),
    Matup("5.2.75", gives="kan", of=("pārśva",), sense="anvicchati",
          case="tṛtīyā",
          why="पार्श्वेनान्विच्छति. **अनृजुरुपायः पार्श्वम्** — "
              "पार्श्व is a crooked means. तेनार्थान् अन्विच्छति "
              "**पार्श्वकः**, **मायावी कौसृतिको जालिक उच्यते**, a "
              "trickster"),
    Matup("5.2.76", gives="ṭhak", of=("ayaḥśūla",),
          sense="anvicchati", case="tṛtīyā", excepts=("5.2.75",),
          why="अयःशूलदण्डाजिनाभ्यां ठक्ठञौ, **यथासंख्यम्**; the "
              "अयःशूल member. **तीक्ष्ण उपायोऽयःशूलम् उच्यते** — "
              "an iron-spike is a harsh means. तेनान्विच्छति "
              "**आयःशूलिकः**, **साहसिक इत्यर्थः**, a man of "
              "violence"),
    Matup("5.2.76", gives="ṭhañ", of=("daṇḍājina",),
          sense="anvicchati", case="tṛtīyā", excepts=("5.2.75",),
          why="अयःशूलदण्डाजिनाभ्यां ठक्ठञौ, the दण्डाजिन member. "
              "**दम्भो दण्डाजिनम्** — staff-and-deerskin is "
              "hypocrisy. तेनान्विच्छति **दाण्डाजिनिकः**, "
              "**दाम्भिक इत्यर्थः**"),
    Matup("5.2.77", gives="kan", of_samjna="pūraṇānta",
          sense="svārtha", result="grahaṇa", optional=True,
          why="तावतिथं ग्रहणमिति लुग् वा. **तावतां पूरणं "
              "तावतिथम्; गृह्यतेऽनेनेति ग्रहणम्** — from a word "
              "already made by an ORDINAL affix, in its own sense, "
              "with that affix optionally removed. द्वितीयेन रूपेण "
              "ग्रन्थं गृह्णाति **द्विकं ग्रहणम्, द्वितीयकम्**; "
              "त्रिकम्, तृतीयकम्.\n\n"
              "**तावतिथेन गृह्णातीति कन् वक्तव्यः, "
              "पूरणप्रत्ययस्य च नित्यं लुक्** — and a vārttika "
              "gives the same affix for the READER rather than the "
              "reading, with the removal obligatory: षष्ठेन रूपेण "
              "ग्रन्थं गृह्णाति **षट्को देवदत्तः**.\n\n"
              "**इतिकरणो विवक्षार्थः; तेन ग्रन्थविषयमेव ग्रहणं "
              "विज्ञायते, नान्यविषयम्** — the इति confines the "
              "*taking* to taking in a TEXT"),
    Matup("5.2.78", gives="kan", sense="grāmaṇī", case="prathamā",
          why="स एषां ग्रामणीः. **ग्रामणीः प्रधानो मुख्य "
              "इत्यर्थः** — the chief of them. देवदत्तो ग्रामणीरेषां "
              "**देवदत्तकाः**; यज्ञदत्तकाः. **ग्रामणीरिति किम्?** "
              "देवदत्तः शत्रुरेषाम् — a leader and not merely "
              "someone they all have in common",
          keeps_out="देवदत्तः शत्रुरेषाम्"),
    Matup("5.2.79", gives="kan", of=("śṛṅkhala",), sense="bandhana",
          case="prathamā", result="karabha",
          why="शृङ्खलमस्य बन्धनं करभे — and both the tether and the "
              "thing tethered are named. **उष्ट्राणां बालकाः "
              "करभाः** — करभ is a camel calf; **तेषां काष्ठमयं "
              "पाशकं पादे व्यतिषज्यते, तदुच्यते शृङ्खलम्**, and "
              "शृङ्खल is the wooden hobble put on its foot. "
              "शृङ्खलं बन्धनमस्य करभस्य **शृङ्खलकः**.\n\n"
              "**यद्यपि रज्ज्वादिकमपि तत्रास्ति तथापि शृङ्खलमस्य "
              "अस्वतन्त्रीकरणे भवति साधनमिति बन्धनमित्युच्यते** — "
              "there is a rope on it too, and the hobble is called "
              "the BOND because it is what takes the animal's "
              "freedom away"),
    Matup("5.2.80", nipatana=True, gives="kan", of=("ud",),
          sense="unmanas",
          why="उत्क उन्मनाः — **उत्क इति निपात्यते**. **उद्गतं "
              "मनो यस्य स उन्मनाः** — one whose mind has gone up "
              "and out. **उच्छब्दात् ससाधनक्रियावचनात् तद्वति कन् "
              "प्रत्ययो निपात्यते**: **उत्को देवदत्तः**; उत्कः "
              "प्रवासी, **उत्सुक इत्यर्थः**, a man away from home "
              "and longing"),
    Matup("5.2.81", gives="kan", sense="roga",
          why="कालप्रयोजनाद् रोगे — from a word for a TIME or for a "
              "CAUSE, of a disease. **अर्थलभ्या समर्थविभक्तिः** — "
              "the case is got from the sense, each as it fits. "
              "**कालो दिवसादिः; प्रयोजनं कारणं रोगस्य फलं वा**.\n\n"
              "द्वितीयेऽह्नि भवो **द्वितीयको ज्वरः**, a fever of "
              "the second day; **चतुर्थकः**, a quartan. And from a "
              "cause: विषपुष्पैर्जनितो **विषपुष्पको ज्वरः**; "
              "उष्णं कार्यमस्य **उष्णको ज्वरः**.\n\n"
              "**उत्तरसूत्राद् इह संज्ञाग्रहणम् अपकृष्यते; "
              "तेनायं प्रकारनियमः सर्वो लभ्यते** — and the "
              "*naming* is pulled BACKWARD from the next rule, "
              "which is what makes all these settled names of "
              "particular fevers"),
    Matup("5.2.82", gives="kan", sense="anna", case="prathamā",
          result="prāya-saṃjñā",
          why="तदस्मिन्नन्नं प्राये संज्ञायाम्. **प्रायो "
              "बाहुल्यम्** — mostly. गुडापूपाः प्रायेणान्नमस्यां "
              "पौर्णमास्यां **गुडापूपिका**, a full-moon day whose "
              "food is chiefly cakes in molasses; तिलापूपिका. "
              "**संज्ञाग्रहणं तदन्तोपाधिः**. "
              "**वटकेभ्य इनिर्वक्तव्यः** — and a different affix "
              "for one of them: **वटकिनी पौर्णमासी**"),
    Matup("5.2.83", gives="añ", of=("kulmāṣa",), sense="anna",
          case="prathamā", result="prāya-saṃjñā",
          excepts=("5.2.82",),
          why="कुल्माषादञ्. **ञकारो वृद्धिस्वरार्थः** — the ञ is "
              "for the strengthening and the accent. कुल्माषाः "
              "प्रायेणान्नमस्यां **कौल्माषी पौर्णमासी**"),
    Matup("5.2.84", nipatana=True, gives="ghan",
          of=("chandas",), sense="adhīta",
          why="श्रोत्रियंश्छन्दोऽधीते — **श्रोत्रियन्निति "
              "निपात्यते**, and the whole SENTENCE is what the "
              "form stands for: **श्रोत्रियंश्छन्दोऽधीत इति "
              "वाक्यार्थे पदवचनम्**, one word for *he has learnt "
              "the Veda*. **नकारः स्वरार्थः**. "
              "**श्रोत्रियो ब्राह्मणः**.\n\n"
              "**छन्दसो वा श्रोत्रभावः, तदधीत इति घंश्च "
              "प्रत्ययः** — or else छन्दस् becomes श्रोत्र and घन् "
              "is the affix. **कथं छन्दोऽधीते छान्दसः?** And how "
              "is the ordinary form छान्दसः explained? "
              "**वाग्रहणमनुवर्तते** — the *optionally* of 5.2.77 "
              "carries down, so this form is one of two"),
    Matup("5.2.85", gives="ini", also_gives=("ṭhan",),
          of=("śrāddha",), sense="anena", result="bhukta",
          why="श्राद्धमनेन भुक्तमिनिठनौ. **श्राद्धशब्दः "
              "कर्मनामधेयं तत्साधने द्रव्ये वर्तित्वा प्रत्ययम् "
              "उत्पादयति** — the word names the RITE and then, "
              "standing for the food of it, takes the affix. "
              "श्राद्धं भुक्तमनेन **श्राद्धी, श्राद्धिकः**.\n\n"
              "**इनिठनोः समानकालग्रहणम्; अद्य भुक्ते श्राद्धे "
              "श्वः श्राद्धिक इति प्रयोगो मा भूत्** — the eating "
              "and the naming must be of one time, so a man who ate "
              "at a śrāddha today is not called that tomorrow"),
    Matup("5.2.86", gives="ini", of=("pūrva",), sense="anena",
          why="पूर्वादिनिः. **अनेनेति प्रत्ययार्थः कर्ता "
              "अनुवर्तते; न च क्रियामन्तरेण कर्ता संभवतीति यां "
              "कांचित् क्रियामध्याहृत्य प्रत्ययो विधेयः** — the "
              "affix reports an AGENT, and an agent needs an "
              "action, so some action or other has to be supplied. "
              "पूर्वं गतमनेन भुक्तं पीतं वा **पूर्वी**, one who "
              "went, or ate, or drank before"),
    Matup("5.2.87", gives="ini", uttarapada="pūrva",
          sense="anena", excepts=("5.2.86",),
          why="सपूर्वाच्च — from a stem ENDING in that word with "
              "something before it. पूर्वं कृतमनेन **कृतपूर्वी "
              "कटम्**, one who has made a mat before; भुक्तपूर्वी "
              "ओदनम्. **सुप्सुपेति समासं कृत्वा तद्धित "
              "उत्पाद्यते** (2.1.4).\n\n"
              "**AND THE TWO RULES TOGETHER TEACH TWO "
              "PARIBHĀṢĀS.** **योगद्वयेन चानेन पूर्वादिनिः "
              "सपूर्वाच्चेति परिभाषाद्वयं ज्ञाप्यते** — that 5.2.87 "
              "is needed at all shows "
              "**व्यपदेशिवद्भावोऽप्रातिपदिकेन** and "
              "**ग्रहणवता प्रातिपदिकेन तदन्तविधिर्नास्ति**, that a "
              "rule naming a word does not reach compounds ending "
              "in it. Two general principles read out of one rule "
              "being split in two"),
    Matup("5.2.88", gives="ini", gana="iṣṭādi", sense="anena",
          why="इष्टादिभ्यश्च. **इष्टी यज्ञे**, one who has "
              "sacrificed; **पूर्ती श्राद्धे**. "
              "**क्तस्येन्विषयस्य कर्मणि इति सप्तम्युपसंख्यायते** "
              "(वा० २.३.३६) — and a supplement gives the locative "
              "for the object.\n\n"
              "इष्ट, पूर्त, उपसादित, निगदित, संकलित, निपठित, "
              "संकल्पित, अर्चित, पूजित, परिगणित, आम्नात, श्रुत, "
              "अधीत, आसेवित, निराकृत, उपकृत, अनुयुक्त, निगृहीत — "
              "इष्टादिः, and every one of them is a past participle"),
    Matup("5.2.89", nipatana=True,
          of=("paripanthin", "paripariṇ"), sense="paryavasthātṛ",
          usage="chandasi",
          why="छन्दसि परिपन्थिपरिपरिणौ पर्यवस्थातरि. "
              "**निपात्येते** — two forms "
              "laid down for the Veda. **पर्यवस्थाता प्रतिपक्षः "
              "सपत्न उच्यते** — one who stands in the way, an "
              "adversary. मा त्वा॑ **परिप॒रिणो॑** विद॒न् मा त्वा॑ "
              "**परिप॒न्थिनो॑** विद॒न् (मा०सं० ४.३४)"),
    Matup("5.2.90", nipatana=True, of=("anupadī",),
          sense="anveṣṭṛ",
          why="अनुपद्यन्वेष्टा — **अनुपदीति निपात्यते**. "
              "**पदस्य पश्चादनुपदम्** — on the track of. "
              "**अनुपदी गवाम्**, one who follows cattle to find "
              "them; अनुपदी उष्ट्राणाम्"),
    Matup("5.2.91", gives="ini", of=("sākṣāt",), sense="draṣṭṛ",
          result="saṃjñā",
          why="साक्षाद् द्रष्टरि संज्ञायाम्. **साक्षाच्छब्दो "
              "ऽव्ययम्** — an indeclinable, and the affix comes "
              "after it. साक्षाद् द्रष्टा **साक्षी**, a witness.\n\n"
              "**संज्ञाग्रहणमभिधेयनियमार्थम्; संज्ञाग्रहणाद् "
              "उपद्रष्टैवोच्यते, न दाता ग्रहीता वा** — the naming "
              "confines it to the ONLOOKER, so a man who gives "
              "evidence or takes it is not called by the word"),
    Matup("5.2.92", nipatana=True, gives="ghac", of=("parakṣetra",),
          sense="cikitsya", case="saptamī",
          why="क्षेत्रियच् परक्षेत्रे चिकित्स्यः. "
              "**क्षेत्रियजिति निपात्यते**, "
              "**परशब्दलोपश्च**, and the vṛtti offers FOUR "
              "readings and accepts them all.\n\n"
              "**परक्षेत्रं जन्मान्तरशरीरम्, तत्र चिकित्स्यः "
              "क्षेत्रियः** — a disease curable only in another "
              "birth's body, that is, incurable: **नामृतस्य "
              "निवर्तत इत्यर्थः**. Or **क्षेत्रियं विषम्, यत् "
              "परक्षेत्रे परशरीरे संक्रमय्य चिकित्स्यते**, a poison "
              "treated by moving it into another body. Or "
              "**क्षेत्रियाणि तृणानि, यानि सस्यार्थे क्षेत्रे "
              "जातानि चिकित्स्यानि नाशयितव्यानि**, weeds in a "
              "cornfield, *treated* by being destroyed. Or "
              "**क्षेत्रियः पारदारिकः; परदाराः परक्षेत्रम्, तत्र "
              "चिकित्स्यो निग्रहीतव्यः**, an adulterer, *treated* "
              "by being punished.\n\n"
              "**सर्वं चैतत् प्रमाणम्** — and all of it is "
              "authoritative. The third place in these two pādas "
              "where the Kāśikā declines to choose"),
    Matup("5.2.93", nipatana=True, gives="ghac", of=("indra",),
          sense="indriya",
          why="इन्द्रियमिन्द्रलिङ्गमिन्द्रदृष्टमिन्द्रसृष्टम् "
              "इन्द्रजुष्टमिन्द्रदत्तमिति वा — six derivations for "
              "one word, and the rule ends by saying it does not "
              "matter which. **इन्द्रियमित्यन्तोदात्तं शब्दरूपं "
              "निपात्यते; रूढिरेषा चक्षुरादीनां करणानाम्; तथा च "
              "व्युत्पत्तेरनियमं दर्शयति** — the word is the "
              "settled name of the eye and the other instruments, "
              "and the rule SHOWS that its derivation is not "
              "fixed.\n\n"
              "**इन्द्र आत्मा, स चक्षुरादिना करणेनानुमीयते; "
              "नाकर्तृकं करणमस्ति** — इन्द्र is the self, inferred "
              "from the instruments, since no instrument is without "
              "an agent. So: the self's MARK, or what the self "
              "SEES by, or SENDS FORTH, or RESORTS TO, or GIVES to "
              "the objects **यथायथं ग्रहणाय**.\n\n"
              "**इतिकरणः प्रकारार्थः; सति संभवे व्युत्पत्तिर् "
              "अन्यथापि कर्तव्या, रूढेरनियमादिति। वाशब्दः "
              "प्रत्येकमभिसंबध्यमानो विकल्पानां स्वातन्त्र्यं "
              "दर्शयति** — the इति means *and so on*, so other "
              "derivations may be made where they will serve, and "
              "the वा goes with each severally, so no one of the "
              "six depends on another"),
    Matup("5.2.94", gives="matup", sense="asti", case="prathamā",
          heading=True,
          why="तदस्यास्त्यस्मिन्निति मतुप् — the rule by which "
              "Sanskrit says a thing HAS something, and the one "
              "this module is named for. **तदिति प्रथमा "
              "समर्थविभक्तिः; अस्यास्मिन्निति प्रत्ययार्थौ; "
              "अस्तीति प्रकृतिविशेषणम्; इतिकरणो विवक्षार्थः**. "
              "गावोऽस्य सन्ति **गोमान् देवदत्तः**; वृक्षा "
              "अस्मिन् सन्ति **वृक्षवान् पर्वतः**.\n\n"
              "**AND THE इति FIXES WHEN IT MAY BE SAID AT ALL.** "
              "**इतिकरणाद् विषयनियमः**, and a kārikā names the "
              "seven grounds:\n\n"
              "    भूमनिन्दाप्रशंसासु नित्ययोगेऽतिशायने ।\n"
              "    संसर्गेऽस्तिविवक्षायां भवन्ति मतुबादयः ॥\n\n"
              "ABUNDANCE — **गोमान्**. BLAME — **कुष्ठी**. PRAISE "
              "— **रूपवती कन्या**. CONSTANT CONNECTION — "
              "**क्षीरिणो वृक्षाः**. EXCESS — **उदरिणी कन्या**. "
              "CONTACT — **दण्डी, छत्री**. And the bare wish to say "
              "*it is there* — **अस्तिमान्**. Seven, and mere "
              "possession is not among them.\n\n"
              "**गुणवचनेभ्यो मतुपो लुग् वक्तव्यः** — and after a "
              "quality-word the affix drops: शुक्लो गुणोऽस्यास्ति "
              "**शुक्लः पटः**"),
    Matup("5.2.95", gives="matup", gana="rasādi", sense="asti",
          case="prathamā",
          why="रसादिभ्यश्च. **रसवान्, रूपवान्**.\n\n"
              "**किमर्थमिदमुच्यते, न पूर्वसूत्रेणैव मतुप् "
              "सिद्धः?** Why is it said, when 5.2.94 gives मतुप् "
              "already? **रसादिभ्यः पुनर्वचनम् अन्यनिवृत्त्यर्थम्; "
              "अन्ये मत्वर्थीया मा भूवन्** — to shut the OTHER "
              "possessive affixes out, so that only मतुप् comes "
              "after these. **कथं रूपिणी कन्या, रूपिको दारकः? "
              "प्रायिकमेतद् वचनम्** — and those forms stand because "
              "the restriction holds for the most part.\n\n"
              "**गुणग्रहणं रसादीनां विशेषणम्** — and the list is "
              "of QUALITIES: रस, रूप, गन्ध, स्पर्श, शब्द, स्नेह, "
              "**गुणात्** (ग०सू०१२४), **एकाचः** (ग०सू०१२५). "
              "**तेन ये रसनेन्द्रियादिग्राह्या गुणाः, तेषामेवायं "
              "पाठः** — only the qualities the senses take in"),
    Matup("5.2.96", gives="lac", also_gives=("matup",),
          of_samjna="prāṇyaṅga", stem_final="ā", sense="asti",
          case="prathamā", optional=True, excepts=("5.2.94",),
          why="प्राणिस्थादातो लजन्यतरस्याम् — from a word ending "
              "in आ that stands for something ON A LIVING BODY, "
              "optionally लच्, so the मतुप् stands beside it. "
              "**चूडालः, चूडावान्**; कर्णिकालः, कर्णिकावान्.\n\n"
              "**प्राणिस्थादिति किम्?** शिखावान् प्रदीपः — a lamp "
              "has a flame-crest and is not a living body. "
              "**आदिति किम्?** हस्तवान्, पादवान्. And "
              "**प्राण्यङ्गादिति वक्तव्यम्** narrows it further, "
              "**इह मा भूत् — चिकीर्षास्यास्ति चिकीर्षावान्**: a "
              "wish is IN a living thing but is not a LIMB of one",
          keeps_out="शिखावान् प्रदीपः, चिकीर्षावान्"),
    Matup("5.2.97", gives="lac", also_gives=("matup",),
          gana="sidhmādi", sense="asti", case="prathamā",
          optional=True, excepts=("5.2.94",),
          why="सिध्मादिभ्यश्च. **सिध्मलः, सिध्मवान्**; गडुलः, "
              "गडुमान्.\n\n"
              "**अन्यतरस्यांग्रहणेन मतुप् समुच्चीयते न तु "
              "प्रत्ययो विकल्प्यते; तस्माद् अकारान्तेभ्य इनिठनौ "
              "प्रत्ययौ न भवतः** — the *optionally* GATHERS मतुप् "
              "in rather than making the affix itself a choice, and "
              "the consequence is that इनि and ठन् do not come "
              "after these at all.\n\n"
              "सिध्म, गडु, मणि, नाभि, जीव, पांसु, सक्तु, हनु, "
              "मांस, परशु, **पार्ष्णिधमन्योर्दीर्घश्च** "
              "(ग०सू०१२६) — पार्ष्णीलः; पर्ण, उदक, प्रज्ञा, "
              "पार्श्व, गण्ड, ग्रन्थि, "
              "**वातदन्तबलललाटानामूङ् च** (ग०सू०१२७) — वातूलः, "
              "दन्तूलः; **जटाघटाकलाः क्षेपे** (ग०सू०१२८) — "
              "जटालः; कर्ण, स्नेह, शीत, श्याम, पित्त, पृथु, मृदु, "
              "कण्डु, **क्षुद्रजन्तूपतापाच्चेष्यते** (ग०सू०१२९) — "
              "यूकालः, मक्षिकालः, and for an affliction "
              "विचर्चिकालः, **मूर्छालः** — सिध्मादिः"),
    Matup("5.2.98", gives="lac", of=("vatsa",), sense="asti",
          result="kāmavat", excepts=("5.2.94",),
          why="वत्सांसाभ्यां कामबले, **यथासंख्यम्**; the वत्स "
              "member. **वत्सलः**, and it does not mean *having a "
              "calf*: **वृत्तिविषये वत्सांसशब्दौ स्वभावात् "
              "कामबलयोर्वर्तमानौ तद्वति प्रत्ययमुत्पादयतः; न "
              "ह्यत्र वत्सार्थोंऽसार्थो वा विद्यते** — inside the "
              "derivation the two words stand for AFFECTION and "
              "STRENGTH by their own nature, and the calf is not in "
              "it at all. **वत्सल इति स्नेहवानुच्यते — वत्सलः "
              "स्वामी, वत्सलः पिता**.\n\n"
              "**न चायमर्थो मतुपि संभवतीति नित्यं लजेव भवति** — "
              "and since मतुप् cannot carry that sense, the affix "
              "here is not one of two but the only one. "
              "**अन्यत्र वत्सवती गौः**, elsewhere the ordinary "
              "affix and the ordinary sense",
          keeps_out="वत्सवती गौः"),
    Matup("5.2.98", gives="lac", of=("aṃsa",), sense="asti",
          result="balavat", excepts=("5.2.94",),
          why="वत्सांसाभ्यां कामबले, the अंस member. "
              "**अंसल इति चोपचितमांसो बलवानुच्यते** — thick in the "
              "flesh, and so strong. **अन्यत्र अंसवान् दुर्बलः**, "
              "where the ordinary affix leaves a man with shoulders "
              "and no strength",
          keeps_out="अंसवान् दुर्बलः"),
    Matup("5.2.99", gives="ilac", also_gives=("lac", "matup"),
          of=("phena",), sense="asti", optional=True,
          excepts=("5.2.94",),
          why="फेनादिलच् च — **चकारात् लच् च**, and the "
              "अन्यतरस्याम् of 5.2.96 carries: "
              "**अन्यतरस्यांग्रहणं मतुप्समुच्चयार्थं सर्वत्रैव "
              "अनुवर्तते**, so मतुप् is gathered in through the "
              "whole stretch. **फेनिलः, फेनलः, फेनवान्**"),
    Matup("5.2.100", gives="śa", also_gives=("matup",),
          gana="lomādi", sense="asti", optional=True,
          excepts=("5.2.94",),
          why="लोमादिपामादिपिच्छादिभ्यः शनेलचः, **यथासंख्यम्**; "
              "the लोमादि member. **लोमशः, लोमवान्**. लोमन्, "
              "रोमन्, वल्गु, बभ्रु, हरि, कपि, शुनि, तरु — लोमादिः"),
    Matup("5.2.100", gives="na", also_gives=("matup",),
          gana="pāmādi", sense="asti", optional=True,
          excepts=("5.2.94",),
          why="लोमादिपामादिपिच्छादिभ्यः शनेलचः, the पामादि member. "
              "**पामनः, पामवान्**. पामन्, वामन्, हेमन्, श्लेष्मन्, "
              "कद्रु, बलि, श्रेष्ठ, पलल, सामन्, "
              "**अङ्गात् कल्याणे** (ग०सू०१३०), "
              "**शाकीपलालीदद्र्वां ह्रस्वत्वं च** (ग०सू०१३१), "
              "**विष्वगित्युत्तरपदलोपश्चाकृतसन्धेः** (ग०सू०१३२), "
              "**लक्ष्म्या अच्च** (ग०सू०१३३) — पामादिः, and four "
              "of the entries carry an operation of their own"),
    Matup("5.2.100", gives="ilac", also_gives=("matup",),
          gana="picchādi", sense="asti", optional=True,
          excepts=("5.2.94",),
          why="लोमादिपामादिपिच्छादिभ्यः शनेलचः, the पिच्छादि "
              "member. **पिच्छिलः, पिच्छवान्**; उरसिलः, उरस्वान्. "
              "पिच्छ, उरस्, ध्रुवका, क्षुवका, "
              "**जटाघटाकलाः क्षेपे** (ग०सू०१३४), वर्ण, उदक, पङ्क, "
              "प्रज्ञा — पिच्छादिः"),
    Matup("5.2.101", gives="ṇa", also_gives=("matup",),
          of=("prajñā", "śraddhā", "arcā", "vṛtti"), sense="asti",
          optional=True, excepts=("5.2.94",),
          why="प्रज्ञाश्रद्धार्चाभ्यो णः. **मतुप् सर्वत्र "
              "समुच्चीयते**. **प्राज्ञः, प्रज्ञावान्**; श्राद्धः, "
              "श्रद्धावान्; आर्चः, अर्चावान्; वार्त्तः, वृत्तिमान्"),
    Matup("5.2.102", gives="vini", of=("tapas",), sense="asti",
          excepts=("5.2.94",),
          why="तपःसहस्राभ्यां विनीनी, and NOT यथासंख्यम् — "
              "**प्रत्ययार्थयोस्तु यथासंख्यं सर्वत्रैवास्मिन् "
              "प्रकरणे नेष्यते**, the matching in order is not "
              "wanted anywhere in this section. तपोऽस्यास्मिन् वा "
              "विद्यते **तपस्वी**; सहस्री.\n\n"
              "**AND THE RULE IS NEEDLESS AND STATED ANYWAY.** "
              "**असन्तत्वाद् अदन्तत्वाच्च सिद्धे प्रत्यये "
              "पुनर्वचनम् अणा वक्ष्यमाणेन बाधा मा भूदिति** — तपस् "
              "would get विनि for ending in अस् and सहस्र would get "
              "इनि for ending in अ; the rule is stated so that the "
              "अण् of the NEXT sūtra does not displace them. "
              "**सहस्रात् तु ठनपि बाध्यते**"),
    Matup("5.2.102", gives="ini", of=("sahasra",), sense="asti",
          excepts=("5.2.94",),
          why="तपःसहस्राभ्यां विनीनी, the सहस्र half — and the two "
              "affixes are NOT matched to the two words in order, "
              "**यथासंख्यं सर्वत्रैवास्मिन् प्रकरणे नेष्यते**. "
              "**सहस्री**"),
    Matup("5.2.103", gives="aṇ", also_gives=("vini", "ini"),
          of=("tapas", "sahasra"), sense="asti",
          excepts=("5.2.94",),
          why="अण् च — and the split from the rule before is for "
              "two reasons at once: **योगविभाग उत्तरार्थो "
              "यथासंख्यार्थश्च**. **तापसः, साहस्रः**.\n\n"
              "**अण्प्रकरणे ज्योत्स्नादिभ्य उपसंख्यानम्** — and a "
              "vārttika adds a list: ज्योत्स्ना विद्यतेऽस्मिन् पक्षे "
              "**ज्यौत्स्नः पक्षः**, a fortnight that has "
              "moonlight; तामिस्रः, कौण्डलः, वैसर्पः, वैपादिकः"),
    Matup("5.2.104", gives="aṇ", of=("sikatā", "śarkarā"),
          sense="asti", excepts=("5.2.94",),
          why="सिकताशर्कराभ्यां च. **सैकतो घटः**, a sandy pot; "
              "**शार्करं मधु**, gritty honey. **अदेश इहोदाहरणम्; "
              "देशे तु लुबिलचौ भविष्यतः** — and the examples are "
              "deliberately not PLACES, since a place is the next "
              "rule's business"),
    Matup("5.2.105", gives="lup", also_gives=("ilac", "aṇ",
                                              "matup"),
          of=("sikatā", "śarkarā"), sense="asti", result="deśa",
          excepts=("5.2.104",),
          why="देशे लुबिलचौ च — where the thing meant is a PLACE, "
              "the affix is removed, or इलच् comes, **चकारादण् च, "
              "मतुप् च**. **कस्य पुनरयं लुप्? मतुबादीनाम् "
              "अन्यतमस्य, विशेषाभावात्** — and WHICH affix is "
              "removed? Any one of them, there being nothing to "
              "choose between.\n\n"
              "सिकता अस्मिन् विद्यन्ते **सिकता देशः, सिकतिलः, "
              "सैकतः, सिकतावान्** — four forms. **देश इति किम्?** "
              "सैकतो घटः",
          keeps_out="सैकतो घटः"),
    Matup("5.2.106", gives="urac", of=("danta",), sense="asti",
          result="unnata", excepts=("5.2.94",),
          why="दन्त उन्नत उरच्. **उन्नत इति प्रकृतिविशेषणम्** — "
              "*prominent* describes the teeth and not the man. "
              "दन्ता उन्नता अस्य सन्ति **दन्तुरः**, buck-toothed. "
              "**उन्नत इति किम्?** दन्तवान्",
          keeps_out="दन्तवान्"),
    Matup("5.2.107", gives="ra", of=("ūṣa", "suṣi", "muṣka",
                                     "madhu"),
          sense="asti", excepts=("5.2.94",),
          why="ऊषसुषिमुष्कमधो रः. **ऊषरं क्षेत्रम्**, saline "
              "ground; **सुषिरं काष्ठम्**, hollow wood; मुष्करः "
              "पशुः; **मधुरो गुडः**.\n\n"
              "**इतिकरणो विवक्षार्थः सर्वत्राभिधेयनियमं करोति** — "
              "5.2.94's इति confines what may be NAMED, throughout: "
              "**इह न भवति — ऊषोऽस्मिन् घटे विद्यते**, of salt in "
              "a pot rather than in the soil.\n\n"
              "**रप्रकरणे खमुखकुञ्जेभ्य उपसंख्यानम्** — खमस्यास्ति "
              "कण्ठविवरं महत् **खरः**; **मुखरः**; कुञ्जावस्य स्तः "
              "**कुञ्जरः**, an elephant, **हस्तिहनू कुञ्जशब्देन "
              "उच्येते**, कुञ्ज being its jaws. "
              "**नगपांसुपाण्डुभ्यश्चेति वक्तव्यम्** — **नगरम्**, "
              "पांसुरम्, पाण्डुरम्; **कच्छ्वा ह्रस्वत्वं च** — "
              "कच्छुरम्",
          keeps_out="ऊषोऽस्मिन् घटे विद्यते"),
    Matup("5.2.108", gives="ma", of=("dyu", "dru"), sense="asti",
          excepts=("5.2.94",),
          why="द्युद्रुभ्यां मः. **द्युमः, द्रुमः**. "
              "**रूढिशब्दावेतौ; रूढिषु मतुप् पुनर्न विकल्प्यते** — "
              "these are settled names, and where a word is a "
              "settled name the मतुप् is not offered beside it. So "
              "the gathering that runs through the rest of the "
              "stretch stops here"),
    Matup("5.2.109", gives="va", also_gives=("ini", "ṭhan",
                                             "matup"),
          of=("keśa",), sense="asti", optional=True,
          excepts=("5.2.94",),
          why="केशाद् वोऽन्यतरस्याम्. **ननु च प्रकृतम् "
              "अन्यतरस्यांग्रहणम् अनुवर्तत एव?** The word was "
              "already running — why say it? **मतुप्समुच्चयार्थं "
              "तदित्युक्तम्; अनेन त्विनिठनौ प्राप्येते; ततश्च "
              "आतूरूप्यं भवति**: the carried one gathers मतुप्, "
              "and THIS one lets इनि and ठन् in, so four forms "
              "stand — **केशवः, केशी, केशिकः, केशवान्**.\n\n"
              "**वप्रकरणेऽन्येभ्योऽपि दृश्यत इति वक्तव्यम्** — "
              "मणिवः, हिरण्यवः, **राजीवम्**; **अर्णसो लोपश्च**, "
              "अर्णवः. **छन्दसीवनिपौ च वक्तव्यौ**: "
              "सु॒म॒ङ्ग॒**लीरि॒यं** व॒धूः (ऋ० १०.८५.३३), and "
              "वनिप् — म॒**घवा॑नम्**ईमहे. "
              "**मेधारथाभ्यामिरन्निरचौ वक्तव्यौ** — **मेधि॑रः**, "
              "र॑थि॒रः"),
    Matup("5.2.110", gives="va", of=("gāṇḍī", "ajaga"),
          sense="asti", result="saṃjñā", excepts=("5.2.94",),
          why="गाण्ड्यजगात् संज्ञायाम्. **गाण्डीवं धनुः**, "
              "**अजगवं धनुः** — the two great bows.\n\n"
              "**ह्रस्वादपि भवति — गाण्डिवं धनुरिति; तत्र तुल्या "
              "हि संहिता दीर्घह्रस्वयोः; उभयथा च सूत्रं प्रणीतम्** "
              "— the short form is admitted too, because in "
              "continuous recitation the long and the short of that "
              "vowel are indistinguishable, and the sūtra was "
              "framed to be read either way. A rule deliberately "
              "left ambiguous because the ambiguity is in the "
              "sound"),
    Matup("5.2.111", gives="īran", of=("kāṇḍa",), sense="asti",
          excepts=("5.2.94",),
          why="काण्डाण्डादीरन्नीरचौ, **यथासंख्यम्**; the काण्ड "
              "member. **काण्डीरः**"),
    Matup("5.2.111", gives="īrac", of=("aṇḍa",), sense="asti",
          excepts=("5.2.94",),
          why="काण्डाण्डादीरन्नीरचौ, the अण्ड member. "
              "**अण्डीरः**"),
    Matup("5.2.112", gives="valac", gana="rajaḥprabhṛti",
          sense="asti", excepts=("5.2.94",),
          why="रजःकृष्यासुतिपरिषदो वलच्. **रजस्वला स्त्री**; "
              "**कृषीवलः कुटुम्बी**, a householder who ploughs; "
              "आसुतीवलः शौण्डिकः; **परिषद्वलो राजा**, a king with "
              "a council. 6.3.118 वले gives the lengthening.\n\n"
              "**इतिकरणो विषयनियमार्थः सर्वत्र संबध्यते; तेनेह न "
              "भवति — रजोऽस्मिन् ग्रामे विद्यते** — the इति of "
              "5.2.94 again, confining what may be named. "
              "**वलच्प्रकरणेऽन्येभ्योऽपि दृश्यते** — भ्रातृवलः, "
              "पुत्रवलः, उत्साहवलः",
          keeps_out="रजोऽस्मिन् ग्रामे विद्यते"),
    Matup("5.2.113", gives="valac", of=("danta", "śikhā"),
          sense="asti", result="saṃjñā", excepts=("5.2.94",),
          why="दन्तशिखात् संज्ञायाम्. **दन्तावलो गजः**, an "
              "elephant, named from its tusks; **शिखावलं नगरम्**, "
              "शिखावला स्थूणा"),
    Matup("5.2.114", nipatana=True, gana="jyotsnādi",
          sense="asti", result="saṃjñā", excepts=("5.2.94",),
          why="ज्योत्स्नातमिस्राशृङ्गिणोर्जस्विन्नूर्जस्वलगोमिन्"
              "मलिनमलीमसाः — eight forms laid down, each with its "
              "own irregularity spelled out.\n\n"
              "**ज्योतिष उपधालोपो नश्च प्रत्ययो निपात्यते** — "
              "**ज्योत्स्ना चन्द्रप्रभा**, moonlight. **तमस "
              "उपधाया इकारो रश्च** — **तमिस्रा रात्रिः**, and "
              "**स्त्रीत्वमतन्त्रम्; अन्यत्रापि दृश्यते — तमिस्रं "
              "नभः**, the feminine is not binding. "
              "**शृङ्गादिनच् प्रत्ययो निपात्यते** — **शृङ्गिणः**. "
              "**ऊर्जोऽसुगागमो निपात्यते विनिवलचौ प्रत्ययौ** — "
              "**ऊर्जस्वी, ऊर्जस्वलः**. **गोर्मिनिप्रत्ययो "
              "निपात्यते** — **गोमी**. **मलशब्दाद् इनजीमसचौ "
              "प्रत्ययौ निपात्येते** — **मलिनः, मलीमसः**"),
    Matup("5.2.115", gives="ini", also_gives=("ṭhan", "matup"),
          stem_final="a", sense="asti", optional=True,
          excepts=("5.2.94",),
          why="अत इनिठनौ — from any stem in short अ. **दण्डी, "
              "दण्डिकः**, and **अन्यतरस्यामित्यधिकाराद् मतुबपि "
              "भवति**, दण्डवान्. **तपरकरणं किम्?** श्रद्धावान् — "
              "the त marks the vowel SHORT.\n\n"
              "**AND A VERSE NAMES FOUR PLACES WHERE THE TWO DO "
              "NOT COME.**\n\n"
              "    एकाक्षरात् कृतो जातेः सप्तम्यां च न तौ "
              "स्मृतौ ॥\n\n"
              "From a ONE-SYLLABLE word — **स्ववान्, खवान्**; from "
              "a कृत् formation — **कारकवान्**; from a word for a "
              "KIND — **व्याघ्रवान्, सिंहवान्**; and in the "
              "LOCATIVE sense — दण्डा अस्यां सन्ति **दण्डवती "
              "शाला**.\n\n"
              "**इतिकरणो विषयनियमार्थः सर्वत्र संबध्यते; तेन "
              "क्वचिद् भवत्यपि** — and the restriction is not "
              "absolute: **कार्यी, हार्यी, तण्डुली, तण्डुलिकः**",
          keeps_out="स्ववान्, कारकवान्, व्याघ्रवान्, दण्डवती शाला"),
    Matup("5.2.116", gives="ini", also_gives=("ṭhan", "matup"),
          gana="vrīhyādi", sense="asti", excepts=("5.2.94",),
          why="व्रीह्यादिभ्यश्च. **मतुब् भवत्येव**: **व्रीही, "
              "व्रीहिकः, व्रीहिमान्**; मायी, मायिकः, मायावान्.\n\n"
              "**AND THE LIST IS NOT UNIFORM.** **न च "
              "व्रीह्यादिभ्यः सर्वेभ्यः प्रत्ययद्वयमिष्यते** — "
              "**शिखादिभ्य इनिर्वाच्य इकन् यवखदादिषु; परिशिष्टेभ्य "
              "उभयम्**: शिखा, मेखला, संज्ञा, बलाका, माला, वीणा, "
              "वडवा, अष्टका, पताका, कर्मन्, चर्मन्, हंसा take इनि "
              "only; यवखद, कुमारी, नौ take इकन् only; the rest "
              "take both.\n\n"
              "**व्रीहिग्रहणं किमर्थम्, यावता तुन्दादिषु "
              "व्रीहिशब्दः पठ्यते?** And why name व्रीहि when it "
              "is already in another list? **एवं तर्हि तुन्दादिषु "
              "व्रीहिग्रहणम् अर्थग्रहणं विज्ञायते** — there the "
              "word is taken for its MEANING, so that शालि too is "
              "reached: **शालिलः, शाली, शालिकः, शालिमान्**. "
              "**शीर्षाद् नञः** (ग०सू०१३५) — अशीर्षी, अशीर्षिकः"),
    Matup("5.2.117", gives="ilac",
          also_gives=("ini", "ṭhan", "matup"), gana="tundādi",
          sense="asti", excepts=("5.2.94",),
          why="तुन्दादिभ्य इलच् च — **चकाराद् इनिठनौ मतुप् च**, "
              "four affixes at once. **तुन्दिलः, तुन्दी, "
              "तुन्दिकः, तुन्दवान्**; उदरिलः, उदरी, उदरिकः, "
              "उदरवान्. तुन्द, उदर, पिचण्ड, घट, यव, व्रीहि, "
              "**स्वाङ्गाद् विवृद्धौ च** (ग०सू०१३६) — तुन्दादिः, "
              "and the last entry takes any part of the body when "
              "it is OVERGROWN"),
    Matup("5.2.118", gives="ṭhañ", pre="eka-go", sense="asti",
          stem_final="a", excepts=("5.2.94",),
          why="एकगोपूर्वाट् ठञ् नित्यम्. एकशतमस्यास्तीति "
              "**ऐकशतिकः**; ऐकसहस्रिकः; **गौशतिकः**, "
              "गौसहस्रिकः.\n\n"
              "**अत इत्येव** — the short अ of 5.2.115 carries, so "
              "**एकविंशतिरस्यास्तीति न भवति**. **कथमैकगविकः? "
              "समासान्ते कृते भविष्यति** — that form comes once "
              "the compound-final has been added. **कथं "
              "गौशकटिकः? शकटीशब्देन समानार्थः शकटशब्दोऽस्ति** — "
              "and that one from a synonym in अ. "
              "**अवश्यं चात इत्यनुवर्त्यम्** for 5.2.128's sake.\n\n"
              "**नित्यग्रहणं मतुपो बाधनार्थम्** — the *always* is "
              "there to keep the gathered मतुप् out"),
    Matup("5.2.119", gives="ṭhañ", uttarapada="śata-sahasra",
          pre="niṣka", sense="asti", excepts=("5.2.94",),
          why="शतसहस्रान्ताच्च निष्कात् — from a stem ending in "
              "*hundred* or *thousand*, those words standing after "
              "निष्क. निष्कशतमस्यास्ति **नैष्कशतिकः**; "
              "नैष्कसहस्रिकः. **सुवर्णनिष्कशतमस्तीत्यनभिधानाद् न "
              "भवति** — and with another word in front the "
              "language does not say it",
          keeps_out="सुवर्णनिष्कशतम्"),
    Matup("5.2.120", gives="yap", of=("rūpa",), sense="asti",
          result="āhata-praśaṃsā", excepts=("5.2.94",),
          why="रूपादाहतप्रशंसयोर्यप्. **निघातिकाताडनादिना "
              "दीनारादिषु रूपं यदुत्पद्यते तदाहतम् उच्यते** — a "
              "stamp struck on a coin. आहतं रूपमस्य **रूप्यो "
              "दीनारः**, a struck dinar; and in praise, प्रशस्तं "
              "रूपमस्यास्ति **रूप्यः पुरुषः**, a handsome man. "
              "**आहतप्रशंसयोरिति किम्?** रूपवान्.\n\n"
              "**यप्प्रकरणेऽन्येभ्योऽपि दृश्यते** — **हिम्याः "
              "पर्वताः**, गुण्या ब्राह्मणाः",
          keeps_out="रूपवान्"),
    Matup("5.2.121", gives="vini", also_gives=("matup",),
          stem_final="as", sense="asti", excepts=("5.2.94",),
          why="असो मायामेधास्रजो विनिः; the अस्-final half. "
              "**मतुप् सर्वत्र समुच्चीयत एव**. **यशस्वी, "
              "तपस्वी, पयस्वी**"),
    Matup("5.2.121", gives="vini", also_gives=("matup",),
          of=("māyā", "medhā", "sraj"), sense="asti",
          excepts=("5.2.94",),
          why="असो मायामेधास्रजो विनिः, the three named words. "
              "**मायावी, मेधावी, स्रग्वी**. **मायाशब्दाद् "
              "व्रीह्यादिषु पाठाद् इनिठनावपि भवतः** — and माया is "
              "in 5.2.116's list as well, so मायी and मायिकः stand "
              "beside them"),
    Matup("5.2.122", gives="vini", sense="asti", usage="chandasi",
          optional=True, excepts=("5.2.94",),
          why="बहुलं छन्दसि — and बहुलम् is doing a great deal of "
              "work. अग्ने॑ **तेजस्विन्**; **न भवति, सूर्यो "
              "वर्चस्वान्**.\n\n"
              "Eight vārttikas hang on that one word. "
              "**अष्ट्रामेखलाद्वयोभयरुजाहृदयानां दीर्घत्वं च** — "
              "अष्ट्॒**रावी**, मेखलावी, उभया॒**वी**; "
              "**मर्मणश्च** — मर्मावी; "
              "**सर्वत्रामयस्योपसंख्यानम्, छन्दसि भाषायां च** — "
              "आमया॒**वी**, in the Veda and in speech alike; "
              "**शृङ्गवृन्दाभ्यामारकन्** — **शृङ्गारकः**, "
              "वृ॒न्दारकः; **फलबर्हाभ्यामिनज्** — फलिनः, बर्हिणः; "
              "**हृदयाच्चालुरन्यतरस्याम्** — हृदयालुः, हृदयी, "
              "हृदयिकः, हृदयवान्; "
              "**शीतोष्णतृप्रेभ्यस्तद् न सहत इत्यालुज्** — "
              "**शीतालुः**, one who cannot BEAR the cold, and "
              "**हिमाच्चेलुः**, हिमेलुः, **बलादूलच्**, बलूलः, "
              "**वातात् समूहे च** — वातूलः; "
              "**पर्वमरुद्भ्यां तन्** — प॑र्व॒तः, मरुत्तः; "
              "**अर्थात् तदभाव इनिः** — **अर्थी**, one who LACKS "
              "it, against अर्थवान् who has it. "
              "**तदेतत् सर्वं बहुलग्रहणेन सम्पद्यते**"),
    Matup("5.2.123", gives="yus", of=("ūrṇā",), sense="asti",
          excepts=("5.2.94",),
          why="ऊर्णाया युस्. **सकारः पदसंज्ञार्थः** — the स is "
              "there to make the result a पद. ऊर्णास्य विद्यते "
              "ऊ॒र्णा॒**युः**. **केचिच्छन्दोग्रहणमनुवर्तयन्ति** — "
              "and some carry the Veda-restriction down to it"),
    Matup("5.2.124", gives="gmini", of=("vāc",), sense="asti",
          excepts=("5.2.94",),
          why="वाचो ग्मिनिः. **वाग्ग्मी**, वाग्ग्मिनौ, वाग्ग्मिनः "
              "— eloquent"),
    Matup("5.2.125", gives="ālac", also_gives=("āṭac",),
          of=("vāc",), sense="asti", result="bahubhāṣin-kutsita",
          excepts=("5.2.124",),
          why="आलजाटचौ बहुभाषिणि, **ग्मिनेरपवादः**. **वाचालः, "
              "वाचाटः**.\n\n"
              "**कुत्सित इति वक्तव्यम्; यो हि सम्यग् बहु भाषते, "
              "वाग्ग्मीत्येव स भवति** — and a vārttika adds that "
              "it must be BLAMEWORTHY talking, since a man who "
              "talks much and well is वाग्ग्मी by the rule before. "
              "The two rules divide the fluent from the garrulous"),
    Matup("5.2.126", nipatana=True, gives="āmin", of=("sva",),
          sense="asti", result="aiśvarya", excepts=("5.2.94",),
          why="स्वामिन्नैश्वर्ये — **स्वामिन्निति निपात्यते**. "
              "**स्वशब्दाद् ऐश्वर्यवाचिनो मत्वर्थ आमिन् प्रत्ययो "
              "निपात्यते**: स्वमस्यास्तीति, ऐश्वर्यमस्यास्तीति "
              "**स्वामी**. **ऐश्वर्य इति किम्?** स्ववान् — a man "
              "with property and no lordship",
          keeps_out="स्ववान्"),
    Matup("5.2.127", gives="ac", gana="arśaādi", sense="asti",
          excepts=("5.2.94",),
          why="अर्शआदिभ्योऽच्. अर्शांसि अस्य विद्यन्ते "
              "**अर्शसः**; उरसः.\n\n"
              "**आकृतिगणश्चायम्; यत्राभिन्नरूपेण शब्देन तद्वतो "
              "ऽभिधानं तत् सर्वमिह द्रष्टव्यम्** — an open list, "
              "and the definition of it is the shape of the "
              "result: wherever a word UNCHANGED IN FORM names the "
              "thing that has it, the base belongs here. A gaṇa "
              "defined by what its members do rather than by "
              "membership.\n\n"
              "अर्शस्, उरस्, तुन्द, चतुर, पलित, जटा, घटा, अभ्र, "
              "कर्दम, आम, लवण, **स्वाङ्गाद् हीनात्** (ग०सू०१३७), "
              "**वर्णात्** (ग०सू०१३८) — अर्शआदिः"),
    Matup("5.2.128", gives="ini", of_samjna="prāṇistha",
          sense="asti", stem_final="a",
          result="dvandva-upatāpa-garhya", excepts=("5.2.94",),
          why="द्वन्द्वोपतापगर्ह्यात् प्राणिस्थादिनिः — three kinds "
              "of base, all naming something ON a living body. "
              "**द्वन्द्वः समासः; उपतापो रोगः; गर्ह्यं निन्द्यम्**. "
              "द्वन्द्वात् — **कटकवलयिनी**, शङ्खनूपुरिणी; "
              "उपतापात् — **कुष्ठी**, किलासी; गर्ह्यात् — "
              "**ककुदावर्ती**, काकतालुकी.\n\n"
              "**प्राणिस्थादिति किम्?** पुष्पफलवान् वृक्षः. "
              "**प्राण्यङ्गाद् नेष्यते** — and NOT a limb, "
              "पाणिपादवती. **अत इत्यनुवर्तते; तेनेह न भवति — "
              "चित्रललाटिकावती**. **सिद्धे प्रत्यये पुनर्वचनं "
              "ठनादिबाधनार्थम्** — the affix was coming anyway, "
              "and the rule is stated to shut ठन् and the rest out",
          keeps_out="पुष्पफलवान् वृक्षः, पाणिपादवती"),
    Matup("5.2.129", gives="ini", of=("vāta", "atisāra"),
          adesa="kuk", sense="asti", result="upatāpa",
          excepts=("5.2.128",),
          why="वातातिसाराभ्यां कुक् च. **वातातिसारयोर् "
              "उपतापत्वात् पूर्वेणैव सिद्धे प्रत्यये कुगर्थमेवेदं "
              "वचनम्** — both are diseases, so 5.2.128 gave the "
              "affix already; this rule is for the कुक् alone. "
              "**वातकी, अतिसारकी**.\n\n"
              "**पिशाचाच्चेति वक्तव्यम्** — **पिशाचकी वैश्रवणः**, "
              "and **रोगे चायमिष्यते; इह न भवति — वातवती गुहा**",
          keeps_out="वातवती गुहा"),
    Matup("5.2.130", gives="ini", of_samjna="pūraṇānta",
          sense="asti", result="vayas", excepts=("5.2.94",),
          why="वयसि पूरणात् — from a word made by an ORDINAL "
              "affix, when an AGE is meant. पञ्चमोऽस्यास्ति मासः "
              "संवत्सरो वा **पञ्चमी उष्ट्रः**, a camel in its "
              "fifth year; नवमी, दशमी.\n\n"
              "**सिद्धे सति नियमार्थं वचनम् — इनिरेव भवति, ठन् न "
              "भवतीति** — the affix was coming; the rule is a "
              "restriction, and shuts ठन् out. **वयसीति किम्?** "
              "पञ्चमवान् ग्रामरागः",
          keeps_out="पञ्चमवान् ग्रामरागः"),
    Matup("5.2.131", gives="ini", gana="sukhādi", sense="asti",
          excepts=("5.2.94",),
          why="सुखादिभ्यश्च — and again a restriction rather than "
              "a giving, **इनिः प्रत्ययो नियम्यते**. **सुखी, "
              "दुःखी**. सुख, दुःख, तृप्र, कृच्छ्र, आम्र, अलीक, "
              "करुणा, कृपण, सोढ, शील, हल, **माला क्षेपे** "
              "(ग०सू०१३९), प्रणय — सुखादिः.\n\n"
              "**माला क्षेप इति पठ्यते, व्रीह्यादिषु च "
              "मालाशब्दोऽस्ति, तदिह क्षेपे मतुब्बाधनार्थं वचनम्** "
              "— माला is in 5.2.116's list too, and its entry here "
              "with *in contempt* is to keep मतुप् out in that "
              "sense alone"),
    Matup("5.2.132", gives="ini",
          uttarapada="dharma-śīla-varṇa", sense="asti",
          excepts=("5.2.94",),
          why="धर्मशीलवर्णान्ताच्च. **अन्तशब्दः प्रत्येकम् "
              "अभिसंबध्यते** — *ending in* goes with each of the "
              "three severally. ब्राह्मणानां धर्मो ब्राह्मणधर्मः, "
              "सोऽस्यास्तीति **ब्राह्मणधर्मी**; ब्राह्मणशीली, "
              "ब्राह्मणवर्णी"),
    Matup("5.2.133", gives="ini", of=("hasta",), sense="asti",
          result="jāti", excepts=("5.2.94",),
          why="हस्ताज् जातौ — and only where the WHOLE WORD names "
              "a kind, **समुदायेन चेज् जातिरभिधीयते**. "
              "हस्तोऽस्यास्तीति **हस्ती**, an elephant. "
              "**जाताविति किम्?** हस्तवान् पुरुषः — a man with "
              "hands is not a kind of thing",
          keeps_out="हस्तवान् पुरुषः"),
    Matup("5.2.134", gives="ini", of=("varṇa",), sense="asti",
          result="brahmacārin", excepts=("5.2.94",),
          why="वर्णाद् ब्रह्मचारिणि — where the whole word names a "
              "STUDENT. **ब्रह्मचारीति त्रैवर्णिकोऽभिप्रेतः; स हि "
              "विद्याग्रहणार्थमुपनीतो ब्रह्म चरति, नियमम् "
              "आसेवत इत्यर्थः** — one of the three classes, "
              "initiated for learning, who *walks in the sacred "
              "word*, that is, keeps the observances. **वर्णी**. "
              "**ब्रह्मचारिणीति किम्?** वर्णवान्",
          keeps_out="वर्णवान्"),
    Matup("5.2.135", gives="ini", gana="puṣkarādi", sense="asti",
          result="deśa", excepts=("5.2.94",),
          why="पुष्करादिभ्यो देशे — where the whole word names a "
              "PLACE. **पुष्करिणी**, a lotus-pond; पद्मिनी. "
              "**देश इति किम्?** पुष्करवान् हस्ती.\n\n"
              "**इनिप्रकरणे बलाद् बाहूरुपूर्वाद् उपसंख्यानम्** — "
              "बाहुबली, ऊरुबली; **सर्वादेश्च** — सर्वधनी, "
              "**सर्वकेशी नटः**; **अर्थाच्चासन्निहिते** — "
              "**अर्थी**, and **असन्निहित इति किम्?** अर्थवान्; "
              "**तदन्ताच्च** — धान्यार्थी, हिरण्यार्थी.\n\n"
              "पुष्कर, पद्म, उत्पल, तमाल, कुमुद, नड, कपित्थ, बिस, "
              "मृणाल, कर्दम, शालूक, करीष, शिरीष, यवास, हिरण्य — "
              "पुष्करादिः",
          keeps_out="पुष्करवान् हस्ती"),
    Matup("5.2.136", gives="matup", also_gives=("ini",),
          gana="balādi", sense="asti", optional=True,
          why="बलादिभ्यो मतुबन्यतरस्याम् — and here मतुप् is given "
              "OUTRIGHT where everywhere else it was gathered in "
              "by the carried अन्यतरस्याम्. "
              "**अन्यतरस्यांग्रहणेन प्रकृत इनिः समुच्चीयते** — the "
              "word now gathers the इनि instead, and the two "
              "affixes have changed places. **बलवान्, बली**; "
              "उत्साहवान्, उत्साही. बल, उत्साह, उद्भाव, उद्वास, "
              "शिखा, पूग, मूल, दंश, कुल, आयाम, व्यायाम, आरोह, "
              "अवरोह, परिणाह, युद्ध — बलादिः"),
    Matup("5.2.137", gives="ini", stem_final="man-ma",
          sense="asti", result="saṃjñā", excepts=("5.2.94",),
          why="संज्ञायां मन्माभ्याम् — from a stem ending in मन् "
              "or in the sound म, where the whole word is a NAME. "
              "**प्रथिमिनी, दामिनी**; and from the म-final, "
              "**होमिनी, सोमिनी**. **संज्ञायामिति किम्?** "
              "सोमवान्, होमवान्",
          keeps_out="सोमवान्"),
    Matup("5.2.138", gives="ba",
          also_gives=("bha", "yus", "ti", "tu", "ta", "yas"),
          of=("kam", "śam"), sense="asti", excepts=("5.2.94",),
          why="कंशंभ्यां बभयुस्तितुतयसः — SEVEN affixes for two "
              "words in one rule, the most of any sūtra in the "
              "pāda. **कम् शम् इति मकारान्तावुदकसुखयोर्वाचकौ** — "
              "कम् is water and शम् is ease. **कम्बः, शम्बः; "
              "कम्भः, शम्भः; कंयुः, शंयुः; कन्तिः, शन्तिः; "
              "कन्तुः, शन्तुः; कन्तः, शन्तः; कंयः, शंयः**.\n\n"
              "**सकारः पदसंज्ञार्थः, तेनानुस्वारपरसवर्णौ सिद्धौ "
              "भवतः; संज्ञायां हि असत्यां कम्यः शम्य इति स्यात्** "
              "— the स in युस् makes the result a पद, and without "
              "that the nasal would not become अनुस्वार and the "
              "forms would come out कम्यः, शम्यः"),
    Matup("5.2.139", gives="bha", of=("tundi", "bali", "vaṭi"),
          sense="asti", excepts=("5.2.94",),
          why="तुन्दिबलिवटेर्भः. **तुन्दिरिति वृद्धा नाभिर् "
              "उच्यते** — a swollen navel. **तुन्दिभः**; "
              "बलिभः, वटिभः. **बलिशब्दः पामादिषु पठ्यते, तेन "
              "बलिन इत्यपि भवति** — and बलि is in the पामादि list "
              "of 5.2.100 as well, so बलिनः stands too"),
    Matup("5.2.140", gives="yus", of=("aham", "śubham"),
          sense="asti", excepts=("5.2.94",),
          why="अहंशुभमोर्युस् — and the pāda ends. "
              "**अहमिति शब्दान्तरमहंकारे वर्तते** — the अहम् here "
              "is a different word from the pronoun and means "
              "SELF-REGARD; **शुभमित्यव्ययं शुभपर्यायः**. "
              "**सकारः पदसंज्ञार्थः**. **अहंयुः**, "
              "**अहंकारवानित्यर्थः**; **शुभंयुः**, "
              "**कल्याणवानित्यर्थः**.\n\n"
              "इति श्रीजयादित्यविरचितायां काशिकायां वृत्तौ "
              "पञ्चमाध्यायस्य द्वितीयः पादः"),
)


@dataclass(frozen=True)
class Comes:
    """What the resolver answers with."""

    affix: str
    sutra: str
    why: str
    also_gives: Tuple[str, ...] = ()
    case: str = ""
    optional: bool = False
    adesa: str = ""
    #: True where the whole form is laid down rather than derived.
    nipatana: bool = False
    excepts: Tuple[str, ...] = ()


def _reaches(row: Matup, stem: str, gana: str, sense: str, case: str,
             result: str, samjna: str, uttarapada: str, pre: str,
             usage: str, stem_final: str) -> bool:
    if row.of and stem not in row.of:
        return False
    if row.gana and gana != row.gana:
        return False
    if row.sense and sense and sense != row.sense:
        return False
    if row.case and case and case != row.case:
        return False
    if row.result and result != row.result:
        return False
    if row.of_samjna and samjna != row.of_samjna:
        return False
    if row.uttarapada and uttarapada != row.uttarapada:
        return False
    if row.stem_final and stem_final != row.stem_final:
        return False
    if row.pre and pre != row.pre:
        return False
    if row.usage and usage != row.usage:
        return False
    return True


def _supplies(row: Matup, wants: str) -> bool:
    """Whether the row gives the affix asked for."""
    return (not wants
            or wants == row.gives
            or wants in row.also_gives)


def _how_specific(row: Matup) -> int:
    """
    A named base is narrowest. The sense counts for more here than
    it did in 5.1, because in this pāda a sense usually belongs to
    exactly one rule.
    """
    return (
        7 * bool(row.of)
        + 6 * bool(row.gana)
        + 5 * bool(row.of_samjna)
        + 5 * bool(row.uttarapada)
        + 4 * bool(row.stem_final)
        + 4 * bool(row.pre)
        + 3 * bool(row.result)
        + 3 * bool(row.usage)
        + 3 * bool(row.sense)
        + 1 * bool(row.case)
    )


def what_comes(stem: str = "", *, gana: str = "", sense: str = "",
               case: str = "", result: str = "", samjna: str = "",
               uttarapada: str = "", pre: str = "", usage: str = "",
               stem_final: str = "", wants: str = "") -> Comes:
    """
    5.2.1–28 — a base, a sense, and the affix that answers.

    Unlike 5.1 there is no heading standing over the section, so a
    question that reaches no rule reaches nothing: the answer is
    empty, and that is the truth about this stretch rather than a
    gap in it.
    """
    matched = [
        row for row in MATUP_TABLE
        if _reaches(row, stem, gana, sense, case, result, samjna,
                    uttarapada, pre, usage, stem_final)
        and _supplies(row, wants)
    ]
    if not matched:
        return Comes("", "", "No rule of 5.2.1–28 is reached. The "
                            "pāda has no heading standing over it, "
                            "so nothing supplies by default")
    row = max(matched, key=_how_specific)
    return Comes(row.gives, row.sutra, row.why,
                 also_gives=row.also_gives, case=row.case,
                 optional=row.optional, adesa=row.adesa,
                 nipatana=row.nipatana, excepts=row.excepts)


def provisions_for(sutra_id: str) -> Tuple[Matup, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in MATUP_TABLE if row.sutra == sutra_id)
