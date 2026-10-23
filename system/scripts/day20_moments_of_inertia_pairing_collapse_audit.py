#!/usr/bin/env python3
"""Audit of Rotational Moments of Inertia and Pairing Collapse across the ND to HD Boundary.

This script audits:
1. Kinematic J^(1) and dynamic J^(2) moments of inertia definitions;
2. Rigid rotor expectation J_rig as a function of mass A and quadrupole deformation beta_2;
3. Experimental J^(1) and J^(2) profiles in 131Ce and 134Nd normal vs highly deformed bands;
4. The pairing collapse transition: jump from J/J_rig ~ 30-55% (ND) to ~88-91% (HD);
5. Dual criteria for A ~ 130 collectivity: Q0 ~ 7.2 eb plateau + J^(2) ~ 0.90 J_rig.
"""

from __future__ import annotations

import hashlib
import json
import math
from datetime import datetime, timezone
from pathlib import Path


def rigid_moment_of_inertia(a: int, beta2: float, r0_fm: float = 1.20) -> float:
    """Calculate rigid body moment of inertia in hbar^2 / MeV.

    J_rig = (2/5) * M * R0^2 * (1 + 0.315 * beta2)
    where M = A * m_N, m_N ~ 938.9 MeV/c^2.
    R0 = r0_fm * A^(1/3) fm.
    hbarc = 197.327 MeV*fm.
    In units of hbar^2 / MeV:
    J_rig / hbar^2 = (2/5) * (A * m_N / hbarc^2) * (r0_fm^2 * A^(2/3)) * (1 + 0.315 * beta2)
    = (2/5) * (938.9 / 197.327^2) * r0_fm^2 * A^(5/3) * (1 + 0.315 * beta2)
    """
    m_n = 938.92
    hbarc = 197.32698
    prefactor = (2.0 / 5.0) * (m_n / (hbarc ** 2)) * (r0_fm ** 2)  # ~ 0.013904
    j_rig = prefactor * (a ** (5.0 / 3.0)) * (1.0 + 0.3149 * beta2)
    return j_rig


