# -*- coding: utf-8 -*-
"""
Aṣṭādhyāyī 1.3 — the it-saṃjñā, 1.3.2 to 1.3.9.

Eight sūtras that between them decide which letters of an enunciated form are
indicatory and then throw them away. Implemented in src/astadhyayi/itsamjna.py
as one analysis, because they constrain one another: 1.3.4 exists only to stop
1.3.3, 1.3.5 has to be tried before 1.3.7 or ñ would be taken singly, and 1.3.9
has to drop whole marks rather than last sounds, which is a decision about
1.1.52.

Codifying these discharges a limitation recorded against 1.1.55: whether a
substitute is śit or ṅit no longer has to be asserted by the caller.
"""

from __future__ import annotations

from src.astadhyayi.itsamjna import (
    analyze,
    its_of,
    lopa,
    stem_of,
    strip_its,
)
from src.astadhyayi.atmanepada import PROVISIONS, pada_of_usage
from src.astadhyayi.pada import pada_of
from src.astadhyayi.reading import adhikara, yathasamkhya
from src.astadhyayi.samjna import is_dhatu
from src.astadhyayi.sources import register


register(
    "1.3.2",
    reuses=('1.3.9',),
    samjna="it",
    apply=analyze,
    codification=(
        "The anunāsika-vowel branch of itsamjna.analyze. The mark is a "
        "combining candrabindu, the same character varna.nasalize produces, so "
        "1.1.8's test answers the question."
    ),
    related=("1.1.8", "1.3.3", "1.3.9", "7.2.16"),
    notes=(
        "SETTLED — what उपदेश means: उपदिश्यतेऽनेनेत्युपदेशः शास्त्रवाक्यानि,\n"
        "  सूत्रपाठः खिलपाठश्च — the enunciated statements, the sūtrapāṭha and\n"
        "  the appended lists. Outside it there are no it-letters, and the\n"
        "  Kāśikā's counter-example is a Vedic अभ्र आँ अपः where a nasal vowel\n"
        "  is simply a nasal vowel. This is why `analyze` takes a Context that\n"
        "  cannot express 'not an upadeśa': calling it at all is the claim.\n"
        "\n"
        "SETTLED — the nasality is not written. प्रतिज्ञानुनासिक्याः पाणिनीयाः,\n"
        "  the Pāṇinīyas hold it by declaration: the sūtrapāṭha does not mark\n"
        "  these vowels and the tradition simply knows which they are. The\n"
        "  dhātupāṭha does mark them, and that is where this rule can actually\n"
        "  be run — Vidyut's file writes the candrabindu as SLP1 `~`. The\n"
        "  Kāśikā's two examples, एध and स्पर्ध, are entries 01.0002 and\n"
        "  01.0003 of it, and both come out right.\n"
        "\n"
        "SETTLED — why अच् and why अनुनासिक: अजिति किम्? 3.2.74; अनुनासिक इति\n"
        "  किम्? सर्वस्याचो मा भूत् — without it every vowel would be it."
    ),
)


register(
    "1.3.3",
    apply=analyze,
    codification=(
        "The final-consonant branch. `scan_phonemes` decides what the final "
        "sound is, so a digraph is not split."
    ),
    related=("1.1.71", "1.3.2", "1.3.4", "1.3.9"),
    notes=(
        "SETTLED — this is the rule that makes the śivasūtras work. The Kāśikā\n"
        "  lists them as its examples: अइउण् — णकारः, ऋऌक् — ककारः,\n"
        "  एओङ् — ङकारः, ऐऔच् — चकारः. src/astadhyayi/sivasutra.py already\n"
        "  strips those finals in order to resolve pratyāhāras, so 1.3.3 was in\n"
        "  effect codified before it was written down; this entry names the\n"
        "  sūtra that licenses it.\n"
        "\n"
        "SETTLED — उपदेश is carried down from 1.3.2 by anuvṛtti, which the\n"
        "  corpus records, and it is doing work: अग्निचित्, सोमसुत् end in\n"
        "  consonants and keep them, being words and not enunciations.\n"
        "\n"
        "SETTLED — the circularity, and how the tradition escapes it. हल् in\n"
        "  this sūtra is itself a pratyāhāra, whose formation needs the l of\n"
        "  हल् to be an it, which needs this sūtra. The Kāśikā's answer is that\n"
        "  the second हल्ग्रहण in the śivasūtra list is तन्त्रेण, taken as one\n"
        "  utterance serving twice: तेन प्रत्याहारपाठे हलित्यत्र लकारस्येत्संज्ञा\n"
        "  क्रियते, तथा च सति हलन्त्यम् इत्यत्र प्रत्याहारे नेतरेतराश्रयदोषो\n"
        "  भवति. Worth recording because the code has the same shape: the\n"
        "  śivasūtra module strips finals by a hardcoded convention rather than\n"
        "  by calling this rule, and that is not a shortcut but the tradition's\n"
        "  own resolution."
    ),
)


register(
    "1.3.4",
    apply=analyze,
    codification=(
        "The prohibition inside the final-consonant branch: in a vibhakti, a "
        "final t-varga, s or m is passed over. TUSMA is built from the varga "
        "table, so tu is the five dentals and not the letter t."
    ),
    related=("1.3.3", "3.4.78", "3.4.101", "4.1.2", "7.1.12"),
    notes=(
        "SETTLED — it is a निषेध on 1.3.3 and nothing else: पूर्वेण प्राप्तायाम्\n"
        "  इत्संज्ञायां विभक्तौ वर्तमानानां तवर्गसकारमकाराणां प्रतिषेध उच्यते.\n"
        "  So it is coded as a guard inside that branch rather than as a rule of\n"
        "  its own, which is what it is.\n"
        "\n"
        "SETTLED — तुस्माः is तु + स् + म्, the t-varga plus s plus m, one of\n"
        "  the places where reading तु as the single letter t would quietly lose\n"
        "  four sounds. The Kāśikā gives an example for each part: टाङसिङसाम्\n"
        "  (7.1.12) for the t-varga, जस् (4.1.2) for s, अपचताम् (3.4.101) for m.\n"
        "\n"
        "SETTLED — जस् is the case that shows the two rules at once. Its j is\n"
        "  indicatory by 1.3.7 and its s is protected by this sūtra, so जस्\n"
        "  yields अस् and ब्राह्मण + अस् gives ब्राह्मणाः. Get either half wrong\n"
        "  and the nominative plural disappears.\n"
        "\n"
        "SETTLED — विभक्ताविति किम्? The Kāśikā's answer is a list of\n"
        "  non-vibhakti affixes whose t, s and m ARE indicatory: यत् (3.1.97),\n"
        "  युस् (5.2.123), श्नम् (3.1.78), अत् (5.3.12). All four are tests here."
    ),
)


