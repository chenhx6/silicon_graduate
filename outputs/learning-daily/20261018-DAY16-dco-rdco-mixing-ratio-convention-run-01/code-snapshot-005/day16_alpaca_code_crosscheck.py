#!/usr/bin/env python3
"""Execute a pinned external ALPACA build against explicit photon traces.

The external GPL implementation stays in the user-specified temporary build.
This harness contains no copied implementation of ALPACA. It checks the frozen
phase/role/observable contract, not an experiment's production analysis.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import sys

import numpy as np

from day16_d96_eq4_erratum_audit import direct_density, direct_operators
from day16_pdco_ambiguity_preview import cg


PURE_E2 = (("E", 2, 1.0),)


def m1e2(delta: float | None) -> tuple:
    return PURE_E2 if delta is None else (("M", 1, 1.0), ("E", 2, delta))


def unobserved_channel(rho: np.ndarray, ji: int, jf: int, parts: tuple) -> np.ndarray:
    """Complete photon marginal: incoherent multipole and magnetic sums."""
    result = np.zeros((2 * jf + 1, 2 * jf + 1), dtype=complex)
    norm = sum(a * a for _, _, a in parts)
    for _, ell, a in parts:
        for mu in range(-ell, ell + 1):
            op = np.array([[cg(jf, mf, ell, mu, ji, mi) if mf + mu == mi else 0.0
                            for mi in range(-ji, ji + 1)]
                           for mf in range(-jf, jf + 1)])
            result += a * a / norm * (op @ rho @ op.T)
    assert abs(np.trace(result) - np.trace(rho)) < 1e-12
    return result


def three_step_trace(spins: list, parts: list, theta: float, phi: float) -> float:
    ji, ja, jb, jf = spins
    rho = np.eye(2 * ji + 1) / (2 * ji + 1)
    conditioned = sum(op @ rho @ op.conj().T
                      for op in direct_operators(ji, ja, parts[0], 0.0, 0.0, None))
    propagated = unobserved_channel(conditioned, ja, jb, parts[1])
    total = sum(np.trace(op @ propagated @ op.conj().T).real
                for op in direct_operators(jb, jf, parts[2], theta, phi, None))
    return float(total * 16 * math.pi**2)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--alpaca-build", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    cfg = json.loads(args.input.read_text())
    assert cfg["identity"] == "DAY16-ALPACA-FIXED-CODE-ROLE-PHASE-01"
    build = args.alpaca_build.resolve()
    sys.path.insert(0, str(build / "python"))
    from alpaca.angular_correlation import AngularCorrelation
    from alpaca.state import State
    from alpaca.transition import ELECTRIC, EM_UNKNOWN, MAGNETIC, Transition

    def external(spins: list | tuple, parts: list, polarized: bool = False,
                 wrong_first_sign: bool = False, parities: list | None = None):
        states = [State(2 * j, parities[i] if parities else 0)
                  for i, j in enumerate(spins)]
        steps = []
        for i, item in enumerate(parts):
            kind, ell, a = item[0]
            if len(item) == 1:
                kindp, ellp, ratio = ("M" if kind == "E" else "E"), ell + 1, 0.0
            else:
                kindp, ellp, ap = item[1]
                ratio = ap / a
            # Frozen KS70 Eq12 / IF21 Eq18 map, before any code output.
            if i == 0 and not wrong_first_sign:
                ratio = -ratio
            em = (ELECTRIC if kind == "E" else MAGNETIC) if polarized else EM_UNKNOWN
            emp = (ELECTRIC if kindp == "E" else MAGNETIC) if polarized else EM_UNKNOWN
            steps.append([Transition(em, 2 * ell, emp, 2 * ellp, ratio), states[i + 1]])
        return AngularCorrelation(states[0], steps)

    angles = [(math.radians(t), math.radians(p))
              for t in cfg["geometry_deg"]["theta"] for p in cfg["geometry_deg"]["phi"]]
    mode_dir = {"q1": 0, "q2": 0, "psi1_deg": 0.0, "psi2_deg": 0.0}
    mode_pol = {"q1": 1, "q2": 0, "psi1_deg": 0.0, "psi2_deg": 0.0}
    records, errors, wrong_errors, pure_wrong_errors, norms = [], [], [], [], []

    def mean_over_sphere(correlation) -> float:
        xs, ws = np.polynomial.legendre.leggauss(6)
        return sum(w * sum(float(correlation(math.acos(x), p))
                           for p in [0.0, math.pi / 4, math.pi / 2, 3 * math.pi / 4])
                   / 4 for x, w in zip(xs, ws)) / 2

    for role, spins in cfg["roles"].items():
        pop = np.ones(2 * spins[0] + 1) / (2 * spins[0] + 1)
        for delta in cfg["delta_KS_D96_values"]:
            parts = ([m1e2(delta), PURE_E2] if role.startswith("first")
                     else [PURE_E2, m1e2(delta)])
            correct = external(spins, parts)
            wrong = external(spins, parts, wrong_first_sign=True)
            norm = mean_over_sphere(correct)
            norms.append(abs(norm - 1.0))
            local = []
            for theta, phi in angles:
                expected = 16 * math.pi**2 * direct_density(
                    tuple(spins), parts[0], parts[1], pop,
                    [0.0, math.degrees(theta), math.degrees(phi)], mode_dir)
                actual = float(correct(theta, phi))
                bad = float(wrong(theta, phi))
                errors.append(abs(actual - expected))
                if role.startswith("first"):
                    (pure_wrong_errors if delta in [0.0, None] else wrong_errors).append(abs(bad - expected))
                local.append({"theta_deg": math.degrees(theta), "phi_deg": math.degrees(phi),
                              "external": actual, "photon_trace": expected, "wrong_first_sign": bad})
            records.append({"role": role, "delta_KS_D96": delta,
                            "mean_over_sphere": norm, "samples": local})
            correct.free()
            wrong.free()

    path = cfg["unobserved_real_path"]
    spins = path["spins"]
    middle = path["middle_delta_KS"]
    parts = [PURE_E2, m1e2(middle), m1e2(path["last_delta_KS"])]
    reversed_middle = [PURE_E2, m1e2(-middle), parts[-1]]
    correlation = external(spins, parts)
    reversed_correlation = external(spins, reversed_middle)
    unobserved_records, middle_sign_errors = [], []
    for theta, phi in angles:
        actual = float(correlation(theta, phi))
        expected = three_step_trace(spins, parts, theta, phi)
        changed = float(reversed_correlation(theta, phi))
        errors.append(abs(actual - expected))
        middle_sign_errors.append(abs(actual - changed))
        unobserved_records.append({"theta_deg": math.degrees(theta), "phi_deg": math.degrees(phi),
                                   "external": actual, "complete_photon_marginal": expected,
                                   "reversed_middle_delta": changed})
    norms.append(abs(mean_over_sphere(correlation) - 1.0))
    correlation.free()
    reversed_correlation.free()

    polarized_records = []
    for case in cfg["polarized_controls"]:
        spins = case["spins"]
        parts = []
        for field in ["first", "last"]:
            one, two, delta = case[field]
            parts.append(((one[0], int(one[1:]), 1.0), (two[0], int(two[1:]), delta)))
        correlation = external(spins, parts, polarized=True, parities=case["parities"])
        pop = np.ones(2 * spins[0] + 1) / (2 * spins[0] + 1)
        local = []
        for theta, phi in angles:
            expected = 32 * math.pi**2 * direct_density(
                tuple(spins), parts[0], parts[1], pop,
                [0.0, math.degrees(theta), math.degrees(phi)], mode_pol)
            actual = float(correlation(theta, phi))
            errors.append(abs(actual - expected))
            local.append({"theta_deg": math.degrees(theta), "phi_deg": math.degrees(phi),
                          "external": actual, "polarized_first_trace": expected})
        norms.append(abs(mean_over_sphere(correlation) - 1.0))
        polarized_records.append({"case": case["id"], "samples": local})
        correlation.free()

    # API-object control: known EM types select W_pol_dir, despite identical
    # spins/multipoles. Averaging opposite analyzer axes recovers W_dir_dir.
    parts = [m1e2(-0.55), PURE_E2]
    direction = external([3, 2, 0], parts)
    polarization = external([3, 2, 0], parts, polarized=True, parities=[1, 1, 1])
    api_records, api_average_errors = [], []
    for theta_deg in cfg["geometry_deg"]["theta"]:
        theta = math.radians(theta_deg)
        unpolarized = float(direction(theta, 0.0))
        parallel = float(polarization(theta, 0.0))
        perpendicular = float(polarization(theta, math.pi / 2))
        api_average_errors.append(abs((parallel + perpendicular) / 2 - unpolarized))
        api_records.append({"theta_deg": theta_deg, "unknown_EM_selects_dir_dir": unpolarized,
                            "known_EM_selects_pol_dir_phi0": parallel,
                            "known_EM_selects_pol_dir_phi90": perpendicular})
    direction.free()
    polarization.free()
    all_values = [r["external"] for case in records for r in case["samples"]]
    all_values += [r["external"] for case in polarized_records for r in case["samples"]]
    tol = cfg["numerical_tolerance"]
    passed = (max(errors) < tol and max(norms) < tol and max(middle_sign_errors) < tol
              and max(api_average_errors) < tol and max(pure_wrong_errors) < tol
              and max(wrong_errors) > 1e-2 and min(all_values) > -tol)
    library = build / "source/libangular_correlation.so"
    result = {
        "identity": cfg["identity"], "commit": cfg["commit"],
        "input_sha256": hashlib.sha256(args.input.read_bytes()).hexdigest(),
        "harness_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "external_shared_library_sha256": hashlib.sha256(library.read_bytes()).hexdigest(),
        "producer_scope": cfg["code_scope"],
        "max_external_vs_photon_trace_error": max(errors),
        "max_angular_mean_error": max(norms),
        "wrong_first_sign_max_mixed_difference": max(wrong_errors),
        "wrong_first_sign_max_pure_difference": max(pure_wrong_errors),
        "unobserved_middle_sign_max_difference": max(middle_sign_errors),
        "API_polarization_average_to_direction_max_error": max(api_average_errors),
        "roles": records, "unobserved": unobserved_records,
        "polarized": polarized_records, "API_observable_switch": api_records,
        "all_checks_passed": passed,
        "new_experimental_result": False,
        "boundary": "Independent public C++/GSL implementation, same published formalism. No actual DCOMAP/RU09 production code, finite response, events or covariance recovered.",
    }
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False) + "\n")
    print(json.dumps({k: result[k] for k in result if k not in
                     ["roles", "unobserved", "polarized", "API_observable_switch"]}, ensure_ascii=False, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
