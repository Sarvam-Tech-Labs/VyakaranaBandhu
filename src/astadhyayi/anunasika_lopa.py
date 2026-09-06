# -*- coding: utf-8 -*-
"""
६.४.३४–४५ — शास्, हन्, and the nasal that goes or becomes आ.

Twelve rules and one recurring stem-shape: a root ending in a
nasal, before an affix that begins with a झल् or is a क्विप्. What
happens to the nasal is the whole of the run, and three different
things happen — it is DROPPED (6.4.37, 6.4.40), it becomes आ
(6.4.41–45), or the rule refuses both (6.4.39).

**AND THE CLASS IS NAMED BY ITS ACCENT IN THE DHĀTUPĀṬHA.**
6.4.37 अनुदात्तोपदेश — roots taught with a low accent — is not a
phonetic class at all: **अनुदात्तोपदेशा अनुनासिकान्ता
यमिरमिनमिगमिहनिमन्यतयः**, seven roots, and the accent they carry
where Pāṇini lists them is what gathers them.

**AND ONE OPTION IS SETTLED RATHER THAN FREE.** 6.4.38 वा ल्यपि
is **व्यवस्थितविभाषा** — **तेन मकारान्तानां विकल्पो भवति,
अन्यत्र नित्यमेव लोपः**: the म्-final roots have the choice and
the rest simply drop. प्रयत्य beside प्रयम्य, but आहत्य alone.

**AND ONE REFUSAL HAS TO REFUSE TWICE.** 6.4.39's न stops the
nasal-loss, and then 6.4.15's lengthening would have applied to
what the loss left — **अनुनासिकलोपे प्रतिषिद्धे अनुनासिकस्य
क्विझलोः क्ङिति इति दीर्घः प्राप्नोति, सोऽपि प्रतिषिध्यते** — so
the sūtra says दीर्घश्च and refuses that too.

**WHAT THIS MODULE DOES NOT DO.** It reports what becomes of the
nasal and by which rule. It does not read the Dhātupāṭha: whether
a root is अनुदात्तोपदेश is what the query says.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Tuple

#: Where these twelve stand, between the न्-dropping run and
#: 6.4.46's आर्धधातुके.
NASAL_RUN: Tuple[str, str] = ("6.4.34", "6.4.45")

#: 6.4.37's class, read off the Dhātupāṭha's accent and listed by
#: the vṛtti: **अनुदात्तोपदेशा अनुनासिकान्ता
#: यमिरमिनमिगमिहनिमन्यतयः**.
ANUDATTOPADESA: Tuple[str, ...] = (
    "yam", "ram", "nam", "gam", "han", "man")

#: And the two the sūtra adds to them by name.
AND_TWO_MORE: Tuple[str, ...] = ("van", "tan")

#: 6.4.42's three, which take आ before सन् and before a झल्.
JANA_SANA_KHANA: Tuple[str, ...] = ("jan", "san", "khan")

#: What 6.4.38's व्यवस्थितविभाषा gives the option to, and what it
#: leaves compulsory: **तेन मकारान्तानां विकल्पो भवति, अन्यत्र
#: नित्यमेव लोपः**.
LYAP_OPTIONAL: Tuple[str, ...] = ("yam", "ram", "nam", "gam")


@dataclass(frozen=True)
class Nasal:
    """One rule of 6.4.34–45: what becomes of the stem's nasal."""

    sutra: str
    #: it, śā, ja, anunāsika-lopa, ā, or lopa.
    does: str = ""
    #: The stems the rule names outright.
    of: Tuple[str, ...] = ()
    #: A named class of stem instead.
    gana: str = ""
    #: What must FOLLOW.
    before: Tuple[str, ...] = ()
    #: The further condition on the environment.
    result: Tuple[str, ...] = ()
    excludes: Tuple[str, ...] = ()
    refuses: bool = False
    optional: bool = False
    #: A व्यवस्थितविभाषा: the option holds in named places and not
    #: as the caller pleases.
    vyavasthita: bool = False
    blocks: Tuple[str, ...] = ()
    keeps_out: str = ""
    why: str = ""


