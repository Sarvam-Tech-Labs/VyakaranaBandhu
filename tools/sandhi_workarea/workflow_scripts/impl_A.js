export const meta = {
  name: 'sandhi-A-continue-drafts',
  description: 'Continue the recovered drafts of ac_yan_ayadi and ac_ekadesa, then review each adversarially',
  phases: [
    { title: 'Implement', detail: 'one agent per rule family, in its own workspace copy of the repo' },
    { title: 'Review', detail: 'an independent adversarial reviewer per family, in the same workspace' },
  ],
}

const REAL = '/workspaces/codespaces-blank/VyakaranaBandhu'
const WSROOT = '/workspaces/codespaces-blank/sandhi_work/ws'
const DATA = '/workspaces/codespaces-blank/sandhi_work/scratch/sandhi_data'

const PREAMBLE = (f) => `
You are implementing ONE FAMILY of rules for a PANINIAN SANDHI ENGINE: given words (or word pieces) it derives the junction step by step, citing for EVERY step the exact sutra of Panini that applies, saying what is replaced by what and why. The engine core exists and is tested; your job is the rules of one family.

YOUR WORKSPACE - an isolated copy of the repository at ${WSROOT}/${f.id}. Work ONLY there: cd into it, run everything from its root (python3 -m unittest ...). The real repository (${REAL}) is off limits; other agents are working in their own copies at the same time, and your files will be merged from your workspace when you finish.

FILES YOU MAY CREATE OR MODIFY (and no others):
${f.files}
Do NOT modify any other file - in particular NOT the core (src/astadhyayi/sandhi/segs.py, rule.py, engine.py, supports.py, parse.py, trace.py, rulebook.py, __init__.py, __main__.py) and NOT other families. If the core lacks something you need, work around it with local helpers inside your family file and record it in 'core_requests' in your final report.

READ FIRST, in this order:
 1. ${WSROOT}/${f.id}/src/astadhyayi/sandhi/README.md  - THE SPECIFICATION. Its 'Writing a rule' section lists conventions that each cost a failure. Follow every one.
 2. The core: segs.py, rule.py, engine.py, supports.py, parse.py, trace.py (all under src/astadhyayi/sandhi/), and the four skeleton families in src/astadhyayi/sandhi/families/ - they are the PATTERN: ac_ekadesa.py and visarga_ru.py especially.
 3. tests/test_sandhi_engine.py - what the engine already proves (ordering, refusals, options, provenance) with the derivations the tradition uses to argue about order.
 4. NORTH_STAR.md sections 3 (the five rules) and 5 (standing decisions): derive, do not tabulate; genuine tests that CAN fail; be transparent about what is not done; every claim traceable to a source on disk.
 5. The project modules that already codify individual sutras as questions - src/astadhyayi/anga.py (yan_sandhi, akah_savarne_dirghah, ato_gune, ayadi, coh_kuh, jhalam_jas_jhasi, khari_ca, sasajuso_ruh, kharavasanayoh, cerebral_n, ...), adesa.py (antaratama, guna_of, vrddhi_of), varna.py, sivasutra.py, pragrhya.py, reading.py, asiddha.py, vipratisedha.py. Where a sutra is already codified there, CALL it (a notion another rule already decides is asked, not redecided); where it is not, derive from these primitives.

NON-NEGOTIABLE RULES
 * Never write a sutra's words or number from memory: the number of every sutra you cite must be verified against corpus.load_vidyut_sutrapatha(), and the trace prints the sutra's own words from the corpus. Reasons in 'overrides' must QUOTE the tradition verbatim from the on-disk commentaries (corpus.commentary_on(id, 'kashika'|'kaumudi'|'balamanorama'|'tattvabodhini'|'bhashya'|...)); check that the quote really is in the source.
 * Never type a class of sounds or a pairing (i->y, c->k, t->c...): use supports.members / is_member / nearest, sivasutra.resolve, varna.VARGA, adesa.*. Two repository tests read every source file and fail otherwise (test_astadhyayi_no_restating, and the guna-literal scan in test_astadhyayi_adesa).
 * The engine acts at JUNCTIONS and at sounds a step of this derivation has made; the insides of the input words are finished words. Iterate v.pairs()/v.junctions()/v.vowel_pairs() for two-sound rules; scan v.live + v.pada_final(s)/v.at_pause(s) for a single pada-final sound. Never rewrite the interior of an input word (gacchati must stay gacchati).
 * Ask the View, never the State. Use the builders in rule.py so Edit.hidden is recorded.
 * A rule that REFUSES another (a pratisedha) is an Application with edits=() and the SAME site as the rule it refuses, wins by overrides=... (see 8.4.44 in hal_assimilation.py). A prakrtibhava rule on vowels uses remark(sight, PRAKRTYA).
 * A rule whose own wording names the PRODUCT of a tripadi rule (or a loss) lists the mark in consumes= (see 6.1.113 and 6.3.111 in visarga_ru.py). That is an exception to 8.2.1, so it is explicit and per rule.
 * Where a sutra's operation depends on something the letters cannot say (dual, vocative, particle, preverb, root, Vedic), read it from the word's flags (v.word(sight).has('nipata'), v.flags(sight)); say so in the docstring; never guess. Meaning is the caller's, NORTH_STAR section 5.
 * A final visarga in the INPUT is read by the parser as the s it came from (8.2.66), unless the word carries the flag final:r; the parser records that as an assumption. Rules therefore start from s or r, never from an input visarga.
 * Options (vibhasa) pass optional='<the sutra's own word>' on the Application: the engine forks and returns both courses. Say which kind of vibhasa it is (aprapta or prapta - 1.3.43 against 1.3.50) in the reason if the commentary does.
 * Vartikas are not Panini: @rule(base_sutra, authority=VARTTIKA, varttika='<the vartika verbatim from corpus.varttikas_on or the commentary>').
 * Family tags for overrides: every vowel-junction rule carries families containing 'ac'; ekadesa rules also 'ekadesa'; consonant rules 'hal'; the ru/visarga rules 'visarga'; the nasal rules 'nasal'; prakrtibhava rules 'prakrtibhava'. A rule may override a whole group with target '@ac' etc. Use the same tags so other families' rules and yours interlock.
 * Explanations: English with Sanskrit terms in braces or sk('...') so the trace prints both scripts. Say what THIS form did.
 * Each family module must define COVERAGE = ((sutra_id, status, note), ...) with status in rule/partial/support/scope/vedic covering EVERY sutra id in your scope; 'scope' and 'partial' need a real reason (the note). rulebook.problems() checks this and must return []. Do not claim to cover a sutra you have not implemented; a sutra you decide not to implement (Vedic-only, accent-only, needs semantics no flag can carry, purely lexical list) gets status 'scope' with the reason, the way the project marks deliberate limits.

PERSISTENCE. The machine can restart at any time and everything under /tmp is then lost. Keep ALL work inside your workspace directory (under /workspaces), never only in /tmp or a scratch directory; if you write helper scripts, put them in your workspace too. Your workspace is what will be merged.

HOW TO WORK
 A. For each sutra in your scope, in order: read its text, the Kasika, the Kaumudi, the Balamanorama and Tattvabodhini, the vartikas (corpus.varttikas_on) and, for ordering arguments, the Bhashya. Find its conditions, its exceptions (nisedha), what it is an apavada of / overridden by, and the examples AND counter-examples ('X iti kim?') the commentaries give. Check the Laghusiddhantakaumudi lines named below.
 B. Implement the rule. Then write tests in ${f.testfile}: (1) each commentary example, with its source named in the test docstring and (2) each counter-example, and (3) for a rule that could give the right result by luck, an assertion on the STEPS (sutra ids in order). Every test must be capable of failing (NORTH_STAR: a test that cannot fail is worse than no test). Tests may use the whole rulebook (nothing else is changing in your workspace) but assertions must be about your own rules' steps and results.
 C. If ${DATA}/${f.id}.catalogue.json and ${f.id}.gold.json exist when you start (an extraction is running in parallel and may not have finished), read them for orientation ONLY - they are unverified until audited. Do not wait for them.
 D. Before you finish, ALL of these must pass, from your workspace root:
      python3 -m unittest ${f.testmodule} tests.test_sandhi_engine
      python3 -m unittest tests.test_astadhyayi_no_restating tests.test_astadhyayi_adesa tests.test_astadhyayi_reuse
      python3 -c "import sys; sys.path.insert(0,'.'); from src.astadhyayi.sandhi import rulebook; print(rulebook.problems())"     # must print []
    and the 'termination' test in tests.test_sandhi_engine (every meeting of two sounds terminates, cites real sutras) must still pass with your rules loaded. Keep the engine fast: a sandhi() call must stay in the millisecond range.
 E. Be transparent: where the grammar is contested or the commentaries disagree, implement the reading the Kasika and Kaumudi share, note the alternative in the docstring as an OPEN or SCOPE note, and list it in 'open_questions'.
`

