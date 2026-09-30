# -*- coding: utf-8 -*-
"""Normalise the five SandhiKosh corpora (Bhardwaj et al., LREC 2018) to the common schema."""
import sys, os, re, json, collections
sys.path.insert(0, os.path.dirname(__file__))
from lib import *
from qc import concat_closeness
import xlrd

BASE = RAW + '/sanskrit-sandhi_SandhiKosh'
URL = 'https://github.com/sanskrit-sandhi/SandhiKosh'
LIC = ('research-use-only (SandhiKosh README: "provided free of cost for research purposes only"; '
       'cite Bhardwaj et al., LREC 2018); no SPDX licence; commit b4938f82')


def sheet_rows(fname, sheet=None):
    wb = xlrd.open_workbook(os.path.join(BASE, fname))
    sh = wb.sheet_by_name(sheet) if sheet else wb.sheet_by_index(0)
    out = []
    for r in range(sh.nrows):
        vals = []
        for c in sh.row(r):
            v = c.value
            if isinstance(v, float) and v == int(v):
                v = str(int(v))
            elif isinstance(v, float):
                v = repr(v)
            vals.append(str(v))
        out.append((r + 1, vals))     # 1-based excel row number
    return out


def clean_dev_token(t):
    """Normalise obvious typing artefacts; return (clean, list_of_notes)."""
    notes = []
    t0 = t
    t = t.replace(' ', ' ')
    t = re.sub(r'\s+', ' ', t).strip()
    # ASCII colon typed as visarga at the end of a token
    if re.search(r'[ऀ-ॿ]:(\s|$)', t):
        t = re.sub(r'(?<=[ऀ-ॿ]):(?=\s|$)', 'ः', t)
        notes.append('ASCII colon read as visarga')
    if t != t0 and not notes:
        notes.append('whitespace normalised')
    return t, notes


