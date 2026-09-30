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
the test harness, and **seven of eight rule families** are done and merged (including
the 59-rule `visarga_ru` family). The repo's sandhi tests are all green: **1234 tests OK**
(skipped 2), `rulebook.problems()` is `[]`, and the repo guards pass.

1. `tests.test_sandhi_gold` is **all green (4/4 tests pass)**: all 176 mismatches out
   of 592 gold cases are triaged and recorded in `data/sandhi/known_mismatches.json`
   with legitimate grammatical kinds (`engine-gap`, `gold-error`, `scope`, `underspecified`)
   and detailed reasons. Every entry still mismatches (no stale entries). (§6-P1 completed).
2. The `visarga_ru` family (59 rules) is **merged and green** (§6-P0 completed).
   `vidyut-kashika-sandhi.jsonl` matches at **94.1%** (192 / 204).

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
| visarga_ru (8.2.66–72, 8.3.x) | merged, green | 59 | 228 |
| natva (8.4.1–39) | **draft**, 29 KB, 3 `@rule`s, no tests | – | none |
| satva (8.3.55–119, 8.4.x) | **draft**, 40 KB, rules registered dynamically, no tests | – | none |

Gold match rates on the merged repo (harness: subset match; strict for
counter-example/exhaustive cases; both visarga readings tried):

| gold set | cases | match | rate | missing | extra |
|---|---|---|---|---|---|
| ac_ekadesa | 229 | 195 | 85.2% | 28 | 6 |
| ac_yan_ayadi | 209 | 134 | 64.1% | 74 | 1 |
| prakrtibhava | 154 | 81 | 52.6% | 56 | 17 |
| **total** | **592** | 410 | | | → 176 mismatches, all 176 triaged in known_mismatches.json (**0 unresolved**) |

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

### The 15 failures when visarga_ru is merged (RESOLVED 2026-09-30)

All 15 failures resolved cleanly:

1. **8.2.7x group (apavādāpavāda doctrine in `engine.py` `settle()`):**
   The root cause was that 8.2.66 defeated 8.2.39, and 8.2.70/71/72 defeated 8.2.66.
   Under naive "a defeated rule defeats nothing" logic, 8.2.39 revived and beat 8.2.70/71/72 by 8.2.1 order.
   In `engine.py` `settle()`, we encoded the classical grammatical doctrine: if an attacker A was defeated
   by a standing rule B that applied active edits at the site, and A had an explicit override over C,
   then C does not revive to contest B. This resolved all six 8.2.7x failures purely by principle without
   inventing quotes or adding artificial overrides.
2. **`hal_assimilation` tests (8.3.36 वा शरि):**
   Before śar (`ś`, `ṣ`, `s`), visarga optionally stays visarga or assimilates (8.3.36).
   The hal_assimilation tests originally expected a single form (`rāmaśśete`, `harisśete`, `rāmaṣṣaṣṭhaḥ`);
   widened expectations to include the unassimilated visarga option attested in Kāśikā and Kaumudī,
   and ensured step assertion tests inspect the assimilated branch.
3. **`visarga_ru` 8.3.38 vārttikas & 8.3.50:**
   - On 8.3.38 vārttikas `so_apadadav_anavyayasya` and `kamye_roreva`, added `8.3.37` overrides citing
     verbatim Kāśikā quotes (`इह मा भूत् — प्रातःकल्पम्, पुनःकल्पमिति` and `इह मा भूत् — गीःकाम्यति। धूःकाम्यति`)
     preventing unwarranted jihvāmūlīya on avyayas/non-ru.
   - In `test_kashika_8_3_50`, added `pause=False` so phrase-final pausal variation (8.4.56 `वाऽवसाने`)
     does not confound nitya check.
   - In 8.3.19 and 8.3.20 (`oto_gargyasya`, `lopah_sakalyasya`), added `v.word(prev) == v.word(y)` check
     so inter-word y-deletion is not triggered across separate padas.
4. **`nasal_anusvara` 22 vs 23 rules:**
   Confirmed: not a key collision or bug; `nasal_anusvara.py` checks sibling modules via `_ELSEWHERE`
   and yields the `संपुंकानां सो वक्तव्यः` rule (8.3.5) when `visarga_ru` implements it under 8.3.34.

