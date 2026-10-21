#!/usr/bin/env python3
"""Input checks only; not an all-checkpoint or scientific completion certificate."""
import argparse
import datetime
import hashlib
import json
from pathlib import Path
from wiki_knowledge_writeback import validate_writeback

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    root=Path('.').resolve()
    run=root/'outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01'
    checks=[]
    def check(name,passed,**evidence):
        checks.append(dict(name=name,passed=bool(passed),**evidence))
    recall=json.loads((run/'active-recall-freeze.json').read_text())
    check('recall hash and priming',hashlib.sha256((root/recall['recall_path']).read_bytes()).hexdigest()==recall['sha256'] and recall['primed'] and not recall['blind_test'])
    scope=json.loads((run/'source-reading-scope-001.json').read_text())
    for name in ['jensen','mu08']:
        d=scope[name]
        check(name+' actual raw hash',hashlib.sha256((root/d['raw_file']).read_bytes()).hexdigest()==d['sha256'])
    check('MU08 recorded six-page scope',scope['mu08']['text_pages_read']==[1,2,3,4,5,6])
    clock=json.loads((run/'clock-contrast-result-001.json').read_text())
    check('formal-session design individual checks',bool(clock.get('checks')) and all(c.get('passed') is True for c in clock['checks']))
    correction=json.loads((run/'strength-boundary-correction-result-078.json').read_text())
    check('correction individual checks',bool(correction.get('checks')) and all(c.get('passed') is True for c in correction['checks']))
    check('current correction script hash',correction['script_sha256']==hashlib.sha256((root/'system/scripts/day18_strength_boundary_correction.py').read_bytes()).hexdigest())
    wb=validate_writeback(root/'outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength.md',root)
    check('writeback function executed',wb['valid'],error=wb['error'])
    body=(root/'knowledge/sources/liu-2016-octupole-correlations-multiple-chiral-doublet-bands-78br.md').read_text()
    check('L16-D18-2 row unique',body.count('| L16-D18-2 |')==1)
    original=json.loads((run/'original-receipt-observed-001.json').read_text())
    current=json.loads((run/'run.json').read_text())
    check('run and deadline preserved',current['run_id']==original['run_id'] and current['overnight_until']==original['overnight_until'])
    result=dict(at=datetime.datetime.now(datetime.timezone.utc).isoformat(),valid=all(c['passed'] for c in checks),checks=checks,
                scope='actual hashes, recorded reading scope, design checks and writeback structure only',
                knowledge_paths_count=len(wb['knowledge_paths']),ready_for_final_completion=False,
                required_separate_audits=['scientific support','protected files','ten headings/card coverage','fresh required checks','post-deadline receipt','H3 publication','one-time credit reconciliation'])
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(valid=result['valid'],checks=len(checks),output=str(args.output))))
    return 0 if result['valid'] else 1

if __name__=='__main__':
    raise SystemExit(main())
