# Codifying the Aṣṭādhyāyī

359 of 3,983 sūtras — the whole of adhyāya 1, and eight paribhāṣās beyond it. There is a browser for it at `#astadhyayi` in the web UI —
run `python server.py` and open <http://localhost:8000/#astadhyayi>. **Pāda 1.1 is complete** — all 75 of it — together with
1.2.27–1.2.32, 1.2.41–1.2.46 and the whole of 1.3. Run `python cli.py --astadhyayi` for the
current count, `--astadhyayi open` for what is still unresolved, and
`--astadhyayi 1.1.9` for a single entry in full.

## The method

For each sūtra, in this order:

1. **The mūla.** Two independent witnesses of the sūtrapāṭha, GRETIL and
   Vidyut, plus `data.json` as a third — collated, so a disagreement is visible
   rather than silently inherited.
2. **Everything on disk that speaks to it.** Ten sources are consulted for
   each sūtra: the Kāśikāvṛtti and its two great subcommentaries, the Nyāsa and
   the Padamañjarī; the Siddhāntakaumudī with the Tattvabodhinī and the
   Bālamanoramā; Vasu's English; Patañjali's Mahābhāṣya with Kielhorn
   locators; and Kātyāyana's vārttikas, kept as a source of their own because
   a vārttika corrects the rule rather than explaining it. A source that is
   here and silent is recorded `ABSENT`, not `PENDING` — it has been consulted.
3. **Notes**, kept in the sūtra's record and marked `SETTLED`, `OPEN` or
   `SCOPE` so that a conclusion can be told from a question.
4. **Python**, written so that the codification says what the sūtra says and
   nothing more.

The works still to be read — Sharma, Joshi & Roodbergen, the BORI Mahābhāṣya,
Benson — hold `PENDING` slots. The schema refuses a `VERIFIED` reading without
a locator, so nothing can quietly claim an authority it does not have.

## Two rules the code follows

**Derive, do not tabulate.** Nothing that a sūtra computes is written down as an
answer. vṛddhi is not the list `ā, ai, au`; it is `ā` plus whatever `aiC`
resolves to through 1.1.71 against the fourteen śivasūtras. The guṇa
correspondences that every primer prints as a table — i→e, u→o, ṛ→ar — are
computed from the Śikṣā's places of articulation by 1.1.50, and a test asserts
that no source file contains the pairing as a literal. The Laghusiddhāntakaumudī
defines the phonetic categories by pratyāhāra (`खरो विवाराः श्वासा अघोषाश्च`,
`यणोऽन्तःस्थाः`, `शल ऊष्माणः`), so `varna.py` resolves those pratyāhāras rather
than listing their members. A fault in the śivasūtras therefore surfaces in the
phonetics, which is the intent.

**Reuse what is already here.** Phoneme segmentation is `chandas.core.
scan_phonemes` — the same scanner the metre engine runs on, so grammar and
prosody cannot drift apart on what one sound is. Vowel duration for 1.1.70 comes
from the same module's vowel tables. Sūtra text, padaccheda with case and
number, anuvṛtti with its source, and adhikāra scope all come from the corpus
for all 3,983 sūtras, so a rule about how to read the text can be run over the
whole text.

## What that buys

A few places where the pieces meet and check each other:

- **1.1.50** measures "nearest" in the Śikṣā's own articulators, and reproduces
  the Kāśikā's worked cases: `cetā` (place beats measure, so i→e not i→a),
  `vāgghasati` (h→gh, because gh alone matches both *soṣman* and *nādavat*),
  and 7.3.52's c→k, j→g.
- **1.1.49, 1.1.66, 1.1.67 and 1.2.43** read a sūtra's own case marking — four
  of the seven cases. Given 6.1.77 इको यणचि, `nirdesa()` reports that इकः is
  what gets replaced and the operation falls on what precedes the aC; given
  2.1.24, that द्वितीया is the upasarjana. The traditional analyses, from the
  text. 1.2.43 is the only conditioned one — a first-case word is an upasarjana
  only in a rule that makes a compound.
- **1.3.2–1.3.9** made `Adesa.its` derivable, discharging a limitation recorded
  against 1.1.55. 1.1.5 क्ङिति च now knows क्त is *kit* because 1.3.8 says so,
  so `ci + kta` gives चितः rather than चेतः through the whole chain.
