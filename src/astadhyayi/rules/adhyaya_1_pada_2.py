# -*- coding: utf-8 -*-
"""
Aṣṭādhyāyī 1.2 — codified sūtra by sūtra.

Begun at 1.2.27, not at 1.2.1. The pāda opens with twenty-six sūtras that make
particular roots and affixes count as kit or ṅit, and each of those needs a
named root from the dhātupāṭha and an affix identified by its own rule; the
block from 1.2.27 stands on its own and closes a gap the codification of 1.1
kept recording.
"""

from __future__ import annotations

from src.astadhyayi.kittva import PROVISIONS as KIT_PROVISIONS
from src.astadhyayi.kittva import behaves_as
from src.astadhyayi.ekasesa import Word, ekasesa, ekasesa_of, number_for
from src.astadhyayi.luk import asisya, hrasva, yuktavat
from src.astadhyayi.svara import Recitation, recite, recite_written
from src.astadhyayi.sources import register
from src.astadhyayi.samjna import (
    aprkta,
    karmadharaya,
    pratipadika,
    upasarjana,
)
from src.astadhyayi.svara import (
    accent_of,
    combines,
    duration,
    substitutable,
    svarita_profile,
)


register(
    "1.2.27",
    samjna="hrasva",
    apply=duration,
    codification=(
        "duration(vowel) -> 1, 2 or 3 mātrās, and duration_name for the "
        "saṃjñā. The tables are the prosody engine's, so a vowel is as long "
        "to the grammar as to the metre."
    ),
    related=("1.1.70", "1.2.28", "1.2.32", "6.1.71"),
    notes=(
        "SETTLED — one sūtra, three names, and the vowel it is written with IS\n"
        "  the measure it assigns. The Kāśikā reads ऊ as a प्रश्लिष्टनिर्देश,\n"
        "  three enunciations fused by sandhi: ऊ इति त्रयाणां मात्रिक-\n"
        "  द्विमात्रिक-त्रिमात्रिकाणां प्रश्लिष्टनिर्देशः — उ, ऊ and ऊ३, of\n"
        "  one, two and three mātrās, matched in order against ह्रस्व, दीर्घ\n"
        "  and प्लुत. उकालो ह्रस्वः — दधि, मधु. ऊकालो दीर्घः — कुमारी, गौरी.\n"
        "  ऊ३कालः प्लुतः — देवदत्त३ अत्र न्वसि.\n"
        "\n"
        "SETTLED — कालग्रहणं परिमाणार्थम्, the word kāla is there to make it a\n"
        "  measure and not a list. So दीर्घ and प्लुत do not also get the name\n"
        "  ह्रस्व — दीर्घप्लुतयोः ह्रस्वसंज्ञा मा भूत् — which would otherwise\n"
        "  follow, and 6.1.71 ह्रस्वस्य पिति कृति तुक् would add a त् to\n"
        "  आलूय and प्रलूय.\n"
        "\n"
        "SETTLED — this is the sūtra behind what was already being computed.\n"
        "  1.1.70 तपरस्तत्कालस्य restricts a tapara term to sounds of its own\n"
        "  duration, and `grahana.kala` has been answering that since before\n"
        "  this pāda was touched. The two agree by construction: both read the\n"
        "  same vowel tables, and a test asserts it."
    ),
)


register(
    "1.2.28",
    reuses=('1.2.27',),
    apply=substitutable,
    codification=(
        "substitutable(sthanin) -> bool: only a vowel can be shortened, "
        "lengthened or protracted by these names."
    ),
    related=("1.1.48", "1.1.49", "1.2.27", "1.2.47", "7.4.25", "8.2.82"),
    notes=(
        "SETTLED — परिभाषेयं स्थानिनियमार्था: it restricts the substituend, not\n"
        "  the substitute. ह्रस्वदीर्घप्लुताः स्वसंज्ञया शिष्यमाणा अच एव स्थाने\n"
        "  वेदितव्याः — where one of the three names is used to prescribe, what\n"
        "  it replaces is a vowel.\n"
        "\n"
        "SETTLED — its first example is 1.2.47 ह्रस्वो नपुंसके, giving\n"
        "  रै → अतिरि, नौ → अतिनु, गो → उपगु. Those are the same three forms\n"
        "  1.1.48 एच इग्घ्रस्वादेशे turns on, from the other side: this sūtra\n"
        "  says the substituend must be a vowel, that one says which vowel the\n"
        "  substitute must be. Between them the pair is fully determined, and\n"
        "  1.1.50 supplies the choice neither of them states.\n"
        "\n"
        "SETTLED — अच इति किम्? सुवाग् ब्राह्मणकुलम्, where the form ends in a\n"
        "  consonant and there is nothing to shorten; भिद्यते and छिद्यते\n"
        "  against चीयते and श्रूयते for 7.4.25; and अग्निचि३त्, सोमसु३त् for\n"
        "  8.2.82, where the pluta falls on the vowel and not on the final त्."
    ),
)


register(
    "1.2.29",
    samjna="udātta",
    apply=accent_of,
    codification=(
        "accent_of(marked) -> Accent. Unmarked is udātta, which is the "
        "convention the SLP1 texts on disk use and why the dhātupāṭha writes "
        "only two marks."
    ),
    related=("1.1.69", "1.2.30", "1.2.31", "1.3.12"),
    notes=(
        "SETTLED — उच्चैः is not loudness. The Kāśikā rules that reading out:\n"
        "  उच्चैरिति च श्रुतिप्रकर्षो न गृह्यते ... उच्चैर्भाषते, उच्चैः\n"
        "  पठतीति — किं तर्हि? स्थानकृतमुच्चत्वं संज्ञिनो विशेषणम्. It is\n"
        "  height WITHIN the place of articulation: ताल्वादिषु हि भागवत्सु\n"
        "  स्थानेषु वर्णा निष्पद्यन्ते, तत्र यः समाने स्थाने ऊर्ध्वभागनिष्पन्नोऽच्\n"
        "  स उदात्तसंज्ञो भवति. So the same sthāna the varṇa layer already\n"
        "  carries, divided into an upper and a lower part.\n"
        "\n"
        "SETTLED — there is a physiological description beside the acoustic\n"
        "  one: यस्मिन्नुच्चार्यमाणे गात्राणाम् आयामः निग्रहो भवति, a tensing\n"
        "  of the organs. Its opposite is given under 1.2.30.\n"
        "\n"
        "SETTLED — this closes a gap. The note on 1.1.69 records that accent is\n"
        "  not modelled anywhere, so the first of the three dimensions\n"
        "  savarṇatva disregards — स्वर, आनुनासिक्य, काल — had no\n"
        "  representation. It has one now, and the dhātupāṭha carries the marks:\n"
        "  1,486 roots udātta, 667 anudātta, 106 svarita."
    ),
)


register(
    "1.2.30",
    samjna="anudātta",
    apply=accent_of,
    codification="The anudātta branch: the SLP1 backslash, as the texts mark it.",
    related=("1.2.29", "1.3.12", "3.1.4"),
    notes=(
        "SETTLED — the mirror of 1.2.29, and the Kāśikā's description is the\n"
        "  mirror too: यस्मिन्नुच्चार्यमाणे गात्राणाम् अन्ववसर्गः = मार्दवं\n"
        "  भवति, स्वरस्य मृदुता, कण्ठविवरस्य उरुता — a slackening, a softness\n"
        "  of tone, a widening of the throat. Against 1.2.29's आयामः निग्रहः.\n"
        "\n"
        "SETTLED — the mark is not decorative. 1.3.12 अनुदात्तङित आत्मनेपदम्\n"
        "  makes an anudātta root take ātmanepada endings, so the backslash in\n"
        "  the dhātupāṭha is grammatical information, and `Dhatu.accent` keeps\n"
        "  it apart from the form for that reason. 667 roots carry it."
    ),
)


