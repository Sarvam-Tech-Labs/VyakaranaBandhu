# The extracted gold, run through the engine twice: as written, and with the flags this
# family reads added for the cases whose sources name a condition the closed vocabulary
# has no word for (the augment, the imitation, a subanta dhātu ...). Orientation only.
import json, sys
sys.path.insert(0, ".")
from src.astadhyayi.sandhi import harness

GOLD = "/workspaces/codespaces-blank/sandhi_work/scratch/sandhi_data/ac_ekadesa.gold.json"
cases = harness.load_gold(GOLD)
EXTRA = {}
def add(ids, word, *flags):
    for i in ids:
        EXTRA.setdefault(f"ac_ekadesa-{i:03d}", {}).setdefault(str(word), []).extend(flags)
add(range(71, 76), 0, "aat"); add([76, 77], 1, "aat"); add([76], 2, "sup:ṅe"); add([77], 2, "sup:ṅas")
add([51], 1, "stem:īra"); add([52], 1, "stem:īrin"); add([56, 57], 1, "krdanta")
add([60, 61], 0, "trtiya"); add(range(65, 71), 1, "stem:ṛṇa")
add([86, 87, 88, 102, 103, 104], 1, "subanta")
add([89, 91, 93], 1, "stem:am")
add([110], 0, "keśaveśe"); add([112], 0, "paśupakṣiṇoḥ")
add([113, 114, 115], 1, "aniyoga"); add([119], 1, "stem:oṣṭha")
add([123, 128], 1, "nipata")
add([149, 150, 151, 152, 155, 156, 158], 0, "avyakta"); add([157], 0, "avyakta"); add([157], 1, "avyakta", "amredita")
add([159, 160], 0, "avyakta"); add([159, 160], 1, "amredita", "dac")
def adapted(c):
    c = dict(c)
    flags = {k: list(v) for k, v in (c.get("flags") or {}).items()}
    for k, v in EXTRA.get(c["id"], {}).items():
        flags.setdefault(k, []).extend(v)
    c["flags"] = flags
    return c
for label, rows in (("as written", cases), ("with the flags this family reads", [adapted(c) for c in cases])):
    s = harness.evaluate(rows)
    print(label, "->", s.matched, "of", s.total)
    if label != "as written":
        for r in s.misses:
            print(f"  [{r.verdict}] {r.id}: {' + '.join(r.words)}  expected {list(r.expected)}  engine {list(r.got)}  steps {'→'.join(r.steps)}")
