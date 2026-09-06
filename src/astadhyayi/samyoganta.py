# -*- coding: utf-8 -*-
"""
८.२.२३–४१ — संयोगान्तस्य लोपः, and what a consonant becomes at the end.

Two blocks. 8.2.23–29 take sounds AWAY: a word ending in a
cluster loses its last sound (गोमान्, कृतवान्), the aorist's स्
goes in four different environments (अभित्त, अकृत, अदेवीत्), and
a cluster's initial स् or क् goes at a word's end (लग्नः, तष्टः).
8.2.30–41 CHANGE them: a palatal becomes a guttural (पक्ता,
वाक्), ह् becomes ढ् or घ् or ध् or थ् by root (सोढा, दग्धा,
नद्धम्, इदमात्थ), eight roots and every छ- and श-final become ष्
(व्रष्टा, मूलवृट्), and a झल् at a word's end goes voiced
(वागत्र, त्रिष्टुबत्र).

**AND THE ORDER AMONG THEM IS THE POINT OF THE WHOLE TRIPĀDĪ.**
8.2.23's own vṛtti works three cases: in श्रेयान् and भूयान्
the रुँ of 8.2.66 comes LATER and so cannot be seen, and the
cluster's loss goes through; in यशः and पयः the जश्त्व of 8.2.39
would have had no other chance and therefore displaces it; and
in दध्यत्र the semivowel is बहिरङ्ग and invisible, so there is
no cluster to lose. One sūtra, three different answers, all of
them from 8.2.1.

**AND ONE RULE IS STATED FOR A SOUND THAT WOULD OTHERWISE NEVER
BE HEARD.** 8.2.25 धि च drops the स् before a ध-initial ending
— **यद्य् अत्र सकारलोपो न स्यात्, सिचः षत्वे जश्त्वे च
विभाषेटः इति मूर्धन्याभावपक्षेऽपि न धकारः श्रूयेत** — without
it अलविध्वम् would come out with no ध् in it at all.

**WHAT THIS MODULE DOES NOT DO.** It says what the sound
becomes. Which affix is there is अध्याय ३'s, and the ordering
itself is 8.2.1's, codified already.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

from src.astadhyayi.nalopa_matup import Changed  # noqa: E402

#: This module's stretch.
SAMYOGA_RUN: Tuple[str, str] = ("8.2.23", "8.2.41")

#: Where the run turns from taking sounds away to changing them.
CHANGES_FROM: str = "8.2.30"

#: 8.2.33's four, whose ह् becomes घ् only optionally.
DRUH_FOUR: Tuple[str, ...] = ("druh", "muh", "ṣṇuh", "ṣṇih")

#: 8.2.36's eight, which become ष् along with every छ- and
#: श-final root.
VRASCADI_EIGHT: Tuple[str, ...] = (
    "vraśc", "bhrasj", "sṛj", "mṛj", "yaj", "rāj", "bhrāj")

#: What 8.2.23's vṛtti settles about its own place in the order.
THREE_ANSWERS: str = (
    "इह श्रेयान्, भूयान् इति रुत्वं परम् अपि असिद्धत्वात् "
    "संयोगान्तस्य लोपं न बाधते। जश्त्वे तु न अप्राप्ते तद् "
    "आरभ्यत इति तस्य बाधकं भवति — यशः, पय इति। दध्यत्र, "
    "मध्वत्र इत्यत्र तु यणादेशस्य बहिरङ्गलक्षणस्य असिद्धत्वात् "
    "संयोगान्तलोपो न भवति")


@dataclass(frozen=True)
class End:
    """One rule of 8.2.23–41: a sound lost or a sound changed."""

    sutra: str
    #: `lopa`, `ku`, `ḍha`, `gha`, `dha`, `tha`, `ṣa`, `bhaṣ`,
    #: `jaś`, `ka`.
    does: str = ""
    #: The roots named outright.
    of: Tuple[str, ...] = ()
    #: The shape of what the rule reaches.
    gana: str = ""
    #: What must follow, `pada-anta` among the alternatives
    #: because a word's end is a condition like any other here.
    before: Tuple[str, ...] = ()
    optional: bool = False
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


SAMYOGA_TABLE: Tuple[End, ...] = (
    End(
        "8.2.23", does="lopa", gana="saṃyoga-anta",
        before=("pada-anta",),
        why="संयोगान्तस्य लोपः — a word ending in a CLUSTER "
            "loses its last sound: **गोमान्, यवमान्, कृतवान्, "
            "हतवान्** — गोमन्त् gives गोमान्, and the त् is "
            "simply gone.\\n\\n"
            "**AND ITS OWN VṚTTI WORKS THREE ORDERINGS AND GETS "
            "THREE DIFFERENT ANSWERS.** In श्रेयान् and भूयान् "
            "the रुँ of 8.2.66 is LATER and therefore invisible "
            "— **रुत्वं परम् अपि असिद्धत्वात् संयोगान्तस्य "
            "लोपं न बाधते** — so the cluster's loss goes "
            "through. In यशः and पयः the जश्त्व of 8.2.39 "
            "would have had no other chance at all — **जश्त्वे "
            "तु न अप्राप्ते तद् आरभ्यत इति तस्य बाधकं भवति** "
            "— so it displaces this rule. And in दध्यत्र the "
            "semivowel is बहिरङ्ग and invisible, so there is no "
            "cluster here to lose. Three answers from one "
            "heading"),
    End(
        "8.2.24", does="lopa", gana="repha-saṃyoga-anta",
        before=("pada-anta",), blocks=("8.2.23",),
        why="रात् सस्य — and where the cluster has a र् in it, "
            "it is the स् that goes and not the last sound: "
            "**गोभिर् अक्षाः; प्रत्यञ्चम् अत्साः**. Without it "
            "8.2.23 would take the स् off अक्षार्स् and leave "
            "*अक्षार्. The vṛtti derives both forms in full — "
            "the aorist of क्षर् and त्सर् with no इट्, "
            "**सिचः छान्दसत्वाद् ईडभावः 7.3.97 इति वचनात्** — "
            "and adds that मातुः and पितुः come out the same "
            "way through 6.1.111's उत्"),
    End(
        "8.2.25", does="lopa", gana="sic", before=("dha-ādi",),
        keeps_out="चकाद्धि पलितं शिरः; पयो धावति — neither स् "
                  "is the aorist's",
        why="धि च — and the aorist's स् goes before a ध-initial "
            "ending: **अलविध्वम्, अलविढ्वम्; अपविध्वम्, "
            "अपविढ्वम्**.\\n\\n"
            "**AND WITHOUT IT THE ध् WOULD NEVER BE HEARD AT "
            "ALL.** **यद्य् अत्र सकारलोपो न स्यात्, सिचः षत्वे "
            "जश्त्वे च विभाषेटः इति मूर्धन्याभावपक्षेऽपि न "
            "धकारः श्रूयेत** — with the स् in place the "
            "following ध् is swallowed by the cerebralisation "
            "and the voicing, and the form comes out with no ध् "
            "in it. **इतः प्रभृति सिचः सकारस्य लोप इष्यते** — "
            "from here on it is the aorist's स् that these "
            "rules mean, which is why पयो धावति is untouched"),
    End(
        "8.2.26", does="lopa", gana="jhal-anta-sic",
        before=("jhal",), keeps_out="अमंस्त, अमंस्थाः — no झल् "
                                    "before the स्; अभित्साताम्, "
                                    "अभित्सत — no झल् after it",
        why="झलो झलि — the aorist's स् goes after a झल् and "
            "before a झल्: **अभित्त, अभित्थाः; अच्छित्त, "
            "अच्छित्थाः**. Both conditions are tested and both "
            "hold. And अवात्ताम् shows the ordering again — "
            "**सिचः सकारलोपस्य असिद्धत्वात् 7.4.49 इति सकारस्य "
            "तकारः**: the loss is invisible to the rule that "
            "turns a स् into a त्, so the त् is made and only "
            "then does the स् go"),
    End(
        "8.2.27", does="lopa", gana="hrasva-anta-aṅga",
        before=("jhal",),
        keeps_out="अच्योष्ट, अप्लोष्ट — the stem's last vowel "
                  "is long; अलाविष्टाम्, अलाविषुः — the "
                  "shortness is the augment's and not the "
                  "stem's",
        why="ह्रस्वादङ्गात् — and after a stem ending in a "
            "SHORT vowel, before a झल्: **अकृत, अकृथाः; अहृत, "
            "अहृथाः**. Both words are tested — **ह्रस्वाद् इति "
            "किम्? अच्योष्ट; अङ्गाद् इति किम्? अलाविष्टाम्** — "
            "and it is the aorist's स् here too, which is why "
            "द्विष्टराम् keeps its own"),
    End(
        "8.2.28", does="lopa", gana="iṭ-anta", before=("īṭ",),
        keeps_out="अकार्षीत्, अहार्षीत् — no इट् before the स्; "
                  "अलाविष्टाम्, अलाविषुः — no ईट् after it",
        why="इट ईटि — and after an इट् before an ईट्: "
            "**अदेवीत्, असेवीत्, अकोषीत्, अमोषीत्**. This is "
            "the fourth and last of the aorist's स्-losses, and "
            "the four between them cover every place the sound "
            "would otherwise be heard: after a र्, before a ध्, "
            "between two झल्, and between the two augments"),
    End(
        "8.2.29", does="lopa", gana="sa-ka-saṃyoga-ādi",
        before=("pada-anta", "jhal"),
        keeps_out="काष्ठशक् स्थाता — the following थ् is a झल् "
                  "but not a सङ्, which a vārttika requires",
        why="स्कोः संयोगाद्योरन्ते च — the स् or क् at the HEAD "
            "of a cluster goes, at a word's end and before a "
            "झल्: from लस्ज् **लग्नः, लग्नवान्, साधुलक्**, from "
            "मस्ज् **मग्नः**, and for the क् from तक्ष् **तट्, "
            "तष्टः, तष्टवान्, काष्ठतट्**. A vārttika narrows "
            "the झल् — **झलि सङि इति वक्तव्यम्** — where सङ् is "
            "a pratyāhāra from स of सन् to the ङ of महिङ्, so "
            "that काष्ठशक् स्थाता keeps its क्"),
    End(
        "8.2.30", does="ku", gana="cu",
        before=("jhal", "pada-anta"),
        why="चोः कुः — a PALATAL becomes the answering guttural "
            "before a झल् and at a word's end: **पक्ता, "
            "पक्तुम्, पक्तव्यम्, ओदनपक्; वक्ता, वक्तुम्, "
            "वक्तव्यम्, वाक्**. This is the rule that makes "
            "पच् end in क् and वच् in क् wherever no vowel "
            "follows, and it is what the whole of 8.2.30–41 is "
            "arranged around"),
    End(
        "8.2.31", does="ḍha", gana="ha",
        before=("jhal", "pada-anta"),
        why="हो ढः — and ह् becomes ढ्: **सोढा, सोढुम्, "
            "सोढव्यम्, जलाषाट्; वोढा, वोढुम्, वोढव्यम्, "
            "प्रष्ठवाट्, दित्यवाट्**. The ढ् is then acted on "
            "further by the rules of 8.4, so what is heard is "
            "often a ट् — जलाषाट् — and the ढ् is only ever an "
            "intermediate step"),
    End(
        "8.2.32", does="gha", of=("da-ādi-dhātu",),
        before=("jhal", "pada-anta"), blocks=("8.2.31",),
        keeps_out="लेढा, लेढुम्, गुडलिट् — लिह् does not begin "
                  "with द्",
        why="दादेर्धातोर्घः — but the ह् of a root BEGINNING "
            "WITH द् becomes घ् instead: **दग्धा, दग्धुम्, "
            "दग्धव्यम्, काष्ठधक्; दोग्धा, दोग्धुम्, दोग्धव्यम्, "
            "गोधुक्**. Both words are tested — **दादेर् इति "
            "किम्? लेढा** — and धातोः is there so that the "
            "द-initial is asked of the ROOT and not of whatever "
            "stands in front of it"),
    End(
        "8.2.33", does="gha", of=DRUH_FOUR,
        before=("jhal", "pada-anta"), optional=True,
        blocks=("8.2.31", "8.2.32"),
        why="वा द्रुहमुहष्णुहष्णिहाम् — and for द्रुह्, मुह्, "
            "ष्णुह् and ष्णिह् the घ् comes only optionally, "
            "the ढ् standing beside it: **द्रोग्धा, द्रोढा; "
            "मित्रध्रुक्, मित्रध्रुट्; उन्मोग्धा, उन्मोढा; "
            "उन्मुक्, उन्मुट्**. None of the four begins with "
            "द्, so 8.2.32 could not have reached them at all "
            "— the option is between this rule and 8.2.31"),
    End(
        "8.2.34", does="dha", of=("nah",),
        before=("jhal", "pada-anta"), blocks=("8.2.31",),
        why="नहो धः — and the ह् of नह् becomes ध्: **नद्धम्, "
            "नद्धुम्, नद्धव्यम्; उपानत्, परीणत्**. उपानह् is "
            "the shoe that is tied on, and उपानत् is what is "
            "left of it after this rule and 8.4's have both "
            "run — one root and four sūtras between the written "
            "form and the spoken one"),
    End(
        "8.2.35", does="tha", of=("āh",), before=("jhal",),
        blocks=("8.2.31",),
        keeps_out="आह, आहतुः, आहुः — no झल् follows, and the ह् "
                  "stands",
        why="आहस्थः — and the ह् of आह् becomes थ्: **इदम् "
            "आत्थ; किम् आत्थ**. The substitute is a fourth "
            "different sound for the same ह्, and the vṛtti "
            "says why one was needed at all — **आदेशान्तरकरणं "
            "8.2.40 इत्यस्य निवृत्त्यर्थम्**: a ढ् would have "
            "been turned into ध् by that rule, and थ् is chosen "
            "to keep it out.\\n\\n"
            "**AND A VĀRTTIKA GIVES THE VEDA A FIFTH.** "
            "**हृग्रहोर् भश् छन्दसि हस्य इति वक्तव्यम्** — the "
            "ह् of हृ and ग्रह् becomes भ् in the Veda"),
    End(
        "8.2.36", does="ṣa", of=VRASCADI_EIGHT,
        gana="cha-śa-anta", before=("jhal", "pada-anta"),
        why="व्रश्चभ्रस्जसृजमृजयजराजभ्राजच्छशां षः — seven roots "
            "named outright, and every छ-final and every "
            "श-final root besides, become ष्: **व्रष्टा, "
            "व्रष्टुम्, व्रष्टव्यम्, मूलवृट्; भ्रष्टा; स्रष्टा; "
            "मार्ष्टा; यष्टा; राट्; भ्राट्**. The ष् then goes "
            "on to become ट् at a word's end by 8.4's rules, "
            "which is why मूलवृट् and राट् are heard with a "
            "stop where the sūtra puts a sibilant"),
    End(
        "8.2.37", does="bhaṣ", gana="ekāc-jhaṣ-anta-baś",
        before=("jhal", "sa", "dhva", "pada-anta"),
        why="एकाचो बशो भष् झषन्तस्य स्ध्वोः — where a "
            "MONOSYLLABIC part of a root ends in a झष् and "
            "begins with a बश्, that बश् becomes the answering "
            "भष् — the aspiration moves from the end of the "
            "syllable to its beginning. **अत्र चत्वारो बशः "
            "स्थानिनो भषादेशाश् चत्वार एव** — four sounds "
            "replaced and four replacing, so 1.3.10's "
            "one-to-one matching would apply; the vṛtti has to "
            "note that there is no ड् among the four to take "
            "the ढ्"),
    End(
        "8.2.38", does="bhaṣ", of=("dadh",),
        before=("ta", "tha", "sa", "dhva"), blocks=("8.2.40",),
        why="दधस्तथोश्च — and for दध् — that is धा with its "
            "reduplication already made — before त्, थ्, and by "
            "the च before स् and ध्व too: **धत्तः, धत्थः, "
            "धत्से, धत्स्व, धद्ध्वम्**. **वचनसामर्थ्याद् आतो "
            "लोपस्य स्थानिवद्भावः** — the आ is gone and counts "
            "as there, which is the only way the root still "
            "ends in a झष् for this rule to reach"),
    End(
        "8.2.39", does="jaś", gana="jhal-anta",
        before=("pada-anta",),
        keeps_out="वस्ता, वस्तव्यम् — a झल् follows but no "
                  "word ends, and अन्तग्रहण shuts it out",
        why="झलां जशोऽन्ते — a झल् at a WORD'S END becomes the "
            "answering जश् — the plain voiced stop: **वागत्र; "
            "श्वलिडत्र; अग्निचिदत्र; त्रिष्टुबत्र**. वाच् "
            "becomes वाक् by 8.2.30 and then वाग् by this, and "
            "which of the two is heard depends on what follows. "
            "**अन्तग्रहणं झलि इत्येतस्य निवृत्त्यर्थम्** — "
            "saying अन्ते is what stops the rule reaching "
            "inside a word"),
    End(
        "8.2.40", does="dha", gana="jhaṣ", before=("ta", "tha"),
        keeps_out="धत्तः, धत्थः — दध् is excepted by name at "
                  "8.2.38",
        why="झषस्तथोर्धोऽधः — a त् or थ् after a झष् becomes "
            "ध्, except after दध्: **लब्धा, लब्धुम्, "
            "लब्धव्यम्, अलब्ध, अलब्धाः; दोग्धा, अदुग्ध; लेढा, "
            "अलीढ**. This is what makes the whole cluster "
            "voiced and aspirated together — लभ् plus त gives "
            "लब्ध and not *लब्त — and it is the rule 8.2.35's "
            "थ् was chosen to keep out"),
    End(
        "8.2.41", does="ka", gana="ṣa-ḍha", before=("sa",),
        keeps_out="पिनष्टि, लेढि — no स् follows",
        why="षढोः कः सि — ष् and ढ् become क् before स्: from "
            "पिष् **पेक्ष्यति, अपेक्ष्यत्, पिपिक्षति**, and "
            "from लिह् **लेक्ष्यति, अलेक्ष्यत्, लिलिक्षति**. "
            "The ढ् meant is the one 8.2.31 has just made out "
            "of a ह्, so लिह् reaches this rule only by going "
            "through that one — which is what makes लेक्ष्यति "
            "and लेढा two steps apart from the same root"),
)


def _reaches(row: End, root: str, gana: str, before: str) -> bool:
    # `of` and `gana` are ALTERNATIVES here and never a
    # conjunction: 8.2.36 names seven roots AND every cha- or
    # sa-final root, and either qualification is enough on its
    # own. That is why 8.2.32, whose root must begin with द्
    # AND have a ह्, carries no `gana` at all — the first draft
    # gave it one and a bare ह् then reached it, so that सोढा
    # came out with the घ् that belongs to दग्धा.
    named = row.of or row.gana
    if named and not (root in row.of
                      or (row.gana and gana == row.gana)):
        return False
    if row.before and before not in row.before:
        return False
    return True


def _how_specific(row: End, root: str, gana: str) -> int:
    """
    A rule that displaces another beats it, and a named root
    beats a shape.

    8.2.31, 8.2.32, 8.2.33, 8.2.34 and 8.2.35 all reach a ह्
    and give it five different sounds; only the named root
    tells them apart.
    """
    return (
        12 * len(row.blocks)
        + 8 * bool(row.of and root in row.of)
        + 4 * bool(row.gana and gana == row.gana)
        + 3 * bool(row.before)
    )


def at_the_end(root: str = "", *, gana: str = "",
               before: str = "") -> Changed:
    """
    8.2.23–41 — the cluster's loss and the consonant's change.

    Nothing answers by default. A sound none of these rules
    reaches stands as it is.
    """
    matched = [
        row for row in SAMYOGA_TABLE
        if _reaches(row, root, gana, before)
    ]
    if not matched:
        return Changed(
            "", "", "No rule of 8.2.23-41 is reached, so the "
                    "sound stands as it is")
    row = max(matched, key=lambda one: _how_specific(one, root, gana))
    return Changed(row.does, row.sutra, row.why,
                   optional=row.optional, blocked_by=row.blocks)


def provisions_for(sutra_id: str) -> Tuple[End, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in SAMYOGA_TABLE
                 if row.sutra == sutra_id)


__all__ = [
    "End", "SAMYOGA_TABLE", "SAMYOGA_RUN", "CHANGES_FROM",
    "DRUH_FOUR", "VRASCADI_EIGHT", "THREE_ANSWERS",
    "at_the_end", "provisions_for",
]