register(
    "1.3.5",
    apply=analyze,
    codification=(
        "The two-letter openings ñi, ṭu, ḍu, tried before the single-letter "
        "ādi rules. Each is claimed entire so that 1.3.9 removes both letters."
    ),
    related=("1.1.52", "1.3.7", "1.3.9"),
    notes=(
        "SETTLED — these are pairs, not letters: ञि टु डु इत्येतेषां समुदायानाम्\n"
        "  आदितो वर्तमानानामित्संज्ञा भवति. Two consequences follow, and both\n"
        "  are structural. It must be tried before 1.3.7, or the ñ of ञिमिदा\n"
        "  would be taken alone as a c-varga letter; and 1.3.9 must remove the\n"
        "  pair, which is exactly why that sūtra says तस्य.\n"
        "\n"
        "SETTLED — it is not restricted to affixes, unlike 1.3.6 to 1.3.8: the\n"
        "  Kāśikā's examples are all roots, ञिमिदा, टुवेपृ, डुपचष्, डुकृञ्, and\n"
        "  every one of them is in the local dhātupāṭha to test against."
    ),
)


register(
    "1.3.6",
    apply=analyze,
    codification="The initial-ṣ branch, conditioned on the form being an affix.",
    related=("1.3.5", "1.3.7", "3.1.145"),
    notes=(
        "SETTLED — प्रत्ययस्य is doing work, and the Kāśikā shows it twice over.\n"
        "  प्रत्ययस्येति किम्? षोडः, षण्डः, षडिकः — words beginning with ṣ that\n"
        "  are not affixes keep it. आदिरित्येव — अविषः, महिषः, where a ṣ that is\n"
        "  not initial keeps its place. Its own example is ष्वुन् (3.1.145),\n"
        "  giving नर्त्तकी."
    ),
)


register(
    "1.3.7",
    apply=analyze,
    codification=(
        "The initial c-varga / ṭ-varga branch for affixes. CUTU is built from "
        "the varga table, so चुटू is ten letters and not two."
    ),
    related=("1.1.69", "1.3.5", "1.3.6", "4.1.2"),
    notes=(
        "SETTLED — चुटू is two udit terms, so by 1.1.69 each stands for its\n"
        "  whole varga: चवर्गटवर्गौ प्रत्ययस्यादी इत्संज्ञौ भवतः. This sūtra is\n"
        "  the Kāśikā's own illustration of udit under 1.1.69, so the two are\n"
        "  codified against each other — CUTU is assembled from the varga table\n"
        "  rather than typed as ten letters.\n"
        "\n"
        "SETTLED — the Kāśikā walks the whole of both vargas: च्फञ् (4.1.98),\n"
        "  ज् in जस् (4.1.2), ञ्य (4.3.92), ट (3.2.16), ड (3.2.97), and it notes\n"
        "  in passing that छ, झ, ठ, ढ get substitutes elsewhere (7.1.2, 7.1.3,\n"
        "  7.3.50) rather than appearing as affix-initials."
    ),
)


register(
    "1.3.8",
    apply=analyze,
    codification=(
        "The initial l / ś / k-varga branch, suppressed for taddhitas. LASAKU "
        "is likewise assembled from the varga table."
    ),
    related=("1.1.26", "1.3.6", "1.3.7", "3.1.68", "3.3.115"),
    notes=(
        "SETTLED — अतद्धिते is a real exclusion and not decoration: a taddhita\n"
        "  beginning with one of these keeps it. The rule reaches the commonest\n"
        "  affixes in the grammar — शप् (3.1.68) giving भवति, ल्युट् (3.3.115)\n"
        "  giving चयनम्, क्त and क्तवतु (1.1.26) giving भुक्तः and भुक्तवान्,\n"
        "  खच् (3.2.38) giving प्रियंवदः, घुरच् (3.2.161) giving भङ्गुरम्.\n"
        "\n"
        "SETTLED — कु again stands for the whole varga, so घ and ख are covered;\n"
        "  ग्स्नु (3.2.139) and घुरच् are the Kāśikā's demonstrations of that."
    ),
)


register(
    "1.3.9",
    reuses=('1.3.2',),
    apply=strip_its,
    codification=(
        "lopa(form, marks) -> the form with every marked span removed entire. "
        "Called at the end of analyze, so Upadesa.stem is already the result."
    ),
    related=("1.1.52", "1.1.60", "1.3.2", "1.3.5"),
    notes=(
        "SETTLED — तस्य is in the sūtra to defeat 1.1.52, and the Kāśikā says so\n"
        "  in one line: \"तस्य\"ग्रहणं सर्वलोपार्थम्। अलोऽन्त्यस्य मा भूत् —\n"
        "  आदिर्ञिटुडवः इति. Without it, अलोऽन्त्यस्य would cut each elision down\n"
        "  to the last sound and ञि would lose only its i. So this is a codified\n"
        "  interaction with a paribhāṣā already implemented, not a free-standing\n"
        "  deletion, and the code removes whole marked spans for that reason.\n"
        "\n"
        "SCOPE — what the it-rules do NOT remove: the vowel that makes a\n"
        "  consonant-final anubandha pronounceable. डुपचष् comes out पच अfter\n"
        "  ḍu and ṣ are dropped, where the root is पच्, and आनङ् comes out आन\n"
        "  where the substitute is आन्. That last a is उच्चारणार्थ, added for\n"
        "  utterance and belonging to no rule codified here. It is left in place\n"
        "  rather than stripped by a guess, because a rule that removed a final\n"
        "  a on suspicion would be wrong wherever the a is real."
    ),
)


register(
    "1.3.1",
    reuses=('1.3.2',),
    samjna="dhātu",
    apply=is_dhatu,
    codification=(
        "is_dhatu(form) -> bool, over the dhātupāṭha. Matched on the "
        "enunciated form or on its it-stripped stem, so डुकृञ् and कृ are the "
        "same root asked for two ways."
    ),
    related=("1.3.2", "1.3.3", "3.1.32", "3.1.91"),
    notes=(
        "SETTLED — the list is another text, and it is on disk. भू इत्येवमादयः\n"
        "  शब्दाः क्रियावचना धातुसंज्ञा भवन्ति, and the Kāśikā's first three\n"
        "  examples are entries 1, 2 and 3 of the dhātupāṭha: भू giving भवति,\n"
        "  एध giving एधते, स्पर्ध giving स्पर्धते. 2,259 roots, none typed here.\n"
        "\n"
        "SETTLED — धातु is not Pāṇini's coinage: धातुशब्दः पूर्वाचार्यसंज्ञा, it\n"
        "  is an earlier teachers' term, and he takes it over along with what it\n"
        "  covered — ते च क्रियावचनानां संज्ञां कृतवन्तः. That is why the sūtra\n"
        "  enumerates rather than defines.\n"
        "\n"
        "SETTLED — the व of भ्वादि has been read two ways and the Kāśikā\n"
        "  gives both in a verse: भूवादीनां वकारोऽयं मङ्गलार्थः प्रयुज्यते।\n"
        "  भुवो वार्थं वदन्तीति भ्वर्था वा वादयः स्मृताः — either it is there for\n"
        "  auspiciousness, or वादि means 'those expressing the sense of भू'.\n"
        "  The corpus's padaccheda splits भू-वा-आदयः, which is the second\n"
        "  reading. Nothing here turns on the choice.\n"
        "\n"
        "SCOPE — क्रियावाचिनाम् एव, only those denoting action. A semantic\n"
        "  condition, and not applied: the dhātupāṭha's entries are roots and are\n"
        "  admitted as such.\n"
        "\n"
        "  Nor does this sūtra reach the derived roots. 3.1.32 सनाद्यन्ता धातवः\n"
        "  makes a stem in सन्, क्यच् and the rest a root too, and that is a\n"
        "  separate provision not codified yet — so is_dhatu answers for the\n"
        "  enumerated roots only."
    ),
)

