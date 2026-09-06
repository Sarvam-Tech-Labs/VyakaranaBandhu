# -*- coding: utf-8 -*-
"""
2.4.32 to 2.4.57 — one thing standing in for another.

Two runs, and 2.4.35 divides them. First three rules replace a pronoun
where it is mentioned a SECOND time; then a heading declares that
everything to 2.4.57 holds before an आर्धधातुक affix, and twenty-two
rules replace a ROOT before one:

    2.4.32 इदमोऽन्वादेशेऽशनुदात्तस्तृतीयादौ  इदम् → अ, from the third case
    2.4.33 एतदस्त्रतसोस्त्रतसौ चानुदात्तौ    एतद् → अ, before त्र and तस्
    2.4.34 द्वितीयाटौस्स्वेनः                and both → एनद् before three
    2.4.35 आर्धधातुके                       heading, through 2.4.57
    2.4.36 अदो जग्धिर्ल्यप्ति किति           अद् → जग्धि
    2.4.37 लुङ्सनोर्घस्लृ                    अद् → घस्लृ
    2.4.38 घञपोश्च                          and before these two affixes
    2.4.39 बहुलं छन्दसि                      variously, in the Veda
    2.4.40 लिट्यन्यतरस्याम्                  optionally in the perfect
    2.4.41 वेञो वयिः                        वेञ् → वयि, likewise
    2.4.42 हनो वध लिङि                      हन् → वध
    2.4.43 लुङि च                           and in the aorist
    2.4.44 आत्मनेपदेष्वन्यतरस्याम्           optionally, in the middle
    2.4.45 इणो गा लुङि                      इण् → गा
    2.4.46 णौ गमिरबोधने                     इण् → गमि, not of knowing
    2.4.47 सनि च                            and before सन्
    2.4.48 इङश्च                            इङ् → गमि, before सन् only
    2.4.49 गाङ् लिटि                        इङ् → गाङ्
    2.4.50 विभाषा लुङ्लृङोः                  optionally in two more
    2.4.51 णौ च संश्चङोः                    and before णि with सन् or चङ्
    2.4.52 अस्तेर्भूः                        अस् → भू
    2.4.53 ब्रुवो वचिः                       ब्रू → वचि
    2.4.54 चक्षिङः ख्याञ्                    चक्षिङ् → ख्याञ्
    2.4.55 वा लिटि                          optionally in the perfect
    2.4.56 अजेर्व्यघञपोः                     अज् → वी, but not before two
    2.4.57 वा यौ                            optionally before ल्युट्

**The योगविभाग is the interesting thing in this run, and it is stated
three times.** A योगविभाग is a rule split in two where one would have
served, and each time the vṛtti says what the split buys:

  2.4.43 लुङि च is separated from 2.4.42 so that 2.4.44's option
  reaches the aorist and NOT the benedictive — आत्मनेपदेषु लुङि
  विकल्पो यथा स्याल्लिङि मा भूत्. Written as one rule, वध्यात् would
  have become optional too.

  2.4.47 सनि च is separated from 2.4.46 so that 2.4.48 इङश्च takes only
  सन् and not णि — इङश्चेति सन्येव यथा स्यात्.

  2.4.45 repeats लुङ् though it was already running, and the vṛtti says
  why: लुङीति वर्तमाने पुनर्लुङ्ग्रहणम् 2.4.44 इत्येतद् मा भूत् — so
  that the option 2.4.44 opened does not carry down. इण् → गा is
  obligatory, अगात् and never *अयात्.

Each of the three is a claim about what the table would do if a row
were merged or dropped, so each is held by a test that merges or drops
it and checks the answer changes.

**आर्धधातुक is taken as given, not worked out.** 2.4.35 is a विषयसप्तमी
and not a परसप्तमी — the vṛtti is explicit: तेनार्धधातुकविवक्षायाम्
आदेशेषु कृतेषु पश्चाद् यथाप्राप्तं प्रत्यया भवन्ति, the substitution
happens where an आर्धधातुक is INTENDED, and the affix itself arrives
afterwards. What makes an affix आर्धधातुक is 3.4.114 आर्धधातुकं शेषः,
which is not codified; 3.4.113's सार्वधातुक is, and the complement
could be taken, but taking it here would be codifying 3.4.114 without
registering it. So the condition is passed in, as the kāraka is at
2.3.1, and this note is the record of why.
"""

