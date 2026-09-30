# Sandhi engine — handover

Written 2026-09-30 for whoever (person or coding harness) continues this. It is
meant to be read top to bottom once, then used as a checklist. Everything stated
as a fact here was checked on that date; things I did not check are marked
**unverified**.

## 0. The 60-second version

**Goal (the user's words):** "a sandhi engine which can do any sandhi by citing
exact Paninian grammar rules for each step, what is being done in each step and as
per which sutra of Panini." It lives in `src/astadhyayi/sandhi/`; that package's
`README.md` is the spec (input syntax, the four things the engine consults,
"Writing a rule"). It is part of VyakaranaBandhu, whose charter is `NORTH_STAR.md`
(derive don't tabulate; tests that can fail; every claim traceable to a source on
disk; record limits as SCOPE).

**State:** the engine core, all interfaces (CLI, HTTP API, browser tab, splitter),
the test harness, and **six of eight rule families** are done and merged. The
repo's sandhi tests are green: **1000 tests OK** (skipped 1), `rulebook.problems()`
is `[]`, and the repo guards pass. Two things are red or missing on purpose:

1. `tests.test_sandhi_gold` fails: **116** of 592 gold cases neither match nor are
   recorded in `data/sandhi/known_mismatches.json` (which holds 60 entries: the
   ones `tools/sandhi_triage_gemination.py` proved differ from the gold only in
   gemination, in a missing ṇatva/ṣatva, in the phrase-final consonant voiced or
   not, or in one m/ṃ; the other 3 of the file's 4 tests pass).
   This test is the to-do list for the triage in §6-P1. Do not make it green by
   deleting the check.
2. The big `visarga_ru` family (59 rules) is written and green **alone** but breaks
   15 tests when merged with the others, so it is **staged, not merged** (§6-P0).
   The repo carries the 9-rule skeleton in its place.

**Git (corrected 2026-09-30):** `VyakaranaBandhu` *is* a git repository
(`origin` = github.com/Sarvam-Tech-Labs/VyakaranaBandhu, branch `main`, 4 commits before
this work). An earlier version of this handover wrongly said it was not — the warning
came from the parent folder. The sandhi work is on the branch
**`sandhi-engine`**, **pushed to `origin` on 2026-09-30** (`main` was left untouched at
`86a3d7f`); open the pull request at
https://github.com/Sarvam-Tech-Labs/VyakaranaBandhu/pull/new/sandhi-engine, review and
merge from there. Push note: the first attempt, with the Codespaces `GITHUB_TOKEN` that
git uses by default, was refused with HTTP 403 (that token may not write to this repo
although the account may). With the user's OK it was pushed with the stored `gh` login
for that one command, changing no config:
`env -u GITHUB_TOKEN -u GH_TOKEN git -c credential.helper= -c
credential.helper='!gh auth git-credential' push origin sandhi-engine` — use the same
form for later pushes from a Codespace. `sandhi_work/sandhi-engine.bundle` is a
same-disk fallback copy of the first commit. `sandhi_work/backup_pre_merge2/` and `backup_pre_merge3/` are older local
copies, no longer needed for history.

## 1. How to run and verify (copy-paste)

```bash
cd /workspaces/codespaces-blank/VyakaranaBandhu

python3 cli.py --sandhi "iti ādi"                 # a derivation, with sūtra text
python3 cli.py --sandhi-split "ityādi"            # sandhi-viccheda, by synthesis
python3 -m src.astadhyayi.sandhi "rāmas ca"

# The sandhi tests + the three repo guards (~90 s, 1000 tests). Expect: OK (skipped=1)
MODS=$(ls tests/test_sandhi_*.py | grep -v test_sandhi_gold | sed 's#tests/##; s#\.py##; s#^#tests.#' | tr '\n' ' ')
python3 -m unittest $MODS tests.test_astadhyayi_no_restating tests.test_astadhyayi_adesa tests.test_astadhyayi_reuse

# Gold cases against the engine (numbers in §4)
python3 tools/sandhi_eval.py data/sandhi/gold/ac_yan_ayadi.gold.json --show 15
python3 tools/sandhi_eval.py --help               # --boundary --sample --show --json --ignore-avagraha

python3 tools/sandhi_data_validate.py             # validates gold + catalogue vs the corpus

# rulebook self-check — must print []
python3 -c "from src.astadhyayi.sandhi import rulebook; print(rulebook.problems())"
```

The **full repo suite** (`python3 -m unittest discover tests -q`, ~10 min) was run
on 2026-09-30 after the merges: **6340 tests, 1 failure, 1 skipped**. Re-run after the gold triage, the
`--ignore-avagraha` harness option and the `tools/` additions (same day, 575 s):
**6342 tests** (the two new harness tests), **the same single failure**, 1 skipped. The single
failure is `test_sandhi_gold.GoldCases.test_every_case_matches_or_is_a_recorded_mismatch`
— the deliberate triage test (§0, §6-P1). Nothing else in the repo regressed
(baseline before the sandhi work: 5,383 tests, all green). Re-run it after any change
to the core files.

Browser: `python3 -c "import server; server.run_server(8765)"` (port 8000 is the
user's own `http.server`; never kill it). Endpoints: `/api/sandhi`,
`/api/sandhi/split`; UI: the "Sandhi" tab in `ui/`.

## 2. Design decisions that each cost failures — do not relitigate

These are also in the README and in the memory file `project-sandhi-engine.md`.

- **8.2.1 पूर्वत्रासिद्धम् by provenance.** Every `Seg` keeps `prior`/`made_by`. A
  rule is handed a `View` that shows the row as that rule may see it
  (`asiddha.visible`). A rule that *names* a tripādī product lists it in
  `Rule.consumes` (वचनप्रामाण्यात्): 6.1.113/114 see RU, 6.3.111 sees RA_LOPA.
  6.1.86 goes through `Rule.operation` ("ṣatva"/"tuk") + `EKADESA_MARK`.
- **Conflict resolution order:** explicit `Rule.overrides` (each with a verbatim
  commentary reason, read from the corpus by a test) → 8.2.1
  (`asiddha.blocks_vipratisedha`) → 1.4.2 (`vipratisedha`). Semantics are
  *grounded*: **a defeated rule defeats nothing** (this matters in §6-P0). A
  prohibition (प्रतिषेध, e.g. 8.4.44) is an `Application` with `edits=()` at the
  same site and declines only the rules it names.
- **Options (विभाषा) fork derivations.** `State.declined` is keyed by
  `(Rule.key, site)`; `View.refused(...)` asks whether a prohibition applies.
- **The engine acts at junctions.** Interiors of finished input words are left
  alone (otherwise `gacchati`'s cch is rewritten). `View.pairs()` offers interior
  pairs only if one sound was derived in this derivation. `View.unit_of` /
  `joined_pada` lift this for pada-internal rules (ṇatva/ṣatva).
- **6.1.85 antādivat is NOT applied to sound-based rules** (`antadivat=False`
  default); otherwise महर्षि gets a visarga. Chained ekādeśa keeps a contiguous
  word range (`Seg.lw`).
- **Derive, don't tabulate.** Sounds come from `sivasutra.resolve`, `varna`,
  `adesa.antaratama` (+ `supports.nearest` ābhyantara tie-break), `varna.savarna`,
  `reading.yathasamkhya`. Never write a sound class or a pairing by hand; repo
  guards enforce it. **Sūtra text in traces always comes from
  `corpus.load_vidyut_sutrapatha()`**; a hand-typed 1.1.66 once read निर्देशे for
  निर्दिष्टे. Do not type quotations — read them from the corpus.
- **A visarga in the input is read as `s`** unless the word has flag `final:r`;
  the trace records this as an assumption.
- **Flags** (`dvivacana`, `nipata`, `dhatu:ROOT`, `stem:X`, …) supply what letters
  cannot. An unread or misspelt flag yields `SandhiResult.warnings`
  (`rulebook.flag_is_read`). `infer.py` (from the prakrtibhava work) infers a
  flag only from a closed list (e.g. `om` is read as the nipāta particle
  wherever it stands).
- **Each family module exports `RULES` and `COVERAGE=((sūtra, status, note), …)`**
  (status ∈ rule / partial / support / scope / vedic). `rulebook.problems()` must
  stay `[]`. Discovery is automatic: any module in `families/` is loaded.
- **Split (viccheda) is synthesis:** the junction index is built by running the
  forward engine, cached at `data/sandhi/.cache/junction_index.json` (env
  `SANDHI_INDEX_CACHE`), keyed by a source fingerprint; every candidate is
  verified by re-derivation. Lexicon optional: `data/sandhi/lexicon.txt`.
- **Testing rule for the gold data:** each `known_mismatches.json` entry needs
  `kind ∈ {engine-gap, gold-error, scope, underspecified}` and a reason longer than
  15 chars, and **a listed mismatch must still mismatch** (so entries cannot
  silently go stale).

## 3. File map

```
src/astadhyayi/sandhi/
  README.md         the spec — read first
  __init__.py       sandhi()/join(), SandhiResult(start, outcomes, warnings)
  __main__.py       python -m entry
  segs.py rule.py engine.py supports.py parse.py infer.py trace.py rulebook.py
  harness.py        run external cases; verdicts match/missing/extra/error/skipped;
                    citation-agreement metric; visarga s/r readings both tried
  split.py          sandhi-viccheda by synthesis (+ doubled-consonant variants)
  families/         ac_yan_ayadi(23 rules) ac_ekadesa(38) prakrtibhava(20)
                    hal_assimilation(37) nasal_anusvara(23) visarga_ru(9, skeleton)
tests/test_sandhi_*.py   12 files: engine, interfaces, harness, gold, data, ui,
                    split, and one per family (ac_yan_ayadi, ac_ekadesa,
                    prakrtibhava, hal_assimilation, nasal_anusvara)
tests/js/sandhi_render_check.js      UI render check used by test_sandhi_ui
tools/sandhi_eval.py                 gold/dataset runner
tools/sandhi_data_validate.py        validates gold + catalogue against the corpus
tools/sandhi_workarea/               the work-area scripts (merge_families.py, replay/recover, the
                                     Workflow scripts, the ac_ekadesa audit/mutation/fuzz tools);
                                     README inside
docs/notes/sandhi_datasets_SOURCES.md  copy of sandhi_work/external_data/SOURCES.md
tools/sandhi_datasets/               fetch.sh (12 GitHub clones at pinned commits; Kaggle via
                                     the kaggle CLI), normalizers/ (the scripts that built
                                     every normalized file), search/ (Kaggle/HF/GitHub search)
tools/sandhi_triage_gemination.py    proves which gold mismatches differ only in gemination,
                                     only in n→ṇ / s→ṣ (missing natva/satva), only in the
                                     last letter voiced or not, or only in one m/ṃ; records
                                     them (--apply) in known_mismatches.json
data/sandhi/known_mismatches.json    60 entries so far (19 underspecified, 22 scope, 19 engine-gap)
data/sandhi/gold/*.gold.json         229 / 209 / 154 cases (ac_ekadesa, ac_yan_ayadi, prakrtibhava)
data/sandhi/catalogue/*.json         44 / 29 / 59 entries (sūtra-by-sūtra example catalogues)
docs/notes/sandhi_staged/            NOT imported: see §5
```

Existing project files that were modified: `cli.py`, `server.py`, `ui/index.html`,
`ui/app.js`, `ui/theme.css`, `README.md`, `.gitignore`. The legacy
`src/phonetics.py` `SANDHI_RULES` has a duplicate-key bug (a+ṛ listed as ar then ār;
the later wins) — it is not used by the engine.

## 4. Where each rule family stands

| family | state | rules | own tests |
|---|---|---|---|
| ac_yan_ayadi (6.1.77–79 …) | merged, green | 23 | 154 + more |
| ac_ekadesa (6.1.84–101 …) | merged, green | 38 | 138 + more |
| prakrtibhava (1.1.11–19 …) | merged, green | 20 | 228 |
| hal_assimilation (8.2.x, 8.4.x) | merged, green | 37 | 275 |
| nasal_anusvara (8.3.x, 8.4.58 …) | merged, green | 23 | 221 |
| visarga_ru (8.2.66–72, 8.3.x) | **staged**, green alone, breaks 15 merged | 59 (repo has 9) | 228 |
| natva (8.4.1–39) | **draft**, 29 KB, 3 `@rule`s, no tests | – | none |
| satva (8.3.55–119, 8.4.x) | **draft**, 40 KB, rules registered dynamically, no tests | – | none |

Gold match rates on the merged repo (harness: subset match; strict for
counter-example/exhaustive cases; both visarga readings tried):

| gold set | cases | match | rate | missing | extra |
|---|---|---|---|---|---|
| ac_ekadesa | 229 | 195 | 85.2% | 28 | 6 |
| ac_yan_ayadi | 209 | 134 | 64.1% | 74 | 1 |
| prakrtibhava | 154 | 81 | 52.6% | 56 | 17 |
| **total** | **592** | 410 | | | → 176 mismatches, of which 60 recorded, **116 unresolved** |

Only these three families have gold. hal_assimilation, nasal_anusvara and
visarga_ru have example tests but **no independent gold set**, and natva/satva
have nothing.

**First independent dataset run (2026-09-30)** — `vidyut-kashika-sandhi.jsonl`
(204 rows, Kāśikā-derived, third-party answers; see
`sandhi_work/external_data/SOURCES.md`):

| engine | match | rate | rows citing the labelled sūtra |
|---|---|---|---|
| repo as merged (skeleton visarga_ru) | 171 / 204 | 83.8% | 124 of 171 (72.5%) |
| scratch copy with the full visarga_ru (+ the experimental 8.2.39 overrides) | 192 / 204 | **94.1%** | 146 of 192 (76.0%) |

So merging `visarga_ru` (§5) is worth about 21 of the 33 misses on this set and
changes none of the gold-set numbers (the gold has no visarga cases). It fixes,
for example, `bhos + atra` (the repo gives `bhoratra`; the source says `bhoatra`
by 8.3.17 + 8.3.19). The 12 rows that still miss with the full family are **all
classified** (2026-09-30):

| rows | what | status |
|---|---|---|
| 4 | the source omits the avagraha (`agnetra` for `agne'tra`; ids 48, 49, 54, 55) | fixed by `--ignore-avagraha` |
| 5 | the source spells the anunāsika as a following `m̐` (`bhavām̐ścinoti`, `pum̐sputraḥ`; ids 71, 78–81); respelt as a candrabindu on the vowel it equals the engine's first form (`bhavā̐ścinoti`) — checked by code. That the two spellings are the same *sound* is an assumption | spelling; a harness normalization could take it |
| 2 | `vāyo iti`, `bhāno iti` (ids 52, 53): the source has no sandhi — the vocative before `iti` is optionally pragṛhya (1.1.16). The row carries no vocative flag; **verified** that with `vāyo{sambuddhi} iti` the engine gives `vāyoiti` | the vidyut normalizer should attach `sambuddhi` (the information is dropped); not an engine fault |
| 1 | `bhavān + lunāti` (id 193): source `bhavām̐llunāti` (anunāsika on the vowel, ll), engine `bhavāl̐lunāti` (anunāsika l, 8.4.60) | **open** — check the Kāśikā on 8.4.60 |

Arithmetic: 192 (full `visarga_ru`, §5) + 4 (`--ignore-avagraha`) + 5 (the nasal
respelling) = 201/204 (98.5%); attaching `sambuddhi` to the two vocative rows would
make it 203/204 (99.5%), leaving one row genuinely open. None of the spelling or flag
fixes is in the harness or the normalizer yet except `--ignore-avagraha`.

**All twelve dataset files were then run (2026-09-30)**; the full table is in
`sandhi_work/external_data/SOURCES.md`. Summary, repo as merged: 97.6% Scharf
dhātupāṭha compounds, 90.3% SandhiKosh literature, 88.8% SandhiKosh UoH (sample),
87.3% Bhagavadgītā, 83.8% joiner benchmark, 79.3% SandhiKosh Aṣṭādhyāyī, 75.9% UoH
extract (sample), and **52.7% Scharf compound matrix, 52.7% SandhiKosh
rule-external, 30.7% SandhiKosh rule-internal** (words inside words — the weakest
area, since the engine acts at junctions). The "error" verdicts (139 rows over the
files run) are **all classified**: 56 an avagraha inside a piece, 14 a space inside a
piece (the four SandhiKosh files), and 69 a **hyphen inside a piece** (the UoH extract
sample: 3.5% of its rows — the piece is a compound and the hyphen marks its internal
boundary; the harness could pass it through in the engine's own `a-b` syntax). None is
a crash: each is the engine refusing input that is already joined or carries a
character it does not read. A dataset-cleaning / harness task. The misses are
**not triaged**: that is the P4 work in §6.

Also run (2026-09-30): the Kaggle "Devanagari Sanskrit Sandhi Corpus"
(`kaggle-viragumathe5-sandhi-corpus`, 13,100 rows; a 2,000-row sample matches
**86.3%**). About 3% of the rows differ from the engine only by an avagraha the
source writes for an elided `a` (`vā + amutra` → `vā'mutra`), a few tenths of a
percent are corrupt rows, and the rest are not triaged. **Done 2026-09-30:**
`tools/sandhi_eval.py --ignore-avagraha` (and `harness.run_case/evaluate(...,
ignore_avagraha=True)`) compares with the avagraha dropped from both sides. It is
opt-in — off by default, so it cannot hide a real difference unasked — and tested in
`tests/test_sandhi_harness.py` (it does not excuse a wrong form). Measured: the Kaggle
sample goes 86.3% → **90.0%** and the vidyut set 83.8% → **85.8%** (exactly the four
avagraha rows); use it for datasets that write `'` for an elided a (the gold sets
should not need it). One real lead: the source applies the `tad`/`etad`
special case (`saḥ + bhṛśaṃ` → `sabhṛśaṃ`, 6.1.132) and the engine has no inference
of `stem:tad` for `saḥ`/`eṣaḥ` (add to `infer.py`'s closed lists, after checking the
sūtra in the corpus). Details: `sandhi_work/external_data/SOURCES.md`.

What the misses look like (sampled, not exhaustively classified):

- **"extra" = optional doubling.** The engine offers doubled forms
  (kumāryyagāram, vadhvvagāram, ā+udakāntāt → odakāntād) via 8.4.51/8.4.47 and
  8.4.56 where the gold lists one form. Five strict cases
  (ac_ekadesa-137, 167, 212, 215; ac_yan_ayadi-073) are exactly this.
  Decision needed: make doubling opt-in for ordinary junctions (recommended), or
  record these as `underspecified`.
- **"missing" = flags the gold row does not carry**, e.g. `lū + yam → lavyam`
  needs 6.1.79 vānto yi pratyaye and therefore the flag `pratyaya`; the row has none.
  Fix the *rows* (add flags) where the source clearly intends it, else record as
  `underspecified`.
- **"missing" = doubled options in the gold that the engine does not offer**
  (arkaḥ → arkkaḥ, brahmā → brahmmā, apa+hnute → apahnnute; 8.4.46/47 forms).
  Same doubling policy question as above, from the other side.
- **Pragṛhya/option rows** (prakrtibhava-011, 012, 028–030): the gold lists
  `kumāriatra`, `asmeindrābṛhaspatī` (no sandhi) but the engine does not produce
  them, or produces `asmaindrā…`. Check each against the source before touching
  the engine — some of these are the *engine's* gaps, some are gold-side
  errors.
- **Gold errors flagged by the implementing agents (verify, then record as
  `gold-error`):** ac_ekadesa-062, 111, 174, 060/061, 221/222; ac_yan_ayadi-033
  (bābho+yaḥ expected bābhravyaḥ — a vārttika/Vedic form that needs its flag).

## 5. Staged, unmerged work — `docs/notes/sandhi_staged/`

Files carry a `.txt` suffix so nothing imports or discovers them.

- `visarga_ru.py.txt` (135 KB, 59 rules) and `test_sandhi_visarga_ru.py.txt`
  (162 KB, 228 tests). To try: copy them to
  `src/astadhyayi/sandhi/families/visarga_ru.py` and
  `tests/test_sandhi_visarga_ru.py`. The test file already contains the fixes made
  today (whitespace/accent-tolerant quote check; five quotations corrected to the
  commentary's own punctuation). It passes 228/228 in its own isolated workspace.
- `natva.py.txt`, `satva.py.txt` — unfinished drafts from agents that were stopped.
  Treat as notes, not as working code.

### The 15 failures when visarga_ru is merged (diagnosis)

Merged with hal_assimilation + nasal_anusvara etc., these fail:

- visarga_ru: `Agreement.test_the_word_end_table_and_the_engine_choose_the_same_sutra`
  [amnas eva] and [bhuvas{mahavyahrti} iti]; `VedicRules` 8.2.70, 8.2.71, 8.3.50;
  `DhatuFinals` 8.2.72 ×2; `SaAndSaOfTheVisarga` ×2 (anavyayasya, kamye);
  `Ahan.test_kashika_vartika_ruparatrirathantaresu` (ERROR).
- hal_assimilation: `StohScunaScuh` ×2 (one ERROR), `StohStunaStuh`, and
  `TheWholeRulebook` ×2 (lakshmi…, laghusiddhantakaumudi lines).

Root cause found for the 8.2.7x group: the visarga family declares
`8.2.66 overrides 8.2.39` (जश्त्वापवादः), and `8.2.70/71/72 override 8.2.66`.
Because **a defeated rule defeats nothing**, once 8.2.72 (or the Vedic option)
displaces 8.2.66, the real `8.2.39` of hal_assimilation is no longer held off and
fires on the final `s`, giving `vidvadbhyām` with the wrong citation (8.2.39, not
8.2.72) and `bhuvaditi` / `amnadeva` where the Kāśikā expects `bhuvariti` /
`amnareva`. (When this family was developed, hal_assimilation was a 5-rule skeleton
so it never met the real 8.2.39.) Likely fix: give 8.2.70/71/72 their own
`overrides` entry for `8.2.39` **with a reason that is verbatim in the corpus**
(look in Kāśikā/Kaumudī/Bālamanoramā on 8.2.72 for a jaśtva-exception wording; if
none exists, prefer resolving via 8.2.1/1.4.2 ordering rather than inventing a
quotation). The hal_assimilation failures were not diagnosed; they may be
expectations written against the skeleton visarga, or may be real. Read each
before changing anything.

**Experiment done 2026-09-30 (scratch copy `sandhi_work/try_p0/`, nothing merged):**
adding `("8.2.39", …)` to the `overrides` of 8.2.70, 8.2.71 and 8.2.72 in
`visarga_ru.py` cut the 15 failures to **9**: all six of the 8.2.7x failures went
away. I used the existing verbatim Kaumudī quote on 8.2.66 (`जश्त्वापवादः`) as the
reason; **no commentary I searched says that 8.2.70–72 are exceptions to 8.2.39**
(Kaumudī and Bālamanoramā say it only of 8.2.66), so that reason is borrowed and
not defensible as it stands. Either find a real quotation, or decide the doctrine
(is a rule that defeats an apavāda entitled to hold back the original utsarga?)
and encode it in the engine rather than in three `overrides`. The sound is `d`
either way; what is at stake is which sūtra is cited.

The 9 that remain, as far as I diagnosed them:

- `hal_assimilation` `StohScunaScuh.test_the_kasika_and_kaumudi_examples`,
  `StohStunaStuh.test_the_kaumudi_examples`,
  `TheWholeRulebook.test_the_laghusiddhantakaumudi_hal_sandhi_lines` /
  `…lakshmi…`: **very likely expectations, not engine faults.** With the real
  visarga rules present, `rāmas śete` gives both `rāmaḥ śete` and `rāmaśśete`
  (8.3.36 वा शरि: the visarga may stay), and likewise `rāmas ṣaṣṭhaḥ`; the tests
  were written against the skeleton and expect one form. Check the Kāśikā/Kaumudī
  on 8.3.36, then widen the expected sets (as was done today for `ṣaṭ santaḥ`).
- `StohScunaScuh.test_the_uncrossed_pairing_…` (ERROR, no 8.4.40 step) — same
  cause, unconfirmed.
- `visarga_ru`: `SaAndSaOfTheVisarga` ×2 (`prātar kalpa{pratyaya}` and
  `gīr kāmyati{pratyaya}` now also yield the jihvāmūlīya form, `prātaẖkalpa`,
  `gīẖkāmyati`), `VedicRules` 8.3.50 (`viśvatas karat` has 2 outcomes, the test
  says the rule is nitya), `Ahan…ruparatrirathantaresu` (ERROR, no vārttika
  step). These are the **real unknowns**: read the Kāśikā on 8.3.37/38 and
  8.3.50 and 8.2.68 vārttika before deciding whether the engine or the test is
  wrong.

Also noticed: with the full visarga_ru merged, `nasal_anusvara` reported 22
rules instead of 23 — a key collision somewhere; find it (compare
`rulebook.by_family()` before/after).

## 6. What is left, in priority order

**P0 — merge visarga_ru** (§5). Success = its 228 tests + all others green together,
`rulebook.problems() == []`, guards green. Use the dry-run first.

**P1 — triage the 116 unresolved gold cases** (176 mismatches minus 60 already recorded) into
`data/sandhi/known_mismatches.json` (format: read `tests/test_sandhi_gold.py`).
For each: fix the engine, fix the gold row, or record with an honest
`kind`/`reason`. Decide the doubling policy first (§4) — it removes most "extra"
and a share of "missing". Success = `tests.test_sandhi_gold` green.

Composition of the unresolved rows, clustered 2026-09-30 by verdict, number of
words, flags and whether a step fired. The counts are from the clustering run
*before* the last 13 rows (9 ṇatva/ṣatva, 4 pausal/m-ṃ variants) were recorded (129 rows then; 116 now). The
clusters are heterogeneous — one example per cluster proved misleading once already
— so read the cases, not the labels.

| rows | cluster | notes |
|---|---|---|
| 55 | two words, missing, no flags | a mix: ṇatva/ṣatva that the tool could not prove because another difference is present, and real ekādeśa questions. Start here |
| 15 | two words, missing, with flags | flag-vocabulary questions (§6-P5); e.g. `sukhena + ṛtaḥ` → `sukhārtaḥ` is a vārttika (ac_ekadesa-060/061, already suspected gold errors) |
| 12 | two words, missing, no step fired, no flags | the rule is not built or a flag is missing (`brahmahū + su` → `brahmahūṣu` was ṣatva) |
| 9 | two words, missing, no step fired, with flags | e.g. `lū + yam` → `lavyam` needs `pratyaya` (6.1.79) |
| 8 | two words, missing, counter-example rows | e.g. `sukhena + itaḥ` → `sukhetaḥ` (ac_ekadesa-062, suspected gold error) |
| 12 | one word, missing | `sthālī` (ac_yan_ayadi-078) lists `sthth…` and `vatsaḥ` (-080) lists `vathsaḥ`: these are not the doubling of an aspirate (that is t+th, `stth…`) — suspected gold errors, check the Kāśikā on 8.4.47 |
| 8 | strict "extra" rows | 4 of these were recorded (the engine also offers the pausal voiced form — `predidhat`/`predidhad`, `ado'bhavat`/`ado'bhavad` — or an m/ṃ variant). **Suggested harness change:** compare counter-example rows modulo the *phrase-final* pausal variant, since such a row is about whether the junction rule applied, not about how the phrase ends; then these entries can be removed. The other 4 are not of that kind: read them |
| 10 | three or more words, or other | e.g. `adhi + i + ya` → `adhītya` (a tuk, 6.1.71), `jānu + u + asya + rujati`, `tṛp + tā` → `tarptā`, `akṣadiv + bhyām` → `akṣadyūbhyām` |

**P2 — finish natva and satva** (8.4.1–39 ṇatva; 8.3.55–119 and 8.4.x ṣatva) as
families with tests, in the existing style ("Writing a rule" in the package
README; look at `hal_assimilation.py` for the house style at scale). Then
**gold for hal_assimilation, nasal_anusvara, visarga_ru, natva, satva** (the
extraction method: cases quoted from Kāśikā/Kaumudī/Laghukaumudī, validated by
`tools/sandhi_data_validate.py`; see `gold_import.py` in the work area).

**P3 — cross-family integration.** The families were built in isolation and only
pairwise-tested. Doubling multiplies the number of surfaces; some optional-form
interplay (8.2.23 / 8.2.29 acting on a word's final cluster; 6.1.96 vs 7.2.80) is
open. Add a test module that runs sandhi over mixed sentences and checks the
derivation cites the same sūtras as an independent source.

**P4 — external datasets at scale** (§8). Run through `tools/sandhi_eval.py`
(`--sample` first), cluster the misses by junction and step signature, and turn
recurring clusters into either rules or `known_mismatches` entries. The harness
already clusters (`Summary.worst_junctions`, `by_steps`).

**P5 — hygiene.**
- Update the README's flag vocabulary with the flags the families actually read:
  aat, avyakta, amredita, dac, subanta, sup:NAME, pum, krdanta, trtiya, aniyoga,
  samprasarana, uth, tannimitta, shakyartha, krayartha, adhvaparimana, stri,
  abhyasa, pluta, akac, nan_samasa, padapuranam, sakatayana, saptamibahuvacana,
  pratyaya, gati, avyaya, apratyaya, isus, krtvo_artha, samartha, antahpada,
  pancami, sasthi, adhyartha, mahavyahrti, kvasu, bha, dhatu (the visarga_ru
  module's docstring lists its own).
- Adversarial review passes were **dropped** (only implementers ran). Run one per
  family: try to make the engine cite a wrong sūtra with a right form.
- Run the full 5,383-test suite.
- Open design questions: 6.1.85 antādivat for sound-based rules (currently
  off); teacher-specific narrowing of the doubling rules; Śākaṭāyana's lighter
  य्/व् (8.3.18) is only offered with flag `sakatayana`.

## 7. The work area (outside the repo, but it persists)

`/workspaces/codespaces-blank/sandhi_work/` (1.8 GB; **`/tmp` is wiped on a
Codespace restart, this directory is not**):

| path | what |
|---|---|
| `ws/<family>/` | isolated repo copies where agents built each family: ac_yan_ayadi, ac_ekadesa, prakrtibhava, hal_assimilation, nasal_anusvara, visarga_ru, natva, satva. **Their core files (engine.py, rule.py, …) are stale copies — never copy core files back.** |
| `merge_families.py` | `python3 merge_families.py [--apply] [family …]` copies a family's module + tests into the repo. Dry-run by default. It reports "outside its remit … DIFFERS" for core files: those are stale copies, ignore them. |
| `scripts/impl_A.js`, `impl_B.js`, `tier2.js` | the Workflow scripts (implementer-only, generic "continue from what is on disk"). impl_B run id was `wf_89751008-1aa`. Only re-run with the user's OK to spend usage. |
| `backup_pre_merge2/`, `backup_pre_merge3/` | copies of `src/astadhyayi/sandhi` and `tests` before the two latest merges (merge3 = today, includes all 5 merged families) |
| `recover.py`, `replay*.py` | rebuild files by replaying Write/Edit tool calls from the session transcript. Caveat: files an agent wrote through a Bash heredoc are **not** replayed (this is why natva/satva are truncated). |
| `repo_ro/` | read-only repo copy used for transcript replays |
| `external_data/` | 409 MB of datasets (§8) |
| `gold_import.py`, `scratch/sandhi_data/` | how the gold was imported and validated |

Session transcript (full history, incl. agents' reasoning):
`/home/codespace/.claude/projects/-workspaces-codespaces-blank/14581267-db0b-459c-a73b-438634dd89d5.jsonl`.

## 8. External datasets and licences

Under `sandhi_work/external_data/`:
`normalized/` holds JSONL in the harness's schema — `sandhikosh-{astadhyayi,
bhagavadgita,literature,rule-external,rule-internal,uoh}.jsonl`,
`scharf-sandhi-{compound-matrix,dhatupatha-compounds,external}.jsonl`,
`uohyd-sandhi-extract(.sample).jsonl`, `vidyut-kashika-sandhi.jsonl`,
`lsk-gold-battery.jsonl`; `raw/` holds the clones (DCS, Scharf, a joiner benchmark,
SandhiSplitter, …); `qc/` holds checks.

- **SandhiKosh data is research-use-only. Do not commit it to the repo.** Provide
  a fetch script instead.
- The dataset agent was stopped before it wrote its README, so provenance and
  licences were reconstructed on 2026-09-30 into
  `sandhi_work/external_data/SOURCES.md` (12 GitHub clones, licence per clone, row
  counts per normalized file, which clone each file came from). **Correction:** an
  earlier version of this handover said no Kaggle/HuggingFace data had been
  collected. In fact the agent's working directory `sandhi_work/scratch_ds/` holds
  10 Kaggle dataset folders (6 downloaded, 4 metadata only; none with a licence in its
  metadata), 5 Wikipedia articles, and the Kaggle (210) and HuggingFace (288) search
  results. HuggingFace was searched, not downloaded; **IndiaAI was never reached**.
  Two Kaggle sandhi corpora were normalized on 2026-09-30; the smaller one was
  run (results in §4). The other is a superset of it and has not been run.
  Three clones state no licence, one is research-only (SandhiKosh), two are GPL:
  keep all of it out of the repo and ship a fetch script instead.
- Default junction kind for a corpus of words-inside-words (SandhiKosh
  *internal*) is `anga`: `default_boundary="anga"` in `harness.evaluate`.
- The sūtra citations in a dataset (when it has any) are compared with the
  derivation's ("citation agreement"); a form match with a wrong sūtra is still a
  finding.

## 9. Environment pitfalls

- 2 CPUs, ~7 GB. A Workflow runs 2 agents at once. Heavy parallelism (4 workflows
  plus a subagent) exhausted the account's session limit in ~1h40m; the weekly
  limit was at 98% when this was written. Prefer transcript replay to redoing
  agent work; don't launch new fleets without checking with the user.
- Port 8000 belongs to the user. Test the server on 8765.
- The Bash safety check refuses `rm -rf $VAR/$OTHER`; create directories with
  `mkdir -p "${VAR:?}/${X:?}"` and avoid removals.
- First `sandhi()` call takes ~4 s (lazy import of the whole `rules` package).
- GRETIL Laghukaumudī `vlk = p_a,b.c` tags contain errors; verify by text.
- Hand-typed quotations from commentaries have been wrong every time they were
  tried (double spaces, `।` vs `,`, Vedic accent marks such as अग॑न्म॒). Compare
  after collapsing whitespace and stripping U+0951/U+0952, as the visarga_ru
  quote test now does.

## 10. Suggested first hour for the next person

1. `git fetch && git checkout sandhi-engine` (§0); everything below is on that branch.
2. Run the verification block in §1; confirm 1000 OK and the single gold failure.
3. Try P0: put `visarga_ru` back from `docs/notes/sandhi_staged/`, run
   `python3 -m unittest tests.test_sandhi_visarga_ru` and the combined run, and
   work through the 8.2.7x group first (one diagnosis explains most of it).
4. Only then P1.
