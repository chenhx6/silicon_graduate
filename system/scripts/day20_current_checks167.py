#!/usr/bin/env python3
"""Fresh structural/identity checks. No scientific certification or credit mutation."""
import json,hashlib,re,subprocess,sys
from pathlib import Path
from datetime import datetime,timezone
from wiki_knowledge_writeback import validate_writeback
root=Path(__file__).resolve().parents[2];d=root/'outputs/learning-daily/20261022-DAY20-be2-qt-deformation-systematics-run-02';report=root/'outputs/learning-daily/20261022-DAY20-be2-qt-deformation-systematics.md';base=json.loads((d/'baseline-001.json').read_text())
started=datetime.now(timezone.utc).isoformat();result={'started_at_utc':started,'scope':'Fresh actual checks; scientific support requires claim self-audit; no final time/card/H3 certification.'}
result['knowledge_writeback']=validate_writeback(report,root,before=base['knowledge_sha256']);print('exact writeback',result['knowledge_writeback']['valid'],flush=True)
protected={k:hashlib.sha256((root/k).read_bytes()).hexdigest()==v for k,v in base['protected_sha256'].items() if k not in ['system/log.md','system/handoff.md']}
protected['original_runner']=hashlib.sha256((d/'runner-original-receipt.json').read_bytes()).hexdigest()==base['original_runner_sha256'];result['protected']=protected
# Compare all pre-existing review statuses and existing true claim flags against baseline HEAD.
mismatches=[]
for rel in result['knowledge_writeback']['knowledge_paths']:
 p=root/rel;s=p.read_text();old=subprocess.run(['git','show',base['head']+':'+rel],cwd=root,capture_output=True,text=True)
 if old.returncode:continue
 def status(t):
  m=re.search(r'^review_status:\s*(.*)$',t,re.M);return m[1] if m else None
 if status(s)!=status(old.stdout):mismatches.append({'path':rel,'kind':'review_status changed'})
 def flags(t):
  x={}
  for line in t.splitlines():
   cells=[c.strip() for c in line.split('|')]
   if len(cells)>4 and cells[-2].lower() in ['true','false']:x[cells[1]]=cells[-2].lower()
  return x
 before=flags(old.stdout);after=flags(s)
 for claim,val in before.items():
  if val=='true' and after.get(claim)=='false':mismatches.append({'path':rel,'claim':claim,'kind':'needs_review lowered'})
result['review_and_flags_mismatches']=mismatches;print('flags checked',len(mismatches),flush=True)
commands={'boundary':[sys.executable,'system/scripts/wiki_boundary_check.py','--root','.'],'preflight':[sys.executable,'system/scripts/wiki_automation_preflight.py','--root','.'],'diff':['git','diff','--check']}
for key,argv in commands.items():
 a=datetime.now(timezone.utc).isoformat();p=subprocess.run(argv,cwd=root,capture_output=True,text=True,timeout=300);result[key]={'argv':argv,'started_at_utc':a,'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr};print(key,p.returncode,flush=True)
text=report.read_text();result['heading_count']=len(re.findall(r'^## ',text,re.M));result['writeback_blocks']=text.count('```knowledge-writeback');result['report_sha256']=hashlib.sha256(report.read_bytes()).hexdigest()
# Full historical raw baseline is identity verification only, never new reading.
rawbad=[]
for rel,expected in base['raw_sha256'].items():
 p=root/rel
 if not p.exists() or hashlib.sha256(p.read_bytes()).hexdigest()!=expected:rawbad.append(rel)
result['raw_identity']={'files':len(base['raw_sha256']),'mismatches':rawbad};print('raw baseline',len(rawbad),flush=True)
result['mechanical_valid']=result['knowledge_writeback']['valid'] and all(protected.values()) and not mismatches and all(result[k]['exit_code']==0 for k in commands) and result['heading_count']==10 and result['writeback_blocks']==1 and not rawbad
result['finished_at_utc']=datetime.now(timezone.utc).isoformat()
out=d/'required-checks-167-fresh.json'
with out.open('x') as f:json.dump(result,f,ensure_ascii=False,indent=2);f.write('\n')
print('mechanical_valid',result['mechanical_valid'],flush=True)