from dataclasses import dataclass
from typing import Dict, Optional, Tuple

# ---------------------------------------------------------------------------
# The table
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Rule:
    """One substitution: what is replaced, by what, and where."""

    sutra: str
    of: Tuple[str, ...]
    gives: str
    #: The affixes or case-slots this holds before. Empty means the whole
    #: आर्धधातुक field 2.4.35 declares.
    before: Tuple[str, ...] = ()
    #: Affixes it expressly does NOT hold before — 2.4.56's घञ् and अप्.
    not_before: Tuple[str, ...] = ()
    #: A sense it does not hold in — 2.4.46's अबोधने.
    not_sense: str = ""
    #: Whether the row is confined to the middle voice — 2.4.44
    #: आत्मनेपदेषु. Not the पद of 1.4.14, which is a different word.
    atmanepada: bool = False
    optional: bool = False
    bahulam: bool = False
    chandas: bool = False
    #: The accent the substitute carries, where the rule states one.
    accent: str = ""
    #: Facts that must hold — अन्वादेश for the three pronoun rules.
    requires: Tuple[str, ...] = ()
    why: str = ""


#: 2.4.35's heading, and what the vṛtti gives as its extent.
ARDHADHATUKA_FROM, ARDHADHATUKA_THROUGH = "2.4.36", "2.4.57"

#: What may be asserted, and what each assertion means.
FACTS: Dict[str, str] = {
    "anvādeśa": "the thing is being mentioned a SECOND time. आदेशः "
                "कथनम्, अन्वादेशोऽनुकथनम् — and it is not mere later "
                "utterance: एकस्यैवाभिधेयस्य पूर्वं शब्देन प्रतिपादितस्य "
                "द्वितीयं प्रतिपादनम्, the same referent said again. So "
                "देवदत्तं भोजय, इमं च यज्ञदत्तम् is not one (2.4.32)",
    "ārdhadhātuka": "an आर्धधातुक affix is intended. 2.4.35 is a "
                    "विषयसप्तमी, so the substitution happens where one "
                    "is meant and the affix follows after (2.4.35)",
}

