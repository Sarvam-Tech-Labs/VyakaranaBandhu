# -*- coding: utf-8 -*-
"""
Merge the family modules and tests the implementers wrote in their isolated
workspaces into the real repository — and say what else they touched.

    python3 merge_families.py            # dry run: report only
    python3 merge_families.py --apply    # copy the permitted files

Every file an agent may edit is named below; anything ELSE under src/ or tests/
that differs from the real repository is reported: either the agent broke the
rules or the core needs a change the agent could not make.
"""
import filecmp, os, shutil, sys

REAL = "/workspaces/codespaces-blank/VyakaranaBandhu"
WSROOT = "/workspaces/codespaces-blank/sandhi_work/ws"
FAM = "src/astadhyayi/sandhi/families/"
FAMILIES = {
    "ac_yan_ayadi": [FAM + "ac_yan_ayadi.py", "tests/test_sandhi_ac_yan_ayadi.py"],
    "ac_ekadesa": [FAM + "ac_ekadesa.py", "tests/test_sandhi_ac_ekadesa.py"],
    "prakrtibhava": [FAM + "prakrtibhava.py", "src/astadhyayi/sandhi/infer.py", "tests/test_sandhi_prakrtibhava.py"],
    "hal_assimilation": [FAM + "hal_assimilation.py", "tests/test_sandhi_hal_assimilation.py"],
    "nasal_anusvara": [FAM + "nasal_anusvara.py", "tests/test_sandhi_nasal_anusvara.py"],
    "visarga_ru": [FAM + "visarga_ru.py", "tests/test_sandhi_visarga_ru.py"],
    "natva": [FAM + "natva.py", "tests/test_sandhi_natva.py"],
    "satva": [FAM + "satva.py", "tests/test_sandhi_satva.py"],
}
ALLOWED = {p for files in FAMILIES.values() for p in files}
IGNORE = {"__pycache__", ".git"}

def walk(root):
    for base, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in IGNORE]
        for name in files:
            if not name.endswith(".pyc"):
                yield os.path.relpath(os.path.join(base, name), root)

def main(apply, only=None):
    for family, files in FAMILIES.items():
        if only and family not in only: continue
        ws = os.path.join(WSROOT, family)
        print(f"\n[{family}]")
        for rel in files:
            src, dst = os.path.join(ws, rel), os.path.join(REAL, rel)
            if not os.path.exists(src):
                print(f"   MISSING  {rel}"); continue
            same = os.path.exists(dst) and filecmp.cmp(src, dst, shallow=False)
            print(f"   {'same   ' if same else 'CHANGED'}  {rel}  ({os.path.getsize(src)} bytes)")
            if apply and not same:
                shutil.copyfile(src, dst)
        strays = []
        for rel in walk(ws):
            if rel in ALLOWED or not rel.startswith(("src/", "tests/")): continue
            real = os.path.join(REAL, rel)
            if not os.path.exists(real): strays.append(f"NEW      {rel}")
            elif not filecmp.cmp(os.path.join(ws, rel), real, shallow=False): strays.append(f"DIFFERS  {rel}")
        if strays:
            print("   outside its remit:")
            for line in strays[:40]: print("     ", line)

if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    main("--apply" in sys.argv, set(args) or None)
