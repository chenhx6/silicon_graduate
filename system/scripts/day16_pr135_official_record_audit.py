#!/usr/bin/env python3
"""Versioned official135Pr record identities; no pooling of Delta/P or delta fits."""
from __future__ import annotations
import argparse
from datetime import datetime
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import re
from zoneinfo import ZoneInfo
from day16_ni60_reference_audit import records


def sha(path:Path)->str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def errors(token:str,unc:str)->dict|None:
    if not token or not unc:return None
    unit=Decimal(10)**Decimal(token).as_tuple().exponent
    if unc.isdigit():return {'plus':float(Decimal(unc)*unit),'minus':float(Decimal(unc)*unit)}
    m=re.fullmatch(r'\+(\d+)-(\d+)',unc)
    if not m:raise ValueError((token,unc))
    return {'plus':float(Decimal(m[1])*unit),'minus':float(Decimal(m[2])*unit)}


def main()->None:
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--contract',type=Path,required=True);p.add_argument('--output',type=Path,required=True);args=p.parse_args();cfg=json.loads(args.contract.read_text());assert cfg['identity']=='N135-OBJECT-MR-POL-LINEAGE-01'
    datasets={};rowlist=[]
    for f in cfg['files']:
        path=Path(f['text_path']);assert sha(path)==f['sha256'];text=path.read_text();data=records(path)
        datasets[f['name']]={'path':str(path),'sha256':sha(path),'line_count':len(text.splitlines()),
            'header':text.splitlines()[:27],'MR_nonempty_gamma_count':sum(bool(g['MR']) for g in data['gammas']),
            'contains_2019erratum_DOI_or_code':'069901' in text or '2019Ga' in text or '2019GA' in text}
        for target in cfg['targets'][f['name']]:
            found=[g for g in data['gammas'] if g['E']==target['E'] and g['parent']['E']==target['parent']]
            assert len(found)==1,(f['name'],target)
            z=found[0];z['dataset_name']=f['name'];z['MR_sigma']=errors(z['MR'],z['DMR'])
            z['final_level_energy_difference_keV']=float(z['parent']['E'])-float(z['E'])
            pol=[]
            for c in z['attached']:
                m=re.search(r'pol=([+-]?\d+(?:\.\d+)?)\s*\{I([^}]+)\}',c['raw'])
                if m:pol.append({'value_token':m[1],'error_token':m[2],'error':errors(m[1],m[2]),'line':c['line']})
            z['pol_fields']=pol;rowlist.append(z)
        if f['name']=='adopted2008':
            other=[g for g in data['gammas'] if g['E']=='746.1'];assert len(other)==1
            decoy=other[0];assert decoy['parent']['E']=='1289.60' and decoy['parent']['Jpi']=='(11/2-)'
    by={name:[g for g in rowlist if g['dataset_name']==name] for name in datasets}
    assert all(not g['MR'] for g in by['adopted2008']+by['garg-xundl3'])
    assert [g['MR'] for g in by['lv-xundl6']]==['-0.47','-0.37']
    assert [g['MR'] for g in by['sensharma-xundl7']]==['-1.40','-1.63']
    assert by['sensharma-xundl7'][0]['MR_sigma']=={'plus':.14,'minus':.12}
    assert by['sensharma-xundl7'][1]['MR_sigma']=={'plus':.02,'minus':.03}
    assert [g['pol_fields'][0]['value_token'] for g in by['garg-xundl3']]==['-0.05','-0.2']
    assert [g['pol_fields'][0]['value_token'] for g in by['lv-xundl6']]==['0.04','-0.03']
    assert not datasets['garg-xundl3']['contains_2019erratum_DOI_or_code']
    result={'at':datetime.now(ZoneInfo('Asia/Shanghai')).isoformat(),'script_sha256':sha(Path(__file__)),
        'contract_sha256':sha(args.contract),'datasets':datasets,'selected_gamma_records':rowlist,
        'energy_only_decoy':decoy,'semantics':{'Garg_pol':'old2015 count asymmetry Delta','Lv_pol':'P from source Table1, not same asymmetry','Sensharma_MR':'angular_distribution 2026 original compilation; not a new independent2026 measurement'},
        'verification_scope':{'all_four_source_hashes_passed':True,'all8_parent_Egamma_exact_identities_passed':True,
            'Garg_selected_object_is_not_2019erratum_update':True,'selected_Adopted_emptyMR_not_new_constraint':True,
            'modern_arrays_response_gates_cov_recovered':False,'new_experimental_delta_or_wobbling_ranking':False}}
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'datasets':{k:{x:v[x] for x in ['line_count','MR_nonempty_gamma_count','contains_2019erratum_DOI_or_code']} for k,v in datasets.items()},'targets':[(z['dataset_name'],z['parent']['E'],z['E'],z['MR'],z['DMR']) for z in rowlist],'decoy':(decoy['parent']['E'],decoy['parent']['Jpi'],decoy['E'])},ensure_ascii=False,indent=2))


if __name__=='__main__':
    main()