register(
    "1.2.31",
    samjna="svarita",
    apply=combines,
    codification=(
        "combines(first, second) -> SVARITA when the two are udātta and "
        "anudātta. A relation between qualities, not between vowels."
    ),
    related=("1.2.29", "1.2.30", "1.2.32", "6.1.185"),
    notes=(
        "SETTLED — what is combined is the two QUALITIES and not two vowels:\n"
        "  सामर्थ्याच्चात्र लोकवेदयोः प्रसिद्धौ गुणावेव वर्णधर्मावुदात्तानुदात्तौ\n"
        "  गृह्येते, नाचौ. One vowel bears both in succession. शिक्यम्, कन्या,\n"
        "  सामन्यः, क्व.\n"
        "\n"
        "SETTLED — and in what proportion the sūtra does not say, which is why\n"
        "  1.2.32 follows immediately. The Kāśikā asks the question there in\n"
        "  four parts: कस्मिन्नंशे उदात्तः? कस्मिन्नंशेऽनुदात्तः? कियान्वा\n"
        "  उदात्तः? कियान्वा अनुदात्तः?"
    ),
)


register(
    "1.2.32",
    reuses=('1.2.27',),
    apply=svarita_profile,
    codification=(
        "svarita_profile(vowel) -> the split in mātrās: 0.5 udātta and the "
        "rest anudātta, whatever the vowel's length."
    ),
    related=("1.2.27", "1.2.31"),
    notes=(
        "SETTLED — it answers both halves of the question 1.2.31 leaves open:\n"
        "  तस्य स्वरितस्य आदावर्धह्रस्वम् उदात्तम्, परिशिष्टम् अनुदात्तम्.\n"
        "  Half a mātrā high at the start, the remainder low.\n"
        "\n"
        "SETTLED — half a mātrā, and not half the vowel. The Kāśikā takes the\n"
        "  wording apart to say so: अर्धह्रस्वम् इति च अर्धमात्रोपलक्ष्यते।\n"
        "  ह्रस्वग्रहणमतन्त्रम्। सर्वेषामेव ह्रस्वदीर्घप्लुतानां स्वरितानाम्\n"
        "  एष स्वरविभागः. So a svarita dīrgha is half a mātrā high and one and\n"
        "  a half low, and a svarita pluta two and a half low — the high part\n"
        "  is a constant and the low part is what varies. Reading अर्धह्रस्व as\n"
        "  'half the short vowel' would make the split proportional and every\n"
        "  long svarita wrong.\n"
        "\n"
        "SETTLED — which is why the profile is computed from 1.2.27's duration\n"
        "  rather than from the vowel: the two sūtras are one calculation."
    ),
)


# ---------------------------------------------------------------------------
# 1.2.41 to 1.2.46 — five saṃjñās and a fourth way of reading a case
#
# Implemented in src/astadhyayi/samjna.py, except 1.2.43's case-reading, which
# joins 1.1.49, 1.1.66 and 1.1.67 in adesa.py so that `nirdesa` reads four of
# the seven cases from one place.
# ---------------------------------------------------------------------------

register(
    "1.2.41",
    samjna="apṛkta",
    apply=aprkta,
    codification=(
        "aprkta(affix) -> bool, on the form after its it-letters are gone"
        ". A test on sounds, so a digraph is one al."
    ),
    related=("1.1.14", "1.3.9", "3.2.58", "6.1.67"),
    notes=(
        "SETTLED — एक means 'without a companion' here, and the Kāśikā gives\n"
        "  the same gloss it gives at 1.1.14: असहायवाची एकशब्दः. So the two\n"
        "  sūtras read एक the same way, one for a particle and one for an\n"
        "  affix. एकालिति किम्? दर्विः, जागृविः. प्रत्यय इति किम्? सुराः.\n"
        "\n"
        "SCOPE — the Kāśikā's own examples cannot be run end to end. क्विन्\n"
        "  at 3.2.58 and ण्वि at 3.2.62 both reduce to व् and are elided by\n"
        "  6.1.67 वेरपृक्तस्य, giving घृतस्पृक् and अर्धभाक् — but only after\n"
        "  the उच्चारणार्थ vowel goes, and no rule codified here removes it.\n"
        "  The it-rules leave क्विन् as वि, which is two sounds and not\n"
        "  apṛkta. The same gap recorded under 1.3.9, showing up again."
    ),
)

register(
    "1.2.42",
    samjna="karmadhāraya",
    apply=karmadharaya,
    codification=(
        "karmadharaya(tatpurusa=..., samanadhikarana=...) -> bool. Both a"
        "re flags, the second because it is a question about meaning."
    ),
    related=("2.1.22", "6.2.46", "6.2.130"),
    notes=(
        "SETTLED — both conditions, and the Kāśikā tests both.\n"
        "  तत्पुरुष इति किम्? पाचिकाभार्यः — a bahuvrīhi is out even though\n"
        "  its members share a referent. समानाधिकरण इति किम्?\n"
        "  ब्राह्मणराज्यम् — a tatpuruṣa is out when they do not.\n"
        "  परमराज्यम् and उत्तमराज्यम् satisfy both.\n"
        "\n"
        "SETTLED — समानाधिकरण is about denotation and not about grammar:\n"
        "  अधिकरणशब्दोऽभिधेयवाची, समानाधिकरणः समानाभिधेयः. So it has to be a\n"
        "  parameter; two strings cannot say whether they name one thing."
    ),
)

register(
    "1.2.43",
    samjna="upasarjana",
    apply=upasarjana,
    codification=(
        "The first-case branch. Read off the corpus like the other three "
        "case-paribhāṣās, but only for a rule that makes a compound."
    ),
    related=("1.1.49", "1.1.66", "1.1.67", "1.2.44", "2.1.24"),
    notes=(
        "SETTLED — a fourth case-reading, beside 1.1.49's sixth, 1.1.66's\n"
        "  seventh and 1.1.67's fifth: प्रथमया विभक्त्या यद् निर्दिश्यते\n"
        "  समासशास्त्रे तदुपसर्जनसंज्ञं भवति. So `nirdesa` now reads four of\n"
        "  the seven cases, and 2.1.24 द्वितीया श्रितातीतपतित... yields\n"
        "  द्वितीया as its upasarjana from the marking alone, giving\n"
        "  कष्टश्रितः.\n"
        "\n"
        "SETTLED — it is the only one of the four that is conditioned:\n"
        "  समास इति समासविधायि शास्त्रं गृह्यते, the word means a rule that\n"
        "  MAKES a compound. A first-case word anywhere else is not an\n"
        "  upasarjana, which is why `samasa_vidhi` has to be passed and the\n"
        "  other three read every sūtra unasked. The Kāśikā walks all six\n"
        "  case-compounds: शङ्कुलाखण्डः, यूपदारु, वृकभयम्, राजपुरुषः,\n"
        "  अक्षशौण्डः."
    ),
)

register(
    "1.2.44",
    apply=upasarjana,
    codification=(
        "The 1.2.44 branch of upasarjana(...), which reports which sūtra "
        "gave the name."
    ),
    related=("1.2.43", "2.2.18"),
    notes=(
        "SETTLED — a second ground for the same name: एका विभक्तिर्यस्य\n"
        "  तदिदमेकविभक्ति, something that keeps ONE case-ending while its\n"
        "  partner varies. निष्क्रान्तः कौशाम्ब्याः gives निष्कौशाम्बिः,\n"
        "  निष्क्रान्तं कौशाम्ब्याः gives निष्कौशाम्बिम् — the first member\n"
        "  changes case and the second stays ablative throughout.\n"
        "\n"
        "SETTLED — अपूर्वनिपाते excepts one consequence and not the name:\n"
        "  पूर्वनिपातं पूर्वनिपाताख्यम् उपसर्जनकार्यं वर्जयित्वा. Being\n"
        "  upasarjana normally puts a member first, and that particular\n"
        "  effect is withheld here.\n"
        "\n"
        "SCOPE — a vārttika एकविभक्तावषष्ठ्यन्तवचनम् adds that the word must\n"
        "  not end in a sixth case. Not codified."
    ),
)

register(
    "1.2.45",
    samjna="prātipadika",
    apply=pratipadika,
    codification=(
        "The 1.2.45 branch of pratipadika(...), which reports which sūtra"
        " gave the name."
    ),
    related=("1.2.46", "1.2.47", "4.1.1"),
    notes=(
        "SETTLED — three conditions and a worked counter-example for each.\n"
        "  अर्थवदिति किम्? वनम्, धनम् — so that the final -अन्, which means\n"
        "  nothing by itself, does not take the name and lose its न् by\n"
        "  नलोप. अधातुरिति किम्? अहन् — the same न् again, saved by\n"
        "  excluding roots. अप्रत्यय इति किम्? काण्डे, कुड्ये — else 1.2.47\n"
        "  ह्रस्वो नपुंसके would shorten them. Its own examples are डित्थः,\n"
        "  कपित्थः, कुण्डम्, पीठम्.\n"
        "\n"
        "SETTLED — a vārttika widens it: निपातस्यानर्थकस्य प्रातिपदिकसंज्ञा\n"
        "  वक्तव्या, a nipāta takes the name even where it means nothing —\n"
        "  अध्यागच्छति, प्रलम्बते. Codified, as the `nipata` flag, because it\n"
        "  is a plain extension of the same test."
    ),
)

