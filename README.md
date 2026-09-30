# VyākaraṇaBandhu (व्याकरणबन्धु)

> **A runnable codification of Pāṇini’s Aṣṭādhyāyī — where every rule is an executable function, every step of prakriyā is traceable to a sūtra, and every reading is grounded in verified classical sources.**

---

## Overview

VyākaraṇaBandhu is a computational engine and verified digital record for Pāṇini’s *Aṣṭādhyāyī*. Rather than merely storing inflectional tables, it implements the grammar dynamically:

1. **Derive, do not tabulate**: Forms (e.g. *jayati* from *ji*) are not pre-stored. They are derived on-the-fly through ordered applications of sūtras (*it-saṃjñā*, *vikaraṇa* insertion, *guṇa*, *aya-ādeśa*, etc.).
2. **Bidirectional Prakriyā & Vyutpatti**:
   - **Forward**: Generate finite paradigms from dhātus according to *lakāra*, *puruṣa*, and *vacana*.
   - **Reverse (व्युत्पत्ति)**: Analyze inflected surface words back to their source roots in the *Dhātupāṭha* along with full sūtra-by-sūtra derivation traces.
3. **Multi-Witness Foundation**: Text collation across independent recensions (GRETIL, Vidyut) and cross-referencing commentaries (Mahābhāṣya with Kielhorn locators, Kāśikāvṛtti, Siddhāntakaumudī, Vasu).

For the project philosophy and architectural roadmap, see [`NORTH_STAR.md`](NORTH_STAR.md).

---

## Quick Start

### 1. Requirements

Python 3.10+ is recommended. Install required packages:

```bash
pip install -r requirements.txt
```

### 2. Running Derivations (व्युत्पत्ति)

Derive a verb paradigm forward from a root:
```bash
python -m src.astadhyayi.vyutpatti ji
```

Trace an inflected word backward to its root with full sūtra derivation steps:
```bash
python -m src.astadhyayi.vyutpatti jayati
```

### 3. Sandhi — every junction derived, every step cited

Join words and see, step by step, which sūtra of Pāṇini does what:
```bash
python cli.py --sandhi "iti ādi"          # → ityādi   (6.1.77 iko yaṇaci)
python cli.py --sandhi "rāmaḥ ca"         # → rāmaśca  (8.2.66, 8.3.15, 8.3.34, 8.4.40)
python cli.py --sandhi "deva-indra"       # a compound;  "pra|ejate" a preverb;  "ne~a" stem|affix
python cli.py --sandhi "इति आदि" --sandhi-json
```
Each step quotes the sūtra's own words from the corpus, says what was replaced by
what and why, lists the other sūtras it leans on, and names the rules it displaced
(1.4.2, 8.2.1). Where the grammar allows more than one result, every one is
derived. The same engine is the **Sandhi** tab of the web app and `/api/sandhi`.
How it works, and how to write a rule: [`src/astadhyayi/sandhi/README.md`](src/astadhyayi/sandhi/README.md).

### 4. CLI Sūtra Explorer

Inspect the codification status or examine a single sūtra:
```bash
# Sūtra summary and progress counts
python cli.py --astadhyayi

# Detailed view of a single sūtra with padaccheda, anuvṛtti, and notes
python cli.py --astadhyayi 1.1.9

# List open points under active investigation
python cli.py --astadhyayi open
```

### 5. Web Browser Interface

Launch the interactive local web app:
```bash
python server.py
```
Then navigate to:
- **Sandhi**: [http://localhost:8000/#sandhi](http://localhost:8000/#sandhi)
- **Aṣṭādhyāyī browser**: [http://localhost:8000/#astadhyayi](http://localhost:8000/#astadhyayi)
- **Classifier & Analysis**: [http://localhost:8000](http://localhost:8000)

---

## Repository Structure

```
├── NORTH_STAR.md          # Architectural decisions & codification standards
├── cli.py                 # Terminal interface for sūtras & subanta/tiṅanta analysis
├── server.py              # Local HTTP application server
├── src/
│   ├── astadhyayi/        # Core Pāṇinian rules, prakriyā, and vyutpatti engine
│   │   └── sandhi/        # The sandhi engine: junctions derived sūtra by sūtra
│   ├── chandas/           # Metric and phonemic scanning tools
│   ├── subanta_engine.py  # Nominal declension generator & analyzer
│   └── tinanta_engine.py  # Verbal conjugation engine
├── tests/                 # Comprehensive unit test suite
├── reference/             # Public domain collated mūla texts and lexicons
├── data/                  # Gold benchmark datasets and evaluation corpora
└── docs/notes/            # Historical research notes and discussions
```

---

## Running Tests

Run the test suite to verify the rule engine:
```bash
python -m unittest discover tests
```

---

## License

Unless otherwise noted, the source code is licensed under the Apache-2.0 / MIT license, and the classical public-domain textual references adhere to their respective source conditions (detailed in `reference/MANIFEST.json`).
