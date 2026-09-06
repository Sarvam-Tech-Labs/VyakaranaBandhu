# -*- coding: utf-8 -*-
"""
८.३.३४–५४ — what the visarga becomes, and where it stays.

Twenty-one sūtras on one sound. 8.3.15 had turned every final
र् into a visarga; this run says what happens to it next.
Before a खर् it becomes स् — **वृक्षश्छादयति, वृक्षस्तरति** —
unless a शर् follows that खर्, when it stays (8.3.35 शशः
क्षुरम्); before a शर् it may do either (8.3.36 वृक्षः शेते
beside वृक्षश्शेते); and before a guttural or a labial it
becomes the जिह्वामूलीय or the उपध्मानीय, or again stays
(8.3.37).

**AND THEN SEVENTEEN SŪTRAS ON WHEN IT IS स् OR ष् ANYWAY.**
Not at the head of a word (8.3.38 पयस्पाशम्), after an इण्
(8.3.39 सर्पिष्पाशम्), of नमस् and पुरस् as preverbs (8.3.40
नमस्कर्ता), of a stem with इ or उ in its penult (8.3.41
निष्कृतम्, दुष्कृतम्), of तिरस् optionally (8.3.42), of द्विस्
and त्रिस् and चतुर् where a NUMBER OF TIMES is meant (8.3.43
द्विष्करोति) — and always inside a compound (8.3.45
सर्पिष्कुण्डिका, धनुष्कपालम्).

**AND SIX OF THEM ARE VEDIC AND ONE OF THOSE IS ABOUT A CASE.**
8.3.51 पञ्चम्याः परावध्यर्थे turns an ABLATIVE's visarga into
स् before परि meaning अधि — **दिवस् परि प्रथमं जज्ञे** — and
8.3.53 does the same for a GENITIVE before seven named words:
**वाचस्पतिम्, दिवस्पुत्राय**. Nowhere else in the pāda does the
case of the word decide the sound.

**WHAT THIS MODULE DOES NOT DO.** 8.3.15, which makes the
visarga in the first place, is codified apart in `anga`. And
8.3.55 अपदान्तस्य मूर्धन्यः, which opens the last heading of
the pāda, belongs to the next module.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

from src.astadhyayi.ru_anunasika import Joined  # noqa: E402

#: This module's stretch.
VISARGA_RUN: Tuple[str, str] = ("8.3.34", "8.3.54")

#: The rule that makes the visarga this run is about, codified
#: apart in `anga` long before the pāda was read.
THE_VISARGA: str = "8.3.15"

#: 8.3.38's four, the affixes before which a word's-head क or
#: प is nevertheless not a word's head.
PASA_FOUR: Tuple[str, ...] = ("pāśa", "kalpa", "ka", "kāmya")

#: 8.3.41's eight, whose visarga becomes ष् before a guttural
#: or a labial: निर्, दुर्, बहिर्, आविस्, चतुर्, प्रादुस् and
#: the two the sūtra's own shape names.
NIRADI: Tuple[str, ...] = (
    "nis", "dus", "bahis", "āvis", "catur", "prādus")

#: 8.3.43's three, which take ष् only where a number of TIMES
#: is meant.
DVIS_THREE: Tuple[str, ...] = ("dvis", "tris", "catur")

#: 8.3.46's seven, before which an अ-final word takes स्.
KRKAMI_SEVEN: Tuple[str, ...] = (
    "kṛ", "kami", "kaṃsa", "kumbha", "pātra", "kuśā", "karṇī")

#: 8.3.53's seven, before which a genitive's visarga does.
PATI_SEVEN: Tuple[str, ...] = (
    "pati", "putra", "pṛṣṭha", "pāra", "pada", "payas", "poṣa")


@dataclass(frozen=True)
class Visarga:
    """One rule of 8.3.34–54: what the visarga becomes."""

    sutra: str
    #: `sa`, `ṣa`, `visarjanīya`, `ka-pa`.
    does: str = ""
    #: The words named outright.
    of: Tuple[str, ...] = ()
    #: The shape of the word instead.
    gana: str = ""
    #: What must follow.
    before: Tuple[str, ...] = ()
    sense: Tuple[str, ...] = ()
    #: The case the word must stand in, for the two sūtras that
    #: turn on one.
    case: str = ""
    optional: bool = False
    chandasi: bool = False
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


VISARGA_TABLE: Tuple[Visarga, ...] = (
    Visarga(
        "8.3.34", does="sa", gana="visarjanīya", before=("khar",),
        why="विसर्जनीयस्य सः — the visarga becomes स् before a "
            "खर्: **वृक्षश्छादयति, प्लक्षश्छादयति; वृक्षष्ठकारः; "
            "वृक्षस्थकारः; वृक्षश्चिनोति; वृक्षस्तरति**. The "
            "sound heard is then further shaped by 8.4's rules — "
            "श् before a palatal, ष् before a cerebral — so what "
            "this rule gives is a स् that is almost never heard "
            "as one"),
    Visarga(
        "8.3.35", does="visarjanīya", gana="visarjanīya",
        before=("khar-śar-para",), blocks=("8.3.34",),
        why="शर्परे विसर्जनीयः — but where the खर् has a शर् "
            "after it the visarga STAYS a visarga: **शशः "
            "क्षुरम्; पुरुषः क्षुरम्; अद्भिः प्सातम्; वासः "
            "क्षौमम्; पुरुषः त्सरुः; घनाघनः क्षोभणश् "
            "चर्षणीनाम्**. The rule is stated as a substitute of "
            "a sound for itself, which is the only way to keep "
            "8.3.34 off without a प्रतिषेध"),
    Visarga(
        "8.3.36", does="visarjanīya", gana="visarjanīya",
        before=("śar",), optional=True, blocks=("8.3.34",),
        why="वा शरि — and before a शर् it may do either: "
            "**वृक्षः शेते, वृक्षश्शेते; प्लक्षः शेते; वृक्षः "
            "षण्डे, वृक्षष्षण्डे; वृक्षः साये, वृक्षस्साये**. "
            "A vārttika adds a third possibility for a शर् with "
            "a खर् after it — **खर्परे शरि वा लोपः** — which is "
            "where the doubled स् of संस्स्कर्ता becomes single"),
    Visarga(
        "8.3.37", does="ka-pa", gana="visarjanīya",
        before=("ku", "pu"), optional=True, blocks=("8.3.34",),
        why="कुप्वोः ≍क≍पौ च — and before a guttural or a labial "
            "the visarga becomes the जिह्वामूलीय or the "
            "उपध्मानीय, one to one, and by the च may also stay: "
            "**वृक्ष≍करोति, वृक्षः करोति; वृक्ष≍खनति; "
            "वृक्ष≍पचति**. These are the two sounds Sanskrit "
            "writes with a mark of their own and almost never "
            "prints, and the rule is why a visarga before क् and "
            "before प् is not the same sound as one before त्"),
    Visarga(
        "8.3.38", does="sa", gana="visarjanīya",
        before=("ku-pu-a-pada-ādi",),
        why="सोऽपदादौ — the visarga becomes स् where the "
            "guttural or labial does NOT begin a word: "
            "**पयस्पाशम्** by 5.3.47's पाशप्, **पयस्कल्पम्, "
            "यशस्कल्पम्** by 5.3.67's कल्पप्, and so for the क "
            "and the काम्य. Four affixes make the whole of the "
            "rule's scope, since only they put a क or a प after "
            "a word without beginning one"),
    Visarga(
        "8.3.39", does="ṣa", gana="iṇ-para-visarjanīya",
        before=("ku-pu-a-pada-ādi",), blocks=("8.3.38",),
        why="इणः षः — but after an इण् it is ष्: **सर्पिष्पाशम्, "
            "यजुष्पाशम्; सर्पिष्कल्पम्; सर्पिष्कः; "
            "सर्पिष्काम्यति**. The pair 8.3.38–39 is the same "
            "division 8.3.57's इण्कोः will make of the whole "
            "rest of the pāda, stated here for one sound and "
            "four affixes"),
    Visarga(
        "8.3.40", does="sa", of=("namas", "puras"),
        gana="gati", before=("ku", "pu"), blocks=("8.3.37",),
        keeps_out="नमः कृत्वा, पुरः कृत्वा — the word is not a "
                  "गति there, and the visarga stands",
        why="नमस्पुरसोर्गत्योः — नमस् and पुरस्, WHERE THEY ARE "
            "PREVERBS, take स् before a guttural or a labial: "
            "**नमस्कर्ता, नमस्कर्तुम्, नमस्कर्तव्यम्; "
            "पुरस्कर्ता**. The condition is the गति name of "
            "1.4.60 and following, and without it नमः कृत्वा "
            "would come out नमस्कृत्वा"),
    Visarga(
        "8.3.41", does="ṣa", of=NIRADI,
        gana="i-u-upadha-a-pratyaya", before=("ku", "pu"),
        blocks=("8.3.37",),
        why="इदुदुपधस्य चाप्रत्ययस्य — and a word with इ or उ in "
            "its penult, provided it is not an affix, takes ष्: "
            "**निष्कृतम्, निष्पीतम्; दुष्कृतम्, दुष्पीतम्; "
            "बहिष्कृतम्; आविष्कृतम्; चतुष्कपालम्; "
            "प्रादुष्कृतम्**. The Kāśikā lists the words the "
            "condition picks out — निर्, दुर्, बहिर्, आविस्, "
            "चतुर्, प्रादुस् — so the shape is a way of naming "
            "six words and not a class"),
    Visarga(
        "8.3.42", does="sa", of=("tiras",), gana="gati",
        before=("ku", "pu"), optional=True, blocks=("8.3.37",),
        keeps_out="तिरः कृत्वा काण्डम् — not a गति, and neither "
                  "form of the option comes",
        why="तिरसोऽन्यतरस्याम् — तिरस् takes स् only OPTIONALLY: "
            "**तिरस्कर्ता, तिरः कर्ता; तिरस्कर्तुम्, तिरः "
            "कर्तुम्**. गतेः is carried down from 8.3.40, two "
            "sūtras back, so the same condition holds and the "
            "only difference between the two rules is that this "
            "one is a choice"),
    Visarga(
        "8.3.43", does="ṣa", of=DVIS_THREE,
        before=("ku", "pu"), sense=("kṛtvo'rtha",),
        optional=True, blocks=("8.3.37",),
        why="द्विस्त्रिश्चतुरिति कृत्वोऽर्थे — द्विस्, त्रिस् "
            "and चतुर् take ष् where a NUMBER OF TIMES is "
            "meant, optionally: **द्विष्करोति, द्विःकरोति; "
            "त्रिष्करोति; चतुष्करोति**. ष is carried down from "
            "8.3.41 by अनुवृत्ति — **ष इति सम्बध्यते** — and "
            "the sense is what tells चतुर् 'four times' from "
            "the चतुर् of 8.3.41"),
    Visarga(
        "8.3.44", does="ṣa", gana="is-us-anta",
        before=("ku", "pu"), sense=("sāmarthya",),
        optional=True, blocks=("8.3.37",),
        keeps_out="तिष्ठतु सर्पिः, पिब त्वम् उदकम् — the two "
                  "words are not construed together",
        why="इसुसोः सामर्थ्ये — and an इस्- or उस्-final word "
            "where the two words are CONSTRUED TOGETHER: "
            "**सर्पिष्करोति, सर्पिः करोति; यजुष्करोति, यजुः "
            "करोति**. Where they are not — the counter-example "
            "is two whole clauses side by side — no option "
            "arises at all, which is what सामर्थ्य means here"),
    Visarga(
        "8.3.45", does="ṣa", gana="is-us-anta",
        before=("ku", "pu"), sense=("samāsa",),
        blocks=("8.3.44",),
        keeps_out="परमसर्पिष्कुण्डिका would not be reached by "
                  "the visarga standing INSIDE the second "
                  "member, which अनुत्तरपदस्थस्य shuts out",
        why="नित्यं समासेऽनुत्तरपदस्थस्य — but inside a COMPOUND "
            "the ष् is compulsory, provided the visarga is not "
            "standing in the second member: **सर्पिष्कुण्डिका, "
            "धनुष्कपालम्, सर्पिष्पानम्, धनुष्फलम्**. What was a "
            "choice one sūtra back is fixed here, and the "
            "difference between सर्पिः करोति and "
            "सर्पिष्कुण्डिका is nothing but the compounding"),
    Visarga(
        "8.3.46", does="sa", gana="a-anta-an-avyaya",
        before=KRKAMI_SEVEN, sense=("samāsa",),
        blocks=("8.3.37",),
        why="अतः कृकमिकंसकुम्भपात्रकुशाकर्णीष्वनव्ययस्य — an "
            "अ-final word that is not indeclinable takes स् "
            "inside a compound before seven named words: "
            "**अयस्कारः, पयस्कारः** before कृ; **अयस्कामः, "
            "पयस्कामः** before कमि; and so before कंस, कुम्भ, "
            "पात्र, कुशा and कर्णी. The list is one of the "
            "longest in the pāda and every one of its members "
            "begins with a guttural or a labial"),
    Visarga(
        "8.3.47", does="sa", of=("adhas", "śiras"),
        before=("pada",), sense=("samāsa",), blocks=("8.3.37",),
        keeps_out="अधः पदम् — no compound, and the visarga "
                  "stands",
        why="अधःशिरसी पदे — अधस् and शिरस् take स् inside a "
            "compound before पद: **अधस्पदम्, शिरस्पदम्; "
            "अधस्पदी, शिरस्पदी**. Both conditions of the sūtra "
            "before are carried down — the compound and the "
            "not-in-the-second-member — and only the list and "
            "the following word are new"),
    Visarga(
        "8.3.48", does="sa", gana="kaskādi", before=("ku", "pu"),
        blocks=("8.3.37",),
        why="कस्कादिषु च — and in the कस्कादि class the visarga "
            "becomes स् or ष् as each word requires: **कस्कः; "
            "कौतस्कुतः; भ्रातुष्पुत्रः; शुनस्कर्णः; सद्यस्कालः; "
            "सद्यस्क्रीः**. The class is a list of finished "
            "words rather than a shape, which is why the sūtra "
            "can leave यथायोगम् to sort out which of the two "
            "sounds each takes"),
    Visarga(
        "8.3.49", does="sa", gana="visarjanīya",
        before=("ku", "pu"), chandasi=True, optional=True,
        blocks=("8.3.37",),
        keeps_out="the प्र and the आम्रेडित, which the sūtra "
                  "excepts by name",
        why="छन्दसि वाऽप्राम्रेडितयोः — and in the VEDA the स् "
            "comes optionally before any guttural or labial, "
            "except before प्र and before an आम्रेडित: "
            "**अयःपात्रम्, अयस्पात्रम्; विश्वतः पात्रम्, "
            "विश्वतस्पात्रम्**. This is the widest of the "
            "seventeen and the only one that needs no condition "
            "on the word at all"),
    Visarga(
        "8.3.50", does="sa", gana="a-aditi-visarjanīya",
        before=("kaḥ", "karat", "karati", "kṛdhi", "kṛta"),
        chandasi=True, blocks=("8.3.37",),
        why="कःकरत्करतिकृधिकृतेष्वनदितेः — and in the Veda "
            "before five forms of कृ, unless the word is अदिति: "
            "**विश्वतस्कः; विश्वतस्करत्; पयस्करति; उरु णस् "
            "कृधि; ज्योतिष्कृतम्**. Five particular forms of "
            "one root are named where a class would have done, "
            "which is what a Vedic rule of this pāda usually "
            "looks like"),
    Visarga(
        "8.3.51", does="sa", case="pañcamī", before=("pari",),
        sense=("adhi",), chandasi=True, blocks=("8.3.37",),
        why="पञ्चम्याः परावध्यर्थे — an ABLATIVE's visarga "
            "becomes स् before परि in the sense of अधि: "
            "**दिवस् परि प्रथमं जज्ञे; अग्निर् हिमवतस् परि; "
            "दिवस् परि**. This is the first of the two sūtras "
            "in the pāda that turn on the CASE of the word "
            "rather than on its shape, and neither has any "
            "counterpart outside the Veda"),
    Visarga(
        "8.3.52", does="sa", case="pañcamī", before=("pātu",),
        chandasi=True, optional=True, blocks=("8.3.37",),
        keeps_out="परिषदः पातु — where the स् does not come, "
                  "which बहुलम् allows",
        why="पातौ च बहुलम् — and before the root पा it comes "
            "VARIOUSLY: **दिवस् पातु; राज्ञस् पातु** — and "
            "**न च भवति — परिषदः पातु**. बहुलम् here is doing "
            "what it always does: recording that the Vedic "
            "corpus has it both ways and declining to say which "
            "way is the rule"),
    Visarga(
        "8.3.53", does="sa", case="ṣaṣṭhī", before=PATI_SEVEN,
        chandasi=True, blocks=("8.3.37",),
        why="षष्ठ्याः पतिपुत्रपृष्ठपारपदपयस्पोषेषु — and a "
            "GENITIVE's visarga becomes स् before seven named "
            "words: **वाचस्पतिं विश्वकर्माणम् ऊतये; दिवस् "
            "पुत्राय सूर्याय**, and so before पृष्ठ, पार, पद, "
            "पयस् and पोष. Every one of the seven begins with "
            "प, so the following sound is the same throughout "
            "and it is the case that does the work"),
    Visarga(
        "8.3.54", does="sa", of=("iḍā",), case="ṣaṣṭhī",
        before=PATI_SEVEN, chandasi=True, optional=True,
        blocks=("8.3.53",),
        why="इडाया वा — but of इडा it comes only optionally: "
            "**इडायास्पतिः, इडायाः पतिः; इडायास्पुत्रः, "
            "इडायाः पुत्रः; इडायास्पृष्ठम्, इडायाः पृष्ठम्**. "
            "One word is taken out of the sūtra before and "
            "given a choice, and with it the run of the "
            "visarga closes"),
)


def _reaches(row: Visarga, word: str, gana: str, before: str,
             sense: str, case: str, chandasi: bool) -> bool:
    # `of` and `gana` CONJOIN. 8.3.40 names नमस् and पुरस् AND
    # wants them to be preverbs; 8.3.54 names इडा AND wants a
    # genitive. An alternative reading would let a bare गति
    # answer for any word at all.
    if row.of and word not in row.of:
        return False
    if row.gana and gana != row.gana:
        return False
    if row.before and before not in row.before:
        return False
    if row.sense and sense not in row.sense:
        return False
    if row.case and case != row.case:
        return False
    if row.chandasi and not chandasi:
        return False
    return True


def _how_specific(row: Visarga) -> int:
    """
    A rule that displaces another beats it, a named word beats
    a shape, and a named case beats a shape too.

    8.3.44 against 8.3.45 is what needs the sense to weigh:
    सर्पिः करोति and सर्पिष्कुण्डिका differ in nothing but the
    compounding, and one is a choice and the other is not.
    """
    return (
        12 * len(row.blocks)
        + 8 * bool(row.of)
        + 6 * len(row.sense)
        + 5 * bool(row.case)
        + 4 * bool(row.gana)
        + 3 * bool(row.before)
        + 2 * bool(row.chandasi)
    )


def the_visarga(word: str = "", *, gana: str = "",
                before: str = "", sense: str = "", case: str = "",
                chandasi: bool = False) -> Joined:
    """
    8.3.34–54 — what the visarga becomes, and where it stays.

    Nothing answers by default, and the answer is the same
    `Joined` the rest of the pāda gives, since the whole of
    8.3 settles one question: what two sounds do side by side.
    """
    matched = [
        row for row in VISARGA_TABLE
        if _reaches(row, word, gana, before, sense, case, chandasi)
    ]
    if not matched:
        return Joined(
            "", "", "No rule of 8.3.34-54 is reached, so the "
                    "visarga stands as 8.3.15 left it")
    row = max(matched, key=_how_specific)
    return Joined(row.does, row.sutra, row.why,
                  optional=row.optional, blocked_by=row.blocks)


def provisions_for(sutra_id: str) -> Tuple[Visarga, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in VISARGA_TABLE
                 if row.sutra == sutra_id)


__all__ = [
    "Visarga", "VISARGA_TABLE", "VISARGA_RUN", "THE_VISARGA",
    "PASA_FOUR", "NIRADI", "DVIS_THREE", "KRKAMI_SEVEN",
    "PATI_SEVEN",
    "the_visarga", "provisions_for",
]
