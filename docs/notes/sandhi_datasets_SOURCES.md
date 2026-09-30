# External sandhi datasets — provenance and licences

Reconstructed 2026-09-30 from the clones themselves, because the collecting agent
was stopped before it wrote its own README. Licence text was read from each repo's
LICENSE file or README; it has **not** been checked by a lawyer, and a repo with no
licence file is treated as "all rights reserved" (no permission to redistribute).

**Corrected 2026-09-30:** an earlier version of this file said every source was a
GitHub repository and that no Kaggle or HuggingFace data had been obtained. That was
wrong. The collecting agent's working directory, `../scratch_ds/` (not `raw/`), also
holds 10 Kaggle dataset folders, 5 Wikipedia articles and the search results for
Kaggle (210 hits) and HuggingFace (288 hits) — see "Also collected" below. **IndiaAI
was never reached: nothing from it exists.** Nothing from HuggingFace was downloaded,
only searched.

**Nothing in this directory may be committed to the VyakaranaBandhu repo.** The
SandhiKosh rows are research-use-only, and several sources state no licence at all.
The repo should carry a fetch script that clones these URLs, not the data.

## Raw clones (`raw/<name>/`)

| clone | upstream | licence found | used for a normalized file? |
|---|---|---|---|
| `sanskrit-sandhi_SandhiKosh` | github.com/sanskrit-sandhi/SandhiKosh | **"free of cost for research purposes only"** (README); no licence file | yes → `sandhikosh-*` (13,771 rows) |
| `funderburkjim__ScharfSandhi` | github.com/funderburkjim/ScharfSandhi | MIT | yes → `scharf-sandhi-*` (1,585 rows) |
| `kmadathil_sanskrit_parser` | github.com/kmadathil/sanskrit_parser | MIT (the data files under `tests/sandhi_test_data/` carry no separate licence; their origin is a University of Hyderabad list — unverified) | yes → `uohyd-sandhi-extract` (72,194 rows; `.sample` = 10,000) |
| `performance__sandhi-joiner-benchmark` | github.com/performance/sandhi-joiner-benchmark | MIT | yes → `lsk-gold-battery` (80 rows) |
| `ambuda-org_vidyut` | github.com/ambuda-org/vidyut | MIT (README) | yes → `vidyut-kashika-sandhi` (204 rows) |
| `ambuda-org__dcs` | github.com/ambuda-org/dcs | CC-BY 4.0 (README) — attribution required | no (raw only) |
| `SriramKrishnan8__sanskrit_segmentation_evaluation` | github.com/SriramKrishnan8/sanskrit_segmentation_evaluation | GPL (LICENSE) | no (raw only) |
| `shantanuo__sandhi` | github.com/shantanuo/sandhi | GPL (LICENSE.txt) | no (raw only) |
| `krishnamrith12__KISS_Sanskrit_Parsing_Data` | github.com/krishnamrith12/KISS_Sanskrit_Parsing_Data | MIT (text inside its README) | no (raw only) |
| `SandeshLamichhane4473__sandhi-split-sanskrit-dataset` | github.com/SandeshLamichhane4473/sandhi-split-sanskrit-dataset | **none stated** | no (raw only) |
| `SandhiKSU__SandhiSplitter` | github.com/SandhiKSU/SandhiSplitter | **none stated** | no (raw only) |
| `sanskrit-sandhi__sanskrit_sandhi_corpus` | github.com/sanskrit-sandhi/sanskrit_sandhi_corpus | **none stated** | no (raw only) |

Six raw clones were collected but never normalized. They are unexplored leads, not
tested data.

## Also collected, in `../scratch_ds/` (outside `raw/`)

`scratch_ds/external_data/raw/kaggle/` (62 MB) — ten Kaggle dataset folders.
`metadata.json` carries **no licence** for any of them (`licenses: null`); the
licence must be read from each dataset's Kaggle page before any use beyond local
testing. Only six actually downloaded; four hold metadata only.