RULES: Tuple[Rule, ...] = (
    # --- the pronouns, before 2.4.35's heading begins ------------------
    Rule("2.4.32", ("idam",), "a", before=("3", "4", "5", "6", "7"),
         accent="anudātta", requires=("anvādeśa",),
         why="इदमोऽन्वादेशेऽशनुदात्तस्तृतीयादौ — आभ्यां छात्राभ्यां "
             "रात्रिरधीता, अथो आभ्यामहरप्यधीतम्. तृतीयादौ is the third "
             "case ONWARD, so the first two are untouched. And the "
             "substitute is given as अश् rather than अ "
             "साकच्कार्थम् — so that इमकाभ्याम् is reached too"),
    Rule("2.4.33", ("etad",), "a", before=("tra", "tas"),
         accent="anudātta", requires=("anvādeśa",),
         why="एतदस्त्रतसोस्त्रतसौ चानुदात्तौ — एतस्मिन् ग्रामे सुखं "
             "वसामः, अथोऽत्र युक्ता अधीमहे. 5.3.5 एतदोऽश् gives the "
             "substitute already; पुनर्वचनमनुदात्तार्थम्, this rule is "
             "written for the ACCENT — and the च makes त्र and तस् "
             "unaccented too, so सर्वानुदात्तं पदं भवति"),
    Rule("2.4.34", ("idam", "etad"), "enad", before=("2", "ṭā", "os"),
         accent="anudātta", requires=("anvādeśa",),
         why="द्वितीयाटौस्स्वेनः — इमं छात्रं छन्दोऽध्यापय, अथो एनं "
             "व्याकरणमध्यापय; अनेन … अथो एनेन; अनयोः … अथो एनयोः. "
             "इदम् is carried down मण्डूकप्लुतिन्यायेन, by a frog's "
             "leap over 2.4.33. The vārttika adds एनद् in the neuter "
             "singular: प्रक्षालयैनत्"),

    # --- अद्, five rules -----------------------------------------------
    Rule("2.4.36", ("ad",), "jagdhi", before=("lyap", "kit-t"),
         why="अदो जग्धिर्ल्यप्ति किति — प्रजग्ध्य, जग्धः, जग्धवान्. The "
             "इ of जग्धि is उच्चारणार्थ and not an अनुबन्ध, so no नुम् "
             "follows. तीति किम्? अद्यते. कितीति किम्? अत्तव्यम्. And "
             "the ल्यप् is stated though जग्धि would have come anyway "
             "अन्तरङ्गत्वात् — ज्ञापयत्यन्तरङ्गाणां ल्यपा भवति बाधनम्, "
             "which teaches that ल्यप् defeats inner operations"),
    Rule("2.4.37", ("ad",), "ghasḷ", before=("luṅ", "san"),
         why="लुङ्सनोर्घस्लृ — अघसत्, जिघत्सति. ऌदित्करणमङर्थम्: the ऌ "
             "is marked so that 3.1.55 gives अङ् in the aorist"),
    Rule("2.4.38", ("ad",), "ghasḷ", before=("ghañ", "ap"),
         why="घञपोश्च — घासः, प्रघसः. The अप् is the one 3.3.59 "
             "उपसर्गेऽदः gives"),
    Rule("2.4.39", ("ad",), "ghasḷ", chandas=True, bahulam=True,
         why="बहुलं छन्दसि — घस्तां नूनम्, सग्धिश्च मे; and not in "
             "आत्तामद्य. बहुलम् rather than अन्यतरस्याम् is deliberate: "
             "कार्यान्तरार्थं बहुलग्रहणम्, it carries other effects too "
             "— घस्तामित्यत्रोपधालोपो न भवति"),
    Rule("2.4.40", ("ad",), "ghasḷ", before=("liṭ",), optional=True,
         why="लिट्यन्यतरस्याम् — जघास, जक्षतुः, जक्षुः beside आद, "
             "आदतुः, आदुः"),

    # --- वेञ् ------------------------------------------------------------
    Rule("2.4.41", ("veñ",), "vayi", before=("liṭ",), optional=True,
         why="वेञो वयिः — उवाय, ऊयतुः, ऊयुः, beside ऊवतुः, ऊवुः. "
             "अन्यतरस्याम् is carried down from 2.4.40. The इ is "
             "उच्चारणार्थ"),

    # --- हन्, three rules, and the योगविभाग ------------------------------
    Rule("2.4.42", ("han",), "vadha", before=("liṅ",),
         why="हनो वध लिङि — वध्यात्, वध्यास्ताम्, वध्यासुः. The "
             "substitute ends in अ, and that अ is dropped; being "
             "स्थानिवत् it keeps 7.2.7's वृद्धि away, so अवधीत् and not "
             "*अवाधीत्"),
    Rule("2.4.43", ("han",), "vadha", before=("luṅ",),
         why="लुङि च — अवधीत्, अवधिष्टाम्, अवधिषुः. योगविभाग उत्तरार्थः: "
             "split from 2.4.42 so that the next rule's option reaches "
             "the aorist and not the benedictive — आत्मनेपदेषु लुङि "
             "विकल्पो यथा स्याल्लिङि मा भूत्"),
    Rule("2.4.44", ("han",), "vadha", before=("luṅ",),
         atmanepada=True,
         optional=True,
         why="आत्मनेपदेष्वन्यतरस्याम् — पूर्वेण नित्ये प्राप्ते विकल्प "
             "उच्यते: 2.4.43 had made it obligatory and this makes it a "
             "choice. आवधिष्ट beside आहत"),

    # --- इण् and इङ् ------------------------------------------------------
    Rule("2.4.45", ("iṇ",), "gā", before=("luṅ",),
         why="इणो गा लुङि — अगात्, अगाताम्, अगुः. लुङ् was already "
             "running, and is said again on purpose: पुनर्लुङ्ग्रहणम् "
             "2.4.44 इत्येतद् मा भूत् — so that rule's option does not "
             "carry down. इह त्वविशेषेण नित्यं च भवति. The vārttika "
             "इण्वदिक adds अध्यगात्"),
    Rule("2.4.46", ("iṇ",), "gami", before=("ṇi",), not_sense="bodhana",
         why="णौ गमिरबोधने — गमयति, गमयतः, गमयन्ति. अबोधन इति किम्? "
             "प्रत्याययति — where making someone KNOW is meant, the "
             "substitute does not come"),
    Rule("2.4.47", ("iṇ",), "gami", before=("san",), not_sense="bodhana",
         why="सनि च — जिगमिषति. योगविभाग उत्तरार्थः, split from 2.4.46 "
             "so that इङश्च takes सन् only: इङश्चेति सन्येव यथा स्यात्"),
    Rule("2.4.48", ("iṅ",), "gami", before=("san",),
         why="इङश्च — अधिजिगांसते, अधिजिगांसेते, अधिजिगांसन्ते. Only "
             "सन्, which is what 2.4.47's split was for"),
    Rule("2.4.49", ("iṅ",), "gāṅ", before=("liṭ",),
         why="गाङ् लिटि — अधिजगे, अधिजगाते, अधिजगिरे. The ङ् is an "
             "अनुबन्ध विशेषणार्थम्, so that 1.2.1 गाङ्कुटादिभ्यः reaches "
             "this substitute: नहि स्थानिवद्भावेन गाङिति रूपं लभ्यते — "
             "being स्थानिवत् would not have supplied the ङ्"),
    Rule("2.4.50", ("iṅ",), "gāṅ", before=("luṅ", "lṛṅ"), optional=True,
         why="विभाषा लुङ्लृङोः — अध्यगीष्ट beside अध्यैष्ट, अध्यगीष्यत "
             "beside अध्यैष्यत. On the substitution side 1.2.1 makes it "
             "ङित् and 6.4.66 gives the ई"),
    Rule("2.4.51", ("iṅ",), "gāṅ", before=("ṇi-san", "ṇi-caṅ"),
         optional=True,
         why="णौ च संश्चङोः — अधिजिगापयिषति beside अध्यापिपयिषति, "
             "अध्यजीगपत् beside अध्यापिपत्. णौ is a परसप्तमी with "
             "respect to इङ् and संश्चङोः with respect to णि, so the "
             "order is root, णि, then सन् or चङ्"),

    # --- four roots replaced through the whole heading ------------------
    Rule("2.4.52", ("as",), "bhū",
         why="अस्तेर्भूः — भविता, भवितुम्, भवितव्यम्. It does not reach "
             "the perfect periphrastic ईहामास, because 3.1.40 "
             "कृञ्चानुप्रयुज्यते लिटि names अस् through a प्रत्याहार and "
             "would be pointless if भू replaced it there"),
    Rule("2.4.53", ("brū",), "vaci",
         why="ब्रुवो वचिः — वक्ता, वक्तुम्, वक्तव्यम्. Being स्थानिवत् "
             "it keeps ब्रू's middle where the fruit falls to the agent: "
             "ऊचे. The इ is उच्चारणार्थ"),
    Rule("2.4.54", ("cakṣiṅ",), "khyāñ",
         why="चक्षिङः ख्याञ् — आख्याता, आख्यातुम्, आख्यातव्यम्. The ञ् "
             "is marked on purpose, so the substitute does NOT keep "
             "चक्षिङ्'s obligatory middle: आख्यास्यति beside आख्यास्यते. "
             "Vārttikas add क्शादि (आक्शाता), and withhold it in the "
             "sense of avoiding — दुर्जनाः संचक्ष्याः"),
    Rule("2.4.55", ("cakṣiṅ",), "khyāñ", before=("liṭ",), optional=True,
         why="वा लिटि — पूर्वेण नित्ये प्राप्ते विकल्प उच्यते: आचख्यौ "
             "beside आचचक्षे"),
    Rule("2.4.56", ("aj",), "vī", not_before=("ghañ", "ap"),
         why="अजेर्व्यघञपोः — प्रवायकः, प्रवयणीयः. अघञपोरिति किम्? "
             "समाजः, उदाजः — and beside them समजः, उदजः by 3.3.69. The "
             "substitute is given LONG, वी: दीर्घोच्चारणं किम्? "
             "प्रवीताः. A vārttika adds क्यप् to the exclusion, समज्या"),
    Rule("2.4.57", ("aj",), "vī", before=("lyuṭ",), optional=True,
         why="वा यौ — यु stands for ल्युट्. प्रवयणो दण्डः beside "
             "प्राजनो दण्डः, प्रवयणमानय beside प्राजनमानय"),
)


