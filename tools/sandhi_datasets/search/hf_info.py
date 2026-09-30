import sys, json, requests, time
from huggingface_hub import HfApi, hf_hub_download
api=HfApi()
UA={'User-Agent':'sandhi-data-survey/0.1 (research; unauthenticated)'}
for rid in sys.argv[1:]:
    print('='*100); print(rid)
    try:
        info=api.dataset_info(rid, files_metadata=True)
    except Exception as e:
        print('ERR',e); continue
    print('sha',info.sha,'lastModified',info.last_modified,'private',info.private,'gated',info.gated)
    cd=info.card_data.to_dict() if info.card_data else {}
    print('license:',cd.get('license'),'| tags:',[t for t in info.tags if not t.startswith('region')][:15])
    tot=0
    for s in info.siblings or []:
        tot+=s.size or 0
        print('   %-70s %10s' % (s.rfilename,s.size))
    print('total bytes',tot)
    try:
        p=hf_hub_download(rid,'README.md',repo_type='dataset')
        t=open(p,encoding='utf-8',errors='replace').read()
        print('--- README (first 2500 chars)'); print(t[:2500])
    except Exception as e:
        print('no README', str(e)[:100])
    time.sleep(1)