| Kaggle dataset | downloaded | what it is | normalized? |
|---|---|---|---|
| `viragumathe5/sanskrit-sandhi-corpus` | yes (train.xlsx 10,000 + test.xlsx 3,500 rows) | "Devanagari Sanskrit Sandhi Corpus": joined form, split form, type | **yes → `kaggle-viragumathe5-sandhi-corpus`** (13,100 rows) |
| `tanujsaxena/sandhi-data` | yes (sandhi_data.xlsx, 13,931 rows) | "Word-Split Pairs"; a **superset** of the one above (all 12,840 unique pairs of that set are in it) | **yes → `kaggle-tanujsaxena-sandhi-data`** (13,529 rows) |
| `varunrajuvangar/rigved-all-sukta-verses-and-meaning-dataset` | yes (38.8 MB JSON) | Rigveda saṃhitā vs padapāṭha; uploader says MIT | script `norm_rigveda_kaggle.py` exists; output not produced |
| `reddy1406/codebase-sandhi` | yes (23 MB) | the SansSandhi code | no |
| `andrasivasaiteja/sanskrit-words-meaning-and-grammatical-features` | yes (Dictionary.xlsx) | word list | no |
| `vinitkp/sanskrit-words` | yes (docx) | word list | no |
| `akashsuklabaidya/segmentation-dataset-fyp-25` | metadata only | word segmentation | no |
| `aluminium13/vyakaran` | metadata only | – | no |
| `dakshdhawal/rigveda-dataset` | metadata only | Rigveda | no |
| `sauhardsaini/pos-sanskrit-annotated-text` | metadata only | POS-annotated text | no |

`scratch_ds/external_data/raw/wikimedia/` — five English Wikipedia articles (Sandhi,
Sanskrit Sandhi, Sanskrit grammar, Vedic Sanskrit grammar, Anusvara), HTML and JSON;
Wikipedia text is CC BY-SA (not checked here). Reference reading, not test data.
`scratch_ds/search/` — `kaggle_search_results.json` (210 datasets) and
`hf_search_results.json` (288 datasets) with the scripts that made them; the
HuggingFace hits were never downloaded, so they are unexplored leads.

The scripts that built every normalized file, and the search scripts, are kept in
the repo at `VyakaranaBandhu/tools/sandhi_datasets/` (`normalizers/`, `search/`,
`fetch.sh` with the pinned commits). They hard-code `/workspaces/codespaces-blank/
sandhi_work/` paths and the `scratch_ds/venv` (which has openpyxl); edit `ROOT`/`RAW`.

## Normalized files (`normalized/*.jsonl`, the harness schema)

One JSON object per line: `id, dataset, input[], output, junction{left_final,
right_initial}, sandhi_type, rule, boundary, vedic, source{file, locator, url}`.
`source.file` names the upstream file and `locator` the line, so any row can be
traced back. Row counts (`wc -l`):

| file | rows | from |
|---|---|---|
| `sandhikosh-uoh` | 9,288 | SandhiKosh |
| `sandhikosh-astadhyayi` | 2,675 | SandhiKosh |
| `sandhikosh-bhagavadgita` | 1,382 | SandhiKosh |
| `sandhikosh-rule-internal` | 150 | SandhiKosh (words inside words → `boundary=anga`) |
| `sandhikosh-literature` | 145 | SandhiKosh |
| `sandhikosh-rule-external` | 131 | SandhiKosh |
| `scharf-sandhi-compound-matrix` | 1,298 | ScharfSandhi |
| `scharf-sandhi-dhatupatha-compounds` | 253 | ScharfSandhi |
| `scharf-sandhi-external` | 34 | ScharfSandhi |
| `uohyd-sandhi-extract` | 72,194 | kmadathil/sanskrit_parser |
| `uohyd-sandhi-extract.sample` | 10,000 | subset of the line above |
| `vidyut-kashika-sandhi` | 204 | ambuda-org/vidyut (Kāśikā-based tests) |
| `lsk-gold-battery` | 80 | performance/sandhi-joiner-benchmark |
| `kaggle-viragumathe5-sandhi-corpus` | 13,100 | Kaggle (train + test); 398 rows dropped: 382 with more than 4 pieces, 15 without a `+`, 1 empty |
| `kaggle-tanujsaxena-sandhi-data` | 13,529 | Kaggle; overlaps the line above almost entirely — **do not add the two** |
| **total (without the sample and the tanujsaxena duplicate)** | **100,934** | |

`qc/` holds the per-file quality reports (rows dropped and why: e.g.
`empty-input-piece` 18 in the UoH extract, `stem-not-in-output` 4 in the vidyut
file) and `qc/rejected/` the rejected rows. The Scharf build kept 6 rows where the
original and the v1 output differ (`qc/scharf_build_summary.json`) — read that
before trusting those rows as gold.

## How to run one through the engine

```bash
cd /workspaces/codespaces-blank/VyakaranaBandhu
python3 tools/sandhi_eval.py ../sandhi_work/external_data/normalized/vidyut-kashika-sandhi.jsonl --show 15
python3 tools/sandhi_eval.py <file> --sample 2000        # a random subset first
python3 tools/sandhi_eval.py <file> --boundary anga      # for words-inside-words corpora
python3 tools/sandhi_eval.py <file> --ignore-avagraha    # datasets that write ' for an elided a
                                                         # (vidyut 83.8% -> 85.8%, Kaggle sample 86.3% -> 90.0%)
```

Results (2026-09-30, engine as merged in the repo, skeleton `visarga_ru`; large
files sampled at 2,000 rows; "err" = the engine refused the input):

