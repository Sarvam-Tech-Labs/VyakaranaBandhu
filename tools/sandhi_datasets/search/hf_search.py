import requests, sys, json, time
UA={'User-Agent':'sandhi-data-survey/0.1 (research; unauthenticated)'}
seen={}
for q in sys.argv[1:]:
    r=requests.get('https://huggingface.co/api/datasets',params={'search':q,'limit':100,'full':'true'},headers=UA,timeout=60)
    if r.status_code!=200: print('ERR',q,r.status_code,r.text[:100]); continue
    for d in r.json():
        seen.setdefault(d['id'],d)
    print(q,'->',len(r.json()))
    time.sleep(2)
rows=[]
for k,d in sorted(seen.items()):
    lic=[t for t in d.get('tags',[]) if t.startswith('license:')]
    rows.append((k,d.get('downloads'),d.get('likes'),lic,d.get('gated'),d.get('private'),(d.get('description') or '')[:100].replace('\n',' ')))
for r in rows: print(r)
json.dump(seen,open('hf_search_results.json','w'))
