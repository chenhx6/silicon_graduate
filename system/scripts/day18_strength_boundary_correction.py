#!/usr/bin/env python3
"""Forward arithmetic and counterexamples; never an experimental fit or ICC lookup."""
import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    checks = []

    def check(name, passed, **evidence):
        checks.append(dict(name=name, passed=bool(passed), **evidence))

    run = Path('outputs/learning-daily/20261020-DAY18-dsam-lifetime-transition-strength-run-01')
    old = json.loads((run / 'mu08-icc-m1-result-075.json').read_text())
    records = []
    for r in old['records']:
        b = r['branching'] / (r['tau_ps'] * 1.758e-8 * r['energy_keV']**3)
        # This is an algebraic residual, NOT an independently supplied alpha.
        records.append(dict(energy_keV=r['energy_keV'], gamma_only_B=b,
                            residual_factor=b/r['printed_bm1']-1))
    ordered = sorted(records, key=lambda r: r['energy_keV'])
    negative = [r for r in ordered if r['residual_factor'] < 0]
    rises = [(a['energy_keV'], b['energy_keV']) for a, b in zip(ordered, ordered[1:])
             if b['residual_factor'] > a['residual_factor']]
    check('old residuals are not nonnegative atomic coefficients', len(negative) > 0,
          negative_energies=[r['energy_keV'] for r in negative])
    check('old strict monotonicity claim fails', len(rises) > 0, increasing_pairs=rises)
    # For photon-normalized intensities r_i and a complete inventory:
    # p_gamma_i=r_i/sum_j[r_j*(1+alpha_j)], a COMMON parent denominator.
    r = (Fraction(93, 100), Fraction(7, 100))
    alpha = (Fraction(1, 5), Fraction(1, 100))  # self-chosen design, not Nd atomic data
    denom = sum(x*(1+a) for x, a in zip(r, alpha))
    photons = [x/denom for x in r]
    total = sum(p*(1+a) for p, a in zip(photons, alpha))
    check('photon-normalized forward inventory conserves total probability', total == 1)
    check('linewise division differs from common parent normalization', photons[0] != r[0]/(1+alpha[0]))
    # A total branch b_i instead gives p_gamma_i=b_i/(1+alpha_i).
    check('two branch definitions differ with identical printed fractions',
          photons[1] != r[1]/(1+alpha[1]))

    unit = lambda a: (3/5)**2*(1.2*a**(1/3))**4/(4*math.pi)*1e-4
    w136, w165 = unit(136), unit(165)
    b1 = [Fraction(26,100), Fraction(8,100), Fraction(14,100), Fraction(11,100)]
    b2 = [Fraction(51,100), Fraction(44,100), Fraction(4,100), Fraction(5,100)]
    ratio = [y/x for x,y in zip(b1,b2)]
    double = ratio[1]/ratio[2]
    check('same-A exact ratio survives unit conversion', double == Fraction(77,4))
    check('within-Band2 printed central drop is eleven', b2[1]/b2[2] == 11)
    check('9.6 W.u. is not the one-W.u. reference', float(b2[2])/w136 > 9)

    def cg2(i, k):
        return 3*(i+k-1)*(i+k)*(i-k-1)*(i-k)/(2*i*(i-1)*(2*i-1)*(2*i+1))

    i = Fraction(27,2)
    c_low, c_high = cg2(i,Fraction(1,2)), cg2(i,Fraction(11,2))
    check('finite-spin rotor CG factors from analytic expression',
          c_low == Fraction(26,75) and c_high == Fraction(76,325))
    q = lambda c: math.sqrt(16*math.pi/5*0.1723/float(c))
    q_low, q_high = q(c_low), q(c_high)
    q_residual = q_low/2.28-1
    const_effect = math.sqrt(1.225/1.224)-1
    check('131Ce remaining residual exceeds rate-constant rounding', abs(q_residual) > 30*const_effect,
          q_low=q_low, printed=2.28, relative_residual=q_residual, constant_effect=const_effect)
    check('predicted geometry ratio does not equal printed ratio',
          abs(q_high/q_low-2.72/2.28) > .02)

    # General axial strong-coupling relation uses Q0, NOT an arbitrary printed Qt.
    # R=(12/5)*(D0/Q0)^2*C1/C2, so D0=Q0*sqrt((5/12)*R*C2/C1).
    c1, c2 = Fraction(1,2), Fraction(3,8)
    check('5/16 is conditional fixed-K high-spin limit', Fraction(5,12)*c2/c1 == Fraction(5,16))
    # This is a design point; no 78Br measured Q0 or digitized Fig5 values supplied.
    d0 = 200*math.sqrt(5/16*1e-7)
    check('dipole scale doubles when self-chosen Q0 doubles',
          abs(400*math.sqrt(5/16*1e-7)/d0-2) < 1e-14)
    # B(M1) and B(E2) carry different units: naked inequality cannot classify modes.
    checks_ok = all(c['passed'] for c in checks)
    result = dict(kind='day18-boundary-correction-078', valid=checks_ok, checks=checks,
                  old_results_superseded=['062','075','076','077'],
                  residuals_not_atomic_ICC=ordered,
                  units=dict(E2_WU_136_e2b2=w136,E2_WU_165_e2b2=w165),
                  exact_double_ratio=str(double),
                  rotor=dict(Q_Khalf=q_low,Q_K11half=q_high,relative_residual=q_residual),
                  design_only_D0_efm=d0,
                  interpretation='no experimental CI, unique producer, atomic coefficients, or mode/shape identification',
                  script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps(dict(valid=checks_ok, checks=len(checks), output=str(args.output))))
    return 0 if checks_ok else 1


if __name__ == '__main__':
    raise SystemExit(main())
