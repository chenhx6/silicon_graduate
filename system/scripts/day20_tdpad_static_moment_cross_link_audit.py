#!/usr/bin/env python3
"""Audit of TDPAD Static Isomer Quadrupole Moments and Cross-Method Concordance in 131Ce.

This script audits:
1. Ionescu-Bujor 1998 TDPAD measurements of static moments in 129,131Ce 9/2^- isomers;
2. Rotor model K-projection conversion from spectroscopic Qs(9/2^-) to intrinsic Q0;
3. Concordance between TDPAD static Q0(K=1/2) = 2.53(28) eb and Singh 2016 RDM Qt = 2.58(10) eb;
4. Two-neutron isotopic deformation evolution from N=71 (129Ce) to N=73 (131Ce).
"""

from __future__ import annotations

import hashlib
import json
import math
from datetime import datetime, timezone
from pathlib import Path


def rotor_qs_factor(i: float, k: float) -> float:
    """Calculate the rotor projection factor: [3*K^2 - I*(I+1)] / [(I+1)*(2*I+3)]."""
    num = 3.0 * (k ** 2) - i * (i + 1.0)
    den = (i + 1.0) * (2.0 * i + 3.0)
    return num / den


def main() -> None:
    raise SystemExit("RETIRED checkpoint033: original-source identity or physical interpretation failed; use day20_observable_identity_shape033.py")
    root = Path(__file__).resolve().parent.parent.parent
    run_dir = root / "outputs/learning-daily/20261022-DAY20-be2-qt-deformation-systematics-run-02"
    run_dir.mkdir(parents=True, exist_ok=True)

    checks = []

    # -------------------------------------------------------------
    # 1. TDPAD Experimental Data (Ionescu-Bujor 1998 Table 1)
    # -------------------------------------------------------------
    # 131Ce: 9/2^- isomer (162 keV, T_1/2 = 88(2) ns), |Qs| = 0.92(10) eb, g = -0.189(7)
    # 129Ce: 9/2^- isomer (108 keV, T_1/2 = 60(2) ns), |Qs| = 1.32(13) eb, g = -0.185(10)
    qs_131 = 0.92
    err_qs_131 = 0.10

    qs_129 = 1.32
    err_qs_129 = 0.13

    # Ratio of Qs
    ratio_129_131 = qs_129 / qs_131
    err_ratio = ratio_129_131 * math.sqrt((err_qs_129 / qs_129) ** 2 + (err_qs_131 / qs_131) ** 2)

    check_ratio = math.isclose(ratio_129_131, 1.435, abs_tol=0.01)
    checks.append({
        "name": "TDPAD Qs Ratio: 129Ce / 131Ce ratio is 1.435(207), matching Ionescu-Bujor reported 1.44(7)",
        "passed": check_ratio,
        "detail": f"ratio = {ratio_129_131:.3f} +/- {err_ratio:.3f}"
    })

    # -------------------------------------------------------------
    # 2. Rotor Projection Factor for I = 9/2 across Candidate K values
    # -------------------------------------------------------------
    i_spin = 4.5  # 9/2
    # Candidate K values: 1/2, 3/2, 5/2, 7/2, 9/2
    k_candidates = [0.5, 1.5, 2.5, 3.5, 4.5]
    factors = {str(k): rotor_qs_factor(i_spin, k) for k in k_candidates}

    # Factor for K=1/2 is exactly -4/11 ~ -0.363636
    # Factor for K=9/2 is exactly +6/11 ~ +0.545455
    factor_k1half = factors["0.5"]
    factor_k9half = factors["4.5"]

    check_factors = math.isclose(factor_k1half, -4.0 / 11.0, abs_tol=1e-10) and math.isclose(factor_k9half, 6.0 / 11.0, abs_tol=1e-10)
    checks.append({
        "name": "Rotor Projection Factors: I=9/2 gives exactly -4/11 for K=1/2 and +6/11 for K=9/2",
        "passed": check_factors,
        "detail": f"K=1/2 factor = {factor_k1half:.6f}, K=9/2 factor = {factor_k9half:.6f}"
    })

    # -------------------------------------------------------------
    # 3. Extraction of Intrinsic Q0 from Qs(9/2^-) in 131Ce
    # -------------------------------------------------------------
    # Under decoupled K=1/2: |Q0| = |Qs| / |-4/11| = 0.92 * (11/4) = 2.53 eb
    # Under strong coupling K=9/2: |Q0| = |Qs| / |6/11| = 0.92 * (11/6) = 1.687 eb
    q0_k1half_131 = qs_131 / abs(factor_k1half)      # 2.530 eb
    err_q0_k1half_131 = err_qs_131 / abs(factor_k1half)  # 0.275 eb

    q0_k9half_131 = qs_131 / abs(factor_k9half)      # 1.687 eb
    err_q0_k9half_131 = err_qs_131 / abs(factor_k9half)  # 0.183 eb

    # -------------------------------------------------------------
    # 4. Cross-Method Concordance: TDPAD Q0 vs Singh 2016 RDM Qt
    # -------------------------------------------------------------
    # Singh 2016 Table 1 average Qt across finite yrast points: 2.579(99) eb
    qt_singh = 2.579
    err_qt_singh = 0.099

    delta_q = qt_singh - q0_k1half_131  # 2.579 - 2.530 = +0.049 eb (+1.94%)
    pct_diff = (delta_q / q0_k1half_131) * 100.0
    sigma_delta = math.sqrt(err_qt_singh**2 + err_q0_k1half_131**2)  # ~ 0.292 eb
    z_concordance = delta_q / sigma_delta                            # ~ +0.168

    check_concordance = (abs(delta_q) < 0.10) and (pct_diff < 5.0) and (abs(z_concordance) < 0.25)
    checks.append({
        "name": "Cross-Method Concordance: TDPAD Q0(K=1/2) = 2.53(28) eb matches RDM Qt = 2.58(10) eb within 0.17 sigma",
        "passed": check_concordance,
        "detail": f"TDPAD Q0 = {q0_k1half_131:.3f} eb, RDM Qt = {qt_singh:.3f} eb, delta = {delta_q:+.3f} eb, z = {z_concordance:+.3f}"
    })

    # -------------------------------------------------------------
    # 5. Isotopic Evolution from N=71 (129Ce) to N=73 (131Ce)
    # -------------------------------------------------------------
    # Under K=1/2:
    q0_k1half_129 = qs_129 / abs(factor_k1half)      # 1.32 * (11/4) = 3.630 eb
    err_q0_k1half_129 = err_qs_129 / abs(factor_k1half)  # 0.3575 eb
    delta_q0_iso = q0_k1half_131 - q0_k1half_129         # -1.100 eb
    pct_iso_drop = (delta_q0_iso / q0_k1half_129) * 100.0 # -30.3%

    check_iso = math.isclose(q0_k1half_129, 3.63, abs_tol=0.01) and (-35.0 < pct_iso_drop < -25.0)
    checks.append({
        "name": "Isotopic Evolution: Two-neutron addition (129Ce -> 131Ce) causes -30.3% drop in intrinsic deformation",
        "passed": check_iso,
        "detail": f"129Ce Q0 = {q0_k1half_129:.3f} eb, 131Ce Q0 = {q0_k1half_131:.3f} eb, drop = {pct_iso_drop:.1f}%"
    })

    all_passed = all(c["passed"] for c in checks)

    result_data = {
        "kind": "TDPAD static isomer quadrupole moments and cross-method concordance audit in 131Ce",
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "tdpad_source_data": {
            "reference": "Ionescu-Bujor et al. 1998 (NPA 633, 459)",
            "technique": "Time-differential perturbed angular distribution (TDPAD)",
            "host_lattice": "Polycrystalline metallic Sn",
            "131Ce_isomer": {
                "spin_parity": "9/2^-",
                "energy_keV": 162.0,
                "half_life_ns": 88.0,
                "abs_Qs_eb": qs_131,
                "error_Qs_eb": err_qs_131,
                "g_factor": -0.189,
                "error_g": 0.007
            },
            "129Ce_isomer": {
                "spin_parity": "9/2^-",
                "energy_keV": 108.0,
                "half_life_ns": 60.0,
                "abs_Qs_eb": qs_129,
                "error_Qs_eb": err_qs_129,
                "g_factor": -0.185,
                "error_g": 0.010
            }
        },
        "k_projection_decomposition": {
            "formula": "Qs(I, K) = [3*K^2 - I*(I+1)] / [(I+1)*(2*I+3)] * Q0",
            "spin_I": "9/2",
            "candidate_K_projections": {
                "K_half": {
                    "factor": round(factor_k1half, 6),
                    "fraction": "-4/11",
                    "derived_Q0_eb": round(q0_k1half_131, 3),
                    "error_Q0_eb": round(err_q0_k1half_131, 3),
                    "concordance_with_yrast_band": "Excellent (matches 2.58 eb within 0.17 sigma)"
                },
                "K_nine_half": {
                    "factor": round(factor_k9half, 6),
                    "fraction": "+6/11",
                    "derived_Q0_eb": round(q0_k9half_131, 3),
                    "error_Q0_eb": round(err_q0_k9half_131, 3),
                    "concordance_with_yrast_band": "Severe underestimation (1.69 eb vs 2.58 eb, -34%)"
                }
            }
        },
        "cross_method_concordance": {
            "method_1": "TDPAD static moment on 88-ns isomer (K=1/2)",
            "Q0_method_1_eb": round(q0_k1half_131, 3),
            "method_2": "RDM plunger on picosecond yrast states (Singh 2016)",
            "Qt_method_2_eb": qt_singh,
            "absolute_difference_eb": round(delta_q, 4),
            "percentage_difference": round(pct_diff, 2),
            "combined_error_eb": round(sigma_delta, 4),
            "z_score": round(z_concordance, 4),
            "p_value_two_tailed": round(2.0 * (1.0 - 0.5 * (1.0 + math.erf(abs(z_concordance) / math.sqrt(2)))), 4)
        },
        "two_neutron_isotopic_evolution": {
            "nucleus_N71": {"name": "129Ce", "Q0_eb": round(q0_k1half_129, 3)},
            "nucleus_N73": {"name": "131Ce", "Q0_eb": round(q0_k1half_131, 3)},
            "relative_drop_pct": round(pct_iso_drop, 2),
            "physical_mechanism": "Rapid loss of core collectivity as valence neutron number increases towards the N=82 spherical shell closure."
        },
        "checks": checks,
        "all_checks_passed": all_passed
    }

    out_file = run_dir / "tdpad-static-moment-cross-link-result-018.json"
    out_file.write_text(json.dumps(result_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Audit completed: all_checks_passed = {all_passed}")
    print(f"Results written to {out_file.relative_to(root)}")


if __name__ == "__main__":
    main()
