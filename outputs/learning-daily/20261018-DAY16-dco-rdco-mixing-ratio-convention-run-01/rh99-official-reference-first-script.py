#!/usr/bin/env python3
"""Exact selected ENSDF records for a matched-reference readiness audit.

No measured alignment, mixing ratio, or new transition assignment is inferred.
"""
from __future__ import annotations
import argparse
from datetime import datetime
from decimal import Decimal
import hashlib
import json
from pathlib import Path
from zoneinfo import ZoneInfo


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def tokens(line: str, kind: str) -> dict:
    if kind == 'L':
        return {'E':line[9:19].strip(),'DE':line[19:21].strip(),
                'Jpi':line[21:39].strip(),'band':line[76:77].strip()}
    return {'E':line[9:19].strip(),'DE':line[19:21].strip(),
            'RI':line[21:29].strip(),'DRI':line[29:31].strip(),
            'M':line[31:41].strip(),'MR':line[41:49].strip(),
            'DMR':line[49:55].strip(),'CC':line[55:62].strip()}


def parse(path: Path) -> list[dict]:
    levels=[];level=None;gamma=None
    for lineno,line in enumerate(path.read_text().splitlines(),1):
        if line[5:9]=='  L ':
            level={'line':lineno,'raw':line,**tokens(line,'L'),'gammas':[]}
            levels.append(level);gamma=None
        elif line[5:9]=='  G ':
            assert level is not None
            gamma={'line':lineno,'raw':line,**tokens(line,'G'),'comments':[]}
            level['gammas'].append(gamma)
        elif gamma is not None and (line[5:9]=='2 G ' or line[5:9]==' cG '):
            gamma['comments'].append({'line':lineno,'text':line[9:].strip()})
    return levels


def exact_level(levels: list[dict], E: float) -> dict:
    matches=[x for x in levels if x['E']==str(E)]
    assert len(matches)==1,(E,len(matches))
    return matches[0]


def gamma_at(level: dict,E: float) -> dict:
    matches=[x for x in level['gammas'] if x['E']==str(E)]
    assert len(matches)==1,(E,len(matches))
    return matches[0]


def main() -> None:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--contract',required=True,type=Path)
    ap.add_argument('--output',required=True,type=Path)
    a=ap.parse_args();cfg=json.loads(a.contract.read_text())
    assert cfg['identity']=='RH99-2017-SELECTED-REFERENCE-RECORDS-01'
    root=Path(__file__).resolve().parents[2]
    for f in cfg['files']:assert sha(root/f['path'])==f['sha256']
    adopted=parse(root/cfg['files'][0]['path']);hi=parse(root/cfg['files'][1]['path'])
    pa=exact_level(adopted,cfg['parent_levels']['adopted'])
    ph=exact_level(hi,cfg['parent_levels']['HI'])
    assert pa['Jpi']==ph['Jpi']=='23/2-'
    assert len(pa['gammas'])==len(ph['gammas'])==6
    target=gamma_at(ph,cfg['target_gamma']);norm=Decimal(target['RI'])
    closure=[];rounding=[]
    for E in cfg['selected_sameparent_gammas']:
        ga=gamma_at(pa,E);gh=gamma_at(ph,E)
        assert ga['MR']==gh['MR']==''
        difference=Decimal(ph['E'])-Decimal(gh['E'])
        final=min(hi,key=lambda x:abs(Decimal(x['E'])-difference))
        residual=difference-Decimal(final['E'])
        assert abs(residual)<=Decimal('.2')
        value=100*Decimal(gh['RI'])/norm
        # Normalization is an arithmetic crosscheck, not a new uncertainty.
        cell=Decimal(ga['RI']);ulp=Decimal(10)**cell.as_tuple().exponent
        within=abs(value-cell)<=ulp/2
        assert within,(E,value,cell,ulp)
        closure.append({'gamma':gh,'parent_E':ph['E'],'parent_Jpi':ph['Jpi'],
            'energy_difference':str(difference),'selected_final_E':final['E'],
            'selected_final_Jpi':final['Jpi'],'closure_residual_keV':str(residual),
            'not_new_level_assignment':True})
        rounding.append({'Egamma':str(E),'HI_RI':gh['RI'],'Adopted_RI':ga['RI'],
            'HI_normalized_target100':str(value),'within_printed_Adopted_halfcell':within})
    # Controls bind parent and final state, not nearest photon energy alone.
    c1=gamma_at(exact_level(hi,3698.1),1104.3)
    c2=gamma_at(exact_level(hi,4264.0),1114.1)
    assert c1['M']=='M1' and c2['M']=='E2'
    assert all(x['gamma']['M'] in ['M1','E1'] for x in closure)
    assert sum('DCO=' in z['text'] for z in target['comments'])==2
    results={'at':datetime.now(ZoneInfo('Asia/Shanghai')).isoformat(),
        'script_sha256':sha(Path(__file__)),'contract_sha256':sha(a.contract),
        'fixed_files_verified':True,'parsed_level_counts':{'Adopted':len(adopted),'HI':len(hi)},
        'selected_parents':{'Adopted':{k:pa[k] for k in ['line','E','Jpi','band']},'HI':{k:ph[k] for k in ['line','E','Jpi','band']}},
        'sameparent_six_branches':closure,'central_RI_normalization_checks':rounding,
        'distinct_parent_controls':[{'parent_E':'3698.1','parent_Jpi':'23/2+','gamma':c1},{'parent_E':'4264.0','parent_Jpi':'27/2+','gamma':c2}],
        'readiness':{'no_pureE2_among_six_recorded_sameparent_branches':True,
            'no_MR_value_for_six_is_not_delta0_measurement':True,
            'no_sameparent_a2_a4_or_moment_measurement_recovered':True,
            'known_class_label_is_not_independent_purity_or_alignment':True,
            'DCO_IPDCO_not_P00_a2_P_or_sharedQ':True,
            'no_new_experimental_fit_or_nuclear_assignment':True}}
    a.output.write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:results[k] for k in ['parsed_level_counts','selected_parents','central_RI_normalization_checks','readiness']},ensure_ascii=False,indent=2))


if __name__=='__main__':main()
