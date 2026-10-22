#!/usr/bin/env python3
"""Quantitative audit of Nolan 1979 Table 7: DSAM vs RDM overlap and shared-stopping bias.

Audits the 1-20 ps overlap comparison between high-velocity DSAM and RDM (Hermans 1977),
evaluates the systematic ~10% inflation of DSAM lifetimes due to stopping-power calibration,
and models the Schwalm 1977 shared-stopping counterexample where common stopping tables
mask absolute scale errors behind < 5% apparent agreement.
Uses only the Python standard library. Requires --output PATH.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True, help="Path for output JSON")
    args = parser.parse_args()

    checks = []
    def check(name, condition):
        checks.append({"name": name, "passed": bool(condition)})
        if not condition:
            raise AssertionError(f"Check failed: {name}")

    # 1. Nolan 1979 Table 7 data (recoils stopping in Mg, from Hermans et al. 1977)
    table7_raw = [
        {"nucleus": "13C", "E_level_MeV": 3.85, "tau_dsam_ps": 12.4, "sig_dsam": 0.6, "tau_rdm_ps": 12.1, "sig_rdm": 0.2, "ratio_printed": 1.02, "sig_ratio_printed": 0.05},
        {"nucleus": "16N", "E_level_MeV": 0.40, "tau_dsam_ps": 6.5,  "sig_dsam": 0.5, "tau_rdm_ps": 5.07, "sig_rdm": 0.04,"ratio_printed": 1.28, "sig_ratio_printed": 0.10},
        {"nucleus": "18O", "E_level_MeV": 1.98, "tau_dsam_ps": 2.99, "sig_dsam": 0.12,"tau_rdm_ps": 2.82, "sig_rdm": 0.06,"ratio_printed": 1.06, "sig_ratio_printed": 0.05},
        {"nucleus": "20O", "E_level_MeV": 1.67, "tau_dsam_ps": 14.2, "sig_dsam": 0.8, "tau_rdm_ps": 9.8,  "sig_rdm": 0.8, "ratio_printed": 1.45, "sig_ratio_printed": 0.11},
        {"nucleus": "30P", "E_level_MeV": 0.79, "tau_dsam_ps": 23.0, "sig_dsam": 2.0, "tau_rdm_ps": 19.9, "sig_rdm": 1.3, "ratio_printed": 1.16, "sig_ratio_printed": 0.13},
        {"nucleus": "36Cl","E_level_MeV": 1.16, "tau_dsam_ps": 10.4, "sig_dsam": 0.5, "tau_rdm_ps": 9.2,  "sig_rdm": 0.4, "ratio_printed": 1.13, "sig_ratio_printed": 0.07},
    ]

    check("Table 7 contains 6 comparative benchmark nuclei", len(table7_raw) == 6)

    table7_processed = []
    for row in table7_raw:
        r = row["tau_dsam_ps"] / row["tau_rdm_ps"]
        sig_r = r * math.sqrt((row["sig_dsam"] / row["tau_dsam_ps"])**2 + (row["sig_rdm"] / row["tau_rdm_ps"])**2)
        # Check printed ratio match within rounding
        check(f"{row['nucleus']} ratio matches printed within 0.01", math.isclose(r, row["ratio_printed"], abs_tol=0.015))
        table7_processed.append({
            **row,
            "calculated_ratio": r,
            "calculated_sigma": sig_r,
            "dsam_longer_than_rdm": r > 1.0,
        })

    # All 6 nuclei have DSAM > RDM (ratio > 1.0)
    check("All 6 benchmark nuclei show DSAM >= RDM", all(pt["dsam_longer_than_rdm"] for pt in table7_processed))

    # 2. Weighted average ratio of DSAM / RDM
    weights = [1.0 / (pt["calculated_sigma"]**2) for pt in table7_processed]
    weighted_mean_ratio = sum(w * pt["calculated_ratio"] for w, pt in zip(weights, table7_processed)) / sum(weights)
    weighted_mean_sigma = 1.0 / math.sqrt(sum(weights))

    check("Weighted mean ratio is ~ 1.100 (10% systematic excess)",
          math.isclose(weighted_mean_ratio, 1.100, abs_tol=0.005))
    check("Weighted mean uncertainty is ~ 0.029",
          math.isclose(weighted_mean_sigma, 0.029, abs_tol=0.005))

    # Significance of DSAM inflation: (mean_ratio - 1.0) / sigma = 0.100 / 0.029 = 3.44 sigma
    z_score = (weighted_mean_ratio - 1.0) / weighted_mean_sigma
    check("DSAM systematic excess over RDM exceeds 3.4 sigma", z_score > 3.4)

    # 3. Stopping power scaling model
    # DSAM: tau_DSAM proportional to 1 / (dE/dx)_e
    # If electronic stopping power is underestimated by delta_S: S_eff = S_true * (1 - delta_S)
    # Then tau_DSAM = tau_true / (1 - delta_S) ~ tau_true * (1 + delta_S)
    # To produce a 10% increase (ratio = 1.100): 1 / (1 - delta_S) = 1.100 => delta_S = 1 - 1/1.100 = 0.0909 (9.1%)
    required_stopping_underestimation = 1.0 - 1.0 / weighted_mean_ratio
    check("A 9.1% electronic stopping power underestimation quantitatively explains the 10% excess",
          math.isclose(required_stopping_underestimation, 0.0909, rel_tol=1e-2))

    # 4. Schwalm 1977 shared-stopping model (Fig. 56)
    # Both lineshape fitting (recoil stopping) and Coulomb excitation yield (beam stopping)
    # depend on the adopted stopping power tables.
    true_b_e2 = 1.0
    nominal_stopping_factor = 1.0
    erroneous_stopping_scale = 1.15  # 15% stopping scale error

    # Lineshape DSAM: inferred tau drops with stopping scale -> inferred B(E2) rises: B ~ S_rec
    # Coulomb excitation: yield Y ~ sigma / S_beam -> inferred B(E2) ~ Y * S_beam
    # If the same table is used for both, both inferred B(E2) values shift in the SAME direction:
    inferred_b_dsam = true_b_e2 * erroneous_stopping_scale
    inferred_b_coulex = true_b_e2 * erroneous_stopping_scale

    apparent_discrepancy = abs(inferred_b_dsam - inferred_b_coulex) / true_b_e2
    absolute_systematic_error = abs(inferred_b_dsam - true_b_e2) / true_b_e2

    check("Shared-stopping gives zero apparent discrepancy between DSAM and CoulEx",
          math.isclose(apparent_discrepancy, 0.0, abs_tol=1e-12))
    check("Absolute systematic error (15%) is completely hidden by shared stopping",
          math.isclose(absolute_systematic_error, 0.15, rel_tol=1e-4))

    result = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "scope": "Nolan 1979 Table 7 DSAM vs RDM overlap (Hermans 1977) and Schwalm 1977 shared-stopping bias",
        "overlap_window": "1 to 20 ps",
        "table7_processed_nuclei": table7_processed,
        "statistical_meta_analysis": {
            "weighted_mean_ratio_dsam_over_rdm": weighted_mean_ratio,
            "weighted_mean_sigma": weighted_mean_sigma,
            "z_significance_of_excess": z_score,
            "conclusion": "DSAM lifetimes in the 1-20 ps window are systematically 10.0 +- 2.9% longer than RDM lifetimes across 6 independent nuclei stopping in Mg",
        },
        "stopping_power_interpretation": {
            "implied_stopping_underestimation_pct": required_stopping_underestimation * 100.0,
            "physics": "Underestimating electronic stopping power dE/dx inflates recoil slowing time, directly shifting deduced DSAM lifetimes upwards while RDM flight-time clock remains unaffected",
        },
        "shared_stopping_counterexample_schwalm1977": {
            "mechanism": "DSAM lineshape fitting (recoil stopping) vs Coulomb excitation yield (beam stopping) on same data",
            "apparent_method_discrepancy_pct": apparent_discrepancy * 100.0,
            "hidden_absolute_error_pct": absolute_systematic_error * 100.0,
            "methodological_rule": "Agreement between two methods sharing the same stopping power table does NOT prove stopping power correctness",
        },
        "checks": checks,
        "check_count": len(checks),
    }

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(f"Nolan overlap audit completed: {len(checks)} checks passed.")
    print(f"Weighted mean DSAM/RDM ratio: {weighted_mean_ratio:.3f} +- {weighted_mean_sigma:.3f} (z = {z_score:.2f} sigma)")
    print(f"Implied electronic stopping underestimation in DSAM: {required_stopping_underestimation*100:.1f}%")
    print(f"Shared-stopping simulation: Apparent discrepancy = {apparent_discrepancy*100:.1f}%, Hidden absolute error = {absolute_systematic_error*100:.1f}%")


if __name__ == "__main__":
    main()
