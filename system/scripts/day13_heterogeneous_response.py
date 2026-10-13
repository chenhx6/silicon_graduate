#!/usr/bin/env python3
"""Day13 declared heterogeneous-Gaussian response fixture.

LG20 Eq4 supplies a position-response template p(Ehit)=1.9+4.4 sqrt(100/Ehit)
mm FWHM. Two Ehit groups and weights, photon energy, beta, geometry and
intrinsic Gaussian comparator are self-chosen; they are not a GANIL refit or
confirmation of the empirical function outside the source's measured domain.
Angles and position FWHM are related by a first-order one-dimensional model.
All linewidths/centroid gains below are conditional on exact known input widths.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq


K_FWHM=2*math.sqrt(2*math.log(2))


def gaussian_density(x, sigmas):
    return np.exp(-.5*(x/sigmas)**2)/(math.sqrt(2*math.pi)*sigmas)


def calculate():
    rest,beta,theta,radius=1000.,.3,math.pi/2,150.
    baseline=2.6  # self-chosen corrected-energy Gaussian FWHM comparator
    deposits=np.array([50.,1000.]);fractions=np.array([.2,.8])
    position=1.9+4.4*np.sqrt(100/deposits)
    angular_sensitivity=rest*beta*math.sin(theta)/(1-beta*math.cos(theta))
    widths=np.sqrt(baseline**2+(angular_sensitivity*position/radius)**2)
    sigmas=widths/K_FWHM
    density=lambda x:float(fractions@gaussian_density(x,sigmas))
    actual_fwhm=2*brentq(lambda x:density(x)-density(0)/2,0,3*float(np.max(widths)))
    variance=float(fractions@(sigmas**2))
    effective_width=K_FWHM*math.sqrt(variance)
    mean_p=float(fractions@position)
    rms_p=math.sqrt(float(fractions@(position**2)))
    wrong_mean_width=math.hypot(baseline,angular_sensitivity*mean_p/radius)
    correct_variance_width=math.hypot(baseline,angular_sensitivity*rms_p/radius)
    normalization=quad(density,-np.inf,np.inf,epsabs=1e-10)[0]
    second_moment=quad(lambda x:x*x*density(x),-np.inf,np.inf,epsabs=1e-9)[0]
    assert abs(normalization-1)<1e-10 and abs(second_moment-variance)/variance<1e-10
    assert abs(correct_variance_width-effective_width)<1e-12
    assert wrong_mean_width<effective_width and actual_fwhm<effective_width
    gates=[]
    for half_width in (actual_fwhm/2,actual_fwhm,2*actual_fwhm):
        actual=float(fractions@np.array([math.erf(half_width/(math.sqrt(2)*s)) for s in sigmas]))
        same_fwhm_gaussian=math.erf(half_width/(math.sqrt(2)*actual_fwhm/K_FWHM))
        same_variance_gaussian=math.erf(half_width/(math.sqrt(2*variance)))
        gates.append({'half_width_keV':half_width,'mixture_fraction':actual,
                      'same_halfheight_FWHM_Gaussian_fraction':same_fwhm_gaussian,
                      'same_variance_Gaussian_fraction':same_variance_gaussian})
    # Fixed counts in each group ensure precision comparisons are independent
    # of random group-occupancy fluctuation. No selection/efficiency is inferred.
    rng=np.random.default_rng(131019);per_trial=1000;trials=20000
    counts=(fractions*per_trial).astype(int);sample_sigmas=np.repeat(sigmas,counts)
    inv_variance=1/sample_sigmas**2
    weighted_sigma=math.sqrt(1/float(np.sum(inv_variance)))
    ordinary_sigma=math.sqrt(float(np.sum(sample_sigmas**2)))/per_trial
    ordinary_est=[];weighted_est=[]
    for _ in range(20):
        data=rng.normal(0.,sample_sigmas,size=(trials//20,per_trial))
        ordinary_est.extend(np.mean(data,axis=1))
        weighted_est.extend((data@inv_variance)/np.sum(inv_variance))
    ordinary_MC=float(np.std(ordinary_est));weighted_MC=float(np.std(weighted_est))
    assert abs(ordinary_MC/ordinary_sigma-1)<.025 and abs(weighted_MC/weighted_sigma-1)<.025
    # A group-dependent centroid violates the shared-mean premise.
    group_mean=np.array([1.,0.])
    ordinary_bias=float(fractions@group_mean)
    weighted_bias=float((fractions/sigmas**2)@group_mean/np.sum(fractions/sigmas**2))
    equal_sigma=np.full(2,2.)
    equal_density=lambda x:float(fractions@gaussian_density(x,equal_sigma))
    equal_fwhm=2*brentq(lambda x:equal_density(x)-equal_density(0)/2,0.,10.)
    assert abs(equal_fwhm-K_FWHM*2)<1e-10
    return {'schema_version':1,'kind':'synthetic conditional energy-dependent position-response mixture',
            'parameters':{'rest_gamma_keV':rest,'beta':beta,'theta_deg':90.,'firstIP_distance_mm':radius,
                          'baseline_corrected_Gaussian_FWHM_keV':baseline,'hit_deposit_energies_keV':deposits.tolist(),
                          'group_fractions':fractions.tolist(),'angular_sensitivity_keV_per_rad':angular_sensitivity},
            'position_template_FWHM_mm':position.tolist(),'conditional_energy_FWHMs_keV':widths.tolist(),
            'position_mean_FWHM_mm':mean_p,'position_rms_FWHM_mm':rms_p,
            'mixture_halfheight_FWHM_keV':actual_fwhm,'mixture_sigma_keV':math.sqrt(variance),
            'same_variance_Gaussian_FWHM_keV':effective_width,
            'wrong_mean_position_substitution_FWHM_keV':wrong_mean_width,'finite_gates':gates,
            'known_per_event_variance_centroid':{'counts_per_trial':per_trial,'trials':trials,
                                                'ordinary_sigma_analytic_keV':ordinary_sigma,'ordinary_sigma_MC_keV':ordinary_MC,
                                                'weighted_sigma_analytic_keV':weighted_sigma,'weighted_sigma_MC_keV':weighted_MC,
                                                'precision_gain_sigma_ratio':ordinary_sigma/weighted_sigma,
                                                'boundary':'conditional on true variances and a common group centroid, not actual tracking performance'},
            'different_group_centroid_counterexample':{'chosen_means_keV':group_mean.tolist(),
                                                      'ordinary_shared_mean_bias_keV':ordinary_bias,
                                                      'weighted_shared_mean_bias_keV':weighted_bias},
            'verification':{'mixture_normalization_error':abs(normalization-1),
                            'mixture_variance_integral_relative_error':abs(second_moment-variance)/variance,
                            'variance_RMS_position_identity_passed':True,'conditional_centroid_MC_passed':True,
                            'equal_width_Gaussian_limit_passed':True,'passed':True},
            'boundaries':['No actual source deposit spectrum, orientation/depth response or covariance supplied.',
                          'LG20 response law is a template in this fixture, not a new measurement or unconditional extrapolation.',
                          'Physical natural Lorentz tails are absent; all conditional moments here are finite Gaussian.',
                          'A Gaussian-fit linewidth depends on the fit definition/window and need not equal the mixture half-height FWHM.'],
            'numpy_version':np.__version__}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True);a=p.parse_args();r=calculate()
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'output':str(a.output),'verification':r['verification'],
                     'mixture_FWHM_keV':r['mixture_halfheight_FWHM_keV'],
                     'variance_equivalent_FWHM_keV':r['same_variance_Gaussian_FWHM_keV'],
                     'wrong_mean_position_FWHM_keV':r['wrong_mean_position_substitution_FWHM_keV']}))


if __name__=='__main__':
    main()