- **Three blocks are decision procedures whose branch ORDER is the rule.**
  1.1.28 relieves a prohibition 1.1.29 has not made yet; 1.1.42 must be tried
  before 1.1.43 or a neuter *śi* loses a name it already has; 1.1.59 re-admits
  reduplication that 1.1.58 excluded from what 1.1.57 allowed against what
  1.1.56 forbade. Each has a test that fails if the order is reversed.
- **The dhātupāṭha and the Gaṇapāṭha** supply what two sūtras point at rather
  than state. 1.1.20's six *ghu* roots are found by taking the it-letters off
  every root in the dhātupāṭha and keeping those shaped दा or धा, less the two
  the sūtra excludes — and the six that fall out are the six the Kāśikā names.
  1.1.27's thirty-five *sarvanāman*s are the Gaṇapāṭha's सर्वादि, which that
  text keys to this very sūtra.
- **The vārttikas**, read only after the apparatus was widened, turned up a
  restriction on 1.1.62 that the Kāśikā there does not give:
  `वर्णाश्रये नास्ति प्रत्ययलक्षणम्`. It is recorded and marked `SCOPE`,
  because the codification has no way to say that an operation is varṇa-based.
- **1.1.2 and 1.1.9** settled a question the notes first got wrong. e and ai
  share a place and an effort, so the features alone make them savarṇa — but
  then 1.1.69 would widen the aiC of 1.1.1 to include e, and vṛddhi would
  contain a guṇa vowel. The Kāśikā's enumeration says the same
  (`सन्ध्यक्षराणां ... द्वादशप्रभेदानि`, twelve *apiece*). The record carries
  the correction and the reasoning.

## Layout

| file | what it holds |
|---|---|
| `sutra.py` | the record schema — `Source`, `Status`, `Reading`, `Sutra`, the registry |
| `corpus.py` | the texts on disk: sūtrapāṭha ×2, Mahābhāṣya, 15 commentaries, 921 vārttikas, 2,259 dhātus, 5,340 attested forms |
| `sources.py` | assembles each sūtra's apparatus from the corpus; `register()` |
| `sivasutra.py` | the fourteen Māheśvara-sūtras and pratyāhāra resolution (1.1.71) |
| `varna.py` | sthāna and prayatna, derived from pratyāhāras; savarṇatva (1.1.9) |
| `grahana.py` | what a term denotes (1.1.68–1.1.71) |
| `itsamjna.py` | the indicatory letters (1.3.2–1.3.9) |
| `adesa.py` | substitution: who, by what, where (1.1.49–1.1.55, 1.1.64–1.1.67) |
| `lopa.py` | disappearance and what survives it (1.1.60–1.1.63) |
| `reading.py` | respective pairing and governing headings (1.3.10–1.3.11) |
| `pada.py` | the marks a root carries, and 1.3.12–1.3.13 |
| `atmanepada.py` | which endings a verb takes in use (1.3.14–1.3.93) |
| `kittva.py` | कित् and ङित् by atideśa (1.2.1–1.2.26) |
| `luk.py` | shortening, disappearance, and the अशिष्य five (1.2.47–1.2.57) |
| `ekasesa.py` | number, and which coordinated word remains (1.2.58–1.2.73) |
| `vipratisedha.py` | the two rules about rules — 1.4.1 एका संज्ञा, 1.4.2 परं कार्यम् |
| `nominal.py` | नदी, घि, लघु, गुरु, अङ्ग, पद, भ, and the numbers (1.4.3–1.4.22) |
| `karaka.py` | the six kārakas and हेतु (1.4.23–1.4.55) |
| `nipata.py` | निपात, उपसर्ग, गति, कर्मप्रवचनीय (1.4.56–1.4.98) |
| `vibhakti.py` | the endings, the persons, संहिता and अवसान (1.4.99–1.4.110) |
| `asiddha.py` | what a rule can see — 8.2.1–3, 6.4.22, 6.1.85–86 |
| `paribhasa.py` | 2.1.1 समर्थः पदविधिः and 3.1.94 वासरूपोऽस्त्रियाम् |
| `cases.py` | worked inputs for every sūtra's playground — most derived from the provision tables |
| `formation.py` | what those two blocks share: shapes, gaṇa runs, precedence |
| `pragrhya.py` | the vowels that refuse sandhi (1.1.11–1.1.19) |
| `samjna.py` | classes of word and affix (1.1.20–1.1.44, 1.1.73–1.1.75) |
| `avyaya.py` | the indeclinables (1.1.37–1.1.41) |
| `sthanivat.py` | when a substitute counts as what it replaced (1.1.56–1.1.59) |
| `svara.py` | vowel duration and the three accents (1.2.27–1.2.32) |
| `rules/` | one module per pāda, auto-discovered; the sūtra records live here |
| `report.py` | the status report behind `cli.py --astadhyayi` |
| `playground.py` | reads a rule's signature so a form can run it |
| `api.py` | catalogue, one sūtra's record, and the dependency graph |
| `glosses.py` | the plain-English gist and worked example for each sūtra |