# ---------------------------------------------------------------------------
# What the question answers with
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Replaced:
    """That something stands in, and by which rule."""

    of: str
    gives: str
    by: str
    why: str
    optional: bool = False
    bahulam: bool = False
    accent: str = ""


@dataclass(frozen=True)
class Kept:
    """
    That nothing stands in.

    ``by`` is empty: no rule of this run REFUSES a substitution, they
    simply do not reach one, and a rule that did not act must not be
    reported as though it had.
    """

    of: str
    why: str
    by: str = ""
    gives: str = ""


def rules_for(sutra_id: str) -> Tuple[Rule, ...]:
    """Every row a sūtra states. 2.4.34 and the rest state one each."""
    return tuple(r for r in RULES if r.sutra == sutra_id)


def in_the_heading(sutra_id: str) -> bool:
    """
    Whether 2.4.35's आर्धधातुके reaches this sūtra.

    आर्धधातुक इत्यधिकारोऽयम् ण्यक्षत्रियार्षञितः इति यावत् — the vṛtti
    gives the extent as running up to 2.4.58, so the last rule it
    governs is 2.4.57.
    """
    def order(sid: str) -> Tuple[int, ...]:
        return tuple(int(p) for p in sid.split("."))

    return (order(ARDHADHATUKA_FROM) <= order(sutra_id)
            <= order(ARDHADHATUKA_THROUGH))


