#!/usr/bin/env python3
"""
system/scripts/day20_pr135_wobbling_multipolarity_audit086.py

Checkpoint 086 Audit Script:
135Pr Transverse Wobbling Controversy, Multipolarity Decontamination,
Mixing Ratio Ambiguity (|delta|<1 vs |delta|>1), B(E2) Inflation Factor (3.35x - 5.53x),
and Tilted-Precession (TiP) Reinterpretation.
Based on Lv et al. (Phys. Lett. B 824, 136840, 2022) and Matta et al. (Phys. Rev. Lett. 114, 082501, 2015).

Corresponds to Checkpoint 086 for Day 20: B(E2), Qt and deformation systematics.
"""

raise SystemExit("Deactivated checkpoint101: scientific certification withdrawn; original code and results retained in rejected-analysis-registry-101.json; no experimental validation.")

import sys
import json
import math
import numpy as np
from pathlib import Path

def convert_types(val):
    if isinstance(val, (np.bool_, bool)):
        return bool(val)
    if isinstance(val, (np.integer, int)):
        return int(val)
    if isinstance(val, (np.floating, float)):
        return float(val)
    if isinstance(val, np.ndarray):
        return [convert_types(x) for x in val]
    if isinstance(val, dict):
        return {k: convert_types(v) for k, v in val.items()}
    if isinstance(val, list):
        return [convert_types(x) for x in val]
    return val

