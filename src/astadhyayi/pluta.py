# -*- coding: utf-8 -*-
"""
८.२.८२–१०८ — the प्लुत, and the three accents it can carry.

8.2.82 वाक्यस्य टेः प्लुत उदात्तः is a heading of three words
at once — **वाक्यस्य टेर् इति, प्लुत इति, उदात्त इति च, एतत्
त्रयम् अपि अधिकृतं वेदितव्यम् आ पादपरिसमाप्तेः** — the LAST
VOWEL of a sentence, made three mātrās long, and high-toned.
Everything to 8.2.108 stands under it, and three later sūtras
change the third word: 8.2.100–102 make the प्लुत अनुदात्त and
8.2.103–105 स्वरित.

**WHERE IT COMES.** A teacher's return-greeting to one who is
not a śūdra (आयुष्मान् एधि देवदत्त३); calling from a distance
(आगच्छ भो माणवक देवदत्त३); ओम् at the opening of a recitation
(ओ३म् अग्निम् ईळे); ये in a sacrificial act (ये३ यजामहे); the
last syllable of a याज्या; the first syllable of ब्रूहि, प्रेष्य,
श्रौषट्, वौषट् and आवह; हि in an answer (अकार्षं हि३); the
आम्रेडित in a threat (चौरचौर३); a verb with अङ्ग left hanging
(अङ्ग कूज३); deliberation (होतव्यं दीक्षितस्य गृहा३इ); and
assent (किम् आत्थ३).

**AND THE VOWEL IT LANDS ON IS NOT ALWAYS THE WHOLE VOWEL.**
8.2.106 प्लुतावैच इदुतौ: where an ऐ or औ would be lengthened,
it is the इ or उ inside it that is — **ऐ३तिकायन, औ३पमन्यव**.
And 8.2.107 goes further: a non-प्रगृह्य ए or ओ splits into a
प्लुत आ plus an इ or उ, so that अग्ने becomes अग्ना३इ — which is
why the deliberating sentences of 8.2.97 all end in that
strange-looking इ.

**WHAT THIS MODULE DOES NOT DO.** It says where the प्लुत comes
and what accent it takes. That a प्लुत vowel is three mātrās is
1.2.27's, and 8.2.108's own second half — the संहिता heading
that runs to the end of the adhyāya — is recorded here but
belongs to 8.3 and 8.4 to use.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: This module's stretch, which closes पाद ८.२.
PLUTA_RUN: Tuple[str, str] = ("8.2.82", "8.2.108")

#: 8.2.82's heading runs to the pāda's end.
ADHIKARA_TO: str = "8.2.108"

#: 8.2.108's second half opens a heading of its own, which runs
#: to the end of the adhyāya and belongs to 8.3 and 8.4.
SAMHITA_TO: str = "8.4.68"

#: 8.2.91's five, whose FIRST syllable is lengthened.
BRUHI_FIVE: Tuple[str, ...] = (
    "brūhi", "preṣya", "śrauṣaṭ", "vauṣaṭ", "āvaha")

#: 8.2.100–102's three settings, where the प्लुत is अनुदात्त.
ANUDATTA_THREE: Tuple[str, ...] = (
    "8.2.100", "8.2.101", "8.2.102")

#: 8.2.103–105's three, where it is स्वरित.
SVARITA_THREE: Tuple[str, ...] = (
    "8.2.103", "8.2.104", "8.2.105")


@dataclass(frozen=True)
class Plu:
    """One rule of 8.2.82–108: a lengthening and its accent."""

    sutra: str
    #: `pluta`, `praṇava`, `id-ut`, `ā-id-ut`, `ya-va`.
    does: str = ""
    #: What accent it carries. Empty takes the heading's उदात्त.
    accent: str = ""
    #: The words named outright.
    of: Tuple[str, ...] = ()
    #: The shape of what is lengthened.
    gana: str = ""
    sense: Tuple[str, ...] = ()
    #: Which syllable: `ṭi` by the heading, or `ādi`, `para`,
    #: `anta`, `anantya` where a rule says otherwise.
    position: str = ""
    #: A named teacher's opinion, which makes the rule an
    #: option in the language.
    view: str = ""
    #: True of a rule that only opens a heading.
    heading: bool = False
    optional: bool = False
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


PLUTA_TABLE: Tuple[Plu, ...] = (
    Plu(
        "8.2.82", does="pluta", accent="udātta", heading=True,
        why="वाक्यस्य टेः प्लुत उदात्तः — a heading of THREE "
            "words at once: **वाक्यस्य टेर् इति, प्लुत इति, "
            "उदात्त इति च, एतत् त्रयम् अपि अधिकृतं वेदितव्यम् "
            "आ पादपरिसमाप्तेः**. What is lengthened is the "
            "टि — the last vowel of a sentence with whatever "
            "follows it; the lengthening is to three mātrās; "
            "and the accent is high. Every rule to 8.2.108 "
            "borrows all three, and only the third is ever "
            "changed — twice, at 8.2.100 and 8.2.103"),
    Plu(
        "8.2.83", does="pluta", sense=("pratyabhivāda",),
        keeps_out="अभिवादये तुषजातीयोऽहं भोः — the greeter is a "
                  "śūdra, and no lengthening comes",
        why="प्रत्यभिवादेऽशूद्रे — in a teacher's RETURN "
            "GREETING to one who is not a śūdra: **अभिवादये "
            "देवदत्तोऽहं भोः — आयुष्मान् एधि देवदत्त३**. "
            "**प्रत्यभिवादो नाम यद् अभिवाद्यमानो गुरुर् आशिषं "
            "प्रयुङ्क्ते** — the blessing the elder speaks "
            "back. It is the first rule under the heading and "
            "the one the Kāśikā uses to prove all three of its "
            "words at once"),
    Plu(
        "8.2.84", does="pluta", sense=("dūrād-dhūta",),
        why="दूराद्धूते च — and in CALLING FROM A DISTANCE: "
            "**आगच्छ भो माणवक देवदत्त३; आगच्छ भो माणवक "
            "यज्ञदत्त३**. **आह्वानं हूतम्, शब्देन "
            "सम्बोधनम्** — a summons by voice. And distance is "
            "settled by the calling and not measured: "
            "**दूरं यद्यपि अपेक्षाभेदाद् अनवस्थितम्, तथापि "
            "हूतापेक्षम्** — far enough that one must raise "
            "one's voice"),
    Plu(
        "8.2.85", does="pluta", of=("hai", "he"),
        sense=("dūrād-dhūta",), position="anantya",
        blocks=("8.2.84",),
        why="हैहेप्रयोगे हैहयोः — but where है or हे is used in "
            "such a call, it is THEY that are lengthened and "
            "not the sentence's last vowel: **है३ देवदत्त; "
            "हे३ देवदत्त; देवदत्त है३; देवदत्त हे३**. Both "
            "orders are given, and the reason the two words are "
            "named twice over is exactly that: **पुनर् "
            "हैहयोर् ग्रहणम् अनन्त्ययोर् अपि यथा स्यात्** — so "
            "the rule shall reach them where they do not stand "
            "last"),
    Plu(
        "8.2.86", does="pluta", gana="guru-an-ṛt",
        position="anantya", view="prācām", optional=True,
        why="गुरोरनृतोऽनन्त्यस्याप्येकैकस्य प्राचाम् — and in "
            "the EASTERNERS' view any heavy vowel that is not "
            "an ऋ may be lengthened, one at a time, even where "
            "it does not stand last: **अपिशब्दाद् "
            "अन्त्यस्यापि**. The rule is about the प्लुत the "
            "sūtras before have already given — **यः प्लुतो "
            "विहितः, तस्य एव अयं स्थानिविशेष उच्यते** — so it "
            "does not add a lengthening anywhere but says which "
            "syllable may carry one that is already due. "
            "Naming the Easterners makes it an option"),
    Plu(
        "8.2.87", does="pluta", of=("om",), sense=("abhyādāna",),
        keeps_out="ओम् इत्येतद् अक्षरम् उद्गीथम् उपासीत — the "
                  "syllable spoken ABOUT and not at an opening",
        why="ओमभ्यादाने — and ओम् at the OPENING of a "
            "recitation: **ओ३म् अग्निम् ईळे पुरोहितम्**. "
            "**अभ्यादानं प्रारम्भः**. The counter-example is "
            "from the Chāndogya, where the syllable is the "
            "subject of the sentence rather than the start of "
            "one, and no lengthening comes"),
    Plu(
        "8.2.88", does="pluta", of=("ye",),
        sense=("yajña-karman",),
        keeps_out="ये यजामह इति पञ्चाक्षरम् — the words quoted "
                  "in study and not used in the rite; ये "
                  "देवासः — a different ये altogether",
        why="ये यज्ञकर्मणि — and ये in a SACRIFICIAL ACT: "
            "**ये३ यजामहे**. The vṛtti narrows it to that one "
            "formula — **ये यजामह इत्यत्र एव अयं प्लुत "
            "इष्यते** — and the counter-example is the same "
            "words counted as five syllables during study, "
            "where the rite is not being performed"),
    Plu(
        "8.2.89", does="praṇava", position="ṭi",
        sense=("yajña-karman",),
        why="प्रणवष्टेः — and in a sacrificial act the टि is "
            "replaced by the प्रणव. The vṛtti has to say what "
            "that is: **पादस्य वा अर्धर्चस्य वा अन्त्यम् "
            "अक्षरम् उपसंगृह्य तदाद्यक्षरशेषस्य स्थाने "
            "त्रिमात्रम् ओकारम् ओङ्कारं वा विदधति, तं "
            "प्रणवम् इत्याचक्षते** — the last syllable of a "
            "quarter or half-verse is taken and what remains "
            "of it is replaced by a three-mātrā ओ. It is a "
            "substitution and not a lengthening, which is why "
            "it needs its own word"),
    Plu(
        "8.2.90", does="pluta", gana="yājyā", position="anta",
        sense=("yajña-karman",),
        keeps_out="याज्या न — where the word is not the last of "
                  "the formula, अन्तग्रहण shuts it out",
        why="याज्याऽन्तः — and the LAST syllable of a याज्या: "
            "**स्तोमैर् विधेमाग्नये३; जिह्वाम् अग्ने चकृषे "
            "हव्यवाह३म्**. **याज्या नाम ये याज्याकाण्डे "
            "पठ्यन्ते मन्त्राः** — the invitatory verses "
            "collected in their own section, and it is the "
            "last यष्टि of them that is lengthened"),
    Plu(
        "8.2.91", does="pluta", of=BRUHI_FIVE, position="ādi",
        sense=("yajña-karman",),
        why="ब्रूहिप्रेष्यश्रौषड्वौषडावहानामादेः — and the "
            "FIRST syllable of five words in a sacrificial "
            "act: **अग्नयेऽनुब्रू३हि; अग्नये गोमयान् प्रे३ष्य; "
            "अस्तु श्रौ३षट्; वौ३षट्; आ३वह**. This is the first "
            "rule of the run to move the प्लुत off the "
            "sentence's end and onto a word's beginning, and "
            "it does so by saying आदेः against the heading's "
            "टेः"),
    Plu(
        "8.2.92", does="pluta", position="ādi-para",
        sense=("agnīt-preṣaṇa",),
        keeps_out="अग्नीद् अग्नीन् विहर बर्हिः स्तृणाहि — not "
                  "the summons the rule means",
        why="अग्नीत्प्रेषणे परस्य च — and in the AGNĪDH'S "
            "SUMMONS, the first syllable and the one after it "
            "as well: **आ३श्रा३वय; ओ३श्रा३वय** — two lengthenings in "
            "one word, which happens nowhere else in the "
            "Aṣṭādhyāyī. **अग्नीधः प्रेषणम् अग्नीत्प्रेषणम्**, "
            "and **अत्रैव अयं प्लुत इष्यते** confines it to "
            "that call"),
    Plu(
        "8.2.93", does="pluta", of=("hi",), optional=True,
        sense=("pṛṣṭa-prativacana",),
        keeps_out="कटं करिष्यति हि — no question was asked; "
                  "करोमि ननु — the particle is not हि",
        why="विभाषा पृष्टप्रतिवचने हेः — and OPTIONALLY हि in "
            "an ANSWER to a question: **अकार्षीः कटं देवदत्त? "
            "अकार्षं हि३, अकार्षं हि; अलावीः केदारं देवदत्त? "
            "अलाविषं हि३, अलाविषं हि**. Both words are tested "
            "and both do work — the answer must be to a "
            "question, and the particle must be हि"),
    Plu(
        "8.2.94", does="pluta", optional=True,
        sense=("nigṛhya-anuyoga",),
        why="निगृह्यानुयोगे च — and in REFUTING and then "
            "putting the question again: **स्वमतात् "
            "प्रच्यावनं निग्रहः। अनुयोगस् तस्य मतस्य "
            "आविष्करणम्** — one has been driven off his own "
            "position, and the winner then says it back to him. "
            "The vṛtti's example is a debate about whether "
            "sound is eternal, which is as close as the "
            "Aṣṭādhyāyī comes to reporting a philosophical "
            "argument"),
    Plu(
        "8.2.95", does="pluta", gana="āmreḍita",
        sense=("bhartsana",),
        why="आम्रेडितं भर्त्सने — and the आम्रेडित in a THREAT: "
            "**चौरचौ३र, वृषलवृष३ल, दस्योदस्यो३ घातयिष्यामि "
            "त्वा, बन्धयिष्यामि त्वा**. The doubling itself is "
            "8.1.8's — **वाक्यादेर् आमन्त्रितस्य० इति भर्त्सने "
            "द्विर्वचनम् उक्तम्, तस्य आम्रेडितं प्लवते** — so "
            "the two ends of the adhyāya meet: one pāda doubles "
            "the word and the next lengthens the copy. A "
            "vārttika adds that the two may alternate: "
            "**भर्त्सने पर्यायेण इति वक्तव्यम्**"),
    Plu(
        "8.2.96", does="pluta", gana="tiṅ", of=("aṅga",),
        sense=("bhartsana",), position="ākāṅkṣa",
        keeps_out="अङ्ग देवदत्त, मिथ्या वदसि — not a finite "
                  "verb; अङ्ग पच — nothing further is expected",
        why="अङ्गयुक्तं तिङ् आकाङ्क्षम् — and a finite verb "
            "construed with अङ्ग and leaving something "
            "EXPECTED, in a threat: **अङ्ग कू३ज, अङ्ग "
            "व्याह३र — इदानीं ज्ञास्यसि जाल्म** — go on, coo; "
            "you will find out, wretch. All three conditions "
            "are tested, and the second — आकाङ्क्षम् — is what "
            "keeps the plain अङ्ग पच out"),
    Plu(
        "8.2.97", does="pluta", sense=("vicāryamāṇa",),
        why="विचार्यमाणानाम् — and of sentences being WEIGHED "
            "against each other: **प्रमाणेन वस्तुपरीक्षणं "
            "विचारः**. **होतव्यं दीक्षितस्य गृहा३इ** — is one "
            "to make the offering in the initiate's house or "
            "not? **तिष्ठेद् यूपा३इ; अनुप्रहरेद् यूपा३इ**. The "
            "इ at the end of each is 8.2.107's — the ए of the "
            "locative split into a प्लुत आ and an इ — which is "
            "why these sentences look as they do"),
    Plu(
        "8.2.98", does="pluta", position="pūrva",
        sense=("vicāryamāṇa",), blocks=("8.2.97",),
        why="पूर्वं तु भाषायाम् — but in the SPOKEN language it "
            "is the FIRST of the alternatives that is "
            "lengthened and not each: **अहिर् नु३ रज्जुर् नु; "
            "लोष्टो नु३ कपोतो नु** — a snake, or a rope? "
            "**प्रयोगापेक्षं पूर्वत्वम्** — first in the order "
            "of speaking. And the sūtra's own भाषा is read as "
            "confining the rule before it to the Veda: "
            "**इह भाषाग्रहणात् पूर्वयोगश् छन्दसि "
            "विज्ञायते**"),
    Plu(
        "8.2.99", does="pluta", sense=("pratiśravaṇa",),
        why="प्रतिश्रवणे च — and in ASSENT: **प्रतिश्रवणम् "
            "अभ्युपगमः, प्रतिज्ञानम्, श्रवणाभिमुख्यं च। तत्र "
            "अविशेषात् सर्वस्य ग्रहणम्** — three senses of the "
            "word and all three taken, since the sūtra "
            "distinguishes none. **देवदत्त भोः — किम् "
            "आत्थ३?** and **गां मे देहि भोः — अहं ते "
            "ददामि३**"),
    Plu(
        "8.2.100", does="pluta", accent="anudātta",
        sense=("praśna-anta", "abhipūjita"),
        why="अनुदात्तं प्रश्नान्ताभिपूजितयोः — and here the "
            "heading's THIRD word is changed: the प्लुत is "
            "अनुदात्त at a question's END and of what is "
            "honoured. **अगम३ः पूर्वा३न् ग्रामा३न् "
            "अग्निभूता३इ, पटा३उ** — the vocatives at the close "
            "take the low-toned lengthening and the rest of "
            "the words their own by 8.2.105. This is the first "
            "of three sūtras that take the उदात्त away"),
    Plu(
        "8.2.101", does="pluta", accent="anudātta",
        of=("cit",), sense=("upamā",),
        why="चिदिति चोपमाऽर्थे प्रयुज्यमाने — and where चित् is "
            "used to make a COMPARISON: **अग्निचिद् भाया३त्; "
            "राजचिद् भाया३त्** — let him shine like a fire, "
            "like a king. And the vṛtti is careful that the "
            "whole lengthening is being prescribed here and "
            "not only its accent — **प्लुतोऽप्य् अत्र "
            "विधीयते, न गुणमात्रम्**"),
    Plu(
        "8.2.102", does="pluta", accent="anudātta",
        of=("upari-svid-āsīt",),
        why="उपरिस्विदासीदिति च — and in उपरि स्विद् आसीत्: "
            "**अधः स्विद् आसी३द् उपरि स्विद् आसी३त्**. The two "
            "halves of the same Vedic line take two different "
            "accents — **अधः स्विद् आसीद् इत्यत्र 8.2.97 "
            "इत्य् उदात्तः प्लुतः**, the deliberation rule "
            "giving the first a high tone, and this sūtra "
            "giving the second a low one"),
    Plu(
        "8.2.103", does="pluta", accent="svarita",
        gana="āmreḍita-pūrva",
        sense=("asūyā", "sammati", "kopa", "kutsana"),
        why="स्वरितमाम्रेडितेऽसूयासम्मतिकोपकुत्सनेषु — and here "
            "the accent changes a second time: the प्लुत before "
            "an आम्रेडित is स्वरित, in envy, approval, anger "
            "or contempt. The doubling is 8.1.8's again, and "
            "the four senses are four of that sūtra's five — "
            "the fifth, threatening, having been given its own "
            "rule with its own accent at 8.2.95"),
    Plu(
        "8.2.104", does="pluta", accent="svarita", gana="tiṅ",
        sense=("kṣiyā", "āśīs", "praiṣa"), position="ākāṅkṣa",
        why="क्षियाऽऽशीःप्रैषेषु तिङ् आकाङ्क्षम् — and a finite "
            "verb that leaves something expected, where a "
            "breach of custom, a blessing or a summons is "
            "meant: **क्षिया आचारभेदः, आशीः प्रार्थनाविशेषः, "
            "शब्देन व्यापारणं प्रैषः**. This is the rule "
            "8.1.60's example needed — स्वयं ह रथेन याति३, "
            "उपाध्यायं पदातिं गमयति — where the first verb "
            "keeps its accent by that sūtra and takes its "
            "प्लुत by this one"),
    Plu(
        "8.2.105", does="pluta", accent="svarita",
        position="anantya", sense=("praśna", "ākhyāna",),
        why="अनन्त्यस्यापि प्रश्नाख्यानयोः — and in a QUESTION "
            "and its ANSWER even a word that does not stand "
            "last takes it: **अगम३ः पूर्वा३न् ग्रामा३न् "
            "अग्निभूता३इ, पटा३उ**. **सर्वेषाम् एव पदानाम् एष "
            "स्वरितः प्लुतः** — every word in the sentence, "
            "and the last one alone takes the अनुदात्त of "
            "8.2.100 instead. One sentence, two accents, and "
            "the two sūtras five apart"),
    Plu(
        "8.2.106", does="id-ut", gana="aic",
        why="प्लुतावैच इदुतौ — where an ऐ or औ is to be "
            "lengthened, it is the इ or उ INSIDE it that is: "
            "**ऐ३तिकायन; औ३पमन्यव**. **यद् एवर्णोवर्णयोर् "
            "अवर्णस्य च समविभागः, तद् एदुतौ द्विमात्रौ अनेन "
            "प्लुतौ क्रियेते** — the diphthong is halved, and "
            "the second half is what carries the three mātrās. "
            "So the lengthening lands inside a vowel rather "
            "than on it"),
    Plu(
        "8.2.107", does="ā-id-ut", gana="ec-a-pragṛhya",
        keeps_out="the दूराद्धूत of 8.2.84, which the sūtra "
                  "excepts by name",
        why="एचोऽप्रगृह्यस्यादूराद्धूते पूर्वस्यार्धस्यादुत्तर"
            "स्येदुतौ — a non-प्रगृह्य ए or ओ that is to be "
            "lengthened splits: the FIRST half becomes a प्लुत "
            "आ and the second an इ or उ. अग्ने gives **अग्ना३इ** "
            "and पटो gives **पटा३उ**. A vārttika lists where it "
            "holds — **प्रश्नान्ताभिपूजितविचार्यमाणप्रत्यभिवाद"
            "याज्यान्तेषु इति वक्तव्यम्** — five settings, "
            "which is why the deliberating sentences of "
            "8.2.97 all end in that इ"),
    Plu(
        "8.2.108", does="ya-va", gana="id-ut",
        position="ac-para",
        why="तयोर्य्वावचि संहितायाम् — and those इ and उ become "
            "य् and व् before a vowel, in संहिता: **अग्ना३याशा; "
            "पटा३वाशा; अग्ना३यिन्द्रम्; पटा३वुदकम्**.\\n\\n"
            "**AND THE SŪTRA'S LAST WORD OPENS A HEADING THAT "
            "RUNS TO THE END OF THE WORK.** **संहितायाम् "
            "इत्येतच् च अधिकृतम्। इत उत्तरम् आध्यायपरिसमाप्तेर् "
            "यद् वक्ष्यामः संहितायाम् इत्येवं तद् वेदितव्यम्** "
            "— everything in 8.3 and 8.4 is said of sounds in "
            "close juncture, and no sūtra of those two pādas "
            "has to say so"),
)


def _reaches(row: Plu, word: str, gana: str, sense: str,
             position: str, view: str) -> bool:
    # A heading answers nothing: 8.2.82 is stated of every rule
    # after it and of none in particular.
    if row.heading:
        return False
    if row.of and word not in row.of:
        return False
    if row.gana and gana != row.gana:
        return False
    if row.sense and sense not in row.sense:
        return False
    if row.position and position != row.position:
        return False
    if row.view and view != row.view:
        return False
    return True


def _how_specific(row: Plu) -> int:
    """
    A rule that displaces another beats it, a named word beats
    a shape, and a named sense beats both.

    8.2.97 against 8.2.98 is what needs the displacer: the same
    deliberation lengthens every alternative in the Veda and
    only the first in the spoken language.
    """
    return (
        12 * len(row.blocks)
        + 8 * bool(row.of)
        + 6 * len(row.sense)
        + 4 * bool(row.gana)
        + 3 * bool(row.position)
        + 2 * bool(row.view)
    )


@dataclass(frozen=True)
class Lengthened:
    """What the run answers: a प्लुत, and the accent it takes."""

    does: str
    sutra: str
    why: str
    #: The heading's उदात्त unless a rule says otherwise.
    accent: str = "udātta"
    optional: bool = False
    view: str = ""
    blocked_by: Tuple[str, ...] = ()


def the_pluta(word: str = "", *, gana: str = "", sense: str = "",
              position: str = "", view: str = "") -> Lengthened:
    """
    8.2.82–108 — where the प्लुत comes and what accent it takes.

    Nothing answers by default, and the accent of whatever does
    is the heading's उदात्त unless the rule names another.
    """
    matched = [
        row for row in PLUTA_TABLE
        if _reaches(row, word, gana, sense, position, view)
    ]
    if not matched:
        return Lengthened(
            "", "", "No rule of 8.2.82-108 is reached, so no "
                    "vowel is lengthened", accent="")
    row = max(matched, key=_how_specific)
    return Lengthened(row.does, row.sutra, row.why,
                      accent=row.accent or "udātta",
                      optional=row.optional, view=row.view,
                      blocked_by=row.blocks)


def provisions_for(sutra_id: str) -> Tuple[Plu, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in PLUTA_TABLE
                 if row.sutra == sutra_id)


__all__ = [
    "Plu", "PLUTA_TABLE", "PLUTA_RUN", "ADHIKARA_TO",
    "SAMHITA_TO", "BRUHI_FIVE", "ANUDATTA_THREE",
    "SVARITA_THREE",
    "Lengthened", "the_pluta", "provisions_for",
]