register(
    "1.2.46",
    apply=pratipadika,
    codification=(
        "The 1.2.46 branch of pratipadika(...), which reports which sūtra"
        " gave the name."
    ),
    related=("1.2.45",),
    notes=(
        "SETTLED — it puts back what अप्रत्ययः had just excluded:\n"
        "  अप्रत्ययः इति पूर्वसूत्रे पर्युदासात् कृदन्तस्य तद्धितान्तस्य च\n"
        "  अनेन प्रातिपदिकसंज्ञा विधीयते. कारकः, हारकः, कर्ता, हर्ता for the\n"
        "  kṛt; औपगवः, कापटवः for the taddhita; राजपुरुषः, ब्राह्मणकम्बलः for\n"
        "  the compound.\n"
        "\n"
        "SETTLED — naming the compound RESTRICTS rather than adds:\n"
        "  अर्थवत्समुदायानां समासग्रहणं नियमार्थम्, and the consequence is\n"
        "  drawn out — समासग्रहणस्य नियमार्थत्वाद् वाक्यस्यार्थवतः संज्ञा न\n"
        "  भवति. A meaningful phrase satisfies 1.2.45 on its face and must\n"
        "  not take the name, and it is the mention of समास here that stops\n"
        "  it. So the codification refuses a phrase explicitly rather than by\n"
        "  omission."
    ),
)

# --- 1.2.1 to 1.2.26: कित्त्व and ङित्त्व by atideśa -----------------------
#
# Registered from `kittva.PROVISIONS` for the same reason 1.3.14–1.3.93 is
# registered from its table: the conditions are written down once, where the
# resolver reads them, and a second copy here could only drift from the first.
# What is written by hand is the notes.

