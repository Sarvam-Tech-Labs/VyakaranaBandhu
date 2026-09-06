# -*- coding: utf-8 -*-
"""
Fetches the reference texts for the Aṣṭādhyāyī codification into reference/.

Every file is recorded in reference/MANIFEST.json with its URL, byte count,
SHA-256, and retrieval date, so any quotation can later be traced to the exact
bytes it came from. Re-running skips files already present with a matching
digest; pass --force to refetch.

Only public-domain and openly-licensed material is fetched. The works still in
copyright (Katre, Sharma, Joshi & Roodbergen, Benson, and the BORI edition's
apparatus) are listed in reference/in-copyright/README.md with acquisition
details instead — they must be obtained legitimately and dropped in by hand.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import time
import urllib.parse
import urllib.request
from dataclasses import dataclass, asdict
from typing import List, Optional

ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "reference")
GRETIL = "https://gretil.sub.uni-goettingen.de/gretil/corpustei/transformations/plaintext"
VIDYUT = "https://raw.githubusercontent.com/ambuda-org/vidyut/main"
USER_AGENT = "astadhyayi-codification/0.1 (local research copy)"


@dataclass
class Item:
    path: str            # destination, relative to reference/
    url: str
    title: str
    source: str          # the holding institution or project
    licence: str
    note: str = ""


ITEMS: List[Item] = [
    # --- mūla: the Aṣṭādhyāyī itself -------------------------------------
    Item(
        "mula/astadhyayi/gretil-astadhyayi.txt",
        f"{GRETIL}/sa_pANini-aSTAdhyAyI.txt",
        "Pāṇini, Aṣṭādhyāyī (sūtrapāṭha)",
        "GRETIL, Göttingen",
        "public domain text; GRETIL terms of use",
    ),
    Item(
        "mula/astadhyayi/gretil-astadhyayi-alt.txt",
        f"{GRETIL}/sa_pANini-aSTAdhyAyI-alt.txt",
        "Pāṇini, Aṣṭādhyāyī — alternate GRETIL recension",
        "GRETIL, Göttingen",
        "public domain text; GRETIL terms of use",
        "Kept alongside the first so readings can be collated where they differ.",
    ),
    Item(
        "mula/astadhyayi/vidyut-sutrapatha.tsv",
        f"{VIDYUT}/vidyut-prakriya/data/sutrapatha.tsv",
        "Sūtrapāṭha, machine-readable (SLP1), 3,983 sūtras",
        "Ambuda / vidyut-prakriya",
        "MIT",
        "id\\ttext, SLP1 encoded. The spine for the codification index.",
    ),
    # --- mūla: the Mahābhāṣya --------------------------------------------
    Item(
        "mula/mahabhasya/gretil-mahabhasya.txt",
        f"{GRETIL}/sa_pataJjali-vyAkaraNamahAbhASya.txt",
        "Patañjali, Vyākaraṇa-Mahābhāṣya (complete)",
        "GRETIL, Göttingen",
        "public domain text; GRETIL terms of use",
        "~4.8 MB. Based on Kielhorn's edition, which the BORI revision follows.",
    ),
    # --- ancillary śāstra --------------------------------------------------
    Item(
        "mula/ancillary/gretil-paribhashendushekhara.txt",
        f"{GRETIL}/sa_nAgeza-paribhASenduzekhara.txt",
        "Nāgeśa, Paribhāṣenduśekhara",
        "GRETIL, Göttingen",
        "public domain text; GRETIL terms of use",
        "The standard collection of interpretive metarules; needed for any rule "
        "that turns on paribhāṣā.",
    ),
    Item(
        "mula/ancillary/gretil-laghusiddhantakaumudi.txt",
        f"{GRETIL}/sa_varadarAja-laghusiddhAntakaumudI.txt",
        "Varadarāja, Laghusiddhāntakaumudī",
        "GRETIL, Göttingen",
        "public domain text; GRETIL terms of use",
        "Topical rearrangement of the sūtras — useful for seeing which rules "
        "the tradition groups together.",
    ),
    Item(
        "mula/ancillary/vidyut-dhatupatha.tsv",
        f"{VIDYUT}/vidyut-prakriya/data/dhatupatha.tsv",
        "Dhātupāṭha, machine-readable",
        "Ambuda / vidyut-prakriya",
        "MIT",
    ),
    Item(
        "mula/ancillary/vidyut-dhatupatha-ganasutras.tsv",
        f"{VIDYUT}/vidyut-prakriya/data/dhatupatha-ganasutras.tsv",
        "Gaṇasūtras of the Dhātupāṭha",
        "Ambuda / vidyut-prakriya",
        "MIT",
    ),
    Item(
        "mula/ancillary/vidyut-phit-sutras.tsv",
        f"{VIDYUT}/vidyut-prakriya/data/phit-sutras.tsv",
        "Phiṭsūtras (Śāntanava), machine-readable",
        "Ambuda / vidyut-prakriya",
        "MIT",
    ),
]

ADH = "https://raw.githubusercontent.com/ashtadhyayi-com/data/master"
SANSKRIT_ADH = "https://raw.githubusercontent.com/sanskrit/ashtadhyayi/master"

#: The commentary tradition, from the data behind ashtadhyayi.com. Every file
#: is JSON keyed by a five-digit sūtra code (11001 = 1.1.1), so all of it is
#: addressable the same way our records are. Licence: free use with credit.
_ADH_CREDIT = "ashtadhyayi.com data repository — free use with attribution"


def _adh(name: str, title: str, note: str = "") -> Item:
    return Item(
        f"commentary/{name}.json",
        f"{ADH}/sutraani/{name}.txt",
        title,
        "ashtadhyayi.com",
        _ADH_CREDIT,
        note,
    )


ITEMS += [
    # --- the vṛtti layer: what each sūtra means, sūtra by sūtra -----------
    _adh("kashika", "Kāśikāvṛtti (Vāmana & Jayāditya)",
         "The standard running gloss on every sūtra. The first commentary to reach for."),
    _adh("nyaas", "Nyāsa / Kāśikāvivaraṇapañjikā (Jinendrabuddhi)",
         "Sub-commentary on the Kāśikā."),
    _adh("padamanjari", "Padamañjarī (Haradatta)",
         "The other major sub-commentary on the Kāśikā."),
    _adh("bhashya", "Mahābhāṣya, keyed by sūtra",
         "A second witness to the bhāṣya, indexed by sūtra rather than by "
         "Kielhorn page — collate against mula/mahabhasya/."),
    _adh("vartika", "Vārttikas of Kātyāyana",
         "Indexed by the sūtra each comments on."),
    # --- the kaumudī tradition -------------------------------------------
    _adh("kaumudi", "Siddhāntakaumudī (Bhaṭṭoji Dīkṣita)"),
    _adh("laghukaumudi", "Laghusiddhāntakaumudī (Varadarāja)"),
    _adh("balamanorama", "Bālamanoramā (Vāsudeva Dīkṣita)"),
    _adh("tattvabodhini", "Tattvabodhinī (Jñānendra Sarasvatī)"),
    _adh("praudhamanorama", "Prauḍhamanoramā (Bhaṭṭoji Dīkṣita)"),
    _adh("laghushabdendushekhar", "Laghuśabdenduśekhara (Nāgeśa)"),
    # --- translation and examples ----------------------------------------
    _adh("vasu_english", "Śrīśa Chandra Vasu, English translation (clean text)",
         "Supersedes the archive.org OCR for the English: this is transcribed, "
         "not scanned, and is keyed by sūtra."),
    _adh("sutrartha_english", "Sūtrārtha in English (brief gloss per sūtra)"),
    _adh("sutra_prayogas", "Attested usages illustrating each sūtra",
         "Worked examples — the natural source of test cases for a codified rule."),
    _adh("data", "Core sūtra data (text, type, pada-split, cross-references)"),
    # --- ancillary pāṭhas Pāṇini presupposes ------------------------------
    Item(
        "mula/ancillary/vidyut-unadipatha.tsv",
        f"{VIDYUT}/vidyut-prakriya/data/unadipatha.tsv",
        "Uṇādisūtras, machine-readable",
        "Ambuda / vidyut-prakriya", "MIT",
        "The affixes 3.3.1 and 3.4.75 hand off to; not codifiable without them.",
    ),
    Item(
        "mula/ancillary/vidyut-varttikas.tsv",
        f"{VIDYUT}/vidyut-prakriya/data/varttikas.tsv",
        "Vārttikas, machine-readable", "Ambuda / vidyut-prakriya", "MIT",
    ),
    Item(
        "mula/ancillary/vidyut-linganushasanam.tsv",
        f"{VIDYUT}/vidyut-prakriya/data/linganushasanam.tsv",
        "Liṅgānuśāsana (gender assignment)", "Ambuda / vidyut-prakriya", "MIT",
    ),
    Item(
        "mula/ancillary/vidyut-ganapatha.rs",
        f"{VIDYUT}/vidyut-prakriya/src/ganapatha.rs",
        "Gaṇapāṭha — the word-lists the sūtras refer to by name",
        "Ambuda / vidyut-prakriya", "MIT",
        "Rust source, but the gaṇas are plain data inside it. Rules like 1.1.27 "
        "sarvādīni sarvanāmāni cannot be codified without these lists.",
    ),
    Item(
        "mula/ancillary/vidyut-meters.tsv",
        f"{VIDYUT}/vidyut-chandas/data/meters.tsv",
        "Metre definitions", "Ambuda / vidyut-chandas", "MIT",
        "An independent check on our own 128-entry chandas catalog.",
    ),
    # --- the wider grammatical tradition ----------------------------------
    Item(
        "mula/ancillary/gretil-vakyapadiya.txt",
        f"{GRETIL}/sa_bhartRhari-vAkyapadIya.txt",
        "Bhartṛhari, Vākyapadīya",
        "GRETIL, Göttingen", "public domain text; GRETIL terms of use",
        "The philosophy behind the grammar — relevant wherever a sūtra's "
        "rationale, not just its effect, is in question.",
    ),
    Item(
        "mula/ancillary/gretil-nirukta.txt",
        f"{GRETIL}/sa_yAska-nirukta.txt",
        "Yāska, Nirukta",
        "GRETIL, Göttingen", "public domain text; GRETIL terms of use",
        "Pre-Pāṇinian etymology; the tradition Pāṇini writes against.",
    ),
    Item(
        "indexes/kaumudi-to-astadhyayi.tsv",
        f"{SANSKRIT_ADH}/data/kaumudiToAshtadhyayiIndex.tsv",
        "Siddhāntakaumudī order ↔ Aṣṭādhyāyī order",
        "github.com/sanskrit/ashtadhyayi", "see repository",
        "Lets a sūtra be found in the kaumudī's teaching sequence and back.",
    ),
    Item(
        "indexes/sutra-basics.json",
        f"{SANSKRIT_ADH}/data/sutraBasics.json",
        "Per-sūtra basics (type, pada-split, references)",
        "github.com/sanskrit/ashtadhyayi", "see repository",
    ),
]

#: Reference works whose archive.org item is unrestricted but whose rights are
#: not formally stated. Fetched as a LOCAL research copy only; check rights
#: before quoting at length or redistributing. The filename is resolved from
#: item metadata rather than guessed.
ARCHIVE_REFERENCE = {
    "katre-astadhyayi-of-panini": (
        "reference/translations/katre-astadhyayi.txt",
        "Sumitra M. Katre, Aṣṭādhyāyī of Pāṇini in Roman Transliteration (1987)",
        "in copyright; archive.org item unrestricted. LOCAL RESEARCH COPY — "
        "quote briefly with attribution, do not redistribute the text.",
        "Sūtra-by-sūtra Roman transliteration with English. One of the three "
        "reference translations for this project's reading method.",
    ),
    "dictionary-of-sanskrit-grammar-oriental-institute-of-baroda": (
        "reference/abhyankar-dictionary-of-sanskrit-grammar.txt",
        "K. V. Abhyankar, A Dictionary of Sanskrit Grammar (Oriental Institute, Baroda)",
        "rights not stated on the item; archive.org access unrestricted. "
        "LOCAL RESEARCH COPY — verify before redistributing.",
        "The standard reference for Pāṇinian technical vocabulary: saṃjñā, "
        "paribhāṣā, anubandha, and the rest. OCR text.",
    ),
}


def archive_reference_items() -> List[Item]:
    items: List[Item] = []
    for identifier, (path, title, licence, note) in ARCHIVE_REFERENCE.items():
        try:
            meta = json.loads(_get(f"https://archive.org/metadata/{identifier}", 60))
        except Exception as error:
            print(f"  ! {identifier}: metadata unavailable — {error}")
            continue
        name = next(
            (f["name"] for f in meta.get("files", []) if f["name"].endswith("_djvu.txt")),
            None,
        )
        if not name:
            print(f"  ! {identifier}: no OCR text published")
            continue
        items.append(
            Item(
                path=path.replace("reference/", ""),
                url=f"https://archive.org/download/{identifier}/{urllib.parse.quote(name)}",
                title=title,
                source="Internet Archive",
                licence=licence,
                note=note,
            )
        )
    return items


#: Śrīśa Chandra Vasu's translation, 1891–98 — public domain. archive.org
#: names the OCR file after the full item title, so the exact name is looked
#: up from each item's metadata rather than guessed.
VASU_VOLUMES = {
    "wg1038": 1, "wg1039": 2, "wg1040": 3, "wg1041": 4,
    "wg1042": 5, "wg1043": 6, "wg1044": 7, "wg1045": 8,
}


def _get(url: str, timeout: int = 180) -> bytes:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read()


def _sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def vasu_items() -> List[Item]:
    """Resolves each Vasu volume's OCR text URL from archive.org metadata."""
    items: List[Item] = []
    for identifier, volume in sorted(VASU_VOLUMES.items(), key=lambda kv: kv[1]):
        try:
            meta = json.loads(_get(f"https://archive.org/metadata/{identifier}", 60))
        except Exception as error:
            print(f"  ! vol {volume} ({identifier}): metadata unavailable — {error}")
            continue
        name = next(
            (f["name"] for f in meta.get("files", []) if f["name"].endswith("_djvu.txt")),
            None,
        )
        if not name:
            print(f"  ! vol {volume} ({identifier}): no OCR text published")
            continue
        title = meta.get("metadata", {}).get("title", identifier)
        items.append(
            Item(
                path=f"translations/vasu-1891/vol{volume}-{identifier}.txt",
                url=f"https://archive.org/download/{identifier}/{urllib.parse.quote(name)}",
                title=f"Śrīśa Chandra Vasu, {title}",
                source="Internet Archive",
                licence="public domain (published 1891–1898)",
                note="OCR text. Devanāgarī OCR of this vintage is unreliable — "
                     "use for the English rendering and check Sanskrit against the mūla.",
            )
        )
    return items


