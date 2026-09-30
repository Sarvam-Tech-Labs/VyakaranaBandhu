import requests, json, time, sys
UA={'User-Agent':'sandhi-data-survey/0.1 (research; anonymous public API)'}
seen={}
for q in ['sanskrit','sandhi','sanskrit sandhi','shlokas','bhagavad gita','ramayana','mahabharata','sanskrit corpus','rigveda','vedic','devanagari sanskrit','sanskrit segmentation','sanskrit grammar','panini','sanskrit morphology','sanskrit verses','upanishad']:
    for page in (1,2,3):
        r=requests.get('https://www.kaggle.com/api/v1/datasets/list',params={'search':q,'page':page},headers=UA,timeout=60)
        if r.status_code!=200: print('ERR',q,page,r.status_code); break
        d=r.json()
        if not d: break
        for x in d: seen.setdefault(x['refNullable'] if 'refNullable' in x else x.get('urlNullable'),x)
        time.sleep(1.5)
    print(q,len(seen))
json.dump(seen,open('kaggle_search_results.json','w'))
rows=[]
for k,x in seen.items():
    rows.append((x.get('refNullable') or k, x.get('licenseNameNullable'), x.get('totalBytesNullable'), x.get('downloadCountNullable'), x.get('subtitleNullable')))
for r in sorted(rows,key=lambda r:str(r[0])): print(r)
