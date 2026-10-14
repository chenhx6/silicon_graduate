#!/usr/bin/env python3
"""Synthetic DAY13 entry-gate, feeding and lifetime-shape design.

ZA23 motivates two resolved entry states and a feeder. These are chosen
parameters and expected density fits, not the source's events, transport,
Ex response, systematic budget, Neyman chi-square or confidence intervals.
Time is proper time in ps; photon recoil and angular alignment are omitted.
An isotropic rest-frame photon is conditioned on chosen lab point angles.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np
import scipy
from numpy.polynomial.legendre import leggauss
from scipy.integrate import quad
from scipy.optimize import minimize, minimize_scalar
from scipy.special import ndtr


E0_KEV = 2396.1
TAU2_PS = 0.070
TAU3_PS = 0.054
EX2_MEV = 4.071
EX3_MEV = 5.228
BR32 = 0.28
BETA_IN = 0.126
BETA_EXIT = 0.080
T_EXIT_PS = 0.4
SIGMA_KEV = 2.0
ANGLES_DEG = (130.0, 150.0, 170.0)


def gate_acceptance(mean, sigma, low, high):
    return float(ndtr((high - mean) / sigma) - ndtr((low - mean) / sigma))


def entry_fraction(population_ratio, sigma, half_width=0.2, offset=0.0):
    low, high = EX2_MEV + offset - half_width, EX2_MEV + offset + half_width
    direct = gate_acceptance(EX2_MEV, sigma, low, high)
    upper = gate_acceptance(EX3_MEV, sigma, low, high)
    f = population_ratio * BR32 * upper / (direct + population_ratio * BR32 * upper)
    return dict(population3_over_population2=population_ratio,
                chosen_Ex_sigma_MeV=sigma, gate_edges_MeV=[low, high],
                direct_entry_acceptance=direct, upper_entry_acceptance=upper,
                target_entry_feed_fraction=f)


def fed_density(t, tau2, tau3):
    if abs(tau2 - tau3) < 1e-8 * max(tau2, tau3):
        return t * np.exp(-t / tau2) / tau2**2
    return (np.exp(-t / tau2) - np.exp(-t / tau3)) / (tau2 - tau3)


def fed_survival(t, tau2, tau3):
    if abs(tau2 - tau3) < 1e-8 * max(tau2, tau3):
        return np.exp(-t / tau2) * (1 + t / tau2)
    return (tau2 * np.exp(-t / tau2) - tau3 * np.exp(-t / tau3)) / (tau2 - tau3)


def kernel(tau2, f, angle, order=128, tau3=TAU3_PS, beta_in=BETA_IN):
    nodes, weights = leggauss(order)
    times = T_EXIT_PS * (nodes + 1) / 2
    beta = beta_in + (BETA_EXIT - beta_in) * times / T_EXIT_PS
    cosine = math.cos(math.radians(angle))
    d_em = (1 - beta * cosine) / np.sqrt(1 - beta**2)
    d_exit = (1 - BETA_EXIT * cosine) / math.sqrt(1 - BETA_EXIT**2)
    time_density = (1 - f) * np.exp(-times / tau2) / tau2
    time_density += f * fed_density(times, tau2, tau3)
    tail = (1 - f) * math.exp(-T_EXIT_PS / tau2)
    tail += f * float(fed_survival(T_EXIT_PS, tau2, tau3))
    time_weights = np.r_[weights * T_EXIT_PS / 2 * time_density, tail]
    ratios = np.r_[d_exit / d_em, 1.0]
    angular_weights = np.r_[1 / d_em**2, 1 / d_exit**2]
    probabilities = time_weights * angular_weights
    return ratios, probabilities / probabilities.sum(), float(time_weights.sum())


def density(grid, e0, tau2, f, angle, order=128, beta_in=BETA_IN):
    ratios, weights, _ = kernel(tau2, f, angle, order, beta_in=beta_in)
    gaussian = np.exp(-0.5 * ((grid[:, None] - e0 * ratios) / SIGMA_KEV)**2)
    return gaussian @ weights / (math.sqrt(2 * math.pi) * SIGMA_KEV)


def moments(e0, tau2, f, angle):
    ratios, weights, _ = kernel(tau2, f, angle, order=256)
    centers = e0 * ratios
    mu = float(weights @ centers)
    var = SIGMA_KEV**2 + float(weights @ ((centers - mu)**2))
    return mu, var


def calculate():
    gate_cases = [entry_fraction(r, s) for s in (0.15, 0.25, 0.5, 0.75)
                  for r in (1.0, 10.0, 100.0)]
    gate_shift_cases = [entry_fraction(10.0, 0.5, offset=o) for o in (-0.1, 0.0, 0.1)]
    grid = np.linspace(E0_KEV - 180.0, E0_KEV + 25.0, 1641)
    fractions = (0.0, 0.05, 0.2, 0.5, 0.9, 1.0)
    fits = []
    norm_error = 0.0
    order_error = 0.0
    for f in fractions:
        truth = [density(grid, E0_KEV, TAU2_PS, f, a) for a in ANGLES_DEG]
        for a, p in zip(ANGLES_DEG, truth):
            norm_error = max(norm_error, abs(float(np.trapezoid(p, grid)) - 1))
            order_error = max(order_error, float(np.max(np.abs(
                p - density(grid, E0_KEV, TAU2_PS, f, a, order=256)))))

        def kl(tau, e0):
            terms = []
            for a, p in zip(ANGLES_DEG, truth):
                q = density(grid, e0, tau, 0.0, a)
                terms.append(float(np.trapezoid(p * (np.log(np.maximum(p, 1e-300))
                                                    - np.log(np.maximum(q, 1e-300))), grid)))
            return float(np.mean(terms))

        fixed = minimize_scalar(lambda t: kl(t, E0_KEV), bounds=(0.02, 0.25),
                                method='bounded', options={'xatol': 1e-10})
        starts = [(float(fixed.x), E0_KEV), (0.04, E0_KEV-2),
                  (0.18, E0_KEV+2), (0.24, E0_KEV+4)]
        profiles = [minimize(lambda x: kl(x[0], x[1]), start, method='L-BFGS-B',
                             bounds=[(0.02, 0.25), (E0_KEV - 5, E0_KEV + 5)],
                             options={'ftol': 1e-13, 'gtol': 1e-8, 'maxiter': 150})
                    for start in starts]
        assert fixed.success and any(x.success for x in profiles)
        profiled = min((x for x in profiles if x.success), key=lambda x: x.fun)
        assert profiled.fun <= fixed.fun + 1e-9
        fits.append(dict(target_entry_feed_fraction=f,
                         pre_photon_selection_mean_waiting_fs=1000*(TAU2_PS+f*TAU3_PS),
                         wrong_no_feeding_fixed_energy_tau_fs=1000*float(fixed.x),
                         wrong_no_feeding_fixed_energy_KL=max(0.0, float(fixed.fun)),
                         wrong_no_feeding_profiled_energy_tau_fs=1000*float(profiled.x[0]),
                         wrong_no_feeding_profiled_rest_energy_keV=float(profiled.x[1]),
                         wrong_no_feeding_profiled_KL=max(0.0, float(profiled.fun)),
                         multistart_results=[dict(start_tau_ps=s[0], start_energy_keV=s[1],
                                                  success=bool(x.success),
                                                  final_tau_ps=float(x.x[0]),
                                                  final_energy_keV=float(x.x[1]),
                                                  final_KL=float(x.fun))
                                             for s, x in zip(starts, profiles)]))

    # Independently generated cascade times and Gaussian photon measurements.
    rng = np.random.default_rng(131420)
    n = 600000
    f = 0.5
    fed = rng.random(n) < f
    times = rng.exponential(TAU2_PS, n) + fed * rng.exponential(TAU3_PS, n)
    mean_t = TAU2_PS + f * TAU3_PS
    sigma_t = math.sqrt(TAU2_PS**2 + f * (2 - f) * TAU3_PS**2)
    assert abs(float(times.mean()) - mean_t) < 5*sigma_t/math.sqrt(n)
    beta = np.where(times < T_EXIT_PS,
                    BETA_IN + (BETA_EXIT - BETA_IN)*times/T_EXIT_PS, BETA_EXIT)
    checks = []
    for a in ANGLES_DEG:
        cosine = math.cos(math.radians(a))
        d_em = (1-beta*cosine)/np.sqrt(1-beta**2)
        d_exit = (1-BETA_EXIT*cosine)/math.sqrt(1-BETA_EXIT**2)
        energy = E0_KEV*d_exit/d_em + rng.normal(0.0, SIGMA_KEV, n)
        w = 1/d_em**2
        mu_mc = float(w @ energy / w.sum())
        var_mc = float(w @ ((energy-mu_mc)**2)/w.sum())
        mu, var = moments(E0_KEV, TAU2_PS, f, a)
        se = float(np.sqrt(np.sum(w**2*(energy-mu_mc)**2))/w.sum())
        assert abs(mu_mc-mu) < 5*se and abs(var_mc/var-1) < 0.015
        # A point photon sample can have a different feed fraction from entry f.
        detected_f = float(np.sum(w[fed])/w.sum())
        checks.append(dict(angle_deg=a, analytic_mean_keV=mu, MC_mean_keV=mu_mc,
                           weighted_mean_SE_keV=se, analytic_variance_keV2=var,
                           MC_variance_keV2=var_mc,
                           MC_photon_conditioned_feed_fraction=detected_f))

    norm_equal = quad(lambda t: float(fed_density(t, TAU2_PS, TAU2_PS)),
                      0, np.inf, epsabs=1e-11)[0]
    surv = float(fed_survival(T_EXIT_PS, TAU2_PS, TAU3_PS))
    quad_surv = quad(lambda t: float(fed_density(t, TAU2_PS, TAU3_PS)),
                     T_EXIT_PS, np.inf, epsabs=1e-11)[0]
    assert abs(norm_equal-1) < 1e-10 and abs(surv-quad_surv) < 1e-10
    assert norm_error < 1e-9 and order_error < 1e-9
    assert abs(fits[0]['wrong_no_feeding_profiled_energy_tau_fs']-70) < 0.001
    assert fits[0]['wrong_no_feeding_profiled_KL'] < 1e-12
    static1 = density(grid, E0_KEV, 0.07, 0.0, 150, beta_in=BETA_EXIT)
    static2 = density(grid, E0_KEV, 0.20, 1.0, 150, beta_in=BETA_EXIT)
    assert np.max(np.abs(static1-static2)) < 1e-12
    ratios, _, mass = kernel(TAU2_PS, 1.0, 150, order=256)
    assert np.all((ratios > 0) & (ratios <= 1)) and abs(mass-1) < 1e-11

    return dict(schema_version=1, kind='synthetic entry-gate/feeding expected-shape design',
                source_inspiration='ZA23-2/3/4/5; not either experiment reanalysis',
                chosen_parameters=dict(rest_gamma_keV=E0_KEV, tau2_ps=TAU2_PS,
                                       tau3_ps=TAU3_PS, EX2_MeV=EX2_MEV, EX3_MeV=EX3_MEV,
                                       BR32=BR32, beta_in=BETA_IN, beta_exit=BETA_EXIT,
                                       slowing_proper_duration_ps=T_EXIT_PS,
                                       gaussian_corrected_energy_sigma_keV=SIGMA_KEV,
                                       point_angles_deg=list(ANGLES_DEG)),
                entry_gate_cases=gate_cases, shifted_gate_cases=gate_shift_cases,
                synthetic_misspecified_fits=fits, independent_MC_checks=checks,
                verification=dict(normalization_max_error=norm_error,
                                  quad128_256_density_max_difference=order_error,
                                  equal_tau_Erlang_limit_passed=True,
                                  cascade_survival_independent_quad_error=abs(surv-quad_surv),
                                  propertime_MC_mean_passed=True,
                                  importance_MC_energy_moments_passed=True,
                                  no_feeding_fit_truth_passed=True,
                                  no_loss_tau_and_feed_shape_independence_passed=True,
                                  all_passed=True),
                boundaries=['Ex resolutions, gate edges, populations, slowing law and detector sigma are chosen.',
                            '70/54fs and branch .28 inspire scales, not an experimental refit.',
                            'Pre-photon entry feed fraction differs from conditional detected fraction.',
                            'Expected KL and pseudo-true tau are not data chi-square, confidence or pooled lifetimes.',
                            'Photon recoil, other feeding, actual gold stopping, correlations and alignment are omitted.',
                            'A mean-waiting bound is not a bound on fitted one-exponential tau.',
                            'Four optimization starts check local solutions; not a theorem of global uniqueness.'],
                library_versions=dict(numpy=np.__version__, scipy=scipy.__version__))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    result = calculate()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'output': str(args.output), 'verification': result['verification'],
                      'synthetic_misspecified_fits': result['synthetic_misspecified_fits']}))


if __name__ == '__main__':
    main()
