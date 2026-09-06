# Works still in copyright — not downloaded

These are central to the reading method but cannot be fetched. They must be
obtained legitimately and placed here by hand; the codification records keep a
`PENDING` slot for each until that happens, and the schema refuses to record a
`VERIFIED` reading without a locator.

Drop files into the folder named for each work. Scans, PDFs, or your own typed
notes are all fine — what matters is that a quotation can be checked.

## Translations and commentaries on the Aṣṭādhyāyī

| Work | Status | Notes |
|---|---|---|
| **Sumitra M. Katre**, *Aṣṭādhyāyī of Pāṇini* (1987) | **fetched but unusable** → `../translations/katre-astadhyayi.txt` | The archive.org item `katre-astadhyayi-of-panini` is unrestricted and the file is here, but the scan was OCR'd with a Devanāgarī model and the **English is destroyed throughout** — not one 4,000-character chunk in 582 reaches 70% Latin letters, median zero. Only the parenthesised sūtra numbers survive. An earlier note here said the English was usable; that was wrong, and checking it is what found out. Checked for a way out: the item's `_djvu.txt` is 4,139,661 bytes, byte-for-byte the size of the file we already hold, so it **is** this file, and no other text derivative exists. The only remaining route is re-OCRing `Katre_Astadhyayi_of_Panini.pdf` (50 MB) with a Latin model, which needs an OCR engine this project does not have. The records carry `UNREADABLE`, not `PENDING`, so this is not mistaken for unread. |
| **Rama Nath Sharma**, *The Aṣṭādhyāyī of Pāṇini*, 6 vols (1987–2003) | **borrowable** | Munshiram Manoharlal. archive.org item `astadhyayiofpani0001shar` (1987) is available through **controlled digital lending** — free account, borrow, read in-browser. Take notes into the record; do not bulk-download. |

## The Mahābhāṣya

| Work | Slot | Notes |
|---|---|---|
| **Kielhorn / Abhyankar**, BORI edition | `bori-mahabhasya/` | The underlying text is in `../mula/mahabhasya/`, and its GRETIL encoding already carries **Kielhorn volume/page/line** references — the same pagination this edition follows, so passages can be located before the volumes arrive. |
| **S. D. Joshi & J. A. F. Roodbergen**, *Vyākaraṇa-Mahābhāṣya* translation series | **borrowable** | Published in parts by adhyāya/āhnika (Poona / Sahitya Akademi). archive.org item `patanjalisvyakar0000sdjo` (1990) is available through controlled digital lending. Coverage is partial — check which part treats the sūtra in hand. |
| **James Benson**, *Patañjali's Remarks on Kāraka* (Kārakāhnika) | `benson/` — **not online** | Covers **1.4.23–55 only**, so records outside that range are `ABSENT`, not `PENDING`. Not on archive.org in any form; needs a library copy or purchase. Nothing before 1.4.23 is blocked on it. |

## How to get the two borrowable ones

Both Sharma and Joshi & Roodbergen are on archive.org under **controlled digital
lending** — one copy, one reader at a time, exactly like a library. A free
account lets you borrow and read in-browser. That is the legitimate route.

Read the passage, then put a short attributed quotation and your own summary
into the sūtra's `Reading` with a page locator. That is how the record is meant
to be filled: the schema wants a citation you can check, not a copy of the book.

**Not via shadow libraries.** Z-Library and its mirrors distribute these titles
without licence. Non-profit and research framing does not change that, and
open-sourcing this project raises the exposure rather than lowering it — a
public repository quoting Katre or Sharma at length is precisely the risk the
`PENDING`/locator discipline exists to avoid.

## Already available locally

Fetched by `tools/fetch_reference.py`, recorded in `../MANIFEST.json` with
SHA-256 for each file:

- Aṣṭādhyāyī sūtrapāṭha — two independent witnesses (GRETIL/Kāśikā; Vidyut)
- Patañjali's Mahābhāṣya, complete, with Kielhorn locators
- Nāgeśa's Paribhāṣenduśekhara
- Varadarāja's Laghusiddhāntakaumudī
- Dhātupāṭha, gaṇasūtras, Phiṭsūtras (Vidyut)
- Śrīśa Chandra Vasu's translation, 8 vols (1891–98), public domain

## Two cautions from checking what we downloaded

**Prefer Vidyut for the sūtra text.** Collating the two witnesses across all
3,983 sūtras leaves ~510 where they differ beyond sandhi and orthography, and
inspection shows many are data-entry errors on the GRETIL side — `duṭū` for
*cuṭū* (1.3.7), `pratyayasaya` for *pratyayasya* (1.3.6), `sasūpāṇām` for
*sarūpāṇām* (1.2.64), `prayarnaṃ` for *prayatnaṃ* (1.1.9). GRETIL remains
valuable as a second witness and for its hyphenated word-splits, but where the
two disagree, check rather than assume. Run
`python -c "from src.astadhyayi.corpus import collation_report; print(collation_report()['counts'])"`
for the current tally.

**Vasu's OCR mangles Sanskrit.** The 1891–98 scans OCR the English well but the
Devanāgarī and diacritics poorly — 1.1.1 comes out as *"n, it and ^jt are
called vriddhi"*. Use Vasu for the English rendering and his notes; take any
Sanskrit from the mūla files.
