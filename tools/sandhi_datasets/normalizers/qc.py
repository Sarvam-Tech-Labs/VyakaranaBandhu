# -*- coding: utf-8 -*-
"""Generic QC for normalised datasets: drop counts, concat closeness, junction distribution, 50-row spread sample."""
import json, os, collections, random, sys
sys.path.insert(0, os.path.dirname(__file__))
from lib import *

QCDIR = OUT + '/qc'
os.makedirs(QCDIR, exist_ok=True)


def lev(a, b):
    """Levenshtein distance on two sequences."""
    if a == b:
        return 0
    if not a:
        return len(b)
    if not b:
        return len(a)
    prev = list(range(len(b) + 1))
    for i, x in enumerate(a, 1):
        cur = [i]
        for j, y in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (x != y)))
        prev = cur
    return prev[-1]


def concat_closeness(inp, out):
    """Edit distance (in sounds) between the concatenation of the input pieces and the joined output (space/hyphen/apostrophe-free).
    Returns (distance, allowed) where allowed = 2*(n_junctions)+1."""
    a = sounds(''.join(inp).replace(' ', '').replace('-', ''))
    b = sounds(out.replace(' ', '').replace('-', ''))
    # avagraha is a marker, not a sound of the pre-sandhi string: drop from both
    a = [x for x in a if x != "'"]
    b = [x for x in b if x != "'"]
    nj = max(1, len(inp) - 1)
    return lev(a, b), 2 * nj + 1


def spread_sample(rows, n=50, seed=3):
    """n rows spread evenly across the list (deterministic)."""
    if len(rows) <= n:
        return rows
    step = len(rows) / n
    return [rows[int(i * step)] for i in range(n)]


def qc_dataset(dataset, path, dropped=None, notes_extra=None, closeness=True, max_rows=None):
    rows = []
    for i, r in enumerate(read_jsonl(path)):
        rows.append(r)
        if max_rows and i + 1 >= max_rows:
            break
    rep = collections.OrderedDict()
    rep['dataset'] = dataset
    rep['rows'] = len(rows)
    rep['dropped_malformed'] = dropped or {}
    rep['dropped_malformed_total'] = sum((dropped or {}).values())
    # closeness
    if closeness and rows:
        ok = 0
        ok_len = 0
        dist = collections.Counter()
        bad = []
        for r in rows:
            d, allowed = concat_closeness(r['input'], r['output'])
            dist[min(d, 10)] += 1
            if d <= allowed:
                ok += 1
            if d <= allowed + 2:
                ok_len += 1
            if d > allowed + 2:
                if len(bad) < 15:
                    bad.append({'id': r['id'], 'input': r['input'], 'output': r['output'], 'edit_distance': d})
        rep['concat_close_fraction'] = round(ok / len(rows), 4)
        rep['concat_close_fraction_lenient'] = round(ok_len / len(rows), 4)
        rep['concat_close_definition'] = 'sound-level edit distance between concat(input) and output <= 2*junctions+1 (strict) or +3 (lenient)'
        rep['concat_distance_histogram'] = dict(sorted(dist.items()))
        rep['concat_far_examples'] = bad
    # junction distribution
    jc = collections.Counter()
    jclass = collections.Counter()
    for r in rows:
        j = r.get('junction')
        if j:
            jc[(j['left_final'], j['right_initial'])] += 1
            jclass[(sound_class(j['left_final']), sound_class(j['right_initial']))] += 1
    rep['two_word_rows'] = sum(jc.values())
    rep['junction_top30'] = [['%s|%s' % k, v] for k, v in jc.most_common(30)]
    rep['junction_class_distribution'] = [['%s|%s' % k, v] for k, v in jclass.most_common()]
    rep['left_final_distribution'] = collections.Counter({k: v for k, v in collections.Counter(j[0] for j in jc.elements()).items()}).most_common(50)
    rep['right_initial_distribution'] = collections.Counter({k: v for k, v in collections.Counter(j[1] for j in jc.elements()).items()}).most_common(50)
    rep['sandhi_type_counts'] = dict(collections.Counter(r['sandhi_type'] for r in rows))
    rep['rule_counts_top15'] = collections.Counter(r['rule'] for r in rows if r['rule']).most_common(15)
    rep['distinct_rules'] = len(set(r['rule'] for r in rows if r['rule']))
    rep['quality_counts'] = dict(collections.Counter(r['quality'] for r in rows))
    rep['spread_sample_50_ids'] = [r['id'] for r in spread_sample(rows, 50)]
    if notes_extra:
        rep.update(notes_extra)
    with open(os.path.join(QCDIR, dataset + '.qc.json'), 'w', encoding='utf-8') as f:
        json.dump(rep, f, ensure_ascii=False, indent=1)
    return rep, rows


def print_spread(rows, n=50):
    for r in spread_sample(rows, n):
        print('%-34s %-34s => %-30s rule=%-9s type=%-9s | %s' % (
            r['id'], ' + '.join(r['input'])[:34], r['output'][:30], r['rule'], r['sandhi_type'], r['source']['locator'][:40]))