const FAMILIES = [
  { id: 'ac_yan_ayadi',
    files: `src/astadhyayi/sandhi/families/ac_yan_ayadi.py (exists with 6.1.77 and 6.1.78; you own and extend it)
tests/test_sandhi_ac_yan_ayadi.py (new)`,
    testfile: 'tests/test_sandhi_ac_yan_ayadi.py', testmodule: 'tests.test_sandhi_ac_yan_ayadi',
    title: 'yan, ayavayav, vanta, doubling and the consonant adjustments that go with them',
    laghu: `Laghusiddhantakaumudi text file (reference/mula/ancillary/gretil-laghusiddhantakaumudi.txt) lines 80-99 and 168-169: iko yanaci with 1.1.66/1.1.50, anaci ca, jhalam jas jhasi, samyoganta-lopa with the vartika yanah pratisedho vacyah, alo ntyasya, eco yavayavah with 1.3.10, vanto yi pratyaye.`,
    scope: `Sutra ids: 6.1.77-6.1.83; 8.4.46-8.4.54; 8.4.64; 8.2.23; 8.2.29; and the supports 1.1.9, 1.1.10, 1.1.50, 1.1.51, 1.1.52, 1.1.66, 1.1.67, 1.1.69, 1.1.70, 1.3.10 (a support is cited through supports.py Vias; add any missing Via helper inside YOUR module).
MUST REPRODUCE, derived step by step with the sutras the Laghu names: sudhi upasya -> suddhyupasya (6.1.77, then the optional doubling of 8.4.47, then 8.4.53, with the vartika yanah pratisedho vacyah refusing 8.2.23 - decide how to model the vartika as a refusal), madhu ari -> maddhari, the r-varna and l-varna examples (dhatr amsah? lr akrtih -> lakrtih - read the exact words in the Laghu text), the ayavayav examples (hare, visnave, nayakah, pavakah - as ne~a-type inputs with an anga boundary such as nai~aka), gavyam / navyam / gavyutih for 6.1.79 with its vartika. Doubling is OPTIONAL and the three teachers (8.4.50 Sakatayana, 8.4.51 Sakalya, 8.4.52 the acaryas) narrow it: decide and DOCUMENT how the engine treats them (the union of what any teacher allows is the natural reading; say so). 8.4.54 abhyase car and other reduplication-only rules are SCOPE (the engine does not derive reduplication) unless a junction case exists.` },
  { id: 'ac_ekadesa',
    files: `src/astadhyayi/sandhi/families/ac_ekadesa.py (exists with 6.1.87, 6.1.88, 6.1.101, 6.1.109; you own and extend it)
tests/test_sandhi_ac_ekadesa.py (new)`,
    testfile: 'tests/test_sandhi_ac_ekadesa.py', testmodule: 'tests.test_sandhi_ac_ekadesa',
    title: 'guna, vrddhi, dirgha, purvarupa, pararupa and the ekadesa machinery',
    laghu: `Laghusiddhantakaumudi text file lines 100-137 and 132-137: ad gunah, vrddhir eci, ety-edhaty-uthsu (with its vartikas aksad uhinyam, prad uhodhodhyesaisyesu, rte ca trtiyasamase, pravatsatara...), upasargad rti dhatau, eni pararupam, omanos ca, antadivac ca, akah savarne dirghah, engah padantad ati.`,
    scope: `Sutra ids: 6.1.84 to 6.1.112 (every one; 6.1.84-6.1.86 are the governing heading and two paribhasas already cited through supports - record them as support/scope as fits) and the supports 1.1.1, 1.1.2, 1.1.3, 1.1.53-1.1.64. MUST HANDLE the chain of exceptions the Kasika describes (purastad apavada anantaran vidhin badhante nottaran) so each of these gives the received form: khatva+indrah, ganga+udakam, krsna+aikyam, upa+eti (upaiti), upa+edhate, pra+rcchati (prarcchati via 6.1.91), pra+ejate (prejate via 6.1.94), upa+osati (uposati), siva+om, siva+ehi (with 6.1.95 and 6.1.85), dandagram, dadhindrah, madhudake, hotr+rkarah (with the vartika rti savarne r va), hare+ava (6.1.109), the vartikas on 6.1.89, and pacanti (6.1.97 ato gune, the exception to 6.1.101 - needs the input pac~anti with an anga boundary so 6.1.97 is not padanta). The conditions the letters cannot carry (that a word is an upasarga, that it is a dhatu whose root begins with e/o, that it is the particle om or the preverb ang) come from word flags and boundary kinds - see the flag vocabulary in the README (upasarga, dhatu:ROOT, ang, nipata) and the boundary kind UPASARGA, and say how each rule reads them. Where two apavada rules stand in a chain, express each relation with overrides carrying the Kasika quote.` },
  { id: 'prakrtibhava',
    files: `src/astadhyayi/sandhi/families/prakrtibhava.py (new)
src/astadhyayi/sandhi/infer.py (exists as a stub; you own it)
tests/test_sandhi_prakrtibhava.py (new)`,
    testfile: 'tests/test_sandhi_prakrtibhava.py', testmodule: 'tests.test_sandhi_prakrtibhava',
    title: 'pragrhya, prakrtibhava and the sounds that refuse sandhi',
    laghu: `Laghusiddhantakaumudi text file lines 138-171: sarvatra vibhasa goh, avan sphotayanasya, indre ca, dur ad dhute ca, plutapragrhya aci nityam, idudeddvivacanam pragrhyam, adaso mat, cadayo satve, pradayah, nipata ekajanan, ot, sambuddhau sakalyasyetav anarse, maya uno vo va, iko savarne sakalyasya hrasvas ca, rty akah.`,
    scope: `Sutra ids: 1.1.11 to 1.1.19; 1.4.56 to 1.4.60; 6.1.115 to 6.1.131; 8.2.82 to 8.2.107; 8.3.33; 8.4.57. The pragrhya predicate ALREADY EXISTS: src/astadhyayi/pragrhya.py pragrhya(form, dvivacana=..., nipata=..., ang=..., sambuddhi=..., before_iti=..., arsa=..., saptami_artha=..., stem=...) returns which sutra of 1.1.11-19 gives the name - CALL IT from your 6.1.125 rule (plutapragrhya aci nityam), passing the word flags, and cite the sutra it returns in via. The rule keeps the vowel by remark(sight, PRAKRTYA) (see rule.py and segs.View.vowel_pairs which then excludes it), so that every rule of vowel sandhi leaves it alone - and it must win against ALL of them (overrides target '@ac'). Test with hari etau (flag dvivacana on the first word, the final vowel long i), amI isah (adas), the particle i indrah / u umesah, aho isah, ang vs bare a (a evam nu manyase versus a udakantat -> odakantat), vayo iti / vayaviti (an option), and the counter-examples. ALSO write src/astadhyayi/sandhi/infer.py: infer_flags() fills in ONLY what a closed class proves - a word in the cadi or pradi ganas is a nipata (read the word lists with corpus.ganas_for / in_gana on 1.4.57 and 1.4.58 from the ganapatha, never type them), a first word before a dhatu with boundary upasarga is an upasarga - and returns (flag, reason) so the trace can show the assumption; never infer what depends on meaning (dual, vocative, locative sense). infer_flags must ALSO return the flag final:r (with the reason) for a word whose text ends in a visarga when the same word with a final r is in the closed class of r-final indeclinables (the svaradi gana, 1.1.37 svaradinipatam avyayam: svar, antar, prator, punar, ... read from the ganapatha through corpus, never typed) - see parse._read_visarga, which reads any final visarga as s unless the word carries final:r. The go-rules 6.1.122-6.1.124, 6.1.127 (iko savarne sakalyasya hrasvas ca), 6.1.128 (rty akah), 8.3.33 (maya uno vo va) are all in your scope. Pluta/accent-only rules of 8.2.82-8.2.107 are SCOPE where they concern accent or the vocative call, with the reason.` },
  { id: 'hal_assimilation',
    files: `src/astadhyayi/sandhi/families/hal_assimilation.py (exists with 8.2.30, 8.2.39, 8.4.40, 8.4.44, 8.4.55; you own and extend it)
tests/test_sandhi_hal_assimilation.py (new)`,
    testfile: 'tests/test_sandhi_hal_assimilation.py', testmodule: 'tests.test_sandhi_hal_assimilation',
    title: 'consonant assimilation: scutva, stutva, jastva, cartva, tuk and friends',
    laghu: `Laghusiddhantakaumudi text file lines 176-205 and 254-257: stoh scuna scuh, sat, stuna stuh, na padantat toranam, toh si, jhalam jaso nte, torli, jharo jhari savarne, khari ca, jhayo ho nyatarasyam, sas cho ti (and the vartika chatvam amiti vacyam), che ca, padantad va. (The Laghu mis-tags udah sthastambhoh purvasya as 8.4.41; it is 8.4.61 - verify every tag against the Vidyut text.)`,
    scope: `Sutra ids: 6.1.71 to 6.1.76; 8.2.24 to 8.2.41; 8.4.40 to 8.4.44; 8.4.55; 8.4.56; 8.4.60 to 8.4.63; 8.4.65 to 8.4.68. The skeleton has 8.2.30, 8.2.39, 8.4.40, 8.4.44, 8.4.55 - read them critically: complete and correct them (8.4.40 is stated for a s or tavarga sound in yoga with s-sound or cavarga sound from either side, and the Kasika says the pairs are NOT matched one to one; 8.4.41 is the retroflex counterpart with its refusals 8.4.42 na padantat torana and 8.4.43 toh si). Add 8.2.31 ho dhah, 8.2.36-8.2.38, 8.2.40, 8.2.41 as the commentaries teach, 8.4.56 va avasane (an option at a pause), 8.4.62, 8.4.63 (+ the vartika), 8.4.65 (an option), 8.4.60, 8.4.61, and the tuk augment rules 6.1.71-6.1.76 (che ca is nitya for a short vowel, dirghat and padantad va differ - get the nitya/optional structure right, and note that tuk is an AGAMA: use insert_after and remember an inserted sound has no predecessor). MUST REPRODUCE: vakpati (8.2.30, 8.2.39, 8.4.55 in that order), vagisah, tacchivah / tacsivah (8.4.40, 8.4.55, 8.4.63 option), tallayah, ramas sete (with the visarga family), sivacchaya, laksmicchaya / laksmi chaya, udgacchati... Anything in these sutras that concerns accent or reduplication only is SCOPE. NOTE 8.2.30 must not fire inside gacchati (interior of a finished word; see the README on pairs()).` },
  { id: 'nasal_anusvara',
    files: `src/astadhyayi/sandhi/families/nasal_anusvara.py (new)
tests/test_sandhi_nasal_anusvara.py (new)`,
    testfile: 'tests/test_sandhi_nasal_anusvara.py', testmodule: 'tests.test_sandhi_nasal_anusvara',
    title: 'nasals, anusvara, parasavarna and the augments nut/tuk/dhut',
    laghu: `Laghusiddhantakaumudi text file lines 188-201 and 206-237: yaro nunasike nunasiko va (and the vartika pratyaye bhasayam nityam), mo nusvarah, nas capadantasya jhali, anusvarasya yayi parasavarnah, va padantasya, mo raji samah kvau, he mapare va, napare nah, adyantau takitau, ngnoh kuktuk sari, dah si dhut, nas ca, si tuk, ngamo hrasvad aci ngamun nityam, samah suti, atranunasikah purvasya tu va, anunasikat paro nusvarah, pumah khayy ampare, nas chavy apra san.`,
    scope: `Sutra ids: 8.3.1 to 8.3.7; 8.3.23 to 8.3.33 (8.3.34 belongs to the visarga family - do not implement it); 8.4.45; 8.4.58; 8.4.59; supports 1.1.46, 1.1.47. MUST REPRODUCE: harim vande (8.3.23), yasamsi / akramsyate (8.3.24 for a non-final n or m - as inputs with an anga boundary), santah, tvankarosi / tvam karosi (8.4.58 and the optional 8.4.59), samrat (8.3.25), kim hmalayati variants (8.3.26-27), pranksasthah forms (8.3.28 with the tuk/kuk augments), sant sah / sansah (8.3.29-30), sancchambhuh forms (8.3.31), pratyannatma / sugannisah / sannacyutah (8.3.32 nam-ut: an augment after a SHORT vowel + ng/n/n-final pada before a vowel), samskarta and pumskokilah (8.3.2, 8.3.4, 8.3.5, 8.3.6 - the ru that becomes visarga or anusvara). NOTE the rutva 8.2.66 that produces the ru and 8.3.15 that makes it a visarga belong to the visarga family (their skeleton is in visarga_ru.py, which the visarga implementer is extending in parallel in its own workspace): your rules must be written to interlock with them - e.g. 8.3.5 samah suti has sam + sut where the s of the sut augment is the next junction; 8.3.2 makes the sound before a ru optionally nasal, and 8.3.4 supplies the anusvara. Where the correct derivation needs a rule of the other family that is not yet there, test the STEPS your rules take and leave the end-to-end result to the integration tests, saying so in the test docstring. For nasal sounds use the anunasika mark (segs.ANUNASIKA) on the plain sound, and the anusvara as the sound with the dot below (the project's ANUSVARA); the nearest nasal is chosen with supports.nearest / varna, never a table.` },
  { id: 'visarga_ru',
    files: `src/astadhyayi/sandhi/families/visarga_ru.py (exists with 9 skeleton rules; you own and extend it)
tests/test_sandhi_visarga_ru.py (new)`,
    testfile: 'tests/test_sandhi_visarga_ru.py', testmodule: 'tests.test_sandhi_visarga_ru',
    title: 'visarga, ru-rutva, utva and the s/r-final padas',
    laghu: `Laghusiddhantakaumudi text file lines 238-289 (visarga chapter) and 100-113: kharavasanayor visarjaniyah, visarjaniyasya sah, va sari, sasajuso ruh, ato ror aplutad aplute, hasi ca, bho bhago agho apurvasya yo si, hali sarvesam, ro supi, ro ri, dhralope purvasya dirgho nah, vipratisedhe param karyam, etat-tadoh sulopo koranan samase hali, so ci lope cet padapuranam, nrn pe, kupvoh ...ka...pau ca, kanamredite, lopah sakalyasya.`,
    scope: `Sutra ids: 8.2.62 to 8.2.81; 8.3.8 to 8.3.22; 8.3.34 to 8.3.54; 6.1.113; 6.1.114; 6.3.111; 6.1.132 to 6.1.135. The skeleton has 8.2.66, 6.1.113, 6.1.114, 8.3.14, 8.3.15, 8.3.17, 8.3.19 (y and v after a or a-long, no 8.3.18 variant), 8.3.34 (WITHOUT its exceptions), 6.3.111 - read them critically, complete and correct them. Add: 8.3.35 sarpare visarjaniyah, 8.3.36 va sari (an option), 8.3.37 kupvoh ..ka..pau ca (jihvamuliya/upadhmaniya and the option), 8.3.10 nrn pe and its neighbours 8.3.8-8.3.13 (the ru before certain particles and the dhralopa-nimitta 8.3.13 ho dhe lopah), 8.3.16, 8.3.18, 8.3.20-8.3.22 (Sakatayana, Gargya, hali sarvesam), 8.2.68-8.2.71 (ahan, and the Vedic options -> vedic status), 8.3.38-8.3.54 (the s/s-visarga rules: so padadau, inah sah, namaspurasor gatyoh, idudupadhasya capratyayasya, tiraso nyatarasyam, dvistriscatur iti krtvo rthe, isusoh samarthye, nityam samase nuttarapadasthasya, ataah krkamikamsa...): several depend on lexical classes (kr, kami, kamsa, kumbha... the kaskadi gana) - read them from the ganapatha (corpus.ganas_for) and implement or mark SCOPE with the reason - and on the word being a compound or an upasarga (word flags / boundary kinds), 6.1.132-6.1.135 (the su-lopa of etad/tad: stem flags). The tripadi/sapadasaptadhyayi interplay is the heart of this family: 8.2.66 is tripadi, 6.1.113/114 sapada and CONSUME its ru; 8.3.14 competes with 6.1.114 for the ru and LOSES by 8.2.1 (manoratha); 6.3.111 names the loss of 8.3.13/14; 8.2.66 overrides 8.2.39 for a pada-final s. Underlying finals: the INPUT gives s or r; a visarga in the input is read as coming from s (the parser says so) unless the word has the flag final:r. MUST REPRODUCE each Laghu example: ramas ca -> ramasca (8.2.66, 8.3.15, 8.3.34, 8.4.40), vrksas tarati, harih sete / hariss sete (8.3.36 option), sivo rcyah, sivo vandyah, deva iha / devayiha, bho deva, bhago namaste, agho yahi, aharahah / ahargana (8.2.69), puna ramate, hari ramyah, sambhu rajate, manoratha, esa visnuh / sa sambhuh (6.1.132) versus esa tra, the so ci lope forms (6.1.134), the s-augment cases. NOTE 8.4.40 (scutva) belongs to the hal family, which is extending it in parallel in its own workspace: your tests should assert your rules' steps (8.2.66, 8.3.15, 8.3.34 ...) and, for end-to-end results that need 8.4.40, use the baseline one you have.` },
]