_KIT_NOTES = {
    "1.2.1": (
        "SETTLED — the गाङ् meant is not the root गाङ् गतौ but the substitute\n"
        "  इङ् takes, and the Kāśikā's reason is a good one: ङकारस्य\n"
        "  अनन्यार्थत्वात्. If the root were meant, its own ङ् would already make\n"
        "  every affix ङित् by 1.3.12's neighbourhood and the sūtra would have\n"
        "  nothing to add. अध्यगीष्ट is the worked form.\n"
        "\n"
        "SETTLED — कुटादि is not a list in the Aṣṭādhyāyī. The Kāśikā fixes both\n"
        "  ends — कुट कौटिल्ये इत्येतदारभ्य यावत् कुङ् शब्दे — and the dhātupāṭha\n"
        "  has कुट at 06.0093 and कुङ् at 06.0136, so the forty-three members\n"
        "  between them are read off the file. Two texts agreeing on both ends.\n"
        "\n"
        "SETTLED — अञ्णित् is a question about the affix's own marks and is\n"
        "  answered by reading them, not by being told: उत्कोटयति is out because\n"
        "  णिच् carries ण्. उत्कुटिता, उत्कुटितुम्, उत्कुटितव्यम् are in."
    ),
    "1.2.3": (
        "SETTLED — अप्राप्तविभाषा. 1.2.2 gave विज् the ṅit behaviour outright;\n"
        "  here ऊर्णु gets it only optionally, and नothing else grants it, so\n"
        "  प्रोर्णुविता and प्रोर्णविता both stand."
    ),
    "1.2.4": (
        "SETTLED — अपित् can be read off the ending. तिप् carries प् and तस् and\n"
        "  झि do not, so कुरुतः and कुर्वन्ति take the ṅit behaviour and करोति\n"
        "  does not. The it-analysis of 1.3.2–1.3.9 answers it; nothing is\n"
        "  listed.\n"
        "\n"
        "SETTLED — सार्वधातुक is the other condition, and कर्ता, कर्तुम् and\n"
        "  कर्तव्यम् are outside it. The saṃjñā itself is 3.4.113's and is not\n"
        "  codified, so it is taken as given."
    ),
    "1.2.5": (
        "SETTLED — असंयोगात् is a question about the root's last two sounds, and\n"
        "  the Kāśikā's counter-examples settle what it means: सस्रंसे and\n"
        "  दध्वंसे, from roots the file writes `sransu̐` and `dhvansu̐`, each\n"
        "  ending in two consonants. भिद्, छिद् and यज् end in one.\n"
        "\n"
        "OPEN — अपित् carries down from 1.2.4, and for a लिट् ending it cannot be\n"
        "  read off the affix. The Kāśikā's counter-example बिभेदिथ shows थल्\n"
        "  counts as पित्, but थल् is spelt with ल् and not प्, and 3.4.82, which\n"
        "  teaches the endings, is not codified. Where that पित्त्व comes from is\n"
        "  not settled here; the caller states it.\n"
        "\n"
        "SETTLED, as reading — the Nyāsa raises ववृते and ववृधे, where kit-ness\n"
        "  and guṇa both offer themselves and guṇa is the later rule. Its answer\n"
        "  is that पर in विप्रतिषेधे परम् means इष्ट and not merely later:\n"
        "  कित्त्वमेवेष्टम्, कित्त्वमेव परम्. Not modelled — 1.4.2 is not codified."
    ),
    "1.2.6": (
        "SETTLED — the Kāśikā, reporting the bhāṣya, says what each of the two\n""  is for:\n"
        "  इन्धेः संयोगार्थं ग्रहणम्, भवतेः पिदर्थम्. इन्ध् ends in a conjunct and\n"
        "  so is outside 1.2.5; भू is named for the पित् endings, which 1.2.5's\n"
        "  अपित् would have excluded — बभूविथ.\n"
        "\n"
        "SCOPE — the vārttika श्रन्थिग्रन्थिदम्भिस्वञ्जीनां लिटः कित्त्वम् adds four\n"
        "  more optionally: श्रेथतुः, ग्रेथतुः, देभतुः, परिषस्वजे. Codified as an\n"
        "  option, but its अनुनासिकलोप is not."
    ),
    "1.2.7": (
        "SETTLED — the Kāśikā explains why seven roots need naming when 1.2.18\n"
        "  will only deny the kit-ness later: तस्यायं पुरस्तादपकर्षः, this is\n"
        "  drawn forward ahead of it. So these seven keep the kit-ness that\n"
        "  1.2.18 takes from every other seṭ क्त्वा, and the codification has\n"
        "  1.2.18 yield to 1.2.7 rather than the other way about.\n"
        "\n"
        "SETTLED — and three of the seven are named for a second reason: गुध,\n"
        "  कुष and क्लिश would have had it only optionally by 1.2.26, so\n"
        "  नित्यार्थं वचनम्, the mention makes it invariable."
    ),
    "1.2.8": (
        "SETTLED — the Kāśikā sorts the six by what each is there for. रुद्, विद्\n"
        "  and मुष् would have had it optionally by 1.2.26, so नित्यार्थं ग्रहणम्;\n"
        "  ग्रह् is a plain grant, विध्यर्थमेव; and स्वप् and प्रच्छ् are named for\n"
        "  the सन् alone, सन्नर्थं ग्रहणम्, किदेव हि क्त्वा — the क्त्वा was kit\n"
        "  anyway. Six roots, three different reasons, and the sūtra says none\n"
        "  of them.\n"
        "\n"
        "SCOPE — ग्रहादीनां कित्त्वात् संप्रसारणं भवति: the kit-ness is what lets\n"
        "  6.1.15's saṃprasāraṇa turn ग्रह् into गृह् and स्वप् into सुप्. That\n"
        "  consequence is not codified, so गृहीत्वा and सुप्त्वा are cited from\n"
        "  the commentary and not derived."
    ),
    "1.2.9": (
        "SETTLED — झल् is what separates चिचीषति from शिशयिषते, and the\n"
        "  separation is computed rather than stated: सन् begins with स्, but\n"
        "  under सेट् it begins with इ, and then it is not झलादि. One condition\n"
        "  covers both of the Kāśikā's forms.\n"
        "\n"
        "SETTLED — the Kāśikā, reporting the bhāṣya, asks किमर्थमिदमुच्यते? and\n""  answers गुणो मा\n"
        "  भूदिति, then raises the objection that 6.4.16's lengthening would\n"
        "  block guṇa anyway, and answers that the kit-ness is needed so the\n"
        "  lengthening has a field of its own. Ten vārttikas and two verses on\n"
        "  this sūtra; none codified."
    ),
    "1.2.10": (
        "SETTLED — समीपवचनोऽन्तशब्दः: अन्त here means 'near', not 'final'. So\n"
        "  हलन्तात् with इकः means a consonant next to an इक्, which is why\n"
        "  बिभित्सति and बुभुत्सते are in and यियक्षते is out — यज् has अ before\n"
        "  its final, and अ is not an इक्. The predicate is exactly that and\n"
        "  nothing more."
    ),
    "1.2.11": (
        "SETTLED — three counter-examples, one per condition, and each names the\n"
        "  rule that would go wrong. इकः: अयष्ट, where 6.1.15's saṃprasāraṇa\n"
        "  would follow. हलन्तात्: अचेष्ट, गुणो न स्यात्. झल्: अवर्तिष्ट, same.\n"
        "  आत्मनेपदेषु: अस्राक्षीत्, where 6.1.58's अम् would not come.\n"
        "\n"
        "SCOPE — none of those consequences is codified; the sūtra's conditions\n"
        "  are, and the forms are cited from the commentary."
    ),
    "1.2.12": (
        "SETTLED — the sūtra says उ and the Kāśikā reads ऋवर्णान्त. The उ is the\n"
        "  one taken with ॠ by 1.1.69 अणुदित् सवर्णस्य, already codified, and the\n"
        "  reading gives कृषीष्ट and अकृत. वरिषीष्ट is not a counter-example to\n"
        "  the ऋ but to the झल्: वृ takes इट् there, so the ending is not झलादि."
    ),
    "1.2.17": (
        "SETTLED — घु is 1.1.20 दाधा घ्वदाप्, already codified, and its six roots\n"
        "  are read from there rather than listed again: दाण्, डुदाञ्, डुधाञ्,\n"
        "  धेट्, देङ्, दो. अदित and अधित are the worked forms.\n"
        "\n"
        "SCOPE — the sūtra does two things and only one is codified. Besides the\n"
        "  kit-ness it substitutes इ for the root's final — इच्च — and that\n"
        "  substitution is not performed here, so उपास्थित is cited and not\n"
        "  derived."
    ),
    "1.2.18": (
        "SETTLED — this denies something that was there. क्त्वा carries an\n"
        "  indicatory क् by 1.3.8 लशक्वतद्धिते, so it is kit before this block\n"
        "  says anything, and the codification reads that mark off the affix\n"
        "  with the same `analyze` that reads a root's marks for 1.3.12.\n"
        "  देवित्वा and वर्तित्वा lose it; कृत्वा and हृत्वा, being अनिट्, keep it.\n"
        "\n"
        "SETTLED — and it does not reach what 1.2.7 and 1.2.8 settled, because\n"
        "  those were drawn forward past it: तस्यायं पुरस्तादपकर्षः. So मृडित्वा\n"
        "  and गृहीत्वा stay kit though both are सेट्. The codification has the\n"
        "  prohibition yield to those two by name.\n"
        "\n"
        "SETTLED — क्त्वाग्रहणं किम्? The mention of क्त्वा keeps निगृहीतिः,\n"
        "  उपस्निहितिः and निकुचितिः out, which are क्तिन् and not क्त्वा."
    ),
    "1.2.19": (
        "SETTLED — सेट् is the condition and स्विन्नः the counter-example, and\n"
        "  the Kāśikā explains how a सेट् निष्ठा of these roots arises at all:\n"
        "  7.2.16 आदितश्च forbids the इट्, and 7.2.17 विभाषा भावादिकर्मणोः lets\n"
        "  it back optionally — स विषयः कित्त्वप्रतिषेधस्य. Neither is codified."
    ),
    "1.2.21": (
        "SETTLED — व्यवस्थितविभाषा चेयम्, a settled option and not a free one:\n"
        "  the Kāśikā restricts it to roots taking शप् as their vikaraṇa, so\n"
        "  गुध परिवेष्टने of the ninth gaṇa is outside — गुधितम् is not\n"
        "  optional. Not codified; the option is offered on the shape alone.\n"
        "\n"
        "SETTLED — three conditions, three counter-examples: उदुपधात् (लिखितम्),\n"
        "  भावादिकर्मणोः (रुचितं कार्षापणं ददाति), सेट् (प्रभुक्त ओदनः)."
    ),
    "1.2.22": (
        "SETTLED — the क्त्वा here is redundant on its face, since 1.2.18 has\n"
        "  already denied a सेट् क्त्वा its kit-ness: तस्य ग्रहणमुत्तरार्थम्, it is\n"
        "  mentioned for what follows. The Kāśikā states the principle —\n"
        "  नित्यमकित्त्वमिडाद्योः क्त्वानिष्ठयोः क्त्वाग्रहणमुत्तरार्थम्."
    ),
    "1.2.23": (
        "SETTLED — two shape conditions and one counter-example each: नोपधात्\n"
        "  keeps रेफित्वा and गोफित्वा out, थफान्तात् keeps स्रंसित्वा and\n"
        "  ध्वंसित्वा out. Both are computed from the root."
    ),
    "1.2.25": (
        "SETTLED — काश्यपग्रहणं पूजार्थम्, वेत्येव हि वर्तते: the naming of\n"
        "  Kāśyapa is a mark of respect and adds nothing, since वा is already\n"
        "  carried down from 1.2.23. So the codification treats it as an\n"
        "  ordinary option and records the attribution rather than acting on it."
    ),
    "1.2.26": (
        "SETTLED — व्युपध is a compound the Kāśikā unpacks: उश्च इश्च वी, वी\n"
        "  उपधे यस्य स व्युपधः — having उ or इ as penultimate. Three shape\n"
        "  conditions in all, and a counter-example for each: रलः (देवित्वा),\n"
        "  व्युपधात् (वर्तित्वा), हलादेः (एषित्वा). All three are computed.\n"
        "\n"
        "SETTLED — this is the sūtra 1.2.7 and 1.2.8 were pre-empting. गुध, कुष,\n"
        "  क्लिश, रुद्, विद् and मुष् all satisfy its conditions and would have\n"
        "  had the kit-ness only optionally; being named earlier makes it\n"
        "  invariable for them."
    ),
}


def _register_kit_block() -> None:
    """One record per sūtra of 1.2.1–1.2.26, from the provision table."""
    ordered = {}
    for provision in KIT_PROVISIONS:
        sutra = provision.sutra.split("v")[0]
        ordered.setdefault(sutra, []).append(provision)

    for sutra in sorted(ordered, key=lambda s: int(s.rsplit(".", 1)[1])):
        provisions = ordered[sutra]
        codification = " · ".join(
            dict.fromkeys(p.describe() for p in provisions)
        )
        note = _KIT_NOTES.get(sutra)
        if note is None:
            first = provisions[0]
            note = "SETTLED — " + first.gloss + "."
            worked = [p.example for p in provisions if p.example]
            against = [p.counter for p in provisions if p.counter]
            if worked:
                note += " The Kāśikā works it as " + "; ".join(
                    dict.fromkeys(worked)) + "."
            if against:
                note += " Its counter-example is " + "; ".join(
                    dict.fromkeys(against)) + "."
        register(
            sutra,
            apply=behaves_as,
            codification=codification,
            notes=note,
        )


_register_kit_block()


# --- 1.2.33 to 1.2.40: how the three accents are actually recited ---------

