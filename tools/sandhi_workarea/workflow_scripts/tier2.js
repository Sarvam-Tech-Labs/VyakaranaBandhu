export const meta = {
  name: 'sandhi-tier2-continue',
  description: 'Continue the recovered drafts of natva and satva, then review each adversarially',
  phases: [
    { title: 'Implement', detail: 'natva and satva, each in its own workspace copy of the repo' },
    { title: 'Review', detail: 'an independent adversarial reviewer for each' },
  ],
}

const REAL = '/workspaces/codespaces-blank/VyakaranaBandhu'
const WSROOT = '/workspaces/codespaces-blank/sandhi_work/ws'

const PREAMBLE = (f) => `
You are implementing ONE FAMILY of rules for a PANINIAN SANDHI ENGINE: given words (or word pieces) it derives the junction step by step, citing for EVERY step the exact sutra of Panini that applies, saying what is replaced by what and why. The engine core exists and is tested; your job is the rules of one family - the cerebralisation rules, which turn a dental n or s into a cerebral n or s after certain sounds (rama + ena -> ramena with n-dot-below; agni + su -> agnisu with s-dot-below).

YOUR WORKSPACE - an isolated copy of the repository at ${WSROOT}/${f.id}. Work ONLY there: cd into it, run everything from its root (python3 -m unittest ...). The real repository (${REAL}) is off limits; other agents are working in their own copies at the same time (six other families of sandhi rules are being written in parallel), and your files will be merged from your workspace when you finish.

FILES YOU MAY CREATE OR MODIFY (and no others):
${f.files}
Do NOT modify any other file - in particular NOT the core (src/astadhyayi/sandhi/segs.py, rule.py, engine.py, supports.py, parse.py, trace.py, rulebook.py, harness.py, __init__.py, __main__.py) and NOT other families. If the core lacks something you need, work around it with local helpers inside your family file and record it in 'core_requests' in your final report.

READ FIRST, in this order:
 1. ${WSROOT}/${f.id}/src/astadhyayi/sandhi/README.md  - THE SPECIFICATION. Its 'Writing a rule' section lists conventions that each cost a failure. Follow every one.
 2. The core: segs.py, rule.py, engine.py, supports.py, parse.py, trace.py (all under src/astadhyayi/sandhi/), and the skeleton families in src/astadhyayi/sandhi/families/ - they are the PATTERN: ac_ekadesa.py and visarga_ru.py especially.
 3. tests/test_sandhi_engine.py - what the engine already proves (ordering, refusals, options, provenance, units).
 4. NORTH_STAR.md sections 3 (the five rules) and 5 (standing decisions): derive, do not tabulate; genuine tests that CAN fail; be transparent about what is not done; every claim traceable to a source on disk.
 5. The project modules that already codify sutras of your family as QUESTIONS: ${f.modules}. Where a sutra is already codified there, CALL it (a notion another rule already decides is asked, not redecided); where not, derive from the primitives (sivasutra.resolve, varna, adesa).

WHERE YOUR FAMILY DIFFERS FROM THE JUNCTION RULES. The engine normally acts only at junctions between words and at sounds a step of this derivation has made: the inside of an input word is a FINISHED word and is left alone. Cerebralisation is the exception: its sthanin (the n or s of an affix or root) is INTERIOR to a piece, and its cause (an r, s-dot, i, u...) may be several sounds away, within one pada. So your rules look across the pieces joined by an ANGA boundary (or, where the sutra says so, an UPASARGA or SAMASA boundary): use View.unit_of(sight, across=(ANGA,)) and View.joined_pada(sight, across=...) - see their docstrings and tests - and NEVER rewrite the inside of a single finished piece (a word with no such join): 'arjuna' and 'gacchati' must stay as they are. The pieces the caller gives are unprocessed morphemes in the sense that matters here (stem, affix, root); how the caller says which is an affix, a substitute, a root or a compound member is by word FLAGS (see the vocabulary in the README; add to your tests the flags you rely on, and say in the docstring exactly which flag each rule reads - suggested names: pratyaya (an affix), adesa (a substitute), krt, taddhita, upasarga, dhatu:ROOT, and the boundary kinds ANGA / SAMASA / UPASARGA). Position in the tripadi matters: 8.2.1 makes each rule asiddha to the ones before it - the engine does this for you through the View, but check your rules against what stands before and after them (satva 8.3.55-119 stands before natva 8.4.1-39, so a ṣ that satva makes can cause natva; scutva 8.4.40 stands after both).

NON-NEGOTIABLE RULES
 * Never write a sutra's words or number from memory: the number of every sutra you cite must be verified against corpus.load_vidyut_sutrapatha(), and the trace prints the sutra's own words from the corpus. Reasons in 'overrides' must QUOTE the tradition verbatim from the on-disk commentaries (corpus.commentary_on(id, 'kashika'|'kaumudi'|'balamanorama'|'tattvabodhini'|'bhashya'|...)); check that the quote really is in the source.
 * Never type a class of sounds or a pairing (n -> n-dot-below...): use supports.members / is_member / nearest, sivasutra.resolve, varna.VARGA, adesa.*. Two repository tests read every source file and fail otherwise (test_astadhyayi_no_restating, and the guna-literal scan in test_astadhyayi_adesa). Lexical lists (roots, words a sutra names) come from the corpus - the dhatupatha (corpus.load_dhatupatha), the ganapatha (corpus.ganas_for) - or are marked SCOPE; never retyped where they exist on disk. A list the sutra itself spells out as its own words (the sutra names the words) may be written in your module ONCE.
 * Ask the View, never the State. Use the builders in rule.py so Edit.hidden is recorded.
 * A rule that REFUSES another (a pratisedha) is an Application with edits=() and the SAME site as the rule it refuses, wins by overrides=... (see 8.4.44 in hal_assimilation.py).
 * Where a sutra depends on something the letters cannot say (which piece is an affix, that a root is nopadesa, that a word is a name), read it from the word's flags or the boundary kind; say so in the docstring; never guess. Meaning is the caller's, NORTH_STAR section 5.
 * Options (vibhasa) pass optional='<the sutra's own word>' on the Application: the engine forks and returns both courses.
 * Vartikas are not Panini: @rule(base_sutra, authority=VARTTIKA, varttika='<the vartika verbatim from corpus.varttikas_on or the commentary>').
 * Family tags: consonant rules carry families containing 'hal'; give yours also '${f.tag}'. A rule may override a group with target '@${f.tag}'.
 * Explanations: English with Sanskrit terms in braces or sk('...') so the trace prints both scripts. Say what THIS form did.
 * Your module must define COVERAGE = ((sutra_id, status, note), ...) with status in rule/partial/support/scope/vedic covering EVERY sutra id in your scope; 'scope' and 'partial' need a real reason. rulebook.problems() checks this and must return []. Do not claim to cover a sutra you have not implemented; a sutra you decide not to implement (purely lexical, Vedic-only, needs meaning no flag can carry) gets status 'scope' with the reason.

PERSISTENCE. The machine can restart at any time and everything under /tmp is then lost. Keep ALL work inside your workspace directory (under /workspaces), never only in /tmp or a scratch directory; if you write helper scripts, put them in your workspace too. Your workspace is what will be merged.

HOW TO WORK
 A. For each sutra in your scope, in order: read its text, the Kasika, the Kaumudi, the Balamanorama and Tattvabodhini, the vartikas (corpus.varttikas_on) and, for ordering arguments, the Bhashya. Find its conditions, exceptions, what it is an apavada of / overridden by, and the examples AND counter-examples ('X iti kim?') the commentaries give.
 B. Implement the rule. Then write tests in ${f.testfile}: each commentary example (source named in the docstring), each counter-example, and, for a rule that could give the right result by luck, an assertion on the STEPS. Every test must be capable of failing. Tests may use the whole rulebook (nothing else changes in your workspace) but assertions must be about your own rules' steps and results.
 C. Before you finish, ALL of these must pass, from your workspace root:
      python3 -m unittest ${f.testmodule} tests.test_sandhi_engine
      python3 -m unittest tests.test_astadhyayi_no_restating tests.test_astadhyayi_adesa tests.test_astadhyayi_reuse
      python3 -c "import sys; sys.path.insert(0,'.'); from src.astadhyayi.sandhi import rulebook; print(rulebook.problems())"     # must print []
    and the termination test in tests.test_sandhi_engine must still pass with your rules loaded (no rule may fire in the inside of a finished word, or an input like a plain two-word junction would be rewritten). Keep the engine fast.
 D. Be transparent: where the grammar is contested or the commentaries disagree, implement the reading the Kasika and Kaumudi share, note the alternative in the docstring as an OPEN or SCOPE note, and list it in 'open_questions'.
`

