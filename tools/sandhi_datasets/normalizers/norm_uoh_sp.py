# -*- coding: utf-8 -*-
"""Normalise the UoH 'Sandhi-Extract' files bundled in kmadathil/sanskrit_parser tests/sandhi_test_data
(MIT at repo level; upstream = University of Hyderabad Dept. of Sanskrit Studies)."""
import sys, os, re, json, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib import *
from qc import concat_closeness

BASE = RAW + '/kmadathil_sanskrit_parser/tests/sandhi_test_data'
URLB = 'https://github.com/kmadathil/sanskrit_parser/blob/a31ff41cc0869201007ca87a01aaee574ebe01b1/tests/sandhi_test_data/'
LIC = ('MIT (sanskrit_parser repo-level LICENSE) -- RISK: upstream provenance is the University of Hyderabad '
       'Dept. of Sanskrit Studies "Sandhi-Extract" files (in-copyright source books, no data licence published there); '
       'keep for local evaluation, verify before redistributing')
FILES = [
    'refs.txt', '2.karnabhara-ext.txt', '130-short-stories-extracted.txt', 'vetalkatha_ext.txt',
    '4.dutaghatotgajam-ext.txt', '3.dutavakyam-ext.txt', 'madyama_ext.txt', 'vrubhangam_ext.txt',
    'balaramayanam_ext.txt', '5.balacharitham-ext.txt', '1.abhishakanatakam-ext.txt', '7.charudattam-ext.txt',
    'vinodini-ext.txt', 'astanga-hridayam-sandhi-extract1-27.txt', 'madhavi-ext.txt', 'manjusa-ext.txt',
    'tarkabhasha-ext.txt', 'Rajkathakunj_ext.txt', 'Aakhyanvallari_ext.txt', 'sanskritkathashatkam1_ext.txt',
    'nyayasara-ext.txt', 'tarkchudamani-ext.txt', 'Sanskritkathakunj_ext.txt', 'agnipuran-1-111-sandhi_ext.txt',
    'vyutpattivada-ext.txt']

_STRIP_PUNCT = re.compile(r'^[\s,.;:!?|।॥"\'‘’“”()\[\]{}\-–—*]+|[\s,.;:!?|।॥"‘’“”()\[\]{}\-–—*]+$')


def load_status():
    """(file, line) -> 'join-pass' | 'join-fail' from sanskrit_parser's derived files."""
    st = {}
    for fn, tag in (('sandhi_join_passing.txt', 'pass'), ('sandhi_join_failing.txt', 'fail')):
        with open(os.path.join(BASE, fn), encoding='utf-8') as f:
            for line in f:
                d = json.loads(line)
                st[(d['file'], d['line'])] = tag
    return st


def clean_side(s, notes):
    s0 = s
    s = s.translate({0x200c: None, 0x200d: None, 0xa0: 0x20})
    s = re.sub(r'\s+', ' ', s)
    s_v = re.sub(r'\s*[|\u0964\u0965]+\s*[\d\u0966-\u096f.\-]+\s*[|\u0964\u0965]+\s*$', '', s)   # trailing verse marker such as ||19||
    if s_v != s:
        notes.add('trailing verse-number marker stripped')
        s = s_v
    s2 = _STRIP_PUNCT.sub('', s)
    # keep a trailing avagraha-like apostrophe? (strip regexp does not include it in the tail set)
    if s2 != s.strip():
        notes.add('leading/trailing punctuation stripped')
    # ASCII colon used for visarga inside/at end of Devanagari token
    if re.search(r'[ऀ-ॿ]:', s2):
        s2 = re.sub(r'(?<=[ऀ-ॿ]):', 'ः', s2)
        notes.add('ASCII colon read as visarga')
    return s2


