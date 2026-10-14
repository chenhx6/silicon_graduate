#!/usr/bin/env python3
"""Chosen 1D foil/depth priors and exit-velocity information for DAY13.

Not the CM21 binary reaction/TKEL generator. Equal effective beam/product
stopping gives depth-independent exit energy despite different entry/history.
Relativistic slowing is parameterized exactly in proper time for constant S.
"""
from __future__ import annotations

import argparse
import json
import math
from functools import lru_cache
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.integrate import quad
from scipy.optimize import minimize, minimize_scalar


M_MEV=20*931.49410242
C_UM_PS=299.792458
L_UM=4.0
BEAM_MEV=100.0
CHANNEL_LOSS_MEV=4.0
S_MEV_UM=2.5
EXIT_MEV=BEAM_MEV-CHANNEL_LOSS_MEV-S_MEV_UM*L_UM
ETA_EXIT=math.acosh(1+EXIT_MEV/M_MEV)
ETA_MAX=math.acosh(1+(BEAM_MEV-CHANNEL_LOSS_MEV)/M_MEV)
A_PER_PS=S_MEV_UM*C_UM_PS/M_MEV
E0_KEV=2396.1
SIGMA_KEV=1.5
ANGLES=(130.,150.,170.)


def depth_pdf(x,prior):
    if prior=='uniform':
        return np.ones_like(x)/L_UM
    if prior=='front':
        return 2*(L_UM-x)/L_UM**2
    if prior=='back':
        return 2*x/L_UM**2
    raise ValueError(prior)


def eta_entry_pdf(eta,prior):
    x=(BEAM_MEV-CHANNEL_LOSS_MEV-M_MEV*(np.cosh(eta)-1))/S_MEV_UM
    return depth_pdf(x,prior)*M_MEV*np.sinh(eta)/S_MEV_UM


@lru_cache(maxsize=12)
def eta_grid(order):
    nodes,weights=leggauss(order)
    eta=ETA_EXIT+(ETA_MAX-ETA_EXIT)*(nodes+1)/2
    return eta,weights*(ETA_MAX-ETA_EXIT)/2


def kernel(tau,prior,angle,order=96,inner_order=48):
    eta,w_eta=eta_grid(order)
    nodes,w_inner=leggauss(inner_order)
    z=eta[:,None]+(ETA_MAX-eta[:,None])*(nodes+1)/2
    emission=np.sum(eta_entry_pdf(z,prior)*np.exp(-(z-eta[:,None])/(A_PER_PS*tau))
                    *w_inner*(ETA_MAX-eta[:,None])/2,axis=1)/(A_PER_PS*tau)
    outside=float(np.sum(w_eta*eta_entry_pdf(eta,prior)
                         *np.exp(-(eta-ETA_EXIT)/(A_PER_PS*tau))))
    mass=float(w_eta@emission+outside)
    cosine=math.cos(math.radians(angle))
    d=np.cosh(eta)-np.sinh(eta)*cosine
    d_exit=math.cosh(ETA_EXIT)-math.sinh(ETA_EXIT)*cosine
    ratios=np.r_[d_exit/d,1.]
    weights=np.r_[w_eta*emission/d**2,outside/d_exit**2]
    weights/=weights.sum()
    assert abs(mass-1)<1e-8
    return ratios,weights,mass,outside


def density(grid,e0,tau,prior,angle,order=96,inner_order=48):
    ratios,weights,_,_=kernel(tau,prior,angle,order,inner_order)
    gauss=np.exp(-0.5*((grid[:,None]-e0*ratios)/SIGMA_KEV)**2)
    return gauss@weights/(math.sqrt(2*math.pi)*SIGMA_KEV)


def moments(e0,tau,prior,angle):
    ratios,w,_,_=kernel(tau,prior,angle,192,96)
    centers=e0*ratios
    mu=float(w@centers)
    return mu,SIGMA_KEV**2+float(w@((centers-mu)**2))


