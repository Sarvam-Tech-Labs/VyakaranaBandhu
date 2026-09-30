import sys; sys.path.insert(0,'.')
from src.astadhyayi.sandhi import sandhi
def show(t, **kw):
    r=sandhi(t, **kw)
    outs=[]
    for o in r.outcomes:
        outs.append((o.surface, "→".join(s.sutra+("*" if s.declined else "") for s in o.steps)))
    print(f"{t!r:45}", outs)
for t in """khaṭvā indra
khaṭvā indraḥ
gaṅgā udakam
kṛṣṇa aikya
kṛṣṇa aikatva
upa|eti{dhatu:i}
upa|edhate{dhatu:edh}
pra|ṛcchati
pra|ejate
upa|oṣati
śiva om{nipata}
śiva ehi{ang}
daṇḍa-agram
daṇḍa agram
dadhi indraḥ
madhu udakam
hotṛ ṛkāraḥ
hare ava
paca~anti
tava ṛkāraḥ
tava ḷkāraḥ
upa indra
śiva ehi
śivāya om{nipata}
śivāya om
akṣa-ūhinī
pra-ūḍha
sukha{trtiya}-ṛta
paramaṃ-ṛta
viṣṇu udaya
daitya ari
śrī īśa
kṛṣṇa autkaṇṭhya
deva aiśvarya
gaṅgā ogha
pra|ṛṇa
vatsatara-ṛṇa
""".strip().splitlines():
    show(t)
