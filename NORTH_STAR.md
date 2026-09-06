# North Star — codifying the Aṣṭādhyāyī

This is the document to read before deciding anything. It records what we are
building, how we agreed to build it, and the decisions already made so they do
not have to be argued again. Status lives elsewhere — `python cli.py
--astadhyayi` for the count, `src/astadhyayi/README.md` for how the code is laid
out. This is for judgement calls.

---

## 1. The goal

**The complete Aṣṭādhyāyī, codified rule by rule, with every claim traceable to
a source you can check.**

Three things at once, and none of them is optional:

- **A record.** For each sūtra: the text from independent witnesses, the
  padaccheda with case and number, the anuvṛtti with its source, what each
  commentary says, and our own notes marked as settled or still open.
- **An engine.** The rule as a function that runs, so a claim about what a
  sūtra does can be tested rather than asserted.
- **A way in, for both kinds of reader.** Someone who has never seen a
  sūtra and someone who has read the Kāśikā should be able to open the same
  page and each get what they came for. The beginner needs to know what kind
  of thing they are looking at before the rule itself will mean anything; the
  scholar needs not to be told. Both should be able to click a worked input
  and watch the rule fire without knowing what to type.

Done means all 3,983. At 977 that is 24.5%. This is a long piece of work and the
pace is not the measure — the quality of each entry is.

Adhyāya 1 is complete: all 351 of it, plus eight paribhāṣās beyond it. That
matters more than the percentage suggests, because the first adhyāya is the
interpreter. Everything after it is read through 1.1.49's ṣaṣṭhī, 1.1.72's
tadantavidhi, 1.4.1's एका संज्ञा and 1.4.2's परं कार्यम्, and those are now
codified rather than assumed.

The compound section has opened on top of it — 2.1.1 to 2.1.21, the whole
अव्ययीभाव — and it is the first stretch that reads almost entirely through
what was already built. 2.1.3's प्राक् is 1.4.1's संज्ञासमावेश device for the
fourth time and is the same code; 2.1.19's संख्या is 1.1.23's and inherits the
four words that are numerals without being numbers; 2.1.1 gates every rule of
the section; 1.1.41 takes the finished compound back as an अव्यय. Almost
nothing here needed new machinery, which is the return on the first adhyāya
being done properly.

## 2. The method

Fixed at the outset, and it has not needed changing. For each sūtra, in order:

1. **The mūla.** Three witnesses to the text — GRETIL, Vidyut, and
   `data.json` — collated so a disagreement is visible rather than inherited.
2. **The commentaries.** Everything on disk that speaks to it: Kāśikā, Nyāsa,
   Padamañjarī, Siddhāntakaumudī, Tattvabodhinī, Bālamanoramā, Vasu's English,
   the Mahābhāṣya with Kielhorn locators, and Kātyāyana's vārttikas.
3. **Notes**, written into the record and marked `SETTLED`, `OPEN` or `SCOPE`.
4. **Python**, saying what the sūtra says and no more.
5. **Tests**, from the commentaries' own worked examples.

One at a time. A batch is fine when the sūtras form a unit — 1.1.56–1.1.59 have
to be read together because each is an exception to the last — but the unit is
chosen by the grammar, not by convenience.

## 3. The five rules we work by

These are the standing instructions. Each has a scar behind it. The first
four are about being right; the fifth is about being usable, and it is not
subordinate to them — a correct page nobody can read has failed at the thing
this project exists for.

### Genuine tests, not fillers

Tests exist to catch errors, so they have to be capable of failing. The
expectations are the commentaries' own worked forms wherever one exists; where
none does, a test asserts a structural property that a wrong table would break
— a partition, an equivalence relation, agreement between two modules.

*It works.* The Kāśikā's `प्राग्नये` proved I had misread एकाच् at 1.1.14 as
"having one vowel" when the gloss says "**is** one vowel". A candidate-count
test showed I was excluding दैप् at 1.1.20 by accident rather than by the rule.
The bhāṣya on 1.1.8 showed anusvāra is **not** anunāsika, which I had backwards.
A test guarding an OPEN note failed the day the question got answered, which is
exactly when it should.

Four more since, and the pattern in them is worth naming: **the dangerous bug
is the one that returns a plausible answer.**

- **Accent read without its position.** The dhātupāṭha marks roots and their
  it-letters with the same two signs, and only the one on the it is
  indicatory. `Asa~\` accents the it and gives आस्ते; `vi\Sa~` accents the
  root's own vowel and gives विशति. Read flat, the two roots are identical —
  विशति came out ātmanepada and 1.3.17 नेर्विशः had nothing left to do. The
  count was wrong by 263 entries and every one of the commentary's nine accent
  claims separated correctly once position was kept.
- **A shortcut that got the right answer for the wrong reason.** I had written
  `upasarga=False` onto 1.4.37 so that 1.4.38 would win. The output was
  correct and 1.4.1 was doing *nothing* — 1.4.38 was winning by being the only
  match. A test that the displacing rule actually displaces something caught it.
- **An over-claim about structure.** I asserted the six kāraka names stand in
  global sūtra order. They do not: 1.4.38 assigns कर्मन् before 1.4.45's
  अधिकरण. The arrangement is *pairwise* — each rule stands after the rule it
  displaces — and the corrected claim is the stronger test.
- **Six coercion bugs between a web form and a signature**, none visible from
  Python, all of which made a rule report the *wrong sūtra* rather than fail:
  an empty optional field arriving as `""` (which reads as *stated, as
  nothing*, so the rule silently missed and the answer fell to the residue
  clause); a select field arriving as an enum's value rather than its member;
  and four rules taking lists of objects no form can produce, which left them
  unreachable from the interface entirely.

Corollary: **a test that cannot fail is worse than no test**, because it reads
as coverage. Two of mine were like that and were replaced — one searched for a
word it had itself concatenated, one looked for IAST diacritics in a string that
was bilingual without them.

### DRY, religiously

Nothing a sūtra computes is written down as an answer.

The guṇa table every primer prints — i→e, u→o, ṛ→ar, ḷ→al — is computed from the
Śikṣā's places of articulation through 1.1.50, and **a test asserts no source
file contains the pairing as a literal**. vṛddhi is not the list `ā ai au`; it
is `ā` plus whatever `aiC` resolves to. The Laghusiddhāntakaumudī defines the
phonetic categories by pratyāhāra, so `varna.py` resolves those rather than
listing members — which means a fault in the śivasūtras surfaces in the
phonetics, as it should.

Reuse across the project, not only within it: phoneme segmentation is the
chandas engine's `scan_phonemes`, so grammar and metre cannot disagree about
what one sound is. 1.2.27's durations are asserted equal to what `grahana.kala`
had already been computing for 1.1.70.

Four blocks of eighty-odd sūtras each turned out to be one system apiece rather
than eighty rules, and are written as **provision tables** — the conditions
declared once, a resolver reading them, and the sūtra records, the codification
lines and the playground's worked inputs all generated from the same table. The
inputs are the sharpest case: a rule's conditions *are* what makes it fire, so
186 of the 531 curated inputs are derived, and a derived input cannot drift
from its rule. That is what gave the verification test something real to catch.

Where a sūtra names a group, the group is read and not typed:

- **कुटादि, द्युतादि, वृतादि** are contiguous runs in the dhātupāṭha between two
  ends the Kāśikā names, and both ends match in every case.
- **त्यदादि** is the tail of 1.1.27's सर्वादि gaṇa from त्यद् — which then makes
  the vārttika त्यदादीनां मिथो यद् यत् परं तत् तच्छिष्यते checkable, since
  'later' means later in that same list.
- **चादि, प्रादि, ऊर्यादि, साक्षात्प्रभृति** come from the gaṇapāṭha, and प्रादि
  turns out to be exactly the twenty-two upasargas, which is the fact 1.4.59
  rests on.
- **1.3.15's गत्यर्थ and हिंसार्थ roots** are not a list at all: the sūtra names
  them by sense and the dhātupāṭha writes the sense of every root. 321 and 157
  respectively, read off the file — which also shows the vārttika
  हसादीनामुपसंख्यानम् doing real work, since none of हस्, जल्प्, पठ् is either.

### A note on measuring reuse

Three attempts to infer the dependency graph from the code gave three
different wrong answers, and the sequence is worth keeping.

A scan of each rule's function body reported 377 gaps — and walking the
first six sūtras by hand, every one of those six was wrong: 1.1.1's set is
built as `sound_class("ā", "aiC")` at module level, so `is_vrddhi` is a bare
membership test with nothing in its body to find. Widening the scan to the
whole module then credited anything sharing a file, and had
`guna_vrddhi_blocked` reusing `guna_of`, which it never calls. Narrowing
again lost the construction-time case a second time.

**The question "does A's code use B's" is not decidable by name-matching**,
and each tuning of the matcher only moved the error. What *is* decidable is
duplication — whether the same set of sounds or words is defined twice — and
that has its own test, passing at zero.

So the dependency is declared by someone who has read the code, and the test
checks the decidable part. The wider lesson is the one already in the tests
rule: a measurement that cannot fail correctly is worse than no measurement,
because a number invites belief. 377 was quoted here for two days before the
first six sūtras were read by hand and found clean.

### What the walk found

The walk over all 395 finished, and the shape of the answer was not the
shape of the question.

**334 of the 395 are not separate implementations at all.** They sit behind
39 shared resolvers — 80 sūtras behind `pada_of_usage`, 43 behind `names_of`,
33 behind `karaka_of`, nine behind `pragrhya`. For those, reuse is not a claim
that could be false; they are the same code. Only 61 sūtras have a function of
their own, and only there can `reuses` assert anything.

That distinction had to be learned from a wrong answer. 1.1.15 declared it
reused 1.1.14 and the test passed — because the two ARE one function, so
everything either does is trivially reachable from the other. The check could
not fail for that shape. 1.1.15's branch is `if nipata and final == "o"` and
never touches 1.1.14's `_is_single_vowel`. The declaration is gone and the
test now rejects any same-function pair.

Two real duplications turned up, and both had been *noticed and documented*
rather than removed:

- `grahana.kala` and `svara.duration` were identical line for line, and
  `duration`'s own docstring said it "licenses what `grahana.kala` was
  already doing." A test asserted the two agreed. Agreement is the weaker
  claim — it can only fail after one copy has been changed and something
  built on the difference. 1.1.70 now asks 1.2.27, and the test asserts one
  answer rather than two that match.
- 1.2.50 इद्गोण्याः sliced the final ī off by hand, while 1.1.52's
  `replace_antya` — whose docstring cites 1.2.50 as its own illustration —
  sat one import away. Each knew about the other; neither called it.

The walk's other product is the reuse that must NOT happen. 1.3.9 तस्य लोपः
looks like it should go through 1.1.52, and must not: तस्यग्रहणं
सर्वलोपार्थम्, अलोऽन्त्यस्य मा भूत् — the word तस्य is there precisely to stop
अलोऽन्त्यस्य from cutting the deletion down to a final sound. डुकृञ् gives
कृ, the two-letter ḍu going entire. That is now a test, because the next
person to notice the near-duplication will be tempted to collapse it.

Of the candidates the tool raised, most were citations: a docstring naming a
sūtra as its example, harvested as though it implemented it. `udit_of` says
the Kāśikā's example is चुटू at 1.3.7 and was credited with 1.3.7. Nineteen
such were read and refused with a written reason, so the worklist reaches
zero — a list that always has leftovers is a list you stop reading.

**Standing: 49 declared edges over 36 sūtras, and two duplications removed.**

The walk paid off again immediately. Codifying 2.1.22–2.1.29 — the
तत्पुरुष section — turned up the same defect in a third place: 2.1.24
द्वितीया श्रितादिभिः names the *second* member and puts the case on the
first, but every avyayībhāva rule runs the other way, so `Pair` carried
only `second_vibhakti` and the check read a field that was never there.
A condition no pair could meet — the same shape as a test that cannot
fail. Two more of the same: `samasa_of`, the playground's entry point,
had no parameter for it, so the whole run was codified but unreachable
from the one surface a person uses; and `resolve` read the pradhāna by
asking specifically for the अव्ययीभाव heading, which would have left
every तत्पुरुष verdict with an empty one.

### The reduplication slice

Ten sūtras taken out of textual order, chosen by working backwards from
लोलुवः and मरीमृजः — the two stems 1.1.4 turns on. Reduplication is the
first operation here that *builds a new term* and then rewrites that term
alone, and the defects it produced were all of that shape.

**A field with nowhere to put something.** 6.1.2 अजादेर्द्वितीयस्य doubles
the second portion of a vowel-initial root, so material stands in *front*
of the copy. Every rule 3.1.22 admits without its vārttika is
consonant-initial, so a split modelled as (abhyāsa, rest) is right for all
of them and looks right for a long time. अटाट्य came out `ā`.

**A record that named the wrong rule.** The result reported only the rule
that *split* the stem, so a reader who ran 7.4.59 was told the answer came
by 6.1.9. Joining every rule that acted into one string then broke shared
code that parses that field as a single sūtra id. The fix was a per-sūtra
entry point onto the one mechanism — and it must report the rule that
*actually* acted, not the one that was asked about, or a counter-example
becomes indistinguishable from a worked one.

**An order the finished forms cannot show.** 7.4.66's Kāśikā states it
outright — उः अदत्वे कृते रुगादय आगमाः क्रियन्ते — and two wrong orders
both produce plausible Sanskrit. Reading 1.1.51 उरण् रपरः into it gives
मर्, which then needs a second, invented application of 7.4.60 to strip the
र् off again: two steps that cancel, arriving at the right answer by the
wrong road. ववृते settles it, having no र् at all.

**And one duplication.** 7.4.59 ह्रस्वः needs the short counterpart of a
vowel, and 1.2.47 had been carrying a nine-row table for it. Every row was
already decided elsewhere: the four diphthongs by 1.1.48 — whose docstring
says it is "computed rather than tabulated" — the five simple vowels as the
savarṇa of one mātrā (1.1.9 with 1.2.27), and ṝ → ṛ rather than ḷ by 1.1.50
breaking the tie. The table is gone.

Five more finished the run — 3.1.22 यङ्, 3.1.32 सनाद्यन्ता धातवः, 3.1.134's
अच्, 2.4.74 यङोऽचि च, 6.4.77 इयङुवङौ — and with them **1.1.4 is reached
rather than asserted**. Its `dhatu_lopa` had only ever been a flag a caller
typed in, so the condition was never tested against anything; now 2.4.74
elides the यङ् earlier in the same derivation, at the instance of the very
affix that would have strengthened the vowel, and 7.2.114 comes back
`by="1.1.4"` on its own.

लू → लोलुव and मृज् → मरीमृज, the two stems the Kāśikā lists under 1.1.4,
each through eight rules.

Two things the slice turned up that were not about reduplication at all.
6.4.77's Kāśikā says इयङुवङ्भ्यां गुणवृद्धी भवतो विप्रतिषेधेन — the
strengthening ordinarily *beats* उवङ् — so the rule had to ask 1.1.4 rather
than assume, and लोलुवः exists only because the answer is yes. And the
गणपाठ on disk already marks पचादि `open_ended`, an आकृतिगण, which is
exactly what admits a stem the grammar built to a list of thirty-six: the
fact was in the corpus and needed reading, not deciding.

**Standing: 3,983 codified (100%), 5,358 tests, 141 declared reuse edges over 111 sūtras. Every sūtra of the Aṣṭādhyāyī is codified, from 1.1.1 वृद्धिरादैच् to 8.4.68 अ अ इति. What is left is not coverage but depth.**

**THE FIRST DEPTH WORK: व्युत्पत्ति, AND WHAT ASKING FOR IT COST.** `vyutpatti.py`
answers the reverse question — given जयति, which root — and the only way the
grammar allows is to make every verb it can make and match. The dhātupāṭha on
disk is the search space, the forward engine is the maker, and the answer comes
back with the derivation attached. जयति → 01.0642 जि जये **and** 01.1096 जि
अभिभवे, two answers because the corpus reads the root twice and the grammar
cannot choose; नयति → णीञ्, the ण् that 6.1.64/65 removed before anything else
happened.

Writing it exposed four real bugs in the forward engine, all of the same kind —
a rule that was codified and asked with the wrong thing, or not asked at all:

* **2.4.72 was asked with the stem instead of the enunciation.** अद् is read
  twice, 01.0064 अदिँ बन्धने and 02.0001 अदँ भक्षणे, and both left the same
  string अद् behind — so शप् was elided for both and अदिँ came out अत्ति instead
  of अदति. `Term.enunciated` now carries the upadeśa to the rules that ask the
  corpus about it. `adiprabhrtibhyah_sapah`'s own docstring had said all along
  that a full upadeśa is looked up exactly; it had simply never been given one.
* **3.4.80 थासः से was codified and not wired**, so 3.4.79 reached थास् too and
  एधसे came out एधथे. Wired with APAVADA standing on 3.4.79's own site, which
  is the same pattern 7.1.3 and 6.1.97 already use.
* **6.1.78 and the एकादेश pair stopped at an emptied term.** 2.4.72's लुक्
  leaves शप् standing as an empty term so 1.1.62 can still see it, and both
  rules read `terms[index + 1]` and found the emptiness: या + अन्ति came out
  यााअन्ति. `_khari_ca` had looked past it from the start.

What it could NOT fix is the honest boundary, and the module states it rather
than papering over it: eight of the ten gaṇas are out of reach because their
विकरण is codified and not wired, and the reach is **read off the engine's own
rule list**, not written down — wire 3.1.77 and the sixth class joins the search
by itself. One slot can be out of reach while its paradigm is in: 7.2.81 आतो
ङितः is what makes पचेते, and without it the two आ-initial ātmanepada duals are
withheld rather than answered wrongly. Every gap is a silence, never a wrong
root: गच्छति gets no answer because 7.3.77 is codified and not wired, and it is
not handed to some other root instead.

6.3.1–6.3.139: **पाद ६.३ is complete — all 139 of it**, and it changes the
subject. 6.2 asked where the accent of a compound falls; this pāda asks what
the first member LOOKS like once a second stands after it. Seven modules, 139
rows, and one heading over all of them.

**A HEADING THAT OUTLASTS ITS OWN PĀDA'S OPERATIONS.** 6.3.1 अलुगुत्तरपदे
opens two at once and its vṛtti bounds both in a single line — **अलुगधिकारः
प्रागानङः। उत्तरपदाधिकारः प्रागङ्गाधिकारात्** — so अलुक् holds twenty-four
sūtras and उत्तरपदे holds all hundred and thirty-nine, stopping only because
6.4.1 अङ्गस्य starts. That is the fourth time in two pādas that one sūtra's two
words stop in different places, and by now it is plainly the device and not the
curiosity. The last sūtra of the pāda still says **उत्तरपद इति वर्तते**.

**THE DEFAULT IS THE OPPOSITE OF EVERY OTHER RUN SO FAR.** 6.3.1–24 are a
प्रतिषेध of 2.4.71, and 6.3.2's vṛtti says it outright — **समासे कृते
प्रातिपदिकत्वात् सुपो लुकि प्राप्ते प्रतिषेधः क्रियते**. Every ablative,
instrumental, dative, locative and genitive that survives inside a Sanskrit
compound survives by one of twenty-three rules; everywhere else the ending is
gone. So silence in that module has to mean DROPPED, not unknown, and the test
that a query no rule reaches comes back naming 2.4.71 is the one that keeps it
honest.

**AND THE GENITIVES SANSKRIT ACTUALLY KEEPS ARE ALMOST ALL VĀRTTIKAS.**
6.3.21 षष्ठ्या आक्रोशे reaches चौरस्यकुलम् and little else; वाचोयुक्तिः,
पश्यतोहरः, देवानांप्रियः, शुनःशेपः and दिवोदासः are every one of them a
vārttika on that one sūtra. Śunaḥśepa and Divodāsa are named men and no sūtra
of the Aṣṭādhyāyī reaches either. The record has to say so rather than widen
6.3.21 to cover them.

**A CLASS IS NOT AN ALTERNATIVE DESCRIPTION — IT IS ONE OF SEVERAL TRUE ONES.**
This cost two wrong tests before it was seen. पाचिका is a कोपधा feminine AND a
भाषितपुंस्कादनूङ् one; दीर्घकेशी is a स्वाङ्ग-ईकारान्त AND a भाषितपुंस्कादनूङ्.
So a query naming one class cannot be expected to reach a rule keyed to the
other, and 6.3.42 पुंवत् कर्मधारयजातीयदेशीयेषु — whose whole content is that it
beats 6.3.37–41 — has to list the five classes it lets back in rather than the
one they all also belong to. The test that its list equals exactly the union of
what those five refuse is the strong form: reach one more and it would be
granting something new, miss one and the vṛtti's walk through all five would be
incomplete.

**AND A CONDITION-PAIR CAN BE ALTERNATIVES OR A CONJUNCTION, AND THE TABLE HAS
TO KNOW WHICH.** 6.3.46 समानाधिकरणजातीययोः is a locative dvandva: EITHER an
appositional second member OR the affix जातीय, and read as a conjunction the
rule reaches nothing at all — neither महादेवः nor महाजातीयः. 6.3.55 ऋचः शे is
the opposite: शस् AND a verse's पाद, both. Modelling the two the same way is
wrong twice over, and only asking the resolver finds it.

**ONE WORD IN ONE SŪTRA SETTLES A PARIBHĀṢĀ FOR THE WHOLE PĀDA.** 6.3.50 names
यत् and अण् as affixes and लेख as a word. If naming an affix under the उत्तरपद
heading reached everything ending in it, लेख would have been redundant — so it
does not: **एतदेव लेखग्रहणं ज्ञापकम् उत्तरपदाधिकारे प्रत्ययग्रहणे
तदन्ताग्रहणस्य**. 6.3.17's vṛtti had already leaned on the fact thirty-three
sūtras earlier. And 6.3.65 shows the other half: **इष्टकादिभ्यस् तदन्तस्यापि
ग्रहणं भवति** — a WORD named here does reach what ends in it. Affix and word
are read in opposite directions under one heading.

**TWICE THE PĀDA STOPS DESCRIBING AND POINTS AT USAGE.** 6.3.109 पृषोदरादीनि
यथोपदिष्टम् and 6.3.137 अन्येषामपि दृश्यते, twenty-eight sūtras apart and the
same shape: what is attested is correct whether a rule reaches it or not. But
the vṛtti then derives पृषोदरम्, बलाहकः and जीमूतः by hand anyway. What is
unlicensed is the operation, not the form, and the record keeps both halves.

**AND THE PĀDA CLOSES BY SETTLING A CONFLICT WITH ITS OWN EARLIER SELF.**
6.3.139 संप्रसारणस्य lengthens कारीषगन्धी before पुत्र; 6.3.61 इको ह्रस्वो
would have shortened the same vowel. The vṛtti answers twice — **व्यवस्थितविभाषा
हि सा**, and then **सकृद्गतौ विप्रतिषेधे यद् बाधितं तद् बाधितम् एव**: a rule
set aside once in a conflict does not come back for a second attempt. Both
modules record it, and the test asserts that 6.3.61's own table already names
कारीषगन्धी as a word its option does not reach.

**AND ONE ANUVṚTTI LEAPS OVER A SŪTRA.** 6.3.133 is ऋचि, 6.3.134 is
**मन्त्रविषये**, and 6.3.135 opens **ऋचीति वर्तते** — carrying the verse
condition across a sūtra that does not have it. The first test written here
asserted the registers narrow monotonically; the table refuted it, and the
corrected claim is the stronger one.

**पाद ६.३ IN SUM.** 139 sūtras: twenty-four on the case ending that does not
drop, nine on आनङ् and the द्वन्द्व substitutions, twelve on a feminine wearing
a masculine's shape, fifteen replacing महत्, द्वि, हृदय, पाद and उदक, twelve
shortening and inserting मुम्, twenty-three on नञ्, सह and समान, eighteen that
would not group, and twenty-six lengthenings under संहितायाम्. Seven modules,
and every one of them defaults to *nothing happens* — which is what a pāda of
exceptions has to do.

7.1.1–7.1.103: **पाद ७.१ is complete**, and it is where the affix stops being
a thing attached and starts being a thing operated on. यु becomes अन and वु
becomes अक (7.1.1), फ ढ ख छ घ at an affix's head become आयन् एय् ईन् ईय् इय्
(7.1.2), and then twenty-five sūtras swap one case ending for another —
वृक्षैः, वृक्षाय, सर्वस्मै, कुण्डानि, अष्टौ, षट् — and seven more decline
युष्मद् and अस्मद् ending by ending. Six modules: the affix's own shape (1–8),
the case endings (9–33), the Vedic block (34–50), the augments to the ending
(51–57), नुम् (58–83), and the strong cases with the ॠ that closes the pāda
(84–103).

**AND ONE SŪTRA LETS THE WHOLE VEDIC DECLENSION OFF.** 7.1.39 सुपां सुलुक्०
allows any case ending to be replaced by any of eleven things, and two
vārttikas widen it past what it says — **सुपां सुपो भवन्ति**, **तिङां तिङो
भवन्ति** — so verbal endings go the same way. The heading round it is exact
where the rule is loose: the vṛtti opens छन्दसि at 7.1.38 and says where it
ends, **आज्जसेरसुक् इति यावत्**, and the module carries both bounds as
constants because the looseness would otherwise leak into the language.

**AND A VEDIC RULE IS ONLY INTELLIGIBLE AGAINST THE FORM THAT WAS DUE.** The
Kāśikā writes **इति प्राप्ते** after each of them — अदुह्र, *अदुहत being what
the grammar owed; वारयध्वात्, *वारयध्वम् being owed — so the module keeps an
`instead_of` column and the test asserts that every substituting Vedic rule
fills it. Recording only what the Veda has would have made the rule look
arbitrary; recording what it displaces is the rule.

**AND `of` AND `gana` NAME DIFFERENT DIMENSIONS IN ONE TABLE, WHICH BROKE
THE RESOLVER.** In the नुम् run `of` is the affix acted on and `gana` the class
of what it follows, so a row carrying both is a CONJUNCTION. Read as
alternatives — the idiom everywhere else — 7.1.81 शप्श्यनोर्नित्यम् swallowed
7.1.80 आच्छीनद्योर्नुम्, and तुदती lost the option the Kāśikā gives it. The
same shape of error as 6.4.108, found the same way: by asking the resolver
for every row's own sūtra and seeing which one answered wrong.

7.2.1–7.2.78: **पाद ७.२ is open to 7.2.78.** Four modules: the सिच् aorist's
vṛddhi (1–7), where the इट् is refused (8–34), and the इट् itself (35–78).

**AND THE LARGEST PLACE IN THE BOOK WHERE THE EXCEPTIONS COME FIRST.**
7.2.35 आर्धधातुकस्येड् वलादेः is what gives the इट् at all, and twenty-seven
sūtras before it refuse an augment that does not yet exist. So the module for
7.2.8–34 answers `iṭ` where no rule of its own is reached — the default is the
rule it was written against — and the module for 7.2.35–78 answers nothing at
all, deferring to the run stated before it. Two runs, two opposite defaults,
and each is a claim about where in the text the reader is standing.

**AND HALF OF 7.2.8–34 IS A WORD LIST WITH SENSES ATTACHED.** कष् gives कष्टम्
only of hardship and thickets and कषितं सुवर्णम् of gold; घुष् gives घुष्टा
only where nothing is declared; धृष् gives धृष्टः only of boldness. 7.2.18 is
eight forms against eight senses matched one to one, and every one of the
eight has its ordinary इट् form beside it in any other sense. The sense is not
a gloss on the rule — it is the rule, and the table has a column for it.

**AND TWO SŪTRAS NAME TEACHERS RATHER THAN SETTLING.** 7.1.74 गालवस्य gives a
भाषितपुंस्क neuter the masculine's forms in Gālava's view, and 7.2.63
भारद्वाजस्य restricts the थल्'s refusal to ऋ-final roots in Bhāradvāja's. Both
are recorded as options and neither is adopted, which is what naming a
teacher does. And 7.1.94's उशनस् has three vocatives and a fourth teacher
wanting guṇa besides — **माध्यंदिनिर्वष्टि गुणम्** — with the vṛtti choosing
none of them.

7.3.1–7.3.120: **पाद ७.३ is complete**, and it opens by qualifying the rule
पाद ७.२ closed on. 7.2.117 had given the FIRST vowel of a stem vṛddhi before a
taddhita; five sūtras take that back at once — देविका gets a plain आ, केकय
turns its य into इय, and a stem after a word-final य् or व् takes no vṛddhi at
all but an ऐ or औ put in FRONT of the semivowel: वैयाकरणः, सौवश्वः. Then four
more take even that back. Six modules: the taddhita vṛddhi and the second
member (1–31), हन् and the causal's augments (32–43), the feminine's क and the
taddhita's ठ (44–51), the gutturals (52–69), the शित् rules (70–83), the guṇa
before a सार्वधातुक (85–100), and the case ending's own augments (101–120).

**AND ONE REFUSAL IS READ AS PROOF ABOUT THE ORDER OF THE WHOLE GRAMMAR.**
7.3.22 refuses the vṛddhi to a following इन्द्र — सौमेन्द्रः — and the vṛtti
points out that no vṛddhi could have applied there anyway, इन्द्र's first vowel
being lost before the taddhita and the rest merging with what precedes. That
the refusal is stated at all is the proof: **बहिरङ्गम् अपि पूर्वोत्तरपदयोः
पूर्वं कार्यं भवति पश्चाद् एकादेशः** — each member's own operations are done
first and the merger after. Which is what makes पूर्वैषुकामशमः possible.

**AND A COUNT WAS WRONG AGAIN, AND THE TABLE SAID SO.** 7.3.59–69 reads like
one block of eleven refusals and is not: 7.3.64 ओक उचः के sits in the middle of
it and SUPPLIES the guttural, laying down ओकस् with the guṇa besides. The test
was written asserting eleven and the resolver answered ten. Same shape as the
हि rules of 6.4.101–106 and the registers of 6.3.131–136 — a stretch that looks
uniform from its numbering and is not.

**AND THE SAME LIST OF FIVE ROOTS TAKES TWO DIFFERENT AUGMENTS TWO PĀDAS
APART.** रुद्, स्वप्, श्वस्, अन्, जक्ष् take an इट् at 7.2.76 before a
वल्-initial सार्वधातुक and an ईट् at 7.3.98 before a single-sound one — and
then, at 7.3.99, an अट् instead **in Gārgya's and Gālava's view**. The DRY test
caught the list written out twice; the second module now asks the first for it,
and a test asserts they are the same object.

**AND NAMING A TEACHER DOES TWO DIFFERENT THINGS.** At 7.1.74 गालवस्य and
7.2.63 भारद्वाजस्य the naming makes the rule an OPTION in the language — both
forms stand. At 7.3.46–48 उदीचाम् does the same and the vṛtti says so outright,
**उदीचांग्रहणं विकल्पार्थम्**. But at 7.3.99 the vṛtti says the opposite:
**गार्ग्यगालवयोर्ग्रहणं पूजार्थम्**, the naming is an honour and not a dissent.
The `pratyaya_ka` module carries a `view` query for the first kind, so that
7.3.49's खट्वाका answers only a reader who asks for it.

8.3.1–8.4.68: **पाद ८.३ and ८.४ are complete, and with them अध्याय ८ —
and the Aṣṭādhyāyī.** All 3,983 sūtras are codified. Six modules: the रुँ
and the nasal and the anusvāra (8.3.1–33), the visarga (34–54), अपदान्तस्य
मूर्धन्यः (55–89), the words laid down and the ten refusals (90–119),
रषाभ्यां नो णः (8.4.1–39), and ष्टुत्व with the doubling and the close
(40–68).

**AND THE WORK ENDS BY UNDOING SOMETHING IT DID IN ITS FIRST LINE.** 8.4.68
**अ अ इति** — **एकोऽत्र विवृतः, अपरः संवृतः। तत्र विवृतस्य संवृतः
क्रियते**. The अ of अइउण् was declared OPEN so that it could count as
homogeneous with आ and the whole machinery of सवर्ण could work; the last rule
closes it again so that nothing is ever actually spoken that way —
**इह शास्त्रे कार्यार्थमकारो विवृतः प्रतिज्ञातः, तस्य तथाभूतस्यैव प्रयोगो मा
भूदिति संवृतप्रतिज्ञानम्**. The book begins by making a sound up and ends by
taking it back.

**AND THREE TEACHERS DISAGREE ABOUT ONE य् AND THREE MORE ABOUT THE
DOUBLING.** At 8.3.18–20 Śākaṭāyana lightens the य्, Śākalya drops it, and
Gārgya drops it after ओ — and the third naming is not a dissent at all:
**नित्यार्थोऽयमारम्भः। गार्ग्यग्रहणं पूजार्थम्**, the same thing 7.3.99 said of
Gārgya and Gālava, and the opposite of what the two namings before it do. At
8.4.50–52 Śākaṭāyana refuses the doubling in a cluster of three, Śākalya
everywhere, and the आचार्याः after a long vowel — and the Kāśikā gives
Śākalya's four examples back as 8.4.46's own words with the doubling gone,
which is as plain a way as it has of saying which teacher the manuscripts
follow.

**AND TWO MORE MISCOUNTS WERE CAUGHT BY THE TABLE, AS THEY HAVE BEEN ALL
ALONG.** 8.3.65's compound was written into a constant called SUNOTI_TWELVE
and names eleven; 8.4.34's was called BHA_BHU_EIGHT and names seven. Both were
found by a smoke test printing `len` beside the name, not by re-reading the
sūtra — which is the point of keeping the list as data rather than as prose.

**AND ONE COLUMN PAIR NEEDED READING THREE DIFFERENT WAYS IN ONE ADHYāYA.**
`of` and `gana` are ALTERNATIVES at 8.2.36 (seven roots OR every छ-final),
a CONJUNCTION at 8.2.46 (क्षि AND a long vowel) and at 8.3.115 (सह् AND the
सोढ् shape), and at 8.3.111 सात्पदाद्योः the two alternatives both had to go
into `of`, since two entries there are alternatives and a `gana` beside them
is not. Each of the three was found by a query returning the wrong sūtra or
none, and each is recorded in the module that holds it.

8.2.1–8.2.108: **पाद ८.२ is complete — the first pāda of the त्रिपादी, and
the one every other rule in the work is asiddha to.** Five modules: the merged
vowel's accent, the न् dropped and मतुप्'s व् (4–22), the cluster's loss and the
consonant changes (23–41), the निष्ठा's त् (42–61), क्विन् and the रुँ and अदस्
(62–81), and the प्लुत (82–108).

**AND 8.2.23's OWN VṚTTI WORKS THREE ORDERINGS AND GETS THREE DIFFERENT
ANSWERS.** संयोगान्तस्य लोपः is weighed against three other rules of the same
pāda, and 8.2.1 answers differently each time. Against 8.2.66's रुँ the loss
wins, that rule being LATER and so invisible — **रुत्वं परमप्यसिद्धत्वात्
संयोगान्तस्य लोपं न बाधते**. Against 8.2.39's जश्त्व it loses, that rule
having no other chance at all — **जश्त्वे तु नाप्राप्ते तदारभ्यत इति तस्य
बाधकं भवति**. And against the semivowel of दध्यत्र it does not arise at all,
that being बहिरङ्ग and equally unseen. One heading, three readings, and the
module holds the passage whole in a constant so that a test can assert all
three at once.

**AND HALF THE निष्ठा RUN TURNS ON A SENSE AND NOT A FORM.** शीनं घृतम् against
शीतो वायुः; समक्नौ against उदक्तमुदकं कूपात्; आद्यूनः against द्यूतम्;
निर्वाणोऽग्निः against निर्वातो वातः. Four pairs that differ in nothing but what
is meant — and the vṛtti says exactly why one of them parts: **विजिगीषया हि
तत्राक्षपातनादि क्रियते**, the dice are thrown in order to win, so द्यूत has
the wish in it and आद्यून has not.

**AND ONE COLUMN CONJOINED WHERE IT SHOULD HAVE, AND ONE WHERE IT SHOULD NOT.**
8.2.32 दादेर्धातोर्घः wants a root that begins with द् AND has a ह्; the first
draft gave it both an `of` and a `gana`, which this table reads as
ALTERNATIVES, and a bare ह् then reached it — सोढा came out with the घ् that
belongs to दग्धा. 8.2.36, four sūtras later, names seven roots AND every छ- or
श-final root besides, and there either qualification really is enough on its
own. Nothing in the shape of the two rows says which is which; only the
vṛtti does.

**AND THE PĀDA ENDS BY OPENING A HEADING THAT OUTLIVES IT.** 8.2.108
तयोर्य्वावचि संहितायाम् — **संहितायामित्येतच्चाधिकृतम्। इत उत्तरमाध्यायपरिसमाप्तेः** —
everything in पाद ८.३ and ८.४ is said of sounds in close juncture, and no
sūtra of those two pādas has to say so.

8.1.1–8.1.74: **पाद ८.१ is complete, and अध्याय ८ is open.** Three
modules: सर्वस्य द्वे and the word said twice (1–15), the three headings and the
निघात (16–50), and the rest of the निघात with the vocative that is not
there (51–74).

**AND THE ADHYĀYA OPENS ON A DOUBLING THAT IS NOT THE ONE ADHYĀYA 7 SPENT
ITSELF ON.** 6.1.1 एकाचो द्वे प्रथमस्य copies ONE syllable and 8.1.1 सर्वस्य
द्वे copies the whole word. They share a name and nothing else, and the
vṛtti settles at once what the second copy is: **के द्वे भवतः? ये शब्दतश् च
अर्थतश् च उभयथा अन्तरतमे** — nearest in sound AND in sense, both at once,
or the substitution rule would let any word stand for any other.

**AND ALMOST EVERY RULE OF THE FIRST RUN NAMES A SENSE AND NOT A FORM.**
Constancy, distribution, exclusion, filling out a metrical quarter, nearness,
envy, approval, anger, contempt, threat, distress, a sort, ease. परि doubles
only of leaving out — परिपरि त्रिगर्तेभ्यो वृष्टो देवः, and never inside a
compound, **समासे तु तेनैव उक्तत्वाद् वर्जनस्य नैव भवति**, the compounding
having said the exclusion already.

**AND THEN 8.1.28 तिङ्ङतिङः, THE RULE THE WHOLE SPOKEN LANGUAGE TURNS ON.**
A finite verb after a word that is not one loses its accent altogether —
देवदत्तः पचति. Twenty of the twenty-two sūtras that follow it in this module
exist to keep it off, and the count is asserted as a property of the table
rather than written into prose.

**AND ONE PAIR IS A REFUSAL OF A REFUSAL, WHICH THE VṚTTI WILL NOT LET PASS
AS ONE.** 8.1.36 spares a verb construed with यावत् or यथा; 8.1.37 पूजायां
नानन्तरम् takes that back where the sense is praise and the verb stands next
— and the commentary spells the double negative out rather than leave it to
be misread: **न अनुदात्तं न भवति। किं तर्हि? अनुदात्तम् एव**. The resolver needs
a displacer to outweigh a refusal for that pair alone, and a test holds the
three-way distinction: यावद् भुङ्क्ते spared, यावत् पचति शोभनम् toneless,
यावद् देवदत्तः पचति शोभनम् spared again.

**AND ONE COLUMN HAD TO BE TAKEN OUT AGAIN.** The first draft of the निघात
table gave 8.1.24 न चवाहाहैवयुक्ते its five particles in an `of` column, read as
an alternative to the word class — and the refusal then swallowed 8.1.20's
enclitic outright, since the query named युष्मद् and that matched. The five are
not what the rule is ABOUT; they are what the word is CONSTRUED WITH. They
moved to `joined`, `of` turned out to be dead across all thirty-five rows, and
the column came out. Same error as 6.4.108 and 7.1.80, caught earlier this
time by a smoke test rather than by a reader.

7.4.1–7.4.97: **पाद ७.४ is complete, and with it अध्याय ७ — all 438 sūtras
of it, and the अङ्गस्य heading opened at 6.4.1 with them.** Five modules: the
चङ् aorist's shortening and the perfect's guṇa (1–12), the अङ् aorist and the
compound's क (13–24), the vowel lengthened before य् and the क्यच् block (25–40),
दा becoming दद् and the losses of स् (41–57), and अभ्यासस्य (58–97).

**AND THE LAST HEADING OF THE ADHYĀYA IS OPENED BY A RULE THAT ALSO DOES
SOMETHING.** 7.4.58 अत्र लोपोऽभ्यासस्य drops the reduplicated copy in exactly the
environment 7.4.54–57 named — मित्सति, दित्सति, आरिप्सते — and in the same
breath opens अभ्यासस्य: **अभ्यासस्य इत्येतच् च अधिकृतं वेदितव्यम् आ
अध्यायपरिसमाप्तेः**. The अत्र is in the sūtra so the heading does NOT carry
the loss down with it — **विषयावधारणार्थम्** — which is a heading and its own
exception stated in three syllables.

**AND SEVEN SŪTRAS OF THAT HEADING WERE ALREADY CODIFIED, INSIDE THE
REDUPLICATION ITSELF.** 7.4.59, 7.4.60, 7.4.66, 7.4.82, 7.4.83, 7.4.90 and
7.4.91 have been in `dvirvacana.py` since the doubling was built, because a
reduplication that does not shorten and trim its copy produces nothing usable.
The new module names them in `CODIFIED_APART` and restates none of them, and a
test asserts both halves together cover 7.4.58 to 7.4.97 with no gap and no
overlap. A pāda read into a stretch already partly codified is not new; a stretch
whose earlier half was seven sūtras deep is, and it is why the coverage is
asserted over the heading rather than over the module.

**AND TWO SŪTRAS NAME THE SAME TWO ROOTS BEFORE THE SAME AFFIX AND DIFFER IN
NOTHING BUT WHICH PIECE THEY TOUCH.** 7.4.87 चरफलोश्च gives चर् and फल्'s COPY a
नुक् and 7.4.88 उत् परस्यातः turns the अ AFTER the copy into उ — both are true of
चञ्चूर्यते at once. The first draft let the second rule answer a question about
the copy, because the `part` column was matched one way only. It now matches
both ways: a row that names no piece must not answer a question about one.
7.4.71 and 7.4.89 are the other two that reach past the copy, and 7.4.89 goes
further still — it sets the heading itself aside, **वचनसामर्थ्याद् इह न
अभिसम्बध्यते**, since चूर्तिः has no reduplication in it at all.

**AND THE CAUSAL AORIST IS MADE BY A RULE THAT BORROWS THREE OTHERS.** 7.4.93
सन्वल्लघुनि चङ्परेऽनग्लोपे says the copy does whatever it would do before सन्,
and the vṛtti names each borrowed rule in turn — **सन्यतः इत्युक्तम्,
चङ्परेऽपि तथा**. अचीकरत्'s ई is made twice over: इ by 7.4.79 borrowed, long
by 7.4.94. Every अचीकरत्-shaped form in the language comes from those two
together, and 7.4.95's seven roots displace both at once.

6.4.1–6.4.175: **पाद ६.४ is complete, and with it अध्याय ६ — all 736 sūtras of
it.** 6.4.1 अङ्गस्य is the longest heading in the book — **अधिकारोऽयम् आ
सप्तमाध्यायपरिसमाप्तेः**, six hundred and thirteen sūtras to the end of
adhyāya 7 — so finishing this pāda does not finish the heading. Nine modules:
the lengthening (1–21), the न् dropped (23–33), शास् and the nasal (34–45),
आर्धधातुके and the losses (46–70), the अट् augment with the semivowel (71–95),
the losses that make a present tense (96–114), the ए of the perfect (115–128),
भस्य and what the weak stem loses (129–153), and इष्ठ with the प्रकृतिभाव
(154–175).

**AND ONE RULE REPLACES A VOWEL AND DELETES A SYLLABLE AT THE SAME TIME.**
6.4.120 अत एकहल्मध्येऽनादेशादेर्लिटि is why पेचुः and not पपचुः: the अ becomes
ए AND the reduplication goes, and neither happens without the other. Recording
only the vowel would leave *पपेचुः. Eight sūtras share the one operation, and
six of them exist to argue about who else gets it — 6.4.122 names four roots
the conditions would have missed and gives a DIFFERENT reason for each,
**तरतेर्गुणार्थम्, फलिभजोरादेशाद्यर्थम्, त्रपेरनेकहल्मध्यार्थम्**, so the
reasons are the content of the sūtra and not decoration on it.

**AND THE HEADING PROVES ITS OWN SCOPE THREE TIMES FROM THREE PLACES.** 6.4.1's
vṛtti does not merely state the range; it takes one rule from this pāda, one
from further on and one from 7.1, and shows a pair for each — the operation
applying, and the same operation not applying because what it would act on is
no अङ्ग: **हलः — हूतः; अङ्गस्येति किम्? निरुतम्**, and so through नामि and
अतो भिस ऐस्.

**AND A PATCH SCRIPT OF MINE TRUNCATED A REGISTRATION THAT WAS ALREADY THERE.**
6.4.22 and 6.4.77 had been codified long before this pāda was read through, and
6.4.77's `register(...)` sat AFTER the file's `__all__` line. A splice that cut
at `__all__` took it with it. The tests caught it within one run — 6.4.77 is on
three test files' lists — and it was rebuilt from `anga.py`'s own docstring,
which is the material it had been written from. Two things follow. A patch that
appends to a file must anchor on something the file will still have, and the
run's own test now asserts that both rules codified before it survive and still
carry notes of full length.

**AND ONE SŪTRA OF THE RUN IS DELIBERATELY NOT IN ITS TABLE.** 6.4.77 अचि
श्नुधातुभ्रुवाम् stays where it was, in `anga.iyan_uvan`, because it BUILDS the
form and has to ask 1.1.4 whether the strengthening that would displace it was
stopped. A table row could only have named the operation. The gap is recorded
in a constant and tested, rather than left to be noticed.

**AND A CLASS BESIDE A NAMED STEM IS SOMETIMES AN ALTERNATIVE AND SOMETIMES A
CONJUNCTION.** 6.4.101 हुझल्भ्यो हेर्धिः is a dvandva in the ablative — हु OR a
झल्-final stem. 6.4.108 नित्यं करोतेः names कृ and takes the उ-affix by
anuvṛtti — कृ AND the class. Reading the two the same way gives कुर्वः where
सुन्वः belongs, and only asking the resolver found it. The table now says which
it is, row by row.

**AND A प्रतिषेध HAD TO BE WEIGHED ABOVE A विभाषा, NOT MERELY ABOVE WHAT IT
REFUSES.** 6.4.137 न संयोगाद् वमन्तात् refuses the अ-loss of 6.4.134; 6.4.136
विभाषा ङिश्योः makes that same loss optional. Both name 6.4.134, so on पर्वणि
the resolver preferred the option and offered a form the Kāśikā does not have —
चर्मणि has no *चर्म्णि beside it. The `blocks` column means two things at once,
a supplying row naming what it replaces and a refusal naming what it holds off,
and the second has to outweigh the first. The refusal's weight was raised above
one displacement's, and 6.4.137 was given both rules it holds off rather than
only the one it is stated against. The test asks for the refusal *with* the
optional environment, which is the query that failed.

**AND THE ADHYĀYA ENDS ON A RUN THAT REVERSES HALFWAY THROUGH.** 6.4.154–162
take things away — तृ, टि, everything from a semivowel on, ten stems replaced
outright, and बहु swallowing the affix and becoming भू. Then at 6.4.163 the
word is **प्रकृत्या** and seven sūtras in a row say that the losses do NOT
happen: स्रजिष्ठः keeps its ज्, सामनः its अन्, पाणिनः its इन्. The module
carries the turn as a constant and the test asserts the stretch rather than
the census, because the half is not uniform: 6.4.170 refuses the standing and
6.4.171–173 lay words down with the loss after all. The last two sūtras are
lists of निपातन, sixteen words between them, and the adhyāya closes by naming
what no rule of it reaches.

**AND ONE DEBT CAME BACK AS A DEPENDENCY.** The भस्य run's shortfall was
written as *4.1.95 and 4.1.105 are not codified* — the इञ् and यञ् that
आग्निशर्मिः and गार्गी are built on. Both had landed with अध्याय ४ while पाद
६.४ was being read, so the test failed the moment it was written, which is
what a debt written as the exact shortfall is for. It now states the live edge
instead, and the new debt names 8.3.59 and 8.4.40 — the ष् of विदुषः and the
ञ् of राज्ञः, which this run exposes and अध्याय ८ supplies.

**AND TWO CLAIMS ABOUT SHAPE WERE REFUTED BY THE TABLE ITSELF.** The registers
of 6.3.131–136 do not narrow monotonically — 6.4.134 goes back to मन्त्र
between two verse-rules, and 6.3.135's **ऋचीति वर्तते** then reaches across it.
And the five हि rules of 6.4.101–106 are not five in a row: 6.4.104 चिणो लुक्
stands in the middle of them, about something else. Both tests were written
asserting the tidier thing, and both were rewritten to what the text says.

6.2.1–6.2.199: **पाद ६.२ is complete — all 199 of it**, and it is one
argument from end to end. 6.1.223 समासस्य had said a compound is accented on
its last syllable and 6.1.158 had silenced every other syllable of it; this
whole pāda is the exceptions, and 6.2.1's vṛtti opens by saying so —
**समासान्तोदात्तत्वापवादोऽयम् आरभ्यते**. Three modules, 199 rows.

**THE PĀDA IS TWO SCOPE-WORDS AND FIVE PLACEMENT-WORDS, AND THEY DO NOT
NEST.** पूर्वपदम् governs 6.2.1–110 and उत्तरपदम् 6.2.111 to the end of the
pāda — **आ पादपरिसमाप्तेः** — and they meet with no gap. Inside each, the
placement-words take turns: प्रकृत्या 1–63, आदिः 64–91, अन्तः 92–110 under
the first; then आदिः 111–136, प्रकृत्या 137–142, अन्तः 143–199 under the
second. And उदात्तः, said once at 6.2.64, outlives three of them and runs to
6.2.137.

**A HEADING'S TWO WORDS STOPPING IN DIFFERENT PLACES IS NOT A CURIOSITY HERE
— IT IS THE PĀDA'S DEVICE, USED THREE TIMES.** 6.2.1 बहुव्रीहौ प्रकृत्या
पूर्वपदम् splits प्रकृत्या from पूर्वपदम्; 6.2.64 आदिरुदात्तः splits आदिः
from उदात्तः — **आदिरिति प्राग् अन्ताधिकारात्। उदात्त इति प्रकृत्या भगालम्
इति यावत्**; and 6.2.111 उत्तरपदादिः splits आदिः from उत्तरपदम् —
**उत्तरपदस्येत्येतदा पादपरिसमाप्तेः। आदिरिति प्रकृत्या भगालम् इति यावत्**.
Three times the same shape, each time read off the vṛtti rather than
inferred, and each time it is what makes a rule's placement decidable from
its number alone. That is now a test: every plain rule of 6.2.111–199 must
place the accent where its own run says, and the seven that do not are
listed by name.

**AND THOSE SEVEN ARE WHERE THE PĀDA IS MOST ITSELF.** 6.2.125 आदिश्चिहणादीनाम्
repeats a word already running — **आदिरिति वर्तमाने पुनरादिग्रहणं
पूर्वपदाद्युदात्तार्थम्** — and the repetition is the whole rule: it moves
आदिः off the second member and back onto the first, once, in the middle of
twenty-six sūtras that do the opposite. 6.2.173 कपि पूर्वम् accents what
stands BEFORE the affix; 6.2.174 ह्रस्वान्तेऽन्त्यात् पूर्वम् one syllable
further back still, and its repeated पूर्वम् is a नियम that shuts 6.2.173 out
where both would reach. 6.2.175 बहोर्नञ्वत् imports four earlier rules with
one word. 6.2.199 परादिः, the pāda's last sūtra, puts the accent on the word
that FOLLOWS.

**AND TWO RULES BREAK THE ONE-ACCENT-PER-WORD RULE OUTRIGHT.** 6.1.158
अनुदात्तं पदमेकवर्जम् leaves one syllable accented and silences the rest;
6.2.140 उभे वनस्पत्यादिषु युगपत् and 6.2.141 देवताद्वन्द्वे च give both
members their own accents **युगपत्**, at the same time. वनस्पतिः carries two,
and इन्द्राबृहस्पती carries three — **बृहस्पतिशब्दे वनस्पत्यादित्वाद्
द्वावुदात्तौ, तेनेन्द्राबृहस्पती इत्यत्र त्रय उदात्ता भवन्ति**. Nowhere else
in the Aṣṭādhyāyī does one word end with three. 6.1.200's कर्तवै had already
shown the paribhāṣā can be broken by naming युगपत्; this is the same word
doing the same work eighty sūtras later, and 6.2.142 then takes most of it
back.

**A RULE CAN BE AN EXCEPTION TO ONE THAT COMES AFTER IT.** 6.2.116 नञो
जरमरमित्रमृताः carves four words out of 6.2.172 नञ्सुभ्याम्, fifty-six sūtras
further on; 6.2.117 and 6.2.119 do the same. The vṛtti says so at each —
**नञ्सुभ्याम् इत्यस्यायमपवादः** — and then says where the direction reverses:
**कपि तु परत्वात् कपि पूर्वम् इत्येतद् भवति**, 6.2.173 taking सुकर्मा back
from 6.2.117 by standing later. Priority in this pāda is argued case by case,
sometimes by विप्रतिषेध and sometimes by पूर्वविप्रतिषेध, and the table
records which on `blocks` rather than deriving it from the numbers.

**AND SIX RULES ARE WIDENED BY A SEVENTH.** 6.2.135 षट् च काण्डादीनि names
six words 6.2.126–129 had each accented under a sense-condition — contempt,
comparison, mixture, a name — and frees every one of them of that condition,
at the price of a non-living genitive in front. The vṛtti walks all four:
**काण्डं गर्हायाम् इत्युक्तम् अगर्हायामपि भवति... कूलं संज्ञायाम् इत्युक्तम्
असंज्ञायामपि भवति**. The test that matters is not that six words are listed
but that they are exactly the words those four rules named — otherwise the
walk is about something else.

**WHAT THE THIRD MODULE HAD TO LEARN THAT THE FIRST TWO DID NOT.** A rule
here names the second member by a word, a class or an affix, and the first
member by a word or a class — and *within* each side those are ALTERNATIVES
while *between* the sides they are requirements. 6.2.151 names two affixes,
four words and a gaṇa, any one of which does; 6.2.145 reaches a क्त-word
after सु and equally after a comparison; but 6.2.112 wants कर्ण in second
place AND a colour-word in first, and one without the other is a different
rule. That distinction is in `_reaches`, and getting it wrong in either
direction silently changes which sūtra answers.

**AND THE SPECIFICITY LESSON HAD TO BE RELEARNED IN A NEW PLACE.** Scoring
the columns a row FILLS rather than the columns this query MATCHED THROUGH
made 6.2.151 — three second-member columns filled — beat 6.2.117 on a query
that reached it by its affix alone, and सुकर्मा came back end-accented
instead of ādi-accented. The same fault 6.1.15 had against 6.1.30 for श्वि.
The rule is: score how the row matched, never what it holds.

**पाद ६.२ IN SUM.** 199 sūtras: sixty-three where the first member keeps
whatever accent it had, forty-seven where it is given one on its first or
last syllable, and eighty-nine where the whole question passes to the second
member. Three modules, and each is arranged the opposite way round from the
one before it — 6.2.1–63 by the word that must FOLLOW, 6.2.64–110 by the word
that must PRECEDE, 6.2.111–199 by the second member again — because that is
how Pāṇini arranged them, and a shared resolver would have had to weigh all
three the same way and would have been wrong twice.

6.1.1–6.1.223: **पाद ६.१ is complete — all 223 of it**, and it is the
longest pāda in the book. Nine modules, 213 new rows, and five
headings open over it at once.

**A HEADING CAN BE BOUNDED FROM INSIDE OR FROM OUTSIDE, AND THE PĀDA
HAS BOTH.** Every प्राक् heading of adhyāyas 4 and 5 was bounded by a
word lifted out of the rule AFTER its last, so the marker stood
outside the run. Here three are bounded by their own LAST RULE —
6.1.45's आकार by **नित्यं स्मयतेः इति यावत्**, 6.1.77's अचि by
**संप्रसारणाच्च इति यावत्**, 6.1.135's सुट् by **पारस्करप्रभृतीनि च
संज्ञायाम् इति यावत्** — and two the old way, संहिता by 6.1.158's
words and एकः पूर्वपरयोः by 6.1.112's. And the two inner ones do NOT
nest: अचि runs 77–108 and एकादेश runs 84–111, so the second opens
inside the first and closes outside it.

**AND A HEADING CAN BE A परिभाषा THAT SPEAKS FOR NO RULE OF ITS OWN.**
6.1.158 अनुदात्तं पदमेकवर्जम् — **परिभाषेयं स्वरविधिविषया** — puts no
accent anywhere. It clears every other syllable out of the way of
whichever rule speaks, and **कः पुनरेको वर्ज्यते? यस्यासौ स्वरो
विधीयते**. Four accents compete — **आगमस्य विकारस्य प्रकृतेः
प्रत्ययस्य च। पृथक्स्वरनिवृत्त्यर्थमेकवर्जं पदस्वरः॥** — and one word
cancels three.

**AND ONE RULE BREAKS THE HEADING THAT GOVERNS IT.** 6.1.200 अन्तश्च
तवै युगपत् gives कर्तवै two accents at the same time, and the vṛtti
names the reason: **युगपद्ग्रहणं पर्यायनिवृत्त्यर्थम्। एकवर्जमिति
वचनाद् यौगपद्यं न स्यात्** — without युगपत्, 6.1.158 would have made
them alternatives.

**AND ONE QUESTION IS ANSWERED THREE WAYS IN ONE PĀDA.** Whether
प्रत्ययलक्षण holds in an accent rule. 6.1.191 and 6.1.198 say yes —
**सर्वस्तोमः**, **सर्पिरागच्छ**. 6.1.197 and 6.1.199 say no —
**गर्गाः**, **पथिप्रियः**. And 6.1.204 exists only to settle it:
**एतदेव ज्ञापयति क्वचिद् इह स्वरविधौ प्रत्ययलक्षणं न भवतीति**, a rule
that would be idle if the maxim held everywhere and so proves it does
not.

**AND A MAXIM IS USED IN ONE PLACE AND DENIED IN ANOTHER.**
**स्वरविधौ व्यञ्जनमविद्यमानवत्** puts the accent on a vowel in a
consonant-final compound at 6.1.223 — and 6.1.176 names the नुट् for
the express purpose of refusing it: **अत्र च स्वरविधौ
व्यञ्जनमविद्यमानवद् इत्येषा परिभाषा नाश्रीयते नुड्ग्रहणात्**, and
**मरुत्वान्** is the form that turns on it.

**AND A PHRASE CAN HAVE FOUR CONSEQUENCES POINTING TWO WAYS.**
6.1.135's **कात् पूर्वग्रहणं सुटोऽभक्तत्वज्ञापनार्थम्**: the root is
not cluster-initial, so संस्कृषीष्ट takes neither इट् nor guṇa; but
संचस्करतुः DOES take its guṇa, by **तन्मध्यपतितस्तद्ग्रहणेन
गृह्यते**; and the accent reaches across the augment anyway, by the
maxim above; and the ट् is there for 8.3.70 to name it by.

**AND A LIST CAN BE DEFINED BY EXCLUSION.** Three आकृतिगण in one
pāda, each with the same membership rule: **अविहितलक्षणः सुट्
पारस्करप्रभृतिषु द्रष्टव्यः** at 6.1.157, **अविहितमाद्युदात्तत्वं
वृषादिषु द्रष्टव्यम्** at 6.1.203, and उञ्छादि at 6.1.160. Whatever no
rule accounts for belongs to them, so none can be closed.

**AND A CONDITION CAN FAIL BECAUSE A CORPUS HAS NO SUCH THING.**
6.1.115 wants a position inside a verse-foot, and the Yajurveda has
none: **यजुषि पादानामभावाद् अनन्तःपादार्थं वचनम्**. Five rules are
stated over again for prose for no other reason. And पाद itself is
read two ways in one pāda — a Vedic foot at 6.1.115, **न तु
श्लोकपादस्य**, and a śloka's foot as well at 6.1.134.

**AND FOUR ĀCĀRYAS ARE NAMED, THREE OF THEM FOR NOTHING.**
आपिशलि at 6.1.92, स्फोटायन at 6.1.123 and शाकल्य at 6.1.127 are each
**पूजार्थम्**, the वा having already made the rule optional. And
चाक्रवर्मण at 6.1.130 is **विकल्पार्थम्** — the name IS the option.
The distinction is invisible from the sūtras.

**पाद ६.१ IN SUM.** 223 sūtras: reduplication and what the copy is
called; thirty-two on a semivowel giving up its consonant; thirteen on
आ for a diphthong; fourteen on what is put in, put in place or taken
out; the संहिता heading and the तुक् before छ; fifty-one on one
substitute standing for two sounds; twenty where nothing happens at
all; twenty-three on an augment that never joins its root; and
sixty-six on where the one accent falls. Nine modules for one pāda,
which is more than any adhyāya before it needed.


5.4.1–5.4.160: **अध्याय ५ is complete — all 555 of it.**

**A PROHIBITION IS THE ONLY EVIDENCE THAT AN AFFIX EXISTS.** 5.4.5
forbids कन् after a past participle when a word for *half* stands by.
The vṛtti shows the prohibition to be idle — **सामिवचने
प्रतिषेधानर्थक्यम्, प्रकृत्याभिहितत्वात्** — and then reads it:
**एवं तर्हि नैवायम् अनत्यन्तगतौ विहितस्य कनः प्रतिषेधः; किं तर्हि?
स्वार्थिकस्य। केन पुनः स्वार्थिकः कन् विहितः? एतदेव ज्ञापकम् — भवति
स्वार्थे कन्निति.** No rule anywhere gives that affix, and with it
the Mahābhāṣya's own **अभिन्नतरकम्** and **बहुतरकम्** are accounted
for. A jñāpaka read out of a rule that does nothing.

**AND AN IDLE WORD GIVES A GENERAL PRINCIPLE.** 5.4.14 says *in the
feminine* where the affix it builds on is given only there:
**एतज् ज्ञापयति — स्वार्थिकाः प्रत्ययाः प्रकृतितो
लिङ्गवचनान्यतिवर्तन्तेऽपि इति** — a स्वार्थिक affix may OVERRIDE the
base's gender and number, which is why देव एव देवता is possible. And
where none overrides, the gender comes from usage anyway:
**लोकाश्रयत्वाल् लिङ्गस्य**, three times in two pādas.

**AND THE PĀDA COUNTS ITS OWN OBLIGATORY AFFIXES.** 5.4.7:
**अन्येऽपि स्वार्थिका नित्याः प्रत्ययाः स्मर्यन्ते — तमबादयः
प्राक् कनः, ञ्यादयः प्राग् वुनः, आमादयः प्राङ् मयटः,
बृहतीजात्यन्ताः समासान्ताश्चेति** — five stretches, each named by
its limits, and every one of those limits now a codified sūtra.
Three separate arguments settle whether a rule is obligatory:
**नित्यश्चायं प्रत्ययः, उत्तरत्र विभाषाग्रहणात्** (read from the
NEXT rule), the same read from the rule before, and
**द्वयोर्विभाषयोर्मध्ये नित्या विधय इति** — a rule standing BETWEEN
two optional ones is itself fixed.

**AND AN AFFIX THAT CALLS FOR A DOUBLING COMES AFTER IT.** 5.4.57:
**डाचि विवक्षिते द्विर्वचनमेव पूर्वं क्रियते, पश्चात् प्रत्ययः** —
the affix being merely WISHED FOR is enough to make the doubling
happen, and the affix itself arrives afterwards.

**AND A LOSS COUNTS AS AN ENDING.** 5.4.138: **स्थानिद्वारेण लोपस्य
समासान्तता विज्ञायते** — a removal is a compound-final through what
it stands in place of. And 5.4.139 lists its forms WITH the loss
already made, which is what confines it: **समुदायपाठस्य च प्रयोजनं
विषयनियमः.**

**AND ONE RULE'S WORD-ORDER IS A ज्ञापक.** 5.4.91 puts the longer
word first against the usual practice, **राजशब्दस्य सवर्णदीर्घार्थं
प्रथमं प्रयोगं कुर्वन्नेतद् ज्ञापयति — यस्याकारेण सवर्णदीर्घत्वं
संभवति तस्येदं ग्रहणमिति**: only what can make that long vowel is
meant, so मद्रराज्ञी is not reached.

**अध्याय ५ IN SUM.** 555 sūtras: 136 on what a thing is good for,
made for, or worth; 140 from a field of grain to the affix for HAVING
something; 119 on the affixes that add nothing; 160 more of those and
then the endings a compound takes as a compound. Eight great headings — छ,
ठञ्, ठक्, काल, त्व, विभक्ति, क, and समासान्त — and among them the
first that supplies a NAME instead of an affix, the first bounded by
अभिविधि rather than प्राक्, the first that carries a condition and no
affix at all, and the one that is stated so that its own exceptions
do NOT displace it. Four modules, 550 table rows, and the chapter is
contiguous end to end against the collation.


5.3.1–5.3.119: **अध्याय ५ पाद ३ is complete — and it opens with a
heading that supplies a NAME.**

Six headings of this project had been bounded by lifting one word out
of the rule they stop at, and every one supplied an AFFIX. 5.3.1
प्राग्दिशो विभक्तिः is bounded the same way and gives nothing:
**प्रागेतस्माद् दिक्संशब्दनाद् यानित ऊर्ध्वमनुक्रमिष्यामो
विभक्तिसंज्ञास्ते वेदितव्याः.** So the resolver has no fall-back
here, and says so instead of naming a rule.

**AND THE समर्थ HEADING LAPSES WITH IT.** **अतः परं स्वार्थिकाः
प्रत्ययाः, तेषु समर्थाधिकारः प्रथमग्रहणं च प्रतियोग्यपेक्षत्वाद्
नोपयुज्यत इति द्वयमपि निवृत्तम्** — 2.1.1 समर्थः पदविधिः has
governed since the second chapter, and it stops because a word can
only be *construed with* something and a स्वार्थिक affix adds none.
**वावचनं तु वर्तत एव**, and the option alone carries on.

**WHAT THESE AFFIXES DO, STATED TWICE.** 5.3.55: **प्रकृत्यर्थ
विशेषणं च स्वार्थिकानां द्योत्यं भवति** — they MAKE MANIFEST a
qualification the base already has. 5.3.66 says it again. And the
consequence is that the gender still comes from usage: **स्वार्थिकत्वे
ऽपि पुँल्लिङ्गता, लोकाश्रयत्वाल् लिङ्गस्य**, कुटी feminine and
कुटीर not.

**A RESTRICTION UNDONE FIVE TIMES BY SUBSTITUTION.** 5.3.58 confines
the two vowel-initial superlative affixes to quality-words. The six
rules after it apply them to प्रशस्य, वृद्ध, अन्तिक, बाढ, युवन् —
none of which is one. **आदेशविधानसामर्थ्यात् तद्विषयो नियमो न
प्रवर्तते; एवमुत्तरेष्वपि योगेषु विज्ञेयम्**: enjoining a substitute
BEFORE an affix is evidence that the affix comes. The last of them
reads it out of an elision, as 5.2.60 did.

**AND A ज्ञापक POINTED AT A COMPOUND.** 5.3.106 takes काकतालीय as
its base, and no rule makes काकताल a compound at all: **समासश्चायम्
अस्मादेव ज्ञापकात्, नह्यस्यापरं लक्षणमस्ति.** The vṛtti then takes
the proverb apart — the crow comes by chance, the palm-fruit falls by
chance, and the fruit kills the crow — and divides the two
comparisons: **तत्र प्रथमे समासः, द्वितीये प्रत्ययः**, the compound
carrying one and the affix the other.

**AND A WORD DRAGGED BACKWARD.** 5.3.12: **उत्तरसूत्राद् वावचनं
पुरस्तादपकृष्यते** — अपकर्ष, where अनुवृत्ति carries forward. The
second instance in two pādas, both from the immediately following
rule.

**AND THE CLOSING FORMULA A SEVENTH TIME.** 5.3.70 प्रागिवात्कः is
the second heading of the pāda and DOES give an affix; 5.3.95 closes
it with **प्रागिवीयस्य पूर्णोऽवधिः**, one sūtra short of its marker.

**AND THE PĀDA ENDS AS IT BEGAN.** 5.3.119 ञ्यादयस्तद्राजाः gives a
second saṃjñā, and like 5.3.1 it says where the name is USED:
**तद्राजप्रदेशाः — तद्राजस्य बहुषु० इत्येवमादयः.** A name is worth
giving only for what follows from it, and both rules of this pāda
that give one say what that is.

One new module of 123 rows, and the pāda is contiguous end to end
against the collation.


5.2.1–5.2.140: **अध्याय ५ पाद २ is complete — and it is the exact
opposite of the pāda before it.**

5.1 was seven headings deep and the question at every rule was which
affix displaced which. 5.2 opens with NONE, and runs ninety-three
sūtras without one: each rule names its own affix and its own sense,
and the senses do not run in families. A field where grain grows, a
cloth reaching the toes, a cow that calves every year, a burglar's
single house, butter churned from yesterday's milking.

**SO THE COMMENTARY CHANGES ITS WORK.** Where 5.1's vṛttis argued
about limits, 5.2's GLOSS, because nothing else will: **भवन्ति
जायन्तेऽस्मिन्निति भवनम्**; **गावस्तिष्ठन्त्यस्मिन्निति गोष्ठम्**;
**गोः पश्चाद् अनुगु**; **नानाजातीया अनियतवृत्तय उत्सेधजीविनः संघा
व्राताः**. And eight rules lay a whole FORM down rather than deriving
one, twice saying outright that the analysis offered is a courtesy:
**यथाकथंचिद् व्युत्पादयितव्यौ**.

**AND SIX RULES OF THIS PĀDA HAVE NO CONTENT BUT WHAT THEY
PRESUPPOSE.** 5.2.51 adds an augment to the ordinal affix after
कतिपय, which is not a numeral and so should never have had that
affix — **तस्मादस्मादेव ज्ञापकाद् डट् प्रत्ययो विज्ञायते**. The same
reading is made at 5.2.52 of पूग and संघ, at 5.2.57 of मास and
संवत्सर, at 5.2.40 out of a SUBSTITUTION, and at 5.2.60 out of an
ELISION: **केन पुनरध्यायानुवाकयोः प्रत्ययः? इदमेव लुग्वचनं ज्ञापकं
तद्विधानस्य** — an elision is evidence of what it elides.

**AND ONE HEADING, ARRIVING NINETY-FOUR RULES IN.** 5.2.94
तदस्यास्त्यस्मिन्निति मतुप्, the rule by which Sanskrit says a thing
HAS something — and the word इति in it fixes when it may be said at
all. A kārikā names the seven grounds: **भूमनिन्दाप्रशंसासु
नित्ययोगेऽतिशायने । संसर्गेऽस्तिविवक्षायां भवन्ति मतुबादयः ॥** —
abundance, blame, praise, constant connection, excess, contact, and
the bare wish to say *it is there*. Bare possession is not among them.

**AND अन्यतरस्याम् DOES NOT MEAN WHAT IT SAYS.** From 5.2.96 it is
carried to the end, and everywhere it GATHERS rather than chooses:
**अन्यतरस्यांग्रहणं मतुप्समुच्चयार्थं सर्वत्रैव अनुवर्तते**. So a
rule giving लच् leaves मतुप् standing beside it. At 5.2.109 the word
is stated a second time on top of the carried one, and the vṛtti
counts the result: **ततश्च आतूरूप्यं भवति**, four forms. At 5.2.136
the two affixes change places. And it stops in two places — where the
word is a settled name (**रूढिषु मतुप् पुनर्न विकल्प्यते**) and where
the sense forbids it (**न चायमर्थो मतुपि संभवति**), वत्सल meaning
affectionate and having no calf in it at all.

**AND A GAṆA DEFINED BY WHAT ITS MEMBERS DO.** 5.2.127's अर्शआदि is
an आकृतिगण, and the vṛtti gives the shape: **यत्राभिन्नरूपेण
शब्देन तद्वतोऽभिधानं तत् सर्वमिह द्रष्टव्यम्** — wherever a word
UNCHANGED IN FORM names the thing that has it, the base belongs.

**AND A RULE FRAMED TO BE READ TWO WAYS ON PURPOSE.** 5.2.110's
गाण्डीव admits गाण्डिव too: **तुल्या हि संहिता दीर्घह्रस्वयोः; उभयथा
च सूत्रं प्रणीतम्** — in continuous recitation the long and short of
that vowel cannot be told apart, so the sūtra was written to be read
either way. The Kāśikā declines to choose three more times in this
pāda — two readings of 5.2.50, four of क्षेत्रिय, six of इन्द्रिय,
**सर्वं चैतत् प्रमाणम्**.

One new module of 155 rows, and the pāda is contiguous end to end
against the collation.


5.1.1–5.1.136: **अध्याय ५ पाद १ is complete, and it is the densest
stretch of headings in the grammar.** Seven of them in 136 sūtras,
and no two of the same kind.

**A HEADING IS BOUNDED BY A SENSE AND NEVER BY AN AFFIX, AND 5.1.1
SAYS WHY.** The rule could have read *before the ठञ्*, since 5.1.18
is where छ actually stops. It does not: **अर्थोऽवधित्वेन गृहीतः, न
प्रत्ययः; तेन प्राक् ठञः छ इति नोक्तम्.** The project had four
instances of the device and no statement of the principle.

**AND NO HEADING ENDS WHERE ITS OWN NAME POINTS.** The closing
formula — **पूर्णोऽवधिः, अतः परम्…** — appears at 4.4.74, 4.4.144,
5.1.17, 5.1.71, 5.1.96 and 5.1.114. Six times. The gaps run twenty
sūtras, eight, two, one; and at 5.1.71 the gap runs the OTHER WAY,
the marker standing eight sūtras BEFORE the last rule. What is
peculiar to that heading is not that its marker and its end coincide
— it is that it REACHES its marker and takes it in, because 5.1.19
says आ and not प्राक्: **अभिविधावयमाकारः, तेनार्हत्यर्थेऽपि ठग्
भवत्येव.**

**AND TWO DEBTS COLLECTED ON THE SAME IMPORT.** 4.4.75 had bounded
यत् with a word from 5.1.5; 4.3.156 had pointed its अतिदेश at
5.1.18. Both were written as tests asserting the target was ABSENT.
**A forward अतिदेश is a stack overflow waiting for its target to
exist** — 4.3.156's borrow branch knew only destinations in अध्याय ४,
so the moment 5.1.18 arrived it would have recursed into the row
asking. It learned a third destination, chosen the way it chooses the
others: by asking which module holds the sūtra named.

**5.1.37 STATES THE ARCHITECTURE OF ITS OWN SECTION, AND THE TABLE IS
BUILT THE WAY IT SAYS.** **ठञादयस्त्रयोदश प्रत्ययाः प्रकृताः।
तेषामितः प्रभृति समर्थविभक्तयः प्रत्ययार्थाश्च निर्दिश्यन्ते** —
5.1.18–36 say WHICH AFFIX and name no sense or case at all; 5.1.37–63
say IN WHAT SENSE and FROM WHICH CASE. The rows for 5.1.19–30 had
been written with the first sense read back onto them, which broke
the moment तस्य निमित्तम् took a genitive.

**A HEADING CAN CARRY A CONDITION AND NOT AN AFFIX.** 5.1.78 कालात्
supplies nothing but the requirement that the base be a word for
time, and so stands inside the ठञ् heading without competing with it.

**AND ONE HEADING IS STATED SO THAT ITS OWN EXCEPTIONS DO NOT BEAT
IT.** 5.1.120: **अपवादैः सह समावेशार्थं वचनम्; त्वतलौ सर्वत्र भवत
एव** — प्रथिमा, पार्थवम्, पृथुत्वम् and पृथुता all stand. Every
other heading in the project is displaced by what it excepts.

**AN अपवाद CAN POINT FORWARD.** 5.1.21's vṛtti says **कनोऽपवादः**
and कन् is 5.1.22, one sūtra later. Where an exception stands
relative to its general rule does not enter into it.

**AND THE COMMENTARY REFUSES TO CHOOSE, TWICE.** 5.1.50: **सूत्रार्थ
द्वयमपि चैतद् आचार्येण शिष्याः प्रतिपादिताः। तदुभयमपि ग्राह्यम्.**
5.1.94: **उभयमपि प्रमाणम्, उभयथा सूत्रप्रणयनात्** — and there the
two readings put the base in different cases and make the derived
word name different things.

**AND THE GRAMMAR NAMES ITSELF.** 5.1.58's vṛtti: **अष्टावध्यायाः
परिमाणमस्य सूत्रस्य अष्टकं पाणिनीयम्** — a work of sūtras eight
chapters in measure is *the eight of Pāṇini*. The rule by which the
Aṣṭādhyāyī is called the Aṣṭādhyāyī, codified in the Aṣṭādhyāyī.

Seven new columns (`uttarapada`, `compounded`, `adesa`, `upadha`,
`vowels`, `usage`, `refuses`), one new module of 163 rows, and the
pāda is contiguous end to end against the collation. Sandhi in a test
substring reached its nineteenth occurrence; the heredoc ate an
escape for the tenth time.


5.1.1–5.1.30: **अध्याय ५ opens, and TWO DEBTS COLLECT ON THE SAME
IMPORT.**

4.4.75 had bounded यत् by lifting हित out of 5.1.5, and 4.3.156 had
pointed its अतिदेश forward at 5.1.18. Both were written as tests
asserting the target was ABSENT. Codifying in textual order meant
both went red at once, because a rule that points forward is pointing
at the next thing to be read.

**AND THE SECOND ONE WOULD HAVE RECURSED FOREVER.** 4.3.156's borrow
branch knew two destinations and both were in अध्याय ४, so the moment
5.1.18 existed it would have called `born_in` with the arguments that
reached 4.3.156 in the first place — the exact crash 4.3.80 produced
the day ITS target arrived. **A forward अतिदेश is a stack overflow
waiting for its target to exist.** The dispatcher learned a third
destination, chosen the way it chooses the other two: by asking which
module holds a row for the sūtra named. Every example the vṛtti gives
now resolves — नैष्किकः from 5.1.20, शत्यः from 5.1.21, साहस्रः from
5.1.27, and, because **वतिः सर्वसादृश्यार्थः**, द्विनिष्कः from
5.1.30, where the affix is not given but REMOVED.

**A HEADING IS BOUNDED BY A SENSE AND NEVER BY AN AFFIX, AND 5.1.1
SAYS SO.** The rule could have read *before the ठञ्*, since 5.1.18 is
where छ actually stops. It does not: **अर्थोऽवधित्वेन गृहीतः, न
प्रत्ययः; तेन प्राक् ठञः छ इति नोक्तम्.** So the four markers are
दीव्यति, वहति, हित and क्रीत — every one a sense a rule names. The
project had four instances of the device and no statement of the
principle; here is the statement.

**AND THE CLOSING FORMULA A THIRD TIME.** 5.1.17: **छयतोः पूर्णोऽवधिः।
इतः परमन्यः प्रत्ययो विधीयते** — after 4.4.74 of ठक् and 4.4.144 of
यत्. Three times settles it: this is how the Kāśikā closes a heading,
and the gap between a marker and a last rule is how they nest. Here
the gap is twenty sūtras, the widest yet.

**AND ONE HEADING IS BOUNDED THE OTHER WAY.** 5.1.19 opens with आ,
not प्राक्: **अभिविधावयमाकारः, तेनार्हत्यर्थेऽपि ठग् भवत्येव** — an
inclusive limit, so ठक् applies at 5.1.63 itself. And it is enjoined
INSIDE another heading as its exception, **ठञधिकारमध्ये तदपवादः ठग्
विधीयते**. Three headings in thirty sūtras, one of them nested in
another.

**AN अपवाद CAN POINT FORWARD.** My test asserted no exception
displaces a later rule; 5.1.21's vṛtti says **कनोऽपवादः** and कन् is
5.1.22, one sūtra on. Not a slip — शत is a numeral, so 5.1.22 would
take it wherever it stood, and where an exception STANDS relative to
its general rule does not enter into it.

**A WORD CAN BE UNDER TWO RULES AND CHANGE SHAPE UNDER ONLY ONE.**
नाभि is in the गवादि list, which gives यत् AND substitutes नभ; it is
also a part of the body, which gives यत् by 5.1.6 and substitutes
nothing. **गवादिषु यता सन्नियुक्तो नभभावोऽत्र न भवति** — नभ्योऽक्षः
against नाभ्यं तैलम्, and the difference is visible only in the
substitute.

**AND BEING KEPT OUT OF ONE RULE IS NOT FALLING BACK TO THE HEADING.**
5.1.19 excepts संख्या from its ठक्, and a numeral then goes to
5.1.22's कन् — not to ठञ्. The vṛtti's own ठञ् example for a numeral,
षाष्टिकम्, is one that 5.1.22 ALSO excludes. Two exclusions deep
before the heading is reached, and my test had assumed one.

Sandhi in a test substring reached its eighteenth and nineteenth
occurrences in the same file — तेन + अर्हति and तदन्तग्रहणम् + अलुकि
both swallow the independent अ.


4.4.91–4.4.144: **अध्याय ४ is complete** — all 635 of it, and the
whole taddhita section with it.

**THE SECOND HEADING CLOSES IN THE FIRST'S OWN WORDS, AND THAT
SETTLES THE SHAPE.** 4.4.144 ends the chapter with **यतः पूर्णोऽवधिः,
अतः परमन्यः प्रत्ययोऽधिक्रियते** — word for word what 4.4.74 said of
ठक्. So यत्'s marker is 5.1.5 and its last rule is 4.4.144, because
5.1.1 प्राक्क्रीताच्छः opens छ inside its range.

Twice in one pāda. **A प्राक्-heading's MARKER is where its name
points; its LAST RULE is where the next heading starts.** The block
before found that at 4.4.74 and had to treat it as a correction; this
one shows it is simply how these headings nest, and a test now
asserts the formula appears at both.

**A RULE RESTATED SO THAT ITS OWN SUCCESSOR CANNOT BEAT IT.** 4.4.116
gives अग्र the heading's own यत्, and is asked why — the heading gives
it already. **घच्छौ च इति वक्ष्यति, ताभ्यां बाधा मा भूदिति
पुनर्विधीयते**: because the NEXT rule adds घ and छ, and without the
restatement they would have displaced the यत्. So asking for that
affix on that base answers by the EARLIER rule, which is the rule
working rather than a gap — and the reachability test now says so in
those terms.

**THE LONGEST RULE OF THE PĀDA, AND EVERY WORD OF IT A CONDITION.**
4.4.125 तद्वानासामुपधानो मन्त्र इतीष्टकासु लुक् च मतोः: an affix for
BRICKS, where the first word of the mantra by which they are laid
names a quality — and the मतुप् that made that word is removed in the
same act. Four counter-examples, one for each condition, and a fifth
word restricting WHICH word of a mantra counts: **इतिकरणो नियमार्थः;
अनेकपदसंभवेऽपि केनचिदेव पदेन तद्वान् मन्त्रो गृह्यते, न सर्वेण**.

**AND A RULE WORDED FOR A STATE THAT DOES NOT YET EXIST.** 4.4.127
names मूर्धन् where it should have named मूर्धन्वत् — **मूर्धन्वत
इति वक्तव्ये मूर्ध्न इत्युक्तम्, मतुपो लुकं भाविनं चित्ते कृत्वा**,
with the coming removal of that मतुप् already in mind.

**A SENSE NARROWED BY POINTING AT THE RULE THAT WOULD OTHERWISE TAKE
IT.** 4.4.98's साधु is **प्रवीणो योग्यो वा, नोपकारकः** — skilled or
fit, not *helpful*, **तत्र हि परत्वात् तस्मै हितम् इत्यनेन विधिना
भवितव्यम्**: for *helpful* a rule in the next chapter would win by
standing later. A definition given by naming its competitor.

**AND THE COMMENTARY DOES ARITHMETIC.** 4.4.140's vārttika extends
the affix to a count of syllables, and the vṛtti works the count out
phrase by phrase — ओश्रावय four, अस्तु श्रौषट् four, यज two, ये
यजामहे five, वषट्कार two — **एष वै सप्तदशाक्षरश्छन्दस्यः**. Seventeen,
added up in the commentary.

**अध्याय ४ IN SUM.** 635 sūtras across four pādas: 178 on whose
descendant a man is, 145 on where a thing is from, 168 on what it is
made of and what is born there, 144 on what a man does by means of it.
Three great प्राक्-headings, each bounded by lifting one word out of
the rule it stops at, and the three between them cover the whole
section. Six modules, 439 table rows, and the chapter is contiguous
end to end against the collation.


4.4.61–4.4.90: **a heading's marker is not its last rule, and I had
that wrong.**

**THE CORRECTION.** 4.4.1's vṛtti bounds the ठक् heading by lifting
वहति out of 4.4.76, and I recorded the range as 4.4.1–4.4.75 — the
rule before the marker. But **4.4.75 प्राग्घिताद् यत् is itself a
heading**, standing inside that range, and 4.4.74's vṛtti closes the
account in as many words: **ठकः पूर्णोऽवधिः, अतः परमन्यः प्रत्ययो
विधीयते**. So ठक् governs 4.4.1 to 4.4.74, and the marker stands two
sūtras past its last rule.

*A heading's MARKER and its LAST RULE come apart when another heading
opens inside its range* — and nothing in the project had shown that
until now, because until now no two headings had overlapped that way.
`THAK_RUN` and `THAK_MARKER` are held separately for it, and a test
asserts the gap is two.

**AND TWO DEBTS COLLECTED IN THE SAME BLOCK.** 4.4.76 arrived — the
marker rule, which a test had been holding open by asserting it
absent. And 4.4.74 arrived — the sixth and last of the six grounds
4.4.7's kārikā named, so that verse's whole claim is now checkable:
**विधिवाक्यापेक्षं च षट्त्वम्, प्रत्ययास्तु सप्त**, and a test
counts six rules and seven affixes, every one of them beginning with
ष्.

**THREE GREAT प्राक्-HEADINGS, ONE DEVICE, AND THE THIRD LEAVES THE
CHAPTER.** 4.1.83 bounded अण् with दीव्यति out of 4.4.2; 4.4.1 bounded
ठक् with वहति out of 4.4.76; 4.4.75 bounds यत् with हित out of 5.1.5.
And 4.4.76 is a sūtra used as a boundary-post by one section and
governed by another — it marks where ठक् stops and itself gives यत्.

**A NEGATION MOVED FROM THE INSTRUMENT TO THE ACTION BECAUSE IT WAS
IDLE WHERE IT STOOD.** 4.4.83's अधनुषा is objected to as unnecessary:
**न हि धनुषा पद्य इत्युक्ते विवक्षितोऽर्थः प्रतीयते** — the words
would not convey the sense anyway. So it is re-read: **धनुष्प्रतिषेधेन
व्यधनक्रिया विशेष्यते, यस्यां धनुष्करणं न संभाव्यत इति** — it
qualifies the ACT, restricting the rule to a piercing a bow could not
do. And that DOES exclude something the first reading would not have:
चौरं विध्यति.

**TWO RULES WHOSE CONDITION IS ANOTHER TEXT'S PROHIBITION.** 4.4.71
applies at a place or hour **शास्त्रेण प्रतिषिद्धौ** — forbidden for
study — and 4.4.73 to a mendicant whose distance from the village is
laid down: **आरण्यकेन भिक्षुणा ग्रामात् क्रोशे वस्तव्यमिति
शास्त्रम्**. Grammatical rules that reach only where a different
discipline has spoken first.

**AND WORDS WHOSE MEANING IS A WHOLE DESCRIPTION.** छात्रः, from
*umbrella*: **गुरुकार्येष्ववहितः तच्छिद्रावरणप्रवृत्तश्छत्रशीलः
शिष्यश्छात्रः**, the pupil whose habit is to COVER his teacher's
faults. ऐकान्यिकः, the student who slipped once at his examination —
and 4.4.64's vṛtti says what counts as a slip: **उदात्ते कर्तव्ये यो
ऽनुदात्तं करोति**. पद्यः कर्दमः, mud **नातिद्रवो नातिशुष्कः**, of just
the consistency to take a footprint. And धेनुष्या, the cow made over
to a creditor in place of interest, for him to milk.

**A LINE BREAK INSIDE A DEVANĀGARĪ WORD, THIRD TIME — AND THIS ONE WAS
THE NOTE'S FAULT.** प्रवृत्तश्छत्रशीलः was wrapped after प्रवृत्तश्,
so the phrase in the note was not the phrase in the text. **A word
ending in a virāma is mid-word when a consonant follows**: प्रवृत्तः +
छत्रशीलः is one word after sandhi and cannot be split at the join.
Rewrapped. And a wrong cross-reference of my own: 4.4.81 repeats
**4.3.124**, not 4.4.124, which does not exist — a number that looked
plausible because the pāda has 144 sūtras, and needed checking against
the registry rather than against memory.


4.4.31–4.4.60: **a verse's count comes true, and a name reaches its
synonyms.**

**THE KĀRIKĀ AT 4.4.7 CORRECTED ITSELF, AND 4.4.31 IS WHY.** That
verse counted the ष-initial affixes of the section at six and then
said **विधिवाक्यापेक्षं च षट्त्वम्, प्रत्ययास्तु सप्त** — six as far
as the rule-STATEMENTS go, seven affixes. 4.4.31 कुसीददशैकादशात्
ष्ठन्ष्ठचौ is the statement that gives two. Five of the six grounds
are now codified and a test asserts each gives an affix beginning with
ष्; the sixth, आवसथ, is written as the exact shortfall.

**A NAME REACHES ITS SYNONYMS AND ITS SPECIES.** 4.4.35: **स्वरूपस्य
पर्यायाणां तद्विशेषाणां च ग्रहणमिहेष्यते** — the word itself, the
words that mean the same, and the words for KINDS of the thing. So
पक्षिन् gives पाक्षिकः by itself, **शाकुनिकः** by a synonym, and
मायूरिकः and तैत्तिरिकः by species. Three words in the rule and a
whole vocabulary of hunters and fishermen out of them.

**TWO IDIOMS THE VṚTTI HAS TO EXPLAIN, BECAUSE NO DERIVATION COULD.**
4.4.46 makes लालाटिकः and कौक्कुटिकः, and the meanings are nowhere in
the parts. **सर्वावयवेभ्यो ललाटं दूरे दृश्यते** — of all the parts of
a man the forehead is what is seen from farthest off, so *one who
looks at the forehead* is the servant who keeps his distance,
**स्वामिनः कार्येषु नोपतिष्ठते**. And the hen's word stands for a
hen's stride: **देशस्याल्पतया हि भिक्षुरविक्षिप्तदृष्टिः
पादविक्षेपदेशे चक्षुः संयम्य गच्छति**, the monk who walks watching the
small patch his foot will fall on.

**TWO SENSES THE FORMS CANNOT TELL APART, DIVIDED BY HOW THE WORLD
WORKS.** 4.4.47 gives the affix for what is DUE and 4.4.50 for RENT,
with the same affix, the same case, and the same four examples.
**नन्ववक्रयोऽपि धर्म्यमेव? नैतदस्ति; लोकपीडया धर्मातिक्रमेणाप्यवक्रयो
भवति** — rent can be exacted to the people's hurt and in defiance of
right, and that is the whole of what separates them. A test asserts
the affixes really are identical, which is what made the argument
necessary.

**AND ONE WORD MADE TWICE IN TWO SENSES.** धानुष्कः comes at 4.4.12
from an entry read as a compound and as its members, meaning one who
LIVES by the bow; and again at 4.4.57 meaning one who FIGHTS with it.
Two rules, one form, forty-five sūtras apart.

**A QUALIFIER ABSORBED INTO THE DERIVED WORD.** 4.4.51: **पण्यमिति
विशेषणं तद्धितवृत्तावन्तर्भूतम्, अतः पण्यशब्दो न प्रयुज्यते** — the
word *wares* is taken up into आपूपिकः and is not said beside it.
4.4.55 says the same of *craft*, and adds that the drum's name there
stands for the PLAYING of it: **मृदङ्गवादने वर्तमानो मृदङ्गशब्दः
प्रत्ययमुत्पादयति**.

**THREE TERMS OF PHILOSOPHY FIXED BY USAGE AND NOT BY DEFINITION.**
4.4.60 makes आस्तिक, नास्तिक and दैष्टिक, and the vṛtti refuses the
easy reading: **न च मतिसत्तामात्रे प्रत्यय इष्यते** — not merely
having an opinion. **परलोकोऽस्तीति यस्य मतिरस्ति, स आस्तिकः**;
**प्रमाणानुपातिनी यस्य मतिः स दैष्टिकः**. And the ground of all of it
is **तदेतदभिधानशक्तिस्वभावाल् लभ्यते**, the nature of what the words
can denote — not anything the rule itself says.

**AND FOUR CASE-RELATIONS IN SIXTY SŪTRAS.** The instrumental for a
means, the accusative from 4.4.28 for what one moves along, the
genitive from 4.4.47 for what is due, the nominative from 4.4.51 for
what a man deals in. Each is spoken in its own words at the rule that
opens it — and a test of mine that had split the pāda in two on the
first change was rewritten to say that instead, which is the third
time this session a census has had to become a property.


4.4.1–4.4.30: **the second great heading, and the join where the two
meet.**

**प्राग्वहतेष्ठक् IS THE COUNTERPART OF प्राग्दीव्यतोऽण्, AND THEY
MEET AT ONE SŪTRA.** 4.1.83 put अण् over the taddhita section up to
the rule that names दीव्यति; 4.4.1 puts ठक् over everything from here
to the rule that names वहति. **प्रागेतस्माद् वहतिसंशब्दनाद्
यानर्थाननुक्रमिष्यामः, ठक् प्रत्ययस्तेष्वधिकृतो वेदितव्यः.** Each
boundary is set by lifting ONE WORD out of the sūtra it stops at —
दीव्यति out of 4.4.2, वहति out of 4.4.76 — so the two are the two
halves of a single division, and 4.1.83's boundary rule is now
codified: a citation the project has carried since the patronymics can
be checked from both sides at last.

**AND THE SENSES BECOME ACTIONS.** 4.1 asked whose descendant a man
was, 4.2 and 4.3 where a thing came from and what it was made of. From
4.4.2 the question is what someone DOES by means of the thing — plays
with it, digs with it, crosses by it, lives by it, carries by it. The
base stands in the instrumental and the affix reports the means, and
the vṛtti says so in as many words: **क्रियाप्रधानत्वेऽपि चाख्यातस्य
तद्धितः स्वभावात् साधनप्रधानः** — though a finite verb foregrounds
the ACTION, a taddhita by its nature foregrounds the MEANS.
अक्षैर्दीव्यति is a sentence about playing; **आक्षिकः** is a word
about the dice.

**A NEW SHAPE FOR THE MATCHER: STRICT WHERE THE OTHERS ARE LOOSE.**
Every rule of this pāda names its own action and only the heading does
not, so a query that names no action is asking after the heading. The
`sense` column therefore matches strictly here, where the sense-tables
of 4.2 and 4.3 match loosely — and that is what makes
प्राग्वहतेष्ठक् executable rather than decorative.

**AN AFFIX A WORD MAY NOT BE USED WITHOUT.** 4.4.20's नित्यम् is not
the ordinary *always*: **नित्यग्रहणं स्वातन्त्र्यनिवृत्त्यर्थम्; तेन
त्र्यन्तं नित्यं मप्प्रत्ययान्तमेव भवति, विषयान्तरे न
प्रयोक्तव्यम्** — a stem ending in 3.3.88's क्त्रि may not be used
ANYWHERE without this affix. Not a rule about when an affix comes but
about a word that cannot stand alone, and **कृत्रिमम्** is what it
makes.

**ONE HOMONYM RESOLVED TWO OPPOSITE WAYS, TWENTY SŪTRAS APART.**
4.4.18's कुटिलिका means both a crooked movement and a smith's iron
rod, and BOTH readings take the affix — **कौटिलिको मृगः**, the deer
that carries off the hunter by swerving, and **कौटिलिकः कर्मारः**, the
smith who draws the coals. 4.4.24's लवण means both the substance salt
and the quality of saltiness, and only one of them causes the elision:
**द्रव्यवाची लवणशब्दो लुकं प्रयोजयति, न गुणवाची**. Where one rule
takes both senses, the other splits on which is meant.

**AND A KĀRIKĀ THAT CORRECTS ITS OWN COUNT.** 4.4.7 counts the
ष-initial affixes of the whole section — **षितः षडेते ठगधिकारे**,
six of them — and then: **विधिवाक्यापेक्षं च षट्त्वम्, प्रत्ययास्तु
सप्त**, six as far as the rule-STATEMENTS go but seven affixes,
because one rule gives two. The six bases are held as data and three
of them are codified so far; a test asserts each of those gives an
affix beginning with ष्, and the rest will be checked as they arrive.

**AN INTRANSITIVE VERB GIVEN AN OBJECT.** 4.4.28 changes the case to
the accusative, and वृत् takes no object: ननु च वृतिरकर्मकः, तस्य कथं
कर्मणा संबन्धः? **क्रियाविशेषणमकर्मकाणामपि कर्म भवति** — what
QUALIFIES an action counts as an object even for a verb that has none.
Which is what lets the case change at all.

**AND A RULE THAT REACHES ONLY THE PARTY AT FAULT.** 4.4.30 gives its
affix for giving, but only where the giving is गर्ह्य — so
**द्वैगुणिकः** is the usurer who lends at double, and गर्ह्यमिति
किम्? **द्विगुणं प्रयच्छत्यधमर्णः**: the debtor who repays double
does nothing blameworthy and gets nothing. One transaction, two
parties, and the affix reaches one of them.


4.3.146–4.3.168: **अध्याय ४ पाद ३ is complete** — all 168, and three
quarters of अध्याय ४ with it.

**लुक् AND लुप् ARE NOT THE SAME REMOVAL, AND 4.3.167 SAYS WHERE THEY
DIFFER.** **लुकि प्राप्ते लुपो विधाने युक्तवद्भावे
स्त्रीप्रत्ययश्रवणे च विशेषः** — 4.3.163's लुक् was already available
on this ground, and लुप् is enjoined instead because under लुप्
1.2.51 makes what is left agree with the word the affix stood on and
the feminine affix is still heard. **अत्र च
व्यक्तिर्युक्तवद्भावेनेष्यते, वचनं त्वभिधेयवदेव भवति**: the GENDER
follows the original and the NUMBER follows what is denoted —
हरीतक्याः फलानि **हरीतक्यः**, feminine because the tree is, plural
because the fruits are. The clearest statement of that distinction the
project has met, and the reason the table needed a second column for
removal.

**A CONDITION STATED ABSTRACTLY AND THEN ENUMERATED.** 4.3.155 is
stated of any base ending in a ञित् affix given in these two senses,
and the vṛtti does not leave the reader to work it out: it names six
rules by number — 4.3.139, 4.3.142, 4.3.154, 4.3.157, 4.3.159,
4.3.168. Held as `NIT_AFFIX_RULES`, because the list is a claim that
can fail: a test asserts every rule named is codified, gives an affix
carrying ञ्, and gives it in one of the two senses. **A commentary
that enumerates what its own condition reaches turns a reading into
something checkable.**

**AND A QUESTION THAT ONLY THE ASKER CAN SETTLE.** 4.3.165 जम्ब्वा वा
gives अण् and 4.3.166 लुप् च takes it away, of one word, in one sense,
under one option — जाम्बवानि फलानि and जम्बूः फलम्, both correct, and
nothing in the ground distinguishes them. So the resolver gained an
`elided` parameter that FILTERS rather than ranks: a rule that removes
is not a narrower version of one that gives, and what tells them apart
is which form is being asked for.

**A THIRD अतिदेश REACHING FORWARD, THIS ONE OUT OF THE CHAPTER.**
4.3.156 क्रीतवत् परिमाणात् borrows a whole section of the fifth —
**प्राग्वतेष्ठञ् इत्यत आरभ्य ... ते विकारेऽतिदिश्यन्ते** — and
**वतिः सर्वसादृश्यार्थः**, the same words 4.2.34 used, so even
5.1.28's elision comes with it. The fifth chapter is not codified, so
the row names 5.1.18 and the answer says no more; the shortfall is
written as a test asserting that rule absent, the third such debt now
open.

**AND TWO OF THIS PĀDA'S OWN DEBTS COLLECTED THEMSELVES IN IT.**
4.3.80's target arrived at 4.3.127 and running the borrowing for the
first time found a stack overflow. 4.3.145's arrived at 4.3.160, and
the two rules now divide one word between them: गो takes मयट् for dung
and यत् for a modification, and the sense is the whole of what
separates them.

**A FRUIT IS BOTH A PART AND A MODIFICATION.** 4.3.163: **फलितस्य
वृक्षस्य फलमवयवो भवति विकारश्च, पल्लवितस्येव पल्लवः** — as a shoot is
of what has shot. Which is why 4.3.135 could make one rule of the two
senses at once, and why one rule here can be stated of both.

**THE PĀDA IN SUM.** 168 rules, 186 rows. Six case-relations, each
opened by a rule that names it. Two pairs of headings deliberately
overlapped, in the same words both times. Two ranges for one word,
bounded the two different ways. Five योगविभाग for two purposes. Two
प्रतिषेध, each naming what it withholds. Three अतिदेश, one reaching
back and running, two reaching forward — of which one has now been
paid.


4.3.121–4.3.145: **a debt collects itself and finds a real fault, and
the same formula appears twice in one pāda.**

**4.3.127 ARRIVED, AND RUNNING THE BORROWING BROKE IT.** 4.3.80
गोत्रादङ्कवत् reaches forward to that rule, and while it was
uncodified the branch returned early and the test held the shortfall
open by asserting the target absent. Codifying it turned the test red
— and the borrowing then **recursed until the stack gave out**, because
4.3.80 was asking under its own sense and case and so matched itself.
The `borrow_query` column added for 4.3.100 was exactly what it
lacked. *A debt written as the exact shortfall does not merely fill
in; it runs the code that was never run.*

**AND WHAT COMES BACK IS NOT THE AFFIX THE RULE NAMES.** 4.3.80 says
अङ्कवत् and so points at 4.3.127, which gives अण् from a base ending
in अञ्, यञ् or इञ् — and its own examples, औपगवकम् and the rest, are
built on words ending in अण् already. So the rule that answers is
4.3.126 गोत्रचरणाद् वुञ्, which is precisely why the vṛtti insists
**तस्माद् वुञप्यतिदिश्यते नाणेव**. The test asserts the answer is
वुञ् and specifically not the अण् of the rule named.

**THE SAME FORMULA TWICE IN ONE PĀDA, WORD FOR WORD.** 4.3.135:
**विकारावयवयोर्युगपदधिकारोऽपवादविधानार्थः, कृतनिर्देशौ हि तौ** — and
4.3.66 said exactly this of भव and व्याख्यान, sixty-nine sūtras
earlier, with only the two names changed. Two headings deliberately
overlapped so their exceptions need stating once. The `also_sense`
column now carries two pairs, and a test asserts the pairs rather
than listing the rules — which is what the last block's lesson was.

**छन्दसि AND भाषा ARE ONE DIMENSION, SO `chandasi` BECAME `usage`.**
4.3.143 confines its affix to the SPOKEN language where 4.3.19–21
confined theirs to the Veda; a rule is in one register, the other, or
neither. Two booleans would let a row claim both — the same argument
that put बह्वच् and द्व्यच् in one column, and refusing to make it a
second time would have been the inconsistency.

**A REFUSAL THAT NAMES ITS TARGET BY WHAT IT INHERITS.** 4.3.130 न
दण्डमाणवान्तेवासिषु names no affix in its own words:
**गोत्रग्रहणमिहानुवर्तते, तेन वुञ्प्रतिषेधो विज्ञायते** — the
lineage-word carries into it, and that is how one knows it is
4.3.126's वुञ् that is withheld. The row therefore states the affix it
refuses, which is what every other refusing table here does, and the
answer comes by 4.3.126 carrying `blocked_by`.

**ONE OPTION DOING OPPOSITE WORK ON ONE LIST.** 4.3.141: **उभयत्र
विभाषेयम्** — for four members of पलाशादि the affix was already coming
by 4.3.140 and the option lets it go; for the rest it was not coming
and the option brings it. The same word denying and granting,
depending which entry it lands on.

**AND A RULE REACHING BACK OVER THE HEADING IT SITS INSIDE.** 4.3.145
गोश्च पुरीषे stands between विकार and अवयव and is in neither:
**पुरीषं न विकारो नाप्यवयवः, तस्येदंविषये विधानम्** — dung is neither
a modification of the cow nor a part of her, so the rule is stated in
4.3.120's sense, twenty-five sūtras back. It also names 4.3.160 as
where the other two senses will be dealt with, and a test holds that
shortfall open the way 4.3.80's was held.

**AND A GLOBAL REPLACE IN A SHARED FILE, WHICH IS EXACTLY WHAT THIS
PROJECT HAS A RULE AGAINST.** Renaming `chandasi` to `usage` in
`kala_taddhita`, I changed the key in `cases.py` with a blanket
`str.replace`. That file holds the worked inputs for EVERY module, and
eleven of the fifteen entries it touched belong to `tacchila`,
`lakara` and `stri`, whose resolvers take `chandasi` and always did.
Only four rows were mine. **A rename is scoped to a module; a
find-and-replace is scoped to a file, and the two are not the same
scope.** Reverted by walking the file and keying each line to the
sūtra it sits under.


4.3.91–4.3.120: **both halves of one instrument, and a grammar dating
its own texts.**

**TWO अतिदेश TWENTY SŪTRAS APART, POINTING OPPOSITE WAYS.** 4.3.80
गोत्रादङ्कवत् reaches ninety-seven sūtras FORWARD to 4.3.127, which is
not codified, so its answer can only name what it means. 4.3.100
जनपदिनां जनपदवत् सर्वम् reaches BACKWARD to 4.2.124, which is — so
that borrowing is executed and returns वुञ्. The two together show the
whole instrument, and a test asserts each behaves the way its target's
availability requires.

And **सर्वग्रहणं प्रकृत्यतिदेशार्थम्** — *all* is in 4.3.100 so that
the BASE is borrowed and not only the affix. In code that is handing
the other resolver a different संज्ञा, which is what `borrow_as` holds;
the vṛtti's own proof is मद्रकः, where the base has to be cut back to
मद्र before 4.2.131 can reach it.

**A PRINCIPLE OF COMPOUNDING TAUGHT BY A RULE'S OWN WORD ORDER.**
4.3.98 वासुदेवार्जुनाभ्यां वुन् puts वासुदेव first, and both
**अल्पाच्तरम्** [2.2.34] and **अजाद्यदन्तम्** [2.2.33] say अर्जुन
should have come first. Obeying neither, the rule **ज्ञापयति —
अभ्यर्हितं पूर्वं निपततीति**: the more venerated goes first. The
evidence IS the order, so the row has to preserve it — a set would have
thrown the argument away, and a test asserts the tuple.

**DIRECT PUPILS ONLY, PROVED FROM THE LISTS THEMSELVES.** 4.3.104
reaches the pupils of two teachers, and **प्रत्यक्षकारिणो गृह्यन्ते,
न तु व्यवहिताः शिष्यशिष्याः** — not pupils of pupils. कुतः?
**कलापिखाडायनग्रहणात्**: कलापी stands in the list of nine, so his own
pupils would need no rule were the reach transitive — and 4.3.108 gives
him one anyway; कठ likewise is in the list and his pupil खाडायन is read
separately in 4.3.106's. **तदेतत् प्रत्यक्षकारिग्रहणस्य लिङ्गम्** —
two redundancies that are redundant only on the wrong reading. Both
lists are held as data, and the tests check the two names really are
where the argument needs them.

**A GRAMMAR DATING ITS OWN TEXTS BY WHAT PEOPLE SAY.** 4.3.105 restricts
its affix to what an ancient sage set forth, and the exclusions are
explained by chronology: **याज्ञवल्क्यादयोऽचिरकाला इत्याख्यानेषु
वार्ता, तया व्यवहरति सूत्रकारः** — the story goes in the traditions
that Yājñavalkya and the rest are recent, and the sūtra-maker goes by
that. A grammatical rule resting openly on a dating the grammar neither
establishes nor claims to.

**MADE AGAINST DISCOVERED.** 4.3.115 उपज्ञाते and 4.3.116 कृते ग्रन्थे
stand one apart, and **उत्पादितं कृतम्, विद्यमानमेव ज्ञातम्
उपज्ञातम्** — what is made is brought into being, what is discovered
was already there. The worked example of the first is
**पाणिनीयमकालकं व्याकरणम्**, the tenseless grammar Pāṇini found out for
himself: a rule of the text describing the text.

**THE WIDEST SENSE, AND THE VṚTTI STATES ITS PRICE.** 4.3.120 तस्येदम्
— **अणादयः पञ्च महोत्सर्गाः** stand behind it — and
**षष्ठ्यर्थमात्रं तत्संबन्धिमात्रं च विवक्षितम्, यदपरं
लिङ्गसंख्याप्रत्यक्षपरोक्षादिकं तत् सर्वमविवक्षितम्**: only the
relation is meant; gender, number, whether the thing is in sight or out
of it, none of it. And even so **अनन्तरादिष्वनभिधानाद् न भवति** — the
widest sense in the section still stops where the language does not say
it, on the same ground 4.3.12 gave a hundred and eight sūtras earlier.

**A WORKED EXAMPLE THAT CAN NOW BE RUN.** `reading.yathasamkhya`, the
helper implementing 1.3.10's pairing-in-order, named 4.3.94
तूदीशलातुरवर्मतीकूचवाराड् ढक्छण्ढञ्यकः as its example long before that
rule was codified. It is codified now, as four rows, and a test runs
the helper on the rule's own bases and affixes — and on 4.3.1's two
against three, where it must return nothing.

**AND FOUR OF THIS PROJECT'S OWN TESTS WERE COUNTING.** *Assert the
property, not the census* is a rule set here long ago, and four tests
broke it in the mildest way: each named an exact set that was true of
the pāda as far as it had been read. The elision rules were four and
are five; the बहुलम् rules were one and are two; the locative was the
commonest case and now is not; the nominative was one rule and is now
eleven. Rewritten to state what stays true — that the elision run is
CONTIGUOUS, that the two बहुलम् rules refuse to enumerate where a list
would have served, and that the locative is **the only case this pāda
states twice**, which is what makes it the one that carries.

**AND SANDHI IN A TEST SUBSTRING THREE TIMES IN ONE BLOCK, TWELFTH
OVERALL.** All three the same shape, and worth naming at last: **a
final virāma is not preserved across a junction.** ज्ञातम् + उपज्ञातम्
is ज्ञातमुपज्ञातम्; अनन्तरादिषु + अनभिधानात् is
अनन्तरादिष्वनभिधानात्, where the initial अ goes instead. A search
string must not end on a virāma the next word absorbs, nor begin with a
vowel the word before absorbed.


4.3.61–4.3.90: **two headings running at once, and five case-relations
in one pāda.**

**TWO अधिकार GOVERNING SIMULTANEOUSLY, ON PURPOSE.** Every range this
project has recorded until now DISPLACED the one before it. 4.3.66's च
does not: **वाक्यार्थसमीपे चकारः श्रूयमाणः पूर्ववाक्यार्थमेव
समुच्चिनोति** — heard beside a sentence's meaning it gathers the
PREVIOUS sentence's, so भव and व्याख्यान run together. And the vṛtti
says what the overlap buys: **भवव्याख्यानयोर्युगपदधिकारोऽपवादविधानार्थः,
कृतनिर्देशौ हि तौ** — the seven exceptions after them can then be
stated once for both instead of twice.

The table has `also_sense` for it, and the column is **deliberately
worth nothing in the ranking**: a rule under two headings is not
narrower than one under a single heading, only reachable from two
directions. A test asserts that — `_how_specific` must score a
two-sense row exactly as it scores a one-sense row — and another walks
all seven exceptions asking each under either sense, which is the
economy the vṛtti claims, made checkable.

**FIVE CASE-RELATIONS, EACH OPENED BY A RULE THAT SAYS SO.** From
4.3.25 the pāda names the relation its base stands in, and over
sixty-six sūtras it names five: सप्तमी at 4.3.25 and again at 4.3.53,
प्रथमा at 4.3.52, षष्ठी at 4.3.66, पञ्चमी at 4.3.74, द्वितीया at
4.3.85. The locative is the one that carries; the other four are each
spoken in their own words.

**AN अतिदेश REACHING NINETY-SEVEN SŪTRAS FORWARD.** 4.3.80 गोत्राद्
अङ्कवत् borrows the affixes of 4.3.127, and **अङ्कग्रहणेन
तस्येदमर्थसामान्यं लक्ष्यते** — the word *brand* stands for the
general sense, **तस्माद् वुञप्यतिदिश्यते नाणेव**, so more than one
affix comes with it. That rule is not codified. The row names it and
the answer says whose affixes are meant rather than pretending to have
them, and the test writes the shortfall as an assertion that 4.3.127
is NOT in the registry — the same shape as 4.2.34's debt, which
collected itself two blocks ago.

**FIVE योगविभाग IN ONE PĀDA, FOR TWO DIFFERENT PURPOSES.** 4.3.21,
4.3.44 and 4.3.90 are उत्तरार्थ, split for the sake of what follows.
4.3.2's and 4.3.82's are the other kind: **योगविभागो
यथासंख्यनिरासार्थः** — read as one rule, two affixes against two
grounds would have paired off in order by 1.3.10 and neither would
have reached both. A test checks that consequence rather than the
label: 4.3.81 and 4.3.82 state the same ground, and each affix must
reach it.

**TWO RULES WITH IDENTICAL OUTPUTS.** 4.3.89 सोऽस्य निवासः and 4.3.90
अभिजनश्च both give स्रौघ्नः from स्रुघ्न. **निवासाभिजनयोः को विशेषः?
यत्र संप्रत्युष्यते स निवासः, यत्र पूर्वैरुषितं सोऽभिजनः** — where a
man lives now, and where his forebears lived. Nothing in the form says
which; the whole difference is in what is being reported.

**AN INSTRUMENT SPOKEN OF AS AN AGENT.** 4.3.86's द्वार:
**द्वारमभिनिष्क्रमणक्रियायां करणं प्रसिद्धम्, तदिह स्वातन्त्र्येण
विवक्ष्यते, तथा साध्वसिश्छिनत्ति** — a gate is ordinarily what one
goes out BY, and here it acts on its own, *as one says the good sword
cuts*. 1.4.54's स्वतन्त्रः कर्ता is what allows it, and this is as
plain a case as the grammar offers.

**A LIST FOLLOWED FROM USAGE AND WRITTEN NOWHERE.** 4.3.88's
इन्द्रजननादि: **आकृतिगणः प्रयोगतोऽनुसर्तव्यः, प्रातिपदिकेषु न
पठ्यते**. The project has met open lists before; this is the first
that is not written out in the गणपाठ at all. And the vṛtti then
notices that the vārttika refusing the देवासुरादि compounds need not
have been stated either, since an आकृतिगण would have settled it.

**AND A VERSE THAT OFFERS TWO WAYS OUT AND CHOOSES NEITHER.** 4.3.84
derives वैदूर्य from विदूर, and is told the stone actually comes from
Bālavāya and is only cut at Vidūra. **वालवायो विदूरं च प्रकृत्यन्तरमेव
वा / न वै तत्रेति चेद् ब्रूयाज्जित्वरीवदुपाचरेत्** — either they are
two separate bases, or, if someone insists it is not from there, let
him treat the word as he treats जित्वरी.

**A LINE BREAK INSIDE A DEVANĀGARĪ WORD, SECOND TIME.**
प्रयोगतोऽनुसर्तव्यः was wrapped after प्रयोगतो, and `unwrapped` joins
wrapped lines with a space — so the phrase in the note was not the
phrase in the text. **The avagraha carries an elided अ: it belongs to
the word after it and can never begin a line.** And sandhi in a test
substring for the eleventh time: इन्द्रजननादिः + आकृतिगणः is
इन्द्रजननादिराकृतिगणः, and the independent आ is simply not there to
search for.


4.3.31–4.3.60: **nine senses named one by one, and one word heading
two ranges.**

**काल HEADS TWO STRETCHES OF THIS PĀDA, AND EACH END IS STATED THE
OTHER WAY.** The first runs 4.3.11–24 and is bounded in ADVANCE by the
rule that opens it — **तत्र जातः इति प्रागतः कालाधिकारः**. Then 4.3.43
कालात् speaks the word afresh in a sūtra of its own and it carries to
4.3.52, an end recorded from BEHIND by 4.3.53's **कालादिति
निवृत्तम्**. One word, two ranges, and both kinds of
boundary-statement, forty sūtras apart. Held as `KALA_RUNS`, and a
test walks the ten rules of the second stretch to check each one
either states काल or names its own bases.

**यथासंख्य FAILS AND THEN RUNS, THIRTY-TWO SŪTRAS APART.** 4.3.1 named
two bases against three affixes and the vṛtti said **वैषम्यात्** — the
counts are unequal, so 1.3.10's matching cannot run and every base
takes every affix. 4.3.33 names two against two and it runs:
सिन्धु→अण्, अपकर→अञ्. The test asserts the counts, not the verdict —
the rule that fails has |bases| ≠ |affixes| and the rule that works has
one base per row.

**AN AFFIX ELIDED, AND A DIFFERENT ONE PUT IN ITS PLACE.** 4.3.34
deletes the taddhita from ten lunar mansions, so श्रविष्ठासु जातः is
just **श्रविष्ठः**. Then **लुक् तद्धितलुकि** [1.2.49] takes the
feminine affix with it — and then, for three words a vārttika adds,
**स्त्रीप्रत्ययस्य लुकि कृते गौरादित्वाद् ङीष्**: 4.1.41 supplies a
different feminine affix to the stem the deletion left. Three rules
acting in sequence on one word, and the test asks 4.1.41 directly to
confirm it still gives ङीष्.

**बहुलम् IS NOT विभाषा, AND THE TABLE KEEPS THEM APART.** 4.3.36 says
वा and 4.3.37 says बहुलम्. An option makes both forms correct wherever
it reaches; *variously* says the elision happens in some places and
not others without undertaking to say which — which is exactly why
4.3.36's vṛtti can call the three preceding rules **बहुलग्रहणस्यायं
प्रपञ्चः**, an unfolding of that one word, and the word still has work
left when they are done.

**THE WORDS DIFFER WHERE THE FACTS DO NOT.** 4.3.38 names four senses
— made there, got there, bought there, skilled there — and the
objection is that they overlap in fact: यच्च यत्र क्रीतं लब्धमपि तत्
तत्रैव भवति, **किमर्थं भेदेनोपादानं क्रियते?** The answer is the
plainest statement of the grammar's own subject the project has met:
**शब्दार्थस्य भिन्नत्वाद् वस्तुमात्रेण क्रीतं लब्धं भवति, शब्दार्थस्तु
भिद्यत एव** — as a matter of fact a thing bought is a thing got; the
meanings of the WORDS are different all the same.

**A SENSE NARROWED BY SUBTRACTING ITS NEIGHBOURS, IN BOTH
DIRECTIONS.** 4.3.41's संभूत is *fitting in*, **नोत्पत्तिः सत्ता वा,
जातभवाभ्यां गतत्वात्** — not arising and not being, because 4.3.25 has
the first and 4.3.53 has the second, and that second rule is fourteen
sūtras ahead of it. 4.3.53 then subtracts back: **सत्ता भवत्यर्थो
गृह्यते न जन्म, तत्र जातः इति गतार्थत्वात्**. Two rules dividing one
region of meaning between them, each naming the other.

**A WORD REPEATED IN ORDER TO PUSH ANOTHER OUT.** 4.3.52 तदस्य सोढम्
takes its base in the NOMINATIVE — the only rule since 4.3.25 to leave
the locative. 4.3.53 says तत्र again, and **पुनस्तत्रग्रहणं तदस्येति
निवृत्त्यर्थम्**: not because the word had lapsed but so that the last
rule's तदस्य goes. Anuvṛtti cancelled by restating what it displaced.

**AND A COMMENTARY CALLING ITS OWN RULE POINTLESS.** 4.3.39:
**प्रायभवग्रहणमनर्थकम्, तत्रभवेन कृतार्थत्वात्** — naming
*mostly-there* achieves nothing, because 4.3.53 covers it. The defence
is turned away too: अनित्यभवः प्रायभव इति चेद्, **मुक्तसंशयेन
तुल्यम्**. The rule is codified all the same, with the verdict
recorded rather than acted on — and a test confirms the two rules do
in fact return the same affix, which is what makes the verdict
checkable instead of merely reported.

**A MECHANISM ALLOWED AT ONE RULE AND NAMED AT ANOTHER.** 4.3.11 let a
word denote a time **गुणवृत्त्यापि**, figuratively, and gave
कादम्बपुष्पिकम् for it. 4.3.48's three bases are not time-words at
all, and the vṛtti names what makes them count: **कलाप्यादयः शब्दाः
साहचर्यात् काले वर्तन्ते** — by the company they keep. यस्मिन् काले
मयूराः कलापिनो भवन्ति स कलापी, the season when the peacocks have their
tail-fans. The principle and its name, thirty-seven sūtras apart.

**AND A GRAMMATICAL NUMBER EXPLAINED BY ANATOMY.** 4.3.57 puts ग्रीवा
in the plural, and the vṛtti says why: **ग्रीवाशब्दो धमनीवचनः, तासां
बहुत्वाद् बहुवचनं कृतम्** — the word names the arteries of the neck,
and there are several. Beside it 4.3.55 gives दन्त्यम्, कर्ण्यम्,
ओष्ठ्यम् — *dental*, *labial* — so a rule about what is IN a body-part
supplies the vocabulary the phoneticians describe speech with.


4.3.1–4.3.30: **the affixes of time, and then the senses come back.**

**A PROMISE MADE FIFTY-EIGHT SŪTRAS EARLIER, AND KEPT.** 4.2.93's
vṛtti said the affixes were being given by naming their bases alone
and that the senses and cases would follow — **तेषां तु जातादयोऽर्थाः
समर्थविभक्तयश्च पुरस्ताद् वक्ष्यन्ते**. 4.3.25 तत्र जातः says they
are being stated now, in nearly the same words: **अणादयो घादयश्च
प्रत्ययाः प्रकृताः, तेषामतः प्रभृत्यर्थाः समर्थविभक्तयश्च
निर्दिश्यन्ते**. So the rule names no affix — **यथाविहितम्**,
whichever was already prescribed — and its examples are the outputs of
4.2.93, 4.2.94 and 4.2.95 read off in order.

`born_in` answers it by CALLING `in_sense`. Ask it about राष्ट्र and
4.2.93's घ comes back; ask it about ग्राम and 4.2.94's य. **The
fall-through is the reuse**, and here it is the whole content of the
rule rather than an exception's reach for its उत्सर्ग.

**AND A DEBT WRITTEN AS THE EXACT SHORTFALL COLLECTED ITSELF.** 4.2.34
कालेभ्यो भववत् borrows the affixes 4.3.11 onward gives; when it was
codified those rules did not exist, so its test recorded the gap by
asserting they were NOT in the registry and the row fell to 4.1.83's
default. Writing 4.3 turned that test red. The row now names what it
borrows from and `in_sense` fetches it — मासो देवतास्य **मासिकम्**,
4.3.11's ठञ् and not the default's अण् — and because **वत्करणं
सर्वसादृश्यपरिग्रहार्थम्** the borrowing is of whatever those rules
give base by base, so प्रावृष् comes back with 4.3.17's एण्य.

**THE WALK COULD NOT SEE THE EDGE THIS CODEBASE USES MOST.** The
fall-through idiom imports the other rule's function inside the branch
that uses it, so the two modules need not import each other at load.
`scratchpad/walk.py` resolved callees only through the CALLER's own
module, so every one of those edges was invisible — **every 4.1.83
fall-through declared since 4.2.1 was declared and never validated.**
The declarations were right; the instrument was not looking. Taught to
read function-local imports, it immediately surfaced **five real
undeclared edges** that `sivasutra.resolve`'s own docstring had already
asserted — *anything that calls `resolve` is running 1.1.71* — at
1.1.45, 1.1.73, 7.3.101, 8.3.15 and 8.4.55. Nine declarations added,
two more candidates examined and refused as citations.

**यथासंख्य FAILS WHEN THE NUMBERS DO NOT MATCH.** 4.3.1 names two
bases and gives three affixes: **वैषम्याद् यथासंख्यं न भवति**, so
1.3.10's matching-in-order cannot run and each base takes all three.
4.2.80 paired seventeen with seventeen and the matching ran; two
against three pairs with nothing.

**A PRONOUN PICKING OUT ONE OF TWO AFFIXES BY HOW EACH GOT THERE.**
4.3.2's तस्मिन्: **साक्षाद् विहितः खञ् निर्दिश्यते, न
चकारानुकृष्टश्छः** — *that* reaches the affix the last rule ENJOINED,
not the one its च dragged in. Which is precisely why the table keeps
`gives` and `also_gives` apart: with all three affixes in one field
there would be nothing for the demonstrative to pick out. **The
commentary's distinction and the schema's are the same distinction.**

**A TECHNICAL TERM READ UNTECHNICALLY TO ESCAPE A PARIBHĀṢĀ.** 4.3.3
wants युष्मद् *followed by a singular*, and 1.1.63 न लुमताङ्गस्य
forbids treating an elided affix as present — so there is no such
ground. The better of the two answers offered: **नैवेदं
प्रत्ययग्रहणम्; किं तर्हि? अन्वर्थग्रहणम्** — एकवचन here is not the
name 1.4.102 gave an ending but the words read for what they mean,
*denoting one thing*. The paribhāṣā never gets a purchase.

**A NON-CARRYING SAID OUT LOUD SO THAT IT REACHES BACKWARD.** 4.3.22's
सर्वत्र cancels the Vedic heading, and the vṛtti presses: ननु च
छन्दसीति नानुवर्तिष्यते? If it simply would not have carried, why
spend a word? **सैवाननुवृत्तिः शब्देनाख्यायते प्रयत्नाधिक्येन
पूर्वसूत्रेऽपि संबन्धार्थम्** — said with deliberate extra effort so
that it reaches back and frees the PREVIOUS rule too. And its च
gathers a second अण् that is not its own: **ऋत्वणि हि तकारलोपो
नास्ति**, two affixes of identical shape told apart by what happens
beside them. **तदेवं त्रीणि रूपाणि भवन्ति**, and each of the three is
cited from a different recension — Taittirīya, Paippalāda, Śaunaka.

**AN ANUVṚTTI REPORTED WITH AN AUTHORITY.** 4.3.27: **संज्ञाधिकारं
केचित् कृतलब्धक्रीतकुशलाः इति यावद् अनुवर्तयन्ति** — SOME carry the
संज्ञा heading to 4.3.38. A range with both ends stated is not the
same thing as a range the tradition agrees on, and the row records
whose reading it is instead of adopting it.

**AND A HEADING RECORDED AS OVER FROM OUTSIDE ITSELF.** 4.3.1 opens
**देशाधिकारो निवृत्तः** before saying anything about its own rule.
Every range so far was bounded by the vṛtti of the rule that OPENED
it, saying in advance where it would stop; this one is closed by the
text that comes after. The eighth range with both ends written down
arrives three sūtras later: **तत्र जातः इति प्रागतः कालाधिकारः**.

**एकदेश IS NOT देश,** and a substring test could not tell them apart.
Checking that no rule of the new pāda carries the lapsed
country-heading, a `"deśa" in ...` matched 4.3.7's ग्रामैकदेश, *one
PART of a village*. The heading has lapsed and the syllables have not.
Asked of the whole field instead, and the collision recorded, because
it is a fact about the two rules and not an inconvenience.


4.2.118–4.2.145: **अध्याय ४ पाद २ is complete** — a hundred and
forty-five rules, and the last twenty-eight spend themselves carving
the countries out of two affixes.

**उपधा IS NOT THE FINAL, AND THE TABLE HAD TO LEARN IT.** Six rules of
this run are stated on the PENULTIMATE sound — कोपध, योपध, रोपध,
खोपध — and the sense-table had only `stem_final`. सांकाश्य does not
end in य; it ends in अ and has य before it. Storing 4.2.132's क as a
stem-final would have answered for every word ending in क, which is a
different set entirely. A new column named by the term 1.1.65 defines,
and a test that asks the wrong question and checks the rule stays
silent. The same discipline as `ending_pada` and `preceded_by` and
`stem_final` before it: **when a field would have to mean two things,
rename rather than overload.**

**A WORD READ TWICE IS A WORD THAT HAD LAPSED.** 4.2.119:
**वृद्धादिति नानुवर्तते, उत्तरसूत्रे पुनर्वृद्धग्रहणात्** — वृद्ध
stops carrying here, and the evidence offered is that the NEXT rule
names it again. Most anuvṛtti in this project has had to be inferred
from where a rule stops making sense; this is the cleanest kind of
proof there is, and it is checkable in the table: 4.2.119's row states
no वृद्ध condition and 4.2.120's states one, or the argument has no
premise.

**AN AFFIX GIVEN IN A PAIR CANNOT BE CARRIED ON ALONE.** The same
rule's second argument: **ठञ्ञिठयोः प्रकरणे ठञः केवलस्यानुवृत्तिर्न
लभ्यत इति ठञ्ग्रहणं कृतम्**. 4.2.116 and 4.2.117 gave ठञ् and ञिठ
together, so 4.2.119 has to name ठञ् itself rather than take it from
them. **What was joined in the giving cannot be split in the
carrying** — a constraint on anuvṛtti that no earlier pāda has needed
to state.

**A RULE THAT ENJOINS A SUBSTITUTE AND NO AFFIX.** 4.2.140 राज्ञः क च:
**आदेशमात्रमिह विधेयम्, प्रत्ययस्तु वृद्धाच्छ इत्येव सिद्धः**. Only
the क is this rule's; the छ was already 4.2.114's, since राजन् has आ
for its first vowel and is वृद्ध by 1.1.73. The row therefore NAMES
the rule it leans on and the resolver fetches that rule's own answer,
rather than repeating छ where it would then have to be kept in step.
The fall-through this project has used since 4.1.84, applied for the
first time to a rule that supplies nothing at all — and the test
checks the affix is 4.2.114's छ and specifically NOT 4.1.83's अण्,
because falling to the wrong place is the failure the vṛtti warns
against.

**THE MAXIM OF BUTTERMILK FOR KAUṆḌINYA.** 4.2.125's अपि:
**अपिग्रहणं किम्, यावता वृद्धात् पूर्वेणैव सिद्धम्?** —
**तक्रकौण्डिन्यन्यायेन बाधा मा विज्ञायीति समुच्चीयते**. Telling the
servants to give buttermilk to Kauṇḍinya does not cancel the milk
everyone else was already getting. And the reason the maxim was needed
is checkable: both rules give वुञ्, so whether the later REPLACES the
earlier or joins it makes no difference to any form. **A question no
form can settle, settled by argument** — and the test asserts exactly
that both affixes are the same.

**A RULE REACHING THIRTEEN SŪTRAS FORWARD TO PROTECT ITS OWN GROUND.**
4.2.124 names a district's BOUNDARY for one reason —
**बाधकबाधनार्थम्**, गर्तोत्तरपदाच्छं बाधित्वा वुञेव जनपदावधेर्भवति.
4.2.137 gives छ to a compound ending in गर्त and त्रिगर्त is one, so
the boundary is named in order that त्रैगर्तकः stands.

**LIST ENTRIES THAT ADD NOTHING WHERE THEY STAND.** 4.2.127's पाथेय
is read **सामर्थ्याददेशार्थं**, to make the word a country-word for a
rule six sūtras back; विदेह and आनर्त the other way, **अदेशार्थः
पाठः**, for the sense that is NOT a country. 4.2.133's कच्छ is there
**उत्तरार्थम्**, for the rule after it. The same list can widen one
rule and narrow another.

**AND A HEADING THAT QUALIFIES ONLY WHAT IT CAN.** 4.2.138:
**देशाधिकारेऽपि संभवापेक्षं विशेषणम्, न सर्वेषाम्** — the country-
heading stands over the rule, but अङ्ग and मगध are in its list beside
पूर्वपक्ष and उत्तमशाख, which are not places at all. A condition
applied where it fits and dropped where it cannot.

**THE SEVENTH STATED RANGE IN ONE PĀDA.** देश enters at 4.2.119
ओर्देशे and a dozen later vṛttis open with **देश इत्येव**, the last of
them on 4.2.145 — so the range has both ends stated, like the two
case-runs and the four sense-runs before it. `DESA_RUN` holds it, and
a test walks every row that carries देश and checks it lies inside.
**Seven bounded ranges in one pāda**, where the whole of अध्याय ३
offered none.

4.2.93–4.2.117: **the affix comes first and the sense afterwards.**

**THE EXACT REVERSE OF THE HUNDRED AND SEVENTEEN RULES BEFORE IT.**
4.2.93: **प्रकृतिविशेषोपादानमात्रेण तावत् प्रत्यया विधीयन्ते; तेषां
तु जातादयोऽर्थाः समर्थविभक्तयश्च पुरस्ताद् वक्ष्यन्ते** — these rules
give affixes by naming their BASES only, and the senses they carry and
the cases they attach in are stated at 4.3.53 and after. Everything
from 4.2.1 to 4.2.91 named a case and a sense and left the affix to
4.1.83; 4.2.92's शेषे is what makes the reversal possible, because
with the sense given as *whatever is left*, an affix can be supplied
before anyone has said what it will mean.

**A NEGATIVE READ AS *LIKE-BUT-NOT* RATHER THAN AS *NOT*.** 4.2.100's
अमनुष्य: **नैवायं मनुष्यप्रतिषेधः; किं तर्हि? नञिवयुक्तन्यायेन
मनुष्यसदृशे प्राणिनि प्रतिपत्तिः क्रियते** — not *not a man* but *a
living thing RESEMBLING a man*, by the principle that a नञ् is joined
with an *iva*. तेन **राङ्कवः कम्बल** इति ष्फग् न भवति: a blanket is
not a man and not like one either. A whole class excluded by reading a
negative as a comparison.

**A LETTER SPENT A HUNDRED AND FIFTY-EIGHT SŪTRAS FROM THE RULE THAT
USES IT.** 4.2.99's ष्फक्: **षकारो ङीषर्थः**, the ष् is there so that
4.1.41's ङीष् comes in the feminine. कापिशायनं मधु, कापिशायनी द्राक्षा.

**A व्यवस्थितविभाषा APPLIED TO A SENTENCE OF A COMMENTARY.** 4.2.116
meets the Mahābhāṣya's वा नामधेयस्य वृद्धसंज्ञा वेदितव्या and answers
**तत्रैवं वर्णयन्ति — वा नामधेयस्येति व्यवस्थितविभाषेयम्, सा छे
कर्तव्ये भवति, ठञ्ञिठयोर्न भवति**: the option is distributed, holding
where छ is to be given and not for these two affixes. The instrument
first met at 3.4.85, turned on a commentary's sentence rather than a
sūtra's word.

**AND THE ATTRIBUTION GUARD EARNED ITS KEEP TWICE.** The first draft
of that note quoted the Kāśikā's own explanation with an ellipsis
through the middle, producing a string that is in no source on disk;
and a later draft put the Bhāṣya citation and the Kāśikā's answer in
ONE paragraph, so the guard looked for the vṛtti's words inside the
Mahābhāṣya. Both were real faults and both were caught by the same
test. **A citation marks a paragraph, so a paragraph carries one
source.**


4.2.67–4.2.92: **the four senses, and then a heading whose content is
everything that is left.**

**A BODY OF RULES NAMED FROM A NUMBER, AND THE NUMBER MADE BY ONE
SYLLABLE.** 4.2.67 to 4.2.70 state four senses — found there, made by
that, the dwelling of that, near that — and 4.2.70's च is what gathers
them: **चकारः पूर्वेषां त्रयाणामर्थानामिह सन्निधानार्थः, तेनोत्तरेषु
चत्वारोऽप्यर्थाः संबध्यन्ते**. Every rule to 4.2.91 then gives an affix
in whichever of the four fits, यथासंभवम्, and the tradition calls them
**चातुरर्थिक**, *of-the-four-senses*. A conjunction produces a number
and the number produces a name for twenty-one rules.

**SEVENTEEN AFFIXES AND SEVENTEEN LISTS IN ONE SŪTRA.** 4.2.80:
वुञादयः सप्तदश प्रत्ययाः, अरीहणादयोऽपि सप्तदशैव प्रातिपदिकगणाः, and
**आदिशब्दः प्रत्येकमभिसंबध्यते** — *and-the-rest* attaches to each of
the seventeen separately. Five times the length of 4.1.42's eleven,
and the longest यथासंख्य correspondence in the grammar. One word
(शिरीष) is in THREE of the seventeen lists and takes the default
besides, so it has four affixes — and 4.2.82's list then elides one of
them.

**A CASE DELIBERATELY WRONG, SO THAT NO RESTRICTION MAY FOLLOW.**
4.2.78 रोणी: **रोणीति कोऽयं निर्देशः, यावता प्रत्ययविधौ पञ्चमी
युक्ता?** — a rule giving an affix names its base in the ablative, and
this names it in the nominative. **सर्वावस्थप्रतिपत्त्यर्थम्**: so
that the word is taken in EVERY state, alone and as a final member.
4.1.150 broke a compounding rule to send a signal; this bends a
case-ending for the same kind of reason.

**A CLAUSE FROM FOURTEEN SŪTRAS BACK DECIDING WHERE AN ELISION MAY
BITE.** 4.2.67 ends तन्नाम्नि — the country must be NAMED by the
derived word. 4.2.81 drops the affix for a country that is a group of
villages, and the vṛtti asks why औदुम्बरो जनपदः is not dropped too:
**तन्नाम्नीति वर्तते, न चात्र लुबन्तं तन्नामधेयं भवति**. And 4.2.85
uses the same clause again — **मतुबन्तस्यातन्नामधेयत्वात्**, which is
why भागीरथी is outside it. One clause, two refusals, eighteen sūtras
apart.

**A ROOT PRODUCING A PEOPLE'S NAME AS THEIR COUNTRY'S.** 4.2.81's
elision is what gives पञ्चालाः, कुरवः, मत्स्याः, अङ्गाः, वङ्गाः,
मगधाः — an affix given and removed, and what remains is the name of a
people used as the name of their land.

**AN OPTIONAL WORD READ AS A ज्ञापक BECAUSE IT WAS UNNECESSARY.**
4.2.83: वाग्रहणं किम्, यावता शर्कराशब्दः कुमुदादिषु वराहादिषु च
पठ्यते? — being in two of 4.2.80's lists gives the alternative already.
**एवं तर्ह्येतज् ज्ञापयति — शर्कराशब्दादौत्सर्गिको भवति, तस्यायं
विकल्पितो लुब्**: the word teaches WHICH affix is being dropped.
**तदेवं षड् रूपाणि भवन्ति** — six forms of one word, counted out.

**And the vṛtti stops to admire the rule it is explaining.** 4.2.74
turns on whether a well stands north or south of one particular river,
and the two affixes differ only in accent. **महती सूक्ष्मेक्षिका
वर्तते सूत्रकारस्य** — *the sūtra-maker's eye for fine distinctions is
great.*

**शेषे — A HEADING WHOSE CONTENT IS THE COMPLEMENT OF EVERY SENSE SO
FAR.** 4.2.92: **उपयुक्तादन्यः शेषः**, whatever is left over from the
descendant-sense through the four. The same word did this for
technical names at 3.4.114 आर्धधातुकं शेषः, and there too the code had
to ask the other rule and take what it did not give.

And the vṛtti gives two reasons pulling opposite ways. **तेषु घादयो मा
भूवन्निति शेषाधिकारः क्रियते** — the earlier senses are special cases
of *this belongs to that*, so without the heading these affixes would
reach back into them. And **साकल्यार्थं शेषवचनम्** — so that they
reach ALL of what remains rather than only the nearest sense. One word
doing an exclusion and an inclusion at once. **शेष इति लक्षणं
चाधिकारश्च**: and it is both a ground and a heading, the third time
the vṛtti has declined to choose between two readings because nothing
turns on it.


4.2.43–4.2.66: **the collection sense closes and four more open** —
territory, first-metre, weapon-in-a-game, and *studies it or knows
it*. Five stated ranges in this pāda now, all four ends checkable.

**ONE LIST-ENTRY READ AS TWO GENERAL PRINCIPLES.** 4.2.45's
क्षुद्रकमालव is already reached by 4.2.44, so its presence must be
teaching something: ननु च परत्वादञा वुञ् बाधिष्यते? **एवं तर्ह्येतज्
ज्ञापयति — वुञि पूर्वविप्रतिषेधः, सामूहिकेषु च तदन्तविधिरस्तीति**.
It teaches (i) that 4.2.39's affix wins the clash by
पूर्वविप्रतिषेध and (ii) that these rules reach a compound through
its last member. **A single word in a गण made to carry two general
principles**, and then restated with a condition to narrow itself.
Two kārikās set the argument out.

**AN अतिदेश BORROWING FROM A VĀRTTIKA.** 4.2.46 चरणेभ्यो धर्मवत् —
and what it borrows is not a sūtra but **चरणाद् धर्माम्नाययोः**
(वा० ४.३.१२६), a supplementary rule on a later sūtra. The project has
seen an extension reach forward to rules not yet stated (4.2.34); this
one reaches forward to something that is not a rule at all.

**A MEMBERSHIP WITHHELD FOR A LATER RULE'S SAKE.** 4.2.50 gives खल,
गो and रथ the same affix 4.2.49's list gives, and the vṛtti says why
they are not simply IN that list: **पाशादिष्वपाठ उत्तरार्थः** — so
that 4.2.51 may name them. 4.1.45 put a word INTO a list for the next
rule's sake; this keeps three OUT of one for the same reason.

**FOUR SENSES OF ONE WORD SET OUT BEFORE THE RIGHT ONE IS PICKED.**
4.2.52: विषयशब्दोऽयं बह्वर्थः — a village-group, an object of sense, a
thing constantly studied, and what a creature cannot live outside;
मत्स्यानां विषयो जलम्. **तत्र देशग्रहणं ग्रामसमुदायप्रतिपत्त्यर्थम्**
— the second word of the sūtra is what picks the first sense, and the
other three are printed so the reader can see the work being done.

**SIX WORDS AND A JOB ASSIGNED TO EACH BEFORE A SINGLE EXAMPLE.**
4.2.55: स इति समर्थविभक्तिः, अस्येति प्रत्ययार्थः, आदिरिति
प्रकृतिविशेषणम्, इतिकरणो विवक्षार्थः, छन्दस इति प्रकृतिनिर्देशः,
प्रगाथेष्विति प्रत्ययार्थविशेषणम्. The most complete word-by-word
account of a sūtra the project has met.

**THE WORD *THAT* SAID TWICE SO TWO PEOPLE MAY BE KEPT APART.** 4.2.59
तदधीते तद्वेद: **द्विस्तद्ग्रहणम् अधीयानविदुषोः पृथग्विधानार्थम्** —
one who studies a thing and one who knows it are not the same person,
and a single statement would have required both at once.

**A restriction that does three refusals with one word.** 4.2.66:
**अनन्यभावो विषयार्थः, तेन स्वातन्त्र्यम् उपाध्यन्तरयोगो वाक्यं च
निवर्तते** — *subject* means having no other being, and three things
fall away with it: the word standing alone, its taking another
qualifier, and a phrase in its place. A rule that gives no affix and
restricts a whole class of words already formed — and its row is the
second of only two in the pāda stating neither a case nor a sense, the
other being 4.2.36's total निपातन. **Neither is a provision, which is
why neither has a ground.**

**And a word refused for a reason outside grammar.** 4.2.60:
औक्थिक्यशब्दाच्च प्रत्ययो न भवत्येव, **अनभिधानात्** — because nobody
says it. The same rule's vārttikas contain the sharpest statement of a
distinction the project keeps meeting:
**आख्यानाख्यायिकयोरर्थग्रहणम्, इतिहासपुराणयोः स्वरूपग्रहणम्** — of
four words in one list, two are taken by their MEANING and two by
their FORM.

**And an elision that makes the student and the work one word.**
4.2.64 प्रोक्ताल्लुक् — **प्रोक्तसहचरितः प्रत्ययः प्रोक्तः**, an affix
given in the sense *declared by* is itself called *declared*, by
association; the second affix then goes, and पाणिनीयम् the book and
पाणिनीयः its student are the same form.

**Affixes that are whole words**, for the first time: 4.2.54's विध and
भक्त, *portion* and *share*; and 4.2.51's vārttikas add खण्डच्,
स्कन्धच् and **काण्डः** — the last of which is what names the
divisions of a book.

**DEBT PAID.** The one written at 4.2.37 — that only two of the four
rules its example subtracts were codified — collected itself when
4.2.44 and 4.2.47 arrived in this block. What the four exclude is now
checked against the table rather than quoted from the note.

**SCAR — an unescaped apostrophe.** A repair script wrote *book's* into
a single-quoted Python literal and broke three test files at import.
The standing rule is *always ast.parse before writing*, and I parsed
two of the three files the script touched. **Parse every file the
script writes, not the ones it was mainly about.**


4.2.22–4.2.42: **the deity sense and the collection sense**, and two
more ranges with both ends stated — **four now in one pāda**, where
most anuvṛtti in this project has had to be inferred from where a rule
stops making sense.

**A SŪTRA SPLIT SO THAT यथासंख्यम् MAY NOT APPLY.** 4.2.28:
**योगविभागः सङ्ख्यातानुदेशपरिहारार्थः** — two affixes and two bases
in one rule would have been paired off one to one by 1.3.10, so
dividing the sūtra is what lets BOTH affixes reach BOTH words. 4.1.150
achieved the same thing by BREAKING a compounding rule and letting the
breach be the signal. **Two instruments for one purpose, a pāda
apart**, and both are now on record.

**AN EXTENSION REACHING FORWARD TO RULES NOT YET STATED.** 4.2.34
कालेभ्यो भववत् borrows whatever 4.3.11 onward will give in another
sense — कालाट् ठञ् इति प्रकरणे भवे प्रत्यया **विधास्यन्ते** — and
**वत्करणं सर्वसादृश्यपरिग्रहार्थम्** says the borrowing takes in EVERY
likeness and not merely the affix. 3.4.85's लोटो लङ्वत् had its
borrowing cut short by an option carried from two sūtras back; this one
is stated to be total.

**THE MOST COMPLETE निपातन IN THE PROJECT.** 4.2.36:
**समर्थविभक्तिः प्रत्ययः प्रत्ययार्थोऽनुबन्ध इति सर्वं निपातनाद्
विज्ञेयम्** — the case-relation, the affix, the sense of the affix and
its marks are ALL to be read backward off the forms given. Nothing in
the rule is derived from anything, and the check that makes it more
than a remark is that its row is the only one in the pāda stating
neither a case nor a sense: there is nothing to state.

**AN EXAMPLE COMPUTED BY SUBTRACTION.** 4.2.37 तस्य समूहः, and the
vṛtti asks किमिहोदाहरणम्? Every ordinary base is claimed by some later
rule of the same section, so the answer is a list of what the example
must NOT be: **चित्तवद् आद्युदात्तम् अगोत्रम् यस्य च नान्यत्
प्रतिपदं ग्रहणम्** — animate, first-accented, not a lineage-name, and
not named in any rule of its own. **A rule whose example exists only
in the gap its own section leaves**, and two of the four rules doing
the excluding are still ahead — written as a debt that fails when they
arrive.

**One word technical inside its section and ordinary outside it.**
4.2.39's गोत्र: **अपत्याधिकारादन्यत्र लौकिकं गोत्रं गृह्यते
अपत्यमात्रम्, न तु पौत्रप्रभृत्येव** — outside the descendant heading
the word means any descendant and not 4.1.162's grandson-onward. The
boundary of a technical name is a SECTION, and this is the first place
the project has seen one stated as such.

**A word restated to break a bundle.** 4.2.24 names its case again
though it is already running: **पुनः समर्थविभक्तिनिर्देशः
संज्ञानिवृत्त्यर्थः** — the repetition is what stops 4.2.21's
संज्ञायाम् carrying down with it. Anuvṛtti brings a rule's conditions
as a bundle, and restating one is how a single one is untied, which is
4.1.65's move seen again.

**Three affixes for one word, each cited to a different text.** 4.2.29
महेन्द्राद् घाणौ च: महेन्द्रियम्, माहेन्द्रम् (तै०सं० ६.५.५.४),
महेन्द्रीयम् (काठ०सं० १५.१). And 4.2.32 gives SIX compounds two forms
apiece, **and cites both forms of all six**. Not a grammarian's
constructions but attested usage, gathered.

**A membership doing the work of a प्रतिषेध.** 4.2.38: युवतिशब्दोऽत्र
पठ्यते, **तस्य ग्रहणसामर्थ्यात् पुंवद्भावो न भवति** — being named in
the list is itself the reason the feminine survives. And the same rule
names the DEFAULT affix expressly, अण्ग्रहणं बाधकबाधनार्थम्, to beat
what would have beaten it: 4.1.84's move for the third time.

**And two more definitions the sūtras do not give.** 4.2.24's देवता —
**यागसंप्रदानं देवता, देयस्य पुरोडाशादेः स्वामिनी**, what a sacrifice
is given TO and the owner of the cake, with the affix on the OFFERING.
And 4.2.39's gloss of which gods two opaque compounds name: शुनो
वायुः, सीर आदित्यः.


4.2.1–4.2.21: **a case-relation and a sense, and the affix
understood.** 4.1 spent 178 sūtras on ONE sense and named its affix in
nearly every rule. This pāda changes the shape entirely: each rule
states a CASE and a SENSE and lets 4.1.83's default supply the affix
unless it has reason to speak. **Eight of these twenty-one name no
affix at all**, and the fall-through is declared as a reuse in each.

    तेन रक्तं रागात्      by that, dyed          — instrumental
    तेन युक्तं कालः       joined with that       — instrumental
    तेन दृष्टं साम        seen by that           — instrumental
    तेन परिवृतो रथः       wrapped in that        — instrumental
    तत्रोद्धृतममत्रेभ्यः  taken up in that       — locative
    तत्र संस्कृतं भक्षाः  prepared in that       — locative
    सास्मिन् पौर्णमासी    that being in it       — nominative

That is what 4.1.82 समर्थानां प्रथमाद्वा was for. It said the affix
attaches to the FIRST of the syntactically connected words; these
rules say WHICH connection, in which case, and in what sense. **The
heading and the section fit together exactly and neither works
alone**, which is the first time in this project that two blocks a
pāda apart have been that closely joined.

**TWO CASE-RUNS WITH BOTH ENDS STATED.** 4.2.1's vṛtti says
द्वैपवैयाघ्रादञ् इति यावत् तृतीयासमर्थविभक्तिरनुवर्तते — the
instrumental runs to 4.2.12. 4.2.14's says क्षीराड् ढञ् इति यावत् —
the locative runs to 4.2.20. **Both ranges are named by the rule that
opens them, so both can be checked** rather than guessed, and the test
that makes them mean anything is the third: no rule inside either
range states the other's case.

**ONE WORD SEPARATING TWO RULES.** 4.2.3 and 4.2.4 share their base,
their case and their sense — and one gives an affix while the other
takes it away. अविशेषे is the whole difference, and the elision is
what lets a star-name serve as the name of a day.

**A grammatical rule unusable without another science, and the vṛtti
supplies it.** 4.2.3: कथं पुनर्नक्षत्रेण पुष्यादिना कालो युज्यते? —
**पुष्यादिसमीपस्थे चन्द्रमसि वर्तमानाः पुष्यादिशब्दाः प्रत्ययम्
उत्पादयन्ति**: the star-names are used of the MOON standing near
those stars, and it is the moon the time is joined with. Two more
rules of the run define their own terms the same way — 4.2.10's
परिवृत, wrapped with **न कश्चिदवयवो अवेष्टितः**, no part left bare;
and 4.2.16's भक्ष and संस्कार, **सत उत्कर्षाधानं संस्कारः**.

**TWO RULES, ONE AFFIX, ONE SENSE — AND THEY STILL DIFFER.** 4.2.18's
vṛtti asks ननु च संस्कृतार्थे प्राग् वहतेष्ठकं वक्ष्यति, तेनैव
सिद्धम्? and answers न सिध्यति: दध्ना हि तत् संस्कृतं यस्य
**दधिकृतमेवोत्कर्षाधानम्**, इह तु दधि **केवलमाधारभूतम्**. There the
curds do the improving; here they are only what the thing stands in
and salt does the work. **A distinction in the situation, not in the
grammar.**

**A silent letter placed to keep an affix out of a rule four chapters
away.** 4.2.9's ड्: डित्करणं किमर्थम्? ययतोश्चातदर्थे इति ...
**अनयोर्ग्रहणं मा भूत्** — 6.2.156 names य and यत्, and without the
mark these two would be caught and अवामदेव्यम् would take the wrong
accent. The exclusion runs through two paribhāṣās, and a verse states
the whole argument.

**A rule stated for what it prevents.** 4.2.11:
**मत्वर्थीयेनैव सिद्धे वचनमणो निवृत्त्यर्थम्** — the affix was
available anyway as a possessive, so the rule exists only to keep the
default out. 4.1.84 was the same, except that there the thing
prevented had not yet been stated.

**And two words spent to teach what one of them does.** 4.2.21:
इतिकरणस्य संज्ञाशब्दस्य च तुल्यमेव फलं ..., तत्र किमर्थं
द्वयमुपादीयते? — **संज्ञाशब्देन तुल्यताम् इतिकरणस्य ज्ञापयितुम्, न
ह्ययं लोके तथा प्रसिद्धः**. The pair is there so that इति may be
TAUGHT to do the job, since it is not commonly known to; and once
taught, it serves alone wherever the grammar says इतिकरणस्ततश्चेद्
विवक्षा. A word explained by being set beside one that is already
understood.

**And the vṛtti offers two derivations rather than one, twice.**
4.2.13's कौमार — either from the girl in the second case, or simply
*what happens in girlhood*, **and the second needs no निपातन at all**,
which is why it is offered. 4.2.21's पौर्णमासी — पूर्णमासादण्, or
पूर्णो माः, **मा इति चन्द्र उच्यते**.


4.1.137–4.1.178: **अध्याय ४ पाद १ is finished** — all 178 sūtras,
checked against the corpus rather than a count. The longest pāda the
project has read, and the one with the most in it about what a
grammar is.

**TWO NAMES FOR ONE DESCENDANT, AND THE CHOICE TURNS ON NOTHING
GRAMMATICAL.** 4.1.162 गोत्र from the grandson onward; 4.1.163 युवन्
while an elder of the line is living. Then 4.1.166 वृद्धस्य च
**पूजायाम्** gives the young name to an elder OUT OF RESPECT, and
4.1.167 यूनश्च **कुत्सायाम्** gives the lineage name to a young man
OUT OF CONTEMPT. Two adjacent rules moving the same pair of names in
opposite directions, and what decides is who is being honoured or
disparaged.

**A WORD'S CASE CHANGED IN READING TO MOVE A BOUNDARY BY ONE
GENERATION.** 4.1.162 counts from the grandson; 4.1.163 must count
from one further down, and the vṛtti gets it by rereading a case
ending — **षष्ठ्या विपरिणम्यते** पौत्रप्रभृतेर्यदपत्यमिति, तेन
चतुर्थादारभ्य युवसंज्ञा विधीयते.

**A SECTION ACTING AS A BARRIER TO A REFERENCE.** 4.1.174 ते
तद्राजाः: सर्वनाम्ना प्रत्यवमृश्यन्ते **न तु पूर्वे,
गोत्रयुवसंज्ञाकाण्डेन व्यवहितत्वात्** — the pronoun reaches the
affixes from 4.1.168 and no earlier, because the naming section stands
between and separates them. **Anuvṛtti has now been stopped four
different ways in this project** — by a word at 3.4.99, read backward
at 4.1.18, carried half-way at 4.1.27, and here blocked by a block of
rules — and each is on record in its own rule.

**A RULE BROKEN ON PURPOSE, SO THAT ITS BREACH MAY CARRY
INFORMATION.** 4.1.150 puts the longer word first in a dvandva where
2.2.34 requires the shorter: **अल्पाच्तरस्यापूर्वनिपातो
लक्षणव्यभिचारचिह्नम्, तेन यथासंख्यमिह न भवति** — the violation is a
MARK that 1.3.10's *taken in order* does not apply. A signal sent by
disobeying a rule.

**FIVE WAYS OF SAYING *OPTIONALLY*, AND ONE WOULD HAVE DONE.** 4.1.160:
उदीचां, प्राचाम्, अन्यतरस्याम्, बहुलम् इति **सर्व एते विकल्पार्थाः,
तेषामेकेनैव सिध्यति**. So the surplus is read as two other things —
आचार्यग्रहणं **पूजार्थम्**, बहुलग्रहणं **वैचित्र्यार्थम्**. And that
same naming is now read three ways across the project: for HONOUR at
3.4.18 and 4.1.130, for VARIETY at 4.1.153, and both at once here.

**Kinship defined by ritual to fix a grammatical condition.** 4.1.165
turns on an older सपिण्ड being alive, and the vṛtti defines the word
by citing a law-book: सप्तमपुरुषावधयः सपिण्डाः, येषाम् **उभयत्र
दशाहानि कुलस्यान्नं न भुज्यते** (मनु० ५.६१). Kinship measured by whose
food may not be eaten. And 4.1.147 does the same in the other
direction — पितुरसंविज्ञाने मात्रा व्यपदेशोऽपत्यस्य कुत्सा, being
named by the mother where the father is unknown IS the contempt the
rule requires.

**Two rules inside the descendant section that make no descendant.**
4.1.145 भ्रातृव्यः means an ENEMY and 4.1.161 मानुषः means a HUMAN
BEING, and both vṛttis say **अपत्यार्थोऽत्र नास्त्येव** in the same
words. And one of them offers a check rather than an assertion: तथा च
मानुषा इति बहुषु न लुग् भवति — the plural keeps the affix, which a
descendant-affix would not.

**A refusal in one chapter used to license an elision in another.**
The pāda ends on it. 4.1.178 refuses the elision for three groups, and
the vṛtti asks what the refusal can be refusing: पाञ्चमिकस्याञः —
5.3.117's affix. कथं पुनस्तस्य भिन्नप्रकरणस्थस्यानेन लुक्
प्राप्नोति? **एतदेव विज्ञापयति** पाञ्चमिकस्यापि तद्राजस्य लुग्
भवतीति. A refusal can only refuse something, so 4.1.177 must reach two
chapters ahead — and the fruit is a third rule entirely:
**यौधेयादिप्रतिषेधो ज्ञापकः पर्श्वाद्यणो लुगिति**.

**And the bluntest thing the vṛtti says about attested usage.** 4.1.103
and 4.1.105 explained three famous names by **अध्यारोप**, transfer.
4.1.151 does not: कथं भाषायां वैन्यो राजेति? **छान्दस एवायं प्रमादात्
कविभिः प्रयुक्तः** — a Vedic form used in ordinary speech BY THE
CARELESSNESS OF POETS.

**A rule's scope read off its neighbour's exclusion, twice and in
opposite directions.** 4.1.139 takes both a compound and the bare word
**उत्तरसूत्रे पूर्वपदप्रतिषेधात्**, because the next rule refuses a
first member. 4.1.177 does NOT reach a compound's last member
**अवन्त्यादिभ्यो लुग्वचनात्**, because the rule before it named
particular words.

**An attributed rule now has to be asked for**, and the change earned
itself twice: 4.1.130's northern teachers and 4.1.153's, both of which
the vṛtti says CO-APPLY with the rule beside them rather than beating
it.

**SCAR — sandhi in a test substring, ninth time.** तेषामेकेनैव joins
तेषाम् and एकेन. And once more of the compounding kind: तस्यापत्यम् is
in a note only inside अपत्यमिति.

**SCAR — a spelling the editions disagree on.** A test asserted the
order of two words in 4.1.150 by looking for one of them, and GRETIL
writes फाण्डाहृति where Vidyut writes फाण्टाहृति. The assertion was
about ORDER and had no business depending on a letter the witnesses
differ over; it now runs over both witnesses and finds each spelling
in its own.


4.1.113–4.1.136: **the ढक् run**, mostly from feminine stems, and the
stretch where the commentary says the most about what a grammar IS.

**A GRAMMAR DEFENDING ITSELF AGAINST ITS OWN EXAMPLES.** 4.1.114 gives
an affix after the names of three royal houses, and the vṛtti stops to
ask: **कथं पुनर्नित्यानां शब्दानाम् अन्धकादिवंशसमाश्रयणेन
अन्वाख्यानं युज्यते?** — if words are eternal, how can a rule be framed
by reference to particular families, which are not? Two answers, and
neither is dropped. केचिदाहुः — **काकतालीयन्यायेन** ...
शब्दास्सुबहवः संकलिताः, तानुपादाय पाणिनिना स्मृतिरुपनिबद्धेति: by the
crow-and-palm-fruit coincidence a great many such words happened to
gather there without mixing, and **Pāṇini recorded what he found**. Or
else the houses are eternal too. The vṛtti puts the first answer first
— a rule in a grammar of eternal speech, admitted to be contingent.

**TWO READINGS OF THE SŪTRA ITSELF, AND BOTH ARE AUTHORITATIVE.**
4.1.117: शुङ्गाशब्दं स्त्रीलिङ्गमन्ये पठन्ति, ततो ढकं
प्रत्युदाहरन्ति — others read one word as feminine and give a
different counter-example. **द्वयमपि चैतत् प्रमाणम् उभयथा
सूत्रप्रणयनात्**: both are valid, *because the sūtra was composed both
ways*. Not two views of one text but two texts. This project's
collation records where the printed editions differ; here is the
commentary doing the same and declining to settle it.

**A RULE THAT IS ITS OWN ज्ञापक.** 4.1.133 states an elision before
ढक् — and nothing anywhere gives ढक् after that stem. कथं पुनरिह ढक्
प्रत्ययः? **एतदेव ज्ञापकं ढको भावस्य**: the rule's own existence is
the evidence that the affix comes. A sūtra whose only support is that
it was written. And 4.1.134 then carries BOTH that rule and the one
before it to another word — पितृष्वसुर्यदुक्तं तद् मातृष्वसुरपि भवति
— an अतिदेश one of whose two objects had nothing to stand on but
having been said.

**And an empty rule read as evidence about words it does not
mention.** 4.1.130: आरग्वचनमनर्थकम्, रका सिद्धत्वात्? — the rule
before already gives the form. **ज्ञापकं त्वयमन्येभ्योऽपि भवतीति**: so
the point of stating it is to teach that the affix comes after OTHER
words — जाडारः, पाण्डारः. Four ज्ञापक arguments in this pāda now, and
these two are the strongest.

**शब्दधर्म against अर्थधर्म, named as such.** 4.1.113 states two
conditions in one rule and the vṛtti says what kind each is:
अवृद्धाभ्य इति **शब्दधर्मः**, नदीमानुषीभ्य इति **अर्थधर्मः** — one a
property of the WORD and one of what the word MEANS, तेनाभेदात्
प्रकृतयो निर्दिश्यन्ते. The distinction returns at 4.1.131 in the same
word and at 4.1.135 in substance.

**And the same kind of word read in opposite ways five sūtras apart.**
4.1.115's स्त्रीलिङ्गनिर्देशोऽर्थापेक्षः — the feminine of the rule's
own word is about the SENSE. 4.1.120's स्त्रीप्रत्ययविज्ञापनाद्
असत्यर्थग्रहणे — the feminine there names the AFFIX, so इडबिड and
दरद, feminine in meaning, fall outside. Two rules, one word, two
readings, and each is argued.

**A condition on which RULE produced the word.** 4.1.122's अनिञः:
आत्रेयः takes the affix and दाक्षिः does not, and the two look
identical — the difference is that दाक्षिः's इ is 4.1.95's इञ्. Not a
shape but a derivation.

**Seven rules now turn on whose family is meant**, after 4.1.117 and
4.1.124 joined the five of the previous block. And विकर्ण is reached by
three of them: वैकर्णः among the Vātsyas, वैकर्णेयः among the
Kāśyapas, वैकर्णिः elsewhere. **One word, three families, three
affixes, and nothing in the word to tell them apart.** The test that
counts them reads the table, so it collected the debt itself.

**An attributed rule now has to be ASKED FOR.** 4.1.130 stands beside
4.1.129 rather than over it — वचनसामर्थ्यादेव पूर्वेण समावेशो भविष्यति
— so a citation of a teacher became a condition on the QUESTION and
not a claim to rank. Both गौधेरः and गौधारः are right, and which you
get depends on whose view you asked for.

**And आचार्यग्रहणं पूजार्थम्, said again.** 4.1.130's vṛtti gives the
word *teachers* the same reading 3.4.18's did — the naming is for
HONOUR — a hundred and thirteen sūtras and a chapter apart, in the same
three words.

**A vārttika that undoes its own rule.** 4.1.128 gives चटका an affix
found nowhere else, and the third vārttika on it takes the affix away
where the descendant is female: चटकाया अपत्यं स्त्री **चटका**. The
word ends where it began.


4.1.92–4.1.112: **तस्यापत्यम्, and the twenty rules that answer it.**
Three syllables naming no affix and no base, because 4.1.82 has said
which word the affix attaches to and 4.1.83 has said which affix comes.
The test reads the sūtra off the corpus and checks it really is that
short.

**A HEADING THAT FACES BOTH WAYS.** पूर्वैरुत्तरैश्च प्रत्ययैर्
अभिसंबध्यते — 4.1.92 is read with the affixes stated BEFORE it as well
as after, so 4.1.85's दैत्यः and 4.1.86's औत्सः turn out to have been
patronymics all along. Every heading the project has met governed
forward only — 3.2.84, 3.3.18, 3.4.67, 4.1.1, 4.1.3, 4.1.14, 4.1.76,
4.1.82, 4.1.83 — and a test holds all nine of them to that, so the
claim about this one means something.

**A SŪTRA SPLIT IN TWO BECAUSE NEITHER READING OF IT WHOLE WOULD
WORK.** 4.1.94 गोत्राद् यून्यस्त्रियाम्: किं पुनरत्र प्रतिषिध्यते? यदि
नियमः, स्त्रियामनियमः प्राप्नोति — as a restriction it leaves the
feminine unrestricted; अथ युवप्रत्ययः, स्त्रियां गोत्रप्रत्ययेन
अभिधानं न प्राप्नोति — as a rule giving an affix it leaves the
feminine with none at all. **तस्माद् योगविभागः कर्तव्यः.** And the
split changes WHAT IS DENIED: युवसंज्ञैव प्रतिषिध्यते, what the second
half refuses is the NAME, so the feminine is named by the
lineage-affix after all.

**A HEADING PRESENT AND OVERRIDDEN BY CAPACITY.** 4.1.100 stands under
गोत्र, and 4.1.93 एको गोत्रे allows a lineage exactly one affix — so
under the heading as carried, the rule could give nothing. इह तु
गोत्राधिकारेऽपि **सामर्थ्याद् यूनि प्रत्ययो विज्ञायते**: the heading
says one thing and the rule is read as being about another, *because
it could not otherwise do anything at all*. गोत्राधिकारस्तूत्तरार्थः —
the heading is carried for the rules after this one. The same argument
returns at 4.1.110, about members of a list rather than a whole rule.

**A CONDITION THAT IS NOTHING IN THE WORD.** Five rules of this run —
4.1.102, 4.1.106, 4.1.107, 4.1.108, 4.1.111 — turn on WHOSE FAMILY is
meant: भार्गव, वात्स्य, आग्रायण, ब्राह्मण, कौशिक, आङ्गिरस, त्रैगर्त.
शारद्वतायनो भवति भार्गवश्चेत्, शारद्वतोऽन्यः — same word, same sense,
different family, different affix. No rule anywhere earlier in the
project has a condition of that kind, and the resolver has to give two
answers to two queries differing in nothing else.

**AND A GRAMMATICAL READING SETTLED BY A PROPER NAME.** 4.1.104's
अनृष्यानन्तर्य can be read as *the immediate descendant of a non-sage*
or as *not being the immediate descendant of a sage*. The second
reading would make **कौशिको विश्वामित्रः** wrong —
ऋष्यपत्यनैरन्तर्यविषये प्रतिषेधे विज्ञायमाने कौशिको विश्वामित्र इति
दुष्यति — so the first must be right: अवश्यं चैतदेवं विज्ञेयम्. A
negative compound resolved by a name it would otherwise spoil.

**A LIST THAT ADDS INSTEAD OF EXCEPTING.** Every गण in this pāda until
now carved an exception out of another rule. 4.1.112's शिवादि holds
गङ्गा, which is in two OTHER lists as well — तिकादिफिञा शुभ्रादिढका च
**समावेशार्थम्, तेन त्रैरूप्यं भवति** — so that all three affixes may
apply: गाङ्गः, गाङ्गायनिः, गाङ्गेयः. And one member of the same list
is there for the opposite purpose and only half of it: तक्षन् beats
4.1.153 and is expressly not wanted to beat 4.1.152, so ताक्ष्णः and
ताक्षण्यः both stand.

**And a double membership read as licensing two forms.** 4.1.108's
वतण्ड is in गर्गादि and in शिवादि: अनाङ्गिरसे तूभयत्र पाठसामर्थ्यात्
प्रत्ययद्वयमपि भवति — outside the family the rule names, वातण्ड्यः AND
वातण्डः, *on the strength of being in two lists*. Where 4.1.99 read a
double membership as EVIDENCE about another rule and 4.1.106 read one
as a restriction to be lifted, this reads one as a licence.

**An elision that buys a different affix.** 4.1.109 लुक् स्त्रियाम् —
लुकि कृते शार्ङ्गरवादिपाठाद् ङीन् भवति: once the यञ् is gone, 4.1.73
reaches the bare word. A rule that removes an affix in order that
another may come, which is 4.1.90's elision-before-formation from the
other end, and both cite the same clause — तस्मिन्निवृत्ते सति यो यतः
प्राप्नोति स ततो भवति.

**The section ends where a rule fourteen sūtras earlier said it
would.** 4.1.98's vṛtti: गोत्राधिकारश्च शिवादिभ्योऽण् इति यावत्. And
4.1.112's: गोत्र इति निवृत्तम्, अतः प्रभृति सामान्येन प्रत्यया
विज्ञायन्ते. The test that makes the pair mean anything is the third:
no row past 4.1.112 states the lineage sense.

**And the same fall-through, one heading further on.** 4.1.95, 4.1.96
and 4.1.112 are all exceptions to 4.1.83's default, and `apatya_affix`
reaches for that rule when none of the twenty names the ground — so
the reuse is the fall-through again, as it was at 4.1.84.

**Attested usage accounted for and not licensed, three times.** अश्वत्थामा
called द्रौणायन, राम called जामदग्न्य, व्यास called पाराशर्य: each is
explained by **अध्यारोप**, a transfer onto a present-day man through
mere likeness of sound, and the vṛtti states beside it what the grammar
would actually give — जामदग्नः, पाराशरः. And प्रदीयतां दाशरथाय मैथिली
is put down to the residual sense. **The grammar declines to own the
usage and refuses to leave it unexplained**, which is a stance worth
recording as such.


4.1.76–4.1.91: **the scaffolding a taddhita rule needs before it can
say anything.** Sixteen sūtras, and not one of them gives an affix in
a sense. Only after all of them does 4.1.92 तस्यापत्यम् — three
syllables, naming no affix at all — begin to say in what senses.

**THE POINT OF THE RUN, AND IT IS TESTABLE.** 4.1.92 is a rule of
three syllables that names no affix, and the vṛtti calls such rules
लक्षणवाक्यानि, sentences that give the ground. That works only because
**4.1.83 प्राग्दीव्यतोऽण्** has already said which affix comes when
nothing else is said. The test reads 4.1.92 off the corpus and checks
that it really does name none.

**One sūtra doing the work of three headings.** 4.1.82 समर्थानां
प्रथमाद्वा — त्रयमप्यधिक्रियते समर्थानामिति च, प्रथमादिति च, वेति च.
And each of the three is shown by what would go wrong without it:
समर्थानामिति किम्? कम्बल उपगोः, अपत्यं देवदत्तस्य — two words in one
sentence that do not go together, and the affix would cross between
them. प्रथमादिति किम्? षष्ठ्यन्ताद् यथा स्यात्. वेति किम्? वाक्यमपि
हि यथा स्यात्, so the phrase may stand beside the compound.

**A heading bounded by the point at which its own words become
empty.** That same rule runs to 5.3.1, and the reason is not a change
of topic: स्वार्थिकेषु ह्यस्योपयोगो नास्ति, विकल्पोऽपि तत्रानवस्थितः
— past there the affixes add no meaning of their own, so there is
nothing for *the first of the connected words* to select, and the
option is not steady either. Every heading before this stopped at a
subject; this one stops where it ceases to mean anything.

**Two headings over one range, feeding each other.** 4.1.1 says what
the affixes attach TO and 4.1.76 says what they are CALLED, and both
run to the end of अध्याय ५. And they are not merely parallel: 1.2.46
makes a taddhita-formed word a प्रातिपदिक, which is what lets 4.1.1
govern the NEXT affix after it.

**A grammatical number read as a scope.**
बहुवचनमनुक्ततद्धितपरिग्रहार्थम् — 4.1.76 gives the name in the PLURAL
so that affixes never stated in these two chapters fall under it:
पृथिव्या ञाञौ and अग्रादिपश्चाड्डिमच् become तद्धित though no sūtra
gives them.

**A boundary named by lifting one word out of the rule it stops at.**
तेन दीव्यति is 4.4.2 and तदेकदेशो दीव्यच्छब्दोऽवधित्वेन गृह्यते —
one word of that rule becomes the marker. 4.1.87 does the same with
5.2.1's भवन. Both boundary rules are checked against the corpus.

**Three readings offered and none chosen.** अधिकारः, परिभाषा,
विधिर्वेति त्रिष्वपि दर्शनेष्वपवादविषयं परिहृत्याण् प्रवर्तते — 4.1.83
may be a heading, a principle or a rule that gives an affix, and the
result is identical under all three. The vṛtti says so instead of
deciding, which is the second time in two pādas it has declined a
question because nothing turns on it.

**AN अपवाद REACHING FOR ITS उत्सर्ग, AND THAT IS THE REUSE.** 4.1.84
to 4.1.87 are the exceptions to 4.1.83's default, and the code says so
by FALLING THROUGH: asked about a ground none of the four names,
`prag_divyatah_affix` returns 4.1.83's own answer. **The relation
between an exception and the rule it excepts is not a citation but a
reaching-for**, and this is the first place in the project where it
could be written as one. Four new edges, and the test checks the
answer is 4.1.83's own `why` and not merely its id.

**A rule stated against a rule that has not been stated yet.** 4.1.84
gives the default affix to a list, which by itself says nothing.
पत्युत्तरपदाद् ण्यं वक्ष्यति, तस्यापवादः — the NEXT rule would take
those words away, so this holds them back in advance. A प्रतिषेध aimed
forward, and the only reading under which the rule says anything.

**One affix serving four senses in a row.** 4.1.87: स्त्रीषु भवं
स्त्रैणम्, स्त्रीणां समूहः स्त्रैणम्, स्त्रीभ्य आगतं स्त्रैणम्,
स्त्रीभ्यो हितं स्त्रैणम् — born among, a collection of, come from,
good for, and the affix does not change. The sense comes from the
section the rule stands in, which is exactly what 4.1.83's default
made possible.

**AN ELISION OF SOMETHING THAT WAS NEVER THERE.** 4.1.90 यूनि लुक् —
प्राग्दीव्यतीयेऽजादौ प्रत्यये विवक्षिते **बुद्धिस्थेऽनुत्पन्न एव**
युवप्रत्ययस्य लुग् भवति, तस्मिन्निवृत्ते सति यो यतः प्राप्नोति स ततो
भवति. What is elided is something merely INTENDED, held in the mind
and never produced, and once it is gone whatever else would have
applied applies. **A derivation blocked by running it and removing the
result**, and the vṛtti states it plainly rather than softening it.

**And the machinery that lets a word mean what no part of it says.**
4.1.88 द्विगोर्लुगनपत्ये: पञ्चकपालः means *prepared in five bowls*,
and the affix that said so was given and then dropped. The rule names
the AFFIX and not the compound — उपचारेण तु लक्षणया
द्विगुनिमित्तभूतः प्रत्यय एव द्विगुः — and a look-alike is kept out by
asking what caused what: पाञ्चकपालम् stands because न तस्य द्विगुत्वं
निमित्तम्.

**And two more feminine affixes, under a different heading.** 4.1.77
to 4.1.81 give तिः and ष्यङ् from under 4.1.76 तद्धिताः rather than
4.1.3 स्त्रियाम्, and 4.1.77's vṛtti says so outright — स च
तद्धितसंज्ञो भवति. The two inventories are kept apart in the code
rather than merged, because merging them would have hidden exactly
that. **And ष्यङ् is CONSUMED FOUR SŪTRAS BEFORE IT IS GIVEN**: 4.1.74
यङश्चाप् reads यङ् as covering ञ्यङ् and ष्यङ्, and 4.1.78 spends a
silent letter — ङकारः सामान्यग्रहणार्थः — so that the earlier rule can
reach it. कारीषगन्ध्या is the example on both sides.

**And a second paribhāṣā declared not invariable.** 4.1.85's
लिङ्गविशिष्टपरिभाषा चानित्या, after 4.1.41's अनित्यः षिल्लक्षणो
ङीषिति — and the first of the two is the principle 4.1.1's own vṛtti
leaned on to explain why its feminine class-words are named at all.


4.1.39–4.1.75: **the feminine run is finished**, and every one of the
eight affixes 4.1.1's two class-words promised is now supplied by some
rule of it. The debt written at 4.1.38 — as the exact shortfall, चाप्
and ङीन् — collected itself the moment 4.1.73 and 4.1.74 arrived.

**A REFUSAL IS NOT NARROWER BY COUNTING ITS WORDS.** This is the
finding, and it came from 4.1.56 न क्रोडादिबह्वचः, which exists for
nothing but to stop 4.1.54. That rule states two conditions and this
one states one, so a resolver that ranked everything by specificity
let the rule being excepted beat the exception — a rule whose whole
content is to stop another would have stopped nothing.

**Specificity settles which rule of a KIND applies; it does not settle
whether a प्रतिषेध applies**, because an exception is narrower by
BEING one. The resolver now does two separate things: pick the most
specific rule that GIVES, then ask whether anything refuses THAT
AFFIX. And the second half falls out for free — 4.1.22, 4.1.23 and
4.1.24 all refuse one affix, and which of them speaks is settled among
the refusals alone, with no weight tuning at all.

**Three conditions defined in verse, and none in a sūtra.** गुणवचन at
4.1.44 — सत्त्वे निविशतेऽपैति पृथग् जातिषु दृश्यते, आधेयश्चाक्रियाजश्च
सोऽसत्त्वप्रकृतिर्गुणः. स्वाङ्ग at 4.1.54 — अद्रवं मूर्तिमत् स्वाङ्गं
प्राणिस्थमविकारजम्, अतत्स्थं तत्र दृष्टं चेत् तस्य चेत् तत्तथायुतम्.
जाति at 4.1.63 — आकृतिग्रहणा जातिर्लिङ्गानां च न सर्वभाक्,
सकृदाख्यातनिर्ग्राह्या गोत्रं च चरणैः सह. **Each is a word the rule
turns on and nothing in the form shows**, and the grammar hands the
definition to a verse rather than to a sūtra. Three in thirty-seven
rules, and none anywhere else in the project so far.

**Eleven words matched to eleven senses.** 4.1.42, the longest
यथासंख्य correspondence met, each pair with its counter-form beside
it — जानपदी if a livelihood, जानपदान्या otherwise. And the sense
decides not only whether the affix comes but WHICH RULE gives it:
नागी in the sense of bulk is 4.1.42's, नागी as a class-name is
4.1.63's, and नागा as a quality is 4.1.4's. One word, one affix, three
rules, told apart by nothing but what it means.

**Three pairs of rules differing only in accent.** 4.1.25 against
4.1.26, 4.1.39 against 4.1.40, and 4.1.60 against the whole स्वाङ्ग
section. ङीप् and ङीष् both give ई; स्वरे विशेषः is the entire
content of each pair, and a sūtra is spent on each side of a
distinction that is inaudible except in pitch.

**A word travelling backward, and what it arrives to do.** 4.1.18's
सर्वत्र was pulled DOWN into 4.1.17 — उत्तरसूत्रादिहापकृष्यते,
बाधकबाधनार्थम् — so that the eastern teachers' ष्फ might beat a rule
fifty-eight sūtras later. That rule is 4.1.75, and it is now codified:
प्राचां ष्फ एव, सर्वत्रग्रहणात् — आवट्यायनी. **Both ends of the
transaction are in the commentary and both are now on record**, one
saying which way the word travels and the other what it arrives to do.

**One rule running the other way.** Four rules of this run license a
VEDIC form beside an ordinary one. 4.1.62 सख्यशिश्वी इति भाषायाम्
licenses an ORDINARY form and leaves the Veda alone — सखा सप्तपदी भव
stands. The only rule of its kind here, and the test reads the Vedic
set off the table so it cannot go stale.

**A redundancy that teaches, for the second time.** 4.1.41 puts two
words in a list its own षित् clause already reached:
षित्त्वादेव सिद्धे ज्ञापनार्थं वचनम्, and what it teaches is
**अनित्यः षिल्लक्षणो ङीषिति** — the षित् ground is not invariable.
The same shape as 3.4.103's ङिद्वचनं ज्ञापनार्थम्, and the two notes
now point at each other.

**A rule beaten or not according to which WORD of it is still
running.** 4.1.73 beats 4.1.63's ङीष् and not 4.1.48's, though both
give the same affix: जातिग्रहणं चेहानुवर्तते, तेन जातिलक्षणो ङीषनेन
बाध्यते, न पुंयोगलक्षणः. Only one of the two is stated with the word
that carries down here.

**And a word repeated to untie ONE of three conditions.** 4.1.65 says
जाति again though it is already carried from 4.1.63, and the repetition
releases that rule's अयोपध while leaving the rest: औदमेयी. Anuvṛtti
brings a rule's conditions as a bundle, and restating a word is how a
single one is untied — which is 4.1.27's संख्याग्रहणमनुवर्तते,
नाव्ययग्रहणम् seen from the other side.

**A rule that gives different amounts to different members of its own
list.** 4.1.49: येषामत्र पुंयोग एवेष्यते, तेषामानुगागममात्रं विधीयते,
प्रत्ययस्तु पूर्वेणैव सिद्धः; अन्येषां तूभयं विधीयते. For some members
the affix came from 4.1.48 and only the augment is new; for the rest
both are given here. One list, two contents.

**And an आकृतिगण — a list defined by shape rather than enumerated.**
4.1.56's क्रोडादि. The first in this project, and it sits beside
4.1.4's अजादि, whose members share no reason at all and which two
later rules of the pāda name as the place to send what they cannot
otherwise place.

**SCAR — a line break inside a Devanāgarī word.** A note wrapped
सोऽसत्त्वप्रकृतिर्गुणः across two lines, and `unwrapped` put a space
where the break was. Worse than a test problem: a reader of the note
saw the split too. Fourth time for the line-wrap scar, and the first
where the damage was visible to a reader rather than only to a test.


4.1.1–4.1.38: **अध्याय ४ opens by doing for nouns what अध्याय ३ had
just finished doing for verbs**, and the parallel is exact enough to
test rather than admire.

**Two enumerations, and the second makes two names where the first
made one.** 3.4.78 gave eighteen verbal endings and spent the last
letter of the last of them on तिङ्. 4.1.2 gives twenty-one case
endings and spends two letters on two: औटष्टकारः सुडिति
प्रत्याहारग्रहणार्थः cuts out सुट्, the first five, and पकारः सुबिति
प्रत्याहारार्थः cuts out सुप्, the whole. The test asserts the SHAPE
of each list rather than its length — three by three by two for one,
three by seven for the other — because a count goes stale and a
product does not.

**And the senses are given somewhere else.** संख्याकर्मादयश्च
स्वादीनामर्थाः शास्त्रान्तरेण विहिताः, तेन सहास्यैकवाक्यता — number
comes from 1.4.21 and the kāraka from अध्याय २, and this rule is read
as ONE SENTENCE with those. That is the reverse of the कृत् affixes,
each of which was given IN a sense, with 3.4.67 supplying one only
where a rule had not.

**The longest heading in the project.** 4.1.1 ङ्याप्प्रातिपदिकात् runs
आ पञ्चमाध्यायपरिसमाप्तेः — to the end of अध्याय ५, two whole chapters.
The test does not take my word for where that is: it reads the last
sūtra of 5.4 off the corpus and checks the heading names it.

**A HEADING THAT TAKES ONLY PART OF THE HEADING ABOVE IT — and the
reuse that finally earned its declaration.** 4.1.3 स्त्रियाम् stands
under 4.1.1 and can use only ONE of the three things that rule names:
प्रातिपदिकमात्रमत्र प्रकरणे संबध्यते, **ङ्यापोरनेनैव विधानात्** —
because this section is where the other two are MADE. A rule cannot
take as its input what it is about to produce.

That is not a remark. `stri_heading` now ASKS `nominal_base` what it
governs and subtracts what this section gives, and the vṛtti's
argument comes out as one set difference. The declaration and the code
are the same thing, which is the only version of a reuse worth
declaring.

**SCAR — a dependency of the FILE is not a dependency of the RULE.**
4.1.4 declared the same edge and did not earn it. The module really
does build its eight affixes out of 4.1.1's two class-words — but that
happens once at import, and no call from `stri_affix` ever asks 4.1.1
anything. The reuse guard caught it, the second time it has caught a
declaration true of the file and false of the sūtra. Withdrawn.

**SCAR — subtract the SECTION, not the progress.** The first version
of that set difference subtracted what the TABLE gives. While
4.1.73–75 were still ahead, it answered that this section may take
चाप् and ङीन् as INPUT — the exact opposite of true, since those are
two of the things it produces. **A section is defined by what it is
for, not by how much of it has been read**, and a derivation that
reads the codebase's own progress will lie about the grammar. Now held
by a test.

**A run that refuses as often as it gives, and in two shapes.** 4.1.10
न षट्स्वस्रादिभ्यः says यो यतः प्राप्नोति स सर्वः प्रतिषिध्यते —
whichever affix would have come from wherever, ALL are refused. Every
other प्रतिषेध here names what it refuses. The case-runner's guard had
only ever met the second kind, and its rule was that a refusal answers
by the rule that SUPPLIES with its own id on `blocked_by`. This is the
first rule to fall under the carve-out already on record — *unless
refusing is all the rule did* — and the guard now reads the two shapes
off the rows rather than being told them.

**A stem in मन् is a stem in न्, and the code could not see it.**
4.1.11 exists only because 4.1.5 reaches मन्; matching `stem_final` as
an exact string made the refusal have nothing to refuse. The
containment is now DECLARED, not computed from spelling, and the
reason is this project's oldest fault met inside a single field:
`stem_final` holds two kinds of value — a SOUND (अ, ऋ, न्) and a whole
final MEMBER (पाद, ऊधस्, हायन) — and a suffix match would have made
पाद a stem in अ.

**Words doing work far from where they stand, three in thirty-eight
sūtras.** 4.1.13's अन्यतरस्याम् is stated so that 4.1.7's र becomes
optional — six sūtras back. 4.1.18's सर्वत्र is pulled DOWN into
4.1.17, उत्तरसूत्रादिहापकृष्यते, so that ष्फ may beat a rule
fifty-seven sūtras later: **anuvṛtti read backward**, and the vṛtti
says so in as many words. And 4.1.27 takes half of 4.1.26's condition
— संख्याग्रहणमनुवर्तते, नाव्ययग्रहणम् — where anuvṛtti from a given
rule is normally all or nothing.

**A गण whose members do not share a reason.** अजादिग्रहणं तु क्वचिद्
जातिलक्षणे ङीषि प्राप्ते, क्वचित् तु पुंयोगलक्षणे, क्वचित्
पुष्पफलोत्तरपदलक्षणे, क्वचित् वयोलक्षणे ङीपि, क्वचित् टिल्लक्षणे —
five different rules blocked, one each, and हलन्तानां त्वप्राप्त एव
कस्मिंश्चिदाब् विधीयते: some members are there for a case no rule
reached at all. Two later rules of the pāda send their own exceptions
into it — कथं त्रिफला? अजादिषु दृश्यते. **A list that is a residue.**

**Two words fixed from opposite ends, in one rule.** 4.1.32:
अन्तर्वदिति मतुब् निपात्यते, वत्वं सिद्धम्; पतिवदिति वत्वं निपात्यते,
मतुप् सिद्धः — in one the affix is the irregular part and the
sound-change follows; in the other the sound-change is irregular and
the affix follows. One निपातन over two words whose irregularities are
in opposite halves.

**One option making three forms.** 4.1.38 मनोरौ वा. वाग्रहणेन द्वावपि
विकल्प्येते, तेन त्रैरूप्यं भवति — the वा covers this rule's own औ
AND the ऐ carried down from 4.1.37, so मनायी, मनावी and मनुः all
stand.

**And a fourth attribution.** 4.1.17 प्राचाम्, after 3.4.18's प्राचाम्,
3.4.19's उदीचाम् and शाकटायन at 3.4.111 and 3.4.112. The set is read
off the tables rather than listed, so it grows with the work.

**DEBT — चाप् and ङीन् are in the inventory and nothing gives them
yet.** 4.1.73 and 4.1.74 are the rules. Written as an assertion of the
exact shortfall, so it fails the moment they arrive: a debt stated as
what is missing collects itself, a debt stated as a comment does not.

**SCAR — sandhi in a test substring, seventh time.** चेत्युभयथापि joins
च and उभयथा. And two more of the compounding kind, which is the same
fault seen from the other side: पञ्चानाम् is in the vṛtti only as
पञ्चानामिति, परस्मैपदेषु only as परस्मैपदेष्वित्येव.


3.4.80–3.4.117: **अध्याय ३ is finished.** All four pādas run unbroken
from 1 to their last sūtra, checked against the corpus rather than
against a count — every rule that gives an affix after a root, and
every rule that says what one stands for, is codified.

**The eighteen endings, worked on for thirty-three sūtras.** 3.4.78
gave them; 3.4.80 to 3.4.112 replace them, drop letters out of them
and put augments in front of them. Held as one table because it is
one question asked over and over, and it makes the whole run testable
against the enumeration behind it — the same payoff 3.4.77 bought for
the ten, now bought again for the eighteen.

**AN OPTION THAT WILL NOT DIE, AND THE SYLLABLE THAT KILLS IT.** This
is the finding of the block. 3.4.83 विदो लटो वा states an option; the
vṛtti then carries it to 3.4.85, 3.4.86, 3.4.97 and 3.4.98, each time
reading it as a **व्यवस्थितविभाषा** — an option DISTRIBUTED over cases
rather than free within any one. Sixteen sūtras later 3.4.99 says
नित्यम् for one reason only: नित्यग्रहणं विकल्पनिवृत्त्यर्थम्.

The point is not the option but what it costs to end one. **Anuvṛtti
runs until something stops it, so silence would have meant the option
continued.** A mechanism that carries words forward for free charges
a word to stop one — and the test that holds it is the sharpest thing
in the block: 3.4.98 and 3.4.99 drop THE SAME SOUND in THE SAME PERSON
and differ only in which लकार precedes, optional in one and obligatory
in the next rule.

**A WORD PLACED IN ONE RULE FOR ANOTHER TO SPEND.** 3.4.111's vṛtti
says एवकार उत्तरार्थः — the एव in शाकटायनस्यैव does nothing where it
stands. Four sūtras on, 3.4.115's vṛtti collects it: two names would
normally CO-APPLY, एकसंज्ञाधिकारादन्यत्र समावेशो भवति, and what makes
आर्धधातुक REPLACE सार्वधातुक instead of joining it is
इह त्वेवकारोऽनुवर्तते, स नियमं करिष्यति. Both ends of the transaction
are stated in the commentary, which is what makes it checkable rather
than a guess, and both ends are now tests.

**THE PLAINEST REUSE EDGE THE PROJECT HAS HAD.** 3.4.114 आर्धधातुकं
शेषः is defined by SUBTRACTION, and there is exactly one thing it
subtracts from. So `ardhadhatuka` calls `sarvadhatuka` and takes the
name that rule did not give — and the test is not that the verdicts
agree but that **the refusal carries 3.4.113's own words**, because
two implementations of one condition can drift and a passed-through
answer cannot. 3.4.113 was codified early, for 7.3.84's sake, and has
stood alone since; its companion turns out to be defined by it in one
word.

**A rule written early rests on a letter, and now on a whole rule.**
3.4.78's ङ् on the last of the eighteen exists so that तिङ् may be
named; 3.4.113 stands on that name; 3.4.114 stands on 3.4.113. Three
rules, one letter at the bottom.

**Two augments that look as though they compete, and do not.** 3.4.107
सुट् तिथोः against 3.4.102 लिङः सीयुट् — तकारथकारावागमिनौ, लिङ्
तद्विशेषणम्; सीयुटस्तु लिङेवागमी, तेन भिन्नविषयत्वात् सुटा बाधनं न
भवति. **The two attach to different things**, so the apparent conflict
is not one. That distinction is why `kind` is a field on these rows,
and it later settled a real ranking bug: 3.4.92 gives an AUGMENT and
so names no ending, 3.4.93 names the ए of that same ending, and with
equal weights the table order decided. A rule that NAMES what it works
on states more than one that speaks of the class — 3.4.107's own
argument, read as a ranking.

**A rule that says too much, and the excess is the teaching.** 3.4.103
states that यासुट् is ङित् when it is ङित् already by स्थानिवद्भाव.
स्थानिवद्भावादेव ... ङित्त्वे सिद्धे यासुटो ङिद्वचनं ज्ञापनार्थम् —
what it teaches is लकाराश्रयङित्त्वमादेशानां न भवति, that a substitute
does NOT inherit ङित्त्व from what it replaces, and the fruit is
अचिनवम् and अकरवम्.

**Two things wearing one name, settled by a paribhāṣā.** 3.4.106's
इट् is the ENDING of 3.4.78, not the augment of the same name:
आगमस्येटो ग्रहणं न भवति, अर्थवद्ग्रहणे नानर्थकस्य. **The hazard that
keeps splitting field names in this codebase, met in the grammar
itself** — and settled there by a general principle rather than by
renaming, which is the option a codebase does not have.

**SCAR, TWICE IN ONE MODULE.** The voice of an ending is पद, and
`pada` is already asked here for 1.4.14's finished word. What a rule
wants in FRONT would naturally be `after`, and `after` is already
asked for the sound that FOLLOWS. Both are now `ending_pada` and
`preceded_by`, and a test holds the two old names to their old
meanings. Overloading either would have produced a silently wrong
answer rather than an error — which is the whole reason this scar
keeps being worth the rename.

**Two named schools and one named man.** 3.4.111 and 3.4.112 cite
शाकटायन by name where 3.4.18 and 3.4.19 cited प्राचाम् and उदीचाम्.
The two kinds are read differently: naming a school was itself read as
making the rule optional; here the option is in the disagreement —
अन्येषां मते — and not in the citation.

**And the pāda closes by pointing backward.** 3.4.117 छन्दसि उभयथा
lets both names hold at once, and gives one form that takes an
operation from EACH: उप स्थेयाम शरणा बृहन्त — सार्वधातुकत्वाल् लिङः
सलोपः, आर्धधातुकत्वादेत्वम्. Then the vṛtti ends अध्याय ३ with
व्यत्ययो बहुलम् इत्यस्यैवायं प्रपञ्चः: all of this is 3.1.85 spelled
out. The last rule of the chapter names a rule of its first pāda.

**SCAR — ast.parse is not enough.** A patch wrapped a gloss into seven
comma-terminated lines. It parsed cleanly, because `Gloss(a, b, c, d,
e, f, g)` is valid Python; it could not be imported, because Gloss
takes two. The rule was 'always ast.parse BEFORE writing'; it is now
**parse AND import**, since arity, names and types are all past the
parser.

**SCAR — the heredoc ate an escape for the sixth time,** and the rule
against it was already written down. Anything containing a backslash
goes through a file written with the Write tool, never through a
heredoc.

**SCAR — sandhi in a test substring, fifth and sixth time.** इह
त्वेवकारोऽनुवर्तते has no free एवकारः; समावेशश्चैवकारानुवृत्तेः joins
च and एव. And a sūtra's word is rarely free in its own commentary:
पञ्चानाम् appears only as पञ्चानामिति, परस्मैपदेषु only as
परस्मैपदेष्वित्येव. The KEEPS_OUT table now stores each word **as the
commentary writes it**, which also records something true — a word
raised for questioning is joined to इति, and one carried down by
anuvṛtti to इत्येव.

**And one paraphrase caught by a test.** 3.4.111's note rendered
तत्किं लङ्ग्रहणेन as 'so why name it?'. The test wanted the word and
did not find it, which is the right failure: a word recorded as doing
work has to be on record in the words that do it.


3.4.37–3.4.79: **the लकार debt is closed**, and 3.4 now runs unbroken
1 to 79 — which takes in 3.4.79 itself, codified long ago out of order
because a derivation elsewhere stopped without it.

**All three debts paid, and the last one buys a check.** NORTH_STAR has
carried them since 3.2.110, where the लकार table began naming its
endings as bare strings with nothing able to ask what one of them was.
3.4.6 gave the Vedic set; **3.4.69** लः कर्मणि च भावे चाकर्मकेभ्यः says
what a लकार DENOTES — the object, or the doer; after an intransitive
root the act, or the doer again, and सकर्मकेभ्यो भावे न भवन्ति so the
two do not overlap; and **3.4.77** लस्य enumerates the ten and says six
are टित् and four ङित्.

What that last buys is a test nothing could run before: **every ending
the table gives, across 3.2, 3.3 and 3.4, checked against the rule that
lists them.** They agree. Two and a half pādas of work validated
against a single later rule, which is the first time in this project
that has been possible.

**And one rule written early rests on a letter only now read.** 3.4.78
gives the eighteen substitutes, and महिङो ङकारस्तिङ् इति
प्रत्याहारग्रहणार्थम् — the ङ on the LAST of them exists so that तिङ्
may be formed as a pratyāhāra. 3.4.113, codified long before the reading
reached this pāda because 7.3.84 could not strengthen without it,
stands on exactly that name.

**A प्रतिषेध reaching backward, and an earlier rule beating a later
one.** 3.4.23 refuses both क्त्वा and णमुल् — णमुल् from the rule
immediately before, क्त्वा from three back: णमुलनन्तरः, क्त्वा तु
पूर्वसूत्रविहितोऽपि प्रतिषिध्यते. And 3.4.37 wins over 3.4.48 by
**पूर्वविप्रतिषेध**, prior contradiction, which is the reverse of the
परत्व that 3.3.142 used. The resolver reaches the same answer by
specificity, so the two grounds agree here without having to — recorded
rather than relied on.

**The seventh suspension of 3.1.94, and then its bound.** 3.4.24
suspends the principle **wherever those two affixes are given
together** — where the six before it bounded it by section. Then 3.4.47
qualifies that from inside: सर्वस्मिन्नेवात्र णमुल्प्रकरणे क्रियाभेदे
सति वासरूपविधिना क्त्वापि भवति, it holds again once the acts are
distinct. Twenty-three sūtras apart, and the bound is a condition on the
situation rather than on the rules.

**A rule given on a named school's authority, twice** —
प्राचामाचार्याणां मतेन and उदीचामाचार्याणां मतेन — and in both the
naming ITSELF is read as making the rule optional. At 3.4.18,
वासरूपविधिश्चेत् पूजार्थम्: if 3.1.94 is invoked there it is *for
honouring the teachers*.

**One argument used in opposite directions.** 3.4.21 holds
समानकर्तृकता *because* शक्तिशक्तिमतोर्भेदस्याविवक्षितत्वात्; 3.4.26
says the distinction is *not* drawn *because* drawing it would
contradict the condition. Five sūtras apart, neither citing the other.

**And the question itself changes at 3.4.67.** Every rule of these four
pādas so far has asked WHICH AFFIX COMES. From कर्तरि कृत् they ask
what an affix, once it has come, STANDS FOR. That heading is unlike any
before it: it attaches only where the rule giving the affix stated no
sense — तत्र येष्वर्थादेशो नास्ति तत्रेदमुपतिष्ठते — so it **fills gaps
rather than covering ground**, where 3.2.84, 3.3.18 and 3.3.19 all
reached every rule under them. Then 3.4.70's एवकारः कर्तुरपकर्षणार्थः
pulls the doer away again for one class, and 3.4.68 lets seven
particular words have it back. Three adjacent rules adjusting one
another.

**SCAR — two rules about the same words are not the same question.** I
put 3.4.75 on 3.3.1's entry point because both speak of the उणादि
words. They ask different things — *does the word stand* against *what
does it denote* — and sharing the entry point made 3.4.75's worked case
come back by 3.3.2. The case runner caught it. This is the reverse of
the collision that keeps splitting field names, and the same kind of
guard catches both.


3.4.25–3.4.36: **the णमुल् run**, where the companion becomes the
OBJECT of the act rather than a particle. 3.4 now runs unbroken 1 to
36, with 3.4.79 and 3.4.113 still out of order ahead of it.

**One ground used in opposite directions, five sūtras apart.** 3.4.21
holds समानकर्तृकता *because* शक्तिशक्तिमतोर्भेदस्याविवक्षितत्वात् —
the difference between a power and what has it is not meant to be
marked. 3.4.26 says न चास्मिन् प्रकरणे शक्तिशक्तिमतोर्भेदो विवक्ष्यते,
समानकर्तृकत्वं हि विरुध्यते: the distinction is not drawn here
*because* drawing it would contradict the condition. The same argument
made to support a rule and then to keep it out of the way.

**A condition that a ROOT adds nothing.** 3.4.27's सिद्धाप्रयोग —
निरर्थकत्वाद् न प्रयोगमर्हति, and अन्यथा भुङ्क्त इति यावानर्थः,
तावानेवान्यथाकारं भुङ्क्त इति गम्यते: the compound says exactly what
the two words said. 3.3.154 made a condition of a WORD being meant and
not uttered; this makes one of a root contributing nothing to what is
uttered. Two conditions about an absence, and neither about a form.

**A group named by where a run begins.** 3.4.34's इतः प्रभृति कषादीन्
यान् वक्ष्यति — from that rule on, the roots named form a class called
after its first member, and 3.4.46 will govern them all. Every gaṇa
met so far has been a LIST, and two of them are on disk; this one is
defined by an extent.

**And a rule whose form says one thing and means another.** 3.4.25
gives an affix meaning "having made him a thief", and the vṛtti has to
say चोरकरणम् आक्रोशसंपादनार्थमेव, न त्वसौ चोरः क्रियते — the making is
only for the abusing, and nobody is made a thief.

**SCAR — the heredoc ate an escape a fifth time**, and this one
reached disk: a `\n` inside a quoted heredoc arrived as a real newline
and split a string literal in `fieldhelp.py`, so the whole suite failed
to import. The rule has been standing since 3.2 and I keep breaking
it. **Anything containing a backslash goes through a file written with
the Write tool, never through a heredoc** — Git Bash on this machine
processes the escape even inside single quotes, and `ast.parse` before
writing does not help when the corruption happens before the script
runs.


3.4.1–3.4.24: **अध्याय ३ पाद ४ opened**, and one of the three debts it
has been carrying since 3.2 is paid. Two rules of this pāda — 3.4.79
and 3.4.113 — were codified long ago because derivations elsewhere
stopped without them, so it has stood open with two rules in it for a
long time; the reading now arrives at its first sūtra.

**3.4.6 छन्दसि लुङ्लङ्लिटः is codified, and 3.2.105 can stop citing a
rule that did not exist.** It gives three PAST endings for any time at
all in the Veda — and the vṛtti glosses अद्या ममार as अद्य म्रियते, a
perfect meaning a present. 3.4.69 and 3.4.77 are still owed; the tests
now assert which half is settled rather than "all three", which would
have gone green the moment the first was written and told nobody.

**A licence rather than a rule.** 3.4.1 धातुसंबन्धे प्रत्ययाः says
that where two acts stand as qualifier and qualified, an affix stated
for the WRONG TIME is correct anyway — अयथाकालोक्ता अपि प्रत्ययाः
साधवो भवन्ति. Broader than 3.3.131's transfers, which lent one *named*
tense's affixes to a *named* time: here nothing is lent. And only one
way round — विशेषणं गुणत्वाद् विशेष्यकालमनुरुध्यते, तेन विपर्ययो न
भवति, an asymmetry the rule does not state. Everything to 3.4.8 stands
under it, which is why those rules hold **सर्वेषु कालेषु**, in every
time at once, where each rule of 3.2 and 3.3 chose an ending FOR a
time.

**A rule given on a named school's authority, twice.** 3.4.18
प्राचामाचार्याणां मतेन and 3.4.19 उदीचामाचार्याणां मतेन — the teachers
of the east and of the north. Nothing in the three pādas before this
attributed a rule that way, and in both the vṛtti reads the
attribution ITSELF as making the rule optional: प्राचांग्रहणं
विकल्पार्थम्, because the other school's usage stands too. And at
3.4.18, वासरूपविधिश्चेत् पूजार्थम् — if 3.1.94 is invoked here it is
**for honouring the teachers** and not for the grammar. A principle
cited as a courtesy.

**A seventh suspension of that same principle, bounded by a pair of
affixes.** The six before it fenced 3.1.94 off by SECTION — the
तच्छीलादि run, the क्रियार्थ ground, the feminine section and what
follows it. 3.4.24 asks ननु च वासरूप इति भविष्यति? and answers
क्त्वाणमुलौ यत्र सह विधीयेते तत्र वासरूपविधिर्नास्ति: **wherever in
the grammar those two affixes are given together.** One test now holds
all seven so an eighth has somewhere to go.

**A प्रतिषेध reaching backward past its neighbour.** 3.4.23 refuses
both क्त्वा and णमुल्; णमुल् is given in the rule immediately before,
but क्त्वा comes from 3.4.21 — णमुलनन्तरः, क्त्वा तु
पूर्वसूत्रविहितोऽपि प्रतिषिध्यते. 3.3.45 had shown the nearest word
LOSING to a further one in an अनुवृत्ति; this shows a refusal reaching
past its neighbour to take in an earlier rule as well.

**A philosophical ground for a grammatical condition.** 3.4.21's
"same doer" holds because शक्तिशक्तिमतोर्भेदस्याविवक्षितत्वात् — the
difference between a power and what has it is not meant to be marked.
The first ground of that kind in this reading. And its dual is read as
not binding — द्विवचनमतन्त्रम् — so more than two acts are reached,
which is the same move 3.3.18 made on its own masculine singular.

**And the commentary saying brevity is no consideration.** 3.4.5:
लाघवं च लौकिके शब्दव्यवहारे नाद्रियते. A tradition that prizes brevity
in its own sūtras above almost everything, saying in passing that the
value does not apply to the language those sūtras describe. Recorded
because it is a statement about method, not about grammar — as 3.3.131's
concession that a whole section need not have been written was.

**SCAR — twenty-two notes carrying a literal backslash-n.** The
escaping depends on HOW a file is written and I used one convention in
the other kind. In a patch script the module's text sits inside a
Python string, so a doubled escape there becomes a single one in the
module and Python reads a newline; written straight to the module, a
doubled escape IS the text and Python reads backslash-plus-n. Every
module built by patch script was right; every one written directly was
wrong wherever I reached for the habit. **Nothing broke** — the notes
simply read `\n\n` where a paragraph break belonged — which is
exactly why nothing caught it. A guard now asserts the property across
every table in the project and every registered note at once, rather
than at the places it happened to bite.

**And the sandhi trap, a fourth time, plus its look-alike.** A test
substring failed because नास्ति + इति + एतत् runs together as
नास्तीत्येतत्. That is not the same failure as a quotation broken by a
LINE WRAP, which bit three times and is now handled by
`tests.unwrapped` — flattening whitespace finds a wrapped phrase, and
no amount of it will find a word sandhi has eaten. The two look alike
and only one has a mechanical fix; the other has to be read.


3.3.56–3.3.176: **अध्याय ३ पाद ३ is complete** — 176 sūtras,
contiguous, eleven entry points that partition it. With 3.2 that is two
whole pādas of this adhyāya.

**The debt six rules were carrying, paid — and it closed a heading
exactly where a rule sixty back said it would.** 3.3.113 कृत्यल्युटो
बहुलम् is the commentary's standing answer wherever a run does not give
a form usage has: 3.2.53, 3.2.153, 3.3.24, 3.3.26, 3.3.43 and 3.3.44
each sent one there. Three separate tests, written in three files
across two pādas, asserted it was uncodified so that writing it would
go red. All three did. And it turned out to do a second thing: भावे
अकर्तरि च कारक इति निवृत्तम् — the two conditions running since 3.3.18
and 3.3.19 stop at this rule, which **3.3.56 had stated fifty-seven
sūtras early by naming it**: यावत् कृत्यल्युटो बहुलम् इति. A claim made
early and confirmed by the rule it named, as 3.2.134's आ क्वेः was.

**And it resolves nothing, on purpose.** बहुलम् is the same refusal
3.3.1 makes about the उणादि affixes at the other end of the pāda, and
the two bracket it: one licenses a text the grammar does not contain,
the other licenses forms it does not derive. What the codification can
say is WHICH KIND of going-beyond the vṛtti means — three, kept apart —
and it says that and no more.

**A rule naming its roots by a संज्ञā, and the resolver asking for it.**
3.3.92 and 3.3.93 want a root called घु, which 1.1.20 दाधा घ्वदाप्
confers and which is codified as `is_ghu`. The rows list no roots: they
**call**. A test then walks the whole class from 1.1.20 and checks each
member reaches 3.3.92, and a non-member does not. The second real
cross-adhyāya call in this pāda after 3.3.14's to 3.2.127.

**The वासरूप suspension is now fenced off at both ends.** 3.1.94 lets a
general affix stand beside the special one excepting it. Four rules had
suspended it over ground marked out by argument (3.2.146, 3.2.177,
3.3.10, 3.3.44). **3.3.107 bounds it from inside** —
वासरूपप्रतिषेधश्च स्त्रीप्रकरणविषयस्यैवोत्सर्गापवादस्य, it holds only
within the feminine section — and **3.3.163 from outside**:
स्त्र्यधिकारात् परेण वासरूपविधिर्नावश्यं भवति, after that section it is
not obligatory. 3.3.167 and 3.3.169 then cite 3.3.163 as settled. Six
suspensions, and a test holds all six so a seventh has somewhere to go.

**A condition about another rule having applied.** 3.3.139's
लिङ्निमित्त asks whether some rule would have given लिङ् here — a fact
about the GRAMMAR'S own state, where every condition before it was
about the act, the speaker, the company or the form. Its content
arrives seventeen sūtras later at 3.3.156, so a reader of 3.3.139 could
not know what satisfied it; both ends now name each other. 3.3.146 then
uses the same fact negatively: लिङ्निमित्तमिह नास्ति तेन लृङ् न भवति.

**A condition on a word being MEANT and NOT SAID.** 3.3.154 wants अलम्
understood and not uttered — सिद्धश्चेदलमोऽप्रयोगः, यत्र गम्यते चार्थो
न चासौ प्रयुज्यते — and its counter-example is that very word spoken.
Nothing in either pāda had made a condition of an absence.

**A commentary conceding that a stretch of the grammar need not have
been written.** At 3.3.131: for a reader who holds the WORD is
present-tense and the other time comes from the sentence, तादृशं
वाक्यार्थप्रतिपत्तारं प्रति प्रकरणमिदं नारभ्यते. Recorded and not acted
on — the rules are in the text, so they are in the codification, and a
test says so.

**Three gaṇas on disk, and one I copied out by hand anyway.** The
गणपाठ keys गम्यादि to 3.3.3, भिदादि to 3.3.104 and संपदादि to 3.3.108.
3.2.5 and 3.2.15 had already taught that the corpus is the authority
for its own lists; I applied that in 3.2 and did not carry it into 3.3,
so 3.3.3's गम्यादि was typed from the vṛtti's running text and came to
**ten members where the corpus has nine** — आगामी for आगमी, and an
आयायी the list does not carry. Both now read from the corpus. Asking
the गणपाठ which gaṇas it keys to the pāda you are in is a thirty-second
check, and this is the second pāda in a row where skipping it cost
something.

**A guard that was crying wolf, and one that was silent.** Three sūtras
corpus-wide were reported as WITNESSES DIVERGE about texts that agree —
GRETIL writes ṝ as ṛ plus a combining macron where Vidyut uses the
precomposed letter, and NFC makes them one word. Fixed in `_normalize`.
The opposite failure came from a patch script: a rename had turned
`_GHAN` into `_BHAVA_KRT`, and a later patch widening that constant's
range matched nothing and **wrote nothing, silently** — eighteen rules
left pointed at the wrong entry point until three tests caught it. Every
patch validates before it writes; that one asserted the rows it added
and not the line it edited. **Assert the edit, not just the insert.**

**A citation of my own that was wrong, caught by a test of my own.**
3.3.107's note said the same ambiguity had been settled "from the SENSE
(3.2.162's साहचर्यात्)". 3.2.162 says स्वभावात्. Two different grounds
merged into one wrong citation, and the test caught it *because it
named the place* — which is exactly what
`test_astadhyayi_attribution.py` was built for. Four grounds are now on
record for choosing between two roots spelt alike, and they are
genuinely different: साहचर्यात् from the company a word keeps,
स्वभावात् from how the world is, अनभिधानात् from there being no such
word, and 3.3.107's own — from the reading that would make the rule say
nothing new.

**A heading stopping is not the sense stopping.** 3.3.113 closes
भावे and अकर्तरि च कारके, and I wrote two tests reading that as "no
rule after this has anything to do with भाव". 3.3.114 नपुंसके भावे
क्तः says भावे in its own words one sūtra later. निवृत्तम् means the
conditions stop RUNNING — later rules must SAY them — and that is the
whole point of an अधिकार. The same mistake then repeated for
भविष्यति at 3.3.16. Both tests now assert the distinction rather than
eliding it.

**A gender outranks a named root.** हसितम् came back as हसः, because
3.3.62 names हस् and 3.3.114 said only "neuter, in the sense of the
act". But the three gender runs at the close of the pāda are अपवाद by
the commentary's own word — 3.3.94 is घञजपामपवादः — so naming a gender
is the strongest thing a rule here does, and the ranking now says what
the text says.

**Some smaller things that had no precedent in 3.2.** A letter put in a
sūtra to keep the sūtra *sayable* (3.3.57's दकारो मुखसुखार्थः). A whole
sūtra existing for an accent (3.3.96), and asked why its wording does
not construe, the commentary answers वैचित्र्यार्थम् — for variety. A
rule protecting half of itself from its own other half, three times
(3.3.169, 3.3.172, 3.3.174). An अनुवृत्ति inherited *minus one word*
(3.3.138's अवरस्मिन्वर्जं पूर्वमनुवर्तते). A निपातन whose whole content
is a single sound (3.3.70's लत्वार्थं निपातनम्) and another whose work
is entirely negative (3.3.123). And at 3.3.175 a form in actual use is
called simply **wrong** — असाधुरेवायम् — then half-saved by an opinion
the commentary reports and does not adopt. Everywhere else in these two
pādas an awkward form was parsed away, sent to 3.3.113, or admitted by
बहुलम्.

**And a scar that has now bitten three times, fixed at last.** Notes
are stored wrapped, so a quoted phrase longer than a few words falls
across a line break and `assertIn` misses it. Three tests had their
quotations shortened to get round it, which weakens them for no reason.
`tests.unwrapped` flattens the wrapping; the quotations are back in
full. It is NOT a fix for sandhi — ततोऽन्यत्रापि contains no
independent अ however it is wrapped — and the two failures look alike
only on the surface.


3.3.1–3.3.55: **the opening of अध्याय ३ पाद ३** — the three rules that
license what the grammar does not derive, everything under भविष्यति, and
the घञ् run to its end. 3.3 runs unbroken 1 to 55.

**A text that was on disk and unread.** 3.3.1 उणादयो बहुलम् licenses the
उणादि affixes, and those are a separate work of 748 sūtras in five pādas
— `reference/mula/ancillary/vidyut-unadipatha.tsv`, which nothing in
`src/` had ever opened. The Kāśikā's first citation under the rule,
प०उ० १.१ कृवापाजिमिस्वदिसाध्यशूभ्य उण्, is that file's first row
verbatim. So the codification holds a **locator** into the text and
quotes it back rather than restating the affix, and a test asserts the
citation resolves. The instruction to leverage what is already
downloaded paid here more directly than anywhere yet.

**बहुलम् refuses to be resolved, and the entry point says so.** यतो
विहितास्ततोऽन्यत्रापि भवन्ति; केचिदविहिता एव प्रयोगत उन्नीयन्ते — some
of these affixes were never prescribed at all and are inferred from
usage. A word's ABSENCE from the list therefore refuses nothing, and
`unadi()` answers 3.3.1 with an empty locator instead of a refusal.

**The future rules went into the past's table, not a second one beside
it.** 3.3.4–15 ask exactly what 3.2.110–122 ask — which tense-ending,
given a time and a situation of speaking — and `Lakara` already carried
a per-row `time` defaulting to the past, with the resolver filtering on
it. Rows, not a new module. Two tests hold the seam: no past question
may reach a future rule and none the other way.

**A rule that states nothing of its own.** 3.3.14 लृटः सद्वा names its
affixes by the संज्ञा 3.2.127 conferred — सत् — and takes its conditions
from 3.2.124: अप्रथमासमानाधिकरणादिषु नित्यम्, अन्यत्र विकल्पः. So
`lrt_substitute` **calls** `sat_samjna` rather than restating शतृ and
शानच्. The dependence is a call, not a declaration.

**The same guard, the opposite remedy.** 3.3.12 declared it reuses
3.2.1 — कर्मण्यण् इति सामान्येन विहितो … पुनरण् विधीयते, it IS that
affix said again — and the row then hardcoded `"aṇ"`. The reuse guard
caught it: *declares 3.2.1 and reaches none of its functions.* A pāda
back the same guard caught 3.2.3 → 1.1.71, where the declaration was
FALSE and came out. Here it is **true and the code was not living up to
it**, so the code changed: the row names the rule it restates and the
affix is fetched from it. A declared reuse whose code holds a copied
string is a claim the guard cannot check.

**Two more ways a condition travels, neither inferable from position.**
3.2.122 had shown मण्डूकप्लुति, a condition vaulting forward over rules
that had explicitly dropped it. 3.3.49 shows **सिंहावलोकितन्याय, the
lion's backward glance**: the विभाषा *about to be stated* at 3.3.50 is
read BACK into it — वक्ष्यमाणं विभाषाग्रहणमिह सिंहावलोकितन्यायेन
संबध्यते. And 3.3.45 shows the **nearest word losing to a further one**:
दृष्टानुवृत्तिसामर्थ्याद् घञनुवर्तते, नानन्तर इनुण् — 3.3.44's इनुण्
stands immediately before and is not what carries down. Three facts,
three rules, and a test that holds all three together so a fourth has
somewhere to go.

**वासरूप suspended twice more, and once by a new device.** 3.1.94 lets a
general affix stand beside the special one excepting it. 3.2.146 argued
that the तच्छीलादि section suspends it and 3.2.177 exists because of the
suspension. 3.3.10 establishes it again over other ground — क्रियायाम्
उपपदे क्रियार्थायां वासरूपेण तृजादयो न भवन्ति — and **3.3.11 and 3.3.12
exist only because of what it took away**. Then 3.3.44 does it a fourth
time by a different means: भाव इति वर्तमाने पुनर्भावग्रहणं
वासरूपनिरासार्थम् — saying a word that was already running, and the
repetition cancels 3.1.94. Repeating a running word was known to WIDEN
(3.2.106, 3.2.124) and to FENCE OFF (3.1.141, 3.2.14); this is a third
use of it.

**A commentary deciding between two witnesses to the mūla — the first
time.** At 3.3.55 GRETIL reads प्रौ and Vidyut परौ. Those are different
preverbs, not a spelling or a sandhi, and no amount of comparing two
mūla texts settles it. The Kāśikā does: परिशब्द उपपदे भवतेः, and every
form it gives is परिभावः, परिभवः. **परौ stands and GRETIL is wrong
here.** The collation had already flagged the pair; what the commentary
adds is which witness to believe.

**And a guard that was crying wolf.** Three sūtras corpus-wide —
3.3.30, 7.2.38, 8.3.10 — were reported as **WITNESSES DIVERGE, check
before relying on this text** about texts that agree exactly. GRETIL
writes ṝ as ṛ plus a combining macron, Vidyut uses the precomposed
letter; composed under NFC they are one word. Fixed in `_normalize`,
whose own docstring already said it strips what editions differ on
without touching what they say — and an encoding choice is exactly
that. A guard that warns about agreement is worse than none, because
the warnings that matter stop being read.

**यथासंख्यम् binding three lists at once.** 3.2.5 and 3.2.13 bound two
lists of words; 3.2.186 bound a kāraka to a kind of being. 3.3.37
परिन्योर्नीणोर्द्यूताभ्रेषयोः binds preverb, root AND sense in one
stroke — द्यूतविषयश्चेन्नयतेरर्थः, अभ्रेषविषयश्चेदिणर्थः — so the row
holds triples, and a test crosses the lists four ways to show none of
them stands.

**Two conditions that one field cannot hold, twice.** 3.3.33 wants the
sense to be spreading AND what is spread not to be speech; 3.3.40 wants
the thing within reach AND the taking not a theft. Written on one axis
each pair cancels — one input cannot be प्रथन and शब्द at once — and
विस्तरो वचसाम् and फलप्रचयश्चौर्येण could not be tested at all. Both are
now second axes. The ninth and tenth field-name collisions, and eight of
the ten have split.

**Two rows carrying one sūtra number.** 3.3.16's vārttika स्पृश उपताप
holds one of that rule's four roots to AFFLICTION, and it changes the
output: without it the rule reaches स्पर्शो देवदत्तः, which takes
3.1.134's अच् instead — स्वरे विशेषः, the two differing in accent alone,
which the unaccented sūtrapāṭha on disk cannot show. 3.2.24 had already
settled that such a vārttika belongs in the table and not in a note.

**The debt that keeps being incurred.** 3.3.113 कृत्यल्युटो बहुलम् is
the commentary's standing answer wherever a run does not give a form
usage has. Two rules of 3.2 leaned on it; **four more of this run do**
— 3.3.24, 3.3.26, 3.3.43, 3.3.44 — and 3.3.43 invokes it for the
irregularity itself rather than for one form. It is codified in this
very pāda, so one test will collect all six.

**DRY, three times, all of it forced by the work rather than tidiness.**
3.2's registration had grown two parallel if/elif chains, function and
description chosen separately, which had to be kept in the same order by
hand; eleven kinds meant twenty-two branches and a rule could get one
entry point with another's description. One dispatch table now. `lakara`
and `bhava_krt` each had a filter and a ranking enumerating every field
by hand — two lists to keep in step, about to double — and each now
iterates one declaration. And `sense` became a tuple because 3.3.41
names four at once, rather than gaining a second field meaning "any one
of these", which is how two ways to say one thing drift apart.

**SCAR — a patch that asserted its rows and not its dispatch.** Renaming
`ghan_affix` to `bhava_affix` also turned `_GHAN` into `_BHAVA_KRT`, and
a later patch widening the dispatch range matched `_BHAVA =`, found
nothing, and **wrote nothing, silently**. Eighteen rules stayed pointed
at the wrong entry point until three tests caught it. Every replace in a
patch script is asserted before the write; this one asserted the rows it
added and not the line it edited. *Assert the edit, not just the
insert.*


3.2.178–3.2.188: **अध्याय ३ पाद २ is complete** — 188 sūtras, contiguous,
each answered by exactly one entry point. The corpus is what says the pāda
ends here, not a number chosen by us: 3.2.189 has no text, and the test
asks the corpus rather than asserting the count.

**One word doing two different jobs a hundred sūtras apart.** दृश्यते at
3.2.75 was read प्रयोगानुसरणार्थम् — the rule follows usage rather than
manufacturing forms. At 3.2.178 the same word is
विध्यन्तरोपसंग्रहार्थम्: it gathers in operations BESIDES the affix —
क्वचिद् दीर्घः, क्वचिद् द्विर्वचनम्, क्वचित् संप्रसारणम्. Nothing in
either sūtra distinguishes them; only the commentary does. Each note now
names the other.

**And the vṛtti catches a redundancy in its own verse.**
जुग्रहणेनात्र नार्थः, भ्राजादिसूत्र एव गृहीतत्वात् — जु was named at
3.2.177 already. The commentary auditing the list it has just supplied is
worth recording, because it is the same move we make against our own tables.

**Two rules dividing a single WORD between them.** 3.2.179 gives क्विप्
where a name is meant, 3.2.180 gives ड where one is not, and the
counter-example of the second IS the example of the first —
असंज्ञायामिति किम्? विभूर्नाम कश्चित्. So विभुः is the all-pervading and
विभूः is somebody so called. `samjna` is tri-state for that reason, as
five conditions before it are.

**A ज्ञापक drawn from ORTHOGRAPHY.** 3.2.182 spells one of its thirteen
roots दश and not दंश, and दंशेरनुनासिकलोपेन निर्देशो ज्ञापनार्थः — the
spelling itself licenses the nasal dropping before affixes other than
कित् and ङित् ones, giving दशनम् by ल्युट्. 3.2.111 and 3.2.126 drew the
same kind of evidence from compound form; this draws it from how a rule
is written down.

**A condition about what a thing BELONGS TO.** 3.2.183's हलसूकरयोः is
neither what the instrument does nor what it is called: पोत्रम् is a
ploughshare and a boar's snout and nothing else. No rule of the pāda had
asked that before, and a test asserts it is still the only one.

**A कारक paired crosswise with a kind of being.** यथासंख्यम् has bound
two lists of words several times in this pāda; 3.2.186 uses it to bind a
kāraka to a kind of being — ऋषौ करणे, देवतायां कर्तरि. Of a seer पवित्र
names the means of purifying, of a deity the one who purifies. One form,
two readings, settled by what it is said of.

**A rule excepting another of its own pāda, and naming it.** 3.2.102 gave
the affix called निष्ठा for the past. 3.2.187 and 3.2.188 give क्त in the
PRESENT, and 3.2.187's vṛtti says why they must —
भूते निष्ठा विहिता वर्तमाने न प्राप्नोतीति विधीयते. Eighty-five sūtras
apart. They are codified from **beside 3.2.102 rather than from the affix
table**, because the question they answer is the one it answers
differently: a reader asking when क्त comes should find all three
together. Each of the three names the others.

**Scar — the table and the heading do not have the same extent.**
3.2.178–186 live in `tacchila.py` because they are affix rules of like
shape; आ क्वेः ends at 3.2.177. Two tests had asserted the two coincide,
which was true only while the module happened to stop where the heading
did. A module boundary is not a textual boundary, and the tests now
assert both halves — rules inside the span fall under the heading, rules
beyond it are in the table and NOT under it. The vṛtti complicates it
rather than settling it: at 3.2.178 it still says ताच्छीलिकेषु, so the
senses reach past the point the heading formally stops. Recorded, not
resolved.


3.2.156–3.2.177: **the तच्छीलादि heading is complete** — all 44 rules
of it, 3.2.134 to 3.2.177, closed from both ends. 3.2 now runs unbroken
1 to 177.

**A debt paid by finishing the section it belonged to.** 3.2.134 bounds
itself by NAMING 3.2.177 rather than giving a number, so while that
rule was unread the extent could be stated but not checked. Reading it
turned the debt test red on schedule. That is the third gap this
session written as a failing assertion and then collected by the work
itself, after 3.2.59's क्विप् contrast and 3.2.128's pratyāhāra.

**And the heading's last rule closes an argument its middle opened.**
At 3.2.146 the vṛtti reasoned that prescribing वुञ् where ण्वुल् gives
the same form must be telling us something — ताच्छीलिकेषु
वासरूपविधिर् नास्ति. Thirty-one rules later 3.2.177 asks why क्विप् is
stated when 3.2.76 gives it already, and answers from that same
ज्ञापक: ताच्छीलिकैर् बाध्यते — this section's affixes would displace
it, and वासरूप being suspended it could not stand beside them. **The
rule exists because of the suspension.**

**Two rules corroborating each other across fourteen.** 3.2.153 asked
whether its refusal was needed when 3.2.167 would displace the युच्
anyway, and cited कम्रा beside कमना, कम्प्रा beside कम्पना as evidence
that both could stand. Those are 3.2.167's OWN forms. Each note now
names the other, so a reader arriving at either finds the pair.

**A question settled स्वभावात्, twice in two rules.** At 3.2.161 it
decides the affix names the thing acted on — wood is broken, it does
not break; at 3.2.162 it picks between two roots spelt alike. Every
other root ambiguity in this pāda was settled from the TEXT
(लुग्विकरणत्वात्, साहचर्यात्, द्वयोरपि ग्रहणम्), so an argument from
how the world is stands out, and both kinds are in use side by side.

**Conditions about a stem already built.** 3.2.166 and 3.2.176 want a
यङन्त, 3.2.168 a सन्नन्त, 3.2.170 a क्यन्त. Every condition before
these was about the root itself; these are about something made from it
before the rule can reach it. And क्य at 3.2.170 stands for three
affixes at once — सामान्येन निर्देशः, one syllable naming क्यच्,
क्यङ् and क्यष् without being a pratyāhāra.

**And the same wrong assumption, written three times.** I kept
asserting that a rule exclusively owns the roots it names — in this
block's tests, in the previous block's, and in the worked inputs. It
failed every time, for one reason: **root-sharing is the norm in this
section**, thirteen pairs of rules sharing at least one, and where they
do the commentary usually gives forms from BOTH — स्थास्नुः and
स्थावरः, जयी and जिष्णुः, गत्वरः and आगामुकम्. That is the समावेश the
vṛtti allows when it calls the suspension प्रायिक, so the data was
saying what the text says. The remedy is the `wants=` idiom two other
entry points already had: a per-rule claim names the affix it asks
after.


3.2.141–3.2.155: **घिनुण्, वुञ्, युच्, उकञ् and षाकन्**, all still
under 3.2.134's heading. 3.2 now runs unbroken 1 to 155.

**A principle codified elsewhere, suspended for a whole heading.**
Three rules of this run appeal to one ज्ञापक — ताच्छीलिकेषु
वासरूपविधिर् नास्ति — and 3.2.146 argues rather than asserts it:
ण्वुलैव सिद्धे वुञ्विधानं ज्ञापनार्थम्, ण्वुल् would have produced the
very same form, so prescribing वुञ् cannot be for the form's sake and
must be telling us something else. **3.1.94 is codified**, and its own
notes already record that it suspends the अपवाद principle for the कृत्
section at large. This heading then suspends the suspension. Nothing in
the code changed — a ranked table already picks one winner — but the
reason it gives one answer is now the text's and not the table's.

**And the suspension is general, not absolute.** प्रायिकं चैतद्
ज्ञापकम्, क्वचित् समावेश इष्यत एव — कम्रा युवतिः beside कमना युवतिः.
Recorded as a scar, since the resolver can only name one rule.

**Thirteen pairs of rules in this run share a root.** I had assumed
each list rule owned its members and wrote a test saying so; it failed
at once. Most of the sharing resolves on other conditions — 3.2.143 to
3.2.145 each want a particular preverb, 3.2.138 wants the Veda where
3.2.139 does not — but लष्, पत् and पद् sit in both 3.2.150 and
3.2.154, and the vṛtti gives forms from EACH: लषणः, पतनः against
अपलाषुकम्, प्रपातुका. That is the समावेश just quoted, met in the data.
The test now asserts the property that holds — a named root is answered
by a rule that names it — rather than one I had supposed.

**A root picked out of a homograph pair by its CLASS**, twice on one
ground four rules apart: लुग्विकरणत्वात्, at 3.2.142 for पृची and at
3.2.145 for वस्. A root that loses its class-marker cannot be
identified by it, so it cannot be the one a rule names.

**A scar the commentary itself will not resolve.** सूदेर् युचि
प्रतिषिद्धे कथं मधुसूदनः? Three explanations are offered at 3.2.153
and none chosen — अनित्य by योगविभाग, or नन्द्यादि, or ल्युडन्त by
3.3.113. That last is the same uncodified rule 3.2.53 leans on, and
both notes now name it, so they surface together when it lands.

**And a guard taught the right lesson about itself.** `CITES_ANOTHER`
exempts rules that legitimately answer by another and is capped at ten
so it cannot become a dumping ground. Four entries of ONE shape had
gone in across this pāda — 3.2.23, 3.2.113, 3.2.152, 3.2.153, every one
a प्रतिषेध answering by its supplier — and four of a shape is precisely
the habit the cap exists to catch. The fix was not to raise it. The
test now reads the refusing sūtras **out of the codification itself**,
any row carrying `refuses`, and asserts something stronger than the
exemption did: that the refusing rule is actually named on
`blocked_by`. **When a guard fires repeatedly for one reason, the
reason belongs in the guard** — the same move the census tests forced
twice before, a stale range becoming a contiguity check and a stale
list of names becoming a partition check.


3.2.134–3.2.140: **habit, office, and doing well.** 3.2 now runs
unbroken 1 to 140.

**A heading bounded by naming its last rule.** 3.2.134 आ क्वेः reaches
as far as the क्विप् of 3.2.177, and अभिविधौ चायम् आङ् — the आ is
inclusive, so that rule is covered too. 3.2.84's भूते gave its extent
implicitly and ended where another time was named; this one points at
a sūtra forty-three rules ahead. The second heading of the pāda, and
the first whose end is a name rather than a boundary.

**Three senses conferred at once, and the vṛtti separates them**
because the first two look alike and are not:
तच्छीलो यः स्वभावतः फलनिरपेक्षस्तत्र प्रवर्तते — by nature, with no
eye to the outcome; तद्धर्मा तदाचारः, यः स्वधर्मे ममायमिति प्रवर्तते
विनापि शीलेन — as one's OFFICE, whether or not it is one's bent;
तत्साधुकारी यो धात्वर्थं साधु करोति — well. **None of the three is an
input**, because no rule of the run divides on which, and a test says
so: offering a caller a choice the grammar does not make would mislead
more than it helps.

**A condition knowable only by reading forward.** 3.2.137's छन्दसि runs
on into 3.2.138 and stops only at 3.2.139, which says so itself —
छन्दसीति निवृत्तम्. I wrote 3.2.138 without it, and the cost was exact:
3.2.138 and 3.2.139 both name भू, they tied on stated conditions, the
earlier row won on table order, and **भूष्णुः was lost**. With the
condition the root divides by register as it should — भविष्णुः in the
Veda, भूष्णुः outside. After 3.2.122's मण्डूकप्लुति this is the second
time a running condition could not be read from its neighbours; there
it leapt forward, here it had to be recovered from where it stops.

**The commentary teaches as well as explains.** 3.2.139's affix is
marked ग and not क्, and three consequences follow — स्था does not
become स्थी, no guṇa comes, भू takes no augment. The vṛtti works each
out against 1.1.5 and 7.2.11, then packs all three into a verse:
क्स्नोर्गित्त्वान्न स्थ ईकारः क्ङितोरीत्वशासनात् / गुणाभावस्त्रिषु
स्मार्यः श्र्युकोऽनिट्त्वं गकोरितोः. The first कārikā this project has
met in the Kāśikā.

**A third debt asserted and paid inside one session.** 3.2.128's तृन्
pratyāhāra runs from 3.2.124 to the न of तृन् at 3.2.135. When that
block was written the near end existed and the far one did not, so the
span could be recorded but not checked — asserted as a test with a
message saying what to do when it went red. Reading this run codified
3.2.135 and the test failed on the next full run. After 3.2.59's
क्विप् contrast, that is twice a debt has been written as a test and
then collected by the reading itself.

**Two debts remain open**, both asserted the same way: 3.2.53's
चौरघातो हस्ती, which the vṛtti answers from the uncodified 3.3.113;
and this heading's far end, since 3.2.177 is not yet read.


3.2.123–3.2.133: **the present, and what replaces it.** 3.2 now runs
unbroken 1 to 133.

**The block boundary is the text's own.** 3.2.123 वर्तमाने लट् is
exactly where 3.2.84's भूते heading stops — not because a count ran
out but because another time is named. And the present is defined by
the act's own course rather than by the moment of speaking:
प्रारब्धोऽपरिसमाप्तश्च वर्तमानः, begun and not finished.

**A pratyāhāra whose members are RULES.** At 3.2.128 the vṛtti asks how
2.3.69's षष्ठीप्रतिषेध can apply if these affixes are not लादेश at all
— सोमं पवमानः — and answers तृन्निति प्रत्याहारनिर्देशात्: क्व
संनिविष्टानां प्रत्याहारः? लटः शतृ० इत्यतः प्रभृति आ तृनो नकारात्.
An abbreviation running from 3.2.124 to the न of तृन् at 3.2.135. The
device that abbreviates a span of SOUNDS, turned on a span of the
grammar itself. A test holds both ends and notes that the far one is
not codified yet.

**A compound's own word-order taken as evidence.** 3.2.126's
लक्षणहेत्वोरिति निर्देशः पूर्वनिपातव्यभिचारलिङ्गम् — हेतु should have
stood first by the rules governing compound order, and its NOT doing so
is the sign that those rules are departed from. The second time this
pāda argues from a compound's form, after 3.2.111's बहुव्रीहिनिर्देश,
so reading the shape of a word as an argument is now attested twice.

**A seventh use of repetition — and it is one already seen.** 3.2.124's
लड्ग्रहणम् अधिकविधानार्थम् lets the substitution reach PAST its stated
condition: सन् ब्राह्मणः agrees with a first-case word, which the rule
excludes. That is the same widening 3.2.106's लिड्ग्रहण did. Six of the
seven jobs repetition does in this pāda are now distinct; widening is
the one attested twice, which makes it a device rather than a reading.

**A term reused rather than split, and the rule for deciding which.**
3.2.129's ताच्छील्य is glossed तत्स्वभावता — word for word what 3.2.78
and 3.2.11 were given — so the field is SHARED. That is the opposite
call from 3.1.149's समभिहार, which had to be kept apart from 3.1.22's
because the vṛtti glossed the two differently. **The decision turns on
the commentary's gloss, not on the word being the same**, and both
directions are now on record.

**And the census stopped naming its kinds.** It had asserted a set of
six entry-point names and went stale the moment a seventh and eighth
arrived — the range lesson in a new costume. It now asserts only that
the kinds PARTITION: every registered sūtra in exactly one, none in
two, none in none. That survives the pāda growing, which no count has.


3.2.110–3.2.122: **which tense-ending comes, and when.** 3.2 now runs
unbroken 1 to 122 — which is exactly where 3.2.84's भूते heading
stops, so the block ends where the heading does.

**A sixth kind of rule, in a module of its own.** Everything in 3.2 up
to here answered one question: which affix a root takes when a word
stands beside it. These thirteen answer another — which लकार is used —
and their conditions are about TIME and about the situation of
speaking: whether it happened today, whether the speaker saw it,
whether a question is being asked or answered, whether the speaker
expects more to follow. A table of उपपद affixes could hold them only
by pretending they were the same kind of thing.

**The future ending, for a past act.** Every rule of the run stands
under भूते. 3.2.112 अभिज्ञावचने लृट् nonetheless gives the FUTURE
ending: what is remembered was future to the remembering, so the ending
looks forward from inside the memory rather than back from the
speaking. Nothing in the code needed changing for it. What it unsettles
is the assumption that an ending's name tells you the time.

**Two conditions that needed three states, because two rules take
opposite sides.** 3.2.115 requires परोक्ष; 3.2.119 requires its
ABSENCE. 3.2.118 and 3.2.119 share the companion स्म and differ in
nothing else, which makes them the sharpest witness the run has. The
same for साकाङ्क्ष: 3.2.114 requires it and 3.2.113's refusal holds
only where it is absent. I first wrote 3.2.113 as a flat refusal and it
swallowed 3.2.114's option — **the vṛtti draws the line itself**,
वासमात्रं स्मर्यते, न त्वपरं किंचिल् लक्ष्यते, तेन उत्तरसूत्रस्य
नायं विषयः.

**A condition that arrives by leaping.** 3.2.122's अनद्यतन comes down
from 3.2.111 by **मण्डूकप्लुति**, a frog's leap — vaulting over 3.2.120
and 3.2.121, which had let it go (अनद्यतने परोक्षे इति निवृत्तम्).
The first this project has met, and a reminder that अनुवृत्ति is not
simply positional. The codification cannot represent running conditions
at all, so what a leap changes is only which rows should state one; the
note is the record that the question was asked.

**A term defined by what speakers believe.** 3.2.115 asks whether every
act is not out of sight, since one sees things and never actions — ननु
च धात्वर्थः सर्वः परोक्ष एव? — and answers that people do take
themselves to see an act in its participants, and परोक्ष is where they
do not. It can hold even of oneself: सुप्तोऽहं किल विललाप. A
grammatical condition resting on a belief rather than on a fact, which
is a kind of definition the project had not met.

**DEBT — the लकाराः are not codified.** What a लकार IS, and what it
becomes, is settled at 3.4.69 and 3.4.77 and after, and 3.4.6 is not
written either — 3.2.105 already had to cite it. So these rules name
their endings as strings and nothing here can ask what an ending is. A
test asserts the debt and goes red when 3.4 lands.

**And the census went stale a fifth time.** It counted five kinds of
rule and a sixth arrived. It now lives in the file for the block last
read and moves with the reading, with nothing elsewhere counting the
kinds — the rule the four earlier failures should already have taught.


3.2.94–3.2.109: **the last of the कृत् affixes, निष्ठा, and what
replaces लिट्.** 3.2 now runs unbroken 1 to 109.

**The pāda needs FIVE kinds of entry point, not one.** A table row is a
rule with conditions that adds an affix. But 3.2.109 and four others
give whole WORDS; 3.2.84 भूते is a heading that confers a condition and
adds nothing; 3.2.102 निष्ठा NAMES an affix rather than adding one; and
3.2.105–108 REPLACE लिट् rather than add to a root. A test now asserts
every registered sūtra of 3.2 falls in exactly one of the five, the
sets disjoint and covering, so a rule that slipped through a gap would
show rather than sit unread.

**A संज्ञा rule that asks another rule what it means — and whose two
refusals have different shapes.** 3.2.102 says the affix bearing the
name निष्ठा comes in the past. WHICH affixes bear it is 1.1.26
क्तक्तवतू निष्ठा's, and that rule is codified, so it is asked and the
reuse declared. An affix bearing no such name comes back **nameless**:
1.1.26 withheld the name, and a rule must not be reported for a
refusal it did not make. A निष्ठा outside the past is refused **by
3.2.102**, since refusing is then the whole of what it does. One
standing decision cutting both ways inside one function.

And the vṛtti raises a circularity against itself:
निष्ठायाम् इतरेतराश्रयत्वाद् अप्रसिद्धिः — the name is conferred on
affixes that do not yet exist, and the affixes are introduced by the
name. नैष दोषः, भाविनी संज्ञा विज्ञायते: the name is understood as
FORTHCOMING.

**A rule that is the systematic undoing of the four before it.**
3.2.101 अन्येष्वपि दृश्यते, and the commentary takes 3.2.97 to 3.2.100
in turn and shows each condition departed from — असप्तम्यामपि,
जातावपि, असंज्ञायामपि, अकर्मण्यपि — then adds that it works from
another root entirely, परिखा. The third open rule of the pāda, held to
attested forms like 3.2.75 and 3.2.76.

**Two more uses of repetition, and neither is any of the three the
pāda had shown.** 3.2.94 repeats to SHUT OUT the other affixes its own
source rule would give beside — प्रत्ययान्तरनिवृत्त्यर्थम्. 3.2.106
repeats to WIDEN what a substitution reaches — लिण्मात्रस्य यथा
स्यात्, so that it covers every लिट् including one given much later.
**Six distinct jobs for one device in a single pāda**, after defeating
(3.2.44, 3.2.77), ending an अनुवृत्ति (3.2.78) and narrowing (3.2.93).

**A root read as containing an affix that is not written.** 3.2.95
wants कर्मणि of युध्, which takes no object — ननु च युधिरकर्मकः? —
and the answer is अन्तर्भावितण्यर्थः सकर्मको भवति: it absorbs a
causative sense and so becomes transitive. A condition satisfied by
reading the root differently rather than by relaxing the rule.

**And a sandhi trap, met in a test this time.** Two of my assertions
looked for word boundaries the text joins: असंज्ञायाम् + अपि is
written असंज्ञायामपि, and अत्र + उपसर्ग becomes अत्रोपसर्ग, which
swallows the initial उ outright. The attribution guard caught the same
thing once in a quotation; here it was the test doing the assuming. A
substring of Sanskrit must be quoted as the text joins it, not as the
words would stand alone.


3.2.76–3.2.93: **the widest rule of the pāda, and what restricts it.**
3.2 now runs unbroken 1 to 93.

**Four rules in a row that provide nothing.** 3.2.76 क्विप् च gives
क्विप् to every root — सर्वधातुभ्यः, companion or none, Veda or speech
— so 3.2.87, 3.2.89, 3.2.90 and 3.2.91 have nothing left to give and
can only RESTRICT. The vṛtti asks it outright at 3.2.87:
किमर्थमिदमुच्यते, यावता सर्वधातुभ्यः क्विब् विहित एव? — and then
**counts the ways each one restricts**. 3.2.87 is fourfold: only these
companions, only this root, only this affix, only the past. 3.2.89 is
**threefold** — धातुनियमं वर्जयित्वा — the root is left free, so
शास्त्रकृत् and भाष्यकृत् stand too. That difference exists only
because the commentary counts them rule by rule; nothing in the sūtras
distinguishes the two.

And 3.2.87's fourfold reading is itself got by **dragging a word
backward from the next sūtra**: तदेतद् वक्ष्यमाणबहुलग्रहणस्य
पुरस्तादपकर्षणाद् लभ्यते. 3.2.88's बहुल is pulled up over 3.2.87 to
make it readable.

**An अधिकार that adds nothing.** 3.2.84 भूते runs to 3.2.122 and puts
every rule under it in the past — यदित ऊर्ध्वम् अनुक्रमिष्यामो भूत
इत्येवं तद् वेदितव्यम् — while stating no affix at all. Its own entry
point, as 3.1's four headings have, and every row from 3.2.85 carries
the condition, since the codification has no way to represent a
condition that *runs*.

**A condition on the whole and not on a part, twice.** 3.2.80's व्रत
is conveyed by root and companion and affix together —
धातूपपदप्रत्ययसमुदायेन व्रतं गम्यते — and 3.2.92's अग्न्याख्या
likewise. The first समुदायोपाधि this project has met, and then a second
twelve rules later.

**A root pinned by what a LATER rule would do with it.** 3.2.82's मन्
is मन्यते of class four and not मनुते of class eight, and the ground
is उत्तरसूत्रे हि खश्प्रत्यये विकरणकृतो विशेषः स्यात् — with 3.2.83's
खश् the class-marker would betray the difference. Not sense, not
company, but a consequence one sūtra downstream.

**Repetition does three different things in this pāda.** A word said
again though it is already running: at 3.2.77 to DEFEAT another rule
(बाधकबाधनार्थं पुनर्वचनम्), at 3.2.78 to END an अनुवृत्ति (पुनः
सुब्ग्रहणम् उपसर्गनिवृत्त्यर्थम्), at 3.2.93 to NARROW (पुनः
कर्मग्रहणं कर्तुः कुत्सानिमित्ते कर्मणि). Three uses of one device,
and only the commentary tells them apart.

**An eighth field collision — the first to resolve toward reuse.**
`upamana` already existed as a STRING, what role the thing likened to
plays, which 3.1.10 and 3.1.11 divide on. I had added it again as a
bool for 3.2.79 कर्तर्युपमाने. But that rule asks the same question and
wants one answer — the agent — so the fix was the existing field with
the value `kartṛ`, not a new name. **The seven collisions before this
were two questions under one name; this was one question under two
spellings**, and the remedy is the opposite one.

**Naming the affix, where two open rules overlap.** 3.2.75 and 3.2.76
are both open and both reach स्रंस्, one giving four affixes and the
other क्विप्, and neither is wrong. `wants=` lets the caller say which
affix is being asked after, and it reaches an affix a rule carries on
`also` as well — useful for the six rules of this pāda that give two
at once.

**And a weight held to its own case.** 3.2.77's बाधकबाधन is real, but
left general it outranked 3.2.4 and took समस्थः from it — the same
affix, the wrong rule named. The row is now held to शम्, which is
where the repetition actually does work; everywhere else 3.2.4 already
answers. A weight is a claim about one contest, not a licence to win
every one.


3.2.48–3.2.75: **the small affixes, the क्विप् run, and the close of
the pāda.** ड, णिनि, टक्, ख्युन्, खिष्णुच्, क्विन्, क्विप्, ण्वि,
ञ्युट्, विट्, कप्, ण्विन्, विच्, and the four that 3.2.74–75 give
together. **3.2 now runs unbroken 1 to 75.**

**A sūtra of two kinds at once, and the first the project has met.**
3.2.59 fixes five WORDS outright — ऋत्विगादयः पञ्चशब्दाः
क्विन्प्रत्ययान्ता निपात्यन्ते — and names three ROOTS that take the
affix by rule, अपरे त्रयो धातवो निर्दिश्यन्ते. So it is registered
against the table AND feeds the fixed-word lookup, and a `_FIXED_ONLY`
list now separates the sūtras answered only from the lookup from those
that are both. 3.2.5 turned out to be the same shape once its lost
vārttika was recovered.

**Three conditions no earlier rule had needed.** 3.2.58 names a
companion in order to REFUSE it — स्पृशोऽनुदके — where every rule
before it named companions to require them. 3.2.59's युज् and क्रुञ्च्
want NO companion at all, केवलादेव. And 3.2.66's अनन्तः पादम् is
**prosodic and not grammatical**: the root must not stand at the end of
a metrical quarter. That last is the first condition anywhere in this
project that turns on where a word sits in a VERSE, and nothing the
codification had could express it.

**One condition asked as two questions.** 3.2.56 and 3.2.57 want the
companion to carry the च्वि MEANING without the च्वि AFFIX, and the
vṛtti asks after each separately — च्व्यर्थेष्विति किम्? and
अच्वाविति किम्? — so the code holds them as two fields rather than
one. The pair also differ in nothing but the kāraka: the instrument
gets ख्युन्, the agent gets खिष्णुच् and खुकञ् both.

**A rule whose whole work is to restrict another.** 3.2.73 is a
नियम, and the vṛtti argues it out against itself: किमर्थमिदमुच्यते,
यावता अन्येभ्योऽपि दृश्यन्ते इति यजेरपि विच् सिद्ध एव? — why state
this, when 3.2.75 gives यज् its विच् already? यजेर्नियमार्थमेतत् —
उपयजेश्छन्दस्येव, न भाषायाम्. Its condition is not a qualification on
a provision; the condition IS the rule.

**A rule open at every joint, held back by usage and not by scope.**
3.2.75 अन्येभ्योऽपि दृश्यन्ते. अपिशब्दः सर्वोपाधिव्यभिचारार्थः — the
अपि is written so that EVERY condition may be departed from — and
निरुपपदादपि भवति, it works with no companion at all. Read as an
ordinary provision it would hand four affixes to every root in the
language. What stops it is its verb: दृशिग्रहणं प्रयोगानुसरणार्थम्,
'are SEEN' is chosen so that one FOLLOWS USAGE. So it is codified with
a condition the caller asserts, and that condition is the codification
of दृश्यन्ते itself. **The same ground as 3.2.1's अनभिधानात्, taken
from the other side**: there usage withholds what a rule would give,
here a rule defers to what usage shows.

**A tie broken by narrowness.** 3.2.70 दुहः कब् names one root; 3.2.61
names twelve with दुह् among them. Both reach कामदुघा and by stated
conditions they tie exactly, so the twelve won on table order and the
cow got गोधुक्'s affix. Narrowness went into the RANKING and not into
`_how_specific` — that answers how much a rule says, which is a fact
about one rule, where the ranking is a fact about a pair.

**A debt asserted, and paid inside the same session.** 3.2.59's
सोपपदात् तु … क्विब् भवति, अश्वयुक् could not be shown while 3.2.61
was uncodified; the test asserting the debt went red the moment 3.2.61
was registered, which is exactly what a debt written as a test is for.
Both halves now run: युङ् bare by 3.2.59, अश्वयुक् by 3.2.61. One debt
remains open — 3.2.53's चौरघातो हस्ती, which the vṛtti answers from
3.3.113, not yet codified.

**Three अनुवृत्ति ended by the commentary and not by the text** —
3.2.48's संज्ञायामिति नानुवर्तते, 3.2.61's कर्मग्रहणं न व्याप्रियते,
3.2.68's छन्दसीति निवृत्तम्. The codification cannot represent
anuvṛtti at all, since every row states its own conditions, so a
condition that ends is simply one not written. The notes are the only
record that a choice was made rather than a line missed, and a test
holds all three.

**And a ज्ञापक.** 3.2.61's उपसर्गग्रहणं ज्ञापनार्थम् — mentioning the
preverb here tells us that ELSEWHERE, where सुप् is mentioned and the
preverb is not, no preverb is meant. A rule saying something by the
fact of its own wording, which is a kind of evidence distinct from
what it states. Recorded, not run.

**Two process failures worth keeping.** A patch script found the end
of a table with `rindex("\n)")` — a sequence that also closes several
function signatures — and **wrote before it validated**, so a syntax
error reached disk. Repaired by walking the module tree for the
assignment instead of guessing at text, and validating first. And the
pāda-coverage test went stale a **fourth** time; it now asserts
contiguity from the first sūtra and names no endpoint, which is what
*assert the property, not the census* should have meant all along.


**Two gaṇas the corpus already held, and the codification did not.** Asking `load_ganapatha()` which gaṇas it keys to this pāda
named मूलविभुजादि at 3.2.5 and पार्श्वादि at 3.2.15. Neither was
in the code. Both sit in vārttikas at the END of their Kāśikā
entries, and both entries had been read through a pipe that cut
them short.

  3.2.5   lost a whole vārttika — कप्रकरणे मूलविभुजादिभ्य
          उपसंख्यानम्, मूलविभुजो रथः, नखमुचानि धनूंषि. Its
          members are FINISHED words, so they are looked up
          whole as निपातन are.
  3.2.15  had its four vārttikas MIS-RECORDED. पार्श्वादिषु is a
          gaṇa, not पार्श्वात् संज्ञायाम्; and उत्तानादिषु
          कर्तृषु is a second vārttika over that same gaṇa,
          taking the companion as AGENT where the first takes it
          as instrument. One row became five.

Membership is now read from the corpus at import, so it cannot
drift from it. **A third bug fell out of the second.** The निपातन
entry point had hardcoded इन् as the affix for every fixed word —
true of 3.2.26, false of 3.2.37, whose उग्रम्पश्यः is a खश् form.
It had been answering wrongly for three words, and only a third
affix arriving made it visible.

**The scar is about method, not about these two rules.** A
commentary entry must be read WHOLE: its length is not knowable
in advance, and the part a pipe loses is the end — which is
exactly where vārttikas sit. Recorded at 3.2.5 as a SCAR. What
found it was not re-reading but asking a *different* local source
the same question, which is the general form of the lesson: the
corpus can be interrogated for what the codification is missing,
and had not been.

3.2.29–3.2.47: **the rest of खश्, and the खच् run.** 3.2 now runs
unbroken 1 to 47.

**यथासंख्यम् cuts both ways inside one run, so no default is right.**
3.2.5 and 3.2.13 required the one-to-one pairing; 3.2.29 refuses it —
यथासंख्यमत्र नेष्यते — and 3.2.36, seven rules later, requires it
again. And 3.2.29 licenses a set that is neither: नासिका with both
roots, स्तन with only धेट्, three combinations of the four. That is
what forced the pairing out of two branches keyed on sūtra id and into
a field on the row; a test now reads the matcher's own source and
asserts no sūtra number appears in it.

**The vṛtti reads the refusal off the ORDER OF THE WORDS.**
लक्षणव्यभिचारचिह्नाद् अल्पाच्तरस्यापूर्वनिपातनाल्लभ्यते — the shorter
word would have been placed first by 2.2.34 अल्पाच्तरम्, and its not
being placed first is the sign that the ordinary reading is departed
from. 3.2.30 gives the same argument through a different rule, the
घि-final word not standing first. A commentary recovering intent from
the sūtra's own word order, which is a kind of evidence this project
had not met before.

**A condition I invented rather than read, and the rule that caught
it.** `causative` had been made to exclude in BOTH directions: 3.2.28
requires ण्यन्त, so I had every rule silent about it refuse a
causative stem. Nothing in the text says that. 3.2.39 says the
opposite outright — तप दाहे चुरादिः, तप संतापे भ्वादिः, द्वयोरपि
ग्रहणम् — both roots spelt alike are meant, so silence admits the
causative. Now one-way, like छन्दसि: requiring a condition excludes
what lacks it, saying nothing excludes nothing. The rule that caught
it sits eleven sūtras after the one the condition was abstracted from,
which is the argument for reading a whole run before trusting a
generalisation drawn from one rule of it. **The test asserting the
wrong behaviour was mine too** — it is now rewritten to say plainly
that the claim was mine and not Pāṇini's.

**A third बाधकबाधन weight.** 3.2.44's अण् is named where वा would have
been shorter, and the vṛtti says why: वेति वक्तव्ये पुनरण्ग्रहणं
हेत्वादिषु टप्रतिषेधार्थम्, to keep 3.2.20's ट out. By stated
conditions the two rules tie exactly, and a tie loses क्षेमकारः — so
the row carries weight its conditions do not warrant, as 3.1.109's
क्यप् and 3.1.141's श्यै do. Three instances now, in two pādas: the
device is a habit of the text.

**A new reuse edge, and the first in this pāda that is a real call.**
3.2.43's उपपदविधौ भयादिग्रहणं तदन्तविधिं प्रयोजयति — naming भय reaches
what ENDS in भय, अभयंकरः. That is 1.1.72 येन विधिस्तदन्तस्य, codified,
so it is asked rather than approximated with a suffix test. Held to
this rule alone, since the vṛtti attaches it here and 3.2.42's सर्व
and कूल carry no such note; a test asserts the neighbouring rules do
NOT have it.

**Census tests go stale every chunk.** Two assertions that 3.2 runs 1
to 28 went red the moment it ran to 47, and an equivalent pair had
already been deleted at the block before. The property is now asserted
in exactly one place — the file for the newest block — with a note
saying why a third copy should not be added. *Assert the property, not
the census* was already a standing rule; what this adds is that a
range is a census even when it looks like a property.


3.2.21–3.2.28: **the rest of the उपपद affixes** — the long list for
कृ, the only प्रतिषेध of the pāda, इन्, a निपातन, a Vedic rule, and
खश्. **3.2 now runs unbroken 1 to 28.**

**A प्रतिषेध does not govern what it excepts, and this is the first
place the code had to prove it.** 3.2.23 refuses 3.2.20's ट for nine
words. What those words then take is 3.2.1's अण् — which is why every
form the vṛtti gives here is -कारः and not -करः — so the answer names
3.2.1 and carries 3.2.23 in a separate `blocked_by`. The decision was
already standing from 2.3.72 and 2.3.50; what is new is a run where a
refusal and a supplier had to be reported at once. The rule still names
itself where refusing leaves nothing at all, and a test holds both
halves.

**A seventh field-name collision, and the first found by a wrong
answer rather than by a rename.** `sense` had been carrying two
different questions — the sense of the ACT (उद्यमन, वयस्, भृति) and
what the finished WORD names (a पशु, a व्रीहि). 3.2.25
हरतेर्दृतिनाथयोः पशौ needs both at once: पशौ is its own condition, and
उद्यमन is what keeps 3.2.9's अच् off दृतिहारः, since carrying a
waterskin IS lifting. With one field the two masked each other and the
vṛtti's own counter-example came out as *दृतिहरः. Split into
`names_a`. The six before this were caught by reading; this one was
caught by the form being wrong.

**One term read two ways inside one pāda.** 3.2.1's कर्मणि is the
kāraka. 3.2.22's is स्वरूपग्रहण — the word कर्मन् itself standing
beside, कर्मशब्द उपपदे. Twenty-one rules apart, nothing in the text
marking the difference, and it is read off what each rule could
sensibly mean. Codified by putting कर्मन् in the companion list and
never in the role, so the two cannot be confused by the code either.

**A vārttika codified as a condition, and another deliberately not.**
3.2.24's व्रीहिवत्सयोरिति वक्तव्यम् goes into the table, because the
vṛtti's own counter turns on it — व्रीहिवत्सयोरिति किम्? स्तम्बकारः —
and a vārttika that changes the output has to be in the table or the
counter cannot be tested. 3.2.21's किंयत्तद्बहुषु कृञोऽज्विधानम् stays
out, because the vṛtti offers a second route in the same breath —
अथवाजादिषु पाठः करिष्यते — and picks neither. Codifying one would be
settling what the commentary left open.

**छन्दसि is one-way; ण्यन्त is two-way.** 3.2.27 holds in the Veda and
not outside it — but the rules that say nothing about the Veda still
answer inside it, since the Veda has the ordinary grammar and only
adds to it. 3.2.28's causative excludes in both directions: the bare
root gets no खश्, and a rule written for bare roots does not answer
for the causative stem. Two conditions that look alike and are not.

**This block declares no reuse at all, and that is the reading rather
than an oversight.** 3.2.28 cites 3.4.113 for what its श buys and
3.2.21 cites the adhyāya-8 rules भास्करः escapes; both consequences
happen downstream of choosing the affix, which is all this module
does. After 3.2.3's false 1.1.71, the test now asserts the *absence*
of declarations here — the guard can catch a declaration without a
call, and only a test can catch the reverse habit of declaring
whatever the prose mentions.


3.2.1–3.2.20: **कर्मण्यण् and the four affixes that cut into it** — the
first run where 3.1.92's उपपद does real work. From here the affix does
not depend on the root alone but on the word standing beside it, and
3.2.1 gives अण् to any root whose companion is the object — कुम्भकारः.
The nineteen after it are all अपवाद to that one rule: क, टक्, अच्, ट.

**यथासंख्यम् has to be held as pairs, not as two lists.** 3.2.5 names
two roots and two words, 3.2.13 two more of each, and in both the
binding is crosswise. Stored flat, the tables would form स्तम्बेजपः —
a word neither rule licenses. Found by writing the rows without their
roots at all and watching 3.2.5 lose to the general rule, which is
also how the ranking bug surfaced: a row that names nothing cannot
outrank one that names something.

**A debt discovered by a test that assumed too much.** The test for
3.2.2 asserted that all three of its roots are आ-final — since the
vṛtti calls the rule कप्रत्ययस्यापवादः, and 3.2.3 gives क to आ-final
roots. Only माङ् is. ह्वेञ् and वेञ् are ए-final in उपदेश and reach
that shape by **6.1.45 आदेच उपदेशेऽशिति, which is not codified**. So
the conflict 3.2.2 exists to settle can be staged here for one of its
three roots and not the other two — and 3.2.2 answers for them by
naming them, which is the right answer arrived at without the contest.
The test now asserts the debt and fails again when 6.1.45 lands. The
same debt sits under 3.2.8's गै. Worth saying plainly: the rule was
never wrong, and only the reason given for it was incomplete.

**A false reuse declaration, refused again — and this one was
reflex.** 3.2.3 was registered as reusing 1.1.71, because the three
runs before it all do. But 1.1.71 is what makes a *pratyāhāra* denote
a span, and 3.2.3's आत् is a plain sound: `ends_in_a` compares one
character and reaches no rule at all. The guard walked two calls deep,
found nothing, and declined. The shared-conditions module had invited
the mistake — its header listed आ-final under "the śivasūtras, through
1.1.71", which is true of हल् and इक् on the lines below it and not of
this one. Header corrected at the source rather than the declaration
re-argued. **Two false declarations in three chunks, both mine, both
caught by the guard rather than by review.**

**A limit no condition can carry.** 3.2.1 as written reaches ग्रामं
गच्छति and आदित्यं पश्यति, and the vṛtti stops it by hand — न भवति,
अनभिधानात् — because usage has no such word. This is the second time
the run has met that ground, after 3.1.108, and it is checked against
usage rather than against the root or the companion, so there is
nothing to turn into a condition. Recorded as a SCAR, and the worked
input for it says in as many words that the code forms what the
grammar does not. Labelling it a counter-example was wrong twice over
— the rule does fire — and the case guard caught that too.

**What the pāda argues, and the code cannot yet do.** 3.2.19 पूर्वे
कर्तरि is the sharpest statement anywhere so far of the debt 2.3.1
first recorded: पूर्वसरः if पूर्व is the doer, पूर्वसारः if it is the
thing gone to. One word, one root, two forms, and the *kāraka* is the
whole of the difference. 1.4.49 is codified, but it takes the semantic
facts asserted of a participant rather than a word — deciding a kāraka
needs the whole clause — so the role is passed in here as it is there.
A helper that pretended to work it out was written during this chunk
and deleted: the worst kind of restatement is one that looks like a
call.

**Two affixes chosen for what a rule three adhyāyas away will do with
them.** 3.2.12 prefers अच् over अण् because the two are told apart in
the feminine, and 3.2.16 gives ट rather than 3.2.15's अच् —
प्रत्ययान्तरकरणं ङीबर्थम् — so the feminine takes ङीप्, कुरुचरी. The
form made here is identical either way. Both are recorded as SETTLED
with the reason, since neither is visible in this pāda's own output
and a reader would otherwise take them for arbitrary.


**अध्याय ३ पाद १ is complete** — all 150, contiguous. And every rule
that had been reached ahead in this pāda for some earlier derivation —
3.1.22, 3.1.32, 3.1.68, 3.1.94, 3.1.134 — has now been overtaken by
the reading and retired from that list. A test asserts none is left.

**Reuse edges went 75 → 90, and that is the real work of this
chunk.** The count had sat at 75 for four chunks while the notes went
on citing earlier sūtras in prose that the code was not calling. An
audit found four places where a codified rule had been RESTATED:

  3.1.83's हलः      a hand-typed vowel list, where हल् is a
                    pratyāhāra 1.1.71 resolves
  3.1.97 and after  "ac", "hal" as bare tokens, when a root's final
                    can be read off the root
  3.1.98, 3.1.110   उपधा passed in, when 1.1.65 अलोऽन्त्यात्पूर्व
                    उपधा is codified
  2.4.77's घु       दा and धा inlined, when 1.1.20 दाधा ध्वदाप् names
                    the class

**Restating a rule hides the reason it exists.** The clearest case is
3.1.135: it names ज्ञा, प्री and कॄ beside the इगुपध roots, and WHY
only becomes visible once इगुपध is asked — ज्ञा's penult is ञ्, no इक्
at all, so the rule could not have reached it. With the condition
passed in as a flag, the naming looked arbitrary.

**पु is not a pratyāhāra, and assuming it was is what caught it.**
3.1.98 पोरदुपधात् — पु is प् marked with उ, standing for its whole
वर्ग by 1.1.69 through savarṇatva. Reading it as a pratyāhāra raised
an error rather than a wrong answer, which is the good kind of
failure.

**Deriving the shapes changed three answers, and the vṛtti had already
settled each.** Once roots carry their own shape, यम् matches 3.1.98
as well as 3.1.100, मृज् 3.1.110 as well as 3.1.113, and वप्/रप्/लप्
3.1.98 as well as 3.1.126. In every case the commentary says the
naming rule exists BECAUSE a shape rule already reached it —
अनुपसर्गनियमार्थम्, प्राप्तविभाषेयम्, यतोऽपवादः. So **naming a root
outweighs naming a shape**, and the tables now say so.

**One of my own new declarations was false, and the reuse guard
refused it.** 3.1.83 went through a convenience wrapper one level below
what 1.1.71 registers: the call was real but invisible to the guard,
which declined to let the claim stand rather than taking my word.
Calling the registered entry point fixed both.

Two findings from 3.1.133–150 itself. **3.1.140's गण is a stretch of
the dhātupāṭha, not a list** — ज्वल इत्येवमादिभ्यः कस इत्येवमन्तेभ्यः,
and the corpus reads ज्वल at 01.0916 and कस् at 01.0996 with the
vṛtti's own चल between them, so the bound is read rather than copied.
And **समभिहार means something different here than at 3.1.22** — there
पौनःपुन्यम्, again and again; here साधुकारित्वम्, doing a thing well,
with the consequence spelled out: once done well is enough, often done
badly is not. A test asserts the two rules do not share a field.

3.1.96–3.1.132, the कृत्य affixes — and with them **3.1 runs unbroken
1 to 132**, closing the section 3.1.95's heading had opened. Four
affixes do the work; seventeen of the run's thirty-seven rules add no
affix at all but fix forms whole.

**The अपवाद chain cuts BOTH ways, so neither walk order works.** 3.1.98
is ण्यतोऽपवादः — यत् taking ground from ण्यत् — and 3.1.125 is
यतोऽपवादः, taking it straight back. A first-match walk loses the
second, a last-match walk loses the first, and the vṛtti names the
relation each time rather than leaving it to a general ordering. So
the table ranks by what each rule states and follows the text, which
is the same resolution the सनादि and aorist tables needed.

**A rule repeated so that a LATER rule cannot displace it.** 3.1.109
says क्यप् again though the word was already running, and the vṛtti
gives the reason: क्यबिति वर्तमाने पुनः क्यब्ग्रहणं बाधकबाधनार्थम् —
to defeat 3.1.125's ण्यत् where the two meet, अवश्यस्तुत्यः. Every
other repetition this project has met was to NARROW a rule (3.1.79's
कृ, 3.1.100's यम्, 3.1.52's अस्); this one is to survive one. The row
carries a weight its conditions alone would not give it, and a test
holds that without the weight अवश्यस्तुत्यः would be lost.

**Seventeen निपातन rules, kept out of the table on purpose.** यदिह
लक्षणेनानुपपन्नं तत् सर्वं निपातनात् सिद्धम् — whatever the rules do
not reach, the fixing supplies. They are recorded as the sūtras give
them, with the sense each holds in and the counter-form the vṛtti
supplies alongside, and a table that tried to derive them would be
pretending. A test asserts that **every rule of the run belongs to
exactly one of the two** — affix-table or निपातन — so a gap would be a
rule nobody had read.

**Two arguments from the commentary worth keeping as they stand.** At
3.1.108 the rival affix is kept out not by a rule but by usage — ण्यत्
तु भावे न भवति अनभिधानात् — a ground of a different kind from
everything else in the run, and reworded into a condition it would
stop being that. And at 3.1.128 the vṛtti meets a scriptural passage
that seems to use the word in the opposite sense, and answers by
reading संमति as *desire* rather than *regard*: a commentary defending
a rule against a text, which is the reverse of the usual direction.

Also a sixth field-name collision — `ends_in` means a compound's last
member at 2.4.20–29 and a root's final sound here. Renamed
`root_ends_in`.

3.1.69–3.1.95: the class-marker, कर्मवद्भाव, and the four headings that
open the कृत् section. **3.1 now runs unbroken 1 to 95**, and with it
every rule that had been reached ahead in this pāda — 3.1.22, 3.1.32,
3.1.68, 3.1.94 — has been overtaken by the reading and retired from
that list.

**Nine of the ten verbal classes now decide their marker from the
corpus.** दिवादि is class 04, स्वादि 05, तुदादि 06, रुधादि 07, तनादि
08, क्र्यादि 09 — the codes the dhātupāṭha already carries, asked
through `verbal_gana`. That helper was extracted for 2.4.72's अदादि,
reused for 3.1.25's चुरादि, and now serves six more. No class list is
written anywhere in this codebase.

**A root name does not pick out a class, and the table says so.** रुध्
is read in the fourth AND the seventh and takes a different marker in
each; दिव् is read in three, तन् in two. Asked without a class the
answer REPORTS the ambiguity instead of resolving it — picking the
first would have been the table choosing on Pāṇini's behalf, and would
have given रुध् श्यन् because 04 sorts before 07. The same shape as
शक् being both इदित् and ऌदित्, and as 2.4.58's कौरव्य: **one spelling,
several readings, and the rule follows the reading.**

**A test caught a refusal saying something false.** Asked for भू in
class 01, the table answered "not read in class 01" — but भू *is*
read there; the class simply takes no marker from this run, going to
3.1.68 शप् instead. Two quite different refusals had one message.
Separated, and the second now names where each of the three remaining
classes is handled. **A refusal has to be as accurate as an answer**,
and this one was accurate about the outcome and wrong about the
reason.

**3.1.79 names कृ in order to restrict a rule two pādas back.** कृ is
already in तनादि, so the naming adds no marker — तनादिपाठादेव
उप्रत्यये सिद्धे करोतेरुपादानं नियमार्थम्, अन्यत् तनादिकार्यं मा भूत्.
What it holds off is 2.4.79, and the test checks that rule really does
fire for तन् before asserting it must not for कृ: a restriction means
nothing unless what it restricts is reachable. The second claim of
this shape after 3.1.40's displacement of 2.4.52.

**कर्मवद्भाव is where 3.1.62–67 gets used.** 3.1.87 says an agent
whose action is like the object's is treated as an object, and the
vṛtti names the four things that follow rather than leaving "treated
as" to be worked out — यक्, the middle endings, चिण्, चिण्वद्भाव.
3.1.89 refuses two of the four for three roots and 3.1.90 displaces
two others; the test asserts that refused and kept together make the
four, so a fifth effect appearing anywhere would fail it.

And 3.1.95's कृत्य is the name **2.1.33 and 2.3.71 were waiting on** —
both codified long before the heading that confers it. A range given,
as headings here usually are, by naming the rule it stops before.

3.1.33–3.1.67: the affix a lakāra brings with it — स्य, तासि, सिप्,
आम् for the perfect, and then च्लि, which exists only to be replaced.
The run ends where the विकरण section begins, so 3.1 is now unbroken
1..68 and has caught up with 3.1.68 कर्तरि शप्, reached ahead long ago
for the present of पच्.

**A scoring function that returned False for every row.** The aorist
table ranks rows by how much each says, and the sum was written
`len(row.of) > 0 + 3 * row.shal_igupadha_anit + …` — `>` binds looser
than `+`, so the whole sum became the right-hand side of one
comparison and every row scored `False`. The ranking did nothing,
last-match-wins quietly stayed in force, and **every answer still
looked plausible**. Caught by the case guard on one input, दुह्. The
test now asserts the SCORES and not only their effect, because a
ranking that has silently stopped ranking is invisible from its
outputs.

**A sūtra naming two ways in needs two rows — the third time.** 3.1.48
takes any ण्यन्त stem OR three named roots; written as one row the
named list shut the causatives out and अचीकरत् reached nothing. After
3.1.25 (thirteen stems or a class of roots) and 3.1.55 (two sub-gaṇas
or a mark), this is a pattern worth stating: **where a sūtra offers
alternative bases, one row per base.** All three failed the same way —
the table still answered, and the rule that had gone missing was the
one nobody asked for.

**Two conditions read from the corpus instead of asserted.** 3.1.55
turns on ऌदित् and 3.1.57 on इरित्, and both marks are written on the
root in the dhātupāṭha. 1.3.2 उपदेशेऽजनुनासिक इत् is what makes them
its, and it is codified — so `root_its` asks that rule rather than
parsing the upadeśas again. गम्ऌ, शक्ऌ, भिदिर्, छिदिर् are found, not
declared. Declared as reuse, and the first reuse edges this project
has added since 2.3.

**3.1.40 keeps 2.4.52 off, and not by prohibiting it.** कृञ् is a
प्रत्याहार taking कृ, भू and अस् together, and तत्सामर्थ्याद्
अस्तेर्भूभावो न भवति: अस्तेर्भूः would have turned अस् into भू and
पाचयामास could never be formed, so that rule is displaced by the fact
that this one would be pointless if it applied. Held by a test that
first checks 2.4.52 really does fire elsewhere — a claim about a
displaced rule means nothing unless the rule is reachable.

**A quotation was caught with its sandhi re-split.** The attribution
guard rejected तत्सामर्थ्यात् अस्तेर्भूभावो, because the vṛtti has it
joined — तत्सामर्थ्यादस्तेर्भूभावो. The same check found a verse
attributed here that the vṛtti actually quotes at 2.4.52. Both
corrected. **Quote the corpus's own wording, not a tidied version of
it**: re-splitting a sandhi makes a citation unfindable, which is
exactly what that guard exists to notice.

Two more of the run's own findings are worth keeping. 3.1.46 is a
नियम and not a विधि — श्लिष् already met 3.1.45's conditions, so the
rule RESTRICTS क्स to the sense of embracing rather than granting it.
And 3.1.65 names a sense in order to WIDEN a prohibition: तस्य ग्रहणम्
अकर्मकर्त्रर्थम्, so the refusal reaches भाव and कर्मन् too, where
3.1.64 beside it stops at कर्मकर्तृ.

**Adhyāya 3 is open.** 3.1.1–3.1.31: four rules saying what an affix
is, then the सनादि affixes that make a NEW root out of a root or a
finished word. The run ends exactly where 3.1.32 सनाद्यन्ता धातवः —
codified long ago for लोलुवः — picks up what it made. 3.1 now runs 1..32
unbroken.

**Three pairs of rules reached the same input, and each collapse hid a
rule rather than producing a wrong form.** 3.1.8 and 3.1.9 both make a
word wish for something — पुत्रीयति and पुत्रकाम्यति both stand, so
naming the affix says which is asked about. 3.1.10 and 3.1.11 both mean
behaving LIKE something and divide by which role the thing compared
plays; a yes-or-no flag lost that and 3.1.11 became unreachable. And
पच् is read in the TENTH class as well as the first, so 3.1.25's
class-row answered before 3.1.26 हेतुमति च — the rule that actually
speaks about causing. The last was fixed by ranking rows: **a rule that
names the sense, or names the base, beats one that names a class** —
विशेष over सामान्य — and that at once fixed a second case not yet
found, धूप, which 3.1.28 names outright and which 3.1.25 had been
taking.

**This is a failure mode worth naming: the table still answered, and
every form it produced was right.** Nothing looked wrong. What was
wrong was that a rule had stopped being reachable, and only a test
asking for THAT rule by name could see it. The case guard caught two of
the three; the third was caught by a test written for the guard's own
sake. **Where two rules can reach one input, test that each is
reachable, not that the input gets an answer.**

**One function answered four rules and named only the first.** 3.1.1 to
3.1.4 say four different things — what an affix is, where it stands,
how it is accented, and the exception to that — and a single resolver
reported 3.1.1 for all of them, so asking 3.1.2 came back citing a rule
that had not acted. The same fault as a refusal reporting the wrong
rule, and caught by the same guard. Each now has its own entry point.

**A fifth field-name collision, and the count is the point.** `kind`
carries 2.4.26's vārttika list; at 3.1.1 it means which of six things a
rule is prescribing, so a beginner asking what an affix is would have
been told about a compound's gender. Renamed `prescribes`. Five now —
`anga`, `pada`, `vibhakti`, `sense`, `kind` — and every one was caught
by reading the inherited hint rather than by a test.

Two small DRY repairs came out of the reading. The dhātupāṭha
class-lookup 2.4.72 did inline is now `verbal_gana` in `pada.py`, asked
by both that rule and 3.1.25. And 3.1.25 itself is **two rows, not
one**: it names thirteen STEMS and then a class of ROOTS, and written
as a single row the named list shut the class out so चुर् reached
nothing.

**अध्याय २ is complete.** 2.1 (72), 2.2 (38), 2.3 (73), 2.4 (85) —
268 sūtras, every pāda contiguous from its first. With adhyāya 1's 351
that is two whole adhyāyas read in order. A test now asserts the
property rather than the number: every sūtra of adhyāya 2 in the corpus
is registered, and each pāda runs 1..N with no gap.

The last two chunks were 2.4.58–71, the descendant-affixes that adhyāya
4 adds and this pāda takes away again, and 2.4.73 with 2.4.75–85, which
close the pāda.

**A second defective gaṇa, and this one would have changed an answer.**
The गोपवनादि on disk for 2.4.67 holds eleven entries, one of them the
bare string `"1"` — a parse artifact, not a word. The vṛtti fixes the
extent outright, एतावन्त एवाष्टौ गोपवनादयः, names the eight, and then
says what the surplus is and why it matters: परिशिष्टानां हरितादीनां
प्रमादपाठः, ते हि चतुर्थे बिदादिषु पठ्यन्ते, तेभ्यश्च बहुषु लुग्
भवत्येव. The extra words belong to बिदादि and the elision DOES happen
for them. **Reading the file straight would have made this prohibition
block exactly the forms the commentary says it must allow** — हरिताः,
किंदासाः. Codified from the vṛtti, with a test that checks the disk
list still disagrees, so a corrected corpus goes red instead of
silently agreeing. After the Kāśikā stored against 2.4.28, that is two
corpus defects in one pāda: **the reference data is evidence, not
authority, and where a commentary states a bound explicitly the bound
is what to codify.**

**A ज्ञापन is a claim about a rule OTHER than the one that states it.**
2.4.66 names भरत where it did not have to — the Bharatas are already
among the प्राच् — and the vṛtti reads the redundancy as deliberate:
भरताः प्राच्या एव, तेषां पुनर्ग्रहणं ज्ञापनार्थम् — अन्यत्र
प्राग्ग्रहणे भरतग्रहणं न भवति. What it teaches lands on 2.4.60, which
therefore does not reach them, and आर्जुनिः पिता, आर्जुनायनः पुत्रः stay
different. Running 2.4.66 cannot check that, so the test asserts the
answer at 2.4.60 — the same shape as the three योगविभाग tests one chunk
earlier. **Where the commentary argues from a rule's redundancy, the
test belongs on the rule the argument is about.**

**Which elision it is can be the whole content of a rule.** 2.4.75
could have said लुक्, already running from 2.4.72; it names श्लु
instead, and the vṛtti gives the reason — लुकि प्रकृते श्लुविधानं
द्विर्वचनार्थम्. Only a श्लु triggers the reduplication, so जुहोति and
बिभर्ति exist because of which word was chosen. A test asserting merely
that something was elided would pass on the reading that loses them.

**Three conditions carried across nine rules, each refused separately.**
बहुषु, अस्त्रियाम् and तेनैव run from 2.4.62 to 2.4.70, and the Kāśikā
gives a counter for each in turn. A form can fail any one alone, so
each is a separate check and each refusal names which condition failed
rather than reporting a bare no.

And a fourth field-name collision — `sense`, which carries अर्थ
everywhere else and गोत्र/युवन् here — renamed `descendant`. Four in
one pāda, after `anga`, `pada` and `vibhakti`. That is now a rule and
not an observation: **a run reaching into a new part of the grammar
reuses ordinary words for new things, so every inherited field name is
read against its help before it is adopted.**

2.4.32–2.4.57 are one thing standing in for another: three rules that
shrink a pronoun on its SECOND mention, then a heading, then
twenty-two that swap a root for a substitute before an आर्धधातुक
affix. 2.4 now runs unbroken from 1 to 57.

**A योगविभाग is a claim about what a rule PREVENTS, and running the
rule cannot test it.** Three of these sūtras exist only to make a
split, and each time the vṛtti says what the split buys: 2.4.43 is
separated from 2.4.42 so that 2.4.44's option reaches the aorist and
not the benedictive — आत्मनेपदेषु लुङि विकल्पो यथा स्याल्लिङि मा भूत्;
2.4.47 is separated from 2.4.46 so that 2.4.48 takes सन् alone —
इङश्चेति सन्येव यथा स्यात्; and 2.4.45 repeats लुङ् though it was
already running, so that 2.4.44's option does not carry down. Each is
held by a test that performs the merge the commentary argues against
and checks the answer changes. **A test that only runs the rule as
written would pass on a table with the split undone**, which is the
same trap as the tests that could not fail.

**The last matching row wins, and three rules depend on it.** पूर्वेण
नित्ये प्राप्ते विकल्प उच्यते appears three times — 2.4.44 over 2.4.43,
2.4.55 over 2.4.54, 2.4.57 over 2.4.56 — each making optional what the
rule immediately before made obligatory. That is 1.4.2 विप्रतिषेधे परं
कार्यम्, and taking the first match instead would leave all three
options unreachable while every worked example still looked right.

**आर्धधातुक is taken as given, and the note says why.** 2.4.35 is a
विषयसप्तमी, not a परसप्तमी — तेनार्धधातुकविवक्षायाम् आदेशेषु कृतेषु
पश्चाद् यथाप्राप्तं प्रत्यया भवन्ति: the substitution happens where the
affix is INTENDED and the affix arrives after. What makes an affix
आर्धधातुक is 3.4.114, which is not codified. 3.4.113's सार्वधातुक is,
and the complement was available — but taking it would have been
codifying 3.4.114 without registering it. Passed in instead, as the
kāraka is at 2.3.1.

**Two more field names that meant something else.** After `anga` at
2.4.2 came `pada` — the पद of 1.4.14 everywhere in this codebase, and
the VOICE at 2.4.44 — and `vibhakti`, whose shared hint asks a
yes-or-no while 2.4.32 needs WHICH case follows. Renamed `atmanepada`
and `before_vibhakti`. Three collisions in one pāda is a pattern, not
an accident: **a run that reaches into a new part of the grammar will
reuse ordinary words for new things, and the field names have to be
checked against their inherited help every time.**

Two UI guards earned their keep on this chunk, both catching things a
reader would have hit and a test-for-coverage would not: a gloss short
enough to be a placeholder, and a chip labelled *"and etad the same
way"* — which only means anything to someone who has already read the
chip beside it.

2.4.1–2.4.31 say what a compound IS once 2.1 and 2.2 have made it.
Those pādas settled which words may join and which is spoken first;
this run settles whether the result counts as ONE — एकवद्भाव, sixteen
rules — and what gender it then carries, fifteen more. With it the
compound section is closed at both ends.

**2.4.17 asks; it does not restate.** स नपुंसकम् — "THAT is neuter" —
has no content of its own. स points back at the sixteen rules before
it, so `gender` runs `ekavat` and reads the answer rather than keeping
its own copy of which compounds count as one. Held by a test that
removes the qualifying fact and checks the neuter goes away with it.
The third rule of this shape, after 2.3.50 शेषे and 1.4.7 घि.

**A source on disk can simply be wrong.** The Kāśikā stored against
2.4.28 in `reference/` is not the Kāśikā on 2.4.28: it is a vṛtti on a
छ-affix rule, about अपोनप्तृ and अपोनप्त्रीयम्, with nothing to do with
हेमन्तशिशिरौ. Codifying from the first commentary that answered would
have put a taddhita rule in the middle of the gender section. Four
other witnesses on disk — Nyāsa, Padamañjarī, Siddhāntakaumudī, Vasu —
agree on the real content, and the rule is codified from them. A test
now asserts the defect, so if the corpus is ever corrected it goes red
and the note gets revisited. **This is the standing argument for
reading EVERY commentary rather than the first one that answers: one
source being wrong is invisible until a second is asked.**

**SCAR — I overwrote a file I had not read.** `adhyaya_2_pada_4.py`
already existed, registering 2.4.72 and 2.4.74 from the लोलुवः run, and
a Write call replaced it whole. Nothing failed loudly: the suite went
green-minus-seven for reasons that all looked like the ordinary gaps of
a new chunk, and the two lost rules showed up only because the pāda's
codified list was checked by hand. They were recovered from the
scratchpad script that had written them. **Before writing over a path,
read it — and when a Write reports "updated" rather than "created",
that is the file telling you it was already there.**

**A grouped enum arrived as a string, and every rule keyed on it
silently matched nothing.** The playground rebuilds enums for top-level
parameters but never did for members of a dataclass, so
`Compound.samasa` reached the rule as `'DVIGU'` instead of
`Samasa.DVIGU` and 2.4.1 answered "no rule reaches this" for its own
worked example. The same shape as `Pair.first_vibhakti` and
`samasa_of`'s missing parameter: **a condition no input could meet, in
code that reads as though it works.** Fixed in `_rebuild_members`,
which now rebuilds enum members the way `_rebuild_enum` always did for
parameters.

**A vārttika misread twice, and tests caught it both times.**
बहुप्रकृतिः फलसेनावनस्पतिमृगशकुनिक्षुद्रजन्तुधान्यतृणानाम् was written
as a condition inside 2.4.12's row, on the assumption that its eight
kinds were a subset of that sūtra's ten. They are not: फल, सेना,
वनस्पति and क्षुद्रजन्तु appear in no sūtra of the run, and the
vārttika's own examples name the rules it actually reaches — बदरामलके
is 2.4.6's, यूकालिक्षे is 2.4.8's, रथिकाश्वारोहौ is 2.4.2's. It
restricts whichever rule would have given एकवद्भाव. Lifted out of the
row; then the second test failed, because 2.4.9's च makes एकवद्भाव
obligatory for animals that are enemies and काकोलूकम् is exactly two
birds — so 2.4.9 stands above the vārttika as well as above 2.4.12.
शकुनि is named by all three rules, which is what made the order
visible. **A gaṇa quoted in a vārttika is not thereby a subset of the
sūtra it is attached to.**

**A field name that meant two different things.** `anga` is the अङ्ग of
6.4.1 everywhere else in this codebase — the stem an affix attaches to
— and in 2.4.2 it is a LIMB, of a body, an instrument or an army. The
shared name gave the form a hint that told a beginner the exact wrong
thing. Renamed `anga_of`, with `jati` → `jati_of` (2.4.6 needs WHICH
kind of class, not a yes) and `members` → `member_count` for the same
reason. **A field whose help has to begin "but in this pāda it means
something else" has the wrong name.**

Two guards were widened, and both got stricter for it. The
registration-order test measured contiguity across a whole pāda, which
2.4 is the first to break by being read from the start while holding
two rules reached ahead; it now sets those aside first and asks whether
what remains is the run 1..N. The attribution guard consulted only the
segmented Mahābhāṣya, which has nothing for 2.4.1, and reported a
quotation that IS in the corpus as absent from it; it now reads both
paths, so quotations it could never confirm before are confirmed or
fail.

2.3.58–2.3.73 close the pāda, and with it **all 73 of 2.3**,
contiguous. The last stretch is the कृत् genitives: 2.3.65
कर्तृकर्मणोः कृति gives both the doer and the object a sixth before
a primary derivative, 2.3.66 takes it back from the doer where both
could have it, 2.3.69 and 2.3.70 refuse it to nine kinds of
derivative outright, and 2.3.67 and 2.3.68 carve two ways back
through that refusal.

**The two pādas write to each other.** 2.3.65 to 2.3.68 CREATE the
genitives that 2.2.12 to 2.2.16 then forbid to compound — the same
phrases stand in both places. राज्ञां मतः takes its sixth from
2.3.67 and is kept from compounding by 2.2.12; इदमेषाम् आसितम् from
2.3.68 and 2.2.13; गवां दोहः from 2.3.66 and 2.2.14; भवतः शायिका
and अपां स्रष्टा from 2.3.65 and 2.2.15/2.2.16. One pāda hands out
a case and the pāda before it says those two words may not be
joined. Neither reads alone, and codifying 2.2 first is what made
the echo visible when 2.3 arrived — the examples were already in
the file.

**An exception clause is not the rule that acts — the sixth time.**
2.3.72 excepts तुला and उपमा by name from the third case it offers
the rest of the group, and the counter-case came back
`by="2.3.72"`. But a rule that excepts a word does not thereby
govern it: तुला's sixth comes from **2.3.50 षष्ठी शेषे**, the
remainder that 2.3.72 never displaced. The counter-case guard
caught it, which is the fifth time a written test has caught this
shape and the first time it was caught by a test rather than by
reading. That is the guard doing its job — but six occurrences
means the reflex still is not automatic, so the check is now
explicit in §4: **after writing any exception, ask which rule
supplies the answer, and name that one.**

Two smaller things worth keeping. 2.3.64's कृत्वोऽर्थप्रयोगे turns
on the affix being *used*, not merely meant — अह्नि शेते keeps its
seventh because no कृत्वस् is there to trigger it, which is a
condition on the surface form and not on the sense. And 2.3.62's
बहुलम् is the rule's own word, so both the sixth and the fourth are
correct in the Veda; `also` carries that rather than a choice being
made on Pāṇini's behalf.

2.3.42–2.3.57 bring in the FIRST case — 2.3.46 प्रातिपदिकार्थ…
मात्रे प्रथमा, where nothing beyond the stem's own meaning is
meant — and with it 2.3.50 षष्ठी शेषे, the leftover genitive.

**शेष is asked last, and has to be.** कर्मादिभ्योऽन्यः
प्रातिपदिकार्थव्यतिरिक्तः शेषः — whatever relation is left when
every kāraka has been taken and the bare stem-meaning too. A
remainder cannot be computed before the things it is the remainder
of, which is the same shape as 2.2.23 शेषो बहुव्रीहिः, and the two
sūtras are why राजपुरुषः is the stock example of both 2.3.50 and
2.2.8.

One OPEN kept rather than resolved: 2.3.51's अविदर्थ. The Kāśikā
gives two readings of what it excludes — the verb of setting about
a thing, or the verb of mistaken apprehension — and chooses
neither. Both are recorded and neither is taken.

2.3.27–2.3.41 carry the pāda to 2.3.41 — the ablative, the
genitive and the locative, and the four kārakas that had not yet
been given endings.

**A field that could hold one alternative met a rule offering
three.** दूरान्तिकार्थेभ्यश् चतस्रो विभक्तयो भवन्ति — words of
far and near take four cases across 2.3.34, 2.3.35 and 2.3.36, and
an `also` holding a single second choice made a four-way option
look binary. It is a tuple now.

Those same three rules cannot be told apart by their conditions,
so only the first can be named as the rule that fired. 2.3.35 goes
on the guard's own escape list with that reason written out —
which is the honest form of an exception: not a silenced test but
a recorded one.

**And the refusal-naming-its-own-rule shape appeared a fourth
time**, at 2.3.40. Four occurrences is no longer a coincidence: a
result type that carries `by` needs to distinguish "this rule
acted" from "this rule declined", and every place that conflates
them turns a counter-example into a worked one.

2.3.14–2.3.26 carry the pāda to 2.3.26: the rest of the fourth
case, then the third, then a run of four rules on the हेतु that
narrows itself twice and changes case twice.

**A refusal must not report the rule that refused.** 2.3.19's
अप्रधान counter came back `by="2.3.19"`, and the chip guard read
that as the rule having fired — the third time this exact shape has
appeared, after the reduplication entry points and the >2 dvandva
case. The counter moved to a unit test, where a refusal can be
asserted as a refusal instead of being squeezed into a field that
means something else.

Two things worth keeping from the reading. अक्ष्णा काणः is 2.3.20's
worked example AND 2.1.30's counter-example: the same phrase seen
from opposite ends, blind IN the eye rather than blinded BY it.
And 2.3.24's अकर्तरि turns on the same hundred changing case with
its role — शताद् बद्धः against शतेन बन्धितः — because there the
debt is what set the binding going and is therefore a कर्तृ.

2.3.1–2.3.13 open the vibhakti section, and this is where two
halves of the grammar meet. 1.4.23 to 1.4.55 decide WHICH kāraka a
participant is and have been codified since adhyāya 1; these rules
take that answer and give it an ending.

**2.3.1 अनभिहिते gates the whole section**, and its list of what
can already have expressed a kāraka is closed —
तिङ्कृत्तद्धितसमासैः परिसंख्यानम्, four and no more. Being a
परिसंख्या it is a tuple and not a flag, and a fifth name is
refused rather than quietly accepted.

**And the kāraka is passed in, not asked for.** That is the same
shape as 2.2.30's SCAR two pādas earlier: deciding which kāraka a
participant is needs the whole clause, not the one word, so no
reuse is declared. The dependency is real in the grammar and is
not a call in the code, and the difference is now written where
the rules are rather than discovered again by a red test.

2.2.30–2.2.38 finish the pāda, and with it **the whole compound
section**: 2.1.1 to 2.2.38, both pādas contiguous, which is the
range 2.1.3 प्राक् कडारात् समासः named at the start.

These nine ask a question none of the rules before them asks —
not whether two words join but which comes out FIRST — so they
went into their own module rather than into a field of the
provision table bent to hold them.

**Where a rule can be asked, ask it; where it cannot, say so.**
Three helpers looked equally available and only one was. 1.4.7
answers घि from the word itself, so 2.2.32 fetches it. 1.1.26
decides whether an AFFIX is निष्ठा and is handed a word here, and
1.2.43's upasarjana depends on the rule that formed the compound
rather than on either word — so those two are stated. Both had
been declared as reuse and neither was a call; the reuse test
caught it. A dependency real in the grammar is not thereby a call
in the code.

Two guards went stale in ways worth keeping. A test that wanted an
UNCODIFIED sūtra under 1.4.1 ran out of them — that heading reaches
to 2.2.38 and the section is now finished — after two earlier
versions had already gone stale by naming a sūtra. Naming a
heading is only a slower way of naming a sūtra. And the search
that replaced it landed on 2.3.1, which is its own अधिकार: the
corpus lists a heading as governed by itself, and a graph rightly
draws no edge from a sūtra to itself.

2.2.23–2.2.29 fill the gap SAMJNAS has carried since it was
written. That table said बहुव्रीहि and द्वन्द्व were left out
deliberately — a range asserted from memory of the tradition
rather than from the commentary is the kind of claim this
codification does not make. They have been read now, and the four
pradhānas are complete: अव्ययीभाव means what its first member
means, तत्पुरुष its second, बहुव्रीहि a third thing that is
neither, द्वन्द्व both at once.

**Only one of the two turned out to be a heading.** शेषो बहुव्रीहिः
governs 2.2.23 to 2.2.28 — it names the REMAINDER, whatever no
other rule has claimed, which is why it can be stated before the
rules that form them. चार्थे द्वन्द्वः governs nothing: it confers
its name on what it itself makes. Put into SAMJNAS it needed a
range and the only one available was its own number, which the
test guarding against copied ranges caught at once. A name a
single sūtra confers now comes from the provision, and resolve
reads both sources — they coincide for every rule of the first
pāda and come apart at 2.2.29.

**PENDING — 2.2.30 to 2.2.38 decide which member is spoken
FIRST.** उपसर्जनं पूर्वम् and the eight rules after it are a
question this table does not answer at all: it says whether a
pair compounds and under what name, not what order the words come
out in. Recorded as the next thing to build rather than
half-modelled into a field that does not mean it.

2.2.12–2.2.22 carry the pāda to 2.2.22: five more prohibitions of
the genitive, three obligatory rules, a नियम and two options.

**A prohibition that does not say what it prohibits will refuse
pairs nobody offered to it.** 2.2.11's अव्यय blocked स्वादुंकारम्,
an उपपद compound with no genitive anywhere in it — because the
prohibition rows fired on the fact alone. They forbid 2.2.8 षष्ठी
and reach only what 2.2.8 would have taken, so they now carry the
case they forbid and skip a pair that never stood in it.

Two tests had to be scoped to their own pāda for a reason worth
keeping: `nitya` means different things on the two sides of the
boundary. In 2.1 it marks a rule ESCAPING the विभाषा heading, and
the test rightly demands each say what the phrase cannot convey —
नहि वाक्येन. In 2.2 no such heading runs, so 2.2.17 to 2.2.20 are
obligatory simply because they say नित्यम्, with nothing overhead
to argue against and therefore no phrase to rule out. A test that
demands a justification only makes sense where something is being
justified against.

2.2.1–2.2.11 open the second pāda around 2.2.8 षष्ठी, the commonest
compound in the language: 2.2.1–5 are its exceptions, 2.2.9 a
re-permission, and 2.2.10–11 its two prohibitions.

A prohibition was a shape the table could not hold. 2.1.7 could
refuse a pair because a rule narrowed an earlier one on a NAMED
WORD; न निर्धारणे refuses a whole class outright. Rows now carry
`prohibits_when`, and resolve asks those before it asks what forms
anything — a prohibition does not compete with 2.2.8 for the pair,
it takes the pair away from it.

**And the new pāda caught a reading that had been wrong all along.**
`optional` computed विभाषा as "anything after 2.1.11", which was
true while 2.1 was the whole codified section and became false the
moment 2.2 existed: all eleven new rules came out optional with
nothing having said so. The text settles the bound — 2.2.3 says
अन्यतरस्याम् in so many words and 2.2.4's Kāśikā argues सोऽपि भवति
for its second reading, neither of which would be worth saying if
an option were already running overhead. The heading is bounded to
its own pāda now, and a rule outside it that is optional says so
itself. Two of the eleven do; nine are obligatory.

A heading whose range is inferred from where it starts and nothing
else will be right until the day the work reaches past it.

2.1.62–2.1.72 close the pāda, and **अध्याय २ पाद १ is complete** —
all seventy-two, in order. The first pāda finished outside adhyāya 1.

The clearest sign it was finished came from a test rather than a
count. 2.1.1 sat on the reached-ahead list because the pāda was once
a stub entered early for its paribhāṣā; the guard that checks every
sūtra outside adhyāya 1 is either reached ahead OR read in order
noticed the pāda had become contiguous and said so in as many words
— take it out of IDS. A list that describes the work has to notice
when the work moves past it.

And a third nipātana rule, 2.1.72 मयूरव्यंसकादि with its
eighty-three ready-made forms, broke the two-item roll for the same
reason the नित्य and बहुल rolls broke before it. Three times now the
same shape of test has failed the same way, and the fix is always to
assert the property rather than the census: here, that no two of the
three lists are the same, which is what makes the field a list and
not a flag.

2.1.52–2.1.61 closed the run to the end of the pāda's तत्पुरुष
section. 2.1.52 संख्यापूर्वो द्विगुः finally gives 2.1.23 something
to work on: that sūtra extends तत्पुरुष to a द्विगु and had been
registered for weeks with no rule under it conferring the name.

The run forced two additions and turned up one collision.

**A row can now be blocked by a fact, not only required by one.**
2.1.58's nine words include पूर्व and अपर, and 2.1.50's own
examples — पूर्वेषुकामशमी, अपरेषुकामशमी — are those very words
with a name meant. Both rules reach them, and 1.4.1 alone hands it
to 2.1.58 as the later, while the Kāśikā cites the form under
2.1.50. The narrower rule is taken to govern and 2.1.58 refuses a
pair where संज्ञा is stated — marked OPEN on the rule itself,
because nothing read so far says that in as many words. A rule
held off a case it would otherwise reach has to say so where it is
written, or the table quietly disagrees with the sūtra it claims.

**A second बहुलम्, and a second list-of-one broken.** 2.1.57's
बहुलम् is व्यवस्थार्थम्, settled case by case; 2.1.32's is
सर्वोपाधिव्यभिचारार्थम्, any condition departable. The test that
named 2.1.32 as the only one was rewritten to hold what actually
matters — that each says what its बहुलम् is FOR.

And the gloss guard caught me reopening 2.1.52 with 'Gives a
name' — the exact stub that was ruled out months of work ago.

2.1.41–2.1.51 finished the pāda's locative run and then changed its
footing: from 2.1.49 the rules stop pairing by case at all and pair
by समानाधिकरण, the two words referring to one thing.

Three things the run turned up. A field that was a bool standing for
one particular answer: `nipatana` meant 2.1.17's तिष्ठद्गुप्रभृति,
and 2.1.48's पात्रेसमितादि wanted the same shape with a different
list — it holds the forms now, both read from the gaṇapāṭha.

A worked input that could only be used by someone who did not need
it: from 2.1.30 the conditions stopped naming words and started
asserting facts, and the generated inputs came out as a form of
ticked boxes with nothing to compound. The seed table took one seed
per sūtra, and 2.1.50 covers a direction-word and a numeral, which
no single pair illustrates. It takes one seed per row now, and a
test holds that every input in the pāda offers both words.

And a note that named the right sūtra number with the wrong sūtra:
2.1.23 said द्विगु is defined at 2.1.52 तद्धितार्थोत्तरपदसमाहारे च.
2.1.51 is that text and forms the compound; 2.1.52 संख्यापूर्वो
द्विगुः is what names it. Written from memory of the tradition
rather than from the सूत्रपाठ, and it stood until the pāda was read
in order — which is the argument for reading in order.

2.1.30–2.1.40 followed, and the तत्पुरुष section is now contiguous
from 2.1.1. These eleven stop naming senses and start naming cases —
third, fourth, fifth, seventh — each with the words it pairs with.
One defect, and it was only reachable here: every earlier तत्पुरुष
names the SECOND member and puts the case on the first, so a rule
written that way passes on all of them. 2.1.39 runs the other way —
स्तोक and its fellows stand in the fifth case themselves — and it was
written like its neighbours, so स्तोकान्मुक्तः compounded by nothing.
Caught by testing against the Kāśikā's own form rather than against
the shape of the rule beside it.

2.1.32's बहुलम् is recorded rather than run. सर्वोपाधिव्यभिचारार्थं
बहुलग्रहणम् — the word is there so that ANY condition may be departed
from, and दात्रेण धान्यं लूनवान् meets them all and still does not
compound. A rule that may ignore its own conditions cannot be run in
either direction and be honest.

### Use what is on disk

Before writing a list, look for the text that has it.

The `reference/` tree holds 15 commentaries, 921 vārttikas, 2,259 dhātus, 262
gaṇas and 5,340 literary attestations. The gaṇapāṭha in particular went
unused for a long time and now supplies seven groups across four sūtras.
Auditing it changed the work: the
apparatus went from 4 sources per sūtra to 10; reading the vārttikas closed an
open question on 1.1.51 (`लपर इति वक्तव्यम्` — the vārttika I had said must
exist but could not cite) and turned up a restriction on 1.1.62 the Kāśikā does
not give; 1.1.20's six *ghu* roots are derived from the dhātupāṭha and match the
Kāśikā's own count; 1.1.27's thirty-five sarvanāmans are the Gaṇapāṭha's list.

The same discipline applies when a source turns out to be useless. Katre is
downloaded and unreadable — OCR'd with a Devanāgarī model, English destroyed,
no better derivative on archive.org. That is recorded as `UNREADABLE`, a
distinct status from `PENDING`, so nobody hunts for it again.

### Be as transparent as possible

A limitation that is recorded is not a failure. A limitation that is hidden is.

Every gap is visible in the interface, not only in the code: a sūtra with an
unresolved finding carries a dot and an eye showing the finding **verbatim**;
the collapsed Sources panel names what is missing (`10 read · 3 not yet
consulted · 1 unreadable`) so a shut panel cannot imply a complete apparatus;
uncodified nodes in the dependency graph are drawn differently and are not
clickable.

The record enforces it: a `VERIFIED` reading without a locator is refused, a
`PENDING` one must stay empty, an `UNREADABLE` one must explain itself.

The resolvers say what they could not decide, rather than answering anyway.
`near_misses` names the condition that was wanting when a rule almost fired, so
a semantic condition left unstated reads as unstated and not as false. Where a
root name is read twice in the dhātupāṭha with different marks — 174 of the
1,590 are — the verdict says so instead of quietly taking the more generous
reading. And a verdict names what it displaced, so 1.4.1 and 1.4.2 doing their
work is visible rather than inferred.

### Anyone should be able to learn from it

The newest of the five, and the one most easily lost: **a page has to work
for a beginner and a scholar at once**, and the beginner is the harder case
because their difficulty is invisible from the inside.

The scar is 1.1.1. Its gloss opened *"Gives a name."* — accurate, and no use
whatever to someone starting out. It does not say what naming is *for*, or
why a grammar would spend its opening rule on three vowels instead of
explaining something. And the missing knowledge was never about 1.1.1: it was
about how the Aṣṭādhyāyī is built, which is the same gap at all 200 saṃjñā
rules. Two hundred glosses were each gesturing at it in three words and not
one of them was answering it.

Four things follow, and they are now how this is written:

- **Explain the kind once, not the rule two hundred times.** The corpus sorts
  every sūtra into five kinds, so five paragraphs reach all 3,983 — including
  the 3,604 not yet codified. A per-sūtra answer to a per-kind question is
  both more work and worse writing.
- **Do not obstruct the reader who already knows.** That orientation is
  collapsed to a two-word label with *what does that mean?* beside it. Printed
  in full on every sūtra it would teach the newcomer once and then be in their
  way for three hundred rules.
- **Never make the reader hold two scripts at once.** देवनागरी (iast),
  everywhere and in both directions — no Sanskrit without its roman, no roman
  without its Sanskrit.
- **Every label is read cold.** A worked-input chip is the whole of what a
  reader has when they click it, so it has to be a claim and not half of one.
  *"but ए is not"* said neither what ए fails to be nor that anything preceded
  it; 103 labels were of that shape.
- **A form asks in words, not in parameter names.** The playground builds its
  inputs from the signature of the function that codifies a rule, so left to
  itself it labels them `al vidhi`, `purva vidhi`,
  `dvirvacana caused by vowel`. That is the failure in its purest form: a
  reader who could act on those would not need the form, and a reader who
  needs the form cannot act on them. All 172 field names across all 379 rules
  now carry a question a person can answer *and* the Sanskrit term behind it —
  *does the rule work on sounds?* over
  <span>अल्विधि</span> — so one line serves the beginner and the reader who
  only wanted the term.

The rule this replaces is the temptation to write for the person who already
agrees with you. Terseness that reads as elegance from the inside reads as a
closed door from outside, and this project has no reason to have one.

## 4. What "done" looks like for one sūtra

- [ ] Text agreed across witnesses, or the disagreement recorded
- [ ] Every commentary on disk read for it
- [ ] Findings written, each marked `SETTLED`, `OPEN` or `SCOPE`
- [ ] Rule codified — deriving, not tabulating
- [ ] Tests from the commentary's own worked examples, including its
      *kim* counter-examples, which are where the conditions live
- [ ] Every exception answered by the rule that SUPPLIES the case,
      not the rule that excepted it — a rule which excepts a word
      by name does not thereby govern it (2.3.72 excepts तुला,
      2.3.50 शेषे is what gives it a sixth)
- [ ] A plain-English gloss with a worked form, both scripts
- [ ] At least one ready-made input, so the rule can be run without knowing
      what to type — derived from the conditions where there is a table
- [ ] Registered, so it appears in the report and the browser

## 5. Standing decisions

Settled. Do not re-litigate without a reason.

| Question | Decision |
|---|---|
| Which witness for the sūtra text | **Vidyut** where they differ. GRETIL has real data-entry errors — `duṭū` for *cuṭū*, `prayarnaṃ` for *prayatnaṃ*. data.json agrees with Vidyut on 3,980 of 3,983. |
| Reusing others' work | **Yes, and build on it.** Vidyut, Ambuda, the Sanskrit Library, GRETIL, ashtadhyayi.com. Their data is in `reference/` with a SHA-256 manifest. |
| Writing over a file that may exist | **Read it first.** `adhyaya_2_pada_4.py` already registered 2.4.72 and 2.4.74 when a Write replaced it whole; nothing failed loudly, and the loss showed up only on a hand check of the pāda's codified list. A Write that reports *updated* rather than *created* is the file saying it was already there. |
| Books still in copyright | Obtain legitimately or leave `PENDING`. **Not** via shadow libraries — the non-profit framing does not change the licence, and open-sourcing raises the exposure. Sharma and Joshi & Roodbergen are borrowable through controlled digital lending. |
| Marking a finding | `SETTLED` = a conclusion. `OPEN` = a question the sources did not settle. `SCOPE` = something we deliberately do not do. Every sūtra reaches at least one. |
| When a rule needs something we cannot compute | Take it as a parameter and say so. Semantics, accent in an unaccented text, whether आङ् is meant — the caller answers, the docstring explains why. |
| Where glosses live | Their own module, not the sūtra records. The notes are the working record for someone who has the vocabulary; a gloss is for someone who does not, and is not a claim. |
| A block of near-identical rules | **A provision table**, not one function each. The conditions are declared once and everything else — records, codification lines, worked inputs — is generated from them. Used for 1.2.1–26, 1.3.14–93, 1.4.23–55, 1.4.56–98. |
| A rule taking something no form can express | Give it a **string entry point** with a written syntax, and document the syntax where the parameter is. `gārgya:vṛddha` for 1.2.65's pair. Otherwise the rule is unreachable from the interface, which is a silent gap. |
| Two names applying at once | Ordinarily 1.4.1 forbids it. It is restored only by an explicit device, and the text names three: 1.4.55's च, 1.4.56's प्राक् range, 1.4.60's च — each with संज्ञासमावेशार्थ stated. A codification returning one name where the text restores two loses the point of the section. |
| Which script the reader types in | **Either.** Devanāgarī is converted to IAST at the one boundary where input arrives, and the call is echoed back so a wrong transliteration is visible rather than guessed at from a surprising answer. What is not a Sanskrit word — a sūtra number, a sense-name, an asserted condition — is left untouched, since converting it would make its rule stop matching silently. |
| Explaining what kind of rule this is | **Once per kind, never per sūtra.** The corpus classifies all 3,983 into five, so five paragraphs cover the grammar, and the answer to "why does it open by naming three vowels" is written where it is true of all 200 saṃjñā rules rather than guessed at 200 times. Collapsed by default, so it teaches without obstructing. |
| Which script the reader sees | **Both, always, in one shape** — देवनागरी (iast). A transform pairs them at the boundary, and it acts only where it can *prove* the roman is the transliteration of the Devanāgarī: `root`, `name`, `sense` and `voice` sit in the same sentences as `gati`, `veda` and `kit`, and all of them round-trip. Proper nouns are paired too; English plurals of loanwords are not, since शिवसूत्रस् is a word in no language. |
| A rule that fixes a form outright | **Its own entry point, and registered against it.** यदिह लक्षणेनानुपपन्नं तत् सर्वं निपातनात् सिद्धम् — a निपातन is what the rules do not reach, so a table deriving it would be pretending. The seventeen of 3.1.96–132 and 3.2.26 are given as they stand, with what the vṛtti says is being fixed in each. And the registration must carry that function too: 3.2.26 was first registered against the table's, so its worked input had nothing to run. A test asserts every rule of a run is in exactly one of the two, since a gap would be a rule nobody had read. |
| A dependency between two sūtras | **Declared, not inferred.** Where one rule's implementation genuinely runs another's, the sūtra says so — `reuses=('1.1.3',)` — and a test checks the cited rule is codified and its implementation reachable. Delete the call and it goes red. Not every textual edge earns a declaration: 6.1.77's अचि descends into 6.1.78 as a condition the caller states, and 6.4.1 अङ्गस्य is a heading. `reuses` is for where code runs code. |
| A notion another rule already decides | **Ask it.** The engine chose तिप् for every root while eighty codified sūtras of pada selection sat unconsulted, so एध् — anudāttet, middle by 1.3.12 — came out एधति. The dependency existed in the grammar and in this codebase, and not in the code that needed it. Anything a rule decides is fetched from that rule: the pada from 1.3.12–93, the ending from 1.4.99–102, the root's initial from 6.1.64/65, एच् from the śivasūtras. |
| Naming an operation | **From a closed vocabulary, never as free text.** Rules that *name* an operation rather than perform one — 1.1.58's ten, 2.1.2's two, 8.2.2's four — were matching bare strings against bare strings, so `dirgha` for `dīrgha` returned the opposite verdict under a different sūtra and nothing said so. Every operation is now a record with both scripts, a gist, and the sūtra prescribing it where one does; an unknown name is refused, a rule's list is checked at import, and the form offers a list rather than a box. |
| What a form field asks | **A question, with the term under it.** The label is built for someone who does not know the vocabulary — *was the thing replaced a vowel?* — and the hint names what it stands for — स्थानिन्. Neither alone is enough: the label by itself strands the scholar, the term by itself strands everyone else. Written once per parameter name in `fieldhelp.py`, so a name shared between rules is described once. |
| A worked-input label | **It must stand alone.** The reader clicking a chip has not read the chip beside it, so no label may open with a connective, end on a dangling verb, or lean on a neighbour with "likewise". The ✕ already carries the contrast; a label that spends a word repeating the icon has less room for the part that was missing. |
| Two kinds of विभाषा | अप्राप्तविभाषा yields to an invariable rule; प्राप्तविभाषा displaces one. The Kāśikā names them apart (1.3.43 against 1.3.50), and collapsing them gets ऋक्ष्वस्य क्रमते बुद्धिः wrong. |

## 6. Order of work

Roughly, and by dependency rather than by number:

1. ~~**Finish adhyāya 1.**~~ **Done.** All 351 sūtras — 75, 73, 93 and 110.
   The kārakas are in, and so are the two rules the rest of the grammar is
   read through: 1.4.1 आ कडारादेका संज्ञा and 1.4.2 विप्रतिषेधे परं कार्यम्.
2. **The paribhāṣās wherever they fall.** Well begun. The asiddhatva family is
   in — 8.2.1, 8.2.2, 8.2.3, 6.4.22, 6.1.85, 6.1.86 — with 2.1.1 समर्थः
   पदविधिः and 3.1.94 वासरूपोऽस्त्रियाम्. Between those and 1.4.1/1.4.2, the
   rules governing rule **conflict** and rule **visibility** are both
   codified, which is the pair a derivation engine has to consult at every
   step. What remains are the smaller ones scattered through 3–7, and the
   Paribhāṣenduśekhara's list is the natural index to work from.
3. **The derivation engine.** **Built** — `prakriya.py`. It applies rules in
   sequence rather than answering one question, and it consults both of the
   rules that make a derivation faithful: *which rule wins* where two contend
   for one place (1.4.2, with its three exclusions) and *what an earlier step
   is even visible to* (8.2.1, in both directions). Neither is a detail —
   8.2.1 switches 1.4.2 off for the last quarter of the grammar.

   **It derives whole words**, and now a whole paradigm: all nine present
   forms of पच् — पचति, पचतः, पचन्ति, पचसि, पचथः, पचथ, पचामि, पचावः,
   पचामः — besides जयति, भवति, भरति, नयति, एधते and शयते. Each step names
   its own sūtra.

   Two of those steps are the first real विप्रतिषेध the engine has met, and
   both are अपवाद relationships the commentaries state outright rather than
   leave to be worked out: 7.1.3 झोऽन्तः against 1.3.7 चुटू for the झ् of
   झि, and 6.1.97 अतो गुणे against 6.1.101 अकः सवर्णे दीर्घः for the अ + अ
   of पच + अन्ति. Lose either and the received form is underivable — पचै
   for the one, पचान्ति for the other. 1.4.2 settles both the way it says
   such clashes are *not* settled: by position yielding to the exception. Three came free once
   the first five rules were in; the last two came from making the engine
   *ask what was already codified* rather than choose for itself. The five sūtras that took it
   there — 3.1.68, 3.4.113, 7.3.84, 7.2.114, 6.1.78 — were chosen by working
   backwards from one word rather than down the list, and that is the method
   worth keeping: pick a word, add exactly what it needs, and the output is
   checkable against a derivation any grammarian can confirm instead of
   against our own worked examples. Nothing in the engine changed to admit
   them; rules join at one place, `prakriya_rules.all_rules`.
4. **The operational rules themselves**, adhyāyas 6 and 7 above all, which
   is what the engine is now waiting on.

## 7. Known threads, largest first

- **Kātyāyana's vārttikas.** 921 of them, few codified. The largest single
  body is the nine on **8.2.3**, each declaring some further operation सिद्ध
  where 8.2.1 would have hidden it — together a substantial qualification of
  the tripādī's asiddhatva. Then eight of the nine on 1.1.72, eight on 1.3.21,
  seven on 1.4.52, and four on 1.1.58. Most need operations modelled as
  objects rather than passed as strings. One
  (`पूर्वत्रासिद्धे न स्थानिवत्`) ties 1.1.56–59 to the tripādī at 8.2.1 —
  and now that 8.2.1 is codified, that one is reachable. The obstacle the
  rest shared — operations passed as bare strings — is gone: they are a
  closed vocabulary now, so a vārttika declaring something of an operation
  has an operation to declare it of.
- **The Mahābhāṣya on disk is question-openers only.** All 220 of its
  non-empty readings across the codified sūtras are a single sentence —
  किमर्थम् इदम् उच्यते, किम् इदम् मुखनासिकावचनः इति — the question Patañjali
  raises, never the answer he gives. This surfaced while trying to close one
  OPEN note on 1.1.1, and it is the more useful finding: it bounds what any
  note may claim of the bhāṣya.

  An audit of the 30 Sanskrit quotations credited to it found **1** carried
  by the bhāṣya text, **14** present in the corpus under another source —
  mostly the Kāśikā, which quotes Patañjali and quotes him accurately — and
  **15** nowhere on disk. The content was not thereby wrong; the citation
  was, and a reader following it arrived at a forty-character question that
  did not contain the claim.

  **Done.** Eleven notes re-attributed to the source that carries them, and
  every quotation that is nowhere on disk now says so in its own paragraph.
  The rule enforced from here is not that everything must be in the corpus —
  much of the tradition is not, and pretending otherwise would be worse. It
  is that **a quotation is either checkable where the note says, or the note
  says it is not checkable**, with nothing quietly in between.
  `test_astadhyayi_attribution.py` holds it, and it also asserts the premise:
  if a fuller bhāṣya is ever added, the test fails on purpose, because the
  notes marked unverifiable could then be checked and someone should go and
  check them.

  One correction made while making the correction, which is worth recording
  as its own scar: re-attributing 8.2.3 I wrote that the corpus carries the
  nine vārttikas. It carries **two**. Fixing a bad citation with another bad
  citation is easy enough to do that the count now sits in the note.

- **The उच्चारणार्थ vowel** — the one making a consonant-final anubandha
  pronounceable — is not removed, because no codified rule removes it. डुपचष्
  yields पच, आनङ् yields आन.
- **Accent** is modelled (1.2.29–32) but not folded into grahaṇa: the
  sūtrapāṭha on disk is unaccented, so widening every term to three accented
  forms would manufacture forms occurring nowhere in the data.
- **A root name can be read twice with different marks.** 174 of the 1,590
  names in the dhātupāṭha are — वह् is anudāttet in one entry and svaritet in
  another — and the commentaries disambiguate by citing the sense. The
  codification takes an `artha` for that, and reports the ambiguity when none
  is given. It does not *resolve* it.
- **Semantic conditions are inputs, everywhere.** ध्रुव, ईप्सिततम, स्वतन्त्र,
  क्रियायोगे, समर्थ: no reading of a form settles any of them. This is not a
  gap to be closed but a boundary to be stated, and every affected record
  states it.
- ~~**No derivation engine.**~~ **Built**, and its rule set is the thread
  that replaces it: the engine can apply only what is codified, and what is
  codified that *operates* is 1.3.2–1.3.9. Everything else answers a
  question. Adhyāyas 6 and 7 are now the bottleneck rather than the
  machinery.

## 8. How to know we are not fooling ourselves

- The suite runs green and the count of tests grows with the count of
  sūtras.
- Every one of the 3,983 has a beginner-facing gloss. 3,734 have at least
  one worked case, 4,028 in all — and the 249 that have none are ALL in
  अध्याय १ and २, which were codified before the worked-case convention
  existed. That is the shape of the depth still owed: not scattered, but
  concentrated in the oldest work, and countable.
- `--astadhyayi open` is short and every entry on it is real. With all 32
  pādas codified it lists EIGHT sūtras — 1.1.1, 1.1.70, 1.2.5, 1.3.11,
  1.4.20, 2.3.51, 7.4.60 and 7.4.83 — beside 155 with a stated SCOPE. Eight
  open questions in 3,983 rules is what finishing the coverage leaves; it
  is not what finishing the work would leave, and the difference between
  those two numbers is the whole of what is still to do.
- Some claim gets falsified by our own machinery, periodically. When 1.1.69
  showed that e~ai savarṇatva would put a guṇa vowel inside vṛddhi, that was
  the system working. When the curated inputs turned out to disagree with the
  rules they were filed under, that was the system working. If nothing ever
  contradicts a note, the notes are not saying enough to be wrong.
- A test that goes red because the work advanced is a good sign, and there
  have been several — one named `..._though_nothing_codified_uses_it_yet`
  failed on the day something did. Each was rewritten to assert the property
  rather than the snapshot. A test tuned to this week's numbers is not a test.

---

*If any of this misstates what you wanted, say so and it changes — this is the
document that governs the rest, so it is worth getting exactly right.*