register(
    "1.3.10",
    apply=yathasamkhya,
    codification=(
        "yathasamkhya(first, second) -> the ordered pairing, or None when the "
        "lists differ in length. Returning None rather than a truncated zip is "
        "the point: a silent zip would drop members and look right."
    ),
    related=("1.4.90", "4.3.94"),
    notes=(
        "SETTLED — संख्या here means ORDER, not quantity:\n"
        "  संख्याशब्देनात्र क्रमो लक्ष्यते। यथासंख्यं यथाक्रमम्. And then the\n"
        "  pairing is stated plainly — प्रथमात् प्रथमः, द्वितीयाद् द्वितीयः.\n"
        "\n"
        "SETTLED — the condition is threefold and the Kāśikā states all three:\n"
        "  समानां समसंख्यानां समं परिपठितानाम् — of equal number, equally\n"
        "  enumerated. 4.3.94 तूदीशलातुरवर्मतीकूचवाराड् ढक्छण्ढञ्यकः names four\n"
        "  places and four affixes, so they pair off: तौदेयः, शालातुरीयः,\n"
        "  वार्मतेयः, कौचवार्यः.\n"
        "\n"
        "SETTLED — समानामिति किम्? 1.4.90 लक्षणेत्थंभूताख्यानभागवीप्सासु\n"
        "  प्रतिपर्यनवः has five senses against three words. Unequal, so no\n"
        "  respective pairing and each word holds for any of the senses. This is\n"
        "  the case the codification has to get right, and it is why the function\n"
        "  refuses rather than truncates."
    ),
)


register(
    "1.3.11",
    samjna="adhikāra",
    apply=adhikara,
    codification=(
        "adhikara(sutra_id) -> the heading and how far it reaches, and "
        "governs() for the sūtras under it. The scope comes from the corpus, "
        "because the mark the sūtra names is not written."
    ),
    related=("1.2.31", "3.1.1", "3.1.91", "4.1.1", "6.4.1", "8.1.16"),
    notes=(
        "SETTLED — the mark is a svarita, and 1.2.31 has already named it:\n"
        "  स्वरितो नाम स्वरविशेषो वर्णधर्मः। तेन चिह्नेनाधिकारो वेदितव्यः.\n"
        "  अधिकारः = विनियोगः, and the word so marked stands over what follows —\n"
        "  अधिकृतत्वाद् उत्तरत्रोपतिष्ठते.\n"
        "\n"
        "SETTLED — and it is not written. प्रतिज्ञास्वरिताः पाणिनीयाः, the\n"
        "  Pāṇinīyas hold the svarita by declaration, exactly as they hold the\n"
        "  anunāsika of 1.3.2. So the mark cannot be read off the text and the\n"
        "  scope has to come from the tradition — which the corpus carries, with\n"
        "  a type and an end for each heading.\n"
        "\n"
        "SETTLED — the Kāśikā names six, and the corpus independently marks all\n"
        "  six with their ends: 3.1.91 धातोः to 3.4.117, 4.1.1 ङ्याप्प्रातिपदिकात्\n"
        "  to 5.4.160, 6.4.1 अङ्गस्य to 7.4.97, 6.4.129 भस्य to 6.4.175,\n"
        "  8.1.16 पदस्य to 8.3.55. Two texts agreeing on six headings is a check\n"
        "  on the scope data, which 3,498 sūtras depend on.\n"
        "\n"
        "OPEN — 3.1.1 प्रत्ययः is the sixth the Kāśikā names, and the corpus types\n"
        "  it प्रत्ययसंज्ञा with no scope-end. It is plainly both: it gives the\n"
        "  name pratyaya AND governs what follows. Whether the missing end is a\n"
        "  gap in the data or a considered position is not settled here, and\n"
        "  `adhikara` admits it on the type alone."
    ),
)


register(
    "1.3.12",
    reuses=('1.3.3',),
    apply=pada_of,
    codification=(
        "pada_of(root, ...) -> which set of endings, and why. The two marks "
        "are read from the dhātupāṭha through 1.2.30's accent and 1.3.3's "
        "final consonant, so no list of roots is written here."
    ),
    related=("1.2.30", "1.3.3", "1.3.13", "1.3.72"),
    notes=(
        "SETTLED — it is a नियम and not a grant, and the Kāśikā says so before\n"
        "  anything else: अविशेषेण धातोरात्मनेपदं परस्मैपदं च विधास्यते,\n"
        "  तत्रायं नियमः क्रियते — both sets are prescribed for a root without\n"
        "  distinction, and this narrows it. तेभ्य एवात्मनेपदं भवति नान्येभ्यः:\n"
        "  from those alone, and from no others. So a root with neither mark\n"
        "  takes the other set, which is what the codification returns.\n"
        "\n"
        "SETTLED — this is where two earlier blocks meet, and neither had to be\n"
        "  written twice. The anudātta mark is 1.2.30's, and the dhātupāṭha is the\n"
        "  only text that writes it — 404 of its 2,259 entries carry it. The ṅ is\n"
        "  found by 1.3.3, and 55 carry that. Between them 458 qualify, and the\n"
        "  list is read rather than typed.\n"
        "\n"
        "  That count was wrong at first, by 263 entries, because the mark was\n"
        "  read without its position. The dhātupāṭha accents roots and their\n"
        "  it-letters with the same two signs, and only the one on the it is\n"
        "  indicatory: आसँ is written `Asa~` with the anudātta after the\n"
        "  anunāsika it, and gives आस्ते; विँशँ is `viSa~` with the anudātta on\n"
        "  the root's own vowel, and gives विशति. Read flat the two are the same\n"
        "  root, and then विशति comes out ātmanepada and 1.3.17 नेर्विशः has\n"
        "  nothing left to do — as do 1.3.29 for गम् and श्रु and 1.3.18 for\n"
        "  क्रीञ्, all of which carry an anudātta somewhere and none of which is\n"
        "  अनुदात्तेत्. The Kāśikā says as much at 1.3.17, opening with\n"
        "  शेषात्कर्तरि परस्मैपदम् इति परस्मैपदे प्राप्ते — the active would\n"
        "  otherwise obtain.\n"
        "\n"
        "  All four of the Kāśikā's examples check out against the file: आस् and\n"
        "  वस् are entries 02.0011 and 02.0013, both anudātta, giving आस्ते and\n"
        "  वस्ते; षूङ् and शीङ् are 02.0025 and 02.0026, both ṅit, giving सूते\n"
        "  and शेते. Its numbering is the continuous one — 1021, 1023, 1031,\n"
        "  1032 — where Vidyut's is gaṇa-and-serial, but the gaps match."
    ),
)