const FAMILIES = [
  { id: 'natva', tag: 'natva',
    files: `src/astadhyayi/sandhi/families/natva.py (new)
tests/test_sandhi_natva.py (new)`,
    testfile: 'tests/test_sandhi_natva.py', testmodule: 'tests.test_sandhi_natva',
    modules: 'src/astadhyayi/natva.py (a provision table for 8.4.1-8.4.39 and the_cerebral_n), src/astadhyayi/anga.py (cerebral_n: 8.4.1 and 8.4.2 on a text), src/astadhyayi/murdhanya.py',
    title: 'natva: the dental n becomes cerebral after r, s-dot and r-vowel (8.4.1-8.4.39)',
    scope: `Sutra ids: 8.4.1 to 8.4.39 (all thirty-nine). Core: 8.4.1 rasabhyam no nah samanapade with 8.4.2 atkupvannumvyavaye 'pi (the n is reached across a vowel, a guttural, a labial, the preverb ang and a num - so the n of karanam is two sounds from its r), the refusals 8.4.35-8.4.38 (padantasya: a word-final n stays - vrksan, girin; the refusal after a pada-final s-dot; 8.4.38 padavyavaye: a whole word between stops it: pra gam nayamah) and the specific provisions between (compound seams in names 8.4.3, vana after named first members 8.4.4-8.4.6, ahna 8.4.7, vahana and pana 8.4.8-8.4.10, 8.4.11-8.4.13, the preverb + nopadesa root rules 8.4.14-8.4.17 (pranamati, parinamati, praniyati...), and the krt-affix n after a vowel 8.4.29-8.4.33). MUST REPRODUCE with the correct steps: rama~ena -> ramena (n-dot-below), karana forms, girina, arkena / murkhena (across ku), pra|namati -> pranamati (with the cerebral n, 8.4.14: read the root's nopadesa status from the dhatupatha: corpus.load_dhatupatha / the marks the corpus carries - it is a question of the ENUNCIATION nam, and the project's pada.py already handles the initial n/n-dot rule 6.1.65), vrksan (word-final n untouched), arjuna (cavarga intervenes: NOT changed), krsna as given (already cerebral), pra gam nayamah (a word between). The lexical provisions (the named words, the roots, the gana lists) are read from natva.py / the corpus or marked SCOPE.` },
  { id: 'satva', tag: 'satva',
    files: `src/astadhyayi/sandhi/families/satva.py (new)
tests/test_sandhi_satva.py (new)`,
    testfile: 'tests/test_sandhi_satva.py', testmodule: 'tests.test_sandhi_satva',
    modules: 'src/astadhyayi/murdhanya.py (8.3.55-8.3.89), src/astadhyayi/murdhanya_nisedha.py (8.3.90-8.3.119, the words laid down whole and the ten refusals), src/astadhyayi/anga.py',
    title: 'satva: the dental s becomes s-dot-below after i-class, u-class, r and ku (8.3.55-8.3.119)',
    scope: `Sutra ids: 8.3.55 to 8.3.119 (all sixty-five). Core: 8.3.55 apadantasya murdhanyah (the adhikara: a non-pada-final s becomes s-dot-below under the conditions that follow), 8.3.57 inkoh (after a vowel other than a, a semivowel, h or a guttural: 'ink' and 'ku'), 8.3.58 numvisarjaniyasavyavaye 'pi (reaching across a num, a visarga or a sibilant), 8.3.59 adesapratyayayoh (the s that is a SUBSTITUTE or part of an AFFIX: agnisu, vayusu, sarpisi - the caller marks the piece as an affix with the flag pratyaya or the substitute with adesa), 8.3.60 sasivasighasinam ca, 8.3.61-8.3.63, the preverb + root rules 8.3.65-8.3.72 (abhisunoti, nisidati, abhistabhnati, pariṣevate - the root is named by a dhatu:ROOT flag and the preverb by boundary UPASARGA), the compound rules 8.3.80-8.3.86 (angulisangah, bhirusthanam, agnistomah, agnisomau, jyotistomah, matrsvasa), the words laid down whole 8.3.90-8.3.109, and the ten refusals 8.3.110-8.3.119 (visrabdhah, punahsrjati, agnisat, the aorist s before yan, sedh of motion, the s of a perfect...). NOTE the visarga rules 8.3.38-8.3.54 belong to ANOTHER family (visarga_ru) - do not implement them. MUST REPRODUCE with the correct steps: agni~su -> agnisu (with the flag pratyaya), vayu~su, sarpis~i -> sarpisi, abhi|sunoti -> abhisunoti (satva, and then natva of the n after it by 8.4.1 - that natva rule is being written in a parallel workspace, so test YOUR step: 8.3.65 gives the s-dot-below; leave the end-to-end result to integration and say so in the test docstring), ni|sidati -> nisidati, pari|sevate, and the counter-examples the Kasika gives (the refusals; 'X iti kim?' cases). The word lists the sutras name (the roots, the compound members) are read from the corpus (dhatupatha, ganapatha) or written once as the sutra's own words; mark SCOPE where a rule needs a distinction no flag can carry.` },
]