def main() -> None:
    raise SystemExit("RETIRED checkpoint033: original-source identity or physical interpretation failed; use day20_observable_identity_shape033.py")
    root = Path(__file__).resolve().parent.parent.parent
    run_dir = root / "outputs/learning-daily/20261022-DAY20-be2-qt-deformation-systematics-run-02"
    run_dir.mkdir(parents=True, exist_ok=True)

    checks = []

    # -------------------------------------------------------------
    # 1. Rigid Body Benchmark Values for 131Ce (A=131) and 134Nd (A=134)
    # -------------------------------------------------------------
    # 131Ce: ND (beta2 = 0.18) vs HD (beta2 = 0.38)
    j_rig_ce_nd = rigid_moment_of_inertia(131, beta2=0.18)  # ~ 48.9 hbar^2/MeV
    j_rig_ce_hd = rigid_moment_of_inertia(131, beta2=0.38)  # ~ 52.0 hbar^2/MeV

    # 134Nd: ND (beta2 = 0.20) vs HD (beta2 = 0.36)
    j_rig_nd_nd = rigid_moment_of_inertia(134, beta2=0.20)  # ~ 51.1 hbar^2/MeV
    j_rig_nd_hd = rigid_moment_of_inertia(134, beta2=0.36)  # ~ 53.6 hbar^2/MeV

    check_j_rig = (47.0 < j_rig_ce_nd < 51.0) and (50.0 < j_rig_ce_hd < 54.0)
    checks.append({
        "name": "Rigid Rotor Reference: J_rig(131Ce) is ~48.9 hbar^2/MeV (ND) and ~52.0 hbar^2/MeV (HD)",
        "passed": check_j_rig,
        "detail": f"J_rig(Ce ND) = {j_rig_ce_nd:.2f}, J_rig(Ce HD) = {j_rig_ce_hd:.2f}"
    })

    # -------------------------------------------------------------
    # 2. 131Ce Moments of Inertia: ND vs HD
    # -------------------------------------------------------------
    # ND band (Singh 2016 Table 1, Alwaleedi 2013 Table 4.1):
    # 19/2^- -> 15/2^-: E_gamma = 642 keV (0.642 MeV), J^(1) = (19-1)/0.642 = 28.04 hbar^2/MeV
    # 23/2^- -> 19/2^-: E_gamma = 750 keV (0.750 MeV), J^(1) = (23-1)/0.750 = 29.33 hbar^2/MeV
    # J^(1) / J_rig(ND) = 28.04 / 48.9 = 57.3%
    j1_ce_nd_19 = 18.0 / 0.642
    ratio_j1_ce_nd = j1_ce_nd_19 / j_rig_ce_nd  # ~ 0.573

    # HD band (Petrache 1998 Table I, Alwaleedi 2013 Table 4.7):
    # Transition energy spacing Delta E_gamma ~ 87 keV (0.087 MeV)
    # J^(2) = 4 / Delta E_gamma = 4 / 0.087 ~ 45.98 hbar^2/MeV
    delta_eg_ce_hd = 0.087  # MeV
    j2_ce_hd = 4.0 / delta_eg_ce_hd  # ~ 45.98 hbar^2/MeV
    ratio_j2_ce_hd = j2_ce_hd / j_rig_ce_hd  # ~ 45.98 / 52.0 ~ 88.4%

    check_ce_jump = (0.50 < ratio_j1_ce_nd < 0.65) and (0.85 < ratio_j2_ce_hd < 0.92)
    checks.append({
        "name": "131Ce Pairing Collapse: J/J_rig jumps from 57.3% (ND) to 88.4% (HD)",
        "passed": check_ce_jump,
        "detail": f"ND J^(1) ratio = {ratio_j1_ce_nd*100:.1f}%, HD J^(2) ratio = {ratio_j2_ce_hd*100:.1f}%"
    })

    # -------------------------------------------------------------
    # 3. 134Nd Moments of Inertia: ND vs HD
    # -------------------------------------------------------------
    # Ground band ND (Klemme 1999 Table I):
    # 4^+ -> 2^+: E_gamma = 552 keV (0.552 MeV), J^(1) = (2*4 - 1)/0.552 = 7 / 0.552 = 12.68 hbar^2/MeV
    # 6^+ -> 4^+: E_gamma = 687 keV (0.687 MeV), J^(1) = 11 / 0.687 = 16.01 hbar^2/MeV
    # Ratio J^(1) / J_rig(ND) = 16.01 / 51.1 ~ 31.3%
    j1_nd_nd_6 = 11.0 / 0.687
    ratio_j1_nd_nd = j1_nd_nd_6 / j_rig_nd_nd  # ~ 0.313

    # yrast HD band (Petrache 1998 Table I):
    # Transition energy spacing Delta E_gamma ~ 84 keV (0.084 MeV)
    # J^(2) = 4 / 0.084 = 47.62 hbar^2/MeV
    delta_eg_nd_hd = 0.084  # MeV
    j2_nd_hd = 4.0 / delta_eg_nd_hd  # ~ 47.62 hbar^2/MeV
    ratio_j2_nd_hd = j2_nd_hd / j_rig_nd_hd  # ~ 47.62 / 53.6 ~ 88.8%

    check_nd_jump = (0.25 < ratio_j1_nd_nd < 0.40) and (0.85 < ratio_j2_nd_hd < 0.92)
    checks.append({
        "name": "134Nd Pairing Collapse: J/J_rig jumps from 31.3% (ND) to 88.8% (HD)",
        "passed": check_nd_jump,
        "detail": f"ND J^(1) ratio = {ratio_j1_nd_nd*100:.1f}%, HD J^(2) ratio = {ratio_j2_nd_hd*100:.1f}%"
    })

    # -------------------------------------------------------------
    # 4. Correlation: Electromagnetic Collectivity (Q0) vs Rotational Rigidity (J2/J_rig)
    # -------------------------------------------------------------
    # In both 131Ce and 134Nd:
    # ND band: Q0 ~ 2.5 - 3.5 eb, J/J_rig ~ 30 - 57% (paired, gamma-soft)
    # HD band: Q0 ~ 6.8 - 7.3 eb, J/J_rig ~ 88 - 90% (unpaired, near-rigid prolate)
    q0_step_ce = 7.30 / 2.58   # 2.83x
    j_step_ce = ratio_j2_ce_hd / ratio_j1_ce_nd  # ~ 1.54x

    check_dual_criteria = (q0_step_ce > 2.5) and (j_step_ce > 1.4)
    checks.append({
        "name": "Dual Collectivity Criteria: HD transition couples 2.83x Q0 step with 1.54x rotational rigidity enhancement",
        "passed": check_dual_criteria,
        "detail": f"Q0 step = {q0_step_ce:.2f}x, J_ratio step = {j_step_ce:.2f}x"
    })

    all_passed = all(c["passed"] for c in checks)

    result_data = {
        "kind": "Rotational moments of inertia and pairing collapse audit across ND to HD boundary",
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "theoretical_framework": {
            "kinematic_moment_formula": "J^(1)(I) = (2*I - 1) / E_gamma(I -> I-2)",
            "dynamic_moment_formula": "J^(2)(I) = 4 / Delta E_gamma = 4 / [E_gamma(I+2) - E_gamma(I)]",
            "rigid_body_formula": "J_rig = (2/5) * M * R0^2 * (1 + 0.315 * beta_2)"
        },
        "nuclear_case_studies": {
            "131Ce": {
                "rigid_body_reference": {
                    "ND_beta2_0p18": round(j_rig_ce_nd, 2),
                    "HD_beta2_0p38": round(j_rig_ce_hd, 2)
                },
                "normal_deformed_band": {
                    "transition": "19/2^- -> 15/2^- (642 keV)",
                    "J1_hbar2_per_MeV": round(j1_ce_nd_19, 2),
                    "fraction_of_J_rig": round(ratio_j1_ce_nd * 100.0, 1),
                    "pairing_status": "Strong static pairing (Delta_p, Delta_n ~ 1.0 MeV)"
                },
                "highly_deformed_band": {
                    "transition_spacing_Delta_E_gamma_keV": 87.0,
                    "J2_hbar2_per_MeV": round(j2_ce_hd, 2),
                    "fraction_of_J_rig": round(ratio_j2_ce_hd * 100.0, 1),
                    "pairing_status": "Pairing collapse (Coriolis anti-pairing + blocking)"
                }
            },
            "134Nd": {
                "rigid_body_reference": {
                    "ND_beta2_0p20": round(j_rig_nd_nd, 2),
                    "HD_beta2_0p36": round(j_rig_nd_hd, 2)
                },
                "normal_deformed_ground_band": {
                    "transition": "6^+ -> 4^+ (687 keV)",
                    "J1_hbar2_per_MeV": round(j1_nd_nd_6, 2),
                    "fraction_of_J_rig": round(ratio_j1_nd_nd * 100.0, 1),
                    "pairing_status": "Strong ground state pairing"
                },
                "highly_deformed_yrast_band": {
                    "transition_spacing_Delta_E_gamma_keV": 84.0,
                    "J2_hbar2_per_MeV": round(j2_nd_hd, 2),
                    "fraction_of_J_rig": round(ratio_j2_nd_hd * 100.0, 1),
                    "pairing_status": "Near-rigid rotation (J2/J_rig = 88.8%)"
                }
            }
        },
        "physical_synthesis": [
            "1. Macroscopic Signature of Pairing Collapse: Across the ND-to-HD boundary, J/J_rig jumps from ~30-57% to ~88-89%, providing clear macroscopic evidence of Coriolis anti-pairing and quasiparticle blocking.",
            "2. Dual Observable Certification: Superdeformed/highly-deformed structures in A ~ 130 are uniquely certified by the simultaneous presence of: (a) an intrinsic quadrupole plateau Q0 ~ 6.8-7.3 eb, and (b) a constant, unperturbed dynamic moment of inertia J^(2) ~ 0.88-0.90 J_rig.",
            "3. Contrast with Backbending in ND Bands: In ND bands, band-crossing alignments cause erratic oscillations in J^(2) (often exceeding 100 hbar^2/MeV), reflecting abrupt changes in the pairing field, whereas HD bands exhibit a remarkably smooth J^(2) trajectory."
        ],
        "checks": checks,
        "all_checks_passed": all_passed
    }

    out_file = run_dir / "moments-of-inertia-pairing-collapse-result-020.json"
    out_file.write_text(json.dumps(result_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Audit completed: all_checks_passed = {all_passed}")
    print(f"Results written to {out_file.relative_to(root)}")


if __name__ == "__main__":
    main()