register(
    "1.3.13",
    apply=pada_of,
    codification="The bhāva/karman branch, which does not consult the root's marks.",
    related=("1.3.12", "3.4.69"),
    notes=(
        "SETTLED — it overrides the restriction rather than qualifying it. Where\n"
        "  the lakāra is prescribed in the sense of the action itself or of the\n"
        "  object — 3.4.69 लः कर्मणि च भावे चाकर्मकेभ्यः — the endings are\n"
        "  ātmanepada whatever the root is marked with. भावे: ग्लायते भवता,\n"
        "  सुप्यते भवता, आस्यते भवता. कर्मणि: क्रियते कटः, ह्रियते भारः.\n"
        "  So it is tested before 1.3.12 and not after.\n"
        "\n"
        "SETTLED — कर्मकर्तरि is the case that looks like an exception and is\n"
        "  not: लूयते केदारः स्वयमेव — the field mows itself — and परस्मैपदं न\n"
        "  भवति even so. The Kāśikā explains that the second कर्तृग्रहण of 3.4.69\n"
        "  carries over, so parasmaipada belongs only where the agent is an agent\n"
        "  proper. Carried as a flag that records the case was considered."
    ),
)


# --- 1.3.14 to 1.3.93: which endings a verb takes -------------------------
#
# Eighty sūtras, and not eighty functions. Their conditions live once, in
# `atmanepada.PROVISIONS`, because that is where the resolver reads them; a
# second copy here as eighty hand-written `apply` callables would be the same
# information twice, and the two would drift. So the registration is generated
# from the table, and each record's codification line is the table's own
# rendering of what the sūtra tests.
#
# What is written by hand is the part no table holds: the notes. Most sūtras
# in this block are lexical — a root, an upasarga, a sense — and for those the
# note records the Kāśikā's worked form and, where it gives one, its
# counter-example, which is the evidence that the conditions were read off a
# source rather than guessed. The ones carrying real interpretation have notes
# written out in full below.

#: Carried by the two sūtras that frame the block — 1.3.14, where the
#: conditioned grants begin, and 1.3.78, where the remainder falls. It is true
#: of every sūtra between them, but attaching it to all eighty would flag two
#: records in five as having something outstanding, and a flag that common
#: says nothing. Each record's codification line already names the conditions
#: it takes as inputs, which is the per-sūtra form of the same statement.
_GIVEN = (
    "SCOPE — through this whole block, sense and transitivity are given and "
    "not computed. A rule such as 1.3.25 उपान्मन्त्रकरणे turns on what the "
    "speaker means, and no reading of the form will settle it; so the "
    "condition is an input, and where it is not stated the rule does not "
    "fire. `near_misses` reports which condition was wanting, rather than "
    "leaving a reader to wonder whether the rule was considered at all."
)

