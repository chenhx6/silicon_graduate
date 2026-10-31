#!/usr/bin/env python3
"""Declared algebra/identifiability controls; no original experimental fit."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction as F
from pathlib import Path


def three_j_squared(a: int, b: int, c: int, x: int, y: int, z: int) -> F:
    """Integer-spin Racah sum squared, exact rational arithmetic."""
    if x + y + z or abs(x) > a or abs(y) > b or abs(z) > c:
        return F(0)
    if not abs(a - b) <= c <= a + b:
        return F(0)
    fact = math.factorial
    delta = F(fact(a + b - c) * fact(a - b + c) * fact(-a + b + c),
              fact(a + b + c + 1))
    product = math.prod(fact(j + m) * fact(j - m)
                        for j, m in [(a, x), (b, y), (c, z)])
    total = F(0)
    for k in range(a + b + c + 2):
        args = [k, a + b - c - k, a - x - k, b + y - k,
                c - b + x + k, c - a - y + k]
        if min(args) >= 0:
            total += F((-1) ** k, math.prod(fact(v) for v in args))
    return delta * product * total * total


def magnetic_sum(ji: int, jf: int, rank: int = 2) -> F:
    # Wigner-Eckart convention:
    # <jf mf|T_kq|ji mi> = phase * (jf k ji; -mf q mi) * R.
    # Set |R|²=1; incoherent average over initial substates.
    return sum((three_j_squared(jf, rank, ji, -mf, q, mi)
                for mi in range(-ji, ji + 1)
                for mf in range(-jf, jf + 1)
                for q in range(-rank, rank + 1)), F(0)) / (2 * ji + 1)


def simpson(function, low: float, high: float, n: int = 2000) -> float:
    h = (high - low) / n
    return h / 3 * (function(low) + function(high) +
                    4 * sum(function(low + i * h) for i in range(1, n, 2)) +
                    2 * sum(function(low + i * h) for i in range(2, n, 2)))


def calculate() -> dict:
    controls: list[dict] = []

    def check(name, actual, expected, tolerance=1e-10):
        ok = math.isclose(float(actual), float(expected),
                          rel_tol=tolerance, abs_tol=tolerance)
        controls.append(dict(name=name, actual=float(actual),
                             expected=float(expected), passed=ok))
        if not ok:
            raise AssertionError(controls[-1])

    # Nontrivial exact angular-momentum summation, plus known zero-spin limit.
    for rank in [1, 2, 3]:
        check(f"zero-spin 3j rank{rank}",
              three_j_squared(0, rank, rank, 0, rank, -rank), F(1, 2 * rank + 1))
    transitions = []
    for ji, jf in [(0, 2), (2, 0), (2, 4), (4, 2), (1, 3), (3, 1), (2, 2)]:
        strength = magnetic_sum(ji, jf)
        check(f"B from magnetic sum {ji}->{jf}", strength, F(1, 2 * ji + 1))
        reverse = magnetic_sum(jf, ji)
        check(f"detailed balance {ji}<->{jf}",
              (2 * ji + 1) * strength, (2 * jf + 1) * reverse)
        transitions.append(dict(ji=ji, jf=jf, B=str(strength), B_reverse=str(reverse)))
    up, down = magnetic_sum(0, 2), magnetic_sum(2, 0)
    check("0->2 excitation/decay B ratio", up / down, 5)
    # Nolan printed Eq6.5: 5 Bup = Bdown for upper Ji=2/lower Jf=0.
    # This control establishes incompatibility with the declared definition,
    # not a verified publisher erratum or knowledge of the authors' producer.
    printed_residual_ratio = 5 * up / down
    check("printed Eq6.5 LHS/RHS in 0<->2 control", printed_residual_ratio, 25)

    # Scaled yield excludes N/rho, solid angle, gamma branches and efficiency.
    # E is MeV, sigma is barn, x is mg/cm², S is MeV/(mg/cm²).
    e0, emin, k, stopping = 10.0, 5.0, .002, 2.0
    sigma = lambda energy: k * energy**2
    positive = simpson(lambda energy: sigma(energy) / stopping, emin, e0)
    signed = simpson(lambda energy: sigma(energy) / -stopping, e0, emin)
    mixed = simpson(lambda energy: sigma(energy) / stopping, e0, emin)
    exact = k * (e0**3 - emin**3) / (3 * stopping)
    check("positive stopping convention", positive, exact)
    check("signed dE/dx convention", signed, exact)
    check("mixed convention negative", mixed, -exact)
    check("zero target thickness", simpson(lambda e: sigma(e) / stopping, e0, e0), 0)
    thin = simpson(lambda e: sigma(e) / stopping, e0 - .001, e0)
    check("thin foil limit", thin / (.001 * sigma(e0) / stopping), 1, tolerance=.00011)

    # q and r denote inferred width combinations after spin/flux/geometry
    # normalization, not raw count rates. All width inputs are synthetic.
    hbar_meV_fs, q_meV = 658.2119569, 1.0
    families = []
    for branch in [.2, .5, 1.0]:
        gamma = q_meV / branch**2
        gamma0 = branch * gamma
        tau = hbar_meV_fs / gamma
        check(f"NRF same observable b={branch}", gamma0**2 / gamma, q_meV)
        check(f"NRF lifetime family b={branch}", tau, hbar_meV_fs * branch**2 / q_meV)
        families.append(dict(branch=branch, Gamma_meV=gamma, Gamma0_meV=gamma0,
                             tau_fs=tau, q_meV=q_meV))
    r_meV = 4.0
    gamma = r_meV**2 / q_meV
    check("combined scattering/selfabsorption branch", q_meV / r_meV, .25)
    check("combined scattering/selfabsorption Gamma", gamma, 16)
    covariance_examples = []
    for correlation in [-1, 0, 1]:
        # ln tau = ln hbar + ln q - 2ln r.
        variance = .1**2 + 4 * .05**2 - 4 * correlation * .1 * .05
        check(f"ln tau variance rho{correlation}", variance,
              {-1: .04, 0: .02, 1: 0}[correlation])
        covariance_examples.append(dict(correlation=correlation,
                                        relative_sigma_linear=math.sqrt(max(0, variance))))
    return dict(
        status="conditional mathematical controls passed",
        scientific_scope="No measured widths, original fit, confidence interval or independent primary experiment",
        angular_definition="B(i->f)=|<f||T||i>|²/(2Ji+1), Hermitian E2 tensor",
        angular_transitions=transitions,
        Nolan_Eq6_5_literal="(2Ji+1)B(Jf->Ji)=(2Jf+1)B(Ji->Jf)",
        literal_vs_declared_definition="incompatible for unequal spins under this standard definition; source literal retained, no verified erratum",
        excitation_decay_ratio_0_2=float(up / down),
        printed_literal_LHS_over_RHS_0_2=float(printed_residual_ratio),
        yield_inputs=dict(E0_MeV=e0, Emin_MeV=emin, sigma_k_barn_per_MeV2=k,
                          S_MeV_per_mg_cm2=stopping),
        scaled_yield_barn_mg_cm2=positive, mixed_sign_yield=mixed,
        nrf_inputs="q=1meV synthetic normalized scattering width; family b=.2/.5/1; optional r=4meV synthetic selfabsorption width",
        nrf_family=families,
        combined_nrf=dict(Gamma_meV=gamma, Gamma0_meV=r_meV, branch=q_meV/r_meV,
                          tau_fs=hbar_meV_fs/gamma),
        nrf_covariance_controls=covariance_examples,
        required_inputs=["spin/flux/efficiency/angular and source-line normalization",
                         "branch and conversion definition; total versus partial widths",
                         "signed or positive beam stopping convention and target thickness",
                         "full shared covariance for companion observables"],
        controls=controls, control_count=len(controls))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = calculate()
    source = Path("raw/papers/gpt/learning-daily/20260920-PREPLAN-high-spin-library/review/1979_Nolan_Sharpey-Schafer_The measurement of the lifetimes of excited nuclear states.pdf")
    result["source_sha256"] = hashlib.sha256(source.read_bytes()).hexdigest()
    result["script_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({k: result[k] for k in ["status", "control_count",
                     "excitation_decay_ratio_0_2", "scaled_yield_barn_mg_cm2",
                     "combined_nrf"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
