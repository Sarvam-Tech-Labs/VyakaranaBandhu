# -*- coding: utf-8 -*-
"""
७.३.५२–६९ — च् and ज् become gutturals, and the ten refusals.

7.3.52 चजोः कु घिन्ण्यतोः turns a च् or ज् into the corresponding
guttural before a घित् affix and before ण्यत्: पाकः, त्यागः,
रागः, पाक्यम्, वाक्यम्. 7.3.53 adds a list of nouns already so
made — न्यङ्कुः, मद्गुः, भृगुः — and 7.3.54–58 give हन् and हि
and जि and चि the same change after a reduplication: घातयति,
घ्नन्ति, जिघांसति, जिगीषति.

**AND THEN TEN SŪTRAS TAKE IT BACK, IN A STRETCH OF ELEVEN.**
7.3.59 to 7.3.69 look like one block of refusals and are not:
7.3.64 ओक उचः के sits in the middle of them and SUPPLIES the
guttural, laying down ओकस् with the guṇa besides. A root that
BEGINS with
a guttural keeps its own (कूजः, गर्जः); अज् and व्रज् keep theirs
(समाजः, परिव्राजः); भुज and न्युब्ज are laid down as nouns
(भुजः पाणिः); प्रयाज and अनुयाज belong to the rite; वञ्च् keeps
its च् of GOING; and six sūtras refuse the change before ण्यत्
alone — अवश्यपाच्यम्, याज्यम्, याच्यम्, वाच्यम्, प्रयोज्यः,
भोज्यम्.

**AND THE REFUSALS BEFORE ण्यत् TURN ON A SENSE EVERY TIME.**
अवश्यपाच्यम् of what MUST be cooked but पाक्यम् otherwise;
वाच्यम् of what is said but वाक्यम् as a grammarian's term;
प्रयोज्यः of what CAN be employed but प्रयोग्यः otherwise;
भोज्यः of food but भोग्यः of a blanket. Six rules, six senses,
and each pair of forms differs in one sound.

**WHAT THIS MODULE DOES NOT DO.** It says which sound the च् or
ज् becomes by class. Which guttural exactly is 1.1.50's — the
nearest one.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: This module's stretch.
KUTVA_RUN: Tuple[str, str] = ("7.3.52", "7.3.69")

#: Where the refusals begin.
REFUSALS_FROM: str = "7.3.59"

#: 7.3.66's five, which refuse the change before ण्यत्.
YAJADI: Tuple[str, ...] = ("yaj", "yāc", "ruc", "pravac", "ṛc")

#: 7.3.61–62 and 7.3.68–69's laid-down nouns, each with the sense
#: that licenses it.
NIPATANA: Tuple[Tuple[str, str], ...] = (
    ("bhuja", "pāṇi"), ("nyubja", "upatāpa"),
    ("prayāja", "yajña-aṅga"), ("anuyāja", "yajña-aṅga"),
    ("prayojya", "śakya"), ("niyojya", "śakya"),
    ("bhojya", "bhakṣya"))


@dataclass(frozen=True)
class Kutva:
    """One rule of 7.3.52–69: the guttural, or its refusal."""

    sutra: str
    #: `kutva` where the change happens, `guṇa` where 7.3.64 also
    #: strengthens, "" where it is refused.
    does: str = "kutva"
    #: The roots or words named outright.
    of: Tuple[str, ...] = ()
    #: The root class instead.
    gana: str = ""
    #: What must follow.
    before: Tuple[str, ...] = ()
    #: What must NOT follow.
    not_before: Tuple[str, ...] = ()
    #: The sense that licenses or shuts out the form.
    sense: str = ""
    #: The sense the rule shuts out.
    excludes: str = ""
    #: True where the change is stated after a reduplication.
    abhyasa: bool = False
    refuses: bool = False
    optional: bool = False
    nipatana: bool = False
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


KUTVA_TABLE: Tuple[Kutva, ...] = (
    Kutva(
        "7.3.52", gana="c-j-anta", before=("ghit", "ṇyat"),
        why="चजोः कु घिन्ण्यतोः — a च् or ज् becomes the "
            "corresponding guttural before a घित् affix and "
            "before ण्यत्: **पाकः, त्यागः, रागः** for the घित्; "
            "**पाक्यम्, वाक्यम्, रेक्यम्** for the ण्यत्. Which "
            "guttural exactly is 1.1.50's business — the nearest "
            "one"),
    Kutva(
        "7.3.53", gana="nyaṅku-ādi",
        why="न्यङ्क्वादीनां च — and a list of nouns already so "
            "made: **न्यङ्कुः, मद्गुः, भृगुः; दूरेपाकः, "
            "फलेपाकः**. Each is worked back to the Uṇādi affix "
            "that built it — **नावञ्चेः**, **मिमस्जिभ्य उः**, "
            "**प्रथिम्रदिभ्रस्जां संप्रसारणं सलोपश्च** — and the "
            "vṛtti notes that some read क्षणेपाक into the list "
            "as well"),
    Kutva(
        "7.3.54", of=("han",), before=("ñit", "na"),
        keeps_out="प्रहारः, प्रहारकः — the root is not हन् but "
                  "हृ, and the rule names हन् by its own form",
        why="हो हन्तेर्ञ्णिन्नेषु — हन्'s ह् becomes a guttural "
            "before a ञित् affix and before न्: **घातयति, "
            "घातकः, साधुघाती, घातो वर्तते** for the ञित्; "
            "**घ्नन्ति, घ्नन्तु, अघ्नन्** for the न्.\\n\\n"
            "**AND WHETHER THE न् MUST STAND IMMEDIATELY AFTER "
            "IS ANSWERED CAREFULLY.** **तच्चानन्तर्यं "
            "संनिपातकृतम् आश्रीयते। स्थानिवद्भावशास्त्रकृतं तु "
            "यद् अनानन्तर्यं तद् अविघातकम्, वचनसामर्थ्यात्** — "
            "an interval made by the sounds themselves stops the "
            "rule; one made by a substitution's counting as its "
            "original does not"),
    Kutva(
        "7.3.55", of=("han",), abhyasa=True,
        keeps_out="जिहननीयिषति — the reduplication belongs to a "
                  "derived stem and not to हन् itself",
        why="अभ्यासाच्च — and after a reduplication: "
            "**जिघांसति, जङ्घन्यते, अहं जघन**. The "
            "reduplication must be हन्'s own — **अभ्यासनिमित्ते "
            "प्रत्यये हन्तेरङ्गस्य योऽभ्यासस्तस्माद् एवैतत् "
            "कुत्वम्**"),
    Kutva(
        "7.3.56", of=("hi",), abhyasa=True, not_before=("caṅ",),
        keeps_out="प्राजीहयद् दूतम् — the चङ् aorist, named out",
        why="हेरचङि — and हि's ह् after a reduplication, except "
            "in the चङ् aorist: **प्रजिघीषति, प्रजेघीयते, "
            "प्रजिघाय**.\\n\\n"
            "**AND THE EXCEPTION IS SHOWN TO BE UNNECESSARY AND "
            "KEPT FOR WHAT IT PROVES.** **अचङीति शक्यम् "
            "अकर्तुम्** — in the चङ् the stem is not हि but the "
            "causal, so the rule could not have reached. "
            "**तत् क्रियते ज्ञापकार्थम्। एतद् ज्ञाप्यते — "
            "हेरचङीति चङोऽन्यत्र हेर् ण्यधिकस्यापि कुत्वं भवति** "
            "— outside the चङ् the change reaches a हि that has "
            "a णि on it, which is what gets प्रजिघाययिषति"),
    Kutva(
        "7.3.57", of=("ji",), abhyasa=True, before=("san", "liṭ"),
        keeps_out="जेजीयते — neither सन् nor the perfect; "
                  "जिज्यतुः — the जि is one संप्रसारण made from "
                  "ज्या, and **लाक्षणिकत्वात् तस्य ग्रहणं न "
                  "भवति**",
        why="सन्लिटोर्जेः — जि's ज् becomes a guttural after its "
            "reduplication, before सन् and the perfect: "
            "**जिगीषति, जिगाय**"),
    Kutva(
        "7.3.58", of=("ci",), abhyasa=True, before=("san", "liṭ"),
        optional=True,
        keeps_out="चेचीयते — neither सन् nor the perfect",
        why="विभाषा चेः — and चि's च् OPTIONALLY: **चिचीषति, "
            "चिकीषति; चिचाय, चिकाय**. The sūtra before had made "
            "the change compulsory for जि in the same two "
            "environments; here it is a choice, and both forms "
            "of each stand"),
    Kutva(
        "7.3.59", refuses=True, does="", gana="ku-ādi",
        before=("ghit", "ṇyat"), blocks=("7.3.52",),
        why="न क्वादेः — but a root that BEGINS with a guttural "
            "keeps its own: **कूजो वर्तते; खर्जः; गर्जः; कूज्यं "
            "भवता; खर्ज्यम्, गर्ज्यं भवता**"),
    Kutva(
        "7.3.60", refuses=True, does="", of=("aj", "vraj"),
        before=("ghit", "ṇyat"), blocks=("7.3.52",),
        why="अजिवृज्योश्च — and अज् and व्रज्: **समाजः, उदाजः; "
            "परिव्राजः, परिव्राज्यम्**. There is no example of "
            "अज् before ण्यत्, 2.4.56 having replaced it with "
            "वी there — **अजेस्तु अजेर्व्यघञपोः इति वीभावस्य "
            "विधानाद् ण्यति नास्त्युदाहरणम्**"),
    Kutva(
        "7.3.61", refuses=True, does="", of=("bhuja", "nyubja"),
        sense="pāṇi-upatāpa", before=("ghañ",), nipatana=True,
        blocks=("7.3.52",),
        keeps_out="भोगः, समुद्गः — neither a hand nor an ailment "
                  "is meant",
        why="भुजन्युब्जौ पाण्युपतापयोः — भुज and न्युब्ज are laid "
            "down as a HAND and an AILMENT: **भुज्यतेऽनेनेति "
            "भुजः पाणिः; न्युब्जिताः शेरतेऽस्मिन्निति न्युब्ज "
            "उपतापो रोगः**. For the first the guṇa is refused as "
            "well, both being **निपात्यते** together"),
    Kutva(
        "7.3.62", refuses=True, does="",
        of=("prayāja", "anuyāja"), sense="yajña-aṅga",
        nipatana=True, blocks=("7.3.52",),
        keeps_out="प्रयागः, अनुयागः — no part of a rite is meant",
        why="प्रयाजानुयाजौ यज्ञाङ्गे — प्रयाज and अनुयाज are laid "
            "down as PARTS OF A RITE: **पञ्च प्रयाजाः; पञ्च "
            "अनुयाजाः**. And the two are named as a specimen — "
            "**प्रदर्शनार्थम्, अन्यत्राप्येवंप्रकारे कुत्वं न "
            "भवति** — so एकादशोपयाजाः, पत्नीसंयाजाः and "
            "ऋतुयाजैः all come out the same way"),
    Kutva(
        "7.3.63", refuses=True, does="", of=("vañc",),
        sense="gati", blocks=("7.3.52",),
        keeps_out="वङ्कं काष्ठम् — crooked wood, and no going "
                  "meant",
        why="वञ्चेर्गतौ — वञ्च् keeps its च् where GOING is "
            "meant: **वञ्च्यं वञ्चन्ति वणिजः**, the traders "
            "travel a road that can be travelled. "
            "**गताविति किम्? वङ्कं काष्ठम्। कुटिलम् इत्यर्थः** — "
            "crooked wood, where the guttural comes"),
    Kutva(
        "7.3.64", does="kutva-guṇa", of=("uc",), before=("ka",),
        nipatana=True,
        why="ओक उचः के — ओकस् is laid down from उच् before क, "
            "with both the guttural and the guṇa: **न्योकः "
            "शकुन्तः; न्योको गृहम्**.\\n\\n"
            "**AND IT IS BUILT ON क RATHER THAN घञ् FOR THE "
            "ACCENT.** **किमर्थं पुनर् अयं घञ्येव न "
            "व्युत्पाद्यते? स्वरार्थम्, अन्तोदात्तोऽयम् इष्यते, "
            "घञि सत्याद्युदात्तः स्यात्** — the word is wanted "
            "with its accent at the end, and a घञ् would have "
            "put it at the front"),
    Kutva(
        "7.3.65", refuses=True, does="", before=("ṇya",),
        sense="āvaśyaka", blocks=("7.3.52",),
        keeps_out="पाक्यम्, वाक्यम्, रेक्यम् — no necessity meant",
        why="ण्य आवश्यके — the change is refused before ण्य where "
            "NECESSITY is meant: **अवश्यपाच्यम्, अवश्यवाच्यम्, "
            "अवश्यरेच्यम्**. Six sūtras from here refuse it "
            "before this affix alone, and every one of them "
            "turns on a sense"),
    Kutva(
        "7.3.66", refuses=True, does="", of=YAJADI,
        before=("ṇya",), blocks=("7.3.52",),
        why="यजयाचरुचप्रवचर्चश्च — and for five roots: **याज्यम्, "
            "याच्यम्, रोच्यम्, प्रवाच्यम्, अर्च्यम्**. प्रवच is "
            "named for the sake of a technical term — "
            "**प्रवाच्यो नाम पाठविशेषोपलक्षितो ग्रन्थोऽस्ति** — "
            "or, on another reading, to restrict the next "
            "sūtra's refusal to that one preverb"),
    Kutva(
        "7.3.67", refuses=True, does="", of=("vac",),
        before=("ṇyat",), excludes="śabda-saṃjñā",
        blocks=("7.3.52",),
        keeps_out="अवघुषितं वाक्यम् — वाक्य as a grammarian's "
                  "term, where the guttural stands",
        why="वचोऽशब्दसंज्ञायाम् — and for वच् where the word is "
            "NOT a technical term: **वाच्यमाह; अवाच्यमाह**. "
            "One sound between what is said and what a grammar "
            "calls a sentence"),
    Kutva(
        "7.3.68", refuses=True, does="",
        of=("prayojya", "niyojya"), sense="śakya", nipatana=True,
        blocks=("7.3.52",),
        keeps_out="प्रयोग्यः, नियोग्यः — no possibility meant",
        why="प्रयोज्यनियोज्यौ शक्यार्थे — प्रयोज्य and नियोज्य "
            "are laid down of what CAN be employed or enjoined: "
            "**शक्यः प्रयोक्तुं प्रयोज्यः; शक्यो नियोक्तुं "
            "नियोज्यः**"),
    Kutva(
        "7.3.69", refuses=True, does="", of=("bhojya",),
        sense="bhakṣya", nipatana=True, blocks=("7.3.52",),
        keeps_out="भोग्यः कम्बलः — a blanket is enjoyed and not "
                  "eaten",
        why="भोज्यं भक्ष्ये — and भोज्य of FOOD: **भोज्य ओदनः; "
            "भोज्या यवागूः**. **इह भक्ष्यम् अभ्यवहार्यमात्रम्** "
            "— anything swallowed, and not the narrower sense "
            "the word has elsewhere"),
)


def _reaches(row: Kutva, root: str, gana: str, before: str,
             sense: str, abhyasa: bool) -> bool:
    named = row.of or row.gana
    if named and not (root in row.of
                      or (row.gana and gana == row.gana)):
        return False
    if row.before and before not in row.before:
        return False
    if row.not_before and before in row.not_before:
        return False
    if row.sense and sense != row.sense:
        return False
    if row.excludes and sense == row.excludes:
        return False
    if row.abhyasa and not abhyasa:
        return False
    return True


def _how_specific(row: Kutva, root: str, gana: str) -> int:
    """
    A refusal outweighs a rule that merely displaces, a named
    sense beats a named root, and a named root beats a class.

    7.3.52 against the eleven that refuse it is the whole of it,
    and 7.3.65 to 7.3.69 need the sense: पाक्यम् and
    अवश्यपाच्यम् differ in one sound and in nothing else.
    """
    return (
        14 * bool(row.refuses)
        + 12 * (0 if row.refuses else len(row.blocks))
        + 8 * bool(row.sense)
        + 6 * bool(row.of and root in row.of)
        + 4 * bool(row.gana and gana == row.gana)
        + 3 * bool(row.abhyasa)
        + 2 * bool(row.before)
    )


@dataclass(frozen=True)
class Made:
    """What the run answers: the guttural, or its refusal."""

    does: str
    sutra: str
    why: str
    nipatana: bool = False
    optional: bool = False
    blocked_by: Tuple[str, ...] = ()


def guttural(root: str = "", *, gana: str = "", before: str = "",
             sense: str = "", abhyasa: bool = False) -> Made:
    """
    7.3.52–69 — whether a च् or ज् becomes a guttural.

    Nothing answers by default. A root with no palatal at the
    point the rule reaches takes nothing from this run.
    """
    matched = [
        row for row in KUTVA_TABLE
        if _reaches(row, root, gana, before, sense, abhyasa)
    ]
    if not matched:
        return Made(
            "", "", "No rule of 7.3.52-69 is reached, so no "
                    "guttural is stated here")
    row = max(matched, key=lambda one: _how_specific(one, root, gana))
    return Made("" if row.refuses else row.does, row.sutra,
                row.why, nipatana=row.nipatana,
                optional=row.optional, blocked_by=row.blocks)


def provisions_for(sutra_id: str) -> Tuple[Kutva, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in KUTVA_TABLE if row.sutra == sutra_id)


__all__ = [
    "Kutva", "KUTVA_TABLE", "KUTVA_RUN", "REFUSALS_FROM",
    "YAJADI", "NIPATANA", "Made", "guttural", "provisions_for",
]