def substitute(
    of: str,
    *,
    before: str = "",
    before_vibhakti: Optional[int] = None,
    sense: str = "",
    atmanepada: bool = False,
    given: Tuple[str, ...] = (),
    chandas: bool = False,
) -> object:
    """
    What stands in for this root or pronoun — 2.4.32 to 2.4.57.

    The rows are tried in the text's own order and the LAST match wins,
    which is 1.4.2 विप्रतिषेधे परं कार्यम् doing its work: 2.4.44 is
    written to make optional what 2.4.43 had made obligatory, and 2.4.55
    and 2.4.57 do the same to 2.4.54 and 2.4.56. Taking the first match
    would give the obligatory answer in all three places and the option
    would never be reachable.
    """
    for fact in given:
        if fact not in FACTS:
            raise ValueError(
                f"{fact!r} is not a fact this run knows. Known: "
                f"{', '.join(sorted(FACTS))}")

    slot = before or (str(before_vibhakti)
                      if before_vibhakti is not None else "")
    found: Optional[Rule] = None
    for rule in RULES:
        if of not in rule.of:
            continue
        if rule.requires and not all(f in given for f in rule.requires):
            continue
        if rule.chandas and not chandas:
            continue
        if rule.not_sense and sense == rule.not_sense:
            continue
        if rule.atmanepada and not atmanepada:
            continue
        if slot and slot in rule.not_before:
            continue
        if rule.before and slot not in rule.before:
            continue
        if in_the_heading(rule.sutra) and "ārdhadhātuka" not in given:
            continue
        found = rule
    if found is None:
        return Kept(
            of,
            f"No rule of 2.4.32 to 2.4.57 replaces {of} here"
            + (f" before {slot}" if slot else "")
            + (". Everything from 2.4.36 needs आर्धधातुक to be asserted, "
               "since 2.4.35 is a विषयसप्तमी and the affix is not yet "
               "there to be inspected"
               if "ārdhadhātuka" not in given else ""),
        )
    return Replaced(of, found.gives, found.sutra, found.why,
                    optional=found.optional, bahulam=found.bahulam,
                    accent=found.accent)
