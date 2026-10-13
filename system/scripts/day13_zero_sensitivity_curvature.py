#!/usr/bin/env python3
"""Day13 second-order longitudinal-beta exercise at cos(theta)=beta0.

Fixed lab photon direction and exact line energy are chosen. Case 1 changes
the beta used by the inverse while holding the measured lab photon fixed.
Case 2 changes the actual emitter speed and holds the inverse beta fixed.
No angular/energy response or detector selection is included. They are two
different fixtures, not simultaneous independent error terms for one dataset.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np


def factor(beta, cosine):
    return (1-np.asarray(beta)*cosine)/np.sqrt(1-np.asarray(beta)**2)


def calculate():
    rng=np.random.default_rng(131021);samples=600000;rows=[];max_curvature=0.;max_sigma_difference=0.
    for rest,beta0,sigma_beta in ((1000.,.07,.002),(1000.,.2,.02),(15000.,.5,.02)):
        cosine=beta0;gamma=1/math.sqrt(1-beta0*beta0)
        d0=float(factor(beta0,cosine));lab=rest/d0
        curvature=rest*gamma**4
        step=1e-4
        f=lambda beta:lab*float(factor(beta,cosine))
        fd_curvature=(f(beta0+step)-2*f(beta0)+f(beta0-step))/(step*step)
        relative_curvature=abs(fd_curvature/curvature-1);max_curvature=max(max_curvature,relative_curvature)
        predicted_mean=.5*curvature*sigma_beta**2
        predicted_sigma=curvature*sigma_beta**2/math.sqrt(2)
        noise=rng.normal(0.,sigma_beta,samples);betas=beta0+noise
        assert np.max(np.abs(betas))<1.
        uncertain_inverse=lab*factor(betas,cosine)-rest
        actual_spread=rest*d0/factor(betas,cosine)-rest
        mean_inverse=float(np.mean(uncertain_inverse));sigma_inverse=float(np.std(uncertain_inverse))
        mean_spread=float(np.mean(actual_spread));sigma_spread=float(np.std(actual_spread))
        max_sigma_difference=max(max_sigma_difference,abs(sigma_inverse/predicted_sigma-1),abs(sigma_spread/predicted_sigma-1))
        assert np.min(uncertain_inverse)>-1e-8 and np.max(actual_spread)<1e-8
        assert abs(mean_inverse/predicted_mean-1)<.05 and abs(mean_spread/(-predicted_mean)-1)<.05
        assert np.max(np.abs(lab*factor(np.full(10,beta0),cosine)-rest))<1e-10
        rows.append({'rest_photon_keV':rest,'beta0':beta0,'self_chosen_longitudinal_sigma_beta':sigma_beta,
                     'lab_theta_deg':math.degrees(math.acos(cosine)),
                     'first_order_beta_variance_prediction_keV2':0.,
                     'second_derivative_keV':curvature,'FD_second_derivative_keV':fd_curvature,
                     'leading_mean_magnitude_keV':predicted_mean,'leading_sigma_keV':predicted_sigma,
                     'fixed_lab_uncertain_inverse_mean_keV':mean_inverse,'fixed_lab_uncertain_inverse_sigma_keV':sigma_inverse,
                     'true_beta_spread_fixed_inverse_mean_keV':mean_spread,'true_beta_spread_fixed_inverse_sigma_keV':sigma_spread,
                     'boundary':'No other response/angle/acceptance kernel; each distribution is non-Gaussian, not a measured linewidth'})
    assert max_curvature<1e-6 and max_sigma_difference<.06
    return {'schema_version':1,'kind':'synthetic second-order zero-Jacobian speed error/dispersion fixtures',
            'rows':rows,'verification':{'zero_linear_derivative_condition_used':True,
                                       'second_derivative_FD_max_relative_error':max_curvature,
                                       'exact_MC_sigma_vs_leading_max_relative_difference':max_sigma_difference,
                                       'opposite_residual_signs_for_two_distinct_fixtures_passed':True,
                                       'zero_uncertainty_inverse_limit_passed':True,'passed':True},
            'boundaries':['Known cos(theta)=beta0 and exact lab direction are self-chosen.',
                          'Correction-estimator errors and actual emitter spread are distinct; their energy/velocity covariance differs.',
                          'A real detector adds intrinsic, angle, position, history and selection uncertainty.',
                          'Leading sigma is not an actual Gaussian FWHM; no observed source tail is attributed to this mechanism.'],
            'numpy_version':np.__version__}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,required=True);a=p.parse_args();r=calculate()
    a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'output':str(a.output),'verification':r['verification'],'rows':r['rows']}))


if __name__=='__main__':
    main()