_NOTES = {
    "1.3.14": (
        "SETTLED — कर्मशब्दः क्रियावाची: the कर्मन् here is the action, not the "
        "object. व्यतिहारो विनिमयः — an exchange: यत्रान्यसंबन्धिनीं क्रियामन्यः "
        "करोति, इतरसंबन्धिनीं चेतरः, where each does to the other what belongs "
        "to the other to do. व्यतिलुनते, व्यतिपुनते; without it, लुनन्ति.\n\n"
        "SETTLED — the कर्तृग्रहण is not for this sūtra at all. The Kāśikā says "
        "so plainly — कर्तृग्रहणमुत्तरार्थम् — it is placed here so that 1.3.78 "
        "can read it down sixty-four sūtras later. That is why पच्यत ओदनः "
        "स्वयमेव keeps the middle endings: the second कर्तृग्रहण reaches it, and "
        "कर्मकर्तरि is not कर्तरि."
    ),
    "1.3.15": (
        "SETTLED — and the roots are not listed anywhere. The sūtra names them "
        "by sense, गत्यर्थेभ्यो हिंसार्थेभ्यश्च, and the dhātupāṭha writes the "
        "sense of every root it teaches: 321 are गत्यर्थ and 157 हिंसार्थ, read "
        "off the file. गम् is `gatO` and सृप् is `gatO`, which is व्यतिगच्छन्ति "
        "and व्यतिसर्पन्ति; हन् is `hiMsAgatyoH` and so falls under both, which "
        "is व्यतिघ्नन्ति. लू is `Cedane` and पू is `pavane`, neither, so "
        "व्यतिलुनते and व्यतिपुनते keep what 1.3.14 gave them.\n\n"
        "SETTLED — the first vārttika does real work and can be shown to. "
        "हसादीनामुपसंख्यानम् adds हस्, जल्प् and पठ् to the prohibition, and by "
        "the file's own glosses none of the three is गत्यर्थ or हिंसार्थ — हस् is "
        "`hasane`, जल्प् and पठ् are `vyaktAyAM vAci`. So the sūtra alone would "
        "not reach them and व्यतिहसन्ति would come out wrong.\n\n"
        "SETTLED — the second, हरतेरप्रतिषेधः, is confirmatory rather than "
        "corrective on this data: हृ is `haraRe` and `prasahyakaraRe`, so the "
        "prohibition never reached it and संप्रहरन्ते राजानः stands either way. "
        "The vārttika is guarding against a reading of हृ as गत्यर्थ that this "
        "recension does not have."
    ),
    "1.3.16": (
        "SETTLED — a prohibition on the ground of redundancy. Where इतरेतर, "
        "अन्योन्य or (by the vārttika) परस्पर already says the reciprocity, the "
        "middle endings have nothing left to mark: इतरेतरस्य व्यतिलुनन्ति."
    ),
    "1.3.17": (
        "SETTLED — नेरुपसर्गस्य ग्रहणम्, by अर्थवद्ग्रहणे नानर्थकस्य ग्रहणम्. It is "
        "the upasarga नि that is meant, not the syllable: मधुनि विशन्ति भ्रमराः "
        "is untouched. And an intervening augment does not break the "
        "adjacency — यदागमास्तद्ग्रहणेन गृह्यन्ते — so न्यविशत keeps it.\n\n"
        "SETTLED — विश् is not अनुदात्तेत्, though the dhātupāṭha writes an "
        "anudātta over it. The mark sits on the root's own vowel (`vi\\Sa~`), "
        "not on the it, so 1.3.12 does not reach it and this sūtra has work to "
        "do. The Kāśikā says as much in its first words: शेषात्कर्तरि "
        "परस्मैपदम् इति परस्मैपदे प्राप्ते."
    ),
    "1.3.18": (
        "SETTLED — अकर्त्रभिप्रायार्थोऽयमारम्भः, and this is the first of "
        "thirteen sūtras in the pāda that the Kāśikā introduces with that "
        "phrase. डुक्रीञ् is ñit, so 1.3.72 already gives it ātmanepada wherever "
        "the fruit reaches the agent; the sūtra exists for the case where it "
        "does not. The mark is checkable: `qukrIY` has ञ् as its final it.\n\n"
        "SETTLED — पर्यादय उपसर्गा गृह्यन्ते, so बहुवि क्रीणाति वनम् is outside."
    ),
    "1.3.19": (
        "SETTLED — विपराशब्दावुपसर्गौ गृह्येते, साहचर्यात्. The two are read as "
        "upasargas because they keep company as such, so बहुवि जयति वनम् and "
        "परा जयति सेना are outside."
    ),
    "1.3.20": (
        "SETTLED — अनास्यविहरणे is a negative condition and so does not need "
        "the sense to be stated: विद्यामादत्ते, but आस्यं व्याददाति.\n\n"
        "SCOPE — two vārttikas extend it and neither is codified. "
        "आस्यविहरणसमानक्रियादपि प्रतिषेधो वक्तव्यः reaches विपादिकां व्याददाति, "
        "and स्वाङ्गकर्मकाच्च reaches व्याददते पिपीलिकाः. Both turn on the object "
        "being one's own limb, which is not modelled."
    ),
    "1.3.21": (
        "SETTLED — आङः carries down from 1.3.20, so the upasargas are four: "
        "आ, अनु, सम्, परि. समासाहचर्याद् अन्वादिरुपसर्गो गृह्यते, so माणवकमनु "
        "क्रीडति, where अनु is a कर्मप्रवचनीय, is outside.\n\n"
        "SCOPE — eight vārttikas hang on this sūtra, more than on any other in "
        "the pāda, and each adds a root in a named sense: सम् with अकूजन, "
        "आ-गम् in क्षमा, शिक्ष् in जिज्ञासा, कॄ in हर्ष/जीविका/कुलायकरण, हृ in "
        "गतताच्छील्य, आ with नु and प्रच्छ्, नाथ् in आशिस्, शप् in उपलम्भन. None is "
        "codified; each would be one more row in the table."
    ),
    "1.3.23": (
        "SETTLED — स्थेय is the arbitrator, विवादपदनिर्णेता लोके स्थेय इति "
        "प्रसिद्धः, and the आख्या-grahaṇa is there to reach the naming of one: "
        "त्वयि तिष्ठते, मयि तिष्ठते. प्रकाशन is showing oneself off — तिष्ठते कन्या "
        "छात्रेभ्यः, glossed प्रकाशयत्यात्मानम्."
    ),
    "1.3.24": (
        "SETTLED — again कर्मशब्दः क्रियावाची: ऊर्ध्वकर्मन् is the upward action, "
        "not an upward object. गेह उत्तिष्ठते is striving for the household; "
        "आसनादुत्तिष्ठति is getting up from a seat.\n\n"
        "SCOPE — the vārttika उद ईहायाम् narrows it further to effort, keeping "
        "अस्माद् ग्रामात् शतमुत्तिष्ठति out, and the Kāśikā is careful that this "
        "is a qualification and not an exception: ईहाग्रहणमनूर्ध्वकर्मण एव "
        "विशेषणम्, नापवादः. Not codified."
    ),
    "1.3.26": (
        "SETTLED — अकर्मकात् starts here and runs to 1.3.29, where the Kāśikā "
        "closes it with अकर्मकादिति निवृत्तम्. Four sūtras, and the corpus's "
        "anuvṛtti agrees exactly: 1.3.27, 1.3.28 and 1.3.29 each carry "
        "अकर्मकात् from 1.3.26, and 1.3.30 does not."
    ),
    "1.3.29": (
        "SETTLED — दृश् is here by vārttika (दृशेश्चेति वक्तव्यम्, संपश्यते), not "
        "by the sūtra, and it is in the codification with the other seven "
        "because the resolver has no way to mark a root as reached by "
        "supplement rather than by rule.\n\n"
        "SETTLED — विदेर्ज्ञानार्थस्य ग्रहणम्, the विद् that means knowing "
        "(02.0059), not the one that means getting. The Kāśikā's reason is "
        "साहचर्य with the parasmaipadin roots it is listed among, and it adds "
        "that the other विद् is svaritet and so उभयतोभाष anyway — a claim the "
        "file bears out.\n\n"
        "SETTLED — अर्ति is taken twice over, ऋ गतिप्रापणयोः of the first gaṇa "
        "and ऋ सृ गतौ of the third, विशेषाभावाद् द्वयोरपि ग्रहणम्. `entries_for` "
        "returns both without being told to."
    ),
    "1.3.30": (
        "SETTLED — अकर्मकादिति निवृत्तम्, and the Kāśikā spells out the "
        "consequence: अतः परं सामान्येनात्मनेपदविधानं प्रतिपत्तव्यम्. From here "
        "the grants are unconditioned by transitivity.\n\n"
        "SETTLED — अकर्त्रभिप्रायार्थोऽयमारम्भः again: ह्वेञ् is ñit, अन्यत्र हि "
        "ञित्वात् सिद्धमेवात्मनेपदम्."
    ),
    "1.3.32": (
        "SETTLED — the seven senses are glossed by the Kāśikā and the glosses "
        "are what the sense-names here stand for: गन्धन is malicious "
        "insinuation (अपकारप्रयुक्तं हिंसात्मकं सूचनम्), अवक्षेपण is abuse, सेवन "
        "is attendance, साहसिक्य is rashness, प्रतियत्न is improving what already "
        "exists (सतो गुणान्तराधानम्), प्रकथन is proclaiming, उपयोग is applying "
        "to a purpose. Outside all seven: कटं करोति."
    ),
    "1.3.34": (
        "SETTLED — and here कर्मन् is the object, not the action: कर्मशब्द इह "
        "कारकाभिधायी न क्रियावचनः. The contrast with 1.3.14 and 1.3.24, where "
        "the same word means the action, is the Kāśikā's own and is why the "
        "condition is carried as शब्दकर्मन् rather than as a sense."
    ),
    "1.3.37": (
        "SETTLED — three conditions and the Kāśikā gives a counter-example for "
        "each: कर्तृस्थ (देवदत्तो यज्ञदत्तस्य क्रोधं विनयति), अशरीर (गडुं विनयति), "
        "कर्मन् (बुद्ध्या विनयति). शरीरं प्राणिकायः, तदेकदेशोऽपि शरीरम् — a part of "
        "a body counts as a body."
    ),
    "1.3.38": (
        "SETTLED — read together with 1.3.39, which the Kāśikā says is there "
        "for उपसर्गनियम and nothing else: सोपसर्गादुपपरापूर्वादेव, नान्यपूर्वात्. "
        "So this sūtra is codified as applying without an upasarga, and 1.3.39 "
        "supplies the only two that are allowed. That is why संक्रामति falls "
        "outside without a separate prohibition."
    ),
    "1.3.42": (
        "SETTLED — समर्थ means the two upasargas are equivalent, तुल्यार्थौ, and "
        "the Kāśikā asks where that holds and answers आदिकर्मणि, in beginning "
        "an action: प्रक्रमते भोक्तुम्, उपक्रमते भोक्तुम्. Where they differ — "
        "पूर्वेद्युः प्रक्रामति (goes), अपरेद्युरुपक्रामति (comes) — it does not.\n\n"
        "SETTLED — and 1.3.39 does not already cover it, because वृत्त्यादि "
        "carries there and these are not those senses. The Kāśikā raises the "
        "objection itself and answers it."
    ),
    "1.3.43": (
        "SETTLED — अप्राप्तविभाषा: the option grants what was not otherwise "
        "available, so both क्रमते and क्रामति stand. Contrast 1.3.50, which "
        "the Kāśikā marks प्राप्तविभाषा — there the ātmanepada was already had "
        "and the option withdraws it."
    ),
    "1.3.44": (
        "SETTLED — सोपसर्गश्चायमपह्नवे वर्तते, न केवलः: the root takes this sense "
        "only with an upasarga, so the codification requires one. शतमपजानीते; "
        "न त्वं किंचिदपि जानासि is outside."
    ),
    "1.3.45": (
        "SETTLED — the Kāśikā anticipates the objection that सर्पिषो जानीते "
        "looks transitive and answers it with a cross-reference: the genitive "
        "is by 2.3.51 ज्ञोऽविदर्थस्य करणे, so सर्पिस् is the means and not the "
        "object. नात्र सर्पिरादि ज्ञेयत्वेन विवक्षितम्.\n\n"
        "SETTLED — अकर्त्रभिप्रायार्थमिदम्, because 1.3.76 अनुपसर्गाज्ज्ञः will "
        "cover the other case."
    ),
    "1.3.50": (
        "SETTLED — प्राप्तविभाषेयम्, an option over something already granted: "
        "1.3.48 gave the ātmanepada and this withdraws it half the time. Both "
        "of 1.3.48's conditions carry — व्यक्तवाचां समुच्चारणे इति च वर्तते — and "
        "the Kāśikā gives a counter-example for each: विप्रवदन्ति शकुनयः for "
        "the first, क्रमेण … विप्रवदन्ति for the second. So समुच्चारण is carried "
        "here as an asserted condition beside the sense, which is the one "
        "place in this block where the same word does both jobs."
    ),
    "1.3.51": (
        "SETTLED — गॄ निगरणे of the tudādi, not गॄ शब्दे of the kryādi, and the "
        "reason given is that the latter is never used with अव at all: तस्य "
        "ह्यवपूर्वस्य प्रयोग एव नास्ति. The file bears the distinction out — "
        "06.0146 is `nigaraRe` and 09.0033 is `Sabde` — but `entries_for` "
        "returns both, so the codification does not enforce it."
    ),
    "1.3.55": (
        "SETTLED — the sūtra needs a third case standing in a fourth's sense, "
        "and the Kāśikā admits this is not otherwise provided for: कथं पुनः "
        "तृतीया चतुर्थ्यर्थे स्यात्? वक्तव्यमेवैतत्. A vārttika supplies it — "
        "अशिष्टव्यवहारे तृतीया चतुर्थ्यर्थे भवति — for improper dealings. दास्या "
        "संप्रयच्छते; पाणिना संप्रयच्छति is outside.\n\n"
        "SETTLED — समः is genitive-as-qualifier, not ablative: समः इति विशेषणे "
        "षष्ठी, न पञ्चमी. That is why प्र can intervene without breaking it."
    ),
    "1.3.57": (
        "SETTLED — of the four roots only स्मृ is अप्राप्त. The Kāśikā works it "
        "out: ज्ञा already has ātmanepada by 1.3.44–1.3.46, and श्रु and दृश् by "
        "1.3.29, and in those cases 1.3.62 पूर्ववत् सनः would carry it to the "
        "desiderative anyway. स्मरतेः पुनरप्राप्त एव विधानम्."
    ),
    "1.3.58": (
        "SETTLED — and the Kāśikā notes what the prohibition amounts to in "
        "practice: तथा च सति सकर्मकस्यैवायं प्रतिषेधः संपद्यते, since the "
        "intransitive case is 1.3.45's and unaffected. पुत्रमनुजिज्ञासति."
    ),
    "1.3.59": (
        "SETTLED — उपसर्गग्रहणं चेदम्, so देवदत्तं प्रति शुश्रूषते, where प्रति is "
        "a कर्मप्रवचनीय, keeps its ātmanepada."
    ),
    "1.3.61": (
        "SETTLED — this is a नियम and not a grant, and the Kāśikā says why: "
        "मृङ् is ṅit, so ङित्त्वादात्मनेपदमत्र सिद्धमेव — 1.3.12 already gave it. "
        "The sūtra restricts it to luṅ, liṅ and a śit, and elsewhere it "
        "lapses: नियमः किमर्थम्? मरिष्यति. अमरिष्यत्. So the codification carries "
        "a second entry that cancels 1.3.12 outside those three, and an "
        "unstated lakāra is not one of the three either."
    ),
    "1.3.62": (
        "SETTLED — an atideśa, and the resolver performs it rather than "
        "tabulating it: the desiderative is resolved again with सन् set aside, "
        "and takes whatever that yields. The Kāśikā's own clause is what makes "
        "that the right mechanism — येन निमित्तेन पूर्वस्मादात्मनेपदं विधीयते, "
        "तेनैव सन्नन्तादपि भवति, by the same cause and not merely the same "
        "outcome.\n\n"
        "SETTLED — which is why शिशत्सति and मुमूर्षति do not get it: शद् needs "
        "a शित् (1.3.60) and मृ needs luṅ, liṅ or a शित् (1.3.61), and neither "
        "is present under सन्. न हि शदिम्रियतिमात्रमात्मनेपदनिमित्तम्. And "
        "अनुचिकीर्षति does not, because 1.3.79 cancelled the cause: यस्य च "
        "पूर्वत्रैव निमित्तभावः प्रतिषिध्यते, तत् सन्नन्तेऽप्यनिमित्तम्. All four "
        "fall out of the mechanism without being written down."
    ),
    "1.3.63": (
        "SCOPE — not codified. The sūtra governs the कृ that is appended after "
        "an आम्-stem in the periphrastic perfect (ईक्षांचक्रे), and neither लिट् "
        "nor 3.1.35's आम् is modelled yet, so there is no anuprayoga for the "
        "atideśa to reach.\n\n"
        "SETTLED, as reading — the Kāśikā holds it does both jobs at once, "
        "उभयमनेन क्रियते, विधिर्नियमश्च: it grants the ātmanepada where the "
        "fruit does not reach the agent, and by the second effort of पूर्ववत् "
        "restricts it, so उदुब्जांचकार stays parasmaipada."
    ),
    "1.3.64": (
        "SETTLED — युजिर् योगे is svaritet, and the file agrees at the right "
        "position: 07.0007 is written `yu\\ji~^r`, the svarita following the "
        "anunāsika it. So 1.3.72 already covers the कर्त्रभिप्राय case and this "
        "sūtra is for the other — अकर्त्रभिप्रायार्थोऽयमारम्भः.\n\n"
        "SCOPE — the vārttika स्वराद्यन्तोपसृष्टात् extends it to उद्युङ्क्ते and "
        "नियुङ्क्ते and is not codified."
    ),
    "1.3.65": (
        "SETTLED — the Kāśikā asks why क्ष्णु was not simply added to 1.3.29's "
        "list and answers अकर्मकादिति तत्र वर्तते: संक्ष्णुते शस्त्रम् is "
        "transitive, so it could not have gone there. The two sūtras are "
        "separated by a condition, not by accident."
    ),
    "1.3.66": (
        "SETTLED — the negative condition अनवने picks the root out for us: "
        "अनवन इति प्रतिषेधेन रौधादिकस्यैव ग्रहणं विज्ञायते, since it is the "
        "seventh-gaṇa भुज् (पालनाभ्यवहारयोः) that has protecting among its "
        "senses at all. So विभुजति पाणिम्, from the sixth-gaṇa भुज् कौटिल्ये, is "
        "outside. `entries_for` returns both entries and the codification does "
        "not enforce the choice."
    ),
    "1.3.67": (
        "SETTLED — the condition is that the object of the non-causative is "
        "the agent of the causative: आरोहन्ति हस्तिनं हस्तिपकाः, and then "
        "आरोहयते हस्ती स्वयमेव. Four counter-examples in the Kāśikā, one per "
        "word of the sūtra — णेः, अणौ, कर्म, कर्ता — and each fails a different "
        "clause.\n\n"
        "SETTLED — the Kāśikā answers the objection that कर्मवद्भाव would give "
        "this anyway: the atideśa reaches कर्मस्थभावक and कर्मस्थक्रिय roots, and "
        "this sūtra is कर्तृस्थार्थ — रुहि is कर्तृस्थक्रिय and दृशि "
        "कर्तृस्थभावक. Not modelled; the condition is carried as an assertion."
    ),
    "1.3.68": (
        "SETTLED — हेतु is the प्रयोजक कर्ता, the one denoted by the lakāra, and "
        "the fear must come from him: जटिलो भीषयते. Where the cause is an "
        "instrument and not the agent — कुञ्चिकयैनं भाययति — it does not apply. "
        "भयग्रहणमुपलक्षणार्थम्, so विस्मय goes with it: जटिलो विस्मापयते."
    ),
    "1.3.69": (
        "SETTLED — प्रलम्भनं विसंवादनं मिथ्याफलाख्यानम्, deceiving by promising a "
        "false result: माणवकं वञ्चयते. अहिं वञ्चयति, avoiding a snake, is the "
        "same root in its ordinary sense and is outside. The dhātupāṭha has "
        "वञ्चु twice and reads the second, 10.0227, in exactly this sense — "
        "`pralamBane` — which is the sūtra's word."
    ),
    "1.3.70": (
        "SETTLED — the च draws प्रलम्भन down from 1.3.69, so there are three "
        "senses and not two: कस्त्वामुल्लापयते is the third. Both लीङ् of the "
        "divādi and ली of the kryādi are meant, विशेषाभावाद् द्वयोरपि ग्रहणम्."
    ),
    "1.3.72": (
        "SETTLED — the two marks are read off the dhātupāṭha and are not the "
        "same mark as 1.3.12's. 106 entries carry a svarita on an it and 45 "
        "carry ञ्; 55 carry ङ्, which is 1.3.12's, and reading the two nasals "
        "as one would collapse this sūtra into that one. डुक्रीञ् is ñit and "
        "takes the middle endings only here; शीङ् is ṅit and takes them "
        "always.\n\n"
        "SETTLED — क्रियाफलं प्रधानभूतम्, यदर्थमसौ क्रियारभ्यते: the fruit is what "
        "the action is undertaken for, and it must fall to the agent the "
        "lakāra denotes. यजते, पचते, सुनुते, कुरुते. The Kāśikā's counter-"
        "examples are precise about what does not count — यजन्ति याजकाः, "
        "पचन्ति पाचकाः, कुर्वन्ति कर्मकराः — since the priest does get his fee "
        "and the labourer his wage, यद्यपि दक्षिणा भृतिश्च कर्तुः फलमिहास्ति, but "
        "न तदर्थः क्रियारम्भः, the action was not undertaken for it."
    ),
    "1.3.77": (
        "SETTLED — the Kāśikā states the scope exactly: पञ्चभिः सूत्रैः, the "
        "five sūtras 1.3.72 to 1.3.76, prescribe on the condition that the "
        "fruit-to-agent be conveyed by the construction, and this adds the "
        "case where an adjacent word conveys it instead — समीपे श्रूयमाणं "
        "शब्दान्तरमुपपदम्. स्वं यज्ञं यजति / यजते."
    ),
    "1.3.78": (
        "SETTLED — this is the hinge of the whole pāda and the Kāśikā's gloss "
        "is the architecture the resolver is built to: पूर्वेण प्रकरणेन "
        "आत्मनेपदनियमः कृतः, न परस्मैपदनियमः। तत् सर्वतः प्राप्नोति, तदर्थमिदम् "
        "उच्यते. The preceding section restricted the ātmanepada and said "
        "nothing about the parasmaipada, which would therefore apply "
        "everywhere; so this one confines it to the remainder — शेषादेव "
        "नान्यस्मात्. The codification returns 1.3.78 only when nothing in "
        "1.3.12–1.3.77 has fired.\n\n"
        "SETTLED — कर्तरि excludes the passive (पच्यते, गम्यते), and the second "
        "कर्तृग्रहण carried down from 1.3.14 excludes कर्मकर्तरि as well: तेन "
        "कर्तैव यः कर्ता, तत्र परस्मैपदं भवति, कर्मकर्तरि न भवति. So पच्यत ओदनः "
        "स्वयमेव keeps the middle endings."
    ),
    "1.3.85": (
        "SETTLED — पूर्वेण नित्ये परस्मैपदे प्राप्ते विकल्प आरभ्यते: 1.3.84 made "
        "it invariable and this makes it optional. यावद्भुक्तमुपरमति / "
        "उपरमते. And 1.3.84 was stated separately for exactly this — "
        "पृथग्योगकरणमुत्तरार्थम् — so that the option should attach to उप alone."
    ),
    "1.3.86": (
        "SETTLED — the Kāśikā works out why the sūtra is needed at all given "
        "1.3.87 and 1.3.88, and the answer is the residue: of these eight, "
        "the intransitive ones would be covered by 1.3.88 if their agents were "
        "sentient, so the sūtra is for अचित्तवत्कर्तृक cases (बोधयति पद्मम्, "
        "नाशयति दुःखम्); and the ones meaning motion would be covered by "
        "1.3.87, so it is for their other senses. Neither reason is modelled — "
        "the codification takes the eight roots as listed."
    ),
    "1.3.87": (
        "SETTLED — निगरणम् अभ्यवहारः and चलनं कम्पनम् are the Kāśikā's glosses, "
        "and both are readable in the dhātupāṭha's own sense-field, so the "
        "roots are derived rather than listed. भोजयति, चलयति, कम्पयति.\n\n"
        "SCOPE — the vārttika अदेः प्रतिषेधः exempts अद्, which the file glosses "
        "`BakzaRe` and which the derivation therefore does reach. Not "
        "codified: आदयते देवदत्तेन would come out parasmaipada."
    ),
    "1.3.88": (
        "SETTLED — the Kāśikā rejects one proposed counter-example and "
        "supplies another. चेतयमानं प्रयोजयति is not it, because हेतुमण्णिचो "
        "विधिः, प्रतिषेधोऽपि प्रत्यासत्तेस्तस्यैव न्याय्यः — the exclusion अणौ "
        "concerns the causative ṇic, so चेतयति stays parasmaipada. The real "
        "one is आरोहयमाणं प्रयुङ्क्ते."
    ),
    "1.3.89": (
        "SETTLED — a prohibition on 1.3.86 to 1.3.88, and the Kāśikā says "
        "precisely what survives it: यत्कर्त्रभिप्रायविषयमात्मनेपदम्, तदवस्थितमेव, "
        "न प्रतिषिध्यते — the ātmanepada 1.3.74 gives is untouched, so पाययते "
        "and रोचयते stand. It also sorts the nine by which of the three "
        "sūtras would have reached them: पा is निगरणार्थ (1.3.87), दमि and the "
        "rest are चित्तवत्कर्तृक (1.3.88), नृति is also चलनार्थ."
    ),
    "1.3.90": (
        "SETTLED — the Kāśikā raises the sharpest question in the pāda and "
        "answers it. If 1.3.12's नियम confines the ātmanepada to marked roots, "
        "how can it appear here merely because the parasmaipada lapsed? "
        "अथात्र परस्मैपदेन मुक्ते कथमात्मनेपदं लक्ष्यते? The answer inverts the "
        "sūtra: आत्मनेपदमेवात्र विकल्पितं विधीयते — what is really being "
        "prescribed optionally is the ātmanepada, and when the option lapses "
        "1.3.78 supplies the other. The resolver reads it the same way: an "
        "optional verdict means both stand.\n\n"
        "SCOPE — क्यष् itself is 3.1.13's and is not codified, so the affix is "
        "taken as given."
    ),
    "1.3.91": (
        "SETTLED — द्युतादि is not a list in the Aṣṭādhyāyī but a run in the "
        "dhātupāṭha, and the Kāśikā fixes both ends: द्युत (धा.पा. ७४१) and, by "
        "साहचर्य, everything down to कृपू (७६२). Here that is 01.0842 to "
        "01.0866, read off the file. The two numberings differ — the Kāśikā's "
        "is continuous and Vidyut's is gaṇa-and-serial — and the counts differ "
        "too, 22 against 25, so this recension reads three entries the "
        "Kāśikā's did not. Both agree on the endpoints.\n\n"
        "SETTLED — बहुवचननिर्देशादाद्यर्थो भवति: the plural in द्युद्भ्यः is what "
        "makes it a gaṇa rather than one root.\n\n"
        "SETTLED — and the option is over an ātmanepada that was invariable: "
        "अनुदात्तेत्त्वान्नित्यमेवात्मनेपदे प्राप्ते. The file confirms it — "
        "द्युत is `dyuta~\\`, the anudātta on the it."
    ),
    "1.3.92": (
        "SETTLED — वृतादि is a tail of the same run, वृतु (७५८) to कृपू (७६२), "
        "which is 01.0862 to 01.0866: five entries against the Kāśikā's five, "
        "and the same two endpoints. It names all five while glossing this "
        "sūtra — वृतु, वृधु, शृधु, स्यन्दू, कृपू — so the derivation can be "
        "checked member by member rather than only at the ends."
    ),
    "1.3.93": (
        "SETTLED — the च is doing textual work and the Kāśikā argues for it. "
        "कॢप् is in वृतादि, so 1.3.92 already gives the option before स्य and "
        "सन्; without the च this sūtra's grant for लुट् alone would, by being "
        "later, displace that one — इयं प्राप्तिः पूर्वां प्राप्तिं बाधेत. The च "
        "draws स्यसनोः down so that all three stand together.\n\n"
        "SETTLED — the root is named कॢपः and the file reads कृपू. 8.2.18 कृपो "
        "रो लः is what connects them, and `root_key` applies it."
    ),
}


