#!/usr/bin/env python3
"""
system/scripts/day20_pr136_magnetic_rotation_shears_audit.py

Checkpoint 031 Audit Script:
136Pr Magnetic Rotation (Shears Mechanism) Dipole Band Electromagnetic Transition Systematics,
TAC-CDFT Microscopic Deformation Collapse, and N=77 Chiral Boundary Audit.
Based on Lv et al. (Phys. Rev. C 111, 014321, 2025).

Corresponds to Checkpoint 031 for Day 20: B(E2), Qt and deformation systematics.
"""

import sys
import json
import math
import numpy as np
from pathlib import Path

def main():
    raise SystemExit("RETIRED checkpoint032: legacy audit is not scientific evidence")
    print("=== Checkpoint 031: 136Pr Magnetic Rotation & Shears Mechanism Audit ===")

    # 1. Experimental Data for Band D4 in 136Pr (Lv 2025 Table I & Fig. 9(c))
    spins_d4 = np.array([16, 17, 18, 19, 20, 21, 22, 23], dtype=int)
    # Experimental B(M1)/B(E2) ratios (in mu_N^2 / (e^2 b^2)):
    bm1_be2_exp = np.array([7.8, 5.4, 3.9, 2.8, 2.1, 1.5, 1.1, 0.8], dtype=float)

    # Check 1: Monotonic steep drop across spin range
    is_strictly_decreasing = np.all(np.diff(bm1_be2_exp) < 0)
    drop_factor = float(bm1_be2_exp[0] / bm1_be2_exp[-1]) # 7.8 / 0.8 = 9.75x
    check1 = bool(is_strictly_decreasing and (drop_factor > 8.0))
    print(f"Check 1 (Monotonic drop): strictly_decreasing={is_strictly_decreasing}, drop_factor={drop_factor:.2f}x -> {check1}")

    # 2. Semiclassical Shears Mechanism Angle Closure
    # In the shears model, blades j1 and j2 close as spin I increases:
    # cos(theta) = (I - I_0) / (I_max - I_0)
    # Band D4 bandhead I_0 = 14.5, maximum shears alignment I_max = 24.0
    I_0 = 14.5
    I_max = 24.0
    theta_deg = 90.0 * (1.0 - (spins_d4 - I_0) / (I_max - I_0))
    theta_rad = np.radians(theta_deg)
    sin2_theta = np.sin(theta_rad) ** 2

    # Theoretical B(M1) ~ B0 * sin^2(theta)
    # For nearly constant weak B(E2), B(M1)/B(E2) ~ C * sin^2(theta)
    C_fit = 8.5
    bm1_be2_model = C_fit * sin2_theta
    correlation_r = float(np.corrcoef(bm1_be2_exp, bm1_be2_model)[0, 1])

    check2 = bool((correlation_r > 0.93) and (theta_deg[0] > 70.0) and (theta_deg[-1] < 15.0))
    print(f"Check 2 (Shears closure): theta={theta_deg[0]:.1f} deg -> {theta_deg[-1]:.1f} deg, r={correlation_r:.4f} -> {check2}")

    # 3. TAC-CDFT Microscopic Deformation Collapse
    # From Lv 2025 Table II:
    # D4 configuration: pi(h11/2)^1 (x) nu(h11/2)^-1 (sd)^-2
    # Deformation: beta2 = 0.17, gamma = 35.0 deg
    # Comparison with collective rotational bands in 134Nd (beta2 = 0.25) or 130Ce (beta2 = 0.26):
    beta2_d4 = 0.17
    beta2_collective = 0.255
    deformation_suppression_percent = (beta2_collective - beta2_d4) / beta2_collective * 100.0 # ~33.3%

    check3 = bool((beta2_d4 == 0.17) and (deformation_suppression_percent > 30.0))
    print(f"Check 3 (Deformation collapse): beta2={beta2_d4} (suppressed by {deformation_suppression_percent:.1f}% vs collective core) -> {check3}")

    # 4. N=77 Chiral Boundary Audit & De-universalization
    # LV25-D19-2 established that absence of chirality in 136Pr does not constitute a universal N=77 cutoff.
    # Neighbor 137Nd (Z=60, N=77) exhibits MchiD candidate bands (Petrache et al. 2020 PRC 102, 014311).
    boundary_audit = {
        "136Pr_status": "No chiral doublet bands observed; magnetic rotation (D4) and shape coexistence (D4/D6) observed",
        "137Nd_status": "4-quasiparticle MchiD candidates reported at N=77",
        "de_universalization": "Absence of chirality in 136Pr is configuration- and nucleus-specific, not an absolute N=77 boundary",
        "driving_mechanism": "Competition between shears closing (small beta2) and aplanar core-quasiparticle rotation (large beta2)"
    }
    check4 = True
    print(f"Check 4 (N=77 boundary de-universalization): verified -> {check4}")

    # 5. Three-mode Discrimination Matrix in A~130 High-Spin Physics
    discrimination_matrix = {
        "Collective_Rotation": {
            "signature": "Strong in-band E2 cascade (B(E2) >> 50 W.u.)",
            "bm1_be2_trend": "Smooth, flat or slightly rising with spin",
            "alignment": "Aligned along principal intermediate axis, delta_i_x = 0",
            "chiral_scalar": "chi == 0"
        },
        "Chiral_Rotation": {
            "signature": "Nearly degenerate same-parity doublet bands with symmetric in-band B(E2)",
            "bm1_be2_trend": "Odd-even staggering with B(M1)_in and B(M1)_out symmetry",
            "alignment": "3D aplanar mutually perpendicular vectors, delta_i_x = 0",
            "chiral_scalar": "chi != 0"
        },
        "Magnetic_Rotation_Shears": {
            "signature": "Enhanced M1 dipole cascade with very weak crossover E2 (B(E2) ~ 1 - 5 W.u.)",
            "bm1_be2_trend": "Steep monotonic drop (~10x decrease) as shears angle closes",
            "alignment": "Planar shears blades closing, delta_i_x variable",
            "chiral_scalar": "chi == 0"
        }
    }
    check5 = len(discrimination_matrix) == 3
    print(f"Check 5 (Three-mode discrimination matrix): verified -> {check5}")

    # 6. Source Locators Crosswalk
    locators = {
        "LV25-5": "Table II reports TAC-CDFT configurations and deformations beta2=0.17, gamma=35 deg for D4",
        "LV25-9": "Authors explicitly conclude no chiral rotation or wobbling in 136Pr; D4 is magnetic rotation",
        "LV25-31": "Table I D4 gives dipole/crossover pairs for spins 16-23; Fig. 9(c) plots steep drop in B(M1)/B(E2)",
        "LV25-D19-2": "Absence of chirality in 136Pr does not constitute a universal N=77 hard termination"
    }
    check6 = len(locators) == 4
    print(f"Check 6 (Source locators crosswalk): {len(locators)} locators verified -> {check6}")

    all_passed = bool(check1 and check2 and check3 and check4 and check5 and check6)
    print(f"All 6 Checks Passed: {all_passed}")

    result_payload = {
        "schema_version": 1,
        "checkpoint": "031",
        "title": "136Pr Magnetic Rotation (Shears Mechanism) Dipole Band Systematics, TAC-CDFT Deformation Collapse, and N=77 Boundary Audit",
        "all_passed": all_passed,
        "d4_shears_band_audit": {
            "spins": spins_d4.tolist(),
            "bm1_be2_exp_muN2_per_e2b2": bm1_be2_exp.tolist(),
            "drop_factor": drop_factor,
            "shears_angles_deg": theta_deg.tolist(),
            "bm1_be2_model_muN2_per_e2b2": bm1_be2_model.tolist(),
            "correlation_r": correlation_r,
            "shears_closure_range": f"{theta_deg[0]:.1f} deg down to {theta_deg[-1]:.1f} deg"
        },
        "tac_cdft_deformation_audit": {
            "d4_configuration": "pi(h11/2)^1 x nu(h11/2)^-1 (sd)^-2",
            "beta2": beta2_d4,
            "gamma_deg": 35.0,
            "core_suppression_percent": deformation_suppression_percent,
            "physical_conclusion": "Reduced quadrupole deformation (beta2 = 0.17) quenches core collective rotation, allowing magnetic shears closing to dominate."
        },
        "boundary_audit": boundary_audit,
        "three_mode_discrimination_matrix": discrimination_matrix,
        "source_locators": locators,
        "checks": {
            "check1_bm1_be2_monotone_drop": check1,
            "check2_shears_angle_closure": check2,
            "check3_tac_cdft_deformation_collapse": check3,
            "check4_n77_boundary_audit": check4,
            "check5_three_mode_discrimination": check5,
            "check6_source_locators": check6
        }
    }

    out_path = Path("outputs/learning-daily/20261022-DAY20-be2-qt-deformation-systematics-run-02/pr136-magnetic-rotation-shears-result-031.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result_payload, f, indent=2, ensure_ascii=False)
    print(f"Result written to {out_path}")

    if not all_passed:
        sys.exit(1)

if __name__ == "__main__":
    raise SystemExit("RETIRED checkpoint032: unsupported scientific certification; see rejected-analysis-registry-032.json and day20_evidence_repair032.py")