const ONLY = ['ac_yan_ayadi', 'ac_ekadesa']
const DRAFTS = {'ac_yan_ayadi': 'src/astadhyayi/sandhi/families/ac_yan_ayadi.py (about 54 KB) and tests/test_sandhi_ac_yan_ayadi.py (about 56 KB, 122 tests) already exist in your workspace: they were written by an EARLIER agent that was interrupted mid-work. When last run, 65 of the 122 tests failed or errored. Treat them as a DRAFT to be continued: run the tests, read the failures, and for each decide whether the module or the test is wrong (check against the commentary, not against convenience); finish any sutra in scope the draft omits; keep every convention of the README. Do not throw the draft away, and do not weaken a test to make it pass.', 'ac_ekadesa': "src/astadhyayi/sandhi/families/ac_ekadesa.py (about 40 KB) and tests/test_sandhi_ac_ekadesa.py (about 74 KB) already exist in your workspace: they were written by an EARLIER agent that was interrupted mid-work. The module currently FAILS AT IMPORT (its helper _varttika looks up vartikas by a needle that carries a trailing virama the corpus text does not: the corpus reads '...न्यामुपसंख्यानम्'), which breaks the whole engine until fixed - fix that first. Treat the rest as a DRAFT to be continued: run the tests, read the failures, decide for each whether the module or the test is wrong (check against the commentary), finish any sutra in scope the draft omits, keep every convention of the README. Do not throw the draft away, and do not weaken a test to make it pass.", 'natva': 'src/astadhyayi/sandhi/families/natva.py (about 27 KB) already exists in your workspace: it was written by an EARLIER agent that was interrupted before it wrote any tests. Treat it as a DRAFT: read it critically against the sources, write tests/test_sandhi_natva.py, run everything, fix what fails, complete what is missing. It may not yet import or pass; do not throw it away, do not weaken a test to make it pass.', 'satva': 'src/astadhyayi/sandhi/families/satva.py (about 37 KB) already exists in your workspace: it was written by an EARLIER agent that was interrupted before it wrote any tests. Treat it as a DRAFT: read it critically against the sources, write tests/test_sandhi_satva.py, run everything, fix what fails, complete what is missing. It may not yet import or pass; do not throw it away, do not weaken a test to make it pass.'}
const SELECTED = FAMILIES.filter((f) => ONLY.includes(f.id))

