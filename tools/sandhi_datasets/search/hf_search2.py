import requests, json, time
UA={'User-Agent':'sandhi-data-survey/0.1 (research; unauthenticated)'}
seen={}
def run(q, limit=1000):
    url='https://huggingface.co/api/datasets'
    params={'search':q,'limit':limit,'full':'true'}
    n=0
    while url:
        r=requests.get(url,params=params,headers=UA,timeout=90)
        if r.status_code!=200: print('ERR',q,r.status_code,r.text[:100]); return
        data=r.json()
        for d in data: seen.setdefault(d['id'],d)
        n+=len(data)
        nxt=r.links.get('next',{}).get('url')
        url=nxt; params=None
        time.sleep(1)
        if n>3000: break
    print(q,'->',n)
for q in ['sanskrit','sandhi','vedic','padapatha','samhita','saṃskṛta','sanskrit segmentation','IndicCorp','upanishad','sutra','panini','ashtadhyayi','dcs','sandhikosh']:
    run(q)
json.dump(seen,open('hf_search_results_all.json','w'))
print(len(seen))
