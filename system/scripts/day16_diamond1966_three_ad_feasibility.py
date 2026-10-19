#!/usr/bin/env python3
"""Conditional positive-population witnesses for D66's three actual ADs.

Same-parent constraints are explicit. A finite grid provides existence
witnesses only; zero hits never exclude a spin sequence or continuous root.
"""
from __future__ import annotations
import argparse
from datetime import datetime
from functools import lru_cache
import hashlib
import json
import math
from pathlib import Path
from zoneinfo import ZoneInfo
import numpy as np
from scipy.optimize import linprog
from day16_co60_conditional_stokes import operators
from day16_rh99_population_feasibility import pair_kernel


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


@lru_cache(None)
def kernel(Ji2,Jf2,nodes):
    n=Ji2+1;pairs=[(i,n-1-i) for i in range(n//2)]
    x,w=np.polynomial.legendre.leggauss(nodes);vals=[]
    for z in x:
        th=math.acos(float(z));L=operators(Ji2,Jf2,(("M",1,1.),),th,0.,'native')
        H=operators(Ji2,Jf2,(("E",2,1.),),th,0.,'native')
        vals.append(pair_kernel(L,H,pairs)[:,0,:])
    vals=np.array(vals);out={}
    for k in [0,2,4,6,8]:
        pol=np.polynomial.legendre.legval(x,[0]*k+[1])
        out[k]=(2*k+1)/2*np.einsum('a,akj->kj',w*pol,vals)
    allowed_low=abs(Ji2-Jf2)<=2
    assert np.max(abs(out[0][1]-1))<1e-12
    assert np.max(abs(out[0][0]-(1 if allowed_low else 0)))<1e-12
    assert np.max(abs(out[0][2]))<1e-12
    assert max(np.max(abs(out[k])) for k in [6,8])<1e-12
    assert np.max(abs(out[4][0]))<1e-12 and np.max(abs(out[4][2]))<1e-12
    th=.731
    def values(components):
        return pair_kernel(operators(Ji2,Jf2,((components[0],1,1.),),th,0.,'native'),
            operators(Ji2,Jf2,((components[1],2,1.),),th,0.,'native'),pairs)[:,0,:]
    assert np.max(abs(values(('M','E'))-values(('E','M'))))<1e-12
    return out


def beta_values(Ji2,Jf2,step):
    if abs(Ji2-Jf2)==4:return [-90.]
    return sorted([float(x) for x in range(-90,90,step)],key=lambda x:(abs(x),x))


def coefficients(Ji2,Jf2,beta,nodes):
    K=kernel(Ji2,Jf2,nodes);rad=math.radians(beta);co,si=math.cos(rad),math.sin(rad)
    if beta==-90:co,si=0.,-1.
    weight=np.array([co*co,si*si,2*co*si])
    return {k:weight@K[k] for k in [2,4]}


def witness(Ji2,obs_vectors,mode,cfg):
    n=(Ji2+1)//2;Aub=[np.r_[-np.eye(n)[i],1.] for i in range(n)];bub=[0.]*n
    for line,vec in obs_vectors:
        for rank in [2,4]:
            mean,err=cfg['observations'][line]['a'+str(rank)];v=vec[rank]
            Aub += [np.r_[v,0.],np.r_[-v,0.]];bub += [mean+err,-mean+err]
    J=Ji2/2;m=np.array([J-i for i in range(n)])
    u2=(3*m*m-J*(J+1))/(2*J*(2*J-1))
    if mode=='extra_lowm_u2nonpositive':Aub.append(np.r_[u2,0.]);bub.append(0.)
    Aub=np.array(Aub);bub=np.array(bub);Aeq=np.array([np.r_[np.ones(n),0.]])
    opts={'primal_feasibility_tolerance':cfg['LP']['primal_tolerance'],
          'dual_feasibility_tolerance':cfg['LP']['dual_tolerance']}
    fit=linprog(np.r_[np.zeros(n),-1.],A_ub=Aub,b_ub=bub,A_eq=Aeq,b_eq=[1.],
        bounds=[(0,None)]*n+[(0,1/n)],method=cfg['LP']['method'],options=opts)
    if not fit.success:
        assert fit.status==2,fit.message
        return None
    residual=max(float(np.max(abs(Aeq@fit.x-1))),max(0.,float(np.max(Aub@fit.x-bub))),max(0.,-float(np.min(fit.x))))
    assert residual<cfg['LP']['witness_tolerance']
    if fit.x[-1]<cfg['LP']['strict_pair_probability']:return None
    q=fit.x[:n]
    return {'q_pair':q.tolist(),'pair_abs_m':m.tolist(),'minimum_pair_probability':float(min(q)),
        'max_constraint_residual':residual,'u2_population':float(u2@q),
        'observations':{line:{'a'+str(rank):float(v[rank]@q) for rank in [2,4]} for line,v in obs_vectors}}


def main() -> None:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--contract',required=True,type=Path)
    ap.add_argument('--output',required=True,type=Path)
    a=ap.parse_args();c=json.loads(a.contract.read_text());assert c['identity']=='D66-FIG2-THREE-AD-CONDITIONAL-FEASIBILITY-01'
    root=Path(__file__).resolve().parents[2];assert sha(root/c['raw'])==c['raw_sha256']
    assert sha(root/c['source'])==c['source_current_sha256']
    for p,h in c['fixed_helpers'].items():assert sha(root/p)==h
    bottom=c['known_bottom_spin2'];spins=c['top_and_middle_spin2_candidates'];nodes=c['quadrature_nodes'];step=c['grid']['beta_step_deg']
    sequences=[(top,mid) for top in spins for mid in spins if abs(top-mid)<=4 and abs(top-bottom)<=4 and abs(mid-bottom)<=4];assert len(sequences)==19
    # The independent middle-level population is not inferred by pretending
    # that all feeding came from the observed 331 branch.
    middle={};trials=0
    for mid in spins:
        for mode in c['population_modes']:
            found=None
            for beta in beta_values(mid,bottom,step):
                trials+=1;v=coefficients(mid,bottom,beta,nodes);q=witness(mid,[('370',v)],mode,c)
                if q is not None:
                    found={'beta_native_deg':beta,'delta_native':None if beta==-90 else math.tan(math.radians(beta)),'pureL2':beta==-90,**q};break
            middle[str(mid)+':'+mode]=found
    rows=[]
    for top,mid in sequences:
        K1=kernel(top,mid,nodes);K2=kernel(top,bottom,nodes)
        v1,v2=K1[4][1],K2[4][1];r4=float(np.dot(v1,v2)/np.dot(v2,v2));err=float(np.max(abs(v1-r4*v2)));assert err<1e-12
        central_product=c['observations']['331']['a4'][0]*c['observations']['701']['a4'][0]
        central_sign_impossible=(r4<0 and central_product>0)
        for mode in c['population_modes']:
            found=None;attempts=0
            if middle[str(mid)+':'+mode] is not None:
                for b1 in beta_values(top,mid,step):
                    v331=coefficients(top,mid,b1,nodes)
                    for b2 in beta_values(top,bottom,step):
                        attempts+=1;trials+=1
                        v701=coefficients(top,bottom,b2,nodes)
                        q=witness(top,[('331',v331),('701',v701)],mode,c)
                        if q is not None:
                            found={'beta331_native_deg':b1,'beta701_native_deg':b2,
                                'delta331_native':None if b1==-90 else math.tan(math.radians(b1)),
                                'delta701_native':None if b2==-90 else math.tan(math.radians(b2)),
                                'pureL2_331':b1==-90,'pureL2_701':b2==-90,**q};break
                    if found is not None:break
            row={'top_spin2':top,'middle_spin2':mid,'bottom_spin2':bottom,'population_mode':mode,
                'source_listed_probable_pair':[top,mid] in c['source_probable_pairs2'],
                'central_rank4_necessary_relation':{'pureE2_A4_331_over_701':r4,
                    'basis_proportionality_max_error':err,
                    'exact_nonzero_central_A4_pair_sign_impossible':central_sign_impossible,
                    'not_an_exclusion_of_quoted_errors_or_source_spin':True},
                'grid_attempts':attempts,'strict_upper_witness':found,
                'middle_witness_key':str(mid)+':'+mode,
                'zero_hit_not_full_parameter_exclusion':True}
            rows.append(row)
            print('pair',top,mid,mode,'strictwitness',found is not None,'trials',attempts,flush=True)
    output={'at':datetime.now(ZoneInfo('Asia/Shanghai')).isoformat(),'script_sha256':sha(Path(__file__)),
        'contract_sha256':sha(a.contract),'raw_source_helpers_unchanged':True,
        'nineteen_sequences':[[p,q] for p,q in sequences],
        'middle_level_witnesses':middle,'sameparent_results':rows,'LP_grid_trials':trials,
        'summary':{mode:{'strict_grid_witness_count':sum(q['population_mode']==mode and q['strict_upper_witness'] is not None for q in rows),
            'not_probability_or_complete_spin_count':True} for mode in c['population_modes']},
        'scope':{'published_AD_marginal_box_not_jointCI':True,'no_new_experimental_spin_delta_or_parity':True,
            'not_replay_of_author_nineteen_to_five_or_their_response':True,
            'native_delta_not_source_convention':True,'no_toy_counts_generated':True}}
    a.output.write_text(json.dumps(output,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'summary':output['summary'],'LP_grid_trials':trials},ensure_ascii=False,indent=2))


if __name__=='__main__':main()