const IMPL_SCHEMA = {
  type: 'object',
  properties: {
    family: { type: 'string' },
    workspace: { type: 'string' },
    files: { type: 'array', items: { type: 'string' } },
    n_rules: { type: 'number' },
    n_tests: { type: 'number' },
    tests_green: { type: 'boolean' },
    coverage_summary: { type: 'string' },
    scope_notes: { type: 'array', items: { type: 'string' } },
    core_requests: { type: 'array', items: { type: 'string' } },
    open_questions: { type: 'array', items: { type: 'string' } },
  },
  required: ['family', 'workspace', 'files', 'n_rules', 'n_tests', 'tests_green', 'coverage_summary', 'scope_notes', 'core_requests', 'open_questions'],
}

const REVIEW_SCHEMA = {
  type: 'object',
  properties: {
    family: { type: 'string' },
    tests_green: { type: 'boolean' },
    adversarial_cases_tried: { type: 'number' },
    defects_found: { type: 'number' },
    defects_fixed: { type: 'number' },
    remaining_defects: { type: 'array', items: { type: 'string' } },
    citation_errors_found: { type: 'number' },
    core_requests: { type: 'array', items: { type: 'string' } },
    verdict: { type: 'string' },
  },
  required: ['family', 'tests_green', 'adversarial_cases_tried', 'defects_found', 'defects_fixed', 'remaining_defects', 'citation_errors_found', 'core_requests', 'verdict'],
}