def main():
    status = load_status()
    dataset = 'uohyd-sandhi-extract'
    rows_by_key = collections.OrderedDict()
    dropped = collections.Counter()
    dropped_ex = collections.defaultdict(list)
    rejected = []
    per_file = collections.Counter()
    total_lines = 0
    for fn in FILES:
        path = os.path.join(BASE, fn)
        with open(path, encoding='utf-8') as f:
            for ln, line in enumerate(f, 1):
                line = line.rstrip('\n')
                if not line.strip() or line.lstrip().startswith('#'):
                    continue
                if '=>' in line:
                    joined, splits = [x for x in line.split('=>', 1)]
                    direction = '=>'
                elif '=' in line:
                    splits, joined = [x for x in line.split('=', 1)]
                    direction = '='
                else:
                    continue
                total_lines += 1
                notes = set()
                if not re.search(r'[ऀ-ॿ]', joined + splits):
                    dropped['not-devanagari'] += 1
                    continue
                if (re.search(r'[ऀ-ॿ]', joined) and re.search(r'[A-Za-z]', joined)) or \
                        (re.search(r'[ऀ-ॿ]', splits) and re.search(r'[A-Za-z]', splits)):
                    dropped['mixed-script'] += 1
                    if len(dropped_ex['mixed-script']) < 6:
                        dropped_ex['mixed-script'].append({'file': fn, 'line': ln, 'text': line[:120]})
                    continue
                pieces = [x for x in splits.split('+')]
                pieces = [clean_side(p, notes) for p in pieces]
                # strip empty pieces at both ends (trailing "+" is common in this corpus)
                while pieces and pieces[-1] == '':
                    pieces.pop(); notes.add('empty end piece removed')
                while pieces and pieces[0] == '':
                    pieces.pop(0); notes.add('empty end piece removed')
                jn = clean_side(joined, notes)
                inp = [dev2iast(p) for p in pieces]
                out = dev2iast(jn)
                reason = malformed_reason(inp, out) if pieces else 'empty-input-piece'
                if reason:
                    key = reason.split(':')[0]
                    dropped[key] += 1
                    if len(dropped_ex[key]) < 6:
                        dropped_ex[key].append({'file': fn, 'line': ln, 'text': line[:120], 'reason': reason})
                    continue
                if len(inp) < 2:
                    dropped['single-piece'] += 1
                    continue
                d, allowed = concat_closeness(inp, out)
                nj = max(1, len(inp) - 1)
                if d > 2 * nj + 3:
                    dropped['misaligned'] += 1
                    rejected.append({'file': fn, 'line': ln, 'input': inp, 'output': out, 'edit_distance': d})
                    continue
                key = (tuple(inp), out)
                st = status.get((fn, ln))
                if key in rows_by_key:
                    rows_by_key[key]['count'] += 1
                    if st == 'fail':
                        rows_by_key[key]['any_join_fail'] = True
                    continue
                rows_by_key[key] = {'inp': inp, 'out': out, 'file': fn, 'line': ln, 'direction': direction,
                                    'notes': notes, 'count': 1, 'status': st, 'any_join_fail': st == 'fail'}
                per_file[fn] += 1
    rows = []
    for i, (key, v) in enumerate(rows_by_key.items(), 1):
        nt = ['UoH extract line; source file %s' % v['file']]
        nt.append('occurrences (identical pair, all files): %d' % v['count'])
        if v['status']:
            nt.append('sanskrit_parser join test: %s' % ('PASS' if v['status'] == 'pass' else 'FAIL (a lead: parser or data may be wrong)'))
        if v['direction'] == '=':
            nt.append('line format "split = joined" (hand examples from a sandhi textbook, refs.txt)')
        if v['notes']:
            nt.append('normalised: ' + '; '.join(sorted(v['notes'])))
        if any(' ' in p for p in v['inp']):
            nt.append('an input piece contains an inner space (phrase only partly split)')
        if ' ' in v['out']:
            nt.append('output keeps typographic space(s): sandhi applied across a space')
        nt.append('UoH convention: pre-sandhi finals are often the pausal/visarga form; word-final m may be anusvara in output')
        rows.append(make_row(dataset, i, v['inp'], v['out'], sandhi_type='unknown', rule=None, boundary='unknown', vedic=False,
                             src_file='kmadathil_sanskrit_parser/tests/sandhi_test_data/%s' % v['file'],
                             locator='line %d' % v['line'], url=URLB + v['file'], license_=LIC,
                             quality='hand-annotated', notes=' | '.join(nt)))
    path = NORM + '/%s.jsonl' % dataset
    write_jsonl(path, rows)
    os.makedirs(OUT + '/qc/rejected', exist_ok=True)
    write_jsonl(OUT + '/qc/rejected/%s.rejected.jsonl' % dataset, rejected)
    summ = {'dataset': dataset, 'input_lines_with_separator': total_lines, 'unique_rows_kept': len(rows),
            'dropped': dict(dropped), 'dropped_examples': dict(dropped_ex), 'per_file_unique': dict(per_file)}
    json.dump(summ, open(OUT + '/qc/%s_build_summary.json' % dataset, 'w'), ensure_ascii=False, indent=1)
    print(json.dumps({k: v for k, v in summ.items() if k != 'dropped_examples'}, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
