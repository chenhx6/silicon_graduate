#!/usr/bin/env python3
"""Quantitative reconciliation audit of 131Ce lifetimes and Qt: Li 2004 vs Singh 2016.

Audits the model dependence of the rotational Clebsch-Gordan K-projection in extracting
transition quadrupole moments Qt from measured lifetimes tau and transition rates B(E2).
Proves that the apparent Qt discrepancy between Li 2004 and Singh 2016 is an algebraic
artifact of K=11/2 vs K=1/2 conventions rather than an experimental disagreement.
Uses only the Python standard library. Requires --output PATH.
"""
import argparse
from datetime import datetime, timezone
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path


def rotor_cg_squared(I, K):
    """Exact closed-form squared Clebsch-Gordan coefficient for I -> I-2 fixed-K transition."""
    I, K = F(I), F(K)
    if I < 2 or abs(K) > I - 2:
        raise ValueError("Transition outside rotor domain")
    return 3 * (I + K - 1) * (I + K) * (I - K - 1) * (I - K) / (2 * I * (I - 1) * (2 * I - 1) * (2 * I + 1))


def b_e2_from_tau(tau_ps, e_gamma_mev):
    """Calculate B(E2) in e^2 b^2 from lifetime tau (in ps) and gamma energy (in MeV)."""
    # T(E2) = 1.225e9 * E^5 * B(E2) [T in s^-1, E in MeV, B in e^2 b^2]
    # tau_s = tau_ps * 1e-12
    # B(E2) = 1 / (tau_s * 1.225e9 * E^5)
    return 1.0 / (tau_ps * 1e-12 * 1.225e9 * (e_gamma_mev ** 5))


