# -*- coding: utf-8 -*-
"""Kaggle sandhi spreadsheets (Word = joined, Split = pieces joined by '+') → harness JSONL.
Run with the scratch_ds venv (it has openpyxl):  venv/bin/python work/norm_kaggle_sandhi.py"""
import sys, os, json, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import openpyxl
from lib import dev2iast

ROOT = '/workspaces/codespaces-blank/sandhi_work/'
RAW = ROOT + 'scratch_ds/external_data/raw/kaggle/'
OUT = ROOT + 'external_data/normalized/'
ZW = {0x200c: None, 0x200d: None}
SOURCES = {
    'kaggle-viragumathe5-sandhi-corpus': ('viragumathe5__sanskrit-sandhi-corpus/files/', ('train.xlsx', 'test.xlsx'),
        'https://www.kaggle.com/datasets/viragumathe5/sanskrit-sandhi-corpus'),
    'kaggle-tanujsaxena-sandhi-data': ('tanujsaxena__sandhi-data/files/', ('sandhi_data.xlsx',),
        'https://www.kaggle.com/datasets/tanujsaxena/sandhi-data'),
}


def iast(s):
    return dev2iast(str(s).translate(ZW)).strip()


for name, (folder, files, url) in SOURCES.items():
    rows, dropped = [], collections.Counter()
    for fn in files:
        ws = openpyxl.load_workbook(RAW + folder + fn, read_only=True).worksheets[0]
        for n, r in enumerate(ws.iter_rows(values_only=True)):
            if n == 0:
                continue
            word, split = r[0], r[1]
            kind = r[2] if len(r) > 2 and r[2] else 'unknown'
            if not word or not split:
                dropped['empty'] += 1
                continue
            pieces = [iast(p) for p in str(split).split('+') if str(p).strip()]
            if len(pieces) < 2:
                dropped['no-plus'] += 1
                continue
            if len(pieces) > 4:
                dropped['more-than-4-pieces'] += 1
                continue
            rows.append({
                'id': f'{name}-{len(rows):06d}', 'dataset': name, 'input': pieces, 'output': iast(word),
                'junction': {'left_final': pieces[0][-1:], 'right_initial': pieces[1][:1]},
                'sandhi_type': kind, 'rule': None, 'boundary': 'unknown', 'vedic': False,
                'source': {'file': f'kaggle/{folder}{fn}', 'locator': f'row {n + 1}', 'url': url}})
    with open(OUT + name + '.jsonl', 'w', encoding='utf-8') as h:
        for x in rows:
            h.write(json.dumps(x, ensure_ascii=False) + '\n')
    print(name, len(rows), 'rows; dropped', dict(dropped))
