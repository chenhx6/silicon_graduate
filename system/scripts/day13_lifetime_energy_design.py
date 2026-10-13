#!/usr/bin/env python3
"""Day13 synthetic lifetime/unknown-energy conditional-shape design.

CO19 motivates fitting lifetime and gamma energy jointly; this is not its
generator or a fit to its data. Beta(t) is a chosen linear function of proper
time for .13ps, then constant exitbeta. E0, sigma, point angles, counts and
uniform angle weights are chosen; isotropic-rest angular acceptance included.
Expected2N*KL compares exact synthetic models, not actual significance.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.optimize import minimize_scalar


BETA_IN=.105
BETA_EXIT=.10
PROPER_EXIT_PS=.13
SIGMA_KEV=1.5
ANGLES=np.array([130.,150.,170.])


def kernel(tau,angle,order=96,beta_in=BETA_IN):
    nodes,weights=leggauss(order)
    times=PROPER_EXIT_PS*(nodes+1)/2
    beta=beta_in+(BETA_EXIT-beta_in)*times/PROPER_EXIT_PS
    cosine=math.cos(math.radians(angle))
    din=(1-beta*cosine)/np.sqrt(1-beta*beta)
    dexit=(1-BETA_EXIT*cosine)/math.sqrt(1-BETA_EXIT*BETA_EXIT)
    ratios=np.concatenate((dexit/din,[1.]))
    inside=weights*PROPER_EXIT_PS/2*np.exp(-times/tau)/tau/din**2
    outside=math.exp(-PROPER_EXIT_PS/tau)/dexit**2
    probability=np.concatenate((inside,[outside]));probability/=np.sum(probability)
    return ratios,probability


def density(grid,e0,tau,angle,order=96,beta_in=BETA_IN):
    ratios,weights=kernel(tau,angle,order,beta_in)
    gaussian=np.exp(-.5*((grid[:,None]-e0*ratios[None,:])/SIGMA_KEV)**2)/(math.sqrt(2*math.pi)*SIGMA_KEV)
    return gaussian@weights


def moments(e0,tau,angle,order=96):
    ratios,weights=kernel(tau,angle,order)
    mu=float(weights@ratios)*e0
    variance=SIGMA_KEV**2+float(weights@((e0*ratios-mu)**2))
    return mu,variance


def calculate():
    true_e0,true_tau,alternative_tau=2396.,.2,.32
    grid=np.linspace(true_e0-60,true_e0+40,1251)
    true_densities=[density(grid,true_e0,true_tau,a) for a in ANGLES]
    normalization_errors=[abs(float(np.trapezoid(d,grid))-1) for d in true_densities]
    max_order=max(float(np.max(np.abs(d-density(grid,true_e0,true_tau,a,order=192))))
                  for d,a in zip(true_densities,ANGLES))
    # Mean-centroid fit has one common E0 scale; tau is fixed to the alternate.
    true_h=np.array([moments(1.,true_tau,a)[0] for a in ANGLES])
    alt_h=np.array([moments(1.,alternative_tau,a)[0] for a in ANGLES])
    mean_only_energy=true_e0*float(true_h@alt_h)/float(alt_h@alt_h)
    centroid_residuals=mean_only_energy*alt_h-true_e0*true_h
    def kl(e0):
        values=[]
        for angle,p in zip(ANGLES,true_densities):
            q=density(grid,e0,alternative_tau,angle)
            values.append(float(np.trapezoid(p*(np.log(np.maximum(p,1e-300))-np.log(np.maximum(q,1e-300))),grid)))
        return float(np.mean(values))
    fit=minimize_scalar(kl,bounds=(true_e0-10,true_e0+10),method='bounded',options={'xatol':1e-8})
    assert fit.success and fit.fun>0
    # Independent importance-weighted Monte Carlo of proper emission times
    # and Gaussian measurement for the chosen point-detector angular density.
    rng=np.random.default_rng(131026);times=rng.exponential(true_tau,500000)
    beta=np.where(times<PROPER_EXIT_PS,BETA_IN+(BETA_EXIT-BETA_IN)*times/PROPER_EXIT_PS,BETA_EXIT)
    moment_checks=[];max_mean_difference=0.
    for angle in ANGLES:
        cosine=math.cos(math.radians(angle));d=(1-beta*cosine)/np.sqrt(1-beta*beta)
        dexit=(1-BETA_EXIT*cosine)/math.sqrt(1-BETA_EXIT**2)
        photons=true_e0*dexit/d+rng.normal(0.,SIGMA_KEV,len(times))
        w=1/d**2
        measured_mean=float(w@photons/np.sum(w))
        measured_variance=float(w@((photons-measured_mean)**2)/np.sum(w))
        expected_mean,expected_variance=moments(true_e0,true_tau,angle)
        max_mean_difference=max(max_mean_difference,abs(measured_mean-expected_mean))
        assert abs(measured_mean-expected_mean)<.03 and abs(measured_variance/expected_variance-1)<.01
        moment_checks.append({'angle_deg':float(angle),'analytic_mean_keV':expected_mean,
                              'MC_mean_keV':measured_mean,'analytic_variance_keV2':expected_variance,
                              'MC_variance_keV2':measured_variance})
    # With no velocity loss the normalized energy shape loses the lifetime
    # information; the lifetime still lives in time/count inputs not modelled.
    noloss=density(grid,true_e0,.2,150.,beta_in=BETA_EXIT)
    noloss_alt=density(grid,true_e0,.32,150.,beta_in=BETA_EXIT)
    assert np.max(np.abs(noloss-noloss_alt))<1e-12
    long_ratios,long_weights=kernel(1e7,150.)
    assert long_weights[-1]>.9999999
    same=float(np.mean([np.trapezoid(p*(np.log(np.maximum(p,1e-300))-np.log(np.maximum(p,1e-300))),grid) for p in true_densities]))
    assert same==0 and max(normalization_errors)<1e-9 and max_order<1e-9
    return {'schema_version':1,'kind':'synthetic lifetime/energy design; no sourcechi2, measured lifetime or force comparison',
            'chosen_parameters':{'true_rest_gamma_keV':true_e0,'true_proper_tau_ps':true_tau,
                                 'fixed_alternative_tau_ps':alternative_tau,'beta_in':BETA_IN,'beta_exit':BETA_EXIT,
                                 'proper_slowing_duration_ps':PROPER_EXIT_PS,'Gaussian_sigma_keV':SIGMA_KEV,
                                 'point_angles_deg':ANGLES.tolist(),'angle_weights':'equal conditional photon samples'},
            'centroid_only_alternative':{'fitted_alternative_rest_energy_keV':mean_only_energy,
                                         'three_centroid_residuals_keV':centroid_residuals.tolist(),
                                         'mean_absolute_residual_keV':float(np.mean(np.abs(centroid_residuals)))},
            'full_shape_alternative':{'fitted_alternative_rest_energy_keV':float(fit.x),
                                      'minimum_mean_KL_per_conditional_photon':float(fit.fun),
                                      'KL_for_centroid_only_alternative':kl(mean_only_energy),
                                      'expected_two_loglikelihood_metrics':[{'chosen_total_photons':n,'expected2N_KL':2*n*float(fit.fun)} for n in (1000,10000)]},
            'moment_checks':moment_checks,'verification':{'energy_profile_normalization_max_error':max(normalization_errors),
                                                         'time_quad96_192_density_max_difference':max_order,
                                                         'importance_MC_moments_passed':True,'max_MC_mean_difference_keV':max_mean_difference,
                                                         'no_loss_tau_independence_limit_passed':True,'long_tau_outside_limit_passed':True,
                                                         'same_model_KL_zero_passed':True,'passed':True},
            'boundaries':['Fixed reaction point, chosen slowing law and response; not the CO19 depth/stopping/feeding/geometry model.',
                          'Source NN200/320fs scales motivate hypotheses only; this is not measured NN/NNN evidence.',
                          'Expected2N*KL is conditional on exact chosen models and counts, not a confidence or actualchi2.',
                          'Unknown stopping, energycalibration, feeding, response/tails and covariance can reduce or change identifiability.'],
            'numpy_version':np.__version__}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True);a=p.parse_args();r=calculate()
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'output':str(a.output),'verification':r['verification'],
                     'centroid':r['centroid_only_alternative'],'fullshape':r['full_shape_alternative']}))


if __name__=='__main__':
    main()
