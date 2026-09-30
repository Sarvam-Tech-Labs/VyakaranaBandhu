# -*- coding: utf-8 -*-
"""
Validator for the sandhi catalogue and gold files under data/sandhi/.

Run from the repository root:

    python3 tools/sandhi_data_validate.py data/sandhi/gold/*.gold.json data/sandhi/catalogue/*.catalogue.json

It exits non-zero and prints every problem it finds.  A file with problems is not
finished.  The point of the checks is that nothing may be *plausible but unsourced*:

  * every sūtra id must exist in the Vidyut sūtrapāṭha and its text must be copied exactly
  * every gold case must carry a source whose quote is a VERBATIM substring (after
    whitespace normalisation) of the on-disk source it names
  * every word / output must use only the project's IAST alphabet
"""
import json
import os
import re
import sys
import unicodedata

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, REPO)
from src.astadhyayi import corpus  # noqa: E402

LAGHU_TXT = os.path.join(
    REPO, "reference", "mula", "ancillary", "gretil-laghusiddhantakaumudi.txt")

SUTRAS = corpus.load_vidyut_sutrapatha()

ALLOWED = set(
    "aāiīuūṛṝḷḹeo"                # vowels (ai, au are digraphs of these letters)
    "kgṅcjñṭḍṇtdnpbmyrlvśṣshḥṃ"   # consonants + anusvāra + visarga
    "ẖḫ"                          # jihvāmūlīya / upadhmānīya
    "'’ -̐"                  # avagraha, space, hyphen, combining candrabindu
)

FAMILIES = {
    "ac_yan_ayadi", "ac_ekadesa", "prakrtibhava", "hal_assimilation",
    "nasal_anusvara", "visarga_ru", "meta_ordering", "internal",
}
TIERS = {"core", "extended", "internal", "vedic", "support"}
KINDS = {"vidhi", "niyama", "nisedha", "paribhasa", "adhikara", "samjna",
         "apavada", "atidesa", "nipatana", "varttika"}
BOUNDARIES = {"pada", "samasa", "upasarga", "anga"}
CONFIDENCE = {"certain", "probable", "uncertain"}
SOURCE_WORKS = {
    "laghukaumudi_text", "kashika", "kaumudi", "laghukaumudi", "balamanorama",
    "tattvabodhini", "nyaas", "padamanjari", "praudhamanorama", "bhashya",
    "vasu_english", "sutrartha_english", "vartika", "tests_cases", "dataset",
    "paribhashendushekhara",
}


def norm_ws(s):
    return re.sub(r"\s+", " ", unicodedata.normalize("NFC", s)).strip()


def strip_markup(s):
    # commentary files mark cross references as <<sutra text>> [[6.1.77]]
    s = re.sub(r"<<|>>", "", s)
    s = re.sub(r"\[\[[^\]]*\]\]", "", s)
    return s


_laghu_cache = {}


def source_text(work, sutra_id):
    """The on-disk text a quote must be found in, or None if the work is unknown."""
    if work == "laghukaumudi_text":
        if "t" not in _laghu_cache:
            _laghu_cache["t"] = norm_ws(open(LAGHU_TXT, encoding="utf-8").read())
        return _laghu_cache["t"]
    if work in {"tests_cases", "dataset", "paribhashendushekhara"}:
        return None  # checked by hand by the auditor
    try:
        text = corpus.commentary_on(sutra_id, work)
    except Exception:
        text = None
    return norm_ws(strip_markup(text)) if text else None


def check_iast(label, word, errors):
    bad = sorted({c for c in unicodedata.normalize("NFC", word) if c not in ALLOWED})
    if bad:
        errors.append(f"{label}: characters outside the project IAST alphabet: {bad!r} in {word!r}")


def check_catalogue(path, data, errors):
    if not isinstance(data, list) or not data:
        errors.append(f"{path}: catalogue must be a non-empty JSON list")
        return
    seen = set()
    for i, e in enumerate(data):
        where = f"{path}[{i}] id={e.get('id')}"
        for key in ("id", "text_iast", "family", "tier", "kind", "effect", "conditions",
                    "exceptions_and_blockers", "overrides", "overridden_by",
                    "ordering_notes", "varttikas", "optional", "vedic_only", "examples"):
            if key not in e:
                errors.append(f"{where}: missing field {key!r}")
        sid = e.get("id")
        if sid in seen:
            errors.append(f"{where}: duplicate id")
        seen.add(sid)
        if sid not in SUTRAS:
            errors.append(f"{where}: not a sūtra id in the Vidyut corpus")
        elif e.get("text_iast") != SUTRAS[sid].text:
            errors.append(f"{where}: text_iast {e.get('text_iast')!r} != corpus {SUTRAS[sid].text!r}")
        if e.get("family") not in FAMILIES:
            errors.append(f"{where}: family {e.get('family')!r} not in {sorted(FAMILIES)}")
        if e.get("tier") not in TIERS:
            errors.append(f"{where}: tier {e.get('tier')!r} not in {sorted(TIERS)}")
        if e.get("kind") not in KINDS:
            errors.append(f"{where}: kind {e.get('kind')!r} not in {sorted(KINDS)}")
        for key in ("overrides", "overridden_by"):
            for other in e.get(key) or []:
                oid = other if isinstance(other, str) else other.get("id")
                if oid not in SUTRAS:
                    errors.append(f"{where}: {key} names unknown sūtra {oid!r}")
        for b in e.get("exceptions_and_blockers") or []:
            if not isinstance(b, dict) or b.get("id") not in SUTRAS:
                errors.append(f"{where}: exceptions_and_blockers entry needs a valid 'id': {b!r}")
        for v in e.get("varttikas") or []:
            if not isinstance(v, dict) or not v.get("text") or not v.get("source"):
                errors.append(f"{where}: each varttika needs 'text' and 'source': {v!r}")


