# Every Devanagari quotation in the module (between * *), checked against the on-disk commentaries.
import re, sys
sys.path.insert(0, '.')
from src.astadhyayi import corpus

def norm(t):
    t = re.sub(r"<<|>>", "", t); t = re.sub(r"\[\[[^\]]*\]\]", "", t)
    t = t.replace("॥", " ").replace("।", " ").replace("॰", " ")
    return re.sub(r"\s+", " ", t).strip()

def squeeze(t):
    return re.sub(r"[\s]+", "", norm(t))

sutras = [f"6.1.{n}" for n in range(84, 114)] + [f"1.1.{n}" for n in list(range(1, 4)) + list(range(50, 72))]
allc = {}
for s in sutras:
    for work, txt in corpus.all_commentary_on(s).items():
        allc.setdefault(s, {})[work] = squeeze(txt)
for s in sutras:
    for v in corpus.varttikas_on(s):
        allc.setdefault(s, {})["varttika"] = allc.get(s, {}).get("varttika", "") + squeeze(v.text)
haystack = "".join(t for d in allc.values() for t in d.values())

src = open("src/astadhyayi/sandhi/families/ac_ekadesa.py", encoding="utf-8").read()
dev = re.compile(r"[\u0900-\u097F]")
bad = []
n = 0
seen=set()
for m in re.finditer(r"\*([^*\n][^*]*?)\*", src):
    q = m.group(1)
    if not dev.search(q): continue
    for p in re.split(r"\s*(?:…|\.\.\.|—|;|,)\s*", q):
        runs = re.findall(r"[\u0900-\u097F](?:[\u0900-\u097F\s\u200c\u200d?]*[\u0900-\u097F])?", p)
        for text in runs:
            text = text.replace("?", " ")
            if len(squeeze(text)) < 10 or text in seen: continue
            seen.add(text)
            n += 1
            if squeeze(text) not in haystack:
                bad.append(text)
print(n, "quoted pieces;", len(bad), "not found verbatim")
for b in bad: print("  NOT FOUND:", b)
