#!/usr/bin/env python3
"""Exact synthetic controls for normalized GCD weights; no experimental fit."""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path


def norm(weights):
    weights = list(map(F, weights))
    assert all(w >= 0 for w in weights) and sum(weights) > 0
    return [w / sum(weights) for w in weights]


def dot(a, b):
    assert len(a) == len(b)
    return sum(x * y for x, y in zip(a, b))


def calculate():
    a, b = norm([8, 2]), norm([2, 8])
    d = [x - y for x, y in zip(a, b)]
    shifts = [F(30), F(-30)]
    offset = [F(-30), F(30)]
    prd = [F(-20), F(40)]
    tau = F(20)
    plus = [t + p / 2 + tau for t, p in zip(offset, prd)]
    minus = [t - p / 2 - tau for t, p in zip(offset, prd)]
    dc = dot(a, plus) - dot(b, minus)
    shifted_dc = dot(a, [x+s for x,s in zip(plus, shifts)]) - dot(b, [x+s for x,s in zip(minus, shifts)])
    assert shifted_dc - dc == dot(d, shifts) == 36
    # All-shift invariance is a vector statement; each basis shift probes a coordinate.
    basis_residuals = [dot(d, [F(i == j) for i in range(2)]) for j in range(2)]
    assert any(basis_residuals)
    assert norm([8, 2]) == norm([80, 20])
    # Fixed shifts may be orthogonal to unequal weight differences.
    assert dot(d, [F(7), F(7)]) == 0
    a3, b3 = norm([2, 1, 1]), norm([1, 2, 1])
    d3 = [x-y for x,y in zip(a3,b3)]
    assert a3 != b3 and dot(d3, [F(1), F(1), F(9)]) == 0
    # General response for role-asymmetric pools; matched calibration uses both roles.
    response = dot(d, offset) + dot([ (x+y)/2 for x,y in zip(a,b)], prd)
    assert (dc - response) / 2 == tau
    shifted_response = dot(d,[t+s for t,s in zip(offset,shifts)]) + dot([(x+y)/2 for x,y in zip(a,b)],prd)
    assert (shifted_dc - shifted_response) / 2 == tau
    # Symmetric target weights with wrong equal-weight PRD: lifetime error, not DeltaC error.
    target_prd = dot(a, prd)
    equal_prd = dot(norm([1,1]), prd)
    assert (target_prd-equal_prd)/2 == -9
    # Different weights can produce the same scalar PRD by coincidence.
    assert dot(a,[F(10),F(10)]) == dot(norm([1,1]),[F(10),F(10)])
    # Original MC113 used Gaussian-only branches: lifetime spread was absent.
    sigma, n = [F(120),F(140)], F(150)
    mean_var = sum(w*w*(s*s+tau*tau)/n for w,s in zip(norm([1,1]),sigma))*2
    gaussian_only_var = sum(w*w*s*s/n for w,s in zip(norm([1,1]),sigma))*2
    assert mean_var == 116 and gaussian_only_var == F(340,3)
    return {
        'scope':'exact rational synthetic design; complete support, common tau, role labels retained, no backgrounds',
        'shift_law':'DeltaC_after-DeltaC_before = sum((a_i-b_i)*s_i), a=w+/sum(w+), b=w-/sum(w-)',
        'all_shift_invariance':'for every independent shift vector s iff a=b; raw weights need only be proportional',
        'fixed_shift_invariance':'for a specified s iff dot(a-b,s)=0; unequal weights may cancel accidentally',
        'general_prompt_response':'R(a,b) = dot(a-b,T0)+dot((a+b)/2,PRD); tau=(DeltaC-R)/2',
        'asymmetric_raw_delta_c_ps':float(dc),'asymmetric_aligned_delta_c_ps':float(shifted_dc),
        'alignment_change_ps':36,'wrong_equal_prd_lifetime_bias_ps':-9,
        'variance_delayed_plus_prompt_model_ps2':float(mean_var),
        'variance_gaussian_only_113_ps2':float(gaussian_only_var),
        'mc113_boundary':'MC113 verifies Gaussian centroid-noise variance only; it omitted exponential lifetime fluctuations and does not verify bias cases',
        'experiment_boundary':'no actual pair counts, sorter, calibration covariance, or original experimental CI reconstructed'
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    result = calculate()
    result['script_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(result,ensure_ascii=False))
