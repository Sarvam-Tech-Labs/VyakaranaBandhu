# -*- coding: utf-8 -*-
import sys, os, json, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
from qc import qc_dataset

SRC = RAW + '/performance__sandhi-joiner-benchmark/release/datasets/lsk_gold_battery.jsonl'
URL = 'https://github.com/performance/sandhi-joiner-benchmark/blob/ba5cbfc481ff2e3abb34707147c44e3f5ab35746/release/datasets/lsk_gold_battery.jsonl'
LIC = 'MIT (repo LICENSE covers benchmark/ and release/; data curated by the repo author from public-domain LSK examples)'
ds = 'lsk-gold-battery'
rows, dropped = [], collections.Counter()
for i, line in enumerate(open(SRC, encoding='utf-8'), 1):
    r = json.loads(line)
    inp = [slp12iast(x) for x in r['pre_sandhi']]
    out = slp12iast(r['post_sandhi'])
    reason = malformed_reason(inp, out)
    if reason:
        dropped[reason] += 1
        continue
    topic = r['topic']
    head = topic.split('/')[0]
    stype = head if head in ('vowel', 'consonant', 'visarga', 'anusvara') else ('none' if head == 'prakrtibhava' else 'unknown')
    nt = ['LSK battery id %s' % r['id'], 'dataset topic=%s' % topic, 'dataset type=%s' % r['type'],
          'sutra name: %s (%s)' % (slp12iast(r['sutra_name_slp1']), r['sutra_name_dev']), 'dataset note: %s' % r['notes'],
          'source label: %s' % r['source']]
    if r['type'] == 'pragrhya' or head == 'prakrtibhava':
        nt.append('prakrtibhava: no sandhi is applied; output keeps the two words separated by a space')
    if r['type'] == 'apavada':
        nt.append('apavada = exception to a more general rule')
    if r['id'] in ('LSK048', 'LSK049'):
        nt.append('LSK048 and LSK049 are the two optional outputs (vA) of the same input')
    if len(inp) == 1:
        nt.append('single input word: pausal/avasana form test, not a junction')
    rows.append(make_row(ds, len(rows) + 1, inp, out, sandhi_type=stype, rule=r['sutra'], boundary='unknown', vedic=False,
                         src_file='performance__sandhi-joiner-benchmark/release/datasets/lsk_gold_battery.jsonl', locator='line %d (%s)' % (i, r['id']),
                         url=URL, license_=LIC, quality='hand-annotated', notes=' | '.join(nt)))
write_jsonl(NORM + '/%s.jsonl' % ds, rows)
rep, rows2 = qc_dataset(ds, NORM + '/%s.jsonl' % ds, dropped=dict(dropped))
print(ds, len(rows), dict(dropped), 'close', rep['concat_close_fraction'], rep['concat_close_fraction_lenient'], rep['sandhi_type_counts'], 'distinct rules', rep['distinct_rules'])
print('far:', rep['concat_far_examples'])