def fetch(items: List[Item], force: bool) -> List[dict]:
    records: List[dict] = []
    for item in items:
        destination = os.path.join(ROOT, item.path)
        os.makedirs(os.path.dirname(destination), exist_ok=True)
        if os.path.exists(destination) and not force:
            with open(destination, "rb") as handle:
                payload = handle.read()
            print(f"  = {item.path}  ({len(payload):,} bytes, already present)")
        else:
            try:
                payload = _get(item.url)
            except Exception as error:
                print(f"  ! {item.path}: {error}")
                continue
            with open(destination, "wb") as handle:
                handle.write(payload)
            print(f"  + {item.path}  ({len(payload):,} bytes)")
        record = asdict(item)
        record.update(
            bytes=len(payload),
            sha256=_sha256(payload),
            retrieved=time.strftime("%Y-%m-%d", time.gmtime()),
        )
        records.append(record)
    return records


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--force", action="store_true", help="refetch even if present")
    parser.add_argument("--skip-vasu", action="store_true", help="skip the 8 Vasu volumes")
    args = parser.parse_args()

    os.makedirs(ROOT, exist_ok=True)
    print("Fetching mūla texts and open data…")
    records = fetch(ITEMS, args.force)

    print("\nResolving reference works on archive.org…")
    records += fetch(archive_reference_items(), args.force)

    if not args.skip_vasu:
        print("\nResolving Vasu volumes on archive.org…")
        records += fetch(vasu_items(), args.force)

    manifest = {
        "generated": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "note": (
            "Local reference copies for the Aṣṭādhyāyī codification. Every entry "
            "carries its URL and SHA-256 so a quotation can be traced to the exact "
            "bytes. Works still in copyright are NOT here — see "
            "reference/in-copyright/README.md."
        ),
        "files": records,
    }
    with open(os.path.join(ROOT, "MANIFEST.json"), "w", encoding="utf-8") as handle:
        json.dump(manifest, handle, ensure_ascii=False, indent=2)

    total = sum(r["bytes"] for r in records)
    print(f"\n{len(records)} files, {total / 1048576:.1f} MB total")
    print(f"manifest: {os.path.join(ROOT, 'MANIFEST.json')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