def calculate():
    tau=0.08
    grid=np.linspace(E0_KEV-60,E0_KEV+30,901)
    fit_cases=[]
    max_norm_error=max_quad_error=0.
    for prior in ('uniform','front','back'):
        truth=[density(grid,E0_KEV,tau,prior,a)for a in ANGLES]
        for a,p in zip(ANGLES,truth):
            max_norm_error=max(max_norm_error,abs(float(np.trapezoid(p,grid))-1))
            max_quad_error=max(max_quad_error,float(np.max(np.abs(
                p-density(grid,E0_KEV,tau,prior,a,192,96)))))
        def kl(t,e):
            terms=[]
            for a,p in zip(ANGLES,truth):
                q=density(grid,e,t,'uniform',a)
                terms.append(float(np.trapezoid(p*(np.log(np.maximum(p,1e-300))
                                                  -np.log(np.maximum(q,1e-300))),grid)))
            return float(np.mean(terms))
        fixed=minimize_scalar(lambda t:kl(t,E0_KEV),bounds=(0.01,0.4),method='bounded',
                              options={'xatol':1e-10})
        profiles=[minimize(lambda v:kl(v[0],v[1]),start,method='L-BFGS-B',
                           bounds=[(0.01,0.4),(E0_KEV-5,E0_KEV+5)],
                           options={'ftol':1e-13,'gtol':1e-8})
                  for start in [(float(fixed.x),E0_KEV),(.06,E0_KEV-1),(.16,E0_KEV+1)]]
        assert fixed.success and any(r.success for r in profiles)
        best=min((r for r in profiles if r.success),key=lambda r:r.fun)
        assert best.fun<=fixed.fun+1e-9
        ratios,w,mass,outside=kernel(tau,prior,150)
        mean,var=moments(E0_KEV,tau,prior,150)
        fit_cases.append(dict(chosen_true_depth_prior=prior,chosen_true_tau_fs=tau*1000,
                              exit_energy_MeV=EXIT_MEV,exit_beta=math.tanh(ETA_EXIT),
                              pre_photon_outside_fraction=outside,
                              corrected150_mean_keV=mean,corrected150_variance_keV2=var,
                              wrong_uniform_fixed_E_tau_fs=float(fixed.x)*1000,
                              fixed_E_mean_KL=max(0.,float(fixed.fun)),
                              wrong_uniform_profiled_tau_fs=float(best.x[0])*1000,
                              profiled_rest_gamma_keV=float(best.x[1]),
                              profiled_mean_KL=max(0.,float(best.fun)),
                              optimizer_multistart_success=[bool(r.success)for r in profiles]))
    assert abs(fit_cases[0]['wrong_uniform_profiled_tau_fs']-80)<0.001
    assert fit_cases[0]['profiled_mean_KL']<1e-12
    assert max_norm_error<1e-9 and max_quad_error<1e-9
    # Proper slowing clock checked by an independent path integral.
    clock_errors=[]
    for x in (0.,1.,2.,3.9):
        ti=BEAM_MEV-CHANNEL_LOSS_MEV-S_MEV_UM*x
        eta=math.acosh(1+ti/M_MEV)
        analytic=(eta-ETA_EXIT)/A_PER_PS
        numeric=quad(lambda distance:1/(C_UM_PS*math.sqrt(
            (1+(ti-S_MEV_UM*distance)/M_MEV)**2-1)),0,L_UM-x,
                     epsabs=1e-12)[0]
        clock_errors.append(abs(analytic-numeric))
    assert max(clock_errors)<1e-11
    # Independent depth/time Monte Carlo, including conditional photon beaming.
    rng=np.random.default_rng(131424)
    mc=[]
    n=500000
    for prior in ('uniform','front','back'):
        random=rng.random(n)
        x=L_UM*random if prior=='uniform' else (
            L_UM*(1-np.sqrt(random))if prior=='front' else L_UM*np.sqrt(random))
        ti=BEAM_MEV-CHANNEL_LOSS_MEV-S_MEV_UM*x
        tf=ti-S_MEV_UM*(L_UM-x)
        assert np.max(np.abs(tf-EXIT_MEV))<1e-12
        eta=np.arccosh(1+ti/M_MEV)
        eta_emit=np.maximum(eta-A_PER_PS*rng.exponential(tau,n),ETA_EXIT)
        c=math.cos(math.radians(150.))
        d=np.cosh(eta_emit)-np.sinh(eta_emit)*c
        de=math.cosh(ETA_EXIT)-math.sinh(ETA_EXIT)*c
        measured=E0_KEV*de/d+rng.normal(0,SIGMA_KEV,n)
        w=1/d**2
        mu=float(w@measured/w.sum());var=float(w@((measured-mu)**2)/w.sum())
        se=float(np.sqrt(np.sum(w*w*(measured-mu)**2))/w.sum())
        expected_mu,expected_var=moments(E0_KEV,tau,prior,150.)
        assert abs(mu-expected_mu)<5*se and abs(var/expected_var-1)<0.015
        mc.append(dict(prior=prior,mean_entry_energy_MeV=float(ti.mean()),
                       final_energy_max_deviation_MeV=float(np.max(np.abs(tf-EXIT_MEV))),
                       analytic_photon_mean_keV=expected_mu,MC_photon_mean_keV=mu,
                       MC_mean_SE_keV=se,analytic_photon_variance_keV2=expected_var,
                       MC_photon_variance_keV2=var))
    # Stopping contrast restores information about depth in final energy.
    contrast=[]
    for product_s in (2.,2.5,3.):
        for prior,mean_x,var_x in [('uniform',L_UM/2,L_UM**2/12),
                                  ('front',L_UM/3,L_UM**2/18),
                                  ('back',2*L_UM/3,L_UM**2/18)]:
            slope=product_s-S_MEV_UM
            contrast.append(dict(chosen_product_S_MeV_per_um=product_s,prior=prior,
                                 final_energy_mean_MeV=BEAM_MEV-CHANNEL_LOSS_MEV-product_s*L_UM+slope*mean_x,
                                 final_intrinsic_variance_MeV2=slope*slope*var_x))
    _,weights,_,_=kernel(1e8,'uniform',150.)
    assert weights[-1]>.99999999
    # The no-loss limit has one speed for all entries/decays and no lifetime shape.
    no_loss_beta=math.sqrt(1-(1+(BEAM_MEV-CHANNEL_LOSS_MEV)/M_MEV)**-2)
    d0=(1-no_loss_beta*math.cos(math.radians(150.)))/math.sqrt(1-no_loss_beta**2)
    assert abs(E0_KEV/d0*d0-E0_KEV)<1e-10
    return dict(schema_version=1,kind='synthetic equal-stopping depth/exit-velocity design',
                chosen_parameters=dict(mass_proxy_MeV=M_MEV,collinear_1D=True,
                                       foil_length_um=L_UM,beam_energy_MeV=BEAM_MEV,
                                       fixed_channel_kinetic_loss_MeV=CHANNEL_LOSS_MEV,
                                       effective_beam_and_product_S_MeV_um=S_MEV_UM,
                                       exit_energy_MeV=EXIT_MEV,true_proper_tau_ps=tau,
                                       gamma_rest_keV=E0_KEV,Gaussian_corrected_sigma_keV=SIGMA_KEV,
                                       point_angles_deg=list(ANGLES)),
                maximum_proper_crossing_ps=(ETA_MAX-ETA_EXIT)/A_PER_PS,
                prior_and_wrong_uniform_fits=fit_cases,independent_MC=mc,
                stopping_contrast_controls=contrast,
                verification=dict(energy_work_and_equal_exit_passed=True,
                                  independent_path_integral_clock_max_error_ps=max(clock_errors),
                                  profile_normalization_max_error=max_norm_error,
                                  quadrature96_48_vs192_96_max_error=max_quad_error,
                                  independent_depth_time_and_photon_MC_passed=True,
                                  uniform_truth_fit_passed=True,
                                  long_tau_outside_and_no_loss_limits_passed=True,
                                  all_passed=True),
                boundaries=['Not the CM21 45degree binary reaction, TKEL unfolding or actual foil stopping law.',
                            'Equal effective beam/product S is a chosen information-loss limit; real geometry/contrast can exclude it.',
                            'No mass-changing reaction kinematics, angular/energy straggling, photon recoil or detector position covariance.',
                            'Wrong-prior pseudo-true tau/E and KL are chosen-model predictions, not source bias or a lifetime refit.',
                            'Measured entry kinematics or a constrained physical depth prior can distinguish these histories.'])


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();r=calculate()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'output':str(args.output),'verification':r['verification'],
                      'fits':r['prior_and_wrong_uniform_fits'],'proper_crossing_ps':r['maximum_proper_crossing_ps']}))


if __name__=='__main__':
    main()
