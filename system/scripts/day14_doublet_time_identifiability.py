#!/usr/bin/env python3
"""Declared energy/time design for HE15-9; never an experimental order fit.

Only the nominal 0.6-keV separation comes from the source. Energy/time widths,
middle-state lifetime and response families are chosen controls. J below is
HALF of the Jeffreys divergence, in nats, not a detection significance.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
from scipy.integrate import quad
from scipy.special import erfc, erfcx, roots_hermitenorm, roots_laguerre
from scipy.stats import exponnorm
from numpy.polynomial.legendre import leggauss


LOG2PI = math.log(2 * math.pi)


def log_normal(x):
    return -.5 * np.asarray(x)**2 - .5 * LOG2PI


def log_exgauss(y, r):
    """Density of N(0,1)+Exp(mean r), using stable erfc branches."""
    y = np.asarray(y, dtype=float)
    if r < 0:
        raise ValueError("mean delay cannot be negative")
    if r == 0:
        return log_normal(y)
    z = (1 / r - y) / math.sqrt(2)
    out = np.empty_like(y)
    positive = z >= 0
    out[positive] = (-math.log(2 * r) - .5 * y[positive]**2
                     + np.log(erfcx(z[positive])))
    out[~positive] = (-math.log(2 * r) + .5 / r**2 - y[~positive] / r
                      + np.log(erfc(z[~positive])))
    return out


def log_joint(x, y, a, r, sign, offset=0.):
    """Z=+-1; X=Za+Nx, Y=Z(offset+sign*U+Ny), all noises independent."""
    if sign not in (-1, 1):
        raise ValueError("order sign must be +-1")
    return np.logaddexp(log_normal(x-a)+log_exgauss(sign*(y-offset), r),
                        log_normal(x+a)+log_exgauss(sign*(-y-offset), r))-math.log(2)


def half_jeffreys_grid(a, r, offset=0., nx=100, ny=600, tail=35.):
    """Positive integrand with finite-box Gauss-Legendre quadrature."""
    x, wx = leggauss(nx)
    y, wy = leggauss(ny)
    xmax = abs(a)+9
    ymax = 9+tail*r+abs(offset)
    x, wx = x*xmax, wx*xmax
    y, wy = y*ymax, wy*ymax
    lp = log_joint(x[:,None], y[None,:], a, r, 1)
    lq = log_joint(x[:,None], y[None,:], a, r, -1, offset)
    lr = lp-lq
    pm, qm = np.exp(lp), np.exp(lq)
    value = float(wx @ ((pm+qm)*.5*np.tanh(lr*.5)*lr) @ wy)
    return dict(J=value, norm_p=float(wx@pm@wy), norm_q=float(wx@qm@wy),
                nx=nx, ny=ny, tail=tail, xmax=xmax, ymax=ymax)


def half_jeffreys_expectation(a, r, offset=0., n=36):
    """Independent full-domain Gauss-Hermite/Gauss-Laguerre expectation.

    J=E_m[tanh(log(p/q)/2)*log(p/q)], m=(p+q)/2. Sampling quadrature
    nodes under both hypotheses avoids subtracting two tiny KL estimates.
    """
    z, wz = roots_hermitenorm(n)
    u, wu = roots_laguerre(n)
    wz = wz/math.sqrt(2*math.pi)
    weights = wz[:,None,None]*wz[None,:,None]*wu[None,None,:]
    total = 0.
    for sign, off in ((1,0.),(-1,offset)):
        for label in (-1,1):
            x = label*a+z[:,None,None]
            y = label*(off+sign*r*u[None,None,:]+z[None,:,None])
            lr = log_joint(x,y,a,r,1)-log_joint(x,y,a,r,-1,offset)
            total += .25*float(np.sum(weights*np.tanh(.5*lr)*lr))
    return total


def energy_label_information(a):
    # Under either label, tanh^2(aX) has the same expectation.
    return quad(lambda x: math.exp(-.5*(x-a)**2)/math.sqrt(2*math.pi)
                *math.tanh(a*x)**2, -12-abs(a), 12+abs(a), epsabs=1e-13)[0]


def time_marginal(y, r, sign, offset=0.):
    return .5*(np.exp(log_exgauss(sign*(y-offset),r))
               +np.exp(log_exgauss(sign*(-y-offset),r)))


def confusion_characteristic(k_high, k_low, r, sigma_single):
    """Positive electronics-tail counterexample, labelled absolute arrivals.

    H+: high prompt gets independent instrument V~Exp(r); low gets nuclear U.
    H-: high gets nuclear U; low prompt gets V. U,V iid. Both characteristic
    functions factor into identical high/low exGaussian marginals. This is a
    nuisance-response ambiguity, NOT an equality with known fixed response.
    """
    high_response_plus = 1/(1-1j*r*k_high)
    low_nuclear_plus = 1/(1-1j*r*k_low)
    high_nuclear_minus = 1/(1-1j*r*k_high)
    low_response_minus = 1/(1-1j*r*k_low)
    gaussian = np.exp(-.5*sigma_single**2*(k_high**2+k_low**2))
    return (gaussian*high_response_plus*low_nuclear_plus,
            gaussian*high_nuclear_minus*low_response_minus)


def audit():
    checks = {}

    def check(name, condition):
        checks[name] = bool(condition)
        if not condition:
            raise AssertionError(name)

    gap, sigma_energy = .6, .8
    a = gap/(math.sqrt(2)*sigma_energy)
    info = energy_label_information(a)
    check('actual_nominal_gap_only_not_centroid_uncertainty_as_resolution', gap == .6)
    check('dimensionless_energy_contrast', abs(a-.5303300858899106)<1e-14)
    check('overlap_information_between_zero_one', 0<info<1)
    check('energy_unresolved_information_zero', energy_label_information(0)==0)
    check('energy_resolved_information_limit', energy_label_information(8)>1-1e-12)
    for r in (.03,.1,1.):
        yy = np.linspace(-10,15,251)
        check(f'stable_density_scipy_independent_r{r}',
              np.max(abs(log_exgauss(yy,r)-exponnorm.logpdf(yy,r)))<1e-10)
        norm = quad(lambda y: float(np.exp(log_exgauss(y,r))),-np.inf,np.inf,
                    epsabs=1e-11)[0]
        check(f'exgaussian_full_domain_norm_r{r}',abs(norm-1)<2e-11)
    xx, yy = np.meshgrid(np.linspace(-4,4,19),np.linspace(-5,5,23))
    p = log_joint(xx,yy,a,.3,1)
    q = log_joint(xx,yy,a,.3,-1)
    check('zero_lifetime_both_orders_equal', np.max(abs(
        log_joint(xx,yy,a,0,1)-log_joint(xx,yy,a,0,-1)))==0)
    check('zero_energy_contrast_known_prompt_order_equal', np.max(abs(
        log_joint(xx,yy,0,.3,1)-log_joint(xx,yy,0,.3,-1)))==0)
    check('time_reversal_swaps_known_calibrated_orders',
          np.max(abs(p-log_joint(xx,-yy,a,.3,-1)))<1e-13)
    check('simultaneous_detector_relabelling_symmetry',
          np.max(abs(p-log_joint(-xx,-yy,a,.3,1)))<1e-13)
    check('time_only_known_prompt_marginal_identical',np.max(abs(
        time_marginal(yy,.3,1)-time_marginal(yy,.3,-1)))==0)
    # Energy marginal is analytically g(x) because each conditional time density
    # integrates to one. Check the independent numerical integration as well.
    egot=[]
    for sign in (-1,1):
        egot.append(quad(lambda y: float(np.exp(log_joint(.7,y,a,.3,sign))),
                         -np.inf,np.inf,epsabs=1e-11)[0])
    eexpected=.5*(np.exp(log_normal(.7-a))+np.exp(log_normal(.7+a)))
    check('energy_only_marginal_unchanged_and_normalized',
          max(abs(np.array(egot)-eexpected))<1e-11)
    table=[]
    for r in (.03,.05,.1,.3,1.):
        row={'r_chosen':r}
        for name,offset in (('calibrated',0.),('mean_matched',2*r)):
            base=half_jeffreys_grid(a,r,offset)
            fine=half_jeffreys_grid(a,r,offset,nx=140,ny=900,tail=45.)
            independent=half_jeffreys_expectation(a,r,offset,n=42)
            independent_fine=half_jeffreys_expectation(a,r,offset,n=68)
            tol=max(2e-12,fine['J']*3e-7)
            check(f'{name}_norm_r{r}',max(abs(fine['norm_p']-1),
                                        abs(fine['norm_q']-1))<2e-10)
            check(f'{name}_box_and_nodes_convergence_r{r}',abs(base['J']-fine['J'])<tol)
            check(f'{name}_independent_expectation_convergence_r{r}',
                  abs(independent-independent_fine)<max(tol,1e-10))
            check(f'{name}_independent_route_agreement_r{r}',
                  abs(independent_fine-fine['J'])<max(tol,1e-10))
            row[name]={'grid':fine,'expectation_n42':independent,
                       'expectation_n68':independent_fine}
        check(f'mean_matching_reduces_information_in_chosen_case_r{r}',
              row['mean_matched']['grid']['J']<row['calibrated']['grid']['J'])
        table.append(row)
    small_r=.01
    cal=half_jeffreys_grid(a,small_r,ny=700)['J']
    matched=half_jeffreys_grid(a,small_r,2*small_r,ny=700)['J']
    check('small_r_calibrated_2r2I',abs(cal/(2*small_r**2*info)-1)<.001)
    check('small_r_mean_matched_4over3_r6I',abs(matched/(4/3*small_r**6*info)-1)<.01)
    h3=lambda y:y**3-3*y
    h3norm=quad(lambda y: h3(y)**2*math.exp(-y*y/2)/math.sqrt(2*math.pi),
                -np.inf,np.inf)[0]
    check('Hermite3_orthogonal_norm_six',abs(h3norm-6)<1e-10)
    r=.3
    moments=[]
    for sign,off in ((1,0.),(-1,2*r)):
        # Conditional energy label +1; the other label reflects the distribution.
        mm=[quad(lambda y,k=k: y**k*float(np.exp(log_exgauss(sign*(y-off),r))),
                 -np.inf,np.inf,epsabs=1e-10)[0] for k in range(1,5)]
        moments.append(mm)
    check('offset2r_matches_mean_variance',np.max(abs(np.array(moments[0][:2])
                                                          -moments[1][:2]))<1e-10)
    check('third_conditional_raw_moment_difference_4r3',
          abs(moments[0][2]-moments[1][2]-4*r**3)<1e-10)
    check('fourth_time_only_raw_moment_difference_16r4',
          abs(moments[0][3]-moments[1][3]-16*r**4)<1e-10)
    check('mean_matching_not_full_density_matching',
          np.max(abs(time_marginal(yy,r,1)-time_marginal(yy,r,-1,2*r)))>.0001)
    zero_a=half_jeffreys_grid(0,.03,.06,ny=800)['J']
    check('zero_a_mean_matched_can_retain_time_only_r8_information',zero_a>0)
    r8ratio=zero_a/(16/3*.03**8)
    check('zero_a_meanmatched_small_r8_control',abs(r8ratio-1)<.03)
    kh,kl=np.meshgrid(np.linspace(-5,5,17),np.linspace(-5,5,19))
    cp,cm=confusion_characteristic(kh,kl,.3,1/math.sqrt(2))
    check('positive_electronics_tail_exact_full_arrival_characteristic',
          np.max(abs(cp-cm))<1e-15)
    check('confounded_response_characteristic_normalized',
          confusion_characteristic(0,0,.3,1/math.sqrt(2))==(1+0j,1+0j))
    check('confounding_uses_different_energy_specific_response_not_known_prompt',
          abs(1/(1-1j*.3)-1)>0)
    # First-order local design: signed nuclear mean mu and prompt offset w
    # have the same score at mu=w=0. This does NOT replace the full r^6 shape
    # information or calibrate arbitrary electronics tails.
    step=1e-5
    score_mu=(log_joint(xx,yy,a,step,1)-log_joint(xx,yy,a,step,-1))/(2*step)
    # Richardson cancellation of the O(h^2) central-difference error permits
    # a larger h and avoids the cancellation seen with a raw h=1e-5 test.
    def offset_score(h):
        return (log_joint(xx,yy,a,0,1,h)-log_joint(xx,yy,a,0,1,-h))/(2*h)
    score_w=(4*offset_score(.0005)-offset_score(.001))/3
    analytic_score=np.tanh(a*xx)*yy
    check('local_signed_delay_score_Ty',np.max(abs(score_mu-analytic_score))<1e-7)
    check('local_offset_score_same_Ty',np.max(abs(score_w-analytic_score))<1e-9)
    check('third_shape_score_orthogonal_to_offset',abs(quad(
        lambda y:y*h3(y)*math.exp(-y*y/2)/math.sqrt(2*math.pi),
        -np.inf,np.inf)[0])<1e-12)
    target_n=100000
    designs=[]
    for cal_m in (0,1000,100000,10000000):
        target_info=target_n*info
        cal_info=cal_m*info  # Chosen same overlap and independent prompt sample.
        fisher=np.array([[target_info,target_info],
                         [target_info,target_info+cal_info]])
        profile=target_info*cal_info/(target_info+cal_info)
        direct=fisher[0,0]-fisher[0,1]**2/fisher[1,1]
        check(f'local_calibration_Schur_M{cal_m}',abs(profile-direct)<1e-10)
        check(f'local_calibration_PSD_M{cal_m}',np.min(np.linalg.eigvalsh(fisher))>=-1e-10)
        check(f'local_information_bounded_by_calibration_M{cal_m}',
              profile<=cal_info and profile<=target_info)
        designs.append(dict(target_N_chosen=target_n,prompt_M_chosen=cal_m,
                            I_prompt_chosen=info,F=fisher.tolist(),
                            signed_mean_profile_information=profile,
                            fraction_of_known_offset=profile/target_info))
    check('no_prompt_calibration_first_order_rank_one',
          np.linalg.matrix_rank(np.array(designs[0]['F']))==1)
    check('independent_prompt_adds_second_score_direction',
          np.linalg.matrix_rank(np.array(designs[1]['F']))==2)
    return dict(model='declared classical matched-pair energy/time mixture',
                evidence=dict(source='knowledge/sources/herzan-2015-193bi-spectroscopy.md',
                              locator='HE15-9',gap_keV_nominal=gap,
                              actual_middle_tau=None,actual_sigma_E=None,
                              actual_sigma_t=None,actual_timewalk_response=None),
                chosen=dict(sigma_E_keV=sigma_energy,a=a,
                            sigma_t_definition='SD of time DIFFERENCE noise',
                            r_definition='mean_middle_delay/sigma_t',
                            offset_definition='energy-specific lag / sigma_t'),
                divergence_definition='J=(KL(p||q)+KL(q||p))/2; nats; not power or p-value',
                overlap_information=info,table=table,
                small_r=dict(r=small_r,J_cal=cal,J_matched=matched,
                             cal_leading=2*small_r**2*info,
                             matched_leading=4/3*small_r**6*info),
                moments_r03= moments,zero_a_matched=dict(J=zero_a,r8_ratio=r8ratio),
                response_counterexample='Full labelled arrivals iid exGaussian under either order when a distinct uncalibrated prompt electronics tail swaps energy labels; no actual-response assertion.',
                local_prompt_calibration_design=designs,
                local_design_boundary='At signed nuclear mean and offset zero only. A first-order information limit, not a ceiling on full finite-r shape information or a p-value.',
                boundaries=['mean-matched offset is NOT profiled optimum',
                            'factorized Gaussian energy/time responses and equal label acceptance are chosen',
                            'no actual 193Bi order/lifetime/significance or experimental L4 replay'],
                checks=checks,checks_passed=len(checks))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    result=audit()
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(checks_passed=result['checks_passed'],
                          all_checks_true=all(result['checks'].values()),
                          output=str(args.output))))


if __name__=='__main__':
    main()
