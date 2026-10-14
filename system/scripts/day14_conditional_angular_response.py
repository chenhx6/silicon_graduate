#!/usr/bin/env python3
"""Conditional gamma-gamma response in chosen 0 -> L -> 0 cascades.

This is a theory exercise, not a reconstruction of 145Tb or 193Bi data.
Both photons are pure electric multipoles; definite intermediate parity is
(-1)^L relative to the spin-zero endpoints. No time deorientation is included.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
from numpy.polynomial import legendre
from scipy.linalg import expm


def direction(theta, phi=0.0):
    return np.array([np.sin(theta)*np.cos(phi),
                     np.sin(theta)*np.sin(phi), np.cos(theta)])


def rotation_columns(rank, n):
    """Complex-conjugate photon D columns with helicities +1/-1."""
    theta=np.arccos(np.clip(n[2],-1,1));phi=np.arctan2(n[1],n[0])
    m=np.arange(rank,-rank-1,-1)
    raising=np.zeros((2*rank+1,2*rank+1))
    for col,mi in enumerate(m):
        if mi<rank:raising[col-1,col]=np.sqrt(rank*(rank+1)-mi*(mi+1))
    small_d=expm(theta/2*(raising.T-raising))
    d=np.exp(-1j*m[:,None]*phi)*small_d
    return d[:,[rank-1,rank+1]].conj()


def first_amplitude(rank,n):
    m=np.arange(rank,-rank-1,-1)
    # <L M; L -M | 0 0>, followed by photon direction projection.
    phase=(-1.0)**(rank-m)/np.sqrt(2*rank+1)
    return phase[:,None]*rotation_columns(rank,n)[::-1]


def joint_helicity(rank,first,second):
    return first_amplitude(rank,first).T@rotation_columns(rank,second)


def joint_kernel_amplitudes(rank,first,second):
    return (2*rank+1)**2/4*np.sum(np.abs(joint_helicity(rank,first,second))**2)


def coefficients(rank):
    return np.array([1,0,.5]) if rank==1 else np.array([1,0,5/14,0,8/7])


def kernel(rank,x):
    return legendre.legval(x,coefficients(rank))


def pair_counts(rank,ns,assignment,target_eff,gate_eff,exclude_same=True):
    k=kernel(rank,np.clip(ns@ns.T,-1,1))
    if exclude_same:np.fill_diagonal(k,0)
    reference=k@gate_eff
    counts=np.array([np.dot(target_eff[assignment==g],reference[assignment==g])
                     for g in range(3)])
    return counts,reference,k


def cone_factor(k,alpha):
    if alpha==0:return 1.0
    c=np.cos(alpha)
    p=legendre.Legendre.basis(k).integ()
    return float((p(1)-p(c))/(1-c))


def cone_grid(center,alpha,order=10,azimuths=32):
    z,w=legendre.leggauss(order);c=np.cos(alpha)
    mu=c+(z+1)*(1-c)/2
    axis=np.array([0.,0.,1.]) if abs(center[2])<.9 else np.array([1.,0.,0.])
    u=np.cross(axis,center);u/=np.linalg.norm(u);v=np.cross(center,u)
    phis=2*np.pi*np.arange(azimuths)/azimuths
    ns=np.array([m*center+np.sqrt(1-m*m)*(np.cos(p)*u+np.sin(p)*v)
                 for m in mu for p in phis])
    weights=np.repeat(w/(2*azimuths),azimuths)
    return ns,weights


def audit():
    checks={}
    def check(name,condition):
        checks[name]=bool(condition)
        if not condition:raise AssertionError(name)
    grid=np.linspace(-1,1,401)
    z,w=legendre.leggauss(24)
    chosen_directions=[direction(.37,.63),direction(1.28,-.91),direction(2.2,2.4)]
    for rank in [1,2]:
        check(f'L{rank}_positive_joint_kernel',np.min(kernel(rank,grid))>0)
        check(f'L{rank}_normalized_single_marginal',np.isclose(np.dot(w,kernel(rank,z))/2,1))
        differences=[]
        for a in chosen_directions:
            for b in chosen_directions:
                differences.append(abs(joint_kernel_amplitudes(rank,a,b)-kernel(rank,np.dot(a,b))))
        check(f'L{rank}_independent_CG_D_and_Legendre_routes',max(differences)<1e-13)
        check(f'L{rank}_joint_is_not_product_of_isotropic_marginals',not np.isclose(kernel(rank,1),1))
        check(f'L{rank}_exchange_symmetry',np.isclose(joint_kernel_amplitudes(rank,*chosen_directions[:2]),joint_kernel_amplitudes(rank,*chosen_directions[:2][::-1])))
        a=first_amplitude(rank,chosen_directions[0]);rho=a@a.conj().T;rho/=np.trace(rho)
        b=rotation_columns(rank,chosen_directions[1]);effect=b.conj()@b.T
        check(f'L{rank}_conditional_density_PSD_trace_one',np.linalg.eigvalsh(rho).min()>-1e-14 and np.isclose(np.trace(rho),1))
        check(f'L{rank}_density_effect_equals_joint_kernel',np.isclose((2*rank+1)/2*np.trace(effect@rho).real,kernel(rank,np.dot(chosen_directions[0],chosen_directions[1]))))
        # Full-angle first-photon integration yields I/(2L+1).
        rho_full=np.zeros_like(rho)
        for cos_theta,weight in zip(z,w):
            for phi in 2*np.pi*np.arange(12)/12:
                aa=first_amplitude(rank,direction(np.arccos(cos_theta),phi))
                rho_full+=weight/24*(aa@aa.conj().T)*(2*rank+1)/2
        check(f'L{rank}_full_angle_gate_erases_conditional_alignment',np.allclose(rho_full,np.eye(2*rank+1)/(2*rank+1),atol=1e-13))

    angles=np.deg2rad([32,58,90]);assign=np.repeat(np.arange(3),4)
    ns=np.array([direction(theta,phi) for theta in angles for phi in np.arange(4)*np.pi/2])
    et=np.array([.04,.06,.05]);eg=np.array([.04,.04,.04]);te=et[assign]/4;ge=eg[assign]/4
    grouped_f=(ge.sum()-eg[0]/4)/(ge.sum()-eg[2]/4)
    array_results=[]
    for rank in [1,2]:
        counts,response,k=pair_counts(rank,ns,assign,te,ge)
        ratio=counts[0]/counts[2]/(et[0]/et[2])
        complete,complete_response,_=pair_counts(rank,ns,assign,te,ge,False)
        check(f'L{rank}_self_pair_exclusion_correct',np.allclose(complete_response-response,ge*kernel(rank,1)))
        check(f'L{rank}_positive_pair_counts',np.all(counts>0))
        check(f'L{rank}_target_efficiency_scale_cancels',np.isclose((7*counts[0])/(7*counts[2])/(et[0]/et[2]),ratio))
        array_results.append({'rank':rank,'chosen_R_ADO':float(ratio),'factorized_group_f_ADO':float(grouped_f),'chosen_angle_counts_per_unit_parent_flow':counts.tolist(),'per_target_gate_response':response.tolist()})
    check('L1_balanced_12_direction_gate_cancels_K2',np.isclose(array_results[0]['chosen_R_ADO'],1))
    check('L2_four_azimuths_do_not_erase_K4',abs(array_results[1]['chosen_R_ADO']-1)>.01)
    # A ring gate is disjoint from the target detectors: no self-exclusion here.
    phi_grid=2*np.pi*np.arange(64)/64
    ring=np.array([direction(np.pi/2,phi) for phi in phi_grid])
    ring_results=[]
    for rank in [1,2]:
        projected=[]
        for theta in [angles[0],angles[2]]:
            direct=np.mean(kernel(rank,ring@direction(theta)))
            cc=coefficients(rank)
            formula=sum(cc[k]*legendre.Legendre.basis(k)(np.cos(theta))*legendre.Legendre.basis(k)(0) for k in range(len(cc)))
            check(f'L{rank}_azimuth_ring_addition_theorem_{theta:.3f}',np.isclose(direct,formula))
            projected.append(float(direct))
        ring_results.append({'rank':rank,'intrinsic_single_gamma_ratio':1,'factorized_no_self_exclusion_prediction':1,'conditional_ring_ratio':projected[0]/projected[1],'conditional_W_at_32_90':projected})

    ideal=np.array([math.asin(2/math.sqrt(5))/2,math.pi/2-math.asin(2/math.sqrt(5))/2,np.pi/2])
    # 8 azimuths integrate harmonics through |q|=4; four do not.
    eight=np.array([direction(t,p) for t in ideal for p in 2*np.pi*np.arange(8)/8])
    cancelled=[np.mean(kernel(2,eight@n)) for n in chosen_directions]
    check('ideal_three_angles_eight_azimuths_erase_K2_K4',np.allclose(cancelled,1,atol=1e-13))
    four=np.array([direction(t,p) for t in ideal for p in 2*np.pi*np.arange(4)/4])
    az_response=[float(np.mean(kernel(2,four@direction(angles[0],p)))) for p in [0,np.pi/4]]
    check('ideal_polar_angles_alone_do_not_erase_azimuth_rank4',abs(az_response[0]-az_response[1])>.01)
    check('zero_efficiency_gate_direction_has_no_effect',np.allclose(kernel(2,ns@ns.T)@np.zeros(12),0))

    caps=[]
    a=direction(.6,.2);b=direction(1.1,-.7);alpha,beta=np.deg2rad([20,35])
    na,wa=cone_grid(a,alpha);nb,wb=cone_grid(b,beta)
    for rank in [1,2]:
        direct=float(wa@kernel(rank,np.clip(na@nb.T,-1,1))@wb)
        cc=coefficients(rank)
        formula=float(sum(cc[k]*cone_factor(k,alpha)*cone_factor(k,beta)*legendre.Legendre.basis(k)(np.dot(a,b)) for k in range(len(cc))))
        check(f'L{rank}_finite_cone_numeric_and_Qk_formula_agree',np.isclose(direct,formula,atol=1e-13))
        check(f'L{rank}_finite_acceptance_changes_response',abs(direct-kernel(rank,np.dot(a,b)))>.001)
        caps.append({'rank':rank,'cone_halfangles_deg':[20,35],'point_response':float(kernel(rank,np.dot(a,b))),'averaged_response':direct,'Qk_target_gate':[{'k':k,'target':cone_factor(k,alpha),'gate':cone_factor(k,beta)} for k in range(2,len(cc),2)]})
    return {'kind':'L2 chosen 0 -> L -> 0 theory cascade; no experimental data',
            'source_locators':['RB67-3 / printed326 PDF21 Eq3.73','RB67-11 / printed316 PDF11 Eq3.24','Z02-6 / printed910 PDF2 Eq2'],
            'legendre_coefficients':{'L1':coefficients(1).tolist(),'L2':coefficients(2).tolist()},
            'chosen_12_detector_response':array_results,'disjoint_90degree_ring_gate':ring_results,
            'ideal_polar_angles_four_azimuths_response_at_phi_0_pi4':az_response,
            'finite_cones':caps,'checks':checks,'checks_passed':sum(checks.values()),
            'boundaries':['Both single-gamma marginals are isotropic; their joint kernel need not factorize.','Spin-zero toy endpoints and chosen detector geometry are not 193Bi or145Tb assignments.','A scalar efficiency correction/self-exclusion does not replace conditional nuclear/angular response.','Q_k for finite detector cones is not nuclear alignment attenuation or Q_sens for Compton polarimetry.','A matched nominal energy gate can have target-detector-dependent acceptance after same-detector exclusion.','The balanced cancellation needs the full angular response tensors, including azimuths and efficiency weights.','No mixing ratio, actual counts, time deorientation or covariance was inferred.','Day14 continues; Day15 preview remains uncredited.']}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();root=Path(__file__).resolve().parents[2];args.output.resolve().relative_to(root)
    result=audit();args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ['checks_passed','legendre_coefficients','chosen_12_detector_response','disjoint_90degree_ring_gate','finite_cones']},ensure_ascii=False))


if __name__=='__main__':main()
