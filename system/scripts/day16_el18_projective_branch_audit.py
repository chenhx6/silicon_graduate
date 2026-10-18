#!/usr/bin/env python3
"""Audit printed EL18 branches, shared attenuation and the pure-E2 endpoint.

Uses a selected real table row and already checked KS70/D96 kernels. Marginal
rectangles are explicitly not the paper's recovered joint likelihood/ellipse.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np
from scipy.optimize import brentq

from day16_ks70_network_reference_audit import matrix
from day16_kf89_w178_gate_audit import finite_delta, intersection, preimage, roots, value


def gfactor(rank: int, phi: float) -> float:
    return (1 + 2 * sum(1 / (1 + q*q*phi*phi) for q in range(1, rank + 1))) / (2*rank + 1)


def dg_dphi(rank: int, phi: float) -> float:
    return -4 * phi * sum(q*q / (1 + q*q*phi*phi)**2 for q in range(1, rank + 1)) / (2*rank + 1)


def delta_interval(interval: list) -> dict:
    lo, hi = interval
    return {"atan_delta_deg": interval,
            "delta_lower": "-infinity" if abs(lo + 90) < 1e-8 else math.tan(math.radians(lo)),
            "delta_upper": "+infinity" if abs(hi - 90) < 1e-8 else math.tan(math.radians(hi))}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    cfg = json.loads(args.input.read_text())
    assert cfg["identity"] == "DAY16-EL18-MO104-PROJECTIVE-BRANCH-01"
    target = cfg["target"]
    forms = {k: matrix("target-first", k) for k in [0, 2, 4]}
    coefficients = {}
    for d in [None, 50.0, -0.15]:
        alpha = math.pi / 2 if d is None else math.atan(d)
        coefficients[str(d)] = {str(k): value(m, alpha) for k, m in forms.items()}
    assert np.max(abs(forms[0] - np.eye(2))) < 1e-12
    assert abs(value(forms[2], math.pi/2) - value(forms[2], -math.pi/2)) < 1e-14
    assert abs(value(forms[4], math.pi/2) - value(forms[4], -math.pi/2)) < 1e-14
    # All exact central A2 roots, without selecting the branch nearest a prior.
    central_a2 = target["corrected_A2"][0]
    candidates = [{"delta": finite_delta(a), "atan_delta_deg": math.degrees(a),
                   "predicted_A4": value(forms[4], a)}
                  for a in roots(forms[2] - central_a2 * np.eye(2))]
    boxes = []
    for scale in [1.0, 1.5, 3.0]:
        sets = [preimage(forms[k], np.eye(2), central-scale*margin, central+scale*margin)
                for k, (central, margin) in [(2, target["corrected_A2"]), (4, target["corrected_A4"])]]
        joint = intersection(sets[0], sets[1])
        wrapped = (bool(joint) and abs(joint[0][0] + 90) < 1e-8
                   and abs(joint[-1][1] - 90) < 1e-8)
        boxes.append({"margin_multiplier": scale,
                      "A2_preimage": [delta_interval(x) for x in sets[0]],
                      "A4_preimage": [delta_interval(x) for x in sets[1]],
                      "intersection": [delta_interval(x) for x in joint],
                      "first_and_last_segments_join_at_same_pure_E2_point": wrapped,
                      "confidence_level": None,
                      "scope": "literal printed marginal rectangle, not recovered source ellipse or DELTA recipe"})

    y2, sy2 = target["raw_A2"]
    y4, sy4 = target["raw_A4"]
    g2, sg2 = cfg["attenuation"]["G2"]
    g4, sg4 = cfg["attenuation"]["G4"]
    jac = np.array([[1/g2, 0, -y2/g2**2, 0],
                    [0, 1/g4, 0, -y4/g4**2]])
    nominal_independent_cov = jac @ np.diag(np.array([sy2, sy4, sg2, sg4])**2) @ jac.T
    phi = brentq(lambda x: gfactor(2, x) - g2, 0, 100)
    g4_from_phi = gfactor(4, phi)
    calibration_slope = dg_dphi(4, phi) / dg_dphi(2, phi)
    # Print-precision test of the 106Mo raw==corrected row, not an error-bar test.
    control = cfg["printed_correction_control"]
    closure = []
    for rank, gg, half_g in [(2, g2, cfg["attenuation"]["G2_half_printing_step"]),
                              (4, g4, cfg["attenuation"]["G4_half_printing_step"])]:
        raw = control[f"raw_A{rank}"][0]
        corr = control[f"corrected_A{rank}"][0]
        half = control["central_half_printing_step_A2A4"][0 if rank == 2 else 1]
        image = sorted(x / z for x in [raw-half, raw+half] for z in [gg-half_g, gg+half_g])
        printed_box = [corr-half, corr+half]
        overlap = max(image[0], printed_box[0]) <= min(image[-1], printed_box[1])
        closure.append({"rank": rank, "raw_divided_by_group_G_central": raw/gg,
                        "source_printed_corrected_central": corr,
                        "all_last_digit_rounding_image": [image[0], image[-1]],
                        "source_corrected_last_digit_box": printed_box,
                        "printing_boxes_overlap": overlap,
                        "statistical_confidence_or_experimental_contradiction": None})
    # Observable sign across delta infinity can change through M1=0 while E2
    # stays positive; this is an algebraic ambiguity, not a fitted shape model.
    reciprocal = [-0.01, 0.0, 0.01]
    reciprocal_example = [{"M1_over_E2": x, "E2_amplitude": 1.0,
                           "delta_E2_over_M1": "pureE2" if x == 0 else 1/x,
                           "A2": value(forms[2], math.atan2(1.0, x)),
                           "A4": value(forms[4], math.atan2(1.0, x))} for x in reciprocal]
    result = {"identity": cfg["identity"],
              "input_sha256": hashlib.sha256(args.input.read_bytes()).hexdigest(),
              "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "target_identity": target,
              "normalized_A0_A2_A4_matrices": {str(k): m.tolist() for k, m in forms.items()},
              "source_candidate_forward_checks": coefficients,
              "all_central_A2_roots": candidates, "printed_margin_boxes": boxes,
              "nominal_raw_over_G": [y2/g2, y4/g4],
              "correction_Jacobian_order_Y2_Y4_G2_G4": jac.tolist(),
              "only_if_inputs_independent_corrected_standard_errors":
                  np.sqrt(np.diag(nominal_independent_cov)).tolist(),
              "actual_corrected_covariance_known": False,
              "Eq9_same_phi_calibration": {"phi_magnitude": phi, "G4_at_same_phi": g4_from_phi,
                   "dG4_dG2": calibration_slope,
                   "g_sign_identified": False,
                   "physical_G2_range": [1/5, 1], "physical_G4_range": [1/9, 1],
                   "source_above_unity_centrals": cfg["calibration_G2_above_unity"],
                   "interpretation": "Gk is even in phi/g. Printed central G2 above1 has no real phi; uncertainty/other recipe is needed, no g is refit or clipped here."},
              "Mo106_literal_correction_printing_check": closure,
              "pure_endpoint_bound_printing_discrepancy": cfg["pure_interval_controls"],
              "fixed_E2_M1_zero_crossing_algebraic_control": reciprocal_example,
              "source_DELTA_producer_recovered": False,
              "new_spin_delta_g_or_shape_measurement": False,
              "all_internal_checks_passed": True}
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False) + "\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