def sutra_from_code(code):
    """Astaadhyaayii corpus 'Rule' column like 11001 -> '1.1.1', 84067 -> '8.4.67'."""
    c = int(code)
    return '%d.%d.%d' % (c // 10000, (c // 1000) % 10, c % 1000)


def build(dataset, fname, sheet, mode):
    rows_out = []
    rejected = []
    dropped = collections.Counter()
    dropped_examples = collections.defaultdict(list)
    raw = sheet_rows(fname, sheet)
    # find header row
    hdr_i = next(i for i, (_, v) in enumerate(raw) if v and v[0].strip().lower().startswith('s'))
    hdr = [x.strip().lower() for x in raw[hdr_i][1]]
    ci = {name: hdr.index(name) for name in ('word', 'split') if name in hdr}
    ti = hdr.index('type') if 'type' in hdr else None
    ri = hdr.index('rule') if 'rule' in hdr else None
    n = 0
    fmt_words = []
    for excel_row, v in raw[hdr_i + 1:]:
        word = v[ci['word']].strip()
        split = v[ci['split']].strip()
        sno = v[0].strip()
        if not word and not split:
            continue
        notes = ['SandhiKosh S.No=%s' % sno]
        if (re.search(r'[\u0900-\u097f]', word) and re.search(r'[A-Za-z]', word)) or (re.search(r'[\u0900-\u097f]', split) and re.search(r'[A-Za-z]', split)):
            dropped['mixed-script'] += 1
            if len(dropped_examples['mixed-script']) < 8:
                dropped_examples['mixed-script'].append({'row': excel_row, 'word': word, 'split': split, 'reason': 'Devanagari mixed with ASCII letters (typically Latin s/S typed for avagraha)'})
            continue
        w_clean, wn = clean_dev_token(word)
        pieces_dev = [p for p in (x.strip() for x in split.split('+'))]
        trailing_plus = False
        while len(pieces_dev) > 1 and pieces_dev[-1] == '':
            pieces_dev.pop()
            trailing_plus = True
        pieces_clean = []
        pn = []
        for p in pieces_dev:
            pc, nn = clean_dev_token(p)
            pieces_clean.append(pc)
            pn += nn
        # transliterate
        out = dev2iast(w_clean)
        inp = [dev2iast(p) for p in pieces_clean]
        reason = malformed_reason(inp, out)
        if reason:
            dropped[reason.split(':')[0]] += 1
            if len(dropped_examples[reason.split(':')[0]]) < 8:
                dropped_examples[reason.split(':')[0]].append({'row': excel_row, 'word': word, 'split': split, 'reason': reason})
            continue
        if trailing_plus:
            notes.append('normalised: trailing "+" (empty last piece) removed')
        d, _allowed = concat_closeness(inp, out)
        nj = max(1, len(inp) - 1)
        if d > 2 * nj + 3:
            dropped['misaligned'] += 1
            rejected.append({'row': excel_row, 'sno': sno, 'word': word, 'split': split, 'input': inp, 'output': out, 'edit_distance': d, 'dataset': dataset})
            if len(dropped_examples['misaligned']) < 8:
                dropped_examples['misaligned'].append({'row': excel_row, 'word': word, 'split': split, 'reason': 'sound-level edit distance %d between concat(split) and word' % d})
            continue
        if wn or pn:
            notes.append('normalised: ' + '; '.join(sorted(set(wn + pn))))
        if any(' ' in p for p in inp):
            notes.append('an input piece contains an inner space (phrase only partly split)')
        if ' ' in out:
            notes.append('output keeps typographic space(s): sandhi applied across a space')
        typ = v[ti].strip() if ti is not None and v[ti].strip() else 'unknown'
        if typ not in ('vowel', 'consonant', 'visarga', 'anusvara', 'mixed', 'none'):
            typ = 'unknown'
        rule = None
        if mode in ('internal', 'external'):
            rc = v[ri].strip()
            comps = rc.split('.')
            rule = '.'.join(comps[:3])
            if len(comps) == 4:
                notes.append('SandhiKosh Rule=%s (sutra %s, example no. %s)' % (rc, rule, comps[3]))
            else:
                notes.append('SandhiKosh Rule=%s' % rc)
        elif mode == 'astadhyayi':
            notes.append('SandhiKosh Rule column = sutra whose WORDING is split here (code %s = sutra %s); it is NOT the sandhi rule applied' % (v[ri].strip(), sutra_from_code(v[ri])))
        elif mode == 'uoh':
            notes.append('SandhiKosh Rule column is only a running index (%s)' % v[ri].strip())
        boundary = 'unknown'
        n += 1
        fmt_words.extend(pieces_clean)
        rows_out.append(make_row(
            dataset, n, inp, out, sandhi_type=typ, rule=rule, boundary=boundary, vedic=False,
            src_file='sanskrit-sandhi_SandhiKosh/%s' % fname + ((':' + sheet) if sheet else ''),
            locator='row %d (S.No %s)' % (excel_row, sno), url=URL, license_=LIC, quality='hand-annotated',
            notes=' | '.join(notes)))
    return rows_out, dropped, dropped_examples, fmt_words, rejected


SPECS = [
    ('sandhikosh-astadhyayi', 'Astaadhyaayii Corpus.xls', None, 'astadhyayi'),
    ('sandhikosh-bhagavadgita', 'Bhagvad_Gita Corpus.xls', None, 'gita'),
    ('sandhikosh-uoh', 'UoH_Corpus.xls', None, 'uoh'),
    ('sandhikosh-rule-internal', 'Rule-based Corpus and Literature Corpus.xls', 'Internal', 'internal'),
    ('sandhikosh-rule-external', 'Rule-based Corpus and Literature Corpus.xls', 'External', 'external'),
    ('sandhikosh-literature', 'Rule-based Corpus and Literature Corpus.xls', 'Literature', 'literature'),
]

if __name__ == '__main__':
    summary = {}
    all_dev_words = []
    for ds, fname, sheet, mode in SPECS:
        rows, dropped, dex, words, rejected = build(ds, fname, sheet, mode)
        os.makedirs(OUT + '/qc/rejected', exist_ok=True)
        write_jsonl(OUT + '/qc/rejected/%s.rejected.jsonl' % ds, rejected)
        path = NORM + '/%s.jsonl' % ds
        write_jsonl(path, rows)
        summary[ds] = {'rows': len(rows), 'dropped': dict(dropped), 'dropped_examples': dict(dex)}
        print(ds, len(rows), 'dropped', dict(dropped))
        all_dev_words += words
    json.dump(summary, open(OUT + '/qc/sandhikosh_build_summary.json', 'w'), ensure_ascii=False, indent=1)
