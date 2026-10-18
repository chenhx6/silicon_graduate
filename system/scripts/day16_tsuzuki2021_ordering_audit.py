#!/usr/bin/env python3
"""Check the stated two-hit ordering domain and reported uncertainty layers.

Uses printed energies and analytic Compton kinematics, not event surrogates.
"""
import argparse
from datetime import datetime
import hashlib
import json
import math
from pathlib import Path
from zoneinfo import ZoneInfo

import sympy as sp


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--contract", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    cfg = json.loads(args.contract.read_text())
    assert cfg["identity"] == "T21-ORDERING-AND-NORMALIZATION-CONTRACT-01"
    assert sha(Path(cfg["raw"])) == cfg["raw_sha256"]
    q = cfg["published_input"]
    mass = q["electron_rest_keV"]
    e, m = sp.symbols("E m", positive=True)
    gap = sp.factor(e*(2/(1+2*e/m)-1))
    assert sp.simplify(gap-e*(m-2*e)/(m+2*e)) == 0
    low_rows = [{"energy_keV": value,
                 "min_EA_minus_ES_keV": value*(mass-2*value)/(mass+2*value),
                 "minenergy_order_guaranteed_under_stated_process": value < mass/2}
                for value in [*q["T21_energy_window_keV"], q["T21_reference_E_keV"]]]
    assert all(row["minenergy_order_guaranteed_under_stated_process"] for row in low_rows)
    E = q["G24_reference_E_keV"]
    crossing = math.degrees(math.acos(1-mass/E))
    both_orders = math.degrees(math.acos(1-mass*mass/(2*E*E)))
    assert both_orders < q["G24_scatter_cut_deg"][0] < crossing < q["G24_scatter_cut_deg"][1]
    rows = []
    for degree in cfg["ordering_demo_angles_deg"]:
        c = math.cos(math.radians(degree))
        ea = E/(1+E/mass*(1-c))
        es = E-ea
        assert abs(1-mass*(1/ea-1/E)-c) < 1e-14
        swapped_cosine = 1-mass*(1/es-1/E)
        swapped_allowed = -1 <= swapped_cosine <= 1
        assert swapped_allowed
        rows.append({"theta_true_deg": degree, "EA_keV": ea, "ES_keV": es,
            "minenergy_selects_true_first_hit": es < ea,
            "reverse_order_also_has_physical_kinematic_cosine": swapped_allowed,
            "reverse_order_thetaK_deg": math.degrees(math.acos(swapped_cosine))})
    E0, threshold = q["T21_reference_E_keV"], q["Si_threshold_approx_keV"]
    threshold_cosine = 1-mass*(1/(E0-threshold)-1/E0)
    assert -1 < threshold_cosine < 1
    xyz = sp.symbols("x1 y1 z1 x2 y2 z2", real=True)
    a, b = sp.Matrix(xyz[:3]), sp.Matrix(xyz[3:])
    forward, reverse = a.cross(b-a), b.cross(a-b)
    assert all(sp.expand(v) == 0 for v in forward+reverse)
    phi = sp.symbols("phi", real=True)
    assert sp.trigsimp(sp.cos(2*(phi+sp.pi))-sp.cos(2*phi)) == 0
    out = {"at": datetime.now(ZoneInfo("Asia/Shanghai")).isoformat(),
        "script_sha256": sha(Path(__file__)), "contract_sha256": sha(args.contract),
        "source_sha256": cfg["raw_sha256"], "free_rest_one_scatter_process_only": True,
        "min_gap_exact": str(gap), "ordering_all_angles_threshold_keV": mass/2,
        "T21_selected_window_controls": low_rows,
        "G24_847_equal_deposits_angle_deg": crossing,
        "G24_847_both_energy_orders_allowed_from_deg": both_orders,
        "847_accepted_angle_examples": rows,
        "T21_8keV_threshold_implied_thetaK_deg_ideal": math.degrees(math.acos(threshold_cosine)),
        "same_point_source_plane_reverse_normal_identity_passed": True,
        "common_axis_cos2phi_invariance_passed": True,
        "order_reversal_always_flips_polarization_sign_claimed": False,
        "reported_error_layer_arithmetic": {"reported_stat": q["T21_stat"], "reported_sys": q["T21_sys"],
            "linear_sum": q["T21_stat"]+q["T21_sys"],
            "quadrature_if_independent_not_source_choice": math.hypot(q["T21_stat"], q["T21_sys"]),
            "source_total_retained": q["T21_total_reported"],
            "Ba_residual_over_assumed_Q100": q["Ba_residual_modulation"]/q["assumed_Q100_for_sys"]},
        "selected_over_registered_from_rounded_totals": q["selected_events_approx"]/q["registered_events_approx"],
        "actual_ordering_misassignment_rate_Pfit_or_template_covariance_recovered": False,
        "boundary": "No raw events, finite-energy response, actual Go event ordering or transfer of atomic P to nuclear gamma reference."}
    args.output.write_text(json.dumps(out, indent=2, allow_nan=False)+"\n")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
