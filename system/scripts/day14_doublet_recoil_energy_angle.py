#!/usr/bin/env python3
"""Declared two-photon recoil design; not an order fit to 193Bi data.

Masses below are energy equivalents (c=1), in keV. Only the nominal doublet
centroids come from HE15-9; A*u, detector widths, angular selection, and the
isolated freely recoiling intermediate state are declared controls.
"""
from __future__ import annotations

import argparse
import json
import math
from decimal import Decimal, localcontext
from fractions import Fraction
from pathlib import Path

import numpy as np
from scipy.special import roots_hermitenorm


def recoil_shifts(M,h,l,c):
    # Common final mass squared: M^2-2M(h+l)+2hl, at anchor opening cosine 0.
    # H+: high first; H-: low first. These subtracted forms avoid loss of
    # significance in M^2-middle^2-final^2 and in E_second-E_anchor.
    low_second_delta=-h*l*c/(M-h*(1-c))
    high_second_delta=-h*l*c/(M-l*(1-c))
    return low_second_delta,high_second_delta


def sum_difference_stable(M,h,l,c):
    return -h*l*c*(h-l)*(1-c)/((M-h*(1-c))*(M-l*(1-c)))


def log_mixture(x,a):
    return (-.5*np.asarray(x)**2-.5*math.log(2*math.pi)-.5*a*a
            +np.logaddexp(a*np.asarray(x),-a*np.asarray(x))-math.log(2))


def mixture_half_jeffreys(a,b,n=96):
    z,w=roots_hermitenorm(n)
    w=w/math.sqrt(2*math.pi)
    value=0.
    for mean in (a,b):
        for label in (-1,1):
            x=label*mean+z
            lr=log_mixture(x,a)-log_mixture(x,b)
            value+=.25*float(w@(np.tanh(.5*lr)*lr))
    return value


def separation_information(a,n=160):
    z,w=roots_hermitenorm(n)
    x=a+z
    score=-a+x*np.tanh(a*x)
    return float(w@(score*score)/math.sqrt(2*math.pi))


def two_dimensional_J(a,b,u,v,n=64):
    # Conditional density factorizes into energy sum Gaussian and an unordered
    # contrast mixture. Independent two-dimensional expectation checks the
    # additive divergence formula, without resolving a 1e-24 sum term alone.
    z,w=roots_hermitenorm(n)
    w=w/math.sqrt(2*math.pi)
    ww=w[:,None]*w[None,:]
    ans=0.
    for sep,mu in ((a,u),(b,v)):
        for label in (-1,1):
            x=label*sep+z[:,None]
            s=mu+z[None,:]
            lr=log_mixture(x,a)-log_mixture(x,b)+.5*((s-v)**2-(s-u)**2)
            ans+=.25*float(np.sum(ww*np.tanh(lr*.5)*lr))
    return ans


def stopped_second_shifts_decimal(M,h,l):
    # Complete stopping removes the O(1/M) opening-angle term. With the SAME
    # free-cascade c0=0 anchors and common final mass, constant O(1/M^2) shifts
    # remain: E*_2/E_anchor=(M-E1)/sqrt(M^2-2ME1). Do not call them exact zero.
    with localcontext() as ctx:
        ctx.prec=70
        M,h,l=map(lambda x:Decimal(str(x)),(M,h,l))
        return (l*((M-h)/(M*M-2*M*h).sqrt()-1),
                h*((M-l)/(M*M-2*M*l).sqrt()-1))


