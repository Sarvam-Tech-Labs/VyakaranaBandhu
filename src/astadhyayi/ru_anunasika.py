# -*- coding: utf-8 -*-
"""
८.३.१–३३ — the रुँ, the nasal before it, and the anusvāra.

पाद ८.३ opens under 8.2.108's संहितायाम् — everything here is
said of sounds in close juncture — and its own first heading
follows at once. 8.3.2 **अत्रानुनासिकः पूर्वस्य तु वा** is an
अधिकार: from here on, whatever a रुँ replaces, the sound BEFORE
it optionally goes nasal. सँस्स्कर्ता beside संस्स्कर्ता, and
8.3.4 supplies the anusvāra for the half where it does not.

**WHERE THE रुँ COMES.** A मतुप्- or वस्-final word before a
vocative ending in the Veda (8.3.1 मरुत्वः), सम् before सुट्
(8.3.5 सँस्स्कर्ता), पुम् before a खय् (8.3.6 पुंस्कामा), any
न्-final word before a छव् (8.3.7 भवांश्छादयति) — and four Vedic
rules besides, of which 8.3.9 दीर्घादटि समानपादे wants the two
sounds in the SAME metrical quarter, a condition nothing else in
the work states.

**AND THREE TEACHERS ARE NAMED IN FOUR SŪTRAS.** 8.3.17 turns
the रुँ's र् into य् before a vowel — भो अत्र, ब्राह्मणा ददति —
and then 8.3.18 gives Śākaṭāyana a LIGHTER य् (भोयत्र), 8.3.19
gives Śākalya its loss (क आस्ते), and 8.3.20 gives Gārgya the
loss after ओ without an option: **नित्यार्थोऽयम् आरम्भः।
गार्ग्यग्रहणं पूजार्थम्** — the name is an honour and not a
dissent, the same thing 7.3.99 said of Gārgya and Gālava. And
8.3.22 हलि सर्वेषाम् settles that before a consonant every
teacher agrees.

**AND THE ANUSVĀRA.** 8.3.23 मोऽनुस्वारः is the rule every
final म् in the language passes through — कुण्डं हसति — and
8.3.24 extends it to a न् or म् inside a word: पयांसि, यशांसि,
धनूंषि.

**WHAT THIS MODULE DOES NOT DO.** 8.3.15 खरवसानयोर्विसर्जनीयः,
which turns the र् into the visarga one actually hears, was
codified long before this pāda was read and is named in
`CODIFIED_APART`.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: This module's stretch.
RU_RUN: Tuple[str, str] = ("8.3.1", "8.3.33")

#: The heading the whole pāda stands under, opened at the end of
#: पाद ८.२ and running to the end of the adhyāya.
SAMHITA: str = "8.2.108"

#: Codified long before the pāda was read. Nothing here restates
#: it: 8.3.15 खरवसानयोर्विसर्जनीयः.
CODIFIED_APART: Tuple[str, ...] = ("8.3.15",)

#: 8.3.2's heading, which every rule of the run borrows.
ANUNASIKA_FROM: str = "8.3.2"

#: The three teachers named in 8.3.18–20.
TEACHERS: Tuple[str, ...] = ("śākaṭāyana", "śākalya", "gārgya")

#: What the Kāśikā says of the third of them, against the other
#: two: the naming is an honour and not a dissent.
PUJARTHAM: str = "नित्यार्थोऽयम् आरम्भः। गार्ग्यग्रहणं पूजार्थम्"


@dataclass(frozen=True)
class Sandhi:
    """One rule of 8.3.1–33: a रुँ, a nasal, or an augment."""

    sutra: str
    #: `ru`, `anunāsika`, `anusvāra`, `lopa`, `visarjanīya`,
    #: `ya`, `laghu-ya`, `ma`, `na`, `kuk-ṭuk`, `dhuṭ`, `tuk`,
    #: `ṅamuṭ`, `va`.
    does: str = ""
    #: The words named outright.
    of: Tuple[str, ...] = ()
    #: The shape of the word instead.
    gana: str = ""
    #: What must follow.
    before: Tuple[str, ...] = ()
    #: A named teacher's opinion.
    view: str = ""
    #: True of a rule that only opens a heading.
    heading: bool = False
    optional: bool = False
    chandasi: bool = False
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


RU_TABLE: Tuple[Sandhi, ...] = (
    Sandhi(
        "8.3.1", does="ru", gana="matup-vasu-anta",
        before=("sambuddhi",), chandasi=True,
        why="मतुवसो रु सम्बुद्धौ छन्दसि — a मतुप्-final or "
            "वस्-final word takes रुँ before a vocative ending, "
            "in the Veda: **इन्द्र मरुत्व इह पाहि सोमम्; "
            "हरिवो मेदिनं त्वा**. **संहितायाम् इति वर्तते** — "
            "8.2.108's heading is running, and every rule of "
            "this pāda is said of sounds in close juncture"),
    Sandhi(
        "8.3.2", does="anunāsika", heading=True, optional=True,
        why="अत्रानुनासिकः पूर्वस्य तु वा — an अधिकार, and the "
            "first of the pāda's own: **इत उत्तरं यस्य स्थाने "
            "रुर् विधीयते, ततः पूर्वस्य तु वर्णस्य वा अनुनासिको "
            "भवति इत्येतद् अधिकृतं वेदितव्यम्**. Wherever a रुँ "
            "is given from here on, the sound BEFORE it may go "
            "nasal — **सँस्स्कर्ता** beside संस्स्कर्ता — and "
            "8.3.4 gives the other half of that option its "
            "anusvāra instead"),
    Sandhi(
        "8.3.3", does="anunāsika", gana="ā-anta-ru-pūrva",
        before=("aṭ",), blocks=("8.3.2",),
        why="आतोऽटि नित्यम् — but before an अट् the आ before a "
            "रुँ is ALWAYS nasal: **महाँ असि**. 8.3.9 will give "
            "the रुँ there, and the heading would have made the "
            "nasal optional — **ततः पूर्वस्य अतोऽनुनासिकविकल्पे "
            "प्राप्ते नित्यार्थं वचनम्**. So the rule exists "
            "only to take an option away"),
    Sandhi(
        "8.3.4", does="anusvāra", gana="a-anunāsika-ru-pūrva",
        why="अनुनासिकात् परोऽनुस्वारः — and where the sound "
            "before the रुँ has NOT been made nasal, an "
            "anusvāra is put in after it: **संस्स्कर्ता; "
            "संस्कर्ता**. The vṛtti has to supply a word for "
            "the sūtra to be read at all — **अन्यशब्दोऽत्र "
            "अध्याहर्तव्यः**, अनुनासिकाद् अन्यः — so that the "
            "genitive means 'other than a nasalised sound' and "
            "not 'after a nasal'"),
    Sandhi(
        "8.3.5", does="ru", of=("sam",), before=("suṭ",),
        why="समः सुटि — सम् takes रुँ before a सुट्: "
            "**सँस्स्कर्ता, सँस्स्कर्तुम्, सँस्स्कर्तव्यम्** and "
            "**संस्स्कर्ता** beside them. The vṛtti walks the "
            "rest of the derivation out: the रुँ becomes a "
            "visarga, and 8.3.36 वा शरि then makes the doubled "
            "स् optional"),
    Sandhi(
        "8.3.6", does="ru", of=("pum",), before=("khay-am-para",),
        why="पुमः खय्यम्परे — पुम् takes रुँ before a खय् that "
            "has an अम् after it: **पुँस्कामा, पुंस्कामा; "
            "पुँस्पुत्रः; पुँस्फलम्; पुँश्चली**. Without it "
            "8.3.37 कुप्वोः क पौ च would have given पुंस्कामा "
            "a जिह्वामूलीय instead of the स्, which is what the "
            "vṛtti says the rule is for"),
    Sandhi(
        "8.3.7", does="ru", gana="na-anta",
        before=("chav-am-para",), keeps_out="प्रशान् — excepted "
                                            "by name in the "
                                            "sūtra itself",
        why="नश्छव्यप्रशान् — any न्-final word except प्रशान् "
            "takes रुँ before a छव् with an अम् after it: "
            "**भवाँश्छादयति, भवांश्छादयति; भवाँश्चिनोति; "
            "भवाँष्टीकते; भवाँस्तरति**. This is the rule every "
            "भवान् in the language passes through before a "
            "stop, and the exception is one word"),
    Sandhi(
        "8.3.8", does="ru", gana="na-anta",
        before=("chav-am-para",), chandasi=True, optional=True,
        blocks=("8.3.7",),
        keeps_out="ताँस्त्वं खाद सुखादितान् — a यजुस् and not "
                  "an ऋच्, where the rule before is compulsory",
        why="उभयथर्क्षु — but in the ṛcs it goes both ways, "
            "with the रुँ or with the न् left standing: "
            "**तस्मिंस् त्वा दधाति, तस्मिन् त्वा दधाति**. "
            "**पूर्वेण नित्ये प्राप्ते विकल्पः क्रियते** — the "
            "sūtra before had made it compulsory and this makes "
            "it a choice, in one register of the Veda only"),
    Sandhi(
        "8.3.9", does="ru", gana="dīrgha-para-na-anta",
        before=("aṭ-samāna-pāda",), chandasi=True,
        why="दीर्घादटि समानपादे — a word-final न् after a LONG "
            "vowel takes रुँ before an अट्, provided the two "
            "stand in the SAME metrical quarter: **परिधीँर् "
            "अति; देवाँ अच्छा दीद्यत्**. **तौ चेद् "
            "निमित्तनिमित्तिनौ समानपादे भवतः** — and पाद here "
            "is the quarter of a verse, **ऋक्ष्वि इति "
            "प्रकृतत्वाद् ऋक्पाद इह गृह्यते**, carried down "
            "from the sūtra before. No other rule in the work "
            "asks where a metrical line begins"),
    Sandhi(
        "8.3.10", does="ru", of=("nṝn",), before=("pa",),
        chandasi=True,
        keeps_out="नॄन् भोजयति — the following word does not "
                  "begin with प",
        why="नॄन् पे — नॄन् takes रुँ before प: **नॄँः पाहि, "
            "नॄंः पाहि; नॄँः प्रीणीहि**. **अकार उच्चारणार्थः** "
            "— the अ in पे is only there to make the letter "
            "pronounceable. And some carry उभयथा down from "
            "8.3.8, which would make it optional; the Kāśikā "
            "records that without adopting it"),
    Sandhi(
        "8.3.11", does="ru", of=("svatavān",), before=("pāyu",),
        chandasi=True,
        why="स्वतवान् पायौ — and स्वतवान् before पायु: "
            "**स्वतवाँः पायुर् अग्ने**. One word before one "
            "word, for one line of the Ṛgveda — which is what a "
            "great many of the Vedic rules of this pāda come "
            "to, and the Kāśikā gives no more than the line"),
    Sandhi(
        "8.3.12", does="ru", of=("kān",), before=("āmreḍita",),
        why="कानाम्रेडिते — and कान् before its own आम्रेडित: "
            "**कांस्कान् आमन्त्रयते; कांस्कान् भोजयति**. The "
            "doubling is 8.1.4's वीप्सा and the word is in the "
            "कस्कादि list of 8.3.48 besides — **तेन कुप्वोः क "
            "पौ च इति न भवति** — so the स् is heard and not a "
            "जिह्वामूलीय"),
    Sandhi(
        "8.3.13", does="lopa", gana="ḍha", before=("ḍha",),
        why="ढो ढे लोपः — a ढ् before a ढ् is dropped: "
            "**लीढम्, मीढम्, उपगूढम्**. The heading पदस्य is "
            "still running from 8.1.16, but a word cannot end "
            "in ढ् before another ढ् — **तस्य असम्भवाद् "
            "अपदान्तस्य ढकारस्य अयं लोपो विज्ञायते** — so the "
            "rule is read of a ढ् INSIDE a word, and the "
            "heading is quietly set aside"),
    Sandhi(
        "8.3.14", does="lopa", gana="repha", before=("repha",),
        why="रो रि — and a र् before a र् is dropped: "
            "**नीरक्तम्, दूरक्तम्; अग्नी रथः; इन्दू रथः; पुना "
            "रक्तं वासः; प्राता राजक्रयः**. The preceding vowel "
            "lengthens by 6.3.111, which is why अग्नि gives "
            "अग्नी. And this rule too reaches inside a word — "
            "**तेन अपदान्तस्य अपि रेफस्य लोपो भवति** — for "
            "अजर्घाः and अपास्पाः"),
    Sandhi(
        "8.3.16", does="visarjanīya", gana="ru", before=("sup",),
        keeps_out="गीर्षु, धूर्षु — the र् is the word's own "
                  "and not a रुँ, so the visarga does not come",
        why="रोः सुपि — the र् of a रुँ becomes a visarga "
            "before a locative plural ending: **पयःसु, "
            "सर्पिःषु, यशःसु**. **सुपि इति सप्तमीबहुवचनं "
            "गृह्यते** — सुप् names that one ending here and "
            "not the whole class. And the rule is a "
            "restriction rather than a provision — **सिद्धे "
            "सत्य् आरम्भो नियमार्थः। रोर् एव सुपि "
            "विसर्जनीयादेशः, न अन्यस्य** — 8.3.15 would have "
            "given the visarga anyway, and this confines it to "
            "a रुँ so that गीर्षु keeps its र्"),
    Sandhi(
        "8.3.17", does="ya", gana="bho-bhago-agho-a-pūrva-ru",
        before=("aś",),
        why="भोभगोअघोअपूर्वस्य योऽशि — the र् of a रुँ standing "
            "after भोः, भगोः, अघोः or an अ-vowel becomes य् "
            "before an अश्: **भो अत्र; भगो अत्र; अघो अत्र; भो "
            "ददाति**; and after an अ, **क आस्ते, कय् आस्ते; "
            "ब्राह्मणा ददति; पुरुषा ददति**. This is the rule "
            "the three teachers of the next three sūtras then "
            "disagree about"),
    Sandhi(
        "8.3.18", does="laghu-ya", gana="ya-va-pada-anta",
        before=("aś",), view="śākaṭāyana", optional=True,
        blocks=("8.3.17",),
        why="व्योर्लघुप्रयत्नतरः शाकटायनस्य — and in "
            "ŚĀKAṬĀYANA'S view that य् — and a व् in the same "
            "position — is pronounced with LESS effort: "
            "**भोयत्र, भो अत्र; कयास्ते, क आस्ते; अस्मायुद्धर, "
            "अस्मा उद्धर**. Naming a teacher makes the rule an "
            "option in the language, and both readings stand"),
    Sandhi(
        "8.3.19", does="lopa", gana="ya-va-pada-anta",
        before=("aś",), view="śākalya", optional=True,
        blocks=("8.3.17",),
        why="लोपः शाकल्यस्य — and in ŚĀKALYA'S view it is "
            "dropped altogether: **क आस्ते, कयास्ते; काक "
            "आस्ते; अस्मा उद्धर; द्वा अत्र, द्वावत्र; असा "
            "आदित्यः, असावादित्यः**. This is why a Vedic pada "
            "text and a saṃhitā text differ where they do, and "
            "the sūtra is the reason अ + अ hiatus is heard in "
            "recitation at all"),
    Sandhi(
        "8.3.20", does="lopa", gana="o-para-ya", before=("aś",),
        view="gārgya", blocks=("8.3.18", "8.3.19"),
        why="ओतो गार्ग्यस्य — and after an ओ the य् is dropped "
            "in GĀRGYA'S view: **भो अत्र; भगो अत्र; भो इदम्; "
            "भगो इदम्**.\\n\\n"
            "**AND HERE NAMING A TEACHER DOES NOT MAKE AN "
            "OPTION.** **नित्यार्थोऽयम् आरम्भः। गार्ग्यग्रहणं "
            "पूजार्थम्** — the rule exists to make the loss "
            "COMPULSORY after ओ where 8.3.19 left it optional, "
            "and the name is an honour. It is the same thing "
            "7.3.99 said of Gārgya and Gālava, and the "
            "opposite of what 8.3.18 and 8.3.19 do"),
    Sandhi(
        "8.3.21", does="lopa", gana="a-pūrva-ya-va",
        before=("uñ-pada",),
        keeps_out="तन्त्र उतम्, तन्त्रयुतम् — the उ is not a "
                  "word of its own, and पदे is not met",
        why="उञि च पदे — and before उञ् STANDING AS A WORD: "
            "**स उ एकविंशवर्तनिः; स उ एकाग्निः**. The पद is "
            "what the counter-example turns on, and the vṛtti "
            "adds a nicety about how a उ that has come from a "
            "वे-root's saṃprasāraṇa can still be recognised as "
            "the particle — **भूतपूर्वेण ञकारेण शक्यते "
            "प्रत्यभिज्ञातुम्**"),
    Sandhi(
        "8.3.22", does="lopa", gana="bho-bhago-agho-a-pūrva-ya",
        before=("hal",), blocks=("8.3.18",),
        why="हलि सर्वेषाम् — and before a CONSONANT the य् is "
            "dropped in EVERY teacher's view: **भो हसति; भगो "
            "हसति; अघो याति; वृक्षा हसन्ति**. "
            "**सर्वेषांग्रहणं शाकटायनस्य अपि लोपो यथा स्यात्** "
            "— Śākaṭāyana had only lightened the sound, and "
            "saying ALL is what takes his lighter य् away "
            "here. Three sūtras of disagreement close in one "
            "of agreement"),
    Sandhi(
        "8.3.23", does="anusvāra", gana="ma-anta",
        before=("hal",),
        keeps_out="त्वमत्र, किमत्र — a vowel follows; गम्यते, "
                  "रम्यते — the म् does not end a word",
        why="मोऽनुस्वारः — a word-final म् becomes an anusvāra "
            "before a consonant: **कुण्डं हसति; वनं हसति; "
            "कुण्डं याति**. This is the rule every accusative "
            "singular and every neuter nominative in the "
            "language passes through, and both its conditions "
            "are tested"),
    Sandhi(
        "8.3.24", does="anusvāra", gana="na-ma-a-pada-anta",
        before=("jhal",),
        keeps_out="राजन् भुङ्क्ष्व — the न् ends a word; "
                  "रम्यते, गम्यते — no झल् follows",
        why="नश्चापदान्तस्य झलि — and a न् or म् INSIDE a word "
            "becomes an anusvāra before a झल्: **पयांसि, "
            "यशांसि, सर्पींषि, धनूंषि**, and for the म् "
            "**आक्रंस्यते, आचिक्रंसते, अधिजिगांसते**. The "
            "neuter plurals of every स्-final stem are made by "
            "this rule together with 7.1.72's नुम्"),
    Sandhi(
        "8.3.25", does="ma", of=("sam",), before=("rāj-kvip",),
        blocks=("8.3.23",),
        keeps_out="संयत् — the following root is not राज्; "
                  "किंराट् — the first word is not सम्; "
                  "संराजिता — no क्विप्",
        why="मो राजि समः क्वौ — but सम् keeps its म् before "
            "राज् with a क्विप्: **सम्राट्, साम्राज्यम्**. "
            "**मकारस्य मकारवचनम् अनुस्वारनिवृत्त्यर्थम्** — "
            "prescribing म् for म् is idle except as a way of "
            "keeping the anusvāra out, which is exactly what "
            "it is for. All three of its conditions are tested"),
    Sandhi(
        "8.3.26", does="ma", gana="ma-anta",
        before=("ha-ma-para",), optional=True, blocks=("8.3.23",),
        why="हे मपरे वा — and before a ह् that has a म् after "
            "it, a म् optionally stays: **किम् ह्मलयति, किं "
            "ह्मलयति; कथम् ह्मलयति**. A vārttika extends it to "
            "three more sounds, one to one: **यवलपरे यवला वा** "
            "— **किय् ह्यः, किं ह्यः; किव् ह्वलति** — so the "
            "म् takes the shape of whatever follows the ह्"),
    Sandhi(
        "8.3.27", does="na", gana="ma-anta",
        before=("ha-na-para",), optional=True, blocks=("8.3.23",),
        why="नपरे नः — and before a ह् with a न् after it, a "
            "म् optionally becomes न्: **किन् ह्नुते, किं "
            "ह्नुते; कथन् ह्नुते**. It is the same assimilation "
            "the vārttika on the sūtra before gave for य्, व् "
            "and ल्, stated as a sūtra because न् is the one "
            "case Pāṇini wrote out"),
    Sandhi(
        "8.3.28", does="kuk-ṭuk", gana="ṅa-ṇa-anta",
        before=("śar",), optional=True,
        why="ङ्णोः कुक्टुक् शरि — a word-final ङ् or ण् "
            "optionally takes a कुक् or a टुक् before a शर्, "
            "one to one: **प्राङ्क् शेते, प्राङ् शेते; "
            "प्राङ्क् षष्ठः; वण्ट् शेते, वण् शेते**. The "
            "augment is put at the END of what precedes — "
            "**पूर्वान्तकरणम्** — and not at the head of what "
            "follows, which is what makes it audible as part "
            "of प्राङ्क्"),
    Sandhi(
        "8.3.29", does="dhuṭ", gana="ḍa-anta-para-sa-ādi",
        optional=True,
        why="डः सि धुट् — a स्-initial word after a ड्-final "
            "one optionally takes a धुट्: **श्वलिट्त्साये, "
            "श्वलिट् साये; मधुलिट्त्साये**. The augment goes at "
            "the head of the SECOND word — **परादिकरणम्** — "
            "and the reason is given: 8.4.42's refusal of "
            "ष्टुत्व after a word-final ट-class sound would "
            "otherwise apply, and putting the धुट् first keeps "
            "the two apart"),
    Sandhi(
        "8.3.30", does="dhuṭ", gana="na-anta-para-sa-ādi",
        optional=True,
        why="नश्च — and after a न्-final word: **भवान्त्साये, "
            "भवान् साये; महान्त्साये**. And the augment is "
            "invisible to the rule that would have given a रुँ "
            "— **धुटश् चर्त्वस्य च असिद्धत्वाद् नश्छव्यप्रशान् "
            "इति रुत्वं न भवति** — so भवान्त्साये keeps its "
            "न् where भवांश्छादयति does not, and the two forms "
            "of the same word are five sūtras apart"),
    Sandhi(
        "8.3.31", does="tuk", gana="na-anta", before=("śa",),
        optional=True,
        why="शि तुक् — a word-final न् optionally takes a तुक् "
            "before श्: **भवाञ्च्छेते**. **पूर्वान्तकरणं "
            "छत्वार्थम्** — the augment goes at the end of the "
            "first word so that 6.1.73's छ् can then come. And "
            "the vṛtti raises a difficulty it does not quite "
            "settle: in कुर्वञ्च्छेते the न् is then no longer "
            "word-final and the cerebral would apply, "
            "**तत्र समाधिम् आहुः**"),
    Sandhi(
        "8.3.32", does="ṅamuṭ", gana="hrasva-para-ṅam-anta",
        before=("ac",),
        why="ङमो ह्रस्वादचि ङमुण्नित्यम् — a vowel after a "
            "ङम्-final word whose ङम् follows a SHORT vowel "
            "ALWAYS takes a ङमुट्, and the three augments match "
            "the three sounds one to one: **प्रत्यङ्ङास्ते** "
            "for the ङ्, **वण्णास्ते** for the ण्, and the न् "
            "likewise. This is why a short vowel before a "
            "final nasal doubles it in recitation and a long "
            "one does not"),
    Sandhi(
        "8.3.33", does="va", of=("uñ",), gana="may-para",
        before=("ac",), optional=True,
        why="मय उञो वो वा — after a मय्, the particle उञ् "
            "optionally becomes व् before a vowel: **शम्वस्तु "
            "वेदिः, शमु अस्तु वेदिः; तद्वस्य परेतः; किम्वावपनम्, "
            "किमु आवपनम्**. The alternative is not a plain "
            "hiatus but a प्रगृह्य, which is why the two "
            "readings are heard as far apart as they are"),
)


def _reaches(row: Sandhi, word: str, gana: str, before: str,
             view: str, chandasi: bool) -> bool:
    # A heading answers nothing: 8.3.2 is stated of every rule
    # after it and of none in particular.
    if row.heading:
        return False
    # `of` and `gana` CONJOIN. 8.3.33 names उञ् AND wants a मय्
    # before it, and an alternative reading would let a bare
    # मय् answer for any particle at all.
    if row.of and word not in row.of:
        return False
    if row.gana and gana != row.gana:
        return False
    if row.before and before not in row.before:
        return False
    if row.view and view != row.view:
        return False
    if row.chandasi and not chandasi:
        return False
    return True


def _how_specific(row: Sandhi) -> int:
    """
    A rule that displaces another beats it, a named word beats
    a shape, and a named teacher weighs least — since asking
    for one is what makes his rule reachable at all.

    8.3.17 against 8.3.18, 8.3.19 and 8.3.20 is the whole of
    why the view column exists: four rules reach one य् and
    three of them are somebody's opinion.
    """
    return (
        12 * len(row.blocks)
        + 8 * bool(row.of)
        + 4 * bool(row.gana)
        + 3 * bool(row.before)
        + 2 * bool(row.chandasi)
        + 1 * bool(row.view)
    )


@dataclass(frozen=True)
class Joined:
    """What the run answers about two sounds in close juncture.

    The whole of अध्याय ८'s last two pādas answers with this one
    shape, which is why it carries two flags this module's own
    table never sets: `refuses` for a sūtra that only keeps
    another off — there are ten in 8.3 alone — and `nipatana`
    for a word laid down whole.
    """

    does: str
    sutra: str
    why: str
    optional: bool = False
    refuses: bool = False
    nipatana: bool = False
    view: str = ""
    blocked_by: Tuple[str, ...] = ()


def in_samhita(word: str = "", *, gana: str = "",
               before: str = "", view: str = "",
               chandasi: bool = False) -> Joined:
    """
    8.3.1–33 — the रुँ, the nasal before it, and the anusvāra.

    Nothing answers by default. A teacher's rule answers only a
    reader who asks for that teacher.
    """
    matched = [
        row for row in RU_TABLE
        if _reaches(row, word, gana, before, view, chandasi)
    ]
    if not matched:
        return Joined(
            "", "", "No rule of 8.3.1-33 is reached, so the two "
                    "sounds stand as they are")
    row = max(matched, key=_how_specific)
    return Joined(row.does, row.sutra, row.why,
                  optional=row.optional, view=row.view,
                  blocked_by=row.blocks)


def provisions_for(sutra_id: str) -> Tuple[Sandhi, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in RU_TABLE if row.sutra == sutra_id)


__all__ = [
    "Sandhi", "RU_TABLE", "RU_RUN", "SAMHITA", "CODIFIED_APART",
    "ANUNASIKA_FROM", "TEACHERS", "PUJARTHAM",
    "Joined", "in_samhita", "provisions_for",
]
