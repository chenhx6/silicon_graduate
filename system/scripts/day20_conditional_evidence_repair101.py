#!/usr/bin/env python3
"""Declared mathematical counterexamples; no original experimental CI or fit.

Reads the literal Singh ledger and Petrache PDF to check provenance, units,
and the limits of common-scale, mixing, and tensor arguments. Writes only a
new result file. Historical results are never rewritten.
"""
from pathlib import Path
import argparse
import hashlib
import json
import math
import numpy as np
import pymupdf
from scipy.constants import alpha, c, electron_volt, hbar


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    run = root / 'outputs/learning-daily/20261022-DAY20-be2-qt-deformation-systematics-run-02'
    ledger_path = run / 'singh-table-ledger-001.json'
    ledger = json.loads(ledger_path.read_text())
    checks = []

    def check(name, condition):
        checks.append({'name': name, 'passed': bool(condition)})
        if not condition:
            raise AssertionError(name)

    # E2 radiation law in SI with B quoted in e^2 b^2, where 1 b=1e-28 m^2.
    energy = 1e6 * electron_volt
    rate = (8*math.pi*3/(2*15**2) / hbar
            * (energy/(hbar*c))**5 * (alpha*hbar*c) * 1e-56)
    check('SI E2 rate for 1MeV and 1e2b2 is about 12.25 per ps',
          math.isclose(rate*1e-12, 12.25, rel_tol=.002))
    # Compare with the old synthesis value; this is a unit error, not a new CI.
    old_rate_ps = .012252
    check('old synthesis rate constant was smaller by about 1000',
          math.isclose(rate*1e-12/old_rate_ps, 1000, rel_tol=.002))

    y = np.array([7.3, 7.4, 6.8, 7.3])
    sigma = np.array([.4, .3, .3, 1.0])
    w = sigma**-2
    L = np.r_[w[:2]/sum(w[:2]), -w[2:]/sum(w[2:])]
    difference = float(L@y)
    scale_sigma = .075  # chosen moment-scale nuisance, NOT measured stopping.
    covariance = scale_sigma**2 * np.outer(y, y)
    residual_variance = float(L@covariance@L)
    check('common multiplicative scale leaves nonzero difference variance',
          residual_variance > 0 and np.isclose(residual_variance,
                                             scale_sigma**2*difference**2))
    check('additive common offset cancels in normalized difference',
          abs(sum(L)) < 1e-14)
    # Correlation by group is an alternative declared response, not a new fit.
    groups = np.array([[y[0], y[1], 0, 0], [0, 0, y[2], y[3]]])
    group_variance = float(L@(scale_sigma**2 * groups.T@groups)@L)
    check('same marginal scales with separate campaigns give different result',
          group_variance > residual_variance*100)
    # Exact common multiplier cancels in ratios; absolute difference scales.
    ratios = [(a*y[0])/(a*y[2]) for a in [.85, 1, 1.15]]
    check('exact common scale cancels in ratio', np.allclose(ratios, y[0]/y[2]))

    # Two different internal mechanisms yield the same one observed amplitude.
    q_initial, q_observed = 5.675, 5.096
    angle = math.acos(q_observed/q_initial)
    rotation = np.array([[math.cos(angle), -math.sin(angle)],
                         [math.sin(angle), math.cos(angle)]])
    transition = rotation @ (np.eye(2)*q_initial)
    shrink = np.eye(2)*q_observed
    check('fixed intrinsic amplitude and scalar shrinkage share one entry',
          np.isclose(transition[0, 0], shrink[0, 0]))
    check('the other transition distinguishes those declared models',
          abs(transition[1, 0]) > 0 and shrink[1, 0] == 0)
    check('mixing preserves complete Frobenius norm',
          np.isclose(np.sum(transition**2), 2*q_initial**2))

    # Cubic shape invariant is not a generic diagonal matrix element.
    gamma = math.pi/6
    q20 = math.cos(gamma)
    q22 = math.sin(gamma)/math.sqrt(2)
    # For a declared |I=2,K=0> rotational basis state, Delta K=2 terms
    # have zero diagonal expectation; Qs=-2/7 Q20 remains finite.
    qs_basis = -2/7*q20
    check('zero cubic invariant need not zero a diagonal moment',
          abs(math.cos(3*gamma)) < 1e-14 and abs(qs_basis) > .2)

    # Preserve table sample roles: alternative fits/external rows aren't peers.
    pe = root / 'raw/papers/1998_Petrache et al_Lifetime measurements of highly deformed bands in 1 3 4 , 1 3 5 Nd and 131 Ce.pdf'
    with pymupdf.open(pe) as doc:
        page3, page4, page5 = [doc[p].get_text() for p in [2, 3, 4]]
    check('Petrache raw bytes match prior actual-read identity',
          hashlib.sha256(pe.read_bytes()).hexdigest() ==
          '9d2297ed085012d2f8633a5faecfa7020cbca96ac06cf2eb5e88d97a24b90e5f')
    check('raw table explicitly assumes no triaxiality', 'assuming no triaxiality' in page3)
    check('raw author says shrinkage could not be determined',
          'this shrink-' in page4 and 'ing effect could not be determined' in page4)
    check('Clark reference is 1996, not 1992',
          '3510 ~1996!' in page5)
    finite_counts = {key: sum(r['Qt']['kind'] == 'finite' for r in ledger[key]['rows'])
                     for key in ['case_Ce131', 'case_Pr133']}
    check('literal ledger contains four Ce and three Pr finite rows',
          finite_counts == {'case_Ce131': 4, 'case_Pr133': 3})
    result = {
        'checkpoint': '101', 'kind': 'declared mathematical controls and selected raw-page reinspection',
        'experimental_ci': False, 'original_producer_recovered': False,
        'controls': checks, 'all_controls_passed': all(r['passed'] for r in checks),
        'E2_rate_ps_per_MeV5_e2b2': rate*1e-12,
        'covariance_design': {'chosen_moment_scale_sigma': scale_sigma,
                              'Ce_minus_Nd_eb': difference,
                              'common_scale_residual_variance_eb2': residual_variance,
                              'separate_campaign_variance_eb2': group_variance,
                              'boundary': '132Ce is external Ref6; shared response/Cov unknown; neither design is an experimental covariance'},
        'mixing_counterexample': {'chosen_amplitudes_eb': [q_initial, q_observed],
                                 'constructed_angle_deg': math.degrees(angle),
                                 'unobserved_companion_amplitude_eb': float(transition[1, 0]),
                                 'boundary': 'No angle or mechanism extracted from Babra data'},
        'tensor_counterexample': {'gamma_deg': 30, 'q20': q20, 'q22': q22,
                                  'basis_state_Qs': qs_basis,
                                  'boundary': 'Declared rotational basis state, not a solved nuclear Hamiltonian or actual Ce wavefunction'},
        'source_locators': ['Petrache1998 PDF3/R12 TableI; PDF4/R13 method limitation; PDF5/R14 Ref6',
                            'Singh2016 PDF5 Table1 and PDF8 Table2, typed ledger001'],
        'finite_counts': finite_counts,
        'input_sha256': hashlib.sha256(ledger_path.read_bytes()).hexdigest(),
        'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    args.output.write_text(json.dumps(result, indent=2, ensure_ascii=False)+'\n')
    print(json.dumps({'controls': len(checks), 'result': str(args.output),
                      'rate_ps': rate*1e-12, 'common_residual_variance': residual_variance,
                      'separate_campaign_variance': group_variance}))


if __name__ == '__main__':
    main()