def audit():
    checks={}
    def check(name,condition):
        checks[name]=bool(condition)
        if not condition:
            raise AssertionError(name)

    h,l=394.,393.4
    unit_mass=931494.10242
    M=193*unit_mass
    sigma=.8
    root2sigma=math.sqrt(2)*sigma
    a0=(h-l)/root2sigma
    K=h*l/M
    F=separation_information(a0)
    check('mass_and_gap_units_keV_c_equal_one',M>1e8 and K<.001)
    check('separation_information_known_overlap_not_zero',0<F<1)
    check('unresolved_equal_energy_separation_information_zero',separation_information(0)==0)
    check('well_separated_mixture_information_tends_one',abs(separation_information(9)-1)<1e-12)
    # An exact rational invariant calculation, independent of floating-point
    # shift formulas, verifies both orders end at the SAME final mass.
    MF=Fraction(193)*Fraction('931494.10242')
    hf,lf=Fraction(394),Fraction('393.4')
    final2=MF*MF-2*MF*(hf+lf)+2*hf*lf
    exact=[]
    for c in (Fraction(-1),Fraction(-7,10),Fraction(0),Fraction(7,10),Fraction(1)):
        for first,second in ((hf,lf),(lf,hf)):
            middle2=MF*MF-2*MF*first
            second_lab=(middle2-final2)/(2*(MF-first*(1-c)))
            # p_final^2=(M-E1-E2)^2-|E1 n1+E2 n2|^2
            final_check=(MF-first-second_lab)**2-(first*first+second_lab**2+2*first*second_lab*c)
            key=f'{c}_{first}'
            check('exact_four_momentum_common_final_'+key,final_check==final2)
            check('positive_final_and_middle_masses_'+key,0<final2<middle2<MF*MF)
            shift=second_lab-second
            expected=recoil_shifts(float(MF),h,l,float(c))[0 if first==hf else 1]
            check('independent_rational_energy_shift_'+key,abs(float(shift)-expected)<2e-16)
            exact.append(dict(c=str(c),first=str(first),second_lab=float(second_lab),
                              final_invariant_residual_exact=str(final_check-final2)))
    # Physical boost cross-check: lab -> intermediate rest -> lab.
    c=.7
    for first,second in ((h,l),(l,h)):
        sh=recoil_shifts(M,h,l,c)[0 if first==h else 1]
        e2=second+sh
        mid=math.sqrt(M*(M-2*first))
        velocity=-first/(M-first)
        gamma=(M-first)/mid
        lab=np.array([e2,e2*math.sqrt(1-c*c),0.,e2*c])
        rest=np.array([gamma*(lab[0]-velocity*lab[3]),lab[1],0.,
                       gamma*(lab[3]-velocity*lab[0])])
        back=np.array([gamma*(rest[0]+velocity*rest[3]),rest[1],0.,
                       gamma*(rest[3]+velocity*rest[0])])
        check('Lorentz_roundtrip_second_photon_'+str(first),np.max(abs(back-lab))<2e-13)
        rest_expected=second*(M-first)/mid
        check('rest_energy_independent_of_lab_opening_angle_'+str(first),
              abs(rest[0]-rest_expected)<2e-13)
    table=[]
    for c in (-1/math.sqrt(2),0.,1/math.sqrt(2)):
        dl,dh=recoil_shifts(M,h,l,c)
        ap=(h-l-dl)/root2sigma
        am=(h-l+dh)/root2sigma
        up,um=dl/root2sigma,dh/root2sigma
        jc=mixture_half_jeffreys(ap,am,n=96)
        jc_fine=mixture_half_jeffreys(ap,am,n=160)
        sd=sum_difference_stable(M,h,l,c)
        js=.5*(sd/root2sigma)**2
        j2=two_dimensional_J(ap,am,up,um)
        leading=F*K*K*c*c/sigma**2
        check('contrast_quadrature_converges_'+str(c),abs(jc-jc_fine)<1e-12)
        check('full_joint_factorization_J_'+str(c),abs(j2-(jc_fine+js))<1e-12)
        check('sum_difference_subtracted_form_'+str(c),abs((dl-dh)-sd)<2e-19)
        check('conditional_measured_sum_same_at_order1overM_'+str(c),abs(sd)<4e-12)
        check('contrast_moment_identity_'+str(c),
              abs((1+ap*ap)-(1+am*am)-((ap-am)*(ap+am)))<1e-15)
        if c:
            check('leading_recoil_information_scale_'+str(c),abs(jc_fine/leading-1)<1e-4)
        else:
            check('reference_angle_both_hypotheses_identical',jc_fine==0 and js==0)
        table.append(dict(c=c,low_second_delta_keV=dl,high_second_delta_keV=dh,
                          contrast_sep_high_first=ap,contrast_sep_low_first=am,
                          contrast_second_moment_difference=(ap-am)*(ap+am),
                          sum_mean_order_difference_keV=sd,
                          J_contrast=jc_fine,J_sum=js,J_joint=jc_fine+js,
                          J_leading=leading))
    # At zero physical energy gap, swapping which detector sees the two
    # otherwise identical photons changes only the sign of the separation;
    # its UNORDERED mixture is exactly even, including finite recoil.
    de0=recoil_shifts(M,h,h,.7)[0]/root2sigma
    xs=np.linspace(-8,8,100)
    check('zero_gap_unordered_full_energy_density_equal',
          np.max(abs(log_mixture(xs,de0)-log_mixture(xs,-de0)))==0)
    check('mixture_even_label_symmetry',np.max(abs(log_mixture(xs,a0)-log_mixture(xs,-a0)))==0)
    # Infinite mass scaling is tested by increasing M with all OTHER controls
    # held fixed, not by refitting h,l or the instrument.
    dl,dh=recoil_shifts(M,h,l,.7)
    dl2,dh2=recoil_shifts(2*M,h,l,.7)
    j1=mixture_half_jeffreys((h-l-dl)/root2sigma,(h-l+dh)/root2sigma)
    j2=mixture_half_jeffreys((h-l-dl2)/root2sigma,(h-l+dh2)/root2sigma)
    check('infinite_mass_shift_halves',abs(dl2/dl-.5)<1e-6)
    check('information_scales_inverse_mass_squared',abs(j1/j2-4)<1e-4)
    # Complete stopping is a DIFFERENT environmental response, not a Lorentz
    # transformation applied to the free-cascade final four-momentum.
    stl,sth=stopped_second_shifts_decimal(M,h,l)
    check('stopping_constant_shift_not_exact_zero',stl>0 and sth>0)
    check('stopping_residual_far_below_leading_free_recoil',float(max(stl,sth))<1e-5*K)
    stl2,sth2=stopped_second_shifts_decimal(2*M,h,l)
    check('stopping_constant_residual_inverse_mass_squared',abs(float(stl/stl2)-4)<1e-4)
    # A declared residual pair-response with energy-contrast slope b*c is
    # locally collinear with the order-dependent recoil slope. Independent
    # calibration is needed to use that row as evidence.
    angles=np.array([-1/math.sqrt(2),1/math.sqrt(2)])
    design=np.c_[angles,angles]
    check('local_nuclear_and_pair_response_slope_rank_one',np.linalg.matrix_rank(design)==1)
    augmented=np.r_[design,[[0.,1.]]]
    check('independent_response_calibration_adds_direction',np.linalg.matrix_rank(augmented)==2)
    # Component-wise unknown pair-response means could make exact conditional
    # spectra match. The construction's dependence on both detectors' opening
    # angle is explicit; this is NOT a single-detector gain error assertion.
    c=.7
    dl,dh=recoil_shifts(M,h,l,c)
    plus=np.array([h,l+dl])
    minus_corrected=np.array([h+dh-dh,l+dl])
    check('unknown_component_pair_response_can_align_conditional_means',
          np.array_equal(plus,minus_corrected))
    return dict(model='exact isolated-cascade kinematics plus CHOSEN conditional Gaussian energy response',
                source=dict(path='knowledge/sources/herzan-2015-193bi-spectroscopy.md',locator='HE15-9',
                            actual_initial_mass=None,actual_intermediate_stopping=None,
                            actual_detector_energy_angle_response=None),
                chosen=dict(mass_number=193,u_keV=unit_mass,initial_M_keV=M,
                            reference_c=0,high_keV=h,low_keV=l,sigma_E_single_keV=sigma,
                            conditional_detector_label_weights='equal; no source assertion'),
                recoil_scale_K_keV=K,overlap_separation_information=F,
                final_mass_squared_exact_rational=str(final2),exact_controls=exact,table=table,
                stopped_constant_second_shifts_keV=[str(stl),str(sth)],
                information_definition='half Jeffreys in nats; conditional on chosen angle; not power/count requirement/p-value',
                boundaries=['not a covariant full angular-amplitude probability model',
                            'static angular-swap theorem alone does not include this energy kernel',
                            'complete stopping removes leading angle term, not every constant recoil correction',
                            'angle-dependent response must be independently constrained',
                            'no actual 193Bi order, mass, lifetime, stopping or measurement significance'],
                checks=checks,checks_passed=len(checks))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path,required=True)
    args=p.parse_args()
    out=audit()
    args.output.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(checks_passed=out['checks_passed'],
                          all_checks_true=all(out['checks'].values()),output=str(args.output))))


if __name__=='__main__':
    main()
