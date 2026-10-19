#!/usr/bin/env python3
"""Convex separation and strictly positive q witnesses for declared P00 model."""
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
from scipy.spatial import ConvexHull
from day16_rh99_population_feasibility import basis


def sha(path:Path)->str:return hashlib.sha256(path.read_bytes()).hexdigest()


def main()->None:
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--contract',type=Path,required=True);p.add_argument('--output',type=Path,required=True);args=p.parse_args();z=json.loads(args.contract.read_text());assert z['identity']=='RH99-1117-MOMENT-CERTIFICATE-01';r=args.contract.parent
    assert sha(r/z['base_contract'])==z['base_contract_sha256'] and sha(r/z['root_result'])==z['root_result_sha256'];cfg=json.loads((r/z['base_contract']).read_text());rr=json.loads((r/z['root_result']).read_text());kernels={name:basis(cfg,parts)[0] for name,parts in cfg['families'].items()};K=kernels['sameParity_M1E2'];vertices=np.column_stack([K['A2'][0],K['A4'][1]]);hull=ConvexHull(vertices);certs=[]
    for root in rr['isolated_central_roots']:
        if root['feasible']:continue
        name=root['family'];d=root['delta_native'];weights=np.array([1,d*d,2*d])/(1+d*d)
        decomp=rr['rank_decompositions'][name];f2=float(weights@np.array(decomp['coefficients_A2'])[:,0]);f4=float(weights@np.array(decomp['coefficients_A4'])[:,1]);target=np.array([cfg['source_central']['a2']/f2,cfg['source_central']['a4']/f4]);violations=hull.equations[:,:2]@target+hull.equations[:,2];ix=int(np.argmax(violations));equation=hull.equations[ix];vertexlhs=vertices@equation[:2]+equation[2];margin=float(violations[ix]);assert margin>1e-8 and np.max(vertexlhs)<1e-12
        certs.append({'family':name,'delta_native':d,'required_moment2_4':target.tolist(),'inequality':'normal dot moment + offset <=0 for everyphysicalvertex','normal':equation[:2].tolist(),'offset':float(equation[2]),'max_lhs_all12_vertices':float(np.max(vertexlhs)),'required_point_lhs':margin,'strictly_separated':True})
    witnesses=[];options={'primal_feasibility_tolerance':cfg['LP']['primal_tolerance'],'dual_feasibility_tolerance':cfg['LP']['dual_tolerance']}
    for request in z['witness_requests']:
        name=request['family'];mode=request['mode'];KK=kernels[name]
        if mode=='exactcentral':d=next(x['delta_native'] for x in rr['isolated_central_roots'] if x['family']==name and x['feasible']);rad=math.atan(d)
        else:rad=math.radians(request['beta_deg']);d=math.tan(rad)
        cs,ss=math.cos(rad),math.sin(rad);weights=np.array([cs*cs,ss*ss,2*cs*ss]);v={key:weights@matrix for key,matrix in KK.items()};n=len(v['A2']);Aeq=[np.r_[np.ones(n),0.]];beq=[1.]
        Aub=[np.r_[-np.eye(n)[i],1.] for i in range(n)];bub=[0.]*n
        if mode=='exactcentral':
            a=cfg['source_central'];Aeq.extend([np.r_[v['A2'],0.],np.r_[v['A4'],0.],np.r_[v['Q90']-a['P90']*v['I90'],0.]]);beq.extend([a['a2'],a['a4'],0.])
        else:
            a=cfg['source_margin_box'];new=[v['A2'],-v['A2'],v['A4'],-v['A4'],v['Q90']-a['P90'][1]*v['I90'],-v['Q90']+a['P90'][0]*v['I90']];Aub.extend([np.r_[x,0.] for x in new]);bub.extend([a['a2'][1],-a['a2'][0],a['a4'][1],-a['a4'][0],0.,0.])
        Aeq=np.array(Aeq);beq=np.array(beq);Aub=np.array(Aub);bub=np.array(bub);lp=linprog(np.r_[np.zeros(n),-1.],A_ub=Aub,b_ub=bub,A_eq=Aeq,b_eq=beq,bounds=[(0,None)]*n+[(0,1/n)],method=cfg['LP']['method'],options=options);assert lp.success,(request,lp.message);q=lp.x[:n];epsilon=float(lp.x[-1]);res=max(float(np.max(abs(Aeq@lp.x-beq))),max(0.,float(np.max(Aub@lp.x-bub))));assert res<cfg['LP']['witness_residual_acceptance'] and epsilon>1e-8 and min(q)>=epsilon-1e-8
        obs={key:float(value@q) for key,value in v.items()};P=obs['Q90']/obs['I90'];assert obs['I90']>0 and abs(P)<=1+1e-10
        witnesses.append({'family':name,'mode':mode,'delta_native':d,'beta_native_deg':math.degrees(rad),'epsilon_all_pairs':epsilon,'minimum_pair_probability':float(min(q)),'q_pair':q.tolist(),'a2':obs['A2'],'a4':obs['A4'],'I90':obs['I90'],'P90':P,'max_constraint_residual':res})
    result={'at':datetime.now(ZoneInfo('Asia/Shanghai')).isoformat(),'script_sha256':sha(Path(__file__)),'contract_sha256':sha(args.contract),'base_and_root_inputs_unchanged':True,'moment_vertices':vertices.tolist(),'separation_certificates':certs,'strictly_positive_witnesses':witnesses,'no_experiment_delta_CI_or_parity_assignment':True,'design_is_post_results':True};args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'certificates':certs,'strict_witnesses':[{k:v for k,v in x.items() if k!='q_pair'} for x in witnesses]},ensure_ascii=False,indent=2))


if __name__=='__main__':main()
