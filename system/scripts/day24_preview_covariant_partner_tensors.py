#!/usr/bin/env python3
"""Abstract good-spin multiplicities/tensors; no physical nuclear realization.

Rotational covariance, Hermiticity, T and C are checked explicitly. Two
different allowed tensors are compared; this is NOT a fixed-operator,
configuration-only comparison or a model fit to an observed nucleus.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np

from day23_prm_basis_rotor import clebsch_gordan,spin_matrices


SPINS=[1,3,5,7]


def spaces():
    sectors={};offset=0
    for two_i in SPINS:
        for alpha in [0,1]:
            sectors[(two_i,alpha)]=slice(offset,offset+two_i+1)
            offset+=two_i+1
    js=[np.zeros((offset,offset),complex) for _ in range(3)]
    h=np.zeros((offset,offset),complex);rotation=np.zeros_like(h)
    levels=[]
    for (two_i,alpha),sl in sectors.items():
        i=two_i/2;axes=spin_matrices(two_i)
        for j,axis in zip(js,axes):j[sl,sl]=axis
        energy=i*(i+1)+alpha*(.4+.03*i)
        h[sl,sl]=energy*np.eye(two_i+1)
        ev,v=np.linalg.eigh(axes[1]);rotation[sl,sl]=(v*np.exp(-1j*math.pi*ev))@v.T.conj()
        levels.append({'two_I_representation':two_i,'multiplicity_alpha':alpha,
                       'dimensionless_energy_design':energy,'magnetic_multiplet_dimension':two_i+1})
    return sectors,js,h,rotation,levels


def rmes(rank,case):
    a={3:1.,5:1.4,7:.9};b=a if case=='a' else {3:1.4,5:.5,7:1.2}
    diag=(1.,1.7) if rank==1 else (.6,1.1)
    cross=(.2,.4) if rank==1 else (.3,.2)
    return {two_i:np.array([[diag[0]*a[two_i],cross[0]*b[two_i]],
                            [cross[1]*b[two_i],diag[1]*a[two_i]]]) for two_i in [3,5,7]}


def tensors(rank,case,sectors):
    dimension=max(s.stop for s in sectors.values())
    tensor={mu:np.zeros((dimension,dimension),complex) for mu in range(-rank,rank+1)}
    values=rmes(rank,case)
    for two_i,r in values.items():
        two_f=two_i-2
        for initial,final,rmatrix in [(two_i,two_f,r),(two_f,two_i,-r.T)]:
            for ai in [0,1]:
                for af in [0,1]:
                    si,sf=sectors[(initial,ai)],sectors[(final,af)]
                    for mi_index,mi in enumerate(np.arange(-initial,initial+1,2)/2):
                        for mf_index,mf in enumerate(np.arange(-final,final+1,2)/2):
                            mu=int(round(mf-mi))
                            if abs(mu)<=rank:
                                tensor[mu][sf.start+mf_index,si.start+mi_index]=(
                                    clebsch_gordan(initial/2,mi,rank,mu,final/2,mf)
                                    *rmatrix[af,ai]/math.sqrt(final+1))
    return tensor,values


def maximum(matrix):
    return float(np.max(abs(matrix)))


def calculate():
    sectors,js,h,rotation,levels=spaces();dimension=len(h);identity=np.eye(dimension)
    t=rotation;c=rotation@rotation
    anti=lambda u,o:u@o.conj()@u.T.conj()
    controls={'ordinary_SU2_commutator':maximum(js[0]@js[1]-js[1]@js[0]-1j*js[2])<1e-12,
              'rotation_unitarity':maximum(rotation.T.conj()@rotation-identity)<1e-12,
              'halfspin_time_reversal_square_minus1':maximum(t@t.conj()+identity)<1e-12,
              'chiral_antiunitary_square_plus1':maximum(c@c.conj()-identity)<1e-12,
              'chiral_representation_is_minusK':maximum(c+identity)<1e-12,
              'H_commutes_with_all_rotations':max(maximum(h@j-j@h) for j in js)<1e-12,
              'H_time_reversal_and_chiral_symmetric':max(maximum(anti(t,h)-h),maximum(anti(c,h)-h))<1e-12,
              'two_multiplicity_sequences_not_forced_degenerate':all(
                  abs(next(r['dimensionless_energy_design'] for r in levels if r['two_I_representation']==i and r['multiplicity_alpha']==0)
                      -next(r['dimensionless_energy_design'] for r in levels if r['two_I_representation']==i and r['multiplicity_alpha']==1))>.1 for i in SPINS)}
    jplus=js[0]+1j*js[1];details={};results=[]
    for case in ['a','b']:
        for rank in [1,2]:
            tensor,values=tensors(rank,case,sectors)
            errors={'Jz_tensor':0.,'Jplus_tensor':0.,'spherical_Hermiticity':0.,'time_parity':0.,'chiral_covariance':0.,'Wigner_Eckart_B':0.,'reverse_detailed_balance':0.}
            for mu,op in tensor.items():
                errors['Jz_tensor']=max(errors['Jz_tensor'],maximum(js[2]@op-op@js[2]-mu*op))
                right=math.sqrt((rank-mu)*(rank+mu+1))*tensor[mu+1] if mu<rank else np.zeros_like(op)
                errors['Jplus_tensor']=max(errors['Jplus_tensor'],maximum(jplus@op-op@jplus-right))
                errors['spherical_Hermiticity']=max(errors['spherical_Hermiticity'],maximum(op.T.conj()-(-1)**mu*tensor[-mu]))
                errors['time_parity']=max(errors['time_parity'],maximum(anti(t,op)-(-1)**(rank-mu)*tensor[-mu]))
                errors['chiral_covariance']=max(errors['chiral_covariance'],maximum(anti(c,op)-op))
            rows=[]
            for two_i,r in values.items():
                two_f=two_i-2;strength=np.zeros((2,2))
                for ai in [0,1]:
                    for af in [0,1]:
                        si,sf=sectors[(two_i,ai)],sectors[(two_f,af)]
                        down=sum(float(np.linalg.norm(op[sf,si])**2) for op in tensor.values())/(two_i+1)
                        up=sum(float(np.linalg.norm(op[si,sf])**2) for op in tensor.values())/(two_f+1)
                        strength[af,ai]=down
                        errors['Wigner_Eckart_B']=max(errors['Wigner_Eckart_B'],abs(down-r[af,ai]**2/(two_i+1)))
                        errors['reverse_detailed_balance']=max(errors['reverse_detailed_balance'],abs((two_i+1)*down-(two_f+1)*up))
                rows.append({'two_I_initial_representation':two_i,'two_I_final_representation':two_f,
                             'dimensionless_RME_design':r.tolist(),
                             'B_over_unknown_scale_squared_rows_final_columns_initial':strength.tolist()})
            tag=f'case_{case}_rank_{rank}'
            for name,error in errors.items():controls[tag+'_'+name]=error<2e-12
            controls[tag+'_partner_insequence_strengths_can_differ']=all(
                abs(r['B_over_unknown_scale_squared_rows_final_columns_initial'][0][0]-r['B_over_unknown_scale_squared_rows_final_columns_initial'][1][1])>.001 for r in rows)
            details[tag]=errors
            seq=[r['B_over_unknown_scale_squared_rows_final_columns_initial'][0][0] for r in rows]
            cross=[r['B_over_unknown_scale_squared_rows_final_columns_initial'][1][0] for r in rows]
            curvature=lambda y:y[2]-2*y[1]+y[0]
            results.append({'case':case,'tensor_rank':rank,'rows':rows,
                            'chosen_three_step_insequence_second_difference':curvature(seq),
                            'chosen_three_step_crosssequence_second_difference':curvature(cross)})
    ca=next(r for r in results if r['case']=='a' and r['tensor_rank']==1)
    cb=next(r for r in results if r['case']=='b' and r['tensor_rank']==1)
    controls['same_listed_symmetries_allow_different_three_step_shape_signs']=(
        ca['chosen_three_step_insequence_second_difference']*ca['chosen_three_step_crosssequence_second_difference']>0
        and cb['chosen_three_step_insequence_second_difference']*cb['chosen_three_step_crosssequence_second_difference']<0)
    controls['rank1_crossI_tensor_nonzero_totalJ_crossI_zero']=sum(
        np.linalg.norm(tensors(1,'a',sectors)[0][mu][sectors[(1,0)],sectors[(3,0)]]) for mu in [-1,0,1])>.1 and all(
        np.linalg.norm(j[sectors[(1,0)],sectors[(3,0)]])==0 for j in js)
    bounds=[]
    for epsilon in [0.,.05,.2,.8,1.]:
        a,b=1.,epsilon;plus=(a+b)**2;minus=(a-b)**2
        contrast=abs((plus-minus)/(plus+minus));bound=2*epsilon/(1+epsilon**2)
        controls[f'epsilon_{epsilon}_special_real_kernel_bound']=abs(contrast-bound)<1e-13
        bounds.append({'dimensionless_EM_kernel_epsilon_design':epsilon,'contrast':contrast,'bound':bound,
                       'scope':'Special real L/R transition kernel aI+b*sigma_x, a!=0; epsilon is not measured, not derived from a spectral gap or actual nuclear localization.'})
    return {'status':'uncredited-abstract-rotation-tensor-preview','formal_day_index':23,'preview_day_index':24,
            'scope':'40D direct-sum good-spin representations with two multiplicities. No intrinsic handed geometry, nucleus, local one-body EM realization or actual spectral fit.',
            'levels_dimensionless_design_only':levels,'tensor_results':results,'special_EM_kernel_bounds':bounds,
            'control_errors':details,'controls':{k:bool(v) for k,v in controls.items()},'all_controls_pass':all(controls.values()),
            'implementation_sha256':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),Path(__file__).with_name('day23_prm_basis_rotor.py')]},
            'limitations':['Rank1/2 tensors have M1/E2 transformation/time-parity properties only; arbitrary RMEs are not certified realizable by the actual fixed nuclear one-body magnetic/charge operators.',
                           'Casesa/b change the abstract tensor RMEs under the same symmetry constraints. They are not a fixed-operator configuration-only comparison and have no assigned nuclear credibility.',
                           'The construction is rotationally invariant and T-invariant, unlike the earlier nonrotational spin-matrix example, but it establishes no intrinsic left/right configuration or actual chiral band.',
                           'Magnetic/Kramers degeneracy remains inside each good-I multiplet; it does not force distinct multiplicity energies to coincide.',
                           'Three-step second differences are only chosen mathematical shape examples, not a universal nuclear staggering theorem or measured anomaly.',
                           'Approximate partner equality in the special kernel needs an EM cross-kernel bound; a small energy splitting alone does not supply epsilon. No actual physical g, B, delta, Q, tau, CI or beamtime inferred.',
                           'Specific135Nd electromagnetic/TAC+RPA support is not erased; additional configuration, dynamics, operator and localization evidence still governs physical hypotheses. NoDay24credit/Day25.']}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
    r=calculate();a.output.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'all_controls_pass':r['all_controls_pass'],'checks':len(r['controls']),
                      'maximum_tensor_error':max(max(v.values()) for v in r['control_errors'].values()),
                      'chosen_shape_second_differences':[{'case':v['case'],'rank':v['tensor_rank'],
                          'in':v['chosen_three_step_insequence_second_difference'],'cross':v['chosen_three_step_crosssequence_second_difference']} for v in r['tensor_results']]},ensure_ascii=False))
    return 0 if r['all_controls_pass'] else 1


if __name__=='__main__':
    raise SystemExit(main())