def check_gold(path, data, errors):
    if not isinstance(data, list) or not data:
        errors.append(f"{path}: gold must be a non-empty JSON list")
        return
    seen = set()
    for i, c in enumerate(data):
        where = f"{path}[{i}] id={c.get('id')}"
        for key in ("id", "family", "input", "boundary", "outputs", "sutras", "source",
                    "confidence", "notes"):
            if key not in c:
                errors.append(f"{where}: missing field {key!r}")
        if c.get("id") in seen:
            errors.append(f"{where}: duplicate case id")
        seen.add(c.get("id"))
        if c.get("family") not in FAMILIES:
            errors.append(f"{where}: family {c.get('family')!r} not in {sorted(FAMILIES)}")
        words = c.get("input")
        if not isinstance(words, list) or not words or not all(isinstance(w, str) and w for w in words):
            errors.append(f"{where}: input must be a non-empty list of non-empty strings")
            words = []
        for w in words:
            check_iast(where + " input", w, errors)
        outs = c.get("outputs")
        if not isinstance(outs, list) or not outs or not all(isinstance(o, str) and o for o in outs):
            errors.append(f"{where}: outputs must be a non-empty list of strings")
            outs = []
        for o in outs:
            check_iast(where + " output", o, errors)
        if c.get("boundary") not in BOUNDARIES:
            errors.append(f"{where}: boundary {c.get('boundary')!r} not in {sorted(BOUNDARIES)}")
        if c.get("confidence") not in CONFIDENCE:
            errors.append(f"{where}: confidence {c.get('confidence')!r} not in {sorted(CONFIDENCE)}")
        for s in c.get("sutras") or []:
            if s not in SUTRAS:
                errors.append(f"{where}: sutras names unknown id {s!r}")
        flags = c.get("flags")
        if flags is not None:
            if not isinstance(flags, dict):
                errors.append(f"{where}: flags must be an object {{word_index: [flag, ...]}}")
            else:
                for k, v in flags.items():
                    if not (k.isdigit() and int(k) < len(words)):
                        errors.append(f"{where}: flags key {k!r} is not a valid word index")
                    if not isinstance(v, list) or not all(isinstance(x, str) for x in v):
                        errors.append(f"{where}: flags[{k}] must be a list of strings")
        for step in c.get("derivation") or []:
            if not isinstance(step, dict) or step.get("sutra") not in SUTRAS:
                errors.append(f"{where}: derivation step needs a valid 'sutra': {step!r}")
        src = c.get("source")
        if not isinstance(src, dict):
            errors.append(f"{where}: source must be an object")
            continue
        work, quote, sid = src.get("work"), src.get("quote"), src.get("sutra")
        if work not in SOURCE_WORKS:
            errors.append(f"{where}: source.work {work!r} not in {sorted(SOURCE_WORKS)}")
            continue
        if not quote or not src.get("locator"):
            errors.append(f"{where}: source needs a non-empty 'quote' and 'locator'")
            continue
        if work in {"tests_cases", "dataset", "paribhashendushekhara"}:
            continue
        if work != "laghukaumudi_text" and sid not in SUTRAS:
            errors.append(f"{where}: source.sutra {sid!r} is not a valid sūtra id")
            continue
        text = source_text(work, sid)
        if text is None:
            errors.append(f"{where}: no on-disk text for work={work!r} sutra={sid!r} — the quote cannot be verified")
            continue
        q = norm_ws(strip_markup(quote))
        if q not in text:
            errors.append(f"{where}: quote is NOT a verbatim substring of {work} "
                          f"(sutra {sid}): {quote[:80]!r}")


def validate_paths(paths, quiet=True):
    """Every problem found in the named files, as strings; [] when sound."""
    errors = []
    for path in paths:
        try:
            data = json.load(open(path, encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{path}: cannot read as JSON: {exc}")
            continue
        if path.endswith(".catalogue.json"):
            check_catalogue(path, data, errors)
        elif path.endswith(".gold.json") or path.endswith(".puzzles.json"):
            check_gold(path, data, errors)
        else:
            errors.append(f"{path}: name must end in .catalogue.json, .gold.json or .puzzles.json")
        if not quiet:
            print(f"{path}: {len(data) if isinstance(data, list) else '?'} entries")
    return errors


def main(paths):
    errors = validate_paths(paths, quiet=False)
    if errors:
        print(f"\n{len(errors)} PROBLEM(S):")
        for e in errors[:200]:
            print("  -", e)
        if len(errors) > 200:
            print(f"  ... and {len(errors) - 200} more")
        sys.exit(1)
    print("OK — no problems found")


if __name__ == "__main__":
    main(sys.argv[1:])
