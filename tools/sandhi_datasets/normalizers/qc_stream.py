# -*- coding: utf-8 -*-
import sys, os, json, random, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from qc import *

def reservoir(src, dst, n=10000, seed=1):
    rnd = random.Random(seed)
    res = []
    with open(src, encoding='utf-8') as f:
        for i, line in enumerate(f):
            if i < n:
                res.append((i, line))
            else:
                j = rnd.randint(0, i)
                if j < n:
                    res[j] = (i, line)
    res.sort()
    with open(dst, 'w', encoding='utf-8') as g:
        for _, l in res:
            g.write(l)
    return len(res)

def qc_stream(dataset, path, dropped=None, extra=None, spread_n=50):
    total = sum(1 for _ in open(path, encoding='utf-8'))
    step = max(1, total // spread_n)
    rep = collections.OrderedDict(); rep['dataset'] = dataset; rep['rows'] = total
    jc = collections.Counter(); jclass = collections.Counter(); types = collections.Counter(); qual = collections.Counter()
    ok = ok_len = 0; hist = collections.Counter(); far = []; spread = []; boundary = collections.Counter(); two = 0
    npieces = collections.Counter(); edge = collections.Counter(); vedic = collections.Counter(); rules = collections.Counter()
    with open(path, encoding='utf-8') as f:
        for i, line in enumerate(f):
            r = json.loads(line)
            if i % step == 0 and len(spread) < spread_n:
                spread.append(r)
            dd, allowed = concat_closeness(r['input'], r['output'])
            hist[min(dd, 10)] += 1
            if dd <= allowed: ok += 1
            if dd <= allowed + 2: ok_len += 1
            elif len(far) < 15: far.append({'id': r['id'], 'input': r['input'], 'output': r['output'], 'edit_distance': dd})
            j = r.get('junction')
            if j:
                two += 1
                jc[(j['left_final'], j['right_initial'])] += 1
                jclass[(sound_class(j['left_final']), sound_class(j['right_initial']))] += 1
            types[r['sandhi_type']] += 1; qual[r['quality']] += 1; boundary[r['boundary']] += 1; vedic[r['vedic']] += 1
            npieces[min(len(r['input']), 6)] += 1
            if 'EDGE-CLEAN' in r['notes']: edge['clean'] += 1
            elif 'EDGE-AFFECTED' in r['notes']: edge['affected'] += 1
            if r['rule']: rules[r['rule']] += 1
    rep['dropped_malformed'] = dropped or {}
    rep['dropped_malformed_total'] = sum((dropped or {}).values())
    rep['concat_close_fraction'] = round(ok / total, 4); rep['concat_close_fraction_lenient'] = round(ok_len / total, 4)
    rep['concat_close_definition'] = 'sound-level edit distance between concat(input) and output <= 2*junctions+1 (strict) or +3 (lenient)'
    rep['concat_distance_histogram'] = dict(sorted(hist.items())); rep['concat_far_examples'] = far
    rep['two_word_rows'] = two
    rep['junction_top40'] = [['%s|%s' % k, v] for k, v in jc.most_common(40)]
    rep['junction_class_distribution'] = [['%s|%s' % k, v] for k, v in jclass.most_common()]
    lf = collections.Counter(); ri = collections.Counter()
    for (a, b), v in jc.items(): lf[a] += v; ri[b] += v
    rep['left_final_distribution'] = lf.most_common(50); rep['right_initial_distribution'] = ri.most_common(50)
    rep['distinct_junction_pairs'] = len(jc)
    rep['sandhi_type_counts'] = dict(types); rep['quality_counts'] = dict(qual); rep['boundary_counts'] = dict(boundary)
    rep['vedic_counts'] = {str(k): v for k, v in vedic.items()}; rep['pieces_per_row'] = dict(sorted(npieces.items()))
    rep['edge_status'] = dict(edge)
    rep['distinct_rules'] = len(rules); rep['rule_counts_top15'] = rules.most_common(15)
    rep['spread_sample_50_ids'] = [r['id'] for r in spread]
    if extra: rep.update(extra)
    json.dump(rep, open(QCDIR + '/%s.qc.json' % dataset, 'w'), ensure_ascii=False, indent=1)
    return rep, spread

if __name__ == '__main__':
    ex = json.load(open(OUT + '/qc/dcs_extract_counts.json'))
    fin = json.load(open(OUT + '/qc/dcs_finalize_stats.json'))
    for ds in ['dcs-mwt-vedic', 'dcs-spaced-vedic', 'dcs-spaced-classical', 'dcs-mwt-classical']:
        p = NORM + '/%s.jsonl' % ds
        n = reservoir(p, NORM + '/%s.sample.jsonl' % ds)
        kind = 'mwt' if 'mwt' in ds else 'spaced'
        dropped = {k: v for k, v in ex.items() if k.startswith('mwt-' if kind == 'mwt' else 'sp-')}
        if kind == 'spaced':
            dropped['sp-allowlist-left'] = fin['spaced_dropped_L_total']; dropped['sp-allowlist-right'] = fin['spaced_dropped_R_total']
        rep, spread = qc_stream(ds, p, dropped=dropped, extra={'note_dropped': 'counts are for the whole DCS extraction (classical + Vedic together); the extraction-level filters run before the classical/Vedic split'})
        print('=====', ds, 'rows', rep['rows'], 'sample', n, 'close strict', rep['concat_close_fraction'], 'lenient', rep['concat_close_fraction_lenient'], 'two_word', rep['two_word_rows'], 'edge', rep['edge_status'], 'boundary', rep['boundary_counts'])
        json.dump(spread, open(OUT + '/../work/spread_%s.json' % ds, 'w'), ensure_ascii=False)
