#!/usr/bin/env python3
"""Quantitative audit of DDCM finite-stopping corrections and Qt sensitivity.

Models the deceleration of recoiling nuclei in a stopper foil (Klemme 1999 Au stopper),
calculates decay fractions in vacuum vs slowing-down vs at rest, and audits the non-uniform
correction scale (1.181 - 1.255) and its differential impact on transition quadrupole moments.
Uses only the Python standard library. Requires --output PATH.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path


def calculate_decay_fractions(tau_ps, t_flight_ps, t_stop_ps):
    """Calculate the decay fractions in vacuum, during slowing down, and at rest."""
    p_vac = -math.expm1(-t_flight_ps / tau_ps)
    p_enter = math.exp(-t_flight_ps / tau_ps)
    p_slow = p_enter * (-math.expm1(-t_stop_ps / tau_ps))
    p_rest = p_enter * math.exp(-t_stop_ps / tau_ps)

    return {
        "tau_ps": tau_ps,
        "flight_time_ps": t_flight_ps,
        "stopping_time_ps": t_stop_ps,
        "fraction_decay_in_vacuum": p_vac,
        "fraction_decay_while_slowing": p_slow,
        "fraction_decay_at_rest": p_rest,
        "slowing_to_remaining_ratio": p_slow / (p_slow + p_rest) if (p_slow + p_rest) > 0 else 0.0,
        "rest_to_remaining_ratio": p_rest / (p_slow + p_rest) if (p_slow + p_rest) > 0 else 0.0,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True, help="Path for output JSON")
    args = parser.parse_args()

    checks = []
    def check(name, condition):
        checks.append({"name": name, "passed": bool(condition)})
        if not condition:
            raise AssertionError(f"Check failed: {name}")

    # 1. Klemme 1999 Table I finite-stopping correction data (six states)
    klemme_table1_corrected = [
        {"state": "6g_1", "E_gamma_keV": 631, "tau_standard": 1.38, "tau_corr": 1.63},
        {"state": "8g_1", "E_gamma_keV": 706, "tau_standard": 0.85, "tau_corr": 1.03},
        {"state": "8gamma_1", "E_gamma_keV": 557, "tau_standard": 1.04, "tau_corr": 1.24},
        {"state": "10S1_1", "E_gamma_keV": 691, "tau_standard": 0.58, "tau_corr": 0.71},
        {"state": "12S1_1", "E_gamma_keV": 666, "tau_standard": 0.47, "tau_corr": 0.59},
        {"state": "16S2_1", "E_gamma_keV": 748, "tau_standard": 0.55, "tau_corr": 0.68},
    ]

    correction_rows = []
    for row in klemme_table1_corrected:
        ratio = row["tau_corr"] / row["tau_standard"]
        diff = row["tau_corr"] - row["tau_standard"]
        correction_rows.append({
            **row,
            "correction_ratio": ratio,
            "absolute_difference_ps": diff,
            "percentage_increase": (ratio - 1.0) * 100.0,
        })

    min_ratio = min(r["correction_ratio"] for r in correction_rows)
    max_ratio = max(r["correction_ratio"] for r in correction_rows)

    check("Six corrected states present", len(correction_rows) == 6)
    check("Min correction ratio matches 1.181 (6g_1: 1.63/1.38)", math.isclose(min_ratio, 1.63/1.38, rel_tol=1e-4))
    check("Max correction ratio matches 1.255 (12S1_1: 0.59/0.47)", math.isclose(max_ratio, 0.59/0.47, rel_tol=1e-4))
    check("Correction ratio is non-uniform (differs across lifetimes)", max_ratio - min_ratio > 0.05)
    check("12S1 (0.47 ps) has larger ratio than 6g (1.38 ps)",
          correction_rows[4]["correction_ratio"] > correction_rows[0]["correction_ratio"])

    # 2. Physics of decay in Au stopper (t_stop = 1.1 ps)
    t_stop_nominal = 1.1  # ps
    decay_fractions_grid = []
    test_lifetimes = [0.2, 0.5, 1.0, 1.38, 2.0, 5.0, 10.0, 94.4]

    for tau in test_lifetimes:
        fracs = calculate_decay_fractions(tau, t_flight_ps=0.0, t_stop_ps=t_stop_nominal)
        decay_fractions_grid.append(fracs)

    f_05 = next(f for f in decay_fractions_grid if f["tau_ps"] == 0.5)
    check("For tau=0.5ps, slowing fraction exceeds 80%", f_05["slowing_to_remaining_ratio"] > 0.85)

    f_138 = next(f for f in decay_fractions_grid if f["tau_ps"] == 1.38)
    check("For tau=1.38ps, slowing fraction is between 50% and 60%", 0.50 < f_138["slowing_to_remaining_ratio"] < 0.60)

    f_944 = next(f for f in decay_fractions_grid if f["tau_ps"] == 94.4)
    check("For tau=94.4ps (2+), rest fraction exceeds 98%", f_944["rest_to_remaining_ratio"] > 0.98)

    # 3. Electronic stopping power sensitivity
    t_stop_increased = t_stop_nominal / 1.30
    check("30% higher stopping reduces t_stop to ~0.846 ps", math.isclose(t_stop_increased, 1.1 / 1.3, rel_tol=1e-4))

    f_nominal = calculate_decay_fractions(1.38, 0.0, t_stop_nominal)
    f_increased = calculate_decay_fractions(1.38, 0.0, t_stop_increased)
    slowing_drop = (f_nominal["fraction_decay_while_slowing"] - f_increased["fraction_decay_while_slowing"]) / f_nominal["fraction_decay_while_slowing"]
    check("30% stopping increase reduces slowing fraction significantly", slowing_drop > 0.15)

    # 4. Transition quadrupole moment ratio shifts under 30% stopping sensitivity (half-correction chart)
    # When stopping power increases by 30%, correction is halved: tau_half = (tau_standard + tau_corr) / 2
    # Qt is proportional to 1 / sqrt(tau).
    # The relative change in Qt ratio for state pair (top / base) under half-chart vs adopted is:
    # factor = [c / ((t + c)/2)] / [v / ((u + v)/2)]
    # rel_change = sqrt(factor) - 1.0
    from fractions import Fraction as F
    t12, c12 = F('0.47'), F('0.59')
    u10, v10 = F('0.58'), F('0.71')
    factor_12_10 = (c12 / ((t12 + c12) / 2)) / (v10 / ((u10 + v10) / 2))
    pct_change_12_10 = (math.sqrt(float(factor_12_10)) - 1.0) * 100.0

    t8, c8 = F('0.85'), F('1.03')
    u6, v6 = F('1.38'), F('1.63')
    factor_8_6 = (c8 / ((t8 + c8) / 2)) / (v6 / ((u6 + v6) / 2))
    pct_change_8_6 = (math.sqrt(float(factor_8_6)) - 1.0) * 100.0

    check("12S1/10S1 Qt ratio increases by ~+0.56%", math.isclose(pct_change_12_10, 0.563123, rel_tol=1e-3))
    check("8g/6g Qt ratio increases by ~+0.58%", math.isclose(pct_change_8_6, 0.584053, rel_tol=1e-3))

    # 5. Direct vs indirect DDCM gate simulation
    tau_level = 2.0  # ps
    v_recoil = 4.796  # um/ps (beta = 0.016)
    ddcm_distances = [5.0, 10.0, 20.0, 50.0, 100.0]
    ddcm_curve = []
    for x in ddcm_distances:
        i_su = math.exp(-x / (v_recoil * tau_level))
        d_iss_dx = (1.0 / (v_recoil * tau_level)) * math.exp(-x / (v_recoil * tau_level))
        deduced_tau = i_su / (d_iss_dx * v_recoil)
        ddcm_curve.append({"distance_um": x, "deduced_tau_ps": deduced_tau})
        check(f"DDCM constant tau at x={x}um", math.isclose(deduced_tau, tau_level, rel_tol=1e-12))

    f_side = 0.20
    tau_side = 10.0
    side_feeding_curve = []
    for x in ddcm_distances:
        i_su_side = (1.0 - f_side) * math.exp(-x / (v_recoil * tau_level)) + f_side * math.exp(-x / (v_recoil * tau_side))
        d_iss_dx_side = (1.0 - f_side) * (1.0 / (v_recoil * tau_level)) * math.exp(-x / (v_recoil * tau_level)) + \
                        f_side * (1.0 / (v_recoil * tau_side)) * math.exp(-x / (v_recoil * tau_side))
        apparent_tau = i_su_side / (d_iss_dx_side * v_recoil)
        side_feeding_curve.append({
            "distance_um": x,
            "apparent_tau_ps": apparent_tau,
            "distortion_relative": apparent_tau / tau_level - 1.0,
        })

    check("Slow side feeding creates non-constant apparent tau(x)",
          side_feeding_curve[-1]["apparent_tau_ps"] > side_feeding_curve[0]["apparent_tau_ps"])
    check("Apparent tau exceeds true level tau due to slow feeder",
          all(pt["apparent_tau_ps"] > tau_level for pt in side_feeding_curve))

    result = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope": "Klemme 1999 Table I finite-stopping audit, deceleration fractions and Qt ratio sensitivity",
        "klemme_table1_corrected_states": correction_rows,
        "correction_ratio_extremes": {
            "min_ratio": min_ratio,
            "min_state": "6g_1",
            "max_ratio": max_ratio,
            "max_state": "12S1_1",
            "non_uniform_scale_verified": True,
        },
        "stopper_decay_fractions_grid": decay_fractions_grid,
        "stopping_power_sensitivity": {
            "t_stop_nominal_ps": t_stop_nominal,
            "t_stop_increased_ps": t_stop_increased,
            "tau_test_ps": 1.38,
            "slowing_fraction_nominal": f_nominal["fraction_decay_while_slowing"],
            "slowing_fraction_increased": f_increased["fraction_decay_while_slowing"],
            "relative_drop": slowing_drop,
        },
        "transition_quadrupole_ratio_shifts": {
            "pair_12S1_over_10S1": {
                "adopted_qt_ratio": math.sqrt(float(v10 / c12)),
                "half_chart_qt_ratio": math.sqrt(float(v10 / c12)) * math.sqrt(float(factor_12_10)),
                "percentage_change": pct_change_12_10,
            },
            "pair_8g_over_6g": {
                "adopted_qt_ratio": math.sqrt(float(v6 / c8)),
                "half_chart_qt_ratio": math.sqrt(float(v6 / c8)) * math.sqrt(float(factor_8_6)),
                "percentage_change": pct_change_8_6,
            },
        },
        "ddcm_ideal_vs_side_feeding": {
            "ideal_coincidence_curve": ddcm_curve,
            "unobserved_side_feeding_distortion": side_feeding_curve,
            "diagnostics_rule": "Flat tau(x) confirms feeder elimination; rising tau(x) indicates unobserved slow feeding",
        },
        "checks": checks,
        "check_count": len(checks),
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(f"Audit completed: {len(checks)} checks passed.")
    print(f"Correction ratio extremes: [{min_ratio:.4f}, {max_ratio:.4f}]")
    print(f"Qt ratio percentage shifts: 12S1/10S1: +{pct_change_12_10:.4f}%, 8g/6g: +{pct_change_8_6:.4f}%")


if __name__ == "__main__":
    main()
