#!/usr/bin/env python3
"""Post-grid isolated-root check with unchanged source inputs and LP controls."""
from __future__ import annotations
import argparse
from datetime import datetime
import hashlib
import json
import math
from pathlib import Path
from zoneinfo import ZoneInfo
import numpy as np
from scipy.optimize import linprog
from day16_rh99_population_feasibility import basis


def sha(p:Path)->str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main()->None:
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--contract',type=Path,required=True);p.add_argument('--output',type=Path,required=True);args=p.parse_args();k=json.loads(args.contract.read_text());assert k['identity']=='RH99-1117-ROOT-AWARE-CENTRAL-01';r=args.contract.parent;root=Path(__file__).resolve().parents[2]
    assert sha(r/k['v1_contract'])==k['v1_contract_sha256'] and sha(r/k['v1_result'])==k['v1_result_sha256'] and sha(root/k['base_script'])==k['base_script_sha256'];cfg=json.loads((r/k['v1_contract']).read_text());central=cfg['source_central'];a,b,obsP=central['a2'],central['a4'],central['P90'];Iobs=1-.5*a+.375*b
    rows=[];decompositions={}
    for name,parts in cfg['families'].items():
        K,pairs=basis(cfg,parts);B2=K['A2'][0];B4=K['A4'][1];vectors=np.column_stack([B2,B4]);coeff={};maxerr=0.
        for key in ['A2','A4','Q90']:
            coeff[key]=[]
            for component in K[key]:
                c=np.linalg.lstsq(vectors,component,rcond=None)[0];maxerr=max(maxerr,float(np.max(abs(vectors@c-component))));coeff[key].append(c)
        assert maxerr<k['rank_identity_tolerance']
        coeff={key:np.array(v) for key,v in coeff.items()};assert np.max(abs(coeff['A2'][:,1]))<1e-12 and np.max(abs(coeff['A4'][[0,2]]))<1e-12
        Fa=coeff['A2'][:,0];Ga=coeff['Q90'][:,0];G4=coeff['Q90'][1,1]
        # Component order LL,HH,LH gives quadratic [constant,linear,squared].
        poly=lambda z:np.array([z[0],2*z[2],z[1]])
        F=poly(Fa);G=poly(Ga);H=a*G-(obsP*Iobs-b*G4)*F
        roots=np.polynomial.polynomial.polyroots(H)
        decompositions[name]={'coefficients_A2':coeff['A2'].tolist(),'coefficients_A4':coeff['A4'].tolist(),'coefficients_Q90':coeff['Q90'].tolist(),'maximum_rank_map_error':maxerr,'central_root_polynomial_ascending':H.tolist(),'roots_complex':[[float(t.real),float(t.imag)] for t in roots]}
        for value in roots:
            if abs(value.imag)>k['root_imag_tolerance']:continue
            delta=float(value.real);Fdelta=float(np.polynomial.polynomial.polyval(delta,F));row={'family':name,'delta_native':delta,'beta_native_deg':math.degrees(math.atan(delta)),'F2_scalar':Fdelta}
            if abs(Fdelta)<k['F2_pole_rejection_tolerance']:
                row.update(feasible=False,reason='F2zero; source nonzeroa2 cannotbe matched by finiteB2');rows.append(row);continue
            norm=1+delta*delta;weights=np.array([1,delta*delta,2*delta])/norm;v={key:weights@val for key,val in K.items()};Aeq=np.array([np.ones(len(pairs)),v['A2'],v['A4'],v['Q90']-obsP*v['I90']]);beq=np.array([1,a,b,0.]);lp=linprog(np.zeros(len(pairs)),A_eq=Aeq,b_eq=beq,bounds=(0,None),method=cfg['LP']['method'],options={'primal_feasibility_tolerance':cfg['LP']['primal_tolerance'],'dual_feasibility_tolerance':cfg['LP']['dual_tolerance']});row['solver_status']=int(lp.status);row['feasible']=bool(lp.success)
            if lp.success:
                q=lp.x;res=max(float(np.max(abs(Aeq@q-beq))),max(0.,-float(np.min(q))));assert res<cfg['LP']['witness_residual_acceptance'];obs={key:float(val@q) for key,val in v.items()};assert obs['I90']>0
                row.update(q_pair=q.tolist(),a2=obs['A2'],a4=obs['A4'],I90=obs['I90'],P90=obs['Q90']/obs['I90'],max_constraint_residual=res)
            else:row['reason']=lp.message
            rows.append(row)
    result={'at':datetime.now(ZoneInfo('Asia/Shanghai')).isoformat(),'script_sha256':sha(Path(__file__)),'contract_sha256':sha(args.contract),'base_script_sha256':k['base_script_sha256'],'v1_source_and_inputs_unchanged':True,'post_grid_check_not_preregistered':True,'rank_decompositions':decompositions,'isolated_central_roots':rows,'scope':{'grid_zero_cannot_exclude_isolatedroots':True,'central_roots_not_experimental_confidence_or_delta_refit':True,'Palit_or_KS_phase_coordinate_not_established':True,'no_source_cov_response_or_alignment_recovered':True}}
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'root_checks':[{k:v for k,v in row.items() if k not in ['q_pair','reason']} for row in rows],'infeasible_reasons':[row.get('reason') for row in rows if not row['feasible']]},ensure_ascii=False,indent=2))


if __name__=='__main__':
    main()