NASAL_TABLE: Tuple[Nasal, ...] = (
    Nasal(
        "6.4.34", does="it", of=("śās",), before=("aṅ", "hal"),
        result=("kṅit",),
        keeps_out="शासति, शशासतुः, शशासुः — neither अङ् nor a "
                  "consonant-initial कित् or ङित्",
        why="शास इदङ्हलोः — शास् takes इ in its penult before अङ् "
            "and before a consonant-initial कित् or ङित्: "
            "**अन्वशिषत्, अन्वशिषताम्, अन्वशिषन्** for the अङ्; "
            "**शिष्टः, शिष्टवान्** for the कित्; **आवां शिष्वः, "
            "वयं शिष्मः** for the ङित्. The ष् is 8.3.60's, "
            "**शासिवसिघसीनां च**, and it comes only after the इ "
            "is in.\\n\\n"
            "**AND A VĀRTTIKA ADDS ONE MORE PLACE.** **क्वौ च "
            "शास इत्त्वं भवतीति वक्तव्यम् — आर्यान् शास्तीति "
            "मित्रशीः**"),
    Nasal(
        "6.4.35", does="śā", of=("śās",), before=("hi",),
        why="शा हौ — and before हि, शास् becomes शा outright: "
            "**अनुशाधि, प्रशाधि**.\\n\\n"
            "**AND TWO CONDITIONS ARE DROPPED HERE AND THE "
            "GENITIVE THEN MEANS SOMETHING ELSE.** **उपधाया इति "
            "निवृत्तम्, ततः शास इति स्थानेयोगा षष्ठी भवति** — "
            "with उपधायाः gone, 1.1.49's rule makes शासः mean *in "
            "place of शास्* rather than *of शास्'s penult*. And "
            "**क्ङितीत्येतदपि निवृत्तम्। तेन यदा वा छन्दसि इति "
            "पित्त्वं हिशब्दस्य, तदाप्यादेशो भवत्येव** — so the "
            "substitute holds even where 3.4.88 makes हि पित्"),
    Nasal(
        "6.4.36", does="ja", of=("han",), before=("hi",),
        why="हन्तेर्जः — and हन् becomes ज before हि: **जहि "
            "शत्रून्**. One root, one substitute, and the same "
            "affix the sūtra before named"),
    Nasal(
        "6.4.37", does="anunāsika-lopa", gana="anudāttopadeśa",
        of=AND_TWO_MORE, before=("jhal",), result=("kṅit",),
        why="अनुदात्तोपदेशवनतितनोत्यादीनाम् अनुनासिकलोपो झलि "
            "क्ङिति — a nasal-final root taught with a LOW ACCENT, "
            "and वन् and तन् and their fellows, drop the nasal "
            "before a झल्-initial कित् or ङित्: **यत्वा, यतः, "
            "यतवान्, यतिः; रत्वा, रतः, रतिः; वतिः**.\\n\\n"
            "**AND THE CLASS IS NAMED BY ITS ACCENT AND THEN "
            "LISTED.** **अनुदात्तोपदेशा अनुनासिकान्ता "
            "यमिरमिनमिगमिहनिमन्यतयः** — six roots, gathered not "
            "by how they sound but by the accent they carry where "
            "the Dhātupāṭha teaches them. A class the phonetics "
            "cannot find"),
    Nasal(
        "6.4.38", does="anunāsika-lopa", gana="anudāttopadeśa",
        of=AND_TWO_MORE, before=("lyap",), optional=True,
        vyavasthita=True,
        why="वा ल्यपि — and before ल्यप्, optionally: **प्रयत्य / "
            "प्रयम्य; प्ररत्य / प्ररम्य; प्रणत्य / प्रणम्य; "
            "आगत्य / आगम्य**.\\n\\n"
            "**AND THE OPTION IS SETTLED AND NOT FREE.** "
            "**व्यवस्थितविभाषा चेयम्। तेन मकारान्तानां विकल्पो "
            "भवति, अन्यत्र नित्यमेव लोपः** — only the म्-final "
            "roots have the choice; the rest simply drop, and "
            "**आहत्य, प्रमत्य, प्रवत्य, प्रक्षत्य** have no second "
            "form"),
    Nasal(
        "6.4.39", refuses=True, gana="anudāttopadeśa",
        of=AND_TWO_MORE, before=("ktic",),
        blocks=("6.4.37", "6.4.15"),
        why="न क्तिचि दीर्घश्च — but before क्तिच् neither the "
            "nasal-loss nor a lengthening: **यन्तिः, वन्तिः, "
            "तन्तिः**.\\n\\n"
            "**AND THE SECOND REFUSAL IS THERE BECAUSE THE FIRST "
            "WOULD HAVE LET A THIRD RULE IN.** **अनुनासिकलोपे "
            "प्रतिषिद्धे अनुनासिकस्य क्विझलोः क्ङिति इति दीर्घः "
            "प्राप्नोति, सोऽपि प्रतिषिध्यते** — stop the loss and "
            "the root is still nasal-final, so 6.4.15 reaches it "
            "and lengthens the penult. The word दीर्घश्च is there "
            "to shut that off too. A refusal that has to refuse "
            "twice because refusing once creates the second case"),
    Nasal(
        "6.4.40", does="anunāsika-lopa", of=("gam",),
        before=("kvip",),
        why="गमः क्वौ — गम् drops its nasal before क्विप्: "
            "**अङ्गगत्, कलिङ्गगत्, अध्वगतो हरयः**.\\n\\n"
            "**AND TWO VĀRTTIKAS WIDEN IT IN TWO DIRECTIONS.** "
            "**गमादीनाम् इति वक्तव्यम्। इहापि यथा स्यात् — संयत्, "
            "परीतत्** — गम् and its fellows, so that 6.3.116 can "
            "lean on this for तन् as well; and **ऊ च गमादीनाम् "
            "इति वक्तव्यम् — अग्रेगूः, अग्रेभूः**, a ऊ beside the "
            "loss"),
    Nasal(
        "6.4.41", does="ā", gana="anunāsika-anta",
        before=("viṭ", "van"),
        why="विड्वनोरनुनासिकस्यात् — a nasal-final stem takes आ "
            "before विट् and वनिप्: **अब्जा गोजा ऋतजा अद्रिजाः; "
            "गोषा इन्दो नृषा असि; कूपखाः, शतखाः, सहस्रखाः; "
            "दधिक्राः; अग्रेगा उन्नेतॄणाम्**. The विट् is "
            "3.2.67's, **जनसनखनक्रमगमो विट्**, and the ष् of "
            "गोषाः is 8.3.106's"),
    Nasal(
        "6.4.42", does="ā", of=JANA_SANA_KHANA,
        before=("san", "jhal"), result=("kṅit",),
        keeps_out="जिजनिषति, सिसनिषति, चिखनिषति — the सन् has an "
                  "इट् and no longer begins with a झल्",
        why="जनसनखनां सञ्झलोः — जन्, सन् and खन् take आ before "
            "सन् beginning with a झल्, and before a झल्-initial "
            "कित् or ङित्: **जातः, जातवान्, जातिः; सिषासति, "
            "सातः, सातिः; खातः, खातवान्, खातिः**.\\n\\n"
            "**AND झल् IS CARRIED DOWN TO QUALIFY THE सन् AND NOT "
            "THE OTHER AFFIX.** **झल्ग्रहणं सन्विशेषणार्थं "
            "किमर्थम् अनुवर्त्यते? इह मा भूत् — जिजनिषति** — with "
            "an इट् the सन् begins with इ and is out"),
    Nasal(
        "6.4.43", does="ā", of=JANA_SANA_KHANA, before=("ya",),
        result=("kṅit",), optional=True,
        why="ये विभाषा — and before a य्-initial कित् or ङित्, "
            "optionally: **जायते / जन्यते; जाजायते / जञ्जन्यते; "
            "सायते / सन्यते; खायते / खन्यते**.\\n\\n"
            "**AND ONE OF THE THREE HAS NO OPTION IN ONE PLACE.** "
            "**जनेः श्यनि ज्ञाजनोर्जा इति नित्यं जादेशो भवति** — "
            "before श्यन् 7.3.79 gives जन् a जा outright, so the "
            "option never arises there"),
    Nasal(
        "6.4.44", does="ā", of=("tan",), before=("yak",),
        optional=True,
        keeps_out="तन्तन्यते — a यङ् and not a यक्",
        why="तनोतेर्यकि — and तन् takes आ before यक्, optionally: "
            "**तायते / तन्यते**"),
    Nasal(
        "6.4.45", does="ā", of=("san",), before=("ktic",),
        optional=True,
        why="सनः क्तिचि लोपश्चास्यान्यतरस्याम् — before क्तिच्, "
            "सन् takes आ, and the आ is optionally DROPPED as "
            "well: **सातिः, सन्तिः, सतिः** — three forms from one "
            "sūtra.\\n\\n"
            "**AND अन्यतरस्याम् IS SAID THOUGH विभाषा WAS ALREADY "
            "RUNNING.** **अन्यतरस्यांग्रहणं विस्पष्टार्थम्। ये "
            "संबद्धं हि विभाषाग्रहणम् इह निवृत्तम् इत्याशङ्क्येत** "
            "— 6.4.43's विभाषा was tied to its ये, and one might "
            "have thought it had lapsed. Saying the word again "
            "settles it"),
)


