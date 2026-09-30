# -*- coding: utf-8 -*-
"""Filter (spaced rows), dedupe by disk sort, and write the DCS-derived JSONL datasets."""
import os, sys, json, collections, subprocess, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
from qc import lev
import dcs_extract as d

WORK = d.WORK
COMMIT = d.COMMIT
URL = 'https://github.com/OliverHellwig/sanskrit/tree/%s/dcs/data/conllu/files' % COMMIT
FILE_PREFIX = 'OliverHellwig_sanskrit/dcs/data/conllu/files/'
LIC = 'CC-BY-4.0'

# ---- allowlists of REGULAR external-sandhi word-boundary alternations (reviewed by hand from the frequency lists) ----------
ALLOW_L = set()
def A(*pairs):
    for p in pairs:
        ALLOW_L.add(p)
A(('m', 'ṃ'), ('m', 'ṅ'), ('m', 'ñ'), ('m', 'ṇ'), ('m', 'n'))
A(('aḥ', 'o'), ('as', 'o'), ('aḥ', 'a'), ('as', 'a'), ('aḥ', 'ā'), ('as', 'ā'), ('ar', 'ā'), ('iḥ', 'ī'), ('uḥ', 'ū'))
A(('ḥ', ''), ('ḥ', 'r'), ('ḥ', 's'), ('ḥ', 'ś'), ('ḥ', 'ṣ'), ('s', 'ḥ'), ('s', 'r'), ('s', ''), ('s', 'ś'), ('s', 'ṣ'),
  ('r', 'ḥ'), ('r', 's'), ('r', 'ś'), ('r', 'ṣ'), ('r', ''))
A(('i', 'y'), ('ī', 'y'), ('u', 'v'), ('ū', 'v'), ('ṛ', 'r'), ('ṝ', 'r'), ('e', 'a'), ('ai', 'ā'), ('au', 'āv'), ('au', 'ā'),
  ('o', 'av'), ('o', 'a'), ('e', 'ay'), ('ai', 'āy'))
A(('t', 'd'), ('t', 'n'), ('t', 'c'), ('t', 'j'), ('t', 'l'), ('t', 'ṭ'), ('t', 'ḍ'), ('t', 'ñ'), ('t', 'ś'), ('d', 't'), ('d', 'n'),
  ('d', 'c'), ('d', 'j'), ('d', 'l'), ('k', 'g'), ('k', 'ṅ'), ('c', 'g'), ('c', 'k'), ('c', 'ṅ'), ('j', 'ḍ'), ('j', 'g'), ('j', 'k'),
  ('j', 'ṭ'), ('ś', 'k'), ('ś', 'g'), ('ś', 'ḍ'), ('ś', 'ṭ'), ('ṣ', 'ṭ'), ('ṣ', 'ḍ'), ('ṭ', 'ḍ'), ('ḍ', 'ṭ'), ('ṭ', 'ṇ'),
  ('bh', 'p'), ('bh', 'b'), ('dh', 'd'), ('dh', 't'), ('h', 'ḍ'), ('h', 'k'), ('p', 'b'), ('p', 'm'), ('b', 'p'), ('g', 'k'), ('t', ''))
A(('n', 'ṃś'), ('n', 'ṃs'), ('n', 'ṃṣ'), ('n', 'ñ'), ('n', 'ṇ'), ('n', 'ṃl'))
# n / ṅ doubling after a short vowel is handled separately (needs the strings)

ALLOW_R = {   # (head of word2 before, after): set of allowed last sounds of the (surface) word1
    ('a', "'"): {'e', 'o'},
    ('ā', "''"): {'ā'},
    ('ś', 'ch'): {'c'},
    ('h', 'gh'): {'g'}, ('h', 'dh'): {'d'}, ('h', 'bh'): {'b'}, ('h', 'jh'): {'j'}, ('h', 'ḍh'): {'ḍ'},
    ('t', 'ṭ'): {'ṣ', 'ṭ'}, ('th', 'ṭh'): {'ṣ', 'ṭ'}, ('st', 'ṣṭ'): {'ṣ'}, ('sth', 'ṣṭh'): {'ṣ'}, ('s', 'ṣ'): {'ṣ'}, ('d', 'ḍ'): {'ḍ'},
}