function implPrompt(f) {
  return PREAMBLE(f) + `
YOUR FAMILY: "${f.id}" - ${f.title}
LAGHU: ${f.laghu}
SCOPE: ${f.scope}

${DRAFTS[f.id] ? 'DRAFT ALREADY PRESENT: ' + DRAFTS[f.id] + '\n\n' : ''}${'CONTINUING. Your workspace may already hold substantial work from earlier attempts that were interrupted (a family module and, where present, its tests). Before writing anything, look: compare your family module with the skeleton in the repository and read any tests file. If work exists, CONTINUE it: run its tests, decide for every failure whether the module or the test is wrong (check the commentary, not convenience), finish what is missing, and never weaken a test to make it pass or throw the draft away. If not, start fresh. Save progress in your workspace as you go - you may be interrupted again and a later agent will resume from what is on disk.'}\n\nDeliver: the family module with EVERY sutra in scope implemented or honestly marked in COVERAGE; ${f.testfile} with genuine tests; all of step D passing. Then reply with the structured summary (workspace path, files, counts, coverage summary, scope notes, core_requests, open_questions).`
}

function reviewPrompt(f, done) {
  return `
You are an INDEPENDENT ADVERSARIAL REVIEWER. Another agent has implemented the sandhi-rule family "${f.id}" (${f.title}) for a PANINIAN SANDHI ENGINE. Its workspace is ${WSROOT}/${f.id} (an isolated copy of the repo at ${REAL}); its self-report:
${JSON.stringify(done)}

Work in that workspace only; do NOT touch the real repository. You may edit ONLY these files (the family module, its tests${f.id === 'prakrtibhava' ? ', and infer.py' : ''}): src/astadhyayi/sandhi/families/${f.id}.py, ${f.testfile}${f.id === 'prakrtibhava' ? ', src/astadhyayi/sandhi/infer.py' : ''}.
Read src/astadhyayi/sandhi/README.md first (the conventions), then the family module, its tests, and the core it uses. Assume the implementation contains mistakes: it was written from commentary in one pass. Your job is to find them and fix them.

1. SOURCES, INDEPENDENTLY. For every sutra in the family scope, read the sutra text, Kasika, Kaumudi, Balamanorama, Tattvabodhini, the vartikas and the Bhashya yourself (corpus.commentary_on(id, name), corpus.varttikas_on(id)) and write down what the rule requires, excepts, and competes with - BEFORE reading how the module does it. Then compare. The scope was: ${f.scope}
   The Laghusiddhantakaumudi lines for this family: ${f.laghu}
2. ADVERSARIAL CASES. Write at least 40 test inputs you believe the grammar decides (from the commentaries' examples AND counter-examples first, then inputs of your own: every sound meeting the family's sounds, both sides of every condition, options, the exceptions). Work out by hand, from the sutras, what the correct result and derivation are; then run the engine (python3 -m src.astadhyayi.sandhi "..." prints the trace) and compare RESULT and STEPS. Any disagreement is a defect until you have shown from the sources that your hand derivation was wrong.
3. CITATIONS. For each rule: is the sutra number right (corpus.load_vidyut_sutrapatha()[id].text matches the rule's name)? Is each 'overrides' reason a verbatim quotation of the named commentary (search the on-disk text)? Does each Via cite a sutra that really plays the role stated? Is anything asserted about a sutra that the sources do not say? Fix every error.
4. HONESTY. Does COVERAGE tell the truth? A sutra marked 'rule' must be fully implemented; anything narrowed is 'partial' with the reason; deliberate omissions are 'scope' with a real reason. Is any class of sounds or any pairing typed rather than derived (the repository guards catch some, not all)? Does any rule rewrite the interior of an input word? Does any rule fire where a counter-example says it must not?
5. FIX what you find, in the files you may edit, and add a test for every defect fixed (the test must fail without the fix). Re-run: python3 -m unittest ${f.testmodule} tests.test_sandhi_engine tests.test_astadhyayi_no_restating tests.test_astadhyayi_adesa tests.test_astadhyayi_reuse and rulebook.problems() (must be []). If a defect needs a core change, do not make it; describe it exactly in core_requests.
6. Reply with the structured summary. Be honest: a reviewer who finds nothing has usually not looked hard enough, and remaining_defects must list everything you could not fix.`
}

phase('Implement')
const results = await pipeline(
  SELECTED,
  (f) => agent(implPrompt(f), { label: 'implement:' + f.id, phase: 'Implement', schema: IMPL_SCHEMA, effort: 'xhigh' }),
)
return results.filter(Boolean)
