# -*- coding: utf-8 -*-
"""
समास — the compound section opens, 2.1.3 to 2.1.21.

    2.1.3   प्राक् कडारात् समासः      from here to 2.2.38, the name is samāsa
    2.1.4   सह सुपा                    a subanta, together with a subanta
    2.1.5   अव्ययीभावः                 and from here, the name avyayībhāva
    2.1.6   अव्ययं विभक्ति…वचनेषु     an indeclinable in any of sixteen senses
    …
    2.1.21  अन्यपदार्थे च संज्ञायाम्   and in a name, for a third thing's sake

Three headings and then the rules they govern. The headings are the section's
architecture and are codified as such rather than as three more provisions:

  * **2.1.3** names everything to 2.2.38 समास, and the Kāśikā says why it is
    phrased as a range — प्राग्वचनं संज्ञासमावेशार्थम्. The प्राक् is there so
    that समास and अव्ययीभाव may both hold of one compound, which 1.4.1 would
    otherwise forbid. This is the fourth such device the codification has met,
    after 1.4.55's च, 1.4.56's प्राक् and 1.4.60's च, and it is the same
    device — so it is the same code. See :func:`names_of`.

  * **2.1.4** is read as three words carried forward — सुप्, सह, सुपा — and
    the Kāśikā splits the yoga: सहग्रहणं योगविभागार्थम्, so that सह alone may
    also license a compound with a *tiṅanta*, अनुव्यचलत्. The Kaumudī adds
    that this half is छन्दसि. Codified as :func:`saha_supa`, which is the one
    place in the section where the second member is not a subanta.

  * **2.1.5** and **2.1.22** are अन्वर्थ names, and the commentaries read the
    same thing out of both: अन्वर्थसंज्ञा चेयं महती
    पूर्वपदार्थप्राधान्यमव्ययीभावस्य दर्शयति, and against it
    उत्तरपदार्थप्रधानस्तत्पुरुषः. Which member's meaning predominates is the
    whole content of the distinction, so it is recorded on the name itself
    and not left in a docstring. See :data:`SAMJNAS`.

What the rules under them have in common is one shape — these two words, in
these senses, compound — so they are a provision table, the same pattern as
1.3.12–93, 1.2.1–26 and 1.4.23–98. The fields differ; the resolver does not.

Two things about the table are worth stating before it is read.

**2.1.11 विभाषा is a heading, not a rule.** Everything from 2.1.12 is
optional, and the table does not repeat `optional=True` sixteen times — it is
read off the heading, exactly as the text reads it off. The one rule that
escapes is 2.1.21, and it escapes for a stated reason: विभाषाधिकारेऽपि
नित्यसमास एवायम्, नहि वाक्येन संज्ञा गम्यते. A name is not conveyed by a
phrase, so where the sūtra says संज्ञायाम् there is no alternative to fall
back to.

**Two rules restate what is already available.** 2.1.7 यथासादृश्ये and 2.1.15
अनुर्यत्समया both name a word and sense that 2.1.6 already covers — यथा and
सादृश्य are in its list, and समीप is in its list. The Kāśikā catches both and
gives different reasons: 2.1.7 is सादृश्यप्रतिषेधार्थम्, narrowing यथा to the
sense 2.1.6 would have allowed anyway, while 2.1.15 is विभाषार्थम्, moving
समीप from obligatory to optional by restating it under 2.1.11. Same surface,
opposite work, and the table records which is which in `restates`.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Dict, FrozenSet, List, Optional, Sequence, Tuple

from src.astadhyayi.formation import gana_items, order_of
from src.astadhyayi.paribhasa import samartha
from src.astadhyayi.samjna import is_samkhya
from src.astadhyayi.vipratisedha import Rule, eka_samjna


# ---------------------------------------------------------------------------
# The names, and what each one is a name for
# ---------------------------------------------------------------------------


class Samasa(Enum):
    """The compound names. The value is the name; `pradhana` is its content."""

    SAMASA = "samāsa"
    AVYAYIBHAVA = "avyayībhāva"
    TATPURUSA = "tatpuruṣa"
    DVIGU = "dvigu"
    BAHUVRIHI = "bahuvrīhi"
    DVANDVA = "dvandva"


@dataclass(frozen=True)
class Samjna:
    """A compound name, the range it heads, and what the name says."""

    name: Samasa
    sutra: str
    #: The last sūtra the heading reaches, from the commentaries' प्राक्.
    through: str
    #: Whose meaning predominates — the अन्वर्थ content of the name.
    pradhana: str
    why: str

    def covers(self, sutra_id: str) -> bool:
        return order_of(self.sutra) <= order_of(sutra_id) <= order_of(
            self.through)


#: 2.1.3, 2.1.5, 2.1.22 — the three headings in force in this pāda.
#:
#: All five are here now. बहुव्रीहि and द्वन्द्व were left out while their
#: sūtras were unread — a range asserted from memory of the tradition
#: rather than from the commentary is the kind of claim this codification
#: does not make — and the ranges below are the ones the Kāśikā gives.
#:
#: The four पradhānas together are the whole point of having names at all.
#: अव्ययीभाव means what its FIRST member means, तत्पुरुष what its second
#: means, बहुव्रीहि means a THIRD thing that is neither, and द्वन्द्व means
#: both at once. उपकुम्भम् is a nearness, कष्टश्रितः a person, चित्रगुः a
#: man with dappled cows, प्लक्षन्यग्रोधौ two trees.
SAMJNAS: Tuple[Samjna, ...] = (
    Samjna(
        Samasa.SAMASA, "2.1.3", "2.2.38",
        pradhana="—",
        why="प्राक् कडारात् समासः — everything named from here to कडाराः "
            "कर्मधारये is a samāsa. कडारसंशब्दनात् प्राग् यानित ऊर्ध्वम् "
            "अनुक्रमिष्यामः, ते समाससंज्ञा वेदितव्याः.",
    ),
    Samjna(
        Samasa.AVYAYIBHAVA, "2.1.5", "2.1.21",
        pradhana="pūrvapada",
        why="अव्ययीभावः — and the name is अन्वर्थ, deliberately long for it: "
            "अन्वर्थसंज्ञा चेयं महती पूर्वपदार्थप्राधान्यम् अव्ययीभावस्य "
            "दर्शयति. What the compound means is what its *first* member "
            "means; उपकुम्भम् is a nearness, not a pot.",
    ),
    Samjna(
        Samasa.TATPURUSA, "2.1.22", "2.2.22",
        pradhana="uttarapada",
        why="तत्पुरुषः — प्राग्बहुव्रीहेः, and a पूर्वाचार्यसंज्ञा rather "
            "than one Pāṇini coined, taken over whole: उत्तरपदार्थप्रधानः "
            "तत्पुरुषः. कष्टश्रितः is someone resorted, not a hardship.",
    ),
    Samjna(
        Samasa.BAHUVRIHI, "2.2.23", "2.2.28",
        pradhana="anyapadārtha",
        why="शेषो बहुव्रीहिः — and शेष is defined by what it is not: "
            "उपयुक्तादन्यः शेषः, कश्च शेषः? यत्रान्यः समासो नोक्तः — "
            "wherever no other compound has been stated. So the name is "
            "the remainder of the section, and 2.2.24 अनेकमन्यपदार्थे "
            "says what it means: a THIRD thing, neither member. "
            "चित्रगुः is a man, not cows and not dappledness. "
            "शेष इति किम्? उन्मत्तगङ्गम् — 2.1.21 named that one "
            "already, so it is not left over.",
    ),
)

#: द्वन्द्व is NOT here, and the omission is the point. SAMJNAS holds
#: headings — names that govern a stretch, where `covers` means something.
#: 2.2.29 चार्थे द्वन्द्वः confers its name on what it itself forms and
#: nothing runs under it, so the only range it could have been given was
#: its own number. That is a range copied from its own start, which is the
#: one thing the ranges here are tested against.
#:
#: द्विगु is out for the same reason and by the same rule: 2.1.52 confers
#: it on the compound 2.1.51 makes.
#:
#: A name a single sūtra confers comes from the provision, and `resolve`
#: reads both sources.


def samjna_over(sutra_id: str) -> Tuple[Samjna, ...]:
    """Every compound heading whose range covers this sūtra."""
    return tuple(s for s in SAMJNAS if s.covers(sutra_id))


def names_of(sutra_id: str) -> FrozenSet[Samasa]:
    """
    Which compound names a rule in this range confers — 2.1.3 against 1.4.1.

    1.4.1 would allow only one, and the later at that, which would leave
    समास conferred by nothing and every rule that says समासे with no reach.
    The प्राक् is what prevents it: प्राग्वचनं संज्ञासमावेशार्थम्. So the
    answer is a set, and the same code that handles 1.4.55, 1.4.56 and 1.4.60
    handles it — those are the four places the text restores co-application,
    and they are one device.
    """
    return frozenset(s.name for s in samjna_over(sutra_id))


# ---------------------------------------------------------------------------
# 2.1.4 सह सुपा, and the yoga split out of it
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Together:
    """What may stand as the second member, and on whose authority."""

    allowed: bool
    by: str
    why: str
    chandas_only: bool = False


def saha_supa(second_is: str = "sup", chandas: bool = False) -> Together:
    """
    2.1.4 सह सुपा — what a subanta compounds *with*.

    The plain reading takes सह and सुपा together: a subanta with a subanta,
    सुपा सुप् सह समस्यते. But the Kāśikā splits the yoga —
    सहग्रहणं योगविभागार्थम्, तिङापि सह यथा स्यात् — so that सह standing
    alone licenses a second member that is a *tiṅanta*: अनुव्यचलत्,
    अनुप्रावर्षत्. The Kaumudī states the limit the Kāśikā leaves implicit,
    योगविभागस्य इष्टसिद्ध्यर्थत्वात् … स च छन्दस्येव, and both are recorded:
    the split is granted, and it is granted for the Vedic language.

    `second_is` — "sup" for a subanta, "tiṅ" for a finite verb.
    """
    if second_is == "sup":
        return Together(
            True, "2.1.4",
            "सुपा सह — a subanta with a subanta, which is the whole rule "
            "read as one yoga. सुप् इति वर्तते: सुप्, सह and सुपा are all "
            "three carried down over what follows.",
        )
    if second_is == "tiṅ":
        return Together(
            chandas, "2.1.4",
            "सह — the yoga split, सहग्रहणं योगविभागार्थम्, तिङापि सह यथा "
            "स्यात्: अनुव्यचलत्, अनुप्रावर्षत्, पर्यभूषयत्. "
            + ("Vedic, which is where the Kaumudī confines it — स च "
               "छन्दस्येव." if chandas else
               "But स च छन्दस्येव, and this is not stated to be Vedic, so "
               "the split does not reach it."),
            chandas_only=True,
        )
    return Together(
        False, "2.1.4",
        f"neither सुप् nor तिङ् — {second_is!r} is not something 2.1.4 "
        f"offers as a second member.",
    )


# ---------------------------------------------------------------------------
# The pair a compound rule is asked about
# ---------------------------------------------------------------------------


#: Facts a rule in this section asks about that no form carries. Each is
#: named by the word the sūtra itself uses.
FACTS: Dict[str, str] = {
    "lakṣaṇa": "the second member names a mark — something the action is "
               "aimed at or measured against (2.1.14, 2.1.15, 2.1.16)",
    "vaṃśya": "the second member names someone standing in a lineage, of "
              "learning or of birth (2.1.19)",
    "nadī": "the second member names a river (2.1.20, 2.1.21)",
    "saṃjñā": "the compound is a proper name (2.1.21)",
    "samāhāra": "an aggregate is meant, not the members severally (2.1.20)",
    "kitava-vyavahāra": "the gamblers' usage, where the rule is wanted "
                        "(2.1.10)",
    "anya-padārtha": "the compound denotes a third thing, neither member "
                     "(2.1.21)",
    "kta": "the second member ends in क्त — a past participle. श्रित, गत "
           "and the rest of 2.1.24's list are क्त-forms too; from 2.1.25 "
           "the rules stop naming them and ask for the affix (2.1.25 to "
           "2.1.28)",
    "kāla": "the first member names a stretch of time — अहर्, रात्रि, मास, "
            "मुहूर्त. काला इति न स्वरूपविधिः, the plural is not about the "
            "word कால but about what a word means (2.1.28, 2.1.29)",
    "kṣepa": "censure is meant. क्षेपो निन्दा, and it is the compound that "
             "carries it: खट्वारूढो जाल्मः is an insult, खट्वाम् आरूढः is a "
             "man on a bed (2.1.26)",
    "anya-padārtha-bv": "the compound denotes a THIRD thing, neither "
                        "member — प्राप्तोदको ग्रामः is a village, not "
                        "water. Not in the nominative sense, which is "
                        "the one बहुव्रीहि does not take: वृष्टे देवे "
                        "गतः (2.2.24)",
    "saṃkhyeya": "a numeral counting the things themselves stands as the "
                 "other member. संख्येय इति किम्? अधिका विंशतिर्गवाम् "
                 "(2.2.25)",
    "antarāla": "the space BETWEEN two directions is meant — "
                "दक्षिणस्याश्च पूर्वस्याश्च दिशोर् यद् अन्तरालम् "
                "(2.2.26)",
    "sarūpa-yuddha": "the two words are the SAME form, one in the "
                     "seventh case and one in the third, and a fight is "
                     "meant — the इति of the sūtra carrying grasping, "
                     "striking and mutual exchange with it (2.2.27)",
    "tulya-yoga": "the two act together. तुल्ययोग इति किम्? सहैव दशभिः "
                  "पुत्रैर् भारं वहति गर्दभी — the ten sons are merely "
                  "THERE. The Kāśikā calls the condition प्रायिक, since "
                  "सलोमकः and सपक्षकः stand outside it too (2.2.28)",
    "ca-artha": "the words stand in the sense of 'and'. Of the four such "
                "senses only two make a compound — इतरेतरयोग and "
                "समाहार; समुच्चय and अन्वाचय lack सामर्थ्य (2.2.29)",
    "pūjā-kta": "the second member is a क्त prescribed for HONOURING, by "
                "3.2.188 मतिबुद्धिपूजार्थेभ्यश्च — राज्ञां मतः. "
                "पूजायामिति किम्? छात्रस्य हसितम्, which does compound "
                "(2.2.12)",
    "adhikaraṇa-kta": "it is a क्त naming the place of the act, by "
                      "3.4.76 — इदमेषाम् आसितम् (2.2.13)",
    "karman-ṣaṣṭhī": "the genitive stands in the OBJECT sense, the one "
                     "2.3.66 उभयप्राप्तौ कर्मणि allows — गवां दोहः "
                     "(2.2.14)",
    "kartṛ-ṣaṣṭhī": "the genitive stands in the AGENT sense — भवतः "
                    "शायिका, अपां स्रष्टा. कर्तरीति किम्? इक्षुभक्षिकां "
                    "मे धारयसि (2.2.15, 2.2.16)",
    "tṛc-aka": "the second member ends in तृच् or अक — स्रष्टृ, भोजक "
               "(2.2.15, 2.2.16)",
    "krīḍā-jīvikā": "a game or a way of making a living is meant. "
                    "क्रीडाजीविकयोरिति किम्? ओदनस्य भोजकः (2.2.17)",
    "ku-gati-pra": "the first member is कु, or a गति, or one of the "
                   "प्रादि. कु is taken as the indeclinable meaning "
                   "'bad', not the noun — गत्यादिभिः साहचर्यात् (2.2.18)",
    "upapada-atiṅ": "the first member is an उपपद that is not a finite "
                    "verb. अतिङिति किम्? एधानाहारको व्रजति (2.2.19)",
    "am-anta": "the उपपद ends in अम् — स्वादुंकारम्, संपन्नंकारम् "
               "(2.2.20, 2.2.21)",
    "upapada-tṛtīyā-prabhṛti": "the उपपद is one of those prescribed from "
                               "3.4.47 उपदंशस्तृतीयायाम् onward. "
                               "तृतीयाप्रभृतीनीत्येव — अलं कृत्वा, खलु "
                               "कृत्वा are outside it (2.2.21, 2.2.22)",
    "ktvā": "the second member is a क्त्वा form — उच्चैः कृत्वा (2.2.22)",
    "ekadeśin": "the second member names a whole of which the first "
                "names a part — एकदेशोऽस्यास्तीति एकदेशी अवयवी. "
                "एकदेशिनेति किम्? पूर्वं नाभेः कायस्य (2.2.1 to 2.2.3)",
    "ekādhikaraṇa": "and the two are of ONE thing — एकं चेद् अधिकरणम् "
                    "एकद्रव्यम्. एकाधिकरण इति किम्? पूर्वं छात्राणाम् "
                    "आमन्त्रयस्व (2.2.1 to 2.2.3)",
    "parimāṇin": "the second member has a measure — परिमाणमस्यास्तीति "
                 "परिमाणी (2.2.5)",
    "akṛt": "the second member does not end in a कृत् affix (2.2.7)",
    "nirdhāraṇa": "one is being singled out of a group by kind, quality "
                  "or act — जातिगुणक्रियाभिः समुदायाद् एकदेशस्य "
                  "पृथक्करणम्. क्षत्रियो मनुष्याणां शूरतमः (2.2.10)",
    "pratipada-vidhāna": "the genitive was prescribed by a rule naming "
                         "this very word, not by 2.3.50's general "
                         "शेषे — सर्पिषो ज्ञानम् (2.2.10)",
    "pūraṇa": "the second member names a place in a series — "
              "छात्राणां पञ्चमः (2.2.11)",
    "guṇa-artha": "it names a quality as such — बलाकायाः शौक्ल्यम्, "
                  "काकस्य कार्ष्ण्यम् (2.2.11)",
    "suhita-artha": "it means filled or satisfied — फलानां सुहितः, "
                    "फलानां तृप्तः (2.2.11)",
    "sat-pratyaya": "it is a शतृ or शानच् participle — ब्राह्मणस्य "
                    "कुर्वन्, कुर्वाणः (2.2.11)",
    "avyaya": "it is indeclinable — ब्राह्मणस्य कृत्वा (2.2.11)",
    "tavya": "it ends in तव्य — ब्राह्मणस्य कर्तव्यम्. The Kāśikā notes "
             "तव्यत् WITH its anubandha does compound: ब्राह्मणकर्तव्यम् "
             "(2.2.11)",
    "jāti": "the word names a kind rather than an individual. जातिरिति "
            "किम्? देवदत्तः प्रवक्ता, कुमारी मतल्लिका (2.1.65, 2.1.66, "
            "2.1.71)",
    "jāti-paripraśna": "the question is which of a kind. कतरो भवतोर् "
                       "देवदत्तः asks between two people, not between "
                       "kinds, and is not this (2.1.63)",
    "praśaṃsā": "the second member is a settled word of praise — "
                "रूढिशब्दाः प्रशंसावचना गृह्यन्ते मतल्लिकादयः (2.1.66)",
    "varṇa": "both members name colours (2.1.69)",
    "catuṣpād": "the first member names a four-footed animal. "
                "चतुष्पाद इति किम्? ब्राह्मणी गर्भिणी (2.1.71)",
    "kutsita": "the word denotes something being run down. कुत्सितानीति "
               "किम्? वैयाकरणश्चौरः — being a grammarian is not what is "
               "faulted there (2.1.53, 2.1.54)",
    "kutsana": "the second member is itself a term of abuse. कुत्सनैरिति "
               "किम्? कुत्सितो ब्राह्मणः (2.1.53)",
    "upamāna": "the word is what something is likened TO — उपमीयते "
               "अनेन इति उपमानम् (2.1.55)",
    "sāmānya-vacana": "and the other names the property they share — "
                      "उपमानोपमेययोः साधारणो धर्मः सामान्यम् (2.1.55)",
    "upamita": "the word is what is likened, not what it is likened to "
               "(2.1.56)",
    "sāmānya-aprayoga": "and the shared property is NOT put into words. "
                        "सामान्याप्रयोग इति किम्? पुरुषोऽयं व्याघ्र इव "
                        "शूरः — say शूर and this rule stops (2.1.56)",
    "viśeṣaṇa": "the first member narrows the second — भेदकं विशेषणम्. "
                "विशेषणमिति किम्? तक्षकः सर्पः (2.1.57)",
    "viśeṣya": "and the second is what gets narrowed — भेद्यं विशेष्यम्. "
               "विशेष्येणेति किम्? लोहितस्तक्षकः (2.1.57)",
    "cvi-artha": "the sense is of becoming what it was not: अश्रेणयः "
                 "श्रेणयः कृताः — made into rows, having been none "
                 "(2.1.59)",
    "nañ-viśiṣṭa": "the second member is the same क्त-form as the first "
                   "with नञ् on it and nothing else changed — नञैव "
                   "विशेषो यस्य सर्वम् अन्यत् तुल्यम् (2.1.60)",
    "pūjyamāna": "the second member names something being honoured. "
                 "पूज्यमानैरिति किम्? उत्कृष्टा गौः कर्दमात् — a cow "
                 "pulled out of mud is not being honoured (2.1.61)",
    "dhvāṅkṣa": "the second member names a crow. ध्वाङ्क्षेणेत्यर्थग्रहणम् "
                "— the sūtra names a sense, so काक and वायस stand beside "
                "ध्वाङ्क्ष (2.1.42)",
    "ṛṇa": "a debt is meant, or an obligation: ऋणग्रहणं "
           "नियोगोपलक्षणार्थम्, which is why पूर्वाह्णगेयं साम is reached "
           "too. ऋण इति किम्? मासे देया भिक्षा (2.1.43)",
    "kṛtya-yat": "the second member ends in the कृत्य affix यत् — "
                 "यत्प्रत्ययान्तेनैव समास इष्यते (2.1.43)",
    "ahorātra-avayava": "the first member names a PART of the day or "
                        "night, not the whole. अवयवग्रहणं किम्? अहनि "
                        "भुक्तम्, रात्रौ वृत्तम् (2.1.45)",
    "samānādhikaraṇa": "the two words refer to the one thing, whatever "
                       "made each of them apt — भिन्नप्रवृत्तिनिमित्त"
                       "प्रयुक्तस्य शब्दस्य एकस्मिन् अर्थे वृत्तिः. "
                       "समानाधिकरणेनेति किम्? एकस्याः शाटी (2.1.49 to "
                       "2.1.51)",
    "dik": "the first member names a direction (2.1.50, 2.1.51)",
    "taddhitārtha": "a taddhita sense follows — पूर्वस्यां शालायां भवः "
                    "gives पौर्वशालः (2.1.51)",
    "uttarapada": "a further member follows the compound: "
                  "पूर्वशालाप्रियः, पञ्चगवधनः (2.1.51)",
    "guṇavacana": "the second member names a quality rather than a thing "
                  "— खण्ड, काण (2.1.30). गुणवचनेनेति किम्? गोभिर्वपावान्",
    "tatkṛta": "and that quality was BROUGHT ABOUT by what the first "
               "member denotes. तत्कृतेनेति किम्? अक्ष्णा काणः — blind in "
               "the eye, not blinded by it (2.1.30)",
    "kṛdanta": "the second member ends in a कृत् affix (2.1.32)",
    "kartṛ-karaṇa": "the third case is in the agent or the instrument "
                    "sense, not another. कर्तृकरणे इति किम्? "
                    "भिक्षाभिरुषितः (2.1.32, 2.1.33)",
    "adhikārtha": "more is said than is meant, for praise or blame — "
                  "स्तुतिनिन्दाप्रयुक्तम् अध्यारोपितार्थवचनम्. काकपेया "
                  "नदी is not a river crows drink (2.1.33)",
    "vyañjana": "the first member names a relish (2.1.34)",
    "anna": "the second member names food (2.1.34)",
    "miśrīkaraṇa": "the first member names what does the mixing (2.1.35)",
    "bhakṣya": "the second member names something eaten — "
               "खरविशदम् अभ्यवहार्यं भक्ष्यम् (2.1.35)",
    "prakṛti-vikāra": "the two stand as material and product. यूपाय दारु "
                      "is wood that becomes a post; रन्धनाय स्थाली is not, "
                      "and does not compound (2.1.36)",
    "alpaśaḥ": "the usage admits this pair. अल्पा पञ्चमी समस्यते न सर्वा — "
               "only a few fifth-case words compound here, and प्रासादात् "
               "पतितः is not one of them (2.1.38)",
    "atyanta-saṃyoga": "the time is wholly taken up — अत्यन्तसंयोगः "
                       "कृत्स्नसंयोगः, कालस्य स्वेन संबन्धिना व्याप्तिः. "
                       "मुहूर्तसुखम् is a happiness filling the hour, not "
                       "one that happened during it (2.1.29)",
}


@dataclass(frozen=True)
class Pair:
    """Two words offered for compounding, in the order they are spoken."""

    first: str
    second: str
    #: What the members mean here. Only asked where a sūtra names a sense.
    first_sense: Tuple[str, ...] = ()
    #: The case the second member stands in — 5 for 2.1.12, 6 for 2.1.18.
    second_vibhakti: Optional[int] = None
    #: The case the first member stands in — 2 for the द्वितीया of 2.1.24
    #: and what it carries down to. Absent until the tatpuruṣa section
    #: needed it: every avyayībhāva rule names the first member and
    #: constrains the second, so only one of the two was ever asked for,
    #: and `other_vibhakti` on a rule naming the *second* member could
    #: never be satisfied. A condition no pair could meet.
    first_vibhakti: Optional[int] = None
    first_vacana: int = 1
    second_vacana: int = 1
    #: Facts asserted from :data:`FACTS`.
    given: Tuple[str, ...] = ()
    #: 2.1.1. None means unstated, and the section withholds rather than
    #: guessing — a pair of words adjacent by accident compounds nothing.
    connected: Optional[bool] = None

    def has(self, fact: str) -> bool:
        return fact in self.given

    def word(self, slot: str) -> str:
        return self.first if slot == "first" else self.second

    def vacana(self, slot: str) -> int:
        return self.first_vacana if slot == "first" else self.second_vacana

    def vibhakti(self, slot: str) -> Optional[int]:
        return (self.first_vibhakti if slot == "first"
                else self.second_vibhakti)


# ---------------------------------------------------------------------------
# The gaṇas the section reads from
# ---------------------------------------------------------------------------


def _saundadi() -> Tuple[str, ...]:
    """
    2.1.40's शौण्डादि, from the gaṇapāṭha on disk — thirteen words.

    Read rather than retyped, for the same reason 2.1.17's तिष्ठद्गु is:
    a list copied into the source is a second witness that can drift from
    the first, and there is no way to notice when it has.
    """
    from src.astadhyayi.formation import gana_items

    return gana_items("2.1.40", "śauṇḍādi")


SAUNDADI: Tuple[str, ...] = _saundadi()


def _gana(sutra_id: str, name: str) -> Tuple[str, ...]:
    """One gaṇa from the gaṇapāṭha on disk."""
    from src.astadhyayi.formation import gana_items

    return gana_items(sutra_id, name)


#: 2.1.56's व्याघ्रादि — twenty words, and the Kāśikā calls it an
#: आकृतिगण outright: आकृतिगणश्चायम्, तेनेदमपि भवति — मुखपद्मम्,
#: करकिसलयम्, पार्थिवचन्द्रः. The file marks it open too.
VYAGHRADI: Tuple[str, ...] = _gana("2.1.56", "vyāghrādi")

#: 2.2.9's याजकादि — thirteen words. The compound was available under
#: 2.2.8 already; this sūtra is a प्रतिप्रसव, a re-permission against the
#: prohibition 2.2.16 कर्तरि च lays down. That sūtra is not codified, so
#: what is held here is the permission and the reason for it.
YAJAKADI: Tuple[str, ...] = _gana("2.2.9", "yājakādi")

#: 2.1.70's श्रमणादि — fifteen words. The Kāśikā divides them by gender:
#: श्रमणा, प्रव्रजिता, कुलटा and the rest are feminine and take कुमारी,
#: while अध्यापक, अभिरूपक, पण्डित go either way — प्रातिपदिकग्रहणे
#: लिङ्गविशिष्टस्यापि ग्रहणम्. The division is recorded, not modelled:
#: gender is not something this table carries.
SRAMANADI: Tuple[str, ...] = _gana("2.1.70", "śramaṇādi")

#: 2.1.72's मयूरव्यंसकादि — eighty-three forms given whole, and the file
#: marks it open, as an आकृतिगण should be.
MAYURAVYAMSAKADI: Tuple[str, ...] = _gana("2.1.72", "mayūravyaṃsakādi")

#: 2.1.59's two lists, श्रेण्यादि and कृतादि — the words that are made
#: into something, and the words that make them so.
SRENYADI: Tuple[str, ...] = _gana("2.1.59", "śreṇyādi")
KRTADI: Tuple[str, ...] = _gana("2.1.59", "kṛtādi")


def _patresamita() -> Tuple[str, ...]:
    """
    2.1.48's पात्रेसमितादि, from the gaṇapāṭha — thirty-three forms.

    The Kāśikā calls it an आकृतिगण outright, and says why: अव्यक्तत्वाच्च
    आकृतिगणोऽयम् — what makes these compounds censorious cannot be spelt
    out, so the list cannot be closed. The file marks it open too.
    """
    from src.astadhyayi.formation import gana_items

    return gana_items("2.1.48", "pātresamitādi")


PATRESAMITADI: Tuple[str, ...] = _patresamita()


def tisthadgu() -> Tuple[str, ...]:
    """
    2.1.17's तिष्ठद्गुप्रभृतीनि, from the gaṇapāṭha.

    These are not derived — तिष्ठद्ग्वादयः समुदाया एव निपात्यन्ते, the whole
    forms are irregularly given, and the name is conferred on the finished
    word rather than on a pair to be joined. तिष्ठद्गु is a time of day, the
    one at which the cows stand to be milked, and no rule of the section
    would produce it.
    """
    return gana_items("2.1.17", "tiṣṭhadgu")


#: 2.1.10's first two. The third of its three is संख्या, which is not
#: written out — 1.1.23 is codified and `is_samkhya` already knows both the
#: numerals and the four words the sūtra admits alongside them.
_AKSA_SALAKA = ("akṣa", "śalākā")


# ---------------------------------------------------------------------------
# The provisions, 2.1.6 to 2.1.21
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Provision:
    """One compound rule, as its conditions."""

    sutra: str
    gives: Samasa = Samasa.AVYAYIBHAVA
    #: The words the sūtra names, and which member they must be.
    words: Tuple[str, ...] = ()
    slot: str = "first"
    #: Whether the named member must be an avyaya (2.1.6 only says so).
    avyaya: bool = False
    #: A sense the named member must be in, and one it must not.
    senses: Tuple[str, ...] = ()
    not_senses: Tuple[str, ...] = ()
    #: The case the *other* member must stand in.
    other_vibhakti: Optional[int] = None
    #: The case the member this sūtra *names* must stand in. 2.1.26 needs
    #: it: खट्वा is the word the rule names and it is the one standing in
    #: the second case — खट्वाशब्दो द्वितीयान्तः क्तान्तेन सह समस्यते.
    vibhakti: Optional[int] = None
    #: What the member the sūtra does *not* name must be, where it says.
    other_words: Tuple[str, ...] = ()
    #: Whether that other member may instead be a saṃkhyā — 2.1.10's third.
    other_samkhya: bool = False
    #: Whether the named member must itself be a saṃkhyā — 2.1.19, 2.1.20.
    samkhya: bool = False
    #: Facts from FACTS that must be asserted.
    requires: Tuple[str, ...] = ()
    #: Facts any one of which makes this row FORBID the compound outright,
    #: reported under this sūtra. 2.2.10 न निर्धारणे and 2.2.11 are
    #: prohibitions of 2.2.8, and they name classes rather than words, so
    #: `niyama_on` — which keys on a named word — cannot carry them.
    prohibits_when: Tuple[str, ...] = ()
    #: Facts whose presence keeps this row away — the mirror of `requires`.
    #: 2.1.58's nine words include पूर्व and अपर, and 2.1.50's own examples
    #: पूर्वेषुकामशमी and अपरेषुकामशमी are exactly those words with a name
    #: meant. Both rules reach them and 1.4.1 hands it to the later, which
    #: is 2.1.58 — and the Kāśikā cites the form under 2.1.50.
    refuses: Tuple[str, ...] = ()
    #: 2.1.10 wants akṣa and śalākā in the singular — एकत्वे अक्षशलाकयोः —
    #: and not the numerals beside them, since द्विपरि and त्रिपरि stand.
    singular_for: Tuple[str, ...] = ()
    #: Set only where the rule departs from the heading it stands under.
    nitya: bool = False
    #: The rule states its own option, rather than taking one from a
    #: heading. 2.2.3's अन्यतरस्याम् and 2.2.4, where the Kāśikā argues
    #: both readings stand — समासविधानात् सोऽपि भवति.
    vibhasa: bool = False
    #: 2.1.32's बहुलम्, which is neither नित्य nor विभाषा but wider than
    #: both: सर्वोपाधिव्यभिचारार्थं बहुलग्रहणम् — the word is there so that
    #: ANY of the conditions may be departed from. So दात्रेण धान्यं
    #: लूनवान् does not compound though it meets them, and पादहारकः does
    #: though it does not. Recorded rather than modelled; a rule that may
    #: ignore its own conditions cannot be run either way and be honest.
    bahula: bool = False
    #: 2.1.7 and 2.1.15 restate 2.1.6; the value is what the restating is for.
    restates: str = ""
    #: Words this rule *confines*. A restating rule can narrow rather than
    #: add: where 2.1.7 names यथा and excludes सादृश्य, यथा in that sense
    #: compounds by no rule at all, 2.1.6's list of sixteen notwithstanding.
    niyama_on: Tuple[str, ...] = ()
    #: 2.1.17's forms are given whole rather than made.
    #: 2.1.17's तिष्ठद्गुप्रभृति and 2.1.48's पात्रेसमितादि are given
    #: whole rather than made — समुदाया एव निपात्यन्ते. This holds the
    #: forms themselves. It was a bool wired to one gaṇa until a second
    #: rule wanted the same shape with a different list, which is when a
    #: flag standing for one particular answer stops being a flag.
    nipatana: Tuple[str, ...] = ()
    gloss: str = ""
    example: str = ""
    counter: str = ""

    @property
    def optional(self) -> bool:
        """
        2.1.11 विभाषा, read off the heading rather than repeated — and
        bounded to the pāda that heading is in.

        Reading it as "anything after 2.1.11" was right while 2.1 was all
        there was, and wrong the moment 2.2 existed: every rule of the new
        pāda came out optional without anything having said so. The text
        settles the bound. 2.2.3 says अन्यतरस्याम् itself and 2.2.4's
        Kāśikā argues सोऽपि भवति for its second reading; neither would be
        worth saying if an option were already in force overhead.
        """
        if self.nitya:
            return False
        if self.vibhasa:
            return True
        pada = self.sutra.rsplit(".", 1)[0]
        return pada == "2.1" and order_of(self.sutra) > order_of("2.1.11")

    def unmet(self, pair: Pair) -> Tuple[str, ...]:
        missing: List[str] = []
        mine = pair.word(self.slot)
        if self.nipatana:
            if mine not in self.nipatana and pair.second not in self.nipatana:
                missing.append(
                    f"not one of the {len(self.nipatana)} forms this sūtra "
                    f"gives whole")
            for fact in self.requires:
                if not pair.has(fact):
                    missing.append(f"{fact} not stated")
            return tuple(missing)
        if self.words and mine not in self.words:
            where = "first" if self.slot == "first" else "second"
            missing.append(
                f"{where} member is not one of {', '.join(self.words)}")
        if self.avyaya:
            from src.astadhyayi.avyaya import is_avyaya
            if not (is_avyaya(mine) or mine in _KNOWN_AVYAYA):
                missing.append(f"{mine} is not an avyaya")
        if self.samkhya and not is_samkhya(mine):
            missing.append(f"{mine} is not a saṃkhyā (1.1.23)")
        theirs = pair.word("second" if self.slot == "first" else "first")
        if self.other_words or self.other_samkhya:
            ok = theirs in self.other_words or (
                self.other_samkhya and is_samkhya(theirs))
            if not ok:
                wanted = list(self.other_words)
                if self.other_samkhya:
                    wanted.append("a saṃkhyā")
                missing.append(
                    f"the other member is not one of {', '.join(wanted)}")
        if self.senses and not (set(self.senses) & set(pair.first_sense)):
            missing.append("not used in the sense " + "/".join(self.senses))
        if self.not_senses and (set(self.not_senses) & set(pair.first_sense)):
            missing.append("used in the sense " + "/".join(self.not_senses)
                           + ", which this rule excludes")
        if self.vibhakti is not None:
            if pair.vibhakti(self.slot) != self.vibhakti:
                missing.append(
                    f"{self.slot} member is not in vibhakti {self.vibhakti}")
        if self.other_vibhakti is not None:
            other = "first" if self.slot == "second" else "second"
            if pair.vibhakti(other) != self.other_vibhakti:
                missing.append(
                    f"{other} member is not in vibhakti "
                    f"{self.other_vibhakti}")
        if self.singular_for:
            other = "second" if self.slot == "first" else "first"
            if theirs in self.singular_for and pair.vacana(other) != 1:
                missing.append(f"{theirs} is not in the singular")
        for fact in self.requires:
            if not pair.has(fact):
                missing.append(f"{fact} not stated")
        for fact in self.refuses:
            if pair.has(fact):
                missing.append(f"{fact} is stated, which this rule excludes")
        return tuple(missing)

    def applies(self, pair: Pair) -> bool:
        return not self.unmet(pair)

    def describe(self) -> str:
        parts: List[str] = []
        if self.words:
            parts.append(f"{self.slot} ∈ {{{', '.join(self.words)}}}")
        if self.avyaya:
            parts.append("first is an avyaya")
        if self.senses:
            parts.append("in the sense " + "/".join(self.senses))
        if self.not_senses:
            parts.append("not in the sense " + "/".join(self.not_senses))
        if self.vibhakti is not None:
            parts.append(f"{self.slot} in vibhakti {self.vibhakti}")
        if self.other_vibhakti is not None:
            parts.append(f"other member in vibhakti {self.other_vibhakti}")
        if self.samkhya:
            parts.append("first is a saṃkhyā")
        if self.other_words or self.other_samkhya:
            wanted = list(self.other_words)
            if self.other_samkhya:
                wanted.append("a saṃkhyā")
            parts.append(f"other ∈ {{{', '.join(wanted)}}}")
        if self.singular_for:
            parts.append("singular")
        parts.extend(self.requires)
        head = self.gives.value
        if self.optional:
            head = "optionally " + head
        return f"{head} when {'; '.join(parts)}" if parts else head


#: 2.1.6's sixteen senses, in the order the sūtra compounds them. The Kāśikā
#: notes वचनग्रहणं प्रत्येकं संबध्यते — the final वचन attaches to each item,
#: so each is "a word *denoting* that", not the thing itself.
VIBHAKTYADI: Tuple[str, ...] = (
    "vibhakti", "samīpa", "samṛddhi", "vyṛddhi", "arthābhāva", "atyaya",
    "asamprati", "śabdaprādurbhāva", "paścāt", "yathā", "ānupūrvya",
    "yaugapadya", "sādṛśya", "sampatti", "sākalya", "anta",
)

#: Words the section treats as avyaya that the avyaya module cannot yet reach
#: on its own — 1.1.37's svarādi list is not loaded, so these are named where
#: they are used rather than asserted globally.
_KNOWN_AVYAYA = frozenset({
    "adhi", "upa", "su", "dur", "nir", "ati", "yathā", "yāvat", "ā", "āṅ",
    "abhi", "prati", "anu", "apa", "pari", "bahis", "pra",
})


def _p(*args, **kwargs) -> Provision:
    return Provision(*args, **kwargs)


PROVISIONS: Tuple[Provision, ...] = (
    # --- obligatory, under 2.1.5 and before 2.1.11 ----------------------
    _p("2.1.6", avyaya=True, senses=VIBHAKTYADI,
       gloss="अव्ययं विभक्तिसमीप…अन्तवचनेषु — an indeclinable used in any of "
             "sixteen senses compounds with a subanta. The senses are the "
             "rule: अधिस्त्रि is the seventh case's sense, उपकुम्भम् is "
             "nearness, सुमद्रम् is thriving and दुर्यवनम् its want, "
             "निर्मक्षिकम् is absence and अतिहिमम् is a season gone by.",
       example="adhistri, upakumbham, sumadram, durgavadikam, nirmakṣikam, "
               "atihimam, atitaisṛkam",
       counter="a word in none of the sixteen senses — the list is the "
               "whole condition, and nothing else licenses the compound"),
    _p("2.1.7", words=("yathā",), avyaya=True, not_senses=("sādṛśya",),
       restates="सादृश्यप्रतिषेधार्थम्", niyama_on=("yathā",),
       gloss="यथासादृश्ये — यथा compounds when it is *not* similarity that "
             "is meant. यथावृद्धं ब्राह्मणानामन्त्रयस्व, invite the elders "
             "in order of age. The compound was already available from "
             "2.1.6, whose list holds both यथा and सादृश्य — यथार्थे यद् "
             "अव्ययम् इति पूर्वेणैव सिद्धे समासे वचनम् इदम् "
             "सादृश्यप्रतिषेधार्थम्. The rule exists to take a sense away.",
       example="yathāvṛddham, yathādhyāpakam",
       counter="yathā devadattas tathā yajñadattaḥ — plain likeness, and no "
               "compound"),
    _p("2.1.8", words=("yāvat",), avyaya=True, senses=("avadhāraṇa",),
       gloss="यावदवधारणे — यावत् compounds when an amount is being fixed. "
             "अवधारणम् इयत्तापरिच्छेदः: यावदमत्रं ब्राह्मणानामन्त्रयस्व, "
             "invite as many brahmins as there are vessels.",
       example="yāvadamatram",
       counter="yāvad dattaṃ tāvad bhuktam — no amount is being fixed, न "
               "अवधारयामि कियद् मया भुक्तम्"),
    _p("2.1.9", words=("prati",), slot="second", senses=("mātrā",),
       gloss="सुप्प्रतिना मात्रार्थे — a subanta compounds with प्रति when "
             "प्रति means a little of something. मात्रा बिन्दुः स्तोकम् "
             "अल्पम् इति पर्यायाः: शाकप्रति, a bit of greens. Note where "
             "प्रति stands — this is the first rule of the section whose "
             "named word is the *second* member. And सुप् is said again "
             "though it is already carried down, अव्ययनिवृत्त्यर्थम्, to "
             "keep 2.1.6's avyaya out of the first slot.",
       example="śākaprati, sūpaprati",
       counter="vṛkṣaṃ prati vidyotate vidyut — प्रति in its ordinary sense"),
    _p("2.1.10", words=("pari",), slot="second",
       other_words=_AKSA_SALAKA, other_samkhya=True,
       singular_for=_AKSA_SALAKA, requires=("kitava-vyavahāra",),
       gloss="अक्षशलाकासंख्याः परिणा — अक्ष, शलाका and a numeral compound "
             "with परि. कितवव्यवहारे समासोऽयम् इष्यते: the throw of five "
             "dice where all but one fall alike, अक्षपरि, एकपरि, द्विपरि, "
             "at most चतुष्परि — for at five there is no losing throw left "
             "to name.",
       example="akṣapari, śalākāpari, ekapari, catuṣpari",
       counter="the same words outside the gamblers' usage"),
    # --- 2.1.11 विभाषा, and everything after it is optional -------------
    _p("2.1.12", words=("apa", "pari", "bahis", "añc"), other_vibhakti=5,
       gloss="अपपरिबहिरञ्चवः पञ्चम्या — these four compound with a fifth "
             "case. अपत्रिगर्तं वृष्टो देवः, it rained everywhere but "
             "Trigarta. And the rule is a ज्ञāपaka besides: "
             "बहिःशब्दयोगे पञ्चमीभावस्य एतद् एव ज्ञापकम् — that बहिस् takes "
             "a fifth case at all is known from its being named here.",
       example="apatrigartam, paritrigartam, bahirgrāmam, prāggrāmam",
       counter="the same words with any other case"),
    _p("2.1.13", words=("ā", "āṅ"), other_vibhakti=5,
       senses=("maryādā", "abhividhi"),
       gloss="आङ् मर्यादाभिविध्योः — आङ् compounds with a fifth case in "
             "either of its two senses: a limit that excludes, "
             "आपाटलिपुत्रं वृष्टो देवः, as far as Pāṭaliputra and not "
             "beyond; or one that includes, आकुमारं यशः पाणिनेः, Pāṇini's "
             "fame reaching even to children.",
       example="āpāṭaliputram in maryādā, ākumāram in abhividhi",
       counter="āṅ in neither sense"),
    _p("2.1.14", words=("abhi", "prati"), senses=("ābhimukhya",),
       requires=("lakṣaṇa",),
       gloss="लक्षणेनाभिप्रती आभिमुख्ये — अभि and प्रति compound with a word "
             "naming a mark, when facing it is meant. लक्षणं चिह्नम्: "
             "अभ्यग्नि शलभाः पतन्ति, the moths fall towards the fire, "
             "having made the fire their mark.",
       example="abhyagni, pratyagni",
       counter="srughnaṃ pratigataḥ — no mark; येनाग्निस्तेन गतः — neither "
               "word; abhyaṅkā gāvaḥ — not facing, but freshly branded"),
    _p("2.1.15", words=("anu",), senses=("samīpa",), requires=("lakṣaṇa",),
       restates="विभाषार्थम्",
       gloss="अनुर्यत्समया — अनु compounds with a word naming a mark, when "
             "अनु means near it. समया समीपम्: अनुवनम् अशनिर्गतः, the "
             "lightning went along by the wood. Already available from "
             "2.1.6, whose list holds समीप — इत्येव सिद्धे पुनर्वचनं "
             "विभाषार्थम्. The restatement is not for the sense but for the "
             "option: standing under 2.1.11 it makes the compound optional.",
       example="anuvanam",
       counter="vanaṃ samayā — no anu; vṛkṣam anu vidyotate vidyut — anu, "
               "but not in the sense of nearness"),
    _p("2.1.16", words=("anu",), senses=("āyāma",), requires=("lakṣaṇa",),
       gloss="यस्य चायामः — and अनु compounds with a mark whose *length* is "
             "what is meant. आयामो दैर्घ्यम्: अनुगङ्गं वाराणसी, Vārāṇasī "
             "along the Ganges — the river's extent measuring the city's.",
       example="anugaṅgaṃ vārāṇasī, anuyamunaṃ mathurā",
       counter="vṛkṣam anu vidyotate vidyut — no length is meant"),
    _p("2.1.17", nipatana=tisthadgu(),
       gloss="तिष्ठद्गुप्रभृतीनि च — and the तिष्ठद्गु forms are given "
             "whole. तिष्ठद्ग्वादयः समुदाया एव निपात्यन्ते: the name is "
             "conferred on a finished word, not on a pair to be joined. "
             "तिष्ठद्गु is a time of day — तिष्ठन्ति गावो यस्मिन् काले "
             "दोहनाय. The च is अवधारणार्थ, and shuts the list: अपरः समासो "
             "न भवति, no परमतिष्ठद्गु.",
       example="tiṣṭhadgu, vahadgu, khaleyavam, prāhṇam, pradakṣiṇam, "
               "daṇḍādaṇḍi",
       counter="paramatiṣṭhadgu — the च forbids compounding one of these "
               "again"),
    _p("2.1.18", words=("pāre", "madhye"), other_vibhakti=6,
       gloss="पारे मध्ये षष्ठ्या वा — पारे and मध्ये compound with a sixth "
             "case. षष्ठीसमासे प्राप्ते तदपवादः अव्ययीभाव आरभ्यते: the "
             "genitive tatpuruṣa was already available and this displaces "
             "it — but वावचनात् षष्ठीसमासोऽपि पक्षे अभ्यनुज्ञायते, the वा "
             "lets it back in, so पारेगङ्गम् and गङ्गापारम् both stand. The "
             "ए of पारे and मध्ये is निपातित along with the rule: "
             "तत्सन्नियोगेन चानयोः एकारान्तत्वं निपात्यते.",
       example="pāregaṅgam, madhyegaṅgam (against gaṅgāpāram, gaṅgāmadhyam)",
       counter="the same words with any other case"),
    _p("2.1.19", samkhya=True, requires=("vaṃśya",),
       gloss="संख्या वंश्येन — a numeral compounds with a word naming "
             "someone in a lineage. विद्यया जन्मना वा प्राणिनाम् "
             "एकलक्षणसन्तानो वंशः: द्विमुनि व्याकरणस्य, the grammar of the "
             "two sages — a lineage of learning; एकविंशतिभारद्वाजम्, one of "
             "birth.",
       example="dvimuni vyākaraṇasya, trimuni, ekaviṃśatibhāradvājam",
       counter="a numeral with anything not standing in a lineage"),
    _p("2.1.20", samkhya=True, requires=("nadī", "samāhāra"),
       gloss="नदीभिश्च — and a numeral with river-names. समाहारे चायम् "
             "इष्यते, an aggregate being meant: पञ्चनदम्, the five-river "
             "country; सप्तगङ्गम्, सप्तगोदावरम्.",
       example="pañcanadam, saptagaṅgam, dviyamunam",
       counter="rivers counted severally rather than as one tract"),
    _p("2.1.21", requires=("nadī", "anya-padārtha", "saṃjñā"), nitya=True,
       gloss="अन्यपदार्थे च संज्ञायाम् — and a river-name compounds with a "
             "word, for a third thing's sake, when the whole is a proper "
             "name. उन्मत्तगङ्गं नाम देशः, the country called Mad-Ganges — "
             "neither the madness nor the river but the place. And though "
             "2.1.11 governs here the compound is obligatory: "
             "विभाषाधिकारेऽपि नित्यसमास एव अयम्, नहि वाक्येन संज्ञा गम्यते. "
             "There is no phrase to fall back to, because a phrase would "
             "not be the name.",
       example="unmattagaṅgam, lohitagaṅgam, kṛṣṇagaṅgam",
       counter="kṛṣṇaveṇṇā — no third thing; śīghragaṅgo deśaḥ — a "
               "description, not a name"),

    # -- 2.1.22 तत्पुरुषः opens here. The heading is in SAMJNAS; these are
    #    the rules it names. सुप् सुपा is still overhead, and so is 2.1.11
    #    विभाषा — the Kāśikā confirms it at 2.1.26 by having to escape it.
    _p("2.1.24", gives=Samasa.TATPURUSA, slot="second",
       words=("śrita", "atīta", "patita", "gata", "atyasta", "prāpta",
              "āpanna"),
       other_vibhakti=2,
       gloss="द्वितीया श्रितातीतपतितगतात्यस्तप्राप्तापन्नैः — a word in the "
             "second case compounds with one of these seven. सुप् सुपेति "
             "वर्तते, तस्य विशेषणम् एतद्: the heading supplies the two "
             "words and this sūtra qualifies them, the first by its case "
             "and the second by name. कष्टं श्रितः gives कष्टश्रितः — "
             "someone resorted to hardship, and by 2.1.22 the compound "
             "means the person and not the hardship.",
       example="kaṣṭaśritaḥ, narakaśritaḥ, kāntārātītaḥ, narakapatitaḥ, "
               "grāmagataḥ, taraṅgātyastaḥ, sukhaprāptaḥ, sukhāpannaḥ",
       counter="a first member in any other case"),
    _p("2.1.24", gives=Samasa.TATPURUSA, slot="second",
       words=("gamī", "gāmī", "bubhukṣu"),
       other_vibhakti=2,
       gloss="श्रितादिषु गमिगाम्यादीनाम् उपसंख्यानम् — Kātyāyana adds गमि, "
             "गामी and their like to the seven. ग्रामं गमी gives "
             "ग्रामगमी; ओदनं बुभुक्षुः gives ओदनबुभुक्षुः. The vārttika "
             "names the stems गमि and गामि; what stands in the compound "
             "is गमी and गामी, and the table holds the forms the Kāśikā "
             "actually works. Kept as a second row rather than folded "
             "into the list above, because the sūtra names seven and the "
             "vārttika is what adds the rest.",
       example="grāmagamī, grāmagāmī, odanabubhukṣuḥ",
       counter="the same words with a first member not in the second case"),
    _p("2.1.25", gives=Samasa.TATPURUSA, words=("svayam",),
       requires=("kta",),
       gloss="स्वयं क्तेन — स्वयम् compounds with a क्त-form. The द्वितीया "
             "of 2.1.24 is carried down but cannot bite: स्वयम् is an "
             "avyaya standing for आत्मना, and तस्य द्वितीयया सह संबन्धो "
             "नोपपद्यते — it takes no case at all. So the Kāśikā reads the "
             "anuvṛtti as passing through for the sūtras after this one, "
             "द्वितीयाग्रहणम् उत्तरार्थम् अनुवर्तते, and this rule asks no "
             "case of its member.",
       example="svayaṃdhautau pādau, svayaṃvilīnam ājyam",
       counter="svayam with anything not ending in क्त"),
    _p("2.1.26", gives=Samasa.TATPURUSA, words=("khaṭvā",), vibhakti=2,
       requires=("kta", "kṣepa"), nitya=True,
       gloss="खट्वा क्षेपे — खट्वा in the second case compounds with a "
             "क्त-form when censure is meant. Obligatory though 2.1.11 "
             "governs: विभाषाधिकारेऽपि नित्यसमास एवायम्, नहि वाक्येन क्षेपो "
             "गम्यते — the phrase cannot carry the insult, so there is no "
             "alternative to fall back to. The bed is not the point; "
             "खट्वारोहणम् इह विमार्गप्रस्थानस्य उपलक्षणम्, and सर्व एव "
             "अविनीतः खट्वारूढ इत्युच्यते.",
       example="khaṭvārūḍho jālmaḥ, khaṭvāplutaḥ",
       counter="khaṭvām ārūḍhaḥ — a man who climbed onto a bed, no censure"),
    _p("2.1.27", gives=Samasa.TATPURUSA, words=("sāmi",),
       requires=("kta",),
       gloss="सामि — and सामि with a क्त-form. सामि is an avyaya and a "
             "synonym of अर्ध, half; असत्त्ववाचित्वात् it names no thing "
             "and so, like स्वयम्, takes no second case. ऐकपद्यम् "
             "ऐकस्वर्यं च समासत्वाद् भवति — one word and one accent, which "
             "is what being a compound gets you.",
       example="sāmikṛtam, sāmipītam, sāmibhuktam",
       counter="sāmi with anything not ending in क्त"),
    _p("2.1.28", gives=Samasa.TATPURUSA, vibhakti=2,
       requires=("kāla", "kta"),
       gloss="कालाः — words naming a time, in the second case, with a "
             "क्त-form. काला इति न स्वरूपविधिः: the rule is not about the "
             "word काल but about any word that means a stretch of time. "
             "अनत्यन्तसंयोगार्थं वचनम् — it is here for the case where the "
             "time is *not* wholly taken up, 2.1.29 taking the other.",
       example="ahaḥsaṃkrāntāḥ, rātrisaṃkrāntāḥ, māsapramitaś candramāḥ",
       counter="a time-word with a second member not ending in क्त"),
    # -- तृतीया, 2.1.30 to 2.1.35 -------------------------------------
    _p("2.1.30", gives=Samasa.TATPURUSA, slot="second", other_vibhakti=3,
       requires=("guṇavacana", "tatkṛta"),
       gloss="तृतीया तत्कृतार्थेन गुणवचनेन — a third-case word compounds "
             "with a quality-word, and the quality must be one THAT WORD "
             "brought about: तत्कृतेन तदर्थकृतेन. शङ्कुलया खण्डः gives "
             "शङ्कुलाखण्डः, broken by the spike.",
       example="śaṅkulākhaṇḍaḥ, kirikāṇaḥ",
       counter="अक्ष्णा काणः — blind in the eye, not blinded by it"),
    _p("2.1.30", gives=Samasa.TATPURUSA, slot="second", words=("artha",),
       other_vibhakti=3,
       gloss="तृतीया … अर्थेन — and with the word अर्थ. धान्येनार्थः gives "
             "धान्यार्थः. A second row because अर्थ is named by its own "
             "form and needs none of the quality conditions.",
       example="dhānyārthaḥ",
       counter="a first member in any other case"),
    _p("2.1.31", gives=Samasa.TATPURUSA, slot="second", other_vibhakti=3,
       words=("pūrva", "sadṛśa", "sama", "ūna", "vikala", "kalaha",
              "nipuṇa", "miśra", "ślakṣṇa"),
       gloss="पूर्वसदृशसमोनार्थकलहनिपुणमिश्रश्लक्ष्णैः — eight words, and "
             "the third case comes from this very sūtra: अस्मादेव वचनात् "
             "पूर्वादिभिर्योगे तृतीया भवति. मासेन पूर्वः gives मासपूर्वः. "
             "ऊनार्थ is a sense and not a form, so विकल stands beside ऊन.",
       example="māsapūrvaḥ, mātṛsadṛśaḥ, mātṛsamaḥ, māṣonam, "
               "māṣavikalam, asikalahaḥ, vāgnipuṇaḥ, guḍamiśraḥ, "
               "ācāraślakṣṇaḥ",
       counter="the same words with a first member in another case"),
    _p("2.1.31", gives=Samasa.TATPURUSA, slot="second", words=("avara",),
       other_vibhakti=3,
       gloss="पूर्वादिष्ववरस्योपसंख्यानम् — Kātyāyana adds अवर to the "
             "eight: मासेनावरः gives मासावरः.",
       example="māsāvaraḥ, saṃvatsarāvaraḥ",
       counter="a first member not in the third case"),
    _p("2.1.32", gives=Samasa.TATPURUSA, slot="second", other_vibhakti=3,
       requires=("kartṛ-karaṇa", "kṛdanta"), bahula=True,
       gloss="कर्तृकरणे कृता बहुलम् — a third case in the agent or "
             "instrument sense, with a कृत्-ending word. अहिना हतः gives "
             "अहिहतः; नखैर्निर्भिन्नः gives नखनिर्भिन्नः. The बहुलम् is "
             "there सर्वोपाधिव्यभिचारार्थम्, so every condition here may "
             "be departed from in either direction.",
       example="ahihataḥ, nakhanirbhinnaḥ, paraśucchinnaḥ",
       counter="भिक्षाभिरुषितः — the case is in neither sense; and "
               "दात्रेण धान्यं लूनवान्, which meets the conditions and "
               "still does not compound"),
    _p("2.1.33", gives=Samasa.TATPURUSA, slot="second", other_vibhakti=3,
       requires=("kartṛ-karaṇa", "adhikārtha"),
       gloss="कृत्यैरधिकार्थवचने — with a कृत्य affix, where more is said "
             "than meant: काकपेया नदी, a river so shallow crows might "
             "drink it. पूर्वस्यैवायं प्रपञ्चः, an unfolding of 2.1.32. "
             "The vārttika narrows the affix — कृत्यग्रहणे यण्ण्यतोर् "
             "ग्रहणं कर्तव्यम् — so काकैः पातव्या is left out.",
       example="kākapeyā nadī, śvalehyaḥ kūpaḥ, bāṣpacchedyāni tṛṇāni",
       counter="काकैः पातव्या — तव्य is not among the two admitted"),
    _p("2.1.34", gives=Samasa.TATPURUSA, other_vibhakti=None, vibhakti=3,
       requires=("vyañjana", "anna"),
       gloss="अन्नेन व्यञ्जनम् — a relish in the third case with a "
             "food-word. दध्ना उपसिक्त ओदनः gives दध्योदनः. संस्कार्यम् "
             "अन्नम्, संस्कारकं व्यञ्जनम् — the food is what is dressed "
             "and the relish is what dresses it.",
       example="dadhyodanaḥ, kṣīraudanaḥ",
       counter="either word standing in another case"),
    _p("2.1.35", gives=Samasa.TATPURUSA, vibhakti=3,
       requires=("miśrīkaraṇa", "bhakṣya"),
       gloss="भक्ष्येण मिश्रीकरणम् — what does the mixing, in the third "
             "case, with what is eaten. गुडेन मिश्रा धानाः gives "
             "गुडधानाः.",
       example="guḍadhānāḥ, guḍapṛthukāḥ",
       counter="either word standing in another case"),

    # -- चतुर्थी, 2.1.36 ------------------------------------------------
    _p("2.1.36", gives=Samasa.TATPURUSA, slot="second", other_vibhakti=4,
       requires=("prakṛti-vikāra",),
       gloss="चतुर्थी तदर्थ… — a fourth-case word with what it is FOR, "
             "and the two must stand as material and product: तदर्थेन "
             "प्रकृतिविकारभावे समासोऽयम् इष्यते. यूपाय दारु gives "
             "यूपदारु.",
       example="yūpadāru, kuṇḍalahiraṇyam",
       counter="रन्धनाय स्थाली — a pot for cooking is not cooking made "
               "of pot"),
    _p("2.1.36", gives=Samasa.TATPURUSA, slot="second", words=("artha",),
       other_vibhakti=4, nitya=True,
       gloss="चतुर्थी … अर्थेन — and with अर्थ, where the vārttika makes "
             "the compound obligatory and of every gender: अर्थेन "
             "नित्यसमासवचनं सर्वलिङ्गता च वक्तव्या. ब्राह्मणार्थं पयः, "
             "ब्राह्मणार्था यवागूः. नहि वाक्येन तादर्थ्यं गम्यते.",
       example="brāhmaṇārthaṃ payaḥ, brāhmaṇārthā yavāgūḥ",
       counter="a first member not in the fourth case"),
    _p("2.1.36", gives=Samasa.TATPURUSA, slot="second", other_vibhakti=4,
       words=("bali", "hita", "sukha", "rakṣita"),
       gloss="चतुर्थी … बलिहितसुखरक्षितैः — and with these four, which "
             "need no material-and-product reading. कुबेराय बलिः gives "
             "कुबेरबलिः; गोहितम्, गोसुखम्, गोरक्षितम्.",
       example="kuberabaliḥ, gohitam, gosukham, gorakṣitam",
       counter="a first member not in the fourth case"),

    # -- पञ्चमी, 2.1.37 to 2.1.39 ---------------------------------------
    _p("2.1.37", gives=Samasa.TATPURUSA, slot="second", words=("bhaya",),
       other_vibhakti=5,
       gloss="पञ्चमी भयेन — a fifth-case word with भय. वृकेभ्यो भयम् "
             "gives वृकभयम्.",
       example="vṛkabhayam, caurabhayam, dasyubhayam",
       counter="a first member not in the fifth case"),
    _p("2.1.37", gives=Samasa.TATPURUSA, slot="second", other_vibhakti=5,
       words=("bhīta", "bhīti", "bhī"),
       gloss="भयभीतभीतिभीभिरिति वक्तव्यम् — the vārttika adds three more "
             "of the same root: वृकभीतः, वृकभीतिः, वृकभीः. पूर्वस्यैवायं "
             "बहुलग्रहणस्य प्रपञ्चः, an unfolding of 2.1.32's बहुल.",
       example="vṛkabhītaḥ, vṛkabhītiḥ, vṛkabhīḥ",
       counter="a first member not in the fifth case"),
    _p("2.1.38", gives=Samasa.TATPURUSA, slot="second", other_vibhakti=5,
       words=("apeta", "apoḍha", "mukta", "patita", "apatrasta"),
       requires=("alpaśaḥ",),
       gloss="अपेतापोढमुक्तपतितापत्रस्तैरल्पशः — five words, and अल्पशः "
             "says how far the rule reaches: अल्पा पञ्चमी समस्यते न "
             "सर्वा. सुखापेतः, चक्रमुक्तः, स्वर्गपतितः. "
             "कर्तृकरणे कृता बहुलम् इत्यस्यैवायं प्रपञ्चः.",
       example="sukhāpetaḥ, kalpanāpoḍhaḥ, cakramuktaḥ, svargapatitaḥ, "
               "taraṅgāpatrastaḥ",
       counter="प्रासादात् पतितः, भोजनादपत्रस्तः — the same words, and "
               "the usage does not admit them"),
    _p("2.1.39", gives=Samasa.TATPURUSA, vibhakti=5,
       requires=("kta",),
       words=("stoka", "antika", "abhyāśa", "dūra", "viprakṛṣṭa",
              "kṛcchra"),
       gloss="स्तोकान्तिकदूरार्थकृच्छ्राणि क्तेन — words MEANING little, "
             "near or far, and कृच्छ्र by its own form, with a क्त-form. "
             "स्तोकान्मुक्तः, अन्तिकादागतः, दूरादागतः, कृच्छ्रान्मुक्तः. "
             "The …अर्थ is why अभ्याश and विप्रकृष्ट stand beside them.",
       example="stokānmuktaḥ, antikādāgataḥ, abhyāśādāgataḥ, "
               "dūrādāgataḥ, kṛcchrānmuktaḥ",
       counter="the same words with a second member not ending in क्त"),

    # -- सप्तमी, 2.1.40 --------------------------------------------------
    _p("2.1.40", gives=Samasa.TATPURUSA, slot="second", other_vibhakti=7,
       words=SAUNDADI,
       gloss="सप्तमी शौण्डैः — a seventh-case word with शौण्ड and its "
             "class. अक्षेषु शौण्डः gives अक्षशौण्डः. The gaṇa is read "
             "from the gaṇapāṭha, thirteen words. वृत्तौ "
             "प्रसक्तिक्रियाया अन्तर्भावात् अक्षादिष्वधिकरणे सप्तमी — the "
             "locative is one of place, the activity being folded into "
             "the compound.",
       example="akṣaśauṇḍaḥ, akṣadhūrtaḥ, akṣakitavaḥ",
       counter="a first member not in the seventh case"),

    # -- सप्तमी continues, 2.1.41 to 2.1.48 ------------------------------
    _p("2.1.41", gives=Samasa.TATPURUSA, slot="second", other_vibhakti=7,
       words=("siddha", "śuṣka", "pakva", "bandha"),
       gloss="सिद्धशुष्कपक्वबन्धैश्च — सप्तमी carries down, and four more "
             "words come with it: साङ्काश्यसिद्धः, आतपशुष्कः, "
             "स्थालीपक्वः, चक्रबन्धः. बहुलग्रहणस्यैवायम् "
             "उदाहरणप्रपञ्चः — an unfolding of 2.1.32's बहुल.",
       example="sāṅkāśyasiddhaḥ, ātapaśuṣkaḥ, sthālīpakvaḥ, cakrabandhaḥ",
       counter="a first member not in the seventh case"),
    _p("2.1.42", gives=Samasa.TATPURUSA, other_vibhakti=7, slot="second",
       requires=("dhvāṅkṣa", "kṣepa"),
       gloss="ध्वाङ्क्षेण क्षेपे — with a word for a crow, in censure. "
             "तीर्थे ध्वाङ्क्ष इव gives तीर्थध्वाङ्क्षः, someone who will "
             "not stay put. ध्वाङ्क्षेणेत्यर्थग्रहणम्, so काक and वायस "
             "serve as well.",
       example="tīrthadhvāṅkṣaḥ, tīrthakākaḥ, tīrthavāyasaḥ",
       counter="तीर्थे ध्वाङ्क्षस्तिष्ठति — a crow at a ford, no censure"),
    _p("2.1.43", gives=Samasa.TATPURUSA, other_vibhakti=7, slot="second",
       requires=("kṛtya-yat", "ṛṇa"),
       gloss="कृत्यैरृणे — with a कृत्य in यत्, where a debt is meant. "
             "मासे देयम् ऋणम् gives मासदेयम्. ऋणग्रहणं "
             "नियोगोपलक्षणार्थम् — the word stands for obligation "
             "generally, so पूर्वाह्णे गेयं साम gives पूर्वाह्णगेयम् too.",
       example="māsadeyam, saṃvatsaradeyam, pūrvāhṇageyam",
       counter="मासे देया भिक्षा — alms owed by the month is no debt"),
    _p("2.1.44", gives=Samasa.TATPURUSA, vibhakti=7, nitya=True,
       requires=("saṃjñā",),
       gloss="संज्ञायाम् — a seventh-case word with any सुप्, where the "
             "whole is a proper name. Obligatory though 2.1.11 governs: "
             "नहि वाक्येन संज्ञा गम्यते, the same argument 2.1.21 makes. "
             "अरण्येतिलकाः, वनेकिंशुकाः, कूपेपिशाचकाः.",
       example="araṇyetilakāḥ, vanekiṃśukāḥ, kūpepiśācakāḥ",
       counter="the same words where no name is meant"),
    _p("2.1.45", gives=Samasa.TATPURUSA, vibhakti=7,
       requires=("ahorātra-avayava", "kta"),
       gloss="क्तेनाहोरात्रावयवाः — the PARTS of a day or night, in the "
             "seventh case, with a क्त-form: पूर्वाह्णकृतम्, "
             "अपररात्रकृतम्. अवयवग्रहणं किम्? अहनि भुक्तम् — the whole "
             "day is not a part of one.",
       example="pūrvāhṇakṛtam, aparāhṇakṛtam, pūrvarātrakṛtam",
       counter="अहनि भुक्तम्, रात्रौ वृत्तम् — the whole, not a part"),
    _p("2.1.46", gives=Samasa.TATPURUSA, vibhakti=7, words=("tatra",),
       requires=("kta",),
       gloss="तत्र — the word तत्र with a क्त-form. तत्रभुक्तम्, "
             "तत्रकृतम्, तत्रपीतम्. ऐकपद्यम् ऐकस्वर्यं च समासत्वाद् "
             "भवति — one word and one accent, which is what being a "
             "compound gets you.",
       example="tatrabhuktam, tatrakṛtam, tatrapītam",
       counter="तत्र with anything not ending in क्त"),
    _p("2.1.47", gives=Samasa.TATPURUSA, vibhakti=7,
       requires=("kta", "kṣepa"),
       gloss="क्षेपे — a seventh-case word with a क्त-form, in censure. "
             "क्षेपो निन्दा, and what these name is effort thrown away: "
             "उदकेविशीर्णम्, भस्मनिहुतम् — an oblation poured on ashes. "
             "निष्फलं यत् क्रियते तद् एवम् उच्यते.",
       example="avataptenakulasthitam, udakeviśīrṇam, bhasmanihutam",
       counter="the same pairs where nothing is being derided"),
    _p("2.1.48", gives=Samasa.TATPURUSA, nipatana=PATRESAMITADI,
       requires=("kṣepa",),
       gloss="पात्रेसमितादयश्च — thirty-three forms given whole: "
             "समुदाया एव निपात्यन्ते. पात्रेसमिताः, gathered at the dish "
             "and nowhere useful; कूपमण्डूकः, a frog in a well. "
             "अव्यक्तत्वाच्च आकृतिगणोऽयम् — what makes them censorious "
             "cannot be spelt out, so the list stays open.",
       example="pātresamitāḥ, pātrebahulāḥ, kūpamaṇḍūkaḥ",
       counter="anything not among the forms the sūtra gives"),

    # -- समानाधिकरण, 2.1.49 to 2.1.51 ------------------------------------
    _p("2.1.49", gives=Samasa.TATPURUSA, requires=("samānādhikaraṇa",),
       words=("pūrvakāla", "eka", "sarva", "jarat", "purāṇa", "nava",
              "kevala"),
       gloss="पूर्वकालैकसर्वजरत्पुराणनवकेवलाः समानाधिकरणेन — seven words "
             "with one that refers to the same thing. पूर्वकाल is a "
             "SENSE and the other six are their own forms: "
             "पूर्वकालोऽपरकालेन समस्यते, so स्नातानुलिप्तः, bathed and "
             "then anointed. एकशाटी, सर्वदेवाः, जरद्धस्ती, पुराणान्नम्.",
       example="snātānuliptaḥ, ekaśāṭī, sarvadevāḥ, jaraddhastī, "
               "purāṇānnam, navānnam, kevalānnam",
       counter="एकस्याः शाटी — the two do not refer to one thing"),
    _p("2.1.50", gives=Samasa.TATPURUSA, requires=("dik", "samānādhikaraṇa",
                                                   "saṃjñā"),
       gloss="दिक्संख्ये संज्ञायाम् — a direction-word with one referring "
             "to the same thing, where the whole is a name: "
             "पूर्वेषुकामशमी.",
       example="pūrveṣukāmaśamī, apareṣukāmaśamī",
       counter="उत्तरा वृक्षाः — northern trees, and no name meant"),
    _p("2.1.50", gives=Samasa.TATPURUSA, samkhya=True,
       requires=("samānādhikaraṇa", "saṃjñā"),
       gloss="दिक्संख्ये संज्ञायाम् — and a numeral likewise: पञ्चाम्राः, "
             "सप्तर्षयः, the Seven Sages.",
       example="pañcāmrāḥ, saptarṣayaḥ",
       counter="पञ्च ब्राह्मणाः — five brahmins, and no name meant"),
    _p("2.1.51", gives=Samasa.TATPURUSA, samkhya=True,
       requires=("samānādhikaraṇa", "samāhāra"),
       gloss="तद्धितार्थोत्तरपदसमाहारे च — दिक्संख्ये carries down, and "
             "these compound in three cases besides the name: before a "
             "taddhita sense, before a further member, or where an "
             "aggregate is meant. समाहारे दिक्शब्दो न संभवति — a "
             "direction cannot be an aggregate, so only the numeral "
             "reaches this one. पञ्चपूली, दशकुमारि, which 2.4.17 makes "
             "neuter and 1.2.47 shortens.",
       example="pañcapūlī, daśapūlī, pañcakumāri, daśakumāri",
       counter="a numeral with a word it does not agree with"),
    _p("2.1.51", gives=Samasa.TATPURUSA, samkhya=True,
       requires=("samānādhikaraṇa", "taddhitārtha"),
       gloss="तद्धितार्थे — before a taddhita sense: पञ्चभिर्नापितैः "
             "क्रीतः gives पाञ्चनापितिः; पञ्चकपालः. For a direction-word "
             "the same: पूर्वस्यां शालायां भवः gives पौर्वशालः by 4.2.107.",
       example="pāñcanāpitiḥ, pañcakapālaḥ, paurvaśālaḥ",
       counter="the same pair with no taddhita following"),
    _p("2.1.51", gives=Samasa.TATPURUSA, samkhya=True,
       requires=("samānādhikaraṇa", "uttarapada"),
       gloss="उत्तरपदे — before a further member: पञ्चगवधनः, दशगवधनः; "
             "and for a direction-word पूर्वशालाप्रियः.",
       example="pañcagavadhanaḥ, daśagavadhanaḥ, pūrvaśālāpriyaḥ",
       counter="the same pair standing alone"),

    # -- 2.1.53 to 2.1.61. समानाधिकरणेन carries to the end of the pāda —
    #    समानाधिकरणेन इत्या पादसमाप्तेर् अनुवर्तते — so every rule from
    #    here on asks it, and none of them asks a vibhakti.
    _p("2.1.53", gives=Samasa.TATPURUSA,
       requires=("kutsita", "kutsana", "samānādhikaraṇa"),
       gloss="कुत्सितानि कुत्सनैः — a word for what is being run down, "
             "with a word that runs it down. वैयाकरणखसूचिः, a grammarian "
             "who is all thumbs. The rule exists for the ORDER: 2.1.57 "
             "would put the qualifier first, and this puts the qualified "
             "word first instead — विशेष्यस्य पूर्वनिपातार्थ आरम्भः.",
       example="vaiyākaraṇakhasūciḥ, yājñikakitavaḥ",
       counter="वैयाकरणश्चौरः — it is not his grammar being faulted"),
    _p("2.1.54", gives=Samasa.TATPURUSA, words=("pāpa", "aṇaka"),
       requires=("kutsita", "samānādhikaraṇa"),
       gloss="पापाणके कुत्सितैः — पाप and अणक with a word for what is "
             "run down. Both are terms of abuse and 2.1.53 would have "
             "put them second; this is here to put them first. "
             "पापनापितः, अणककुलालः.",
       example="pāpanāpitaḥ, pāpakulālaḥ, aṇakanāpitaḥ",
       counter="either word with something not being faulted"),
    _p("2.1.55", gives=Samasa.TATPURUSA,
       requires=("upamāna", "sāmānya-vacana", "samānādhikaraṇa"),
       gloss="उपमानानि सामान्यवचनैः — what a thing is likened TO, with "
             "the property they share. शस्त्रीव श्यामा gives "
             "शस्त्रीश्यामा, dark as a knife. कुमुदश्येनी, हंसगद्गदा, "
             "न्यग्रोधपरिमण्डला.",
       example="śastrīśyāmā, kumudaśyenī, haṃsagadgadā",
       counter="फाला इव तण्डुलाः — no shared property is named"),
    _p("2.1.56", gives=Samasa.TATPURUSA, slot="second", words=VYAGHRADI,
       requires=("upamita", "sāmānya-aprayoga", "samānādhikaraṇa"),
       gloss="उपमितं व्याघ्रादिभिः सामान्याप्रयोगे — what IS likened, "
             "with व्याघ्र and its class, when the shared property is "
             "left unsaid. पुरुषोऽयं व्याघ्र इव gives पुरुषव्याघ्रः. "
             "आकृतिगणश्चायम्, so मुखपद्मम् and पार्थिवचन्द्रः stand too.",
       example="puruṣavyāghraḥ, puruṣasiṃhaḥ",
       counter="पुरुषोऽयं व्याघ्र इव शूरः — say शूर and the rule stops"),
    _p("2.1.57", gives=Samasa.TATPURUSA, bahula=True,
       requires=("viśeṣaṇa", "viśeṣya", "samānādhikaraṇa"),
       gloss="विशेषणं विशेष्येण बहुलम् — a qualifier with what it "
             "qualifies: नीलोत्पलम्. Here the बहुलम् is व्यवस्थार्थम्, "
             "settled case by case rather than free: कृष्णसर्पः is "
             "always compounded, रामो जामदग्न्यः never, and "
             "नीलमुत्पलम् beside नीलोत्पलम् either way.",
       example="nīlotpalam, raktotpalam, kṛṣṇasarpaḥ, lohitaśāliḥ",
       counter="तक्षकः सर्पः — a name, not a qualifier; and लोहितस्तक्षकः"),
    _p("2.1.58", gives=Samasa.TATPURUSA,
       words=("pūrva", "apara", "prathama", "carama", "jaghanya",
              "samāna", "madhya", "madhyama", "vīra"),
       requires=("samānādhikaraṇa",), refuses=("saṃjñā",),
       gloss="पूर्वापरप्रथमचरमजघन्यसमानमध्यमध्यमवीराश्च — nine words "
             "with one referring to the same thing: पूर्वपुरुषः, "
             "मध्यमपुरुषः, वीरपुरुषः. पूर्वस्यैवायं प्रपञ्चः, an "
             "unfolding of 2.1.57. It is held off where a NAME is meant, "
             "because 2.1.50 is the rule for that and its own examples — "
             "पूर्वेषुकामशमी, अपरेषुकामशमी — are two of these very nine "
             "words. Which of the two governs is not settled in what has "
             "been read; 1.4.1 alone would hand it to this one, being "
             "later, and the Kāśikā cites the form under 2.1.50.",
       example="pūrvapuruṣaḥ, prathamapuruṣaḥ, madhyamapuruṣaḥ, "
               "vīrapuruṣaḥ",
       counter="पूर्वेषुकामशमी — a name, and so 2.1.50's"),
    _p("2.1.59", gives=Samasa.TATPURUSA, words=SRENYADI,
       other_words=KRTADI, requires=("samānādhikaraṇa",),
       gloss="श्रेण्यादयः कृतादिभिः — two gaṇas, and both are read from "
             "the gaṇapāṭha. अश्रेणयः श्रेणयः कृताः gives श्रेणिकृताः, "
             "made into rows having been none. The vārttika says the "
             "sense is that of च्वि — श्रेण्यादिषु च्व्यर्थवचनं "
             "कर्तव्यम्.",
       example="śreṇikṛtāḥ, ekakṛtāḥ",
       counter="either list's word with something outside the other"),
    _p("2.1.60", gives=Samasa.TATPURUSA,
       requires=("kta", "nañ-viśiṣṭa", "samānādhikaraṇa"),
       gloss="क्तेन नञ्विशिष्टेनानञ् — a क्त-form without नञ्, with the "
             "same क्त-form carrying नञ्: कृतं च तदकृतं च gives "
             "कृताकृतम्. भुक्ताभुक्तम्, पीतापीतम्, उदितानुदितम्. The "
             "vārttika adds कृतापकृतम्, गतप्रत्यागतम्, यातानुयातम्.",
       example="kṛtākṛtam, bhuktābhuktam, pītāpītam, uditānuditam",
       counter="two क्त-forms differing in anything but the नञ्"),
    _p("2.1.61", gives=Samasa.TATPURUSA,
       words=("sat", "mahat", "parama", "uttama", "utkṛṣṭa"),
       requires=("pūjyamāna", "samānādhikaraṇa"),
       gloss="सन्महत्परमोत्तमोत्कृष्टाः पूज्यमानैः — five words with "
             "what is being honoured. पूज्यमानैरिति वचनात् पूजावचनाः "
             "सदादयो विज्ञायन्ते — the condition tells you the five are "
             "meant as praise. सत्पुरुषः, महापुरुषः, परमपुरुषः.",
       example="satpuruṣaḥ, mahāpuruṣaḥ, paramapuruṣaḥ, uttamapuruṣaḥ",
       counter="उत्कृष्टा गौः कर्दमात् — a cow hauled out of mud"),

    # -- 2.1.62 to 2.1.72, closing the pāda ------------------------------
    _p("2.1.62", gives=Samasa.TATPURUSA, slot="second",
       words=("vṛndāraka", "nāga", "kuñjara"),
       requires=("pūjyamāna", "samānādhikaraṇa"),
       gloss="वृन्दारकनागकुञ्जरैः पूज्यमानम् — the mirror of 2.1.61: "
             "there the praise-word comes first, here it comes second. "
             "गोवृन्दारकः, गोनागः, गोकुञ्जरः. पूज्यमानमिति वचनाद् "
             "वृन्दारकादयः पूजावचना गृह्यन्ते — the condition is what "
             "tells you the three are meant as praise.",
       example="govṛndārakaḥ, gonāgaḥ, gokuñjaraḥ",
       counter="सुषीमो नागः — an actual elephant, honouring nobody"),
    _p("2.1.63", gives=Samasa.TATPURUSA, words=("katara", "katama"),
       requires=("jāti-paripraśna", "samānādhikaraṇa"),
       gloss="कतरकतमौ जातिपरिप्रश्ने — the two words for 'which', where "
             "the asking is between KINDS. कतरकठः, कतमकालापः. The "
             "Kāśikā notes the condition is not idle: naming it shows "
             "कतम is used elsewhere too — कतमशब्दोऽन्यत्रापि वर्तते.",
       example="katarakaṭhaḥ, katamakaṭhaḥ, katamakālāpaḥ",
       counter="कतरो भवतोर्देवदत्तः — which of you two, not which kind"),
    _p("2.1.64", gives=Samasa.TATPURUSA, words=("kim",),
       requires=("kṣepa", "samānādhikaraṇa"),
       gloss="किं क्षेपे — किम् with any word, in censure. किंराजा, यो न "
             "रक्षति — what sort of king is he, who does not protect; "
             "किंसखा, योऽभिद्रुह्यति; किंगौः, यो न वहति.",
       example="kiṃrājā, kiṃsakhā, kiṃgauḥ",
       counter="को राजा पाटलिपुत्रे — a plain question, no censure"),
    _p("2.1.65", gives=Samasa.TATPURUSA, slot="second",
       words=("poṭā", "yuvati", "stoka", "katipaya", "gṛṣṭi", "dhenu",
              "vaśā", "vehat", "baṣkayaṇī", "pravaktṛ", "śrotriya",
              "adhyāpaka", "dhūrta"),
       requires=("jāti", "samānādhikaraṇa"),
       gloss="पोटायुवति…धूर्तैर्जातिः — a kind-word with thirteen, most "
             "of them names for a cow at a stage of life: गृष्टिः "
             "एकवारप्रसूता, धेनुः प्रत्यग्रप्रसूता, वशा वन्ध्या. "
             "गोगृष्टिः, गोधेनुः, इभपोटा, कठप्रवक्ता. "
             "धूर्तग्रहणमकुत्सार्थम् — धूर्त is here WITHOUT the abuse "
             "it carries at 2.1.53.",
       example="ibhapoṭā, gogṛṣṭiḥ, godhenuḥ, kaṭhapravaktā",
       counter="देवदत्तः प्रवक्ता — a person, not a kind"),
    _p("2.1.66", gives=Samasa.TATPURUSA,
       requires=("jāti", "praśaṃsā", "samānādhikaraṇa"),
       gloss="प्रशंसावचनैश्च — जाति carries down, and now the second "
             "member is a settled word of praise: गोप्रकाण्डम्, "
             "गोमतल्लिका, गोमचर्चिका. Those words are आविष्टलिङ्ग, "
             "carrying their own gender, so they agree with a kind-word "
             "of any gender.",
       example="goprakāṇḍam, gomatallikā, aśvamatallikā",
       counter="कुमारी मतल्लिका — a girl is not a kind"),
    _p("2.1.67", gives=Samasa.TATPURUSA, words=("yuvan",),
       other_words=("khalati", "palita", "valina", "jarat"),
       requires=("samānādhikaraṇa",),
       gloss="युवा खलतिपलितवलिनजरतीभिः — young, with bald, grey, "
             "wrinkled, aged. युवखलतिः, युवपलितः, युववलिनः, युवजरन्. "
             "The list is given in the FEMININE — जरतीभिः — and the "
             "Kāśikā reads that as a ज्ञापक for प्रातिपदिकग्रहणे "
             "लिङ्गविशिष्टस्यापि ग्रहणम्, so both genders are reached.",
       example="yuvakhalatiḥ, yuvapalitaḥ, yuvavalinaḥ, yuvajaran",
       counter="either word with something outside the four"),
    _p("2.1.68", gives=Samasa.TATPURUSA, words=("tulya", "sadṛśa"),
       requires=("samānādhikaraṇa",), refuses=("jāti",),
       gloss="कृत्यतुल्याख्या अजात्या — words meaning 'like', with a word "
             "that does NOT name a kind: तुल्यश्वेतः, सदृशमहान्. "
             "अजात्येति किम्? भोज्य ओदनः — rice is a kind, and the "
             "compound is not made.",
       example="tulyaśvetaḥ, tulyamahān, sadṛśaśvetaḥ",
       counter="भोज्य ओदनः — ओदन names a kind"),
    _p("2.1.68", gives=Samasa.TATPURUSA,
       requires=("kṛtya-yat", "samānādhikaraṇa"), refuses=("jāti",),
       gloss="कृत्य… अजात्या — and a कृत्य-ending word likewise: "
             "भोज्योष्णम्, भोज्यलवणम्, पानीयशीतम् — hot as food goes, "
             "salt as food goes.",
       example="bhojyoṣṇam, bhojyalavaṇam, pānīyaśītam",
       counter="भोज्य ओदनः — the second word names a kind"),
    _p("2.1.69", gives=Samasa.TATPURUSA,
       requires=("varṇa", "samānādhikaraṇa"),
       gloss="वर्णो वर्णेन — a colour-word with a colour-word. "
             "कृष्णसारङ्गः, लोहितशबलः. The Kāśikā explains how two "
             "colours can agree at all: अवयवद्वारेण, through the parts "
             "— कृष्ण names the whole by way of a part of it.",
       example="kṛṣṇasāraṅgaḥ, lohitaśabalaḥ, kṛṣṇaśabalaḥ",
       counter="either word naming something other than a colour"),
    _p("2.1.70", gives=Samasa.TATPURUSA, words=("kumāra", "kumārī"),
       other_words=SRAMANADI, requires=("samānādhikaraṇa",),
       gloss="कुमारः श्रमणादिभिः — कुमार with the fifteen of श्रमणादि: "
             "कुमारी श्रमणा gives कुमारश्रमणा. The Kāśikā divides the "
             "list by gender — the feminine members take कुमारी, and "
             "अध्यापक and its like go either way.",
       example="kumāraśramaṇā, kumārapravrajitā, kumārādhyāpakaḥ",
       counter="कुमार with a word outside the gaṇa"),
    _p("2.1.71", gives=Samasa.TATPURUSA, slot="second",
       words=("garbhiṇī",),
       requires=("catuṣpād", "jāti", "samānādhikaraṇa"),
       gloss="चतुष्पादो गर्भिण्या — a four-footed animal with गर्भिणी: "
             "गोगर्भिणी, अजागर्भिणी. The vārttika adds that it must be "
             "a KIND — चतुष्पाज्जातिरिति वक्तव्यम् — which keeps "
             "कालाक्षी गर्भिणी and स्वस्तिमती गर्भिणी out.",
       example="gogarbhiṇī, ajāgarbhiṇī",
       counter="ब्राह्मणी गर्भिणी — two-footed; कालाक्षी गर्भिणी — not "
               "a kind"),
    _p("2.1.72", gives=Samasa.TATPURUSA, nipatana=MAYURAVYAMSAKADI,
       gloss="मयूरव्यंसकादयश्च — eighty-three forms given whole, and the "
             "pāda ends on them: समुदाया एव निपात्यन्ते. मयूरव्यंसकः, "
             "काम्बोजमुण्डः. चकारोऽवधारणार्थः — the च shuts the door, so "
             "परममयूरव्यंसक is not formed on top of one.",
       example="mayūravyaṃsakaḥ, chātravyaṃsakaḥ, kāmbojamuṇḍaḥ",
       counter="anything not among the forms the sūtra gives"),

    # === अध्याय २ पाद २ ================================================
    # 2.2.8 षष्ठी is the rule this pāda opens around. 2.2.1 to 2.2.3 and
    # 2.2.5 are its अपवादs, 2.2.9 a re-permission, 2.2.10 and 2.2.11 its
    # two prohibitions.
    _p("2.2.1", gives=Samasa.TATPURUSA,
       words=("pūrva", "apara", "adhara", "uttara"),
       requires=("ekadeśin", "ekādhikaraṇa"),
       gloss="पूर्वापराधरोत्तरमेकदेशिनैकाधिकरणे — four words for a part, "
             "with the whole they are part of, both being of one thing. "
             "पूर्वं कायस्य gives पूर्वकायः. षष्ठीसमासापवादोऽयं योगः — "
             "an exception to 2.2.8, which would else have taken it.",
       example="pūrvakāyaḥ, aparakāyaḥ, adharakāyaḥ, uttarakāyaḥ",
       counter="पूर्वं नाभेः कायस्य — the navel is no whole here; "
               "पूर्वं छात्राणाम् — several students, not one thing"),
    _p("2.2.2", gives=Samasa.TATPURUSA, words=("ardha",),
       requires=("ekadeśin", "ekādhikaraṇa"),
       gloss="अर्धं नपुंसकम् — अर्ध, and the neuter अर्ध only: the one "
             "meaning an EQUAL division, समप्रविभागे, which carries its "
             "own gender. अर्धं पिप्पल्याः gives अर्धपिप्पली. "
             "षष्ठीसमासापवादोऽयं योगः.",
       example="ardhapippalī, ardhakośātakī",
       counter="ग्रामार्धः, नगरार्धः — the masculine अर्ध, a mere part; "
               "अर्धं पिप्पलीनाम् — several peppers"),
    _p("2.2.3", gives=Samasa.TATPURUSA, vibhasa=True,
       words=("dvitīya", "tṛtīya", "caturtha", "turya", "turīya"),
       requires=("ekadeśin", "ekādhikaraṇa"),
       gloss="द्वितीयतृतीयचतुर्थतुर्याण्यन्यतरस्याम् — the fractions, "
             "OPTIONALLY: द्वितीयं भिक्षायाः gives द्वितीयभिक्षा, and "
             "the 2.2.8 compound भिक्षाद्वितीयम् stands beside it. The "
             "अन्यतरस्याम् is what lets both, and by its very presence "
             "keeps 2.2.11's prohibition off — तुरीयशब्दस्यापीष्यते.",
       example="dvitīyabhikṣā, tṛtīyabhikṣā, turyabhikṣā",
       counter="the same words where the two are not of one thing"),
    _p("2.2.4", gives=Samasa.TATPURUSA, vibhasa=True,
       words=("prāpta", "āpanna"), other_vibhakti=2,
       gloss="प्राप्तापन्ने च द्वितीयया — प्राप्त and आपन्न with a "
             "second-case word, and here they come FIRST: प्राप्तो "
             "जीविकाम् gives प्राप्तजीविकः. 2.1.24 already made "
             "जीविकाप्राप्तः, and समासविधानात् सोऽपि भवति — both stand.",
       example="prāptajīvikaḥ, āpannajīvikaḥ",
       counter="either word with something not in the second case"),
    _p("2.2.5", gives=Samasa.TATPURUSA, requires=("kāla", "parimāṇin"),
       gloss="कालाः परिमाणिना — a time-word with something that HAS that "
             "measure: मासो जातस्य gives मासजातः, a month-old child. "
             "षष्ठीसमासविषये योगारम्भः — begun within 2.2.8's ground.",
       example="māsajātaḥ, saṃvatsarajātaḥ, dvyahajātaḥ",
       counter="a time-word with something carrying no measure"),
    _p("2.2.6", gives=Samasa.TATPURUSA, words=("na",),
       gloss="नञ् — the negative with any word it is construable with: "
             "न ब्राह्मणः gives अब्राह्मणः, अवृषलः. The नञ् becomes अ "
             "before a consonant and अन् before a vowel, which is "
             "6.3.73's and 6.3.74's doing and not this sūtra's.",
       example="abrāhmaṇaḥ, avṛṣalaḥ",
       counter="anything other than नञ् in the first place"),
    _p("2.2.7", gives=Samasa.TATPURUSA, words=("īṣat",),
       requires=("akṛt", "guṇavacana"),
       gloss="ईषदकृता — ईषत्, 'slightly', with a word that does not end "
             "in a कृत् affix. The vārttika narrows it further — "
             "ईषद्गुणवचनेनेति वक्तव्यम् — to a quality-word: "
             "ईषत्कडारः, ईषत्पिङ्गलः, ईषद्रक्तम्.",
       example="īṣatkaḍāraḥ, īṣatpiṅgalaḥ, īṣadraktam",
       counter="ईषद् गार्ग्यः — a name is no quality"),
    _p("2.2.8", gives=Samasa.TATPURUSA, other_vibhakti=None, vibhakti=6,
       refuses=("nirdhāraṇa", "pratipada-vidhāna", "pūraṇa", "guṇa-artha",
                "suhita-artha", "sat-pratyaya", "avyaya", "tavya"),
       gloss="षष्ठी — a genitive with the word it is construable with, "
             "and the commonest compound in the language: राज्ञः पुरुषः "
             "gives राजपुरुषः, ब्राह्मणकम्बलः. A vārttika adds the "
             "genitive that goes with a कृत् — कृद्योगा च षष्ठी "
             "समस्यते: इध्मप्रव्रश्चनः, पलाशशातनः.",
       example="rājapuruṣaḥ, brāhmaṇakambalaḥ, idhmapravraścanaḥ",
       counter="the same words with the first in another case"),
    _p("2.2.9", gives=Samasa.TATPURUSA, slot="second", words=YAJAKADI,
       other_vibhakti=6,
       gloss="याजकादिभिश्च — the genitive with thirteen agent-words. "
             "2.2.8 gave the compound already; this is a प्रतिप्रसव, "
             "letting it back in against the prohibition 2.2.16 कर्तरि च "
             "would lay down. ब्राह्मणयाजकः, क्षत्रिययाजकः. Two "
             "vārttikas widen it: तत्स्थैश्च गुणैः — चन्दनगन्धः, "
             "कपित्थरसः — and गुणात्तरेण तरलोपश्च — सर्वश्वेतः.",
       example="brāhmaṇayājakaḥ, kṣatriyayājakaḥ",
       counter="a first member not in the genitive"),
    _p("2.2.10", gives=Samasa.TATPURUSA, vibhakti=6,
       prohibits_when=("nirdhāraṇa", "pratipada-vidhāna"),
       gloss="न निर्धारणे — the genitive that SINGLES ONE OUT of a group "
             "does not compound: क्षत्रियो मनुष्याणां शूरतमः stays a "
             "sentence. A vārttika adds the genitive prescribed by a rule "
             "naming the word itself — प्रतिपदविधाना च षष्ठी न समस्यते: "
             "सर्पिषो ज्ञानम्, मधुनो ज्ञानम्",
       example="kṣatriyo manuṣyāṇāṃ śūratamaḥ — and it stays two words",
       counter="राजपुरुषः — an ordinary genitive, and 2.2.8 takes it"),
    _p("2.2.11", gives=Samasa.TATPURUSA, vibhakti=6,
       prohibits_when=("pūraṇa", "guṇa-artha", "suhita-artha",
                       "sat-pratyaya", "avyaya", "tavya"),
       gloss="पूरणगुणसुहितार्थसदव्ययतव्यसमानाधिकरणेन — seven more the "
             "genitive will not join. अर्थशब्दः प्रत्येकमभिसंबध्यते — "
             "the word अर्थ attaches to each, so these are SENSES and "
             "not forms: छात्राणां पञ्चमः, बलाकायाः शौक्ल्यम्, फलानां "
             "तृप्तः, ब्राह्मणस्य कुर्वन्, ब्राह्मणस्य कृत्वा, "
             "ब्राह्मणस्य कर्तव्यम्",
       example="chātrāṇāṃ pañcamaḥ — and it stays two words",
       counter="ब्राह्मणकर्तव्यम् — तव्यत् with its anubandha does "
               "compound, which is why the sūtra says तव्य and not तव्यत्"),

    # -- 2.2.12 to 2.2.16, five more prohibitions of 2.2.8 ---------------
    _p("2.2.12", gives=Samasa.TATPURUSA, vibhakti=6, prohibits_when=("pūjā-kta",),
       gloss="क्तेन च पूजायाम् — the genitive does not join a क्त that was "
             "prescribed for honouring. राज्ञां मतः, राज्ञां पूजितः stay "
             "two words. पूजाग्रहणमुपलक्षणार्थम् — the word stands for "
             "the whole of 3.2.188's मति, बुद्धि and पूजा",
       example="rājñāṃ mataḥ — and it stays two words",
       counter="छात्रस्य हसितम् gives छात्रहसितम् — no honouring there"),
    _p("2.2.13", gives=Samasa.TATPURUSA, vibhakti=6,
       prohibits_when=("adhikaraṇa-kta",),
       gloss="अधिकरणवाचिना च — nor a क्त that names the PLACE of the act, "
             "which 3.4.76 provides for. इदमेषामासितम्, इदमेषां भुक्तम्",
       example="idam eṣām āsitam — and it stays two words",
       counter="an ordinary क्त, which 2.2.8 takes"),
    _p("2.2.14", gives=Samasa.TATPURUSA, vibhakti=6,
       prohibits_when=("karman-ṣaṣṭhī",),
       gloss="कर्मणि च — nor a genitive standing in the OBJECT sense, the "
             "one 2.3.66 उभयप्राप्तौ कर्मणि lets in beside the "
             "accusative. आश्चर्यो गवां दोहः, विचित्रा सूत्रस्य कृतिः "
             "पाणिनिना",
       example="gavāṃ dohaḥ — and it stays two words",
       counter="an ordinary possessive genitive"),
    _p("2.2.15", gives=Samasa.TATPURUSA, vibhakti=6,
       prohibits_when=("kartṛ-ṣaṣṭhī",),
       gloss="तृजकाभ्यां कर्तरि — nor an AGENT genitive with a तृच् or अक "
             "word: भवतः शायिका, भवत आसिका. The Kāśikā notes तृच् is "
             "prescribed for an agent and nothing else, so no agent "
             "genitive can stand beside it — तस्मात् तृज्ग्रहणम् "
             "उत्तरार्थम्, the mention is for the next sūtra's sake",
       example="bhavataḥ śāyikā — and it stays two words",
       counter="इक्षुभक्षिकां मे धारयसि — the genitive is not the agent"),
    _p("2.2.16", gives=Samasa.TATPURUSA, vibhakti=6,
       prohibits_when=("tṛc-aka",),
       gloss="कर्तरि च — and again with तृच् and अक used of an agent: "
             "अपां स्रष्टा, पुरां भेत्ता, ओदनस्य भोजकः. This is the "
             "prohibition 2.2.9 lets thirteen words back through. The "
             "Kāśikā heads off an objection — भर्तृ is in that gaṇa — by "
             "saying the गण's भर्तृ is the relational word meaning "
             "husband, not this one",
       example="apāṃ sraṣṭā — and it stays two words",
       counter="ब्राह्मणयाजकः — 2.2.9 re-permits the याजकादि"),

    # -- 2.2.17 to 2.2.22, obligatory, then the upapada rules ------------
    _p("2.2.17", gives=Samasa.TATPURUSA, nitya=True, vibhakti=6,
       requires=("krīḍā-jīvikā",),
       gloss="नित्यं क्रीडाजीविकयोः — and where a GAME or a LIVELIHOOD is "
             "meant the genitive does compound, and must: "
             "उद्दालकपुष्पभञ्जिका, a game of breaking uddālaka flowers; "
             "दन्तलेखकः, one who lives by carving teeth. नहि वाक्येन "
             "क्रीडा जीविका वा गम्यते. तृच् does not occur in these two "
             "senses, so only अक forms are shown",
       example="uddālakapuṣpabhañjikā, dantalekhakaḥ",
       counter="ओदनस्य भोजकः — an eater of rice, neither game nor trade"),
    _p("2.2.18", gives=Samasa.TATPURUSA, nitya=True,
       requires=("ku-gati-pra",),
       gloss="कुगतिप्रादयः — कु, the गति words and the प्रादि compound "
             "with whatever they are construable with, obligatorily. "
             "कुपुरुषः, उररीकृतम्, दुष्पुरुषः, सुपुरुषः, अतिपुरुषः, "
             "आपिङ्गलः. The senses the Kāśikā gives — कु for बad, दुर् "
             "for blame, सु for praise — are प्रायिक, usual rather than "
             "required: कोष्णम् and दुष्कृतम् stand outside them",
       example="kupuruṣaḥ, duṣpuruṣaḥ, supuruṣaḥ, atipuruṣaḥ",
       counter="कु as a noun rather than the indeclinable"),
    _p("2.2.19", gives=Samasa.TATPURUSA, nitya=True,
       requires=("upapada-atiṅ",),
       gloss="उपपदमतिङ् — an उपपद that is not a finite verb compounds "
             "obligatorily: कुम्भकारः, नगरकारः. The Kāśikā draws a "
             "paribhāṣā out of the very oddity of the wording — since "
             "सुप् सुपा is overhead, a finite verb could never have been "
             "in question, so its exclusion shows सुप् सुपा does NOT "
             "reach these two sūtras, and the upapada compounds are made "
             "प्राक् सुबुत्पत्तेः, before any ending is added",
       example="kumbhakāraḥ, nagarakāraḥ, aśvakrītī",
       counter="एधानाहारको व्रजति — the उपपद goes with a finite verb"),
    _p("2.2.20", gives=Samasa.TATPURUSA, nitya=True,
       requires=("upapada-atiṅ", "am-anta", "avyaya"),
       gloss="अमैवाव्ययेन — a नियम, not a fresh permission: 2.2.19 gave "
             "the compound already, and this says that with an "
             "indeclinable it happens ONLY where the उपपद ends in अम्. "
             "स्वादुंकारं भुङ्क्ते, संपन्नंकारं भुङ्क्ते. The एव is "
             "there to qualify the उपपद, not the अव्यय",
       example="svāduṃkāraṃ bhuṅkte, saṃpannaṃkāraṃ bhuṅkte",
       counter="कालो भोक्तुम् — an infinitive by 3.3.167, not an अम् form"),
    _p("2.2.21", gives=Samasa.TATPURUSA, vibhasa=True,
       requires=("upapada-atiṅ", "am-anta", "avyaya",
                 "upapada-tṛtīyā-prabhṛti"),
       gloss="तृतीयाप्रभृतीन्यन्यतरस्याम् — the उपपदs from 3.4.47 "
             "उपदंशस्तृतीयायाम् onward compound with an indeclinable "
             "optionally. मूलकोपदंशं भुङ्क्ते beside मूलकेनोपदंशं "
             "भुङ्क्ते; उच्चैःकारमाचष्टे beside उच्चैः कारम्. "
             "उभयत्रविभाषेयम् — the option cuts both ways, licensing "
             "where 2.2.20 would have compelled and where it would have "
             "refused",
       example="mūlakopadaṃśaṃ bhuṅkte, uccaiḥkāram ācaṣṭe",
       counter="an उपपद before 3.4.47"),
    _p("2.2.22", gives=Samasa.TATPURUSA, vibhasa=True,
       requires=("ktvā", "upapada-tṛtīyā-prabhṛti"),
       gloss="क्त्वा च — and with a क्त्वा form, optionally. उच्चैःकृत्य "
             "beside उच्चैः कृत्वा. अमैव was running over the last two "
             "and would have kept this out, so the sūtra is begun. Where "
             "the compound IS made the affix appears as ल्यप् — "
             "समासपक्षे ल्यबेव — which is 7.1.37's doing",
       example="uccaiḥkṛtya, nīcaiḥkṛtya",
       counter="अलं कृत्वा, खलु कृत्वा — उपपदs before 3.4.47"),

    # -- 2.2.23 to 2.2.29. The heading is शेष — whatever no other rule
    #    has named — so these five say what falls to it, and 2.2.29
    #    turns to the last name of all.
    _p("2.2.24", gives=Samasa.BAHUVRIHI, requires=("anya-padārtha-bv",),
       gloss="अनेकमन्यपदार्थे — two or more words, standing for a THIRD "
             "thing that is neither of them. प्राप्तमुदकं यं ग्रामम् "
             "gives प्राप्तोदको ग्रामः; चित्रगुर्देवदत्तः is a man with "
             "dappled cows. अनेकग्रहणं किम्? so that more than two may "
             "join. Every case-sense but the nominative is reached — "
             "प्रथमार्थम् एकं वर्जयित्वा — and वृष्टे देवे गतः shows "
             "why the one is left out.",
       example="prāptodako grāmaḥ, ūḍharatho'naḍvān, citragurdevadattaḥ",
       counter="वृष्टे देवे गतः — the nominative sense, which this "
               "compound does not take"),
    _p("2.2.25", gives=Samasa.BAHUVRIHI, requires=("saṃkhyeya",),
       words=("upa", "āsanna", "adūra", "adhika"), samkhya=False,
       gloss="संख्ययाव्ययासन्नादूराधिकसंख्याः संख्येये — with a numeral "
             "that counts the things themselves: an indeclinable, or "
             "आसन्न, अदूर, अधिक, or another numeral. उपदशाः, about ten; "
             "आसन्नदशाः; अधिकविंशाः; and numeral with numeral, "
             "द्वित्राः, two or three.",
       example="upadaśāḥ, āsannadaśāḥ, adhikaviṃśāḥ",
       counter="पञ्च ब्राह्मणाः — no such word beside the numeral; "
               "अधिका विंशतिर्गवाम् — the numeral is not counting"),
    _p("2.2.25", gives=Samasa.BAHUVRIHI, requires=("saṃkhyeya",),
       samkhya=True, other_samkhya=True,
       gloss="संख्यया … संख्याः — and a numeral with a numeral, for the "
             "same reason: द्वित्राः, त्रिचतुराः, द्विदशाः.",
       example="dvitrāḥ, tricaturāḥ, dvidaśāḥ",
       counter="a numeral where nothing is being counted"),
    _p("2.2.26", gives=Samasa.BAHUVRIHI, requires=("antarāla",),
       gloss="दिङ्नामान्यन्तराले — the NAMES of directions, for the space "
             "between two of them: दक्षिणपूर्वा दिक्, the south-east. "
             "नामग्रहणं रूढ्यर्थम् — the sūtra says names so that a "
             "direction described some other way is left out, and "
             "ऐन्द्र्याश्च कौबेर्याश्च दिशोः is not reached.",
       example="dakṣiṇapūrvā, pūrvottarā, uttarapaścimā",
       counter="ऐन्द्री and कौबेरी — directions by their gods, not by "
               "their names"),
    _p("2.2.27", gives=Samasa.BAHUVRIHI, requires=("sarūpa-yuddha",),
       gloss="तत्र तेनेदमिति सरूपे — the same word twice, once in the "
             "seventh case and once in the third, for a fight. The "
             "इतिकरण is what carries the sense: what is named by तत्र "
             "is the grasping, what by तेन the striking, and what by "
             "इदम् the fight itself — सर्वम् इतिकरणाल् लभ्यते.",
       example="daṇḍādaṇḍi, keśākeśi",
       counter="the same pair where no exchange of blows is meant"),
    _p("2.2.28", gives=Samasa.BAHUVRIHI, words=("saha",),
       other_vibhakti=3, requires=("tulya-yoga",),
       gloss="तेन सहेति तुल्ययोगे — सह with a third-case word, where the "
             "two act TOGETHER: सह पुत्रेणागतः gives सपुत्रः. "
             "तुल्ययोग इति किम्? सहैव दशभिः पुत्रैर् भारं वहति गर्दभी — "
             "the sons are merely present. The Kāśikā then admits the "
             "condition is प्रायिक: सलोमकः and सपक्षकः are mere "
             "possession and compound anyway.",
       example="saputraḥ, sacchātraḥ, sakarmakaraḥ",
       counter="सहैव दशभिः पुत्रैः — present, not acting with her"),
    _p("2.2.29", gives=Samasa.DVANDVA, requires=("ca-artha",),
       gloss="चार्थे द्वन्द्वः — two or more words in the sense of 'and'. "
             "The Kāśikā names four such senses and admits two: "
             "इतरेतरयोग, where they stand severally — प्लक्षन्यग्रोधौ, "
             "धवखदिरपलाशाः — and समाहार, where they are taken as one "
             "and the compound turns neuter and singular: वाक्त्वचम्. "
             "समुच्चय and अन्वाचय make no compound, असामर्थ्यात्.",
       example="plakṣanyagrodhau, dhavakhadirapalāśāḥ, vāktvacam",
       counter="words merely listed one after another, with no 'and'"),

    _p("2.1.29", gives=Samasa.TATPURUSA, vibhakti=2,
       requires=("kāla", "atyanta-saṃyoga"),
       gloss="अत्यन्तसंयोगे च — and a time-word in the second case "
             "compounds with any सुप् when the time is wholly filled. "
             "कालाः इति वर्तते, क्तेनेति निवृत्तम्: the time-words carry "
             "down and the क्त does not, which is the whole difference "
             "from 2.1.28 — so मुहूर्तं सुखम् gives मुहूर्तसुखम् though "
             "सुख is no participle. Where both rules reach a pair 1.4.1 "
             "settles it and this one stands, being later.",
       example="muhūrtasukham, sarvarātrakalyāṇī, sarvarātraśobhanā",
       counter="a happiness that merely occurred during the hour"),
)


def dvigu(
    first: str,
    second: str,
    given: Optional[Sequence[str]] = None,
    connected: bool = True,
) -> Optional[Samjna]:
    """
    2.1.52 संख्यापूर्वो द्विगुः — the compound of 2.1.51 whose first
    member is a numeral bears the further name द्विगु.

    It forms nothing. 2.1.51 makes the compound and this names it, in the
    three settings that sūtra allows: पञ्चकपालः before a taddhita,
    पञ्चनावप्रियः before a further member, पञ्चपूली for an aggregate.

    The name is wanted for what other rules do with it — 4.1.21 द्विगोः
    gives पञ्चपूली its ङीप्, 4.1.88 द्विगोर्लुगनपत्ये drops the affix of
    पञ्चकपालः, 5.4.99 नावो द्विगोः supplies the ending of
    पञ्चनावप्रियः. None of those is codified, so what is held here is the
    name and the reason for it.

    And this is what 2.1.23 द्विगुश्च extends तत्पुरुष to: until now that
    sūtra had nothing bearing the name to reach.
    """
    if isinstance(given, str):
        given = [g.strip() for g in given.split(",") if g.strip()]
    pair = Pair(first, second, connected=connected,
                given=tuple(given or ()))
    verdict = resolve(pair)
    if not verdict.compounds or verdict.by != "2.1.51":
        return None
    if not is_samkhya(first):
        return None
    return Samjna(
        Samasa.DVIGU, "2.1.52", "2.1.52",
        pradhana="uttarapada",
        why="संख्यापूर्वो द्विगुः — the 2.1.51 compound with a numeral "
            "first. तद्धितार्थे पञ्चकपालः, उत्तरपदे पञ्चनावप्रियः, "
            "समाहारे पञ्चपूली.",
    )


def provisions_for(sutra_id: str) -> Tuple[Provision, ...]:
    return tuple(p for p in PROVISIONS if p.sutra == sutra_id)


# ---------------------------------------------------------------------------
# Resolving
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Verdict:
    """Whether these two compound, under which names, by which rule."""

    compounds: bool
    names: FrozenSet[Samasa]
    by: str
    why: str
    optional: bool = False
    pradhana: str = ""
    instead_of: Tuple[str, ...] = ()


def resolve(pair: Pair) -> Verdict:
    """
    Whether this pair compounds — 2.1.6 to 2.1.29.

    2.1.1 comes first and is not part of the table: समर्थः पदविधिः is a
    paribhāṣā over every rule about words in the grammar, so it gates the
    section rather than sitting inside it. With connectedness unstated the
    answer is withheld, because two words adjacent by accident are exactly
    what the paribhāṣā exists to exclude.

    Then the table, and then 1.4.1 — but 1.4.1 as 2.1.3 leaves it. The names
    do not compete: समास is conferred by the range and अव्ययीभाव by the range
    within it, and प्राग्वचनं संज्ञासमावेशार्थम् is the text saying so. What
    1.4.1 still settles is a contest between two *provisions*, and there the
    later stands as everywhere else.
    """
    reach = samartha(connected=pair.connected, padavidhi=True)
    if not reach.applies:
        return Verdict(False, frozenset(), "2.1.1", reach.why)

    for rule in PROVISIONS:
        if not rule.niyama_on:
            continue
        if pair.word(rule.slot) in rule.niyama_on and (
                set(rule.not_senses) & set(pair.first_sense)):
            return Verdict(
                False, frozenset(), rule.sutra,
                rule.gloss + " — so this pair compounds by nothing. The "
                "restatement would be idle if it only granted what 2.1.6 "
                "grants already; what it does is take the excluded sense "
                "away, and यथा देवदत्तस्तथा यज्ञदत्तः stays a sentence.",
            )

    # A prohibition is asked before anything is formed. न निर्धारणे does
    # not compete with 2.2.8 for the pair; it takes the pair away from it.
    for rule in PROVISIONS:
        if not rule.prohibits_when:
            continue
        # A prohibition forbids some OTHER rule, and reaches only what
        # that rule would have taken. 2.2.10 to 2.2.16 all forbid 2.2.8
        # षष्ठी, so a pair with no genitive in it was never theirs to
        # refuse — and 2.2.11's अव्यय would otherwise have blocked
        # स्वादुंकारम्, an upapada compound with no genitive anywhere.
        if rule.vibhakti is not None and                 pair.vibhakti(rule.slot) != rule.vibhakti:
            continue
        hit = [f for f in rule.prohibits_when if pair.has(f)]
        if hit:
            return Verdict(
                False, frozenset(), rule.sutra,
                rule.gloss + f" — {', '.join(hit)} is stated, so the "
                f"genitive does not compound here.",
            )

    matched = [p for p in PROVISIONS
               if not p.prohibits_when and p.applies(pair)]
    if not matched:
        return Verdict(
            False, frozenset(), "2.1.3",
            "प्राक् कडारात् समासः — no rule of the section reaches this "
            "pair. A heading confers a name on what the rules below it "
            "join; it joins nothing itself, and that is as true of "
            "2.1.22 तत्पुरुषः as of 2.1.5 अव्ययीभावः.",
        )

    settled = eka_samjna([Rule(p.sutra, what=p.gives.value) for p in matched])
    chosen = max(matched, key=lambda p: order_of(p.sutra))
    displaced = tuple(s for s in settled.against if s != chosen.sutra)

    why = chosen.gloss
    if displaced:
        why += (f" — and 1.4.1 leaves this one of {len(matched)}: एका "
                f"संज्ञा, the later standing.")

    # Both sources: what the heading in force confers by its range, and
    # what this very rule confers by being itself. They coincide for every
    # rule of the first pāda, and come apart at 2.2.29.
    conferred = names_of(chosen.sutra) | {chosen.gives}
    return Verdict(
        True, conferred, chosen.sutra, why,
        optional=chosen.optional,
        pradhana=next((s.pradhana for s in samjna_over(chosen.sutra)
                       if s.pradhana != "—"), ""),
        instead_of=displaced,
    )


def near_misses(pair: Pair) -> Tuple[Tuple[str, Tuple[str, ...]], ...]:
    """Every rule that did not reach this pair, and what it wanted."""
    out = []
    for p in PROVISIONS:
        missing = p.unmet(pair)
        if missing:
            out.append((p.sutra, missing))
    return tuple(out)


# ---------------------------------------------------------------------------
# String entry points
# ---------------------------------------------------------------------------


def samasa_of(
    first: str,
    second: str,
    sense: Optional[str] = None,
    second_vibhakti: Optional[int] = None,
    first_vibhakti: Optional[int] = None,
    first_vacana: int = 1,
    second_vacana: int = 1,
    given: Optional[Sequence[str]] = None,
    connected: bool = True,
) -> Verdict:
    """
    :func:`resolve` from plain values, for the playground.

    `sense` is what the *named* member means here — one of 2.1.6's sixteen,
    or avadhāraṇa, mātrā, maryādā, abhividhi, ābhimukhya, āyāma.
    `given` asserts facts from :data:`FACTS`, comma-separated or a list.

    Both vibhaktis are asked for. The avyayībhāva rules only ever constrain
    the second member, so for a while only that one was here; 2.1.24
    द्वितीया श्रितादिभिः puts the case on the first, and without this
    parameter the whole तत्पुरुष run was codified but unreachable from the
    playground.
    """
    if isinstance(given, str):
        given = [g.strip() for g in given.split(",") if g.strip()]
    return resolve(Pair(
        first_vibhakti=first_vibhakti,
        first=first,
        second=second,
        first_sense=(sense,) if sense else (),
        second_vibhakti=second_vibhakti,
        first_vacana=first_vacana,
        second_vacana=second_vacana,
        given=tuple(given or ()),
        connected=connected,
    ))


__all__ = [
    "Samasa", "Samjna", "SAMJNAS", "samjna_over", "names_of",
    "Together", "saha_supa",
    "FACTS", "Pair", "tisthadgu", "VIBHAKTYADI",
    "Provision", "PROVISIONS", "provisions_for",
    "Verdict", "resolve", "near_misses", "samasa_of",
]