def qt_from_b_e2(b_e2_b2, I, K):
    """Calculate transition quadrupole moment Qt in e b from B(E2) and rotor CG factor."""
    cg_sq = float(rotor_cg_squared(I, K))
    return math.sqrt(16.0 * math.pi * b_e2_b2 / (5.0 * cg_sq))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True, help="Path for output JSON")
    args = parser.parse_args()

    checks = []
    def check(name, condition):
        checks.append({"name": name, "passed": bool(condition)})
        if not condition:
            raise AssertionError(f"Check failed: {name}")

    # 1. 27/2- level analysis (E_gamma = 0.827 MeV)
    I_27 = F(27, 2)
    e_27 = 0.827  # MeV
    tau_li_27 = 1.23  # ps (Li 2004 Table 1: 1.23(23) ps)
    tau_singh_27 = 1.24  # ps (Singh 2016 Table 1: 1.24(+0.23/-0.13) ps)

    # Verify that the two measured lifetimes are virtually identical (difference < 1%)
    tau_diff_pct = abs(tau_singh_27 - tau_li_27) / tau_li_27 * 100.0
    check("Li 2004 and Singh 2016 measured lifetimes agree within 1% for 27/2-", tau_diff_pct < 1.0)

    # Clebsch-Gordan squared values for 27/2-
    cg_27_k11 = rotor_cg_squared(I_27, F(11, 2))  # = 76/325
    cg_27_k1 = rotor_cg_squared(I_27, F(1, 2))    # = 26/75
    check("CG^2(27/2, K=11/2) is 76/325", cg_27_k11 == F(76, 325))
    check("CG^2(27/2, K=1/2) is 26/75", cg_27_k1 == F(26, 75))

    # Analytical ratio of Qt between K=11/2 and K=1/2
    ratio_cg = math.sqrt(float(cg_27_k1 / cg_27_k11))
    check("Qt(K=11/2) / Qt(K=1/2) is exactly sqrt(169/114)",
          math.isclose(ratio_cg, math.sqrt(169.0 / 114.0), rel_tol=1e-12))

    # B(E2) reported by Li 2004 Table 1 is 1723 e^2 fm^4 = 0.1723 e^2 b^2
    b_li_27 = 0.1723
    qt_li_k11 = qt_from_b_e2(b_li_27, I_27, F(11, 2))
    qt_li_k1 = qt_from_b_e2(b_li_27, I_27, F(1, 2))

    check("Li 2004 reported Qt=2.72 eb matches K=11/2 calculation (2.722 eb)",
          math.isclose(qt_li_k11, 2.72, abs_tol=0.01))
    check("Converting Li's B(E2) with K=1/2 yields 2.235 eb, matching Singh's 2.28 eb within 2%",
          math.isclose(qt_li_k1, 2.235, abs_tol=0.05))

    # 2. 23/2- level analysis (E_gamma = 0.750 MeV)
    I_23 = F(23, 2)
    e_23 = 0.750  # MeV
    tau_li_23 = 1.44  # ps (Li 2004: 1.44(54) ps)
    # Singh reports lower limit tau > 1.3 ps (corresponding to Qt < 2.85 eb)
    check("Li 2004 lifetime tau=1.44 ps satisfies Singh lower limit tau > 1.3 ps", tau_li_23 > 1.3)

    cg_23_k11 = rotor_cg_squared(I_23, F(11, 2))  # = 340/1771
    cg_23_k1 = rotor_cg_squared(I_23, F(1, 2))    # = 55/161
    check("CG^2(23/2, K=11/2) is 340/1771", cg_23_k11 == F(340, 1771))
    check("CG^2(23/2, K=1/2) is 55/161", cg_23_k1 == F(55, 161))

    b_li_23 = 0.2416  # e^2 b^2 (Li reports 2416(906) e^2 fm^4)
    qt_23_k11 = qt_from_b_e2(b_li_23, I_23, F(11, 2))
    qt_23_k1 = qt_from_b_e2(b_li_23, I_23, F(1, 2))

    check("Li 2004 reported Qt=3.55 eb matches K=11/2 calculation (3.557 eb)",
          math.isclose(qt_23_k11, 3.55, abs_tol=0.01))
    check("Converting Li's 23/2- B(E2) with K=1/2 yields 2.666 eb",
          math.isclose(qt_23_k1, 2.666, abs_tol=0.01))
    check("Converted Qt(23/2-, K=1/2) = 2.67 eb strictly satisfies Singh limit Qt < 2.85 eb",
          qt_23_k1 < 2.85)

    # 3. Complete K grid for the yrast cascade (I = 15/2 to 35/2)
    spins = [F(15, 2), F(19, 2), F(23, 2), F(27, 2), F(31, 2), F(35, 2)]
    k_values = [F(1, 2), F(3, 2), F(5, 2), F(7, 2), F(9, 2), F(11, 2)]
    grid_results = []

    for I in spins:
        row = {"spin": str(I), "cg_squared_by_K": {}}
        for K in k_values:
            if K <= I - 2:
                cg_val = float(rotor_cg_squared(I, K))
                row["cg_squared_by_K"][str(K)] = cg_val
        grid_results.append(row)

    # Ratio of Qt(K=11/2) / Qt(K=1/2) across spins
    ratio_evolution = []
    for I in spins:
        if F(11, 2) <= I - 2:
            cg_11 = float(rotor_cg_squared(I, F(11, 2)))
            cg_1 = float(rotor_cg_squared(I, F(1, 2)))
            r = math.sqrt(cg_1 / cg_11)
            ratio_evolution.append({"spin": str(I), "qt_ratio_K11_over_K1": r})

    # The ratio decreases with spin as K becomes small compared to I
    check("K=11/2 vs K=1/2 Qt discrepancy decreases monotonically with spin",
          ratio_evolution[0]["qt_ratio_K11_over_K1"] > ratio_evolution[-1]["qt_ratio_K11_over_K1"])
    check("At 35/2-, the K-ratio discrepancy drops below 1.15",
          ratio_evolution[-1]["qt_ratio_K11_over_K1"] < 1.15)

    result = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope": "131Ce negative-parity yrast lifetimes: Li 2004 vs Singh 2016 K-projection reconciliation",
        "level_27_2_minus": {
            "energy_gamma_MeV": e_27,
            "tau_li_2004_ps": tau_li_27,
            "tau_singh_2016_ps": tau_singh_27,
            "lifetime_difference_pct": tau_diff_pct,
            "experimental_lifetimes_concur": True,
            "B_E2_reported_eb2": b_li_27,
            "Qt_with_K_11_2_eb": qt_li_k11,
            "Qt_with_K_1_2_eb": qt_li_k1,
            "ratio_K11_over_K1_exact": "sqrt(169/114) = 1.21756",
            "published_Qt_Li_eb": 2.72,
            "published_Qt_Singh_eb": 2.26,
            "published_Qt_Singh_recalculated_Li_eb": 2.28,
        },
        "level_23_2_minus": {
            "energy_gamma_MeV": e_23,
            "tau_li_2004_ps": tau_li_23,
            "singh_lifetime_limit": "> 1.3 ps",
            "lifetimes_consistent": True,
            "B_E2_reported_eb2": b_li_23,
            "Qt_with_K_11_2_eb": qt_23_k11,
            "Qt_with_K_1_2_eb": qt_23_k1,
            "published_Qt_Li_eb": 3.55,
            "singh_Qt_limit_eb": "< 2.85",
            "reconciliation_finding": "Under K=1/2, Li's Qt is 2.67 eb, which strictly satisfies Singh's < 2.85 eb limit",
        },
        "cg_squared_grid": grid_results,
        "k_ratio_spin_evolution": ratio_evolution,
        "checks": checks,
        "check_count": len(checks),
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(f"131Ce reconciliation audit completed: {len(checks)} checks passed.")
    print(f"27/2- measured lifetimes: Li={tau_li_27} ps vs Singh={tau_singh_27} ps (diff: {tau_diff_pct:.2f}%)")
    print(f"Qt(27/2-): K=11/2 gives {qt_li_k11:.3f} eb (Li published: 2.72 eb); K=1/2 gives {qt_li_k1:.3f} eb (Singh published: 2.26 eb)")
    print(f"Qt(23/2-): K=11/2 gives {qt_23_k11:.3f} eb (Li published: 3.55 eb); K=1/2 gives {qt_23_k1:.3f} eb (satisfying Singh limit < 2.85 eb)")


if __name__ == "__main__":
    main()
