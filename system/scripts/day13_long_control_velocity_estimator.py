#!/usr/bin/env python3
"""Chosen DAY13 long gamma controls: finite history and velocity estimator.

CM21 control energies/lifetimes motivate scales; the proper-time trajectory,
angles/noise and whole-line-mean/peak-mode estimators are chosen. Neither is
identified with the paper's actual calibration algorithm or stopping law.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.optimize import brentq, minimize_scalar


CHOSEN_BETA_IN = 0.10
TRUE_BETA_EXIT = 0.09
CHOSEN_PROPER_CROSSING_PS = 0.13
LAB_GAUSSIAN_SIGMA_KEV = 1.0
ANGLES = (130.0, 150.0, 170.0)
CONTROLS = ((1375.80, 1.27), (3853.170, 12.4))


def doppler_factor(beta, angle):
    return (1-beta*math.cos(math.radians(angle)))/np.sqrt(1-beta**2)


def kernel(tau, angle, beta_exit=TRUE_BETA_EXIT, order=128):
    nodes, weights = leggauss(order)
    t = CHOSEN_PROPER_CROSSING_PS*(nodes+1)/2
    beta = CHOSEN_BETA_IN+(beta_exit-CHOSEN_BETA_IN)*t/CHOSEN_PROPER_CROSSING_PS
    time_weights = np.r_[weights*CHOSEN_PROPER_CROSSING_PS/2*np.exp(-t/tau)/tau,
                        math.exp(-CHOSEN_PROPER_CROSSING_PS/tau)]
    assert abs(time_weights.sum()-1) < 1e-12
    all_beta = np.r_[beta, beta_exit]
    d = doppler_factor(all_beta, angle)
    photon_weights = time_weights/d**2
    photon_weights /= photon_weights.sum()
    return all_beta, d, photon_weights


def mean_lab(e0, tau, angle, beta_exit=TRUE_BETA_EXIT, order=128):
    _, d, w = kernel(tau, angle, beta_exit, order)
    return float(w @ (e0/d))


def calculate():
    results = []
    order_error = 0.0
    modes = []
    for e0, tau in CONTROLS:
        for angle in ANGLES:
            b, d, w = kernel(tau, angle)
            centers = e0/d
            mean = float(w @ centers)
            order_error = max(order_error, abs(mean-mean_lab(e0, tau, angle, order=256)))
            exit_lab = e0/float(doppler_factor(TRUE_BETA_EXIT, angle))
            def density(energy):
                g = np.exp(-0.5*((energy-centers)/LAB_GAUSSIAN_SIGMA_KEV)**2)
                return float(w @ g)/(math.sqrt(2*math.pi)*LAB_GAUSSIAN_SIGMA_KEV)
            def density_derivative(energy):
                offset=energy-centers
                g=np.exp(-0.5*(offset/LAB_GAUSSIAN_SIGMA_KEV)**2)
                return float(w @ (-offset*g/LAB_GAUSSIAN_SIGMA_KEV**2))/(
                    math.sqrt(2*math.pi)*LAB_GAUSSIAN_SIGMA_KEV)
            fit_mode = minimize_scalar(lambda value:-density(value),
                                       bounds=(float(centers.min()-5), float(centers.max()+5)),
                                       method='bounded', options={'xatol':1e-9})
            assert fit_mode.success
            # The bounded optimizer has a relative energy tolerance floor.
            # Refine the selected dominant mode through its analytic score.
            mode = brentq(density_derivative, exit_lab-2*LAB_GAUSSIAN_SIGMA_KEV,
                           exit_lab+2*LAB_GAUSSIAN_SIGMA_KEV,xtol=1e-12)
            assert abs(density_derivative(mode))<1e-10
            coarse=np.linspace(float(centers.min()-5),float(centers.max()+5),401)
            assert density(mode)>=max(density(value) for value in coarse)-1e-10
            assert density(mode) >= density(exit_lab)-1e-10
            apparent_mean_beta = brentq(lambda value:mean*float(doppler_factor(value,angle))-e0,
                                       TRUE_BETA_EXIT-1e-8,CHOSEN_BETA_IN,xtol=1e-14)
            apparent_mode_beta = brentq(lambda value:mode*float(doppler_factor(value,angle))-e0,
                                       TRUE_BETA_EXIT-1e-8,CHOSEN_BETA_IN,xtol=1e-14)
            # Correct finite-history mean model can recover the chosen late
            # speed; that recovery still assumes the declared trajectory.
            physical_beta = brentq(lambda value:mean_lab(e0,tau,angle,value)-mean,
                                   0.085,0.095,xtol=1e-13)
            assert abs(physical_beta-TRUE_BETA_EXIT)<1e-10
            target_rest=2396.1
            d_exit=float(doppler_factor(TRUE_BETA_EXIT,angle))
            results.append(dict(context_control_rest_energy_keV=e0,context_control_tau_ps=tau,
                                chosen_angle_deg=angle,
                                pre_photon_inside_fraction=1-math.exp(-CHOSEN_PROPER_CROSSING_PS/tau),
                                conditional_inside_photon_fraction=float(w[:-1].sum()),
                                lab_mean_keV=mean,lab_mode_keV=mode,late_only_lab_energy_keV=exit_lab,
                                bounded_optimizer_mode_keV=float(fit_mode.x),
                                analytic_score_refinement_keV=mode-float(fit_mode.x),
                                exit_reference_mean_residual_keV=mean*d_exit-e0,
                                exit_reference_mode_residual_keV=mode*d_exit-e0,
                                beta_from_whole_line_mean_and_late_only_model=apparent_mean_beta,
                                beta_from_peak_mode_and_late_only_model=apparent_mode_beta,
                                beta_from_declared_finite_history_model=physical_beta,
                                chosen_late_target_gamma_error_with_mean_reference_keV=target_rest*(
                                    float(doppler_factor(apparent_mean_beta,angle))/d_exit-1),
                                chosen_late_target_gamma_error_with_mode_reference_keV=target_rest*(
                                    float(doppler_factor(apparent_mode_beta,angle))/d_exit-1)))
            modes.append(mode)
    assert order_error < 1e-9

    # Independent proper-time / photon-beaming / lab-noise generator checks
    # whole-line means. It does not estimate a mode by a histogram maximum.
    rng=np.random.default_rng(131434)
    mc=[]
    generated=700000
    for e0,tau in CONTROLS:
        times=rng.exponential(tau,generated)
        beta=CHOSEN_BETA_IN+(TRUE_BETA_EXIT-CHOSEN_BETA_IN)*np.minimum(
            times/CHOSEN_PROPER_CROSSING_PS,1)
        angle=150.0
        d=doppler_factor(beta,angle)
        weight=1/d**2
        measured=e0/d+rng.normal(0,LAB_GAUSSIAN_SIGMA_KEV,generated)
        observed=float(weight @ measured/weight.sum())
        expected=mean_lab(e0,tau,angle)
        se=float(np.sqrt(np.sum(weight**2*(measured-observed)**2))/weight.sum())
        assert abs(observed-expected) < 5*se
        mc.append(dict(control_e0_keV=e0,tau_ps=tau,weighted_mean_keV=observed,
                       analytic_mean_keV=expected,MC_mean_SE_keV=se))
    # Long lifetime removes the finite-history offset. Equal entry/exit speed
    # makes both estimators the same regardless of lifetime.
    long_mean=mean_lab(1375.80,1e8,150)
    late=1375.80/float(doppler_factor(TRUE_BETA_EXIT,150))
    assert abs(long_mean-late)<1e-7
    _,d,w=kernel(0.070,150,beta_exit=CHOSEN_BETA_IN)
    assert np.max(np.abs(d-d[-1]))<1e-12
    assert abs(float(w @ (1375.80/d))-1375.80/d[-1])<1e-10
    return dict(schema_version=1,kind='synthetic long-control velocity estimator/history',
                source_context='CM21-15/16 control scales; actual calibration estimator not attested',
                chosen_parameters=dict(beta_in=CHOSEN_BETA_IN,beta_exit=TRUE_BETA_EXIT,
                                       proper_crossing_ps=CHOSEN_PROPER_CROSSING_PS,
                                       point_angles_deg=list(ANGLES),no_feeding=True,
                                       Gaussian_lab_sigma_keV=LAB_GAUSSIAN_SIGMA_KEV,
                                       whole_line_mean_vs_peak_mode=True,
                                       independent_MC_seed=131434,MC_generated_per_control=generated),
                controls=results,independent_MC=mc,
                verification=dict(quadrature128_256_mean_max_difference_keV=order_error,
                                  finite_history_late_speed_recovery_passed=True,
                                  independent_propertime_mean_MC_passed=True,
                                  mode_analytic_score_and_coarse_grid_passed=True,
                                  long_tau_and_equal_speed_limits_passed=True,all_passed=True),
                boundaries=['The.13ps is a chosen proper duration, not a relabeling of the source crossing-time estimate.',
                            'Rest-frame isotropic photons, fixed point angles and linear proper slowing are chosen.',
                            'Whole-line mean and density mode are different estimators; neither is asserted to be the source fitted peak center.',
                            'Mode/mean values depend on response, ROI and selection; actual source objectives/windows are unknown.',
                            'Correct-history inversion assumes the trajectory and control lifetime; it does not independently measure entryhistory.',
                            'The late-target2396.1keV reference test is chosen, not a20Ocalibration shift or discrepancy explanation.',
                            'Different nuclei/materials/charge states need actual paths/stopping/beta and joint calibration covariance.'])


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    result=calculate()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'verification':result['verification'],'controls':result['controls'],'MC':result['independent_MC']}))


if __name__=='__main__':
    main()
