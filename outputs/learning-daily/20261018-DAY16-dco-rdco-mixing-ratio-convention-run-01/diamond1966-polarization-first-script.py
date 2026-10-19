#!/usr/bin/env python3
"""D66 fixed-amplitude polarization companion projections, not a P fit.

Only existing AD-compatible beta points are used. Fractional-LP ranges project
over their common-parent populations; they are not full mixing-ratio profiles
or simultaneous rectangular confidence regions.
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
from day16_co60_conditional_stokes import operators,pair_kernel
from day16_diamond1966_three_ad_feasibility import kernel,coefficients


def sha(p:Path)->str:return hashlib.sha256(p.read_bytes()).hexdigest()


@lru_cache(None)
def at90(Ji2,Jf2,dual=False):
    pairs=[(i,Ji2-i) for i in range((Ji2+1)//2)]
    kinds=('E','M') if dual else ('M','E')
    a=operators(Ji2,Jf2,((kinds[0],1,1.),),math.pi/2,0.,'native')
    b=operators(Ji2,Jf2,((kinds[1],2,1.),),math.pi/2,0.,'native')
    return pair_kernel(a,b,pairs)


def weight(beta):
    z=math.radians(beta);co,si=math.cos(z),math.sin(z)
    if beta==-90:co,si=0.,-1.
    return np.array([co*co,si*si,2*co*si])


def actual_vectors(top,mid,betas,base):
    return {line:coefficients(top,jf,b,base['quadrature_nodes']) for line,jf,b in [('331',mid,betas[0]),('701',9,betas[1])]}


def constraints(top,vectors,mode,base):
    A=[];b=[]
    for line,vals in vectors.items():
        for rank in [2,4]:
            mean,err=base['observations'][line]['a'+str(rank)]
            A += [vals[rank],-vals[rank]];b += [mean+err,-mean+err]
    if mode=='extra_lowm_u2nonpositive':
        J=top/2;m=np.array([J-i for i in range((top+1)//2)])
        A.append((3*m*m-J*(J+1))/(2*J*(2*J-1)));b.append(0.)
    return np.array(A),np.array(b)


def project_P(numerator,intensity,A,b):
    n=len(intensity);eq=np.array([np.r_[np.ones(n),-1.],np.r_[intensity,0.]])
    ub=np.column_stack((A,-b));outputs=[]
    for sign in [1.,-1.]:
        fit=linprog(np.r_[sign*numerator,0.],A_ub=ub,b_ub=np.zeros(len(b)),A_eq=eq,b_eq=[0.,1.],
            bounds=[(0,None)]*n+[(0,None)],method='highs')
        assert fit.success and fit.x[-1]>0
        q=fit.x[:n]/fit.x[-1];P=float(numerator@q/(intensity@q))
        assert abs(q.sum()-1)<1e-8 and min(q)>-1e-8 and np.max(A@q-b)<1e-8
        assert -1-1e-9<=P<=1+1e-9
        outputs.append({'P':P,'q_pair':q.tolist(),'I90':float(intensity@q),
            'max_constraint_residual':max(abs(q.sum()-1),max(0.,float(np.max(A@q-b))))})
    assert outputs[0]['P']<=outputs[1]['P']+1e-10
    return {'P_min':outputs[0]['P'],'P_max':outputs[1]['P'],'endpoint_witnesses':outputs,
        'fixed_betas_only_not_fullprofile_or_jointCI':True}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--contract',required=True,type=Path);p.add_argument('--output',required=True,type=Path);args=p.parse_args();c=json.loads(args.contract.read_text());assert c['identity']=='D66-FIXED-AMPLITUDE-POLARIZATION-COMPANION-01';r=args.contract.parent
    for name in ['base_contract','grid_result','domain_result','replay_result']:assert sha(r/c[name])==c[name+'_sha256']
    base=json.loads((r/c['base_contract']).read_text());grid=json.loads((r/c['grid_result']).read_text());domain=json.loads((r/c['domain_result']).read_text());replay=json.loads((r/c['replay_result']).read_text())
    max_pure=max_dual=max_I=0.
    for top,mid in grid['nineteen_sequences']:
        for jf in [mid,9]:
            K=kernel(top,jf,base['quadrature_nodes']);V=at90(top,jf);D=at90(top,jf,True)
            max_pure=max(max_pure,float(np.max(abs(V[0,1]-1.5*K[2][0]))),
                float(np.max(abs(V[1,1]-1.5*K[2][1]-.625*K[4][1]))))
            max_dual=max(max_dual,float(np.max(abs(V[:,0]-D[:,0]))),float(np.max(abs(V[:,1]+D[:,1]))))
            norm=np.zeros_like(K[2]);norm[0]=1. if abs(top-jf)<=2 else 0.;norm[1]=1.
            max_I=max(max_I,float(np.max(abs(V[:,0]-(norm-.5*K[2]+.375*K[4])))))
    assert max_pure<1e-12 and max_dual<1e-12 and max_I<1e-12
    rows=[]
    for case in c['cases']:
        top,mid,mode=case['top2'],case['mid2'],case['mode']
        if [top,mid]==[11,11]:
            item=replay['new_strict_points'][0]['upper_interior'];q=np.array(item['q_pair']);betas=item['betas_native_deg']
        else:
            row=next(x for x in grid['sameparent_results'] if x['top_spin2']==top and x['middle_spin2']==mid and x['population_mode']==mode)
            point=row['strict_upper_witness'];q=np.array(point['q_pair']);betas=[point['beta331_native_deg'],point['beta701_native_deg']]
        vals=actual_vectors(top,mid,betas,base);A,b=constraints(top,vals,mode,base);observables={};projections={}
        for line,jf,beta in [('331',mid,betas[0]),('701',9,betas[1])]:
            mixed=np.einsum('k,kij->ij',weight(beta),at90(top,jf));I,Q=float(mixed[0]@q),float(mixed[1]@q)
            a2,a4=vals[line][2]@q,vals[line][4]@q
            assert abs(I-(1-.5*a2+.375*a4))<1e-12 and abs(Q/I)<=1+1e-12
            pureE2=(1.5*a2+.625*a4)/I
            observables[line]={'a2':float(a2),'a4':float(a4),'I90':I,'P90_plane_axis_native_EM':Q/I,
                'E2_fraction_of_radiative_amplitude_norm':float(weight(beta)[1]),
                'pureE2_formula_from_same_AD_counterfactual':float(pureE2),
                'not_measured_polarization_or_source_delta':True}
            projections[line]=project_P(mixed[1],mixed[0],A,b)
        rows.append({'top_spin2':top,'middle_spin2':mid,'population_mode':mode,
            'beta331_native_deg':betas[0],'beta701_native_deg':betas[1],
            'witness_observables':observables,'individual_fixed_beta_P_projections':projections,
            'same_parent_population_shared':True,'not_joint_projection_rectangle':True})
    out={'at':datetime.now(ZoneInfo('Asia/Shanghai')).isoformat(),'script_sha256':sha(Path(__file__)),
        'contract_sha256':sha(args.contract),'all_input_hashes_unchanged':True,
        'pure_rank_and_EMdual_controls':{'max_pure_relation_error':max_pure,'max_EMdual_error':max_dual,
            'max_I90_reconstruction_error':max_I,'EMdual_AD_same_P_opposite':True},
        'cases':rows,'scope':{'no_measured_P_Q_or_covariance':True,'fixed_beta_projection_not_full_mixing_profile':True,
            'no_unique_spin_or_parity_identification':True,'photon_emission90_not_Compton90':True,
            'not_relabeling_inferred_P_as_independent_observation':True}}
    args.output.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'controls':out['pure_rank_and_EMdual_controls'],
        'cases':[{'top2':x['top_spin2'],'mid2':x['middle_spin2'],
        'beta331':x['beta331_native_deg'],'beta701':x['beta701_native_deg'],
        'P_at_witness':{k:v['P90_plane_axis_native_EM'] for k,v in x['witness_observables'].items()},
        'fixed_beta_P_projection':{k:[v['P_min'],v['P_max']] for k,v in x['individual_fixed_beta_P_projections'].items()}} for x in rows]},ensure_ascii=False,indent=2))


if __name__=='__main__':main()
