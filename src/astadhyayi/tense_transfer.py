# -*- coding: utf-8 -*-
"""
३.३.१३१–१३२ and ३.३.१३५–१३८ — one tense's affixes used for another.

These six rules name no affix. They say that the affixes given for one
time are used for a different time — वर्तमानवत्, भूतवत्, अनद्यतनवत् —
and four of the six are प्रतिषेध of exactly that.

So the question is not "which ending comes" but "may the endings of
this time stand for that one", which is why they answer from here and
not from the लकार table. The वत् is the whole of it: 3.3.131's vṛtti
says वत्करणं सर्वसादृश्यार्थम् — the transfer carries EVERYTHING, so
whatever conditions an affix had in its own time it keeps in the
borrowed one. पवमानः and यजमानः come out of a rule about the present
being read for the past.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

from src.astadhyayi.upapada_krt import Added, NotAdded

#: The extent 3.3.131 transfers. वर्तमाने लट् इत्यारभ्य यावद् उणादयो
#: बहुलम् इति वर्तमाने प्रत्यया उक्तः — everything given for the
#: present from 3.2.123 to 3.3.1, which is the run this project has
#: just finished reading. Named at both ends by the vṛtti, so the
#: extent is the text's and not ours.
VARTAMANA_FROM = "3.2.123"
VARTAMANA_THROUGH = "3.3.1"


@dataclass(frozen=True)
class Transfer:
    """One rule moving a tense's affixes to another time."""

    sutra: str
    #: Which time's affixes are borrowed — वर्तमानवत्, भूतवत्,
    #: अनद्यतनवत्.
    like: str
    #: The time they are used FOR.
    for_time: str = ""
    #: The sense that licenses it, where a rule names one.
    sense: str = ""
    #: 3.3.135 to 3.3.138 REFUSE the transfer rather than allowing it.
    refuses: bool = False
    #: विभाषा — 3.3.131 and 3.3.132 offer, 3.3.138 refuses optionally.
    optional: bool = False
    why: str = ""