def _reaches(row: Nasal, stem: str, gana: str, before: str,
             result: str) -> bool:
    named = row.of or row.gana
    if named and not (stem in row.of
                      or (row.gana and gana == row.gana)):
        return False
    if row.before and before not in row.before:
        return False
    if row.result and result not in row.result:
        return False
    if row.excludes and (stem in row.excludes
                         or result in row.excludes):
        return False
    return True


def _supplies(row: Nasal, wants: str) -> bool:
    if not wants:
        return True
    return wants == row.does and not row.refuses


def _how_specific(row: Nasal, stem: str, gana: str) -> int:
    """
    A refusal beats what it refuses, and a named stem beats a
    named class.

    6.4.37 and 6.4.40 both drop a nasal from गम्, and the second
    names it where the first has only the accent-class; 6.4.42 and
    6.4.43 both give आ to जन्, and the option is told apart by
    what follows.
    """
    return (
        10 * bool(row.refuses)
        + 6 * bool(row.of and stem in row.of)
        + 4 * bool(row.gana and gana == row.gana)
        + 3 * bool(row.result)
        + 2 * bool(row.before)
    )


@dataclass(frozen=True)
class Became:
    """What the run answers: what the nasal becomes."""

    does: str
    sutra: str
    why: str
    optional: bool = False
    vyavasthita: bool = False
    blocked_by: Tuple[str, ...] = ()


