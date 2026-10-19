#!/usr/bin/env python3
"""Reproduce the original models against their exact pre-write page prefixes.

Canonical pages now contain later writeback. The original guards and code stay
unchanged; a temporary Wiki-local mirror restores only the frozen metadata/page
prefix view, with hash-checked original PDFs linked from the same workspace.
"""
from __future__ import annotations
import argparse
import ast
from datetime import datetime
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
from zoneinfo import ZoneInfo


def sha(p:Path)->str:return hashlib.sha256(p.read_bytes()).hexdigest()


def canonical_result(obj):
    if isinstance(obj,dict):return {k:canonical_result(v) for k,v in obj.items() if k!='at'}
    if isinstance(obj,list):return [canonical_result(v) for v in obj]
    return obj


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--run-dir',required=True,type=Path)
    ap.add_argument('--output',required=True,type=Path)
    a=ap.parse_args();root=Path(__file__).resolve().parents[2];r=a.run_dir.resolve()
    assert r.is_relative_to(root/'outputs/learning-daily')
    assert a.output.resolve().is_relative_to(root/'outputs/learning-daily')
    mirror=root/'tmp/day16-frozen-alignment-replay';mirror.mkdir(exist_ok=True)
    actions=[];prefixes=[]
    for freeze_name in ['diamond1966-transfer-before-freeze.json','cejnar1996-transfer-before-freeze.json']:
        f=json.loads((r/freeze_name).read_text());source=root/f['source'];current=source.read_bytes();lf=current.replace(b'\r\n',b'\n')
        candidates=[current,lf,lf.replace(b'\n',b'\r\n')];matches=[x[:f['prefix_bytes']] for x in candidates if hashlib.sha256(x[:f['prefix_bytes']]).hexdigest()==f['prefix_sha256']]
        assert matches,('frozen prefix not recoverable',f['source'])
        data=matches[0];dest=mirror/f['source'];assert dest.resolve().is_relative_to(mirror)
        dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(data)
        raw=root/f['raw'];assert raw.resolve().is_relative_to(root/'raw') and sha(raw)==f['raw_sha256']
        link=mirror/f['raw'];link.parent.mkdir(parents=True,exist_ok=True)
        if link.is_symlink():assert link.resolve()==raw.resolve()
        else:assert not link.exists();link.symlink_to(raw.resolve())
        prefixes.append({'source':f['source'],'historical_prefix_sha256':sha(dest),
            'matches_original_freeze':sha(dest)==f['prefix_sha256'],'original_raw_unchanged':True,
            'canonical_current_page_not_modified':True})
    pending=['day16_alignment_transfer_sign','day16_cejnar1996_transfer_replay'];copied={}
    while pending:
        name=pending.pop()
        if name in copied:continue
        original=root/'system/scripts'/(name+'.py');assert original.is_file()
        target=mirror/'system/scripts'/original.name;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(original.read_bytes())
        copied[name]={'path':str(original.relative_to(root)),'sha256':sha(original),'mirror_same_bytes':sha(target)==sha(original)}
        for node in ast.walk(ast.parse(original.read_text())):
            if isinstance(node,ast.ImportFrom) and node.module and node.module.startswith('day16_'):pending.append(node.module)
            if isinstance(node,ast.Import):pending += [x.name for x in node.names if x.name.startswith('day16_')]
    env=os.environ.copy();deps=root/'tmp/day16-jt74/python-deps';assert deps.is_dir();env['PYTHONPATH']=str(deps)
    pairs=[('day16_alignment_transfer_sign.py','alignment-transfer-contract.json','alignment-transfer-result.json','alignment-transfer-frozen-replay-result.json'),
           ('day16_cejnar1996_transfer_replay.py','cejnar1996-transfer-contract.json','cejnar1996-transfer-result.json','cejnar1996-transfer-frozen-replay-result.json')]
    for script,contract,original_result,new_result in pairs:
        old=json.loads((r/original_result).read_text());assert sha(root/'system/scripts'/script)==old['script_sha256']
        cmd=[sys.executable,str(mirror/'system/scripts'/script),'--contract',str(r/contract),'--output',str(r/new_result)]
        p=subprocess.run(cmd,cwd=root,env=env,capture_output=True,text=True,timeout=90)
        action={'original_script':script,'command':cmd,'exit_code':p.returncode,'stderr':p.stderr,
            'new_result':new_result,'original_result':original_result}
        actions.append(action)
        if p.returncode:
            a.output.write_text(json.dumps({'prefixes':prefixes,'copied_code':copied,'actions':actions},ensure_ascii=False,indent=2)+'\n');print(p.stderr);raise SystemExit(p.returncode)
        new=json.loads((r/new_result).read_text());assert new['script_sha256']==old['script_sha256']
        action['all_scientific_result_fields_identical_excluding_execution_timestamp']=canonical_result(new)==canonical_result(old)
        assert action['all_scientific_result_fields_identical_excluding_execution_timestamp']
        action['new_result_sha256']=sha(r/new_result);print(script,'actualexit0; originalscientificfieldsidentical',flush=True)
    result={'at':datetime.now(ZoneInfo('Asia/Shanghai')).isoformat(),'script_sha256':sha(Path(__file__)),
        'kind':'historical prewrite prefix view only; no change to canonical pages/raw/code/contracts',
        'prefixes':prefixes,'copied_code':copied,'actions':actions,
        'scope':{'original_model_algorithms_and_coefficients_unchanged':True,
            'no_new_independent_experiment_or_credit':True,'replay_guard_not_bypassed':True,
            'source_prefix_state_reconstructed_and_hash_verified':True,
            'all_paths_within_Wiki_and_no_vendor_redistribution':True}}
    a.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')


if __name__=='__main__':main()
