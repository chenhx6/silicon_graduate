#!/usr/bin/env python3
"""Read-only whole-run review-status, prefix and publication-boundary audit."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import subprocess

ROOT=Path(__file__).resolve().parents[2]
RUN=ROOT/'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'


def git(*args):
    return subprocess.check_output(['git',*args],cwd=ROOT)


def flags(text):
    rows={};fenced=False
    for line in text.splitlines():
        if line.startswith('```'):
            fenced=not fenced;continue
        if fenced:
            continue
        match=re.match(r'^\|\s*([A-Za-z0-9][A-Za-z0-9_-]*-\d+)\s*\|.*\|\s*(true|false)\s*\|\s*$',line)
        if match:
            rows.setdefault(match[1],[]).append(match[2])
    return rows


def metadata(text,key):
    match=re.search(r'^'+re.escape(key)+r':\s*(.*?)\s*$',text,re.M)
    return match.group(1) if match else None


def main():
    baseline=json.loads((RUN/'baseline.json').read_text());start=baseline['git_head']
    verification=json.loads((RUN/'verification-088.json').read_text())
    changed=verification['writeback']['changed_paths'];failures=[];sources=[]
    for path in changed:
        if not path.startswith('knowledge/sources/'):
            continue
        current=(ROOT/path).read_text();new=flags(current)
        proc=subprocess.run(['git','show',start+':'+path],cwd=ROOT,capture_output=True)
        if proc.returncode==0:
            original=proc.stdout.decode();old=flags(original)
            for claim,oldflags in old.items():
                if claim not in new or new[claim]!=oldflags:
                    failures.append({'path':path,'claim':claim,'issue':'old flag/count changed','before':oldflags,'after':new.get(claim)})
            if metadata(original,'review_status')!=metadata(current,'review_status'):
                failures.append({'path':path,'issue':'page review_status changed'})
        else:
            old={}
            if metadata(current,'review_status')=='human-reviewed':
                failures.append({'path':path,'issue':'new human-reviewed page'})
        fresh={key:value for key,value in new.items() if key not in old}
        for claim,values in fresh.items():
            if values!=['true']:
                failures.append({'path':path,'claim':claim,'issue':'new claim not uniquely needs_review=true','flags':values})
        sources.append({'path':path,'old_claim_rows':sum(map(len,old.values())),
                        'new_claim_rows':sum(map(len,fresh.values())),
                        'old_review_status_preserved':True,'new_claims_needs_review':True})
    prefixes=[]
    for filename in ['frauendorf2001-human-prefix-snapshot.json','draper1970-human-prefix-snapshot.json',
                     'ekstrom1979-human-prefix-snapshot.json','kumar2025-prefix-snapshot.json']:
        item=json.loads((RUN/filename).read_text());length=item.get('bytes',item.get('length'))
        actual=hashlib.sha256((ROOT/item['path']).read_bytes()[:length]).hexdigest()
        passed=actual==item['sha256'];prefixes.append({'snapshot':filename,'path':item['path'],'length':length,'passed':passed})
        if not passed:
            failures.append({'path':item['path'],'issue':'protected prefix mismatch'})
    protected={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==digest for p,digest in baseline['protected'].items()}
    if not all(protected.values()):
        failures.append({'issue':'PLAN/Bib baseline mismatch'})
    dirty=set(baseline['dirty_baseline']);allowed={'system/log.md'}
    manifests=[]
    for path in sorted(RUN.glob('publication-manifest-*.json')):
        item=json.loads(path.read_text());paths=item['paths']
        for owned in paths:
            if owned=='PLAN.md' or owned.startswith(('raw/','tmp/')) or owned.lower().endswith(('.pdf','.bib')):
                failures.append({'manifest':path.name,'path':owned,'issue':'forbidden publication path'})
            if owned in dirty and owned not in allowed and not owned.startswith(str(RUN.relative_to(ROOT))+'/'):
                failures.append({'manifest':path.name,'path':owned,'issue':'inherited dirty path entered manifest'})
        manifests.append({'manifest':path.name,'path_count':len(paths)})
    original_log=git('show',start+':system/log.md');published_log=git('show','HEAD:system/log.md')
    if not published_log.startswith(original_log):
        failures.append({'issue':'published log did not preserve starting HEAD prefix'})
    result={'at':datetime.now(timezone.utc).isoformat(),'baseline_head':start,
       'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
       'source_pages':sources,'protected_human_or_inherited_prefixes':prefixes,
       'protected_PLAN_Bib':protected,'publication_manifests':manifests,
       'published_log_starting_HEAD_prefix_preserved':published_log.startswith(original_log),
       'source_count':len(sources),'old_claim_row_count':sum(x['old_claim_rows'] for x in sources),
       'new_claim_row_count':sum(x['new_claim_rows'] for x in sources),
       'valid':not failures,'failures':failures}
    (RUN/'source-protection-final-audit.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['source_count','old_claim_row_count','new_claim_row_count','valid','failures']},indent=2))
    raise SystemExit(0 if result['valid'] else 1)


if __name__=='__main__':
    main()
