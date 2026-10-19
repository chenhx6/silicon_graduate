#!/usr/bin/env python3
"""Optional low-|m| preparation bound for the actual P00 marginal box.

An additional physical condition, not a recovered source prior or new parity.
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
import sympy as sp
from sympy.physics.wigner import clebsch_gordan,wigner_6j
from day16_rh99_population_feasibility import basis


def sha(p:Path)->str:return hashlib.sha256(p.read_bytes()).hexdigest()


def main()->None:
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--contract',type=Path,required=True);p.add_argument('--output',type=Path,required=True);args=p.parse_args();z=json.loads(args.contract.read_text());assert z['identity']=='RH99-1117-OPTIONAL-LOWM-BOUND-01';r=args.contract.parent;assert sha(r/z['base_contract'])==z['base_contract_sha256'] and sha(r/z['root_result'])==z['root_result_sha256'];cfg=json.loads((r/z['base_contract']).read_text());rr=json.loads((r/z['root_result']).read_text());J=sp.Rational(cfg['Ji2'],2);jf=sp.Rational(cfg['Jf2'],2)
    def coeff(L,Lp,k):return sp.simplify((-1)**(J+jf-1)*sp.sqrt((2*L+1)*(2*Lp+1)*(2*J+1))*clebsch_gordan(L,Lp,k,1,-1,0)*wigner_6j(L,Lp,k,J,J,jf))
    f11=coeff(1,1,2);ratio22=sp.simplify(coeff(2,2,2)/f11);crosssquare=sp.simplify((coeff(1,2,2)/f11)**2);assert ratio22==sp.Rational(13,35) and crosssquare==sp.Rational(63,5)
    K,pairs=basis(cfg,cfg['families']['sameParity_M1E2']);m=np.array([float(J-i) for i in range(len(pairs))]);lowbound=float(J*(J+1)/3)
    moment=(3*m*m-float(J*(J+1)))/float(2*J*(2*J-1));assert np.max(abs(moment-K['A2'][0]))<1e-12
    d=sp.symbols('delta',real=True);s=sp.sqrt(crosssquare);t=ratio22
    F=1-2*s*d+t*d*d;G=sp.Rational(3,2)+s*d+sp.Rational(3,2)*t*d*d
    derivative=sp.factor(sp.diff(G/F,d));critical=-1/sp.sqrt(t);rmin=sp.simplify((G/F).subs(d,critical));assert float(F.subs(d,critical))>0 and float(rmin)<0
    assert sp.simplify(sp.diff(G/F,d).subs(d,critical))==0
    box=cfg['source_margin_box'];corners=[]
    for a2 in box['a2']:
        for a4 in box['a4']:
            maximum=float((rmin*a2+sp.Rational(5,8)*a4)/(1-.5*a2+.375*a4));corners.append({'a2':a2,'a4':a4,'Pupper':maximum})
    maxP=max(x['Pupper'] for x in corners);assert maxP<box['P90'][0]
    # Independent dense scan validates the analytic scalar bound, without
    # assuming scan0 can exclude roots.
    beta=np.linspace(-math.pi/2,math.pi/2,100001);DD=np.tan(beta[1:-1]);FF=1-2*float(s)*DD+float(t)*DD*DD;GG=1.5+float(s)*DD+1.5*float(t)*DD*DD;values=GG[FF>0]/FF[FF>0];assert np.min(values)>=float(rmin)-1e-9
    # Sourcebox pureE1 strict-positive q with optional lowM condition.
    E,pairs=basis(cfg,cfg['families']['oppositeParity_E1M2']);v={key:val[0] for key,val in E.items()};n=len(m);Aeq=np.array([np.r_[np.ones(n),0.]]);beq=np.array([1.]);Aub=[np.r_[-np.eye(n)[i],1.] for i in range(n)];bub=[0.]*n
    constraints=[v['A2'],-v['A2'],v['A4'],-v['A4'],v['Q90']-box['P90'][1]*v['I90'],-v['Q90']+box['P90'][0]*v['I90'],m*m]
    Aub.extend([np.r_[x,0.] for x in constraints]);bub.extend([box['a2'][1],-box['a2'][0],box['a4'][1],-box['a4'][0],0.,0.,lowbound]);Aub=np.array(Aub);bub=np.array(bub);lp=linprog(np.r_[np.zeros(n),-1.],A_ub=Aub,b_ub=bub,A_eq=Aeq,b_eq=beq,bounds=[(0,None)]*n+[(0,1/n)],method=cfg['LP']['method'],options={'primal_feasibility_tolerance':cfg['LP']['primal_tolerance'],'dual_feasibility_tolerance':cfg['LP']['dual_tolerance']});assert lp.success and lp.x[-1]>1e-8;res=max(float(np.max(abs(Aeq@lp.x-beq))),max(0.,float(np.max(Aub@lp.x-bub))));assert res<cfg['LP']['witness_residual_acceptance'];q=lp.x[:n];obs={key:float(val@q) for key,val in v.items()}
    central=next(x for x in rr['isolated_central_roots'] if x['feasible']);central_m2=float(np.array(central['q_pair'])@(m*m));assert central_m2>lowbound
    result={'at':datetime.now(ZoneInfo('Asia/Shanghai')).isoformat(),'script_sha256':sha(Path(__file__)),'contract_sha256':sha(args.contract),'source_and_previous_results_unchanged':True,
        'exact_independent_F2_ratios':{'F22_over_F11':str(ratio22),'F12_over_F11_squared':str(crosssquare),'native_interference_sign_not_inferred_from_this_route':True},
        'optional_mean_bound':{'J':float(J),'m2_isotropic':lowbound,'B2_definition':'sumq [3m²-J(J+1)]/[2J(2J-1)]','kernelvertex_max_error':float(np.max(abs(moment-K['A2'][0]))),'not_a_measured_source_condition':True},
        'analytic_bound':{'F':str(F),'G':str(G),'d_ratio':str(derivative),'min_G_over_F_on_Fpositive':str(rmin),'numeric_min':float(rmin),'delta_at_min':str(critical),'corner_bounds':corners,'global_Pupper_sameParity_given_lowM':maxP,'sourcebox_Pminimum':box['P90'][0],'allreal_delta_bound_not_only_grid':True,'dense_sanity_points':100001},
        'oppositeParity_pureE1_strict_witness':{'q_pair':q.tolist(),'minimum_q_pair':float(min(q)),'a2':obs['A2'],'a4':obs['A4'],'I90':obs['I90'],'P90':obs['Q90']/obs['I90'],'mean_m2':float(q@(m*m)),'max_constraint_residual':res},
        'old_central_M1E2_witness_optional_bound_violation':{'mean_m2':central_m2,'optional_limit':lowbound},
        'scope':{'conditional_input_design_not_source_orientation_measurement':True,'no_newexperimental_parity_or_delta':True,'no_Gaussian_width_fitted':True,'post_results_design':True}}
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps({k:result[k] for k in ['exact_independent_F2_ratios','optional_mean_bound','analytic_bound','old_central_M1E2_witness_optional_bound_violation']},ensure_ascii=False,indent=2))


if __name__=='__main__':main()
