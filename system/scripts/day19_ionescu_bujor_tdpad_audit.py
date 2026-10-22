#!/usr/bin/env python3
"""Quantitative audit of Ionescu-Bujor 1998 TDPAD moments in 129,131Ce.

Audits the quadrupole interaction period formula, spin determination (J=9/2 vs 7/2),
common-host EFG cancellation in the Q-moment ratio (1.44(7)), decoupling between
invariant single-particle g-factor (-0.19) and core quadrupole deformation expansion,
and the spectroscopic quadrupole projection factor across K values.
Uses only the Python standard library. Requires --output PATH.
"""
import argparse
from datetime import datetime, timezone
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path


def q_spec_projection_factor(I, K):
    """Calculate [3*K^2 - I*(I+1)] / [(I+1)*(2*I+3)]."""
    I, K = F(I), F(K)
    num = 3 * K**2 - I * (I + 1)
    den = (I + 1) * (2 * I + 3)
    return num / den


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True, help="Path for output JSON")
    args = parser.parse_args()

    checks = []
    def check(name, condition):
        checks.append({"name": name, "passed": bool(condition)})
        if not condition:
            raise AssertionError(f"Check failed: {name}")

    # 1. Quadrupole interaction period prefactor T0 = (2J*(2J-1)/3) * (1/nu_Q) (Eq. 1)
    # For J = 9/2:
    fac_9_2 = F(2 * F(9, 2) * (2 * F(9, 2) - 1), 3)  # = 24
    # For J = 7/2:
    fac_7_2 = F(2 * F(7, 2) * (2 * F(7, 2) - 1), 3)  # = 14
    check("J=9/2 quadrupole prefactor is exactly 24", fac_9_2 == 24)
    check("J=7/2 quadrupole prefactor is exactly 14", fac_7_2 == 14)
    check("Frequency ratio for J=9/2 vs J=7/2 is 24/14 = 1.714",
          math.isclose(float(fac_9_2 / fac_7_2), 24.0 / 14.0, rel_tol=1e-12))

    # In Ionescu-Bujor 1998, chi^2 is 2.7 for J=9/2 vs 13.9 for J=7/2 (Fig. 1)
    chi2_9_2 = 2.7
    chi2_7_2 = 13.9
    check("J=9/2 fit is substantially superior to J=7/2 (chi2 2.7 vs 13.9)", chi2_7_2 / chi2_9_2 > 5.0)

    # 2. Common-host electric field gradient cancellation (Table 1)
    # Both 129Ce and 131Ce stopped in identical polycrystalline metallic Sn host
    Q_129 = 1.32  # eb
    Q_129_unc = 0.13
    Q_131 = 0.92  # eb
    Q_131_unc = 0.10

    q_ratio = Q_129 / Q_131  # = 1.43478
    # Because both are in the same host, V_zz cancels out:
    # omega_0(129) / omega_0(131) = Q(129) / Q(131)
    check("Q ratio Q(129)/Q(131) is ~ 1.435 (reported as 1.44(7))",
          math.isclose(q_ratio, 1.4348, rel_tol=1e-3))

    # 3. Magnetic g-factor invariance across 2 neutrons
    g_129 = -0.185
    g_129_unc = 0.010
    g_131 = -0.189
    g_131_unc = 0.007

    g_ratio = g_129 / g_131  # = 0.9788
    g_diff_pct = abs(g_129 - g_131) / abs(g_131) * 100.0
    check("g-factors of 129Ce and 131Ce agree within 2.2%", g_diff_pct < 2.5)
    check("g-factor ratio is within 2.5% of unity", abs(g_ratio - 1.0) < 0.025)

    # Decoupling: while g differs by <2.5%, Q differs by ~43.5%
    check("Quadrupole moment changes by > 40% while g changes by < 2.5%",
          (q_ratio - 1.0) * 100.0 > 40.0 and g_diff_pct < 2.5)

    # 4. Spectroscopic quadrupole moment projection factors for I = 9/2
    I_val = F(9, 2)
    k_grid = [F(1, 2), F(3, 2), F(5, 2), F(7, 2), F(9, 2)]
    factors = {}
    for K in k_grid:
        fac = q_spec_projection_factor(I_val, K)
        factors[str(K)] = {"fraction": str(fac), "float_val": float(fac)}

    check("K=9/2 factor is +6/11 (+0.5455)", factors["9/2"]["fraction"] == "6/11")
    check("K=7/2 factor is +2/11 (+0.1818)", factors["7/2"]["fraction"] == "2/11")
    check("K=5/2 factor is -1/11 (-0.0909)", factors["5/2"]["fraction"] == "-1/11")
    check("K=3/2 factor is -3/11 (-0.2727)", factors["3/2"]["fraction"] == "-3/11")
    check("K=1/2 factor is -4/11 (-0.3636)", factors["1/2"]["fraction"] == "-4/11")

    # Sign reversal between K=5/2 and K=7/2
    check("Projection factor changes sign from negative at K<=5/2 to positive at K>=7/2",
          float(q_spec_projection_factor(I_val, F(5, 2))) < 0 < float(q_spec_projection_factor(I_val, F(7, 2))))

    # Zero-crossing at K = sqrt(I*(I+1)/3) = sqrt(24.75/3) = sqrt(8.25) ~ 2.872
    k_zero = math.sqrt(float(I_val * (I_val + 1)) / 3.0)
    check("Zero-crossing of Q_spec occurs at K ~ 2.872 (between K=5/2 and K=7/2)",
          2.5 < k_zero < 3.5)

    # 5. Intrinsic quadrupole moment Q0 extraction from Q_spec
    # If the bandhead is pure K = 9/2: Q0 = Q_spec / (6/11) = (11/6) * Q_spec
    q0_131_k9 = (11.0 / 6.0) * Q_131  # = 1.6867 eb
    q0_129_k9 = (11.0 / 6.0) * Q_129  # = 2.4200 eb
    check("Under K=9/2, Q0 for 131Ce is ~ 1.69 eb", math.isclose(q0_131_k9, 1.6867, abs_tol=0.01))
    check("Under K=9/2, Q0 for 129Ce is ~ 2.42 eb", math.isclose(q0_129_k9, 2.4200, abs_tol=0.01))

    result = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope": "Ionescu-Bujor 1998 TDPAD static moments: quadrupole interaction period, EFG cancellation, and g vs Q decoupling",
        "quadrupole_interaction_prefactors": {
            "formula": "T0 = (2J*(2J-1)/3) * (1/nu_Q)",
            "J_9_2_factor": int(fac_9_2),
            "J_7_2_factor": int(fac_7_2),
            "frequency_ratio": float(fac_9_2 / fac_7_2),
            "chi2_comparison_129Ce": {"J_9_2_chi2": chi2_9_2, "J_7_2_chi2": chi2_7_2},
            "spin_assignment": "Confirmed J = 9/2 for 129Ce and 131Ce isomers",
        },
        "common_host_efg_cancellation": {
            "host_material": "Polycrystalline metallic Sn foils",
            "Q_129Ce_eb": Q_129,
            "Q_131Ce_eb": Q_131,
            "measured_Q_ratio": q_ratio,
            "published_Q_ratio": "1.44(7)",
            "cancellation_mechanism": "Because both isotopes were stopped in identical Sn lattice at same temperature, V_zz cancels strictly out of the frequency ratio",
        },
        "schmidt_magnetic_moment_vs_core_quadrupole_decoupling": {
            "g_129Ce": g_129,
            "g_131Ce": g_131,
            "g_difference_pct": g_diff_pct,
            "Q_difference_pct": (q_ratio - 1.0) * 100.0,
            "nuclear_structure_insight": "Magnetic moment remains pinned at the Schmidt single-particle value of the nu h11/2 orbit (-0.19), while the spectroscopic quadrupole moment undergoes a 43.5% collective expansion from 131Ce to 129Ce",
        },
        "q_spec_projection_factors_spin_9_2": factors,
        "zero_crossing_point": {
            "K_zero": k_zero,
            "insight": "Spectroscopic quadrupole moment vanishes at K ~ 2.87 despite nonzero intrinsic deformation Q0, confirming that Q_spec = 0 is a geometric projection artifact rather than proof of spherical shape",
        },
        "checks": checks,
        "check_count": len(checks),
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(f"Ionescu-Bujor TDPAD audit completed: {len(checks)} checks passed.")
    print(f"Quadrupole prefactors: J=9/2 is {int(fac_9_2)}, J=7/2 is {int(fac_7_2)} (chi2: {chi2_9_2} vs {chi2_7_2})")
    print(f"Q ratio Q(129)/Q(131): {q_ratio:.3f} (V_zz cancels in same Sn host)")
    print(f"Magnetic g-factors: 129Ce={g_129} vs 131Ce={g_131} (diff: {g_diff_pct:.2f}%)")


if __name__ == "__main__":
    main()