TRANSFER: Tuple[Transfer, ...] = (
    Transfer(
        "3.3.131", like="vartamāna", for_time="samīpa", optional=True,
        why="वर्तमानसामीप्ये वर्तमानवद् वा — कदा देवदत्तागतोऽसि? "
            "अयमागच्छामि, एषोऽस्म्यागतः; कदा गमिष्यसि? एष गच्छामि, "
            "एष गमिष्यामि. समीपमेव सामीप्यम्: what is NEAR the "
            "present, past or future, may take the present's "
            "affixes.\n\n"
            "THE TRANSFER CARRIES EVERYTHING. वत्करणं "
            "सर्वसादृश्यार्थम्, येन विशेषणेन वर्तमाने प्रत्यया "
            "विहिताः प्रकृत्युपपदादिना तथैवात्र भवन्ति — whatever "
            "conditions an affix had in its own time it keeps in the "
            "borrowed one, root and companion alike. So पवमानः, "
            "यजमानः and अलंकरिष्णुः all come out of it, and the "
            "extent transferred is stated at both ends: वर्तमाने लट् "
            "इत्यारभ्य यावद् उणादयो बहुलम् इति.\n\n"
            "सामीप्यग्रहणं किम्? विप्रकर्षविवक्षायां मा भूत् — "
            "परुदगच्छत् पाटलिपुत्रम्, वर्षेण गमिष्यति.\n\n"
            "AND THE VṚTTI CONCEDES THE WHOLE SECTION MAY BE "
            "UNNECESSARY. यो मन्यते गच्छामीति पदं वर्तमाने काल एव "
            "वर्तते, कालान्तरगतिस्तु वाक्याद् भवति — for one who "
            "holds that the WORD is present-tense and the other time "
            "comes from the sentence, न च वाक्यगम्यः कालः "
            "पदसंस्कारवेलायामुपयुज्यत इति, तादृशं "
            "वाक्यार्थप्रतिपत्तारं प्रति प्रकरणमिदं नारभ्यते: for "
            "such a reader this whole section is not undertaken. A "
            "commentary saying that a stretch of the grammar answers "
            "a question one need not ask"),
    Transfer(
        "3.3.132", like="bhūta", for_time="bhaviṣyat",
        sense="āśaṃsā", optional=True,
        why="आशंसायां भूतवच्च — उपाध्यायश्चेदागमत्, आगतः, आगच्छति, "
            "आगमिष्यति; एते व्याकरणमध्यगीष्महि, अधीमहे, अध्येष्यामहे. "
            "चकाराद् वर्तमानवच्च, so both transfers stand.\n\n"
            "आशंसनमाशंसा, अप्राप्तस्य प्रियार्थस्य प्राप्तुमिच्छा, "
            "तस्याश्च भविष्यत्कालो विषयः — the wish for a good thing "
            "not yet had, whose field is the future. The PAST's "
            "affixes used for it.\n\n"
            "AND A GENERAL TRANSFER DOES NOT CARRY THE SPECIAL CASES. "
            "सामान्यातिदेशे विशेषानतिदेशात् लङ्लिटौ न भवतः — लङ् and "
            "लिट् do not come, being given for particular kinds of "
            "past. A limit on सर्वसादृश्य that 3.3.131 did not state "
            "and this rule needs"),
    Transfer(
        "3.3.135", like="anadyatana", refuses=True,
        sense="kriyāprabandha",
        why="नानद्यतनवत् क्रियाप्रबन्धसामीप्ययोः — यावज्जीवं "
            "भृशमन्नमदात्, भृशमन्नं दास्यति. "
            "क्रियाणां प्रबन्धः सातत्येनानुष्ठानम्, an unbroken doing; "
            "कालानां सामीप्यं तुल्यजातीयेनाव्यवधानम्, times of one "
            "kind with nothing between.\n\n"
            "भूतानद्यतने भविष्यदनद्यतने च लङ्लुटौ विहितौ, तयोरयं "
            "प्रतिषेधः — what is refused is 3.2.111's लङ् and "
            "3.3.15's लुट्, one from each pāda. And द्वौ प्रतिषेधौ "
            "यथाप्राप्तस्याभ्यनुज्ञापनाय: TWO prohibitions, so that "
            "what would ordinarily come is thereby allowed. A "
            "refusal read as a licence for everything it does not "
            "refuse"),
    Transfer(
        "3.3.136", like="anadyatana", refuses=True,
        for_time="bhaviṣyat", sense="deśa-maryādā",
        why="भविष्यति मर्यादावचनेऽवरस्मिन् — योऽयमध्वा गन्तव्य आ "
            "पाटलिपुत्रात्, तस्य यदवरं कौशाम्ब्याः, तत्र द्विरोदनं "
            "भोक्ष्यामहे. अक्रियाप्रबन्धार्थम् असामीप्यार्थं च "
            "वचनम्, so the rule exists for ground 3.3.135 left.\n\n"
            "THREE CONDITIONS, THREE COUNTER-EXAMPLES, and each is a "
            "whole scene rebuilt: भविष्यतीति किम्? — the same journey "
            "in the past. मर्यादावचन इति किम्? — the same journey "
            "with no limit named. अवरस्मिन्निति किम्? — the same "
            "journey, the FARTHER side. The commentary tests a "
            "condition by changing one word of a sentence and "
            "printing the rest again.\n\n"
            "इह सूत्रे देशकृता मर्यादा, उत्तरत्र कालकृता — the limit "
            "here is of PLACE and at 3.3.137 of TIME, and तत्र न "
            "विशेषं वक्ष्यति, the difference is not stated in either "
            "rule. Read off the examples alone"),
    Transfer(
        "3.3.137", like="anadyatana", refuses=True,
        for_time="bhaviṣyat", sense="kāla-maryādā",
        why="कालविभागे चानहोरात्राणाम् — योऽयं संवत्सर आगामी, तत्र "
            "यदवरमाग्रहायण्याः, तत्र युक्ता अध्येष्यामहे.\n\n"
            "पूर्वेणैव सिद्धे वचनमिदमहोरात्रनिषेधार्थम् — 3.3.136 "
            "settles it already and this exists to EXCEPT days and "
            "nights: अनहोरात्राणामिति किम्? and the vṛtti gives "
            "त्रिविधमुदाहरणम्, three ways a period can touch a day, "
            "closing सर्वथाहोरात्रस्पर्शे प्रतिषेधः. A rule stated "
            "for what it takes away.\n\n"
            "योगविभाग उत्तरार्थः — and split off for the rule after, "
            "as 3.3.115 and 3.3.148 were"),
    Transfer(
        "3.3.138", like="anadyatana", refuses=True, optional=True,
        for_time="bhaviṣyat", sense="kāla-maryādā-para",
        why="परस्मिन् विभाषा — योऽयं संवत्सर आगामी, तस्य यत् "
            "परमाग्रहायण्याः, तत्र युक्ता अध्येष्यामहे, अध्येतास्महे: "
            "both stand.\n\n"
            "AND THE RULE INHERITS EVERYTHING BUT ONE WORD. "
            "अवरस्मिन्वर्जं पूर्वमनुवर्तते — all of 3.3.137 carries "
            "down EXCEPT अवरस्मिन्, which this rule replaces with its "
            "own परस्मिन्. अवरस्मिन् पूर्वेण प्रतिषेध उक्तः, संप्रति "
            "परस्मिन्नप्राप्त एव विकल्प उच्यते: the nearer side was "
            "already refused, so on the farther side an option is "
            "offered where nothing had applied. An अनुवृत्ति with a "
            "single word cut out of it, which the codification cannot "
            "represent and states per row"),
)


def tense_transfer(*, like: str = "", sense: str = "",
                   for_time: str = "") -> object:
    """
    3.3.131, 3.3.132 and 3.3.135 to 3.3.138 — whether one tense's
    affixes may stand for another time.

    These name no affix, so the answer is a permission or a refusal
    and not a form. `like` names the tense borrowed from —
    वर्तमान, भूत or अनद्यतन.

    Four of the six REFUSE, and a refusal here names itself: refusing
    is the whole of what those rules do, which is the case 3.2.23
    marked off as the one where a प्रतिषेध may be reported.
    """
    matched = [row for row in TRANSFER
               if (not like or row.like == like)
               and (not row.sense or row.sense == sense)
               and (not row.for_time or not for_time
                    or row.for_time == for_time)]
    if not matched:
        return NotAdded(
            "",
            "No rule of 3.3.131 to 3.3.138 speaks to that. They move "
            "the present's affixes to what is near it, the past's to "
            "a hoped-for future, and refuse the not-today affixes in "
            "four situations")
    best = max(matched, key=_how_specific)
    if best.refuses:
        return NotAdded(best.sutra, best.why, best.like)
    return Added(best.like + "vat", best.sutra, best.why)


def _how_specific(row: Transfer) -> int:
    """How much a row states."""
    return 3 * bool(row.sense) + 2 * bool(row.for_time) + bool(row.like)


def transferred_extent() -> Tuple[str, str]:
    """
    What 3.3.131 moves, as the vṛtti names it: from वर्तमाने लट् to
    उणादयो बहुलम्.

    Both ends are NAMED rules and not numbers, which is the third
    extent of this kind — 3.2.134's आ क्वेः and 3.3.56's यावत्
    कृत्यल्युटो बहुलम् were the others, and 3.3.141's is a fourth.
    """
    return VARTAMANA_FROM, VARTAMANA_THROUGH