| file | rows run | match | rate | err |
|---|---|---|---|---|
| scharf-sandhi-dhatupatha-compounds | 253 | 247 | 97.6% | 0 |
| sandhikosh-literature | 145 | 131 | 90.3% | 4 |
| scharf-sandhi-external | 34 | 30 | 88.2% | 0 |
| sandhikosh-uoh (sample) | 2000 | 1776 | 88.8% | 0 |
| sandhikosh-bhagavadgita | 1382 | 1207 | 87.3% | 12 |
| lsk-gold-battery | 80 | 67 | 83.8% | 0 |
| vidyut-kashika-sandhi | 204 | 171 | 83.8% (94.1% with full visarga_ru) | 0 |
| sandhikosh-astadhyayi | 2675 | 2121 | 79.3% | 43 |
| uohyd-sandhi-extract.sample (sample) | 2000 | 1518 | 75.9% | 79 |
| scharf-sandhi-compound-matrix | 1298 | 684 | 52.7% | 0 |
| kaggle-viragumathe5-sandhi-corpus (sample, seed 1) | 2000 | 1726 | 86.3% | 4 |
| sandhikosh-rule-external | 131 | 69 | 52.7% | 1 |
| sandhikosh-rule-internal (`--boundary anga`) | 150 | 46 | 30.7% | 0 |

All 139 "err" rows were classified (2026-09-30): the 79 in the UoH sample are 69
hyphens inside a piece (a compound's internal boundary written inside one piece) and
10 avagraha. The 60 in the four SandhiKosh files: every one is the
engine refusing an input that is **already joined** — an avagraha inside a piece
(`adhiśīṅsthā''sām`, `puro'grato'greṣu`: 46) or a space inside a piece
(`yoge kṣema`: 14). None is a crash. They are dataset normalization work
(split the row's pieces properly), not engine faults.

Low rates to look at first: `scharf-sandhi-compound-matrix` and
`sandhikosh-rule-external` (52.7%, both mostly junction-level rows) and
`sandhikosh-rule-internal` (30.7%, words-inside-words — the engine acts at
junctions, so internal sandhi is the weakest area and `anga`-boundary handling of
suffix junctions is where to start). None of these misses has been triaged.

These are third-party answers, not verified ones. A miss is a lead (engine fault,
wrong or under-specified row, or a place the engine deliberately does not go), and
the visarga in a row is tried under both readings (`final:s`, `final:r`).

## Kaggle sandhi corpus — what the misses are (2026-09-30)

A fresh random 2,000-row sample (seed 7) of `kaggle-viragumathe5-sandhi-corpus`:
1,717 match (85.9%), 9 errors (input refused), 274 misses. Classified by code where
possible:

| class | rows | meaning |
|---|---|---|
| avagraha-only difference | 62 (3.1% of all rows) | the expected form has `'` where the engine has none (`vā + amutra` → `vā'mutra`, engine `vāmutra`): the source writes an avagraha for an elided `a`. With the avagraha ignored these rows match, i.e. 89.0% |
| corrupt row | 7 | the expected output is unrelated to the pieces (`tip + pada` → `jñānaprakāracaitrādi…`, `saḥ + eṣa` → `saeṣaeṣakṛtakasupto'bhavat|`): the source is noisy; expect a few tenths of a percent of such rows |
| avagraha restored as `a` | 1 | |
| other | 204 | **not triaged** — these are the leads |

Two leads from reading a handful of the "other" rows (not verified): `saḥ +
bhṛśaṃ` → `sabhṛśaṃ` but the engine gives `sobhṛśaṃ` — the source applies the
`tad`/`etad` special case (6.1.132, in the staged `visarga_ru`, which reads the flag
`stem:tad`), and the engine has no rule that infers that `saḥ`/`eṣaḥ` are those
stems; and `dakṣiṇāt + āc` → `dakṣiṇādāc` where the engine gives `dakṣiṇādāk` /
`dakṣiṇādāg` (the engine devoices/voices the final of `āc`, the source does not).

## vidyut-kashika-sandhi — the 12 rows that miss with the full `visarga_ru`

All classified (2026-09-30): 4 avagraha omitted by the source (ids 48, 49, 54, 55;
`--ignore-avagraha`), 5 the source's `m̐` for the anunāsika (ids 71, 78–81; respelling
it as a candrabindu on the vowel makes each equal the engine's first form — checked
by code; sameness of sound is an assumption), 2 a vocative before `iti` with no
vocative flag on the row (ids 52, 53: with `{sambuddhi}` the engine gives the
source's `vāyoiti`), and 1 open (id 193, `bhavām̐llunāti` vs the engine's
`bhavāl̐lunāti`, 8.4.60).