def the_nasal(stem: str = "", *, gana: str = "", before: str = "",
              result: str = "", wants: str = "") -> Became:
    """
    6.4.34–45 — what becomes of the stem's nasal.

    Nothing answers by default: where no rule is reached the nasal
    stays, which is what शासति and तन्तन्यते are.
    """
    matched = [
        row for row in NASAL_TABLE
        if _reaches(row, stem, gana, before, result)
        and _supplies(row, wants)
    ]
    if not matched:
        return Became(
            "", "", "No rule of 6.4.34–45 is reached, so the stem "
                    "keeps its nasal as it is")
    row = max(matched, key=lambda one: _how_specific(one, stem, gana))
    return Became("" if row.refuses else row.does, row.sutra,
                  row.why, optional=row.optional,
                  vyavasthita=row.vyavasthita,
                  blocked_by=row.blocks)


def provisions_for(sutra_id: str) -> Tuple[Nasal, ...]:
    """Every row one sūtra states."""
    return tuple(row for row in NASAL_TABLE if row.sutra == sutra_id)


__all__ = [
    "Nasal", "NASAL_TABLE", "NASAL_RUN", "ANUDATTOPADESA",
    "AND_TWO_MORE", "JANA_SANA_KHANA", "LYAP_OPTIONAL", "Became",
    "the_nasal", "provisions_for",
]
