#!/usr/bin/env python3
"""Declared observation-map invariance when a Curie offset is allowed.

No experimental counts, calibration prior, original fit or CI is inferred.
The source admits omitted temperature-independent terms; their real magnitude
is NOT supplied here. Expected two-detector curves are constructed, not sampled.
"""
from pathlib import Path
import argparse
import hashlib
import json
import math
import numpy as np
from scipy.constants import Boltzmann, hbar, physical_constants


MU_N = physical_constants['nuclear magneton'][0]
MU_B = physical_constants['Bohr magneton'][0]
J_ELECTRON = 2.5
GJ_ELECTRON = 6/7


def observation(g_n, b0_T, constant_offset, temperatures, fields, times):
    curie_K = GJ_ELECTRON*(J_ELECTRON+1)/3 * MU_B*b0_T/Boltzmann
    enhancement = 1+constant_offset+curie_K/temperatures
    omega = MU_N/hbar * g_n * enhancement[:, None] * fields[None, :]
    # Chosen constant electronic correlation time, NOT a Kondo fit.
    tau_electron_s = 1e-13
    relaxation_rate = (2*(MU_N/hbar)**2*(J_ELECTRON+1)/J_ELECTRON
                       * (g_n*b0_T)**2 * tau_electron_s)
    asymmetry = (.15*np.exp(-relaxation_rate*times)[None, None, :]
                 * np.cos(2*(.3-omega[:, :, None]*times)))
    # Choose a separate nuclear DECAY half-life, not alignment relaxation.
    unpolarized = 1000*np.exp(-math.log(2)*times/2e-6)
    expected_counts = unpolarized[None, None, None, :]*(1+np.array([-1, 1])[None, None, :, None]*asymmetry[:, :, None, :])
    return {'curie_K': curie_K, 'enhancement': enhancement, 'omega': omega,
            'relaxation_rate': relaxation_rate, 'asymmetry': asymmetry,
            'expected_counts': expected_counts,
            'fast_fluctuation_parameter': abs(g_n*MU_N*b0_T/(hbar*J_ELECTRON))*tau_electron_s}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    temperatures = np.array([298., 504., 900.])
    # Chosen field grid; this is NOT pooling two historical experiments.
    fields = np.array([-3.2, -1.98, 1.98, 3.2])
    times = np.linspace(0, 4e-6, 2001)
    g_n, b0, k0 = -.180, 178., 0.
    base = observation(g_n, b0, k0, temperatures, fields, times)
    checks = []
    cases = []

    def check(name, value):
        checks.append({'name': name, 'passed': bool(value)})
        if not value:
            raise AssertionError(name)

    check('chosen field enhancement positive', np.all(base['enhancement'] > 0))
    check('chosen fast-fluctuation condition holds', base['fast_fluctuation_parameter'] < 1e-3)
    check('chosen expected counts remain positive', np.all(base['expected_counts'] > 0))
    for scale in [.998, 1.002]:
        changed = observation(scale*g_n, b0/scale, (1+k0)/scale-1,
                              temperatures, fields, times)
        omega_residual = float(np.max(abs(base['omega']-changed['omega'])))
        counts_residual = float(np.max(abs(base['expected_counts']-changed['expected_counts'])))
        check(str(scale)+' frequency invariant at every T and field sign',
              np.allclose(base['omega'], changed['omega'], rtol=2e-15, atol=1e-7))
        check(str(scale)+' nuclear relaxation rate invariant',
              np.isclose(base['relaxation_rate'], changed['relaxation_rate'], rtol=2e-15))
        check(str(scale)+' all constructed detector time curves invariant',
              counts_residual < 1e-10)
        check(str(scale)+' zero-offset restriction breaks the degeneracy',
              np.max(abs(observation(scale*g_n, b0/scale, 0, temperatures, fields, times)['omega']-base['omega'])) > 1e3)
        cases.append({'chosen_g_scale': scale, 'g_N': scale*g_n,
                      'B0_T': b0/scale, 'constant_offset': (1+k0)/scale-1,
                      'max_abs_omega_residual_rad_s': omega_residual,
                      'max_abs_expected_bin_residual': counts_residual})
    result = {
        'checkpoint': '108', 'kind': 'declared analytic observation-map counterexample',
        'experimental_CI': False, 'original_producer': False, 'event_sampling': False,
        'exact_transformation': 'gN->a*gN, B0->B0/a, 1+K0->(1+K0)/a',
        'identified_combinations': ['gN*(1+K0)', 'gN*B0'],
        'observation_model': 'beta=1+K0+C/T, C=gJ(J+1)muB B0/(3kB); omega proportional gN beta Bext; alignment rate proportional (gN B0)^2 tau_electron',
        'chosen_parameters': {'g_N': g_n, 'B0_T': b0, 'K0': k0,
                              'electronic_J': J_ELECTRON, 'electronic_gJ': GJ_ELECTRON,
                              'electronic_tau_s': 1e-13, 'nuclear_decay_half_life_s': 2e-6,
                              'temperatures_K': temperatures.tolist(), 'fields_T': fields.tolist(),
                              'time_range_s': [0, 4e-6], 'time_points': len(times),
                              'phase_rad': .3, 'asymmetry_amplitude': .15,
                              'unpolarized_initial_expected_count': 1000},
        'baseline_alignment_tau_s': 1/base['relaxation_rate'],
        'fast_fluctuation_parameter': base['fast_fluctuation_parameter'],
        'cases': cases, 'controls': checks,
        'all_controls_passed': all(c['passed'] for c in checks),
        'boundaries': ['Small offsets and scale changes are chosen witnesses, not measured systematics or uncertainty bounds.',
                       'The model is simplified and constructed; no actual detector response, count likelihood, g-factor fit or nuclear CI recovered.',
                       'Independent information on constant shifts, absolute field enhancement or nuclear g can break the invariance.',
                       'Authors use the zero-offset Curie restriction; this counterexample does not declare their reported results invalid.',
                       'Two-detector expected curves are deterministic functions, not Monte Carlo timing-spectrum validation.'],
        'source_locator': 'BA81-D20-2/4/6; Barth1981 printed813/814 and819',
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    args.output.write_text(json.dumps(result, indent=2, ensure_ascii=False)+'\n')
    print(json.dumps({'controls': len(checks), 'baseline_alignment_tau_s': result['baseline_alignment_tau_s'],
                      'cases': cases}))


if __name__ == '__main__':
    main()