def _register_pada_block() -> None:
    """
    Registers 1.3.14–1.3.93 from the provision table.

    One record per sūtra, whatever number of provisions it contributes: 1.3.72
    contributes two (the svarita and the ñ), 1.3.61 three (two grants and the
    niyama that cancels 1.3.12 outside them). The codification line is the
    table's own rendering, so it cannot drift from what the resolver tests.
    """
    ordered: "dict[str, list]" = {}
    for provision in PROVISIONS:
        sutra = provision.sutra.split("niyama")[0].split("v")[0]
        if sutra in ("1.3.12", "1.3.13"):
            continue
        ordered.setdefault(sutra, []).append(provision)

    # 1.3.62, 1.3.63 and 1.3.78 contribute no row: the first is performed by
    # the resolver, the second is not codified, the third is the residue.
    for sutra in ("1.3.62", "1.3.63", "1.3.78"):
        ordered.setdefault(sutra, [])

    for sutra in sorted(ordered, key=lambda s: int(s.rsplit(".", 1)[1])):
        provisions = ordered[sutra]
        if provisions:
            codification = " · ".join(
                dict.fromkeys(p.describe() for p in provisions)
            )
            worked = [p.example for p in provisions if p.example]
            against = [p.counter for p in provisions if p.counter]
        else:
            codification = {
                "1.3.62": "performed by the resolver: सन् is set aside and the "
                          "root resolved again, so the atideśa carries the "
                          "cause and not merely the outcome",
                "1.3.63": "PENDING — needs लिट् and 3.1.35's आम्, neither codified",
                "1.3.78": "the residue: returned when nothing in 1.3.12–1.3.77 "
                          "has fired",
            }[sutra]
            worked, against = [], []

        note = _NOTES.get(sutra)
        if note is None:
            first = provisions[0]
            note = "SETTLED — " + first.gloss + "."
            if worked:
                note += " The Kāśikā works it as " + "; ".join(
                    dict.fromkeys(worked)) + "."
            if against:
                note += " Its counter-example is " + "; ".join(
                    dict.fromkeys(against)) + "."
        if sutra in ("1.3.14", "1.3.78") and "SCOPE" not in note:
            note = note + "\n\n" + _GIVEN

        register(
            sutra,
            apply=pada_of_usage,
            codification=codification,
            notes=note,
        )


_register_pada_block()


__all__ = [
    "PROVISIONS",
    "adhikara",
    "analyze",
    "is_dhatu",
    "its_of",
    "lopa",
    "pada_of",
    "pada_of_usage",
    "stem_of",
    "yathasamkhya",
]
