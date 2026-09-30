import sys, itertools, time; sys.path.insert(0,'.')
from src.astadhyayi.sandhi import sandhi
from src.astadhyayi import corpus
known = corpus.load_vidyut_sutrapatha()
V = ["a","ā","i","ī","u","ū","ṛ","ṝ","ḷ","e","ai","o","au"]
lefts = [f"k{v}" for v in V] + V
rights = [f"{v}k" for v in V] + V
bounds = ["", "|", "-", "~"]
lflags = ["", "{upasarga}", "{aat}", "{avyakta}", "{trtiya}", "{samprasarana}", "{ang}"]
rflags = ["", "{dhatu}", "{dhatu:i}", "{dhatu:edh}", "{nipata}", "{ang}", "{uth}", "{subanta,dhatu}", "{sup:jas}", "{sup:śas}", "{sup:am}", "{sup:au}", "{sup:ṅas}", "{sup:ṅasi}", "{sup:ṅe}", "{avyakta,amredita}", "{aniyoga}", "{krdanta}", "{stem:ūṭh}"]
n=0; bad=[]; t0=time.time(); maxsteps=0; maxms=0
for l, r, b, lf, rf in itertools.product(lefts[::2] if False else lefts, rights, bounds, lflags, rflags):
    if (lf and l[0] != "k" and False): continue
    # keep the space manageable: flags only on some combos
    if (lf and rf) : continue
    sep = {"": " ", "|": "|", "-": "-", "~": "~"}[b]
    text = f"{l}{lf}{sep}{r}{rf}"
    t1=time.perf_counter()
    try:
        res = sandhi(text)
    except Exception as e:
        bad.append((text, repr(e))); continue
    maxms=max(maxms,(time.perf_counter()-t1)*1000)
    n+=1
    for o in res.outcomes:
        maxsteps=max(maxsteps,len(o.steps))
        if o.stopped != "no rule applies": bad.append((text,o.stopped))
        for s in o.steps:
            for sid in [s.sutra]+[v.sutra for v in s.detail.via]+[a.sutra for a in s.against]:
                if sid not in known: bad.append((text,"unknown "+sid))
print(n,"runs",round(time.time()-t0),"s; max steps",maxsteps,"max ms",round(maxms),"; problems:",len(bad))
for b in bad[:30]: print(b)
