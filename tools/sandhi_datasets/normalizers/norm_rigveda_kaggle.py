# -*- coding: utf-8 -*-
"""Rigveda samhita (sandhied) vs padapatha (split) from the Kaggle JSON (MIT per uploader): align padapatha morphs to samhita tokens."""
import sys, os, re, json, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
from qc import lev, qc_dataset
import dcs_finalize as F

SRC = RAW + '/kaggle/varunrajuvangar__rigved-all-sukta-verses-and-meaning-dataset/files/complete_rigveda_all_mandalas.json'
URL = 'https://www.kaggle.com/datasets/varunrajuvangar/rigved-all-sukta-verses-and-meaning-dataset'
LIC = 'MIT (Kaggle uploader Varun Raju Vangar; underlying Rigveda text and padapatha are public-domain editions, provenance of the digitisation not stated)'
DS = 'rigveda-padapatha-samhita'
j = json.load(open(SRC, encoding='utf-8'))
ZW = {0x200c: None, 0x200d: None}


def iast(s):
    s = dev2iast(s.translate(ZW)).replace('ḻ', 'ḷ')
    return s


def strip_av(x):
    return [t for t in sounds(x) if t != "'"]


rows, dropped, uniq = [], collections.Counter(), {}
def rec(inp, out, loc, kind, notes_extra):
    key = (tuple(inp), out)
    if key in uniq:
        uniq[key]['n'] += 1
        return
    uniq[key] = {'inp': inp, 'out': out, 'loc': loc, 'kind': kind, 'n': 1, 'x': notes_extra}


for man, suk in j.items():
    for sname, riks in suk.items():
        for rk in riks:
            loc = '%s %s rik %s' % (man, sname, rk.get('rik_number'))
            try:
                sam = rk['samhita']['devanagari']['text']
                pw = rk['padapatha']['devanagari']['words']
            except Exception:
                dropped['missing-field'] += 1
                continue
            if not sam or not pw or not isinstance(sam, str):
                dropped['missing-field'] += 1
                continue
            pw = [w for w in pw if isinstance(w, str)]
            toks = [iast(t) for t in re.split(r'[\s।॥|]+', sam) if t.strip()]
            toks = [t for t in toks if t and not re.search(r'\d', t)]
            morphs, wordidx = [], []
            for wi, w in enumerate(pw):
                w = w.strip()
                if not w or w in ('।', '॥') or re.fullmatch(r'[\d\s।॥]+', w):
                    continue
                for ci, c in enumerate(w.split('ऽ')):
                    if c:
                        morphs.append(iast(c)); wordidx.append((wi, ci))
            if not toks or not morphs or any(re.search(r'[^a-zāīūṛṝḷḹṅñṭḍṇśṣṃḥ\']', x) for x in morphs + toks):
                dropped['unusable-rik'] += 1
                continue
            m, n = len(toks), len(morphs)
            INF = 10 ** 9
            cost = [[INF] * (n + 1) for _ in range(m + 1)]
            back = [[0] * (n + 1) for _ in range(m + 1)]
            cost[0][0] = 0
            tsnd = [strip_av(t) for t in toks]
            for a in range(1, m + 1):
                for b in range(1, n + 1):
                    for k in range(1, 6):
                        b0 = b - k
                        if b0 < 0 or cost[a - 1][b0] >= INF:
                            continue
                        c = lev(strip_av(''.join(morphs[b0:b])), tsnd[a - 1])
                        # penalise big edits per group: each junction may change ~2 sounds
                        if c > 2 * (k - 1) + 4:
                            continue
                        if cost[a - 1][b0] + c < cost[a][b]:
                            cost[a][b] = cost[a - 1][b0] + c; back[a][b] = b0
            if cost[m][n] >= INF or cost[m][n] > 3 * m:
                dropped['no-alignment'] += 1
                continue
            groups = []
            b = n
            for a in range(m, 0, -1):
                b0 = back[a][b]; groups.append((a - 1, b0, b)); b = b0
            groups.reverse()
            for gi, (a, b0, b1) in enumerate(groups):
                mm = morphs[b0:b1]
                if len(mm) >= 2:
                    # compound members or fused words
                    kinds = ''.join('s' if wordidx[q][0] == wordidx[q + 1][0] else 'p' for q in range(b0, b1 - 1))
                    rec(mm, toks[a], loc, 'fused', kinds)
            for (a, b0, b1), (a2, c0, c1) in zip(groups, groups[1:]):
                if b1 - b0 == 1 and c1 - c0 == 1:
                    u1, u2 = morphs[b0], morphs[c0]; f1, f2 = toks[a], toks[a2]
                    if f1 == u1 and f2 == u2: continue
                    if first_sound(f1) != first_sound(u1) or last_sound(f2) != last_sound(u2): continue
                    ok1, _ = F.l_ok(u1, f1); ok2, _ = F.r_ok(u2, f2, f1)
                    tl = F.d.zone_left(u1, f1); tr = F.d.zone_right(u2, f2)
                    if not (ok1 and ok2) or tl[2] > 3 or tl[3] > 3 or tr[2] > 3 or tr[3] > 3:
                        dropped['spaced-not-regular'] += 1; continue
                    rec([u1, u2], f1 + ' ' + f2, loc, 'spaced', 'p')
i = 0
for key, v in uniq.items():
    inp, out = v['inp'], v['out']
    reason = malformed_reason(inp, out)
    if reason:
        dropped[reason.split(':')[0]] += 1; continue
    i += 1
    if v['kind'] == 'fused':
        lc = first_sound(out) == first_sound(inp[0]); rc = last_sound(out) == last_sound(inp[-1]) and out.endswith(inp[-1][-1:])
        edge = 'EDGE-CLEAN' if (lc and rc) else ('EDGE-AFFECTED' + ('-LEFT' if not lc else '') + ('-RIGHT' if not rc else ''))
        nt = 'Rigveda samhita token aligned to padapatha morphs by DP (sound-level edit distance) | %s | piece boundaries (s=compound member,p=word)=%s | occurrences=%d' % (edge, v['x'], v['n'])
        bset = set(v['x']); boundary = 'samasa' if bset == {'s'} else ('pada' if bset == {'p'} else 'unknown')
    else:
        nt = 'Rigveda adjacent samhita tokens (one padapatha word each) aligned by DP; sandhi visible although a space remains | occurrences=%d' % v['n']
        boundary = 'pada'
    nt += ' | input = padapatha forms (compound parts split at the avagraha sign), output = samhita text; Vedic orthography, no accents; Vedic letter LA written as l with dot below'
    rows.append(make_row(DS, i, inp, out, sandhi_type='unknown', rule=None, boundary=boundary, vedic=True,
                         src_file='kaggle/varunrajuvangar__rigved-all-sukta-verses-and-meaning-dataset/files/complete_rigveda_all_mandalas.json',
                         locator=v['loc'], url=URL, license_=LIC, quality='derived-from-annotated-corpus', notes=nt))
write_jsonl(NORM + '/%s.jsonl' % DS, rows)
rep, r2 = qc_dataset(DS, NORM + '/%s.jsonl' % DS, dropped=dict(dropped))
print(DS, len(rows), dict(dropped), 'close', rep['concat_close_fraction'], rep['concat_close_fraction_lenient'], 'two_word', rep['two_word_rows'], collections.Counter('fused' if 'token aligned' in r['notes'] else 'spaced' for r in rows))
import random
random.seed(5)
for r in random.sample(rows, 40): print(' + '.join(r['input'])[:44], '=>', r['output'][:36], '|', r['source']['locator'])
