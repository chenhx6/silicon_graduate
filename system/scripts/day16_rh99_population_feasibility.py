#!/usr/bin/env python3
"""Conditional LP feasibility for P00's actual AD/P summary, not a delta fit.

Physical q(m)>=0, source marginal boxes, local Jones axes and phase coordinates
are explicit. Scan cells/boxes are not confidence regions or experimental data.
"""
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
from day16_co60_conditional_stokes import operators,LINEAR_BASIS


def sha(path:Path)->str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def pair_kernel(opsL,opsH,mabs):
    # Output shape: component(LL,HH,LH) x (I,Q) x positive|m|pair.
    ans=np.zeros((3,2,len(mabs)))
    for j,(negative,positive) in enumerate(mabs):
        for col in [negative,positive]:
            L,H=opsL[:,:,col],opsH[:,:,col]
            mats=[L@L.conj().T,H@H.conj().T,(L@H.conj().T+H@L.conj().T)/2]
            for k,tau in enumerate(mats):
                lin=LINEAR_BASIS@tau@LINEAR_BASIS.conj().T
                ans[k,0,j]+=2*math.pi*np.trace(lin).real
                ans[k,1,j]+=2*math.pi*(lin[0,0]-lin[1,1]).real
    return ans


def basis(cfg,parts):
    ji,jf=cfg['Ji2'],cfg['Jf2'];n=ji+1
    pairs=[(i,n-1-i) for i in range(n//2)]
    x,w=np.polynomial.legendre.leggauss(cfg['quadrature_nodes'])
    vals=[]
    for cosine in x:
        angle=math.acos(float(cosine))
        l=operators(ji,jf,((parts[0][0],parts[0][1],1.),),angle,0.,'native')
        h=operators(ji,jf,((parts[1][0],parts[1][1],1.),),angle,0.,'native')
        vals.append(pair_kernel(l,h,pairs))
    vals=np.array(vals)
    coeff={}
    for rank in [0,2,4,6,8]:
        pol=np.polynomial.legendre.legval(x,[0]*rank+[1])
        coeff[rank]=(2*rank+1)/2*np.einsum('a,akj->kj',w*pol,vals[:,:,0,:])
    assert np.max(abs(coeff[0][0:2]-1))<1e-12
    assert np.max(abs(coeff[0][2]))<1e-12
    assert max(np.max(abs(coeff[k])) for k in [6,8])<1e-12
    l=operators(ji,jf,((parts[0][0],parts[0][1],1.),),math.pi/2,0.,'native')
    h=operators(ji,jf,((parts[1][0],parts[1][1],1.),),math.pi/2,0.,'native')
    at90=pair_kernel(l,h,pairs)
    rec=coeff[0]-.5*coeff[2]+.375*coeff[4]
    assert np.max(abs(rec-at90[:,0,:]))<1e-12
    return {'A2':coeff[2],'A4':coeff[4],'I90':at90[:,0,:],'Q90':at90[:,1,:]},pairs


def main()->None:
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--contract',type=Path,required=True);p.add_argument('--output',type=Path,required=True);args=p.parse_args();cfg=json.loads(args.contract.read_text());assert cfg['identity']=='RH99-1117-ACTUAL-OBSERVABLE-FEASIBILITY-01'
    root=Path(__file__).resolve().parents[2];raw=root/'tmp/day16-palit2000/springer-pdf.pdf';assert sha(raw)==cfg['source_sha256']
    for path,digest in cfg['fixed_helper_hashes'].items():assert sha(root/path)==digest
    kernels={};pairs=None
    for name,parts in cfg['families'].items():kernels[name],pairs=basis(cfg,parts)
    same=kernels['sameParity_M1E2'];opp=kernels['oppositeParity_E1M2']
    for key in ['A2','A4','I90']:assert np.max(abs(same[key]-opp[key]))<1e-12
    assert np.max(abs(same['Q90']+opp['Q90']))<1e-12
    # Independent pure dipole Eq3 check has A4=0 exactly for each q vertex.
    assert np.max(abs(same['A4'][0]))<1e-12
    pure_relation=3*same['A2'][0]/(2-same['A2'][0])
    assert np.max(abs(pure_relation-same['Q90'][0]/same['I90'][0]))<1e-12
    grid=cfg['grid'];betas=np.arange(grid['start_deg'],grid['stop_deg']+grid['step_deg']/2,grid['step_deg'])
    rows=[];numerical_boundaries=[]
    options={'primal_feasibility_tolerance':cfg['LP']['primal_tolerance'],'dual_feasibility_tolerance':cfg['LP']['dual_tolerance']}
    for name,K in kernels.items():
        for beta in betas:
            rad=math.radians(float(beta));cs=math.cos(rad);ss=math.sin(rad)
            if abs(beta)==90:cs=0.;ss=math.copysign(1.,beta)
            weights=np.array([cs*cs,ss*ss,2*cs*ss])
            v={key:weights@matrix for key,matrix in K.items()}
            for mode in cfg['LP']['modes']:
                if mode=='exactcentral':
                    z=cfg['source_central'];Aeq=np.array([np.ones(len(pairs)),v['A2'],v['A4'],v['Q90']-z['P90']*v['I90']]);beq=np.array([1,z['a2'],z['a4'],0]);Aub=bub=None
                else:
                    z=cfg['source_margin_box'];Aeq=np.ones((1,len(pairs)));beq=np.array([1.]);Aub=np.array([v['A2'],-v['A2'],v['A4'],-v['A4'],v['Q90']-z['P90'][1]*v['I90'],-v['Q90']+z['P90'][0]*v['I90']]);bub=np.array([z['a2'][1],-z['a2'][0],z['a4'][1],-z['a4'][0],0.,0.])
                lp=linprog(np.zeros(len(pairs)),A_ub=Aub,b_ub=bub,A_eq=Aeq,b_eq=beq,bounds=(0,None),method=cfg['LP']['method'],options=options)
                row={'family':name,'mode':mode,'beta_native_deg':float(beta),'delta_native':float(ss/cs) if cs else None,'pure_upper':bool(cs==0),'solver_status':int(lp.status),'feasible':False}
                if lp.success:
                    q=lp.x
                    residual=max(float(np.max(abs(Aeq@q-beq))),max(0.,-float(np.min(q))))
                    if Aub is not None:residual=max(residual,max(0.,float(np.max(Aub@q-bub))))
                    assert residual<cfg['LP']['witness_residual_acceptance'],(name,mode,beta,residual)
                    obs={key:float(values@q) for key,values in v.items()};assert obs['I90']>0
                    P=obs['Q90']/obs['I90'];assert abs(P)<=1+1e-10
                    row.update(feasible=True,q_pair=q.tolist(),a2=obs['A2'],a4=obs['A4'],I90=obs['I90'],P90=P,max_constraint_residual=residual)
                elif lp.status!=2:numerical_boundaries.append(dict(row,message=lp.message))
                rows.append(row)
    windows=[]
    for name in kernels:
        for mode in cfg['LP']['modes']:
            selected=[r for r in rows if r['family']==name and r['mode']==mode]
            starts=[];run=[]
            for row in selected:
                if row['feasible']:run.append(row)
                elif run:starts.append(run);run=[]
            if run:starts.append(run)
            windows.append({'family':name,'mode':mode,'feasible_grid_count':sum(r['feasible'] for r in selected),
                'windows_beta_deg':[[a[0]['beta_native_deg'],a[-1]['beta_native_deg']] for a in starts],
                'not_exact_interval_or_confidence_region':True})
    representatives=[]
    for name in kernels:
        for mode in cfg['LP']['modes']:
            feasible=[r for r in rows if r['family']==name and r['mode']==mode and r['feasible']]
            for target in [-60.,0.,60.]:
                if feasible:
                    chosen=min(feasible,key=lambda z:abs(z['beta_native_deg']-target))
                    if chosen not in representatives:representatives.append(chosen)
    result={'at':datetime.now(ZoneInfo('Asia/Shanghai')).isoformat(),'script_sha256':sha(Path(__file__)),'contract_sha256':sha(args.contract),'source_sha256':cfg['source_sha256'],'fixed_helpers_unchanged':True,
        'pair_abs_m':[str((cfg['Ji2']-2*i)/2) for i in range(len(pairs))],
        'kernel_validation':{'all_pure_basis_integrals_one':True,'mixed_cross_integral_zero':True,'rank6_8_absmax_lt1e12_inverse':True,'pointI90_from_legendre':True,'EMdual_I_same_Q_opposite':True,'pureM1_relation_to_a2':True},
        'window_summary':windows,'representative_witnesses':representatives,'numerical_boundaries':numerical_boundaries,'all_rows':rows,
        'scope':{'mathematical_box_not_jointCI':True,'detector_response_cov_and_phase_bridge_to_P00_not_recovered':True,'actual_delta_refit_or_new_parity_assignment':False,'new_toy_counts_generated':False}}
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps({'windows':windows,'numerical_boundary_count':len(numerical_boundaries),'representatives':[(r['family'],r['mode'],r['beta_native_deg'],r['delta_native'],r['a2'],r['a4'],r['P90']) for r in representatives]},ensure_ascii=False,indent=2))


if __name__=='__main__':
    main()