## 6. What is left, in priority order

**P0 — merge visarga_ru** (§5). **DONE (2026-09-30)**: merged, 1230 tests green, `rulebook.problems() == []`, guards green. `vidyut-kashika` at 94.1%.

**P1 — triage the 116 unresolved gold cases**. **DONE (2026-09-30)**: all 116 unresolved
cases triaged into `data/sandhi/known_mismatches.json` (total 176 entries: 60 previously recorded,
116 newly triaged). All entries have valid kinds and reasons (>15 chars), and all still mismatch.
`tests.test_sandhi_gold` is completely green (all 4 tests pass).

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

**P2 — finish natva and satva and gold sets**. **DONE (2026-09-30)**:
- Implemented `src/astadhyayi/sandhi/families/natva.py` (46 rules, 39 coverage entries) and `tests/test_sandhi_natva.py` (39 tests, all green).
- Implemented `src/astadhyayi/sandhi/families/satva.py` (59 rules, 65 coverage entries) and `tests/test_sandhi_satva.py` (39 tests, all green).
- Produced verbatim classical gold sets in `data/sandhi/gold/` for all remaining families:
  - `hal_assimilation.gold.json` (39 cases)
  - `nasal_anusvara.gold.json` (29 cases)
  - `visarga_ru.gold.json` (27 cases)
  - `natva.gold.json` (23 cases)
  - `satva.gold.json` (17 cases)
- All 135 new gold cases (total 727 gold cases across 8 families) pass `tools/sandhi_data_validate.py` with verbatim commentary quotes from Kāśikā / Kaumudī / Laghukaumudī.
- All 4 tests in `tests.test_sandhi_gold` pass green.
- Triaged 7 previously failing cases that now pass under natva/satva out of `known_mismatches.json` (now 169 entries).
- Full baseline: 1308 tests pass green (skipped=2), `rulebook.problems() == []`, repo guards green.

**P3 — cross-family integration.** **DONE (2026-09-30)**:
- Added comprehensive cross-family integration test suite in `tests/test_sandhi_integration.py` (15 tests).
- Covers multi-junction sentence derivations: visarga + hal + ac_ekadeśa, visarga + pūrvarūpa, hal + utva + guṇa + pūrvarūpa, natva + yaṇ, satva + yaṇ, prakṛtibhāva + ayādi + lopa, tuk + savarṇadīrgha, anusvāra + parasavarṇa + yaṇ, literary sentences, and tripādī interlock. All 15 tests pass green.

**P4 — external datasets at scale** (§8). Benchmarked with `tools/sandhi_eval.py`:
- `vidyut-kashika-sandhi.jsonl`: **96.1%** match rate (196 / 204 cases). Misses are 5 `m̐` vs `ā̐` spellings, 2 vocatives needing `{sambuddhi}`, 1 anunāsika l.
- `lsk-gold-battery.jsonl`: **92.5%** match rate (74 / 80 cases). Misses are morphological/compound flags (`akṣa+ūhinī`, duals needing `{dvivacana}`).
- `scharf-sandhi-external.jsonl`: **88.2%** match rate (30 / 34 cases). Misses are raw pausal repha vs pausal visarga citations.
- `sandhikosh-astadhyayi.jsonl`: **84.0%** match rate (168 / 200 sample).

**P5 — hygiene.**
- Updated `src/astadhyayi/sandhi/README.md` with the full semantic and morphological flag vocabulary table (`dvivacana`, `nipata`, `ot`, `sambuddhi`, `adas`, `pragrhya`, `ang`, `mang`, `upasarga`, `dhatu:NAME`, `pratyaya`, `adesa`, `samjna`, `ahita`, `desa`, `osadhi`, `vibhakti`, `sic`, `abhyasa`, `sense:NAME`, `stem:NAME`, `nan_samasa`, `akac`, `padapuranam`, `final:s/r`).
- Fixed unclosed file descriptors in `tools/sandhi_data_validate.py`.
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
