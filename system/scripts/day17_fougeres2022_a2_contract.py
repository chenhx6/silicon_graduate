#!/usr/bin/env python3
"""Symbolic contract for the actual thesis A.2 equal-width background windows."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
from fractions import Fraction as F

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / 'outputs/learning-daily/20261019-DAY17-linear-polarization-paq-compton-run-01'


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    cp = RUN / 'fougeres2022-thesis-a2-exercise-contract.json'
    c = json.loads(cp.read_text())
    assert sha(ROOT / c['pdf']) == c['pdf_sha256']
    left, signal, upper = c['windows_keV']
    hvalue = signal[1] - signal[0]
    assert left[1] == signal[0] and signal[1] == upper[0]
    assert left[1]-left[0] == upper[1]-upper[0] == hvalue == 30
    # Integrate x=h*t: coefficients multiply b0*h, b1*h**2, b2*h**3.
    intervals = [(F(-1, 2), F(1, 2)), (F(-3, 2), F(-1, 2)), (F(1, 2), F(3, 2))]
    integrals = [[(hi**(k+1)-lo**(k+1))/(k+1) for k in range(3)] for lo, hi in intervals]
    residual = [integrals[0][k]-(integrals[1][k]+integrals[2][k])/2 for k in range(3)]
    assert residual == [F(0), F(0), F(-1)]
    operator = [F(1), F(-1, 2), F(-1, 2)]
    cov_coeff = {'V_S': operator[0]**2, 'V_L': operator[1]**2, 'V_U': operator[2]**2,
                 'C_SL': 2*operator[0]*operator[1], 'C_SU': 2*operator[0]*operator[2],
                 'C_LU': 2*operator[1]*operator[2]}
    assert list(cov_coeff.values()) == [F(1), F(1,4), F(1,4), F(-1), F(-1), F(1,2)]
    out = {'at': datetime.now(timezone.utc).isoformat(), 'script_sha256': sha(Path(__file__)),
           'contract_sha256': sha(cp), 'actual_windows_keV': c['windows_keV'],
           'order_for_operator': ['signal', 'lower side', 'upper side'],
           'operator': [[str(v) for v in operator]],
           'general_variance_coefficients': {k: str(v) for k, v in cov_coeff.items()},
           'general_variance': 'V_S + V_L/4 + V_U/4 - C_SL - C_SU + C_LU/2',
           'independent_primitive_Poisson_special_case': 'S + L/4 + U/4',
           'background_density_units': 'counts per keV per chosen ejectile bin',
           'density': 'b0+b1*x+b2*x**2',
           'integral_coefficient_basis': ['b0*h', 'b1*h**2', 'b2*h**3'],
           'background_integral_coefficients': [[str(v) for v in row] for row in integrals],
           'background_residual_coefficients': [str(v) for v in residual],
           'background_residual_symbolic': '-b2*h**3',
           'at_actual_width_keV': f'-{hvalue**3}*b2',
           'signal_contribution': 'A_signal - (A_lower + A_upper)/2; leakage is response dependent',
           'actual_counts_covariance_and_curvature_not_provided': True,
           'no_new_experimental_yield_tau_branch_or_CI': True, 'ok': True}
    (RUN / 'fougeres2022-thesis-a2-exercise-result.json').write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
