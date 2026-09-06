# -*- coding: utf-8 -*-
"""
८.१.१६–५० — पदस्य, पदात्, and the finite verb's lost accent.

Three headings open one after another and none of them ends in
this pāda. 8.1.16 **पदस्य** runs to 8.3.55, 8.1.17 **पदात्** to
8.1.68, and 8.1.18 **अनुदात्तं सर्वम् अपादादौ** to the end of
the pāda — and the third carries THREE words down at once:
**अनुदात्तम् इति च, सर्वम् इति च, अपादादाव् इति च। एतत् त्रयम्
अधिकृतं वेदितव्यम् आ पादपरिसमाप्तेः**.

**AND THEN COMES THE RULE THE WHOLE SPOKEN LANGUAGE TURNS ON.**
8.1.28 **तिङ्ङतिङः** — a finite verb after a word that is not a
finite verb loses its accent altogether: देवदत्तः पचति, with
पचति toneless. Almost everything from 8.1.29 to 8.1.66 exists to
keep that off: the periphrastic future keeps its accent (8.1.29
श्वः कर्ता), and so does a verb construed with any of some
thirty particles — यत्, यदि, हन्त, कुवित्, नेत्, चेत्, चण्,
कच्चित्, यत्र (8.1.30), नह in remonstrance (8.1.31), सत्यम् in
a question (8.1.32), अङ्ग and हि where nothing contrary is meant
(8.1.33–34), यावत् and यथा (8.1.36), तु, पश्य, पश्यत, अह and
अहो in praise (8.1.39–40), पुरा of haste (8.1.42), ननु of asking
leave (8.1.43), किम् in a question about an action (8.1.44),
एहि मन्ये in jest (8.1.46), जातु with nothing before it (8.1.47),
a किम्-form with चित् after it (8.1.48), and आहो and उताहो
(8.1.49).

**AND TWO SŪTRAS REFUSE THE REFUSAL.** 8.1.37 **पूजायां न
अनन्तरम्** and 8.1.38 **उपसर्गव्यपेतं च** take 8.1.36 back where
the sense is praise, and the vṛtti has to spell out that a
double negative here is an assertion: **न अनुदात्तं न भवति। किं
तर्हि? अनुदात्तम् एव** — यावत् पचति शोभनम्, with पचति toneless
after all.

**AND FOUR SŪTRAS REPLACE युष्मद् AND अस्मद् OUTRIGHT.**
8.1.20–23 give the enclitic वाम्, नौ, वस्, नस्, ते, मे, त्वा and
मा — and every one of them is toneless, which is what the
heading supplies and no rule of the four has to say.

**WHAT THIS MODULE DOES NOT DO.** It says which word loses its
accent. What accent it had is 6.1's, and the compound's own is
6.2's. 8.1.51 opens the next module and 8.1.16's own heading
runs on into 8.2 and 8.3.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: This module's stretch.
NIGHATA_RUN: Tuple[str, str] = ("8.1.16", "8.1.50")

#: 8.1.16 पदस्य reaches all the way to 8.3.55.
PADASYA_TO: str = "8.3.55"

#: 8.1.17 पदात् stops at 8.1.68 कुत्सने च सुप्यगोत्रादौ.
PADAT_TO: str = "8.1.68"

#: 8.1.18's three words run to the end of the pāda.
APADADAU_TO: str = "8.1.74"

#: The rule the rest of the pāda is stated against.
THE_NIGHATA: str = "8.1.28"

#: 8.1.24's five, which keep the enclitics off.
CA_VA_FIVE: Tuple[str, ...] = ("ca", "vā", "ha", "aha", "eva")

#: 8.1.30's nine particles, which keep the निघात off.
NIPATA_NINE: Tuple[str, ...] = (
    "yat", "yadi", "hanta", "kuvit", "net", "cet", "caṇ",
    "kaccit", "yatra")

#: 8.1.39's four, which do it in praise.
PUJA_FOUR: Tuple[str, ...] = ("tu", "paśya", "paśyata", "aha")


@dataclass(frozen=True)
class Nighata:
    """One rule of 8.1.16–50: an accent lost, kept, or replaced."""

    sutra: str
    #: `anudātta`, `vām-nau`, `vas-nas`, `te-me`, `tvā-mā`.
    does: str = ""
    #: The word class the rule speaks of: `tiṅ`, `āmantrita`,
    #: `luṭ`, `lṛṭ`, `yuṣmad-asmad`, `gotrādi`, `kiṃvṛtta`. No
    #: rule of this run names an individual word — what looks
    #: like a list is always a list of what the word is
    #: CONSTRUED WITH, which is the `joined` column.
    gana: str = ""
    #: What must stand before.
    after: str = ""
    #: The particle or word it must be construed with. This is
    #: the column almost every refusal of the run turns on.
    joined: Tuple[str, ...] = ()
    #: The case and number, for the four enclitic rules.
    case: str = ""
    sense: Tuple[str, ...] = ()
    #: Where in the sentence, or how far from what it is
    #: construed with: `a-pādādi`, `anantara`,
    #: `upasarga-vyapeta`, `a-pūrva`.
    position: str = ""
    #: True of a rule that only opens a heading.
    heading: bool = False
    #: True where the sūtra only keeps another rule off.
    refuses: bool = False
    optional: bool = False
    chandasi: bool = False
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


NIGHATA_TABLE: Tuple[Nighata, ...] = (
    Nighata(
        "8.1.16", heading=True,
        why="पदस्य — a heading, and the longest of the three "
            "this pāda opens: **पदस्येत्ययम् अधिकारः प्राग् "
            "अपदान्ताधिकारात्**, running from here to 8.3.55. "
            "What is said from here on is said OF A WORD and "
            "not of a stem or an affix — **वक्ष्यति संयोगान्तस्य "
            "लोपः, पचन्, यजन्; पदस्येति किम्? पचन्तौ, "
            "यजन्तौ**.\\n\\n"
            "**AND THE GENITIVE IN IT IS READ TWO WAYS.** "
            "**वक्ष्यमाणवाक्यापेक्षया पदस्य अधिकृतस्य "
            "षष्ठ्यर्थव्यवस्था द्रष्टव्या — क्वचित् स्थानषष्ठी "
            "क्वचिद् अवयवषष्ठी** — sometimes it names what a "
            "substitute stands FOR and sometimes the whole a "
            "part belongs to, and which one is settled by the "
            "sūtra that borrows it"),
    Nighata(
        "8.1.17", heading=True,
        why="पदात् — and a second heading over the first: "
            "**पदाद् इत्ययम् अधिकारः प्राक् कुत्सने च "
            "सुप्यगोत्रादौ इत्येतस्मात्**, from here to 8.1.68. "
            "It says what must stand BEFORE — **वक्ष्यति "
            "आमन्त्रितस्य च। आमन्त्रितस्य पदात् परस्य "
            "अनुदात्तादेशो भवति इति। पचसि देवदत्त**. And the "
            "test of it is the same example turned round: "
            "**पदाद् इति किम्? देवदत्त पचसि** — with the "
            "vocative first there is no word in front of it, "
            "and its accent stays"),
    Nighata(
        "8.1.18", heading=True,
        why="अनुदात्तं सर्वम् अपादादौ — the third heading, and "
            "it carries THREE words down at once: "
            "**अनुदात्तम् इति च, सर्वम् इति च, अपादादाव् इति च। "
            "एतत् त्रयम् अधिकृतं वेदितव्यम् आ पादपरिसमाप्तेः** "
            "— toneless, WHOLLY, and not at the head of a "
            "metrical quarter. सर्वम् is why पचसि देवदत्त loses "
            "every syllable's accent and not one; अपादादौ is "
            "why **यत् ते नियानं रजसं मृत्यो अनवधर्ष्यम्** keeps "
            "its own, standing where a quarter begins"),
    Nighata(
        "8.1.19", does="anudātta", gana="āmantrita", after="pada",
        position="a-pādādi",
        keeps_out="देवदत्त पचसि — the vocative stands first, "
                  "and 8.1.17's पदात् is not met",
        why="आमन्त्रितस्य च — a VOCATIVE that stands after a "
            "word, and not at the head of a quarter, is "
            "toneless throughout: **पचसि देवदत्त; पचसि "
            "यज्ञदत्त**. It is stated against 6.1.198, which "
            "would have given the vocative an accent on its "
            "first syllable — **आमन्त्रिताद्युदात्तत्वे "
            "प्राप्ते वचनम्**.\\n\\n"
            "**AND A VĀRTTIKA CONFINES IT TO ONE SENTENCE.** "
            "**समानवाक्ये निघातयुष्मदस्मदादेशा वक्तव्याः** — "
            "the toneless vocative, and the enclitics of the "
            "four sūtras after, want the two words in ONE "
            "sentence. **ओदनं पच तव भविष्यति** keeps तव, the "
            "two clauses being separate; **इह देवदत्त माता ते "
            "कथयति** takes the enclitic, being one"),
    Nighata(
        "8.1.20", does="vām-nau", gana="yuṣmad-asmad",
        case="dvivacana", after="pada", position="a-pādādi",
        why="युष्मदस्मदोः षष्ठीचतुर्थीद्वितीयास्थयोर्वान्नावौ — "
            "युष्मद् and अस्मद् standing in the genitive, dative "
            "or accusative DUAL become वाम् and नौ, one to one: "
            "**ग्रामो वां स्वम्; जनपदो नौ स्वम्; ग्रामो वां "
            "दीयते; ग्रामो वां पश्यति**. The two are toneless "
            "because 8.1.18 says so, and the sūtra does not "
            "have to. **एकवचनबहुवचनान्तयोर् आदेशान्तरविधानाद् "
            "द्विवचनान्तयोर् एतौ आदेशौ विज्ञायेते** — the "
            "singular and the plural get substitutes of their "
            "own in the next two sūtras, and that is how the "
            "dual is known to be meant here"),
    Nighata(
        "8.1.21", does="vas-nas", gana="yuṣmad-asmad",
        case="bahuvacana", after="pada", position="a-pādādi",
        why="बहुवचने वस्नसौ — and in the PLURAL they become "
            "वस् and नस्: **ग्रामो वः स्वम्; जनपदो नः स्वम्; "
            "ग्रामो वो दीयते; ग्रामो वः पश्यति**. All three "
            "cases again, and the accent again from the heading "
            "rather than from the rule"),
    Nighata(
        "8.1.22", does="te-me", gana="yuṣmad-asmad",
        case="ekavacana", after="pada", position="a-pādādi",
        why="ते मयावेकवचनस्य — and in the SINGULAR ते and मे, "
            "but only in the genitive and dative: **ग्रामस् ते "
            "स्वम्; ग्रामो मे स्वम्; ग्रामस् ते दीयते**. The "
            "accusative is left out, and the reason is that the "
            "next sūtra gives it something else — "
            "**द्वितीयान्तस्य आदेशान्तरविधानसामर्थ्यात् "
            "षष्ठीचतुर्थ्योर् एव अयं योगः**"),
    Nighata(
        "8.1.23", does="tvā-mā", gana="yuṣmad-asmad",
        case="ekavacana-dvitīyā", after="pada",
        position="a-pādādi",
        why="त्वामौ द्वितीयायाः — and in the singular ACCUSATIVE "
            "त्वा and मा: **ग्रामस् त्वा पश्यति; ग्रामो मा "
            "पश्यति**. एकवचनस्य is carried down from the sūtra "
            "before, so the whole of what युष्मद् and अस्मद् do "
            "in these three cases is said in four sūtras and "
            "eight substitutes"),
    Nighata(
        "8.1.24", refuses=True, joined=CA_VA_FIVE,
        gana="yuṣmad-asmad", after="pada",
        blocks=("8.1.20", "8.1.21", "8.1.22", "8.1.23"),
        why="न चवाहाहैवयुक्ते — but NOT where the word is "
            "construed with च, वा, ह, अह or एव: **ग्रामस् तव च "
            "स्वम्; ग्रामो मम च स्वम्; युष्माकं च स्वम्; ग्रामस् "
            "तुभ्यं च दीयते**. **पूर्वेण प्रकरणेन प्राप्ताः "
            "प्रतिषिध्यन्ते** — the four rules before had "
            "supplied the enclitics and this takes all four "
            "back at once. The list is the one 8.1.58 and "
            "8.1.63 later call चादि"),
    Nighata(
        "8.1.25", refuses=True, gana="yuṣmad-asmad",
        after="pada", joined=("paśyārtha",),
        blocks=("8.1.20", "8.1.21", "8.1.22", "8.1.23"),
        why="पश्यार्थैश्च अनालोचने — nor where it is construed "
            "with a verb of SEEING used of knowing and not of "
            "the eye: **ग्रामस् तव स्वं समीक्ष्य आगतः; ग्रामस् "
            "त्वां समीक्ष्य आगतः**. The vṛtti splits the two "
            "senses in a line — **दर्शनं ज्ञानम्। आलोचनं "
            "चक्षुर्विज्ञानम्** — and the refusal is for the "
            "first, so that a सम्+ईक्ष् of thinking keeps तव "
            "and one of looking does not"),
    Nighata(
        "8.1.26", refuses=True, gana="yuṣmad-asmad",
        after="sa-pūrvā-prathamā", optional=True,
        blocks=("8.1.20", "8.1.21", "8.1.22", "8.1.23"),
        why="सपूर्वायाः प्रथमाया विभाषा — and OPTIONALLY after "
            "a nominative that has a word before it: **ग्रामे "
            "कम्बलस् ते स्वम्, ग्रामे कम्बलस् तव स्वम्; ग्रामे "
            "छात्रास् त्वा पश्यन्ति**. Both forms stand, and "
            "what makes the option available at all is the "
            "word before the nominative — a bare प्रथमा leaves "
            "the enclitic compulsory"),
    Nighata(
        "8.1.27", does="anudātta", gana="gotrādi", after="tiṅ",
        sense=("kutsana", "ābhīkṣṇya"),
        why="तिङो गोत्रादीनि कुत्सनाभीक्ष्ण्ययोः — the words of "
            "the गोत्रादि class, standing after a finite verb, "
            "are toneless in the sense of CONTEMPT or of "
            "REPETITION: **पचति गोत्रम्; जल्पति गोत्रम्; "
            "पचतिपचति गोत्रम्**, and with ब्रुवम् for गोत्रम् "
            "likewise. The doubled verb in the second set is "
            "8.1.4's, so the two runs of this pāda meet in one "
            "example. **ब्रुवः इति ब्रुवः कन् निपातनात्** — the "
            "form is laid down with its own affix"),
    Nighata(
        "8.1.28", does="anudātta", gana="tiṅ", after="a-tiṅ",
        keeps_out="नीलम् उत्पलम्, शुक्लं वस्त्रम् — neither word "
                  "is a finite verb; भवति पचति — what precedes "
                  "IS one",
        why="तिङ्ङतिङः — **THE NIGHĀTA.** A finite verb standing "
            "after a word that is NOT a finite verb loses its "
            "accent altogether: **देवदत्तः पचति; यज्ञदत्तः "
            "पचति**, with पचति toneless throughout.\\n\\n"
            "**AND IT IS THE RULE THE REST OF THE PĀDA IS "
            "STATED AGAINST.** From 8.1.29 to 8.1.66 almost "
            "every sūtra is a प्रतिषेध of this one — a list of "
            "particles, senses and positions in which the verb "
            "keeps what it had. Both words of the sūtra are "
            "tested and both do work: **तिङ् इति किम्? नीलम् "
            "उत्पलम्; अतिङः इति किम्? भवति पचति**, where the "
            "first word is itself a verb and the second is "
            "spared"),
    Nighata(
        "8.1.29", refuses=True, gana="luṭ", after="a-tiṅ",
        blocks=("8.1.28",),
        why="न लुट् — but the periphrastic future keeps its "
            "accent: **श्वः कर्ता; श्वः कर्तारौ; मासेन "
            "कर्तारः**. **पूर्वेण अतिप्रसक्ते प्रतिषेध "
            "आरभ्यते** — the rule before had reached too far "
            "and this pulls it back.\\n\\n"
            "**AND THE VṚTTI SAYS WHERE THE ACCENT THEN SITS.** "
            "**तासेः परस्य लसार्वधातुकस्य अनुदात्तत्वे सति "
            "सर्वतासिर् एव उदात्तः। यत्र तु टिलोपः, तत्र "
            "उदात्तनिवृत्तिस्वरो भवति** — with the ending "
            "toneless the तास् carries the whole accent, and "
            "where the ending is lost outright the accent "
            "falls back by 6.1.161"),
    Nighata(
        "8.1.30", refuses=True, gana="tiṅ", after="a-tiṅ",
        joined=NIPATA_NINE, blocks=("8.1.28",),
        why="निपातैर्यद्यदिहन्तकुविन्नेच्चेच्चण्कच्चिद्यत्र"
            "युक्तम् — nor a verb construed with any of NINE "
            "particles: **यत् करोति; यदि पचति; हन्त करोति; "
            "कुवित् करोति; नेज् जिह्मायन्त्यो नरके पताम; स चेद् "
            "भुङ्क्ते; कच्चित् पचति; यत्र पचति**. This is the "
            "longest single list of the run and the one later "
            "sūtras keep pointing back to — 8.1.54 has to say "
            "that हन्त's refusal here is compulsory while its "
            "own is optional"),
    Nighata(
        "8.1.31", refuses=True, gana="tiṅ", after="a-tiṅ",
        joined=("naha",), sense=("pratyārambha",),
        blocks=("8.1.28",),
        keeps_out="नह वै तस्मिन् अमुष्मिन् लोके दक्षिणाम् "
                  "इच्छन्ति — नह in its plain sense",
        why="नह प्रत्यारम्भे — nor with नह in REMONSTRANCE: "
            "**नह भोक्ष्यसे; नह अध्येष्यसे**. The sense is "
            "defined for the occasion — **चोदितस्य अवधीरणे "
            "उपालिप्सया प्रतिषेधयुक्तः प्रत्यारम्भः क्रियते** "
            "— one who has been urged to something brushes it "
            "aside, and the speaker takes him up on it"),
    Nighata(
        "8.1.32", refuses=True, gana="tiṅ", after="a-tiṅ",
        joined=("satyam",), sense=("praśna",), blocks=("8.1.28",),
        keeps_out="सत्यं वक्ष्यामि नानृतम् — a statement and "
                  "not a question",
        why="सत्यं प्रश्ने — nor with सत्यम् in a QUESTION: "
            "**सत्यं भोक्ष्यसे? सत्यम् अध्येष्यसे?** The same "
            "word in a statement leaves the verb toneless, and "
            "the vṛtti's counter-example is a whole line of the "
            "Atharvan to make the difference audible"),
    Nighata(
        "8.1.33", refuses=True, gana="tiṅ", after="a-tiṅ",
        joined=("aṅga",), sense=("aprātilomya",),
        blocks=("8.1.28",),
        keeps_out="अङ्ग कूज३ वृषल, इदानीं ज्ञास्यसि जाल्म — the "
                  "cooing is unwelcome, and the speaker is "
                  "contrary",
        why="अङ्गाप्रातिलोम्ये — nor with अङ्ग where nothing "
            "CONTRARY is meant: **अङ्ग कुरु; अङ्ग पच; अङ्ग "
            "पठ**. Where the speaker is set against what he "
            "names — **कूजनम् अनभिमतम् असौ कुर्वन् प्रतिलोमो "
            "भवति** — the refusal lapses and 8.1.28 has its way"),
    Nighata(
        "8.1.34", refuses=True, gana="tiṅ", after="a-tiṅ",
        joined=("hi",), sense=("aprātilomya",),
        blocks=("8.1.28",),
        why="हि च — and with हि, under the same condition: **स "
            "हि कुरु; स हि पच; स हि पठ**, and **अप्रातिलोम्ये "
            "इत्येव — स हि कूज३ वृषल**. The sense is carried "
            "down from the sūtra before rather than said again, "
            "which is what makes the pair one rule in two parts"),
    Nighata(
        "8.1.35", refuses=True, gana="tiṅ", after="a-tiṅ",
        joined=("hi",), chandasi=True, blocks=("8.1.28",),
        why="छन्दस्यनेकम् अपि साकाङ्क्षम् — and in the Veda MORE "
            "THAN ONE verb construed with हि keeps its accent, "
            "if the sense is still expectant: **कदाचिद् एकं "
            "कदाचिद् अनेकम् इत्यर्थः**. Two together — "
            "**अनृतं हि मत्तो वदति, पाप्मा एनं विपुनाति**, "
            "neither toneless; and one only — **अग्निर् हि "
            "पूर्वम् उदजयत्, तम् इन्द्रोऽनूदजयत्**, where both "
            "verbs stand with हि and the second is toneless all "
            "the same"),
    Nighata(
        "8.1.36", refuses=True, gana="tiṅ", after="a-tiṅ",
        joined=("yāvat", "yathā"), blocks=("8.1.28",),
        why="यावद्यथाभ्याम् — nor with यावत् or यथा: **यावद् "
            "भुङ्क्ते; यथा भुङ्क्ते; यावद् अधीते; यथा अधीते**. "
            "And the particle need not come first — "
            "**परेण अपि योगे भवति प्रतिषेधः; देवदत्तः पचति "
            "यावत्; देवदत्तः पचति यथा** — which is why the two "
            "sūtras after it have to say ANANTARA to get the "
            "refusal back"),
    Nighata(
        "8.1.37", does="anudātta", gana="tiṅ", after="a-tiṅ",
        joined=("yāvat", "yathā"), sense=("pūjā",),
        position="anantara", blocks=("8.1.36",),
        keeps_out="यावद् देवदत्तः पचति शोभनम् — a word stands "
                  "between, and अनन्तरम् is not met",
        why="पूजायां न अनन्तरम् — but where the sense is PRAISE "
            "and the verb stands NEXT to यावत् or यथा, the "
            "refusal lapses: **यावत् पचति शोभनम्; यथा करोति "
            "चारु**, with the verb toneless after all.\\n\\n"
            "**AND THE VṚTTI HAS TO SPELL OUT THE DOUBLE "
            "NEGATIVE.** **न अनुदात्तं न भवति। किं तर्हि? "
            "अनुदात्तम् एव** — it is not that it fails to be "
            "toneless; it is toneless. A refusal of a refusal "
            "is an assertion, and the commentary will not let "
            "the reader take it for anything else"),
    Nighata(
        "8.1.38", does="anudātta", gana="tiṅ", after="a-tiṅ",
        joined=("yāvat", "yathā"), sense=("pūjā",),
        position="upasarga-vyapeta", blocks=("8.1.36",),
        why="उपसर्गव्यपेतं च — and where only a PREVERB stands "
            "between: **यावत् प्रपचति शोभनम्; यथा प्रकरोति "
            "चारु**. **पूर्वम् अनन्तरम् इत्युक्तम्, "
            "उपसर्गव्यवधानार्थोऽयम् आरम्भः** — the sūtra exists "
            "for the gap a preverb makes and for nothing else, "
            "and a full word in the gap still stops it: "
            "**यावद् देवदत्तः प्रपचति शोभनम्**"),
    Nighata(
        "8.1.39", refuses=True, gana="tiṅ", after="a-tiṅ",
        joined=PUJA_FOUR, sense=("pūjā",), blocks=("8.1.28",),
        keeps_out="पश्य मृगो धावति — seeing and not praising",
        why="तुपश्यपश्यताहैः पूजायाम् — nor with तु, पश्य, "
            "पश्यत or अह where the sense is PRAISE: **माणवकस् "
            "तु भुङ्क्ते शोभनम्; पश्य माणवको भुङ्क्ते शोभनम्; "
            "अह माणवको भुङ्क्ते शोभनम्**.\\n\\n"
            "**AND पूजायाम् IS SAID TWICE OVER ON PURPOSE.** "
            "**पूजायाम् इति वर्तमाने पुनः पूजायाम् इत्युच्यते "
            "निघातप्रतिषेधार्थम्** — the word was already "
            "running down from 8.1.37, where it belonged to an "
            "assertion; saying it again here attaches it to a "
            "refusal instead"),
    Nighata(
        "8.1.40", refuses=True, gana="tiṅ", after="a-tiṅ",
        joined=("aho",), sense=("pūjā",), blocks=("8.1.28",),
        why="अहो च — and with अहो in praise: **अहो देवदत्तः "
            "पचति शोभनम्; अहो विष्णुमित्रः करोति चारु**. "
            "**पृथग्योगकरणम् उत्तरार्थम्** — it is a separate "
            "sūtra only so that the next one can take अहो up "
            "again in every OTHER sense"),
    Nighata(
        "8.1.41", refuses=True, gana="tiṅ", after="a-tiṅ",
        joined=("aho",), sense=("śeṣa",), optional=True,
        blocks=("8.1.28",),
        why="शेषे विभाषा — and with अहो in any sense BUT praise, "
            "optionally: **कटम् अहो करिष्यसि; मम गेहम् अहो "
            "एष्यसि** — **असूयावचनम् एतत्**, said in spite. "
            "**कश् च शेषः? यद् अन्यत् पूजायाः**. The vṛtti "
            "notes that शेष did not strictly have to be said "
            "at all, praise having stopped with the sūtra "
            "before — **अनधिकारे सिद्धे शेषवचनं "
            "विस्पष्टार्थम्**, it is there for clarity"),
    Nighata(
        "8.1.42", refuses=True, gana="tiṅ", after="a-tiṅ",
        joined=("purā",), sense=("parīpsā",), optional=True,
        blocks=("8.1.28",),
        keeps_out="नडेन स्म पुरा अधीयते — पुरा of a distant "
                  "past, where the particle marks distance and "
                  "not haste",
        why="पुरा च परीप्सायाम् — and with पुरा where HASTE is "
            "meant, optionally: **परीप्सा त्वरा। अधीष्व माणवक, "
            "पुरा विद्योतते विद्युत्; पुरा स्तनयति "
            "स्तनयित्नुः** — study, boy, before the lightning "
            "flashes. **पुराशब्दोऽत्र भविष्यदासत्तिं "
            "द्योतयति** — the word points at something close "
            "ahead, which is the opposite of what it usually "
            "does"),
    Nighata(
        "8.1.43", refuses=True, gana="tiṅ", after="a-tiṅ",
        joined=("nanu",), sense=("anujñaiṣaṇā",),
        blocks=("8.1.28",),
        keeps_out="अकार्षीः कटं देवदत्त? ननु करोमि भोः — an "
                  "answer to a question and not a request",
        why="नन्वित्यनुज्ञैषणायाम् — and with ननु where LEAVE "
            "is being asked: **ननु करोमि भोः; ननु गच्छामि "
            "भोः** — **अनुजानीष्व मां करणं प्रति इत्यर्थः**, "
            "let me do it. **अनुज्ञायाः एषणा प्रार्थना "
            "अनुज्ञैषणा**. The same words answering a question "
            "leave the verb toneless"),
    Nighata(
        "8.1.44", refuses=True, gana="tiṅ", after="a-tiṅ",
        joined=("kim",), sense=("kriyāpraśna",),
        position="anupasarga-apratiṣiddha", blocks=("8.1.28",),
        why="किं क्रियाप्रश्नेऽनुपसर्गम् अप्रतिषिद्धम् — and "
            "with किम् in a question ABOUT AN ACTION, where the "
            "verb has no preverb and no other refusal has "
            "already reached it: **किं देवदत्तः पचति, आहोस्विद् "
            "भुङ्क्ते? किं देवदत्तः शेते, आहोस्विद् अधीते?**\\n\\n"
            "**AND THE VṚTTI RECORDS A DISAGREEMENT ABOUT THE "
            "SECOND VERB.** **अत्र केचिद् आहुः — पूर्वं "
            "किंयुक्तम् इति तद् न निहन्यते, उत्तरं तु न "
            "किंयुक्तम् इति तद् निहन्यत एव इति। अपरे तु "
            "आहुः** — one party spares only the verb the किम् "
            "actually stands with, another spares both, and the "
            "Kāśikā reports the two and settles neither"),
    Nighata(
        "8.1.45", refuses=True, gana="tiṅ", after="a-tiṅ",
        joined=("kim-lopa",), sense=("kriyāpraśna",),
        position="anupasarga-apratiṣiddha", optional=True,
        blocks=("8.1.28",),
        why="लोपे विभाषा — and optionally where the किम् is "
            "there in sense but not in sound: **क्व च अस्य "
            "लोपः? यत्र गम्यते च अर्थः, न च प्रयुज्यते "
            "किंशब्दः** — **देवदत्तः पचति, आहोस्वित् पठति**, a "
            "question with no interrogative in it. "
            "**प्राप्तविभाषा इयं किमर्थेन योगात्** — the option "
            "is of something already available, since the "
            "SENSE of किम् is present"),
    Nighata(
        "8.1.46", refuses=True, gana="lṛṭ", after="a-tiṅ",
        joined=("ehi-manye",), sense=("prahāsa",),
        blocks=("8.1.28",),
        keeps_out="एहि मन्यस ओदनं भोक्ष्य इति — मन्यसे and not "
                  "मन्ये, where the jest is absent",
        why="एहिमन्ये प्रहासे लृट् — and a FUTURE construed with "
            "एहि मन्ये in JEST: **प्रकृष्टो हासः प्रहासः, "
            "क्रीडा**. **एहि मन्ये ओदनं भोक्ष्यसे, नहि "
            "भोक्ष्यसे, भुक्तः सोऽतिथिभिः** — come, you think "
            "you will eat the rice; you will not, the guests "
            "have eaten it. The whole idiom is one the rule "
            "exists to keep audible"),
    Nighata(
        "8.1.47", refuses=True, gana="tiṅ", after="a-tiṅ",
        joined=("jātu",), position="a-pūrva", blocks=("8.1.28",),
        keeps_out="कटं जातु करिष्यति — a word stands before "
                  "जातु, and अपूर्वम् is not met",
        why="जात्वपूर्वम् — and with जातु, provided nothing "
            "stands before it: **जातु भोक्ष्यसे; जातु "
            "करिष्यामि**. **अपूर्वम् इति किम्? कटं जातु "
            "करिष्यति** — with a word in front, the verb is "
            "toneless as usual. The condition is about the "
            "PARTICLE's place in the sentence and not the "
            "verb's, which is what makes it worth a column"),
    Nighata(
        "8.1.48", refuses=True, gana="kiṃvṛtta", after="a-tiṅ",
        joined=("cit",), position="a-pūrva", blocks=("8.1.28",),
        why="किम्वृत्तं च चिदुत्तरम् — and a किम्-form with "
            "चित् after it and nothing before it: **कश्चिद् "
            "भुङ्क्ते; कश्चिद् भोजयति; कस्मैचिद् ददाति; "
            "कतरश्चित् करोति; कतमश्चिद् भुङ्क्ते**. "
            "**किम्वृत्तग्रहणेन तद्विभक्त्यन्तं प्रतीयात्, "
            "डतरडतमौ च प्रत्ययौ** — the name covers किम् in "
            "any case AND the stems made from it with डतर and "
            "डतम, which is why कतरश्चित् is in the list"),
    Nighata(
        "8.1.49", refuses=True, gana="tiṅ", after="a-tiṅ",
        joined=("āho", "utāho"), position="anantara-a-pūrva",
        blocks=("8.1.28",),
        keeps_out="देवदत्त आहो भुङ्क्ते — a word stands before "
                  "आहो, and अपूर्वम् is not met",
        why="आहो उताहो चानन्तरम् — and with आहो or उताहो, where "
            "the verb stands NEXT to the particle and nothing "
            "stands before it: **आहो भुङ्क्ते; उताहो भुङ्क्ते; "
            "आहो पठति**. Both conditions come from elsewhere — "
            "अनन्तरम् is the sūtra's own word and अपूर्वम् is "
            "carried down from 8.1.47, two sūtras back"),
    Nighata(
        "8.1.50", refuses=True, gana="tiṅ", after="a-tiṅ",
        joined=("āho", "utāho"), optional=True,
        blocks=("8.1.28",),
        why="शेषे विभाषा — and elsewhere, optionally: "
            "**कश् च शेषः? यद् अन्यद् अनन्तरात्** — where a "
            "word stands between. **आहो देवदत्तः पचति** beside "
            "**आहो देवदत्तः पचति** with the verb toneless; "
            "**उताहो देवदत्तः पठति** likewise. It is the second "
            "शेषे विभाषा of the pāda, the first being 8.1.41's, "
            "and each takes back what the sūtra just before it "
            "had confined"),
)


def _reaches(row: Nighata, gana: str, after: str, joined: str,
             case: str, sense: str, position: str,
             chandasi: bool) -> bool:
    # A heading is stated of everything after it and of nothing
    # in particular. 8.1.16, 8.1.17 and 8.1.18 answer nothing.
    if row.heading:
        return False
    if row.gana and gana != row.gana:
        return False
    if row.after and after != row.after:
        return False
    if row.joined and joined not in row.joined:
        return False
    if row.case and case != row.case:
        return False
    if row.sense and sense not in row.sense:
        return False
    if row.position and position != row.position:
        return False
    if row.chandasi and not chandasi:
        return False
    return True


def _how_specific(row: Nighata) -> int:
    """
    A refusal outweighs the rule it refuses, and an assertion
    that displaces a refusal outweighs both.

    8.1.37 against 8.1.36 is the pair that needs the last part:
    यावत् पचति शोभनम् is toneless and यावद् भुङ्क्ते is not,
    and the two rules differ only in a sense and a position.
    """
    return (
        12 * len(row.blocks)
        + 6 * len(row.joined)
        + 5 * bool(row.case)
        + 4 * len(row.sense)
        + 4 * bool(row.gana)
        + 3 * bool(row.position)
        + 3 * bool(row.after)
        + 2 * bool(row.chandasi)
    )


@dataclass(frozen=True)
class Toneless:
    """What the run answers: an accent lost, kept, or replaced."""

    does: str
    sutra: str
    why: str
    refuses: bool = False
    optional: bool = False
    blocked_by: Tuple[str, ...] = ()


def after_a_pada(*, gana: str = "", after: str = "",
                 joined: str = "", case: str = "", sense: str = "",
                 position: str = "",
                 chandasi: bool = False) -> Toneless:
    """
    8.1.16–50 — what loses its accent after a word, and what
    keeps it.

    Nothing answers by default. A word none of these rules
    reaches keeps whatever accent अध्याय ६ gave it.
    """
    matched = [
        row for row in NIGHATA_TABLE
        if _reaches(row, gana, after, joined, case, sense,
                    position, chandasi)
    ]
    if not matched:
        return Toneless(
            "", "", "No rule of 8.1.16-50 is reached, so the word "
                    "keeps the accent adhyaya 6 gave it")
    row = max(matched, key=_how_specific)
    return Toneless(row.does, row.sutra, row.why,
                    refuses=row.refuses, optional=row.optional,
                    blocked_by=row.blocks)


def provisions_for(sutra_id: str) -> Tuple[Nighata, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in NIGHATA_TABLE
                 if row.sutra == sutra_id)


__all__ = [
    "Nighata", "NIGHATA_TABLE", "NIGHATA_RUN", "PADASYA_TO",
    "PADAT_TO", "APADADAU_TO", "THE_NIGHATA", "CA_VA_FIVE",
    "NIPATA_NINE", "PUJA_FOUR",
    "Toneless", "after_a_pada", "provisions_for",
]
