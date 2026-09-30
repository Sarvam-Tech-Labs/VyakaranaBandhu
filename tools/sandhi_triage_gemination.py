# -*- coding: utf-8 -*-
"""
First-pass triage of gold mismatches: the ones whose *only* difference from the
gold is gemination — the number of identical consonants stacked (kk/k, yy/y,
ddh/dh …), which is where optional doubling (8.4.46–47 and their neighbours)
shows up — or a missing ṇatva/ṣatva (the gold has ṇ/ṣ where the engine has n/s).

The classification is mechanical and claims only what code can prove. Two
classes are recognised — gemination, and a missing ṇatva/ṣatva (the gold has ṇ or
ṣ where the engine leaves n or s, nothing else differing):

* verdict ``extra``   (strict row; the engine offers more forms than the gold
  lists): every extra form equals a listed form once gemination is collapsed
  → kind ``underspecified``;
* verdict ``missing`` (the gold lists a form the engine does not produce): every
  missing form equals a produced form once gemination is collapsed →
  ``scope`` if the row is one word (the engine acts at junctions, so the
  inside of a single input word is not its business), else ``engine-gap``.

The reasons say "differs only in gemination"; they do not say the gold is right
or wrong. Read them as leads, not verdicts. Anything not provable this way is left
for a person.

    python3 tools/sandhi_triage_gemination.py            # report only
    python3 tools/sandhi_triage_gemination.py --apply    # merge into
                                                         # data/sandhi/known_mismatches.json
"""

from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.astadhyayi.sandhi import harness  # noqa: E402

KNOWN = "data/sandhi/known_mismatches.json"
_CONSONANTS = "kgcjñṭḍṇtdnpbmyrlvśṣshṅ"
_GEMINATE = re.compile(f"([{_CONSONANTS}])\\1")
#: (what the engine leaves, what the gold has) — the whole of a ṇatva / ṣatva
_RETROFLEX = {("n", "ṇ"): "ṇatva (8.4.1–39)", ("s", "ṣ"): "ṣatva (8.3.55–119)"}


#: A form's last letter voiced or unvoiced — what a pause does (8.2.39, and the
#: option of 8.4.56 to unvoice it again).
_PAUSAL = ({"t", "d"}, {"k", "g"}, {"ṭ", "ḍ"}, {"p", "b"}, {"c", "j"})


def variant_kind(a: str, b: str):
    """Why `a` and `b` are one form's variants, if only that differs (else None):
    the very last letter voiced/unvoiced, or one m against one ṃ."""
    if a == b or len(a) != len(b):
        return None
    diffs = [(i, x, y) for i, (x, y) in enumerate(zip(a, b)) if x != y]
    if len(diffs) != 1:
        return None
    i, x, y = diffs[0]
    if i == len(a) - 1 and {x, y} in _PAUSAL:
        return "the last letter voiced or voiceless (pausal, 8.2.39 / 8.4.56)"
    if {x, y} == {"m", "ṃ"}:
        return "m against ṃ at one place (cf. 8.4.59 vā padāntasya)"
    return None


def retroflexed(expected: str, got: str):
    """The set of ṇatva/ṣatva kinds if `expected` is `got` with only n→ṇ / s→ṣ."""
    if len(expected) != len(got) or expected == got:
        return None
    kinds = set()
    for g, e in zip(got, expected):
        if g != e:
            if (g, e) not in _RETROFLEX:
                return None
            kinds.add(_RETROFLEX[(g, e)])
    return kinds


def collapse(form: str) -> str:
    """The form with each run of one consonant reduced to a single one."""
    return _GEMINATE.sub(r"\1", _GEMINATE.sub(r"\1", form))


def classify(row, result):
    """(kind, reason) if the mismatch is provably only gemination, else None."""
    if result.ok or result.verdict not in ("extra", "missing") \
            or row.get("confidence") == "uncertain":
        return None
    expected, got = set(result.expected), set(result.got)
    if result.verdict == "extra":
        extras = got - expected
        if extras and {collapse(f) for f in extras} <= {collapse(f) for f in expected}:
            return ("underspecified",
                    "The gold lists one form and the engine also offers "
                    + ", ".join(sorted(extras))
                    + ": each differs from a listed form only in gemination "
                      "(optional doubling, 8.4.46–47); the row does not say "
                      "whether the doubled forms are allowed.")
        if extras and all(any(variant_kind(e, x) for x in expected) for e in extras):
            why = {variant_kind(e, x) for e in extras for x in expected} - {None}
            return ("underspecified",
                    "The gold lists one form and the engine also offers "
                    + ", ".join(sorted(extras)) + ", which differs from a "
                    "listed form only in " + " and in ".join(sorted(why))
                    + "; the row does not say whether that variant is allowed.")
        return None
    absent = expected - got
    if absent:
        kinds, ok = set(), True
        for form in absent:
            found = [retroflexed(form, g) for g in got]
            found = [k for k in found if k]
            if not found:
                ok = False
                break
            kinds |= found[0]
        if ok:
            return ("engine-gap",
                    "The gold has " + ", ".join(sorted(absent)) + " where the "
                    "engine leaves n or s: the only difference is the missing "
                    + " and ".join(sorted(kinds)) + ", which the natva/satva "
                    "families (unmerged drafts) are to supply.")
    if absent and {collapse(f) for f in absent} <= {collapse(f) for f in got}:
        words = len(row.get("input") or ())
        forms = ", ".join(sorted(absent))
        if words == 1:
            return ("scope",
                    f"The gold lists {forms}, which differs from what the engine "
                    "derives only in gemination; the row is a single word and "
                    "the engine acts at junctions, not inside a finished word "
                    "(optional doubling, 8.4.46–47).")
        return ("engine-gap",
                f"The gold lists {forms}, which differs from what the engine "
                "produces only in gemination: the engine does not offer this "
                "variant of the optional doubling (8.4.46–47) at this junction.")
    if absent and all(any(variant_kind(m, g) for g in got) for m in absent):
        why = {variant_kind(m, g) for m in absent for g in got} - {None}
        return ("engine-gap",
                "The gold lists " + ", ".join(sorted(absent)) + ", which differs "
                "from what the engine produces only in " + " and in ".join(sorted(why))
                + "; the engine does not offer this variant.")
    return None


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--apply", action="store_true")
    args = ap.parse_args()
    known = {}
    if os.path.exists(KNOWN):
        with open(KNOWN, encoding="utf-8") as handle:
            known = json.load(handle)
    found, unresolved = {}, 0
    for path in sorted(glob.glob("data/sandhi/gold/*.gold.json")):
        for row in harness.load_gold(path):
            result = harness.run_case(row)
            if result.ok or row.get("confidence") == "uncertain" or row["id"] in known:
                continue
            verdict = classify(row, result)
            if verdict:
                found[row["id"]] = {"kind": verdict[0], "reason": verdict[1]}
            else:
                unresolved += 1
    by_kind = {}
    for entry in found.values():
        by_kind[entry["kind"]] = by_kind.get(entry["kind"], 0) + 1
    print(f"provably gemination-only: {len(found)} {by_kind}; "
          f"left for a person: {unresolved}; already recorded: {len(known)}")
    if args.apply and found:
        known.update(found)
        with open(KNOWN, "w", encoding="utf-8") as handle:
            json.dump(dict(sorted(known.items())), handle, ensure_ascii=False,
                      indent=1)
            handle.write("\n")
        print(f"wrote {KNOWN} ({len(known)} entries)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