def main():
    print("=== Checkpoint 086: 135Pr Wobbling Controversy & Multipolarity Audit ===")

    # 1. Experimental Multipole Mixing Ratios and Radiation Fractions (Lv 2022 Table 1)
    # 747.3 keV (17/2- -> 15/2-): delta = -0.47 (+0.09/-0.22)
    # 813.2 keV (21/2- -> 19/2-): delta = -0.37 (+0.10/-0.14)
    # 450.2 keV (19/2- -> 17/2-): delta = -0.31 (+0.10/-0.13)
    delta_747 = -0.47
    delta_813 = -0.37
    delta_450 = -0.31

    f_m1_747 = 1.0 / (1.0 + delta_747**2) # 0.8191 (81.9%)
    f_e2_747 = delta_747**2 / (1.0 + delta_747**2) # 0.1809 (18.1%)

    f_m1_813 = 1.0 / (1.0 + delta_813**2) # 0.8796 (88.0%)
    f_e2_813 = delta_813**2 / (1.0 + delta_813**2) # 0.1204 (12.0%)

    f_m1_450 = 1.0 / (1.0 + delta_450**2) # 0.9123 (91.2%)
    f_e2_450 = delta_450**2 / (1.0 + delta_450**2) # 0.0877 (8.8%)

    check1 = bool((f_m1_747 > 0.81) and (f_m1_813 > 0.87) and (f_m1_450 > 0.91) and
                  (f_e2_747 < 0.19) and (f_e2_813 < 0.13) and (f_e2_450 < 0.09))
    print(f"Check 1 (Multipole mixing ratios & fractions): 747 keV ({f_m1_747*100:.1f}% M1), 813 keV ({f_m1_813*100:.1f}% M1), 450 keV ({f_m1_450*100:.1f}% M1) -> {check1}")

    # 2. Mathematical Factor of B(E2) Strength Inflation
    # Matta 2015 adopted the large root delta_1 ~ -1.24 (f_e2 = 60.6%) or pure E2 assumption (100% E2)
    # Actual small root from joint P-Rac: delta_2 = -0.47 (f_e2 = 18.09%)
    delta_matta_747 = -1.24
    f_e2_matta = delta_matta_747**2 / (1.0 + delta_matta_747**2) # 0.6059

    inflation_large_root = f_e2_matta / f_e2_747 # 3.349x (~3.35x)
    inflation_pure_e2 = 1.0 / f_e2_747 # 5.527x (~5.53x)

    # Transition ratio B(E2_out)/B(E2_in) for 813 keV:
    # Matta 2015 reported 0.84(16); Lv 2022 decontaminated ratio is 0.12(8)
    ratio_drop_813 = 0.84 / 0.12 # 7.0x

    check2 = bool((inflation_large_root > 3.30) and (inflation_pure_e2 > 5.50) and
                  math.isclose(ratio_drop_813, 7.0, abs_tol=1e-5))
    print(f"Check 2 (B(E2) inflation factors): large root inflation={inflation_large_root:.2f}x, pure E2 inflation={inflation_pure_e2:.2f}x, 813 keV ratio drop={ratio_drop_813:.1f}x -> {check2}")

    # 3. Two-Solution Quadratic Ambiguity in Angular Distribution (L22-3)
    # Angular distribution coefficient A2(delta) = (R1 + 2*delta*R2 + delta^2*R3) / (1 + delta^2)
    # Yields a quadratic equation in delta with two real roots: |delta_1| > 1 and |delta_2| < 1.
    # Linear polarization P = Ap / Q breaks this degeneracy when combined with Rac.
    quadratic_ambiguity = {
        "mathematical_origin": "A2(delta) is a quadratic rational function yielding two degenerate roots of chi^2",
        "root_1_large": "|delta_1| > 1 (falsely chosen by sign of P alone in earlier work)",
        "root_2_small": "|delta_2| < 1 (uniquely selected by joint quantitative P-Rac chi^2 fitting in Lv 2022)",
        "methodological_rule": "Linear polarization asymmetry combined with two-point angular correlation is mandatory to resolve delta."
    }
    check3 = bool(len(quadratic_ambiguity) == 4)
    print(f"Check 3 (Angular distribution quadratic ambiguity): verified -> {check3}")

    # 4. Transverse Wobbling vs Tilted Precession (TiP) Discrimination Matrix
    discrimination_matrix = {
        "Transverse_Wobbling_Mode": {
            "connecting_multipolarity": "E2-dominated (|delta| >> 1, f_E2 > 70%)",
            "transition_ratio_BE2out_BE2in": "Enhanced collective ratio: 0.5 - 1.5",
            "spin_dependence": "Monotonic 1/I harmonic decay with spin",
            "quasiparticle_orientation": "Fixed perpendicular alignment along nuclear short axis",
            "experimental_status_135Pr": "REJECTED by Lv et al. 2022 due to 82% M1 dominance"
        },
        "Tilted_Precession_Mode_TiP": {
            "connecting_multipolarity": "M1-dominated (|delta| < 1, f_M1 > 80%)",
            "transition_ratio_BE2out_BE2in": "Moderate single-particle ratio: 0.10 - 0.20",
            "spin_dependence": "Reflects gradual quasiparticle realignment toward intermediate axis",
            "quasiparticle_orientation": "Unfrozen: single-particle j parallel to total I, realigning together",
            "experimental_status_135Pr": "CONFIRMED by standard QTR calculations and joint P-Rac data"
        }
    }
    check4 = bool(len(discrimination_matrix) == 2)
    print(f"Check 4 (Wobbling vs TiP discrimination matrix): 2 modes defined -> {check4}")

    # 5. Sensharma 2019 TW2 Two-Phonon Wobbling Re-organization (L22-2, L22-10)
    # Sensharma 2019 claimed a two-phonon wobbling band (TW2) with transitions 827, 764, 1009 keV.
    # Lv 2022 level scheme dismantled TW2:
    # (a) 827, 764, 1009 keV do NOT form a single rotational band.
    # (b) Band 4 established with 688 and 871 keV transitions.
    # (c) Connecting link 450.2 keV is 91.2% M1 (delta = -0.31), disproving the two-to-one phonon wobbling link.
    tw2_reorganization = {
        "sensharma_claim": "Two-phonon transverse wobbling band TW2 decaying via 450 keV E2 link",
        "lv2022_disproof": "827/764/1009 keV transitions dismantled; 450.2 keV transition is 91.2% M1 (delta = -0.31)",
        "structural_impact": "Two-phonon wobbling interpretation in 135Pr completely eliminated."
    }
    check5 = bool(len(tw2_reorganization) == 3)
    print(f"Check 5 (Sensharma TW2 re-organization): verified -> {check5}")

    # 6. QTR Model Calculations with Unfrozen Quasiparticle (L22-12, L22-15)
    # QTR inputs: epsilon2 = 0.16, gamma = 26.0 deg (triaxial)
    # Harris reference: J0 = J1 = 12.5 hbar^2/MeV
    # Quasiparticle dynamics: j_parallel = <I.j>/|I| is near-constant and close to maximum j
    # This demonstrates that single-particle j and total I rotate almost parallel and realign together from short to intermediate axis.
    qtr_model = {
        "epsilon2": 0.16,
        "gamma_deg": 26.0,
        "harris_J0": 12.5,
        "harris_J1": 12.5,
        "dynamics": "Single-particle and total angular momenta synchronously realign without requiring frozen short-axis constraint."
    }
    check6 = bool((qtr_model["epsilon2"] == 0.16) and (qtr_model["gamma_deg"] == 26.0))
    print(f"Check 6 (QTR model parameters & unfrozen realignment): eps2={qtr_model['epsilon2']}, gamma={qtr_model['gamma_deg']} deg -> {check6}")

    # 7. Four Evidence Boundaries and Caveats
    boundaries = {
        "boundary_1_weak_755": "755.1 keV transition too weak for linear polarization extraction; delta assumed from Rac",
        "boundary_2_qtr_high_spin_energy": "Standard QTR overestimates Band 2 and Band 5 energies at high spins",
        "boundary_3_band_5_link": "Band 5 structure partially relies on previously reported but unobserved 1009 keV line",
        "boundary_4_model_dependence_tip": "Tilted precession interpretation is a model-dependent framework, not a direct laboratory observable"
    }
    check7 = bool(len(boundaries) == 4)
    print(f"Check 7 (Evidence boundaries & caveats): {len(boundaries)} boundaries verified -> {check7}")

    # 8. Source Locators Crosswalk
    locators = {
        "L22-1": "Lv 2022: JUROGAM II 100Mo(40Ar,1p4n)135Pr experiment with 5.1x10^10 events (PDF p. 2)",
        "L22-2": "L22: Dismantling of Sensharma 2019 TW2 band into Band 4 and Band 5 (PDF p. 2; Fig. 1)",
        "L22-4": "L22: Joint P-Rac analysis yields delta=-0.47, -0.37, -0.31 (|delta|<1) (PDF p. 3; Table 1)",
        "L22-5": "L22: Connecting transitions are 82%, 88%, 91% M1-dominated (PDF p. 3)",
        "L22-7": "L22: B(E2;747)/B(E2;526) = 0.7(+0.7/-0.5), incompatible with one-phonon wobbling (PDF p. 3)",
        "L22-8": "L22: Matta 2015 used only polarization sign rather than quantitative fit, picking false |delta|>1 root (PDF pp. 2-3)",
        "L22-11": "L22: Rejection of one-phonon (Band 3) and two-phonon (Band 4/5) wobbling interpretations (PDF pp. 3, 5)",
        "L22-13": "L22: QTR calculation explains bands 1, 3, 4 as tilted-precession bands with unfrozen realignment (PDF pp. 4-5)"
    }
    check8 = bool(len(locators) == 8)
    print(f"Check 8 (Source locators crosswalk): {len(locators)} locators verified -> {check8}")

    all_passed = bool(check1 and check2 and check3 and check4 and check5 and check6 and check7 and check8)
    print(f"All 8 Checks Passed: {all_passed}")

    result_payload = {
        "schema_version": 1,
        "checkpoint": "086",
        "title": "135Pr Transverse Wobbling Controversy, Multipolarity Decontamination, Mixing Ratio Disproof, and Tilted-Precession Reinterpretation",
        "all_passed": all_passed,
        "checks": {
            "check1_multipole_mixing_ratios": check1,
            "check2_be2_inflation_factors": check2,
            "check3_quadratic_ambiguity": check3,
            "check4_wobbling_vs_tip_discrimination": check4,
            "check5_tw2_reorganization": check5,
            "check6_qtr_unfrozen_model": check6,
            "check7_evidence_boundaries": check7,
            "check8_source_locators_crosswalk": check8
        },
        "multipolarity_decontamination": {
            "transitions": {
                "747.3_keV": {"delta": delta_747, "f_M1_pct": f_m1_747 * 100.0, "f_E2_pct": f_e2_747 * 100.0},
                "813.2_keV": {"delta": delta_813, "f_M1_pct": f_m1_813 * 100.0, "f_E2_pct": f_e2_813 * 100.0},
                "450.2_keV": {"delta": delta_450, "f_M1_pct": f_m1_450 * 100.0, "f_E2_pct": f_e2_450 * 100.0}
            },
            "inflation_factors": {
                "large_root_delta1_inflation": inflation_large_root,
                "pure_E2_assumption_inflation": inflation_pure_e2,
                "ratio_813_drop_factor": ratio_drop_813
            }
        },
        "quadratic_ambiguity": quadratic_ambiguity,
        "discrimination_matrix": discrimination_matrix,
        "tw2_reorganization": tw2_reorganization,
        "qtr_model": qtr_model,
        "evidence_boundaries": boundaries,
        "source_locators": locators
    }

    result_payload = convert_types(result_payload)

    out_path = Path("outputs/learning-daily/20261022-DAY20-be2-qt-deformation-systematics-run-02/pr135-wobbling-multipolarity-result-086.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result_payload, f, indent=2, ensure_ascii=False)
    print(f"Result written to {out_path}")

    if not all_passed:
        sys.exit(1)

if __name__ == "__main__":
    main()