register(
    "1.2.33",
    apply=recite_written,
    codification=(
        "recite(accents, Recitation(setting='dūrāt-sambuddhi')) -> every "
        "syllable at one tone. Over a sequence rather than a sound, because "
        "1.2.39 asks what came before and 1.2.40 what comes after."
    ),
    related=("1.2.29", "1.2.30", "1.2.31", "2.3.49"),
    notes=(
        "SETTLED — एकश्रुति is not a fourth accent but the suppressing of the\n"
        "  three: स्वराणाम् उदात्तादीनाम् अविभागो भेदतिरोधानम् एकश्रुतिः. So the\n"
        "  codification returns a register and not an accent, and 1.2.29–1.2.32\n"
        "  are what it is a register *of*.\n"
        "\n"
        "SETTLED — the सम्बुद्धि here is not 2.3.49's. एकवचनं सम्बुद्धिः gives\n"
        "  the name to a vocative singular ending; here the Kāśikā glosses it\n"
        "  दूरात् संबोधयति येन वाक्येन तत् संबोधनं संबुद्धिः — the utterance\n"
        "  itself, by which one calls to someone far off. It says न एकवचनं\n"
        "  सम्बुद्धिः in as many words, which is worth recording because the\n"
        "  other saṃjñā is the one a reader will have met.\n"
        "\n"
        "SETTLED — the rule is over a sentence, एकश्रुति वाक्यं भवति, and the\n"
        "  contrast is with त्रैस्वर्ये पदानां प्राप्ते, where all three stand.\n"
        "  आगच्छ भो माणवक देवदत्त३ at one tone; the same words near at hand\n"
        "  keep their accents."
    ),
)


register(
    "1.2.34",
    apply=recite_written,
    codification="The same, for setting='yajña', with three exceptions.",
    related=("1.2.33", "1.2.36"),
    notes=(
        "SETTLED — the mantras are taught with their three accents and would\n"
        "  be used so in the rite too: त्रैस्वर्येण वेदे मन्त्राः पठ्यन्ते, तेषां\n"
        "  यज्ञक्रियायामपि तथैव प्रयोगे प्राप्ते एकश्रुतिर्विधीयते. So this is a\n"
        "  rule about performance and not about the text.\n"
        "\n"
        "SETTLED — three exceptions, and the Kāśikā glosses each. जपः is the\n"
        "  muttered mantra, अनुकरणमन्त्रः उपांशुप्रयोगः. न्यूङ्खs are the sixteen\n"
        "  ओकारs, some udātta and some anudātta — तेषु केचिदुदात्ताः केचिद्\n"
        "  अनुदात्ताः — so flattening them would lose what they are. सामानि are\n"
        "  the sung portions, वाक्यविशेषस्था गीतयः.\n"
        "\n"
        "SCOPE — the three are carried as flags. Whether a given passage is a\n"
        "  japa or a sāman is not something any rule decides."
    ),
)


register(
    "1.2.35",
    apply=recite_written,
    codification="Recitation(setting='yajña', vasatkara=True) -> uccaistarām.",
    related=("1.2.34",),
    notes=(
        "SETTLED — and the word is not quite the one the sūtra uses.\n"
        "  वषट्शब्देनात्र वौषट्शब्दो लक्ष्यते, वौषट् इत्यस्यैवेदं स्वरविधानम् — it is\n"
        "  वौषट् whose accent is being prescribed, and वषट् stands for it. The\n"
        "  Kāśikā asks why the sūtra did not simply say वौषट् and answers\n"
        "  वैचित्र्यार्थम्, for variety: विचित्रा हि सूत्रस्य कृतिः पाणिनेः.\n"
        "\n"
        "SETTLED — the option is between उच्चैस्तराम् and the एकश्रुति 1.2.34\n"
        "  would otherwise give, not between उच्चैस्तराम् and the ordinary\n"
        "  accents. सोमस्याग्ने वीही३ वौ३षट्."
    ),
)


register(
    "1.2.36",
    apply=recite_written,
    codification="Recitation(setting='chandas') -> optionally one tone.",
    related=("1.2.34",),
    notes=(
        "SETTLED — विभाषा is used rather than the वा already available, and\n"
        "  the Kāśikā says why: वेति प्रकृते विभाषाग्रहणं यज्ञकर्मणीत्यस्य\n"
        "  निवृत्त्यर्थम्. The fresh word cuts off यज्ञकर्मणि, so the option\n"
        "  reaches private study as well — स्वाध्यायकालेऽपि पाक्षिक\n"
        "  ऐकश्रुत्यविधिर्भवति. That is the whole point of the choice of word.\n"
        "\n"
        "SETTLED — पक्षान्तरे त्रैस्वर्यमेव भवति: on the other reading all three\n"
        "  accents stand, which is what the codification returns as optional."
    ),
)


register(
    "1.2.37",
    apply=recite_written,
    codification=(
        "Recitation(setting='subrahmaṇyā') -> the accents stand, and a "
        "svarita is raised to udātta."
    ),
    related=("1.2.34", "1.2.36", "8.4.66"),
    notes=(
        "SETTLED — a प्रतिषेध on two rules at once, and the Kāśikā names both:\n"
        "  तत्र यज्ञकर्मणि इति विभाषा छन्दसि इति चैकश्रुतिः प्राप्ता प्रतिषिध्यते.\n"
        "  So it is tested before either of them.\n"
        "\n"
        "SETTLED — and it does a second thing. यस्तु लक्षणप्राप्तः स्वरितः तस्य\n"
        "  उदात्त आदेशो भवति — a svarita that arises *by rule* becomes udātta.\n"
        "  The rule meant is 8.4.66 उदात्तादनुदात्तस्य स्वरितः, and the Kāśikā\n"
        "  works इन्द्र आगच्छ through it syllable by syllable to show four\n"
        "  udāttas coming out where two would have been.\n"
        "\n"
        "SCOPE — 8.4.66 is not codified, so the svarita is taken as given\n"
        "  rather than derived. What is codified is what becomes of it."
    ),
)


register(
    "1.2.38",
    apply=recite_written,
    codification="Within the subrahmaṇyā, देव and ब्रह्मन् take anudātta instead.",
    related=("1.2.37",),
    notes=(
        "SETTLED — an exception inside an exception, and a narrow one: it\n"
        "  concerns one line of the subrahmaṇyā, देवा ब्रह्माण आगच्छत, where\n"
        "  1.2.37 would have raised the svarita to udātta and this lowers it\n"
        "  instead. सुब्रह्मण्यायामेव देवा ब्रह्माण इति पठ्यते — the Kāśikā is\n"
        "  explicit that the two words are being taken from that text."
    ),
)


register(
    "1.2.39",
    apply=recite_written,
    codification=(
        "Anudāttas following a svarita go to one tone, in saṃhitā. Needs the "
        "sequence: what decides it is what came earlier."
    ),
    related=("1.2.31", "8.4.66"),
    notes=(
        "SETTLED — संहितायाम् is the condition and the pada-pāṭha the\n"
        "  counter-example: संहिताग्रहणं किम्? अवग्रहे मा भूत् — इमं। मे।\n"
        "  गङ्गे। यमुने। सरस्वति। Said word by word, the anudāttas keep\n"
        "  themselves; said continuously, इमं मे गङ्गे यमुने सरस्वति शुतुद्रि,\n"
        "  everything after the svarita on मे runs at one tone.\n"
        "\n"
        "SETTLED — the svarita it looks back to is itself derived, by 8.4.66\n"
        "  उदात्तादनुदात्तस्य स्वरितः: मे is anudātta after an antodātta and so\n"
        "  becomes svarita, and only then does this rule have something to\n"
        "  work from. Not codified, so the accents are supplied."
    ),
)


register(
    "1.2.40",
    apply=recite_written,
    codification=(
        "An anudātta with an udātta or svarita next after it is recited "
        "sannatara. Needs the sequence: what decides it is what follows."
    ),
    related=("1.2.39",),
    notes=(
        "SETTLED — सन्नतर is glossed अनुदात्ततर, lower than an anudātta, so it\n"
        "  is a fourth register and not one of the three. The compound is\n"
        "  unpacked as a bahuvrīhi both ways: उदात्तः परो यस्मात् स उदात्तपरः,\n"
        "  स्वरितः परो यस्मात् स स्वरितपरः — the anudātta *before* a high tone,\n"
        "  not after one.\n"
        "\n"
        "SETTLED — the Kāśikā's two examples give one for each half. देवा\n"
        "  मरुतः पृश्निमातरोऽपः has the ो before the antodātta अपः; माणवक\n"
        "  जटिलकाध्यापक क्व गमिष्यसि has the क before the svarita क्व.\n"
        "\n"
        "SETTLED — अनुदात्तानाम् carries down from 1.2.39 and nothing else\n"
        "  does, which the corpus's anuvṛtti records: this is the only sūtra\n"
        "  of the eight that does not carry एकश्रुति."
    ),
)