const ONLY = ['natva', 'satva']
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
SCOPE: ${f.scope}

${DRAFTS[f.id] ? 'DRAFT ALREADY PRESENT: ' + DRAFTS[f.id] + '\n\n' : ''}${'CONTINUING. Your workspace may already hold substantial work from earlier attempts that were interrupted (a family module and, where present, its tests). Before writing anything, look: compare your family module with the skeleton in the repository and read any tests file. If work exists, CONTINUE it: run its tests, decide for every failure whether the module or the test is wrong (check the commentary, not convenience), finish what is missing, and never weaken a test to make it pass or throw the draft away. If not, start fresh. Save progress in your workspace as you go - you may be interrupted again and a later agent will resume from what is on disk.'}\n\nDeliver: the family module with EVERY sutra in scope implemented or honestly marked in COVERAGE; ${f.testfile} with genuine tests; all of step C passing. Then reply with the structured summary (workspace path, files, counts, coverage summary, scope notes, core_requests, open_questions).`
}

function reviewPrompt(f, done) {
  return `
You are an INDEPENDENT ADVERSARIAL REVIEWER. Another agent has implemented the sandhi-rule family "${f.id}" (${f.title}) for a PANINIAN SANDHI ENGINE. Its workspace is ${WSROOT}/${f.id} (an isolated copy of the repo at ${REAL}); its self-report:
${JSON.stringify(done)}

