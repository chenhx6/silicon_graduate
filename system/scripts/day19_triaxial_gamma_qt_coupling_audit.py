#!/usr/bin/env python3
"""Quantitative audit of triaxiality gamma-coupling in transition quadrupole moments Qt.

Models the exact algebraic dependence of Qt on triaxiality parameter gamma (Matev 2007 Eq. 15):
Qt(gamma) = Q2 * [cos(gamma) - (1/sqrt(3))*sin(gamma)] = Q2 * (2/sqrt(3)) * cos(gamma + 30 deg).
Audits the 42.3% suppression at maximum triaxiality (gamma = 30 deg), non-collective extinction
at gamma = 60 deg, and the systematic underestimation of beta2 when an axial shape is assumed.
Uses only the Python standard library. Requires --output PATH.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path


def qt_over_q2(gamma_deg):
    """Calculate Qt / Q2 for rotation about the intermediate axis (y-cranking)."""
    rad = math.radians(gamma_deg + 30.0)
    return (2.0 / math.sqrt(3.0)) * math.cos(rad)


def calculate_beta2_from_q2(q2_eb, z=60, a=134, r0_fm=1.25, c2=0.16):
    """Convert quadrupole deformation magnitude Q2 to beta2."""
    r0 = r0_fm * (a ** (1.0 / 3.0))
    prefactor = (3.0 / math.sqrt(5.0 * math.pi)) * z * (r0 ** 2) * 0.01  # eb
    discriminant = 1.0 + 4.0 * c2 * (q2_eb / prefactor)
    return (-1.0 + math.sqrt(discriminant)) / (2.0 * c2)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True, help="Path for output JSON")
    args = parser.parse_args()

    checks = []
    def check(name, condition):
        checks.append({"name": name, "passed": bool(condition)})
        if not condition:
            raise AssertionError(f"Check failed: {name}")

    # 1. Algebraic landmarks across the gamma domain [-60 deg, +60 deg]
    # Landmark A: gamma = -30 deg (maximum enhancement)
    qt_m30 = qt_over_q2(-30.0)
    check("At gamma = -30 deg, Qt/Q2 is exactly 2/sqrt(3) ~ 1.1547",
          math.isclose(qt_m30, 2.0 / math.sqrt(3.0), rel_tol=1e-12))

    # Landmark B: gamma = 0 deg (axial prolate collective rotation)
    qt_0 = qt_over_q2(0.0)
    check("At gamma = 0 deg, Qt/Q2 is strictly 1.0000",
          math.isclose(qt_0, 1.0, abs_tol=1e-12))

    # Landmark C: gamma = +30 deg (maximum triaxiality)
    qt_30 = qt_over_q2(30.0)
    check("At gamma = +30 deg, Qt/Q2 is exactly 1/sqrt(3) ~ 0.5774",
          math.isclose(qt_30, 1.0 / math.sqrt(3.0), rel_tol=1e-12))
    check("Maximum triaxiality suppresses Qt by 42.3% at constant Q2",
          math.isclose(1.0 - qt_30, 0.42265, rel_tol=1e-3))
    check("Maximum triaxiality suppresses B(E2) by factor 3 (B/B_ax = 1/3)",
          math.isclose(qt_30 ** 2, 1.0 / 3.0, rel_tol=1e-12))

    # Landmark D: gamma = +60 deg (axial oblate non-collective rotation)
    qt_60 = qt_over_q2(60.0)
    check("At gamma = +60 deg, Qt/Q2 is strictly zero (collective E2 extinction)",
          math.isclose(qt_60, 0.0, abs_tol=1e-12))

    # 2. Grid evaluation from -30 deg to +60 deg
    gamma_grid = [-30, -25, -20, -15, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
    grid_results = []
    for g in gamma_grid:
        val = qt_over_q2(g)
        be2_ratio = val ** 2
        # Underestimation of Q2 if axial prolate (gamma=0, Qt=Q2) is assumed:
        # Q2_true = Qt / val = Q2_assumed / val => Q2_true is larger than Q2_assumed when val < 1
        underest_pct = ((1.0 / val) - 1.0) * 100.0 if val > 0 else float("inf")
        grid_results.append({
            "gamma_deg": g,
            "qt_over_q2": val,
            "be2_over_be2_axial": be2_ratio,
            "q2_underestimation_if_axial_assumed_pct": underest_pct,
        })

    # Assertions on realistic triaxial region in A ~ 130 (gamma = 20 to 25 deg)
    pt_20 = next(pt for pt in grid_results if pt["gamma_deg"] == 20)
    pt_25 = next(pt for pt in grid_results if pt["gamma_deg"] == 25)

    check("At gamma = 20 deg, Qt/Q2 is ~ 0.742 (25.8% drop)", math.isclose(pt_20["qt_over_q2"], 0.7422, abs_tol=0.005))
    check("At gamma = 25 deg, Qt/Q2 is ~ 0.662 (33.8% drop)", math.isclose(pt_25["qt_over_q2"], 0.6623, abs_tol=0.005))
    check("At gamma = 25 deg, assuming axial prolate understates true Q2 by ~ 51.0%",
          math.isclose(pt_25["q2_underestimation_if_axial_assumed_pct"], 50.988, rel_tol=1e-2))

    # 3. Non-uniqueness and deformation degeneracy at fixed Qt = 5.0 eb
    # A single measured Qt = 5.0 eb can correspond to different (beta2, gamma) pairs
    qt_target = 5.0  # eb
    hypothetical_pairs = []
    test_gammas = [-30, -20, 0, 15, 25, 30]

    for g in test_gammas:
        ratio = qt_over_q2(g)
        q2_true = qt_target / ratio
        beta2_true = calculate_beta2_from_q2(q2_true)
        hypothetical_pairs.append({
            "gamma_deg": g,
            "required_Q2_eb": q2_true,
            "required_beta2": beta2_true,
        })

    check("Fixed Qt=5.0 eb spans required beta2 from 0.22 to 0.44 across gamma",
          hypothetical_pairs[0]["required_beta2"] < 0.23 and hypothetical_pairs[-1]["required_beta2"] > 0.43)
    check("At gamma = 30 deg, required beta2 is > 1.7x larger than at gamma = -30 deg",
          hypothetical_pairs[-1]["required_beta2"] / hypothetical_pairs[0]["required_beta2"] > 1.7)

    result = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope": "Triaxiality gamma-coupling in transition quadrupole moment Qt (Matev 2007 Eq. 15)",
        "formula": "Qt(gamma) = Q2 * [cos(gamma) - (1/sqrt(3))*sin(gamma)] = Q2 * (2/sqrt(3)) * cos(gamma + 30 deg)",
        "landmarks": {
            "maximum_enhancement": {"gamma_deg": -30, "Qt_over_Q2": qt_m30, "ratio": "2/sqrt(3) = 1.1547"},
            "axial_prolate_baseline": {"gamma_deg": 0, "Qt_over_Q2": qt_0, "ratio": "1.0000"},
            "maximum_triaxiality": {"gamma_deg": 30, "Qt_over_Q2": qt_30, "ratio": "1/sqrt(3) = 0.5774", "suppression_pct": 42.27},
            "oblate_noncollective_extinction": {"gamma_deg": 60, "Qt_over_Q2": qt_60, "ratio": "0.0000", "note": "Collective E2 vanishes"},
        },
        "gamma_grid_evaluation": grid_results,
        "fixed_Qt_degeneracy_study": {
            "target_Qt_eb": qt_target,
            "degenerate_pairs": hypothetical_pairs,
            "conclusion": "A single measured Qt cannot uniquely determine deformation; assuming axial prolate (gamma=0) underestimates true beta2 by up to 40-50% in triaxial nuclei",
        },
        "checks": checks,
        "check_count": len(checks),
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(f"Triaxial gamma-coupling audit completed: {len(checks)} checks passed.")
    print(f"Landmarks: gamma=-30 deg -> {qt_m30:.4f}, 0 deg -> {qt_0:.4f}, 30 deg -> {qt_30:.4f}, 60 deg -> {qt_60:.4f}")
    print(f"At gamma=25 deg: Qt/Q2 = {pt_25['qt_over_q2']:.4f} (-33.8% drop; Q2 underestimated by +{pt_25['q2_underestimation_if_axial_assumed_pct']:.1f}% if axial assumed).")


if __name__ == "__main__":
    main()
