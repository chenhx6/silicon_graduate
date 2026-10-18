#!/usr/bin/env python3
"""Martin87 Eq9: photon-conditioned versus total-decay unobserved transfer.

Uses actual nominal BrIcc168.71 pure-component outputs in a declared W178 path
design. No observed DCO for this endpoint gate is supplied or inferred.
"""
from __future__ import annotations

import argparse
import ctypes as ct
import hashlib
import json
import math
from pathlib import Path

import numpy as np

from day16_alpaca_code_crosscheck import unobserved_channel
from day16_d96_eq4_erratum_audit import direct_operators
from day16_kf89_w178_gate_audit import parts as target_parts, population
from day16_pdco_ambiguity_preview import orientation


def mixture(u1: float, u2: float, q: float) -> float:
    return (u1 + q * u2) / (1 + q)


def endpoint_density(spins: list, pop: np.ndarray, delta_first: float,
                     q_middle: float, angles: list) -> float:
    j0, j1, j2, j3 = spins
    theta_first, theta_last, phi = np.deg2rad(angles)
    initial = np.diag(pop)
    after_first = sum(op @ initial @ op.conj().T
                      for op in direct_operators(j0, j1, target_parts(delta_first),
                                                 theta_first, 0.0, None))
    # This is the integrated nuclear rank-L channel with the declared weights.
    # It does not simulate electron trajectories or atomic wave functions.
    after_middle = unobserved_channel(after_first, j1, j2,
                                      (("M", 1, 1.0), ("E", 2, math.sqrt(q_middle))))
    total = sum(np.trace(op @ after_middle @ op.conj().T).real
                for op in direct_operators(j2, j3, (("E", 2, 1.0),),
                                            theta_last, phi, None))
    assert total > 0
    return float(total)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--captured", type=Path, required=True)
    parser.add_argument("--gsl-library", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    cfg = json.loads(args.input.read_text())
    data = json.loads(args.captured.read_text())
    assert cfg["identity"] == data["identity"] == "DAY16-W178-168P71-UNOBSERVED-IC-01"
    assert data["query_input_sha256"] == hashlib.sha256(args.input.read_bytes()).hexdigest()
    models = {m["multipole"]: m for m in data["models"]}
    alpha_m, alpha_e = [models[k]["values"]["Tot"]["value"] for k in ["M1", "E2"]]
    error_m, error_e = [models[k]["values"]["Tot"]["quoted_error"] for k in ["M1", "E2"]]
    c = (1 + alpha_e) / (1 + alpha_m)
    q_gamma = cfg["middle_delta_gamma"] ** 2
    q_total = q_gamma * c
    mean_alpha = (alpha_m + q_gamma * alpha_e) / (1 + q_gamma)
    p_gamma = 1 / (1 + mean_alpha)
    assert abs(p_gamma - (1 + q_gamma) / (1 + alpha_m + q_gamma * (1 + alpha_e))) < 1e-15
    literal_c_box = [(1 + alpha_e - error_e) / (1 + alpha_m + error_m),
                     (1 + alpha_e + error_e) / (1 + alpha_m - error_m)]
    grad = np.array([-(1 + alpha_e) / (1 + alpha_m)**2, 1 / (1 + alpha_m)])
    covariance_family = {str(rho): math.sqrt(max(0.0,
        grad[0]**2 * error_m**2 + grad[1]**2 * error_e**2
        + 2 * rho * grad[0] * grad[1] * error_m * error_e)) for rho in [-1, 0, 1]}

    gsl = ct.CDLL(str(args.gsl_library.resolve()))
    sixj = gsl.gsl_sf_coupling_6j
    sixj.restype = ct.c_double
    sixj.argtypes = [ct.c_int] * 6
    ji, jf = cfg["endpoint_design"]["spins"][1:3]
    reference = np.zeros((2 * ji + 1, 2 * ji + 1))
    reference[-1, -1] = 1.0
    u_records, pure_errors, controls = [], [], []
    for k in [0, 2, 4]:
        values = []
        for kind, ell in [("M", 1), ("E", 2)]:
            u = ((-1)**(ji + jf + ell) * math.sqrt((2 * ji + 1) * (2 * jf + 1))
                 * sixj(2 * ji, 2 * ji, 2 * k, 2 * jf, 2 * jf, 2 * ell))
            direct = unobserved_channel(reference, ji, jf, ((kind, ell, 1.0),))
            trace_ratio = orientation(jf, direct, k) / orientation(ji, reference, k)
            pure_errors.append(abs(u - trace_ratio))
            values.append(u)
        u1, u2 = values
        gamma, total = mixture(u1, u2, q_gamma), mixture(u1, u2, q_total)
        delta = q_gamma * (c - 1) * (u2 - u1) / ((1 + q_gamma) * (1 + c * q_gamma))
        assert abs(total - gamma - delta) < 1e-14
        # Pure limits, equal/zero ICC and delta-sign controls.
        assert mixture(u1, u2, 0.0) == u1
        assert abs(mixture(u1, u2, 1e14) - u2) < 1e-12
        assert mixture(u1, u2, (-cfg["middle_delta_gamma"])**2) == gamma
        for common_alpha in [0.0, alpha_m, alpha_e]:
            assert abs(mixture(u1, u2, q_gamma * (1 + common_alpha) / (1 + common_alpha)) - gamma) < 1e-15
        if k == 0:
            assert max(abs(u1 - 1), abs(u2 - 1), abs(total - 1), abs(gamma - 1)) < 1e-12
        u_records.append({"rank": k, "U_M1": u1, "U_E2": u2,
                          "photon_conditioned": gamma, "total_decay_marginal": total,
                          "difference": total - gamma, "analytic_difference": delta,
                          "theory_literal_margin_image": sorted(mixture(u1, u2, q_gamma * cc) for cc in literal_c_box)})

    design = cfg["endpoint_design"]
    spins, angles = design["spins"], design["angles_AB_deg"]
    pop = population(spins[0], spins[0] * design["sigma_std_over_J"])
    endpoint = []
    for first_delta in design["first_delta_KS_D96_candidates"]:
        comparison = {}
        for label, q in [("gamma_postselected_middle", q_gamma), ("middle_gamma_or_conversion_unobserved", q_total)]:
            w_ab = endpoint_density(spins, pop, first_delta, q, angles)
            w_ba = endpoint_density(spins, pop, first_delta, q, [angles[1], angles[0], angles[2]])
            comparison[label] = {"W_first90_last38": w_ab, "W_first38_last90": w_ba,
                                 "R_W90_38_over_W38_90": w_ab / w_ba}
        gamma_r = comparison["gamma_postselected_middle"]["R_W90_38_over_W38_90"]
        total_r = comparison["middle_gamma_or_conversion_unobserved"]["R_W90_38_over_W38_90"]
        endpoint.append({"delta_first_conditional_candidate": first_delta, "predictions": comparison,
                         "R_total_minus_gamma": total_r - gamma_r,
                         "fractional_R_change": total_r / gamma_r - 1,
                         "measured_ratio_for_this_gate_available": False})
    # All ranks depend on q_total only. A positive alternative ICC factor can
    # be absorbed exactly by q_gamma if no radiative-mixing companion exists.
    invariance_proof = "q_gamma_B=q_gamma_A*c_A/c_B => c_B*q_gamma_B=c_A*q_gamma_A => all U_k equal (c_A,c_B>0). No parity identification from U alone when q_gamma is free."
    result = {"identity": cfg["identity"],
              "input_sha256": hashlib.sha256(args.input.read_bytes()).hexdigest(),
              "captured_theory_sha256": hashlib.sha256(args.captured.read_bytes()).hexdigest(),
              "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "alpha_total_M1_E2": [alpha_m, alpha_e],
              "q_gamma": q_gamma, "ICC_weight_factor_c": c, "q_total_decay": q_total,
              "abs_effective_total_mixing_coordinate": math.sqrt(q_total),
              "radiative_E2_fraction": q_gamma / (1 + q_gamma),
              "total_decay_E2_fraction": q_total / (1 + q_total),
              "radiative_fraction_of_middle_decays": p_gamma,
              "theory_c_literal_margin_box": literal_c_box,
              "theory_c_local_error_covariance_family": covariance_family,
              "confidence_level": None, "pure_U_GSL_vs_channel_max_error": max(pure_errors),
              "U_records": u_records, "endpoint_design": endpoint,
              "identifiability_boundary": invariance_proof,
              "missing_companion": "Independent radiative |delta_gamma| or matched measured ICC/branch/response; ENSDF CC.8(.3) has no certified producer here and is not treated as an independent measurement.",
              "all_internal_checks_passed": bool(max(pure_errors) < 1e-12),
              "new_experimental_result": False,
              "scope": "Martin Eq9 total-decay versus explicitly photon-conditioned channels; chosen endpoint/gate/spin/alignment/point response. No new W178 delta, DCO or experimental significance."}
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False) + "\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
