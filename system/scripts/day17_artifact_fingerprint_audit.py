#!/usr/bin/env python3
"""Byte-identity audit of declared result/script/contract bindings only."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
RUN=ROOT/'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'


def main():
    script_pool=list((ROOT/'system/scripts').glob('day17*.py'))+list(RUN.glob('*.py'))
    input_pool=[p for p in RUN.iterdir() if p.is_file() and p.suffix in ['.json','.md','.txt','.py']]
    def index(paths):
        result={}
        for path in paths:
            result.setdefault(hashlib.sha256(path.read_bytes()).hexdigest(),[]).append(str(path.relative_to(ROOT)))
        return result
    scripts,inputs=index(script_pool),index(input_pool)
    rows=[];unmatched=[]
    for path in sorted(RUN.glob('*result*.json')):
        if any(x in path.name for x in ['before','initial','snapshot','draft','trial']):
            continue
        value=json.loads(path.read_text())
        for field,pool in [('script_sha256',scripts),('contract_sha256',inputs)]:
            digest=value.get(field)
            if not isinstance(digest,str) or len(digest)!=64:
                continue
            matches=pool.get(digest,[])
            row={'result':path.name,'field':field,'sha256':digest,'matching_paths':matches,
                 'historical_first_pass':any(s in path.name for s in ['first-pass','first-component'])}
            rows.append(row)
            if not matches:
                unmatched.append(row)
    recovered=RUN/'pb207-stokes-contract-first-pass-hash-recovered.json'
    prior=json.loads((RUN/'pb207-stokes-result-first-pass.json').read_text())
    assert hashlib.sha256(recovered.read_bytes()).hexdigest()==prior['contract_sha256']
    result={'at':datetime.now(timezone.utc).isoformat(),
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'scope':'top-level declared script_sha256 and contract_sha256 in non-initial/non-before result artifacts; exact bytebindings, not functional replay or experimental producer certification',
        'fingerprints_checked':len(rows),'rows':rows,'unmatched':unmatched,
        'historical_contract_recovery':{'path':str(recovered.relative_to(ROOT)),
            'recorded_hash_matched_exactly':True,
            'method':'current declared contract with recorded dependency subset; bounded JSON formatting variants; accepted only after full original SHA256 match',
            'not_claimed_as_original_disk_copy':True},
        'valid':not unmatched}
    (RUN/'artifact-fingerprint-final-audit.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'fingerprints_checked':len(rows),'valid':result['valid'],'unmatched':unmatched},indent=2))
    raise SystemExit(0 if result['valid'] else 1)


if __name__=='__main__':
    main()