Roughly 7,400 lines of source against 5,000 of tests, in 1,008 tests.

## The browser

`#astadhyayi` in the web UI lists what is codified and, for each sūtra, shows
first a **plain-English gist** — what the rule says, with every technical term
in Devanāgarī and roman together (इक् iK, गुण guṇa) and a worked form beside
it, so चि ci + क्त kta → चितः citaḥ says in one line what a paragraph does not.
Where the corpus has a sūtrārtha it is shown underneath and attributed, so a
reader can tell this project's sentence from a cited one; it covers 92 of the
95. Below that, the padaccheda with the case of every word outlined where a paribhāṣā reads it,
a form that **runs the rule**, the dependency graph, the findings, and the ten
sources with their status.

The form is not written per sūtra. `playground.py` reads each rule's signature
and builds fields from it — a string, a checkbox, a select for an enum, a boxed
group for a dataclass argument like `Adesa`. A test sweeps all 95 and fails
with the offending parameter named if any rule grows one the builder cannot
handle, so the UI cannot quietly acquire a dead panel.

A sūtra whose record still has something unresolved carries a dot in the list,
and an **eye** beside it: hover or focus and the outstanding finding appears in
full, verbatim from the record rather than paraphrased. Two of the 95 have an
OPEN question, fourteen a SCOPE note, and 79 have every finding settled. The
same principle governs the collapsed Sources panel, whose summary names what is
missing — `10 read · 3 not yet consulted · 1 unreadable · 1 silent here` — so a
shut panel cannot imply a complete apparatus.

The graph draws the three kinds of dependency differently because they are
different things: **anuvṛtti** (solid, labelled with the word carried down),
**adhikāra** (dashed, a governing heading), and **related** (dotted, a
cross-reference this project recorded rather than the grammar). Sources of
carried words sit above the sūtra, cross-references below. A filled box is a
sūtra already codified and clicking it goes there.

## Tests

The expectations are the commentaries' own worked examples wherever a
commentary supplies one — the Kāśikā's `कचटतप` and `इचुयश` sets for 1.1.9, its
nine saṃyoga words for 1.1.7, the bhāṣya's argument about anusvāra for 1.1.8.
Where a test asserts something no source states, it asserts a structural
property that a wrong table would break: that khaR and haŚ partition haL
exactly, that savarṇatva is an equivalence relation, that the two case-readings
agree across all 3,983 sūtras.

Several tests exist to show a provision is load-bearing rather than decorative.
`savarna()` takes switches that turn off the ṛ/ḷ vārttika, turn off 1.1.10, and
read the prayatnas as the Kāśikā counts them instead of as the Kaumudī does —
so a test can demonstrate that 1.1.10 rescues exactly the pairs the Kāśikā
names, and that under the other reading it rescues none.

## Known limits

Recorded in the sūtras' own notes and listed by `--astadhyayi open`:

- **Accent** is modelled (1.2.29–1.2.32) but is not folded into grahaṇa: the
  sūtrapāṭha on disk is unaccented, so widening every term to three accented
  forms would produce forms that occur nowhere in the data. The dhātupāṭha is
  the text that marks it — 667 anudātta roots, 106 svarita — and 1.3.12 reads
  exactly that mark.
- **The उच्चारणार्थ vowel** — the one that makes a consonant-final anubandha
  pronounceable — is not removed, because no rule codified here removes it. So
  डुपचष् yields पच and आनङ् yields आन. Left visible rather than stripped on
  suspicion.
- **1.1.50's अर्थतः**, nearness of meaning, needs a semantics this project does
  not have. Omitted rather than faked; `Nearness.artha` is always `None`.
- **Katre** is downloaded and unreadable — the scan was OCR'd with a Devanāgarī
  model and the English is destroyed throughout. Its slots carry `UNREADABLE`,
  a distinct status from `PENDING`, so it is not mistaken for merely unread.
  See `reference/in-copyright/README.md`.
