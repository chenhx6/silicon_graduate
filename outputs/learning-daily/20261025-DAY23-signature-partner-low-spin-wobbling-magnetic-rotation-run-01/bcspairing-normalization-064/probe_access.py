from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import requests,json,datetime,hashlib
O=Path(__file__).resolve().parent
targets=[
 ('publisher_landing','https://www.sciencedirect.com/science/article/pii/0375947478906139'),
 ('publisher_pdfft','https://www.sciencedirect.com/science/article/pii/0375947478906139/pdfft'),
 ('publisher_api_pdf','https://api.elsevier.com/content/article/pii/0375947478906139?httpAccept=application%2Fpdf'),
 ('openalex_doi','https://api.openalex.org/works/https://doi.org/10.1016/0375-9474(78)90613-9'),
 ('lund_institutional','https://portal.research.lu.se/en/publications/nuclear-core-quasiparticle-coupling')
]
def probe(t):
 name,url=t;v={'name':name,'requested_url':url,'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  r=requests.get(url,timeout=(10,25),headers={'User-Agent':'Academic research source verification','Accept':'application/pdf' if 'pdf' in name else '*/*'},allow_redirects=True)
  v.update(http_status=r.status_code,final_url=r.url,content_type=r.headers.get('Content-Type'),bytes=len(r.content),is_pdf=r.content.startswith(b'%PDF'))
  if v['is_pdf']:
   path=O/(name+'.pdf');path.write_bytes(r.content);v.update(file=str(path),sha256=hashlib.sha256(r.content).hexdigest())
  else:
   ext='.json' if 'json' in r.headers.get('Content-Type','') else '.html'
   path=O/(name+ext);path.write_bytes(r.content);v['response_file']=str(path)
   if name=='openalex_doi' and r.status_code==200:
    j=r.json();v['selected_metadata']={k:j.get(k) for k in ['id','doi','title','publication_year','open_access','best_oa_location','locations','primary_location']}
 except Exception as e:v['error_type']=type(e).__name__;v['error_message']=str(e)[:300]
 return v
with ThreadPoolExecutor(max_workers=5) as ex:out=list(ex.map(probe,targets))
(O/'access-probes.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
for v in out:print(json.dumps(v,ensure_ascii=False))