# --- 1.2.47 to 1.2.73: shortening, disappearance, number, एकशेष ----------

_TAIL = {
    "1.2.47": (
        hrasva,
        "hrasva(stem, napumsaka=True) -> the final vowel shortened, by "
        "1.1.52 अलोऽन्त्यस्य, which is already codified and does the locating.",
        "SETTLED — the substitute goes on the last sound and not the whole "
        "stem, and that is 1.1.52's doing rather than this sūtra's: "
        "ह्रस्वो भवत्यादेशोऽलोऽन्त्यस्याचः. अतिरि कुलम्, अतिनु कुलम्.\n\n"
        "SETTLED — two counter-examples, one per word. नपुंसक इति किम्? "
        "ग्रामणीः, सेनानीः, which are masculine. प्रातिपदिकस्येति किम्? "
        "काण्डे तिष्ठतः, कुड्ये तिष्ठतः — there the long vowel is a case-form "
        "and not part of the stem.\n\n"
        "SETTLED — and the mention of प्रातिपदिक does a second thing by its "
        "very presence: प्रातिपदिकग्रहणसामर्थ्याद् एकादेशः पूर्वस्यान्तवन् न "
        "भवति. Not modelled; 6.1.85 is not codified."
    ),
    "1.2.48": (
        hrasva,
        "The same, for a subordinate गो-final or feminine-affix-final stem.",
        "SETTLED — गो is named by its own form and स्त्री by the affix, and "
        "the Kāśikā tells them apart by accent: गो इति स्वरूपग्रहणम्, स्त्रीति "
        "प्रत्ययग्रहणं स्वरितत्वात्. The svarita is the unwritten mark of "
        "1.3.11, which is why the distinction cannot be read off the text.\n\n"
        "SETTLED — that reading is what keeps अतितन्त्रीः, अतिलक्ष्मीः and "
        "अतिश्रीः out: their ई is part of the stem and not a feminine affix. "
        "स्वरितत्वं किम्? is the Kāśikā's own way of putting the question.\n\n"
        "SETTLED — उपसर्जनस्येति किम्? राजकुमारी, where the feminine is the "
        "head and not subordinate. उपसर्जन itself is 1.2.43's, already "
        "codified.\n\n"
        "SCOPE — the vārttika ईयसो बहुव्रीहेः प्रतिषेधः exempts a bahuvrīhi in "
        "ईयस् — बहुश्रेयसी, विद्यमानश्रेयसी. Not codified."
    ),
    "1.2.49": (
        hrasva,
        "Where a taddhita has dropped, the subordinate feminine affix drops "
        "rather than shortening.",
        "SETTLED — an apavāda to 1.2.48, and the Kāśikā says so in its first "
        "words: पूर्वेण ह्रस्वत्वे प्राप्ते लुग् विधीयते. So the codification "
        "tests these four backwards, most specific first.\n\n"
        "SETTLED — three conditions and a counter-example for each. तद्धित: "
        "गार्ग्याः कुलं गार्गीकुलम्, a compound and not a taddhita. लुक्: "
        "गार्गीत्वम्, where the taddhita stands. उपसर्जन: अवन्ती, कुन्ती, "
        "कुरूः, where the feminine is not subordinate."
    ),
    "1.2.50": (
        hrasva,
        "And गोणी takes इ where 1.2.49 would have dropped its affix.",
        "SETTLED — an apavāda to the apavāda: पूर्वेण लुकि प्राप्ते इकारो "
        "विधीयते. पञ्चभिर् गोणीभिः क्रीतः पटः पञ्चगोणिः.\n\n"
        "SETTLED — the इत् of the sūtra is read as a योगविभाग, a splitting "
        "that leaves इत् standing on its own, so that सूची is reached as "
        "well: पञ्चसूचिः, दशसूचिः. The Kāśikā adds स च एवंविषय एव, and that "
        "second rule is not codified — only गोणी is."
    ),
    "1.2.51": (
        yuktavat,
        "yuktavat(gender=..., number=...) -> what a लुप्-form carries over.",
        "SETTLED — युक्तवत् is glossed through the क्तवतु of निष्ठा: युक्तः "
        "प्रकृत्यर्थः प्रत्ययार्थेन संबद्धः, the base-meaning as it stood joined "
        "to the affix-meaning. पञ्चालाः is masculine plural as the name of "
        "the warriors and stays so as the name of the country.\n\n"
        "SETTLED — व्यक्ति and वचन are not Pāṇini's words. व्यक्तिवचने इति च "
        "लिङ्गसंख्ययोः पूर्वाचार्यनिर्देशः, तदीयमेवेदं सूत्रम् — the sūtra is the "
        "earlier teachers', taken over whole. Which is why 1.2.53 turns "
        "round two sūtras later and discards it: तथा चास्य प्रत्याख्यानं "
        "भविष्यति.\n\n"
        "SETTLED — लुपीति किम्? Under लुक् it does not hold, and the gender "
        "follows the noun qualified instead: लवणः सूपः, लवणा यवागूः, लवणं "
        "शाकम्. The two elisions are different saṃjñās and only one is meant."
    ),
    "1.2.52": (
        yuktavat,
        "And the qualifiers carry it too, except the class-word.",
        "SETTLED — पञ्चालाः रमणीयाः बह्वन्नाः, the adjectives following the "
        "name into the plural. अजातेरिति किम्? पञ्चालाः जनपदः, where जनपद "
        "names the class and stays singular.\n\n"
        "SETTLED — and the exception spreads: जातिद्वारेण यानि विशेषणानि "
        "तेषामपि युक्तवद्भावो न भवति. Once the class-word is singular, "
        "whatever qualifies *through* it is singular as well — पञ्चालाः "
        "जनपदो रमणीयो बह्वन्नः, with रमणीय now agreeing with जनपद and not "
        "with पञ्चालाः.\n\n"
        "SCOPE — three vārttikas: हरीतक्यादिषु व्यक्तिः, खलतिकादिषु वचनम्, "
        "मनुष्यलुपि प्रतिषेधः. None codified."
    ),
    "1.2.53": (
        asisya,
        "asisya('yuktadbhāva') -> the record. Nothing is performed, because "
        "the sūtra prescribes nothing.",
        "SETTLED — and this is a different kind of sūtra from anything "
        "codified so far. It teaches nothing; it says that something else "
        "need not have been taught. तद् अशिष्यम्, न वक्तव्यम्. What is "
        "withdrawn is 1.2.51, two sūtras back.\n\n"
        "SETTLED — the reason is that पञ्चाल and वरणा are names: नैते "
        "योगशब्दाः, किं तर्हि? जनपदादीनां संज्ञा एताः. A name carries its "
        "gender and number by nature — तत्र लिङ्गं वचनं च स्वभावसिद्धमेव न "
        "यत्नप्रतिपाद्यम् — as आपः, दाराः, गृहाः, सिकताः and वर्षाः do without "
        "any rule.\n\n"
        "IMPLEMENTATION — codified as a record and not as a function. A "
        "sūtra that declines to prescribe has no operation to perform, and "
        "giving it one would invent exactly the work it refuses."
    ),
    "1.2.54": (
        asisya,
        "asisya('lup') -> the record.",
        "SETTLED — and now the लुप् itself goes, which is to say 4.2.81 "
        "जनपदे लुप् and 4.2.82 वरणादिभ्यश्च. The reason: न हि पञ्चाला वरणा "
        "इति योगः संबन्धः प्रख्यायते — the connection those rules presuppose "
        "is not one anybody perceives. नैतद् उपलभामहे वृक्षयोगान् नगरे वरणा "
        "इति: nobody takes the city to be called वरणा from the trees.\n\n"
        "SETTLED — and the consequence is drawn to the end: if 4.2.69 and "
        "4.2.70 never produce a taddhita here, there is nothing left for a "
        "लुप् to remove — तस्माद् अत्र तद्धितो नैवोत्पद्यते, किं लुपो विधानेन."
    ),
    "1.2.55": (
        asisya,
        "asisya('the-argument-for-it') -> the record.",
        "SETTLED — the only one of the five that argues rather than asserts, "
        "and the argument is a good one. If पञ्चाल denoted the connection, "
        "then where the connection failed the word would fail with it: "
        "तदभावे अदर्शनम् अप्रयोगः स्यात्. It does not fail — दृश्यते च संप्रति "
        "विनैव क्षत्रियसंबन्धेन जनपदेषु पञ्चालादिशब्दः, the word is used of the "
        "country with no warriors in view. Therefore it never named the "
        "connection: रूढिरूपेणैव तत्र प्रवृत्तः."
    ),
    "1.2.56": (
        asisya,
        "asisya('how-a-compound-divides-its-meaning') -> the record.",
        "SETTLED — aimed at the पूर्वाचार्याः and their formula "
        "प्रधानोपसर्जने प्रधानार्थं सह ब्रूतः, प्रकृतिप्रत्ययौ सहार्थं ब्रूतः. "
        "तत् पाणिनिराचार्यः प्रत्याचष्टे — the teacher Pāṇini rejects it.\n\n"
        "SETTLED — the ground is that meaning is not a grammarian's to fix: "
        "शब्दैर् अर्थाभिधानं स्वाभाविकं न पारिभाषिकम्, अशक्यत्वात्, लोकत एव "
        "अर्थावगतेः. And the proof offered is empirical. यैरपि व्याकरणं न "
        "श्रुतं तेऽपि राजपुरुषम् आनयेत्युक्ते राजविशिष्टं पुरुषम् आनयन्ति, न "
        "राजानं नापि पुरुषमात्रम् — people who never studied grammar, told to "
        "fetch the king's man, fetch neither the king nor just any man. "
        "यश्च लोकतोऽर्थः सिद्धः किं तत्र यत्नेन."
    ),
    "1.2.57": (
        asisya,
        "asisya('the-definitions-of-today-and-of-upasarjana') -> the record.",
        "SETTLED — तुल्यशब्दो हेत्वनुकर्षणार्थः: the तुल्यम् is there to carry "
        "1.2.56's reason across, so two more of the old definitions fall on "
        "the same ground. One party fixed काल as आ न्याय्याद् उत्थानाद् आ "
        "न्याय्याच् च संवेशनात्, another as अहरुभयतोऽर्धरात्रम्; and उपसर्जन "
        "they defined as अप्रधानम्. All discarded, since people who never "
        "studied grammar say इदम् अस्माभिर् अद्य कर्तव्यम् and are understood.\n\n"
        "SETTLED — the Kāśikā asks why this was not simply folded into "
        "1.2.56 and answers प्रदर्शनार्थः, that the split shows a kind: "
        "अन्यदप्येवंजातीयकम् अशिष्यम्. It then names four more of the old "
        "definitions that go with them — मत्वर्थे बहुव्रीहिः, "
        "पूर्वपदार्थप्रधानोऽव्ययीभावः, उत्तरपदार्थप्रधानस्तत्पुरुषः, "
        "उभयपदार्थप्रधानो द्वन्द्वः. So the five are a programme and not a "
        "list, and the record says which four the programme reaches."
    ),
    "1.2.58": (
        number_for,
        "number_for(counted=1, jati=True) -> (1, 3), optionally.",
        "SETTLED — a class is one thing, so the singular is what would come: "
        "जातिर् नामायम् एकोऽर्थः, तदभिधान एकवचनम् एव प्राप्तम्, अत इदम् उच्यते. "
        "संपन्नो व्रीहिः beside संपन्ना व्रीहयः.\n\n"
        "SETTLED — and the plural spreads to the qualifiers, which are not "
        "class-words themselves: तेन तद्विशेषणानाम् अजातिशब्दानाम् अपि "
        "संपन्नादीनां बहुवचनम् उपपद्यते.\n\n"
        "SETTLED — आख्यायाम् is a condition, not decoration. काश्यपः meaning "
        "a portrait of Kāśyapa is a class-word but does not *name* a class — "
        "भवत्ययं जातिशब्दो न त्वनेन जातिराख्यायते — so it stays singular.\n\n"
        "SCOPE — the vārttika संख्याप्रयोगे प्रतिषेधः bars it where a numeral "
        "is used: एको व्रीहिः संपन्नः. Codified."
    ),
    "1.2.59": (
        number_for,
        "number_for(counted=1 or 2, asmad=True) -> the plural as well.",
        "SETTLED — अहं ब्रवीमि / वयं ब्रूमः for one, आवां ब्रूवः / वयं ब्रूमः "
        "for two.\n\n"
        "SCOPE — two supplements, neither codified. सविशेषणस्य प्रतिषेधः bars "
        "it where अस्मद् carries a qualifier — अहं देवदत्तो ब्रवीमि. And "
        "युष्मदि गुराव् एकेषाम् extends it to युष्मद् for a teacher, on some "
        "authorities: त्वं मे गुरुः / यूयं मे गुरवः."
    ),
    "1.2.60": (
        number_for,
        "number_for(counted=2, star='phalgunī', nakshatra=True) -> plural too.",
        "SETTLED — the च draws द्वयोः down from 1.2.59, चकारो द्वयोर् इत्य् "
        "अनुकर्षणार्थः, so the rule is about two: कदा पूर्वे फल्गुन्यौ, कदा "
        "पूर्वाः फल्गुन्यः.\n\n"
        "SETTLED — नक्षत्र इति किम्? फल्गुन्यौ माणविके, two girls of that name, "
        "which keeps the dual. So the codification asks which star and "
        "whether a star is meant, not merely whether a pair is."
    ),
    "1.2.61": (
        number_for,
        "And in the Veda, पुनर्वसू may stand in the singular.",
        "SETTLED — two conditions, each with its counter-example: नक्षत्रे "
        "(पुनर्वसू माणवकौ keeps the dual) and छन्दसि (पुनर्वसू इति, outside "
        "the Veda, likewise). पुनर्वसुर् नक्षत्रम् beside पुनर्वसू नक्षत्रम्."
    ),
    "1.2.62": (
        number_for,
        "And विशाखा likewise.",
        "SETTLED — छन्दसि carries down, and the two sūtras differ only in "
        "which pair of stars they name: विशाखा नक्षत्रम् beside विशाखे "
        "नक्षत्रम्. Codified as one condition with two star-names."
    ),
    "1.2.63": (
        number_for,
        "number_for(dvandva_of=('tiṣya','punarvasū'), nakshatra=True) -> dual.",
        "SETTLED — one star and two make three, so the dvandva would be "
        "plural, and this makes it dual: तिष्य एकः पुनर्वसू द्वौ, तेषां द्वन्द्वो "
        "बह्वर्थः. उदितौ तिष्यपुनर्वसू दृश्येते.\n\n"
        "SETTLED — नक्षत्रे is repeated though it was already available, and "
        "the Kāśikā explains why: पर्यायाणाम् अपि यथा स्यात्, so that the "
        "star's other names are reached too — पुष्यपुनर्वसू, सिद्ध्यपुनर्वसू.\n\n"
        "SETTLED — बहुवचनस्येति किम्? एकवचनस्य मा भूत्. And the Kāśikā takes "
        "that restriction as a ज्ञापक for a paribhāṣā it does not otherwise "
        "have: सर्वो द्वन्द्वो विभाषैकवद् भवति. Not codified.\n\n"
        "SETTLED — नित्यग्रहणं विकल्पनिवृत्त्यर्थम्, the नित्यम् shutting out the "
        "options carried down from 1.2.58."
    ),
}


