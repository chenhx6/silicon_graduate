#!/usr/bin/env python3
"""Synthetic RF-phase/rigidity discrete aliases for DAY13 velocity learning.

Only for a hypothetical measurement retaining RF phase and losing the period
index. Actual VAMOS unwrapping is not evaluated. Chosen constant flight speed,
mass=A*u approximation, path, errors and priors; no material transport.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np


C_M_NS = 0.299792458
MU_MEV = 931.49410242
RIGIDITY_FACTOR = 3.107
RF_PERIOD_NS = 102.0


def beta_from_rigidity(brho, a, q):
    bg = brho * q / (RIGIDITY_FACTOR * a)
    return bg / math.sqrt(1 + bg * bg)


def phase_difference(predicted, observed, period=RF_PERIOD_NS):
    return (predicted - observed + period/2) % period - period/2


def kinetic_energy(a, beta):
    return a * MU_MEV * (1/math.sqrt(1-beta*beta) - 1)


def calculate():
    a1, q1, a2, q2 = 19, 8, 20, 6
    beta1 = 0.1
    brho = RIGIDITY_FACTOR * a1/q1 * beta1/math.sqrt(1-beta1**2)
    beta2 = beta_from_rigidity(brho, a2, q2)
    # Deliberately choose a path that makes two flight times differ by one RF period.
    path = C_M_NS * RF_PERIOD_NS / (1/beta2 - 1/beta1)
    time1, time2 = path/(C_M_NS*beta1), path/(C_M_NS*beta2)
    phase = time1 % RF_PERIOD_NS
    energy1, energy2 = kinetic_energy(a1, beta1), kinetic_energy(a2, beta2)
    sigma_phase, sigma_path, sigma_brho, sigma_energy = 1.0, 0.01, 0.001, 2.0
    candidates = []
    for a in range(17, 22):
        for q in range(5, 9):
            b = beta_from_rigidity(brho, a, q)
            t = path/(C_M_NS*b)
            residual = phase_difference(t, phase)
            # Integrate local path and rigidity errors into phase prediction.
            sigma_t = math.sqrt(sigma_phase**2 + (t*sigma_path/path)**2
                                + (t*(1-b*b)*sigma_brho/brho)**2)
            e = kinetic_energy(a, b)
            candidates.append(dict(A=a, ionic_q=q, beta=b, flight_ns=t,
                                   period_index=int(math.floor(t/RF_PERIOD_NS)),
                                   predicted_phase_ns=t % RF_PERIOD_NS,
                                   wrapped_phase_residual_ns=residual,
                                   effective_phase_sigma_ns=sigma_t,
                                   phase_only_chi2=(residual/sigma_t)**2,
                                   energy_MeV=e,
                                   phase_plus_independent_energy_chi2=(residual/sigma_t)**2
                                       + ((e-energy1)/sigma_energy)**2))
    for key, output in [('phase_only_chi2', 'phase_only_equal_prior_weight'),
                        ('phase_plus_independent_energy_chi2', 'with_energy_equal_prior_weight')]:
        scores = np.array([x[key] for x in candidates])
        w = np.exp(-0.5*(scores-scores.min()))
        w /= w.sum()
        for row, value in zip(candidates, w):
            row[output] = float(value)
    pair = [x for x in candidates if (x['A'], x['ionic_q']) in [(a1,q1),(a2,q2)]]
    assert len(pair) == 2
    assert abs(time2-time1-RF_PERIOD_NS) < 1e-10
    assert abs(phase_difference(time2, phase)) < 1e-10
    assert all(abs(x['phase_only_chi2']) < 1e-20 for x in pair)
    assert pair[0]['with_energy_equal_prior_weight'] > 0.999999
    assert abs(beta_from_rigidity(brho, a1, q1)-beta1) < 1e-15
    assert abs(phase_difference(phase+2*RF_PERIOD_NS, phase)) < 1e-12

    # Local continuous uncertainty within the correct period branch.
    beta_sigma = beta1*math.sqrt((sigma_path/path)**2+(sigma_phase/time1)**2)
    rng = np.random.default_rng(131402)
    n = 500000
    path_mc = path + rng.normal(0, sigma_path, n)
    time_mc = time1 + rng.normal(0, sigma_phase, n)
    beta_mc = path_mc/(C_M_NS*time_mc)
    sd_mc = float(np.std(beta_mc))
    assert abs(sd_mc/beta_sigma-1) < 0.006
    # A source-inspired photon illustrates correction sensitivity to a discrete branch.
    e0 = 1375.80
    theta = math.radians(150.0)
    d1 = (1-beta1*math.cos(theta))/math.sqrt(1-beta1**2)
    d2 = (1-beta2*math.cos(theta))/math.sqrt(1-beta2**2)
    lab = e0/d1
    assert abs(lab*d1-e0) < 1e-10
    d1_jac = d1*(beta1/(1-beta1**2)-math.cos(theta)/(1-beta1*math.cos(theta)))
    eps = 1e-6
    def d(b):
        return (1-b*math.cos(theta))/math.sqrt(1-b*b)
    fd = (d(beta1+eps)-d(beta1-eps))/(2*eps)
    assert abs(fd-d1_jac) < 1e-8

    return dict(schema_version=1, kind='synthetic RF phase/rigidity global alias design',
                source_inspiration='CM21-1/15 and AS21-9/10; not a source unwrapping failure',
                chosen_parameters=dict(period_ns=RF_PERIOD_NS, path_m=path,
                                       brho_Tm=brho, mass_proxy='A*u; not actual isotope masses',
                                       Z=8, A_candidates=list(range(17,22)),
                                       q_candidates=list(range(5,9)), priors='equal per enumerated A,q',
                                       sigma_phase_ns=sigma_phase, sigma_path_m=sigma_path,
                                       sigma_brho_Tm=sigma_brho, independent_energy_sigma_MeV=sigma_energy),
                exact_pair=pair,
                all_candidates_sorted_by_phase=sorted(candidates,key=lambda x:x['phase_only_chi2']),
                local_precision=dict(conditional_TOF_beta_sigma=beta_sigma,
                                     independent_MC_beta_sigma=sd_mc,
                                     alias_beta_separation=abs(beta1-beta2),
                                     separation_over_local_beta_sigma=abs(beta1-beta2)/beta_sigma),
                photon_illustration=dict(chosen_rest_gamma_keV=e0, chosen_lab_angle_deg=150,
                                         generated_lab_keV=lab, correct_branch_rest_keV=lab*d1,
                                         alternate_branch_corrected_keV=lab*d2,
                                         alternate_branch_residual_keV=lab*d2-e0),
                verification=dict(period_difference_exact_passed=True,
                                  rigidity_and_phase_pair_closure_passed=True,
                                  independent_energy_removes_alias_in_chosen_model=True,
                                  modulo_period_invariance_passed=True,
                                  conditional_MC_variance_passed=True,
                                  exact_photon_roundtrip_passed=True,
                                  derivative_finite_difference_passed=True,
                                  all_passed=True),
                boundaries=['Only applies if an RF period index is absent; raw timestamps may resolve it.',
                            'Mass proxy, constant speed/path and noise/priors are chosen, not VAMOS configuration.',
                            'Rigidity speed conditional on the same isotope/charge assignment is not an independent validator.',
                            'Independent energy is assumed independently calibrated here; real material/clock covariance is omitted.',
                            'Known gamma identity can constrain a branch, but unknown rest energy cannot act as an independent clock.'],
                numpy_version=np.__version__)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    result = calculate()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'output':str(args.output), 'verification':result['verification'],
                      'pair':result['exact_pair'], 'local_precision':result['local_precision'],
                      'photon':result['photon_illustration']}))


if __name__ == '__main__':
    main()