def l_ok(u1, f1):
    if u1 == f1:
        return True, ('', '')
    tl = d.zone_left(u1, f1)
    key = (tl[0], tl[1])
    if key in ALLOW_L:
        return True, key
    if key in (('', 'n'), ('', 'ṅ')) and last_sound(u1) == key[1] and f1 == u1 + key[1]:
        return True, ('dbl', key[1])
    return False, key


def r_ok(u2, f2, f1):
    if u2 == f2:
        return True, ('', '')
    tr = d.zone_right(u2, f2)
    key = (tr[0], tr[1])
    if key in ALLOW_R and last_sound(f1) in ALLOW_R[key]:
        return True, key
    return False, key


def sh_sort(src, dst, k1, k2):
    env = dict(os.environ, LC_ALL='C')
    subprocess.check_call(['sort', '-s', '-t', '\t', '-k%d,%d' % (k1, k2), '-T', WORK, '-o', dst, src], env=env)


def main():
    stats = collections.OrderedDict()
    # ------------------------------------------------ SPACED: filter -> sort -> group
    dropL = collections.Counter(); dropR = collections.Counter(); keptL = collections.Counter(); keptR = collections.Counter()
    n_in = n_ok = 0
    with open(WORK + '/spaced.tsv', encoding='utf-8') as f, open(WORK + '/spaced.filtered.tsv', 'w', encoding='utf-8') as g:
        for line in f:
            n_in += 1
            c = line.rstrip('\n').split('\t')
            u1, u2, f1, f2 = c[0], c[1], c[2], c[3]
            okl, kl = l_ok(u1, f1)
            okr, kr = r_ok(u2, f2, f1)
            if not okl:
                dropL[kl] += 1; continue
            if not okr:
                dropR[kr] += 1; continue
            keptL[kl] += 1; keptR[kr] += 1
            n_ok += 1
            g.write(line)
    stats['spaced_raw'] = n_in; stats['spaced_after_allowlist'] = n_ok
    stats['spaced_dropped_L_top'] = [[list(k), v] for k, v in dropL.most_common(40)]
    stats['spaced_dropped_R_top'] = [[list(k), v] for k, v in dropR.most_common(25)]
    stats['spaced_dropped_L_total'] = sum(dropL.values()); stats['spaced_dropped_R_total'] = sum(dropR.values())
    stats['spaced_kept_L_signatures'] = [[list(k), v] for k, v in keptL.most_common(60)]
    stats['spaced_kept_R_signatures'] = [[list(k), v] for k, v in keptR.most_common(20)]
    print('spaced', n_in, '->', n_ok)
    sh_sort(WORK + '/spaced.filtered.tsv', WORK + '/spaced.sorted.tsv', 1, 5)
    sh_sort(WORK + '/mwt.tsv', WORK + '/mwt.sorted.tsv', 1, 3)

    outs = {}
    def opener(name):
        if name not in outs:
            outs[name] = open(NORM + '/%s.jsonl' % name, 'w', encoding='utf-8')
        return outs[name]
    counters = collections.defaultdict(lambda: collections.Counter())

    # ---------------- MWT grouping
    def group(path, keycols):
        cur = None; rows = []
        with open(path, encoding='utf-8') as f:
            for line in f:
                c = line.rstrip('\n').split('\t')
                k = tuple(c[:keycols])
                if k != cur:
                    if cur is not None:
                        yield cur, rows
                    cur, rows = k, []
                rows.append(c)
            if cur is not None:
                yield cur, rows

    idx = collections.Counter()
    for k, rows in group(WORK + '/mwt.sorted.tsv', 3):
        U, S, vd = k[0].split('+'), k[1], k[2]
        first = rows[0]
        # prefer an occurrence that is fully manual, then any
        best = min(rows, key=lambda r: {'none': 0, 'part': 1, 'all': 2}[r[4]])
        bnd, rflag, edge, loc_file, sent_id, text = best[3], best[4], best[5], best[6], best[7], best[8]
        name = 'dcs-mwt-vedic' if vd == '1' else 'dcs-mwt-classical'
        idx[name] += 1
        bset = set(bnd.split(',')) if bnd else set()
        boundary = 'samasa' if bset == {'s'} else ('pada' if bset == {'p'} else 'unknown')
        edge_txt = 'EDGE-CLEAN' if edge == 'LR' else ('EDGE-AFFECTED-LEFT' if edge[0] == 'l' else '') + (' EDGE-AFFECTED-RIGHT' if edge[1] == 'r' else '')
        nt = 'DCS multiword token | %s | unsandhied_reconstructed=%s | piece boundaries (s=compound member,p=word)=%s | occurrences=%d | ' % (edge_txt.strip(), {'all': 'all pieces', 'part': 'some pieces', 'none': 'none (manual)'}[rflag], bnd, len(rows))
        nt += 'input = DCS Unsandhied forms; output = the running-text token'
        if edge != 'LR':
            nt += ' | edge flags: the first piece initial and/or the last piece final may be altered by the neighbouring word (not part of the input): compare the last/first sound leniently'
        r = make_row(name, idx[name], U, S, sandhi_type='unknown', rule=None, boundary=boundary, vedic=(vd == '1'),
                     src_file=FILE_PREFIX + loc_file, locator='sent_id=%s' % sent_id, url=URL, license_=LIC,
                     quality='derived-from-annotated-corpus', notes=nt)
        opener(name).write(json.dumps(r, ensure_ascii=False, separators=(',', ':')) + '\n')
        counters[name]['rows'] += 1
        counters[name]['occurrences'] += len(rows)
        counters[name]['edge_clean'] += (edge == 'LR')
        counters[name]['recon_' + rflag] += 1

    # ---------------- SPACED grouping
    for k, rows in group(WORK + '/spaced.sorted.tsv', 5):
        u1, u2, f1, f2, vd = k
        best = min(rows, key=lambda r: r[6].count('r'))
        bd, rflag, loc_file, sent_id, text = best[5], best[6], best[7], best[8], best[9]
        name = 'dcs-spaced-vedic' if vd == '1' else 'dcs-spaced-classical'
        idx[name] += 1
        nt = ('DCS adjacent single-word tokens; sandhi is applied although a typographic space remains | unsandhied_reconstructed(left,right; m=manual r=reconstructed)=%s | occurrences=%d | '
              'edge-clean: word1 initial and word2 final unchanged | only pairs with a visible sandhi change and a regular signature are kept') % (rflag, len(rows))
        r = make_row(name, idx[name], [u1, u2], f1 + ' ' + f2, sandhi_type='unknown', rule=None, boundary=('samasa' if bd == 's' else 'pada'), vedic=(vd == '1'),
                     src_file=FILE_PREFIX + loc_file, locator='sent_id=%s' % sent_id, url=URL, license_=LIC,
                     quality='derived-from-annotated-corpus', notes=nt)
        opener(name).write(json.dumps(r, ensure_ascii=False, separators=(',', ':')) + '\n')
        counters[name]['rows'] += 1
        counters[name]['occurrences'] += len(rows)
    for f in outs.values():
        f.close()
    stats['datasets'] = {n: dict(c) for n, c in counters.items()}
    json.dump(stats, open(OUT + '/qc/dcs_finalize_stats.json', 'w'), ensure_ascii=False, indent=1)
    print(json.dumps(stats['datasets'], indent=1))
    for n in outs:
        print(n, os.path.getsize(NORM + '/%s.jsonl' % n))


if __name__ == '__main__':
    main()
