# Copy validated gold + catalogues into the repo, adding the flags each source implies.
import json, os, re, shutil, sys
SD = "/workspaces/codespaces-blank/sandhi_work/scratch/sandhi_data"
REPO = "/workspaces/codespaces-blank/VyakaranaBandhu"
os.makedirs(f"{REPO}/data/sandhi/gold", exist_ok=True); os.makedirs(f"{REPO}/data/sandhi/catalogue", exist_ok=True)

def spec_from_adapt(path):
    """Read the EXTRA table out of the agent's gold_adapt.py (its add(...) calls)."""
    src = open(path, encoding="utf-8").read()
    extra = {}
    def add(ids, word, *flags):
        for i in ids:
            extra.setdefault(f"ac_ekadesa-{i:03d}", {}).setdefault(str(word), []).extend(flags)
    body = src.split("EXTRA = {}")[1].split("def adapted")[0]
    body = re.sub(r"^def add\(.*?\n(?=\S)", "", body, flags=re.S | re.M)
    exec(body, {"add": add, "range": range})
    return extra

EXTRA = {"ac_ekadesa": spec_from_adapt("/workspaces/codespaces-blank/sandhi_work/ws/ac_ekadesa/.work/gold_adapt.py"),
         "ac_yan_ayadi": {}, "prakrtibhava": {}}
def y(ids, word, *flags):
    for i in ids:
        EXTRA["ac_yan_ayadi"].setdefault(f"ac_yan_ayadi-{i:03d}", {}).setdefault(str(word), []).extend(flags)
y([45], 0, "adhvaparimana"); y([49], 1, "tannimitta"); y([52, 53], 0, "shakyartha"); y([56], 0, "krayartha"); y([59], 0, "stri")
y(range(129, 140), 0, "abhyasa")

for fam in ("ac_ekadesa", "ac_yan_ayadi", "prakrtibhava"):
    gold = json.load(open(f"{SD}/{fam}.gold.json", encoding="utf-8"))
    added = 0
    for c in gold:
        extra = EXTRA[fam].get(c["id"])
        if extra:
            flags = {k: list(v) for k, v in (c.get("flags") or {}).items()}
            for k, v in extra.items():
                for f in v:
                    if f not in flags.setdefault(k, []): flags[k].append(f)
            c["flags"] = flags
            c["flags_added"] = sorted({f for v in extra.values() for f in v})
            added += 1
    json.dump(gold, open(f"{REPO}/data/sandhi/gold/{fam}.gold.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    shutil.copyfile(f"{SD}/{fam}.catalogue.json", f"{REPO}/data/sandhi/catalogue/{fam}.catalogue.json")
    print(fam, len(gold), "cases;", added, "with flags added")