#: Verified by reading the branch, not inferred. 1.2.47, 1.2.48 and 1.2.50
#: each put their substitute on the stem's last sound, and all three do it by
#: calling 1.1.52's `replace_antya` rather than slicing the string — which is
#: what the Kāśikā says is happening: ह्रस्वो भवत्यादेशोऽलोऽन्त्यस्याचः.
#: 1.2.49 is not here: it drops the affix outright, which is a luk and not a
#: substitution of the final sound.
_TAIL_REUSES = {
    "1.2.47": ("1.1.52",),
    "1.2.48": ("1.1.52",),
    "1.2.50": ("1.1.52",),
}


def _register_tail() -> None:
    for sutra, (fn, codification, notes) in _TAIL.items():
        register(sutra, apply=fn, codification=codification, notes=notes,
                 reuses=_TAIL_REUSES.get(sutra, ()))


_register_tail()


_EKASESA = {
    "1.2.64": (
        "ekasesa(words) -> which one remains, and by which sūtra.",
        "SETTLED — the Kāśikā gives the reason the rule is needed at all, "
        "and it is worth having: प्रत्यर्थं शब्दनिवेशाद् नैकेनानेकस्याभिधानम्, "
        "a word is deployed once per thing meant, so one word cannot denote "
        "several. Two trees call for two utterances of वृक्ष; तत्र "
        "अनेकार्थाभिधाने अनेकशब्दत्वं प्राप्तम्, तस्माद् एकशेषः.\n\n"
        "SETTLED — four words, four counter-examples, and the Kāśikā gives "
        "one for each. सरूपाणाम्: प्लक्षन्यग्रोधाः. रूपम् rather than अर्थ, so "
        "that it holds though the senses differ — भिन्नेऽप्यर्थे यथा स्यात्, "
        "अक्षाः, पादाः, माषाः. एक: द्विबह्वोः शेषो मा भूत्. शेष rather than "
        "आदेश: आदेशो मा भूत्. एकविभक्तौ: पयः पयो जरयति, ब्राह्मणाभ्यां च कृतं "
        "ब्राह्मणाभ्यां च देहि.\n\n"
        "SCOPE — the vārttika विरूपाणामपि समानार्थकानाम् एकशेषो वक्तव्यः "
        "extends it to words of unlike form but one meaning. Not codified."
    ),
    "1.2.65": (
        "The gotra name survives against its descendant's.",
        "SETTLED — वृद्ध is not Pāṇini's coinage either: वृद्धशब्दः "
        "पूर्वाचार्यसंज्ञा गोत्रस्य, अपत्यम् अन्तर्हितं वृद्धम्. Same species as "
        "1.3.1's धातु and 1.2.51's व्यक्तिवचन — an earlier teachers' term "
        "taken over.\n\n"
        "SETTLED — तल्लक्षणश्चेदेव विशेषः is unpacked word by word — तद् is "
        "वृद्धयुवनोः, लक्षण is निमित्त, चेत् is 'if', एव is restrictive, विशेष "
        "is वैरूप्य — and each word earns a counter-example. वृद्ध: "
        "गर्गगार्ग्यायणौ. यूना: गार्ग्यगर्गौ. तल्लक्षण: गार्ग्यवात्स्यायनौ, "
        "different stems. एव: भागवित्तिभागवित्तिकौ, where कुत्सा and "
        "सौवीरत्व divide them besides. The codification tests all four."
    ),
    "1.2.66": (
        "A feminine elder survives, and takes the masculine's forms.",
        "SETTLED — two things at once, and the च joins them: the feminine "
        "survives where 1.2.67 would have dropped her, and पुंस इवास्याः "
        "कार्यं भवति, her form follows the masculine. गार्गी च गार्ग्यायणश्च "
        "गार्ग्यौ — the survivor is गार्गी and the form is गार्ग्य.\n\n"
        "SETTLED — दाक्षी च दाक्षायणश्च दाक्षी is the case where the पुंवद्भाव "
        "leaves the form unchanged, which is why the Kāśikā gives it beside "
        "the other two."
    ),
    "1.2.67": (
        "The masculine survives against the feminine.",
        "SETTLED — ब्राह्मणश्च ब्राह्मणी च ब्राह्मणौ, and तल्लक्षणश्चेदेव विशेषः "
        "carries down from 1.2.65 with its full force. Three "
        "counter-examples: कुक्कुटमयूर्यौ, different stems; इन्द्रेन्द्राण्यौ, "
        "where 4.1.48 पुंयोगादाख्यायाम् is a second difference — अपरो विशेषः; "
        "and प्राक्प्राच्यौ, where प्राक् is not masculine but of no gender at "
        "all, प्रागित्यव्ययम् अलिङ्गम्."
    ),
    "1.2.68": (
        "भ्रातृ survives against स्वसृ, and पुत्र against दुहितृ.",
        "SETTLED — यथासंख्यम्, and the codification calls 1.3.10 rather than "
        "repeating it. Two words against two, equal in number and equally "
        "enumerated, so they pair off in order: भ्राता च स्वसा च भ्रातरौ, "
        "पुत्रश्च दुहिता च पुत्रौ. The Kāśikā's first word on the sūtra is "
        "यथासंख्यम्, so the cross-reference is its own."
    ),
    "1.2.69": (
        "The neuter survives, and optionally goes into the singular.",
        "SETTLED — शुक्लश्च कम्बलः शुक्ला च बृहतिका शुक्लं च वस्त्रं तद् इदं "
        "शुक्लम्, or तानीमानि शुक्लानि.\n\n"
        "SETTLED — अनपुंसकेनेति किम्? Three neuters together give शुक्लानि by "
        "1.2.64, and एकवच् च इति न भवति — the singular option does not reach "
        "them. That is the whole work of the word, and the codification "
        "requires a non-neuter to be present."
    ),
    "1.2.70": (
        "पितृ survives against मातृ, optionally.",
        "SETTLED — अन्यतरस्याम् carries down from 1.2.69 but नैकवत् does not, "
        "which is what the Kāśikā's अन्यतरस्यामिति वर्तते नैकवदिति settles: "
        "the option is over whether to retain at all, not over the number. "
        "माता च पिता च पितरौ, or मातापितरौ."
    ),
    "1.2.71": (
        "श्वशुर survives against श्वश्रू, optionally.",
        "SETTLED — the same shape as 1.2.70 and the same anuvṛtti: "
        "श्वशुरश्च श्वश्रूश्च श्वशुरौ, or श्वश्रूश्वशुरौ."
    ),
    "1.2.72": (
        "A त्यदादि word survives against anything, invariably.",
        "SETTLED — त्यदादि is not a separate list. The name means त्यद् and "
        "what follows, and what follows is fixed by 1.1.27's सर्वादि gaṇa, "
        "which the corpus holds entire: त्यद् is its twenty-fourth member and "
        "twelve remain after it, ending at किम्. So the group is read.\n\n"
        "SETTLED — सर्वग्रहणं साकल्यार्थम्, नित्यग्रहणं विकल्पनिवृत्त्यर्थम्: "
        "against everything, and without the options. स च देवदत्तश्च तौ.\n\n"
        "SETTLED — the vārttika त्यदादीनां मिथो यद् यत् परं तत् तच्छिष्यते "
        "settles the case of two त्यदादि words, and 'later' means later in "
        "that same gaṇa: स च यश्च यौ (यद् after तद्), यश्च कश्च कौ (किम् after "
        "यद्). Codified, and checkable against the gaṇa's order."
    ),
    "1.2.73": (
        "But for a herd of grown domestic animals, the feminine survives.",
        "SETTLED — an apavāda to 1.2.67, and the Kāśikā says so outright: "
        "पुमान् स्त्रिया इति पुंसः शेषे प्राप्ते स्त्रीशेषो विधीयते. गाव इमाः, "
        "अजा इमाः.\n\n"
        "SETTLED — four conditions and a counter-example for each. ग्राम्य: "
        "रुरव इमे, पृषता इमे, which are wild. पशु: ब्राह्मणाः, क्षत्रियाः. "
        "सङ्घ: एतौ गावौ चरतः, two cows and not a herd. अतरुण: वत्सा इमे, "
        "बर्करा इमे. And अतरुण qualifies the animals rather than the herd, "
        "सामर्थ्यात् पशुविशेषणम्.\n\n"
        "SETTLED — the vārttika अनेकशफेषु adds a fifth, cloven-hoofed, "
        "keeping अश्वा इमे out. Codified."
    ),
}


def _register_ekasesa() -> None:
    for sutra, (codification, notes) in _EKASESA.items():
        register(sutra, apply=ekasesa_of, codification=codification,
                 notes=notes)


_register_ekasesa()


__all__ = [
    "KIT_PROVISIONS",
    "Recitation",
    "Word",
    "accent_of",
    "asisya",
    "ekasesa",
    "hrasva",
    "number_for",
    "yuktavat",
    "recite",
    "behaves_as",
    "aprkta",
    "combines",
    "duration",
    "karmadharaya",
    "pratipadika",
    "substitutable",
    "svarita_profile",
    "upasarjana",
]
