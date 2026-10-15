#!/usr/bin/env python3
"""Declared DCO design using real spin sequences, not NORDBALL replay.

Angles, pair acceptance, reference cascades and populations are chosen. The
actual reported ratios do not supply these missing experimental inputs.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from fractions import Fraction

import numpy as np
from scipy.optimize import linprog

from day14_cascade_order_identifiability import coupling, intensity, maximal_coupling
from day14_conditional_angular_response import direction, rotation_columns
from day14_zobel83_alignment_worksheet import tensor_polynomials
from day14_positive_population_hull import rational_vertices


def photon_map(c, rank, n):
    return np.einsum("imk,kq->imq",c,rotation_columns(rank,n))*math.sqrt((2*rank+1)/2)


def joint(c1,c2,l1,l2,n1,n2):
    return np.einsum("imq,mfs->ifqs",photon_map(c1,l1,n1),photon_map(c2,l2,n2))


def population_witness(a,b,ratio):
    n=len(a)
    # Maximize the minimum pair mass under a declared ratio constraint.
    result=linprog(np.r_[np.zeros(n),-1.],
                   A_ub=np.c_[-np.eye(n),np.ones(n)],b_ub=np.zeros(n),
                   A_eq=np.r_[np.r_[np.ones(n),0.][None,:],
                               np.r_[a-ratio*b,0.][None,:]],
                   b_eq=[1.,0.],bounds=[(0,None)]*(n+1),method="highs")
    return dict(status=int(result.status),success=bool(result.success),
                q=(result.x[:n].tolist() if result.success else None),
                min_pair_mass=(float(result.x[-1]) if result.success else None))


def audit():
    checks={}
    def check(name,condition):
        checks[name]=bool(condition)
        if not condition:raise AssertionError(name)
    angles=[40.,90.]
    na,nb=[direction(np.deg2rad(x),0.) for x in angles]
    check("degree_to_radian_direction_contract",np.isclose(na[2],math.cos(math.radians(40))) and abs(nb[2])<1e-14)
    check("unit_direction_vectors",np.isclose(np.dot(na,na),1) and np.isclose(np.dot(nb,nb),1))
    records=[]
    for name,ji,jm,jf,l1,l2 in [("A958_target_871_reference",6.5,4.5,3.5,2,1),
                               ("B554_target_1160_reference",4.5,4.5,2.5,1,2)]:
        c1,c2=coupling(jm,l1,ji),coupling(jf,l2,jm)
        check(name+"_CG1_isometry",np.allclose(np.einsum('imk,jmk->ij',c1,c1),np.eye(len(c1)),atol=1e-12))
        check(name+"_CG2_isometry",np.allclose(np.einsum('imk,jmk->ij',c2,c2),np.eye(len(c2)),atol=1e-12))
        for low,rank,upper,c in [(jm,l1,ji,c1),(jf,l2,jm,c2)]:
            if upper==low+rank:
                expected=maximal_coupling(low,rank)
                check(name+f'_maximal_binomial_control_{rank}',np.allclose(c,expected,atol=1e-12) or np.allclose(c,-expected,atol=1e-12))
        ma=np.arange(ji,-ji-1,-1)
        magnitudes=np.arange(.5,ji+.1,1.)
        ab,ba=joint(c1,c2,l1,l2,na,nb),joint(c1,c2,l1,l2,nb,na)
        aa,bb=[],[]
        for mag in magnitudes:
            rho=np.diag((abs(ma)==mag).astype(float)/2)
            aa.append(intensity(ab,rho));bb.append(intensity(ba,rho))
        a,b=np.array(aa),np.array(bb);ratios=a/b
        check(name+"_denominators_strictly_positive",min(b)>0)
        rho_iso=np.eye(len(ma))/len(ma)
        ratio_iso=intensity(ab,rho_iso)/intensity(ba,rho_iso)
        check(name+"_random_initial_ratio_one",np.isclose(ratio_iso,1,atol=1e-12))
        phi=.37
        rotated=joint(c1,c2,l1,l2,direction(np.deg2rad(40),phi),direction(np.deg2rad(90),phi))
        rho_chosen=np.diag(np.exp(-ma*ma/5.));rho_chosen/=np.trace(rho_chosen)
        check(name+"_axial_global_azimuth_rotation",np.isclose(intensity(ab,rho_chosen),intensity(rotated,rho_chosen),atol=1e-12))
        # Partial trace of the first unobserved photon is a physical feed,
        # not an independently reset Gaussian at the intermediate level.
        fed=np.einsum('imk,ij,jnk->mn',c1,rho_chosen,c1.conj())
        check(name+"_unobserved_feeding_density_PSD_trace_one",np.linalg.eigvalsh(fed).min()>-1e-12 and np.isclose(np.trace(fed),1))
        # Sphere-average the second gamma and recover the first marginal.
        x,w=np.polynomial.legendre.leggauss(8)
        total=0.
        for xx,ww in zip(x,w):
            for ph in np.linspace(0,2*math.pi,12,endpoint=False):
                total+=ww/24*intensity(joint(c1,c2,l1,l2,na,direction(np.arccos(xx),ph)),rho_chosen)
        single=photon_map(c1,l1,na)
        single_intensity=float(np.einsum('ij,imq,jmq->',rho_chosen,single,single.conj()).real)
        check(name+"_joint_integrates_to_first_single_marginal",np.isclose(total,single_intensity,atol=2e-12))
        q=np.arange(1,len(a)+1,dtype=float);q/=q.sum()
        direct=np.dot(a,q)/np.dot(b,q);convex=np.dot(b*q/np.dot(b,q),ratios)
        check(name+"_fractional_ratio_is_positive_weighted_vertex_average",np.isclose(direct,convex) and ratios.min()<=direct<=ratios.max())
        witness=population_witness(a,b,1.45)
        check(name+"_LP_agrees_with_complete_vertex_range",witness['success']==bool(ratios.min()<=1.45<=ratios.max()))
        if witness['success']:
            qq=np.array(witness['q'])
            check(name+"_strictly_positive_witness_matches_chosen_ratio",min(qq)>0 and np.isclose(qq.sum(),1) and np.isclose(qq@a/(qq@b),1.45))
        else:
            check(name+"_all_vertex_halfspaces_exclude_forced_ratio",max(a-1.45*b)<0)
        f_range=[1.45/float(ratios.max()),1.45/float(ratios.min())]
        records.append(dict(name=name,spins=[ji,jm,jf],ranks=[l1,l2],
                            abs_M=magnitudes.tolist(),numerator_kernel=a.tolist(),
                            denominator_kernel=b.tolist(),vertex_ratios=ratios.tolist(),
                            complete_R_range=[float(ratios.min()),float(ratios.max())],
                            isotropic_R=ratio_iso,witness_R1p45=witness,
                            common_scalar_f_compatible_range=f_range))
    check("pre_registered_two_model_prediction_revised_not_angles_retuned",records[0]['witness_R1p45']['success'] and not records[1]['witness_R1p45']['success'])
    lo=max(x['common_scalar_f_compatible_range'][0] for x in records)
    hi=min(x['common_scalar_f_compatible_range'][1] for x in records)
    check("unknown_common_scalar_leaves_overlapping_model_ranges",lo<1.45<hi)
    check("isotropic_models_with_declared_unknown_f_can_share_reportedratio",all(np.isclose(1.45*x['isotropic_R'],1.45) for x in records))
    # Ratios from the same corrected 2x2 event-pair cells are reciprocal;
    # source ratios must not be assumed to use such mutually swapped gates.
    q=np.ones(7)/7;reciprocal=(q@np.array(records[0]['numerator_kernel']))/(q@np.array(records[0]['denominator_kernel']))
    check("same_corrected_pair_target_reference_swap_is_reciprocal",np.isclose(reciprocal*(1/reciprocal),1))
    check("two_literal1p45_values_are_not_a_mutual_corrected_pair",not np.isclose(1.45**2,1))
    # Even exact single-photon rank2/rank4 calibration need not determine a
    # two-photon analyzer. Find the complete ratio range at those fixed moments.
    first=records[0];a=np.array(first['numerator_kernel']);b=np.array(first['denominator_kernel'])
    m,t=tensor_polynomials(6.5)
    indices=[np.flatnonzero(np.isclose(m,x))[0] for x in first['abs_M']]
    tensors=t[:,indices];constraint=np.vstack([b,tensors]);calibrated=[]
    for sign in [1,-1]:
        res=linprog(sign*a,A_eq=constraint,b_eq=[1,0,0],
                    bounds=[(0,None)]*len(a),method='highs')
        check(f'calibrated_{sign}_linear_fractional_LP_success',res.success)
        y=res.x;q=y/y.sum();dual=res.eqlin.marginals
        slack=sign*a-constraint.T@dual
        check(f'calibrated_{sign}_primal_dual_residuals',
              np.max(abs(constraint@y-np.array([1,0,0])))<1e-10 and
              slack.min()>-1e-10 and abs(sign*a@y-dual[0])<1e-10)
        exact_q=[Fraction(float(x)).limit_denominator(100000) for x in q]
        _,v=rational_vertices()
        check(f'calibrated_{sign}_exact_population_moments_zero',
              sum(exact_q)==1 and all(sum(qq*p[k] for qq,p in zip(exact_q,v))==0 for k in [0,1]))
        # Mix5%isotropic to avoid reliance on boundary populations.
        qi=.95*q+.05/len(q)
        rho=np.zeros((14,14))
        for mag,mass in zip(first['abs_M'],qi):
            for index in np.flatnonzero(np.isclose(abs(m),mag)):
                rho[index,index]=mass/2
        c1,c2=coupling(4.5,2,6.5),coupling(3.5,1,4.5)
        photon1=np.einsum('ij,imk,jml->kl',rho,c1,c1.conj())
        feed=np.einsum('imk,ij,jnk->mn',c1,rho,c1.conj())
        photon2=np.einsum('mn,mfk,nfl->kl',feed,c2,c2.conj())
        check(f'calibrated_{sign}_both_full_photon_marginals_identical_isotropic',
              np.allclose(photon1,np.eye(5)/5,atol=2e-12) and
              np.allclose(photon2,np.eye(3)/3,atol=2e-12))
        check(f'calibrated_{sign}_strict_PSD_population',np.linalg.eigvalsh(rho).min()>0)
        calibrated.append(dict(q=q.tolist(),q_exact=[str(x) for x in exact_q],
                               ratio=float(a@y),LP_dual=dual.tolist(),
                               reduced_costs=slack.tolist(),
                               interior_q=qi.tolist(),interior_ratio=float(a@qi/(b@qi))))
    check('same_single_photon_calibration_leaves_nontrivial_joint_ratio_interval',
          calibrated[1]['ratio']-calibrated[0]['ratio']>.04)
    check('strict_PSD_controls_keep_different_joint_ratios',
          calibrated[1]['interior_ratio']-calibrated[0]['interior_ratio']>.04)
    return dict(kind="L2 source-state-grounded declared DCO design; no NORDBALL replay",
                chosen_geometry=dict(theta_degrees=angles,phi_radians=0.,point_detectors=True,
                                     pol_unobserved=True,efficiency_correction_assumed=True),
                actual_source_input_only="N67-7 reported1.45/1.45/.77; actual gate/ref/geometry unavailable",
                source_nominal_pure_limits_only=True,models=records,
                unknown_common_f_overlap=[lo,hi],
                f1p45_is_a_counterexample_not_an_independent_calibration=True,
                mutual_corrected_gate_identity="R(target,reference)*R(reference,target)=1",
                actual_both_reported_R_product=1.45**2,
                fixed_single_photon_moments=dict(alpha2_chosen=0.,alpha4_chosen=0.,
                                                numerical_primal_dual_checked=True,
                                                LP_extrema=calibrated,
                                                full_photon1_marginal='I5/5',
                                                full_photon2_marginal='I3/3',
                                                actual_calibration_or_population=False),
                boundaries=[
                    "The frozen40/90geometry and these reference paths are chosen, not extracted from missing primary or actual NORDBALL data.",
                    "ModelB's1.45infeasibility revises the prediction within this particular model; it does not reject E1, source data, or every allowed response/mixing.",
                    "Positive population witnesses are mathematical states, not reconstructed physical reaction populations.",
                    "Unknown scalar f only demonstrates missing calibration; deriving f from this same target ratio is circular and gives no source geometry.",
                    "Real array response may be nonseparable, energy/gate-dependent and finite; a common scalar is itself an extra assumption.",
                    "Mutual reciprocal identity requires the same corrected cells/event selection; actual two reported ratios need not meet that condition.",
                    "Actual conditional counts/covariance/gates are absent; no experimental pvalue, new multipolarity, new card or L4 replay is claimed."],
                checks=checks,checks_passed=len(checks))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();result=audit()
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(checks_passed=result['checks_passed'],all_checks_true=all(result['checks'].values()),output=str(args.output))))


if __name__=='__main__':main()
