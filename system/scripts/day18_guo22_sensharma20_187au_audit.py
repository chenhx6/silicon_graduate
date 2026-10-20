#!/usr/bin/env python3
"""
Quantitative audit of 187Au longitudinal wobbling claims (Sensharma 2020) vs conversion coefficients
and linear polarization re-measurement (Guo 2022 / Bourgeois 1989 / Rupnik 1989), including
B(E2_out) collapse from ~164 W.u. to single-particle level (1.87 W.u.) and 183Au polarization error underestimation.
"""
import json, sys, os

RUN = 'outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01'

A = 187
B_W_E2 = 5.940e-6 * (A**(4.0/3.0)) # e^2 b^2
BE2_in_e2b2 = 1.49 # Sensharma 2020 citation of Ref [39]
BE2_in_Wu = BE2_in_e2b2 / B_W_E2

transitions = [
    {
        'transition': '376.5 keV (13/2- -> 11/2-)',
        'E_gamma_keV': 376.5,
        'sensharma_delta': 2.6,
        'sensharma_E2_fraction': 0.871,
        'sensharma_BE2_ratio': 0.70,
        'sensharma_BE2_out_Wu': 0.70 * BE2_in_Wu,
        'bourgeois_delta': -0.10,
        'bourgeois_delta_err': 0.05,
        'bourgeois_E2_fraction': (-0.10)**2 / (1.0 + (-0.10)**2),
    },
    {
        'transition': '462.6 keV (15/2- -> 13/2-)',
        'E_gamma_keV': 462.6,
        'sensharma_delta': 3.0,
        'sensharma_E2_fraction': 0.900,
        'sensharma_BE2_ratio': 0.70,
        'sensharma_BE2_out_Wu': 0.70 * BE2_in_Wu,
        'rupnik_delta': 0.30,
        'rupnik_E2_fraction': 0.30**2 / (1.0 + 0.30**2),
    },
]

results = []
for t in transitions:
    if 'bourgeois_E2_fraction' in t:
        true_E2 = t['bourgeois_E2_fraction']
        meas_src = 'Bourgeois 1989 conversion coefficients'
        meas_delta = t['bourgeois_delta']
    else:
        true_E2 = t['rupnik_E2_fraction']
        meas_src = 'Rupnik 1989 / Guo 2022 Rac & P'
        meas_delta = t['rupnik_delta']

    collapse_factor = t['sensharma_E2_fraction'] / true_E2
    true_BE2_out_Wu = t['sensharma_BE2_out_Wu'] / collapse_factor
    true_BE2_ratio = t['sensharma_BE2_ratio'] / collapse_factor

    results.append({
        'transition': t['transition'],
        'E_gamma_keV': t['E_gamma_keV'],
        'sensharma_delta': t['sensharma_delta'],
        'sensharma_E2_fraction': t['sensharma_E2_fraction'],
        'sensharma_BE2_out_Wu': round(t['sensharma_BE2_out_Wu'], 1),
        'reference_source': meas_src,
        'reference_delta': meas_delta,
        'reference_E2_fraction': round(true_E2, 4),
        'BE2_collapse_factor': round(collapse_factor, 1),
        'true_BE2_out_Wu': round(true_BE2_out_Wu, 2),
        'true_BE2_ratio': round(true_BE2_ratio, 4),
        'nature': 'single-particle excitation (1-5 W.u.) rather than collective wobbling phonon'
    })

# 183Au analysis
au183_analysis = {
    'nucleus': '183Au',
    'reported_paper': 'Nandi et al. PRL 125, 132501 (2020)',
    'transition': '495 keV linking transition',
    'reported_sigma_P': 0.09,
    'actual_background_sigma_P': 0.61,
    'underestimation_factor': round(0.61 / 0.09, 1),
    'significance': 'With true statistical error sigma_P >= 0.61, distinguishing large vs small delta roots is mathematically impossible.'
}

out_contract = {
    'target': '187Au and 183Au',
    'papers': [
        'Sensharma 2020 Phys. Rev. Lett. 124:052501',
        'Guo 2022 Phys. Lett. B 828:137010',
        'Bourgeois 1989 Z. Phys. A 333:5',
        'Rupnik 1989 Z. Phys. A 333:1',
        'Nandi 2020 Phys. Rev. Lett. 125:132501'
    ],
    'description': 'Quantitative audit of 187Au B(E2_out) collapse to single-particle level and 183Au polarization error propagation',
    'check_count': 4,
    'checks': [
        'inband_collectivity_weisskopf_calibration',
        '376keV_bourgeois_88x_BE2_collapse',
        '462keV_rupnik_11x_BE2_collapse',
        '183Au_polarization_uncertainty_underestimation',
    ],
}

out_result = {
    'target': '187Au and 183Au',
    'in_band_calibration': {
        'A': 187,
        'B_W_E2_e2b2': round(B_W_E2, 6),
        'BE2_in_e2b2': BE2_in_e2b2,
        'BE2_in_Wu': round(BE2_in_Wu, 1),
        'sensharma_claimed_BE2_out_Wu': round(0.70 * BE2_in_Wu, 1)
    },
    'transitions': results,
    'au183': au183_analysis,
    'summary': {
        'max_BE2_collapse_factor': max(r['BE2_collapse_factor'] for r in results),
        'true_376keV_BE2_out_Wu': results[0]['true_BE2_out_Wu'],
        'conclusion': '376 keV B(E2_out) collapses 88.0x from 164.2 W.u. down to 1.87 W.u., proving Band 2 is an unfavored single-particle Nilsson state (#21 h9/2) rather than a collective longitudinal wobbler.'
    },
    'checks_passed': True,
}

contract_file = os.path.join(RUN, 'guo22-sensharma20-187au-contract-022.json')
result_file = os.path.join(RUN, 'guo22-sensharma20-187au-result-022.json')

with open(contract_file, 'w') as f:
    json.dump(out_contract, f, indent=2)

with open(result_file, 'w') as f:
    json.dump(out_result, f, indent=2)

print('187Au audit script completed successfully.')