Work in that workspace only; do NOT touch the real repository. You may edit ONLY: src/astadhyayi/sandhi/families/${f.id}.py and ${f.testfile}.
Read src/astadhyayi/sandhi/README.md first (the conventions), then the family module, its tests, and the core it uses (note View.unit_of / joined_pada). Assume the implementation contains mistakes: it was written from commentary in one pass. Your job is to find them and fix them.

1. SOURCES, INDEPENDENTLY. For every sutra in the family scope, read the sutra text, Kasika, Kaumudi, Balamanorama, Tattvabodhini, the vartikas and the Bhashya yourself (corpus.commentary_on(id, name), corpus.varttikas_on(id)) and write down what the rule requires, excepts and competes with - BEFORE reading how the module does it. Then compare. Scope: ${f.scope}
2. ADVERSARIAL CASES. Write at least 40 test inputs you believe the grammar decides (the commentaries' examples AND counter-examples first, then inputs of your own: every trigger with every intervening sound, both sides of every condition, the exceptions, and inputs that must NOT change - a finished word with an n after an r inside one piece, two padas). Work out by hand from the sutras what the correct result and derivation are; then run the engine (python3 -m src.astadhyayi.sandhi "..." prints the trace) and compare RESULT and STEPS. Any disagreement is a defect until you have shown from the sources that your hand derivation was wrong.
3. CITATIONS. For each rule: is the sutra number right? Is each 'overrides' reason a verbatim quotation of the named commentary? Does each Via cite a sutra that really plays the role stated? Fix every error.
4. HONESTY. Does COVERAGE tell the truth? Is any class of sounds or pairing typed rather than derived? Does any rule rewrite the inside of a finished single piece? Does any rule fire where a counter-example says it must not?
5. FIX what you find, in the files you may edit, and add a test for every defect fixed (it must fail without the fix). Re-run: python3 -m unittest ${f.testmodule} tests.test_sandhi_engine tests.test_astadhyayi_no_restating tests.test_astadhyayi_adesa tests.test_astadhyayi_reuse and rulebook.problems() (must be []). If a defect needs a core change, do not make it; describe it exactly in core_requests.
6. Reply with the structured summary. Be honest: remaining_defects must list everything you could not fix.`
}

phase('Implement')
const results = await pipeline(
  SELECTED,
  (f) => agent(implPrompt(f), { label: 'implement:' + f.id, phase: 'Implement', schema: IMPL_SCHEMA, effort: 'xhigh' }),
)
return results.filter(Boolean)
