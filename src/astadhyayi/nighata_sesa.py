# -*- coding: utf-8 -*-
"""
८.१.५१–७४ — the rest of the निघात, and the vocative that is not there.

The पāda closes in four movements. 8.1.51–56 finish the list of
particles and constructions that spare a finite verb its accent
— an imperative of motion and the future or imperative construed
with it (आगच्छ देवदत्त, ग्रामं द्रक्ष्यसि), हन्त, आम्, and in
the Veda a verb followed by यत्, हि or तु. 8.1.57–66 add the
words that spare it by standing AFTER it — चन, चित्, इव, the
गोत्रादि class, a taddhita, an आम्रेडित, and every particle of
the चादि list — and then, in six sūtras, the FIRST of two verbs
construed with च, वा, ह or अह.

**AND THE LAST OF THOSE IS THE ONLY ONE THAT SAYS ALWAYS.**
8.1.66 **यद्वृत्तान्नित्यम्** — a finite verb after any word
with यद् in it keeps its accent without exception: यो भुङ्क्ते,
यं भोजयति, येन भुङ्क्ते. Every other refusal of the pāda is
hedged by a sense, a position or an option; this one is not.

**AND THEN THE PĀDA TURNS ROUND AND MAKES THINGS TONELESS
AGAIN.** 8.1.67–71: what is praised after a word of praise
(काष्ठाध्यापकः), the verb after those even with a preverb
(यत् काष्ठं पचति), the verb before a word of contempt
(पचति पूति), and a गति before another गति or before an accented
verb (अभ्युद्धरति, यत् प्रपचति).

**AND IT ENDS BY MAKING A WORD DISAPPEAR.** 8.1.72
**आमन्त्रितं पूर्वम् अविद्यमानवत्** — a vocative standing
first counts as not being there at all, so that देवदत्त
यज्ञदत्त has nothing in front of its second word and 8.1.19
cannot reach it. 8.1.73 takes that back where the second
vocative agrees with the first, and 8.1.74 makes the taking-back
optional for a plural.

**WHAT THIS MODULE DOES NOT DO.** It says which word is toneless
and which is spared. `Toneless` and the sūtra number of the
निघात itself are asked of `nighata` rather than restated here.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

from src.astadhyayi.nighata import (  # noqa: E402
    THE_NIGHATA,
    Toneless,
)

#: This module's stretch, which closes पाद ८.१.
SESA_RUN: Tuple[str, str] = ("8.1.51", "8.1.74")

#: Where 8.1.17's पदात् stops, in the middle of this run.
PADAT_ENDS_AT: str = "8.1.68"

#: 8.1.57's six, before which a verb keeps its accent.
CANADI_SIX: Tuple[str, ...] = (
    "cana", "cit", "iva", "gotrādi", "taddhita", "āmreḍita")

#: 8.1.67's own class, the words of praise a praised word
#: follows: काष्ठ, दारुण, अमातापुत्र, अयुत, अद्भुत, अनुक्त,
#: भृश, घोर, परम — the Kāśikā's list, not exhausted here.
KASTHADI: Tuple[str, ...] = (
    "kāṣṭha", "dāruṇa", "amātāputra", "ayuta", "adbhuta",
    "anukta", "bhṛśa", "ghora", "parama")


@dataclass(frozen=True)
class Sesa:
    """One rule of 8.1.51–74: an accent kept, lost, or unseen."""

    sutra: str
    #: `anudātta`, `avidyamānavat`.
    does: str = ""
    #: The word class the rule speaks of: `tiṅ`, `loṭ`, `lṛṭ`,
    #: `prathamā-tiṅ`, `gati`, `pūjita`, `āmantrita` and its
    #: two qualified forms.
    gana: str = ""
    #: What must stand before.
    after: str = ""
    #: What must follow. Ten sūtras of this run turn on it,
    #: which is what makes it a column of its own rather than
    #: another reading of `joined`.
    before: str = ""
    #: The particle or construction it must be construed with.
    joined: Tuple[str, ...] = ()
    sense: Tuple[str, ...] = ()
    #: `samāna-kāraka`, `sopasarga-anuttama`, `ekāntara`,
    #: `sagati`, `pūrva`.
    position: str = ""
    #: True where the sūtra only keeps another rule off.
    refuses: bool = False
    optional: bool = False
    chandasi: bool = False
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


SESA_TABLE: Tuple[Sesa, ...] = (
    Sesa(
        "8.1.51", refuses=True, gana="lṛṭ",
        joined=("gatyartha-loṭ",), position="samāna-kāraka",
        blocks=(THE_NIGHATA,),
        keeps_out="आगच्छ देवदत्त, यज्ञदत्तो ग्रामं द्रक्ष्यति — "
                  "the कारक is wholly another",
        why="गत्यर्थलोटा लृण् न चेत् कारकं सर्वान्यत् — a FUTURE "
            "construed with the imperative of a verb of motion "
            "keeps its accent, provided the कारक is not wholly "
            "different: **आगच्छ देवदत्त, ग्रामं द्रक्ष्यसि**. "
            "**यत्रैव कारके कर्तरि कर्मणि वा लोट्, तत्रैव यदि "
            "लृड् अपि भवति इत्यर्थः** — the same agent or the "
            "same object in both halves, and the vṛtti is "
            "careful that only those two count: **कर्तृकर्मणी "
            "एव अत्र कारकग्रहणेन गृह्येते, न करणादि "
            "कारकान्तरम्**"),
    Sesa(
        "8.1.52", refuses=True, gana="loṭ",
        joined=("gatyartha-loṭ",), position="samāna-kāraka",
        blocks=(THE_NIGHATA,),
        keeps_out="पच देवदत्त ओदनं, भुङ्क्ष्व एनम् — पच् is no "
                  "verb of motion",
        why="लोट् च — and an IMPERATIVE so construed: **आगच्छ "
            "देवदत्त, ग्रामं पश्य; आगच्छ विष्णुमित्र, ग्रामं "
            "शाधि**, and in the passive **आगम्यतां देवदत्तेन "
            "ग्रामो दृश्यतां यज्ञदत्तेन**. The condition is the "
            "same one word for word — **लोडन्तयोर् एकं कारकं "
            "यदि भवति इत्यर्थः** — so the pair of sūtras "
            "differs in nothing but which tense is spared"),
    Sesa(
        "8.1.53", refuses=True, optional=True, gana="loṭ",
        joined=("gatyartha-loṭ",), position="sopasarga-anuttama",
        blocks=("8.1.52",),
        keeps_out="आगच्छ देवदत्त ग्रामं पश्य — no preverb, so "
                  "the refusal is compulsory and not optional",
        why="विभाषितं सोपसर्गम् अनुत्तमम् — but where the "
            "imperative has a PREVERB and is not first person, "
            "the sparing is only optional: **आगच्छ देवदत्त "
            "ग्रामं प्रविश** beside **प्रविश** with the accent "
            "kept; **आगच्छ देवदत्त ग्रामं प्रशाधि, प्रशाधि**. "
            "**प्राप्तविभाषा इयम्** — what is made optional was "
            "already available from the sūtra before"),
    Sesa(
        "8.1.54", refuses=True, optional=True, gana="loṭ",
        joined=("hanta",), position="sopasarga-anuttama",
        blocks=(THE_NIGHATA,),
        keeps_out="हन्त कुरु — no preverb, and 8.1.30's refusal "
                  "reaches it compulsorily instead",
        why="हन्त च — and with हन्त, an imperative with a "
            "preverb and not first person, optionally: **हन्त "
            "प्रविश, प्रविश; हन्त प्रशाधि, प्रशाधि**. "
            "**पूर्वं सर्वम् अनुवर्तते गत्यर्थलोटं "
            "वर्जयित्वा** — everything is carried down except "
            "the verb of motion.\\n\\n"
            "**AND THE VṚTTI HAS TO SAY WHY हन्त IS HERE AT "
            "ALL.** हन्त was already in 8.1.30's list of nine, "
            "where the sparing is compulsory — **निपातैर्यद्यदि"
            "हन्त० इति नित्यम् अत्र निघातप्रतिषेधो भवति**. "
            "This sūtra is for the preverb case, where the "
            "option is wanted"),
    Sesa(
        "8.1.55", refuses=True, gana="āmantrita", joined=("ām",),
        position="ekāntara", sense=("anantika",),
        blocks=("8.1.19",),
        keeps_out="शाकं पचसि देवदत्त३ — no आम्; आम् प्रपचसि "
                  "देवदत्त३ — two words between and not one",
        why="आम एकान्तरम् आमन्त्रितम् अनन्तिके — a VOCATIVE "
            "standing after आम् with ONE word between, of "
            "someone not close by, keeps its accent: **आम् "
            "पचसि देवदत्त३; आम् भो देवदत्त३**. It is 8.1.19's "
            "refusal, and the vṛtti notes that भो counts as a "
            "vocative-final word here — **भो इत्यामन्त्रितान्तम् "
            "अपि 8.1.73 इति न अविद्यमानवद् भवति**, so the rule "
            "at the end of the pāda and this one meet"),
    Sesa(
        "8.1.56", refuses=True, gana="tiṅ", before="yat-hi-tu-para",
        chandasi=True, blocks=(THE_NIGHATA,),
        why="यद्धितुपरं छन्दसि — and in the VEDA a finite verb "
            "followed by यत्, हि or तु keeps its accent: "
            "**गवां गोत्रम् उदसृजो यद् अङ्गिरः; इन्दवो वाम् "
            "उशन्ति हि; आख्यास्यामि तु ते**. "
            "**आमन्त्रितम् इत्येतद् अस्वरितत्वान् न "
            "अनुवर्तते** — the vocative of the sūtra before is "
            "not carried down, being unmarked; तिङ् is. The "
            "same three particles spare a verb they PRECEDE by "
            "8.1.30 and 8.1.34, and what is new here is that "
            "they may follow"),
    Sesa(
        "8.1.57", refuses=True, gana="tiṅ", after="a-gati",
        before="cana-cid-iva-gotrādi-taddhita-āmreḍita",
        blocks=(THE_NIGHATA,),
        why="चनचिदिवगोत्रादितद्धिताम्रेडितेष्वगतेः — a finite "
            "verb keeps its accent before चन, चित्, इव, a "
            "गोत्रादि word, a taddhita or an आम्रेडित, provided "
            "it does not itself stand after a गति: **देवदत्तः "
            "पचति चन; पचति चित्; पचतीव; पचति गोत्रम्; पचति "
            "ब्रुवम्; पचति प्रवचनम्**. The गोत्रादि here are "
            "the ones 8.1.27 named and in the senses that sūtra "
            "named — **इह अपि गोत्रादयः कुत्सनाभीक्ष्ण्ययोर् "
            "एव गृह्यन्ते** — so the two rules read each other"),
    Sesa(
        "8.1.58", refuses=True, gana="tiṅ", after="a-gati",
        before="cādi", blocks=(THE_NIGHATA,),
        why="चादिषु च — and before the चादि particles: "
            "**देवदत्तः पचति च, खादति च; पचति वा, खादति वा; "
            "पचति ह; पचत्यह; पचत्येव**. **चादयो न "
            "चवाहाहैवयुक्ते इत्यत्र ये निर्दिष्टाः, त इह "
            "परिगृह्यन्ते** — the list is 8.1.24's five and not "
            "the whole चादि class of 1.4.57, which is the only "
            "place in the pāda where a गण name is narrowed by "
            "pointing at an earlier sūtra"),
    Sesa(
        "8.1.59", refuses=True, gana="prathamā-tiṅ",
        joined=("ca", "vā"), blocks=(THE_NIGHATA,),
        why="चवायोगे प्रथमा — where two verbs are construed "
            "with च or वा, the FIRST keeps its accent and the "
            "second does not: **गर्दभांश् च कालयति, वीणां च "
            "वादयति; गर्दभान् वा कालयति, वीणां वा वादयति**. "
            "Both words of the sūtra are load-bearing — "
            "**योगग्रहणं पूर्वाभ्याम् अपि योगे निघातप्रतिषेधो "
            "यथा स्याद् इति; प्रथमाग्रहणं द्वितीयादेस् "
            "तिङन्तस्य मा भूद् इति** — and अगतेः, carried down "
            "into the sūtra before, stops here"),
    Sesa(
        "8.1.60", refuses=True, gana="prathamā-tiṅ",
        joined=("ha",), sense=("kṣiyā",), blocks=(THE_NIGHATA,),
        why="हेति क्षियायाम् — and the first of two verbs "
            "construed with ह, where a BREACH OF CUSTOM is "
            "meant: **क्षिया धर्मव्यतिक्रमः, आचारभेदः**. "
            "**स्वयं ह रथेन याति३, उपाध्यायं पदातिं गमयति; "
            "स्वयं ह ओदनं भुङ्क्ते३, उपाध्यायं सक्तून् "
            "पाययति** — he rides while he makes his teacher "
            "walk. The प्लुत on the first verb is 8.2.104's, "
            "and the two rules are cited side by side"),
    Sesa(
        "8.1.61", refuses=True, gana="prathamā-tiṅ",
        joined=("aha",), sense=("viniyoga", "kṣiyā"),
        blocks=(THE_NIGHATA,),
        why="अहेति विनियोगे च — and with अह where a "
            "DISTRIBUTIVE ASSIGNMENT is meant, and by the च in "
            "the breach of custom as well: **नानाप्रयोजनो "
            "नियोगो विनियोगः। त्वम् अह ग्रामं गच्छ, त्वम् अह "
            "अरण्यं गच्छ** — you to the village and you to the "
            "forest, with the first verb accented and the "
            "second not. The क्षिया examples are the sūtra "
            "before's over again with अह for ह"),
    Sesa(
        "8.1.62", refuses=True, gana="prathamā-tiṅ",
        joined=("ca-lopa", "aha-lopa"), sense=("avadhāraṇa",),
        blocks=(THE_NIGHATA,),
        why="चाहलोप एवेत्यवधारणम् — and where the च or the अह "
            "is there in sense but not in sound, provided एव "
            "is used for EMPHASIS: **क्व च अस्य लोपः? यत्र "
            "गम्यते च अर्थो न च प्रयुज्यते**. **देवदत्त एव "
            "ग्रामं गच्छतु, स देवदत्त एव अरण्यं गच्छतु**. And "
            "the vṛtti tells the two elisions apart by whose "
            "agent is whose — **समानकर्तृके चलोपः, नानाकर्तृके "
            "अहलोपः**, since च joins and अह singles out"),
    Sesa(
        "8.1.63", refuses=True, optional=True, gana="prathamā-tiṅ",
        joined=("cādi-lopa",), blocks=(THE_NIGHATA,),
        why="चादिलोपे विभाषा — and where any of the चादि is "
            "elided, optionally: **शुक्ला व्रीहयो भवन्ति, "
            "श्वेता गा आज्याय दुहन्ति** — भवन्ति keeps its "
            "accent or loses it. With वा elided, **व्रीहिभिर् "
            "यजेत, यवैर् यजेत**. The list is again 8.1.24's, "
            "pointed at by name — **चादयो न चवाहाहैवयुक्ते इति "
            "सूत्रनिर्दिष्टा गृह्यन्ते**"),
    Sesa(
        "8.1.64", refuses=True, optional=True, gana="prathamā-tiṅ",
        joined=("vai", "vāva"), chandasi=True,
        blocks=(THE_NIGHATA,),
        why="वैवावेति च च्छन्दसि — and with वै or वाव in the "
            "Veda, optionally: **अहर् वै देवानाम् आसीद् "
            "रात्रिर् असुराणाम्; बृहस्पतिर् वै देवानां पुरोहित "
            "आसीत् शण्डामर्कावसुराणाम्; अयं वाव हस्त आसीत्, "
            "नेतर आसीत्**. In each pair the first verb is "
            "spared and the second is not, which is the shape "
            "every rule from 8.1.59 has taken"),
    Sesa(
        "8.1.65", refuses=True, optional=True, gana="prathamā-tiṅ",
        joined=("eka", "anya"), chandasi=True,
        blocks=(THE_NIGHATA,),
        why="एकान्याभ्यां समर्थाभ्याम् — and with एक and अन्य "
            "where they are construed with the verb, optionally, "
            "in the Veda: **प्रजाम् एका जिन्वत्य् ऊर्जम् एका "
            "राष्ट्रम् एका रक्षति देवयूनाम्** — जिन्वति is "
            "spared on one alternative and not on the other; "
            "**तयोर् अन्यः पिप्पलं स्वाद्वत्त्य् अनश्नन्न् "
            "अन्यो अभि चाकशीति**, with अत्ति the same way"),
    Sesa(
        "8.1.66", refuses=True, gana="tiṅ", after="yadvṛtta",
        blocks=(THE_NIGHATA,),
        why="यद्वृत्तान्नित्यम् — a finite verb after ANY word "
            "with यद् in it keeps its accent, and this one "
            "says ALWAYS: **यो भुङ्क्ते; यं भोजयति; येन "
            "भुङ्क्ते**. **यत्र पदे यच्छब्दो वर्तते तत् सर्वं "
            "यद्वृत्तम्** — every word containing यद्, however "
            "made.\\n\\n"
            "**AND THE NAME IS READ MORE WIDELY HERE THAN IT "
            "WAS AT 8.1.48.** **इह वृत्तग्रहणेन तद्विभक्त्यन्तं "
            "प्रतीयात् डतरडतमौ च प्रत्ययौ इत्येतद् न "
            "आश्रीयते** — किंवृत्त was confined to the "
            "inflected forms and the two affixes; यद्वृत्त is "
            "not, and neither is the option: छन्दसि and "
            "प्रथमा both stop before this sūtra"),
    Sesa(
        "8.1.67", does="anudātta", gana="pūjita",
        after="pūjana-kāṣṭhādi",
        why="पूजनात् पूजितम् अनुदात्तम् — after a word of "
            "PRAISE of the काष्ठादि class, what is praised is "
            "toneless: **काष्ठाध्यापकः, काष्ठाभिरूपकः; "
            "दारुणाध्यापकः; अमातापुत्राध्यापकः; अयुताभिरूपकः; "
            "अद्भुताध्यापकः; अनुक्ताध्यापकः; भृशाध्यापकः; "
            "घोराध्यापकः; परमाध्यापकः** — a teacher and a half. "
            "The pāda turns here: from 8.1.28 to 8.1.66 every "
            "sūtra kept an accent, and from here five sūtras "
            "take one away"),
    Sesa(
        "8.1.68", does="anudātta", gana="tiṅ",
        after="pūjana-kāṣṭhādi", position="sagati",
        blocks=("8.1.30",),
        why="सगतिरपि तिङ् — and a finite verb after those, WITH "
            "or without a preverb: **यत् काष्ठं पचति; यत् "
            "काष्ठं प्रपचति; यद् दारुणं पचति; यद् दारुणं "
            "प्रपचति**. **तिङ्ङतिङः इति निघातस्य "
            "निपातैर्यद्यदिहन्त० इति प्रतिषेधे प्राप्ते "
            "पुनर्विधानम्** — the यत् in the examples had "
            "spared the verb by 8.1.30, and this puts the "
            "निघात back. **सगतिग्रहणात् च गतिर् अपि "
            "निहन्यते** — the preverb goes toneless with it, "
            "which is what saying सगति buys"),
    Sesa(
        "8.1.69", does="anudātta", gana="tiṅ",
        before="sup-kutsana-a-gotrādi", position="sagati",
        keeps_out="पचति शोभनम् — praise and not contempt; पचति "
                  "क्लिश्नाति — a verb and not a सुबन्त; पचति "
                  "गोत्रम् — a गोत्रादि word, which 8.1.57 "
                  "spares",
        why="कुत्सने च सुप्यगोत्रादौ — and a finite verb before "
            "a noun of CONTEMPT that is not a गोत्रादि word: "
            "**पचति पूति; प्रपचति पूति; पचति मिथ्या; प्रपचति "
            "मिथ्या**. **पदाद् इति निवृत्तम्** — 8.1.17's "
            "heading stops with the sūtra before, so this rule "
            "needs nothing to stand in front; सगतिरपि तिङ् is "
            "carried down and the preverb goes toneless too"),
    Sesa(
        "8.1.70", does="anudātta", gana="gati", before="gati",
        keeps_out="देवदत्तः प्रपचति — the गति has no other गति "
                  "after it",
        why="गतिर्गतौ — a गति standing before another गति is "
            "toneless: **अभ्युद्धरति; समुदानयति; "
            "अभिसम्पर्याहरति**. In each the last preverb keeps "
            "an accent and every earlier one loses it, which is "
            "how a string of four is heard as one word. "
            "**गतौ इति किम्? आ मन्द्रैर् इन्द्र हरिभिर् याहि "
            "मयूररोमभिः** — आ is a गति there but nothing "
            "follows it, and without the second word the rule "
            "would make it toneless with no condition at all"),
    Sesa(
        "8.1.71", does="anudātta", gana="gati",
        before="udāttavat-tiṅ",
        why="तिङि चोदात्तवति — and a गति before a finite verb "
            "THAT HAS an accent: **यत् प्रपचति; यत् प्रकरोति**. "
            "**तिङ्ग्रहणम् उदात्तवतः परिमाणार्थम्** — saying "
            "तिङ् measures how much must carry the accent: "
            "without it the root alone would have to, and यत् "
            "प्रकरोति, where the accent is on the affix, would "
            "fall outside. The vṛtti quotes the paribhāṣā that "
            "makes a प्र a गति in the first place — "
            "**यत्क्रियायुक्ताः प्रादयस् तेषां तं प्रति "
            "गत्युपसर्गसंज्ञे भवतः**"),
    Sesa(
        "8.1.72", does="avidyamānavat", gana="āmantrita",
        position="pūrva",
        why="आमन्त्रितं पूर्वम् अविद्यमानवत् — a VOCATIVE "
            "standing first counts as not being there: "
            "**तस्मिन् सति यत् कार्यं तन् न भवति, असति यत् तद् "
            "भवति**. **कानि पुनर् अविद्यमानवत्त्वे "
            "प्रयोजनानि? आमन्त्रिततिङ्निघातयुष्मदस्मदादेशा"
            "भावाः** — three things do not happen: the "
            "vocative's own निघात by 8.1.19, the verb's by "
            "8.1.28, and the enclitics of 8.1.20–23. In "
            "**देवदत्त यज्ञदत्त** the second vocative has "
            "nothing in front of it and keeps 6.1.198's accent "
            "on its first syllable"),
    Sesa(
        "8.1.73", refuses=True, gana="āmantrita-sāmānyavacana",
        before="āmantrita-samānādhikaraṇa", blocks=("8.1.72",),
        keeps_out="देवदत्त पचसि — no vocative follows; and a "
                  "following vocative that does not agree",
        why="न आमन्त्रिते समानाधिकरणे सामान्यवचनम् — but a "
            "GENERAL vocative followed by one that agrees with "
            "it does NOT count as absent: **अग्ने गृहपते; "
            "माणवक जटिलकाध्यापक**. **किं तर्हि? विद्यमानवद् "
            "एव** — it is there, and so the second vocative "
            "has a word in front of it and goes toneless by "
            "8.1.19: **पूर्वस्य विद्यमानवत्त्वात् परम् "
            "अनुदात्तम् एव भवति**"),
    Sesa(
        "8.1.74", does="avidyamānavat", optional=True,
        gana="āmantrita-bahuvacana",
        before="āmantrita-viśeṣavacana", blocks=("8.1.73",),
        why="विभाषितं विशेषवचने बहुवचनम् — and a PLURAL "
            "vocative before a specifying one counts as absent "
            "only optionally: **देवाः शरण्याः** beside "
            "**देवाः शरण्याः** with the second word toneless; "
            "**ब्राह्मणा वैयाकरणाः** the same way. "
            "**सामान्यवचनाधिकारादेव विशेषवचन इति सिद्धे "
            "विशेषवचनग्रहणं विस्पष्टार्थम्** — the qualifying "
            "word was already implied by the sūtra before and "
            "is said again for plainness. With this the pāda "
            "closes"),
)


def _reaches(row: Sesa, gana: str, after: str, before: str,
             joined: str, sense: str, position: str,
             chandasi: bool) -> bool:
    if row.gana and gana != row.gana:
        return False
    if row.after and after != row.after:
        return False
    if row.before and before != row.before:
        return False
    if row.joined and joined not in row.joined:
        return False
    if row.sense and sense not in row.sense:
        return False
    if row.position and position != row.position:
        return False
    if row.chandasi and not chandasi:
        return False
    return True


def _how_specific(row: Sesa) -> int:
    """
    A rule that displaces another beats it, and a named
    construction beats a bare class.

    8.1.53 against 8.1.52 is the pair that needs the position:
    प्रविश is spared only optionally and पश्य compulsorily, and
    the two differ in nothing but the preverb and the person.
    """
    return (
        12 * len(row.blocks)
        + 6 * len(row.joined)
        + 4 * len(row.sense)
        + 4 * bool(row.gana)
        + 4 * bool(row.before)
        + 3 * bool(row.position)
        + 3 * bool(row.after)
        + 2 * bool(row.chandasi)
    )


def in_the_sentence(*, gana: str = "", after: str = "",
                    before: str = "", joined: str = "",
                    sense: str = "", position: str = "",
                    chandasi: bool = False) -> Toneless:
    """
    8.1.51–74 — the rest of the निघात, and what escapes it.

    Nothing answers by default, and the answer is the same
    `Toneless` the earlier half of the pāda gives, since the two
    runs settle one question between them.
    """
    matched = [
        row for row in SESA_TABLE
        if _reaches(row, gana, after, before, joined, sense,
                    position, chandasi)
    ]
    if not matched:
        return Toneless(
            "", "", "No rule of 8.1.51-74 is reached, so the word "
                    "keeps whatever 8.1.16-50 left it")
    row = max(matched, key=_how_specific)
    return Toneless(row.does, row.sutra, row.why,
                    refuses=row.refuses, optional=row.optional,
                    blocked_by=row.blocks)


def provisions_for(sutra_id: str) -> Tuple[Sesa, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in SESA_TABLE if row.sutra == sutra_id)


__all__ = [
    "Sesa", "SESA_TABLE", "SESA_RUN", "PADAT_ENDS_AT",
    "CANADI_SIX", "KASTHADI",
    "in_the_sentence", "provisions_for",
]
